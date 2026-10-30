# Candidate017 residual identity: Opus reviews and origin condition

## Exact statement, notation and hypotheses

Let F be the residual of immutable candidate017, raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114,
with c=4076476460239181/2251799813685248, rho=-partial_y Delta chi,
U=(-chi_xyy,chi_xxy) and F=(cX+U).grad rho-rho on R2. Lebesgue measure
is understood. For locally integrable G, H(G) is the supremum of
|int G phi| over real smooth compactly supported phi with ||grad phi||2<=1.
Write F_n=f(r)sin(n theta) for one positive odd angular projection.
For a finite trial

 u(r)=sum_i x_i r^3(1+r^2)^(-beta_i)(r^2/(1+r^2))^k_i,
 psi=u(r)sin(n theta),

assume every beta_i>3/2, k_i>=-1 integer, 3+2k_i-n even and nonnegative,
and x_i real. Set d=||grad psi||2^2>0, p=int F_n psi,
Z=-u' sin(n theta)e_r-(r u''+u')cos(n theta)e_theta/n,
a=||Z||2^2, A_F=-r f cos(n theta)e_theta/n, b=<A_F,Z> and
Q=||rF_n||2^2<infinity. Then

 R^2=||r(F_n+Delta psi)||2^2=Q+2n^2(b-p)+n^2(a+d),
 max(0,sqrt(d)-R/n,|p|/sqrt(d))<=H(F_n)<=sqrt(d)+R/n.

This is the statement reviewed independently in T1 R1-053 and T2's
The T2 check of N4-017 (residual identity). It is already the statement of
../candidate017_dual_residual_replay/PROOF.md. The present result
checks the two reviews, supplies the candidate's local integrability
hypothesis directly, and corrects one auxiliary bound in T2's first
review. It does not change any candidate017 mode endpoint.

## Complete argument

The exact source is a finite sum of H_m(x,y) times a real power of
1+r^2, times t_R^w u_R^q P_j(2t_R-1), where H_m=Re(x+iy)^(2m),
t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2), R>0 and m,w,q,j are
nonnegative integers. Each factor is smooth near zero, since its
only denominators there are positive. The exact checker examines every
saved generator and its rational coefficient. Thus chi, rho, U and F
are smooth near zero. Each H_m and each radial factor is even in x
and y. Hence rho and F are odd in y, F(0)=0, and bounded first
derivatives give F(X)=O(|X|). Its angular projection satisfies
|f_n(r)| <= pi^(-1) int_0^(2pi)|F(r,theta)|dtheta=O(r).
In particular F_n is locally integrable. This does not use Q to infer
unweighted integrability near zero. It discharges T2 R3 directly from
the raw smooth potential, without rebuilding any projection.

The trial is smooth at zero by the parity assumption and has u and
its first two logarithmic derivatives O(r^(3-2 beta_min)) at infinity.
Thus d,a and ||r Delta psi||2^2 are finite. Radial cutoffs approximate
psi in gradient norm, with squared cutoff error O(R^(6-4 beta_min)).
This proves H(Delta psi)=sqrt(d) by integration by parts and testing
against cutoffs of psi. Angular integration by parts shows div A_G=G
for every locally integrable single sine-n mode with rG in L2. There
is no radial flux, and its L2 norm is ||rG||2/n. Consequently
H(G)<=||rG||2/n. All integrations follow on annuli and pass to zero
and infinity by the stated local integrability and L2 conditions.

With y=log r and v(y)=u(exp(y)), the radial integrals after theta
integration are d/pi=int(v'^2+n^2v^2)dy and
a/pi=int(v'^2+v''^2/n^2)dy. Therefore

 ||r Delta psi||2^2
 =pi int(v''-n^2v)^2dy
 =n^2(a+d)-2pi n^2[v v']_(-infinity)^(infinity)
 =n^2(a+d).

The boundary term vanishes at zero since u=O(r^n), and at infinity
since beta_min>3/2. The identity int r^2 F_n Delta psi=n^2(b-p)
is pointwise in the radial integrands and needs no integration by
parts. Expansion of ||r(F_n+Delta psi)||2^2 proves the claimed R^2.
The triangle inequalities for H, the completion identity and the
single-mode Hardy bound give both sides involving sqrt(d). Testing
against cutoffs of psi supplies |p|/sqrt(d). These arguments are
exactly the main statements both Opus reviewers accepted.

All cross pairings are absolutely convergent. Cauchy-Schwarz gives
|b|<=sqrt(Qa)/n, |p|<=sqrt(Qd)/n and, for C=int r^2F_n Delta psi,

 |C| <= ||rF_n||2 ||r Delta psi||2 = n sqrt(Q(a+d)).

T2's first review omits n in this last expression. It is false for
n>1: take any nonzero admissible trial and F_n=Delta psi. Then
C=Q=n^2(a+d)>0, whereas sqrt(Q(a+d))=n(a+d). Taking n=3 and
u=r^3(1+r^2)^(-3) gives an explicit rational-integral counterexample.
The missing factor affects neither the main residual identity nor
absolute convergence nor any saved bound in N4-425.

At beta=3/2 with n=1,k=0 the boundary term still vanishes, although
d diverges logarithmically. The strict beta hypothesis ensures all
energy integrals are finite; no converse about the boundary term is
asserted. The six T2 leading-order formulas follow with alpha=3-2beta:
d's radial integrand has leading coefficient alpha^2+n^2, a has
alpha^2+alpha^4/n^2, and the Laplacian square has (alpha^2-n^2)^2,
all multiplying r^(5-4beta).

## Finite independent verification and dependencies

The checker uses its own exact algebra of terms c r^m S^e with
S=1+r^2 and c,e rational. Differentiation is
D(r^m S^e)=m r^(m-1)S^e+2e r^(m+1)S^(e-1).
Products are collected exactly. For every nonzero odd-power term,
A=(m+1)/2 is a positive integer and sigma=-e>A; its integral is

 int_0^infinity r^m S^(-sigma)dr
 =(A-1)!/[2 product_(j=1)^A(sigma-j)].

This follows by t=r^2/(1+r^2) and repeated integration by parts for
the beta integral. Every integrated term is required separately to
converge. No quadrature or numerical derivative is used. Exact JSON
fixtures reproduce all six quantities in each of T2's three examples,
the known Riesz example, the six leading-order rows and the explicit
n=3 counterexample. The two triangle comparisons are checked by
squaring positive rationals. These fixtures validate the algebra;
the generic proof above supplies the general theorem.

Bind the old T2 review, inert program, log and JSON; T1's review53,
inert program, log and extract; own425/426 accepted roots, immutable
raw017 and its source proof and implementation. Compare the complete
T1 extract with all16saved mode records and both residual endpoints,
then recompose its squared lower bound exactly. This is not a replay
of T1's three FLOAT quadratures, any peer code or all1339moment groups.
The existing N4-425/426 certificates supply those actual mode values.
All frozen local dependencies are hashed before and after the check.
A corrected T2 review, when available, is a new separately bound version.

## Scope

CONFIRMED means the analytic identity, source local regularity and
listed finite checks, with the auxiliary typo explicitly repaired.
The complete candidate017 H upper bound, E2 and ordering with007
remain OPEN, including158other Hardy inputs,14residual trials and
G0,G1,P2. No inverse, correction radius or existence is obtained.
Both Opus peers are configured as us.anthropic.claude-opus-5-5 in this
run; the actual provider response is not observable to this lane.
No replacement model or remote client is used.
