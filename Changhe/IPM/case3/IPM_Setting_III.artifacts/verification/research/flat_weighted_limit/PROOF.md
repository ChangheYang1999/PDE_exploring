# The limiting weighted constant for a flat center defect

Date: 2026-10-20. Status: independent analytic reconstruction and rational
certification; implementation checks are recorded separately. All profile
conclusions below are conditional on flatness, or additionally on a strain
cap. They do not exclude the full primary class.

## Statement

For an exact smooth primary profile, set ell>1, D=ell-1,
a=rho_y(0)!=0, h=rho-ay, sigma=sup|sym DU|_op and
M=sup_(X!=0)(-X.U/r^2). Define the compact self-adjoint operator L on
ell^2(Z) by zero diagonal and edge weights

    (Lf)_k=w_(k-1)f_(k-1)+w_k f_(k+1),
    w_k=1/(4|2k+1|).

Let lambda be its top spectral value. It is positive. The following strict
rational enclosure is certified for the entire infinite operator:

    363427798/10^9 < lambda < 363427799/10^9.              (1)

If h is flat at zero, then

    M >= ell-lambda|a|, hence sigma >= ell-lambda|a|.     (2)

In particular either cap M<=D or sigma<=D, together with flatness, forces

    |a| >= 1/lambda > 10^9/363427799
                         > 2.7515781752.                 (3)

Under the stronger cap sigma<=D, result63 makes the alternatives exhaustive:
either h is nonflat with first odd degree n and a>=(n-1)(2ell-1), or h
is flat and (3) holds. Thus no exact profile has sigma<=D and |a|<=2.
Negative a under that cap necessarily takes the flat alternative. No such
jet dichotomy is asserted under a cap on M alone.

## Weighted input and its whole-plane scope

For flat h the exact transport relation, sublinear growth and parities
imply that phi=psi+Dxy and v=U-(Dx,-Dy) are flat at the corresponding
Taylor orders. For every odd integer m>=3, the weighted cylinder inverse
is unique and all boundary terms vanish. Results59 and61 prove

    (m-1)ell-1 <= m M + |a| Qsign(m),                     (4)

where Qsign=Qminus for a>0 and Qplus for a<0. These are the upper spectral
values of half-line Jacobi matrices with diagonal respectively
+d_j and -d_j, d_1=1/4,d_j=1/2 for j>=2, and off-diagonal

    b_j(m)=(m^2+4j^2)/(4|4j^2-m^2|).

This input retains the affine-subtracted velocity v, not a velocity with
an arbitrarily chosen harmonic strain. For each fixed m the nonzero norm
of h has already been divided out. A bound uniform in m on that norm is
neither used nor needed.

## Norm convergence of the shifted Jacobi matrices

Write m=2J+1 and embed the half-line vertex j>=1 as k=j-J-1 in Z,
extending the matrix by zero on missing vertices. For an included edge,
q=2j, so q-m=2k+1. A direct identity gives

    b_j(m)/m - 1/(4|q-m|)
       = sign(q-m) q/(4m(q+m)).                          (5)

Its absolute value is at most1/(4m). Each omitted edge of L also has
size at most1/(4m), since |2k+1|>=m there. The diagonal discrepancy is
at most1/(2m). The sum of absolute discrepancies in every row is at most
1/m. The same holds in every column by symmetry. Cauchy-Schwarz, or
2|f_k f_l|<=|f_k|^2+|f_l|^2, therefore bounds the operator norm by1/m.

The top spectral value of the zero extension is Qsign(m)/m, rather than
zero: both Q's are positive. For the negative diagonal matrix, a vector
on the edge q=m+1 has Rayleigh quotient at least b_j(m)-1/2>0 for m>=3;
the positive diagonal case is immediate. The variational definition of
the top spectrum and the norm bound give

    |Qminus(m)/m-lambda|<=1/m,
    |Qplus(m)/m-lambda|<=1/m.                            (6)

