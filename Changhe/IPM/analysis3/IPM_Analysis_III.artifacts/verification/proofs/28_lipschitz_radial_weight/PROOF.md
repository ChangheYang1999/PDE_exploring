# Radial Fredholm theorem with a Lipschitz logarithmic weight

Status: proved under the stated global margin. This extends proof 21 and
checks the theory author's piecewise affine weight proposed on2026-10-28 at02:18Z.
It does not certify the margin numerically.

## Exact statement

Let ell>0. Let V be a globally Lipschitz C1 vector field on R2, V(0)=0,
div V=2ell, with V1 odd in x and even in y and V2 even in x and odd in y.
Let a,c be bounded continuous real functions tending to zero both at the
origin and at infinity. Let a be odd in both coordinates and c even in
both. Let mu:R->R be globally Lipschitz, with Lipschitz constant M<2.
Set w(X)=exp(mu(log|X|)) for X!=0. Values at the single point0 are irrelevant.
Let X_w be the complex parity subspace of L2(w dX), even in x and odd in y.
Define Sij by Fourier multiplier xi_i xi_j/|xi| squared, initially on
Schwartz functions and then by its bounded weighted extension. Put

 T=a S12-c S11,  Lfix=V.grad-1+T,
 D_w={h in X_w: V.grad h in X_w in distributions on R2}.

Equivalently one may require the distributional identity on the punctured
plane. Give D_w its transport graph norm. Define, almost everywhere,

 q(X)=V(X).X/|X| squared,
 b_+(X)=(sqrt(a(X) squared+c(X) squared)-c(X))/2,
 kappa(X)=1+ell+mu'(log|X|)q(X)/2.

Suppose

 m=essinf_{X!=0}(kappa(X)-b_+(X))>0.

Then Lfix:D_w->X_w is closed and Fredholm of index0. There is a compact
K:X_w->X_w such that

 m ||h||_w <= ||Lfix h||_w+||K h||_w   (h in D_w).

In particular Lfix is bijective if and only if it is injective. No explicit
bound on K or the inverse is asserted. The theorem applies to real functions
by restriction.

## Proof, including each change from the smooth-weight argument

The logarithmic Lipschitz bound gives, for r,s>0,

 max(w(r)/w(s),w(s)/w(r)) <= max((r/s)^M,(s/r)^M).

Conjugate by J:h->sqrt(w)h. Off the diagonal the additional kernel in
J Sij J^{-1}-Sij is Kij(X-Y)(sqrt(w(X)/w(Y))-1), where |Kij(Z)|<=C|Z|^-2.
The identity part of Sij cancels. Schur's test with auxiliary function1/r
uses the two convergent integrals

 r^(M/2-1) integral_0^(r/2) s^(-M/2) ds,
 r^(1-M/2) integral_(2r)^infinity s^(M/2-2) ds.

Both are uniformly bounded because M<2. On comparable radii and near the
diagonal, |log r-log s|<=C|X-Y|/r and the Lipschitz inequality for mu gives
|sqrt(w(X)/w(Y))-1|<=C_M|X-Y|/r. Thus the remaining kernel is bounded by
C_M/(r|X-Y|), integrable uniformly by Schur's test. The comparable-radius
portion away from the diagonal has area O(r squared) and kernel O(r^-2).
The transposed estimates are identical after interchanging r,s. Therefore
all Sij are bounded on X_w.

For a continuous multiplier d vanishing at0 and infinity, the operator
d(J Sij J^{-1}-Sij) is compact. Truncate d to an annulus; the norm of the
error tends to zero by the bound above. With X in that annulus, Y near0
gives a square-integrable kernel majorized in square by C(1+|Y|^-M),
and Y near infinity gives C(|Y|^-4+|Y|^(M-4)). On two bounded annuli,
mu(log r) is Lipschitz. The near-diagonal kernel is O(|X-Y|^-1), its
Schur norm after truncation at distance eta is O(eta), and the rest is
Hilbert-Schmidt. Norm limits prove compactness. Smoothness of mu was
unnecessary at every step.

The compact principal-symbol inequality is independent of mu after
conjugation. For completeness let Rj be the self-adjoint Fourier multiplier
xi_j/|xi|, so R1 squared+R2 squared=I. For every continuous d vanishing
at infinity, [d,Rj] is compact: approximate d uniformly by compact smooth
functions, truncate their commutator kernels away from the diagonal and
infinity, and use the O(|X-Y|^-1) near-diagonal bound and square integrable
tails. The symmetric matrix [[-c,a/2],[a/2,0]] has largest eigenvalue b_+.
Moving the coefficients past Rj, applying this pointwise matrix inequality,
and moving b_+ back gives

 Re<Tg,g> <= integral b_+|g| squared dX+Re<K0g,g>,

where K0 is compact. Conjugation gives the same inequality in X_w with a
compact error. Projection to the parity subspace preserves it.

