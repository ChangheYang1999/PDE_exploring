# Exact real-energy localization and its regular-patch defect

## Operator identity

Let H be a Hilbert space of square-integrable functions with a positive measure. Let C be bounded on H. Let chi_0,...,chi_J be real bounded multiplication operators satisfying sum_j chi_j^2=1 almost everywhere. Then

 C-sum_j chi_j C chi_j=(1/2)sum_j [chi_j,[chi_j,C]].       (1)

In particular, the full quadratic-form localization error is a paired double commutator. It is not necessary to bound the first commutators separately. All terms in (1) are bounded, so this identity holds on H without a domain extension.

For a real first-order transport T=V.grad-1 on its maximal weighted L2 graph domain, assume multiplication by each chi_j preserves that domain, and all V.grad chi_j are bounded. Then

 Re<Tu,u>=sum_j Re<T(chi_j u),chi_j u>.                  (2)

Thus real transport energy has no localization error for a square partition of unity. The assumptions hold, for example, for smooth cutoffs with bounded V.grad chi_j; product differentiation in distributions proves graph-domain preservation.

## Explicit regular-patch Hilbert-Schmidt bound

Use the convolution singular integral M and its principal-value representation from proof 95, with real even off-diagonal kernel |K(Z)|<=C_K |Z|^(-2). Let b be real, supported on a compact set E of area A, with |b|<=B. Let f=exp(q) with bounded real q and Q=osc q. Put D=M_f M_b M M_(f^-1). Assume the cutoffs above are nonnegative and globally Lipschitz and set Lchi^2=sum_j Lip(chi_j)^2. Define the real-energy localization defect

 Hloc=sym(D-sum_j chi_j D chi_j).

Then Hloc is Hilbert-Schmidt with off-diagonal kernel

 (K(X-Y)/2)[b(X)f(X)/f(Y)+b(Y)f(Y)/f(X)]
                         [1-sum_j chi_j(X)chi_j(Y)].      (3)

The point-mass multiplication part of M contributes zero. Define

 Cnear=C_K B exp(Q) Lchi^2/2,
 Cfar=C_K B exp(Q).

For every R>0,

 ||Hloc||_HS^2<=2 pi A(Cnear^2 R^2+Cfar^2/R^2).          (4)

Deletion of |X-Y|<epsilon has Hilbert-Schmidt error at most sqrt(2 pi A) Cnear epsilon, and deletion of |X-Y|>R has error at most sqrt(2 pi A) Cfar/R. On the remaining bounded product set one may apply the finite-rank cell-projection estimate of proof 92, after introducing smooth radial cutoffs and including their actual derivative bounds.

This statement is restricted to a bounded positive regular extension f and a compact coefficient b. It does not claim that the singular global angular weight has such an extension, or that all nonlocal axis-jet and radial-tail pieces are covered. Those remain separate parts of an actual compact-defect split.

## Proof

Expanding [chi,[chi,C]] gives chi^2 C-2chi C chi+C chi^2. Summing and using sum chi^2=1 proves (1). The distributional product rule gives T(chi_j u)=chi_j Tu+(V.grad chi_j)u. Its real energy differs from <Tu,chi_j^2 u> by the integral chi_j(V.grad chi_j)|u|^2. These last terms sum to (1/2)V.grad(sum chi_j^2)|u|^2=0. This proves (2) on the stated domain.

The same square partition gives the exact pointwise identity

 1-sum_j chi_j(X)chi_j(Y)
                 =(1/2)sum_j(chi_j(X)-chi_j(Y))^2.        (5)

Nonnegativity of the chi_j implies their inner product is nonnegative. Their squared norms are1, so the factor in (5) lies in[0,1]. It is also at most Lchi^2 |X-Y|^2/2. Taking the adjoint of D and using the even real kernel gives (3). Its coefficient in square brackets, after division by2, has absolute value at most B exp(Q), and the kernel is supported where X or Y belongs to E. Therefore its modulus is bounded both by Cnear and by Cfar |X-Y|^(-2). The same explicit two-dimensional integrals as in proof 95 yield (4) and the two deletion errors.

The principal-value truncations converge strongly before localization and in Hilbert-Schmidt norm after the paired cancellation, which identifies the kernel with the bounded-operator defect. No assertion about the integrability of an uncut derivative of the kernel is needed.

For signed cutoffs, (1),(2),(5) remain valid, but the factor in (5) can be as large as2. Formula (4) then needs Cfar=2 C_K B exp(Q). The nonnegative hypothesis is therefore material to the displayed constant.

## Verification

The script checks (1) for exact rational noncommuting matrices and verifies (5) on a nontrivial rational square partition. The infinite-dimensional proof is the bounded-operator algebra and explicit kernel argument above. No actual localization constant, finite rank or inverse has been computed.
