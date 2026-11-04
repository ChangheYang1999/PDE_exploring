# Nonflat vorticity-zero invariant probabilities

Status: CONFIRMED A433 after independent reconstruction and the configured-model coordinator check. This audits LIT90. It gives necessary spectra, not existence or nonexistence of a decaying Euler profile.

## 1. Statement

Let 0<c<1/2 and omega be any real number. On an open subset of R3 let U be C2 and P be C1, with

    div U=0,
    (1-c)U+B.grad U+omega JU+grad P=0,
    B=(cI-omega J)y+U, W=curl U.

Let K be a compact set invariant under the whole B flow, all of whose orbits are defined for every real time. Write Psi_t for the flow of -B. Let mu be a probability on K invariant and ergodic under the whole flow, and assume W=0 and B!=0 mu-almost everywhere. Put

    a=1-2c, kappa=1+c, d=3c, alpha=B cross W.

Every exponent below is an ambient Lyapunov exponent of D Psi_t, counted with multiplicity. Exactly one of the following holds almost everywhere:

1. DW=0. No upper carrier-exponent bound is concluded.
2. The spectrum is (a/2,0,-d-a/2), DW has rank one, and its only nonzero Oseledets block maps the positive-exponent line to the negative-exponent line. In this case D alpha has rank one.
3. The spectrum is (kappa,0,-d-kappa), DW has rank one, and its only nonzero block maps the positive-exponent line to the flow line R B. In this case D alpha=0.

In cases2 and3, (DW)^2=0 and h_mu(Psi_1)=0. The exponents in these two cases are distinct. These are spectra of a derivative cocycle, not eigenvalues of the pointwise matrix -DB. No boundedness, sublinearity or decay of U away from K is assumed, and no measure is assumed physical.

If D alpha is nonzero on a set of positive mu measure, case2 holds, so the top exponent is a/2<2a. If DW!=0 almost everywhere but D alpha vanishes on a positive-measure set, case3 holds. The inequality kappa>2a holds exactly for c>1/5, in particular throughout 2/5<c<1/2, so case3 retains a possible obstruction to the C2 coverage condition. Measures on B=0 and the case DW=0 are not controlled.

## 2. Differentiating the exact Cauchy law

Taking curl of the profile equation gives

    [B,W]=-kappa W.

Let A_t(x)=D Psi_t(x). The exact transport law is

    W(Psi_t x)=exp(kappa t) A_t(x)W(x).             (1)

At a point with W(x)=0, differentiate in the initial point. The term involving D A_t is multiplied by W(x), hence vanishes. With L=DW,

    L(Psi_t x)A_t(x)=exp(kappa t)A_t(x)L(x),
    L(Psi_t x)=exp(kappa t)A_t(x)L(x)A_t(x)^(-1).  (2)

C2 velocity regularity supplies a C2 local flow and C1 W, exactly enough for this calculation. For any finite interval, compactness of K and local flow existence provide a neighborhood on which the derivatives used in (2) are defined. Completeness is assumed only on K, and does not assert complete orbits on the whole surrounding open set.

The zero set of W is invariant by (1). Its rank function rank L is invariant by (2), so full-flow ergodicity makes it constant almost everywhere. Thus either L=0 almost everywhere or L!=0 almost everywhere. Differentiating W(Psi_t x)=0 in t at t=0 also gives

    L(x)B(x)=0.                                   (3)

No division by L, or integration of log|L|, is used.

## 3. Two-sided boundedness forces a Hom-cocycle resonance

The matrices A_t and A_t^(-1), for |t|<=1 and base points in K, are uniformly bounded. The invertible multiplicative ergodic theorem therefore applies to A_t and to the endomorphism cocycle

    C_t T=exp(kappa t)A_t T A_t^(-1).

On a block Hom(E_lambda,E_eta), its exponent is

    kappa+eta-lambda.                              (4)

This is the tensor product of the output tangent cocycle with the inverse dual input cocycle, times exp(kappa t). The minus sign belongs to the input exponent. Authoritative statements checked in the actual Filip manuscript, arXiv1710.10694v1, are Theorem2.2.6 and invertible Variant2.2.10 on printed pages6-7, and the tensor, dual and Hom rules in Section3.1.1 on page13. The PDF is retained in verification. We use its theorem for the possibly nonergodic time-one map by ergodic decomposition; bounded cocycle norms give all integrability premises on every component.

At a two-sided regular point, the Oseledets direct-sum projections are tempered. If a vector in any cocycle has bounded images in both time directions, all its nonzero-exponent components vanish. Indeed a component of exponent rho>0 has norm at least exp((rho-epsilon)n) for large n, while its projection from a bounded total vector has norm at most C exp(epsilon n); choose epsilon<rho/3. A rho<0 component is excluded in the same way at time -n. This argument also applies when several blocks share an exponent, by grouping them. It does not assume a lower bound on the original vector along the orbit.

By (2), C_t L(x)=L(Psi_t x) is bounded for every real t, since L is continuous on compact K. Hence L lies in the zero-exponent Hom subspace. Equivalently,

    L(E_lambda) subset E_(lambda-kappa),           (5)

