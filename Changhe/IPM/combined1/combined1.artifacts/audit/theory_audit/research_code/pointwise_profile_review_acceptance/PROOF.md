# Acceptance of the pointwise-profile review

## Statement, data and dependencies

Use c=4076476460239181/2251799813685248, q=1/c-4,
delta=1-1/c, D=5c-1 and the exact odd sine polynomials A,P,Theta0
for each of007,013,014 in the registered JSON inputs. For real z set
f_z=z1 A+100000 z2 P and define

 G(z)=sup_theta sqrt(q^2 f_z(theta)^2+f_z'(theta)^2),
 N(z)=sup_theta |V_q[f_z](theta)|.

V_q is the canonical IPM Hessian velocity of the homogeneous potential
r^(q+2) sum_n (f_z)_n sin(n theta)/((q+2)^2-n^2), evaluated at r=1.
It includes the contact term. There is no resonance in the finite odd
mode sets here. For all three data sets the following are confirmed:

 N(z)<=E G(z), E=93/250, for every real z.                 (1)

The optimal constants for this particular angular inequality are at
least0.3714757,0.3714938,0.3715026, respectively. Thus the available
improvements of E are at most0.0005243,0.0005062,0.0004974. These are
bounds for(1), not for every estimate using a stronger stationary
hypothesis or an independently larger lower bound on H_q.

Let h be C1, even in x, odd in y, with

 H_q=max(sup_X(1+|X|)^(-q)|h(X)|,
             sup_X(1+|X|)^(1-q)|grad h(X)|)<infinity,

and assume r^(-q)h(r e_theta) converges uniformly to(A+tP)/(4c).
Then the uniform-limit theorem402/413 gives

 limsup_(r->infinity) sup_theta r^(-q)
 |U[h](r e_theta)+DK(r e_theta)M[h]|<=E H_q.               (2)

Here K is the canonical IPM velocity kernel and M[h]=integral Xh(X)dX
is the absolutely convergent first moment. The kernel and compensation
are those of the frozen402 theorem; no alternative gauge is introduced.

T4-415 proves the reduction and has its own61440-rectangle certificate.
The frozen independent review ee7b1b1b7d9bc92c2fba61324c25b39aa4178c75a42296bbe7b444c8959671e8
reconstructs its algebra, reproduces all saved cells and supplies a
second certificate. The present argument checks that second certificate
and its new lower bounds using the already accepted exact angular
algebra. T4-422 supplies the conditional radial-cap consequence, whose
inputs and displayed enclosures are independently recomputed below.

## Proof of the independent certificate

Homogeneity reduces z to(cos alpha,sin alpha), -pi/2<=alpha<=pi/2.
Both quadratic forms have only even cosine degrees in the physical
angle, so reflection and period pi reduce theta to[0,pi/2]. Put
Q_ij(phi)=q^2 f_i(phi)f_j(phi)+f_i'(phi)f_j'(phi) and
F_ij(theta)=V_q[f_i](theta) dot V_q[f_j](theta). For any fixed witness
phi, G(z)^2>=z^TQ(phi)z.

A symmetric quadratic form is t(alpha)=a+b cos(2alpha)+d sin(2alpha).
On a closed phase arc of length less than pi, there is at most one
critical point unless the form is constant. If an interior minimum
occurs, the derivative at the left end is negative and that at the
right end is positive. Consequently if the left derivative is strictly
positive or the right derivative is strictly negative, both endpoints
bound the minimum. Otherwise the global bound a-sqrt(b^2+d^2) is valid.
At a zero derivative or an interval-arithmetic ambiguity the latter
bound is used. This proves the review's arc-minimum rule without a
heuristic search.

For a theta cell centered at theta_j with halfwidth k, Taylor's theorem
gives, for every alpha in its chosen arc,

 z^TF(theta)z<=z^TF(theta_j)z
       +(theta-theta_j)z^TF'(theta_j)z
       +(k^2/2)max(0,sup_(alpha,xi) z^TF''(xi)z).

For the linear term the worst value on[-k,k] is one of its two
endpoints. Apply the proved arc rule to each of
E^2Q(phi)-F(theta_j)-s k F'(theta_j), s=+1,-1, and subtract the displayed
second-order bound. A positive result on all cells proves(1).

The supplied certificate contains17 projective arcs per reference,
with exact rational endpoints covering[-1/2,1/2] in alpha/pi. Each uses
1536 equal theta cells, giving78336 rectangles over the three references.
The selected witnesses have phi=d*pi/(2*1536), with integer indices.
Coverage, strict positive margins and all degrees are checked in exact
rational arithmetic and Arb. The positive margins prove(1) independently
of the FLOAT procedure that selected the witnesses.

For(2), set g_R(X)=R^(-q)h(RX). The weighted derivative bound gives
|grad g_R(X)|<=H_q|X|^(q-1). Uniform convergence on compact annuli
therefore gives the same pointwise gradient bound for its smooth limit.
At |X|=1 this is G(1,t/100000)/(4c)<=H_q. Combine with(1) and the
uniform compensated-velocity limit from402/413. No convergence of
rescaled gradients is assumed. This argument supplies no finite radius.

## Lower bounds on the optimal angular coefficient

For each frozen rational w and theta0 take z=(1,w). Then
N(z)>=sqrt(z^TF(theta0)z). The denominator squared is the even cosine
polynomial D_z(theta)=q^2 f_z(theta)^2+f_z'(theta)^2. Divide[0,pi/2]
into8192 cells. If their center is m and halfwidth h, then

 D_z(theta)<=D_z(m)+h|D_z'(m)|
                   +(h^2/2) sum_n n^2 |(D_z)_n|.

The largest directed upper bound over all cells is an upper bound
for G(z)^2. Dividing the positive point numerator by its square root
proves the three stated lower coefficients. This is a global angular
upper bound for the denominator, not a sampled maximum.

The review's sentence that any remainder estimate must start from
these coefficients needs this angular-comparison scope. For an actual
stationary correction, a restricted value of t or a stronger estimate
of H_q could permit a different comparison. No such estimate is proved
here. The lower bounds do not constrain all possible stationary proofs.

## Radial-cap consequence and the current remainder

Let B=dist_L2(A,span(P))/(4c), g0=Theta0'(0), alpha0=-2q-2 and
S=2 delta^2/[alpha0(alpha0+delta)(alpha0+2delta)]. Let H0 be the
certified integer lower bound on H_q in the exact parameters. With
V>=0 and the optimistic assumptions of zero remaining error and an
available coefficient E throughout the exterior, define

 r0=[sqrt(2pi) H0 (V+E g0)/(D B)]^(1/delta),
 cap=B r0^(q+1) sqrt(S).                                  (3)

Integrating[B-B(r0/r)^delta]_+^2 r^(2q+1) over r proves cap^2:
a direct expansion gives S=1/alpha0-2/(alpha0+delta)+1/(alpha0+2delta).
Thus(3) is an upper bound on this particular CI certificate even under
these optimistic assumptions. For each target beta its critical E is

 Ecrit=D B/[sqrt(2pi) H0 g0]
           *[B sqrt(S)/beta]^(delta/(-q-1))-V/g0.           (4)

Equations(3)-(4) are recomputed with V=0 and with the optimistic value
V=v0=|U_lead(0)|. If only V>=v0 is proved, using equality gives an
upper bound on what this certificate could reach, not a verified upper
bound on the actual background velocity. All enclosures and flags in
T4-422 and the peer review are checked against these formulas. The
three scalar targets lie below cap and the graded target above cap.
This is necessary arithmetic, not a sufficient existence certificate.

With the present two-weight tail list, the audited421 argument gives
J(R)/H>=Sigma(5/r_beta)^delta for L0<=R<=r_beta, with
Sigma=1/2+2^(3-q)+2^(1-q)+2^(2-q)/(q+5),
r_beta=[B/(beta sqrt(alpha0))]^(1/(-q-1)). Compare this lower bound
with the positive room Ecrit(Phi)-E, where Phi is the audited pointwise
lower bound for H. The review's lower factors46.06 at sharpw,66.54
at TB and22.19 at the fixed ball are verified, and the graded room
is negative. For larger starting radii and radius-dependent choices,
the radial-average theorem425/432 supplies the obstruction. It uses
the actual Green average, not a pointwise substitution. This confirms
the correction of the review of T4-414 section4 made in the new review.

## Provenance and verdict

The restored the review of T4-414 has the announced intact hash
221b113543dc815315d771563c9c0b9618919663db794720f55887169221ab51.
The review correctly distinguishes the initial E=3/8 trial launch from
the final E=93/250 computation. The final saved result includes its
actual UTC and source hashes; no separate historical launch file or
log for that final invocation is asserted. The independent replay is
new validation, not a replacement invented historical log.

The 256-bit recalculation of the original certificate has slightly
different directed lower bounds from its192-bit version. The review's
comparison uses tolerance1e-8, not equality or interval overlap; its
printed 'equal' wording must be read as agreement within that tolerance.
Each set of lower bounds is positive on its own. This acceptance uses
no tolerance to decide validity of any rectangle or inequality.

Verdict: CONFIRMED(1),(2), the conditional cap calculation and the
specified remainder obstruction. T4-415 and T4-422 become AUDITED upon
success of the finite checks. The lower-coefficient claim is confirmed
for(1) with the scope above. No inverse, finite-radius remainder,
stationary H_q upper bound, candidate status change or existence proof
follows. The peer script is retained as text and not executed here.
