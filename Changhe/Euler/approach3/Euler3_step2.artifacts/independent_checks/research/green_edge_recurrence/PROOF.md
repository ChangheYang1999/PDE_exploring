# Scaled Green coefficients at quadrature-panel edges

Status: exact finite-sum identities. Floating-point error and quadrature error
are separate and are not bounded by these identities.

## Statement and hypotheses

Fix an integer ell>=0, complex source samples f_j at positive radii s_j,
real quadrature weights w_j, and ordered target radii 0<r_1<...<r_k<T.
Assume no s_j equals a target radius. Write q_j=w_j f_j. The finite samples
may include the remainder after subtracting a specified tail on s>T. Let
E_ell(r) be the exact exterior Green contribution of that subtracted tail.
Define the scaled inner and outer integrals

    I_ell(r) = sum_(s_j<r) q_j r (s_j/r)^(ell+2),
    O_ell(r) = sum_(s_j>=r) q_j s_j (r/s_j)^ell + E_ell(r).

Assume E_ell(a)=(a/b)^ell E_ell(b) whenever 0<a<b<T. Then

    I_ell(b) = (a/b)^(ell+1) I_ell(a)
              + sum_(a<=s_j<b) q_j b (s_j/b)^(ell+2),
    O_ell(a) = (a/b)^ell O_ell(b)
              + sum_(a<=s_j<b) q_j s_j (a/s_j)^ell.

The potential and radial derivative coefficients associated with these sums
are P_ell=(I_ell+O_ell)/(2ell+1) and
D_ell=(-(ell+1)I_ell+ell O_ell)/(r(2ell+1)).

For a rotating power/log tail with source coefficient

    f_ell,m(s) = (A+B log s) s^(-2alpha-2+i m kappa), s>=T,

where alpha>0 and |m|<=ell, put e=-ell-2alpha+i m kappa. Then

    E_ell,m(r) = (r/T)^ell T^(-2alpha+i m kappa)
                 [A+B(log T-1/e)]/(-e).

All powers use positive real radii and the real logarithm. Since Re(e)<0,
the tail integral converges absolutely. The formula avoids forming a large
factor r^ell and a tiny factor T^(-ell) separately.

## Proof

Split I_ell(b) at a. For every s_j<a,

    b(s_j/b)^(ell+2)
      = (a/b)^(ell+1) a(s_j/a)^(ell+2).

Summing proves the inner recurrence. Split O_ell(a) at b. For s_j>=b,
s_j(a/s_j)^ell=(a/b)^ell s_j(b/s_j)^ell. The stated homogeneity of E_ell
allows its contribution to be combined with this sum and proves the outer
recurrence. These arguments are algebraic and do not assume positivity of
the complex source samples.

For the tail, the unscaled exterior integral is
int_T^infinity (A+B log s)s^(e-1) ds. Direct integration gives
T^e[A+B(log T-1/e)]/(-e); the boundary term at infinity vanishes because
Re(e)<0. Multiplication by r^ell and collection of the powers of T gives the
displayed formula, including its required homogeneity in r. The potential
and derivative coefficients are exactly the scaled forms of the Green
formula proved in `../pressure_consistency/PROOF.md`.

## Scope and dependencies

Targets must be quadrature-panel edges when these sums are used as a
quadrature for a physical source. Otherwise classifying whole quadrature
nodes by the target radius omits the necessary partial-panel integration.
The recursion changes only finite-sum evaluation order. Agreement with the
old direct sums is a regression test, not an independent pressure reference.
No zero source moment is imposed. The angular synthesis and the source
sampling must be checked independently.
