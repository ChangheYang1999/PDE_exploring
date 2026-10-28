# Independent cross-audit of V239 (proof 224, scaled cutoff errors) and V240 (proof 225, jet graph completion)

## Files and hashes audited

- V239: verification/proofs/224_scaled_holder_patching/PROOF.md, SHA256 a4c29a53aade5ddc442f7ba2359a46c28d5adbff8926c2e20c434344d7619ce4 (recomputed with sha256sum; matches the requested hash and evidence/check.json).
- V240: verification/proofs/225_jet_graph_completion/PROOF.md, SHA256 caf020f92b59c98b9e464c830e089861f80d9af2554fd89e36fecd7451511fc3 (recomputed; matches the requested hash and evidence/check.json).
- All dependency hashes listed in the two check.json files match the current PROOF.md files: topics 213 (29c5fe9c...), 214 (77e47e53...), 215 (e2379986...), 216 (db542813...), 217 (a4a9e82a...), 222 (d5a1747b...), 223 (30980d7f...), 01 (f0e20786...), 33 (60905882...), 204 (5254cc9a...).

Read in full for this audit: both proofs and their check.json, topics 01, 202 (statement and cutoff definitions), 204, 213, 215, 216, 217, 222, and the INDEX entries for the cited topics. I also read the earlier cross-audits xaudit_V227.md (proof 216) and xaudit_V235.md (proof 222) to see which known caveats the new proofs inherit.

Note on citations in the request: the origin inverse actually used by V239 is the full-column extension A_delta of proof 217 (built on the factorization of proof 215 and the characteristic inverse of topics 202/203). It is not cited as "topics 203 to 207". The proof's own citations are correct.

## Verdicts

VERDICT V239: PASS WITH REMARKS

VERDICT V240: PASS WITH REMARKS

I found no gap and no mathematical error in either proof. All findings below are remarks, notation issues or citation refinements. None affects a claimed statement.

## Summary of the arguments checked

V239. The noncompact sequence consists of flow-box packets that oscillate transversally to the flow: u_n(F(s,z)) = n^(-alpha) eta1(s) theta(z) cos(nz) in exact flow-box coordinates (V.grad s = 1, V.grad z = 0). They are reflected to the physical parities and corrected by -c[u_n] q to get exact c = J = 0. The transport differentiates only eta1. So u_n and T u_n are uniformly C^alpha, supported in a fixed compact set off the axes, and hence uniformly bounded in Z. The supremum tends to 0. With a = V.grad chi, the vertical two-point quotient of a h_n at Q and Q_n = Q + (0, pi/n) tends to 2|a(Q)|/(x0^2 pi^alpha) in the local E2 factor. For a box outside B2 the same holds in a scaled annular C^alpha seminorm, with an extra factor R_j^(alpha-beta). Since Z-convergence implies local uniform convergence and a h_n tends to 0 uniformly, no subsequence converges in Z. The nonlocal part [C0,chi] h_n tends to 0 in Z by estimate (1), which uses only ||h||_infinity on a fixed support. Estimate (1) splits into four pieces: the kernel (chi(Y)-chi(X))K(X-Y) for the local Holder norm; separation and parity on the axis strip for the x^2-weighted seminorm; dipole decay r^(-3) of U[chi h] for the far annuli and the weighted L2 norm (for every gamma > 4k); and boundedness of c on fixed off-origin supports for the rank-one M0 part. The patch identity (A0 K - chi eta) f_n = [A0,chi] h_n is exact, with f_n = A_delta h_n bounded in Z.

V240. The completion statement is the standard fact that an unbounded linear functional has dense graph, made explicit with the unit-J, graph-null packets k_epsilon. The image identity J(A0 h) = 0 is an exact jet computation. It uses the normalization 3 ell0 - c[rho0] = 1 and J(M0) = 1.

## Findings

### V239 (proof 224)

