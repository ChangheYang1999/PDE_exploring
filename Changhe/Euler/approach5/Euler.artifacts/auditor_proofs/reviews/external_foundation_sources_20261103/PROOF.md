# External inputs in the compact dynamical argument

Status: independently CONFIRMED at the source and elementary-identity scopes A2475-A2479; broader conclusions OPEN A2480. This review does not replace the proofs of the report's curve-selection, unstable-density or Euler classification lemmas. It distinguishes a missing primary citation from a false mathematical statement.

## 1. Statements, notation and reading scope

Let M be a compact smooth Riemannian manifold without boundary, f a C2 diffeomorphism, and mu an invariant Borel probability. No ergodicity or absence of zero Lyapunov exponents is assumed unless explicitly added. Write E^u for the sum of the positive Lyapunov subspaces and W^u for the associated immersed unstable manifolds. Conditional measures concern measurable subordinate partitions, with atoms containing intrinsic neighbourhoods in these manifolds. They do not concern the generally nonmeasurable partition into complete leaves.

The source-comparison conclusions are:

1. Ruelle1979 supplies the two-sided nonergodic splitting and local/global invariant-manifold statements used by the report. Ledrappier-Young1985 Part I supplies the specified chart estimates. These are different statements and should have separate citations.
2. Ruelle1978, Ledrappier-Strelcyn1982 and Ledrappier-Young1985 Part I supply the upper entropy bound, the entropy formula for unstable absolutely continuous measures, its converse, and the nonergodic density formula at the compact C2 scope.
3. The exact entropy identities used in the flow averaging step follow from the elementary proofs in Sections 4 and 5. The integral-affinity proof assumes the standard ergodic disintegration theorem on a standard Borel probability space, but not a separate entropy-affinity theorem or an unread book citation.
4. The disintegration input should specify a standard Borel target, or an equivalent countably generated measurable partition modulo null sets.

This review compares the complete seven-section the literature agent inventory against the pinned f773564b assembled report. The report passages containing Lemmas 24 and 28 and the complete external-input inventories 2C.3 and 2D.3 were read in this pass. Prior independent audits control the report's other proofs. Hashes and exact primary copies are in the team records.

The complete five-page Ruelle1978 and seventeen-page Ledrappier-Strelcyn1982 manuscripts were read here. Ruelle1979 was read at its introduction, Theorem 3.1 and proof, Section 3.2, Corollary 3.3, Section 6 including proofs and Remarks 6.4, and Appendix B. Its graph-transform Sections 4 and 5 were not reconstructed in this review. Ledrappier-Young Part I was read at Definitions 1.4.1-1.4.2, Theorem A, all of Section 2, Lemma 3.1.1 with construction, Lemma 4.2.2 with proof and surrounding statements, and Sections 6.1-6.2. The printed formulas on LS82 page206 and LY85I page534 were also checked visually. No whole-paper approval follows from these reading records.

## 2. Splittings, real times and local manifolds

Ruelle1979 Theorem 3.1 assumes an invertible probability-preserving base map and a measurable GL(m,R) cocycle T with both log^+||T|| and log^+||T^-1|| integrable. It supplies a measurable invariant splitting, finite exponents and their two-sided limits. There is no ergodicity assumption. Section 3.2 gives invariance of the subspaces; Corollary 3.3 gives subexponential angle control.

For the derivative of f, compactness bounds Df and Df^-1, hence both integrability assumptions hold. If a vector has components in more than one Lyapunov subspace, the forward logarithmic rate is the largest exponent among its nonzero components. For negative integers n, n^-1 log|Df^n v| tends to the smallest exponent among them. One way to check the latter sign is to apply the forward assertion to f^-1 and then reverse the sign of the logarithmic-rate denominator. The angle estimate prevents exponential cancellation between the components.

Suppose f=Psi_1 for a C2 flow on M. For every real t write t=n+s with n an integer and 0<=s<1. Compactness and the variational equation give K>=1 with

    K^-1 |v| <= |D Psi_s(x)v| <= K|v|,
    x in M, 0<=s<=1.

