# Result

A complete computer-assisted stationary IPM existence theorem is established at the fixed exponent
\[
c=\frac{4076476460239181}{2251799813685248}.
\]
The unchanged Candidate013 admits a real S1 correction with
\[
\boxed{\|k\|_2\le3.81377\times10^{-7},\qquad
\|WJ^{21/10}k\|_2\le0.3,\qquad
\|J^{21/10}(Wk)\|_2<0.355363<0.387.}
\]
The actual frozen operators, their inverse solutions for the fixed residual, the full invariant ball, contraction, elliptic equation, symmetry, and origin normalization are proved below. The final exact rational self-map margin exceeds0.0260141 and the contraction factor is below0.123.

The proof uses a joint local energy identity in the Q norm and a finite-time forced-evolution barrier. It does not retain an unverified old H4-REST or high-inverse premise. All adopted numerical inputs have whole-plane certificates. The main numerical join and two separate implementations of the complete scalar reconstruction pass.

The campaign began2026-11-04 at21:34:55UTC, with the original hard deadline2026-11-05 at21:34:55UTC. The theorem was closed before that deadline. Candidate007, Candidate013, the exact exponent and the inherited combined2 files were preserved.

The following integrated proof is included in full so this report is self-contained. Its separate [frozen proof file](IPM.artifacts/operator_theory/FIXED_PARAMETER_THEOREM_PROOF_v01.md) and linked detailed lemmas retain the reproducible certificate dependencies.

## Fixed-parameter stationary IPM existence theorem

**Status: complete fixed-parameter proof.** The strict numerical consumer,
its independent 768-bit reconstruction, and a separate independent final
scalar audit all pass. The analytic generator, local identity, source and
transport estimates, nonlinear estimate, fixed-point bridge, symmetry and
normalization proofs have been independently reviewed. All numerical
inputs below refer to the actual unchanged 007-plus-013 profile.

The immutable final consumer result has SHA256
`845b472f63f53cdcb39afeca221f336b7a6b55e81101357c4bf98e8d5fddf62f`;
its producer SHA256 is
`af0ce4ce35977e2707080657b47ada8773db63fb89277669f99911ea895e09d1`.
The [complete numerical certificate](IPM.artifacts/operator_theory/fixed_parameter_closure_v01.json),
[independent coordinator reconstruction](IPM.artifacts/ROOT_FINAL_LOCAL_Q_REPLAY.json),
and [separate final scalar audit](IPM.artifacts/independent_closure_audit/final_join_audit.json)
record the complete bindings and strict inequalities. This proof uses the
high regularity of the actual L2 inverse applied to this fixed residual
only; it does not assert a bounded Q-to-Q inverse for arbitrary forcing.

## Theorem and conventions

Let
\[
c=\frac{4076476460239181}{2251799813685248},\quad
q=21/10,\quad\delta=1/10,\quad W=(1+4|X|^2)^{1/2},
\]
\[
R=\frac{381377}{10^{12}},\qquad M=3/10.
\]
Use the exact unchanged Candidate 007 potential \(\chi\) and the exact
Candidate 013 correction potential \(\phi\), bound to the SHA256 values
in [the structural certificate](IPM.artifacts/operator_theory/structure013_result.json). Define
\[
\rho_*=-\Delta\chi_y-\Delta\phi,\quad
\psi_*=\chi_{xy}+\phi_x,\quad
u_*=(-\psi_{*,y},\psi_{*,x}).
\]
The symmetry class S1 consists of real functions even in \(x\) and odd
in \(y\). Set
\[
Q(g)=\|WJ^qg\|_2,\qquad N(g)=\|J^q(Wg)\|_2,
\quad J=(1-\Delta)^{1/2}.
\]
The velocity convention is
\[
U[g]=(-R_1R_2g,R_1^2g),\quad
R_j=\partial_j(-\Delta)^{-1/2},\quad
\nabla^\perp=(-\partial_y,\partial_x).
\]
Its vector multiplier is
\((\xi_1\xi_2/|\xi|^2,-\xi_1^2/|\xi|^2)\).

There exists a unique correction in
\[
\mathcal B=\{k\in\mathrm{S1}:\|k\|_2\le R,\ Q(k)\le3/10\}
\]
which solves the stationary correction equation. For that correction,
\[
\rho=\rho_*+k,\quad u=u_*+U[k],\quad
\psi=\psi_*+(-\Delta)^{-1}\partial_x k
\]
solve on the entire plane
\[
(cX+u)\cdot\nabla\rho=\rho,\qquad
-\Delta\psi=\partial_x\rho,\qquad u=\nabla^\perp\psi.
\tag{T}
\]
The exponent \(c\) and the numerical center are fixed exactly. In
addition to the two defining correction radii, the additional bounds are
\[
N(k)<0.355363,\qquad
\|\psi-\psi_*\|_{H^{31/10}}\le3/10.
\tag{4}
\]
The correction belongs to the required weighted \(H^{21/10}\) space;
\(k,U[k]\in C^{1,\alpha}\) and
\(\psi-\psi_*\in C^{2,\alpha}\) for every \(0<\alpha<1/10\).
The parity is preserved, the total density has positive \(y\)-slope at
the origin, and the velocity normalization is
\(c+\partial_yu_2(0)=1\). Uniqueness here means uniqueness in
\(\mathcal B\), rather than a claim about all stationary IPM profiles.

