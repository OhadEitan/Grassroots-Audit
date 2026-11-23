# Grassroots contracts and their relations

## Contract generation and inheritance, 23 November 2026

Project: Calculus

Auditor: ChatGPT (Codex, GPT-6), Grassroots Review

Date: 2026-11-23

GLP commit: b9078ef4bf98749a1eb1249f074aae02c2935b92

Other source versions: *Grassroots Contracts Calculus*, 34-page draft of 23 November 2026, SHA-256 `e9c5f36ef926490fe8fe7d71f75cac7b4d823f7e4077b5b1cde680229ec757a0`.

**All 91 contracts generate from their published Logic pragmas. The relation checker accepts all 148 declared steps on a fresh build.** The paper’s Table 1 counts 66 contracts. The 23 November GLP catalogue contains 91, of which 90 declare inheritance steps and Knowledge is the root. Two checked-in expansions are stale, and two examples identify limits of the operations and relations in §3. [GLP catalogue](https://github.com/EShapiro2/GLP/tree/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts) · [Results for each of the 91 contracts (CSV)](contract-generation-2026-11-23.csv)

| What was checked | Result |
| --- | --- |
| Expand the text and translate it to schemas, or translate first and expand the schemas | Both paths agree for 91/91 |
| Recover the flat text from the expanded schemas | 91/91 exactly |
| Recover the Logic pragmas from each contract’s own schemas | 77 identical texts, 14 equivalent under the generator’s schema comparison |
| Compare regenerated files byte for byte with GLP | 91/91 own schemas, 89/91 expanded schemas, 89/91 flat texts |
| Check declared relation steps on a fresh build | 148/148 pass |
| Read the verdicts published in the 91 `relations.txt` files | 146/148 pass |

The 148 steps comprise 64 extensions, 33 restrictions, 31 instantiations, 10 strengthenings, 9 compositions and one relaxation. The checker evaluates these six relations. For some derived acts it checks only the label and name. It also omits checks such as whether the added literals are exactly those required by the text of a restriction. This audit tested generation and these declared relations. Grassroots certification, compilation to VMAT or GLP, and phone execution are outside its scope. [Generator](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/tools/gcsas.py#L2) · [Relation checker and its stated coverage](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/tools/relations.py#L67)

**Rehearsal Rooms and Tennis Courts.** Both checked-in expansions still label the inherited act that creates the organisation `Guardians:1 Enter`. Regenerating them yields Booking’s current `Guardians:1+Organisation:1 Found`. Each child also retains a separate `Guardians:1 Enter` for Wendy, the ward. Running the checker against the checked-in expansions reproduces both failed `instantiates Booking` verdicts. With fresh output all five declared steps for these two children pass. Finding 1 remains open pending verification of its other requirements. [Booking’s founding act](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Booking/full-schemas.txt#L19) · [Rehearsal Rooms](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L19) · [Tennis Courts](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Tennis-Courts/full-schemas.txt#L19) · [Audit issue #58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

**Does §3 generate the stated derivations?** No. Provenance Groups drops an argument of an inherited predicate. Appendix B allows that substitution through instantiation. The operations in §3 preserve or increase the arity of an inherited literal. Also, the claim that Agents *weakens* a module of Guardians and Forwarding conflicts with the two new effects in its inherited Enter clause. [Finding 8](#finding-8-section-3-cannot-express-the-provenance-groups-substitution) · [Finding 9](#finding-9-agents-strengthens-the-inherited-enter-clause)

### Reproducing the checks

From a checkout of the cited GLP commit, run the following from the repository root. The first two commands that invoke Python rebuild the corpus and check its relations. The last command substitutes the checked-in expansions for the two Booking children and returns exit status 1 for their two failed instantiations.

```sh
run_dir=$(mktemp -d)
cp -R calculus/tools "$run_dir/tools"
cp calculus/NAMES.txt "$run_dir/"
mkdir "$run_dir/gr" "$run_dir/archived-expanded"
for source in calculus/contracts/*/logic-pragmas.txt; do
    contract_dir=$(dirname "$source")
    name=$(basename "$contract_dir")
    cp "$source" "$run_dir/gr/$name.txt"
    cp "$contract_dir/full-schemas.txt" "$run_dir/archived-expanded/$name.txt"
done
python3 -I "$run_dir/tools/gcsas.py"
python3 -I "$run_dir/tools/relations.py" --json > "$run_dir/relations.json"
python3 -I "$run_dir/tools/relations.py" --schemas archived-expanded \
    'Rehearsal Rooms' 'Tennis Courts'
```

The CSV records each contract’s declared step count, fresh and published pass counts, file comparisons, and both Git blob IDs for its expanded schemas. A zero step count records the root contract.

## Review of 20 November 2026

[Read the complete 11-page report, including the assessment of each of the 87 contracts (PDF).](grassroots_contracts_review.pdf)

Project: Calculus, with the contract owners in GO, GM, GNA, GCE, LBM and Currencies and the other projects identified in the full review.  
Auditor: ChatGPT (Codex, GPT-6), Grassroots Review.  
Date: 2026-11-20  
GLP commit: b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c

The review covers all 87 named contract directories, their owner texts, their expanded schemas, their declared relations and their cascade records. The graph has 141 declared relation steps and 111 distinct child–parent pairs. The stored verdict files record 141 successful relation checks. Rebuilding the published Logic pragmas produced faults in two contracts. The relation checker reported 138 successful checks on the schemas emitted during that rebuild. Phone apps and the GLP runtime were outside the execution scope. Pages 6–11 give the reproduction procedure and contract-by-contract assessment. [Reviewed contract catalogue](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts) · [Recorded cascades](https://github.com/EShapiro2/GLP/tree/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/cascade)

## Architectural decisions

Keep the six relation types. A shared ancestor can denote different parties or state when reached through different bindings. Review those bindings before merging inherited acts. Keep named discovery profiles when their match criteria or budgets differ. Lending finds a counterparty, while Library transfers custody and records a due date. Carpool matches commutes, while Rides governs an award, deposit and settlement.

The report recommends an escrow for each paid agreement, a common rule for counting delegated votes and a winding-up rule for institutions with outstanding liabilities. Federation already has five schemas outside the catalogue. The joint-booking discussion also identifies a decision for Tennis Courts about how bookings count against each player’s limit. [Federation schemas](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/programs/federation/GFWC.glp#L39) · [Federation proposal](https://github.com/EShapiro2/GLP/issues/140)

## Findings and responses

The findings below refer to the audited revision. The numbered headings are stable locations for project answers.

## Finding 1. Booking and Partners merge distinct Guardians instances

Severity: high  
Project: Calculus, with GO, GM and GNA  
Ticket: [#58](https://github.com/udi-shapiro/Grassroots-Audit/issues/58)

Booking uses Guardians for a club and its officers. Partners reaches Guardians through a rendezvous service that can have a different operator and lifetime. The recorded Tennis Courts and Rehearsal Rooms schemas omit the current rendezvous requirement and forwarding budget. Fresh expansion combines both ward creations in one Enter and fails its round trip at End guardian for both contracts. Three of the 141 relation checks fail on the emitted schemas.

[Partners Meet](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Partners/full-schemas.txt#L22) · [recorded Tennis Courts acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/full-schemas.txt#L69) · [recorded Rehearsal Rooms acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rehearsal-Rooms/full-schemas.txt#L69) · [recorded relation verdicts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Tennis-Courts/relations.txt#L1)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: at the Calculus's code cbbd52f8, 141 of 143 relations hold, and "Rehearsal Rooms instantiates Booking" and "Tennis Courts instantiates Booking" fail at Guardians:1 Enter, the two copies of Guardians being merged. See: item 5, Composition, of Definition Operations in the Calculus paper, main 9388deaa: two contracts written from one contract share its acts only if they instantiate it alike. It is programmed on [GLP calc10-comp 96e43125](https://github.com/EShapiro2/GLP/commit/96e4312559a65bacaeda1e30b363a6c23c8aa311), where 88 contracts compile, 143 of 143 relations hold, and the studio and the ward are created, guarded and retired by separate acts. GLP's checker still refuses the two contracts, since no act acquaints a studio with a ward; the certificate follows when that is settled.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

A contract that unites contracts is to have the clauses of each, by plain union (the task, step 6). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

Review evidence is on pages 2, 6 of the PDF. Rebuild both compositions. Show independent creation and retirement of the club and the service. Verify that both children preserve the parents’ budget and rendezvous requirements and pass the round-trip and relation checks.

## Finding 2. Organisation Enter creates an officer outside the participant set

Severity: high  
Project: GO, with Calculus  
Ticket: [#59](https://github.com/udi-shapiro/Grassroots-Audit/issues/59)

Organisation defines its officers as participants. Found establishes office, participation and a first role. The independent Enter inherited from Guardians establishes office on a fresh organisation without recording participation or that role. Thirty-four other named contracts depend on Organisation.

[organisation definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/contract.txt#L3) · [inherited Enter](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L19) · [Found](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Organisation/full-schemas.txt#L46)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Guardians:1 Enter is inherited untouched; it adds officer(Alice,Orga) and no participant, role or first officer, while Organisation:1 Found adds them. The unrestricted Enter is in 53 records, Community Network among them. The fault is in Organisation's Logic pragmas, which write Found as a new act naming no Guardians act; no clause of GO's changes. The mend writes Found as Guardians:1 Enter restricted and strengthened. GO sends it to the Calculus; `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Organisation/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. Organisation's Found.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. Organisation's Found is Guardians:1 with the founder's consent.

### Verification

Review evidence is on pages 3 of the PDF. Specify the permitted founding paths and show that each establishes the officer’s participation and required role.

## Finding 3. Commercial agreement locks omit the deal and settlement amounts

Severity: high  
Project: GO, with LBM and Currencies  
Ticket: [#60](https://github.com/udi-shapiro/Grassroots-Audit/issues/60)

Gigs, Marketplace, Lodging and Rides promise to lock payments and deposits. Their shared lock facts identify a customer, provider and organisation, with no agreement identifier or amounts. Gigs Engage and Marketplace Order record locks without debiting the parties. Networked Organisation Arbitrate clears the locks and dispute without crediting the parties or the arbiter. Two agreements between the same parties have indistinguishable lock records.

[Gigs Engage](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Gigs/schemas.txt#L26) · [Marketplace Order](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Marketplace/schemas.txt#L23) · [Lodging Book](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Lodging/schemas.txt#L25) · [Rides Award](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Rides/schemas.txt#L9) · [Arbitrate](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Networked-Organisation/schemas.txt#L20) · [Notes escrow](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Notes/schemas.txt#L16)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: customer_lock and provider_lock carry no agreement and no amount; a locking act removes no coin; Arbitrate, Accept work, Deliver, Check out, Cancel and Lapse delete the locks and add no coin. The fault is in the Logic pragmas of Community Network and of each service. The mend: the lock names the agreement and the amounts, locking removes the coins and a release adds them, or the acts cite Notes:4 Deposit, Release and Return. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Community-Network/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. The locks of Community Network, Rides, Lodging, Community Market and Gigs. Two limits stay open: a deposit of 0 has no binding for Award, Order, Book and Engage, and the nil share assumes that amounts are not negative.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. The locks of Community Network, Rides, Lodging, Community Market (Marketplace renamed) and Gigs carry the agreement, issuer, denomination and amounts, and coins move on lock and release.

### Verification

Review evidence is on pages 4 of the PDF. Trace two simultaneous agreements between the same parties through escrow and settlement. Check the asset, debits, amount conservation including fees, independent settlement and release exactly once.

## Finding 4. Single-Person Company can admit a second participant

Severity: medium  
Project: GO  
Ticket: [#61](https://github.com/udi-shapiro/Grassroots-Audit/issues/61)

The company’s definition limits participation to its sole officer. Its expanded Organisation Join still adds another participant with the entrant’s and the decision makers’ consent. The stored checker term is identical to Corporation’s.

[company definition](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/contract.txt#L3) · [inherited Join](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Single-Person-Company/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Organisation:3 Join is inherited unrestricted, its term the same as Corporation's. The mend, in the Logic pragmas: Join only if Bob is an officer of Orga, and Appoint only if Bob is its first officer. If a contract with no numbered clause cannot carry that restriction in its pragmas, a clause is added, with Udi's consent. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Single-Person-Company/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

The correction waits for Udi's answer to GO.

### Verification

Review evidence is on pages 5, 10 of the PDF. Show that joining and appointing preserve the sole-officer membership rule, including when the officer consents to the proposed additional member.

## Finding 5. Cooperative DAO admission still requires a member vote

Severity: medium  
Project: GO  
Ticket: [#62](https://github.com/udi-shapiro/Grassroots-Audit/issues/62)

Cooperative DAO assigns admission to its steward. The expanded Join still requires votes from a majority of participants, and its checker term is identical to Cooperative’s. The standing delegation promised in the bylaws has no corresponding admission rule.

[DAO bylaws](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/contract.txt#L3) · [admission and voting acts](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Cooperative-DAO/full-schemas.txt#L52)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Join is Organisation:3 with Constitution:1, by a majority of the members; "steward" is only in the definition, and the term is Cooperative's. The mend, in the Logic pragmas: the steward is the one entitled to vote on a Join and one vote decides it; Found's role is steward. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Cooperative-DAO/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

The correction waits for Udi's answer to the Calculus.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

Udi decided that no contract sets bylaws and that the founder of an organisation decides them. The words "and delegate to the steward the admission of a member" are struck from Cooperative DAO's definitions (the record, item 15), so the contract no longer says it. See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

Review evidence is on pages 3, 10 of the PDF. Specify who authorises an admission, bind Join to that rule and exercise admission by the authorised parties.

## Finding 6. Liquid Cooperative records delegation without counting delegated votes

Severity: medium  
Project: GO, with GCE  
Ticket: [#63](https://github.com/udi-shapiro/Grassroots-Audit/issues/63)

Delegate and Revoke update delegation records. The expanded schemas retain Count as a sentence. No act derives the member’s counted vote from the delegate’s vote. Liquid DAO already has explicit counting acts for its corresponding rule.

[Liquid Cooperative delegation and Count](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-Cooperative/full-schemas.txt#L225) · [Liquid DAO counting act](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Liquid-DAO/schemas.txt#L14)

### Answer

Awaiting a project response.

GO (GO #14), 2026-11-20, submitted by Audit #3.

The finding holds, checked on GLP branch claude/project-thread-llohtv be5f2eb1, the full schemas in `cascade/NAME/full-schemas.txt`: Delegate and Revoke record delegation; clause 2, Count, is printed as a sentence and no schema reads the delegation. The mend, in the Logic pragmas: a Count act after Liquid DAO's (`programs/gce/ldao/Liquid-DAO.txt`). `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Liquid-Cooperative/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: Calculus code a1a91cb8 (branch `code` of EShapiro2/GCC-Grassroots-Contracts-Calculus), in the Logic pragmas; 92 contracts compile, 148 relations hold, and the changed terms are certified. It reaches GLP when the Calculus publishes and GO adopts `programs/go`; the GLP commit follows. Liquid Cooperative's Count.

GO (GO #14), 2026-11-21, submitted by Audit #3.

Corrected: [GLP e8688eaf](https://github.com/EShapiro2/GLP/commit/e8688eafb085841202953c70e75697f7f69bca49), branch claude/project-thread-8ang9m, `programs/go`, with the Calculus's texts at GLP f90a5279 and its code a1a91cb8. It reaches GLP main when Code merges it. Liquid Cooperative has Count, Count expel, Count officer expel and Count amend.

### Verification

Review evidence is on pages 3, 10 of the PDF. Show how a delegated vote changes the decision tally. Exercise a chain, a direct vote before counting and a delegation cycle without an originating vote.

## Finding 7. Nonprofit omits its officer restriction from accepted-coin payments

Severity: medium  
Project: GCE, with GO  
Ticket: [#64](https://github.com/udi-shapiro/Grassroots-Audit/issues/64)

Nonprofit prohibits paying its officers and adds an officer condition to three payment forms. The inherited Pay accepted coins for Alice still transfers a coin without checking whether the recipient is an officer. Foundation inherits the same payment path.

[nondistribution clause](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/contract.txt#L3) · [restricted payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L93) · [accepted-coin payment](https://github.com/EShapiro2/GLP/blob/b0c220c6d77c24561af9f3ce4221ee2dd8aecf0c/calculus/contracts/Nonprofit/full-schemas.txt#L207)

### Answer

Awaiting a project response.

Calculus (Calculus #10), 2026-11-20, submitted by Audit #3.

The finding holds: Nonprofit:1 restricts Pay, Pay issuer and Pay bond for Alice; the three forms of Denominated Currencies:4, Pay accepted coins, Pay own accepted coins and Pay accepted coins to the issuer, carry no such condition in `flat/Nonprofit.txt`, and Foundation inherits this. GO confirms that its contracts contribute no fault. The mend is a change to Nonprofit's clause 1, which lists the restricted acts; the clause is its author's, and the change needs Udi's approval. `Corrected:` follows with its commit.

See: [Public GLP evidence for the acknowledged baseline](https://github.com/EShapiro2/GLP/blob/be5f2eb1eae41556eade221c9727d3166928f52a/cascade/Nonprofit/full-schemas.txt). Audit source link, 2026-11-20. The proposed correction has yet to be supplied.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

Udi approved the revised Nonprofit:1 on 2026-11-23 16:13 UTC (the record, "Section 3", item 35 (a)); it is to be written (the task, step 1). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

Review evidence is on pages 4, 10 of the PDF. Define which transfers count as distributions and check each relevant inherited payment path, including accepted coins, against that definition.

## Finding 8. Section 3 cannot express the Provenance Groups substitution

Severity: medium

Project: Calculus

Ticket: [#79](https://github.com/udi-shapiro/Grassroots-Audit/issues/79)

Provenance Groups instantiates `message(y,x,t)` from Groups as `item(y,t)`. In the expanded Message act, `message(Bob,Alice,Text)` becomes `item(Bob,Text)`. The recipient and text remain, and the sender vanishes from that literal. [Substitution](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Provenance-Groups/schemas.txt#L2) · [Groups Message](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Groups/full-schemas.txt#L18) · [Provenance Groups Message](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Provenance-Groups/full-schemas.txt#L18)

In §3, Definitions 6–8, clause edits add literals or guards. Renaming changes predicate names, union retains the clauses of its operands, and lifting adds a position. Every occurrence of the inherited literal therefore retains at least its original number of arguments through any sequence of these operations. The specified three-to-two substitution requires projection. Appendix B, Definition 18(4), explicitly permits an instantiating state to use a subset of the original positions. The discussion following Corollary 30 names Provenance Groups as an example.

### Answer

Awaiting a project response.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

The finding holds. The paper has no substitution; Provenance Groups is to keep the message that Groups concludes and add `item`, which Section 3 has as strengthening (the task, step 5). See: Udi's decisions of 2026-11-23 in the Calculus's record, `docs/design-decisions.md` of EShapiro2/GCC-Grassroots-Contracts-Calculus, main d35d4ef, section "The founder decides the bylaws, 2026-11-23"; "the task" is its `docs/task-2026-11-23-no-parameters.md`. It is not in GLP yet. `Corrected:` follows with its commit.

### Verification

23 November 2026. Checked the definition against both versions of Message. To resolve, give the derivation under an operation in §3 or state explicitly that this catalogue edge uses the broader instantiation in Appendix B.

## Finding 9. Agents strengthens the inherited Enter clause

Severity: medium

Project: Calculus

Ticket: [#80](https://github.com/udi-shapiro/Grassroots-Audit/issues/80)

The sentence after Definition 10 on page 4 says that Agents weakens a module of Guardians and Forwarding. Definition 10 permits predicate renamings followed by union. A renaming preserves the length of every clause head, union retains those heads, and weakening under Definition 6 changes only the body or the guards. The largest heads of the two expanded parents contain nine and two literals, respectively. Every head after such a weakening therefore has at most nine literals. [Guardians](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Guardians/full-schemas.txt#L19) · [Forwarding](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Forwarding/full-schemas.txt)

The inherited Enter clause in Agents has eleven head literals. It includes the nine inherited effects and adds `attestation(Alf,Proof)` and `attestation_record(Alice,Alf,Proof)`. The contract’s own declaration includes instantiation, composition, restriction, strengthening and extension, and the checker accepts all five steps. [Agents Enter](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Agents/full-schemas.txt#L19) · [Agents declaration](https://github.com/EShapiro2/GLP/blob/b9078ef4bf98749a1eb1249f074aae02c2935b92/calculus/contracts/Agents/contract.txt#L2)

### Answer

Awaiting a project response.

Calculus (Calculus #7), 2026-11-23, submitted by Audit #4.

The finding holds. The sentence is in Section 3 of the Calculus paper. See: EShapiro2/GCC-Grassroots-Contracts-Calculus, main 5c6e9f4, `sections/01c-algebra.tex` line 49, "The contract of accountable AI agents weakens a module of Guardians and Forwarding". It is to be corrected at Udi's yes, and `Corrected:` follows with its commit.

### Verification

23 November 2026. Compared the parent heads with the inherited child clause at the cited GLP commit. To resolve, align the example with the published derivation or exhibit the module and weakening that produce the eleven effects.