1. REMARK (mechanism; no repair needed). Location: "Exact transverse packets". The packets h_n are themselves graph-bounded with no Z-convergent subsequence: ||h_n||_infinity tends to 0 while [h_n]_(y,2) is at least about 2/(x0^2 pi^alpha). So the noncompactness of [T,chi] is the noncompactness of the graph embedding D_Z -> Z, localized at Q by the coefficient a. This explains why the result says nothing about sums of patches. In a partition of unity the coefficients V.grad chi_i add to zero, but they multiply different local solution operators, so whether they cancel depends on how the patches are assembled. The proof correctly makes no claim either way.

2. REMARK (notation; suggested repair). Location: "A particular full-column origin patch". The proof renames the full-column extension A_delta of proof 217 (2) as L_delta. In proof 215, L_delta and B_delta denote the H0-normalized extension and coupling chi(X/delta)(U[h]+c[h]X/3).grad rho0. The identity "V_delta.grad u = u + eta f - B_delta u" needs the full coupling chi(X/delta){U[u].grad rho0 + c[u]M0}, which is never defined under the name B_delta in this topic. The mathematics is correct because the proof does say it uses the exact full extension. Repair: write B_delta^M for chi(X/delta){U[.].grad rho0 + c[.]M0} and L_delta^M = A_delta of proof 217.

3. TYPO (overloaded symbol and wording). Locations: "The complete nonlocal commutator..." and "Exact statement". The letter K denotes both the patch operator chi R_delta eta and the compact support set in (1), with constant C_K. "The fixed compact support of h_n" should read "a fixed compact set containing the supports of all h_n", because the zero sets of cos(nz) vary with n. "A regular analytic flow box Q = (x0,y0)" conflates the point and its box. "Separated from x=0 and the origin" is redundant. Repair: rename the support set (for example Sigma) and adjust the wording.

4. REMARK (support conventions; implicit but correct). Location: patch section. Proof 202 defines the coefficient cutoff chi(X/delta) to be 1 on B_(delta/2) and supported in B_delta. I checked that this matches the proof's statement. For V_delta = V and chi(X/delta) = 1 on a neighborhood of supp chi, supp chi should be a compact subset of the open disk B_(delta/2). The coupling part of f_n lies in the closed disk of radius delta, where eta = 1 by continuity, so eta f_n = f_n. Also chi eta = chi, so the error operator is simply A0 K - chi. Repair: state these explicitly.

5. REMARK (unneeded strength). Location: "An integration by parts in z gives c[u_n] = O(n^(-alpha-1))". The bound is correct. Because the amplitude is smooth and compact in z, it actually holds to every order. However the trivial bound |c[u_n]| <= C||u_n||_infinity = O(n^(-alpha)) already suffices, since the strain kernel is bounded on the fixed support. Every later use needs only c[u_n] -> 0 and a bounded correction.

6. REMARK (intermediate annuli and quasi-convexity; fill-in). Location: the paragraph proving the far components of (1). The proof handles the axis strip, the local E2 factor and the far radius where chi = 0. It leaves implicit the finitely many annuli in between. Those follow from the global C^alpha bound for W (also proved there) and the bounded Lipschitz gradient of rho0. For the scaled seminorm on a far annulus A_j, the derivative bound must be integrated along paths inside A_j of length comparable to |X-X'|. This works because the annuli are quasi-convex, or one can split at |X-X'| ~ R_j using the supremum. The result is R^alpha [W.grad rho0]_(C^alpha(A_j)) <= C||h||_infinity R^(k-4). Repair: one sentence each.

7. REMARK (weighted bound; an improvement over V227, correctly scoped). The weighted L2 part of (1) uses the pointwise bound O(r^(k-4)). Its square integral against w_gamma converges whenever gamma > 2k-6, a condition that is always satisfied. This removes the gamma < 2 dependence of proof 216 (9), which used proof 214's weighted multiplier bound. The graph boundedness of the packets still uses boundedness of C0 on Z for all gamma > 4k (proof 222). That boundedness carries the caveat of xaudit_V235 Finding 6: for gamma >= 2, proof 214 is applied only through its E2 part with an auxiliary weight. The caveat is resolved there and does not affect V239.