Thus the logarithms of |D Psi_t(x)v| and |Df^n(x)v| differ by at most log K. Dividing by t proves the same pointwise real-time limit wherever the integer-time limit exists. A probability only invariant under f is sufficient for this pointwise interpolation. No claim that it is flow invariant is needed.

Ruelle1979 Appendix B, in contrast, explicitly starts with a semiflow preserving its probability. Its cocycle theorem therefore has that additional premise. It may be applied to the flow-averaged nu in the report, but cannot simply be applied to a measure known only to be invariant under one time map. The elementary interpolation above avoids that misuse.

Ruelle1979 Theorems 6.1 and 6.3 give local and global stable manifolds for C^(r,theta) maps, r>=1 and 0<theta<=1. For diffeomorphisms, the global objects are images under injective immersions, with the specified tangent spaces. Remark 6.4(b) identifies the full stable manifold by strictly negative exponential approach. Applying these statements to f^-1 gives the unstable manifolds. C2 on a compact manifold supplies C^(1,1) bounds, and neutral directions are permitted.

LY85I Section 2 provides Lyapunov charts with a measurable tempered size l(x). Its Sections 2-5 are explicitly stated first for an ergodic measure; the nonergodic theorem is obtained in Section 6.2. Lemma 4.2.2 bounds the Lipschitz constant of the tangent graph on the specified centre-unstable set by D l(x). It is not a global uniform continuity theorem for E^u. Bounds are uniform only after the chart data and spectral gaps have been controlled on appropriate regular blocks. LS82 Proposition 3.3 gives closed blocks of full-measure union, uniform local sizes and contraction, and continuous local plaques. These are the block restrictions needed in the report. The primary statements do not justify extending the unstable bundle continuously to every point of the invariant compact set.

## 3. Entropy, subordinate partitions and density orientation

Ruelle1978 Theorem 2 concerns every invariant probability for a C1 self-map of a compact smooth manifold. It gives

    h_mu(f) <= integral sum_i lambda_i^+(x) dim E_i(x) dmu(x).

No invertibility, ergodicity or nonzero-exponent premise is imposed. The five-page proof was read: it bounds the number of small partition elements met by an image through the exterior-power derivative, derives the entropy estimate for iterates, and passes to the Lyapunov limit. Its remark that entropy is affine is not a proof of integral affinity.

LS82 Definition 1 specifies absolute continuity relative to unstable leaves by measurable subordinate pieces. Theorem 1.2 supplies the entropy formula and the Pinsker statement under the paper's invariant-manifold and integrability assumptions. Its page206 explicitly says that its singular-set and derivative conditions hold automatically for a smooth compact-manifold diffeomorphism. The proof uses the lower bound, with the upper bound supplied separately. The statement is nonergodic. Sections 2.6 and 3.5 explicitly treat, respectively, the part with no positive exponent and the nonergodic construction.

LS82 Proposition 3.1 constructs an increasing measurable subordinate partition with finite-volume atoms, a generating property and exhaustion of global leaves. Absolute continuity is not an assumption of that construction. Its Proposition 2.6 is the Hopf observation that invariant information is constant along unstable leaves, modulo null sets. The proof compares backward Birkhoff averages of continuous functions at exponentially asymptotic points and then uses density in L2.

LY85I Theorem A at page513 states the equivalence between unstable absolute continuity and the entropy formula for a compact C2 diffeomorphism and an invariant Borel probability. Part I proves the implication from the formula to absolute continuity. It explicitly attributes the reverse implication to Sinai and its precise proof to LS82. This distinction is retained in the report.

For the increasing partition in LY85I Section 6.1, Corollary 6.1.4 gives, on almost every atom,

    rho(y)/rho(x)
      = product_{i>=1} J^u f(f^-i x)/J^u f(f^-i y).

The density is strictly positive and its logarithm is locally Lipschitz along the indicated leaf. Corollary 6.2 extends this conclusion to a nonergodic measure. The numerator and denominator were checked in the rendered page534, since the text extraction drops part of the fraction. These are measurable versions on almost every atom, not a globally bounded density.

The report's Lemma 28 has J^u F=e^a A/(A composed with F). Substitution in the finite product gives exactly

    product_{i=1}^N J^u F(F^-i z)/J^u F(F^-i y)
      = [A(y)/A(z)] [A(F^-N z)/A(F^-N y)].

