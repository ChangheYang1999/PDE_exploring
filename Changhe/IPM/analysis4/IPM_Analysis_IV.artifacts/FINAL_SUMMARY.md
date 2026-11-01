# FINAL SUMMARY: convergence of the stationary far-field series for self-similar IPM

Final version (run start 2026-10-31T01:57:42Z; research stopped 2026-11-01T00:38Z). Labels: PROVED (complete proof written and confirmed by the
independent verification), NUMERICAL EVIDENCE, CONJECTURAL, OBSTRUCTED, OPEN. Section and theorem numbers refer to the theory part of the report.

Notation: $c=c_l>1$, $\delta=1-1/c$, $\gamma=1/c$, $z=r^{-\delta}$, $r^{-\gamma}\rho=\sum_{n\ge1}z^{n-1}f_n(\theta)$,
$\alpha=\delta/2$, $\mathcal B(\alpha)=\sum_k\log(q_{k+1})/q_k$ the Brjuno sum of $\alpha$ ($q_k$ the continued
fraction denominators), $d_n=\operatorname{dist}(n\delta,2\mathbb Z)$. A rational $\delta$ is written $2h/Q$ with coprime
positive integers $h,Q$ (so $h/Q=\delta/2$ in lowest terms); its stream resonances sit at the orders $n$ with
$n\delta\in2\mathbb Z$, $n\delta\ge4$. The responses $\sigma_k$ of the tuned series are indexed by $k\ge2$ if $h=1$ and by
$k\ge1$ if $h\ge2$; "$\inf_k|\sigma_k|$" always refers to that range.

## 0. Answers in brief

