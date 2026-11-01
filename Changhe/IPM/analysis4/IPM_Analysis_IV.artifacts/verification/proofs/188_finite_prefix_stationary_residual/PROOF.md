# A finite, exact upper bound for the stationary truncation residual

Status: PROVED. Independent analytic review is closed inV376; exact arithmetic examples were confirmed inV367.

## Statement and hypotheses

Fix c>1 and delta=1-1/c. Let J>=1 be an integer. Suppose the finite trigonometric polynomials f_n,g_n, 1<=n<=J, satisfy the pure stationary recurrence and angular Poisson equation from the problem statement, with p_n=1-n delta and P_n=2-n delta. In particular, for 2<=n<=J,

    (n-1)(c-1) f_n = sum_(i+j=n) [P_i g_i f_j' - p_j g_i' f_j],

and each homogeneous pair satisfies -Delta(r^P_n g_n)=d_x(r^p_n f_n). The sums use ordered pairs. Assume all frequencies in f_n,g_n have magnitude at most Bn. Let alpha_n>=||f_n||_1 and beta_n>=||g_n||_1 be nonnegative certified rational upper bounds in the angular Wiener norm. No infinite convergence assumption is needed for this finite statement.

Define the truncated fields

    rho_J = sum_(n=1)^J r^p_n f_n,
    psi_J = sum_(n=1)^J r^P_n g_n,
    u_J = (-(psi_J)_y, (psi_J)_x),

and the stationary residual

    R_J = c r d_r rho_J + u_J . grad rho_J - rho_J.

For J<n<=2J set

    C_n = sum_(i+j=n, 1<=i,j<=J)
          (|P_i| B j + |p_j| B i) beta_i alpha_j.

For nonnegative integers a,b and z>0 define

    T_(a,b)(z) = sum_(n=J+1)^(2J)
                 z^(n-1) |p_n|^a (Bn)^b C_n.

The convention x^0=1 includes x=0. With gamma=1-delta, every r>0 obeys

    r^(-gamma) ||(r d_r)^a d_theta^b R_J||_1
      <= T_(a,b)(r^(-delta)).

Consequently, T_(a,b)(R^(-delta)) bounds this weighted norm on the entire exterior r>=R. The Poisson residual -Delta psi_J-d_x rho_J vanishes identically. All bounds are rational whenever delta, the norm upper bounds and z are rational. If an actual convergent solution with this prefix is known independently, this is its finite truncation residual; the statement itself does not prove that infinite solution exists.

## Complete proof

The polar identity

    u_J . grad rho_J
      = r^(-2) [(r d_r psi_J) d_theta rho_J
                - (d_theta psi_J) r d_r rho_J]

gives an ordered pair (i,j) the radial degree P_i+p_j-2=1-(i+j)delta=p_(i+j). The linear term on order n is

    (c p_n-1) f_n = -(n-1)(c-1) f_n.

Its n=1 value is zero. At each order 2<=n<=J the recurrence cancels it exactly against the ordered quadratic sum. There are no linear terms at orders n>J and no quadratic terms at orders n>2J. Thus the exact residual is

    R_J = sum_(n=J+1)^(2J) r^p_n
          sum_(i+j=n, 1<=i,j<=J) [P_i g_i f_j' - p_j g_i' f_j].

The angular Wiener norm is a Banach algebra. The bandwidth assumptions imply ||f_j'||_1<=Bj alpha_j and ||g_i'||_1<=Bi beta_i. Triangle inequalities therefore bound the norm of the nth bracket by C_n. Its bandwidth is at most B(i+j)=Bn, since differentiation preserves support and multiplication adds supports. Taking a Euler derivatives multiplies r^p_n by p_n^a; taking b angular derivatives increases its norm by at most (Bn)^b. Finally r^(p_n-gamma)=r^(-(n-1)delta)=z^(n-1). Summing proves the claimed bound. Each power n-1 is positive, so T_(a,b) increases in z and its value at R bounds every r>=R. Linearity of the Laplacian proves the exact Poisson cancellation.

## Amplitude, data and scope

For a normalized leading profile with homogeneous coefficients of degree n, an amplitude epsilon changes each term in C_n by |epsilon|^n. Thus the bound is |epsilon| T_(a,b)(|epsilon|r^(-delta)). This finite statement applies for every nonzero real epsilon; the zero amplitude case is trivial.

A convenient certified choice is beta_n=L alpha_n+|H_n|_upper from the proved Poisson estimate. This requires H_n at every resonant order n<=J. A prefix certificate that has not yet tuned H_N at its last order N must use J<=N-1, or separately obtain H_N. It is not valid to silently set the final free harmonic to zero. Finite residual smallness by itself is neither convergence nor an error bound to a true infinite solution.

## Dependencies

Only the exact recurrence and Poisson identities in the problem statement and the elementary Wiener product and bandwidth estimates are used. Sources for numerical norm bounds and every retained exact arithmetic evaluation must be listed in the verification artifacts.

## Exact arithmetic examples

At 2026-10-31T13:59:53+00:00, V367 confirms the arithmetic: Four finite prefixes yield exact upper bounds for stationary residuals and all mixed Euler/angular derivatives of total order at most3. Independent replay checks4,086 ordered pairs and40 derivative bounds; a symbolic one-mode calculation confirms the sign and factors. For the two-mode root4 at J35,R=2^(135/4), the density-weighted residual is <2^-496; for Candidate-shaped root1 at J26,R=2^(171/4), it is <2^-466. Q5root5 at J50,R=2^35 gives <2^-660; Q6root6 at J60,R=2^45 gives <2^-765. The weight is r^(-gamma), and the bounds are uniform on the stated closed exteriors. Evaluation took1.3088831882923841seconds; replay took11.691869120113552seconds. Independent analytic review remains pending.

## Independent analytic review, 2026-10-31T14:07:17+00:00

The theory part independently checked the polar identity, every radial exponent and cancellation, the ordered-pair limits, Wiener estimates, amplitude homogeneity and the final-harmonic condition. The retained review also reports a separate Cartesian numerical check, which is supporting evidence and is not needed for the proof. All analytic steps are confirmed.
