# Explicit-mode verification

Date: 2026-10-29T03:23:08.575329+00:00. The theorem remains OPEN pending independent Opus review.
The local check is FLOAT diagnostic evidence only. It is not used as a
proof of the analytic inequalities or an endpoint statement.

For f(r)=r^M exp(-r^2), the positive-mode Beurling radial output is
exp(-r^2)[r^M-(M-1)r^(M-2)] (g=f for M=1); the negative-mode output is
-r^(-M-2) gamma_lower(M+2,r^2). Differentiating these explicit expressions
checks the radial ODE independently of numerical differentiation.
The script integrates input/output gradient energies and the signed
identity on the whole half-line, with M=1,3,7 and eight weights.
All24 real-pair tests and2828 pointwise potential comparisons pass.
At p=0 all unweighted ratios are1 to quadrature precision.
Real computation time0.121207251seconds.

Output SHA256 da6f24ea6169f8137dba85ddb06777bf7759e924288b3d2a915fb127ca73703f.
