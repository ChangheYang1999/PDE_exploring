# Independent cross-audit of V224 (proof 214): global coupling and closed realization on the common Holder target

Auditor: independent auditor. Read-only review by hand. The only computations were sha256sum, the exponent values, and one short numerical check of a slab integral. No file other than this one was created or modified. No git, no network.

Audited file: verification/proofs/214_global_holder_coupling/PROOF.md

SHA256 (sha256sum): 77e47e53a391e4e8e6d07c3f8b4e9d46a4b818d08672d8e6044f04148c27bc1b

This matches the hash in V224 and in evidence/check.json. The evidence directory holds only check.json, which lists dependency hashes and "computation: none". All seven dependency hashes in it (topics 213, 199, 203, 204, 39, 50, 117) match the current files byte for byte.

Context read: VERIFICATION_RECORD sections V203 to V226; proofs 199, 203, 204 and 213 in full; the statements of topics 39, 50 and 167 (the moving-tail family, used to check the claim about the full normalized linearization).

Numerical constants: k = 1615536043799051/2^53 = 0.1793605..., so 4k = 0.71744 and ell0 = 1/k = 5.5754.

## Verdict

**PASS WITH REMARKS.** I found no mathematical gap. The global directional bounds (3) and (4) are correct. The band analysis is done only for compactly supported inputs, which lie in unweighted L2, and each low-frequency remainder is shown to tend uniformly to 0. The bounds then pass to general E2 inputs by radial truncation and pointwise convergence of the far-subtracted kernel, so no reconstruction from weighted L2 data is ever needed. The annular weighted L2 proof is correct for -2<gamma<2 and identifies the extension with the canonical velocity. The global products, the rank-one column, the tail bound (1), closedness, and the J = 1, c = 0 packets with their full nonlocal images all check out. The scope statements are accurate. Three remarks matter for how V224 is integrated. (a) "The actual renormalized coupling" uses the cut-off column H0 = chi0 X.grad rho0/3. The raw column c[h] X.grad rho0/3 grows like r^k and does not map into Y. (b) The lower endpoint 4k is never used in this proof; the coupling results hold for every -2<gamma<2. (c) Two small steps need spelling out: the parity argument that makes the canonical velocity equal the L2 multiplier for compact inputs (load-bearing for U1/x), and the continuity of the U1/x extension at x = 0 for non-compact inputs. Neither changes any conclusion.

## Checks

### 1. Global x-Holder bound, first line of (3), and its low-frequency reconstruction: PASS

Fix xi and transform in y. The multipliers xi^2/(xi^2+eta^2) and xi eta/(xi^2+eta^2) have y-kernels (|xi|/2)exp(-|xi||y|) and, up to a factor i, (xi/2)sign(y)exp(-|xi||y|). Neither has a delta part, because each multiplier decays in eta for fixed xi not equal to 0. Localize smoothly to |xi| ~ N. The 2D kernel is K_N(x,y) = N^2 K_1(Nx,Ny), so its L1 norm does not depend on N. On the fixed xi annulus, |xi| is smooth, so integrating by parts in xi gives |K_1| <= C_L (1+|x|)^(-L)(1+|y|)^L exp(-c|y|). The sign(y) factor is a constant parameter in this integration, as the proof says. Since the xi support avoids 0, the integral of K_N(.,y) over x vanishes for every y. Hence, with x moment ∫∫|K_1||x|^alpha < infinity, the band is bounded by C [h]_x N^(-alpha). Also ||∂_x K_N||_L1 = CN. For N >= 1 this gives |U_N(x+d)-U_N(x)| <= CM min(N^(-alpha), N^(1-alpha)|d|), which sums to CM|d|^alpha. For dyadic N < 1, each band is bounded by CM and its difference by CM min(1, N|d|). The sum is C|d| when |d| <= 1, and C + log2|d| when |d| >= 1. Since 1+log d <= C_alpha d^alpha for d >= 1, [U]_x <= C(||h||_inf + [h]_x). Only the sup norm and the x-seminorm of h are used.

