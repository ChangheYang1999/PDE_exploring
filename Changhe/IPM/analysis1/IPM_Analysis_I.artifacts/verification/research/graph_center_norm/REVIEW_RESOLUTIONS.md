# Review resolutions

2026-10-21. The first review was actual Claude Opus5.5, stop end_turn, request84a6fedb-5e81-4ec2-bf98-e2a428730bd2. It accepted the estimates with explicit scope and wording requests. The original proof has been preserved.

G1. D_L is a real linear subspace containing every h_delta. Each h in D_L has a continuous even-even factor in h=x^2 y a near the center and J(h)=a(0). This makes J real-linear and J(h_delta)=1. Factor continuity is a property of each element; it is not continuity of J as a functional on the graph norm. The phrase closed under addition in the original proof is redundant with linearity, and the construction uses all real scalar multiples.

G2. The explicit inner stream polynomials and exterior harmonic modes match through radial derivative6. Therefore U[h_delta] and its first derivatives agree across r=delta; polar coordinates are smooth there. The density h_delta itself is C5, including across its support boundary. Products with locally C2 rho and with the assumed C1 V have the weak derivatives used in the argument. The compactly supported transport term and its first derivatives have zero traces at the boundary. Thus no derivative measure occurs at the support boundary. No regularity of V outside a neighborhood of the unit disk is used for this compact term.

G3. Membership of a scaling candidate K in D_L is a separate hypothesis. In particular C^{2,alpha} of rho and its continuous cubic factor do not by themselves give a continuous factor for rho-X dot grad rho. The counterexample and hypotheses of research/scaling_index/PROOF.md remain in force. Nonzero K means a nonzero X equivalence class.

G4. The bump velocity is the explicit canonical Green inverse. It satisfies the specified Poisson equation, density symmetries, regular origin condition and decay at infinity. In the specified stream mode class n=2,4, the difference of two canonical solutions is a homogeneous radial combination a_n r^n+b_n r^(-n). The origin excludes b_n, and the absence of added growing harmonic strain excludes a_n. Equivalently the canonical inverse is the fixed Green formula, so no independent affine velocity is being chosen. Uniqueness here is only within that stated canonical class; no unspecified larger class is invoked.

G5. The result is for X as the image norm and ||h||_X+||Lh||_X as the domain topology. It does not apply automatically to a norm that controls the central factor, a stronger image space, a narrower domain that excludes the bumps, or a numerical row norm with no link to X. It does not assert closedness, Fredholmness or a global inverse for L.

G6. All near-disk velocity and global density derivative bounds are explicit background hypotheses. The constants in ADDENDUM.md show finiteness and dependence; no values of A,B,D for the numerical profile have been certified here.

S1. ADDENDUM.md proves the equality of admissible inverse constants before and after imposing J=0 by graph-density and norm continuity. It does not require a kernel. The kernel obstruction is its conditional special case.

Computation correction. The first symbolic check used expand on a rational expression after substituting r^2=x^2+y^2. Its unsimplified polynomial denominator caused an exact equality test to fail. Applying exact cancel gave zero residual. Expanding the divisible radial polynomials before substitution repairs the symbolic test without changing formula(4), the proof or any numerical datum. The failed source and error are retained as evidence/attempt1_source.py.txt and evidence/attempt1_failure.txt. A different rational polynomial dictionary implementation reconstructs all sources directly and agrees exactly.
