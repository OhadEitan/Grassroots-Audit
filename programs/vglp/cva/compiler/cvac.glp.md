# Audit report: programs/vglp/cva/compiler/cvac.glp

Project: LBM (Claude, for Ohad Eitan), a project that uses the compiler and does not work on it
Auditor: LBM's Claude, reporting from use; not a GPT auditor
Date: 2026-11-24
GLP commit: 235bab588e903e4975a6da00ea481862f11c345a (main); the same behaviour at ff6579e19
Other source versions: the Logic pragmas of `programs/lbm/Auction.txt` on the LBM branch `ohad/gra-ss-sglp` (pull request to EShapiro2/GLP); the simulation logs under `simulation/GRA-SS/` on that branch.

Scope: three ways a compiled canonical platform refuses or drops an act that its contract allows, met while writing the Second-Score Auction's Logic pragmas.
Coverage: the platform's request path (`request_cond/4`, `part_dom/4`, `cand_ok/4`, `rs_req/2`) read and exercised in the REPL on states taken from the logs; the compiler itself was not read. Findings 2 and 3 are described by their symptoms; their cause in the compiler was not found.

## Finding 1: an act that names a condition it also deletes is always refused

Severity: medium

`rs_req(rs(_, _, D, K, _), R) :- uncleared(D, D1), app(K, D1, R)` takes an act's required atoms to be its conditions K and also the atoms it deletes, D. Where a condition is also deleted, as in "Rank: provided Alice holds Bob's unranked bid ...; after which no longer Alice holds Bob's unranked bid", the atom is required twice, and `ms_sub/3` asks the state for two copies of it. The state has one, so the act is refused (`unable`) whatever the state. The Calculus accepts such text and the checker calls it grassroots; the platform never runs the act. Either the compiler should count a deleted condition once, or the Calculus should refuse the text.

### Answer

### Verification

## Finding 2: an act with a number in no atom, not defined by an equation, is refused

Severity: low

Two acts were refused in every state where their conditions held, and were accepted once the number was also recorded in an atom: Rank behind, whose Score appeared only in "W is Score plus Fare" and "Score is at most Second"; and Arrive late, whose Late appeared only in "Pickup is Due plus Late". Numbers that appear in no atom but stand on the left of an equation ("Cost is L times Delay", "Due is Start plus Delay") are accepted. `part_dom/4` gives `yes` on the state taken from the log, so the refusal comes later in the request path.

### Answer

### Verification

## Finding 3: an act that deletes and adds the same atom loses its button

Severity: low

An act whose effects are "no longer the second score of x's call c is w and the second score of x's call c is w" compiles, but it is left out of the platform's `Proposal` type and gets no button, so no person can propose it. The compiler says nothing.

### Answer

### Verification
