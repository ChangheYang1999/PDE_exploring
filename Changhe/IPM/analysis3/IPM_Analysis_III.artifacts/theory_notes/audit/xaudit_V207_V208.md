# Independent cross-audit of V207 (proof 203) and V208 (proof 204)

Auditor: independent auditor, by hand only. There were no computations, no servers and no edits outside this file.
Audited files:
- verification/proofs/203_quadratic_holder_endpoint/PROOF.md (SHA in V207: 885960de...)
- verification/proofs/204_holder_graph_normalization/PROOF.md (SHA in V208: 5254cc9a...)

Taken as given, without re-auditing: proof 199 (V203), including its directional bound (3) for U1/x at p<=2; proof 200 (V204); proof 201 (V205); proof 202 (V206). The sibling audits xaudit_V203_V204.md and xaudit_V205_V206.md cover these. I re-derived the p=2 cases that proof 203 imports from topics 25, 200 and 202, because those statements are formally restricted to p<2.

## Verdicts

- **V207 / proof 203: PASS WITH REMARKS.** I found no gap. The band amplitude (4), the dyadic split at lambda ~ 1/delta, the low/high estimates behind (3), the y, x and sup parts of the E_p norm of the coupling, the cutoff-boundary pairs, the p=2 strain column and functional, and both Neumann/maximal-domain inversions are correct. All remarks are cosmetic or informational.
- **V208 / proof 204: PASS WITH REMARKS.** I recomputed every scaling. The conclusion "J is not closable in the L_delta graph topology, even on ker c" follows, with closability in the precise sense stated below. All remarks are cosmetic. Two of them are worth adopting: state J's domain precisely, and state the density form of the kernel conclusion.

## A. Independent checks for V207

