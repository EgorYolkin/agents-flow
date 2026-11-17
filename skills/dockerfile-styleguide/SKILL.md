---
name: dockerfile-builder
description: Create, review, fix, and optimize production Dockerfiles and project-specific .dockerignore files with secure defaults, efficient BuildKit caching, small runtime images, and concise human comments. Use this skill whenever the user asks to containerize an application, create or improve a Dockerfile, reduce image size or build time, add multi-stage builds, configure BuildKit secrets or caches, harden a container image, troubleshoot Docker build layers, or review Docker image security—even if they ask only to “dockerize” a project and do not explicitly mention Dockerfile best practices.
---

# Dockerfile Builder

Create a Docker setup that is boring, maintainable, secure by default, and optimized for the actual project. Optimize where the benefit is concrete; do not turn a small application into an infrastructure framework.

## Workflow

1. Inspect the repository before writing anything:
   - identify the language, runtime, framework, package manager, lockfiles, build command, start command, output artifacts, listening port, and writable runtime paths;
   - read existing Dockerfile, Compose, CI, deployment, and ignore files;
   - check the runtime version from authoritative project files such as `.tool-versions`, `.nvmrc`, `go.mod`, `pyproject.toml`, or CI configuration;
   - determine whether native libraries, CGO, browser binaries, certificates, locales, fonts, or system packages are required.
2. If a critical fact cannot be inferred, ask a focused question rather than silently inventing it. For low-risk details, make a conventional choice and state the assumption.
3. For creation or implementation requests, create or update both `Dockerfile` and the build context’s `.dockerignore`; preserve unrelated user rules in existing files. For review, explanation, or troubleshooting requests, do not edit unless the user asks for fixes.
4. Validate the result when tools are available:
   - build the intended target with BuildKit/buildx;
   - run the container or its relevant smoke test;
   - inspect final image size, configured user, entry command, and obvious secret leakage;
   - use a Dockerfile linter or vulnerability scanner if the project already provides one.
5. Report changed files, important choices, the build command, and any assumptions or residual risks. Do not claim the image builds if it was not built.

## Decision order

Make decisions in this order so size optimizations do not break correctness:

1. runtime compatibility and correct process behavior;
2. security and secret handling;
3. reproducibility and maintainability;
4. build-cache efficiency;
5. final image size.

Prefer the simplest design that satisfies these goals. A single-stage image is acceptable when another stage would not remove toolchains, dependencies, or artifacts from the runtime image.

## Base images

- Use a trusted, maintained source: normally a Docker Official Image, Verified Publisher, Docker Hardened Image, or an organization-approved internal base.
- Never rely on an implicit or explicit `latest` tag. Select a concrete supported runtime and OS variant, for example `python:3.13-slim-bookworm` or `alpine:3.21`.
- Prefer a readable version tag plus an immutable digest for production or supply-chain-sensitive builds:

  ```dockerfile
  FROM python:3.13-slim-bookworm@sha256:<verified-digest>
  ```

  Never invent a digest. Resolve and verify it from the registry, or leave a clear note that the user must pin it. Explain that digest pinning requires automated update/rebuild tooling so security fixes are not frozen forever.
- Avoid a general-purpose full distribution when an official runtime `slim`, Alpine, distroless, or `scratch` image meets the real requirements. “Smallest” is not automatically “best.”
- Choose variants deliberately:
  - use Alpine when the workload is compatible with musl/BusyBox; it is often effective for static Go binaries and simple runtimes;
  - prefer a glibc-based slim image for Python, Node, Ruby, or native dependencies unless Alpine compatibility is known and tested;
  - consider distroless or `scratch` for a well-understood final artifact when the team can operate and debug a shell-less image;
  - with `scratch`, explicitly account for CA certificates, time-zone data, passwd/group data, and dynamic libraries;
  - for Go with CGO, do not assume an Alpine or `scratch` runtime is compatible with a glibc-linked binary.
- Keep builder and runtime image versions compatible. Do not copy shared libraries across incompatible distributions casually.

## Multi-stage builds

- Use named stages such as `deps`, `build`, `test`, and `runtime` only when each has a clear purpose.
- Keep compilers, headers, package managers, source code, test tooling, and development dependencies out of the final stage.
- Copy only the required runtime artifacts from earlier stages. Avoid `COPY --from=build / /` and other broad transfers.
- Build and test in an earlier stage when appropriate, but keep the default production target lean.
- Use `COPY --from=... --chown=<uid>:<gid>` to set ownership without a later recursive `chown` layer.

## Build cache and layers

