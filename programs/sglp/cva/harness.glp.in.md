# Audit report: programs/sglp/cva/harness.glp.in

Project: LBM (Claude, for Ohad Eitan), a project that uses sGLP and does not work on it
Auditor: LBM's Claude, reporting from use; not a GPT auditor
Date: 2026-11-24
GLP commit: 235bab588e903e4975a6da00ea481862f11c345a (main)
Other source versions: the cascade records `cascade/Local-Overlay` and `cascade/Second-Score-Auction` at that commit; the LBM branch `ohad/gra-ss-sglp` (pull request to EShapiro2/GLP), which holds a scratch harness, `programs/sglp/gra/harness.glp.in`, showing one way round both findings.

Scope: whether the harness of every canonical CVA platform can run the platforms of contracts whose conditions read the environment or the current date.
Coverage: the harness's `agents/3` and the monitor it starts, against the platforms' `agent` procedures and the platform's `dated/2`; one simulation of the Second-Score Auction, ten persons for forty simulated minutes, run with the scratch harness. The paper, sGLP, was not re-read for this report.

## Finding 1: the harness passes no environment, so a platform with one cannot be run

Severity: medium

`agents/3` calls `agent(K?, In?, Out, Thr, Asks)`, agent/5. A contract whose Logic pragmas have an `Environment:` line compiles to agent/6, `agent(Peer?, Stream(Net)?, Stream(Net), Stream(Output), List(Atom)?, Stream(Ask(Question)))`, the fifth argument the environment's atoms, read once at the start (`env_atoms/2` into the initial state). At the commit above this includes `cascade/Local-Overlay/platform.glp` and `cascade/Second-Score-Auction/platform.glp`. No simulation of either platform can start: the harness has no way to give an agent its environment, for example whether a person is a rider or a driver.

The scratch harness gives each agent its environment from its key (`env_of/2`: `[driver]` for a key below `e`, `[rider]` otherwise). A general answer would let the sGLP source declare each person's environment beside its attributes.

### Answer

### Verification

## Finding 2: a platform's "current date" is the machine's wall clock, not the simulated clock

Severity: medium

The platform reads the date at every step, `dated(St, St1) :- now(T), D := floor(T / 86400000), set_today(...)`. `now/1` is the machine's clock (`GlpRuntime.machineNow`, wall time plus any offset `set_clock/1` gave), while a run's time is sGLP's simulated clock, which the monitor steps. Nothing connects the two, so in a forty-minute or thirty-day simulation `today` stays the real date for the whole run. Every condition on the current date (a bidding period that ends, a maximum pickup delay, a bond's maturity) is decided against the wrong time. A profile also has no clock of its own, so a person cannot propose an act whose parameters include the current date (Award, Pickup and Call in the Second-Score Auction).

The scratch harness sets the machine's clock from the simulated clock at every step of its own copy of the monitor (`set_clock(floor(T * 1440000))`, one platform day to one simulated minute), and shows the minute to each person by adding `clock(Minute)` to the views it relays. That worked for the run, but a profile still sees the clock only when a view arrives.

### Answer

### Verification
