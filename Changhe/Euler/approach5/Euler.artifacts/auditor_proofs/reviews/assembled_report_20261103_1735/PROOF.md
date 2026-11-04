# Report Note99: repaired hypotheses and remaining source-scope wording

## 1. Version and method

The reviewed report is the 6245-line version assembled at 17:28Z, pinned at 2026-11-03T17:30:37.089166Z, SHA256 973e3afdf8a81042b3f696806fe577fe6f9b3f91e1d5c79ab0b1d9c7b98b9e2b. this report is byte-identical. Verification retains this version, the prior baseline, the 169-line report diff and complete README, attempts and obstructions diffs. The report diff was read in full except that the very long, previously audited AppendixB paragraph was checked by an exhaustive token diff with context; that token diff is also retained and was read completely. No unchanged long paragraph is claimed to have been reread in full in this delta audit.

Coordinator Note99 was read completely. The B-source repairs were independently checked in A1855-A1856. The latest Theory Agent C precision note was read and checked against the current report and earlier proofs, rather than accepted solely on its author's assertion.

## 2. Pressure normalization and Hardy time slices

For C1 divergence-free V and continuous P satisfying div div(V tensor V+P I)=0 near x0, the invariant pressure-deficit mean is M(r)=P(x0)-average_{|x-x0|=r}P. Its derivative is the spherical mean of ((V.grad)V).n. The revised LIT257 row now uses the comparison P(x0)-P>=kappa|V|^2 with kappa>0. Together with |(V.grad)V|<=K|V|^2/r it gives r M'<=K M/kappa. Since M(0)=0 and the comparison controls velocity, the finite-order and flat-germ conclusions have exactly the scope of A1698-A1702. The tail application separately notes P2(x0)=0 at a common flat point. Thus it no longer applies the estimate after an arbitrary pressure shift, and the A1818 flat-shear counterexample does not meet the repaired comparison.

The Hardy row now retains all time-slice premises of A1716-A1718: the weak stress equation, local integrability of v tensor v, v locally time-integrable with values in the solenoidal L2 space, and p locally time-integrable with values in the indicated global Hardy space H^q, 0<q<=1. The quadratic integrability is not inferred from the L1 time norm of v. These are faithful repairs of A1818-A1819. The external Hardy-space inputs remain labeled external.

## 3. W2 scopes and historical B statements

The B58 row now explicitly concerns the equality rate rho=-2(1-c), grad S(w) nonzero, with the hypotheses of B56. The conclusions about avoidance of the scalar zero sets and divergent component constants are not promoted to the strict-rate branch. The common component identity S=D_C|k|^q remains a rank consequence on its usual domain; the restricted claim is the stronger local geometry and blowup conclusion.

The B59-B61 row now distinguishes local C2 contact identities for 0<c<1/2 from escaping-direction conclusions in the actual helicity-free natural-profile class for 2/5<c<1/2. The latter use H9, H3, C1 local tail convergence and V in C2 or C3 near w. B60's supported-direction conclusion follows from the already established C1 scattering map. V in C3 supplies the pressure regularity by A1799. The report correctly says finite-jet T0, and leaves the C2 strict-rate branch open.

The corresponding changes in Remark6.1, Section7(R3), Section10(2) and AppendixB item1e preserve that distinction. B45 no longer carries an unnecessary nonzero-U premise in the updated conclusion. The all-order B51-B52 statements are explicitly consequences in an already empty decaying smooth helicity-free class; the C3 level-germ exception A911 remains separately identified. B62 now states DW=0 at a contact only for C2 velocity, and keeps its local consequence in the A1733 setting and on a fully saturated neighborhood. These changes agree with A1729-A1740 and A1792-A1800.

## 4. New scalar and global-ratio results

The LIT264 additions in the summary, research plan, table, README, T40 and obstruction file retain global twisted homogeneity, div V=0, k=X.V=0 everywhere, W.grad S=0, and two-sided positive finite comparison constants on the entire sphere. The smooth result has 0<c<1/2; the finite-regularity target version has 2/5<c<1/2, V in C2 and S in C3. Under those premises A1822 supplies a continuous closed W1,t normalized form across arbitrary zeros. Its global potential is constant on the complete explicit linear spiral orbits, so it attains its maximum on the sphere. The full three-dimensional equation is div(q|grad phi|^(m-2)grad phi)=0, m=1/c, with q positive and bounded above and below. The actual Serrin theorem checked in A1825 applies to the nonnegative function max(phi)-phi, with zero additive Harnack constant. The report does not replace this global argument by local continuation or assume a ratio derivative.