- Order instructions from stable to frequently changing. Copy dependency manifests and lockfiles before application source, install dependencies, then copy the source and build it.
- Use lockfile-aware deterministic commands such as `npm ci`, `pnpm install --frozen-lockfile`, `pip` with locked requirements, or the ecosystem’s equivalent. Never delete a valid lockfile to make a build pass.
- Each Dockerfile instruction creates a cache boundary. Combine commands when they form one atomic operation—especially package index update, install, and cleanup—but do not create unreadable mega-`RUN` instructions merely to minimize layer count.
- Use BuildKit cache mounts for expensive disposable caches when they provide a real benefit:

  ```dockerfile
  RUN --mount=type=cache,target=/root/.cache/pip \
      pip install -r requirements.txt
  ```

  Adjust cache paths, ownership, and `sharing` mode to the package manager. The build must remain correct if the cache is empty or removed.
- Use bind mounts in build steps only when their added complexity clearly improves cache behavior and the mounted files do not need to persist in the layer.
- Do not add cache mounts or extra stages to tiny builds where they make the Dockerfile harder to understand without measurable value.

## Package installation

- Install only runtime packages that the application needs.
- On Debian/Ubuntu, keep update and install together, avoid recommended extras when appropriate, and remove apt lists in the same instruction:

  ```dockerfile
  RUN apt-get update \
      && apt-get install -y --no-install-recommends ca-certificates \
      && rm -rf /var/lib/apt/lists/*
  ```

- On Alpine, use `apk add --no-cache`.
- Do not run a blanket distribution upgrade during the image build. Rebuild regularly from maintained, updated base images instead.
- Do not install `sudo`, SSH daemons, editors, shells, network tools, or debugging packages in a production image unless the workload genuinely requires them.
- Keep build-only OS packages in a builder stage rather than installing and removing them in the runtime stage.

## COPY, ADD, paths, and ownership

- Use `COPY` for normal local files and for artifacts from other stages. It is explicit and predictable.
- Do not treat `ADD` as categorically forbidden. Use it only when deliberately using a documented feature such as verified remote retrieval or local archive extraction; otherwise use `COPY`. For remote artifacts, require integrity verification such as `ADD --checksum` or fetch and verify in an isolated builder stage.
- Use an absolute `WORKDIR`; do not emulate it repeatedly with `RUN cd ...`.
- Prefer narrow, explicit copies over `COPY . .` when practical. If `COPY . .` is appropriate, ensure `.dockerignore` is strict first.
- Use `COPY --chown` and, when useful, `--chmod` instead of broad follow-up permission changes.
- Never use world-writable permissions such as `chmod 777` as a convenience fix.

## Non-root runtime

- Run the final application as a non-root, unprivileged user unless the workload has a documented reason not to.
- Reuse the official image’s non-root account when it has suitable ownership and a stable contract. Otherwise create a dedicated system user/group without login shell or unnecessary home directory.
- Prefer a stable numeric UID/GID (commonly above 10000 for custom users) when volume ownership or platform policy depends on it. Use names for readability and numeric ownership where cross-image resolution matters.
- Complete package installation and privileged filesystem setup before `USER`, then switch once near the end. Avoid switching between root and non-root repeatedly.
- Ensure the user can read application files and write only to required paths. Do not make the whole application tree writable.
- Remember that non-root is defense in depth, not complete isolation. Runtime controls such as dropping capabilities, `no-new-privileges`, a read-only root filesystem, seccomp/AppArmor, and narrow writable mounts usually belong in Compose, Kubernetes, or the deployment platform—not in the Dockerfile. Recommend them when relevant, but do not generate unrelated deployment configuration unless requested.
- The desired user is **unprivileged**, not “privileged.” Never recommend `--privileged` for an ordinary application container.

## BuildKit and secrets

- Put `# syntax=docker/dockerfile:1` on the first line when using modern Dockerfile features.
- Use modern `docker buildx build ...` or `docker build ...` on a current Docker installation. BuildKit is already the default in modern Docker Desktop and Docker Engine; mention `DOCKER_BUILDKIT=1` only for older compatible installations, not as a permanent requirement.
- Never pass secrets through `ARG`, `ENV`, command-line substitutions embedded in a `RUN`, or copied credential files. Those values can leak through metadata, history, cache, logs, or layers.
- Use a narrowly scoped BuildKit secret mount:

  ```dockerfile
  RUN --mount=type=secret,id=npmrc,target=/root/.npmrc,required=true \
      npm ci
  ```

  Build with, for example:

  ```sh
  docker buildx build --load --secret id=npmrc,src="$HOME/.npmrc" -t app:local .
  ```

