# P301: runtime24/48 comparison against the independent full-plane reference

UTC 2026-10-22T07:07:01.253644+00:00. Verdict CONFIRMED103/103 for conditional scalar comparisons. The runtime component arrays, historical CLI and source hashes are absent; their reconstruction remains OPEN. General B2 remains OPEN.

The frozen12/24file has ng_ref=12,ng=24; the24/48file has ng_ref=24,ng=48. Both label the K48,beta3.092 state,lambda0.9326700862338395. The generic key max_U48 means M24 in the first file and M48 in the second. Current read-only source confirms Cartesian component maxima per radius, shared radius loops and default181interiorangles. No NUMcode was executed. Its angular convention matches the independent P291 quadrature, conditional on historical default use.

At r=1e9: reported M24=5111809.838148594, M48=5111888.351475239; independent numerical Mref=3906358.98233997. Reported D24,48=110.68851709365845, only 2.16531562278e-05 of M48. Yet |M24-Mref|/Mref=0.308586809676 and |M48-Mref|/Mref=0.308606908527. Thus the two runtime orders agree much more closely with each other than with the independent reference. This is a conditional numerical comparison, not an enclosure of the true inverse error and not a diagnosis of its cause.

Reported D12,24=4058426.4509415627 and D12,48=4058537.1394586563 are compatible with the triangle inequalities. The comparisons at all eight radii and arithmetic details are in verification/COMPARISON.csv. Scalar compatibility uses an explicitly recorded tolerance1e-10 times the largest compared norm; at1e9 this is0.000511188835. That tolerance is only for reported-number rounding, not an accuracy bound. The direct lower bound |M24-Mref| always dominates the transferred bound max(0,|M48-Mref|-D24,48).

The proof is complete before controls. Own checker code_independent/check_runtime_24_48_comparison.py SHA81b25be73a7044089cfe8ab9459f160c145adffaf2c900450d495fbc4e39e88b ran 2026-10-22T07:03:52.360659+00:00 to 2026-10-22T07:03:52.362631+00:00 in0.001966s. Initial103/103 retained before the per-radius and bound-domination proof clarification; unchanged arithmetic rerun103/103.

Actual Opus519,520,521,523 all returned claude-opus-5-5. The exchange verified norm inequalities and source interpretation; three review overstatements and one wrong bound comparison were rejected and corrected. Full adjudication is in verification/OPUS_ADJUDICATION.md. Finite two-order changes do not establish quadrature convergence or bound a common bias;48/96NaNs are not used or diagnosed.