## 1. Exact background and actual L2 generator

The [structural proof](IPM.artifacts/operator_theory/STRUCTURE013_PROOF.md) verifies the exact potential
identities, S1 symmetry, divergence freeness,
\(c+\partial_yu_{*,2}(0)=1\), and
\(a_0=\partial_y\rho_*(0)>1\). The actual value is
\(a_0=10.297367365256267\ldots\). Write
\(b=\nabla\rho_*\) and
\(F=(cX+u_*)\cdot\nabla\rho_*-\rho_*\).

For each \(k\in\mathcal B\), define the actual operator
\[
A_k=(cX+u_*+U[k])\cdot\nabla-1+b\cdot U.
\]
The drift is globally Lipschitz, has at most linear growth and constant
divergence \(2c\). Its complete flow defines the transport group in
L2. The source \(b\cdot U\) is bounded in L2. The flow generator plus
this bounded source is the maximal distributional L2 operator; compactly
supported smooth S1 functions are a graph core. The flow difference quotient identifies its generator with the distributional
transport derivative in one direction. In the other direction, radial
cutoffs and the bounded Lipschitz Friedrichs/mollifier commutator give
graph approximation by compactly supported smooth functions. This proves
the equality of the maximal and flow domains for rough inputs as well.
These facts are proved in sections1–2 of
[the operator bridge](IPM.artifacts/operator_theory/OPERATOR_BRIDGE_v01.md).

The complete direct Candidate 013 L2 certificate and its independent
replay give
\[
\Re\langle A_kg,g\rangle\le-\beta_2\|g\|_2^2,
\quad\beta_2=2087491/10^6.
\tag{5}
\]
The drift perturbation \(U[k]\) is divergence free, so the certificate
is uniform over the whole ball and needs no origin-strain constraint.
Consequently
\[
\|e^{tA_k}\|_{2\to2}\le e^{-\beta_2t},\qquad
-A_k^{-1}F=\int_0^\infty e^{tA_k}F\,dt.
\tag{6}
\]
The actual certificate is
[L2 signed far v05](IPM.artifacts/coercivity_residual/L2_signed_far_v05/result.json),
with [independent coordinator replay](IPM.artifacts/ROOT_DIRECT_L2_REPLAY.json).

The inherited independently audited exact residual norm and the new
integer-tensor forcing proof give
\[
\|F\|_2<f_2=7961207/10^{13},\qquad Q(F)<n=759/100000.
\tag{7}
\]
The exact rational inequality \(R\beta_2>f_2\) is strict. The forcing
proof uses the inherited ordered Cartesian tensors of \(WF\), explicit
derivatives of \(W^{-1}\), integer product rules and interpolation; it
uses no unverified norm multiplier constant. See
[the forcing certificate](IPM.artifacts/source_Q_from_integer_tensors.json) and
[its producer](IPM.artifacts/verify_source_Q_from_integer_tensors.py). The final
consumer separately binds the inherited actual unweighted publication and
its independent audit, and checks their exact rational norm and energy
uppers against \(f_2\).

## 2. Exact local background energy

Let \(f=J^\delta g\), \(h=J^2f=J^qg\), and
\[
d=c+1+(cX+u_*)\cdot\nabla\log W,\quad S=\operatorname{Sym}Du_*,
\]
\[
K=\begin{pmatrix}-b_y&b_x/2\\b_x/2&0\end{pmatrix},\qquad
\mathcal M=(d-qc)I-qS-K.
\]
This is the full source-and-strain matrix from the prompt. The new method
retains it on Hessian columns in physical space, rather than weakening
its source term before combining principal terms.

The exact Taylor identity is
\[
[J^q,u_*\cdot\nabla]g
=-q\operatorname{div}(S\nabla f)
+\frac{q\delta}{2}D^2u_*:D^3J^{\delta-2}g
+\mathcal R_{3,u_*}(\nabla g).
\tag{8}
\]
The integer identity \(U[J^2f]=U[f]+(-f_{xy},f_{xx})\) combines the
highest source with the highest transport contribution. In two dimensions
\[
(\Delta f)(\mathcal M:D^2f)
=\sum_j(\nabla\partial_jf)^T\mathcal M(\nabla\partial_jf)
+\operatorname{tr}(\mathcal M)\det D^2f.
\]
The last term is integrated exactly using
\[
\int a\det D^2f
=\int a_{xy}f_xf_y-\tfrac12a_{xx}f_y^2-\tfrac12a_{yy}f_x^2.
\]
The divergence term containing \(\Delta u_*\) is also integrated in
full. The complete identity and all signs are proved in
[the local Q background identity](IPM.artifacts/operator_theory/LOCAL_Q_BACKGROUND_IDENTITY_v01.md),
independently reviewed by the coordinator and finite-rank agent, and
checked by [exact polynomial regression](IPM.artifacts/operator_theory/local_Q_algebra_result.json).

