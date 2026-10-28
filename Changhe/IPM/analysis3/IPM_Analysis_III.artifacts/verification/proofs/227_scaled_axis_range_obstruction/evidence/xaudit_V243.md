# Independent cross-audit of V243 (proof 227, outgoing-axis range obstruction in the scaled target Z)

## Audited file

verification/proofs/227_scaled_axis_range_obstruction/PROOF.md

SHA256 (sha256sum, recomputed at audit time): a96237e8a3907bd56be431d7ea3702a489ff7e3f5a63606ae52c49932d2fe096

This matches the expected hash and proof_sha256 in evidence/check.json. All seven dependency hashes in the current check.json match the PROOF.md files on disk: 88 (f5003612...), 35 (f6b46867...), 117 (20b9e69c...), 217 (a4a9e82a...), 220 (d906b7a2...), 222 (6fabe851..., the updated hash), 223 (30980d7f...). During the audit check.json was updated to record that proof 222 changed from d5a1747b... to 6fabe851... (V244 clarification). I diffed the archived 222/evidence/audited_PROOF.md against the current 222 PROOF.md: the changes are one added sentence in the cutoff commutator paragraph, removal of a frequency remark in the endpoint paragraph, a reworded construction of q, a changed citation for the normalization packets, and a rewritten closing scope paragraph that now points to proof 227. None of the estimates used by proof 227 (Z, (3), (4), (5), boundedness of Cren and C0, closed maximal domain) changed.

## What I read

Proof 227 PROOF.md and evidence/check.json in full. Proof 222 PROOF.md in full (current version, plus diff against the archived audited version). Proof 223 PROOF.md and AUDIT_CLARIFICATIONS.md (sha 7fdb5807...). Proof 217 PROOF.md and AUDIT_CLARIFICATIONS.md (sha ebabca8b..., the "sharp tail clarification"). Proof 220 PROOF.md in full. Proof 88 PROOF.md in full. The opening of proof 52 (V globally Lipschitz C1, A=2ell-1, D=4ell-1, d(t) asymptotics), the opening of proof 79 (field definition), the strain definition in proof 213, the q construction in proof 204, the C6 join statement in proof 50, and the statements of topics224, 225, 226 (to check consistency of scope).

## VERDICT

PASS WITH REMARKS.

## Summary

The argument is correct. The positive vertical axis is invariant (V1 is odd in x) and is the unstable branch of the origin. V2(0,y)>0 for y>0 follows from the zero set of proof 88 (with W=0) and D>0. Continuous dependence on a compact time interval plus the far quotient bound (2) then give the two-sided exponential bounds (3), uniformly in small x, with the exact rate ell. The characteristic representation (11) holds for every h in D_Z, because h and V.grad h are continuous, V is C1 and nonvanishing along the orbit, and the endpoint term decays since ell beta<1. The key coupling estimate (7)-(8) uses only Z-controlled quantities. The full Z norm controls the scaled velocity Holder bound (4) of proof 222. Oddness of U1 in x then gives the gain x_t^alpha. No control of U1/x is used (and Z gives none far away). The resulting rate x^(1+alpha) is exactly why the exponent window is alpha<sigma<1+alpha. The forcings are compact C^alpha functions supported outside B4, so they lie in Z with zero local factor. The local E2 factor forces |h(x,1/2)|<=N x^2 2^(-alpha), while the forcing integral is a_sigma x^sigma(1+o(1)) with a_sigma>0. This is a genuine contradiction, and the least-exponent argument gives linear independence of the cosets. The conclusion covers T, Lren and A0 on D_Z for the stated parameter range. The scope disclaimers are accurate. I found no gap, sign error or exponent error. The remarks concern unstated regularity citations, provenance of cited sidecar files, and a notation clash.

## Findings

1. REMARK (section "Compact forcing classes", sentence "write V1=x a1(x,y) with C^1 a1"). The geometry section only invokes global C1 regularity of V ("global C1 regularity suffices"). For a C1 field, a1=V1/x is only continuous, which is not enough for sigma a1 |x|^sigma to be C^alpha. The claim is nevertheless true. The forcing support {|x|<=2, Y<|y|<2Y} lies in a compact punctured region where rho0 is C6 (proof 50, restated in proof 217), so U[rho0] is C^(1,alpha) and in fact much smoother there. Proof 225 also states that V1/x is locally Holder. Only a1 in C^alpha is needed. This affects only the auxiliary claim f_sigma in D_Z, not the cokernel statement, which needs only f_sigma in Z. Suggested repair: cite proof 50/217 local regularity and state that a1 in C^alpha suffices.

2. REMARK (section "Characteristic contradiction", the citation of "the flow-box argument in proof 223's audit clarification"). Item 4 of 223/AUDIT_CLARIFICATIONS.md is formulated on r>=R0/2, where V is nonvanishing by its outward radial component. Here the orbit starts at (x,1/2) inside B2. The argument is local: it needs only V in C1 and V nonzero along the orbit. This holds because V2>0 on the initial compact segment for small x, by (1) and continuity, and V2/y>=ell/2 for y>=R. Proof 220 contains the same argument for interior strips. Suggested repair: add one sentence noting V is nonzero along the whole orbit, so the local flow-box argument applies verbatim.