1. Yes. PROVED. For every $c$ with $\delta/2$ a Brjuno number (almost every $c$) and every nonzero analytic
   odd-harmonic $f_1$ the series converges with all derivatives on an explicit exterior (Theorems A, A'); for example
   $c=(5+\sqrt5)/4$, $f_1=\sin\theta$, $r\ge2^{26}$. At every rational $\delta$ the uniquely tuned pure series converges
   for every nonzero finite real odd sine polynomial $f_1$ that satisfies one exact compatibility condition and whose
   responses are bounded away from zero (Theorems T, T_Q, T_{Q,h}, a conditional statement); profiles satisfying both
   hypotheses are known explicitly only at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2,7/3,5,13/7$, where 87 are certified, all with explicit
   radii: 76 two-mode profiles $\sin\theta+b\sin3\theta$, seven keeping all eight higher harmonics of Candidate 007, and
   the single harmonics $\sin11\theta$, $\sin9\theta$, $\sin7\theta$, $\sin17\theta$ at $\delta=4/9,4/7,4/5,6/13$, which have no
   $\sin\theta$ term and carry open families of convergent lattice profiles $\sum_{j\in J}a_j\sin(jM\theta)$ ($J$ any fixed finite set of positive odd integers containing 1).
2. Domain and norm: an exterior $r>R_0$ with explicit $R_0$; absolute convergence, uniform on every closed exterior
   $r\ge R>R_0$, with all weighted Cartesian derivatives, in an analytic Wiener norm in $\theta$ (PROVED). For the 87
   certified rational profiles the proved radii are $2^{16}$ to $2^{42}$ times $|\varepsilon|^{1/\delta}$
   for the 32 two-mode profiles at $\delta=2/3,1/2,2/5,1/3,4/9,3/5,4/7$, $2^{47}$ to $2^{109/2}$ times $|\varepsilon|^{7/2}$
   for the ten at $\delta=2/7$, $2^{113/2}$ to $2^{65}$ times $|\varepsilon|^4$ for the ten at $\delta=1/4$, $2^{127/2}$ to $2^{72}$ times
   $|\varepsilon|^{9/2}$ for the ten at $\delta=2/9$, $2^{147/2}$ to $2^{87}$ times $|\varepsilon|^5$ for the fourteen at $\delta=1/5$, $2^{161/4}$ to
   $2^{175/4}$ times $|\varepsilon|^{9/4}$ for the seven Candidate-shaped ones, and $2^{20}|\varepsilon|^{5/4}$, $2^{147/4}|\varepsilon|^{7/4}$,
   $2^{213/4}|\varepsilon|^{9/4}$, $2^{160/3}|\varepsilon|^{13/6}$ for $\sin7\theta$, $\sin9\theta$, $\sin11\theta$, $\sin17\theta$.
   The proved lower bounds for the required exterior radius (from the top Fourier mode) are at most
   $1.15|\varepsilon|^{1/\delta}$ for the 25 two-mode profiles at $\delta=2/3,1/2,2/5,1/3,4/9$, $0.0016$ to $0.062$ times
   $|\varepsilon|^{5/3}$ at the four roots at $\delta=3/5$, $6.0\cdot10^{-10}|\varepsilon|^{9/4}$ for the Candidate-shaped profiles and
   $0.0127$ to $0.880$ times $|\varepsilon|^{7/4}$ at the three two-mode roots at $\delta=4/7$, and $0.507|\varepsilon|^{9/4}$,
   $0.236|\varepsilon|^{7/4}$, $0.0902|\varepsilon|^{5/4}$, $0.495|\varepsilon|^{13/6}$ for $\sin11\theta$, $\sin9\theta$, $\sin7\theta$,
   $\sin17\theta$, and $5.74\cdot10^{-7}$ to $0.344$ times $|\varepsilon|^{7/2}$ at the ten roots at $\delta=2/7$ and $5.25\cdot10^{-7}$
   to $0.721$ times $|\varepsilon|^4$ at the ten at $\delta=1/4$, $3.63\cdot10^{-6}$ to $1.51$ times $|\varepsilon|^{9/2}$ at the ten at $\delta=2/9$ and $3.33\cdot10^{-12}$ to $3.23$ times $|\varepsilon|^5$ at the fourteen at $\delta=1/5$ (PROVED; lower bounds only), and the computed two-mode series suggest true radii between
   about $0.05$ and $3\cdot10^7$ times $|\varepsilon|^{1/\delta}$ (finite fits; the largest, $2.2\cdot10^7$ to $3.5\cdot10^7$ at order 300 and $2.2\cdot10^7$ to $2.5\cdot10^7$ at order 600, at the first root at $\delta=1/5$; NUMERICAL EVIDENCE). Explicit bounds for the remainder after any order and for the
   stationary residual of any truncation, with all derivatives, are PROVED.
3. Yes, on that exterior: the sums are real-analytic, solve the stationary equations exactly, have a convergent
   velocity potential and a single-valued pressure, and are nonterminating: no finite truncation is an exact solution
   (PROVED). A global solution is OPEN.
4. Candidate 007's profile: convergent at every Brjuno $\delta$, including one within $2\cdot10^{-32}$ of the stored value
   (PROVED); at the stored rational value the series is controlled below its first resonance at order
   $8152952920478362$ (PROVED), and the compatibility condition there is OPEN (out of computational reach). At $c=9/5$
   its own profile is obstructed (PROVED); changing only its $\sin3\theta$ coefficient to any of the seven compatible
   values gives a convergent tuned series at Candidate 007's amplitude on $r>2^{50}$ to $2^{54}$ (PROVED for all seven).
5. Varying $c$: convergence on the full-measure Brjuno set, with constants depending on $c$ through $\mathcal B(\delta/2)$
   (PROVED); divergence (radius zero) on a dense $G_\delta$ set of $c$ for every finite real profile with a $\sin\theta$
   term (PROVED); at rational $c$ the pure series of $\sin\theta$ is obstructed (PROVED at $\delta=a/p$, $p\ge5$ prime,
   $4\le a<p$ even, and at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2$; finite exact computation at further rationals; OPEN at a general
   rational), and the tuned series converges for compatible finite profiles with responses bounded away from zero
   (PROVED).
6. Exact resonances obstruct the pure series of incompatible profiles (OBSTRUCTED; PROVED for $\sin\theta$ at
   $\delta=a/p$, $p\ge5$ prime, $4\le a<p$ even, and at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2$; finite exact computation in further cases)
   but not convergence as such. Small divisors are harmless under the Brjuno condition (a sufficient condition; its
   necessity is not shown), and for every finite real profile with a $\sin\theta$ term the series has radius zero on a
   dense $G_\delta$ set of non-Brjuno $c$ (PROVED).
7. Typically convergent in measure, typically divergent in the Baire sense (both PROVED; the Baire statement for every
   finite real profile with a $\sin\theta$ term and for generic analytic profiles). The canonical logarithmic
   series at rational $c$ is undecided (OPEN); for a nonzero finite real odd sine polynomial $f_1$ only two alternatives
   are possible (PROVED).
8. Strongest theorems: Theorem A/A' (Brjuno convergence with explicit radius, all derivatives and the potential) and
   its rational counterpart Theorem T_{Q,h} (convergent tuned pure series at every rational $\delta\in(0,1)$ under the
   compatibility and response hypotheses), with Theorem S (exact exterior solutions with any truncation as asymptotic
   expansion, at every $c>1$).
9. Main open step: a geometric bound on the realized stream (equivalently density) sums of the canonical logarithmic
   series at rational $\delta$ for a nonzero finite real odd sine polynomial profile; this is equivalent to its convergence. Also open: the first compatibility condition at
   Candidate 007's stored value, the necessity of the Brjuno condition, and a global solution.

## Main results and their status

| Result | Statement in short | Status |
|---|---|---|
| Theorem A, A' | Brjuno $\delta/2$, analytic odd-harmonic sine series $f_1\ne0$: convergence with all derivatives on $r>A^{1/\delta}$, explicit $A$ | PROVED |
| Theorem D, Section 7.5 | $\sin\theta$ at $\delta=1/\sqrt5$: $r\ge2^{26}$; Candidate 007's profile there: $r\ge2^{42}$; $\sin\theta$ at $c=2N+\sqrt5$, $N\in\mathbb Z$, $N\ge16$: $r\ge128$ | PROVED |
| Theorem B | analytic dependence on $f_1$; uniformity on Brjuno sublevel sets | PROVED |
| Top-mode bound (8.2, 14.22) | explicit upper bound for the radius; sharp asymptotics of the top Fourier mode | PROVED |
| Exact solution, potential (Section 7, 12.3) | sums solve the equations exactly; nonterminating | PROVED |
| Theorem S | for every $c>1$ and $C^\infty$ odd-harmonic (S1) $f_1$, each truncation is the expansion of an exact exterior solution | PROVED |
| Theorems M, M' | Brjuno $\delta/2$: convergent double series with geometrically bounded prescribed exterior multipoles ($\sum_kk\lvert h_k\rvert Y_0^k<\infty$ for some $Y_0>0$) | PROVED |
| Theorem E | rational $\delta$ (Candidate 007's stored value): geometric bound for $n<Q$; this covers every order below the first stream resonance of Candidate 007's stored parameter (compatibility there OPEN) | PROVED |
| Resonance compatibility | pure series at rational $\delta$ needs the first compatibility coefficient to vanish | OBSTRUCTED for $\sin\theta$ at the parameters of Theorem P and at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2$ (PROVED); further cases by finite computation |
| Theorems P, P' | $\delta=a/p$, $p\ge5$ prime, $4\le a<p$ even: $\kappa(\sin\theta)\equiv(-1)^{(a-4)/2}\pmod p$; every finite profile with a $\sin\theta$ term incompatible for all but finitely many $p$ | PROVED |
| Theorems C*, Q, Corollary C*.1, Section 10.6 | for every finite real odd sine polynomial $f_1$ with nonzero $\sin\theta$ coefficient: radius zero on a dense $G_\delta$ set of irrational $\delta$ (Theorem C*), and the growth constant is discontinuous at every Brjuno point (Corollary C*.1); explicit divergent Liouville parameters for profiles with coefficients in a number field and $\alpha_1\alpha_L\ne0$, under the approximation condition of Theorem Q; whenever the coefficients are not geometrically bounded (in particular at all these divergent parameters), the terms are unbounded at every radius along almost every ray (Section 10.6) | PROVED |
| Theorems T, T_Q, T_{Q,h} | every rational $\delta$, finite real odd sine polynomial $f_1$: tuned pure series converges if $O(f_1)=0$ and $\inf_k\lvert\sigma_k\rvert>0$ | PROVED |
| Corollaries T.3 to T.10, T_4, T_5, T_6, T_7, T_8, T_9, T_10, T_{9,2}, T_{9,2}.C, T_{10,3}, T_{7,2}, T_{Q,h}.9 | 87 explicit certified profiles (76 two-mode, 7 Candidate-shaped, 4 single harmonics with no $\sin\theta$ term), all with explicit radii; nearby families within the stated fixed-exponent compatibility or lattice spaces | PROVED |
| Proposition T_{Q,h}.8 | $\delta=2h/Q$ reduced with $h\ge2$, $Q$ odd: the first obstruction is an odd form of degree $Q$, so every two-dimensional linear space of finite odd sine polynomials contains a nonzero compatible profile | PROVED |
| Corollary T_{Q,h}.9 | $Q$ odd, $h\ge2$, $M=Q+2h-2$: for every fixed finite set $J$ of positive odd integers containing 1, every lattice profile $\sum_{j\in J}a_j\sin(jM\theta)$ is compatible at the first resonance; around a center with $\inf_k\lvert\sigma_k\rvert>0$ the lattice profiles in a fixed finite space form an open family of convergent tuned series; centers $\sin11\theta$, $\sin9\theta$, $\sin7\theta$, $\sin17\theta$ at $\delta=4/9,4/7,4/5,6/13$ certified | PROVED |
| Theorems T.8, T_Q.5, T_{Q,h}.5 | response condition generic on regular components of the normalized compatibility hypersurface of the finite-dimensional profile spaces ($\delta=2/Q$, $3\le Q\le10$, and $\delta=4/9$) | PROVED |
| Propositions T_{Q,h}.6, T_{9,2}.7 | first compatibility does not imply the response hypothesis: a support gap forces zero responses; a generic order-18 obstruction on two frequency lattices at $\delta=4/9$ | PROVED |
| Corollary T_{10,3}(c) | for positive amplitude the four $\delta=3/5$ solutions are positive in the upper half-plane on an exterior; on the first quadrant the density increases with the angle at the two smaller roots and has exactly one interior angular maximum at the two larger ones (by reflection, two maxima in the upper half-plane) | PROVED |
| Proposition 3.4 | near $\delta=2/5$ the resonant stream coefficients of $\sin\theta$ at orders 10, 15, 20 have poles of orders 1, 2, 3 in $\delta-2/5$ | PROVED |
| Proposition 3.5 | near $\delta=2/Q$, $Q\ge3$, for a finite odd sine profile: the coefficients of $g_n$ and $f_n$ have poles in $\varepsilon=\delta-2/Q$ of order at most $\max(0,\lfloor n/Q\rfloor-1)$ and $\max(0,\lfloor(n-1)/Q\rfloor-1)$, and the resonant stream coefficient at order $kQ$ has an explicit leading coefficient; for $\sin\theta$ near $2/5$ its pole at order $5k$ has order exactly $k-1$ for every $k\ge2$ | PROVED |
| Proposition 14.23 | the shifted three-order multiplier and residual determine the norm growth exactly (geometric, or factorial and divergent); conditional, its hypotheses are not established for the computed sequence | PROVED |
| Proposition 14.24 | along a residue class modulo $Q$, a multiplier with $\log_{10}\lvert a_n\rvert/n\to\beta$ and residual ratios $e_n\le E<1$ gives $\log_{10}\lVert x_n\rVert/n^2\to\beta/(2Q)$; a positive lower rate forces radius zero with no bound on $e_n$; conditional, its hypothesis is not established | PROVED |
| Remarks 3 to 7 of Section 12.6 | necessary radii; sharper majorants; certified prefixes; explicit remainder and residual bounds | PROVED |
| Section 14 | logarithmic series: formal existence, log-degree and Gevrey bounds; equivalent convergence criteria; dichotomy | PROVED |
| Canonical logarithmic series at rational $\delta$ | convergence | OPEN |
| Compatibility at Candidate 007's stored $\delta$ | first condition at order $8.2\cdot10^{15}$ | OPEN |
| Growth constants, true radii | finite-order fits | NUMERICAL EVIDENCE |
| $\lvert\kappa_{p,a}\rvert\ge\mu^p$ | would sharpen the divergence threshold | CONJECTURAL |

## Certified radii at rational $\delta$

Every row is PROVED: the uniquely tuned pure series with leading profile $\varepsilon f_1$ converges, with all weighted
derivatives and a convergent potential, on $r>2^e|\varepsilon|^{1/\delta}$. Single-harmonic rows use $f_1=\sin M\theta$ with
$M=Q+2h-2$ at $\delta=2h/Q$. Two-mode rows use
$f_1=\sin\theta+b\sin3\theta$, with $b$ running through the real roots of the exact compatibility polynomial in
increasing order; Candidate-shaped rows keep Candidate 007's eight normalized higher harmonics and replace only the
$\sin3\theta$ coefficient by a root. The exponents come from the resonance-block majorant started from a certified
finite prefix (Section 12.6, Remark 5; at $\delta=2/7$ and $1/4$ the prefixes run through order $8Q$, and at the third roots through orders 140 and 96
with tail-only response bounds, Corollaries T_7(b) and T_8(b); at $\delta=2/9$ through orders 36 to 72, Corollary T_9(b); at $\delta=1/5$ through orders 40 to 80, and at the fifth root through order 120 with a tail-only response bound, Corollary T_10(b)); they are sufficient radii, not estimates of the true radii.

| Family | $\delta$ ($c$) | exponents $e$, roots in increasing order | restored exponent at Candidate 007's amplitude |
|---|---|---|---|
| two-mode | $2/3$ ($3$) | $35/2,\ 16$ | |
| two-mode | $1/2$ ($2$) | $41/2,\ 23,\ 24,\ 24,\ 23,\ 47/2$ | |
| two-mode | $2/5$ ($5/3$) | $59/2,\ 71/2,\ 65/2,\ 65/2,\ 65/2,\ 63/2$ | |
| two-mode | $1/3$ ($3/2$) | $38,\ 42,\ 42,\ 83/2,\ 40,\ 79/2$ | |
| two-mode | $4/9$ ($9/5$) | $129/4,\ 125/4,\ 32,\ 121/4,\ 117/4$ | |
| two-mode | $3/5$ ($5/2$) | $133/6,\ 137/6,\ 65/3,\ 125/6$ | |
| two-mode | $4/7$ ($7/3$) | $27,\ 117/4,\ 109/4$ | |
| two-mode | $2/7$ ($7/5$) | $47,\ 50,\ 109/2,\ 54,\ 53,\ 53,\ 105/2,\ 103/2,\ 54,\ 49$ | |
| two-mode | $1/4$ ($4/3$) | $113/2,\ 119/2,\ 65,\ 63,\ 63,\ 125/2,\ 62,\ 62,\ 60,\ 115/2$ | |
| two-mode | $2/9$ ($9/7$) | $127/2,\ 135/2,\ 72,\ 72,\ 143/2,\ 71,\ 71,\ 139/2,\ 70,\ 65$ | |
| two-mode | $1/5$ ($5/4$) | $147/2,\ 76,\ 80,\ 165/2,\ 87,\ 167/2,\ 83,\ 165/2,\ 82,\ 163/2,\ 81,\ 159/2,\ 77,\ 149/2$ | |
| single harmonic $\sin11\theta$ | $4/9$ ($9/5$) | $213/4$ | |
| single harmonic $\sin9\theta$ | $4/7$ ($7/3$) | $147/4$ | |
| single harmonic $\sin7\theta$ | $4/5$ ($5$) | $20$ | |
| single harmonic $\sin17\theta$ | $6/13$ ($13/7$) | $160/3$ | |
| Candidate-shaped | $4/9$ ($9/5$) | $161/4,\ 83/2,\ 87/2,\ 171/4,\ 171/4,\ 83/2,\ 175/4$ | $50,\ 51,\ 53,\ 53,\ 53,\ 51,\ 54$ |

The restored column uses $a_1^{9/4}<2^{9.49}$ for Candidate 007's $\sin\theta$ coefficient $a_1\approx18.568$. The raw
$\sin3\theta$ coefficients of the seven Candidate-shaped profiles at that amplitude are about
$-2.834,\ 0.780,\ 1.660,\ 3.232,\ 5.444,\ 8.680,\ 44.09$ (Candidate 007's own value is $2.107$); their certified
response bounds are $2^{-14},2^{-21},2^{-28},2^{-23},2^{-21},2^{-13}$ and $1$.

## 1. Is there a nontrivial $f_1$, $c_l$ with a rigorously convergent infinite series?

YES. PROVED.

- Irrational parameters (Theorems A, A', D). For every $c$ with $\delta/2$ Brjuno (Lebesgue almost every $c>1$, all
  Diophantine $\delta$, and a dense set of Liouville $\delta$) and every nonzero odd-harmonic $f_1$, finite or analytic in
  a strip, the series converges. Explicit certificate: $c=(5+\sqrt5)/4$ ($\delta=1/\sqrt5$), $f_1=\sin\theta$: for
  $R=2^{36}$ and every $N\ge1$, $\sup_{r\ge R}\|r^{-\gamma}\rho-\sum_{n\le N}r^{-\delta(n-1)}f_n\|_\sigma\le512\cdot2^{-N}$ in the
  analytic Wiener norm of width $\sigma=\frac12\log2$; the sharper constant $A_E$ gives $r\ge2^{26}$. Candidate 007's exact
  leading profile at the same $\delta$: $r\ge2^{54}$, and $r\ge2^{42}$ with $A_E$.
- Rational parameters (Theorems T, T_Q, T_{Q,h}). Let $f_1$ be a nonzero finite real odd sine polynomial. At $\delta=2h/Q$
  each resonance leaves one free exterior multipole. If the first compatibility coefficient vanishes and the responses
  $\sigma_k$ of the later obstructions to the free constants are all nonzero, the constants are fixed uniquely so that no
  logarithm appears in the density and stream series (the potential keeps the finitely many logarithmic terms listed
  in Question 3); if moreover $\inf_k|\sigma_k|>0$ ($k\ge2$ for $h=1$, $k\ge1$ for $h\ge2$), the resulting pure series
  converges with all derivatives on an exterior and solves the equations exactly.
- Explicit profiles, each certified by exact algebra (compatibility polynomial and root enclosure) and a certified lower
  bound for all responses in the independently confirmed proofs; parts of these certificates were reproduced here by
  floating checks, exact replay of boxes or separate programs, as recorded in Section 12 (not every certificate was
  recomputed): $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ at the 2 real roots of an irreducible sextic at $c=3$,
  the 6 real roots of polynomials of degree 8, 10 and 12 at $c=2$, $5/3$, $3/2$, the 5 real roots of a degree 9
  polynomial at $c=9/5$, and the 4 real roots of an irreducible degree 10 polynomial at $c=5/2$ ($\delta=3/5$, Corollary
  T_{10,3}); at $c=9/5$ also the 7 profiles that keep all eight higher harmonics of Candidate 007 and change
  only its $\sin3\theta$ coefficient (Corollary T_{9,2}.C); at $c=7/3$ ($\delta=4/7$) the 3 real roots of an irreducible
  degree 7 polynomial (Corollary T_{7,2}); at $c=7/5$ ($\delta=2/7$) the 10 real roots of an irreducible degree 14
  polynomial (Corollary T_7, response lower bounds at unit amplitude from $256$ down to $2^{-22}$); at $c=4/3$ ($\delta=1/4$) the 10 real roots of an
  irreducible degree 16 polynomial (Corollary T_8, response lower bounds at unit amplitude from $2^{12}$ down to $2^{-29}$); at $c=9/7$ ($\delta=2/9$) the 10 real roots of an
  irreducible degree 18 polynomial (Corollary T_9, response lower bounds at unit amplitude from $2^{20}$ down to $2^{-14}$); at $c=5/4$ ($\delta=1/5$) the 14 real roots of an
  irreducible degree 20 polynomial (Corollary T_10, response lower bounds at unit amplitude from $2^{26}$ down to $2^{-23}$); and, with no $\sin\theta$
  term, $f_1=\varepsilon\sin11\theta$, $\varepsilon\sin9\theta$, $\varepsilon\sin7\theta$, $\varepsilon\sin17\theta$ at $\delta=4/9,4/7,4/5,6/13$, whose first
  compatibility holds for every amplitude because the frequency is the extremal one $M=Q+2h-2$, and whose responses
  at $\varepsilon=1$ satisfy $|\sigma_k|>2^{-29},2^{-25},2^{-20},2.77\cdot10^{-12}$ for every $k\ge1$ (they scale like $\varepsilon^Q$) (Corollary T_{Q,h}.9). Near the $c=3$ profiles there are explicit three-mode families
  $|\tau|\le1/512$ and $|\tau|\le1/128$ (Corollary T.10). The four $c=5/2$ solutions (positive amplitude) are positive in
  the upper half-plane on an exterior; at the two smaller roots the density increases with the angle on the first quadrant,
  at the two larger ones it has exactly one interior angular maximum, at an angle tending to about $44.3^\circ$ and $38.7^\circ$
  (Corollary T_{10,3}(c), PROVED, with explicit exteriors at all four roots).
- These are not isolated: at $\delta=2/Q$, $3\le Q\le10$, and at $\delta=4/9$ the response condition holds on an open dense set of full
  measure of every regular component of the normalized compatibility hypersurface (Theorems T.8, T_Q.5 with Remark 3 after it,
  T_{Q,h}.5); around each of the four single harmonics the profiles $\sum_{j\in J}a_j\sin(jM\theta)$, $J$ a fixed finite set of positive odd
  integers containing 1, form an open family of convergent tuned series (Corollary T_{Q,h}.9(b)); and at every reduced $\delta$ with
  even numerator at least 4 the first condition has a nonzero real solution in every two-dimensional linear space of finite odd sine polynomials
  (Proposition T_{Q,h}.8; the response condition must still be checked).

## 2. On what domain, in which norm?

PROVED unless stated otherwise.

- Brjuno case, finite odd sine polynomial $f_1$ with top frequency $L$ (Theorem A): $r>R_0=A^{1/\delta}$ with
  $A=8Ke^{2\mathcal B(\delta/2)}\|f_1\|_{\ell^1}/\delta$, $K=2\lambda_\delta(L+2)/(c-1)$,
  $\lambda_\delta=\frac32+\frac\delta2+\frac1\delta$; $\|f_n\|_{\ell^1}\le A^n/(8Kn)$. Convergence is
  absolute and uniform in $\theta$, the sum is analytic in $z$ on a disc and in $\theta$ in a strip, and the density, stream,
  potential and every Cartesian derivative series converge uniformly on $r\ge R$ for every $R>R_0$ with the natural radial
  weights. Amplitude: $f_1\to\varepsilon f_1$ moves the radius to $|\varepsilon|^{1/\delta}R_0$. For an odd sine series $f_1$
  analytic in a strip, $\|f_1\|_{\sigma_0}<\infty$ (Theorem A'), the same conclusions hold on $r>R_0'=(A'/\sigma_0)^{1/\delta}$
  with $A'=8K'e^{2\mathcal B(\delta/2)}\|f_1\|_{\sigma_0}/\delta$, $K'=2e^{\sigma_0}(1+\sigma_0)\lambda_\delta/(c-1)$.
- Lower bound for the exterior radius (an upper bound for the radius of convergence in $z$): the top Fourier mode of $f_n$ satisfies a closed recursion solved exactly; for $\sin\theta$ at
  $\delta=1/\sqrt5$ the true growth constant lies in $[0.3896,\,84218]$, and the finite-order estimate is $0.468$
  (NUMERICAL EVIDENCE). The top mode is unaffected by the free resonant constants, which gives proved lower bounds for
  the exterior radius of the tuned series too (Section 12.6, Remark 3): at the 25 two-mode roots at
  $\delta=2/3,1/2,2/5,1/3,4/9$ they are below $0.16|\varepsilon|^{1/\delta}$, except $1.144|\varepsilon|^{9/4}$ at the largest
  two-mode root at $\delta=4/9$; at the four roots at $\delta=3/5$ they are $0.0016$, $0.0037$, $0.0259$, $0.0624$ times
  $|\varepsilon|^{5/3}$ (rounded down; PROVED); for the seven Candidate-shaped profiles the common bound is
  $6.0152\cdot10^{-10}|\varepsilon|^{9/4}$; at the three two-mode roots at $\delta=4/7$ they are $0.0127184$, $0.0430461$,
  $0.880537$ times $|\varepsilon|^{7/4}$; and for the single harmonics they are $0.507476|\varepsilon|^{9/4}$ ($\sin11\theta$ at
  $\delta=4/9$), $0.2365977|\varepsilon|^{7/4}$ ($\sin9\theta$ at $4/7$), $0.0902973|\varepsilon|^{5/4}$ ($\sin7\theta$ at $4/5$) and
  $0.4954372|\varepsilon|^{13/6}$ ($\sin17\theta$ at $6/13$); at the ten two-mode roots at $\delta=2/7$ they are $5.740541\cdot10^{-7}$ to
  $0.3441017$ times $|\varepsilon|^{7/2}$, at the ten at $\delta=1/4$ $5.257627\cdot10^{-7}$ to $0.7213489$ times $|\varepsilon|^4$, at the ten at $\delta=2/9$
  $3.631688\cdot10^{-6}$ to $1.511272$ times $|\varepsilon|^{9/2}$, and at the fourteen at $\delta=1/5$ $3.332518\cdot10^{-12}$ to $3.233134$ times $|\varepsilon|^5$; all rounded down (PROVED). These are lower bounds, not estimates of the true radius; for the single harmonics the proved
  brackets are wide, for example $0.0902973<R/|\varepsilon|^{5/4}\le2^{20}$ for $\sin7\theta$.
- Rational case: the certified radii are in the table above (sufficient radii of a majorant, $2^{16}$ to $2^{42}$ times
  $|\varepsilon|^{1/\delta}$ for the 32 two-mode profiles at $\delta=2/3,1/2,2/5,1/3,4/9,3/5,4/7$, $2^{47}$ to $2^{109/2}$ times $|\varepsilon|^{7/2}$ for the ten
  at $\delta=2/7$, $2^{113/2}$ to $2^{65}$ times $|\varepsilon|^4$ for the ten at $\delta=1/4$, $2^{127/2}$ to $2^{72}$ times $|\varepsilon|^{9/2}$ for the ten at $\delta=2/9$, $2^{147/2}$ to $2^{87}$ times $|\varepsilon|^5$ for the fourteen at $\delta=1/5$, $2^{161/4}$ to $2^{175/4}$ times $|\varepsilon|^{9/4}$ for the Candidate-shaped ones, $2^{20}$, $2^{147/4}$, $2^{213/4}$, $2^{160/3}$ times $|\varepsilon|^{1/\delta}$ for $\sin7\theta$, $\sin9\theta$, $\sin11\theta$, $\sin17\theta$). Earlier, cruder majorants gave $2^{51}$ to about $2^{484}$; the improvement comes from the actual norms of
  the first coefficients, the sharp Poisson constant, a majorant that groups the coefficients by residue modulo $Q$, and
  certified prefixes up to order 100 (order 120 with a tail-only response bound at the fifth root at $\delta=1/5$, order 140 at the third root at $\delta=2/7$, and order 300 with tail-only response bounds at the four roots at $\delta=3/5$).
- True radii (NUMERICAL EVIDENCE, root tests of the computed tuned series in 1024-bit ball arithmetic to order 300 or
  306): at $\delta=4/9$ fitted growth constants $0.304,0.408,1.03,1.71,10.7$ for the five two-mode roots, i.e. radii near
  $0.07,0.13,1.07,3.4,2\cdot10^2$ times $|\varepsilon|^{9/4}$; at $c=3$ about $0.13$ and $0.63$ times $|\varepsilon|^{3/2}$; at
  $c=5/3$ about $30$, $0.10$, $0.13$, $0.77$, $3.9$, $24$ times $|\varepsilon|^{5/2}$ at the roots $-0.4898$, $0.0490$,
  $0.1253$, $0.2121$, $0.3153$, $0.5600$; at $c=3/2$ about $440$, $0.11$, $0.55$ to $0.61$, $2.7$ to $3.6$, $11$ to $14$ and $130$ to $144$
  times $|\varepsilon|^3$ at the roots $-0.6087$, $0.0886$, $0.1407$, $0.1965$, $0.2785$, $0.5122$; at $c=5/2$ about $0.065$ to $0.07$,
  $0.06$, $0.25$ to $0.28$ and $1.1$ to $1.4$ times $|\varepsilon|^{5/3}$ at the four roots in increasing order; at $\delta=2/7$,
  $1/4$, $2/9$ and $1/5$ (double precision to orders 301, 304, 306 and 300, fits to the per-period maxima, checked against the ball-arithmetic values at
  $\delta=1/3$; repeating the runs at $\delta=2/7$ and $1/4$ to orders 601 and 600 changes the fitted $A$ on the same windows by less than $3.8\%$, at $\delta=2/9$ to order 612 by less than $6\%$ and at $\delta=1/5$ to order 600 by less than $7.1\%$) from $0.108$ to $5.3\cdot10^3$ times $|\varepsilon|^{7/2}$, from $0.116$ to $8.5\cdot10^4$ times $|\varepsilon|^4$, from $0.131$ to about $10^6$ times $|\varepsilon|^{9/2}$ and from $0.157$ to about $3\cdot10^7$ times $|\varepsilon|^5$ at
  the ten roots each (fourteen at $\delta=1/5$), largest at the root of largest modulus, and $0.41$ and $0.48$ at the third roots, whose responses
  nearly vanish once and whose certified radii are the largest; for $\sin7\theta$ at $\delta=4/5$ about $0.50|\varepsilon|^{5/4}$ ($0.496$ to $0.499$ on windows ending at order 500),
  while for $\sin9\theta$, $\sin11\theta$, $\sin17\theta$ the responses are still decreasing at order 300 and no growth
  constant is quoted (at $-0.6087$ the certified finite
  residual enclosures still grow from order 40 to 80 at $r=512$ and decrease at $r=1024$; finite data only). So the proved brackets are still wide (at the largest root at $\delta=4/9$:
  $(1.144,\,2^{117/4})$), and the sufficient radii hardly depend on the root while the estimated ones vary by a factor of about $3\cdot10^3$ at
  $\delta=4/9$, $4\cdot10^3$ at $\delta=1/3$, $5\cdot10^4$ at $\delta=2/7$ and $7\cdot10^5$ at $\delta=1/4$; the
  majorant is probably limited by its constants (a heuristic). The variation that the sufficient radii do show follows the
  response lower bound, not the growth constant: at $\delta=1/3$ the exponent never decreases as the response infimum falls
  (from $38$ at $17$ to $42$ at $1.7\cdot10^{-4}$), and at $\delta=2/5$ the root with the largest apparent radius has the smallest
  exponent ($59/2$) and the root with the smallest apparent radius the largest ($71/2$).
- Remainders and residuals (Section 12.6, Remarks 6 and 7, PROVED): every passing majorant box gives explicit
  bounds (exactly computable rationals when the box data and the radius parameter are rational), uniform on the closed exterior, for $(r\partial_r)^a\partial_\theta^b$ of the density and stream remainders after
  any order $J\ge N$ (weights $r^{-\gamma}$, $r^{-1-\gamma}$), and every finite prefix gives an exact bound for the
  stationary residual of its truncation with all derivatives. Examples: the first Candidate-shaped profile, prefix to order
  27, on $r\ge2^{171/4}$: density remainder after order 27 below $2^{-399}$, third angular derivative below $2^{-371}$;
  residual of the truncation at order 26 below $2^{-466}$ (unit amplitude).

## 3. Does the sum solve the stationary IPM equation exactly?

YES, on the exterior domain. PROVED.

- The sums are real-analytic on $r>R_0$ and satisfy $\rho=-\partial_y\Delta\chi$, $u=(-\chi_{xyy},\chi_{xxy})$,
  $(cX+u)\cdot\nabla\rho=\rho$ exactly, with the velocity generated by the convergent potential series and a single-valued
  pressure. For the tuned rational series the potential carries the logarithms
  $r^2\log r\,(\alpha+\beta\cos2\theta)+\lambda\log r$ at $\delta=2/Q$, $Q\ge3$ ($h=1$), only $\lambda\log r$ at $h=2$ and
  none at $h\ge3$, and termwise differentiation is justified. The logarithm is really there in the certified
  single-harmonic cases: $\sin11\theta$ at $\delta=4/9$, $\sin9\theta$ at $\delta=4/7$ and $\sin7\theta$ at $\delta=4/5$ have
  no pure-power potential (Corollary T_{Q,h}.9(d), (g), PROVED); the density and stream stay pure power series. The fourth
  single-harmonic center, $\sin17\theta$ at $\delta=6/13$ ($h=3$), has a pure-power potential. At every $\delta=2/Q$, $3\le Q\le10$,
  each of the sixty-four two-mode series needs a nonzero term $r^2\log r\,(\alpha+\beta\cos2\theta)$ at order $Q$ (Remark after
  Corollary T_8 and Corollaries T_9(c), T_10(c), PROVED).
- Nontrivial and nonterminating: $\rho=r^\gamma f_1+O(r^{\gamma-\delta})$, and no finite sum of analytic S1 terms
  $r^sF_s(\log r,\theta)$ with smallest density exponent below one solves the equations.
- Cutting off the potential inside a disk gives a smooth whole-plane S1 pair equal to the exterior solution outside the
  disk, with the canonical velocity; its residual is supported in the disk. A global stationary solution (zero residual
  inside as well) is OPEN.
- Without convergence (Theorem S): for every $c>1$ (rational, Liouville and divergent parameters included), every
  $C^\infty$ odd-harmonic $f_1$ and every $N$ there is an exact S1 exterior solution, with a $C^k$ common potential and
  single-valued pressure, whose density and stream agree with the first $N$ terms of the series up to $O(r^\beta)$,
  $O(r^{\beta+1})$, for any $\beta\in(p_{N+1},p_N)\setminus\{-3,-5,\dots\}$; for any $k\ge4$ one can take
  $\rho\in C^{k-2}$, $\psi\in C^{k-1}$, with the bounds holding for derivatives of order up to $k-2$ and $k-1$. One solution with the whole divergent series as expansion is OPEN.

## 4. What happens for Candidate 007's leading profile?

- Extraction is exact: 10 odd harmonics $\sin\theta,\dots,\sin19\theta$, $a_1\approx18.568$, $\|f_1\|_{\ell^1}\approx21.586$ (the exact coefficients are listed in Section 8.5 of the theory);
  the exact recursion reproduces all eight stored pure branches (exact arithmetic).
- At Brjuno $\delta$, for example $1/\sqrt5$ or a quadratic irrational within $2\cdot10^{-32}$ of the stored value, its
  series converges (PROVED). In every neighborhood of the stored $\delta$ it also diverges, with radius zero, on a dense
  $G_\delta$ set, including an explicitly constructible Liouville number (PROVED).
- At the stored rational $c=4076476460239181/2^{51}$ (first resonance $n_0=8152952920478362$): below $n_0$ the
  coefficients obey a geometric bound with $A_{\rm rat}<13178350$, and the truncation at $n_0-1$ is an exterior
  approximate solution with weighted residual below $2^{-8152952920478298}$ for $r\ge(2A_{\rm rat})^{1/\delta}\approx10^{16.6}$
  (Theorem E, PROVED). The compatibility at $n_0$ is OPEN: it is out of computational reach, and no arithmetic theorem
  applies, since the stored $\delta$ has odd numerator and composite denominator
  $4076476460239181=127\cdot114599\cdot280091797$ (exact factorization, independently confirmed), whereas Theorems P and P' need an even numerator
  over a prime. Theorem T_{Q,h} covers the stored value formally ($h=1824676646553933$, $Q=8152952920478362$), but both of
  its hypotheses concern orders near $8.2\cdot10^{15}$ (OPEN). Convergence of the logarithmic continuation there is OPEN.
  At every nearby rational with small denominator, $\delta=2h/Q\in(2/5,1/2)$ with $h\ge2$ and $Q\le120$ (217 parameters,
  $\delta=4/9$ among them), its exact profile violates the first compatibility condition, so its pure series is
  obstructed at order $Q$ (OBSTRUCTED; finite exact facts from a modular computation by two independent programs with
  equal residues). This says nothing about the stored rational itself.
- At the nearby $c=9/5$ ($\delta=4/9$; the stored $c\approx1.8103$) Candidate 007's own normalized profile is obstructed at
  order 9 (exact). Keeping its eight normalized higher harmonics and changing only the $\sin3\theta$ coefficient, the
  compatibility condition has exactly seven real solutions; the nearest moves the raw coefficient from $2.107$ to $1.660$
  (about $21\%$). All seven have certified response bounds, so each has a uniquely tuned pure series that converges with
  all derivatives at Candidate 007's amplitude, on $r>2^{50},2^{51},2^{53},2^{53},2^{53},2^{51},2^{54}$ in increasing order of
  the root, and solves the equations exactly (Corollary T_{9,2}.C(b) to (h), PROVED; for the nearest root the root, the responses and
  the box were also reproduced by separate programs, and for the first two roots the responses were rechecked in
  floating arithmetic and the prefix box of the first root was recomputed). Every exterior of uniform $C^2$ convergence
  of these seven series needs $r>6.0152\cdot10^{-10}|\varepsilon|^{9/4}$ (PROVED; about $4\cdot10^{-7}$ at Candidate 007's
  amplitude), so the proved brackets are very wide. This is $c=9/5$, not the stored $c$.
- Numerically the series at the stored $c$ (raw amplitude, 2048-bit ball arithmetic to order 500, independently rechecked
  at 2304 bits) has $\ell^1$ root tests $\|f_n\|^{1/n}=3.498$, $3.508$, $3.511$, $3.5113$ at $n=400,450,480,500$, still rising slowly,
  i.e. apparent convergence for $r\gtrsim16.5$ at the computed orders (NUMERICAL EVIDENCE; finite orders, not a convergence statement).
- Shape (PROVED for the variational statement, heuristic for its relevance): profiles whose leading stream has no
  modes below its top frequency form an explicit family converging to the zero-velocity shear
  $A_\gamma^{-1}\operatorname{sign}(y)|y|^\gamma$, $A_\gamma=\frac2\pi\int_0^\pi\sin^{1+\gamma}\theta\,d\theta$, and the family member of degree $2K+1$ uniquely minimizes the combined unweighted Wiener norm of the leading polar velocity components among
  profiles of that degree with unit $\sin\theta$ coefficient. Candidate 007's normalized coefficients $0.1135,0.0336$ for
  $\sin3\theta,\sin5\theta$ are near the family's $0.1260,0.0555$, which is consistent with its small growth constant per
  unit $\sin\theta$ coefficient ($0.19$, against $0.468$ for $\sin\theta$; NUMERICAL EVIDENCE).

## 5. What is the effect of varying $c_l$?

- Admissible set (PROVED): convergence for every $c$ with $\mathcal B(\delta/2)<\infty$, a full-measure set containing dense
  Liouville parameters; the constants depend on $c$ only through $\mathcal B(\delta/2)$, $\lambda_\delta$ and $c-1$, the radius
  bound is uniform on Brjuno sublevel sets, and the sum depends continuously on $c$ there.
- Divergence (PROVED): for $\sin\theta$, Candidate 007's profile, every finite real profile with nonzero $\sin\theta$
  coefficient and a residual set of analytic profiles, the radius is zero on a dense $G_\delta$ set of $c$ (Theorems P, P',
  C*). Explicitly (Theorem Q), radius zero holds whenever $0<|\delta-a/p|<p^{-\tau p^2}$ for infinitely many primes $p$ and
  even $a$, with $\tau>dB\pi^2/6$ for profiles with coefficients in a real number field of degree $d$ and top frequency
  $B-1$ ($\tau=4$ for $\sin\theta$, $40$ for Candidate 007's profile). At every irrational $\delta$ and for every nonzero finite
  real odd sine polynomial $f_1$, geometric density sums, geometric stream sums and exterior convergence are equivalent,
  and otherwise the terms are unbounded at every radius along almost every ray (Section 10.6); the divergence for generic
  analytic profiles is the separate residual-set statement above. So in every interval of $c$ both convergence (full measure) and divergence
  (residual) occur, and no interval is admissible.
- Rational $c$: the pure series of $\sin\theta$ is obstructed at the first resonance (OBSTRUCTED). PROVED at
  $\delta=a/p$, $p\ge5$ prime, $4\le a<p$ even ($\kappa\equiv(-1)^{(a-4)/2}\pmod p$, Theorem P), and at
  $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2$ (the compatibility polynomials of the two-mode families there are irreducible of degree at least
  6, so they do not vanish at $b=0$). By finite exact computation (not labeled PROVED) at all 55 rationals in
  $(0.40,0.50)$ with first resonance at most 60 (its 21 even-numerator, prime-denominator cases are covered by Theorem
  P and have the predicted residues), and, by an exact modular computation (a nonzero residue of $\kappa$ modulo a prime
  proves $\kappa\ne0$), at all 2074 rationals $\delta=2h/Q\in(0,1)$ with $h\ge2$ and $Q\le120$ (finite exact facts,
  independently confirmed). At a general rational it is OPEN. At odd numerators
  $\delta=a/p$ ($3\le a<p$ odd, $p$ prime, first resonance at order $2p$) an exact computation here finds the first
  compatibility coefficient of $\sin\theta$ nonzero, with $p$-adic valuation between $-2$ and $0$, at all 37 such $\delta$
  with $p\le23$ (exact finite computation, independently confirmed by two further exact programs; no congruence is proved). For compatible finite
  profiles whose responses are bounded away from zero the tuned pure series converges at every rational $\delta$
  (conditional theorem, Question 1); such profiles are known explicitly only at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2,7/3,5,13/7$ (at $c=5$
  and $c=13/7$ only $\sin7\theta$, $\sin17\theta$ and their lattice families).
- Near a rational: for $f_1=\sin\theta$ at $\delta=2/5+\varepsilon$ the near-resonant orders are $10,15,20,\dots$, each
  near-resonant inverse contributes one factor $\varepsilon^{-1}$, and the resonant stream coefficients at orders 10, 15, 20
  have poles of exact orders 1, 2, 3 in $\varepsilon$ with explicit nonzero constants (Proposition 3.4, PROVED). At every
  order the resonant stream coefficient at $n=5k$ has a pole of order exactly $k-1$, with a leading coefficient $v_k$ satisfying $k|v_k|^{1/k}\to3.57\cdot10^{-4}$
  (Proposition 3.5, PROVED, which also bounds the pole orders near every $\delta=2/Q$, $Q\ge3$, for every finite odd sine
  profile). So the poles accumulate without bound; this says nothing about the series at a fixed $\varepsilon\ne0$; a fixed tuned shape is discontinuous at $\delta=2/3$, but a unique formal shape curve $b(\delta)$
  through each of the two explicit profiles of Corollary T.3 makes every coefficient regular there (PROVED); whether $b(\delta)$ converges is OPEN.
- The finite-order fitted growth constant for $\sin\theta$ is about $0.468$ near $\delta\approx0.447$; the fitted
  estimates vary little over the tested non-resonant values of $\delta$ and depend much more on the shape of $f_1$ than on
  $c$ (NUMERICAL EVIDENCE). The actual growth constant $\limsup_n\|f_n\|^{1/n}$ is not a smooth function of $\delta$: it is
  finite at every Brjuno point and infinite on a dense set of irrationals, hence discontinuous at every Brjuno point
  (Corollary C*.1, from Theorems A and C*; PROVED).

## 6. Are resonances or small divisors a genuine obstacle?

- Exact resonances obstruct the pure power series of incompatible profiles such as $\sin\theta$ (OBSTRUCTED; PROVED in
  the cases listed as PROVED in Question 5, finite exact computation in the others; whether $\sin\theta$ is incompatible
  at every rational is OPEN, and no compatible rational is known for it). The canonical normalization
  (zero free constants) is obstructed even for tuned profiles (at order 9 for the two explicit profiles of Corollary T.3 at
  $c=3$).
- They are not an obstruction to convergence as such: for a finite profile, one free multipole per resonance removes
  every later obstruction, uniquely, once the first condition holds and every response $\sigma_k$ is nonzero, and if the
  responses are bounded away from zero the tuned series converges (Theorems T, T_Q, T_{Q,h}, PROVED). In the tuned
  series the responses $\sigma_k$ act as divisors; they can be small (at the third two-mode root at $\delta=4/9$,
  $|\sigma_{13}|\approx2.4\cdot10^{-7}$, about 150 times below $|\sigma_\infty|$, because $k\mapsto\sigma_k$ changes sign between
  12 and 13; the minimum itself is PROVED; at the fifth two-mode root at $\delta=1/5$ the global minimum is
  $|\sigma_8|\approx2.44\cdot10^{-7}$, about 82 times below $|\sigma_\infty|$, PROVED). The computed branches with isolated small responses still have modest
  finite fitted radii (the third roots at $\delta=2/7$ and $1/4$, with $\sigma_{10}\approx1.4\cdot10^{-8}$ at $\delta=1/4$,
  have apparent radii $0.41$ and $0.48$, among the smallest, and the largest certified radii). The single-harmonic runs
  show slope changes near ranges of small responses ($\sin9\theta$, $\sin11\theta$, $\sin17\theta$ to order 300).
  These are observed associations: the numerator in $H=-R/\sigma$ also varies, and the response values alone give no
  coefficient-growth law (NUMERICAL EVIDENCE). At $\delta=2/Q$, $3\le Q\le10$, and at $\delta=4/9$, on every regular component of the
  normalized compatibility hypersurface of the finite-dimensional profile spaces of Theorems T.8, T_Q.5 and
  T_{Q,h}.5, the profiles where the response condition fails form a closed null set (PROVED); at other parameters and at
  singular points this is OPEN.
- Small divisors: harmless under the Brjuno condition, where they cost a factor $e^{2\mathcal B}$ in the growth rate
  (PROVED). The Brjuno condition is sufficient; its necessity is not shown, and no statement covers every non-Brjuno $c$.
  What is proved off it (Theorem C) is divergence on a constructed exceptional set: where the rationals with nonzero
  first compatibility coefficient are dense, a coefficient has a pole in $c$ at each of them, and the series has radius
  zero on a dense $G_\delta$ set of $c$ (PROVED; the density hypothesis is PROVED for every finite real profile with a
  $\sin\theta$ term and for generic analytic profiles).
- The compatibility depends on $f_1$: $\sin11\theta$ and $\sin13\theta$ are compatible at the first resonance of
  $\delta=4/9$ (order 9), and with the free constant of order 9 set to zero (canonical choice) incompatible at the
  second (order 18) (exact, computed by two programs; Section 10). With every resonant constant free, $\sin13\theta$ is
  obstructed at order 36 and $\sin15\theta$ at order 45, because a response vanishes exactly there (OBSTRUCTED, PROVED;
  finite exact computations; the $\sin13\theta$ result is reproduced exactly by a second program in a different form of the
  recursion, the $\sin15\theta$ result by a continuation modulo two large integers whose residues equal those of the exact
  rationals, with every division checked, together with the support proposition that forces $\sigma_4=0$; both reproductions
  were audited independently). For
  $\sin11\theta$ every response satisfies $|\sigma_k|>2^{-29}$, so its tuned series exists at all orders and converges on
  $r>2^{213/4}|\varepsilon|^{9/4}$ (Corollary T_{Q,h}.9, PROVED). Its responses come close to zero: the
  rational interpolation of $k\mapsto\sigma_k$ in $t=1/(4k-2)$ has a real zero strictly between $k=513$ and $k=514$
  (PROVED, and the zero is unique in that interval), where $\sigma_{513}\approx-1.34\cdot10^{-8}$ and $\sigma_{514}\approx8.08\cdot10^{-9}$, so
  the discrete bound cannot be replaced by a bound on the interpolation. The same happens for $\sin17\theta$ at
  $\delta=6/13$: its interpolation has exactly one real zero between $k=2379$ and $k=2380$ (Corollary T_{Q,h}.9(e'), PROVED),
  while every integer response satisfies $|\sigma_k|\ge|\sigma_{2380}|>2.77\cdot10^{-12}$ (the minimum is attained only at $k=2380$),
  so its tuned series converges on $r>2^{160/3}|\varepsilon|^{13/6}$
  (Corollary T_{Q,h}.9(c), PROVED).
- First compatibility does not imply the response hypothesis. For odd $Q$ and leading frequencies far from zero (a
  single harmonic $\sin M\theta$ with $M>Q+2h-2$, or a narrow band of harmonics around a large $M$), the first
  compatibility condition can hold automatically while the responses vanish for all large $k$, so Theorem T_{Q,h} does
  not apply (Proposition T_{Q,h}.6, PROVED). For $h\ge2$ the boundary frequency $M=Q+2h-2$ is the exception: its first condition
  holds automatically and no support gap kills its responses; at $\delta=4/9,4/7,4/5,6/13$ they are certified bounded away
  from zero (Corollary T_{Q,h}.9). At $\delta=4/9$, for $M\in\{17,19\}$ and a fixed finite set $J$ of
  positive odd integers containing 1, the profiles $\sum_{j\in J}a_j\sin(jM\theta)$ are obstructed at order 18 except for
  amplitudes $(a_j)$ in a closed nowhere dense null subset of $\mathbb R^J$
  (Proposition T_{9,2}.7, PROVED, resting on recorded exact single-mode values that were replayed independently).

## 7. Is the series typically convergent, divergent or undecided?

- Convergent for almost every $c$ and every nonzero analytic $f_1$; divergent on a dense $G_\delta$ set of $c$ for every
  finite real profile with a $\sin\theta$ term and for generic analytic profiles; at a fixed divergent $c$, divergence is
  residual in the analytic profiles. So typically convergent in measure and typically divergent in the Baire sense
  (PROVED).
- At rational $c$: the pure series is obstructed for $\sin\theta$ in the cases of Question 5, and for every finite real
  profile with a $\sin\theta$ term at all but finitely many of the parameters of Theorem P (Theorem P'). At $\delta=2/Q$, $3\le Q\le10$,
  and at $\delta=4/9$, compatible profiles with responses bounded away from zero form an open dense full-measure subset of
  every regular component of the normalized compatibility hypersurface, a codimension-one set among the finite profiles
  (PROVED). Convergent tuned series also exist for profiles with no $\sin\theta$ term (Corollary T_{Q,h}.9). The
  canonical logarithmic series is undecided (OPEN), but for a nonzero finite real odd sine polynomial $f_1$ only two cases are possible (Sections 14.18,
  14.19, PROVED): either it converges on an exterior, or
  its stream and density terms are unbounded at almost every point and on a dense residual set.
- Divergence does not make the truncations meaningless: each truncation is the asymptotic expansion of an exact
  exterior solution (Theorem S, PROVED).

## 8. Strongest theorem proved

Theorem A/A' (PROVED). If $\delta/2$ is a Brjuno number and $f_1\ne0$ is an odd-harmonic sine series with
$\|f_1\|_{\sigma_0}<\infty$, then $\|f_n\|_\sigma\le A'^n/(8K'n(\sigma_0-\sigma)^{n-1})$ for $0\le\sigma<\sigma_0$, with explicit
$A',K'$, and the density, stream and potential series converge with all weighted Cartesian derivatives on
$r>(A'/\sigma_0)^{1/\delta}$; the sum is an exact real-analytic exterior solution with a convergent potential.

Its counterpart at rational parameters, Theorem T_{Q,h} with Theorems T and T_Q (PROVED): at every rational
$\delta\in(0,1)$, if $f_1$ is a nonzero finite real odd sine polynomial whose first compatibility coefficient vanishes
and whose responses satisfy $\inf_k|\sigma_k|>0$ ($k\ge2$ for $h=1$, $k\ge1$ for $h\ge2$), the free multipoles are uniquely determined so that no logarithm appears in the density and stream series, and
the pure series converges with all derivatives and a convergent potential on an explicit exterior; the hypotheses hold
at 87 explicit profiles (Question 1; all have explicit radii in the table above) and generically on regular components of the normalized compatibility hypersurface of the finite-dimensional profile spaces at
$\delta=2/Q$, $3\le Q\le10$, and at $\delta=4/9$.

Without any arithmetic condition, Theorem S (PROVED) gives exact exterior solutions with any truncation as asymptotic
expansion at every $c>1$. Supplements: Theorems B, D, E, M, M', P, P', C*, Q and the top-mode bounds (table above).

## 9. What exact step remains open?

1. At rational $\delta$, including Candidate 007's stored value, does the logarithmic series with the canonical
   normalization (zero free constants) converge? For $\sin\theta$, at every rational where its first compatibility
   coefficient is nonzero (the cases of Question 5), no choice of constants avoids logarithms, so this is the relevant
   series. Equivalently (Sections 14.17 and 14.19, PROVED reductions for a nonzero finite real odd sine polynomial $f_1$): a geometric bound on
   the realized plain stream sums $N_n=\sum_k\|g_{n,k}\|$, or equivalently on the density sums $M_n$; either bound gives
   convergence on an explicit exterior, and without it the logarithmic terms are not absolutely summable at any radius
   $R_0>e$.
   - Why this is hard (PROVED): the canonical Poisson inverse is unbounded on general admissible inputs in the plain
     norm, in every factorial norm $q!\,s^q$ with $s\le b/\gcd(a,2)$ at $\delta=a/b$ and in every half-line exponential
     norm, and there are admissible density sequences with bounded sums whose canonical streams grow faster than any
     geometric sequence. So a proof must use a property of the generated sequence. Proved partial results: at
     $\delta=2/Q$, for finite odd sine profiles with the canonical normalization, every fixed log deficit is harmless
     (each fixed-deficit subseries is entire; rationals with reduced numerator above 2, such as $4/9$, are not covered);
     the truncated recursions keeping only products with
     one factor of order at most $K$ converge whenever those low factors carry no logarithm ($K\le5$ at $\delta=2/3$); the
     stream sum is bounded by the density sum plus an explicit term from high log degrees at small shifts; a sufficient
     condition $N_n\le H_0M_n$ gives explicit radii.
   - Data at $\delta=2/3$, $f_1=\sin\theta$ (NUMERICAL EVIDENCE): certified in 512-bit ball arithmetic through order 329 (the same run's balls stay exact enclosures
     through 340 and certify $N_{332}/M_{332}>1.49$, $N_{338}/M_{338}>1.70$ and $N_{335}>0.34M_{335}$),
     the plain sums decay geometrically (about $10^{-0.70}$ per order through 300), $N_n/M_n$ first exceeds $1/4$ at order
     323, and an interior maximum of the factorially weighted log columns grows from order 235. A separate continuation from the
     order-329 midpoints to order 390 (Section 14.16; its own arithmetic bounded, the inherited input uncertainty not bounded) shows the
     stream sums above the density sums at every order $n\equiv2\pmod3$ from 332 on except 335, and the 27-order decay slopes of
     $\log_{10}M_n$, $\log_{10}N_n$ weakening from $-0.70$, $-0.68$ at order 300 to $-0.58$, $-0.55$ at order 350 and $-0.544$,
     $-0.542$ at order 360. From 351 to 360 the increments are nearly, not exactly, periodic with period 3 (the three-order
     decrements of $\log_{10}M_n$ are $-1.632$, $-1.630$, $-1.628$), and $M_{360}^{1/360}\approx0.2014$. Through order 390 the
     decrements keep drifting toward weaker decay ($-1.627$, $-1.625$, $-1.623$ from 360 to 369, $-1.622$, $-1.620$,
     $-1.619$ from 369 to 378, $-1.617$, $-1.615$, $-1.614$, $-1.612$ from 378 to 390, $-1.611$, $-1.609$, $-1.607$ from 390 to
     399, $-1.606$, $-1.604$, $-1.602$ from 399 to 408 and $-1.601$, $-1.599$, $-1.597$, $-1.595$ from 408 to 420 and $-1.594$, $-1.592$, $-1.590$ from 420 to 429 and $-1.588$, $-1.587$, $-1.585$ from 429 to 438, the continuation having
     reached order 440 and been rechecked independently through 440, with $M_{420}^{1/420}\approx0.2122$, $M_{440}^{1/440}\approx0.2150$, $\log_{10}M_{440}=-293.769$, $\log_{10}N_{440}=-293.530$), the shifted three-order multiplier
     increasing by a nearly constant $+0.0016$ per period in $\log_{10}|a_n|$ since 366, and three tail models fit to within a few times the
     rounding level of the multipliers (with the printed multipliers the exponential one has the smallest residual on the longer windows and the power one a marginally
     smaller residual on the final seven-point window, 420 to 438): a limit $A$ (with the residual ratio tending to some $E<1$ this gives $\|x_n\|^{1/n}\to(A/\sqrt{1-E^2})^{1/3}$, geometric
     decay when that limit is below one), growth like $n^{\beta}$ (a power lower bound alone forces divergence; with the residual
     ratio bounded by some $E<1$ the coefficient arrays grow like $(n!)^{\beta/3}$), with $\beta=0.555$ fitted on 348 to 370 and $0.4550$
     on 357 to 390, $0.464$ on 357 to 400 (fitted to five-decimal multipliers; $0.463$ unrounded), $0.472$ on 357 to 410, $0.483$ on 357 to 420, $0.493$ on 357 to 429 and $0.502$ on 357 to 438 (the limit model gives $|a_\infty|=0.0377$, $0.0383$, $0.0388$, $0.0395$, $0.0401$ and $0.0407$ there; on later windows both fitted values keep rising), and exponential growth of the multiplier, $\log_{10}|a_n|$
     linear in $n$ with slope $0.000529$ per order ($0.000535$ on 357 to 410, $0.000541$ on 357 to 420, $0.000546$ on 357 to 429, $0.000551$ on 357 to 438), under which $\log_{10}\|x_n\|$ grows at least quadratically and the radius is zero
     (Proposition 14.24(b); with residual ratios bounded by some $E<1$ the growth is exactly quadratic, 14.24(a); in the exact linear model with a constant residual ratio the decay would stop near order $3.4\cdot10^3$). The root-mean-square
     residuals of the three fits on 357 to 390 are $5.03$, $5.20$, $4.93$ times $10^{-4}$: on such short windows the models
     cannot be separated. Propositions 14.23 and 14.24 (PROVED, conditional statements) make the consequences exact, and
     none of their hypotheses is established. One perturbed
     continuation, with every order-329 ball replaced by a boundary point, differs by $1.5\cdot10^{-7}$ to $2.5\cdot10^{-6}$ in $\log_{10}$
     through order 332, by less than $2\cdot10^{-9}$ at 340 and by less than $5\cdot10^{-11}$ at 350, not monotonically; in the
     relative full-array $\ell^1$ distance the displacement is first amplified (by factors 1.23 and 1.92 in the stream at 330
     and 331) and then attenuated, to below $4\cdot10^{-8}$ at 340 and to $2.0\cdot10^{-4}$ (density) and $1.05\cdot10^{-5}$
     (stream) times the input displacement at 350 (a single sample, not a bound). Over this window both plain sums decline overall, though not at
     every order (the stream sum rises by a factor of about $4.8$ at order 332); whether they stay geometric is exactly the
     open question, and finite orders cannot decide it.
2. The first compatibility condition at Candidate 007's stored value (order $8.2\cdot10^{15}$), and the later responses
   there; no arithmetic shortcut is known for odd numerators and composite denominators.
3. Is the Brjuno condition necessary? Divergence is proved on a dense $G_\delta$ set and under the explicit
   approximation condition of Theorem Q; the exponent $p^2\log p$ there comes only from the height lower bound for
   $\kappa_{p,a}$. With a lower bound $|\kappa_{p,a}|\ge\mu^p$ (CONJECTURAL; the exact values for $\sin\theta$ at all 122 prime
   centers with $p\le61$ in $(0.25,0.75)$ satisfy $|\kappa_{p,a}|\ge10^{-1.01p}$, NUMERICAL EVIDENCE) the threshold would drop to
   $|\delta-a/p|<p^{-(1+\eta)p}$ (PROVED implication for centers in a compact subinterval); a gap to the Brjuno condition
   would remain.
4. For profiles not covered by Theorems P, P' (no $\sin\theta$ term, or infinitely many harmonics), are incompatible
   rationals dense?
5. Tuned series: explicit profiles at the remaining rationals (for the extremal harmonics $\sin((Q+2h-2)\theta)$ with $h\ge2$ and $Q>2h$ odd and coprime to $h$, at
   $(h,Q)$ other than $(2,5),(2,7),(2,9),(3,13)$ the response hypothesis is the only open condition), singular points of the compatibility hypersurfaces, the
   convergence of the shape curve $b(\delta)$, sharp radii (the brackets of Question 2), and whether every exterior
   solution is of the tuned or logarithmic form.
6. A global stationary solution: an interior extension with zero residual inside the disk as well.