The LIT263 row accurately states the real scalar C1 intersect W2,2 full-disk trace inequality with a measurable symmetric uniformly elliptic coefficient and bounded lower-order coefficient, and continuation from infinite pointwise value order. It also records that conjugating the weighted m-equation preserves its principal weight. The short Section10 phrase 'pointwise unique continuation' should say 'continuation from infinite pointwise value order' to avoid suggesting that one zero suffices. For example the harmonic function u(x1,x2)=x1 has a zero and is not identically zero. The full row is already correct.

## 5. C55-C56: keep the local qualifier explicit

The C56 row preserves the distinction between the local tail-identity classification and its further refinement for actual tails of the C47 natural zero-helicity class. The latter uses P2>=0 at supported common zeros of V and W; it is not inferred from the local system. Its two exact local examples have no flat point and no asserted global realization. This agrees with A1828-A1833.

The C55 normalization repair is correct, but its first sentence should explicitly say 'on C sufficiently near x0'. Indeed the proof for one fixed component uses S=D_C|k|^q and |k|<=|X|sqrt(E), where E=|V|^2 and q>2. Thus

    |S|/E <= |D_C| |X|^q E^(q/2-1).

Only near the chosen zero x0 does this become <=epsilon for any fixed epsilon in (0,1/2). It then gives

    (1/2-epsilon)E I <= V tensor V+P I <= (3/2+epsilon)E I.

This is positivity of M and uniform positivity of M/E near x0, not on an entire component at all distances. The row's title mentions 'near a velocity zero', but putting the radius qualification in the assertion removes an otherwise avoidable ambiguity. No global positivity extension is certified here.

## 6. Three remaining C-source corrections

The C43 sentence at the end of the tail discussion still puts both conclusions under 'Kinematically'. Only the constant multiplier V=sigma grad k on a regular nodal arc has that scope. The assertion that each complementary disk of a closed regular nodal curve contains a critical zero needs the actual-profile exclusion A701 of periodic W curves. The full proof of A844-A850 was reread. At omega=0, for p=(1-c)/c in the target interval, the smooth punctured-space field

    V=(2-p) r^(-p)e3+p x3 r^(-p-2)x

is divergence free, homogeneous and helicity free, with k=2c x3 r^(-p). Its angular zero set is the regular equator, and neither complementary disk contains any zero of K. Its curl has circular orbits, so it fails A701. This refutes the purely kinematic reading. Split the report sentence after the multiplier assertion and begin the next clause 'For actual profiles, using A701'. The actual-profile theorem itself remains confirmed.

The C44 and C45 table rows still display A942 and A980 as live open configurations. Under their stated actual helicity-free natural-profile hypotheses the noninterior vortical nodal configuration is empty for every omega by A960-A964. The exact stable-rate argument makes the transported scalar vanish on an open saturation, contradicting noninteriority. Keep these rows as mechanisms, but explicitly state that the configuration is empty; C45 was submitted as a vacuous mechanism. The same historical prose in AppendixB should be labeled historical or followed immediately by the superseding conclusion.

Finally the current C36 source calls the isolated-tail-zero statement Proposition14, while the report still says Proposition9. Its mathematical statement is unchanged and A512 remains the correct audit dependency. Replace the source proposition number, since the same file also has a different Lemma9.

## 7. Verdict and limits

All substantive Note99 repairs and the newly inserted conditional theorems are confirmed at the precise scopes above. Whole-report approval remains open until the retained C43 wording and stale C44-C45 configuration labels are repaired. Also make the C55 locality, scalar infinite-order phrase and C36 source number explicit. The categorical phrase 'no bound on sup|curl U| follows from bare decay' in Theorem8 and the C59 row should read 'no such bound has been derived here': A1791 is an open inference, not a counterexample within the profile class. The same precision applies to T39's 'decay alone does not bound it'.

The relative-path source pins and reviewed diffs are evidence for this version only. No numerical computation or formal build was used. Configured model file collaboration continues, without independently attested provider runtime. The new LIT268-LIT269 submissions, received during this audit, are separate next tasks. Nothing here proves the original arbitrary-helicity bare-decay conjecture.
