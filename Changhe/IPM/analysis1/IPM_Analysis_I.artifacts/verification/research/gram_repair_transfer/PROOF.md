# A conditional Gram transfer bound for the repaired columns

## Statement fixed before arithmetic

Let Omega_1,...,Omega_s be a finite common subdivision into compact
annuli of the supports of the selected topic132 functions. Let H_b be the
Hilbert direct sum of the weighted H1 spaces on these annuli, with inner
product obtained by polarizing

    integral (h^2+r^2|grad h|^2) w(r) dX,
    w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2),
    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2).

Derivatives in H_b are taken inside each open annulus. All these weights
are positive and bounded, with bounded inverses, on the compact supports.
Let X be the full-plane space with this norm using the weak gradient.
A continuous compactly supported piecewise polynomial belongs to X and
its X norm equals its H_b norm. A jumping original column can belong to
H_b while failing to belong to X.

Let h_j be N nonzero original columns in H_b, and let hhat_j be their
exact continuous repairs in X. Suppose

    ||hhat_j-h_j||_b < delta ||h_j||_b,  j=1,...,N, delta>0.

Set n_j=||h_j||_b, e_j=h_j/n_j, ehat_j=hhat_j/n_j. The repaired columns
are normalized by the ORIGINAL norms. Define synthesis maps
S c=sum c_j e_j and Shat c=sum c_j ehat_j, and real symmetric Gram
matrices G=S* S and Ghat=Shat* Shat. G is the exact broken Gram and
Ghat is the exact X Gram of these repaired, originally normalized columns.
Let eta=sqrt(N) delta. Then

    ||Shat-S||_(ell2 -> H_b) < eta,
    |Ghat_ij-G_ij| < 2 delta+delta^2,
    ||Ghat-G||_2 < N(2 delta+delta^2).

If the exact matrix G satisfies G >= gamma I for a KNOWN gamma>0 and
eta<sqrt(gamma), set epsilon=eta/sqrt(gamma)<1. Then in quadratic-form
order

    (1-epsilon)^2 G <= Ghat <= (1+epsilon)^2 G.

For an exact whitening matrix Q with Q^T G Q=I this implies

    (1-epsilon)^2 I <= Q^T Ghat Q <= (1+epsilon)^2 I.

No gamma or whitening matrix is certified by this theorem. The general
bound ||(Shat-S)Q|| <= ||Shat-S|| ||Q|| applies to every coefficient map,
but does not eliminate its conditioning. No row/operator matrix is
transferred by a Gram comparison alone.

## Proof

Put f_j=ehat_j-e_j and E=Shat-S. For every coefficient vector c,

    ||Ec||_b <= sum_j |c_j| ||f_j||_b
             <= ||c||_2 (sum_j ||f_j||_b^2)^(1/2)
             < eta ||c||_2,

where the finite sum of strict column bounds supplies a uniform operator
bound strictly less than eta. Since ||e_j||_b=1, expanding each Gram
entry gives

    Ghat_ij-G_ij = <f_i,e_j>+<e_i,f_j>+<f_i,f_j>.

Cauchy-Schwarz proves the entrywise bound. The spectral norm of a real
symmetric matrix is at most its maximum absolute row sum, so the stated
N(2delta+delta^2) bound follows. Equivalently, ||S||<=sqrt(N), and
Ghat-G=S*E+E*S+E*E yields the same upper bound. These are independent
ways to obtain the finite matrix estimate.

Under the gamma hypothesis, ||Sc||>=sqrt(gamma)||c||, hence
||Ec||<=epsilon||Sc||. The triangle and reverse triangle inequalities
give (1-epsilon)||Sc||<=||Shat c||<=(1+epsilon)||Sc||. All factors are
nonnegative, so squaring gives both quadratic-form inequalities. Substituting
c=Qz proves the conditional whitening statement. Products of bounded
synthesis and coefficient maps give the final general estimate.

## Application, dependencies and verification plan

Use precisely topic132's 90 radial columns times16 angular modes and
187 radial columns times24 angular modes. Thus N=1440 and4488, with
exact strict relative ceilings delta=8447/10^18 and
6419/250000000000000000 respectively. Topic132 supplies the repairs and
column bounds. Their common partition is finite, so the construction of
H_b above is valid. Full-plane angular integration is understood.

Recheck every topic132 final pin. Compute outward rational ceilings for
eta and N(2delta+delta^2) using Arb512, and independently using rational
squares and integer square roots. Check that the public intervals really
contain the exact quantities and are strictly outward. The proof precedes
this arithmetic. No actual Gram entries, eigenvalue lower bound gamma,
quadrature error, source execution history or floating whitening matrix
is verified here.

The estimate explains one sufficient way to transfer an exact broken
Gram to the repaired X space once its conditioning is bounded. It does
not allow a bounded operator on X to act on discontinuous original
functions, and no X norm is assigned to their differences. Velocities,
operator rows, normalization, inverse and the PDE remain OPEN.
