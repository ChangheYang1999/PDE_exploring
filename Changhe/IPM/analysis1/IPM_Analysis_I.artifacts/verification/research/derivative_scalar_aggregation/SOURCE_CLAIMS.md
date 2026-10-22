# Exact frozen report excerpts

These excerpts are copied from the frozen NUM_REPORT.md; their claims are being checked, not adopted. The full file digest is 6d2e73bd269ce91814f037feaf42d59fe124b56921b5c7e9fc39bff4391142b2.

Cartesian derivatives follow from d_x = e^{-t}(cos th d_t - sin th d_th),
d_y = e^{-t}(sin th d_t + cos th d_th): r |grad eps~| <= W_1_0 + W_0_1 and r^2 |d^2 eps~| (any second derivative) <=
W_2_0 + 2 W_1_1 + W_0_2 + W_1_0 + 2 W_0_1 pointwise on the cell. Division by the certified cell minimum

R5: ||eps~ - X.grad eps~||_{R0 norm} = sup W_eps_minus_dteps/m <= 0.427 (middle region); ||K~||_{R0 norm} = sup W_K/m <= 450.8 with
K~ = rho~ - X.grad rho~ (K~ is of the size of rho~ itself, L^3 m ~ 448 m at small r), ||d_t K~||/m <= 2119.
R3 (P-disc

With the middle (7809 cells), outer (8948) and
inner (2632) regions, the first and second derivative norms of the residual are now bounded rigorously on the whole plane except the two tails
(r < 5.155e-5 and r > 8.228e10, where only the zeroth-order majorants of 7.3 are available): sup over 5.155e-5 <= r <= 8.228e10 of r|grad eps~|/m
<= 0.4195 and of r^2|D^2 eps~|/m <= 713.2, both attained at the lobe next to P (r = 8.78); away from the shell [4, 16) the suprema are 8.559e-3 and
4.516 (middle shell [16, 64)), 4.169e-3 and 1.122 (outer), 2.762e-4 and 1.396e-2 (inner). Whole-plane status: chain6 complete
