# Diagonal maximality of the finite part N(b), and the two-term asymptotics of C_alpha

Version 1, 2026-10-28T01:37Z. Status: proof complete (lead); audit requested from the verifier.
Two independent derivations of the key moment formula (Lemma 2) are given; a third, numerical, check is in
scripts/qk_hyp.py and scripts/qk_closed.py.

## 0. Setting and the statement

a = 1/2, x = a, y = -a (complex notation). For w in C \ {x, y, 0} put

    G(w) = w / (pi (w^2 - a^2)^2) = (1/(2 pi)) [ (w - a)^(-2) - (w + a)^(-2) ].

For every direction b the increment density of the rotated kernel K_b(z) = cos(2 arg z - 2b)/(2 pi |z|^2) is

    nu_b(w) = K_b(x - w) - K_b(y - w) = Re( e^(2ib) G(w) ) = |G(w)| cos(arg G(w) + 2b).

(Check: on the real axis w = t > a, both sides equal t/(pi (t^2 - a^2)^2); on the imaginary axis both vanish at b = 0.)
Let Omega_rho = C \ (B_rho(x) u B_rho(y)), 0 < rho < 1/4, and

    N(b) = lim_{rho -> 0} [ (1/2) int_{Omega_rho} |nu_b| dA + (2/pi) log rho ].

This is the finite part called V_beta in the verifier's notes and N(b) in notes/c0_theorem.md, where it was shown that
Lambda_0(b) = (log 2 - 1)/pi + N(b) and that

    C_alpha = 2/(pi alpha) + max_b Lambda_0(b) + o(1)   (alpha -> 0+),

a statement the verifier confirmed with an independent proof (general-direction second-term theorem). The verifier also
proved N(pi/4) = 1/2 exactly (diagonal second-term theorem).

**Theorem M.** N is even, pi/2-periodic, and strictly increasing on [0, pi/4]. Explicitly, for every real b,

    N(b) = N(0) + (1/pi) sum_{n>=1} R_n (1 - cos 4nb) / (n (4n^2 - 1)),
    R_n = prod_{k=0}^{n-1} (2n + 1 + 4k)/(2n + 3 + 4k) = Gamma(n/2+3/4) Gamma(3n/2+1/4) / ( Gamma(n/2+1/4) Gamma(3n/2+3/4) ),

and max_b N(b) = N(pi/4) = 1/2. Consequently max_b Lambda_0(b) = 1/2 - (1 - log 2)/pi and

    **C_alpha = 2/(pi alpha) + 1/2 - (1 - log 2)/pi + o(1)   as alpha -> 0+.**

Corollary values: N(0) = 1/3 + (sqrt 3 - 1 + log(2/(2 + sqrt 3)))/pi = 0.36778722444500357...
(closed form from the external consultation; it agrees with the verifier's 50-digit quadrature of V_axis and with the
series above to 1e-15, see scripts/qk_closed.py). The series gives N(pi/4) - N(0) = (4/pi) sum_{n odd} R_n/(2n(4n^2-1)),
numerically 0.13221277555, which matches 1/2 - N(0) = 0.13221277555499642.

## 1. Fourier expansion in the direction (justified)

Let Theta(w) = 2 arg G(w) in T = R/2piZ (defined for w != 0). For n >= 1 let

    M_n(rho) = int_{Omega_rho} |G| e^(i n Theta) dA,   M_n = lim_{rho -> 0} M_n(rho).

