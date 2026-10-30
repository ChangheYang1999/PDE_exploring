# Acceptance of both independent reviews of the partial Hardy theorem

Written UTC 2026-10-29T16:38:19.630323+00:00, before this checker. Targets are T1 R1-050 in
review set 47 and T2 the review of T4-474, frozen with their complete programs,
logs and available exact outputs. Neither peer program is executed here.

## Exact theorem and analytic acceptance

Let F be real, locally integrable on R2, even in x and odd in y, and
rF in L2(R2). Set H(F)=sup|int F phi| over phi in C_c^infinity(R2)
with ||grad phi||2<=1. For its positive odd sine coefficients f_n,
let S_n=pi int_0^infinity r^3 f_n(r)^2 dr and S=||rF||2^2.
Angular Parseval gives S=sum_n S_n. Put M2=sum_n S_n/n^2.
For odd N>=1 with every odd n<N included, define

 B_N=S/N^2+sum_(n<N)(1/n^2-1/N^2)S_n.

Then H(F)^2<=M2<=B_N, the sequence B_N decreases to M2, and
0<=B_N-M2<=N^(-2)sum_(n>N)S_n<=S/N^2. Every coefficient in the
upper-data formula U/N^2+sum_(n<N)(1/n^2-1/N^2)U_n is nonnegative,
so U>=S and U_n>=S_n suffice. All these inputs must refer to the
same F and the complete prefix. Directed uppers from several prefixes
may be combined by their minimum.

Here is a full proof of the limit and origin steps. For almost every r,
F(r,.) belongs to angular L2. Oddness in y removes cosines and the
constant, and evenness in x removes even sine frequencies. The field
A_F=-e_theta r sum_n f_n(r)cos(n theta)/n converges in planar L2,
with squared norm M2<=S. At almost every radius the series also converges
absolutely and uniformly, by Cauchy-Schwarz with sum n^(-2)<infinity.
Its angular distributional derivative is rF. For compact smooth phi,
A_F.grad phi belongs to L1. Angular integration by parts and Fubini,
using F phi in L1, give int A_F.grad phi=-int F phi on the whole
plane. Equivalently use annuli and radial cutoffs; A_F is tangential
so all radial cutoff derivative terms vanish. Thus the origin creates
no extra point mass. Cauchy-Schwarz proves the negative-norm bound.
This auxiliary angular divergence identity does not remove the local
term in the canonical IPM velocity used to construct a candidate F.

The coefficient of S_n in B_N is max(n^(-2),N^(-2)). Subtracting
M2 gives sum_(n>N)(N^(-2)-n^(-2))S_n, a nonnegative convergent series.
Its upper bound proves convergence. Also
B_(N+2)-B_N=((N+2)^(-2)-N^(-2))sum_(n>N)S_n<=0.
These formulas prove both the infinite series theorem and the exact
finite algebra without relying on a finite sample of test cases.
The split interval form Q=sum U_n/n^2+(U-sum L_n)/N^2 satisfies
Q-P=sum_(n<N)(U_n-L_n)/N^2>=0, where P is the positive-coefficient
form. Equality concerns the included interval widths; the total U
need not equal S. No omitted low mode can be assigned the tail weight.

For tests of distinct frequencies satisfying the domain and decay
hypotheses of the audited theorem469, let
Z_j=A_(Delta psi_j)-grad psi_j, a_j=||Z_j||2^2>0,
b_j=<A_F,Z_j>. The tests need not exhaust F's modes. Their divergence
vanishes and distinct angular frequencies make the Z_j orthogonal.
The finite expansion of ||A_F+sum t_j Z_j||2^2 at t_j=-b_j/a_j
gives H(F)^2<=M2-sum b_j^2/a_j<=B_N-sum b_j^2/a_j.
Thus L_j<=|b_j| and A_j>=a_j>0 give the directed gain L_j^2/A_j.
Distinct functions of one frequency cannot be added by this argument;
use the Gram form or select one. This makes explicit the intended
meaning of 'distinct angular tests' in474. Both reviews state this
same qualification. The hypotheses on469's tests remain in force.

The local integrability hypothesis is independent: on0<r<1/2,
F=sgn(y)/(r^2|log r|) has ||rF||2^2=2pi/log2, while
int|F|=2pi int_0^(1/2)dr/(r|log r|)=infinity. The substitution
u=-log r proves both integrals. This is a counterexample to dropping
a stated hypothesis, not to the theorem that retains it.

## Independent exact manufactured checks

