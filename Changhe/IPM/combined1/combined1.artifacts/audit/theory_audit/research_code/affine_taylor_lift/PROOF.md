# A constructive affine lift of the five Taylor constraints

Status: OPEN independent Opus review. This proof precedes the exact candidate
calculation. The result supplies a feasible affine step for the physical-metric
minimization problem. It is not an existence theorem for stationary IPM.

## Statement, notation and hypotheses

Let c be a nonzero real number and p=(3+1/c)/2. Let chi be an even-in-x,
even-in-y smooth potential near the origin. Define

    rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy),
    F(chi)=(c(x,y)+u).grad rho-rho, a=rho_y(0).

Assume chi_xxyy(0)=1-c and a-4c+2 != 0, a-8c+4 != 0. Let C(chi) be the
five coefficients of x^2,y^2,x^4,x^2 y^2,y^4 in F(chi)/y, in this order.
All coefficients below concern the jet at the origin.

For (i,j) in {(2,1),(0,3),(3,1),(1,3),(0,4)} put

    e_(i,j)=x^(2i)y^(2j)(1+x^2+y^2)^(p-i-j-2).

Let eta=alpha e_(2,1)+beta e_(0,3)+gamma e_(3,1)
+delta e_(1,3)+epsilon e_(0,4) be the unique correction supplied by the
audited T4-211 theorem, so C(chi+eta)=0. Set

    K=60(a-8c+4),
    u0=-192 alpha^2/K,
    v0=18 alpha beta/c,
    w0=(a-4)v0/112,
    tau=u0 e_(3,1)+v0 e_(1,3)+w0 e_(0,4),
    z=eta+tau.

Then z is the unique element of span{e_(2,1),e_(0,3),e_(3,1),e_(1,3),e_(0,4)}
satisfying the affine Taylor equation

    C(chi)+DC(chi)[z]=0.                                      (1)

Both eta and z preserve a and the origin strain. Their difference tau
begins at potential degree eight and has coefficients quadratic in
alpha,beta. The nonlinear constraints of the affine step are instead

    C(chi+z)=(0,0,-192 alpha^2,-8640 alpha beta,0).             (2)

Thus an affine feasible step generally needs a nonlinear retraction after
it is taken. Equations (1) and (2) refer to different constraints.

When c equals the frozen candidate007 exponent, all five e_(i,j), hence
eta, tau and z, belong to its existing potential span and preserve its
leading and first-descendant tail rows. No assertion of membership in
that frozen span is made for other c.

## Proof

The exact Taylor identity proved in T4-241 is

    C(chi)+DC(chi)[eta]=(0,0,192 alpha^2,8640 alpha beta,0).    (3)

For completeness, the leading potential correction is alpha x^4 y^2
+beta y^6. Its induced density is -24 alpha x^2 y-120 beta y^3 and its
velocity is (-8 alpha x^3,24 alpha x^2 y). Consequently its quadratic
transport contribution is -192 alpha^2 x^4 y-8640 alpha beta x^2 y^3.
Every interaction involving a potential term of degree at least eight
has degree at least seven in F and cannot enter C. Since C(chi+eta)=0,
the exact quadratic expansion of F gives (3).

The last three basis functions begin at degree eight. Their changes to
the last three entries of C are linear, with matrix

    [ K            0        0 ]
    [ 0          -480c      0 ]
    [ 0          12(a-4) -1344 ].                            (4)

To verify (4), use the leading linear variation for a homogeneous
potential M of degree eight,

    ((2c-1)x partial_x+y partial_y-1)(-partial_y Delta M)
       +a M_xxy,

and substitute M=x^6 y^2, x^2 y^6, y^8. Terms in chi beyond its degree-four
jet cannot enter these entries. The first two entries do not change.
Multiplying (4) by (u0,v0,w0) gives exactly
(-192 alpha^2,-8640 alpha beta,0). Together with (3) this proves (1).

The full five-by-five derivative matrix on this correction space is
block lower triangular. Its diagonal entries are

    24(a-4c+2), -240, K, -480c, -1344.

They are nonzero by the hypotheses. Hence (1) has exactly one solution
in this space. The quadratic transport contribution of z is the same
as that of eta, because tau begins at degree eight. Applying the exact
quadratic expansion again to the zero affine residual proves (2).
The degree of all five corrections is at least six, so they do not
change a or chi_xxyy(0).

For the tail statement, write l=i+j and expand x^(2i)y^(2j) in the even
harmonics H_m=Re(x+iy)^(2m) times powers of r^2. In block (0,m), the
resulting radial polynomial is a constant multiple of

    t^(l-m)(1-t)^2, t=r^2/(1+r^2).

Its value and first derivative vanish at t=1. The exact T4-209 membership
check places these finitely many polynomials in the frozen007 span
when c=c007. This proves the stated tail claim without changing the
exponent of any basis function.

## Whole-plane density size, when c>1

Let B_ij be the whole-plane L2 norm of -partial_y Delta e_(i,j).
These norms are finite for c>1. The triangle inequality gives

    ||rho[tau]||2 <= |u0|B_31+|v0|B_13+|w0|B_04,             (5)
    ||rho[z]||2 <= ||rho[eta]||2+||rho[tau]||2.

The audited T4-211 computation expresses every B_ij^2 as pi times an
exact positive rational at rational c. It follows by differentiating
M(1+r^2)^q three times and integrating each polynomial-square monomial
with the beta integral. Substitution of those exact rationals into
(5), followed by outward ball arithmetic, certifies its bound.

## Verification and scope

The exact candidate check will reconstruct chi, eta, tau and z in two
ways: from their local polynomial jets and from their frozen canonical
coordinates. It will verify all five affine equations, all five values
in (2), origin strain, density slope, and all affected tail moments.
All correction parameters and coordinate changes are retained as exact
JSON. No candidate snapshot is published or altered.

Dependencies: audited T4-211/T4-233 for the nonlinear correction,
T4-241/T4-247 for its quadratic defect, T4-209 for the five directions'
frozen-basis membership, and elementary differentiation and the triangle
inequality. A small affine step is not a solution of the nonlinear PDE.