A1. Band amplitude (4), j>=1. Write ψ for the enlarged band cutoff. The band kernel of the convolution part of U2 is
K_j(z,y) = (lambda^2/4pi) ∫ ψ(ω)|ω| e^{-lambda|ω||z|} e^{i lambda y ω} dω, and |ω| is smooth on supp ψ. Integrating by parts twice in ω gives
|K_j| <= C lambda^2 e^{-c lambda|z|} (1+lambda|y|)^{-2}. The powers (lambda|z|)^k are absorbed by the exponential. Hence ∫|K_j| dy <= C lambda e^{-c lambda|z|}.
For the identity term, proof 199 (5) gives ||g_j(x,.)||_inf <= CM|x|^p lambda^{-alpha}, since Delta_j has mean zero and [g(x,.)]_alpha <= CM|x|^p.
Then ∫ lambda e^{-c lambda|x-x'|}|x'|^p dx' <= C_p(|x|^p + lambda^{-p}). So (4) is correct. It holds for every p>=0, not only 1<=p<=2.

A2. The j=0 block. (4) is not claimed for j=0, and it is not needed there. The low block enters only through ||d_y U2[g_0](x,.)||_inf <= CM on |x|<=1. The multiplier is iη|η|e^{-|η||z|}η~_0(η)/2 with |z|<=5. It is bounded with a bounded weak η-derivative, so it is in H^1_η, and its y-kernel has uniformly bounded L1 norm. The identity part is d_y η_0(D_y)g, which is a Schwartz kernel applied to g. Correct.

A3. Far-kernel subtraction at X=0. For the compact g=chi_x chi_y h with both reflections, the subtracted constants ∫_{|Y|>1} K_i(-Y)g(Y)dY vanish by parity. K2 is even/even and g is odd in y. K1 is odd/odd and g is even-x/odd-y. So U[g] is the plain L^2 multiplier velocity, and U[h]=U[g]+U[h-g] agrees with the canonical definition. The far input h-g vanishes on [-2,2]^2. Its subtracted velocity has |D^k U^far| <= C||h||_inf on B1 for k=1,2, and U2^far is odd in y. Hence |U2^far| <= CM|y| and [U2^far(x,.)]_{alpha,[-2delta,2delta]} <= CM(4delta)^{1-alpha}. Correct.

A4. Dyadic sums. Take 2^N <= 1/delta < 2^{N+1}.
- Low derivative sum: sum_{j=1}^N lambda^{1-alpha} delta^p <= C_alpha 2^{N(1-alpha)} delta^p <= C_alpha delta^{p+alpha-1}, which is <= C_alpha.
- Second sum: sum_{j>=1} lambda^{1-alpha-p} = 1/(2^{p+alpha-1}-1). At p=2 this is 1/(2^{1+alpha}-1) < 1.

No logarithm occurs anywhere. A log would appear only at alpha=1 (first sum) or at p+alpha=1 (second sum). p+alpha=2 plays no role: integral (8) has no log for any p, and the log at gamma=2 in proof 201 is a pointwise remainder that is not used here. The constants grow like 1/(1-2^{alpha-1}) as alpha->1 and like 1/(1-2^{-alpha}) as alpha->0. That is harmless for fixed alpha.

A5. Oddness bound for the low part. Delta_j and U2 have even symbols in η, so every block is odd in y. The low part is a finite sum of C^1-in-y functions with |d_y| <= CM on |x|<=delta, and it vanishes at y=0. Hence its sup on |y|<=2delta is <= 2CM delta, and its seminorm on [-2delta,2delta] is <= CM(4delta)^{1-alpha}. Correct.

A6. High part, uniform in |x|<=delta. For j>N, lambda >= 2^{N+1} > 1/delta and |x|^p <= delta^p, so (4) <= 2CM delta^p lambda^{-alpha}. This is uniform in |x|<=delta and in y. In the dyadic characterization, the derivative sum over 2^j<=1/d and the supremum sum over 2^j>1/d restricted to j>N are dominated by the full sums. So the global seminorm is <= C_alpha M delta^p, uniform in N. The sup is <= C_alpha M delta^p 2^{-alpha(N+1)} <= C_alpha M delta^{p+alpha}. Since p >= 1 > 1-alpha and delta<1, we get delta^p <= delta^{1-alpha} and delta^{p+alpha} <= delta. So (3) holds.

A7. y-seminorm of the coupling. Write G = chi_delta(a1 V1 + a2 U2), so the coupling is x^2 G.
- chi_delta a1 has sup C delta and Lipschitz constant C, so [.]_alpha <= C delta^{1-alpha}.
- chi_delta a2 has sup C and Lipschitz constant C/delta, so [.]_alpha <= C delta^{-alpha}.

Pair types at fixed |x|<=delta, with y in the support (|y|<=delta):
- y' in [-2delta,2delta]: evaluate the undifferenced U2 at y. The terms are C delta^{-alpha}·CM delta + C·CM delta^{1-alpha}. For the V1 term, use [V1]_alpha, ||V1||_inf <= CM on [-1,1].
- |y'| > 2delta: |y-y'| >= delta and sup|G| <= CM delta, so the quotient is <= CM delta^{1-alpha}.
- Both points outside the support: the difference is 0.

So [G(x,.)]_alpha <= CM delta^{1-alpha}, and [Bh]_{y,p} <= delta^{2-p}[Bh]_{y,2} <= CM delta^{3-p-alpha}. Correct.

A8. Sup and x-seminorm of the coupling. On B_delta, |U1| = |x||V1| <= CM delta, |U2| <= CM delta and |grad rho| <= C delta^2, so sup|Bh| <= CM delta^3.
For the x-seminorm, write Bh = U·W with W = chi_delta grad rho. Then ||W||_inf <= C delta^2 and Lip(W) <= C delta, so [W]_alpha <= C delta^{2-alpha}. Choose X in supp W. The identity F(X)-F(X') = U(X)·(W(X)-W(X')) + (U(X)-U(X'))·W(X') gives [Bh]_x <= CM delta^{3-alpha} + CM delta^2. The second term vanishes unless X' is in supp W, which lies in B1 where [U]_alpha <= CM.
Since p+alpha>1 gives 3-p-alpha<2, both delta^3 and delta^2 are <= delta^{3-p-alpha}. So (1) holds for every 1<=p<=2.

A9. Strain column and functional at p=2.
- H_delta = (x^2/3)chi_delta(a1 + y a2). The coefficient has sup C delta and Lipschitz constant C, so [H_delta]_{y,2} <= C delta^{1-alpha}. Also sup <= C delta^3 and [H_delta]_x <= C delta^{3-alpha}. The power at p=2 is 1-alpha, as claimed.
- |c[h]| <= (4/pi)([h]_{y,2}/(1+alpha) + ||h||_inf) <= (4/pi)||h||_{E_2}. So ||c||_{E_2*} <= 4/pi is correct, since max(1, 1/(1+alpha)) = 1.

A10. Frozen inversion at p=2. Proof 25 (2) is proved for every p>=0, and kappa_2 = 1+2A-D alpha = D(1-alpha). On D(T0) in E_2, ||R0|| <= max(1, 1/(D(1-alpha))), because the x-factor is 1/(1+A alpha) <= 1. Bounded homogeneous solutions vanish. Then L = (I + B_norm R0)T0 on the same domain, with ||B_norm R0|| = O(delta^{1-alpha}). Correct.

A11. Variable inversion at p=2. I checked each ingredient of proof 202 at p=2:
- kappa0 = q0+2-alpha beta0 = (1+2A0-alpha D0)/A0 = beta0(1-alpha).
- (6): the exponent is -(q0+p-alpha L)t.
- (7)-(9): the exponent identity alpha(L+1)+kappa = q0+p+alpha, and a^2 e^{-(q0+2+alpha)t0} <= (2delta)^2 because q0+alpha>0.
- (10): C_R is bounded for small delta.
- (11): the multiplier bound uses p only through |x|^p.
- (12): T_delta = A_delta(S_delta - m_delta) is algebraic. I re-derived it: T_delta - A_delta S_delta = A_delta q0 - 1 = -A_delta m_delta.

The replacement bound ||E_delta|| <= C_M delta^{2-alpha} + (q0 + C_M delta^{2-alpha}) C_norm delta^{1-alpha} is correct. With it, L^{-1} = R_delta(I + E_delta R_delta)^{-1} q_delta on D_delta. Correct.

A12. Sharpness (informational). Fix h = x^2 y chi(r) in E_2, so c[h] = (1/4)∫ r chi dr > 0. Then U = c(-x,y) + O(r^3) is smooth, a1 = 2y + O(r^2) and a2 = 1 + O(r). So G = chi_delta(-c y + R) with R = O(r^2) and d_y R = O(r). The pair (x->0, y = delta/4) against y' = 0 gives [chi_delta U·grad rho]_{y,2} >= c' delta^{1-alpha}. So the power 1-alpha in (1) at p=2 cannot be improved. The same holds for ||H_delta||_{E_2}. Any better rate for (2) would have to come from the normalization cancellation, and proof 203 does not claim one.

## B. Independent checks for V208

B1. The E_2 norm of h_eps = x^2 y chi(X/eps) = eps^3 H(X/eps). Here chi is radial and smooth, equal to 1 on B_{r0}, supported in B1, with 0<=chi<=1.
- Sup: ||h_eps||_inf <= eps^3 max_{B1} r^3 cos^2θ|sinθ| = (2/(3 sqrt3)) eps^3.
- x-seminorm: [h_eps]_x = eps^{3-alpha}[H]_x, and [H]_x < inf because H is C_c^inf.
- y-seminorm with weight |x|^2: |h_eps(x,y)-h_eps(x,y')|/(x^2|y-y'|^alpha) = eps^{1-alpha}|Z_y chi(Z) - Z'_y chi(Z')|/|Z_y-Z'_y|^alpha. So [h_eps]_{y,2} = eps^{1-alpha}[H]_{y,2} exactly.