8. REMARK (lower bound for boxes outside B2). Location: end of "Exact transverse packets". The dichotomy is complete. If |Q| < 2, then Q and Q_n lie where the Z cutoff equals 1, and the E2 quotient applies. If |Q| >= 1, some A_j contains Q in its interior because the annuli overlap, and the scaled seminorm gives the lower bound R_j^(alpha-beta) 2|a(Q)|/pi^alpha. Repair (optional): display this constant.

9. REMARK (scope sentence). Location: "What would close a global construction", the sentence "It does refute obtaining that conclusion from local inverses and individual cutoff compactness without further proof." What is proved is the following. For any cutoff with a regular off-axis point where V1 != 0 and V.grad chi != 0, the individual commutator is noncompact, and the specific origin patch has noncompact error. A Fredholm conclusion could still come from small-norm errors or from cancellation in an assembled error, and the preceding sentence of the proof says so. The hypothesis is close to generic: a nonzero compact chi cannot be flow-invariant, and V1 != 0 can be relaxed to V != 0, as noted in xaudit_V227 remark 3. That genericity is not proved in this topic. Repair (optional): add "for cutoffs satisfying the flow-box hypothesis".

10. REMARK (right inverse versus injectivity; verified, no repair). Suppose K: Z -> D_Z is graph-bounded and E = A0 K - I has norm below 1. Then A0 K (I+E)^(-1) = I, so K(I+E)^(-1): Z -> D_Z is a bounded right inverse and A0 is onto Z. Nothing in this implies ker A0 = 0. A separate lower bound ||h||_Z <= C||A0 h||_Z on D_Z, or a left inverse, is needed. A two-sided parametrix modulo compacts (the left one compact on D_Z with the graph norm) gives Fredholmness by Atkinson's theorem, and index and kernel remain to be analysed. The proof states exactly this.

### V240 (proof 225)

11. REMARK (abstract content). The density argument (choose v_n = h_n + (j - J(h_n))k_n) is correct, and the isometric identification with G_sm (+) R in the l^1 sum norm follows because i is isometric with dense image in a complete space. The argument uses nothing about A0 beyond closedness, S subset of D_Z, and unboundedness of J on (S, ||.||_G), which the packets supply. It is the general fact that the graph of an unbounded linear functional is dense in X x R. The definition of G_sm as the closure of S (not D_Z intersect ker c) means no density assumption is hidden. Repair (optional): cite the general fact.

