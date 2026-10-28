# Independent audit: proof 243 sharp full common-target tail (verifier record V276)

Target: verification/proofs/243_sharp_common_target_tail/PROOF.md (94 lines)

SHA256 checked: b718ea65ec31af8b67c779fab843e9fee74bd86d02cb1514f7ccbb6a92b5d8c5 (matches the expected value
and the proof_sha256 in evidence/derivation.json).

Dependency hashes listed in evidence/derivation.json were recomputed and all eight match the current files:
213 PROOF/AUDIT_CLARIFICATIONS, 217 PROOF/AUDIT_CLARIFICATIONS, 222 PROOF/AUDIT_CLARIFICATIONS,
226 PROOF/AUDIT_CLARIFICATIONS. Also read: 222 LOCAL_COMMUTATOR_CLARIFICATION.md, 214 tail section.

VERDICT: PASS WITH REMARKS

No binding findings. All findings below are cosmetic or scope notes.

## Checks requested

(1) Operator-norm lower bound (lines 47-81). PASS. The test input q is one fixed compact smooth function,
independent of R (line 65). ||q||E2 and ||q||Y_gamma are finite (support away from both axes, so the x^-2
vertical seminorm is harmless). For r>=2R, beta_R=1 for any admissible cutoff. Sup part: at r=3R, theta in I,
|beta_R C0 q|>=b(3R)^p log(3R)>=b 3^p R^p log R (line 71). Weighted part (line 75-79): on 2R<=r<=3R,
w_gamma>=(1+9R^2)^(-gamma/2)>=10^(-gamma/2)R^(-gamma) for R>=1; r^(2p)>=(3R)^(2p) since p<0;
log^2 r>=log^2 R; polar area (9-4)R^2/2*|I|=(5/2)|I|R^2. Taking the square root gives exactly (6),
R^(p+1-gamma/2) log R = R^(2k-gamma/2) log R. Division by the fixed ||q|| gives the operator-norm bound.

(2) Velocity part is lower order (lines 57-63). PASS. c[q]=1 so C0q=U[q].grad rho0+M0. Odd-y parity gives
integral q=0; the separated multipole expansion of the degree -2 kernel gives U[q]=O(r^-3); grad rho0=O(r^(k-1))
(222 line 109), so U[q].grad rho0=O(r^(k-4)) and k-4<p. The conclusion is robust: even the crude E2 bound
|U[h]|<=CM(1+log(2+r)) of proof 226 (2) gives U[q].grad rho0=O(r^(k-1)log r)=o(r^p log r), since p-(k-1)=k>0.
No cancellation of the M0 log term is possible.

(3) Exponent matching (lines 83-90). PASS. Upper bound of 226 (1) (and its clarification 2): four terms
R^(k-1),R^(k-gamma/2),R^p,R^(2k-gamma/2) times (1+log R); k-1<p and k-gamma/2<2k-gamma/2, so the bound is
<=8C R^(s_gamma) log R for R>=e. Lower bound: R^max(p,2k-gamma/2) log R. For gamma>2, s=p (sup part);
for 4k<gamma<2, s=2k-gamma/2 (weighted annulus); at gamma=2 both equal 2k-1. Exponents match exactly in all
regimes. All are negative since k<1/2 and gamma>4k. Constants are qualitative and not uniform as gamma->4k,
as already stated in 226 clarification 2.

(4) Sup part of E2 is unweighted. PASS. Proof 213 statement: ||h||E2=||h||infinity+[h]_x+[h]_(y,2), plain
supremum. r^p log r with p=2k-1<0 has sup over r>=2R comparable to R^p log R, consistent with 226 (7).

(5) Operator on E2 versus maximal domain. PASS. (1)-(2) concern beta_R C0 as a bounded operator on the whole
space (line 30: "not its restriction to ker c"); membership q in E2 / Y_gamma suffices. The extra domain
statement (line 55) is correctly flagged as not required.

(6) Refutation of R^(k-1)(1+log R) for full C0 (lines 30, 92). PASS. Lower bound divided by R^(k-1)(1+log R)
is >=c R^k/2 -> infinity, in both targets since s_gamma>=p. The refutation is for C0 on the full space only.
On ker c, C0 coincides with Cren, whose R^(k-1)(1+log R) rate is quoted from proof 214 (4k<gamma<2, weighted
Riesz input) and proof 226 (E2, gamma>=2); proof 244 treats that separately. The result also shows that the
upper bound of proof 217 (1), R^(2k-gamma/2)(1+log R) for 4k<gamma<2, is sharp. No verified record was found
asserting R^(k-1) for the full C0, so no earlier record is contradicted.

