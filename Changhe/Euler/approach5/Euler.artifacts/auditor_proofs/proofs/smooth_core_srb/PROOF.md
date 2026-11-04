# Smooth core SRB measure, conditional on the generalized u-Gibbs theorem

## Statement and external premise

Assume Theorems A and B and the ergodic-component property in Claim A.1 of S. Ben Ovadia and D. Burguet, Generalized u-Gibbs measures for C-infinity diffeomorphisms, arXiv:2506.18238v2. Their statements have been checked against the actual manuscript. The campaign has not reconstructed their complete proof. The result below is explicitly conditional on that external premise.

Let B be a complete C-infinity vector field on R3 with div B=d>0 constant. Suppose constants R0,b0>0 satisfy

    B(y).y >= b0 |y|^2 for |y|>=R0.

Let W be a nonzero C-infinity field satisfying [B,W]=-kappa W, with kappa>d. Write Psi_t for the backward B-flow. Then there is a compactly supported full-flow invariant and ergodic probability nu with

    nu(B!=0)=1, spectrum (chi,0,-d-chi), chi>0,
    h_nu(Psi_1)=chi.

Its conditional measures on unstable manifolds are absolutely continuous, and its basin for continuous-time averages has positive three-dimensional Lebesgue measure. Either

1. nu(W!=0)=1, chi=kappa-d, and a positive-volume part of the basin lies in {W!=0}; or
2. nu(W=0)=1, W is flat at every point of supp nu, and {W=0} has positive three-dimensional volume.

There is no assumption div W=0 or W=curl(B-Ay). For a smooth nonconstant uniformly sublinear Euler profile, apply this with d=3c, kappa=1+c and 0<c<1/2, for every finite omega. This does not establish the primary C2 conjecture or any nonexistence conclusion.

## Compactification and derivative growth

Choose R1>R0 and R2>R1. Let rho be smooth, radial, one on the closed R1-ball, positive on the open R2-ball, and zero outside it. The field X=-rho B extends smoothly by zero to S3. Its time-one map F is a smooth diffeomorphism. The closed R1-ball is forward trapping, and the compactified and original flows, with their derivatives, agree there.

Every point in the annulus R1<|y|<R2 enters the R1-ball in finite positive time. Indeed rho has a positive minimum between R1 and the initial radius, and the radial derivative is strictly negative there. Such points do not recur to themselves. Outside the open R2-ball the field is stationary. Recurrence and ergodicity therefore put every positive-entropy ergodic F-invariant probability inside the original maximal invariant core K in the R1-ball. Its full-flow saturation is also contained in K.

The bracket identity gives

    D Psi_t(x) W(x)=exp(-kappa t) W(Psi_t x).

Let M=max_(|y|<=R1)|W(y)|. The open nonzero set of W meets the interior of this ball, because a nonzero point can be transported inward without becoming zero. For each such x, the smallest singular value sigma3 of D Psi_t(x) is at most exp(-kappa t)M/|W(x)|. Its determinant is exp(-dt), so

    sigma1 sigma2 >= exp((kappa-d)t)|W(x)|/M,
    ||D Psi_t(x)|| >= exp((kappa-d)t/2)(|W(x)|/M)^(1/2).

Thus the top upper derivative exponent of F is positive on a positive-volume set. The external Theorem A produces an invariant generalized u-Gibbs probability over one-dimensional disks; Claim A.1 permits an ergodic component mu. A nontrivial disk contained in a Pesin unstable manifold forces a positive exponent. Theorem B makes h_mu(F)>0.

## Spectrum, entropy and full-flow invariance

The preceding localization puts mu on K and excludes mass on {B=0}. The relation D F^n B=B composed with F^n gives exponent zero in the B direction. For example, boundedness gives an upper bound of zero and recurrence to a set |B|>=epsilon gives a subsequence with exponent zero; the Oseledets vector exponent exists. Ruelle's inequalities for F and F inverse require a positive and a negative exponent. In dimension three the spectrum is therefore exactly (chi,0,-d-chi), with chi>0. Theorem B and Ruelle give respectively h_mu(F)>=chi and h_mu(F)<=chi.

Let Theta be the compactified flow and set

    nu=integral_0^1 (Theta_s)_*mu ds.