Reconstruction. Let h be compact, so h is in L2. On the slab |xi| <= N, both multipliers have L2(R^2) norm O(N). Indeed ∫ xi^4/(xi^2+eta^2)^2 deta = ∫ xi^2 eta^2/(xi^2+eta^2)^2 deta = (pi/2)|xi|, and I checked the first identity numerically. Integrating over |xi| <= N gives (pi/2)N^2. Cauchy-Schwarz then bounds the low part pointwise by CN||h||_2, which tends to 0 uniformly as N -> 0. So the velocity is the uniform limit of its band sums. The proof says this reconstruction "removes any polynomial ambiguity". The precise reason the L2 velocity is the canonical one is the parity argument in Remark 3. For x-differences a constant would drop out anyway. An xi = 0 component would be a function of y alone, and it would also drop out of x-differences. The supremum is not controlled by this band sum (the low bands diverge logarithmically). It is controlled separately in Check 2, as the proof correctly arranges.

### 2. Logarithmic supremum, second line of (3): PASS

Moving horizontally then vertically gives a local alpha seminorm on the unit disk about X of at most [h]_x + (|X|+1)^2 [h]_(y,2) <= CM(1+|X|^2). With eps = (1+|X|^2)^(-1/alpha), circular cancellation of the order-zero kernel gives CM(1+|X|^2) eps^alpha/alpha = CM/alpha. The shell from eps to about 1+|X| gives M log((1+|X|)/eps) <= C_alpha M(1+log(2+|X|)). The subtraction K(-Y) over 1<|Y|<2(1+|X|) gives the same logarithm. Beyond that radius, |K(X-Y)-K(-Y)| <= C|X||Y|^(-3), which integrates to a bounded quantity. The local delta part of U2 is bounded by CM. All regions are accounted for, possibly with overlaps, each bounded by C_alpha M(1+log(2+|X|)). This uses the full E2 norm, as stated.

### 3. y-band estimates for U2 in (4): PASS

