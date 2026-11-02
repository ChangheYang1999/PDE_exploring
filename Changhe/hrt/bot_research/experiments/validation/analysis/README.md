# Validation analysis, reading order

Start with [What the final validation establishes](VALIDATION_FINDINGS.md) for the completed D results, retained failures, source and replay checks, and the limits of the reserve. Its [independent review](../reviews/terminal_final_independent_001/guide-completed-review-001/REVIEW.md) binds the factual review before publication.

Start with [What the checked adaptation examples establish](ADAPTATION_FINDINGS.md) for the O-through-V response sequence, its measured failures and the two conditional selection bounds. Its [independent review](../reviews/adaptation-findings-independent-review-001.md) links the retained evidence. The numbered topics below preserve the full reading order; dated open entries describe their status at that time, with later completion entries following.

1. [Player-assignment symmetry](assignment_symmetry/PROOF.md) states the hypotheses under which swapping policies only swaps the outcome.
2. [Pure-splash damage threshold](splash_threshold/PROOF.md) characterizes arrivals on a fixed map containing no guns.
3. [Pure-tier threat estimates](pure_tier_threat/PROOF.md) give an exact counterexample: cheap fillers in non-arriving spawn phases make a mixed purchase stronger than every pure-tier purchase at the same budget.
4. [Exact-rollout improvement](rollout_improvement/PROOF.md) gives the conditions under which searching one-step deviations cannot make a fixed continuation policy worse against a known deterministic opponent.

5. [First-round defense certificate](opening_certificate/PROOF.md) proves that a specific 89-gold gun-and-wall opening stops every affordable first-round roster.

6. [Timing-trajectory equivalence](timing_equivalence/PROOF.md) justifies reusing an exact baseline only when the full action list at the sole differing round agrees.

These are informal proofs about the bundled engine. No machine-checked proof is claimed. The verification evidence named in each proof is supplementary, not a substitute for the argument.

7. [Finite-policy identification](model_identification/PROOF.md) proves that exact purchase signatures never eliminate a fixed true catalogue member under its stated reconstruction assumptions. This gives no strength guarantee.

8. [Turret-range route occupancy](range_forest/PROOF.md) proves an independent obstruction-search algorithm for the maximum induced linear forest of a finite grid region. Completed search evidence supplies the numerical values.

9. [Stateful public-policy forecasting](stateful_forecast/PROOF.md) proves exact lockstep prediction when a deterministic adapting policy's initial state and full public observation history are known.

10. [Exact attack certificate](attack_certificate/PROOF.md) proves a rational lower bound on a package's damage under every affordable legal construction response, including a sound integer ceiling and the spawn cutoff.

11. [Falsification fallback](falsification_fallback/PROOF.md) states when a one-way fallback preserves the original identifier's trajectory, and what policy-call saving follows after a switch. It gives no recovery or strength guarantee.

12. [Finite empirical policy game](finite_metagame/PROOF.md) gives an exact rational certificate for a policy mixture against a fixed, audited payoff table. It does not imply robustness to opponents outside that table.

13. [Compiled public trajectory](compiled_policy/PROOF.md) proves when an exact observation-guarded action table reproduces a recorded game, and states why fallback does not guarantee recovery against an unexpected opponent.

14. [Zero-based roster wrapping](roster_wrap/PROOF.md) derives the exact padding for the first wrapped heavy copy and gives a component test of a frozen sampler's off-by-one error.

15. [Compatible compiled trajectory library](compiled_library/PROOF.md) proves simultaneous reproduction of compatible public histories and explains exact finite conflict-graph selection.

16. [Large-roster gun pruning](large_roster_pruning/PROOF.md) gives a legal component fixture where two guns stop all sampled attacks but a roster-size shortcut excludes the gun search.

17. [First-round damage bound](opening_damage/PROOF.md) proves that four tier1 copies and one tier2 copy maximize immediate damage against every legal first-round map containing no turrets.

18. [An off-route turret and a public policy feature](feature_bluff/PROOF.md) proves that the declared bluff gun cannot damage any copy on its unchanged map, while its positive turret count disables economy13's no-turret branch.

19. [A three-policy counter cycle](counter_cycle/PROOF.md) proves the unique uniform equilibrium conditional on the measured economy, guard and bluff payoff matrix. It illustrates why a successful counter need not dominate the policy it beats.