12. REMARK (citation for the actual-field packets). Location: "Topics204/222 give an explicit sequence k_epsilon". Proof 204 proves the transport-image estimate only for the frozen and localized operators, and proof 222 refers back to proof 204. The estimate for the actual global field V and the actual k_epsilon is in proof 214, and proof 217 transfers it to A0 (xaudit_V235 Finding 3 records the same point). The self-contained sketch in V240 is correct. It needs V in C^2 near 0, which proof 33 supplies, so that V1(eps X')/(eps x') and V2(eps X')/eps are uniformly C^1 on the support. Repair: add topics214/217 to the citation.

13. REMARK (possible strengthening). Location: statement, "cannot create a stronger Banach function domain". One could add that the image of the completion in D_Z is G_sm, and its quotient norm is inf_j(||g||_G + |j|) = ||g||_G. So the construction returns exactly the original graph space, with no stronger function norm. This sharpens the sentence and needs no new argument.

14. REMARK (implicit degree counting in (2)). Location: "The exact image cubic coefficient...". The jet computation uses three facts that the proof leaves implicit. First, parity excludes quadratic terms, so U[rho0] = c[rho0](-x,y) + O(r^3) and U[h] = c[h](-x,y) + O(r^3). Second, h = J x^2 y + O(r^5), because even-x, odd-y, axis-vanishing smooth functions have only the odd-degree monomials x^(2a) y^(2b+1) with a >= 1. Third, rho0 - x^2 y = O(r^5) and U[zeta] = c[zeta](-x,y) + O(r^3) (proof 217). Every remainder product is then O(r^5) and cannot reach the x^2 y coefficient. I checked each of these facts. Repair: one sentence.

15. REMARK (scope of "where it is defined"). Location: end of the image section. For a general g in G_sm the pointwise cubic jet of A0 g need not exist, and J o A0 is not continuous on Z. But J(A0 h) = 0 holds on all of S, which is dense in G_sm. So any extension of J o A0 that is continuous, or even closable, from S vanishes identically, and no extension can recover the abstract label. The proof's conclusion is therefore robust. Repair (optional): say so explicitly.

16. TYPO (minor). The proof writes "ell" for ell0 in "3ell-c[rho0]=1" and "diag(ell-c[rho0],ell+c[rho0])". The "annular" q of the packet section is proof 204's q_raw/c[q_raw] with q_raw = x^2 y beta(r). It meets both axes but vanishes on x = 0, so it lies in S's ambient class, as needed.

## What I verified independently, and how

- Hashes: recomputed SHA256 for both proofs and for every dependency listed in the two check.json files.
- Cubic jet identity (sympy, inline). With the transport linear part diag(ell-c0, ell+c0) acting on J x^2 y and minus the identity, the x^2 y coefficient is J(3ell - c0 - 1). With velocity c_h(-x,y) acting on x^2 y, the coefficient is -c_h. For M0, (X.grad x^2y + c_z(-x,y).grad x^2y)/(3-c_z) has coefficient exactly 1. The total is identically 0 after substituting c0 = 3ell - 1. I also re-checked proof 01's cancellation (c(-x,y) + cX/3).grad(x^2 y) = 0.
- Sign of the strain linear part (sympy). For K1 = -xy/(pi r^4), d_x K1 evaluated at -Y equals -sin(3 theta)/(pi r^3). So d_x U1(0) = -c[h], consistent with DU(0) = diag(-c,c) of proof 01 and with the linear part c[h](-x,y) used in V240.
- Exact constants (Python Fractions). k = 1615536043799051/2^53, about 0.179361, and ell0 = 1/k, about 5.57536. A = 2ell0 - 1, about 10.1507, and D = 4ell0 - 1, about 21.3015, are both positive, with D - 2A - 1 = 0 exactly. Also 2k - 1, about -0.6413, is below k. The far exponent k - 4 - beta is below -3.17 over the whole beta range, and 2k - 6 < 4k. So all far and weighted exponents in V239 (1) have the claimed signs.
- Dipole decay (numerical, inline). For a four-point source with the physical parities (zero mass, nonzero y-moment), R^3 |U(R,theta)| with the IPM kernels K1 = -xy/(pi r^4) and K2 = (x^2-y^2)/(2 pi r^4) converges to 0.254648 (= 0.8/pi, the dipole moment over pi) at three angles for R = 10 to 10^4. This confirms the r^(-3) decay used for the far components of (1).
- Packet Holder bounds (numerical, inline). For g_n = n^(-alpha) theta(z) cos(nz) with alpha = 0.6 and n = 10, 40, 160, the sampled C^alpha quotient stays at about 1.1 while the supremum falls from 0.25 to 0.048. The two-point quotient at z = 0 and z = pi/n tends to 2/pi^alpha, about 1.0063. This matches the uniform bound and the lower-bound limit in V239.
- Normalization integral (sympy). The integral of sin(3 theta) cos^2(theta) sin(theta) over a period is pi/4, which gives proof 204's c[q_raw] formula. I also checked c[h_epsilon] = epsilon^2 c[H] by homogeneity.
- By hand, V239:
  - flow-box diffeomorphism (det DF(0,0) = V1(Q));
  - reflection equivariance of T under the physical parities;
  - uniform C^alpha and Z bounds of u_n and T u_n;
  - exact c = J = 0 after the q correction;
  - the two-point E2 quotient and the annular alternative;
  - the subsequence argument via local uniform convergence;
  - parity cancellation of the canonical subtraction constants for compact inputs;
  - the d(1+|log d|) kernel commutator estimate;
  - the axis-strip division a1 W1/x + a2 W2;
  - the rank-one M0 term;
  - membership of chi u in D_Z for u = R_delta eta f;
  - the identities eta f_n = f_n and R_delta f_n = h_n (uniqueness in the maximal E2 domain);
  - the exact formula (A0 K - chi eta) f_n = [A0,chi] h_n;
  - the construction of an admissible Q near the saddle: V.X = -A x^2 + D y^2 + O(r^4) < 0 for |y| < (A/D)^(1/2)|x| small, so V1(Q) != 0 and chi'(r) V.X/r != 0.
- By hand, V240:
  - S subset of D_Z via (V.grad h)/x^2 = (V1/x)(h_x/x) + V2 (h_y/x^2);
  - scaling of the E2 seminorms of h_epsilon: epsilon^3, epsilon^(3-alpha), epsilon^(1-alpha);
  - closedness of G_sm and c = 0 on it;
  - isometry and density of i;
  - kernel of the projection;
  - uniqueness of the continuous extension of A0;
  - density of S intersect ker J and the limit k_* with J(k_*) = 1.

## Scope I consider proved

V239 (proof 224). Fix 0 < alpha < 1, 2k-1 < beta < k and gamma > 4k, with Z, C0 = U[.].grad rho0 + c[.]M0, A0 = T + C0 and D_Z as in proof 222.

Let chi be any smooth compact cutoff, even in both coordinates, and suppose some point Q off both axes, in a region where V is smooth, has V1(Q) != 0 and (V.grad chi)(Q) != 0. Then:
- Multiplication by a = V.grad chi, which equals [T,chi], is bounded but not compact from D_Z with its graph norm into Z.
- The same holds for the full commutator [A0,chi], including the rank-one M0 column.
- Both statements hold for every gamma > 4k.
- Noncompactness is witnessed by graph-bounded smooth compact inputs h_n with c[h_n] = J(h_n) = 0 and ||h_n||_infinity -> 0.
- On these inputs [C0,chi] h_n -> 0 in Z, including the local E2, scaled-annular and weighted components.

For the explicit patch K = chi R_delta eta:
- R_delta is the inverse of proof 217's full-column origin extension A_delta, delta is small, chi is radial and compactly supported in B_(delta/2), and eta is radial, equal to 1 on B_delta and supported in B2.
- K is bounded Z -> D_Z.
- A0 K - chi eta (which equals A0 K - chi) is bounded but not compact on Z.

The following elementary implications are also correct: a graph-bounded K with ||A0 K - I|| < 1 gives surjectivity but not injectivity, and two-sided compact parametrices give Fredholmness. Not proved, and not claimed:
- anything about sums of patches or cancellation between them;
- the middle-annulus assembled error;
- smallness of any error norm;
- Fredholmness, injectivity or invertibility of A0 on Z;
- transfer of the proof 220/221 range obstructions to Z.

V240 (proof 225). With S = smooth compact physical-parity functions vanishing on x = 0 with c = 0, and G_sm their closure in the A0 graph of D_Z:
- The completion of S in ||h||_G + |J(h)| is isometric to G_sm (+) R (sum norm) via h -> (h, J(h)).
- Its natural map to functions is (g,j) -> g, with kernel exactly {0} (+) R.
- The continuous extension of A0 is (g,j) -> A0 g, which annihilates {0} (+) R.
- S intersect ker J is graph-dense in G_sm. In particular its closure contains smooth k_* with actual cubic coefficient 1, and the subspace j = 0 of the completion projects onto all of G_sm.
- For every smooth compact physical-parity h vanishing on x = 0, including c[h] != 0, A0 h has an ordinary cubic jet and J(A0 h) = 0. So the image jet carries no information about J(h).

This rules out only the naive augmented completion. It says nothing about stronger norms that control actual derivatives, divided cofactors, a jet remainder or a Sobolev trace, and it makes no claim about invertibility of A0 on Z.
