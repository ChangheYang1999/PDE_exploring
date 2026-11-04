# Flat periodic witnesses force zero-work connections

Status: A820-A827 and A829-A830 CONFIRMED at the stated scopes. The source's denial of local vortical density at a nonflat endpoint is REFUTED, A828. Exclusion of the connections and the stronger endpoint bounds remain OPEN, A831.

## 1. Exact hypotheses and conclusions

Let 2/5<c<1/2, omega be any real number, a=1-2c, kappa=1+c, A=cI-omega J, and Jx=(-x2,x1,0). Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0, U(x)->0 uniformly as |x|->infinity.       (1)

Write B=Ax+U, Omega=curl U, Vort={Omega!=0}, Xbar=closure(Vort), g=U.B and H=P+|U|^2/2+(Ax).U. Pressure need not be normalized for Sections 1-7: only differences of levels occur. The equation gives P,H,g in C2. The complete carrier flow is Phi; completeness follows from bounded U and linear growth of B.

Assume Gamma is a nonconstant periodic carrier orbit in Xbar, with Omega=DOmega=0, U!=0, g=0 and H=H0 on Gamma. Assume its nonzero velocity covector has the constant rate rho:

    U(Phi_t x)^T D Phi_t(x)=exp(rho t)U(x)^T, x in Gamma,
    rho<=-2a, or rho>=2-c.                               (2)

Call these the lower and upper windows. The precise previously proved local inputs are: the Floquet exponents are 0,rho,3c-rho; the local unstable cylinder is irrotational in both windows, and the local stable cylinder is irrotational in the upper window (A474,A523). The closure trace of the cylinder tangent to the central level lies in {H=H0,g=0} (A764). The global rank identity is dH wedge dg=0 on Xbar (A413). The local origin theorem A478 excludes U(0)=0 with 0 in Xbar. No density of Vort and no derivative bound at infinity is assumed in these sections.

Conclusions. There is no homoclinic carrier orbit to Gamma contained in Xbar. Both Xbar intersect W^u(Gamma) and Xbar intersect W^s(Gamma) contain points outside Gamma. Every orbit of the former in the lower window, or the latter in the upper window, is irrotational, has U!=0 everywhere, and satisfies

    H=H0, g=0, grad H=-aU, grad g=rho U,
    U(Phi_t x)^T D Phi_t(x)=exp(rho t)U(x)^T.             (3)

Every such lower-window orbit either escapes forward to infinity or converges forward to a single irrotational carrier equilibrium q. Every such upper-window orbit converges backward to a single such q. At the endpoint,

    q in Xbar, U(q)=-Aq!=0, H(q)=H0, g(q)=0,
    DB(q)^T U(q)=rho U(q).                               (4)

The invariant plane U(q)^perp has real eigenvalues with sum 3c-rho and signs lambda_-<=0<lambda_+ in the lower window, or lambda_-<0<=lambda_+ in the upper window. Thus there is at least one heteroclinic Gamma-to-equilibrium connection or an escaping orbit in the lower window, and at least one equilibrium-to-Gamma connection in the upper window. Different orbits may have different equilibria; lower-window connections and escaping orbits can coexist. No realizing profile has been constructed.

## 2. Propagation on the vortical closure

On R={dH!=0} define the C1 scalar ell=(grad g.grad H)/|grad H|^2. Rank gives dg=ell dH on Xbar intersect R. Differentiate this equality only on the open set Vort intersect R, obtaining dell wedge dH=0 there. Both sides are continuous, so this identity extends to Xbar intersect R.

Take any carrier orbit in Xbar with g=0 and dH!=0 at one point x. On the maximal time interval I containing zero where dH stays nonzero, the global identity BH=-ag gives

    d_t g=-a ell g, d_t H=-ag.

Uniqueness makes g=0 and H constant. Since dell is proportional to dH, B ell=0 on this interval. Put r=-a ell(x). Differentiating the global identity BH=-ag, as an ambient identity, gives the linear covector equation

    d_t grad H=(rI-DB^T)grad H,
    grad H(Phi_t x)=exp(rt)D Phi_t(x)^(-T)grad H(x).       (5)

At a finite endpoint of I its right side has a nonzero limit: the complete C1 flow has an invertible differential at every finite time. Thus the interval cannot end, and (5) holds for every real t. This proves propagation without assuming nonzero velocity along the whole orbit.

