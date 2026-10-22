# Exactly normalized exterior counterterms with homogeneous H^{-1} residual

Status: new complete informal proof before the finite input audit.
This is an explicit construction of trials, not stationary profiles.

## 1. Statement and dependencies

Let rho0 be the exact normalized finite modal trial defined in
modal_repair/PROOF.md. Its canonical velocity U0, center factor and scalar
c0=1/k are the exactly defined ones, not rounded substitutes. Use the
original exact dyadic k,L,tplus and set R_b=exp(tplus). The exact input
obeys 0<k<1/4; this stronger inequality is to be checked by integer
comparison. Set

 a1=2k-1, a2=3k-2, d=k-2, a3=4k-3<-2.

Let D0,D1,D2,Dd be the actual angular coefficients of r^k, r^a1,
r^a2 and r^d in the exterior density rho0. Explicitly, with z the exact
normalization scalar and zeta=cos(2theta),

 D0=R_b^(3-k) cos^2theta sin theta sum_(m=0)^259
                      (A_m0+z delta_m0) T_m(zeta),
 D1=R_b^(3-a1) cos^2theta sin theta sum_m A_m1 T_m(zeta),
 D2=R_b^(3-a2) cos^2theta sin theta sum_m A_m2 T_m(zeta),
 Dd=R_b^(3-d) cos^2theta sin theta sum_m A_m6 T_m(zeta).             (1)

Column6 is exactly the exterior pair(j,l)=(0,1). Normalization modifies
column0 and its fast joined correction only. Every definition in(1) is
an exact real finite expression from the archived data and canonical
normalization integral. Enclosures do not redefine these coefficients.

The complete exterior representation and exact normalization are earlier
proved dependencies, in outer_majorant, outer_leading_cancellation,
modal_repair and normalized_tail_repair (topic105). They are rehashed
by the finite input audit. No new full convolution is assumed validated.

We construct explicit rho_T for every T>=max(R_b,L,1), such that:

(i) rho_T satisfies the kinematic P2 requirements: density C^(2,alpha)_loc
for some0<alpha<1, continuous even center factor rho=x^2 y a with a(0)=1,
parities, canonical sublinear velocity and sublinear density/derivative
growth. Its density equals rho0 on r<=T, its exact canonical strain at
zero is unchanged, and c0=1/k. Stationarity and P2 membership are not
claimed; nor is P_infty.

(ii) Its residual epsilon_T=(c0X+U[rho_T]).grad rho_T-rho_T obeys
r epsilon_T in L2(R2), and therefore defines a continuous functional on
the completion of C_c^infty(R2) in the gradient L2 seminorm:

 ||epsilon_T||_(dot H^-1) <= ||r epsilon_T||_L2 < infinity.         (2)

No numerical ceiling for either finite norm is supplied.

(iii) Its weighted factor distance from rho0 tends to zero as T tends
to infinity. Its correction is not in unweighted L2 and its leading
r^k angular profile D0 is unchanged. Its difference from the topic105
trial using the same T is in unweighted L2.

## 2. The angular particular velocity and ordered quadratic products

For any finite odd-sine polynomial A(theta)=sum_(j>=0) d_j
sin((2j+1)theta), let a be a real density exponent such that
(2n)^2-(a+1)^2 is nonzero in all required even stream modes. Define

 F_n=[(a+1-2n)d_(n-1)+(a+1+2n)d_n]/2,
 V_a[A]=sum_n [-2n F_n/((2n)^2-(a+1)^2)] cos(2ntheta),
 W_a[A]=sum_n [(a+1) F_n/((2n)^2-(a+1)^2)] sin(2ntheta).          (3)

