# Final navigation and research organization review

Reviewed UTC: 2026-10-31T23:41:52Z. Model: GPT-6 Astra.

**CONFIRMED, with two small navigation repairs proposed.** Existing local links resolve in the inspected Markdown graph. Two standalone matrix-extension proofs have no clickable route from the main analysis index. The latest numbered V and fourth-decision entries also lead to preserved preparation indexes instead of their completed results. These are organization findings, not additional strength evidence or refutations of the results.

The fixed inspection ran from 2026-10-31T23:39:49.146695+00:00 to 23:39:49.734852+00:00. [INSPECTION.json](inspection-001/INSPECTION.json) contains every input hash, compressed input snapshot, link edge and reachability result. Its SHA256 is `5027da354614bfc3ca7184fce5c762803db96c66465df6b1898b9b724cb5e298`. [scan_navigation.py](scan_navigation.py), SHA256 `0288e80622c5dd96bb87ea21ded4d65df993b912727d1adbdd5df8154804ce18`, imports only the standard library and reads retained Markdown. The scan excludes source/archive subtrees from the initial topic inventory and follows existing local Markdown links. It never opens linked JSON parameters or executes project code.

The scan read and archived 384 Markdown documents, including all 169 distinct Markdown targets linked directly from the main index. It found 331 local link occurrences, no missing local target and no unresolved heading anchor among the recognized links. Sixty-six distinct non-Markdown targets were checked for existence only. All 165 standalone analysis `PROOF.md` files are reachable from the index. Two further standalone proofs in the explicitly included review topics are not. Human review concentrated on the current guides, late preparation/completion pages and both matrix-extension arguments; this is not a new semantic verification of all 165 earlier proofs.

The index and guide snapshots are:

| Input | SHA256 |
| --- | --- |
| `bot_research/experiments/validation/analysis/README.md` | `d11e35db633f34a867bdc0deb1e6b4394ac2194cdd49de994dc4d0145d5532c9` |
| `bot_research/experiments/validation/analysis/VALIDATION_FINDINGS.md` | `fb4931c66944cfa59058a2947214681d90d05d927b5ecd58b92875df340c19f2` |
| `bot_research/experiments/validation/analysis/ADAPTATION_FINDINGS.md` | `b371dd4205158191d72499c8efe57a35b33d1ff418467ca725356f1228891cba` |

## 1. Two matrix extensions need a route from the main index

The [one-row frr3 extension proof](../frr3_extension_review_001/PROOF.md) has its exact matrix, hypotheses, notation, necessity and sufficiency argument, dependencies and limits. Its [reading-order index](../frr3_extension_review_001/INDEX.md) exists but contains plain text paths rather than clickable links. Neither page is reachable from the main analysis index. The proof's SHA256 is `2fadc704e204dcdfa51f7041a124254485d95e01f6a32d202a828b902169f86b`; the index's is `d2561362b569c25e343224c8ff14d4ca48e0d233426942d8deb333b7975f9412`.

The final [frr5/frr6 review](../frr5_frr6_final_fortress_001/README.md), [matrix reading order](../frr5_frr6_final_fortress_001/finite_matrix_extension/INDEX.md) and [standalone proof](../frr5_frr6_final_fortress_001/finite_matrix_extension/PROOF.md) are internally organized and link retained evidence. No main-index path reaches them. Their SHA256 values are respectively `750588f8fdeac81a29e51cefae322d06b5a8e8f3bcccc2a9f37ee069dce1f708`, `3e3116150b8355427663a66854c9d203f5314287a02cf86281dec91aabf8e123`, and `87ef401959751b4e343be05e6b2fd3ee3f1f33d90275aba89c440499d3924bdf`.

These are conditional finite-matrix results. The base frr1 self-play diagonal is imposed as zero. The final extension additionally allows any unmeasured real skew mutual entry between v46 and v48 and proves zero weight on both added strategies in every optimum, conditional on the specified old rows. It neither measures that mutual game nor proves a strategy of the unrestricted game. The proposed index wording preserves those distinctions.

Minimum repair: add one supplemental finite-matrix reading route from the mutable analysis index. Link the frr1 index, the frr3 index **and proof**, and the final extension index and completed review. No sealed proof or existing topic index needs editing.

## 2. Link completed results beside historical preparation indexes

Numbered entry 163 currently links the V preparation index, which says that a complete experiment and implementation are future work. That index is explicitly dated 22:21:25.023265Z. The [completed V results](../../analysis/fourth_round_wall_counter/RESULTS.md) are dated 22:37:11.017297Z. Numbered entry 164 links the fourth-decision preparation index, dated 22:26:13.069893Z, which says, "The empirical V application is OPEN." The [completed fourth-decision results](../../analysis/fourth_round_ambiguity/RESULTS.md), SHA256 `a152644a7d2a2f620578449ca54977dc110e83b9f0d5a4f917eefc306e568c12`, are dated 22:39:14.240550Z.

Those preparation statements are historically accurate and should remain. The main index explicitly explains its dated OPEN entries, and its later numbered entries report completion. The adaptation guide already links both completed results. Thus there is no scientific status contradiction in the complete reading route. The remaining problem is that clicking a current numbered completion entry lands on an older preparation page without a link forward.

Minimum repair: add direct completed V and fourth-decision RESULTS links next to the corresponding current index entries, or append the short current-completion route in [MINIMUM_ADDITIONS.md](MINIMUM_ADDITIONS.md). U's preparation index is similarly historical, but it lacks an explicit timestamp in its body. A direct link to U's dated completed results avoids relying on that page to convey current status. Preserve the preparation pages and the index's dated 22:24 and 22:30 OPEN notes.

The terminal guide correctly reports completed D and links the final candidate JSON, independent reader and postchecks. Its neighboring frozen protocol remains prospective by design. The human-readable [terminal RESULTS.md](../../analysis/terminal_reserved_validation/RESULTS.md), SHA256 `6d44d1dbdeac19101b8107c1af84ec25f090bbb3389b57f6bb56215fa230ff64`, is nevertheless not reachable through the present Markdown graph. A direct link beside the terminal guide would make the condition-level result table easier to find. The adaptation guide's explicit pre-D date and scope are historical, not a claim that D remains unplayed.

## Remaining scope and pending work

Of 98 `RESULTS.md` pages read, 83 are not reachable through recognized clickable links, commonly because a proof or index names `RESULTS.md` only in prose or code. The detailed list is retained in the inspection. Most are older protocol records, and the current guides already provide a route through their selected evidence. This review does not require a mass rewrite of sealed texts. An optional future result catalogue could add links without altering those documents.

The AF5 matrix extension under `reviews/frr7_frr8_late_af5_001/af5_matrix_extension/` was being prepared after the fixed inspection. It is **OPEN for this review** until its proof and index are sealed and independently inspected. It is not included in the count of 167 inspected standalone proofs. A future index link is listed separately in the proposal and is not represented as already approved.

The link reader recognizes inline and explicit-reference Markdown links, excludes fenced and inline code, and checks ATX/explicit anchors. There were no reference definitions or external links in the inspected inputs. It is a static navigation check, not a full renderer. Input hashes authenticate the archived bytes read, not continuous historical source identity. No policy, constructor, Engine, game, replay, project checker or test was called. No existing proof, guide, declaration, pipeline or other lane file was changed. No JavaScript/TypeScript, server, cluster, remote compute, GPU or formal prover was used.
