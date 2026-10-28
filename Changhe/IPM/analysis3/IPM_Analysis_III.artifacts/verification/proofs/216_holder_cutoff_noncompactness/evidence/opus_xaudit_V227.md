# Independent cross-audit of V227 (proof 216, noncompact Holder cutoff errors)

Proof audited: verification/proofs/216_holder_cutoff_noncompactness/PROOF.md

SHA256 (sha256sum, computed at audit time): db542813246227d26da1b2f24cd0994e253f7a2a8ac0f34b138ed4fb8d40472f

This matches proof_sha256 in 216_holder_cutoff_noncompactness/evidence/check.json and the hash in the VERIFICATION_RECORD V227 record. The five dependency hashes in check.json (topics 202, 212, 213, 214, 215) match the current PROOF.md files on disk.

Read: proof 216 PROOF.md and evidence/check.json, proof 213, proof 214, proof 215, proof 212, proof 202 PROOF.md files, the opening of proof 199 (canonical velocity and its far subtraction), the V227 record in VERIFICATION_RECORD.md, and xaudit_V226.md. No computation was run. Every check below was done by hand.

## Verdict

**PASS WITH REMARKS.** I found no mathematical gap. The flow box is a genuine local diffeomorphism, the packets satisfy the uniform bounds (4) in C^alpha, E2 and L2(w_gamma), and the transport image is bounded because V.grad equals partial_s in the box coordinates. The strain correction gives c = J = 0 exactly. The two-point quotient (8) uses the correct weighted vertical seminorm of E2 and gives a positive lower bound on ||a h_n||_Y while a h_n tends to 0 uniformly. This excludes every convergent subsequence. The nonlocal commutator bound (9) is correct and uses only ||h||_infinity on a fixed support, so (13) holds. That suffices for the full commutator. The parametrix identity (14) is exact, f_n is bounded in Y, eta f_n = f_n, and R_delta f_n = h_n by uniqueness in the maximal domain. The scope statements do not overclaim. The remarks below concern hypotheses that are stronger than needed, a notation clash, the domain of the general identity E = [L_ren,chi] R_delta eta, and wording.

## Checks

### 1. Flow box and the packets u_n: PASS

F(s,z) = Phi_s(x0, y0+z) has DF(0,0) with columns V(Q) and (0,1), so det DF(0,0) = V1(Q). If V1(Q) != 0 the inverse function theorem gives a local diffeomorphism of the regularity of the flow. Differentiating F(s+t,z) = Phi_t(F(s,z)) at t = 0 gives partial_s F = V(F). So V.grad = partial_s in these coordinates, which is (3). On the stated analytic radial interval the finitely many angular modes of the stream function solve radial ODEs with analytic forcing, so V is analytic there and F is smooth.

In box coordinates g_n = n^(-alpha) eta1(s) theta(z) cos(nz) has sup C n^(-alpha) and gradient C n^(1-alpha). Splitting differences at 1/n gives a uniform C^alpha bound. Composition with the fixed Lipschitz map F^(-1) keeps it. The transport image is (partial_s g_n - g_n) composed with F^(-1), and partial_s falls only on eta1. So T u_n has the same structure and the same bounds. The reflected copies are disjoint because Q is off both axes. V has the physical parities (V1 odd in x, even in y; V2 even in x, odd in y), so V.grad commutes with the reflections and T u_n on each copy is the reflected copy of T u_n on the first box. The compact supports lie inside the box, so extension by zero preserves C^alpha.

E2: the x seminorm and sup are ordinary Holder quantities. For the weighted vertical seminorm, every vertical line meeting the support has |x| >= b > 0, so [u]_(y,2) <= b^(-2)[u]_(C^alpha). Lines missing the support contribute nothing, and u_n(0,y) = 0. This is proof 213's compact-support comparison. Weighted L2 is at most the sup times the square root of a fixed weighted volume, so it is O(n^(-alpha)). Thus u_n and T u_n are bounded in Y. V.grad u_n is classical and equals the distributional derivative, so u_n is in D_Y. The graph norm ||h||_Y + ||L_ren h||_Y is bounded because C_ren is bounded on Y (proof 214).

