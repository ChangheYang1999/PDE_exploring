Independent independent cross-audit of V266 (proof 238, actual source transport cokernel)
==============================================================================

Auditor: independent team. Date: 2026-10-28, audit finished about 16:40Z.
Mode: read only. No computation was run and no scratch files were created.

Audited SHA256 values
---------------------
proofs/238_actual_source_transport_cokernel/PROOF.md
  50aa29671cde2ac758224786dd616c9e87efc3dee083a2b89832a1aa4e90c136
  (matches the expected value; checked at the start (16:31Z) and again at the end (16:37Z))
proofs/238_actual_source_transport_cokernel/evidence/derivation.json
  4364759f15d9e1af69b914d09ee35d7c1494a2560aa1e3bd4adf2be0016ceef5
  (its proof_sha256 field equals the PROOF.md hash above)

All dependency hashes listed in derivation.json were recomputed on disk and match:
  209_source_transport_conjugacy/PROOF.md   5a89be22b6bc70743ba7b4cbc9a527f4e9f66d428b1cb871eff1c381e8d681e1
  79_actual_global_zero_set/PROOF.md        0627393740d8604dc55bd4110a400127f35c939fc4edeb6c783847ed1ad7e4c2
  88_robust_zero_geometry/PROOF.md          f50036125da8ee431b162b4ad748b9e74093128e4d165e9978cf7b2c6a09f1ed
  228_scaled_quadratic_axis_space/PROOF.md  dc9ffef502b399f2b914f4a8846d4c40a282a988ca81d6c920a2ddafbcd31d3e
  236_joint_cofactor_holder_space/PROOF.md  58369aa93dbfd1dd90cf8b305f3a1ab3f143dbb38bb2359fbf2b57e59049688e
Other files read but not in the manifest (for reference):
  15_modal_source/PROOF.md                         20071e87df00c49ddbcc4d5c2dc8552c354c33b2802dcc6c2bc05e55f1f7a16d
  223_scaled_exterior_inverse/AUDIT_CLARIFICATIONS 7fdb58074127898c3859f57f4f975cd303d820a05755ee8811a051b240394e58
  228 AUDIT_CLARIFICATIONS.md                      420f095e3d828d1e06ea3109296f16f85ca0d57d8e2784789f9fcdac08f7cd34
  236 AUDIT_CLARIFICATIONS.md                      70e23e8d0307f37cb315baec5bc2b8fcbdb77d752b82a585180d673d802026e8
  (236's clarification file is dated 16:30, after 238's derivation at 16:24. 238 uses only the
  norm definition (1) of 236 PROOF.md, which the clarifications do not change.)
Also read: 209 AUDIT_CLARIFICATIONS.md, 223 PROOF.md, 227 PROOF.md and clarifications, 60 statement,
210 statement, 01 strain formula, INDEX.md entries.

VERDICT: PASS WITH REMARKS

Every load-bearing step is correct. All the remarks below are MINOR (notation, citation and
manifest completeness). None of them affects the theorem.

Summary of what was checked
---------------------------
(a) Cusps. With B=diag(A_s,mu_s), a=1/A_s and b=mu_s/A_s, direct differentiation confirms
(A_s s d_s + mu_s y d_y - 1)[s^a phi(y/s^b)] = 0 on s>0. The constants are used correctly. Proof 15
gives A_s+mu_s=2/k and mu_s in (0.99999997745,0.99999997750). Then A_s = 2/k - mu_s, about 10.1507,
so 10<A_s<51/5, 5/51<a<1/10 and 0<b<a. These also satisfy proof 209's hypotheses (1)
(99/100<mu<1, 10mu<A<11mu). The proof uses the local conjugacy Psi of 209, i.e. (2) there,
DPsi V = B Psi, and not the cutoff map Phi_delta. Since b>0, u_phi vanishes identically near every
point of {s=0} except the origin, so u_phi is smooth on R2 minus the origin and continuous at it
(since a>0). The derivative bounds |d_s u|<=C s^(a-1) and |d_y u|<=C s^(a-b) are correct on the
support |y| ~ s^b. Local C^a follows: use the derivative for d<=s/2, the supremum otherwise, and
Lipschitz in y (because a>b). The two-point test (s, v0 s^b) vs (0, v0 s^b) correctly shows that
u is not C^alpha for alpha>a, and this failure survives the C^1 change of variables.

