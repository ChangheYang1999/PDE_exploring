# Definition and endpoint clarifications

2026-10-21. Read with PROOF.md. These clauses make the domains and the modulus at zero explicit.

The formula F is defined on the larger unnormalized kinematic class in which the continuous center factor may have any finite real value. Every other regularity, canonical velocity and growth condition is retained. The normalized class used in the theorem is its subset with factor value1. Thus F(rho_s), the full linearization L_s at rho_s, and F(q_delta) all have literal meanings, even though J(rho_s)=s^-2. Only q_delta is required to be normalized. Sigma is the canonical linear functional, and the rank-one term in L_s is Sigma(h)E rho_s/3.

The prohibited modulus means a map omega:[0,infinity)->[0,infinity) with omega(0)=0 and lim_(t down to0)omega(t)=0. The value at zero is explicitly included, so the argument applies even if some residuals vanish exactly. An arbitrary discontinuous assignment omega(0)>0 is outside the claim. No monotonicity of omega is needed.

The norm X is a space of function classes identified almost everywhere, with distributional first derivatives, finite displayed weighted integral and the usual norm identification. All functions used in this proof are locally C1, so their distributional derivatives equal their classical derivatives. Nonzero continuous functions on an open set represent nonzero X classes. This justifies d_s>0 from the nonzero center factor: choose a small sector away from the axes and use uniform continuity of that factor.

The two-scale compact stream was recomputed by piecewise Green integration and by an independent exact4x4 radial ODE matching solve, at both stream modes2 and4. All stream coefficients agree, as do28 derivative traces through order6 at radii1 and2. The second method also checks12 full radial density traces through order5. The strain is zero both from the inner stream coefficient and from a separate radial moment integral. Its outer stream is (5/1008)r^-2 sin(2theta)+(1/160)r^-4 sin(4theta).

The constants S1,S2,C_H are independently recovered from Cartesian binomial expansions, derivatives and absolute coefficient sums. In the notation of PROOF,

    A_Q=2060256330/7,
    B_Q=23661731790/7,
    4(A_Q^2+B_Q^2)=2256488829788806692000/49.

Arb512 and mpmath.iv180 each verify 2sqrt(A_Q^2+B_Q^2)<6800000000, with exact interval endpoints retained. Hence the explicit compact-family estimate may also be written

    ||U[b_delta] dot grad b_delta||X
         <6800000000 sqrt(pi C_w) delta^3

for delta>0 in the stated range. This deliberately coarse constant is sufficient for convergence; it is not a useful general nonlinear closing constant and is not a bilinear bound on X.

The first informal draft used s^3 for the stream of s rho(X/s); the correct factor is s^2. The error was found and corrected before any new computation or model review. The original draft and proof-first record are retained in evidence. An initial computation had a redundant axis-zero check and an unused branch; the source and result are retained, and the cleaned source was rerun before the independent comparison. Neither affects a claimed identity.

The first actual Opus5.5 review reached its output token limit before listing its qualifications. It is incomplete and cannot authorize finalization. Its raw result remains part of the history. A completed follow-up must audit this addendum and the full current bundle.
