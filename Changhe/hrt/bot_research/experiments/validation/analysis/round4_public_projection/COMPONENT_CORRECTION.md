# Projection component correction

Recorded 2026-10-31T16:07:35.043129+00:00.

The first prefix-only receipt, verification/prefixes.json, checked action-prefix equality but did not independently verify projected HP. Review found that simulate_map mutates the defender's HP. The initial implementation read HP after simulation and subtracted damage again. No full game used that implementation.

The corrected source captures both starting HP values before either simulation. check_projection_prefixes now independently reconstructs each prefix with a separate original Engine, submits the early proposal and an empty opponent action list, and checks both damages, own terminal HP and HP difference. The new receipt is verification/prefixes_corrected.json. The original source and checker are preserved as reviews/projected_lead_selector_v1.py and reviews/check_projection_prefixes_v1.py. The old numerical projections are superseded.
