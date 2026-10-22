# Quantitative size and local velocity of the higher exterior counterterms

Status: exact informal proof written before the new full angular computations.
The conclusions using decimal constants remain conditional on the two-engine
finite audit. This concerns the explicit topic106 family only.

## 1. Exact objects and statement

Import the normalized modal trial rho0, exact k=1615536043799051/9007199254740992,
c0=1/k, R_b=exp(tplus), L, and the topic106 repair rho_T. All its definitions,
canonical gauge, center factor, C6 regularity, C7 new joins, and finite Green
expansions are as in hminus1_tail_repair/PROOF.md and ADDENDUM.md. In particular
0<k<1/4, a1=2k-1, a2=3k-2, ad=k-2. Its three physical density counterterms are
H1=A1-D1, H2=A2-D2, Hd=-Dd, where
A1=k/(1-k) B_(k,k)(D0,D0) and
A2=k/[2(1-k)] [B_(k,a1)(D0,A1)+B_(a1,k)(A1,D0)].
The ordered angular Green product B is reconstructed below.
Write Hi=cos^2(theta)sin(theta)sum_m q_(i,m)cos(2m theta), and put
Ni=sum_m|q_(i,m)| and Ii=the sin(3theta) coefficient of Hi.
These exact finite real numbers do not depend on T.

The task is to enclose all physical coefficients of H2 and Hd, hence N2,Nd,
|I2|,|Id|. N1<38.37961982 and |I1|<.03893786140 are prior proved bounds105.
This supplies explicit constants in106's weighted factor estimate. Put
omega=(3-k)/2, Jb=1/145860, bmax=2^-16, and

 Ci=L^(k-3)[2^omega Ni + 4 bmax 5^omega |Ii|/((1-ai)Jb)].        (1)

Then for every T>=max(R_b,L,1),

 sup |(rho_T-rho0)/(x^2 y W)|
     <=C1 T^(k-1)+C2 T^(2k-2)+Cd T^(-2),                     (2)
 W=(1+(r/L)^2)^((k-3)/2).

The quotient means its continuous angular extension on the axes, not division
of numerical samples by zero. C1<.334616 is already known. New numerical upper
bounds for C2,Cd must be rigorously rounded before use.

For a compact disk |X|<=R0, 2R0<=T, each velocity component and Cartesian
partial derivative of order j=0,1,2,3 obeys

 sup |partial^alpha U[rho_T-rho0]_ell|
  <=R0^(3-j) sum_i Ki,j T^(ai-3),
 Ki,j=2 Ni m(ai) Sj,
 m(a)=max(1/2,2/(3-a)),
 (S0,S1,S2,S3)=(4/3,44/9,416/27,1312/27).                     (3)

These are component bounds, not Frobenius tensor bounds. In particular the
velocity converges to zero in C3 on each compact disk. If the validated right
sides for j=0,1 at R0=9 and an explicit Tstar>=3000 are both less than1e-8,
then the source-point identity of topic76 gives

 |partial_y F(rho_T,c0)(P)|>3.69e-7

for every admissible T>=Tstar. P is the original trial source with |P|<9;
it need not be a source of the changed velocity. This is explicit-family
nonstationarity, not a neighborhood exclusion. If the finite bounds fail this
threshold, only the computed bounds and (2)-(3) are asserted.

## 2. Reconstruction and full finite angular support

For A=sum_j A_j sin((2j+1)theta) at density exponent a, differentiation and
Poisson inversion give F_n=((a+1-2n)A_(n-1)+(a+1+2n)A_n)/2,
v_n=-2n F_n/[4n^2-(a+1)^2], w_n=(a+1)F_n/[4n^2-(a+1)^2]. The radial and
tangential velocities are r^a sum_n v_n cos(2n theta) and
r^a sum_n w_n sin(2n theta). All denominators used here are positive.
The complete ordered product is

 B_(a,b)(A,B)=b (sum_n v_n cos2n theta) B(theta)
                         +(sum_n w_n sin2n theta) B'(theta).   (4)

It follows directly from U_r partial_r rho+U_theta partial_theta rho/r.
Both orders in A2 are required. To evaluate without a grid, let z=exp(i theta)
and represent 2i A by real Laurent coefficients A_j at +(2j+1), -A_j at the
negative frequency. Vr has coefficients v_n/2 at both signs of2n. The series
2i W has coefficients w_n,-w_n there; B' has (2j+1)B_j/2 at both odd signs.
Thus the real Laurent coefficients of 2i B_(a,b) are exactly those of
b Vr*(2i B)+(2i W)*B'. Ordinary finite convolution computes all of them.

D0 and Dd have maximum odd frequency521. A1 has maximum odd frequency1043.
The two products in A2 therefore have maximum odd frequency1565, giving H2
sine indices0..782. The quotient degree is at most781, as also follows by
factoring (4) through cos^2(theta)sin(theta). There are no omitted angular
tails. Hd's quotient degree is259 and its coefficients are exactly
-R_b^(5-k)A_(m,6). Its I is the negative physical original sine coefficient
(2A06+A16-A26-A36)/8.

