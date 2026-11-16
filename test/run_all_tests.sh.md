# Audit report: test/run_all_tests.sh

Project: Code
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-16
GLP commit: d56822c2e6c474d883f8535bd63d0ef1b6381486

Scope: A single audit record for `KNOWN_RED_CHECKS`, as requested by Udi. This is an inventory and reporting policy, not a new defect report or a new full-suite execution.
Coverage: Parsed the current exact-name array: **20 distinct SG entries**. The three former APPS entries have been removed. The current APPS run passes 249/249 and K passes 134/134. SG and the full suite were not rerun. [Current machine-readable registry](https://github.com/udi-shapiro/Grassroots-Audit/blob/fe7a040a32a45e7b126df20cc2c898710c1642fa/auditor/evidence/catchup-20261116/known-red-registry.json). The previous 23-entry inventory remains in Git history and its pinned evidence.

A listed failure increments the known-red count and does not fail the suite. A listed success fails the rot guard until the obsolete entry is removed. Matching is by exact check name. Report these acknowledged reds here once; component reports link here and do not create new findings for each affected app or assertion. An unlisted failure retains its harness classification, but several assertions caused by one defect still do not become several findings.

| Source comment's group | Entries | Recorded dependency / responsibility |
| --- | ---: | --- |
| CSSN super-app port | 11 | GSG's hosting port |
| Retired handwritten CSSN/childsafe fixtures | 9 | GSG's port of replaced/deleted examples, recorded while the project was dormant |

The group labels above summarize the source comments; they do not reassign project ownership. These are historical named checks, not 20 new audit findings.

### CSSN super-app port

```text
SG two mini-apps at once: bob connected and greeted under it
SG two mini-apps on two smartphones: and its message arrives
SG super-app hosts the child-safe platform: alice connected to bob
SG super-app hosts the child-safe platform: bob connected and greeted
SG super-app hosts the child-safe platform: no failed play
SG two mini-apps at once: alice connected under the child-safe platform
SG two mini-apps on two smartphones: the child-safe friendship holds
SG child-safe platform on two smartphones: alice is connected to bob
SG child-safe platform on two smartphones: bob is connected to alice
SG child-safe platform on two smartphones: alice's message reaches bob
SG two mini-apps at once: no failed play
```

### Retired handwritten CSSN/childsafe fixtures

```text
SG super-app: cssn's artefact is refused a certificate
SG super-app: load_file gives cssn's artefact as text
SG super-app: the super-app installs no text
SG super-app: the child-safe platform's artefact is certified
SG two mini-apps at once: alice's swap settles
SG two mini-apps at once: bob's swap settles
SG two mini-apps on two smartphones: the currency's conversation opens
SG two mini-apps on two smartphones: alice's swap settles
SG two mini-apps on two smartphones: bob's swap settles
```

### Relationship to published findings

[Application integration Finding 1](../programs/apps/compile.sh.md) is now verified corrected at the current pin. Its historical APPS failures remain attached to their original run; the independent November 16 APPS run passes 249/249. The twenty SG names above remain an inventory, not newly executed failures in this batch. No new per-app findings are created for those known reds.

The new GB escrow and GSA certificate cases are distinct semantic checks, absent from this registry. They are not relabeled known-red suite failures. No test expectations or source allowlist entries were changed by the auditor.
