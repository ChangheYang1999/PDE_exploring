# Positive unstable densities in the conditional Euler theorem

This is a fresh source and transfer audit of the Ledrappier-Young input used in report Lemmas 11 and 12. The exact retained Part I PDF has SHA256 8f611bce4e328a50c3def42ce78f2d882ed24186e66867b6558c41588829d7a7. The report reference is the approved fc469b9c assembly. The audit confirms the stated source input and its use; it does not claim to reprove the whole Ledrappier-Young theorem.

## 1. Exact source statement

Let M be a compact smooth Riemannian manifold without boundary, f a C2 diffeomorphism of M onto itself, and nu an f-invariant Borel probability. Suppose

    h_nu(f) = integral sum_i max(lambda_i(x),0) dim E_i(x) dnu(x).

Theorem A, numbered (1.5), of Ledrappier-Young Part I implies that nu has absolutely continuous conditional measures on unstable manifolds. Definition 1.4.1 requires a subordinate measurable partition xi to have, at almost every base point x, xi(x) contained in W^u(x) and containing a relatively open neighborhood of x in W^u(x). Definition 1.4.2 expresses absolute continuity for every such partition.

The stronger conclusion needed by the Euler argument is also supplied by the source. Lemma 3.1.1 gives an increasing subordinate partition. For the partition constructed there, Corollary 6.1.4 gives a strictly positive density rho, with

    rho(y)/rho(x) = product_(i>=1) J^u(f^(-i)x)/J^u(f^(-i)y),
    J^u(z) = |Jac(Df(z) restricted to E^u(z))|.

Lemma 6.1.1 bounds this product above and below away from zero on the relevant partition element. Corollary 6.2 explicitly extends Corollary 6.1.4 to the nonergodic case. Neither the absence of zero exponents nor ergodicity of f is a hypothesis of Theorem A or this extension. The source's standing assumptions and definition of regular point explicitly permit a central space.

## 2. Why positivity is the necessary property

Absolute continuity alone would not justify the passage from a full conditional-measure set to a full arclength set: a density could vanish on a positive-length subset. Here rho is strictly positive and finite, and the source gives its positive lower bound on the chosen element. Consequently nu_x and the Riemannian measure on xi(x) have exactly the same null sets. In the one-dimensional unstable case this measure is arclength. Also, if rho>=c_x>0 there and nu_x is a probability, then length(xi(x))<=1/c_x<infinity. No lower bound uniform in x is needed.

Let G be any Borel set with nu(G)=1. Disintegration gives nu_x(G)=1 for almost every x. For such an x with the subordinate-partition properties, choose an embedded arclength-parametrized open arc gamma around x inside xi(x). Then T=gamma^(-1)(G) has full one-dimensional Lebesgue measure in its parameter interval. It is dense there. If G is contained in a closed set S, continuity of gamma implies gamma is entirely contained in S. This proves exactly the full-arclength and support assertions used in report Lemma 12.

## 3. The compact model and its hypotheses

In the Euler application B(y)=(cI-omega J)y+U(y), U is a bounded C2 vector field on R3, 0<c<1/2 and omega is any finite real number. Here J is the fixed skew-symmetric rotation generator. Write M0=sup|U| and let Psi be the flow of -B. The already proved radial estimate is

    B(y).y >= c|y|^2-M0|y|.

It is independent of the rotation rate because (Jy).y=0. Choose R1>2M0/c, let Q be the closed ball of radius R1, and define K=intersection_(t>=0) Psi_t(Q). The radial estimate makes Q forward invariant for Psi, so K is a compact invariant core. Assume that the probability nu in this application is supported in K. Choose a smooth radial cutoff rho_c equal to1 on a larger ball and zero outside a still larger ball. The field -rho_c B is compactly supported on R3 and extends by zero to the one-point compactification S3. Its time-one map f is a C2 diffeomorphism when B is C2. A smooth metric obtained by a cutoff convex combination equals the Euclidean metric near the compact trapped core K.

