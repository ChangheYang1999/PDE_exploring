# Exact origin repair and its complete density perturbation norm

## Statement

Let c>1, gamma=1/c, p=(3+gamma)/2, and let chi be a smooth even
potential near the origin. Set rho=-partial_y Delta chi,
u=(-chi_xyy,chi_xxy), F=(cX+u).grad rho-rho and a=rho_y(0).
Suppose chi_xxyy(0)=1-c and both a-4c+2 and a-8c+4 are nonzero.
For the ordered pairs

    (i,j)=(2,1),(0,3),(3,1),(1,3),(0,4),

put l=i+j and eta_ij=x^(2i)y^(2j)(1+r^2)^(p-l-2).
There is a unique five-parameter correction in these directions that
sets the coefficients of 1,x^2,y^2,x^4,x^2y^2,y^4 in F/y to zero.
It preserves a and chi_xxyy(0), depends rationally on the order-eight
jet and c, and is idempotent. For candidate007 at its exact reference
c, these directions belong to its canonical span and preserve every
imposed leading and first-descendant tail row. The membership assertion
is at this c; a potential basis frozen at one exponent need not contain
these functions at another c.

This audit reconstructs the correction with Cartesian Taylor polynomials,
independently of T4-211's squared-coordinate calculation. It also
computes the exact squared L2 norm of the combined density change,
including every cross term. The exact potential changes are an algebraic
artifact. They do not solve the stationary PDE or supply residual smallness.

## Triangular origin equations

Write the linear origin fields as rho=a y+O(r^3),
u=((c-1)x,(1-c)y)+O(r^3). These follow from evenness and the strain.
For a homogeneous even potential M of degree d>=6, its leading residual
variation is

    ((2c-1)x partial_x+y partial_y-1)(-partial_y Delta M)
         +a M_xxy.

Indeed the first term is the background drift on the density variation,
and the second is the velocity variation acting on a y. The quadratic
interaction of degree d and e potential perturbations starts at degree
d+e-7 in F. A degree6 perturbation can therefore affect the cubic and
quintic residual, whereas a degree8 perturbation affects the quintic
residual affinely and cannot change the cubic residual.

Let f20,f02 be the x^2,y^2 coefficients of F/y. Direct monomial
differentiation gives the diagonal degree6 response

    diag(24(a-4c+2), -240).

Hence alpha=-f20/[24(a-4c+2)] and beta=f02/240 are forced.
Apply these two corrections, including their degree8 Taylor terms and
all their quadratic interactions, and call the resulting quartic
coefficients g40,g22,g04. The three degree8 directions have response

    [60(a-8c+4)       0           0]
    [     0        -480c         0]
    [     0        12(a-4)    -1344].

Thus gamma0=-g40/[60(a-8c+4)], delta0=g22/(480c), and
epsilon0=[g04+12(a-4)delta0]/1344. Every denominator is nonzero.
This proves existence and uniqueness of the five parameters. The
constant residual coefficient is (c+u2_y(0)-1)a=0 throughout.
The perturbations begin at degree6, so a and the strain do not change.
Only the order-eight potential jet contributes. Rational operations
prove rational dependence; a second application starts from five zero
coefficients and returns zero parameters.

For tail preservation, expand x^(2i)y^(2j) in the homogeneous harmonics
H_m=Re(x+iy)^(2m) times r^(2(l-m)). Its coefficient in block (0,m) is
then a rational multiple of t^(l-m)(1-t)^2, t=r^2/(1+r^2).
Both value and derivative vanish at t=1. These are precisely the two
endpoint moments of each affected block. The independently confirmed
constraint-rank record supplies the finite harmonic expansions and
basis membership. The audit also reconstructs the full Cartesian
order-eight jet from the resulting canonical changes.

## Independent complete-plane perturbation norm

Put S=1+r^2. For nonnegative a,b, direct repeated product differentiation
gives

    partial_x^a partial_y^b S^q
      =sum_(h,k) a! b! (2x)^(a-2h)(2y)^(b-2k)
         (q)fall_(a+b-h-k) S^(q-a-b+h+k)
         /[h! k! (a-2h)! (b-2k)!],

where 0<=2h<=a and 0<=2k<=b. To see this, each pair of derivatives
that hits the same quadratic S contributes one second derivative,
and every unpaired derivative contributes 2x or 2y. Counting the
choices gives the stated factorial coefficient. This can also be
proved by differentiating once more and collecting adjacent h,k terms.
Leibniz's rule with this formula constructs a rational polynomial H_ij
such that

    -partial_y Delta eta_ij=S^(p-l-5) H_ij.

This route does not use the peer's recursive polynomial derivative
operator. The degree is at most2l+3. Since l is3 or4, the full density
change is S^(p-9) H, with

    H=S(alpha H_21+beta H_03)
                   +gamma0 H_31+delta0 H_13+epsilon0 H_04.

It has degree at most11, is even in x and odd in y. Its squared norm
is the integral of H^2 S^(-A), where A=18-2p=15-gamma>14.
For nonnegative integers u,v with A>u+v+1, polar coordinates give

    int_R2 x^(2u)y^(2v) S^(-A)
      =pi (1/2)_u (1/2)_v
                   /product_(k=1)^(u+v+1)(A-k).

Here (1/2)_u is the product of i-1/2 for i=1..u. The identity follows
by multiplying the angular beta integral and the radial beta integral;
all half-integer gamma factors simplify to the displayed products.
Odd moments vanish by reflection. Every term in H^2 has u+v<=11,
so all moments converge. Summing them exactly over Q gives

    ||rho_repaired-rho||2^2=pi times a nonnegative rational.

All cross terms are included. Outward ball evaluation provides strict
rational upper bounds for the square root. For comparison, evaluating
the five individual norms and summing |parameter| times each norm
reproduces T4-211's triangle bound independently.

## Consequence and scope

For any class of exact solutions already known to satisfy
||rho_solution-rho007||2>d, the triangle inequality gives

    ||rho_solution-rho_repaired||2>d-e,

whenever the independently bounded density change is at most e.
The reference c, canonical velocity and affine-class hypotheses of the
original exclusion remain necessary. This transfers a distance bound,
not the background matrix bounds, derivative norms or closure theorem.
Tail equality also preserves the hypotheses of the separately audited
c-pinning statement within its stated canonical weighted chart.

The code verifies the initial exact jet against N4-164, reconstructs all
five parameters, checks six final residual coefficients, idempotence,
strain, a, endpoint moments and canonical reconstruction, and compares
its values with frozen T4-211 records. Every input and helper is hashed.
The general triangular argument requires Opus review separately; the
numerical peer comparison does not substitute for that review.