3. REMARK (endpoint bound "|h(Phi_t X)|<=C N exp(ell beta t)"). The stated range allows 2k-1<beta<=0. For negative beta the displayed bound needs the lower radial bound r_t>=a exp(ell t) from (3), or simply boundedness of h. It is true as stated, but the two-sided use of (3) is implicit. No repair needed beyond a parenthetical.

4. REMARK (provenance; evidence/check.json). The proof cites two sidecar files that check.json does not hash: the proof 217 "sharp tail clarification" (217/AUDIT_CLARIFICATIONS.md, sha ebabca8b...) and proof 223's "audit clarification" (223/AUDIT_CLARIFICATIONS.md, sha 7fdb5807...). The proof also implicitly uses facts from unlisted topics: proof 52 (V globally Lipschitz C1, D=4ell-1>0), proof 213 (the E2 vertical seminorm and the strain kernel (1/pi) sin(3 theta) r^(-3)), and proof 50 (C6 joins, see finding 1). Suggested repair: add these to the dependency record.

5. TYPO (section "Actual characteristics", "the three zeros 0 and (+/-p,0)"). Here p denotes the source abscissa (about 8.6, topics79/88), but in proof 222, proof 226 and the beta range of this very theorem p=2k-1. Suggested repair: write (+/-x_P,0) or p_src.

6. REMARK (optional sharpening of scope, not an error). For T and Lren the identical proof also works at beta=2k-1, because proof 222 gives Cren bounded and T closed there. Only A0 needs beta>2k-1, for M0 in Z. The base height y0=1/2 can also be any 0<y0<2. Neither extension is claimed, so the statement is not wrong, merely not maximal.

## Independent verification

Flow geometry. I checked that V1(0,y)=0 by parity, so the positive vertical axis is invariant and x_t>0 is preserved (V is globally Lipschitz by proof 52). Zeros of V on that axis are zeros of V2(0,.). Proof 88 with W=0 (which satisfies its hypotheses) gives exactly three zeros, and assertion 5 gives the y-axis as the unstable direction with D>21. Hence V2(0,y)>0 for all y>0. The orbit from (x,1/2) never passes through the saddle neighbourhood: it starts on the unstable side at distance 1/2 and moves upward, so no saddle-passage estimate is needed. The axis orbit reaches any height in finite time, because V2(0,.) is positive on compacts and V2(0,y)/y tends to ell.

I verified (2) for all large r, not just in the cone, from |U[rho0]|<=C r^k and |DU[rho0]|<=C r^(k-1) (proof 223 (3), proof 220 (1)). When x>=r/2, divide directly. Otherwise average partial_x U1 along the segment from (0,y) to (x,y), whose points have radius at least y>=0.86 r. The same works for U2/y. So no bootstrap on the cone is required. For t>=T_*, y_t>=y_(T*) exp(ell(t-T*)/2). The integral of C r_t^(k-1) is bounded by C R^(k-1)/(ell(1-k)/2). Exponentiating d log x_t/dt and d log y_t/dt then gives (3) with the exact rate ell. Combined with the compact initial segment (x_t/x bounded above and below since a1 is bounded and continuous), the constants are uniform in 0<x<x0. The cone bound x_t/y_t<=(B/a)x follows.

The exactness of the rate ell matters only for the endpoint term exp(-t)h(Phi_t X), when beta is near k. The coupling integrals have the large margin ell(1-beta)>ell(1-k), about 4.58.

Representation (11). With g=Th=f-C[h] continuous, d/dt[exp(-t)h(Phi_t X)]=exp(-t)g(Phi_t X) along the orbit. The endpoint exp(-t)(1+r_t)^beta tends to 0 iff ell beta<1, i.e. beta<k. The sign in (11) is correct.

Coupling exponents (sympy check). For x_t ~ x e^(ell t) and r_t ~ e^(ell t):
- The U1 rho0_x term x_t^(1+alpha) r_t^(beta-alpha+k-2) has time exponent ell(1+alpha)+ell(beta-alpha+k-2)-1=ell(beta-1), symbolically confirmed.
- The U2 rho0_y term x_t^2 r_t^(beta+k-3) has the same exponent, also confirmed.
- The M0 term x_t^2 r_t^(2k-3)(1+log r_t) has exponent ell(2k-1)-1=ell(k-1)=1-ell, confirmed.

Numerically, k=0.1793605..., ell=5.5753626..., 2k-1=-0.6412789..., 4k=0.7174421..., A=2ell-1=10.1507..., D=4ell-1=21.3015... The coupling exponent lies between -9.15 (beta=2k-1) and -4.58 (beta=k), and the M0 exponent is -4.58.

