# Google Swift checklist and provenance

## Upstream baseline

- Use descriptive `.swift` filenames; name single-type files after their type and conformance extensions with a type-plus-protocol name.
- Import needed modules explicitly; keep imports grouped and sorted as described by the guide.
- Use spaces, two-space block indentation, and a 100-column target, honoring upstream exceptions for imports, generated code, and indivisible text.
- Avoid statement semicolons. Keep separate statements readable; a short single-statement block may remain inline.
- Wrap argument lists consistently; preserve Swift syntax and meaningful literal content.
- Keep switch cases aligned with the switch and indent their bodies.
- Organize declarations logically and keep related overloads together.
- **Naming:** Google's *Apple's API Style Guidelines* section incorporates the
  [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/).
  Read names at the call site. Use labels to distinguish roles or units; omit
  a label only when the base name and argument make its meaning clear. Use
  access control rather than a naming convention to hide implementation.
- **Optional Types / Error Types:** use an optional for expected absence or
  one obvious failure, not a sentinel. Use `throws` when callers need to
  distinguish errors. Do not erase that distinction with `try?` as cleanup.
  Document a force unwrap's safety invariant unless it is obvious in context;
  test-only code has exceptions.
- **Documentation Comments:** use `///` and a one-sentence summary ending in
  a period for public/open declarations and their public/open members. The
  [pinned documentation section](https://github.com/google/swift/blob/79459b39f2ab0330ee05a90f20c3f716d8406b24/index.md#documentation-comments)
  gives exceptions for obvious enum cases, overrides, protocol implementations,
  tests, and extensions. Do not copy an inherited comment; document changed
  behavior. Explain nonobvious associated values.
- Use `- Parameter name:` for one parameter or a grouped `- Parameters:` list
  for several. Use the local parameter names, not the external labels. Follow
  with `- Returns:` and, for a throwing operation, `- Throws:` describing the
  failure conditions. Omit parameter or result tags only when the summary
  already covers them fully; do not invent a result for `Void`.
- **Early exits / Vertical Whitespace:** Google uses `guard` to place an
  exceptional exit beside its condition and keep the success path unnested.
  It permits blank lines to separate logical groups of statements; it does
  not require a blank line after every `guard` or mutation.

These are paraphrased reminders, not a replacement for the full guide's exceptions.

## Source

- Publisher: Google, drawing on Apple's Swift API conventions.
- Read on: 2026-11-17.
- [Published guide](https://google.github.io/swift/).
- [Pinned guide source](https://github.com/google/swift/blob/79459b39f2ab0330ee05a90f20c3f716d8406b24/index.md).
- Revision: `79459b39f2ab0330ee05a90f20c3f716d8406b24`, `gh-pages`, 2019-06-05.
- [Branch license](https://github.com/google/swift/blob/79459b39f2ab0330ee05a90f20c3f716d8406b24/LICENSE.txt): Apache 2.0 with the displayed runtime-library exception. Do not assume the separate google/styleguide repository's license applies here.

This skill is an independently written workflow and short paraphrased checklist, not an official Google package. Full upstream text is not bundled. Project precedence, API preservation, incremental edits, current-tool verification, and modern Swift compatibility are explicit adaptations of this skill.

## Applying old guidance to current code

The revision date is material: check current compiler and library requirements before interpreting old examples as current API advice. A project formatter can implement a chosen formatting profile without checking API design or semantic safety. A passing formatter alone is insufficient evidence of full guide compliance.

## Worked examples

These examples are original to this package. The choices about ownership,
abstraction, and blank lines below are project preferences, not additional
Google rules.

### Decide what assignment means

A reader wants to preview progress without moving their saved place. The
following contrast has two problems: `update(8)` does not identify the unit,
and assigning a class reference makes both names refer to the same tracker.

```swift
final class Tracker {
  private var page = 0

  func update(_ number: Int) -> Int? {
    if number > page {
      let change = number - page
      page = number
      return change
    } else {
      return nil
    }
  }
}

let saved = Tracker()
let preview = saved
let change = preview.update(8)  // Also moves the saved tracker.
```

Here the invariant is that the recorded page only moves forward. A value with
one `mutating` method protects it, and its integer state is independent after
assignment. For a new API, name the action and give the integer a role at the
call site. The documentation uses `page`, the parameter's name inside the
method; the caller sees `toPage`.

```swift
/// A reader's furthest recorded page, measured from zero before reading.
public struct ReadingProgress {
  private var lastPage = 0

  /// Creates progress for a reader who has not started.
  public init() {}

  /// Records a later page and reports how far the reader advanced.
  ///
  /// - Parameter page: The one-based destination page.
  /// - Returns: The number of pages advanced, or `nil` without changing
  ///   progress if `page` is not later than the recorded page.
  public mutating func advance(toPage page: Int) -> Int? {
    guard page > lastPage else { return nil }

    let pagesAdvanced = page - lastPage
    lastPage = page

    return pagesAdvanced
  }
}

var savedProgress = ReadingProgress()
var previewProgress = savedProgress
let previewAdvance = previewProgress.advance(toPage: 8)  // 8.
let savedAdvance = savedProgress.advance(toPage: 3)  // 3, not nil.
```

Keep related checks together; separate the early exit from normal work and
the completed state update from the return with a blank line. Follow the
project's configured formatter if it differs; do not split a natural
single-expression return just to add spacing.

If two views must observe *one* live reading session instead, shared identity
can justify a class. Say who retains that session and when it ends; a class
alone does not synchronize concurrent access. Nor does a struct promise deep
copies of class instances stored inside it. Do not switch an existing API
between these designs as a style fix.

### Generalize an operation, not its owner

If one caller needs the next chapter marker, an existing array's
`first(where:)` is enough. If a reader and a player both need the same
selection rule for page numbers and timestamps, a function in the existing
module can name it. `Comparable` supplies `>`; the repeated `Position`
keeps the threshold, markers, and optional result in the same domain.

```swift
/// Returns the first entry in `markers` strictly after `position`, in input
/// order, or `nil` if none qualifies.
func nextMarker<Position: Comparable>(
  after position: Position,
  in markers: [Position]
) -> Position? {
  return markers.first { $0 > position }
}

let nextPage = nextMarker(after: 5, in: [5, 12, 8])  // 12, not 8.
let nextTimestamp = nextMarker(after: 1.5, in: [0.5, 2.25])  // 2.25.
```

There is no mutable owner here. Neither `Any` plus a cast nor a new
`MarkerProvider` protocol improves these calls. Introduce a protocol when a
consumer actually depends on behavior supplied by different implementations;
if it just needs one operation, consider passing a function instead.
