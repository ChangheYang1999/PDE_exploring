# Smooth global stream and temperature search representation

Date:2026-10-20. Status: representation identities independently derived;
implementation tests and additional Opus audit pending. This is a search
space, not a completeness claim and not an existence result.

## 1. Statement and notation

Fix beta>=2, nu=1/beta, q=x^2+y^2, z=x+i y. Let P_k be Re(z^k)
for positive odd k and Im(z^k) for positive even k. Then P_k is a
homogeneous harmonic polynomial of degree k, odd in x, and divisible
by x. Let Q_l be Re(z^l) for even l>=0 and Im(z^l) for odd l>=1.
Then Q_l is homogeneous harmonic and even in x. In particular
P_1=x, P_2=2xy, Q_0=1, Q_1=y. These choices impose no y parity.
All sums below are finite and all coefficients are real.

For stream labels (k,n,j), k,n>=1, j>=0, put

    a=(2-n nu-k)/2,
    f_{a,j}(q)=q^j(1+q)^(a-j),                         (1)
    S_{k,n,j}=P_k f_{a,j}.

For k=1,j=0 replace f in(1) by

    f^*_{a,0}(q)=[(1+q)^a-1]/a if a!=0,
    f^*_{0,0}(q)=log(1+q).                            (2)

Formula(2) is smooth jointly in a,q for q>=0, computed as
expm1(a log1p q)/a, with the continuous value at a=0. It has
f(0)=0, f'(0)=1. Define S_*=S_{1,1,0}, T_*=S_{2,1,0}.
For every other stream label define the projected column

    Sbar=S - d S_* - e T_*,
    d=f'(0) if k=1 and0 otherwise,
    e=1 if k=2,j=0 and0 otherwise.                    (3)

Omit the labels of S_* and T_* from the free coefficient list.
A normalized stream is

    Psi=-(nu/2) S_* +(c/2) T_* +sum v_i Sbar_i,
    c=1+beta/2, U=(-Psi_y,Psi_x), Omega=-Delta Psi.     (4)

For temperature labels (l,h,j), l,h,j>=0, put

    d_lh=-(1+(h+2)nu+l)/2,
    T_lhj=Q_l q^j(1+q)^(d_lh-j).

Let F_*=T_000 and project every other column by
Tbar=T-T(0)F_*, omitting label000. Define

    F=F_*+sum w_i Tbar_i, Theta=x^2 F.                (5)

Then every field(4)-(5) is globally smooth, has B2 parity and the axis
condition, and satisfies the exact normalization and center constraints

    F(0)=1, U(0)=0, Psi_xy(0)=c,
    Omega_x(0)=4/beta.                               (6)

Moreover Omega=O((1+r)^(-nu)), U=o(r), Theta=O((1+r)^(1-2nu)).
The velocity equals the absolutely convergent canonical relative
Biot-Savart inverse of Omega. The convention U(0)=0 is the relative
representative, not a restriction to B1: a chosen observer v0 restores
U_phys=U+v0 and the corresponding material-center path. The coefficient
search uses W=beta X+U, exactly equal to beta X+U_phys-U_phys(0).
No fitted independent drift, wall, affine strain or exterior source is
present. These assertions do not state either transport equation.

## 2. Center and inverse proof

Every radial factor is analytic in q near q>=0. The parity assertions
follow from those of P_k,Q_l. For any harmonic homogeneous P_k,
Euler's identity X.grad P_k=k P_k gives

    Delta(P_k f(q))=P_k L_k f(q),
    L_k f=4q f''+4(k+1)f'.                           (7)

Thus only k=1 contributes to Omega_x(0), giving -8f'(0).
For the generic f in(1), f'(0)=1 for j=1 and0 for j>=2.
For(2), f'(0)=1. The only contribution to Psi_xy(0) is
P_2 f(0)=2xy f(0), with f(0)=1 exactly for k=2,j=0.
The k=1 terms have f(0)=0, so Psi_x(0)=0; no other degree gives
a nonzero first derivative. Projection(3) removes each free column's
contribution to both center derivatives. The particular coefficients
in(4) give (-8)(-nu/2)=4nu and2(c/2)=c. Formula(5) fixes F(0)=1.
This proves(6). It also proves that the reduced center residuals vanish:
A(0)=beta-c=(beta-2)/2 and (A(0)+1)G(0)=2.

For generic stream factors, at infinity S and its derivative of order m
are O(r^(2-n nu-m)). The special formula(2), for a!=0, is the sum of
x(1+q)^a/a and the harmonic term -x/a. Its velocity is a constant plus
O(r^(1-n nu)); its vorticity is O(r^(-n nu)). When a=0 it is
x log(1+q), with velocity O(log r) and vorticity O(r^-1).
Here a=0 occurs exactly when n nu=1. In a finite sum, these estimates
imply the stated bounds with nu<=1/2. For temperature, T_lhj and
its derivatives have leading order r^(-1-(h+2)nu); multiplication
by x^2 gives the asserted temperature growth. Projection subtracts
only reference columns with the same or slower allowed bounds.
All derivative assertions refer to r>=1 and follow by differentiating
the explicit smooth factors.

