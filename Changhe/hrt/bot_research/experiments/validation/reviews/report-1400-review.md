# Review of the 14:00 report snapshot

Date: 2026-10-31T14:03:45.287811+00:00

Reviewed snapshot: `report-1400-snapshot.md`, SHA-256
`501c06ff72f2b0d1c9745da6ad20981f665ffbf95864a178174a0f7df7ca1e77`.
This review concerns that snapshot, not subsequent edits. The report was read
in full. Its separation of development evidence from reserved validation,
explicit negative results, and condition-specific selection rule should be
preserved. The following corrections affect the precision of its claims.

1. REFUTED: line596 uses S < 1500 to infer tier5 arrivals "by P1".
   P1 is a sufficient condition for immunity, not its converse. Guns may kill
   copies even with S=0; late spawn phases may also prevent arrival. The
   original-engine component in `analysis/splash_converse/PROOF.md` and its
   verification file has five gun3 turrets, S=0, and one tier5 killed. The
   same copy hits an empty control map for140. Replace the parenthetical
   with "below P1's sufficient immunity threshold" and retain the recorded
   round12 damage as the empirical evidence for leakage. This correction
   does not dispute the reported840 damage in the actual loss trace.

2. REFUTED as literal source claims: lines96-100 say all imported policies
   use no randomness and no wall-clock cutoff. The econ20 branch imports
   defense/v26/replan.py, which uses `random.Random(seed)` at line108. Its
   fixed seed and fixed iteration count give reproducible pseudorandom
   choices. More importantly, econ20 passes a finite `plan_time=1e6` to
   defense/v15/plan.py; that planner forms and checks an actual wall-clock
   deadline (lines543,575 and475). A million-second cutoff is irrelevant
   to the recorded calls but is not an absent cutoff. State the distinction:
   the normal branch has no time cutoff; the foreign-map branch uses a
   fixed-seed replanner and a million-second gun-planning cutoff, not reached
   in these runs. This also qualifies lines807 and1043, and the corresponding
   prose in the frozen best_v9e docstring. The source need not be changed to
   correct the report. New F34/F35 and guard-handoff opponents retain a
   three-second gun-planning cutoff; include them if their results enter the
   final report. Observed equal seat histories do not remove that limitation.

3. OPEN without a map-completion argument: lines547-548 conclude from P1
   that an S>=180 splash-only answer exists at bounded cost. P1 proves the
   answer works if such a legal completion exists. It does not construct a
   completion around arbitrary permanent buildings. Restrict the statement
   to a proved layout-completion hypothesis, give the explicit completion,
   or remove the existence clause. Suggested wording: "A map reaching
   S>=180 would stop every tier1-tier3 roster; the planner searches for an
   affordable completion and may also choose guns."

Before publication, mark historical states as historical. In particular,
old statements that a setting "is best.py", that a pool is unused, and that
jobs are queued should not read as current after later sections supersede
them. The final summary should identify which exact frozen source has each
reserved-pool result; neither the best_v9a pool-A result nor the best_v9b
pool-B result transfers to a later source. For validation pools, use
"withheld until first unblinding" rather than an unqualified "not used for
tuning" if any disclosed conditions later enter development.

The review uses the research-storytelling guidance on evidence-first
exposition and explicit limits. It does not ask for a wholesale rewrite of
the useful development history. No report-owner file was modified.
