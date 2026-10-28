# The local coupling commutator with a smooth variable order

## Statement

Use the actual normalized modal trial, X_s, C_R, b, p and chi of proof 123, and the order reductions A_v,A_u of proof 144. Set v=h/b, u=chi h/(bp), w=A_v v and z=A_u u. Let R=grad<D>^(-1) on the cylinder. Define the real symmetric matrix

 P(X)=R_theta^T [[-rho_y,rho_x/2],[rho_x/2,0]] R_theta,

where R_theta rotates cylinder covectors to Cartesian directions. Thus the principal coupling symbol is nu^T P nu. The matrix is bounded and tends uniformly to zero at both cylinder ends. Fix the escape coefficient N in A_v,A_u. For every eta>0 there is a compact linear map J_eta:X_s->L2(C) plus L2(C) such that

 |Re<A_v(C_R h/b),w>-<P Rw,Rw>|
 +|Re<A_u(chi C_R h/(bp)),z>-<P Rz,Rz>|
 <=(eta||h||_(X_s)+||J_eta h||_(L2 plus L2))||h||_(X_s).  (1)

Increasing a constant or rescaling J_eta is implicit in (1). Both operations preserve compactness. Equivalently the compact seminorm in (1) can be written ||K_eta h||_(X_s) for a compact operator on the Hilbert space X_s. This confirms Q2 of the theory author's Proposition Hs; no lower-order norm term is needed for this particular version. All constants and compact maps are qualitative.

## A local commutator lemma

Let q be compactly supported on a cylinder chart and belong to H^(51/8). Let A=Op(e^(N Lambda)<xi>^s), with 41/20<=s<=25/4 as above. Then

 [A,M_q]:H^s->L2

is compact. The analogous assertion holds at constant order25/4. Here compact support can be replaced by fixed cutoffs on the input and output.

First, multiplication by q is bounded on H^s, with norm controlled by ||q||H^(51/8), by the product estimate proved in proof 123. Also H^(51/8) embeds in L-infinity, so multiplication by q is bounded on L2. Consequently

 ||[A,M_q]f||_2<=C||q||H^(51/8)||f||H^s.                 (2)

Choose compactly supported smooth q_n converging to q in H^(51/8), with a common compact support. This is legitimate for the localized actual coefficients, which are in H^r for every r<13/2. Equation(2) proves operator-norm convergence of [A,M_q_n] to [A,M_q]. For each q_n the smooth composition formula gives a commutator of relative order at most -1+d, for any fixed d>0. Its kernel is supported near the compact coefficient support up to a smoothing, decaying off-diagonal part. Local Rellich compactness and the summable off-diagonal kernel bound therefore make [A,M_q_n]:H^s->L2 compact. A norm limit of compact operators is compact, proving the lemma. This argument requires no quantitative rate for q_n and no false claim of infinite regularity for q.

If U_0 is a smooth order-zero pseudodifferential operator localized on both sides to this chart, the same smooth composition formula proves

 [A,U_0]:H^s->L2 compact.                                (3)

Its principal scalar symbol commutes with that of A; the remaining terms gain a frequency power, up to logarithms from s. The local chart version of U on a rescaled annulus has precisely this form. Smooth coordinate changes are permitted by the variable-order coordinate invariance checked in proof 123.

Combining (2)-(3), for q as above,

 A M_q U_0 f-M_q U_0 A f
  =[A,M_q]U_0 f+M_q[A,U_0]f                            (4)

is compact H^s->L2. Every term is a bounded operator on the displayed spaces. Formula(4) is an identity on smooth functions and extends by their density in the unconstrained H^s chart space. It does not use a dense normalized core of X_s. The result restricts to X_s because the inclusion of its component into H^s is bounded.

## Principal form and the cofactor

On an annulus away from the vertical axis, the compactly localized bulk coupling is a sum M_q U_0 with the coefficients just considered. Smooth b factors only produce the already covered commutators. The localized normalization strain is finite rank: c is a bounded scalar functional and its localized range lies in H^(51/8). Therefore (4) moves A_v through the coupling modulo a compact L2-valued map.

