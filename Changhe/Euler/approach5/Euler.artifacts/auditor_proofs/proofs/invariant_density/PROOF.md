# Invariant-set density at infinity

## Statement and scope

Let c>0, omega be real, J(x,y,z)=(-y,x,0), and U in C1(R3;R3) be bounded and divergence-free. Put B=(cI-omega J)y+U and let Phi be its flow. If a Lebesgue measurable V satisfies Phi_t(V)=V for every real t, then either |V|=0 or, for every C>1, there are delta>0 and rho0 such that

    |V intersect {rho<|y|<C rho}| >= delta rho^3  (rho>=rho0).

No profile equation is used in this statement. For a C2 Euler profile with bounded U, the additional condition

    liminf rho^-3 |E intersect {rho<|y|<C rho}|=0

for one C>1 implies U is constant if E={Omega!=0}, or if E={B cross Omega!=0} and c!=1/2. Under decay that constant is zero.

## Proof

Write M=sup|U| and take R0>2M/c. Linear growth gives a complete C1 flow. Its Jacobian is exp(3ct), since div B=3c. For an orbit starting at radius at least r>=R0, radial differentiation gives

    r'(t)=c r(t)+U(Phi_t x) dot Phi_t x/r(t),
    r(t)>=r(0)exp(ct/2),
    |log(r(t)/r(0))-ct|<=kappa(r):=2M/(cr).

The bound holds for all t>=0, because the radial derivative stays positive outside R0. Thus the image of the shell (r,(1+epsilon)r) is contained in the shell

    (r exp(ct-kappa(r)), (1+epsilon)r exp(ct+kappa(r))).

The forward-bounded set is contained in the intersection of Phi_-t(closed ball R0), whose volume is at most exp(-3ct)|ball R0| for every t. It is null. Every other point eventually lies outside any prescribed R1>=R0 and stays there. Using integer times and invariance of V, positive volume of V therefore implies positive volume of V outside R1. A countable shell cover then supplies an r>=R1 with

    m=|V intersect {r<|y|<(1+epsilon)r}|>0.

Given C>1, choose epsilon>0 and R1 sufficiently large that (1+epsilon)exp(2kappa(R1))<=C. For rho>=r exp(-kappa(r)), choose

    t=(log(rho/r)+kappa(r))/c>=0.

The preceding shell image is contained in (rho,C rho), and invariance and the exact Jacobian give

    |V intersect {rho<|y|<C rho}| >= (rho/r)^3 exp(3kappa(r))m.

Taking delta=m/r^3 proves the theorem. The argument also covers M=0 by any R0>0.

For the Euler consequences, both indicated E are open and invariant. The vorticity Cauchy law proves this for Omega. The covector alpha=(B cross Omega)^flat satisfies Phi_t^*alpha=exp((2c-1)t)alpha and proves it for the cross product. The density hypothesis makes E null, hence empty. If Omega=0, each bounded component of U is harmonic and is constant. If the cross product vanishes, the exact profile identity

    (1-2c)U + Omega cross B + grad Htilde=0

makes U a gradient when c!=1/2, reducing to the preceding case. This last step uses the Euler equation and the coupling Omega=curl U.

## Audit of the examples and interpretations in CO7

Sublinear-width slabs, tubes around finitely many lines, and cones of shrinking aperture have zero normalized annular volume. For a width h(r)=o(r), use sup_{s>=rho}|h(s)|/s ->0 to make the estimate uniform over a fixed-ratio annulus.

The more general assertion that small angular area on a positive-logarithmic-density set of radii implies zero annular density is false for arbitrary measurable sets. For example, take E={y: the fractional part of |y| is in (0,1/2)}. Angular area is zero on asymptotically half the radii in every dyadic range, but for every fixed C>1,

    rho^-3 |E intersect {rho<|y|<C rho}| -> (2pi/3)(C^3-1)>0.

This example is not asserted invariant. The quoted generic measure-theoretic justification must be removed or replaced by a separate invariance argument.

The cross-product corollary says: if Omega is parallel to B outside a set of zero annular density, then U is constant. Wording that says nonzero profiles cannot be parallel except on a zero-density set reverses the exceptional set.

For an independent bracket eigenfield W, the first corollary proves W=0 under its density hypothesis, not U constant. Indeed any compactly supported nonconstant divergence-free U together with W=0 obeys the bracket equation. The Euler-specific conclusion uses W=curl U.

No assertion about a vortical set at the physical singular time follows without establishing that terminal field and its trace. The theorem is an exact statement about profile-space invariant sets.

## Dependencies and verdict

The proof uses the elementary complete-flow and covector identities audited in A002, A006 and A056, the divergence theorem for harmonicity, and bounded harmonic Liouville. The mathematical proposition and its precisely stated Euler corollaries are CONFIRMED. The broad angular-area example is REFUTED as a general set assertion; the physical-time interpretation is not certified.