20. [Removing an unused opponent forecast](visible_schedule/PROOF.md) proves exact trajectory equivalence for the fixed schedule controller when a declared opening prior and later visible rosters equal every forecast defensive threat list.

21. [Isolated-copy exposure](single_copy_exposure/PROOF.md) gives an exact fixed-map survival threshold for one active entry, with all standard guns and splashes. It does not certify defense against a stream.

22. [Fixed capacity on a full map](full_map_capacity/PROOF.md) proves permanent construction obstruction and a lower bound on arrivals from gun damage capacity, with explicit spawn-cutoff, budget and survival limitations.

23. [Construction projection of a stateful policy](construction_projection/PROOF.md) proves why the fixed Lead10 policy's construction can be forecast exactly from its current public observation even when resetting its private attack history makes the full action forecast wrong. It gives no general guarantee for other policies or counter outcomes.

24. [Unused grower forecast](blind_grower/PROOF.md) proves that a growth/flood controller whose defense begins after the game horizon returns the same actions as the corresponding blind FeatureBluff, provided the unused model succeeds and has no external effects. It does not assert strategic strength.

25. [Current-route immunity](current_immunity/PROOF.md) proves that enough splash exposure prevents every arrival even when guns are present. It states the separate route-persistence requirement for future safety and the remaining offensive uncertainty.

26. [Fixed-map gun support](fixed_gun_support/PROOF.md) refines the gun-capacity certificate with exact possible firing ticks and gives a finite exact search for the smallest package certified by that bound. It distinguishes current-map and full-map response guarantees.

27. [Public forecasting through a known legal opening](prefixed_forecast/PROOF.md).
    Call-through opening semantics preserve exact stateful public forecasting;
    they differ from initializing the target only after a prefix.

28. [Minion-only forecast equivalence](minion_projection/PROOF.md) proves when the timing controller can discard forecast construction and factory purchases without changing its trajectory; a recorded round-6 attack violates the gate hypothesis.

29. [A corner guard against three tier1 copies](corner_guard/PROOF.md) proves that one gun1 at (10,1) stops the three-copy opening roster for 30 gold. This does not certify every affordable roster or full-game strength.

30. [Monotone stateful policy identification](stateful_catalogue/PROOF.md) proves that a true deterministic catalogue member is retained when independent clones are advanced once per reached round and falsified members are permanently removed. Identification and strategic strength remain separate questions.

31. [The measured best_v9b counter cycle](current_best_cycle/PROOF.md) binds three directed winning edges to six already audited games. No self-play values or equilibrium are inferred.

32. [Attack selection from a retained catalogue](catalogue_attack_selection/PROOF.md) gives a conditional current-round damage bound and safe-lethal criterion. The bounded purchase search and its economic weight do not imply full-game optimality.

33. [Terminal catalogue-score scope](catalogue_terminal_score/PROOF.md) states the separate final-round gain guarantee and gives an abstract forecast-table counterexample to inferring optimal terminal outcomes. It does not claim that the counterexample table is a reachable game state.

34. [One-way catalogue continuation](catalogue_continuation/PROOF.md) proves exact parent trajectories while the true member is retained and specifies the fresh continuation after rejection. It does not guarantee recovery against an outside opponent.

35. [A guarded opening with a synchronized forecast](guarded_forecast/PROOF.md) preserves exact public-policy prediction while replacing the observer's opening, and states the separate original-combat condition for zero incoming damage. It gives no affordability or winning guarantee.

36. [Singleton terminal selection](catalogue_singleton_terminal/PROOF.md) proves best terminal outcome within the evaluated purchase set when the sole retained model is true and exact. It holds construction fixed and makes no global or nonterminal optimality claim.

37. [Adaptive catalogue continuation](adaptive_continuation/PROOF.md) combines the bounded attack selector with the fresh economy20 continuation after complete rejection. It proves the component identities, not an outside-opponent strength guarantee.

38. [Threshold-search boundary counterexample](kill_threshold_boundary/PROOF.md) shows that the frozen fortress helper returns 2 when one tier5 is already lethal on an empty map, because count 1 is assumed nonlethal. It does not attribute any recorded full-game loss to that component error.

39. [Defensive search budget](defense_step_budget/PROOF.md): a surviving-round witness from one recorded scripted-map loss; the 30-step original-combat check passes, and a full-game intervention is separately declared.

40. [Guarded adaptive continuation](guarded_adaptive_continuation/PROOF.md) proves catalogue retention and equality with the parent fed the same actual observations after replacing only its opening. It does not imply a performance improvement.

