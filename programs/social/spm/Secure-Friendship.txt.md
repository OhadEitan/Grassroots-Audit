# Audit report: programs/social/spm/Secure-Friendship.txt

Project: SPM
Auditor: Ohad Eitan (SPM co-author), with Claude (Opus 5.5)
Date: 2026-11-17
GLP commit: 2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266
Other source versions: none

Scope: The five clauses of Secure Friendship (SGSG), the English contract and its Logic pragmas, read against what each act needs in order to happen.
Coverage: Read [Secure-Friendship.txt](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt) and its generated `Secure-Friendship.glp`, clause by clause. The contract was compiled with `cascade.sh` and an sGLP run of it was attempted with `programs/sglp/cva/run.sh`. The run stops at load with `Undefined procedure: agent/5`, because the compiled platform's agent takes the environment argument and the CVA harness does not pass it. That is a gap in the sGLP harness, not in the contract, and it is not a finding here. Not examined: the paper's appendix, and a run of the revised contract on GLP's tools.

## Finding 1: Clause 1 does not say how custodians are named or that they learn it

Severity: low

[Clause 1](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L12) mentions only fixing the identity record, while the Logic pragmas have two acts: Name custodian and Fix. Carol can vouch in clause 5 only if she knows she is Alice's custodian, and the English never says she records it.

Proposed: Alice may name Carol, whom she knows, her identity custodian, and Carol records that she is; then Alice may fix her identity record, once, with her threshold.

### Answer

Awaiting SPM's answer.

### Verification

Pending.

## Finding 2: Bob never learns the threshold, and may never get the identity record

Severity: high

[Clause 2](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L13) says Alice sends her identity record, but the `send_record` schema sends only the custodians. Bob needs the threshold to count vouches in clause 5. The record is sent only "when they become friends", so if Alice befriends Bob before fixing her record, Bob never receives it. Send record also has no "once", so the platform cannot tell it is done.

Proposed: once Alice and Bob are friends and Alice has fixed her identity record, Alice sends Bob, once, her friends and her identity record, her custodians and her threshold.

### Answer

Awaiting SPM's answer.

### Verification

Pending.

## Finding 3: The checkpoint is sent with nobody deciding, again and again, and carries nothing

Severity: medium

[Clause 3](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L14) has no "may", and its schema has no done-mark, so the platform must send checkpoints endlessly. The schema's checkpoint does not carry Alice's records, and nothing says a new checkpoint replaces an earlier one.

Proposed: Alice may send each of her friends a checkpoint of her records and her identity record, and the friend keeps it in place of any earlier checkpoint from Alice.

### Answer

Awaiting SPM's answer.

### Verification

Pending.

## Finding 4: A state loss cannot happen during a run, and Restore gives back too little

Severity: high

In the Logic pragmas of [clause 4](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L15), `state_loss` is an environment predicate. It is given at deployment and never changes, so no loss can occur while the platform runs. The `restore` schema adds back only the friendship with the restoring friend, not what the clause says he sends. A custodian's record that she is a custodian is lost with her state, and nothing gives it back, so she can no longer vouch. Nothing limits a restore to once for each loss. Friends may also send Alice different versions of the same friendship, and the clause does not say which one she keeps.

Proposed: after a state loss of Alice, which her machine records, each friend of Alice sends her, once for that loss, what he holds of her, and tells her if she is his identity custodian. Alice records them again, keeping for each friendship the latest she is sent. "Latest" is left to the implementation: for example, each friendship carries an epoch, 0 at first, odd once begun and even once ended, rising with each change; Alice keeps the highest, and a friendship rebound to a new identity (clause 5) continues from the epoch it had.

### Answer

Awaiting SPM's answer.

### Verification

Pending.

## Finding 5: The vouches never reach Bob, and telling Alicia is not an act

Severity: high

In [clause 5](https://github.com/EShapiro2/GLP/blob/2edbcd8c6ab343dd4d6fad5421f8e6e5386d3266/programs/social/spm/Secure-Friendship.txt#L16) each vouch is recorded only at the custodian, so Bob has nothing to count. The `accept` schema replaces the count by the environment predicate `threshold_vouched`, fixed at deployment. "Bob tells Alicia the friends of Alice he records" has no schema. The forbidden atom `accepted(Bob, Alicia, Alice, _)` uses a wildcard, which forbidden atoms do not enforce. Nothing on the platform checks the key loss, which can be checked only by the custodian. The name Accept is easily confused with accepting a friendship.

Proposed: Carol vouches, once, after she checks that Alicia is Alice, and sends her vouch to Alicia, with the friends of Alice she records if she is a friend of Alice. Alicia presents the vouches to each friend of Alice she knows. Bob, once shown vouches from at least the threshold of the custodians he records, rebinds Alice to Alicia, once, and sends Alicia what he holds of Alice, as in Restore.

### Answer

Awaiting SPM's answer.

### Verification

Pending.

## Proposed revision of the five clauses

1. ■ Identity record. Alice may name Carol, whom she knows, her identity custodian, and Carol records that she is; then Alice may fix her identity record, once, with her threshold, more than half of her identity custodians. It then changes only by the replacement of a custodian's lost identity (Secure Friendship:5).
2. ■ Friendship updates. Tell: Alice tells each of her friends when she becomes a friend of Bob (Friendship:1) and when she ends a friendship (Friendship:2), and the friend records it. Send record: once Alice and Bob are friends and Alice has fixed her identity record, Alice sends Bob, once, her friends and her identity record, her custodians and her threshold, and Bob keeps them.
3. ■ Checkpoint. Alice may send each of her friends a checkpoint of her records and her identity record, and the friend keeps it in place of any earlier checkpoint from Alice.
4. ■ State recovery. Restore: After a state loss of Alice, which her machine records, each friend of Alice sends her, once for that loss, what he holds of her: her records, her identity record and the friendship updates she told him, and tells her if she is his identity custodian. Alice records them again, keeping for each friendship the latest she is sent.
5. ◆ Identity replacement. Replace: After an identity loss, Alice may establish a new identity, Alicia (Knowledge:1), and ask her identity custodians to vouch for it. Vouch: Carol, an identity custodian of Alice, may vouch, once, after she checks that Alicia is Alice, and sends her vouch to Alicia, with the friends of Alice she records if she is a friend of Alice. Present: Alicia shows the vouches she holds to each friend of Alice she knows. Rebind: once Bob, a friend of Alice, has been shown vouches from at least the threshold of the identity custodians he records for Alice, he takes Alicia in place of Alice, once: Alicia is then his friend in place of Alice, and his identity custodian if Alice was. Bob then sends Alicia what he holds of Alice, as in Restore (Secure Friendship:4), and tells his friends of the change.

The same clauses are proposed to GLP in [https://github.com/EShapiro2/GLP/pull/86](https://github.com/EShapiro2/GLP/pull/86), which changes the English clauses only. The Logic pragmas still follow the old text and must be rewritten from them, with `calculus/tools/adopt.py` regenerating `Secure-Friendship.glp`.
