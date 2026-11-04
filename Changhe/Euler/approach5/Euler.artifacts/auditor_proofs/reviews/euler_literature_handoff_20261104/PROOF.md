# Scope audit of the main Euler literature handoff

## 1. Exact object and scope

The object audited is the handoff in the team records in the literature agent, at SHA256 978b3bb8c60fb3a70cd876c63e4068b685fd0719377b9b1a084224a31f1e8b0a. All seven sections were read. The longer literature review, Sections 1-5.10, the entire current Liu audit, the rotating-period-map proof, and the inviscid-adjoint proof were compared. Selected theorem statements from ten retained primary-source text extractions were then read directly. Their exact excerpts and source hashes are retained in the team records.

The question is whether this handoff asserts an unconditional theorem for globally C2, decaying, rotating Euler profiles that is not supplied by its sources. The answer from these checks is no. This is an integration and scope audit, not a new proof of all the external theorems. In particular, it does not re-read every page of the ten manuscripts, establish the missing 2023 results, or certify the entire 149-PDF inventory. The current Liu PDF and its earlier full-proof audits remain explicitly identified dependencies.

## 2. Parameter conversion and physical norms

Let 0<c<1/2, let omega be any finite real number, and let J(x1,x2,x3)=(-x2,x1,0). Set alpha=1/c-1. Since c is positive,

    2/5<c<1/2 if and only if 1<alpha<3/2,
    alpha<=3/p if and only if c>=p/(p+3), for finite p>0,
    alpha>3/2 if and only if c<2/5,
    3/(1+alpha)=3c,
    3-2alpha=5-2/c.

Thus the first Chae-Shvydkoy exclusion with finite p>=3 starts at c>=1/2, and the second ends below c=2/5. At p=infinity the first bound is alpha<=0. Neither range contains the primary interval. The natural ball-energy power 5-2/c lies strictly between zero and one. A bound E(R)<=C R^(5-2/c) permits unbounded total energy.

For an exact physical similarity field with this scaling, a spatial Lp norm scales as

    ||u(t)||_p = (T-t)^(c-1+3c/p) ||U||_p

for finite p, and with exponent c-1 for p=infinity. Orthogonal rotating factors do not change this formula. A finite profile norm therefore does not by itself imply a physical norm bounded uniformly up to T. The physical-flow premises in Constantin-Ignatova-Vicol Theorem 2.1 and Remark 2.2 cannot be silently obtained from profile membership.

For a vorticity tail r^(-1/c) W(theta), where W is bounded on the sphere and nonzero on a set of positive angular measure, its radial p-integral has the power r^(2-p/c). It converges at infinity exactly for p>3c. This explains why such a tail does not meet a theorem requiring a vorticity power p<3c. This calculation concerns a stated nondegenerate tail, not an asymptotic expansion derived from decay.

## 3. Rotation, the actual period map and Bernoulli obstruction

Suppose U,P are globally C1, div U=0, U=o(|y|) uniformly, and solve

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0.

Put R_s=exp(omega J s), V(y,s)=R_s U(R_s^(-1)y), and Q(y,s)=P(R_s^(-1)y). Direct differentiation gives

    partial_s V=omega JV-omega (Jy).grad V.

Applying the orthogonal change of variables to the profile equation gives

    partial_s V+(1-c)V+(cy+V).grad V+grad Q=0.

For omega!=0 the pair is periodic with period 2pi/|omega|. For omega=0 it is stationary and every positive period works. More generally it is relatively periodic for every L>0 with relative rotation R_L.

Let Phi be the complete flow of B=(cI-omega J)y+U. Completeness follows from at-most-linear growth; uniform sublinearity and the radial identity B.y=c|y|^2+U.y confine every backward orbit. If X_{s,0} is the nonautonomous flow of cy+V, differentiation and uniqueness give X_{s,0}=R_s Phi_s. Its actual untwisted period map is therefore

    R_L^(-1) X_{L,0}=Phi_L.