**Lemma 1.** (i) M_n(rho) is real (the conjugation w -> conj w preserves Omega_rho and |G| and maps Theta to -Theta).
(ii) There are rho_0 > 0 and C with |M_n(rho) - M_n(rho')| <= C |rho - rho'| for all n >= 1 and 0 < rho, rho' < rho_0.
Hence M_n exists and sup_{n, rho < rho_0} |M_n(rho)| < infinity.

Proof of (ii). Near x write w = x + r e^(i t). Then G(w) = (1/(2pi)) r^(-2) e^(-2it) u(w) with u(w) = 2w/(w + a)^2,
holomorphic near x, u(x) = 1, |u - 1| <= C_1 r. So |G| = |u|/(2 pi r^2) and Theta = -4t + 2 arg u. On the circle of radius
r the map t -> phi(t) = -4t + 2 arg u(x + r e^(it)) has derivative -4 + O(r), hence for r < rho_0 it is a decreasing
diffeomorphism of the circle covering T four times, and

    int_0^{2pi} |u| e^(i n phi(t)) dt = int e^(i n phi) J(phi) dphi,   J = |u| / |phi'(t)| = 1/4 + e(phi),  |e| <= C_2 r,

where the phi-integral runs over a range of length 8 pi. The constant 1/4 integrates to 0 for n >= 1, so the circle
integral is at most 8 pi C_2 r in modulus, uniformly in n. The area element is r dr dt, so the contribution of the
annulus rho < r < rho' to M_n is at most (1/(2pi)) int_rho^rho' r^(-2) * 8 pi C_2 r * r dr = 4 C_2 (rho' - rho).
The same holds near y. The rest of the plane contributes at most int |G| over C \ (B_rho0(x) u B_rho0(y)), which is
finite because G = O(|w|^(-3)) at infinity and G is continuous elsewhere. []

**Lemma 1'.** For every Lipschitz function g on T with mean zero and absolutely summable Fourier coefficients
ghat(k) = (1/2pi) int g e^(-ikx) dx,

    lim_{rho -> 0} int_{Omega_rho} |G| g(Theta) dA = sum_{k != 0} ghat(k) M_|k| .

Proof. For fixed rho the pushforward measure m_rho of |G| 1_{Omega_rho} dA under Theta is finite, so
int g dm_rho = sum_k ghat(k) int e^(ikx) dm_rho = sum_{k != 0} ghat(k) M_|k|(rho) (the k = 0 term vanishes and
M_{-k} = conj M_k = M_k by (i)). Let rho -> 0 by dominated convergence in k, using Lemma 1(ii). []

Apply this to g_b(x) = |cos(x/2 + 2b)| - |cos(x/2)|, which is Lipschitz with mean zero (both terms have mean 2/pi);
(1/2)|nu_b| - (1/2)|nu_0| = (1/2) |G| g_b(Theta), and the log rho terms cancel. Using
|cos s| = 2/pi + (4/pi) sum_{n>=1} (-1)^(n+1) cos(2ns)/(4n^2 - 1) and dropping sine terms (they pair with the real M_n
against an odd function and vanish), one gets

    N(b) - N(0) = (2/pi) sum_{n>=1} (-1)^(n+1) (cos 4nb - 1) M_n / (4n^2 - 1).           (1.1)

## 2. The moments in closed form

**Lemma 2.** M_n = (-1)^n R_n/(2n), with R_n as in Theorem M. In particular M_1 = -3/10, M_2 = 45/308,
M_3 = -385/3978, and n |M_n| = R_n/2 decreases strictly from 3/10 to 1/(2 sqrt 3).

First derivation (Green's formula; this argument came from an external consultation and was checked line by line here).
Substitute z = 4w^2 (two sheets). Then w^2 - a^2 = (z - 1)/4, |G| = 8 |z|^(1/2)/(pi |z - 1|^2),
e^(in Theta) = (z/|z|)^n ((conj z - 1)/(z - 1))^(2n), dA(w) = dA(z)/(16|z|), and

    M_n = (1/pi) PV int_C z^(alpha-1) conj(z)^(beta-1) (1 - z)^(-2n-1) (1 - conj z)^(2n-1) dA(z),
    alpha = 3/4 + n/2,  beta = 3/4 - n/2,

where products z^p conj(z)^q with p - q in Z mean |z|^(2q) z^(p-q), and PV means removal of a disc of radius 4rho
about z = 1 (the image of the two removed discs differs from it by a set whose contribution is O(rho), since the
integrand is O(|z - 1|^(-2))). Let
Q(zeta) = sum_{k=0}^{2n-1} (-1)^k binom(2n-1,k) zeta^(beta+k)/(beta+k) and U(z) = z^(alpha-1) (1 - z)^(-2n-1) Q(conj z).
Every term z^(alpha-1) conj(z)^(beta+k) = |z|^(2(beta+k)) z^(n-1-k) is single valued, and
d U / d conj(z) is the integrand (because Q'(zeta) = zeta^(beta-1) (1 - zeta)^(2n-1)). Also U = O(|z|^(1/2)) at 0 and
U = O(|z|^(-3/2)) at infinity. Green's formula int d_{conj z} U dA = (1/(2i)) oint U dz on the domain
{eps < |z|, |z - 1| > 4rho, |z| < L} and the limits eps -> 0, L -> infinity leave only the clockwise circle about 1.
With z = 1 + h, U = -h^(-2n-1) (1 + h)^(alpha-1) Q(1 + conj h); a term h^(j-2n-1) conj(h)^k survives the angular
integration only if j = 2n + k and then carries the factor (4rho)^(2k). In the limit only k = 0 survives, and the
orientation gives M_n = binom(alpha - 1, 2n) Q(1). Finally Q(1) = sum_k (-1)^k binom(2n-1,k)/(beta+k)
= (2n-1)!/(beta (beta+1) ... (beta+2n-1)) (an identity of rational functions of beta, checked for beta > 0 by
Q(1) = int_0^1 t^(beta-1)(1-t)^(2n-1) dt). Hence

    M_n = (1/(2n)) prod_{j=1}^{2n} (alpha - j) / prod_{k=0}^{2n-1} (beta + k).

Since alpha - j = beta + (n - j), the numerator factors j = 1, ..., n cancel the denominator factors k = n-1, ..., 0.
For j = n + 1 + i and k = n + i (i = 0, ..., n-1) the remaining factors are alpha - j = -(n/2 + 1/4 + i) and
beta + k = n/2 + 3/4 + i, so M_n = ((-1)^n/(2n)) prod_{i=0}^{n-1} (2n + 1 + 4i)/(2n + 3 + 4i) = (-1)^n R_n/(2n). For n = 1: (alpha-1)(alpha-2)/(beta(beta+1)) = (1/4)(-3/4)/((1/4)(5/4)) = -3/5, M_1 = -3/10.

Second derivation (Fourier transform of homogeneous functions). Substituting z = -4s with s = w^2 - a^2 instead,
M_n = (1/pi) (p.v. K * H)(1) with K(z) = |z|^(-2) e^(-4in arg z) and H(u) = |u|^(-1/2) e^(in arg u).
For -2 < mu < 0 and integer m the tempered function r^mu e^(im phi) has Fourier transform
c(mu,m) rho^(-mu-2) e^(im psi), c(mu,m) = 2 pi (-i)^|m| 2^(mu+1) Gamma((|m|+mu+2)/2)/Gamma((|m|-mu)/2), and the
p.v. kernel K has multiplier 2pi (-i)^(4n)/(4n) e^(-4in psi) = (pi/(2n)) e^(-4in psi). The product of multipliers is
the transform of (pi/(2n)) c(-1/2,n)/c(-1/2,-3n) |u|^(-1/2) e^(-3in arg u); evaluation at u = 1 gives
M_n = ((-1)^n/(2n)) Gamma(n/2+3/4) Gamma(3n/2+1/4)/(Gamma(n/2+1/4) Gamma(3n/2+3/4)), the same number
(prod_{k=0}^{n-1} (n/2+1/4+k)/(n/2+3/4+k) equals this Gamma ratio).

Numerical check. scripts/qk_hyp.py evaluates M_n from a third, independent representation (binomial expansion of
the angular integral in the s-plane on the two sides of |s| = 1/4, giving two 3F2(1) series). It agrees with the
closed form to 30 digits for n = 1, ..., 10 (scripts/qk_closed.py). It also agrees (to about 2e-5, the accuracy of
that quadrature) with direct quadrature in scripts/qk_fourier.py.

Substituting Lemma 2 in (1.1) gives the series of Theorem M:

    N(b) - N(0) = (1/pi) sum_{n>=1} R_n (1 - cos 4nb)/(n (4n^2 - 1)).                       (2.1)

## 3. Convexity of the coefficients

**Lemma 3.** The function R(x) = Gamma(x/2+3/4) Gamma(3x/2+1/4)/(Gamma(x/2+1/4) Gamma(3x/2+3/4)), x > 0, is
positive, strictly decreasing and strictly convex, R(x) < 1 for x >= 1, and R(x) -> 1/sqrt 3.

Proof. Let phi(v) = psi(v + 1/2) - psi(v) = int_0^inf e^(-vs) W(s) ds, W(s) = 1/(1 + e^(-s/2)), for v > 0 (from
psi(v+1/2) - psi(v) = int_0^inf (e^(-vs) - e^(-(v+1/2)s))/(1 - e^(-s)) ds). With u = x/2 + 1/4 we have
3x/2 + 1/4 = 3u - 1/2 and log R(x) = log Gamma(u+1/2) - log Gamma(u) - [log Gamma(3u) - log Gamma(3u - 1/2)], so

    (log R)'(x) = (1/2) phi(u) - (3/2) phi(3u - 1/2),   (log R)''(x) = (1/4) phi'(u) - (9/4) phi'(3u - 1/2).

Substituting s -> s/3 in the second integrals,

    (log R)'(x)  = (1/2) int_0^inf e^(-us) [ W(s) - e^(s/6) W(s/3) ] ds,
    (log R)''(x) = (1/4) int_0^inf s e^(-us) [ e^(s/6) W(s/3) - W(s) ] ds,

valid for u > 1/6, i.e. x > -1/6. With Y = e^(s/6) > 1: W(s) = Y^3/(Y^3 + 1) and e^(s/6) W(s/3) = Y^2/(Y + 1), and
Y^2/(Y+1) - Y^3/(Y^3+1) = [Y^2 (Y^3 + 1) - Y^3 (Y + 1)] / ((Y + 1)(Y^3 + 1)) and
Y^2 (Y^3 + 1) - Y^3 (Y + 1) = Y^2 (Y^3 - Y^2 - Y + 1) = Y^2 (Y - 1)^2 (Y + 1) > 0. Hence (log R)' < 0 and
(log R)'' > 0, so R = exp(log R) is strictly decreasing and strictly convex (R'' = R ((log R)'' + ((log R)')^2)).
R(1) = 3/5 < 1, and Stirling gives R(x) -> (1/3)^(1/2). []

(The consultation gave the same conclusion with the equivalent representation
log R(x) = -(1/2) int_0^inf (e^(-xt/2) - e^(-3xt/2))/(t cosh(t/4)) dt.)

**Corollary.** c(x) = R(x)/(4x^2 - 1) is positive, strictly decreasing and strictly convex on [1, infinity), and
c_n = c(n) = O(n^(-2)). (Product of positive, decreasing, convex functions; (1/(4x^2-1))'' = 8(12x^2+1)/(4x^2-1)^3.)

## 4. Monotonicity

Differentiating (2.1) termwise (the differentiated series converges absolutely and uniformly since R_n < 1):

    N'(b) = (4/pi) sum_{n>=1} c_n sin(4nb).

**Lemma 4 (sine series with convex coefficients).** If c_n > 0 decreases to 0 and d_m = c_m - 2c_(m+1) + c_(m+2) >= 0,
then for 0 < theta < pi,

    sum_n c_n sin(n theta) = sum_{m>=1} d_m E_m(theta),   E_m(theta) = [ (m+1) sin theta - sin((m+1) theta) ] / (4 sin^2(theta/2)) >= 0,

and the sum is > 0 if some d_m > 0. Proof: two Abel summations, using sum_{j<=k} sin(j theta) partial sums
D_k = [cos(theta/2) - cos((k+1/2) theta)]/(2 sin(theta/2)), sum_{k<=m} D_k = E_m, the bound |D_k| <= 1/sin(theta/2),
m (c_m - c_(m+1)) -> 0 (convexity), and |sin(k theta)| < k sin theta for k >= 2, 0 < theta < pi. []

With theta = 4b in (0, pi), N'(b) > 0 for 0 < b < pi/4. Evenness and pi/2-periodicity of N are visible in (2.1).
Hence max_b N(b) = N(pi/4) = 1/2 (verifier's diagonal theorem; also directly from (2.1) and the closed form of N(0)).
This proves Theorem M and the two-term asymptotics of C_alpha. []

## 5. Remarks

- The finite-part maximality is strict: the maximizing directions are exactly b = pi/4 mod pi/2, i.e. the functionals
  T_xy f(x) - T_xy f(y) with x - y on a coordinate axis, or T_xx f(x) - T_xx f(y) with x - y on a diagonal.
- An alternative proof of monotonicity: the pushforward density of |G| dA under Theta, after subtracting a constant,
  is the function sum_n M_n cos(n x); by Lemma 3 and Lemma 4 applied to rho^n n|M_n| (0 < rho < 1) its Abel means are
  symmetric decreasing about x = pi, and the Hardy-Littlewood rearrangement inequality on the circle gives
  N(b) <= N(pi/4). The direct derivative argument above is shorter.
- Nothing here addresses D_alpha = ||R_1^2||; its additive constant is still only known to lie in
  [1/2 - (1 - log 2)/pi, 1 - (1 - log 2)/pi].
