# A localized divergence criterion using the actual compatibility coefficient

Status: the compact-center argument below is complete. The corresponding unlocalized statement in theory version12, Section10.5, has an unresolved endpoint step.

## Exact statement

Let f1 be a nonzero finite real S1 sine polynomial, with largest frequency L and coefficient alpha_L nonzero. Let delta be irrational in (0,1), and let f_n(delta) be its unique pure stationary coefficients. For a prime p and an even integer 4<=a<p, define

\[
 \kappa_{p,a}=[\sin((a-3)\theta)]f_p(a/p).
\]

The coefficient f_p at this rational center is defined before the first genuine stream resonance. Suppose that there are eta>0, a compact interval J contained in (0,1), and infinitely many distinct pairs (p,a) with a/p in J such that

\[
 0<|\delta-a/p|<|\kappa_{p,a}|p^{-(1+\eta)p}.
 \tag{1}
\]

Then

\[
 \limsup_n\|f_n(\delta)\|_{\ell^1}^{1/n}=\infty.
 \tag{2}
\]

The density series has radius zero in both the angular Wiener norm and the uniform angular norm. No algebraicity or nonzero first harmonic is required. Condition (1) itself implies that the selected compatibility coefficients are nonzero.

## Proof

Choose epsilon>0 so that J is contained in [epsilon,1-epsilon]. The uniform disk argument of topic46 uses only this localization and a finite leading profile. With R_p=1/(4p^2), there is a constant C depending only on epsilon and f1 such that

\[
 |\kappa_{p,a}|\le(Cp)^p
 \tag{3}
\]

at every selected center, and

\[
 \left\|f_{p+1}(a/p+h)-\frac{\operatorname{Res}_{p,a}}h\right\|_{\ell^1}
 \le2(Cp)^{p+1},\qquad 0<|h|\le R_p/2.
 \tag{4}
\]

For clarity, each nonresonant stream divisor on the disk differs by less than 1/(4p) from a nonzero integer divided by p. The stream norm is therefore bounded by 4p times the density norm, including the resonant boundary circle at order p. The stationary inverse has norm at most 2/(epsilon(n-1)). Angular bandwidth is at most (L+1)n. The Catalan majorant consequently gives (3) and the boundary bound for f_(p+1). Multiplication by h removes its sole possible simple pole, and Cauchy's estimate gives (4). These estimates require no height bound.

Let gamma0=1-a/p and j=a/2-1. The highest contributing input frequency gives the residue coefficient

\[
 [\sin((L+2j)\theta)]\operatorname{Res}_{p,a}
 =-\frac{\kappa_{p,a}j(L+\gamma_0)\alpha_L}
 {2p^2(c_0-1)},\qquad c_0=(1-a/p)^{-1}.
 \tag{5}
\]

For sufficiently large p, its modulus is at least

\[
 c_*|\kappa_{p,a}|/p,\qquad c_*=\epsilon^2|\alpha_L|/8>0.
 \tag{6}
\]

Indeed, j>=epsilon p/4, L+gamma0>=1, and 1/(c0-1)>=epsilon. Only the top input harmonic contributes to this output frequency in the residue.

Equations (1) and (3) imply

\[
 |h|<C^p p^{-\eta p}\longrightarrow0.
\]

Thus the centers approach delta and |h|<R_p/2 eventually. The order of this reasoning matters: the compact-center bound (3) is available before approach to delta is concluded. Apply (4)-(6) to obtain

\[
 \|f_{p+1}(\delta)\|_{\ell^1}
 \ge c_*p^{(1+\eta)p-1}-2(Cp)^{p+1}.
 \tag{7}
\]

The ratio of the second term to the first is at most

\[
 (2/c_*)C^{p+1}p^{2-\eta p}\longrightarrow0.
\]

The right side of (7) is therefore at least half its first term eventually. Taking its (p+1)-st root proves (2). A real sine amplitude is at most twice the uniform angular norm, so the same root conclusion holds there.

## Exponential compatibility lower bounds

Suppose J contains delta in its interior and there is mu>0 such that

\[
 |\kappa_{p,a}|\ge\mu^p
\]

for all sufficiently large admissible primes with a/p in J. If

\[
 0<|\delta-a/p|<p^{-(1+\eta)p}
\]

holds infinitely often for some eta>0, these centers automatically approach delta and eventually belong to J. Choose 0<eta'<eta. For large p,

\[
 \mu^p p^{-(1+\eta')p}\ge p^{-(1+\eta)p}.
\]

The preceding theorem, with eta', proves zero radius. The exponential lower bound is an additional hypothesis, not a consequence of the finite numerical table.

## Endpoint gap in the unlocalized version

The initial version of Proposition10.5 does not assume a/p in a compact subinterval or a/p approaching delta. Its proof first asserts that the centers approach delta, then invokes (3) with a center-independent C. The existing proof of (3) depends on epsilon, through the stationary inverse. It cannot be invoked before localization has been established.

The compact-center theorem and the exponential-lower-bound consequence above are valid. The fully unlocalized statement remains OPEN until an endpoint-uniform bound or a different argument is supplied. A numerical search for rapidly growing compatibility coefficients at a=4 is only a diagnostic of that missing argument. A finite coefficient cannot refute the infinite statement.

## Dependencies and verification

Dependencies are the independent recurrence, the finite bandwidth bound, the disk and remainder argument in topic46, and the exact residue formula in topic15. The accompanying audit will compute certified logarithms of all122 exact compatibility coefficients already regenerated in topic57, and compare the reported extrema and means. Those finite values do not establish a uniform exponential lower bound.

## Independent extended interval scan at 2026-10-31T07:12:11Z

V167 confirms190 further first-resonance values using an independent512-bit Cartesian Laurent recursion. The projection onto known odd sine parity and linear support is justified by the exact support theorem: the positive coefficient interval is retained, the exact negative coefficient is its opposite, and all other exact coefficients vanish. Each discarded or paired interval is also checked before projection. This avoids carrying artificial interval uncertainty in coefficients known to vanish exactly. All2252025 checks pass, and the exact rational p67 checks are included. Every kappa ball is retained in verification/cartesian_arb_scan_20261031T070106Z/. This finite scan does not establish a uniform asymptotic lower bound.


## Finite prime-denominator evidence

V276certifies all502specifically listed centers of verification/complete_prime_scan/checks.json for f_1=sin(theta). Each p is prime, a is even with4<=a<p, and the first stream resonance is p: divisibility by p is necessary, while n=p satisfies the resonance condition. Its resonant forcing is -(a-2) times the density coefficient at frequencya-3. Independent Cartesian interval recurrences enclose this coefficient in a ball separated from zero at every listed center. The exact dyadic balls, source hashes and arithmetic checks are retained. Thus the ordinary pure series is obstructed at each of these502centers with this fixed leading profile. These finite data supply none of the infinitude or approximation assumptions of the divergence theorem above.
