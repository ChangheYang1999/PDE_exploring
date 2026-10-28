# Separate left and right exponent comparisons

## Statement, hypotheses and constants

Use the real homogeneous Holder operator norms C_alpha and D_alpha,
with their kernels, circular principal values and quotient extension
as in ../../../../01_setup/PROOF.md. Fix a center alpha0 in (0,1), an
auxiliary interval [a,b] containing it, and cutoffs epsilon,R as in
../../PROOF.md. Let E be a common upper bound for the two truncation
errors on [a,b]. Let m_C and m_D be positive upper bounds for the
Jordan masses of the truncated phase measures, and d>=1 a common
upper bound for their support diameters. Suppose

    C_alpha0<=U, D_alpha0>=V, V>E, U+E>0.

Write

    u=U+E, v=V-E,
    ell=log(d),
    h_C=max(0, log(m_C/u)/alpha0),
    h_D=max(0, log(m_D/v)/alpha0),
    G_minus(rho)=v exp(-ell rho)-u exp(h_C rho)-2E,
    G_plus(rho)=v exp(-h_D rho)-u exp(ell rho)-2E.

If rho>=0 and [alpha0-rho,alpha0+rho] is contained in [a,b], then

    D_alpha-C_alpha >= min(G_minus(rho),G_plus(rho))           (1)

throughout that closed interval. A positive right side therefore
proves C_alpha<D_alpha on the entire interval.

This is a corollary of the accepted finite-mass comparison in ../PROOF.md.
It uses the same cutoffs and endpoint certificates. It makes no claim
that these sufficient intervals are maximal.

## Complete argument

For alpha=alpha0+s with s>=0, the one-sided inequalities in ../PROOF.md
and the two truncation errors give

    C_alpha <= E+u d^s,
    D_alpha >= -E+v(v/m_D)^(s/alpha0)
             >= -E+v exp(-h_D s).

For alpha=alpha0-s they give

    C_alpha <= E+u(m_C/u)^(s/alpha0)
             <= E+u exp(h_C s),
    D_alpha >= -E+v d^(-s).

The uses of max(0,...) only weaken these valid inequalities. Since
ell,h_C,h_D are nonnegative, both G_minus and G_plus are nonincreasing
on [0,infinity). Thus s<=rho gives the appropriate one-sided gap at
least its endpoint value. Taking the minimum proves (1). All endpoints
are included. The phase suprema and finite-measure limiting arguments
are already justified in the parent proof; no optimizing phase or
common optimizing coupling is assumed here.

Unlike the common maximum-log estimate, (1) does not combine an adverse
C bound from one side of the center with an adverse D bound from the
other side. That is the sole change. It does not alter an endpoint
value of either operator norm or use a new numerical integration.

## Verification

The input errors, masses, cutoffs and endpoint values are exact rational
upper or lower bounds from the parent certificates. The producer
computes the two exponential expressions with320-bit balls. A separate
640-bit program uses the four power expressions and subtracts the
matching upper and lower bounds on each side. Exact rational interval
containment and downward rounding are checked before acceptance.
