# Candidate016: complete upper bound from the odd prefix through31

Written UTC 2026-10-29T16:35:32.381258+00:00, before this independent checker.

## Exact statement and hypotheses

Fix the real S1 candidate C1-N1-016-legqs25-quot013, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Set c=4076476460239181/2251799813685248 and
delta=1824676646553933/4076476460239181. The canonical IPM velocity
includes its local contact term. Its complete residual is
F=(cX+U[rho]).grad rho-rho. The accepted T4-467 representation has1360
branches, with all160 positive odd sine modes1 through319, representation
SHA2565a0451b817eaf2544b238aa6124a175f50524c788efac8631dddb12352b33367.
F is smooth and locally integrable, and rF belongs to L2(R2).
All norms below use Lebesgue measure. Let
H(F)=sup{|int F phi|:phi in C_c^infinity(R2),||grad phi||2<=1}.

This result assumes the accepted exact raw-to-residual construction,
the complete component certificate T4-467, and each152-file-bound
source-specific positive-pole moment enclosure and outward serialization.
Their construction is not re-proved by hashing. The finite theorem469
is independently AUDITED by both Opus theory lanes, accepted475/477.
The cross and dual certificates472 were independently replayed at full
precision. The general infinite-mode extension474 is unnecessary here.

Let F=sum_n f_n(r)sin(n theta), q_n=pi int r^3 f_n^2 dr and
S=||rF||2^2=sum_n q_n. Assume the complete n=1,3,...,31 certificates
q_n in[L_n,U_n], and S<=S_U. Every omitted mode is at least33. Then

 H(F)^2 <= M2=sum_n q_n/n^2 <=
 P=S_U/1089+sum_(n<33)(1/n^2-1/1089) U_n.             (1)

With J=59664789113139289718803/250000000000000000000000,
the strict cross floor accepted in472 gives

 H(F)^2 < P-J.                                       (2)

For this exact candidate and these accepted source certificates, the
finite replay establishes

 0.529469576110512066428681 < H(F) < 0.619652,
 608.392385921614 < E2(F) < 629.296113.                 (3)

The plain upper from(1) is H(F)<0.789068. Here the registered energy is
E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2,
G0=||F||2, G1=||grad F||2,
P2=||(1+4r^2)^(2/5)D2F||2, with the same tensor convention as467.
These bounds retain E2(007)<606.820219, hence the strict pairwise gap
E2(016)-E2(007)>1.572166921614. They are statements about one residual
norm at identical weights, not correction distances, global minimizers,
an inverse or an existence theorem. Candidate016 remains excluded by
its separately audited correction distance.

## Proof of complete tail coverage

Set A_F=-e_theta r sum_n f_n(r)cos(n theta)/n. Angular sine and cosine
square integrals are pi, so ||A_F||2^2=M2<=S and A_F belongs to L2.
Angular integration by parts gives -int A_F.grad phi=int F phi for
compact smooth phi. On annuli this is an ordinary finite Fourier
identity. The origin limit follows from local integrability of F and
L2 of A_F; radial cutoff gradients are perpendicular to A_F. Thus
div A_F=F on the whole plane without an additional point mass. This
auxiliary divergence identity leaves the canonical IPM contact term
in the definition of F intact. Cauchy-Schwarz gives H(F)^2<=M2.

Every q_n is nonnegative. Therefore
sum_(n>=33)q_n/n^2<=sum_(n>=33)q_n/1089.
Use sum q_n=S and then each positive coefficient1/n^2-1/1089>0
for the complete included prefix to obtain(1). This covers all144
unintegrated modes. Omitting a low mode would invalidate this step.
The alternative split upper is Q=sum U_n/n^2+(S_U-sum L_n)/1089.
Require its tail upper S_U-sum L_n>=0. Exactly
Q-P=sum_(n<33)(U_n-L_n)/1089>=0. The tighter P is selected.
The prefix lower sum L_n/n^2 bounds M2 from below, not H(F)^2.

For the two already admissible distinct-frequency tests of472, put
Z_j=A_(Delta psi_j)-grad psi_j, a_j=||Z_j||2^2>0,
b_j=<A_F,Z_j>. The reviewed theorem469 proves div Z_j=0 and
mutual L2 orthogonality. Thus
H(F)^2<=||A_F+sum t_j Z_j||2^2=M2+sum(2t_j b_j+t_j^2 a_j).
Choose t_j=-b_j/a_j. The accepted strict floor
sum b_j^2/a_j>J proves(2). No completeness of these two trial
functions is assumed, and same-frequency contributions are not added.
The independent472 dual lower square is
280338032026645329921970081837663385523457239013/10^48.
Insert that lower and(2), together with467's positive component
endpoints, into the stated E2 identity. Exact squared comparisons give
(3) and the unchanged007 ordering. Every displayed decimal comparison
is checked as a rational inequality, without floating-point rounding.

## Independent finite replay and source scope

N4-409's version2 result is
01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41.
Its sixteen complete mode files contain484groups:31groups per mode
through19, then29 per mode21 through31. For each mode the complete
ordered branch-pair set and exponent sums are rechecked. In the source
radial convention f_n=r sum_ell v^(ell delta/2)A_(ell,n)(t),
t=r^2/(1+r^2), v=1-t, the square integral is

 q_n=(pi/2)sum_E int_0^1 v^(E delta/2-4)(1-v)^2 G_E(1-v)dv.

The pi factor is angular;1/2 is the Jacobian. After factoring the exact
numerator zero v^k at the endpoint, each exponent E delta/2-4+k>-1.
The denominator factors are positive1+624v. The source exact rational
partial fraction identity, positive-pole moment evaluation and directed
remainder establish each group ball. This finite audit retains those
source-specific premises and checks their exact decomposition metadata.

Reparse every650-digit group interval at8192bits. Extract and sum its
dyadic lower and upper endpoints as exact rationals, then multiply by
a containing pi/2. These complete sums are the enclosure premise.
Require every N4 prefix endpoint to contain the independent enclosure.
A separately rounded original mode ball may have a different radius;
intersection with it is only a consistency check, never a proof of
containment. This follows the already frozen REPLAY_SCOPE_v02.
Recheck source, candidate, c, delta, full1360branch/160mode support,
33Cartesian construction checks,484group counts, endpoint exponents,
ordered-pair coverage, all152source bindings and the reviewed theorem
chain. Compose both exact upper forms and verify their difference.
No candidate moment, residual numerator reconstruction, peer script,
optimization or FLOAT quadrature executes in this audit.

All large values stay in exact JSON inputs and are registered in the
manifest. The proof precedes the checker and original outputs are
immutable. Existing Opus5.5 lanes provide the independent reviews;
the configured identity is us.anthropic.claude-opus-5-5 and the actual
provider identity is unobservable. No new remote model client runs.