Letting Z_x->0 and taking the pair (s,0) with s<r0 gives [H]_{y,2} >= r0^{1-alpha}. Hence ||h_eps||_{E_2} is comparable to eps^{1-alpha}: the rate is exact, not just an upper bound.

B2. Transport image.
- Direct differentiation gives T_delta h_eps(eps Z) = eps^3 Z_x^2 Z_y[(-2A_delta+D_delta-1)chi - Z_x A_delta d_1 chi + Z_y D_delta d_2 chi]. This matches (3).
- Frozen case: 1+2A0-D0 = 0, so T0 h_eps = x^2 y chi~'(r/eps)(D0 y^2 - A0 x^2)/(eps r). It is supported in the annulus r0 eps <= r <= eps.
- Variable case: (-2A_delta+D_delta-1)(eps Z) = O(eps^2), and d_Z[A_delta(eps Z)] = eps grad A_delta = O(eps delta). So the bracket has bounded C^1 norm uniformly in eps.

The same scaling as B1 gives ||T_delta h_eps||_{E_2} <= C eps^{1-alpha}. Correct.

B3. Coupling image, checked without using V207 smallness.
- U is order-zero homogeneous, and parity removes the subtraction constants for compact data. Hence U[h_eps](X) = eps^3 U[H](X/eps) and V1[h_eps] = eps^2 V1[H](X/eps).
- V1[H] and U2[H] have bounded sup and bounded global C^alpha_y. On |Z|<=2 this is proof 199 (3) and (11). Outside, the field is smooth and decaying, and U1 is odd in Z_x.
- The product rules of A7 and A8 then give ||chi_delta U[h_eps]·grad rho||_{E_2} = O(delta eps^{2-alpha} + delta^{1-alpha} eps^2 + eps^{3-alpha}) = O(eps^{2-alpha}) for fixed delta.
- The column term is |c[h_eps]| ||H_delta|| = O(eps^2).

So the full image is O(eps^{1-alpha}), and the transport part dominates. V208's route (B_delta bounded on E_2) gives the same conclusion.