with zero image when that target exponent is absent. This is the complete resonance condition. It does not say that L commutes with a pointwise strain matrix.

The same bounded-vector argument applied to A_t B(x)=B(Psi_t x) puts the nonzero vector B in the base zero-exponent subspace. The determinant identity

    det A_t=exp(-dt)

gives the sum of the three exponents as -d. The time-one regular set and spectra can be taken invariant under the whole flow: conjugation by A_s and A_s^(-1), for fixed s and points in K, changes long-time logarithmic norms by bounded quantities, and compact unit-time bounds bridge integer and real time. Thus the spectra are whole-flow-invariant measurable functions and are constant by the assumed full-flow ergodicity. No ergodicity of Psi_1 is required.

## 4. Exhausting the three-dimensional possibilities

Assume L!=0 almost everywhere. If the zero exponent had multiplicity two, the remaining exponent would be -d. All differences would have absolute value at most d, while kappa-d=a>0. Equation (5) would force L=0. Three zero exponents are impossible since their sum is -d<0. Thus the zero exponent is simple and E0=R B.

Let the other exponents be lambda,eta, both nonzero, with sum -d. If both were negative, each would lie strictly between -d and0, and no difference could equal kappa>d. This again contradicts (5). Therefore one is positive, say lambda>0, and the other is eta=-d-lambda<0.

Equation (3) kills the source E0 block. Since (5) lowers the exponent by kappa>0, a source E_eta block and every self-block vanish. There remain only two possible blocks:

    E_lambda -> E_eta: lambda-eta=kappa,
    E_lambda -> E0:    lambda=kappa.

The first gives lambda=(kappa-d)/2=a/2. The second gives lambda=kappa. They cannot occur simultaneously because a/2<kappa. In each case the surviving source and target are one-dimensional, and L is nonzero almost everywhere, so its rank is one. It annihilates its own image in either case, proving L^2=0. This proves the two nonflat alternatives without any further dynamical or regularity assumption.

At W=0,

    D alpha(v)=B cross L(v).                       (6)

In case2 the image E_eta is independent of the flow line, so cross product with B is injective on that image and D alpha has rank one. In case3 the image is the flow line, so (6) is zero. Conversely these alternatives, already proved almost everywhere, justify the positive-measure formulations in Section1. No separate claim that the pointwise rank of D alpha is flow invariant is needed.

## 5. Why both nonflat alternatives have zero entropy

The exact dependency A089 is the following theorem: if B is C^r near compact invariant K, div B=d>0, W is C^(r-1), [B,W]=-kappa W with kappa>0, and an ergodic backward time-one probability has positive entropy and W=0 almost everywhere, then D^j W=0 almost everywhere for 0<=j<=r-1. It does not require the probability to be vortical, physical or flow ergodic. At r=2 its conclusion is DW=0. The complete proof in auditor_proofs/proofs/zero_jet_entropy/PROOF.md has been reread for this audit.

For completeness, its r=2 argument is short. Positive time-one entropy excludes a carrier equilibrium measure. The carrier exponents have one positive, one zero and one negative value. On the vorticity zero set, (2) shows that any nonzero derivative must differentiate in the backward unstable direction: a derivative along the stable line alone cannot meet its Cauchy growth. Since L B=0, some scalar component of W has nonzero derivative along that unstable line. At such a point the zero set is isolated on its local one-dimensional unstable curve. Thus the measure's conditional probabilities on unstable leaves are atomic. For an increasing unstable partition xi, the n-step conditional information is at most -log of the mass of its point atom, independent of n. Birkhoff and the Ledrappier-Young unstable entropy identity force entropy zero, a contradiction. The full A089 proof supplies the precise partition and compactification hypotheses.

Decompose the present full-flow mu into Psi_1-ergodic probabilities. Almost every component gives full measure to W=0 and DW!=0 in either nonflat case. A positive-entropy component would contradict A089 at r=2. Entropy is nonnegative, finite here, and affine under ergodic decomposition, so h_mu(Psi_1)=0. To meet compact-manifold hypotheses, cut the field off outside a neighborhood of K and compactify; this changes no orbit or derivative on K. No divergence condition is needed away from K.

## 6. Scope and evidence

For the campaign, this theorem can test a nonstationary ergodic maximizer on the irrotational part of a compact core or component core. It removes the rank-one D alpha case from the dangerous C2 spectrum, but leaves DW=0, carrier equilibria and case3. The known local harmonic carrier circles have W identically zero, hence DW=0, and fall only under case1; their arbitrary exponents do not contradict this theorem.

No occurrence of either nonflat alternative in an entire decaying profile has been constructed. No uniform spectral bound on all zero-vorticity measures follows. All omega enter only through the exact Cauchy identity; the proof makes no small- or large-rotation approximation.

The proof uses no numerical computation, formal build, boundary integral or pressure normalization. The source submission, A089 dependency and actual MET source are pinned in the team records. The coordinator independently checked the tensor orientation, both-time classification, rank conclusions and threshold c>1/5; its entropy check was explicitly conditional on A089. This auditor reread the complete A089 proof and its actual-source interfaces, so that dependency is independently verified here. The review is pinned as in the team records. The existing agent is configured as the primary model; this is not provider attestation.