### 2. Strain, correction and J: PASS

The kernel sin(3 theta)/(pi r^3) is even in x and odd in y, so the four copies contribute equally. On each box it is smooth. After the change of variables the amplitude k(F) |det DF| eta1 theta is compactly supported and C^1 in z, so one integration by parts in z gives (5) with no boundary term. This needs F of class C^2, which holds. The trivial bound |c[u_n]| <= C ||u_n||_infinity = O(n^(-alpha)) already suffices for every later use (Remark 1).

The function q exists. Take a small box in the open first quadrant where sin(3 theta) has fixed sign (for example near theta = pi/6), disjoint from the axes and the flow boxes. Reflect a positive bump evenly in x and oddly in y. The four contributions to c have the same sign, so c is nonzero, and one divides by it. q vanishes near the origin, so J(q) = 0. q is compactly supported and smooth, so q and V.grad q are in Y. Then c[h_n] = c[u_n] - c[u_n] c[q] = 0. J(h_n) = 0 because h_n vanishes on a neighborhood of 0. ||h_n||_infinity = O(n^(-alpha)), and h_n is graph-bounded. q vanishes on the whole flow box, in particular at Q and Q_n.

### 3. Noncompactness of multiplication by a: PASS

Multiplication by a fixed compactly supported, even-even, Lipschitz coefficient preserves Y. Proof 213's argument for radial eta works verbatim. Use the product identity with the undifferenced h at a supported endpoint, and the bound |h(x,y)| <= [h]_(y,2) x^2 |y|^alpha, which follows from oddness in y. The coefficient a = V1 chi_x + V2 chi_y is even in both variables, and it is C^1 because V is C^1 on supp chi. The distributional Leibniz identity V.grad(chi h) = chi V.grad h + a h holds for continuous h and V in C^1, so chi preserves D_Y and (7) holds.

At Q = F(0,0) and Q_n = F(0, pi/n), with eta1(0) = 1 and theta = 1 near 0, we get h_n(Q) = n^(-alpha) and h_n(Q_n) = -n^(-alpha) for large n. The two points share x = x0 and differ by pi/n vertically. The E2 vertical seminorm is exactly sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha), which is the quotient in (8). Its numerator is n^(-alpha)|a(Q)+a(Q_n)|, its denominator is x0^2 pi^alpha n^(-alpha), and the ratio tends to 2|a(Q)|/(x0^2 pi^alpha) > 0. Here x0 != 0 makes the weight finite. Hence ||a h_n||_Y >= c > 0 for all large n. On the other hand ||a h_n||_infinity <= ||a||_infinity ||h_n||_infinity -> 0, and convergence in Y implies uniform convergence. So any Y-limit of a subsequence would be 0, which contradicts the lower bound. The argument is complete.

### 4. The nonlocal commutator: PASS

[L_ren,chi] = [T,chi] + [C_ren,chi] = a + [C_ren,chi], and the displayed formula for [C_ren,chi] is correct. The local multiplier part of U2 commutes with chi. For compactly supported parity inputs the canonical far-subtraction constants of proof 199 vanish: the U1 kernel at -Y is odd in x against an x-even input, and the U2 kernel is even in y against a y-odd input. So W is given by the absolutely convergent kernel (10), and the principal value is not needed.

Bound (11): the near-diagonal piece over the two disks of radius 2d contributes C d. Off those disks, with xi on the segment, |xi - Y| >= |X - Y|/2 and |D_X G(xi,Y)| <= C |xi - Y|^(-2), from both the grad chi term and the (chi(Y)-chi(xi)) DK term. This gives C d (1 + |log d|). Bound (12): on |x| < b/2 every source point is at distance at least b/2, so all derivatives of W are bounded uniformly in y. Oddness gives W1(0,y) = 0, so W1/x and its y derivative are bounded. With a1 = rho0_x/x and a2 = rho0_y/x^2 bounded with bounded y derivative (proof 212 (17) near 0, compact joins, proof 214 (10) far out), the divided coupling a1 W1/x + a2 W2 has bounded y-Holder seminorm. For |x| >= b/2 use (11) and x^(-2) <= 4/b^2. Vertical pairs share x, so these two cases cover all of them. The weighted L2 bound uses proof 214's L2(w_gamma) bound for U. The strain terms are bounded by C_K ||h||_infinity because K is away from the origin.

