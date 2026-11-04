# Independent comparison of two actual Pan-Zhang author manuscripts

The submitted version comparison has SHA256 5b85d0a0a0f564919d1668e5e756ca75316db16fa04f7d55eca16597088539b9. All five sections and22 manual checks were read. This audit concerns the exact retained PDFs, not an assumed publisher version. It independently checks the printed counterexamples, the precise sequel statements and the planar regularity argument. The existing configured model comparison remains pending at initial writing.

## 1. Sources and reading coverage

The retained first PDF, *Unique continuation of Schrodinger-type equations for partial_bar*, by Yifei Pan and Yuan Zhang, has28 pages and SHA256 2ec50b48aaa6e7ea0761fa74c86567c68fd4a194c1d02f8fe215fd8230a82582. The retained second PDF, *A remark on unique continuation of partial_bar*, has12 pages and SHA256 6889cfa47af191d69ae4b4b9c343c37566936c809a0849cdc2ad1249e0ab0a6f. Both are in `verification`, together with the literature agent's HTTP retrieval record, extracted text and PDF metadata. This agent independently accessed the retained files and checked their hashes; it did not perform those HTTP retrievals.

The first PDF's printed pages11 and20-22 were read. The second PDF's pages1-3,7-8 and10-12 were read in full. Rendered first-PDF pages11,20,22 and second-PDF pages3,11 were visually inspected. The metadata creation dates2025-10-10 and2026-01-12 are not verified publication dates or version dates. The earlier v1 audits retain their own different PDF hash. No unseen journal version is included.

## 2. The Example4 coefficient mismatch remains in the first PDF

Use dbar=(partial_x+i partial_y)/2. Take the permitted real sequence a_j=2^(-j-2), j>=1, in the smaller printed disc B(0,1/4), and choose h=1. Put

    L0=log|z|^2, Lj=-log|z-a_j|^2,
    u=1/(L0 product_(j>=1) Lj^(1/j^2)).

Around a1=1/8 set w=z-a1 and

    H=1/(L0 product_(j>=2) Lj^(1/j^2)).

On |w|<1/64 the other a_j have distance at least3/64, and0 has distance at least7/64. All logarithms entering H are bounded away from their singularities and zero. The series of logarithms defining the product and each of its derivatives converge uniformly on compact subsets: each derivative is uniformly bounded in j and is multiplied by1/j^2. Thus H is smooth and nowhere zero on this disc. Since u=H/L1 and dbar L1=-1/conjugate(w),

    q:=(dbar u)/u=(dbar H)/H+1/(conjugate(w)L1).

The k=1 term of the printed potential is H/(conjugate(w)L1^2). The first printed term and the sum over k>=2 are O(1/L1), by the same uniform distance bounds and summability. Hence

    V_printed/q -> 0 as w->0, w!=0.

Here |q| is asymptotic to1/(|w|L1), which diverges; the bounded dbar H/H cannot cancel it. The equation dbar u=V_printed u would instead require V_printed/q=1 wherever q and u are nonzero. The printed formula therefore fails on a punctured neighborhood. This is an algebraic mismatch, not a removability issue.

Direct logarithmic differentiation gives the correct product-free coefficient

    -z/(|z|^2 L0)+sum_(j>=1)(z-a_j)/(j^2 |z-a_j|^2 Lj).

Moreover |u|/|w| is asymptotic to a positive constant divided by |w|log(1/|w|), so the continuous zero extension at a1 is not locally Lipschitz. This is no smooth scalar or Euler counterexample. Nothing here refutes a main continuation theorem.

## 3. Two noncompact Carleman scopes fail as printed

Proposition6.3 in the first PDF states, for all half-integers lambda and global H1 functions vanishing near0,

    integral |u|^2 r^(-2lambda-2) <=16 integral |dbar u|^2 r^(-2lambda),

