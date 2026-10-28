# Exact frozen-corner singularity and the scope of its transfer

## Statement and maximal realization

Let ell>1, A=2ell-1, D=4ell-1=2A+1, a=17/4 and eta=5/4.
Set

    w(X)=|x|^(-2a) max(1,|X|)^(2a-eta),
    R=L2_P(w dX),
    T=-A x partial_x+D y partial_y-1,
    D_R={h in R: Th in R distributionally}.

The subscript P imposes evenness in x and oddness in y. The maximal
operator T:D_R->R is bijective, with inverse norm at most

    1/kappa_*, kappa_*=1+ell+eta A/2>0.                    (1)

Choose a real even chi in C_c^infinity(R), chi=1 on [-1,1], and a real
odd psi in C_c^infinity(R), supported where 1/2<=|y|<=2, nonnegative
and not identically zero for y>0. Put

    f(x,y)=x^4 chi(x) psi(y).

Then f is in R and is smooth and compactly supported. Its unique
solution is

    h(x,y)=-integral_0^infinity e^(-s)
                       f(x e^(-As),y e^(Ds)) ds.          (2)

Whenever 0<|y|<1/2 and |x|(2|y|)^(A/D)<=1, it is exactly

    h(x,y)=-C x^4 sgn(y)|y|^beta,
    beta=(1+4A)/D=2-1/D,
    C=(1/D) integral_(1/2)^2 u^(-beta-1)psi(u)du>0.         (3)

At every nonzero point of the x-axis the solution is locally in Hs
exactly for

    s<beta+1/2=5/2-1/D,                                  (4)

and is locally C^(1,beta-1) but not C^(1,alpha) for alpha>beta-1.
Its cofactor h/(x^2 y) is locally in Hsigma across that axis exactly
for sigma<beta-1/2=3/2-1/D. In particular the endpoint in both Sobolev
statements is excluded.

These are statements about T, the frozen transport operator. They do
not assert the same explicit singularity for the full variable-field
nonlocal linearized operator. That transfer remains open.

## The weighted inverse and domain

The complete flow of the vector field is

    Phi_s(x,y)=(e^(-As)x,e^(Ds)y).

Away from r=1 and the axes, its weighted divergence gives

    kappa_w=1+(D-A)/2+(V.grad log w)/2.

For r<1 this is 1+ell+aA. For r>1 it is

    1+ell+aA+(a-eta/2)(-A cos^2(theta)+D sin^2(theta)).

Since a>eta/2, its lower bound is exactly (1). The radial weight is
continuous at r=1, so its piecewise first derivative has no surface
measure. Changes of variables along the flow, or integration of its
logarithmic derivative, give

    ||S_s||_(R->R)<=exp(-kappa_* s),
    S_s f=e^(-s) f(Phi_s(X)), s>=0.                        (5)

The maps S_s form a strongly continuous semigroup. Strong continuity
follows first for compact smooth functions supported away from x=0,
then by their density in R and the uniform local bound. The generator
is the stated maximal T: cutoffs in log|x| and log|y| have uniformly
small V derivatives, radial cutoffs have uniformly bounded derivatives,
and ordinary mollification on compact sets away from the axes gives
a graph core. More explicitly, after taking logarithms separately in
each quadrant and multiplying by the square root of the transformed
weight, the transport becomes a constant directional derivative plus
a bounded piecewise coefficient. Its maximal distributional domain is
the generator domain. Logarithmic cutoffs remove the axes without
leaving a distribution there. This also proves closedness.

The Bochner integral -integral_0^infinity S_s f ds is in the generator
domain: S_t h-h=integral_0^t S_s f ds and division by t converges to f.
It obeys (1). A vector in the kernel is fixed by S_s and therefore
vanishes by (5). This proves bijectivity and (2).

The forcing belongs to R because near the only singular weight locus,
x=0 with y bounded away from0, its squared weighted integrand is a
bounded multiple of |x|^(8-2a)=|x|^(-1/2). This is integrable. The exact
criterion for a smooth x^m leading term at such a point is a<m+1/2.
For m=4 this is a<9/2, not a<19/4.

## Exact characteristic computation

For y>0, the support of psi restricts the integral to values
u=y exp(Ds) in [1/2,2]. Under the displayed condition in the statement,

    |x exp(-As)|=|x|(y/u)^(A/D)<=|x|(2y)^(A/D)<=1.

Thus chi=1 throughout the integral. Moreover

    e^(-s)(x e^(-As))^4=x^4 (y/u)^((1+4A)/D),
    ds=du/(D u).

Substitution proves (3) for y>0; parity proves it for y<0. The integral
C is strictly positive by the assumed sign of psi. At each fixed x0,
a small enough rectangle about (x0,0) satisfies the condition for all
y in it. When x0 is nonzero its x^4 factor never vanishes on a smaller
rectangle.

## Exact local regularity, including the endpoints

Here D>3, hence 5/3<beta<2. For a smooth compact cutoff equal to1 at0,
the one-dimensional function chi_0(y)sgn(y)|y|^beta has distributional
second derivative equal near0 to

    beta(beta-1)sgn(y)|y|^(beta-2).

There are no delta terms since the function and its first derivative
are continuous at0. Put nu=beta-2 in (-1/3,0). The localized homogeneous
function sgn(y)|y|^nu belongs to Hsigma(R), for 0<=sigma<1, exactly when

    sigma<nu+1/2.

