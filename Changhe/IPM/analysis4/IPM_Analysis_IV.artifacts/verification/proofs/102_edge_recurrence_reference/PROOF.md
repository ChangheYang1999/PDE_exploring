# Exact reference for the edge-restricted recurrence

Status: CONFIRMED finite exact computation in V183. Both variants reach order 18. It is not a convergence theorem.

## Definition and conventions

Fix delta=2/3, c=3, p_n=1-2n/3 and P_n=p_n+1. Let rho_n=r^(p_n)F_n(t,theta), psi_n=r^(P_n)G_n(t,theta), t=log r. Start with F_1=sin theta. For an integer K>=1, admit exactly the ordered pairs

    E_(n,K)={(i,n-i):1<=i<n and min(i,n-i)<=K}.

Each ordered pair appears once, including the central pair when n is even. Put u_i=(-partial_y psi_i,partial_x psi_i) and define

    S_n=sum_((i,j) in E_(n,K)) u_i dot grad rho_j,
    (2(n-1)-3 partial_t)F_n=the angular-log coefficient of S_n,
    -Delta psi_n=partial_x rho_n.

The polynomial density inverse is unique because 2(n-1)>0. The polynomial Poisson inverse is chosen with zero constant coefficient in every resonant stream channel. These choices determine each finite order. They define a modified recurrence: its sum does not generally solve the original stationary equation.

## Exact checks and dependency argument

The independent implementation uses Cartesian derivatives of exact rational complex Fourier polynomials. At each order it reconstructs a common potential chi_n with rho_n=-partial_y Delta chi_n and psi_n=partial_x partial_y chi_n. It checks these identities, the Poisson equation, and the modified stationary coefficient equation

    (3p_n-1)F_n+3 partial_t F_n+S_n=0.

For n<=2K+1 every pair with i+j=n satisfies min(i,j)<=K: otherwise n>=2K+2. Induction therefore proves that the K-edge recurrence agrees with the full recurrence through order2K+1. This provides an exact prefix comparison for K=1 and K=3. For n>2K every admitted pair has exactly one index at most K, so the recurrence is linear in the later coefficients, with the finite first K coefficients held fixed. This observation does not bound products of its order-dependent linear operators.

Every exported coefficient is an exact rational number. Plain norms sum absolute real sine amplitudes over all log degrees. The log degrees, maximum angular frequencies and norms are finite diagnostics only. A fit or a finite comparison of these data does not decide geometric growth, the infinite series, or the nonlinear full recurrence.

## Dependencies and evidence

The Cartesian derivative engine and independent polynomial inverse are in code/cartesian_verify.py and code/logarithmic_verify.py, with their earlier verification in topics01 and10. The present wrapper selects ordered pairs by a set condition and uses the same exact reconstruction checks. Frozen source copies and the computed finite tables belong in sources/ and verification/.

## Completed finite checks

The Cartesian implementation computed each K=1 and K=3 variant through order 18, including exact common-potential reconstruction at every order. The full recurrence was computed through order 7 for prefix comparisons. A separate sine product-to-sum audit checked all 43 stored orders, 1564 coefficient identities, 141 ordered pair products and 11 zero resonant constants. Every check passed. The K=1 variant agrees with the full recurrence through order 3 and K=3 through order 7, as the pair-set argument predicts. Both variants have density degree 4 and stream degree 5 at order 18. Exact data and both implementations are retained.

The first launch stopped before computing coefficients because the rational helper accepts one argument; the corrected expression divides Q(2*n) by 3. That startup error is retained separately and contributes no verification evidence.

## Floating comparison at 2026-10-31T07:50:53Z

V186 compares the frozen edge-1 checkpoint through order 250 with all 830 exact coefficient positions through order 18. There are no exact-zero mismatches; the maximum discrepancy relative to the exact order norm is 3.77e-16. The finite slopes and profile numbers in the peer's 07:48 note reproduce to their quoted rounding. These are not enclosures. The checkpoint contains 78523 nonzero subnormal values, and its stored nonzero log degrees fall to 49 at 250. This requires a calculation with arbitrary exponents before interpreting the high-degree columns. No conclusion about asymptotic rates or the complete nonlinear problem follows. The exact reference remains valid independently of this floating calculation.


## Why a global factorial maximum needs more than a float dump

Consider two polynomials with a single sine angular mode,

    A(t,theta)=(10^(-237)+10^(-247)t)sin(theta),
    B(t,theta)=A(t,theta)+10^(-325)t^98 sin(theta).

They have identical correctly rounded binary64 coefficients, because 10^(-325)<2^(-1075). Their nonconstant factorial-column maximum divided by the constant-column norm is radically different: for A it is 10^(-10), while for B it is at least 98!*10^(-88)>10^65. Both inequalities are exact integer comparisons in verification/underflow_counterexample.json. These polynomials respect the order-300 density degree upper bound and sine symmetry, but are not asserted to be generated by the stationary recurrence.

This refutes an inference from the floating coefficient dump alone that an observed q=1 maximum is unchanged by missing columns. It does not refute the actual edge-1 maximum. That maximum needs an arbitrary-exponent recomputation or a bound on the missing weighted tail. Likewise finite fitted slopes remain empirical estimates without an enclosure of high-order errors. The relevant binary64 thresholds differ: about 2.2e-308 is the smallest normal value, while the smallest positive subnormal is 2^(-1074), about 4.94e-324. Nonzero subnormals in the frozen checkpoint show that its trimming is not simply a cutoff at 1e-308.

## Independent all-order forcing check for the K1 and K3 ball runs

For the two unit-sine variants at delta=2/3, every retained low factor throughK is independent of t. This permits a direct check of every nonlinear coefficient without reproducing the generating implementation. Write a stream monomial as B(t)sin(h theta), h positive and even, and a density monomial as A(t)sin(m theta), m positive and odd. In the ordered product with stream indexi and density indexj, put

    U=m(P_i B+B')A,   V=h B(p_j A+A').

The forcing contributes(U-V)/2 to sin((h+m)theta) and(U+V)/2 to sin((h-m)theta). Negative sine frequencies are converted using sin(-q theta)=-sin(q theta). These identities follow by applying sin(h)cos(m)=(sin(h+m)+sin(h-m))/2 and cos(h)sin(m)=(sin(h+m)-sin(h-m))/2. The prime in this paragraph is a t derivative.

Enumerate exactly the ordered pairsi+j=n with min(i,j)<=K. A central pair is counted once. For K1 orK3, one polynomial in each pair is constant in t, so the two product coefficients above require only a scalar multiplication and the coefficient rule[t^q]B'=(q+1)[t^(q+1)]B. Sum every contribution and compare, coefficient by coefficient, with

    2(n-1)F_n-3 partial_t F_n.

A stored coefficient interval is accepted at this stage only when the difference interval contains zero. This is a finite interval consistency check, conditional on the input enclosures, and is separate from the independent Poisson, initial-data and low-order exact checks. The source is `code/edge_nonlinear_audit.py`; any completed runs are recorded in the chronological verification ledger (not included). Preparing this method does not itself certify an unexecuted run.


## Completed K1 ball audit through300

V217 at2026-10-31T08:54:21Z closes the high-column uncertainty for the actual K1 run: every nonconstant factorial column is below the constant column at every computed order. The frozen1024-bit input,1152-bit calculations, all exact inclusions and Poisson residuals are retained in verification/arb_edge1_20261031T084803Z. The exact log degrees at300 are98 for density and99 for stream. This finite conclusion is distinct from the convergence theorem in topics106/107. The all-order nonlinear forcing audit has not yet finished.