For the lower-window unstable trace, A764 supplies g=0,H=H0 and regularity on a backward tail near Gamma. There ell tends to -rho/a; its constancy therefore fixes r=rho. Irrotationality propagates from the local unstable cylinder by the vorticity Cauchy law. The Lamb identity grad H=B cross Omega-aU yields (3). The upper-window stable trace is identical with the Gamma end at positive time.

If an irrotational zero-g orbit in Xbar had both a zero and a nonzero velocity point, applying (5) at the nonzero point would contradict the zero. Thus either U is everywhere nonzero or identically zero on it. In the latter case it is exp(tA)x. A compact invariant set containing such an orbit must contain x=0 with U(0)=0, which A478 excludes from Xbar.

## 3. No homoclinic orbit, and existence of nontrivial traces

In the lower window, the tangent plane of {H=H0} along Gamma is span(B,e_(3c-rho)); the stable cylinder has tangent plane span(B,e_rho). A chart (theta,s) on the stable cylinder, with Gamma given by s=0, therefore has partial_s H!=0 on Gamma. The implicit function theorem and a finite cover of Gamma show that the stable cylinder meets {H=H0} only in Gamma in a sufficiently small tube. A homoclinic orbit in Xbar would have H=H0 by Section 2 and a forward tail in that intersection. It would meet Gamma and hence equal it by uniqueness, a contradiction. In the upper window reverse stable and unstable and time. This removes the extra U!=0 premise in A765.

For existence, choose tubes Gamma contained in N, closure(N) contained in a compact local hyperbolic tube N0. Choose vortical y_n in N tending to Gamma but outside the local stable cylinder. This is possible because Vort is open and the cylinder has empty interior. Their first forward exit times tau_n from N are finite by the local stable trapping characterization, and tend to infinity by continuous dependence. A subsequence of p_n=Phi_(tau_n)y_n converges to p in boundary(N). For every fixed s>=0, Phi_(-s)p lies in closure(N), since the same is true before each first exit. The local unstable characterization gives p in W^u_loc(Gamma), and p in Xbar. It is outside Gamma. Backward exits from points outside the unstable cylinder prove the stable trace statement. No quantitative inclination lemma is required.

Put M0=sup|U|. The radial bound r'>=cr-M0 shows that an unbounded forward orbit eventually crosses r>2M0/c and thereafter escapes. Every backward orbit obeys

    |Phi_(-t)x|<=exp(-ct)|x|+(M0/c)(1-exp(-ct)), t>=0.    (6)

Hence the opposite end of every upper-window trace is bounded; a bounded lower-window trace has a nonempty compact full invariant omega-limit Lambda.

## 4. The covector law on the compact limit

All equalities in (3), initially allowing U=0, pass to Lambda by continuity and continuous dependence at each fixed time. If U(q)=0 at a point of Lambda, its covector law makes U zero along the entire orbit of q. This orbit is exp(tA)q. Compact full invariance forces q=0, contrary to A478. Thus min_Lambda|U|>0, and Lambda lies in the regular central level.

On the open ambient set R define

    N_H=grad H/|grad H|^2, f=BH=-ag,
    Ytilde=B-f N_H, S={H=H0} intersect R.                (7)

This C1 field is tangent to every nearby H-level. Let Y be its restriction to the C2 surface S. It equals B along the entire trace and on Lambda. Crucially the ambient identities inherited from (3) give

    df=rho dH on Lambda.                                (8)

For a tangent vector v at a point of Lambda, DYtilde v=DB v. This is an ambient differential calculation; it does not differentiate the vanishing of g on a thin set.

If a periodic orbit gamma of period T lay in Lambda, the B return differential would have multipliers 1,exp(rho T),exp((3c-rho)T). The invariant tangent plane ker dH=U^perp has multipliers 1 and exp((3c-rho)T). Equation (8) makes them the surface-flow multipliers too. In the lower window this is a repelling surface cycle. In an annular collar, a periodic positive rescaling of the transverse coordinate puts its equation into v'=(3c-rho)v+o(|v|), uniformly in phase. Both small collar boundaries point outward; every noncycle orbit inside leaves in finite forward time and cannot reenter. Such a cycle cannot belong to the forward limit of the distinct trace orbit. In the upper window apply the same argument to -Y. Thus Lambda contains no periodic carrier orbit.