The actual global matrix bound
\(\mathcal M\ge\beta I\), \(\beta=7/10\), is certified by the
complete actual matrix prefix and its independent replay. The
signed exterior rule, exact origin bound and exhaustive core-prefix
geometry are proved in
[the prefix assembly proof](IPM.artifacts/operator_theory/SIGNED_MATRIX_PREFIX_CERTIFICATE_PROOF_v01.md).
Its far bound is \(0.7200661085\ldots\), the origin lower is
\(0.7103192085\ldots\), and all 711 intervening base panels with
996 complete adaptive leaves pass. The exact geometric overlap and both
endpoint proofs exhaust the plane. The
[independent prefix receipt](IPM.artifacts/independent_closure_audit/matrix_prefix_audit.json)
binds the unchanged result, origin cache, raw chunks and source files.

The completed whole-plane local certificate gives
\[
\|S\|_{\infty,\mathrm{op}}\le3/2<c,\quad
K_1<483.477,\quad K_0<117.012,\quad
W_{u,2}:=\sup W|D^2u_*|_F<5.348.
\tag{9}
\]
The strain bound and \(u_*(0)=0\) imply
\(X\cdot u_*(X)\ge-(3/2)|X|^2\), hence \(d\ge c+1\).
The exact weight identity is
\[
Q(g)^2=\|WD^2f\|_2^2+2\|W\nabla f\|_2^2+\|Wf\|_2^2
-8\|\nabla f\|_2^2-16\|f\|_2^2.
\]
The local part of the background form is therefore bounded above by
\[
-\beta Q(g)^2-(c+1-\beta)(\|W\nabla f\|_2^2+\|Wf\|_2^2)
+K_1\|\nabla f\|_2^2+K_0\|f\|_2^2
+\langle Wh,Wb\cdot U[f]\rangle.
\tag{10}
\]
All coefficient constants in (9) come from the complete 599-panel local
certificate including its origin and exterior, rather than sampled values;
see [the result](IPM.artifacts/local_energy_coefficients_v01/result.json) and
[the independent scalar assembly](IPM.artifacts/ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json).

For any fixed splitting radius \(R_b\), let
\(B_n\ge\sup_{|X|\le R_b}W|b|\) and
\(B_f\ge\sup_{|X|\ge R_b}|b|\). The angular Hardy inequality for
central odd functions gives the joint weighted velocity bound
\(\|WU[f]\|_2\le\sqrt3\|Wf\|_2\). Thus the final term in (10)
is at most
\[
B_n\|f\|_2Q(g)+\sqrt3B_f\|Wf\|_2Q(g).
\]
Young's inequality absorbs the far term into the explicit negative
weighted-f allowance in (10), at cost
\(e_f=3B_f^2/[4(c+1-\beta)]\). The complete
[near source envelopes](IPM.artifacts/source_envelopes_v01/result.json) and
[actual far source bounds](IPM.artifacts/Q_far_source_highpass_result.json) provide
these constants. For \(R_b=30000\), \(B_f<0.294545\); the final
consumer uses all containing digits and the corresponding certified near
envelope.

## 3. Fractional transport, full source commutator and nonlinear loss

Let \(B_j=\|D^jb\|_2\), \(X_j=\|D^j(Xb)\|_2\). The velocity
moment bounds needed by the third remainder are
\[
U_2=\tfrac12\sqrt{B_1B_3},\quad
U_3=\tfrac12\sqrt{B_2B_4},\quad
XU_3=\tfrac12\sqrt{[X_2+(\sqrt2+1)B_1]
[X_4+(\sqrt2+1)B_3]}.
\]
The exact Taylor remainder obeys
\[
\|W\mathcal R_{3,u_*}\nabla g\|_2
\le T_3\|\nabla g\|_2,\qquad
T_3=\frac{51}{1000}(U_3+2XU_3+6U_2).
\tag{11}
\]
The rational factor is a strict upper for
\(q\delta/(3\sqrt{2-\delta})\). The second term of (8) is bounded
by \((q\delta/2)W_{u,2}\|J^{q-1}g\|_2\). These are proved,
including cutoff passage for the actual growing background velocity, in
[the fractional transport proof](IPM.artifacts/operator_theory/Q_TRANSPORT_SECOND_TAYLOR_v01.md).

