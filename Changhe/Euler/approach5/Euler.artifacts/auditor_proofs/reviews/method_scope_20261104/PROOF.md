# Scope of the remaining method-obstruction sentences

Status: independent audit and comparison with the existing Theory Agent C  review. The findings concern prose precision, not a withdrawal of any proved Euler theorem. The report reviewed is the exact 49861043 snapshot in the verification record.

## 1. Statements and notation

Fix 0<c<1/2 and a real rotation rate omega. Let Jx=e3 cross x, A=cI-omega J and B=Ay+U. A full profile satisfies

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0.

In the global statements U is C2 and P is C1. Smoothness and decay are additional hypotheses wherever the cited global theorem requires them. In reduced tail systems V,W,S,P are the explicitly listed auxiliary fields; they must not silently be identified with a global profile. Write X=Ax, L=(1-c)I+omega J, k=X.V and T=tr((DV)^2). For the profile variables, H=P+|U|^2/2+(Ay).U. A formal Lyapunov test for a C1 scalar function requires the prescribed derivative inequality for every admissible local jet in its stated domain.

The questions are whether the report's model tests establish universal necessity of a particular proof method, whether B27 satisfies every scalar identity developed in the campaign, and whether the formal classification excludes constants.

## 2. What a reduced countermodel proves

Let P0 be a list of premises and C a proposed conclusion. If an example satisfies P0 and violates C, then P0 does not imply C. A proof of C from stronger premises must therefore use some information not implied by P0. This does not identify a unique additional premise or a unique way of using it.

If the stronger *specified finite list* is exactly P0 together with P1, a proof from that list must use information from P1. However, this conclusion does not apply to an enlarged class of arguments with further global hypotheses, boundary conditions or consequences not included in the list. In particular, a model that violates the pressure equation does not prove that every possible proof must invoke that equation explicitly.

This is the quantifier distinction already recorded in A529, A2599 and A2603. It does not show that any new proof method succeeds; it only restricts what the countermodel establishes.

## 3. The B27 obstruction is restricted

The exact confirmed B27 construction, with 2/5<c<1/2, keeps a prescribed carrier B fixed while replacing its auxiliary fields by

    (W,v,H) -> (sW,sv,sH),  s>0.

The bracket relation, divergences, the prescribed-carrier Lamb identity, both helicity signs and the stated energy bound survive. Let mu be its compact regular-attractor invariant probability, n=W/|W|, S_v=sym Dv, ell=n.S_v n and b=S_v n-ell n. The putative pressure is

    P_s=sH-s^2 |v|^2/2-s(Ay).v.

It has Hessian O(s) uniformly on the compact support of mu. The genuine full-profile second-order scalar identity would require

    integral (s^2 |b|^2-n.D2P_s n) dmu
      =2+integral (s ell-1)^2 dmu.

The left side is O(s), while the right side is 3+O(s). Thus it fails for every sufficiently small positive s. The mean-stretching identity integral s ell dmu=1 also fails. No numerical limit argument is involved: the coefficients are fixed bounded functions on a compact set and the displayed expressions are finite polynomials in s.

Consequently the statement that these models satisfy every scalar identity developed so far is not supported and, when applied to B27 itself, is false. The parenthetical references to restricted scopes should be reflected in the main sentence. A precise replacement is:

    The specified reduced scalar identities admit the cited models at their recorded scopes. Those identities alone do not decide the sign. A proof needs a further property that the models fail, which could be a consequence of the pressure or momentum equations.

This does not claim that the B27 model has physical pressure or physical carrier-velocity coupling.

## 4. C65 and CO60

The C65 fields satisfy div V=0, W=curl V, k=X.V=0, X.grad V=-LV and grad k=X cross W-(1-2c)V. They are flat at the stated nonzero point, nonzero in every neighborhood, and realize either sign of T near that point. They do not supply the scalar S or the pressure premises of the full setting. Hence the listed equations plus flatness alone exclude neither sign. The source's revised Remark 1 now states exactly this.

For an exclusion within the full specified local system, one needs an additional premise, for instance information involving S or pressure. A global profile argument may instead obtain further global information not supplied by this local example. The report should therefore replace its unrestricted "must use S or the pressure" by "needs a further premise, such as a property involving S or the pressure".

The same distinction applies to CO60: its satisfaction of the listed reduced tail equations except Poisson shows that those remaining equations alone do not exclude it. A precise conclusion is that an exclusion needs the missing pressure relation or some other additional local or global input. Neither example classifies all possible nonexistence arguments.

## 5. Constants in the formal classification

For any constant C, the function Psi identically C has derivative zero along every formal jet. It satisfies either nonpositive or nonnegative derivative inequalities. Thus the literal phrase "no zeroth-, first- or second-order formal Lyapunov function" is false. The missing word is "nonconstant".

The confirmed classifications A044, A081 and A100 state, for omega nonzero, that the function is constant on the admissible jet space. The second-order conclusion is intrinsic: a nonconstant ambient formula that vanishes on the constraint set does not contradict it. For omega zero the correct variable is

    H0=H-c(1-2c)|y|^2/2.

With the report's nonpositive derivative convention, the permitted functions are the nondecreasing functions of H0, as checked in A2177-A2178. No classification on global decaying solutions, or at higher orders without their stated hypotheses, follows. The repaired first clause should read:

    No nonconstant zeroth-, first- or second-order formal Lyapunov function on the admissible jet space for omega nonzero (Theory Agent C C07, C15, C16).

The current omega-zero correction can remain. Adding the three source claim numbers improves traceability without changing the theorem.

## 6. The optional strain cross-reference

For bounded full C2/C1 profiles with 0<c<1, A506 proves that

    limsup_(|y|->infinity) lambda_max(sym DU)<1+c/2

implies DU tends uniformly to zero. Therefore a bounded profile for which derivative decay fails has extended-real limsup at least 1+c/2. Decay of U implies boundedness. The report's weaker lower bound 1 is true; it can be replaced by 1+c/2 with a reference to A506 and Section 6. No finiteness of that limsup is inferred. The critical Dini envelope in A506 has its own hypotheses and is not automatic from decay.

## 7. Comparison and verification scope

The existing Theory Agent C  01:30 and 01:35 notes were fully compared for the targeted findings. This audit agrees with their reduced-premise correction, source citations and optional strain reference, and also explicitly catches "every scalar identity" and the omitted "nonconstant". The C65 source was fully reread; the B27 independent proof, including its exact scaling countertest, was fully reread. The A506 argument and exact verdict were checked at the stated scope. The listed earlier formal-jet verdicts are dependencies, not a claim to have rerun their full proofs here.

No claim is made that every one of the Theory Agent C 's 333 citation checks was independently repeated. Existing configured model Theory Agent C  collaboration was used through files; actual provider execution is not independently attested. No new client, agent, mathematical computation or formal build was used.

## 8. Report consequence

The proved mathematical results retain their recorded scopes. The newly isolated prose defects need repair in the next assembly. Earlier cumulative approvals do not certify the stronger literal readings identified here; the new targeted findings qualify those readings. The unrestricted rotating decay-only conjecture remains open for arbitrary helicity.