The identity U2 = -I + eta^2(-∂_x^2+eta^2)^(-1) is correct, since -xi^2/(xi^2+eta^2) = -1 + eta^2/(xi^2+eta^2). The band kernel of the second term is N^2 G_1(Nx,Ny). Two integrations by parts in eta give the y-integrated bound CN exp(-cN|z|). For N >= 1, the mean-zero band and the weighted y-seminorm give ||h_j(x,.)||_inf <= CM x^2 N^(-alpha). The moment ∫ N exp(-cN|x-x'|) x'^2 dx' <= C(x^2+N^(-2)) gives (5). In the dyadic characterization of proof 199, the constant is sup_N N^alpha a_N <= CM(1+x^2). Bernstein in y applies to each band at fixed x. For N < 1, each band amplitude is CM (identity term plus a kernel of x-integral C), and its y-difference is CM min(1, N|d|). The sum is C|d| for |d| <= 1 and C(1+log|d|) <= C_alpha |d|^alpha for |d| >= 1.

Reconstruction for compact inputs. The -1 part gives -P_<eps h, and |P_<eps h(x,y)| <= C eps ∫|h(x,y')|dy', which tends to 0 uniformly. The other part has L2 norm squared ∫_{|eta|<eps} (pi/2)|eta| deta = (pi/2)eps^2, so it is O(eps) and its contribution tends to 0 uniformly. For compact inputs there is no eta = 0 term. The sentence "Any eta=0 term is independent of y and drops out" is a harmless safeguard.

### 4. y-band estimates for U1/x in (4), including the x-independent quotient terms: PASS

∂_x U1 = -i eta ∂_x^2(-∂_x^2+eta^2)^(-1) = i eta I - i eta [eta^2(-∂_x^2+eta^2)^(-1)]. So the derivative is i eta h_j plus i eta times the U2 convolution, as stated. For N|x| <= 1 and |s| <= |x|, both terms are at most CN·M N^(-alpha)(s^2+N^(-2)) <= CM N^(-1-alpha). U1[h_j] is odd in x, so it vanishes at x = 0, and integrating from 0 gives (6). For N|x| >= 1, the direct kernel bound gives CM N^(-alpha)(x^2+N^(-2)) <= 2CM N^(-alpha) x^2. The unweighted bound gives CM. Dividing by |x| gives (7).

Dyadic constants: from (6), N^alpha·N^(-1-alpha) = 1/N <= 1. From (7), N^alpha·|x|N^(-alpha) = |x|. So the high-band seminorm is at most CM(1+|x|).

Supremum. For |x| <= 1, the sum is bounded by sum N^(-1-alpha) + |x|·C|x|^alpha. For |x| >= 1, split at |x|^(2/alpha): the pieces are C(1+log|x|)/|x| and C|x|·|x|^(-2). All are uniformly bounded.

Low bands. ||∂_x U1[h_j]||_inf <= CNM, and oddness gives ||U1[h_j]/x|| <= CNM, with y-derivative CN^2 M. Both sums converge.

The x-independent quotient terms are the worrying case: a term U1 = x g(y), for instance a strain-type x-linear velocity, would add g(y) to U1/x. The proof excludes such terms. For compact h, U1[P_<eps h] is the L2 sum of bands below eps. Each band's x-derivative has sup at most CNM because of the explicit factor eta, so the derivative of the remainder is at most C eps M. Oddness then gives |U1[P_<eps h]/x| <= C eps M, which tends to 0. So no x-linear or y-only quotient term survives, and this is the correct mechanism. At the origin the extension equals -c[h] (proof 201), consistent with |c| <= (4/pi)M.

Continuity of the extension. Each band is C^1 in x. For uniform convergence for all x, note min(|x|N^(-alpha), 1/|x|) <= N^(-alpha/2), which gives an x-independent summable majorant CM N^(-alpha/2) (Remark 5).

### 5. Passage from compact to general E2 inputs: PASS

The truncations chi(X/R)h have E2 norm at most CM uniformly in R >= 1. In the x-seminorm the cutoff term is M min(2, C|d|/R) <= CM|d|^alpha. In the weighted y-seminorm the cutoff term uses |h|/x^2 <= M|y|^alpha. For |d| <= R both points lie within 3R, so the term is (3R)^alpha C|d|/R <= C|d|^alpha. For |d| > R, orient the product so that h is evaluated on the cutoff support, which gives M(2R)^alpha <= CM|d|^alpha. Parity and h(0,y) = 0 are preserved.

Pointwise convergence of the canonical velocities follows by dominated convergence. Away from Y = X, the majorant |K(X-Y) - K(-Y)1_{|Y|>1}|·||h||_inf is integrable (O(|X||Y|^(-3)) at infinity). Near Y = X, chi_R h = h for large R and the local cancellation applies. Every bound in (3) and (4) is a pointwise inequality among finitely many values of U, so all of them pass to the limit. Continuity of the U1/x extension at x = 0 for non-compact h needs one more line (Remark 4).

### 6. Weighted L2 multiplier bound and identification: PASS

The annuli A_0 = {r<2} and A_j have weight comparable to 2^(-gamma j). For l >= j+3, |X-Y| >= (3/4)2^l and |K| <= C2^(-2l). Cauchy-Schwarz on A_l gives an L1 bound C2^l·2^(gamma l/2)||h_l||_{L2(w)}, and the output factor is (∫_{A_j} w)^(1/2) ~ 2^((1-gamma/2)j). The block norm is therefore C2^(-(1-gamma/2)(l-j)), which is (8). For j >= l+3 one gets C2^(-(1+gamma/2)(j-l)), which is (9). For |j-l| <= 2 the unweighted bound and comparable weights suffice. Young's inequality on Z finishes the proof.

Endpoints. gamma < 2 is used in (8) and in the far integral ∫_{r>1} r^(-4) w^(-1) dX = C∫ r^(gamma-3) dr < infinity. gamma > -2 is used only in (9). This is the A2 range of (1+r^2)^(-gamma/2) on R^2, so the result agrees with weighted Calderon-Zygmund theory. The bound 4k < gamma is not used anywhere in this proof (Remark 2).

Identification. Compact truncations converge in L2(w) and define the bounded extension. The un-subtracted far integral converges absolutely by the r^(-4)w^(-1) integral. The canonical subtraction constant vanishes by parity, and pointwise and L2(w) limits agree almost everywhere. So the extension is the canonical velocity, with no added harmonic field.

### 7. Global products with grad rho0: PASS

The background is a finite angular sum (260 modes, proof 50) with C6 radial joins (proof 39), and it is even in x and odd in y. So rho0_x is odd in x and vanishes on the y-axis, while rho0_y vanishes there to second order. The quotients a1 = rho0_x/x and a2 = rho0_y/x^2 are C^1 across x = 0 away from the origin. On the leading mode, a1 = r^(k-2)·(bounded angular factor) and a2 = r^(k-3)·(bounded angular factor). This gives (10). The faster subleading powers are imported from topics 39, 50 and 117; I did not re-derive them.

The divided identity (11) is exact, and parities and the axis value of the output are correct. For the y-seminorm with |d| <= 1:
- a1[V1] contributes C r^(k-2)·CM(1+|x|) <= CM r^(k-1);
- a2[U2] contributes C r^(k-3)·CM(1+x^2) <= CM r^(k-1);
- the coefficient differences are CM r^(k-3)|d| and CM log(2+r) r^(k-4)|d|.

All of these are bounded because |x| <= r and k < 1. For |d| >= 1, twice the bounded supremum of (11) suffices. Note that the growth rates (1+|x|) and (1+x^2) in (4) exactly match a1 ~ r^(k-2) and a2 ~ r^(k-3) (Remark 6).

For the x-seminorm: [U]_x·sup|grad rho0| is bounded, since grad rho0 is O(r^2) at 0, bounded on compacts and O(r^(k-1)) at infinity. For |d| <= 1 the term |U|·|∂_x grad rho0||d| is at most CM log(2+r) r^(k-2)|d|. For |d| > 1 use twice the supremum, which is at most CM(1+log r) r^(k-1) and so bounded. The near disk is handled by proof 203 at p = 2 (bounded with factor delta^(1-alpha)). 1-chi_delta is a bounded E2 multiplier by the cutoff lemma of proof 213. So U[.].grad rho0 is bounded E2 -> E2 globally, and bounded on L2(w) by sup|grad rho0| times Check 6.

### 8. Rank-one column c[h]H0: PASS (scope in Remark 1)

||c||_{E2*} <= 4/pi by proof 213. H0 = chi0 X.grad rho0/3 = chi0 x^2(a1 + y a2)/3 is compact smooth after division, and it has the E2 parities, so it lies in Y. The column is bounded and rank one. Its tail beta_R H0 vanishes for large R. This column is the one in proof 167, formula (1). It is not the raw column c[h]X.grad rho0/3.

### 9. Tail estimate (1): PASS

On r >= R the supremum is at most CM(1+log r) r^(k-1) <= CM R^(k-1)(1+log R), because r^(k-1) log r is eventually decreasing. In the x-seminorm, [U]_x times sup_{r>=R}|grad rho0| gives CM R^(k-1). The derivative of beta_R grad rho0 is at most C R^(k-2), since the cutoff costs C/R against r^(k-1). Times |U| this gives CM R^(k-2)(1+log R)|d| for |d| <= 1, and twice the supremum covers |d| > 1. In the weighted y-seminorm the small-difference terms are at most CM R^(k-1). The coefficient-derivative terms are CM R^(k-3) and CM R^(k-4) log R. For large differences the supremum of the divided coupling is at most CM R^(k-2)(1+log R). In weighted L2 the bound is C R^(k-1) C_gamma ||h||_{L2(w)}. The total is C R^(k-1)(1+log R)||h||_Y. The log comes only from the supremum and x-seminorm parts, through |U| <= CM log r. Note that grad rho0 decays like r^(k-1). It is X.grad rho0 that grows, like r^k.

### 10. Closedness of the maximal Y graph: PASS

The transport part is T h = V.grad h - h, with the actual global field V = ell0 X + U[rho0]. V is at least C^1 globally and div V = 2 ell0 exactly, so V.grad h = div(Vh) - 2 ell0 h is a well-defined distribution for continuous h. The Y norm contains the sup norm. So h_n -> h and V.grad h_n -> g in Y imply V.grad h = g in distributions. Hence the maximal operator V.grad is closed, and so is T. C_ren is bounded on all of Y. So L_ren = T + C_ren is closed on the same domain, and {h in Y : L_ren h in Y} = D_Y. Closedness therefore reduces exactly to the transport part, and that part is soft (Remark 7). The proof correctly disclaims density of S and any resolvent or inverse.

### 11. J-nonclosability packets in the global graph: PASS

For h_eps = x^2 y chi(X/eps): J = 2/2 = 1. Scaling gives E2 norm O(eps^(1-alpha)) and L2(w) norm O(eps^4), since the support has area eps^2 and the sup is eps^3.

Near 0, parity gives V = (-x A, y D) with A = A0 + O(r^2), D = D0 + O(r^2) and C^2 coefficients. So proof 204, formula (3), applies verbatim to the actual field once eps < delta/2. This gives ||T h_eps||_{E2} = O(eps^(1-alpha)) and ||T h_eps||_{L2(w)} = O(eps^4).

The complete nonlocal image consists of two parts. U[h_eps].grad rho0 is supported on the whole plane. It is controlled by the global bound of Checks 6 and 7, not by any localization. The column eps^2 c[H] H0 is O(eps^2). The identity c[h_eps] = eps^2 c[H] is exact homogeneity.

q = x^2 y beta(r)/c[q_raw] with c[q_raw] = (1/4)∫ r beta dr > 0 lies in S, with J(q) = 0 and c[q] = 1. Its transport image is x^2 times a compact C^1 function, so q is in D_Y.

k_eps = h_eps - eps^2 c[H] q has J = 1 and c = 0, and its graph norm is O(eps^(1-alpha)) + O(eps^2), which tends to 0. So (0,1) lies in the closure of the graph of J on S ∩ ker c. On ker c, the column c[f]M(ell0) of the moving-tail operator A_0 in proof 167, formula (4), vanishes. So A_0 k_eps = L_ren k_eps, and the transfer claimed in line 160 is correct.

### 12. Scope: PASS

The proof claims boundedness of C_ren, closedness of the maximal L_ren, the tail bound and the packets. It explicitly disclaims injectivity, surjectivity, dense domain, inverse bounds, compactness of the full coupling, realization of the full moving-tail operator, and any nonlinear or existence result (lines 17, 24, 31, 33, 147, 162). The V224 wording matches. The only phrases that could be over-read are listed in Remark 8.

## Remarks

1. The cut-off column is essential to the claim. C_ren is defined with H0 = chi0 X.grad rho0/3, not with c[h] X.grad rho0/3. The raw column behaves like k r^k Theta/3 at infinity. It is unbounded, so it is not in E2, and it is in L2(w_gamma) only when gamma > 2+2k > 2. So for c[h] not equal to 0, the raw normalization term does not map into Y at all. "The actual renormalized coupling" in V224 must therefore be read as the split of proof 167: column c[h]H0, with the moving-tail part c[h]m(ell0) left aside. The proof's bounds say nothing about m(ell0). It enters only through c, so the packet statement transfers. The symbol L_fix on line 160 is not defined in this proof. It should be identified with A_0 of proof 167, formula (4), whose scalar column is c[f]M(ell0).

2. The lower endpoint 4k is never used. The multiplier bound, the products, the tail bound (1), closedness and the packets hold for every -2<gamma<2. Nothing in this proof needs gamma >= 0 or gamma > 4k. The restriction 4k < gamma comes only from proof 213 (F0 in Y if and only if gamma > 4k). The upper endpoint gamma < 2 is used twice: in (8), and in the far integral of the identification. The constants blow up like (1 - 2^(-(1-gamma/2)))^(-1) as gamma -> 2, so (1) is not uniform near gamma = 2. This is harmless for fixed gamma.

3. Identifying the canonical velocity with the L2 velocity for compact inputs is load-bearing, and it should be stated in the band section. Line 54 says only that the reconstruction "removes any polynomial ambiguity". The precise reason is parity. K1 is odd in x and odd in y, K2 is even in both, and h is even in x and odd in y. So ∫_{|Y|>1} K(-Y)h(Y) dY = 0, and the canonical velocity equals the decaying L2 multiplier velocity. That makes U1 odd in x, which (6) needs through U1[h_j](0,y) = 0. Any nonzero constant added to U1 would make U1/x unbounded near x = 0. The argument appears only later, on line 107, for Y inputs. A cross-reference would close this.

4. Line 89 claims only pointwise convergence of the truncated velocities. That gives the bounds in (3) and (4) but not, by itself, continuity of the U1/x extension at x = 0 for non-compact h. The missing line: U1[(1-chi_R)h] is smooth on B_(R/2) and odd in x, with |∂_x U1[(1-chi_R)h]| <= CM/R there. So U1[chi_R h]/x converges locally uniformly to U1[h]/x, which is therefore continuous across x = 0.

5. Line 85 justifies uniform convergence of the high-band quotients "using (6) near x=0". An x-independent summable majorant exists for all x: min(|x|N^(-alpha), 1/|x|) <= N^(-alpha/2), so CM N^(-alpha/2) works everywhere. This is presentation only.

6. The bounds (4) are deliberately crude: they ignore [h]_x and the smoothing in x of the band kernels. They are exactly enough. The weights (1+|x|) and (1+x^2) are absorbed by a1 ~ r^(k-2) and a2 ~ r^(k-3) only because k <= 1. This is informational and requires no repair.

7. Closedness is the soft part. Any maximal distributional realization with continuous V, div V constant, and a norm controlling local uniform convergence is closed. The substantive new content of V224 is that C_ren is bounded on Y globally, with the stated tail. The closed graph yields no density, resolvent or Fredholm information, and the proof claims none. The proof shows membership in D_Y only for the packets and q. Membership for all of S also holds by the same divided-coefficient argument, but it is not needed.

8. Wording. "Its actual global transport image is compact in Y" (line 156) means compactly supported, and could be misread as compactness of a set or an operator. "A global closed linear realization" (line 33) should be read as the closed maximal operator for L_ren with the cut-off column, not a realization of the full moving-tail operator. Line 31 already says this. The audit request's phrase "growth of grad rho0 at infinity (r^(k-1))" describes decay. The log factor in (1) comes from |U| <= CM log r, not from grad rho0.

9. Statement (2) gives no rate. The proof gives graph norm O(eps^(1-alpha)), the same rate as proof 204. Recording the rate would make the comparison with V208 immediate.

10. Imported, not re-derived: the far coefficient bounds (10) with their subleading powers, the C^1 regularity of a1 and a2 across the y-axis at every radius, and the global C^1 (in fact C^3 near 0) regularity of V. All rest on topics 39, 50 and 117 (finite angular sum, C6 joins, exact outer modes). I checked that those statements support the claims as used, but I did not recompute the modal exponents.
