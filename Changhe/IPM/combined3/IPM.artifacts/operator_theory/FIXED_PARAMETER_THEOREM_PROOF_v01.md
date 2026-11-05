# Fixed-parameter stationary IPM existence theorem

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
The [complete numerical certificate](fixed_parameter_closure_v01.json),
[independent coordinator reconstruction](../ROOT_FINAL_LOCAL_Q_REPLAY.json),
and [separate final scalar audit](../independent_closure_audit/final_join_audit.json)
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
in [the structural certificate](structure013_result.json). Define
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

The [structural proof](STRUCTURE013_PROOF.md) verifies the exact potential
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
[the operator bridge](OPERATOR_BRIDGE_v01.md).

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
[L2 signed far v05](../coercivity_residual/L2_signed_far_v05/result.json),
with [independent coordinator replay](../ROOT_DIRECT_L2_REPLAY.json).

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
[the forcing certificate](../source_Q_from_integer_tensors.json) and
[its producer](../verify_source_Q_from_integer_tensors.py). The final
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
[the local Q background identity](LOCAL_Q_BACKGROUND_IDENTITY_v01.md),
independently reviewed by the coordinator and finite-rank agent, and
checked by [exact polynomial regression](local_Q_algebra_result.json).

The actual global matrix bound
\(\mathcal M\ge\beta I\), \(\beta=7/10\), is certified by the
complete actual matrix prefix and its independent replay. The
signed exterior rule, exact origin bound and exhaustive core-prefix
geometry are proved in
[the prefix assembly proof](SIGNED_MATRIX_PREFIX_CERTIFICATE_PROOF_v01.md).
Its far bound is \(0.7200661085\ldots\), the origin lower is
\(0.7103192085\ldots\), and all 711 intervening base panels with
996 complete adaptive leaves pass. The exact geometric overlap and both
endpoint proofs exhaust the plane. The
[independent prefix receipt](../independent_closure_audit/matrix_prefix_audit.json)
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
see [the result](../local_energy_coefficients_v01/result.json) and
[the independent scalar assembly](../ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json).

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
[near source envelopes](../source_envelopes_v01/result.json) and
[actual far source bounds](../Q_far_source_highpass_result.json) provide
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
[the fractional transport proof](Q_TRANSPORT_SECOND_TAYLOR_v01.md).

The full source commutator satisfies
\[
\|W[J^q,b\cdot]U[g]\|_2
\le qH_1\|J^{q-1}g\|_2+c_qA_2\|J^\delta g\|_2
+c_qA_q\|g\|_2,
\tag{12}
\]
where \(H_1=\sup W|Db|_F\), \(c_q=q(q-1)/2\), and
\(A_s=M_s(b)+2M_s(Xb)+4M_{s-1}(b)\).
See [the source proof](../finite_rank/Q_SOURCE_FRACTIONAL_COMMUTATOR.md)
and [its independent review](Q_SOURCE_COMMUTATOR_REVIEW_v01.md).
The complete
[whole-plane source certificate](../finite_rank/Q_source_certificate_v01/result.json)
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
[the nonlinear proof and review](NONLINEAR_CORE_AND_Q_REVIEW_v01.md).
It holds for every \(k\in\mathcal B\), and does not require
\(\ell(k)=0\). Its scalar function is evaluated with rigorous Arb
intervals by [the short producer](../finite_rank/Qnorm_nonlinear_bound.py).
Its only nontrivial continuum scalar constant, \(53/50\), has a fresh
complete certificate and independent replay:
[original](nonlinear_core_scalar_result.json),
[replay receipt](../ROOT_NONLINEAR_CORE_REPLAY.json).
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

[The final consumer](assemble_fixed_parameter_closure_v01.py) checks all
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
[the final join note](FINAL_JOIN_FORMULAS_v01.md).

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
[the rational final ball certificate](../RATIONAL_FINAL_BALL.json).

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
proved in [the preferred forced-evolution bridge](Q_FORCED_EVOLUTION_BRIDGE_v02.md).

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
See [the explicit norm proof](../finite_rank/Q_TO_INHERITED_N_EXPLICIT.md)
and [the fixed-radii calculation](../Q_to_inherited_N_at_M03.json).

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
[the independent auditor's lemma](../independent_closure_audit/EXPLICIT_STREAMFUNCTION.md).
The background potential identities directly provide its streamfunction;
the [canonical background velocity proof](CANONICAL_BACKGROUND_VELOCITY_v01.md)
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
