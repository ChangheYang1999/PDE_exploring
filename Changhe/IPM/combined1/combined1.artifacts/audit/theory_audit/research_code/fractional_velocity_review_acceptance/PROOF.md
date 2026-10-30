# Independent acceptance of the full fractional-ball obstruction

## Exact statement and dependencies

Let -5<q<-3, a=-q, 0<s<2 and w1,w2>0. Put

 omega(X)=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2),
 X_(s,w)(h)^2=||omega D2 J^s h||2^2
              +w1||D J^s h||2^2+w2||J^s h||2^2.

Dk is the complete ordered Cartesian tensor. The space is the completion
of real compact smooth S1 functions, with S1 meaning even in x and odd
in y. Define H_q(h) as the maximum of sup(1+r)^a|h| and
sup(1+r)^(a+1)|grad h|. The canonical velocity is
U[h]=(partial_xy,-partial_xx)Delta^(-1)h, including its contact term.
Let K be its nonlocal kernel, M[h]=integral Xh(X)dX and
c[h]=partial_y U2[h](0).

Fix rho,beta,R0>0. If a universal E satisfies

 |U[h](X)+DK(X)M[h]| <= E H_q(h)|X|^q, |X|>=R0,

for every smooth real S1 h in that completion with finite H_q,
absolute first moment, c[h]=0, X_(s,w)(h)<=rho and ||h||2<=beta,
then E>=(a-1)/(2a(a-3)). The same assertion holds after additionally
requiring any prescribed H_q(h)=Hstar>0. This is the full statement
of T4-397. Its original standalone proof is frozen in source/proposal.md.
The independent Opus theory-lane review is source/review.md, R1-042.

## Complete argument and the reviewed points

Put alpha=2-s. The positive convolution kernel of J^(-alpha) is

 G_alpha(Z)=1/Gamma(alpha/2) integral_0^infinity
 t^(alpha/2-1)e^(-t)(4pi t)^(-1)exp(-|Z|^2/(4t))dt.

Its mass is one. The inequality
omega(X)<=2^(2/5)omega(Y)omega(X-Y), together with the Gaussian
4/5 moment, gives

 ||omega J^(-alpha)g||2 <= C_s||omega g||2,
 C_s=2^(2/5)[1+16^(2/5)Gamma(7/5)
                   Gamma(alpha/2+2/5)/Gamma(alpha/2)].

This bound applies directly to every g in the indicated weighted L2
space by Minkowski. Since weighted L2 is contained in L2, Fourier
multipliers also define the same distribution. Consequently, for any
smooth f with the indicated derivatives in weighted L2,
J^s f=J^(-alpha)(f-Delta f) holds in distributions and in the resulting
L2 spaces. The trace contraction has norm sqrt(2), hence

 ||omega D2 J^s f||2 <= C_s(||omega D2 f||2+sqrt(2)||omega D4 f||2),
 ||D J^s f||2 <= ||Df||2+sqrt(2)||D3 f||2,
 ||J^s f||2 <= ||f||2+sqrt(2)||D2 f||2.

This justifies the bounds on noncompact functions without assuming
membership in the completion first, and resolves review remark R1.

Use f_R=y(R^2+r^2)^(-(a+1)/2)/a and
k_R=f_R-R^(-a-1)b/a, where b=y eta(r^2),
eta(t)=exp(1-1/(1-t)) for t<1 and eta=0 otherwise.
The weighted derivative integrals of f_1 through order4 are finite.
Scaling f_R=R^(-a)f_1(X/R) and
omega(RY)<=R^(4/5)omega(Y) give a finite explicitly defined
D_(s,w,a), the derivative-integral expression in the original proof,
such that

 X_(s,w)(k_R)<=D_(s,w,a)R^(1-a)+X_(s,w)(b)R^(-a-1)/a ->0.

Its L2 norm also tends to zero. Compact smooth radial cutoffs converge
in all those integer weighted derivative norms by Leibniz and tail
integrability, and therefore converge in X_(s,w) by the displayed
inequalities. This proves the specified completion membership.

Each k_R is a pure first sine mode. For g=F(r)sin(theta), the regular
Poisson solution has near-origin non-harmonic term F'(0)r^3 sin(theta)/8.
Its harmonic linear term has zero Hessian velocity. Therefore
c[g]=-F'(0)/4 and c[k_R]=0 exactly. This identity is asserted only
for the first sine mode. A general S1 function also has a nonlocal
third-sine contribution to c[h], which is not being dropped here.
This resolves R2. The weighted radial and angular gradient estimates
give

 1<=H_q(k_R)<=(1+R^-2)^((a+1)/2)+5*2^(a+1)R^(-a-1)/a ->1.

The first absolute moment is finite because a>3. The canonical radial
Green formula, after compensating its full dipole, gives the limiting
velocity along theta=pi/4 of magnitude

 lim_(r->infinity) r^(-q)|U[k_R]+DK M[k_R]|
   =(a-1)/(2a(a-3)).

Indeed the leading potential is r^(q+2)sin(theta)/(a(q+1)(q+3));
the remaining potential has two differentiated bounds giving velocity
O_R(r^(q-2)). The compact first-sine subtraction contributes exactly
its dipole outside r=1. Apply the proposed universal estimate for each
large R, first take r to infinity and then R to infinity, to obtain
the lower bound for E. If Hstar is prescribed, multiply k_R by
Hstar/H_q(k_R); those factors tend to Hstar, so both smallness bounds
still tend to zero and the velocity ratio is unchanged.

The notation D_(s,w,a) above denotes the derivative-integral scaling
constant, and is distinct from the endpoint transport denominator
1-c(q-delta). This resolves R3 without changing any formula.

## Evidence, verdict and limits

CONFIRMED: R1-042 accepts all analytic sections of T4-397. T4-397 is
now AUDITED. The review independently checked nineteen exact symbolic
identities and three Arb calculations. Its C_s interval at s=1/5184
contains the value 4.468299565794177304409883, consistent with the
original finite check. Its two FLOAT quadrature diagnostics are not
certificates and are unnecessary for the limiting proof.

In particular the review's R=512 membership and numerical D and X(b)
values are FLOAT only. They use numerical quadrature and do not include
a certified quadrature-error and infinite-tail enclosure. No finite-R
membership, lower E for that particular R, or new stationary estimate
is accepted from those diagnostics. The exact limiting theorem is
unaffected. No review checker was executed by this acceptance.

This theorem rules out lowering a universal velocity coefficient by
only adding these fractional, L2, normalization and H_q restrictions.
It does not rule out a sharper estimate on solutions of the stationary
equation, on a restricted tail subspace, or under additional quantitative
hypotheses. It proves no inverse, existence result or new candidate
exclusion. Model collaboration used the existing independent theory
lane configured for Claude Opus5.5; provider identity is not independently
observable from these files.
