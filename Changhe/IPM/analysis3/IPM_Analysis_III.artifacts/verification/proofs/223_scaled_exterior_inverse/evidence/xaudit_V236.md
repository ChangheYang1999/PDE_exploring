# Independent audit of V236 / proof 223 (actual exterior inverse in scaled far Holder norms)

Audited file: verification/proofs/223_scaled_exterior_inverse/PROOF.md
sha256: 30980d7ffb01e0df479447034809d21c5c413f15c3693688c810323f4e6b0530 (recomputed, matches the task and evidence/check.json).
Evidence: evidence/check.json (dependency hashes only, "computation: none"). I recomputed the three listed dependency
hashes: proof 35 f6b46867..., proof 117 20b9e69c..., proof 222 d5a1747b...; all match the current PROOF.md files. The proof 222
sidecar LOCAL_COMMUTATOR_CLARIFICATION.md has sha256 8d031b03..., matching the hash recorded in proof 222's check.json.
Context read: proof 222 (PROOF.md and sidecar) in full, topics 220 and 221 in full (for the drift and characteristic
arguments that proof 223 says it follows), the opening of proof 117, and the INDEX entries for 213 to 223.

VERDICT: PASS WITH REMARKS

Summary. The argument is correct. The exterior is forward invariant because the radial part of V is at least ell r/2;
the actual flow is a dilation at the exact rate ell=1/k up to bounded multiplicative errors, uniformly for R>=R0; the
composition f(Phi_t .) grows in the scaled annular norm exactly like exp(ell beta t), so exp(-t) wins precisely when
beta<k, with constant 1/(1-ell beta)=k/(k-beta). Homogeneous solutions grow like r^k along orbits and are excluded by the
r^beta annular bound, so no inner boundary condition is needed or allowed (the circle |X|=R is the inflow boundary of
the exterior, and the trace of the solution there is determined by f). The weighted L2 bound is correct in both regimes
and the two regimes cover every gamma>4k. The cutoff extension and restriction maps are uniformly bounded, the coupling
B_R is small through the output tails proved in proof 222, and the Neumann formula (15) is a genuine two-sided inverse on
the exact maximal domain D_R. The statement is carefully scoped. I found no gap and no exponent error. The findings are
justification remarks and typos.

## Findings

1. TYPO (line 39, drift integral). With r_s>=r exp(ell s/2) one has
   integral_0^infinity C r_s^(k-1) ds <= C r^(k-1) * 2/(ell(1-k)), not C r^(k-1)/(ell(1-k)). The factor 2 is absorbed in
   the generic C and does not affect (4). Repair: write 2C, as proof 221 (4) does with its factor 4.