Near the vertical axis write h=x^2 f and rho=x^2 g on a Cartesian chart whose radial coordinate stays away from zero. Proof 141 proved the exact identity

 (U[h].grad rho)/x^2=rho_x U_1[f]+rho_y U_2[f]+T f,       (5)

where T gains at least1/16 derivative locally at the relevant high regularity. Its proof uses the single and double coordinate commutators and division of an odd double-commutator output by x. Smooth radial and nonzero y factors convert f to the cofactor u. Inputs outside a larger vertical chart have a separated smooth kernel. Thus the cofactor principal operator has the same symbol as the bulk one, and its remainder is locally compact after applying A_u. The exact zero-axis trace is imposed only after subtracting E Gamma_C. That axis map is compact into the unconstrained pair of Sobolev components by proof 140, so it contributes to J_eta. No separate assertion that E Gamma_C maps to the zero-trace X_s is used.

For a smooth compactly supported matrix P, smooth symbol composition shows that its principal operator with symbol nu^T P nu differs from R^* P R by a negative-order operator. Here the inhomogeneous symbol uses xi/<xi> rather than xi/|xi|; their difference is order -2. The difference is compact on L2 after localizing. For the actual H^(51/8) matrix, approximate it by smooth matrices in that norm. The principal operator is a finite sum of bounded smooth order-zero multipliers preceded by multiplication by matrix entries, so convergence in L-infinity gives operator-norm convergence on L2. The same is true of R^* P R. Hence their difference remains compact. This proves the local quadratic form identity. It also avoids any need to take an inverse of A at low frequencies.

In the sector component, Rz is not supported in the sector. Proof 144 permits replacement by a larger angular localization, with a lower-order, locally compact error when the radial support is compact. The cofactor principal identity is therefore valid as a global L2 quadratic form modulo the compact map described above. Nonlocal angular tails have not been silently discarded.

## Global assembly

Choose a smooth radial cutoff chi_c, equal to one on a sufficiently large compact cylinder and supported on a slightly larger one, and put chi_E=1-chi_c. Proof 138 gives

 ||chi_E C_R||_(X_s->X_s)->0

as the cylinder grows. The corresponding statement for the two unconstrained component norms is part of that proof. Applying the fixed bounded order reductions makes the two tail coupling forms at most eta||h||X_s^2 after enlarging the cylinder. Smooth cutoff commutators are harmless; one may simply apply the bound to the already cut output.

The principal form on the output tail is bounded by sup_(tail)|P| times ||Rw||_2^2+||Rz||_2^2. This tends to zero because grad rho=O(r^2) at the origin and O(r^(k-1)) at infinity. Thus only a compact output annulus remains.

On this output annulus, inputs outside a larger radial annulus tend to zero in operator norm by the six dyadic matrices in proof 123. Explicitly, with the output index in a fixed finite set, each of their input tails is a convergent geometric series; their row and column sums tend to zero. The same estimates include all output derivatives up to the required orders. This permits another eta error and leaves finitely many charts with compact input and output support. Apply the local result on these charts and sum the finitely many compact maps. The axis map is compact globally and can be included before this truncation. The end strain cancellation is kept intact in the initial full C_R tail estimate; the strain term is split off as finite rank only after restricting to a compact output annulus.

The finite sum defines a compact map J_eta into the pair of L2 component spaces and proves (1), after allocating eta among the finitely many small errors. If a compact operator on X_s itself is desired, let K_eta=(J_eta^* J_eta)^(1/2). It is compact by the spectral theorem for positive compact operators and satisfies ||K_eta h||X_s=||J_eta h||. This is a norm representation only; it need not preserve a pointwise formula for the two components.

## Scope and dependencies

The proof uses proof 123 (multipliers, coordinate calculus and radial matrices), proof 138 (full coupling tails), proof 140 (axis compactness), proof 141 (cofactor identity and local gain) and proof 144 (order reduction and separated supports). Its smooth symbolic input is Krainer-Mendoza Propositions4.4,4.12 and5.2, already checked against the retained primary source. It closes the local variable-order coefficient issue in Q2 by approximation, not by postulating a quantitative rough symbolic expansion. It does not close Q1, Q5 or the full Hs estimate.
