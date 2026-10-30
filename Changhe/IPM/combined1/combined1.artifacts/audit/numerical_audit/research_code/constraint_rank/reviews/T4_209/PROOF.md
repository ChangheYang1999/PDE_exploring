# Independent audit of the physical constraint dimension

Status: independent audit of N4-164. The proof precedes the local
calculation. All numerical conclusions refer to the frozen exact
candidate007 and its existing2982 generator coordinates.

## Exact assertion

Let V be the1922-dimensional real potential function span independently
confirmed in T4-195. Its blocks are

    H_m(x,y)(1+r^2)^(p_j-m) P(t),
    p_j=(3+1/c-j(1-1/c))/2, t=r^2/(1+r^2),
    c=4076476460239181/2251799813685248.

There are360 blocks. Impose each block's leading moment, the first
descendant in the60 blocks j=0,1,2, and the center strain. Then the
linear constraint rank is421. Adding the differentials of the five
coefficients of x^2,y^2,x^4,x^2y^2,y^4 in F/y gives rank426 at the
exact candidate, provided the two exactly checked factors

    a0-4c+2, a0-8c+4, where a0=rho_y(0),

are nonzero. Thus the tangent kernel in V has dimension1496 and its
preimage in the2982 coefficient coordinates has dimension2556. The
latter still contains all1060 zero-potential directions. These are
constraint ranks, not residual Jacobian ranks or inverse estimates.
The candidate need not solve the five Taylor equations for this
rank calculation. The verifier explicitly records their values.

## 1. Tail rows and test directions

For a block polynomial P the leading and first descendant functionals
are

    L0(P)=P(1), L1(P)=(p_j-m)P(1)-P'(1).

The local checker constructs shifted Legendre coefficients by the
explicit binomial sum and finds a nonzero1x1 or2x2 minor in every
block. Blocks are independent by T4-195's exact angular and radial
nonresonance proof. The total tail rank is420.

Put l=a+b and

    eta_(a,b)=x^(2a)y^(2b)(1+r^2)^(p0-l-2).

For l<=4, expand the homogeneous polynomial x^(2a)y^(2b) uniquely as
sum_(m=0)^l w_m H_m r^(2(l-m)). The harmonic matrix is nonsingular:
on the unit circle its basis restricts to the independent functions
1,cos(2theta),...,cos(2l theta). In block(0,m) the remaining factor
is w_m t^(l-m)(1-t)^2. The checker verifies that its nonzero monomials
are present in the frozen block and checks both zero endpoint moments.
Hence all these functions lie in the tail kernel.

Use the six pairs

    (1,1),(2,1),(0,3),(3,1),(1,3),(0,4).

The first has strain4, the rest strain0. This raises the linear rank
to421. At a normalized background the linearized leading residual
from a homogeneous potential M of even degree at least6 is

    ((2c-1)x partial_x+y partial_y-1)(-partial_y Delta M)
       +a0 M_xxy.

Dividing by y, the degree6 pair gives diagonal24(a0-4c+2),-240 on
rows x^2,y^2. The degree8 triple gives the matrix

    [60(a0-8c+4)       0          0]
    [      0        -480c        0]
    [      0       12(a0-4)   -1344]

on rows x^4,x^2y^2,y^4. Higher terms and higher background jets only
enter below these blocks. The full determinant is therefore

    4*24(a0-4c+2)*(-240)*60(a0-8c+4)*(-480c)*(-1344).

Its nonzero value proves rank426. The opposite bound is the number
of rows. Rank-nullity then gives both tangent dimensions.

## 2. Independent squared-coordinate jet calculation

To avoid repeating N4's Cartesian differentiation code, set X=x^2,
Y=y^2 and write chi=phi(X,Y). Define rho=y R, u1=x U and u2=y W.
Direct differentiation gives

    R=-4phi_XY-12phi_YY-8X phi_XXY-8Y phi_YYY,
    U=-4phi_XY-8Y phi_XYY,
    W=4phi_XY+8X phi_XXY.

Consequently

    F/y=2X(c+U) R_X+2Y(c+W) R_Y+(c+W-1)R.           (1)

These exact polynomial formulas retain the full local velocity,
including strain W(0). They compute both the candidate Taylor
coefficients and the derivative columns in six independent eta
directions. The differential of(1) is used directly, with background
R,U,W fixed; no finite difference or floating derivative is involved.

The canonical potential is truncated at degree4 in X,Y, equivalent
to degree8 in x,y. This determines R,U,W through degree2 and F/y
through degree2 because three physical derivatives reduce an even
potential's degree by3. Discarded potential degree at least10 affects
F/y only at degree at least3. Thus the truncation is exact for every
coefficient used here.

## 3. Feasibility and scope

The center relation c+W(0)=1 is exact. The five other Taylor equations
are not assumed to vanish; their full rational values are retained
and compared with N4. A rank426 differential at this point describes
the level set at its actual constraint values. It does not put the
candidate on the zero-Taylor level set. Conditional on a feasible
point with the same nonzero determinant, the finite-dimensional
implicit function theorem gives a local1496-dimensional constraint
manifold. No existence theorem for the IPM equation follows.

Dependencies: T4-195's exact potential rank, polynomial differentiation,
rational finite-dimensional linear algebra and, only for the conditional
level-set interpretation, the elementary implicit function theorem.
No numerical optimizer or external code is executed in this audit.