There is no missing sign or inverted factor. Along backward returns of y to a block where A is bounded below and tangent estimates are uniform, a fixed z on the same sufficiently small unstable plaque approaches y exponentially. Their tangents approach within that common local graph, so continuity of the one-form makes the last quotient tend to one on the return subsequence. The density product has a full limit by the cited theorem; its value therefore is A(y)/A(z). This checks the source-sensitive part of the argument. It does not replace the separate construction of such blocks, plaques and conditional versions in the earlier audit.

## 4. Integer-iterate entropy, with proof

Let T preserve a probability rho, and let p be a positive integer. Then

    h_rho(T^p)=p h_rho(T).

No ergodicity, invertibility or finite-entropy assumption is needed. For a finite measurable partition P write

    P_n=join_{j=0}^{n-1} T^-j P,
    H_rho(P)=-sum_{A in P} rho(A) log rho(A),
    h_rho(T,P)=lim_{n->infinity} H_rho(P_n)/n.

We set 0 log 0=0 and use natural logarithms. Entropy subadditivity and invariance give existence of the limit as the infimum. The Kolmogorov-Sinai entropy is the supremum over finite partitions.

The n-fold join of P under T^p is coarser than P_(pn). Hence

    h_rho(T^p,P)<=p h_rho(T,P)<=p h_rho(T).

Take the supremum in P for one inequality. Conversely let Q=join_{i=0}^{p-1} T^-i P. Its n-fold join under T^p is exactly P_(pn), so

    h_rho(T^p,Q)=p h_rho(T,P).

Taking the supremum over P gives the reverse inequality, also if either side is infinite.

In report Lemma 24, p was selected as a positive integer and g=Psi_p. The averaged measure nu is invariant under Psi_1. The preceding result with T=Psi_1 proves the precise scaling needed there. No theorem for noninteger flow times is needed.

## 5. Integral affinity, with proof from ergodic disintegration

Let (Y,B,rho) be a standard Borel probability space, completed if desired, and let T:Y->Y preserve rho. Assume an ergodic disintegration

    rho=integral rho_z d eta(z)

over a standard Borel parameter space, with measurable conditional kernel rho_z for the invariant sigma-algebra I, and rho_z T-invariant and ergodic for eta-almost every z. Then

    h_rho(T)=integral h_(rho_z)(T) d eta(z).                    (5)

The exact external input here is the existence and conditional-kernel property of this ergodic disintegration. The entropy identity will be proved rather than imported.

First fix a finite partition P. Since the probability algebra is separable, I is countably generated modulo rho-null sets. Choose increasing finite partitions Q_j contained in I whose generated sigma-algebra is I modulo null sets. For completeness, a countable dense family in the measure algebra of I exists because this algebra is a subspace of the separable measure algebra of B. Approximating any invariant set in measure by that family and extracting an almost-everywhere convergent subsequence shows that the family generates I modulo null sets. Its finite joins give Q_j.

Every atom of Q_j is invariant modulo null sets, hence T^-1 Q_j=Q_j modulo null sets. The chain rule and monotonicity of Shannon entropy imply

    H_rho(P_n)-H_rho(Q_j)
       <= H_rho(P_n | Q_j) <= H_rho(P_n).

Dividing by n and letting n tend to infinity gives

    lim_n n^-1 H_rho(P_n | Q_j)=h_rho(T,P).

For each fixed j the conditional block entropies are subadditive: use the chain rule, discard conditioning to bound the two blocks, and use T-invariance of both rho and Q_j for the shifted block. Consequently

    h_rho(T,P)=inf_n n^-1 H_rho(P_n | Q_j).

Conditional probabilities of a fixed finite partition converge under the increasing sigma-algebras generated by Q_j to those conditioned on I. This is the conditional-expectation martingale convergence theorem. The function -t log t is bounded and continuous on [0,1], so dominated convergence gives

    H_rho(P_n | I)=inf_j H_rho(P_n | Q_j).

The two infima can be interchanged. Therefore

    h_rho(T,P)
      =inf_j inf_n n^-1 H_rho(P_n | Q_j)
      =inf_n n^-1 H_rho(P_n | I).                             (6)

