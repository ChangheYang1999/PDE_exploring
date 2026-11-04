# Report delta at pin e20f4e30: conditional labels and dynamical scope

## 1. Statement, evidence and reading boundary

This is a mathematical assembly audit of the pinned this report with SHA256 e20f4e3016e2e72abb4827821d7e99c7f15edd4438b9ab565424887bd224f647. The baseline is f865716ee2d61ed1980b5ef012ccb1aded6d59515d599469bdb5127bd150fa44, whose front matter, Sections0-10 and AppendixA were approved in A2276. The new front/main/AppendixA occupies lines1-5139. AppendixB starts5140, AppendixC6534 and AppendixD6670.

All66652 characters of the report delta,27036 of ASSUMPTIONS,2765 of PROOF_OBSTRUCTIONS and9155 of THEOREM_ATTEMPTS were read. README is unchanged. The coordinator's entire referee disposition note was read. The manifest records the pinned bytes. These are reading and comparison statements, not substitutes for checking the claims.

The previous d0d9 historical AppendixB-D has now been read in full, but still carries only individual verdicts: historical flat-periodic and horseshoe packages remain separately queued. This review does not give a blanket historical recertification. It changes no full-profile theorem and does not solve the unrestricted decaying-profile conjecture.

## 2. The remaining summary label omission

At report line38, the complete-proof row still says "Theorems 1, 3 and 4 PROVED". The same report's front labels define PROVED to mean no premise beyond the stated problem class and explicitly mark Theorem3(i) and the C2 form of3(f) CONDITIONAL. The former needs an annular L2 vorticity bound; the latter uses its extra nonvanishing hypothesis at C2. Their arguments are complete, but the extra hypotheses have not been deduced from bare decay.

Therefore the blanket label is not consistent with the report's definition. This is REFUTED as reporting scope, not as a counterexample to either conditional theorem. The exact repair is to repeat the exceptions: Theorems1 and4 and Theorem3 apart from(i) and the C2 form of(f) are PROVED; those two parts are CONDITIONAL. The other repaired summary rows already do this.

## 3. The gamma row loses a compactness hypothesis

Set 0<c<1/2, kappa=1+c and delta=1-2c. For smooth vector fields X=-B,W satisfying

    div X=-3c, div W=0, [X,W]=kappa W,

let Psi_t be the X-flow and beta=(B cross W) dot dy. A2265 proves the covector identity Psi_t^*beta=e^(delta t)beta. It proves beta(a)!=0 under three further conditions: the positive X-orbit of a is precompact, W(a)!=0, and the limit set contains no B-zero. The new AppendixA row at line4696 and its ASSUMPTIONS copy omit precompactness.

The omission is false for the displayed kinematic class. Put nu=(1+4c)/2 and on all of R3 set

    X=(kappa*x,-nu*y,-nu*z),
    W=(x^2,-2*x*y,0).

Both fields are smooth. Their divergences are kappa-2nu=-3c and2x-2x=0. Direct differentiation gives

    (X dot grad)W=(2kappa*x^2,-2(kappa-nu)*x*y,0),
    (W dot grad)X=(kappa*x^2,2nu*x*y,0),

so [X,W]=kappa W. At a=(1,0,0), W(a)!=0 but X(a) and W(a) are parallel, hence beta(a)=0. The positive trajectory is (e^(kappa*t),0,0), defined for every t>=0, and has empty limit set. That set contains no B-zero. Thus the nonparallel inference fails exactly as written without a compact-orbit or corresponding explicit boundedness premise. This is a kinematic countertest, not an Euler profile or a target counterexample.

With precompactness restored the argument is valid. If beta(a)=0 and B(a)!=0, write W(a)=qB(a), q!=0. Bracket transport and preservation of B by its own flow give W(Psi_t a)=q e^(kappa*t)B(Psi_t a). Precompactness bounds W, while compactness and absence of B-zeros in the limit set bound |B| below at late times. This is impossible. If B(a)=0, the stationary orbit already violates the limit-set hypothesis. These are precisely the conditions of A2265, not a new stronger theorem.

## 4. The scalar-multiplier row needs a nonzero starting field

The same row says that a scalar multiple fW0 of a bracket pair with no zero of W0 on a compact limit set has none there. As an unqualified statement it is false: f identically0 satisfies the same divergence and bracket equations, but fW0 vanishes everywhere.

The valid A2266 statement concerns an orbit starting with W(a)=f(a)W0(a)!=0. Where W0 is nonzero, the equations for both W0 and fW0 give Xf=0 and W0 dot grad f=0. The invertible linear transport preserves nonvanishing of W0 at finite times, so f is constant along the orbit. If its compact limit set contains no zero of W0, every limit point p satisfies W(p)=f(a)W0(p)!=0. The starting nonvanishing premise is necessary and sufficient for this particular argument. The limit set and the field W0 must be those associated with this same orbit.