and its partial analogue. Let chi be a smooth radial function, zero for r<=1 and one for r>=2. Set u=chi(r)z^(-2), interpreted as0 near0. This is smooth and globally H1: its exterior squared function and derivative integrals are bounded respectively by constants times integral_2^infinity r^(-3)dr and integral_2^infinity r^(-5)dr. The dbar derivative is compactly supported on the transition annulus. For lambda=-5/2 the right side is finite but the left side contains2pi integral_2^infinity1 dr. The partial version fails with chi(r)conjugate(z)^(-2). Thus global H1 alone does not control these negative-weight tails.

Corollary6.4 permits merely local Hl and support away from0. Choose v=chi(r)z^2, k=1, l=2, alpha=(1,0), beta=(1,1), lambda=1/2. These satisfy the stated componentwise order and local H2 hypotheses. For r>=2, partial v=2z and partial dbar v=0. Its asserted left side contains8pi integral_2^infinity1 dr, whereas the right side is compactly supported and finite. The local-Sobolev formulation fails independently of the preceding negative-weight example.

## 4. The compact-annular repair and its scope

For a smooth compactly supported function on0<r<infinity expand all angular modes and set t=-log r. With w_k(t)=exp(lambda t)u_k(exp(-t)), the squared first estimate reduces to

    integral |w_k'+(k-lambda)w_k|^2
      =integral |w_k'|^2+(k-lambda)^2 integral |w_k|^2.

There is no end term because the support is compact in t. Every half-integer lambda has |k-lambda|>=1/2 for all integer k. Parseval, including all modes, gives the norm constant4 and squared constant16. Complex conjugation gives the partial form. Smooth approximation within a slightly larger fixed annulus proves the H1 version. Applying these inequalities successively to derivatives gives constant16^(l-k) in the corollary, with appropriately shifted half-integer weights. This also verifies the k=1,l=2 instance used above when support is compact.

For the first inequality, noncompact global H1 with lambda>=0 is sufficient: outside a fixed inner disc, both weights are bounded. Cut off at an increasing outer radius, apply the compact estimate and pass by H1 convergence and the vanishing cutoff error. This is a sufficient repair, not a maximal characterization of every negative weight. Theorem6.1 uses a compact outer cutoff and is not refuted by Sections2-3. Its valid strict planar vector argument was separately reconstructed in the team records.

## 5. Exact sequel statements

In the second PDF, n denotes complex source dimension and N finite complex target dimension. The norm of dbar u is Euclidean over all nN components. A domain is open and connected. L1 integral flatness at z0 means

    lim_(r->0) r^(-m) integral_(|z-z0|<r)|u|=0 for every m>=1.

Theorem1.4 assumes u in W1,1_loc(O;C^N),0 in O, and |dbar u|<=C|u|/|z| almost everywhere for a finite positive C. It concludes zero from L1 flatness for scalar N=1 with no smallness restriction on C, and for N>=2 under the strict restriction C<1/4. The printed theorem does not include vector equality C=1/4.

Theorem1.1 assumes W1,1_loc and a coefficient in Lp_loc with p>2n. Theorem1.2 is scalar, with u in W1,2n+epsilon_loc for some epsilon>0 and coefficient in L2n_loc. Theorem1.3 has complex source dimension n=2, finite target dimension, u in W1,4+epsilon_loc and coefficient in L4_loc. These are exact statement checks, not independent certification of their full higher-dimensional proofs. None supplies an arbitrary weak-L2 coefficient result or an estimate derived from the Euler hypotheses.

## 6. Independent planar bootstrap

Let u in W1,1_loc near0 in the plane satisfy |dbar u|<=C|u|/r and L1 integral flatness. For any M,m>0 and epsilon>0, sufficiently small s satisfy integral_(B_s)|u|<=epsilon s^(m+M). Summing the dyadic annuli in B_r yields

    integral_(B_r)|u(z)| |z|^(-M)
       <=epsilon 2^M r^m/(1-2^(-m)).

In this display the weight inside the integral is the radial function |z|^(-M); the r outside denotes the disc radius. Thus u/|z|^M is integrable and flat for every M. If u is locally Lp, p>1, and1<q<p, set epsilon=(p-q)/(p-1). The identity q=epsilon+p(1-epsilon) and Holder give

    integral (|u|/|z|)^q
       <=(integral |u|/|z|^(q/epsilon))^epsilon
          (integral |u|^p)^(1-epsilon)<infinity.

