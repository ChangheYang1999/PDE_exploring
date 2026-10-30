# Exact triangular projection onto the five origin equations

Status: proposed theorem, OPEN independent Opus review. The proof is written
before the candidate calculation. This is a finite algebraic correction,
not an existence theorem for the stationary IPM equation.

## Statement

Let c be a nonzero real number, put p=(3+1/c)/2, and let chi be a smooth
even-in-x, even-in-y potential near the origin. Define

    rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy),
    F=(cX+u).grad rho-rho, a=rho_y(0).

Assume chi_xxyy(0)=1-c and

    a-4c+2 != 0, a-8c+4 != 0.

For each pair (i,j) in {(2,1),(0,3),(3,1),(1,3),(0,4)}, define

    eta_(i,j)=x^(2i)y^(2j)(1+x^2+y^2)^(p-i-j-2).

There are unique real numbers alpha,beta,gamma,delta,epsilon such that

    chi*=chi+alpha eta_(2,1)+beta eta_(0,3)
             +gamma eta_(3,1)+delta eta_(1,3)+epsilon eta_(0,4)

has zero coefficients of x^2,y^2,x^4,x^2y^2,y^4 in F*/y. The correction
preserves a and chi_xxyy(0). Its constant coefficient in F*/y is also zero.
The five parameters are rational functions of c and the order-eight jet
of chi. They are rational numbers for rational input jets. This map is
idempotent: applying it to chi* returns five zero correction parameters.

Each eta is a member of the candidate007 potential span and annihilates
all its leading and first-descendant tail constraints, as checked in
T4-209. Thus the construction remains in the same tail/strain fiber. It
does not assert that all later residual Taylor coefficients vanish.

## Proof

Write X=x^2, Y=y^2 and chi=phi(X,Y). Direct differentiation gives

    rho=y R, u1=x U, u2=y W,
    R=-4phi_XY-12phi_YY-8X phi_XXY-8Y phi_YYY,
    U=-4phi_XY-8Y phi_XYY,
    W=4phi_XY+8X phi_XXY,
    F/y=2X(c+U)R_X+2Y(c+W)R_Y+(c+W-1)R.

The assumed strain implies W(0)=1-c, U(0)=c-1. The constant coefficient
of F/y is (c+W(0)-1)a=0. All five eta begin at physical degree at least6,
so they preserve a, U(0), and W(0).

For a homogeneous even potential M of degree at least6, the leading
linear residual variation is

    ((2c-1)x partial_x+y partial_y-1)(-partial_y Delta M)
       + a M_xxy.

Quadratic interactions between degree6 potential corrections first appear
at degree5 in F, hence degree4 in F/y. Consequently the degree2
coefficients in F/y depend affinely on alpha,beta and do not depend on
gamma,delta,epsilon. Their coefficient matrix is diagonal:

    A=24(a-4c+2), B=-240.

If f20 and f02 are the initial coefficients of X,Y, set

    alpha=-f20/A, beta=-f02/B,
    chi1=chi+alpha eta_(2,1)+beta eta_(0,3).

The two degree2 coefficients now vanish exactly. Evaluate the three
degree4 coefficients g40,g22,g04 of F1/y. They include every background
interaction, the quadratic alpha/beta interactions, and the higher jets
of eta_(2,1),eta_(0,3).

The last three eta begin at physical degree8. Their interaction with a
degree6 correction first contributes at physical degree7 in F, beyond
the requested coefficients. Their mutual interactions start later still.
Their effect on the degree4 coefficients is exactly the lower triangular
matrix

    [ C            0          0 ]
    [ 0          -480c        0 ]
    [ 0          12(a-4)   -1344 ],
    C=60(a-8c+4).

Therefore

    gamma=-g40/C,
    delta=g22/(480c),
    epsilon=(g04+12(a-4)delta)/1344.

This gives all five zero coefficients, and the nonzero diagonal gives
uniqueness. It also proves the rational dependence and idempotence.
Only the order-eight potential jet enters these computations: discarded
physical degrees at least10 give F/y degree at least6.

For the tail claim, write l=i+j and expand

    x^(2i)y^(2j)=sum_(m=0)^l b_m H_m r^(2(l-m)),
    H_m=Re(x+iy)^(2m).

Then eta_(i,j) in block (0,m) has polynomial
b_m t^(l-m)(1-t)^2, t=r^2/(1+r^2). Its value and first derivative at t=1
are zero. The existing candidate007 block monomials contain these finite
polynomials, as independently checked in T4-209. No other branch changes.
This proves preservation of all stated tail constraints.

## Scope and verification

The retained correction parameters will be stored in exact JSON. A second
construction of the patched canonical potential jet will verify all six
residual coefficients exactly and check all endpoint moments. This is an
algebraic artifact in the T4 lane, not a published candidate snapshot.
Norms or exclusion margins of candidate007 cannot automatically be copied
to the patched potential without an explicit perturbation estimate.

## Optional exact L2 size bound for c>1

For one direction eta=M(1+r^2)^q, where M=x^(2i)y^(2j), l=i+j and
q=p-l-2, define the polynomial derivative operator

    D_x^q P=(1+r^2)partial_x P+2q xP

and the corresponding y operator. Three applications, with exponent
reduced by one each time, give a polynomial H such that

    -partial_y Delta eta=(1+r^2)^(p-l-5) H(x,y).

The degree of H is at most2l+3. Set A=2l+7-1/c. The square of this
factor has radial exponent -A. For nonnegative integers u,v with
A>u+v+1, polar integration and the beta integral give

    integral_R2 x^(2u)y^(2v)(1+r^2)^(-A) dxdy
       = pi (2u)!(2v)!/[4^(u+v)u!v!]
         / product_(k=1)^(u+v+1)(A-k).

For c>1 all polynomial-square moments here meet this condition. Odd
moments vanish by parity. Thus each direction's squared density norm
is pi times an exactly computable positive rational. If those five
norms are B_i and the correction parameters are t_i, the triangle
inequality proves

    ||rho*-rho||2 <= sum_i |t_i| B_i.

An outward ball evaluation of this sum is a rigorous norm upper bound.
It uses no grid or radial cutoff. Any pre-existing necessary distance
||rho_solution-rho||2>d then gives distance greater than d minus this
upper bound from rho*. This transfers that distance obstruction only;
other background or residual certificates require their own checks.