## 5. Invariant probabilities and the surface equilibrium index

For completeness, the measure classification invoked in B47-B48 does apply. On compact Lambda the time-one derivative and its inverse have bounded logarithms, so the continuous-time multiplicative ergodic theorem applies to every whole-flow-ergodic probability. Use the flow theorem; whole-flow ergodicity does not imply time-one ergodicity. The covector law and min|U|>0 give exponent -rho for DPhi_t^(-T), so rho is a forward exponent. At a recurrent nonstationary regular point, DPhi_t B=B composed with Phi_t gives exponent zero: boundedness bounds it above, and a recurrent subsequence bounds it below. The determinant exp(3ct) supplies the remaining exponent 3c-rho.

The previously proved nonflat irrotational measure alternative A467 has spectrum {-a/2,0,3c+a/2}. It cannot contain rho in either window: in the upper window the gap is (2-c)-(3c+a/2)=3a/2>0. The flat alternative A470-A471 has this same covector and rate rho; comparison at time one fixes its classified rate to rho. Its largest backward exponent max(-rho,rho-3c) is positive, so A471 makes it periodic. Section 4 excludes this. Thus all ergodic probabilities on Lambda are equilibrium atoms; every invariant probability is supported on its equilibrium subset E, and every minimal subset is a single equilibrium. In particular E is nonempty. The exact scopes of A467 and A471 are dependencies, not new assertions for arbitrary surface measures.

At q in E, (4) follows from the covector law. The plane U^perp is invariant and has trace 3c-rho. If in the lower window both eigenvalues had positive real parts, a positive quadratic Lyapunov function for the reversed linear field would make q a repeller of the surface field. Small ellipsoids would be outward pointing, impossible for an external orbit accumulating at q. A complex pair has positive real part because the trace is positive and is therefore also excluded. The eigenvalues must be real with lambda_-<=0<lambda_+. Reverse time for the upper window. A zero eigenvalue is allowed. A flow-direction zero exponent is not asserted at the equilibrium itself.

## 6. The compact limit collapses to a single equilibrium

Use the independently proved surface theorem A657-A658 in its exact general form:

Let X be C1 on a C2 surface, with a positive C1 density nu near K. Let K be the exact omega-limit of an external forward orbit precompact in that surface. If div_nu X>0 on K and every equilibrium in K has real eigenvalues lambda<=0<eta, then K is a singleton equilibrium. No isolation among all surface zeros, finite-equilibrium assumption, genus restriction or invariant-measure premise is part of this theorem.

Its complete standalone proof is the dependency in the team records, Sections 1 and 3-8, reread for this application. To specify what is used: center-manifold coordinates give s'=F(s)+rA, r'=rC with |F'|<b<=C. Uniform invariant graphs through all nearby center zeros, constructed by the cones |s-u|<=L|r|, bound backward-invariant strips. An external orbit cannot enter such strips, so its limit has only extreme center zeros and finitely many equilibria. At a nonisolated zero the accessible side is a zero-free attracting center half-block. Its punctured passage maps have unique inverse limits; thickening on the inaccessible side requires only relative isolation from K and the orbit. Finite disjoint transversals then give return inverses contracting flux distance to K by one uniform factor below one. Positive distances along an external orbit tending to K would consequently increase at every return. This excludes regular limit points; connectedness gives one equilibrium. This is the general surface proof, not the specialized W1 endpoint estimate.

We verify each application premise. Choose bounded nested ambient neighborhoods Lambda subset N1, closure(N1) subset N0, closure(N0) subset R. A sufficiently late trace has closure compact in N0 intersect {H=H0}; this establishes surface precompactness, not only ambient boundedness. The trace is external: membership in Lambda would put its entire orbit and hence its Gamma end in Lambda, contradicting Section 4.

On S orient the positive density by

    nu=(i_(N_H) volume)|S=dS/|grad H|.

Since Ytilde is tangent to all H-levels, [Ytilde,N_H]H=0. Cartan's formula therefore gives div_nu Y=(div Ytilde)|S; the bracket contraction vanishes on pairs of tangent vectors. Directly,

    div Ytilde=3c-N_H f-f div N_H=3c-rho on Lambda.       (9)

