# Whole-plane Sobolev control of the moving source

This is an independent reconstruction of the lead's V34. At proof writing
its numerical enclosures are to be checked. All conclusions concern the
specified exact modal trial and whole-plane Sobolev perturbations. There
is no asserted global inverse, Newton radius or decisive IPM endpoint.

## 1. Exact setting and imported results

Use the unitary Fourier transform
hhat(xi)=(2pi)^(-1) integral exp(-i X.xi)h(X)dX on R2 and
||h||Hs^2=integral (1+|xi|^2)^s |hhat(xi)|^2 dxi. Vector norms are
Euclidean and all derivative tensor norms are Frobenius, including all
ordered pairs of derivative indices. Fix a real h in Hs, s>3, even in x
and odd in y. Define the canonical perturbation velocity and raw strain by

 Uhat[h]=(xi1 xi2,-xi1^2)hhat/|xi|^2,
 sigma[h]=(2pi)^(-1) integral -i xi1^2 xi2 hhat/|xi|^2 dxi,
 W[h](X)=U[h](X)+sigma[h] X/3.                         (1)

The value of the multiplier at frequency0 is irrelevant. Absolute
convergence of the strain and differentiated velocity integrals follows
below. Formula(1) uses -Delta psi=partial_x h, U=(-psi_y,psi_x) and
sigma=psi_xy(0)=-partial_x U1(0)=partial_y U2(0). It fixes the harmonic
ambiguity; the affine term is the physical strain correction, not an
additional permitted harmonic velocity.

Let rho0 be the exact normalized modal_v2 trial of topic94. Its canonical
velocity V0 has one source P=(p,0) in the verified bracket

 4841405518533377/2^49 < p < 4841405518533711/2^49
 and 8.6 < p < 8.60006381.

On B_R0(P), R0=99/2000, the verified bounds are
MV=743/2500 for ||D^2 V0||F and Mrho=5059/10000 for
||D^2 rho0||F. Both may be used as strict upper bounds. Put
A0=partial_x V0_1(P), mu0=partial_y V0_2(P), G0=partial_y rho0(P).
Topic94 provides

 A0 in[10.150725243,10.150725244],
 |mu0-1+2.2528046115e-8|<4.7e-19,
 |G0-29.7494906633335090153|<9.2e-20.                   (2)

The trial is C6 on this source disc. For 0<R<R0, I=[p-R,p+R], let
m=A0-MV R. In particular m>m0=10.1360138. Set

 e0=sup_I|W1|, e1=sup_I|partial_x W1|,
 e2=sup_I|partial_y W2|, e3=sup_I|h_y|,
 m2=sup_(B_R0(P))||D^2 W||F.                           (3)

Dependencies are the frozen exact source and Hessian data in topic94,
the order-s local estimate in topic92, and its rough-coefficient and
graph-completion extension in topic100. Their verdict pins must be checked.
We restate the source-motion argument to make its use transparent.

On I, the fundamental theorem gives w'=partial_x V0_1>=m>0 and
|w(x)|>=m|x-p|, where w(p)=0. If e0<mR, endpoint signs give a zero p_h
of w+W1 in I, and every zero satisfies d=|p_h-p|<=e0/m. If e1<m,
then w'+partial_x W1>0 and the zero is unique. Parity gives V2(x,0)=0
and zero off-diagonal derivatives on the axis, so P_h=(p_h,0) is an
equilibrium with diagonal DV. Since div U=0,

 A_h+mu_h=2/k+2sigma[h]/3,
 |mu_h-mu0|<=MV e0/m+e2,
 |partial_y rho0(P_h)-G0|<=Mrho e0/m.                  (4)

The background in the transported linear estimate is rho0. For the
nonlinear perturbed density rho0+h, add e3 to the last bound. The safe
sufficient source-box inequalities from topic94 are

 B1=MV e0/m+e2<=0.0099999,
 B2=2|sigma[h]|/3+MV e0/m+e2<=0.0492747,
 B3=Mrho e0/m<=0.2505.                                (5)

They imply A_h in[10,10.2], mu_h in[0.99,1.01] and
partial_y rho0(P_h) in[29,30]. They are deliberately conservative
relative to the exact margins in(2).

## 2. Fourier estimates with angular constants

For every s>3 define

 CU=[32pi(s-1)]^(-1/2),
 Csigma=[64pi(s-1)(s-2)]^(-1/2),
 Cy=[8pi(s-1)(s-2)]^(-1/2),
 CH=[4pi(s-1)(s-2)(s-3)]^(-1/2).                       (6)

