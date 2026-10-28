# Audit clarifications

Recorded 2026-10-28T14:38:37.834972+00:00. The independent audit gives PASS WITH REMARKS. Its proof hash matches the current PROOF.md.

The low-band Taylor derivatives are Q_xxy and Q_yyy, linked by Q_xxy=-Q_yyy+g_yyy. Note70's shorthand Q_xx is corrected here. The sharpness cutoff is a fixed smooth profile rescaled to radius b delta, with |D^j chi_Q|<=C_j delta^(-j). The axis function series also converges absolutely since |Q_j(0,y)|<=CM 2^(-j(2+alpha)); its derivative series converges uniformly and identifies the canonical strain. The available actual regularity is C^(4,1), and both parities exclude degrees2 and4. All constants are for fixed alpha, with delta small enough for every fixed local disk and cutoff.

Remark12's optional multiplier sharpening is proved separately in proof 215. It improves the actual-variable Neumann error to O(delta^2), without changing proof 212's already correct upper bounds or its operator scope.