Only a positive lower bound holds in a neighborhood, obtained by continuity. The eigenvalue premise is Section 5, and DY=DB on the tangent plane by (8). The theorem now gives Lambda={q}. For the upper window use -Y, with divergence rho-3c>0 and eigenvalues -lambda_+<=0<-lambda_-. This proves all per-orbit convergence assertions in Section 1.

## 7. Nonflat endpoints and the source correction

If DOmega(q)!=0, some partial_j Omega_i stays nonzero in a small box. No nonempty open subset of that box can have Omega identically zero. Thus Vort is dense there. Rank extends throughout a smaller regular H-coordinate box, so g=G(H), G(H0)=0 and G'(H0)=-rho/a. The central level is locally B-invariant. The source statement that this local density is unavailable for a nonflat W2 endpoint is false.

The A469 nonflat equilibrium classification gives two families, with the distinguished covector eigenvalue rho:

    {rho,rho+kappa,-a-2rho},
    {rho,(-a-rho)/2,(1+4c-rho)/2}.                       (10)

In the lower window the latter two level eigenvalues are both positive, impossible by Section 5. In the first family -a-2rho>0, so rho+kappa<=0. Consequently a nonflat lower endpoint has rho<=-kappa and the first family. In the upper window A522 supplies its separately proved first-family and separating-level conclusion. Those results have not been derived from surface dynamics alone.

The W1 lower bound rho>=-2kappa, strict exclusion of a nonflat endpoint at rho=-kappa, and its incoming vorticity power law do not follow here. The W2 trace is irrotational. For the abstract surface theorem alone, X=lambda x partial_x+(d-lambda)y partial_y, with arbitrary lambda<0,d>0, has an external stable orbit tending to its saddle and divergence d; there is no universal lower bound on lambda. This is only a surface countertest, not an Euler profile.

## 8. Escaping traces, with the extra derivative hypothesis separated

On any escaping trace, bounded U gives |Phi_t z| comparable to exp(ct), and (3) gives exactly

    d_t log|U(Phi_t z)|=rho-c-n.(sym DU)n, n=U/|U|.      (11)

Bare uniform velocity decay does not bound the integral of the last term. If DU(Phi_t z)->0, its time average tends to zero and (1/t)log|U(Phi_t z)| tends to rho-c. A positive asymptotic multiplicative constant requires convergence of that strain integral.

For the stronger global natural bounds, with p=(1-c)/c,

    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1),                          (12)

the strain is integrable along the escaping orbit and |U| is comparable to exp((rho-c)t). The verified pressure lemma A674 gives |grad P|<=C r^(-2p-1); its proof uses the actual momentum normalization to remove the entire harmonic gradient, and the zero zeroth and first moments of tr((DU)^2). There is no free pressure normalization at this step.

On the irrotational trace, (3) and momentum give grad P=DU U-(a+rho)U. Divide its normal component by |U|. Unless rho=-a, comparison with the pressure rate forces rho<=c(1-(2p+1))=-2(1-c). Thus every lower-window escaping trace under (12) has rho<=-2(1-c). The actual H limit exists, and its constant trace level is H0=Hinf.

There is a further distinction from the W1 vortex-line case. This entire trace is irrotational. Under (12), the actual C1 scattering diffeomorphism Xi obeys Xi_*Omega=W. Therefore W vanishes on its scattering ray. Also rho<-a makes its velocity decay faster than the natural rate, so the actual tail V vanishes on that ray. Both actual tail fields vanish there. The W1 conclusion of nonzero radial tail vorticity must not be imported to this W2 orbit.

## 9. Verification record and remaining scope

The repaired B source through Section 3e, the full w2chain answer, the full w2collapse proof and the indicated older independent proofs were read. The collapse review agrees with the correction of nonflat density and with the explicit surface-precompactness premise. Its attempted model request failed at credentials and is not a successful model review. Continuing collaboration uses the existing configured model coordinator/theory agents; provider runtime is not independently attested. The complete new proof was postread before ledger promotion.

The source's earlier claim of an unconditional velocity exponent is retained only in the conditional form (11). The abstract collapse theorem has no additional Euler premise, but its supplied regular level, rate, externality and spectral hypotheses are all checked above. The proof does not exclude the resulting heteroclinic connections, force one common endpoint, or remove global zero helicity. General smooth decaying rotating-profile nonexistence remains OPEN. No numerical computation or formal build was used.