The weights of L tend to zero at both ends, so deleting all but finitely
many edges approximates L in norm by finite rank matrices. This proves
compactness. Alternating signs of f_k change the sign of its quadratic
form, so its spectrum is symmetric; a two-vertex test gives a positive
top value. No assertion that an eigenvector of the profile exists is
involved. Divide (4) by m and use (6) through odd m to prove (2).

## An independent Schur certificate for the infinite operator

We give a direct certificate different from the positive-vector test in
the audited source. Reflection k->-k preserves L. Along either arm from
the central vertex0, the edge from distance r to r+1 is

    alpha_r=1/(4(2r+1)), r>=0.

Fix N=8. The tails beyond distance N begin at N+1. Their top spectra are
at most tau=2alpha_(N+1) by the row-sum bound and monotonicity of alpha_r.
Let Lambda=363427799/10^9; it exceeds tau. The resolvent of each tail at
Lambda is positive and bounded by1/(Lambda-tau). Eliminating it from
Lambda I-L therefore leaves a finite matrix bounded below by the one
whose two terminal diagonal entries are

    p_N=Lambda-alpha_N^2/(Lambda-tau).

Eliminate successively along both identical arms, with

    p_r=Lambda-alpha_r^2/p_(r+1), 1<=r<N,
    p_0=Lambda-2alpha_0^2/p_1.                            (7)

All nine pivots p_N,...,p_0 are strictly positive as exact rational numbers.
Their complete fractions are in verification/checks.json. Finite positive
pivots, a positive tail gap and completion of squares prove a uniform
positive lower bound for Lambda I-L. Thus lambda<Lambda. This is a bound
for the full infinite operator; it does not truncate the physical domain.

For the lower endpoint l=363427798/10^9, take only the central vertex and
its two arms through distance8, deleting the remaining edges. Define

    q_N=l, q_r=l-alpha_r^2/q_(r+1), 1<=r<N,
    q_0=l-2alpha_0^2/q_1.                                (8)

The eight arm pivots are positive and the central pivot is negative.
Completing squares gives a negative direction for l I-L in this finite
subspace. Equivalently its Rayleigh quotient for L exceeds l, proving
the lower bound in (1). The strict signs in both calculations are exact
integer-arithmetic comparisons, not floating-point eigenvalue estimates.

For scale, the central pivots in (7) and (8) are approximately
+1.9192267363e-9 and -1.9627858060e-10. These decimals merely describe the
certified fractions and are not used to decide their signs. Inverting
(1) gives

    10^9/363427799 < 1/lambda < 500000000/181713899,

or approximately2.751578175229 <1/lambda<2.751578182801.

## The capped alternatives and scope

Under sigma<=D, result63 proves the first nonzero Taylor term needs
positive a>=(n-1)A>=2A>2. If there is no such term, flatness and (2)
give (3). Thus even equality |a|=2 is excluded for that subclass.
A convenient positive-a necessary bound is

    a >= min(2A,1/lambda),

while negative a gives flatness and |a|>=1/lambda. The rational number
10^9/363427799 may replace1/lambda for a weaker explicit bound. Flatness
has not been proved for general negative-slope profiles without the cap.

Under the weaker cap M<=D, only the flat conditional part of this proof
survives. The radial cap does not give nonnegativity of the full leading
strain polynomial. Both M and sigma, the slope a, ell and flatness are
invariant under rho_lambda(X)=lambda rho(X/lambda). Consequently every
claim above is independent of the remaining spatial normalization.

Dependencies: results59 and61 for the full weighted identity and inverse,
and result63 for the capped Taylor dichotomy. The limiting matrix,
norm convergence and certificate have been established explicitly here.
Numerical eigenvalues are optional supporting checks only. These are
conditional necessary conditions, not a proof that a capped profile
exists or an unconditional bound on its strain.

Verification update 2026-10-20T20:15:16.231038+00:00: independent implementation checks passed2026-10-20T20:13:40Z. Exact counts and rational evidence are in verification/checks.json. Verdict CONFIRMED with the conditional scope above.