The question was whether the argument proves compactness or only convergence along the sequence. It proves (13) along this sequence, since ||h_n||_infinity -> 0. That suffices: if [L_ren,chi] h_(n_j) converged in Y to g, then a h_(n_j) = [L_ren,chi] h_(n_j) - [C_ren,chi] h_(n_j) would converge to g, contradicting Check 3. Boundedness of [L_ren,chi] on D_Y follows from boundedness of a, chi and C_ren on Y.

### 5. Local parametrix: PASS

Take R_delta = L_delta^(-1) from proof 215 (2) (Remark 6). On B_(delta/2), V_delta = V and chi(X/delta) = 1. With chi0 = 1 there, B_delta h = U[h].grad rho0 + c[h] X.grad rho0/3 = U[h].grad rho0 + c[h] H0. So L_delta and L_ren agree pointwise on supp chi. For g = R_delta eta f, V.grad(chi g) = chi(T_delta g + g) + a g with T_delta g = eta f - B_delta g. Every term is a compactly supported E2 function, hence lies in Y. So K: Y -> D_Y is graph-bounded and E is bounded on Y.

h_n is supported in B_(delta/2): the boxes and q are placed there. T h_n = T_delta h_n is supported in B_(delta/2). B_delta h_n = chi(X/delta) U[h_n].grad rho0 (since c[h_n] = 0) is supported in the closed disk of radius delta. So f_n = L_delta h_n is supported where eta = 1 (by continuity on the closed disk), and eta f_n = f_n. ||f_n||_E2 <= ||T h_n||_E2 + ||B_delta|| ||h_n||_E2 is bounded, and compact support gives the weighted L2 bound. h_n lies in the maximal domain D_delta, and L_delta is bijective there, so R_delta f_n = h_n. Then E f_n = L_ren(chi h_n) - chi L_delta h_n = L_ren(chi h_n) - chi L_ren h_n = [L_ren,chi] h_n. This is (14). Since f_n is bounded and E f_n has no convergent subsequence, E is not compact. The construction of Q near 0 is correct. V = (-A0 x, D0 y) + O(r^3), because the parities exclude quadratic terms. For |y0| small relative to |x0|, X.V < 0, so V.grad r != 0 and V1(Q) != 0, and a radial chi with chi'(r(Q)) != 0 gives a(Q) != 0.

### 6. Scope: PASS

The statement restricts itself to the explicit operator K = chi R_delta eta and to commutators with fixed cutoffs. It disclaims global invertibility and its failure, smallness of the assembled error, flow-adapted partitions, other graph topologies and direct global inverses. The proof supports exactly these conclusions.

## Findings

1. (remark) The integration by parts behind (5) is correct but not needed. The kernel is bounded on the fixed support, so |c[u_n]| <= C ||u_n||_infinity = O(n^(-alpha)). That already gives c[u_n] -> 0 and a bounded correction, which is all that (6), (8) and (13) use.

2. (remark) The regularity actually used is weaker than analyticity. V in C^1 near Q gives the flow box, (4), the Leibniz identity and the C^1 coefficient a. V in C^2 gives (5). C^infinity is used only so that h_n lies in S = C_c^infinity, where J is defined. In any case J(h_n) = 0 because h_n vanishes near 0. The analytic-interval hypothesis is sufficient, and it is stated and checked correctly.