The additional condition used in the Liu rotating criterion is precise: there is one L>0 such that for almost every y there are an integer m>=1 and a point p with Phi_(mL)(p)=p and Phi_(-mnL)(y)->p. Approach to a periodic orbit as a set does not imply this condition. If that orbit has minimal period T, the sampled limit requires mL to be an integer multiple of T, as well as convergence to a phase point. No such statement follows just from relative periodicity of the velocity field.

Put Omega=curl U, X=cy+U and a=1-2c. Define

    H_rot=P+|U|^2/2+((cI-omega J)y).U-ac|y|^2/2.

Direct differentiation and the profile equation give

    grad H_rot=-aX-Omega cross B,
    B.grad H_rot=-a X.B.

At B(p)=0, its gradient is -a omega Jp. The sign and critical-set reductions used in the ordinary Liu proof are therefore unavailable in general. For omega!=0, the exact constant profile b=(-c,omega/2,0), with P=-((1-c)b+omega Jb).y, has X.B=-omega^2/4 at y=(1,0,0). It violates the putative nonnegative sign but is not decaying. The handoff retains exactly this limitation and does not present it as a target counterexample.

The ordinary theorem and its C1 pullback, rank-capture and countable null-basin arguments remain the already checked A010/A2776. The statement read from Liu Theorem 7.3 expressly retains the actual-period-map condition. The handoff does not replace that condition by automatic convergence.

## 4. Direct comparison of theorem hypotheses

The retained Constantin-Ignatova-Vicol statements match the handoff. Theorem 2.1 assumes finite initial kinetic energy and the physical Type I gradient-of-vorticity bound. Equation (3.8) is explicitly introduced as an assumption. Theorem 3.8 uses a local outgoing inequality at a vortical stagnation point; Theorem 3.9 additionally invokes the section's normalization, equation (3.8), and the finite stagnation set in Definition 3.7. Theorem 4.5 is axisymmetric and cites (3.5) and (3.8). The handoff separately labels the campaign's transport-based sublinear strengthening; it does not attribute that stronger statement to the printed theorem. Equivariant axisymmetry gives JU-(Jy).grad U=0, so rotation about that axis disappears only within the symmetry class.

Pineau-Vicol Theorem 1.4 expressly concerns Navier-Stokes and the fixed Type I bound. It has small- and large-rotation thresholds depending on that bound. Its text says the intermediate regime remains open. No inviscid or arbitrary-rotation theorem is imported from it.

Chae-Shvydkoy Theorems 3.1, 3.2, 4.1 and 4.2 retain, respectively, the critical energy and two-sided tail premises; the associated pressure and velocity-integrability range; vanishing strain and one strictly subcritical vorticity power; and exact exterior homogeneity. The handoff correctly keeps the bounded alpha=0 source-version defect separate from the target interval. A repair of displayed examples is not used to reject unrelated theorem arguments.

The direct Chae statements agree with the compressed rows: the 2007 theorem has all sufficiently small positive vorticity powers; the perturbation theorem also explicitly bounds the full gradient; the maximum-principle theorem has derivative decay and the strict exponent k>1/c; Chae-Tsai retains derivative and norm premises; and the zero-neighborhood theorem starts from velocity zero on an open neighborhood of the distinguished origin. The latter is stronger information than flat vorticity at an arbitrary point. The Xue theorem has C3 spatial regularity, finite-p space-time integrability and its specified associated pressure. Its allowed positive energy-growth power is not a nonexistence result in the primary interval.

These are statement and applicability checks. The handoff records exact inspected versions and explicitly leaves the three unavailable 2023 main manuscripts unverified. Their metadata and the separately read Chae-Wolf Appendix A do not substitute for the main theorems.

## 5. Adjoint and counterexample distinctions

For a C1 carrier B with div B=3c>0 and complete backward-confined flow, a C1 solution of div(Bw)=0 obeys w(Phi_(-t)y)=exp(3ct)w(y). Continuity bounds its value on the compact backward-orbit closure, forcing w(y)=0. For a merely continuous distributional solution, the same identity follows by pulling the weak conservation equation back through the C1 flow: the density w(Phi_t y)det D Phi_t is time-independent as a distribution and then pointwise by continuity. Thus the handoff's continuous formulation is valid. This says nothing against singular invariant measures or a different adjoint equation.