The full source commutator satisfies
\[
\|W[J^q,b\cdot]U[g]\|_2
\le qH_1\|J^{q-1}g\|_2+c_qA_2\|J^\delta g\|_2
+c_qA_q\|g\|_2,
\tag{12}
\]
where \(H_1=\sup W|Db|_F\), \(c_q=q(q-1)/2\), and
\(A_s=M_s(b)+2M_s(Xb)+4M_{s-1}(b)\).
See [the source proof](IPM.artifacts/finite_rank/Q_SOURCE_FRACTIONAL_COMMUTATOR.md)
and [its independent review](IPM.artifacts/operator_theory/Q_SOURCE_COMMUTATOR_REVIEW_v01.md).
The complete
[whole-plane source certificate](IPM.artifacts/finite_rank/Q_source_certificate_v01/result.json)
uses all 2,303 radial panels and containing origin and exterior expansions.
The strict consumer and both independent scalar reconstructions sum all
six actual raw energies and both tails again. Safe outward displays are

| Global coefficient | Certified upper |
|---|---:|
| \(H_1\) | 14.831 |
| \(A_2\) | 222.177 |
| \(A_q\) | 247.658 |
| \(B_1,B_2\) | 17.012, 10.466 |
| \(B_3,B_4\) | 28.415, 992.321 |
| \(X_2,X_4\) | 57.994, 279.212 |
| \(U_2,U_3,XU_3\) | 10.993, 50.955, 92.811 |
| \(T_3\) | 15.430 |

These are global containing bounds; no partial core sum is used as a
whole-plane upper.

Put \(r=R/M\). On every test satisfying \(\|g\|_2\le R\),
\(Q(g)\ge M\), interpolation, (10)--(12), and the near/far source
split give the uniform background loss
\[
\begin{aligned}
e_{\rm bg}={}&e_f+(K_1+B_n)r^{20/21}+K_0r^{40/21}
+\frac{q\delta}{2}W_{u,2}r^{10/21}+T_3r^{11/21}\\
&+qH_1r^{10/21}+c_qA_2r^{20/21}+c_qA_qr.
\end{aligned}\tag{13}
\]
All exponents are positive, so evaluating at the two ball radii is valid
on the entire exterior test region.

The nonlinear term \(U[k]\cdot\nabla g\) has the independently
proved exterior loss \(L_Q(R,M)\) from
[the nonlinear proof and review](IPM.artifacts/operator_theory/NONLINEAR_CORE_AND_Q_REVIEW_v01.md).
It holds for every \(k\in\mathcal B\), and does not require
\(\ell(k)=0\). Its scalar function is evaluated with rigorous Arb
intervals by [the short producer](IPM.artifacts/finite_rank/Qnorm_nonlinear_bound.py).
Its only nontrivial continuum scalar constant, \(53/50\), has a fresh
complete certificate and independent replay:
[original](IPM.artifacts/operator_theory/nonlinear_core_scalar_result.json),
[replay receipt](IPM.artifacts/ROOT_NONLINEAR_CORE_REPLAY.json).
The argument uses the exact coordinate identity for \(W^2=1+4r^2\);
it does not transfer an unweighted transport bound to Q without proof.

Define
\[
b_Q=\beta-e_{\rm bg}-L_Q(R,M).
\]
The required strict numerical conditions are
\[
b_Q>0,\qquad b_QM^2-nM>0,\qquad
\frac{5M}{\beta_2\sqrt{11\pi}}<1.
\tag{14}
\]
All conditions (14) pass with the exact prescribed radii and
\(R_b=30000\). Containing numerical values give
\[
e_{\rm bg}<0.157652150,\quad L_Q<0.227998902,\quad
b_Q>0.314348949,
\]
\[
b_QM^2-nM>0.0260144054,\qquad
S_1M/\beta_2<0.122235.
\tag{15}
\]
The lower source far rate is below \(0.0308328987471\), the near
source rate is below \(0.062680871151\), the third transport rate is
below \(0.012591769585\), and the source principal rate is below
\(0.048512437102\). The final certificate records all eight
separate interpolation rates; the two independent reconstructions agree.

[The final consumer](IPM.artifacts/operator_theory/assemble_fixed_parameter_closure_v01.py) checks all
source and code bindings, complete covers and binary leaf partitions,
endpoint provenance, forcing and nonlinear replays, and actual coefficient
reconstruction before reporting `FINAL_NUMERICAL_CLOSURE_PASS`.
Its globally valid background Garding pair, obtained by the weighted
AM--GM tangent and rounded upward, is
\[
\epsilon=\frac{3491}{31250}=0.111712,\qquad
C=28427625600,
\]
\[
\Re\langle WJ^qA_*g,WJ^qg\rangle
\le-(7/10-\epsilon)Q(g)^2+C\|g\|_2^2.
\tag{16}
\]
Here \(A_*=(cX+u_*)\cdot\nabla-1+b\cdot U\) is the full
background operator. This is a one-sided full background form estimate;
it does not misidentify a noncompact negative contribution as an
absolute compact remainder. The rounded frozen self-map margin is still
strictly greater than \(0.0260142657\). The exact formulas are in
[the final join note](IPM.artifacts/operator_theory/FINAL_JOIN_FORMULAS_v01.md).