For completeness, its fractional seminorm on y>0 and y<z<2y is a
positive constant times integral_0^epsilon y^(2nu-2sigma)dy: set z=uy,
1<u<2. This diverges at and above sigma=nu+1/2. To obtain the upper
bound below that value, split the double integral into comparable
positive radii, comparable negative radii and separated radii. For
comparable radii the mean value bound and the same scaling apply;
for separated radii use |f(y)-f(z)|^2<=2(|f(y)|^2+|f(z)|^2), and integrate
the larger radius first. The opposite-sign comparable case has the
same scaling. All parts are finite under the displayed condition.
Smooth cutoff terms cause no restriction. This proves (4); larger
orders fail by Sobolev inclusion.

The analogous cofactor is chi_0(y)|y|^(beta-1), with exponent in (2/3,1).
Its first derivative is a nonzero multiple of sgn(y)|y|^(beta-2), so
the identical argument gives threshold beta-1/2. Tensoring with a
nonzero smooth x cutoff does not change these thresholds: Fourier
transformation gives upper and lower comparisons with the one-dimensional
Hs norm, restricting the x frequency to a fixed bounded set for the
lower comparison. Multiplication by x^4 or x^2 on a neighborhood of a
nonzero x0 is invertible and smooth. Cylinder coordinates (log r,theta)
are smooth there, so the cofactor's angular threshold is the same.
The C^(1,beta-1) statement follows directly from the first derivative's
power beta-1, with strict failure for a larger Holder exponent.

## Consequences for earlier proposed high spaces

The forcing f belongs to the factored high spaces of topics54 and57:
it is compactly supported away from the origin, and its quotient by
x^2 y is smooth (psi/y is smooth because psi vanishes near0). Thus it
is an admissible smooth high forcing for any target that contains
these functions.

The solution cannot belong to the global factored cylinder H7 space:
on every nonzero x-axis segment the cofactor fails Hsigma once
sigma>=3/2-1/D. Adding a compact Hs_K component away from x=0 does not
repair the corner. There is a positive distance from K to the vertical
axis, and choosing x0 closer to0 leaves the same forbidden H7 cofactor
singularity on a neighborhood disjoint from K. Independently, choosing
s>=5/2-1/D on a source neighborhood intersecting the x-axis would exclude
the ordinary solution even there. These conclusions hold for the frozen
operator's inverse, not automatically for the actual profile inverse.

The cone-local space of proof 63 allows ordinary Hs in the x-axis
angular region down to the origin. Locally near0, (3) has total radial
order 4+beta. Dividing by its bulk factor r^(3+delta) leaves radial
order 1+beta-delta>0 for delta<2. Its local angular Hs membership is
therefore compatible with any 2<s<5/2-1/D. This is only a check of this
corner singularity; no global frozen inverse bound in that high space
is inferred, in particular at infinity.

Parity alone does not improve the energy threshold for arbitrary R
data. Even functions |x|^m with noninteger m>a-1/2 are permitted by R.
The first allowable even integer m=4 applies to smooth forcings with
an integer Taylor expansion. Claims of a better threshold must state
that smoothness hypothesis, and require a sufficiency argument if they
claim more than this explicit obstruction. To see the distinction as an
explicit counterexample, take f_m=|x|^m chi(x)psi(y) with
 a-1/2<m<4. This is even in x and belongs to R. The same calculation
gives h_m=-C_m |x|^m sgn(y)|y|^((1+mA)/D) locally. Its ordinary local
threshold at every nonzero x-axis point is (1+mA)/D+1/2, strictly below
the m=4 threshold and tending to

    (1+(a-1/2)A)/D+1/2=(1+ell+aA)/D

as m decreases to a-1/2. Thus the energy threshold is sharp for this
family of parity-compatible R data. Taking m=31/8 already disproves
any parity-only improvement to the m=4 threshold.

## Why rescaling alone is not a transfer proof

Near the true corner V=diag(-A,D)X+O(r^3), grad rho=O(r^2). For a fixed
smooth compact profile H and H_lambda(X)=H(lambda X), homogeneity of
the canonical velocity indeed gives, on any fixed rescaled compact set,

    (V-diag(-A,D)X).grad H_lambda = O(lambda^(-2)),
    U[H_lambda].grad rho = O(lambda^(-2)).                  (6)

These orders describe the locally rescaled operator on prescribed
profiles. They do not establish asymptotics of its selected inverse.
In particular, one must prove a uniform inverse selection, control
nonlocal contributions from outside the rescaled set, and show that
the coefficient of the corner singularity is nonzero for the selected
forcing. Operator convergence on smooth tests alone proves none of
these three assertions. For a conforming profile H with finite c[H], change of variables in
its homogeneous degree-minus-three kernel gives c[H_lambda]=lambda c[H].
Since H0(Y/lambda)=lambda^(-3)x_Y^2 y_Y near0, the normalized rank term
c[H_lambda]H0 is also O(lambda^(-2)) there. Globally its coefficient
grows like lambda. Thus even its correct local scaling does not give
the global inverse or the nonzero singular coefficient.

Thus the explicit frozen obstruction is CONFIRMED. The proposed claim
that every sufficiently concentrated f_lambda necessarily produces the
same nonzero singular term for the full operator is OPEN. It is not
used to declare the actual high spaces impossible.

## Verification evidence and dependencies

All new characteristic and regularity arguments are given above.
The numerical exponents are recomputed from the exact binary rational
k in the read-only original NPZ, with ell=1/k. The evidence records
exact fractions and conservative decimal intervals. No numerical
quadrature of a selected bump is needed: C>0 follows analytically.
No nonlinear existence theorem is claimed.