All integrals are on a fixed sufficiently small disc. Consequently dbar u is Lq. The standard planar local elliptic implication dbar u in Lq => u in W1,q,1<q<infinity, follows from the Cauchy kernel, the Lq boundedness of its Beurling derivative and the holomorphic remainder. These qualitative classical inputs are explicit dependencies.

Planar W1,1 gives local L2. Taking q=3/2 gives W1,3/2 and then L6. Taking q=3 next gives W1,3 and local boundedness. For each finite q choose a larger p, use boundedness to obtain Lp, and repeat the interpolation. This proves W1,q_loc for every finite q. Away from0 the coefficient is bounded and ordinary local bootstrap applies. Boundedness also gives integral |u|^2<=M integral |u|, transferring L1 to L2 integral flatness. All steps apply to finite vectors. This independently validates the planar regularity step in the source; it is distinct from the continuation step and introduces no smallness condition on finite C.

## 7. Higher-dimensional and historical limits

The sequel's proof invokes restrictions to complex radial lines. Lemma3.4 on page7 was read here, including its use of v=u^2, Holder and Morrey when p>2n. Lemma3.3 and the complete slicing chain were not read, so no collective independent certification of the higher-dimensional extension is made. The submitted source comparison says those two proofs were unread in its own files; that is consistent with this agent having additional coverage of Lemma3.4.

The original Pan-Wolff1998 manuscript has not become available in the retained evidence. A citation, publisher metadata or the sequel's re-use of its gradient inequality does not count as reading that original. The sequel's strict vector theorem does not independently certify the new closed-endpoint argument. The separate LIT349 and LIT350 submissions require their own audits. No general real-carrier reconstruction or Euler quotient control is obtained.

## 8. Verification record

The source hash, exact PDFs, retrieval evidence, extracted texts and five inspected images are retained in `verification`. No mathematical computation, formalization or new model call was used. Existing configured model comparison is requested through the permitted working files; actual provider execution is independently unattested. Only the local printed claims and the explicit planar argument above are within this review's scope.

## 9. Existing model comparison

The complete Theory Agent C note dated2026-11-04T04:46:17Z was read. Items1-4 agree with the two actual manuscript hashes, the smaller disc in the first Example4, its unchanged erroneous factors, both noncompact Carleman hypotheses, the sequel's four theorem statements and the planar bootstrap. The comparison independently accessed the same author-hosted PDFs as text; this agent retains the visual coverage listed in Section1 and does not infer that the other agent viewed rendered pages. The factor separation holds in the smaller disc because a1=1/8 and the selected radius1/64 stay inside it.

The sequel's reference10 describes the first paper as Comm. Anal. Geom., to appear. That bibliographic notice identifies an intended venue, not a final typeset version or a publication date. Metadata creation dates also do not establish publication. The direct proofs of the three defects apply to the retained28-page author file; they do not extend automatically to unseen journal pages.

The comparison supplies no full independent proof of the higher-dimensional slicing chain. The theorem-statement check and planar regularity result are confirmed at the scope stated here; no collective higher-dimensional certification is claimed. The closed vector threshold has the separate A2930 proof, and LIT350 has its separate distributional reconstruction. Actual provider execution of the existing configured model agent is independently unattested. No new client or computation was used.


## 10. Confirmed-source status revision

The exact current source has SHA256 e6d205cb60bba2d97b4d0e8b7b558ae50b0623b2b7dad50cf51ec10dcafbc8bd. The full difference from the retained submission has been read: one opening status line changes, and one final comparison section is added. The opening and final section cite A2937-A2939 at their exact source, statement-extraction and planar-bootstrap scopes. The note expressly declines to infer that the literature agent read Lemma3.4 merely because this auditor did. The source and higher-dimensional limitations remain explicit. No displayed equation, mathematical hypothesis or proof argument changes. The old pending sentences belong to the dated original submission and are superseded by the new status section. The capture and complete difference are retained in verification.