2. REMARK (lines 49 to 53 and 63 to 71, enlarged annuli). The sentence "Finite overlaps of the annuli imply the same
   bound on every comparable-radius enlarged annulus" is correct but deserves its one-line proof, since it carries the
   whole seminorm estimate (8). If Y,Y' lie in the closure of Omega_R with |Y|<=|Y'|<=2|Y|, choose i with
   r_i<=|Y|<2r_i; then both points lie in A_(i,R). If |Y'|>2|Y| then |Y-Y'|>=|Y|, and the difference is bounded by the
   supremum part, 2CN|Y|^beta<=CN|Y|^(beta-alpha)|Y-Y'|^alpha. Hence for all Y,Y' in {s/C1<=|Y|<=C1 s} intersected with
   the closed exterior, |f(Y)-f(Y')|<=C(C1,alpha,beta)N s^(beta-alpha)|Y-Y'|^alpha, uniformly in R and s. With (6) for
   output pairs at distance at most r_j/4 and the supremum bound for farther pairs, this gives (8) exactly as stated,
   including negative beta (the lower bound in (4) is used there). I rederived each step; it is fine.

3. REMARK (line 77 and line 122, characteristic identity). "Local flow boxes" and "Flow boxes imply the same identity
   distributionally" are sketches. They need V in C^1 and nonvanishing on r>=R0/2, which holds: the far velocity is a
   finite modal sum with termwise cylinder derivatives (proof 117), and the radial component is at least ell r/2. Either a
   C^1 flow-box change of variables (as in topics 220/221) or Friedrichs mollification with V Lipschitz gives the integral
   identity for almost every transverse coordinate, then for every point by continuity, and at boundary points |X|=R by
   letting the initial time tend to 0. In the converse direction, Q_R f has a continuous classical derivative along every
   orbit, jointly continuous in flow-box coordinates, so the classical and distributional V.grad agree. Suggested repair:
   cite the proof 220 paragraph explicitly instead of only "as in topics220/221". Not a gap.

4. REMARK (lines 81 to 103, gamma bookkeeping). Both bounds are correct: (10) uses only |Phi_(-t)Z|>=c|Z|exp(-ell t)
   and the exact Jacobian exp(2 ell t); (11) has denominator 1+ell-ell gamma/2, positive iff gamma<2+2k; (12) is
   integrable iff gamma>2+2beta. The pointwise route therefore already works on the overlap 2+2beta<gamma<2+2k, so the
   semigroup bound is only needed for 4k<gamma<=2+2beta, a nonempty interval because beta>2k-1. The constant in (11)
   blows up as gamma increases to 2+2k, which is harmless for fixed gamma but is avoided by switching to (12) at any
   gamma>2+2beta. Optional clarification only.

5. REMARK (lines 5 and 17 to 21, scope of the transport part). The transport inverse and its uniform bound (13) do not
   use beta>2k-1 or gamma>4k: they hold for every real beta<k and every gamma>0, with R>=R0. The restriction to
   2k-1<beta<k and gamma>4k is needed only for the coupling part (membership of M0 in Z and the negative tail exponents in
   (14)). The theorem is stated in a narrower range than proved, which is not an error.

6. REMARK (line 23 and line 126, the cutoff eta). The statement does not say 0<=eta<=1. "The weighted L2 norm does not
   increase" needs it; otherwise insert the factor sup|eta|. Also make explicit the case of a Z-annulus [2^j,4*2^j] that
   straddles the inner circle: for X with |X|>5R/4 and X' with E_R h(X')=0 one has
   |E_R h(X)|=|eta_R(X)-eta_R(X')||h(X)|<=C min(1,|X-X'|/R)|h(X)|<=C(|X-X'|/R)^alpha N R^beta, and 2^j is comparable to R
   on such annuli, so the scaled seminorm is uniformly bounded. Annuli not meeting the transition shell 5R/4<=|X|<=2R lie
   entirely on one side, where eta is constant. With chi supported in B4 and 5R/4>4 for R>=4, the local E2 factor of
   E_R h vanishes. The P_R bound follows from 2^m<=R<2^(m+1), which puts A_(j,R) inside A_(j+m) union A_(j+m+1), together
   with the ratio-2 argument of finding 2. I verified ||E_R||, ||P_R||<=C uniformly.

7. REMARK (line 145, the identity outside 2R). "For |X|>=2R, E_R h=h and its derivatives agree locally" is literally
   true on the open set |X|>2R; on the circle |X|=2R the identity A0(E_R h)=A_R h holds by continuity, or directly because
   V.grad(eta_R h)=eta_R V.grad h+h V.grad eta_R and V.grad eta_R vanishes where eta_R is locally constant up to the
   boundary of its plateau. It is also worth one sentence that E_R maps D_R boundedly into the proof 222 domain D_Z:
   V.grad eta_R=eta'(|X|/R)(V.X)/(R|X|) is O(1) with scale-R derivative bounds on the transition shell, so h V.grad eta_R
   is in Z with norm at most C||h||F_R. This makes "the actual A0 expression applied to E_R h" an evaluation of the closed
   operator A0 of proof 222, and gives the explicit transition discrepancy
   A0(E_R h)-A_R h=(eta_R-1)T_R h+h V.grad eta_R on R<=|X|<=2R, consistent with the stated limitation.

8. REMARK (dependencies). The cited proof 222 inputs are exactly: C0=Cren+c[.](M0-H0), equivalently
   C0 h=U[h].grad rho0+c[h]M0, bounded on Z for p<beta<k; the strain bound (5); the tail bound (2) for
   (1-chi_*(X/s))U[.].grad rho0; and (9) for (1-chi_*(X/s))M0. Since 1-chi_*(4X/R)=1 on |X|>=R/2, B_R equals
   P_R(1-chi_*(X/s))C0 E_R with s=R/4 (the compact H0 term drops out for large R), and (14) is the sum of those bounds.
   All four exponents k-1, beta+k-gamma/2, p-beta, 2k-gamma/2 are strictly negative in the stated range (the second
   because gamma>4k>2beta+2k). Topics 220/221 are cited for the drift argument but not listed in check.json; the argument
   is reproduced inline, so this is only provenance. This audit takes the proof 222 estimates as given (I checked their
   statements and the exponent arithmetic in its proof, not every kernel estimate of proof 222).

9. TYPO (throughout). Missing spaces such as "equal0", "and1", "at mostCN", "tends to0", "the grids 2^j and2^jR". Harmless.

## Independently verified, and how

- Hashes: PROOF.md, the three dependency PROOF.md files, and the proof 222 sidecar (sha256sum).
- Constants: k=0.179360531..., ell=5.575362..., 2k-1=-0.64128, 4k=0.71744, 2+2k=2.35872 (exact rational arithmetic).
- Forward invariance and exit: V.X/|X|>=ell r-Cr^k>=ell r/2 for r>=R0/2, so radii increase at least like
  r exp(ell t/2); the exterior is forward invariant, backward orbits reach |X|=R in finite time, so |X|=R is the inflow
  boundary. By hand.
- (4), (5), (7): Gronwall on exp(-ell t)DPhi_t with ||DU||<=Cr^(k-1), Liouville with div V=2 ell exactly (the canonical
  IPM velocity symbol is divergence free). Numerically sanity checked on a toy divergence-free field with the physical
  parities, U=grad^perp(A r^(k+1)sin 2theta), by RK4 of the flow and variational equation: |Phi_t X|/(r exp(ell t)) stayed
  in [0.95,1.05], ||DPhi_t||/exp(ell t) in [1.00,1.05], and det DPhi_t/exp(2 ell t)=1.000000 to six digits.
- (8), (9): the composition estimate by hand (finding 2), and the time integral
  integral_0^infinity exp(-t)exp(ell beta t)dt=1/(1-ell beta) in sympy.
- (10), (11): the change of variables and weight ratio by hand; the integral 1/(1+ell-ell gamma/2) and the threshold
  gamma=2+2k by sympy.
- (12): integral_R^infinity r^(2beta+1-gamma)dr=R^(2beta+2-gamma)/(gamma-2beta-2) by sympy; gamma-2beta-2>=2(k-beta) and
  the R-power at most beta-k by hand.
- Characteristic identity: d/ds of -exp(s)integral_s^infinity exp(-v)f(v)dv equals the same expression plus f(s) (sympy),
  giving V.grad Q_R f=Q_R f+f; the endpoint exp(-t)h(Phi_t X)=O(r^beta exp((ell beta-1)t))->0 for h in F_R gives
  Q_R T_R h=h; homogeneous solutions satisfy |h(Phi_t X)|>=c|h(X)|(|Phi_t X|/r)^k and are excluded by beta<k.
- Neumann formula: A_R=(I+B_R Q_R)T_R on D_R, so Q_R(I+B_R Q_R)^(-1) is a right and a left inverse, with norm at most
  K/(1-K||B_R||). By hand.
- E_R, P_R uniform bounds and parity/axis preservation (finding 6), and the identity outside 2R (finding 7). By hand.

## Scope I consider proved

Fix 0<alpha<1, 2k-1<beta<k, gamma>4k. Granting the far velocity bounds (3) from topics 35/117 and the proof 222 estimates
listed in finding 8, the following hold.

(a) There is R0 such that for every R>=R0 the exterior transport T_R=V.grad-1, with the actual field
V=ell X+U[rho0], is a closed bijection from the maximal domain D_R onto F_R, with inverse given by the forward orbit
integral (1), and ||Q_R||F_R->F_R<=K with K independent of R. No inner boundary condition is imposed; uniqueness comes
from the growth bound beta<k. (This part in fact holds for every beta<k and gamma>0.)

(b) There is R1>=R0 such that for every R>=R1 the operator B_R=P_R C0 E_R satisfies ||B_R||<=C epsilon(R/4)->0 with
epsilon as in (14), and A_R=T_R+B_R is a closed bijection D_R->F_R with inverse (15) and ||A_R^(-1)||<=2K.

(c) On |X|>=2R, A_R h coincides with the full proof 222 expression A0 applied to E_R h; on R<=|X|<=2R they differ by the
explicit cutoff terms of finding 7.

Not proved and not claimed: any global inverse of A0 on Z, patching of the exterior inverse to the middle or origin
regions, treatment of the transition shell, the cubic normalization constraint, a complement or projection certificate
for Avenue IV, nonlinear closure, Sobolev condition (I), or any explicit radius or constant.
