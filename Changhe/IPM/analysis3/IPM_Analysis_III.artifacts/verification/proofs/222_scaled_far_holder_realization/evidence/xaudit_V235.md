# Independent audit of V235 / proof 222 (scaled far Hoelder realization and the logarithmic endpoint)

Audited file: verification/proofs/222_scaled_far_holder_realization/PROOF.md

SHA256 (sha256sum at audit time): d5a1747bfcfa83daa7ea0458ab3051b1c05dd90ab11a879cea9cb506b61b4c08

This matches evidence/check.json. The sidecar LOCAL_COMMUTATOR_CLARIFICATION.md has SHA256 8d031b03864f06ba7cf1be502d862f1de432d37b1e9521db2a91a60692b1bdca, which matches the value recorded in check.json. All seven dependency hashes in check.json (topics 35, 117, 203, 213, 214, 217, 204) match the current PROOF.md files. The recorded highest_coefficient_certificate_sha256 (77e0b152...) is the SHA256 of proof 35 evidence/check.json (identical to check.log).

Read in full: PROOF.md, the sidecar, check.json; topics 213, 214, 217 (each with AUDIT_CLARIFICATIONS.md), 35 (with code/check.py and evidence), 117 (with the relevant part of code/check.py), 204, 01, 220, 221; the prior audit of proof 217 (xaudit_V228.md); the angular basis of proof 12 and the exact-trial loader used by topics 30 and 117. I also looked at the parts of proof 223 that cite proof 222. Small sympy and fraction checks were run inline.

VERDICT: PASS WITH REMARKS