This is invariant under the whole flow. Each translate is F-ergodic, conjugate to mu and has the same spectrum and entropy. Integral affinity of entropy gives h_nu(F)=chi. A full-flow invariant set is F-invariant and has the same measure under all these translates; its measure is zero or one. Thus nu is full-flow ergodic. Ledrappier-Young Part I, Theorem A, which permits zero exponents and nonergodic time-one measures, gives absolute continuity of unstable conditionals.

## The stable-holonomy step and physicality

Here is an explicit formulation which keeps the neutral flow direction. Let G be the full nu-measure set generic for continuous-time averages. Choose an unstable curve gamma with a positive-length subset E contained in G and a compact regular Pesin block. Restrict to a small neighborhood where B never vanishes and the stable line, unstable line and B direction have angles bounded away from zero. All local stable plaques in this block have a common positive size.

A small flow strip Sigma through gamma is a two-dimensional surface transverse to the stable line. The flow saturation E0 of E for a short interval has positive induced area on Sigma, lies in G, and remains in an enlarged uniform Pesin block. Local strong stable plaques through E0 lie in G, because their orbits approach exponentially and time averages of uniformly continuous functions agree. Fixed flow-time shifts also preserve G.

To see positive ambient volume without assuming a differentiable stable foliation, take a family of nearby, parallel, two-dimensional transverse slices Sigma_s in a local Euclidean chart, with s in a small interval in the stable direction. Shrink E0 to a compact positive-area subset away from the edges. Every stable plaque through it crosses every Sigma_s. Absolute continuity of stable holonomy gives positive induced area to the crossing set on each slice. These sets form a measurable union, since plaques vary continuously on the compact block. Fubini gives positive three-dimensional volume. All these crossings lie in G, proving physicality.

The exact primary source for this step is A. Blumenthal and L.-S. Young, Absolute continuity of stable foliations for mappings of Banach spaces, retained as in the team records. Its Theorem A, Section 4.1, gives two-sided bounded distortion of induced volume between C^(1+Lip) transversals to a compact stack of stable plaques. Lemmas 3.8-3.9 construct the stack and its holonomy. Section 2.2 allows a negative spectral cutoff with E-plus containing both the zero and positive exponents; the theorem does not require every transverse exponent to be positive. In finite dimension its compactness hypothesis H3 is automatic. Apply the theorem to the compactly supported time-one map on R3 and to the two-dimensional flow strip and slices. Smoothness of the field and individual unstable plaques supplies the required C^(1+Lip) transversals. No assertion about physicality for the discrete time-one map is used.

The same flow-physicality conclusion is stated in the actual Crovisier-Wang-Yang-Zhang manuscript arXiv:2305.03910v3, printed page 3. Its Section 2.5 defines regular hyperbolicity as exactly one zero exponent in the flow direction. The present argument separately verifies how that direction is handled.

## The two alternatives

Full-flow ergodicity and invariance of {W=0} give nu(W=0) equal to zero or one. In the first case, transport and recurrence give exponent -kappa along W. This direction is independent of B, whose exponent is zero. The determinant fixes chi=kappa-d. The same smooth W-flow saturation as in A094 yields a positive-volume vortical part of the physical basin; only short local W-flow intervals are needed, so completeness of W is not required.

In the second case, every time-one ergodic component of nu has positive entropy chi and lies in {W=0}. A089 applies at each finite order. Hence W and all its derivatives vanish nu-almost everywhere. Their common zero set S is closed and full-flow invariant, so supp nu is contained in S.

Any point y on a local stable plaque of a regular x in supp nu approaches Psi_t x exponentially. Its distance to supp nu is at most C exp(-ell t), with ell>0. On a common compact trap, Taylor's theorem gives for every N

    |W(Psi_t y)| <= C_N exp(-N ell t).

If L bounds ||DB|| there, the inverse derivative estimate gives

    |W(y)| <= exp((L-kappa)t)|W(Psi_t y)|.

Choosing N ell>L-kappa and letting t tend to infinity proves W(y)=0. Thus the stable and flow saturation used above is contained in {W=0}; its positive ambient volume proves alternative 2. This does not claim that the whole topological basin is irrotational or that the zero set has interior.

## Audit and scope

This checks LIT40 and the earlier generalized_gibbs_flow proposal, including the coordinator's model cross-check in the team records. The deep 2026 generalized-u-Gibbs existence and entropy theorems remain explicit external premises. The flow-strip argument and the flat-zero alternative are independently reconstructed here. No almost-everywhere basin coverage, uniqueness, maximizing property, or vortical support without an additional argument is asserted.

Verdict: A198 CONFIRMED as a conditional implication from the stated external premise.
