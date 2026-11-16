# Audit report: programs/apps/gc

Project: Currencies
Auditor: ChatGPT/Codex, coordination session of 2026-11-12; model version not exposed
Date: 2026-11-12
GLP commit: c40e6d3ad68b198066ab723d17c05171c0a7de76

Scope: GC's committed app against GC's schemas and its recorded cascade.
Coverage: Read the app README, `self.glp`, wrapper and scripted plays; compared concrete schema names with the contract and phone certificate. The app's `platform.vglp` is byte-identical to `cascade/GC/platform.vglp`, which was regenerated and checked in this sweep. All seven schema names match.

GC's [contract report](../currencies/coins/GC.glp.md) records the checked permissions and asset accounting. The [cascade report](../../cascade/GC.md) records four replayed examples. The app has its own `play_coins` and village scripts; these must not be confused with the four cascade plays. The prior [APPS execution](compile.sh.md#existing-application-tests), at `5c17c4a`, had 56 passing GC assertions; those are historical results, not a new APPS run in this sweep.

No independent new app finding in this scope. UI input validation, arbitrary interleavings and physical-phone execution remain untested here. Known-red suite entries are centralized in [the test registry](../../test/run_all_tests.sh.md), without per-app duplicate findings.

## Follow-up, 2026-11-16

At GLP `d56822c2e6c474d883f8535bd63d0ef1b6381486`, The current GC platform rebuilds byte for byte and the GC checks pass within the APPS section, including the village and isolate-based boot fixtures. The complete APPS section passes 249/249. [Execution](https://github.com/udi-shapiro/Grassroots-Audit/actions/runs/43849758772) and [durable evidence](https://github.com/udi-shapiro/Grassroots-Audit/tree/fe7a040a32a45e7b126df20cc2c898710c1642fa/auditor/evidence/catchup-20261116). This extends the stated reproduction coverage; it is not a new full contract audit.