41. [Appending attackers](append_monotonicity/PROOF.md) proves fixed-map damage monotonicity for appended active entries, including modulo-spawn wrapping, and justifies a bounded positive lethal-count search. The 64 paired original-combat fixtures and 64 finite threshold checks pass.

42. [Delayed policy switches](delayed_policy_switch/PROOF.md) proves public-history indistinguishability until the first substituted submission and the corresponding one-round rejection delay. The targeted full-game hypothesis is separate.

43. [A current empirical policy game](current_policy_game/PROOF.md) defines a paired five-policy table and its exact conditional maximin certificate, while separating observed clock-dependent outcomes from future expectations.

44. [Weak covering turrets](weak_covering_bluff/PROOF.md) gives two gun positions that satisfy positive route coverage yet cannot kill any standard copy. It separates this geometric fact from the proposed full-game bluff test.

45. [Fixed bluff placement census](bluff_placement_census/PROOF.md): a declared exhaustive family of all legal round-one gun1 cells, with both physical assignments.

46. [Roster bait](roster_bait/PROOF.md) proves when a round-two purchase first becomes observable and activates the frozen relevance predicate. Full-game harm is a separate hypothesis.

47. [Proposed openings against every affordable roster](proposed_opening_rosters/PROOF.md) proves exhaustive enumeration of the 27 ordered first-round rosters and checks both proposed openings on the unchanged engine. This is not full-game strength.

48. [Fixed-wall factory growth](maze_growth/PROOF.md) derives exact cash and factory recurrences for surviving, no-hit grower policies. It does not imply that a cash-maximizing maze wins a game.

