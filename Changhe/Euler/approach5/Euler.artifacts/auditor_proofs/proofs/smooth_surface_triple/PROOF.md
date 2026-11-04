# A smooth surface triple with a certified trapping disk

Status: CONFIRMED, with the finite interval computation described below. This is a surface dynamical construction, not an Euler profile or a three-dimensional plug.

## Statement and notation

Let T2 = R2/Z2 have its flat metric and normalized area form nu. Put

    q = (1+sqrt(5))/2, K = q^2, ell = K^(-1),
    A = [[2,1],[1,1]], v = (1,-q), eta = q dx1 + dx2,
    a = 1/4, R = 13/50, delta = 1/100000000.

Write D for the open metric disk of radius R about zero and S = T2 minus D. For every 0 < rho <= K^(-7), there is a smooth orientation-preserving torus diffeomorphism f fixing zero, homotopic to A, such that

    f(S) is compactly contained in interior S,
    f*eta = K eta on T2,
    Df v = rho v on a neighborhood of S.

On S, f*nu = K rho nu and i_v nu = eta. The nonempty set Lambda = intersection over n >= 0 of f^n(S) is a locally maximal hyperbolic attracting set, without a transitivity assertion. Its stable multiplier is rho; a continuous complementary invariant frame has multiplier K.

For every 2/5 <= c < 1/2, taking rho = K^(-(1+c)/(1-2c)) and roof time T = log(K)/(1-2c) gives transverse rates -(1+c), 1-2c and volume rate -3c. This last statement concerns the surface tensor laws needed by a suspension, not its global topology or an actual Euler coupling.

## Exact construction

Define the even C7 function

    G(x) = 9/(pi a^2) (1-|x|^2/a^2)^8 for |x| < a,
    G(x) = 0 otherwise.

Its integral is one, by polar integration. Convolve with the normalized even smooth nonnegative kernel proportional to exp(-1/(1-|x|^2/delta^2)) on |x| < delta and zero outside. Denote this kernel by k_delta and the convolution by G_delta. Its support lies strictly inside D.

For k = (k1,k2) != 0, with z = 2 pi a |k|, set

    G_k = 9! J_9(z) (2/z)^9,
    H_k = G_k / (2 pi i (k1-q k2)), H_0 = 0.

The radial Fourier formula follows by expanding J_0 and integrating the beta moments integral_0^1 t^j(1-t)^8 dt = j! 8!/(j+9)!. Thus the function H defined below solves D_v H = G-1. Its coefficients are imaginary and odd, so H is real and odd.

Indeed, with q' = (1-sqrt(5))/2 and n = max(|k1|,|k2|),

    |k1-q k2|^(-1) <= |k1-q' k2| <= q n.

The first inequality follows because the product is the nonzero integer k1^2-k1 k2-k2^2. The integer-order real Bessel integral gives |J_9(z)| <= 1. Consequently

    |H_k| <= C0 n^(-8), C0 = 9! q / [2 pi (pi a)^9].

There are 8n lattice points in shell n. Derivative series through order five converge absolutely, so H is C5 and the Fourier equation holds classically. The zero-mean solution is unique. Let H_delta = H*k_delta; it is smooth and odd, with D_v H_delta = G_delta-1.

The exact map is

    f([x]) = [Ax + (ell-rho) H_delta(x) v].

It uses the full smooth function, not a truncated series. Since Av = ell v and eta A = K eta,

    f*eta = K eta,
    Df v = [rho+(ell-rho)G_delta]v,
    det Df = K[rho+(ell-rho)G_delta] > 0.

The last inequality uses rho > 0 and ell > rho. The map has degree one and is a local diffeomorphism of a compact torus, hence a one-sheeted covering and a global diffeomorphism. Oddness fixes zero. The support property gives the required exact derivatives near S.

## Infinite errors reduced to one finite inequality

