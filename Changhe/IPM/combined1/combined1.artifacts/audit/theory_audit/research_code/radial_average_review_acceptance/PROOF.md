# Radial averaging does not rescue the current two-weight remainder

Status: independently audited through T1 R1-045, accepted here. The informal proof
is written before the checker. This statement bounds a specified error
majorant. It is not a lower bound on the velocity of a solution and does
not prove nonexistence.

## 1. Exact setting and allowed majorants

Use the canonical S1 stationary setting of T4-335, including the full
contact term in U, the same fixed c and leading angular data, and

 c=4076476460239181/2251799813685248,
 gamma=1/c, q=gamma-4, delta=1-gamma,
 kappa=1-q=5-gamma=4+delta, D=c kappa=5c-1.

Let h be a real C1 S1 correction with finite H=H_q(h)>0, where

 H_q(h)=max(sup_X(1+|X|)^(-q)|h(X)|,
             sup_X(1+|X|)^(1-q)|grad h(X)|).

Assume the full reference and stationarity hypotheses of T4-335,
including the quantitative bounds on its residual and gradient errors.
In particular the reference gradient bound is G r^(gamma-1), G>=g0>0.
The endpoint angular data A,P,Theta0 are the exact copied data for one
of007,013,014. Put

 b=(A+tP)/(4c), t=m/pi, m=integral y h(x,y)dxdy,
 B=dist_L2(0,2pi)(A,span(P))/(4c),
 Phi=|q(AP'-A'P)|/[4c sqrt(q^2 P^2+(P')^2)] at theta_star,
 g0=Theta0'(0), alpha=-2q-2.

The chosen rational theta_star is stored in data/parameters.json.
T4-380 gives H>=Phi>0 for every value of the moment t. The exact sine
projection gives ||b||_L2>=B>0.

Use the tail list of T4-335(7), containing a strictly positive term
C_delta r^(q-delta). This is an explicit hypothesis on the list used
in T4-410; for the present list C_delta=H(V+E G)/D>0. It restricts
any exponent chosen in410 to0<epsilon<=delta. Let R0>=2, L0=2R0,
a=q-epsilon, and use the explicit amplitude and remainder from410:

 A410>=H(1+L0)^epsilon,
 J(s)=A410 s^(-epsilon)[C_a+L_a(1+log_+(k s^epsilon))],
 C_a=1/2+2^(3-a)+2^(a+2)/(-a)
                   +2^(-a-2)/(-a-3)+2^(2-a)/(a+5),
 L_a=2^(1-a), k>=0.

The normalized velocity coefficient furnished by410 is

 E410(s)=Eprof+J(s)/H+(B_b/H)(L0/s)^(q+5), s>=L0,

where Eprof,B_b>=0. The quantities and their proofs are fully specified
in the frozen source/two_weight_PROOF.md. In particular this is a
majorant for |U[h]+DK M[h]|/(H s^q), not for the uncompensated velocity.

One may instead, or at selected radii, use any constant Eu whose
universal compensated-velocity inequality is valid for the entire
S1 norm class, possibly with the fractional, L2, strain-normalization
and prescribed H restrictions of T4-397/409. No extra stationary or
angular-tail restriction is allowed when calling Eu universal here.
The audited universal theorem then requires

 Eu>=Emin=(-q-1)/[2(-q)(-q-3)].                              (1)

An allowed coefficient E(s) is any measurable coefficient selected
from these E410 estimates, their uniform envelopes, and such universal
constants, or any coefficient no smaller than their pointwise infimum.
Below the validity radius of a410 estimate, that estimate is unavailable.
Different410 choices of R0,epsilon may be used at different radii.
No independently stronger, tail-restricted or stationary-only velocity
estimate is included in this class.

## 2. Uniform lower envelope of the chosen coefficients

Set lambda=1/2+5*2^(1-q). Since a<=q and all omitted terms are positive,

 C_a+L_a>=1/2+2^(3-q)+2^(1-q)=lambda.

For every s>=max(L0,5),

 J(s)/H>=lambda[(1+L0)/s]^epsilon
        >=lambda(5/s)^delta.                               (2)

To check the last step, if the first base is at least1 its power is
at least1; otherwise its base is at least5/s and epsilon<=delta.
For L0<=s<=5 the same expression is at least lambda, since1+L0>=5.
The exact arithmetic check below proves lambda>Emin. Consequently
all the allowed choices in section1 satisfy, for s>=2,

 E(s)>=e_min(s)=min(Emin,lambda(5/s)^delta).                 (3)

For s<5, the right side is Emin<lambda. This avoids extending(2)
outside its valid range. A uniform envelope of410 is no smaller than
its own pointwise coefficient, so it also satisfies(3). Taking infima
across different admissible parameter choices preserves this common
lower envelope. Below their validity radii only universal estimates
are among the stated choices, and(1) applies. This proves(3) with all
validity radii accounted for.

## 3. The correct radial averaging operator

For the compensated-velocity contribution to U[h].grad reference,
the forcing majorant at radius s is HG E(s) s^(q+gamma-1). Integrating
the stationary radial equation for r^(-gamma)h from r to infinity,
using the vanishing condition there from H<infinity, therefore gives
this positive contribution to the error bound:

 e_vel(r)=(HG/c)r^gamma integral_r^infinity E(s)s^(q-2)ds
         =(HG/D)r^(q-delta) Eeff(r),
 Eeff(r)=kappa r^kappa integral_r^infinity E(s)s^(-kappa-1)ds. (4)

This is a term in the chosen upper bound on the radial error. It is
not an assertion that the actual error is at least e_vel. If the
integral is infinite the majorant certifies no positive CI contribution,
so assume it finite when evaluating CI. Positivity of the integration
weight and(3) give Eeff>=T[e_min], where T is the operator in(4).

Let ru=5(lambda/Emin)^(1/delta). Because lambda>Emin, ru>5.
Direct integration on(r,ru) and(ru,infinity) gives the exact formula

 T[e_min](r)=Emin[1-delta/(kappa+delta)(r/ru)^kappa], r<=ru,
 T[e_min](r)=lambda(5/r)^delta kappa/(kappa+delta), r>=ru.    (5)

Both branches agree at ru and decrease with r. In particular, for
r<=Rmax<ru,

 Eeff(r)>=Emin[1-delta/(kappa+delta)(Rmax/ru)^kappa].         (6)

The power kappa is essential. Substitution of a pointwise coefficient
into a constant-coefficient error formula would not prove(4)-(6).

## 4. Consequence for all four registered CI targets

For each exact target beta in data/parameters.json, define

 r_beta=[B/(beta sqrt(alpha))]^(1/(-q-1)),
 Kcrit=D B r_beta^delta/[sqrt(2pi) g0].

The checker reconstructs B,Phi,g0 from the exact angular data and
proves, for all twelve reference-target pairs,

 5<r_beta<18860,
 Kcrit/Phi<0.785064,
 ru>18860,
 T[e_min](18860)>0.79303>0.785064.                          (7)

Take R>=R0 as a starting radius for a radial certificate built from
the majorants above. If ehat(r) is the chosen bound on |e(r,theta)|/r^q,
its compensated-velocity contribution(4) ensures

 ehat(r)>=(HG/D)r^(-delta) Eeff(r).

All other terms in the T4-335 absolute error bound are nonnegative.
Thus for any R<=r<=r_beta, positivity of the usual CI integrand,

 [B-sqrt(2pi) ehat(r)]_+^2 r^(2q+1),

would require

 Eeff(r)<D B r^delta/[sqrt(2pi) H G]
        <=(r/r_beta)^delta Kcrit/Phi<0.785064,

contrary to(6)-(7). Therefore the integrand vanishes up to r_beta.
Beyond r_beta it is strictly smaller than B^2 r^(2q+1), because
H,G and the envelope(5) are positive at every finite radius. Since

 B^2 integral_r_beta^infinity r^(2q+1)dr=beta^2,

the computed CI integral from any R is strictly below beta^2. This
also holds when R>r_beta, by the strict decrease of that tail integral.
No assumption R<=r_grad is made or needed.

The conclusion is that every majorant specified in section1 fails
to certify the given target through this CI. It extends the uniform
obstruction of421 to radius-dependent choices and to splicing with
any norm-class universal constant. It includes the current universal
upper bound1.747261 as a special case. It does not preclude a smaller
actual velocity, cancellation in the radial forcing, a stronger tail
input without the delta-term, a sharper estimate using the tail class,
a different norm, or an existence proof by another method.

## 5. Sources, arithmetic and independence

The derivation(4) was suggested by T1 R1-043, which treated the current
universal constant. The argument here proves a common envelope for
all parameter choices, handles s<5, and uses the audited lower bound
for any norm-class universal constant. It also supplies the missing
averaging step for the radius-dependent discussion in T2 the review of T4-414.
The T1 displayed cutoff0.785063 is rounded too low;0.785064 is used.

Dependencies are the full standalone T4-335 proof and its acceptance350,
the CI proof351, the endpoint pointwise inequality380, the universal
lower theorem397/409, and the two-weight theorem410/424. Frozen copies
and exact input JSON are under source/ and data/. The checker verifies
source hashes, exact exponent identities, the elementary integration
identities, all twelve cutoff inequalities and the lower bound(7) in
768-bit Arb. No numerical quadrature or floating optimizer is used.
The independent Opus review R1-045 confirms the entire analytic statement.


## 6. Outer-amplitude extension and its proof

The inner-amplitude hypothesis in Section1 can be dropped for the
following precisely specified substitute. The tail list remains the
T4-335(7) list, with C_delta=H(V+Ebase G)/D, where V>=0,
G>=g0>0 and Ebase>=Emin is the valid norm-class universal coefficient
used when deriving that list. It is fixed as an input to the list;
it is not the improved coefficient that will be deduced from the list.
For any chosen 0<epsilon<=delta, L0>=4, require only
A410>=F C_delta L0^(epsilon-delta), where F>=1.
For s>=L0, positivity of the bracket and its bound by lambda give

 J(s)/H >= lambda Emin g0/D * L0^(epsilon-delta) s^(-epsilon)
          >= lambda Emin g0/D * s^(-delta).                (8)

The last inequality is (s/L0)^(delta-epsilon)>=1.
Dropping the inner amplitude need not itself be a valid velocity
upper bound. Statement(8) is a lower bound on any valid remainder
majorant that retains at least this outer amplitude. If a separately
proved treatment of the inner part supplies additional nonnegative
terms, they only increase that majorant.

At radii below a chosen L0 that choice is unavailable. Allowing all
choices of L0 and all valid norm-class universal fallbacks thus yields

 E(s)>=min(Emin,Cout s^(-delta)),
 Cout=lambda Emin g0/D, rout=(lambda g0/D)^(1/delta).        (9)

The radial average for r<=rout is

 Eeff(r)>=Emin[1-delta/(kappa+delta)(r/rout)^kappa].         (10)

This is exactly the integral in Section3 with a changed switching
radius, so its proof and monotonicity remain valid. The exact angular
inputs for each candidate give rout>r_beta for allfour targets and
the expression in(10) at r_beta is strictly greater than0.79303648.
It is therefore greater than every Kcrit/Phi<0.785064. The same
integrand comparison in Section4 proves that none of these majorants
certifies the target. This strengthens the prior relaxed0.793
calculation but has the same conclusion and scope. It does not
exclude smaller velocity estimates based on additional structure.

## 7. Independent review and provenance

The frozen T1 R1-045 review read the original199-line proof and
independently checked the analytic steps, including the source
stationary equation, the small-radius case, the averaging operator,
all12 target inequalities and the extension(8)-(10). Its independent
script has16 passing groups; the script and output are retained as
source text, not executed here. The peer uses exact algebra and Arb
for acceptance. Float conversions used to format printed endpoints
are not used to accept an inequality. This acceptance recomputes the
finite constants in768-bit Arb from exact angular data.

The historical425 package captured T2_review.md after the coordinator's
12:12:48 overwrite incident. That source has hashc0e299a4a4d08c112ba09eb77ffa22dd4edc3a0eb75022fd826f20d73fde2f9b
and is preserved as historical_incident_review.md, not attributed to
T2. The intact12:06 T2 copy used by423 is frozen here as T2_review.md,
hash20ee1bb384c866e1180a64efb3e31aeac5abfdaee10b9ac108a78038cbe9c89c.
Their only mathematical-text change is the same factor0.67204164
printed to more digits0.672041641664145. Start/save metadata account
for the remaining differences. The exact byte comparison is recorded.
The historical425 result is not modified, and its theorem never
relied on the changed digits or incident metadata.

R1-045 also accepts the426 corrections:0.793 is a relaxed lower
value, its averaged fallback is strictly below0.793 but above0.7929999,
and the VH contribution to C_delta persists independently of a
reduction in the velocity coefficient. Its locked R1-044 revision
changes no mathematical statement. The frozen source diff is retained.

The complete425 theorem is now AUDITED, and the R1 outer extension
is independently confirmed here. Collaboration used the existing
lane configured for Claude Opus5.5; actual provider identity remains
unobservable. No new remote client, foreign executable or server is
used for this acceptance.