Off-axis norm control (1) is correct. P=(p,0) with p about 8.6 (proof 79 bracket), so chi (supported
in B4) vanishes near P, and the annular pieces N_4 (Z2) and M_4 (Z3) control the full C^alpha norm on
a small disk K. In Z2 this uses one horizontal and one vertical step, and the factor x^2 ~ 74 is
harmless. In Z3 it uses h=x^2 g. The quadratic-axis and cofactor conditions are vacuous for all
objects built here, because everything vanishes near the vertical axis.

(b) The product rule gives f_phi = T H_phi = (V.grad chi_s o Psi)(u_phi o Psi). It is supported in
the annulus where chi_s varies, where u_phi is smooth. So f_phi is C^infinity and compactly
supported (V is analytic on the certified 1/1000 disk of 209). It has even-x parity because V is
equivariant under x -> -x, and odd-y parity because chi_s is radial, Psi is y-equivariant and phi is
odd. It vanishes near both axes and the origin, so it lies in Z2, in Z3 and in both maximal domains.
J(f_phi)=0 because f_phi vanishes near 0. c[f] = (1/pi) int f y(3x^2-y^2)/r^6 (proof 01) converges
absolutely. phi -> c[f_phi] is a linear functional on the infinite-dimensional space E, and its
kernel still has infinite dimension.

(c) The uniqueness lemma is correct. w = v - H_phi is continuous, satisfies T w = 0 in D'(R2), and
obeys |w| <= C|X|^beta outside a disk (from the Z2 and Z3 annular sup norms). Proof 79 states
explicitly that every open-quadrant orbit escapes to infinity in forward time. Proof 88 is used only
in its unperturbed case. The axes are invariant and V is globally Lipschitz and C1 (proof 52).
d log r/dt = ell + O(r^(k-1)) gives r_t ~ exp(ell t), and both the upper and lower comparisons are
available, which handles negative beta (note 2k-1 is about -0.64). The flow-box step works as
follows: pull back by a C^1 flow box (with mollification/Friedrichs as needed), giving
d_tau(e^-tau w~)=0 in D'; then continuity yields w(X)=exp(-t)w(Phi_t X) on every orbit. The endpoint
is O(exp((beta/k-1)t)), which tends to 0. So w=0 on the open quadrants and, by continuity,
everywhere. In particular the kernel of T on D_Z is trivial. The proof correctly works in the
larger continuous class, since H_phi is not in Z.

(d) If T v = f_phi with v in D_Z, then v = H_phi, so H_phi would be in Z. That contradicts (1) and
the two-point test when phi != 0. Linearity of phi -> (H_phi, f_phi) and the uniqueness step show
that phi -> [f_phi] is injective into the algebraic quotient. This gives infinitely many
independent classes, with no closed-range assumption.

(e) The scope is correct. The result is transport only, alpha>1/A_s, with no statement about A0,
Lren, F0, alpha<=1/A_s or profile existence. It is consistent with proof 210's Riesz-term source
inverse: the -gM term changes the effective damping, so there is no conflict.

Numbered findings
-----------------
1. MINOR (derivation.json, "scope" field). "strictp<beta<k" uses p in proof 228's meaning p=2k-1.
   PROOF.md uses p for the source abscissa P=(p,0). This repeats the notation clash already flagged
   in proof 227's clarification 2. Needed: write "2k-1<beta<k" (PROOF.md already states it
   correctly). Not load-bearing.

