# Finite composition of the 24 accepted weak exclusions

## Statement, spaces and hypotheses

Fix c0=4076476460239181/2251799813685248 and gamma=1/c0. For each
immutable reference numbered 002 through 026 except 011, use its exact
stored potential chi, density rho=-partial_y Delta chi and velocity
u=(-chi_xyy,chi_xxy). Let F=(c0 X+u).grad rho-rho. Their accepted source
and canonical-generator certificates imply smoothness, div u=0,
rho,u=O(r^gamma) and grad rho=O(r^(gamma-1)). These properties and the
previously accepted complete moment certificates are premises here.
This finite audit repeats no field construction or integration.

On R2 with Lebesgue measure, let U[h] have Fourier symbol
(xi1 xi2/|xi|^2,-xi1^2/|xi|^2). Any assignment at xi=0 gives the same
L2 operator. Suppose real h in L2 solves, in distributions,

 F+div((c0 X+u)h)-(2c0+1)h+U[h].grad rho+div(h U[h])=0.       (1)

This definition uses the canonical velocity of h and a fixed exponent.
It is meaningful at L2 regularity since U is an L2 contraction, h U[h]
is locally L1 and the reference coefficients are smooth. S1 normalized
corrections, whenever their traces exist, form a subset. No trace or
exterior-only strain formula is imposed on an arbitrary L2 function.

For each of the 24 references, the accepted probe certificates and the
finite strict comparisons below imply that every correction (1) obeys

                         ||h||2>1/1000.                    (2)

The conclusion excludes the eight exact scalar tuples in the frozen
families.json, the original graded/gradedL2 boxes, and the stated
trans/statL parameter choices retaining the exact top margin and norm
below. It does not quantify over every possible correction space or
commutator constant. Dyadic schemes require their separate tests. Neither
an inverse nor a successful existence closure is inferred.

## Weak identity and strict arithmetic test

Each accepted probe phi is smooth with phi=O(r^-3), grad phi=O(r^-4).
Let I=|int F phi|, let D bound
||(c0 X+u).grad phi+(2c0+1)phi||2+||phi grad rho||2 from above, and
let H bound ||grad phi||infinity from above. The older localized probes
use a valid triangle bound D; the newer angular probes use the complete
M+C. These alternatives have the same role.

Test (1) with phi times a compact radial cutoff that tends to one.
Since div(c0 X+u)=2c0, integration by parts yields the transport
coefficient (2c0+1)phi. The vector multiplier has squared norm
xi1^2/|xi|^2<=1 and has zero divergence. Cauchy-Schwarz therefore bounds
the two linear corrections by D||h||2 and the nonlinear correction by
H||h||2^2. On an escaping annulus of radius R, the cutoff error from
c0 X is O(R^-3) and from u is O(R^(gamma-4)). Their L2 norms tend to
zero. The nonlinear coefficient error tends uniformly to zero, while
h U[h] is L1. The residual pairing converges absolutely because
gamma<1. Consequently

                     I<=Dm+Hm^2, m=||h||2.                 (3)

For containing rational intervals, take Iminus below the absolute
pairing, Dplus above D, and Hplus above H. Positivity and

        Iminus-Dplus/1000-Hplus/1000000>0                   (4)

exclude every m<=1/1000. This is entirely rational arithmetic and needs
no square-root or decimal display. Each source midpoint and radius is
an exact decimal rational. A signed interval crossing zero would give
Iminus=0 and fail (4), rather than inherit a displayed distance floor.

## Exact scalar family ceilings

A scalar norm X_s dominates sqrt(W2)||h||2. The necessary positive
margin, for total correction radius r, is

              mu-C s-cU r/sqrt(s)>0, s>0.                 (5)

