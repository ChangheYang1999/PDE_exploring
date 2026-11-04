# Recheck of the conditional W2 contact theorems

Status: independent recheck completed; designated verdicts recorded separately. This note supplements the full standalone arguments in the team records and in the team records. Those files state all profile, tail, regularity and escaping-trace hypotheses.

## 1. Exact scope of the derivative conclusion

For the actual C2 zero-helicity Euler profile with natural decay and C1 tail convergence, let w be an escaping lower-window W2 scattering direction, assume the tail V is C2 near w, and write M=DV(w), W=curl V. The nonflat theorem A1255 applies under the additional hypothesis M!=0. It gives DW(w)=0 and D2k(w)=-aM for that contradiction argument. It gives no derivative assertion when M=0. The old Section6 of the auditor's B66 proof placed DW(w)=0 before its explicit nonflat hypothesis. That unqualified transfer was unsupported, for exactly the reason already identified in A2520. The corrected paragraph places it inside M!=0. No conclusion or estimate in the local contradiction changes.

The issue is logical scope, not a counterexample to DW(w)=0 for the full actual-tail class. At a C2 field's zero, DV(w)=0 fixes W(w)=0 but does not fix the second derivatives determining DW(w). B67 correctly avoids this extra premise. Its remaining derivative statements concern boundary points of the open irrotational region, where DW=0 follows from C1 continuity and vanishing on that open region.

## 2. Re-derived contact contradiction and pressure alternative

Fix a=1-2c in (0,1), sigma>0 and the orthonormal transverse coordinates of the full B66 proof. Under M!=0, the strict-rate necessary jets are D2k=-aM and D2S=-4 sigma^2 f tensor f. The rank identity gives 4a sigma^2 tau u^2+o(r^2)=0 on the support, with tau=+-sigma, so |u|<|s| there after shrinking the disc. On the entire punctured disc, |V|>=sigma r/2. These facts do not assume the conclusion.

For G=|DV|^2, R=|V|^2 and v_f=V.f, the contact defect Phi=grad S.f-2Gkv_f/R is C1 in u. The four differentiated quotient terms are O(r), -4a sigma^2 s^2/r^2+o(1), O(r), and 8a sigma^2 s^2u^2/r^4+o(1). Thus Phi_u<=-2 sigma^2(1-a)<0 uniformly on a sufficiently small punctured disc. Here k=-a tau su+o(r^2), not o(r^2) throughout the disc. At the two extreme support points on a segment with fixed nonzero s, open ambient irrotational points approach from outside the support. Hence W=DW=0 at both contacts and V!=0. The contact identity sets Phi=0 twice, contradicting its strict decrease. The contact identity itself follows by tracing the local power law and dividing by a quantity tending to (q-1)a^2|V|^2>0. It uses no common component constant.

After M=0 is concluded, the B67 argument uses the distinct contact bound |grad S|<=2|X||DV|^2. At a zero-velocity contact with grad S!=0, differentiating the rank identity gives rank DV<=1; symmetry and zero trace force DV=0. The resulting zero two-jet permits C2 harmonic pasting of k from open irrotational regions. This yields the scalar relation bS grad k=ak grad S on a connected neighbourhood. Near a regular zero of S it has k=C_+-|S|^(a/b), and C1 regularity with 0<a/b<1 forces both constants to vanish.

At a zero-gradient point, H=D2S is symmetric, trace free on the transverse plane and annihilates X. A supplied nonzero-velocity contact sequence gives Hh_n=o(|h_n|), so H has a transverse kernel and is zero. Without that sequence, H!=0 gives a transverse saddle and |grad S|>=sigma_H r/2, excluding such contacts by the quadratic contact bound. On central-orbit boundary points the boundary condition, not M=0, supplies DW=0. Harmonic pasting then produces regular zeroes of S accumulating at w, each interior to {k=0}. Therefore H!=0 implies w in closure(int{k=0}). These are exactly the alternatives already confirmed in A2515-A2519.

All characteristic uses are finite local flowbox uses, with X nonzero. Rotation contributes invertible orthogonal factors. Constants and radii may depend on c, omega and local bounds. No pressure renormalization is introduced; P2 retains its established tail normalization. The C2 tail hypothesis is not supplied by the natural estimates. The conclusion is finite-jet T0, not infinite flatness or unrestricted nonexistence.

## 3. Comparison and evidence limits

All six sections of in the team records were read against the two full auditor proofs, and the A1255 statement and full proof Section3 were reread. The mathematical comparison agrees after the auditor's own scope correction in Section1. The Theory Agent B  report references identify the right passages in pin d8799b6e, but their section numbers are transposed: lines4453-4460 belong to Section7, whereas lines4944-4960 belong to Section10. This is a locator typo, not a changed theorem.

The complete reduced-example script was read, not run. It checks a degree14 truncation of the angular analytic solution, the resulting equation to finite series orders, and the leading failure (W.grad S)(1,0,z)=5z^2+O(z^3). A script alone is not execution evidence; no corresponding captured output was supplied in the inspected scratch directory. It does not exit nonzero for a false printed Boolean. The independent analytic example and its scope were already confirmed in A2623-A2625 and transferred in A2648; this recheck supplies no new computation or full-system counterexample.

Existing configured model comparisons of B66 and B67 remain part of the earlier full proofs. The new Theory Agent B  comparison is the configured model agent, not an independently attested model execution. No new model client or agent was used. The captured sources and timestamp are in the team records.