Then U is in Hs(R2;R2), ||U||Hs<=||h||Hs, and U has continuous
bounded second derivatives. The following bounds hold globally:

 sup|U1|<=CU||h||Hs,
 |sigma[h]|, sup|partial_x U1|, sup|partial_y U2|<=Csigma||h||Hs,
 sup|h_y|<=Cy||h||Hs,
 sup||D^2 U||F<=CH||h||Hs.                             (7)

Proof. The squared vector multiplier in(1) is xi1^2/|xi|^2<=1,
which proves the vector Sobolev bound directly, not by adding separate
component estimates. Write xi=r(cos theta,sin theta). Each quantity in(7)
has symbol modulus r^j omega(theta). Its norm after Fourier inversion
is bounded by the integral of that modulus times |hhat|, including the
tensor norm in the Hessian case. Cauchy-Schwarz gives the constant

 (2pi)^(-1)[integral r^(2j) omega(theta)^2(1+r^2)^(-s) dxi]^(1/2). (8)

The cases (j, average omega^2) are (0,1/8) for U1, (1,1/16) for
sigma and both displayed derivatives, (1,1/2) for h_y, and (2,1/2)
for the complete Hessian tensor. For the last claim, the squared
multiplier tensor is sum_(i,j,k)|xi_j xi_k v_i|^2
=r^4|v|^2=r^4 cos(theta)^2, with v the vector multiplier in(1).
The angular averages follow, for nonnegative integers a,b, from

 average(cos^(2a)theta sin^(2b)theta)
 =(2a)!(2b)!/[4^(a+b) a! b! (a+b)!].                   (9)

For completeness, integrating a derivative of cos^(2a-1)theta
sin^(2b+1)theta over a period yields the usual reduction in a and b;
together with average1=1 and symmetry, that recurrence gives(9).

Substitute u=r^2. Repeated integration by parts, with vanishing endpoint
terms when s>j+1, gives

 2pi integral_0^infty r^(2j+1)(1+r^2)^(-s) dr
 =pi j!/[(s-1)(s-2)...(s-j-1)].                        (10)

Thus(8) gives exactly(6). The weighted symbol integrals are finite for
s>3, so hhat and the velocity Fourier derivatives through order2 are
integrable. Dominated convergence in Fourier inversion proves continuity;
the distributional derivatives agree with these integrals. This also
proves the claimed regularity of h. No parity hypothesis is needed for
(7), but parity is needed for the source interpretation of(4).

## 3. Explicit uniform source hypotheses at s=153/50

Let H=||h||H^(153/50), xmax=8.64956381 and R=49/1000. Since R<R0
and p has the strict upper bound above, |x|<xmax on I. Equations(1),(7)
give, with c0=CU+xmax Csigma/3 and c1=4Csigma/3,

 e0<=c0 H, e1,e2<=c1 H, e3<=Cy H, m2<=CH H.            (11)

The affine field has zero Hessian. It need not belong to whole-plane Hs;
its restriction near the source does. Define

 b1=MV c0/m0+c1, b2=b1+2Csigma/3, b3=Mrho c0/m0.       (12)

Then B1<=b1 H, B2<=b2 H and B3<=b3 H. The following outward
ceilings are to be certified independently by Arb and rational arithmetic:

 CU<0.06948907, Csigma<0.04772529, Cy<0.13498750,
 CH<0.77935065, c0<0.20709004, c1<0.06363372,
 b1<0.06970585, b2<0.10152270, b3<0.01033610.            (13)

For H<=7/50, these and direct evaluation of the unrounded formulas give

 B1<0.00975882, B2<0.01421318, B3<0.00144706,
 B3+e3<0.02034531, e0<0.02899261, e1<0.00890872,
 m2<0.10910910, e0/m<0.00286036,
 mR>0.4966646, delta_h=(R0-d)/3>0.01554654.             (14)

Consequently e0<mR and e1<m, so the equilibrium exists uniquely in I,
and all of(5) hold. The unrounded B1 sufficient-radius threshold exceeds
0.14345856. The smaller round radius7/50 is used throughout.
The correct scale relation is 0<delta_h<=33/2000. Equality occurs for
h=0, and more generally whenever the source does not move. The lead's
strict inequality delta_h<33/2000 is therefore not universally valid.
It is not needed for the numerical bound or open-disc inclusion.

## 4. Uniform local forcing coefficient, with explicit scope

