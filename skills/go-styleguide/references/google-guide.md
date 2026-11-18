# Google Go guidance and project adaptations

## Source and attribution

Adapted from **Go Style** by Google contributors, accessed 18 November 2026.
The four documents below are pinned to the same `google/styleguide` revision.
The [published guide](https://google.github.io/styleguide/go) may change.

- [Overview](https://github.com/google/styleguide/blob/47cbd91d1c65a447f233c3fd5379dc800b2ecd7a/go/index.md): defines the status of each document **at Google**.
- [Style Guide](https://github.com/google/styleguide/blob/47cbd91d1c65a447f233c3fd5379dc800b2ecd7a/go/guide.md): canonical and normative. Prefer clarity and simplicity over concision; use the least machinery that solves the problem.
- [Style Decisions](https://github.com/google/styleguide/blob/47cbd91d1c65a447f233c3fd5379dc800b2ecd7a/go/decisions.md): normative but not canonical. It records settled review decisions and their exceptions.
- [Best Practices](https://github.com/google/styleguide/blob/47cbd91d1c65a447f233c3fd5379dc800b2ecd7a/go/best-practices.md): neither normative nor canonical. These are recommendations for particular situations.

The [repository licensing notice](https://github.com/google/styleguide/blob/47cbd91d1c65a447f233c3fd5379dc800b2ecd7a/README.md#licensing)
licenses upstream text under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
and upstream code samples under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
This selection paraphrases the text and adds project-specific guidance. All Go
examples below are original; none were copied from upstream. Keep attribution
when redistributing the adaptation.

## Names and formatting

The Guide's *Formatting*, *MixedCaps*, *Line length* and *Naming* sections
require `gofmt` output and set no fixed line length. Let the formatter choose
indentation and alignment. Refactor an unreadable expression rather than
breaking every long line at a column limit. Under Decisions, keep standard
library imports first, then other imports, with separate groups for protobuf
and side-effect imports when present. `gofmt` sorts within groups; it does not
infer those categories. Keep intentional side-effect imports.

- Choose a short lowercase package name that explains what callers import;
  avoid a `util` package for an unrelated helper. Omit names repeated by the
  package qualifier: `checkpoint.Cursor` rather than `checkpoint.CheckpointCursor`.
- Use `MixedCaps` for exported multiword identifiers and `mixedCaps` for
  unexported ones, including constants. Keep common initialisms intact:
  `recordID`, not `recordId`. A getter can be `Offset`, not `GetOffset`.
  Don't apply identifier rules to filenames, generated APIs or wire keys.
- A short local `i` or `err` can be clearer than a long name. Give a value
  crossing multiple steps a name that describes its role (e.g., `nextOffset`).
  Use a short, consistent receiver abbreviation (`c` for `Cursor`), not `self`.

## Exported contracts and errors

**Decisions — Commentary and Errors.** Put a package comment directly above
one package clause. Document exported declarations and methods; start a doc
comment with the name (an article may precede it) and attach it directly to
the declaration. Document unobvious unexported behavior too. A signature can
specify `uint64` but cannot say whether that number is a byte offset or a
record count. Explain the part the caller cannot infer.

Use `error` as the last result for an operation that can fail. Return a nil
error on success, not a typed nil pointer inside an `error` interface. Handle
an error or propagate it; don't panic for ordinary bad input or hide a failure
in a valid zero result. Other results are unspecified on error unless the API
says otherwise (a reader may return both bytes and an error). Prefer `(T, bool)`
for an ordinary lookup miss. Handle the failing path first and omit an `else`
after its `return`. Write composable error strings without initial capitals
(except names and acronyms) or trailing punctuation.

**Best Practices — Error handling and Documentation.** Add context only when
it identifies something new. Use `%w` with `fmt.Errorf` when callers should
be able to recognize a cause with `errors.Is` or inspect its type with
`errors.As`; `%v` formats the text without preserving that chain. Exposing an
underlying storage error is an API choice, not a formatting improvement. Name
significant errors in the doc comment rather than making callers match their
text. Usually return the error instead of both logging and returning it.
Document required cleanup, mutation, concurrency and cancellation behavior
where they affect correct use, not as a checklist of boilerplate.

## Choosing the boundary

**Decisions — Interfaces and Generics.** Delay abstraction until there is a
real caller. A consumer normally defines the smallest interface it needs or
uses an existing one. A producer can publish an interface when the protocol
itself is the product. Returning concrete types is a useful default, not a
ban on returning interfaces such as `error`. Use type parameters when real
uses at different types share an algorithm, not simply because they might one
day. Document an exported generic API and show a motivating runnable example.

### One operation, not a service

Suppose a checkpoint comes from a file in production and a buffered network
stream in an importer. `func Read(f *os.File) (uint64, error)` would require
both callers to supply a file even though the operation needs only bytes. No
new `CheckpointSource` interface, storage package or reader struct is needed:

```go
// Package checkpoint reads byte offsets from a checkpoint stream.
package checkpoint

import (
	"encoding/binary"
	"io"
)

// Read consumes one eight-byte, big-endian offset from r. At end of stream,
// it returns io.EOF if no bytes were read or io.ErrUnexpectedEOF for a partial
// offset. It does not close r.
func Read(r io.Reader) (uint64, error) {
	var buf [8]byte
	if _, err := io.ReadFull(r, buf[:]); err != nil {
		return 0, err
	}

	return binary.BigEndian.Uint64(buf[:]), nil
}
```

Here the input is an established interface describing behavior; the result is
one concrete number. A zero offset is valid. Returning the read error unchanged
preserves the caller's ability to distinguish an empty stream from truncation.
This shorter wrapper loses that distinction:

```go
func readOffset(r io.Reader) uint64 {
	offset, _ := Read(r)
	return offset
}
```

For an empty stream, a truncated record and an encoded zero, `readOffset`
returns the same value. Keep the error result unless the caller has an
explicit policy that makes these outcomes equivalent.

### State belongs with its invariant

In the same package, use a receiver if an actual caller needs to keep its
position monotonic across updates. A stateless `Read` doesn't belong on this
type: reading a number and accepting it as a new position are different acts.
This example uses the standard `errors` package.

```go
// ErrBackward means that an offset precedes the cursor's current position.
var ErrBackward = errors.New("offset precedes cursor")

// A Cursor tracks a byte offset. Its zero value starts at offset zero.
type Cursor struct {
	offset uint64
}

// Advance moves c to next and returns the number of bytes advanced. If next
// is smaller than the current offset, it returns 0 and ErrBackward without
// moving c. Repeating the current offset succeeds with a distance of zero.
func (c *Cursor) Advance(next uint64) (uint64, error) {
	if next < c.offset {
		return 0, ErrBackward
	}

	distance := next - c.offset
	c.offset = next

	return distance, nil
}
```

**Project preference:** the guard ends before the success calculation, and the
assignment stands apart from the return. These blank lines do not constitute a
Google rule. Keep the error check next to the operation it tests, and preserve
the order of validation and mutation; whitespace must not change the contract.

### Same element type in, same element type out

Start concrete if the only caller uses offsets. If two existing callers take
the last recorded offset (`[]uint64`) and the last shard name (`[]string`) with
a fallback, a small Go 1.18+ helper can express their shared rule. In contrast,
`func lastOr(values []any, fallback any) any` loses the result type, allows an
unrelated fallback, and cannot take `[]string` directly. No method is called on
an element, so a behavior interface or a `comparable` constraint adds nothing.

```go
func lastOr[T any](values []T, fallback T) T {
	if len(values) == 0 {
		return fallback
	}

	return values[len(values)-1]
}
```

`lastOr([]uint64{4, 0}, uint64(9))` returns `uint64(0)`, not the fallback;
`lastOr([]string(nil), "local")` returns `"local"`. Both nil and empty slices
mean no elements. Don't introduce a type parameter into a module targeting an
older language version or export a helper solely to share it with tests.

## Applying the guide outside Google

Use the existing package, its supported Go version and its configured formatter
and checks. Google's presubmit and internal libraries are not prerequisites.
Check callers before changing exported names, pointer/value receivers, error
identity, ownership or serialized data. For example, nil and empty slices both
have length zero but can produce different JSON. A style-only edit must not
silently change that output. When reporting a finding, say which caller would
be affected or which documented convention it violates.