For F=(1+r^2)^(-3)sgn(y), write h=(1+r^2)^(-3). Its odd coefficients
are f_n=4h/(pi n). The continuous periodic function
g(theta)=(pi-2|theta|)/2 on[-pi,pi] satisfies g'=-sgn(theta), has
zero mean and cosine coefficients4/(pi n^2) for odd n.
Consequently A_F=-e_theta r h g, with no jump distribution. Direct
radial beta integrals give int r^3 h^2 dr=1/40. Hence S=pi/20 and
M2=pi^3/240, either by direct integration of g^2 or angular Parseval.
The same Parseval identities establish sum_odd n^(-2)=pi^2/8 and
sum_odd n^(-4)=pi^4/96 here, so no externally quoted special-value
claim is needed. Inserting these values gives an exact expression
for each B_N. Its strict positive loss and decrease follow from the
positive higher odd energies, with Arb used only to check the printed
example comparisons.

For polynomial P, int A_F.grad(P(1+r^2)^(-4)) equals minus
int h sgn(y)P(1+r^2)^(-4). For a monomial x^a y^b it vanishes unless
a is even and b odd. Otherwise its angular factor is
2 Beta((b+1)/2,(a+1)/2), and the radial factor is
Beta((a+b+2)/2,7-(a+b+2)/2)/2. These are finite beta integrals.
Evaluating them gives the eight pairings listed in exact JSON, with
values divided by pi. Their noncompact tests have L2 gradients and
integrable pairings, and truncation justifies the displayed identity.
This checks all parity classes, including tests nonzero at the origin.

For psi_1=r(1+r^2)^(-3/2)sin theta, let t=r^2/(1+r^2),w=1-t.
The radial Euler operator on r w^b P(t) is
D_b P=(1-2bt)P+2t(1-t)P'. It follows that D_(3/2)^2(1)
=1-12t+15t^2. Thus the pairing with this infinite-mode source is
b=2 int_0^1 t^(1/2)(1-t)^2(1-12t+15t^2)dt=-256/1155.
The cross energy is a=3pi/8. The mode1 Hardy square is2/(5pi).
The peer's Green-function quadrature is retained as FLOAT and is
not independently replayed or promoted to a certificate.

For F=-Delta(psi_1+psi_3), psi_3=r^3(1+r^2)^(-3)sin3theta,
exact polynomial beta moments give, in units of pi,
S_1=3/4,S_3=64/35,d_1=3/8,d_3=6/35,a_1=3/8,a_3=2/63,b_j=-a_j.
Therefore M2=1201/1260, H(F)^2=153/280 and the two-test improved
bound is exact. The gradient norm equality follows because these
smooth decaying potentials are in the gradient completion and solve
-Delta psi=F. Exact radial cutoff convergence is part of469's domain
argument. These known solutions do not identify candidate016.
The four finite energy lists and each omission example are recomputed.

The review's asymptotic loss statement also follows analytically:
with S_n=2/(5pi n^2), N^3(B_N-M2) equals2/(5pi) times the odd-mesh
Riemann sum N^(-1)sum_(n>=N)[(n/N)^(-2)-(n/N)^(-4)]. This tends
to(1/(5pi))int_1^infinity(t^(-2)-t^(-4))dt=2/(15pi).
Integral bounds control the decreasing tails. Division by S/N^2 gives
the asymptotic ratio8/(3pi^2 N). The finite decimal ratios stay FLOAT.

## Candidate composition and rounding discipline

The reviews' prefix7 arithmetic is checked against frozen476 inputs.
Recompute the complete upper P, Q-P, accepted cross floor, H lower
square, E2 squares and the seven loss bounds. Source groups, full
representation and moment soundness retain their earlier accepted
proofs; this acceptance repeats no candidate integration. T4-480
separately accepts prefix31 and is not attributed to these reviews.

R1-050 V7 uses three rounded intermediate values as if they were
directed uppers. Exact arithmetic gives
M2_upper>1.129995949,
M2_upper>(1.063012676)^2, and
improved_H_square_upper>(0.944106346)^2.
Thus the claim that those particular decimal steps follow by exact
squaring is false. The script actually squares the full saved endpoints
and verifies the coarser published1.063013 and0.944107, correctly.
Safe intermediate upper displays are1.129995950,1.063012677 and
0.944106347. This refutes the directed rounding attribution, not the
valid coarse theorem or an actual H bound obtainable from a different
certificate. Similarly print the total S interval with outward
endpoints[51.06104528760498,51.06104528760499], or mark its repeated
rounded value as approximate. The E2 upper722.968760 is directed and
valid. Both analytic reviews remain CONFIRMED with these qualifications.

Evidence and source maps bind the exact reviewed474/476 files and
previously accepted numerical inputs. The complete peer scripts and
logs are inspected, not executed. Existing Opus5.5 lanes provide
collaboration, configured us.anthropic.claude-opus-5-5; actual provider
identity is unobservable. No new model call, server, JavaScript,
cluster, candidate integration or existence proof occurs here.
