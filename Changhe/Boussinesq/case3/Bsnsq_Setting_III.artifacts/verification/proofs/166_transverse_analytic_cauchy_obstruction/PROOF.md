# An analytic transverse trace excludes an outgoing endpoint

Status: CONFIRMED local conditional theorem by an independent complete proof,101 exact controls,2 negative controls and a checked written actual Opus5.5 review. The proof was written before controls. This strengthens164 by replacing finite transverse degree with two explicit analyticity conditions. It remains a local conditional theorem.

## 1. Statement

Let (u,v) be oriented orthonormal physical Cartesian coordinates centered at0. Suppose W is C-infinity on a full rectangle, divW identically equal to a positive constant D, W(0)=0, and partial_v W_v(0)=D. Its normal nullcline v=k(u) is a smooth graph. Suppose this graph consists of equilibria for u<=0 near0 and the reduced field W_u(u,k(u)) is strictly positive for u>0 near0.

Assume:

1. There exist u0>0 and one open interval I containing0 in its interior, with (0,u0) times I inside the original rectangle, such that for every u in (0,u0), curlW(u,.) is real analytic on I and vanishes on a nonempty open subinterval J_u of I.
2. The two value traces a_i(v)=W_i(0,v) are real analytic near v=0.

These assumptions are incompatible. The analytic interval in condition1 must connect the vanishing subinterval to v=0. No joint analyticity of W on a full neighborhood, no analytic u dependence, and no analytic Neumann trace is assumed.

For a full smooth beta2 B2 profile with a smooth outgoing endpoint, the vanishing subintervals are supplied by162/164: Omega=-curlW vanishes on the local outgoing side, and every small physical u>0 meets that side in a v interval. Choose u positive along the outgoing reduced drift. In these physical coordinates the strong unstable curve is u=h(v), with h(0)=h'(0)=0, and its outgoing side is u>h(v). For every fixed sufficiently small u>0, continuity of h gives an open v interval containing0 inside that outgoing side and inside I. This is the same positive u side as the nonzero reduced drift. The outgoing region itself need not be a half-plane. The spatial normal-form change used in162/164 preserves the original flow time. Thus the profile cannot satisfy both the transverse analyticity of curl and the analytic value-trace condition stated above.

## 2. Harmonicity on the positive side

For each fixed u>0, the analytic identity theorem in v makes curlW zero on the whole common interval. Constant divergence and the exact Cartesian identities

    Delta W_u=partial_u divW-partial_v curlW,
    Delta W_v=partial_v divW+partial_u curlW

make both components harmonic on a positive half-rectangle. No uniform complex analyticity radius as u tends0 is needed for this identity-theorem step.

## 3. Reflection of a harmonic function with analytic value trace

Fix a scalar component H=W_i and let a(v)=H(0,v). Extend a holomorphically to a disk around0 in the complex v plane. Its Taylor coefficients are real. For real u,v close to0, define

    A(u,v)=[a(v+iu)+a(v-iu)]/2.                     (1)

This is real valued, real analytic and harmonic, with A(0,v)=a(v). On the positive half-rectangle put Q=H-A. It is harmonic and smooth up to u=0, with Q(0,v)=0. Define the odd reflection

    Q_tilde(u,v)=Q(u,v) for u>=0,
    Q_tilde(u,v)=-Q(-u,v) for u<0.                  (2)

Here all claims of boundary smoothness can be checked directly. Along u=0, Q=Q_v=Q_vv=0. Harmonicity from the positive side and continuity give Q_uu=-Q_vv=0 there. The one-sided derivatives of(2) through order2 match: Q_u and Q_uv are reflected evenly; Q, Q_v, Q_uu and Q_vv are reflected oddly, and their boundary values are zero. Hence Q_tilde is C2 on a smaller full rectangle. It is harmonic on both sides and on the boundary, so it is harmonic on the full rectangle. Harmonic functions are real analytic. Therefore

    P_i=A+Q_tilde

is a real analytic extension of H from the positive side through0.

This is a direct C2 reflection argument. It does not use a well-posed smooth elliptic Cauchy problem, and it does not assume analyticity of the normal derivative. The latter follows for the positive-side trace after extension. Applying the construction to both components yields an analytic vector field P that agrees with W for u>0 near0. It need not agree with W for u<0. Smoothness nevertheless makes all jets of W and P at0 equal.

## 4. The equilibrium arc must continue

The analytic normal component P_v has partial_v P_v(0)=D!=0. The analytic implicit-function theorem gives its normal nullcline as an analytic graph v=k_P(u). On u>0, uniqueness of the normal graph makes k_P equal to the original smooth k. Thus the smooth reduced function

    f(u)=W_u(u,k(u))

is zero for u<0 and equals the analytic function f_P(u)=P_u(u,k_P(u)) for u>0. Every derivative of f at0 is zero, and hence every derivative of f_P at0 is zero. Analyticity forces f_P to vanish identically near0, contradicting strict positivity beyond0. This proves the theorem.

Only nonvanishing of the reduced field beyond0 is needed in this last step. The application to B2 uses outgoing dynamics to supply condition1 and does not address the incoming or accumulating alternatives.

## 5. Scope

A velocity polynomial of uniformly finite degree in v, with smooth u coefficients, satisfies both analyticity conditions, so164 is a special case. A further explicit sufficient hypothesis is that W and partial_u W extend holomorphically in v to a common complex neighborhood, with smooth real-u dependence there. This ensures transverse analyticity of curl and the value traces. That hypothesis is not derived from the B2 equations.

The proof does not assume that differentiating an arbitrary pointwise transversely analytic smooth family in u preserves analyticity. Instead it states the analyticity of curl separately. Nor can the value-trace assumption be replaced by a bound on the single jet at0: flat jets are compatible with nonanalytic traces on a neighboring interval.

No finite Gevrey estimate, joint analyticity of an arbitrary smooth B2 field, global inverse, parity or far field is proved here. The broad smooth B2 question and the quantitative flatness question under its full endpoint hypotheses remain OPEN. The theorem identifies a conditional obstruction, not a numerical failure of finite angular approximation.

Dependencies: the analytic identity theorem, exact Cartesian differentiation, formula(1), the explicitly checked C2 reflection, harmonic analyticity and the implicit-function theorems. The B2 application imports only the independently checked local outgoing-side harmonicity of162/164. No numerical fact is a premise.

Written UTC 2026-10-21T12:30:50.488476+00:00, before controls. The earlier correct proof with both Cauchy traces is preserved in verification; the analytic Neumann-trace assumption has been removed by the explicit odd reflection argument.

Review precision UTC 2026-10-21T12:35:14.112749+00:00: the positive divergence is explicitly constant; the real interval I and u range are common; the physical curved outgoing side supplies J_u on the positive reduced-drift side. Actual Opus267 confirmed the analytic-value-only reflection and the right-side nullcline argument. Its B2 upstream vanishing premise was not independently re-audited in that response; it is supplied by162/164 and their earlier checks.
