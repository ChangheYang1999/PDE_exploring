# Acceptance of the smooth normalized velocity obstruction

## Exact statement

Let -5<q<-3, a=-q, and define

 H_q(h)=max(sup (1+|X|)^a |h(X)|,
            sup (1+|X|)^(a+1)|grad h(X)|).

Let U[h]=(psi_xy,-psi_xx), Delta psi=h, be the canonical velocity.
Let M[h]=integral X h(X) dX and c[h]=partial_y U2[h](0).
For every beta>0 and R0>0, suppose E satisfies

 |U[h](X)+DK(X)M[h]|<=E H_q(h)|X|^q, |X|>=R0,

for all real smooth S1 functions h with finite H_q, finite first
absolute moment, c[h]=0 and ||h||2<=beta. Then

 E >= (a-1)/(2a(a-3)).

S1 means even in x and odd in y. K is the canonical homogeneous
Biot-Savart kernel, with its sign fixed by U as above. This accepts
T4-384 on exactly its stated domain. The same lower bound holds if
the L2 restriction is omitted. No stationarity assumption is used.

## Complete argument checked against the independent review

For R>=1, set f_R=y(R^2+r^2)^(-(a+1)/2)/a. Let
eta(s)=exp(1-1/(1-s)) for 0<=s<1 and zero for s>=1, and
b=y eta(r^2). Both functions are smooth and S1. They are first sine
modes. For any such smooth mode g=F(r)sin(theta), solving the radial
Poisson equation near zero gives

 psi=A1 y+F'(0) r^2 y/8+O(r^5),
 c[g]=-psi_xxy(0)=-F'(0)/4.

This recovers the local contact term. In the full strain formula,
the sin(3theta) principal-value term vanishes on each annulus for a
first sine mode. Hence c[f_R]=-R^(-a-1)/(4a), c[b]=-1/4, and

 k_R=f_R-R^(-a-1)b/a

has exactly c[k_R]=0. Finite first absolute moments require a>3,
which is part of the hypothesis. The stronger smoothness at the
origin avoids any trace ambiguity.

The polar gradient components of f_R are

 (R^2-a r^2)(R^2+r^2)^(-(a+3)/2)sin(theta)/a,
 (R^2+r^2)^(-(a+1)/2)cos(theta)/a.

Their norm is bounded by (R^2+r^2)^(-(a+1)/2), using the convex
combination of the two squared component bounds, not their sum.
Cauchy-Schwarz gives (1+r)/sqrt(R^2+r^2)<=sqrt(1+R^-2).
The amplitude bound is smaller. Since |grad b|<5 and b is supported
in the unit disk, H_q(b)<=5*2^(a+1). Therefore

 1<=H_q(k_R)<=(1+R^-2)^((a+1)/2)+R^(-a-1)5*2^(a+1)/a.

The lower bound follows from the weighted gradient limit on the
positive y-axis. Thus H_q(k_R) tends to1. Scaling gives
||f_R||2=R^(1-a)||f_1||2 and the compact subtraction also tends to
zero in L2, so every fixed positive beta admits all large R.

For a first sine density F(r)sin(theta), the canonical potential is

 -sin(theta)/2 [r^-1 integral_0^r s^2F(s)ds
                         +r integral_r^infinity F(s)ds].

For F=r(R^2+r^2)^(-(a+1)/2)/a, subtracting the complete moment from
the first integral leaves the leading homogeneous potential
r^(q+2)sin(theta)/(a(q+1)(q+3)), with remainder O_R(r^q).
Its first two derivatives have the corresponding differentiated
bounds: writing T=integral_r^infinity s^2F(s)ds and J=integral_r^infinity F(s)ds,
the radial remainder coefficient is (T/r-rJ)/2, with derivatives
-(T/r^2+J)/2 and T/r^3+F. No uncontrolled remainder is differentiated.
The compact first sine b contributes exactly its dipole outside the
unit disk. Thus it does not change U[k_R]+DK M[k_R] there.
The homogeneous Hessian velocity divided by r^q is

 (cos(theta)[1+(q-1)sin(theta)^2],
  -sin(theta)[1+(q-1)cos(theta)^2])/(a(q+3)).

At theta=pi/4 its norm is (a-1)/(2a(a-3)). Apply the assumed
inequality to k_R and let r tend to infinity first, then R tend to
infinity. The asserted lower bound follows.

## Review evidence and repairs

The frozen T2 review confirms the preceding proof and independently
checks the contact identity by the local ODE, kernel integration by
parts and two Gaussian Fourier integrals. Its code has12 exact
checks for381 and21 for384, plus the Fourier values -1/4 and -1/8.
Its Arb calculations agree with the earlier independent T4 results.
The code's FLOAT diagnostics are not part of this acceptance. The
review also independently confirms381's retained-delta cap, already
AUDITED through391.

Two presentation corrections are required, without changing the
review's theorem verdict. Section1(d)'s first sentence says that
|X|f_R is integrable since a>2; the sufficient and exact tail condition
here is a>3. Also, several decimal tables are nearest-rounded, not
outward bounds. For example013's delta cap at v0=0 is
1.42080023828412...e-7, strictly greater than the printed1.420800e-7;
014's v0>0 radius is21220.6119998838..., strictly below21220.612.
The normalized-sequence H upper at R=10000 is1.00000002223805...,
strictly greater than the printed1.00000002. Label those displays as
approximate or round outward. The full stored intervals and the
conservative common caps1.421e-7 and1.124e-7 remain correct.

The input375 hash is printed and captured in the source manifest;
the checker does not assert that particular hash despite the review's
wording. Its exact angle is compared to381's source parameter and
the full accepted computation remains bound to frozen source bytes.
No claim here depends on the FLOAT conversions of Arb endpoints.

## Verdict and scope

CONFIRMED: T4-384 is now AUDITED through this acceptance. T4-381 also
has a second independent review. The numerical and integrability
wording repairs above concern the review, not either theorem. The
bound applies to any fixed starting radius and arbitrarily small
L2 balls with exact normalization. Whether stationarity or a full
fractional X ball permits a better estimate is not answered by384.
No inverse, weighted stationary budget, existence result or new
candidate exclusion is inferred. No foreign code was executed.