Let V=V0+W[h] and use background rho0. For any 0<delta'<=delta_h,
B_(3delta')(P_h) is contained in B_R0(P): each point in the first open
ball has distance strictly less than3delta'+d<=R0 from P. Moreover
p_h>p-R0>8.55 and3delta'<=R0<p_h/2, and delta'<1. Choose the
translated and scaled cutoffs of topics92,94 with
Ctheta=delta'||grad theta||infinity<=2. Parity and(5) supply the
source A,mu,g box. The density is C5 there. The velocity is the sum of
a C4 field and a local Hs field, with s=153/50>3, so topic100 applies.
Its explicit cutoff error may be bounded using the constant divergence

 div V=2/k+2sigma[h]/3=A_h+mu_h.                       (15)

The coefficient in the order-s source estimate is

 E<=((12s+9/2)(MV+m2)+3Mrho)delta',
 kappa(s)=1301/200-(101/100)s=3.4144,
 K1=1/(kappa-E).                                      (16)

Evaluating the larger scale33/2000 and m2=CH(7/50) gives
E<0.30138506 and K1<0.32123200. These ceilings hold uniformly for
all such h and every permitted smaller cutoff scale. The function u
estimated by this local inequality is distinct from the coefficient
correction h. Its admissible completion is exactly the one in topic100;
in particular it contains whole-plane Hs functions with u(0)=grad u(0)=0
and a localized L u in Hs on a neighbourhood of the cutoff support.
No jet condition on the coefficient correction h is required here.

Only K1 and its geometric and source-box hypotheses have been made
uniform. The other local coefficients, the norms centred at P_h, the
auxiliary inverse bound, strain denominator, physical inverse, outer
matching and nonlinear estimates have not been made uniform. No embedding
from a proposed weighted correction norm to this whole-plane Hs norm is
proved by this result.

## 5. A narrow non-stationarity corollary about the trial

If H<=3.2318e-7, no rho=rho0+h with the law(1) solves
V[rho].grad rho=rho classically on a neighbourhood of P_h.
This is not an exclusion ball about X3.

Proof. Equations(11)-(14) supply a source and e3<29. The mean value
bound gives

 |partial_y rho(P_h)-G0|<=Mrho R0+e3<G0,

where(2) verifies the strict last inequality. Thus g_h=partial_y rho(P_h)
is nonzero. Both rho and V are differentiable at P_h; parity gives
rho(P_h)=0 and grad rho(P_h)=(0,g_h), and V(P_h)=0. Along P_h+t e2,

 V.grad rho=t mu_h g_h+o(t), rho=t g_h+o(t).

Stationarity would force mu_h=1. Equations(2),(4) then imply

 MV e0/m+e2 >=1-mu0 > 2.2528046e-8.                    (17)

But(12) bounds the same left side by b1 H. Independent directed
checks give b1(3.2318e-7)<2.25276e-8<2.2528046e-8, a contradiction.
The sufficient H-radius threshold
(2.2528046e-8-4.7e-19)/b1 is greater than3.23187352e-7; the
strictly smaller round radius in the statement is used. This proof needs
only the source data and elementary Sobolev bounds, not the rough local
inverse or graph-completion theorem.

The trial is distinct from X3, and X3-rho0 has not been shown to belong
to whole-plane Hs with a certified norm. Comparing this Hs radius with
a residual supremum, or with fitting errors measured in other norms,
does not establish containment or noncontainment of any numerical
uncertainty ball. No decisive endpoint can be inferred from(17).

## 6. Independent arithmetic criterion

All scalar inputs and decimal claims are exact rational JSON data.
One checker evaluates(6),(11),(12),(14),(16),(17) with Arb balls.
A second constructs an exact rational bracket for pi using
pi=16 arctan(1/5)-4 arctan(1/239), the alternating series with its
first omitted term, and square-root brackets obtained by integer square
roots after exact dyadic scaling. No floating arithmetic enters the
second construction. Every lower and upper published bound must pass
both methods separately. Overlap alone is insufficient.

The pi identity follows from tan(2 arctan(1/5))=5/12 and
tan(4 arctan(1/5))=120/119, hence
 tan(4 arctan(1/5)-arctan(1/239))=1.
The angle lies in(0,pi/2), so it equals pi/4. The alternating series
bound follows from decreasing positive terms. For q>0 and integer B,
L=isqrt(floor(q 2^(2B))) satisfies L/2^B<=sqrt(q)<(L+1)/2^B,
which proves the directed rational square-root construction.