Let H_N retain the square of frequencies max|ki| <= N = 64. Define the exact finite sums S0 = sum |H_k| and S1 = sum 2 pi |k| |H_k|. The shell estimate gives

    ||H-H_N||_infinity <= E0 = 8 C0 N^(-6)/6,
    ||grad(H-H_N)||_infinity <= E1 = 8 C0 (2 pi sqrt(2)) N^(-5)/5.

Convolution gives ||H_delta-H||_infinity <= delta(S1+E1). The reference lift F_N(x) = Ax+ell H_N(x)v therefore differs from f by at most

    E = |v| {ell[E0+delta(S1+E1)]
             + K^(-7)[S0+E0+delta(S1+E1)]}.

This bound is uniform over the entire allowed rho interval. On x(theta) = R(cos(theta),sin(theta)), the reference map has angular Lipschitz constant

    L = R[K+ell |v| S1].

Torus distance to zero is 1-Lipschitz. With M = 4096 equally spaced angular samples, and d_min a lower bound on all sampled distances, every boundary image satisfies

    distance_T2(f(x),0)-R >= d_min-R-L pi/M-E.       (1)

The submitted calculation was independently repeated with 128-bit Arb balls, all 4096 samples, and the opposite order of the nested polynomial evaluations. The original calculation used 96 bits and symmetry to reduce to 2048 samples. Our checker has no symmetry reduction.

The local checker encloses every Bessel coefficient, sums upper bounds for S0 and S1, and takes upper bounds for E0, E1, E and L. At a sample it verifies that a proposed neighboring integer and its two neighbors bracket each coordinate ball. It minimizes the three coordinate-distance lower bounds, clamps any negative roundoff lower bound to zero, and combines the two nonnegative lower bounds in Euclidean norm. The midpoint float chooses only the candidate integer; checked interval inequalities justify the choice. Laurent polynomial evaluation uses complex balls. No numerical approximation to the smoothing kernel is needed.

The run completed on 2026-11-02 at 22:19:27 UTC, in 19.9281 seconds on one CPU. It certified

    d_min > 0.3025040726871746194339,
    E < 0.0094275320075440423952,
    L < 15.123069425997005492665,
    right side of (1) > 0.0214772917029605077643 > 0.

Full directed enclosures, every sampled lower bound, exact input parameters, the coefficient artifact and the checker are in the team records. The proof uses the finite interval inequality together with the analytic tail and smoothing estimates; sample positivity alone would not suffice. This is not proof-assistant verification.

## Topology and hyperbolicity

Equation (1) says f(boundary D) avoids closure D. The embedded open disk f(D) contains zero. The connected set closure D avoids its boundary and meets f(D), so it lies entirely in f(D). Thus f^(-1)(closure D) is a compact subset of D. Taking complements gives the strict trapping inclusion for S.

The nonempty nested compact sets f^n(S) have an invariant intersection Lambda in interior S. Choose a constant w with eta(w)=1. On Lambda write Df(x)w=Kw+b(x)v. The uniformly convergent series

    z(x) = sum over j>=1 of rho^(j-1) K^(-j) b(f^(-j)x)

is continuous and solves Kz(fx)=b(x)+rho z(x). Therefore Df(x)(w+z(x)v)=K(w+z(fx)v). The stable and unstable frames are everywhere independent because eta(v)=0 and eta(w+zv)=1. Compactness bounds their norms and inverse frame norms, proving uniform hyperbolicity with the claimed rates. The trapping-neighborhood description also gives local maximality and attraction. No argument here establishes transitivity.

## Dependencies and scope

The construction is the literature agent LIT46, building on the derivative prescription independently checked in A224. Its infinite estimates and topological implication were checked separately from the numerical run. The independent verification manifest pins the submitted proof and both checkers. Existing model agents have been notified for the ongoing cross-model review; a configured model name is not a provider attestation.

This result does not construct a decaying velocity, impose curl U = W for the same carrier, choose a three-dimensional embedding or meridian, or settle the rotating Euler nonexistence question.