For a proof using only short rational ball constants, adopt
\[
b_0=\frac{9192}{15625}=7/10-\epsilon,\qquad
L_Q<\frac{57}{250},\qquad
b'=b_0-\frac{57}{250}=\frac{11259}{31250}.
\]
Then the exact sufficient ball inequalities are
\[
R\beta_2-f_2=\frac{355107}{10^{18}}>0,
\]
\[
b'M^2-nM-CR^2
=\frac{8129427150678683343}{312500000000000000000}
>0.0260141,
\tag{17}
\]
and \(S_1M/\beta_2<123/1000\). The contraction comparison follows
already from the rational lower \(\pi>157/50\). These exact checks,
including the high-norm translation, are recorded in
[the rational final ball certificate](IPM.artifacts/RATIONAL_FINAL_BALL.json).

## 4. Finite-time barrier gives the actual high inverse

The preceding verified estimates now establish the frozen self-map.
For smooth frozen \(k\in\mathcal B\),
the transport flow acts as a C0 group on Q: Q is equivalent to
\(\{g:g,xg,yg\in H^q\}\); integer H2/H3 flow estimates and
interpolation establish the claim. The source is bounded on Q by the joint
weighted velocity estimate and multiplication in this coordinate Sobolev
space. The Q semigroup agrees with the actual L2 semigroup, and compactly
supported smooth S1 functions form its graph core. No global Q dissipation
has been assumed.