The conditional-kernel property of the disintegration gives

    H_rho(P_n | I)=integral H_(rho_z)(P_n) d eta(z).

For almost every z, rho_z is invariant and

    n^-1 H_(rho_z)(P_n)->h_(rho_z)(T,P).

All these quantities lie in [0,log |P|]. Dominated convergence therefore identifies the limit of the integrals. On the other hand, the conditional block entropies given I are subadditive for the same reason as above, so their normalized limit equals the infimum in (6). It follows that

    h_rho(T,P)=integral h_(rho_z)(T,P) d eta(z).               (7)

To pass from one partition to full entropy, choose increasing finite Borel partitions P_k generating B. A standard Borel space has such a countable generator. The same choice can be used for every rho_z. We give the entropy approximation argument to avoid importing a generator theorem. For any finite partition R and any invariant probability sigma, the chain rule gives

    H_sigma(R_n)<=H_sigma((P_k)_n)+n H_sigma(R | P_k).

Indeed condition successively on the joined P_k names, then discard all but the corresponding single-time condition in each term and use invariance. Divide by n to obtain

    h_sigma(T,R)<=h_sigma(T,P_k)+H_sigma(R | P_k).

Since P_k generates the Borel sigma-algebra, conditional-expectation convergence and dominated convergence give H_sigma(R | P_k)->0. Completed-measurable atoms of R may be replaced by Borel representatives modulo sigma-null sets. Thus

    h_sigma(T)=lim_k h_sigma(T,P_k).

The sequence is increasing. It holds for sigma=rho and for every invariant component for which the disintegration is defined. The component entropy at a fixed P_k is measurable: it is the infimum of the measurable functions n^-1 H_(rho_z)((P_k)_n). Applying monotone convergence to (7) with P=P_k proves (5), including the case of infinite entropy.

Report Lemma 24 uses rho_s=(Psi_s)_*mu for 0<=s<=p, where mu is g-ergodic and the maps Psi_s commute with g. Each rho_s is g-invariant and g-ergodic, because Psi_s is an invertible conjugacy. The map s->rho_s is weakly continuous on the compact support, hence Borel. Its pushforward of normalized Lebesgue measure is a probability on the ergodic g-invariant measures with barycentre nu. By uniqueness of the standard ergodic decomposition, this is the decomposition of nu. Repeated values of rho_s do not matter. Identity (5) now gives h_nu(g)=integral h_(rho_s)(g) ds/p. Conjugacy makes the integrand constant. This proves the exact integral-affinity step used there.

This proof still uses familiar conditional expectation, martingale convergence, standard Borel disintegration and uniqueness of ergodic decomposition. It does not assert that these are elementary algebra, nor that their original manuscripts were read. It removes the separate unverified Jacobs/Walters entropy-affinity citation as a necessary proof dependency if the report includes or cites this argument.

## 6. Remaining citation scope and conclusion

The external inventory should cite RU79 Theorem 3.1 for two-sided nonergodic exponents, RU79 Theorems 6.1/6.3 and Remark 6.4(b) for local/global manifolds, and LY85I Section 2 and Lemma 4.2.2 for the local chart and tangent estimates. A narrow chart lemma is not the source of the whole global manifold statement.

Disintegration should be stated over a standard Borel target, or for a countably generated measurable partition modulo null sets. The report's actual Euclidean and compact metric spaces admit that scope. Neither this review nor the sources authorize arbitrary nonmeasurable leaf quotients.

The original Oseledec, Pesin, Fathi-Herman-Yoccoz, Birkhoff, Rohlin, Jacobs, Walters, Abramov, Hartman and Evans-Gariepy texts have not been read here unless separately documented in an earlier audit. The alternative primary statements and the explicit proofs above are the evidence actually checked. No result is declared false merely because its original citation remains unread.

In particular, this review does not prove the curve-to-unstable-conditional conversion in Lemma 20, the compactification construction, or the assembled Euler classification anew. Those require their existing separate audits. It identifies no new contradiction in the source-sensitive steps read here. The decay-only nonexistence conjecture for arbitrary helicity and arbitrary rotation remains OPEN.
