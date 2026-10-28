# Binding clarifications after the independent audit

Date: 2026-10-28T16:39:27.741213+00:00. The original proof is unchanged. The complete actual audit is saved as evidence/opus_audit.md.

1. The transport-only parts need the stated Z3 space and local norm comparisons. The full A0 and Lren parts also use bounded C0 and Cren on Z3. Those hypotheses are now independently confirmed: proof 234 by V265 and proof 236 by V268, with their binding clarifications. The audit's reference to an awaiting V257 audit describes its earlier status and is now resolved. No global inverse hypothesis has been added.

2. For a selection S of preimages, set v0=S(0), which belongs to the maximal domain and satisfies Lv0=0. Then S(N(a_n))-v0 is itself a maximal-domain preimage of N(a_n). The rescaled bound(2) gives ||S(N(a_n))-v0||Z3>=b_L. This proves the claimed failure of continuity of the composition at zero even if S(0) is a nonzero kernel element. It does not infer failure from the mere fact that each selected preimage has a norm bounded below.

3. The actual velocity is equivariant under both coordinate reflections: V1 is odd in x and even in y; V2 is even in x and odd in y. This transports the flow coordinates to all reflected boxes with V.grad z=0. The construction uses a small open first inner cell separated from its boundaries and the origin. The exact finite radial Green formulas are smooth there, and the nonlocal contributions from its complement are smooth there by elliptic locality. Thus V and the local flow coordinates are smooth on the chosen box, as needed for smooth strips; C3 already suffices for the estimates. Choose the tube and tau before n so that both trajectories z=0 and z=1/n stay in its smaller closed part for0<=s<=tau. There eta=1, grad d=0, and the compensator and its derivatives vanish. Only the first box is used for the positive two-orbit lower bound.

4. To avoid notation conflicts in a restatement, call the oscillatory strips s_n instead of k_n and the fixed tube time tau_box. The exponent k and the exterior cutoffs of proof 236 are unchanged. This is a naming clarification only.

5. The nonlinear parity is exact: U1 is odd-even and h_x is odd-odd, while U2 is even-odd and h_y is even-even. Both products are even-odd. Since c[h_n]=0, the scalar velocity contribution vanishes. For every fixed n the image is smooth and compact in the same off-axis set, so the full Z3 membership follows from(3), including its weighted L2 part.

The full independent audit finds no gap. The result refutes continuity of this semilinear graph-to-target map and of its preimage composition when defined on these images. It does not refute stronger derivative norms, a quasilinear iteration or existence, and does not prove a global linear inverse.
