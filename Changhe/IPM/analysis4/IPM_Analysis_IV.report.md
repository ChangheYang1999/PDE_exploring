# IPM Analysis IV: convergence of the infinite stationary far-field series for self-similar IPM

**Status: FINAL. Central question answered: nontrivial convergent infinite far-field series exist (PROVED, with all derivatives, on explicit exteriors; independently verified). Not reached: sharp radii, convergence of the canonical logarithmic series at rational $\delta$, the compatibility condition at Candidate 007's stored parameter, necessity of the Brjuno condition, a global stationary solution.**

Run record: start T0 = 2026-10-31T01:57:42Z (logged). The research team was stopped at 2026-11-01T00:38Z, shortly before the planned stop at 23 hours (2026-11-01T00:57:42Z) of the 24-hour budget, so that this write-up finishes inside the budget. The write-up ended at T_end = 2026-11-01T00:51:55Z; elapsed time T_end minus T0 = 22 h 54 min 13 s. No research or computation was done after the team stop.

## Summary

1. **Verdict.** Yes: for almost every $c=c_l>1$ (all $c$ with $\alpha=\delta/2$ Brjuno, $\delta=1-1/c$) and every nonzero odd-harmonic analytic $f_1$, and at rational $\delta$ for explicit tuned profiles, the infinite series converges with all derivatives and sums to an exact real-analytic stationary solution on an exterior. Typical behaviour is convergent in measure and divergent in the Baire sense (the latter for every finite real profile with a $\sin\theta$ term and for generic analytic profiles); both are PROVED.
2. **Theorem A (PROVED).** If $\mathcal B(\alpha)=\sum_k\log(q_{k+1})/q_k<\infty$ and $f_1\ne0$ is an odd sine polynomial of top frequency $L$, then $\|f_n\|_{\ell^1}\le A^n/(8Kn)$ with $A=8Ke^{2\mathcal B(\alpha)}\|f_1\|_{\ell^1}/\delta$, $K=2\lambda_\delta(L+2)/(c-1)$, $\lambda_\delta=\frac32+\frac\delta2+\frac1\delta$. Density, stream and velocity potential converge absolutely and uniformly, with every weighted Cartesian derivative, on $r\ge R$ for every $R>R_0=A^{1/\delta}$; the sum solves the stationary equations exactly, has single-valued pressure and is nonterminating. Theorem A' gives the same for $f_1$ analytic in a strip, in a smaller strip.
3. **Certified radii (PROVED, sufficient, not sharp).** At $\delta=1/\sqrt5$, $c=(5+\sqrt5)/4$: $\mathcal B(\alpha)=2.5385730957726\ldots$, $A<84218$ for $\sin\theta$; a sharper constant gives $r\ge2^{26}$ for $\sin\theta$. Candidate 007's unnormalized leading profile converges on $r\ge2^{42}$, there and at a specified quadratic irrational within $2\cdot10^{-32}$ of its stored $\delta$. At $c=2N+\sqrt5$, $N\in\mathbb Z$, $N\ge16$: $\sin\theta$ converges on $r\ge128$.
4. **Rational $\delta=2h/Q$ (Theorems T, T_Q, T_{Q,h}, PROVED).** The pure series is obstructed unless the first compatibility coefficient vanishes. If a nonzero finite real odd sine polynomial $f_1$ satisfies it and the later responses satisfy $\inf_k|\sigma_k|>0$, the uniquely tuned pure density and stream series converge with derivatives on an exterior (the potential may carry finitely many logarithms). First compatibility alone does not suffice.
5. **87 certified rational profiles (PROVED, explicit sufficient radii)** at $c=3,2,5/3,3/2,7/5,4/3,9/7,5/4,9/5,5/2,7/3,5,13/7$: 76 two-mode profiles $\sin\theta+b\sin3\theta$ (radii from $2^{16}|\varepsilon|^{1/\delta}$ up to $2^{87}|\varepsilon|^5$, $\varepsilon$ the amplitude); seven profiles equal to Candidate 007's leading profile except for its $\sin3\theta$ coefficient, at $\delta=4/9$ ($r>2^{50}$ to $2^{54}$ at Candidate 007's amplitude); $\sin7\theta,\sin9\theta,\sin11\theta,\sin17\theta$ at $\delta=4/5,4/7,4/9,6/13$ ($2^{20}|\varepsilon|^{5/4}$, $2^{147/4}|\varepsilon|^{7/4}$, $2^{213/4}|\varepsilon|^{9/4}$, $2^{160/3}|\varepsilon|^{13/6}$), each with an open family of convergent nearby profiles at the same exponent within each fixed finite-dimensional odd-multiple lattice space.
6. **Divergence and obstruction (PROVED).** At $\delta=a/p$, $p\ge5$ prime, $4\le a<p$ even, the first compatibility coefficient of $\sin\theta$ is $\equiv(-1)^{(a-4)/2}\pmod p$, hence nonzero. For every finite real profile with a $\sin\theta$ term the series has radius zero on a dense $G_\delta$ set of irrational $\delta$, and the growth constant $\limsup\|f_n\|^{1/n}$ is discontinuous at every Brjuno point. Small divisors are harmless under the Brjuno condition (sufficient; necessity OPEN); exact resonances are a genuine obstruction for incompatible profiles.
7. **Finite truncations (Theorem S, PROVED).** For every $c>1$ and every $C^\infty$ odd-harmonic $f_1$, each finite truncation is realized to its order by an exact exterior solution (depending on the truncation). No solution realizing a whole divergent series is claimed.
8. **Candidate 007** (stored $c=4076476460239181/2251799813685248$, a rational $\delta$): controlled with a geometric bound below its first stream resonance at order $8152952920478362$ (Theorem E, PROVED); compatibility there OPEN (out of computational reach). Its own profile is obstructed at $c=9/5$ (PROVED).
9. **Numerical evidence only (finite orders, not proofs):** Candidate 007 at the stored parameter to order 500 (density norm root about 3.511); the canonical logarithmic $\sin\theta$ series at $\delta=1/2$ to order 300 and at $\delta=2/3$ to order 440 (conditional after order 329); tuned series at $\delta=2/7,1/4,2/9,1/5$ to orders 600 to 612; apparent true radii from about $0.05$ to $3\cdot10^7$ times $|\varepsilon|^{1/\delta}$ for the two-mode profiles.
10. **Exact remaining gap.** (a) For the canonical logarithmic series at rational $\delta$ (the case of $\sin\theta$ at $c=2,3$), the first missing inequality is a geometric bound $\|G_n\|_*\le HA_0^n$ on the realized stream sums (Section 14.16 norm); by Proposition 14.17 it is equivalent to absolute convergence of the series, and only two alternatives are possible (PROVED). (b) The first compatibility coefficient at Candidate 007's stored parameter (order $8.15\cdot10^{15}$) is neither computed nor bounded. (c) Necessity of the Brjuno condition, sharp radii (only sufficient radii and separate top-mode lower bounds are proved) and a global stationary extension are OPEN.
11. **Verification.** An independent verifier rederived the recurrence and signs with its own low-order implementation, audited every result labeled PROVED, checked every certified number and the 87 radius certificates, and at the end reread 142 standalone proof texts with no defect found; several derivations were also checked by an external referee (a second model). The verifier did not read the assembled report cover to cover or replay every historical certificate at the end, and no formal (proof-assistant) verification was done.

Labels used below: PROVED (complete proof written in this report and confirmed by the independent verifier), NUMERICAL EVIDENCE, CONJECTURAL, OBSTRUCTED, OPEN. Finite-order computations are never used as evidence of infinite-series convergence without saying so. The mathematical text (Sections 0 to 14) is self-contained apart from the computations it cites; Section 15 summarizes the numerical experiments, Section 16 describes the accompanying artifacts, and the appendices collect supporting material.

Notation: $c=c_l>1$, $\delta=1-1/c$, $\gamma=1/c$, $z=r^{-\delta}$, $r^{-\gamma}\rho=\sum_{n\ge1}z^{n-1}f_n(\theta)$,
$\alpha=\delta/2$, $\mathcal B(\alpha)=\sum_k\log(q_{k+1})/q_k$ the Brjuno sum of $\alpha$ ($q_k$ the continued
fraction denominators), $d_n=\operatorname{dist}(n\delta,2\mathbb Z)$. A rational $\delta$ is written $2h/Q$ with coprime
positive integers $h,Q$ (so $h/Q=\delta/2$ in lowest terms); its stream resonances sit at the orders $n$ with
$n\delta\in2\mathbb Z$, $n\delta\ge4$. The responses $\sigma_k$ of the tuned series are indexed by $k\ge2$ if $h=1$ and by
$k\ge1$ if $h\ge2$; "$\inf_k|\sigma_k|$" always refers to that range.

## Answers to the nine questions

### 0. Answers in brief

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

### Main results and their status

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

### Certified radii at rational $\delta$

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

### 1. Is there a nontrivial $f_1$, $c_l$ with a rigorously convergent infinite series?

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

### 2. On what domain, in which norm?

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

### 3. Does the sum solve the stationary IPM equation exactly?

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

### 4. What happens for Candidate 007's leading profile?

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

### 5. What is the effect of varying $c_l$?

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

### 6. Are resonances or small divisors a genuine obstacle?

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

### 7. Is the series typically convergent, divergent or undecided?

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

### 8. Strongest theorem proved

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

### 9. What exact step remains open?

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

# Mathematical report

## 0. Results in brief

Notation: $c=c_l>1$, $\gamma=1/c$, $\delta=1-\gamma\in(0,1)$, $p_n=1-n\delta$, $z=r^{-\delta}$,
$d_n=\operatorname{dist}(n\delta,2\mathbb Z)=2\|n\delta/2\|$, and $\alpha:=\delta/2$ with continued fraction denominators
$q_0=1,q_1,q_2,\dots$ and Brjuno sum
$$\mathcal B(\alpha)=\sum_{k\ge0}\frac{\log q_{k+1}}{q_k}\le\infty .$$

1. (Theorem A, PROVED: independently audited and confirmed line by line, including the potential reconstruction and
   all weighted derivatives.) If $\alpha=\delta/2$ is a Brjuno number ($\mathcal B(\alpha)<\infty$; this holds
   for Lebesgue almost every $\delta$, for every Diophantine $\delta$, and in particular for $\delta=1/\sqrt5$), then for
   every nonzero odd-harmonic sine polynomial $f_1$ the recursion (R) is defined at every order and
   $\|f_n\|_{\ell^1}\le A^n/(8Kn)$ with explicit $K,A$ (Section 6). The density, stream and potential series converge
   absolutely, uniformly on $r\ge R$ for every $R>R_0=A^{1/\delta}$, together with all their Cartesian derivatives with
   the natural weights, and the sum is a real-analytic solution of the stationary equation on $r>R_0$, with velocity
   generated by the convergent potential. A sharper constant $A_E$, which charges $\log(e_{k-1}/e_k)\approx\log a_{k+1}$
   instead of $\log q_{k+1}$ at each continued-fraction level, gives the radius $2^{26}$ for $\sin\theta$ at
   $\delta=1/\sqrt5$ and the common radius $128$ for $\sin\theta$ at every $c=2N+\sqrt5$, $N\in\mathbb Z$, $N\ge16$ (Section 7.5,
   PROVED: independent proof, reviewed here and independently confirmed).
2. (Theorem A', PROVED: independently confirmed, with the completed early-order potential argument of Section 7.2.)
   The same holds for every nonzero $f_1$ that is real-analytic in a strip, i.e.
   $\|f_1\|_{\sigma_0}=\sum_k|a_{1,k}|e^{\sigma_0(2k+1)}<\infty$ for some $\sigma_0>0$; then
   $\|f_n\|_{\sigma}\le A'^n/(8K'n(\sigma_0-\sigma)^{n-1})$ for $0\le\sigma<\sigma_0$.
3. (Theorem B, PROVED in the form of Section 9: maps $\mathcal A_{\sigma_0}\to\mathcal A_\sigma$, $\sigma<\sigma_0$.)
   For fixed Brjuno $\alpha$ the radius bound is uniform on bounded sets of
   $f_1\in\mathcal A_{\sigma_0}$ and the sum depends analytically on $f_1$; in $c$ the bound is uniform on every set
   $\{\delta:\mathcal B(\delta/2)\le\mathcal B_*\}$. No open interval of $c$ can be admissible for a fixed $f_1$ unless
   compatibility holds at every rational in it (Section 9).
4. (Rational $\delta$, OBSTRUCTED for the pure ansatz.) At $n\delta=2(j+1)$ the pure series exists only if the coefficient
   of $\sin((2j-1)\theta)$ in $f_n$ vanishes. This fails for $f_1=a\sin\theta$ at $c=9/5$ (order 9) and $c=2$
   (order 8), exactly. For generic $f_1$ in any finite-dimensional space containing $\sin\theta$ it fails at those $c$.
   This obstruction concerns the first resonance. When the first condition holds and every later response $\sigma_k$ is
   nonzero, the free multipoles remove all later obstructions (item 12); the convergence theorems need in addition
   $\inf_k|\sigma_k|>0$. Nonzero responses are a separate condition: at $\delta=4/9$ the profiles
   $\sum_ja_j\sin(17j\theta)$ meet the first condition automatically, but responses vanish and the pure series is
   obstructed at order 18 outside a closed nowhere dense null set of amplitudes (item 13, Proposition T_{9,2}.7).
5. (Theorems P, P' and C*, PROVED; Section 10.) At $\delta=a/p$ with $p\ge5$ prime and $a$ even, $4\le a<p$, the first
   compatibility coefficient of $f_1=\sin\theta$ satisfies $\kappa\equiv(-1)^{(a-4)/2}\pmod p$, so it is never zero;
   for every finite real profile with nonzero $\sin\theta$ coefficient (including Candidate 007's exact profile) $\kappa\ne0$
   for all but finitely many $p$. Beyond these theorems, a modular computation gives $\kappa\ne0$ for $\sin\theta$ at every
   $\delta=2h/Q\in(0,1)$ with $h\ge2$ and $Q\le120$ (2074 parameters) and for Candidate 007's exact profile at every such
   $\delta\in(\frac25,\frac12)$ (217 parameters) (finite exact facts, independently confirmed; Section 10). The prime-denominator parameters of Theorems P and P' are dense, so for these $f_1$ the series has radius zero on a dense
   $G_\delta$ set of $\delta$: convergence is generic in measure (Theorem A), divergence is generic in the sense of Baire
   category. Consequently the growth constant $\limsup_n\|f_n\|_0^{1/n}$ is finite at every Brjuno point and infinite on
   a dense set, so it is discontinuous at every Brjuno point and is not a smooth function of $\delta$ (Corollary C*.1,
   PROVED); finite-order fits that vary little over sampled parameters do not contradict this. The same holds for a residual set of analytic profiles, there is a computable divergent Liouville parameter
   in every interval, and at a fixed divergent parameter divergence is residual in the analytic data. At every
   divergent irrational parameter the terms of the density, stream, radial-velocity and potential series are unbounded
   at every radius along almost every ray, and at every irrational $\delta$ geometric density sums, geometric stream
   sums and exterior convergence are equivalent, with no arithmetic condition (Section 10.6, PROVED). Quantitatively
   (Theorem Q, Section 10.4, PROVED), every irrational $\delta$ with infinitely many approximations
   $0<|\delta-a/p|<p^{-\tau p^2}$ ($p$ prime, $a$ even), $\tau>dB\pi^2/6$, gives radius zero for every profile with
   coefficients in a real number field of degree $d$, top frequency $L=B-1$ and nonzero $\sin\theta$ coefficient. (H)
   does depend on $f_1$: $\sin11\theta$ is compatible at the first resonance of $\delta=4/9$. For $f_1=x\sin\theta+h$ with
   any analytic higher modes $h$, the threshold $\tau>\pi^2/3$ suffices for all $x$ outside a set of Hausdorff dimension
   zero (Corollary Q2, PROVED; independently confirmed). The exponent $p^2\log p$ comes only from the height lower
   bound for the first compatibility coefficient $\kappa_{p,a}$: divergence holds whenever
   $|\delta-a/p|<|\kappa_{p,a}|p^{-(1+\eta)p}$ infinitely often with $a/p$ in a fixed compact subinterval of $(0,1)$
   (Section 10.5, PROVED: independently confirmed), and the computed $|\kappa_{p,a}|$ for $\sin\theta$ are at least
   $10^{-1.01p}$ for $p\le61$ (NUMERICAL EVIDENCE).
6. The stored rational parameter of Candidate 007 first resonates at order $n=8152952920478362$. Candidate 007's profile
   $f_1$ at every Brjuno $\delta$ (for example $\delta=1/\sqrt5$, or a quadratic irrational within $2\cdot10^{-32}$ of the
   stored $\delta$) gives a convergent series by Theorem A. At the stored value itself, Theorem E (Section 8.1;
   PROVED, independently confirmed with outward constants) gives the geometric bound for every order below the first resonance.
   At the nearby rational $\delta=4/9$ Candidate 007's own leading profile is obstructed at order 9, but changing only its
   $\sin3\theta$ coefficient by $0.448$ (about $21\%$) satisfies the first compatibility condition, and the resulting
   profile, which keeps all eight higher harmonics of Candidate 007, has a uniquely tuned convergent pure series at
   $c=9/5$ on $r>2^{593}$ (Corollary T_{9,2}.C, PROVED; item 14), and on $r>2^{300}$ with the sharper constants of
   Section 12.6, Remark 4, on $r>2^{60}$ with Remark 5, and on $r>2^{53}$ with Remark 5 and a certified prefix (PROVED).
   All seven compatible modifications of this kind (the seven real roots of the compatibility polynomial) are now
   certified, each with a convergent tuned series on $r>2^{54}$ at Candidate 007's amplitude (PROVED; item 14).
7. (Rational $\delta$, logarithmic series; Section 14.) The polynomial-in-$\log r$ continuation exists formally to all
   orders, with sharp log-degree bounds and a Gevrey bound of order $1/n_r$ (PROVED; independently confirmed). Two
   sufficient criteria for convergence are proved (Proposition 14.5: geometric plain sums of density and stream;
   Section 14.5(b): a geometric factorial norm), and at $\delta=2/3$ the highest log degree is explicit and harmless (Proposition 14.7,
   PROVED). Convergence itself is OPEN. Numerics (Section 14.6, NUMERICAL EVIDENCE of finite-order behavior): the density
   plain sums decay geometrically through order 290 at $\delta=2/3$, 320 at $4/9$ and 300 at $1/2$; at $2/3$ an interior
   maximum of $k!\,\|f_{n,k}\|$ appears from order 235 and the stream plain sums decay more slowly than the density sums from about order 263. A fixed
   angular truncation converges at every $\delta$ (Proposition 14.8, PROVED; independently confirmed), so such
   truncations cannot detect divergence. Every fixed log deficit is harmless (Section 14.9): at $\delta=2/3$, $\sin\theta$,
   the factorially weighted column of deficit $d$ grows at most like $((d+1)\lambda)^k$ per block, $\lambda=157/129600$
   (PROVED), and the same holds at every $\delta=2/Q$ for finite profiles (PROVED; independently confirmed); the
   growth that matters lies at deficits proportional to the order, where no estimate is known. Neither the factorial
   norm nor a reciprocal-binomial norm closes under the recursion operators on general inputs (Section 14.11,
   PROVED; independently confirmed); the loss sits at angular modes near the diagonal $m\approx n\delta-3$, and a norm
   that is factorial only near the diagonal fails too (Section 14.12, PROVED; independently confirmed). In the
   data the Poisson step at the diagonal does not realize this loss (14.6 item 7). For profiles with separated high
   harmonics the Gevrey order improves to $(1-1/A)/Q<1/Q$ (Section 14.13, PROVED; independently confirmed).
   Convergence follows if one realized ratio, the factorial norm of the forcing over the weighted sum of products of
   the factorial norms of its factors, stays bounded on the generated sequence (Section 14.14, PROVED; independently
   confirmed); this is a sufficient route, not a characterization. At $\delta=2/3$ the unweighted ratio stays below
   $0.3691$ through order 290, but through that order the factorial norms themselves grow like a Gevrey sequence of
   order near $0.30$, while the plain column sums decay geometrically (NUMERICAL EVIDENCE); if this growth persists to
   all orders, the factorial-norm route cannot close at $\delta=2/3$ (PROVED implication), and an exact example shows
   that such growth alone does not imply divergence (Section 14.15, PROVED). A second sufficient route needs only
   the realized ratio of the plain stream and density sums: if $N_n\le H_0M_n$ for all $n$, the series converges on
   an explicit exterior whose radius depends on $H_0$ (Section 14.16, PROVED; independently confirmed); at $\delta=2/3$
   this is $r\ge64$ for $H_0=1/4$, improved to $r\ge27$ in Section 14.18(a) (PROVED). The value $H_0=1/4$ is excluded
   by the data: the ratio is at most $0.2115$ through order 322 (certified); it rose from $10^{-2.53}$ at order 260 to
   $10^{-1.60}$ at 290, was $10^{-2.01}$ at 300, $0.0821$ at 311 and $0.207$ at 317, and it is $0.336$ at order 323 and
   $0.322$ at 326; at orders 332 and 338 the stream sums exceed the density sums:
   $N_{332}/M_{332}>1.49$ and $N_{338}/M_{338}>1.70$, while $N_{335}>0.34M_{335}$ (certified ball arithmetic through order 340,
   independently reproduced; NUMERICAL EVIDENCE). A continuation from the order-329 midpoints (inherited uncertainty not
   bounded; Section 14.16) has $N_n>M_n$ at every order $n\equiv2$ modulo 3 from 332 to 368 except 335. So (14.16.1) fails for every $H_0<1.70$, and the conditional radii $110$ and $46$ computed for $H_0=0.34$
   do not apply. Whether $\sup_nN_n/M_n<\infty$ is OPEN. A geometric bound on the plain stream sums alone
   already implies one on the density sums and convergence, and it is necessary for absolutely summable stream log
   terms, so in that sense the open problem at rational $\delta$ is exactly the geometric growth of the realized stream
   sums (Section 14.17, PROVED). Through order 300 they decay geometrically at
   $\delta=2/3$, with a rate that changed once near orders 245 to 263 (NUMERICAL EVIDENCE). There is no intermediate
   case: if the stream terms are bounded on any set of positive area, the series converges on an exterior; otherwise
   the stream series diverges at almost every point (Section 14.18, PROVED). The same section lowers the conditional
   radius at $\delta=2/3$ from $64$ to $27$ for $H_0=1/4$ and from $110$ to $46$ for $H_0=0.34$ (both values of $H_0$
   are excluded by the data). On the generated sequence a geometric bound on the density sums alone also
   suffices, because the next-order density equation controls the stream through a coercive transport operator
   (Section 14.19, PROVED); so the open problem is a geometric bound on either sum.
8. (Sections 7.4 and 8.2, PROVED.) No finite sum of analytic S1 terms $r^sF_s(\log r,\theta)$ with smallest density
   exponent below one is an exact solution, so the convergent solutions are nonterminating. The top Fourier mode of
   $f_n$ obeys a closed scalar recursion solved by a beta integral; it bounds the radius of the series in $z$ above by an
   explicit $R_{\rm top}$ ($1/R_{\rm top}=0.3896$ for $\sin\theta$ at $\delta=1/\sqrt5$, against the finite-order growth
   estimate $0.468$, NUMERICAL EVIDENCE). Its coefficients have the exact asymptotic
   $h_n\sim\mathcal K R_H^{-n}n^{-1-\nu}$, and the edge recurrences reproduce this sector with radii $R_K\downarrow R_H$
   (Section 14.22, PROVED).
9. (Section 8.3.) The profiles whose leading stream has no mode below its top frequency form an explicit family
   whose limit is the exact zero-velocity, non-$C^1$ shear $A_\gamma^{-1}\operatorname{sign}(y)|y|^\gamma$,
   $A_\gamma=\frac2\pi\int_0^\pi\sin^{1+\gamma}\theta\,d\theta$ (PROVED); at each degree the
   family member uniquely minimizes the combined unweighted Wiener norm $V_0$ of the leading polar velocity components (Proposition 8.4, PROVED; independently confirmed). Candidate 007's
   profile is close to this family, which gives a heuristic explanation of its small finite-order growth constant.
10. (Section 12.1, Theorem M, PROVED; independently confirmed.) At every Brjuno $\delta$ the exterior solution
   with arbitrary prescribed, geometrically bounded harmonic stream multipoles $h_kr^{2-2k}\sin((2k-2)\theta)$ is given by
   a double series in $(r^{-\delta},r^{-2})$ that converges with all derivatives; the small divisors are needed only at
   the generated velocities. Theorem M' (PROVED; independently confirmed) extends this to real-analytic profiles.
11. (Section 12.2, Theorem S, PROVED; independently confirmed.) Every truncation of the canonical series is the
   asymptotic expansion of an exact exterior solution: for every $c>1$, every $C^\infty$ S1 profile $f_1$, every $N$ and
   every $\beta\in(p_{N+1},p_N)\setminus\{-3,-5,\dots\}$ there is, on some exterior $r>R$, an S1 solution of $-\Delta\psi=\partial_x\rho$
   and $(cX+u)\cdot\nabla\rho=\rho$ with $\rho-\rho_N=O(r^\beta)$ and $\psi-\psi_N=O(r^{\beta+1})$ together with finitely
   many derivatives (for any $k\ge4$, $\rho\in C^{k-2}$ and $\psi\in C^{k-1}$ with the bounds for derivatives of order up
   to $k-2$ and $k-1$), and with a single-valued pressure. This holds at rational, Liouville and divergent parameters
   alike: divergence obstructs the convergent representation, not the existence of solutions with these asymptotics.
   The proof is a weighted energy estimate for the transport operator, in which the term $-\rho$ gives the coercivity
   $1-c\beta>0$, combined with an exact weighted Poisson inverse; it needs no all-order small-divisor condition. By
   Section 12.3 (PROVED) these solutions also have a common potential $\chi\in C^k$ with $\chi_{xy}=\psi$ and
   $-\partial_y\Delta\chi=\rho$ on every slightly smaller exterior.
12. (Section 12.4, Theorem T, PROVED: independently audited and confirmed.) At $c=3$, for every real odd-harmonic sine
   polynomial $f_1$ with $O_6(f_1)=0$ whose response coefficients satisfy $\inf_k|\sigma_k|>0$, there is exactly one
   choice of the multipoles $H_{3k}r^{2-2k}\sin((2k-2)\theta)$ for which the pure power series exists to all orders, and
   then it converges absolutely with all derivatives on an exterior $r>A^{3/2}$; the sums are real analytic, contain no
   logarithm, solve the equations exactly and have $\rho=r^{1/3}f_1+O(r^{-1/3})$. The hypotheses hold, by exact algebra, for
   $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ with $b=0.28066\ldots$ or $b=0.64635\ldots$, the real roots of an irreducible
   sextic (Corollary T.3, PROVED; the exact arithmetic was independently reproduced), and for them the exterior
   $r>2^{63}|\varepsilon|^{3/2}$ is admissible, and per profile $r>2.61\cdot10^{16}|\varepsilon|^{3/2}$ and
   $r>4.75\cdot10^{14}|\varepsilon|^{3/2}$ (Corollary T.4 and the sharper constants after it, PROVED). The admissible
   profiles are not isolated: the response condition is open (Theorem T.6, PROVED), so near each of them every profile on
   the hypersurface $O_6=0$ qualifies, for example $\sin\theta+b(\tau)\sin3\theta+\tau\sin5\theta$ with $b(\tau)$ real analytic
   and $|\tau|\le10^{-13}$ (Corollary T.7, PROVED, common exterior $r>2^{72}|\varepsilon|^{3/2}$). On every connected analytic
   piece of $\{O_6=0\}$ containing one admissible profile, the admissible profiles form an open dense set of full measure
   (Theorem T.8, PROVED), and the same holds on every regular component of the normalized hypersurface (Theorem T_Q.5,
   PROVED). For the three-mode profiles the limiting response $\sigma_\infty(b,\tau)$ is an explicit cubic with no zero on
   the real compatibility curve for $-3\le\tau\le98$ (Proposition T.9, PROVED), and explicit families exist for
   $|\tau|\le1/512$ and $|\tau|\le1/128$ with exteriors $r>2^{63}$ and $2^{57}$ times $|\varepsilon|^{3/2}$ (Corollary T.10,
   PROVED). The potential is a convergent series whose only
   logarithms are $r^2\log r(\alpha+\beta\cos2\theta)$ and $\lambda\log r$ (Proposition T.5, PROVED). For these profiles the canonical normalization $H=0$ is
   obstructed at order 9, and the measured growth constants of the tuned series are about $0.26$ and $0.73$ (NUMERICAL
   EVIDENCE). So at this rational parameter resonance does not prevent convergence; it prevents the canonical series
   and, for profiles such as $\sin\theta$ with $O_6\ne0$, every pure series. The tuned series is not the limit of the
   nonresonant series of the same shape as $\delta\to2/3$ (a stream coefficient at order 9 has a pole), but a unique
   formal shape $b(\delta)$ through each of these two profiles makes every coefficient regular at $\delta=2/3$ (Section 12.4,
   Remarks 6 and 7, PROVED); whether $b(\delta)$ converges is OPEN.
13. (Section 12.5, Theorem T_Q: PROVED for every integer $Q\ge3$, independently confirmed. Corollary T_5 (a), (b), (c),
   Proposition T_Q.4, Theorem T_Q.5, Corollary T_4 (a), (b), (c), Corollary T_6 (a), (b): PROVED.) The mechanism of Theorem T holds at every
   $\delta=2/Q$, $Q\ge3$ an integer ($c=Q/(Q-2)$): resonances sit at $n=kQ$, $k\ge2$, each obstruction is affine in the
   preceding multipole with slope $\sigma_k$ (a degree-$Q$ polynomial in $f_1$), and for a nonzero real odd sine
   polynomial $f_1$ with $O_{2Q}(f_1)=0$ and $\inf_{k\ge2}|\sigma_k|>0$ the uniquely tuned pure series converges with all derivatives on an exterior $r>A^{Q/2}$, with
   $\rho=r^{1-2/Q}f_1+O(r^{1-4/Q})$ and a convergent potential series whose only logarithms sit at orders $Q$ and $2Q$. At
   $\delta=2/5$ ($c=5/3$) the hypotheses hold exactly for $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ at the six real roots $b$
   of an irreducible integer polynomial of degree 10 (a degree argument: $\sigma_k$ has degree 5 in $b$), with certified
   all-$k$ response bounds and explicit exteriors $r>2^{140}$ to $2^{175}$ times $|\varepsilon|^{5/2}$ (common
   $2^{185}|\varepsilon|^{5/2}$); the minimum of $|\sigma_k|$ over $k\ge2$ is attained at exactly one $k$ for each profile
   (exact values), which sharpens the exteriors to $r>7.01\cdot10^{37}$ to $5.33\cdot10^{48}$ times $|\varepsilon|^{5/2}$ (about
   $2^{126}$ to $2^{162}$). At $\delta=1/2$ ($c=2$) the same holds at the six real roots of an irreducible polynomial of
   degree 8, with exact response infima (one of them not attained) and exteriors $r>2^{80}$ to $2^{98}$ times
   $\varepsilon^2$ (Corollary T_4). At $\delta=1/3$ ($c=3/2$) the same holds at the six real roots of an irreducible polynomial
   of degree 12, with exact infima (two not attained) and exteriors $r>2^{180}$ to $2^{219}$ times $|\varepsilon|^3$ (Corollary
   T_6, PROVED). At $\delta=2/7$ ($c=7/5$) the hypotheses hold at the ten real roots of an irreducible polynomial of degree
   14, with certified response lower bounds and exteriors $r>2^{47}$ to $2^{109/2}$ times $|\varepsilon|^{7/2}$ from the
   certified-prefix majorant of Remark 5(b) (Corollary T_7, PROVED), and at $\delta=1/4$ ($c=4/3$) at the ten
   real roots of an irreducible polynomial of degree 16, with exteriors $r>2^{113/2}$ to $2^{65}$ times $|\varepsilon|^4$ (Corollary
   T_8, PROVED), and at $\delta=2/9$ ($c=9/7$) at the ten real roots of an irreducible polynomial of degree 18, with
   exteriors $r>2^{127/2}$ to $2^{72}$ times $|\varepsilon|^{9/2}$ (Corollary T_9, PROVED). At $\delta=1/5$ ($c=5/4$) the hypotheses hold at the fourteen real roots of an irreducible polynomial of degree 20, with certified response lower bounds $2^{-23}$ to $2^{26}$ and exteriors $r>2^{147/2}$ to $2^{87}$ times $|\varepsilon|^5$ (Corollary T_10, PROVED). At every $\delta=2/Q$, $3\le Q\le10$, every one of these sixty-four two-mode series needs a nonzero potential
   term $r^2\log r\,(\alpha+\beta\cos2\theta)$ at order $Q$ (Remark after Corollary T_8 and Corollaries T_9(c), T_10(c), PROVED); the density and stream
   series stay pure. The resonance-block majorant (Section 12.6, Remark 5(b); PROVED: independent proof, reviewed here)
   lowers these exteriors to $2^{61/2}$ to $2^{73/2}$ at $c=5/3$, $2^{43/2}$ to $2^{25}$ at $c=2$, $2^{39}$ to $2^{43}$ at $c=3/2$, and
   $2^{35/2}$, $2^{16}$ at $c=3$ (Theorem T), times $|\varepsilon|^{Q/2}$; starting it from certified prefixes gives
   $2^{59/2}$ to $2^{71/2}$ at $c=5/3$, $2^{41/2}$ to $2^{24}$ at $c=2$ and $2^{38}$ to $2^{42}$ at $c=3/2$ (Remark 5(c)). Remarks 6 and 7
   of Section 12.6 (PROVED) turn each passing box into explicit bounds for the remainder after any order and for the
   stationary residual of the truncated series, with all derivatives. At $\delta=2/Q$, $3\le Q\le10$, the response condition holds on an open dense set
   of full measure of every regular component of the normalized compatibility hypersurface, with no known profile
   required (Theorem T_Q.5 and Remark 3 after it).
14. (Section 12.6, Theorem T_{Q,h}, Proposition T_{Q,h}.3, Corollary T_{9,2} and Theorem T_{Q,h}.5: PROVED, independent
   proofs reviewed here, with an independent exact reproduction here of the nonvanishing certificate and of the radius
   boxes of Corollary T_{9,2}.) The same conditional theorem holds at every rational $\delta\in(0,1)$. Write $\delta=2h/Q$ with coprime $h\ge2$, $Q>2h$ (the case $h=1$ is item 13).
   The resonances sit at $n=kQ$ for every $k\ge1$, so the first compatibility condition $O_Q(f_1)=0$ comes before any
   free constant, and the free constant of order $Q$ already acts on the next obstruction. For a nonzero real odd sine
   polynomial $f_1$ with $O_Q(f_1)=0$ and $\inf_{k\ge1}|\sigma_k|>0$ the uniquely tuned pure series converges with all derivatives on an exterior $r>A^{Q/(2h)}$,
   with $\rho=r^{1-2h/Q}f_1+O(r^{1-4h/Q})$; the potential series needs one logarithm $\lambda\log r$ if $h=2$ and none if
   $h\ge3$. The proof is the majorant of item 13 with shifted starting degrees and a different order of the unknowns.
   At $\delta=4/9$ ($c=9/5$, near Candidate 007) the hypotheses hold exactly for $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ at
   the five real roots of an irreducible polynomial of degree 9. Here the response has the same degree 9 as the
   obstruction, so nonvanishing needs more than a degree count: an exact certificate that no $\sigma_k$, $k\ge1$, and not
   $\sigma_\infty$ is a rational multiple of the obstruction. With certified all-$k$ response bounds $2^{-29}$ to $1$, the
   exteriors $r>2^{414}$ to $2^{1935/4}$ times $|\varepsilon|^{9/4}$ are admissible (common $2^{484}|\varepsilon|^{9/4}$). With the exact
   infima, which are attained only at $k=7,4,13$, not at all (the limit) and at $k=5$ (Corollary T_{9,2}(c), PROVED,
   independently confirmed), the exteriors improve to $2^{360}$ to $2^{1899/4}$, common $2^{475}$. With the actual norms of
   $f_1,\dots,f_9$ in place of the Catalan bounds, a smaller bilinear constant and the sharp Poisson norm (Section 12.6,
   Remark 4; PROVED: independent proof, reviewed here) the proved exteriors are $2^{225}$ to $2^{1017/4}$, and $2^{747/4}$ to
   $2^{963/4}$ with the exact infima. The resonance-block majorant of Section 12.6, Remark 5 (PROVED: independent proof,
   reviewed here) gives $2^{39},2^{38},2^{167/4},2^{39},2^{171/4}$ with the bounds of (b) and
   $2^{38},2^{73/2},2^{161/4},2^{151/4},2^{147/4}$ with the exact infima, and $2^{117/4}$ at the largest root when it starts
   from a certified prefix to order 90; with certified prefixes to order 36 the first four roots get
   $2^{129/4},2^{125/4},2^{129/4},2^{121/4}$, and $2^{32}$ at the third with a prefix to order 54 (all times $|\varepsilon|^{9/4}$). The proved lower bounds from the top mode for the
   required exterior radius are at most $1.15|\varepsilon|^{9/4}$ (Remark 3; lower bounds only), and the computed tuned series to order 306 suggest true radii near $2\cdot10^2$ at the
   largest root and near $0.07$, $0.13$, $1.07$ and $3.4$ at the first four roots (NUMERICAL EVIDENCE). At the
   third profile, $|\sigma_{13}|\approx2.4\cdot10^{-7}$ is about 150 times smaller than $|\sigma_\infty|$ because $k\mapsto\sigma_k$
   has a real zero near $k=13$ (NUMERICAL EVIDENCE). On every regular component of the normalized compatibility
   hypersurface at $\delta=4/9$, the admissible profiles are open, dense and of full measure (Theorem T_{Q,h}.5). If
   Candidate 007's normalized higher harmonics $\sin5\theta,\dots,\sin19\theta$ are kept and only its $\sin3\theta$ coefficient
   is changed, the first compatibility condition at $\delta=4/9$ has exactly seven real solutions (PROVED: independent
   proof, reviewed here); the nearest moves the normalized coefficient from $0.1135$ to $0.0894$, and for it every response
   satisfies $|\sigma_k|>2^{-28}$, so its tuned pure series converges with all derivatives on $r>2^{2331/4}|\varepsilon|^{9/4}$
   ($r>2^{593}$ at Candidate 007's own amplitude, $r>2^{300}$ with Remark 4, $r>2^{60}$ with Remark 5, $r>2^{53}$ with a certified prefix; Corollary T_{9,2}.C, PROVED: independent proof,
   reviewed here, with the root, the responses and the box reproduced by separate programs here). The first, second and fourth
   of the seven roots are certified in the same way (Corollary T_{9,2}.C(e), (c), (d)), with $r>2^{50}$, $2^{51}$, $2^{53}$ at
   Candidate 007's amplitude by Remark 5 with certified prefixes, and so is the fifth (Corollary T_{9,2}.C(f), with the
   original constants $r>2^{570}$, with a certified prefix $r>2^{53}$) and the sixth (Corollary T_{9,2}.C(g), $r>2^{543}$
   with the original constants, with a certified prefix $r>2^{51}$) and the seventh (Corollary T_{9,2}.C(h), $|\sigma_k|>1$ for
   all $k$, $r>2^{534}$ with the original constants, with a certified prefix $r>2^{54}$). So all seven roots carry convergent
   tuned series, with restored exteriors $2^{50},2^{51},2^{53},2^{53},2^{53},2^{51},2^{54}$ in increasing order of the root.
   At $\delta=3/5$ ($c=5/2$, $h=3$, the first parameter whose reduced numerator is odd and greater than one) the hypotheses hold exactly for
   $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ at the four real roots of an irreducible polynomial of degree 10, and the
   potential series needs no logarithm (Corollary T_{10,3}, PROVED: independent exact certificate, reviewed here); explicit
   radii are certified at all four roots, $r>2^{133/6}$, $2^{137/6}$, $2^{65/3}$ and $2^{125/6}$ times $|\varepsilon|^{5/3}$ in increasing
   order of the root (Corollary T_{10,3}(b), PROVED: independent certificates).
   At $\delta=4/7$ ($c=7/3$) the same holds at the three real roots of an irreducible polynomial of degree 7, with exteriors
   $r>2^{27}$, $2^{117/4}$, $2^{109/4}$ times $|\varepsilon|^{7/4}$ (Corollary T_{7,2}, PROVED). For odd $Q$ the first condition is
   solvable in every two-dimensional linear space of finite odd sine polynomials (Proposition T_{Q,h}.8, PROVED). The single harmonic
   $\sin((Q+2h-2)\theta)$ is compatible at the first resonance for every amplitude, and its tuned series converges at
   $\delta=4/9$ ($\sin11\theta$, $r>2^{213/4}|\varepsilon|^{9/4}$) and at $\delta=4/7$ ($\sin9\theta$, $r>2^{147/4}|\varepsilon|^{7/4}$), with open
   lattice families of convergent profiles around both, at $\delta=4/5$ ($\sin7\theta$, $r>2^{20}|\varepsilon|^{5/4}$) and at
   $\delta=6/13$ ($\sin17\theta$, $r>2^{160/3}|\varepsilon|^{13/6}$) (Corollary T_{Q,h}.9, PROVED). The three centers with $h=2$ need
   the potential logarithm (Corollary T_{Q,h}.9(d), (g), PROVED); the $\sin17\theta$ center ($h=3$) has a pure-power potential.
   Candidate 007's stored rational parameter is formally covered
   ($h=1824676646553933$, $Q=8152952920478362$), but its first compatibility condition is out of computational reach.
15. (Section 12.6, Propositions T_{Q,h}.6 and T_{9,2}.7: PROVED, independent proofs reviewed here line by line and
   independently confirmed.) First compatibility does not imply the response hypothesis. If the leading frequencies
   avoid a neighbourhood of zero in the sense that $2h-1\notin Q\Lambda+E_{Q-1}$ ($\Lambda$ the signed support of $f_1$), every
   response $\sigma_k$ with $k>(QL+Q-2h+4)/(4h)$ vanishes, so Theorems T_Q and T_{Q,h} do not apply; for odd $Q$ this holds for
   $\sin M\theta$ with $M>Q+2h-2$, and for $h\ge2$ the first compatibility condition then holds automatically. At $\delta=4/9$,
   every pure series with leading profile $\sin13\theta$ is obstructed at order 36 and with $\sin15\theta$ at order 45, for
   every choice of the resonant constants (finite exact computations, each independently reproduced: PROVED), and on the lattices $\sum_ja_j\sin(jM\theta)$,
   $M\in\{17,19\}$, the pure series is obstructed at order 18 outside a closed nowhere dense null set of amplitudes.
   The threshold frequency $M=Q+2h-2$ behaves differently: $\sin11\theta$ at $\delta=4/9$ has every response above $2^{-29}$ and a
   convergent tuned series (Corollary T_{Q,h}.9, PROVED).

The insight behind Theorem A is that the recursion is of Cauchy-Kovalevskaya type (the factor $1/((n-1)(c-1))$ absorbs
the single angular derivative per nonlinear interaction; the Poisson inverse loses nothing in angular regularity), and
the small divisors $d_n$ enter in exactly the way they enter Siegel's linearization problem, one divisor per node of the
binary interaction tree. Brjuno's counting argument then gives geometric bounds.

## 1. Setting

Cartesian $(x,y)$, polar $x=r\cos\theta$, $y=r\sin\theta$. Potential formulation:
$$\rho=-\partial_y\Delta\chi,\qquad u=(-\chi_{xyy},\chi_{xxy}),\qquad (cX+u)\cdot\nabla\rho-\rho=0. \tag{E}$$
With $\psi:=\chi_{xy}$ we have $u=(-\psi_y,\psi_x)$ and $-\Delta\psi=\partial_x\rho$. Moreover
$u\cdot\nabla\rho=\psi_x\rho_y-\psi_y\rho_x=r^{-1}(\psi_r\rho_\theta-\psi_\theta\rho_r)$.

S1 symmetry: $\rho$ even in $x$, odd in $y$; $\chi$ even in $x$ and $y$; $\psi$ odd in $x$ and $y$. On the circle:
$$f=\sum_{k\ge0}a_k\sin((2k+1)\theta),\quad g=\sum_{j\ge1}b_j\sin(2j\theta),\quad C=\sum_{m\ge0}c_m\cos(2m\theta).$$

Series: $\rho=\sum_n r^{p_n}f_n$, $\psi=\sum_n r^{P_n}g_n$, $\chi=\sum_n r^{q_n}C_n$ with $P_n=p_n+1=2-n\delta$,
$q_n=p_n+3=4-n\delta$. Since $r^{p_n}=r^\gamma z^{n-1}$, $r^{-\gamma}\rho=\sum_n z^{n-1}f_n$.

Amplitude scaling. $\rho_\lambda(X)=\lambda^{-1}\rho(\lambda X)$ maps solutions of (E) to solutions; on the series it
maps $f_n\mapsto\lambda^{-n\delta}f_n$. So replacing $f_1$ by $\varepsilon f_1$ replaces $f_n$ by $\varepsilon^nf_n$ and
moves the radius of convergence $R_0$ to $|\varepsilon|^{1/\delta}R_0$ ($\varepsilon\ne0$ real). For $\varepsilon>0$ this is the
dilation with $\lambda=\varepsilon^{-1/\delta}$, not a different convergence mechanism; for $\varepsilon<0$ it is that dilation
for $|\varepsilon|$ followed by $f_n\mapsto(-1)^nf_n$ (the coefficients are homogeneous of degree $n$ in $f_1$), which is
not a dilation but leaves the radius unchanged. All radius statements below are therefore stated together with the amplitude.
This applies to the pure series. For the logarithmic series of Section 14 (rational $\delta$), replacing $f_1$ by
$\varepsilon f_1$ still replaces each canonical coefficient $F_n(t,\theta)$ by $\varepsilon^nF_n(t,\theta)$ at fixed
$t=\log r$ (PROVED, independently confirmed), so at fixed $t$ the radius of convergence in $z$ is divided by $|\varepsilon|$. The dilation, however,
maps $F_n(t,\cdot)$ to $\lambda^{-n\delta}F_n(t+\log\lambda,\cdot)$ and changes the free multipole constants
$B_{n,j}(0)$ to $\lambda^{-n\delta}B_{n,j}(\log\lambda)$, so for $\lambda\ne1$ it does not preserve the canonical normalization
(at $\delta=2/3$, $f_1=\sin\theta$, the first changed constant is $\lambda^{-4}b_2\log\lambda$ with $b_2$ of
Proposition 14.7, and the density changes from order 7 on). The amplitude scaling and the dilation are therefore
different operations on the logarithmic series.

## 2. Derivation of the recursion

Lemma 2.1 (angular Poisson inverse). For $\rho=r^pf$ and $\psi=r^{p+1}g$, $-\Delta\psi=\partial_x\rho$ is equivalent to
$$-(g''+(p+1)^2g)=p\cos\theta\,f-\sin\theta\,f'.$$
With the Fourier bases above and $P=p+1$,
$$p\cos\theta f-\sin\theta f'=\sum_{j\ge1}\tfrac12[(p-2j+1)a_{j-1}+(p+2j+1)a_j]\sin(2j\theta),$$
and, whenever $4j^2\ne P^2$,
$$b_j=\frac{(p-2j+1)a_{j-1}+(p+2j+1)a_j}{2(4j^2-P^2)}=-\frac{a_{j-1}}{2(2j+P)}+\frac{a_j}{2(2j-P)}. \tag{B}$$

Proof. $\partial_x(r^pf)=r^{p-1}(p\cos\theta f-\sin\theta f')$ and $\Delta(r^Pg)=r^{P-2}(g''+P^2g)$.
$p\cos\theta\sin((2k+1)\theta)=\frac p2[\sin((2k+2)\theta)+\sin(2k\theta)]$ and
$-\sin\theta\,(2k+1)\cos((2k+1)\theta)=-\frac{2k+1}2[\sin((2k+2)\theta)-\sin(2k\theta)]$; collecting $\sin(2j\theta)$ from
$k=j-1$ and $k=j$ gives the displayed forcing (the $k=0$ term gives nothing at frequency $0$). The operator
$-(\partial_\theta^2+P^2)$ acts on $\sin(2j\theta)$ as multiplication by $4j^2-P^2$. The partial fraction form uses
$p-2j+1=-(2j-P)$ and $p+2j+1=2j+P$. $\square$

For $P=P_n=2-n\delta$ the two multipliers are $2j+P_n=2(j+1)-n\delta$ and $2j-P_n=2(j-1)+n\delta\ge n\delta>0$.

Proposition 2.2 (recursion). Inserting the series into (E) and collecting $r^{p_n}$ gives, for $n\ge2$,
$$(n-1)(c-1)f_n=\sum_{i+j=n,\ i,j\ge1}\big[P_i\,g_if_j'-p_j\,g_i'f_j\big], \tag{R}$$
with $g_i$ given by (B) from $f_i$; at $n=1$ the equation is $(c\gamma-1)f_1=0$, so $f_1$ is free.

Proof. $(cr\partial_r-1)(r^pf)=(cp-1)r^pf$ and $cp_n-1=c(1-n\delta)-1=c\delta(1-n)=-(n-1)(c-1)$ because
$c\delta=c-1$. For the quadratic term, with $\psi_i=r^{P_i}g_i$, $\rho_j=r^{p_j}f_j$:
$r^{-1}(\partial_r\psi_i\partial_\theta\rho_j-\partial_\theta\psi_i\partial_r\rho_j)
=r^{P_i+p_j-2}(P_ig_if_j'-p_jg_i'f_j)$ and $P_i+p_j-2=p_i+p_j-1=p_{i+j}$. The sum is over ordered pairs; $i$ is the
velocity index and $j$ the density index. $\square$

These are formulas (3), (4), (5) of the problem, with all signs confirmed. They were also checked by direct substitution of
the reconstructed potential into (E) in exact arithmetic through order 4 and, in an independent implementation,
through order 8 (also Candidate 007's profile through order 5): the residual of the truncated series is $O(r^{p_{N+1}})$ with
coefficient $N(c-1)f_{N+1}$, as predicted.

Support. If the top frequency of $f_1$ is $L$ and $B:=L+1$, induction on (B) and (R) gives
$\deg f_n\le nB-1$ and $\deg g_n\le nB$. Indeed $b_j\ne0$ needs $a_{j-1}\ne0$ or $a_j\ne0$, so $\deg g_n\le\deg f_n+1$,
and the products in (R) have degree at most $iB+jB-1$.

### 2.3 The potential correspondence $C_n\leftrightarrow f_n\leftrightarrow g_n$

For $\chi=r^qC$ with $C=\sum c_m\cos(2m\theta)$: $\Delta\chi=r^{q-2}D$ with $D=\sum D_m\cos(2m\theta)$,
$D_m=(q^2-4m^2)c_m$ (not to be confused with the divisors $d_n$). Then $\rho=-\partial_y(r^{q-2}D)=r^p[-(p+1)\sin\theta D-\cos\theta D']$ with $p=q-3$, which in
coefficients reads, with $x:=-(p+1)/2=(n\delta-2)/2$ at order $n$,
$$a_0=2x\,D_0+(1-x)D_1,\qquad a_m=(m+x)D_m+(m+1-x)D_{m+1}\quad(m\ge1). \tag{P}$$
And $\psi=\chi_{xy}$: $\partial_x\partial_y(r^q\cos2m\theta)=r^{q-2}[B_m\sin(2(m+1)\theta)-A_m\sin(2(m-1)\theta)]$,
$A_m=(q+2m)(q+2m-2)/4$, $B_m=(q-2m)(q-2m-2)/4$.

Proposition 2.3. Let $\delta$ be irrational and $n\ge1$. (i) Given a finite odd sine polynomial $f_n$ there is a unique
finite even cosine polynomial $C_n$ with $-\partial_y\Delta(r^{q_n}C_n)=r^{p_n}f_n$; the stream function
$(r^{q_n}C_n)_{xy}$ equals $r^{P_n}g_n$ with $g_n$ from (B). (ii) The map is injective on smooth S1 homogeneous
potentials of degree $q_n$: no gauge freedom survives.

Proof. In (P), $m+x=m-1+n\delta/2>0$ for $m\ge1$ and $2x=n\delta-2\ne0$; solve downward from the top frequency.
$q_n^2-4m^2=(q_n-2m)(q_n+2m)\ne0$ since $q_n=4-n\delta\notin2\mathbb Z$. So $c_m=D_m/(q_n^2-4m^2)$. The stream
function of the potential solves the same Poisson equation as $r^{P_n}g_n$, whose solution is unique among S1
homogeneous functions of degree $P_n$ because $4j^2\ne P_n^2$. For (ii): if $\partial_y\Delta\chi=0$ with
$\Delta\chi=r^{q-2}D$, then $r^{q-2}D$ is an even function of $x$ alone, homogeneous of degree $q-2\notin\mathbb Z$,
hence a multiple of $|x|^{q-2}$, which is not smooth at $x=0$; so $D=0$, and $\Delta(r^qC)=0$ forces $C=0$ since
$q\ne\pm2m$. $\square$

Exceptional orders (rational $\delta$ only). The potential map is exceptional exactly when $n\delta=2$ ($x=0$, the
$D_0$ equation degenerates; $\chi=r^2\log r$ and $r^2\log r\cos2\theta$ supply the two missing directions) or
$q_n=\pm2m$, i.e. $n\delta\in\{2,4,6,\dots\}$. At $q=2$ the kernel modes are full gauges. At $q=0$ the constant is a
gauge but $\log r$ carries a harmonic stream. At $q=-2m'\le-2$ the harmonic potential $r^{-2m'}\cos(2m\theta)$
($m=m'$) has zero density but a nonzero harmonic stream, i.e. it is a density-free exterior multipole, not a gauge.
None of this occurs for irrational
$\delta$.

## 3. Resonances

Proposition 3.1. A stream resonance occurs at order $n$ and frequency $2j$ iff $n\delta=2(j+1)$, $j\ge1$
($P_n=-2j$; the branch $P_n=2j$ is impossible because $n\delta>0$). The $\sin(2j\theta)$ equation is then
$0\cdot b_{n,j}=\frac12[(p_n-2j+1)a_{n,j-1}+(p_n+2j+1)a_{n,j}]=-2j\,a_{n,j-1}$. Compatibility: $a_{n,j-1}=0$,
the coefficient of $\sin((n\delta-3)\theta)$ in $f_n$. If compatible, $b_{n,j}$ is free: an exterior harmonic stream
multipole $r^{-2j}\sin(2j\theta)$ (zero density). If not, the pure ansatz fails at order $n$ and a term
$\frac{h}{4j}r^{-2j}\log r\,\sin(2j\theta)$ in $\psi$ is required ($h$ the forcing coefficient), after which further
powers of $\log r$ are generated by the nonlinearity.

Resonance is the coincidence of a far-field exponent with an exterior multipole exponent. The harmonic exterior
stream modes are $r^{-2j}\sin(2j\theta)$; $P_n=-2j$ is exactly the resonance.

Rational $\delta=A/B$ in lowest terms. $n\delta\in2\mathbb Z$ iff $n$ is a multiple of $n_0=2B/\gcd(A,2)$, where
$n_0\delta=2A/\gcd(A,2)$. The first stream resonance is at $n_0$ if $A/\gcd(A,2)\ge2$, else at $2n_0$. Examples:
$\delta=4/9$ ($c=9/5$): $n=9$, $j=1$. $\delta=1/2$ ($c=2$): potential exception $n=4$, stream resonance $n=8$.
$\delta=2/5$ ($c=5/3$): potential exception $n=5$, stream resonance $n=10$.
Candidate 007's stored value $c=4076476460239181/2^{51}$ has $\delta=1824676646553933/4076476460239181$ (numerator
$3\cdot883\cdot5737\cdot6133\cdot19577$ and denominator $127\cdot114599\cdot280091797$, both odd and coprime; both factorizations independently confirmed by exact multiplication and primality checks), so the first resonance is at $n=2\cdot4076476460239181=8152952920478362$, $j=A-1$.

Populated modes. The resonant compatibility involves the frequency $2j-1=n\delta-3<n-3$, which lies below the support
bound $nB-1$; such low frequencies are generically populated (confirmed numerically in all computed cases), so the resonance is not
removed by support considerations. For irrational $\delta$ the near-resonant divisor $2(j+1)-n\delta$ is active at
order $n$ only if $a_{n,j-1}\ne0$; the proofs below use only $d_n\le|2(j+1)-n\delta|$ and need no information on which
modes are populated.

Proposition 3.2 (pure-ansatz obstructions, PROVED; computed twice independently in exact
rational arithmetic). For $f_1=a\sin\theta$, $a\ne0$:
at $c=9/5$ the order-9 forcing at $\sin2\theta$ is
$-a^9\cdot37109215993375012065093034946875/443877619295577935692260192337640030208\ne0$;
at $c=2$ the order-8 forcing is $-a^8\cdot126709539517/484849833302016000\ne0$, and already at order 4,
$f_4(\pi/2)=359a^4/401310\ne0$ is not the density of any smooth pure potential $r^2C(\theta)$.
Hence at these $c$ no pure all-order series with $f_1=a\sin\theta$ exists.

Corollary 3.3 (generic profiles). Fix $L\ge1$ and $V_L$ = odd sine polynomials of degree $\le L$. At $c=9/5$ the
compatibility coefficient $\kappa(f_1)=a_{9,0}(f_1)$ is a homogeneous polynomial of degree 9 on $V_L$, not identically
zero (it is nonzero at $\sin\theta$). Its zero set is a proper real algebraic subset (the zero set of a nonzero polynomial); so the pure series fails for
an open dense, full-measure set of $f_1\in V_L$. Same at $c=2$ (degree 8).

Proposition 3.4 (accumulating poles near a rational; PROVED: independent proof, reviewed here and independently
confirmed, with the three constants computed and confirmed by two independent exact programs). Let $f_1=\sin\theta$ and $\delta=\frac25+\varepsilon$ with $0<|\varepsilon|$
small, so that no order $n\le20$ is exactly resonant. The pure coefficients $f_n,g_n$ ($n\le20$) are rational functions of
$\varepsilon$, analytic at $\varepsilon=0$ for $f_n$, $n\le10$, and $g_n$, $n\le9$. Let $R=[\sin\theta]f_{10}$ at $\delta=\frac25$, and let
$\sigma_2,\sigma_3$ be the responses at $\delta=\frac25$ of Section 12.5 (the $\sin((2k-1)\theta)$ coefficient of $f_{5(k+1)}$ per unit
free harmonic $\sin((2k-2)\theta)$ in $g_{5k}$). Then
$$[\sin2\theta]g_{10}=\frac{R}{20}\varepsilon^{-1}+O(1),\qquad[\sin4\theta]g_{15}=\frac{R\sigma_2}{600}\varepsilon^{-2}+O(\varepsilon^{-1}),\qquad
[\sin6\theta]g_{20}=\frac{R\sigma_2\sigma_3}{24000}\varepsilon^{-3}+O(\varepsilon^{-2}),$$
with $R=-8749424340298743474786211/74774522543657493340241516298240\approx-1.170\cdot10^{-7}$,
$\sigma_2=2049177715807847/1331806379780997120\approx1.539\cdot10^{-3}$ and
$\sigma_3=735941710766023529/1020093969974880632832\approx7.214\cdot10^{-4}$, all nonzero. So the stream resonances
at $\delta=\frac25$ are the orders $10,15,20,\dots$ ($n=5k$, $k\ge2$), each near-resonant inverse contributes one factor
$\varepsilon^{-1}$, and the pole orders accumulate; there is no common overall factor $\varepsilon^{-1}$. Nothing is asserted
about the pole orders beyond order 20.

Proof. At $n=5k$ put $j=k-1$; then $P_n=-2j-n\varepsilon$, and the Poisson inverse gives
$[\sin2j\theta]g_n=\frac{(P_n-2j)a_{n,j-1}+(P_n+2j)a_{n,j}}{2(4j^2-P_n^2)}$ with $2(4j^2-P_n^2)=-8jn\varepsilon-2n^2\varepsilon^2$.
If $a_{n,j-1}=A\varepsilon^{-d}+O(\varepsilon^{-d+1})$ and every density coefficient at order $n$ has a pole of order at most $d$,
the resonant stream coefficient is $\frac A{2n}\varepsilon^{-d-1}+O(\varepsilon^{-d})$, since $P_n-2j=-4j+O(\varepsilon)$ and $P_n+2j=-n\varepsilon$;
the nonresonant coordinates keep pole order at most $d$. The first singular stream is $g_{10}$ and the first singular
density $f_{11}$, so a product with two singular factors has order at least $21$, and through order 20 every singular
contribution is linear in one singular factor (the same index count as in Lemma T.1). Hence the $\varepsilon^{-1}$ part of
$f_{11},\dots,f_{15}$ is $\frac R{20}$ times the response to a unit harmonic at order 10, computed from fields of order at most 5
at $\delta=\frac25$, and the obstruction coordinate of $f_{15}$ has leading term $\frac{R\sigma_2}{20}\varepsilon^{-1}$; the inverse at 15 adds
$\frac1{30}\varepsilon^{-1}$. In the same way the $\varepsilon^{-2}$ part of $f_{16},\dots,f_{20}$ is generated by the leading harmonic of $g_{15}$
alone, so the obstruction coordinate of $f_{20}$ has leading term $\frac{R\sigma_2\sigma_3}{600}\varepsilon^{-2}$, and the inverse at 20 adds
$\frac1{40}\varepsilon^{-1}$. The constants were obtained in exact Cartesian Laurent arithmetic, and a separate exact sine and
cosine recurrence evaluated at $\varepsilon=2^{-20},2^{-30},2^{-40}$ matches the three predicted leading terms with relative
discrepancy below $2.7\cdot10^{-10}$ at $2^{-40}$, decreasing by about $2^{10}$ per refinement. $\square$

Proposition 3.5 (the pole hierarchy at every order; PROVED: independent proof, reviewed here line by line and
independently confirmed). Let $Q\ge3$, $\delta=\frac2Q+\varepsilon$, and let $f_1$ be a finite real odd sine polynomial independent of
$\varepsilon$. Put $U(n)=\max(0,\lfloor n/Q\rfloor-1)$ and $V(n)=\max(0,\lfloor(n-1)/Q\rfloor-1)$.
(a) For each $n$ the pure coefficients $f_n,g_n$ are rational functions of $\varepsilon$; every coefficient of $g_n$ has a pole of
order at most $U(n)$ at $\varepsilon=0$, and every coefficient of $f_n$ a pole of order at most $V(n)$.
(b) Let $R=[\sin\theta]f_{2Q}$ at $\delta=\frac2Q$ and, for $k\ge2$, let $\sigma_k$ be the response at $\delta=\frac2Q$ (the
$\sin((2k-1)\theta)$ coefficient of $f_{(k+1)Q}$ per unit free harmonic $\sin((2k-2)\theta)$ in $g_{kQ}$, computed from
$f_1,\dots,f_Q$ and $g_1,\dots,g_{Q-1}$). Then for every $k\ge2$
$$[\sin((2k-2)\theta)]\,g_{kQ}=v_k\varepsilon^{-(k-1)}+O(\varepsilon^{-(k-2)}),\qquad v_k=\frac{R\prod_{j=2}^{k-1}\sigma_j}{(2Q)^{k-1}\,k!},$$
and every other coefficient of $g_{kQ}$ has a pole of order at most $k-2$. So if $R\ne0$ and $\sigma_j\ne0$ for all $j$, the
pole order of $g_{kQ}$ is exactly $k-1$ for every $k\ge2$.
(c) If $R\ne0$, $\sigma_k\ne0$ for every $k\ge2$ and $\sigma_k\to\sigma_\infty\ne0$, then $k|v_k|^{1/k}\to e|\sigma_\infty|/(2Q)$, so
$\sum_kv_kt^k$ is entire.
None of this says anything about the series at a fixed $\varepsilon\ne0$: the neighbourhood of $\varepsilon=0$ on which order $n$ has no
other pole shrinks with $n$.

Proof. (a) The density divisor $\lambda_n=(n-1)\delta/(1-\delta)$ and the factors $P_i,p_j$ are analytic and $\lambda_n\ne0$ at
$\varepsilon=0$. At $\delta=\frac2Q$ a Poisson denominator $2(l-1-P_n)$ or $2(l+1+P_n)$ ($l$ odd) vanishes only if $P_n$ is an even
integer, i.e. $Q\mid n$; at $n=Q$ the only candidate is the absent first term for $l=1$, and at $n=kQ$, $k\ge2$, it is the
single mode $l=2k-3$, with a simple zero in $\varepsilon$. Induct on $n$. A product $g_if_j$ ($i+j=n$) has pole order at most
$U(i)+V(j)$. If both are positive, $U(i)+V(j)=\lfloor i/Q\rfloor+\lfloor(j-1)/Q\rfloor-2\le\lfloor(n-1)/Q\rfloor-2=V(n)-1$; if only
one is positive, it is at most $V(n)$ because $i,j\le n-1$ and $U(i)\le V(i+1)$. Hence $f_n$ has order at most $V(n)$. A
nonresonant inverse keeps it, and $U(n)=V(n)$ unless $Q\mid n$; at $n=kQ$ the simple pole raises the bound to
$V(kQ)+1=k-1=U(kQ)$, in the single mode $2k-2$.
(b) At $n=kQ$ put $j=k-1$; then $P_n+2j=-n\varepsilon$, and the resonant stream coefficient is
$[\sin(2k-3)\theta]f_n/(2n\varepsilon)$ plus a term analytic times the other neighbour, as in the proof of Proposition 3.4. Since
$f_{2Q}$ is analytic, $v_2=R/(4Q)$. Fix $k\ge2$ and $n=kQ+r$, $1\le r\le Q$, where $V(n)=k-1$. By (a) a product of two singular
factors has order at most $k-2$, so the $\varepsilon^{-(k-1)}$ part of $f_n$ comes from products of one factor of order $k-1$ with an
analytic factor at $\varepsilon=0$. A stream factor has order $k-1$ only from index $kQ$ on and a density factor only from
$kQ+1$ on, so the companion has index at most $r\le Q$, and only $f_1,\dots,f_Q$, $g_1,\dots,g_{Q-1}$ at $\delta=\frac2Q$ enter.
The $\varepsilon^{-(k-1)}$ parts of $g_{kQ},f_{kQ+1},g_{kQ+1},\dots,f_{(k+1)Q}$ therefore satisfy exactly the linear response
recursion of the affine block identity at $\delta=\frac2Q$ (Lemma T_Q.1), started from $v_k\sin((2k-2)\theta)$ in $g_{kQ}$ and zero
density at $kQ$ (as $V(kQ)=k-2$), with no resonant inverse in between. So the obstruction coordinate of $f_{(k+1)Q}$ has
leading term $v_k\sigma_k\varepsilon^{-(k-1)}$, and the inverse at $(k+1)Q$ gives $v_{k+1}=v_k\sigma_k/(2(k+1)Q)$. The product
formula follows by induction. (c) The Cesaro mean of $\log|\sigma_j|$ tends to $\log|\sigma_\infty|$, so
$(k!|v_k|)^{1/k}\to|\sigma_\infty|/(2Q)$, and Stirling's formula gives the limit. $\square$

For $f_1=\sin\theta$ and $Q=5$ this reproduces the constants $\frac R{20}$, $\frac{R\sigma_2}{600}$, $\frac{R\sigma_2\sigma_3}{24000}$ of
Proposition 3.4. For this example $R\ne0$ (Proposition 3.4) and every response is nonzero (PROVED: independent exact certificate): for $k\ge4$,
$\sigma_k$ is a rational function of $k$ of degree 17, generated twice independently with identical results; its values at
$k=2,\dots,12$ (with $k=2,3$ from their separate exact responses) are nonzero, and after $k=11+t$ every numerator coefficient
is negative and every denominator coefficient positive; the limit is $\sigma_\infty=-3575370901/2725632000000$. So, by
Proposition 3.5, the pole order of $g_{5k}$ at $\delta=\frac25$ is exactly $k-1$ for every $k\ge2$, and
$k|v_k|^{1/k}\to e|\sigma_\infty|/10\approx3.57\cdot10^{-4}$ (PROVED; the limit of $(k!|v_k|)^{1/k}$ is
$|\sigma_\infty|/10=3575370901/27256320000000$).

## 4. Norms and elementary lemmas

$\|h\|_\sigma=\sum_k|\hat h(k)|e^{\sigma|k|}$ ($\sigma\ge0$), which for $f=\sum a_k\sin((2k+1)\theta)$ is
$\sum|a_k|e^{\sigma(2k+1)}$; $\alpha_n:=\|f_n\|_0$. $\|h\|_{L^\infty}\le\|h\|_0$.

Lemma 4.1 (algebra). $\|uv\|_\sigma\le\|u\|_\sigma\|v\|_\sigma$; for products of a sine series and a cosine series
(as in (R)) the result is a sine series with the same bound. ($\sin A\cos B=\frac12[\sin(A+B)+\sin(A-B)]$ and
$e^{\sigma|A\pm B|}\le e^{\sigma|A|}e^{\sigma|B|}$.)

Lemma 4.2 (Poisson multipliers). Let $n\ge1$ with $d_n>0$ and $\lambda_\delta:=\frac32+\frac\delta2+\frac1\delta$. Then
$$\|g_n\|_\sigma\le e^\sigma\Big(\frac1{2d_n}+\frac1{2n\delta}\Big)\|f_n\|_\sigma,\qquad
|P_n|\,\|g_n\|_\sigma\le e^\sigma\lambda_\delta\frac n{d_n}\|f_n\|_\sigma,\qquad
\|g_n'\|_\sigma\le e^\sigma\lambda_\delta\frac n{d_n}\|f_n\|_\sigma .$$

Proof. In (B) the $a_{j-1}$ term moves frequency $2j-1$ to $2j$ (weight factor $e^\sigma$) with multiplier
$1/(2|2(j+1)-n\delta|)\le1/(2d_n)$, since $2(j+1)$ is an even integer. The $a_j$ term moves $2j+1$ to $2j$ (factor
$\le1$) with multiplier $1/(2(2j-2+n\delta))\le1/(2n\delta)$. This gives the first bound. For the second, $|P_n|\le2+n\delta\le n(2+\delta)$,
so $|P_n|(\frac1{2d_n}+\frac1{2n\delta})\le\frac n{d_n}(1+\frac\delta2)+\frac1{n\delta}+\frac12
\le\frac n{d_n}(\frac32+\frac\delta2+\frac1\delta)$, using $d_n\le1\le n$. For the third, the derivative multiplies
$b_j$ by $2j$. If $2(j+1)\ge2n\delta$ then $|2(j+1)-n\delta|\ge j+1$ and $2j/|2(j+1)-n\delta|<2\le2/d_n$; otherwise
$2j<2n\delta$ and the ratio is $<2n\delta/d_n$. So $2j/|2(j+1)-n\delta|\le2n/d_n$. Also
$2j/(2j-2+n\delta)\le\max(1,2/(n\delta))$. Hence
$\|g_n'\|_\sigma\le e^\sigma[\frac n{d_n}+\frac12+\frac1{n\delta}]\|f_n\|_\sigma\le e^\sigma\frac n{d_n}(\frac32+\frac1\delta)\|f_n\|_\sigma$. $\square$

The stream inverse therefore gains one full angular derivative relative to the forcing (no loss of regularity), at the
price of the factor $n/d_n$.

## 5. The majorant inequality and the Siegel form

Proposition 5.1. Let $\delta$ be irrational, $f_1$ a finite odd sine polynomial with top frequency $L$, $B=L+1$. Then for
$n\ge2$
$$(n-1)(c-1)\,\alpha_n\le\lambda_\delta(B+1)\sum_{i+j=n}\frac{ij}{d_i}\alpha_i\alpha_j .$$

Proof. By Lemma 4.1, $\|P_ig_if_j'\|_0\le|P_i|\|g_i\|_0\|f_j'\|_0$ and $\|p_jg_i'f_j\|_0\le|p_j|\|g_i'\|_0\alpha_j$.
$\|f_j'\|_0\le\deg(f_j)\,\alpha_j\le(jB-1)\alpha_j$. $|p_j|=|1-j\delta|\le\max(1,j\delta-1)$, so
$(jB-1)+|p_j|\le j(B+\delta)\le j(B+1)$. Insert Lemma 4.2 ($\sigma=0$). $\square$

Set $x_n=n\alpha_n$ and $y_n=x_n/d_n$. Since $n/(n-1)\le2$ and $d_j\le1$,
$$y_n\le\frac K{d_n}\sum_{i+j=n}y_iy_j\quad(n\ge2),\qquad K:=\frac{2\lambda_\delta(B+1)}{c-1},\qquad
y_1=\frac{\alpha_1}{\delta}. \tag{S}$$
(Indeed $x_n\le K\sum(x_i/d_i)x_j=K\sum y_i\,d_jy_j\le K\sum y_iy_j$.) This has the same tree-majorant structure as
Siegel's linearization problem, with divisors $d_n=2\|n\alpha\|$; for $\lambda=e^{2\pi i\alpha}$ one has
$2d_n\le|\lambda^n-1|\le\pi d_n$, so the divisors are comparable to the rotation divisors (the indexing of the
standard conjugacy equation differs by one, which is immaterial here).

## 6. Tree expansion, counting lemma, coefficient bound

Let $Y_1=y_1$ and $Y_n=\frac K{d_n}\sum_{i+j=n}Y_iY_j$. By induction $y_n\le Y_n$. Expanding,
$$Y_n=K^{n-1}y_1^n\sum_{T\in\mathcal T_n}\prod_{v\in\mathrm{int}(T)}\frac1{d_{n_v}},$$
where $\mathcal T_n$ is the set of plane full binary trees with $n$ leaves, $\mathrm{int}(T)$ its $n-1$ internal nodes,
and $n_v$ the number of leaves below $v$ (so $n_{\rm root}=n$, and $n_v=n_{v'}+n_{v''}$ for the two children).
$|\mathcal T_n|$ is the Catalan number $C_{n-1}\le4^{n-1}$.

Lemma 6.1 (arithmetic). Let $\alpha\in(0,\frac12)$ be irrational with convergent denominators $q_k$ and
$S_k:=\{m\ge1:\|m\alpha\|<1/(4q_k)\}$. Then $S_{k+1}\subset S_k$, every $m\in S_k$ satisfies $m\ge q_k$, and distinct
$m,m'\in S_k$ satisfy $|m-m'|\ge q_k$.

Proof. Nesting: $q_k$ is nondecreasing. Best approximation: for $1\le l<q_k$, $\|l\alpha\|\ge\|q_{k-1}\alpha\|>
1/(q_{k-1}+q_k)\ge1/(2q_k)$. If $m\in S_k$ then $\|m\alpha\|<1/(4q_k)$, so $m\ge q_k$. If $m\ne m'$ are in $S_k$ then
$\|(m-m')\alpha\|<1/(2q_k)$, so $|m-m'|\ge q_k$. ($k=0$: $q_0=1$, trivial.) $\square$

Lemma 6.2 (counting). For $T\in\mathcal T_n$ and $k\ge0$, the number $N_k(T)$ of internal nodes $v$ with $n_v\in S_k$
satisfies $N_k(T)\le2n/q_k$, and $N_k(T)=0$ if $q_k>n$.

Proof. Call such nodes marked. For a marked $v$ let $e_v$ be the number of leaves below $v$ that are not below any
marked proper descendant of $v$. Every leaf is counted in at most one $e_v$ (its lowest marked ancestor), so
$\sum e_v\le n$. Consider the forest $F$ of marked nodes ordered by ancestry. If $v$ has no marked descendant,
$e_v=n_v\ge q_k$ (Lemma 6.1). If $v$ has exactly one maximal marked descendant $w$, then $e_v=n_v-n_w$, with
$n_v>n_w$ both in $S_k$, so $e_v\ge q_k$. Let $\ell$, $u$, $b$ be the numbers of marked nodes with zero, one, at least two
children in $F$. Then $q_k(\ell+u)\le n$ and $b\le\ell$ (a rooted forest has fewer branching nodes than leaves), so
$N_k=\ell+u+b\le2(\ell+u)\le2n/q_k$. The last claim follows from $n_v\le n$ and $\min S_k\ge q_k$. $\square$

Lemma 6.3 (product). For irrational $\alpha=\delta/2\in(0,\frac12)$ and every $T\in\mathcal T_n$,
$$\prod_{v\in\mathrm{int}(T)}\frac1{d_{n_v}}\le2^{n-1}\exp\big(2n\,\mathcal B(\alpha)\big).$$

Proof. $d_m=2\|m\alpha\|$. If $m\notin S_0$ then $\|m\alpha\|\ge1/4$ and $1/d_m\le2$. If $m\in S_k\setminus S_{k+1}$
then $\|m\alpha\|\ge1/(4q_{k+1})$ and $1/d_m\le2q_{k+1}$. Every $m$ lies in finitely many $S_k$ ($\|m\alpha\|>0$).
Hence $\log\prod_v(1/d_{n_v})\le(n-1)\log2+\sum_kN_k(T)\log q_{k+1}\le(n-1)\log2+2n\sum_k\log(q_{k+1})/q_k$. $\square$

Theorem 6.4 (coefficient bound). Let $\delta\in(0,1)$ with $\alpha=\delta/2$ Brjuno, $c=1/(1-\delta)$, and $f_1\ne0$ an odd
sine polynomial of top frequency $L$, $B=L+1$. Then (R) defines $f_n$ for all $n$ and
$$\alpha_n\le\frac{d_n}{n}y_n\le\frac{A^n}{8Kn},\qquad A:=8K\,e^{2\mathcal B(\alpha)}\frac{\alpha_1}{\delta},\qquad
K=\frac{2\lambda_\delta(B+1)}{c-1}.$$
Moreover $\alpha_n/d_n\le A^n/(8Kn)$, $\|g_n\|_0\le\frac{1+\delta^{-1}}2\frac{A^n}{8Kn}$ and
$\|g_n'\|_0\le\lambda_\delta\frac{A^n}{8K}$.

Proof. $y_n\le Y_n\le K^{n-1}y_1^n\,4^{n-1}\,2^{n-1}e^{2n\mathcal B}=(8K)^{-1}(8Ke^{2\mathcal B}y_1)^n$ by Lemma 6.3.
Then $\alpha_n=d_ny_n/n$. The $g$ bounds follow from Lemma 4.2. $\square$

Remark (Diophantine special case). If $\|m\alpha\|\ge\kappa/m$ for all $m$ (bounded type, e.g. $\delta=1/\sqrt5$), the
same proof works with $\mathcal B(\alpha)$ finite; no separate argument is needed.

## 7. Theorem A: convergent exterior solutions

Theorem A (PROVED; independently confirmed). Let $\alpha=\delta/2$ be a Brjuno number, $c=1/(1-\delta)$, and $f_1\ne0$ an odd sine
polynomial with top frequency $L$. Let $A$ be as in Theorem 6.4 and $R_0=A^{1/\delta}$. Then:

1. $r^{-\gamma}\rho=\sum_{n\ge1}z^{n-1}f_n$ converges absolutely in $\mathcal A_\sigma$ for $|z|e^{\sigma B}<1/A$; in
   particular $\sup_{r\ge R}\sup_\theta r^{-\gamma}|\sum_{n\ge N}r^{p_n}f_n(\theta)|\le\sum_{n\ge N}\frac{A}{8Kn}(AR^{-\delta})^{n-1}\to0$
   for every $R>R_0$. The map $z\mapsto r^{-\gamma}\rho$ is analytic from $|z|<1/A$ into $\mathcal A_0$, and into
   $\mathcal A_\sigma$ on $|z|<e^{-\sigma B}/A$.
2. The stream and potential series $r^{-\gamma-1}\psi=\sum z^{n-1}g_n$ and $r^{-\gamma-3}\chi=\sum z^{n-1}C_n$ converge in the
   same sense, with $\|C_n\|_0\le C_\chi\,\alpha_n/d_n$ for a constant $C_\chi$ depending only on $\delta,L$ (Lemma 7.1).
3. For every multi-index $\beta$ with $|\beta|=m$ and every $R>R_0$,
   $\sum_n\sup_{r\ge R}r^{m-\gamma}|D^\beta(r^{p_n}f_n)|$, $\sum_n\sup_{r\ge R}r^{m-\gamma-1}|D^\beta(r^{P_n}g_n)|$ and
   $\sum_n\sup_{r\ge R}r^{m-\gamma-3}|D^\beta(r^{q_n}C_n)|$ converge. Thus all derivatives converge uniformly on $r\ge R$
   with these weights.
4. The sums $\rho,\psi,\chi$ are real-analytic on $r>R_0$ and satisfy $\psi=\chi_{xy}$, $\rho=-\partial_y\Delta\chi$,
   $u=(-\chi_{xyy},\chi_{xxy})=(-\psi_y,\psi_x)$, $-\Delta\psi=\partial_x\rho$ and $(cX+u)\cdot\nabla\rho-\rho=0$ there.
   $\rho\not\equiv0$ and $\rho=r^\gamma f_1+O(r^{\gamma-\delta})$.

Proof. (1) $\|f_n\|_\sigma\le e^{\sigma(nB-1)}\alpha_n$ by the support bound, then Theorem 6.4. The tail estimate uses
$r^{p_n}=r^\gamma z^{n-1}$ and $z\le R^{-\delta}<1/A$. (2) Theorem 6.4 for $g_n$; Lemma 7.1 for $C_n$.
(3) For $h$ a trigonometric polynomial of degree $\le J$ and real $s$,
$\partial_x(r^sh)=r^{s-1}(s\cos\theta\,h-\sin\theta\,h')$, $\partial_y(r^sh)=r^{s-1}(s\sin\theta\,h+\cos\theta\,h')$, and the
new angular factor has degree $\le J+1$ and $\|\cdot\|_0\le(|s|+J)\|h\|_0$. Iterating, $D^\beta(r^sh)=r^{s-m}h_\beta$;
with $a=|s|+J$, the $(\ell+1)$-st derivative costs at most $|s-\ell|+J+\ell\le a+2\ell$, so by the arithmetic-geometric
mean inequality $\|h_\beta\|_0\le\prod_{\ell=0}^{m-1}(a+2\ell)\|h\|_0\le(a+m-1)^m\|h\|_0\le(|s|+J+m)^m\|h\|_0$. For the density, $|p_n|\le1+n$ and $J=nB-1$, so the factor is at most
$((B+1)n+m+1)^m$, a polynomial in $n$; likewise for $\psi$ ($|P_n|\le2+n$, $J=nB$) and $\chi$ ($|q_n|\le4+n$,
$J\le nB$). Since $\sum_n n^{m}(AR^{-\delta})^n<\infty$, (3) follows. (4) By (3) the series converge in $C^k$ on
$\{r\ge R\}$ for every $k$; termwise identities $\psi_n=(\chi_n)_{xy}$, $\rho_n=-\partial_y\Delta\chi_n$ (Proposition 2.3)
pass to the limit. In the stationary equation the linear part is $\sum_n(cp_n-1)r^{p_n}f_n$ and the quadratic part is the
double series $\sum_{i,j}u_i\cdot\nabla\rho_j=\sum_{i,j}r^{p_{i+j}}(P_ig_if_j'-p_jg_i'f_j)$, which converges absolutely
(bounded by $r^{2\gamma-1}\sum_{i,j}\mathrm{poly}(i,j)(AR^{-\delta})^{i+j-2}$). Regrouping by $n=i+j$ and using (R), the
coefficient of every $r^{p_n}$ vanishes; hence the equation holds. Real-analyticity: by (1), $r^{-\gamma}\rho$ is a
convergent series in $z=r^{-\delta}$ and in $e^{\pm i\theta}$ on a complex neighbourhood of every point of $r>R_0$, and
$z$, $e^{i\theta}$ are real-analytic functions of $(x,y)\ne0$. $\square$

Lemma 7.1 (potential bound). For irrational $\delta$ and $n$ with $n\delta\ge3$,
$\|C_n\|_0\le(3/|4-n\delta|+1)\,\alpha_n/d_n$. For the finitely many $n<3/\delta$ the map $f_n\mapsto C_n$ is an invertible
finite triangular matrix on degrees $\le nB-1$; let $T_*$ be the maximum of $d_n\cdot$(its $\ell^1$ norm) over these $n$.
Then $C_\chi:=\max(T_*,\max_{n\ge3/\delta}(3/|4-n\delta|+1))<\infty$.

Proof. For $n\delta\ge3$, $x=(n\delta-2)/2\ge\frac12$ and $|m+1-x|\le m+x$ for $m\ge1$, so solving (P) downward,
$|D_m|\le|a_m|/(m+x)+|D_{m+1}|$, hence $|D_m|\le\sum_{k\ge m}|a_k|/(k+x)\le\alpha_n/(m+x)$ for $m\ge1$, and $|D_0|\le(|a_0|+|1-x||D_1|)/(2x)\le3\alpha_n$.
For $m\ge1$, $|q_n^2-4m^2|=|q_n-2m||q_n+2m|$; both factors are distances from $n\delta$ to even integers, hence
$\ge d_n$, and the larger is $\ge2m$; so $|q_n^2-4m^2|\ge2md_n$. For $m=0$, $q_n^2\ge d_n|4-n\delta|$. Summing,
$\|C_n\|_0\le\frac{\alpha_n}{d_n}(\frac3{|4-n\delta|}+\sum_{m\ge1}\frac1{2m(m+\frac12)})\le\frac{\alpha_n}{d_n}(\frac3{|4-n\delta|}+1)$.
Only finitely many $n$ have $|4-n\delta|<1$, and for those $|4-n\delta|\ge d_n>0$. $\square$

### 7.2 Theorem A' (analytic leading profiles)

Theorem A' (PROVED; independently confirmed). Let $\alpha=\delta/2$ be Brjuno and $f_1\ne0$ an odd-harmonic sine series with
$\|f_1\|_{\sigma_0}<\infty$ for some $\sigma_0>0$. Put $K'=2e^{\sigma_0}(1+\sigma_0)\lambda_\delta/(c-1)$ and
$A'=8K'e^{2\mathcal B(\alpha)}\|f_1\|_{\sigma_0}/\delta$. Then for all $n\ge1$ and $0\le\sigma<\sigma_0$
$$\|f_n\|_\sigma\le\frac{A'^n}{8K'n\,(\sigma_0-\sigma)^{n-1}} .$$
Consequently $\sum z^{n-1}f_n$ converges in $\mathcal A_\sigma$ for $|z|<(\sigma_0-\sigma)/A'$, and conclusions 1 to 4 of
Theorem A hold on $r>R_0'=(A'/\sigma_0)^{1/\delta}$ (derivatives: each $\theta$-derivative costs a factor
$C/(\sigma_0-\sigma)$ by the Cauchy estimate in a slightly smaller strip; the potential series by the potential
reconstruction below).

Potential reconstruction for Theorem A'. For $n\delta\ge3$ the proof of Lemma 7.1 works in weighted norms:
$e^{2m\sigma}|D_m|\le\sum_{k\ge m}|a_k|e^{(2k+1)\sigma}/(k+x)\le\|f_n\|_\sigma/(m+x)$, so
$\|C_n\|_\sigma\le(3/|4-n\delta|+1)\|f_n\|_\sigma/d_n$. For the finitely many orders with $n\delta<3$ (so $-1<x<\frac12$)
the downward solution of (P) is, for $m\ge1$,
$D_m=\sum_{k\ge m}(-1)^{k-m}\frac{a_k}{k+x}\prod_{l=m}^{k-1}\frac{l+1-x}{l+x}$, and $D_0=(a_0-(1-x)D_1)/(2x)$ is
recovered separately ($x\ne0$ for irrational $\delta$). Separating the factor $l=1$ and using
$\log\frac{l+1-x}{l+x}\le\frac{1-2x}{l+x}\le\frac3{l-1}$ for $l\ge2$ gives $|\prod_{l=m}^{k-1}\cdots|\le C_xk^3$ with a
finite constant $C_x$ depending on $x$. (The constant is needed: at $n=1$, $\delta=1/\sqrt5$, $m=1$, $k=2$ the product is
$6\sqrt5-1\approx12.42>2^3$.) The polynomial factor is absorbed by
$\sup_k(k+1)^ae^{-(\sigma'-\sigma)(2k+1)}<\infty$ for $\sigma<\sigma'$, so $C_n$ is analytic in every smaller strip; since
these orders are finitely many, they do not change the radius. For a given $R>R_0'$ choose the strip width so that
$A'R^{-\delta}<\sigma_0-\sigma$ and reserve a further strip gap for derivatives and for the finitely many exceptional
potential orders.

Proof. Let $\nu_n=\sup_{0\le\sigma<\sigma_0}(\sigma_0-\sigma)^{n-1}\|f_n\|_\sigma$. Nagumo's lemma for Wiener norms: if
$\|h\|_{\sigma'}\le\nu(\sigma_0-\sigma')^{-k}$ for all $\sigma'<\sigma_0$, then $\|h'\|_\sigma\le(k+1)\nu(\sigma_0-\sigma)^{-k-1}$.
(For $k\ge1$ use $|m|e^{-\epsilon|m|}\le1/(e\epsilon)$ with $\epsilon=\sigma'-\sigma=(\sigma_0-\sigma)/(k+1)$ and
$(1+1/k)^k\le e$. For $k=0$ the same choice reaches the boundary $\sigma'=\sigma_0$; letting $\sigma'\uparrow\sigma_0$ gives
$\|h'\|_\sigma\le\nu/(e(\sigma_0-\sigma))\le\nu/(\sigma_0-\sigma)$.) Hence $\|f_j'\|_\sigma\le j\nu_j(\sigma_0-\sigma)^{-j}$. With Lemma 4.2 and $|p_j|\le j$,
$$\|P_ig_if_j'\|_\sigma+\|p_jg_i'f_j\|_\sigma\le e^{\sigma_0}\lambda_\delta\frac{ij}{d_i}\nu_i\nu_j
\frac{1+(\sigma_0-\sigma)}{(\sigma_0-\sigma)^{n-1}} ,$$
so $(n-1)(c-1)\nu_n\le e^{\sigma_0}(1+\sigma_0)\lambda_\delta\sum_{i+j=n}(ij/d_i)\nu_i\nu_j$, and $\nu_1=\|f_1\|_{\sigma_0}$.
This is Proposition 5.1 with $B+1$ replaced by $e^{\sigma_0}(1+\sigma_0)$; Sections 5 and 6 apply verbatim. $\square$

So no special profile is needed: every nonzero real-analytic odd profile works. The family of admissible $f_1$ is
open (indeed all of $\mathcal A_{\sigma_0}\setminus\{0\}$), with radius controlled by $\|f_1\|_{\sigma_0}$.

### 7.3 Theorem D (Diophantine parameters, fully explicit certificate)

This is an independent proof of the Diophantine case with a different packing argument and constants that are
certified by exact rational inequalities. It was written and audited independently of Theorem A.

Theorem D (PROVED; independently confirmed). Let $c>1$, $\delta=1-1/c$, and suppose $|m-n\delta|\ge\kappa n^{-\tau}$ for
all $n\ge1$, $m\in\mathbb Z$, with $\kappa>0$, $\tau\ge1$. Let $f_1\ne0$ be a real odd-harmonic sine polynomial with top
frequency $L$, $B=L+1$, $\sigma\ge0$, $F=\|f_1\|_\sigma$, and
$$\Lambda_\sigma=e^\sigma(2+\delta^{-1}),\quad K_0=\frac{2\Lambda_\sigma(B+1)}{c-1},\quad Q=\frac{(2e)^\tau}{\kappa},\quad
M=\frac{QF}{\delta},\quad A=4K_0M .$$
(These $K_0$, $Q$, $M$, $A$ are local to Theorem D and Appendix A; they differ from the $K$, $A$ of Theorem A.)
Then $\|f_n\|_\sigma\le MA^{n-1}$ for all $n\ge1$, and for every $R>A^{1/\delta}$ the density, stream and potential
series and every fixed weighted Cartesian derivative series converge uniformly on $r\ge R$; the sums solve the
stationary potential equation on $r>R$ and give a nonzero smooth exterior S1 solution.

Proof outline (complete proof in Appendix A). (i) Multipliers: with $k=2j$, $|k+P_n|\ge d_n$, $k-P_n\ge n\delta$, $|P_n|\le2n$, one gets
$\max(\|g_n'\|_\sigma,|P_n|\|g_n\|_\sigma)\le\Lambda_\sigma(n/d_n)\|f_n\|_\sigma$. (ii) With $Y_n=n\|f_n\|_\sigma/d_n$:
$Y_n\le(K_0/d_n)\sum_{i+j=n}Y_iY_j$, $Y_1=F/\delta$. (iii) Leaf-charge packing: in a binary tree with $N$ leaves mark
the internal vertices whose subtree size $s$ has $d_s<\varepsilon$; then every mark has at least
$q=(\kappa/\varepsilon)^{1/\tau}$ leaves below it, comparable marks of sizes $m>l$ satisfy $d_{m-l}\le d_m+d_l<2\varepsilon$,
hence $m-l>q/2$, and charging disjoint leaf sets to terminal and unary marks gives at most $2N(\varepsilon/\kappa)^{1/\tau}$
marks. (iv) Layer cake: $\log\prod_vd_{s(v)}^{-1}=\int_0^\infty\#\{v:d_{s(v)}<e^{-t}\}dt\le N\log((2e)^\tau/\kappa)$. With
the Catalan count $4^{n-1}$ this gives $Y_n\le K_0^{n-1}Y_1^n4^{n-1}Q^n$ and the bound. (v) Potential and derivatives:
$\|C_n\|_\sigma\le C_*n^{\tau-1}\|f_n\|_\sigma$ (a direct estimate of (P) at the orders $n\delta\ge8$, with $C_*$ also covering the
finitely many earlier orders; Appendix A.6 uses instead the weaker bound $\|C_n\|_0\le C_\chi\kappa^{-1}n^\tau\|f_n\|_\sigma$ from
Lemma 7.1, which also suffices), $\|g_n\|_\sigma\le K_\sigma n^\tau\|f_n\|_\sigma$, and each Cartesian derivative
costs a polynomial factor in $n$. $\square$

Explicit example (PROVED). $\delta=1/\sqrt5$, $c=(5+\sqrt5)/4$, $\tau=1$, $\kappa=1/(5+2\sqrt5)$ (from $5m^2-n^2\ne0$),
$f_1=\sin\theta$, $\sigma=\frac12\log2$: $M=10\sqrt2\,e(2+\sqrt5)<256$, $A=480e(11+5\sqrt5)<2^{15}$. With $R=2^{36}$,
$R^\delta>2^{16}$ and
$$\sup_{r\ge R}\Big\|r^{-\gamma}\rho-\sum_{n=1}^Nr^{-\delta(n-1)}f_n\Big\|_{\frac12\log2}\le512\cdot2^{-N}\qquad(N\ge1).$$
For the exact leading polynomial extracted from Candidate 007 (top frequency 19, $T=\sum_{k=0}^92^k|a_{2k+1}|<31$) at the
same $\delta=1/\sqrt5$: $M<2^{13}$, $A<2^{23}$, $R=2^{54}$, tail $\le2^{14}\cdot2^{-N}$.

A further variant (complete independent proof, not reviewed here; stated for reference, not used and not counted as PROVED) replaces the Diophantine
hypothesis by the integral condition $\int_0^\infty\min(1,2/q(2e^{-t}))\,dt<\infty$, $q(\varepsilon)=\min\{n:d_n<\varepsilon\}$,
using the same leaf charges; its precise relation to the Brjuno condition is not analysed here, and it is not needed
for the results below.

### 7.4 The solutions do not terminate (PROVED; independent proof, audited and independently confirmed)

Proposition 7.4. Let $S,Q\subset\mathbb R$ be finite sets of distinct exponents with $S\ne\varnothing$ and $\min S<1$, and let
$$\rho=\sum_{s\in S}r^sF_s(\log r,\theta),\qquad\psi=\sum_{q\in Q}r^qG_q(\log r,\theta),$$
where every $F_s$, $G_q$ is a nonzero polynomial in $\log r$ whose angular coefficients are real-analytic, those of $F_s$
odd in $\theta$ and even about $\pi/2$, those of $G_q$ odd in $\theta$ and odd about $\pi/2$. Then $(\rho,\psi)$ cannot
satisfy $-\Delta\psi=\partial_x\rho$ and $cr\partial_r\rho-\rho+r^{-1}(\psi_r\rho_\theta-\psi_\theta\rho_r)=0$ on an exterior
domain. In particular the solutions of Theorems A and A' are nonterminating series: no finite truncation, and no
finite sum with additional multipoles, logarithms or other real exponents, is an exact solution.

Proof. Lemma: if $f\ne0$ has the density symmetries, $g\ne0$ the stream symmetries, both analytic, and $(a,b)\ne(0,0)$,
then $agf'-bg'f\not\equiv0$. Indeed, at $\theta=0$ the vanishing orders $s,t$ of $f,g$ are odd and the leading Taylor
coefficient of $agf'-bg'f$ is a nonzero multiple of $as-bt$; at $\theta=\pi/2$ the orders $s'$ (even, possibly $0$) and
$t'$ (odd) give $as'-bt'$. If the identity held: $as=bt$, so $a=0$ iff $b=0$, hence both are nonzero; $s'=0$ is impossible
because then $-bg'f$ alone has the lowest order there; and $s'>0$ gives $ts'=t's$ with an even left and an odd right side.
Now let $s_*=\min S$ and let $f$ be the top $\log r$-coefficient of $F_{s_*}$. The top coefficient of
$\partial_x(r^{s_*}F_{s_*})$ is $r^{s_*-1}(s_*\cos\theta f-\sin\theta f')$, which is nonzero (its leading Taylor coefficient at
$0$ is a multiple of $s_*-v$, $v\ge1$ the order of $f$). So the Poisson equation needs a stream exponent $s_*+1$, and
$q_*=\min Q\le s_*+1$. The least exponent of the nonlinear term is $q_*+s_*-2\le2s_*-1<s_*$; it is produced only by the
pair $(q_*,s_*)$ and by no linear term, so its coefficient vanishes. Its top $\log r$-coefficient is $q_*gf'-s_*g'f$, with $g$
the top coefficient of $G_{q_*}$ (radial derivatives of the polynomial part lower the degree); by the Lemma this forces
$q_*=s_*=0$. Then no density exponent equals $-1$, so $G_0$ is harmonic: its top coefficient satisfies $g''=0$, and a
periodic odd $g$ with $g''=0$ vanishes. Contradiction. $\square$

### 7.5 A sharper constant from the continued-fraction errors (PROVED: independent proof, reviewed here and independently confirmed)

Theorem A$_E$. Let $\delta\in(0,1)$ be irrational, $\alpha=\delta/2=[0;a_1,a_2,\dots]$ with convergents $p_k/q_k$
($p_0=0$, $q_0=1$), $e_k=|q_k\alpha-p_k|$ (so $e_0=\alpha$), and
$$E(\alpha)=\sum_{k\ge1}\frac{\log(e_{k-1}/e_k)}{q_k}.$$
$E(\alpha)<\infty$ if and only if $\mathcal B(\alpha)<\infty$. If it is finite, then for every nonzero odd sine
polynomial $f_1$ with top frequency $L$ and $\ell^1$ norm $F$, with $K$ as in Theorem 6.4,
$$\frac{n\|f_n\|_{\ell^1}}{d_n}\le\frac\alpha{4K}A_E^n,\qquad A_E=\frac{4KF}{\alpha\delta}e^{2E(\alpha)}=\frac{8KF}{\delta^2}e^{2E(\alpha)},$$
and all conclusions of Theorem A hold on $r>A_E^{1/\delta}$. So the radius bound of Theorem A may be taken as
$\min(A,A_E)^{1/\delta}$.

Proof. (i) Best approximation: for $k\ge1$ and $0<m<q_k$, $\|m\alpha\|\ge e_{k-1}$. (Write $(l,m)=a(p_{k-1},q_{k-1})+
b(p_k,q_k)$ with integers $a,b$, possible since the determinant is $\pm1$; $0<m<q_k$ excludes $a=0$ and $a,b$ nonzero of
equal sign; in the remaining cases $b=0$ or $a,b$ have opposite signs, and since $q_{k-1}\alpha-p_{k-1}$ and
$q_k\alpha-p_k$ have opposite signs the two contributions to $m\alpha-l$ have equal sign, so $|m\alpha-l|\ge|a|e_{k-1}
\ge e_{k-1}$.) (ii) Let $S_k=\{m\ge1:\|m\alpha\|<e_{k-1}/2\}$, $k\ge1$. By (i) every element of $S_k$ is $\ge q_k$ and
distinct elements differ by $\ge q_k$; the sets decrease in $k$. If $m$ lies in exactly $S_1,\dots,S_h$ ($h\ge0$), then
$d_m=2\|m\alpha\|\ge e_h$, so $\log(1/d_m)\le\log(1/\alpha)+\sum_{k:m\in S_k}\log(e_{k-1}/e_k)$, all terms nonnegative.
(iii) The counting of Lemma 6.2 uses only these two properties of $S_k$, so a plane full binary tree with $n$ leaves has
at most $2n/q_k$ internal nodes with $n_v\in S_k$. Summing (ii) over the $n-1$ internal nodes gives
$\prod_v d_{n_v}^{-1}\le\alpha^{-(n-1)}e^{2nE}$, which replaces Lemma 6.3. With (S) and $C_{n-1}\le4^{n-1}$ trees,
$y_n\le(4K/\alpha)^{n-1}y_1^ne^{2nE}=\frac\alpha{4K}A_E^n$ ($y_1=F/\delta$; for $n=1$ the right side is $e^{2E}y_1$). The
stream, potential and derivative bounds of Theorems A and A' depend on the coefficient bound only through
$\|f_n\|/d_n$ and a geometric rate, so they carry over with $A$ replaced by $A_E$. (iv) Equivalence: from
$q_{k+1}\alpha-p_{k+1}=a_{k+1}(q_k\alpha-p_k)+(q_{k-1}\alpha-p_{k-1})$ and the alternating signs,
$e_{k-1}=a_{k+1}e_k+e_{k+1}$, so $e_{k-1}/e_k\in(a_{k+1},a_{k+1}+1)$; also $q_{k+1}/q_k\in[a_{k+1},a_{k+1}+1)$.
The logarithms differ by at most $\log2$ and $\sum1/q_k<\infty$ ($q_{k+2}\ge2q_k$), so $E<\infty$ if and only if
$\sum_k\log(q_{k+1}/q_k)/q_k<\infty$, which differs from $\mathcal B$ by the convergent $\sum\log q_k/q_k$. Tail: if
$a_{k+1}\le M$ for $k\ge N$ then $\sum_{k\ge N}\log(e_{k-1}/e_k)/q_k\le4\log(M+1)/q_N$. $\square$

$E$ charges the logarithm of the ratio $e_{k-1}/e_k\approx a_{k+1}$ at each level instead of $\log q_{k+1}$; the price
is $1/\alpha$ instead of $2$ per internal node. For bounded type this is a large gain.

Values. At $\delta=1/\sqrt5$, $\alpha=[0;4,\overline{2,8}]$: $E<0.449555117500$ (against $\mathcal B\approx2.5386$), so
$A_E<2886.635$ for $\sin\theta$ and $A_E<436180.855$ for the raw Candidate 007 profile (against $A<84218$ and
$A<12725638$). Hence convergence with all derivatives holds on $r\ge2^{26}$ and $r\ge2^{42}$ respectively (strict
comparisons $A_E<2^{26\delta}$, $A_E<2^{42\delta}$ in outward-rounded arithmetic). These are radius statements; the
geometric ratio $A_ER^{-\delta}$ is below $0.913$ at $R=2^{26}$, and a ratio below $1/2$ holds for $\sin\theta$ at
$R=2^{28}$ (compare Theorem D: $R=2^{36}$ with ratio $1/2$). The same dyadic radii hold at the quadratic irrational $\delta_*$ of
Section 8 (defined before Section 8.1) that lies within $2\cdot10^{-32}$ of Candidate 007's stored $\delta$.

Corollary (a uniform radius for a family of large $c$). For $f_1=\sin\theta$ and $c_N=2N+\sqrt5$, every integer
$N\ge16$, the series converges with all derivatives on $r\ge128$. Proof: with $\varphi=(1+\sqrt5)/2$ and
$T=N+1/\varphi$ one has $c_N=2T+1$, $\alpha=T/(2T+1)=[0;2,N,1,1,1,\dots]$, $e_0/e_1=T$ and $e_{k-1}/e_k=\varphi$ for
$k\ge2$, $q_1=2$, $q_2=2N+1$; so $e^{2E}\le T\varphi^{8/(2N+1)}$, and with $K=\lambda_\delta(L+2)/T$,
$A_E\le8\lambda_\delta(L+2)F\varphi^{8/(2N+1)}/\delta^2$. For $N\ge16$: $\delta>32/33$, $\lambda_\delta<97/32$ and
$\varphi^{8/33}<2^{8/33}<6/5$ ($2^85^{33}<6^{33}$), so $A_E<8\cdot\frac{97}{32}(\frac{33}{32})^2\frac65\cdot3<96$, and
$96^{33}<128^{32}$ gives $96<128^\delta$. $\square$

Status. PROVED: independent proof, reviewed here step by step, and the complete argument
with its corollaries is independently confirmed; its finite checks (outward enclosures of $E$ and $A_E$, 270000 threshold classifications, 29638 exact maximal mark
counts over binary trees through 512 leaves, 4599 scalar majorant comparisons, and the integer inequalities of the
corollary) are independently confirmed.

## 8. Explicit constants

$\delta=1/\sqrt5$, $c=(5+\sqrt5)/4$: $\alpha=1/(2\sqrt5)=[0;4,\overline{2,8}]$, $q_k=1,4,9,76,161,1364,2889,\dots$,
$\mathcal B(\alpha)=2.5385730957726$ (25 exact terms plus a tail bound $<4\cdot10^{-14}$), $\lambda_\delta=3.95967$.
The decimals in this section are rounded approximations (independently recomputed: $\mathcal B(\alpha)\approx
2.53857309577257$, $K\approx29.36656$, $A\approx84217.954$, $\log_{10}R_0\approx11.01354$), not outward-rounded
certificates. A certificate with exact rational upper bounds is given in Section 7.3.

| $f_1$ | $\alpha_1$ | $L$ | $K$ | $A$ | $\log_{10}R_0$ |
|---|---|---|---|---|---|
| $\sin\theta$ | 1 | 1 | 29.37 | $84217.95\ldots<84218$ | 11.0135 |
| $\sin\theta+\frac12\sin3\theta$ | 1.5 | 3 | 48.94 | $\approx2.11\cdot10^5$ | 11.90 |
| Candidate 007 profile (raw amplitude) | 21.586 | 19 | 205.6 | $12725637.79\ldots<12725638$ | 15.89 |

The two outward bounds $A<84218$ and $A<12725638$ are certified by interval arithmetic (512-bit balls) from exact
continued fractions; the other entries are rounded.

For the 007 profile normalized to unit $\ell^1$ norm ($\alpha_1=1$), $A=5.9\cdot10^5$ and $\log_{10}R_0=12.9$. These are rigorous but crude:
the numerically observed growth at $\delta=1/\sqrt5$, $f_1=\sin\theta$ is $\|f_{n+1}\|_{\ell^2}/\|f_n\|_{\ell^2}\approx L(1-2.03/n)$ with
$L\approx0.468$ (here $L$ is a growth constant, not the top frequency of the table; the $\ell^1$ ratio $\alpha_{n+1}/\alpha_n$
gives the same $L$ with exponent about $1.8$; Section 15), i.e. an observed growth constant about $1.8\cdot10^5$ times smaller than $A$.

A Brjuno parameter next to the stored value. The stored $\alpha_{007}=\delta_{007}/2$ is rational with continued fraction
$[0;4,2,7,2,1,5,8,3,1,3,3,2,4,2,1,1,1,43,17,1,2,3,7,8,1,3,1,1,3,5,2]$ and denominator $q_{31}=8152952920478362$. Let
$\alpha_*=[0;a_1,\dots,a_{31},1,1,1,\dots]$ (the same partial quotients followed by the golden tail). Then $\alpha_*$ is a
quadratic irrational of bounded type, $|\alpha_*-\alpha_{007}|=1/(q_{31}(q_{31}\phi+q_{30}))<10^{-32}$, so
$|\delta_*-\delta_{007}|<2\cdot10^{-32}$, and $\mathcal B(\alpha_*)=2.55753\ldots$ (the finite part is $2.5575257$; the tail
adds about $1.28\cdot10^{-14}$, and less than $2\cdot10^{-14}$ rigorously: for the golden tail
$q_{j+2}\ge2q_j$ and $q_{j+1}\le2q_j$, so with $Q=q_{31}$ the tail is at most $(4\log Q+14\log2)/Q<2\cdot10^{-14}$). Theorem A applies to Candidate 007's profile at $\delta_*$ with essentially the constants of
the last table row. At the stored rational value itself the pure series is defined up to order $8152952920478361$; the
compatibility at the first resonance is not computable and is OPEN.

### 8.1 Theorem E: rational parameters below the first resonance, and Candidate 007's stored value

At a rational $\delta$ the tree argument still controls every order below the first exact resonance, with the finite
Brjuno sum of the rational number $\delta/2$.

Theorem E (PROVED; independently confirmed, including the rational endpoint of the best-approximation argument, the residual pair count, and outward interval constants). Let $\delta\in(0,1)$ be rational, $\delta/2=p/q$ in
lowest terms, with continued fraction $[0;a_1,\dots,a_J]$ and convergent denominators $q_0=1,q_1,\dots,q_J=q$. Put
$$\mathcal B_{\rm rat}=\sum_{k=0}^{J-1}\frac{\log q_{k+1}}{q_k},\qquad
A_{\rm rat}=8K\,e^{2\mathcal B_{\rm rat}}\frac{\alpha_1}\delta,\qquad K=\frac{2\lambda_\delta(B+1)}{c-1},$$
for a finite odd sine polynomial $f_1\ne0$ of top frequency $L=B-1$ ($\alpha_n=\|f_n\|_0$ as in Section 4). Then for $1\le n<q$ the pure recursion is defined
(no stream resonance and no exceptional potential order occurs) and
$$\alpha_n\le\frac{d_n}ny_n\le\frac{A_{\rm rat}^n}{8Kn},\qquad\frac{\alpha_n}{d_n}\le\frac{A_{\rm rat}^n}{8Kn}.$$
Consequently, for $N<q$ the truncations $\rho_N=\sum_{n\le N}r^{p_n}f_n$, $\psi_N$, $\chi_N$ (built from the exact
coefficients, $\rho_N=-\partial_y\Delta\chi_N$, $\psi_N=(\chi_N)_{xy}$) satisfy, with $t=A_{\rm rat}r^{-\delta}<1$,
$$\sup_\theta r^{-\gamma}\big|(cX+u_N)\cdot\nabla\rho_N-\rho_N\big|\le\frac{\lambda_\delta(B+1)A_{\rm rat}}{64K^2}\,
\frac{N\,t^N}{1-t}.$$

Proof. (a) $n\delta/2=np/q\in\mathbb Z$ iff $q\mid n$; so for $n<q$, $n\delta\notin2\mathbb Z$ and $d_n=2\|n\delta/2\|\ge2/q>0$.
All Poisson and potential inverses at these orders are defined, and Lemma 4.2, Proposition 5.1 and (S) hold verbatim
for $n<q$. (b) For a rational $\alpha=p/q$ the best-approximation statements of Lemma 6.1 hold for $k\le J$: for
$1\le l<q_k$, $\|l\alpha\|\ge\|q_{k-1}\alpha\|$, and $\|q_{k-1}\alpha\|=1/(\alpha_k'q_{k-1}+q_{k-2})$ with complete quotient
$\alpha_k'\le a_k+1$ (equality $\alpha_J'=a_J$ at the last step), hence $\|q_{k-1}\alpha\|\ge1/(q_k+q_{k-1})$. So Lemma 6.1
and the counting Lemma 6.2 hold for $0\le k\le J$. (c) For $1\le m<q$, $\|m\alpha\|\ge1/q$, so $m\notin S_J$ (as
$1/(4q_J)<1/q$); thus every $m<q$ with $m\in S_0$ lies in $S_k\setminus S_{k+1}$ for a unique $k\le J-1$, and
$1/d_m\le2q_{k+1}$. In a tree with $n<q$ leaves all subtree sizes are $<q$, and the proof of Lemma 6.3 gives the product
bound $2^{n-1}\exp(2n\mathcal B_{\rm rat})$. Theorem 6.4's proof then gives the coefficient bounds for $n<q$. (d) The
residual of the truncation consists exactly of the pairs $i,j\le N<i+j$ (the pairs with $i+j\le N$ cancel against the
linear terms by (R)): $r^{-\gamma}\,\mathrm{res}=\sum_{i,j\le N<i+j}r^{-\delta(i+j-1)}(P_ig_if_j'-p_jg_i'f_j)$. By
Lemma 4.2 and Proposition 5.1 each pair is bounded by $\lambda_\delta(B+1)\frac{ij}{d_i}\alpha_i\alpha_j\le
\frac{\lambda_\delta(B+1)}{64K^2}A_{\rm rat}^{i+j}$; there are at most $N$ pairs with each $i+j=n\in(N,2N]$, and summing
the geometric series gives the bound. $\square$

Candidate 007's stored parameter. Here $q=8152952920478362$ (the first stream resonance $n_0$), the continued
fraction of $\delta/2$ has 31 partial quotients,
$\mathcal B_{\rm rat}=2.5575257\ldots$, $\lambda_\delta=3.95789$, and for the extracted leading polynomial (raw amplitude,
$\alpha_1=21.586$, $L=19$): $K=205.14$, $A_{\rm rat}\approx1.318\cdot10^7$, $\log_{10}A_{\rm rat}^{1/\delta}\approx15.906$; for
$f_1=\sin\theta$: $A_{\rm rat}\approx8.72\cdot10^4$. So at the stored rational $c$ every one of the first
$8152952920478361$ coefficients obeys the same geometric bound as at a Brjuno parameter, and for
$r\ge(2A_{\rm rat})^{1/\delta}$ (about $10^{16.58}$ at raw amplitude) the truncation at $N=n_0-1$ is an approximate exterior
solution with weighted stationary residual $\sup_\theta r^{-\gamma}|(cX+u_N)\cdot\nabla\rho_N-\rho_N|$ below
$2^{-8152952920478298}$ (certified exponent; for $f_1=\sin\theta$ below $2^{-8152952920478302}$). An independent
certificate in 512-bit interval arithmetic gives $A_{\rm rat}<13178350$ (raw 007 profile) and $A_{\rm rat}<87214$
($\sin\theta$). Whether the series continues beyond $n_0$ as a pure power series (compatibility at $n_0$) or must acquire a
logarithm there, and whether the continued (logarithmic) series converges, is not decided by this theorem (Section 14).
The decimals above are rounded (50-digit evaluation), not certified bounds.

### 8.2 An upper bound for the radius: the top Fourier mode (PROVED; independent proof, audited and independently confirmed)

Proposition 8.2. Let $f_1$ be a finite odd sine polynomial with top frequency $L$ and top coefficient $\alpha\ne0$; put
$B=L+1$, $d=c-1$, $\eta=B-\delta$, $a=2/\eta$, $b=2(B-1)/\eta$ (so $1<b<2$), and
$\mathcal B_x(a,b)=\int_0^xu^{a-1}(1-u)^{b-1}du$, $\mathcal B=\mathcal B_1$. Let $A_n$ be the coefficient of
$\sin((Bn-1)\theta)$ (the top frequency) in $f_n$. Then $A_n=(-1)^{n-1}\alpha^nh_n$ with $h_n>0$, and
$$\limsup_n|A_n|^{1/n}=\frac1{R_{\rm top}},\qquad R_{\rm top}=\frac{4d}{|\alpha|}\big[a\,\mathcal B(a,b)\big]^{1/a}.$$
Consequently, wherever the pure recursion is defined at all orders, the series $\sum z^{n-1}f_n$ has radius at most
$R_{\rm top}$ in $C^0$ (and at most $e^{-B\sigma}R_{\rm top}$ in $\|\cdot\|_\sigma$): for $r<R_{\rm top}^{-1/\delta}$ its terms
are unbounded in sup norm. $A_n$ is also the complete (constant in $\log r$) top coefficient of the canonical logarithmic
series of Section 14, so the same bound holds there.

Proof. The top stream coefficient of $g_i$ (frequency $Bi$) is $T_i=-A_i/(2(\eta i+2))$ by (B); its divisor is positive,
so it never resonates. In (R) the top output frequency $Bn-1$ arises only from the top modes of $g_i$ and $f_j$, and a
direct computation gives
$$(n-1)d\,A_n=\tfrac14\sum_{i+j=n}\Big[1-\frac{2Bj}{\eta i+2}\Big]A_iA_j .$$
With $A_n=(-1)^{n-1}\alpha^nh_n$ the kernel becomes $\frac{2Bj}{\eta i+2}-1$; symmetrized over $(i,j)\leftrightarrow(j,i)$ it is
$B[\frac j{\eta i+2}+\frac i{\eta j+2}]-1\ge\frac{2Bn}{\eta n+4}-1>0$ (the difference of the two bracketed expressions has
numerator $\eta(\eta n+2)(i-j)^2\ge0$, and $(B+\delta)n>4$), so $h_n>0$ by induction. With $E=z\partial_z$,
$H=\sum h_nz^n$, $J=\sum h_nz^n/(\eta n+2)$ (so $\eta EJ+2J=H$) the recursion is $(d-BJ/2)EH=dH-H^2/4$. Put $x=H/(4d)$,
$v=BJ/(2d)$: $Ex=x(1-x)/(1-v)$, $Ev=a(Bx-v)$. Eliminating $z$, $w=1/(1-v)$ solves
$w'-a\frac{Bx-1}{x(1-x)}w=\frac a{x(1-x)}$, whose integrating factor is $x^a(1-x)^b$ (partial fractions, $b=a(B-1)$);
the solution with $w(0)=1$ is $x^a(1-x)^bw=a\mathcal B_x(a,b)$. Then $d\log z/dx=(1-v)/(x(1-x))=a^{-1}d\log\mathcal B_x/dx$,
and the initial coefficient gives
$$z=4d\,[a\mathcal B_x(a,b)]^{1/a},\qquad H=4dx,$$
an analytic, increasing map of $x\in(0,1)$ onto $z\in(0,R_H)$, $R_H=4d[a\mathcal B(a,b)]^{1/a}$, with analytic inverse near
$0$ that reproduces the coefficients. Since $h_n\ge0$, the radius of $H$ is the first real singularity (Pringsheim), so it
is at least $R_H$; at $x=1$, $dz/dx\to0$ because $b>1$, so $dH/dz\to\infty$ and the radius is exactly $R_H$. Finally
$|A_n|\le\frac4\pi\|f_n\|_{L^\infty}$ and $\|f_n\|_\sigma\ge|A_n|e^{\sigma(Bn-1)}$. For the logarithmic series the same support
argument applies: resonant stream modes have frequency $n\delta-2<Bn$, the top density coefficient is constant in
$\log r$ by induction, and so is the top stream inverse. $\square$

Values for $f_1=\sin\theta$ ($B=2$): $R_{\rm top}=2.56653\ldots$ at $\delta=1/\sqrt5$ ($1/R_{\rm top}=0.38963$, against the
observed growth constant $0.468$ and the proved $A<84218$), and $1/R_{\rm top}=0.17789,\ 0.32437,\ 0.39343$ at
$\delta=2/3,\ 1/2,\ 4/9$ (512-bit evaluation of the beta integrals, two independent formulas). The finite-order growth
estimates of the full series (NUMERICAL EVIDENCE) exceed these values, consistent with the proved inequality
$\limsup_n\|f_n\|_0^{1/n}\ge1/R_{\rm top}$. For Candidate 007's profile the top coefficient is small
($\alpha=a_{19}\approx1.9\cdot10^{-3}$) and $1/R_{\rm top}\approx1.5\cdot10^{-3}$ is far below the finite-order growth
estimate, so the bound is uninformative there. Which singularity dominates the full series is OPEN.
Section 14.22(d) sharpens Proposition 8.2: $\lim_n|A_n|^{1/n}=1/R_{\rm top}$ exists, and
$h_n=\mathcal K R_H^{-n}n^{-1-\nu}(1+O(n^{-\nu}))$ with explicit $\mathcal K>0$ (PROVED).

### 8.3 Profiles that cancel the leading stream, and the shape of Candidate 007 (PROVED: independent proof, audited and independently confirmed)

Proposition 8.3. Let $0<\gamma<1$, $d=c-1$, $K\ge0$, $N=2K+2$, and
$$a_0=1,\qquad a_k=\prod_{j=1}^k\frac{2j-1-\gamma}{2j+1+\gamma},\qquad f_1^{(K)}=\sum_{k=0}^Ka_k\sin((2k+1)\theta).$$
(i) These are the unique profiles of top frequency at most $2K+1$ with $\sin\theta$ coefficient 1 whose leading stream
has no modes $\sin2\theta,\dots,\sin2K\theta$; the leading stream is $g_1=-a_K\sin(N\theta)/(2(N+\gamma+1))$.
(ii) All $a_k>0$, $\sum_{k\le K}a_k=\big(\frac{1+\gamma}2-(K+\frac{3+\gamma}2)a_{K+1}\big)/\gamma\le\frac{1+\gamma}{2\gamma}$ and
$a_K\le\big(\frac{3+\gamma}{2K+3+\gamma}\big)^{1+\gamma}$.
(iii) $\|f_2^{(K)}\|_{\ell^1}=\frac{a_K}{2d(N+\gamma+1)}\sum_{k\le K}a_k\max\{(1+\gamma)(2k+1),\gamma N\}$, which is nonzero, at
most $(1+\gamma)^2a_K/(4\gamma d)$, and asymptotic to $(1+\gamma)a_K/(4d)$ as $K\to\infty$.
(iv) As $K\to\infty$, $f_1^{(K)}$ converges uniformly to $A_\gamma^{-1}\operatorname{sign}(\sin\theta)|\sin\theta|^\gamma$,
$A_\gamma=\frac2\pi\int_0^\pi\sin^{1+\gamma}\theta\,d\theta$. The corresponding density $A_\gamma^{-1}\operatorname{sign}(y)|y|^\gamma$
is an exact stationary solution with zero velocity ($\partial_x\rho=0$, and $c\,y\partial_y\rho=c\gamma\rho=\rho$), but it is
not $C^1$ across $y=0$, so it is not an admissible smooth profile.

Proof. (i) By (B) at $n=1$ ($P_1=1+\gamma$) the stream mode $j$ is $-a_{j-1}/(2(2j+1+\gamma))+a_j/(2(2j-1-\gamma))$;
setting it to zero for $j\le K$ gives the product, and at $j=K+1$ only the first term remains. (ii) With
$A=\frac{1-\gamma}2$, $B'=\frac{3+\gamma}2$ one has $(k+B')a_{k+1}=(k+A)a_k$, hence
$(k+B'-1)a_k-(k+B')a_{k+1}=\gamma a_k$; summing telescopes. The bound on $a_K$ follows from
$a_K=\prod_j(1-\frac{1+\gamma}{j+(1+\gamma)/2})$, $\log(1-x)\le-x$ and an integral comparison. (iii) By (R) at $n=2$,
$d f_2=(1+\gamma)g_1f_1'-\gamma g_1'f_1$; with $g_1=b\sin N\theta$ the mode $m=2k+1$ of $f_1$ contributes
$\frac{ba_k}{2d}((1+\gamma)m-\gamma N)$ at frequency $N+m$ and $\frac{ba_k}{2d}((1+\gamma)m+\gamma N)$ at $N-m$, all frequencies
distinct; $|x-y|+x+y=2\max(x,y)$ gives the norm, and dominated convergence the limit. (iv) The function
$h=\operatorname{sign}(\sin\theta)|\sin\theta|^\gamma$ satisfies $\gamma\cos\theta\,h-\sin\theta\,h'=0$, i.e. $\partial_x(r^\gamma h)=0$, so its
Fourier coefficients obey the cancellation relations of (i); by (ii) the series converges absolutely and uniformly. $\square$

Meaning. Small low-order coefficients are not a bound on the growth constant, and the constants of Theorems A and D grow
with the bandwidth $K$, so Proposition 8.3 does not by itself improve the radius. It does identify a mechanism. The exact
leading profile of Candidate 007, normalized to $\sin\theta$ coefficient 1, has $\sin3\theta,\sin5\theta$ coefficients
$0.1135, 0.0336$, against $0.1260, 0.0555$ for the family at the stored $\gamma=0.55239$; its leading stream mode
$\sin2\theta$ is $-0.0140$, against $-0.1408$ for $\sin\theta$ (exact rational evaluation, displayed rounded). The
reduction by a factor of about 10 is specific to this first stream harmonic: the combined polar velocity norm $V_0$ of
Proposition 8.4 is $0.0909$ for Candidate 007's normalized profile against $1/2$ for $\sin\theta$ (a factor 5.5), and the
minimum of $V_0$ over profiles of degree at most 19 is $0.00345$. The Wiener distance from the normalized profile to the
normalized shear is $0.254$ (the shear has Wiener norm $1.405$). So Candidate
007's profile is close to the zero-velocity shear $\operatorname{sign}(y)|y|^\gamma$. This is a plausible explanation (a
heuristic, not a proof) of why its finite-order
growth constant per unit $\sin\theta$ amplitude ($3.5/18.568\approx0.19$, NUMERICAL EVIDENCE) is well below the value
$0.468$ for $\sin\theta$ at nearby $\delta$, and why halving its $\sin3\theta$ coefficient raises the finite-order growth
estimate (NUMERICAL EVIDENCE). Whether the infinite-order growth constant tends to zero along the family is OPEN.

Proposition 8.4 (leading-velocity minimizers; PROVED: independent proof, reviewed here and independently confirmed).
Let $f_1=\sum_ka_k\sin((2k+1)\theta)$ be real-analytic, i.e. $|a_k|\le Ce^{-\varepsilon k}$ for some $\varepsilon>0$ (this
includes all finite sine polynomials and all profiles of finite strip norm $\|f_1\|_\sigma$, $\sigma>0$), with $a_0=1$.
With $P=1+\gamma$, $A_0=1$, $A_k=\prod_{l=1}^{k}\frac{2l-P}{2l+P}$ (the coefficients $a_k$ of Proposition 8.3) and
$g_1=\sum_jb_j\sin2j\theta$ the leading stream of $f_1$, put
$V_\sigma=\|g_1'\|_\sigma+P\|g_1\|_\sigma=\sum_j(2j+P)e^{2j\sigma}|b_j|$ (the Wiener norm of the two polar leading-velocity
components). Then $\sum_jc_jb_j=-1$ with $c_j=2(2j+P)/A_{j-1}$, hence $V_\sigma\ge\inf_jW_j$, $W_j=A_{j-1}e^{2j\sigma}/2$, with
equality exactly for convex combinations of the truncations of Proposition 8.3 at minimizing indices. At $\sigma=0$ and
degree at most $2K+1$ the unique minimizer is the family member $f_1^{(K)}$, with $V_0=A_K/2$; over all analytic profiles
$\inf V_0=0$ is not attained. For $\sigma>0$ the minimizing index is $\lceil(P/2)\coth\sigma\rceil$ (two tied indices when
$(P/2)\coth\sigma$ is an integer). Proof: with $s_k=a_k/A_k$, (B) at $n=1$ reads $2(2j+P)b_j/A_{j-1}=s_j-s_{j-1}$; summing gives
the constraint ($s_0=1$, and $s_k\to0$ because $a_k$ decays exponentially while $A_k$ decays only like $k^{-P}$), then $\sum w_j|b_j|\ge\inf_j(w_j/c_j)\,|\sum c_jb_j|$,
and $W_{j+1}/W_j=e^{2\sigma}(2j-P)/(2j+P)$ is increasing in $j$. $\square$ The analyticity hypothesis is needed: for the
non-analytic profile $a_k=A_k$ (the shear itself, Wiener class only) all $b_j$ vanish and the constraint fails. This
concerns the linear leading Poisson map only; it does not minimize $\|f_2\|$, the growth constant or the radius.

### 8.5 Candidate 007's exact leading data

Candidate 007's stored parameters are $c=4076476460239181/2^{51}$ and $\delta=1-1/c=1824676646553933/4076476460239181$.
Its leading density profile, extracted exactly from the stored coefficient file (the accompanying artifacts), is
$f_1=\sum_{j\in\{1,3,\dots,19\}}a_j\sin j\theta$ with the following reduced fractions $a_j=u_j/v_j$:

- $a_{1}$: $u=53501412188225329043456378665984841156800774793640858598810651910894675943891259402603$, $v=2881404794319635260205243881084667137623393188492655664427500723137627314703787098112$;
- $a_{3}$: $u=3036023326053406465428409492820059643010786423837762141517160205226178197221964175853$, $v=1440702397159817630102621940542333568811696594246327832213750361568813657351893549056$;
- $a_{5}$: $u=900056916006943473347773975213892472207893042373130943766688246408762314113015286225$, $v=1440702397159817630102621940542333568811696594246327832213750361568813657351893549056$;
- $a_{7}$: $u=108853646715257036862143108217933292797833436415270310591798293935788295098289498393$, $v=720351198579908815051310970271166784405848297123163916106875180784406828675946774528$;
- $a_{9}$: $u=-1171779746151241573555363399700741889232977971124414655043470426904987534707767593277$, $v=11525619177278541040820975524338668550493572753970622657710002892550509258815148392448$;
- $a_{11}$: $u=324368115644365179358590068298161176836225025021358091526739678306614147871685016313$, $v=11525619177278541040820975524338668550493572753970622657710002892550509258815148392448$;
- $a_{13}$: $u=26613729498246410043640166041841442929887826751468229650894806158848938995293900925$, $v=11525619177278541040820975524338668550493572753970622657710002892550509258815148392448$;
- $a_{15}$: $u=16866701624570492891512400918720799503164451797956623575433679823404791694343438125$, $v=46102476709114164163283902097354674201974291015882490630840011570202037035260593569792$;
- $a_{17}$: $u=-39582895742399680732391972940642397747041019152701328226371589490938627373132685435$, $v=46102476709114164163283902097354674201974291015882490630840011570202037035260593569792$;
- $a_{19}$: $u=43722108434953264581307482219906309863224888822988585606559734924365698324354185625$, $v=23051238354557082081641951048677337100987145507941245315420005785101018517630296784896$.

So $a_1\approx18.567822$, $a_3/a_1\approx0.113493$ and $\|f_1\|_{\ell^1}=\sum_j|a_j|\approx21.58623$. These are the exact
coefficients used in Theorem E, in Section 8.3 and in Corollary T_{9,2}.C. A separate extraction from the same stored file, written independently, gives the
same ten reduced fractions.

## 9. Theorem B: stability

Theorem B (PROVED; independently confirmed). (i) Fix Brjuno $\alpha=\delta/2$ and $\sigma_0>0$. Each $f_n$ is a continuous homogeneous
polynomial of degree $n$ as a map $\mathcal A_{\sigma_0}\to\mathcal A_\sigma$ for every $\sigma<\sigma_0$ (not, in general,
as a map $\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0}$: already the derivative of $f_1\mapsto f_2$ at $\sin\theta$ is
unbounded on $\mathcal A_{\sigma_0}$, since its $\sin((m+2)\theta)$ output coefficient on the unit vectors
$e^{-\sigma_0m}\sin(m\theta)$ grows linearly in $m$ after weighting), and for $\|f_1\|_{\sigma_0}\le M$ the series converges in
$\mathcal A_\sigma$ uniformly for $|z|\le\theta_0(\sigma_0-\sigma)/A'(M)$, any $\theta_0<1$. Hence the exterior solution
depends analytically on $f_1$ and every perturbation of $f_1$ in $\mathcal A_{\sigma_0}$ preserves convergence on a common
exterior domain $r>R'(M)$.
(ii) Fix $[\delta_-,\delta_+]\subset(0,1)$ and $\mathcal B_*<\infty$, and let
$D_{\mathcal B_*}=\{\delta\in[\delta_-,\delta_+]:\mathcal B(\delta/2)\le\mathcal B_*\}$. The constants of Theorems 6.4 and A'
are bounded on $D_{\mathcal B_*}$, so the radius bound is uniform there (here $\mathcal B:=+\infty$ at rational $\delta/2$,
so $D_{\mathcal B_*}$ consists of irrationals). Each $f_n$ depends continuously, indeed locally analytically, on $\delta$
at every irrational $\delta$, as a map into $\mathcal A_\sigma$, $\sigma<\sigma_0$: at fixed order the Poisson operators are
analytic in $\delta$ away from their resonances, their high-frequency denominators are uniformly controlled on a small
parameter neighbourhood, and the recursion composes them with the nonlinearity between successively smaller strips (for
finite profiles $f_n$ is a rational function of $\delta$ with poles at resonant rationals; for infinite profiles it need
not be rational). Hence the sum is continuous on $D_{\mathcal B_*}\times\{\|f_1\|_{\sigma_0}\le M\}$; for the potential
one also uses that a bounded Brjuno sum keeps $\delta$ away from each fixed exceptional rational, so the finitely many
exceptional potential inverses are uniformly bounded. The measure of $[\delta_-,\delta_+]\setminus D_{\mathcal B_*}$ tends to
zero as $\mathcal B_*\to\infty$.
(iii) For fixed $f_1$, the set of $\delta$ at which the pure series exists to all orders excludes every rational at
which a compatibility condition fails; for $f_1=a\sin\theta$ this includes $\delta=4/9$ ($c=9/5$) and $\delta=1/2$
($c=2$). For every finite real profile with nonzero $\sin\theta$ coefficient such rationals are dense (Theorems P, P',
Section 10.1), so the admissible set contains no interval.
Stability in $c$ is therefore formulated in the Brjuno class with a bound on $\mathcal B$, not on open intervals.

Proof. (i) Scaling gives homogeneity; induction on (R) with the smaller-strip targets gives polynomiality and
continuity; Theorem A' gives the uniform bound; uniform limits of polynomials with geometric bounds on bounded sets are
analytic. (ii) The constants depend on $\delta$ through $\lambda_\delta$, $c-1=\delta/(1-\delta)$ and
$\mathcal B$. Continuity of the sum follows from the Weierstrass M-test. The measure statement is because $\mathcal B<\infty$
almost everywhere. (iii) Proposition 3.2. $\square$

## 10. Theorem C: obstruction and generic divergence

Fix $f_1\ne0$ (a finite odd sine polynomial). For a rational $\delta_*$ let $n_0$ be its first stream resonance, $j_0=n_0\delta_*/2-1$, and
$\kappa(\delta_*)$ the coefficient of $\sin((2j_0-1)\theta)$ in $f_{n_0}(\delta_*)$ (all $f_n$, $n\le n_0$, are regular at
$\delta_*$).

Lemma 10.1. If $\kappa(\delta_*)\ne0$ then $\|f_{n_0+1}(\delta)\|_0\to\infty$ as $\delta\to\delta_*$ through irrationals.

Proof. At order $n_0$ all multipliers in (B) other than $1/(2(2j_0+2-n_0\delta))$ are regular at $\delta_*$, so
$g_{n_0}(\delta)=S(\delta)\sin(2j_0\theta)+\tilde g(\delta)$ with $\tilde g$ continuous and
$S(\delta)=-a_{n_0,j_0-1}(\delta)/(2(2j_0+2-n_0\delta))$, $|S|\to\infty$. In (R) at order $n_0+1$ only the pair
$(i,j)=(n_0,1)$ involves $g_{n_0}$, so $f_{n_0+1}=\frac{S(\delta)}{n_0(c-1)}[P_{n_0}\sin(2j_0\theta)f_1'-2j_0p_1\cos(2j_0\theta)f_1]
+$ (continuous). At $\delta_*$ the bracket is $-2j_0[\sin(2j_0\theta)f_1'+\gamma\cos(2j_0\theta)f_1]$, which is not
identically zero (simplest check: if $a_L\sin(L\theta)$ is the top harmonic of $f_1$, the coefficient of
$\sin((L+2j_0)\theta)$ in the bracket is $-2j_0\frac{L+\gamma}2a_L\ne0$; alternatively: otherwise $f_1=C|\sin(2j_0\theta)|^{-\gamma/(2j_0)}$ on each interval between zeros of
$\sin(2j_0\theta)$, which is unbounded unless $C=0$, forcing $f_1\equiv0$). Explicitly,
$\operatorname{Res}_{\delta=\delta_*}f_{n_0+1}=-\frac{\kappa(\delta_*)j_0}{n_0^2(c_*-1)}[\sin(2j_0\theta)f_1'+\gamma_*\cos(2j_0\theta)f_1]$. $\square$

Theorem C (PROVED as a conditional theorem, independently confirmed; the hypothesis is PROVED in Section 10.1 for
every finite real profile with nonzero $\sin\theta$ coefficient, and in Section 10.2 for generic analytic profiles). Let $I\subset(0,1)$ be an open interval. Assume
(H): the rationals $\delta_*\in I$ with $\kappa(\delta_*)\ne0$ are dense in $I$. Then
$G=\{\delta\in I\setminus\mathbb Q:\limsup_n\|f_n(\delta)\|_0^{1/n}=\infty\}$ is a dense $G_\delta$ subset of $I$, and
for $\delta\in G$ the series $\sum z^{n-1}f_n$ has radius zero: for no $r$ does
$\sum r^{p_n}f_n$ converge uniformly in $\theta$ (its terms are unbounded in sup norm).

Proof. $U_{M,N}=\{\delta\in I\setminus\mathbb Q:\exists n\ge N,\ \|f_n(\delta)\|_0>M^n\}$ is relatively open in $I\setminus\mathbb Q$
because each $f_n$ is continuous there; thus $U_{M,N}$ is the intersection of $I\setminus\mathbb Q$ with an open subset of $I$. It is dense: any open $J\subset I$ contains infinitely many rationals with
$\kappa\ne0$, hence one with denominator $\ge N$, so $n_0\ge N$; by Lemma 10.1 irrationals close to it lie in $U_{M,N}$.
$I\setminus\mathbb Q$ is completely metrizable, so $\bigcap_{M,N}U_{M,N}$ is a dense $G_\delta$ in it; since
$I\setminus\mathbb Q$ is itself a $G_\delta$ in $I$ and each $U_{M,N}$ is the trace of an open set, it is a dense $G_\delta$ in
$I$. Sup
norms: on trigonometric polynomials of degree $\le nB$, $\|h\|_0\le(2nB+1)^{1/2}\sqrt2\,\|h\|_{L^\infty}$, so the sup norms
also have $\limsup^{1/n}=\infty$. $\square$

$G$ is disjoint from the Brjuno set (Theorem A), so under (H) both convergence (full measure) and divergence (residual
set) occur in every interval. A weaker hypothesis suffices: density of rationals where some $f_n$ has a pole. Exact
computation gives $\kappa\ne0$ at all 55 rationals $\delta\in(0.40,0.50)$ with $n_0\le60$ for $f_1=\sin\theta$, with
$|\kappa|/\|f_{n_0}\|_{\ell^1}$ between $4\cdot10^{-6}$ and $4\cdot10^{-3}$ (finite exact facts); Section 10.1 proves (H)
for all intervals. Modular computation extends the list. If every divisor of the recursion through $n_0$ is nonzero
modulo a prime $\ell$, every coefficient lies in the ring $\mathbb Z_{(\ell)}$ of rationals with denominator prime to $\ell$,
reduction modulo $\ell$ is a ring homomorphism on it, and so the recursion run in $\mathbb F_\ell$ returns $\kappa\bmod\ell$; a
nonzero residue proves $\kappa\ne0$ (a zero residue would be inconclusive). With $\ell=33554393$ and, where needed, a second
prime: $\kappa\ne0$ for $f_1=\sin\theta$ at every $\delta=2h/Q\in(0,1)$ with $h\ge2$, $\gcd(h,Q)=1$, $Q\le120$ (2074 parameters, first
resonance at $n_0=Q$), and for the exactly extracted leading profile of Candidate 007 at every such $\delta\in(\frac25,\frac12)$
(217 parameters). So at each of these parameters the pure series with that profile is obstructed at order $Q$ (finite
exact facts, independently confirmed: computed by a Cartesian finite-field program with every modular division checked,
and both grids also by a separate polar Fourier program, with equal residues at all 2291 parameters). (H) does depend on $f_1$: the inputs $\sin11\theta$ and $\sin13\theta$ (zero $\sin\theta$ coefficient)
are compatible at the first resonance of $\delta=4/9$ (exact), while $\sin9\theta$ is not. With the free stream constant
of order 9 set to zero (the canonical choice), both are incompatible at the second resonance, order 18, $j=3$: the
coefficient of $\sin5\theta$ in $f_{18}$ is about $2.2055\cdot10^{-4}$ and $2.666\cdot10^{-5}$ (exact rational
computation, reproduced by an independent program; finite exact facts). With that constant free, the second condition
is affine in it (Lemma T_{Q,h}.1). For $\sin13\theta$ the slope is $\sigma_1\approx-5.490\cdot10^{-2}\ne0$, the next
slope is nonzero too, and then $\sigma_3=0$ exactly by a support gap (Proposition T_{Q,h}.6) while $R_3\ne0$: every pure
series with this profile is obstructed at order 36 for every choice of the constants (finite exact computation, Section
12.6, independently reproduced: PROVED). The same happens for $\sin15\theta$ at order 45 (PROVED). For $\sin11\theta$ the support gap is absent, and the first two
slopes are nonzero: $\sigma_1\approx0.17640$ (with $R_1\approx2.2055\cdot10^{-4}$) and $\sigma_2\approx8.7815$ (finite exact
computation by the polar Fourier program of Section 12.6), and so is the third, $\sigma_3\approx0.12419$ (with
$R_3\approx-9.559\cdot10^{-2}$): the tuned pure series of $\sin11\theta$ exists through order 36, with $H_9,H_{18},H_{27}$ uniquely fixed (finite exact
computation; $H_{36}$ is fixed only by the order-45 condition). In fact every response is bounded away from zero and the
tuned series converges (Corollary T_{Q,h}.9, PROVED).

### 10.1 Theorem P: prime denominators are incompatible (PROVED; independent proof, audited and independently confirmed, with independent exact checks)

Theorem P. Let $p\ge5$ be prime, $a$ even with $4\le a<p$, $\delta=a/p$ (so $c=p/(p-a)$). Let
$f_1=\sum_{m\text{ odd}}\alpha_m\sin m\theta$ be a finite sine polynomial with rational coefficients and $\alpha_1\ne0$,
such that $p$ divides no denominator of the $\alpha_m$ and not the numerator of $\alpha_1$. Then the first stream
resonance is at $n_0=p$, $j_0=a/2-1$; the coefficients of $f_n$, $n\le p$, are rationals with denominators prime to $p$;
and the compatibility coefficient (the coefficient of $\sin((a-3)\theta)$ in $f_p$) satisfies
$$\kappa\equiv(-1)^{(a-4)/2}\,\alpha_1\pmod p .$$
In particular $\kappa\ne0$. For $f_1=\sin\theta$, coefficientwise
$f_p\equiv\sum_{\ell=0}^{p-1}(-1)^\ell\sin((2\ell+1)\theta)-(-1)^{(p-1)/2}\sin(p\theta)\pmod p$.

Proof. Write $s=\sin\theta$, $q=\cos\theta$, $D=\partial_\theta$, $\mu=(p-1)/2$, $\mathbb Z_{(p)}$ for the rationals with
denominator prime to $p$; congruences are coefficientwise in $\mathbb Z_{(p)}$ (after adjoining $i$ and inverting $q$
where needed; reduction mod $p$ of Laurent polynomials in $w=e^{i\theta}$ embeds into $\mathbb F_p(i)((w))$).

(i) Reduction. $n\delta\in2\mathbb Z$ iff $p\mid n$, so all orders $i<p$ are nonresonant, and by (B)
$b_{i,j}=\frac p2\big[-a_{i,j-1}/(p(2j+2)-ia)+a_{i,j}/(p(2j-2)+ia)\big]$ with denominators $\equiv\mp ia$, units for
$1\le i<p$. Hence if $f_i$ is $p$-integral then $g_i\in p\,\mathbb Z_{(p)}$ and, using
$q\sin((2k+1)\theta)=\frac12(\sin(2k+2)\theta+\sin2k\theta)$, $g_i/p\equiv qf_i/(ia)$. So $P_ig_i=2g_i-ia\,g_i/p\equiv-qf_i$
and $p_jg_i'=g_i'-ja\,g_i'/p\equiv-\frac ji(qf_i)'$. Since $\lambda_n=(n-1)a/(p-a)\equiv-(n-1)$ is a unit for
$2\le n\le p$, induction shows that $f_n$ ($n\le p$) is $p$-integral and reduces to $F_n$, where $F_1=f_1$ and
$$(n-1)F_n=\sum_{i+j=n}\Big[qF_iF_j'-\frac ji(qF_i)'F_j\Big]\tag{10.1}$$
(a recursion over $\mathbb Q$ whose denominators are prime to $p$ for $n\le p$).

(ii) Generating identity (over $\mathbb Q$). Put $U=\sum_nF_nz^n$, $A=q\sum_nF_nz^n/n$, $E=z\partial_z$, so $EA=qU$. Then
(10.1) reads $(1+A_\theta)EU-qUU_\theta=U$, i.e. $\mathcal LU=U$ for the derivation
$\mathcal L=(1+A_\theta)E-(EA)\partial_\theta$ of $\mathbb Q[s,q,q^{-1}][[z]]$. One has $\mathcal LA=EA$ and
$\mathcal L\phi(\theta)=-(EA)\phi'(\theta)$, so for $W=U-\sum_{k\ge1}\frac{A^k}{k!}D^{k-1}\sec\theta$ the sum telescopes:
$\mathcal L\sum_{k\ge1}\frac{A^k}{k!}D^{k-1}\sec=EA\sum_{k\ge1}\big[\frac{A^{k-1}}{(k-1)!}D^{k-1}\sec-\frac{A^k}{k!}D^k\sec\big]
=EA\sec\theta=U$, hence $\mathcal LW=0$. $W$ has no $z^0$ term and $\mathcal L=E+O(z)$, so its lowest coefficient
$W_N$ satisfies $NW_N=0$: $W=0$. Thus
$$EA=\sum_{k\ge1}v_kA^k,\qquad v_k=\frac{q\,D^{k-1}\sec\theta}{k!},\qquad v_1=1,\quad A_1=qf_1,$$
and comparing coefficients, $(n-1)A_n=\sum_{k=2}^nv_k[z^n]A^k$.

(iii) Order $p$. $D^{k-1}\sec\theta\in\mathbb Z[s,q,q^{-1}]$, so $v_k$ is $p$-integral for $k<p$, and $A_n=qF_n/n$ is
$p$-integral for $n<p$. At $n=p$ all terms with $k<p$ are $p$-integral; multiplying by $p$ and reducing,
$(p-1)\,pA_p\equiv pv_pA_1^p$. With $pA_p=qF_p$, $pv_p=qD^{p-1}\sec\theta/(p-1)!$ and Wilson's theorem
$(p-1)!\equiv-1$: $F_p\equiv D^{p-1}(\sec\theta)\,(qf_1)^p$.

(iv) In characteristic $p$, $D^{p-1}\sec\theta=(-1)^\mu\sec\theta-\sec^p\theta$: in $w$, $\sec\theta=2\sum_k(-1)^kw^{2k+1}$
and $D=iw\partial_w$; $(w\partial_w)^{p-1}$ fixes $w^e$ for $p\nmid e$ and kills it for $p\mid e$ (Fermat); the killed
part ($k=\mu+pj$) is $(-1)^\mu\sec^p\theta$ (Frobenius, $2^p=2$); and $i^{p-1}=(-1)^\mu$. Hence
$F_p\equiv f_1^p\,[(-1)^\mu q^{p-1}-1]$.

(v) For $f_1=\sin\theta$: $s^p\equiv(-1)^\mu\sin p\theta$ and $q^p\equiv\cos p\theta$, so
$F_p\equiv\sin p\theta\cos p\theta/q-(-1)^\mu\sin p\theta$, and multiplying by $2q$ and telescoping,
$\sin(2p\theta)/(2q)=\sum_{\ell=0}^{p-1}(-1)^\ell\sin((2\ell+1)\theta)$ ($p$ odd). This is the stated pattern: coefficient
$(-1)^\ell$ at every odd mode $2\ell+1\le2p-1$ except $0$ at mode $p$. The mode $a-3=2\ell+1$ has $\ell=(a-4)/2<\mu$.
For general $f_1$, Frobenius gives $f_1^p\equiv\sum_m\alpha_m^p\sin(m\theta)^p$, $\sin(m\theta)^p\equiv(-1)^\mu\sin(mp\theta)$,
and for $m\ge3$ the term $\sin(mp\theta)[(-1)^\mu q^{p-1}-1]$ has only frequencies $\ge(m-1)p+1>a-3$; the term $m=1$ gives
$\alpha_1^p\equiv\alpha_1$ times the pattern above. $\square$

Checks: a direct exact implementation of (R) and (B) (independent of (10.1)) confirms the congruence and the complete
pattern for $f_1=\sin\theta$ for all 37 pairs $(p,a)$ with $p\le23$, and the 21 prime-denominator cases of the exact
55-rational scan have the predicted residues.

Theorem P' (every finite real profile with a first harmonic; PROVED: independent proof, audited and independently confirmed). Let
$f_1=\sum_{m\text{ odd}\le L}\alpha_m\sin m\theta$ with real $\alpha_m$ and $\alpha_1\ne0$. There is a finite set $S$ of primes,
depending on $f_1$, such that $\kappa(a/p)\ne0$ for every prime $p\ge5$ outside $S$ and every even $a$ with $4\le a<p$.

Proof. Replace the amplitudes by indeterminates $X_m$. The compatibility coefficient $K_{p,a}(X)$ is a homogeneous
polynomial of degree $p$ with coefficients in $\mathbb Z_{(p)}$ (the proof of Theorem P runs verbatim over $\mathbb Q[X]$:
the divisors depend only on $a,p$, the order and the Fourier index), and steps (iv), (v) give
$K_{p,a}(X)\equiv(-1)^{(a-4)/2}X_1^p\pmod p$; over the polynomial ring the $p$-th power must be kept. Algebraic amplitudes:
choose $D\ge1$ such that the minimal polynomials of all $\alpha_m$ and of $\alpha_1^{-1}$ have coefficients in $\mathbb Z[1/D]$,
and let $S_0=\mathbb Z[1/D][\alpha,\alpha_1^{-1}]$, which is integral over $\mathbb Z[1/D]$. For $p\nmid D$, $S_0/pS_0\ne0$:
otherwise $1/p$ is integral over $\mathbb Z[1/D]$, and multiplying its monic equation by a power of $p$ gives
$1\in p\,\mathbb Z[1/D]$, i.e. $p$ divides a power of $D$. In $S_0\otimes\mathbb Z_{(p)}$ the difference
$K_{p,a}(\alpha)-(-1)^{(a-4)/2}\alpha_1^p$ lies in $p(S_0\otimes\mathbb Z_{(p)})$ and $\alpha_1^p$ is a unit, so
$K_{p,a}(\alpha)=0$ would force $S_0/pS_0=0$. Real amplitudes: $R=\mathbb Q[\alpha,\alpha_1^{-1}]\subset\mathbb R$ is a
nonzero finitely generated $\mathbb Q$-algebra; for a maximal ideal $\mathfrak m$ the residue field $R/\mathfrak m$ is a
finite extension of $\mathbb Q$ (Hilbert's Nullstellensatz in Zariski's form), and the images $\beta_m$ of $\alpha_m$ are
algebraic with $\beta_1\ne0$. Since $K_{p,a}$ has rational coefficients, $K_{p,a}(\alpha)=0$ implies $K_{p,a}(\beta)=0$,
which fails for $p$ outside the finite exceptional set of $\beta$. $\square$

The specialization only excludes exact vanishing; it gives no lower bound for $|\kappa|$. Exact checks over $\mathbb Q[u]$
for $\sin\theta+u\sin3\theta+u^2\sin5\theta$ and $u\sin\theta+\sin3\theta$ at seven pairs $(p,a)$ with $p\le13$ confirm
the polynomial congruence (independent computation).

Odd numerators (exact finite computation here, independently confirmed by two further exact programs, an exact rational Fourier recursion and a Cartesian Laurent recursion, with identical $p$-adic digits; finite exact facts, not a theorem). Theorem P needs an even numerator. Let
$\delta=a/p$ with $p\ge5$ prime and $3\le a<p$ odd. For $n<2p$, $n\delta$ is an integer only at $n=p$, where it equals
the odd number $a$, so the first stream resonance is at $n=2p$ with $j=a-1$, and the compatibility coefficient is the
coefficient $\kappa_{\rm odd}$ of $\sin((2a-3)\theta)$ in $f_{2p}$. For $f_1=\sin\theta$, exact rational arithmetic
gives $\kappa_{\rm odd}\ne0$ at all 37 such pairs with $p\le23$, with $v_p(\kappa_{\rm odd})\in\{-2,-1,0\}$ (the value
$0$ occurs only at $(p,a)=(11,5)$). The leading $p$-adic digits show no pattern that we could fit, so no congruence
analogous to Theorem P is claimed for odd numerators; these 37 parameters are obstructed for $\sin\theta$ by finite
computation only.

Theorem C* (generic divergence, PROVED). Let $f_1$ be a finite odd real sine polynomial with nonzero $\sin\theta$
coefficient; for example $f_1=\sin\theta$, or the exactly extracted leading profile of Candidate 007. Then (H) holds on
every open interval $I\subset(0,1)$, and
$\{\delta\in(0,1)\setminus\mathbb Q:\limsup_n\|f_n(\delta)\|_0^{1/n}=\infty\}$ is a dense $G_\delta$ subset of $(0,1)$ of Lebesgue
measure zero. At each of its points the series has radius zero: for no $r$ are its terms bounded in sup norm.
Equivalently, for $c\in(1,\infty)$ divergence is topologically generic and convergence (Theorem A) is generic in measure.

Proof. For $[\alpha,\beta]\subset I$ with $\alpha>0$, every prime $p>\max(4/\alpha,2/(\beta-\alpha))$ has an even $a$ in
$[p\alpha,p\beta]$, and then $4<a<p$. Excluding the finite set $S$ of Theorem P' (for rational amplitudes: the primes
dividing a denominator or the numerator of $\alpha_1$, by Theorem P), $\kappa(a/p)\ne0$. Theorem C applies; measure zero
follows from Theorem A. $\square$

Corollary C*.1 (the growth constant is discontinuous; PROVED, independently confirmed). Let $f_1$ be as in Theorem C*
and, for irrational $\delta\in(0,1)$, let $\Lambda(\delta):=\limsup_n\|f_n(\delta)\|_0^{1/n}\in[0,\infty]$. Then
$\Lambda(\delta_0)<\infty$ at every $\delta_0$ with $\delta_0/2$ Brjuno, and $\Lambda=\infty$ on a dense subset of every open
interval. Hence $\Lambda$ is not bounded on any interval of irrational parameters, it is discontinuous (in the relative
topology of the irrationals) at every Brjuno point, and it is not a continuous, let alone smooth, function of $\delta$, or of
$c=1/(1-\delta)$, on the nonresonant parameters. Proof. Theorem A(1) gives convergence of $\sum z^{n-1}f_n$ in $\mathcal A_0$
for $|z|<1/A$, so $\Lambda(\delta_0)\le A<\infty$. Theorem C* gives the dense set where $\Lambda=\infty$; a sequence from it
converging to $\delta_0$ contradicts continuity at $\delta_0$, and density excludes a finite bound on any interval. The change
of variable to $c$ is a homeomorphism. $\square$ At a fixed order, $f_n$ is rational in $\delta$ with finitely many poles in a
compact interval, so finite-order fitted growth statistics can vary little over a sampled set of parameters that avoids
those poles; that says nothing about the limsup. The corollary is compatible with the uniform bound of Theorem A on a fixed
Brjuno sublevel set $\{\mathcal B\le M\}$.

### 10.2 Generic analytic data (PROVED; independent proof, audited and independently confirmed)

Fix $\sigma>0$ and $X_\sigma=\{f=\sum_ka_k\sin((2k+1)\theta):\|f\|_\sigma<\infty\}$. For each fixed $n$ and fixed irrational
$\delta$, $f_1\mapsto f_n$ is a continuous homogeneous polynomial of degree $n$ from $X_\sigma$ to $C^0$ (finitely many
bounded operations, using a finite decreasing sequence of strip widths for the angular derivatives).

(a) The set of $f_1\in X_\sigma$ for which every center $a/p$ of Theorem P is incompatible is a dense $G_\delta$ in
$X_\sigma$, and its complement meets every finite-dimensional subspace containing $\sin\theta$ in a Lebesgue null set. For
every such $f_1$ the conclusion of Theorem C* holds. Proof: the compatibility coefficient $K_t(f)$ at $t=a/p$ is a
continuous homogeneous polynomial of degree $p$, and $h\mapsto K_t(f+h\sin\theta)$ is a real polynomial with leading
coefficient $K_t(\sin\theta)\ne0$; so $\{K_t=0\}$ is closed with empty interior (in finite dimensions, the zero set of a
nonzero polynomial). Lemma 10.1 holds for analytic $f_1$: if $f_1$ vanishes to odd order $v$ at $0$, the bracket
$\sin(2j_0\theta)f_1'+\gamma_*\cos(2j_0\theta)f_1$ has leading Taylor coefficient $(2j_0v+\gamma_*)$ times that of $f_1$,
and the remaining terms of $f_{n_0+1}$ are continuous in $\delta$ near $\delta_*$. The Baire argument is unchanged.

(b) At a fixed irrational $\delta$, if one $g\in X_\sigma$ has $\limsup\|f_n(g)\|_\infty^{1/n}=\infty$, the data with this
property form a dense $G_\delta$ in $X_\sigma$. Proof: otherwise $\|f_n(f)\|_\infty\le M^n$ for $n\ge N$ on a ball
$B(f_0,r)$; with $h\|g\|_\sigma<r$, $t\mapsto f_n(f_0+tg)$ is a $C^0$-valued polynomial of degree $n$, bounded by $M^n$ on
$[-h,h]$, with leading coefficient $f_n(g)$; its $n$-th Chebyshev coefficient on $[-h,h]$ has norm $\le2M^n$, so
$\|f_n(g)\|_\infty\le(2M/h)^n$, a contradiction. $\square$

By Theorem C*, such $g$ (namely $\sin\theta$) exist at every point of a dense $G_\delta$ of parameters.

### 10.3 A computable divergent Liouville parameter (PROVED; independent construction, audited and independently confirmed)

In every interval with rational endpoints in $(0,1)$, in particular in every neighborhood of Candidate 007's stored
$\delta$, there is a computable Liouville number $\delta_*$ at which the pure series of $\sin\theta$ (or of Candidate
007's exact profile) has radius zero. Construction: choose nested closed rational intervals $I_k$, $|I_k|<2^{-k}$, around
centers $t_k=a_k/p_k$ of Theorem P with increasing primes $p_k>k$, such that $I_k\subset(t_k-p_k^{-k},t_k+p_k^{-k})\setminus\{t_k\}$,
$I_k$ avoids the first $k$ rationals of a fixed enumeration and the finitely many poles through order $p_k+1$, and the
coefficient of $\sin((L+2j_0)\theta)$ in $f_{p_k+1}$ ($L$ the top frequency of $f_1$, $\alpha_L$ its coefficient,
$j_0=a_k/2-1$) exceeds $k^{p_k+1}$ in modulus on $I_k$. By Lemma 10.1 this coefficient has a simple pole at $t_k$ with
residue $-\kappa j_0(L+\gamma_*)\alpha_L/(2p_k^2(c_*-1))\ne0$ (for $\sin\theta$: frequency $a_k-1$, residue
$-\kappa j_0(1+\gamma_*)/(2p_k^2(c_*-1))$), so such intervals exist and are found by exact rational arithmetic. The limit is irrational, computable, satisfies
$0<|\delta_*-a_k/p_k|<p_k^{-k}$ for all $k$, and $\|f_{p_k+1}(\delta_*)\|_0>k^{p_k+1}$.

### 10.4 An explicit arithmetic divergence condition (PROVED: independent proof, audited and independently confirmed)

Theorem Q. Let $K\subset\mathbb R$ be a number field of degree $d$ and $f_1=\sum_{m\le L,\ m\ \rm odd}\alpha_m\sin(m\theta)$
with $\alpha_m\in K$, $\alpha_1\alpha_L\ne0$, $B=L+1$. Let $\delta\in(0,1)$ be irrational and suppose that for some
$\tau>dB\pi^2/6$ there are infinitely many primes $p$ and even integers $4\le a<p$ with
$$0<|\delta-a/p|<p^{-\tau p^2}.$$
Then $\limsup_n\|f_n(\delta)\|_{\ell^1}^{1/n}=\infty$: the pure series has radius zero, in the Wiener and in the uniform
angular norm. The same holds for every nonzero real multiple of $f_1$. For rational profiles ($d=1$), $\tau=2B$ suffices,
so $\tau=4$ for $\sin\theta$ and $\tau=40$ for Candidate 007's exact rational profile. In particular every irrational
$\delta$ in
$$U=\{\delta:\ 0<|\delta-a/p|<p^{-p^3}\ \text{for infinitely many admissible }(p,a)\},$$
a dense $G_\delta$ set of Liouville numbers of measure zero, gives radius zero simultaneously for every finite algebraic
profile with nonzero $\sin\theta$ coefficient.

Proof. Write $\delta_0=a/p$ and let $\kappa_p$ be the first compatibility coefficient at $\delta_0$ (Theorem P').
(i) Height. Let $Q\in\mathbb N$ make every $Q\alpha_m$ an algebraic integer. Expand $f_p(\delta_0)$ over ordered binary
trees with $p$ leaves. An internal node of mass $n$ whose velocity child has mass $i$ and stream mode $j$ contributes
the stream factor $\pm p/(2v^\pm_{i,j})$, $v^+_{i,j}=(2j+2)p-ia$, $v^-_{i,j}=(2j-2)p+ia$ (nonzero integers for $i<p$),
one radial factor with numerator an integer and denominator $p$, a trigonometric $\frac12$, integer frequencies and
$1/((n-1)(c_0-1))=(p-a)/(a(n-1))$; so its denominator divides $4a(n-1)v^\pm_{i,j}$. Distinct nodes of equal mass have
disjoint leaf sets, so there are at most $\lfloor p/n\rfloor$ nodes of mass $n$ and at most $\lfloor p/i\rfloor$ velocity
children of mass $i$, with $1\le j\le Bi/2$. Hence $D_p\kappa_p$ is an algebraic integer for
$D_p=Q^p(4a)^{p-1}\prod_{2\le n\le p}(n-1)^{\lfloor p/n\rfloor}\prod_{i<p}\prod_{j\le Bi/2}|v^+_{i,j}v^-_{i,j}|^{\lfloor p/i\rfloor}$.
Since $|v^\pm_{i,j}|\le(B+3)p^2$ and $\sum_{i<p}i\lfloor p/i\rfloor\le\frac{\pi^2}{12}p^2+\frac p2(1+\log p)$,
$\log D_p\le(\frac{B\pi^2}6+o(1))p^2\log p$. By Theorem P', $\kappa_p\ne0$ outside finitely many $p$, so the field norm of
$D_p\kappa_p$ is a nonzero integer; each conjugate $\sigma(\kappa_p)$ is the compatibility coefficient of the conjugate
profile and is at most $(Cp)^p$ by (ii). Therefore $\log(1/|\kappa_p|)\le(\frac{dB\pi^2}6+o(1))p^2\log p$.
(ii) A uniform disk. Fix $\epsilon>0$, centers in $[\epsilon,1-\epsilon]$, $p$ large, $R_p=1/(4p^2)$. On
$|z-\delta_0|\le R_p$ every stream divisor of order $i<p$ has modulus $\ge3/(4p)$, and at order $p$ every divisor has
modulus $\ge1/(4p)$ on the boundary circle; so $\|g_i\|\le4p\|f_i\|$ there, and the scalar recursion (Section 5) gives
$n\|f_n\|\le\frac{112Bp}\epsilon\sum_{i+j=n}i\|f_i\|\,j\|f_j\|$, hence $\|f_n(z)\|\le(Cp)^n$ for $n\le p$ on the disk and
for $n=p+1$ on its boundary, with $C$ depending only on $\epsilon,B,f_1$. Only the mode $j_0=a/2-1$ of $g_p$ has a pole
in the disk, a simple one at $\delta_0$, so $hf_{p+1}(\delta_0+h)$ is holomorphic there and Cauchy's estimate gives
$\|f_{p+1}(\delta_0+h)-\mathrm{Res}_p/h\|\le2(Cp)^{p+1}$ for $|h|\le R_p/2$.
(iii) By Lemma 10.1 the coefficient of $\sin((L+2j_0)\theta)$ in $\mathrm{Res}_p$ is
$-\kappa_pj_0(L+\gamma_0)\alpha_L/(2p^2(c_0-1))$, of modulus $\ge\epsilon^2|\alpha_L||\kappa_p|/(8p)$ once $p\ge4/\epsilon$.
With $dB\pi^2/6<\beta<\tau$, (i) gives $|\kappa_p|\ge p^{-\beta p^2}$, so at $h=\delta-\delta_0$ that coefficient of
$f_{p+1}(\delta)$ is at least $\frac{\epsilon^2|\alpha_L|}8p^{(\tau-\beta)p^2-1}-2(Cp)^{p+1}$, whose $(p+1)$-st root tends to
infinity. The set $U$ is a countable intersection of open dense sets (unions of punctured intervals at centers with
$p>N$), its measure is at most $\sum_{p>N}2p\,p^{-p^3}\to0$, and its elements are Liouville. $\square$

Corollary Q2 (almost every first amplitude, analytic higher modes; PROVED: independent proof, reviewed here and
independently confirmed). Let
$h=\sum_{m\ge3,\ m\ \rm odd}\alpha_m\sin(m\theta)$ be real with $\sum_m|\alpha_m|e^{\sigma_0m}<\infty$ for some
$\sigma_0>0$; $h$ may be an infinite sum, and no algebraicity is assumed. There is a set $E_h\subset\mathbb R$ of Hausdorff
dimension zero, independent of $\delta$ and $\tau$, such that for every $x\notin E_h$ and every $\delta\in(0,1)$ having,
for some $\tau>\pi^2/3$, infinitely many primes $p$ and even $4\le a<p$ with $0<|\delta-a/p|<p^{-\tau p^2}$, the pure
series for $f_1=x\sin\theta+h$ has radius zero in the uniform angular norm.

Proof. (i) At $\delta_0=a/p$ the coefficient $f_p$ is a homogeneous polynomial of degree $p$ in $f_1$, so
$P_{p,a}(x)=[\sin((a-3)\theta)]f_p[x\sin\theta+h]$ is a real polynomial of degree at most $p$ whose $x^p$ coefficient is
the first compatibility coefficient $\kappa^0_{p,a}$ of $\sin\theta$. It is nonzero by Theorem P, and step (i) of the
proof of Theorem Q with $d=1$, $B=2$ gives $|\kappa^0_{p,a}|\ge p^{-(\pi^2/3+\eta)p^2}$ for every $\eta>0$ and all large
$p$, uniformly in $a$. (ii) Write $P_{p,a}=b\prod_{j\le p}(x-z_j)$. If $|P_{p,a}(x)|<|b|r^p$ then $|x-z_j|<r$ for some $j$,
so $\{x\in\mathbb R:|P_{p,a}(x)|<p^{-(\pi^2/3+2\eta)p^2}\}$ is covered by $p$ intervals of radius $p^{-\eta p}$. There are
fewer than $p$ numerators for each $p$, and $\sum_{p>M}p^2(2p^{-\eta p})^s\to0$ as $M\to\infty$ for every $s>0$, so the
set of $x$ lying in infinitely many of these sets has Hausdorff dimension zero. Let $E_h$ be $\{0\}$ together with the
union of these limsup sets over $\eta=1/m$, $m\in\mathbb N$. For $x\notin E_h$ and every $\eta=1/m$,
$|P_{p,a}(x)|\ge p^{-(\pi^2/3+2\eta)p^2}$ for all large admissible $(p,a)$. (iii) Step (ii) of Theorem Q holds for the
analytic profile on shrinking strips $\sigma_n=\sigma_0-(n-1)\sigma_0/(2p)$, where an angular derivative costs
$2p/\sigma_0$ and the stream inverse costs $4pe^{\sigma_0}$ at every frequency; the scalar recursion becomes
$Y_n\le Kp^3\sum_{i+j=n}Y_iY_j$ with $K=112e^{\sigma_0}/(\epsilon\sigma_0)$, so $\|f_n(z)\|_{\sigma_n}\le(Cp^3)^n$ on the
disk ($n\le p$) and on its boundary ($n=p+1$), and Cauchy's estimate gives
$\|f_{p+1}(\delta_0+w)-\mathrm{Res}_{p,a}/w\|_{\sigma_0/2}\le2(Cp^3)^{p+1}$ for $|w|\le R_p/2$. (iv) With $j=a/2-1$ and
$\gamma_0=1-a/p$, the pole part of $g_p$ is $\kappa/(2pw)\sin(2j\theta)$ with $\kappa=P_{p,a}(x)$, and $P_p=-2j$, $p_1=\gamma_0$
give
$$\mathrm{Res}_{p,a}=-\frac{P_{p,a}(x)\,j}{p^2(c_0-1)}\big(\sin(2j\theta)f_1'+\gamma_0\cos(2j\theta)f_1\big),$$
whose $\sin((2j+1)\theta)$ coefficient is $\frac12\big((1+\gamma_0)x-(4j+1-\gamma_0)\alpha_{4j+1}\big)$ (only the input
frequencies $1$ and $4j+1$ contribute). Since $(4j+1)\alpha_{4j+1}\to0$ this has modulus at least $|x|/4$ for large $j$,
and with $j\ge\epsilon p/4$, $1/(c_0-1)\ge\epsilon$, the coefficient of $\sin((2j+1)\theta)$ in $f_{p+1}(\delta)$ has modulus
at least $\frac{\epsilon^2|x|}{16}p^{(\tau-\pi^2/3-2\eta)p^2-1}-2(Cp^3)^{p+1}$ once $\pi^2/3+2\eta<\tau$. Its $(p+1)$-st
root tends to infinity, and a sine amplitude is at most twice the uniform norm. $\square$

Corollary Q2 replaces the algebraicity of Theorem Q by a dimension-zero exceptional set of first amplitudes, and its
threshold $\pi^2/3$ does not depend on the higher modes. For example, for Candidate 007's higher modes $h$ (the
$\sin3\theta,\dots,\sin19\theta$ part of its profile) the threshold is $\pi^2/3$ for every first amplitude outside
$E_h$, against $\tau>40$ from Theorem Q for the stored profile itself. Checks: exact $\mathbb Q[x]$ computations with
$f_1=x\sin\theta+\sin3\theta$ confirm degree $p$ and the leading coefficient $\kappa^0_{p,a}$ at the tested centers, and
the residue amplitude was checked in exact Cartesian arithmetic for finite test profiles.

Theorem Q makes the divergence of Theorem C* explicit and uniform in the profile, but its approximation exponent is of
order $p^2\log p$, far beyond failure of the Brjuno condition; the gap between the two is OPEN. Section 10.5 locates it.

### 10.5 Where the gap to the Brjuno condition sits (PROVED: independently confirmed, for centers in a compact interval)

The approximation exponent $\tau p^2$ of Theorem Q comes only from step (i), the height lower bound
$|\kappa_p|\ge p^{-\beta p^2}$ for the first compatibility coefficient. Steps (ii) and (iii) give the following
statement with the actual size of $\kappa$.

Proposition 10.5. Let $f_1$ be a finite real odd sine polynomial with top frequency $L$ and $\alpha_L\ne0$ (no
algebraicity and no condition on $\alpha_1$), and let $\delta\in(0,1)$ be irrational. For a prime $p$ and an even
$4\le a<p$ let $\kappa_{p,a}$ be the coefficient of $\sin((a-3)\theta)$ in $f_p(a/p)$ (the first compatibility
coefficient). Suppose that for some $\eta>0$ and some compact interval $J\subset(0,1)$ there are infinitely many such
$(p,a)$ with $a/p\in J$ and
$$0<|\delta-a/p|<|\kappa_{p,a}|\,p^{-(1+\eta)p}.$$
Then $\limsup_n\|f_n(\delta)\|_{\ell^1}^{1/n}=\infty$. Consequently, if for some compact $J\subset(0,1)$ containing
$\delta$ in its interior there are $\mu>0$ and $p_0$ with $|\kappa_{p,a}|\ge\mu^p$ whenever $a/p\in J$ and $p\ge p_0$
(hypothesis $(H_\kappa)$), the series has radius zero at every irrational $\delta$ with
$0<|\delta-a/p|<p^{-(1+\eta)p}$ for infinitely many such $(p,a)$ and some $\eta>0$.

Proof. Take $\epsilon>0$ with $J\subset[\epsilon,1-\epsilon]$. Step (ii) of Theorem Q uses no arithmetic of the coefficients: with
$R_p=1/(4p^2)$ and $C=C(\epsilon,B,f_1)$ it gives $\|f_n(z)\|\le(Cp)^n$ on $|z-a/p|\le R_p$ for $n\le p$ (in particular
$|\kappa_{p,a}|\le(Cp)^p$ at every center in $J$) and $\|f_{p+1}(a/p+h)-\mathrm{Res}_p/h\|\le2(Cp)^{p+1}$ for $0<|h|\le R_p/2$. Step (iii)
(Lemma 10.1) gives a coefficient of $\mathrm{Res}_p$ of modulus $\ge\epsilon^2|\alpha_L||\kappa_{p,a}|/(8p)$ for
$p\ge4/\epsilon$. Put $h=\delta-a/p$. Since $|h|<|\kappa_{p,a}|p^{-(1+\eta)p}\le C^pp^{-\eta p}<R_p/2$ for large $p$
(here the bound on $\kappa$ is used before it is known that the centers approach $\delta$), the
same coefficient of $f_{p+1}(\delta)$ has modulus at least
$$\frac{\epsilon^2|\alpha_L|}8\,p^{(1+\eta)p-1}-2(Cp)^{p+1},$$
and the ratio of the second term to the first is $O(C^{p+1}p^{2-\eta p})\to0$. So $\|f_{p+1}(\delta)\|_{\ell^1}\ge
\frac{\epsilon^2|\alpha_L|}{16}p^{(1+\eta)p-1}$ for infinitely many $p$, whose $(p+1)$-st root tends to infinity. The
consequence follows since such centers tend to $\delta$, hence eventually lie in $J$, and
$|\kappa_{p,a}|p^{-(1+\eta')p}\ge p^{-(1+\eta)p}$ for $\eta'<\eta$ and large $p$. $\square$

Without the compact interval $J$ the statement is OPEN: the constant in $|\kappa_{p,a}|\le(Cp)^p$ depends on the
distance of $a/p$ from $0$ and $1$ through the stationary inverse $1/((n-1)(c-1))$ (near $a/p=4/p$ the same argument
gives only a bound of the form $(Cp^2)^p$), so far centers with very large $\kappa_{p,a}$ are not excluded.

So the gap between Theorem Q and the Brjuno condition is a quantitative lower bound on the first compatibility
coefficient. Theorems P and P' give only $\kappa_{p,a}\ne0$ (reduction modulo $p$), and the height argument converts this
into $p^{-\beta p^2}$. Under $(H_\kappa)$ the divergence condition becomes $|\delta-a/p|<p^{-(1+\eta)p}$, which in
terms of the continued fraction of $\delta$ is roughly $\log q_{k+1}\ge(1+\eta)q_k\log q_k$ infinitely often, against the
failure of $\sum_k\log(q_{k+1})/q_k<\infty$ for non-Brjuno numbers. A gap would remain (a single large term against a
divergent sum, and the factor $\log q_k$, which comes from the crude divisor bound $1/(4p)$ in step (ii)).

Data (NUMERICAL EVIDENCE for $(H_\kappa)$, $f_1=\sin\theta$). The exact values of $\kappa_{p,a}$ at all 122 pairs
$(p,a)$ with $p$ prime, $7\le p\le61$ (15 primes), and even $a$ with $a/p\in(0.25,0.75)$ satisfy
$-1.01\le\log_{10}|\kappa_{p,a}|/p\le-0.21$ (certified extremes $-1.00818$ at $(11,8)$ and $-0.21361$ at $(61,16)$); the mean over $a$
at fixed $p$ rises slowly, from $-0.93$ at $p=7$ to $-0.51$ at $p=61$, and the minimum over $a$ stays between $-1.01$ and
$-0.82$. The height bound of Theorem Q only guarantees $\log_{10}|\kappa|\ge-(\pi^2/3)p^2\log_{10}p$, about $-2\cdot10^4$
at $p=61$, against the observed $\ge-62$. These are finite computations; $(H_\kappa)$ is CONJECTURAL.

Remark (the endpoint $\delta\to0$; PROVED: independent proof, reviewed here, with a numerical check here). For
$f_1=\sin3\theta$ the pure coefficients are rational in $\delta$ at each fixed order, and coefficientwise
$f_n=\delta^{-2n+2}H_n+O(\delta^{-2n+3})$, $g_n=\delta^{-2n+1}\frac{[\sin3\theta]H_n}{2n}\sin2\theta+O(\delta^{-2n+2})$, because the only
Poisson denominator vanishing at $\delta=0$ is $m-P_n=n\delta$ at $m=2$. The leading terms obey
$(n-1)H_n=\sum_{i+j=n}\frac{[\sin3\theta]H_i}{i}(\sin2\theta\,\partial_\theta-\cos2\theta)H_j$, so $H=\sum_nH_nx^{n-1}$ is
$H=\exp(u(\sin2\theta\,\partial_\theta-\cos2\theta))\sin3\theta$ with $(xu')'=[\sin3\theta]H$. The flow is explicit in $w=\tan\theta$,
and with $v=\tanh u$ and $1/(\cosh2u-\sinh2u\cos2\theta)=1+2\sum_{j\ge1}v^j\cos2j\theta$ one finds
$[\sin3\theta]H=\operatorname{sech}^3u$, hence $u=\operatorname{arsinh}x$ and
$$H=e^u\sin\theta\Big[-1+\frac{4\cos^2\theta}{\cos^2\theta+e^{4u}\sin^2\theta}\Big],\quad
[\sin3\theta]H=(1+x^2)^{-3/2},\quad [\sin\theta]H=-\frac{x^2}{\sqrt{1+x^2}}-\frac{x(2+x^2)}{1+x^2}.$$
So for odd $n=2k+1\ge3$, $\lim_{\delta\to0}\delta^{2n-2}[\sin\theta]f_n=(-1)^k\binom{2k-2}{k-1}4^{1-k}\ne0$. At $\delta=4/p$ the
first compatibility coefficient is $\kappa_{p,4}=[\sin\theta]f_p$; as a rational function of $\delta$ it has a pole of exact
order $2p-2$ at $\delta=0$, with a leading coefficient that is only polynomially small in $p$. This is why the bound for
compact $J$ cannot be continued to the endpoint. It is a fixed-order statement: the remainder is not uniform in $n$, so
it gives no estimate of $\kappa_{p,4}$ itself as $p\to\infty$. Check here (accompanying artifacts): at $\delta=10^{-12}$,
$\delta^{2n-2}[\sin\theta]f_n$ equals $-1,\frac12,-\frac38,\frac5{16}$ at $n=3,5,7,9$ and $\delta^{2n-2}[\sin3\theta]f_n$ equals
$-\frac32,\frac{15}8,-\frac{35}{16},\frac{315}{128}$ (the coefficients of $(1+x^2)^{-3/2}$) to ten digits.

Status. PROVED for the statement with the compact interval $J$ and for the consequence under $(H_\kappa)$: complete
proof written here and independently confirmed (with an independent write-up of the localized form); the extreme data
values are independently certified.

### 10.6 Density and stream growth are equivalent at every irrational $\delta$; divergence along almost every ray (PROVED: independent proof, reviewed here and independently confirmed)

Proposition 10.6. Let $\delta\in(0,1)$ be irrational, $c=1/(1-\delta)$, and let $f_1\ne0$ be a finite real odd sine
polynomial with top frequency $L$; put $B=L+1$, $M_n=\|f_n\|_0$, $N_n=\|g_n\|_0$ for the pure coefficients
($\rho_n=r^{1-n\delta}f_n$, $\psi_n=r^{2-n\delta}g_n$, common potential $\chi_n=r^{4-n\delta}h_n$). No arithmetic condition
on $\delta$ is assumed. The following are equivalent:
1. $M_n\le CA^n$ for some $C,A$;
2. $N_n\le CA^n$ for some $C,A$;
3. the density, stream and potential series converge on some exterior $r\ge R$, absolutely and uniformly with every
   fixed weighted Cartesian derivative, and their sums solve the stationary equation there;
4. at some radius $r_0>0$ the individual density terms are bounded on a measurable set of angles of positive length;
5. the same as 4 for the stream terms, or for the radial-velocity terms, or for the potential terms.

If they fail, there is a set $\Theta$ of angles of full measure, which is also residual in the circle, such that for
every $\theta\in\Theta$ and every $r>0$ the individual terms of the density, stream, radial-velocity and potential
series are unbounded. In particular this holds at every divergent parameter of Theorem C, Section 10.3 and Section 10.4
(all of them have $\limsup_n M_n^{1/n}=\infty$).

Proof. With $E=B(3-\delta)$, the recursion (R) and the bounds $|P_i|\le(2-\delta)i$, $|p_j|\le j$ give
$\|P_ig_if_j'-p_jg_i'f_j\|\le E\,ij\,N_iM_j$ in the plain norm and in every weight $\|v\|_\rho=\sum_m|v_m|\rho^m$, $\rho\ge1$.

2 implies 1. If $N_i\le HA_0^i$, then $Y_n=nM_n$ satisfies $Y_n\le K\sum_{i=1}^{n-1}iA_0^iY_{n-i}$ with
$K=2EH/(c-1)$. Let $y_*\in(0,1)$ solve $Ky_*=(1-y_*)^2$; then $K\sum_iiy_*^i=1$ and induction gives
$Y_n\le M_1(A_0/y_*)^{n-1}$ (the linear renewal of Section 14.17 with no logarithms).

1 implies 2. Write $f_1=\sum_{k\le L}a_k\sin k\theta$ and choose $\rho\ge4$ with
$S=\sum_{k<L}|a_k|\rho^k/(|a_L|\rho^L)\le1/16$; put $T=|a_L|\rho^L/2$. For $i\delta\ge16$, $a=i\delta-2$ and $p=1-\delta$,
the operator $\mathcal L_ig=-agf_1'-pf_1g'$ (the pair $(i,1)$ of (R) at order $i+1$) satisfies
$\|\mathcal L_ig\|_\rho\ge\frac{223}{256}T[La\|g\|_\rho+p\|g'\|_\rho]\ge\frac{TL\delta i}8\|g\|_\rho$: the $k=L$ upper
contributions $-a_Lg_m(La+pm)/2$ sit at the distinct indices $m+L$, and all other contributions carry at most
$\rho^{-2}+S(1+\rho^{-2})\le33/256$ of that weight (this is Section 14.19 with $D=0$; there is no small denominator,
since $m$ is even and $L$ odd). Isolating $\mathcal L_ig_i$ at order $i+1$, with $X_n=\|f_n\|_\rho\le\rho^{Bn}M_n$ and
$Y_i=\|g_i\|_\rho\ge N_i$,
$$Y_i\le\alpha c\delta\,X_{i+1}+\alpha E\sum_{k+j=i+1,\,k<i}jY_kX_j,\qquad\alpha=\frac8{TL\delta}.$$
If $M_n\le CA^n$, put $A_*=\max(1,A\rho^B)$, $K_*=\alpha ECA_*$, and choose $H_*\ge\alpha c\delta CA_*$ (this bounds the
forcing term, since $\alpha c\delta X_{i+1}\le\alpha c\delta CA_*\,A_*^i$) and also $H_*\ge Y_i/A_*^i$ for the finitely many $i$ with
$i\delta<16$. Then $Y_i\le H_*A_*^i+K_*\sum_{l=1}^{i-1}(l+1)A_*^lY_{i-l}$ for all $i$, and with
$A_2=A_*\max(4,8K_*)$, $y=A_*/A_2\le1/4$, the mass is $K_*y(2-y)/(1-y)^2\le4K_*y\le1/2$, so $Y_i\le2H_*A_2^i$.

1 and 2 imply 3. For $X=n\delta\ge20$ and $q=4-X$, $V_n$ defined by $\partial_y\chi_n=r^{q-1}V_n$ satisfies the Euler
identity $(q-1)(q-2)V_n=\cos\theta\,P_ng_n+\sin\theta\,g_n'-\sin^2\theta\,f_n$ (substitute
$g_n=(q-1)\cos\theta V_n-\sin\theta V_n'$ and $(q-1)^2V_n+V_n''=-f_n$), so
$\|V_n\|_0\le\frac{16}{X^2}[M_n+n(B+\delta)N_n]$. Solving $\partial_y(r^qh_n)=r^{q-1}V_n$ downward in the cosine
coefficients ($-v_0=2xc_0+(1-x)c_1$, $-v_m=(m+x)c_m+(m+1-x)c_{m+1}$, $x=-q/2\ge8$) gives $\|h_n\|_0\le3\|V_n\|_0$, so
$\|h_n\|_0\le\frac{48}{X^2}[M_n+n(B+\delta)N_n]$. All three coefficient norms are geometric; for $AR^{-\delta}<1$ the
series and each fixed weighted derivative (cost polynomial in $n$) converge uniformly on $r\ge R$, Cauchy products and
differentiation are justified, and the sums solve the equation. 3 implies 4 trivially.

4 or 5 implies 1 or 2. If $|r_0^{\beta-n\delta}v_n(\theta)|\le J$ for all $n$ on a set of angles of length $\eta>0$
(after shrinking to such a $J$), with $v_n$ of frequency at most $Bn$, the trigonometric interpolation bound of
Section 14.18 gives $\|v_n\|_0\le Jr_0^{-\beta}[r_0^{\delta}(16\pi e/\eta)^{2B}]^n$. Take $\beta=1$, $v_n=f_n$ (density);
$\beta=2$, $v_n=g_n$ (stream); $\beta=1$, $v_n=-g_n'$ with $\|g_n'\|_0\ge2N_n$ (radial velocity); $\beta=4$, $v_n=h_n$
with $N_n\le Cn^2\|h_n\|_0$ (two Cartesian derivatives) for the potential.

Exceptional set. If 1 fails, for each integer radius $k\ge1$ and each of the four fields the set
$\bigcup_J\bigcap_n\{\theta:|u_n(k,\theta)|\le J\}$ is a countable union of closed sets, null by the previous step,
hence each closed piece has empty interior. Let $\Theta$ be the complement of the union over $k$ and the four fields.
For $\theta\in\Theta$ and $r\le k$, $u_n(r,\theta)=(r/k)^\beta(k/r)^{n\delta}u_n(k,\theta)$ with $(k/r)^{n\delta}\ge1$, so the
terms are unbounded at every $r>0$. $\square$

Remarks. 1. Theorem A gives 1 for Brjuno $\delta$; Proposition 10.6 does not give convergence at any non-Brjuno
parameter. It says that the small divisors of the Poisson inverse cannot destroy geometric boundedness of the stream when the
generated density coefficients have a geometric bound: the stream at order $i$ is controlled through the density at
order $i+1$, not through the Poisson inverse. (The two geometric bases may differ; no ordering of them is asserted.) 2. The
divergence statements of Sections 10 to 10.4 (unbounded sup norms on one circle) are thereby strengthened to divergence
at every radius along almost every ray. $\Theta$ may depend on $\delta$ and $f_1$; no common set over parameters is
asserted. 3. The same argument at rational $\delta$, with the logarithms, is Sections 14.17 to 14.19.

Status. PROVED (written independently, reviewed here line by line, and independently confirmed).

## 11. Gevrey fallback

Superseded for Brjuno $\delta/2$ by Theorem A. For the record, an independent proof (PROVED; independently confirmed) gives a
Gevrey-one bound at $\delta=1/\sqrt5$, $\|f_n\|_\sigma\le FD^{n-1}(n-1)!$, with an exponentially small residual for
optimal truncation. For non-Brjuno irrational $\delta$ an analogous Gevrey bound with a growth rate depending on the
approximation exponent is expected (OPEN).

## 12. Exterior versus global

1. The convergent potential of Theorem A defines a legitimate exterior stream function and velocity on $r>R_0$ (Theorem A
   item 4). This is the exterior theorem.
2. Canonical velocity (PROVED: independent proof, reviewed here and independently confirmed). Let $\chi_{\rm ext}$ be the convergent exterior potential
   of Theorem A or A' on $r>R_0$, so $|D^j\chi_{\rm ext}|\le C_jr^{\gamma+3-j}$ for $r\ge R_1>R_0$. Take a smooth radial
   cutoff $\eta$ equal to $0$ on $r\le R_1$ and $1$ on $r\ge R_2$, and put $\chi=\eta\chi_{\rm ext}$, $\rho=-\partial_y\Delta\chi$,
   $\psi=\chi_{xy}$, $u=(-\psi_y,\psi_x)$. Then $(\rho,u)$ is a smooth S1 whole-plane pair with $\rho=O(r^\gamma)$,
   $-\Delta\psi=\partial_x\rho$ on $\mathbb R^2$, $\psi=O(r^{\gamma+1})=o(r^2)$, equal to the exterior solution on
   $r\ge R_2$; so its stationary residual is supported in $r\le R_2$. Moreover $\psi$ is the canonical stream: any two
   smooth solutions of $-\Delta\psi=\partial_x\rho$ that are odd in $x$ and in $y$ and $o(r^2)$ differ by a harmonic
   function of growth $o(r^2)$, which is affine, and an affine function odd in both variables vanishes. (The same
   function is given by the symmetrically regularized Green integral.) For any other smooth S1 interior extension
   $\tilde\rho$ that agrees with $\rho$ on $r\ge R_2$, the canonical stream differs from the series stream on $r>R_2$ by
   a harmonic S1 function that is $o(r^2)$, i.e. $\sum_{j\ge1}\beta_jr^{-2j}\sin(2j\theta)$, with
   $\beta_j=-\frac1{2\pi}\int\operatorname{Im}((y_1+iy_2)^{2j-1})\,(\tilde\rho-\rho)(Y)\,dY$ (moments of the difference
   from the cutoff extension, not of $\tilde\rho$ alone). So the canonical-velocity requirement is not an obstruction
   to extending the exterior solution; stationarity inside the disk is the open part.
3. Compatibility with the exponent sequence. A multipole $r^{-2j}\sin(2j\theta)$ has stream exponent $-2j$, which equals
   $P_n$ only at resonance. For irrational $\delta$ it opens new exponent channels: nonlinear interactions with the
   density produce density exponents $p_n-2m$, and the general exterior solution is a double series in
   $(r^{-\delta},r^{-2})$ (the exponents recorded in the residual of Candidate 007 indeed include $p_n$ and $p_n-2$).
4. Effect on the proof. At density exponent $s=p_n-2m$ the linear coefficient is $cs-1=-(n-1)(c-1)-2mc$ and the Poisson
   denominators are $4j^2-(2-n\delta-2m)^2$, which are small exactly when $d_n$ is small. So the double series has the
   same small divisors and the same Cauchy-Kovalevskaya structure. Theorem M (Section 12.1) extends Theorem A to this
   double series at every Brjuno $\delta$, with arbitrary geometrically bounded prescribed multipoles.
5. A global stationary solution (an interior extension whose residual vanishes in the disk as well) is OPEN; by item 2
   the canonical-velocity condition is not the obstacle.
6. Exterior solutions without convergence: Theorem S (Section 12.2) gives exterior solutions with the truncated series
   as asymptotic expansion for every $c>1$ and every $N$, on an exterior that depends on $N$.

### 12.1 Theorem M: exterior solutions with prescribed harmonic multipoles (PROVED: independent proof, reviewed here and independently confirmed)

Theorem M. Let $\delta\in(0,1)$ with $\alpha=\delta/2$ a Brjuno number, $c=1/(1-\delta)$, $f\ne0$ a real odd sine polynomial
with top frequency $L$, $B=L+1$, $F=\|f\|_0$, and let $h_k\in\mathbb R$ ($k\ge2$) satisfy
$H(Y_0)=\sum_{k\ge2}k|h_k|Y_0^k<\infty$ for some $Y_0>0$. For a density index $I=(n,k)$, $n\ge1$, $k\ge0$, put
$\mu_I=n\delta+2k$, $p_I=1-\mu_I$, $P_I=2-\mu_I$, $w_I=n+k$; the stream index $(0,k)$, $k\ge2$, carries the prescribed
harmonic term $G_{0,k}=h_k\sin((2k-2)\theta)$ with $P_{0,k}=2-2k$. Define $F_{1,0}=f$, the generated stream $G_I$ of every
density index by the Poisson inverse (B) with $P_n$ replaced by $P_I$, and for $w_I\ge2$
$$c(\mu_I-\delta)F_I=\sum_{A+D=I}\big[P_AG_AF_D'-p_DG_A'F_D\big],\tag{M}$$
where $D$ runs over density indices and $A$ over density indices and the multipole indices $(0,k)$. Then there are
$X,Y>0$ such that
$$\rho=\sum_{n\ge1,k\ge0}r^{1-n\delta-2k}F_{n,k},\qquad
\psi=\sum_{n\ge1,k\ge0}r^{2-n\delta-2k}G_{n,k}+\sum_{k\ge2}h_kr^{2-2k}\sin((2k-2)\theta)$$
converge absolutely, with all Cartesian derivatives after removal of their radial weights, on $r\ge R$ whenever
$R^{-\delta}<X$, $R^{-2}<Y$. The sums are real-analytic, satisfy $-\Delta\psi=\partial_x\rho$ and
$(cX+u)\cdot\nabla\rho=\rho$ with $u=(-\psi_y,\psi_x)$, come from the potential
$\chi=\sum r^{4-n\delta-2k}C_{n,k}-h_2\log r+\sum_{k\ge3}h_kr^{4-2k}\cos((2k-4)\theta)/((2k-4)(2k-3))$ (so
$\rho=-\partial_y\Delta\chi$, $\psi=\chi_{xy}$), and $\rho=r^\gamma(f+o(1))$. One can take
$X=1/(16KF_*)$ and any $Y<Y_0$ with $H(Y)<1/(16K)$, where $K=14B/(c-1)$ (a constant of this theorem, not the $K$ of Theorem A), $C_P=(1+\delta^{-1})/2$ and
$F_*=2C_Pe^{2\mathcal B(\alpha)}F$.

Remarks. (a) The prescribed multipoles force density corrections: for $f=\sin\theta$,
$F_{1,2}=-h_2[\delta\sin\theta+(1+\gamma)\sin3\theta]/(4c)$ (checked by hand from (M) and by an independent exact
computation). (b) No index $(n,1)$ occurs ($F_{n,1}=G_{n,1}=0$), and all exponents $\mu_I$ are distinct because $\delta$
is irrational, so no logarithms appear in density or stream. (c) By Section 12 item 2, changing the interior density
changes the exterior canonical stream by multipoles of exactly this form, and the exterior equation then requires a
corrected density. Theorem M shows that for all geometrically bounded multipole data the corrected exterior problem
still has a convergent series solution; this is the family that a matching with a nontrivial interior would have to
use. Whether a given interior realizes given multipoles, and whether the interior residual can be made zero, is not
addressed.

Proof. (1) Recursion. The linear stationary coefficient of $r^{p_I}F_I$ is $cp_I-1=-c(\mu_I-\delta)$ (as $c-1=c\delta$), and
$u\cdot\nabla\rho$ for $\psi=r^{P_A}G_A$, $\rho=r^{p_D}F_D$ is $r^{P_A+p_D-2}(P_AG_AF_D'-p_DG_A'F_D)$, of exponent $p_{A+D}$;
this gives (M). Since $c(\mu_I-\delta)=(c-1)(n-1)+2kc\ge(c-1)(w_I-1)$, (M) determines $F_I$ for $w_I\ge2$ by induction on $w$.
The Poisson denominators are $2j+P_I=2j+2-2k-n\delta$, nonzero for irrational $\delta$, and $2j-P_I\ge\mu_I\ge n\delta$.
Supports: $\deg F_I\le Bn+2k-1$, $\deg G_I\le Bn+2k$.
(2) Divisors. Each input coefficient enters (B) through two channels, of sizes at most $1/(2d_n)$ and $1/(2n\delta)$
($|2j+P_I|\ge\operatorname{dist}(n\delta,2\mathbb Z)=d_n$ because $2k$ is even), so
$\|G_I\|_0\le C_P\|F_I\|_0/d_n$, uniformly in $k$.
(3) Scalar inequality. With $Z_I=w_I\|F_I\|_0$, $U_I=w_I\|G_I\|_0$ for density indices and $U_{0,k}=k|h_k|$, the bounds
$|P_A|\le4w_A$, $|p_D|\le3w_D$, $\deg G_A\le Bw_A$, $\deg F_D\le Bw_D$ (for $(0,k)$: $|P_A|=2k-2$, $\deg G_A=2k-2$),
the Wiener algebra inequality and $w_I/(w_I-1)\le2$ give $Z_I\le K\sum_{A+D=I}U_AZ_D$.
(4) Marked trees. Iterating, $Z_I$ is bounded by a sum over plane binary trees whose right children are density subtrees
and whose left children are density subtrees (used through (2)) or multipole leaves. A tree with $n$ density leaves and
$s$ multipole leaves has $n+s-1$ interactions and contributes $K^{n+s-1}C_P^{\,n-1}F^n\prod_{\rm leaves}k|h_k|$ times
$\prod_v d_{n_v}^{-1}$, the product over the $n-1$ marked vertices (roots of left density subtrees; $n_v$ the number of
density leaves below $v$). The divisor sits only at generated velocity children, not at every density vertex. If a
marked $v$ lies strictly below a marked $u$, then $v$ is the left child of a vertex at or below $u$ whose right child
contains a density leaf, so $n_u>n_v$. This strict monotonicity is what the counting of Section 6 uses: with
$S_j=\{m\ge1:\|m\alpha\|<1/(4q_j)\}$, whose elements are $\ge q_j$ and pairwise at distance $\ge q_j$, the marked vertices
with mass in $S_j$ number at most $2n/q_j$ (assign to each such vertex the density leaves below it but not below its
marked $S_j$-descendants; zero-mass multipole leaves do not enter). Hence
$\prod_vd_{n_v}^{-1}\le2^{M}e^{2n\mathcal B(\alpha)}$ for $M$ marks. The same holds with one more mark at the root
(it has mass $n$, larger than every marked descendant), which bounds $Z_I/d_n$ and $U_I$.
(5) Majorant. Every tree weight is at most its weight in $W=F_*x+H(y)+KW^2$ (here $C_P\ge1$ is used), whose solution
$W=(1-\sqrt{1-4K(F_*x+H(y))})/(2K)$ has nonnegative coefficients and is analytic near the closed polydisc
$|x|\le X$, $|y|\le Y$, since $F_*X+H(Y)<1/(8K)$. Therefore $w_I\|F_I\|_0$, $w_I\|F_I\|_0/d_n$ and $w_I\|G_I\|_0$ are all
at most $[x^ny^k]W$, and $\sum_IX^nY^k[x^ny^k]W=W(X,Y)<\infty$.
(6) Potential. Lemma 7.1 holds verbatim with $n\delta$ replaced by $\mu_I$, since every distance from $\mu_I$ to an even
integer is at least $d_n$: $\|C_I\|_0\le(3/|4-\mu_I|+1)\|F_I\|_0/d_n$ for $\mu_I\ge3$, and only finitely many $(n,k)$ have
$\mu_I<3$ or $|4-\mu_I|<1$, each with an invertible finite potential matrix. The multipole potentials are checked
directly: $\partial_{xy}(-\log r)=r^{-2}\sin2\theta$, and $\partial_{xy}\operatorname{Re}(z^{-m})=m(m+1)r^{-m-2}\sin((m+2)\theta)$
with $m=2k-4$; they have zero density.
(7) Exterior sums. The weighted terms are $r^{-\gamma}\rho_I=x^{n-1}y^kF_I$ and $r^{-\gamma-1}\psi_I=x^{n-1}y^kG_I$ with
$x=r^{-\delta}$, $y=r^{-2}$. Derivatives cost polynomial factors in $w_I$, absorbed by the margin in $(X,Y)$; a small
angular strip is obtained in the same way, which gives real analyticity. The stationary series converges absolutely, so
it can be regrouped by $(n,k)$, and each group vanishes by (M). $\square$

Status. The proof is the independent one on prescribed multipoles; each step above was
checked here. The finite checks (exact mixed-index coefficients in two rational and two $\mathbb Q(\sqrt5)$ cases, the
marked-count and strict-ancestry property on all 10879 tree shapes with at most 8 leaves) are independently confirmed.
The all-order theorem is independently confirmed.

Theorem M' (analytic profiles; PROVED: independent proof, reviewed here and independently confirmed). Let $\delta$,
$c$, the prescribed $h_k$ and the recursion (M) be as in Theorem M, but let $f$ be a real odd sine series with
$F=\|f\|_{\sigma_0}<\infty$ for some $\sigma_0>0$ (Wiener norm $\|a\|_\sigma=\sum_m|\hat a(m)|e^{\sigma|m|}$). Let
$H_0(y)=\sum_{k\ge2}k|h_k|y^k$ have radius $\rho_0>0$, and put (constants local to this theorem)
$$C_P=\tfrac12(1+\delta^{-1}),\quad\Lambda=1+2C_P=2+\delta^{-1},\quad K=\frac{2e^{\sigma_0}\Lambda(1+2\sigma_0)}{c-1},\quad
F_*=2e^{2\mathcal B(\alpha)}F,$$
$$H(y)=\sum_{k\ge2}k|h_k|\sigma_0^{k-1}e^{(2k-2)\sigma_0}y^k=\frac{e^{-2\sigma_0}}{\sigma_0}H_0(\sigma_0e^{2\sigma_0}y),$$
$X=1/(16KF_*)$, and choose $Y>0$ with $\sigma_0e^{2\sigma_0}Y<\rho_0$ and $H(Y)<1/(16K)$. Then all conclusions of
Theorem M hold on $r\ge R$ whenever $R^{-\delta}<\frac{\sigma_0}2X$ and $R^{-2}<\frac{\sigma_0}2Y$; the angular
coefficients of the sums are analytic in a strip.

Proof. (1) Stream estimates without finite support. In (B) with $P_I$ in place of $P_n$, the two channels have
denominators $|2j+P_I|\ge d_n$ (because $\mu_I-n\delta$ is even) and $2j-P_I\ge n\delta\ge\delta d_n$, and a frequency
shift by one costs $e^\sigma$, so $\|G_I\|_\sigma\le e^{\sigma_0}C_P\|F_I\|_\sigma/d_n$. For the angular derivative,
$m\le|m+P_I|+|P_I|$ and $m\le(m-P_I)+|P_I|$ give, per input coefficient, at most
$e^\sigma[1+|P_I|(1/d_n+1/(n\delta))/2]\le e^{\sigma_0}\Lambda w_I/d_n$ (using $|P_I|\le2w_I$, $d_n\le1$, $n\ge1$). Hence
$$\max\big(|P_I|\,\|G_I\|_\sigma,\ \|\partial_\theta G_I\|_\sigma\big)\le e^{\sigma_0}\Lambda\,w_I\|F_I\|_\sigma/d_n .$$
(2) Shrinking strips. With $s=\sigma_0-\sigma$ let $\nu_I=\sup_{0\le\sigma<\sigma_0}s^{w_I-1}\|F_I\|_\sigma$ and
$\nu_{0,k}=|h_k|\sigma_0^{k-1}e^{(2k-2)\sigma_0}$. The Nagumo lemma of Section 7.2 gives $\|F_D'\|_\sigma\le w_D\nu_Ds^{-w_D}$.
The prescribed mode has frequency $|P_{0,k}|=2k-2$, so $\max(|P_A|\|G_A\|_\sigma,\|G_A'\|_\sigma)\le2k\nu_{0,k}s^{-(k-1)}$
(as $s\le\sigma_0$). In (M) the term $P_AG_AF_D'$ has strip power $s^{-(w_I-1)}$ and the term $p_DG_A'F_D$ (with
$|p_D|\le2w_D$) has $s^{-(w_I-2)}$; bounding the extra $s$ by $\sigma_0$ and using $c(\mu_I-\delta)\ge(c-1)(w_I-1)$,
$$(c-1)(w_I-1)\nu_I\le e^{\sigma_0}\Lambda(1+2\sigma_0)\sum_{A+D=I}\frac{w_Aw_D\nu_A\nu_D}{e_A},$$
with $e_A=d_{n_A}$ for a generated stream child and $e_A=1$ for a prescribed one. With $Z_I=w_I\nu_I$,
$Z_{0,k}=k\nu_{0,k}$ and $w_I/(w_I-1)\le2$ this is $Z_I\le K\sum_{A+D=I}Z_AZ_D/e_A$, with $Z_{1,0}=F$.
(3) Trees. The divisors sit at the generated stream children only, exactly as in step (4) of Theorem M; there are no
factors $C_P$ at internal nodes, because $K$ contains the stream constants. The marked-tree bound gives
$w_I\nu_I\le[x^ny^k]W$ and $w_I\nu_I/d_n\le[x^ny^k]W$ for the solution of $W=F_*x+H(y)+KW^2$, which is analytic near the
closed polydisc $|x|\le X$, $|y|\le Y$ since $F_*X+H(Y)<1/(8K)$. By (1),
$w_I\sup_\sigma s^{w_I-1}\|G_I\|_\sigma\le e^{\sigma_0}C_P[x^ny^k]W$.
(4) Summation. At $\sigma=\sigma_0/2$ the weighted density terms $x^{n-1}y^k\|F_I\|_{\sigma_0/2}$ ($x=r^{-\delta}$,
$y=r^{-2}$) are bounded by the coefficients of $(s/x)W(x/s,y/s)$, $s=\sigma_0/2$. Every density index has $n\ge1$, so it
suffices to bound at $r=R$, and the strict inequalities on $R$ leave a polydisc margin, which absorbs the polynomial
factors in $w_I$ produced by radial derivatives; angular derivatives are taken in a smaller strip. The prescribed
multipoles converge because $R^{-2}e^{2\sigma}<\sigma_0e^{2\sigma_0}Y<\rho_0$ for $\sigma\le\sigma_0/2$. For the potential,
Lemma 7.1 in the weighted form of Section 7.2, with $n\delta$ replaced by $\mu_I$ (every distance from $\mu_I$ to
$2\mathbb Z$ is at least $d_n$), gives $\|C_I\|_\sigma\le(3/|4-\mu_I|+1)\|F_I\|_\sigma/d_n$ for $\mu_I\ge3$; the finitely many
indices with $\mu_I<3$ or $|4-\mu_I|<1$ use the downward recurrence of Section 7.2 and are analytic in every smaller
strip. Regrouping the absolutely convergent stationary series by $(n,k)$ completes the proof as in Theorem M. $\square$

Status. The proof is the independent one on analytic multipoles; each step above was checked
here (the condition $\sigma_0e^{2\sigma_0}Y<\rho_0$ makes explicit the choice of $Y$ needed for the prescribed multipoles).
Its finite checks (26542 exact single-mode cases and 79626 inequalities for the multiplier estimates, including
multipole index $10^6$ and frequencies next to resonance) and the all-order theorem are independently confirmed.
Theorem M' covers the same profile class as Theorem A'.

### 12.2 Theorem S: exact exterior solutions behind every truncation, for every $c>1$ (PROVED; independently confirmed)

The convergence theorems concern the series itself. This section shows that, independently of convergence, every
truncation of the canonical series is the asymptotic expansion of an exact exterior solution, for every $c>1$
(rational, Liouville and divergent parameters included) and every smooth leading profile. The proof is a fixed point
in physical space and needs no all-order small-divisor condition: the finitely many divisors up to order $N$ affect
only the size of the coefficients and of $T_0$.

Coordinates and spaces. Put $t=\log r$, $Z=\mathbb R\times S^1$ with coordinates $(t,\theta)$ and measure $dt\,d\theta$,
$Z_T=(T,\infty)\times S^1$, and $\partial\in\{\partial_t,\partial_\theta\}$. $H^k(Z_T)$ is the usual Sobolev space built
on $\partial_t,\partial_\theta$; for $\beta\in\mathbb R$, $H^k_\beta(Z_T)=\{w:e^{-\beta t}w\in H^k(Z_T)\}$ with
$\|w\|_{k,\beta}=\|e^{-\beta t}w\|_{H^k(Z_T)}$. All translates $Z_T$ are isometric, so Sobolev, extension and
commutator constants below do not depend on $T$. Since $r\partial_r=\partial_t$ and
$\partial_x,\partial_y=e^{-t}(\text{trigonometric combinations of }\partial_t,\partial_\theta)$, the Sobolev
embedding $H^k\subset C^{k-2}$ on unit cells $(s,s+1)\times S^1$ gives, for $w\in H^k_\beta(Z_T)$, $k\ge3$,
$$|D^mw(x)|\le C_{k,\beta}\|w\|_{k,\beta}\,|x|^{\beta-m}\qquad(|x|>e^{T+1},\ m\le k-2).\tag{12.2.1}$$
In these coordinates $cX\cdot\nabla=c\partial_t$, $u\cdot\nabla\rho=e^{-2t}\{\psi,\rho\}$ with
$\{\psi,\rho\}=\psi_t\rho_\theta-\psi_\theta\rho_t$, and $-\Delta\psi=\partial_x\rho$ reads
$-(\partial_t^2+\partial_\theta^2)\psi=e^t(\cos\theta\,\partial_t-\sin\theta\,\partial_\theta)\rho$.

Theorem S. Let $c>1$, $\delta=1-1/c$, and let $f_1$ be a real $C^\infty$ function with the S1 symmetry (an odd-harmonic
sine series with rapidly decreasing coefficients). Let $F_n,G_n$ ($n\ge1$) be the coefficients of the canonical series:
$F_n=f_n$, $G_n=g_n$ at irrational $\delta$ (Section 2), and the polynomials in $t$ of Section 14.1 at rational $\delta$,
with any choice of the free resonant constants (the canonical one is $H_{n,j}=0$). Let $N\ge1$,
$$\rho_N=\sum_{n\le N}r^{p_n}F_n(\log r,\theta),\qquad\psi_N=\sum_{n\le N}r^{P_n}G_n(\log r,\theta),$$
and let $\beta\in(p_{N+1},p_N)$ with $\beta\notin\{-3,-5,-7,\dots\}$, and $k\ge4$. Then there are $T_0$ and, for every
$T\ge T_0$, functions $\rho\in C^{k-2}$ and $\psi\in C^{k-1}$ on $r>R:=e^{T+2}$, with the S1 symmetry of Section 1 ($\rho$ even in
$x$ and odd in $y$, $\psi$ odd in $x$ and in $y$), such that

(a) $-\Delta\psi=\partial_x\rho$ and $(cX+u)\cdot\nabla\rho=\rho$ with $u=(-\psi_y,\psi_x)$ hold classically on $r>R$;

(b) $|D^m(\rho-\rho_N)|\le C|x|^{\beta-m}$ for $m\le k-2$ and $|D^m(\psi-\psi_N)|\le C|x|^{\beta+1-m}$ for $m\le k-1$;
in particular $\rho=\sum_{n\le N}r^{p_n}F_n(\log r,\theta)+O(r^\beta)$ with $\beta<p_N$;

(c) the velocity is a Darcy velocity with a single-valued pressure: $u+(0,\rho)=-\nabla p$ on $r>R$ for some $p\in C^{k-2}$,
and $\operatorname{div}u=0$.

The construction is $\rho=\rho_N+e^{\beta t}v$, $\psi=\psi_N+\Phi_\beta[e^{\beta t}v]$ with the operator $\Phi_\beta$ of Step 2,
and, for fixed $N,\beta,T$ and cutoff, $v$ is the only $v\in H^3(Z_T)$ with the S1 symmetry and $\|v\|_{H^3(Z_T)}\le1$ that solves the auxiliary
transport problem (12.2.3) on all of $Z_T$, including the strip $T<t<T+2$ where the physical Poisson equation is not
imposed. No uniqueness is claimed for the exterior equations on $r>R$ alone. The constant $T_0$
depends on $c,f_1,N,\beta,k$ and on the choice of the free resonant constants.

Proof. Step 1 (the approximate solution). For $n\le N$ the coefficients satisfy, by Section 14.1 (which reduces to
Section 2 when there are no logarithms), $(\lambda_n-cD)F_n=Q_n$ and the Poisson equations
$-\Delta(r^{P_n}G_n)=\partial_x(r^{p_n}F_n)$, where $Q_n=\sum_{i+j=n}q_{ij}$,
$q_{ij}=(P_i+D)G_i\,\partial_\theta F_j-\partial_\theta G_i\,(p_j+D)F_j$. They are polynomials in $t$ whose
coefficients are $C^\infty$ in $\theta$: in each angular mode the inverses $(\lambda_n-cD)^{-1}$ and $(D+P_n\pm2j)^{-1}$ of
Section 14.1 are finite sums on polynomials of bounded degree, with coefficients bounded uniformly in $j$ (because
$|2(j+1)-n\delta|\to\infty$ and $|2j-P_n|\ge n\delta$), except at the finitely many resonant modes of orders $n\le N$, where
the degree is raised by one; and products and $\partial_\theta$ preserve rapid decay of Fourier coefficients. So rapid
decay propagates from $f_1$ to all $F_n,G_n$ with $n\le N$. Since
$(cr\partial_r-1)(r^{p_n}F_n)=-r^{p_n}(\lambda_n-cD)F_n$ and $e^{-2t}\{r^{P_i}G_i,r^{p_j}F_j\}=r^{p_{i+j}}q_{ij}$, we get
$-\Delta\psi_N=\partial_x\rho_N$ on $r>0$ and
$$\operatorname{Res}_N:=c\partial_t\rho_N-\rho_N+e^{-2t}\{\psi_N,\rho_N\}=\sum_{i,j\le N,\ i+j\ge N+1}r^{p_{i+j}}q_{ij}.$$
Let $K$ bound the $t$-degrees of all $F_n,G_n$, $n\le N$. Then on $t\ge1$, for every multi-index $\alpha$,
$|\partial^\alpha\operatorname{Res}_N|\le C_\alpha e^{p_{N+1}t}t^{2K}$,
$|\partial^\alpha(e^{-2t}\nabla\psi_N)|\le C_\alpha e^{-\delta t}t^{K}$ (because $P_n-2=-n\delta\le-\delta$) and
$|\partial^\alpha(e^{-t}\nabla\rho_N)|\le C_\alpha e^{-\delta t}t^{K}$ (because $p_n-1\le-\delta$). Hence, with
$\varepsilon_R(T):=\|\operatorname{Res}_N\|_{k,\beta}$ and
$\varepsilon_N(T):=\sum_{|\alpha|\le k+1}\big(\|\partial^\alpha(e^{-2t}\nabla\psi_N)\|_{L^\infty\cap L^2(Z_{T-1})}
+\|\partial^\alpha(e^{-t}\nabla\rho_N)\|_{L^\infty\cap L^2(Z_{T-1})}\big)$, both tend to $0$ as $T\to\infty$; the first
because $\beta>p_{N+1}$.

Step 2 (the velocity correction). Fix $\chi_0\in C^\infty(\mathbb R)$ with $\chi_0=0$ on $(-\infty,1]$, $\chi_0=1$ on
$[2,\infty)$, put $\chi_T(t)=\chi_0(t-T)$, $\mu=\beta+1$. For $w\in H^0_\beta(Z_T)$ with the S1 symmetry let
$\hat w=e^{-\beta t}\chi_Tw$, extended by $0$ to $Z$, and
$$h=(\partial_t+\mu)(\cos\theta\,\hat w)-\partial_\theta(\sin\theta\,\hat w)
=\cos\theta\,(\partial_t+\beta)\hat w-\sin\theta\,\partial_\theta\hat w=e^{-\mu t}e^t(\cos\theta\,\partial_t-\sin\theta\,\partial_\theta)(\chi_Tw).$$
By Lemma 2.1, $h=\sum_{j\ge1}h_j(t)\sin(2j\theta)$. Define $\hat\varphi=\sum_{j\ge1}\hat\varphi_j(t)\sin(2j\theta)$ by the
Fourier multiplier in $t$
$$\widehat{\hat\varphi_j}(\xi)=m_j(\xi)\widehat{h_j}(\xi),\qquad m_j(\xi)=\frac1{4j^2-(i\xi+\mu)^2},$$
and $\Phi_\beta[w]:=\varphi:=e^{\mu t}\hat\varphi$. Since $|4j^2-(i\xi+\mu)^2|^2=((2j-\mu)^2+\xi^2)((2j+\mu)^2+\xi^2)$,
$\mu<2$ (because $\beta<p_1<1$) and $\mu\ne-2j$ for all $j\ge1$, the number
$\vartheta_\mu=\inf_{j\ge1}\min\{(2j-\mu)^2,(2j+\mu)^2\}/(4j^2)$ lies in $(0,1]$, and
$|m_j(\xi)|\le\vartheta_\mu^{-1}(4j^2+\xi^2)^{-1}\le\tfrac54\vartheta_\mu^{-1}(1+4j^2+\xi^2)^{-1}$. So $m$ gains two
derivatives in the Fourier description of $H^s(Z)$, and for every $k\ge0$
$$\|\hat\varphi\|_{H^{k+1}(Z)}\le C_E\|\hat w\|_{H^k(Z)}\le C_E'\|w\|_{k,\beta},\tag{12.2.2}$$
with $C_E'$ depending on $k,\mu,\chi_0$ but not on $T$ (for $k=0$ use that $h$ is a first derivative of $L^2$ functions,
so $\|h\|_{H^{-1}}\le C(1+|\mu|)\|\hat w\|_{L^2}$). In each mode $(4j^2-(\partial_t+\mu)^2)\hat\varphi_j=h_j$, and
$e^{\mu t}(\partial_t+\mu)=\partial_te^{\mu t}$, so
$$-(\partial_t^2+\partial_\theta^2)\varphi=e^t(\cos\theta\,\partial_t-\sin\theta\,\partial_\theta)(\chi_Tw),\quad\text{i.e.}\quad
-\Delta\varphi=\partial_x(\chi_Tw)\ \text{on }\mathbb R^2\setminus\{0\},$$
and $-\Delta\varphi=\partial_xw$ on $t>T+2$. The map is real, linear and preserves the symmetry ($\varphi$ is odd in $x$
and in $y$). It is the unique solution of this equation with $e^{-\mu t}\varphi\in H^1(Z)$: a difference is harmonic,
each mode solves $((\partial_t+\mu)^2-4j^2)\hat\varphi_j=0$, and $e^{(-\mu\pm2j)t}\notin L^2(\mathbb R)$. (In each mode the
multiplier is the Green function that decays at $+\infty$ when $\mu<-2j$ and the two-sided one when $|\mu|<2j$; so for
$\mu\in(-2,2)$ every mode uses the two-sided kernel, and for $\mu\in(-2J-2,-2J)$ the modes $j\le J$ are solved from
$+\infty$. This is why the exponents $\beta+1=-2j$ are excluded.)

Step 3 (the equation for the correction). Write $\rho=\rho_N+w$, $\psi=\psi_N+\varphi$ with $\varphi=\Phi_\beta[w]$. On
$t>T+2$, $-\Delta\psi=\partial_x\rho$, and $(cX+u)\cdot\nabla\rho=\rho$ is equivalent to
$c\partial_tw-w+e^{-2t}\{\psi_N+\varphi,w\}=-\operatorname{Res}_N-e^{-2t}\{\varphi,\rho_N\}$. We solve this equation on all
of $Z_T$. With $w=e^{\beta t}v$, $\Psi=\psi_N+\varphi$, $a=(a^t,a^\theta)=e^{-2t}(\Psi_t,\Psi_\theta)$ and
$\kappa:=1-c\beta>0$ (since $\beta<p_1=1/c$), and using $\{\Psi,e^{\beta t}v\}=e^{\beta t}(\{\Psi,v\}-\beta\Psi_\theta v)$, it becomes
$$L_av:=(c-a^\theta)\partial_tv+a^t\partial_\theta v-(\kappa+\beta a^\theta)v=G(v):=-e^{-\beta t}\operatorname{Res}_N
-e^{-(\beta+2)t}\{\varphi,\rho_N\}.\tag{12.2.3}$$
Write $a=a_N+a_\varphi$ with $a_N=e^{-2t}\nabla\psi_N$ and
$a_\varphi=e^{-2t}\nabla\varphi=e^{(\beta-1)t}\big(\partial_t\hat\varphi+\mu\hat\varphi,\ \partial_\theta\hat\varphi\big)$. By
(12.2.2), Sobolev's embedding and $\beta<1$,
$$\|a_\varphi\|_{W^{1,\infty}(Z_{T-1})}+\|\nabla a_\varphi\|_{H^{k-1}(Z_{T-1})}\le C_1e^{(\beta-1)T}\|v\|_{H^k(Z_T)},\qquad
\|a_\varphi\|_{L^2(Z_{T})}\le C_1e^{(\beta-1)T}\|v\|_{L^2(Z_T)},\tag{12.2.4}$$
and, because $e^{-(\beta+2)t}\{\varphi,\rho_N\}=\big[(\partial_t\hat\varphi+\mu\hat\varphi)\,e^{-t}\partial_\theta\rho_N-
\partial_\theta\hat\varphi\,e^{-t}\partial_t\rho_N\big]$,
$$\|G(v)\|_{H^k(Z_T)}\le\varepsilon_R(T)+C_2\varepsilon_N(T)\|v\|_{H^k(Z_T)},\qquad
\|G(v)-G(v')\|_{L^2(Z_T)}\le C_2\varepsilon_N(T)\|v-v'\|_{L^2(Z_T)}.\tag{12.2.5}$$

Step 4 (the linear transport problem). Lemma. Let $k\ge4$ and let $a$ be a $C^1$ vector field on $Z_{T-1}$ with
$A(a):=\|a\|_{W^{1,\infty}(Z_{T-1})}+\|\nabla a\|_{H^{k-1}(Z_{T-1})}$. There is $\varepsilon_k>0$, depending on
$c,\beta,k$ only, such that if $A(a)\le\varepsilon_k$ then for every $G\in H^k(Z_T)$ there is a unique $v\in H^1(Z_T)$ with
$L_av=G$; moreover $v\in H^k(Z_T)$ and
$$\|v\|_{L^2(Z_T)}\le\tfrac2\kappa\|G\|_{L^2(Z_T)},\qquad\|v\|_{H^k(Z_T)}\le\tfrac4\kappa\|G\|_{H^k(Z_T)}.$$
Proof. (i) Energy identity. Let $V=(c-a^\theta)\partial_t+a^t\partial_\theta$, so $\operatorname{div}V=-\partial_ta^\theta+\partial_\theta a^t$. For
$f\in H^1(Z_T)$ (by density of functions smooth up to $t=T$ with bounded support in $t$),
$$\int_{Z_T}f\,Vf=-\tfrac12\int_{S^1}(c-a^\theta)f^2\big|_{t=T}\,d\theta-\tfrac12\int_{Z_T}(\operatorname{div}V)f^2 .$$
If $\varepsilon_k\le c/2$ the boundary term is $\le0$: no boundary condition is needed at $t=T$, because the
characteristics of $V$ leave $Z_T$ through $t=T$ only in the backward direction. If also
$|\beta|\|a\|_\infty+\|\nabla a\|_\infty\le\kappa/2$, then $-\int fL_af\ge\frac\kappa2\|f\|_{L^2}^2$. With $f=v$ this gives the
$L^2$ bound and uniqueness in $H^1$. (ii) $H^k$ bound for smooth $v$ with bounded support in $t$. For $|\alpha|\le k$,
$L_a\partial^\alpha v=\partial^\alpha G-[\partial^\alpha,L_a]v$, and $[\partial^\alpha,L_a]v=[\partial^\alpha,-a^\theta]\partial_tv
+[\partial^\alpha,a^t]\partial_\theta v-\beta[\partial^\alpha,a^\theta]v$. The commutator estimate
$\|[\partial^\alpha,b]g\|_{L^2}\le C_k(\|\nabla b\|_{L^\infty}\|g\|_{H^{k-1}}+\|\nabla b\|_{H^{k-1}}\|g\|_{L^\infty})$ for
$|\alpha|\le k$ (Klainerman-Majda, Kato-Ponce; on $Z_T$ through a $T$-independent extension operator) and
$\|v\|_{W^{1,\infty}}\le C\|v\|_{H^3}$ give $\|[\partial^\alpha,L_a]v\|_{L^2}\le C_k'A(a)\|v\|_{H^k}$. Applying (i) to
$f=\partial^\alpha v$ and summing over $|\alpha|\le k$:
$\frac\kappa2\|v\|_{H^k}^2\le\|v\|_{H^k}(\|G\|_{H^k}+C_k''A(a)\|v\|_{H^k})$, which gives the $H^k$ bound if
$C_k''\varepsilon_k\le\kappa/4$. (iii) Existence for smooth $a$ with bounded derivatives and smooth $G$ with bounded
$t$-support, say $G=0$ for $t\ge T'$. The $t$-component of $V$ is at least $c/2$, so the forward flow $\Phi_s$ of $V$
($s\ge0$) is global on $\overline{Z_T}$ and increases $t$ at rate at least $c/2$. Put
$q=\kappa+\beta a^\theta\ (\ge\kappa/2)$ and
$$v(x)=-\int_0^\infty\exp\Big(-\int_0^sq(\Phi_\tau x)\,d\tau\Big)G(\Phi_sx)\,ds .$$
The integrand vanishes once $t(\Phi_sx)\ge T'$, so $v$ is smooth, vanishes for $t\ge T'$, and differentiating
$E(s)v(\Phi_sx)$ with $E(s)=\exp(-\int_0^sq)$ along the flow shows $L_av=G$. (iv) General $G\in H^k(Z_T)$, smooth $a$:
approximate $G$ in $H^k$ by data as in (iii); by (ii) the solutions form a Cauchy sequence in $H^k$, and the limit solves
$L_av=G$ ($H^k\subset C^1$). (v) General $a$: mollify, $a_\epsilon=J_\epsilon a$ (on $Z_{T-1}$, kernel of radius $<1$), so
$\|a_\epsilon\|_{W^{1,\infty}(Z_T)}+\|\nabla a_\epsilon\|_{H^{k-1}(Z_T)}\le A(a)$ and $a_\epsilon\to a$ uniformly on $Z_T$; parts (i) to (iii)
use only these norms on $Z_T$. The solutions $v_\epsilon$ of $L_{a_\epsilon}v_\epsilon=G$
are bounded in $H^k$ by (ii), and $L_{a_\epsilon}(v_\epsilon-v_{\epsilon'})=(L_{a_{\epsilon'}}-L_{a_\epsilon})v_{\epsilon'}$ has
$L^2$ norm at most $(1+|\beta|)\|a_\epsilon-a_{\epsilon'}\|_{L^\infty}\|v_{\epsilon'}\|_{H^1}\to0$; by (i) they converge in
$L^2$, hence in $H^{k-1}\subset C^1$ by interpolation, to $v\in H^k$ with $L_av=G$ and the stated bounds. $\square$

Step 5 (iteration). Let $v^0=0$ and, given $v^m$, let $a^m=a_N+a_\varphi(v^m)$ and $v^{m+1}$ the solution of
$L_{a^m}v^{m+1}=G(v^m)$. Each $v^m$ has the S1 symmetry, so that $\Phi_\beta$ is applied only within its domain: if $v^m$
has it, the reflections described at the end of this step map the solution of $L_{a^m}v=G(v^m)$ to a solution of the
same linear problem (same coefficients, same data), so by the uniqueness in the Lemma $v^{m+1}$ has it too. Put $M:=8\varepsilon_R(T)/\kappa$. Choose $T_0$ so that for $T\ge T_0$: $M\le1$,
$\varepsilon_N(T)+C_1e^{(\beta-1)T}\le\varepsilon_k$ (so the Lemma applies whenever $\|v^m\|_{H^k}\le1$),
$4C_2\varepsilon_N(T)/\kappa\le1/2$, and $\frac2\kappa\big(C_2\varepsilon_N(T)+C_3C_1e^{(\beta-1)T}\big)\le\frac12$, where
$C_3$ is the constant in $\|\partial v\|_{L^\infty}+|\beta|\|v\|_{L^\infty}\le C_3\|v\|_{H^3}$. Induction: if $\|v^m\|_{H^k}\le M$ then by the Lemma and (12.2.5)
$\|v^{m+1}\|_{H^k}\le\frac4\kappa(\varepsilon_R+C_2\varepsilon_NM)\le\frac M2+\frac M2=M$. Contraction: $d^{m+1}=v^{m+1}-v^m$ solves
$$L_{a^m}d^{m+1}=G(v^m)-G(v^{m-1})-(L_{a^m}-L_{a^{m-1}})v^m,$$
and $(L_a-L_{a'})v=-(a^\theta-a'^\theta)\partial_tv+(a^t-a'^t)\partial_\theta v-\beta(a^\theta-a'^\theta)v$, so
$\|(L_{a^m}-L_{a^{m-1}})v^m\|_{L^2}\le C_3\|a_\varphi(v^m)-a_\varphi(v^{m-1})\|_{L^2}\|v^m\|_{H^3}$ ($L^2$ times $L^\infty$).
By (12.2.4), (12.2.5) and the $L^2$ bound of the Lemma,
$\|d^{m+1}\|_{L^2}\le\frac2\kappa(C_2\varepsilon_N+C_3C_1e^{(\beta-1)T}M)\|d^m\|_{L^2}\le\frac12\|d^m\|_{L^2}$. Hence $v^m\to v$ in
$L^2(Z_T)$, $\|v\|_{H^k}\le M$, and by interpolation $v^m\to v$ in $H^{k-1}(Z_T)\subset C^1$ ($k\ge4$); by (12.2.2) at
level $k-1$, $\hat\varphi(v^m)\to\hat\varphi(v)$ in $H^k(Z)\subset C^2$, so $a^m\to a(v)$ in $C^1$, and passing to the limit
in $L_{a^m}v^{m+1}=G(v^m)$ shows that $v$ solves (12.2.3) classically. Uniqueness: let $v'$ be another solution of (12.2.3) with
the S1 symmetry (the domain of $\Phi_\beta$) and $\|v'\|_{H^3(Z_T)}\le1$, and $d=v-v'$. Then $L_{a(v')}d=G(v)-G(v')-(L_{a(v)}-L_{a(v')})v$. By (12.2.4) at level $k=3$,
$a(v')$ satisfies the smallness conditions of part (i) of the Lemma once $T_0$ is large (this needs only
$\|v'\|_{H^3}\le1$), and the computation above gives $\frac\kappa2\|d\|_{L^2}\le(C_2\varepsilon_N+C_3C_1e^{(\beta-1)T})\|d\|_{L^2}
\le\frac\kappa4\|d\|_{L^2}$, so $d=0$ (with $C_3$ as above and
$\|v\|_{H^3}\le M\le1$). Part (i) of the Lemma needs only $a\in C^1$ with the smallness conditions, and $d\in H^1$. Symmetry: the reflections $\theta\mapsto-\theta$ and $\theta\mapsto\pi-\theta$, acting on densities
with the parities of odd sine series and on streams with the parities of $\sin(2j\theta)$, commute with $\Phi_\beta$
and map solutions of (12.2.3) to solutions (they fix $\rho_N,\psi_N$ and $\operatorname{Res}_N$); by uniqueness $v$ is
invariant, which is the S1 symmetry.

Step 6 (conclusion). $\rho=\rho_N+e^{\beta t}v$ and $\psi=\psi_N+\Phi_\beta[e^{\beta t}v]$ satisfy (a) on $t>T+2$ by Steps
2 and 3. (b) is (12.2.1) for $w=e^{\beta t}v$ and, for $\varphi=e^{\mu t}\hat\varphi$ with $\hat\varphi\in H^{k+1}(Z)$, the
same argument with $k+1$ and $\mu$. Regularity: $\rho_N,\psi_N$ are smooth on $r>0$, $w\in C^{k-2}$, $\varphi\in C^{k-1}$.
(c) $u=\nabla^\perp\psi$ is divergence free, and $\operatorname{curl}(u+(0,\rho))=\Delta\psi+\partial_x\rho=0$, so
$u+(0,\rho)$ is locally a gradient. Its circulation around the circle $r=r_0$ vanishes because the field is symmetric
under the reflection $(x,y)\mapsto(-x,y)$ (its first component is odd in $x$, its second even), which reverses the
orientation of the circle. So the pressure is single valued. $\square$

Remarks. 1. Theorem S holds at every $\delta\in(0,1)$: at rational $\delta$ with logarithms, at Liouville $\delta$, and on
the dense $G_\delta$ set of Theorem C where the series diverges at every radius (see also Sections 10.2 to 10.6 and
14.18). Divergence of the series is therefore a failure of the representation by a convergent expansion, not an absence
of exterior solutions with the truncated series as asymptotic expansion to any finite order. Theorem S says nothing
about convergence.
2. A solution given by Theorem S for some $N'$ and $\beta'$ also satisfies (b) for every $N<N'$ and every
$\beta\in(p_{N+1},p_N)$, because $\rho_{N'}-\rho_N=O(r^{p_{N+1}}(\log r)^K)$, $p_{N+1}<\beta$ and $\beta'<p_{N'}\le p_{N+1}$, and similarly
for the stream; at $N'$ itself it satisfies (b) only for $\beta\ge\beta'$. Since $T_0$ depends on $N$, the
theorem does not give one exterior solution with the expansion to all orders; whether such a solution exists when the
series diverges is OPEN.
3. Uniqueness holds only within the class of Step 5, in which the velocity correction is $\Phi_\beta$, the solution of the
Poisson equation in the weighted space $e^{(\beta+1)t}H^1$. Other exterior solutions with the same expansion are expected
(compare the multipole freedom of Section 12 item 2 and Theorem M) and are not classified here. The weight $\beta<p_1=\gamma$
excludes the homogeneous solutions $r^{\gamma}h(\theta)$ of $c\,r\partial_r w=w$, which carry a new leading profile.
4. The smoothness index $k$ is fixed in advance, and $T_0$ grows with $k$ (the commutator constants in Step 4 grow
with $k$). A $C^\infty$ solution on one fixed exterior is not claimed.
5. The construction works with $\rho$ and $\psi$ only. A common potential exists afterwards: by Section 12.3 with
$s=k-1$, for every $R_2>R$ there is $\chi\in C^k(\mathbb R^2)$, even in $x$ and in $y$, with $\chi_{xy}=\psi$ and
$-\partial_y\Delta\chi=\rho$ on $r>R_2$, so the solutions of Theorem S also solve the potential formulation there. No
asymptotics of $\chi$ are claimed, because the reconstruction may add gauge terms $A(x)+by^2$ of arbitrary growth.
6. The exclusion $\beta\notin\{-3,-5,\dots\}$ is needed for the operator $\Phi_\beta$ (at $\mu=\beta+1=-2j$ the symbol is
$4j^2-(i\xi+\mu)^2=\xi(\xi+4ij)$, so $m_j\widehat{h_j}\notin L^2$ whenever $\widehat{h_j}(0)\ne0$; the solution involves a primitive in $t$
of a forcing with nonzero mean), not for the conclusion: for an excluded $\beta$, apply the theorem with a
nonexceptional $\tilde\beta\in(p_{N+1},\beta)$; then (a) and (c) hold, and (b) at $\tilde\beta$ implies (b) at $\beta$.
7. Context. Well-posedness in classes with prescribed spatial asymptotic expansions of finite order, including
logarithms, is known for the time-dependent Euler equations (R. McOwen and P. Topalov, Spatial asymptotic expansions in
the incompressible Euler equation, arXiv:1606.08059, 2016), and stable self-similar blow-up for a special
infinite-energy class of IPM solutions that reduces to a one-dimensional equation is proved by C. Collot, C. Prange and
J. Tan (arXiv:2507.17381, 2025). Neither concerns stationary self-similar exterior IPM solutions with a prescribed
truncated far-field series. We did not find an equivalent statement in the literature; no priority is claimed.

Status. PROVED (independently confirmed, including the repairs made during its verification). The standard ingredients are Sobolev embedding, a $T$-independent extension
operator for $Z_T$, and the Moser-type commutator estimate.

### 12.3 A common potential for exterior solutions (PROVED: independent proof, reviewed here)

Proposition 12.3. Let $R>0$, let $s\ge2$ be an integer and $\Omega_R=\{x^2+y^2>R^2\}$. Let $\rho\in C^{s-1}(\Omega_R)$ and
$\psi\in C^s(\Omega_R)$ have the S1 symmetry ($\rho$ even in $x$ and odd in $y$, $\psi$ odd in $x$ and in $y$) and satisfy
$-\Delta\psi=\partial_x\rho$. Then for every $R_2>R$ there is $\chi\in C^{s+1}(\mathbb R^2)$, even in $x$ and in $y$, with
$$\chi_{xy}=\psi,\qquad-\partial_y\Delta\chi=\rho\qquad\text{on }\Omega_{R_2},$$
so that $u=(-\psi_y,\psi_x)=(-\chi_{xyy},\chi_{xxy})$ there. Two $C^3$ functions on $\Omega_{R_2}$ that are even in $x$ and in
$y$ and have these two properties differ exactly by $A(x)+by^2$ with $A$ even of class $C^3$ and $b\in\mathbb R$, and
every such difference is allowed.

Proof. Fix $R<R_1<R_2$ and a smooth radial $\zeta$ with $\zeta=0$ for $r\le R_1$ and $\zeta=1$ for $r\ge R_2$. Then
$\tilde\psi=\zeta\psi$, extended by $0$, is $C^s$ on $\mathbb R^2$, odd in $x$ and in $y$, and equal to $\psi$ on
$\Omega_{R_2}$. Put $\chi_0(x,y)=\int_0^x\int_0^y\tilde\psi(a,b)\,db\,da$. It is even in $x$ and in $y$ and satisfies
$\partial_x\partial_y\chi_0=\tilde\psi$. It is $C^{s+1}$: for $i,j\ge1$, $\partial_x^i\partial_y^j\chi_0=\partial_x^{i-1}\partial_y^{j-1}\tilde\psi$,
and $\partial_x^i\chi_0=\int_0^y\partial_x^{i-1}\tilde\psi(x,b)\,db$, $\partial_y^j\chi_0=\int_0^x\partial_y^{j-1}\tilde\psi(a,y)\,da$; for
$i+j\le s+1$ these use at most $s$ derivatives of $\tilde\psi$ and are continuous. On $\Omega_{R_2}$ put
$$F=-\partial_y\Delta\chi_0-\rho=-\tilde\psi_x-\int_0^x\tilde\psi_{yy}(a,y)\,da-\rho .$$
$F$ is $C^{s-2}$, even in $x$ and odd in $y$, and its $x$-derivative exists classically and equals
$-\tilde\psi_{xx}-\tilde\psi_{yy}-\rho_x=-\Delta\psi-\partial_x\rho=0$ on $\Omega_{R_2}$. Hence $F$ is constant on each component of
each horizontal section $\{x:(x,y)\in\Omega_{R_2}\}$. For $|y|>R_2$ the section is a line; for $|y|\le R_2$ it consists of two
half-lines exchanged by $x\mapsto-x$, and since $F$ is even in $x$ the two constants agree. So $F(x,y)=A_0(y):=F(x_*,y)$ on
$\Omega_{R_2}$ for any fixed $x_*>R_2$, and $A_0\in C^{s-2}(\mathbb R)$ is odd. This is where the reflection symmetry removes
the possible mismatch between the two sides of the hole. Put $B(y)=\frac12\int_0^y(y-b)^2A_0(b)\,db$. Then $B'''=A_0$, $B\in
C^{s+1}$, and $B$ is even because $A_0$ is odd. The function $\chi=\chi_0+B$ is $C^{s+1}$ and even in $x$ and $y$; on
$\Omega_{R_2}$, $\chi_{xy}=\tilde\psi=\psi$ and $-\partial_y\Delta\chi=(F+\rho)-A_0=\rho$.

Gauge. Let $h$ be the difference of two such potentials. Then $h_{xy}=0$ and $\partial_y\Delta h=0$ on $\Omega_{R_2}$. At
fixed $x$, $h_x$ is constant on each component of the vertical section, and since $h_x$ is even in $y$ the two constants
agree when there are two components; so $h_x=a(x)$ with $a\in C^2(\mathbb R)$ odd. Likewise $h_y=b_0(y)$ with $b_0\in
C^2(\mathbb R)$ odd. With the even primitives $A'=a$, $B_0'=b_0$, $h-A-B_0$ has zero gradient on the connected set
$\Omega_{R_2}$ and is constant; put the constant into $A$. Then $0=\partial_y\Delta h=B_0'''$, and evenness gives
$B_0=by^2+d$; put $d$ into $A$. Conversely $A(x)+by^2$ has zero mixed derivative and zero $\partial_y\Delta$. $\square$

For Theorem S, $\rho\in C^{k-2}$ and $\psi\in C^{k-1}$, so $s=k-1\ge3$ and $\chi\in C^k\subset C^4$, enough for the
differentiated density equation to hold pointwise. The proposition gives existence only. It does not select the
homogeneous radial powers of the formal potential series, it may add gauge terms of unrelated growth, and it gives no
convergence, no $C^\infty$ solution on one fixed exterior and no common solution for all truncations.

### 12.4 Theorem T: a convergent series without logarithms at the rational parameter $c=3$ (PROVED: independently audited and confirmed, with independent exact arithmetic)

At $\delta=2/3$ ($c=3$) the pure ansatz with the canonical constants is obstructed, and the canonical continuation
carries logarithms (Section 14). Every resonance, however, leaves one free harmonic multipole constant. This section
shows that for profiles that pass the first compatibility condition, and whose response coefficients stay away from
zero (hypotheses (T-a) and (T-b) below), these constants can be chosen, uniquely, so that every later compatibility
condition holds, and that the resulting pure power series converges. So at this rational
parameter the resonances do not by themselves prevent a convergent series; what they prevent is the pure series with
the canonical constants, and any pure series for profiles that fail the first condition (such as $\sin\theta$).

Setting. Throughout $c=3$, $\delta=2/3$, $p_n=1-\frac{2n}3$, $P_n=2-\frac{2n}3$, $\lambda_n=2(n-1)$. The pure ansatz is
$\rho=\sum_{n\ge1}r^{p_n}f_n(\theta)$, $\psi=\sum_{n\ge1}r^{P_n}g_n(\theta)$ with $f_n=\sum_{m\text{ odd}}a_{n,m}\sin m\theta$ and
$g_n=\sum_{q\ge2\text{ even}}b_{n,q}\sin q\theta$. With $D=0$ the equations of Section 14.1 read
$$\lambda_nf_n=\sum_{i+j=n}T_{i,j}(g_i,f_j),\qquad T_{i,j}(g,f)=P_i\,g\,\partial_\theta f-p_j\,(\partial_\theta g)\,f\qquad(n\ge2),\tag{T1}$$
$$(q^2-P_n^2)\,b_{n,q}=\tfrac12(P_n+q)\,a_{n,q+1}+\tfrac12(P_n-q)\,a_{n,q-1}.\tag{T2}$$
Since $P_n<2$, (T2) is singular only when $P_n=-q$, i.e. at $n=3k$, $q=q_k:=2k-2$, $k\ge2$. There (T2) reads
$0=-q_ka_{3k,q_k-1}$, so it is solvable if and only if the obstruction $O_{3k}:=a_{3k,\,2k-3}$ vanishes, and then
$b_{3k,q_k}=:H_{3k}$ is free (the multipole $H_{3k}r^{-q_k}\sin q_k\theta$). Every other divisor $q\pm P_n$ lies in
$\frac23\mathbb Z\setminus\{0\}$. For nonresonant $n$ write $g_n=\Pi_nf_n$, with
$b_{n,q}=-a_{n,q-1}/(2(q+P_n))+a_{n,q+1}/(2(q-P_n))$. Given $f_1$ and constants $(H_{3k})_{k\ge2}$, (T1), $g_n=\Pi_nf_n$ at
nonresonant $n$, and $g_{3k}=\Pi'_{3k}f_{3k}+H_{3k}e_k$ define all $f_n,g_n$. Here $e_k=\sin q_k\theta$ and $\Pi'_{3k}$ is the
same formula with the whole mode $q_k$ omitted, so $H_{3k}$ is the entire coefficient $b_{3k,q_k}$; the canonical
normalization of Section 14 is $H_{3k}=0$. The formal series solves every order if and only if $O_{3k}=0$ for all
$k\ge2$.

Response coefficients. For $k\ge2$ and $n=3k$ define (the orders $n+1,n+2$ are not multiples of 3, so $\Pi_{n+1},\Pi_{n+2}$
are nonresonant)
$$\varphi_1=\lambda_{n+1}^{-1}T_{n,1}(e_k,f_1),\qquad
\varphi_2=\lambda_{n+2}^{-1}\big[T_{n,2}(e_k,f_2)+T_{1,n+1}(g_1,\varphi_1)+T_{n+1,1}(\Pi_{n+1}\varphi_1,f_1)\big],$$
$$\varphi_3=\lambda_{n+3}^{-1}\big[T_{n,3}(e_k,f_3)+T_{1,n+2}(g_1,\varphi_2)+T_{n+2,1}(\Pi_{n+2}\varphi_2,f_1)
+T_{2,n+1}(g_2,\varphi_1)+T_{n+1,2}(\Pi_{n+1}\varphi_1,f_2)\big],$$
and let $\sigma_k$ be the coefficient of $\sin((q_k+1)\theta)$ in $\varphi_3$. It depends only on $f_1,f_2,f_3,g_1,g_2$ and $k$,
and is homogeneous of degree 3 in $f_1$.

Lemma T.1. Let $k\ge2$, $n=3k$, and fix all constants except $H_n$. Then $f_{n+i}=f^{(0)}_{n+i}+H_n\varphi_i$ for $i=1,2,3$,
where $f^{(0)}$ is computed with $H_n=0$. Hence $O_{n+3}=R_k+\sigma_kH_n$, where $R_k$, the coefficient of
$\sin((q_k+1)\theta)$ in $f^{(0)}_{n+3}$, depends only on $f_1,\dots,f_n$, $g_1,\dots,g_{n-1}$ and $g_n-H_ne_k$.

Proof. $H_n$ enters only through $g_n$. A product $T_{i,j}(g_i,f_j)$ with $i+j\le n+3$ has at most one factor of order
$\ge n$, because $2n>n+3$. So $f_m$ ($m\le n+3$) and $g_m$ ($m\le n+2$) are affine in $H_n$, and their linear parts
satisfy the recursion that defines $\varphi_1,\varphi_2,\varphi_3$: at order $n+i$ the linear part collects the products of
$e_k$ (order $n$) with $f_i$, and of the linear parts at orders $n+1,\dots,n+i-1$ with $f$ or $g$ of the complementary
order. $\square$

Proposition T.2. If $O_6(f_1)=0$ and $\sigma_k\ne0$ for all $k\ge2$, there is exactly one sequence $(H_{3k})_{k\ge2}$ for
which the pure ansatz solves every order, namely $H_{3k}=-R_k/\sigma_k$, determined recursively in $k$.

Proof. $O_6$ involves no constant. By Lemma T.1, $O_{3k+3}=0$ fixes $H_{3k}$ uniquely, and $R_k$ involves only
$H_{3k'}$ with $k'<k$. $\square$

Theorem T. Let $c=3$ and let $f_1=\sum_{m\text{ odd},\,m\le L}a_{1,m}\sin m\theta$ be a nonzero real sine polynomial
with top frequency $L$, $B=L+1$. Assume
(T-a) $O_6(f_1)=0$, and (T-b) $\sigma_k\ne0$ for every $k\ge2$ and $\sigma_*:=\inf_{k\ge2}|\sigma_k|>0$. Let $(H_{3k})$ be the
constants of Proposition T.2. Then:

1. there are $C,A>0$ with $\|f_n\|_{\ell^1}+\|g_n\|_{\ell^1}\le CA^n$ for all $n\ge1$;
2. for $r>A^{3/2}$ the series $\rho=\sum r^{p_n}f_n$ and $\psi=\sum r^{P_n}g_n$ converge absolutely, together with every
   Cartesian derivative series, uniformly on $r\ge R$ for every $R>A^{3/2}$ and for $\theta$ in a complex strip whose width
   depends on $R$; the sums
   are real analytic on $r>A^{3/2}$, contain no logarithm, have the S1 symmetry, and satisfy $-\Delta\psi=\partial_x\rho$ and
   $c\,r\partial_r\rho+u\cdot\nabla\rho=\rho$ with $u=(-\psi_y,\psi_x)$ exactly; $\rho=r^{1/3}f_1+O(r^{-1/3})$;
3. on $r>R_2$, for every $R_2>A^{3/2}$, there is a $C^\infty$ potential $\chi$ with $\chi_{xy}=\psi$ and $-\partial_y\Delta\chi=\rho$
   (Proposition 12.3; its construction preserves $C^\infty$), and a single-valued pressure, since
   $\operatorname{curl}(u+(0,\rho))=\Delta\psi+\partial_x\rho=0$ and the circulation vanishes by the reflection symmetry
   (as for Theorem S);
4. this is the only formal solution of the form $\rho=\sum r^{p_n}f_n$, $\psi=\sum r^{P_n}g_n$ with $2\pi$-periodic
   coefficients, the S1 symmetry of both fields ($\rho$ even in $x$ and odd in $y$, $\psi$ odd in both, so that each $g_n$ is a
   sine series in even frequencies with no extra stream gauge) and leading term $f_1$; no uniqueness among arbitrary
   exterior solutions is claimed. Replacing $f_1$ by
   $\varepsilon f_1$, $\varepsilon\ne0$ real, preserves (T-a) and (T-b) (homogeneity of degrees 6 and 3) and multiplies $H_n$ by
   $\varepsilon^n$.

Proof of 1. Write $M_n=\|f_n\|_{\ell^1}$, $N_n=\|g_n\|_{\ell^1}$, $x_n=nM_n$, $\eta_n=n|H_n|$ for $n=3k\ge6$ and $\eta_n=0$
otherwise.

Step 1 (linear bounds). By induction the frequencies satisfy $\le Bn-1$ for $f_n$ and $\le Bn$ for $g_n$ (note $q_k<3kB$).
The $\ell^1$ norm of the product of a sine and a cosine polynomial is at most the product of the norms, $|p_j|\le j$ and
$|P_i|\le\frac43i$. Hence $\|T_{i,j}(g,f)\|\le\frac{7B}3\,ij\,\|g\|\|f\|$ when the frequencies of $g$, $f$ are at most $Bi$,
$Bj$. Since $m/\lambda_m\le1$ for $m\ge2$, for every finite family of such pairs
$$m\Big\|\lambda_m^{-1}\sum T_{i,j}(g_i,f_j)\Big\|\le\kappa\sum\big(i\|g_i\|\big)\big(j\|f_j\|\big),\qquad\kappa=\tfrac{7B}3.\tag{K}$$
Each $a_{n,m}$ enters at most two stream coefficients, with factors $1/(2|q\pm P_n|)\le\frac34$. So
$\|\Pi_nf\|\le\frac32\|f\|$ at nonresonant $n$, $\|\Pi'_nf\|\le\frac32\|f\|$, and $N_n\le\frac32M_n+|H_n|$ at resonant $n$.

Step 2 (inequalities). From (T1) and Step 1,
$$x_n\le\kappa\sum_{i+j=n}\big(\tfrac32x_i+\eta_i\big)x_j\qquad(n\ge2).\tag{I1}$$
For $n=3k\ge6$ put $u_n=(n+1)\|f^{(0)}_{n+1}\|$ and $v_n=(n+2)\|f^{(0)}_{n+2}\|$. In $f^{(0)}_{n+1},f^{(0)}_{n+2},f^{(0)}_{n+3}$
the stream of order $n$ is $\Pi'_nf_n$, of norm $\le\frac32M_n$, and $\eta_i\ne0$ only for multiples $i\le n-3$ of 3, so the
order of the partner of such an $\eta_i$ is $\ge4$. A pair with one index in $\{1,2\}$ and the other above $n$ uses
$f^{(0)}_{n+1}$, $f^{(0)}_{n+2}$ or their Poisson images (norm factor $\frac32$), and both orientations occur. Hence
$$u_n\le\kappa\Big[\tfrac32\sum_{i+j=n+1}x_ix_j+\sum_{\substack{i+j=n+1\\ j\ge4}}\eta_ix_j\Big],\qquad
v_n\le\kappa\Big[\tfrac32\sum_{\substack{i+j=n+2\\ i,j\ge2}}x_ix_j+\sum_{\substack{i+j=n+2\\ j\ge4}}\eta_ix_j\Big]+3\kappa x_1u_n,\tag{I2}$$
and, since $\eta_n=n|R_k|/|\sigma_k|\le\sigma_*^{-1}(n+3)\|f^{(0)}_{n+3}\|$,
$$\eta_n\le\frac\kappa{\sigma_*}\Big[\tfrac32\sum_{\substack{i+j=n+3\\ i,j\ge3}}x_ix_j+\sum_{\substack{i+j=n+3\\ j\ge4}}\eta_ix_j
+3x_1v_n+3x_2u_n\Big].\tag{I3}$$

Step 3 (majorant sequences). Define $\bar x_1=x_1$, $\bar\eta_n=0$ for $n\le3$, and $\bar x_n$ ($n\ge2$), $\bar u_n,\bar v_n,\bar\eta_n$
($n\ge4$, all $n$, not only multiples of 3) by equality in (I1) to (I3). The right sides are polynomials with nonnegative
coefficients, and the dependence is triangular: $\bar x_n$ uses $\bar\eta_i$ with $i<n$; $\bar u_n,\bar v_n,\bar\eta_n$ use
$\bar x_i$ with $i\le n$, $\bar\eta_i$ with $i<n$, and $\bar u_n,\bar v_n$. By induction $x_n\le\bar x_n$ and $\eta_n\le\bar\eta_n$.

Step 4 (generating functions). Put $X=\sum_{n\ge1}\bar x_nz^n=P+z^4W$ with $P=\bar x_1z+\bar x_2z^2+\bar x_3z^3$, and
$\sum_{n\ge4}\bar\eta_nz^n=z^4\hat E$, $\sum_{n\ge4}\bar u_nz^n=z^4\hat U$, $\sum_{n\ge4}\bar v_nz^n=z^4\hat V$. Since
$\bar x_2=\frac32\kappa\bar x_1^2$ and $\bar x_3=3\kappa\bar x_1\bar x_2$, the equalities in (I1) to (I3) are equivalent to the
following identities of formal power series:
$$W=\tfrac32\kappa\big[\bar x_2^2+2\bar x_1\bar x_3+2\bar x_2\bar x_3z+\bar x_3^2z^2\big]+3\kappa PW+\tfrac32\kappa z^4W^2
+\kappa\hat E(P+z^4W),$$
$$\hat U=\tfrac32\kappa\big(2\bar x_2\bar x_3+\bar x_3^2z\big)+3\kappa\tfrac Pz\,W+\tfrac32\kappa z^3W^2+\kappa z^3\hat EW,$$
$$\hat V=\tfrac32\kappa\big[\bar x_3^2+2(\bar x_2+\bar x_3z)W+z^2W^2\big]+\kappa z^2\hat EW+3\kappa\bar x_1\hat U,$$
$$\hat E=\frac\kappa{\sigma_*}\big[3\bar x_3W+\tfrac32zW^2+z\hat EW+3\bar x_1\hat V+3\bar x_2\hat U\big].$$
(For instance $\sum_{i+j=n+3,\,i,j\ge3}\bar x_i\bar x_j$ is the coefficient of $z^{n+3}$ in $(\bar x_3z^3+z^4W)^2$, whose part of
degree $\ge7$ is $2\bar x_3z^7W+z^8W^2$.) This is a system $Y=\Phi(z,Y)$, $Y=(W,\hat U,\hat V,\hat E)$, with $\Phi$ polynomial.
Every term of $\Phi$ that is nonlinear in $Y$ carries a factor $z$, and at $z=0$ the linear part $J=\partial_Y\Phi(0,\cdot)$ is
strictly lower triangular in the order $(W,\hat U,\hat V,\hat E)$. Hence $\det(I-J)=1$, and comparing coefficients of
$z^m$ gives $(I-J)Y_m=$ (a polynomial in $Y_0,\dots,Y_{m-1}$), so the formal solution is unique. At $z=0$ the affine
equation $Y_0=\Phi(0,Y_0)$ has a unique solution because $I-J$ is invertible (explicitly, $J$ has the entries $3\kappa\bar x_1$,
$3\kappa\bar x_2$, $3\kappa\bar x_1$ below the diagonal in its second and third rows and $3\kappa\bar x_3/\sigma_*$, $3\kappa\bar x_2/\sigma_*$,
$3\kappa\bar x_1/\sigma_*$ in its last row, so $J^4=0$). By the holomorphic implicit function theorem at $(0,Y_0)$ the system has a
holomorphic solution near $z=0$; its Taylor series is a formal solution,
hence equal to the majorant series. So the majorant series have a positive radius $\rho_0$, and for any $A>1/\rho_0$,
$\bar x_n+\bar\eta_n\le CA^n$. Therefore $M_n\le CA^n$, $|H_n|\le CA^n$ and $N_n\le\frac32M_n+|H_n|\le3CA^n$. $\square$

No smallness condition enters: the factor $1/\sigma_*$ may be large, since it multiplies only terms that are lower
triangular at $z=0$. The constant $A$ is not explicit.

Proof of 2 to 4. The frequency bounds and 1 give $|r^{p_n}f_n(\theta)|\le r^{1/3}C'(Ae^{B\tau}r^{-2/3})^{n-1}$ for
$|\operatorname{Im}\theta|\le\tau$, and likewise for $g_n$; a Cartesian derivative of $r^pF(\theta)$ is $r^{p-1}$ times a
combination of $pF$ and $F'$, so each derivative costs a factor polynomial in $n$. For each $R>A^{3/2}$ choose $\tau>0$ with
$Ae^{B\tau}R^{-2/3}<1$. After omitting the finitely many terms whose radial exponent is not negative, every remaining term
of a derivative series has its supremum over $r\ge R$ at $r=R$, and these suprema are summable; so all derivative series
converge uniformly and absolutely on $r\ge R$. The normalized sums $r^{-1}\rho=\sum_nf_nz^n$ and $r^{-2}\psi=\sum_ng_nz^n$
are holomorphic in $(z,\theta)$ for $|z|<R^{-2/3}$, $|\operatorname{Im}\theta|<\tau$ ($\rho$ and $\psi$ themselves carry the factors
$r$ and $r^2$), so $\rho$ and $\psi$ are real analytic on the exterior. The order equations (T1) and (T2), which hold at every order by Proposition T.2, are the
coefficient identities of the two equations (Section 2), and absolute convergence permits the rearrangement of the
products. The potential and the pressure follow from Proposition 12.3 and the identity
$\operatorname{curl}(u+(0,\rho))=\Delta\psi+\partial_x\rho=0$ with the symmetry argument of Theorem S. Uniqueness is Proposition
T.2, and the scaling statement follows from $f_n\mapsto\varepsilon^nf_n$, $g_n\mapsto\varepsilon^ng_n$. $\square$

Corollary T.3 (explicit profiles). Let
$$\mathcal P_6(b)=176703765525000b^6-222533688701250b^5+96180432855375b^4-20675598499400b^3+2783057141280b^2
-243275209320b+10532171936 .$$
$\mathcal P_6$ is irreducible over $\mathbb Q$ and has exactly two real roots, $b_1\in(\frac14,\frac13)$, $b_1=0.280661662731966\ldots$,
and $b_2\in(\frac12,1)$, $b_2=0.646352289880934\ldots$. Let $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ with $b\in\{b_1,b_2\}$ and
$\varepsilon\ne0$ real.

(a) (T-a) and (T-b) hold, so Theorem T gives a convergent pure power series without logarithms at $c=3$.

(b) $R_2\ne0$. So the canonical normalization $H_6=0$ is obstructed at order 9, and the canonical continuation for these
profiles carries logarithms from order 9 on.

(c) $\inf_{k\ge2}|\sigma_k|=-\sigma_4$, attained only at $k=4$, and $\sigma_k<\sigma_4<0$ for every $k\ge7$. For $\varepsilon=1$,
$-\sigma_4=3.812446147157974\ldots\cdot10^{-5}$ for $b_1$ and $-\sigma_4=1.568387259640781\ldots\cdot10^{-3}$ for $b_2$.

Proof of (a) (exact rational arithmetic in $\mathbb Q[b]$ and $\mathbb Q(k)[b]$, the accompanying artifacts). For
$f_1=\sin\theta+b\sin3\theta$ one finds $O_6=\mathcal P_6(b)/35818438656000000$. The response coefficients are
$$\sigma_2=\frac{183414000b^3-97851780b^2+8099325b+978848}{1435033600},\qquad
\sigma_3=-\frac{176551375b^3-16246560b^2-11708208b+1479808}{1078197120},$$
explicit nonzero cubics for $k=4,5,6$, and for $k\ge7$
$$\sigma_k=-\frac{(k-1)(2k-1)^2\,\mathcal N(k,b)}{9600\,k(3k-4)(3k-2)(3k-1)(3k+1)^2(3k+2)(6k-11)(6k-7)(6k-5)(6k-1)},$$
where $\mathcal N$ has degree 3 in $b$ and 8 in $k$ (given in full in the artifacts). The formula comes from the same
computation with $k$ symbolic. Each of $\varphi_1,\varphi_2,\varphi_3$ is linear in $e_k$, so every frequency in it has the
form $\pm(q_k+j)$ with a fixed integer $|j|\le11$: the maximal frequencies of $f_1,g_1,f_2,g_2,f_3$ are $3,4,7,8,11$, so the
offsets in $\varphi_1$, $\Pi_{n+1}\varphi_1$, $\varphi_2$, $\Pi_{n+2}\varphi_2$, $\varphi_3$ are at most $3,4,7,8,11$. The Poisson divisors
are nonzero: at order $n+s$, $s=1,2$, $P_{n+s}=-q_k-\frac{2s}3$, so a stream frequency $q_k+j$ has the divisors
$j-\frac{2s}3\ne0$ and $2q_k+j+\frac{2s}3>0$.
For $k\ge7$ every $q_k+j$ that occurs is at least $q_k-11=2k-13\ge1$, so the folding $\sin(-m\theta)=-\sin m\theta$, the
omission of the zero stream mode and the choice of Poisson branches are the same for every $k\ge7$, and the symbolic
computation is exact there. It also agrees with the direct computation at $k=4,5,6$. The four coefficients of $\mathcal N(k,\cdot)$
have no common zero (their gcd in $\mathbb Q[k]$ is 1), and $\lim_{k\to\infty}\sigma_k=\sigma_\infty=-(75b^3+6735b^2-2925b+314)/129600$.
$\mathcal P_6$ has content 1 and is irreducible over $\mathbb Q$ (exact factorization; an independent certificate: its
reduction modulo 19 has a unit leading coefficient and, after normalization, is $h=b^6-3b^5-4b^4-4b^3+b^2-4b-4$, with
$\gcd(h,b^{19^j}-b)=1$ for $j=1,2,3$, so $h$ has no factor of degree at most 3 over $\mathbb F_{19}$), and exact real-root
isolation gives the two stated intervals. So $b$ is algebraic of degree 6, and no nonzero rational polynomial of degree at
most 3 vanishes at $b$. Hence
$\sigma_k\ne0$ for every $k\ge2$ and $\sigma_\infty\ne0$, so $\sigma_*>0$. Homogeneity extends this to $\varepsilon f_1$. $\square$

Proof of (b). Take $\varepsilon=1$; $R_2$ scales by $\varepsilon^9$. Compute $f_2,\dots,f_9$ with $H_6=0$ in $\mathbb Q[b]$, reducing
modulo $\mathcal P_6$ after each order; this is the computation in the field $\mathbb Q(b_i)$. The coefficient of $\sin3\theta$
in $f_9$ is a nonzero rational polynomial of degree 5 in $b$. It does not vanish at $b_i$ because $\mathcal P_6$, of degree
6, is the minimal polynomial of $b_i$. $\square$

Proof of (c) (exact rational interval arithmetic; the accompanying artifacts). On rational isolating intervals of width
$10^{-40}$ every polynomial in $b>0$ is bounded termwise by monotonicity. This gives $\sigma_4<0$ at both roots, a constant
sign of $\sigma_k$ for $k=2,3,5,6$ and $|\sigma_k|-|\sigma_4|\ge1.17\cdot10^{-5}$ ($b_1$), $\ge1.15\cdot10^{-3}$ ($b_2$), the
smallest gap being at $k=5$. For $k\ge7$ write $\sigma_k=-(k-1)(2k-1)^2\mathcal N(k,b)/D(k)$ as above; $D(t+7)$ has positive
coefficients in $t$, and every one of the 12 coefficients in $t$ of $\sigma_4(b)D(t+7)+(t+6)(2t+13)^2\mathcal N(t+7,b)$ is
positive on the isolating intervals (smallest lower bounds $1.42\cdot10^6$ and $7.38\cdot10^7$). So
$\sigma_4D(k)+(k-1)(2k-1)^2\mathcal N(k,b)>0$, that is $\sigma_k<\sigma_4$, for every $k\ge7$. $\square$

The same computation gives $H_6=-R_2/\sigma_2$ exactly: $H_6=1.306821685959859169015207\cdot10^{-6}$ for $b_1$ and
$H_6=7.390373331408422\cdot10^{-5}$ for $b_2$.

Values. For $b_1$: $\sigma_2=-2.794\cdot10^{-4}$, $\sigma_3=-7.579\cdot10^{-4}$, $\sigma_4=-3.812\cdot10^{-5}$,
$\sigma_\infty=-1.948\cdot10^{-4}$. For $b_2$: $\sigma_2=1.036\cdot10^{-2}$, $\sigma_3=-3.227\cdot10^{-2}$, $\sigma_4=-1.568\cdot10^{-3}$,
$\sigma_\infty=-9.702\cdot10^{-3}$. For both roots, among $2\le k\le10^5$ the modulus $|\sigma_k|$ is smallest at $k=4$, and
$\sigma_k$ has no sign change for $7\le k\le10^5$ (evaluation of the exact formulas); part (c) proves both statements
for all $k$.

Corollary T.4 (explicit radii; PROVED: independent proofs, reviewed here, with independent exact checks). For the
profiles of Corollary T.3 the tuned density and stream series converge, with every Cartesian derivative series and the
radial weights of item 2, absolutely and uniformly on $r\ge R$ whenever $R>2^{63}|\varepsilon|^{3/2}$; for $b_1$ already
when $R>2^{57}|\varepsilon|^{3/2}$, and for $b_2$ when $R>2^{51}|\varepsilon|^{3/2}$.

Proof. Take $\varepsilon=1$ and scale at the end ($f_n$, $g_n$, $H_n$ scale by $\varepsilon^n$). First, $|\sigma_k|\ge10^{-5}$ for
every $k\ge2$ at both roots, by exact rational inequalities: for $k\le6$ by evaluating the cubics $\sigma_k$ on rational
isolating intervals of width $10^{-30}$, termwise monotonically in $b>0$; for $k\ge7$ because, after the substitution $k=t+7$,
every coefficient in $t$ of $-(k-1)(2k-1)^2\mathcal N(k,b)-10^{-5}D(k)$, with $D(k)>0$ the denominator in the formula for
$\sigma_k$, is a cubic in $b$ that is positive on the isolating intervals (so $\sigma_k\le-10^{-5}$ for all $k\ge7$). Next,
$\|f_1\|_{\ell^1}=1+b\le2$ and $\kappa=\frac{28}3\le10$, and the right sides of (I1) to (I3) increase with $x_1$, $\kappa$ and
$1/\sigma_*$, so the majorants are dominated by those with $a=x_1=2$, $\kappa=10$, $\sigma_*=10^{-5}$, for which $x_2\le d=60$
and $x_3\le e=3600$. Write the generating-function system of the proof of item 1 as $Y=\Phi(z,Y)$,
$Y=(W,\hat U,\hat V,\hat E)$, $\Phi=c+JY+z\Psi(z,Y)$ with $c=\Phi(0,0)$, $J$ the constant strictly lower triangular matrix of
Step 4 and $\Psi$ a polynomial with nonnegative coefficients. With $Q=I+J+J^2+J^3=(I-J)^{-1}$ the system reads
$Y=Qc+zQ\Psi(z,Y)$, and exact integer arithmetic gives $Qc=(270000,\,22680000,\,2041200000,\,19245600000000000)\le M:=2^{55}$
and $\max_iQ\Psi(1,2M,2M,2M,2M)_i<2^{153}\le2^{120}M$. Hence for $0\le z\le z_0=2^{-120}$ and $0\le Y\le2M$ the right side
is at most $2M$. Iterate $Y\mapsto Qc+zQ\Psi(z,Y)$ from $Y=0$: the iterates are polynomials in $z$ with nonnegative
coefficients that increase, each coefficient is constant after finitely many steps (every nonconstant term has a factor
$z$), so the iterates converge coefficientwise to the formal majorant solution, and their values at $z_0$ stay below $2M$.
So the majorant coefficients are at most $2Mz_0^{-m}$, and $x_n$, $\eta_n$ are bounded geometrically with base $2^{120}$.
The proof of items 2 to 4 then applies with $A=2^{120}$, which gives $r>2^{180}$.

The scalar box wastes a lot. With the same transformed map $G(z,Y)=Qc+zQ\Psi(z,Y)$, any vector $\mathcal B\ge Qc$ with
$G(z_0,\mathcal B)\le\mathcal B$ componentwise bounds the iterates at $z_0$ (for $0\le z\le z_0$ and $0\le Y\le\mathcal B$,
$G(z,Y)\le G(z_0,\mathcal B)\le\mathcal B$ by the nonnegativity of $Q$ and $\Psi$), and the argument above goes through with base
$z_0^{-1}$. Take $\mathcal B=2Qc$. Exact rational arithmetic gives $\max_iG_i(z_0,\mathcal B)/\mathcal B_i=0.86835$ at
$z_0=2^{-42}$ for $a=2$, $\kappa=10$, $\sigma_*=10^{-5}$, hence $r>2^{63}$. With the per-root parameters $a=1.281$, $\sigma_*=3.8124\cdot10^{-5}$
($b_1$) and $a=1.647$, $\sigma_*=1.5683\cdot10^{-3}$ ($b_2$), $\kappa=\frac{28}3$, which are admissible by Corollary T.3(c) and
$1+b_1<1.281$, $1+b_2<1.647$, the ratios are $0.69742$ at $z_0=2^{-38}$ and $0.70983$ at $z_0=2^{-34}$, hence $r>2^{57}$ and
$r>2^{51}$. (At $z_0=2^{-40},2^{-36},2^{-32}$ the box $2Qc$ fails; that says nothing about convergence.) $\square$

Sharper constants (PROVED: proof here, independently confirmed with independent exact supersolutions). The same argument with $a$ at most $1.2807$ ($b_1$) and
$1.6464$ ($b_2$), $\kappa=\frac{28}3$ and $\sigma_*=3.8\cdot10^{-5}$ ($b_1$), $1.5\cdot10^{-3}$ ($b_2$) (Corollary T.3(c)), with an
exact rational supersolution $\Phi(z_1,\hat Y)\le\hat Y$ (which implies $G(z_1,\hat Y)\le\hat Y$) at $z_1=1.1380\cdot10^{-11}$ ($b_1$)
and $z_1=1.6448\cdot10^{-10}$ ($b_2$), where $\hat Y$ is a rounded-up numerical fixed point at a slightly larger $z$,
gives convergence for $R>2.61\cdot10^{16}|\varepsilon|^{3/2}\approx2^{54.5}|\varepsilon|^{3/2}$ ($b_1$) and
$R>4.75\cdot10^{14}|\varepsilon|^{3/2}\approx2^{48.8}|\varepsilon|^{3/2}$ ($b_2$). An independent check with its own rational
supersolutions at $z_0=1138\cdot10^{-14}$ and $1644\cdot10^{-13}$ gives the slightly smaller sufficient thresholds
$2.6049\cdot10^{16}$ and $4.7440\cdot10^{14}$. Here
$z_1$ is $0.99$ times the critical value of the majorant system found by bisection ($1.1495\cdot10^{-11}$ and
$1.6614\cdot10^{-10}$), so a substantially better radius needs a sharper majorant, not a better supersolution. The loss
comes mainly from the factor $\kappa/\sigma_*$ in (I3). The measured growth constants below suggest radii near $0.13$ and $0.63$.

Proposition T.5 (a convergent potential series; PROVED: independent proof, reviewed here). Under the hypotheses of
Theorem T, with $A$ from item 1, there are cosine polynomials $C_n$ in even frequencies with $\deg C_n\le Bn-2$ and
$\|C_n\|_{\ell^1}\le C'A^n$, and real constants $\alpha,\beta,\lambda$, such that
$$\chi=\sum_{n\ge1}r^{4-2n/3}C_n(\theta)+r^2\log r\,(\alpha+\beta\cos2\theta)+\lambda\log r$$
and each of its Cartesian derivative series of order $h$, with the weight $r^{h-10/3}$, converge absolutely and uniformly on
$r\ge R$ for every $R>A^{3/2}$; $\chi$ is even in $x$ and in $y$, real analytic on $r>A^{3/2}$, and $\chi_{xy}=\psi$,
$-\partial_y\Delta\chi=\rho$ there. The logarithms occur only at orders 3 and 6.

Proof. Put $S_n=4-2n/3=p_n+3$ and $x=n/3-1$, and write the density coefficients of $f_n$ as $a_m$ at frequency $2m+1$,
$0\le m\le K=(Bn-2)/2$. For $\Delta(r^{S_n}C_n)=r^{-2x}\sum_md_m\cos2m\theta$ the equation $-\partial_y\Delta\chi_n=r^{p_n}f_n$ reads
$a_0=2xd_0+(1-x)d_1$, $a_m=(m+x)d_m+(m+1-x)d_{m+1}$ ($m\ge1$, $d_{K+1}=0$), from
$-\partial_y(r^q\cos M\theta)=r^{q-1}[\frac{M-q}2\sin(M+1)\theta+\frac{M+q}2\sin(M-1)\theta]$. For $n\ge12$ ($x\ge3$) descending
substitution has ratios $|m+1-x|/(m+x)\le1$ and $|1-x|/(2x)\le1$, so $|d_m|\le x^{-1}\sum_{j\ge m}|a_j|$ and
$\|d\|_{\ell^1}\le\frac{K+1}x\|f_n\|_{\ell^1}\le2B\|f_n\|_{\ell^1}$. The Laplacian multiplies $r^{S_n}\cos2m\theta$ by $S_n^2-4m^2$, which
vanishes only for $n=3k$, $m=k-2$; there the density relation is $a_{k-2}=(2k-3)d_{k-2}$ and $a_{k-2}=O_{3k}=0$, so
$d_{k-2}=0$ and that mode is not needed. Otherwise $|S_n^2-4m^2|\ge\frac23\cdot\frac n3$ for $n\ge12$, so the potential $C_n^0$ has
$\|C_n^0\|\le\frac{9B}n\|f_n\|$. Its stream solves the same Poisson equation as $g_n$, so it equals $g_n$ except at $n=3k$,
where they differ by a multiple of $r^{2-2k}\sin(2k-2)\theta$; since
$\partial_x\partial_y(r^{-\ell}\cos\ell\theta)=\ell(\ell+1)r^{-\ell-2}\sin(\ell+2)\theta$ and $r^{-\ell}\cos\ell\theta$ is harmonic, adding
$[\ell(\ell+1)]^{-1}(H_n-H_n^0)\cos\ell\theta$, $\ell=2k-4$, matches the whole resonant stream coefficient without changing the
density. Two Cartesian derivatives cost at most $(B+1)^2n^2$ in $\ell^1$, and $\ell(\ell+1)\ge n^2/9$, so
$\|C_n\|\le9B[1+9(B+1)^2]\|f_n\|/n+9\|g_n\|/n^2$ for $n\ge12$. For $n<12$, $n\ne3,6$, the triangular system has nonzero
diagonal and the multipliers are nonzero except at $n=9$, which is treated as above with $\ell=2$. At $n=3$ ($S_3=2$, $x=0$) the
pure columns $r^2\cos2m\theta$, $m\ge2$, remove the density modes of frequency at least 5, and the residual
$a\sin\theta+a'\sin3\theta$ is produced by $r^2\log r$ (density $-4r^{-1}\sin\theta$, stream $\sin2\theta$) and
$r^2\log r\cos2\theta$ (density $4r^{-1}(\sin\theta+\sin3\theta)$, stream $-\frac12\sin4\theta$), with $\alpha=(a'-a)/4$, $\beta=a'/4$;
the stream then equals $g_3$ because $P_3=0$ has no positive even sine kernel. At $n=6$ ($S_6=0$) $O_6=a_0=0$, the columns
$\cos2m\theta$, $m\ge1$, produce the density, and $\lambda\log r$, with $\partial_x\partial_y\log r=-r^{-2}\sin2\theta$ and $\Delta\log r=0$,
matches the resonant stream coefficient $H_6$. The weighted derivative series converge as in item 2, and the logarithmic
terms have radial order below $10/3$. $\square$

Theorem T.6 (stability on the compatibility hypersurface; PROVED: independent proof, reviewed here, with independent
checks). Fix an even $B\ge4$, let $\mathcal S_B$ be the complex space of sine polynomials $f=\sum_{j\text{ odd},\,j<B}c_j\sin j\theta$
with $\|f\|_1=\sum|c_j|$, and let $O_6(f)$ and $\sigma_k(f)$ be the obstruction and the responses of Theorem T for $f_1=f$
(homogeneous polynomials of degrees 6 and 3 in the $c_j$). Put $\kappa=7B/3$ and $M_B=10\kappa^3(\frac32)^2$.

(a) $|\sigma_k(f)|\le M_B\|f\|_1^3$ for every $k\ge2$ and $f\in\mathcal S_B$.

(b) Let $f_*$ be real with $\inf_k|\sigma_k(f_*)|\ge s_*>0$ and $\|f_*\|_1\le A_0$. If
$\|f-f_*\|_1<\min\{1,\,s_*/(2M_B(A_0+2)^3)\}$, then $|\sigma_k(f)|>s_*/2$ for every $k\ge2$. So every real $f$ in this ball
with $O_6(f)=0$ satisfies the hypotheses of Theorem T with the common constants $\|f\|_1\le A_0+1$, $B$, $\sigma_*=s_*/2$,
and all the tuned series converge, with all weighted derivatives, on one common exterior.

(c) For $B=6$ and $f_*=\sin\theta+b_i\sin3\theta$ ($i=1,2$), the equation $O_6(\sin\theta+b\sin3\theta+\tau\sin5\theta)=0$
defines a real analytic function $b(\tau)$ near $\tau=0$ with $b(0)=b_i$, and for small real $\tau$ the profiles
$\varepsilon(\sin\theta+b(\tau)\sin3\theta+\tau\sin5\theta)$ have convergent tuned pure series. This is a one-parameter family of
shapes, not only amplitudes; more higher modes give more parameters.

Proof. (a) Fix $n=3k$ and change $H_n$ by $1$. Up to order $n+3$ every product contains at most one factor of index $\ge n$
($2n>n+3$), so the density changes $\varphi_s$ at orders $n+s$, $s=1,2,3$, are exactly linear in this change and involve
only $f_1,f_2,f_3$, $g_1,g_2$ and the unit harmonic; $\sigma_k$ is one sine coefficient of $\varphi_3$. With $x_i=i\|f_i\|_1$
and $y_s=(n+s)\|\varphi_s\|_1/n$, the bilinear bound $\kappa ij\|g_i\|\|f_j\|$, the factor $m/(2(m-1))\le1$ and the Poisson bound
$\frac32$ at the nonresonant orders $n+1,n+2$ (proof of item 1) give $y_1\le\kappa x_1$, $y_2\le\kappa(x_2+3x_1y_1)$,
$y_3\le\kappa(x_3+3x_2y_1+3x_1y_2)$, where the first term is the direct harmonic contribution and the factor $3=2\cdot\frac32$
counts the two orientations of each pair. With $x_1=a=\|f\|_1$, $x_2\le\frac32\kappa a^2$, $x_3\le\frac92\kappa^2a^3$ this gives
$y_1\le\kappa a$, $y_2\le\frac92\kappa^2a^2$, $y_3\le\frac{45}2\kappa^3a^3=M_Ba^3$, and $|\sigma_k|\le\|\varphi_3\|_1\le y_3$. The norm
estimates use only the triangle inequality, so they hold for complex coefficients. (b) For $\|f-f_*\|_1\le1$ and
$\|h\|_1=1$ the cubic polynomial $z\mapsto\sigma_k(f+zh)$ is bounded by $M_B(A_0+2)^3$ on $|z|=1$, so by Cauchy's estimate
$|D\sigma_k(f)h|\le M_B(A_0+2)^3$ for every $k$; integration along the segment from $f_*$ to $f$ gives
$|\sigma_k(f)-\sigma_k(f_*)|<s_*/2$. The rest is Theorem T, whose majorant system depends only on $\|f\|_1$, $B$ and
$\sigma_*$. (c) At $\tau=0$, $O_6=\mathcal P_6(b)/35818438656000000$, and $\mathcal P_6$ is irreducible, so its roots are simple and
$\partial_bO_6\ne0$ at $(b_i,0)$; the implicit function theorem gives $b(\tau)$, real for real $\tau$, and $\|f_\tau-f_*\|_1=
|b(\tau)-b_i|+|\tau|\to0$, so (b) applies with $s_*=10^{-5}$ (Corollary T.3(c)). $\square$

Corollary T.7 (explicit three-mode families; PROVED: independent proof, reviewed here, with independent exact checks).
Let $t_1=10^{-13}$ and $t_2=10^{-14}$, and let $m_i$ be the midpoint of a rational isolating interval of $b_i$ of width at
most $10^{-20}$. For $i=1,2$ and every real $\tau$ with $|\tau|\le t_i$ there is exactly one $b$ with $|b-m_i|<10^{-13}$ and
$O_6(\sin\theta+b\sin3\theta+\tau\sin5\theta)=0$;
it is the real analytic branch $b(\tau)$ of Theorem T.6(c), with $b_1'(0)=0.826960117499745\ldots$ and
$b_2'(0)=1.388318047714879\ldots$. For these $\tau$ and every real $\varepsilon\ne0$, the tuned pure series of
$f_1=\varepsilon(\sin\theta+b(\tau)\sin3\theta+\tau\sin5\theta)$ converges with all weighted derivatives on $r>2^{72}|\varepsilon|^{3/2}$, and
its sums depend real analytically on $\tau$.

Proof. Write $[l,u]$ for the isolating interval, $m=m_i$, and expand $O(m+x,\tau)=\sum c_{jl}x^j\tau^l$ exactly (total degree 6). With $h=10^{-13}$, exact arithmetic gives
$\sum_{(j,l)\ne(1,0)}|c_{jl}|h^jt_i^l<|c_{10}|h$, with ratio $0.82696$ ($i=1$) and $0.13883$ ($i=2$). By Rouche's theorem on
$|x|=h$ there is exactly one zero, simple, for each $|\tau|\le t_i$; at $\tau=0$ it is $b_i$, and conjugation symmetry makes it
real for real $\tau$. The profile distance is less than $h+(u-l)/2+t_i<2.1\cdot10^{-13}<1/790272000000$, the radius of
Theorem T.6(b) for $B=6$, $A_0=2$, $\kappa=14$, $s_*=10^{-5}$ ($M_B=61740$). So all these profiles have $\|f\|_1\le3$ and
$|\sigma_k|\ge1/200000$, and the componentwise box of Corollary T.4 with $a=3$, $\kappa=14$, $\sigma_*=1/200000$ passes at
$z_0=2^{-48}$ (ratio $0.72386$), which gives $r>2^{72}$ (the scalar box gives $2^{240}$). The coefficients are rational
functions of $(b,\tau)$ with denominators products of the $\sigma_j$, and the majorant bounds also hold for complex $\tau$ in
the disk, so the sums are uniform limits of functions holomorphic in $\tau$. $\square$

Theorem T.8 (the response condition is generic on the compatibility hypersurface; PROVED: proof here, independently
confirmed by a second derivation). Fix an even $B\ge4$ and use the notation of Theorem T.6.

(a) Let $k_0=\frac{3B}2+1$. There are a polynomial $D_B(k)$ without zeros at integers $k\ge k_0$ and a polynomial
$N_B(k,f)$, homogeneous of degree 3 in the coefficients of $f$, with $\sigma_k(f)=N_B(k,f)/D_B(k)$ for all $k\ge k_0$ and all
$f\in\mathcal S_B$. The limit $\sigma_\infty(f)=\lim_{k\to\infty}\sigma_k(f)$ exists, is a cubic form in $f$, and the convergence
is uniform on bounded subsets of $\mathcal S_B$.

(b) Let $Z$ be a connected real analytic submanifold of $\{f\in\mathcal S_B\text{ real}:O_6(f)=0\}$ that contains one
profile satisfying (T-b). Let $G\subset Z$ be the set of profiles satisfying (T-b). Then $G$ is open in $Z$, and
$Z\setminus G$ is contained in $\{\sigma_\infty=0\}\cup\bigcup_{k\ge2}\{\sigma_k=0\}$, a countable union of proper analytic subsets
of $Z$. So $G$ is open and dense in $Z$ and $Z\setminus G$ has measure zero; near every point of $Z$ with $\sigma_\infty\ne0$,
$Z\setminus G$ is a finite union of proper analytic subsets. For every $f\in G$ Theorem T gives a convergent tuned pure series.

(c) In particular, along the real analytic continuation of either curve $b(\tau)$ of Theorem T.6(c) (as a connected
analytic curve in $\{O_6=0\}$), the tuned series converges for all parameters except a countable set, closed in the parameter interval
of the curve, whose accumulation points inside that interval are among the isolated zeros of $\sigma_\infty$ on the
curve. Nothing is asserted about convergence or divergence at the exceptional parameters. (Theorem T_Q.5 in Section 12.5
removes the hypothesis that $Z$ contains an admissible profile, for regular components of the normalized hypersurface.)

Proof. (a) The frequencies of $f_1,f_2,f_3$ are at most $B-1,2B-1,3B-1$ and those of $g_1,g_2$ at most $B,2B$. So every
frequency in $\varphi_1$, $\Pi_{n+1}\varphi_1$, $\varphi_2$, $\Pi_{n+2}\varphi_2$, $\varphi_3$ is $q_k+j$ with an integer offset $|j|$ at
most $B-1$, $B$, $2B-1$, $2B$, $3B-1$ respectively. For $k\ge k_0$, $q_k=2k-2\ge3B$, so all these frequencies are at least
$1$, the density frequencies entering $\Pi_{n+1},\Pi_{n+2}$ are at least $3$, and no folding $\sin(-m\theta)=-\sin m\theta$, no
omitted zero stream mode and no change of Poisson branch occurs. Then the bookkeeping of offsets is independent of $k$,
and each coefficient of $\varphi_s$ at offset $j$ is obtained from the coefficients of $f_1,f_2,f_3,g_1,g_2$ by sums of
products with factors $P_i,p_j$ (constants or affine in $k$), derivative factors $q_k+j$ (affine in $k$), and divisions by
$\lambda_{n+s}=2(3k+s-1)$ and by the Poisson divisors $2(q\pm P_{n+s})$, which equal $2(j-\frac{2s}3)\ne0$ and
$2(2q_k+j+\frac{2s}3)>0$. This gives $N_B$ and $D_B$ (the product of the divisors used). By Theorem T.6(a),
$|\sigma_k(f)|\le M_B\|f\|_1^3$ for all $k$. Each coefficient of a cubic monomial in $\sigma_k$ is a fixed linear combination of the
values $\sigma_k(f^{(i)})$ at finitely many profiles $f^{(i)}$, so it is a rational function of $k$ that is bounded for
$k\ge k_0$, hence has a finite limit as $k\to\infty$. This gives $\sigma_\infty$ and the uniform convergence on bounded sets.
(b) Openness: if $f_0\in G$ then $|\sigma_\infty(f_0)|\ge\inf_k|\sigma_k(f_0)|>0$. By uniform convergence and continuity there
are $K$ and a neighborhood $V$ of $f_0$ with $|\sigma_k|\ge\frac12|\sigma_\infty(f_0)|$ on $V$ for $k\ge K$, and the finitely many
$\sigma_k$, $k<K$, are nonzero at $f_0$ and hence bounded away from zero on a smaller neighborhood. The same argument shows
that a profile with $\sigma_\infty\ne0$ and $\sigma_k\ne0$ for every $k$ lies in $G$, which is the stated inclusion, and that
near a point with $\sigma_\infty\ne0$ only finitely many $\sigma_k$ can vanish. Each $\sigma_k$ and $\sigma_\infty$ is a polynomial,
so its restriction to $Z$ is real analytic; it is nonzero at the given profile of $G$, so it does not vanish identically
on the connected manifold $Z$, and its zero set is a closed proper analytic subset, nowhere dense and of measure zero. A
countable union of such sets is meager and of measure zero, so its complement is dense by Baire's theorem. (c) is (b)
for a curve, where proper analytic subsets are discrete. $\square$

Remark. Theorem T.8 says nothing about components of $\{O_6=0\}$ that contain no verified profile, and $\{O_6=0\}$
itself has measure zero in $\mathcal S_B$: the pure series exists only for a codimension-one set of profiles (on its
complement it is obstructed at order 6 for every choice of constants).

Proposition T.9 (the three-mode limiting response; PROVED: independent proof, reviewed here, with an independent exact
recomputation). Let $B=6$ and $f=\sin\theta+b\sin3\theta+\tau\sin5\theta$, $(b,\tau)$ real or complex. For every integer
$k\ge10$, $\sigma_k=N(k,b,\tau)/D(k)$ with polynomials $N$ and $D$ (Theorem T.8(a), $k_0=10$), and
$$\sigma_\infty(b,\tau)=-\frac{254100b^3+8113875b^2\tau+22818180b^2-3679500b\tau^2-12142680b\tau-9909900b+8130900\tau^2+1353264\tau+1063832}{439084800}.$$
The resultant $\operatorname{Res}_b(O_6,\sigma_\infty)$ is a nonzero polynomial of degree 18 in $\tau$ with exactly two real
roots, $\tau_-=-3.0164889488602\ldots$ and $\tau_+=98.6039033811810\ldots$. Hence $\sigma_\infty\ne0$ at every real profile
of this form with $O_6=0$ and $\tau\notin\{\tau_-,\tau_+\}$, in particular whenever $-3\le\tau\le98$. On every compact arc of
the real curve $\{O_6(b,\tau)=0\}$ along which $-3\le\tau\le98$, condition (T-b) fails at no more than finitely many points,
and at all other points of the arc Theorem T gives a convergent tuned series. Nothing is claimed about which real
branch, if any, passes over $\tau_\pm$.

Proof. The formula is the computation of Theorem T.8(a) with symbolic $k$ (coefficients in $\mathbb Q(k)[b,\tau]$); it agrees
with direct computations at $k=10,\dots,14$, $\sigma_\infty$ is its termwise limit, and at $\tau=0$ it is the $\sigma_\infty$ of
Corollary T.3. The coefficient of $b^6$ in $O_6$ is a nonzero constant (proof of Theorem T_Q.5), so the resultant vanishes at
the $\tau$ of every common zero; it is nonzero by Theorem T_Q.5, its degree is at most $3\cdot6+6\cdot3-18=18$ from the
Sylvester determinant (total degrees 6 and 3), and exact real root isolation gives the two roots. On a compact arc $\Gamma$
as stated, $|\sigma_\infty|\ge2\eta>0$ on $\Gamma$, so by the uniform convergence of Theorem T.8(a) there is $K$ with
$|\sigma_k|\ge\eta$ on $\Gamma$ for $k\ge K$. Each $\sigma_k$ with $k<K$ vanishes at finitely many points of $\{O_6=0\}$: its
resultant with $O_6$ is a nonzero polynomial in $\tau$ (Theorem T_Q.5) and each fiber has at most 6 points. $\square$

Corollary T.10 (larger explicit three-mode families; PROVED: independent proof, reviewed here, with independent exact
checks). Let $m_i$ be the rational midpoint of the isolating interval of $b_i$ used in the certificate (width at most
$10^{-30}$; $m_1=0.2806616627319\ldots$, $m_2=0.6463522898809\ldots$), and put
$(t_1,h_1,s_1,a_1)=(\frac1{512},\frac1{256},10^{-5},\frac{1287}{1000})$, $(t_2,h_2,s_2,a_2)=(\frac1{128},\frac1{64},\frac1{2000},\frac{167}{100})$.
For $i=1,2$ and every real $\tau$ with $|\tau|\le t_i$ there is exactly one $b$ with $|b-m_i|<h_i$ and
$O_6(\sin\theta+b\sin3\theta+\tau\sin5\theta)=0$; it is the branch $b_i(\tau)$ of Theorem T.6(c) and Corollary T.7. For these
profiles $|\sigma_k|\ge s_i$ for every $k\ge2$, and for every real $\varepsilon\ne0$ the tuned pure series of
$\varepsilon(\sin\theta+b_i(\tau)\sin3\theta+\tau\sin5\theta)$ converges with all weighted derivatives on $r>2^{63}|\varepsilon|^{3/2}$
($i=1$) and $r>2^{57}|\varepsilon|^{3/2}$ ($i=2$), and its sums depend real analytically on $\tau$. The disks are about $10^{10}$
times wider than those of Corollary T.7, and the exteriors are smaller.

Proof. Write $m=m_i$, $t=t_i$, $h=h_i$, $s=s_i$ and expand exactly $O_6(m+x,\tau)=\sum c_{jl}x^j\tau^l$,
$\sigma_k(m+x,\tau)=\sum d_{k,jl}x^j\tau^l$ for $2\le k\le9$, and, with $k=10+w$, $N(10+w,m+x,\tau)=\sum n_{\ell jl}w^\ell x^j\tau^l$
and $D(10+w)=\sum D_\ell w^\ell$. Exact rational arithmetic gives: (1) $\sum_{(j,l)\ne(1,0)}|c_{jl}|h^jt^l<|c_{10}|h$ (ratios
$0.52882$ and $0.99830$); (2) $|d_{k,00}|-\sum_{(j,l)\ne(0,0)}|d_{k,jl}|h^jt^l>s$ for $2\le k\le9$; (3) after one common sign
change of $N$ and $D$, $D_\ell\ge0$ for all $\ell$, $D_0>0$, and $-n_{\ell00}-\sum_{(j,l)\ne(0,0)}|n_{\ell jl}|h^jt^l-sD_\ell\ge0$ for
every $\ell$, strictly for $\ell=0$. By (1) and Rouche's theorem on $|x|=h$, for every complex $|\tau|\le t$ there is exactly
one zero in $|x|<h$, and it is simple; at $\tau=0$ it is $b_i$, and conjugation symmetry makes it real for real $\tau$. By
(2) and (3), for complex $|x|\le h$, $|\tau|\le t$ and every $k\ge2$ we get $|\sigma_k|>s$: for $k\le9$ by the triangle
inequality (each finite response keeps its own sign; $\sigma_2>0$ on the second family while $\sigma_\infty<0$), and for
$k\ge10$ because $\operatorname{Re}(-N(10+w,\cdot))\ge sD(10+w)>0$ for real $w\ge0$. Then $\|f_1\|_{\ell^1}\le1+|m|+h+t\le a_i$, and
the componentwise box of Corollary T.4 (the system of Section 12.5, Step 4, at $Q=3$, $B=6$, $\kappa=14$) with
$(a_i,s_i)$ passes at $z_0=2^{-42}$ and $2^{-38}$ (largest component ratios $0.743$ and $0.720$), which gives $R>z_0^{-3/2}$.
Holomorphy in $\tau$ follows as in Corollary T.7. $\square$ The inequalities (1) to (3) and the box tests were computed twice,
by a Cartesian-monomial program and by an independent Fourier-coefficient program, with identical circle ratios; the
next dyadic values $z_0=2^{-41}$ and $2^{-37}$ also pass (ratios $0.985$ and $0.94$), so the exteriors $r>2^{61.5}$ and
$2^{55.5}$ times $|\varepsilon|^{3/2}$ are also admissible.

Numerical evidence (accompanying artifacts; NUMERICAL EVIDENCE). With $\varepsilon=1$ the tuned series was computed in
double precision to order 240 (fast Fourier transforms on 4096 points, with the exact frequency support imposed at
each order, $H_n$ fixed by a finite-difference slope) and, for $b_1$, in 40-digit arithmetic to order 30 with
$H_n=-R_k/\sigma_k$. The runs agree. The 40-digit run reproduces the exact $H_6$ to 25 digits and gives
$H_9=2.255085806559639\cdot10^{-9}$, $H_{12}=1.724168205113161\cdot10^{-10}$, $H_{15}=-1.796939693571644\cdot10^{-11}$, with
residual obstructions $|O_{3k}|\le6\cdot10^{-48}$; in double precision the residual obstructions are below $10^{-16}\|f_n\|$.
The finite-difference slopes agree with the exact $\sigma_k$ to the printed five digits. For $b_1$ the root test gives
$\|f_n\|_{\ell^1}^{1/n}=0.151$ at $n=12$, $0.241$ at $n=90$ and $0.251$ at $n=240$, increasing slowly; least-squares fits of
$\log\|f_n\|_{\ell^1}=n\log A+\beta\log n+\text{const}$ over $n\ge60$ and over $n\ge120$ give $A=0.259$ and $A=0.261$, and
$|H_n|^{1/n}=0.250$ at $n=225$. For $b_2$ the values are $0.711$ at $n=240$, fitted $A=0.733$ and $0.731$, and
$|H_n|^{1/n}=0.704$ at $n=225$. The fitted $\beta$ is not stable, so only $A$ is reported. These rates are consistent with
the geometric bound of Theorem T and suggest convergence for $r>A^{3/2}$, about $r>0.13$ for $b_1$ and $r>0.63$ for $b_2$;
the proved radius of Corollary T.4 is far larger.

Remarks. 1. Theorem T concerns density and stream. The potential correspondence of Section 2.3 is exceptional at $n=3$
and $n=6$ ($n\delta\in\{2,4\}$). At $n=6$ the multipole $H_6r^{-2}\sin2\theta$ is the stream of $-H_6\log r$, since
$\partial_x\partial_y\log r=-r^{-2}\sin2\theta$, so a potential series may contain logarithms although density and
stream do not. Item 3 uses only Proposition 12.3; Proposition T.5 gives the potential as a convergent series whose only
logarithms are these, at orders 3 and 6.
2. For $f_1=\sin\theta$ (that is, $b=0$), $O_6=\mathcal P_6(0)/35818438656000000\ne0$, so the pure ansatz fails at order 6
for every choice of constants.
3. The proof uses $\delta=2/3$ through its constants and through the fact that the period 3 of the resonant orders is
smaller than the first resonant order 6, so that each obstruction is affine in the preceding constant. The same
holds at every $\delta=2/Q$, $Q\ge3$ an integer; Section 12.5 gives the analogue (Theorem T_Q) and explicit profiles at
$\delta=2/5$.
4. Compared with Theorem M (Section 12.1), the multipoles here are not prescribed but forced by the profile, and the
parameter is rational, where Theorem M does not apply.
5. The tuning constants do not reach the top frequency: $H_{3k}$ sits at frequency $2k-2<3kB$, and a product involving
$g_{3k}$ at order $3k+j$ has frequency at most $2k-2+Bj-1<B(3k+j)-1$. So the top coefficients of the tuned series are
the $A_n=(-1)^{n-1}\alpha^nh_n$ of Proposition 8.2 and Section 14.22, here with $B=4$ and $\alpha=\varepsilon b$. Hence
$\limsup_n\|f_n\|_{\ell^1}^{1/n}\ge|\alpha|/R_H$, with $R_H=4.103676$ at $\delta=2/3$, $B=4$: the growth constant is at least
$|\alpha|/R_H\approx0.06839$ for $b_1$ and $\approx0.15751$ for $b_2$ (rigorous decimal lower bounds $0.0683$ and $0.1575$) ($\varepsilon=1$; this inequality uses only Proposition 8.2 and the support
argument above, and holds for any pure series built on these profiles), consistent with the fitted $0.26$
and $0.73$. By Section 14.22(f), uniform termwise $C^2$ convergence of the tuned density series on $\{r\ge R\}$ requires
$R>(|\alpha|/R_H)^{3/2}$.
6. (The tuned series is not the limit of the nonresonant series of the same shape; PROVED: independent proof, reviewed
here, with certified intervals.) Fix $b=b_1$ or $b_2$ and $f_1=\sin\theta+b\sin3\theta$, and let $\delta\to\frac23$ through
nonresonant values, with no free constants. The stream mode $q$ at order $n$ is
$b_{n,q}=[(P_n-q)a_{n,q-1}+(P_n+q)a_{n,q+1}]/[2(q^2-P_n^2)]$. At $n=6$, $q=2$ the denominator has a simple zero at $\delta=\frac23$
($P_6=-2$) and the numerator vanishes there because $a_{6,1}(\frac23)=O_6=0$; so the coefficient extends analytically, with
limit $H_6^{\lim}=\frac1{12}a_{6,1}'(\frac23)+\frac18a_{6,3}(\frac23)$ ($'=d/d\delta$), and the orders 7 to 9 extend analytically as
well. Their limits are the $\delta=\frac23$ coefficients computed with $H_6=H_6^{\lim}$, so $a_{9,3}\to\sigma_2(H_6^{\lim}-H_6)$, where
$H_6$ is the tuned constant of Proposition T.2. At $n=9$, $q=4$ ($P_9=-4$) the numerator tends to $-8a_{9,3}$ and the
denominator has derivative $-144$, so $b_{9,4}$ has a simple pole at $\delta=\frac23$ with residue $\sigma_2(H_6^{\lim}-H_6)/18$
unless $H_6^{\lim}=H_6$. Interval arithmetic gives the residues $1.8474368363\ldots\cdot10^{-11}$ ($b_1$) and
$-5.2286526586\ldots\cdot10^{-8}$ ($b_2$), with $H_6^{\lim}\approx1.166\cdot10^{-7}$, $H_6\approx1.307\cdot10^{-6}$ and
$H_6^{\lim}\approx-1.698\cdot10^{-5}$, $H_6\approx7.390\cdot10^{-5}$. So for a fixed shape the nonresonant coefficients do not
converge to those of the tuned series as $\delta\to\frac23$. This concerns one coefficient of a fixed shape; it says nothing
about convergence at a fixed nonresonant $\delta$, and it does not exclude that a shape moving with $\delta$ removes the pole.
7. (A shape moving with $\delta$ removes every pole, formally; PROVED: independent proof, reviewed here.) Let
$t=\delta-\frac23$, let $b(t)$ be a formal power series with $b(0)=b_i$, and run the nonresonant recursion over $\mathbb R((t))$
with $f_1=\sin\theta+b(t)\sin3\theta$. (a) All coefficients through order 9 are regular at $t=0$ if and only if
$b'(0)=12(H_6-H_6^{\lim})/O_b$, where $O_b=\mathcal P_6'(b_i)/35818438656000000\ne0$ ($\mathcal P_6$ is irreducible, hence
square-free): by the quotient rule of Remark 6 the order-6 limit along the curve is $H_6^{\lim}+O_bb'(0)/12$, and the order-9
residue is $\sigma_2/18$ times its difference from $H_6$. The slopes are $-4.2923862068\ldots$ ($b_1$) and $5.8016929269\ldots$
($b_2$), with certified intervals; in the parameter $c$ they are divided by $9$. (b) There is a unique formal series
$b(t)=b_i+\sum_{j\ge1}\beta_jt^j$ for which every coefficient of the recursion is regular in $t$ and equals the tuned
coefficient at $t=0$. At $n=3k$ one has $P_n=-q_k-nt$; the denominator $2(q_k^2-P_n^2)$ has derivative $-4nq_k$ at $t=0$ and the
factor of $a_{n,q_k-1}$ in the numerator is $-2q_k$, so each resonant division turns a perturbation $\eta t^m$ of the
obstruction into $\eta t^{m-1}/(2n)$ in the resonant stream coefficient and loses exactly one power of $t$. By Lemma T.1 the
constant term of that coefficient at $n=3k$ is therefore affine in $\beta_{k-1}$, independent of $\beta_j$ for $j\ge k$, with
slope $C_k=O_b\prod_{\ell=2}^{k-1}\sigma_\ell\big/\prod_{r=2}^{k}(6r)\ne0$. Matching the tuned $H_{3k}$ fixes $\beta_{k-1}$, and
uniqueness follows from Proposition T.2 applied to the constant terms. An independent second-jet computation gives
$\beta_2\approx308.68293$ ($b_1$) and $-445.70127$ ($b_2$), reproduces $C_3=\sigma_2O_b/216$, and matches all 288 tuned
constants through $f_{12}$ and $g_{11}$ (NUMERICAL EVIDENCE, certified intervals). This is a formal statement in $\delta$: it
gives no bound on $\beta_j$, no analytic family of exact solutions at nearby $\delta$ (nearby rational exponents have their
own resonances and nearby irrational ones their own small divisors), and no exterior radius uniform in $\delta$.

Status. Corollary T.3(c), Corollary T.4 (radii $2^{63}$, $2^{57}$, $2^{51}$ times $|\varepsilon|^{3/2}$), Proposition T.5,
Theorem T.6, Corollary T.7, Proposition T.9 and Corollary T.10: PROVED (independent proofs, reviewed here; the exact checks
of T.3(c), T.4, T.7, T.9 and T.10, including the degree-6 obstruction polynomial in $(b,\tau)$, the limiting response and
its resultant, were repeated with independent code). Theorem T.8: PROVED (independently confirmed). The sharper radii after Corollary T.4: PROVED (independently
confirmed). Theorem T and Corollary T.3: PROVED. An independent audit confirmed Lemma T.1, Proposition T.2, the majorant
inequalities (I1) to (I3), the generating-function system and the triangular implicit function step; an independent
Cartesian implementation in exact rational arithmetic, sharing no code with the original, reproduced $O_6$, the response
coefficients $\sigma_2,\dots,\sigma_{12}$ and $\sigma_k$ symbolically in $k$, the gcd and limit, the irreducibility and
root isolation of $\mathcal P_6$ and the nonzero canonical obstruction at order 9 (both computations are in the
accompanying artifacts). The values in the last two paragraphs before the remarks
are NUMERICAL EVIDENCE.

### 12.5 Theorem T_Q: the same mechanism at every $\delta=2/Q$ (PROVED for every integer $Q\ge3$: proof here and an independent proof, compared line by line)

Theorem T is not special to $c=3$. What it uses is that the resonant orders form one arithmetic progression whose
period is smaller than its first term, so that each obstruction is affine in the preceding free constant. This holds
at every $\delta=2/Q$ with an integer $Q\ge3$ (for odd $Q$ these are the $\delta=a/b$ in lowest terms with $a=2$; for
even $Q$ they are the $\delta=1/b$, $b=Q/2\ge2$). In the notation of Section 14.2 these are exactly the rational $\delta$
with $h=1$.

Setting. Fix an integer $Q\ge3$ and put $\delta=2/Q$, $c=Q/(Q-2)$, $p_n=1-\frac{2n}Q$, $P_n=2-\frac{2n}Q$ and
$\lambda_n=(n-1)(c-1)=\frac{2(n-1)}{Q-2}$. The order equations (T1), (T2) of Section 12.4 hold verbatim (Section 14.1
at $D=0$ is stated for every $c$). Since $P_n\le2-\frac2Q<2$, (T2) is singular only when $P_n=-q$, that is at $n=kQ$,
$q=q_k:=2k-2$, $k\ge2$ (at $n=Q$ the only zero multiplier belongs to the absent mode $q=0$). There (T2) reads
$0=-q_ka_{kQ,q_k-1}$, so the obstruction is $O_{kQ}:=a_{kQ,\,2k-3}$, and $H_{kQ}:=b_{kQ,q_k}$ is free. Every other divisor
$q\pm P_n$ is a nonzero element of $\frac2Q\mathbb Z$, so $|q\pm P_n|\ge\frac2Q$. Define $\Pi_n$, $\Pi'_n$ and $e_k=\sin q_k\theta$
as in Section 12.4. For $Q=3$ everything below reduces to Section 12.4.

Response coefficients. For $k\ge2$ and $n=kQ$ define $\varphi_1,\dots,\varphi_Q$ by
$$\lambda_{n+r}\varphi_r=T_{n,r}(e_k,f_r)+\sum_{s=1}^{r-1}\big[T_{r-s,n+s}(g_{r-s},\varphi_s)+T_{n+s,r-s}(\Pi_{n+s}\varphi_s,f_{r-s})\big],
\qquad1\le r\le Q$$
(the orders $n+1,\dots,n+Q-1$ are not multiples of $Q$), and let $\sigma_k$ be the coefficient of $\sin((2k-1)\theta)$ in
$\varphi_Q$. It depends only on $f_1,\dots,f_Q$, $g_1,\dots,g_{Q-1}$ and $k$, and is homogeneous of degree $Q$ in $f_1$.

Lemma T_Q.1. Let $k\ge2$, $n=kQ$, and fix all constants except $H_n$. Then $f_{n+r}=f^{(0)}_{n+r}+H_n\varphi_r$ for
$1\le r\le Q$, and $O_{n+Q}=R_k+\sigma_kH_n$, where $R_k$ is the coefficient of $\sin((2k-1)\theta)$ in $f^{(0)}_{n+Q}$.

Proof. $H_n$ enters only through $g_n$; $f_n$ does not depend on it. A product $T_{i,j}(g_i,f_j)$ in which both factors
depend on $H_n$ has $i\ge n$ and $j\ge n+1$, hence order at least $2n+1>n+Q$, because $n\ge2Q$. So $f_m$ ($m\le n+Q$)
and $g_m$ ($m\le n+Q-1$) are affine in $H_n$, and the linear parts satisfy the recursion that defines the $\varphi_r$. The
low factors $f_r$ ($r\le Q$) and $g_{r-s}$ ($r-s\le Q-1$) contain no constant, since the first constant sits in $g_{2Q}$.
$\square$

Proposition T_Q.2. If $O_{2Q}(f_1)=0$ and $\sigma_k\ne0$ for all $k\ge2$, there is exactly one sequence $(H_{kQ})_{k\ge2}$
for which the pure ansatz solves every order, namely $H_{kQ}=-R_k/\sigma_k$, determined recursively in $k$. (As in
Proposition T.2.)

Theorem T_Q. Let $Q\ge3$ be an integer, $\delta=2/Q$, $c=Q/(Q-2)$, and let $f_1=\sum_{m\text{ odd},\,m\le L}a_{1,m}\sin m\theta$
be a nonzero real sine polynomial with $B=L+1$. Assume (T_Q-a) $O_{2Q}(f_1)=0$, and (T_Q-b) $\sigma_k\ne0$ for every
$k\ge2$ and $\sigma_*:=\inf_{k\ge2}|\sigma_k|>0$. Let $(H_{kQ})$ be the constants of Proposition T_Q.2. Then:

1. there are $C,A>0$ with $\|f_n\|_{\ell^1}+\|g_n\|_{\ell^1}\le CA^n$ for all $n\ge1$;
2. for $r>A^{Q/2}$ the series $\rho=\sum r^{p_n}f_n$ and $\psi=\sum r^{P_n}g_n$ converge absolutely, with every Cartesian
   derivative series, uniformly on $r\ge R$ for every $R>A^{Q/2}$ and for $\theta$ in a complex strip depending on $R$; the
   sums are real analytic on $r>A^{Q/2}$, contain no logarithm, have the S1 symmetry, and satisfy $-\Delta\psi=\partial_x\rho$
   and $c\,r\partial_r\rho+u\cdot\nabla\rho=\rho$ exactly; $\rho=r^{1-2/Q}f_1+O(r^{1-4/Q})$;
3. on $r>R_2$, for every $R_2>A^{Q/2}$, there are a $C^\infty$ potential (Proposition 12.3) and a single-valued pressure,
   as in Theorem T;
4. this is the only formal solution of this form with the S1 symmetry and leading term $f_1$. Replacing $f_1$ by
   $\varepsilon f_1$ preserves (T_Q-a) and (T_Q-b) (homogeneity of degrees $2Q$ and $Q$) and multiplies $H_n$ by
   $\varepsilon^n$.

Proof of 1. Write $M_n,N_n,x_n,\eta_n$ as in the proof of Theorem T ($\eta_n=n|H_n|$ at $n=kQ\ge2Q$, else $0$).

Step 1 (linear bounds). The frequencies are at most $Bn-1$ for $f_n$ and $Bn$ for $g_n$ ($q_k<kQB$). Now $|p_j|\le j$ and
$|P_i|\le(2-\frac2Q)i$, so $\|T_{i,j}(g,f)\|\le(3-\frac2Q)B\,ij\,\|g\|\|f\|$ under these frequency bounds, and
$m/\lambda_m=\frac{m(Q-2)}{2(m-1)}\le Q-2$ for $m\ge2$. So (K) holds with
$$\kappa=\kappa_Q:=(Q-2)\big(3-\tfrac2Q\big)B,$$
which is $\frac{7B}3$ at $Q=3$. Each $a_{n,m}$ enters at most two stream coefficients, with factors $1/(2|q\pm P_n|)\le\frac Q4$,
so $\|\Pi_nf\|,\|\Pi'_nf\|\le L_Q\|f\|$ with $L_Q:=\frac Q2$, and $N_n\le L_QM_n+|H_n|$ at resonant $n$.

Step 2 (inequalities). For $n=kQ$ and $1\le r\le Q-1$ put $u_{n,r}=(n+r)\|f^{(0)}_{n+r}\|$. Then, with $L=L_Q$,
$$x_n\le\kappa\sum_{i+j=n}(Lx_i+\eta_i)x_j\qquad(n\ge2),\tag{I1$_Q$}$$
$$u_{n,r}\le\kappa\Big[L\!\!\sum_{\substack{i+j=n+r\\ i,j\ge r}}\!\!x_ix_j+\!\!\sum_{\substack{i+j=n+r\\ j\ge Q+1}}\!\!\eta_ix_j
+Q\sum_{s=1}^{r-1}x_su_{n,r-s}\Big],\tag{I2$_Q$}$$
$$\eta_n\le\frac\kappa{\sigma_*}\Big[L\!\!\sum_{\substack{i+j=n+Q\\ i,j\ge Q}}\!\!x_ix_j+\!\!\sum_{\substack{i+j=n+Q\\ j\ge Q+1}}\!\!\eta_ix_j
+Q\sum_{s=1}^{Q-1}x_su_{n,Q-s}\Big].\tag{I3$_Q$}$$
Indeed, in $f^{(0)}_{n+r}$ the stream of order $n$ is $\Pi'_nf_n$, of norm at most $LM_n$; the nonzero $\eta_i$ have $i\le n-Q$,
so their partners have order at least $Q+r\ge Q+1$; a pair with one index in $\{n+1,\dots,n+r-1\}$ has its partner $s$ in
$\{1,\dots,r-1\}$ and uses $f^{(0)}_{n+r-s}$ or its Poisson image, in both orientations, which gives $\kappa(L+L)x_su_{n,r-s}$;
all other pairs have both indices in $[r,n]$. For (I3$_Q$), $\eta_n=n|R_k|/|\sigma_k|\le\sigma_*^{-1}(n+Q)\|f^{(0)}_{n+Q}\|$. At
$Q=3$ these are (I1) to (I3), with $u_n=u_{n,1}$ and $v_n=u_{n,2}$.

Step 3 (majorant sequences). Define $\bar x_1=x_1$, $\bar\eta_n=0$ for $n\le Q$, and $\bar x_n$ ($n\ge2$), $\bar u_{n,r}$ and
$\bar\eta_n$ (every $n\ge Q+1$) by equality in (I1$_Q$) to (I3$_Q$). The right sides have nonnegative coefficients and the
dependence is triangular ($\bar x_n$, then $\bar u_{n,1},\dots,\bar u_{n,Q-1}$, then $\bar\eta_n$; in the $\eta$ sums $j\ge Q+1$
forces $i\le n-1$). By induction $x_n\le\bar x_n$ and $\eta_n\le\bar\eta_n$.

Step 4 (generating functions). For $j\le Q$ the equalities give $\bar x_j=\mathrm{Cat}_{j-1}(\kappa L)^{j-1}\bar x_1^j$ (Catalan
numbers). Put $P=\sum_{j=1}^Q\bar x_jz^j$, $P_r=\sum_{j=r}^Q\bar x_jz^j$, $X=\sum_n\bar x_nz^n=P+z^{Q+1}W$,
$\sum_{n\ge Q+1}\bar\eta_nz^n=z^{Q+1}E$, $\sum_{n\ge Q+1}\bar u_{n,r}z^n=z^{Q+1}V_r$, and
$$A_r=z^{-(Q+r+1)}\big[P_r^2\big]_{\ge Q+r+1}+2z^{-r}P_rW+z^{Q+1-r}W^2\qquad(1\le r\le Q),$$
where $[\cdot]_{\ge d}$ deletes the terms of degree below $d$. The equalities are equivalent to
$$W=\kappa L\,z^{-(Q+1)}\big[P^2\big]_{\ge Q+1}+2\kappa LPW+\kappa Lz^{Q+1}W^2+\kappa E(P+z^{Q+1}W),$$
$$V_r=\kappa\Big[LA_r+z^{Q+1-r}EW+Q\sum_{s=1}^{r-1}\bar x_sV_{r-s}\Big]\quad(1\le r\le Q-1),\qquad
E=\frac\kappa{\sigma_*}\Big[LA_Q+zEW+Q\sum_{s=1}^{Q-1}\bar x_sV_{Q-s}\Big].$$
Every term that is nonlinear in $Y=(W,V_1,\dots,V_{Q-1},E)$ carries a factor $z$ ($P=O(z)$ and $Q+1-r\ge1$). At $z=0$ the
linear part is strictly lower triangular in this order: the $W$ row is zero, the $V_r$ row has $2\kappa L\bar x_r$ in the
$W$ column and $Q\kappa\bar x_s$ in the $V_{r-s}$ columns, and the $E$ row has $2\kappa L\bar x_Q/\sigma_*$ and
$Q\kappa\bar x_s/\sigma_*$. So $J^{Q+1}=0$, $\det(I-J)=1$, the formal solution is unique, and the holomorphic implicit function
theorem gives it a positive radius, exactly as in Theorem T. (At $Q=3$, $A_3=2\bar x_3W+zW^2$ and the system is that of
Section 12.4.) Hence $\bar x_n+\bar\eta_n\le CA^n$, and $N_n\le LM_n+|H_n|$. $\square$

Proof of 2 to 4. As for Theorem T, with $z=r^{-2/Q}$: $|r^{p_n}f_n(\theta)|\le r^{1-2/Q}C'(Ae^{B\tau}r^{-2/Q})^{n-1}$ for
$|\operatorname{Im}\theta|\le\tau$, and each Cartesian derivative costs a polynomial factor in $n$. $\square$

Corollary T_Q.3 (uniform response bound, openness, genericity). (a) For every complex $f$ with frequencies below $B$ and
every $k\ge2$, $|\sigma_k(f)|\le M_{B,Q}\|f\|_1^Q$ with $M_{B,Q}=\frac12\binom{2Q}Q\kappa_Q^QL_Q^{Q-1}$ (at $Q=3$ this is
$M_B=10\kappa^3(\frac32)^2$ of Theorem T.6). (b) For $k\ge k_0:=\frac{QB}2+1$, $\sigma_k=N(k,f)/D(k)$ with polynomials $N$
(homogeneous of degree $Q$ in $f$) and $D$ (without zeros at integers $k\ge k_0$); $\sigma_\infty=\lim_k\sigma_k$ exists, is a
form of degree $Q$, and the convergence is uniform on bounded sets. (c) The set of profiles satisfying (T_Q-b) is open
in the coefficient space, and on every connected real analytic submanifold of $\{O_{2Q}=0\}$ that contains one profile
satisfying (T_Q-b), such profiles form an open dense subset of full measure.

Proof. (a) For a unit multipole at $n=kQ$ put $y_r=(n+r)\|\varphi_r\|/n$. Step 1 gives
$y_r\le\kappa\big[x_r+2L\sum_{s=1}^{r-1}y_sx_{r-s}\big]$ with $x_r=r\|f_r\|$. Majorize $x_r$ by the coefficients of
$X=az+\kappa LX^2$, $a=\|f\|_1$; then $\sum_ry_rz^r$ is majorized by
$\kappa X/(1-2\kappa LX)=\big[(1-4\kappa Laz)^{-1/2}-1\big]/(2L)$, whose coefficient of $z^Q$ is
$\binom{2Q}Q(\kappa La)^Q/(2L)$; and $|\sigma_k|\le\|\varphi_Q\|\le y_Q$. (b) As Theorem T.8(a): for $k\ge k_0$, $q_k\ge QB$, the
frequencies in $\varphi_r$ and $\Pi_{n+r}\varphi_r$ are $q_k+j$ with $|j|\le Br-1$ and $|j|\le Br$, so they are at least $1$ and the
density inputs of $\Pi_{n+r}$ ($r\le Q-1$) are at least $B+1\ge3$; no folding, omitted zero mode or change of branch occurs.
The divisors are $\lambda_{n+r}$, $2(j-\frac{2r}Q)$ with $j$ even (nonzero, since $0<\frac{2r}Q<2$) and
$2(2q_k+j+\frac{2r}Q)>0$. The limit follows from (a) as in Theorem T.8(a). (c) Openness: as Theorem T.6(b) and T.8(b),
from (a) by Cauchy estimates and from (b); genericity: as Theorem T.8(b). $\square$

Corollary T_5 (explicit profiles at $\delta=2/5$, $c=5/3$; PROVED: two independent exact computations that agree
identically, the accompanying artifacts). (a) For
$f_1=\sin\theta+b\sin3\theta$ at $Q=5$ one finds $O_{10}=\mathcal P_{10}(b)/d_{10}$ with an explicit positive integer $d_{10}$ and
an integer polynomial $\mathcal P_{10}$ of degree 10 and content 1 (given in full in the artifacts). $\mathcal P_{10}$ is
irreducible over $\mathbb Q$ (exact factorization; an independent certificate: its reduction modulo 11 has a unit leading
coefficient and is irreducible over $\mathbb F_{11}$), and it has exactly six real roots,
$$b\approx-0.4897579913,\ 0.0489986662,\ 0.1253337788,\ 0.2120921309,\ 0.3152765950,\ 0.5599810535,$$
isolated in rational intervals of width $10^{-30}$. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a) and (T_Q-b), so Theorem T_Q gives a convergent pure power
series without logarithms at $c=5/3$, on $r>A^{5/2}$.
(b) In the order of the roots above and for $\varepsilon=1$, $|\sigma_k|\ge s_i$ for every $k\ge2$ with
$s_i=2^{-5},2^{-23},2^{-16},2^{-15},2^{-14},2^{-11}$, and the tuned density and stream series converge, with every
Cartesian derivative series and the radial weights of item 2, absolutely and uniformly on $r\ge R$ whenever
$R>2^{140},2^{175},2^{160},2^{160},2^{160},2^{155}$ times $|\varepsilon|^{5/2}$ respectively; $R>2^{185}|\varepsilon|^{5/2}$
works for all six.
(c) (Exact minima; PROVED: two independent exact certificates.) For each root, $\min_{k\ge2}|\sigma_k(b_i)|$ is attained at
exactly one index, $k_i=5,8,5,6,5,5$, with values $0.40131059711\ldots$, $2.17701970431\ldots\cdot10^{-6}$,
$1.58186094150\ldots\cdot10^{-4}$, $4.17828835876\ldots\cdot10^{-4}$, $1.15215729535\ldots\cdot10^{-3}$,
$6.84924868687\ldots\cdot10^{-3}$; so (b) holds with $s_i=\frac{401}{1000},\frac{217}{10^8},\frac{79}{500000},\frac{417}{10^6},
\frac{23}{20000},\frac{171}{25000}$. With these $s_i$ and $a_i=\frac{149}{100},\frac{21}{20},\frac{113}{100},\frac{61}{50},\frac{33}{25},
\frac{39}{25}$ the box test of (b) passes at $z_0=2^{-51},2^{-66},2^{-60},2^{-59},2^{-59},2^{-58}$ (exteriors
$R>2^{127.5},2^{165},2^{150},2^{147.5},2^{147.5},2^{145}$ times $|\varepsilon|^{5/2}$), and with $a=\frac{39}{25}$,
$\sigma_*=\frac{217}{10^8}$, $z_0=2^{-69}$, for all six. Sharper (PROVED: an independent certificate with non-dyadic
$z_0$ and explicit rational supersolutions $Y$ with $\Phi(z_0,Y)<Y$ componentwise, checked here exactly with the map
$\Phi$ built independently from Step 4, together with $R^2z_0^5>1$; the $a_i$ are $\frac{149}{100},\frac{1049}{1000},\frac{563}{500},
\frac{1213}{1000},\frac{329}{250},\frac{39}{25}$): the exteriors
$$R>7.01\cdot10^{37},\ 5.33\cdot10^{48},\ 3.41\cdot10^{44},\ 9.19\cdot10^{43},\ 2.48\cdot10^{43},\ 3.68\cdot10^{42}$$
times $|\varepsilon|^{5/2}$ (about $2^{125.8}$, $2^{161.9}$, $2^{147.9}$, $2^{146.1}$, $2^{144.2}$, $2^{141.4}$) are admissible, so
$R>5.33\cdot10^{48}|\varepsilon|^{5/2}$ works for all six. These imply the dyadic exteriors above.

Proof. Here $B=4$ and $k_0=11$. The response $\sigma_k$ was computed in $\mathbb Q(k)[b]$ with $k$ symbolic, valid for $k\ge11$
by Corollary T_Q.3(b), and directly for $2\le k\le16$; the two agree at $11\le k\le16$. For $k\ge11$,
$\sigma_k=N(k,b)/D(k)$ where $D$ is a product of linear factors with no zero at an integer $k\ge11$, and the six
coefficients of $N(k,\cdot)$ (a polynomial of degree 5 in $b$) have a common divisor in $\mathbb Q[k]$ whose only integer
root is $1$; so $N(k,\cdot)\not\equiv0$ for every integer $k\ge11$. For $2\le k\le10$, $\sigma_k$ is a nonzero polynomial
of degree 5 in $b$, and $\sigma_\infty$ is a nonzero polynomial of degree 5,
$\sigma_\infty=\frac{280671715860741}{44632806400000}b^5-\frac{985510990231659}{219803444224000}b^4+\cdots-\frac{3575370901}{2725632000000}$.
A root of the irreducible $\mathcal P_{10}$ is algebraic of degree 10, so no nonzero rational polynomial of degree at most 5
vanishes there. Hence $\sigma_k(b)\ne0$ for all $k\ge2$ and $\sigma_\infty(b)\ne0$, so $\sigma_*>0$. Homogeneity extends this
to $\varepsilon f_1$. This proves (a).

(b) The lower bounds are exact rational inequalities, as in Corollary T.3(c) and T.4: for $2\le k\le10$ by interval
evaluation of the quintics $\sigma_k$ on the isolating intervals; for $k\ge11$, after $k=11+t$, $D(11+t)$ has positive
coefficients (after a sign normalization) and every $t$-coefficient of $\epsilon_iN(11+t,b)-s_iD(11+t)$, with
$\epsilon_i=\operatorname{sign}\sigma_\infty(b_i)=-,+,-,-,+,+$, is a quintic in $b$ that is nonnegative on the isolating
interval, the constant one positive; so $\epsilon_i\sigma_k(b_i)\ge s_i$ for all real $k\ge11$. For the radius take
$\kappa=\kappa_5=\frac{156}5$, $L=\frac52$, $a_i=\frac{149}{100},\frac{1049}{1000},\frac{563}{500},\frac{1213}{1000},
\frac{329}{250},\frac{39}{25}$ ($\ge\|f_1\|_{\ell^1}=1+|b_i|$) and $\sigma_*=s_i$ in the system of Step 4, $Y=\Phi(z,Y)$ with
$Y=(W,V_1,\dots,V_4,E)$. With $c_0=\Phi(0,0)$, $J$ its strictly lower triangular linear part at $z=0$,
$T=I+J+\dots+J^5=(I-J)^{-1}$ and $Y_0=Tc_0$, the system is equivalent to $Y=G(z,Y):=Y_0+T[\Phi(z,Y)-c_0-JY]$, and $G-Y_0$
has nonnegative coefficients, each with a positive power of $z$. Exact rational arithmetic gives $G(z_0,2Y_0)\le2Y_0$
componentwise at $z_0=2^{-56},2^{-70},2^{-64},2^{-64},2^{-64},2^{-62}$ (largest component ratios $0.675$, $0.841$, $0.761$,
$0.704$, $0.666$, $0.731$), and at $z_0=2^{-74}$ for $a=\frac85$, $\sigma_*=2^{-23}$ (ratio $0.768$). The monotone iteration of
Corollary T.4 then bounds the majorant coefficients by $2Y_0z_0^{-n}$, and items 2 to 4 give $R>z_0^{-5/2}$. At $4z_0$ each
of these box tests fails; this says nothing about divergence. Both parts were computed twice, by independent programs,
with the same bounds and the same component ratios.

(c) Let $e_i$ be the sign of $\sigma_{k_i}(b_i)$ (its interval excludes $0$). For $2\le k\le10$, $k\ne k_i$, the interval
lower bound of $|\sigma_k|$ on the isolating interval exceeds the interval upper bound of $e_i\sigma_{k_i}$ (smallest gap
$4.4\cdot10^{-6}$, at the second root). For $k=11+t$, every $t$-coefficient of
$\epsilon_iN(11+t,b)-e_i\sigma_{k_i}(b)D(11+t)$, a polynomial in $b$, has a strictly positive interval lower bound on the
isolating interval; with $D(11+t)>0$ this gives $\epsilon_i\sigma_k(b_i)>|\sigma_{k_i}(b_i)|$ for every real $k\ge11$. The
dyadic radii follow as in (b). For the sharper radii, a supersolution $\Phi(z_0,Y)\le Y$ with $Y>0$ gives
$G(z_0,Y)=Tc_0+T(\Phi(z_0,Y)-c_0-JY)\le T(Y-JY)=Y$ because $T=(I-J)^{-1}$ is nonnegative, so Step 4 applies with the box
$Y$ in place of $2Y_0$; the six rational pairs $(z_0,Y)$ satisfy $\Phi(z_0,Y)<Y$ exactly, and $R^2z_0^5>1$. The minima and their uniqueness were certified twice, by independent programs. $\square$

Values ($\varepsilon=1$; floating point evaluation of the exact formulas). In the order
of the roots above, $\sigma_\infty=-0.8482$, $8.381\cdot10^{-5}$, $-3.291\cdot10^{-4}$, $-1.355\cdot10^{-3}$, $2.223\cdot10^{-3}$,
$0.1363$, and $\min_{2\le k\le2000}|\sigma_k|=0.4013$ ($k=5$), $2.177\cdot10^{-6}$ ($k=8$), $1.582\cdot10^{-4}$ ($k=5$),
$4.178\cdot10^{-4}$ ($k=6$), $1.152\cdot10^{-3}$ ($k=5$), $6.849\cdot10^{-3}$ ($k=5$). For the second root $\sigma_k$
changes sign between $k=8$ and $k=9$. These minima are the exact minima of (c).

Corollary T_4 (explicit profiles at $\delta=1/2$, $c=2$; PROVED: (a), (b) and (c), including its radii, were computed twice by
independent programs, with identical results, and the independent review confirmed the proof). Let $Q=4$ and $f_1=\sin\theta+b\sin3\theta$, so $B=4$ and $k_0=9$.
(a) $O_8=-\mathcal P_8(b)/136031716379156417555623759872000$ with an integer polynomial $\mathcal P_8$ of degree 8 and content
1 (leading coefficient $82668272572218361620942808786146$, constant term $-17775107835680457282107307$; given in full in
the artifacts). $\mathcal P_8$ is irreducible over $\mathbb Q$, and it has exactly six real roots,
$$b\approx-0.2796388302,\ 0.0399356952,\ 0.0771467388,\ 0.1877630741,\ 0.3515044178,\ 0.6267874991.$$
For every such root and every real $\varepsilon\ne0$, $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a) and (T_Q-b),
so Theorem T_Q gives a uniquely tuned convergent pure power series without logarithms at $c=2$, with
$\rho=r^{1/2}f_1+O(1)$.
(b) In the order of the roots above and for $\varepsilon=1$, $|\sigma_k|\ge s_i$ for every $k\ge2$ with
$s_i=2^{-5},2^{-14},2^{-15},2^{-14},2^{-10},2^{-9}$, and the tuned series converge as in Corollary T_5(b) on $r\ge R$ whenever
$R>2^{82},2^{96},2^{98},2^{98},2^{92},2^{92}$ times $\varepsilon^2$; $R>2^{104}\varepsilon^2$ works for all six.
(c) (Exact infima.) $\min_{k\ge2}|\sigma_k(b_i)|$ is attained at exactly one index, $k_i=5,3,5,5,5$, for the roots
$i=1,2,4,5,6$, with values $3.6425300\ldots\cdot10^{-2}$, $1.2072651\ldots\cdot10^{-4}$, $1.1416804\ldots\cdot10^{-4}$,
$1.2089201\ldots\cdot10^{-3}$, $3.2000608\ldots\cdot10^{-3}$. For $i=3$, $|\sigma_k(b_3)|>|\sigma_\infty(b_3)|=4.3023439\ldots\cdot10^{-5}$
for every $k\ge2$, so the infimum $|\sigma_\infty(b_3)|$ is not attained. Hence (b) holds with
$s_i=\frac{91}{2500},\frac{3}{25000},\frac{43}{10^6},\frac{57}{500000},\frac{3}{2500},\frac{2}{625}$, and with these $s_i$ and the same
$a_i$ the box test passes at $z_0=2^{-40},2^{-47},2^{-49},2^{-48},2^{-46},2^{-46}$, so the exteriors
$R>2^{80},2^{94},2^{98},2^{96},2^{92},2^{92}$ times $\varepsilon^2$ are admissible (the radii from these $s_i$: PROVED, two
exact certificates by independent programs; $2^{104}\varepsilon^2$ remains the common exterior).
Since $\mathcal P_8(0)\ne0$, $f_1=\sin\theta$ is obstructed at order 8 at $c=2$ for every choice of constants.

Proof. As for Corollary T_5. (a) The exact factorization of $\mathcal P_8$ over $\mathbb Q$ has one factor. Independently,
modulo 5 and modulo 29 (unit leading coefficient, squarefree reduction) $\mathcal P_8$ factors into irreducible factors of
degrees $2,6$ and $1,7$; the degree of a rational factor would be a sum of a subset of each list, and the only common
sums are $0$ and $8$. The six real roots are isolated in rational intervals of width at most $10^{-30}$. The response
$\sigma_k$ has degree 4 in $b$; for $k\ge9$, $\sigma_k=N(k,b)/D(k)$, computed with symbolic $k$ (Corollary T_Q.3(b)) and
equal to the direct computation at $9\le k\le14$, where $D$ is a product of linear factors with no integer zero $\ge9$
and the common divisor in $\mathbb Q[k]$ of the five $b$-coefficients of $N$ has no integer root $\ge9$ (its rational roots
are at most $\frac94$). For $2\le k\le8$, $\sigma_k$ is a nonzero quartic, and
$\sigma_\infty=\frac{41504277}{95406080}b^4-\frac{55490341}{91069440}b^3+\frac{54365903}{182138880}b^2-\frac{2732099}{57953280}b+\frac{9137}{4214784}$.
A root of $\mathcal P_8$ has degree 8 over $\mathbb Q$, so no nonzero rational polynomial of degree at most 4 vanishes there.
(b) For $2\le k\le8$ by interval evaluation; for $k=9+t$, $D(9+t)$ has positive coefficients and every $t$-coefficient of
$\epsilon_iN(9+t,b)-s_iD(9+t)$, $\epsilon_i=\operatorname{sign}\sigma_\infty(b_i)=+$ for all six roots, is positive on the
isolating interval at $t^0$ and nonnegative otherwise. In the system of Step 4 with $\kappa_4=20$, $L_4=2$ and
$a_i=\frac{32}{25},\frac{26}{25},\frac{27}{25},\frac{119}{100},\frac{34}{25},\frac{163}{100}$ ($\ge1+|b_i|$), exact arithmetic gives
$G(z_0,2Y_0)\le2Y_0$ at $z_0=2^{-41},2^{-48},2^{-49},2^{-49},2^{-46},2^{-46}$ (largest component ratios $0.761$, $0.870$,
$0.947$, $0.863$, $0.854$, $0.938$; each fails at $2z_0$), and at $z_0=2^{-52}$ for $a=\frac{163}{100}$, $\sigma_*=2^{-15}$;
then $R>z_0^{-2}$. (c) As Corollary T_5(c), with $k_0=9$. For $i=3$ the target is $\sigma_\infty(b)D(9+t)$: its top
$t$-coefficient cancels the top coefficient of $N(9+t,b)$ identically in $b$, and every other $t$-coefficient of
$N(9+t,b)-\sigma_\infty(b)D(9+t)$ has a strictly positive lower bound on the isolating interval, so $\sigma_k(b_3)>\sigma_\infty(b_3)>0$
for every real $k\ge9$; for $2\le k\le8$, $|\sigma_k(b_3)|$ exceeds $\sigma_\infty(b_3)$ by at least $6.9\cdot10^{-5}$. $\square$

Values ($\varepsilon=1$; floating point). For the third root $\sigma_k$ decreases to $\sigma_\infty=4.302\cdot10^{-5}$; at
$k=2000$ it is $4.334\cdot10^{-5}$.

Corollary T_6 (explicit profiles at $\delta=1/3$, $c=3/2$; PROVED: proof here and an independent proof with independent
exact computations of $O_{12}$, the responses, the infima and the boxes). Let $Q=6$ and $f_1=\sin\theta+b\sin3\theta$, so $B=4$, $\kappa_6=\frac{128}3$, $L_6=3$ and $k_0=13$.
(a) $O_{12}=-\mathcal P_{12}(b)/d_{12}$ with $d_{12}=52232904824122197575544253519343269951693358688275781831123219997047128064\cdot10^9$
and an integer polynomial $\mathcal P_{12}$ of degree 12 and content 1 (given in full in the artifacts). $\mathcal P_{12}$ is
irreducible over $\mathbb Q$: modulo 13 and modulo 19 (unit leading coefficient, squarefree reduction) it factors into
irreducible factors of degrees $3,9$ and $1,11$, and the only common subset sums are $0$ and $12$. It has exactly six real
roots,
$$b\approx-0.6087269138,\ 0.0885568921,\ 0.1407241791,\ 0.1965153635,\ 0.2784978894,\ 0.5121564736,$$
isolated in rational intervals of width at most $10^{-30}$. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a) and (T_Q-b), so Theorem T_Q gives a uniquely tuned convergent
pure power series at $c=3/2$, with $\rho=r^{2/3}f_1+O(r^{1/3})$.
(b) (Exact infima.) $\min_{k\ge2}|\sigma_k(b_i)|$ is attained at exactly one index, $k_i=6,5,6$, for the roots $i=1,2,3$
and $k_6=6$ for $i=6$, with values $17.3619766\ldots$, $1.74760999\ldots\cdot10^{-4}$, $3.09283616\ldots\cdot10^{-4}$,
$0.483508941\ldots$. For $i=4,5$, $|\sigma_k(b_i)|>|\sigma_\infty(b_i)|$ for every $k\ge2$, with $|\sigma_\infty(b_4)|=1.45328950\ldots\cdot10^{-3}$
and $|\sigma_\infty(b_5)|=1.89856986\ldots\cdot10^{-2}$, so these two infima are not attained. Hence $|\sigma_k|\ge s_i$ for
every $k\ge2$ with $s_i=\frac{434}{25},\frac{87}{500000},\frac{309}{10^6},\frac{29}{20000},\frac{189}{10000},\frac{483}{1000}$. With these
$s_i$ and $a_i=\frac{161}{100},\frac{109}{100},\frac{23}{20},\frac65,\frac{32}{25},\frac{38}{25}$ ($\ge1+|b_i|$) the box test passes at
$z_0=2^{-60},2^{-73},2^{-73},2^{-71},2^{-68},2^{-65}$ (largest component ratios $0.914$, $0.829$, $0.770$, $0.809$, $0.798$,
$0.811$; each fails at $2z_0$), so the exteriors $R>2^{180},2^{219},2^{219},2^{213},2^{204},2^{195}$ times $|\varepsilon|^3$ are
admissible, and $R>2^{231}|\varepsilon|^3$ ($a=\frac{161}{100}$, $\sigma_*=\frac{87}{500000}$, $z_0=2^{-77}$) works for all six.
Since $\mathcal P_{12}(0)\ne0$, $f_1=\sin\theta$ is obstructed at order 12 at $c=3/2$ for every choice of constants.

Proof. As for Corollaries T_5 and T_4. (a) For $k\ge13$, $\sigma_k=N(k,b)/D(k)$, computed with symbolic $k$ (Corollary
T_Q.3(b)) and equal to the direct computation at $13\le k\le18$; $N$ has degree 6 in $b$ and degree 197 in $k$, $D$ is a
product of linear factors with no integer zero $\ge13$, and the common divisor in $\mathbb Q[k]$ of the seven $b$-coefficients
of $N$ has no integer root $\ge13$ (its rational roots have modulus at most $\frac{13}4$). For $2\le k\le12$, $\sigma_k$ is a nonzero polynomial of
degree 6, and $\sigma_\infty=-\frac{15620361982640929}{109303999516800}b^6+\dots+\frac{873110393}{2049271488000}$ is nonzero of
degree 6. A root of $\mathcal P_{12}$ is algebraic of degree 12, so no nonzero rational polynomial of degree at most 6
vanishes there. (b) As Corollary T_5(c) and T_4(c), with $k_0=13$: for $2\le k\le12$, $k\ne k_i$, interval evaluation on the
isolating interval separates $|\sigma_k|$ from the target (smallest gap $9.6\cdot10^{-6}$, at the second root); for $k=13+t$,
$D(13+t)$ has positive coefficients after a sign normalization, and every $t$-coefficient of
$\epsilon_iN(13+t,b)-e_i\sigma_{k_i}(b)D(13+t)$ has a strictly positive lower bound on the isolating interval. For $i=4,5$
the target is $\sigma_\infty(b)D(13+t)$: its top $t$-coefficient cancels that of $N(13+t,b)$ identically in $b$, and every
other $t$-coefficient of $\epsilon_i[N(13+t,b)-\sigma_\infty(b)D(13+t)]$ has a strictly positive lower bound there. $\square$

Corollary T_7 (explicit profiles at $\delta=2/7$, $c=7/5$; PROVED: independent exact reconstruction of the compatibility
polynomial and its roots, independent all-index response covers and exact boxes, and the exact nonvanishing certificate
below computed here; (c) and (d) independently confirmed). Let $Q=7$ and $f_1=\sin\theta+b\sin3\theta$, so $B=4$,
$L_7=\frac{147}{80}$ (Section 12.6, Remark 4(iii)), $\kappa_*=\frac{1275}{49}$ (Remark 4(ii) with a certified prefix through
order 14, factor $\frac{15}{14}$) and $k_0=15$.
(a) $O_{14}=\mathcal P_{14}(b)/d_{14}$ with an explicit positive integer $d_{14}$ and an integer polynomial $\mathcal P_{14}$ of degree 14
(given in full in the artifacts). $\mathcal P_{14}$ is irreducible over $\mathbb Q$: an exact factorization gives one factor, and
independently its reductions (unit leading coefficient, squarefree) factor into irreducible factors of degrees
$2,2,2,8$ modulo 29, $1,6,7$ modulo 43 and $1,2,11$ modulo 67, whose subset sums have only $0$ and $14$ in common. It has
exactly ten real roots, all simple,
$$b\approx-0.6736263358,\ -0.0567076198,\ 0.0150535150,\ 0.0305536042,\ 0.0659329807,$$
$$0.1007255318,\ 0.1356654311,\ 0.1797781928,\ 0.2517896667,\ 0.4751674513,$$
isolated in rational intervals of width at most $10^{-30}$. Being irreducible of degree 14, $\mathcal P_{14}$ has $\mathcal P_{14}(0)\ne0$, so $\sin\theta$
itself is obstructed at order 14 for every choice of constants. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a) and (T_Q-b), so Theorem T_Q gives a uniquely tuned pure density
and stream series at $c=7/5$ converging with all derivatives on an exterior $r>A^{7/2}$, with $\rho=r^{5/7}f_1+O(r^{3/7})$, and
Proposition T_Q.4 gives a convergent potential whose only possible logarithms sit at the orders 7 and 14.
(b) Explicit exteriors. In the order of the roots and for $\varepsilon=1$, $|\sigma_k|$ is bounded below for every $k\ge2$ by
$256,\ 2^{-9},\ 2^{-22},\ 2^{-17},\ 2^{-15},\ 2^{-14},\ 2^{-12},\ 2^{-10},\ 2^{-13},\ 1$ (independent certificates: direct finite responses,
a complete interval cover of the integer tail with one or two Taylor leaves, six singleton and two Taylor leaves at the
third root, every root replayed at 1024 bits against 1202 exact polynomial coefficients; the replay calls the same audited
Taylor-jet enclosure routine as the constructor and reconstructs the roots, the coverage and the prefix checks separately). The certified-prefix
resonance-block majorant of Remark 5(b), with $M=2$ (an exact prefix through order $N=14$; no free constant enters at order
7) and these constants, passes at $w=z^7=r^{-2}=2^{-q}$ with $q=95,101,113,109,107,107,106,104,109,99$. Certified prefixes
through $N=8Q=56$ improve this to $q=94,100,112,108,106,106,105,103,108,98$ (PROVED: a 1536-bit Cartesian computation and a
separately written 2048-bit polar computation that fixes each resonant harmonic by two provisional continuations, with
all norms, harmonics and responses compared; boxes at $N=14,28,42,56$ replayed in exact rational arithmetic against a
separately indexed scalar recurrence), so the series of (a) converge on $r>2^{q/2}|\varepsilon|^{7/2}$, that is on
$$r>2^{47},\ 2^{50},\ 2^{56},\ 2^{54},\ 2^{53},\ 2^{53},\ 2^{105/2},\ 2^{103/2},\ 2^{54},\ 2^{49}$$
times $|\varepsilon|^{7/2}$. The longer prefixes lower each radius by the factor $2^{1/2}$ only. At the third root, whose
response is small at $k=18$ (Values below), a prefix through order 140 (independent 2048-bit Cartesian and 3072-bit
polar computations, all norms and the 19 tuning responses compared) and the tail-only bound $|\sigma_k|\ge2^{-19}$ for
$k\ge20$ of Remark 5(b') (eight direct responses and two closed Taylor leaves; the higher-precision replay sums the
Taylor terms separately but shares the jet algebra, and the scalar map is checked exactly) give
$q=109$ (PROVED), so this series converges on $r>2^{109/2}|\varepsilon|^{7/2}$, and $r>2^{109/2}|\varepsilon|^{7/2}$ is a common
sufficient exterior for the ten roots.
(c) In the expansion of Proposition T_Q.4 the potential necessarily contains a nonzero term $\varepsilon^7r^2\log r\,(\alpha_7+\beta_7\cos2\theta)$ at order 7 at every
root (PROVED: independent polar and Cartesian arithmetic with a full density and stream reconstruction; both leading
coefficients below agree exactly). At $n=Q$ the density exponent is $-1$ and the potential exponent 2; a pure
potential term $r^2\cos2m\theta$ has density $4m(1-m^2)r^{-1}[\sin(2m+1)\theta+\sin(2m-1)\theta]$, which has no $\sin\theta$
component, while $-\partial_y\Delta(r^2\log r)=-4r^{-1}\sin\theta$ and $-\partial_y\Delta(r^2\log r\cos2\theta)=4r^{-1}(\sin\theta+\sin3\theta)$.
Eliminating the frequencies $\ge5$ through the pure columns leaves $a_7\sin\theta+d_7\sin3\theta$ with $a_7=[\sin\theta]f_7$, so
$\beta_7=d_7/4$, $\alpha_7=(d_7-a_7)/4$ and $\beta_7-\alpha_7=a_7/4$. Here $a_7$ is a rational polynomial in $b$ of exact degree 7
(leading coefficient $-\frac{164636345977547089678145625463}{6907160871651870058217472}$), so it does not vanish at a root of the
irreducible $\mathcal P_{14}$. The stream needs no logarithm, since $P_7=0$ and the Poisson operator $l^2$ is invertible on
$\sin l\theta$, $l\ge1$.
(d) Necessary radii (PROVED: the exact top coefficients and all twenty bounds of (d) and Corollary T_8(d) are
independently confirmed in directed 512- and 1024-bit arithmetic). By Remark 3 of Section 12.6 with $B=4$, uniform termwise $C^2$
convergence of a tuned series of (a) on $\{r\ge R\}$ requires $R>(|\varepsilon b|/R_H)^{7/2}$, with $R_H=0.9136802595\ldots$ at $\delta=\frac27$
(checked against the scalar top recursion to order 1500: $h_nR_H^nn^{1+1/b}=0.48044,\ 0.47656,\ 0.47566,\ 0.47514$ at
$n=100,400,800,1500$). In the order of the roots the lower bounds are $0.3441017$, $5.956143\cdot10^{-5}$, $5.740541\cdot10^{-7}$,
$6.838151\cdot10^{-6}$, $1.009437\cdot10^{-4}$, $4.448449\cdot10^{-4}$, $1.261427\cdot10^{-3}$, $3.379089\cdot10^{-3}$, $1.098633\cdot10^{-2}$,
$0.1014339$ times $|\varepsilon|^{7/2}$ (rounded down). They bound the true radius from below only.

Proof. As for Corollaries T_5 and T_6, with $k_0=\frac{QB}2+1=15$. For $k\ge15$, $\sigma_k=N(k,b)/D(k)$, computed with symbolic $k$
(Corollary T_Q.3(b)) and equal to the direct computation at $15\le k\le20$; $N$ has degree 7 in $b$ and degree 269 in $k$. $D$ is $k$
times a product of linear factors whose roots are rationals of modulus at most $\frac{53}{14}$, so it has no integer zero
$\ge15$; the common divisor in $\mathbb Q[k]$ of the eight $b$-coefficients of $N$ has degree 217 and splits into linear factors
whose roots are rationals of modulus at most $\frac{53}{14}$, so $N(k,\cdot)\not\equiv0$ for every integer $k\ge15$. For
$2\le k\le14$, $\sigma_k$ is a nonzero polynomial of degree 7 in $b$, and $\sigma_\infty$ is a nonzero polynomial of degree 7,
$\sigma_\infty=-\frac{1327810876333465003630261161909575}{160061627303888199791362965504}b^7+\cdots$. A root of the irreducible
$\mathcal P_{14}$ is algebraic of degree 14, so no nonzero rational polynomial of degree at most 7 vanishes there. Hence
$\sigma_k(b_i)\ne0$ for every $k\ge2$ and $\sigma_\infty(b_i)\ne0$; since $\sigma_k\to\sigma_\infty$, $\inf_{k\ge2}|\sigma_k(b_i)|>0$.
Homogeneity extends this to $\varepsilon f_1$. $\square$

Values ($\varepsilon=1$; floating point evaluation of the exact formulas on the isolating intervals; NUMERICAL EVIDENCE for
the minima, not used in the proof). In the order of the roots above, $\sigma_\infty=1.605\cdot10^3$, $2.833\cdot10^{-2}$,
$8.027\cdot10^{-5}$, $1.210\cdot10^{-4}$, $-3.636\cdot10^{-4}$, $-8.007\cdot10^{-4}$, $1.158\cdot10^{-3}$, $7.161\cdot10^{-3}$,
$-2.231\cdot10^{-2}$, $-11.21$, and $\min_{2\le k\le2000}|\sigma_k|=1.054\cdot10^3$ ($k=7$), $1.442\cdot10^{-2}$ ($k=6$),
$1.114\cdot10^{-6}$ ($k=18$), $5.668\cdot10^{-5}$ ($k=6$), $2.041\cdot10^{-4}$ ($k=5$), $3.209\cdot10^{-4}$ ($k=7$), $1.163\cdot10^{-3}$
($k=2000$), $7.177\cdot10^{-3}$ ($k=2000$), $8.154\cdot10^{-4}$ ($k=9$), $7.273$ ($k=7$); at the seventh and eighth roots $|\sigma_k|$
decreases toward $|\sigma_\infty|$ from $k=7$ on, so the infimum is presumably the limit. At the third root $\sigma_k$ changes
sign between $k=2$ and $3$, between $4$ and $5$, and again between $16$ and $20$, which is why its smallest response is about 70 times smaller
than $|\sigma_\infty|$. Double-precision tuned runs to order 301, with linear fits to the per-period maxima of
$\log_{10}\|f_n\|_{\ell^1}$ (NUMERICAL EVIDENCE, finite orders only), give apparent radii $A^{7/2}$ of about $5.2\cdot10^3$, $7.5$, $0.41$,
$0.163$, $0.109$, $0.53$, $2.1$, $8.9$, $92$ and $9.3\cdot10^2$ in the order of the roots: far inside the sufficient radii of (b); the
third root, which has the largest sufficient radius, has one of the smaller apparent radii.

Corollary T_8 (explicit profiles at $\delta=1/4$, $c=4/3$; PROVED: independent exact reconstruction of $\mathcal P_{16}$, its roots and
its irreducibility, independent all-index response covers and exact boxes, and the exact nonvanishing certificate below
computed here). Let $Q=8$ and
$f_1=\sin\theta+b\sin3\theta$, so $B=4$, $L_8=\frac{48}{23}$, $\kappa_*=\frac{255}8$ (Remark 4(ii) with a certified prefix through
order 16) and $k_0=17$.
(a) $O_{16}=-\mathcal P_{16}(b)/d_{16}$ with an explicit positive integer $d_{16}$ and an integer polynomial $\mathcal P_{16}$ of degree 16
(given in full in the artifacts). $\mathcal P_{16}$ is irreducible over $\mathbb Q$: an exact factorization gives one factor, and
independently its reductions (unit leading coefficient, squarefree) factor into irreducible factors of degrees $2,2,5,7$
modulo 7 and $3,13$ modulo 101, whose subset sums have only $0$ and $16$ in common (the patterns $1,3,3,9$ modulo 41 and
$1,2,4,9$ modulo 47 are consistent with this). It has exactly ten real roots, all simple,
$$b\approx-0.7085996283,\ -0.0789381642,\ 0.0207043700,\ 0.0511771649,\ 0.0761107981,$$
$$0.1002774721,\ 0.1283945760,\ 0.1661386773,\ 0.2316191269,\ 0.4455854511,$$
isolated in rational intervals of width at most $10^{-30}$. As at $Q=7$, $\mathcal P_{16}(0)\ne0$, so $\sin\theta$ itself is obstructed at
order 16. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a) and (T_Q-b), so Theorem T_Q gives a uniquely tuned pure density
and stream series at $c=4/3$ converging with all derivatives on an exterior $r>A^4$, with $\rho=r^{3/4}f_1+O(r^{1/2})$, and
Proposition T_Q.4 gives a convergent potential whose only possible logarithms sit at the orders 8 and 16. Theorem T_Q
does not use the parity of $Q$.
(b) Explicit exteriors. In the order of the roots and for $\varepsilon=1$, $|\sigma_k|$ is bounded below for every $k\ge2$ by
$2^{12},\ 2^{-6},\ 2^{-29},\ 2^{-14},\ 2^{-14},\ 2^{-12},\ 2^{-11},\ 2^{-10},\ 2^{-4},\ 16$ (independent certificates: 23 direct finite
responses, a complete interval cover of the integer tail $t\in[0,\frac1{32}]$, every root replayed at 1024 bits against 1566
exact prefix coefficients, with the same replay scope as in Corollary T_7(b)). The certified-prefix majorant of Remark 5(b) with $M=2$ (prefix through order 16) passes at
$w=r^{-2}=2^{-q}$ with $q=114,120,141,127,127,126,125,125,121,116$. Certified prefixes through $N=8Q=64$, computed and
replayed as in Corollary T_7(b) (boxes at $N=16,32,48,64$), improve this to $q=113,119,140,126,126,125,124,124,120,115$
(PROVED). At the third root, whose response nearly vanishes at $k=10$ (Values below), a prefix through order 96
(independent 2048-bit Cartesian and 3072-bit polar computations, all norms and the eleven tuning responses compared)
and the tail-only bound $|\sigma_k|\ge2^{-19}$ for $k\ge12$ of Remark 5(b') (13 direct responses and a complete two-leaf
Taylor cover of the remaining integer tail, re-evaluated at 3072 bits with separate term summation and the same jet
algebra) give $q=130$ (PROVED). So the series of (a) converge on
$$r>2^{113/2},\ 2^{119/2},\ 2^{65},\ 2^{63},\ 2^{63},\ 2^{125/2},\ 2^{62},\ 2^{62},\ 2^{60},\ 2^{115/2}$$
times $|\varepsilon|^4$, and $r>2^{65}|\varepsilon|^4$ is a common sufficient exterior. The third root still has the largest
sufficient radius.
(c) As in Corollary T_7(c), the potential necessarily contains a nonzero term $\varepsilon^8r^2\log r\,(\alpha_8+\beta_8\cos2\theta)$
at order 8 at every root (PROVED, confirmed with Corollary T_7(c)): $a_8=[\sin\theta]f_8$ has exact degree 8 in $b$ (leading
coefficient $\frac{27211082630015197276722412191819100898525982717}{6712392727239885213732046293727256780800}$) and $\mathcal P_{16}$ is
irreducible of degree 16.
(d) Necessary radii (PROVED, confirmed with Corollary T_7(d)), as in Corollary T_7(d): $R_H=0.7688906250\ldots$ at $\delta=\frac14$
($h_nR_H^nn^{1+1/b}=0.39793,\ 0.39460,\ 0.39383,\ 0.39339$ at $n=100,400,800,1500$), and the lower bounds
$(|\varepsilon b_i|/R_H)^4$ are $0.7213489$, $1.110938\cdot10^{-4}$, $5.257627\cdot10^{-7}$, $1.962667\cdot10^{-5}$, $9.601229\cdot10^{-5}$,
$2.893045\cdot10^{-4}$, $7.775502\cdot10^{-4}$, $2.179840\cdot10^{-3}$, $8.234541\cdot10^{-3}$, $0.1127887$ times $|\varepsilon|^4$ (rounded down).

Proof. As for Corollary T_7, with $k_0=17$. For $k\ge17$, $\sigma_k=N(k,b)/D(k)$ with $N$ of degree 8 in $b$ and degree 411 in $k$,
equal to the direct computation at $17\le k\le22$. $D$ is $k$ times a product of powers of 64 distinct linear
factors (total degree 410) whose roots are rationals in $[-\frac{11}4,\frac{17}4]$; the common divisor in $\mathbb Q[k]$ of the nine $b$-coefficients
of $N$ has degree 343 and splits into linear factors with roots in the same interval. So $D(k)\ne0$ and $N(k,\cdot)\not\equiv0$
for every integer $k\ge17$. For $2\le k\le16$, $\sigma_k$ is a nonzero polynomial of degree 8 in $b$, and $\sigma_\infty$ is a
nonzero polynomial of degree 8. A root of the irreducible $\mathcal P_{16}$ is algebraic of degree 16, so no nonzero rational
polynomial of degree at most 8 vanishes there, and $\inf_{k\ge2}|\sigma_k(b_i)|>0$ as before. $\square$

Values ($\varepsilon=1$; floating point evaluation of the exact formulas; NUMERICAL EVIDENCE, not used in the proof). In the
order of the roots, $\sigma_\infty=3.474\cdot10^4$, $-0.2169$, $-3.517\cdot10^{-5}$, $4.414\cdot10^{-4}$, $8.256\cdot10^{-4}$,
$-1.216\cdot10^{-3}$, $-4.652\cdot10^{-3}$, $1.932\cdot10^{-2}$, $0.5727$, $143.4$, and $\min_{2\le k\le2000}|\sigma_k|=3.101\cdot10^4$ ($k=8$),
$0.1169$ ($k=7$), $1.370\cdot10^{-8}$ ($k=10$), $2.644\cdot10^{-4}$ ($k=5$), $3.557\cdot10^{-4}$ ($k=7$), $1.220\cdot10^{-3}$ ($k=2000$,
the last sampled index, just above $|\sigma_\infty|$), $3.425\cdot10^{-3}$ ($k=7$), $4.600\cdot10^{-3}$ ($k=8$), $0.3747$ ($k=8$), $97.36$ ($k=8$). At the third root
$\sigma_9\approx4.90\cdot10^{-6}$, $\sigma_{10}\approx1.37\cdot10^{-8}$ and $\sigma_{11}\approx-3.84\cdot10^{-6}$: the response changes sign
between $k=10$ and $11$ and passes very close to zero at $k=10$, about 2600 times below $|\sigma_\infty|$; this is a near
small divisor of the tuning, not a zero. Double-precision tuned runs to order 304 (fits as for Corollary T_7; NUMERICAL
EVIDENCE) give apparent radii $A^4$ of about $8\cdot10^4$, $57$, $0.48$, $0.118$, $0.50$, $2.0$, $8.3$, $51$, $2.3\cdot10^2$ and $6.2\cdot10^3$
in the order of the roots; the near small divisor at the third root does not raise its finite-order growth rate.

Remark (first-period potential logarithms at $3\le Q\le8$; PROVED: independent proofs, reviewed here, with an
independent exact computation of $a_Q$ at $Q=4,\dots,8$ here). Let $3\le Q\le8$, $\delta=2/Q$, $c=Q/(Q-2)$, and let $b$ be any
real root of the first compatibility polynomial $O_{2Q}$ of Theorem T ($Q=3$) or of Corollaries T_4 to T_8 (two roots at
$Q=3$, six at each of $Q=4,5,6$, ten at each of $Q=7,8$). For $f_1=\varepsilon(\sin\theta+b\sin3\theta)$, $\varepsilon\ne0$ real,
the common potential of the tuned convergent series (Proposition T_Q.4) contains a nonzero term
$\varepsilon^Qr^2\log r\,(\alpha_Q+\beta_Q\cos2\theta)$ at order $Q$. The density and stream series stay pure, the radii are
unchanged, and no claim is made about the coefficient $\lambda$ of $\log r$ at order $2Q$.

Proof. As in Corollary T_7(c): $f_Q$ is fixed before the first free constant (at $2Q$), and its $\sin\theta$ coefficient
$\varepsilon^Qa_Q(b)$ is a rational polynomial of degree at most $Q$; the pure columns $r^2\cos2m\theta$ produce no $\sin\theta$
density, so the potential is pure at order $Q$ only if $a_Q(b)=0$, and otherwise $\beta_Q=d_Q/4$, $\alpha_Q=(d_Q-a_Q)/4$ with
$\beta_Q-\alpha_Q=a_Q/4\ne0$. At $Q=3$, $a_3=-\frac3{64}b^3+\frac{1161}{17920}b^2-\frac{573}{44800}b+\frac1{6400}$ and $O_6$ is irreducible
of degree 6. At $Q=4$,
$a_4=\frac{97583}{34848}b^4-\frac{3092293}{1829520}b^3+\frac{8185447}{25613280}b^2-\frac{75727}{2716560}b+\frac{27}{21952}$; at $Q=4,5,6$ the
rational Euclidean remainder chain of $O_{2Q}$ and $a_Q$ has degrees $8,4,3,2,1,0$, $10,5,4,3,2,1,0$ and $12,6,5,4,3,2,1,0$ and
ends in a nonzero constant, so $\gcd(O_{2Q},a_Q)=1$. At $Q=7,8$ see Corollaries T_7(c), T_8(c), at $Q=9$ Corollary T_9(c) and at $Q=10$ Corollary T_10(c) below. In every case $a_Q(b)\ne0$ at each
real root. $\square$

Corollary T_9 (explicit profiles at $\delta=2/9$, $c=9/7$; PROVED: two independent exact computations of $\mathcal P_{18}$ (a
polar one here and a Cartesian one in the verification), identical in all 19 coefficients and in the scale; independent all-index
response covers and exact boxes; the exact nonvanishing certificate below computed here and independently reconstructed; the protocol, constants and scope reviewed here; (d) independently confirmed, including all eighteen top coefficients and $R_H$). Let $Q=9$ and
$f_1=\sin\theta+b\sin3\theta$, so $B=4$, $L_9=\frac{243}{104}$, $\kappa_*=\frac{3059}{81}$ (Remark 4(ii) with a certified prefix through
order 18, factor $\frac{19}{18}$) and $k_0=19$.
(a) $O_{18}=\frac{2401}{d_{18}}\mathcal P_{18}(b)$ with an explicit positive integer $d_{18}$ and a primitive integer polynomial
$\mathcal P_{18}$ of degree 18 with positive leading coefficient (given in full in the artifacts, with a SHA-256 hash of its
comma-joined descending coefficients). $\mathcal P_{18}$ is irreducible over $\mathbb Q$: an exact factorization gives one
factor, and independently its reductions (unit leading coefficient, squarefree) factor into irreducible factors of degrees
$1,3,5,9$ modulo 19, $1,1,4,12$ modulo 23, $1,2,3,3,4,5$ modulo 37, $3,4,11$ modulo 47 and $2,16$ modulo 53, whose subset sums
have only $0$ and $18$ in common. It has exactly ten real roots, all simple (exact Sturm chains in both computations),
$$b\approx-0.7278897040,\ -0.0930476777,\ 0.0410531875,\ 0.0598318523,\ 0.0776908602,$$
$$0.0974986694,\ 0.1215109720,\ 0.1550501385,\ 0.2158912625,\ 0.4214946586,$$
isolated in rational intervals of width at most $10^{-30}$ here and $10^{-60}$ in the verification. As at $Q=7,8$,
$\mathcal P_{18}(0)\ne0$, so $\sin\theta$ itself is obstructed at order 18 for every choice of constants. At $n=9$ the formal
resonant stream mode is the zero mode, absent by sine symmetry, so all coefficients through $f_{18}$ and $g_{17}$ are fixed by
$f_1$ and compatibility at order 18 is exactly $O_{18}(b)=0$. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a), and (T_Q-b) holds by the covers of (b) and, independently, by the exact certificate in the proof, so Theorem T_Q gives a
uniquely tuned pure density and stream series at $c=9/7$ converging with all derivatives on an exterior $r>A^{9/2}$, with
$\rho=r^{7/9}f_1+O(r^{5/9})$, and Proposition T_Q.4 gives a convergent potential whose only possible logarithms sit at the
orders 9 and 18.
(b) Explicit exteriors. In the order of the roots and for $\varepsilon=1$, $|\sigma_k|$ is bounded below for every $k\ge2$ by
$2^{20},\ 2^{-3},\ 2^{-14},\ 2^{-14},\ 2^{-12},\ 2^{-10},\ 2^{-10},\ 2^{-6},\ 2^{-6},\ 2^{8}$ (independent certificates: for each root a
768-bit construction and a 1024-bit replay with 25 direct finite responses, 8 comparisons of direct and compact responses,
a complete closed dyadic Taylor cover of the integer tail $t=1/(2k-2)\in[0,\frac1{36}]$, $k\ge19$, whose leaf at $t=0$ contains the
limiting response, and 1978 signed exact prefix coefficients; the replay sums the Taylor terms separately and shares the
audited jet algebra, as in Corollary T_7(b)). The certified-prefix resonance-block majorant of Remark 5(b) with $M=2$
(prefix through order $N=18$, density bounds $d_n>n\|f_n\|_{\ell^1}$, initial harmonic $e_1=0$) and these constants passes at
$w=z^9=r^{-2}=2^{-q}$ with
$$q=130,\ 139,\ 148,\ 148,\ 147,\ 145,\ 146,\ 143,\ 144,\ 134$$
(54 exact rational scalar identities and supersolution inequalities per root), that is $r>2^{65},\ 2^{139/2},\ 2^{74},\ 2^{74},\ 2^{147/2},\ 2^{145/2},\ 2^{73},\ 2^{143/2},\ 2^{72},\ 2^{67}$
times $|\varepsilon|^{9/2}$. Certified prefixes through $N=36,36,54,72,36,36,36,36,36,54$ ($4Q$, $6Q$ or $8Q$; Cartesian
directed-interval prefixes replayed in 2048-bit polar arithmetic with every response rederived from two provisional
continuations; response bounds rational round-downs of the exact global infima of the Values paragraph; $\kappa$ with the
factor $\frac{N+1}N$; exact rational boxes) improve this to
$$q=127,\ 135,\ 144,\ 144,\ 143,\ 142,\ 142,\ 139,\ 140,\ 130$$
(PROVED, independently computed and replayed). So the series of (a) converge, with all weighted derivatives, on
$$r>2^{127/2},\ 2^{135/2},\ 2^{72},\ 2^{72},\ 2^{143/2},\ 2^{71},\ 2^{71},\ 2^{139/2},\ 2^{70},\ 2^{65}$$
times $|\varepsilon|^{9/2}$ (responses scale by $\varepsilon^9$), and $r>2^{72}|\varepsilon|^{9/2}$ is a common sufficient exterior. As at
$Q=7,8$, the longer prefixes lower the radii by small powers of 2 only.
(c) The potential necessarily contains a nonzero term $\varepsilon^9r^2\log r\,(\alpha_9+\beta_9\cos2\theta)$ at order 9 at every
root (PROVED: independent polar and Cartesian computations, full density and stream reconstruction; all ten coefficients of
$a_9$ agree): $a_9=[\sin\theta]f_9$ has exact degree 9 in $b$, with leading coefficient
$\frac{4340888406427735159775152958831807070908446851307288067998397}{30133249523002875527560231676979113065492806369280000}$, and
$\gcd(\mathcal P_{18},a_9)=1$ (also immediate from the irreducibility of $\mathcal P_{18}$ and $\deg a_9=9<18$). The argument is that
of Corollary T_7(c), and the Remark after Corollary T_8 therefore holds for $3\le Q\le9$. The density and stream series stay
pure; no claim is made about the order-18 logarithm.
(d) Necessary radii (PROVED: computed here and independently confirmed at 512 and 1024 bits, $R_H$ to 65 digits), as in
Corollary T_7(d): $R_H=0.6640666020\ldots$ at $\delta=\frac29$ ($h_nR_H^nn^{1+1/b}=0.33936,\ 0.33645,\ 0.33578,\ 0.33539$ at
$n=100,400,800,1500$), and uniform termwise $C^2$ convergence on $\{r\ge R\}$ requires $R>(|\varepsilon b_i|/R_H)^{9/2}$, that is
$R>1.511272$, $1.442854\cdot10^{-4}$, $3.631688\cdot10^{-6}$, $1.978079\cdot10^{-5}$, $6.407849\cdot10^{-5}$, $1.780498\cdot10^{-4}$,
$4.795317\cdot10^{-4}$, $1.436059\cdot10^{-3}$, $6.369501\cdot10^{-3}$, $0.129304$ times $|\varepsilon|^{9/2}$ (rounded down). They bound the
true radius from below only.

Proof. (a) and (c) are finite exact computations, done twice with separately written programs. For (b), the covers give a
positive lower bound $s_i$ for $|\sigma_k(b_i)|$ at every integer $k\ge2$ (direct responses for $2\le k\le26$; for $k\ge19$ the compact
response is a continuous function of $t\in[0,\frac1{36}]$ enclosed leaf by leaf, and the direct and compact values agree at the eight
overlapping indices); with $s_i$, $L_9$ and $\kappa_*$ the comparison of Remark 5(b) dominates every later density and harmonic
coefficient by induction on the order and the resonance period, and the rational supersolution at $w=2^{-q}$ bounds the
majorant series there. Theorem T_Q and Proposition T_Q.4 then apply as in Corollary T_7; homogeneity gives the factor
$|\varepsilon|^{9/2}$. Independently of the covers, (T_Q-b) also follows exactly, as for Corollary T_8, with $k_0=19$. For $k\ge19$, $\sigma_k=N(k,b)/D(k)$ with $N$ of degree 9 in $b$ and degree 595 in $k$, equal to the direct computation at $19\le k\le24$. $D$ is $k$ times a product of powers of 81 distinct linear factors (total degree 594) whose roots are rationals in $[-\frac{59}{18},\frac{43}9]$; the common divisor in $\mathbb Q[k]$ of the ten $b$-coefficients of $N$ has degree 509 and splits into linear factors with roots in the same interval (an independent reconstruction over $\mathbb Q(k)$ from ten exact specializations in $b$ gives the reduced form: numerator and denominator of degree 89 in $k$ after cancelling a common factor of degree 506, numerator-coefficient divisor $(k-1)(k-\frac12)^2$, and the same denominator factors, divisor roots and $\sigma_\infty$). So $D(k)\ne0$ and $N(k,\cdot)\not\equiv0$ for every integer $k\ge19$. For $2\le k\le18$, $\sigma_k$ is a nonzero polynomial of degree 9 in $b$, and $\sigma_\infty$ is a nonzero polynomial of degree 9. A root of the irreducible $\mathcal P_{18}$ is algebraic of degree 18, so no nonzero rational polynomial of degree at most 9 vanishes there; since $\sigma_k\to\sigma_\infty\ne0$, $\inf_{k\ge2}|\sigma_k(b_i)|>0$ at every root. This gives positivity, not the explicit bounds of (b). (d) is Remark 3 of Section 12.6 with $B=4$. $\square$

Values ($\varepsilon=1$; floating point evaluation of the exact formulas; NUMERICAL EVIDENCE, not used in the proof). In the order of the roots, $\sigma_\infty=-6.458\cdot10^6$, $-3.704$, $-5.752\cdot10^{-4}$, $-9.695\cdot10^{-4}$, $1.578\cdot10^{-3}$, $4.286\cdot10^{-3}$, $-1.718\cdot10^{-2}$, $-0.1661$, $0.6416$, $3284$, and $\min_{2\le k\le2000}|\sigma_k|=4.576\cdot10^6$ ($k=8$), $0.9288$ ($k=7$), $3.356\cdot10^{-4}$ ($k=4$), $4.326\cdot10^{-4}$ ($k=7$), $1.583\cdot10^{-3}$ ($k=2000$, the last sampled index, just above $|\sigma_\infty|$), $4.296\cdot10^{-3}$ ($k=2000$, likewise), $6.837\cdot10^{-3}$ ($k=9$), $9.995\cdot10^{-2}$ ($k=9$), $0.1225$ ($k=8$), $2007$ ($k=8$). Each is above the certified bound of (b) for its root, by factors between 4.3 and 7.9. Unlike the third root at $Q=8$ there is no near small divisor; the smallest response, at the third root, belongs to the root with the largest certified radius. Global infima (PROVED, independently confirmed; exact, at the algebraic roots): $\inf_{k\ge2}|\sigma_k(b_i)|$ is attained only at $k=8,7,4,7$ at roots 1 to 4 and only at $k=9,9,8,8$ at roots 7 to 10, with values $4.57599\cdot10^6$, $0.928753$, $3.35596\cdot10^{-4}$, $4.32597\cdot10^{-4}$, $6.83709\cdot10^{-3}$, $9.99473\cdot10^{-2}$, $0.122548$, $2006.76$; at roots 5 and 6 it equals $|\sigma_\infty|$ ($1.57823\cdot10^{-3}$ and $4.28563\cdot10^{-3}$) and is not attained at any finite index. Proof: with $e_i$ the sign of $\sigma_\infty$ and $T_i(b)$ the signed candidate minimum ($\pm\sigma_{k_i}(b)$, or $e_i\sigma_\infty(b)$ at roots 5 and 6), every coefficient of $D(19+x)$ and every nonzero $x$-coefficient of $e_iN(19+x,b)-T_i(b)D(19+x)$ is strictly positive on the rational isolating interval of $b_i$ (interval Horner evaluation; at roots 5 and 6 the two leading coefficients vanish identically), so $|\sigma_k(b_i)|>T_i(b_i)$ for all integers $k\ge19$; for $2\le k\le18$ the comparisons with $T_i$ are strict interval comparisons except at the minimizing index itself. This replaces the sampled minima above by exact ones; the radii of (b) are unchanged. At the tenth root an independent 512-bit ball computation to
order 99 (rechecked independently in 1024-bit Cartesian arithmetic: all 2700 coefficients through order 36, the responses, the Poisson
identities and the full nonlinear sums at orders 50 and 99) gives $\sigma_2,\dots,\sigma_{10}=-1.5726\cdot10^4$, $-5.9917\cdot10^5$, $-3.7255\cdot10^6$, $7.7781\cdot10^6$, $-3.8724\cdot10^6$,
$-1.8300\cdot10^5$, $2.0068\cdot10^3$, $2.8409\cdot10^3$, $2.8540\cdot10^3$ (every tuned obstruction a ball containing zero), all above
the certified bound $2^8$ and equal to the exact values above to all printed digits, and $\|f_{99}\|_{\ell^1}^{1/99}=9.24$. Double-precision tuned runs to order 306 (fits as for Corollary T_7; NUMERICAL EVIDENCE; their 170 responses $\sigma_2,\dots,\sigma_{18}$ agree with the exact values to five digits) give apparent radii $A^{9/2}$ of about $1.1\cdot10^6$, $4.7\cdot10^2$, $0.13$, $0.52$, $2.0$, $8.4$, $41$, $1.8\cdot10^2$, $1.7\cdot10^3$ and $5.3\cdot10^4$ in the order of the roots; at the first and the sixth to tenth roots the fitted slope still decreases as the fit window moves to higher orders.

Corollary T_10 (explicit profiles at $\delta=1/5$, $c=5/4$; PROVED: two independent exact computations of $\mathcal P_{20}$ (a polar one here and a Cartesian one in the verification), identical in all 21 coefficients and in the scale; an independent exact response formula, compared identically with the polar one used here; independent all-index response certificates with a rational-endpoint replay; certified prefixes with independent polar replays and exact rational boxes for the radii of (b); (c) and (d) independently confirmed, including all twenty top coefficients and $R_H$ to 65 digits). Let $Q=10$ and
$f_1=\sin\theta+b\sin3\theta$, so $B=4$, $L_{10}=\frac{75}{29}$, $\kappa_*=\frac{1092}{25}$ (Remark 4(ii) with a certified prefix through
order 20, factor $\frac{21}{20}$) and $k_0=21$.
(a) $O_{20}=-\mathcal P_{20}(b)/d_{20}$ with an explicit positive integer $d_{20}$ (272 digits) and a primitive integer polynomial
$\mathcal P_{20}$ of degree 20 with positive leading coefficient (given in full in the artifacts, with a SHA-256 hash of its
comma-joined descending coefficients). $\mathcal P_{20}$ is irreducible over $\mathbb Q$: an exact factorization gives one
factor, and independently its reductions (unit leading coefficient, squarefree) factor into irreducible factors of degrees
$3,17$ modulo 31, $2,2,3,13$ modulo 41, $1,1,3,7,8$ modulo 59 and $1,8,11$ modulo 61, whose subset sums
have only $0$ and $20$ in common. It has exactly fourteen real roots, all simple (it is irreducible, hence squarefree),
$$b\approx-0.7392162513,\ -0.1026497041,\ -0.0179696714,\ 0.0029607467,\ 0.0187313042,\ 0.0338140463,\ 0.0484678038,$$
$$0.0622821572,\ 0.0771571043,\ 0.0941607772,\ 0.1153410616,\ 0.1459434958,\ 0.2033317730,\ 0.4015874794,$$
isolated in rational intervals of width at most $10^{-30}$ here and $10^{-60}$ in the verification. As at $Q=7,8,9$,
$\mathcal P_{20}(0)\ne0$ ($\mathcal P_{20}(0)\approx-2.17\cdot10^{265}$), so $\sin\theta$ itself is obstructed at order 20 for every choice of constants. At $n=10$ the formal
resonant stream mode is the zero mode, absent by sine symmetry, so all coefficients through $f_{20}$ and $g_{19}$ are fixed by
$f_1$ and compatibility at order 20 is exactly $O_{20}(b)=0$. For every such root and every real $\varepsilon\ne0$,
$f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_Q-a), and (T_Q-b) holds by the proof below (with explicit constants by (b)), so Theorem T_Q gives a
uniquely tuned pure density and stream series at $c=5/4$ converging with all derivatives on the exterior of (b), with
$\rho=r^{4/5}f_1+O(r^{3/5})$, and Proposition T_Q.4 gives a convergent potential whose only possible logarithms sit at the
orders 10 and 20.
(b) Explicit response bounds and exteriors (PROVED: independent certificate with a separate rational-endpoint replay; independently computed and replayed prefixes and boxes). In the order of the roots and for $\varepsilon=1$, $|\sigma_k|$ is bounded below for every $k\ge2$ by
$$2^{26},\ 2^{5},\ 2^{-6},\ 2^{-11},\ 2^{-23},\ 2^{-12},\ 2^{-11},\ 2^{-10},\ 2^{-8},\ 2^{-7},\ 2^{-5},\ 2^{-1},\ 2^{5},\ 2^{15}$$
(for $k\ge21$ every coefficient of $D(21+x)$ is positive and every coefficient of $e_iN(21+x,b)-s_iD(21+x)$, $e_i$ the sign of $\sigma_\infty(b_i)$, is nonnegative on the isolating interval of $b_i$ with positive constant term, 1540 nonzero tail coefficients in all; for $2\le k\le20$, 266 strict interval comparisons). With these constants and $L_{10}$, the certified-prefix resonance-block majorant of Remark 5(b) (prefix through order $N=40,40,80,40,60,40,40,80,40,60,40,40,60,40$, that is $4Q$, $6Q$ or $8Q$; rational upper bounds for $n\|f_n\|_{\ell^1}$, $n\le N$, and for $aQ|H_{aQ}|$, $2\le a<N/Q$, the harmonic at order $Q$ being zero; $\kappa=\frac{208}{5}\frac{N+1}N$; Cartesian directed-interval prefixes, 800 exact low-order comparisons per root, replayed in 2048-bit polar arithmetic with every response rederived from two provisional continuations; exact rational boxes) passes at $w=z^{10}=r^{-2}=2^{-q}$ with
$$q=147,\ 152,\ 160,\ 165,\ 177,\ 167,\ 166,\ 165,\ 164,\ 163,\ 162,\ 159,\ 154,\ 149$$
(PROVED, independently computed and replayed). At the fifth root a tail-only response bound improves this: the prefix through $N=120$ already contains the harmonics $H_{10k}$ with $k<12$, so only the responses with $k\ge12$ enter the tail ($H_{120}$, the first harmonic fixed in the tail, solves $R_{120}+\sigma_{12}H_{120}=0$ at order 130), and $|\sigma_k|>2^{-20}$ for every $k\ge12$ (exact interval evaluation of the response polynomials for $12\le k\le20$ and the positive-coefficient test above for $k\ge21$, with 110 positive shifted numerator and 110 positive denominator coefficients); the exact box passes at $q=174$ (PROVED, independently replayed). So the series of (a) converge, with all weighted derivatives, on
$$r>2^{147/2},\ 2^{76},\ 2^{80},\ 2^{165/2},\ 2^{87},\ 2^{167/2},\ 2^{83},\ 2^{165/2},\ 2^{82},\ 2^{163/2},\ 2^{81},\ 2^{159/2},\ 2^{77},\ 2^{149/2}$$
times $|\varepsilon|^5$, in particular on $r>2^{87}|\varepsilon|^5$ at every root. These are sufficient radii only; they are not estimates of the true radii.
(c) The potential necessarily contains a nonzero term $\varepsilon^{10}r^2\log r\,(\alpha_{10}+\beta_{10}\cos2\theta)$ at order 10 at every
root (PROVED: independent polar and Cartesian computations, full density and stream reconstruction; all eleven coefficients of
$a_{10}$ agree): $a_{10}=[\sin\theta]f_{10}$ has exact degree 10 in $b$, with leading coefficient
$-\frac{46561666649544153955167479676895117318053568650766058315542118351}{1123218368027928974941550686614820172006625299854824960}$, $\beta_{10}-\alpha_{10}=a_{10}/4$, and
$\gcd(\mathcal P_{20},a_{10})=1$ (also immediate from the irreducibility of $\mathcal P_{20}$ and $\deg a_{10}=10<20$). The argument is that
of Corollary T_7(c), and the Remark after Corollary T_8 therefore holds for $3\le Q\le10$. The density and stream series stay
pure; no claim is made about the order-20 logarithm.
(d) Necessary radii (PROVED: computed here and independently confirmed, $R_H$ to 65 digits), as in
Corollary T_7(d): $R_H=0.5845837583\ldots$ at $\delta=\frac15$ ($h_nR_H^nn^{1+1/b}=0.29568,\ 0.29309,\ 0.29249,\ 0.29215$ at
$n=100,400,800,1500$), and uniform termwise $C^2$ convergence on $\{r\ge R\}$ requires $R>(|\varepsilon b_i|/R_H)^5$, that is
$R>3.233134$, $1.669378\cdot10^{-4}$, $2.744523\cdot10^{-8}$, $3.332518\cdot10^{-12}$, $3.377585\cdot10^{-8}$, $6.475182\cdot10^{-7}$,
$3.917716\cdot10^{-6}$, $1.372728\cdot10^{-5}$, $4.005399\cdot10^{-5}$, $1.084217\cdot10^{-4}$, $2.990101\cdot10^{-4}$, $9.698174\cdot10^{-4}$,
$5.090875\cdot10^{-3}$, $0.1529914$ times $|\varepsilon|^5$ (rounded down; at equality the highest second-angular-derivative coefficient grows like $n^{11/30}$, so the boundary itself is excluded). They bound the
true radius from below only.

Proof. (a) and (c) are finite exact computations, done twice with separately written programs. For (T_Q-b), with $k_0=21$: for $k\ge21$, $\sigma_k=N(k,b)/D(k)$, where after cancellation $N$ has degree 10 in $b$ and degree 109 in $k$, and $D$ is $k$ times a product of 100 further distinct linear factors, eight of them squared (total degree 109), whose roots are rationals in $[-\frac{15}4,\frac{21}4]$; the common divisor in $\mathbb Q[k]$ of the eleven $b$-coefficients of $N$ is $(k-1)(k-\frac12)^2$. This reduced form was computed from eleven exact specializations in $b$ (an independent Cartesian computation) and agrees identically in $k$, at all eleven specializations, with the full response computed by the polar recurrence used here (the two share the rational-function arithmetic); six direct computations at $21\le k\le26$ agree with it. So $D(k)\ne0$ and $N(k,\cdot)\not\equiv0$ for every integer $k\ge21$. For $2\le k\le20$, $\sigma_k$ is a nonzero polynomial of degree 10 in $b$, and $\sigma_\infty$ is a nonzero polynomial of degree 10. A root of the irreducible $\mathcal P_{20}$ is algebraic of degree 20, so no nonzero rational polynomial of degree at most 10 vanishes there; since $\sigma_k\to\sigma_\infty\ne0$, $\inf_{k\ge2}|\sigma_k(b_i)|>0$ at every root, and Theorem T_Q and Proposition T_Q.4 apply as in Corollary T_7; homogeneity gives the factor $|\varepsilon|^5$ (responses scale by $\varepsilon^{10}$). For the explicit bounds of (b): $D(21+x)$ has positive coefficients, and the coefficient inequalities make $e_iN(21+x,b_i)-s_iD(21+x)>0$ for every real $x\ge0$, so $|\sigma_k(b_i)|>s_i$ for every integer $k\ge21$; the finite comparisons cover $2\le k\le20$. (d) is Remark 3 of Section 12.6 with $B=4$. $\square$

Values ($\varepsilon=1$; floating point evaluation of the exact formulas; NUMERICAL EVIDENCE, not used in the proof). In the order of the roots, $\sigma_\infty=-1.300\cdot10^8$, $64.92$, $3.392\cdot10^{-2}$, $9.020\cdot10^{-4}$, $1.991\cdot10^{-5}$, $7.992\cdot10^{-4}$, $1.265\cdot10^{-3}$, $-2.383\cdot10^{-3}$, $-4.926\cdot10^{-3}$, $1.994\cdot10^{-2}$, $9.856\cdot10^{-2}$, $-0.6819$, $-51.49$, $-9.280\cdot10^4$, and $\min_{2\le k\le2000}|\sigma_k|=1.219\cdot10^8$ ($k=9$), $46.79$ ($k=9$), $2.764\cdot10^{-2}$ ($k=8$), $9.028\cdot10^{-4}$ ($k=2000$, the last sampled index, just above $|\sigma_\infty|$), $2.438\cdot10^{-7}$ ($k=8$), $3.551\cdot10^{-4}$ ($k=4$), $5.647\cdot10^{-4}$ ($k=7$), $2.116\cdot10^{-3}$ ($k=7$), $4.938\cdot10^{-3}$ ($k=2000$, likewise), $9.269\cdot10^{-3}$ ($k=9$), $5.254\cdot10^{-2}$ ($k=9$), $0.6820$ ($k=2000$, likewise), $45.87$ ($k=9$), $7.142\cdot10^4$ ($k=9$). Each is above the certified bound of (b) for its root, by factors between 1.15 and 2.2. At the fifth root $\sigma_7\approx-1.01\cdot10^{-4}$, $\sigma_8\approx-2.44\cdot10^{-7}$ and $\sigma_9\approx5.6\cdot10^{-7}$: the response changes sign between $k=8$ and $9$ and passes close to zero at $k=8$, about 80 times below $|\sigma_\infty|$; as at the third root at $Q=8$ this is a near small divisor of the tuning, not a zero. Global infima (PROVED, independently confirmed; exact, at the algebraic roots): $\inf_{k\ge2}|\sigma_k(b_i)|$ is attained only at $k=9,9,8$ at roots 1 to 3, at $k=8,4,7,7$ at roots 5 to 8, at $k=9,9$ at roots 10 and 11 and at $k=9,9$ at roots 13 and 14, with values $1.21876\cdot10^8$, $46.7895$, $2.76399\cdot10^{-2}$, $2.43768\cdot10^{-7}$, $3.55078\cdot10^{-4}$, $5.64687\cdot10^{-4}$, $2.11587\cdot10^{-3}$, $9.26865\cdot10^{-3}$, $5.25377\cdot10^{-2}$, $45.8745$, $7.14208\cdot10^4$; at roots 4, 9 and 12 it equals $|\sigma_\infty|$ ($9.02039\cdot10^{-4}$, $4.92551\cdot10^{-3}$ and $0.681896$) and is not attained at any finite index. Proof: as at $Q=9$, with $D$ made monic, $e_i$ the sign of $\sigma_\infty$ and $T_i(b)$ the signed candidate minimum, every coefficient of $D(21+x)$ and every nonzero $x$-coefficient of $e_iN(21+x,b)-T_i(b)D(21+x)$ is strictly positive on the rational isolating interval of $b_i$ (directed 1024-bit Horner evaluation, replayed at 1536 bits; 1537 positive coefficients, and at roots 4, 9 and 12 the leading coefficient vanishes identically), so $|\sigma_k(b_i)|>T_i(b_i)$ for all integers $k\ge21$; for $2\le k\le20$ there are 266 finite comparisons with $T_i$: 255 strict interval comparisons and 11 identities at the attained minimizing indices. This replaces the sampled minima above by exact ones; the response bounds of (b) are unchanged. The fifth root has the smallest infimum, $2.44\cdot10^{-7}$ at $k=8$, about 82 times below $|\sigma_\infty|$. Double-precision tuned runs at the fourteen roots to order 300 (NUMERICAL EVIDENCE; block-maximum line fits on $n\ge100,150,200$ as in the numerical part of the report) give apparent radii $A^5$ between $0.157$ and $0.163$ at the sixth root, $1.2$ to $1.7$ at the fifth and $2.2\cdot10^7$ to $3.5\cdot10^7$ at the first, each far above the necessary radius of (d); these give no bound on the true radius.

Proposition T_Q.4 (a convergent potential series; PROVED: independent proof, reviewed here). Let $Q\ge3$ be an integer and
let real sine polynomials $f_n$ (odd frequencies at most $Bn-1$) and $g_n$ (even frequencies at most $Bn$) satisfy the
Poisson equation (T2) at every order and $\|f_n\|_{\ell^1}+\|g_n\|_{\ell^1}\le CA^n$. Put $S_n=4-\frac{2n}Q$. Then there are even
cosine polynomials $C_n$ of degree at most $Bn-2$ with $\|C_n\|_{\ell^1}\le C'A^n$ and real $\alpha,\beta,\lambda$ such that
$$\chi=\sum_{n\ge1}r^{S_n}C_n(\theta)+r^2\log r\,(\alpha+\beta\cos2\theta)+\lambda\log r$$
satisfies $\chi_{xy}=\psi$ and $-\partial_y\Delta\chi=\rho$, and for every $R>A^{Q/2}$ the series and each Cartesian derivative of
order $h$, multiplied by $r^{h-S_1}$, converge absolutely and uniformly on $r\ge R$. In particular the solutions of Theorem T_Q
and Corollary T_5 have such a potential, with logarithms only at the orders $Q$ and $2Q$. The same holds without the
weight: for each derivative order $h$, $S_n-h<0$ once $n>Q(4-h)/2$, so the tail of the differentiated series from that
order on converges absolutely and uniformly on $r\ge R$, and the finitely many earlier terms do not affect uniform
convergence. The same remark applies to the density and stream series of Theorem T_Q, whose exponents $p_n$, $P_n$ are
negative for $n>Q$.

Proof (outline; at $Q=3$ this is Proposition T.5). Write $\Delta\chi_n=r^{-2x}\sum_md_m\cos2m\theta$ with $x=\frac nQ-1$. Then
$-\partial_y\Delta\chi_n=r^{p_n}f_n$ is the bidiagonal system $a_0=2xd_0+(1-x)d_1$, $a_m=(m+x)d_m+(m+1-x)d_{m+1}$, whose
descending solution obeys $\|d\|\le\frac{2BQ}3\|f_n\|$ for $n\ge4Q$. The Laplace multipliers $S_n^2-4m^2$ vanish only when
$Q\mid n$; at $n=kQ\ge4Q$ the single zero is at $m=k-2$, where the system reads $a_{k-2}=(2k-3)d_{k-2}$ and compatibility
($a_{kQ,2k-3}=0$) gives $d_{k-2}=0$; elsewhere $|S_n^2-4m^2|\ge2n/Q^2$. The harmonic $r^{-\ell}\cos\ell\theta$, $\ell=2k-4$, has
zero density and stream $\ell(\ell+1)r^{-\ell-2}\sin((\ell+2)\theta)$, which matches the prescribed resonant stream coefficient.
This gives $\|C_n\|\le\frac{BQ^3}{3n}[1+Q^2(B+1)^2]\|f_n\|+Q^2\|g_n\|/n^2$ for $n\ge4Q$, so the base $A$ is preserved. The
finitely many orders $n<4Q$ are finite invertible linear problems except at $n=Q$ and $n=2Q$, where
$r^2\log r\mapsto(\rho,\psi)=(-4r^{-1}\sin\theta,\sin2\theta)$, $r^2\log r\cos2\theta\mapsto(4r^{-1}(\sin\theta+\sin3\theta),
-\frac12\sin4\theta)$ and $\log r\mapsto(0,-r^{-2}\sin2\theta)$ supply the missing density and stream. $\square$

Theorem T_Q.5 (genericity on every regular compatibility component, $Q\in\{3,5\}$; PROVED: independent proof, reviewed
here). Let $Q\in\{3,5\}$, let $B\ge6$ be even and write normalized profiles $f(b,t)=\sin\theta+b\sin3\theta+\sum_{5\le j<B,\,j\text{ odd}}t_j\sin j\theta$.
Let $\mathcal M=\{(b,t):O_{2Q}=0,\ \nabla O_{2Q}\ne0\}$ and $\mathcal G=\{(b,t)\in\mathcal M:\inf_{k\ge2}|\sigma_k|>0\}$. Then $\mathcal G$
is open and dense in every connected component of $\mathcal M$ and $\mathcal M\setminus\mathcal G$ has measure zero in every
chart; no component needs to contain a known admissible profile. Every point of $\mathcal G$ has the tuned convergent series of
Theorem T ($Q=3$) or Theorem T_Q ($Q=5$), and every compact subset of $\mathcal G$ has a common radius. For $B=6$,
$\mathcal M\setminus\mathcal G$ is countable, closed in $\mathcal M$, and accumulates in $\mathcal M$ only at the finitely many points
where $\sigma_\infty=0$. Profiles with a nonzero $\sin\theta$ coefficient reduce to this case by scaling.

Proof. $O_{2Q}$ is homogeneous of degree $2Q$ in the coefficients, so after normalization it has total degree at most $2Q$
in $(b,t)$; its restriction to $t=0$ is a nonzero multiple of the irreducible $\mathcal P_6$ (Corollary T.3) or
$\mathcal P_{10}$ (Corollary T_5), so the coefficient of $b^{2Q}$ is a nonzero constant. Let $P$ be the monic multiple. A
factorization $P=AC$ in $\mathbb Q[t,b]$ has constant leading coefficients in $b$, so it specializes at $t=0$ with both
$b$-degrees preserved; hence $P$ is irreducible, also in $\mathbb Q(t)[b]$. Each $\sigma_h$ ($h=k\ge2$ or $h=\infty$) is a
polynomial of total degree at most $Q<2Q$ (Corollary T_Q.3(b), T.8(a)) whose restriction to $t=0$ is nonzero, so
$R_h(t)=\operatorname{Res}_b(P,\sigma_h)\in\mathbb Q[t]$ is nonzero, and since $P$ is monic, $R_h(t)=0$ wherever $P$ and $\sigma_h$
have a common real zero. The points of $\mathcal M$ with $\partial_bP\ne0$ are dense in $\mathcal M$: if $\partial_bP\equiv0$ on an
open piece, the piece is a graph $t_j=\phi(b,\hat t)$ with $\partial_b\phi=0$, so $P(\cdot,t)$ would vanish on an interval for
fixed $t$, impossible for a monic polynomial. Near a point with $\partial_bP\ne0$, $\mathcal M$ is a graph $b=\beta(t)$ over an
open set, so $\sigma_h$ cannot vanish on an open piece of $\mathcal M$ ($R_h$ would vanish on an open set). Hence each zero set
$\{\sigma_h=0\}\cap\mathcal M$ is closed and nowhere dense, and of measure zero (it is the zero set of an analytic function
not identically zero on any component). Since $\sigma_k\to\sigma_\infty$ locally uniformly, $\inf_k|\sigma_k|>0$ holds
exactly when $\sigma_\infty\ne0$ and every $\sigma_k\ne0$, and this set is open; Baire's theorem gives density. For $B=6$
each $R_h$ has finitely many zeros and each fiber of $P$ at most $2Q$ points, so every $\{\sigma_h=0\}\cap\{P=0\}$ is finite;
near a point with $\sigma_\infty\ne0$ only finitely many $k$ matter, which gives the accumulation statement. $\square$

This removes from Theorem T.8 the hypothesis that the component contains a known admissible profile, for regular
components of the normalized hypersurface.

Remarks. 1. The proof never uses the parity of $Q$. Two independent derivations of Lemma T_Q.1, the inequalities
(I1$_Q$) to (I3$_Q$), the generating system and the response bound agree term by term, including the constants
$\kappa_Q$ and $L_Q$, and the independent audit covers every integer $Q\ge3$. The exact data of Corollary T_5 were computed twice, by a Fourier-coefficient program and
by an independent Cartesian-monomial program; $O_{10}$, $\sigma_k$ for $2\le k\le12$, the rational function $\sigma(k)$ (an
exact polynomial identity after cross-multiplication) and $\sigma_\infty$ agree identically.
2. For the other rational $\delta$ ($h\ge2$ in Section 14.2) the first resonant order equals the period. Each obstruction
is still affine in the preceding constant (a product of two factors that depend on $H_n$ has order at least
$2n+1>n+Q$), but the first constant enters at the period itself, and the generating system needs shifted starting
degrees; Section 12.6 gives it (Theorem T_{Q,h}, PROVED).
3. The proof of Theorem T_Q.5 uses only the irreducibility of the two-mode restriction $\mathcal P_{2Q}$ and the degree
bound $\deg\sigma_h\le Q$. With $\mathcal P_8$ of Corollary T_4(a) it gives the same statement at $Q=4$ (PROVED:
independently confirmed), and with $\mathcal P_{12}$ of Corollary T_6(a) at $Q=6$ (PROVED: independently confirmed). With
$\mathcal P_{14}$ of Corollary T_7(a) it gives the same statement at $Q=7$ (PROVED: independently confirmed): $\mathcal P_{14}$ is
irreducible of full degree $2Q=14$, and the restrictions to $t=0$ of $\sigma_k$ ($2\le k\le14$), of $N(k,\cdot)$ ($k\ge15$) and of
$\sigma_\infty$ are nonzero polynomials of degree at most 7, which is all the proof uses. In the same way $\mathcal P_{16}$ of
Corollary T_8(a) gives it at $Q=8$ (PROVED: independently confirmed, including the countable closed exceptional set
of the three-mode extension). $\mathcal P_{18}$ of Corollary T_9(a) gives it at $Q=9$ (PROVED, independently confirmed): $\mathcal P_{18}$ is irreducible of full degree 18, and the restrictions to $t=0$ of $\sigma_k$ ($2\le k\le18$), of $N(k,\cdot)$ ($k\ge19$) and of $\sigma_\infty$ are nonzero polynomials of degree at most 9 (proof of Corollary T_9). $\mathcal P_{20}$ of Corollary T_10(a) gives it at $Q=10$ (PROVED, independently confirmed, including the countable closed exceptional set of the three-mode extension): $\mathcal P_{20}$ is irreducible of full degree 20, and the restrictions to $t=0$ of $\sigma_k$ ($2\le k\le20$), of $N(k,\cdot)$ ($k\ge21$) and of $\sigma_\infty$ are nonzero polynomials of degree at most 10 (proof of Corollary T_10).
4. For $\sin\theta$ itself, $O_{10}=\mathcal P_{10}(0)/d_{10}\ne0$ at $\delta=2/5$, so the pure series of $\sin\theta$ is
obstructed at order 10 for every choice of constants, as at $\delta=2/3$.

### 12.6 Theorem T_{Q,h}: every rational $\delta\in(0,1)$ (PROVED: independent proof, reviewed here line by line)

Every rational $\delta\in(0,1)$ has a unique representation $\delta=\frac{2h}Q$ with coprime positive integers $h,Q$ and $2h<Q$:
for $\delta=\frac ab$ in lowest terms, $(h,Q)=(\frac a2,b)$ if $a$ is even and $(h,Q)=(a,2b)$ if $a$ is odd. Section 12.5 is the
case $h=1$. This section treats $h\ge2$. It includes $\delta=\frac49$ ($h=2$, $Q=9$), close to Candidate 007 ($\delta\approx0.4476$),
and formally Candidate 007's stored rational value itself ($Q=8152952920478362$, the first resonant order of Section 0
item 6), where the first compatibility condition is out of computational reach. The new feature is that the first stream resonance is the period $Q$ itself, so the first compatibility
condition precedes every free constant and the free constant of the first resonance is already present at order $Q$.

Setting. Fix coprime integers $h\ge2$, $Q>2h$, and put $\delta=\frac{2h}Q$, $c=\frac Q{Q-2h}$, $p_n=1-\frac{2hn}Q$,
$P_n=2-\frac{2hn}Q$, $\lambda_n=(n-1)(c-1)=\frac{2h(n-1)}{Q-2h}$. The order equations (T1), (T2) hold verbatim. Since $P_n<2$, (T2)
is singular only where $P_n=-q$ for an even $q\ge2$, that is $n=\frac{Q(q+2)}{2h}$; as $\gcd(h,Q)=1$ this means $n=kQ$ and
$q=q_k:=2hk-2$, $k\ge1$. There (T2) reads $0=-q_ka_{kQ,q_k-1}$ (the density mode $q_k+1$ has the factor $p_n+q_k+1=0$), so the
obstruction is $O_{kQ}:=a_{kQ,\,2hk-3}$ and $H_{kQ}:=b_{kQ,q_k}$ is free. Every other divisor $q\pm P_n$ is a nonzero element of
$\frac2Q\mathbb Z$, so the Poisson inverses obey $\|\Pi_nf\|,\|\Pi'_nf\|\le\frac Q2\|f\|$. At $\delta=\frac49$ the first three
resonances are $(n,q_k,2hk-3)=(9,2,1),(18,6,5),(27,10,9)$.

Response coefficients. For $k\ge1$ and $n=kQ$ define $\varphi_1,\dots,\varphi_Q$ by the recursion of Section 12.5 with
$e_k=\sin q_k\theta$ (the orders $n+1,\dots,n+Q-1$ are nonresonant), and let $\sigma_k$ be the coefficient of
$\sin((2h(k+1)-3)\theta)$ in $\varphi_Q$, the obstruction mode at order $(k+1)Q$. It depends only on $f_1,\dots,f_Q$,
$g_1,\dots,g_{Q-1}$ and $k$, and it is homogeneous of degree $Q$ in $f_1$.

Lemma T_{Q,h}.1. Let $k\ge1$, $n=kQ$, and fix all constants except $H_n$. Then $f_{n+r}=f^{(0)}_{n+r}+H_n\varphi_r$ for
$1\le r\le Q$, and $O_{n+Q}=R_k+\sigma_kH_n$, where $R_k$ is the coefficient of $\sin((2h(k+1)-3)\theta)$ in $f^{(0)}_{n+Q}$.

Proof. As Lemma T_Q.1: a product in which both factors depend on $H_n$ has order at least $2n+1>n+Q$, since $n\ge Q$. The low
factors $f_r$ ($r\le Q$) and $g_{r-s}$ ($r-s\le Q-1$) contain no constant, since the first constant sits in $g_Q$. $\square$

Proposition T_{Q,h}.2. If $O_Q(f_1)=0$ and $\sigma_k\ne0$ for all $k\ge1$, there is exactly one sequence $(H_{kQ})_{k\ge1}$
for which the pure ansatz solves every order, namely $H_{kQ}=-R_k/\sigma_k$, determined recursively in $k$. $\square$

Theorem T_{Q,h}. Let $h\ge2$ and $Q>2h$ be coprime, $\delta=\frac{2h}Q$, $c=\frac Q{Q-2h}$, and let $f_1$ be a nonzero real sine
polynomial with odd frequencies below an even $B$. Assume (T_{Q,h}-a) $O_Q(f_1)=0$, and (T_{Q,h}-b) $\sigma_k\ne0$ for every
$k\ge1$ and $\sigma_*:=\inf_{k\ge1}|\sigma_k|>0$. Let $(H_{kQ})$ be the constants of Proposition T_{Q,h}.2. Then items 1 to 4 of
Theorem T_Q hold with $A^{Q/2}$ replaced by $A^{Q/(2h)}$, with the homogeneity degrees $Q$ and $Q$ of $O_Q$ and $\sigma_k$
in place of $2Q$ and $Q$ in item 4 and with $\rho=r^{1-2h/Q}f_1+O(r^{1-4h/Q})$; replacing $f_1$ by
$\varepsilon f_1$ preserves the hypotheses and multiplies every sufficient radius by $|\varepsilon|^{Q/(2h)}$. The constants $C,A$
depend only on $B$, $Q$, $h$, $\|f_1\|_{\ell^1}$ and $\sigma_*$.

Proof of item 1. Step 1. With the frequency bounds $Bn-1$ and $Bn$, $|p_j|\le j$, $|P_i|\le(2-\delta)i$ and
$\frac m{\lambda_m}\le\frac{Q-2h}h$ for $m\ge2$, the constants are
$$\kappa=\kappa_{Q,h}:=\frac{B(Q-2h)(3-\frac{2h}Q)}h,\qquad L=\frac Q2,$$
and $N_n\le LM_n+|H_n|$ at resonant $n$. Step 2. The inequalities (I1$_Q$) to (I3$_Q$) hold verbatim, now for every $n=kQ$
with $k\ge1$, where $\eta_n=n|H_n|$ at $n=kQ\ge Q$ and $\eta_n=0$ otherwise; the justification is the same (the nonzero $\eta_i$
in $f^{(0)}_{n+r}$ have $i\le n-Q$, so their partners have order at least $Q+r$). The density norms $x_1,\dots,x_Q$ contain no
$\eta$, since a term $\eta_ix_j$ needs $i\ge Q$ and $j\ge1$. Step 3. Define $\bar x_n$ by equality in (I1$_Q$) and
$\bar u_{n,r},\bar\eta_n$ by equality in (I2$_Q$), (I3$_Q$) for every base index $n\ge Q$ (at nonresonant $n$ these are
artificial nonnegative majorants), computed in the order $\bar x_n$, $\bar u_{n,1},\dots,\bar u_{n,Q-1}$, $\bar\eta_n$, then
$\bar x_{n+1}$. In particular $\bar\eta_Q$ is included and is not zero. By induction $x_n\le\bar x_n$ and $\eta_n\le\bar\eta_n$.

Step 4 (shifted generating functions). With $\bar x_j=\mathrm{Cat}_{j-1}(\kappa L)^{j-1}\bar x_1^j$ for $j\le Q$, $P$ and $P_r$ as in
Section 12.5, put
$$X=P+z^{Q+1}W,\qquad\sum_{n\ge Q}\bar\eta_nz^n=z^QE,\qquad\sum_{n\ge Q}\bar u_{n,r}z^n=z^QV_r,$$
$$A_r=z^{-(Q+r)}\big[P_r^2\big]_{\ge Q+r}+2z^{1-r}P_rW+z^{Q+2-r}W^2\qquad(1\le r\le Q).$$
The equalities are equivalent to
$$W=\kappa L\,z^{-(Q+1)}\big[P^2\big]_{\ge Q+1}+2\kappa LPW+\kappa Lz^{Q+1}W^2+\kappa E\big(z^{-1}P+z^QW\big),$$
$$V_r=\kappa\Big[LA_r+z^{Q+1-r}EW+Q\sum_{s=1}^{r-1}\bar x_sV_{r-s}\Big]\quad(1\le r\le Q-1),\qquad
E=\frac\kappa{\sigma_*}\Big[LA_Q+zEW+Q\sum_{s=1}^{Q-1}\bar x_sV_{Q-s}\Big].$$
The shifts are the only difference from Section 12.5: the product of $z^QE$ with $X=P+z^{Q+1}W$ starts at degree $Q+1$ and
gives $E(z^{-1}P+z^QW)$ after division by $z^{Q+1}$; in a lookahead row it is $(z^QE)(z^{Q+1}W)$ divided by $z^{Q+r}$, which
gives $z^{Q+1-r}EW$; the sums $\sum_{i+j=n+r,\,i,j\ge r}\bar x_i\bar x_j$ over $n\ge Q$ give $A_r$ after division by $z^{Q+r}$.
At $z=0$, $A_r(0)=[z^{Q+r}]P_r^2$ is a constant, every other nonlinear term carries a positive power of $z$, and the only
unknown in the $W$ row is $\kappa\bar x_1E$. Hence $\Phi(0,Y)=c_0+JY$ with $J$ strictly lower triangular in the order
$Y=(V_1,\dots,V_{Q-1},E,W)$, so $J^{Q+1}=0$ and $\det(I-J)=1$; the formal solution is unique, the holomorphic implicit
function theorem gives a positive radius, and $\bar x_n+\bar\eta_n\le CA^n$. (Keeping $P$ of degree $Q-1$ and putting
$\bar x_Q$ into $W$ would instead leave the quadratic term $EW$ in the $E$ row at $z=0$.) The box test of Step 4 applies
verbatim with this order of the unknowns: if $G(z_0,2Y_0)\le2Y_0$, then $A=z_0^{-1}$ is admissible. $\square$

Proof of items 2 to 4. As for Theorem T, with $z=r^{-2h/Q}$; so every $R>A^{Q/(2h)}$, in particular $R>z_0^{-Q/(2h)}$ after a
passing box test, is sufficient. $p_n<0$ and $P_n<0$ for $n>Q/h$. $\square$

Proposition T_{Q,h}.3 (a convergent potential series; PROVED: independent proof, reviewed here). Under the hypotheses of
Proposition T_Q.4 with $\delta=\frac{2h}Q$, $h\ge2$, put $S_n=4-\frac{2hn}Q$. There are even cosine polynomials $C_n$ of degree at
most $Bn-2$ with $\|C_n\|_{\ell^1}\le C'A^n$ and, for $h=2$ only, a real $\lambda$, such that
$\chi=\sum_nr^{S_n}C_n(\theta)+\lambda\log r$ satisfies $\chi_{xy}=\psi$ and $-\partial_y\Delta\chi=\rho$, with the convergence
statements of Proposition T_Q.4 for every $R>A^{Q/(2h)}$. For $h\ge3$ no logarithm occurs. The pressure is single valued.

Proof (outline). Write $\Delta\chi_n=r^{-2x}\sum_md_m\cos2m\theta$ with $x=\frac{hn}Q-1$. The descending bidiagonal system of
Proposition T_Q.4 fails only at $x=0$, that is $hn=Q$, which coprimality and $h\ge2$ exclude; for $n\ge4Q$ it gives
$\|d\|\le\frac{2BQ}{3h}\|f_n\|$. The Laplace multiplier $S_n^2-4m^2$ vanishes only at $n=kQ$, $m=hk-2$; there the equation for
$d_{hk-2}$ reads $a_{kQ,2hk-3}=(2hk-3)d_{hk-2}$, so compatibility gives $d_{hk-2}=0$, and elsewhere $|S_n^2-4m^2|\ge\frac{2hn}{Q^2}$.
At $n=kQ$ the harmonic $r^{-\ell}\cos\ell\theta$, $\ell=2hk-4$, has zero density and stream $\ell(\ell+1)r^{-\ell-2}\sin((\ell+2)\theta)$,
with $\ell+2=q_k$ and $-\ell-2=P_{kQ}$, which matches the prescribed resonant stream coefficient whenever $\ell>0$. This gives
$\|C_n\|\le\frac{BQ^3}{3h^2n}[1+\frac{Q^2}{h^2}(B+1)^2]\|f_n\|+\frac{Q^2}{h^2n^2}\|g_n\|$ for $n\ge4Q$, so the base is preserved.
The only case with $\ell=0$ is $h=2$, $k=1$: then $S_Q=0$, compatibility removes the $\sin\theta$ density mode, and
$\lambda\log r$ supplies the free stream $H_Q\sin2\theta$ at $r^{-2}$, because $\Delta\log r=0$ and
$\partial_x\partial_y\log r=-r^{-2}\sin2\theta$. Every term has even reflection symmetry, so the Darcy one-form has zero period
and the pressure is single valued, as in Section 12.3. $\square$

Corollary T_{Q,h}.4 (uniform response bound, limit, openness). (a) $|\sigma_k(f)|\le\frac12\binom{2Q}Q\kappa_{Q,h}^QL^{Q-1}\|f\|_1^Q$
for every complex $f$ with frequencies below $B$ and every $k\ge1$. (b) For $k\ge k_0:=\lceil\frac{QB+2}{2h}\rceil$,
$\sigma_k=N(k,f)/D(k)$ with $N$ homogeneous of degree $Q$ in $f$ and $D$ without zeros at integers $k\ge k_0$; the limit
$\sigma_\infty=\lim_k\sigma_k$ exists, is a form of degree $Q$, and the convergence is uniform on bounded sets. (c) The set of
profiles satisfying (T_{Q,h}-b) is open, and $\inf_{k\ge1}|\sigma_k|>0$ holds exactly when $\sigma_\infty\ne0$ and every
$\sigma_k\ne0$.

Proof. As Corollary T_Q.3, with $\kappa_{Q,h}$; for (b), once $q_k\ge QB$ no response frequency folds through zero. $\square$

The limit also has a direct formula (PROVED: independent derivation, reviewed here; it reproduces the exact limits of
Corollaries T.3, T_4 and T_5, and at $\delta=\frac49$ it coincides exactly, as a polynomial of degree 9 in $b$, with the leading
coefficient of the generic rational function $\sigma_k=N(k,b)/D(k)$ computed by the program of this section). In the Laurent encoding $\sin m\theta\leftrightarrow(z^m-z^{-m})/2$ with $A_j=\sum_m(p_j+m)a_{j,m}z^m$ and
$B_j=\sum_m(P_j+m)b_{j,m}z^m$, put $(L_sv)(z)=-\sum_\nu v_\nu z^{\nu+1}/(2(\nu+1-\delta s))$ and
$u_r=(1-\delta)\big[-\frac12A_r+\sum_{s=1}^{r-1}(u_sB_{r-s}-(L_su_s)A_{r-s})\big]$; then $\sigma_\infty=2[z^{2h-1}]u_Q$. It is
obtained from the response recursion by keeping the leading order in $q_k$ of the positive carrier.

The whole tail $k\ge k_0$ also has a compact form (PROVED: independent derivation, reviewed here). Put $t=1/q_k$ and factor
out the carrier $z^{q_k}$; a high field of radial degree $-q_k-\alpha$ ($\alpha=1+\delta s$ for the density and $\alpha=\delta s$
for the stream at step $s$, $\alpha=0$ for $e_k$) and offset $v$ has $q_k^{-1}\partial_x,q_k^{-1}\partial_y$ given by
$\frac t2(v-\alpha)z^{v-1}\mp\big(1+\frac t2(v+\alpha)\big)z^{v+1}$, the eigenvalue becomes
$\lambda_{n+r}/q_k=(1+(2+\delta(r-1))t)/(1-\delta)$ because $\delta n=q_k+2$, and the divided Laplace denominator
$(u-\delta s)(2+(u+\delta s)t)$ cancels against the $x$-derivative, so that a density coefficient $a_v$ at step $s$ contributes
$-a_v/(2(v+1-\delta s))$ to the stream offset $v+1$ and $ta_v/(2(2+(v-1+\delta s)t))$ to the offset $v-1$. Then
$\sigma_k=\sigma(1/q_k)$ for a rational function $\sigma(t)$ that is regular on $[0,1/q_{k_0}]$ and equals $\sigma_\infty$ at
$t=0$. Interval evaluation of this recursion on a binary partition of $[0,1/q_{k_0}]$, where a node is closed either by a
lower bound $|\sigma|\ge s$ on it or because it contains no point $1/q_k$ with integer $k\ge k_0$, gives an explicit lower bound
for $\inf_{k\ge k_0}|\sigma_k|$ from finitely many exact rational checks.

Corollary T_{9,2} (explicit profiles at $\delta=\frac49$, $c=\frac95$; PROVED: independent exact certificates, reviewed here,
with an independent exact reproduction here of the nonvanishing certificate and of the radius boxes). Let $Q=9$, $h=2$ and $f_1=\sin\theta+b\sin3\theta$,
so $B=4$, $\kappa_{9,2}=\frac{230}9$, $L=\frac92$ and $k_0=10$.
(a) $O_9=\mathcal P_9(b)/d_9$ with an integer polynomial $\mathcal P_9$ of degree 9 and content 1 (given in full in the
artifacts). $\mathcal P_9$ is irreducible over $\mathbb Q$ (modulo 19 and modulo 29 its factor degrees are $3,6$ and $1,8$,
with no common proper subset sum), and it has exactly five real roots,
$$b\approx0.0634372745,\ 0.1524299875,\ 0.2698308394,\ 0.4223764828,\ 1.8566753384.$$
For every such root and every real $\varepsilon\ne0$, $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_{Q,h}-a) and
(T_{Q,h}-b), so Theorem T_{Q,h} gives a uniquely tuned convergent pure power series at $c=\frac95$ on an exterior
$r>A^{9/4}$, with $\rho=r^{5/9}f_1+O(r^{1/9})$ and a convergent potential whose only logarithm is $\lambda\log r$.
Since $\mathcal P_9(0)\ne0$, $f_1=\sin\theta$ is obstructed at order 9 at $\delta=\frac49$ for every choice of constants.
(b) In increasing root order, $|\sigma_k(b_i)|\ge s_i$ for every $k\ge1$ with $s=(2^{-29},2^{-24},2^{-25},2^{-14},1)$. With
$a_i=\frac{133}{125},\frac{1153}{1000},\frac{127}{100},\frac{1423}{1000},\frac{2857}{1000}\ge1+|b_i|$ the box test passes at
$z_0=2^{-215},2^{-207},2^{-212},2^{-193},2^{-184}$ (maximal component ratios $0.824,0.873,0.792,0.817,0.842$) and fails at
$2z_0$. Hence the tuned series and all weighted derivatives converge on every exterior $r\ge R>R_i|\varepsilon|^{9/4}$ with
$$R_i=2^{1935/4},\ 2^{1863/4},\ 2^{477},\ 2^{1737/4},\ 2^{414},$$
and $r>2^{484}|\varepsilon|^{9/4}$ suffices for all five. These radii come from a crude majorant and are not estimates of the
true radii of convergence.
(c) (Exact infima and sharper radii; PROVED: complete proof here, independently confirmed by a separate exact computation
of the five minima and an exact identity for the generic response.) In
increasing root order, $\inf_{k\ge1}|\sigma_k(b_i)|$ is attained only at $k_i=7,4,13$ for $i=1,2,3$; for $i=4$ it equals
$|\sigma_\infty(b_4)|$ and is attained at no $k$; for $i=5$ it is attained only at $k_5=5$. The infima are
$8.446749852\cdot10^{-9}$, $4.351240063\cdot10^{-7}$, $2.356952307\cdot10^{-7}$, $3.967548192\cdot10^{-4}$ and $4114.009724$
(to the digits shown), and $|\sigma_k(b_i)|\ge s'_i$ for every $k\ge1$ with
$$s'=\Bigl(\tfrac{211}{25\cdot10^{9}},\ \tfrac{87}{2\cdot10^{8}},\ \tfrac{47}{2\cdot10^{8}},\ \tfrac{99}{250000},\ 4114\Bigr).$$
With the $a_i$ of (b) the box test passes at $z_0=2^{-211},2^{-201},2^{-206},2^{-187},2^{-160}$ (maximal component ratios
$0.753,0.948,0.801,0.983,0.839$) and fails at $2z_0$, so the conclusion of (b) holds with
$$R_i=2^{1899/4},\ 2^{1809/4},\ 2^{927/2},\ 2^{1683/4},\ 2^{360},$$
and $r>2^{475}|\varepsilon|^{9/4}$ suffices for all five.

Proof. Here $\deg_b\sigma_k\le9=\deg\mathcal P_9$, so the degree argument of Corollaries T_5, T_4 and T_6 is not available.
Since $\mathcal P_9$ is irreducible, $\sigma_k(b_i)=0$ at one real root forces $\mathcal P_9\mid\sigma_k$, so $\sigma_k$ would be a
rational multiple (possibly $0$) of $\mathcal P_9$. Two certificates exclude this for every $k\ge1$. (i) With $O_0$, $O_9$ the
constant and leading coefficients of $O_9(b)$, $a_k=\sigma_k(0)$ and $d_k=[b^9]\sigma_k$ (the responses of the single modes
$\sin\theta$ and $\sin3\theta$, by homogeneity), proportionality forces $D_k:=O_9a_k-O_0d_k=0$. The independent certificate
computes $a_k,d_k$ directly for $1\le k\le9$, as rational functions of $k$ for $k\ge10$ (equal to the direct values at
$k=10,11$), and shows $D_k\ne0$: the reduced numerator and denominator of $D(k)$ have degree 89, all coefficients of their
shifts to $k=24+t$ are nonnegative after one sign normalization with positive constant terms, and $10\le k\le23$ are
evaluated exactly. (ii) Independently, the program of this section reduces the full numerator $N(k,b)$ modulo the monic
$\mathcal P_9$ and finds that the common divisor in $\mathbb Q[k]$ of the coefficients of the remainder has no integer root
$\ge k_0$, that the denominator has no such root, and that $\sigma_k$ is nonzero and not divisible by $\mathcal P_9$ for
$1\le k\le k_0-1$; this test is an equivalence. Finally $\sigma_\infty$ is coprime to $\mathcal P_9$ (an exact Euclidean
remainder chain). By Corollary T_{Q,h}.4(c), $\inf_{k\ge1}|\sigma_k(b_i)|>0$ at all five roots. For (b), the independent
certificate evaluates $\sigma_k(b_i)$ directly for $1\le k\le16$ and covers $k\ge10$ by the compact recursion above, with
1772, 163, 757, 2007 and 567 closed nodes for the five roots, every accepted node stored as an exact dyadic midpoint and radius
and replayed in rational arithmetic. The boxes were checked in exact rational arithmetic by the independent program and,
from the same inputs $(a_i,s_i)$, by a second program here, with identical smallest passing exponents and ratios. $\square$

Proof of (c). For $1\le k\le9$, $\sigma_k(b)$ is computed exactly as a polynomial in $b$ by the direct recurrence. For
$k\ge k_0=10$ it is the generic rational function $N(k,b)/D(k)$ of (a)(ii), of degree 505 in $k$ in numerator and denominator.
Each root is enclosed in a rational isolating interval $I_i$ of width at most $10^{-30}$. Every evaluation below is an exact
rational interval evaluation over $I_i$ of one polynomial in $b$, formed before evaluation so that $b$ is not counted
twice. Let $\tau_i(b)=\pm\sigma_{k_i}(b)$ for $i\ne4$ and $\tau_4(b)=\pm\sigma_\infty(b)$, with the sign that makes it positive
on $I_i$, and let $\epsilon_i$ be the sign of $\sigma_\infty$ on $I_i$. Put $K_i=10$ for $i\ne3$ and $K_3=24$.
(1) Finite indices. For $1\le k<K_i$, $k\ne k_i$, the lower bound of $|\sigma_k|$ on $I_i$ exceeds the upper bound of
$\tau_i$ on $I_i$; for $10\le k\le23$ the exact values of $N(k,\cdot)/D(k)$ are used. The smallest such gaps are
$1.8\cdot10^{-10}$, $1.6\cdot10^{-7}$, $2.1\cdot10^{-6}$, $1.5\cdot10^{-3}$ and $4.2\cdot10^2$.
(2) Tail. After one sign normalization all 506 coefficients of $D(K_i+t)$ as a polynomial in $t$ are positive. Every
$t$-coefficient of $\epsilon_iN(K_i+t,b)-\tau_i(b)D(K_i+t)$ is positive on $I_i$, except for $i=4$ the top one, which vanishes
identically because $\epsilon_4\tau_4=\sigma_\infty$ is the ratio of the leading coefficients in $k$. Hence
$\epsilon_i\sigma_k(b_i)>\tau_i(b_i)$ for every integer $k\ge K_i$. At the third root the tail must start at $K_3=24$ because
$\sigma_k(b_3)<0<\sigma_\infty(b_3)$ for $10\le k\le12$.
By (1) and (2), $|\sigma_k(b_i)|>\tau_i(b_i)$ for all $k\ge1$ other than $k_i$ (for all $k\ge1$ when $i=4$), while
$|\sigma_k(b_4)|\to\tau_4(b_4)$. This proves the statements on the infima. Each $s'_i$ is a rational with 3 significant digits
below the lower endpoint of $\tau_i$ on $I_i$. The boxes are exact rational computations by the box program of (b). The
program that proves (1) and (2) also runs the box test, with the coarser bounds
$a=\frac{107}{100},\frac{29}{25},\frac{127}{100},\frac{143}{100},\frac{143}{50}$, and passes at
$z_0=2^{-211},2^{-202},2^{-206},2^{-188},2^{-160}$. $\square$

Numerical evidence (floating evaluation of the exact generic formula, $1\le k\le2000$). The minima of $|\sigma_k(b_i)|$ are
$8.45\cdot10^{-9}$ ($k=7$), $4.35\cdot10^{-7}$ ($k=4$), $2.36\cdot10^{-7}$ ($k=13$), $|\sigma_\infty(b_4)|=3.97\cdot10^{-4}$ (not
attained; $|\sigma_k(b_4)|$ decreases to it) and $4.11\cdot10^3$ ($k=5$), and $\sigma_\infty(b_i)\approx-1.772\cdot10^{-8}$,
$1.460\cdot10^{-6}$, $3.555\cdot10^{-5}$, $-3.968\cdot10^{-4}$, $6.114\cdot10^3$; so the bounds $s_i$ of (b) lie below the
infima by factors of about $4.5$, $7.3$, $7.9$, $6.5$ and $4.1\cdot10^3$ (the minima are exact infima by (c)). At the third
root the signs of $\sigma_1,\sigma_2,\sigma_3$ are $+,-,+$, $\sigma_k<0$ for $4\le k\le12$ ($\sigma_{12}\approx-2.377\cdot10^{-6}$)
and $\sigma_k>0$ for $k\ge13$ ($\sigma_{13}\approx2.357\cdot10^{-7}$; for $k\ge24$ this is part of (c)(2)): the rational
function $k\mapsto\sigma(k,b_3)$ has a real zero near $k\approx12.9$, and the integer minimum at $k=13$ is about 150 times
smaller than $|\sigma_\infty(b_3)|$. Exact
nonvanishing at every integer is part (a); the near-zero shows how close this profile is to the exceptional set of Theorem
T_{Q,h}.5, where some $\sigma_k$ vanishes on the compatibility hypersurface.

Theorem T_{Q,h}.5 (genericity when obstruction and response have equal degree; PROVED: independent proof, reviewed here).
Let $h\ge2$, $Q>2h$ coprime, $B\ge6$ even, and write normalized profiles $f(b,t)=\sin\theta+b\sin3\theta+\sum_{5\le j<B,\,j\text{ odd}}t_j\sin j\theta$.
Assume that $O_Q(b,0)$ has degree exactly $Q$ and is irreducible over $\mathbb Q$, and that for every $k\ge1$ and for
$k=\infty$, $\sigma_k(b,0)$ is not a rational multiple (including $0$) of $O_Q(b,0)$. Then the conclusions of Theorem T_Q.5 hold
on $\mathcal M=\{O_Q=0,\ \nabla O_Q\ne0\}$ with $\inf_{k\ge1}$, the tuned series being those of Theorem T_{Q,h}. At
$\delta=\frac49$ the hypotheses are exactly the certificates of Corollary T_{9,2}, so there the tuned convergent series exist on
an open dense subset of full measure of every regular component of the normalized compatibility hypersurface.

Proof. As Theorem T_Q.5, except at the step where $\deg\sigma_h<2Q$ was used. Total degree at most $Q$ makes the coefficient
of $b^Q$ in $O_Q$ a nonzero constant, so the monic multiple $P$ is irreducible in $\mathbb Q(t)[b]$ as before. Let $S$ be a
finite or limiting response, of total degree at most $Q$. If $P$ and $S$ had a common factor, then $P\mid S$; for
$\deg_bS<Q$ this gives $S=0$, and for $\deg_bS=Q$ it gives $S=C(t)P$ where $C(t)$ equals the coefficient of $b^Q$ in $S$, again a
rational constant by the degree bound. Either way $S(b,0)$ is a rational multiple of $O_Q(b,0)$, which is excluded. So every
resultant $\operatorname{Res}_b(P,S)$ is a nonzero polynomial in $t$, and the rest of the proof of Theorem T_Q.5 applies
unchanged. $\square$

Corollary T_{9,2}.C (a profile with Candidate 007's higher harmonics; PROVED: independent proof, reviewed here, with an
independent floating computation of the root and of the responses and an exact replay of the box here). Let
$a_1,a_3,\dots,a_{19}$ be the exact sine coefficients of Candidate 007's leading density profile (listed exactly in Section 8.5;
$a_1\approx18.5678$, $a_3/a_1\approx0.113493$), let $B=20$ and
$$f_1(\theta;b)=\sin\theta+b\sin3\theta+\sum_{j=5,7,\dots,19}\frac{a_j}{a_1}\sin j\theta .$$
(a) At $\delta=\frac49$ the first compatibility coefficient $O_9(b)=[\sin\theta]f_9$ is a polynomial of degree 9 in $b$,
irreducible over $\mathbb Q$ (irreducible modulo 229), with exactly seven real roots, all simple,
$$b\approx-0.152635,\ 0.0420057,\ 0.0893795,\ 0.174059,\ 0.293188,\ 0.467492,\ 2.374461 .$$
It does not vanish at $b=a_3/a_1$, so Candidate 007's own leading profile is obstructed at order 9 at $\delta=\frac49$ for
every choice of constants. The root nearest to $a_3/a_1$ is the third, $b_*\approx0.0893795255904838610$.
(b) At $b=b_*$, $|\sigma_k|>2^{-28}$ for every $k\ge1$, and $\|f_1\|_1<\frac{1139}{1000}$. With $\kappa_{9,2}=\frac{1150}9$ ($B=20$)
and $L=\frac92$ the box test of Theorem T_{Q,h} passes at $z_0=2^{-259}$ (largest component ratio $0.8206$) and fails at
$2z_0$. Hence for every real $\varepsilon\ne0$ the profile $\varepsilon f_1(\cdot;b_*)$ satisfies (T_{Q,h}-a) and (T_{Q,h}-b): its
uniquely tuned pure series at $c=\frac95$ converges with all weighted derivatives on every exterior
$r\ge R>2^{2331/4}|\varepsilon|^{9/4}$, solves the equations exactly there, and has a convergent potential whose only
logarithm is $\lambda\log r$ (Proposition T_{Q,h}.3). For $\varepsilon=a_1$ the leading profile is Candidate 007's exact leading
profile with only its $\sin3\theta$ coefficient changed, from $a_3\approx2.10732$ to $a_1b_*\approx1.65958$ (an $\ell^1$ change of
$0.44774$, about $21\%$ of that coefficient), and since $a_1^9<2^{38}$ the exterior $r>2^{593}$ suffices.

Proof. (a) is the exact computation of the independent proof: $O_9$ from the exact recurrence with the exact
coefficients $a_j$, its irreducibility modulo 229, and Sturm sequences for the real roots; at $b=a_3/a_1$ it reproduces the
earlier exact obstruction of Candidate 007's profile. (b) By Lemma T_{Q,h}.1 the responses use only $f_1,\dots,f_9$ and
$g_1,\dots,g_8$, which contain no free constant. The independent proof evaluates $\sigma_k(b_*)$ for $1\le k\le52$ by the full
Cartesian recurrence in ball arithmetic (768 bits) on an isolating interval of $b_*$. For $k\ge46$ the carrier
$q=4k-2\ge182$ exceeds $BQ=180$, so the compact tail recursion of this section applies with $t=1/q\in(0,\frac1{182}]$; a dyadic
tree on $[0,\frac1{182}]$, including $t=0$ (that is, $\sigma_\infty(b_*)\approx-4.84861\cdot10^{-8}$), has 406 leaves, of which 260
carry an interval lower bound above $2^{-28}$ and 146 contain no point $1/(4k-2)$, $k\ge46$, and all nodes are replayed in
exact rational arithmetic; the full and compact computations agree at $46\le k\le52$. The box is an exact rational
computation with $a=\frac{1139}{1000}$, $s=2^{-28}$. Independent checks here: a separate floating program (40 digits; the
Fourier form of the recurrence, no shared code) finds the root $b_*$ to 30 digits, $\|f_1\|_1=1.13844761693081\ldots$ and
$\sigma_1,\dots,\sigma_{52}$ in agreement to 8 digits. The box replayed in exact arithmetic by the program used for
Corollary T_{9,2}(b), with $B=20$, gives the same exponent and ratio. The constants $a_1^9<2^{38}$ and
$\|f_1\|_1<\frac{1139}{1000}$ were checked exactly. $\square$

Numerical evidence (floating, 40 digits, $1\le k\le60$ and $k=100,200,500,1000,2000,5000$). The smallest response is
$|\sigma_3(b_*)|=2.921\cdot10^{-8}$, about $7.8$ times $2^{-28}$. From $k=6$ on, $\sigma_k(b_*)$ is negative and increases in
modulus monotonically toward $\sigma_\infty(b_*)$ ($\sigma_6=-4.232\cdot10^{-8}$, $\sigma_{60}=-4.8155\cdot10^{-8}$,
$\sigma_{5000}=-4.84819\cdot10^{-8}$). The parameter is $c=\frac95$, not Candidate 007's stored $c\approx1.8103$.
(c) (Second root; PROVED: independent certificate by the method of (b).) At the second root $b_2\approx0.0420056861532581427$
of (a), the independent proof certifies $|\sigma_k|\ge2^{-21}$ for every $k\ge1$ by the same two parts (direct ball
evaluation for small $k$; compact tail tree with 108 accepted and 19 empty leaves, replayed exactly; $\sigma_\infty(b_2)\approx
-2.94016\cdot10^{-6}$). So $\varepsilon f_1(\cdot;b_2)$ also satisfies (T_{Q,h}-a) and (T_{Q,h}-b); its sin3 coefficient at
Candidate 007's amplitude is $a_1b_2\approx0.780$. With the original constants the box passes at $z_0=2^{-244}$ (restored radius
$2^{559}$); with Remark 4, $r>2^{287}$, and with Remark 5, $r>2^{59}$ at Candidate 007's amplitude. A separate floating program here (40 digits, Fourier form) finds the same root and $\min|\sigma_k|=2.78\cdot10^{-6}$ (at $k=7$) over
$k\le60$ and $k=100,200,500,1000,2000$, with $\sigma_{2000}=-2.93978\cdot10^{-6}$, consistent with the certified bound $2^{-21}\approx4.77\cdot10^{-7}$.
(d) (Fourth root; PROVED: independent certificate by the method of (b).) At the fourth root $b_4\approx0.174059472087551$ of
(a) the independent proof certifies $|\sigma_k|\ge2^{-23}$ for every $k\ge1$ (tail cover with 108 accepted and 19 empty
leaves; $\sigma_\infty(b_4)\approx1.38692\cdot10^{-6}$); with the original constants the restored radius is $2^{575}$, with
Remark 5 it is $2^{60}$.
(e) (First root; PROVED: independent certificate by the method of (b).) At the smallest root
$b_1\approx-0.152635000561798277$ of (a), $\|f_1\|_1<\frac{601}{500}$ and the independent proof certifies $|\sigma_k|\ge2^{-14}$ for
every $k\ge1$ (ball evaluation for $k\le52$; compact tail cover from $k=46$ with 260 accepted, 146 empty and 405 split cells,
replayed exactly; $\sigma_\infty(b_1)\approx1.43813\cdot10^{-3}$). With the original constants the box passes at $z_0=2^{-232}$
(restored radius $2^{532}$). With Remark 5 the box passes at $w_0=2^{-197}$ and fails at $2^{-196}$ (reproduced here,
together with the root enclosure and the initial norms), so the normalized radius is $2^{197/4}$ and, since
$a_1^{9/4}<2^{9.49}$, the exterior $r>2^{59}$ suffices at Candidate 007's amplitude. A separate floating program here (40 digits, Fourier form) finds the same root to 30 digits,
$\|f_1\|_1=1.2017030919\ldots$ and $\min|\sigma_k|=3.57\cdot10^{-4}$ (at $k=7$, about 5.9 times $2^{-14}$) over $k\le60$ and
$k=100,200,500,1000,2000$, with $\sigma_{2000}=1.43690\cdot10^{-3}$.
(f) (Fifth root; PROVED: independent certificate by the method of (b).) At the fifth root
$b_5\approx0.293187687845006959$ of (a) the independent proof certifies $|\sigma_k|\ge2^{-21}$ for every $k\ge1$ (ball evaluation
for small $k$; compact tail cover with 317 accepted, 279 empty and 595 split cells, replayed exactly;
$\sigma_\infty(b_5)\approx6.64046\cdot10^{-5}$). With the original constants the normalized radius is $2^{2241/4}$ and the
restored radius at Candidate 007's amplitude is $2^{570}$; with a certified prefix to order 36 (Remark 5(c)) the restored
radius is $2^{53}$. Its sin3 coefficient at that amplitude is $a_1b_5\approx5.444$.
(g) (Sixth root; PROVED: independent certificate by the method of (b).) At the sixth root $b_6\approx0.467492154252794$ of
(a) the independent proof certifies $|\sigma_k|>2^{-13}$ for every $k\ge1$ (ball evaluation for $k\le52$; compact tail
cover with 818 accepted, 720 empty and 1537 split cells, replayed exactly; $\sigma_\infty(b_6)\approx-1.56375\cdot10^{-3}$).
With the original constants and $\|f_1\|_1<\frac{1517}{1000}$ the box passes at $z_0=2^{-237}$, so the normalized radius is
$2^{2133/4}$ and the restored radius at Candidate 007's amplitude is $2^{543}$; with a certified prefix to order 36
(Remark 5(c)) the restored radius is $2^{51}$. Its sin3 coefficient at that amplitude is $a_1b_6\approx8.680$.
(h) (Seventh root; PROVED: independent certificate by the method of (b).) At the largest root
$b_7\approx2.37446144530777899$ of (a) the independent proof certifies $|\sigma_k|>1$ for every $k\ge1$ (52 direct finite
checks; compact tail cover with 260 accepted, 146 empty and 405 split cells, replayed exactly from rational addresses;
$\sigma_\infty(b_7)\approx61454.218$). With the original constants and $\|f_1\|_1<\frac{428}{125}$ the box passes at
$z_0=2^{-233}$, so the normalized radius is $2^{2097/4}$ and the restored radius at Candidate 007's amplitude is $2^{534}$;
with a certified prefix to order 36 (Remark 5(c)) the restored radius is $2^{54}$. Its sin3 coefficient at that amplitude
is $a_1b_7\approx44.09$. So all seven real roots of (a) carry convergent tuned series with all derivatives on
$r>2^{54}$ at Candidate 007's amplitude.

Corollary T_{10,3} (explicit profiles at $\delta=\frac35$, $c=\frac52$, the first parameter whose reduced numerator is odd and greater than one;
PROVED: independent exact certificate, reviewed here, with the polynomial, its irreducibility and its real roots computed
here and independently). Let $Q=10$, $h=3$ and $f_1=\sin\theta+b\sin3\theta$, so $B=4$, $\kappa_{10,3}=\frac{64}5$, $L=5$ and
$k_0=7$. The first resonance is at order 10 (stream mode $\sin4\theta$, obstruction mode $\sin3\theta$).
(a) $O_{10}=\mathcal P_{10}(b)/d_{10}$ with an integer polynomial $\mathcal P_{10}$ of degree 10 (given in full in the artifacts).
$\mathcal P_{10}$ is irreducible over $\mathbb Q$ (it is irreducible modulo 53, where its leading coefficient is a unit), and it
has exactly four real roots,
$$b\approx0.0659472179,\ 0.1093408010,\ 0.3505637599,\ 0.5942044255.$$
For every such root and every real $\varepsilon\ne0$, $f_1=\varepsilon(\sin\theta+b\sin3\theta)$ satisfies (T_{Q,h}-a) and
(T_{Q,h}-b), so Theorem T_{Q,h} gives a uniquely tuned convergent pure power series at $c=\frac52$ on an exterior $r>A^{5/3}$,
with $\rho=r^{2/5}f_1+O(r^{-1/5})$ and, by Proposition T_{Q,h}.3, a convergent potential series without any logarithm. Since
$\mathcal P_{10}(0)\ne0$, $f_1=\sin\theta$ is obstructed at order 10 at $\delta=\frac35$ for every choice of constants.

Proof. The responses $\sigma_k(b)$ and their limit $\sigma_\infty(b)$ have degree at most 10 in $b$, the degree of
$\mathcal P_{10}$, so the degree argument of Corollaries T_5, T_4 and T_6 is not available. If $\sigma_k(b_i)=0$ at a root, then
by irreducibility $\mathcal P_{10}\mid\sigma_k$, so $\sigma_k$ is a rational multiple of $O_{10}$ (possibly zero), and its
constant and $b^{10}$ coefficients are proportional to those of $O_{10}$:
$C(k):=O_{10,10}\,\sigma_{k,0}-O_{10,0}\,\sigma_{k,10}=0$. By homogeneity of degree 10 in $f_1$, $\sigma_{k,0}$ and $\sigma_{k,10}$ are
the responses of the single profiles $\sin\theta$ and $\sin3\theta$. For $k\ge7$ the two signed carriers $\pm(6k-2)$ cannot
interact (every density offset through ten orders has modulus at most $39<6k-2$), so a single rational function of $k$
gives the response on that tail. The independent certificate computes $C(k)$ exactly as a rational function of $k$
(numerator and denominator of degree 106), checks $k=1,\dots,9$ directly, shows that after the shift $k=10+x$ the
numerator and denominator have coefficients of one sign with nonzero constant terms, and that the limit $C(\infty)$ is a
nonzero rational. Hence no $\sigma_k$ and not $\sigma_\infty$ vanishes at any root, and since
$\sigma_k(b_i)\to\sigma_\infty(b_i)\ne0$ (Corollary T_{Q,h}.4), $\inf_k|\sigma_k(b_i)|>0$. The independent check also encloses the
tuned prefix to order 40 at the largest root in 2048-bit arithmetic, with every compatibility coordinate containing zero and
the common potential reconstructed with no logarithm. $\square$

(b) (Explicit radii; PROVED: independent certificates.) At the largest root $b_4$ every response satisfies
$|\sigma_k|>2^{-22}$ (direct evaluation for $k\le16$ and a compact interval cover of the tail $k\ge7$ with 935 accepted
leaves), and at the smallest root $b_1$, $|\sigma_k|>2^{-42}$ (cover with 2645 accepted leaves; $\sigma_\infty(b_1)\approx
-7.460\cdot10^{-11}$), at the second root $b_2$, $|\sigma_k|>2^{-42}$ (a cover of 17866 leaves, 7481 accepted intervals and
10385 intervals containing no integer), and at the third root $b_3$, $|\sigma_k|>2^{-31}$ (a cover of 2229 leaves, 935 accepted
and 1294 containing no integer). With these bounds, the sharp Poisson constant $L_Q=\frac{75}{29}$ and certified prefixes to order 40,
the resonance-block majorant of Remark 5 gives the exteriors $r>2^{65/3}|\varepsilon|^{5/3}$ at $b_4$,
$r>2^{139/6}|\varepsilon|^{5/3}$ at $b_1$, $r>2^{70/3}|\varepsilon|^{5/3}$ at $b_2$ and $r>2^{67/3}|\varepsilon|^{5/3}$ at $b_3$ (prefixes to orders 10, 20, 30, 40 give the exponents
$\frac{82}3,\frac{131}6,\frac{131}6,\frac{65}3$, then $\frac{169}6,\frac{139}6,\frac{139}6,\frac{139}6$, then $\frac{167}6,\frac{70}3,\frac{70}3,\frac{70}3$, then
$\frac{83}3,\frac{45}2,\frac{45}2,\frac{67}3$). Longer certified prefixes improve these: the prefix to order 100 gives $r>2^{139/6}|\varepsilon|^{5/3}$ at $b_2$, and
prefixes to order 300 with the tail-only response bounds of Remark 5(b') of Section 12.6 ($|\sigma_k|>2^{-37}$ at $b_1$ and
$|\sigma_k|>2^{-17}$ at $b_4$ for $k\ge30$, each by a complete interval cover of the tail) give $r>2^{133/6}|\varepsilon|^{5/3}$ at
$b_1$ and $r>2^{125/6}|\varepsilon|^{5/3}$ at $b_4$ (independent box certificates with separate exact replays). Tail bounds for $k\ge30$ at the other two roots,
$|\sigma_k|>2^{-40}$ at $b_2$ (a complete cover with 68 leaves) and $|\sigma_k|>2^{-27}$ at $b_3$ (23 leaves), give $r>2^{137/6}|\varepsilon|^{5/3}$
at $b_2$ and $r>2^{65/3}|\varepsilon|^{5/3}$ at $b_3$ with the same prefixes (independent certificates with exact and 1024-bit replays).
So the explicit exteriors are $2^{133/6}$, $2^{137/6}$, $2^{65/3}$ and $2^{125/6}$ times $|\varepsilon|^{5/3}$ at $b_1,\dots,b_4$, and
$r>2^{137/6}|\varepsilon|^{5/3}$ is a common sufficient exterior for the four roots. The tuned prefixes of all four roots to order 40 are
enclosed independently in 2048-bit arithmetic, with the common potential reconstructed and no logarithm needed.

(c) (Shape of the solutions; PROVED: independent proof, reviewed here and independently confirmed, with the explicit
inequalities checked independently in exact rational arithmetic.) The isolating intervals give $0<b_1<b_2<\frac19<b_3<b_4<1$.
Let $\varepsilon>0$. For each root there is $R$ such that for $r\ge R$: $\rho(r,\theta)>0$ for $0<\theta<\pi$ (and $\rho<0$ in the lower
half-plane); at $b_1,b_2$, $\partial_\theta\rho>0$ for $0<\theta<\frac\pi2$, so the angular maximum is on the axis $\theta=\frac\pi2$; at $b_3,b_4$,
$\rho(r,\cdot)$ has exactly one critical point in $(0,\frac\pi2)$, a strict maximum whose angle tends to
$\arcsin\sqrt{(1+3b)/(12b)}$ (about $44.3^\circ$ at $b_3$ and $38.7^\circ$ at $b_4$) as $r\to\infty$, and $\theta=\frac\pi2$ is a local angular
minimum. $R$ scales by $|\varepsilon|^{5/3}$, and $\varepsilon<0$ reverses the inequalities. Explicitly, $r\ge2^{70/3}\varepsilon^{5/3}$ suffices for
positivity and monotonicity at $b_1$ and for positivity and the unique first-quadrant maximum at $b_3$ and $b_4$, and
$r\ge2^{25}\varepsilon^{5/3}$ for positivity and monotonicity at $b_2$; so $r\ge2^{25}\varepsilon^{5/3}$ suffices for all four.

Proof. Since $\sin3\theta=\sin\theta(3-4\sin^2\theta)$, $f_1/(\varepsilon\sin\theta)=1+3b-4b\sin^2\theta\ge1-b>0$ and
$f_1'/(\varepsilon\cos\theta)=1+3b-12b\sin^2\theta$, which is at least $1-9b>0$ for $b<\frac19$. With $z=r^{-3/5}$,
$r^{-2/5}\rho/\varepsilon=\sum_{n\ge1}(\varepsilon z)^{n-1}\tilde f_n$ ($\tilde f_n$ the coefficients at unit amplitude,
$\tilde f_n=\sum_ma_{n,m}\sin m\theta$, $m$ odd, $m\le4n-1$), and $E_j(z)=\sum_{n\ge2}\sum_mm^j|a_{n,m}|z^{n-1}$ is finite and tends to
$0$ as $z\to0$ by the weighted convergence of Theorem T_{Q,h}. On $[0,\pi]$, $|\sin m\theta|\le m\sin\theta$, and for odd $m$ on
$[0,\frac\pi2]$, $|\cos m\theta|\le m\cos\theta$ (apply the first bound at $\frac\pi2-\theta$). So positivity holds once $E_1(\varepsilon z)<1-b$, and
monotonicity at $b_1,b_2$ once $E_2(\varepsilon z)<1-9b$. For $b>\frac19$ write $T=\sin^2\theta$ and, for $m=2k+1$,
$P_m(T)=(-1)^k[1+2\sum_{j=1}^kT_j(2T-1)]$ ($T_j$ Chebyshev), so that $P_m(\sin^2\theta)=\cos m\theta/\cos\theta$, $|P_m|\le m$ and
$|P_m'|\le4\sum_{j\le k}j^2=m(m^2-1)/6$ on $[0,1]$. Then $r^{-2/5}\partial_\theta\rho/\varepsilon=\cos\theta\,H(T)$ with
$|H(T)-(1+3b-12bT)|\le E_2$ and $|H'(T)+12b|\le E_4/6$. If $E_2<\min(1+3b,9b-1)$ and $E_4<72b$, then $H(0)>0>H(1)$ and
$H'<0$, so $H$ has exactly one zero $T_*$, with $|T_*-\frac{1+3b}{12b}|\le E_2/(12b)$. Reflection $\theta\mapsto\pi-\theta$ gives the rest.
For the explicit radii take the box of (b) at $w_0=2^{-q}$ with prefix bounds $d_n\ge n\|f_n\|_1$ and tail coordinates $x_r$,
$z=2^{-t}$ with $t>q/10$, and $\eta=z^{10}/w_0\le\frac12$; using $m\le4n$ and $k^j\eta^k\le c_j\eta$ for integers $k\ge1$ ($c_1=1$,
$c_2=\frac94$, $c_3=8$), $E_1,E_2,E_4$ are bounded by finite rational sums, and the required strict inequalities hold at $t=14$
($q=139$, prefix 20, at $b_1$; $q=130$, prefix 40, at $b_4$), and at $t=15$ at $b_2$ (prefix 20). $\square$

Numerical evidence (floating and 1024-bit ball arithmetic). At the largest root the first responses are
$\sigma_1\approx-1.5205\cdot10^{-3}$, $\sigma_2\approx1.5137\cdot10^{-2}$ and $\sigma_3\approx-3.5147\cdot10^{-5}$; the smallest
computed responses ($k\le29$) are about $1.2\cdot10^{-6}$ ($k=6$) at $b_4$, $2.2\cdot10^{-9}$ ($k=11$) at $b_3$, $1.8\cdot10^{-12}$
($k=4$) at $b_2$ and $1.6\cdot10^{-12}$ ($k=15$) at $b_1$. The tuned runs to order 300 give apparent exteriors $r>A^{5/3}$ of about
$1.1$ to $1.4$ ($b_4$), $0.25$ to $0.28$ ($b_3$), $0.06$ ($b_2$) and $0.065$ to $0.07$ ($b_1$), far inside the proved exteriors.

Proposition T_{Q,h}.6 (a support gap forces zero responses; PROVED: independent proof, reviewed here line by line, and
independently confirmed). Let $h\ge1$ and $Q\ge3$ be coprime with $2h<Q$, $\delta=\frac{2h}Q$, and let
$f_1$ be a nonzero real finite sine polynomial with odd frequencies. Let $\Lambda$ be its signed Fourier support (a finite
symmetric set of odd integers), $L=\max\{|m|:m\in\Lambda\}$, $r\Lambda$ the set of sums of $r$ elements of $\Lambda$ with
repetition, $E_r=\{-r,-r+2,\dots,r\}$, and $K=Q\Lambda+E_{Q-1}$. For $k$ in the resonant range ($k\ge1$ if $h\ge2$, $k\ge2$ if
$h=1$) let $\sigma_k$ be the response of Section 12.5 ($h=1$) or of this section ($h\ge2$). Then:
(a) $\sigma_k\ne0$ is possible only if $2h-1\in K$ or $4hk+2h-5\in K$.
(b) If $2h-1\notin K$, then $\sigma_k=0$ for every $k>\frac{QL+Q-2h+4}{4h}$ in the resonant range, so the response hypothesis
(T_{Q,h}-b), or its analogue in Theorem T_Q for $h=1$, fails for $f_1$ and for every nonzero multiple of it.
(c) Let $Q$ be odd and let the positive frequencies of $f_1$ lie in $[M-W,M+W]$ with $M$ odd, $W$ even and $0\le W<M$. If
$M>Q(W+1)+2h-2$, then $2h-1\notin K$. If $h\ge2$ and $M>Q(W+1)+2h-4$, the first compatibility condition $O_Q(f_1)=0$ holds
automatically.
(d) If $Q$ is even, $2h-1\in K$ for every nonempty $\Lambda$, so (b) never applies. This says nothing about whether the
responses vanish at even $Q$.

Proof. For $1\le r\le Q$, $\operatorname{supp}f_r\subset r\Lambda+E_{r-1}$, and $\operatorname{supp}g_r\subset r\Lambda+E_r$ for
$r<Q$: the right side of (T2) multiplies by $\cos\theta$ or $\sin\theta$ and differentiates, so it shifts frequencies by
$\pm1$, and a nonresonant inverse changes coefficients but not frequencies; a product in (T1) with $i+j=r$ has support in
$i\Lambda+E_i+j\Lambda+E_{j-1}=r\Lambda+E_{r-1}$, since $E_a+E_b=E_{a+b}$; difference frequencies are included because all
these sets are symmetric. The density $f_Q$ is formed before its possibly resonant inverse, so no compatibility is used.
At $n=kQ$ the response recursion of Lemma T_{Q,h}.1 (Lemma T_Q.1 for $h=1$) has the direct term $T(e_k,f_r)$ and terms
built from $\varphi_a$, $a<r$, and its nonresonant inverse with the low fields; by the same induction
$\operatorname{supp}\varphi_r\subset\{-q_k,q_k\}+r\Lambda+E_{r-1}$. The target mode $2h(k+1)-3=q_k+2h-1$ of $\varphi_Q$ is
reached from $q_k$ only if $2h-1\in K$ and from $-q_k$ only if $2q_k+2h-1=4hk+2h-5\in K$; the negative target is the mirror
case. This proves (a). Every element of $K$ has modulus at most $QL+Q-1$, so the second alternative is impossible once
$4hk+2h-5>QL+Q-1$, which is (b). For (c), a sum of $Q$ signed frequencies is $Ms+e$ with $s$ odd and $|e|\le QW$, so every
element of $K$ has modulus at least $M-QW-Q+1$; this exceeds $2h-1$ under the first inequality, and exceeds the first
obstruction mode $2h-3$ under the second. For (d), $Q/2$ cancelling pairs put $0$ in $Q\Lambda$, and the odd number
$2h-1\le Q-3$ lies in $E_{Q-1}$. $\square$

Examples (reviewed here). At $\delta=\frac49$ ($Q=9$, $h=2$): for $f_1=\sin M\theta$, $M$ odd, (c) gives automatic first
compatibility for $M\ge11$ and $2h-1\notin K$ for $M\ge13$. For $M=13$ the possibly nonzero responses are
$k\in\{1,2,4,5,6,8,9,11,12,14,15\}$ (the values with $8k-1\in K$), so $\sigma_3=0$ and $\sigma_k=0$ for $k\ge16$. Every profile
supported on $\sin31\theta,\sin33\theta,\sin35\theta$ ($M=33$, $W=2$) is compatible at order 9 and has $\sigma_k=0$ for $k\ge41$.
For $\sin11\theta$ the offset $3$ lies in $K$, and indeed $\sigma_1\ne0$ (below). A zero response does not by itself obstruct
the series: if $R_k=0$ as well, $H_{kQ}$ is free; the proposition only removes the uniqueness and the uniform lower bound
used by Theorem T_{Q,h}.

Finite exact computations at $\delta=\frac49$ (exact rational arithmetic, all resonant stream constants free; finite exact
facts, not general theorems). For $f_1=\sin13\theta$ the responses $\sigma_1,\sigma_2$ are nonzero, so $H_9$ and $H_{18}$ are
uniquely fixed by orders 18 and 27; then $\sigma_3=0$ exactly and $R_3=0.0309513358717254451\ldots\ne0$, so every pure series
with this profile (or a nonzero multiple of it) is obstructed at order 36. For $f_1=\sin15\theta$, $\sigma_1,\sigma_2,\sigma_3\ne0$,
$\sigma_4=0$ exactly and $R_4=3.7559105420448248\ldots\ne0$, so every pure series is obstructed at order 45. These were obtained
with the independent Cartesian program. A separate exact program in the polar Fourier form of the recursion (tuning
each constant from the two runs $H_{kQ}=0,1$ and recomputing every tuned block directly) reproduces the $\sin13\theta$ result:
$R_1\approx2.6661\cdot10^{-5}$, $\sigma_1\approx-5.4900\cdot10^{-2}$, $\sigma_2\approx58.923$, $\sigma_3=0$ exactly and $R_3$ the same
nonzero rational (numerator of 2282 digits; the displayed values and digit counts were audited independently). The same
program gives, for $f_1=\sin11\theta$, $\sigma_1\approx0.17640$, $\sigma_2\approx8.7815$ and $\sigma_3\approx0.12419$, all nonzero, so
$H_9,H_{18},H_{27}$ are uniquely fixed and the tuned pure series exists through order 36 (each tuned block recomputed
directly; finite exact computation, single program); Corollary T_{Q,h}.9 below proves that every response is bounded away
from zero and that the tuned series converges. For $f_1=\sin15\theta$ the exact polar run gives $H_9\approx-1.1047456\cdot10^{-3}$ and
$H_{18}\approx2.0547660\cdot10^{-5}$, agreeing with the Cartesian values, but each block costs about 37 times the previous one, so
it was stopped at order 27. The same continuation was then carried out in the prime fields $\mathbb F_p$, $p=2^{61}-1$ and
$p=4611686018427387847$: every divisor (Poisson divisors, $\lambda_n$, $2$ and the responses used for tuning) is checked to be a
unit mod $p$, so every residue is the reduction of the corresponding exact rational. At both primes the eleven residues of
$R_k,\sigma_k$ ($k\le4$) and $H_{9k}$ ($k\le3$) equal those of the exact Cartesian rationals; the residues of $\sigma_1,\sigma_2,\sigma_3$
and $R_4$ are nonzero, and $\sigma_4\equiv0$. Since $\sigma_4=0$ exactly by Proposition T_{Q,h}.6(a) ($K=9\{\pm15\}+E_8$ contains
neither $3$ nor $8\cdot4-1=31$), and a nonzero residue proves $R_4\ne0$, this is an independent proof of the order-45 obstruction
for $\sin15\theta$ (39.6 s per prime). It was independently confirmed: two separate modular replays agree with the eleven
reductions of the exact Cartesian rationals at each modulus, and every division checks $a\cdot a^{-1}=1$, so the argument does not
even need the moduli to be prime (PROVED). Logarithmic series and
additional exponent channels are outside the claim.

Proposition T_{9,2}.7 (a generic obstruction at order 18 on high-harmonic lattices; PROVED: independent proof, reviewed
here, with the recorded exact single-mode witnesses replayed independently). Let
$\delta=\frac49$, $M\in\{17,19\}$, $J$ a finite set of positive odd integers containing $1$, and
$f_1=\sum_{j\in J}a_j\sin(jM\theta)$, $a\in\mathbb R^J$. There is a nonzero homogeneous rational polynomial $R_J$ of degree 18
such that every pure density and stream series with this leading profile requires $R_J(a)=0$, whatever the constant $H_9$.
So the profiles admitting a pure continuation are contained in a closed nowhere dense null subset of $\mathbb R^J$
(whether the set of such profiles is itself closed is not decided), although the first compatibility condition at order 9
holds for every $a$.

Proof. Every element of $\Lambda$ is an odd multiple of $M$, so every element of $K=9\Lambda+E_8$ has modulus at least
$M-8\ge9$. Hence $O_9=0$ identically (mode $1$), and the response at order 18 (target mode $5$ from the carriers $\pm2$, needing
$3$ or $7$ in $K$) is identically zero by Proposition T_{Q,h}.6(a). With $H_9=0$ every coefficient through order 18 is a
polynomial in $a$, homogeneous of degree $n$ at order $n$, and $R_J$ is the $\sin5\theta$ coefficient of $f_{18}$; it is the
obstruction for every $H_9$. At $a=e_1$ the profile is $\sin M\theta$, for which the exact recorded value is nonzero
(about $5.35033\cdot10^{-6}$ for $M=17$ and $3.34765\cdot10^{-6}$ for $M=19$). A nonzero real polynomial has a closed zero set
with empty interior and Lebesgue measure zero. $\square$

The general form of the support step: for odd $Q$, $h\ge2$ and a lattice of odd multiples of $M$ with $M>Q+6h-6$, the first
compatibility and the response at the second resonance vanish identically, so a nonzero single-mode obstruction at order
$2Q$ gives a generic obstruction at order $2Q$ on every such lattice. These high-harmonic families have zero $\sin\theta$ coefficient, so
they lie outside the normalized profile space $\sin\theta+b\sin3\theta+\dots$ of Theorem T_{Q,h}.5, and there is no conflict
with that theorem.

Proposition T_{Q,h}.8 (odd degree forces real compatible profiles; PROVED: proof here and an independent proof, compared
here, independently confirmed). Let $h\ge2$
and $Q>2h$ be coprime with $Q$ odd; equivalently, $\delta=\frac{2h}Q$ is a reduced fraction whose numerator is even and at
least $4$. Let $V$ be a real linear space of real finite sine polynomials with odd frequencies, of dimension $d\ge2$.
(a) On $V$ the first obstruction $O_Q$ and every response $\sigma_k$ ($k\ge1$) are real homogeneous polynomials of degree
$Q$ in the coordinates (possibly identically zero), so $O_Q(-f)=-O_Q(f)$ and $\sigma_k(-f)=-\sigma_k(f)$.
(b) Every two-dimensional subspace of $V$ contains a nonzero profile with $O_Q(f)=0$. If $O_Q$ is not identically zero on
$V$, the open cones $\{O_Q>0\}$ and $\{O_Q<0\}$ are both nonempty and are exchanged by $f\mapsto-f$.
(c) For the normalized profiles $f(b,t)=\sin\theta+b\sin3\theta+\sum_{5\le j<B,\,j\text{ odd}}t_j\sin j\theta$ of Theorem
T_{Q,h}.5 and any fixed real $t$, $b\mapsto O_Q(f(b,t))$ is a polynomial of degree at most $Q$ whose coefficient of $b^Q$ is
$O_Q(\sin3\theta)$. If $O_Q(\sin3\theta)\ne0$ it has a real root for every $t$; if $O_Q(\sin3\theta)=0$, then $\sin3\theta$
itself is compatible.
(d) Under the hypotheses of Theorem T_{Q,h}.5 (with this $Q$ odd) the regular set $\mathcal M$ is nonempty. Hence its open
dense subset of profiles with convergent tuned pure series is nonempty: at such a parameter the algebraic hypotheses of
Theorem T_{Q,h}.5 already give a convergent tuned pure series, with no separate search for real roots.

Proof. For $h\ge2$ the first free constant is $H_Q$ in $g_Q$ (Lemma T_{Q,h}.1), and every inverse below order $Q$ is the
unique nonresonant one, linear in its input. By induction on (T1), (T2), $f_n$ and $g_n$ are homogeneous of degree $n$ in the
coefficients of $f_1$ for $n\le Q$ and $n\le Q-1$ respectively, with rational coefficients. So $O_Q$, the coefficient of
$\sin((2h-3)\theta)$ in $f_Q$, is a form of degree $Q$; the responses $\sigma_k$ are forms of degree $Q$ by Section 12.6. As
$Q$ is odd, both are odd functions, which is (a). For (b), let $W\subset V$ have dimension $2$ and let $S$ be a circle in $W$
centered at $0$. If $O_Q$ vanishes at some $v\in S$ we are done. Otherwise $O_Q(v)$ and $O_Q(-v)=-O_Q(v)$ have opposite
signs, $S$ is connected, and the intermediate value theorem on an arc of $S$ from $v$ to $-v$ gives a zero on $S$, a nonzero
profile. The second sentence of (b) follows from oddness. For (c), homogeneity gives
$O_Q(f(b,t))=b^QO_Q(\sin3\theta+b^{-1}(\sin\theta+\sum t_j\sin j\theta))$ for $b\ne0$, which identifies the coefficient of $b^Q$; a
real polynomial of odd degree has a real root. For (d), the hypotheses of Theorem T_{Q,h}.5 say that $O_Q(b,0)$ has degree
exactly $Q$ and is irreducible over $\mathbb Q$. A real polynomial of odd degree has a real root $b_0$. An irreducible
polynomial over $\mathbb Q$ has no repeated complex root, so $\partial_bO_Q(b_0,0)\ne0$ and $(b_0,0)\in\mathcal M$. Theorem
T_{Q,h}.5 makes its good set open and dense in the component of $\mathcal M$ through $(b_0,0)$, so that set is nonempty.
$\square$

Scope. The argument uses only the parity of the degree. It gives nothing for $h=1$, where the first resonance is at $2Q$
and $O_{2Q}$ has even degree $2Q$, or for even $Q$ (odd $h\ge3$, such as $\delta=\frac35$ with $Q=10$, and Candidate 007's stored value, whose reduced
numerator is odd), where the degree $Q$ is even; at those parameters a two-dimensional family can have no real compatible profile without contradicting anything
proved here. It gives no information about the response hypothesis (T_{Q,h}-b), which remains the open part of
Theorem T_{Q,h} at a general even-numerator rational: Proposition T_{Q,h}.6 shows that responses can vanish identically
on support-gap families. In one-dimensional families $\{\varepsilon f\}$ it says nothing, since there $O_Q(\varepsilon
f)=\varepsilon^QO_Q(f)$. Consistent examples: at $\delta=\frac49$ the degree-9 polynomial $O_9(b,0)$ of Corollary T_{9,2} has
real roots, and at $\delta=\frac47$ the degree-7 first-obstruction polynomial of $\sin\theta+b\sin3\theta$ is irreducible over
$\mathbb Q$ (it is irreducible modulo 23) and has three real roots, near $0.23215$, $0.46595$ and $2.61445$ (Corollary T_{7,2},
where all three give convergent tuned series).

Corollary T_{7,2} (explicit profiles at $\delta=\frac47$, $c=\frac73$; PROVED: independent exact certificates, reviewed here,
with the polynomial, its irreducibility, its real roots and the nonvanishing of every response also computed here by a
separate exact program). Let $Q=7$, $h=2$ and $f_1=\sin\theta+b\sin3\theta$, so $B=4$, $L_7=\frac{147}{80}$ and
$\kappa_*=\frac{48}7$ (Remark 4). The first resonance is at order 7 (stream mode $\sin2\theta$, obstruction mode $\sin\theta$).
(a) $O_7=\mathcal P_7(b)/d_7$ with an integer polynomial $\mathcal P_7$ of degree 7 (given in full in the artifacts). It is
irreducible over $\mathbb Q$ (irreducible modulo 23, where its leading coefficient is a unit) and has exactly three real roots
(Sturm sequences, here and independently),
$$b_1\approx0.2321514760,\qquad b_2\approx0.4659545905,\qquad b_3\approx2.6144481765,$$
as Proposition T_{Q,h}.8(c) requires at least one. Since $\mathcal P_7(0)\ne0$, $\sin\theta$ is obstructed at order 7.
(b) For each root, $\inf_{k\ge1}|\sigma_k(b_i)|>0$. Independent certificate: $|\sigma_k|>2^{-24}$, $2^{-21}$ and $8$ at
$b_1,b_2,b_3$ for every $k\ge1$ (16 finite responses evaluated directly and a complete interval cover of the tail with 13
singleton and 3 Taylor leaves at each root, every leaf replayed at 1024 bits, and 306 coefficients compared with exact
polynomial formulas). Exact certificate here: the response is a single rational function of $k$ for $k\ge8$, which agrees
with direct exact values at $k=8,\dots,13$; reduced modulo $\mathcal P_7$, its coefficients have a common factor of degree 207 in
$k$ whose rational roots are not integers, $\sigma_\infty$ has degree 7 and is not divisible by $\mathcal P_7$, and so by
irreducibility no $\sigma_k$ and not $\sigma_\infty$ vanishes at a root. The exact infima are attained at $k=4,8,6$ (also
certified independently: fixed thresholds, full responses below $k=16,24,16$, Taylor covers of the tails and a 1536-bit replay), with values
about $3.476\cdot10^{-7}$, $2.189\cdot10^{-6}$ and $47.28$ ($\sigma_\infty\approx1.380\cdot10^{-6}$, $8.944\cdot10^{-5}$, $-49.95$).
(c) Hence, for every real $\varepsilon\ne0$ and each root, $f_1=\varepsilon(\sin\theta+b_i\sin3\theta)$ has a uniquely tuned pure
series at $c=\frac73$ that converges with all derivatives, with $\rho=r^{3/7}f_1+O(r^{-1/7})$ and a convergent potential series
with at most the logarithm $\lambda\log r$ of Proposition T_{Q,h}.3. The resonance-block majorant of Remark 5 with the
constants of Remark 4 and certified prefixes to order 7, with the response lower bounds $\frac{347}{10^9}$, $\frac{109}{5\cdot10^7}$
and $\frac{1182}{25}$ below the minima of (b), gives the exteriors $r>2^{27}$, $2^{117/4}$ and $2^{109/4}$ times
$|\varepsilon|^{7/4}$ at $b_1,b_2,b_3$ (independent exact boxes at $q=108,117,109$ with fresh replays; before the minima were
used, $2^{113/4}$, $2^{121/4}$, $2^{57/2}$), so $r>2^{117/4}|\varepsilon|^{7/4}$ is a common sufficient exterior. $\square$

Corollary T_{Q,h}.9 (one high harmonic and its lattices; PROVED). Let $h\ge2$ and $Q>2h$ be coprime with $Q$ odd, $\delta=\frac{2h}Q$, $c=\frac Q{Q-2h}$ and
$M=Q+2h-2$ (odd). Let $J$ be a finite set of positive odd integers containing $1$ and $f_1(\cdot;a)=\sum_{j\in J}a_j\sin(Mj\theta)$,
$a\in\mathbb R^J$; $e_1$ denotes the vector with $a_1=1$ and all other $a_j=0$, so $f_1(\cdot;e_1)=\sin M\theta$.
(a) (Automatic first compatibility; PROVED: independent proof, reviewed here.) $O_Q(f_1(\cdot;a))=0$ for every $a$, real or
complex. Among single harmonics $\sin M'\theta$, $M=Q+2h-2$ is the only frequency for which the first condition is forced
by the support bound of Proposition T_{Q,h}.6 and the same support bound does not force the responses to vanish for all
large $k$ (precisely: $2h-3\notin K$ if and only if $M'>Q+2h-4$, and $2h-1\in K$ if and only if $M'\le Q+2h-2$). This classifies
the support test only: a smaller $M'$ may still have a first coefficient that vanishes by cancellation.
(b) (Open lattice families; PROVED: independent proof, reviewed here.) Suppose $s_0=\inf_{k\ge1}|\sigma_k(e_1)|>0$. Then there are
an open neighbourhood $U$ of $e_1$ in $\mathbb R^J$ and $R<\infty$ such that for every $a\in U$ the tuned pure series with leading
profile $f_1(\cdot;a)$ is unique and converges with all weighted derivatives on $r\ge R$, its coefficients and sums depend
real-analytically on $a$, and the density takes both signs on every circle $r\ge R$. The potential is a pure power series if
$h\ge3$ and has at most one term $\lambda\log r$ if $h=2$. The neighbourhood and $R$ are qualitative, and the statement is for
fixed $\delta$ and fixed $J$, not openness among all odd sine profiles or in $\delta$.
(c) (Certified centers.) For $f_1=\varepsilon\sin M\theta$, $\varepsilon\ne0$ real, the response hypothesis holds and Theorem T_{Q,h}
gives a uniquely tuned pure series converging with all derivatives on the following exteriors. All numerical response
bounds below are for $\varepsilon=1$; for general $\varepsilon$ multiply them by $|\varepsilon|^Q$, since $\sigma_k(\varepsilon f)=\varepsilon^Q\sigma_k(f)$
(the radii already contain the amplitude factor).
- $\delta=\frac49$, $c=\frac95$, $f_1=\varepsilon\sin11\theta$: $|\sigma_k|>2^{-29}$ for every $k\ge1$ (27 responses evaluated directly
and a complete cover of the tail with 25 Taylor and 99 singleton leaves), and the exact majorant box with a certified prefix to
order 9 at $w=z^9=2^{-213}$ gives $r>2^{213/4}|\varepsilon|^{9/4}$ (PROVED: independent certificate with a 1024-bit replay, and
2029 low-order coefficients compared with a separately written exact Cartesian recursion; specialization reviewed here);
- $\delta=\frac47$, $c=\frac73$, $f_1=\varepsilon\sin9\theta$: $B=10$, $L_7=\frac{147}{80}$, $\kappa_*=\frac{120}7$, $|\sigma_k|>2^{-25}$ (17 direct
responses and 40 leaves), box exponent $q=147$, so $r>2^{147/4}|\varepsilon|^{7/4}$ (PROVED: independent certificate and
replay, specialization reviewed here). The responses tend to
$$\lim_{k\to\infty}\sigma_k=S(0)=\frac{82651586141768218752124086777}{415161675019179052311193843662848000}\approx1.99083\cdot10^{-7}$$
for $\varepsilon=1$ (PROVED: the compact response $\sigma_k=S(\frac1{4k-2})$ is a rational function of $t$ with nonzero
denominators near $t=0$, and $S(0)$ is computed exactly by the limiting recurrence in which the high carrier has the
derivatives $\mp z$; confirmed against a separate 1536-bit evaluation of the compact formula, reviewed here). It is
about 6.7 times the uniform bound $2^{-25}$, and much smaller than the computed responses at $k\le42$, which decrease
like $1.04\cdot10^{-3}/k$ (NUMERICAL EVIDENCE);
- $\delta=\frac45$, $c=5$, $f_1=\varepsilon\sin7\theta$: $B=8$, $L_5=\frac{75}{56}$, $\kappa_*=\frac{24}5$, $|\sigma_k|>2^{-20}$ (10 direct
responses, 11 singleton and 2 Taylor leaves), $q=80$, so $r>2^{20}|\varepsilon|^{5/4}$ (PROVED: the certificate
arithmetic is independently replayed, the specialization is reviewed here, and the first five responses and $H_5,\dots,H_{20}$
agree with an independent 1024-bit Cartesian computation). The exact polar
program of this section gives $\sigma_1,\dots,\sigma_5\approx1.9470\cdot10^{-5}$, $4.9233\cdot10^{-4}$, $-2.6233\cdot10^{-3}$,
$7.4295\cdot10^{-4}$, $3.8906\cdot10^{-4}$ (finite exact values);
- $\delta=\frac6{13}$, $c=\frac{13}7$, $f_1=\varepsilon\sin17\theta$ ($h=3$): $B=18$, $L_{13}=\frac{507}{152}$, $\kappa_*=\frac{7938}{169}$, $|\sigma_k|>2^{-45}$ for every
$k\ge1$ (39 direct responses; the compact formula holds for $k\ge40$, and the tail $t=\frac1{6k-2}\in[0,\frac1{238}]$ is covered by 22
singleton and 16 degree-five Taylor leaves), and the exact majorant box with a prefix through order 13 at $w=z^{13}=r^{-6}=2^{-334}$
gives $r>2^{167/3}|\varepsilon|^{13/6}$ (PROVED: independent certificate with a 1024-bit replay, 6209 low-order coefficients compared
with a separately written exact Cartesian recursion and 78 exact scalar identities; specialization reviewed here). The
minimum of $|\sigma_k|$ over the integers $k\ge1$ is attained only at $k=2380$, with $|\sigma_{2380}|\approx2.7706\cdot10^{-12}$, so
$|\sigma_k|\ge|\sigma_{2380}|>\frac{277}{10^{14}}$ for every $k\ge1$ (PROVED: each of the 39 direct responses and each of the 38 leaves
of the cover, including the closed leaf that touches $t=0$, is compared strictly in 1536-bit arithmetic with a rational
upper bound for $|\sigma_{2380}|$; independently confirmed). With this constant the same box passes at $q=320$, so the
series converges on $r>2^{160/3}|\varepsilon|^{13/6}$ (PROVED). Since
$h=3$, no exceptional potential exponent falls at an integer order, so the density, the stream and the potential are pure
power series.
By (b), each certified center carries an open lattice family of convergent tuned series. These are the first explicit
convergent profiles with zero $\sin\theta$ coefficient (they lie outside the normalized profile space of Theorem
T_{Q,h}.5), and each solution changes sign on every circle of its exterior.
(d) (The potential and a necessary radius at $\delta=\frac49$; PROVED: independent proof and directed-arithmetic constants,
reviewed here.) For $f_1=\varepsilon\sin11\theta$ the common potential needs the term $\varepsilon^9\lambda\log r$ with an exact
$\lambda>0$ at unit amplitude, so no pure-power potential exists, and by continuity the logarithm persists on a neighbourhood
in (b). The top-mode argument of Remark 3 (here $B=12$, $R_H=1.351842750\ldots$) shows that uniform termwise $C^2$
convergence on $r\ge R$ requires $R>0.507476|\varepsilon|^{9/4}$. So the true exterior of convergence of this series lies
between $0.507476|\varepsilon|^{9/4}$ and $2^{213/4}|\varepsilon|^{9/4}$.
(e) (A real zero between consecutive indices; PROVED: independent certificates, reviewed here.) For
$f_1=\sin11\theta$ the compact response formula, a rational function of $t=1/(4k-2)$ valid for $k\ge28$, has a zero at a real
index strictly between $513$ and $514$: in directed 1024-bit arithmetic it is about $-1.3355\cdot10^{-8}$ at $t=\frac1{2050}$ and
$+8.0772\cdot10^{-9}$ at $t=\frac1{2054}$, with every denominator nonzero on the interval between. The zero in this interval is
unique: a degree-three Taylor enclosure gives $S'(t)\in-0.022561\pm6.5\cdot10^{-7}$ on all of $[\frac1{2054},\frac1{2050}]$ (PROVED:
independent certificate with a 1536-bit replay, argument reviewed here). Nothing is claimed about real zeros outside this
interval.
So the bound $2^{-29}$ of (c) holds at the integers only; no lower bound on the real interpolation could replace the discrete
cover there.
(e') (The same phenomenon at $\delta=\frac6{13}$; PROVED: independent certificates, the specialization reviewed here.) For
$f_1=\sin17\theta$ at $\delta=\frac6{13}$ ($h=3$, $B=18$) the compact response formula, a rational function of $t=1/(6k-2)$, has
exactly one real zero with $t\in[\frac1{14278},\frac1{14272}]$, that is, at a real index strictly between $2379$ and $2380$: in directed
1024-bit arithmetic (replayed at 1536 bits) it is about $+2.7706\cdot10^{-12}$ at $t=\frac1{14278}$ and $-1.1292\cdot10^{-11}$ at
$t=\frac1{14272}$, and a degree-three Taylor enclosure gives $S'(t)\in-4.77591\cdot10^{-4}\pm4.65\cdot10^{-10}$ on the whole interval.
The denominators are nonzero there: the frequencies of the response recursion satisfy $|v|\le20r-1$, so
$|v-1+\frac{6r}{13}|\le\frac{3192}{13}$ for $r\le12$, and $2-\frac{3192}{13\cdot14272}>0$. The integer responses $\sigma_{2379}$ and
$\sigma_{2380}$ are nonzero with opposite signs, and every integer response satisfies $|\sigma_k|\ge|\sigma_{2380}|>\frac{277}{10^{14}}$ by (c).
(f) (Necessary radii at the other two centers; PROVED: independent proof, the specialization reviewed here, and the
constants confirmed in independent directed arithmetic.) For $f_1=\varepsilon\sin7\theta$ at $\delta=\frac45$ ($B=8$,
$a=\frac5{18}$, $b=\frac{35}{18}$, $4d=16$) uniform termwise $C^2$ convergence on $r\ge R$ requires $R>0.0902973|\varepsilon|^{5/4}$, and for
$f_1=\varepsilon\sin9\theta$ at $\delta=\frac47$ ($B=10$, $a=\frac7{33}$, $b=\frac{21}{11}$, $4d=\frac{16}3$) it requires $R>0.2365977|\varepsilon|^{7/4}$.
So the true exteriors lie between $0.0902973|\varepsilon|^{5/4}$ and $2^{20}|\varepsilon|^{5/4}$, and between $0.2365977|\varepsilon|^{7/4}$ and
$2^{147/4}|\varepsilon|^{7/4}$ (the exact thresholds are $0.0902973480\ldots$ and $0.2365977527\ldots$). The same formula at
$\delta=\frac6{13}$, $M=17$ ($h=3$, $B=18$) gives the necessary bound $R>0.4954372|\varepsilon|^{13/6}$ for the tuned $\sin17\theta$
series of (c) (exact threshold $0.49543724057\ldots$), so its true exterior lies between $0.4954372|\varepsilon|^{13/6}$ and
$2^{160/3}|\varepsilon|^{13/6}$.
(g) (Mandatory potential logarithms at $\delta=\frac45$ and $\frac47$; PROVED: independent proof with two exact
implementations, reviewed here.) For $f_1=\varepsilon\sin7\theta$ at $\delta=\frac45$ ($Q=5$) and $f_1=\varepsilon\sin9\theta$ at
$\delta=\frac47$ ($Q=7$) the common potential of the tuned series of (c) needs the term $\varepsilon^Q\lambda_Q\log r$, with the exact
rationals $\lambda_5=-8.44351932666868990\ldots\cdot10^{-4}$ and $\lambda_7=+1.25629761803687665\ldots\cdot10^{-4}$ at unit amplitude. So
none of the three certified centers of (c) with $h=2$ has a pure-power potential, and by continuity the logarithm persists on a
neighbourhood in (b). The density and the stream remain pure power series.

Proof. (a) For $n\le Q$ the signed supports satisfy $\operatorname{supp}f_n\subset n\Lambda+E_{n-1}$ (proof of Proposition
T_{Q,h}.6), $\Lambda=\{\pm Mj:j\in J\}$. An element of $Q\Lambda$ is $M$ times a sum of $Q$ odd integers, which is odd since $Q$ is
odd, so it has modulus at least $M$, and every frequency of $f_Q$ has modulus at least $M-(Q-1)=2h-1>2h-3$. For a single
frequency $M'$ the first condition holds identically if $M'>Q+2h-4$ by Proposition T_{Q,h}.6(c), and $2h-1\notin K$ if
$M'>Q+2h-2$; for $M'=M$ the element $M\in Q\Lambda$ gives $2h-1=M-(Q-1)\in K$. (b) The responses $\sigma_k(a)$ are forms of degree
$Q$ in $a$ (Section 12.6). For $2hk-2\ge BQ$, $B=M\max J+1$, the compact response formula is a rational function of
$t_k=1/(2hk-2)$ whose coefficients are polynomials in $a$ and whose denominators do not depend on $a$ and are nonzero near $t=0$,
so $\sigma_k\to\sigma_\infty$ uniformly on compact sets of complex $a$. Choose a closed polydisk $P$ around $e_1$ on which
$|\sigma_\infty|\ge\frac34s_0$, then $K$ with $|\sigma_k-\sigma_\infty|<\frac14s_0$ on $P$ for $k\ge K$, and shrink $P$ so that the finitely
many $\sigma_k$, $k<K$, stay above $\frac12s_0$; then $\inf_{P,k}|\sigma_k|\ge\frac12s_0$. (Pointwise continuity of each response
would not suffice; the locally uniform limit is what gives the common bound.) The tuned coefficients are rational in $a$
with denominators that are products of responses, hence holomorphic on the interior of $P$. The majorant of Theorem T_{Q,h}
uses only absolute values, a bound on $\|f_1\|_1$, $B$ and the response bound, so one geometric bound holds on $P$; fixed
derivatives add polynomial factors, and uniform convergence gives holomorphic, hence real-analytic, dependence. At $e_1$ the
profile equals $1$ at $\theta=\frac\pi{2M}$ and $-1$ at $\frac{3\pi}{2M}$, both in the first quadrant since $M\ge7$; shrink $U$ so these
values stay beyond $\pm\frac12$ and enlarge $R$ so the remainder of the series is below $\frac12$. The potential statement is
Proposition T_{Q,h}.3: $S_n=4-\frac{2hn}Q$ vanishes at an integer order only if $hn=2Q$, which needs $h=2$ and $n=Q$. (c) is
Theorem T_{Q,h} with the stated certificates, the sharp constants of Remark 4 and the resonance-block majorant of Remark 5;
the amplitude factor is $|\varepsilon|^{Q/(2h)}$ since $w=z^Q=r^{-2h}$. (d) A pure degree-zero potential for the order-9 density forces a stream amplitude
$\beta_{\rm pure}$ of $\sin2\theta$ at order 9, while the order-18 condition fixes $H_9=-R_1/\sigma_1$; both are exact rationals, and
$\lambda=\beta_{\rm pure}-H_9>0$, which $\lambda\log r$ ($\Delta\log r=0$, $\partial_{xy}\log r=-r^{-2}\sin2\theta$) corrects without
changing the density. (g) is the same argument at $Q=5,7$. At $n=Q$ the density, stream and potential exponents are $-3,-2,0$; with
$D_{2k}$ the cosine coefficients of the degree $-2$ field $\Delta\chi$, the density identity reads $a_1=2D_0$,
$a_{2k+1}=(k+1)D_{2k}+kD_{2k+2}$ ($k\ge1$), the coefficient $a_1$ vanishes by (a), and backward substitution from above the largest
frequency determines every $D_{2k}$ uniquely; the potential has cosine coefficients $-D_{2k}/(4k^2)$, is unique up to a constant
(Section 12.3), and gives $\beta_{\rm pure}=D_4/8$. An $r^2\log r$ term would need $S_n=2$, that is $n=Q/2$, which is not an integer.
With $H_Q=-R_1/\sigma_1$ the coefficient is $\lambda_Q=\beta_{\rm pure}-H_Q$, and the pure-potential obstruction at order $2Q$ is
$R_1+\sigma_1\beta_{\rm pure}=\sigma_1\lambda_Q\ne0$. The values ($\sigma_1=1.94701466744668\ldots\cdot10^{-5}$,
$H_5=8.43850893134459\ldots\cdot10^{-4}$; $\sigma_1=-9.59906357874719\ldots\cdot10^{-3}$, $H_7=-1.27607811755652\ldots\cdot10^{-4}$) agree
between an exact Cartesian computation, which also reconstructs every density and stream coefficient from the potential,
and an exact polar replay; $\sigma_1$ and $H_5$ also agree with the exact polar program of this section and $\sigma_1$, $H_7$ with a
separate floating polar program. Since $Q$ is odd, the coefficient $\varepsilon^Q\lambda_Q$ has the sign of $\varepsilon\lambda_Q$.
The top coefficients are those of Proposition 8.2 with
$\alpha=\varepsilon$ and $B=12$, and Section 14.22(f) gives the bound. (e) Intermediate value theorem; uniqueness by Taylor's theorem with remainder applied to $S'$, which gives
$S'(m+x)\in c_1(m)+2c_2(m)[-r,r]+3c_3(I)[0,r^2]$ for the jet coefficients at the midpoint $m$ and over $I$, and so $S'<0$ on $I$. (f) The free
harmonics sit at $\delta n-2<Bn$, so the top density coefficients $A_n=(-1)^{n-1}\varepsilon^nh_n$ of frequency $Bn-1$, $B=M+1$, obey
$4d(n-1)h_n=\sum_{i+j=n}\bigl[\frac{2Bj}{(B-\delta)i+2}-1\bigr]h_ih_j$, $h_1=1$, $d=c-1$: the top stream coefficient is
$-A_i/(2((B-\delta)i+2))$ and $(2-i\delta)(Bj-1)-(1-j\delta)Bi=2Bj-((B-\delta)i+2)$. Section 14.22 gives
$h_nR_H^n\sim Kn^{-1-1/b}$, $K>0$, with $R_H=4d\,[a\Gamma(a)\Gamma(b)/\Gamma(a+b)]^{1/a}$, $a=\frac2{B-\delta}$, $b=\frac{2M}{B-\delta}$; at
$r=R_H^{-1/\delta}|\varepsilon|^{1/\delta}$ the top coefficient of the second angular derivative of the $n$-th term is of order
$n^{1-1/b}$, which does not tend to zero since $b>1$. The values $R_H^{-1/\delta}=0.09029734807\ldots$ and $0.23659775280\ldots$
were evaluated independently twice; a float run of the scalar recursion to $n=1500$ at $\delta=\frac45$ gives
$h_nR_H^nn^{1+1/b}=5.6497,\ 5.6359,\ 5.6326,\ 5.6306$ at $n=100,400,800,1500$, consistent with the law. $\square$

Remarks. 1. The generating system of Theorem T_{Q,h} was derived twice, here and in the independent proof, and the two
agree term by term (constants, shifts, the order of the unknowns and the potential). The independent check also verified 330 coefficient identities of the shifted system against a direct ordered recursion for $(h,Q)=(2,5),(2,7),(3,7),
(3,8),(2,9),(3,13)$.
2. Together with Theorems T and T_Q, this gives a convergent tuned pure series at every rational $\delta\in(0,1)$ for every
profile satisfying the two hypotheses, and explicit profiles at $\delta=\frac23,\frac25,\frac12,\frac13,\frac27,\frac14,\frac49,\frac35,\frac47$ (PROVED), single high harmonics with convergent
tuned series at $\delta=\frac49,\frac47,\frac45,\frac6{13}$ (Corollary T_{Q,h}.9, PROVED),
including at $\delta=\frac49$ seven profiles that keep all eight higher harmonics of Candidate 007 (Corollary T_{9,2}.C). It says nothing
about the canonical normalization or about profiles that fail the first compatibility condition (such as $\sin\theta$ at
$\delta=\frac49$, for which every pure series is obstructed at order 9 and the logarithmic series of Section 14 is forced).
3. (Necessary radii from the top mode; PROVED: complete proof here, independently confirmed with all 23 radii.) The free constants never reach the top
frequency: $H_{kQ}$ sits at the stream frequency $2hk-2<BkQ$, and a product involving $g_{kQ}$ at order $kQ+j$ has frequency
at most $2hk-2+Bj-1<B(kQ+j)-1$. So, as in Remark 5 after Theorem T, the top coefficients of every tuned series of
Theorems T_Q and T_{Q,h} are the $A_n=(-1)^{n-1}\alpha^nh_n$ of Proposition 8.2, here with $B=4$ and $\alpha=\varepsilon b$. By
Section 14.22(f), uniform termwise $C^2$ convergence on $\{r\ge R\}$ then requires $R>(|\varepsilon b|/R_H)^{1/\delta}$. The
beta-integral values are $R_H=1.475398$ ($\delta=\frac25$), $2.151872$ ($\frac12$), $1.127213$ ($\frac13$) and $1.748618$
($\frac49$). They were checked against the scalar top recursion to order 1500, and $h_2,\dots,h_5$ against the direct
recurrence at $\delta=\frac49$. For the explicit roots of Corollaries T_5, T_4, T_6 and T_{9,2} these lower bounds for the required exterior radius
are below $0.16|\varepsilon|^{1/\delta}$ (they bound the true radius from below only), except at the largest root at $\delta=\frac49$, where $(|b_5|/R_H)^{9/4}=1.144$. At $\delta=\frac35$ (Corollary T_{10,3}, $B=4$) the same formula gives
$R_H=3.137331$ and lower bounds $0.0016010$, $0.0037185$, $0.0259225$, $0.0624634$ times $|\varepsilon|^{5/3}$ at $b_1,\dots,b_4$
(rounded down; computed here, checked against the scalar top recursion to order 1500, and PROVED: independent check of the
top-mode constants). At $\delta=\frac47$ (Corollary T_{7,2}, $B=4$) it gives $R_H=2.811595$ and lower bounds $0.0127184$,
$0.0430461$, $0.880537$ times $|\varepsilon|^{7/4}$ at the three roots (rounded down; computed here and checked against the scalar
top recursion to order 1500, where $h_nR_H^nn^{1+1/b}=1.6548,\ 1.6455,\ 1.6433,\ 1.6421$ at $n=100,400,800,1500$; PROVED:
independent proof with exact root intervals, the constants at 512 and 1024 bits and the first seven top coefficients compared
with the exact prefix polynomials). For the seven Candidate-shaped profiles of Corollary T_{9,2}.C ($B=20$, top ratio
$\alpha=a_{19}/a_1=1.02151762\ldots\cdot10^{-4}$ of the normalized profile, $R_H=1.28042563\ldots$) the same argument gives the common
necessary bound $R>6.0152\cdot10^{-10}|\varepsilon|^{9/4}$ (PROVED: independent proof with directed-arithmetic constants, reviewed
here), far below the sufficient $2^{161/4}$ to $2^{175/4}$; for $\sin11\theta$ at $\delta=\frac49$ it gives $0.507476|\varepsilon|^{9/4}$
(Corollary T_{Q,h}.9(d)). The proved
sufficient radii of Remark 5 for these two-mode profiles are $2^{16}$ to $2^{42}$ times $|\varepsilon|^{1/\delta}$ (up to $2^{593}$ before Remarks 4 and 5), so the
true radii are bracketed only loosely. At $\delta=\frac49$, $b_5$, the tuned series computed in 1024-bit arithmetic to order 306
(all 34 obstructions vanishing to working precision) has root tests $\|f_n\|^{1/n}=7.35,9.13,9.61,9.83,9.96,10.005$ at
$n=36,72,144,216,288,300$, a fitted growth constant $A\approx10.69$ for $n\ge150$ and $|H_n|^{1/n}\approx10.04$ at $n=288$
(NUMERICAL EVIDENCE, the numerical report). This points to a true radius near $A^{9/4}\approx2\cdot10^2$ at $\varepsilon=1$,
inside the bracket $(1.144,\,2^{117/4})$ given by Remark 5.
4. (Sharper constants in the majorant; PROVED: independent proof, reviewed here line by line, with an independent exact
reproduction of the boxes here.) Three changes leave every step of the proof of item 1, the shifts of Step 4 and the strictly
lower triangular form of $J$ unchanged.
(i) Initial norms. In Step 4 the Catalan values $\bar x_j$, $j\le Q$, serve only as upper bounds for $x_j=j\|f_j\|_1$: the $W$
row sums the density equalities from order $Q+1$ on, and the $V$ and $E$ rows use $\bar x_1,\dots,\bar x_Q$ only as
coefficients. Since $f_1,\dots,f_Q$ contain no free constant, any rationals $d_j\ge j\|f_j\|_1$ ($1\le j\le Q$) may replace
them; the induction of Step 3 then starts at order $Q+1$ and never uses the Catalan recursion.
(ii) Reduced bilinear constant. $|p_j|/j=|1/j-\delta|\le\max(\delta,1-\delta)$ and $|P_i|/i=|2/i-\delta|\le2-\delta$ for
$i,j\ge1$, so $\|T(g_i,f_j)\|_1\le B\big(2-\delta+\max(\delta,1-\delta)\big)ij\|g_i\|_1\|f_j\|_1$. Every order estimated after the
initial block is $m\ge Q+1$, where $\frac m{\lambda_m}=\frac{1-\delta}\delta\frac m{m-1}\le\frac{1-\delta}\delta\frac{Q+1}Q$, and in the $E$ row
the factor $\frac n{n+Q}\le1$ is dropped. So $\kappa$ may be replaced by
$$\kappa_*=B\big(2-\delta+\max(\delta,1-\delta)\big)\frac{(1-\delta)(Q+1)}{\delta Q},$$
which is $\frac{950}{81}$ instead of $\frac{230}9$ at $\delta=\frac49$, $B=4$, and $\frac{4750}{81}$ instead of $\frac{1150}9$ for $B=20$.
(iii) Sharp Poisson norm. For odd $l\ge1$,
$\Pi_n\sin l\theta=\frac{\sin(l-1)\theta}{2(l-1-P_n)}-\frac{\sin(l+1)\theta}{2(l+1+P_n)}$, without the first term if $l=1$ and with
resonant outputs deleted. The linear denominators $u=l-1-P_n$, $v=l+1+P_n$ of the retained outputs are nonzero elements of
$\frac2Q\mathbb Z$ with $u+v=2l$, so they are not both negative, and convexity of $u\mapsto\frac1u+\frac1{2l-u}$ on
$[\frac2Q,2l-\frac2Q]$ (and monotonicity when one is negative) gives $\frac12(\frac1{|u|}+\frac1{|v|})\le\frac Q4+\frac Q{4(lQ-1)}$. For
$l=1$ the single output gives $\frac Q4$. Hence $\|\Pi_nf\|_1\le L_Q\|f\|_1$ with
$$L_Q=\frac{3Q^2}{4(3Q-1)}<\frac Q2,$$
uniformly in $n$; $L_9=\frac{243}{104}$ is attained by $\sin3\theta$ at $n=13$ (outputs $\frac9{104}$ and $-\frac94$). So $L=\frac Q2$
may be replaced by $L_Q$ in Steps 1 to 4; the free constants keep their own variables $\eta_n$.
With (i) to (iii), the exact box test (smallest passing $z_0=2^{-q}$ in the family $2Y_0$; the box at $2^{-(q-1)}$ fails)
gives, at the five roots of Corollary T_{9,2} in increasing order:
- with the bounds $s_i$ of (b): $q=104,100,113,101,107$, so $R_i=2^{234},2^{225},2^{1017/4},2^{909/4},2^{963/4}$ (PROVED;
  with (i) and (ii) alone $q=113,108,122,110,115$, and with (i) alone $q=125,120,134,122,127$);
- with the bounds $s'_i$ of (c): $q=100,94,107,96,83$, so $R_i=2^{225},2^{423/2},2^{963/4},2^{216},2^{747/4}$ (PROVED, as (c)).
For Corollary T_{9,2}.C(b) ($B=20$, $s=2^{-28}$) it gives $q=129$ ($q=138$ with (i) and (ii) alone, $q=150$ with (i) alone),
so the series converges on $r\ge R>2^{1161/4}|\varepsilon|^{9/4}$, and since $a_1^{9/4}<2^{9.49}$, on $r>2^{300}$ at Candidate
007's amplitude (was $2^{593}$; PROVED). For Corollary T_{9,2}.C(c) it gives $q=123$, so $r\ge R>2^{1107/4}|\varepsilon|^{9/4}$
and $r>2^{287}$ at Candidate 007's amplitude ($q=132$ with (i) and (ii) alone; PROVED). Remark 5 improves all of these.
The initial norms $d_j$ were obtained here by interval arithmetic (90 digits) over a root enclosure of width $2\cdot10^{-40}$
certified by a sign change of $O_9$, rounded up to 10 significant digits. The independent proof uses ball arithmetic and
the Cartesian form of the recurrence; for every case computed by both programs the exponents agree.
Why the radii stay large (heuristic, not a theorem): in $A_1$ the term $2P_1W$ feeds $W$ into $V_1$ with weight about
$2\kappa L\bar x_1z$, the rows $V_2,\dots,V_{Q-1}$ and $E$ multiply by about $2\kappa L\bar x_1$ each, $E$ carries the factor
$1/\sigma_*$, and the $W$ row returns $\kappa\bar x_1E$. A passing box needs this loop gain
$(2\kappa L\bar x_1)^Q\kappa\bar x_1z_0/\sigma_*$ to stay below $1$; with $\kappa_*$, $L_9$ and $s'$ it requires about $z_0<2^{-83}$ at
$b_1$ and $z_0<2^{-59}$ at $b_5$, against the exact $2^{-100}$ and $2^{-83}$. The loop bounds the $Q$-step linear response of
the lookahead to a change of $f_n$ one step at a time; a much smaller radius would need a bound on that response as a
whole, uniform in $n$. Remark 5 removes the main part of this loss: the loop there closes through $w=z^Q$.
5. (Resonance-block majorant; PROVED: independent proof, reviewed here line by line, with the boxes of (c) at $M=1$
reproduced exactly here by a second program that also checks the system against the scalar recursion.) In Step 4 the
variables $\bar\eta_n$ and $\bar u_{n,r}$ are introduced at every order $n\ge Q$, although $H_n=0$ unless $Q\mid n$; the
loop of Remark 4 then closes after one power of $z$, and the geometric base is the loop gain itself.
(a) Let (T_{Q,h}-a) hold, let $0<s\le\inf_k|\sigma_k|$, fix $M\ge1$, $N=MQ$, and let $d_j\ge j\|f_j\|_1$ ($1\le j\le N$) and
$e_a\ge aQ|H_{aQ}|$ ($1\le a<M$) be rational bounds for the actual tuned prefix. Let $L=L_Q$ and
$\kappa_N=B\big(2-\delta+\max(\delta,1-\delta)\big)\frac{(1-\delta)(N+1)}{\delta N}$. Put $x_j=d_j$ ($j\le N$), $\eta_{aQ}=e_a$ ($a<M$),
$\eta_n=0$ for $Q\nmid n$, and for $n=kQ\ge N$ define in this order $u_{n,1},\dots,u_{n,Q-1}$, $\eta_n$, $x_{n+1},\dots,x_{n+Q}$ by
$$u_{n,r}=\kappa_N\Big[L\!\!\sum_{i+j=n+r,\ i,j\ge r}\!\!x_ix_j+\!\!\sum_{i+j=n+r,\ j\ge Q+1}\!\!\eta_ix_j+2L\sum_{j=1}^{r-1}d_ju_{n,r-j}\Big],$$
$\eta_n=\frac{\kappa_N}{s}[\,\cdots]$ with the same bracket at $r=Q$, and $x_m=\kappa_N\sum_{i+j=m}(Lx_i+\eta_i)x_j$. These are the
inequalities of Steps 2 and 3 (with Remark 4) with $\eta_n=0$ off the resonances, which is exact because $H_n=0$ there; the
harmonic partner in a lookahead row has index at least $Q+1$ because the harmonic index is at most $n-Q$, and every
estimated order is at least $N+1$. So the induction of Step 3 gives $j\|f_j\|_1\le x_j$ and $n|H_n|\le\eta_n$ for all $j,n$.
With $w=z^Q$, $X_r=\sum_{k\ge0}x_{N+r+kQ}w^k$ ($1\le r\le Q$), $E=\sum_{k\ge0}\eta_{N+kQ}w^k$, $V_r=\sum_{k\ge0}u_{N+kQ,r}w^k$, the
density is $P+U$ with $P=\sum_{j\le N}d_jz^j$, $U=\sum_rz^{N+r}X_r(z^Q)$, and the free constants are $H+z^NE(z^Q)$ with
$H=\sum_{a<M}e_az^{aQ}$. Projecting the equalities onto the residues: $U\cdot U$ contributes $w^MD_r+w^{M+1}C_r$ with
$D_r=\sum_{i+j=r}X_iX_j$, $C_r=\sum_{i+j=Q+r}X_iX_j$ ($1\le i,j\le Q$); $d_iz^i\cdot U$ contributes $d_iX_tw^{(i+t-r)/Q}$ when
$Q\mid i+t-r$; $H\cdot U$ gives $H_*X_r$ with $H_*=\sum_ae_aw^a$; $z^NE\cdot P$ gives $E\sum_ad_{aQ+r}w^a$; $z^NE\cdot U$ gives
$w^MEX_r$. The restrictions $i,j\ge r$ and $j\ge Q+1$ in the lookahead rows remove exactly the constant cross terms and
the term $Ed_r$. For $M=1$ the result is
$$V_r=\kappa\Big[LA_r+wEX_r+2L\sum_{j<r}d_jV_{r-j}\Big],\quad E=\frac\kappa s\Big[LA_Q+wEX_Q+2L\sum_{j<Q}d_jV_{Q-j}\Big],
\quad X_r=\kappa\big[LB_r+Ed_r+wEX_r\big],$$
with $A_r=a_r+2w\sum_{i+j=Q+r}d_iX_j+wD_r+w^2C_r$, $B_r=A_r-a_r+b_r+2\sum_{i+j=r}d_iX_j$,
$a_r=\sum_{i+j=Q+r,\,i,j\ge r}d_id_j$, $b_r=\sum_{i+j=Q+r}d_id_j$ (indices in $1,\dots,Q$). In every case the map
$Y=(V_1,\dots,V_{Q-1},E,X_1,\dots,X_Q)\mapsto\Phi(w,Y)$ has nonnegative coefficients, and at $w=0$ the $V$ rows depend only on
earlier $V$ rows, $E$ only on $V$, and $X_r$ only on $E$ and $X_t$, $t<r$. So $\Phi(0,Y)=c_0+JY$ with $J\ge0$ strictly lower
triangular, and the box test of Step 4 applies with $T=(I-J)^{-1}$, $Y_0=Tc_0$, $G=Y_0+T(\Phi(w,Y)-\Phi(0,Y))$: if a rational
vector $b\ge Y_0$ satisfies $G(w_0,b)\le b$, then $x_n+\eta_n=O(w_0^{-n/Q})$, and the tuned series, its derivatives and the
potential of Proposition T_{Q,h}.3 converge on $r\ge R>w_0^{-1/(2h)}|\varepsilon|^{Q/(2h)}$.
(b) ($h=1$.) The same holds at $\delta=2/Q$ for Theorem T_Q with $M\ge2$, $e_1=0$ (there is no free constant at order $Q$,
where the stream frequency would be $0$), the responses $\sigma_k$, $k\ge2$, and $R>w_0^{-1/2}|\varepsilon|^{Q/2}$: $L_Q$ is valid
because $P_n\in\frac2Q\mathbb Z$, $N\ge2Q$ makes the first unknown free constant a true resonance, and the potential keeps
only the logarithms at orders $Q$ and $2Q$.
(b') (Tail-only response bound; PROVED: independent proof, reviewed here and independently confirmed.) In (a) and (b)
the hypothesis $s\le\inf_k|\sigma_k|$ may be replaced by $0<s\le|\sigma_k|$ for every $k\ge M$. Indeed the response enters
the system only through the division in the row of $\eta_n$, $n=kQ\ge N$, that is, at the unknown free constants
$H_{kQ}=-R_k/\sigma_k$ with $k\ge M$; the known constants $H_{aQ}$, $a<M$, enter only through the certified bounds $e_a$, which
already contain the effect of the earlier responses. The constants $L,\kappa_N$, the residue projection and the box test
are unchanged. This helps when the global minimum of $|\sigma_k|$ occurs at a small $k$ inside the certified prefix.
(c) Radii (exact rational boxes; the box at $2w_0$ fails in the same family). At $\delta=\frac49$, $M=1$, box $2Y_0$, the
two-mode roots in increasing order give $w_0=2^{-q}$ with $q=156,152,167,156,171$ for the bounds $s_i$ of Corollary
T_{9,2}(b), so $R_i=2^{39},2^{38},2^{167/4},2^{39},2^{171/4}$, and $q=152,146,161,151,147$ for the exact infima of (c), so
$R_i=2^{38},2^{73/2},2^{161/4},2^{151/4},2^{147/4}$. At the largest root, the independent proof's prefix through order 90
(ball arithmetic in 3072 bits, propagated from the root interval without midpoint resets; $M=10$, $s=4114$, box found by
an approximate iteration and verified exactly) gives $q=117$, so $R=2^{117/4}<6.4\cdot10^{8}$. For Corollary T_{9,2}.C(b),
(c), (d), (e) ($B=20$, $s=2^{-28},2^{-21},2^{-23},2^{-14}$): $q=200,194,198,197$, normalized
$R=2^{50},2^{97/2},2^{99/2},2^{197/4}$, and at Candidate 007's amplitude $r>2^{60},2^{59},2^{60},2^{59}$. At the first four
two-mode roots the independent proof certifies prefixes to order 36 by the same ball method ($M=4$, exact infima of (c),
boxes found by approximate iteration and verified exactly), with $q=129,125,129,121$, so $R=2^{129/4},2^{125/4},2^{129/4},
2^{121/4}$. For Corollary T_{9,2}.C(e), (c), (b), (d) (the first four roots of (a)) the independent proof certifies
prefixes to order 27 by the same method ($M=3$), with $q=161,166,174,171$, so normalized $R=2^{161/4},2^{83/2},2^{87/2},
2^{171/4}$ and, since $a_1^{9/4}<2^{9.49}$, $r>2^{50},2^{51},2^{53},2^{53}$ at Candidate 007's amplitude. At the smallest
two-mode root a prefix to order 72 gives no further gain (the best box stays at $q=129$ for $N=27,36,\dots,72$); at the
second and fourth the same holds ($q=125,121$), and at the third a prefix to order 54 gives $q=128$, so $R=2^{32}$. For
Corollary T_{9,2}.C(f) a prefix to order 36 gives $q=171$ (first reached at $N=27$), so normalized $R=2^{171/4}$ and
$r>2^{53}$ at Candidate 007's amplitude; for Corollary T_{9,2}.C(g) it gives $q=166$ (first reached at $N=27$; $q=167$ for
the box $2Y_0$), so normalized $R=2^{83/2}$ and $r>2^{51}$; for Corollary T_{9,2}.C(h) (uniform response bound $1$) it gives
$q=175$ (first reached at $N=18$), so normalized $R=2^{175/4}$ and $r>2^{54}$. For $h=1$, $M=2$, with the response bounds of Theorem T and Corollaries T_4, T_5,
T_6, in increasing root order: $Q=3$: $R=2^{35/2},2^{16}$; $Q=4$: $2^{43/2},2^{24},2^{25},2^{25},2^{24},2^{49/2}$; $Q=5$:
$2^{61/2},2^{73/2},2^{67/2},2^{67/2},2^{67/2},2^{67/2}$; $Q=6$: $2^{39},2^{43},2^{43},2^{85/2},2^{41},2^{81/2}$; all times
$|\varepsilon|^{Q/2}$ (before: $2^{54.5}$ and $2^{48.8}$, $2^{80}$ to $2^{98}$, $2^{126}$ to $2^{162}$, $2^{180}$ to $2^{219}$). With $M=2$ and the
exact prefixes through $2Q$ the same system gives the radii $2^{95/2}$ to $2^{113/2}$ at $Q=7$ and $2^{57}$ to $2^{141/2}$ at $Q=8$
of Corollaries T_7(b) and T_8(b) (independent certificates); prefixes through $8Q$ lower them to $2^{47}$ to $2^{56}$ and
$2^{113/2}$ to $2^{70}$, and (b') with prefixes through orders 140 and 96 gives $2^{109/2}$ and $2^{65}$ at the third roots
for $Q=7$ and $Q=8$. At
$Q=4$ the independent proof also certifies prefixes to order 40 (best boxes first reached at $N=24,32,24,16,16,16$), which
give $R=2^{41/2},2^{23},2^{24},2^{24},2^{23},2^{47/2}$ times $|\varepsilon|^2$; at $Q=5$ certified prefixes to order 50
give $R=2^{59/2},2^{71/2},2^{65/2},2^{65/2},2^{65/2},2^{65/2}$ times $|\varepsilon|^{5/2}$ (first reached at $N=30,20,30,20,20,20$),
improved at the sixth root to $2^{63/2}$ by (b') ($N=50$, $|\sigma_k|>\frac1{32}$ for $k\ge10$, an independent certificate
with a complete interval cover of the tail), and at $Q=6$
certified prefixes to order 60 give $R=2^{38},2^{42},2^{42},2^{83/2},2^{40},2^{79/2}$ times
$|\varepsilon|^3$ (first reached at $N=24,24,24,24,36,24$). The
$\delta=\frac49$ boxes at $M=1$ were reproduced here with the initial norms of Remark 4, and in each case the formal
solution of the block system agreed with the direct scalar recursion in 54 exact coefficients. The $M\ge2$ and $h=1$
boxes are exact certificates of the independent proof and were not recomputed here, except as stated next. A second
program here for general $M$ (the tuned prefix computed in interval arithmetic over the root enclosure, with the
obstruction mode checked to contain zero and each $H_{aQ}$ obtained from two provisional continuations; the block system
checked against the direct scalar recursion) reproduces the $M=1$ exponent $q=151$ at the fourth two-mode root and
gives $q=122$ there with $M=2$. With $M=4$ it gives, at the first four two-mode roots, $q=130,126,130,122$ for the box
$2Y_0$ and $q=129,125,129,121$ for a box from an approximate iteration (verified exactly), the same exponents as the
independent proof in both families.
(d) At the largest root at $\delta=\frac49$ the bracket for the true radius is now $(1.144,\,2^{117/4})$, against the numerical
estimate of about $2\cdot10^2$ (Remark 3). No estimate here apportions the remaining factor of about $2^{22}$. Heuristically it comes from the constants
$\kappa_N$ and $L_Q$, which are applied at every order and frequency although each is attained only at particular ones
($L_9=\frac{243}{104}$ is attained, for example, at $n=13$ by the input $\sin3\theta$, whose particular stream is
$\frac9{104}\sin2\theta-\frac94\sin4\theta$), and from the triangle inequality in the lookahead rows. A failing box does
not exclude other supersolutions, so a sufficient radius is not a proved lower bound for the true radius. At the
other two-mode roots the comparison is similar (NUMERICAL EVIDENCE: root tests of the computed tuned series to order
306, by a separate program): fitted growth constants of about $0.30$, $0.41$, $1.03$ and $1.71$ at the first four
roots give radii $A^{9/4}$ near $0.07$, $0.13$, $1.07$ and $3.4$, against the sufficient radii $2^{129/4}$, $2^{125/4}$,
$2^{32}$, $2^{121/4}$.
The sufficient radii hardly depend on the root while the numerical radii vary by a factor of about $3\cdot10^3$, which
suggests (a heuristic, not a proved statement) that the majorant is limited by its constants rather than by the profile. The
same pattern holds at $\delta=\frac13$ (NUMERICAL EVIDENCE, root tests to order 300 by a separate program): fitted constants
of about $7.6$, $0.48$, $0.82$ to $0.85$, $1.39$ to $1.53$, $2.2$ to $2.4$ and $5.0$ to $5.2$ at the six roots in increasing order give
apparent radii $A^3$ near $440$, $0.11$, $0.55$ to $0.61$, $2.7$ to $3.6$, $11$ to $14$ and $130$ to $144$ times $|\varepsilon|^3$, against
the sufficient $2^{38}$, $2^{42}$, $2^{42}$, $2^{83/2}$, $2^{40}$, $2^{79/2}$; at $\delta=\frac25$ the constants $3.91$, $0.393$, $0.440$,
$0.901$, $1.73$, $3.59$ give $A^{5/2}$ near $30$, $0.10$, $0.13$, $0.77$, $3.9$, $24$, against $2^{59/2}$, $2^{71/2}$, then $2^{65/2}$ at the
next three and $2^{63/2}$ at the sixth. The variation that the sufficient radii do show follows the response lower bound $s$ of the box rather than the
growth constant (an observation about these certificates): at $\delta=\frac13$ the exponents $38,\frac{79}2,40,\frac{83}2,42,42$ belong to
response infima of about $17$, $0.48$, $1.9\cdot10^{-2}$, $1.5\cdot10^{-3}$, $3.1\cdot10^{-4}$, $1.7\cdot10^{-4}$ (first, sixth, fifth,
fourth, third and second roots), and at $\delta=\frac25$ the root with the largest apparent radius ($-0.4898$, $s=0.401$) has the
smallest exponent while the root with the smallest one ($0.0490$, $s=2.17\cdot10^{-6}$) has the largest. At the root $-0.6087$ the
certified finite residual enclosures of the truncations grow from $N=40$ to $N=80$ at $r=512$ and decrease over $N=10,20,40,80$ at
$r=1024$ and $r=2048$; these finite data do not locate the true threshold.
6. (Explicit remainder bounds; PROVED: independent proof, reviewed here line by line.) Let a box of Remark 5(a) or 5(b)
pass at $w_0$, and let $b_1,\dots,b_Q$ and $e$ be its $X_r$ and $E$ components. Fix an integer $J\ge N$ and $z>0$ with
$t=z^Q/w_0<1$, and put $K_r=\max\big(0,\lceil(J+1-N-r)/Q\rceil\big)$, $K_E=\max\big(0,\lceil(J+1-N)/Q\rceil\big)$. For an integer
$d\ge0$ let $A_0(m,K,t)=\frac{t^K}{(m+QK)(1-t)}$ and $A_d(m,K,t)=\big(m+Qt\frac{d}{dt}\big)^{d-1}\frac{t^K}{1-t}$ for $d\ge1$, and
$$D_d=\sum_{r=1}^Qb_rz^{N+r}A_d(N+r,K_r,t),\qquad E_d=e\,z^NA_d(N,K_E,t).$$
Then the tails $\rho_J=\sum_{n>J}r^{1-n\delta}f_n$ and $\psi_J=\sum_{n>J}r^{2-n\delta}g_n$ satisfy, with $z=r^{-\delta}$ and for all
integers $a,b\ge0$, $d=a+b$,
$$r^{-1}\big\|(r\partial_r)^a\partial_\theta^b\rho_J\big\|\le\max(\delta,1-\delta)^aB^bD_d,\qquad
r^{-2}\big\|(r\partial_r)^a\partial_\theta^b\psi_J\big\|\le(2-\delta)^aB^b\big(LD_d+E_d\big),$$
in the uniform norm and in the Wiener norm in $\theta$. Since $D_d$ and $E_d$ increase with $z$, their values at
$z=R^{-\delta}$ bound the tails uniformly on $r\ge R$ whenever $R^{-\delta Q}<w_0$. For amplitude $\varepsilon$ replace $z$ by
$|\varepsilon|r^{-\delta}$ ($f_n$, $g_n$ and $H_n$ are homogeneous of degree $n$ in $\varepsilon$ by the uniqueness of the tuning).
Proof. Monotone iteration gives $X_r(w_0)\le b_r$ and $E(w_0)\le e$ for the formal solution, so
$x_{N+r+kQ}\le b_rw_0^{-k}$ and $\eta_{N+kQ}\le e\,w_0^{-k}$. Every $n>N$ is uniquely $N+r+kQ$ with $1\le r\le Q$, $k\ge0$, and
$n>J$ if and only if $k\ge K_r$; $H_n=0$ unless $Q\mid n$, and $N+kQ>J$ if and only if $k\ge K_E$. Since
$n^d\|f_n\|_1\le n^{d-1}x_n$, $n^d|H_n|\le n^{d-1}\eta_n$ and $(m+Qt\frac d{dt})t^k=(m+Qk)t^k$, this gives
$\sum_{n>J}n^d\|f_n\|_1z^n\le D_d$ and $\sum_{n>J}n^d|H_n|z^n\le E_d$ (for $d=0$ use $\frac1{m+Qk}\le\frac1{m+QK}$). The radial
multipliers are $(1-n\delta)^a$ and $(2-n\delta)^a$, with $|1-n\delta|\le n\max(\delta,1-\delta)$ and $|2-n\delta|\le n(2-\delta)$
for $n\ge1$; the frequencies of $f_n$ and $g_n$ are at most $Bn$, and $\|g_n\|_1\le L\|f_n\|_1+|H_n|$. The dominating series
converge, which justifies termwise differentiation. The moment identity was checked here in exact arithmetic in 270
cases ($d\le4$). Since even $\sum_kx_{N+r+kQ}w_0^k\le b_r$ holds, $A_d$ may be replaced by $\sup_{k\ge K}(m+Qk)^{d-1}t^k$ (and
$A_0$ by $\frac{t^K}{m+QK}$), which removes the factor $\frac1{1-t}$ (PROVED: proposed here, independent proof and
confirmation). The proof is three lines: with $c_k=x_{N+r+kQ}w_0^k\ge0$ and $\sum_kc_k\le b_r$,
$\sum_{k\ge K}c_k(m+Qk)^{d-1}t^k\le b_r\max_{k\ge K}(m+Qk)^{d-1}t^k$. For $d\ge2$ the ratio of consecutive
terms, $t(1+Q/(m+Qk))^{d-1}$, decreases strictly to $t<1$, so the maximum is attained at the least $k\ge K$ where the
ratio is at most $1$; for $d=1$ the ratio is $t$, and for $d=0$ it is $t(m+Qk)/(m+Q(k+1))<1$ (increasing in $k$), so in
both cases the maximum is the term at $k=K$. The maximum is an exactly computable rational when $m$, $Q$ and $t$ are
rational (not for general real $t$: $K=1$, $m=10$, $Q=5$, $d=0$, $t=\sqrt2/2$ gives $\sqrt2/30$). A maximum is no larger than the corresponding sum, so the sharpened bounds are no
larger than $D_d,E_d$, and for one residue class they are the best bounds that use only its total budget $b_r$ (this says
nothing about the actual coefficients). In the primary normalization of the theorem ($r^{-\gamma}$, $\gamma=1-\delta$, for
the density and $r^{-1-\gamma}$ for the stream) the right sides are multiplied by $|\varepsilon|/z$, since
$r^{\delta}=|\varepsilon|/z$ for $z=|\varepsilon|r^{-\delta}$; at unit amplitude this is division by $z$. These bounds turn every passing box into
explicit truncation-error estimates for the density, the stream and their derivatives; they give nothing inside the
radius of the box. Examples (exact rational evaluations of the independent proof with the sharpened bounds, primary
normalization, $\varepsilon=1$, closed exteriors; not recomputed here): for the fourth two-mode root at $\delta=\frac49$ with
the prefix to order 36, on $r\ge2^{135/4}$ and $J=36$, the density remainder and its first three angular derivatives are
below $2^{-448},2^{-440},2^{-433},2^{-426}$, and the stream remainders below $2^{-446},2^{-439},2^{-432},2^{-425}$; for the first
Candidate-shaped root with the prefix to order 27, on $r\ge2^{171/4}$ and $J=27$, the density bounds are
$2^{-399},2^{-390},2^{-381},2^{-371}$ and the stream bounds $2^{-396},2^{-386},2^{-377},2^{-368}$; for the largest two-mode root at
$\delta=\frac49$ with the prefix to order 90, on $r\ge2^{63/2}$ and $J=90$, the density remainder is below $2^{-902}$ and its
third angular derivative below $2^{-877}$ (the earlier $2^{-916}$ and $2^{-891}$ in the weight $r^{-1}$ are the same bounds
multiplied by $z=2^{-14}$).
7. (Finite stationary residual; PROVED: independent proof, reviewed here line by line.) Let $J\ge1$ and let $f_n,g_n$,
$1\le n\le J$, satisfy (R) for $2\le n\le J$ and the Poisson equations $-\Delta(r^{2-n\delta}g_n)=\partial_x(r^{1-n\delta}f_n)$
(at a resonant order $n\le J$ this includes the harmonic $H_n$ actually used). Assume all frequencies of $f_n,g_n$ are at
most $Bn$, and let $\alpha_n\ge\|f_n\|_1$, $\beta_n\ge\|g_n\|_1$. Put $\rho_J=\sum_{n\le J}r^{1-n\delta}f_n$,
$\psi_J=\sum_{n\le J}r^{2-n\delta}g_n$, $u_J=(-\partial_y\psi_J,\partial_x\psi_J)$ and $\mathcal R_J=c\,r\partial_r\rho_J+u_J\cdot\nabla\rho_J-\rho_J$.
Then $-\Delta\psi_J=\partial_x\rho_J$ exactly and
$$\mathcal R_J=\sum_{n=J+1}^{2J}r^{1-n\delta}\sum_{i+j=n,\ i,j\le J}\big[(2-i\delta)g_if_j'-(1-j\delta)g_i'f_j\big],$$
so that, with $C_n=\sum_{i+j=n,\,i,j\le J}\big(|2-i\delta|Bj+|1-j\delta|Bi\big)\beta_i\alpha_j$, $z=r^{-\delta}$ and all
$a,b\ge0$,
$$r^{-\gamma}\big\|(r\partial_r)^a\partial_\theta^b\mathcal R_J\big\|_1\le\sum_{n=J+1}^{2J}z^{n-1}|1-n\delta|^a(Bn)^bC_n .$$
The right side increases in $z$, so its value at $z=R^{-\delta}$ bounds the closed exterior $r\ge R$; amplitude $\varepsilon$
multiplies it by $|\varepsilon|$ with $z$ replaced by $|\varepsilon|r^{-\delta}$. Proof: in polar form
$u\cdot\nabla\rho=r^{-2}\big[(r\partial_r\psi)\partial_\theta\rho-\partial_\theta\psi\,(r\partial_r\rho)\big]$, and the pair $(i,j)$ has radial
degree $(2-i\delta)+(1-j\delta)-2=1-(i+j)\delta$; the linear part at order $n$ is $(c(1-n\delta)-1)f_n=-(n-1)(c-1)f_n$, which
vanishes at $n=1$ and cancels the quadratic part at each $2\le n\le J$ by (R); the Wiener algebra and bandwidth bounds
give $C_n$, and $r^{1-n\delta-\gamma}=z^{n-1}$. Checked here independently in floating point at $\delta=\frac27$,
$f_1=\sin\theta+\frac13\sin3\theta$, $J=6$, $B=4$ (non-resonant prefix): the residual computed directly from the Cartesian
operator agrees with the displayed order-$J+1$ to $2J$ formula to relative $7\cdot10^{-14}$ at 24 points, the Poisson
equations hold to finite-difference accuracy, and the bounds for $(a,b)=(0,0),(1,1)$ hold at the sampled points. If $J$ is
resonant the residual must use the tuned $H_J$ (which is fixed only at a later order), so a prefix whose last harmonic
is not yet tuned is used with $J-1$. A small residual is not by itself convergence or an error bound for a true
solution; with Remark 6 it quantifies how well a certified prefix satisfies the stationary equation. Examples (exact
evaluations of the independent proof, weight $r^{-\gamma}$, $\varepsilon=1$): the fourth two-mode root at $\delta=\frac49$ with
$J=35$ on $r\ge2^{135/4}$ gives $\|r^{-\gamma}\mathcal R_J\|<2^{-496}$; the first Candidate-shaped root with $J=26$ on
$r\ge2^{171/4}$ gives $<2^{-466}$; the fifth root at $Q=5$ with $J=50$ on $r\ge2^{35}$ gives $<2^{-660}$; the sixth root at
$Q=6$ with $J=60$ on $r\ge2^{45}$ gives $<2^{-765}$.

## 13. Gaps and next steps

- Logarithmic series at rational $\delta$, including the stored value of Candidate 007 (Section 14): formal existence and
  a Gevrey bound of order $1/n_r$ are proved; convergence for the canonical normalization is OPEN. Sufficient
  estimates are stated in Section 14.5, and Sections 14.14 and 14.16 give two further sufficient routes.
- Theorem E (Section 8.1): PROVED and independently confirmed. Compatibility at the first resonance $n_0$ and the
  infinite continuation at the stored value remain OPEN.
- Double series with exterior multipoles: Theorems M and M' (Section 12.1, PROVED) give convergence at every Brjuno
  $\delta$ for finite and real-analytic profiles and geometrically bounded multipoles. Rational $\delta$ (where
  logarithms reappear) is not covered by them, and whether every exterior solution has this form is OPEN. At
  $\delta=2/3$, Theorem T (Section 12.4, PROVED) gives convergent pure series with multipoles forced by the profile whenever
  $O_6=0$ and $\inf_k|\sigma_k|>0$, verified exactly for two explicit two-mode profiles. The second condition is open
  (Theorem T.6, PROVED), so the admissible profiles contain a relatively open subset of the hypersurface $O_6=0$ around
  each verified profile, including explicit three-mode families (Corollary T.7, PROVED); on every regular component of
  the normalized hypersurface it holds on an open dense set of full measure (Theorems T.8 and T_Q.5, PROVED). The same
  mechanism works at every $\delta=2/Q$, $Q\ge3$ (Theorem T_Q, Section 12.5; PROVED), with six explicit profiles and
  explicit radii at $\delta=2/5$ (Corollary T_5, PROVED, exact minima of the response included), six at $\delta=1/2$,
  $c=2$ (Corollary T_4, PROVED), six at $\delta=1/3$ (Corollary T_6, PROVED), ten at $\delta=2/7$ (Corollary T_7, PROVED), ten at
  $\delta=1/4$ (Corollary T_8, PROVED), ten at $\delta=2/9$ (Corollary T_9, PROVED) and fourteen at $\delta=1/5$ (Corollary T_10, PROVED). It extends to every rational
  $\delta\in(0,1)$ (Theorem T_{Q,h}, Section 12.6, PROVED), with five explicit profiles at $\delta=4/9$ (Corollary T_{9,2},
  PROVED), genericity there (Theorem T_{Q,h}.5, PROVED), and convergent tuned series for all seven profiles that keep all
  eight higher harmonics of Candidate 007 and change only its $\sin3\theta$ coefficient (Corollary T_{9,2}.C, PROVED), and
  four explicit profiles at $\delta=3/5$, $c=5/2$ (Corollary T_{10,3}, PROVED; explicit radii PROVED at all four roots). First compatibility
  does not imply the response condition: a support gap in the leading frequencies forces zero responses (Proposition
  T_{Q,h}.6, PROVED), and $\sin13\theta$, $\sin15\theta$ at $\delta=4/9$ are obstructed at orders 36 and 45 with every constant
  free (finite exact computations, independently reproduced: PROVED). Conversely, at every reduced $\delta$ with even numerator at least 4 the first
  condition is solvable in every two-dimensional linear space of finite odd sine polynomials (Proposition T_{Q,h}.8, PROVED); the parity argument says nothing at odd numerators, including Candidate 007's stored
  value. At $\delta=4/7$ three explicit two-mode profiles converge (Corollary T_{7,2}, PROVED), and single high harmonics
  with no $\sin\theta$ term give convergent tuned series and open lattice families at $\delta=4/9$, $4/7$, $4/5$ and $6/13$ (Corollary
  T_{Q,h}.9, PROVED). At
  $\delta=2/3$ the three-mode restriction
  has no zero of $\sigma_\infty$ on the compatibility curve for $-3\le\tau\le98$ (Proposition T.9, PROVED), and the two
  explicit roots carry explicit polydisks of admissible three-mode profiles (Corollary T.10, PROVED). OPEN: the
  genericity theorems for other $Q$ and $h$ ($h=1$ with $Q\ge11$, and $h\ge2$ except $\delta=4/9$; they need the irreducibility of the two-mode obstruction and, for $h\ge2$,
  non-proportionality certificates); the compatibility condition at Candidate 007's stored rational value (order
  $Q\approx8.2\cdot10^{15}$); whether the unique formal shape $b(\delta)$ through a tuned profile (Section 12.4,
  Remark 7, PROVED) converges, which would give a family of tuned solutions across a rational exponent; singular points of the
  compatibility hypersurface and profiles with zero $\sin\theta$ coefficient; whether the response condition holds at a
  given profile without exact algebra; and whether every exterior solution is of this form.
- Hypothesis (H) of Theorem C: PROVED for every finite real profile with nonzero $\sin\theta$ coefficient and for
  generic analytic profiles (Section 10). OPEN for finite profiles without a $\sin\theta$ term (at $\delta=4/9$,
  $\sin11\theta$ is compatible at the first resonance and even has a convergent tuned series, Corollary T_{Q,h}.9, and on the
  lattices of Proposition T_{9,2}.7 the first condition holds
  identically there) and for an arbitrary fixed analytic profile.
- Necessity of the Brjuno condition: divergence holds on a dense $G_\delta$ of non-Brjuno parameters (Theorem C*), and
  at every $\delta$ with infinitely many prime-center approximations $|\delta-a/p|<p^{-\tau p^2}$, $\tau>dB\pi^2/6$
  (Theorem Q, Section 10.4), but whether every non-Brjuno $\delta$ gives divergence is OPEN. The
  Brjuno class is strictly larger than every polynomial Diophantine class: after any finite continued-fraction prefix,
  the choice $a_{k+1}=2^{\lfloor\sqrt{q_k}\rfloor}$ gives a Liouville number with $\mathcal B<\infty$
  ($\log q_{k+1}\le\sqrt{q_k}\log2+\log q_k+1$, and $q_k$ grows superexponentially), so convergence holds at a dense set
  of Liouville parameters (independently confirmed).
- Non-analytic $f_1$ (finite smoothness): convergence is not expected; OPEN. For $C^\infty$ profiles Theorem S
  (Section 12.2, PROVED) still gives exterior solutions with every truncation as asymptotic
  expansion, and they have a common $C^k$ potential (Section 12.3, PROVED). A single exterior solution with the full series as asymptotic expansion (to all orders) when the series
  diverges, and $C^\infty$ regularity on one fixed exterior, are OPEN.
- Sharper radius: the proof loses a factor about $10^5$ in $A$ at $\delta=1/\sqrt5$ (observed growth constant $0.468$
  for $\sin\theta$).

## 14. The logarithmic series at rational $\delta$

Throughout, $\delta=a/b$ in lowest terms, $t=\log r$, $D=\partial_t$, $\lambda_n=(n-1)(c-1)$.

### 14.1 Ansatz and recursion

At a rational $\delta$ with an incompatible resonance the pure series does not exist (Proposition 3.2). The natural
continuation keeps the exponent lattice and lets the angular coefficients be polynomials in $t$:
$$\rho=\sum_{n\ge1}r^{p_n}F_n(t,\theta),\qquad\psi=\sum_{n\ge1}r^{P_n}G_n(t,\theta),\qquad F_1=f_1 .$$
Since $(cr\partial_r-1)(r^{p_n}H)=r^{p_n}(cD-\lambda_n)H$ and $-\Delta(r^{P}G)=-r^{P-2}((P+D)^2+\partial_\theta^2)G$,
the equations are
$$(\lambda_n-cD)F_n=Q_n:=\sum_{i+j=n}\big[(P_i+D)G_i\,\partial_\theta F_j-\partial_\theta G_i\,(p_j+D)F_j\big],$$
$$-\big((P_n+D)^2+\partial_\theta^2\big)G_n=\cos\theta\,(p_n+D)F_n-\sin\theta\,\partial_\theta F_n .$$
On polynomials, $(\lambda_n-cD)^{-1}=\sum_{h\ge0}c^hD^h/\lambda_n^{h+1}$ (a finite sum), so $F_n$ is determined. With
$F_n=\sum_jA_{n,j}(t)\sin((2j+1)\theta)$, $G_n=\sum_jB_{n,j}(t)\sin(2j\theta)$, the Poisson equation splits into
$$B_{n,j}=-\tfrac12(D+P_n+2j)^{-1}A_{n,j-1}-\tfrac12(D+P_n-2j)^{-1}A_{n,j},$$
which at $D=0$ is (B). Here $(D+s)^{-1}H=\sum_h(-1)^hD^hH/s^{h+1}$ for $s\ne0$; $P_n-2j\le-n\delta<0$ always. At a stream
resonance $P_n=-2j$ the mode equation is $D(4j-D)B_{n,j}=h_{n,j}$ (the $\sin(2j\theta)$ component of the Poisson forcing),
solved by $B_{n,j}=H_{n,j}+\int_0^t(4j-D)^{-1}h_{n,j}$ with one free constant $H_{n,j}=B_{n,j}(0)$ (the coefficient of
the exterior multipole $r^{-2j}\sin(2j\theta)$). There are no other free constants: $r^{-2j}t^k\sin(2j\theta)$ is not
harmonic for $k\ge1$. The canonical normalization is $H_{n,j}=0$, i.e. $B_{n,j}(0)=0$, at every resonance; this is
the normalization used in all computations and in the confirmed exact data. (This normalization depends on the
unit of length, since $t\mapsto t+\log\lambda$ under dilation; the family of all choices is invariant.) The potential
$\chi$ is recovered as in Section 2.3, with extra powers of $t$ at the exceptional potential orders; one extra power is
not always enough: at $q=0$ the density $r^{-3}\sin\theta$ needs $\chi=((\log r)^2+\log r)/4$, and no potential with a single
logarithm produces it (independently confirmed; this happens at order 9 for $\sin\theta$ at $\delta=4/9$). Density and
stream are unaffected. Formal existence
to all orders is independently confirmed, and the potential identities and the exact stationary coefficients were checked
independently in exact Cartesian arithmetic through the first logarithmic orders at $\delta=4/9,1/2,2/5$ (exact finite
identities, PROVED; independently confirmed).

### 14.2 Degree bounds (PROVED; independently confirmed)

Let $n_r=2b/\gcd(a,2)$ (the resonance period: $n\delta\in2\mathbb Z$ iff $n_r\mid n$), $h=a/\gcd(a,2)$, and
$\varepsilon=1$ if $h=1$ (then the first multiple $n=n_r$ has $n\delta=2$, which is not a stream resonance), $\varepsilon=0$
otherwise. Then
$$\deg_tF_n\le\kappa_n:=\max\big(0,\lfloor(n-1)/n_r\rfloor-\varepsilon\big),\qquad
\deg_tG_n\le\eta_n:=\max\big(0,\lfloor n/n_r\rfloor-\varepsilon\big).$$
Proof: the density inverse and the nonresonant Poisson inverses preserve the $t$-degree, a resonant inverse raises it by
one, and $\eta_i+\kappa_j\le\kappa_{i+j}$. For $\delta=4/9$: $\deg_tF_n\le\lfloor(n-1)/9\rfloor$. For $f_1=\sin\theta$ both bounds are attained at
every order $2\le n\le160$ at $\delta=2/3,1/2,4/9$, and the density bound at every computed order, through 290 at
$\delta=2/3$, 320 at $4/9$ and 300 at $1/2$ (numerical computation of Section 14.6, item 1).

### 14.3 Gevrey bound (PROVED; independently confirmed; complete proof in Appendix B)

For a polynomial $H=\sum_kt^kh_k$ put $\|H\|_{!,s}=\sum_kk!\,s^k\|h_k\|_{\ell^1}$. Then $\|DH\|_{!,s}\le s^{-1}\|H\|_{!,s}$
and $\|\int_0^tH\|_{!,s}=s\|H\|_{!,s}$, so with $s=4b$ every Poisson inverse is bounded (each nonzero $P_n\pm2j$ has
modulus $\ge1/b$) and $\|G_n\|_{!,s}\le4b\|F_n\|_{!,s}$; the density inverse has norm $\le2/\lambda_n$. Products lose a
binomial: $\|UV\|_{!,s}\le\binom{e+d}{e}\|U\|_{!,s}\|V\|_{!,s}$ for degrees $e,d$. Normalizing by $\kappa_n!$, $\eta_n!$
removes the binomial (because $\eta_i+\kappa_j\le\kappa_{i+j}$), and a Catalan majorant gives, for a finite profile with
top frequency $L$, $B=L+1$,
$$\|F_n\|_{!,4b}\le\frac{\kappa_n!}{n}\|f_1\|_{\ell^1}\big(8C\|f_1\|_{\ell^1}\big)^{n-1},\qquad C=\frac{56bB}{c-1},$$
and the analogue for analytic profiles with $C_{\rm an}=(32+48\sigma_0)be^{\sigma_0}/(c-1)$ and a strip loss
$(\sigma_0-\sigma)^{-(n-1)}$. Since $\kappa_n\approx n/n_r$, this is a Gevrey bound of order $1/n_r$ in the order index.

### 14.4 Why the proof of Theorem A does not extend

(a) Factorial amplification by fixed divisors. $(D+s)^{-1}t^K=\sum_{\ell\le K}(-1)^\ell\frac{K!}{(K-\ell)!}\frac{t^{K-\ell}}{s^{\ell+1}}$,
whose constant coefficient is $(-1)^KK!/s^{K+1}$. At rational $\delta$ the nonzero divisors $s=2(j+1)-n\delta$ take values
in $\frac{\gcd(a,2)}b\mathbb Z$ and the small ones recur at every order, so a lower bound $|s|\ge1/b$ does not prevent
factorial growth of the inverse on polynomials of growing degree. In the plain coefficient norm
$\sum_k\|h_k\|\rho^k$ products are lossless but the inverse loses $K!$; in the factorial norm the inverse is bounded but
products lose binomials. The total binomial loss along an interaction tree is the number of ways to interleave the
resonant nodes (linear extensions of the tree order restricted to resonant nodes), at most $\kappa_n!$; it is of that size
for "caterpillar" trees in which resonant subtrees are attached one after another along a spine.

(b) Weighted sup norms in $t$. With $\|H\|=\sup_{t\ge0}|H(t)|e^{-\nu_n t}$ and superadditive $\nu_n$ (e.g. $\nu_n=\mu\kappa_n$
or $\mu n$) products are lossless and the density inverse, $F(t)=c^{-1}\int_t^\infty e^{-\lambda_n(u-t)/c}Q(u)\,du$, is
bounded for $\nu_n<\lambda_n/c$. A Poisson mode with $0<s<\nu_n$ is not controlled: its polynomial solution
$B(t)=\int_{-\infty}^te^{-s(t-u)}A(u)\,du$ depends on $A$ on $t<0$. The homogeneous solutions $e^{-st}$ discarded by the
polynomial normalization are exactly the exterior multipoles $r^{P_n-s}=r^{-2j}$, so this difficulty is the same as the
choice of multipole content in Section 12.

(c) Free constants. Convergence cannot hold for every choice of the free constants: choosing $|H_{n,j}|$ larger than
$e^{n^2}$ and larger than twice the weighted coefficient sum of the forced part of $B_{n,j}$ makes the stream terms
unbounded at every fixed $r$. The convergence question is therefore about a specific normalization; the canonical one
($H=0$) is the natural candidate. A different normalization can be better: at $\delta=2/3$, for profiles with $O_6=0$,
Theorem T (Section 12.4, PROVED) chooses the constants so that no logarithm appears in the density and stream series
(the common potential still needs the terms $r^2\log r\,(\alpha+\beta\cos2\theta)+\lambda\log r$ of Proposition T.5), and the resulting pure series
converges, while for the explicit profiles of Corollary T.3 the canonical normalization is obstructed at order 9.

(d) A linear warning example. For $(z\partial_z-qw\partial_w+\xi-1)U=z/(1-z^qw\log z)$ with $q\in\mathbb N$, $\xi>0$, the
polynomial-log solution $U=\sum_kz^{qk+1}w^ku_k(\log z)$ has $u_k'+\xi u_k=t^k$, so
$u_k(t)=(-1)^kk!\xi^{-k-1}\sum_{j\le k}(-\xi t)^j/j!$, which diverges factorially at every fixed $t$. This shows that
Fuchsian structure alone does not give convergence of polynomial-log series; it is not an IPM example. The IPM
nonlinearity has extra cancellations (e.g. the sum-frequency coefficient $\frac12(P_i\ell-p_jm)$ of the product of modes
$\sin(m\theta)$ of $G_i$ and $\sin(\ell\theta)$ of $F_j$ vanishes when $P_i=-m$, $p_j=-\ell$), which absolute majorants
discard.

(e) Standard singular-PDE theorems do not apply directly (hypothesis check, independently confirmed). In $z=r^{-\delta}$,
$E=z\partial_z$, with $\rho=r^\gamma F(z,\theta)$, $\psi=r^{\gamma+1}G(z,\theta)$, the equations read
$-(c-1)EF+z\big[((\gamma+1-\delta E)G)F_\theta-G_\theta((\gamma-\delta E)F)\big]=0$ and
$-\big[(\gamma+1-\delta E)^2+\partial_\theta^2\big]G=(\gamma-\delta E)\cos\theta\,F-\sin\theta\,F_\theta$. Solved for $E^2G$, the
right side contains $-\delta^{-2}G_{\theta\theta}$ with a coefficient that does not vanish at $z=0$, and the stream
indicial exponents $(\gamma+1\pm2j)/\delta$ are unbounded (the plus branch on the lattice $s=n-1$ is exactly the
resonance $n\delta=2(j+1)$). So condition C2(iii) of Theorem 4.1 of H. Tahara and H. Yamane (Logarithmic singularities
of solutions to nonlinear partial differential equations, J. Math. Soc. Japan 60 (2008), 603-630) and assumption A3 of
Theorem 2 of H. Tahara (Solvability of partial differential equations of nonlinear totally characteristic type with
resonances, J. Math. Soc. Japan 55 (2003), 1095-1113) fail. After the change $x=e^{i\theta}$ the principal symbol of the
Poisson block, divided by its radial coefficient, is $\lambda^2-\delta^{-2}\nu^2$, with the positive root $\lambda=1/\delta$ at
$\nu=1$, so condition (P) of the 2003 theorem fails as well. The Poisson symbol $C(n,q)=(2-n\delta)^2-q^2$ (positive even $q$)
also has no quadratic lower bound away from its exact resonances: at $\delta=2/3$ the pairs $n=3k+2$, $q=2k$ give
$P_n+q=2/3$ and $|C(n,q)|/(n+q+1)^2=(8k/3-4/9)/(5k+3)^2\to0$. This rules out only these direct applications (PROVED:
independent proof, reviewed here, for the algebraic statements; the hypotheses are as stated in the two papers).

(f) Analytic inputs and the support bounds do not suffice (PROVED: independent proof, reviewed here). Let $\delta=a/b$ in
lowest terms, $g=\gcd(a,2)$, $h=a/g$, $q_0=2b/g$, $f_1=\sin\theta$, and for $k\ge1$ let $n_k=q_0(k+1)+2$, $m_k=2h(k+1)-1$.
Prescribe the arbitrary densities $F_{n_k}=t^k\sin(m_k\theta)$ and $F_n=0$ at the other orders $n\ge2$. They satisfy the
sharper degree bound of Section 14.2, the frequency bound $m_k<2n_k-1$ and $M_n\le1$, and the density
$U=zF_1+z^{q_0+2}\sum_{k\ge1}w^k\sin(m_k\theta)$, $z=r^{-\delta}$, $w=z^{q_0}t$, is holomorphic near $(z,w)=(0,0)$ on a complex
angular strip. The canonical Poisson inverse sends the mode $m_k$ to the stream mode $m_k+1$ through the nonresonant shift
$P_{n_k}+m_k+1=2-2\delta$, with output $-\frac12(\partial_t+2-2\delta)^{-1}t^k$, whose constant term is
$\frac12(-1)^{k+1}k!/(2-2\delta)^{k+1}$; so $N_{n_k}^{1/n_k}\to\infty$. An analytic logarithmic lift together with the support
bounds therefore cannot give the uniform inverse estimate that a Fuchsian argument would need; a proof has to use the
recursion itself, as in (d).

### 14.5 Sufficient criteria for convergence

Let $M_n=\sum_k\|f_{n,k}\|_{\ell^1}$ and $N_n=\sum_k\|g_{n,k}\|_{\ell^1}$, where $F_n=\sum_kt^kf_{n,k}$,
$G_n=\sum_kt^kg_{n,k}$.

(a) Plain sums. If $M_n\le CA^n$ then, with the degree bound,
$\sum_n r^{-\delta(n-1)}\sup_\theta|F_n(\log r,\theta)|\le C\sum_nA^nr^{-\delta(n-1)}\max(1,\log r)^{n/n_r}<\infty$ for all
large $r$, and the density converges with all derivatives. Conversely absolute convergence of the individual log terms at
one $r>e$ forces an exponential bound on $M_n$. A bound on $M_n$ alone does not control the stream (independently
confirmed counterexample, not a solution of the recursion): at $\delta=4/9$ the density family
$F_{9k+8}=t^k\sin((4k+1)\theta)$ has $M_n\le1$ and the degree bound, but its nonresonant stream mode $j=2k+1$ has divisor
$P_n+2j=4/9$ and equals $-\frac12(D+\frac49)^{-1}t^k$, whose value at every fixed $t$ grows like $k!(9/4)^{k+1}$. So the
convergence criterion in plain sums needs $N_n\le CA^n$ as well on general admissible inputs; on the generated sequence
the density bound implies it (Section 14.19).

Proposition 14.5 (the joint criterion is sufficient; PROVED: independent proof, reviewed here and independently confirmed). For any fixed choice of the
resonant constants, if $M_n\le CA^n$ and $N_n\le CA^n$ for all $n$, then the density, stream and potential series and all
their weighted Cartesian derivatives converge absolutely and uniformly on $r\ge R$ for every $R>e$ with
$AR^{-\delta}(\log R)^{2/n_r}<1$, and the sum is an exact exterior solution. The potential is controlled order by order:
for $X=n\delta\ge20$ there is a potential $C_n$ producing $F_n$ and $G_n$, of log degree $\le n/n_r$, with
$$\|C_n\|_*\le\frac{432}{(n\delta)^2}\Big[M_n+n\big(B+\tfrac32\delta\big)N_n\Big],\qquad\|H\|_*=\sum_k\|h_k\|_{\ell^1}.$$
Proof. With $q=4-X$ and $Y=\partial_y\chi=r^{q-1}V$ one has $Y_x=\psi$, $-\Delta Y=\rho$, and the Euler identity
$E(E-1)Y=(x^2-y^2)\psi_x+2xy\psi_y-y^2\rho$ ($E=x\partial_x+y\partial_y$), i.e.
$(q-1+D)(q-2+D)V=\cos\theta\,(P_n+D)G_n+\sin\theta\,\partial_\theta G_n-\sin^2\theta\,F_n$. On polynomials of degree
$K\le n/n_r\le X/2$ the operator $D$ has norm $\le K$, so for $X\ge20$ both factors have Neumann inverses of norm
$\le4/X$, and $\|V\|_*\le16X^{-2}[M_n+n(B+\frac32\delta)N_n]$ (no small divisor occurs). Next, $\partial_y(r^qC)=r^{q-1}\mathcal Y(q)C$
with $\mathcal Y(q)C=q\sin\theta\,C+\cos\theta\,\partial_\theta C$ on cosine series $C=\sum_mc_m\cos2m\theta$; with $x=-q/2$ the
inverse $T(q)=\mathcal Y(q)^{-1}$ is given by the triangular system $-v_0=2xc_0+(1-x)c_1$, $-v_m=(m+x)c_m+(m+1-x)c_{m+1}$, and for $\operatorname{Re}x\ge\frac12$,
$|m+1-x|\le|m+x|$ gives $\|T(q)\|\le3$, analytic in $q$ on $\operatorname{Re}q\le-1$. Cauchy's estimate on the disc of radius
$s=\frac34(X-5)$ about $q$ bounds the Taylor coefficients by $3s^{-h}$, and $K/s\le\frac89$ for $X\ge20$, so
$C_n=\sum_{h\le K}T_hD^hV$ (where $T(q+z)=\sum_hT_hz^h$) satisfies $\partial_y(r^qC_n)=Y$ and $\|C_n\|_*\le27\|V\|_*$. Summation: for $t=\log r\ge1$ the
log factors are at most $t^{n/n_r}\le t^{2(n-1)/n_r}$, and $r^{-\delta}(\log r)^{2/n_r}$ is nonincreasing for $r\ge e$ since
$\delta n_r\ge2$; derivatives cost polynomial factors in $n$; finitely many low orders (which may carry extra logarithms,
Section 14.1) are smooth on $r\ge R$. $\square$

(b) Factorial norm (PROVED). A geometric bound $\|F_n\|_{!,4b}\le CA^n$ is sufficient for everything: Section 14.3 bounds the
polynomial-log Poisson inverse uniformly in this norm, so $\|G_n\|_{!,4b}\le4bCA^n$, and the plain sums are dominated by
the factorial norm, so Proposition 14.5 applies. The same two steps, written out with explicit constants, are steps
(iv) and (v) of the proof of Proposition 14.14. One sufficient route, still OPEN, is to replace $\kappa_n!$ in Section 14.3 by a geometric
factor (in either form (a) or (b)); the alternative is to show that factorial growth occurs. Section 14.15 shows that factorial-norm
growth would not by itself imply divergence, and reports certified data in which the factorial norms grow at
$\delta=2/3$ while the plain sums stay geometric; so form (a) is the more promising target there.

### 14.6 Numerical evidence (canonical normalization, $f_1=\sin\theta$)

Implementation and checks. The recursion of Section 14.1 is implemented with complex Fourier modes times powers of $t$,
with an angular band that grows with the order (density band $2n-1$ at order $n$; Section 14.8 explains why a fixed band
would give a false impression). The double-precision version reproduces 478 independently computed exact coefficients at
$\delta=4/9,1/2,2/5$ to relative error $6\cdot10^{-14}$, and its highest log column at $\delta=2/3$ agrees with the exact
cycle of Proposition 14.7 at every order $7\le n\le320$ to $1.3\cdot10^{-13}$. An extended-precision version (64-bit
mantissa) was run at $\delta=2/3$ to order 290. An independent 512-bit ball-arithmetic computation agrees with these
columns at $\delta=2/3$ through order 180, with every tabulated value at $\delta=2/3$ through order 290, and with the
columns at $\delta=4/9$ through order 260. It reproduces the interior factorial maximum of item 3 below through order 290; at order 180 every stored ball at
$\delta=2/3$ has relative radius below $10^{-70}$ (a statement about order 180 only; a stream ball at order 179 has
relative radius about $9\cdot10^{-70}$), and through order 245 every individual ball has relative radius below
$1.4\cdot10^{-40}$ (independently audited). All values below are for unit amplitude; $c_k=\|f_{n,k}\|_{\ell^1}$,
$F_n=\sum_kt^kf_{n,k}$, $M_n=\sum_kc_k$, and similarly $N_n$ and $g_{n,k}$ for the stream.

Ball-arithmetic coverage at $\delta=2/3$. The computation runs in 512-bit ball arithmetic; the independent audits decode
its stored balls exactly and re-enclose them at 640 bits. Every density and stream coefficient ball through order 290 is
resolved, with largest individual relative radius below $3.4\cdot10^{-30}$ through order 270, $5.3\cdot10^{-26}$ through
280, and $1.5\cdot10^{-21}$ (density) and $1.2\cdot10^{-20}$ (stream) through 290. Certified independently from these
balls: the factorial-column maxima of item 3 at orders 180, 240, 260, 270, 280 and 290, and the plain sums through 290;
the Poisson equation, with zero canonical constants, for every stored stream coefficient through 290; the full
nonlinear recurrence at orders 240 and 290; the fixed-$t$ values of item 6 at $t=0,\pm20,\pm40$ at selected orders from
220 to 290; the signed Poisson sums of item 7 at orders 250, 260, 263, 265 and 268; and the mass partitions of item 7
at selected orders from 240 to 290. "Ball arithmetic" below refers to these data.

Conditioning at $\delta=2/3$. The nonzero divisors satisfy $|P_n+2j|\ge2/3$, so $(D+s)^{-1}$ sends $t^K$ to a constant
term of size up to $K!\,1.5^{K+1}$, and the low log columns are obtained by cancellation: $\|F_n\|_{!,1.5}/c_0$ is $10^{0.8}$
at $n=160$, $10^{4.2}$ at 200, $10^{11.3}$ at 260 and $10^{14.0}$ at 280. Double and extended precision agree on every
density column to $2\cdot10^{-14}$ in $\log_{10}$ through order 180, to $1.4\cdot10^{-5}$ at 260, $10^{-3}$ at 280 and
$0.15$ at 290. The extended-precision errors are expected to be about $2^{-11}$ times the double ones, so the
extended data are used through order 290, which is the end of the reliable range.

Density (per-order increments of $\log_{10}$ averaged over the preceding 20 orders):

| $\delta$ | $n$ | $\kappa_n$ | $M_n^{1/n}$ | $c_0^{1/n}$ | incr. $c_0$ | incr. $\|F_n\|_{!,1}$ | incr. $\|F_n\|_{!,4b}$ | $\max_{k\ge1}\log_{10}(k!\,c_k/c_0)$ |
|---|---|---|---|---|---|---|---|---|
| 2/3 | 40 | 12 | 0.1775 | 0.1768 | -0.7267 | -0.7250 | -0.6103 | -0.91 ($k=1$) |
| 2/3 | 80 | 25 | 0.1854 | 0.1850 | -0.7099 | -0.7096 | -0.4837 | -0.86 ($k=1$) |
| 2/3 | 160 | 52 | 0.1909 | 0.1907 | -0.7048 | -0.7042 | -0.3576 | -0.72 ($k=1$) |
| 2/3 | 200 | 65 | 0.1923 | 0.1921 | -0.7039 | -0.7030 | -0.3443 | -0.66 ($k=1$) |
| 2/3 | 240 | 78 | 0.1933 | 0.1930 | -0.7033 | -0.6728 | -0.3037 | -0.24 ($k=42$) |
| 2/3 | 260 | 85 | 0.1937 | 0.1934 | -0.7029 | -0.6296 | -0.3094 | 1.36 ($k=46$) |
| 2/3 | 280 | 92 | 0.1940 | 0.1938 | -0.7025 | -0.6172 | -0.2936 | 3.04 ($k=50$) |
| 2/3 | 290 | 95 | 0.1942 | 0.1939 | -0.7022 | -0.6106 | -0.2953 | 3.94 ($k=57$) |
| 1/2 | 40 | 8 | 0.3296 | 0.3296 | -0.4436 | -0.4436 | -0.4432 | -2.59 ($k=1$) |
| 1/2 | 80 | 18 | 0.3501 | 0.3501 | -0.4273 | -0.4273 | -0.4270 | -2.34 ($k=1$) |
| 1/2 | 120 | 28 | 0.3589 | 0.3588 | -0.4231 | -0.4231 | -0.4151 | -2.18 ($k=1$) |
| 1/2 | 160 | 38 | 0.3638 | 0.3638 | -0.4210 | -0.4209 | -0.3397 | -2.06 ($k=1$) |
| 4/9 | 40 | 4 | 0.4027 | 0.4027 | -0.3530 | -0.3530 | -0.3529 | -3.45 ($k=1$) |
| 4/9 | 80 | 8 | 0.4296 | 0.4296 | -0.3363 | -0.3363 | -0.3362 | -3.19 ($k=1$) |
| 4/9 | 160 | 17 | 0.4475 | 0.4475 | -0.3301 | -0.3301 | -0.3300 | -2.91 ($k=1$) |
| 4/9 | 240 | 26 | 0.4545 | 0.4545 | -0.3283 | -0.3283 | -0.3282 | -2.74 ($k=1$) |
| 4/9 | 320 | 35 | 0.4584 | 0.4584 | -0.3273 | -0.3273 | -0.3272 | -2.62 ($k=1$) |

Here $4b=12$ at $\delta=2/3$, $8$ at $1/2$ and $36$ at $4/9$; the rows at $2/3$ use the extended-precision data.

Stream at $\delta=2/3$ (extended precision; increments averaged over 18 orders, which keeps the residue class mod 3):

| $n$ | $N_n^{1/n}$ | incr. $N_n$ | $\max_{k\ge1}\log_{10}(k!\,\|g_{n,k}\|/\|g_{n,0}\|)$ |
|---|---|---|---|
| 160 | 0.1852 | -0.6974 | -0.39 ($k=1$) |
| 200 | 0.1871 | -0.7074 | -0.42 ($k=1$) |
| 240 | 0.1886 | -0.7055 | -0.40 ($k=1$) |
| 260 | 0.1894 | -0.7044 | 1.00 ($k=46$) |
| 280 | 0.1906 | -0.6786 | 2.29 ($k=50$) |
| 290 | 0.1917 | -0.6723 | 2.65 ($k=54$) |

Findings, each a finite-order observation under the stated conditions.
1. The $t$-degree equals the bound $\kappa_n$ of Section 14.2 at every computed order (to 290 at $2/3$, 320 at $4/9$,
   300 at $1/2$).
2. The density plain sums decay geometrically over the whole computed range: at $2/3$ the 20-order mean increment of $\log_{10}c_0$
   drifts slowly upward, from $-0.7042$ (window ending at order 180) through $-0.7039$ (200), $-0.7035$ (220),
   $-0.7033$ (240) and $-0.7029$ (260) to $-0.7022$ (290), i.e. ratio about $0.198$ per order; it is
   $-0.327$ at $4/9$ ($0.471$) and $-0.421$
   at $1/2$ ($0.379$), and $M_n$ stays within a factor $1.4$ of $c_0$.
3. At $2/3$ the factorial profile develops an interior maximum. For $n\le230$ the maximum of $k!\,c_k/c_0$ over $k\ge1$ is
   at $k=1$ and below one; from $n\approx235$ a maximum near $k\approx0.55\kappa_n$ takes over and grows by about $0.085$
   decades per order. Double and extended precision agree on it to $0.01$ through order 280, and the ball-arithmetic
   computation confirms it with certified enclosures: the maximum over $k\ge1$ moves to an interior degree at $n=235$
   ($k=40$), first exceeds the constant column at $n=244$ ($k=40$, $\log_{10}$ ratio $0.0709$), and is $0.543$ at
   $n=250$ ($k=44$), so the interior maximum is not roundoff (independently audited; see the coverage paragraph above). It
   is invisible in the plain sums ($c_{57}/c_0\approx10^{-73}$ at $n=290$). No interior maximum occurs through 320 at $4/9$
   or through 300 at $1/2$ (512-bit ball arithmetic at every order; at $1/2$ the maximum over $k\ge1$ of
   $\log_{10}(k!\,c_k/c_0)$ stays at $k=1$ and rises slowly, to $-1.80$ at $n=300$, while the columns $k=40,50,60$ rise, to
   $-26.3,-28.5,-35.1$ at $n=300$, so a later interior maximum is not excluded; $M_{300}^{1/300}=0.3716$). These are finite
   observations.
4. At $2/3$ the stream plain sums, dominated by $g_{n,0}$, grow at the density rate through order 262 and faster from
   about 263 on, while the stream profile develops the same interior maximum. With $L(n)=\log_{10}$ of the plain stream
   sum (amplitude one), the 9-order increment $[L(n)-L(n-9)]/9$ lies between $-0.717$ and $-0.688$ for $150\le n\le262$
   (mean slope $-0.7057$ over $200\le n\le262$, density $-0.7029$), and between $-0.700$ and $-0.666$ for $263\le n\le290$
   (mean slope $-0.6615$ over $270\le n\le290$, density $-0.7015$). Ball arithmetic confirms the extended-precision
   values to four decimals where both exist: $-0.7116$ at 180, $-0.7006$ at 230, $-0.7005$ at 250, and
   $-0.6933,-0.6949,-0.6998,-0.6795,-0.6877,-0.6933,-0.6714,-0.6840$ at $263,\dots,270$. The ball run also shows the
   stream maximum over $k\ge1$ becoming interior at 242 and exceeding the constant column from 248 on; at 270 the
   density and stream factorial maxima are at $k=48$, $2.155$ and $1.701$ decades above the constant columns, and at
   280 both are at $k=50$, $3.040$ and $2.291$ decades above, and at 290 at $k=57$ and $k=54$, $3.940$ and $2.646$ decades
   above (ball arithmetic, all coefficient balls resolved).
5. The factorial norm with $s=4b$ grows at the plain rate at $4/9$ through 320, consistent with criterion (b) of
   Section 14.5. At $2/3$ its increments rise from $-0.61$ ($n=40$) to $-0.36$ (160) and $-0.29$ to $-0.31$ (240 to 290);
   at $1/2$ from $-0.44$ (40) to $-0.34$ (160). A factor $(\kappa_n!)^\alpha$ would raise the increments like
   $(\alpha/n_r)\log_{10}n$; between orders 200 and 290 the $2/3$ data are compatible with $\alpha$ near one and also with a
   geometric rate that is still converging. The unweighted factorial norm $\sum_kk!\,c_k$ ($s=1$, amplitude one,
   extended precision) has 9-order mean increments $-0.705\pm0.001$ for windows ending at $150\le n\le210$, then
   $-0.697$ (220), $-0.683$ (230), $-0.659$ (240), $-0.636$ (250), $-0.625$ (260), $-0.619$ (270), $-0.614$ (280) and
   $-0.610$ (290), while $c_0$ stays at $-0.703$. The changes per 10 orders, $0.0104,0.0063,0.0049,0.0044$ from 250 to
   290, are close to the $1.45/n\approx0.0051$ to $0.0057$ that a factor $(n!)^{1/3}$ would give and are also compatible
   with a transient that is dying out; near order 350 the two would differ clearly ($0.0042$ against much less).
6. Fixed $t=\log r$. Evaluate $F_n(t,\cdot)$ and $G_n(t,\cdot)$ at $t\in\{0,\pm1,\pm2,\pm5,\pm10,\pm20,\pm40\}$ (extended
   precision through order 260; an independent interval evaluation of the ball-arithmetic coefficients agrees with
   these values to $2\cdot10^{-10}$ in $\log_{10}$ at $n=180,190,200,209,210$ for all thirteen $t$ and both fields; a
   separate 512-bit ball evaluation at $t=\pm20,\pm40$ for $n=220,240,250,255$, with certified radii 40 decades below the
   values (and later evaluations from 260 to 290 with relative radii below $10^{-22}$), reproduces the extended-precision increments; a double-precision rerun agrees with extended precision at
   $n=260$ to $10^{-5}$ for the density at $|t|\le20$ and to $2\cdot10^{-3}$ for the stream at $|t|\le10$, in $\log_{10}$). The
   18-order mean increment of $\log_{10}\|F_n(t,\cdot)\|_{\ell^1}$ for $140\le n\le260$ lies between $-0.706$ and $-0.698$
   for $|t|\le10$, with the slow drift of $c_0$ ($t=0$: $-0.7056$ at 140, $-0.7043$ at 180, $-0.7034$ at 240, $-0.7029$ at
   260); it is between $-0.6950$ and $-0.6913$ at $t=20$, between $-0.692$ and $-0.689$ at $t=-20$, between $-0.673$ and
   $-0.670$ at $t=40$ and between $-0.67$ and $-0.65$ at $t=-40$ (for $|t|=40$ only orders $\le220$ are used from extended precision; the ball values give $-0.671$ and
   $-0.637$ for $240\to250$ and $-0.654$ and $-0.704$ for $250\to255$ at $t=40$ and $t=-40$; from 260 to 280 the ball values give mean increments
   $-0.687,-0.683,-0.673,-0.675$ per order at $t=20,-20,40,-40$, and from 280 to 290 $-0.698,-0.675,-0.672,-0.673$). The stream
   behaves alike with more scatter (increments $-0.70$ to $-0.71$ for $|t|\le5$). These values arise from strong
   cancellation between log columns: $\log_{10}(\sum_k|t|^kc_k/\|F_n(t,\cdot)\|_{\ell^1})$ at $n=260$ is $0.07$ at $t=1$,
   $0.69$ at $t=10$ and $3.79$ at $t=20$, and at $n=210$, $t=40$ the interval values are $8.14$ (density) and $7.53$
   (stream). Because of this cancellation and the column accuracy stated under Conditioning, the extended-precision $|t|=40$
   values are not used beyond order 220; the ball values (cancellation 9.5 decades at 240 and 10.0 at 255) are certified. So at each tested $t$ the coefficients of the series in $z$ at fixed $\log r$ decay
   geometrically through the computed orders, with a rate that depends weakly on $t$: in this range $\|F_n(t,\cdot)\|$
   behaves like $A^ne^{\epsilon n|t|}$ with $\epsilon$ about $0.002$. A bound $\|F_n(t)\|,\|G_n(t)\|\le CA^ne^{\epsilon n|t|}$
   for all $n$ and $t\ge0$ with some $\epsilon<\delta$ would give convergence of the density and stream sums for large $r$
   (the $t$-derivatives of these polynomials of degree $\le n/3$ cost polynomial factors by Markov's inequality); no such
   bound is proved, and these data do not give one.
7. The Poisson step at the diagonal. For the density mode $a(t)\sin m\theta$ nearest the diagonal (offset
   $s=m+3-n\delta=\pm2/3$, the smallest nonzero modulus at $\delta=2/3$) the upward stream channel is
   $-\frac12(\partial_t+s)^{-1}a$, whose constant term is $-\frac12\sum_h(-1)^hh!\,a_hs^{-h-1}$. In the extended-precision
   data ($f_1=\sin\theta$; orders $n=80,140,160,200,220,260$, with $s=+,+,-,+,-,+\,2/3$) this signed sum reproduces the
   computed stream constant coefficient at frequency $m+1$ to $10^{-3}$ in $\log_{10}$. The coefficientwise absolute
   bound $\frac12\sum_hh!\,|a_h|\,|s|^{-h-1}$ exceeds that coefficient by $0.45,1.20,1.19,3.36,4.46,7.74$ decades, while
   $\frac12\sum_hh!\,|a_h|/|s|$ exceeds it by only $0.28,0.29,0.06,0.75,0.11,1.17$ decades; the difference between the two
   is the factor $|s|^{-h}\le(3/2)^h$, which is geometric in the order. Summed over all modes, the absolute bound exceeds
   the stream constant column by $2.48$ decades at $n=200$ and $6.85$ at $n=260$, and more than $99\%$ of the excess comes
   from this one mode. At $n=200$ and $260$ the stream constant at this mode is even below the plain norm
   $\sum_h|a_h|$ of its input (by $0.71$ and $0.32$ decades); this is not uniform, since at $n=263$ it exceeds it by
   $0.37$ decades (ball arithmetic, which also confirms the values at 260). So in these data the Poisson step at the diagonal does not
   realize the factorial loss of Proposition 14.11(c), and a pointwise bound through
   $(\partial_t+s)^{-1}a(t)=\int_0^\infty e^{-s\tau}a(t-\tau)\,d\tau$ ($s>0$) is within $0.5$ decades of the actual value
   for $n\le220$ (3.5 decades at 260). The Poisson and stationary inverses cost only fixed factors in the weighted
   factorial norm (Section 14.3), and in these samples the diagonal Poisson step is within $1.2$ decades of the
   factorial norm of its input. This points to the products as the source of the growth of the interior maximum of
   item 3; it is a reading of finite data, not a proof, and it does not exclude growth from the linear steps at other
   orders. An independent interval partition of the Fourier mass at orders 240 to 280 puts more than $99.6\%$ of the
   mass of the maximizing interior column (density and stream) at modes with $|s|>q$, that is, far from the diagonal
   (at 270, $q=48$: $99.991\%$ density, $99.873\%$ stream; at 280, $q=50$: $99.995\%$ density, more than $99.93\%$
   stream). Almost all of it lies below the diagonal ($s<-q$, lower
   frequencies); the fraction with $s>q$ is below $10^{-9}$ at 260 and 270. The near-diagonal mass sits instead in the
   low log columns of the stream (at $10\le q\le30$, 16 to 54 percent of their mass within $|s|\le q/4$ at orders 240 to 280; in the constant stream column this near-diagonal share grows with the order: $0.12$ at 240, $0.47$ at 280, $0.81$ at 290), and the highest columns lie on the diagonal, as
   Proposition 14.7 requires.

Reading. Through the computed orders the data at $4/9$ are consistent with both sufficient criteria of Section 14.5;
at $2/3$ and $1/2$ the factorial criterion is not visible in the data (which is not evidence of divergence, since that
criterion is only sufficient), and at $2/3$ the joint plain criterion holds for the density through 290 but the stream
changes its growth near order 263. This is NUMERICAL EVIDENCE of finite-order behavior only; it does not decide the
convergence of the canonical logarithmic series, which remains OPEN. An independent exact rational computation at
$\delta=4/9$ to order 73 gives $\max_k\|f_{n,k}\|^{1/n}=0.4267$ at $n=73$.

### 14.7 The highest log degree at $\delta=2/3$ (PROVED: independent proof, audited and independently confirmed)

Proposition 14.7. Let $\delta=2/3$ ($c=3$, $n_r=3$, $\varepsilon=1$), $f_1=\sin\theta$, canonical normalization, so that
$\kappa_n=\max(0,\lfloor(n-1)/3\rfloor-1)$, $\eta_n=\max(0,\lfloor n/3\rfloor-1)$. For $k\ge2$,
$[t^{k-1}]G_{3k}=b_k\sin((2k-2)\theta)$, with
$$b_2=-\frac{177047}{1204224000000},\quad b_3=\frac{416591591}{16616364441600000000},\quad
\frac{b_{k+1}}{b_k}=\frac{(k-1)(2k-1)^2(8478k^4-13599k^3+507k^2+4184k-340)}{9600k^2(3k-4)(3k-2)(3k+1)(3k+2)(6k-5)(6k-1)}\ (k\ge3).$$
Hence $b_k>0$ for $k\ge3$, $((k-1)!\,|b_k|)^{1/k}\to\lambda=157/129600$, and for $r=1,2,3$ the top density coefficients
$H_{k,r}=[t^{k-1}]F_{3k+r}$ satisfy $((k-1)!\,\|H_{k,r}\|_{\ell^1})^{1/(3k+r)}\to\lambda^{1/3}=0.10660\ldots$; the same holds
for the top stream coefficients. The top-degree subseries, as a series in independent variables $z,t$, converges for all
complex $z,t$.

Proof. For $i,j\ge4$, $\lfloor i/3\rfloor+\lfloor(j-1)/3\rfloor\le\lfloor(n-1)/3\rfloor$ gives $\eta_i+\kappa_j\le\kappa_n-1$,
so the top degree $k-1$ of $F_{3k+r}$ ($r=1,2,3$) receives only the products with $i\le3$, $j\in\{3k+1,\dots,3k+r-1\}$ or
$j\le3$, $i\in\{3k,\dots,3k+r-1\}$; in them $D$ lowers the degree, so only $P_i,p_j$ enter, the density inverse acts
as division by $\lambda_n=2(n-1)$, and nonresonant Poisson inverses act on top coefficients as the scalar multipliers
of (B). At order $3k$ only the resonant mode $\sin((2k-2)\theta)$ ($P_{3k}+2(k-1)=0$) reaches degree $k-1$, through the
integration $\int_0^tt^{k-2}=t^{k-1}/(k-1)$, and the canonical constant affects only $t^0$. The top degree therefore
obeys a linear three-step cycle driven by $f_1,f_2,f_3,g_1,g_2$, which gives
$b_{k+1}=-\frac{b_k}{2k}[\sin((2k-1)\theta)]a_3(k)$ with $a_3(k)$ an explicit rational function; for $k\ge3$ no reflected
negative frequency reaches the mode $2k-1$, which gives the displayed ratio ($b_3$ includes one reflected term). The
ratio $R(k)=b_{k+1}/b_k$ (the deficit-zero transfer of Section 14.9 at $Q=3$) is positive for $k\ge3$ and $kR(k)\to4\cdot8478/(9600\cdot81\cdot36)=157/129600$. The normalized cycle profiles are
bounded rational functions of $k$ with nonzero limits, which gives the norm statements. $\square$

Checks: an exact Cartesian computation of the full logarithmic recursion through order 45 reproduces every $b_k$,
$k\le15$, and every top profile (independently confirmed); the double-precision implementation of Section 14.6
reproduces $\|[t^{k-1}]F_{3k+1}\|_{\ell^1}=|b_k|(k-1)/(3k)$ for all $k\le70$ (orders up to 211) to relative error $1.6\cdot10^{-14}$.

Meaning. In the factorial norm the top degree is harmless: there $k!\,\|[t^k]F_n\|$ decays geometrically (like $\lambda^k$ up to subexponential factors), so the
$\kappa_n!$ of Section 14.3 is not attained at the top degree. Whatever growth the canonical series has sits in the
intermediate degrees, where the data of Section 14.6 show it.


### 14.8 A fixed angular truncation always converges (PROVED: independent proof, reviewed here and independently confirmed)

Proposition 14.8. Fix $\delta\in(0,1)$, an odd $L$, $M=L+1$, a nonzero $f_1$ in the span of
$\sin\theta,\sin3\theta,\dots,\sin L\theta$, and let $\Pi_L$ be the orthogonal projection onto that span. Replace $Q_n$ in
the density equation of Section 14.1 by $\Pi_LQ_n$, keep the Poisson equation, and use the canonical normalization at
resonances. Put $\|H\|_T=\sum_qT^q\|[t^q]H\|_{\ell^1}$. Then the projected recursion is defined at every order,
$\deg_tF_n\le n-1$, $\deg_tG_n\le n$, and there are constants $T,C_P,A$ depending only on $\delta,L,f_1$ with
$$\|F_n\|_T\le\|f_1\|_{\ell^1}A^{n-1},\qquad\|G_n\|_T\le\frac{C_P}n\|f_1\|_{\ell^1}A^{n-1}.$$
The projected density and stream series converge absolutely and uniformly, with all weighted Cartesian derivatives, on
some exterior region $r\ge R$; for irrational $\delta$ every coefficient is independent of $t$ and the series in
$z=r^{-\delta}$ has a positive radius, with no arithmetic condition on $\delta$. The sum satisfies the Poisson relation
and the projected stationary equation; its unprojected stationary residual is in general nonzero.

Proof. On the stream mode $\sin(m\theta)$, $2\le m\le M$, the Poisson operator is $(m-P_n-D)(m+P_n+D)$. Since $P_n<2\le m$,
only $P_n=-m$ can resonate, which requires $n\delta=m+2\le M+2$: finitely many orders. Take $T\ge16/\delta$; then
$\|D\|\le k/T$ on polynomials of degree $\le k$, $\|\partial_\theta\|\le m$ on a band through $m$, $\|\Pi_L\|\le1$ and
$\|\cdot\|_T$ is submultiplicative. Let $N_*=\lceil4(M+2)/\delta\rceil$. For $n\ge N_*$, $|m+P_n|=n\delta-2-m\ge3n\delta/4$
and $m-P_n\ge n\delta$, while $\|D\|\le n/T\le n\delta/16$, so each factor has inverse norm at most $2/(n\delta)$; the
forcing $(p_n+D)\cos\theta F_n-\sin\theta\,\partial_\theta F_n$ costs at most $(n\delta+1+L+n/T)\le2n\delta$ because
$1+L\le n\delta/4$. Hence $\|G_n\|_T\le8\|F_n\|_T/(n\delta)$ for $n\ge N_*$. The finitely many earlier Poisson maps are
linear maps between finite-dimensional spaces, with norms $C_n$; put $C_P=\max(8/\delta,\max_{n<N_*}nC_n)$, so that
$\|G_n\|_T\le C_P\|F_n\|_T/n$ for all $n$. The density inverse has norm $\le1/((n-1)(d-c/T))\le2/((n-1)d)$, $d=c-1$, since
$c/T\le c\delta/16=d/16$. With $a=2+\delta+1/T$, $\|(P_i+D)G_i\|_T\le ai\|G_i\|_T$ and $\|(p_j+D)F_j\|_T\le aj\|F_j\|_T$,
so $X_n=\|F_n\|_T$ obeys $X_n\le K_0\sum_{i+j=n}X_iX_j$ with $K_0=4aMC_P/d$, and the Catalan majorant gives
$X_n\le F(4K_0F)^{n-1}$, $F=\|f_1\|_{\ell^1}$. For summation, $\|H(t)\|_{\ell^1}\le\max(1,t/T)^k\|H\|_T$, and for
$t=\log r\ge T$ the functions $r^{-\delta}\log r$ and $t^ne^{-\delta(n-1)t}$ ($n\ge2$) are nonincreasing, so the density
and stream terms are bounded by their values at $r=R$ for $R\ge e^T$ with $AR^{-\delta}\log R/T<1$; derivatives cost
polynomial factors in $n$. $\square$

Consequences. (1) A caution for computations. For $f_1=\sin\theta$ the full recursion has density band $2n-1$ at order
$n$, so it agrees with the projected recursion through order $n$ once $L\ge2n-1$. On the divergence set of Theorem Q
the full series has radius zero while every projection converges; hence the projected sums cannot be bounded on a
common disk in $z$ uniformly in $L$ (the individual radii need not tend to zero). A computation that holds the angular
band fixed cannot detect the small-divisor divergence. All computations reported here let the band grow with $n$.
(2) A reading for the logarithmic series (heuristic, not a theorem). Without the projection the Neumann inversion of
$D+P_n+2j$ in $\|\cdot\|_T$ still works for every stream mode with $|P_n+2j|\ge2\deg_t/T$; it fails only in the band
$|P_n+2j|<2\deg_t/T$ around $2j=n\delta-2$, of width about $4n/(n_rT)$. At rational $\delta$ the nonzero divisors in that band
are at least $1/b$, so the nonresonant part of the band is empty only if $T\gtrsim2b\deg_t\approx2bn/n_r$, a weight growing linearly in $n$; a weight
$T^q$ with $T$ of the order of the degree is the factorial weight of Section 14.3 up to exponential factors. So the difficulty in the
sufficient estimates of Section 14.5 lies in the near-resonant stream band; outside it the inversion is bounded in a fixed polynomial weight. The exact zero divisors (the resonant stream
modes) are present for every $T$; they are inverted by integration in $t$, which raises the $t$-degree by one and is
not a Neumann inversion.


### 14.9 Every fixed logarithmic deficit at $\delta=2/Q$ (PROVED: independent proofs, reviewed here and independently confirmed)

Setting. Let $Q\ge3$ be an integer, $\delta=2/Q$, $c=Q/(Q-2)$, $f_1\ne0$ a real finite odd sine polynomial, and use the
canonical normalization. The stream resonances are at $n=Qk$, $k\ge2$, on the mode $\sin(m_k\theta)$, $m_k=2k-2$
($P_{Qk}=-m_k$). The degree bounds of Section 14.2 read $\deg_tF_n\le\max(0,\lfloor(n-1)/Q\rfloor-1)$ and
$\deg_tG_n\le\max(0,\lfloor n/Q\rfloor-1)$ (for even $Q$ the reduced form of $\delta$ is $1/(Q/2)$ and the resonance
period is still $Q$). Density block $k$ consists of the orders $Qk+r$, $1\le r\le Q$, and stream block $k$ of the
orders $Qk+r$, $0\le r<Q$; on both the degree bound is $k-1$. The deficit-$d$ column of a block is its coefficient of
$t^{q}$, $q=k-1-d$.

Proposition 14.9. There is a real constant $\Lambda=\Lambda(Q,f_1)$, computed by the finite offset algorithm in step (3)
below, rational for rational $f_1$ and homogeneous of degree $Q$ in $f_1$, such that for every fixed $d\ge0$, with
$q=k-1-d$,
$$\limsup_{k\to\infty}\big(q!\,\|[t^q]F_{Qk+r}\|_{\ell^1}\big)^{1/k}\le(d+1)|\Lambda|\quad(1\le r\le Q),\qquad
\limsup_{k\to\infty}\big(q!\,\|[t^q]G_{Qk+r}\|_{\ell^1}\big)^{1/k}\le(d+1)|\Lambda|\quad(0\le r<Q).$$
Hence for each fixed $d$ the extracted series $\sum_kz^{Qk+r}t^{k-1-d}[t^{k-1-d}]F_{Qk+r}$ and its stream analogue are
entire in independent complex variables $(z,t)$, with every fixed derivative, on every bounded complex angular strip.
Values: $\Lambda=\lambda=157/129600$ for $Q=3$, $f_1=\sin\theta$ (at $d=0$ this is Proposition 14.7);
$3557/10368000$ for $Q=3$, $f_1=\sin\theta+\frac1{10}\sin3\theta$; $-9137/8429568$ for $Q=4$, $f_1=\sin\theta$;
$3575370901/5451264000000$ for $Q=5$, $f_1=\sin\theta$. No uniformity in $d$ is asserted, and nothing is asserted
about the sum over all deficits.

Proof. (1) Grading. A product of a stream child $i$ and a density child $j$ with $i+j=n=Qk+r$, both of index $>Q$, has
$\lfloor i/Q\rfloor+\lfloor(j-1)/Q\rfloor\in\{k-1,k\}$. Each term has at most one $t$-derivative ($\ell\in\{0,1\}$; the
Jacobian $r^{-1}(\psi_r\rho_\theta-\psi_\theta\rho_r)$ carries one radial derivative), so the child deficits satisfy
$a+b+\ell\in\{d-1,d-2\}$ and both are smaller than $d$. A child of index $\le Q$ has log degree $0$, and its partner lies
either in the current block (same deficit) or in the previous block (deficit $d-1-\ell$). The $\partial_t$ terms of the
density and Poisson equations use higher columns of the same coefficient, that is, smaller deficits. At $n=Qk$ the
density has degree at most $k-2$, so the nonresonant modes of $[t^{k-1-d}]G_{Qk}$ come from $F_{Qk}$ at deficit $d-1$ of
block $k-1$ (with the same factorial $(k-1-d)!$). Modulo smaller deficits, the only unknown of block $k$ at deficit $d$
is the scalar $a_{k,d}=[\sin m_k\theta]\,[t^{k-1-d}]G_{Qk}$.
(2) The cycle. Linearize the recursion about the $t$-independent low coefficients $f_j,g_j$ ($j\le Q$): starting from
$J_0=\sin m_k\theta$ at order $Qk$, compute the density $H_r$ at order $Qk+r$ by the log-free stationary formula and,
for $r<Q$, the stream $J_r$ by the ordinary nonresonant Poisson inverse. Let $K(k)$ be the coefficient of
$\sin((2k-1)\theta)$ in $H_Q$. At a resonance $P=-m$ the forcing of $\sin m\theta$ is
$\frac12(P-m)a_{m-1}+\frac12(P+m)a_{m+1}=-m\,a_{m-1}$, and the resonant column equation
$-2P(q+1)B_{q+1}=H_q+(q+1)(q+2)B_{q+2}$ with $-2P=4k$ gives
$$a_{k+1,d}=\frac{kR(k)}{k-d}\,a_{k,d}+E_{k,d},\qquad R(k)=-\frac{K(k)}{2k},$$
where $E_{k,d}$ depends only on smaller deficits. With $A_{k,d}=(k-1-d)!\,a_{k,d}$ this reads
$A_{k+1,d}=kR(k)A_{k,d}+(k-d)!\,E_{k,d}$: the homogeneous coefficient does not depend on $d$.
(3) The limit $\Lambda=\lim_kkR(k)$. Write the high profiles by offsets $s$ from $m_k$; there are finitely many,
depending on $Q$ and the bandwidth of $f_1$. The Poisson inverse at order $Qk+r$, $r<Q$, sends a density offset $s$ to
the stream offset $s+1$ with multiplier $-1/[2(s+1-2r/Q)]$, which is finite because $s$ is odd and $0<2r/Q<2$, and to
$s-1$ with a multiplier $O(1/k)$. The stationary denominator is $(Qk+r-1)(c-1)\sim cm_k$ and
$P_{Qk+i},p_{Qk+i}\sim-m_k$. So, up to $O(1/k)$, a high stream offset $s$ (amplitude $b$) times a low density mode $\ell$
(amplitude $a$, exponent $p_j$) contributes $-ba(\ell+p_j)/(2c)$ at offset $s+\ell$ and $ba(p_j-\ell)/(2c)$ at $s-\ell$, and
a low stream mode $\ell$ (amplitude $b$, exponent $P_i$) times a high density offset $s$ (amplitude $a$) contributes
$ba(P_i+\ell)/(2c)$ at $s+\ell$ and $ba(\ell-P_i)/(2c)$ at $s-\ell$. These finitely many operations give the finite limit
$\Lambda=-\frac12\lim_kK(k)$. Each path uses low orders adding up to $Q$, so $\Lambda$ is homogeneous of degree $Q$.
(4) Induction on $d$. At fixed deficit the Poisson and density inverses are triangular in the columns above the target;
the nonzero divisors are bounded below (by $2/Q$ in one factor, by a multiple of $k$ in the other), and after factorial
normalization all coefficients are polynomial in $k$, so these operations preserve $k$-th root rates. For $d=0$,
$E_{k,0}=0$ after finitely many blocks, so $\limsup_k|A_{k,0}|^{1/k}\le|\Lambda|$ (also when $\Lambda=0$). If the bound
holds for all $a<d$, with rates $\beta_a=(a+1)(|\Lambda|+\epsilon)$, then a product of deficits $a,b$ at child degrees $u,v$,
multiplied by $(u+v)!$, gives $\binom{u+v}{u}(u!\,\cdot)(v!\,\cdot)$, and the sum over all splits is at most a constant
times $(\beta_a+\beta_b)^{u+v}$, where $\beta_a+\beta_b=(a+b+2)(|\Lambda|+\epsilon)\le(d+1)(|\Lambda|+\epsilon)$. Linear terms with a
low child have smaller rates. Hence $(k-d)!\,|E_{k,d}|\le Ck^M[(d+1)(|\Lambda|+\epsilon)]^k$, and variation of constants
(eventually $|kR(k)|\le\eta$ for any $\eta>|\Lambda|$) gives the scalar bound; the block reconstruction gives the column
bounds. The extracted series are entire because their coefficients are at most $C\rho^k/(k-1-d)!$ for every
$\rho>(d+1)|\Lambda|$ and the bandwidth grows linearly in $k$. $\square$

Status. PROVED. At $\delta=2/3$, $f_1=\sin\theta$: independent proof, reviewed here and independently confirmed, with
23 exact linearized blocks verifying the transfer and its deficit-independent normalization. For general $Q$ and finite
profiles: independent proof, reviewed here and independently confirmed, including even $Q$, the low-order children and
the case $\Lambda=0$; its finite checks (exact Cartesian cycles at $k=16,32,64,128$ approaching the four values of
$\Lambda$, and 36 transfer identities) are independently confirmed. Rational $\delta$ with reduced numerator larger than 2 (for example $4/9$) have a different
degree grading and are not covered.

Data (NUMERICAL EVIDENCE of finite-order behavior; $\delta=2/3$, $f_1=\sin\theta$, extended precision, density column
norms $c_q$ of $F_{3k+r}$ through order 290). The per-block increment of $\log_{10}(q!\,c_q)$, $q=k-1-d$, averaged over the
5 blocks ending at $k=90$, is $-2.925$ for $d=0$ (against $\log_{10}\lambda=-2.917$), $-2.627$ for $d=1$ (bound
$\log_{10}2\lambda=-2.616$), $-2.454$ for $d=2$ ($-2.440$), $-2.332$ for $d=3$ ($-2.315$), $-2.162$ for $d=5$ ($-2.139$),
$-2.01$ for $d=8$ ($-1.962$) and $-1.95$ for $d=10$ ($-1.875$); the three residues $r$ agree to $0.002$ for $d\le8$. For
$15\le d\le60$ the increments are irregular, between about $-1.65$ and $-2.1$, below the bounds ($-1.71$ to $-1.13$). So
at small fixed $d$ the rate $(d+1)\lambda$ is nearly attained. At $k=90$, however, $\log_{10}(q!\,c_q)$ increases from
$-267$ at $d=0$ to a maximum of about $-191$ near $d\approx40$: the columns that matter for the full series have
deficits proportional to $k$, where Proposition 14.9 says nothing. A rate $(d+1)\lambda$ at $d=\theta k$ would make the
plain coefficients grow like $k^{\theta k}$, which the plain sums do not do through order 290; the binomial step of the
induction is far from sharp at large deficits. A deficit-uniform estimate would give one sufficient route.

Refinement (PROVED: independent proof, reviewed here and independently confirmed). For large $k$ the transfer $kR(k)$ is a rational function of $k$
(finitely many offsets, Poisson divisors linear in $k$), bounded at infinity. So either $R(k)=0$ for all large $k$ (then
every fixed-deficit column has finite support in $k$, by the induction of Proposition 14.10(b)), or
$kR(k)=\lambda_sk^{-s}+O(k^{-s-1})$ for a unique integer $s\ge0$ and real $\lambda_s\ne0$. In the second case, for every fixed
$d$ and $q=k-1-d$, $\limsup_k\big((k!)^s\,q!\,\|[t^q]F_{Qk+r}\|_{\ell^1}\big)^{1/k}\le(d+1)^{s+1}|\lambda_s|$, and likewise for
$G$. Proof: with $B_{k,d}=(k!)^sA_{k,d}$ the homogeneous factor becomes $(k+1)^skR(k)\to\lambda_s$; a product of blocks
$i,j$ now carries $\binom ki^{s+1}$ up to a power of $k$, and
$\sum_i\binom ki^px^iy^{k-i}\le(x^{1/p}+y^{1/p})^{pk}$ for $p\ge1$ (from $\sum v_i^p\le(\sum v_i)^p$) with
$x=(a+1)^p\beta$, $y=(b+1)^p\beta$ gives the rate $(a+b+2)^p\beta\le(d+1)^p\beta$; linear terms from block $k-1$ cost $k^s$.
At the positive roots of the cubic of Proposition 14.10(a) one has $s\ge1$ (or eventual vanishing), so every fixed-deficit
column there decays at least like $C\rho^k/((k!)\,q!)$. (Independent proof, reviewed here and independently confirmed, including $s\ge1$ at all three roots.)

### 14.10 Vanishing transfers (PROVED: independent proofs, reviewed here and independently confirmed)

Proposition 14.10. (a) At $\delta=2/3$ and $f_1=\alpha\sin\theta+\beta\sin3\theta$,
$$\Lambda=\frac{314\alpha^3-2925\alpha^2\beta+6735\alpha\beta^2+75\beta^3}{259200}.$$
The cubic $75b^3+6735b^2-2925b+314$ has exactly three real roots, all simple, in $(-90.233,-90.232)$,
$(0.19598,0.19599)$ and $(0.23674,0.23675)$. For $\beta/\alpha$ equal to either positive root, $\Lambda=0$ and every
fixed-deficit factorial column has zero exponential rate (by Proposition 14.9; $\Lambda=0$ does not imply $R(k)=0$).
(b) Frequency gap. Let $Q\ge3$ be odd, $\delta=2/Q$, and let every frequency of $f_1$ be an odd multiple of one odd
$M>Q$; let $L$ be the top frequency. Then $R(k)=0$ exactly for $4k>Q(L+1)+2$. Consequently every fixed-deficit column
vanishes for all large $k$ (each extracted series of Proposition 14.9 is a polynomial), and with
$K_*=\lfloor(Q(L+1)+2)/4\rfloor+1$, $A=K_*+3$ and $B(k)=\max(0,k-\lceil(k+3)/A\rceil)$,
$$\deg_tF_n\le B(\lfloor(n-1)/Q\rfloor),\qquad\deg_tG_n\le B(\lfloor n/Q\rfloor),$$
so the log degree grows with slope at most $(1-1/A)/Q<1/Q$. (Example: $Q=3$, $f_1=\sin5\theta$, $K_*=6$, $A=9$.)

Proof. (a) is a finite exact computation with the offset algorithm of Section 14.9 in a polynomial ring (it gives
$3557/10368000$ at $\beta/\alpha=1/10$, as listed there), followed by sign checks at the rational endpoints. (b) Use signed
Fourier supports: products add frequencies, the Poisson inverse moves a density frequency by $\pm1$, and $\partial_\theta$,
$\partial_t$ and integration in $t$ preserve frequencies. The linearized cycle from $Qk$ to $Q(k+1)$ is a sum of trees with
$Q$ leading leaves, one external stream leaf $\sin m_k\theta$ and $Q$ interactions; of the $Q$ stream children one is the
external leaf, so $Q-1$ Poisson inversions occur. A frequency of $H_Q$ is
$\epsilon m_k+\sum_{a=1}^{Q}\epsilon_a\ell_a+\sum_{b=1}^{Q-1}\eta_b$ with signs $\epsilon,\epsilon_a,\eta_b$ and leading
frequencies $\ell_a$. For the target $m_k+1$ with $\epsilon=1$, $\sum_a\epsilon_a\ell_a$ is $M$ times a sum of $Q$ odd numbers,
so its modulus is at least $M\ge Q+2$, while $|\sum_b\eta_b|\le Q-1$; the total cannot be $1$. With $\epsilon=-1$ the
total would have to be $4k-3>QL+Q-1$. So $K(k)=0$. The deficit-0 forcing vanishes for $k\ge2$, and by induction on $d$
the lower-deficit columns have finite support in $k$, so $E_{k,d}=0$ for large $k$ and then $a_{k+1,d}=0$. For the degree
bound let $C_d$ be the largest block with a nonzero deficit-$d$ column. A quadratic forcing from blocks $u\le C_a$,
$v\le C_b$ lands in block at most $u+v+1$, the density at order $Qk+Q$ feeds stream block $k+1$, and the next scalar is
one block later; so $C_0\le K_*$ and $C_d\le\max(K_*,d+1,C_a+3,C_a+C_b+3)$ over $a<d$ and $a+b\le d-1$. The numbers
$D_d=A(d+1)-3$ satisfy this recursion, so $C_d\le D_d$, and a nonzero column of degree $q=k-1-d$ in block $k$ needs
$d\ge\lceil(k+3)/A\rceil-1$. $\square$

Status. PROVED: independent proofs (on transfer cancellation and on the log-degree gap), reviewed here;
the finite checks of (a) and of the cycle vanishing in (b) (formal cubic identity, nine exact Cartesian evaluations,
root brackets, 60 exact cycles, of which the 28 above the threshold vanish exactly) are independently confirmed, and
the all-order statements of (a) and (b), including the degree bound, are independently confirmed. Meaning: the leading profile controls the deficit transfer, and for profiles
with a frequency gap the logarithms are sparser than the general bound, but neither result controls all deficits at
once, so the convergence of the full logarithmic series stays OPEN for these profiles too.

### 14.11 Why coefficientwise norms do not close (PROVED: independent proofs, reviewed here and independently confirmed)

The statements of this section concern arbitrary coefficient arrays that obey the degree, bandwidth and symmetry
restrictions. They say nothing about divergence of the actual series; they show that a convergence proof must use
relations specific to the generated coefficients.

Proposition 14.11. (a) Deficit-only weights. For $R>0$ and positive weights $(w_d)_{d\ge0}$ put
$\|A\|_{R,w}=\sum_{k,q}R^kw_{k-1-q}\,q!\,|a_{k,q}|$ on scalar polynomials $A=\sum_{k\ge1}\sum_{q\le k-1}a_{k,q}z^kt^q$.
No constant $C$ gives $\|AB\|_{R,w}\le C\|A\|_{R,w}\|B\|_{R,w}$ for all $A,B$; if the product is measured at radius $r$
instead, a bound of this form forces $r\le R/2$.
(b) Reciprocal-binomial weights. For $A=\sum_{q<k}a_qt^q$ with coefficients in the angular $\ell^1$ algebra put
$N_k(A)=\sum_q\|a_q\|/\binom{k-1}{q}$ (so $N_k(A)=\sum_q\frac{d!\,q!}{(k-1)!}\|a_q\|$ with $d=k-1-q$). Then
$N_k(A)\le P(A)\le2^{k-1}N_k(A)$, where $P(A)=\sum_q\|a_q\|$; $N_{i+j}(AB)\le N_i(A)N_j(B)$ and
$N_{i+j+1}(AB)\le N_i(A)N_j(B)$; $N_k(\partial_tA)\le(k-1)N_k(A)$; and at $\delta=2/Q$ the stationary inverse on density
block $k$ satisfies $N_k(F_n)\le2N_k(S_n)/\lambda_n$, where $(\lambda_n-c\,\partial_t)F_n=S_n$ and
$\lambda_n=(n-1)(c-1)\ge2ck$.
(c) Poisson barrier. At $\delta=2/Q$ and $n=Qk+1$, $k\ge2$, the density input $t^{k-1}\sin((2k-3)\theta)$, which obeys
the degree, bandwidth and S1 restrictions, produces a stream whose $\sin((2k-2)\theta)$ coefficient has constant term
$(k-1)!/(2(2/Q)^k)$. Hence no bound $N_k(G_n)\le C_0C_1^kN_k(F_n)$, and no bound in any family of norms exponentially
equivalent to the plain norm, holds on the full input space, also after fixed losses in angular strip width or radius.

Proof. (a) $A_m=B_m=z^mt^{m-1}/(m-1)!$ have norm $R^mw_0$, and $A_mB_m$ (block $2m$, deficit 1) has norm
$R^{2m}w_1\binom{2m-2}{m-1}\ge R^{2m}w_1\,4^{m-1}/(2m-1)$; at output radius $r$ the factor $(r/R)^{2m}$ appears.
(b) The comparison with $P$ is $1\le\binom{k-1}q\le2^{k-1}$. For products, $\binom{i-1}u\binom{j-1}v$ is one term of the
Vandermonde sum $\binom{i+j-2}{u+v}\le\binom{i+j-1}{u+v}\le\binom{i+j}{u+v}$. For the derivative,
$q/\binom{k-1}{q-1}=(k-q)/\binom{k-1}q$. For the stationary inverse, $n-1\ge Qk$ and $c-1=2/(Q-2)$ give $\lambda_n\ge2ck$,
and the Neumann series of $(\lambda_n-c\partial_t)^{-1}$ gives the factor $1/(\lambda_n-c(k-1))\le2/\lambda_n$.
(c) For a density $a(t)\sin m\theta$ the upward stream harmonic $m+1$ satisfies
$[(m+1)^2-(P_n+\partial_t)^2]B=\frac12(\partial_t+p_n-m)a$, and $p_n-m=P_n-(m+1)$, so the numerator cancels one factor:
$B=-\frac12(\partial_t+P_n+m+1)^{-1}a$. For $m=2k-3$ one has $P_n+m+1=-2/Q=:-s$ (the other factor $m+1-P_n=4k-4+2/Q$
is nonzero), so $B=\frac1{2s}\sum_hs^{-h}\partial_t^ht^{k-1}$, whose constant term is $(k-1)!/(2s^k)$. $\square$

Meaning. The factorial norm $\sum_qq!\|a_q\|$ keeps the Poisson and stationary inverses geometric (Section 14.3) but not
products (a); the reciprocal-binomial norm keeps products and the stationary inverse geometric but not the Poisson
inverse (c). The loss in (c) comes from $(\partial_t+P_n+m+1)^{-1}$ with a bounded factor: it moves column $q$ to column
$q-h$ with factor $q!/((q-h)!\,|P_n+m+1|^h)$, which is at most $C^h$ when $|P_n+m+1|\ge q/C$. So the loss can only come
from angular modes within distance $O(q)$ of the diagonal $m\approx n\delta-3$. On the generated sequence the top
columns sit exactly on this diagonal ($[t^{k-1}]G_{3k}$ is the single resonant mode, Proposition 14.7) and are
factorially small (Propositions 14.7 and 14.9), which compensates the loss of (c) at every fixed deficit. A convergence
proof along these lines would have to exploit this correlation between log degree and angular position uniformly in the deficit. The same
mechanism gives the density-versus-stream example of Section 14.5 at $\delta=4/9$.

Status. PROVED: independent proofs (on deficit-only weights and on
the Poisson barrier), reviewed here, and the all-order arguments are independently confirmed; their finite checks (100 exact ratio instances; 216225 product inequalities, 4950
derivative identities and 56 exact Cartesian Poisson witnesses at $Q=3,4,5,9$) are independently confirmed.

### 14.12 A near-diagonal mixed norm also fails (PROVED: independent proof, reviewed here and independently confirmed)

Proposition 14.12. Let $\delta=2/Q$, $Q\ge3$, and $\eta>0$. For a density coefficient array at order $n=Qk+r$
($1\le r\le Q$) of log degree at most $k-1$ give the coefficient of $t^q\sin m\theta$ the weight $q!$ if
$|m+3-n\delta|\le\eta q$ and the weight $1/\binom{k-1}q$ otherwise, and let $M_n$ be the weighted absolute sum.
(a) Away from the band the upward Poisson channel is geometric: if $|s|\ge q/C$ then
$\|(\partial_t+s)^{-1}(a_qt^q)\|_{\rm plain}\le|a_q|(q+1)\max(1,C)^q/|s|$. The downward channel
$\frac12(m-1-P_n-\partial_t)^{-1}$ has scalar divisor $n\delta+m-3\ge2q+2/Q$ whenever $1\le q\le k-1$.
(b) There are no constants $C_0,C_1$ such that
$M_{2i}\big((\lambda_{2i}-c\,\partial_t)^{-1}J(G,F)\big)\le C_0C_1^iM_i(F)^2$ for every admissible density $F$ at a single order
$i$, where $G$ is the exact Poisson inverse of $F$ at order $i$ and $J$ is the quadratic term of the recursion. This
stays false after fixed losses in strip width or radius.

Proof. (a) $(\partial_t+s)^{-1}t^q=\sum_{h\le q}(-1)^h\frac{q!}{(q-h)!}s^{-h-1}t^{q-h}$ and $q!/(q-h)!\le q^h$; for the
downward channel use $q\le k-1$ and $n\delta\ge2k+2/Q$. (b) Take $i=Qk+1$, $h=4k-3$, $q=\lfloor(k-1)/(1+\eta)\rfloor$ and
$F=t^q(\sin\theta+\sin h\theta)$, which obeys the degree, bandwidth and S1 restrictions. With $P=P_i=2-2k-2/Q$ the
two input offsets are $4-2k-2/Q$ and $2k-2/Q$, of modulus larger than $k-1>\eta q$ for $k\ge4$, so $M_i(F)\le2$. The
top-degree stream coefficients are $-1/(2(P+2))$ at frequency $2$ and $-1/(2(P+h+1))$ at frequency $h+1$. The output
frequency $h+2=4k-1$ at degree $2q$ receives only the two cross products $(2,h)$ and $(h+1,1)$; with
$Pgf'-p\,g'f$ ($p=P-1$) the coefficient of $\sin((l+m)\theta)$ is $\frac12(Pm-pl)$ times the product of amplitudes, so
$$T=-\frac{-2P^2+(h-1)^2P+4(h+1)}{4(P+h+1)(P+2)},\qquad|T|\ge\frac{(h-1)^2}{4(h+1)}\quad(k\ge4),$$
because $P<-2$, $2P^2>8(k-1)^2\ge4(h+1)$, $0<P+h+1\le h+1$ and $|P+2|<|P|$. At order $2i$ the output offset is
$4k+2-(2Qk+2)\delta=2-4/Q$, inside the band once $2\eta q\ge2-4/Q$, and the stationary inverse keeps the top coefficient
$T/\lambda_{2i}$. Hence $M_{2i}\ge(2q)!\,|T|/\lambda_{2i}$, which grows faster than any exponential in $k$ since
$q/k\to1/(1+\eta)$, while $M_i(F)\le2$. $\square$

Meaning. Two modes far from the diagonal with opposite offsets (the lowest mode and a mode near twice the diagonal)
produce a near-diagonal mode at the doubled order, so a band around the diagonal is not invariant, and a norm that is
factorial near the diagonal and binomial away from it does not close on general inputs. Like 14.11, this concerns
general admissible inputs, not the generated series; in the generated data the near-diagonal mass of the maximizing
interior column is below $0.4\%$ (14.6 item 7).

Status. PROVED: independent proof, reviewed here step by step, and the all-order argument
(for every $\eta>0$) is independently confirmed; its finite checks (35 exact Cartesian witnesses at $Q=3,4,5,9,17$, 18
further witnesses for other widths, and 400 linear monomial bounds) are independently confirmed. It does not prove
divergence of the generated series.

### 14.13 A smaller Gevrey order for separated high harmonics (PROVED: independent proof, reviewed here and independently confirmed)

Proposition 14.13. Under the hypotheses of Proposition 14.10(b) (odd $Q\ge3$, every frequency of $f_1$ an odd multiple
of one odd $M>Q$, top frequency $L$), with $A$ and $B$ as there, put $D_n=B(\lfloor(n-1)/Q\rfloor)$,
$E_n=B(\lfloor n/Q\rfloor)$, $C=56Q(L+1)/(c-1)$ and $F=\|f_1\|_{\ell^1}$. Then
$$\|F_n\|_{!,4Q}\le\frac{D_n!}nF(8CF)^{n-1},\qquad\|G_n\|_{!,4Q}\le4Q\,\frac{D_n!}nF(8CF)^{n-1},$$
and $D_n!\le(n!)^\sigma$ with $\sigma=(1-1/A)/Q<1/Q$.

Proof. With $\alpha=1-1/A$ one has $B(k)=\max(0,\lfloor\alpha k-3/A\rfloor)$, which is nondecreasing and superadditive: if
$B(u),B(v)>0$ then $B(u)+B(v)\le\lfloor\alpha(u+v)-6/A\rfloor\le B(u+v)$, and otherwise monotonicity suffices. Hence
$E_i+D_j\le B(\lfloor i/Q\rfloor+\lfloor(j-1)/Q\rfloor)\le D_{i+j}$, and $E_n\ge D_n$. By Proposition 14.10(b),
$\deg_tF_n\le D_n$ and $\deg_tG_n\le E_n$. The proof of Section 14.3 now applies with $\kappa_n,\eta_n$ replaced by
$D_n,E_n$: every Poisson shift is $0$ or of modulus $\ge1/Q$, so $\|G_n\|_{!,4Q}\le4Q\|F_n\|_{!,4Q}$; the stationary
inverse costs $2/\lambda_n$ because $c/(4Q\lambda_n)=1/(8(n-1))$; the product loses $\binom{E_i+D_j}{E_i}$, which the
normalization $u_n=\|F_n\|_{!,4Q}/D_n!$ absorbs; and with the factors $4i,3j$ for the radial exponents and $(L+1)i,(L+1)j$
for $\partial_\theta$, $x_n=nu_n$ satisfies $x_n\le2C\sum_{i+j=n}x_ix_j$, $x_1=F$, so $x_n\le F(8CF)^{n-1}$ by the Catalan
bound. Finally $D_n\le\alpha(n-1)/Q\le\sigma n$ and $\log(d!)/d$ is nondecreasing in $d$. $\square$

Examples: $Q=3$, $f_1=\sin5\theta$: $A=9$, $\sigma=8/27$, $8CF=4032$; $f_1=\sin9\theta$: $A=12$, $\sigma=11/36$. This improves
the Gevrey order $1/Q$ of Section 14.3 for these profiles but still permits factorial growth, so the convergence of their
logarithmic series remains OPEN. Status. PROVED: independent proof, reviewed here step by
step, and the all-order argument is independently confirmed; its finite checks (1383698 integer inequalities and 168 exact norm comparisons
against the full recursions through order 42 for $\sin5\theta$ and $\sin9\theta$) are independently confirmed.

### 14.14 A sufficient condition: one realized product-loss bound (PROVED: independent proof, reviewed here and independently confirmed)

Let $\delta=a/b$ in lowest terms, $c=1/(1-\delta)$, let $f_1$ be a finite real S1 sine polynomial with top frequency $L$
and $F=\|f_1\|_{\ell^1}$, and use the canonical constants of Section 14.1. With $Q_n=(\lambda_n-cD)F_n$ the forcing of
Section 14.1, $\|H\|_{!,\sigma}=\sum_qq!\,\sigma^q\|[t^q]H\|_{\ell^1}$ and
$w_{i,j}=(L+1)\big[j(|P_i|+1)+i(|p_j|+1)\big]$, define the realized loss ratio
$$\rho_n^{(\sigma)}=\frac{\|Q_n\|_{!,\sigma}}{\sum_{i+j=n}w_{i,j}\|G_i\|_{!,\sigma}\|F_j\|_{!,\sigma}}\qquad(n\ge2).$$
No bound on this ratio follows from estimating each product separately: the computation in the proof of Proposition
14.11(a), with all weights equal, shows that two inputs of log degree $m-1$ can have a product whose factorial norm
exceeds the product of their factorial norms by $\binom{2m-2}{m-1}\ge4^{m-1}/(2m-1)$. The statement below concerns the
generated sequence only.

Proposition 14.14. (a) If there are constants $B,T$ with $\|G_n\|_{!,1}\le B\|F_n\|_{!,1}$ and $\rho_n^{(1)}\le T$ for
all $n$, then $\|F_n\|_{!,1}\le\frac FnA^{n-1}$ and $\|G_n\|_{!,1}\le\frac{BF}nA^{n-1}$ with
$A=8(L+1)(5-2\delta)BTF/(c-1)$.
(b) If $\rho_n^{(4b)}\le T$ for all $n\ge2$, then $\|F_n\|_{!,4b}\le\frac FnA^{n-1}$ and
$\|G_n\|_{!,4b}\le4b\frac FnA^{n-1}$ with $A=32b(L+1)(5-2\delta)TF/(c-1)$. No hypothesis on the stream is needed.
In both cases the density, stream and a compatible potential series converge absolutely and uniformly on $r\ge R$ for
every $R>A^{1/\delta}$, together with all their Cartesian derivatives with the natural weights, and the sum is a
real-analytic exterior solution of the stationary equation.

Proof. (i) Linear steps. $\|DH\|_{!,\sigma}\le\sigma^{-1}\|H\|_{!,\sigma}$. For $\sigma=1$: a genuine stream resonance
needs $P_n=-m$ with $m\ge2$ even, so the first one, $N_0$, has $N_0\delta\ge4$, and $F_n$ is free of $t$ for
$n\le N_0$; there $n\|F_n\|\le\frac n{\lambda_n}\|Q_n\|\le\frac2{c-1}\|Q_n\|$. For $n\ge N_0+1\ge2+2/\delta$ the finite
Neumann series gives $n\|F_n\|\le\frac n{\lambda_n-c}\|Q_n\|=\frac1{c-1}\frac n{n-1-1/\delta}\|Q_n\|\le\frac2{c-1}\|Q_n\|$,
using $c/(c-1)=1/\delta$. For $\sigma=4b$: $c=b/(b-a)$ gives $c/\sigma=(c-1)/(4a)$, so the finite
Neumann series gives $n\|F_n\|\le\frac n{\lambda_n-c/\sigma}\|Q_n\|=\frac1{c-1}\frac n{n-1-1/(4a)}\|Q_n\|\le\frac2{c-1}\|Q_n\|$
for $n\ge3$, while $F_2$ and $Q_2$ are free of $t$ and $2/\lambda_2=2/(c-1)$; and Section 14.3 gives
$\|G_n\|_{!,4b}\le4b\|F_n\|_{!,4b}$ at every order. (ii) Weights. For $i\ge1$ and $0<\delta<1$,
$|2-i\delta|+1\le(3-\delta)i$ and $|1-i\delta|+1\le(2-\delta)i$ (check both signs), so
$w_{i,j}\le(L+1)(5-2\delta)ij$. (iii) Majorant. $Y_n=n\|F_n\|_{!,\sigma}$ satisfies $Y_1=F$ and
$Y_n\le K\sum_{i+j=n}Y_iY_j$ with $K=2(L+1)(5-2\delta)BT/(c-1)$ in (a) and $K=8b(L+1)(5-2\delta)T/(c-1)$ in (b); the
Catalan bound gives $Y_n\le(4K)^{n-1}F^n$, i.e. the stated bounds with $A=4KF$. (iv) Potential. For $X=n\delta\ge20$
the two Euler factors have inverses of norm $\le1/(X-4)\le4/X$ in $\|\cdot\|_{!,\sigma}$ (because $\|D\|\le1$), and the
Cauchy sum costs at most 27, so Proposition 14.5 holds with $\|\cdot\|_*$ replaced by $\|\cdot\|_{!,\sigma}$; the finitely
many early potential coefficients exist by Section 14.1. (v) Summation. $\|H(t)\|_{\ell^1}\le e^{|t|/\sigma}\|H\|_{!,\sigma}$
since $|t|^q/q!\le e^{|t|}$. A fixed Cartesian derivative costs a polynomial in $n$. For $r\ge\max(R,1)$ the weighted
term of order $n$ is at most a constant times $n^hA^{n-1}r^{1-\delta(n-1)}$, which decreases in $r$ once
$\delta(n-1)>1$, and $AR^{-\delta}<1$ makes the sum converge; on a compact range $R\le r\le1$ use $e^{|t|}\le1/R$.
Complex neighborhoods and absolute convergence give analyticity and allow regrouping of the stationary products, so
the sum solves the equation. $\square$

Part (a) is an independent proof, reviewed here step by step; part (b) is a refinement given here, in which the stream
hypothesis becomes the confirmed Section 14.3; both are independently confirmed, and the sharper stationary step in
(i) for $\sigma=4b$, which halves the first constant given here, was found in the independent check and rechecked here. Thus a
sufficient route to convergence at rational $\delta$ is to prove that $\rho_n^{(4b)}$ stays bounded on the generated
coefficients. Necessity is not claimed. Section 14.15 reports that through order 290 at $\delta=2/3$ the factorial
norms themselves grow like a Gevrey sequence of order near $0.30$. Finite data cannot decide an all-order bound, but
if the factorial norms are not geometrically bounded, Corollary 14.15(b) makes $\rho_n^{(4b)}$ unbounded.

Data (NUMERICAL EVIDENCE, $\delta=2/3$, $f_1=\sin\theta$, canonical constants, certified in ball arithmetic through
order 290, unweighted norm $\sigma=1$). $\rho_n^{(1)}$ lies in $[0.1206,0.1474]$ for $20\le n\le210$ and then
rises: $0.157$ (220), $0.194$ (230), $0.242$ (240), $0.315$ (250), $0.344$ (260), $0.324$ (270), $0.361$ (280); its
maximum over $2\le n\le280$ is $0.36072$ at $n=280$ and over $2\le n\le290$ it is $0.36910$ at $n=289$. In the
progression $n=245,254,263,272$ the 9-order increments decrease ($0.065,0.035,0.013,0.007$), but not in every residue
class: at $n=277$ and $279$ the latest 9-order increment exceeds $0.85$ times the preceding one. The stream ratio
$\|G_n\|_{!,1}/\|F_n\|_{!,1}$ is at most $0.2115$ (at $n=3$) and is $0.0010$ at 280. The rise after order 210 coincides with the
move of the largest term of $\|F_n\|_{!,1}$ from the constant column to the interior ($q=46$ at 260, $q=57$ at 290). The products of the positive-degree parts alone,
measured the same way, have ratio $0.077$ (120), $0.106$ (180), $1.06$ (220), $28.4$ (250), $42.4$ (260), $50.1$ (270),
$58.0$ (280), and their norm exceeds that of the full forcing from order 250 on (by the factor $1.33$ at 280): the
boundary products with $t$-free factors cancel part of them. The weighted ratio $\rho_n^{(12)}$ of part (b) is reported in
Section 14.15(c).

Status. Proposition 14.14 PROVED (independently confirmed, including the halved constant of (b)); the data are finite
and certified; the hypotheses of (a) and (b) are OPEN, and Section 14.15 gives finite evidence against them at
$\delta=2/3$.

### 14.15 Growth of the factorial norms at $\delta=2/3$, and what it decides

(a) Proposition 14.15 (factorial-norm growth does not imply divergence). Let $\delta=2/3$, $c=3$, $t=\log r$,
$D=\partial_t$, $q_n=4-2n/3$, $k_n=\max\{0,\lfloor(n-1)/3\rfloor-1\}$, $a_0=-27/400$, and
$\chi_n=a_0r^{q_n}t^{k_n}$, $\psi_n=\partial_x\partial_y\chi_n$, $\rho_n=-\partial_y\Delta\chi_n$. Then
$\psi_n=r^{P_n}G_n$ and $\rho_n=r^{p_n}F_n$ with
$$G_n=\tfrac12(q_n+D)(q_n-2+D)H_n\,\sin2\theta,\qquad F_n=-(q_n-2+D)(q_n+D)^2H_n\,\sin\theta,\qquad H_n=a_0t^{k_n},$$
$F_1=\sin\theta$, $-\Delta\psi_n=\partial_x\rho_n$, every resonant constant is zero, and the log degrees are at most
$k_n$, the canonical degree bound at $\delta=2/3$ (Section 14.7). The three series $\sum\chi_n$, $\sum\psi_n$, $\sum\rho_n$
converge absolutely and uniformly on $r\ge e$ together with every fixed Cartesian derivative in its natural weight,
and their sums are real analytic. Nevertheless, for every fixed $\sigma>0$,
$$\lim_{n\to\infty}\frac{\log\|F_n\|_{!,\sigma}}{n\log n}=\lim_{n\to\infty}\frac{\log\|G_n\|_{!,\sigma}}{n\log n}=\frac13 .$$
The sequence is not a solution of the stationary recursion: at order 2 the residual is
$-\frac{79}{100}\sin\theta-\frac1{20}\sin3\theta$.

Proof. For a radial $g=r^qH(t)$ one has $g'=r^{q-1}(q+D)H$, $g''=r^{q-2}(q-1+D)(q+D)H$, so
$\partial_x\partial_yg=\frac12(g''-g'/r)\sin2\theta$ and $\Delta g=r^{q-2}(q+D)^2H$, which give the two formulas;
$F_1=-\frac43\cdot\frac{100}9a_0=1$. Poisson's equation holds because the derivatives commute. The stream has only the
frequency 2, whose only resonance is $P_6=-2$; there $q_6=0$, $k_6=0$ and $G_6=F_6=0$, so all resonant constants
vanish. For $t\ge1$, $k_n\le(n-1)/3$ gives $r^{-2(n-1)/3}t^{k_n}\le(t^{1/3}e^{-2t/3})^{n-1}\le e^{-2(n-1)/3}$, since the
bracket decreases for $t>1/2$; a fixed derivative costs a polynomial in $n$ and does not raise the degree in $t$, so
the weighted series converge geometrically, and the same margin on a small complex neighborhood gives analyticity. The
top coefficient of $F_n$ is $-(q_n-2)q_n^2a_0\ne0$ for $n\notin\{3,6\}$, so
$\|F_n\|_{!,\sigma}\ge|a_0||q_n-2|q_n^2\,k_n!\,\sigma^{k_n}$, and $\|q+D\|_{!,\sigma}\le|q|+1/\sigma$ gives an upper bound
of the same form times a polynomial in $n$; similarly for $G_n$; Stirling's formula and $k_n/n\to1/3$ give the limits.
The residual is a direct computation from $F_1$, $G_1=-\frac3{20}\sin2\theta$ and $F_2=\frac8{25}\sin\theta$. $\square$

(b) Corollary. If $\limsup_n\|F_n\|_{!,4b}^{1/n}=\infty$ for the generated sequence at $\delta=a/b$, then
$\sup_n\rho_n^{(4b)}=\infty$; if $\limsup_n\|F_n\|_{!,1}^{1/n}=\infty$, the hypotheses of Proposition 14.14(a) fail for
all $B,T$. (Contrapositive of Proposition 14.14.)

(c) Data (NUMERICAL EVIDENCE, $\delta=2/3$, $f_1=\sin\theta$, canonical constants, orders $\le290$). Certified in
512-bit ball arithmetic (all coefficient balls at order 290 resolved): for $L_n=\log_{10}\|F_n\|_{!,12}$ the finite
curvature statistic
$$\hat\sigma_{n,h}=\frac{L_n-2L_{n-h}+L_{n-2h}}{\log_{10}n!-2\log_{10}(n-h)!+\log_{10}(n-2h)!},$$
which equals $\sigma$ exactly for norms of the form $CA^n(n!)^\sigma$, takes the values $0.2988$, $0.3040$, $0.2989$,
$0.3008$, $0.2992$ at $n=180,210,240,270,290$ with $h=30$ (stream: $0.3297$, $0.3152$, $0.3076$, $0.3078$, $0.3058$).
The weighted ratio $\rho_n^{(12)}$ depends strongly on $n\bmod3$ (1.630, 1.635, 1.640 at $n=282,285,288$; 0.562, 0.561,
0.560 at 283, 286, 289; 1.098, 1.108, 1.119 at 284, 287, 290), and its maximum over $2\le n\le290$ is $1.6398$ at
$n=288$. In the class $n\equiv0\pmod3$ it rises steadily, about $0.12$ per 30 orders since order 150: 0.29 (60),
0.77 (90), 0.93 (120), 1.10 (150), 1.20 (180), 1.32 (210), 1.44 (240), 1.56 (270), 1.64 (288); in the class $n\equiv2$
it rises from 0.15 (59) to 1.12 (290); in the class $n\equiv1$ it is largest near order 100 (1.03) and falls to 0.56
(289). The unweighted $\rho_n^{(1)}$ has maximum $0.36910$ at $n=289$.
From the stored midpoints (not certified): the plain column sum $M_n=\sum_q\|[t^q]F_n\|_{\ell^1}$ has 30-order slopes
of $\log_{10}M_n$ equal to $-0.7059$, $-0.7043$, $-0.7036$, $-0.7032$, $-0.7026$, $-0.7018$ on the windows
$110$ to $140$, ..., $260$ to $290$, and its largest column is $q=0$; the slopes of the factorial norms with
$\sigma=3$ and $\sigma=12$ increase from window to window by $0.86$ to $1.02$ and $0.89$ to $0.91$ times the increase
$\frac13\log_{10}(n_2/n_1)$ of the model $(n!)^{1/3}$. The largest weighted column $q!\,12^q\|[t^q]F_n\|_{\ell^1}$ is at $q=57$, $75$, $84$
for $n=200,260,290$ ($q/n\approx0.29$), and exceeds the constant column by $49.9$, $73.4$, $85.9$ decades; with the weight
$q!(3/2)^q$ (the cost of the Poisson factor with the smallest nonzero shift $2/3$, see (d)) the excess is $3.35$,
$10.34$, $14.61$ decades. The plain stream sums gain on the density sums: $\log_{10}(M_n(G)/M_n(F))=-2.43$ (230),
$-2.53$ (260), $-2.13$ (272), $-1.86$ (281), $-1.60$ (290). A two-sided real-line norm behaves like the factorial
norms: on a quarter-step grid in $[-640,640]$ the sampled maximum of $e^{-|t|/3}\|F_n(t,\cdot)\|_{\ell^1}$ lies at
negative $t$ (near $t=-244$ at $n=290$), where it is within one decade of the column bound $\sum_q\|[t^q]F_n\|\,|t|^q$,
and the 30-order slopes of the sampled maxima increase ($-0.52$ on 150 to 180, $-0.47$ on 240 to 270). The grid does
not locate the global maximum, but a certified enclosure of the global supremum is available: on each interval
$[x_{j-1},x_j]$ of a partition of $[0,K/\eta]$, where $K$ is the log degree and $\eta=1/3$, the supremum is at most
$e^{-\eta x_{j-1}}U(x_j)$ with $U(x)=\sum_q\|[t^q]F_n\|x^q$, and beyond $K/\eta$ the envelope decreases. In ball
arithmetic this gives $\log_{10}\sup_te^{-|t|/3}\|F_n(t,\cdot)\|_{\ell^1}\in[-171.455,-170.661]$ at $n=290$, and
$[-174.497,-173.700]$ for the stream (independent computation, reviewed here). At fixed $t\ge0$ the values decay geometrically (Section 14.6).
Reading. The generated coefficients have the shape of the example in (a): high log columns that are geometrically,
not factorially, small, and large cancellation in the values at fixed $t\ge0$ (Section 14.6). Such columns make
every factorial norm grow like $(q^*)!$ with $q^*\approx0.29n$. If this persists, then by (b) the route of
Proposition 14.14 cannot close at $\delta=2/3$, and by (a) this growth says nothing about divergence.

(d) The obstacle for column norms (PROVED; elementary). For real $\mu\ne0$ the polynomial inverse of $\mu+D$ maps
$t^k$ to $\sum_{h\le k}(-1)^h\frac{k!}{(k-h)!}\frac{t^{k-h}}{\mu^{h+1}}$, whose constant term is
$(-1)^kk!/\mu^{k+1}$. Hence in any weighted column norm $\sum_q\omega_q\|[t^q]H\|_{\ell^1}$ its norm on polynomials of
degree $\le k$ is at least $\omega_0k!/(|\mu|^{k+1}\omega_k)$, and a bound uniform in $k$ forces
$\omega_k\ge C^{-1}\omega_0k!|\mu|^{-k}$, a factorial weight with $\sigma\ge1/|\mu|$. At $\delta=a/b$ the Poisson
inverse at order $n$ and even stream frequency $m$ is built from the inverses of $P_n\pm m+D$. Since
$P_n\pm m=(2b(1+j)-na)/b$ with $j$ an integer and $\gcd(a,b)=1$, the nonzero shifts lie in $(g/b)\mathbb Z$ with
$g=\gcd(a,2)$, and the value $g/b$ occurs ($2/3$ at $\delta=2/3$; Proposition 14.11(c) exhibits the shift on an
admissible input). So every column norm in which all linear steps are uniformly bounded dominates a factorial norm
with $\sigma\ge b/g$ ($\sigma\ge3/2$ at $\delta=2/3$). This threshold is sharp (independent proof, reviewed here): in
the norm $\sum_qq!\,s^q\|[t^q]H\|_{\ell^1}$ the canonical Poisson map is bounded uniformly in the order and the log
degree if and only if $s>b/g$, with bound $\max\{s,1/(g/b-1/s)\}$, since $\|D\|=1/s$ in this norm, integration from
$0$ has norm $s$, and each density coefficient feeds two stream modes with factor $1/2$; at $s=b/g$ the input $t^k$ at
the shift $g/b$ gives the ratio $(k+1)b/(2g)$. At $\delta=2/3$ the weight $q!\,2^q$ gives the bound $6$, and the
stationary inverse $(2(n-1)-3D)^{-1}$ has norm at most $2$ in the same norm. If the
column shape in (c) persists, with high columns that are geometrically but not factorially small, every factorial
norm with $\sigma>0$ eventually grows faster than geometrically; through order 290 this is seen at $\sigma=3$ and
$\sigma=12$. In that case a convergence proof at rational $\delta$ in a column norm cannot rest on uniform bounds for
the linear steps; it must use a property of the generated sequence that general admissible inputs lack, such as a
realized bound on the plain stream-to-density ratio (Section 14.16), the angular location of the high
log columns (for $|P_n\pm m|\ge q/C$ the inverse costs only $C^h$, see the end of Section 14.11), or the cancellation in
the values $F_n(t,\theta)$ at fixed $t\ge0$, which is what convergence of the series on $r\ge R$ requires. In the
data both are present: the maximizing columns lie almost entirely far from the band (Section 14.6, item 7), while the
stream mode closest to the band, at shift $2/3$, carries a weighted mass $\max_qq!(3/2)^q\|[t^q]G_n\|$ about $7.8$
decades above the constant column of $G_n$ at $n=289$ and $290$ (midpoint values), on whichever side of the band
that mode lies.

Status. (a) PROVED: independent proof, reviewed here and independently confirmed (with exact Cartesian checks through
order 72). (b) and (d) PROVED (elementary); the sharpness statement in (d): PROVED (reviewed here and independently confirmed). The
enclosure in (c): PROVED (elementary lemma) with a certified finite computation. (c) NUMERICAL EVIDENCE at finite orders; whether the factorial norms of
the generated sequence grow faster than geometrically is OPEN, and convergence at rational $\delta$ remains OPEN.

### 14.16 A single realized hypothesis in the plain norm (PROVED: independent proof, reviewed here and independently confirmed)

Unlike the factorial norms of Sections 14.3 and 14.14, the plain column norm $\|H\|_*=\sum_{q,m}|h_{q,m}|$ (for
$H=\sum_{q,m}h_{q,m}t^q\sin m\theta$ or the cosine analogue; $\|H\|_*=\sum_q\|[t^q]H\|_{\ell^1}$) is an algebra,
$\|UV\|_*\le\|U\|_*\|V\|_*$, so products lose nothing; the stationary inverse is cheap by the degree bound; and the only
unbounded linear step is the Poisson inverse (Section 14.5(a), 14.15(d)). The following proposition replaces that step
by one realized inequality.

Proposition 14.16. Let $\delta=a/b$ be reduced, $f_1$ a nonzero real finite sine polynomial with highest frequency $L$
and $F=\|f_1\|_{\ell^1}$, with the canonical constants of Section 14.1. Put $M_n=\|F_n\|_*$, $N_n=\|G_n\|_*$,
$n_r=2b/\gcd(a,2)$ as in Section 14.2, and $C_0=3-\delta+2/n_r\le3$. Suppose there is $H_0>0$ with
$$N_n\le H_0M_n\qquad(n\ge1).\tag{14.16.1}$$
Then with $K=2H_0(L+1)C_0/(c-1)$ and $A=4KF$,
$$M_n\le\frac FnA^{n-1},\qquad N_n\le\frac{H_0F}nA^{n-1},$$
and for every $R>e$ with $AR^{-\delta}(\log R)^{2/n_r}<1$ the density, stream and potential series converge absolutely
and uniformly on $r\ge R$, with every weighted Cartesian derivative; the sum is real analytic and solves the stationary
equation exactly on $r>R$.

Proof. Use the degree bounds $\deg_tF_n\le\kappa_n$, $\deg_tG_n\le\eta_n$ of Section 14.2, with $h$ and $\varepsilon$ as
there. First, $\kappa_n\le\frac\delta2(n-2)$ for $n\ge2$: if $h=1$ then $\delta=2/n_r$ and $\kappa_n\le(n-1)/n_r-1\le(n-2)/n_r$
when $\kappa_n>0$; if $h\ge2$ then $1/n_r=\delta/(2h)\le\delta/4$, so $\kappa_n\le\delta(n-1)/4\le\delta(n-2)/2$ for $n\ge3$,
and $\kappa_2=0$. Since $\lambda_n=(n-1)(c-1)=c\delta(n-1)$ and $\|D\|_*\le\kappa_n$ on polynomials of degree $\le\kappa_n$,
the finite Neumann series gives $\|(\lambda_n-cD)^{-1}\|_*\le1/(\lambda_n-c\kappa_n)\le2/(c\delta n)$, that is,
$$n M_n\le\frac2{c-1}\|Q_n\|_*.$$
By induction from $f_1$ and the shift by $\pm1$ in the Poisson step, the frequencies of $F_j$ are at most $(L+1)j-1$ and
those of $G_i$ at most $(L+1)i$, so $\|\partial_\theta F_j\|_*\le(L+1)jM_j$ and $\|\partial_\theta G_i\|_*\le(L+1)iN_i$. With
$|P_i|\le(2-\delta)i$, $|p_j|\le j$, $\eta_i\le i/n_r$, $\kappa_j\le j/n_r$ and the algebra property, the forcing of Section 14.1
satisfies
$$\|Q_n\|_*\le(L+1)\sum_{i+j=n}\big[j(|P_i|+\eta_i)+i(|p_j|+\kappa_j)\big]N_iM_j\le(L+1)C_0\sum_{i+j=n}ij\,N_iM_j .$$
With (14.16.1) and $Y_n=nM_n$ this gives $Y_1=F$ and $Y_n\le K\sum_{i+j=n}Y_iY_j$, so
$Y_n\le\mathrm{Cat}_{n-1}K^{n-1}F^n\le F(4KF)^{n-1}$. The bound on $N_n$ follows from (14.16.1). Proposition 14.5 now gives
the potential coefficients and the convergence: for $t=\log r\ge1$ each term is at most a polynomial in $n$ times
$[AR^{-\delta}(\log R)^{2/n_r}]^{n-1}$, and $r^{-\delta}(\log r)^{2/n_r}$ is nonincreasing for $r\ge e$ because
$\delta n_r=2h\ge2$. $\square$

For $\delta=2/3$ and $f_1=\sin\theta$ ($n_r=3$, $C_0=3$, $L=1$, $F=1$, $c-1=2$) one gets $A=24H_0$. With $H_0=1/4$, $A=6$
and $R=64$ is admissible: $6\cdot64^{-2/3}(\log64)^{2/3}=0.9698<1$ (equivalently $6^{3/2}\log64<15\cdot4.2=63<64$). For
$H_0=1$ the condition holds for $R\ge800$. With the exponent $1/n_r$ of Section 14.18(a) in place of $2/n_r$ these radii improve to $27$
($6\cdot27^{-2/3}(\log27)^{1/3}=0.9921$) and $300$ ($24\cdot300^{-2/3}(\log300)^{1/3}=0.957$). Both radii are PROVED conditional on (14.16.1) with the stated $H_0$ (reviewed here and independently confirmed).
The data below show that (14.16.1) with $H_0=1/4$ is false for the generated sequence (it fails at orders 323 and 326), so the
radii $64$ and $27$ do not apply to it. Finitely many exceptions to (14.16.1) can always be absorbed by enlarging $H_0$,
so (14.16.1) holds for some $H_0$ exactly when $\sup_nN_n/M_n<\infty$, and any admissible $H_0$ is at least
$\max_{n\le329}N_n/M_n=0.3362004\pm4.3\cdot10^{-8}$ (attained at $n=323$), and in fact at least $1.70$ (order 338, Data
below). For $H_0=0.34$ ($A=8.16$) the radius $R=110$ is admissible
($8.16\cdot110^{-2/3}(\log110)^{2/3}=0.9974$), and with the exponent of Section 14.18(a) $R=46$ is admissible
($8.16\cdot46^{-2/3}(\log46)^{1/3}=0.9943$); both are PROVED conditional on (14.16.1) with $H_0=0.34$ (the two inequalities, and the failure of $109$ and $45$, independently checked), which is false for the generated sequence (it fails at 332, 335, 338 and 340; Data below).

Relation to Sections 14.5 and 14.14. Proposition 14.5 needs geometric bounds on both $M_n$ and $N_n$; Proposition
14.16 derives them from the single ratio (14.16.1). Compared with Proposition 14.14 it needs no factorial weight and
no product-loss ratio. On general admissible inputs (14.16.1) fails (the example at $\delta=4/9$ in Section 14.5(a),
and Section 14.15(d)); the hypothesis is about the generated sequence only. Necessity is not claimed.

Remark (the canonical Poisson factor is a one-sided average in $\log r$; PROVED, elementary). For real $\mu\ne0$ and a
polynomial $p$, the unique polynomial solution of $(\mu+D)y=p$ is
$$y(t)=\int_0^\infty e^{-\mu u}p(t-u)\,du\quad(\mu>0),\qquad y(t)=-\int_0^\infty e^{\mu u}p(t+u)\,du\quad(\mu<0),$$
as differentiation under the integral shows; uniqueness holds because the kernel $e^{-\mu t}$ is not a polynomial. In the
Poisson step the shifts are $\mu=P_n\pm m$. So for a positive shift the canonical stream at $t=\log r$ averages the
density polynomial over all $\log r'\le\log r$, including $r'<1$, where the polynomial in $\log r$ has no meaning as a
function value, with a weight that decays at rate $|\mu|\ge\gcd(a,2)/b$. Hypothesis (14.16.1) therefore asks that the
density polynomials attached to the small positive shifts stay small, in this averaged sense, far into $t<0$; in the
data of Section 14.15(c) the sampled maximum of the exponentially weighted values of $F_n(t,\cdot)$ over the real line
lies far in $t<0$ (near $t=-244$ at $n=290$).

The averaging cannot be confined to a half-line (independent proof, reviewed here; general inputs). For fixed $\eta>0$
and $T\in\mathbb R$ put $\|H\|_{\eta,T}=\sup_{t\ge T}e^{-\eta(t-T)}\|H(t,\cdot)\|_{\ell^1}$. The canonical Poisson map is
not bounded in this norm uniformly in the order, even on admissible inputs. With the Laguerre polynomials
$L_k(x)=\sum_{j\le k}\binom kj(-x)^j/j!$ and $p_k(t)=L_k(2\eta(t-T))$, the generating function
$\sum_kL_k(x)z^k=e^{-xz/(1-z)}/(1-z)$ and Cauchy's bound on $|z|=k/(k+1)$ give $\|p_k\|_{\eta,T}\le e(k+1)$, while the
canonical solution of $(\mu+D)y=p_k$ has $y(T)=\mu^{-1}(1+2\eta/\mu)^k$. Placing $p_k\sin((m-1)\theta)$ at an order and
frequency with $P_n+m=g/b$ (these exist with arbitrarily large admissible degree) gives the ratio
$(1+2\eta b/g)^k/(2e(g/b)(k+1))$. The solution with $y(T)=0$ is bounded by $\|p\|_{\eta,T}/(\mu+\eta)$ and differs from
the canonical one by $y(T)e^{-\mu(t-T)}$; in the stream this difference is a multiple of $r^{P_n}e^{-(P_n+m)t}\sin m\theta
=r^{-m}\sin m\theta$, a homogeneous exterior harmonic, which lies outside the polynomial-in-$\log r$ coefficient at the
exponent $P_n$. A negative shift $-\nu$ is bounded by $1/(\nu-\eta)$ for $\eta<\nu$, since it samples only $t+u\ge T$. So
on general inputs the obstruction is exactly the canonical normalization of the positive shifts; this says nothing by
itself about the generated sequence.

Data (NUMERICAL EVIDENCE, $\delta=2/3$, $f_1=\sin\theta$, canonical constants, certified in ball arithmetic through
order 300, and through order 329 by a 512-bit ball run whose norm-relative density radii are below $10^{-6}$ through
order 328 and $2.5\cdot10^{-6}$ at 329). The ratio $N_n/M_n$ is below $1/4$ for every $n\le329$ except $n=323$ and $n=326$, with maximum
$0.21149$ at $n=3$ on $n\le322$. At order 323 it is $0.3362004\pm4.3\cdot10^{-8}$ and at 326 it is
$0.321538\pm2.2\cdot10^{-7}$, so (14.16.1) with $H_0=1/4$ is false for the generated sequence (certified enclosures,
reproduced by an independent decoding of the ball data, which also confirms every norm entry on 301 to 326). The history of the
ratio: it turned upward from about order 263:
$\log_{10}(N_n/M_n)=-2.430$ (230), $-2.527$ (260), $-2.126$ (272), $-1.858$ (281), $-1.603$ (290), and the 30-order
slope of $\log_{10}N_n$ on 260 to 290 is $-0.671$ against $-0.702$ for $\log_{10}M_n$ (midpoints). If the rate of the
18 orders up to 290 (about $0.029$ decades per order) had persisted, the ratio would have exceeded $1/4$ near order
325. It did not persist: on 291 to 300 the ratio lies between $10^{-2.01}$ (at 300) and $10^{-1.52}$ (at 296). Over 263 to
300 the stream sums decay at a nearly constant geometric rate that is about $0.02$ decades per order slower than that of
the density sums (Section 14.17), so the ratio still drifts upward on average; if that persisted, (14.16.1) would fail for
every $H_0$, while the hypothesis of Proposition 14.17 could still hold. On 301 to 316, $\log_{10}(N_n/M_n)$ lies in
$[-2.09,-1.09]$; on 317 to 329 it lies in $[-1.34,-0.47]$, with values $-0.684$ (317), $-0.473$ (323), $-0.858$,
$-0.799$, $-0.493$, $-0.873$, $-0.890$, $-0.829$ (324 to 329); the largest values occur at the orders $n\equiv2$
modulo 3, where the increments of $N_n$ are erratic ($+0.28$ at 317, $-0.68$ at 320, $+0.15$ at 323, $-0.60$ at 326).
The 27-order slope of $\log_{10}N_n$ minus that of $\log_{10}M_n$ is $+0.004$ (window ending at 310), $+0.013$ (316),
$+0.033$ (320) and $+0.049$ (326). On 330 to 340 the run no longer meets its $10^{-6}$ relative stopping rule, but
that rule is a diagnostic only: the stored coefficient balls are still exact enclosures (the recurrence keeps using ball
arithmetic and the checkpoints store exact dyadic centers and radii), and every individual ball is resolved. An
independent summation of the stored balls at 640 bits certifies $N_{332}/M_{332}>1.49$ and $N_{338}/M_{338}>1.70$, and
$N_n>0.34M_n$ also at $n=335$ and $340$; all 375226 new Poisson coefficient identities on 331 to 340 pass. At these
orders $n\equiv2$ modulo 3 the stream mass is concentrated within a few log columns of the resonant diagonal (more than
$0.89$ of $N_n$ at 332, 335, 338). So (14.16.1) is false for every $H_0<1.70$. This is a finite certified inequality;
it does not decide whether $\sup_nN_n/M_n$ is finite, nor convergence.

Continuation beyond the certified run (NUMERICAL EVIDENCE, conditional on the order-329 midpoints). The certified run
above is the only source of the certified statements on 330 to 340. Its balls stay exact enclosures, but their
norm-relative radii grow from about $10^{-4.9}$ at 330 to $10^{-3}$ to $10^{-2}$ at 335 to 340 and reach order one by 345, so it
resolves nothing from about order 344 on. A second computation restarts the same recursion in 512-bit ball arithmetic
from the midpoints of the order-329 balls, with the radii set to zero, and has reached order 390. Its own radii
(norm-relative $10^{-151}$ to $10^{-107}$) bound only the arithmetic from those midpoints; the effect of the discarded
order-329 uncertainty ($2.5\cdot10^{-6}$ relative) is not bounded, so every value of the continuation is conditional on the
midpoints. On 330 to 340 its values of $\log_{10}M_n$ differ from the midpoints of the certified run by at most $5\cdot10^{-6}$,
inside the certified radii. In the continuation, $\log_{10}(N_n/M_n)$ lies between $+0.15$ and $+0.23$ at every order
$n\equiv2$ modulo 3 from 332 to 390 except 335, where it is $-0.031$ (a ratio of about $0.93$, consistent with the certified
$N_{335}>0.34M_{335}$). The 27-order slopes of $\log_{10}M_n$ and $\log_{10}N_n$ are $-0.70$ and $-0.68$ for the window ending at
300, $-0.58$ and $-0.55$ (ending 350), $-0.544$ and $-0.542$ (360), $-0.542$ and $-0.545$ (370), $-0.543$ and $-0.539$ (380) and $-0.539$ and $-0.539$ (390). From 351 on the increments
are nearly, not exactly, periodic with period 3: the three-order decrements of $\log_{10}M_n$ are $-1.632$, $-1.630$, $-1.628$
on 351 to 360, $-1.627$, $-1.625$, $-1.623$ on 360 to 369 and $-1.622$, $-1.620$, $-1.619$ on 369 to 378 and $-1.617$, $-1.615$, $-1.614$, $-1.612$ on 378 to 390, with
$M_{360}^{1/360}\approx0.2014$, $M_{380}^{1/380}\approx0.2047$ ($N_{380}^{1/380}\approx0.2050$) and $M_{390}^{1/390}\approx0.2070$ ($N_{390}^{1/390}\approx0.2064$). The drift sits in the class-0 increment ($-0.193$ at 360,
$-0.184$ at 378, $-0.177$ at 390). The per-period increments of $\log_{10}|a_n|$ for the shifted three-order density multiplier
$a_n$ of Section 14.23 at the class-0 orders from 357 to 390 are $+0.0011$, $+0.0018$, $+0.0015$ and then $+0.0016$ to within
$0.00004$ from 366 on, apart from $+0.0014$ for 375 to 378; an earlier reading of that single step as a slowing of the drift
is withdrawn. Fitted on 357 to 390 to the unrounded multipliers at every order (independently recomputed), the power
model gives $\beta=0.4550$ (against $0.555$ on 348 to 370, fitted to five-decimal multipliers), the limit model $|a_\infty|=0.03771$
(against $0.041$), and a model with $\log_{10}|a_n|$ linear in $n$ (exponential growth of the multiplier, Proposition 14.24) has slope
$0.000529$ per order, with root-mean-square residuals $5.03$, $5.20$ and $4.93$ times $10^{-4}$; on windows this short the first two models are tangent to within about $10^{-4}$ in $\log_{10}$,
so the fits cannot separate them (the bound is PROVED in the application of Proposition 14.23).
Extended to order 400: the three-order decrements on 390 to 399 are $-1.611$, $-1.609$, $-1.607$, the drift again sitting only in
the class-0 increment ($-0.176$, $-0.174$, $-0.173$; the class-1 and class-2 increments have stayed at $-0.700$ and $-0.734$ since
330); the 27-order slopes ending at 400 are $-0.537$ ($M$) and $-0.540$ ($N$), $M_{400}^{1/400}\approx0.2086$
($N_{400}^{1/400}\approx0.2081$), the per-period increment of $\log_{10}|a_n|$ stays near $+0.0016$, and the three fits on 357 to
400 give $\beta=0.464$, $|a_\infty|=0.0383$ and a slope $0.000533$ per order, with residuals $5.0$, $5.5$ and $4.8$ times $10^{-4}$
(fits by the continuation program to the multipliers rounded to five decimals, a computation reproduced independently;
the unrounded multipliers give $\beta=0.463$, $|a_\infty|=0.0382$ and a slope $0.000532$, with residuals $5.1$, $5.5$ and $4.9$ times $10^{-4}$): the models are still not separated. Extended to order 420 and rechecked independently through 420 (same conditional status): the three-order decrements from 408 to 420 are $-1.601$, $-1.599$, $-1.597$, $-1.595$, again with the drift only in the class-0 increment ($-0.164$, $-0.163$, $-0.161$; it was $-0.197$ at 354), $M_{420}^{1/420}\approx0.2122$, $\log_{10}M_{420}=-282.799$, $\log_{10}N_{420}=-283.305$, and the full-precision fits on 357 to 420 give $\beta=0.483$, $|a_\infty|=0.0395$ and a slope $0.000541$ per order, with residuals $6.1$, $7.6$ and $5.2$ times $10^{-4}$ (on 357 to 410: $\beta=0.472$, $|a_\infty|=0.0388$, slope $0.000535$): the models are still not separated. Extended to order 430 and rechecked independently through 430 (same conditional status): the three-order decrements from 420 to 429 are $-1.594$, $-1.592$, $-1.590$, the class-0 increments $-0.159$, $-0.158$, $-0.156$, $M_{430}^{1/430}\approx0.2136$, $\log_{10}M_{430}=-288.275$, $\log_{10}N_{430}=-288.709$; the fits on 357 to 429 give $\beta=0.493$, $|a_\infty|=0.0401$ and a slope $0.000546$ per order (residuals $5.1$, $7.9$ and $2.2$ times $10^{-4}$), and on 410 to 429 $\beta=0.561$, $|a_\infty|=0.0445$, slope $0.000580$. The power exponent and the fitted limit keep rising as the window moves up; the linear model has the smallest residual, but the multipliers are known to four digits only, so the models are still not separated (NUMERICAL EVIDENCE). Extended to order 440 and rechecked independently through 440 (same conditional status; the recheck covers the coefficient norms, the Poisson identities and the fitted statistics): the three-order decrements from 429 to 438 are $-1.588$, $-1.587$, $-1.585$, the class-0 increments $-0.154$, $-0.153$, $-0.151$ (the class-1 and class-2 increments stay at $-0.700$ and $-0.735$), $M_{440}^{1/440}\approx0.2150$, $\log_{10}M_{440}=-293.769$, $\log_{10}N_{440}=-293.530$; the fits on 357 to 438 give $\beta=0.502$, $|a_\infty|=0.0407$ and a slope $0.000551$ per order (residuals $6.3$, $9.9$ and $2.7$ times $10^{-4}$), on 390 to 438 $\beta=0.540$, $|a_\infty|=0.0433$, slope $0.000568$, and on 420 to 438 $\beta=0.576$, $|a_\infty|=0.0457$, slope $0.000583$. The pattern is unchanged: the fitted exponent and limit rise with the window start; with the printed four-digit multipliers the linear model has the smallest residual on the longer windows and the power model a marginally smaller one on the final seven-point window 420 to 438 ($4.27$ against $4.35$ times $10^{-5}$), while with the unrounded multipliers the linear model has the smallest residual on all seven final windows ($1.10$ against $3.22$ times $10^{-5}$ on 420 to 438); the margins are a few times the rounding level of the printed multipliers and no model is excluded (NUMERICAL EVIDENCE).
The density sum decreases at every
order through 400; the stream sum decreases at every order except 332 (up by $0.68$ decades) and 338 (nearly unchanged).
One perturbed restart, with every order-329 ball replaced by a random boundary point, differs from the midpoint
continuation by $1.5\cdot10^{-7}$ to $2.5\cdot10^{-6}$ in $\log_{10}M_n$ and $\log_{10}N_n$ on 330 to 332, and the difference
is $1.5\cdot10^{-9}$ and $1.9\cdot10^{-9}$ at 340, an overall decrease that is not monotone (it increases, for example, from 333 to 334 in the stream sum and from 336 to 337
in both). Measured instead by the relative full-array $\ell^1$ distance $d_n=\|\text{perturbed}-\text{reference}\|_1/\|\text{reference}\|_1$,
whose largest input value over both fields and $n\le329$ is $D_{\rm in}=3.58\cdot10^{-6}$, the displacement is first amplified,
to $4.39\cdot10^{-6}$ at 330 and $6.86\cdot10^{-6}$ at 331 in the stream (factors 1.23 and 1.92), and then attenuated, to
$3.3\cdot10^{-8}$ (density) and $8.0\cdot10^{-9}$ (stream) at 340, and to $7.15\cdot10^{-10}$ and $3.77\cdot10^{-11}$ at 350, that is
$2.0\cdot10^{-4}$ and $1.05\cdot10^{-5}$ times $D_{\rm in}$, with every value from 332 to 350 below $D_{\rm in}$; in $\log_{10}M_n$ and
$\log_{10}N_n$ the difference at 350 is $4.5\cdot10^{-11}$ and $4.7\cdot10^{-12}$ (independently recomputed from the stored arrays;
a single displacement, a diagnostic and not a bound). Section 14.23 converts the nearly periodic pattern of
this continuation into exact conditional growth laws.

Status. Proposition 14.16: PROVED (independent proof, reviewed here and independently confirmed). The remark: PROVED
(elementary); its half-line statement: PROVED (reviewed here and independently confirmed). Hypothesis (14.16.1) at all orders: OPEN. The data: NUMERICAL EVIDENCE at finite orders.

### 14.17 The stream sums alone decide (PROVED)

A geometric bound on the density sums alone does not control the stream on general admissible inputs (the example at
$\delta=4/9$ in Section 14.5(a)); on the generated sequence it does (Section 14.19). The opposite implication holds: since the density recursion is linear in the density
once the stream is given, a geometric bound on the stream sums alone implies one on the density sums.

Proposition 14.17. Let $\delta=a/b$ be reduced, $f_1$ a nonzero real finite sine polynomial with highest frequency $L$
and $F=\|f_1\|_{\ell^1}$, with the canonical constants of Section 14.1, and let $M_n=\|F_n\|_*$, $N_n=\|G_n\|_*$, $n_r$
and $C_0$ be as in Section 14.16.

(a) Suppose $N_n\le HA_0^n$ for all $n\ge1$, with $H,A_0>0$. Put $K=2H(L+1)C_0/(c-1)$ and
$y_*=1+\frac K2-\sqrt{K+K^2/4}\in(0,1)$, the root in $(0,1)$ of $Ky=(1-y)^2$. Then for every $B>A_0/y_*$ there is
$C_B$ with $M_n\le C_BB^n$ for all $n$. Consequently the density, stream and potential series converge absolutely and
uniformly on $r\ge R$, with every weighted Cartesian derivative, for every $R>e$ with $BR^{-\delta}(\log R)^{2/n_r}<1$,
and the sum is an exact solution of the stationary equation on $r>R$.

(b) Conversely, if for one $R_0>e$ the stream log terms are absolutely summable,
$\sum_{n,q}R_0^{-\delta(n-1)}(\log R_0)^q\|[t^q]G_n\|_{\ell^1}<\infty$, then $N_n\le CA_0^n$ for some $C$, $A_0$, and (a)
applies.

So the absolute convergence of the stream's individual log terms at a single radius implies the convergence of all
three series on an explicit exterior. For convergence in the sense of absolutely summable log terms, the problem at
rational $\delta$ is therefore exactly whether the realized stream sums $N_n$ grow at most geometrically.

Proof. (a) The first part of the proof of Proposition 14.16 (degree bound, finite Neumann inverse, frequency
induction, algebra property) did not use (14.16.1); it gives, for $n\ge2$,
$$nM_n\le\frac2{c-1}\|Q_n\|_*\le\frac{2(L+1)C_0}{c-1}\sum_{i+j=n}iN_i\,jM_j .$$
With $Y_n=nM_n$ and the hypothesis, $Y_1=F$ and $Y_n\le K\sum_{i=1}^{n-1}iA_0^iY_{n-i}$. Define $Z_1=F$ and
$Z_n=K\sum_{i=1}^{n-1}iA_0^iZ_{n-i}$; by induction $0\le Y_n\le Z_n$. The generating function satisfies
$Z(x)=Fx+Kg(A_0x)Z(x)$ with $g(y)=\sum_{i\ge1}iy^i=y/(1-y)^2$, so $Z(x)=Fx/(1-Kg(A_0x))$. On $[0,1)$, $g$ increases
from $0$ to $\infty$ and $Kg(y_*)=1$; hence $Z$ is given by a power series with nonnegative coefficients that converges
for $0\le x<y_*/A_0$, and $Z_n\le Z(x)x^{-n}$ there. With $x=1/B$ this gives $M_n\le Y_n\le Z(1/B)B^n$. Since $y_*<1$,
$B>A_0$ and $N_n\le HB^n$. Proposition 14.5 with base $B$ and constant $\max(Z(1/B),H)$ gives the convergence and the
exact solution.

(b) Every term is at most the sum $S$, and $(\log R_0)^q\ge1$, so $\|[t^q]G_n\|_{\ell^1}\le SR_0^{\delta(n-1)}$; summing over
the at most $\eta_n+1\le n+1$ columns gives $N_n\le(n+1)SR_0^{\delta(n-1)}$, which is geometric. $\square$

The radius in (a) can be much larger than $R_0$ in (b); no sharpness is claimed. Together with Section 14.15(d), the
proposition locates the difficulty in one place: $N_n=\|T_nF_n\|_*$, where $T_n$ is the canonical Poisson inverse,
which is unbounded in the plain norm on general admissible inputs (Section 14.5(a)), applied to the realized
densities. Hypothesis (14.16.1) is a special way of bounding this quantity; Proposition 14.17 needs only its
geometric growth, so it remains applicable if the stream and density sums decay at different geometric rates.

Data (NUMERICAL EVIDENCE, $\delta=2/3$, $f_1=\sin\theta$, canonical constants; $M_n$ and $N_n$ certified in ball
arithmetic through order 300, the slopes and shares computed from the certified values or from midpoints). The per-order
slope of $\log_{10}N_n$ from three-step differences (pooled over the three residue classes) has mean $-0.706$ (standard
deviation $0.012$) on 230 to 257 and $-0.677$ (standard deviation $0.012$) on 263 to 290; on 291 to 300 the mean is
$-0.700$ with a larger scatter (standard deviation $0.054$). Least-squares slopes of $\log_{10}N_n$ over 27 consecutive
orders are $-0.676$ for the windows starting at 260, 263 and 268 and $-0.684$ for 274 to 300, while the density slope
stays at $-0.701$ to $-0.702$. The gain of the stream is carried by the stream modes whose smallest Poisson shift is
$2/3$ (for $n\equiv2\pmod3$, where that shift is $+2/3$, their share of $N_n$ grows from $0.37$ at 263 to $0.80$ at 290),
and the constant log column carries $0.44$ to $0.66$ of $N_n$ on 263 to 290. The ratio $N_n/M_n$ stays below $0.2115$
through order 300 with its maximum at $n=3$; on 291 to 300 its largest value is $0.0302$ (at 296) and at 300 it is
$0.0098$, so the faster rise seen over the last 18 orders before 290 did not continue. The certified prefix now reaches
order 315: every ratio through 315 is below $1/4$ (maximum $0.2115$ at $n=3$), on 301 to 310 the largest value is $0.0300$
(at 302), at 310 it is $0.0180$, and on 311 to 315 the values are $0.0821$, $0.0473$, $0.0560$, $0.0381$, $0.0199$.
The certified prefix was later extended to order 329: the ratio exceeds $1/4$ twice, $0.336$ at 323 and $0.322$ at 326, and the
27-order slopes ending at 326 are $-0.6920$ for $\log_{10}M_n$ and $-0.6428$ for $\log_{10}N_n$, a difference of
$+0.049$ per order, against $+0.017$ at 300 and $+0.033$ at 320 (Section 14.16 Data).
Least-squares slopes over the 27 orders ending at 316 are $-0.7001$ for $\log_{10}M_n$ and $-0.6876$ for $\log_{10}N_n$
(midpoints of ball values). Through order 300 the stream sums
therefore look geometric, with a rate that changed once, near orders 245 to 263, rather than accelerating; a Gevrey law
of order $0.3$ would steepen the slope by about $0.045$ per 100 orders, which the fits do not show. The stream rate
nevertheless stays about $0.02$ decades per order slower than the density rate: a straight-line fit of $\log_{10}(N_n/M_n)$
on 263 to 300 has slope $0.022$ and would reach $\log_{10}(1/4)$ near order 349. This is an extrapolation, not a claim;
the ratio in fact first exceeded $1/4$ at order 323, at one of the fluctuating orders $n\equiv2$ modulo 3.
If the two rates stayed different, (14.16.1) would fail for every $H_0$ while the hypothesis of (a) would hold. A
heuristic in the other direction (HEURISTIC, with a measurement): the term $i=n-1$, $j=1$ of $Q_n$ (the stream $G_{n-1}$
against $f_1$) is of size about $|P_{n-1}|N_{n-1}$, and the density inverse $(\lambda_n-cD)^{-1}$ has size about
$1/\lambda_n=1/(c\delta(n-1))$, so this term contributes about $N_{n-1}/c$ to $F_n$. Measured on the midpoints, its plain
norm after the inverse is $0.25$ to $0.31$ times $N_{n-1}$ at every order checked from 30 to 290 ($c=3$). Unless it cancels
against the other terms, this forces $M_n$ to decay no faster than $N_{n-1}$ and so caps the ratio near $cN_n/N_{n-1}$,
about $0.6$ at the observed stream rate. In the same measurement the density is carried by the low-order streams: the
single term $i=1$ (the stream $G_1$ against $F_{n-1}$) has plain norm $0.77$ to $0.80$ times $M_n$ on 60 to 290, the terms
$i=2$ and $i=3$ about $0.10$ and $0.07$, and the products with $4\le i\le n-4$ together $0.08$ to $0.12$ (the code is
among the accompanying artifacts). This is finite-order evidence and heuristics only and does not bear on the all-order
hypothesis of (a).

Status. Proposition 14.17: PROVED (written here, independently confirmed). Whether $N_n$ grows at most geometrically at rational
$\delta$: OPEN. The data: NUMERICAL EVIDENCE at finite orders.

### 14.18 Exterior convergence or divergence almost everywhere (PROVED)

The setting is that of Proposition 14.17. Write $T_n(t,\theta)=e^{P_nt}G_n(t,\theta)$ for the order-$n$ stream term
$r^{P_n}G_n(\log r,\theta)$, viewed as a function on the $(t,\theta)$ plane. Recall that $G_n$ has log degree at most
$\eta_n\le n/n_r$ and angular frequencies at most $(L+1)n$ (Section 14.16).

Proposition 14.18. (a) (Sharper radius.) If $M_n\le CA^n$ and $N_n\le CA^n$ for all $n$, the conclusion of Proposition
14.5 holds on $r\ge R$ for every $R\ge e$ with $AR^{-\delta}(\log R)^{1/n_r}<1$. In Proposition 14.17(a) the base
$B_0=A_0/y_*$ itself is admissible: $M_n\le FB_0^{\,n-1}/n$ for all $n$.

(b) (Equivalences.) The following statements are equivalent:
1. $N_n\le CA^n$ for all $n$, for some $C$ and $A$;
2. the stream log terms are absolutely summable at one radius $R_0>e$, as in Proposition 14.17(b);
3. the stream series $\sum_nT_n$ converges uniformly on some closed annulus $r_0\le r\le r_1$, $r_0<r_1$, for all $\theta$;
4. the sequence $(T_n)$ is bounded at every point of some nonempty open subset of the $(t,\theta)$ plane;
5. the sequence $(T_n)$ is bounded at every point of some Lebesgue-measurable subset of the plane of positive area.

Each of them gives the conclusion of Proposition 14.17(a), with the radius condition of (a). Statement 4 or 5 holds in
particular if the stream series converges at every point of an open set, or of a set of positive area.

(c) (Dichotomy.) Consequently, for each rational $\delta$ and each $f_1$, exactly one of the following holds. Either the
density, stream and potential series converge absolutely and uniformly, with every weighted Cartesian derivative, on
some exterior $r\ge R$, and the sum is an exact exterior solution; or the set of points where the individual stream terms
are bounded has area zero and is meagre (a countable union of closed sets with empty interior), so that the stream
series diverges at almost every point and on a dense residual set of the plane. The same alternative holds for the
series of the radial velocity and for any potential series that generates the stream and whose order-$n$ coefficient
has log degree and frequency $O(n)$ at large $n$ (such as the potential of Section 14.5).

Proof. (a) The density, stream and potential coefficients satisfy $\|\cdot\|_*\le C'A^n$ with log degree at most
$n/n_r$ at large $n$ (Section 14.5 for the potential). For $t=\log r\ge1$ the order-$n$ term, after the common leading
power of $r$, is at most $C'A^ne^{-\delta(n-1)t}t^{n/n_r}$. For $n\ge2$ its logarithmic $t$-derivative is
$-\delta(n-1)+n/(n_rt)\le\frac1{n_r}\big(n-\delta n_r(n-1)\big)\le\frac{2-n}{n_r}\le0$, since $\delta n_r=2h\ge2$. On
$r\ge R$ the term is therefore at most $C'A(\log R)^{1/n_r}q_R^{\,n-1}$ with $q_R=AR^{-\delta}(\log R)^{1/n_r}$.
Weighted derivatives cost polynomial factors in $n$, and the remainder is the proof of Proposition 14.5. (The former
exponent $2/n_r$ came from replacing $t^{n/n_r}$ by $t^{2(n-1)/n_r}$ before maximizing in $r$.) For the base, with $K$
and $y_*$ as in Proposition 14.17, $K\sum_{i\ge1}iy_*^i=Kg(y_*)=1$. If $Y_j\le FB_0^{\,j-1}$ for $j<n$, then
$Y_n\le K\sum_{i=1}^{n-1}iA_0^iFB_0^{\,n-i-1}=FB_0^{\,n-1}K\sum_{i=1}^{n-1}iy_*^i\le FB_0^{\,n-1}$, and $Y_1=F$.

(b) 1 implies 2: for $t\ge1$, $\sum_qt^q\|[t^q]G_n\|_{\ell^1}\le t^{n/n_r}N_n$; choose $R_0$ with
$AR_0^{-\delta}(\log R_0)^{1/n_r}<1$. 2 implies 1 is Proposition 14.17(b); the factor $n+1$ there can be dropped,
since the whole order-$n$ sum is at most $S$. 1 implies 3 by Proposition 14.17(a). 3 implies 4, because uniformly
convergent series have uniformly bounded terms, and 4 implies 5 trivially. The step 5 implies 1 uses three elementary
lemmas.

Lemma 1 (separated nodes). If $S\subset\mathbb R$ is bounded and measurable with $|S|=\mu>0$ and $d\ge1$, there are
$x_0<\dots<x_d$ in $S$ with $x_k-x_j\ge(k-j)\mu/(4d)$ for $j<k$. Proof: $\Phi(x)=|S\cap(-\infty,x]|$ is continuous,
nondecreasing and 1-Lipschitz, with values from $0$ to $\mu$. The preimage under $\Phi$ of the window
$W_j=\big((j+\frac14)\frac{\mu}{d+1},(j+\frac34)\frac{\mu}{d+1}\big)$ meets $S$ in a set of measure $\frac{\mu}{2(d+1)}>0$;
choose $x_j$ there. Then $x_k-x_j\ge\Phi(x_k)-\Phi(x_j)>(k-j-\frac12)\frac{\mu}{d+1}\ge\frac{(k-j)\mu}{2(d+1)}\ge\frac{(k-j)\mu}{4d}$.

Lemma 2 (polynomials on a measurable set). If $p$ is a real polynomial of degree at most $d\ge1$ with $|p|\le V$ on a
measurable $S\subset[-B,B]$, $|S|=\mu>0$, then the sum of the absolute values of its coefficients is at most
$V[8e(1+B)/\mu]^d$. Proof: interpolate at the nodes of Lemma 1. Each numerator $\prod_{k\ne j}(t-x_k)$ has coefficient sum
at most $(1+B)^d$, each denominator is at least $(\mu/(4d))^dj!(d-j)!$, and $\sum_j1/(j!(d-j)!)=2^d/d!$ with
$d!\ge(d/e)^d$.

Lemma 3 (trigonometric polynomials on a measurable set). If $h$ has frequencies in $[-M,M]$ and $|h|\le V$ on a
measurable set of angles of measure $\eta>0$ within one period, then $\sum_m|\hat h_m|\le V(16\pi e/\eta)^{2M}$. Proof:
some half-period $[\alpha,\alpha+\pi]$ contains a part of the set of measure $\mu\ge\eta/2$. Take the nodes of Lemma 1
there with $d=2M$, and $z_j=e^{ix_j}$; then $|z_k-z_j|=2\sin\frac{x_k-x_j}2\ge\frac{2(x_k-x_j)}\pi\ge\frac{(k-j)\mu}{2\pi d}$.
Interpolating the polynomial $z^Mh$ of degree at most $d$ at the $z_j$ (the numerators now have coefficient sum at most
$2^d$) gives $\sum_m|\hat h_m|\le V(8\pi d/\mu)^d/d!\le V(8\pi e/\mu)^d\le V(16\pi e/\eta)^{2M}$.

Proof that 5 implies 1. The terms are $2\pi$-periodic in $\theta$ and the plane is a countable union of rectangles, so we
may assume that the set $E$ of statement 5 lies in $Q=[T_0,T_1]\times[0,2\pi)$, $h=T_1-T_0>0$, with positive area. The
measurable sets $E_j=\{(t,\theta)\in E:|T_n(t,\theta)|\le j\text{ for all }n\}$ increase to $E$, so some $E_j$ has area
$\mathcal A>0$. By Fubini the slice measures $\ell(t)$ of $E_j$ integrate to $\mathcal A$; with $\eta=\mathcal A/(2h)$, the
set $S$ of $t$ with $\ell(t)\ge\eta$ has measure at least $\mu=\mathcal A/(4\pi)$, since the other $t$ carry at most
$\eta h=\mathcal A/2$ and $\ell\le2\pi$. Put $B=\max(|T_0|,|T_1|)$. For $t\in S$, on its slice,
$|G_n|=e^{-P_nt}|T_n|\le je^{2B}e^{n\delta T_1}$. Lemma 3 with $M\le(L+1)n$ bounds the angular $\ell^1$ norm, which for a
sine polynomial is the sum of the absolute sine amplitudes, so every amplitude $b_{n,m}(t)$ is at most
$je^{2B}e^{n\delta T_1}(16\pi e/\eta)^{2(L+1)n}$ on $S$. Lemma 2 with degree at most $n/n_r$ bounds its coefficient sum
by the same quantity times $[8e(1+B)/\mu]^{n/n_r}$ (both brackets exceed $1$). Summing over at most $(L+1)n$ amplitudes,
$$N_n\le j(L+1)e^{2B}\,n\,B_*^{\,n},\qquad B_*=e^{\delta T_1}\Big(\frac{16\pi e}\eta\Big)^{2(L+1)}\Big(\frac{8e(1+B)}\mu\Big)^{1/n_r},$$
which is geometric.

(c) If statement 1 holds, (a) and Proposition 14.17(a) give the convergence. If it fails, the set where $(T_n)$ is
bounded is $Z=\bigcup_jZ_j$, $Z_j=\bigcap_n\{|T_n|\le j\}$, with each $Z_j$ closed because the $T_n$ are continuous. By
5 implies 1, $Z$ has area zero, so each $Z_j$ has empty interior and $Z$ is meagre; outside $Z$ the terms are unbounded
and the series diverges. For the radial velocity, the order-$n$ term is $r^{1-n\delta}\partial_\theta G_n$ up to sign;
the same proof with radial exponent $1$ in place of $2$ (Lemma 3 applies to cosine amplitudes too) bounds
$\|\partial_\theta G_n\|_*\ge N_n$ geometrically. For the potential, the order-$n$ term is $r^{4-n\delta}C_n$; the same
proof with exponent $4$ bounds $\|C_n\|_*$ geometrically, and since $\psi=\partial_x\partial_y\chi$, each Cartesian
derivative costs at most the radial exponent, the log degree and the frequency, all $O(n)$, while multiplication by
$\cos\theta$ or $\sin\theta$ has norm at most $1$; so $N_n\le Cn^2\|C_n\|_*$ at large $n$. $\square$

At $\delta=2/3$ under (14.16.1) with $H_0=1/4$, where $A=6$, part (a) improves the conditional radius of Section 14.16
from $64$ to $27$: $q_{27}^3=216\log27/729=\frac89\log3<1$, because
$e^{9/8}>\sum_{j\le4}(9/8)^j/j!=300993/98304>3$.

Remarks. 1. Part (c) excludes intermediate behavior at rational $\delta$: the canonical far-field series cannot
converge on a set of positive area, such as a sector of an annulus, without converging on a full exterior, and
divergence, if it occurs, is divergence at almost every point. The proposition does not decide which case occurs; the
data of Section 14.17 support the first at $\delta=2/3$ through order 315. 2. Statements 4 and 5 give no explicit radius:
the base $B_*$ depends on the unknown set and bound. Statement 2 with explicit $S$ and $R_0$, or statement 1 with explicit
$C$ and $A$, gives an explicit radius. 3. The argument for 5 implies 1 uses only the radial factor and the two linear
degree bounds, not the recursion; the recursion enters only through Proposition 14.17(a). 4. (Quantitative form;
PROVED.) The bounded set may depend on $n$, provided its area stays bounded below. Let
$Q=[T_0,T_1]\times[0,2\pi)$, $h=T_1-T_0>0$, $B=\max(|T_0|,|T_1|)$. If $|T_n|\le V_n$ on a measurable subset of $Q$ of area at
least $\pi h$ (half of $Q$), the proof of 5 implies 1, run for this single $n$ with $\eta=\pi/2$ and $\mu=h/4$, gives
$N_n\le(L+1)e^{2B}\,n\,V_nB_Q^{\,n}$ with $B_Q=e^{\delta T_1}(32e)^{2(L+1)}[32e(1+B)/h]^{1/n_r}$, independent of $n$. By
Chebyshev's inequality $|T_n|\le2\|T_n\|_{L^1(Q)}/|Q|$ on at least half of $Q$, so
$N_n\le\frac{(L+1)e^{2B}}{\pi h}\,n\,B_Q^{\,n}\,\|T_n\|_{L^1(Q)}$; conversely $\|T_n\|_{L^1(Q)}\le2\pi h\,e^{2B}e^{-n\delta\min(T_0,0)}$
$\times\max(1,B)^{n/n_r}N_n$. Hence $N_n$ is geometric if and only if $\|T_n\|_{L^1(Q)}$ is, for one or for every such
rectangle, and in the second alternative of (c) the integrals $\int_Q|T_n|$ are not bounded by any geometric sequence on
any rectangle: $\limsup_n\|T_n\|_{L^1(Q)}^{1/n}=\infty$. This does not assert eventual growth or a root limit; degree bounds
alone do not exclude sequences that vanish at infinitely many orders. 5. ($L^p$ and angular sectors; PROVED: independent
proof, reviewed here.) The same equivalence holds in $L^p(Q)$ for every $0<p\le\infty$ (quasi-norms for $p<1$): Chebyshev
gives $|T_n|\le(\pi h)^{-1/p}\|T_n\|_{L^p(Q)}$ on half of $Q$, so $N_n\le(L+1)e^{2B}(\pi h)^{-1/p}nB_Q^{\,n}\|T_n\|_{L^p(Q)}$, and
$\|T_n\|_{L^p(Q)}\le(2\pi h)^{1/p}e^{2B}e^{-n\delta\min(T_0,0)}\max(1,B)^{n/n_r}N_n$ (for $p=\infty$ drop the area factors). On
$[T_0,T_1]\times I$ with an angular interval $I$ of length $\ell\in(0,2\pi]$ take $\eta=\ell/4$: the factor $(32e)^{2(L+1)}$
becomes $(64\pi e/\ell)^{2(L+1)}$ and the area factors become $(2/(h\ell))^{1/p}$ and $(h\ell)^{1/p}$. So geometric local $L^p$
bounds on any nonempty open rectangle already give a geometric bound on $N_n$; the density with $M_n$ is the same.

Status. Proposition 14.18: PROVED (independent proof, reviewed here and independently confirmed). The radius $27$:
PROVED, conditional on (14.16.1) with $H_0=1/4$, which is false for the generated sequence (it fails at orders 323 and 326;
Section 14.16 Data, NUMERICAL EVIDENCE from certified enclosures). The radius $46$ for $H_0=0.34$ (Section 14.16):
PROVED, conditional on (14.16.1) with $H_0=0.34$, which is also false for the generated sequence (it fails at 332, 335, 338
and 340). Remark 4: PROVED (reviewed here and independently confirmed). Which alternative of (c) holds at any rational $\delta$: OPEN.

### 14.19 The density sums alone decide on the generated sequence (PROVED)

By Section 14.5(a), a geometric bound on the density sums does not control the stream on general admissible inputs. On
the generated sequence it does: the density equation at order $i+1$ contains $G_i$ through a transport operator built
from the leading profile, and this operator is coercive in a weighted norm. No Poisson inverse is used.

Proposition 14.19. In the setting of Proposition 14.17 write $f_1=\sum_{k\le L}a_k\sin k\theta$ with $a_L\ne0$. If
$M_n\le CA^n$ for all $n$, then $N_n\le HB^n$ for all $n$, for some $H$ and $B$. Consequently, for the canonical sequence
at rational $\delta$ the following are equivalent: the density sums $M_n$ grow at most geometrically; the stream sums
$N_n$ do; each of the statements 1 to 5 of Proposition 14.18(b) holds; the density, stream and potential series converge
on some exterior.

Proof. Weighted norm. Choose $\rho\ge4$ with $S:=\sum_{k<L}|a_k|\rho^k/(|a_L|\rho^L)\le1/16$, and put
$T=|a_L|\rho^L/2$, $r=\rho^{-2}\le1/16$ and $\|H\|_\rho=\sum_{q,m}|h_{q,m}|\rho^m$ for a sine or cosine series
$H=\sum h_{q,m}t^q\sin m\theta$ (or $\cos m\theta$), $m\ge0$. Since $\sin m\theta\cos l\theta=\frac12[\sin(m+l)\theta+\sin(m-l)\theta]$
and $\rho^{|m-l|}\le\rho^{m+l}$, this norm is submultiplicative on the products that occur, and by the frequency bounds
$M_n\le\|F_n\|_\rho\le\rho^{(L+1)n}M_n$ and $N_n\le\|G_n\|_\rho$.

Step 1 (coercivity). Let $i\delta\ge16$, $a=i\delta-2$, $p=1-\delta$, and let $G$ be a sine polynomial of log degree
$K\le i/n_r$. Then $\mathcal L_iG=(-a+D)G\,f_1'-p\,f_1\,\partial_\theta G$ satisfies
$$\|\mathcal L_iG\|_\rho\ge\frac{TL\delta i}8\,\|G\|_\rho .\tag{14.19.1}$$
For a monomial $g\,t^q\sin m\theta$ the top harmonic of $f_1$ produces
$-\frac{a_L}2(La+pm)g\,t^q\sin(m+L)\theta+\frac{a_L}2(pm-La)g\,t^q\sin(m-L)\theta$. The upper parts sit at distinct indices
$(q,m+L)$, so their norm is exactly $T\sum(La+pm)|g_{q,m}|\rho^m=T\Lambda$ with
$\Lambda=La\|G\|_\rho+p\|\partial_\theta G\|_\rho$. The lower parts have modulus at most the upper ones and weight
ratio $\rho^{|m-L|-m-L}=\rho^{-2\min(m,L)}\le r$, so their norm is at most $rT\Lambda$. A lower harmonic $k<L$
contributes at most $|a_k|\rho^k(1+r)\Lambda/2$ (both branches, using $k\le L$), in total at most $(1+r)ST\Lambda$. By the
reverse triangle inequality the part of $\mathcal L_iG$ without $D$ has norm at least
$(1-r-(1+r)S)T\Lambda\ge\frac{223}{256}TLa\|G\|_\rho$. For the part with $D$, $\|DG\|_\rho\le K\|G\|_\rho$ and
$\|f_1'H\|_\rho\le\sum_kk|a_k|\rho^k\frac{1+r}2\|H\|_\rho\le TL(1+r)(1+S)\|H\|_\rho\le\frac{289}{256}TL\|H\|_\rho$. Since
$K\le i/n_r\le\delta i/2$,
$$\|\mathcal L_iG\|_\rho\ge TL\Big[\frac{223(\delta i-2)}{256}-\frac{289\,\delta i}{512}\Big]\|G\|_\rho
=TL\Big[\frac{157\,\delta i}{512}-\frac{223}{128}\Big]\|G\|_\rho ,$$
and the bracket is at least $\delta i/8$ when $\delta i\ge892/93$, in particular when $\delta i\ge16$.

Step 2 (isolating $G_i$). Since $Df_1=0$, $p_1=p$ and $P_i=-a$, the summand $k=i$, $j=1$ of the forcing at order
$i+1$ is exactly $\mathcal L_iG_i$:
$$(\lambda_{i+1}-cD)F_{i+1}=\mathcal L_iG_i+\sum_{k+j=i+1,\ k<i}\big[(P_k+D)G_k\,\partial_\theta F_j-\partial_\theta G_k\,(p_j+D)F_j\big].$$
Put $X_n=\|F_n\|_\rho$ and $Y_n=\|G_n\|_\rho$. The estimate in the proof of Proposition 14.16, repeated in the weighted
norm, bounds the $(k,j)$ summand by $(L+1)C_0\,kj\,Y_kX_j$; and $\|(\lambda_{i+1}-cD)F_{i+1}\|_\rho\le2c\delta i\,X_{i+1}$,
since $\lambda_{i+1}=c\delta i$ and $\kappa_{i+1}\le\delta(i+1)/2$. With $\alpha=8/(TL\delta)$, (14.19.1) gives, for
$i\delta\ge16$,
$$Y_i\le2\alpha c\delta\,X_{i+1}+\alpha(L+1)C_0\sum_{k+j=i+1,\ k<i}j\,Y_kX_j .$$

Step 3 (majorant). By the hypothesis $X_j\le CA_*^j$ with $A_*=\max(1,A\rho^{L+1})$. Put $K_*=\alpha(L+1)C_0CA_*$ and
choose $H_*\ge2\alpha c\delta CA_*$ with $H_*\ge Y_i/A_*^i$ for the finitely many $i$ with $i\delta<16$. Writing $j=l+1$,
$Y_i\le H_*A_*^i+K_*\sum_{l=1}^{i-1}(l+1)A_*^lY_{i-l}$ for all $i\ge1$. With $B=A_*\max(4,8K_*)$ and $y=A_*/B$,
$K_*\sum_{l\ge1}(l+1)y^l=K_*y(2-y)/(1-y)^2\le4K_*y\le\frac12$, and induction gives $Y_i\le2H_*B^i$, hence $N_i\le2H_*B^i$.
The equivalences then follow from Propositions 14.17 and 14.18. $\square$

Corollary 14.19. The dichotomy of Proposition 14.18(c) holds for the density series as well: if the individual
density terms $e^{p_nt}F_n(t,\theta)$ are bounded at every point of some measurable set of positive area (for example,
if the density series converges on such a set, or uniformly on an annulus), then all three series converge on an
exterior; otherwise the density terms are unbounded at almost every point and on a dense residual set. Proof: the
proof that 5 implies 1 in Proposition 14.18(b) applies verbatim with the radial exponent $p_n$ in place of $P_n$
(now $|F_n|\le je^{B}e^{n\delta T_1}$ on the slices), the density log degree $\kappa_n\le n/n_r$ and the frequency bound
$(L+1)n$, and gives a geometric bound on $M_n$; Proposition 14.19 then applies. $\square$ Since
$(t,\theta)\mapsto(e^t\cos\theta,e^t\sin\theta)$ is a local diffeomorphism with Jacobian $e^{2t}>0$, the statements
about area zero and residual sets hold equally in the physical plane. They cannot be strengthened to every point: all
density and stream terms vanish on the axis $\theta=0,\pi$ by the sine symmetry, whatever the growth of the
coefficients.

Remarks. 1. The example at $\delta=4/9$ in Section 14.5(a), with bounded density sums and a factorially large stream,
does not satisfy the next-order density equation; for general admissible inputs the density bound remains insufficient.
2. The proposition does not give the ratio bound (14.16.1), and its base $B$ can be much larger than $A$ (by the factor
$\rho^{L+1}$ and through $K_*$). 3. The two estimates do not close by themselves: the coercive term $\mathcal L_iG_i$ of
Step 2 is the same term that carries $G_{n-1}$ into $F_n$ in the density recursion (the term measured in Section
14.17), so inserting Step 2 into the density estimate bounds $M_n$ by a multiple of $M_n$. 4. Through order 300 at
$\delta=2/3$ both sums decay geometrically, at about $-0.70$ (density) and $-0.68$ to $-0.70$ (stream) decades per
order (NUMERICAL EVIDENCE, Section 14.17).

Status. Proposition 14.19 and Corollary 14.19: PROVED (independent proof, reviewed here and independently confirmed). A geometric
bound on $M_n$, equivalently on $N_n$, at any rational $\delta$: OPEN.

### 14.20 A criterion localized to the small divisors (PROVED: independent proof, reviewed here)

The only unbounded step in the plain norm is the Poisson inverse. This section shows that it can exceed a fixed
multiple of the density only through coefficients of high log degree $k$ attached to shifts $|s|<2k$.

Setting. As in Proposition 14.16, with $F_n=\sum_{m,k}a_{n,m,k}t^k\sin m\theta$. By Section 14.1 a density coefficient at
frequency $m$ enters the stream at frequency $q=m+1$ through the shift $s=P_n+m+1$ and, if $m>1$, at $q=m-1$ through
$s=P_n-m+1$ (its two incidences). For $k\ge0$ put $W_k(s)=\sum_{h\le k}k!/((k-h)!\,|s|^{h+1})$ for $s\ne0$ and
$W_k(0)=1/(k+1)$; this is $\|(D+s)^{-1}t^k\|_*$, with $D^{-1}H=\int_0^tH$. Let $d_*=\gcd(a,2)/b$ and
$$E_n=\tfrac12\sum|a_{n,m,k}|\,W_k(s),$$
the sum running over the coefficients and their incidences with $0<|s|<2k$.

Proposition 14.20. (a) For every polynomial-log density $F_n$ with these frequencies (generated or not), with the
canonical constants, $N_n\le d_*^{-1}M_n+E_n$. (b) For the generated sequence, if $E_n\le BA^n$ for all $n$ with some
$A,B$, then $M_n$ and $N_n$ grow at most geometrically, and the density, stream and potential series converge on an
exterior. (c) If $E_n\le BM_n$ for all $n$, then (14.16.1) holds with $H_0=d_*^{-1}+B$.

Proof. (a) In mode $q$ the stream polynomial is $-\frac12(D+P_n+q)^{-1}H_{q-1}-\frac12(D+P_n-q)^{-1}H_{q+1}$, where $H_m$ is the
density polynomial at frequency $m$; at a resonance $P_n=-q$ the canonical coefficient is this expression minus its
value at $t=0$ (the whole constant, both branches). Removing a constant term does not increase $\|\cdot\|_*$, so
$N_n\le\frac12\sum|a_{n,m,k}|W_k(s)$ over all incidences. Every nonzero shift has $|s|\ge d_*$, since
$bs=2b(1+\ell)-na$ with $\ell\in\mathbb Z$ is a nonzero multiple of $\gcd(a,2b)=\gcd(a,2)$. For the incidences not counted in
$E_n$: $s=0$ gives $W_k\le1$; $k=0\ne s$ gives $W_0=1/|s|\le d_*^{-1}$; $k\ge1$ and $|s|\ge2k$ give $W_k(s)\le2/|s|\le1$,
because successive terms of $W_k$ have ratio at most $k/|s|\le1/2$. Since $d_*\le1$ and each coefficient has at most
two incidences, each with the factor $\frac12$, these contribute at most $d_*^{-1}M_n$. (b) The proof of Proposition
14.16 gives $nM_n\le\kappa\sum_{i+j=n}(iN_i)(jM_j)$ with $\kappa=2(L+1)C_0/(c-1)$. With $x_n=nM_n$, $e_n=nE_n$ and (a),
$x_n\le\kappa d_*^{-1}\sum_{i+j=n}x_ix_j+\kappa\sum_{i+j=n}e_ix_j$. The series $e(z)=\sum e_nz^n$ is holomorphic for $|z|<1/A$, and
the equation $X=Fz+\kappa d_*^{-1}X^2+\kappa e(z)X$, $X(0)=0$, has a holomorphic solution near $0$ by the implicit function
theorem; its coefficients are nonnegative and dominate $x_n$ by induction. Cauchy's estimate bounds $M_n$ geometrically,
(a) then bounds $N_n$, and Proposition 14.5 gives the convergence. (c) follows from (a). $\square$

At $\delta=2/3$ and $f_1=\sin\theta$: $d_*^{-1}=3/2$, $\kappa=6$, and the majorant equation is $X=z+9X^2+6e(z)X$.

Data (certified ball arithmetic at $\delta=2/3$, $f_1=\sin\theta$, through order 315). Every $E_n<(1/4)^n$, the largest
value of $E_n^{1/n}$ being $0.2087$ (at $n=314$). $E_n$ first exceeds $M_n$ at $n=196$, and $E_n/M_n$ reaches $10^{9.57}$
(at $n=314$), while $N_n/M_n<1/4$ through order 315 (and through 322; Section 14.16 Data); so $E_n$ overestimates the stream by many orders and the hypothesis of
(c) is not supported. Over the 27 orders ending at 315 the slopes of $\log_{10}E_n$ in the three residue classes modulo
3 are $-0.671$, $-0.599$, $-0.599$ (compare $\log_{10}(1/4)=-0.602$), and the slope of one class has risen from $-0.693$
(window ending at 150) to $-0.599$. These finite data do not indicate a definite geometric base for $E_n$ (NUMERICAL
EVIDENCE; no extrapolation).

Status. Proposition 14.20: PROVED (independent proof, reviewed here). The hypothesis of (b): OPEN. A failure of (b)'s
hypothesis would not imply divergence, because $E_n$ uses absolute values before the two branches are added.

### 14.21 Edge recurrences with log-free low factors converge (PROVED: independent proof, reviewed here)

The finite data of Section 15 include truncated recursions in which only products with one factor of low order are
kept. This section proves that such recursions converge whenever the low factors carry no logarithm, so any divergence
of the canonical series must come from products of two factors of order above that range.

Definition. For $K\ge1$ the $K$-edge recurrence is the recursion of Section 14.1, with the canonical constants, in which
$Q_n$ keeps exactly the ordered pairs $(i,j)$, $i+j=n$, with $\min(i,j)\le K$, each counted once. It agrees with the full
recursion through order $K+1$. Its sums (when they converge) satisfy the modified equation
$$(cX\cdot\nabla-1)\rho+u_{\le K}\cdot\nabla\rho+u\cdot\nabla\rho_{\le K}-u_{\le K}\cdot\nabla\rho_{\le K}=0,$$
where $\rho_{\le K}$ and $u_{\le K}$ are the sums of the first $K$ terms; for $n>2K$ it is linear in the coefficients of order
above $K$.

Proposition 14.21. Let $\delta=a/b$ be reduced, $f_1$ a nonzero finite real odd sine polynomial with top frequency $L$,
$K\ge1$, and suppose $F_i$ and $G_i$ are independent of $t$ for $i\le K$. This holds whenever $K\delta<4$, because a stream
resonance $P_i=-q$ with $q\ge2$ requires $i\delta\ge4$ (in particular for $K=1$ at every $\delta$, and for $K\le5$ at
$\delta=2/3$). Put $d_*=\gcd(a,2)/b$, $s=2/d_*$ and $\|H\|_s=\sum_qq!\,s^q\|[t^q]H\|_{\ell^1}$. Then there are $A$ and $C_0$ with
$\|F_n\|_s\le C_0A^n$ and $\|G_n\|_s\le(2/d_*)C_0A^n$ for all $n$, and the density, stream and potential series of the
$K$-edge recurrence converge with all weighted Cartesian derivatives on an exterior; the sums are real analytic and
solve the modified equation. At $\delta=2/3$ and $f_1=\sin\theta$ the sharper bounds $\|F_n\|_3\le(23/10)^{n-1}$ ($K=1$) and
$\|F_n\|_3\le(5/2)^{n-1}$ ($K=3$), with $\|G_n\|_3\le3\|F_n\|_3$, hold, and $r\ge4$ suffices in both cases.

Proof. Linear steps. $\|D\|_s=1/s=d_*/2$, and $d_*\le\delta$ gives $cd_*/2\le(c-1)/2$, so the finite Neumann series gives
$\|(\lambda_n-cD)^{-1}\|_s\le1/((c-1)(n-\frac32))$ for $n\ge2$. Every nonzero Poisson shift has modulus at least $d_*$
(Section 14.20), so $\|(D+\sigma)^{-1}\|_s\le1/(d_*-d_*/2)=2/d_*$; the zero shift is integration from $0$, of norm $s=2/d_*$;
each density coefficient has two incidences with the factor $\frac12$, and removing the whole resonant constant does not
increase the norm. Hence $\|G_n\|_s\le(2/d_*)\|F_n\|_s$. Products. Multiplication by a $t$-independent trigonometric
polynomial $H$ acts column by column, so $\|HV\|_s\le\|H\|_{\ell^1}\|V\|_s$; this is the only place where the hypothesis
is used (the norm is not an algebra for general log polynomials). Recursion. For $n>2K$ each retained pair has exactly
one index $i\le K$, and $j=n-i\ge2$. In the two ordered terms no $t$-derivative falls on the low factor, and with the
frequency bounds $\le(L+1)j$, $|p_j|\le j$, $|P_j|\le(2-\delta)j$, $d_*/2\le jd_*/4$ and $j/(n-\frac32)\le\frac43$ one gets
$$M_n\le\sum_{i\le K}b_iM_{n-i},\qquad b_i=\frac{4(L+1)}{3(c-1)}\Big\{\big[|P_i|+i(1+\tfrac{d_*}4)\big]Q_i
+\tfrac2{d_*}\big[(2-\delta+\tfrac{d_*}4)i+|p_i|\big]H_i\Big\},$$
with $M_n=\|F_n\|_s$, $H_i=\|F_i\|_{\ell^1}$, $Q_i=\|G_i\|_{\ell^1}$. With $A=\max(1,2\sum b_i)$ one has $\sum b_iA^{-i}\le\frac12$, and
induction from the first $2K$ orders gives the bounds. Convergence. $\|H\|_*\le\|H\|_s$, the degree bounds of Section 14.2
persist when pairs are removed, and the proof of Proposition 14.5 uses only the linear potential identities and these
degree bounds; so it applies to the $K$-edge recurrence. Absolute convergence permits regrouping, which gives the
modified equation. The case $\delta=2/3$: here $d_*=2/3$, $s=3$, the shifts have $|\sigma|\ge2/3$, so $\|(D+\sigma)^{-1}\|_3\le3$ and
$\|(2(n-1)-3D)^{-1}\|_3\le1/(2n-3)$. With the exact values $\|G_1\|=3/20$, $\|F_2\|=1/10$, $\|G_2\|=33/4480$, $\|F_3\|=251/44800$,
$\|G_3\|=637/537600$, the same computation with the exact exponents gives $M_n\le\sum_{i\le K}B_iM_{n-i}$ for $n\ge4$ ($K=1$) and
$n\ge7$ ($K=3$), with $B_1=23/10$, $B_2=929/2240$, $B_3=2537/53760$; the first orders are checked exactly, and
$B_1/(5/2)+B_2/(5/2)^2+B_3/(5/2)^3=831077/840000<1$. Since $\|H(t)\|_{\ell^1}\le e^{|t|/3}\|H\|_3$, convergence holds for
$r>A^{3/2}$, and $(5/2)^{3/2}<4$. $\square$

Remarks. 1. At $\delta=2/3$ these recurrences have geometric bounds in the norm with weight $q!\,3^q$, while in the
full recursion the same norm grows faster than geometrically through order 290 in the certified data of Section
14.15(c) (finite data, NUMERICAL EVIDENCE). So that growth comes from the omitted products, in which both factors have
order above $K$. 2. The proposition gives finite sufficient radii, not the observed rates
(Section 15). It does not apply to edge recurrences whose low factors carry logarithms ($K\ge6$ at $\delta=2/3$; for those see
Proposition 14.21b, which gives a Gevrey bound of order below $1/Q$), and it says nothing about the full recursion.

Status. Proposition 14.21: PROVED (independent proof, reviewed here; the exact low-order values and the finite checks are
part of the independent proof).

Proposition 14.21b (edge recurrences with logarithmic low factors; PROVED: independent proof, reviewed here). Let
$\delta=a/b\in(0,1)$ in lowest terms, $c=1/(1-\delta)$, $f_1\ne0$ a finite real sine polynomial with top frequency $L$, and
$K\ge1$. In the $K$-edge recurrence (canonical constants, each ordered pair with $\min(i,j)\le K$ counted once) let
$d_i=\max(\deg_tF_i,\deg_tG_i,0)$ for $i\le K$ and $\sigma=\max_{i\le K}d_i/i$. Put $d_*=\gcd(a,2)/b$, $s=2/d_*$ and
$\|H\|_s=\sum_{q\ge0}q!\,s^q\|[t^q]H\|_{\ell^1}$. Then there are explicit $C_0,A>0$ (from finitely many coefficients) with
$$\|F_n\|_s\le C_0A^n(n!)^\sigma,\qquad\|G_n\|_s\le sC_0A^n(n!)^\sigma\qquad(n\ge1).$$
If $\sigma=0$, the density and stream series converge with every weighted derivative on $r>A^{1/\delta}$. At $\delta=2/q_0$
($q_0\ge3$ an integer): $\sigma=0$ if $K<2q_0$, and $\sigma\le(m-1)/(q_0m)<1/q_0$ with $m=\lfloor K/q_0\rfloor$ if $K\ge2q_0$. At
$\delta=2/3$ this gives the Gevrey orders $2/9$ for $K=10$ and $3/10$ for $K=30$, below the order $1/3$ of Section 14.3.

Proof. In $\|\cdot\|_s$, $\|\partial_t\|\le1/s=d_*/2$. Every nonzero Poisson shift $P_n\pm j$ lies in
$\frac1b(2b\mathbb Z-na)$, so has modulus at least $d_*$, and $(\partial_t+\alpha)^{-1}$ has norm at most $1/(d_*-d_*/2)=s$;
integration from $0$ at a zero shift has norm $s$, and the deletion of the resonant constant is contractive. Each density
mode feeds two stream modes with weight $\frac12$, so $\|G_n\|_s\le s\|F_n\|_s$. Since $cd_*/2\le c\delta/2=(c-1)/2$,
$\|(\lambda_n-c\partial_t)^{-1}\|\le1/((c-1)(n-\frac32))$ for $n\ge2$. The degree induction of Section 14.2 survives the deletion
of products and gives $\deg F_n\le\max(0,\lfloor(n-1)/q_0\rfloor-\epsilon)$, $\deg G_n\le\max(0,\lfloor n/q_0\rfloor-\epsilon)$, with
$q_0=2b/\gcd(a,2)$ and $\epsilon=1$ if $a/\gcd(a,2)=1$, else $0$ (at $\epsilon=1$ use $\max(0,u-1)+\max(0,v-1)\le\max(0,u+v-1)$; a
stream degree rises only at a resonance, and for $\epsilon=1$ the first multiple of $q_0$ is not one). If $\deg U\le d$ and
$\deg U+\deg V\le n$, then $\|UV\|_s\le n^d\|U\|_s\|V\|_s$, since $\binom{q+l}{l}\le n^l$. For $n>2K$ every retained pair has
exactly one index $i\le K$ and both orientations occur; with $|p_j|\le j$, $|P_j|\le(2-\delta)j$, the support bound
$\deg_\theta\le(L+1)n$ and $j/(n-\frac32)\le\frac43$ this gives $M_n\le\sum_{i\le K}b_in^{d_i}M_{n-i}$, where $M_n=\|F_n\|_s$,
$$b_i=\frac{4(L+1)}{3(c-1)}\Big\{\big[|P_i|+\tfrac1s+i(1+\tfrac1s)\big]\|G_i\|_s+s\big[i(2-\delta+\tfrac1s)+|p_i|+\tfrac1s\big]\|F_i\|_s\Big\}.$$
Let $A=\max(1,2\sum_i2^{\sigma i}b_i)$ and $C_0=\max_{n\le2K}M_n/(A^n(n!)^\sigma)$. For $n>2K$, each factor of $n!/(n-i)!$
exceeds $n/2$, so $n^{d_i}((n-i)!/n!)^\sigma\le2^{\sigma i}n^{d_i-\sigma i}\le2^{\sigma i}$, and induction gives
$M_n\le C_0A^n(n!)^\sigma\sum_i2^{\sigma i}b_iA^{-i}\le\frac12C_0A^n(n!)^\sigma$. If $\sigma=0$, $\|H(t)\|_{\ell^1}\le e^{|t|/s}\|H\|_s$ and
$e^{\log r/s}$ is a fixed power of $r$, so the late terms are dominated by a geometric series on $r\ge R$ for every
$R>A^{1/\delta}$; derivatives cost polynomial factors. For $\delta=2/q_0$, $\epsilon=1$ and $d_i\le\max(0,\lfloor i/q_0\rfloor-1)$; on
the block $q_0l\le i<q_0(l+1)$ the ratio $d_i/i$ is at most $(l-1)/(q_0l)$, which increases with $l\le m$. $\square$

A positive $\sigma$ is only a Gevrey upper bound for the modified recurrence: it proves neither convergence nor divergence,
and says nothing about the full recursion. With $\sigma=0$ it recovers Proposition 14.21 with cruder constants.

Proposition 14.21c (the highest log column of the 1-edge recurrence at $\delta=2/3$; PROVED: independent proof, reviewed
here, with an independent exact reproduction). In the 1-edge recurrence (pairs $(1,n-1)$ and $(n-1,1)$) at $\delta=2/3$,
$f_1=\sin\theta$, with canonical constants, $\deg_tF_n\le\max(0,\lfloor(n-1)/3\rfloor-1)$, $\deg_tG_n\le\max(0,\lfloor n/3\rfloor-1)$,
and for $k\ge2$ the top column of $G_{3k}$ is $[t^{k-1}]G_{3k}=b_k\sin((2k-2)\theta)$ with
$b_2=-\frac{9589}{73728000000}$, $b_3=-\frac{37847783}{8138627481600000000}$ and $b_{k+1}=R(k)b_k$ for $k\ge3$,
$$R(k)=\frac{(k-1)(2k-1)P(k)}{14400k^2(3k-4)(3k-2)(3k+1)(3k+2)(6k-5)(6k-1)},\quad
P(k)=6480k^5-3132k^4-23454k^3+29472k^2-10791k+880.$$
$P(x+3)=6480x^5+94068x^4+522162x^3+1398858x^2+1818927x+921445$ has positive coefficients, so every $b_k<0$, and
$kR(k)\to1/3240$, so $((k-1)!\,|b_k|)^{1/k}\to1/3240$. The three highest-degree density and stream subsequences after each
resonance have the same factorially weighted rate, and the subseries formed by these top columns are entire in
$(r^{-\delta},\log r)$. The coefficient $[t^{82}\sin165\theta]F_{250}=-\frac{164}{747}b_{83}$ is nonzero but smaller than
$2^{-1075}$ in modulus, so binary64 arithmetic records it as zero; this is one mechanism by which a floating computation
loses its top log columns. Nothing follows for the lower columns.

Proof. At $n=3k+r$, $r=1,2,3$, the top degree is $k-1$; there $\partial_t$ terms drop out and the density recurrence reads
$2(n-1)a_r=P_{n-1}h_{r-1}f_1'-p_1h_{r-1}'f_1+P_1g_1a_{r-1}'-p_{n-1}g_1'a_{r-1}$ with $a_0=0$, $h_0=\sin((2k-2)\theta)$,
$g_1=-\frac3{20}\sin2\theta$ (normalized by $b_k$). The Poisson inverse at $3k+1$, $3k+2$ is nonresonant, and at $3k+3$ the
resonant operator $\partial_t(4k-\partial_t)$ in the mode $2k$ is forced by $-2k$ times the $\sin((2k-1)\theta)$ coefficient of
$a_3$, so $b_{k+1}/b_k=-[\sin((2k-1)\theta)]a_3/(2k)$. Carrying the four steps symbolically in $k$ with signed frequencies gives
$a_1=-\frac{2(k-1)}{9k}\sin((2k-1)\theta)-\frac{k-1}{9k}\sin((2k-3)\theta)$ and $[\sin((2k-1)\theta)]a_3=-2kR(k)$; for $k\ge3$ no
reflected frequency meets $2k-1$. The limits of the offset coefficients of $a_1,a_2,a_3,h_1,h_2$ are nonzero ($-\frac29$,
$\frac1{54}$, $-\frac1{1620}$, $\frac1{12}$, $-\frac1{72}$), which gives the rates of the other top subsequences. $\square$
Checks here (accompanying artifacts): a direct exact polynomial-log 1-edge recurrence through order 24 reproduces
$b_2$, $b_3$, $b_{k+1}/b_k=R(k)$ for $k=3,\dots,7$, the profile $a_1$ and the degree bounds; a symbolic computation in $k$
reproduces the cycle identity; the exact product formula gives $|[t^{82}\sin165\theta]F_{250}|<2^{-1075}$
($\log_{10}\approx-415.5426$).

### 14.22 The highest Fourier mode of the edge hierarchy and of the full series (PROVED: independent proofs, reviewed here)

This section sharpens Proposition 8.2 and compares the edge recurrences of Section 14.21 with the full recursion in the
one Fourier sector where both are explicit: the top frequency. None of its statements concerns the full angular norm.

Notation. $\delta\in(0,1)$, $c=(1-\delta)^{-1}$, $d=c-1$; $f_1$ is a nonzero finite real odd sine polynomial with top
frequency $L$ and top coefficient $\alpha$; $B=L+1$, $\eta=B-\delta$, $a=2/\eta$, $b=2(B-1)/\eta\in(1,2)$, $\nu=1/b\in(\frac12,1)$,
$\mathcal B=\mathcal B(a,b)$ and $R_H=4d[a\mathcal B]^{1/a}$ (so $R_{\rm top}=R_H/|\alpha|$ in Proposition 8.2). The recursion is
the canonical one of Section 14.1 (whole resonant constant zero), or the pure one where it exists at all orders; they
have the same top coefficients. Write $A_n=(-1)^{n-1}\alpha^nh_n$ for the coefficient of $\sin((Bn-1)\theta)$ in $F_n$, and
$h_{n,K}$ for the same quantity in the $K$-edge recurrence (pairs with $\min(i,j)\le K$). Both are constant in $\log r$, and
$$h_{n,K}=\frac1{4d(n-1)}\sum_{i+j=n,\ \min(i,j)\le K}\Big[\frac{2Bj}{\eta i+2}-1\Big]h_{i,K}h_{j,K},\qquad h_{1,K}=1,\tag{14.22.1}$$
with $h_n$ given by the same formula without the restriction (Proposition 8.2). Put
$V_K(z)=\sum_{i\le K}h_iz^i/(\eta i+2)$, let $R_K>0$ solve $V_K(R_K)=2d/B$, and let $p_{i,K}=Bh_iR_K^i/[2d(\eta i+2)]$
($1\le i\le K$, a probability vector), $\mu_K=\sum_iip_{i,K}$, $s_K=2-\delta/B-(B-2)/(B\mu_K)$.

Proposition 14.22.
(a) Comparison. $0<h_{n,K}\le h_{n,K+1}\le h_n$; $h_{n,K}=h_n$ for $n\le2K+1$ (indeed the whole $K$-edge recurrence agrees
with the full one through order $2K+1$); at $m=K+1$,
$h_{2m}-h_{2m,K}=[2Bm/(\eta m+2)-1]h_m^2/[4d(2m-1)]>0$, and $h_{n,K}<h_{n,K+1}$ for all $n\ge2K+2$. For $0<r<r'<R_H$,
$\sup_{|z|\le r}|H(z)-H_K(z)|\le(r/r')^{2K+2}H(r')$, where $H=\sum h_nz^n$, $H_K=\sum h_{n,K}z^n$.
(b) Edge radii. $\lim_nh_{n,K}^{1/n}=1/R_K$. Moreover $R_K>R_{K+1}>R_H$, $R_K\downarrow R_H$, and
$0<R_K-R_H\le4d(\eta+2)/[\eta(K+1)+2]$. For $K=1$, $R_1=2d(\eta+2)/B$ ($20/3$ at $\delta=2/3$, $B=2$).
(c) Fixed-edge asymptotics. For each fixed $K$ there is $\kappa_K>0$ with
$h_{n,K}=\kappa_KR_K^{-n}n^{-s_K}[1+O(1/n)]$. The means satisfy $1=\mu_1<\mu_2<\dots<b$ and $\mu_K\to b$, so
$s_1=1+(2-\delta)/B$ and $s_K\to1+\nu$; for $B=2$, $s_K=2-\delta/2$ for every $K$ ($5/3$ at $\delta=2/3$), and for $B>2$, $s_K$
increases strictly. For $B=2$, $K=1$, with $a=2/(2-\delta)$, $s=2-\delta/2$ and $R_1=d(4-\delta)$,
$h_{n,1}=\frac12R_1^{-(n-1)}\frac{\Gamma(n+a-s)\Gamma(1+a)}{\Gamma(1+a-s)\Gamma(n+a)}$ for $n\ge2$ and $\kappa_1=\frac{R_1}2\frac{\Gamma(1+a)}{\Gamma(1+a-s)}$.
(d) The full top coefficient. With $C=(ab\mathcal B)^\nu$ and $\mathcal K=4dC\nu/\Gamma(1-\nu)>0$,
$$h_n=\mathcal K\,R_H^{-n}\,n^{-1-\nu}\,[1+O(n^{-\nu})].$$
In particular $h_{n+1}/h_n\to1/R_H$ and $\lim_nh_n^{1/n}=1/R_H$ (an ordinary limit, not only a lim sup).
(e) Approach rates. $R_K-R_H\sim\frac{BR_H\mathcal K}{4d(B-1)(1+\nu)}K^{-1-\nu}$, $b-\mu_K\sim\frac{B\mathcal K}{2d\eta\nu}K^{-\nu}$, and for
$B>2$, $(1+\nu)-s_K\sim\frac{(B-2)\mathcal K}{4d(B-1)}K^{-\nu}$.
(f) A derivative obstruction at the critical radius. Let $r_*=(|\alpha|/R_H)^{1/\delta}$. At $r=r_*$ the density series is
not absolutely summable in $C^1$ in $\theta$, and its twice $\theta$-differentiated terms do not tend to zero in $C^0$; the
stream series is not absolutely summable in $C^2$, and its thrice differentiated terms do not tend to zero. For
$r<r_*$ the density terms are unbounded. Hence uniform termwise convergence of two angular density derivatives on
$\{r\ge R\}$ requires $R>r_*$. In the Wiener norm $\|\cdot\|_\sigma$ the same holds with $r_\sigma=(|\alpha|e^{B\sigma}/R_H)^{1/\delta}$.
(g) A limitation. For the positive scalar recurrence $x_1=1$, $x_n=\sum_{i+j=n}\min(i,j)!\,x_ix_j$, every $K$-edge
truncation has positive radius, agrees with $x_n$ through $2K+1$ and increases with $K$, but $\sum x_nz^n$ has radius zero.
So convergence of every fixed edge recurrence, with growing prefix agreement and monotonicity, does not imply
convergence of the full recurrence.

Proof. (a) The symmetrized kernel $C_{i,j}=B[\frac j{\eta i+2}+\frac i{\eta j+2}]-1$ is positive (Proposition 8.2: the
bracket exceeds $\frac{2(i+j)}{\eta(i+j)+4}$ by $\eta[\eta(i+j)+2](i-j)^2/[(\eta i+2)(\eta j+2)(\eta(i+j)+4)]\ge0$, so
$C_{i,j}\ge[(B+\delta)(i+j)-4]/[\eta(i+j)+4]>0$). Increasing $K$ adds nonnegative terms and increases the factors, which
gives the ordering by induction; for $n\le2K+1$ no pair is omitted; at $n=2K+2$ only $(K+1,K+1)$ is omitted, which gives
the difference; the retained pair $(1,n-1)$ with positive kernel propagates strictness. The differences vanish
through $2K+1$ and are dominated by $h_n$, which gives the sup bound.
(b) For $n>2K$ each retained pair has exactly one index $i\le K$, so
$h_{n,K}=\sum_{i\le K}q_{n,i}h_{n-i,K}$ with $q_{n,i}=\frac{h_i}{2d(n-1)}\{B[\frac{n-i}{\eta i+2}+\frac i{\eta(n-i)+2}]-1\}$. With
$c_i=Bh_i/[2d(\eta i+2)]$ one has exactly
$q_{n,i}/c_i=1+\{1-i-(\eta i+2)/B+i(\eta i+2)/(\eta(n-i)+2)\}/(n-1)$; since $n-i>i$ and $\eta i+2>B$ this gives
$(1-D_i/(n-1))c_i\le q_{n,i}<c_i$ with $D_i=i-1+(\eta i+2)/B$. The equation $\sum_ic_i\lambda^{-i}=1$ is $V_K(1/\lambda)=2d/B$. A
supersolution $C\lambda^n$ and, for each $\varepsilon$, a subsolution $C_\varepsilon\lambda_\varepsilon^n$ with
$(1-\varepsilon)\sum c_i\lambda_\varepsilon^{-i}=1$ give the root limit. Proposition 8.2 gives $H(R_H)=4d$ and $J(R_H)=2d/B$ (monotone
convergence of the positive boundary sums); the omitted terms of $J$ are positive, so $V_K(R_H)<2d/B$, $R_K>R_H$, and
adding the $(K+1)$st term gives $R_{K+1}<R_K$. Since $V_K'\ge1/(\eta+2)$, $R_K-R_H\le(\eta+2)[J(R_H)-V_K(R_H)]\le
(\eta+2)H(R_H)/[\eta(K+1)+2]$.
(c) One has $q_{n,i}/c_i=1-D_i/n+O(n^{-2})$ uniformly in $i\le K$, and $D_i=(2-\delta/B)i+(2/B-1)$, so
$\sum_ip_{i,K}D_i=\mu_Ks_K$. For $w_n=h_{n,K}R_K^nn^{s_K}$ this gives $w_n=\sum_ia_{n,i}w_{n-i}$ with $a_{n,i}>0$ and
$\sum_ia_{n,i}=1+O(n^{-2})$. Hence $0<m\le w_n\le M$. Writing the recurrence with a row-stochastic companion matrix, every
product of $K$ consecutive matrices has entries at least $\alpha_0^K$ for some $\alpha_0\in(0,\frac1{2K})$, so the oscillation of
the state vector contracts by $1-K\alpha_0^K$ every $K$ steps up to an $O(n^{-2})$ error; this gives $|w_n-w_{n-1}|=O(n^{-2})$,
so $w_n\to\kappa_K\ge m>0$ with error $O(1/n)$. For the means, $p_{i,K+1}<p_{i,K}$ for $i\le K$ (since $R_{K+1}<R_K$) and both
vectors have mass one, so $\mu_{K+1}-\mu_K=\sum_{i\le K}(K+1-i)(p_{i,K}-p_{i,K+1})>0$. The limit weights
$p_{i,\infty}=Bh_iR_H^i/[2d(\eta i+2)]$ have mass $BJ(R_H)/(2d)=1$ and mean $\frac B{2d\eta}[H(R_H)-2J(R_H)]=b$; the bound in (b)
gives $K\log(R_K/R_H)\le4d(\eta+2)/(\eta R_H)$, hence $ip_{i,K}\le e^{C}ip_{i,\infty}$, and dominated convergence gives $\mu_K\to b$.
The limit of $s_K$ is $2-\delta/B-(B-2)/(Bb)=1+1/b$. For $B=2$, $K=1$: $q_{n,1}=R_1^{-1}(n-1+a-s)/(n-1+a)$ for $n\ge3$, and
$h_{2,1}=q_{2,1}/2$ because the central pair occurs once; the gamma product follows, all its arguments are positive
($1+a-s=(4-\eta^2)/(2\eta)>0$), and Stirling's formula gives $\kappa_1$.
(d) With $x=H/(4d)$ and $v=BJ/(2d)$ the recursion is $Ex=x(1-x)/(1-v)$, $Ev=a(Bx-v)$, $E=z\partial_z$. On $|z|=R_H$,
$z\ne R_H$, the strict triangle inequality for the positive coefficients of $J$ gives $|v|<1$, so the system is
holomorphic at the boundary values and $H$ continues across every such point. Near $R_H$, with $u=1-x$, the beta
parametrization reads $1-(z/R_H)^a=u^b\Phi(u)/(b\mathcal B)$ with $\Phi$ holomorphic and $\Phi(0)=1$; inverting,
$H=4d-4dC(1-z/R_H)^\nu+O(|1-z/R_H|^{2\nu})$ in a slit neighborhood, uniformly in sectors $|\arg(1-z/R_H)|\le\pi-\epsilon$. So $H$ is
holomorphic in a domain $\{|z|<R_H+\epsilon,\ z\ne R_H,\ |\arg(z-R_H)|>\vartheta\}$ with $\vartheta<\pi/2$. A Cauchy integral over the
standard contour (a circle of radius $R_H/n$ about $R_H$, two rays at angle $\pm\varphi$, $\vartheta<\varphi<\pi/2$, and an outer arc)
bounds the coefficients of the remainder by $O(R_H^{-n}n^{-1-2\nu})$, and $[z^n](1-z/R_H)^\nu=R_H^{-n}\Gamma(n-\nu)/[\Gamma(-\nu)\Gamma(n+1)]$
with $\Gamma(n-\nu)/\Gamma(n+1)=n^{-1-\nu}(1+O(1/n))$ gives the formula, the prefactor being $-4dC/\Gamma(-\nu)=\mathcal K>0$.
(e) From (d), the tail $\tau_K=J(R_H)-V_K(R_H)\sim\frac{\mathcal K}{\eta(1+\nu)}K^{-1-\nu}$. The derivative terms of $V_K$ on
$[R_H,R_K]$ are dominated by $e^C$ times the summable terms of $J'(R_H)$, and $R_HJ'(R_H)=[H(R_H)-2J(R_H)]/\eta=2db/B$, so
$\tau_K=(R_K-R_H)(J'(R_H)+o(1))$, which gives the first formula. Then $b-\mu_K=\sum_{i>K}ip_{i,\infty}-\sum_{i\le K}ip_{i,\infty}[(R_K/R_H)^i-1]$;
the first sum is $\sim\frac{B\mathcal K}{2d\eta\nu}K^{-\nu}$ and the second is $O(K^{-2\nu})$. The third formula follows from
$(1+\nu)-s_K=\frac{B-2}B\frac{b-\mu_K}{b\mu_K}$.
(f) A sine or cosine coefficient of frequency $m$ is bounded by $\frac4\pi$ times the sup norm, and $\partial_\theta^k$ multiplies the
top coefficient by $(Bn-1)^k$. At $r_*$, $|A_n|r_*^{1-n\delta}=r_*h_nR_H^n$, so by (d) the $k$-th derivative of the $n$-th density
term has sup norm at least a constant times $n^{k-1-\nu}$, and the stream term (top coefficient $-A_n/[2(\eta n+2)]$, one
more frequency) at least a constant times $n^{k-2-\nu}$; $\nu<1$ gives the four assertions. For $r<r_*$ the terms grow
geometrically. The Wiener-norm version is the same with the factor $e^{\sigma(Bn-1)}$.
(g) For $n>2K$ each retained pair has one index $i\le K$, so $x_{n,K}=\sum_{i\le K}c_ix_{n-i,K}$ with $c_i=2\,i!\,x_i$, and
$A=\max(1,2\sum c_i)$ gives $x_{n,K}\le CA^n$. For the full recurrence $x_{2m}\ge m!\,x_m^2\ge m!$. $\square$

Remarks. 1. Part (d) identifies the singularity of the top-mode generating function: a branch point of exponent $\nu$ at
$z=R_H$, and no other singularity on its circle. Parts (b), (c), (e) show that the edge hierarchy approximates this sector
well: every fixed edge has the right kind of growth ($R_K\downarrow R_H$, polynomial exponent $s_K\to1+\nu$), and the
approximation error in the radius is of order $K^{-1-\nu}$.
2. Part (g) shows that this agreement alone cannot decide convergence of the full recursion: the top sector is one
sector, and the edge recurrences omit exactly the products of two high factors that drive the factorial growth
discussed in Sections 14.11 and 14.15. A bound uniform in $K$ would be additional information.
3. Values at $\delta=2/3$: for $B=2$, $R_H=5.621567$, $\nu=2/3$, $\mathcal K=1.833148$, $R_1=20/3$, $\kappa_1=3.925572$; for $B=4$,
$R_H=4.103676$, $\nu=5/9$, $\mathcal K=2.474643$. An independent double-precision evaluation of (14.22.1) at $B=2$ gives
$h_nR_H^nn^{5/3}=1.82748,\ 1.83022,\ 1.83193,\ 1.83262$ at $n=100,\ 1000,\ 5000,\ 20000$, approaching $\mathcal K$ at the rate
$n^{-2/3}$ allowed by (d) (NUMERICAL EVIDENCE, a consistency check only), and the gamma product in (c) reproduces the
exact $h_{n,1}$ ($h_{2,1}=1/40$) to 30 digits at $n=2,3,10,60$.
4. For $f_1=\sin\theta$ at $\delta=2/3$, (f) gives the necessary condition $R>r_*=R_H^{-3/2}=0.0750$ for uniform termwise
$C^2$ convergence of the canonical density series. The plain sums of Section 14.6 have $M_n^{1/n}=0.1942$ at $n=290$, above
$1/R_H=0.1779$, so in those finite data the top sector carries a geometric rate close to, but below, that of the plain
sums. Convergence of the full canonical series is not addressed by (f).

Status. Proposition 14.22: PROVED (independent proofs, reviewed here line by line; the finite checks in Remark 3 are
consistency checks, not part of the proof).

### 14.23 Growth laws from a shifted projection (PROVED: independent proof, reviewed here and independently confirmed)

The late canonical data at $\delta=2/3$ (the continuation of Section 14.16 and the accompanying numerical report) show coefficient arrays that
nearly repeat every three orders after a shift of the Fourier index by one. The following elementary statement converts
such a pattern into norm growth, exactly, so that the two finite-order tail models below have definite consequences.

Proposition 14.23. Let $x_n\ne0$ ($n\ge1$) lie in a real Hilbert space, let $S$ be a linear isometry and $Q\ge1$, and for $n>Q$
put $a_n=\langle Sx_{n-Q},x_n\rangle/\|x_{n-Q}\|^2$, $r_n=x_n-a_nSx_{n-Q}$ and $e_n=\|r_n\|/\|x_n\|$. Then, whenever $a_n\ne0$,
$$\frac{\|x_n\|}{\|x_{n-Q}\|}=\frac{|a_n|}{\sqrt{1-e_n^2}},\qquad\text{in particular}\qquad\|x_n\|\ge|a_n|\,\|x_{n-Q}\|.\tag{14.23.1}$$
(a) If $|a_n|\to A>0$ and $e_n\to E<1$ (along all residue classes modulo $Q$), then $\|x_n\|^{1/n}\to(A/\sqrt{1-E^2})^{1/Q}$.
(b) If $C_-n^\beta\le|a_n|\le C_+n^\beta$ and $e_n\le E<1$ for all large $n$, then $K_-B_-^n(n!)^{\beta/Q}\le\|x_n\|\le K_+B_+^n(n!)^{\beta/Q}$
for some positive constants.
(c) If $|a_n|\ge Cn^\beta$ with $C,\beta>0$ for all large $n$ in one residue class modulo $Q$, then
$\limsup\|x_n\|^{1/n}=\infty$; no bound on $e_n$ is needed.
(d) Let $x_n$ be the coefficient array $(F_{n,q,j})$ of the canonical density at order $n$ (log degree $q$, Fourier index $j$),
in $\ell^2$, and $S$ the index shift $(Sx)_{q,j+1}=x_{q,j}$, $(Sx)_{q,0}=0$, at a rational $\delta\in(0,1)$ with a nonzero finite real
odd sine profile $f_1$ and the canonical normalization. Under (a), the density, stream and potential series converge with all
weighted Cartesian derivatives on some exterior. Under (c), the individual stream terms are bounded only on a null meagre
subset of the plane, and the same holds for the radial-velocity and potential series.

Proof. $r_n\perp Sx_{n-Q}$ and $\|Sx_{n-Q}\|=\|x_{n-Q}\|$, so $\|x_n\|^2=a_n^2\|x_{n-Q}\|^2+\|r_n\|^2$; dividing by $\|x_n\|^2$ gives
(14.23.1). (a) Telescope $\log\|x_n\|$ along each residue class: the increments tend to $\log A-\frac12\log(1-E^2)$, and the
number of increments up to $n$ is $n/Q+O(1)$. (b) The increments lie between $\log C_-+\beta\log n$ and
$\log C_+-\frac12\log(1-E^2)+\beta\log n$, and along $n=s+kQ$, $\sum_{j\le k}\log(s+jQ)=k\log Q+\log k!+O(\log k)=\frac1Q\log n!+O(n)$.
(c) Use only the lower bound in (14.23.1) on that class; $(n!)^{\beta/(Qn)}\to\infty$. (d) The array has at most $Cn^2$
nonzero positions (log degree and frequency are linear in $n$), so $\|x\|_2\le\|x\|_1\le Cn\|x\|_2$ for the plain sum
$M_n=\|x_n\|_1$. Under (a), $M_n$ grows at most geometrically, and Propositions 14.19 and 14.18(c) give the convergent
exterior solution. Under (c), $M_n\ge\|x_n\|_2$ has no geometric bound, so by Proposition 14.19 neither has $N_n$, and
Proposition 14.18(b),(c) gives the second alternative. $\square$

Proposition 14.24 (exponential growth of the multiplier; PROVED: independent proof, reviewed here and independently
confirmed). In the setting of Proposition 14.23 fix one residue class modulo $Q$.
(a) If eventually $a_n\ne0$ and $e_n\le E<1$ on the class, and $\log_{10}|a_n|/n\to\beta\in\mathbb R$ along it, then
$\log_{10}\|x_n\|/n^2\to\beta/(2Q)$ along it.
(b) If $\liminf\log_{10}|a_n|/n\ge\beta>0$ along the class (no bound on $e_n$), then $\liminf\log_{10}\|x_n\|/n^2\ge\beta/(2Q)$ along it,
so $\limsup\|x_n\|^{1/n}=\infty$ and $\sum x_nz^n$ has radius zero; in the setting of Proposition 14.23(d) the conclusion of its
case (c) follows.
(c) (Exact linear model.) If $\log_{10}|a_n|=\alpha+\beta n$ and $e_n=E$ exactly on the class, put $d=-\frac12\log_{10}(1-E^2)$; then
$\log_{10}\|x_n\|=\frac\beta{2Q}n^2+\big(\frac{\alpha+d}Q+\frac\beta2\big)n+C$ on the class, and for $\beta>0$ its continuous interpolation is
smallest at $n=-\frac{\alpha+d}\beta-\frac Q2$.

Proof. By (14.23.1), $\log_{10}\|x_n\|-\log_{10}\|x_{n-Q}\|=\log_{10}|a_n|+\vartheta_n$ with $0\le\vartheta_n\le-\frac12\log_{10}(1-E^2)$. Write
$n=n_0+kQ$ and telescope from a fixed large $n_0$: $\sum_{j=1}^k(n_0+jQ)=\frac{n^2-n_0^2}{2Q}+\frac{n-n_0}2$, the errors
$o(n_0+jQ)$ add up to $o(n^2)$ and the $\vartheta$ terms to $O(n)$; divide by $n^2$. For (b) use only $\|x_n\|\ge|a_n|\|x_{n-Q}\|$ and
$\log_{10}|a_n|\ge(\beta-\eta)n$ eventually, telescope, divide by $n^2$ and let $\eta\downarrow0$. (c) is the same telescoping with the
exact increments $\alpha+\beta n+d$. $\square$

Application at $\delta=2/3$ (NUMERICAL EVIDENCE, conditional on the order-329 midpoints of the continuation). With
$Q=3$ and the shift above, the certified multipliers and residuals are $(a_n,e_n)=(-0.02293,\,0.0141)$ at $n=350$ and
$(-0.02365,\,0.00095)$ at $n=365$; $|a_n|$ increases slowly (about $0.0228$ at 348, $0.0238$ at 369, $0.0241$ at 378). Two tail
models fit $\log_{10}|a_n|$ on 348 to 370 equally well: $|a_n|\propto n^{0.555}$, which under (b) and (c) would mean coefficient arrays
growing like $(n!)^{0.185}$ times a geometric factor and a divergent series, and $|a_n|\to0.0409$ with a $1/n$ correction,
which with $e_n\to0$ would give an array root rate $0.0409^{1/3}\approx0.345$ under (a). With the orders through 390 the
increase per period of $\log_{10}|a_n|$ is nearly constant, $+0.0016$ from 366 to 390 (one step $+0.0014$), and the fits on 357 to 390
give (unrounded, every order) $\beta=0.4550$ and $|a_\infty|=0.03771$, again with equal residuals, and a third law
$\log_{10}|a_n|=\alpha+\beta'n$ with $\beta'=0.000529$, $\alpha=-1.8188$ fits as well (residuals $5.03$, $5.20$, $4.93$ times $10^{-4}$;
on 357 to 400, fitted to five-decimal multipliers: $\beta=0.464$, $|a_\infty|=0.0383$, $\beta'=0.000533$, residuals $5.0$, $5.5$, $4.8$ times $10^{-4}$); on windows this short the first two models agree to within
about $10^{-4}$ in $\log_{10}$ (they are tangent at the window centre). Precisely (PROVED: elementary, reviewed here and
independently confirmed): on $a\le n\le b$ with $n_0=\frac{a+b}2$, $h=\frac{b-a}{a+b}<1$, the power model
$\alpha+\beta\log_{10}n$ and the inverse-order model with the same value and slope at $n_0$ differ by at most
$|\beta|h^2/(2\ln10\,(1-h)^2)$, since their difference is $\frac\beta{\ln10}[\ln(1+x)-\frac x{1+x}]$ with $x=\frac{n-n_0}{n_0}$; on 348 to
370 with $|\beta|\le0.557$ this is below $1.25\cdot10^{-4}$, so the best inverse-order fit has a root-mean-square residual at
most that much above the power-model residual, against fit residuals of about $0.0023$. Finite orders cannot distinguish
them. The third law is the exact model of Proposition 14.24(c): if it held with these values (with $e_n\approx10^{-3}$, so $d<10^{-6}$),
the norms would decrease until about order $3.4\cdot10^3$ (the vertex $1.8188/0.000529-\frac32$) and then grow like $10^{\beta'n^2/6}$, so the
series would diverge (Proposition 14.24(b)), with no sign of it in the norms below that order. Neither hypothesis of Proposition 14.23
nor that of Proposition 14.24 is established for the actual sequence; convergence of the canonical
series at $\delta=2/3$ remains OPEN.

## 15. Numerical experiments (summary)

All statements in this section are finite-order computations (NUMERICAL EVIDENCE) unless they are exact finite
identities, which are labelled. None of them is by itself a proof of convergence of the infinite series.

Implementation and validation.
- The recursion (B), (R) was implemented three times:
  - exact rational arithmetic;
  - ball arithmetic at 256 to 1024 bits, with rigorous error radii and a relative-radius threshold of $10^{-6}$ (written as a stopping rule; it is a
    diagnostic only, and the continued runs of Section 14.16 keep exact ball enclosures beyond it);
  - for the logarithmic series: double precision, extended precision (64-bit mantissa), and independently 512-bit ball
    arithmetic.
- In every implementation the angular band grows with the order (density band $2n-1$ at order $n$ for
  $f_1=\sin\theta$). This matters: a fixed angular truncation converges at every $\delta$ (Proposition 14.8) and cannot
  show small-divisor divergence.
- Checks:
  - direct symbolic substitution of the reconstructed potential into the stationary equation: all orders up to $N$
    cancel, and the first surviving term equals $N(c-1)f_{N+1}$;
  - exact agreement of independent implementations;
  - exact reproduction of all eight stored pure branches of Candidate 007 from its exact leading data;
  - agreement of 256-bit and 512-bit runs through order 110.

Growth for $f_1=\sin\theta$ (unit amplitude) at non-resonant $\delta$.
- The $\ell^2$ ratio follows $\|f_{n+1}\|/\|f_n\|=L(1-a/n)$, with $a=2.03$ to rms $2\cdot10^{-7}$ over orders 190 to 388. The $\ell^1$ ratio gives the same $L$ with $a$ about $1.82$ to $1.85$.
- Values of $L$:
  - $0.4682$ at $\delta=1/\sqrt5$ (1024 bits; fit through order 625, giving $a=2.028$; the same run, continued to order 700, is used for the correlation test below);
  - $0.4676$ at Candidate 007's stored $\delta$ (to order 362);
  - $0.4704$ at $\delta=0.44598$;
  - $0.5595$ at $\delta=0.401$.
- So the apparent radius in $z$ is about $1/L\approx2.1$. The rigorous constant $A<84218$ is about $1.8\cdot10^5$ times
  larger than the observed growth constant.
- The proved top-mode bound of Section 8.2 gives $\limsup_n\|f_n\|_0^{1/n}\ge1/R_{\rm top}=0.3896$ at $\delta=1/\sqrt5$, so the
  true growth constant lies in $[0.3896,\,84218]$; the finite-order estimate $0.468$ lies in this interval.
- Short-lag correlations of consecutive normalized coefficient vectors are nearly constant (about $0.24$ at lag 1,
  $-0.88$ at lag 2). A fixed rotation in a two-plane is nevertheless excluded by longer lags: with interval arithmetic,
  the order-700 vector has distance $>0.99999999$ from the span of orders 572 and 573 (at $\delta=1/\sqrt5$), and short-lag
  correlations alone cannot locate singularities (an explicit counterexample sequence exists). The location of the
  dominant $z$-singularities, and whether one lies on the positive real axis, is OPEN.

Direct evaluation at Candidate 007's $\delta$, $f_1=\sin\theta$.
- The weighted stationary residual of the truncation, $\sup_\theta R^{-\gamma}|(cX+u_N)\cdot\nabla\rho_N-\rho_N|$ at
  $R=1$, is $2.4\cdot10^{-5}$, $6.8\cdot10^{-9}$, $1.0\cdot10^{-15}$ and $3.6\cdot10^{-29}$ for $N=10,20,40,80$. It decreases
  like $L^N$, and the partial sums are stable to 8 digits from $N=20$.
- The values for $N=10$ and $20$ are certified independently by interval arithmetic:
  $(2.3629,2.4340)\cdot10^{-5}$ and $(6.7799,7.1880)\cdot10^{-9}$.

Candidate 007's profile at its own $c$ (raw amplitude, $\|f_1\|_{\ell^1}=21.586$).
- The ratio oscillates between about 2 and 5, and the $\ell^1$ root test is $3.46$ at order 233, $3.498$ at 400, $3.508$ at 450
  and $3.5113$ at 500, still rising slowly (2048-bit ball arithmetic to order 500, relative ball radii below $10^{-300}$; all
  coefficient balls, the Poisson coefficients and the printed root values were rechecked independently at 2304 bits;
  the complete nonlinear density equation at order 500, all 499 ordered products recomputed from the checkpoint, has every one of its
  20000 residual coefficient intervals containing zero, with absolute residual at most $1.2\cdot10^{-26}$ against a forcing of about
  $2.2\cdot10^{275}$).
- If the root test were representative of the limit, the apparent radius would be $r\approx16.5$. This is an
  extrapolation from finite orders, not a convergence statement; at this rational parameter only the orders below the
  first resonance are covered by a theorem (Theorem E).
- A near-resonance at order 9 ($9\delta\approx4.03$) produces a jump at order 10.
- At the Brjuno parameter $\delta=1/\sqrt5$, where convergence is proved, the same profile gives
  $(n\|f_n\|)^{1/n}=3.6$ at order 300 (1024 bits), against the rigorous constant $A<12725638$.

Shape dependence (at Candidate 007's $\delta$, order 200; $L$ denotes the finite-order growth estimate). $L$ is
homogeneous of degree one in $f_1$ but depends strongly on its shape:
- $\sin\theta$: $0.468$;
- $\sin\theta\pm\sin3\theta$: $4.2$ and $5.2$;
- $\sin3\theta$: $4.7$;
- the 007 profile normalized to unit $\ell^1$ norm: about $0.16$ (about $0.19$ per unit $\sin\theta$ coefficient).
- In the family $\sin\theta+a\sin3\theta+b\sin5\theta$ the smallest value on the tested grid is $L=0.171$ at
  $(a,b)=(0.11,0.03)$, close to Candidate 007's own harmonic ratios $a_3/a_1=0.1135$, $a_5/a_1=0.0336$. Whether the
  leading profiles of actual solutions minimize $L$ is CONJECTURAL. The only proved variational statement concerns the
  leading velocity, not $L$ (Proposition 8.4).
- Rescaling only the $\sin3\theta$ coefficient of Candidate 007's profile at its own $c$ (order 200) raises $L$ from
  about $3.5$ to $8.4$ (factor $0.5$) and to about $5$ to $6$ (factors $0.75$ and $1.25$), consistent with the
  stream-cancellation picture of Section 8.3.

Near-resonance. At $\delta=2/5+\varepsilon$ ($\varepsilon=10^{-3},10^{-6},10^{-9}$), $\|g_{10}\|$ and $\|f_{11}\|$ scale like
$1/\varepsilon$, and the prefactor of $L^n$ grows as $\varepsilon\to0$ (finite-order observation). The exact structure is
Proposition 3.4 of the theory (PROVED through order 20): the near-resonant orders are $10,15,20,\dots$ (not only the multiples of 10), each
near-resonant inverse contributes one factor $\varepsilon^{-1}$, and the resonant stream coefficients at orders 10, 15, 20 have
poles of orders 1, 2, 3, so the amplification accumulates from one resonance to the next; Proposition 3.5 (PROVED) extends
this to every order: the pole order at order $5k$ is exactly $k-1$ for every $k\ge2$.

Exact resonances (exact rational arithmetic; finite exact computations, not labelled PROVED except where Theorem P or
an irreducibility argument of the theory covers the case). The first compatibility coefficient is nonzero for the
following cases:
- $f_1=\sin\theta$ at $c=2,9/5,5/3,20/11$;
- Candidate 007's profile at $c=9/5,5/3$;
- $f_1=\sin\theta$ at all 55 rationals $\delta\in(0.40,0.50)$ with first stream resonance $n_0\le60$.
- $f_1=\sin\theta$ at all 37 odd-numerator values $\delta=a/p$, $p\le23$ prime, $3\le a<p$ odd (first resonance at
  order $2p$, coefficient of $\sin((2a-3)\theta)$; $p$-adic valuation $-2$, $-1$ or $0$; computed by three independent exact
  programs, with identical $p$-adic digits at valuations $-4$ to $1$).

No compatible rational has been found for $f_1=\sin\theta$ (Theorem P proves this at $\delta=a/p$ with $p\ge5$ prime and $a$ even, $4\le a<p$; odd numerators and composite
denominators are outside it). The congruence of Theorem P holds in all 122 exact cases $a/p$ with $p$ prime, $7\le p\le61$ (15 primes), $a$ even, $4\le a<p$ and
$\delta\in(0.25,0.75)$. An independent direct implementation of (R), (B) in exact rational arithmetic confirms the congruence of
Theorem P and the complete residue pattern of $f_p$ modulo $p$ for all 37 pairs $(p,a)$ with $p$ prime, $5\le p\le23$,
$a$ even, $4\le a<p$. For other profiles compatibility can hold: $\sin11\theta$ and $\sin13\theta$ are compatible at
the first resonance of $\delta=4/9$ (order 9) and, with the free constant of order 9 set to zero, incompatible at the
second (order 18).

Logarithmic series (Section 14.6). Canonical normalization, $f_1=\sin\theta$. The plain density sums decay
geometrically through order 290 at $\delta=2/3$ (ratio $0.198$ per order), 320 at $4/9$ ($0.471$) and 300 at $1/2$
($0.379$ through 160, $0.381$ on orders 271 to 300; 512-bit ball arithmetic, no interior maximum of the factorially weighted
columns through 300), and the $t$-degree equals its proved bound at every order. At $4/9$ the factorial norm grows at the same rate.
At $2/3$ the constant log columns arise from cancellation of up to 14 decades at order 280, which limits double
precision to about order 270 and extended precision to about 290; an interior maximum of $k!\,\|f_{n,k}\|$ appears
from order 235 and is reproduced in both precisions and in 512-bit ball arithmetic (independently audited through
order 290; it exceeds the constant column from order 244, by $0.54$ decades at order 250, $1.36$ at 260, $2.15$ at
270, $3.04$ at 280, where it sits at log degree 50 for both density and stream, the stream maximum being $2.29$
decades above its constant column, and $3.94$ at 290), and the plain stream sums decay more slowly than the density sums from about order 263 (9-order increments of
$\log_{10}$ between $-0.700$ and $-0.666$ for $263\le n\le290$, against $-0.717$ to $-0.688$ before; the ball values
through 270 agree to four decimals, and the certified stream to density ratio rises from order 260 to 290). Through
order 315 the plain ratio $N_n/M_n$ is certified below $0.2115$ (maximum at $n=3$); on 291 to 300 it lies between
$10^{-2.01}$ and $10^{-1.52}$, on 311 to 315 between $0.0199$ and $0.0821$, so the rise of the ratio before 290 did not continue, while least-squares slopes of
$\log_{10}N_n$ over 27-order windows from 260 on stay between $-0.684$ and $-0.676$ per order against $-0.701$ for the
density (descriptive finite-window statistics, Section 14.17). In plain norm the density at order $n$ is carried mostly
by the order-one stream acting on $F_{n-1}$ ($0.77$ to $0.80$ of $M_n$ on 60 to 290; midpoints), and the term of $G_{n-1}$
against $f_1$ is $0.25$ to $0.31$ times $N_{n-1}$ after the density inverse. The 512-bit ball computation agrees with the tabulated column values of Section 14.6 through order 290 at
$2/3$ and 260 at $4/9$ (the audit coverage is listed there). An independent exact computation at $\delta=4/9$ to order 73 agrees.
Per-deficit growth at $2/3$: for small fixed deficits $d$ the factorially weighted column grows at a rate near the
proved $(d+1)\lambda$ of Proposition 14.9, and the largest weighted columns sit at deficits roughly proportional to
the order. At fixed $t=\log r$ (extended precision for $|t|\le20$ through order 260 and $|t|=40$ through 220; ball arithmetic
at $t=0,\pm20,\pm40$ at selected orders through 290) the norms $\|F_n(t,\cdot)\|$ decay geometrically, with 18-order
mean $\log_{10}$ increments between $-0.71$ and $-0.65$ per order (shorter ball-arithmetic windows at $|t|=40$ give
$-0.704$ to $-0.637$), after cancellation between log columns of up to 11.5 decades (the ball increments from 260 to
280 are $-0.687,-0.683,-0.673,-0.675$ per order at $t=20,-20,40,-40$, and from 280 to 290
$-0.698,-0.675,-0.672,-0.673$). At the angular mode nearest the diagonal
the Poisson step reproduces the computed stream to $10^{-3}$ in $\log_{10}$; a coefficientwise absolute bound overestimates
it by up to 7.7 decades at order 260, almost all of it the geometric factor $|s|^{-h}$ with $|s|=2/3$, while the
factorial norm of the input exceeds it by at most 1.2 decades at the sampled orders; the output is below the plain
norm of its input at 200 and 260 but above it, by 0.37 decades, at 263. The maximizing interior column has more than
$99.6\%$ of its Fourier mass far from the diagonal, almost all on the low-frequency side (interval partition at orders
240 to 280; at 280 the density fraction off the band is $0.99995$). The near-diagonal mass sits in the low stream
columns ($16$ to $54\%$ of their mass within $|s|\le q/4$ for $10\le q\le30$, orders 240 to 280) and, in the constant stream column, grows with the order
($0.12$ at 240, $0.47$ at 280, $0.81$ at 290). These are finite-order
observations; they do not decide convergence.

Truncated recursions (floating-point midpoints without error enclosure; NUMERICAL EVIDENCE only). To see which products
set the rate at $\delta=2/3$, $f_1=\sin\theta$, the quadratic sum of the density recursion was restricted to the pairs
$(i,j)$ with $\min(i,j)\le K$, keeping the canonical Poisson inverse. With $K=1$ (each order generated from the previous
one through the first-order stream and density only) the root $M_{300}^{1/300}$ is $0.1627$, with $K=3$ it is $0.1870$,
and the full recursion gives $0.1943$; the 27-order slopes of $\log_{10}M_n$ ending at 300 are $-0.780$, $-0.719$ and
$-0.701$. In both truncated runs the stream and density slopes agree to within $0.002$ per order and $N_n/M_n$ decreases
slowly ($10^{-2.84}$ and $10^{-2.79}$ at 300), whereas in the full recursion the stream decays $0.013$ to $0.02$ decades per
order more slowly than the density and $N_n/M_n$ varies with the residue of $n$ modulo 3. Among the retained floating
columns the factorially weighted log columns of the truncated runs have no interior maximum ($K=3$ at 300: the largest
is at log degree 1, $10^{-7.6}$ relative to the constant column; full recursion: $10^{4.9}$ at degree 59), but double
precision loses the highest log columns beyond order about 200 (they fall below the subnormal range), and a coefficient
below that range can still dominate after multiplication by $q!$, so the floating runs alone do not control the dropped
columns. The completed 1024-bit ball reruns of both truncated recursions keep all columns through order 300 (the finite
column maxima and the modified recurrence were checked independently): at order 300 every nonconstant factorially
weighted log column is smaller than the constant column, and log degree 1 gives the largest nonconstant column for both
density and stream in both runs. Interpretation (tentative): most of the geometric rate is
produced by products involving the lowest few orders, while the slower stream rate and the interior factorial maximum
need products of two high orders. For these truncated recursions convergence is PROVED (Section 14.21): with
$K\le5$ at $\delta=2/3$ the retained low factors carry no logarithm, the factorially weighted norms with weight $q!\,3^q$
are geometrically bounded ($\le(23/10)^{n-1}$ for $K=1$ and $\le(5/2)^{n-1}$ for $K=3$), and $r\ge4$ suffices; the finite
rates above are much smaller than these bounds.

Tuned pure series at $\delta=2/3$ (Section 12.4). For $f_1=\sin\theta+b\sin3\theta$ with $b$ a real root of the sextic
$\mathcal P_6$, the pure series with the multipoles $H_{3k}$ chosen to cancel the next obstruction was computed in double
precision to order 240 (Fourier transforms on 4096 points, exact frequency support imposed at each order) and, for
$b_1=0.28066\ldots$, in 40-digit arithmetic to order 30. The 40-digit $H_6$ agrees to 25 digits with the exact value
from $\mathbb Q(b_1)$, and the finite-difference responses agree with the exact $\sigma_k$. The root test
$\|f_n\|_{\ell^1}^{1/n}$ rises slowly, to $0.251$ at order 240 for $b_1$ and $0.711$ for $b_2$; fits with a power correction
give growth constants $0.26$ and $0.73$. The residual obstructions stay below $10^{-16}\|f_n\|_{\ell^1}$. These are
finite-order data; convergence is the content of Theorem T, not of these runs.

Tuned pure series at other rational $\delta$ (Sections 12.5, 12.6). The same construction in 1024-bit ball arithmetic, with
every tuned obstruction certified to be a ball containing zero, was run to order 300 (306 at $\delta=4/9$) for the
two-mode profiles $\sin\theta+b\sin3\theta$ of Corollaries T_4, T_5, T_6, T_{9,2} and T_{10,3}; at $c=3$ the run for $b_1$ reached
order 398 (root test $0.2533$ at 390, fit $A=0.259$). The computed values of $|\sigma_k|$ agree with the theory: they reproduce
the exact minima where the theory proves them and stay above the certified lower bounds where only bounds are proved
(at $\delta=3/5$). The table compares the finite-order growth constant $A$ (a three-parameter fit
$\log_{10}\|f_n\|_{\ell^1}=n\log_{10}A+\beta\log_{10}n+C$ on $n\ge150$, or the root test at order 300 where the fit is unstable)
and the apparent exterior radius $A^{1/\delta}$ with the certified sufficient radius $2^e$ of the theory (all at unit
amplitude). The first two columns of numbers are NUMERICAL EVIDENCE; the last is PROVED.

| $\delta$ | root $b$ | $A$ | apparent radius $A^{1/\delta}$ | certified radius |
|---|---|---|---|---|
| $2/3$ | $0.2807$, $0.6464$ | $0.259$, $0.73$ | $0.13$, $0.63$ | $2^{35/2}$, $2^{16}$ |
| $1/2$ | $-0.2796$, $0.0399$, $0.0771$ | $1.33$, $0.288$, $0.2225$ (root tests) | $1.8$, $0.083$, $0.050$ | $2^{41/2}$, $2^{23}$, $2^{24}$ |
| $1/2$ | $0.1878$, $0.3515$, $0.6268$ | $0.371$ (root test), $0.89$ to $0.92$, $2.15$ | $0.14$, $0.8$, $4.6$ | $2^{24}$, $2^{23}$, $2^{47/2}$ |
| $2/5$ | $-0.4898$, $0.0490$ | $3.91$, $0.393$ | $30$, $0.10$ | $2^{59/2}$, $2^{71/2}$ |
| $2/5$ | $0.1253$, $0.2121$, $0.3153$, $0.5600$ | $0.440$, $0.901$, $1.73$, $3.59$ | $0.13$, $0.77$, $3.9$, $24$ | $2^{65/2}$, $2^{65/2}$, $2^{65/2}$, $2^{63/2}$ |
| $1/3$ | $-0.6087$, $0.0886$, $0.1407$ | $7.61$, $0.478$, $0.82$ to $0.85$ | $440$, $0.11$, $0.55$ to $0.61$ | $2^{38}$, $2^{42}$, $2^{42}$ |
| $1/3$ | $0.1965$, $0.2785$, $0.5122$ | $1.39$ to $1.53$, $2.2$ to $2.4$, $5.0$ to $5.2$ | $2.7$ to $3.6$, $11$ to $14$, $130$ to $144$ | $2^{83/2}$, $2^{40}$, $2^{79/2}$ |
| $4/9$ | $0.0634$, $0.1524$, $0.2698$ | $0.304$, $0.408$, $1.03$ | $0.069$, $0.13$, $1.07$ | $2^{129/4}$, $2^{125/4}$, $2^{32}$ |
| $4/9$ | $0.4224$, $1.8567$ | $1.71$, $10.7$ | $3.4$, $206$ | $2^{121/4}$, $2^{117/4}$ |
| $3/5$ | $0.0659$, $0.1093$ | $0.195$ to $0.20$, $0.18$ | $0.065$ to $0.07$, $0.06$ | $2^{133/6}$, $2^{137/6}$ |
| $3/5$ | $0.3506$, $0.5942$ | $0.43$ to $0.47$, $1.07$ to $1.22$ | $0.25$ to $0.28$, $1.1$ to $1.4$ | $2^{65/3}$, $2^{125/6}$ |

At the largest root for $\delta=1/2$ the stationary residual of the truncation decays geometrically in the truncation
order for $r\ge8$ and grows for $r\le4$, matching the apparent radius $4.6$; at $c=3$ ($b_1$) it decays at every tested
radius down to $r=0.2$, consistent with $0.13$. The apparent radii at the same $\delta$ differ by factors up to about $4\cdot10^3$, while
the certified radii differ by factors of at most $2^6$; the proved lower bounds for the required radius from the top mode are
below $0.16$ ($1.144$ at $b=1.8567$). Where the certified radii do differ, they follow the response lower bound of the
certificate rather than the growth constant: at $\delta=2/5$ the root $-0.4898$ (largest apparent radius, response infimum $0.40$)
has the smallest certified exponent and the root $0.0490$ (smallest apparent radius, response infimum $2.2\cdot10^{-6}$) the
largest. At $\delta=1/3$, root $-0.6087$, the certified finite residual enclosures grow from $N=40$ to $N=80$ at $r=512$ and
decrease over $N=10,20,40,80$ at $r=1024$ and $r=2048$, so the apparent radius lies between 512 and 1024 at these orders; finite
truncation data do not locate the true threshold.

Periods seven to ten, and the single harmonics. The tuned series of Corollaries T_7 ($\delta=2/7$), T_8 ($\delta=1/4$), T_9 ($\delta=2/9$)
and T_10 ($\delta=1/5$) were computed in double precision to orders 301, 304, 306 and 300 by a separate program (dense sine arrays; every resonant
harmonic fixed by two provisional continuations through the next obstruction; every tuned obstruction set to zero after
its residual is recorded; at the first roots the run uses the amplitude $1/16$ to avoid overflow and rescales). An
extended-precision rerun (64-bit mantissa) at the third roots, started from the same double-precision value of the root
(so it tests the propagation of rounding errors, not the accuracy of the root), agrees with double precision to $10^{-10}$ at $\delta=2/7$ and
$2\cdot10^{-7}$ at $\delta=1/4$ in $\log_{10}\|f_n\|_{\ell^1}$. An independent directed-rounding computation of the exact
branches through order 56 at $\delta=2/7$ and 64 at $\delta=1/4$ (96 at the third root) agrees with the unit-amplitude runs
to $7.7\cdot10^{-8}$ in $\log_{10}$ of every norm, $2.5\cdot10^{-7}$ in $\log_{10}|H_{kQ}|$ and a relative $3.9\cdot10^{-12}$ in every
response (all 915 printed responses, at every order, agree with an independent evaluation at the exact root to a
relative $6.1\cdot10^{-12}$); the later orders are not checked in this way. At the first roots the amplitude-$1/16$ runs used for the
table print the same norms, to all ten printed decimals, as the unit-amplitude runs up to their overflow at orders 286 and 247. The norms oscillate within each period, so $A$ is the slope of a
linear fit to the per-period maxima of $\log_{10}\|f_n\|_{\ell^1}$ on $n\ge100$, $150$ and $200$; the table gives the range over
these three windows. The same program and fit at $\delta=1/3$ reproduce the ball-arithmetic values of the table above
($426$ to $435$, $0.109$ to $0.110$, $0.61$, $2.7$ to $2.8$, $11.2$ to $11.6$ and $125$ to $130$ at the six roots). At $\delta=2/9$ the 170 double-precision responses $\sigma_2,\dots,\sigma_{18}$ at the ten roots agree with the exact values of Corollary T_9 to the five printed digits (relative $4.5\cdot10^{-5}$ at most). At $\delta=2/7$ the runs at all ten roots were repeated to order 601 (fits on complete periods through order 595): the fitted $A$ on $n\ge100$, $200$, $300$ and $400$ are $11.55$ to $11.57$, $1.763$ to $1.768$, $0.769$ to $0.772$, $0.5976$ to $0.5990$, $0.530$ to $0.533$, $0.834$ to $0.835$, $1.233$ to $1.237$, $1.846$ to $1.859$, $3.677$ to $3.689$ and $6.977$ to $6.998$, all within 1% of the order-301 ranges in the table. The overlapping printed norms agree exactly with the order-301 runs, and at all ten roots these finite statistics were rechecked independently in exact rational arithmetic (comparing the same windows $n\ge100,150,200$ at both orders, the largest relative change of $A$ is $3.2\%$, at the ninth root, and at most $1.5\%$ at the first eight). Doubling the order does not materially change these apparent radii (NUMERICAL EVIDENCE; it gives no bound on the true radius). At $\delta=1/4$ the runs at all ten roots were repeated to order 600 (fits on complete periods through order 592): the fitted $A$ on $n\ge100$, $200$, $300$ and $400$ are $17.01$ to $17.06$, $2.686$ to $2.713$, $0.8335$ to $0.8343$, $0.5855$ to $0.5869$, $0.8416$ to $0.8435$, $1.173$ to $1.178$, $1.700$ to $1.705$, $2.672$ to $2.675$, $3.920$ to $3.937$ and $8.971$ to $9.013$, within 1% of the order-304 ranges in the table except at the second root (up to 2% below). On the same windows $n\ge100,150,200$ at both orders the largest relative change of $A$ is about $3.71\%$ (ninth root, $n\ge200$), so the apparent radii $A^4$ change by less than 16%; at all ten roots the overlapping printed norms are identical to those of the order-304 runs, and these finite statistics were rechecked independently in exact rational arithmetic (NUMERICAL EVIDENCE). The
necessary radii are the lower bounds of Corollaries T_7(d), T_8(d), T_9(d) and T_10(d) (PROVED, independently confirmed at all four $\delta$). All at unit amplitude; the apparent radius
columns are NUMERICAL EVIDENCE, the certified radii PROVED. At $\delta=1/5$ the certified radii come from certified prefixes of 40 to 120 orders (Corollary T_10(b); at the fifth root the tail-only response bound with a prefix of 120 orders).

| $\delta$ | root $b$ | $A$ | apparent radius $A^{1/\delta}$ | necessary radius | certified radius |
|---|---|---|---|---|---|
| $2/7$ | $-0.6736$ | $11.4$ to $11.6$ | $5.1\cdot10^3$ to $5.3\cdot10^3$ | $0.344$ | $2^{47}$ |
| $2/7$ | $-0.0567$ | $1.77$ to $1.78$ | $7.4$ to $7.6$ | $5.95\cdot10^{-5}$ | $2^{50}$ |
| $2/7$ | $0.0151$ | $0.77$ to $0.78$ | $0.40$ to $0.42$ | $5.74\cdot10^{-7}$ | $2^{109/2}$ |
| $2/7$ | $0.0306$ | $0.595$ to $0.597$ | $0.163$ to $0.164$ | $6.83\cdot10^{-6}$ | $2^{54}$ |
| $2/7$ | $0.0659$ | $0.53$ | $0.108$ to $0.110$ | $1.00\cdot10^{-4}$ | $2^{53}$ |
| $2/7$ | $0.1007$ | $0.83$ to $0.84$ | $0.53$ to $0.54$ | $4.44\cdot10^{-4}$ | $2^{53}$ |
| $2/7$ | $0.1357$ | $1.23$ to $1.25$ | $2.05$ to $2.19$ | $1.26\cdot10^{-3}$ | $2^{105/2}$ |
| $2/7$ | $0.1798$ | $1.85$ to $1.88$ | $8.6$ to $9.2$ | $3.37\cdot10^{-3}$ | $2^{103/2}$ |
| $2/7$ | $0.2518$ | $3.6$ to $3.7$ | $86$ to $98$ | $1.09\cdot10^{-2}$ | $2^{54}$ |
| $2/7$ | $0.4752$ | $7.0$ to $7.1$ | $887$ to $971$ | $0.101$ | $2^{49}$ |
| $1/4$ | $-0.7086$ | $16.7$ to $17.1$ | $7.8\cdot10^4$ to $8.5\cdot10^4$ | $0.721$ | $2^{113/2}$ |
| $1/4$ | $-0.0789$ | $2.74$ to $2.77$ | $56$ to $59$ | $1.11\cdot10^{-4}$ | $2^{119/2}$ |
| $1/4$ | $0.0207$ | $0.83$ | $0.47$ to $0.48$ | $5.25\cdot10^{-7}$ | $2^{65}$ |
| $1/4$ | $0.0512$ | $0.584$ to $0.588$ | $0.116$ to $0.120$ | $1.96\cdot10^{-5}$ | $2^{63}$ |
| $1/4$ | $0.0761$ | $0.84$ to $0.85$ | $0.50$ to $0.51$ | $9.60\cdot10^{-5}$ | $2^{63}$ |
| $1/4$ | $0.1003$ | $1.17$ to $1.20$ | $1.9$ to $2.1$ | $2.89\cdot10^{-4}$ | $2^{125/2}$ |
| $1/4$ | $0.1284$ | $1.67$ to $1.72$ | $7.8$ to $8.7$ | $7.77\cdot10^{-4}$ | $2^{62}$ |
| $1/4$ | $0.1661$ | $2.65$ to $2.70$ | $49$ to $53$ | $2.17\cdot10^{-3}$ | $2^{62}$ |
| $1/4$ | $0.2316$ | $3.8$ to $4.0$ | $2.1\cdot10^2$ to $2.5\cdot10^2$ | $8.23\cdot10^{-3}$ | $2^{60}$ |
| $1/4$ | $0.4456$ | $8.8$ to $9.0$ | $6.0\cdot10^3$ to $6.4\cdot10^3$ | $0.112$ | $2^{115/2}$ |
| $2/9$ | $-0.7279$ | $21.6$ to $22.7$ | $1.0\cdot10^6$ to $1.3\cdot10^6$ | $1.51$ | $2^{127/2}$ |
| $2/9$ | $-0.0930$ | $3.89$ to $3.96$ | $4.5\cdot10^2$ to $4.9\cdot10^2$ | $1.44\cdot10^{-4}$ | $2^{135/2}$ |
| $2/9$ | $0.0411$ | $0.637$ to $0.640$ | $0.131$ to $0.134$ | $3.63\cdot10^{-6}$ | $2^{72}$ |
| $2/9$ | $0.0598$ | $0.860$ to $0.870$ | $0.51$ to $0.54$ | $1.97\cdot10^{-5}$ | $2^{72}$ |
| $2/9$ | $0.0777$ | $1.16$ to $1.17$ | $1.96$ to $2.06$ | $6.40\cdot10^{-5}$ | $2^{143/2}$ |
| $2/9$ | $0.0975$ | $1.58$ to $1.64$ | $7.7$ to $9.2$ | $1.78\cdot10^{-4}$ | $2^{71}$ |
| $2/9$ | $0.1215$ | $2.22$ to $2.34$ | $36$ to $46$ | $4.79\cdot10^{-4}$ | $2^{71}$ |
| $2/9$ | $0.1551$ | $3.06$ to $3.30$ | $1.5\cdot10^2$ to $2.2\cdot10^2$ | $1.43\cdot10^{-3}$ | $2^{139/2}$ |
| $2/9$ | $0.2159$ | $5.02$ to $5.43$ | $1.4\cdot10^3$ to $2.0\cdot10^3$ | $6.36\cdot10^{-3}$ | $2^{70}$ |
| $2/9$ | $0.4215$ | $10.9$ to $11.5$ | $4.7\cdot10^4$ to $6.0\cdot10^4$ | $0.129$ | $2^{65}$ |
| $1/5$ | $-0.7392$ | $29.5$ to $32.2$ | $2.2\cdot10^{7}$ to $3.5\cdot10^{7}$ | $3.23$ | $2^{147/2}$ |
| $1/5$ | $-0.1026$ | $5.28$ to $5.55$ | $4.1\cdot10^{3}$ to $5.3\cdot10^{3}$ | $1.66\cdot10^{-4}$ | $2^{76}$ |
| $1/5$ | $-0.0180$ | $2.14$ to $2.19$ | $45$ to $50$ | $2.74\cdot10^{-8}$ | $2^{80}$ |
| $1/5$ | $0.0030$ | $1.34$ | $4.2$ to $4.3$ | $3.33\cdot10^{-12}$ | $2^{165/2}$ |
| $1/5$ | $0.0187$ | $1.03$ to $1.12$ | $1.2$ to $1.7$ | $3.37\cdot10^{-8}$ | $2^{87}$ |
| $1/5$ | $0.0338$ | $0.690$ to $0.696$ | $0.157$ to $0.163$ | $6.47\cdot10^{-7}$ | $2^{167/2}$ |
| $1/5$ | $0.0485$ | $0.902$ to $0.920$ | $0.599$ to $0.659$ | $3.91\cdot10^{-6}$ | $2^{83}$ |
| $1/5$ | $0.0623$ | $1.17$ to $1.18$ | $2.2$ to $2.3$ | $1.37\cdot10^{-5}$ | $2^{165/2}$ |
| $1/5$ | $0.0772$ | $1.54$ to $1.59$ | $8.6$ to $10$ | $4.00\cdot10^{-5}$ | $2^{82}$ |
| $1/5$ | $0.0942$ | $2.08$ to $2.17$ | $39$ to $48$ | $1.08\cdot10^{-4}$ | $2^{163/2}$ |
| $1/5$ | $0.1153$ | $2.79$ to $3.00$ | $1.7\cdot10^{2}$ to $2.4\cdot10^{2}$ | $2.99\cdot10^{-4}$ | $2^{81}$ |
| $1/5$ | $0.1459$ | $3.98$ to $4.25$ | $1.0\cdot10^{3}$ to $1.4\cdot10^{3}$ | $9.69\cdot10^{-4}$ | $2^{159/2}$ |
| $1/5$ | $0.2033$ | $6.00$ to $6.51$ | $7.8\cdot10^{3}$ to $1.2\cdot10^{4}$ | $5.09\cdot10^{-3}$ | $2^{77}$ |
| $1/5$ | $0.4016$ | $13.6$ to $14.6$ | $4.7\cdot10^{5}$ to $6.7\cdot10^{5}$ | $0.152$ | $2^{149/2}$ |

As at the smaller periods, the apparent radii at one $\delta$ vary much more than the certified ones (by a factor of about
$5\cdot10^4$ at $\delta=2/7$, $7\cdot10^5$ at $\delta=1/4$, $10^7$ at $\delta=2/9$ and $2\cdot10^8$ at $\delta=1/5$, against $2^{15/2}$, $2^{17/2}$, $2^{17/2}$ and $2^{27/2}$), and the root of largest modulus has
the largest apparent radius. At $\delta=2/9$ the fitted slopes still decrease as the window moves from $n\ge100$ to $n\ge200$ at the first root and the sixth to tenth roots, so the upper ends of those ranges are probably too large. The third roots, whose responses nearly vanish once ($\sigma_{10}\approx1.37\cdot10^{-8}$ at
$\delta=1/4$), have the largest certified radii but apparent radii near the smallest ($0.41$ and $0.48$); their certified radii come
from certified prefixes through orders 140 and 96 followed by tail-only response lower bounds, which the majorant uses in
every later period. This is an observed association at finite order: the
numerator in $H=-R/\sigma$ also varies, and the response values alone give no coefficient-growth law; it does not show
that the true radius ignores small responses. At $\delta=2/9$ no response nearly vanishes (the smallest global response infimum, PROVED exactly, is $3.356\cdot10^{-4}$, attained at $k=4$ at the third root); the third root again has the largest certified radius ($2^{72}$, shared with the fourth) and here the smallest apparent radius ($0.13$). At $\delta=2/9$ the runs at all ten roots were repeated to order 612 (fits on complete periods through order 603; amplitudes $1/16$ and $1/4$ at the first two roots, $1$ at the third to sixth, $1/2$ at the seventh and eighth, $1/4$ and $1/8$ at the ninth and tenth, then rescaled exactly): the fitted $A$ on $n\ge100$, $200$, $300$ and $400$ are $21.79$ to $21.96$, $3.785$ to $3.836$, $0.6400$ to $0.6416$, $0.8734$ to $0.8757$, $1.140$ to $1.148$, $1.575$ to $1.587$, $2.268$ to $2.288$, $3.234$ to $3.256$, $5.291$ to $5.323$ and $11.47$ to $11.55$ at the ten roots, a spread of less than $1.4\%$ over the four windows at every root, so apparent radii $A^{9/2}$ from about $0.134$ (third root) to $1.09\cdot10^6$ (first root). These ranges lie inside the order-306 ranges of the table or depart from them by less than $2.7\%$ (most at the second root, below); the upper ends at order 306 were too large at the first and sixth to ninth roots, as remarked above, but not at the tenth. The overlapping printed norms are identical to those of the order-306 runs at all ten roots. On the same windows $n\ge100,150,200$ at both orders the fitted $A$ changes by less than $6\%$ (the largest change, $+5.9\%$, at the eighth root on $n\ge200$), so the apparent radii change by less than $30\%$ (NUMERICAL EVIDENCE; finite statistics, no bound on the true radius). At $\delta=1/5$ (order 300, complete periods through order 290; amplitude $1/16$ at the first root and $1/2$ at the second and ninth to fourteenth, then rescaled exactly) the fitted $A$ decreases from the window $n\ge100$ to $n\ge200$ at every root except the fourth, by up to $8.4\%$ at the first root, so the upper ends of those ranges are probably too large; at the fourth root the per-period maxima lie on a line (residual below $0.03$ decades on $n\ge100$). The fifth root, whose global response minimum $|\sigma_8|\approx2.44\cdot10^{-7}$ is the smallest at this $\delta$ (PROVED), has the largest certified radius ($2^{87}$, against $2^{177/2}$ from its global response bound), apparent radius $1.2$ to $1.7$ and the largest fit residual on $n\ge100$ ($1.3$ decades); its printed $\sigma_8=-2.437677575521\cdot10^{-7}$ agrees with the exact infimum to eleven digits. The smallest apparent radius ($0.16$) is at the sixth root and the largest ($2\cdot10^7$ to $3.5\cdot10^7$) at the first, and every apparent radius lies far above the necessary radius of its root. These finite-order statistics give no bound on the true radius. Repeating the runs at all fourteen roots to order 600 (fits on complete periods through order 590; amplitudes $1/32$, $1/4$ and $1/2$ at the first three roots, $1$ at the fourth to eighth, $1/2$ at the ninth to eleventh, $1/4$ at the twelfth and thirteenth and $1/8$ at the fourteenth, then rescaled exactly) gives fitted $A$ on $n\ge100$, $200$, $300$ and $400$ of $29.60$ to $30.17$, $5.224$ to $5.286$, $2.092$ to $2.116$, $1.341$ to $1.348$, $1.076$ to $1.087$, $0.6955$ to $0.6970$, $0.9218$ to $0.9265$, $1.150$ to $1.159$, $1.524$ to $1.541$, $2.032$ to $2.064$, $2.784$ to $2.825$, $3.886$ to $3.961$, $5.991$ to $6.087$ and $13.37$ to $13.61$ at the fourteen roots, a spread of less than $2\%$ over the four windows at every root, so apparent radii $A^5$ from about $0.163$ (sixth root) to $2.5\cdot10^7$ (first root). The overlapping printed norms are identical to those of the order-300 runs at all fourteen roots. On the same windows $n\ge100,150,200$ at both orders the fitted $A$ changes by less than $7.1\%$ (the largest change, $-7.0\%$, at the fourteenth root on $n\ge100$; on that window the order-600 value is smaller at eleven of the fourteen roots), so the apparent radii change by less than $31\%$; this confirms that the upper ends of the order-300 ranges were too large (NUMERICAL EVIDENCE; finite statistics, no bound on the true radius).

For the single harmonics the same program gives, for $\sin7\theta$ at $\delta=4/5$, a stable fit $A=0.567$ to $0.570$ through
order 300, an apparent radius $0.49$ (necessary $0.0902$, certified $2^{20}$; unit amplitude). A separate 1024-bit ball computation
to order 300 (every tuned obstruction a ball containing zero; $\sigma_1,\dots,\sigma_5$ equal to the exact values to all printed
digits) gives straight-line slopes $A=0.569$ to $0.570$ on the windows from orders 100, 150 and 200 to 300 (apparent radius $0.494$ to $0.496$) and an endpoint base $0.573$ on orders 100 to 300 (apparent radius $0.499$), and stationary residuals of the
truncations (Section 13 test) that decrease geometrically at $R=1$ and $R=2$, are marginal at $R=0.5$ and grow at $R\le0.25$. The prefix of this run was rechecked independently in interval arithmetic (all coefficients through order 20, the norms and Poisson identities through order 300, the full nonlinear sums at orders 50, 100, 200 and 300; root of the density norm $0.55264$ at order 300), and the continuum residuals of the truncations at $N=10,20,40,80$ and $1/8\le R\le4$ were enclosed with two angular derivatives; at $R=1/2$ the enclosed residual increases from $N=20$ to $40$ and from $40$ to $80$ (supremum about $0.286$ at $N=80$). These are finite checks and do not decide convergence at any radius. The ball computation was continued to order 500 and rechecked independently in interval arithmetic (all coefficients through order 20, the norms and Poisson identities through order 500, the full nonlinear sums at orders 400 and 500, exact agreement with the order-300 run at the common orders, where the free stream harmonic at order 300, not yet set in the earlier run, was checked separately; root of the density norm $0.56104$ at order 500). Its line fits on the windows from orders 100, 200, 300 and 400 to 500 give $A=0.5710$, $0.5714$, $0.5723$ and $0.5738$ (radius diagnostics $A^{5/4}=0.4964$ to $0.4994$), and the endpoint base on orders 100 to 500 is $0.5736$ ($0.4992$). The slope increases slightly as the window moves up, so these diagnostics are not bounds either; extending the run from order 300 to 500 changes the apparent radius by less than $1\%$ (NUMERICAL EVIDENCE). For $\sin9\theta$ at $4/7$,
$\sin11\theta$ at $4/9$ and $\sin17\theta$ at $6/13$ the per-period growth changes abruptly within the computed range (near
orders 77, 130 and 230), the fits on $n\ge100,150,200$ disagree and their residuals reach 1 to 4 decades, so no growth
constant is quoted. For $\sin9\theta$ and $\sin11\theta$ extended-precision reruns to order about 150 reproduce the changes,
so they are not rounding effects. For $\sin9\theta$ a 1024-bit ball computation to order 301 (every tuned obstruction a ball containing zero; rechecked independently in interval arithmetic: all coefficients through order 28, the norms and Poisson identities through order 301, the full nonlinear sums at orders 50, 100, 200 and 300; root of the density norm $1.9476$ at order 301) reproduces the change near order 77. Its least-squares line fits on the windows from orders 100, 150 and 200 to 301 give $A=2.031$, $1.982$ and $2.119$ (radius diagnostics $A^{7/4}=3.46$, $3.31$ and $3.72$), and the endpoint base on orders 100 to 301 is $2.113$ (radius diagnostic $3.70$); the diagnostics vary nonmonotonically with the window and are neither upper nor lower bounds for the radius, which the proved bounds place between $0.2365977$ and $2^{147/4}$ (unit amplitude). The enclosed continuum residuals of the truncations at $N=10,20,40,80$ decrease at each step at $R=4$, decrease from $N=20$ to $40$ and increase from $40$ to $80$ at $R=2$, and the sampled residuals grow at $R\le1$. For $\sin11\theta$ a 1024-bit ball computation to order 306 (every tuned obstruction a ball containing zero; $\sigma_1,\sigma_2,\sigma_3$ equal to the exact values; rechecked independently in interval arithmetic: all coefficients through order 36, the norms and Poisson identities through order 306, the full nonlinear sums at orders 50, 100, 200 and 300; root of the density norm $3.388$ at order 306) reproduces the change near order 130: the ten-order slopes of $\log_{10}\|f_n\|_{\ell^1}$ are $0.328$ to $0.335$ per order through order 130 and $0.43$ to $1.30$ after it. Its line fits on the windows from orders 100, 150 and 200 to 306 give $A=4.965$, $4.984$ and $4.202$ (radius diagnostics $A^{9/4}=36.8$, $37.1$ and $25.3$), the endpoint base on 100 to 306 is $4.321$ ($26.9$), and the early slope through order 130 corresponds to $A\approx2.15$ ($5.6$). Again these are not bounds for the radius, which the proved bounds place between $0.507$ and $2^{213/4}$ (unit amplitude). The enclosed continuum residuals of the truncations at $N=10,20,40,80$ increase at each step at $R=4$ and decrease at each step at $R=8$, and the sampled residuals decrease at $R\ge8$ and grow at $R\le4$. In these three cases the computed responses become small within the computed range and
keep decreasing: for $\sin9\theta$ from $k=9$ on, like $1.04\cdot10^{-3}/k$ for $20\le k\le42$, toward the limit $\lim_k\sigma_k\approx1.9908\cdot10^{-7}$ (the last computed response, $\sigma_{42}=2.43\cdot10^{-5}$, is about 122 times the limit; an exact rational number, Corollary T_{Q,h}.9(c), PROVED;
fits on $k\le42$ give values between $5\cdot10^{-9}$ and $9\cdot10^{-8}$ and do not determine it; the certified lower bound is
$2^{-25}\approx3\cdot10^{-8}$); for $\sin11\theta$ from $k=14$ on
($-1.0\cdot10^{-3}$ at $k=14$, $-1.85\cdot10^{-4}$ at $k=33$), while $|\sigma_k|\ge0.12$ for $k\le13$ except $k=11$; for $\sin17\theta$ they are below $0.02$
at $k=3,11,14,17$ and from $k=20$ on ($-2.0\cdot10^{-5}$ at $k=22$), with the certified real response zero between $k=2379$ and
$2380$ far beyond. Each tuned harmonic is $H_{kQ}=-R_k/\sigma_k$. The finite growth transitions occur in ranges where the computed responses are small; the tuning identity alone does not determine the eventual growth because its obstruction numerator $R_k$ also varies. Order
300 is pre-asymptotic for these profiles. For $\sin7\theta$ the responses decrease slowly and appear to level off
($-2.96\cdot10^{-5}$ at $k=6$, $-7.9\cdot10^{-6}$ at $k=54$).

## 16. Accompanying artifacts

The accompanying artifacts include exact commands and restart instructions. They contain:

- the detailed theory and numerical reports and the short answers;
- the constant computations for Theorems A, D and E, the low-order consistency check of the recurrence
  against direct substitution, the logarithmic-series scripts, and the exact
  algebra and certificates for Theorems T, T_Q, T_{Q,h} and Corollaries T.3 to T.10 and T_4 to T_10 (compatibility
  polynomials, irreducibility, exact response bounds, certified prefixes and radius boxes, necessary radii),
  the double-precision tuned runs with their fits, and the light reproductions rerun at the end of the run;
- the high-order recursion (exact, ball-arithmetic and floating-point versions), the extraction of
  Candidate 007's leading data, the experiment and analysis scripts, the per-order run data, the exported
  coefficient states, and the restart commands;
- the independent low-order implementation and verification programs, the standalone
  proofs written during the verification, the claim map, the table of certified radii and the executed reproduction
  commands;
- the best candidate parameters and Fourier coefficients (Candidate 007's leading data and the exact
  compatible tuned profiles).

The multi-gigabyte binary recursion checkpoints of the longest runs are not included. Fresh runs can recompute the
series, but replaying the recorded midpoint-reset and sensitivity continuations requires the omitted checkpoint.
Candidate 007's exact leading coefficients are also listed in Section 8.5, so the Candidate-shaped profiles are
fully specified in this report.

## Appendix A. Complete proof of Theorem D (Diophantine parameters, explicit certificate)

Hypotheses as in Section 7.3: $|m-n\delta|\ge\kappa n^{-\tau}$ for all $n\ge1$, $m\in\mathbb Z$ ($\kappa>0$, $\tau\ge1$);
$f_1\ne0$ a real odd sine polynomial with top frequency $L$, $B=L+1$; $\sigma\ge0$, $F=\|f_1\|_\sigma$;
$\Lambda_\sigma=e^\sigma(2+\delta^{-1})$, $K_0=2\Lambda_\sigma(B+1)/(c-1)$, $Q=(2e)^\tau/\kappa$, $M=QF/\delta$, $A=4K_0M$.
Write $F_n=\|f_n\|_\sigma$ and $d_n=\operatorname{dist}(n\delta,2\mathbb Z)$.

A.1 Arithmetic. The hypothesis implies that $\delta$ is irrational, so no $n\delta$ is an even integer and every Poisson
and potential inverse is defined. Then $0<d_n\le1$, $d_1=\delta$, $d_n\ge\kappa n^{-\tau}$, and
$$d_{m-l}\le d_m+d_l\qquad(m>l\ge1),\tag{A.1}$$
by subtracting the nearest even integers to $m\delta$ and $l\delta$.

A.2 Multipliers. Let $k=2j\ge2$. Then $|k+P_n|=|2j+2-n\delta|\ge d_n$, $k-P_n=k-2+n\delta\ge n\delta$ and $|P_n|\le2n$.
In (B) each input amplitude enters one output through a frequency increase (weight factor $\le e^\sigma$) and at most
one through a decrease (factor $\le1$). For the differentiated stream the two multipliers satisfy
$$\frac k{2|k+P_n|}+\frac k{2(k-P_n)}\le1+\frac{|P_n|}{2d_n}+\frac{|P_n|}{2n\delta}\le(2+\delta^{-1})\frac n{d_n},$$
using $k/|k+P_n|\le1+|P_n|/|k+P_n|$ and $k/(k-P_n)\le1+|P_n|/(k-P_n)$; each bound holds separately for its channel, so
the sum bounds the column. For $|P_n|$ times the undifferentiated stream,
$|P_n|/(2|k+P_n|)+|P_n|/(2(k-P_n))\le(1+\delta^{-1})n/d_n$. Hence
$$\max\{\|g_n'\|_\sigma,\ |P_n|\,\|g_n\|_\sigma\}\le\Lambda_\sigma\frac n{d_n}F_n.\tag{A.2}$$

A.3 Scalar recursion. By the Wiener algebra property, (R), (A.2), $\|f_j'\|_\sigma\le(Bj-1)F_j$ and
$|p_j|\le j$,
$$F_n\le\frac{\Lambda_\sigma(B+1)}{(c-1)(n-1)}\sum_{i+j=n}\frac{ij}{d_i}F_iF_j\qquad(n\ge2).$$
With $Y_n=nF_n/d_n$, $jF_j=d_jY_j\le Y_j$ and $n/(n-1)\le2$ give
$$Y_n\le\frac{K_0}{d_n}\sum_{i+j=n}Y_iY_j,\qquad Y_1=F/\delta.\tag{A.3}$$
Let $b_1=1$, $b_n=d_n^{-1}\sum_{i+j=n}b_ib_j$. Induction gives $Y_n\le K_0^{n-1}Y_1^nb_n$, and
$b_n=\sum_T\prod_{v}d_{s(v)}^{-1}$ over the plane full binary trees $T$ with $n$ leaves (at most $4^{n-1}$ of them), the
product running over the internal vertices $v$, with $s(v)$ the number of leaves below $v$.

A.4 Packing lemma. Fix a tree with $N$ leaves and $0<\varepsilon\le1$. Mark the internal vertices with
$d_{s(v)}<\varepsilon$ and put $q=(\kappa/\varepsilon)^{1/\tau}$.
- Every marked vertex has $s(v)>q$, since $\kappa s^{-\tau}\le d_s<\varepsilon$.
- If two marked vertices are comparable, with sizes $m>l$, then $d_{m-l}<2\varepsilon$ by (A.1), so
  $m-l>(\kappa/(2\varepsilon))^{1/\tau}=q2^{-1/\tau}\ge q/2$.
- Join each marked vertex to its nearest marked descendants. This gives a forest; let $L_0,L_1,L_2$ be the numbers of its
  vertices with no child, one child, and at least two children. Then $L_2\le L_0$ (edge count of a forest).
- Charge to each childless marked vertex all leaves below it (more than $q$), and to each marked vertex with one marked
  child the leaves below it but not below that child (more than $q/2$). These leaf sets are pairwise disjoint.
- Hence $N\ge qL_0+\frac q2L_1$ and the number of marked vertices is
  $L_0+L_1+L_2\le2L_0+L_1\le2N/q=2N(\varepsilon/\kappa)^{1/\tau}$. It is also at most $N-1$.

A.5 Product bound. Since $0<d_s\le1$,
$\log\prod_vd_{s(v)}^{-1}=\int_0^\infty\#\{v:d_{s(v)}<e^{-t}\}\,dt$. Put $t_0=\log(2^\tau/\kappa)>0$ (as $\kappa\le d_1<1$).
Use the bound $N$ for $t<t_0$ and A.4 with $\varepsilon=e^{-t}$ for $t\ge t_0$:
$$\log\prod_vd_{s(v)}^{-1}\le Nt_0+2N\kappa^{-1/\tau}\int_{t_0}^\infty e^{-t/\tau}\,dt=N(t_0+\tau)=N\log\frac{(2e)^\tau}\kappa .$$
So every tree product is at most $Q^N$, $b_n\le4^{n-1}Q^n$, and
$F_n\le Y_n\le K_0^{n-1}Y_1^n4^{n-1}Q^n=QY_1(4K_0QY_1)^{n-1}=MA^{n-1}$.

A.6 Potential and derivatives. Lemma 7.1 and $d_n\ge\kappa n^{-\tau}$ give $\|C_n\|_0\le C_\chi\kappa^{-1}n^\tau F_n$. (A direct estimate of (P) gives the sharper factor $n^{\tau-1}$, Section 7.3; the bound here suffices.)
The undifferentiated stream is bounded directly from the two channels of (B) (not from (A.2), since $P_n$ may be small):
$\|g_n\|_\sigma\le\frac{e^\sigma}2(d_n^{-1}+(n\delta)^{-1})F_n\le\Lambda_\sigma\kappa^{-1}n^{\tau}F_n$, using $d_n\le1$, $n\ge1$. Every Cartesian derivative costs a factor polynomial in $n$
(proof of Theorem A, item 3). For $R>A^{1/\delta}$ these polynomial factors are summable against $(AR^{-\delta})^{n-1}$, so
the proof of Theorem A, item 4, applies verbatim: the sums are a nonzero real-analytic exterior S1 solution. $\square$

A.7 The explicit example. $\delta=1/\sqrt5$, $c=(5+\sqrt5)/4$, so $c-1=(1+\sqrt5)/4$.
- Divisor constant: if $|m-n/\sqrt5|<\frac12$ then $m\sqrt5+n\le n(2+\sqrt5)$ and
  $|m-n/\sqrt5|=|5m^2-n^2|/(\sqrt5(m\sqrt5+n))\ge1/((5+2\sqrt5)n)$, since $5m^2-n^2$ is a nonzero integer; if
  $|m-n/\sqrt5|\ge\frac12$ the bound is immediate because $\kappa/n<\frac12$. So $\tau=1$, $\kappa=1/(5+2\sqrt5)$.
- $f_1=\sin\theta$, $\sigma=\frac12\log2$: $F=e^\sigma=\sqrt2$, $B=2$, $\Lambda_\sigma=\sqrt2(2+\sqrt5)$,
  $K_0=24\sqrt2(2+\sqrt5)/(1+\sqrt5)$, $Q=2e(5+2\sqrt5)$.
- $M=QF/\delta=10\sqrt2\,e(2+\sqrt5)<256$ and $A=4K_0M=1920e(9+4\sqrt5)/(1+\sqrt5)=480e(11+5\sqrt5)<2^{15}$, using
  $e<3$ and $\sqrt5<9/4$.
- $R=2^{36}$: $R^\delta=2^{36/\sqrt5}>2^{16}$ (as $36/\sqrt5>16$), so $AR^{-\delta}<\frac12$ and for $r\ge R$
  $$\Big\|r^{-\gamma}\rho-\sum_{n\le N}r^{-\delta(n-1)}f_n\Big\|_\sigma\le\sum_{n>N}M2^{-(n-1)}=2M\,2^{-N}<512\cdot2^{-N}.$$
- Candidate 007's extracted polynomial at the same $\delta$: top frequency 19, $B=20$, and
  $F=\sqrt2\,T$ with $T=\sum_{k=0}^92^k|a_{2k+1}|<31$ (exact rational evaluation). Relative to $\sin\theta$, $M$ is
  multiplied by $T$ and $A$ by $7T$ ($K_0$ scales by $(B+1)/3=7$). So $M<2^{13}$, $A<2^{15}\cdot217<2^{23}$, and with
  $R=2^{54}$, $R^\delta>2^{24}$, the tail after $N$ terms is at most $2M\,2^{-N}<2^{14}\cdot2^{-N}$.

## Appendix B. Complete proof of the logarithmic degree and Gevrey bounds (Sections 14.2, 14.3)

Setting: $\delta=a/b$ in lowest terms, $t=\log r$, $D=\partial_t$, $\lambda_n=(n-1)(c-1)$, the recursion of Section 14.1
with the canonical normalization $B_{n,j}(0)=0$ at every resonance, $f_1$ a finite odd sine polynomial with top frequency
$L$, $B=L+1$, $F=\|f_1\|_0$. Let $n_r=2b/\gcd(a,2)$, $h=a/\gcd(a,2)$, $\varepsilon=1$ if $h=1$ and $\varepsilon=0$ otherwise,
$\kappa_n=\max(0,\lfloor(n-1)/n_r\rfloor-\varepsilon)$, $\eta_n=\max(0,\lfloor n/n_r\rfloor-\varepsilon)$, $s=4b$,
$$\|H\|_{!,s}=\sum_{k\ge0}k!\,s^k\|[t^k]H\|_0,\qquad C=\frac{56bB}{c-1}.$$
Claim: $\deg_tF_n\le\kappa_n$, $\deg_tG_n\le\eta_n$, and
$$\|F_n\|_{!,s}\le\frac{\kappa_n!}nF(8CF)^{n-1},\qquad\|G_n\|_{!,s}\le4b\,\frac{\kappa_n!}nF(8CF)^{n-1}.$$

B.1 Degrees. $n\delta\in2\mathbb Z$ iff $n_r\mid n$; the stream resonances are $n=n_rm$ with $hm\ge2$ (at $hm=1$,
$n\delta=2$ and $P_n=0$, which is not a stream resonance). The density inverse $(\lambda_n-cD)^{-1}=\sum_k c^kD^k/\lambda_n^{k+1}$
and the nonresonant inverses $(D+v)^{-1}=\sum_k(-1)^kv^{-k-1}D^k$ preserve $t$-degree; the resonant integration raises it
by one. For $i+j=n$, $\eta_i+\kappa_j\le\kappa_n$: for $\varepsilon=0$ this is $\lfloor i/n_r\rfloor+\lfloor(j-1)/n_r\rfloor\le
\lfloor(n-1)/n_r\rfloor$; for $\varepsilon=1$ use also $\max(0,x-1)+\max(0,y-1)\le\max(0,x+y-1)$ for integers
$x,y\ge0$. At a resonance $\eta_n=\kappa_n+1$, otherwise $\eta_n=\kappa_n$. Induction on $n$ gives both degree bounds.

B.2 Norm properties. $\|DH\|_{!,s}\le s^{-1}\|H\|_{!,s}$ and $\|\int_0^tH\|_{!,s}=s\|H\|_{!,s}$ (direct from the weights).
Every nonzero $P_n+2j=2+2j-na/b$ lies in $b^{-1}\mathbb Z$, so $|P_n+2j|\ge1/b$; also $2j-P_n\ge n\delta\ge1/b$. Hence for
these divisors $\|(D+v)^{-1}\|\le1/(|v|-1/s)\le4b/3$.

B.3 Stream inverse. In $B_{n,j}=-\frac12(D+P_n+2j)^{-1}A_{n,j-1}-\frac12(D+P_n-2j)^{-1}A_{n,j}$ each input coefficient
$A_{n,m}$ enters the two outputs $B_{n,m+1}$ and $B_{n,m}$. Its first channel costs at most $\frac12s=2b$ (resonant
integration) or $\frac12\cdot\frac{4b}3$; its second channel costs $\frac12\cdot\frac{4b}3$, plus the same amount again when
the output mode is resonant and its constant term is subtracted to enforce $B_{n,j}(0)=0$. The column sum is
$\le2b+\frac{4b}3<4b$, so $\|G_n\|_{!,s}\le4b\|F_n\|_{!,s}$.

B.4 Products and the density inverse. For polynomials $U,V$ of degrees $\le e,d$,
$\|UV\|_{!,s}\le\binom{e+d}e\|U\|_{!,s}\|V\|_{!,s}$, because $(k+l)!\le\binom{k+l}k k!\,l!$ and $\binom{k+l}k$ is increasing in
$k$ and $l$. Put $u_n=\|F_n\|_{!,s}/\kappa_n!$ and $v_n=\|G_n\|_{!,s}/\eta_n!$. Since $\eta_i+\kappa_j\le\kappa_n$,
$\binom{\eta_i+\kappa_j}{\eta_i}\eta_i!\,\kappa_j!\le\kappa_n!$, so in the normalized quantities the products are lossless; and
$v_n\le4bu_n$ (as $\eta_n\ge\kappa_n$). The density inverse satisfies
$\|(\lambda_n-cD)^{-1}\|\le\lambda_n^{-1}(1-c/(s\lambda_n))^{-1}\le2/\lambda_n$, since $c/(s\lambda_n)=1/(4a(n-1))\le\frac14$.

B.5 Scalar majorant. The angular supports satisfy $\deg_\theta F_n\le Bn-1$, $\deg_\theta G_n\le Bn$. In
$Q_n=\sum[(P_i+D)G_i\,\partial_\theta F_j-\partial_\theta G_i\,(p_j+D)F_j]$ the four factors cost at most $4i$ (as
$|P_i|+s^{-1}\le2i+1\le4i$), $Bj$, $Bi$ and $3j$ (as $|p_j|+s^{-1}\le j+1$) respectively, relative to $\|G_i\|_{!,s}$ and
$\|F_j\|_{!,s}$. With $\|G_i\|\le4b\|F_i\|$ the two terms give $4b(4B+3B)=28bB$ times $ij$, and the density inverse a factor
$2/\lambda_n$.
Combining with B.3 and B.4,
$$u_n\le\frac C{n-1}\sum_{i+j=n}ij\,u_iu_j .$$
With $x_n=nu_n$: $x_1=F$, $x_n\le2C\sum_{i+j=n}x_ix_j$, and the Catalan majorant gives $x_n\le F(8CF)^{n-1}$. This proves
the claim. For analytic profiles the same argument in the strip norms, with the Nagumo device of Theorem A' (an angular
derivative on a strip of width decrease $(\sigma_0-\sigma)/j$), gives the bound with
$C_{\rm an}=(32+48\sigma_0)be^{\sigma_0}/(c-1)$ and the factor $(\sigma_0-\sigma)^{-(n-1)}$. $\square$

B.6 What the bound does not give. For fixed $v\ne0$, $[(D+v)^{-1}t^K]_{t^0}=(-1)^KK!/v^{K+1}$, so separated divisors alone do
not give exponential bounds on the plain coefficients $\|[t^k]F_n\|_0$. The bound above is therefore a Gevrey bound of
order $1/n_r$ ($\kappa_n!\approx(n/n_r)!$), not a convergence proof; Section 14.5 states sufficient estimates.