- Use `RUN --mount=type=ssh` for SSH-agent access to private Git dependencies. Do not copy private keys into the image. Verify remote host keys rather than disabling host-key checks.
- Do not bake runtime secrets into an image at all; inject them through the runtime platform.

## Process behavior

- Use exec/JSON form for the main process so it receives signals directly:

  ```dockerfile
  CMD ["node", "dist/server.js"]
  ```

- Use `ENTRYPOINT` when the image has a fixed executable and `CMD` for its default arguments. Use `CMD` alone when users should easily replace the whole command.
- If an entrypoint script is truly needed, keep it small and end with `exec "$@"`. Do not add a wrapper merely for aesthetics.
- Ensure PID 1 handles termination and reaps children. Add an init process only when the application cannot do this itself; prefer the runtime’s `--init` where suitable.
- Set `EXPOSE` only for ports the process actually listens on; it documents the port but does not publish it.
- Add `HEALTHCHECK` only when the image can perform a meaningful, cheap, bounded local check without installing a large utility solely for that purpose. In orchestrated environments, let platform probes own health behavior when that is the established convention.

## `.dockerignore`

Create or update `.dockerignore` for the actual build context. Start from project evidence rather than blindly pasting a universal template.

Usually exclude:

```dockerignore
.git
.gitignore
.env
.env.*
*.pem
*.key
*.log
.DS_Store
.idea
.vscode
coverage
.tmp
tmp
```

Also exclude ecosystem-specific local dependencies and build artifacts when they are recreated in the image, such as `node_modules`, `.venv`, `venv`, `__pycache__`, `.pytest_cache`, `dist`, `build`, `target`, or `bin`.

Apply these safeguards:

- never exclude files the Dockerfile needs, including dependency lockfiles or intentionally copied artifacts;
- use negation rules where a broad pattern would hide required example/config files;
- account for monorepos and non-root build contexts—the relevant `.dockerignore` belongs at the context root;
- when multiple Dockerfiles use distinct contexts, consider Dockerfile-specific ignore files such as `Dockerfile.production.dockerignore` if that is clearer;
- understand Docker’s special handling: the Dockerfile and applicable `.dockerignore` are still sent to the builder even if ignore patterns match them, but Docker does not make them available to `COPY` or `ADD`; do not rely on ignore rules to suppress their transfer;
- treat `.dockerignore` as protection against accidental context transfer, not as a secret-management system.

## Security and supply chain review

Check for these issues before finishing:

- trusted and supported base image;
- no `latest` or unbounded base reference;
- digest pinning considered according to the project’s update process;
- no credentials, tokens, private keys, or sensitive `.env` data in context or layers;
- non-root final `USER` and narrow file permissions;
- no unnecessary packages, setuid helpers, daemon socket, or privileged assumptions;
- final stage contains only runtime requirements;
- dependency lockfiles are used and security updates are not permanently frozen;
- remote downloads are versioned and integrity-checked;
- main process receives stop signals correctly;
- the image can be rebuilt regularly and scanned in CI.

For higher-assurance pipelines, recommend rather than automatically implement: vulnerability scanning, SBOM and provenance attestations (`docker buildx build --sbom --provenance`), image signing, digest update automation, registry policies, and runtime hardening. Keep these out of a simple Dockerfile unless the user’s environment calls for them.

## Comments and presentation

- Write concise, natural comments that explain non-obvious intent or tradeoffs: why dependency files are copied first, why a runtime base was chosen, why a permission is needed, or why a secret mount is used.
- Do not narrate obvious syntax (`# Copy files`, `# Set workdir`) and do not fill the file with tutorial prose.
- Match the repository’s language and tone when evident; otherwise use clear English comments.
- Group the Dockerfile into visually coherent stages. Add a stage comment only when it explains purpose or a non-obvious tradeoff; avoid decorative banners unless the repository already uses them.
- Keep formatting idiomatic: uppercase instructions, consistent continuation indentation, and one logical concern per block.

## Final response

After making changes, provide:

1. paths created or changed, or explicitly state that the review made no edits;
2. a short explanation of base image, stages, cache strategy, runtime user, and `.dockerignore` choices relevant to the request;
3. the exact BuildKit/buildx command and, if useful, a minimal run command;
4. validation performed and its result;
5. assumptions, unverified digests, or environment-specific follow-ups.

Do not overwhelm the user with every theoretical optimization. Surface only decisions that affect correctness, security, maintenance, or measurable build/runtime behavior.
