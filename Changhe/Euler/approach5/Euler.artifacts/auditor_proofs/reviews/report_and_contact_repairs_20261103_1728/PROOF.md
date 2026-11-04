# Closed-threshold report edits and contact-point repairs

## 1. Snapshot and scope

This review concerns the report assembled at 17:17Z and pinned at 2026-11-03T17:27:02.501361Z, together with the five B files listed in the team records. It is a delta review against the previously audited 17:09Z report and the B62 sources. The report has 6219 lines and SHA256 cf7823419bc26344d66736a45779507780a127e6aff764c727843dc82a9347ed. Its published-copy file is identical. The 91-line report diff, 12-line README diff, and all five B diffs were read completely. The attempts and obstruction files have no changes against the recorded baselines. Coordinator Note99, received subsequently, supplies a newer report; it requires its own audit.

## 2. Closed nonlinear-weight threshold

For 0<c<2/3 and every real omega, suppose U in C2 and P in C1 solve the rotating profile equation on R3 with div U=0, U bounded and U(R.) tending to zero in distributions. Define h_c and t_c by the singular scalar initial-value problem in A1720-A1725, and T(c)=sqrt(t_c). The correctly stated conclusion is U=0 if sup|curl U|<=T(c), including equality. This is conditional on the global vorticity bound, which already implies bounded vorticity; no derivative-decay assumption is added. The proof is A1782-A1785: the limiting nonnegative density first pins the strain to h_c'(|W|^2)(W tensor W-|W|^2 I/3). This yields bounded DU before A492 is used. The resulting decay and the cubic divergence identity remove the equality case. Neither the report nor README reverses this order.

The strict monotonicity and the bracket 1.004<T(2/5)<1.01272 match A1786-A1789. The earlier twenty rational brackets are unchanged. The phrase sharp threshold is explicitly restricted to Lemma NW. Its admissible weights require a strictly positive density, so the assertion that no such weight reaches t_c is consistent with a limiting nonnegative weight at the closed endpoint. Other weight families and an a priori vorticity bound from bare decay remain open. Thus the changed Theorem8, tables, summary and README correctly integrate the closed endpoint.

## 3. Extended angular-frequency integrals

Under the local Poisson and mean-comparison assumptions of A1764-A1766, the angular index ell>=1 gives r M' <=(ell-1)K and K<=M/kappa. Integrating the resulting scalar differential inequality excludes a nonzero infinitely value-flat germ when the upper logarithmic mean of ell is finite. A1801-A1802 allow the nonnegative integral of (ell-1)/r to be extended-valued: an infinite integral on any smaller annulus gives the necessary divergence immediately; otherwise ordinary integration on finite annuli yields it. The canonical choice max(1,(sqrt(1+4 A/N)-1)/2), with ell=1 where N=0, is measurable and satisfies the angular-energy inequality. The revised report row uses precisely this statement. It does not infer a finite frequency bound from the tail equations.

## 4. Nonzero contact and derivative regularity

Let X=(cI-omega J)x, L=(1-c)I+omega J, a=1-2c, b=2-2c, W=curl V, k=X.V and S=P2-|V|^2/2. The homogeneous velocity relation is DV X=-LV. At a nonzero-velocity contact z, DV(z) cannot vanish: otherwise the invertible matrix L would kill V(z). Thus the positive denominator |DV(z)|^2 in the contact formula is justified.

All revised contact statements now explicitly impose V(z) nonzero, W(z)=DW(z)=0 and membership in the closure of the vortical set, with the C2 Poisson/rank hypotheses of A1729. These yield grad S=2|DV|^2 k V/|V|^2 and the stated scalar quotient. Being off the central orbit implies V nonzero only in the separately established nonflat branch. The flat branch no longer uses that invalid implication. The change appears in LemmaW2.14, TheoremFP(12), REPORT_SECTION_B and THEOREM_B_SUMMARY.

For the C1 homogeneous irrotational-component lemma, W is merely continuous. The revised source now places DW(z)=0 inside the C2 qualification: W vanishes on the adjacent open irrotational component, so DW does also, and continuity transfers it to z. The global maximum principle itself still needs only C1 V. It applies for 1/3<c<1/2, every finite omega, and an open set fully saturated by the linear dilation-rotation flow, with V zero on its relative boundary. The proof and the singular c=1/3 endpoint countertest are A1792-A1794. The local no-bubble consequence retains the A1733 equality-rate, outside-closure-Z and full-saturation premises; it means that a component's quotient closure meets the outer transverse boundary.

## 5. Hessian identity and pressure bootstrap

The corrected I17 parenthesis is explicitly the supported nonflat contradiction branch. The general formulas are

    D2k[h]=-a DV h+(Ah) cross W+X cross DW h,
    D2S X=-(bI+A^T)grad S.

At the branch in question W=DW=0, hence D2k=-a DV. The first differentiated rank identity gives (DV h) cross grad S=0 for every h. The rank-two saddle then forces grad S=0, so D2S X=0 is used only after it is established. At C3 the second differentiated rank identity gives (DV h) cross (D2S h)=0; proportionality and the trace contradiction exclude DV nonzero. This is the valid order of A1735-A1738 and A1797.

The pressure simplification is also valid. If V is C3 near the point, -tr((DV)^2) is C2 there. The Poisson equation and interior Schauder regularity give P2 in C3,alpha on smaller neighborhoods for every alpha<1. Consequently the R3 extra premise can be stated as V in C3 alone. Under the natural tail bounds A539 already gives P2 in C2,alpha, so the R2 extra premise is V in C2. The revised B copies agree with A1799.

## 6. Qualifications still missing in this report snapshot

The LIT257 row still states M=-mean P and -P>=kappa|V|^2 without P(x0)=0. The pressure-shift counterexample in A1818 refutes that local wording: a flat shear with constant pressure -1 has zero acceleration and is nonzero arbitrarily close to the flat point. The invariant repair is M=P(x0)-mean P and P(x0)-P>=kappa|V|^2. At a common flat tail point P2(x0)=0 supplies the normalization separately.

The Hardy row still needs the weak stress equation and local integrability of quadratic products as premises, in addition to the stated time norms. The W2 row still labels escaping-direction conclusions as local structure for 0<c<1/2; those conclusions use the helicity-free natural-profile class and 2/5<c<1/2. The B58 equality-rate premise and historical prose-body updates remain pending in this snapshot. These are A1819-A1821, not new refutations of the underlying conditional theorems. Note99 says they are repaired; that newer delta is not covered by the present verdict.

## 7. Verification and limitations

The delta review confirms the new closed-threshold, extended-integral and B-source repairs at their exact scopes. It does not approve the whole report while Section6 remains. Source pins and complete diffs are retained in verification. Dependencies are the standalone proofs referenced above; no new numerical computation or formal build was run. File exchange with the configured model agents continues; actual provider runtime remains independently unattested. The main bare-decay, arbitrary-helicity conjecture for every omega remains open.