B3a. A sharper bound than the proof needs. The scaling in B3 shows the coupling part of L_delta h_eps is O(eps^{2-alpha}), smaller than the O(eps^{1-alpha}) the proof uses.

B4. Strain, J and the correction.
- cos^2θ sinθ = (sinθ + sin3θ)/4. Since ∫ sin3θ sinθ dθ = 0 and ∫ sin^2 3θ dθ = pi, we get c[x^2 y beta(r)] = (1/pi)(pi/4)∫ r beta dr = (1/4)∫ r beta dr > 0.
- Substituting X = eps Z (dX = eps^2 dZ, r^{-3} -> eps^{-3}) gives c[h_eps] = eps^2 c[H] exactly.
- J(h_eps) = 1 because chi = 1 near 0. J(q) = 0 because q vanishes near 0.
- Hence J(k_eps) = 1, c[k_eps] = 0, and ||k_eps||_graph <= C eps^{1-alpha} + eps^2|c[H]| ||q||_graph. This uses eps^2 <= eps^{1-alpha} and the fact that q is C_c^inf, so it lies in D(L_delta).

B5. What closability means here. Let G = (D(L_delta), ||h||_{E_2} + ||L_delta h||_{E_2}). This is a Banach space because L_delta is closed. Let S = {h in C_c^inf(R^2): h even in x, odd in y, h(0,.) = 0}. Every h in S equals x^2 φ with φ smooth, so S ⊂ E_2 and T_delta S ⊂ E_2, hence S ⊂ D(L_delta). Define J: S -> R by J(h) = (1/2) d_x^2 d_y h(0).

J is closable in G if s_n in S, s_n -> 0 in G and J(s_n) -> t imply t = 0. For a linear functional this is equivalent to boundedness, |J(s)| <= C||s||_graph on S.

The sequence k_eps lies in S ∩ ker c, tends to 0 in G, and has J(k_eps) = 1. So J is unbounded, hence non-closable, already on S ∩ ker c, and the graph closure contains (0,1). By V207, L_delta is an isomorphism, so this is the same as saying that f -> J(L_delta^{-1} f) is unbounded in E_2 on L_delta(S ∩ ker c). The conclusion of V208 follows.

## C. Numbered issues

V207 (proof 203):

1. Line 80: "Proof 200 proves that H_delta=chi_delta X.grad rho/3 has E_p norm at most C_H delta^(3-p-alpha)." Proof 200's statement reads "Fix 0<alpha<1 and1<=p<2". Proof 203 does say that the strain functional bound remains valid at p=2, but it does not say this for the H_delta bound. The H_delta proof in proof 200 does not use p<2 (A9). Why it matters: it is a formal dependency gap only. **Cosmetic.** Repair: add "the proof of proof 200's H_delta bound is p-independent and applies verbatim at p=2". The same applies to proof 25: its (2) is stated for p>=0, so p=2 is covered explicitly.

2. Line 48: "Including the low block, the whole low sum has y derivative at most C M." The proof does not say where this holds. The blocks with j>=1 need |x|<=delta; the j=0 block holds on |x|<=1; both hold for all y. Why it matters: readability only. **Cosmetic.**

3. Line 54: "Since p>1-alpha and p+alpha>1, these are bounded respectively by C M delta^(1-alpha) and C M delta." These are the same condition, and the step also uses delta<=1. **Cosmetic.**

4. Line 40: "This proves(4) for every 1<=p<=2." (4) holds for every p>=0. The restriction to 1<=p<=2 is needed only for V1 (proof 199 (10)) and for convergence of sum lambda^{1-alpha-p}, where p+alpha>1 suffices. **Cosmetic, informational.**

5. Line 29: "Its separated far velocity has uniformly bounded derivatives through order2. Its second component is odd in y, so it meets(3)." This is correct, and one derivative suffices. The proof does not say that, for compact g, parity makes the canonical subtraction constants vanish, so that U[h] = U[g] + U[h-g] is consistent (A3). **Cosmetic.**