Norm control of the coupling. (5) uses the scaled seminorm [U[h]]_(C^alpha) <= C N r^(beta-alpha) on {r<=|X|<=2r} from proof 222 (4). Both points (x_t,y_t) and (0,y_t) lie there with r=y_t, because x_t/y_t<1/4, and U1[h](0,y_t)=0 by oddness and continuity. This uses only N=||h||_Z. U1/x is never used. The divided density bounds (6) match proof 220 (5) and proof 222 (a1, a2 bounded and Lipschitz). The M0 divided far bound matches proof 217 (6) (stated for m0=M0-H0, with H0 compact), and |c[h]|<=CN is proof 222 (5). H0=chi0 X.grad rho0/3=chi0 x^2(a1+y a2)/3 is compact and quadratically divisible, so its contribution is O(N x^2) over a bounded time interval. C0=Cren+c(M0-H0)=U.grad rho0+c M0, so A0 has no H0 term. This is correctly handled.

Forcings. |x|^sigma is C^alpha on compacts for alpha<sigma<1+alpha (C^sigma when sigma<=1, C^1 when sigma>1). F_sigma is even in x, odd in y, zero on x=0, and supported in {|x|<=2, Y<|y|<2Y} with Y>4, hence outside B4. Its local E2 factor is therefore zero, so F_sigma is in Z. F_sigma is in W^(1,1)_loc since sigma>0, so the distributional and a.e. transport derivatives agree. Then V1 partial_x(|x|^sigma phi) g = sigma a1 |x|^sigma phi g + V1 |x|^sigma phi' g, which is compact, C^alpha and zero on the axis (with finding 1).

For q, the strain kernel is (1/pi) sin(3 theta) r^(-3) (proof 213). I checked symbolically that partial_x^2 partial_y log r = 2 sin(3 theta)/r^3. I also checked that sin(3 theta) is even under theta -> pi-theta and odd under theta -> -theta, i.e. it has the density parity. Hence a reflected first-quadrant bump at theta near pi/6 has nonzero strain, and the quadrant contributions add. Since q is supported outside a fixed cone and the orbit stays in the cone x_t/y_t<=(B/a)x, q vanishes along the orbit after shrinking x0. Shrinking x0 does not invalidate a, B.

Forcing asymptotics and contradiction. y_t is strictly increasing along the orbit, so the support of g is met once, in a bounded time window. On that window phi(x_t)=1 for small x, and x_t/x converges uniformly to xi(t)=exp(integral_0^t partial_x V1(0,y^0_s)ds)>0. This uses continuity of a1, which holds for a C1 V. Dominated convergence gives a_sigma=integral exp(-t) xi(t)^sigma g(y^0_t)dt>0.

For the local bound, chi=1 on B2, so the pair (x,1/2),(x,0) gives |h(x,1/2)|<=N x^2 2^(-alpha) by the x^2-weighted vertical seminorm and h(x,0)=0. After dividing by x^sigma, the left side and the coupling are O(x^(2-sigma)) and O(x^(1+alpha-sigma)), both of which tend to 0, while the forcing term tends to -a_sigma. Contradiction. For a finite combination, the term with the least exponent dominates, giving independence. The range is a linear subspace because D_Z is linear, so the cosets are independent and the algebraic cokernels are infinite dimensional, hence the operators are not Fredholm.

Consistency. Proof 223's exterior orbits never enter B_R, so its inverse never meets the local quadratic condition, and there is no conflict. Proof 224 explicitly left non-Fredholmness on Z open, and proof 222's updated closing paragraph now defers to proof 227, so there is no contradiction with accepted statements.

Process note. To run the sympy checks I briefly created the scratch file tmp/xaudit_v243_check.py and deleted it immediately after the run. No other file was created or modified, and nothing under verifier, source or repo was touched.

## Scope I consider proved

For every 0<alpha<1, 2k-1<beta<k and gamma>4k, with Z=Z_(alpha,beta,gamma) of proof 222 and its closed maximal domain D_Z: the quotients Z/Range(T), Z/Range(Lren) and Z/Range(A0) are infinite dimensional as algebraic vector spaces, so none of the three operators is onto or Fredholm. This persists under any further restriction of the domain. The cosets of f_sigma=F_sigma-c[F_sigma]q, for any infinite set of distinct sigma in (alpha,1+alpha), are linearly independent in each quotient. The f_sigma are compactly supported, vanish on B4, have c=J=0, lie in Z, and lie in D_Z (given the local regularity of finding 1). The obstruction comes from the local quadratic axis condition near (0,1/2) being transported backward along the outgoing vertical separatrix, where Z imposes only ordinary C^alpha control. Not proved, and not claimed: any statement about the range of the actual residual F0, any statement about spaces that keep a quadratic axis condition along the whole outgoing axis, the Sobolev condition (I), or nonexistence of a profile. Proof 223's exterior inverse is unaffected.