Missing coefficients are zero. To verify signs and exponents,
partial_x(r^a A)=r^(a-1)(a cos theta A-sin theta A'), and direct
product-to-sum gives F_n. Applying -Delta to
r^(a+1)sin(2ntheta) gives [(2n)^2-(a+1)^2]r^(a-1)sin(2ntheta).
For U=(-psi_y,psi_x), polar components are -psi_theta/r and psi_r.
Thus r^a(V_a[A],W_a[A]) is the exterior particular velocity. We do not
extend a singular homogeneous density through zero in this definition.

For another angular density B at exponent b, define the ordered product

 B_(a,b)(A,B)=b V_a[A] B+W_a[A] B'.                              (4)

It is the coefficient of r^(a+b-1) in U[r^a A].grad(r^b B), when the
particular velocities are used. Its order matters. Both orders are
included whenever a cross term occurs.

The factor cos^2theta sin theta is preserved. Indeed, if
A=cos^2theta sin theta P_A(zeta) and B=cos^2theta sin theta P_B(zeta),
then W_a[A]=sin2theta Z_a(zeta), while V_a[A] is a polynomial in zeta.
Division of(4) by cos^2theta sin theta gives exactly

 b V_a[A] P_B + Z_a[(3zeta-1)P_B-2(1-zeta^2)P_B'].                (5)

Both sides extend polynomially across the axes. If P_A has degree M_A,
then V_a[A] and Z_a have degrees at most M_A+2 and M_A+1. Therefore the
quotient in(5) has degree at most M_A+M_B+2. This is algebraic
factorization, not division at sampled angles.

## 3. The forced exterior rows

Define the target rows by exact finite formulas

 A1= k/(1-k) B_(k,k)(D0,D0),
 A2= k/[2(1-k)] {B_(k,a1)(D0,A1)+B_(a1,k)(A1,D0)},              (6)

and define corrections

 H1=A1-D1, H2=A2-D2, Hd=-Dd.                                    (7)

The angular quotients have degrees at most520,781 and259 respectively.
Consequently every expression is finite. All denominators in(3) used
in(6) are positive: k+1 is between1 and5/4, and a1+1=2k is between0
and1/2, whereas2n>=2. The denominators for the cutoff tails H2 and Hd
are also positive because a2+1=3k-1 and d+1=k-1 lie in(-1,0).

For c0=1/k, the coefficient of r^a in the linear part (c0E-1)rho is
(a/k-1) times its angular coefficient. At exponent a1, the only
nonlinear pair above the later remainder is(k,k), and

 (a1/k-1)A1+B_(k,k)(D0,D0)=0.

At exponent a2 the only relevant ordered pairs are(k,a1) and(a1,k), so

 (a2/k-1)A2+B_(k,a1)(D0,A1)+B_(a1,k)(A1,D0)=0.                  (8)

At exponent d there is no nonlinear product at that order: all
nonlinear exponents other than a1,a2 are at most a3, and d>a3. Thus the
correct target row there is zero, achieved by Hd=-Dd. The exponent
identities use the exact k, not a fitted decimal.

The H1 here equals the topic105 correction exactly. The leading
residual of rho0 is Epsilon=(a1/k-1)D1+B_(k,k)(D0,D0), and
k Epsilon/(1-k)=-D1+A1. This identifies both the correct sign and the
nonzero H1 established there.

## 4. Cutoffs and exact canonical strain compensation

Use precisely the polynomial transition of105:

 b(s)=(s-1)^8(2-s)^8 on1<s<2 and0 otherwise,
 B0=integral_1^2 b(s)ds=(8!)^2/17!, J_b=integral_1^2 s b(s)ds=3B0/2,
 chi(s)=B0^-1 integral_1^s b(t)dt on(1,2), with values0 below1,1 above2.

For i in{1,2,d}, put a_d=d and define

 I_i=(1/pi)integral_0^(2pi) sin(3theta) H_i(theta)dtheta,
 J_i=integral_1^infinity chi(s)s^(a_i-2)ds,
 lambda_T=(4/J_b) sum_i I_i J_i T^(a_i-3),
 h_T=sum_i chi(r/T)r^a_i H_i(theta)-lambda_T x^2 y b(r/T),
 rho_T=rho0+h_T.                                                (9)

Since each a_i<1, the exact integrals J_i converge absolutely. Integration
by parts gives 0<J_i<=1/(1-a_i). They define lambda_T exactly; no
numerical quadrature or approximate center strain is substituted.

For a function vanishing near zero, the canonical raw strain is
sigma[h]=integral K_s(Y)h(Y)dY, with K_s=sin(3theta)/(pi r^3).
The plus sign includes evaluation of the odd kernel at -Y in the
convolution. Hence

 sigma[chi(r/T)r^a_i H_i]=I_i J_i T^(a_i-1),
 sigma[x^2 y b(r/T)]=T^2 J_b/4>0.

Substitution of lambda_T yields sigma[h_T]=0 exactly. The density and
factor corrections vanish identically on r<=T, while the velocity changes
analytically there. This preserves the nonlocal center normalization
3c0-psi[rho_T]_xy(0)=1 as well as a(0)=1.

The new density and factor are C7 across the two annular joins, and
vanish near the center. All earlier joins remain C6. The center regularity
and sublinear density/first-derivative growth of rho0 are unchanged.
The finitely many canonical Green integrals converge and give sublinear
velocity. The canonical gauge excludes growing homogeneous streams;
parity and sublinear growth give uniqueness as in104 and105. No P2
membership follows without the stationary equation.

## 5. The complete residual remainder

The original eleven exterior density exponents are

 k-j(1-k)-2l, (j,l)=(0,0),(1,0),...,(5,0),(0,1),(1,1),(2,1),(0,2),
 and3-bo.

For the actual input, bo>120. Other than k,a1,a2,d, every exponent is
at most a3. The four leading pure-power rows have no logarithms; the
fast joined row has logarithmic degree at most6. All its mode denominators
are nonzero by exact finite input checks, so the velocity has the same
logarithmic degree. After(9), the three leading density rows for r>=2T
are r^k D0+r^a1 A1+r^a2 A2. The d row is zero and all others have powers
at most a3.

For a cutoff r^a H at each of a1,a2,d, its exterior velocity is the
particular term(3) times r^a plus finitely many homogeneous velocities
r^(-2n-1), n>=1. This follows either from the exact radial Green formula
or by subtracting the particular solution in the exterior and using
canonical sublinear growth to remove growing homogeneous solutions.
The outer Green integral converges because its integrand has exponent
a-2n<-1. The inner lower-limit constants and compact annular sources
contribute only to the decaying homogeneous modes. The largest required
stream indices are522,783 and261 respectively.

Every particular velocity-density product other than(k,k),(k,a1),(a1,k)
has exponent at most a3. The two possibilities attaining that upper
bound are a1+a1-1 and k+a2-1=a2+k-1, all equal to a3. Every homogeneous
velocity-density product has exponent at most k-4<a3. Linear terms at
k vanish, at a1 and a2 cancel by(8), and at d are absent. All remaining
linear powers are at most a3. Thus, for each fixed T,

 epsilon_T=O(r^a3(1+log r)^12),  r->infinity.                     (10)

The finite constant may depend on T and is not evaluated here. The
integer12 allows products of two logarithmic degree6 terms; no unknown
infinite tail is being discarded. Since a3<-2, the radial integral
of r^2|epsilon_T|^2 is bounded by a constant times
integral r^(2a3+3)(1+log r)^24 dr, which converges at infinity. On compact
sets epsilon_T is continuous and therefore r epsilon_T is square
integrable. This proves the first assertion of(ii).

## 6. Homogeneous H^{-1} by an angular primitive

The residual is odd in y, so it has zero angular mean on every circle.
In fact it is a finite odd-sine polynomial for each radius. Write

 epsilon_T(r,theta)=sum_(nu odd,nu>=1) e_nu(r) sin(nu theta),
 P(r,theta)=-sum_nu e_nu(r) cos(nu theta)/nu,
 J(r,theta)=r P(r,theta) e_theta.

Then partial_theta P=epsilon_T and div J=epsilon_T distributionally.
To verify the distribution identity, integrate by parts in the periodic
theta variable for every test function. There is no radial boundary
term; the vector has only a tangential component. Local integrability
at the origin follows from J in L2. Orthogonality on each circle gives
integral|P|^2 dtheta<=integral|epsilon_T|^2 dtheta because nu>=1.
Consequently ||J||_2<=||r epsilon_T||_2. Thus

 |integral epsilon_T phi dX|=|integral J.grad phi dX|
     <=||r epsilon_T||_2 ||grad phi||_2

for every phi in C_c^infty. This extends continuously to the gradient
completion and proves(2). No positive-frequency lower bound beyond1,
compact support, or radial moment cancellation of epsilon_T is required.
The constant1 is an exact L2 angular-multiplier bound, not a proposed
small IPM Holder constant.

## 7. Weighted distance and precise limitations

Write H_i=cos^2theta sin theta Q_i(cos2theta), and let N_i be its exact
finite Chebyshev coefficient absolute sum. Set I_i^*=|I_i| and
omega=(3-k)/2. The proof in105, applied separately at each a_i, yields

 sup |h_T/(x^2 y W)| <= sum_i C_i T^(a_i-k),
 C_i=L^(k-3){2^omega N_i+
             [4 I_i^* 2^-16/((1-a_i)J_b)]5^omega},              (11)
 W=(1+(r/L)^2)^((k-3)/2).

For clarity, the tail factor is
L^(k-3) r^(a_i-k)(1+L^2/r^2)^omega Q_i; on r>=T its bound is
2^omega L^(k-3) T^(a_i-k)N_i. The compensator uses r<=2T and
J_i<=1/(1-a_i), giving the second term in(11). Add the three estimates
by the triangle inequality. All C_i are finite exact real expressions;
C_1<0.334616 is already certified in105. The two new constants C_2,C_d
are not evaluated or claimed small here. Their decay powers are

 a1-k=k-1<0, a2-k=2k-2<0, d-k=-2.

Thus the weighted factor distance tends to zero. H1 is nonzero and
r^a1 H1 is not L2 because a1+1=2k>0. The other two tails are L2 because
a2<-1 and d<-1, as is the compact compensator. Hence h_T is not L2,
and the difference from the105trial is L2.

This construction removes the previously known far-field obstruction to
membership of the residual in dot H^-1. It does not bound that norm
numerically or make it small. It does not put the scaling source
E rho_T, whose leading power is r^k, in dot H^-1. It supplies no full
linear inverse, control of the nonlocal source coupling, nonlinear
closing inequality, uncertainty class around X3, or stationary profile.
Its leading angular tail D0 remains the modal one, so the103separation
from X3 is untouched. No decisive endpoint has been established.
