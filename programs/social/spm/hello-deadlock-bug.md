# Bug: a friend who restarts after a fault deadlocks with its friends

The code is the compiler's text, `programs/vglp/cva/compiler/text.glp`, at GLP `6c14d338`.

## The bug

1. Two machines act together only after greeting both ways: a peer is known "once hello has been sent to it and received from it" (line 1247). Proposing needs every participant known (`may_propose`, line 1800), and voting needs the initiator known (`vote_go`, line 2061).
2. Bob still lists the restarted Alice as greeted, so he starts an act with her and locks, waiting for her vote. A machine holds one lock and defers other starts while it holds it.
3. Alice's greeted list was erased, so she withholds her vote silently. Bob gets no refusal.
4. Alice's new hello is dropped, because she greeted Bob before (`hello_cond`, line 1279). Bob doesn't greet back either, because he already knows her (`meet_hello`, line 1251).
5. Bob stays locked forever, and every friend who then starts an act with Bob locks behind him. In the simulation, Alice is never restored. The platform has no timer to break this.

## Fix, minor fault (state loss): Alice's machine only reacts

1. **Who:** Alice's restarted machine answers a start from a peer it has neither greeted nor heard from with `who(Alice)`.
2. **Re-greet with proof:** Bob answers `rehello(Bob, Proof)`, carrying the hello Alice signed before. Alice keeps her key, so her machine verifies its own signature and takes Bob as known without asking her. Bob's checkpoints then restore her.
3. **Re-fire:** on the second request while an act Bob started is still open, his machine re-sends the start once, to participants with no vote. A start a machine has already asked or voted on is dropped.

## Fix, major fault (identity loss): Alicia starts everything

1. Alicia, a new key on a new machine, meets her custodians and friends by an ordinary acquaint. A re-greet can't apply, because the old key is gone.
2. **Give up:** if Bob's act with old Alice is still open after the re-fire, Bob's machine yields it and frees his lock.
3. Alicia presents the custodians' vouches; once they reach Alice's threshold, Bob accepts Alicia in place of Alice.

## Status: fixed

- **Contract:** [EShapiro2/GLP #144](https://github.com/EShapiro2/GLP/pull/144) - Checkpoint and Restore as sender-chosen acts.
- **Platform:** [EShapiro2/GLP #145](https://github.com/EShapiro2/GLP/pull/145) - who/rehello, re-fire, give-up, the simulator's fault step, and all platforms reprinted.
- **Tests:** vGLP section 1,349 / 1,349; fast tier no failures. In sGLP, Alice recovers after a random state loss in every 3-person run, in both delivery orders. A start open at the fault is re-fired and resolved; without re-firing, Bob stays locked. After an identity loss, Bob re-fires once, yields, carries on, and accepts Alicia.
- **Open:** Udi's "no machine applies an act before every participant confirmed the commit" is implemented as a separate draft, waiting for the paper's text. Rule 1 tested; rule 2 needs message delay, which the simulator lacks. The Calculus must renew Secure Friendship's `verdict-term.sha256` (#144).
