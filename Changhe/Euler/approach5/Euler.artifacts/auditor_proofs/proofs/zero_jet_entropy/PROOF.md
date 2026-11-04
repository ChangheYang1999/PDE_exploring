# Positive entropy on the zero set forces vanishing derivatives

## Statement

Let r>=2 be an integer. Let B be C^r on a neighborhood of a compact invariant set K in R3, with div B=d>0 constant there. Let W be C^(r-1) on that neighborhood and satisfy

[B,W]=-b W, b>0.

Let F=Phi_-1, where Phi is the B-flow, and let mu be an ergodic F-invariant probability supported on K. If h_mu(F)>0 and W=0 mu-almost everywhere, then D^j W=0 mu-almost everywhere for every 0<=j<=r-1.

For a smooth field the measure is therefore supported on points where W is flat. In the Euler application W=Omega=curl U, b=1+c, d=3c. Neither divergence-freeness of W nor the Euler coupling W=curl U is needed for this local theorem.

As a consequence, a nonconstant real-analytic uniformly sublinear Euler profile with 0<c<1/2 has core entropy exactly 1-2c. It has a maximizing flow-ergodic probability which sees nonzero B and Omega and whose backward exponents are {1-2c,0,-(1+c)}. This is a conditional structure theorem, not nonexistence.

## Compact setting and exponents

Cut B off outside a neighborhood of K and extend it by zero to S3. The C^r compactified flow agrees with the original one and its derivatives near K. All measure-theoretic theorems below apply to its C2 time-one diffeomorphism. No divergence identity outside K is used.

The invariant set {B=0} cannot have full measure because F would then have entropy zero. Ergodicity makes B nonzero almost everywhere. The identity DPhi_t B=B composed with Phi_t, boundedness of B on K, and two-sided Oseledets estimates show that B spans a zero-exponent direction: a positive exponent in this vector would contradict forward boundedness, and a negative exponent would contradict backward boundedness. Tempered Oseledets projections prevent cancellation between exponent subspaces.

The three forward exponents sum to d. Positive entropy for F and Ruelle's inequality require a negative forward exponent. Hence the forward spectrum is simple and has the form

lambda_-<0, 0, lambda_+=d-lambda_->0.

Write the three lines as E_-, RB, E_+. The unstable manifold for F is a one-dimensional C1 immersed manifold tangent to E_-.

## The top-derivative identity

Set Sigma_j={D^ell W=0 for 0<=ell<=j}. The transport formula is

W(Phi_t x)=exp(-b t)DPhi_t(x)W(x).

Differentiating and inducting shows that all Sigma_j are invariant. At a point of Sigma_(j-1), every lower-order term in the differentiated identity vanishes, giving

D^j W(Phi_t x)[DPhi_t v_1,...,DPhi_t v_j]
 =exp(-b t)DPhi_t D^j W(x)[v_1,...,v_j].             (1)

The available regularity justifies this for j<=r-1, including the derivatives of DPhi_t on the right.

If the conclusion fails, ergodicity gives a least k>=1 for which mu(Sigma_(k-1))=1 and mu(Sigma_k)=0. Write T=D^k W. It is nonzero almost everywhere. Differentiating D^(k-1)W along an orbit inside Sigma_(k-1) gives

T[B,v_2,...,v_k]=0.                                (2)

At a two-sided regular point, take v in E_+. If w=T[v,...,v] were nonzero, (1) at time -n and boundedness of T would imply

exp(b n)|DPhi_-n w| <= C |DPhi_-n v|^k.

The logarithmic growth of the right side is -k lambda_+. If lambda_w is the smallest forward exponent in w, the left side has growth b-lambda_w. The inequality forces lambda_w>=b+k lambda_+>lambda_+, impossible. Thus T vanishes on k copies of E_+.

By symmetry, (2), and the one-dimensionality of E_+, a nonzero value of T must contain an E_- input. Expanding the other inputs in Cartesian coordinates, some scalar component g of D^(k-1)W has

g=0 on Sigma_(k-1), Dg(v_-)!=0 for some v_- in E_-.

Therefore each such regular point is isolated in the intersection of its local F-unstable curve with Sigma_(k-1). This argument does not assume the zero set itself is a submanifold.

## Entropy contradiction

Choose an increasing measurable partition xi subordinate to unstable manifolds as in Ledrappier-Young Part I, Lemma 3.1.1. Its conditional measures give full mass to the regular subset just described. On each unstable leaf that subset is countable: each point is isolated, and the leaf is second countable. The conditional measures are consequently atomic, with

p(x)=mu_x^xi({x})>0 almost everywhere.

The increasing convention means F^-1 xi refines xi. Put

I(x)=-log mu_x^xi((F^-1 xi)(x))>=0.

Conditional-measure compatibility and invariance give

sum_{j=0}^{n-1} I(F^j x)
 =-log mu_x^xi((F^-n xi)(x)) <= -log p(x).

The entropy is finite for a C1 map of a compact finite-dimensional manifold. Ledrappier-Young Corollary 5.3 identifies the finite integral of I with h_mu(F). Birkhoff's theorem applied to the displayed bound yields integral I=0. This contradicts positive entropy and proves the statement.

## Analytic Euler corollary

By A055 and A065, a nonconstant smooth sublinear profile below one half has a flow-ergodic maximizing probability nu of entropy at least 1-2c. Flow ergodicity makes Omega either zero or nonzero almost everywhere. In the first case, decompose nu into F-ergodic probabilities. Entropy affinity supplies a positive-entropy component supported on Omega=0. Apply the theorem at every finite order and intersect the resulting full-measure sets. There is a point at which all derivatives of Omega vanish.

If U is real analytic, so is Omega. Its Taylor series at that point vanishes, so Omega vanishes on a neighborhood and then on all connected R3. A uniformly sublinear divergence-free curl-free entire U is constant by harmonic Liouville, a contradiction. Thus nu sees Omega nonzero. A037 and A065 give the exact spectrum, entropy 1-2c and unstable absolute continuity. The maximum equals the topological entropy. No physical-basin assertion is needed for this conclusion.

## Actual-source check

F. Ledrappier and L.-S. Young, The metric entropy of diffeomorphisms. Part I, Annals of Mathematics 122 (1985), 509-539, is retained in the team records. The standing hypotheses on page 511 are a compact smooth manifold without boundary and a C2 diffeomorphism. Lemma 3.1.1 on page 519 constructs the required increasing partitions. Proposition 5.1 on page 529 assumes an ergodic Borel probability. Corollary 5.3 on page 532 identifies unstable partition entropy with full entropy. These statements explicitly allow a zero exponent. The source's entropy equality criterion for absolute continuity is not being assumed in the atomicity argument.

This independently verifies LIT19. At finite regularity it gives vanishing only through order r-1. Smooth flat points remain possible, and the proof does not exclude the main smooth rotating-profile class.