The flow of rho_c B leaves {|y|>=R1} forward invariant: the radial derivative is nonnegative there and strictly positive on |y|=R1. If y is exponentially backward asymptotic under f to an orbit in K, it cannot have crossed that sphere, since all subsequent backward integer iterates would then remain outside. Thus its full backward orbit remains in the inner ball, where the cutoff flow agrees with the original one, and y belongs to K. Conversely, a point backward asymptotic for Psi has bounded forward B orbit; the lower radial estimate forces this orbit into {|y|<=M0/c}, hence into K. The unstable manifolds of the two maps agree. At nonregular points this is an assertion about asymptotic sets only, not a smooth-manifold claim.

The original invariant probability is supported in K. Along K the maps, their derivatives and the metric agree, so invariance, all Lyapunov exponents and measure entropy transfer unchanged. The stipulated spectrum (a,0,-kappa), with a=1-2c>0 and kappa=1+c, has positive-exponent sum a. The stipulated entropy a is therefore precisely the equality in Section 1. These spectrum and entropy premises are furnished by the separate coverage theorem; the density theorem does not establish them and cannot be used circularly to obtain that coverage.

## 4. Flow ergodicity does not imply time-one ergodicity

The probability in the Euler argument is ergodic under the entire Psi flow. No step may infer that Psi_1 is ergodic. Section 1 applies directly to its possibly nonergodic time-one map.

Two-sided flow genericity can also be obtained without that inference. For a bounded continuous observable q put q1(x)=integral_0^1 q(Psi_s x) ds. The integer-time ergodic theorem for Psi_1 gives convergence almost everywhere of N^(-1) sum_(n=0)^(N-1) q1(Psi_n x), which equals the continuous-time average of q over [0,N]. The limsup of the latter is invariant under every fixed real flow shift, since the two boundary intervals contribute at most 2|s| ||q||_infinity/N. This invariance holds pointwise wherever the limit exists, and that existence set is itself invariant under all shifts. Full-flow ergodicity makes the limit constant; invariance and bounded convergence identify it with integral q dnu. The negative flow gives the other direction. A countable dense set of observables on the compact support supplies simultaneous genericity for all continuous observables there. The report separately handles global basin measurability and tightness outside the support.

Thus a full-measure Borel set of two-sided generic regular points may be inserted into Section 2. The support is compact and closed, so every selected local unstable arc lies entirely in it. The product-box map Gamma_tau Psi_r gamma(s) has independent tangent directions E^s, E^0 and E^u at the base point. Its C1 inverse-function and change-of-variables arguments then convert the full arclength set into the full-volume basin box. These last facts use the previously established complete flows and Oseledets directions, not any stronger source claim about transverse absolute continuity.

## 5. Actual reading coverage and source typography

The source text was freshly read at printed pages 511-513, 519-520 and 533-535. Printed pages 513, 533, 534 and 535 were also rendered and visually inspected. These cover the standing assumptions, the regular-point convention, definitions, Theorem A, the partition statement, density product, its bound and the nonergodic extension. The full proofs of the intermediate entropy estimates and the cited Ledrappier-Strelcyn partition construction were not freshly rechecked. The source theorem is an explicit external dependency.

Two harmless printed details on page 534 should not be mistaken for mathematical premises. The displayed Jensen inequality for log uses concavity, although the prose says convexity. Its later pointer to Lemma 6.2.2 is to the immediately preceding integral identity of Lemma 6.1.2 on page 533. The actual inequality and identity have the correct directions. Neither typo is reproduced as an input of the Euler proof, and neither changes the density corollaries.

## 6. Verdict scope and comparison

This recheck supports A479 and A2926: the source explicitly supplies positive unstable densities in the nonergodic setting, and report Lemma 11(b) uses it with the correct compactness, regularity, spectrum and entropy hypotheses. Lemma 12 needs only that part. The separate formula rho=C ell in Lemma 11(c) is not a dependency of the later basin or sign argument and is not newly certified by the present source reading.

The existing Theory Agent A  in the team records, read in full, is the configured model comparison for the surrounding theorem chain. It expressly did not reread these external sources, so the present primary-source coverage is this auditor's contribution, not attributed to that agent. Actual provider execution is independently unattested. No new model client, agent, mathematical computation or formalization was used. The unrestricted Euler conjecture and automatic C2 coverage remain open; the helicity-sign nonexistence theorem remains conditional on its stated sign premise.