The forced trajectory
\[
g(t)=\int_0^te^{sA_k}F\,ds
\]
belongs to the Q generator domain, is C1 in Q, and satisfies
\(g_t=A_kg+F\), \(g(0)=0\). The actual L2 bound (6) gives
\(\|g(t)\|_2\le(f_2/\beta_2)(1-e^{-\beta_2t})<R\).
On an interval with \(Q(g(t))>M\), graph-core approximation passes
(16)--(17) and the exterior nonlinear bound to this actual trajectory,
giving
\[
\tfrac12\partial_tQ(g(t))^2
\le-b'Q(g(t))^2+nQ(g(t))+CR^2<0.
\]
The final strict sign follows because the positive root of
\(b'z^2-nz-CR^2\) is strictly smaller than \(M\), by (17).
Continuity prevents a first crossing of \(M\). Thus \(Q(g(t))\le M\)
for every finite time. Taking the actual L2 limit (6) and weak Q lower
semicontinuity gives
\(z_k=-A_k^{-1}F\in\mathcal B\).
For this fixed residual F, this proves the high regularity of every actual
frozen L2 inverse image and the self-map. No high inverse was assumed as a
premise of an energy calculation, and no arbitrary-forcing Q inverse
claim is needed. The full domain and barrier argument is
proved in [the preferred forced-evolution bridge](IPM.artifacts/operator_theory/Q_FORCED_EVOLUTION_BRIDGE_v02.md).

For rough \(k\in\mathcal B\), approximate \(J^qk\) in
\(L^2(W^2dX)\) by Schwartz S1 functions, apply \(J^{-q}\), and rescale
by the minimum of the two radius ratios. These in-ball approximants
converge in Q. If \(z_n\) are their already constructed actual inverses,
the maximal L2 difference equation and uniform gradient bound give
\[
\|z_n-z_k\|_2\le\beta_2^{-1}M
\|U[k_n]-U[k]\|_\infty\longrightarrow0.
\]
Weak Q lower semicontinuity proves \(z_k\in\mathcal B\).
No old reference-ball graph witness is needed in this proof.

## 5. Contraction, normalization and full elliptic system

The ball is complete in the L2 metric: L2 limits of Q-bounded sequences
have the same Q bound by distributional identification and weak lower
semicontinuity. The exact gradient embedding is
\[
\|\nabla z\|_\infty\le S_1Q(z),\qquad
S_1=5/\sqrt{11\pi}.
\]
The difference of two actual frozen inverse equations, the L2 inverse
bound, and \(\|U[g]\|_2\le\|g\|_2\) prove
\[
\|z_k-z_l\|_2\le(S_1M/\beta_2)\|k-l\|_2.
\]
The last inequality in (14) gives a contraction. Its unique fixed point
satisfies
\[
(cX+u_*+U[k])\cdot\nabla k-k+b\cdot U[k]=-F,
\]
which expands exactly to the first equation of (T).

For the inherited high norm, the explicit heat-kernel commutator proof
gives, with \(L_\delta=\sqrt\pi\Gamma(9/20)/(20\Gamma(19/20))\),
\[
N(k)\le M[1+2L_\delta r^{1/21}+4r^{10/21}
+8L_\delta r^{11/21}+8r^{20/21}+10L_\delta r].
\]
At the exact radii above, its interval evaluation is
\(N(k)<0.355362796535<0.355363\).
See [the explicit norm proof](IPM.artifacts/finite_rank/Q_TO_INHERITED_N_EXPLICIT.md)
and [the fixed-radii calculation](IPM.artifacts/Q_to_inherited_N_at_M03.json).

To obtain the actual streamfunction without a low-frequency assumption,
put \(G(\xi)=J(\xi)^q\widehat k(\xi)\). The Q bound gives
\(G\in H^1_\xi\). Central oddness removes its zero angular mode, so
angular Poincare and polar integration give
\[
\int|G(\xi)|^2/|\xi|^2\,d\xi\le\|\nabla_\xi G\|_2^2.
\]
Therefore the ordinary Fourier function
\(\widehat{\psi_k}=i\xi_1\widehat k/|\xi|^2\) lies in
\(H^{q+1}\), with
\(\|J^q\psi_k\|_2\le M/2\) and
\(\|\nabla J^q\psi_k\|_2\le M\). Retaining the two frequency
budgets jointly gives the stronger bound
\[
\|\psi_k\|_{H^{q+1}}^2
\le\|G\|_2^2+\|\nabla_\xi G\|_2^2
\le\|G\|_2^2+4\|\nabla_\xi G\|_2^2=Q(k)^2\le M^2.
\]
This proves (4) and the two elliptic identities in (T). The complete Hardy and streamfunction proof is
[the independent auditor's lemma](IPM.artifacts/independent_closure_audit/EXPLICIT_STREAMFUNCTION.md).
The background potential identities directly provide its streamfunction;
the [canonical background velocity proof](IPM.artifacts/operator_theory/CANONICAL_BACKGROUND_VELOCITY_v01.md)
also identifies the appropriate central-odd renormalized whole-plane
Riesz velocity for the growing density. Equivalently the explicit
background pressure is \(p_* =\chi_{yy}+\phi_y\), which gives Darcy's
law by differentiation, and the L2 correction has the ordinary Fourier
Darcy velocity.

Finally parity gives \(\rho(0)=u(0)=0\) and
\(\partial_x\rho(0)=0\). The positive total y-slope follows from
\(\partial_y\rho(0)\ge a_0-S_1M>0\).
Taking the first-order y-axis expansion of the now continuous stationary
equation yields
\[
(c+\partial_yu_2(0)-1)\partial_y\rho(0)=0.
\]
Thus \(c+\partial_yu_2(0)=1\), or
\(\ell(k)=\partial_yU_2(k)(0)=0\), automatically at the fixed point.
No origin hyperplane was imposed on the frozen iteration ball.

Every premise used above is proved analytically or supplied by a complete
actual interval certificate with the indicated independent checks. Hence
(T), the correction bounds, the fixed exponent, the symmetry and the
normalization all follow. In particular no inherited high generator,
reference-ball graph witness, unfinished analytic far assumption, or
conditional old commutator closure remains in this existence argument.

For a fresh numerical reconstruction preserving the immutable original
certificate and receipts, run from the repository root:

```sh
/tmp/ipm-combined3-venv/bin/python -B \
  Changhe/IPM/combined3/IPM.artifacts/verify_final_local_Q_closure.py \
  --bits 768 --out /tmp/ipm-fixed-parameter-join-replay.json
```

The verifier reads the final certificate's exact input paths and checks
all bound hashes and all raw source panels before rebuilding the nonlinear
formula, the eight background rates, both self-map margins and contraction
ratio. It imports neither the main consumer nor its nonlinear calculator.
The source producer and complete analytical proofs remain available for
independent regeneration of every numerical premise.


## Required direct-coercivity and full-matrix investigations

The immutable source identities used throughout are:

| Exact source | SHA256 |
|---|---|
| Candidate007 d2w_j7_n4_E2bal_mid180_exact.json | ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21 |
| Candidate013 phi_007_b18s2_phi_exact.json | a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a |

### A. Direct actual Candidate013 L2 coercivity

The direct source form is decomposed into its signed pointwise contribution and the gradient-structured double-Riesz Hilbert–Schmidt remainder. The established inherited identity is
\[
\kappa^2=\frac{(\log2-1/2)\|D\rho_{*,x}\|_2^2
 +(3\log2-2)\|D\rho_{*,y}\|_2^2}{16\pi}.
\]
Its cutoff extension applies to this exact smooth sublinear background. This is an inherited proved identity, rather than a transfer of Candidate007's numerical coercivity.

The actual Candidate013 computation gives
\[
\theta\le1/80,\qquad \kappa<0.710328127935052,\qquad
\beta_{\rm actual}=c+1-\theta-\kappa>2.087491082264946.
\]
The adopted rational lower is2087491/1000000. This is the strongest certified direct rate produced in this campaign; no optimality is claimed.

The completed certificate uses1856 core panels and an exact signed far expansion. The far homogeneous terms are integrated with their cross-power terms retained before taking norms. A complete independent assembly replay agrees with all adopted values. The source-identity, configuration, code, used-chunk and far-cache hashes are checked by the final consumer. See [the final direct certificate](IPM.artifacts/coercivity_residual/L2_signed_far_v05/result.json), [its independent replay](IPM.artifacts/ROOT_DIRECT_L2_REPLAY.json), and [the completed A/B handoff](IPM.artifacts/coercivity_residual/A_B_HANDOFF.md).

The improved rate was propagated into the actual L2 ball and the high-energy calculation. The exact adopted radius condition is
\[
(381377/10^{12})(2087491/10^6)-7961207/10^{13}
=355107/10^{18}>0.
\]

### B. Genuine full-matrix Riesz residual bound

For the original-norm source \(H=J^{21/10}(WF_*)\), a matrix-weighted Riesz dual bound was obtained with an actual sine115 Gaussian test vector of width1471/10000. All73 source-coordinate panels,73 inverse-matrix Gram panels, heat-integration errors, omitted vector mass and endpoint errors are controlled. The argument computes the requisite Riesz functional; it never replaces a Riesz transform by the original residual pointwise.

The source coordinate is approximately0.000495955159. Its test norm square is bounded by \(B<0.423911139\). For the free baseline
\(\beta_o=13999/20000\), the inverse Gram is bounded by
\(\Gamma<0.453730730\). The exact variational/Woodbury estimate gives
\[
d_F^2\le\frac{n_N^2}{\beta_o}
-\frac{|c_F|^2}{\beta_o^2(\Gamma+B/\beta_o)}
<4.360534122\times10^{-5}.
\]
Consequently
\[
\boxed{d_F<0.00660344,\qquad
\sqrt{\beta_o}\,d_F<0.00552464.}
\]
The corresponding scalar source bound is \(n_N<0.00555458\); the squared dual upper improves by about1.068%. The fresh actual global matrix certificate discharges the matrix premise. [The actual-source join](IPM.artifacts/ACTUAL_FULL_MATRIX_RESIDUAL_JOIN.json) separately checks the inherited exact Hermite-majorant norm upper and its independent audit. The complete interval value of the effective source upper is0.005524631986056117....

This improvement was incorporated into an executed old-N nonlinear closure comparison, including the loss-adjusted inverse denominator. At the same conservative matrix baseline \(\beta_o=0.69995\), the old-L2 case has conditional margin−0.0007497167; the improved direct L2 rate gives+0.0070962617; adding the full-matrix source gives+0.0071090663. These are matched-baseline comparisons with the old CE/background-form premises retained. They do not claim a verified old H4 estimate, and the first row is not the different original combined2 planned matrix tuple. See [the executed comparison](IPM.artifacts/old_N_actual_AB_comparison.json).

The full-matrix result uses the original N source. No N residual bound is transferred to Q. The existence proof uses its separately proved Q forcing bound.

## Compact/noncompact decomposition and implemented finite rank

The original-N exact decomposition retains the noncompact favorable multiplier \(-qcJ^{-2}\) and the principal pointwise matrix. Its remaining operator is qualitatively compact for the actual coefficient class. Spatial coefficient decay and frequency localization are essential: negative order alone does not imply whole-plane compactness.

[The exact decomposition](IPM.artifacts/EXACT_COMPACT_DECOMPOSITION.md) reconstructs TIS, TII, transport, scalar-weight and source forms. [The independent direct compactness supplement](IPM.artifacts/independent_closure_audit/DIRECT_COMPACTNESS_SUPPLEMENT.md) proves compactness of the decaying-coefficient and transport remainders by Fourier tails, physical cutoffs and Hilbert–Schmidt low-frequency kernels. The actual inherited EW kernel proof is present and its coefficient/weight hypotheses were checked.

An actual nonzero smooth rank-one approximation of \(C_{vs3}\) was certified:
\[
\varphi(x,y)=\sqrt{2/\pi}\,y e^{-(x^2+y^2)/2},\qquad
P=|\varphi\rangle\langle\varphi|,\qquad K_N=PC_{vs3}P.
\]
Its explicit matrices are
\[
A_{11}\simeq-0.0686740077826094,\qquad
B_{11}=\|WJ^{21/10}\varphi\|_2^2
\simeq76.24248469591405.
\]
The finite-rank price satisfies \(C_N<1309/250=5.236\). Orthogonality of \(T\mapsto PTP\) in Hilbert–Schmidt space gives the actual whole-plane operator tail
\[
\|C_{vs3}-PC_{vs3}P\|_{\rm op}
\le\sqrt{\kappa^2-|A_{11}|^2}
<7071/10000.
\]
The lower endpoint of \(|A_{11}|^2\), rather than its upper endpoint, is subtracted. The original-N predual Gram is used consistently. [The proof and certificate](IPM.artifacts/finite_rank/ACTUAL_RANK1_OPERATOR_TAIL_PROOF.md) bind every source and arithmetic dependency.

This tail is too coarse for the old closure budget. Larger Hermite matrices, algebraic-tail bases, spatial/frequency splits and joint-form computations were investigated. Uncertified larger matrices remain explicitly labeled FLOAT. A closing quantitative finite-rank approximation of the entire old compact remainder was not obtained.

The successful theorem instead uses the exact local identity in the proof above. It replaces that particular decomposition, combining the principal source and transport before estimating lower orders. The old full-compact estimate is not a hypothesis of this proof, and eliminated TIS/TII/Cvs3/Ew prices are not added again. The actual finite-rank work is preserved as a qualified deliverable; its unsuccessful sufficient bound is not a nonexistence claim.

## Comparison with combined2

| Item | Inherited route | Established in combined3 |
|---|---|---|
| Exponent and numerical center | Exact fixed c, Candidate013 | Identical |
| L2 rate used | 7/4 after transfer | Direct actual rate >2.087491082264946 |
| L2 correction radius | 4.549261e-7 | 3.81377e-7 |
| Original-N forcing | <.00555458 | Same source; matrix-effective upper <.00552464 |
| Weighted correction ball | N≤.387 | Q≤.3 and N<.355363 |
| Nonlinear loss | CE/N upper .3651689966 at inherited radii | Proved outside-Q upper <.228 at selected radii |
| Background strong rate after high price | Planned b0=.55, retaining form premises | Certified .7−.111712=.588288 |
| Background weak price | Near113428316345 plus stipulated rest9941475955 | Certified full-Q price28427625600 |
| Actual inverse/self-map | Retained operator and high-energy conditions | Actual L2 flow inverse and forced Q barrier proved |
| Existence status | Conditional | Fixed-parameter theorem proved above |

The nonlinear norms, radii and background decompositions differ. This table does not equate their individual component prices. The relevant comparison is the complete invariant-ball calculation, which is now verified with exact rational margin
\[
\frac{8129427150678683343}{312500000000000000000}
=0.0260141668821717866976.
\]

## Isolated high-order residual-pairing experiment

The separately requested experiment is complete in its own subdirectory, with [a self-contained report, convergence tables, exact coefficients and reproduction commands](IPM.artifacts/residual_pairing_experiment/residual_pairing_experiment.report.md). It retained the original requested radii
\(R=4.549261\times10^{-7}\), \(M=.387\), independently of the selected theorem ball.

It found numerical \(Q(F_*)\approx0.0050494\), with estimated screening uncertainty about1e-7. However,
\[
\boxed{\|J^{2.1}(W^2J^{2.1}F_*)\|_2=\infty.}
\]
An exact nonzero residual tail has exponent
\(p=4/c-5=-2.790444924\ldots\). Bessel differentiation preserves its leading algebraic term; \(W^2J^{2.1}F_*\) therefore has a non-L2 tail. Resolved finite-box values near214 cannot establish finiteness.

A Gaussian high-pass split has numerical \(D_{\rm hi}\approx214.9504\) and a pairing estimate near9.7922e-5, about twenty times smaller than the numerical direct QM estimate. These fractional FFT/FFTLog values are not rigorous norm certificates. They are worth separate certification. None of them is an input to the existence proof.

The experiment did not optimize or change Candidate013, shared checkpoints or running main jobs. Its numerical children ran individually at idle scheduling priority and have finished.

## Reproducibility and independent verification

[REPRODUCE.md](IPM.artifacts/REPRODUCE.md) gives the pinned environment bootstrap, verification into fresh output destinations, and primary regeneration commands. All new durable artifacts are in combined3. Exact caches, raw panels, code/source bindings, interval outputs, independent receipts and restartable checkpoints are preserved. Four host restarts were recovered from saved work without resetting the deadline.

The primary quantitative certificate is [the frozen final numerical join](IPM.artifacts/operator_theory/fixed_parameter_closure_v01.json). The independently implemented complete scalar reconstructions are [the root768-bit replay](IPM.artifacts/ROOT_FINAL_LOCAL_Q_REPLAY.json) and [the separate auditor replay](IPM.artifacts/independent_closure_audit/final_join_audit.json). [The final rational-ball certificate](IPM.artifacts/RATIONAL_FINAL_BALL.json) checks the simple displayed constants using exact rational arithmetic.

The full logical chain includes the exact profile, all whole-plane numeric inputs, actual generator/domain construction, finite-time Q evolution, fixed-forcing inverse regularity, rough-input passage, ball completeness, contraction, elliptic system and derived normalization. A scalar calculator's PASS is not substituted for those proofs.

The old entire-compact finite-rank tail remains an auxiliary open quantitative problem, and the isolated FFT experiment remains numerical evidence. Neither is an assumption of the theorem. No global uniqueness, stability, or additional smoothness conclusion is asserted.