6. Line 78: "Pairs outside a fixed larger neighborhood are covered by the supported supremum." This is harmless but unnecessary. If the undifferenced velocity is evaluated at the point in supp chi_delta (A8), the other term carries the factor W(X'), which vanishes off the support. The proof should state this choice of identity explicitly, since the O(M delta) velocity bound is valid only on B_delta. **Cosmetic.**

7. Statement, line 5: "for all sufficiently small delta>0". This should be made explicit. Line 61 uses the bounds on B_(3delta), which needs 3delta<=delta0. N>=1 needs delta<1/2, and line 42 shrinks delta below 1/4. **Cosmetic.**

8. Constant dependence. C_alpha grows like 1/(1-2^{alpha-1}) and 1/(1-2^{-alpha}), and the frozen inverse bound max(1, 1/(D0(1-alpha))) blows up as alpha->1. The statement "every fixed alpha<1" is accurate, but no uniformity in alpha holds. **Informational.**

9. The rate in (1) at p=2 is sharp (A12). The un-normalized coupling and the column are each comparable to delta^{1-alpha} for fixed smooth h with c[h]≠0. Proof 203 makes no sharpness claim for (2). **Informational.**

V208 (proof 204):

10. Line 9: "On smooth parity-compatible inputs define J(h)". Parity alone does not force h(0,.)=0. For example y chi(r) has the parities but is not in E_2, since its weighted y-seminorm is infinite. The domain should be S = C_c^inf ∩ E_2 with both parities (B5). Every function the proof uses (h_eps, q, k_eps) lies in S. **Cosmetic.**

11. Line 14: "J has no continuous or closable extension". For a linear functional into R, closable and bounded on its domain are equivalent, so this is one statement, not two. Line 16 defines closability correctly. **Cosmetic.**

12. Lines 14 and 64: "The smooth J=0 subspace is not closed even after imposing c=0". Read literally this is weak: a subspace of smooth functions is never closed in G for trivial reasons. The real content is stronger and should be stated as follows. Since J is unbounded on S ∩ ker c, ker J ∩ ker c ∩ S is graph-norm dense in S ∩ ker c, so J=0 imposes no closed constraint in this topology. Line 64's k_* argument proves exactly the "k_* is in the closure" part. **Cosmetic; wording repair as given.**

13. Line 48: "supported in a fixed annulus strictly inside B_(delta/2)". The placement inside B_(delta/2) is unnecessary; any fixed annulus works. **Cosmetic.**

14. Lines 5 and 44: "with delta small enough for proof 203 to apply" and "a fixed bounded E_2 operator by proof 203". V208 uses only that B_delta is bounded on E_2 and that L_delta is closed. It does not use V207's smallness or invertibility. Boundedness on E_2 already follows from proof 199's endpoint remark ("The same bounded mapping into E_2 holds at p=2") together with proof 200's column and strain bounds at p=2. Direct scaling even gives O(eps^{2-alpha}) for the coupling image (B3). So V208 does not depend on V207's new estimate. **Informational (positive).**

15. Line 31: "Thus ||h_epsilon||_(E_2)<=C epsilon^(1-alpha)." In fact the norm is comparable to eps^{1-alpha} (B1). The rate is exact for this packet, though only the decay to zero is needed. **Informational.**

There are no fatal and no repairable mathematical gaps in either proof.

## D. Five-line summary

1. independent cross-audit of V207 (proof 203) and V208 (proof 204): both PASS WITH REMARKS. No fatal or repairable gap; all 15 remarks are cosmetic or informational.
2. V207: the U2 band bound CM lambda^-alpha(|x|^p+lambda^-p) (j>=1), the j=0 block and the far part (parity kills the subtraction constants) all check out. The dyadic sums converge with no log at p+alpha=2. The low part (Lipschitz CM, odd) gives sup CM delta and seminorm CM delta^(1-alpha). The high part has C^alpha_y CM delta^p and sup CM delta^(p+alpha), uniformly in |x|<=delta.
3. V207: full E_p norm of the coupling: sup CM delta^3, x-seminorm CM delta^2, y-seminorm CM delta^(3-p-alpha), including cutoff-boundary pairs. At p=2 the column is O(delta^(1-alpha)) and ||c||<=4/pi. The frozen (kappa2=D(1-alpha)) and variable (kappa0=beta0(1-alpha)) Neumann inverses hold on the same maximal E_2 domains. The rate delta^(1-alpha) is sharp for the un-normalized coupling.
4. V208: ||x^2y chi(X/eps)||_E2 is comparable to eps^(1-alpha) (sup eps^3, x-seminorm eps^(3-alpha), weighted y-seminorm exactly eps^(1-alpha)[H]). The transport image is O(eps^(1-alpha)) and the coupling image is O(eps^(2-alpha)). c[h_eps]=eps^2 c[H] and c[x^2y beta]=(1/4)∫r beta, so J(k_eps)=1, c(k_eps)=0 and ||k_eps||_graph->0.
5. Hence J on C_c^inf∩E_2 is unbounded (equivalently non-closable) in the L_delta graph norm even on ker c, and ker J∩ker c is graph-dense. V208 needs only boundedness of the coupling, not V207's smallness. Suggested fixes: state J's domain, state the density form, and note that proof 200/202 apply verbatim at p=2.
