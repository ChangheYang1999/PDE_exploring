# Far-field obstruction to an exactly compact correction

## Statement

Let c>1, gamma=1/c, and let R be a smooth S1 density on R^2 with
smooth canonical velocity U_R. Here S1 means even in x and odd in y.
Assume |grad R(X)|<=G |X|^(gamma-1) for |X|>=R0. Set
F=(cX+U_R).grad R-R. Suppose h is S1, belongs to L2(R^2), and vanishes
outside the disk of radius A>0. Assume R+h solves the stationary
equation at the same c in distributions, with canonical velocity
U[R+h]=U_R+U[h]. Then for r=|X|>=max(2A,R0),

    |F(X)| <= (8G/pi) r^(gamma-4) integral |Y| |h(Y)|dY
            <= 4 sqrt(2/pi) G A^2 ||h||2 r^(gamma-4).  (1)

Consequently, if the exact finite-branch convergent expansion of F
contains any nonzero angular coefficient at exponent e>gamma-4,
there is no such compactly supported correction. Neither this
statement nor the coefficient test below excludes a correction whose
mass is mostly in an annulus but whose tail is nonzero.

## Kernel and exterior estimate

With the Fourier symbol

    Uhat[h]=(xi1 xi2/|xi|^2,-xi1^2/|xi|^2) hhat,

the kernel away from the origin is

    K(X)=(-xy/(pi r^4),(x^2-y^2)/(2pi r^4)).            (2)

Indeed apply -partial_xy and partial_xx to the fundamental solution
-(log r)/(2pi) of -Delta. The second component also has the local
term -h/2. That local term is retained in the global operator and
vanishes outside the support of h. No strain/contact formula is
altered by this exterior argument.

For X outside the support, U[h](X)=integral K(X-Y)h(Y)dY. This follows
first for smooth compact functions and then by L2 approximation; on
an exterior compact set the integral kernel is smooth and bounded.
The odd y symmetry and compact support imply integral h=0. In polar
coordinates

    K=r^-2(-sin(2theta),cos(2theta))/(2pi).

Its radial derivative and its normalized angular derivative are
orthogonal vectors of common length1/(pi r^3). Thus the operator
norm of DK is exactly1/(pi r^3). For r>=2A, the line segment X-tY
has length at least r-A>=r/2, so the mean-value formula gives

    |K(X-Y)-K(X)| <= 8 |Y|/(pi r^3).

Subtract K(X)integral h=0 and integrate to obtain the first factor
in(1). Cauchy-Schwarz on the disk gives

    integral |Y||h(Y)|dY <= sqrt(pi/2) A^2 ||h||2.

On |X|>A the correction is identically zero, and the distributional
stationary equation reduces to the smooth identity
F+U[h].grad R=0. Combining these estimates proves(1).

## Why an expansion coefficient contradicts (1)

For the finite ordinary generator class used here, every branch has
an analytic expansion in z=r^-2 for r>1, with smooth finite Fourier
angular coefficients. The residual exponents are

    e_(ell,q)=1-ell delta-2q,
    delta=1-gamma, 1<=ell<=16, q>=0.

There are finitely many exponents above any fixed threshold. Group
coincident exponents. If one coefficient above gamma-4 is nonzero,
choose the largest such exponent with a nonzero coefficient and an
angle where that coefficient is nonzero. The expansion gives a
nonzero limit after division by r to that exponent, contradicting
(1). The remainder is smaller because the finite analytic branch
series converge for r>1. This step does not use a finite asymptotic
model as a bound for the actual residual at a specified radius.

## A short exact test on the published candidates

The canonical polar fields have the form

    R=r sum_(j,n) v^a_j R_jn(t) sin(n theta),
    psi=r^2 sum_(j,m) v^a_j S_jm(t) sin(m theta),
    t=r^2/(1+r^2), v=1-t, a_j=(j+1)delta/2.

The first descendant density coefficient for branch ell=j+1 is

    D_(ell,n)=-a_j R_jn(1)-R'_jn(1),                    (3)

and the corresponding stream coefficient is
Sdesc_(ell,m)=-a_j S_jm(1)-S'_jm(1). This follows by taking the first
coefficient of(1+z)^(-a_j)R_jn((1+z)^-1), and similarly for S.
Let ell_* be the first branch with a nonzero density coefficient(3).
If all lower density and stream descendants vanish, the residual
coefficient at e=1-ell_*delta-2 is exactly

    (ce-1) D_(ell_*,n).                                (4)

Every quadratic contribution at that exponent would use a first
descendant from a strictly lower branch, so it is zero. The checker
also verifies that exponents from different ell in1,...,16 cannot
coincide after an integer change of q, using exact rational delta.
Therefore(4) is the actual residual coefficient. A nonzero value and
e>gamma-4 complete the compact-correction obstruction.

The checker uses exact canonical007,013and014inputs already bound to
their immutable raw snapshots. It independently computes(3), checks
all lower descendant cancellations, and stores the nonzero rational
angular coefficients in JSON. Their numerical magnitudes are not
needed. Candidate assertions are accepted only if those checks pass;
the general theorem above is independent of their outcome.

## Dependencies, independence and scope

The only imported algebra is the already audited exact polar field
constructor. The exterior proof is a separate kernel argument, not
an application of a weighted existence theorem. Common-leading-tail
pinning, if needed to make an all-c statement, remains a separate
hypothesis. This result explains a limitation of an exactly annular
correction ansatz; it gives no lower bound for the fraction of mass
outside an annulus and no global nonexistence result.