## Independent recomputations

- Coefficient: with [sin((2n+1)theta)]Q_q=-(n-q)a_n^2/[4(n+q+2)] (222 (10)) and S_M=-2k^2 Q_k/n'_0
  (222 (12)), the sin(1043 theta) coefficient is 2k^2(n-k)a_n^2/[4n'_0(n+k+2)]=k^2(n-k)a_n^2/[2n'_0(n+k+2)],
  matching line 41 and 222 (13). 1043=2*521+1; only the pair (521,521) reaches that frequency because the
  polar velocity of mode n has frequencies n+-1, so a_n^2 alone contributes and a low-mode repair cannot.
- Formula 222 (10) itself was rechecked numerically (convention Laplacian psi=-d_x rho, u=grad-perp psi, single
  mode, unit a_n) for (n,q)=(7,0.3),(13,k),(521,k): agreement to about 1e-14. Scratch:
  agent_243/check2.py.
- Log coefficient source: d_q of U[Phi_q].grad Phi_q=r^(2q-1)Q_q times -k^2 gives -k^2 r^p(2 log r Q_k+d_qQ_q),
  the linear r^k terms cancel exactly (ell0 k=1, proof 217 lines 73-77), X.grad R=O(r^p) has no log, cross terms
  with R are O(r^(3k-2) log r)=o(r^p). So (3) holds with the stated S_M.
- k=0.1793605..., p=-0.6412789..., 4k=0.7174421...; k-4<p, 3k-2<p, k-1<p all true.
- Strain kernel: c[h]=(1/pi)int sin(3theta)r^-3 h (proof 213). sin(3*pi/6)=1, and K q0>0 on all four reflected
  disks (K and q0 are both even-x, odd-y). Hence c[q0]>0.

## Findings

1. (cosmetic) Line 45: the uniform O(r^p) remainder is attributed to the homogeneous interaction and the
   O(r^(3k-2)(1+log r)) remainder; it also contains -k^2 r^p d_qQ_q and X.grad R/n'_0. Both are O(r^p) and are
   covered by the cited 222 (11)-(12), so nothing changes.

2. (cosmetic) Line 57: U[q]=O(r^-3) is stated for the canonical (far-subtracted) velocity without saying that
   the compact subtraction constant vanishes by parity (226 clarification 1, 222 line 52). As noted in check
   (2), the conclusion needs only U[q].grad rho0=o(r^p log r), which already follows from the general E2
   velocity bound; no gap.

3. (cosmetic) Line 55: "Tq ... is at least C1" relies on local regularity of U[rho0] near the bump; that holds
   (C6 joins, proof 217 line 90), and the proof itself says domain membership is not needed for the norm bound.
   J(q)=0 is asserted without stating why; it holds because q vanishes near the origin (cubic normalization).
   Not used in the norm estimates.

4. (cosmetic) Lines 37, 41: positivity uses n'_0>=3 (topics31/35 via 222 clarifications); only n'_0 nonzero
   and a_521 nonzero are needed. Aout[259,0] is a nonzero dyadic rational, so a_521 is nonzero.

5. (scope) Line 18: R_alpha must also exceed half the radius beyond which (5) holds and the radius in 226 (1);
   this is implicit in "sufficiently large". The lower constants do not depend on the cutoff at all.

6. (scope) The CLAIM wording "R^(k-1)(1+log R) is valid only for C_ren" should be read as: valid for Cren by
   topics214/226 (and for C0 restricted to ker c), not proved here. The proof's line 92 is correctly hedged
   ("in the corresponding earlier scope").

## Conclusion

The two-sided rates (1)-(2) are correctly derived: the lower bound is a genuine operator-norm bound from one
fixed admissible input, the M0 logarithmic column is exactly nonzero and cannot be cancelled by the velocity
part, and the upper bounds quoted from proof 226 match exponent for exponent, including gamma=2 and gamma>2.
The faster rate R^(k-1)(1+log R) is correctly refuted for the full C0 on unrestricted inputs.