3. (remark) The mechanism is the noncompactness of the graph embedding D_Y -> Y. The same h_n are graph-bounded, tend to 0 uniformly, and satisfy [h_n]_(y,2) >= 2/(x0^2 pi^alpha). Multiplication by a only localizes this at Q. Consequently hypothesis (1) is close to generic. V1(Q) != 0 can be replaced by V(Q) != 0, using a horizontal transversal and the x seminorm when V1(Q) = 0. Also, if a is not identically zero, then by continuity there is a nearby point with a != 0, V != 0, off the axes and off the radial joins. This makes the scope disclaimer conservative, not an overclaim. It also explains why the proof points to flow-adapted partitions (V.grad chi = 0) as the natural escape.

4. (remark) Bound (9) proves more than convergence along this sequence. Y-bounded inputs supported in a fixed compact K off the vertical axis are precompact in the sup norm (Arzela-Ascoli, using the local C^alpha control of proof 213). So (9) makes [C_ren,chi] compact on such inputs. The proof neither claims nor needs this, nor compactness of [C_ren,chi] on all of D_Y. The subsequence argument in Check 4 is the correct and sufficient logic.

5. (remark) The general identity E = [L_ren,chi] R_delta eta needs R_delta eta f to lie in D_Y. Proof 213 deliberately does not assume that the uncut origin inverse preserves L2(w_gamma), so this is not known for general f. The proof uses the identity only on f_n, where R_delta f_n = h_n lies in D_Y, so (14) is valid. For general f the meaningful form is E f = a g + (U[chi g] - chi U[g]).grad rho0 + c[chi g] H0 - chi c[g] H0, with g = R_delta eta f in E2. Every term is defined on E2.

6. (cosmetic) In proof 202, R_delta denotes the characteristic inverse S_delta^(-1) of (5). In proof 216, R_delta denotes the full inverse L_delta^(-1) of proof 215 (2). The step R_delta eta f_n = h_n requires the latter. One sentence fixing this notation would remove the ambiguity.

7. (cosmetic) "A neighborhood of Q and its four reflections is disjoint" should say three reflections, giving four disjoint copies, and the hypothesis is automatic for Q off both axes. "Separated from the vertical axis and the origin" in (9) is redundant. In "Its transport image is compact in Y", "compact" means compactly supported, not a compact operator or a compact set.

8. (cosmetic) supp chi should be a compact subset of the open disk B_(delta/2), so that V = V_delta on a neighborhood of supp chi and the distributional identity chi V.grad g = chi V_delta.grad g is immediate. supp f_n lies in the closed disk of radius delta, and eta = 1 there by continuity. Both points are implicit in the proof.

9. (cosmetic) The bound for T u_n on the reflected copies implicitly uses the reflection equivariance of V, which follows from the physical parities. It could be stated.

10. (cosmetic) "A successful scheme must estimate or otherwise invert its actual transport error" is correct for schemes built on this patch K. Reading it as "a successful scheme using this patch" matches the scope sentences elsewhere in the proof.

11. (remark) The argument also gives a positive explicit lower bound ||E|| >= 2|a(Q)|/(x0^2 pi^alpha sup_n ||f_n||_Y). The proof does not compare this with 1. Its statement that small norm is not ruled out is therefore accurate.

## Scope summary (quotable)

Proof 216 (V227) is correct. Take any fixed smooth compact even cutoff chi with V.grad chi != 0 at a regular off-axis point Q where V1(Q) != 0. Then multiplication by a = V.grad chi, which equals the transport commutator [T,chi], and the full commutator [L_ren,chi] are bounded but not compact from D_Y with its graph norm into Y = E2 intersect L2(w_gamma). Smooth compact graph-bounded packets with c = J = 0 witness this. The nonlocal commutator tends to 0 in Y on these packets and cannot cancel the transport lower bound. For the explicit origin patch K = chi R_delta eta, the residual E = L_ren K - chi eta is bounded but not compact on Y. The result shows only that the cutoff error of this construction is not automatically compact. It proves nothing about small norm of that error, flow-adapted partitions, other graph topologies, global invertibility or its failure, or profile existence.