49. [One splash guard on a grower's maze](guarded_maze/PROOF.md) proves tier1 arrival exclusion after a verified guard is installed. Delayed installation and full-game outcomes remain separate questions.

50. [Staged splash guards](staged_guards/PROOF.md) gives the exact pure-splash arrival formula for each legally built prefix and states the checked monotonicity condition needed to preserve previous HP thresholds.

51. [Guarded heavy-drip affordability](guarded_heavy_drip/PROOF.md) proves the exact schedule's cash lower bounds under a first-round hit and continued survival. Full-game transfer is separate empirical evidence.

52. [Public opening selection](public_opening_selector/PROOF.md) proves trajectory inheritance for stateless arms with a common first-round action list. The fitted selector has no out-of-sample or identification guarantee.

53. [Passive roster-cost threshold](passive_cost_threshold/PROOF.md) proves the45-gold first crossing of the proposed40-gold exemption, with explicit roster and observation hypotheses. Full-game consequences are measured separately.

54. [Passive-guard parameter equivalence](passive_guard_equivalence/PROOF.md) proves that nonnegative bait thresholds and turret-only relevance cannot change the stated no-early-minion, heavy-only counter trajectories in the exact v24 program.

55. [Sticky failed-attack adaptation](sticky_attack_failure/PROOF.md) proves the permanent conservative-mode selection under an explicit sub-immunity hypothesis, then separates the staged-guard diagnosis and full-game parameter interventions.

56. [Factory-relative passive exemption](passive_ratio_guard_equivalence/PROOF.md) proves cross-version equivalence of v24 and v25 on the stated empty-roster early histories, including the no-bait staged-guard counter.

57. [A guard upgrade ladder](guard_ladder/PROOF.md) applies the pure-splash arrival formula to checked extensions of the empty-layout guards and separates the second-failure counter hypothesis.

58. [A porous mixed guard](mixed_guard_ladder/PROOF.md) states the finite original-engine checks needed to stop one tier3 while retaining tier3 in the two best large-roster current-map choices. Full-game impact is separate.

59. [Screened timed guards](screened_guard_ladder/PROOF.md) accounts for the complete active roster and its spawn indices when searching a guard against the next tier3 purchase.

60. [Response candidate truncation](response_candidate_truncation/PROOF.md) states when the two-entry current-map shortlist omits an attack that passes the same response criterion.

61. [Guard handoff](guard_handoff/PROOF.md) states the observation boundary and legality of a filtered transition from the guard-growth opening to a frozen defender.

62. [v27 all-candidate equivalence](response_candidate_truncation/v27_equivalence/PROOF.md) gives the conditional cross-version argument and separates source inspection from full-history shadow checks.

63. [The converse of splash immunity](splash_converse/PROOF.md) gives a legal gun-only component with S=0 that kills one tier5, so the sufficient immunity threshold cannot be reversed.

64. [Public-HP defensive handoff](hp_handoff/PROOF.md) proves observation-only one-way trigger semantics and sequential action legality. Its strength and clock-dependent equality with fixed H10 are empirical questions.

65. [Forecast-specific defensive handoff](forecast_handoff/PROOF.md) proves the public-information boundary and action legality, with conditional forecast correctness. Repeatedly wasting an attacker's gold is a separate measured hypothesis.

66. [Standard-start forecast scope](forecast_standard_scope/PROOF.md) proves that synchronized copies of v28 stay on its deterministic standard planner; the clock-limited foreign fallback is relevant only when its trigger can be reached. This corrects the overly broad clock caveat in the frozen forecast-handoff experiment plan.

67. [Repeated purchases with zero damage](forecast_spending/PROOF.md) derives the finite-history consequence of nonnegative arrival damage and distinguishes full-policy forecasting comparisons from one-round effects or economic worthlessness.

68. [Early guard extension](early_guard_extension/PROOF.md) separates a legal construction insertion and checked defensive components from the full-game counter to an earlier strike.

69. [Cheap extensions to the two-splash guard](cheap_guard_search/PROOF.md): finite one-turret, one-wall component search with explicit limits on any minimum-cost claim.

70. [Minimum pure-splash extension](pure_splash_extensions/PROOF.md) gives an exact immunity criterion for a pure-splash map and the finite enumeration needed to certify the number of additions on the original guarded fixture.

71. [Handoff-counter transfer to early-defense repairs](nominee_handoff/PROOF.md) specifies a finite development comparison with deliberately unchanged forecast models and separates completed-policy effects from one-round claims.

72. [Disclosed handoff counters against fortress v36](fortress36_handoff/PROOF.md) declares the finite transfer comparison and its model-mismatch and clock limitations.

73. [Retargeting the handoff forecaster](retargeted_forecast/PROOF.md) proves exact standard-start predictions for a synchronized P5TNUBM clone and declares the separate four-game counter-repair hypothesis.

74. [Early heavy strike and defensive handoff](early_heavy_handoff/PROOF.md) proves observation-only action filtering and states the component and full-game hypotheses for a round-five tier4.

75. [Knowledge after an early heavy strike](early_heavy_knowledge/PROOF.md) defines matched visible-roster and mismatched-model interventions, with legality separate from empirical winning.

76. [Round-five single-building response](round5_heavy_defense/PROOF.md) defines a funded geometric minimum and a separate affordable one-round counterfactual, without a full-game guarantee.

77. [Budget-based defensive handoff](budget_handoff/PROOF.md) proves legal public-only construction of a finite pure-tier forecast set. It explicitly gives no universal mixed-roster or full-game guarantee.

78. [The nominee-counter policy game](nominee_counter_game/PROOF.md) defines four fixed policies, reuses three audited pairs and declares the missing pairs. Any cycle or mixed certificate is restricted to that finite game.

79. [Fixed budget-counter transfer](budget_handoff_transfer/PROOF.md) declares five targets and four unchanged model-free counters, separating the public-input proof from the transfer hypothesis.

80. [Public-HP-triggered budget handoff](triggered_budget_handoff/PROOF.md) proves a public one-way trigger and conditional equivalence to its realized fixed deadline, with full-game transfer tested separately.

81. [Triggered strike timing](triggered_budget_timing/PROOF.md) separates a fixed timing intervention from the public trigger and proves the round-four cash constraint.

82. [No-strike deadline controls](no_strike_handoff_controls/PROOF.md) states exact matched comparisons and the conditional full-history equality at a realized handoff.

83. [Nominee prefix equivalence](nominee_prefix_equivalence/PROOF.md) proves equal gameplay through round four under equal public labels. It makes no strategic impossibility claim.

84. [Guarded round-four strike](guarded_round4_strike/PROOF.md) proves the affordable empty-route gun component and declares the full-game intervention.

85. [Guarded-strike transfer](guarded_round4_transfer/PROOF.md) keeps the winning counter fixed across six new targets without assuming the gun lemma's roster hypothesis.

86. [Route-preserving defense ceiling](route_preserving_defense/PROOF.md) proves the off-route planner's unchanged route and an exact560 splash ceiling on the corner-gun map, with a stated fixed-map heavy-roster consequence.

87. [One-time wall insertion](handoff_wall_intervention/PROOF.md) separates legal snapshot reconstruction and unchanged controls from the full-game transfer hypothesis.

88. [Joint wall and turret handoff](template_handoff_defense/PROOF.md) changes only the post-trigger planner, preserving the public forecast and matched free-planner controls.

89. [Public first-roster selection](public_roster_selector/PROOF.md) proves the common first-round prefix and legal one-time selection, while marking its development-fitted threshold and transfer hypothesis.

90. [Public selector transfer to existing archetypes](public_selector_baselines/PROOF.md). Unchanged adaptive and forced branches,72 declared development games.

91. [Exact-count public selector](exact_roster_selector/PROOF.md). Forty declared games and old branch controls.

92. [Adversarial opening feature changes](roster_feature_spoof/PROOF.md). Thirty-two declared games with matched branch controls.

93. [Published entry-point consistency](best_entrypoint_equivalence/PROOF.md). Fresh direct and factory instances on exact recorded histories, including skipped opening calls.

94. [Independent fortress-table audit](team_fortress_report_audit/PROOF.md). Correct denominators, damage interpretation, and explicit missing-replay scope.

95. [Round-four public projection selector](round4_public_projection/PROOF.md). Delayed branch selection with a no-enemy-action projection; exact component checks are separate from full-game strength.

96. [Final reserved validation](final_reserved_validation/PROOF.md) states the exact finite counting argument, skipped-call continuation semantics, prespecified comparison and limits of pool C.

97. [Route-gated selection](route_gated_selection/PROOF.md): a disclosed-data repair of the projected early-attack rule, with exact old-branch controls; the repair and later aggressive challenge are both fully audited.

98. [Effective pool-C diversity](effective_pool_c_diversity/PROOF.md) separates nominal conditions from complete observed trajectories and proves why the skipped guard openings cease to differ.

99. [Aggressive route builders](route_feature_challenge/PROOF.md) challenge the public route gate with a declared96-game matrix and matched fixed-branch controls.

100. [Route selector transfer](route_selector_transfer/PROOF.md) tests the unchanged selector and both fixed branches against five additional frozen teammate policies.

101. [Indistinguishable public prefixes](indistinguishable_prefix/PROOF.md) tests two hidden continuations after exactly identical public histories and states the restricted binary-selection bound.

102. [Emergency defense after an early strike](emergency_after_strike/PROOF.md) adds a public visible-damage trigger while preserving the round-four choice; component and full-game checks are separate.

103. [Emergency continuation transfer](emergency_transfer/PROOF.md): declared 90-game comparison on the preceding 45-target development union.

104. [Delegated defensive continuation](delegated_defense/PROOF.md): exact common opening, public handoff, and component/full-game comparison of frozen teammate defenders.

105. [Frozen-delegate transfer](delegated_transfer/PROOF.md): both continuations on the entire 45-target development union, with paired old controls and independent public handoff reconstruction.

106. [Timing challenge for the frozen defensive handoff](delegated_timing/PROOF.md): thirty fixed timing/defensive-budget settings, two continuations and both assignments.

107. [Public-clone adversary for the adaptive counter](delegated_forecaster/PROOF.md): a conditional forecast argument, component checks and an eighty-game fixed timing challenge.

108. [Forced early branch against public clones](forced_early_forecaster/PROOF.md): paired intervention with a correctly updated private target model; four component prefixes and forty full games planned.

109. [Recent teammate transfer and branch ablation](recent_transfer/PROOF.md): six pinned targets, three unchanged selector modes and both assignments.

110. [Fixed policies after counter adaptation](latest_counter_game/PROOF.md): a declared three-policy game with a single unchanged counter model, explicit self-play, reused edges and a conditional rational mixture certificate.

111. [Defended opening budget](guarded_opening_budget/PROOF.md): an exact cash identity and finite original-combat search for early defense without losing the round-four heavy purchase.

112. [Earlier walls and the round-four heavy budget](guarded_opening_wall_timing/PROOF.md). Declared finite component search after the negative round-three-only result.

113. [Bait and guard schedule transfer](bait_guard_transfer/PROOF.md). Original fortress reproduction and transfer to five other fixed defender specifications.

114. [Early-wall guard policy](early_wall_policy/PROOF.md). Eight component-derived openings with frozen Fortress38 continuations, teammate transfer and updated public clones.

115. [First early-wall witness transfer](early_wall_transfer/PROOF.md): full previous forty-five-target union, paired controls and four additional counters.

116. [Early-wall public-clone timing grid](early_wall_forecaster/PROOF.md): forty new matching-model games and explicit adaptive/early controls.

117. [Reused pool C independent execution](reused_c_validation/PROOF.md): fixed best_v9f comparison with all selection effects stated.

118. [Living cleanup counterexample](late_copy_cleanup/PROOF.md): legal nine-round original-engine prefix,249kills and one living clearance; corrects the literal all-copies-die statement without changing splash immunity.

119. [Terminal reserve D](terminal_reserved_validation/PROOF.md): prospective96-condition final report protocol; no candidate execution before23:00Z and final selection.

120. [Fixed-schedule bait removal](bait_removal/PROOF.md): delete only three tier1 purchases,24newgames and24audited controls.

121. [Early-wall round-four purchase ablation](early_wall_attack_ablation/PROOF.md): no purchase or tier3 versus the tier4 control, with a common factory and continuation rule;28newgames onsevenfixedtargets.

122. [Five fixed counter policies](extended_counter_game/PROOF.md): expand the earlier cycle with the early-wall guard and its HP-triggered counter, test the old mixture and certify any new finite-game solution by exact arithmetic.

123. [Guarded round-four strike against best_v9f](guarded_round4_best9f/PROOF.md): unchanged half/full-budget counters, four new games and four explicitly reused best_v9e controls.

124. [A public-roster-gated extra attack](early_wall_followup/PROOF.md): three fixed round-five packages, thirty new games and ten reused controls; all choices declared before execution.

125. [Decision-timing accounting](decision_timing_accounting/PROOF.md): reconciles144completedCconditions, corrects wrapper-versus-policy labels, and checks the Dpublisher accounting without running D.

126. [A targeted clone challenge of the HP grower](hp_handoff_forecaster/PROOF.md): twelve matching-model policies against fixed H, both assignments, with component gates and full-game checks.

127. [Exact overlap-audit input snapshots](audit_input_snapshots/PROOF.md): preserve the bytes named by audit hashes even after append-only team result streams grow.

128. [A sixth fixed counter policy](six_policy_game/PROOF.md): ten new games and thirty-two reused games test the transfer of a private-model change and extend the exact finite table.

129. [Classified artifact-path audit](artifact_path_audit/PROOF.md): preserve a failed lexical scan, redact one outer traceback path, and distinguish an exact frozen generic rejection guard.

130. [A response selected after a shared first move](shared_prefix_response/PROOF.md): fourteen new games test a public round-two selector against the six prior policies and itself.

131. [Fixed counters against af2g](af2g_fixed_counters/PROOF.md): ten new games and ten old controls, with all five counter specifications fixed before new execution.

132. [Manipulating a public wall signal](wall_signal_response/PROOF.md): twelve new games compare two adjacent wall counts against the selector and both fixed-response controls.

133. [Seven-policy finite-game certificate](seven_policy_game/PROOF.md): exact reanalysis of 56 already checked games after adding the public-response selector; no new policy calls.

134. [Delayed twenty-wall timing attacks](wall_signal_delayed/PROOF.md): four heavier or later purchases against the public selector and both fixed controls, 24 new games.

135. [Wall-signal defense feasibility](wall_signal_defense_diagnosis/PROOF.md): selected first-leak states, fixed alternative planners and original-engine one-round witnesses.

136. [Wall-signal defensive repair](wall_signal_repair/PROOF.md): a guarded free-planner fallback, six complete-policy tests and six reused controls.

137. [Eight-policy extension](eight_policy_game/PROOF.md): ten new games after the fixed L repair, 62 reused controls, exact finite-table verification.

138. [Public-label and player-index invariance](identity_invariance/PROOF.md): all72 retained C histories, two fresh transformed factory instances per history,2208 actual calls and no action differences; no new games.

139. [Exact affordable-roster coverage](affordable_roster_coverage/PROOF.md): 13658 original-engine interventions on100selected reached states; two zero-sample counterexamples from one paired state.

140. [Screened roster continuation](screened_roster_continuation/PROOF.md): three orders of the same package and three fixed continuations against frozen best_v9e;18full games declared before execution.

141. [Five-wall component guard](screened_roster_wall_guard/PROOF.md): five fixed original-engine interventions preserve the26damage attack while testing protection against the return hit.

142. [Guarded screened-roster policy](screened_roster_guarded_policy/PROOF.md): six new full games and six reused controls after the five-wall component selection.

143. [Exact wall-cost verification](screened_guard_minimum/PROOF.md): all wall sets of cardinality0 through4 on the selected fixed-action state, with exact domain checks and original-router/Engine witnesses.

144. [Screened-guard transfer](screened_guard_transfer/PROOF.md): 24 declared games against six frozen finalists and revisions, with matched unguarded controls.

145. [Purchase-order mechanism](screened_order_mechanism/PROOF.md):750 original ticks and an independent target/HP observer explain the known round-six difference; includes an inspected static figure and worked explanation.

146. [Forecast-defense diagnosis](screened_forecast_defense/PROOF.md):six fixed-state interventions distinguish visible and post-submission rosters at the two AS1C loss states; no full-game or admissible-forecast claim.

147. [Stronger screened continuations](screened_continuation_repair/PROOF.md): twelve new games and four reused controls; no tested continuation beats AS1C, while Fortress41 preserves the two best_v9e wins.

148. [Ten-policy extension](ten_policy_game/PROOF.md):34 new games and76 reused records test the old mixture against the screened counter and AS1C, with exact certificate checks.

149. [Independent backward-route audit](reverse_route_audit/PROOF.md): all14,901,218 scores rescored by a different routing algorithm, plus11,097 full original-Python path checks.

150. [Visible-gold runtime](visible_gold_runtime/PROOF.md):reproduce100 final-candidate calls on two retained high-factory histories and distinguish wall time, CPU time and linear threat-list size.

151. [Native immunity shortcut](immune_runtime_shortcut/PROOF.md): a source-reviewed response-preserving optimization, with74 retained histories declared for fresh action, state and runtime comparison. The original overbroad proof and its scope amendment are retained.

152. [Shortcut boundary and unpaired timing follow-up](immune_shortcut_followup/PROOF.md): exact terminal stream checks on74 inputs,100 shortcut-only calls and a separate sampled-leak component profile.

153. [Second shared-prefix selector](wall_prefix_selector/PROOF.md): a common20-wall opening chooses G or L from completed public round-one state;22 predeclared games test the ten-policy mixture and every old opponent.

154. [Delayed public wall signal](delayed_wall_counter/PROOF.md): G walls shifted to round2 force O's L branch; ten prospective games against O/L/G/B/N, both assignments. The signal and early economy both change.

155. [Reserved delayed-wall strike](reserved_wall_counter/PROOF.md): withholding two round-three factories restores the round-four heavy purchase; ten games and matched P controls.

156. [Support-only finite certificate](support_only_certificate/PROOF.md): half G, half O has exact value zero for every skew completion of the partially measured twelve-policy game; 46 existing replays, six unplayed P pairs and unplayed P self explicitly separated.

157. [Two-round selector](two_round_wall_selector/PROOF.md): exact shared first-two-round actions, persistent member selection, and a conditional finite support-row certificate. All28games and selected controls pass; read RESULTS.md and CONTEXT.md for measured scope and publication recovery.

158. [Late reserved-wall counter](late_reserved_wall_counter/PROOF.md): all ten games and 712 fresh decisions checked; S beats R/L, draws G and beats B/N in both seats. Exact route, reservation and full-history transfer checks pass.

159. [Delayed-signal ambiguity](delayed_signal_ambiguity/PROOF.md): all twelve retained histories replayed with zero policy calls. The measured table supports the exact conditional restricted value -1/3 at probability 2/3 of G; full continuation coupling remains a hypothesis. Read EXPLANATION_v2.md, PROOF.md and RESULTS.md.

160. [Wall-timing transfer](wall_timing_transfer/PROOF.md): all24 new games and eight G/N controls audited;2400 fresh external calls. S and Q have equal WDL in all16 matched conditions, although S has worse HP against H. Both-seat histories and exact openings pass. Read RESULTS.md for scope.

161. [Fourth-round selection](third_round_wait/PROOF.md): all four T/H,S games and two original G/S controls audited, 400 fresh external calls. T wins H 800:656 and draws S 740:740 in both seats; all four hypotheses pass. Read RESULTS.md for the exact scope.

162. [Blind fourth-round control](blind_fourth_round/PROOF.md): all four new U/H,S games and four retained T controls audited, with 248 fresh external calls. U/H completely reproduces T/H; U/S loses -246:800 at round12 in both seats while T/S draws740:740. All four hypotheses pass. Read RESULTS.md for the exact scope.

- 2026-10-31T22:24:06.777212+00:00: [Exact frr1 equilibrium](frr1_equilibrium/INDEX.md) independently verifies the optimal face of the recorded ten-policy matrix. Zero self-play diagonal is imposed, not measured; no new games or policy calls. [Prospective fourth-round wall counter](fourth_round_wall_counter/INDEX.md) has a checked conditional first-five-round proof; full-game outcomes remain open.

- 2026-10-31T22:30:02.989886+00:00: [Fourth-decision ambiguity](fourth_round_ambiguity/INDEX.md) has a reviewed shared-prefix lemma and exact conditional bound for selecting G/U against H/V. Numerical V application remains open.

163. [Fourth-round wall counter](fourth_round_wall_counter/INDEX.md): audit completed2026-10-31T22:37:11.017297+00:00; ten games and696 fresh external decisions audited. V wins againstT/U in both seats and loses againstG/B/N in both; first-five private mechanism verified, later clock coupling remains conditional.

164. [Fourth-decision ambiguity](fourth_round_ambiguity/INDEX.md): eight retained complete replays and24 opening steps, no policy calls. Both physical-seat tables are G/H=-1,U/H=+1,G/V=+1,U/V=-1; the restricted conditional optimum is halfG,halfU at value0. Read PROOF.md and RESULTS.md for the continuation hypothesis.

## Completed evidence and finite-matrix supplements

Published 2026-10-31T23:45:27.127092+00:00.

- Read the [exact frr1 equilibrium](frr1_equilibrium/INDEX.md), then the [one-row fortress extension reading order](../reviews/frr3_extension_review_001/INDEX.md) and its [standalone proof](../reviews/frr3_extension_review_001/PROOF.md), followed by the [final two-row extension index](../reviews/frr5_frr6_final_fortress_001/finite_matrix_extension/INDEX.md) and [completed frr5/frr6 review](../reviews/frr5_frr6_final_fortress_001/README.md). These are conditional results for the specified finite matrices, with zero self-play entries imposed. The final proof allows any unmeasured skew mutual entry between the two added fortress rows; it does not supply that matchup as measured evidence.
- Completed late adaptation evidence is in [T results](third_round_wait/RESULTS.md), [U results](blind_fourth_round/RESULTS.md), [V's worked explanation](fourth_round_wall_counter/EXPLANATION.md), [V results](fourth_round_wall_counter/RESULTS.md), and the [fourth-decision ambiguity application](fourth_round_ambiguity/RESULTS.md). The corresponding preparation indexes and their OPEN statements retain their historical meaning. The application still assumes correctly advanced state and full selected-continuation payoff coupling.
- The [completed terminal D result table](terminal_reserved_validation/RESULTS.md) accompanies [the validation guide](VALIDATION_FINDINGS.md) and its linked independent evidence. Read standard starts and the two prescribed continuations separately.
- Added 2026-10-31T23:56:09.904827+00:00: the [AF5 finite-matrix reading order](../reviews/frr7_frr8_late_af5_001/af5_matrix_extension/INDEX.md) leads to its [standalone proof](../reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md) and [independent record and rational checks](../reviews/frr7_frr8_late_af5_001/root_review_002.json). In the specified eleven-policy WDL matrix, every optimal mixture assigns one third each to AF5 and the guard, and splits the remaining third between P5 and AS1C. The seven other policies have zero weight. The proof also allows the two added fortress rows with unmeasured AF5 entries and their mutual entry under its stated bounds. This is a conditional finite-table result. For the associated frr8 games, use the [HP erratum](../reviews/frr7_frr8_late_af5_001/hp_erratum_001/ERRATUM.md) and its [independent recount](../reviews/frr7_frr8_late_af5_001/root_hp_erratum_review_002.json): AF5 finishes 790:735 in both seats. The original sealed review retains its incorrect 795:740 sentence as historical evidence.
- Added 2026-11-01T00:00:58.681366+00:00: the [foreign attack-gate reading order](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/INDEX.md) links a [conditional source proof](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/PROOF.md), [retained-history review](../reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/REVIEW.md) and [independent recount](../reviews/frr7_frr8_late_af5_001/root_foreign_gate_review_001.json). The ordinary AF5/g1 attack helper checks the foreign-map hold; finishing and doom have separate predicates and no such check. No legal-game counterexample is established. The 45 retained histories contain no accepted minion purchase in the 356 inspected rounds after the scripted opening and before round 11. This corrects the shared-guard explanation without changing the separate 120-condition outcome comparison.
