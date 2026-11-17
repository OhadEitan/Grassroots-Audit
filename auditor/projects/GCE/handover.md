# GCE auditor assignment

Source: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`. Published name: Grassroots Contract Examples. Paper keys: none presented.

Status: queued; no substantive coverage claimed and no active dedicated session. Begin with auditor/roster.md, project-structure.json, coordination.md and current main rules. Pin current papers and relevant code before review. Preserve source paths and review the project's papers and code together. Do not infer an unpresented paper's key or version. Record exact scope and a handover after each bounded work unit.

## PR #27 and PR #28 proposals — 2026-11-17

Contributor: Claude for Nimrod Talmon (GCE). Audit main base: `ebfbaba47f0fe79640289df26c80ce348b4375cf`. Public GLP inspected at `e817b136f15a4c9d10cca4f105b86a7636ed7fa7`.

PR #27 head `da764b4829d4e0b7210d11469097e03891cb5903` proposes stale-report detection and rename rules. Review [#5939538357](https://github.com/udi-shapiro/Grassroots-Audit/pull/27#pullrequestreview-5939538357) requests changes: `ISSUES.md` is falsely treated as a report, and a plain report move does not preserve the original path/finding identifier. Actual executed check: the submitted script in an isolated fixture with root `ISSUES.md` exited 1 and printed `ISSUES.md: gone at GLP ?`. Source inspection: the pinned five-column `calculus/NAMES.txt` supports the proposed rename lookup. No full GLP/papers checkout run was claimed.

PR #28 head `641d4a705ce9658f777a20c2a80d564201d523ad` proposes Website Finding 1. Public source inspection supports the underlying presentation mismatch; review [#5939560673](https://github.com/udi-shapiro/Grassroots-Audit/pull/28#pullrequestreview-5939560673) requests corrected totals, Website auditor ownership with GCE attribution preserved separately, and regenerated status. The site was not executed.

Next: inspect new heads and discussion before responding; do not merge either unchanged. For PR #27, require a non-report Markdown regression and durable old-identifier alias semantics. For PR #28, require 29 reports / 17 findings / one unanswered and nine unresolved / eight verified corrected throughout the publication.

## PR #29 Calculus-tool proposal — 2026-11-17

PR [#29](https://github.com/udi-shapiro/Grassroots-Audit/pull/29), head `6a0ad185ec398e5cbe45e3597fe845c0df7f9556`, proposes a medium-severity finding at `calculus/tools/SAS-WRITING.txt.md`, attributed to Claude for Nimrod Talmon (GCE).

Source inspection at public GLP `e817b136f15a4c9d10cca4f105b86a7636ed7fa7` supports the concrete gap: SAS-WRITING requires `gr/` to say the same as `rev/` and forbids substantive changes; Friendship:1 adds a knows-each-other condition and changes trust to an undertaking; inspection of all 21 Python tools under `calculus/tools/` found no direct rev/gr equivalence check. No Calculus tool was executed.

Review [#5939623857](https://github.com/udi-shapiro/Grassroots-Audit/pull/29#pullrequestreview-5939623857) requests changes: update public totals relative to current main, resolve project ownership because the accepted roster has no Calculus project and `Auditor: none` is invalid, preserve GCE attribution separately, and regenerate status. Do not merge unchanged.