For an odd-sine row E of quotient degree at mostM, multiply its Laurent
polynomial by the appropriate monomial. In the variable z^2 the resulting
polynomial has coefficients E_j at positions M+2+j and -E_j at M+1-j.
The identity 2i cos^2(theta)sin(theta)=(z-z^-1)(z+z^-1)^2/4 proves divisibility
by (w-1)(w+1)^2 in w=z^2. Three synthetic divisions by-1,-1,+1 and multiplication
by4 therefore recover the symmetric quotient Laurent polynomial. Its central
coefficient is q0, and twice its positive coefficients are qm for m>0.
A separate implementation may instead use collected exact integer inverse
forms q0=4 sum_(j>=1) c_(j-1) E_j,
qm=8 sum_(j>=m+1)c_(j-m-1)E_j, c_l=(-1)^l(floor(l/2)+1).
These expressions are finite algebraic identities. Dependency inflation is
included by interval arithmetic; a zero-containing division remainder is only
a diagnostic, not proof of divisibility. Divisibility follows analytically
from (4) and the common factor of both inputs.

## 3. Weighted distance

Each individual correction is chi(r/T)r^ai Hi minus its exact compact strain
compensator. Here chi is the fixed106 polynomial transition, its values lie
in[0,1], and b(s)=(s-1)^8(2-s)^8 on[1,2]. The strain integral Ji obeys
0<Ji<=1/(1-ai), while sup b=2^-16 and integral s b(s)ds=Jb. On the tail r>=T,
r^(ai-3)/W = L^(k-3) r^(ai-k)(1+L^2/r^2)^omega.
The first term in(1) follows from T>=L and ai<k. On the compensator support
T<=r<=2T use 1+r^2/L^2<=5T^2/L^2. Multiplying the exact compensator coefficient
4 Ii Ji T^(ai-3)/Jb proves the second term. Summing yields(2).

## 4. Local velocity with exact strain cancellation

For each term separately choose its own exact strain compensator; the sum is
identical to106's compensator. The density is zero on r<T, so its stream there
is harmonic. If Hi=sum h_(i,n)sin((2n+1)theta), direct integration by parts in
the canonical Green formula gives its n-th interior stream, n>=1, as

 (h_(i,n)/2) r^(2n) T^(ai-2n+1)
                  integral_1^infinity chi(s)s^(ai-2n)ds.

The missing lower sine coefficient cancels in the integration by parts. The
boundary term at infinity vanishes since ai<1; chi vanishes at1. The integral
lies in(0,1/(2n-ai-1)]. The compact x^2 y radial compensator has interior
stream only at n=1. Exact strain cancellation removes that entire quadratic
mode. Thus only n>=2 remains. The derivative of order j of either velocity
component has magnitude at most
n |h_(i,n)| (2n-1)_j R0^(2n-1-j) T^(ai-2n+1)/(2n-ai-1).
By its Fourier integral, |h_(i,n)|<=2||Hi||infinity<=2Ni.
For n>=2, n/(2n-ai-1)<=m(ai). The maximum is at n=2 if ai+1>=0,
and its supremum is1/2 if ai+1<0. The latter case applies to a2 and ad;
using only2/(3-ai) there would be an invalid bound. Factoring
R0^(3-j)T^(ai-3), and using R0/T<=1/2, gives the geometric sums
Sj=sum_(m>=0)(2m+3)_j4^-m. Their stated exact rational values follow by
differentiating the geometric series or by polynomial moment sums. This
proves(3) and includes all finitely many angular modes by a convergent
infinite upper bound.

At the original P, the new density and its derivatives agree with rho0.
The original source identity changes by g partial_y u2(P)+g' u1(P),
where g=rho0_y(P) and g'=rho0_xy(P). Topic76 proves
|F_y(rho0,c0)(P)|>6.70197e-7 and |g|+|g'|<30.0230.
Thus if each perturbation jet has magnitude<1e-8 the triangle inequality
gives a lower bound greater than3.69e-7. T exponents ai-3 are negative,
so a bound checked at Tstar holds for all larger T.

## 5. Finite audit and limits

Arb balls and an independently coded iv/exact-integer convolution will form
all Laurent product coefficients, followed by different quotient inversions.
Each must separately supply strict bounds for N2,Nd,I2,Id and the constants
and local jets. The audit checks original dyadics, exact support and Green
signs, all propagated coefficient radii, normalization and predecessor pins,
integer convolution scaling, and the exact rational geometric sums. Neither
coefficient overlap nor sampled residual values proves the theorem.
Actual Opus5.5 review is required before FINAL; availability failures must be
reported. No full residual norm ceiling, inverse, fixed point, meaningful
uncertainty neighborhood of X3 or decisive endpoint is supplied.
