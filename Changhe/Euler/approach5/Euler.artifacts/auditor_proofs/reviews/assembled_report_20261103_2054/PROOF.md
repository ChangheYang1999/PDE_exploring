# Audit of Note117 and report pin fec0c41e

Status: scoped confirmation with one remaining summary-hypothesis defect. This is an audit of the exact report pin fec0c41e4698e801f8f222bbf1eea7afeb01611d953440da35d069e91fe15819, not a blanket certificate for every historical appendix entry. The unrestricted conjecture remains OPEN.

## 1. Evidence and coverage

The report has 6713 lines and 943276 bytes. Its retained baseline is the Note116 pin e20f4e3016e2e72abb4827821d7e99c7f15edd4438b9ab565424887bd224f647 audited in the team records. The complete independently generated delta was read, all 38918 characters. The complete companion deltas were also read: ASSUMPTIONS 40733 characters and PROOF_OBSTRUCTIONS 3990 characters. THEOREM_ATTEMPTS and README are byte identical to the baseline. No truncated output was used as complete coverage.

The verification manifest pins each complete current file and each independently generated diff. Full foundation blocks were compared between exact named headings, including every proof paragraph:

    2A: 36588 bytes, SHA256 9c4d20f5dfdb3908ca7f02c343cf6c37dd0a3c48dc941ccfbf8f1c9d9f533eea
    2B: 70148 bytes, SHA256 c985d7f5934eea5240954ee15d739b41fe54d858238b8142fbeb6cfa29fe8c46
    2C: 94353 bytes, SHA256 b8ba08dbf478df0f4a03bee4373b6d017241045c37a5e7eeca9da57cf04e31cf
    2D: 81689 bytes, SHA256 05a563640961fee790f1d1be2fdd3c63e14e3bb4f8fd9986f0d7c2eff167f923

All four complete blocks are byte identical. Thus their prior independent mathematical audits transfer without an assertion that their proofs were newly rewritten. Appendix A begins at line4685, B at5148, C at6542 and D at6679. The main scoped assembly considered here is front matter, Sections0-10 and AppendixA, lines1-5147. The changed B.7 sentence is checked separately below.

## 2. Repairs that now have their correct hypotheses

The former summary row2 blanket label is repaired. It now labels Theorems1 and4 PROVED and Theorem3 PROVED apart from (i) and the C2 form of(f), which are CONDITIONAL. Theorem5 retains its helicity-sign condition. This removes A2297 without strengthening the mathematical class.

The nonparallel gamma assertion now assumes that the positive X-orbit of a is precompact, W(a)!=0, and its limit set contains no zero of B=-X. These are precisely the hypotheses of A2265 and the correction A2299. For completeness, if W(a) is parallel to X(a), write W(a)=qX(a) with q!=0. The bracket transport with kappa=1+c gives W(Psi_t a)=e^(kappa t)DPsi_t(a)W(a), while DPsi_t(a)X(a)=X(Psi_t a). Hence W(Psi_t a)=q e^(kappa t)X(Psi_t a). Precompactness bounds W, and absence of X-zeros in the compact limit set bounds |X| below at all sufficiently late times, a contradiction. If X(a)=0 its stationary orbit already contradicts the same limit-set assumption. Thus the required nonparallel conclusion holds. The complete covector identity and sign conventions are retained in the team records Section2; the hypotheses now match it. In particular the escaping countertest to the old statement is no longer admissible. The corresponding B.7 sentence now also explicitly says precompact and is correct.

The scalar-multiplier row restores W(a)=f(a)W0(a)!=0 and the nonvanishing of W0 on the compact orbit limit set, so the zero-multiplier countertest to A2298 is excluded. However its new wording has lost a different hypothesis, addressed next. Confirmation of the repaired hypotheses does not approve the shortened scalar statement as a whole.

## 3. Remaining scalar-multiplier defect and an exact counterexample

The new AppendixA and ASSUMPTIONS sentence says that if W=fW0 with W(a)!=0 and W0 nowhere zero on the compact limit set of the positive X-orbit, then W has no zero on that limit set. The preceding displayed equations in that row concern X and W only. It does not say that W0 satisfies the same bracket equation. This omission is material. The previous shorter wording referred to a bracket pair, and B.7 still correctly refers to a known bracket pair.

Here is a globally smooth counterexample to the new unqualified sentence for every 0<c<1/2. In Cartesian coordinates define

    X=(-x,-(2+c)y,(3-2c)z),
    W=x e_y, W0=e_y, f=x, a=e_x.