Let K(z)=(z2,-z1)/(2pi|z|^2). The integral

    B(X)=int_R2 [K(X-Y)-K(-Y)]Omega(Y)dY              (8)

converges absolutely. The two local singularities are integrable;
for |Y|>2|X| the difference is O(|X|/|Y|^2), and nu>0 makes the
tail integrable. A three-region split bounds B by C(1+r^(1-nu)).
Smoothly truncating the source and passing to local uniform limits
gives div B=0 and -curl B=Omega. Hence U-B has harmonic components,
is smooth and sublinear, and vanishes at0. Interior gradient estimates
on expanding disks make its gradient zero; its value at0 then gives
U=B. This identifies the exact full-plane relative inverse, including
the constants carried by the k=1 subtraction. It is not a finite-box
Poisson inversion or an imposed harmonic correction.

At beta2 all finite members are real analytic, so the previously proved
analytic exclusion implies no exact nontrivial member can solve both
transport equations. Their use at beta2 is only as an approximation
attempt; no approximation theorem for the necessary flat-point behavior
is asserted. For beta>2, no density or completeness claim is made either.

## 3. Stable Cartesian differentiation and residuals

Write H=Psi/x using the polynomial P_k/x, valid also at x=0.
For a single stream term, denoting R_k=P_k/x, exact formulas are

    V1/x=-(R_{k,y}f+2y R_k f'),
    V2=P_{k,x}f+2x P_k f',
    G=Omega/x=-R_k L_k f,
    G_x=-R_{k,x}L_k f-2x R_k (L_k f)',
    G_y=-R_{k,y}L_k f-2y R_k (L_k f)',
    (L_k f)'=4q f'''+4(k+2)f''.                      (9)

These are polynomial formulas with no numerical division by x.
Temperature coefficients give F and its first derivatives directly.
For f=q^j(1+q)^b the mth derivative, m<=3, is

    sum_{i=0}^{min(j,m)} binom(m,i) (j)_i q^(j-i)
                                  (b)_{m-i}(1+q)^(b-m+i),       (10)

where (v)_i=v(v-1)...(v-i+1), (v)_0=1. For(2), f'= (1+q)^(a-1),
f''=(a-1)(1+q)^(a-2), f'''=(a-1)(a-2)(1+q)^(a-3).
Equation(10) is Leibniz's rule, including the polynomial cases at0.

Set A=beta+V1/x and B=beta y+V2. The exact divided residuals are

    RF=A(2F+x F_x)+B F_y-(beta-2)F,
    RG=A(G+x G_x)+B G_y+G-2F-x F_x.                 (11)

The prompt's Cartesian residuals are RTheta=x^2 RF and ROmega=x RG.
Both divided equations and their axis limits must be checked; small
Cartesian residuals near x=0 alone carry no information. Pointwise
normalized residuals use the sum of the absolute values of the terms
specified in the prompt, or all separate terms of(11), without a floor:
0/0 is reported0, nonzero/0 as infinity, and any underflow is counted.

## 4. Exact coefficient Jacobian and verification requirements

All displayed fields are affine in coefficients v,w for fixed beta.
Let (Aj,Bj,Gj,Gxj,Gyj) be a stream column and (Fi,Fxi,Fyi) a temperature
column. Differentiation of(11) yields

    dRF/dvj=Aj(2F+x Fx)+Bj Fy,
    dRF/dwi=A(2Fi+x Fxi)+B Fyi-(beta-2)Fi,
    dRG/dvj=Aj(G+x Gx)+A(Gj+x Gxj)+Bj Gy+B Gyj+Gj,
    dRG/dwi=-2Fi-x Fxi.                             (12)

For fixed beta this Jacobian is exact up to arithmetic evaluation. A
free-beta search must vary the exponents, particular stream, and every
projected column with beta, rather than fitting a PDE exponent while
holding the tail envelope fixed. A numerical beta column must be checked
under step refinement. Residual training weights may compensate far-tail
amplitudes but are not substituted for the prompt's diagnostics.

Before treating any fit as evidence, separately check these formulas by
Cartesian finite differences and the independent physical-space inverse,
including axis limits, multiple beta and the logarithmic a=0 case.
Use independent evaluation nodes and report resolution and domain effects.
No numerical success is claimed in this document.

Dependencies: homogeneous harmonic polynomial identities, elementary
Leibniz differentiation, full-plane relative inverse uniqueness by
harmonic gradient estimates, and the exact B2 equations. The inverse
argument is complete here. The beta2 scope warning additionally uses
packet08's independently audited analytic exclusion.