Summary. I found no gap that invalidates any of the four numbered statements. The space Z is well defined and Banach. The direct kernel estimate (4) holds for -2<beta<1 with no logarithm, and it gives the strain bound (5), the far coupling bound (7) and the weighted L2 tail. The commutator argument for the local E2 factor is correct once the diagonal boundary term, which the sidecar supplies, is included. I rederived the endpoint logarithm and its sin(1043 theta) coefficient independently. The coefficient is k^2(n-k)a_n^2/(2 n'_0 (n+k+2)) with n=521, and it is strictly positive. The endpoint counterexample and the nonclosability of J are correct. The findings below are about a sidecar-only step, a mislabelled citation and construction, one unsupported closing sentence, and notation. I also note a sharpening of statement 3.

## Findings

1. REMARK (main text omits a term that the sidecar supplies). Location: section "A cutoff commutator needed for the local axis norm", the paragraph that differentiates the kernel (chi(X)-chi(Y))K_i(X-Y). The main text lists three pieces: (partial_l chi)U_i[h], the principal kernels z_m partial_l K_i, and the Taylor remainder. It does not mention the boundary term that appears when the truncated integral over |X-Y|>eps is differentiated. That term has size O(1), not o(1). Its limit is a smooth coefficient partial_m chi(X) times the moment integral over the unit circle of omega_m omega_l K_i(omega), multiplied by h(X). I computed these moments for the IPM kernels K1=-xy/(pi r^4) and K2=(x^2-y^2)/(2 pi r^4). They are +/-1/4 or 0, so the term really is present. The sidecar identifies it correctly and bounds it by the local C^alpha norm of h. The conclusion (W in C^(1,alpha) with norm at most CN) is therefore correct. Suggested repair: move the sidecar sentence into the main text.

2. TYPO (inconsistent description of the endpoint test function). Location: section "The logarithmic endpoint is genuinely excluded", the paragraph beginning "Choose a compact smooth physical-parity q, supported away from both axes and the physical origin ... rescale the explicit nonzero-strain bump of proof 204". The bump in proof 204 is q_raw=x^2 y beta(r) with beta supported in an annulus. Its support avoids the origin but meets both axes. Either function works: x^2 y beta(r)/c[q_raw] is in D_Z, because it is compact and smooth with an x^2 factor. A bump near a point (x0,y0) with sin(3 theta0) nonzero, together with its parity reflections, is supported away from both axes and has nonzero strain, since the strain kernel sin(3theta)/r^3 has the same parity as q. Suggested repair: drop "away from both axes", or replace the citation with this explicit construction.

3. REMARK (citation). Location: section "Normalization and remaining scope", the phrase "the exact compact smooth packets h_epsilon of proof 204 ... their E2 and actual transport-image norms tend to0". Proof 204 proves the transport-image estimate only for the frozen and localized operators. The estimate ||T h_eps||_E2=O(eps^(1-alpha)) for the actual global field V is proved in proof 214, section "Closedness and the actual global normalization packets". Proof 214 also gives the zero-strain packets k_eps. The mathematics is unaffected. Suggested repair: cite proof 214 for the actual-field image and for k_eps.

4. REMARK (unsupported and partly inaccurate closing sentence). Location: final section, "This norm excludes the bad far packets of topics220/221". This is not one of the numbered statements, and it is not proved. Read literally, it is not accurate for proof 220. That topic's forcings are F_b=x^2 phi(x)g_b(y), with b in (1/2,1). On the annulus at radius R they have supremum and unit-scale x-variation of order R^(-b). Their scaled annular norm is therefore of order R^(alpha-beta-b), so F_b belongs to Z whenever alpha<=beta+b. What is true is that neither obstruction mechanism transfers to Z.
   - Proof 220 needs the x^2-weighted vertical seminorm on the solution. Z only gives |h(x,Y)|<=C x^alpha Y^(beta-alpha) far out. That bound conflicts with x^(k+b) only if alpha>k+b, and then alpha>beta+b, so F_b is not in Z.
   - Proof 221's packets f_X0 have Z norm of order X0^(2+alpha-beta). After normalization, the characteristic lower bound at (R1,y*) is of order X0^(-(2+alpha+k-beta)). The Z upper bound is of order X0^(-(2+alpha)). There is no contradiction, precisely because beta<k.

   Suggested repair: replace the sentence with "the specific mechanisms of topics220/221 do not apply in Z (for 221 this uses beta<k)". It should not be read as any surjectivity statement.

5. REMARK (sharper form of statement 3, available from the proof). The proof shows that L_fix=T+U[.].grad rho0 maps D_Z into Z at beta=p, because U[.].grad rho0=Cren-c[.]H0 is bounded. It also shows that M0 is not in Z. Hence for every h in D_Z at the endpoint, A0 h is in Z if and only if c[h]=0. In other words, among inputs of D_Z the endpoint failure is exactly the strain direction, and A0 agrees with Lren on D_Z intersect ker c. This is consistent with the cautious final sentence of that section, and it identifies the obstruction more precisely. No repair is needed; the statement could optionally record it.

6. REMARK (auxiliary weight in the local factor). Location: section "A cutoff commutator ...", the sentence "Proof 214's bounded coupling applies to it, with its weighted L2 norm bounded by its compact E2 norm". Proof 214 is stated only for 4k<gamma<2. Proof 222 allows every gamma>4k, including gamma>=2. The use is still legitimate. Only the E2 part of proof 214's output bound is needed, and that part depends only on ||chi h||_E2; any fixed auxiliary gamma0 in (4k,2) can be used for the compact input. The weighted L2 part of the Z output is handled separately, by the pointwise bound (7). Suggested repair: say this explicitly.

7. REMARK (sign of (13) relies on cited data). Positivity in (13) needs n'_0>0. That comes from n'_0=3-c[zeta]>=3, which uses the certified positive sin(3theta) moment (proof 31/V034) and the nonnegative cutoff log moment (proof 35, eq. (2)), as already noted in the proof 217 audit. For the endpoint exclusion only n'_0 nonzero is needed, and that is already required for M0 to be defined. The statement "no new numerical enclosure is needed" is correct with this understanding.

8. REMARK (quantitative size of the endpoint logarithm). With the cited data, a_521=exp((3-k)t_+)Aout[259,0]/8 is about -8.96e-10. For n'_0=3 the coefficient (13) is about 4.3e-21, and it is smaller for larger n'_0. The exclusion at beta=p is mathematically correct but invisible numerically at any practical radius. Nothing in the proof depends on its size. Any later numerics should not expect to detect it.

9. TYPO (notation). The symbol beta is used both for the growth exponent and for the tail cutoff beta_R=1-chi_*(X/R), and both appear in (2) and (9). Two cutoffs, chi and chi_*, are also in play. Suggested repair: rename the cutoff, for example tau_R.

10. REMARK (an unnecessary assertion). Location: before (12), "X.grad R, which has no r^p log r term and angular frequency at most521". Only X.grad R=O(r^p) is needed, and it follows from D_cyl^j R=O(r^(2k-1)) (proof 117: the outer exponents are pure exponentials, and the matching corrections decay strictly faster). The frequency bound is not evidently supported by the cited source. The leading outer cofactor modes m<=259 of the proof 12 basis give frequencies at most 2*259+3=521. However, proof 117 writes rho/r^3 as a sum of sin((2j+1)theta) with j up to 261, which allows frequency 523 in the correction terms. I did not settle which applies to R. It plays no role in the argument. Suggested repair: delete "and angular frequency at most521".

## What I verified independently, and how

- Hashes. I recomputed SHA256 for PROOF.md, the sidecar, the seven dependency proofs and the certificate. I also loaded the original NPZ, whose SHA256 a069d85d... matches proof 35. It gives k=1615536043799051/2^53 exactly, Aout[259,0]=-8059128652303703/10384593717069655257060992658440192, M=260 and t_+=2289893859708677/2^48.
- Coefficient reconstruction. The proof 12 basis is cos^2(theta) sin(theta) cos(2m theta), whose top sine coefficient is 1/8 (checked symbolically). Proof 117 has outer cofactor terms A exp((k-3)(t-t_+)) multiplying r^3, so the coefficient of r^k sin(521 theta) is exp((3-k)t_+)Aout[259,0]/8, as cited. Proof 117 and the loader also show that the exact joins and the scalar repair do not change the leading outer coefficient.
- Modal identities (sympy). With -Delta psi=partial_x h and U=(-psi_y,psi_x) (proof 01), I checked the stream equation -[(q+1)^2P+P'']=q cos(theta)S-sin(theta)S' and the identity U.grad h=r^(2q-1)(-qP'S+(q+1)PS') for generic P and S. For n=3 and n=5, with arbitrary lower odd sine modes, I solved the modal ODE exactly. I confirmed p_(n+1)=-a_n/(2(n+q+2)), the top coefficient [sin((2n+1)theta)]Q_q=-(n-q)a_n^2/(4(n+q+2)), and that no frequency 2n+3 or cos term appears. The general-n derivation by hand agrees.
- Endpoint bookkeeping. I checked that the q-derivative of r^(2q-1)Q_q has log coefficient 2Q_q. I checked the linear cancellation (ell0 r d_r-1)(-k^2 r^k log r Theta)=-k r^k Theta against X.grad(r^k Theta)=k r^k Theta. All cross terms involving R, U[R] (O(r^p) by (4) with beta=p) and compact multipoles are O(r^(3k-2)(1+log r)), which is o(r^p) since 3k-2<2k-1. Finally -2k^2/n'_0 times (10) equals (13) exactly (sympy).
- Kernels (sympy). K1 is odd in x and in y, and K2 is even in both. Both have zero angular mean. All eight kernels z_m partial_l K_i are homogeneous of degree -2 with zero angular mean. The diagonal moments are nonzero (Finding 1). The parity argument for the canonical subtraction (K1(-Y)h odd in x, K2(-Y)h odd in y) is correct.
- Estimates by hand. I checked:
  - the three-region proof of (4) (inner part needs beta>-2, outer part needs beta<1, comparable radii by scale invariance of the order-zero kernel; no logarithm appears);
  - the strain bound (5) (r^alpha dr near 0, r^(beta-2) dr at infinity);
  - the commutator kernel calculus and the d(1+log(1/d)) remainder;
  - the E2 membership of W.grad rho0 through a1 W1/x+a2 W2, with a1, a2 bounded and Lipschitz;
  - the product bound (7);
  - the weighted L2 integral r^(2beta+2k-1-gamma), which is finite iff gamma>2beta+2k, and this holds for all beta<k and gamma>4k;
  - the tail exponents in (2) and (9);
  - F0 in Z exactly when beta>=p, and the weighted L2 condition exactly gamma>4k;
  - closedness of T and the bounded-perturbation domain equality;
  - the counterexample A0 q=L_fix q+M0, not in Z;
  - the transfer of proof 214's zero-strain packets k_eps to the Z graph through the compact-support comparison of proof 213.
- Exponent arithmetic (exact fractions). p is about -0.6413, 3k-2 about -1.4619 and 4k about 0.7174. On a grid of beta in [p,k) and gamma in (4k,5], the exponents k-1, beta+k-gamma/2 and 2k-gamma/2 are all negative.

## Scope I consider proved

For every fixed 0<alpha<1, 2k-1<=beta<k and gamma>4k:
- Z is a Banach space of continuous physical-parity functions vanishing on x=0.
- c is bounded on Z.
- Cren=U[.].grad rho0+c[.]H0 is bounded Z->Z, with the output-tail bound (2), and both exponents in (2) are negative.
- F0 lies in Z, and beta>=2k-1 is necessary for this.

For 2k-1<beta<k:
- M0 lies in Z with the tail bound (9).
- A0=T+C0 is closed on the maximal transport domain D_Z, and C0 has a small output tail.
- J is not closable on smooth c=0 inputs in the A0 graph.

At beta=2k-1:
- M0=r^p log(r)S_M+O(r^p), with S_M=-2k^2Q_k/n'_0 not identically zero. Its sin(1043theta) coefficient is k^2(521-k)a_521^2/(2n'_0(523+k))>0.
- Hence M0 is not in Z, and A0 h is not in Z for every h in D_Z with c[h] nonzero (Finding 5).
- Cren is still bounded, and J is not closable in the Lren graph.

These are realization and mapping statements only. No inverse, Fredholm property, closed cubic constraint, nonlinear result or profile existence follows. The closing sentence about topics220/221 should be read only in the reworded form of Finding 4.
