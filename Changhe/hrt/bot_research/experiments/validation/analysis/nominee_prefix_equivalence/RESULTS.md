# Equal gameplay prefixes do not prove a strategic impossibility

Checked 2026-10-31T15:34:47.685820+00:00.

CONFIRMED under the exact hypotheses in PROOF.md: P4TNUB and P5TNUBM have identical gameplay histories through round 4 and identical observations before round-5 submissions, when their public labels are equal. The proof is a source specialization and induction on engine transitions. The verifier confirms that removing the inactive v30 additions yields the v28 syntax tree, checks the shared parameter relation, and reproduces twelve equal four-round prefixes on the original engine, covering six other policies in both assignments. These finite samples support the implementation check; they do not replace the induction argument.

This rules out identifying which nominee is present from those gameplay observations alone before the round-5 action. It does not prove that no one policy can beat both. The same legal action might be effective against both, and later decisions may adapt to their divergent histories. Any claim that insurance or an attack has an unavoidable loss tradeoff needs a separate payoff argument over the relevant legal choices.

The equal-label hypothesis is necessary for this information claim. Engine.snapshot exposes each player's name, and the development runner normally uses its full specification as that name. A policy allowed to read those names can identify a specification before gameplay diverges. The current counter does not use that shortcut. Final evaluation should distinguish gameplay adaptation from identity-based selection, and no benchmark secrecy claim follows from the interface.

The formal source hashes, exact parameters, all twelve prefixes and checker source hash are in verification/prefix.json. Run check_nominee_prefix_equivalence with a fresh output path using .venv/bin/python -B from the project root, bytecode disabled, temporary files under bot_research/tmp, one thread, low priority and assigned affinity. No held-out conditions were used.