Then div X=-1-(2+c)+(3-2c)=-3c and div W=0. With [X,W]=DW X-DX W,

    DW X=-x e_y,
    DX W=-(2+c)x e_y,
    [X,W]=(1+c)W.

The positive X-orbit of a is exp(-t)e_x. It is precompact and has compact limit set {0}. At a, W(a)=e_y!=0. W0 is everywhere nonzero, yet W(0)=0. Thus the sentence is false even with a precompact orbit. The missing equation fails because [X,W0]=(2+c)W0, not (1+c)W0. No Euler, pressure or curl relation was required by the kinematic row, so this counterexample lies in exactly its asserted class.

The repair is to require W0 to be a smooth field satisfying div W0=0 and [X,W0]=(1+c)W0, as in the full original A2266 proof. The product rule gives

    [X,fW0]-(1+c)fW0=(Xf)W0.

On the orbit starting with W(a)!=0, W0 never reaches a zero in finite time, by its invertible linear transport. Hence Xf=0 there and f is the nonzero constant f(a). At every limit point p, continuity gives W(p)=f(a)W0(p)!=0. This proves the repaired assertion. The divergence equation additionally gives W0.grad f=0, though the bracket equation alone suffices for constancy on this orbit. A2266 is unchanged and remains confirmed; the defect is its new summary formulation.

## 4. New local-pressure and strain insertions

The LIT295 insertion retains c=9/20, r=7/10, v=2/5, carrier speed one, the specified earlier pressure jets and the transverse leading potential Re((x+iy)^n)/n. Its rotation magnitude sqrt(65)/10 follows from r^2+v^2=65/100. It correctly distinguishes n=3 analytic leading germs and exact scalar transport with Poisson residual O(distance^4), from the n=4 impossibility of any full C1 next scalar for those earlier jets. The invariant -5299294616/615616875 and the exhaustion of all relevant free coefficients were independently checked in the team records. The insertion keeps the unresolved full n=3 scalar, general earlier data and global extension explicit. It does not claim that finite compatibility solves the full scalar equation.

The C66 insertion is a statement about weights satisfying TheoremSF.3 on the fixed product -lambda_min(S)<=6/5, |W|^2<=103/100. Thus its coefficient a is positive, as required by that theorem, and it may be normalized to one. Under that interpretation, weights exist for 0<c<=447/1000 and none for 179/400<=c<2/3, even when b and gamma are arbitrary real numbers. The complete independent exact proof is in the team records. At gamma<=0, S=0 and W!=0 already give negative density; for gamma>0 the exact three-point certificate and monotonicity in c give the upper obstruction. The nonlinear C65 profile corollary retains both pointwise bounds everywhere, Hb, C2 velocity and C1 pressure. The old Theorem8 result remains true.

The words arbitrary real coefficients must be read with the positive-a premise of TheoremSF.3. They cannot mean a=b=gamma=0 is forbidden from having nonnegative density: that zero density is trivially nonnegative but is not an admissible weight. The report explicitly says satisfying TheoremSF.3; repeating a>0 and arbitrary b,gamma in ASSUMPTIONS would make the shorthand clearer. The old open range 11/25<c<9/20 recorded with A2211 is historical; C66 now narrows the remaining threshold question to the interval between447/1000 and179/400.

LIT297 is correctly described as an endpoint first-jet failure of the directional argument. Its data satisfy the pointwise carrier identities for every omega and make grad log(E/H)=0 at exact ratio1/[2(1-2c)^2]. They do not satisfy an asserted neighborhood Poisson problem. Both the report and the obstruction list retain the full endpoint field theorem as OPEN. The constant25/2 is now identified as the largest constant uniform over the target open interval; at each fixed c the strict method condition is mu<1/[2(1-2c)^2]. Saying the method reaches that threshold describes its boundary, not a proof at equality, where the text explicitly states failure.

## 5. Scoped verdict and open work

All changed mathematical assertions in the front matter, Sections0-10 and AppendixA are confirmed at their stated scopes, except the scalar-multiplier sentence in Section3 of this audit. The same exception applies to ASSUMPTIONS. PROOF_OBSTRUCTIONS retains the conditional classes and correct method limitations. The four unchanged foundational proofs transfer from the prior complete audits, and the changed B.7 nonparallel sentence is confirmed.

A clean scoped approval of the exact fec0c41e report remains OPEN until the W0 bracket premise is restored. No blanket approval is given to the historical appendices. Two explicitly identified historical source packages remain pending: the flat-periodic checks and the vortical-horseshoe discussion. The unrestricted nonexistence conjecture, general off-axis positive-pressure zeros, arbitrary common-flat configurations and constructions of full profiles remain OPEN. No computation or new external model call was needed for this report audit.