The weight is locally W^{1,infinity} on every compact annulus and its weak
derivative satisfies V.grad log w=mu'(log r)q almost everywhere. This
multiplier is bounded since |q|<=Lip(V). The weight and its reciprocal are
bounded on each such annulus. For h in the maximal transport domain,
cutoffs near0 and infinity approximate h and V.grad h: their transport
derivatives are bounded uniformly, supported in escaping annuli, and
multiply the integrable function |h| squared w. On a fixed annulus ordinary
mollifiers approximate in the graph norm. The commutator of a C1 Lipschitz
V with a mollifier is uniformly bounded on L2 and tends to zero, by the
kernel formula

 grad eta_e(X-Y).(V(X)-V(Y))+eta_e(X-Y)div V(Y).

The first-order Taylor term cancels under integration; convergence for
smooth input and density give the result. Thus compact smooth parity
functions away from0 are a core. The maximal domain is closed.

Since M<2, w^{-1} is locally integrable also at0. Weighted L2 convergence
therefore implies local L1 convergence. The core approximants and their
transport derivatives converge in distributions on the whole plane. This
proves equivalence of the punctured and full-plane realizations. In
particular no point-supported term at0 is introduced by closure.

Integration by parts with the weak derivative of w is valid on the core.
There is no surface measure at a corner of mu: mu and w are continuous,
and their first weak derivatives are locally bounded functions. It gives

 (V.grad)^*=-V.grad-2ell-mu'(log r)q

with maximal domain D_w. The latter assertion follows first as a
distributional adjoint identity and then from boundedness of the added
multiplier and the same core argument. Bounded T changes neither domain.
Consequently

 Re<Lfix h,h>_w <=-m||h||_w squared+Re<K h,h>_w.

Core approximation extends this to D_w and proves the claimed estimate.
Compactness gives finite-dimensional kernel and closed range: if no lower
bound held on the kernel's orthogonal complement, a normalized sequence
with Lfix h_n->0 would have a Cauchy subsequence by the compact estimate,
converging to a kernel element in that complement. The same real-part
estimate for the adjoint gives finite-dimensional cokernel.

Finally L_s=V.grad-1+sT,0<=s<=1, has fixed domain and margin at least m
since b_+>=0. It is a norm-continuous Fredholm path from a bijective
transport operator L_0: the transport and its adjoint are bounded below
by m and their kernels are zero. Local finite-dimensional kernel/cokernel
splittings prove constancy of the index along the path. Hence the index
of Lfix is0. This completes the proof.

## The proposed piecewise affine weight

Let mu(0)=0, with knots3/2,7/4,3,4,5,6,7,8,9,10 and consecutive slopes

 (4,17,28,27,25,18,4,-10,-17,-19,-20)/16.

It is globally Lipschitz with M=7/4<2, equals t/4 for t<=3/2, and equals
-5t/4 plus a constant for t>=10. Thus the theorem applies directly if a
global almost-everywhere positive margin is certified. A box crossing a
knot must enclose every slope attained inside the box. Including both
adjacent slopes at endpoints is harmless and sufficient. No mollification
or loss in m is required.

A nonzero separated power r^p A(theta), A in angular L2, lies in L2(w)
near0 if and only if 2p+1+1/4>-1, and near infinity if and only if
2p+1-5/4<-1. For0<k<5/16 the residual order r^(2k-1) is integrable at
infinity, since4k-5/4<0. For k>0 the homogeneous tail r^k is not, since
2k+2-5/4>0. These statements require the angular coefficient to be
nonzero when asserting nonmembership. They are membership statements,
not residual size estimates.

## Optional mollification and its precise limitations

For an even smooth probability kernel eta_e supported in[-e,e], mu_e=
mu*eta_e satisfies Lip(mu_e)<=7/4 and |mu_e-mu|<=7e/4. Consequently, with
A=exp(7e/8),

 A^-1||h||_w <= ||h||_{w_e} <= A||h||_w.

If every weight knot is a boundary of a radial certificate box and e is
less than the shortest positive radial box width, each point's e-neighborhood
contains only slopes in the closed slope hull of its own box. The certified
pointwise box inequality then transfers to mu_e with the same m. Without
that partition alignment, the claimed hull implication need not hold: a
knot just inside a neighboring box may lie within e of a point whose own
box does not meet the knot. One may instead enlarge each box's slope hull
by its e-neighborhood. The direct Lipschitz theorem avoids this issue.

Under a valid smoothing transfer the domain is unchanged, as equivalent
weighted norms give the same maximal graph space. Compactness, closedness
and index survive equivalence. The quantitative estimate obtained solely
by changing both norms is

 m||h||_w <= A squared (||Lfix h||_w+||K h||_w).

Thus its possible loss is exp(7e/4), not just exp(7e/8). The direct theorem
has no such loss. No numerical inverse bound follows from either route
until the compact remainder and injectivity are controlled.

## Dependencies and scope

Proof 21 supplies the original smooth formulation; all weight-sensitive
arguments and the functional-analytic conclusion are reproduced here.
The theorem says nothing about continuity or closedness of the strain
c[h], the cubic normalization J, an added tail coordinate, or the nonlinear
map. Those are distinct domain questions.