The other gamma conclusions retain their necessary limitations: the triangular theorem needs global product coordinates; the smooth-fiber return theorem needs transverse fibers through the limiting locus and a return extending with F(0)=0; the monomial theorem needs cyclic order matching and nondegenerate fiber connections. Their complete standalone arguments remain at in the team records. The historical B.7 insertion is read with its bounded case-(gamma) context and these individual verdicts; it is not a theorem about arbitrary smooth vector fields without that context.

## 5. The C62 insertion and the meaning of its numerical constant

The new C62 row and Section10 use the complete setting of the C60/C61 row: 0<c<1/2, arbitrary real omega, smooth local leading-tail equations on an X-flowbox about a common flat orbit Gamma through x0!=0, k=0, S=0 on Gamma, S<0 off Gamma and the Poisson equation for P2=S+|V|^2/2. These are extra local hypotheses. A2278-A2282 imply that every neighborhood contains |sym DV|^2>mu|curl V|^2 whenever

    2mu(1-2c)^2<1.

Consequently mu=25/2 works for every2/5<c<1/2 and every omega. The comparison with LIT294 is correct: the ranges coincide for0<c<=1/3; above that C62 is stronger. The pointwise relations used in the directional estimate have algebraic countertests above the threshold (A2283). This does not construct a local field solving the Poisson equation, a common flat germ, a global tail or a profile. The endpoint and field sharpness remain OPEN A2284.

PROOF_OBSTRUCTIONS calls25/2 the limit of the pointwise method. Precisely, it is the largest uniform constant over the entire open target interval: the infimum of1/[2(1-2c)^2] there is25/2, reached only at the excluded left endpoint. For fixed c inside the interval the threshold is strictly larger. The prose should say "largest uniform constant" or display the variable threshold. Read in this uniform sense, it is consistent with A2283; it must not be cited as the fixed-c threshold.

## 6. Other scope repairs and unchanged foundations

The remaining changes agree with their cited verdicts. The summary keeps the no-helicity exception7(g)(i). The dynamical table retains U!=0 for witness statements and the exact annular bound for3(i). The trapping paragraph no longer claims that every structural result uses only sublinearity. Regularity is separated among the C1 nonrotating theorem, C2 transport and smooth coverage. The finite-regularity condition(G) is componentwise and refers to every relevant ergodic measure. The omega=0 theorem is explicitly excepted from the arbitrary-omega discussion.

The far-field bijection concerns divergence-free candidate leading fields, not their nonlinear extension. The rotational defect is (Jy) dot grad U-JU; the smallness threshold depends on the stipulated bounds and retains decay. The axisymmetric-pressure consequence defines the azimuthal component. Angular modes refer to cylindrical vector components. Derivative decay supplies only the derivative premise of Theorem7, which still needs a tail condition.

The C51 logarithmic Holder bound is now explicit on B(y,|y|/4), with exponent s<min(1+sigma,1/c),0<=sigma<=3/2 and a fixed Holder exponent in(0,1). Sigma consistently denotes velocity decay and no longer collides with1-2c. Smallness, growth and misalignment hypotheses remain conditional. The weighted-shell lower bound specifies the C1 bounded Hb class with2/5<c<1. The misalignment average is along segments to a fixed sphere and the Holder seminorm uses B(y,3). No newly derived decay or global nonexistence follows from these clarifications.

A full-block byte comparison, using the exact named 2A,2B,2C,2D and Section3 boundaries, proves all four foundations identical to the approved pin. The block sizes are36588,70148,94353 and81689 bytes. Their hashes are recorded in the team records. The initial loose heading matcher undercovered the foundation boundary and yielded no conclusion; the corrected exact-boundary comparison requires all four blocks and their full sizes. The earlier independent foundation verifications therefore transfer without a new mathematical change.

## 7. Verdict and limits of approval

A2297 REFUTES the surviving blanket summary label. A2298 REFUTES the two unqualified gamma-row implications. A2299 CONFIRMS the corrected gamma statements at the exact compact-orbit and nonvanishing scope. A2300 CONFIRMS the C62 insertion with the uniform-constant interpretation. A2301 CONFIRMS the remaining referee precision repairs. A2302 CONFIRMS the unchanged foundations and the front/main/AppendixA assembly only with the two explicit reporting exceptions above. A2303 leaves a clean blanket approval of this pin, historical blanket recertification and the unrestricted conjecture OPEN.

No computation was necessary for the countertests or scope arguments. Hashing and text comparison are file evidence only. The review does not borrow a conclusion from the coordinator's referee: each changed mathematical inference was compared with the independent proof and its exact conditions. Collaboration continues through the configured model coordinator/theory agents and literature agent; actual provider execution is not independently attested.