Here mu,C,cU,sqrt(W2) are the exact positive tuples in the JSON. It
follows that ||h||2<sqrt(s)(mu-C s)/(cU sqrt(W2)). The derivative
of mu z-C z^3 is mu-3Cz^2, for z=sqrt(s). Its unique positive maximum
occurs at s=mu/(3C), with squared L2 ceiling

                  4mu^3/(27 C cU^2 W2).                   (6)

Exact arithmetic checks that all eight are below (3793/10^9)^2, which
is below (1/1000)^2. Any further theorem restrictions shrink these
balls. Computed-defect versions use the total correction h=g+e in (5),
so this conclusion applies to their total radius as well. An error
radius for e cannot replace that condition.

The old TB-rebal printed value 3.5125e-7 is not treated as an upper
bound. Formula (6), or the accepted outward 3.5126e-7, governs it.
The family identities and norm embeddings are accepted theory inputs,
independently reviewed by the existing Opus T2 lane. This checker
recomputes their finite consequences, not the commutator estimates.

## Original graded and trans/statL margins

Use the unitary Fourier transform, J=(1-Delta)^(1/2), s>0 and
omega=(1+4|X|^2)^(2/5)>=1. Put
P=||omega D2 J^s h||2, a=||D J^s h||2, b=||J^s h||2,
with ordered Cartesian Hessian and Euclidean vector norm. The identity
(1+|xi|^2)^2=1+2|xi|^2+sum_ij xi_i^2 xi_j^2 gives
||h||H^(2+s)^2<=P^2+2a^2+b^2. In the original graded component box
P<=r2,a<=r1,b<=r0, let n=sqrt(r2^2+2r1^2+r0^2), so ||h||2<=n.
Its required top margin is exactly

  1/2-4708s-(217/50+(1049/5)s)n/sqrt(s)>0.                 (7)

Discarding the positive term in the denominator gives
n<(50/217)sqrt(s)(1/2-4708s). The cubic maximum occurs at
s=1/28248. Hence

        n<50/(651 sqrt(28248))<25/54684<1/1000.            (8)

The last relaxation follows from 168^2<28248; no attainment is claimed.
The exact squared middle expression is 625/2992882662.

For the stated trans/statL choices the same margin uses the total
X_s radius R, with X_s^2=P^2+128^2 a^2+512^2 b^2. Thus R<25/54684
and ||h||2<=R/512<25/(54684*512)<3793/10^9. This implication uses
only the original positive top margin. It is independent of K_L and
alpha but does not supply their other existence hypotheses, a resolvent
or a normalization theorem. Changed top floors or constants are outside
scope.

## Independent source check and Opus collaboration

Freeze T4-459's complete finite source manifest, coverage assignments,
registry, proof, checker text and result. Freeze T2's full review,
review checker text and result, plus its direct cited inputs. No peer
code is executed. Every retained file is checked before and after the
own arithmetic. The source manifest's original-path hashes attest the
frozen capture; mutable current handoffs need not equal earlier captures.

Verify all 24 accepted pairing/D/H assignments and compare (4) exactly
with the T4 rational result. Verify each raw registry identity and its
raw-to-canonical bridge where required, distinct from a unlike JSON
serialization hash. Bind all displayed independent comparisons and
accepted ledger excerpts. Match the T2 review's target hashes and its
24 witness identities. Its displayed floating summaries are not input
bounds. Recompute the eight exact (6), (8), and the trans/statL ceiling.
This is a finite composition audit of accepted integrations, not a new
integration, all-transitive-dependency audit or verification of every
claim in the frozen matrix.

T2's sections 1 through 4 explicitly confirm T4-459. Section 5's new
WU3 bound at the bL margin cap is a separate CLAIMED supplement at this
capture and is excluded from this acceptance. Candidate001's stronger
annular application is also separate. Candidates011,027 and any newly
published028 remain outside the 24-candidate statement. The configured
Opus model is us.anthropic.claude-opus-5-5; this file collaboration does
not expose an actual provider response identity and uses no remote
client or substituted model. Only passing own checks authorize this
finite acceptance.