The local arbitrary-shear countertest A377 was rechecked from its full standalone proof. With a=1-2c, kappa=1+c and d0=c(1-c)+omega^2, it has

    U=(-cx-omega y, omega x+(c-1)y+f(x), z),
    P=d0(x^2+y^2)/2-omega axy+2omega F(x)-z^2,
    F'=f,  B=(0,-ay+f(x),kappa z).

The three momentum components cancel exactly, and div U=0. Taking f(x)=(1-2omega)x+x_+^p, 2<p<3, gives C2 but not C3 regularity near a point with B cross curl U nonzero. Its component U3=z fails decay; its backward y-flow can escape. It refutes a local equation-only regularization assertion, not one using global decay or trapping.

The remaining counterexample rows are faithful scope summaries of the prior audited constructions. A145 expressly covers centered-ball identities and a non-profile, not the vector equation on arbitrary domains. Auxiliary complex-vector continuation examples solve their own inequality; they do not supply a real divergence-free Euler velocity, its curl, or its pressure. At this handoff pin the target-2k construction is confirmed A3005, while the target-(k+1) construction is still submitted. The status boundary is correctly retained.

## 6. Conclusion and verification boundary

No new scope error was found in the pinned handoff. The unrestricted claim covering arbitrary finite omega in the C2 decaying class remains OPEN; the ordinary case omega=0 is already covered by the Liu theorem. The separately proved pressure and energy results do not remove the smooth-versus-C2 coverage gap or the basinwise helicity-sign assumption. The theorem in the analytic-interface review keeps those premises explicit.

The exact primary statements selected above, the current agent summaries, and the elementary deductions are the evidence for this conclusion. No new download, inventory-wide hash check, complete re-audit of all source proofs, numerical experiment or new model client is claimed. The existing configured model C comparison is checked in Section 7; actual provider execution is independently unattested.


## 7. Existing C comparison and precise evidence limits

The complete six-item C comparison of 06:26:02Z and its diagnostic qualifications were read. It agrees with Sections 1-6. In addition to the retained excerpt blocks, the definition of the finite nodal set in Constantin-Ignatova-Vicol Definition 3.7 and the definition of the strain tensor in Chae-Shvydkoy were reread directly from the retained primary text. These two definitions are outside the initial excerpt selection and supply the relevant qualifications in Section 4.

The complete final handoff-check script and both run logs were read. The final log reports thirteen symbolic checks and two exact negative controls, all passing. These cover elementary scaling and vector identities, not the analytic proofs of the cited theorems. The endpoint substitutions do not by themselves prove monotonicity on a parameter interval; the conversions in Section 2 follow directly from c>0 and p>0. The script assumes positive omega, but the manually derived algebraic identities hold for every real omega. The negative controls show a nonzero residual when the -z^2 or 2 omega F pressure terms are removed from the indicated nontrivial shear example; they do not say that the second term is necessary when omega=0 or f=0.

The first log has one failed power-simplification check. The final script uses T-t>0, the actual physical domain. A complete diff shows that the retained reconstruction of the first script differs only in that symbol declaration and a comment. It is not the original first script, so this verifies the reconstructed repair, not the exact original file history. Both final scripts set a nonzero exit status on their detected failures. This agent did not execute them.

The excerpt-matcher script and complete log were also read. They record equality of all 439 numbered lines in 22 selected blocks with the retained source text, and one altered-line negative control, for 23 passing checks. The matcher checks the displayed numbered lines, not completeness of a manuscript or truth of a theorem. The directly read blocks agree with its classification. An earlier weaker-control log was overwritten by its author and is not independently recoverable; no result here depends on it.

The comparison confirms the scope of the pinned handoff. Its historical SUBMITTED status for LIT358 is correct at that pin and is not a denial of the later A3011 result. The three unavailable 2023 manuscripts remain unavailable as full proof sources. No new unconditional rotating theorem, inventory-wide certification, novelty claim or source-proof audit follows from these comparisons.