2. MINOR (derivation.json dependency manifest). Not hashed:
   - proof 15, cited in the text for the source quantities A_s, mu_s, A_s+mu_s=2/k;
   - proof 52, for the global Lipschitz/C1 property, U=O(r^k) and the axis parities;
   - proof 223 clarification 4, the C1 flow-box identity behind (5);
   - proof 60, the planar limit-set argument behind proof 79's escape statement.
   Proof 79's hashed statement already contains the escape conclusion, and the remaining facts are
   either re-derived inline or standard. Needed: add these hashes for traceability. Not load-bearing.

3. MINOR (Uniqueness section, "smooth flow boxes"). V is only finitely differentiable globally:
   C1 by proof 52, with C6-type knot joins. C1 flow boxes suffice, and the "almost every transverse
   parameter, then continuity" argument given is exactly the one in proof 223 clarification 4.
   Needed: say "C1" and cite 223 clar. 4. Not load-bearing.

4. MINOR (Scope and dependencies, "proof 228 gives the far growth bounds used to identify the
   terminal value"). The pointwise bound |h|<=C||h|| |X|^beta comes from the norm definitions
   (228 (5); 236 norm comparisons). The actual-V radial comparison r_t ~ exp(ell t) is 223 (3)-(4);
   228 uses the time-changed field W. The proof re-derives the needed comparison inline from
   U=O(r^k), so nothing is missing. Needed: correct the attribution. Not load-bearing.

5. MINOR (Compact actual weak solutions). Two facts are used implicitly and should be stated:
   - the even reflection to the disk about -P needs V1 odd in x and V2 even in x, so that
     T commutes with x -> -x (topics52/88);
   - the conjugacy chart, and hence supp H_phi and supp f_phi, is chosen inside the certified
     1/1000 analytic disk of proof 209, which is what makes f_phi C^infinity.
   Both hold. Not load-bearing.

6. MINOR (Exact local homogeneous solutions, weak-derivative check). The "W^(1,1) plus zero trace
   across s=0" justification is valid but terse. A cleaner statement: u_phi is bounded, smooth on
   R2 minus the origin, and has L1_loc gradient. A single point is removable for distributional
   first derivatives of bounded functions in 2D (the cutoff error is O(eps sup|u|)). So the
   distributional and pointwise derivatives agree and (3) holds in D'(R2). Not load-bearing.

7. MINOR (role of b<a). The condition b<a, equivalently mu_s<1, holds by a very small margin:
   a-b = a(1-mu_s) is about 2.2e-9, but it is strictly positive. It is used only for the sharpness
   statement that u_phi is C^a (Lipschitz in y). The obstruction itself uses only continuity
   (a>0), W^(1,1) (a+b>0), the exact equation (3) and the two-point test, so it would survive
   without b<a. Needed: optionally note that the C^a assertion is informational. Not load-bearing.

Scope paragraph
---------------
The confirmed result is as follows. For the actual normalized modal trial and the exact source
P=(p,0), for every 1/A_s<alpha<1, 2k-1<beta<k and gamma>4k, the transport operator T=V.grad-1
alone, on its distributional maximal domain in Z2 (proof 228) or Z3 (proof 236), has an
infinite-dimensional algebraic cokernel. The representatives are smooth, compactly supported,
physical-parity forcings supported near +/-P with exact c=J=0. The mechanism is the exact
homogeneous source cusp s^a phi(y/s^b) carried by the verified conjugacy of proof 209, together with
uniqueness by forward quadrant escape (proof 79) and the terminal growth condition beta<k.

The audit does not cover, and the proof does not claim:
- any cokernel or non-surjectivity for A0 or Lren, whose source Riesz term -gM changes the local
  equation (compare proof 210's source inverse, which is consistent with this result);
- any statement for alpha<=1/A_s, where H_phi itself belongs to Z;
- the range of F0, a global inverse on Z3, or profile existence.
The source conjugacy and the certified source constants were taken as previously verified and were
checked only for correct use.
