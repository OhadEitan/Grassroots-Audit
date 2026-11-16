# Audit report: programs/apps/gb

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GB's app, its calendar/maturity scripts, and the escrow implementation.
Coverage: Read the README, declarations, mini-app calendar grant, both existing plays and their scripted persons. The app's platform is byte-identical to `cascade/GB/platform.vglp`, reproduced by this sweep's cascade check. Its 22 concrete schema names match the source and phone certificate.

Executed the existing `play_bonds` and two audit-only escrow plays against the committed compiled platform. The accepting play deposits two coins and two bonds with Carol, then transfers one of each to Dave; the declining play leaves all four instruments with Carol and emits a refusal. The full trace and final-state checks are [preserved](https://github.com/udi-shapiro/Grassroots-Audit/tree/d61f8d3f6520ec0ef665d3a7030a517beda982ba/auditor/evidence/currencies-gsa-20261112/currency-witnesses). This is evidence for [GB.glp Finding 1](../currencies/bonds/GB.glp.md), not another app finding.

`play_bonds` and `play_village` are app scripts. GB's recorded cascade explicitly contains **no run**. The village's release on day 30 is scheduled by its scripted person; it is not an escrow-condition predicate in the contract implementation. The app receives a stream of dates, and the play supplies it. No independently attested device clock was tested.

The prior [APPS run](compile.sh.md#existing-application-tests), at `5c17c4a`, had 27 passing GB assertions. That history and the present targeted run do not establish arbitrary concurrency, economic solvency, device operation or input-domain safety. [Known reds](../../test/run_all_tests.sh.md) are tracked once for the shared suite.

## Follow-up, 2026-11-16

At GLP `d56822c2e6c474d883f8535bd63d0ef1b6381486`, The current GB platform rebuilds byte for byte and its checks pass within the APPS section, including the revised escrow-record village scenario. The unresolved enforced-condition issue remains GB Finding 1. The complete APPS section passes 249/249. [Execution](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43849758772) and [durable evidence](https://github.com/udi-shapiro/Grassroots-Audit/tree/fe7a040a32a45e7b126df20cc2c898710c1642fa/auditor/evidence/catchup-20261116). This extends the stated reproduction coverage; it is not a new full contract audit.
