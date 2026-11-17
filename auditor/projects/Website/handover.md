# Published second core sweep — 2026-11-12

[PR #9](https://github.com/udi-shapiro/Grassroots-Audit/pull/9) is merged as `0b5b8781b6025f8c7e8fb4fbded6a7936ba005fc`; all 16 publication file blobs were checked against the reviewed local contents. Published totals: **13 reports, nine findings, six unanswered**. Two new findings; three corrections independently verified, with Website's fix integrated and GSC's two source fixes awaiting integration into the observed GLP main. GSC's revised published paper is verified. The 72 selected existing tests passed; broader tests and full two-agent/phone execution remain outside this batch.

The exact roster, original/rebuilt PDFs, checks, results and handovers are preserved on GPT-Auditor. The working and execution branches were not merged into main. No further user approval was needed. The next work is the unresolved proof/runtime coverage and verification of new responses, as recorded below; no background monitoring or persistent project session has been started. Earlier “prepared” checkpoints below are retained history, superseded by this publication record.

# Website: current handover, second core sweep

Date: 2026-11-12
Sources: GLP `f68fbcbc3ef91b9707037ef7e5dfdb302acd1458`, papers `f4ae6121866387641f2941e3e9bf46e5fd964e7d`. The Website correction additionally uses main `66732717819d4d200070c60ac2a46d6b2228131a`.

Read the latest coordination/stages record and main reports before acting. This is a bounded scope performed in the current coordination conversation; no persistent project session or monitor exists.

Coverage: Current map and all 64 unchanged owner headers; old cache reproduction and new correction controls.

Findings/status: Cache Finding 1 is verified resolved on main 66732717819d4d200070c60ac2a46d6b2228131a, source blob 80840182bd3b03efc205e975293be16507e5924a. Answer preserved and merged in PR #6.

Next: Check relevant future changes; no live server/real LaTeX build was executed by the cache fixture. Website ownership transfer is complete.

Evidence: auditor/evidence/core-20261112 and auditor/checks/core-20261112. Actual PDF bytes are permanently preserved on this branch; runtime runs are 43304380799 (typed cycle and 72 tests), 43305549939 (fixed race fixture), 43307926679 (fixed merge fixture). Keep mathematical arguments distinct from runtime observations and bounded auditor models. Check the latest stages record for this batch's publication status.

Udi authorised continuing known work without routine go-aheads; collect genuinely necessary approvals at a concrete end-of-sweep boundary. Preserve attributed answers and independently verify corrections. Never merge GPT-Auditor into main.

## Proposed Website Finding 1 — 2026-11-17

PR [#28](https://github.com/udi-shapiro/Grassroots-Audit/pull/28), head `641d4a705ce9658f777a20c2a80d564201d523ad`, proposes a low-severity finding at `servers/peoplesweb/web/index.html.md`, attributed to Claude for Nimrod Talmon (GCE).

Source inspection at public GLP `e817b136f15a4c9d10cca4f105b86a7636ed7fa7` supports the claim: `index.html` lines 274–280 labels every non-live contract “Not compiled” and says no platform was printed; line 1071 says “No app yet”; Ads, Auction and Networked-Organisation manifests explicitly state that they are parametric and intentionally have no realisation/platform; `build.py` exposes platform/record/refusal state but no parametric distinction. The site was not run.

Review [#5939560673](https://github.com/udi-shapiro/Grassroots-Audit/pull/28#pullrequestreview-5939560673) requests changes before merge: update public totals to 29 reports, 17 findings, one unanswered, nine unresolved and eight verified corrected; replace `Auditor: none` with Website GPT auditor ownership while preserving the GCE proposal attribution; regenerate status. Finding remains proposed/unpublished until a corrected head is reviewed.
