# Prospective code-test audit

Registered 2026-10-29T18:40:16.362549+00:00. Proof SHA256 76007dc400c0fad0bb5875050112b40bb9a5c4b7e8e8ff608215f45f2dd0bde9.

Capture the numerics side's current pressure code-test function and exact source hash. Reproduce its Gaussian radial expressions on the production holdout radii of the P1 segment-3 endpoint with the same mode degrees, eps in {1e-3,2e-3,4e-3} and scales R0,64R0. Evaluate shell RMS independently from modal orthonormality and retain all shell values, underflow omissions and the largest relative error. Compare the source-extracted angular implementation if feasible. Do not change a threshold or step after observing the result. This is a manufactured code check; no campaign-state pressure clearance is attempted.

Use the serial pause wrapper when numerical imports or execution are needed. One CPU35 computation, one thread, no GPU. Do not execute production main or write outside this side.
