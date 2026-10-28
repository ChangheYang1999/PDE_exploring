# Hölder-seminorm constants of the planar second-order Riesz transforms

**Status: final report. The exact sharp constants $C_\alpha$ and $D_\alpha$ were not determined for any fixed
$0<\alpha<1$. Proved and independently verified: the sharp coefficient $2/\pi$ of $1/\alpha$ and the exact second terms for both
constants, the sharp coefficient at $\alpha\to1$, explicit upper bounds for every $\alpha$, and certified two-sided bounds.**

## Summary

*Setting.* Real $f$ on $\mathbb R^2$, $[f]_\alpha=\sup_{x\ne y}|f(x)-f(y)|/|x-y|^\alpha$, operators on the homogeneous space modulo
constants with principal values (Section 1). $C_\alpha=\|T_{xx}\|=\|T_{xy}\|$ (equality proved by rotation), $D_\alpha=\|R_1^2\|$,
$T_{xx}=R_1^2+\frac12I$, and $C_\alpha\le D_\alpha\le C_\alpha+\frac12$. The same norms hold for complex inputs with the modulus seminorm.

*Verdict.* Neither endpoint at fixed $\alpha$ (an exact sharp constant) was reached. The next endpoint of the task, a provably
sharp small-$\alpha$ coefficient, was reached: $C_*=\lim\alpha C_\alpha=\lim\alpha D_\alpha=2/\pi$, together with the second terms.

*Main theorems (all proved and checked by an independent verifier).*
1. For every $0<\alpha<1$ and every real $f\in\dot C^\alpha(\mathbb R^2)$: $[T_{xx}f]_\alpha,[T_{xy}f]_\alpha\le F^{**}(\alpha)[f]_\alpha$ and
   $[R_1^2f]_\alpha\le G^*(\alpha)[f]_\alpha$, with $F^{**}(\alpha)=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{209/500}{1-\alpha}+\frac{1353}{2500}$,
   $G^*(\alpha)=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac{209/500}{1-\alpha}+\frac{72}{125}+\frac12$, $A_\alpha=\frac{\Gamma(1+\alpha/2)}{2\sqrt\pi\,\Gamma(3/2+\alpha/2)}$ (Theorem 9.3).
   The bounds $F$, $G$ of Theorems 3.1, 3.2 are smaller for $\alpha$ above about $0.98$, respectively $0.973$; the computable bounds
   of Theorems 3.3 to 3.10 and 5.7 are smaller at the tabulated exponents (Table 1).
2. $C_\alpha=\frac2{\pi\alpha}+C_0+O(\alpha)$ and $D_\alpha=\frac2{\pi\alpha}+2C_0+O(\alpha)$ as $\alpha\to0^+$, with $C_0=\frac12-\frac{1-\log2}\pi=0.4023257139\ldots$
   (Theorems 5.4, 5.6, 5.7). For $0<\alpha\le\frac1{100}$: $C_\alpha\le\frac2{\pi\alpha}+C_0+2.4755\alpha$ and $D_\alpha\le\frac2{\pi\alpha}+2C_0+2.7250\alpha$.
   The lower $O(\alpha)$ constant is explicit for $C_\alpha$ and not evaluated for $D_\alpha$.
3. $\lim_{\alpha\to1}(1-\alpha)C_\alpha=\lim_{\alpha\to1}(1-\alpha)D_\alpha=\frac{3\sqrt3}{4\pi}$ (Theorem 6.1).
4. For every $\alpha$, an explicit certified function $\ell$ satisfies $\ell\le C_\alpha\le1.0625\,\ell$ and $\ell\le D_\alpha\le1.2894\,\ell$
   (Theorem 9.2; the second uses a lower bound for $C_\alpha$). For $C_\alpha$ the ratio is at most $1.0173$ on $(0,0.005]$ and $1.0263$ on $[0.995,1)$.
5. $T_{xx}$ and $R_1^2$ differ: $D_\alpha-C_\alpha\to C_0$, and $C_\alpha<D_\alpha$ is proved at the ten exponents below, on explicit
   intervals around them, and for all sufficiently small $\alpha$. The complex-input Beurling norm exceeds the real one at every $\alpha$.

*Certified bounds (interval arithmetic, outward rounding; Table 1).*

| $\alpha$ | 0.001 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|---|---|---|
| $C_\alpha\ge$ | 637.019180 | 64.065164 | 13.153259 | 6.811396 | 3.686167 | 2.699605 | 2.089155 | 2.497894 | 4.845586 | 42.002877 |
| $C_\alpha\le$ | 637.024561 | 64.088164 | 13.183951 | 6.851141 | 3.743166 | 2.772659 | 2.193410 | 2.638768 | 5.006611 | 42.217585 |
| $D_\alpha\ge$ | 637.334050 | 64.370268 | 13.416594 | 7.044543 | 3.957869 | 3.016191 | 2.454214 | 2.894834 | 5.241300 | 42.380088 |
| $D_\alpha\le$ | 637.427136 | 64.493836 | 13.614657 | 7.285901 | 4.182558 | 3.216648 | 2.645079 | 3.097370 | 5.468871 | 42.681671 |

The two finest lower certificates ($D_{1/2}$, $D_{3/4}$) have a complete structural audit of all task records and independent
replays of 52 and 70 selected complete tasks; complete independent replays exist for the coarser values $2.4531232777$ and $2.8938332593$.

*Remaining gap.* At the ten tabulated exponents, the certified upper/lower ratio is at most $1.0564$ for $C_\alpha$ (at $\alpha=0.75$) and $1.0778$ for
$D_\alpha$ (at $\alpha=0.5$); at $\alpha=\frac12$ the window is $[2.089155,2.193410]$ for $C$ and $[2.454214,2.645079]$ for $D$. Closing it
needs, at fixed $\alpha$, an upper bound for the two-point dual transport problem that matches an admissible witness. Numerical
linear programs (not proofs) suggest $C_{1/2}\in[2.09,2.12]$, so most of the gap is on the upper side. Also open: $C_\alpha<D_\alpha$ for every $\alpha$ and the lower $O(\alpha)$
constant for $D_\alpha$ (Section 10). No published exact value or explicit bound for these planar norms was found (Section 2).

*Run.* Start $T_0=$ 2026-10-28T00:20:16Z; the planned 16-hour window ran to its cap at 16:20:16Z; this version was completed at
$T_{\rm end}=$ 2026-10-28T16:35:01Z, over 16 h 14 min after $T_0$, after about 15.8 hours of working sessions (Section 12).

Every statement labelled **Theorem** has a complete proof that has been checked independently. A statement
labelled **Conjecture** is not proved. Numerical observations are labelled as such and are never used as proofs.
Reproducible scripts and certified interval data are in the accompanying artifacts.

## 0. Detailed summary

Throughout, $0<\alpha<1$, $[f]_\alpha=\sup_{x\ne y}|f(x)-f(y)|/|x-y|^\alpha$, and

$$C_\alpha=\|T_{xx}\|_{\dot C^\alpha\to\dot C^\alpha}=\|T_{xy}\|_{\dot C^\alpha\to\dot C^\alpha},\qquad
D_\alpha=\|R_1^2\|_{\dot C^\alpha\to\dot C^\alpha},$$

with $T_{xx}=R_1^2+\tfrac12 I$, $T_{xy}=R_1R_2$ (precise definitions in Section 1). The equality
$\|T_{xx}\|=\|T_{xy}\|$ is proved in Section 1.

**Closed-form upper bound (Theorem 3.1).** With

$$a_n(\alpha)=\frac n\pi\int_0^{\pi/(2n)}\sin(nt)\,(2\sin t)^\alpha\,dt\quad(n=1,2,3),\qquad
a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(2+\alpha)},$$

$$b_\alpha=\min\Big\{\frac{a_3(\alpha)+a_1(\alpha)}2,\ \frac{2^{\alpha+1}}{3\pi}\Big\},\quad
B_\alpha=\frac{2a_3(\alpha)}{1-\alpha}+b_\alpha,\quad
s_\alpha=\frac{(1-\alpha)B_\alpha}{2a_2(\alpha)},$$

$$F(\alpha)=\frac{2a_2(\alpha)\,s_\alpha^{\alpha}}{\alpha(1-\alpha)},\qquad
A_\alpha=\frac{\Gamma(\frac{\alpha+2}2)}{2\sqrt\pi\,\Gamma(\frac{\alpha+3}2)},\qquad
G(\alpha)=F(\alpha)\Big(\frac{A_\alpha}{a_2(\alpha)}\Big)^{1-\alpha}+\frac12,$$

every real $f\in\dot C^\alpha(\mathbb R^2)$ satisfies

$$\boxed{[T_{xx}f]_\alpha\le F(\alpha)[f]_\alpha,}\qquad
\boxed{[T_{xy}f]_\alpha\le F(\alpha)[f]_\alpha,}\qquad
\boxed{[R_1^2f]_\alpha\le G(\alpha)[f]_\alpha.}$$

The same inequalities hold for complex-valued $f$ with the modulus seminorm. The bound for $R_1^2$ uses a
projection pairing adapted to the identity term (Theorem 3.2). It is strictly smaller than $F(\alpha)+\frac12$, the
bound given by the triangle inequality.

**Closed-form bounds with a smaller constant term (Theorem 9.3).** With
$\kappa=0.418$, $c_C=0.5412$ and $c_D=0.576$,

$$\boxed{C_\alpha\le F^{**}(\alpha)=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{\kappa}{1-\alpha}+c_C,\qquad
D_\alpha\le G^*(\alpha)=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac{\kappa}{1-\alpha}+c_D+\frac12}$$

for every $0<\alpha<1$. They are smaller than $F$ and $G$ for $\alpha$ below about $0.98$ and $0.973$ respectively, and their
constant terms at $\alpha\to0$ are $0.4203$ and $0.8574$ (sharp: $0.4023$ and $0.8047$).

**Sharper computable upper bounds (Theorems 3.3 to 3.10).** For every $\alpha$ and every integer $m\ge1$,

$$\boxed{C_\alpha\le U_m(\alpha),\qquad D_\alpha\le U^D_m(\alpha),}$$

where $U_m$ and $U^D_m$ are explicit sums of closed-form terms and of the maximum, over $m+1$ kernel phases, of
positive integrals with bounded integrands over fixed compact domains (Section 3). Theorems 3.4 to 3.7 sharpen
the pole-disk, exterior, middle and local parts by finite transport plans. The phase grid is covered by an exact sine
interpolation between adjacent grid phases (Theorem 3.8), never worse than a factor $\sec(\pi/(4m))$, so no direction is assumed
to be extremal. For $D_\alpha$, the positive local remainder that carries the identity term is charged $\frac12$ by translation in
these bounds; a reflection coupling on two inscribed disks charges it strictly less (Theorems 3.9 and 3.10), and in particular
$D_\alpha<G(\alpha)$ for every $\alpha$. Certified values are in Table 1.

**Lower bounds (Section 4).** $C_\alpha\ge L(\alpha)$ and $D_\alpha\ge L(\alpha)$, where $L(\alpha)$ is the maximum over
explicit certified witness families. At every exponent in Table 1 the best is a polygonal signed-distance
witness with an optimized shape parameter. For $D_\alpha$ alone, a witness that uses the identity term
(Theorem 4.6, $0<\alpha\le\frac12$) gives more at the listed exponents $\alpha\le0.3$, and proves the strict separation $C_\alpha<D_\alpha$ at six exponents:

$$\boxed{C_{1/1000}\le637.02457<637.33405\le D_{1/1000},\qquad C_{1/100}\le64.08817<64.37026\le D_{1/100},\qquad
C_{1/20}\le13.18396<13.41659\le D_{1/20},}$$

$$\boxed{C_{1/10}\le6.85115<7.02597\le D_{1/10},\qquad C_{1/5}\le3.74317<3.80880\le D_{1/5},\qquad C_{3/10}\le2.77266<2.80517\le D_{3/10}.}$$

Half-plane lattice witnesses in the axis phase (Theorem 4.7) prove the separation also at four larger exponents, and give larger
margins at $\alpha=\frac1{10}$, $\alpha=\frac15$ and $\alpha=\frac3{10}$:

$$\boxed{C_{1/2}\le2.19341<2.45421\le D_{1/2},\qquad C_{3/4}\le2.63877<2.89483\le D_{3/4},\qquad C_{9/10}\le5.00662<5.24130\le D_{9/10},}$$

$$\boxed{C_{99/100}\le42.21759<42.38008\le D_{99/100},\qquad C_{1/10}\le6.85115<7.04454\le D_{1/10},}$$

$$\boxed{C_{1/5}\le3.74317<3.95786\le D_{1/5},\qquad C_{3/10}\le2.77266<3.01619\le D_{3/10}.}$$

Since $D_\alpha-C_\alpha\to C_0>0$ (items 4 and 5 below), the separation $C_\alpha<D_\alpha$ also holds for all sufficiently small $\alpha$;
no explicit threshold is claimed. Since $C_\alpha$ and $D_\alpha$ are continuous in $\alpha$ (Theorem 1.5), each of the ten certified
separations also holds on an explicit closed interval around its exponent, of radius $5\cdot10^{-8}$, $5\cdot10^{-6}$, $10^{-4}$,
$5\cdot10^{-4}$, $0.002$, $0.003$, $0.002$, $0.001$, $2\cdot10^{-4}$ and $10^{-6}$ in the order of Table 1 (the remarks after Theorem 1.5).

**Best coefficient of $1/\alpha$ and the gap.** The coefficient $2/\pi$ of $1/\alpha$ is proved to be sharp for both
$C_\alpha$ and $D_\alpha$. The next term is also determined exactly for both: $C_\alpha=\frac2{\pi\alpha}+C_0+o(1)$
and $D_\alpha=\frac2{\pi\alpha}+2C_0+o(1)$ (items 4 and 5 below). So there is no asymptotic gap through order
$\alpha^0$. The closed-form bounds have the sharp coefficient $2/\pi$ but not the sharp constant term:
$F-\frac2{\pi\alpha}\to0.7221$ and $G-\frac2{\pi\alpha}\to1.1244$; for $F^{**}$ and $G^*$ (Theorem 9.3) the limits are $0.4203$ and
$0.8574$, against the sharp $C_0=0.4023$ and $2C_0=0.8047$. The explicit bounds of Theorem 5.7 have the sharp first two
terms: $C_\alpha\le\frac2{\pi\alpha}+C_0+2.4755\alpha$ and $D_\alpha\le\frac2{\pi\alpha}+2C_0+2.7250\alpha$ for $0<\alpha\le\frac1{100}$. With the matching
lower expansion, $C_\alpha=\frac2{\pi\alpha}+C_0+O(\alpha)$. So for $C_\alpha$ the gap between proved upper and lower bounds is $O(\alpha)$ as
$\alpha\to0$; for $D_\alpha$ it is also $O(\alpha)$ (Theorem 5.7(v)), with a lower constant that is not evaluated. At fixed $\alpha$, the certified ratio of upper to lower bound for $C_\alpha$ is
at most $1.0564$ at the ten exponents of Table 1; for $D_\alpha$ it is at most $1.0778$, attained at $\alpha=0.5$. For $C_\alpha$ it is at most $1.0173$ on the whole interval $0<\alpha\le0.005$ and
at most $1.0263$ on the whole interval $0.995\le\alpha<1$ (Theorem 9.1). For every $0<\alpha<1$ the certified bounds satisfy
$\ell(\alpha)\le C_\alpha\le1.0625\,\ell(\alpha)$ and $\ell(\alpha)\le D_\alpha\le1.2894\,\ell(\alpha)$ with an explicit certified lower function
$\ell$ (Theorem 9.2).

**Small $\alpha$ (Section 5).**

1. *Leading coefficient (Theorem 5.1), proven asymptotically sharp:* $\lim_{\alpha\to0}\alpha C_\alpha=\lim_{\alpha\to0}\alpha D_\alpha=2/\pi$, so $C_*=2/\pi$.
2. *Second term for one fixed-direction functional (Theorem 5.2):* the norm of $f\mapsto T_{xy}f(e_1/2)-T_{xy}f(-e_1/2)$
   on $\{[f]_\alpha\le1\}$ equals $\frac2{\pi\alpha}+\frac12-\frac{1-\log2}\pi+o(1)$.
3. *Variational formula for the second term (Theorem 5.3):* $C_\alpha=\frac2{\pi\alpha}+C_0+o(1)$, with $C_0$ the maximum
   over directions of an explicit finite-part integral.
4. *Two-term asymptotics of $C_\alpha$ (Theorem 5.4):* the maximum in item 3 is attained exactly in the diagonal
   direction, so

$$\boxed{C_\alpha=\frac{2}{\pi\alpha}+C_0+o(1)\qquad(\alpha\to0^+),\qquad C_0=\frac12-\frac{1-\log 2}{\pi}=0.4023257139688609\ldots}$$

   Two independent proofs of the maximality were written and cross-checked.
5. *Two-term asymptotics of $D_\alpha$ (Theorem 5.6):*

$$\boxed{D_\alpha=\frac{2}{\pi\alpha}+2C_0+o(1)\qquad(\alpha\to0^+),\qquad 2C_0=1-\frac{2(1-\log2)}{\pi}=0.8046514279377218\ldots}$$

   Hence $D_\alpha-C_\alpha\to C_0$: the identity term in $R_1^2=T_{xx}-\frac12I$ raises the second term by exactly $C_0$. The
   upper bound comes from the projection pairing (Theorem 3.2). The lower bound comes from an explicit witness that
   realizes that pairing at both poles at once, with Hölder seminorm $1+O(\alpha^2)$. An earlier, weaker lower bound
   $\liminf(D_\alpha-\frac2{\pi\alpha})\ge C_0+\frac2\pi\log\cosh\frac\pi4=0.5812906021$ (Theorem 5.5) is superseded.
6. *Explicit second-term bounds and a linear remainder (Theorem 5.7):* for every $\alpha$ and $0<\rho<\frac12$, $C_\alpha\le J_C(\alpha,\rho)$
   and $D_\alpha\le J_D(\alpha,\rho)$ with explicit $J_C$, $J_D$ whose expansions are $\frac2{\pi\alpha}+C_0+O_\rho(\alpha)$ and
   $\frac2{\pi\alpha}+2C_0+O_\rho(\alpha)$. In particular, for $0<\alpha\le\frac1{100}$,

$$\boxed{C_\alpha\le\frac2{\pi\alpha}+C_0+2.4755\,\alpha,\qquad D_\alpha\le\frac2{\pi\alpha}+2C_0+2.7250\,\alpha,}$$

   and a signed-distance witness gives $C_\alpha\ge\frac2{\pi\alpha}+C_0+\kappa_C\alpha+o(\alpha)$, so $C_\alpha=\frac2{\pi\alpha}+C_0+O(\alpha)$. A fixed-radius
   projection witness with a Hölder-envelope repair gives $D_\alpha\ge\frac2{\pi\alpha}+2C_0-O(\alpha)$, so also $D_\alpha=\frac2{\pi\alpha}+2C_0+O(\alpha)$.

**Endpoint $\alpha\to1$ (Theorem 6.1), proven asymptotically sharp:**
$\lim_{\alpha\to1}(1-\alpha)C_\alpha=\lim_{\alpha\to1}(1-\alpha)D_\alpha=\frac{3\sqrt3}{4\pi}$.

**Status of each result (labels of the task specification).**

| Result | Label |
|---|---|
| $\lim\alpha C_\alpha=\lim\alpha D_\alpha=2/\pi$ | proven asymptotically sharp |
| $\lim(1-\alpha)C_\alpha=\lim(1-\alpha)D_\alpha=3\sqrt3/(4\pi)$ | proven asymptotically sharp |
| $C_\alpha=2/(\pi\alpha)+\frac12-(1-\log2)/\pi+o(1)$ | proven asymptotically sharp to second order |
| $D_\alpha=2/(\pi\alpha)+1-2(1-\log2)/\pi+o(1)$, $D_\alpha-C_\alpha\to C_0$ | proven asymptotically sharp to second order |
| $C_\alpha=2/(\pi\alpha)+C_0+O(\alpha)$, $D_\alpha=2/(\pi\alpha)+2C_0+O(\alpha)$; $C_\alpha\le\frac2{\pi\alpha}+C_0+2.4755\alpha$, $D_\alpha\le\frac2{\pi\alpha}+2C_0+2.7250\alpha$ on $(0,\frac1{100}]$; $C_\alpha\le J_C$, $D_\alpha\le J_D$ for all $\alpha$ (Theorem 5.7) | proven asymptotically sharp to second order with an explicit linear upper error; the error is $O(\alpha)$ in both directions (lower constant explicit for $C_\alpha$ only) |
| $C_\alpha\le\min(F,U_m)$, $D_\alpha\le\min(G,U^D_m)$ and Theorems 3.4 to 3.10, for all $\alpha$ | rigorous near-sharp at both endpoints (uniform ratio for $C_\alpha$ at most $1.027$ on $(0,0.005]\cup[0.995,1)$); rigorous nonsharp intermediate bound for moderate $\alpha$ (certified ratio for $C_\alpha$ $\le1.057$ at the exponents of Table 1 and $\le1.0625$ for every $\alpha$; for $D_\alpha$ $\le1.0778$ and $\le1.2894$; Theorem 9.2) |
| $C_\alpha\le F^{**}(\alpha)$, $D_\alpha\le G^*(\alpha)$ for all $\alpha$ (Theorem 9.3) | rigorous nonsharp closed-form bound |
| $C_\alpha\ge L(\alpha)$, $D_\alpha\ge L(\alpha)$ | rigorous (certified) lower bounds |
| $D_\alpha\ge(J_\alpha+\frac12)/K_\alpha$ for $\alpha\le\frac12$; $C_\alpha<D_\alpha$ at $\alpha=\frac1{1000},\frac1{100},\frac1{20},\frac1{10},\frac15,\frac3{10}$; Theorem 4.7: $D_{1/10}\ge7.0445$, $D_{1/5}\ge3.9578$, $D_{3/10}\ge3.0161$, $D_{1/2}\ge2.4542$, $D_{3/4}\ge2.8948$, $D_{9/10}\ge5.2413$, $D_{99/100}\ge42.3800$, $C_\alpha<D_\alpha$ at $\frac12,\frac34,\frac9{10},\frac{99}{100}$ | rigorous (certified) lower bound and strict separation |
| Parity restrictions do not change $C_\alpha$, $D_\alpha$ (Theorem 1.1); the three operators are unbounded for the full norm $\|f\|_\infty+[f]_\alpha$ (Theorem 1.2); $C_\alpha$, $D_\alpha$ are limits of finite transport problems with explicit errors (Theorem 1.3); $C_\alpha$, $D_\alpha$ are continuous in $\alpha$, with an explicit modulus (Theorem 1.5); extremal functions exist in the homogeneous space for all three operators (Theorem 1.6); on complex inputs $S=T_{xx}+iT_{xy}$ has explicit two-sided bounds with $\alpha N_\alpha\to1$ and $(1-\alpha)N_\alpha\to\frac23$, and $N_\alpha>C_\alpha$ for every $\alpha$, so the complex-input Beurling norm exceeds the real-input one at every exponent (Theorem 1.4) | rigorous |
| Exact values of $C_\alpha$, $D_\alpha$ for fixed $\alpha$ | not determined; the estimates in Section 7 are numerical conjectures |

**Table 1. Certified bounds.** Upper bounds are upper interval endpoints rounded up, lower bounds lower endpoints
rounded down, at six decimals. The columns $F$, $F+\frac12$ and $G$ are the closed-form bounds; $F+\frac12$ is the
triangle-inequality bound for $D_\alpha$ and is superseded by $G$. The best upper columns are the
smallest certified values of Theorems 3.1 to 3.10, 5.7 and 9.3. The
column $L(\alpha)$ bounds both $C_\alpha$ and $D_\alpha$. The column "best lower $D_\alpha$" repeats it, except for the bold
entries, which come from the projection witness of Theorem 4.6 ($\alpha\le\frac1{20}$) and the lattice witness of Theorem 4.7
($\alpha=0.1,0.2,0.3,\frac12,\frac34,\frac9{10},0.99$) and bound $D_\alpha$ only; they exceed the best upper bound for $C_\alpha$. The ratios are best upper over best lower bound. The last column is the two-term asymptotic
value of $C_\alpha$ and is not a bound.

| $\alpha$ | $F\ge C_\alpha$ | $F+\frac12$ | $G\ge D_\alpha$ | best upper $C_\alpha$ | best upper $D_\alpha$ | $L(\alpha)\le C_\alpha$ | polygon shape $a$ | best lower $D_\alpha$ | ratio for $C$ | ratio for $D$ | $\frac2{\pi\alpha}+C_0$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | 637.342465 | 637.842465 | 637.744762 | 637.024561 | 637.427136 | 637.019180 | 0.577 | **637.334050** | 1.0001 | 1.0002 | 637.0221 |
| 0.01 | 64.390137 | 64.890137 | 64.792178 | 64.088164 | 64.493836 | 64.065164 | 0.576 | **64.370268** | 1.0004 | 1.0020 | 64.0643 |
| 0.05 | 13.485817 | 13.985817 | 13.886755 | 13.183951 | 13.614657 | 13.153259 | 0.57 | **13.416594** | 1.0024 | 1.0148 | 13.1347 |
| 0.1 | 7.153626 | 7.653626 | 7.553279 | 6.851141 | 7.285901 | 6.811396 | 0.563 | **7.044543** | 1.0059 | 1.0343 | 6.7685 |
| 0.2 | 4.048333 | 4.548333 | 4.445798 | 3.743166 | 4.182558 | 3.686167 | 0.545 | **3.957869** | 1.0155 | 1.0568 | 3.5854 |
| 0.3 | 3.082363 | 3.582363 | 3.478289 | 2.772659 | 3.216648 | 2.699605 | 0.524 | **3.016191** | 1.0271 | 1.0665 | 2.5244 |
| 0.5 | 2.513787 | 3.013787 | 2.909435 | 2.193410 | 2.645079 | 2.089155 | 0.465 | **2.454214** | 1.0500 | 1.0778 | 1.6756 |
| 0.75 | 2.946087 | 3.446087 | 3.350210 | 2.638768 | 3.097370 | 2.497894 | 0.329 | **2.894834** | 1.0564 | 1.0700 | 1.2512 |
| 0.9 | 5.281265 | 5.781265 | 5.696277 | 5.006611 | 5.468871 | 4.845586 | 0.229 | **5.241300** | 1.0333 | 1.0435 | 1.1097 |
| 0.99 | 42.424680 | 42.924680 | 42.848126 | 42.217585 | 42.681671 | 42.002877 | 0.173 | **42.380088** | 1.0052 | 1.0072 | 1.0454 |

The best upper bound for $C_\alpha$ comes from the explicit bound $J_C$ of Theorem 5.7(ii) at $\alpha=0.001$ and from the
paired local circles with the balanced and radial residual couplings (Theorem 3.7) and the middle-arc residual cost
of Theorem 3.6, with the phase interpolation of Theorem 3.8, at the other nine exponents. The best upper bound for $D_\alpha$
comes from $J_D$ at $\alpha=0.001,0.01$, from the exterior circles at $\alpha=0.05,0.1$ and from the middle-circle transport with the
middle-arc residual cost (Theorem 3.6), the finer cross-disk enclosure and the phase interpolation of Theorem 3.8 at
$\alpha=0.2,0.3,0.5,0.75,0.9,0.99$, in every case lowered by the strict saving of Theorem 3.10. The table is
regenerated from the certified data by a script in the accompanying artifacts. An independent selection from the
same certificates gave identical entries.

**Guide to the requested items.** (1) Definitions and identities: Section 1 (with the parity classes, the full norm,
the transport formulation and complex inputs in Theorems 1.1 to 1.4). (2) Literature: Section 2.
(3) Upper-bound theorems: Theorems 3.1 to 3.10, the explicit second-term bounds of Theorem 5.7, and the closed forms of Theorem 9.3. (4) Proofs: after each theorem, with full versions in the accompanying
artifacts. (5) Optimizations (cutoff radius, shell constant, projection pairing, midpoint split, reflection orbits,
witness shapes): Sections 3 and 4. (6) Rigorous lower bounds: Section 4 (Theorems 4.6 and 4.7 for $D_\alpha$) and Theorems 5.5, 5.6. (7) Numerics: Section 7.
(8) Small-$\alpha$ asymptotics: Section 5, with the endpoint $\alpha\to1$ in Section 6. (9) Comparison of $T_{xx}$,
$T_{xy}$ and $R_1^2$: Section 8. (10) Unresolved steps and the gap: Sections 9 and 10.

## 1. Definitions, normalizations and identities

**Seminorm and space.** For $0<\alpha<1$ and $f:\mathbb R^2\to\mathbb R$,
$[f]_\alpha=\sup_{x\ne y}|f(x)-f(y)|/|x-y|^\alpha$ and $\dot C^\alpha(\mathbb R^2)=\{f:[f]_\alpha<\infty\}/\mathbb R$ (functions
modulo additive constants). For complex $f$ the same formula with the modulus is used.

**Kernels and operators.** With $z=r(\cos\theta,\sin\theta)$,

$$K_{xx}(z)=\frac{\cos2\theta}{2\pi r^2},\qquad K_{xy}(z)=\frac{\sin2\theta}{2\pi r^2},\qquad
T_{xx}f=\mathrm{p.v.}\,K_{xx}*f,\quad T_{xy}f=\mathrm{p.v.}\,K_{xy}*f .$$

With $\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx$ and $R_j=\partial_j(-\Delta)^{-1/2}$ (multiplier $i\xi_j/|\xi|$), the
distributional identity $\partial_i\partial_j\big(-\tfrac1{2\pi}\log|z|\big)=\mathrm{p.v.}\frac{2z_iz_j-\delta_{ij}|z|^2}{2\pi|z|^4}-\tfrac12\delta_{ij}\delta_0$
gives

$$T_{xx}=R_1^2+\tfrac12 I,\qquad T_{xy}=R_1R_2,\qquad
m_{xx}(\xi)=\frac{\xi_2^2-\xi_1^2}{2|\xi|^2}=-\tfrac12\cos2\psi,\qquad m_{xy}(\xi)=-\frac{\xi_1\xi_2}{|\xi|^2}=-\tfrac12\sin2\psi,$$

where $\xi=|\xi|(\cos\psi,\sin\psi)$, and $R_1^2$ has multiplier $-\cos^2\psi$. If $u=\frac1{2\pi}\log|\cdot|*f$, so that
$\Delta u=f$, then $u_{x_1x_1}=\tfrac12f-T_{xx}f$, $u_{x_2x_2}=\tfrac12f+T_{xx}f$, $u_{x_1x_2}=-T_{xy}f$.

**Extension to $\dot C^\alpha$.** For $f$ of growth $O(|z|^\alpha)$ and a base point $p$, the increment

$$\mathcal T f(x)-\mathcal Tf(p)=\lim_{M\to\infty}\lim_{\epsilon\to0}\int_{|z-p|<M}
\big(K(x-z)\mathbf 1_{|x-z|>\epsilon}-K(p-z)\mathbf 1_{|p-z|>\epsilon}\big)(f(z)-f(p))\,dz$$

converges absolutely after the local subtractions (the kernel difference is $O(|x-p||z|^{-3})$ at infinity), does not
depend on additive constants in $f$, and agrees with the principal-value convolution for $f\in C_c^\infty$. The operator
norms

$$C_\alpha=\sup_{[f]_\alpha\ne0}\frac{[T_{xx}f]_\alpha}{[f]_\alpha},\qquad D_\alpha=\sup_{[f]_\alpha\ne0}\frac{[R_1^2f]_\alpha}{[f]_\alpha}$$

are the same whether the supremum runs over real $f\in C_c^\infty(\mathbb R^2)$ or over all real $f\in\dot C^\alpha$
(approximation by McShane extension, truncation and mollification; the accompanying artifacts contain the proof).

**Identities.**

1. Rotation: if $U_\beta f(x)=f(Q_\beta x)$ with $Q_\beta$ the rotation by $\beta$, then
   $U_\beta^{-1}T_{xx}U_\beta=\cos2\beta\,T_{xx}+\sin2\beta\,T_{xy}$. Hence $\|T_{xx}\|=\|T_{xy}\|=\|\cos\gamma T_{xx}+\sin\gamma T_{xy}\|$
   for every $\gamma$, and rotation by $\pi/2$ maps $T_{xx}$ to $-T_{xx}$, so $\|T_{xx}-\tfrac12I\|=\|T_{xx}+\tfrac12I\|=D_\alpha$
   (also $=\|R_2^2\|$).
2. $C_\alpha\le D_\alpha\le C_\alpha+\tfrac12$ (from $T_{xx}=\tfrac12[(T_{xx}-\tfrac12I)+(T_{xx}+\tfrac12I)]$ and the
   triangle inequality), and $C_\alpha\ge\tfrac12$, $D_\alpha\ge1$ (test function $\cos x_1$).
3. Complex form: $S=T_{xx}+iT_{xy}$ has kernel $\frac1{2\pi\bar z^2}$ and multiplier $-\tfrac12e^{2i\psi}$;
   $S=-\tfrac12\overline{B\bar f}$ for the Beurling transform $Bf=-\frac1\pi\,\mathrm{p.v.}\,\frac1{z^2}*f$. For real
   inputs, $\|S\|_{\dot C^\alpha\to\dot C^\alpha(\mathbb C)}=C_\alpha$ and $\|B\|_{\dot C^\alpha(\mathbb R)\to\dot C^\alpha(\mathbb C)}=2C_\alpha$.
4. Duality form of the norm. For $|x-y|=1$ (by scaling and translation every increment reduces to this case),
   $T_{xx}f(x)-T_{xx}f(y)=\int\nu(w)f(w)\,dw$ with the principal-value density $\nu(w)=K_{xx}(x-w)-K_{xx}(y-w)$. Taking
   $x=(\tfrac12,0)$, $y=-x$ and rotating the kernel instead of the points, with $K_b(z)=\cos(2\arg z-2b)/(2\pi|z|^2)$,

   $$C_\alpha=\sup_{b}\ V(\alpha,b),\qquad V(\alpha,b)=\sup_{[f]_\alpha\le1}\int\nu_b f,\qquad
   \nu_b(w)=\operatorname{Re}\big(e^{2ib}G(w)\big),\quad G(w)=\frac{w}{\pi(w^2-\frac14)^2}$$

   in complex notation. Similarly $D_\alpha=\sup_b\sup_{[f]_\alpha\le1}\big(\int\nu_bf-\tfrac12(f(x)-f(y))\big)$.

**Theorem 1.1 (coordinate parity classes).** Let $\chi_1,\chi_2\in\{-1,1\}$ and let $X_\chi$ be the class of real functions with
$f(-z_1,z_2)=\chi_1f(z_1,z_2)$ and $f(z_1,-z_2)=\chi_2f(z_1,z_2)$. For $A\in\{T_{xx},T_{xy},R_1^2\}$,

$$\sup_{0\ne f\in C_c^\infty(\mathbb R^2)\cap X_\chi}\frac{[Af]_\alpha}{[f]_\alpha}=\|A\|_{\dot C^\alpha\to\dot C^\alpha},$$

and the same holds for the supremum over $f\in\dot C^\alpha$ that have a representative in $X_\chi$. Thus functions that are odd or
even in each variable give the same constants $C_\alpha$ (for $T_{xx}$, $T_{xy}$) and $D_\alpha$ (for $R_1^2$).

*Proof.* Let $0\ne f\in C_c^\infty$ have support in $B(0,R)$, let $p\ne q$ lie in $B(0,R)$, and for $L>R$ put $a_L=(L,L)$,
$Q_\epsilon=\operatorname{diag}(\epsilon_1,\epsilon_2)$ and
$F_L(z)=\sum_{\epsilon\in\{\pm1\}^2}\chi_1^{(1-\epsilon_1)/2}\chi_2^{(1-\epsilon_2)/2}f(Q_\epsilon z-a_L)$. Then $F_L\in C_c^\infty\cap X_\chi$, and the four
summands are supported in balls at mutual distance at least $2L-2R$. If $2\|f\|_\infty\le[f]_\alpha(2L-2R)^\alpha$, a case split over
the positions of two points (same ball, one ball and the complement of all balls, different balls) gives
$[F_L]_\alpha\le[f]_\alpha$. The summand with $\epsilon=(1,1)$ contributes exactly $Af(p)-Af(q)$ to $AF_L(a_L+p)-AF_L(a_L+q)$. Since
$|\nabla K_{xx}(z)|=|\nabla K_{xy}(z)|=1/(\pi|z|^3)$, the mean value theorem bounds the contribution of each of the other three
summands by $|p-q|\,\|f\|_1/(\pi(2L-2R)^3)$, and their identity terms vanish at the two points. If $N_\chi$ is the restricted
supremum, then $|Af(p)-Af(q)|\le N_\chi[f]_\alpha|p-q|^\alpha+3|p-q|\,\|f\|_1/(\pi(2L-2R)^3)$, and $L\to\infty$ gives the unrestricted bound.
The reverse inequality is inclusion of the test classes, and the statement for $\dot C^\alpha$ follows from the approximation
statement above. $\square$

The statement concerns the output seminorm over all pairs of points in the plane. It says nothing about increments at a
fixed pair of points near the coordinate axes, or about problems on bounded domains.

**Theorem 1.2 (the full Hölder norm).** For $A\in\{T_{xx},T_{xy},R_1^2\}$,

$$\sup_{0\ne f\in C_c^\infty(\mathbb R^2)}\ \frac{\inf_{c\in\mathbb R}\|Af+c\|_\infty}{\|f\|_\infty+[f]_\alpha}=\infty .$$

So none of the three operators is bounded for the whole-plane norm $\|f\|_\infty+[f]_\alpha$, even after the output is normalized
by a constant. The constants $C_\alpha$ and $D_\alpha$ of this report are seminorm constants only. Full-norm estimates, such as local
Schauder estimates on bounded domains, answer a different question.

*Proof.* Let $\chi$ be smooth and nondecreasing, $\chi=0$ on $(-\infty,1]$, $\chi=1$ on $[2,\infty)$, $|\chi'|\le2$. For $R\ge2$ put
$\eta_R(r)=\chi(r)(1-\chi(r/R))$ and $f_R=\eta_R(r)\cos2\theta$ ($\eta_R(r)\sin2\theta$ for $T_{xy}$). Then $|f_R|\le1$ and $|\nabla f_R|\le2\sqrt2$,
so $|f_R(z)-f_R(w)|\le\min(3|z-w|,2)$, $[f_R]_\alpha\le2^{1-\alpha}3^\alpha$ and $\|f_R\|_\infty+[f_R]_\alpha\le4$. Since $f_R=0$ near the origin,

$$T_{xx}f_R(0)=\frac1{2\pi}\int_0^{2\pi}\cos^22\theta\,d\theta\int_0^\infty\eta_R(r)\,\frac{dr}r\ \ge\ \frac12\log\frac R2,$$

and the same holds for $T_{xy}$; also $R_1^2f_R(0)=T_{xx}f_R(0)$. Each transform tends to $0$ at infinity, so its oscillation is at
least $\frac12\log\frac R2$ and $\inf_c\|Af_R+c\|_\infty\ge\frac14\log\frac R2$. The quotient is at least $\frac1{16}\log\frac R2$. $\square$

**Theorem 1.3 (finite transport approximation).** For $0<\epsilon<\frac12$ and $R>1$ let
$\Omega=B(0,R)\setminus(B(x,\epsilon)\cup B(y,\epsilon))$, $\mu_b=\mathbf 1_\Omega\nu_b\,dA$ and $\mu_b^D=\mu_b-\frac12\delta_x+\frac12\delta_y$, with $x,y,\nu_b$ as in
item 4. For a finite signed measure $\mu$ of total mass zero and compact support let $W_\alpha(\mu)$ be the infimum of
$\int|z-w|^\alpha\,d\pi(z,w)$ over couplings $\pi\ge0$ of $\mu^+$ and $\mu^-$. Then, with

$$E=\frac{2a_2(\alpha)\epsilon^\alpha}\alpha+\frac{(1+2\epsilon)^\alpha\epsilon^2}{2(1-\epsilon)^2}+\frac{2^\alpha R^{\alpha-1}}{(1-\alpha)(1-1/(4R^2))^2},$$

$$\Big|C_\alpha-\sup_bW_\alpha(\mu_b)\Big|\le E,\qquad \Big|D_\alpha-\sup_bW_\alpha(\mu_b^D)\Big|\le E .$$

*Proof.* For a finite zero-mass measure, $W_\alpha(\mu)=\sup_{[f]_\alpha\le1}\int f\,d\mu$: one inequality holds for every coupling because
$|z-w|^\alpha$ is a metric; for atomic measures the other is finite linear-programming duality (with the potential
$f=\min_j(B_j+|\cdot-q_j|^\alpha)$); a general measure is pushed to representatives of a partition with cells of diameter $h$, which
changes both sides by at most $h^\alpha|\mu|(\mathbb R^2)$, and $h\to0$. It remains to compare the principal-value functional with
$\int f\,d\mu_b$ for $[f]_\alpha\le1$. On each omitted disk the own-pole kernel has mean zero on circles, and the exact angular lemma
(part (a) of the proof of Theorem 3.1) bounds its contribution by $a_2(\alpha)\epsilon^\alpha/\alpha$. The two other-pole terms combine by central reflection into
$-\int_{B(x,\epsilon)}K_b(z-y)(f(z)-f(-z))\,dA$, at most $\frac{(1+2\epsilon)^\alpha\epsilon^2}{2(1-\epsilon)^2}$. On $|z|>R$, central reflection and
$|\nu_b(z)|\le|z|/(\pi(|z|^2-\frac14)^2)$ give the last term. The atoms are the same on both sides. $\square$

So the operator norms are limits of finite-measure transport problems as $\epsilon\to0$, $R\to\infty$. A computed discrete
transport value becomes a bound only if the spatial discretization (at most $h^\alpha|\mu|(\mathbb R^2)$), the phase sampling (at
most $2\sin(h_0/2)F(\alpha)$ for phase spacing $h_0$) and the cell masses are also controlled. The linear-programming values of
Section 7 do not control these errors and are not bounds.

**Theorem 1.4 (complex inputs; the Beurling transform).** Let $N_\alpha$ be the norm of $S=T_{xx}+iT_{xy}$ on complex-valued
$\dot C^\alpha(\mathbb R^2)$ (modulus seminorm, modulo complex constants). By identity 3 the Beurling transform has norm $2N_\alpha$
on complex inputs and $2C_\alpha$ from real to complex inputs. For integers $n\ge1$ put $Q_n=\max_{0\le t\le\pi/(2n)}\sin(nt)/\sin^\alpha t$
and $b_n=2^{\alpha-1}/Q_n$, so that $Q_1=1$ and

$$Q_2=\frac2{\sqrt{2-\alpha}}\Big(\frac{1-\alpha}{2-\alpha}\Big)^{\frac{1-\alpha}2},\qquad
Q_3=\frac6{3-\alpha}\Big(\frac{3(1-\alpha)}{4(3-\alpha)}\Big)^{\frac{1-\alpha}2}.$$

Put $\mathcal A_\alpha=\frac{2^{-\alpha}}\alpha+\int_0^{1/2}\frac{t^\alpha}{1-t}dt$, $\mathcal B_\alpha=\frac{2b_3}{1-\alpha}+\min\{\frac{b_1+b_3}2,\frac{2^\alpha}\pi\}$ and
$\tilde s_\alpha=\frac{(1-\alpha)\mathcal B_\alpha}{2b_2}$. Then for every $0<\alpha<1$:

(i) $[\,|z|^\alpha e^{\pm in\arg z}]_\alpha=2^{1-\alpha}Q_n$ exactly, and $\big|\frac1{2\pi}\int_0^{2\pi}e^{in\theta}f(re^{i\theta})d\theta\big|\le b_nr^\alpha[f]_\alpha$ for every
complex $f$ and $r>0$, with equality for $f=|z|^\alpha e^{-in\arg z}$;

(ii)
$$\max\Big\{\frac{\mathcal A_\alpha}{Q_2}+\frac{2^\alpha\pi\alpha}{Q_3\sin\pi\alpha},\ \frac{\alpha+3}{2(1-\alpha)Q_3}\Big\}\ \le\ N_\alpha\ \le\
\frac{2b_2\,\tilde s_\alpha^{\alpha}}{\alpha(1-\alpha)};$$

(iii) $N_\alpha>C_\alpha$: the complex-input norm of the Beurling transform is strictly larger than its real-input norm at every exponent;

(iv) $\alpha N_\alpha\to1$ as $\alpha\to0$ and $(1-\alpha)N_\alpha\to\frac23$ as $\alpha\to1$, against $\alpha C_\alpha\to\frac2\pi$ and
$(1-\alpha)C_\alpha\to\frac{3\sqrt3}{4\pi}$ (Theorems 5.1 and 6.1), so the ratio of the two Beurling norms tends to $\frac\pi2$ and to $\frac{8\pi}{9\sqrt3}$;
moreover $\liminf_{\alpha\to0}(N_\alpha-\frac1\alpha)\ge1-\frac{\log2}2$;

(v) $T_{xx}$, $T_{xy}$ and $R_1^2$ have real kernels and real local terms, and their norms on complex inputs are $C_\alpha$, $C_\alpha$, $D_\alpha$.

Both sides of (ii) have the sharp coefficients of (iv) at both endpoints. Expanding the upper bound at $\alpha=0$
(where $Q_2=1+\frac{\log2}2\alpha+O(\alpha^2)$ and $\tilde s_0=1+\frac1\pi$) gives $\limsup_{\alpha\to0}(N_\alpha-\frac1\alpha)\le1+\frac{\log2}2+\log(1+\frac1\pi)=1.62292\ldots$,
so $0.6534\le\liminf_{\alpha\to0}(N_\alpha-\frac1\alpha)\le\limsup_{\alpha\to0}(N_\alpha-\frac1\alpha)\le1.6230$; whether the limit exists, and its value, are open. At the exponents of Table 1, with the lower bound of (ii)
evaluated in outward ball arithmetic and the upper bound rounded up:

| $\alpha$ | 0.001 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|---|---|---|
| $N_\alpha\ge$ | 1000.6525 | 100.6448 | 20.6158 | 10.5913 | 5.5802 | 3.9544 | 2.9079 | 3.8369 | 8.0623 | 68.7271 |
| $N_\alpha\le$ | 1001.6243 | 101.6358 | 21.6886 | 11.7588 | 6.9155 | 5.4345 | 4.6230 | 5.4987 | 9.4980 | 70.0268 |
| $C_\alpha\le$ (Table 1) | 637.0246 | 64.0882 | 13.1840 | 6.8512 | 3.7432 | 2.7727 | 2.1935 | 2.6388 | 5.0067 | 42.2176 |

*Proof.* (v) For complex $f$ and a fixed output increment choose $\gamma$ with $e^{-i\gamma}(Tf(x)-Tf(y))\ge0$; this equals the
increment of $T\operatorname{Re}(e^{-i\gamma}f)$, and $[\operatorname{Re}(e^{-i\gamma}f)]_\alpha\le[f]_\alpha$. The converse inequality is restriction to real inputs.

(i) A pair containing $0$ has quotient $1$. Dilation and rotation bring two nonzero points to radii $e^{\pm x}$, $x\ge0$, and angular
separation $2t$, $0\le t\le\frac\pi2$; the squared quotient is then $2^{2-2\alpha}[\sinh^2(\alpha x)+\sin^2(nt)]/[\sinh^2x+\sin^2t]^\alpha$.
Since $\log\cosh$ is convex and vanishes at $0$, $\cosh(\alpha x)\le\cosh^\alpha x$, and since $(v+u)^\alpha-u^\alpha$ decreases in $u$,
$\sinh^2(\alpha x)\le(\sinh^2x+u)^\alpha-u^\alpha$ for $0\le u\le1$. With $u=\sin^2t$ and $L=\max_{[0,\pi/2]}\sin^2(nt)/\sin^{2\alpha}t\ge1$ the numerator
is at most $L(\sinh^2x+u)^\alpha$, so the quotient is at most $2^{1-\alpha}\sqrt L$, with equality at $x=0$ and a maximizing $t$. Replacing $t$
by $t'=\frac1n\arcsin|\sin nt|\le t$ does not decrease the ratio, so $L=Q_n^2$. For $n=2,3$, with $s=\sin t$ the objectives
$2s^{1-\alpha}\sqrt{1-s^2}$ and $3s^{1-\alpha}-4s^{3-\alpha}$ have unique critical points $s^2=\frac{1-\alpha}{2-\alpha}$ and $s^2=\frac{3(1-\alpha)}{4(3-\alpha)}$.
For the functional, subtracting the rotation of $f$ by $2t$ multiplies the Fourier coefficient by $1-e^{-2int}$, of modulus $2|\sin nt|$,
and the difference is at most $(2r\sin t)^\alpha[f]_\alpha$ pointwise; optimize over $t$.

(ii), upper bound. Let $|x-y|=h$, $f$ compact and smooth, and split $S=N_R+H_R$ at radius $R$ about the evaluation point. Circle
cancellation and (i) with $n=2$ give $|N_Rf(x)|,|N_Rf(y)|\le b_2R^\alpha[f]_\alpha/\alpha$. Differentiating $H_R$ in a direction $e=e^{i\beta}$
gives a bulk term with density $-e^{i(3\theta-\beta)}/(\pi r^3)$ on $|z|>R$, at most $2b_3R^{\alpha-1}[f]_\alpha/(1-\alpha)$ by (i) with $n=3$, and a circle
term with density $e^{2i\theta}\cos(\theta-\beta)=\frac12(e^{i(3\theta-\beta)}+e^{i(\theta+\beta)})$, at most $\frac{b_3+b_1}2R^{\alpha-1}[f]_\alpha$ by (i), or at most
$\frac{2^\alpha}\pi R^{\alpha-1}[f]_\alpha$ by antipodal subtraction. Integrating along the segment, $|Sf(x)-Sf(y)|\le[f]_\alpha(2b_2R^\alpha/\alpha+\mathcal B_\alpha hR^{\alpha-1})$;
the choice $R=\tilde s_\alpha h$ minimizes and gives the stated bound, which passes to all of $\dot C^\alpha$ as in Theorem 3.1(e), with $\chi_NP_Mf$ in place of the McShane extension.
Here $f(0)=0$, $P_M$ is the $1$-Lipschitz metric projection of $\mathbb C$ onto the disk $|w|\le M$, and $\chi_N(z)=\min\{1,(2-|z|/N)_+\}$. Then
$[\chi_N]_\alpha\le N^{-\alpha}$, so $[\chi_NP_Mf]_\alpha\le[f]_\alpha+MN^{-\alpha}$, and $\chi_NP_Mf=f$ on $|z|\le\min\{N,(M/[f]_\alpha)^{1/\alpha}\}$; let
$M\to\infty$ with $MN^{-\alpha}\to0$, mollify, and pass to the limit in the convergent increment formula.

(ii), lower bounds. *Cubic witness.* $f_\alpha=|z|^\alpha e^{-3i\arg z}$ has $[f_\alpha]_\alpha=2^{1-\alpha}Q_3$ by (i). With
$U=-|z|^{\alpha+2}e^{-3i\arg z}/((\alpha+2)^2-9)$ one has $-\Delta U=f_\alpha$ and, by $(\partial_x+i\partial_y)(r^be^{in\theta})=(b-n)r^{b-1}e^{i(n+1)\theta}$,
$\frac12(\partial_x+i\partial_y)^2U=\frac{\alpha+3}{2(1-\alpha)}|z|^\alpha e^{-i\arg z}$. Since $S$ has multiplier $-\frac12e^{2i\psi}$, this function and $Sf_\alpha$
solve the same Poisson equation, are both $\alpha$-Hölder, and so differ by a constant (Liouville). Its increment between $1$ and $-1$ is
$\frac{\alpha+3}{1-\alpha}$ at distance $2$; divide by $2^\alpha\cdot2^{1-\alpha}Q_3$. *Glued witness.* Let $x=\frac12$, $y=-\frac12$, $\tau(r)=\max(0,\min(r,\frac12-r))$,
$F(z)=b_2\tau(|z|)^\alpha e^{-2i\arg z}$, $f_{\rm in}=F(\cdot-x)-F(\cdot-y)$ and $f_{\rm out}(z)=b_3(|z|-1)_+^\alpha e^{-3i\arg z}$. The maps
$z\mapsto\tau(|z|)z/|z|$ and $z\mapsto(|z|-1)_+z/|z|$ are $1$-Lipschitz (their radial parts are $1$-Lipschitz and lie between $0$ and $|z|$, and
$|\Psi(z)-\Psi(w)|^2=(\rho(r)-\rho(s))^2+2\rho(r)\rho(s)(1-\cos(\theta-\phi))$), so each piece has seminorm at most $1$ by (i). For $z$ in a pole disk with
$u=\tau(|z\mp\frac12|)$ and $|w|>1$ with $v=|w|-1$, $|z-w|\ge u+v$ and $b_2u^\alpha+b_3v^\alpha\le2^{\alpha-1}(u^\alpha+v^\alpha)\le(u+v)^\alpha$ because $Q_n\ge1$;
the analogous estimate holds for $z$, $w$ in different pole disks. Hence $[f_{\rm in}+f_{\rm out}]_\alpha=1$. At each pole the phase of $F$ cancels that
of the kernel, so $Sf_{\rm in}(x)-Sf_{\rm in}(y)=2b_2\int_0^{1/2}\tau(r)^\alpha\frac{dr}r=2b_2\,2^{-\alpha}\mathcal A_\alpha=\mathcal A_\alpha/Q_2$; the cross terms vanish, because
on the support disk of $F(\cdot-x)$ the other-pole kernel is $\frac1{2\pi}\sum_{k\ge0}(k+1)(-\bar u)^k$ ($u=z-x$), uniformly convergent, and
$\bar u^ke^{-2i\arg u}$ has angular mode $-(k+2)\ne0$. On $|z|\ge1$ the increment density is $\sum_{k\ge0}(k+1)e^{i(2k+3)\theta}/(\pi4^kr^{2k+3})$, so only
$k=0$ survives against $e^{-3i\theta}$ and $Sf_{\rm out}(x)-Sf_{\rm out}(y)=2b_3\int_1^\infty(r-1)^\alpha r^{-2}dr=2b_3B(\alpha+1,1-\alpha)=\frac{2^\alpha\pi\alpha}{Q_3\sin\pi\alpha}$.
Both increments are positive and $|x-y|=1$. Truncating the exterior radial profile at a large radius and mollifying gives compact smooth
inputs with the same limit.

(iii) By Theorem 3.1(d) with $R=h$ and $b_\alpha\le\frac{2^{\alpha+1}}{3\pi}$, $C_\alpha\le\frac{2a_2}\alpha+\frac{2a_3}{1-\alpha}+\frac{2^{\alpha+1}}{3\pi}$, and Theorem 3.1 with
$b_\alpha$ replaced by $\frac{2^{\alpha+1}}{3\pi}$ gives an optimized bound $U(\alpha)$. Hölder interpolation in the integrals $a_n$ gives
$a_2,a_3\le\frac1\pi$, and $a_3\le\frac14$ for $\alpha\ge\frac34$ (from $a_3(\frac34)^4\le a_3(0)a_3(1)^3<\frac1{256}$); also $Q_n\le n^\alpha$. For $0<\alpha\le\frac1{10}$ the
first term of the glued bound gives $\alpha N_\alpha\ge2^{-\alpha}/Q_2\ge4^{-\alpha}>\frac45$, while $\alpha C_\alpha\le\frac2\pi+\frac2{9\pi}+\frac2{15\pi}<\frac45$. For
$\frac9{10}\le\alpha<1$ the cubic bound gives $(1-\alpha)N_\alpha\ge\frac{\alpha+3}{2Q_3}\ge\frac{13}{20}$, while $(1-\alpha)C_\alpha\le\frac12+\frac2{9\pi}+\frac2{15\pi}<\frac{13}{20}$. On
$[\frac1{10},\frac9{10}]$, $42$ rational closed intervals are checked in outward ball arithmetic, each with the glued or the cubic bound
strictly above $U$; the integral $\int_0^{1/2}\frac{t^\alpha}{1-t}dt$ in $\mathcal A_\alpha$ is replaced by a positive partial sum of its expansion $\sum_k2^{-\alpha-k-1}/(\alpha+k+1)$, and $a_3$ is enclosed by a positive
binomial series with a proved tail. The cover was replayed independently with a separately derived series.

(iv) As $\alpha\to0$: $Q_2,Q_3\to1$, $b_n\to\frac12$, $\mathcal A_\alpha=\frac1\alpha+O(\alpha)$ and $Q_2=1+\frac{\log2}2\alpha+O(\alpha^2)$, so the glued bound is
$\frac1\alpha-\frac{\log2}2+1+o(1)$; $\tilde s_\alpha\to1+\frac1\pi$, so $\alpha$ times the upper bound tends to $1$. As $\alpha\to1$: $Q_3\to3$ and $Q_2\to2$, so
$(1-\alpha)$ times the cubic bound tends to $\frac46$, and $(1-\alpha)\mathcal B_\alpha\to\frac23$, $\tilde s_\alpha\to\frac23$, so $(1-\alpha)$ times the upper bound tends
to $2b_2(1)\cdot\frac23=\frac23$. $\square$

Weaker explicit witnesses, a tent cusp with $[\cdot]_\alpha\le2^\alpha$ giving $16^{-\alpha}(\frac1\alpha-\frac1{18})$ and the cubic mode with
the seminorm bound $2^{1-\alpha}3^\alpha$, give smaller lower bounds than (ii).

**Theorem 1.5 (continuity in the exponent).** Let $0<a\le b<1$, $0<\epsilon<\frac12$ and $R>1$, and put

$$\bar E=\frac{2\epsilon^a}{\pi a}+\frac{(1+2\epsilon)^b\epsilon^2}{2(1-\epsilon)^2}+\frac{2^bR^{b-1}}{(1-b)(1-1/(4R^2))^2},\qquad M=\frac2\pi\log\frac{R+\frac12}\epsilon,\qquad
\Lambda=\max\Big(\frac1{ea},\,(2R)^b\log(2R)\Big).$$

Then for $\alpha,\beta\in[a,b]$

$$|C_\alpha-C_\beta|\le2\bar E+M\Lambda|\alpha-\beta|,\qquad |D_\alpha-D_\beta|\le2\bar E+\big(M+\tfrac12\big)\Lambda|\alpha-\beta| .$$

Hence $\alpha\mapsto C_\alpha$ and $\alpha\mapsto D_\alpha$ are continuous on $(0,1)$. Every certified strict inequality $C_{\alpha_0}<D_{\alpha_0}$
holds on an open interval around $\alpha_0$: if $U\ge C_{\alpha_0}$, $V\le D_{\alpha_0}$, $g=V-U>0$, $a<\alpha_0<b$ and $4\bar E<g$, then
$C_\alpha<D_\alpha$ for every $\alpha\in[a,b]$ with $|\alpha-\alpha_0|<(g-4\bar E)/\big((2M+\frac12)\Lambda\big)$.

*Proof.* Write $\phi$ for the phase $b$ of Theorem 1.3, since $b$ is an exponent here. The measures $\mu_\phi$ and $\mu_\phi^D$ of Theorem 1.3 do not depend on $\alpha$ and are supported in the closed disk of radius $R$.
The integral of $|K_\phi|$ over the annulus $\epsilon\le|z-p|\le R+\frac12$ about a pole $p$ is $M$, because $\int_0^{2\pi}|\cos(2\theta-2\phi)|\,d\theta=4$;
so $|\mu_\phi|(\mathbb R^2)\le2M$, and since $\mu_\phi$ has mass zero each of its Jordan parts has mass at most $M$. The atoms of $\mu_\phi^D$ add $\frac12$
to each part. For $0<r\le1$ and $t\in[a,b]$, $|\partial_tr^t|=r^t\log\frac1r\le r^a\log\frac1r\le\frac1{ea}$, and for $1\le r\le2R$, $|\partial_tr^t|\le(2R)^b\log(2R)$,
so $|r^\alpha-r^\beta|\le\Lambda|\alpha-\beta|$ for every distance $0\le r\le2R$ between support points. All couplings of the two Jordan parts
have the same total mass, so the two transport costs of any coupling differ by at most $M\Lambda|\alpha-\beta|$, and
$|W_\alpha(\mu_\phi)-W_\beta(\mu_\phi)|\le M\Lambda|\alpha-\beta|$, uniformly in $\phi$; likewise with $M+\frac12$ for $\mu_\phi^D$. On $[a,b]$ the error $E$ of
Theorem 1.3 is at most $\bar E$, because $a_2(\alpha)\le\frac1\pi$ (the function $2+t-2^{1+t/2}$ is concave on $[0,1]$, vanishes at $0$ and is
positive at $1$). Theorem 1.3 and $|\sup_\phi A_\phi-\sup_\phi B_\phi|\le\sup_\phi|A_\phi-B_\phi|$ give the two inequalities. Given a tolerance, choose
$\epsilon$ and $R$ with $2\bar E$ below half of it and then $\alpha$ close to $\beta$; this proves continuity. For the last statement,
$D_\alpha-C_\alpha\ge g-4\bar E-(2M+\frac12)\Lambda|\alpha-\alpha_0|$. $\square$

With cutoffs for which $4\bar E$ is below the certified gaps of Table 1, $M$ and $\Lambda$ are large and the resulting intervals are very
short. With $\epsilon=2^{-k}$, $R=2^m$ and an interval $[a,b]$ around $\alpha_0$, all exact, the inequality at the end of the proof, applied to the
certified endpoints $U$ and $V$ behind Table 1 (ten decimals), gives $C_\alpha<D_\alpha$ for $|\alpha-\alpha_0|\le r$ with the radii $r$ below; the last column is a lower bound for
$g-4\bar E-(2M+\frac12)\Lambda r$, hence for $D_\alpha-C_\alpha$ on the whole interval. At $\alpha_0=\frac12$, for example, $k=15$, $m=18$ and
$[a,b]=[\frac{99}{200},\frac{101}{200}]$. The checks use directed 320-bit ball arithmetic, with an independent 640-bit replay
(the accompanying artifacts list every $k$, $m$, $a$, $b$).

| $\alpha_0$ | $r$ | $k$ | $m$ | gap on the interval $\ge$ |
|---|---:|---:|---:|---:|
| $1/1000$ | $10^{-9}$ | 16183 | 7 | 0.2340 |
| $1/100$ | $10^{-7}$ | 1297 | 8 | 0.2259 |
| $1/20$ | $10^{-5}$ | 218 | 8 | 0.1639 |
| $1/10$ | $10^{-5}$ | 102 | 9 | 0.1386 |
| $1/5$ | $10^{-6}$ | 45 | 10 | 0.1633 |
| $3/10$ | $10^{-6}$ | 28 | 12 | 0.1901 |
| $1/2$ | $10^{-8}$ | 15 | 18 | 0.2040 |
| $3/4$ | $10^{-15}$ | 10 | 41 | 0.2085 |
| $9/10$ | $10^{-38}$ | 10 | 117 | 0.1952 |
| $99/100$ | $10^{-474}$ | 10 | 1562 | 0.1313 |

These are sufficient intervals only, not the extent of the separation set. Near $\alpha=1$ the radii are tiny because $\Lambda$
grows like $(2R)^b\log(2R)$ while $\bar E$ needs $R^{b-1}$ small.

A comparison of transport costs gives much wider intervals. Let $\mu$ be a finite signed measure of mass zero whose Jordan parts
have mass at most $m$ and whose support has diameter at most $d>0$, and let $W_t$ be its transport cost for the cost $r^t$. For
$0<s<t<1$, $d^{s-t}W_t\le W_s\le m^{1-s/t}W_t^{s/t}$: the first because $r^t\le d^{t-s}r^s$ for $0\le r\le d$, the second by
Jensen's inequality for the concave map $u\mapsto u^{s/t}$ on a coupling divided by its mass (the zero measure is immediate). Apply this phase by phase to
$\mu_\phi$ (with $m=M$) and $\mu_\phi^D$ (with $m=M+\frac12$) from the proof of Theorem 1.5, with $d=2R$, and take suprema over
$\phi$. Put $U_0=U+\bar E$, $V_0=V-\bar E>0$, $H_C=\max(\log2R,\frac1{\alpha_0}\log\frac M{U_0},0)$ and
$H_D=\max(\log2R,\frac1{\alpha_0}\log\frac{M+1/2}{V_0},0)$. For $\alpha\ge\alpha_0$ the first inequality bounds the cost of $\mu_\phi$
from above and the second, rearranged, bounds the cost of $\mu_\phi^D$ from below; for $\alpha\le\alpha_0$ the roles are exchanged.
With the truncation errors of Theorem 1.3 this gives, whenever $[\alpha_0-\rho,\alpha_0+\rho]\subset[a,b]$,

$$D_\alpha-C_\alpha\ge V_0e^{-H_D\rho}-U_0e^{H_C\rho}-2\bar E\qquad(|\alpha-\alpha_0|\le\rho),$$

with no factor $(2R)^b$ multiplying $\rho$. With the cutoffs and intervals $[a,b]$ listed in the accompanying artifacts
(320-bit ball arithmetic with an independent 640-bit replay), the
right side is positive for the radii $5\cdot10^{-8}$, $5\cdot10^{-6}$, $10^{-4}$, $5\cdot10^{-4}$, $0.002$, $0.003$, $0.002$, $0.001$,
$2\cdot10^{-4}$ and $10^{-6}$ at the ten exponents in the order of Table 1, with lower bounds $0.0853$, $0.0893$, $0.0737$, $0.0163$,
$0.0225$, $0.0387$, $0.0846$, $0.0518$, $0.0369$ and $0.0503$ for $D_\alpha-C_\alpha$ on these closed intervals. These are again
sufficient intervals only. Evaluating the two sides separately, that is, using
$\min\big(V_0e^{-\rho\log2R}-U_0e^{h_C\rho},\,V_0e^{-h_D\rho}-U_0e^{\rho\log2R}\big)-2\bar E$ with $h_C=\max(0,\frac1{\alpha_0}\log\frac M{U_0})$ and
$h_D=\max(0,\frac1{\alpha_0}\log\frac{M+1/2}{V_0})$, which decreases in $\rho$, gives the radii $10^{-7}$, $10^{-5}$, $2\cdot10^{-4}$,
$8\cdot10^{-4}$, $0.002$, $0.003$, $0.005$, $0.002$, $4\cdot10^{-4}$ and $3\cdot10^{-6}$, with corresponding gap bounds ($0.0849$, $0.0852$, $0.0571$, $0.0047$,
$0.0346$, $0.0631$, $0.0094$, $0.0346$, $0.0306$, $0.0041$; see the accompanying artifacts).

**Theorem 1.6 (extremal functions).** Let $0<\alpha<1$. There are a real function $f$ on $\mathbb R^2$ with $[f]_\alpha=1$ and points
$z\ne w$ with $|z-w|=1$ such that $|T_{xx}f(z)-T_{xx}f(w)|=C_\alpha$, with the increment of item 4 extended to the homogeneous space as in
the paragraph on the extension to $\dot C^\alpha$ in Section 1. The same holds for $T_{xy}$ with $C_\alpha$ and for $R_1^2$ with $D_\alpha$. The function can be chosen odd about the midpoint of
$z$ and $w$. Smoothness, compact support or uniqueness of $f$, and the direction of $z-w$, are not asserted.

*Proof.* Let $B=\{f:f(0)=0,\ [f]_\alpha\le1\}$. Since $|f(z)|\le|z|^\alpha$ on $B$, the Arzelà-Ascoli theorem on the disks of integer radius
and a diagonal sequence make $B$ compact for local uniform convergence, which is a metrizable topology. For fixed $\epsilon$ and $R$
the functions $(f,b)\mapsto\int f\,d\mu_b$ and $\int f\,d\mu_b^D$ are continuous on $B\times[0,\pi]$, since the measures have compact support,
finite variation and a density linear in $\cos2b$, $\sin2b$. The proof of Theorem 1.3 bounds the difference between the increment
functional and $\int f\,d\mu_b$ (respectively $\int f\,d\mu_b^D$) by the error $E$ of Theorem 1.3 for each $f\in B$, uniformly in $b$. As $E\to0$ the increment
functionals are uniform limits of continuous functions, hence continuous on the compact set $B\times[0,\pi]$, and their absolute values
attain their maxima, which are $C_\alpha$ and $D_\alpha$ by item 4. A maximizer has $[f]_\alpha=1$, since the maxima are positive and
$f/[f]_\alpha$ would otherwise give a larger value. The density $\nu_b$ and the pair of atoms are odd under $z\mapsto-z$, so
$\frac12(f(z)-f(-z))$ gives the same value and its seminorm is at most that of $f$. Rotating the plane turns the maximizing phase
into the kernel of $T_{xx}$, which gives $z$ and $w$; $T_{xy}$ is $T_{xx}$ rotated by $\frac\pi4$, and $R_1^2$ is treated in the same way with
$\mu_b^D$. $\square$

## 2. Literature

Only statements read in the primary sources are reported; sources were saved and read during the project.

1. **Exact Hölder constant of the conjugate function (periodic).** V. F. Babenko, *Sharp estimates for norms of
   functions from conjugate classes in metrics C and L*, arXiv:1402.0829 (English version of a 1973 paper). Theorem 1(2):
   for a concave modulus of continuity $\omega$ with $\int_0\omega(t)t^{-1}dt<\infty$ and the conjugate function with
   kernel $-(2\pi)^{-1}\cot((t-x)/2)$,
   $\sup_{f\in H^\omega}\max_x|\tilde f(x+h)-\tilde f(x)|=\frac2\pi\int_0^{h/2}\frac{\sin(h/2)}{\cos u-\cos(h/2)}\,\omega(\rho(u)-u)\,du$,
   with $\rho$ defined by matching positive and negative kernel masses ($\tan(\rho/2)\tan(u/2)=\tan^2(h/4)$). This is an exact
   result for a one-dimensional operator.
2. **Real-line Hilbert transform.** From the same structure we proved independently (accompanying artifacts) that the
   Hilbert transform $Hf=\frac1\pi\mathrm{p.v.}\frac1t*f$ satisfies $\|H\|_{\dot C^\alpha(\mathbb R)\to\dot C^\alpha(\mathbb R)}=\frac{2^{1-\alpha}}{\pi}B\big(\tfrac{1-\alpha}2,\alpha\big)$,
   with an explicit extremizer. For $\omega(t)=t^\alpha$, Babenko's theorem gives the same constant
   $\frac{2^{1-\alpha}}\pi B(\frac{1-\alpha}2,\alpha)=\Gamma(\frac\alpha2)\Gamma(\frac{1-\alpha}2)/\pi^{3/2}$ as the exact norm of the periodic conjugate
   function for the angular geodesic seminorm $\sup_{0<h\le\pi}|f(x+h)-f(x)|/h^\alpha$, and also for the chordal seminorm
   $\sup|f(x)-f(y)|/|e^{ix}-e^{iy}|^\alpha$, for real and complex inputs (corollaries of
   Theorem 1(2) with the moduli $h^\alpha$ and $(2\sin\frac h2)^\alpha$, a theorem whose proof is announced but not given in the source;
   we also proved both constants directly, by an explicit pairing of the two lobes of the difference kernel for the upper
   bound and by rescaled real-line inputs for the lower bound, without the announced theorem, in the accompanying artifacts). The two seminorms differ, but the two operator constants agree. This is a one-dimensional analogue only; we use it for comparison: it equals
   $\frac2{\pi\alpha}+O(1)$ as $\alpha\to0$ and $\frac2{\pi(1-\alpha)}+O(1)$ as $\alpha\to1$.
3. **Beurling transform on domains (qualitative).** J. Mateu, J. Orobitg, J. Verdera, *Extra cancellation of even
   Calderón-Zygmund operators and quasiconformal mappings*, J. Math. Pures Appl. 91 (2009) 402-431, arXiv:0802.1185. Main
   Lemma: for bounded $C^{1+\varepsilon}$ domains $\Omega$ and even homogeneous $C^1$ kernels with zero mean,
   $\|T(f\chi_\Omega)\|_{\mathrm{Lip}(\varepsilon,\Omega)}\le C\|T\|_{CZ}\|f\|_{\mathrm{Lip}(\varepsilon,\Omega)}$ with
   $C=C(n,\varepsilon,\Omega)$ not evaluated and an inhomogeneous norm. E. Doubtsov, A. V. Vasin, arXiv:1604.07670:
   restricted Beurling transforms on Campanato spaces of $C^{1,\omega}$ domains, modulus transformation
   $\tilde\omega(x)=\int_0^x\omega(t)t^{-1}dt+x\int_x^1\omega(t)t^{-2}dt$ (for $\omega=t^\alpha$:
   $x^\alpha/\alpha+(x^\alpha-x)/(1-\alpha)$, the same $1/\alpha$ and $1/(1-\alpha)$ endpoint orders as here), constants
   unspecified. V. Cruz, X. Tolsa, arXiv:1201.5385, and X. Tolsa, arXiv:1201.5403: Besov/Sobolev regularity of $B\chi_\Omega$
   on Lipschitz domains; sharp in the regularity exponents, no numerical constants.
4. **General Calderón-Zygmund operators on Lipschitz spaces.** J. García-Cuerva, A. E. Gatto, *Lipschitz spaces and
   Calderón-Zygmund operators associated to non-doubling measures*, arXiv:math/0212289. For a Radon measure with
   $\mu(B(x,r))\le Cr^n$, Definition 3.2 requires the operator to be bounded on $L^2(\mu)$ and represented off the support
   by a standard kernel with size bound and Hölder regularity of exponent $\epsilon$; Definition 3.4 extends it to Lipschitz
   functions modulo constants. Their Theorem 3.6: for $0<\alpha<\epsilon\le1$, such $T$ is bounded on $\mathrm{Lip}(\alpha,\mu)$ if
   and only if $T(1)=0$ in that quotient space. No numerical norm. A. González-Pérez, *Hölder classes via semigroups and
   Riesz transforms*, Math. Z. 301 (2022) 3245-3284: qualitative Hölder boundedness of first-order Riesz transforms in
   semigroup and manifold settings, with seminorm equivalences and constants not evaluated.
   **Exact one-dimensional transport lemma.** V. Babenko, V. Babenko, O. Kovalenko, arXiv:2006.14581, Lemma 8 (the
   Korneichuk-Stechkin lemma): for bounded positive weights $\psi_1$ on $[a,a']$ and $\psi_2$ on $[b',b]$ ($a<a'\le b'<b$)
   of equal mass and the decreasing mass-matching map $\rho$ defined by $\int_a^s\psi_1=\int_{\rho(s)}^b\psi_2$, the difference of
   the weighted integrals of a function with modulus of continuity $\omega$ is at most $\int_a^{a'}\psi_1(s)\omega(\rho(s)-s)ds$,
   with equality for concave $\omega$. This is the one-dimensional mechanism behind Babenko's theorem; our angular lemma
   (Theorem 3.1(a)) is a circular analogue proved directly.
5. **Schauder estimates.** P. Fife, Pacific J. Math. 13 (1963) 511-550, Theorem 2.1: partial Hölder estimates for integral
   operators, constant not evaluated. L. Marino, S. Menozzi, E. Priola, arXiv:2107.06012: "sharp constants" there means
   preservation of a given Schauder constant under perturbation, not its value. J. Sauer, S. A. Smith, arXiv:2412.01486:
   Schauder estimates for germs with non-explicit constants. X.-J. Wang, *Schauder estimates for elliptic and parabolic
   equations*, Chinese Ann. Math. B 27 (2006) 637-642, Theorem 1.1 and (1.3): for a $C^2$ solution of $\Delta u=f$ in the
   unit ball, a local Hessian estimate whose Hölder part carries the factor $\frac1{\alpha(1-\alpha)}$, times a dimensional
   constant $C_n$ that is not evaluated. This has the same endpoint orders as $F(\alpha)$, but no numerical constant.
6. **Negative result of the search.** No published exact value, and no published explicit numerical bound, for the
   $\dot C^\alpha(\mathbb R^2)$ operator norm of $T_{xx}$, $T_{xy}$, $R_1^2$ or the Beurling transform was found. This is
   the outcome of a search, not a claim that none exists.

## 3. The explicit upper bound

**Theorem 3.1.** Let $0<\alpha<1$ and let $a_n(\alpha)$, $b_\alpha$, $B_\alpha$, $s_\alpha$, $F(\alpha)$ be as in Section 0. For every
real $f\in\dot C^\alpha(\mathbb R^2)$, with the operators defined modulo constants as in Section 1,

$$[T_{xx}f]_\alpha\le F(\alpha)[f]_\alpha,\qquad[T_{xy}f]_\alpha\le F(\alpha)[f]_\alpha,\qquad
[R_1^2f]_\alpha\le\big(F(\alpha)+\tfrac12\big)[f]_\alpha .$$

The same holds for complex $f$ (apply the real statement to $\operatorname{Re}(e^{i\phi}f)$ with the phase $\phi$ chosen for
each output increment). Equivalently $C_\alpha\le F(\alpha)$ and $D_\alpha\le F(\alpha)+\frac12$; Theorem 3.2 improves the
latter to $D_\alpha\le G(\alpha)$. Moreover

$$F(\alpha)=\frac2{\pi\alpha}+\frac2\pi\Big(\log\frac43+\frac{\log2}2+\frac12\Big)+O(\alpha)=\frac2{\pi\alpha}+0.7220895\ldots+O(\alpha)\quad(\alpha\to0),$$

$$\lim_{\alpha\to1}(1-\alpha)F(\alpha)=2a_3(1)=\frac{3\sqrt3}{4\pi}=0.41350\ldots$$

(For the first expansion: $a_n(\alpha)=\frac1\pi+O(\alpha)$, $a_2=\frac1\pi(1+\alpha(\frac{\log2}2-\frac12))+O(\alpha^2)$,
$s_\alpha\to\frac43$. For the second: $(1-\alpha)B_\alpha\to2a_3(1)$, $s_\alpha\to a_3(1)/a_2(1)$, and
$a_3(1)=\frac3\pi\int_0^{\pi/6}\sin3t\,2\sin t\,dt=\frac{3\sqrt3}{8\pi}$.) Both leading coefficients are sharp (Sections 5 and 6).

*Proof.* **(a) Exact angular lemma.** For $r>0$, $n\ge1$ and any phase $\gamma$,

$$\Big|\frac1{2\pi}\int_0^{2\pi}\cos(n\theta-\gamma)f(r\cos\theta,r\sin\theta)\,d\theta\Big|\le a_n(\alpha)\,r^\alpha[f]_\alpha ,$$

and the constant is attained. After a rotation $\gamma=0$. Split each positive lobe of $\cos n\theta$ into two halves and
reflect each half across its adjacent zero ray onto the neighbouring negative half-lobe. If $t\in[0,\pi/(2n)]$ is the
angular distance to that ray, both densities have modulus $\sin(nt)$ and the paired points are at distance $2r\sin t$, so the
pair contributes at most $\frac{[f]_\alpha r^\alpha}{2\pi}\int_0^{\pi/(2n)}\sin(nt)(2\sin t)^\alpha dt$. Summing over the $2n$
pairs gives the bound. Equality holds for $f=p_\alpha\circ u_n$, where $u_n=\operatorname{sign}(\cos(n\arg z))\operatorname{dist}(z,Z_n)$,
$Z_n$ the zero lines of $\cos n\theta$, and $p_\alpha(s)=2^{\alpha-1}\operatorname{sign}(s)|s|^\alpha$: $u_n$ is 1-Lipschitz (a
segment joining points of opposite sign crosses $Z_n$) and $p_\alpha$ has Hölder seminorm 1 on $\mathbb R$ because
$2^{\alpha-1}(a^\alpha+b^\alpha)\le(a+b)^\alpha$. For $n=2$ the substitution $v=\sin t$ gives $a_2=2^{1+\alpha/2}/(\pi(\alpha+2))$.

**(b) Near and far parts.** For $f\in C_c^\infty$ and $R>0$, $T_{xx}f=N_Rf+H_Rf$ with
$N_Rf(x)=\int_{|z|<R}K_{xx}(z)(f(x-z)-f(x))dz$ and $H_Rf(x)=\int_{|z|\ge R}K_{xx}(z)f(x-z)dz$. By (a) with $n=2$ on each
circle, $|N_Rf(x)|\le\frac{a_2(\alpha)}{\alpha}R^\alpha[f]_\alpha$.

**(c) Derivative of the far part.** For a unit vector $e=(\cos\beta,\sin\beta)$, $\partial_eK_{xx}=-\cos(3\theta-\beta)/(\pi r^3)$, and
$\partial_e(\mathbf 1_{|z|\ge R}K_{xx})=\mathbf 1_{|z|>R}\partial_eK_{xx}+\delta(|z|-R)\,(e\cdot z/|z|)K_{xx}$. By (a) with $n=3$ the bulk
term is at most $2a_3\,[f]_\alpha\int_R^\infty r^{\alpha-2}dr=\frac{2a_3}{1-\alpha}R^{\alpha-1}[f]_\alpha$. The sphere term has angular
density $\cos2\theta\cos(\theta-\beta)=\frac12\cos(3\theta-\beta)+\frac12\cos(\theta+\beta)$, giving the bound
$\frac{a_3+a_1}2R^{\alpha-1}[f]_\alpha$; alternatively it is odd under $\theta\mapsto\theta+\pi$, and antipodal pairing gives
$2^{\alpha-1}\frac1{2\pi}I(\beta)R^{\alpha-1}[f]_\alpha$ with $I(\beta)=\int_0^{2\pi}|\cos2\theta\cos(\theta-\beta)|d\theta$. On $[0,\pi/4]$,
$I''+I=4\cos2\beta$, $I(0)=4(2\sqrt2-1)/3$, $I'(0)=0$, so $I(\beta)=(8\sqrt2\cos\beta-4\cos2\beta)/3\le I(\pi/4)=8/3$ and this
bound is $\frac{2^{\alpha+1}}{3\pi}R^{\alpha-1}[f]_\alpha$. Hence $|\partial_eH_Rf(x)|\le B_\alpha R^{\alpha-1}[f]_\alpha$ uniformly in $x$
and $e$. All angular densities used have mean zero, so constants in $f$ play no role.

**(d) Optimization.** For $h=|x-y|$, integrating (c) along the segment and using (b) at both points,
$|T_{xx}f(x)-T_{xx}f(y)|\le[f]_\alpha\big(\frac{2a_2}{\alpha}R^\alpha+B_\alpha hR^{\alpha-1}\big)$. With $R=sh$, the function
$s\mapsto\frac{2a_2}\alpha s^\alpha+B_\alpha s^{\alpha-1}$ has derivative of the sign of $2a_2s-(1-\alpha)B_\alpha$, so its unique
minimizer is $s_\alpha$ and its minimum is $F(\alpha)$.

**(e) Extension.** Rotation gives the $T_{xy}$ bound and $R_1^2=T_{xx}-\frac12I$ gives $F+\frac12$. For general $f\in\dot C^\alpha$,
normalize $f(0)=0$, use the McShane extension of $f|_{\overline B_M}\cup 0|_{\mathbb R^2\setminus B_{2M}}$ in the metric
$|x-y|^\alpha$ (seminorm preserved), mollify, and pass to the limit in the absolutely convergent increment formula of
Section 1 (majorants $r^{\alpha-2}$ near the singularities and $r^{\alpha-3}$ at infinity). $\square$

**Optimizations used in Theorem 3.1** (task item 5). (i) The angular lemma is exact, so no loss occurs on single circles.
(ii) The sphere term uses the smaller of a harmonic-splitting bound and an antipodal-pairing bound; the pairing bound
is smaller for small $\alpha$ (limits $\frac2{3\pi}$ against $\frac1\pi$) and the harmonic bound is smaller near $\alpha=1$
(at $\alpha=0.9$: $0.3451$ against $0.3960$). (iii) The splitting radius $R=s_\alpha h$ is optimized exactly.
The remaining losses are: the two near parts are bounded separately (each by its own extremizer, which are not
compatible with a single far-field extremizer), and the bulk and sphere terms of the far derivative are bounded
separately along the whole segment.

**Theorem 3.2 (projection pairing for $R_1^2$).** Let $0<\alpha<1$ and

$$A_\alpha=\frac2\pi\int_0^{\pi/4}\sin^{\alpha+1}(2t)\,dt=\frac{\Gamma(\frac{\alpha+2}2)}{2\sqrt\pi\,\Gamma(\frac{\alpha+3}2)}=2^{-\alpha}a_1(\alpha).$$

For every real $f\in\dot C^\alpha(\mathbb R^2)$,

$$[R_1^2f]_\alpha\le G(\alpha)[f]_\alpha,\qquad G(\alpha)=F(\alpha)\Big(\frac{A_\alpha}{a_2(\alpha)}\Big)^{1-\alpha}+\frac12 .$$

Since $\sin2t<2\sin t$ on $(0,\pi/4)$, $A_\alpha<a_2(\alpha)$ and $G(\alpha)<F(\alpha)+\frac12$ for every $\alpha$. As
$\alpha\to0$, $G(\alpha)=\frac2{\pi\alpha}+\frac12+\frac2\pi\log\frac83+O(\alpha)=\frac2{\pi\alpha}+1.1244152\ldots+O(\alpha)$, against
$F(\alpha)+\frac12=\frac2{\pi\alpha}+1.2220895\ldots+O(\alpha)$.

*Proof.* Write the local operator of radius $R$ as $N_Rf(z)=\int_{|w|<R}K_{xx}(w)(f(z-w)-f(z))\,dw$. Split each of the two
positive lobes of $\cos2\theta$ into two half-lobes. In a half-lobe, let $t\in(0,\pi/4)$ be the angle to the
neighbouring zero ray, let $v_+(t)$ be the unit vector at angle $t$ inside the positive half-lobe, and let $v_-(t)$
be its mirror image across that ray. Both angular densities have modulus $\sin2t/(2\pi)$. Put $\lambda(t)=\cos2t$.
Then $\lambda v_-$ is the orthogonal projection of $v_+$ onto the ray of $v_-$, so $|v_+-\lambda v_-|=\sin2t$. Define

$$P_Rf(z)=\sum_{j=1}^4\frac1{2\pi}\int_0^{\pi/4}\sin2t\int_0^R\frac{f(z-rv_{+,j})-f(z-\lambda rv_{-,j})}r\,dr\,dt,\qquad
Q_Rf(z)=\sum_{j=1}^4\frac1{2\pi}\int_0^{\pi/4}\sin2t\int_{\lambda R}^R\frac{f(z-rv_{-,j})}r\,dr\,dt .$$

For fixed $t$ and a lower cutoff $\varepsilon$, the substitution $u=\lambda r$ gives
$\int_\varepsilon^R\frac{f(z-\lambda rv_-)-f(z-rv_-)}r\,dr=\int_{\lambda\varepsilon}^\varepsilon\frac{f(z-uv_-)}u\,du-\int_{\lambda R}^R\frac{f(z-uv_-)}u\,du$.
As $\varepsilon\to0$ the first term tends to $\log(1/\lambda)f(z)$, with error at most $[f]_\alpha\varepsilon^\alpha/\alpha$, and
$\sin 2t\log(1/\cos2t)$ is integrable. Hence

$$N_R=P_R+\kappa_Q I-Q_R,\qquad \kappa_Q=\frac2\pi\int_0^{\pi/4}\sin2t\log\frac1{\cos2t}\,dt=\frac1\pi .$$

$Q_R$ is convolution with a positive measure of total mass $\kappa_Q$. The projection distances give
$|P_Rf(z)|\le\frac{A_\alpha}\alpha R^\alpha[f]_\alpha$ (the same computation as in Theorem 3.1(a), with $2r\sin t$ replaced by $r\sin2t$).
With $H_R=T_{xx}-N_R$ as in Theorem 3.1(b),

$$R_1^2=T_{xx}-\tfrac12I=P_R+H_R-\big(Q_R+(\tfrac12-\kappa_Q)I\big).$$

Because $\kappa_Q=1/\pi<1/2$, the last operator is convolution with a positive measure of mass $\frac12$, so it changes
every increment by at most $\frac12[f]_\alpha|x-y|^\alpha$. With Theorem 3.1(c) for $H_R$,
$|R_1^2f(x)-R_1^2f(y)|\le[f]_\alpha\big(\frac{2A_\alpha}\alpha R^\alpha+B_\alpha hR^{\alpha-1}+\frac12h^\alpha\big)$ for $h=|x-y|$. Minimizing over
$R=sh$ as in Theorem 3.1(d), with $a_2$ replaced by $A_\alpha$, gives
$\frac{2A_\alpha(s^D_\alpha)^\alpha}{\alpha(1-\alpha)}$ with $s^D_\alpha=\frac{(1-\alpha)B_\alpha}{2A_\alpha}$, and this equals
$F(\alpha)(A_\alpha/a_2(\alpha))^{1-\alpha}$. The extension to all of $\dot C^\alpha$ is as in Theorem 3.1(e). The Gamma form of
$A_\alpha$ is the Beta integral $\int_0^{\pi/2}\sin^{\alpha+1}u\,du$. For the expansion: $A_0=a_2(0)=\frac1\pi$,
$A_0'=\frac{\log2-1}\pi$ and $a_2'(0)=\frac{\log2-1}{2\pi}$, so $(A_\alpha/a_2)^{1-\alpha}=1+\frac{\log2-1}2\alpha+O(\alpha^2)$. $\square$

**Theorem 3.3 (midpoint split).** Let $x=\frac12$, $y=-\frac12$ in complex notation, $G(w)=\frac w{\pi(w^2-1/4)^2}$,
$E=B_1(0)\setminus(B_{1/2}(x)\cup B_{1/2}(y))$, and for $0\le\phi\le\pi/2$

$$M_\alpha(\phi)=\frac12\int_E|\operatorname{Re}(e^{i\phi}G(w))|(2|w|)^\alpha\,dA(w)
+\int_{B_{1/2}(x)}\Big|\operatorname{Re}\frac{e^{i\phi}}{2\pi(w+\frac12)^2}\Big|(2|w|)^\alpha\,dA(w),$$

$$H_\alpha=\frac{2a_3(\alpha)}{1-\alpha}+\frac2\pi\sum_{n=1}^\infty\frac{(n+1)4^{-n}}{2n+1-\alpha}\Big[\frac{2(2n+3)\cos(\pi/(4n+6))}{(2n+3)^2-1}\Big]^\alpha .$$

For every integer $m\ge1$,

$$C_\alpha\le U_m(\alpha)=\frac{2^{1-\alpha}a_2(\alpha)}\alpha+H_\alpha+\sec\frac\pi{4m}\max_{0\le j\le m}M_\alpha\Big(\frac{j\pi}{2m}\Big),$$

$$D_\alpha\le U^D_m(\alpha)=\frac{2^{1-\alpha}A_\alpha}\alpha+\frac12+H_\alpha+\sec\frac\pi{4m}\max_{0\le j\le m}M_\alpha\Big(\frac{j\pi}{2m}\Big).$$

*Proof.* By Section 1 (identity 4) it suffices to bound $\int\nu_\phi f$ for the increment density $\nu_\phi=\operatorname{Re}(e^{i\phi}G)$,
uniformly in the phase $\phi$, for $[f]_\alpha\le1$. Write $K_\phi(w)=\operatorname{Re}(e^{i\phi}/(2\pi w^2))$. Subtract the two local
convolutions of radius $\frac12$ centred at $x$ and $y$. By the angular lemma each costs at most $a_2(\alpha)2^{-\alpha}/\alpha$. For $R_1^2$,
use Theorem 3.2 instead: the two paired parts cost $2A_\alpha2^{-\alpha}/\alpha$ together, and the positive remainder with the
identity term costs at most $\frac12$. The remaining density $m_\phi$ equals $-K_\phi(w-y)$ on $B_{1/2}(x)$, $K_\phi(w-x)$ on
$B_{1/2}(y)$, and $\nu_\phi$ elsewhere. It is odd under $w\mapsto-w$. Pairing $w$ with $-w$ inside $B_1(0)$ bounds its
contribution there by $\frac12\int_{B_1}|m_\phi|(2|w|)^\alpha=M_\alpha(\phi)$. For $|w|=r\ge1$,
$G(re^{i\theta})=\frac1\pi\sum_{n\ge0}(n+1)4^{-n}r^{-2n-3}e^{-i(2n+3)\theta}$. The angular lemma bounds the $n$th term by
$2(n+1)4^{-n}a_{2n+3}(\alpha)/(2n+1-\alpha)$. The $n=0$ term is kept exactly. For $k\ge5$ Jensen's inequality, for the
probability measure $k\sin(kt)\,dt$ on $[0,\pi/(2k)]$, gives
$a_k(\alpha)\le\frac1\pi\big(\frac{2k\cos(\pi/(2k))}{k^2-1}\big)^\alpha$. This gives $H_\alpha$. Finally, $\phi\mapsto M_\alpha(\phi)$ is the restriction to unit
vectors of a seminorm of the two real coefficients $(\cos\phi,\sin\phi)$, even and of period $\pi$. On a grid of spacing $\delta=\pi/(2m)$
every unit vector is a combination of its two neighbouring grid vectors, with nonnegative coefficients whose sum is at most
$\sec(\delta/2)$. This covers all phases. $\square$

The two integrals in $M_\alpha$ have bounded integrands on fixed compact parameter rectangles. With $r=\sin v$,
$\theta=\frac\pi2-v+v\tau$ on $[0,\frac\pi2]\times[0,1]$ for the first, and $w=\frac12+se^{i\theta}$ on $[0,\frac12]\times[0,\pi]$ for
the second, the symmetric reduction uses $|a+b|+|a-b|=2\max(|a|,|b|)$. Interval quadrature over rectangles therefore
encloses $M_\alpha$ rigorously. The omitted tail of $H_\alpha$ after $N$ terms is at most $\frac{(1+1/N)4^{1-N}}{3\pi}$. The certified
evaluations of $U_m$ use $m=32$ and $512\times512$ rectangles with 160-bit ball arithmetic.

**Theorem 3.4 (four-point reflection orbits).** For $w=X+iY$ with $X,Y>0$, put $h=(2X)^\alpha$, $v=(2Y)^\alpha$, $d=(2|w|)^\alpha$
and $\mathcal P(w;a,b)=2\max\{ah+b(d-h),\ a(d-v)+bv\}$ for $a,b\ge0$. In Theorem 3.3, $M_\alpha(\phi)$ may be replaced by

$$\widetilde M_\alpha(\phi)=\int_{E\cap\{X,Y>0\}}\mathcal P\big(w;|\operatorname{Re}G|\cos\phi,|\operatorname{Im}G|\sin\phi\big)\,dA
+\int_{B_{1/2}(x)\cap\{Y>0\}}\mathcal P\big(w;|\operatorname{Re}Q|\cos\phi,|\operatorname{Im}Q|\sin\phi\big)\,dA,\qquad Q(w)=\frac1{2\pi(w+\frac12)^2},$$

and $\widetilde M_\alpha\le M_\alpha$ pointwise.

*Proof.* The regular density is odd under $w\mapsto-w$; its $\cos\phi$ component is even and its $\sin\phi$ component odd under
conjugation. Hence on each orbit $(\pm X,\pm Y)$ the masses are $a+b$, $a-b$, $-a+b$, $-a-b$ at $(X,Y)$, $(X,-Y)$, $(-X,Y)$, $(-X,-Y)$.
If $a\ge b$, every transport plan from the positive to the negative masses sends some $q\in[0,a-b]$ along each horizontal edge
and the rest along the diagonals. Its cost is $2qh+2(a-q)d$, which is minimal at $q=a-b$. If $b\ge a$ the same holds with
vertical edges. The two linear expressions in $\mathcal P$ differ by $(a-b)(h+v-d)$, and $h+v\ge d$, so $\mathcal P$ equals the
optimal cost in both cases. Summing increments of $f$ along this finite plan bounds the orbit functional by $\mathcal P$.
$\mathcal P$ is a seminorm of $(a,b)$, so the phase-grid argument of Theorem 3.3 applies. Since $h,v\le d$,
$\mathcal P\le2\max(a,b)d$, which is the antipodal cost used in Theorem 3.3. $\square$

The fine evaluation of Theorem 3.4 ($384^2$ rectangles) gives $C_{1/2}\le2.3152114881$ and $D_{1/2}\le2.7455751656$. The
regular term itself is about $0.338$ at $\alpha=\frac12$, and its reduction by the orbit transport is modest. Most of the
remaining excess at moderate $\alpha$ comes from the exterior term $H_\alpha$. The next theorem replaces $H_\alpha$ by a
finite transport on circles.

**Theorem 3.5 (exterior circles).** For $0\le q\le\frac14$ and a phase $\phi$ put
$g_{q,\phi}(\theta)=\operatorname{Re}\big(e^{i\phi-3i\theta}/(\pi(1-qe^{-2i\theta})^2)\big)$, so that the increment density of Theorem 3.3
on $|w|=r\ge1$ is $r^{-3}g_{1/(4r^2),\phi}(\theta)$. Let $n$ be even, and split the circle into $n$ equal cells $I_j$ of length
$\Delta=2\pi/n$ with $I_{j+n/2}=I_j+\pi$. Let $\mathcal Q$ be a closed interval of $q$-values. Choose rational $m_j$ for
$j<n/2$ and set $m_{j+n/2}=-m_j$. Each $m_j$ must be $0$, or else for every $q\in\mathcal Q$ the function $g_{q,\phi}$ has the
sign of $m_j$ on $I_j$ and $|m_j|\le\int_{I_j}|g_{q,\phi}|$. Let $T_j\ge\sup_{q\in\mathcal Q}\int_{I_j}|g_{q,\phi}|$. Let
$\pi_{jk}\ge0$ be any matrix whose row sums are the positive $m_j$ and whose column sums are the magnitudes of the negative
$m_k$. Put $c_{jk}=[2\sin(\min\{\pi,d_{jk}+\Delta\}/2)]^\alpha$, where $d_{jk}$ is the angular distance between cell centres. Then
for every $q\in\mathcal Q$ and every $f$ on the unit circle with $|f(e^{i\theta})-f(e^{i\eta})|\le|e^{i\theta}-e^{i\eta}|^\alpha$,

$$\Big|\int_0^{2\pi}g_{q,\phi}f\,d\theta\Big|\le B_\alpha(\mathcal Q,\phi):=\sum_{j,k}\pi_{jk}c_{jk}+2^\alpha\sum_{j<n/2}(T_j-|m_j|).$$

Consequently, if $0<u_0<u_1<\dots<u_N=1$ and $B_i$ is such a bound for $\mathcal Q_i=[u_{i-1}^2/4,u_i^2/4]$, then in Theorem 3.3 the
exterior term $H_\alpha$ may be replaced, at each phase node, by

$$E_\alpha(\phi)=\sum_{i=1}^NB_i\,\frac{u_i^{1-\alpha}-u_{i-1}^{1-\alpha}}{1-\alpha}
+\frac{2a_3(\alpha)u_0^{1-\alpha}}{1-\alpha}+2\sum_{k\ge1}\frac{(k+1)4^{-k}a_{2k+3}(\alpha)u_0^{2k+1-\alpha}}{2k+1-\alpha},$$

provided that $E_\alpha(\phi_j)$ is placed inside the phase maximum together with $\widetilde M_\alpha(\phi_j)$. That is,

$$C_\alpha\le\frac{2^{1-\alpha}a_2(\alpha)}\alpha+\sec\frac\pi{4m}\max_{0\le j\le m}\big(\widetilde M_\alpha(\phi_j)+E_\alpha(\phi_j)\big),\qquad
D_\alpha\le\frac{2^{1-\alpha}A_\alpha}\alpha+\frac12+\sec\frac\pi{4m}\max_{0\le j\le m}\big(\widetilde M_\alpha(\phi_j)+E_\alpha(\phi_j)\big).$$

*Proof.* Fix $q\in\mathcal Q$. For each nonzero $m_j$ take the submeasure of $|g_{q,\phi}|\,d\theta$ on $I_j$ of mass $|m_j|$ obtained by
scaling, and on $I_{j+n/2}$ its image under $\theta\mapsto\theta+\pi$. Couple these submeasures by the product couplings
$\pi_{jk}\,(\mu_j/|m_j|)\otimes(\mu_k/|m_k|)$. Any two points of $I_j$ and $I_k$ are at chordal distance at most
$2\sin(\min\{\pi,d_{jk}+\Delta\}/2)$, so this part of the functional is at most $\sum\pi_{jk}c_{jk}$. Since $g_{q,\phi}(\theta+\pi)=-g_{q,\phi}(\theta)$,
the residual density $\rho$ is also odd under $\theta\mapsto\theta+\pi$, and its total variation on a half-circle is at most
$\sum_{j<n/2}(T_j-|m_j|)$. Then $\int\rho f=\int_0^\pi\rho(\theta)(f(e^{i\theta})-f(-e^{i\theta}))\,d\theta$ is at most $2^\alpha$ times that variation. For
the radial step, a function with $[f]_\alpha\le1$ on the plane restricts on $|w|=r$ to $r^\alpha$ times a function as above, so the
exterior contribution is at most $\int_1^\infty r^{\alpha-2}B_\alpha\,dr=\int_0^1u^{-\alpha}B_\alpha\,du$ with $u=1/r$. On $(0,u_0)$ the series bound
of Theorem 3.3 is used at radius $1/u_0$. The sum of the regular and exterior functionals is a linear functional of
$(\cos\phi,\sin\phi)$ after the two local operators have been subtracted, and the local bounds are uniform in $\phi$. The phase
argument of Theorem 3.3 therefore applies to the sum. $\square$

*Certification.* The cell masses are enclosed by interval evaluation of $g_{q,\phi}$ at cell midpoints, together with the
derivative bounds $|\partial_\theta g|\le3(1+Q)/(\pi(1-Q)^3)$ and $|\partial_\theta^2g|\le9(1+4Q+Q^2)/(\pi(1-Q)^4)$ for $q\le Q\le\frac14$. These
follow from $g=\operatorname{Re}\frac{e^{i\phi}}\pi\sum_{k\ge0}(k+1)q^ke^{-i(2k+3)\theta}$. The transport matrices pair adjacent sign runs.
They are integer matrices whose row and column sums are checked exactly. A floating search only selects the plan. The
certificate uses $512$ cells, $128$ radial intervals, $m=16$ and 160-bit ball arithmetic, combined with an evaluation of the compact
(reflection-orbit) part of Theorem 3.4 on $384^2$ rectangles. That combination gives $C_{1/2}\le2.2380825911$ and
$D_{1/2}\le2.6684462687$. A finer evaluation of the compact part, on $768^2$ rectangles split into contiguous row blocks
whose interval sums are merged after exact checks of the block boundaries, gives $C_{1/2}\le2.2284808052$,
$D_{1/2}\le2.6588444828$, $C_{3/4}\le2.6784342031$ and $C_{9/10}\le5.0493226547$. For $D_\alpha$ at $\alpha=0.05$ and $\alpha=0.1$ this, lowered by
Theorem 3.10, is the best upper bound in Table 1. At the larger exponents, Theorem 3.6 also replaces the reflection cost on the middle
region $E$ by an exact finite transport. The reflection cost loses the cancellation within each half-plane.

**Theorem 3.6 (transport on the middle circles).** Keep the notation of Theorems 3.3 to 3.5 and put
$\nu_\phi=\operatorname{Re}(e^{i\phi}G)$. Points of $E\cap\{Y>0\}$ are $z(t,s)=\sin t\,e^{i(\pi/2+ts)}$ with $0<t<\frac\pi2$ and
$-1\le s\le1$, because $re^{i\theta}$ lies outside both pole disks exactly when $|\cos\theta|\le r$. Then $dA=t\sin t\cos t\,ds\,dt$, and
with $w_\phi(t,s)=t\sin t\cos t\,\nu_\phi(z(t,s))$ and $G(-z)=-G(z)$,

$$\int_E\nu_\phi f\,dA=\int_0^{\pi/2}\!\!\int_{-1}^1w_\phi(t,s)\big(f(z(t,s))-f(-z(t,s))\big)\,ds\,dt .$$

Split $[0,\frac\pi2]$ into bins $[a,b]$ and $[-1,1]$ into $N$ cells $S_j$ of width $2/N$. On each bin choose rational $m_j$, each
either $0$ or of the sign of $w_\phi$ on the whole cell for every $t\in[a,b]$ with $|m_j|\le\inf_{t\in[a,b]}\int_{S_j}|w_\phi(t,s)|\,ds$,
and $T_j\ge\sup_{t\in[a,b]}\int_{S_j}|w_\phi(t,s)|\,ds$. The reflected cells $-z(t,S_j)$ carry the masses $-m_j$. Let $\pi_{jk}\ge0$ be a
rational transport from the positive to the negative model masses (over both halves) with exact marginals, and let $c_{jk}$
bound $|z-z'|^\alpha$ for $z,z'$ in the two cells at a common $t\in[a,b]$, for example, with $k$ the difference of the cell
indices,

$$c^{\rm same}_k=\big[2\sin b\,\sin\big(\min\{\tfrac\pi2,\ b(k+1)/N\}\big)\big]^\alpha,\qquad
c^{\rm opp}_k=\big[2\sin b\,\cos\big(a\max\{0,k-1\}/N\big)\big]^\alpha$$

for two cells in the same half and in opposite halves. Then for $[f]_\alpha\le1$ the bin contributes at most
$(b-a)\big(\sum\pi_{jk}c_{jk}+(2\sin b)^\alpha\sum_j(T_j-|m_j|)\big)$ to $|\int_E\nu_\phi f|$. In this bound the residual term
$(b-a)(2\sin b)^\alpha\tau$, $\tau=\sum_j(T_j-|m_j|)$, may be replaced by the middle-arc residual cost
$\sum_i(b_i-a_i)\big(\tau A_i+\min(\tau,Q_i)(B_i-A_i)\big)$, for any intervals $[a_i,b_i]$ that partition $[a,b]$, where
$A_i=(2\sin^2b_i)^\alpha$, $B_i=(2\sin b_i)^\alpha$ and $Q_i\ge\sup_{a_i\le t\le b_i}|M_\phi(t)-\sum_jm_j|$, with

$$M_\phi(t)=-\frac2\pi\sin t\cos t\,\sin\phi\,\Lambda(\sin^2t),\qquad\Lambda(u)=\log(1+8u)+\frac{8u(1-4u)}{1+8u}.$$

Call the sum over bins $W_\alpha(\phi)$, and let
$X_\alpha(\phi)$ be the second (pole-disk) integral in $\widetilde M_\alpha(\phi)$ of Theorem 3.4. Then

$$C_\alpha\le\frac{2^{1-\alpha}a_2(\alpha)}\alpha+\sec\frac\pi{4m}\max_{0\le j\le m}\big(W_\alpha(\phi_j)+X_\alpha(\phi_j)+E_\alpha(\phi_j)\big),$$

and the same with $\frac{2^{1-\alpha}A_\alpha}\alpha+\frac12$ in place of the first term bounds $D_\alpha$; here $\phi_j=j\pi/(2m)$.

*Proof.* At fixed $t$ take, in each cell with $m_j\ne0$, the submeasure of $|w_\phi(t,\cdot)|\,ds$ of mass $|m_j|$ obtained by
scaling, and its image in the reflected cell. Couple them by the product couplings weighted by $\pi_{jk}$. The distance
bounds follow from $|z(t,s)-z(t,s')|=2\sin t\,\sin(t|s-s'|/2)$ and $|z(t,s)+z(t,s')|=2\sin t\,\cos(t|s-s'|/2)$. The remainder is
odd under $z\mapsto-z$, has variation at most $\sum_j(T_j-|m_j|)$ on the upper half, and is paired antipodally at cost
$(2\sin t)^\alpha$. Integrating over $t$ gives the bin bound. For the middle-arc residual cost let $\sigma$ be the remainder on
the upper arc at a fixed $t\in[a_i,b_i]$, with variation $V\le\tau$ and signed mass $q$. Its positive and negative parts have masses
$\frac{V+q}2$ and $\frac{V-q}2$. Couple an amount $\frac{V-|q|}2$ of each within the arc by product measures, do the same for the reflected
copy, and pair the remaining one-signed part, of mass $|q|$, antipodally. The arc $z(t,[-1,1])$ has angular width $2t\le\pi$, so
its diameter is $2\sin^2t$, and the cost is at most $(V-|q|)(2\sin^2t)^\alpha+|q|(2\sin t)^\alpha\le(V-|q|)A_i+|q|B_i\le\tau A_i+\min(\tau,Q_i)(B_i-A_i)$,
because both coefficients are nonnegative, $|q|\le V$ and $B_i\ge A_i$. It remains to identify $q=\int_{-1}^1w_\phi(t,s)\,ds-\sum_jm_j$. With
$r=\sin t$ and $\theta=\frac\pi2+ts$, $\int_{-1}^1w_\phi(t,s)\,ds=r\cos t\,\operatorname{Re}\big(e^{i\phi}\int_{\pi/2-t}^{\pi/2+t}G(re^{i\theta})\,d\theta\big)$. On the upper
half-plane $\Phi(z)=-\frac{2z}{z^2-1/4}+4\operatorname{artanh}(2z)$, with principal logarithms, satisfies $\Phi'(z)=(z^2-\frac14)^{-2}$ and
$\Phi(-\bar z)=-\overline{\Phi(z)}$. Since $G(z)\,d\theta=\Phi'(z)\,dz/(i\pi)$ on the circle, the inner integral is
$\frac1{i\pi}\big(\Phi(-\bar z_R)-\Phi(z_R)\big)=\frac{2i}\pi\operatorname{Re}\Phi(z_R)$, where $z_R=r^2+ir\cos t$. For $u=r^2$ direct computation gives
$|z_R^2-\frac14|^2=\frac{1+8u}{16}$, $\operatorname{Re}\frac{-2z_R}{z_R^2-1/4}=\frac{8u(1-4u)}{1+8u}$, $|1+2z_R|^2=1+8u$ and $|1-2z_R|^2=1$, so
$\operatorname{Re}\Phi(z_R)=\Lambda(u)$ and $\int_{-1}^1w_\phi(t,s)\,ds=M_\phi(t)$. The pole disks and the exterior are treated as in Theorems 3.4
and 3.5. The sum of the three regular functionals is linear in $(\cos\phi,\sin\phi)$, so the phase argument of Theorem 3.3
applies. $\square$

*Certification.* On $E$ both poles are at distance at least $\frac12$, so $|G'|\le16/\pi$ and $|G''|\le96/\pi$. With
$W=t\sin t\cos t$ and $r=\sin t$ this gives $|\partial_sw_\phi|\le16Wtr/\pi$ and $|\partial_s^2w_\phi|\le Wt^2(16r+96r^2)/\pi$.
An interval enclosure of $w_\phi$ at the cell midpoint, uniform in $t$ over the bin, then certifies the sign on the cell and
encloses the cell mass with error $L_2h^3/24$, $h=2/N$. Masses are rounded down to multiples of $2^{-44}$, and the integer
transport marginals are checked exactly. A floating search only selects the plan. The certificate uses $N=512$ cells,
$512$ bins, $m=16$ and 160-bit ball arithmetic. $X_\alpha$ is enclosed on $512^2$ polar rectangles of the half disk, and
$E_\alpha$ is the exterior certificate of Theorem 3.5. The results are

$$C_{3/10}\le2.7985307220,\quad C_{1/2}\le2.2179196588,\quad C_{3/4}\le2.6608093210,\quad C_{9/10}\le5.0274238322,$$
$$D_{3/10}\le3.2188978827,\quad D_{1/2}\le2.6482833363,\quad D_{3/4}\le3.1018021765,\quad D_{9/10}\le5.4739442376.$$

An independent recomputation of each final endpoint from the adverse endpoints of the source intervals, in 90-digit
arithmetic, stays below these decimals. With the middle-arc residual cost on $8$ equal subintervals of each bin, $Q_i$ enclosed
from the real formula for $M_\phi$ in 160-bit ball arithmetic, and the extracted masses recomputed with the original precision
and mass unit (so that every plan stays admissible), each phase bound is lowered by the amount, if positive, by which a lower
bound for the former residual cost exceeds an upper bound for the new one. This gives

$$D_{3/10}\le3.2175043762,\quad D_{1/2}\le2.6460060556,\quad D_{3/4}\le3.0984107266,\quad D_{9/10}\le5.4698599222,$$

with worst phase $j=11$ at all four exponents. The recomputation covers all $512$ bins and $17$ phases, its former residual
costs agree with the stored enclosures, and the recombination is exact. Theorems 3.8 to 3.10 lower these bounds for $D_\alpha$
further. The bounds for $C_\alpha$ are superseded at all four by the next theorem.

**Theorem 3.7 (paired transport on the local circles).** Keep the notation of Theorems 3.3 to 3.6, so $x=\frac12$, $y=-\frac12$
and $K_\phi(w)=\operatorname{Re}(e^{i\phi}/(2\pi w^2))$. For $0<r<\frac12$ and $0\le\theta<2\pi$ put $z_r(\theta)=x+re^{i\theta}$ and

$$w_\phi(r,\theta)=\frac{\cos(2\theta-\phi)}{2\pi}-\frac{r^2}{2\pi}\operatorname{Re}\frac{e^{i\phi}}{(1+re^{i\theta})^2}.$$

Fix $0<\delta<\frac12$ and split $[\delta,\frac12]$ into radial bins $[a,b]$, and the circle into $N$ cells $I_j$ of length $h=2\pi/N$. On
each bin choose rational $m_j$, each either $0$ or of the sign of $w_\phi(r,\cdot)$ on the whole of $I_j$ for every $r\in[a,b]$, with
$|m_j|\le\inf_{r\in[a,b]}\int_{I_j}|w_\phi(r,\theta)|\,d\theta$, and $T_j\ge\sup_{r\in[a,b]}\int_{I_j}|w_\phi(r,\theta)|\,d\theta$. The reflected cells
$-z_r(I_j)$ on the circle around $y$ carry the masses $-m_j$. Let $\pi\ge0$ be a rational flow on ordered pairs of cells (on either
circle) whose first marginal minus its second marginal is exactly this signed family. For two cells on the same circle at
circular index distance $k$ put $c_k=2\sin(\pi\min\{k+1,N/2\}/N)$, and for a cell $I_j$ on the right circle and a reflected cell
$-z_r(I_k)$ let $e_{jk}\ge\sup\{|1+r(e^{i\theta}+e^{i\eta})|:\theta\in I_j,\ \eta\in I_k,\ r\in[a,b]\}$. The bin cost is

$$\ell_{[a,b]}(\phi)=\sum_{\text{same circle}}\pi_{jk}c_k^\alpha\frac{b^\alpha-a^\alpha}\alpha+\sum_{\text{opposite circles}}\pi_{jk}e_{jk}^\alpha\log\frac ba
+(1+2b)^\alpha\log\frac ba\sum_j(T_j-|m_j|),$$

and $L_\alpha(\phi)$ is the sum of the bin costs. With $V=\log\frac ba\sum_j(T_j-|m_j|)$ and any
$Q\ge\big|\frac{\cos\phi}2(b^2-a^2)+\log\frac ba\sum_jm_j\big|$, the last term of the bin cost may be replaced by the balanced residual cost
$(2b)^\alpha V+\min(V,Q)\big((1+2b)^\alpha-(2b)^\alpha\big)$, or by the radial residual cost defined as follows. Put
$\tau=\sum_j(T_j-|m_j|)$, $q(r)=-r^2\cos\phi-\sum_jm_j$ and $g(r)=(1+2r)^\alpha-(2r)^\alpha$; for $0<s<t$ put $L=\log\frac ts$, $H=\frac12-\frac{s^2L}{t^2-s^2}$ and

$$E(s,t)=\tau2^\alpha\frac{t^\alpha-s^\alpha}\alpha+g(s)\min\big(\tau L,\,(L-H)|q(s)|+H|q(t)|\big);$$

then for every partition $a=s_0<s_1<\dots<s_n=b$ the last term of the bin cost may be replaced by $\sum_{i<n}E(s_i,s_{i+1})$. Let $W_\alpha$ and $E_\alpha$ be as in Theorems 3.6 and 3.5, and

$$S_\alpha(\delta)=\frac{2a_2(\alpha)\delta^\alpha}\alpha+\frac{(1+2\delta)^\alpha\delta^2}{2(1-\delta)^2}.$$

Then, with $\phi_j=j\pi/(2m)$,

$$C_\alpha\le S_\alpha(\delta)+\sec\frac\pi{4m}\max_{0\le j\le m}\big(L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)\big).$$

*Proof.* On $B(x,\frac12)$, in the coordinates $z=z_r(\theta)$, $dA=r\,dr\,d\theta$, the increment density
$\nu_\phi(z)=K_\phi(z-x)-K_\phi(z-y)$ times $dA$ equals $w_\phi(r,\theta)\,d\theta\,dr/r$. Since $\nu_\phi(-z)=-\nu_\phi(z)$, the
contribution of the two disks $B(x,\frac12)\cup B(y,\frac12)$ is

$$\int_0^{1/2}\frac{dr}r\int_0^{2\pi}w_\phi(r,\theta)\big(f(z_r(\theta))-f(-z_r(\theta))\big)\,d\theta ,$$

where the own-pole part has angular mean zero, so $f(x)$ and $f(y)$ may be subtracted and the integral converges for
$\alpha>0$. Unlike Theorems 3.3 to 3.6, the smooth other-pole part $-\frac{r^2}{2\pi}\operatorname{Re}(\cdots)$ stays inside the transported
measure, so no separate cross-disk term arises. For fixed $r$ the circle measure is centrally odd with total mass zero. On each
cell with $m_j\ne0$ let $\mu_j$ be the submeasure of $|w_\phi(r,\cdot)|\,d\theta$ of mass $|m_j|$ obtained by scaling, normalized to
mass one; on each cell with $m_j=0$ let $\mu_j$ be a point mass in the cell; on the reflected cells use the images. Since
$\pi$ has divergence $m_j$ at every cell, $\sum\pi_{jk}\,\mu_j\otimes\mu_k$ has first minus second marginal $\sum_jm_j\mu_j$, so a
flow may pass through cells with $m_j=0$. Writing the functional as the integral of $f(z)-f(z')$
against this coupling bounds it by the integral of $|z-z'|^\alpha$. Two points of one circle in cells at index distance $k$
are at distance at most $rc_k$, and $\int_a^br^\alpha\,dr/r=(b^\alpha-a^\alpha)/\alpha$. For points on opposite circles,
$|z_r(\theta)+z_r(\eta)|=|1+r(e^{i\theta}+e^{i\eta})|\le e_{jk}$. The remainder is odd under $z\mapsto-z$, has variation at most
$\sum_j(T_j-|m_j|)$ on the right circle, and is paired with its reflection at distance $|2z_r(\theta)|\le1+2b$. This gives the bin
cost. For the balanced residual cost let $\sigma$ be the remainder on the right annulus $a\le|z-x|\le b$, so that $V_\sigma=|\sigma|(\mathbb R^2)\le V$
and the remainder on the left is $-M_\#\sigma$ with $M(z)=-z$. The own-pole density has angular mean zero, and $(1+\zeta)^{-2}$ is
holomorphic on the unit disk with circular means $1$, so $\int_0^{2\pi}w_\phi(r,\theta)\,d\theta=-r^2\cos\phi$ and the measure $w_\phi\,d\theta\,dr/r$
on the right annulus has mass $-\frac{\cos\phi}2(b^2-a^2)$. The extracted part has mass $\log\frac ba\sum_jm_j$, so $q=\sigma(\mathbb R^2)$ satisfies $|q|\le Q$. Let
$h=\min(\sigma^+(\mathbb R^2),\sigma^-(\mathbb R^2))$, so $2h=V_\sigma-|q|$. Couple mass $h$ of $\sigma^+$ with mass $h$ of $\sigma^-$ in the closed disk
$\overline B(x,b)$ (distance at most $2b$), do the same for the reflected parts in $\overline B(y,b)$, and pair the remaining one-signed mass $|q|$
with its reflection (distance at most $1+2b$). The cost is $V_\sigma(2b)^\alpha+|q|((1+2b)^\alpha-(2b)^\alpha)$, which is at most the balanced
residual cost because both coefficients are nonnegative and $|q|\le\min(V_\sigma,Q)$. For the radial residual cost apply the same
coupling on each circle $|z-x|=r$ separately. Removing from $w_\phi(r,\cdot)\,d\theta$ on each $I_j$ a part of mass $m_j$ (possible by the sign and size
conditions on $m_j$) leaves a measure of variation at most $\tau$ and, since $\int_0^{2\pi}w_\phi(r,\theta)\,d\theta=-r^2\cos\phi$, of mass exactly
$q(r)$; it lies on a circle of diameter $2r$, and its points are at distance at most $1+2r$ from their reflections. So the cost per unit $dr/r$
is at most $\tau(2r)^\alpha+|q(r)|g(r)$; the measures are measurable in $r$, so these bounds may be integrated over $[s,t]$. The first term
integrates to $\tau2^\alpha(t^\alpha-s^\alpha)/\alpha$. Next, $g'(r)=2\alpha((1+2r)^{\alpha-1}-(2r)^{\alpha-1})<0$, so $g\le g(s)$ on $[s,t]$. Finally $|q(r)|\le\tau$,
and $q$ is affine in $r^2$, so by convexity $|q(r)|\le\frac{(t^2-r^2)|q(s)|+(r^2-s^2)|q(t)|}{t^2-s^2}$; integrating against $dr/r$ gives
$(L-H)|q(s)|+H|q(t)|$, with $0<H<L$ because $\frac{r^2-s^2}{t^2-s^2}\in(0,1)$ inside the interval. On the omitted disks $B(x,\delta)\cup B(y,\delta)$ the own-pole parts cost at most $a_2(\alpha)\delta^\alpha/\alpha$ each by the angular
lemma. The other-pole density has $\int_0^{2\pi}|\cdot|\,d\theta\le r^2/(1-r)^2$, and pairing with the reflection at distance at most
$1+2\delta$ costs at most $(1+2\delta)^\alpha\int_0^\delta r(1-r)^{-2}\,dr\le(1+2\delta)^\alpha\delta^2/(2(1-\delta)^2)$. The local disks, the middle
region of Theorem 3.6 and the exterior of Theorem 3.5 are disjoint up to null sets and cover the plane. After removing the
two omitted disks, the remaining functional is linear in $(\cos\phi,\sin\phi)$, so the phase argument of Theorem 3.3 applies
to it; the omitted disks are bounded uniformly in $\phi$. Reflection in the horizontal axis and a change of sign reduce all
phases to $[0,\frac\pi2]$. $\square$

The identity term can also be moved into these local circles: adding atoms $-\lambda(r)\delta_x+\lambda(r)\delta_y$ with
$\int_0^{1/2}\lambda(r)\,dr/r=\frac12$ reproduces $-\frac12(f(x)-f(y))$ exactly. This would give a bound for $D_\alpha$, but it needs its own
phase range ($[0,\frac\pi2]$ is not enough for the identity-bearing densities) and has not been certified.

*Certification.* The cells are $I_j=[\frac\phi2+\frac\pi4+jh,\frac\phi2+\frac\pi4+(j+1)h]$, aligned with the zeros of the own-pole
density, whose cell masses are computed exactly from the sine antiderivative. The other-pole part
$q=\frac{r^2}{2\pi}\operatorname{Re}\frac{e^{i\phi}}{(1+re^{i\theta})^2}$ has $|\partial_\theta^2q|\le b^3(1+2b)/(\pi(1-b)^4)=:L_2$ on the bin, since before taking
the real part the second derivative is $r^3e^{i(\phi+\theta)}(1-2re^{i\theta})/(\pi(1+re^{i\theta})^4)$. Its cell integral is therefore
enclosed by $hq(r,\theta_j)\pm L_2h^3/24$, uniformly in $r\in[a,b]$ by interval evaluation. A direct interval evaluation of $w_\phi$ on
the whole cell certifies the sign. Masses are rounded down to multiples of $2^{-44}$. For the opposite-circle distances,
$|1+r(e^{i\theta}+e^{i\eta})|^2$ is a convex quadratic in $r$, so complex interval evaluation at $r=a$ and $r=b$ gives $e_{jk}$. The flows are
built greedily; the greedy ordering uses floating distances, which only selects a feasible plan, and every integer flow is
checked exactly to have the stated marginals. With $\alpha=\frac12$, $\delta=\frac1{64}$, $N=512$, $256$ radial bins, $m=16$,
160-bit ball arithmetic for the local circles and 192-bit balls for the recombination, the largest phase sum is at $\phi=\frac{3\pi}8$ and is below $2.04301160395$, while
$S_{1/2}(\frac1{64})<0.15154248213$. This gives

$$C_{1/2}\le2.1970179509 .$$

An independent recombination from the adverse endpoints of all source intervals, in 90-digit arithmetic, gives
$2.19701795084725\ldots$. Independent real-coordinate checks of 63325 extracted masses, 1013200 sign samples and 12792 distances
found no violation; these support, but do not replace, the interval certificate.

With the same parameters ($\delta=\frac1{64}$, $N=512$, $256$ radial bins, $m=16$, 160-bit local arithmetic, 192-bit recombination) the certificate was repeated at three
more exponents, with one set of integer flows shared by the three exponents. This is admissible because a feasible plan
need not be optimal: the greedy order uses only Euclidean distances, and every marginal is checked exactly. Same-circle edges
at the same cell-index distance $k$ have the same certified chord bound $2\sin(\pi\min(k+1,256)/512)$, so their integer
masses are summed before the cost is applied; this does not change the cost. The result is

$$C_{3/10}\le2.7748077123,\qquad C_{3/4}\le2.6442935978,\qquad C_{9/10}\le5.0137426873,$$

with independent 90-digit recombinations $2.77480771223\ldots$, $2.64429359776\ldots$ and $5.01374268729\ldots$. Since the right side
is an upper bound for every admissible choice of flows and plans, the plans of the middle and exterior circles may also be
chosen by floating optimization at the exponent itself; only their evaluation must be rigorous. With the same local flows and
grids ($\delta=\frac1{64}$, $m=16$, $N=512$, $256$ local radial bins), middle-circle plans on $512$ radial bins of $[0,\frac\pi2]$ with $512$
cells per half and exterior plans on $128$ radial bins of $u\in[\frac14,1]$ with $512$ cells, chosen at each exponent, the certificate gives

$$C_{1/100}\le64.0882805059,\quad C_{1/20}\le13.1843720067,\quad C_{1/10}\le6.8520467682,\quad C_{1/5}\le3.7444366045,\quad C_{99/100}\le42.2253356279,$$

and $C_{1/1000}\le637.0404763100$, which is weaker than Theorem 5.7(ii). The worst phases are $j=16,15,15,14,11$ (and $16$ at
$\alpha=\frac1{1000}$). An independent audit checked exact coverage of all radial rows and phases, the identity of the programs
with those of the certificates above, and recombined all six values at 320 bits; the whole computation at $\alpha=\frac15$ was
replayed independently.

With the smaller of the balanced and the radial residual cost in each radial bin, the latter on $8$ equal subintervals of the bin,
$Q$, $\tau$ and $|q|$ evaluated in outward arithmetic and all other terms unchanged, the same certificates give

$$C_{1/100}\le64.0882485032,\quad C_{1/20}\le13.1842538716,\quad C_{1/10}\le6.8518145023,\quad C_{1/5}\le3.7439473709,\quad C_{3/10}\le2.7740910337,$$

$$C_{1/2}\le2.1956570947,\quad C_{3/4}\le2.6421664049,\quad C_{9/10}\le5.0112069529,\quad C_{99/100}\le42.2225497071$$

(and $C_{1/1000}\le637.0404730920$, weaker than Theorem 5.7(ii)); the worst phases are $j=16,15,15,14,14,12,11,11,11$. The angular extraction does not depend on $\alpha$, so one replay serves all exponents: the extracted
integer masses of all $256$ radial rows and $17$ phases were recomputed independently with the extraction routine and precision
of the original certificates, keeping their exact sums and absolute sums; the former residual cost was removed by subtracting
the lower endpoint of its stored enclosure, and these enclosures were checked against all source chunks. The radial residual
costs were evaluated from the same masses in 256-bit ball arithmetic and recombined exactly. The bounds for $D_\alpha$ are not improved by Theorem 3.7.

At $\alpha=\frac3{10},\frac12,\frac34,\frac9{10}$ the middle term $W_\alpha$ of these certificates is that of the middle-circle certificate of
Theorem 3.6; at the other exponents it is a middle-circle certificate with plans chosen at the exponent and the same
angular extraction, hence the same extracted masses and residual variations. With the middle-arc residual cost of Theorem 3.6,
evaluated as there, in addition to the radial residual cost,

$$C_{1/100}\le64.0882119580,\quad C_{1/20}\le13.1840592665,\quad C_{1/10}\le6.8514311158,\quad C_{1/5}\le3.7431835793,\quad C_{3/10}\le2.7729133174,$$

$$C_{1/2}\le2.1934924293,\quad C_{3/4}\le2.6387739538,\quad C_{9/10}\le5.0071216363,\quad C_{99/100}\le42.2180350354$$

(and $C_{1/1000}\le637.0404694256$, weaker than Theorem 5.7(ii)); the worst phases are $j=16,15,15,15,14,12,11,11,11$. Theorem 3.8 lowers
these values further.

**Theorem 3.8 (exact phase interpolation).** Let $m\ge1$, $\gamma=\pi/(2m)$ and $\phi_j=j\gamma$. For $u,v\ge0$ put

$$H_\gamma(u,v)=\begin{cases}u,&v\le u\cos\gamma,\\ v,&u\le v\cos\gamma,\\ \dfrac{\sqrt{u^2+v^2-2uv\cos\gamma}}{\sin\gamma},&\text{otherwise}\end{cases}$$

(if both of the first two conditions hold, then $u=v=0$). Let $\Lambda_\phi=\cos\phi\,\Lambda_0+\sin\phi\,\Lambda_{\pi/2}$ be linear functionals
on $\dot C^\alpha$ with $\|\Lambda_{\phi_j}\|\le u_j$ for $0\le j\le m$. Then

$$\sup_{0\le\phi\le\pi/2}\|\Lambda_\phi\|\le\max_{0\le j<m}H_\gamma(u_j,u_{j+1})\le\sec\frac\gamma2\max_{0\le j\le m}u_j .$$

Consequently, in each of Theorems 3.3 to 3.7 the term $\sec\frac\pi{4m}\max_{0\le j\le m}u_j$, where $u_j$ is the phase bound at $\phi_j$
(for example $W_\alpha(\phi_j)+X_\alpha(\phi_j)+E_\alpha(\phi_j)$ in Theorem 3.6 or $L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)$ in Theorem 3.7), may be
replaced by $\max_{0\le j<m}H_\gamma(u_j,u_{j+1})$. The terms that are uniform in the phase, namely the local terms (with the
identity term for $D_\alpha$), $H_\alpha$ in Theorem 3.3 and $S_\alpha(\delta)$ in Theorem 3.7, stay outside the interpolation.

*Proof.* Fix $j$, write $\phi=\phi_j+t$ with $0\le t\le\gamma$, and put $u=u_j$, $v=u_{j+1}$. Multiplying the identity
$\sin(\gamma-t)+\sin t\,e^{i\gamma}=\sin\gamma\,e^{it}$ by $e^{i\phi_j}$ and taking real and imaginary parts gives
$\Lambda_\phi=\big(\sin(\gamma-t)\Lambda_{\phi_j}+\sin t\,\Lambda_{\phi_{j+1}}\big)/\sin\gamma$, with nonnegative coefficients. Hence
$\|\Lambda_\phi\|\le g(t)=\big(u\sin(\gamma-t)+v\sin t\big)/\sin\gamma=u\cos t+(v-u\cos\gamma)\sin t/\sin\gamma$. On $[0,\gamma]$, $g\ge0$ and
$g''=-g\le0$, so $g$ is concave, with $g'(0)=(v-u\cos\gamma)/\sin\gamma$ and $g'(\gamma)=(v\cos\gamma-u)/\sin\gamma$. If $g'(0)\le0$ the
maximum is $g(0)=u$; if $g'(\gamma)\ge0$ it is $g(\gamma)=v$; otherwise it is attained inside and equals the amplitude
$\big(u^2+(v-u\cos\gamma)^2/\sin^2\gamma\big)^{1/2}=\sqrt{u^2+v^2-2uv\cos\gamma}/\sin\gamma$. The coefficient sum is
$\cos(t-\frac\gamma2)/\cos\frac\gamma2\le\sec\frac\gamma2$, which gives the second inequality. In Theorems 3.3 to 3.7, after the
reduction of the phases to $[0,\frac\pi2]$ made there, the phase-dependent functional that remains when the phase-uniform parts
are removed is of the form $\Lambda_\phi$, and the proofs bound it at the grid phases by $u_j$ before covering the other phases.
The grid argument of Theorem 3.3 may therefore be replaced by the one above, and the phase-uniform bounds are added
afterwards. $\square$

$H_\gamma$ is nondecreasing in each argument, being the maximum of $g$ over $t$, so upper endpoints of the $u_j$ suffice. In the
certificates the $u_j$ are the exact rational upper endpoints of the stored phase bounds ($m=16$), the trigonometric functions
and the square root are enclosed in ball arithmetic, and the branch is chosen by a certified sign of $g'(0)$ or $g'(\gamma)$; where
a sign is not decided, the smaller of the amplitude and $\sec\frac\gamma2\max(u,v)$ is used, since both are valid. Applied to the
last certificates of Theorem 3.7 this gives

$$C_{1/100}\le64.0881631620,\quad C_{1/20}\le13.1839509406,\quad C_{1/10}\le6.8511402022,\quad C_{1/5}\le3.7431650122,\quad C_{3/10}\le2.7726584812,$$

$$C_{1/2}\le2.1934098609,\quad C_{3/4}\le2.6387679109,\quad C_{9/10}\le5.0066105983,\quad C_{99/100}\le42.2175842339$$

(and $C_{1/1000}\le637.0403844930$, weaker than Theorem 5.7(ii)), and applied to the middle-arc certificates of Theorem 3.6

$$D_{3/10}\le3.2173694859,\quad D_{1/2}\le2.6458416700,\quad D_{3/4}\le3.0981226274,\quad D_{9/10}\le5.4695864502.$$

At $\alpha=\frac15$ and $\alpha=\frac{99}{100}$ the middle bins of the direct certificates of Theorem 3.7 (plans chosen at the exponent),
lowered by their middle-arc residual savings, are admissible values of $W_\alpha(\phi_j)$ in Theorem 3.6, since the middle measure is the
same and the plans and extracted masses are unchanged. With the cross-disk certificate $X_\alpha$ and, at each phase, the smaller
of the two exterior certificates $E_\alpha(\phi_j)$, Theorem 3.6 gives $D_{1/5}\le4.1832609515$ and $D_{99/100}\le42.6825968459$ with the
factor $\sec\frac\pi{64}$, and with the interpolation

$$D_{1/5}\le4.1832253664,\qquad D_{99/100}\le42.6823437055.$$

All of them were recomputed independently from the stored endpoints,
in 768-bit arithmetic and through a separate cosine-sine amplitude expression, with source-hash checks.

The cross-disk term $X_\alpha$ of Theorem 3.6 was also enclosed on $2048\times2048$ polar rectangles at
$\alpha=\frac15,\frac3{10},\frac12,\frac34,\frac9{10},\frac{99}{100}$ and all $17$ phases, by the same interval program as the $512^2$ enclosure. At each
phase the smaller of the two enclosures is used. With the middle and exterior certificates unchanged and the interpolation,
Theorem 3.6 gives

$$D_{1/5}\le4.1827417136,\quad D_{3/10}\le3.2168671631,\quad D_{1/2}\le2.6453267957,$$

$$D_{3/4}\le3.0975797394,\quad D_{9/10}\le5.4690226815,\quad D_{99/100}\le42.6817720410.$$

The independent check of this enclosure consisted of a check that the program is unchanged, a complete Cartesian
quadrature of the same integrals in floating point at all nodes (a diagnostic, not a second interval computation) and an
exact recombination of all $102$ phase endpoints at $384$ and $768$ bits.

The same unchanged program enclosed $X_\alpha$ once more on $4096\times4096$ polar rectangles at the same six exponents and all
$17$ phases. At each phase the smaller of the available enclosures is used. With the middle and exterior certificates unchanged
and the interpolation, Theorem 3.6 gives

$$D_{1/5}\le4.1826621448,\quad D_{3/10}\le3.2167849538,\quad D_{1/2}\le2.6452417528,$$

$$D_{3/4}\le3.0974919455,\quad D_{9/10}\le5.4689292769,\quad D_{99/100}\le42.6816774355.$$

The independent check of this enclosure consisted of hash checks that the program and its inputs are unchanged, a comparison
of all $204$ floating-point Cartesian quadrature values recorded for the $2048^2$ check with the new interval enclosures (a
diagnostic, not a second interval computation; every value lies inside its enclosure) and an exact recombination of all $102$
phase endpoints at $384$ and $768$ bits. Theorems 3.9 and 3.10 lower these values further.

**Theorem 3.9 (a strict saving in the identity term of $R_1^2$).** Let $0<\alpha<1$, $p=\alpha(1-\alpha)$, $q=\alpha(1-\alpha)(2-\alpha)(3-\alpha)$ and

$$J=-\frac{31}{32}+\frac{27}8\log\frac43=2\int_0^{1/4}\frac{t^3}{(\frac34+t)^2}\,dt,\qquad
K=-\frac{233}{1024}+\frac{405}{512}\log\frac43=\frac12\int_0^{1/4}\frac{t^5}{(\frac34+t)^2}\,dt,$$

so that $J>\frac1{512}$ and $K>\frac1{49152}$ (numerically $J=0.0021769945$, $K=2.1951842\cdot10^{-5}$). For $R>0$ let
$\mu_R=Q_R+(\frac12-\kappa_Q)\delta_0$ be the positive measure of mass $\frac12$ of Theorem 3.2, or its image under a rotation. If $|x-y|=h$ and $R=sh$ with $0<s<2$, then

$$|\mu_R*f(x)-\mu_R*f(y)|\le\big(\tfrac12-\eta(s)\big)h^\alpha[f]_\alpha,\qquad \eta(s)=pJs^2+qKs^4 .$$

Consequently:

(a) in the bounds for $D_\alpha$ of Theorems 3.3 to 3.6, where $s=\frac12$, the term $\frac12$ may be replaced by $\frac12-\frac{pJ}4-\frac{qK}{16}$; like
the local terms, it stays outside the phase maximum and the interpolation of Theorem 3.8;

(b) $D_\alpha\le G(\alpha)-\eta(s^D_\alpha)<G(\alpha)$ for every $0<\alpha<1$, with $s^D_\alpha=\frac{(1-\alpha)B_\alpha}{2A_\alpha}$ as in Theorem 3.2;

(c) for $0<\rho<\frac12$,

$$D_\alpha\le J_D(\alpha,\rho)-p\Big[J\rho^2-\frac{\rho^4}{512(1-\rho)^2}\Big]-q\Big[K\rho^4-\frac{\rho^6}{49152(1-\rho)^2}\Big],$$

with $J_D$ as in Theorem 5.7(ii), and both brackets are positive.

*Proof.* Take $h=1$ and $e=x-y$. With $\beta$ the rotation angle of $\mu_R$ ($\beta=0$ for $\mu_R$ itself), the density of $Q_R$ is $|\cos2(\theta-\beta)|/(2\pi r^2)$ on the two negative lobes, where
$R|\sin2(\theta-\beta)|\le r\le R$. Let $n$ be the unit vector along one negative axis and let $D_\pm$ be the disks of radius $\frac R4$
centred at $c_\pm=\pm\frac34Rn$. *Containment.* In units of $R$, a point of the inner boundary at angle $d\in[0,\frac\pi4]$ from the
axis is $\sin2d\,(\cos d,\sin d)$, and with $\sigma=\sin d$ its squared distance from $(\frac34,0)$, minus $\frac1{16}$, is
$p_0(\sigma)=\frac12-3\sigma+4\sigma^2+3\sigma^3-4\sigma^4$. With $\tau=\sigma-\frac13\in[-\frac13,\frac5{12}]$,
$p_0=\frac1{162}+\frac2{27}\tau+\tau^2(\frac{13}3-\frac73\tau-4\tau^2)$, and the concave bracket is at least its smaller endpoint value $\frac83$, so
$p_0\ge\frac1{162}+\frac2{27}\tau+\frac83\tau^2\ge\frac{11}{1944}>0$. Points of $D_\pm$ satisfy $|\sin d|\le\frac13$ and $r\le R$, and $D_\pm$ does not meet the
inner boundary, so $D_\pm$ lies in the closed lobe, which contains its centre. *Density.* At $c_\pm+u$ with $|u|=tR$, $0\le t\le\frac14$, let $v$ be the cosine of the angle between $u$ and $\pm n$, and put $c=\frac34$.
In units of $R$ the point has coordinates $c+tv$ along the axis and $t\sqrt{1-v^2}$ across it, so the density of $Q_R$ there is
$g_t(v)/(2\pi R^2)$ with $g_t(v)=\big(c^2+2ctv+t^2(2v^2-1)\big)/\big(c^2+2ctv+t^2\big)^2$. Since
$\partial_vg_t=2t\,(3ct^2+2t^3v-c^3)/(c^2+2ctv+t^2)^3$ and $3ct^2+2t^3\le c^3$ for $t\le\frac c2$, $g_t$ is nonincreasing in $v\in[-1,1]$, and the
density of $Q_R$ is at least $w(t)=g_t(1)/(2\pi R^2)=1/(2\pi R^2(\frac34+t)^2)$. *Coupling.* Write $\mu_R=\omega+\omega'$, where $\omega$ has density $w(|z-c_\pm|/R)$ on
$D_\pm$ and $\omega'\ge0$. Couple $\omega'$ by translation, at cost $\omega'(\mathbb R^2)$. On $D_\pm$, $\omega$ is invariant under the reflection
$u\mapsto u'=u-2(u\cdot e)e$ of $u=z-c_\pm$, so $\int f(y-z)\,d\omega=\int f(y-c_\pm-u')\,d\omega$, and $f(x-c_\pm-u)$ is paired with
$f(y-c_\pm-u')$, at distance $1-\xi$, $\xi=2u\cdot e\in[-\frac s2,\frac s2]$. Averaging $u$ and $u'$ gives the cost $A(\xi)=\frac12((1-\xi)^\alpha+(1+\xi)^\alpha)$.
Here $A(0)=1$, $A'(0)=A^{(3)}(0)=0$, $A''(0)=-p$ and $A^{(4)}(\xi)=-\frac q2((1-\xi)^{\alpha-4}+(1+\xi)^{\alpha-4})\le-q$ by convexity of $t^{\alpha-4}$,
so $A(\xi)\le1-\frac p2\xi^2-\frac q{24}\xi^4$. With $\int_0^{2\pi}\cos^2=\pi$ and $\int_0^{2\pi}\cos^4=\frac{3\pi}4$, the two disks save
$4\pi p\int_0^{R/4}r^3w\,dr+\pi q\int_0^{R/4}r^5w\,dr=pJR^2+qKR^4$, which is the main inequality. The bounds on $J$ and $K$ follow from
$(\frac34+t)^{-2}>1$ on $[0,\frac14)$, and the closed forms from the expansions of $(u-\frac34)^3u^{-2}$ and $(u-\frac34)^5u^{-2}$ after the
substitution $u=\frac34+t$. (a) In Theorems 3.3 to 3.6 the term $\frac12$ is the translation cost of $\mu_R$ with $R=\frac12$ at $h=1$, so $s=\frac12$. (b) Theorem 3.2
bounds the increment by $\frac{2A_\alpha}\alpha R^\alpha+B_\alpha R^{\alpha-1}+\frac12-\eta(R)$ for $R<2$, and $R=s^D_\alpha$ gives $G(\alpha)-\eta(s^D_\alpha)$. It
remains to show $s^D_\alpha<2$. Substituting $u=nt$, $a_n(\alpha)=\frac1\pi\int_0^{\pi/2}\sin u\,(2\sin\frac un)^\alpha du$, so $a_3\le a_1=2^\alpha A_\alpha$, and
$b_\alpha\le\frac{a_1+a_3}2\le a_1$. Hence $s^D_\alpha=\frac{2a_3+(1-\alpha)b_\alpha}{2A_\alpha}\le2^{\alpha-1}(3-\alpha)$, which increases on $[0,1]$ and is below $2$ for
$\alpha<1$. (c) In the proof of Theorem 5.7(ii) the projection plan of radius $\rho$ is perturbed by the cross kernels, whose absolute
density on the pole disks is at most $H=1/(2\pi(1-\rho)^2)$. Both full marginal densities at the ends of a translation edge
of $Q_\rho$ with density $\lambda_0$ are at least $\lambda_0$ and change by at most $H$, so the flow-deletion lemma retains at least the fraction
$1-H/\lambda_0$ of the edge, that is, density at least $\lambda_0-H$. On $D_\pm$ with $R=\rho$, $\lambda_0\ge w\ge\frac1{2\pi\rho^2}>H$,
since $\rho<1-\rho$. So the radial measure with density $w-H\ge0$ on $D_\pm$ consists of retained
translation edges, and the coupling above may be applied to it alone, with every other flow unchanged. Its saving is that of $w$
minus $4\pi pH\int_0^{\rho/4}r^3dr+\pi qH\int_0^{\rho/4}r^5dr=\frac{p\rho^4}{512(1-\rho)^2}+\frac{q\rho^6}{49152(1-\rho)^2}$. Since $\frac\rho{1-\rho}<1$,
$J-\frac{\rho^2}{512(1-\rho)^2}>J-\frac1{512}>0$ and $K-\frac{\rho^2}{49152(1-\rho)^2}>K-\frac1{49152}>0$. $\square$

**Theorem 3.10 (larger disks and all even moments).** Let $\sigma$ be the unique root in $(0,\frac13)$ of $p_4(s)=2s^4-3s^2+4s-1$ and

$$c_*=\frac{(1-2\sigma^2)^2}{2(1-2\sigma+2\sigma^3)}.$$

Then $\frac{49}{66}<c_*<\frac34$. Let $c_*\le c\le\frac34$ and $a=1-c$, and for integers $m,n\ge1$ put

$$B_m(c)=\int_0^a\frac{t^m}{(c+t)^2}\,dt,\qquad A_n(\alpha)=\frac{2\alpha}{(n!)^2}\prod_{k=1}^{2n-1}(k-\alpha).$$

With $\mu_R$, $h=|x-y|$ and $s=R/h$ as in Theorem 3.9, if $2as<1$, then

$$|\mu_R*f(x)-\mu_R*f(y)|\le\big(\tfrac12-\eta_c(s)\big)h^\alpha[f]_\alpha,\qquad \eta_c(s)=\sum_{n\ge1}A_n(\alpha)B_{2n+1}(c)\,s^{2n}.$$

All terms of $\eta_c$ are positive, so every partial sum may replace it. At $c=\frac34$ the first two terms are the terms $pJs^2$ and $qKs^4$ of
Theorem 3.9. Each $B_m$ decreases in $c$, so $c=c_*$ gives the largest saving in this family, and $\eta_c(s)>\eta(s)$. Consequently:

(a) in the bounds for $D_\alpha$ of Theorems 3.3 to 3.6, where $s=\frac12$, the term $\frac12$ may be replaced by $\frac12-\eta_c(\frac12)$, outside the
phase maximum as in Theorem 3.9(a);

(b) for $0<\rho<\frac12$, with $J_D$ as in Theorem 5.7(ii),

$$D_\alpha\le J_D(\alpha,\rho)-\sum_{n\ge1}A_n(\alpha)B^\rho_{2n+1}(c)\,\rho^{2n},\qquad B^\rho_m(c)=B_m(c)-\frac{\rho^2a^{m+1}}{(m+1)(1-\rho)^2}>0.$$

(c) let $M_m=\int_0^ax^m\sqrt{a^2-x^2}\,dx$ and

$$I_n(c)=\int_0^a\frac{x^{2n}\sqrt{a^2-x^2}}{c^2+2cx+a^2}\,dx,\qquad \widetilde A_n(\alpha)=\frac{4^{n+1}}\pi\Big(-\binom\alpha{2n}\Big).$$

Then $\eta_c(s)$ may be replaced, in the displayed bound and in (a), by $\widetilde\eta_c(s)=\sum_{n\ge1}\widetilde A_n(\alpha)I_n(c)s^{2n}$, each of
whose terms is larger than the corresponding term of $\eta_c(s)$, and the sum in (b) by
$\sum_{n\ge1}\widetilde A_n(\alpha)\big(I_n(c)-\frac{\rho^2}{(1-\rho)^2}M_{2n}\big)\rho^{2n}$, whose terms are positive.

(d) more generally, let $(c_i,a_i)$, $i=0,\dots,k$, satisfy $0<a_i<\frac{c_i}2$, $c_i+a_i\le1$, $|c_i-c_j|\ge a_i+a_j$ for $i\ne j$, and

$$P_i(t)=c_i^2-a_i^2-4c_it+4t^2+4c_it^3-4t^4\ge0\qquad(0\le t\le\tfrac1{\sqrt2}),$$

and let $2s\max_ia_i<1$. Then the savings of (c) for the pairs of disks of radius $a_iR$ about the two points at distance $c_iR$ from the
origin on the negative axis, with $c,a$ replaced by $c_i,a_i$ in $I_n$ and $M_m$, may be added: their sum replaces $\eta_c(s)$ in the
displayed bound and in (a), and the sum of the cutoff sums replaces the sum in (b). For $c+a=1$ the condition on $P_i$ is $c\ge H$ on
$[0,\frac1{\sqrt2}]$, as in the proof below. The family used below is $(c_0,a_0)=(c,1-c)$, with the rational centre $c$ given after the proof,
together with $(\frac{41}{100},\frac3{40})$, $(\frac{29}{100},\frac1{25})$, $(\frac9{40},\frac3{125})$ and $(\frac7{40},\frac7{500})$.

The savings of Theorems 3.9 and 3.10 come from couplings of the same part of $\mu_R$ and are never added. Theorem 3.9(b) is not
extended to $c<\frac34$, since $2as^D_\alpha<1$ is not established for such $c$ (at $c=\frac34$ it is the inequality $s^D_\alpha<2$
proved there).

*Proof.* Let the negative axis be horizontal. In the containment argument scale $R=1$; the density and the coupling below keep
$R$ and use $h=1$ as in Theorem 3.9. The disk of radius $a$ about $(c,0)$ is internally tangent to $|z|=1$. With
$s_0=\sin d$, $0\le d\le\frac\pi4$, the inner-boundary point $\sin2d\,(\cos d,\sin d)$ has squared distance from $(c,0)$, minus $a^2$, equal to
$P_c(s_0)=2c\,\psi(s_0)-(1-2s_0^2)^2$, where $\psi(s)=1-2s+2s^3$. On $[0,\frac1{\sqrt2}]$, $\psi\ge1-\frac4{3\sqrt3}>0$ (the minimum is at $\frac1{\sqrt3}$), so the
inner boundary avoids the open disk if and only if $c\ge H(s)=\frac{(1-2s^2)^2}{2\psi(s)}$ on $[0,\frac1{\sqrt2}]$. Here $H'=-(1-2s^2)p_4/\psi^2$,
$p_4'(s)=2+8(s-\frac12)^2(s+1)>0$, $p_4(0)=-1$ and $p_4(\frac13)=\frac2{81}$. So $H$ increases up to $\sigma$ and decreases after it, and
$\max H=H(\sigma)=c_*$. Since $\sigma<\frac13$, $c_*>H(\frac13)=\frac{49}{66}$. Also $P_{3/4}$ is the polynomial $p_0$ of the proof of Theorem 3.9, which is
positive, so $H<\frac34$ and $c_*<\frac34$. For $c_*\le c\le\frac34$ we have $c>\frac23$, hence $a<\frac c2$, and the open disk lies in $|z|<1$ and in the
sector of half-width $\arcsin\frac ac<\frac\pi6$ about the axis. It is connected, contains its centre, and contains neither the origin (at distance $c>a$)
nor a point of the inner boundary, so it lies in the lobe; the second disk follows by symmetry. Since $a<\frac c2$, the density computation of
Theorem 3.9 applies with $c$ in place of $\frac34$: at distance $tR$ from the centre, $0\le t\le a$, the density of $Q_R$ is at least
$w(t)=1/(2\pi R^2(c+t)^2)$. In the reflection coupling of Theorem 3.9 the paired distances are $1\mp\xi$ with $|\xi|\le2as<1$, and

$$1-\tfrac12\big((1+\xi)^\alpha+(1-\xi)^\alpha\big)=\sum_{n\ge1}\Big(-\binom\alpha{2n}\Big)\xi^{2n},\qquad -\binom\alpha{2n}=\frac\alpha{(2n)!}\prod_{k=1}^{2n-1}(k-\alpha)>0.$$

All terms are nonnegative and may be integrated termwise. With $\xi=2st\cos\theta$, $\theta$ the angle between the offset $u$ of Theorem 3.9 and $e$, and $\frac1{2\pi}\int_0^{2\pi}\cos^{2n}\theta\,d\theta=\binom{2n}n4^{-n}$, the
$n$-th term saves, on the two disks together, $2\big(-\binom\alpha{2n}\big)(2s)^{2n}\binom{2n}n4^{-n}B_{2n+1}(c)=A_n(\alpha)B_{2n+1}(c)s^{2n}$. At $c=\frac34$,
$A_1B_3=2p\cdot\frac J2$ and $A_2B_5=\frac q2\cdot2K$. The integral $B_m(c)$ decreases in $c$ because its interval shrinks and its integrand decreases.
(b) As in Theorem 3.9(c) the retained density on the disks is at least $w-H_\rho$ with $H_\rho=1/(2\pi(1-\rho)^2)$, and $w\ge\frac1{2\pi\rho^2}>H_\rho$ since
$c+t\le1$ and $\rho<1-\rho$. In units of $\rho$ the retained radial weight is $\frac1{2\pi}\big((c+t)^{-2}-\frac{\rho^2}{(1-\rho)^2}\big)t\,dt\,d\theta>0$, whose
moments are the $B^\rho_m(c)$, and $2a\rho<a<1$.
(c) Use coordinates divided by $R$ and the pushed-forward measure, so that the physical density is $R^{-2}$ times the
density below; the distance weight still contains $s=R/h$. Let $c\,\omega+z$, $|z|=r\le a$, be a point of the disk, where $\omega$ is the unit vector from the origin towards its centre, and let
$v$ be the cosine of the angle between $z$ and $\omega$. The density of $Q_R$ there is $q_r(v)/(2\pi)$, with

$$q_r(v)=\frac{c^2+2crv+r^2(2v^2-1)}{(c^2+2crv+r^2)^2},$$

and $q_r(1)/(2\pi)=1/(2\pi(c+r)^2)$ is the minorant $w$ used above. With $N=c^2+2crv+r^2$,

$$q_r'(v)=\frac{2r(-c^3+3cr^2+2r^3v)}{N^3},\qquad q_r''(v)=\frac{4r^2(3c^4-8c^2r^2-4cr^3v+r^4)}{N^4}.$$

Since $r\le a<\frac c2$, the first bracket is below $c^3(-1+\frac34+\frac14)=0$, and with $t=\frac rc\le\frac12$ the second is at least
$c^4(3-8t^2-4t^3+t^4)\ge\frac9{16}c^4$. So $q_r$ is decreasing and convex on $[-1,1]$. Let $F$ be the reflection in the line through
the centre perpendicular to the increment; it maps the disk onto itself. Let $\theta$ be the angle between $z$ and the increment
and $\gamma$ the angle between $\omega$ and the increment. The density $\min\{q_r(v(z)),q_r(v(Fz))\}=q_r(|\cos\gamma\cos\theta|+\sin\gamma\sin\theta)$ is
$F$-invariant, so the reflection coupling may use it in place of $w$, and the rest of $\mu_R$ is translated as before. The weight
$(2sr\cos\theta)^{2n}$ of the $n$-th term is even in $\theta$. Averaging the angles $\theta$ and $-\theta$ and using convexity, then
$|\cos\gamma\cos\theta|\le|\cos\theta|$ and monotonicity, the density may be replaced by $q_r(|\cos\theta|)$, its value for $\gamma=0$, at every
orientation. For $\gamma=0$ write $z=(x,y)$ with $x$ along the increment. The density $((c+|x|)^2-y^2)/((c+|x|)^2+y^2)^2$ is the
$y$-derivative of $y/((c+|x|)^2+y^2)$, so its integral over $|y|\le\sqrt{a^2-x^2}$ is $2\sqrt{a^2-x^2}/(c^2+2c|x|+a^2)$. Integrating
$(-\binom\alpha{2n})(2sx)^{2n}$ against it over $|x|\le a$, dividing by $2\pi$ and doubling for the two disks gives $\widetilde A_n(\alpha)I_n(c)s^{2n}$.
Since $q_r(|\cos\theta|)>q_r(1)$ when $r>0$ and $|\cos\theta|<1$, each term exceeds $A_n(\alpha)B_{2n+1}(c)s^{2n}$. In (b), in units of $\rho$, the
retained density is at least $(q_r-\kappa)/(2\pi)$ with $\kappa=\frac{\rho^2}{(1-\rho)^2}<1\le q_r(1)$; $q_r-\kappa$ is again decreasing and convex, and the
constant $\kappa$ contributes $M_{2n}$ in place of $I_n(c)$.
(d) For a centre $c_i$ and radius $a_i$, the squared distance of the inner-boundary point at angle $d$ from $(c_i,0)$, minus $a_i^2$, is
$P_i(\sin d)$; for $a=1-c$ this is $P_c$. So $P_i\ge0$, $c_i+a_i\le1$, $P_i(0)=c_i^2-a_i^2>0$ and $a_i<\frac{c_i}2$ place each open disk in
the lobe, as for $c$. Opposite disks are disjoint since $c_i>a_i$, and disks on the same side are disjoint by $|c_i-c_j|\ge a_i+a_j$. The
proof of (c) uses only $r\le a_i<\frac{c_i}2$, $|2sx|\le2sa_i<1$ and, in (b), $q_r(1)\ge(c_i+a_i)^{-2}\ge1>\kappa$. The reflection-invariant
densities on the disjoint disks together are at most the density of $Q_R$, so the reflection couplings on all the disks and the
translation of the rest of $\mu_R$ form one coupling, and the savings add. $\square$

For the numerical values $\sigma$ is isolated by exact rational bisection of $p_4$, $c_*$ is enclosed using the monotonicity of the numerator and
denominator of $H$ on the isolating interval, and the rational centre $c=18575812884078966825547550257/25000000000000000000000000000$ (the upper enclosure rounded up at
$10^{-30}$) is used. The moments are enclosed from their closed form (a rational function of $c$ plus $m(-c)^{m-1}\log\frac1c$, from $u=c+t$) and,
independently, from the positive series $B_m(c)=c^{m-1}\sum_{k\ge0}\binom{m+k-1}k\frac{a^{m+k+1}}{m+k+1}$ (from $u=t/(c+t)$), truncated after $96$
terms with a geometric remainder. The first eight terms of $\eta_c$ are kept; the omitted terms are positive and are not subtracted.
For part (c), $M_m=a^{m+2}W_m/(m+2)$ with the Wallis integrals $W_m=\int_0^{\pi/2}\sin^m\phi\,d\phi$. Since $c+a=1$,
$c^2+2cx+a^2=1-2c(a-x)$, and $I_n(c)=\sum_{k\ge0}(2c)^k\int_0^ax^{2n}(a-x)^k\sqrt{a^2-x^2}\,dx$ is a series of nonnegative terms, each an exact
rational combination of the $M_m$, so of the form $A\pi+B$ with rational $A$ and $B$; successive terms decrease at least by the factor
$2ca<1$. The partial sum of the first $64$ terms is the lower bound used, and the remainder is at most the first omitted term divided
by $1-2ca$. As an independent check, the substitutions $x=a\sin\phi$ and $t=\tan(\phi/2)$ give, with $A_0=c^2+a^2$,

$$F_0=\int_0^a\frac{\sqrt{a^2-x^2}}{A_0+2cx}\,dx=\frac{A_0\pi/2-2ca-2(c^2-a^2)\arctan\frac{c-a}{c+a}}{4c^2},\qquad F_m=\frac{M_{m-1}-A_0F_{m-1}}{2c},$$

where $F_m$ is the same integral with the factor $x^m$, so $I_n(c)=F_{2n}$; this ball, at $768$ bits, lies inside the series enclosure. The
computation is done at $384$ and $768$ bits, which give the same rounded values. Again eight terms are kept.
For part (d) the conditions on the four further pairs are verified in exact rational arithmetic: the separations directly, and
$P_i\ge0$ on $[0,\frac34]$ from the nonnegativity of the degree-four Bernstein coefficients of $P_i$ on $256$ rational subintervals (an
independent Sturm count finds no root of any $P_i$ in $[0,\frac34]$). For these pairs $c_i+a_i<1$, and $I_n$ is enclosed in the same way from
$c_i^2+2c_ix+a_i^2=(c_i+a_i)^2\big(1-\frac{2c_i(a_i-x)}{(c_i+a_i)^2}\big)$, with ratio at most $\frac{2c_ia_i}{(c_i+a_i)^2}<1$, and checked by the same closed form.

Subtracting the savings from the best certified upper endpoints before any saving, in $384$-bit ball arithmetic and again at
$768$ bits (for Theorem 3.9 with $J$ and $K$ from their closed forms and an exact rational series for $\log\frac43$), gives:

| $\alpha$ | upper bound for $D_\alpha$ before the saving | source | saving of Theorem 3.9 at least | saving of Theorem 3.10 at least | saving of Theorem 3.10(c) at least | saving of Theorem 3.10(d) at least | new upper bound |
|---|---|---|---|---|---|---|---|
| $\frac1{20}$ | $13.6146872781$ | Theorem 3.5 | $2.62\cdot10^{-5}$ | $2.94\cdot10^{-5}$ | $3.01\cdot10^{-5}$ | $3.12\cdot10^{-5}$ | $13.6146560118$ |
| $\frac1{10}$ | $7.2859601007$ | Theorem 3.5 | $4.96\cdot10^{-5}$ | $5.56\cdot10^{-5}$ | $5.71\cdot10^{-5}$ | $5.92\cdot10^{-5}$ | $7.2859008968$ |
| $\frac15$ | $4.1826621448$ | Theorems 3.6, 3.8 | $8.81\cdot10^{-5}$ | $9.88\cdot10^{-5}$ | $1.01\cdot10^{-4}$ | $1.05\cdot10^{-4}$ | $4.1825570225$ |
| $\frac3{10}$ | $3.2167849538$ | Theorems 3.6, 3.8 | $1.15\cdot10^{-4}$ | $1.29\cdot10^{-4}$ | $1.33\cdot10^{-4}$ | $1.37\cdot10^{-4}$ | $3.2166471427$ |
| $\frac12$ | $2.6452417528$ | Theorems 3.6, 3.8 | $1.37\cdot10^{-4}$ | $1.53\cdot10^{-4}$ | $1.58\cdot10^{-4}$ | $1.63\cdot10^{-4}$ | $2.6450780506$ |
| $\frac34$ | $3.0974919455$ | Theorems 3.6, 3.8 | $1.02\cdot10^{-4}$ | $1.15\cdot10^{-4}$ | $1.18\cdot10^{-4}$ | $1.22\cdot10^{-4}$ | $3.0973694678$ |
| $\frac9{10}$ | $5.4689292769$ | Theorems 3.6, 3.8 | $4.92\cdot10^{-5}$ | $5.51\cdot10^{-5}$ | $5.66\cdot10^{-5}$ | $5.87\cdot10^{-5}$ | $5.4688705643$ |
| $\frac{99}{100}$ | $42.6816774355$ | Theorems 3.6, 3.8 | $5.41\cdot10^{-6}$ | $6.06\cdot10^{-6}$ | $6.23\cdot10^{-6}$ | $6.45\cdot10^{-6}$ | $42.6816709818$ |

Only the largest saving, that of Theorem 3.10(d), is subtracted, and the new upper bounds are the values of Table 1 at these exponents. At
$\alpha=\frac1{1000}$ and $\alpha=\frac1{100}$, Theorem 3.10(b) and (d) are applied together with Theorem 5.7(ii); the resulting values follow Theorem 5.7.
Compared with Theorem 3.9, the larger disks increase each saving by about $12$ percent, and the terms with $n\ge3$ add less than $0.05$
percent; the phase-uniform density of part (c) adds about $2.7$ percent more, and the four further disk pairs of part (d) add about
$3.5$ percent of the saving of part (c). In Theorem 3.9 the fourth-moment term contributes between $0.5$ and $1.5$ percent of each saving. The savings are small:
the coupling changes only the transport within a few small disks, while the rest of $\mu_R$ is still translated.

## 4. Rigorous lower bounds

All witnesses are built from one device.

**Lemma 4.0 (signed-distance witnesses).** Let $Z\subset\mathbb R^2$ be closed and let $\sigma$ be a sign function that is
constant on each connected component of $\mathbb R^2\setminus Z$. Then $v=\sigma\operatorname{dist}(\cdot,Z)$ is 1-Lipschitz
and $p_\alpha\circ v$, $p_\alpha(s)=2^{\alpha-1}\operatorname{sign}(s)|s|^\alpha$, has $[p_\alpha\circ v]_\alpha\le1$, with equality if
two points at equal distance from $Z$, of opposite signs, are reflections of each other across a straight piece of $Z$.
Maxima and minima of functions with $[\cdot]_\alpha\le1$ again have $[\cdot]_\alpha\le1$.

*Proof.* Equal signs: distance functions are 1-Lipschitz. Opposite signs: the segment crosses $Z$, so
$\operatorname{dist}(p,Z)+\operatorname{dist}(q,Z)\le|p-q|$. Then $|a^\alpha-b^\alpha|\le|a-b|^\alpha$ and
$2^{\alpha-1}(a^\alpha+b^\alpha)\le(a+b)^\alpha$ (concavity). The max/min statement holds because the functions are
1-Lipschitz for the metric $|p-q|^\alpha$. $\square$

If the witness $f$ satisfies $f(x)=f(y)$ at the two evaluation points, the local term of $R_1^2=T_{xx}-\frac12I$ does not
change that output increment, so every such bound for $C_\alpha$ is also a bound for $D_\alpha$. Every lower bound below
holds already for the supremum over real $f\in C_c^\infty$ (mollification and compact truncation, Section 1).

**Theorem 4.1 (two-cusp bound).** With $q=\sqrt2-1$, for $0<\alpha<1$,
$$C_\alpha\ge L_1(\alpha),\quad D_\alpha\ge L_1(\alpha),\qquad L_1(\alpha)=q^\alpha\Big(\frac4{\pi\alpha(\alpha+2)}-\frac14\Big)=\frac2{\pi\alpha}+\frac{2\log q-1}\pi-\frac14+O(\alpha).$$

*Proof.* Let $s(z)=(|z_1|-|z_2|)/\sqrt2$, $\nu=\operatorname{sign}(s)\min\{|s|,(\frac12-|z|)_+\}$, $g=p_\alpha\circ\nu$, and
$f(z)=g(z)-g(z-e_1)$; $f$ is a signed-distance witness (Lemma 4.0) with $f(0)=f(e_1)=0$. With
$S=\int K_{xx}g$ and $E=\int K_{xx}(e_1-z)g(z)dz$, the increment is $2(S-E)$. On $|z|\le r_0=1/(2+\sqrt2)$ one has
$\nu=s$, so $g$ is the exact angular extremizer of Theorem 3.1(a) and $S\ge\frac{a_2}\alpha r_0^\alpha$ (all other
contributions to $S$ are nonnegative because $K_{xx}g\ge0$). Next $\|g\|_\infty\le\frac12q^\alpha$, $0\le K_{xx}(e_1-z)\le\frac2\pi$ on
$B_{1/2}$ and $\int g=0$, so $|E|\le\frac1\pi\cdot\frac\pi4\cdot\frac12q^\alpha=\frac18q^\alpha$. Finally $2^{\alpha/2}r_0^\alpha=q^\alpha$. $\square$

**Theorem 4.2 (refined two-cusp bound).** With $b(t)=\sin t/(1+\sin t)$, $P=\frac1{15}+\frac14\log\frac{15}{16}>0$ and
$$S_\alpha=\frac2\pi\int_0^{\pi/4}\sin2t\Big[\frac{b(t)^\alpha}\alpha+\int_0^{b(t)}\frac{w^\alpha}{1-w}dw\Big]dt
=\frac4\pi\sum_{n\ge0}\frac{q^{\alpha+n+2}}{\alpha+n+2}\sum_{k=0}^n\frac{(n-k+1)(n-k+2)}{2(\alpha+k)},$$
$C_\alpha,D_\alpha\ge L_2(\alpha)=2S_\alpha-\frac{2q^\alpha}\pi P=\frac2{\pi\alpha}-\frac{1+\log2+2P}\pi+O(\alpha)$.

*Proof.* Same witness. $S$ is computed exactly in the eight sectors, where $|\nu|=\min(r\sin t,\frac12-r)$ with $t$ the
angle to the nearest diagonal. For $E$, expand $K_{xx}(e_1-z)=\frac1{2\pi}\operatorname{Re}\sum_m(m+1)z^m$ on the disc; by the
symmetries of $g$ only $m=4k+2$ survive, each angular moment is at most $4\|g\|_\infty\le2q^\alpha$, and the radial sum is
$\frac{q^\alpha}\pi\sum_k\frac{4k+3}{4k+4}16^{-k-1}=\frac{q^\alpha}\pi P$. $\square$

**Theorem 4.3 (gated witness).** Let $x=(\frac12,0)$, $c=t/\sqrt2$, $\ell=(t-1)/2$ and
$$J(t)=\frac1\pi\int_\ell^\infty\sum_{\epsilon=\pm1}\mathbf 1_{|r|+\epsilon c>0}(|r|+\epsilon c)\Big[\frac1{r^2+(|r|+\epsilon c)^2}-\frac1{(r+1)^2+(|r|+\epsilon c)^2}\Big]dr>0 .$$
Then $C_\alpha,D_\alpha\ge L_{\rm gate}(\alpha)=\alpha\int_0^\infty t^{\alpha-1}J(t)\,dt$, and
$L_{\rm gate}(\alpha)=\frac2{\pi\alpha}+\frac{\log2}\pi+O(\alpha)$ as $\alpha\to0$, $L_{\rm gate}(\alpha)=\frac{1+\sqrt2}{2\pi(1-\alpha)}+O(1)$ as $\alpha\to1$.

*Proof.* With $u(z)=p_\alpha\big((|z_1|-|z_2|)/\sqrt2\big)$ and $h(w)=2^{\alpha-1}w_1^\alpha$, put
$v(w)=\max\{-h(w),\min(u(w-x),h(w))\}$ for $w_1\ge0$, $v=0$ for $w_1<0$, and $f(w)=v(w)-v(-w)$. Lemma 4.0 gives
$[f]_\alpha\le1$ on each half-plane, and across the axis $|f(p)-f(q)|\le2^{\alpha-1}(p_1^\alpha+|q_1|^\alpha)\le|p-q|^\alpha$; also
$f(\pm x)=0$. Writing $d=|a-\frac12|-|b|$ for $w=(a,b)$, $a>0$, one has $f=\frac12\operatorname{sign}(d)\min\{\sqrt2|d|,2a\}^\alpha$, whose
layer-cake decomposition $f=\frac\alpha2\int_0^\infty t^{\alpha-1}\sigma_t\,dt$ has elementary level sets $\sigma_t$. The vertical
primitive $\int K_{xx}(s,b)db=b/(2\pi(s^2+b^2))$ reduces each level to $2J(t)$, and absolute Fubini (justified by the
$r^{\alpha-2}$ and $r^{\alpha-3}$ majorants) gives the formula. $J>0$ because $a>0$ makes the bracket positive. $\square$

**Theorem 4.4 (degree-three homogeneous witness).** With
$M_\alpha=\frac{(\alpha+1)2^{\alpha-1}}{\cos((\alpha+2)\pi/6)}\int_0^{\pi/6}\sin((\alpha+2)t)\sin^\alpha t\,dt$,
$$C_\alpha\ge2^{1-\alpha}\big(M_\alpha+\tfrac14\big),\qquad D_\alpha\ge2^{1-\alpha}M_\alpha ,$$
and $2^{1-\alpha}M_\alpha=\frac{3\sqrt3}{4\pi(1-\alpha)}+O(1)$ as $\alpha\to1$.

*Proof.* $f_\alpha=p_\alpha\circ u_3$ with $u_3$ the signed distance to the zero lines of $\cos3\theta$ (Lemma 4.0, $[f_\alpha]_\alpha=1$),
$f_\alpha=r^\alpha F_\alpha(\theta)$, $f_\alpha(\pm e_1)=\pm\frac12$. With $\beta=\alpha+2$, solve $g''+\beta^2g=F_\alpha$ on $[0,\pi/6]$, $g'(0)=0$,
$g(\pi/6)=0$ ($\cos(\beta\pi/6)>0$), extend by the symmetries of $F_\alpha$ to a $C^{2,\alpha}$ function, and put
$U=-r^\beta g(\theta)$, so $-\Delta U=f_\alpha$. Then $V=\partial_{11}U$ is homogeneous of degree $\alpha$ and globally Hölder, and
$R_1^2f_\alpha-V$ is harmonic with $O(1+|x|^\alpha)$ growth, hence constant. So $R_1^2f_\alpha(e_1)-R_1^2f_\alpha(-e_1)=2V(e_1)=2M_\alpha$
with $|2e_1|^\alpha=2^\alpha$, which gives the $D$ bound, and $T_{xx}=R_1^2+\frac12I$ adds $\frac12(f_\alpha(e_1)-f_\alpha(-e_1))=\frac12$. The
asymptotics follow from $\cos((\alpha+2)\pi/6)\sim\frac\pi6(1-\alpha)\sin\frac\pi2$ and $\int_0^{\pi/6}\sin3t\sin t\,dt=\frac{\sqrt3}{16}$. $\square$

**Theorem 4.5 (polygonal signed-distance witness).** For $a>0$ let $Z_a$ be the union of the horizontal axis, the
vertical segments from $(0,0)$ to $(0,a)$ and from $(1,0)$ to $(1,a)$, the rays from $(0,a)$ in direction $120^\circ$ and
from $(1,a)$ in direction $60^\circ$, and the images of these pieces under $(x,y)\mapsto(1-x,-y)$. In the upper half-plane give
sign $-1$ to the component between the two broken lines and $+1$ to the two outer components, and extend the sign oddly
under the same point reflection. For $f_{\alpha,a}=p_\alpha\circ(\sigma\operatorname{dist}(\cdot,Z_a))$ and the $T_{xy}$ increment
between $e_1$ and $0$,
$$C_\alpha,\ D_\alpha\ \ge\ I(\alpha,a)=2^{\alpha-1}\alpha\int_0^\infty t^{\alpha-1}J_a(t)\,dt ,$$
where $J_a(t)>0$ is an explicit elementary function obtained by integrating the kernel increment
$\nu(x,y)=K_{xy}(x-1,y)-K_{xy}(x,y)$ over the eroded components $\{\operatorname{dist}(\cdot,Z_a)>t\}$ (convex polygons and one region
bounded by a segment, a circular arc of radius $t$ and a ray), using the horizontal primitive of $\nu$. Because $J_a>0$,
the integral over any finite $t$-interval is a rigorous lower bound. The logarithmic singularity of $J_a$ at $t=0$ is integrated exactly and the range $t\to\infty$ is treated by a
reciprocal substitution, so the full integral, both tails included, is enclosed by interval arithmetic (160-bit
balls, $1.2\times10^5$ to $6\times10^5$ logarithmic cells). With the shape optimized separately at each exponent this gives the
lower bounds of Table 1, for example

$$C_{1/2},\ D_{1/2}\ \ge\ 2.0891556369\quad(a=0.465),\qquad C_{3/10},\ D_{3/10}\ \ge\ 2.6996050307\quad(a=0.524).$$

As $t\to0$, $J_a(t)=-\frac4\pi\log t+j_0(a)+O(t)$ with $j_0(a)=\frac1\pi\big[\sqrt3\arctan\frac1a-\frac12\log(1+a^{-2})-2\log2\big]$, so

$$I(\alpha,a)=\frac2{\pi\alpha}+\kappa(a)+o(1),\qquad \kappa(a)=\frac1{2\pi}\Big[\sqrt3\arctan\frac1a-\frac12\log(1+a^{-2})+2\log2\Big].$$

Since $\kappa'(a)$ has the sign of $\frac1a-\sqrt3$, $\max_a\kappa=\kappa(1/\sqrt3)=\frac1{2\sqrt3}+\frac{\log2}{2\pi}=0.3989929346\ldots$, which is
$0.0033$ below the sharp $C_0=0.4023257\ldots$ (Theorem 5.4). The $\alpha\to1$ coefficient of $I(\alpha,a)$ is the sharp
$\frac{3\sqrt3}{4\pi}$ for every $a>0$. (The polygonal construction and its first numerical evaluations came from the numerical
part of the project. The one-dimensional reduction, the endpoint regularization and the certificates were obtained
independently.)

*Proof.* Lemma 4.0 gives $[f_{\alpha,a}]_\alpha\le1$, and $f_{\alpha,a}(0)=f_{\alpha,a}(e_1)=0$. The layer-cake formula and the exact
eroded level sets (each component is either an intersection of half-planes, or bounded by the inward offsets of a segment,
a corner arc and a ray) give the formula; positivity of $J_a$ follows from the slice formula. The full derivation and the
interval code are in the accompanying artifacts. $\square$

**Combined finite-$\alpha$ lower bound.** $L(\alpha)=\max\{L_1,L_2,L_{\rm gate},2^{1-\alpha}(M_\alpha+\frac14),\sup_aI(\alpha,a)\}$
bounds $C_\alpha$. Since $C_\alpha\le D_\alpha$ (identity 2), it also bounds $D_\alpha$. At every exponent of Table 1 the
largest certified member is the polygonal witness with an optimized shape. For example, at $\alpha=\frac12$ the gated
bound is $1.8996$ and the polygonal bound $2.0892$. At $\alpha=0.99$ the degree-three bound is $41.7628$ and the
polygonal bound $42.0029$.

**Theorem 4.6 (a finite-exponent projection witness for $D_\alpha$; strict separation $C_\alpha<D_\alpha$).** Let either
(i) $0<\alpha\le\frac14$, $0<a\le1$ and $0<\rho\le a/6$, or (ii) $0<\alpha\le\frac12$, $a>0$ and $0<\rho\le\min\{1,a/7\}$. Use coordinates $z=(X,Y)$ centred at the midpoint of the two
evaluation points $x=(\frac12,0)$ and $y=-x$. Let $\Gamma_a=\{(b_a(Y),Y):Y\in\mathbb R\}$ with
$b_a(Y)=\frac12+(|Y|-a)_+/\sqrt3$ (a vertical segment through $x$ of half-height $a$, continued by two rays), let $s_a$ be
the signed distance to $\Gamma_a$, positive on its right, and put $V=(s_a,Y)$, $\Pi=2|s_aY|/|V|$ ($\Pi=0$ at $V=0$). On
$\{X>0\}$ define

$$F=-\tfrac12+\tfrac12\min(|V|,\rho)^\alpha+\tfrac12\operatorname{sgn}(s_aY)\,\Pi^\alpha,\qquad h=\tfrac12(2X)^\alpha,\qquad
f=\max(-h,\min(h,F)),$$

extend $f$ oddly under $z\mapsto-z$, and set $f=0$ on $\{X=0\}$. With $k=1/(1-\alpha)$, $A(u)=(1-u)^{-\alpha}$ and
$B(u)=\big(\frac{1+u^{\alpha k}}2\big)^{1/k}+\frac{1-u^\alpha}{2(1-u)^\alpha}$, let
$K_\alpha=\max\{1,\sup_{0<u<1}\min(A(u),B(u))\}$. Then $K_\alpha<\infty$ ($K_\alpha\le1+2\alpha^2$ if $\alpha\le\frac14$), $[f]_\alpha\le K_\alpha$, $f(x)=-\frac12$,
$f(y)=\frac12$, and

$$D_\alpha\ge\frac{J_\alpha(a,\rho)+\frac12}{K_\alpha},\qquad
J_\alpha(a,\rho)=2\int_Q\nu(X,Y)\operatorname{sgn}(s_a(X,Y))\,M(X,Y)\,dX\,dY,$$

where $Q$ is the open first quadrant, $\nu(z)=K_{xy}(z-x)-K_{xy}(z-y)$, and, with $P=\Pi^\alpha$, $H=(2X)^\alpha$,
$B_\rho=\min(|V|,\rho)^\alpha$,

$$M=\max\Big(0,\min\Big(P,\ H,\ \frac{P+H+B_\rho-1}2\Big)\Big).$$

The integral converges absolutely. For $a=1$ and $\rho=\frac16$ the certified values are

$$\boxed{\begin{aligned}&C_{1/1000}\le637.0245603580<637.3340501785\le D_{1/1000},\qquad C_{1/100}\le64.0881631620<64.3702681064\le D_{1/100},\\
&C_{1/20}\le13.1839509406<13.4165946841\le D_{1/20},\qquad C_{1/10}\le6.8511402022<7.0259799882\le D_{1/10},\\
&C_{1/5}\le3.7431650122<3.8088065348\le D_{1/5}.\end{aligned}}$$

The separations $D_\alpha-C_\alpha$ are at least $0.3094$, $0.2821$, $0.2326$, $0.1748$ and $0.0656$. These are the first finite exponents in
this investigation at which $D_\alpha$ and $C_\alpha$ are proved to differ. In range (ii), with $a=\frac32$ and $\rho=\frac3{14}$, and
with the profile factor $K^*_{3/10}\le1.007$ (see after the proof) in place of $K_{3/10}$,

$$\boxed{C_{3/10}\le2.7726584812<2.8051718212\le D_{3/10},}$$

so $D_{3/10}-C_{3/10}\ge0.0325$. The upper bound is the one of Theorem 3.8. With $K_{3/10}$ itself and a coarser integration the
same witness gives $D_{3/10}\ge2.7212438248$.

*Proof.* Seminorm. In the ball $B(x,\sqrt3a/2)$ the nearest point of $\Gamma_a$ lies on the vertical segment, so $V(z)=z-x$
there; for an oblique ray the projection would lie beyond the ray's endpoint (Cauchy-Schwarz). In this ball $F$ is the
frozen planar projection profile $\min\{g,\frac12\rho^\alpha+\frac12\operatorname{sgn}(S)|S|^\alpha\}-\frac12$ of Theorem 5.6,
with $S(u)=2u_1u_2/|u|$. The second function in the minimum has seminorm at most one. For $g$, every pair has quotient
at most one except opposite-sign pairs whose negative point has the smaller radius. After normalizing the larger radius
to one and calling the smaller one $u$, the range bound $g(p)\le1$, $g(q)\ge0$, $|p-q|\ge1-u$ gives $A(u)$. The inequality
$\sin2a+\sin2b\le2|p-q|$ together with the exact weighted power-mean maximization of Theorem 5.6, Step 1, gives $B(u)$. Hence
$[g]_\alpha\le K_\alpha$. Away from the frozen set, $F$ equals the outer profile
$H_o=-\frac12+\frac12\rho^\alpha+\frac12\operatorname{sgn}(S(V))|S(V)|^\alpha$. Its seminorm is at most one for
$\alpha\le\frac23$: for equal signs $S\circ V$ is $2\sqrt2$-Lipschitz, and for opposite signs the segment meets the zero set
$\Gamma_a\cup\{Y=0\}$, while $\Pi\le2\operatorname{dist}(\cdot,\Gamma_a\cup\{Y=0\})$. A mixed pair has $|V(p)|\le\rho$, which
forces $|p-x|\le\rho$, and $|q-x|\ge5\rho$. In the only adverse ordering its quotient is at most
$\frac12\big(4^{-\alpha}+(5/2)^\alpha\big)$. This is convex in $\alpha$, equals one at $\alpha=0$ and is below one at $\alpha=\frac14$. In the
other ordering, $F\le H_o$ and $F(q)=H_o(q)$ give the bound directly. Clamping to $[-h,h]$ preserves the seminorm (lattice
property, $[h]_\alpha\le1$). For pairs on opposite sides of $\{X=0\}$, the odd extension gives
$|f(w)-f(z)|\le h(w)+h(-z)\le(X_w+|X_z|)^\alpha\le|w-z|^\alpha$ by concavity, exactly as in Theorem 5.5. Finally,
$K_\alpha\le1+2\alpha^2$ by Step 1 of Theorem 5.6: $A(u)\le(1-\alpha)^{-\alpha}\le1+2\alpha^2$ for $u<\alpha$ and $B(u)\le1+\alpha^2$ for $u\ge\alpha$.

Range (ii). The argument is the same, with three changes. First, the same-quadrant estimates for $g$ extend to
$\alpha\le\frac12$. If the distance $D$ of the pair is at most the smaller radius, the quotient is at most $(\alpha+2^\alpha)/2<1$. If
$D$ exceeds it and the quadrant is positive, $(1+t)^\alpha-\frac12t^\alpha\le1+\alpha t-\frac12t^\alpha\le1$ for $0<t\le1$, because
$\alpha t\le\frac t2\le\frac12t^\alpha$. The opposite-sign bounds $A(u)$ and $B(u)$ hold for every $\alpha<1$. Second, $6/7<\sqrt3/2$, so
$V(z)=z-x$ on $B(x,6\rho)$ and a mixed pair has $|q-x|\ge6\rho$. Its quotient in the adverse ordering is at most
$\frac12\big(5^{-\alpha}+(12/5)^\alpha\big)$, which is convex in $\alpha$, equals one at $\alpha=0$ and equals $(1+2\sqrt3)/(2\sqrt5)<1$ at
$\alpha=\frac12$ (equivalently $4\sqrt3<7$). Third, $\rho\le1$ gives $B_\rho\le1$, which is what the clamp-amplitude formula below
needs. $K_\alpha$ is finite because $A(u)\to1$ as $u\to0$ and $B(u)\to1$ as $u\to1$.

Value. Write $f(X,\pm Y)$ as the clamps to $[-\frac H2,\frac H2]$ of $-\frac{1-B_\rho}2\pm\frac P2$ (for $s_a>0$). The
difference of two clamped values is the length of the clamped interval, and this gives
$f(X,Y)-f(X,-Y)=\operatorname{sgn}(s_a)M$ on $Q$. Central oddness and the reflection $Y\mapsto-Y$, under which $\nu$ is odd,
reduce $T_{xy}f(x)-T_{xy}f(y)$ to $J_\alpha$. Since $f(x)-f(y)=-1$, the identity term of $T_{xy}-\frac12I$ adds $\frac12$.
Rotation by $\pi/4$ carries $T_{xy}-\frac12I$ to a rotated copy of $R_1^2$, with the same norm $D_\alpha$ (Section 1). Dividing
by $[f]_\alpha\le K_\alpha$ proves the lower bound. At the pole, $M=O(|z-x|^\alpha)$; at infinity, $|f|\le\frac12(2|z|)^\alpha$ and
$\nu=O(|z|^{-3})$. So $J_\alpha$ converges absolutely.

Certification. Put $\delta=\frac1{24}$ and $R=4096$. In the upper half of $B(x,\delta)$ one has $V=z-x$ and $B_\rho=r^\alpha$, and
the cap $H$ does not reduce $P$. The third argument of the minimum gives $M\ge P-\alpha r/(1-2\delta)$. Hence the local part
of $J_\alpha$ is at least

$$\frac{2A_\alpha\delta^\alpha}\alpha-\frac{2\alpha\delta}{\pi(1-2\delta)}-\frac{2(1+\delta)\delta^{\alpha+3}}{(1-\delta)^4(\alpha+3)}.$$

The part with $|z-x|>R$, after central reflection, lies in $\{|z|>L\}$ with $L=R-\frac12$. There
$|\nu(z)|\le|z|/(\pi(|z|^2-\frac14)^2)$, so its absolute value is at most
$2^\alpha L^{\alpha-1}/\big((1-\alpha)(1-1/(4L^2))^2\big)$. The remaining compact integral, over $\delta\le|z-x|\le R$ in $Q$, is
enclosed in the coordinates $u=\log|z-x|$ and $t=\theta/\theta_{\max}(r)$, where $\theta_{\max}=\pi$ for $r\le\frac12$ and
$\arccos(-1/(2r))$ otherwise. It uses three radial patches $[\delta,\frac12]$, $[\frac12,2]$ and $[2,R]$, each with $1024\times1024$
rectangles. On every rectangle, 160-bit ball arithmetic encloses the kernel, the distances to the segment and both
rays, the clamp amplitude $M$ (by its symmetric hull when the rectangle meets $\Gamma_a$) and the Jacobian. No rectangle is
discarded. At $\alpha=0.3$ the local radius is $\delta=\frac3{56}$ instead of $\frac1{24}$, and for the separation each patch uses
$2048\times2048$ rectangles ($12582912$ in all); the compact integral is then enclosed in $[1.5313375386,1.5886775389]$, and an
independent Gaussian evaluation, not used for the certificate, gives $1.5600784065$. $K_\alpha$ is enclosed by a one-dimensional
certificate on rational cells, with explicit bounds for the two endpoint intervals of $u$. To avoid cancellation in $B(u)$
near $u=1$, a second certificate uses the smaller of $B(u)$ and a positive-term upper bound for it, obtained from a midpoint
Taylor bound for $t^k$ on $[u,1]$; any upper bound for $\min(A,B)$ is admissible. The values used are
$K_{1/1000}\le1.000000240308$, $K_{1/100}\le1.000024085602$, $K_{1/20}\le1.000608619784$, $K_{1/10}\le1.002471319750$,
$K_{1/5}\le1.010555855930$ and $K_{3/10}\le1.026981110219$. The final endpoints were recomputed independently in 90-digit
arithmetic from the adverse regular endpoints (at $\alpha=0.3$ with the factor $1.007$: $2.80517183631\ldots$). The upper bounds for $C_\alpha$ are the best values of Table 1: Theorem 5.7(ii) at $\alpha=\frac1{1000}$ and Theorem 3.7 with the phase interpolation of Theorem 3.8 at the other five exponents. $\square$

The witness is the polygonal analogue of the witness of Theorem 5.6. There the graph is the sign-change curve of $\nu$
and $\rho=\alpha$. The certified compact integrals have interval radius about $0.06$ with $1024^2$ rectangles per patch and
$0.029$ with $2048^2$, so finer rectangles raise the lower bounds by roughly that amount. At $\alpha=0.3$ a floating-point
evaluation of the same witness, divided by $1.007$, gives about $2.834$.

*The profile factor.* $K_\alpha$ bounds the seminorm of the frozen profile through the one-dimensional reduction above. The
exact seminorm $K^*_\alpha$ of the profile is smaller. All pair classes except opposite-sign pairs (points in adjacent quadrants, where $S$ has
opposite signs) have quotient at most one for $\alpha\le\frac12$, and after the symmetries and a dilation the opposite-sign quotient is

$$\frac{1-u^\alpha+\sin(2a)^\alpha+u^\alpha\sin(2b)^\alpha}{2(1+u^2-2u\cos(a+b))^{\alpha/2}},\qquad 0<u<1,\quad a,b\in[0,\tfrac\pi2].$$

A complete covering of this box by rational subboxes (1926349 at $\alpha=0.3$, 1331983 at $\alpha=\frac12$), with monotone bounds for
the numerator, the convex radial minimization of the denominator, explicit endpoint estimates and 160-bit ball
arithmetic, proves $K^*_{3/10}\le1.007$ and $K^*_{1/2}\le1.021$. Since every other part of the seminorm proof of Theorem 4.6
gives quotient at most one, $[f]_\alpha\le\max(1,K^*_\alpha)$, so either factor may replace $K_\alpha$ in Theorem 4.6; the separation at
$\alpha=0.3$ uses $1.007$. At $\alpha=\frac12$ the floating-point value of the witness
with $a=\frac32$, $\rho=\frac3{14}$ is about $1.90$, below $L(\frac12)$.


**Theorem 4.7 (half-plane lattice witnesses for $D_\alpha$; strict separation at $\alpha=\frac12,\frac34,\frac9{10},\frac{99}{100}$).** Use coordinates
centered at the midpoint of the poles: $x=(\frac12,0)$, $y=-x$, $H=\{X>0\}$, $h(X,Y)=\frac12(2X)^\alpha$, and for a phase $\phi$ let
$\nu_\phi(z)=K_\phi(z-x)-K_\phi(z-y)$ with $K_\phi(w)=\operatorname{Re}(e^{i\phi}/w^2)/(2\pi)$.

(i) If $F:H\to\mathbb R$ has $[F]_{\alpha,H}\le1$ and $F(x)\le-\frac12$, let $f=\max(-h,\min(h,F))$ on $H$, $f(-z)=-f(z)$, and $f=0$ on
$X=0$. Then $[f]_\alpha\le1$, $f(x)=-\frac12$, $f(y)=\frac12$, and for every $\phi$

$$D_\alpha\ \ge\ 2|J_\phi|+\tfrac12,\qquad J_\phi=\mathrm{p.v.}\int_H\nu_\phi f,$$

where the principal value deletes disks centered at $x$. For $\phi=0$ the half-plane mass is
$\mathrm{p.v.}\int_H\nu_0=-\frac12$, so $J_0=\int_H\nu_0\,(f-f(x))+\frac14$ with an absolutely convergent integral.

(ii) For $b>0$ let $B(X)=\frac12-X$ on $(0,\frac12]$, $B(X)=X-\frac12$ on $[\frac12,\frac12+b]$ and $B(X)=(X-\frac12+(\sqrt3-1)b)/\sqrt3$ for
$X\ge\frac12+b$. Let $Z\subset\overline H$ be the vertical axis together with the graphs $Y=\pm B(X)$, let $\sigma=+1$ where $|Y|<B(X)$ and
$\sigma=-1$ elsewhere in $H\setminus Z$, and put $F=2^{\alpha-1}\sigma\operatorname{dist}(\cdot,Z)^\alpha-\frac12$. Then $F$ satisfies (i), and

$$D_{3/4}\ \ge\ 2.7572557572\quad(b=\tfrac34),\qquad D_{9/10}\ \ge\ 5.1886577849\quad(b=\tfrac7{20}),\qquad D_{99/100}\ \ge\ 42.3800881920\quad(b=1).$$

(iii) With $g=2^{\alpha-1}\sigma\operatorname{dist}(\cdot,Z)^\alpha$ as in (ii) for $b=\frac34$ and the sector cusp
$P_s=\big((|X-\frac12|-|Y|)_+/\sqrt2\big)^\alpha$, the function $F=\min(g-\frac3{10},\,-\frac12+P_s)$ satisfies (i), and

$$D_{1/2}\ \ge\ 2.2856680189.$$

(iv) Let $P(u,v)=\frac12\big[(u^2+v^2)^{\alpha/2}+\operatorname{sgn}(u^2-v^2)\big(|u^2-v^2|/\sqrt{u^2+v^2}\big)^\alpha\big]$ and $P(0,0)=0$.
This is the frozen projection profile of Theorems 4.6 and 5.6 rotated by $\frac\pi4$, so $[P]_{1/2}\le K^*_{1/2}\le\frac{1021}{1000}$ (see
after the proof of Theorem 4.6). With $g$ as in (iii) ($b=\frac34$), the function
$F=\min\big(g-\frac3{20},\,-\frac12+\frac{1000}{1021}P(X-\frac12,Y)\big)$ satisfies (i), and

$$D_{1/2}\ \ge\ 2.4378062352.$$

(v) Let $\alpha=\frac3{10}$, let $g$ be as in (ii) with $b=\frac32$, and let $P$ be as in (iv). Then $[P]_{3/10}\le K^*_{3/10}\le\frac{1007}{1000}$
(see after the proof of Theorem 4.6), the function $F=\min\big(g,\,-\frac12+\frac{1000}{1007}P(X-\frac12,Y)\big)$ satisfies (i), and

$$D_{3/10}\ \ge\ 2.9418686222.$$

(vi) Let $\alpha=\frac34$, let $g$ be as in (iii) ($b=\frac34$), and let $P$ be as in (iv). Then $[P]_{3/4}\le\frac{53}{50}$, the function
$F=\min\big(g-\frac3{10},\,-\frac12+\frac{50}{53}P(X-\frac12,Y)\big)$ satisfies (i), and

$$D_{3/4}\ \ge\ 2.8821844092.$$

(vii) Let $P$ be as in (iv), let $g=2^{\alpha-1}\sigma\operatorname{dist}(\cdot,Z)^\alpha$ with $Z$ and $\sigma$ as in (ii), and let $(\alpha,b,c,\lambda)$ be $(\frac12,\frac34,-\frac3{20},\frac{1000}{1021})$,
$(\frac34,\frac34,-\frac3{10},\frac{50}{53})$ or $(\frac9{10},\frac7{20},-\frac3{10},\frac{10}{11})$; the first two are the witnesses of (iv) and (vi). Then
$[P]_{9/10}\le\frac{11}{10}$, the function $F=\min\big(g+c,\,-\frac12+\lambda P(X-\frac12,Y)\big)$ satisfies (i), and

$$D_{1/2}\ \ge\ 2.4542144708,\qquad D_{3/4}\ \ge\ 2.8948343532,\qquad D_{9/10}\ \ge\ 5.2413008171.$$

The tail of the integral has an explicit homogeneous limit: with $f$ as in (i), $H_b=\sqrt{(b+\frac12)^2+b^2}$,
$\beta=\max(H_b^\alpha+|c|,\frac12+2^{-\alpha})$ and $q=\frac1{4R^2}$, for every $R>\frac12$

$$\Big|\int_{|z|>R}\nu_0f\,dz-\frac{2a_3(\alpha)R^{\alpha-1}}{1-\alpha}\Big|\ \le\ \frac{2\beta}{R(1-q)^2}+\frac{R^{\alpha-3}}{2(3-\alpha)(1-q)^2},$$

and this holds for every $b>0$, real $c$ and $\lambda\ge0$ with $\lambda[P]_\alpha\le1$ and $\lambda(1+2^{-\alpha})\ge1$. The right side may be
replaced by $\frac{4\beta}{\pi R}+\frac{\beta}{3R^3(1-q)^2}+\frac{R^{\alpha-3}}{2(3-\alpha)(1-q)^2}$. The pole disks have an explicit main term: for
$\lambda>0$ with $\lambda[P]_\alpha\le1$ and $0<\epsilon<\frac12$ with $(\lambda+2^{\alpha-1})\epsilon^\alpha\le c+\frac12$ and $\lambda\epsilon^\alpha\le\frac12$, let
$A_\alpha$ be as in Theorem 3.2, put $C_\epsilon=(1-2\epsilon)^{\alpha-1}$ and

$$M=\frac{\lambda A_\alpha\epsilon^\alpha}\alpha+\frac{\epsilon^2}4,\quad E_c=\frac{\alpha C_\epsilon^3\epsilon^{3-2\alpha}}{6\pi\lambda^2(3-2\alpha)},\quad E_b=\frac{\alpha C_\epsilon\epsilon}\pi,\quad E_s=\frac{\epsilon^{\alpha+2}}{(\alpha+2)(1-\epsilon)^2};$$

then $J_\epsilon=\mathrm{p.v.}\int_{|z-x|<\epsilon}\nu_0f\,dz$ satisfies $M-E_c-E_s\le J_\epsilon\le M+E_b+E_s$. If moreover
$\alpha C_\epsilon\epsilon^{1-\alpha}\le\frac\lambda2$, then $J_\epsilon\le M+E_s$.

(viii) Let $g$ be as in (ii) with $b=\frac38$, let $P$ be as in (iv), and let $(\alpha,\lambda,c)$ be $(\frac1{10},\frac{1000}{1003},-\frac1{40})$,
$(\frac15,\frac{1000}{1011},-\frac1{20})$ or $(\frac3{10},\frac{1000}{1007},-\frac1{20})$. Then $\lambda[P]_\alpha\le1$ ($[P]_{1/10}\le K_{1/10}\le\frac{1003}{1000}$ and
$[P]_{1/5}\le K_{1/5}\le\frac{1011}{1000}$ by the proof of Theorem 4.6, and $[P]_{3/10}\le K^*_{3/10}\le\frac{1007}{1000}$ as in (v)), the
function $F=\min\big(g+c,\,-\frac12+\lambda P(X-\frac12,Y)\big)$ satisfies (i), and

$$D_{1/10}\ \ge\ 7.0445434786,\qquad D_{1/5}\ \ge\ 3.9578692464,\qquad D_{3/10}\ \ge\ 3.0161919859.$$

With Table 1, $C_{1/2}\le2.1934098609<D_{1/2}$, $C_{3/4}\le2.6387679109<D_{3/4}$, $C_{9/10}\le5.0066105983<D_{9/10}$ and
$C_{99/100}\le42.2175842339<D_{99/100}$; $D_\alpha-C_\alpha\ge0.2608$, $0.2560$, $0.2346$ and $0.1625$. With $C_{3/10}\le2.7726584812$, part (viii)
gives $D_{3/10}-C_{3/10}\ge0.2435$, against $0.1692$ from part (v) and $0.0325$ from Theorem 4.6; with $C_{1/5}\le3.7431650122$ part (viii) gives
$D_{1/5}-C_{1/5}\ge0.2147$, against $0.0656$ from Theorem 4.6; and with $C_{1/10}\le6.8511402022$ it gives $D_{1/10}-C_{1/10}\ge0.1934$, against
$0.1748$ from Theorem 4.6.

*Proof.* (i) Since $|s^\alpha-t^\alpha|\le|s-t|^\alpha$ for $s,t\ge0$, $[h]_{\alpha,H}\le2^{\alpha-1}\le1$, and pointwise minima and
maxima of functions with seminorm at most one have seminorm at most one. So $[f]_{\alpha,H}\le1$ and $|f|\le2^{\alpha-1}X^\alpha$. For
$p\in H$, $q\in-H$, concavity gives $|f(p)-f(q)|\le2^{\alpha-1}(X_p^\alpha+|X_q|^\alpha)\le(X_p+|X_q|)^\alpha\le|p-q|^\alpha$; points on the axis
are similar. At $x$, $h=\frac12$ and $F\le-\frac12$, so $f(x)=-\frac12$, and $f(y)=\frac12$ by oddness. The kernel difference is
$O(|z|^{-3})$ at infinity, and near $x$ the singular term against $f-f(x)$ is absolutely integrable, while the constant
$f(x)$ integrates to zero over centered annuli; so $J_\phi$ exists. Both $\nu_\phi$ and $f$ are odd, so the full increment of
$T_\phi$ is $2J_\phi$. $T_\phi-\frac12I$ and $T_\phi+\frac12I=-(T_{\phi+\pi}-\frac12I)$ are rotation conjugates of $\pm R_1^2$ and have
norm $D_\alpha$; their increments are $2J_\phi\pm\frac12$ because $f(x)-f(y)=-1$, and the larger absolute value is
$2|J_\phi|+\frac12$. The half-plane mass follows from the strip identity: $T_{xx}$ acts as $-\frac12$ on functions of $X$ alone.

(ii) $\sigma\operatorname{dist}(\cdot,Z)^\alpha$ has seminorm at most $2^{1-\alpha}$ on $H$ (for points of opposite sign the two distances
add up to at most their separation), so $[F]_{\alpha,H}\le1$, and $F(x)=-\frac12$. For $X,Y>0$ put
$V(X,Y)=-\frac1{2\pi}\operatorname{Im}\big[((X+iY)^2-\frac14)^{-1}\big]>0$; then $\nu_0=\partial_YV$. Integrating by parts in $Y$ and
decomposing $f$ into its level sets, whose boundaries consist of straight segments and circular arcs with explicit
primitives of $V$, gives $R_1^2f(x)-R_1^2f(y)=1+2(J_++J_{\rm mid}+J_-)$ with three one-dimensional integrals of nonnegative
functions. Lower enclosures on $131072$ cells per integral in 256-bit ball arithmetic, omitting only nonnegative tails,
give the values at $\frac34$ and $\frac9{10}$. At $\frac{99}{100}$ the omitted tails are not small: the two level integrals are taken over
$\log t\in[-20,900]$ instead of $[-20,30]$, and each of the three integrals uses $2097152$ cells. (iii) $P_s$ is the $\alpha$-th power of the distance to the closed sector
$\{|Y|\ge|X-\frac12|\}$, so $[P_s]\le1$, and $P_s(x)=0$; the minimum of two functions with seminorm at most one has seminorm at
most one. The function $f$ is even in $Y$ and nonincreasing in $|Y|$ for fixed $X$, so the increment equals
$1+4\int_0^\infty\!\int_0^\infty V\,dm_X\,dX$ with the positive Stieltjes measures $m_X((u,v])=f(X,u)-f(X,v)$; for this $f$ the inner
integrals reduce to explicit integrals of $V$ along line segments and circular arcs, and the same 256-bit procedure gives the value.
(iv) $\frac{1000}{1021}P(\cdot-x)$ has seminorm at most one and vanishes at $x$, so $F$ satisfies (i). The profile $P$ is nonincreasing
in $|Y|$ (this is part of the seminorm proof of the profile), and so is $g$; minima and the clamp preserve this, so the same
positive formula $1+4\int_0^\infty\!\int_0^\infty V\,dm_X\,dX$ holds. It is bounded below by finite Stieltjes sums. On disjoint strips
$X=\frac12\pm d$, $d\in[d_l,d_r]$ ($32768$ logarithmic strips for each sign), and at ratios $0<v_0<\dots<v_{256}$, outward arithmetic gives
$A_j\le f(X,dv_j)-f(X,dv_{j+1})$ with $A_j\ge0$ and $B_j\le\min(V(X,dv_j),V(X,dv_{j+1}))$, uniformly for $d$ in the strip. Since $V(X,\cdot)$
is unimodal on $(0,\infty)$, its minimum on $[dv_j,dv_{j+1}]$ is at an endpoint, so the strip contributes at least $(d_r-d_l)\sum_jA_jB_j$.
Every omitted strip, interval and tail contributes a nonnegative amount. The sums were evaluated in ball arithmetic (192-bit pieces, recombined at 256 bits), with
the exact distances to the polygon pieces and exact integer coverage checks; independent 60-digit point evaluations at $14400$
points agree with the interval enclosures. The primitives were cross-checked against direct quadratures to 65 digits, and floating-point
values of the same functional from a separate two-dimensional quadrature agree ($2.75844$ at $\alpha=\frac34$, $5.19435$ at
$\alpha=\frac9{10}$). For the witness of (iv) these Stieltjes sums give $2.3869631120$; the stated bound comes from a direct enclosure of the
full increment $2J_0=\mathrm{p.v.}\int\nu_0f$. The two open disks of radius $\frac12$ about the poles are covered by polar cells centered at the
poles (radii from $10^{-6}$ to $\frac12$), and their complement by polar cells centered at the midpoint (radii from $10^{-2}$ to $10^8$). On a
cell $Q$ with centroid $z_c$, $r_Q\ge\max_Q|z-z_c|$, the integral of $\nu_0f$ (of $K_0(z-x)(f-f(x))$ and $K_0(z-y)f$ separately in the
disk about $x$) is enclosed by the centroid value with error $|Q|(\sup_Q|\nu_0|\,r_Q^\alpha+|f(z_c)|\sup_Q|\nabla\nu_0|\,r_Q)$, which uses only
$[f]_\alpha\le1$. Where every branch of the minimum and the clamp is certified unique and smooth on $Q$ (strictly separated center
values, unique nearest polygon piece, angular range off the diagonals of $P$), the error is $\frac12\mathcal H\int_Q|z-z_c|^2$ instead, with
explicit Hessian bounds $\mathcal H$ for the kernel, the profile $P$ and the distance functions. Cells straddling a disk boundary at the
last refinement level are enclosed symmetrically by $|Q|\sup|\nu_0f|$. The omitted pole disks, the region of radius below $10^{-2}$
about the midpoint outside both disks, and the exterior of radius $10^8$ contribute at most $2\cdot0.0020001$, $1.03\cdot10^{-7}$ and
$2.83\cdot10^{-4}$, by $|f-f(x)|\le|z-x|^\alpha$, $|\nu_0|\le4/\pi$ on the disk complement and the dipole decay of $\nu_0$. With
$4009444$ cells in 80-bit ball arithmetic and exact rational recombination, $2J_0\in[1.9378062,1.9717699]$, so
$D_{1/2}\ge2|J_0|+\frac12\ge2.4378062352$. (v) The argument of (iv) applies verbatim: $\frac{1000}{1007}P(\cdot-x)$ has seminorm at most one at $\alpha=\frac3{10}$ and
vanishes at $x$, and $g$ vanishes at $x$, so $F(x)=-\frac12$; the monotonicity in $|Y|$ is unchanged. The same lower Stieltjes sums,
with $32768$ logarithmic strips for each sign ($\log d\in[-18,24]$ for $X>\frac12$ and $\log d\in[-18,\log\frac12]$ for $X<\frac12$) and
$256$ ratio intervals with $\log v\in[-12,14]$, give a lower endpoint at least $2.94186862221$. The chunked sums were recombined
independently as exact rational intervals, with complete coverage and source-hash checks.
(vi) The bound $[P]_{3/4}\le\frac{53}{50}$ comes from the complete pair reduction of the profile (the equal-sign and the
opposite-sign pair classes, with power-mean estimates at the endpoints of the parameter domains) and exhaustive exact rational
bisection covers of the two compact parameter domains in 192-bit outward arithmetic ($2620$ and $282604$ accepted boxes; the
endpoint bounds are $1.0000000075$ and $1.00375$). So $\frac{50}{53}P(\cdot-x)$ has seminorm at most one and vanishes at $x$, and $F$
satisfies (i) as in (iv). The value is enclosed by the cell method of (iv), with polar cells about the poles for radii in $[10^{-6},\frac12]$
and about the midpoint for radii in $[10^{-2},10^{16}]$, the same three analytic remainder bounds for the omitted regions, $9078024$
cells in $456$ tasks, and exact rational recombination: $2J_0\in[2.3821844,2.4089789]$, so $D_{3/4}\ge2.8821844092$. The whole
computation was replayed independently from frozen sources.
(vii) The bound $[P]_{9/10}\le\frac{11}{10}$ is proved as in (vi), by the pair reduction and complete rational box covers of the two
parameter domains (largest accepted box bounds below $1.0999977$ and $1.0999999$). Hence $\lambda[P]_\alpha\le1$ in all three cases, and
$F$ satisfies (i) as in (iv). The scalar condition $\lambda(1+2^{-\alpha})\ge1$ holds in all three cases ($1.67$, $1.50$, $1.39$). For the
tail, use coordinates $w=z$ centered at the midpoint. Let $Z_\infty$ be the union of the vertical axis and the four rays from $0$ in
the directions $(\pm\frac{\sqrt3}2,\pm\frac12)$, the zero set of $\cos3\theta$, and put
$g_\infty(w)=2^{\alpha-1}\operatorname{sgn}(\cos3\theta)\operatorname{dist}(w,Z_\infty)^\alpha$. The four rays of $Z$ are translates of the
corresponding rays of $Z_\infty$ by vectors $(\pm(b+\frac12),\pm b)$ of length $H_b$, the bounded
pieces of $Z$ lie in the closed disk of radius $H_b$, and the vertical axes coincide; so the two distances differ by at most $H_b$, which settles the points where the signs agree.
By symmetry let $X>0$, $Y\ge0$. Where the signs differ, $Y$ lies between the graph $Y=B(X)$ and the line $Y=X/\sqrt3$, both
distances are at most the vertical distances to these two graphs, and their sum is at most $|B(X)-X/\sqrt3|$. Here $B(X)-X/\sqrt3$ is
affine on $[0,\frac12]$ and on $[\frac12,\frac12+b]$ and constant beyond, so its absolute value is convex on each piece and at most
the largest of the values $\frac12$, $\frac1{2\sqrt3}$ and $|b-(b+\frac12)/\sqrt3|$ at $X=0,\frac12,\frac12+b$, all at most $H_b$. So the signed distances differ by at most $H_b$ everywhere. Since $t\mapsto2^{\alpha-1}\operatorname{sgn}(t)|t|^\alpha$ has
seminorm at most one, $|g-g_\infty|\le H_b^\alpha$. The six rays are equally spaced, so $|g_\infty(w)|\le\frac12|w|^\alpha$, and $|g_\infty|\le h$
because $Z_\infty$ contains the axis. Where $g_\infty>0$ in $X>0$, $|\theta|<\frac\pi6$, so $\cos2\theta>\frac12$ and
$\lambda P(w)\ge\lambda(1+2^{-\alpha})\frac{|w|^\alpha}2\ge g_\infty(w)$; where $g_\infty\le0$ this holds because $P\ge0$. Hence
$\max(-h,\min(h,g_\infty,\lambda P(w)))=g_\infty(w)$. By $\lambda[P]_\alpha\le1$, $|-\frac12+\lambda P(w-x)-\lambda P(w)|\le\frac12+2^{-\alpha}$. The
minimum and the maximum are nonexpansive in the largest change of their arguments, so $|f-g_\infty|\le\beta$ on $X>0$, and by
oddness on the whole plane. Next, $\nu_0(w)=\operatorname{Re}\frac1{\pi w^3(1-1/(4w^2))^2}$ (Section 5), and expanding $(1-\epsilon)^{-2}$ with
$|\epsilon|=\frac1{4|w|^2}\le q$ gives, for $|w|=r>R$, $|\nu_0(w)|\le\frac1{\pi r^3(1-q)^2}$ and
$|\nu_0(w)-\frac{\cos3\theta}{\pi r^3}|\le\frac1{2\pi r^5(1-q)^2}$. Integrating $\beta|\nu_0|$ and $\frac12r^\alpha|\nu_0-\frac{\cos3\theta}{\pi r^3}|$ over
$|w|>R$ gives the two error terms. Finally, each of the twelve half-lobes of $\cos3\theta$ contributes the same angular integral,
so $\int_0^{2\pi}\cos3\theta\,g_\infty(e^{i\theta})\,d\theta=12\cdot2^{\alpha-1}\int_0^{\pi/6}\sin3t\,\sin^\alpha t\,dt=2\pi a_3(\alpha)$, and
$\int_R^\infty r^{\alpha-2}\,dr=\frac{R^{\alpha-1}}{1-\alpha}$. This proves the tail estimate. For the sharper error write
$d=\frac{\cos3\theta}{\pi r^3}$ and $\nu_0f-dg_\infty=d(f-g_\infty)+(\nu_0-d)(f-g_\infty)+(\nu_0-d)g_\infty$; since $\int_0^{2\pi}|\cos3\theta|\,d\theta=4$, the three
terms give $\frac{4\beta}{\pi R}$, $\frac{\beta}{3R^3(1-q)^2}$ and $\frac{R^{\alpha-3}}{2(3-\alpha)(1-q)^2}$. For the pole disks write $z=x+u$. Since $x\in Z$,
$g(z)+c\ge c-2^{\alpha-1}|u|^\alpha$, and $-\frac12\le-\frac12+\lambda P(u)\le-\frac12+\lambda|u|^\alpha$; so the two conditions on $\epsilon$ make the
profile branch active in the minimum and below $h$, and only the lower clamp remains: $f(z)=-\frac12+\lambda P(u)+d(u)$ with
$d(u)=(\frac12-\frac12(1+2u_1)^\alpha-\lambda P(u))_+$. Here $d=0$ for $u_1\ge0$, and $d(u)\le\alpha C_\epsilon(-u_1)$ for $u_1<0$ by the mean
value theorem. The integral of $K_0(u)\lambda P(u)$ over the disk is $\lambda\epsilon^\alpha/\alpha$ times
$\frac1{4\pi}\int_0^{2\pi}|\cos2\theta|^{1+\alpha}d\theta=A_\alpha$, because the radial part $\frac12|u|^\alpha$ of $P$ has zero circular mean against
$K_0$. The constant $-\frac12$ against $-K_0(z-y)$ gives $\frac12\pi\epsilon^2K_0(e_1)=\frac{\epsilon^2}4$ by the mean value property of the harmonic
function $K_0$, and the rest of the other-pole term is at most $E_s$ in absolute value by $|f(z)+\frac12|\le|u|^\alpha$ and
$|z-y|\ge1-\epsilon$. For the clamp, $|\int K_0d|\le E_b$ by $|K_0(u)|\le\frac{|\cos2\theta|}{2\pi|u|^2}$, and the part where $K_0\ge0$ is
nonnegative. Under the extra condition this part vanishes: where $K_0\ge0$, $|u_1|\ge|u_2|$, so $P(u)\ge\frac12|u|^\alpha$ and
$d(u)\le(\alpha C_\epsilon r-\frac\lambda2r^\alpha)_+=0$ for $r=|u|<\epsilon$; hence $\int K_0d\le0$, which gives $J_\epsilon\le M+E_s$. Where $K_0<0$ and $u_1<0$, put $t=-u_1/|u|\in(0,\frac1{\sqrt2})$; then $|\cos2\theta|=1-2t^2$ and, by $s^\alpha\le1+\alpha(s-1)$,
$P(u)=\frac12|u|^\alpha(1-(1-2t^2)^\alpha)\ge\alpha|u|^\alpha t^2$, so $d\le\alpha(C_\epsilon rt-\lambda r^\alpha t^2)_+$ with $r=|u|$. The two arcs with a
given $t$ have measure $2\,dt/\sqrt{1-t^2}$ and $(1-2t^2)/\sqrt{1-t^2}\le1$, so this part is at least
$-\frac\alpha\pi\int_0^\epsilon\frac{dr}r\int_0^{C_\epsilon r^{1-\alpha}/\lambda}(C_\epsilon rt-\lambda r^\alpha t^2)\,dt=-E_c$. For the values, the region $|z|\le R$ is enclosed by the
cell method of (iv), with complete initial segments of the radial task lists: $13777550$, $4299752$ and $5015234$ cells, with
$R=10^8$, $3944.81\ldots$ and $1179.76\ldots$ (exact rational radii recorded in the certificates). At $\alpha=\frac12$ the cells
are twice as fine as in (iv) (angular and logarithmic radial steps $0.005$ instead of $0.01$, pole cells from radius $10^{-8}$), and all
$1847$ tasks are used. At $\alpha=\frac12$ and $\alpha=\frac9{10}$ two further valid refinements are used: on a cell off the midline where every branch of the minimum and the clamp is smooth,
$|f-f(z_c)|\le\min(r_Q^\alpha,L r_Q)$ with $L$ the largest Lipschitz bound of the branches (a minimum or maximum of $L$-Lipschitz
functions is $L$-Lipschitz, so the active branch may change inside the cell), and cells meeting the boundaries of the pole disks
are subdivided two more levels. The main tail terms are $0.0001004$, $0.2289465$ and $2.1132780$, $a_3$ being enclosed by $100$
terms of the positive series
$a_3(\alpha)=\frac3{4\pi}\sum_{k\ge0}\binom{2k}k16^{-k}\big(\frac3{\alpha+2+2k}-\frac1{\alpha+4+2k}\big)$ with remainder at most
$\frac{3\cdot4^{-N}}{\pi(\alpha+2+2N)}$ after $N$ terms; with the sharper error the tail errors are at most $1.8\cdot10^{-8}$, $0.000526$ and $0.001325$. The pole disks are bounded by the
lemma, at the radii $\epsilon=0.0117008\ldots$, $0.0110701\ldots$ and $5.0112\ldots\cdot10^{-6}$ (exact rationals in the certificates, all three
conditions on $\epsilon$, including the extra one, checked in outward arithmetic); the completed cell tasks inside these disks are removed with an exact coverage check.
The midpoint region of radius below $10^{-2}$ is bounded as in (iv). Exact rational recombination
in 320-bit ball arithmetic gives $2J_0\in[1.9531232,1.9597430]$, $[2.3870680,2.4046173]$ and $[4.7413008,4.7530337]$, which give
$D_{1/2}\ge2.4531232777$, the bound at $\alpha=\frac9{10}$ and $D_{3/4}\ge2.8870680072$. The cell computations were replayed independently from frozen sources.
At $\alpha=\frac34$ a finer complete computation gives more: angular and logarithmic radial steps $0.005$, all
$1220$ tasks with $27946926$ cells, polar cells about the poles for radii in $[10^{-2},\frac12]$ and about the midpoint for radii in
$[10^{-2},10^{16}]$, the pole disks bounded by the lemma at $\epsilon=\frac1{100}$ (all three conditions on $\epsilon$ checked in outward
arithmetic), the midpoint region of radius below $10^{-2}$ as in (iv), and the exterior of radius $10^{16}$ by the tail estimate
with the sharper error. Exact rational recombination gives $2J_0\in[2.3938332,2.3987032]$, so $D_{3/4}\ge2.8938332593$. This
computation is itself an independent replay of the frozen cell evaluator. The stated bound comes from a still finer computation
with the same evaluator: steps $0.0035$, $3961$ tasks with $59232568$ cells, polar cells about the poles for radii in $[10^{-6},\frac12]$
and about the midpoint for radii in $[10^{-2},10^{16}]$. The cells inside the pole disks of radius $\epsilon=0.00165846\ldots$ (an exact
rational task endpoint, recorded in the certificate) are removed and the disks are bounded by the lemma (all three conditions checked
in outward arithmetic); the midpoint region and the exterior are bounded as before. Exact rational recombination gives
$2J_0\in[2.3948343,2.3977111]$, so $D_{3/4}\ge2.8948343532$. The independent check of this computation consists of an audit of all
$3961$ task records (sources, parameters, exact coverage and the exact recombination) and an exact independent recomputation of $70$
complete tasks with $2396908$ cells, chosen to include both ends of the radial ranges, the changes of angular resolution and the
largest error contributions; it is not a complete independent replay of all cells.
At $\alpha=\frac12$ the stated bound likewise comes from a finer computation with the same evaluator: steps $0.0035$, $4019$ tasks with
$24900260$ cells, polar cells about the poles for radii in $[10^{-8},\frac12]$ and about the midpoint for radii in $[10^{-2},10^8]$. The
cells inside the pole disks of radius $\epsilon=0.0099201\ldots$ (an exact rational task endpoint, recorded in the certificate) are
removed and the disks are bounded by the lemma (all three conditions checked in outward arithmetic); the midpoint region and the
exterior are bounded as before. Exact rational recombination gives $2J_0\in[1.9542144,1.9586939]$, so $D_{1/2}\ge2.4542144708$. Its
independent check is of the same kind: an audit of all $4019$ task records and an exact independent recomputation of $52$ complete
tasks with $1129918$ cells; it is not a complete independent replay of all cells.
(viii) $K_{1/10}\le1.002471319750$ and $K_{1/5}\le1.010555855930$ bound $[P]_{1/10}$ and $[P]_{1/5}$ (proof of Theorem 4.6), and
$K^*_{3/10}\le1.007$ bounds $[P]_{3/10}$ (as in (v)), so $F$ satisfies (i) as in (iv) ($g$ vanishes at $x$ and $c>-\frac12$), and $f$ is nonincreasing in $|Y|$, so the Stieltjes sums of (iv) apply. They are sharpened by a better
admissible choice of $A_j$: the largest of the following lower bounds for $f(X,dv_j)-f(X,dv_{j+1})$, valid uniformly on the strip,
replaced by $0$ if negative. (a) The ball enclosure of (iv), in which $\xi^\alpha$ is enclosed by $[0,(\sup\xi)^\alpha]$ when the enclosure of a
quantity $\xi\ge0$ contains $0$. (b) $d_l^\alpha\lambda(p(v_j)-p(v_{j+1}))$ with $p(v)=P(1,v)$, when the enclosures prove at both nodes that the
profile branch is active throughout the strip (then the increment is $d^\alpha\lambda(p(v_j)-p(v_{j+1}))$ by homogeneity). (c), (d) First- and
second-order mean value bounds about the midpoint of the strip, when the enclosures certify the active branch of the minimum
and the clamp at both nodes throughout the strip. For the distance branch, one piece of $Z$ (axis, segment or ray) must be certainly
nearest and the side of the graph certain; the distance $r$ to that convex piece is $C^1$ off it with gradient of length one, and
$C^{1,1}$ with $0\le D^2r\le(I-\nabla r\nabla r^{\mathsf T})/r$ almost everywhere. (e) The minimum of the lower endpoints of the ball enclosures, as in (a), on all $8$ equal
subintervals of the strip. The strips are $\log d\in[-60,-18]$ ($2048$ strips with $256$ ratio intervals, both signs) and $\log d\in[-18,12]$ for $X>\frac12$,
$\log d\in[-18,\log\frac12]$ for $X<\frac12$ ($16384$ strips with $512$ ratio intervals), all with $\log v\in[-6,3]$, in 192-bit ball arithmetic, at $\alpha=\frac15$ and
$\alpha=\frac3{10}$. The $18$ chunk sums give $D_{1/5}\ge3.9578692464$ and $D_{3/10}\ge3.0161919859$. At $\alpha=\frac1{10}$ the strips with
$\log d\le-18$ are $\log d\in[-150,-18]$ ($4096$ strips with $512$ ratio intervals, both signs), the others are as above, and the
$20$ chunk sums give $D_{1/10}\ge7.0445434786$. The chunks were recombined independently with exact coverage,
profile-constant and source-hash checks, and three selected chunks at each exponent were replayed independently.
The complete proof and data are in the accompanying artifacts. $\square$

The witness of (ii) is the analogue for the axis phase of the polygonal witness of Theorem 4.5, shifted to the pole
value $-\frac12$; the pole jump contributes the term $1$. At $\alpha=\frac12$ the same witness gives only about $2.09$, close to
$L(\frac12)$. The cusp of (iv) is the stronger construction: a floating-point evaluation of the same $F$ gives about
$2.457$, inside the certified enclosure $[2.4542,2.4587]$ of its value (part (vii)). Coarser lower Stieltjes sums of the same witness gave
$2.3093554304$ and $2.3869631120$ (the latter in the proof of (iv)). At $\alpha=\frac{99}{100}$ the certified enclosure of the value of the witness of (ii) is
$[42.3800,42.4352]$; only its lower end is used.

## 5. Small-$\alpha$ asymptotics

Notation for this section: $x=(\frac12,0)$, $y=-x$; for a phase $b$, $K_b(z)=\cos(2\arg z-2b)/(2\pi|z|^2)$,
$T_b=\cos2b\,T_{xx}+\sin2b\,T_{xy}$ (so $\|T_b\|=C_\alpha$ and $\|T_b-\frac12I\|=D_\alpha$ by identity 1), and
$\nu_b(w)=K_b(x-w)-K_b(y-w)=\operatorname{Re}(e^{2ib}G(w))$, $G(w)=\frac w{\pi(w^2-1/4)^2}$. Put
$\Omega_\rho=\mathbb R^2\setminus(B_\rho(x)\cup B_\rho(y))$ and define the circular finite part

$$N(b)=\lim_{\rho\to0}\Big[\frac12\int_{\Omega_\rho}|\nu_b|\,dA+\frac2\pi\log\rho\Big].$$

The limit exists because near each pole $|\nu_b|=|\cos(2\theta-2b')|/(2\pi r^2)+O(1)$ for a suitable phase $b'$, and the
angular mean of $|\cos|$ is $2/\pi$. Let $V(\alpha,b)=\sup_{[f]_\alpha\le1}|T_bf(x)-T_bf(y)|$, so $C_\alpha=\sup_bV(\alpha,b)$.

**Theorem 5.1 (leading coefficient).** $\lim_{\alpha\to0}\alpha C_\alpha=\lim_{\alpha\to0}\alpha D_\alpha=\frac2\pi$.
In particular $C_*=2/\pi$ is the sharp coefficient of $1/\alpha$ for $T_{xx}$, $T_{xy}$ and $R_1^2$.

*Proof.* $C_\alpha\le D_\alpha\le C_\alpha+\frac12$ (identity 2). Theorem 3.1 gives $\alpha C_\alpha\le\alpha F(\alpha)\to2/\pi$ and
Theorem 4.1 gives $\alpha C_\alpha\ge\alpha L_1(\alpha)\to2/\pi$. $\square$

**Theorem 5.2 (one fixed functional).** For $b=\pi/4$, that is, for the functional
$f\mapsto T_{xy}f(x)-T_{xy}f(y)$ with $x-y$ along a coordinate axis,

$$V(\alpha,\tfrac\pi4)=\frac2{\pi\alpha}+\frac12+\frac{\log2-1}\pi+o(1)\qquad(\alpha\to0),$$

and $N(\frac\pi4)=\frac12$.

*Proof.* (i) *Finite part.* In the upper half-plane $\nu_{\pi/4}>0$ exactly for $|X|>\beta(Y)$, where
$\beta(Y)^2=\frac13\big(a^2-Y^2+2\sqrt{Y^4+a^2Y^2+a^4}\big)$, $a=\frac12$: the numerator of $\nu_{\pi/4}$ has the sign of
$Y\big((X^2+Y^2)(3X^2-Y^2)-2a^2(X^2+Y^2)-a^4\big)$. For $Y>0$ the integral of $\nu_{\pi/4}$ over a horizontal line vanishes, so its
total variation there is $H(Y)=\frac{2Y}\pi\big[\frac1{(\beta-a)^2+Y^2}-\frac1{(\beta+a)^2+Y^2}\big]$. The substitution
$Y=\frac{2a\sqrt{t(t^2+t+1)}}{t^2-1}$, $\beta=a\frac{t^2+1}{t^2-1}$, $t\in(1,\infty)$, gives
$-\pi H(Y)\frac{dY}{dt}=\frac1t+\frac2{1+t^2}-\frac2{(1+t)^2}$. Integrating gives the strip finite part
$\lim_{\varepsilon\to0}[\frac2\pi\log\varepsilon+\int_\varepsilon^\infty H]=\frac12-\frac1\pi$. Converting the strip cutoff to circular cutoffs about the
two poles adds $\frac1{2\pi}\int_0^{2\pi}|\sin2\theta|\log\frac1{|\sin\theta|}d\theta=\frac1\pi$. Hence $N(\frac\pi4)=\frac12$.
(ii) *Upper bound.* For $0<\delta<\frac14$, the two local parts of radius $\delta$ cost at most $2a_2(\alpha)\delta^\alpha/\alpha$ by the
angular lemma. The remaining density is odd under $w\mapsto-w$. Antipodal pairing bounds its action by
$2^{\alpha-1}\int|\nu_\delta||w|^\alpha$, which tends to $\frac12\int_{\Omega_\delta}|\nu|+O(\delta^2)$ as $\alpha\to0$ by dominated convergence.
Since $2a_2(\alpha)\delta^\alpha/\alpha=\frac2{\pi\alpha}+\frac2\pi\log\delta+\frac{\log2-1}\pi+O_\delta(\alpha)$, letting $\alpha\to0$ and then $\delta\to0$ gives
$\limsup(V-\frac2{\pi\alpha})\le\frac{\log2-1}\pi+N(\frac\pi4)$.
(iii) *Lower bound.* Let $v$ be the signed distance to the zero set of $\nu_{\pi/4}$ (closure, poles included), with the sign of
$\nu_{\pi/4}$, and $f_\alpha=p_\alpha\circ v$. Lemma 4.0 gives $[f_\alpha]_\alpha\le1$, and $f_\alpha(x)=f_\alpha(y)=0$. Away from the poles
$f_\alpha\to\frac12\operatorname{sign}\nu$. Near each pole the zero set is the horizontal axis and a curve at distance $O(r^4)$ from the
vertical line, because $\beta(Y)=a+O(Y^4)$. So $v=v_0+O(r^4)$, with $v_0$ the signed distance to two perpendicular lines, for
which $p_\alpha\circ v_0$ is the exact angular extremizer. The weighted error is $O(\alpha r^3+r^6)$ per circle, and the local
contribution is $\frac{2a_2(\alpha)\delta^\alpha}\alpha+O(\delta^2)$. This matches (ii). $\square$

**Theorem 5.3 (existence and variational form of the second term).** For every $b$,
$V(\alpha,b)=\frac2{\pi\alpha}+\frac{\log2-1}\pi+N(b)+o(1)$, the upper estimate holds uniformly in $b$, and

$$C_\alpha=\frac2{\pi\alpha}+\frac{\log2-1}\pi+\max_bN(b)+o(1)\qquad(\alpha\to0).$$

*Proof.* The upper bound of Theorem 5.2(ii) holds for every $b$, and its error terms are uniform in $b$: the local bound
does not depend on $b$, and the truncated densities $\nu_{b,\delta}$ are dominated, uniformly in $b$, by
$|G|\mathbf 1_{\Omega_\delta}+O(1)\mathbf 1_{B_\delta(x)\cup B_\delta(y)}$. For the lower bound, take the signed distance $v_b$ to the
zero set of $\nu_b$. Near each pole that zero set is a $C^1$ perturbation of the two zero lines of the own kernel, and
$|v_b-v_0|\le Cr^3$ in $B_r$ uniformly in $b$, because $\nu_b$ is the own kernel plus a smooth term. The argument of
Theorem 5.2(iii) then applies, with the weighted error $O(\alpha r^2+r^4)$. The upper bound for $C_\alpha=\sup_bV(\alpha,b)$ uses
the uniform upper estimate; the lower bound uses the pointwise estimate at a maximizing $b$, which exists because $N$
is continuous on the phase circle. $\square$

The full proof is in the accompanying artifacts; the verification of the local estimate was done independently
of the original derivation. An equivalent form is $C_0=-\frac{1+\log2}\pi+\max_bJ(b)$, with $J(b)=N(b)+\frac{2\log2}\pi$ the
half-plane integral $J(b)=\int_{H\setminus B(x,1/2)}|\nu_b|+\int_{B(x,1/2)}(|\nu_b|-|K_b(x-\cdot)|)$, $H=\{w_1>0\}$.

**Theorem 5.4 (the direction maximum and the second term of $C_\alpha$).** $N$ is even, $\pi/2$-periodic and strictly
increasing on $[0,\pi/4]$. Explicitly,

$$N(b)=N(0)+\frac1\pi\sum_{n\ge1}\frac{R_n(1-\cos4nb)}{n(4n^2-1)},\qquad
R_n=\prod_{k=0}^{n-1}\frac{2n+1+4k}{2n+3+4k}=\frac{\Gamma(\frac n2+\frac34)\Gamma(\frac{3n}2+\frac14)}{\Gamma(\frac n2+\frac14)\Gamma(\frac{3n}2+\frac34)},$$

$$N(0)=\frac13+\frac{\sqrt3-1+\log\frac2{2+\sqrt3}}\pi=0.3677872244\ldots,\qquad \max_bN=N(\tfrac\pi4)=\frac12 .$$

Consequently

$$\boxed{C_\alpha=\frac2{\pi\alpha}+\frac12-\frac{1-\log2}\pi+o(1)\qquad(\alpha\to0).}$$

The maximizing directions are exactly $b\equiv\frac\pi4\pmod{\frac\pi2}$: the functionals $T_{xy}f(x)-T_{xy}f(y)$ with $x-y$ on a
coordinate axis, or $T_{xx}f(x)-T_{xx}f(y)$ with $x-y$ on a diagonal.

*Proof.* Let $\Theta=2\arg G$ and $M_n=\lim_{\rho\to0}\int_{\Omega_\rho}|G|e^{in\Theta}dA$. Near a pole, $G=\frac1{2\pi}r^{-2}e^{-2it}u$ with
$u$ holomorphic and $u(x)=1$: at $x$, $u=1-h^2/(1+h)^2$ with $h=re^{it}$, and at $y$ the same holds with $(1+h)^2$ replaced by
$(1-h)^2$ and an overall minus sign, which changes $\Theta$ only by $2\pi$. For
$r\le\frac14$, $|u-1|\le\frac{16}9r^2$, $|\partial_tu|\le\frac{128}{27}r^2$ and $|u|\ge\frac89$, so $\eta=\arg u$ is single-valued with
$|\eta'|\le\frac{16}3r^2$. The substitution $s=t-\frac\eta2$, with $|s'-1|\le\frac83r^2\le\frac16$, gives $\Theta\equiv-4s\pmod{2\pi}$, and the moment over the
circle of radius $r$ becomes $\frac1{2\pi r}\int a_r(s)e^{-4ins}ds$ with $a_r=|u|/s'$ and $|a_r-1|\le\frac{16}3r^2$. Its constant part vanishes,
so its modulus is at most $\frac{16}3r$ for every $n\ge1$, without the factor $n$ that a derivative of $e^{in\Theta}$ would bring. This
gives existence of $M_n$, with $|M_n(\rho)-M_n(\rho')|\le\frac{16}3|\rho^2-\rho'^2|$ for $\rho,\rho'\le\frac14$ (both poles), uniformly in $n$. Expanding the
Lipschitz function $|\cos(\Theta/2+2b)|-|\cos(\Theta/2)|$ in its absolutely convergent Fourier series gives
$N(b)-N(0)=\frac2\pi\sum_n(-1)^{n+1}\frac{(\cos4nb-1)M_n}{4n^2-1}$. The substitution $z=4w^2$ turns $M_n$ into
$\frac1\pi\,\mathrm{PV}\!\int z^{\alpha_n-1}\bar z^{\beta_n-1}(1-z)^{-2n-1}(1-\bar z)^{2n-1}dA$ with $\alpha_n=\frac34+\frac n2$, $\beta_n=\frac34-\frac n2$. A
$\bar\partial$-primitive and Green's formula reduce it to a residue at $z=1$, giving $M_n=(-1)^nR_n/(2n)$. A second
derivation uses the Fourier transforms of homogeneous functions $r^\mu e^{im\phi}$, and a third, numerical one uses
hypergeometric series; all three agree. Then $\log R(x)$, with $R(x)$ the Gamma ratio, has
$(\log R)'<0$ and $(\log R)''>0$ by an integral representation of $\psi(v+\frac12)-\psi(v)$, whose integrand difference
factors as $Y^2(Y-1)^2(Y+1)>0$. So $c_n=R_n/(4n^2-1)$ is positive, decreasing and convex. A sine series with such
coefficients is positive on $(0,\pi)$ (two Abel summations, Fejér-type kernel $E_m\ge0$). So
$N'(b)=\frac4\pi\sum_nc_n\sin4nb>0$ on $(0,\frac\pi4)$. $N(\frac\pi4)=\frac12$ is Theorem 5.2. The closed form of $N(0)$ comes from an
independent horizontal-slice computation, with critical values $X^2=Y^2+a^2\pm2Y\sqrt{Y^2+a^2}$ and strip-to-circle
correction $\frac{1+\log2}\pi$. It agrees with the series value $N(\frac\pi4)-\frac4\pi\sum_{n\ \rm odd}\frac{R_n}{2n(4n^2-1)}$ to $10^{-15}$.
Combine with Theorem 5.3. $\square$

**Theorem 5.5 (second term of $D_\alpha$, bracket).**

$$C_0+\frac2\pi\log\cosh\frac\pi4\le\liminf_{\alpha\to0}\Big(D_\alpha-\frac2{\pi\alpha}\Big)\le\limsup_{\alpha\to0}\Big(D_\alpha-\frac2{\pi\alpha}\Big)\le2C_0,$$

with $C_0=\frac12-\frac{1-\log2}\pi$; numerically $0.5812906021\le\liminf\le\limsup\le0.8046514280$. Hence
$\liminf_{\alpha\to0}(D_\alpha-C_\alpha)\ge\frac2\pi\log\cosh\frac\pi4=0.1789648881\ldots$.

*Proof of the lower bound.* Fix $A,B>0$, $A+B=1$, $p=1/(1-\alpha)$, $M_\alpha=(A^p+B^p)^{-1/p}$ and
$P_\alpha(v)=M_\alpha(Av_+^\alpha-B v_-^\alpha)$. Hölder's inequality $As^\alpha+Bt^\alpha\le(A^p+B^p)^{1/p}(s+t)^\alpha$ gives
$[P_\alpha]_\alpha\le1$ on $\mathbb R$. Also $\log M_\alpha=\alpha H(A)+O(\alpha^2)$ with $H(A)=-A\log A-B\log B$. Take $b=\frac\pi4$, $v_b$ as in Theorem
5.3, $c=\frac12-A$, $h_\alpha(w)=\frac12(2w_1)^\alpha$. On $\{w_1>0\}$ let $f_\alpha=\max\{-h_\alpha,\min\{h_\alpha,c+P_\alpha\circ v_b\}\}$, and extend
by $f_\alpha(-w)=-f_\alpha(w)$. Then $[f_\alpha]_\alpha\le1$ (lattice property, and $2^{\alpha-1}(w_1^\alpha+|z_1|^\alpha)\le|w-z|^\alpha$
across the axis), and $f_\alpha(x)=c=-f_\alpha(y)$. For small $\alpha$ the clamp is inactive in fixed small pole disks. There
the two signed branches give $\frac{2a_2(\alpha)\rho^\alpha}\alpha\frac{M_\alpha}{2^\alpha}+O(\rho^2)$; the constant $c$ cancels on circles.
Outside, $f_\alpha\to\frac12\operatorname{sign}\nu_b$. So $T_bf_\alpha(x)-T_bf_\alpha(y)=\frac2{\pi\alpha}+\frac12+\frac{2H(A)-\log2-1}\pi+o(1)$.
The identity term subtracts $\frac12(f_\alpha(x)-f_\alpha(y))=c$. Maximizing $\frac2\pi(H(A)-\log2)+A-\frac12$ at
$A=e^{\pi/2}/(1+e^{\pi/2})$ gives the gain $\frac2\pi\log\cosh\frac\pi4$.

*Proof of the upper bound.* Repeat the upper half of Theorem 5.3. In each local disk, replace the reflection pairing by
the projection pairing of Theorem 3.2. The two paired parts cost $\frac{2A_\alpha\rho^\alpha}\alpha$. The positive
remainders $Q_\rho$ are the same measure translated to $x$ and $y$, so they cost at most $\kappa_Q=\frac1\pi$. Together with the
uncancelled identity coefficient $\frac12-\kappa_Q$ the cost is $\frac12$. The regular part is unchanged and uniform in $b$.
Since $A_0=a_2(0)=\frac1\pi$ and $A_0'-a_2'(0)=\frac{\log2-1}{2\pi}$, the constant term rises by
$\frac12+2(A_0'-a_2'(0))=\frac12+\frac{\log2-1}\pi=C_0$, from $C_0$ (Theorem 5.4) to $2C_0$. $\square$

**Theorem 5.6 (two-term asymptotics of $D_\alpha$).**

$$D_\alpha=\frac2{\pi\alpha}+2C_0+o(1)\quad(\alpha\to0^+),\qquad\text{hence}\qquad D_\alpha-C_\alpha\to C_0=0.4023257139688609\ldots$$

So the upper bound of Theorem 5.5 is attained, and its lower bound is not sharp.

*Proof.* The upper bound is Theorem 5.5. For the lower bound, rotation by $\pi/4$ conjugates $R_1^2=T_{xx}-\frac12I$ to $T_{xy}-\frac12I$
without changing the seminorm. So it suffices to evaluate $\Phi(f)=(T_{xy}-\frac12I)f(x)-(T_{xy}-\frac12I)f(y)$ with $x=(\frac12,0)$,
$y=-x$. Write $S(u)=2u_1u_2/|u|$ ($S(0)=0$) and $\nu=K_{xy}(\cdot-x)-K_{xy}(\cdot-y)$.

*Step 1 (local profile).* For $0<\alpha\le\frac14$, the function $g(u)=\frac12\big[|u|^\alpha+\operatorname{sgn}(S(u))|S(u)|^\alpha\big]$ satisfies
$[g]_\alpha\le1+2\alpha^2$. Points in one quadrant: $|S|$ is 2-Lipschitz there ($|\nabla S|\le2$). If $|p-q|\le\min(|p|,|q|)$ the quotient
is at most $(\alpha+2^\alpha)/2<1$. Otherwise it is at most $(1+t)^\alpha-\frac12t^\alpha\le1$, with $t=\min(|p|,|q|)/|p-q|$, in a positive
quadrant, and at most $2^{\alpha-1}$ in a negative one. Opposite quadrants of equal sign have $p\cdot q\le0$, so $|p-q|\ge\max(|p|,|q|)$
and $0\le g\le|u|^\alpha$ suffices. For opposite signs, $g(q)-g(p)\le\frac12(|q|^\alpha-|p|^\alpha)$ handles one ordering. For the other, by
symmetry and scaling take $p=e^{ia}$, $q=Ue^{-ib}$ with $0<a,b<\frac\pi2$, and put $s=\sin2a$, $t=\sin2b$, $R=U^\alpha$, $D=|p-q|$. The
quotient is $Q=(1-R+s^\alpha+Rt^\alpha)/(2D^\alpha)$, and $D\ge|1-U|$, $s+t=2\sin(a+b)\cos(a-b)\le2D$.
- If $U\ge1$, then $Q\le(s^\alpha+t^\alpha)/(2D^\alpha)\le1$ by concavity.
- If $U<\alpha$, then $Q\le(1-\alpha)^{-\alpha}\le1+2\alpha^2$.
- If $\alpha\le U<1$, let $k=1/(1-\alpha)$. The maximum of $X^\alpha+RY^\alpha$ over $X+Y\le2$ is $2^\alpha(1+R^k)^{1/k}$. Hence
  $Q\le1+\delta+\frac12(1-R)((1-U)^{-\alpha}-1)$, with $\delta=((1+R^k)/2)^{1/k}-\frac{1+R}2\le\frac{k-1}{8R}(1-R)^2\le\frac{\alpha^2}3$.
  Elementary bounds give $\frac12(1-R)((1-U)^{-\alpha}-1)\le\frac{2\alpha^2}3$, so $Q\le1+\alpha^2$.

*Step 2 (the witness).* In $\{X>0\}$ the sign of $\nu$ is that of $Y(X-b(Y))$, where
$b(Y)^2=\frac13\big(\frac14-Y^2+2\sqrt{Y^4+Y^2/4+1/16}\big)=\frac14+Y^4+O(Y^6)$. Let $s(z)$ be the signed distance to the curve $\Gamma=\{X=b(Y)\}$,
$V(z)=(s(z),Y)$ and $\rho=\alpha$. Define

$$F_\alpha=-\tfrac12+\tfrac12\min(|V|,\rho)^\alpha+\tfrac12\operatorname{sgn}(S(V))|S(V)|^\alpha,$$

clamp it to $[-h,h]$ with $h=\frac12(2X)^\alpha$, and extend the result $f_\alpha$ oddly under $z\mapsto-z$. Then $f_\alpha(x)=-\frac12$ and $f_\alpha(y)=\frac12$.

*Step 3 (seminorm).* We show $[f_\alpha]_\alpha\le1+2\alpha^2+O(\alpha^4)$. The frozen planar profile $\frac12\min(|u|,\rho)^\alpha+\frac12\operatorname{sgn}(S)|S|^\alpha$ equals
$\min\{g,\frac12\rho^\alpha+\frac12\operatorname{sgn}(S)|S|^\alpha\}$. The second function has seminorm at most $\frac12\cdot2^{1-\alpha}\cdot2^\alpha=1$, so the minimum has
seminorm at most $1+2\alpha^2$. On $B(x,20\rho)$ the map $V$ is $(1+O(\rho^3))$-Lipschitz, since $\nabla s$ is horizontal up to $O(\rho^3)$.

Away from the frozen set, $F_\alpha=H:=-\frac12+\frac12\rho^\alpha+\frac12\operatorname{sgn}(S(V))|S(V)|^\alpha$, and $[H]_\alpha\le1$ for $\alpha\le\frac23$:
- for equal signs, $|S\circ V|$ is $2\sqrt2$-Lipschitz, and $\frac12(2\sqrt2)^\alpha\le1$;
- for opposite signs, the segment meets the zero set $Z=\Gamma\cup\{Y=0\}$, and $|S(V)|\le2\operatorname{dist}(\cdot,Z)$.

Mixed pairs: let $|V(p)|<\rho$ (so $|p-x|\le2\rho$) and $|q-x|\ge20\rho$. If $F_\alpha(p)\ge F_\alpha(q)$, then $F_\alpha(p)-F_\alpha(q)\le H(p)-H(q)$. In the
other order, the quotient is at most $\frac12(18^{-\alpha}+(20/9)^\alpha)\le1$ for $\alpha\le\frac12$. The clamp and the odd extension
are treated as in Theorem 5.5.

*Step 4 (value).* Fix a small $\delta$. Since $V(x+u)=u+O(|u|^4)$, the local integral $\int_{|u|<\delta}K_{xy}(u)(f_\alpha(x+u)-f_\alpha(x))\,du$
equals $A_\alpha\delta^\alpha/\alpha$ up to an error whose upper limit as $\alpha\to0$ is $O(\delta^6)$:
- the radial term is constant on circles and integrates to zero;
- the signed term gives exactly $A_\alpha\delta^\alpha/\alpha$, because $\int_0^{2\pi}|\sin2\theta|^{1+\alpha}d\theta=4\pi A_\alpha$;
- the lower clamp changes the profile by at most $C\alpha|u|+\frac\alpha2\log_+(2|u|/\rho)$, whose integral against $|K_{xy}|$ is
  $O(\alpha\delta+\alpha\log^2(2\delta/\rho))\to0$ for $\rho=\alpha$;
- the upper clamp is inactive for $\delta<\frac14$.

By oddness the same holds at $y$. Off the two disks, $f_\alpha\to\frac12\operatorname{sgn}\nu$ pointwise, with domination by $\frac12(2|z|)^\alpha$, and the
identity term contributes $+\frac12$. Using $\frac{2A_\alpha\delta^\alpha}\alpha=\frac2{\pi\alpha}+\frac2\pi\log\delta+\frac{2(\log2-1)}\pi+o(1)$ and the finite part of
Theorem 5.2, $\lim_{\delta\to0}[\frac2\pi\log\delta+\frac12\int_{\text{outside}}|\nu|]=\frac12$, we get

$$\liminf_{\alpha\to0}\Big(\Phi(f_\alpha)-\frac2{\pi\alpha}\Big)\ge\frac12+\frac{2(\log2-1)}\pi+\frac12=2C_0.$$

Since $\Phi(f_\alpha)=O(1/\alpha)$ and $[f_\alpha]_\alpha=1+O(\alpha^2)$, normalizing changes the value by $O(\alpha)$. $\square$

*Remarks.* The witness realizes the projection pairing of Theorem 3.2 at both poles at once. It also realizes the full
identity gain $\frac12$, because $f_\alpha$ is close to $f_\alpha(x)=-\frac12$ on the support of the positive remainder near $x$.
Step 1 is the only place where $\alpha\le\frac14$ is used. On projection pairs $p=e^{it}$, $q=\cos2t\,e^{-it}$ the quotient of $g$ equals
$1+\frac{(1-K)(1-S)}{2S}$, with $K=\cos^\alpha2t$ and $S=\sin^\alpha2t$, so $[g]_\alpha>1$. The constant $1+2\alpha^2$ is therefore of the correct order.

**Theorem 5.7 (explicit bounds with the sharp second term, and linear remainders for $C_\alpha$ and $D_\alpha$).** For $0<\rho<\frac12$ put

$$E(\rho)=-\tfrac12\log(1-\rho^2),\qquad N_0(\rho)=\tfrac12-\tfrac2\pi\log\rho,\qquad L(\rho)=\max\{-\log(1-2\rho),\ (1+2\rho)\log(1+2\rho)\},$$

$$B_C(\rho)=\frac{\rho^2}{2(1-\rho)^2}\Big(-\log\rho+\frac12+\frac{2\beta(2)}\pi\Big),\qquad
B_D(\rho)=\frac{\rho^2}{2(1-\rho)^2}\Big(-\log\rho+\frac12+\log2\Big),\qquad
T(\alpha)=\frac{2^{\alpha+1}\alpha}\pi S(\alpha),\qquad S(\alpha)=\sum_{n\ge0}\frac{(n+1)4^{-n}}{(2n+1-\alpha)(2n+1)},$$

where $\beta(2)=\sum_{n\ge0}(-1)^n(2n+1)^{-2}=0.9159655\ldots$ is Catalan's constant. Every term of $S$ increases with $\alpha$,
$S(\alpha)<\frac1{1-\alpha}+\frac12-\log\frac32$, and for every integer $N\ge1$

$$S(\alpha)\le S^+_N(\alpha)=\sum_{n=0}^{N-1}\frac{(n+1)4^{-n}}{(2n+1-\alpha)(2n+1)}+\frac43\cdot\frac{4^{-N}(N+1)}{(2N+1-\alpha)(2N+1)}.$$

(i) For every $0<\alpha<1$ and every $0<\rho<\frac12$,

$$C_\alpha\le H_C(\alpha,\rho)=\frac{2a_2(\alpha)\rho^\alpha}\alpha+R(\alpha,\rho),\qquad
D_\alpha\le H_D(\alpha,\rho)=\frac{2A_\alpha\rho^\alpha}\alpha+\frac12+R(\alpha,\rho),$$

with $R(\alpha,\rho)=2^\alpha N_0(\rho)+[2^\alpha+(1+2\rho)^\alpha]E(\rho)+T(\alpha)$.

(ii) For every $0<\alpha<1$ and every $0<\rho<\frac12$,

$$C_\alpha\le J_C(\alpha,\rho)=\frac{2a_2(\alpha)\rho^\alpha}\alpha+2^\alpha N_0(\rho)+(2^\alpha-1)E(\rho)+T(\alpha)+\alpha\big[B_C(\rho)+E(\rho)L(\rho)\big],$$

$$D_\alpha\le J_D(\alpha,\rho)=\frac{2A_\alpha\rho^\alpha}\alpha+\frac12+2^\alpha N_0(\rho)+(2^\alpha-1)E(\rho)+T(\alpha)+\alpha\big[B_D(\rho)+3E(\rho)L(\rho)\big].$$

(iii) For every $0<\alpha\le\frac1{100}$,

$$\boxed{C_\alpha\le\frac2{\pi\alpha}+C_0+2.4755\,\alpha,\qquad D_\alpha\le\frac2{\pi\alpha}+2C_0+2.7250\,\alpha.}$$

(iv) Let $f_\alpha=2^{\alpha-1}\operatorname{sign}(\nu)\,d^\alpha$, where $\nu=K_{xy}(\cdot-x)-K_{xy}(\cdot-y)$ and $d$ is the distance to the
closed zero set of $\nu$ (poles included). Then $[f_\alpha]_\alpha\le1$ and
$\int\nu f_\alpha=\frac2{\pi\alpha}+C_0+\kappa_C\alpha+o(\alpha)$, with an explicit convergent integral $\kappa_C$ (below). Consequently

$$\boxed{C_\alpha=\frac2{\pi\alpha}+C_0+O(\alpha)\qquad(\alpha\to0^+).}$$

(v) For $D_\alpha$ the lower error of Theorem 5.6 is also linear. Consequently

$$\boxed{D_\alpha=\frac2{\pi\alpha}+2C_0+O(\alpha)\qquad(\alpha\to0^+).}$$

The constant in the lower $O(\alpha)$ term is finite and independent of $\alpha$, but it is not evaluated.

*Proof.* (i) Reduce to the increment between $x=\frac12$ and $y=-\frac12$ with an arbitrary phase $b$. The increment splits into
the two centred own-kernel integrals over $B_\rho(x)$ and $B_\rho(y)$ and the integrable density
$\mu_{b,\rho}=K_b(x-\cdot)\mathbf 1_{|x-\cdot|\ge\rho}-K_b(y-\cdot)\mathbf 1_{|y-\cdot|\ge\rho}$. The local parts cost
$2a_2\rho^\alpha/\alpha$ by the angular lemma (Theorem 3.1(a)). For $R_1^2$ the projection decomposition of Theorem 3.2 replaces
this, together with the whole identity term, by $2A_\alpha\rho^\alpha/\alpha+\frac12$, uniformly in $b$. The density $\mu_{b,\rho}$ is odd
under $w\mapsto-w$, so antipodal pairing bounds its action by $\frac12\int|\mu_{b,\rho}|(2|w|)^\alpha\,dA$. The finite-part identity
$V_b(\rho)+\Delta_b(\rho)=N(b)-\frac2\pi\log\rho$ holds, where $V_b(\rho)=\frac12\int_{\Omega_\rho}|\nu_b|$ and $\Delta_b(\rho)$ is half
the integral of $|\nu_b|-|\text{own kernel}|$ over the two disks. It follows from the exact annular integral $\frac2\pi\log\frac\rho{r_1}$ ($0<r_1<\rho$) of
the own kernel. Here $N(b)\le\frac12$ (Theorem 5.4), and $|\Delta_b|\le E(\rho)$ by the reverse triangle inequality and the
Poisson integral $\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{1+r^2+2r\cos\theta}=\frac1{1-r^2}$. On the disks $2|w|\le1+2\rho$. For $|w|>1$, the expansion
$G(w)=\frac1\pi\sum_{n\ge0}(n+1)4^{-n}w^{-2n-3}$ and $\int_1^\infty(r^\alpha-1)r^{-2n-2}dr=\frac\alpha{(2n+1-\alpha)(2n+1)}$ bound the excess over the
base cost by $T(\alpha)$. For $n\ge1$, $2n+1-\alpha>2n$, and $\frac{n+1}{2n(2n+1)}=\frac1{2n}-\frac1{2(2n+1)}$ with
$\sum_{n\ge1}\frac{4^{-n}}{2n}=\frac12\log\frac43$ and $\sum_{n\ge1}\frac{4^{-n}}{2n+1}=\log3-1$ gives the elementary bound on $S$. The function
$x\mapsto\frac{x+1}{(2x+1-\alpha)(2x+1)}$ decreases on $x\ge0$, so the terms with $n\ge N$ sum to at most $\frac43\,4^{-N}$ times its value at $N$.

(ii) The exterior plan of (i) costs at most $V_b(\rho)+(2^\alpha-1)(N_0+E)+T(\alpha)$. The new point is a local plan that pays
the own-kernel cost plus $\Delta_b(\rho)$ and an error linear in $\alpha$; then $V_b+\Delta_b\le N_0(\rho)$ removes $E$ from the
leading term. For $C_\alpha$: on each circle about a pole, the positive lobes of the own kernel are split into half-lobes and
paired by reflection across the adjacent zero ray. With $A$, $B$ the two values of the full density at a pair and
$m=\frac12(|A|+|B|-|A+B|)$, one has $|A|+|B|=2m+|A+B|$. So the cost minus the own-kernel cost minus $\Delta_b$ is exactly
$2\sum(m-u)(d^\alpha-1)$, the sum over the pairs at one pole (the other pole contributes the same by oddness), plus the residual
antipodal cost minus its flow mass, where $u$ is the own-kernel mass of the pair and $d<1$ the pair distance. With
$H=1/(2\pi(1-\rho)^2)$, which bounds the cross kernel on the disks, $A=u+e$ and $B=-u+f$ (densities) with $|e|,|f|\le H$, and
$|m-u|\le H$: always $m\le\min(|A|,|B|)\le u+H$; if $u\le H$ then $m\ge0\ge u-H$, and if $u>H$ then $A>0>B$ and $m=\min(|A|,|B|)\ge u-H$.
The residual is bounded by the cross kernel, is odd, is paired by $w\leftrightarrow-w$, and has flow mass at most $E(\rho)$. The
bounds $|d^\alpha-1|\le\alpha(-\log d)$ and $|(2|w|)^\alpha-1|\le\alpha L(\rho)$ on the disks (mean value theorem), the pair distance
$d=2r\sin t$ at angle $t\in(0,\frac\pi4)$ from the zero ray, the four pair families at one pole and the log-sine integral
$\int_0^{\pi/4}-\log(2r\sin t)\,dt=-\frac\pi4\log r+\frac{\beta(2)}2$ bound the two errors by
$8\alpha H\int_0^\rho r\big(-\frac\pi4\log r+\frac{\beta(2)}2\big)dr=\alpha B_C(\rho)$ and $\alpha E(\rho)L(\rho)$. For $D_\alpha$ the local plan is the measure-preserving projection plan of Theorem 3.2, perturbed by the
cross kernels, whose total variation is $\|\gamma\|\le2E(\rho)$. A flow-deletion lemma retains on each edge the largest
fraction of the flow compatible with the new marginals. The removed flow has mass $Z\le\|\gamma\|$, and the residual is
odd, paired antipodally, with flow mass $Z+\frac12\int(|\lambda+\gamma|-|\lambda|)\le\frac32\|\gamma\|\le3E(\rho)$, where $\lambda$ and $\lambda+\gamma$ are the marginal densities before and after the perturbation. So the residual costs at most
$3\alpha E(\rho)L(\rho)$ beyond its base, and the removed flow costs at most the integral of $1-d^\alpha\le\alpha(-\log d)$ over the removed
flow. A projection edge at half-lobe angle $t\in(0,\frac\pi4)$ and radius $r<\rho$ has flow density $c\,dr\,dt/r$ with $c=\frac{\sin2t}{2\pi}$
and length $d=r\sin2t$; the own-kernel densities at its source and at its target (radius $r\cos2t$) are $c/r^2$ and
$c/(r^2\cos^22t)$, so the deficiency fractions are at most $Hr^2/c$ and $Hr^2\cos^22t/c$. The lemma removes the larger of the two
fractions, so the removed flow density is at most $Hr\,dr\,dt$. With the four projection families at each pole and
$\int_0^{\pi/4}-\log(r\sin2t)\,dt=\frac\pi4(-\log r+\log2)$, the removed flow costs at most
$8\alpha H\int_0^\rho\frac\pi4r(-\log r+\log2)\,dr=\alpha B_D(\rho)$.

(iii) Write $2a_2\rho^\alpha/\alpha=\frac2{\pi\alpha}e^{h_C(\alpha)}$ with $h_C=\alpha(\log\rho+\frac{\log2}2)-\log(1+\frac\alpha2)$. Then $h_C(0)=0$ and
$h_C'(0)=\ell_C=\log\rho+\frac{\log2}2-\frac12$. Also $h_C'$ is negative and increasing, and $0<h_C''\le\frac14$, so $(e^{h_C})''\le\ell_C^2+\frac14$.
Similarly $2A_\alpha\rho^\alpha/\alpha=\frac2{\pi\alpha}e^{h_D}$ with $h_D'(0)=\ell_D=\log\rho+\log2-1$, and $h_D''$ is positive and decreasing
with $h_D''(0)=1-\frac{\pi^2}{12}$. On $(0,\varepsilon]$, $(2^\alpha-1)/\alpha\le(2^\varepsilon-1)/\varepsilon$ and $T(\alpha)/\alpha\le2^{\varepsilon+1}S(\varepsilon)/\pi$. Taylor's formula in (ii) and the identities
$\frac{2\ell_C}\pi+N_0=C_0$ and $\frac{2\ell_D}\pi+\frac12+N_0=2C_0$ give
$C_\alpha\le\frac2{\pi\alpha}+C_0+K_C\alpha$ and $D_\alpha\le\frac2{\pi\alpha}+2C_0+K_D\alpha$ for $0<\alpha\le\varepsilon$, with

$$K_C=\frac{\ell_C^2+\frac14}\pi+Z+B_C(\rho)+E(\rho)L(\rho),\qquad K_D=\frac{\ell_D^2+1-\frac{\pi^2}{12}}\pi+Z+B_D(\rho)+3E(\rho)L(\rho),$$

$$Z=\frac{2^\varepsilon-1}\varepsilon\big(N_0(\rho)+E(\rho)\big)+\frac{2^{\varepsilon+1}S(\varepsilon)}\pi.$$

At
$\varepsilon=\frac1{100}$, with $\rho=\frac{34891}{100000}$ for $K_C$ and $\rho=\frac{15993}{50000}$ for $K_D$, outward ball evaluation with
$S(\varepsilon)\le S^+_{64}(\varepsilon)$ gives $K_C<2.4754617576$ and, without a reflection saving, $K_D<2.7251476744$. The boxed constant for $D_\alpha$ uses the
saving of Theorem 3.10(b) as well. Since $A_n(\alpha)/\alpha$ decreases in $\alpha$, the saving divided by $\alpha$ is at least
$\sum_{n\ge1}\frac{A_n(\varepsilon)}\varepsilon B^\rho_{2n+1}(c)\rho^{2n}$ on $(0,\varepsilon]$. With $\rho=\frac{31987}{100000}$, the rational centre $c$ given after
Theorem 3.10 and eight terms, this gives $K_D<2.7249482772$. With the terms of Theorem 3.10(c) in their place, which is allowed since
$\widetilde A_n(\alpha)/\alpha$ also decreases in $\alpha$, it gives $K_D<2.7249415501$, and with all the disks of Theorem 3.10(d)
$K_D<2.7249328469$.

(iv) $[f_\alpha]_\alpha\le1$ is Lemma 4.0. Near each pole the zero set is the horizontal line and a curve with fourth-order contact
with the vertical line, so $d=d_0+O(r^4)$, where $d_0$ is the distance to the two perpendicular zero lines of the own kernel.
Expanding $d^\alpha=1+\alpha\log d+O(\alpha^2\log^2d)$ off the pole disks, and treating the disks with the exact angular integral
$2a_2\delta^\alpha/\alpha$, gives the stated expansion with
$\kappa_C=\frac{\ell^2+\frac14}\pi+\frac{\log2}2J_0+\frac{J_1}2$. Here $\ell=\log\delta+\frac{\log2}2-\frac12$ and $J_0=1-\frac4\pi\log\delta$ (from $N(\frac\pi4)=\frac12$). The
term $J_1=\int_{\Omega_\delta}|\nu|\log d+\int_{B_\delta(x)\cup B_\delta(y)}(|\nu|\log d-|\text{own kernel}|\log d_0)$ converges absolutely; it depends
on $\delta$, but the combination defining $\kappa_C$ does not. Combine with (iii).

(v) Fix a geometric radius $\rho>0$, independent of $\alpha$ and sufficiently small, and use the witness of Theorem 5.6 with this $\rho$ in place of
$\rho=\alpha$, clamped in addition to $[-\frac12,\frac12]$ and by the pole cone $-\frac12+|z-x|^\alpha$ (compatible with the half-plane clamp,
since $-h\le-\frac12+|z-x|^\alpha$ with $h=\frac12(2X)^\alpha$ as in Theorem 5.6). Call the result $F_\alpha$ on $\{X>0\}$ and put $\Lambda_\alpha=1+2\alpha^2$. On $B(x,r_0)$ with $r_0\le40\rho$
the map $V$ is $(1+Cr_0^3)$-Lipschitz, so $|F_\alpha(p)-F_\alpha(q)|\le \Lambda_\alpha(1+Cr_0^3)^\alpha|p-q|^\alpha$; every pair with a point outside
$B(x,20\rho)$ has quotient at most one, as in Step 3 of Theorem 5.6. Replace $F_\alpha$ by $\widetilde F_\alpha(p)=\inf_{X(q)>0}[F_\alpha(q)+\Lambda_\alpha|p-q|^\alpha]$.
Because $F_\alpha(p)\le-\frac12+r^\alpha$ with $r=|p-x|$, only points $q$ with $|p-q|<r$ can lower the value, so
$0\le F_\alpha-\widetilde F_\alpha\le C\Lambda_\alpha\alpha r^{\alpha+3}$ near $x$ and $\widetilde F_\alpha=F_\alpha$ outside $B(x,20\rho)$. Then $f_\alpha=\max(\widetilde F_\alpha,-h)$, extended
oddly, has $[f_\alpha]_\alpha\le \Lambda_\alpha$, the pole values $\mp\frac12$, and $|\int\nu(F_\alpha-f_\alpha)|=O(\alpha)$. For the value, fix $\delta<\frac\rho4$. On
$B(x,\delta)$ the flat profile contributes exactly $A_\alpha\delta^\alpha/\alpha$. The difference between the curved and the flat profile,
minus its limit at $\alpha=0$, contributes $O(\alpha)$: the clamps cost $O(\alpha r)+O(\alpha r^{\alpha+3})$; the vertical zero line is displaced
by $O(r^3)$ in angle, which gives a weighted logarithmic error $O(r^3)$ where the curved and flat signs agree and a set of weighted
size $O(r^6(1+|\log r|))$ where they differ. Off the two disks, $|(v^\alpha-1)/\alpha|\le(1+v^{1/4})|\log v|$ for $\alpha\le\frac14$ and the
integrability of the logarithms of the distances give $\int\mu_\delta F_\alpha=\int\mu_\delta F_0+O(\alpha)$, $F_0=\frac12\operatorname{sgn}\nu$.
The limiting constants recombine exactly into $V(\delta)+\Delta(\delta)=\frac12-\frac2\pi\log\delta$, the finite part of Theorem 5.2. With
$\frac{2A_\alpha\delta^\alpha}\alpha=\frac2{\pi\alpha}+\frac2\pi(\log\delta+\log2-1)+O(\alpha)$ and the identity term $+\frac12$, the increment is
$\frac2{\pi\alpha}+2C_0+O(\alpha)$; dividing by $\Lambda_\alpha$ costs $O(\alpha)$. With (iii) this proves (v). $\square$

Numerically (outward evaluation in 384-bit ball arithmetic, rechecked at 768 bits, at rational radii chosen by a
floating-point scan; only their admissibility is used), (ii) with $S\le S^+_{64}$ gives $C_{1/1000}\le637.0245603580$ at $\rho=\frac{218}{625}$, $D_{1/1000}\le637.4271355465$ at $\rho=\frac{1279}{4000}$,
$C_{1/200}\le127.7386138886$ at $\rho=\frac{8717}{25000}$, $D_{1/200}\le128.1421848905$ at $\rho=\frac{31961}{100000}$, $C_{1/100}\le64.0890268187$ at $\rho=\frac{34853}{100000}$ and $D_{1/100}\le64.4938379166$ at $\rho=\frac{3993}{12500}$.
With the saving of Theorem 3.10(b) (eight terms, the centre $c$ given after Theorem 3.10) at $\rho=\frac{31977}{100000}$, $\frac{31963}{100000}$ and $\frac{15973}{50000}$,
$D_{1/1000}\le637.4271353454$, $D_{1/200}\le128.1421838895$ and $D_{1/100}\le64.4938359260$; with part (c),
$D_{1/1000}\le637.4271353386$, $D_{1/200}\le128.1421838557$ and $D_{1/100}\le64.4938358589$; with part (d),
$D_{1/1000}\le637.4271353298$, $D_{1/200}\le128.1421838120$ and $D_{1/100}\le64.4938357721$. Catalan's constant
enters through the exact rational enclosure $\beta_{512}<\beta(2)<\beta_{512}+2^{-512}$, where
$\beta_N=\sum_{k<N}b_kh_k2^{-k-1}$, $b_k=\frac{2\cdot4\cdots(2k)}{3\cdot5\cdots(2k+1)}$ and $h_k=\sum_{j\le k}\frac1{2j+1}$; it follows from
$\beta(2)=\int_0^1\frac{-\log t}{1+t^2}dt$, the expansion $\frac1{1+t^2}=\frac12\sum_k(\frac{1-t^2}2)^k$ and $\int_0^1(-\log t)(1-t^2)^kdt=b_kh_k\in(0,1]$.
These are the best upper values in Table 1 for $C_{1/1000}$, $D_{1/1000}$ and $D_{1/100}$; for $C_{1/100}$ the paired local circles of Theorem 3.7, with Theorems 3.6 and 3.8, give a smaller value. At $\alpha\ge\frac1{20}$ the transport certificates of Section 3 and the closed form $F^{**}$ are smaller.
Statement (iii) is a uniform bound on the whole interval $0<\alpha\le\frac1{100}$ with the sharp first two terms.

## 6. The endpoint $\alpha\to1$

**Theorem 6.1.** $\lim_{\alpha\to1}(1-\alpha)C_\alpha=\lim_{\alpha\to1}(1-\alpha)D_\alpha=\frac{3\sqrt3}{4\pi}=0.4134967\ldots$

*Proof.* Upper: $(1-\alpha)F(\alpha)\to2a_3(1)=\frac{3\sqrt3}{4\pi}$ (Theorem 3.1). Since $(A_\alpha/a_2(\alpha))^{1-\alpha}\to1$, also
$(1-\alpha)G(\alpha)\to\frac{3\sqrt3}{4\pi}$, and $D_\alpha\le G(\alpha)$. Lower: Theorem 4.4 gives $C_\alpha\ge2^{1-\alpha}(M_\alpha+\frac14)$ and
$D_\alpha\ge2^{1-\alpha}M_\alpha$, with $(1-\alpha)2^{1-\alpha}M_\alpha\to\frac{3\sqrt3}{4\pi}$. $\square$

The mechanism is the same in the upper and the lower bound: as $\alpha\to1$ the cost concentrates at large scales,
where the increment density is a dipole with angular profile $\cos3\theta$. The exact angular constant $a_3$ of
Theorem 3.1(a) governs both. The polygonal witness of Theorem 4.5 has the same leading coefficient for every
shape $a>0$. The next term is not determined. The certified bounds at $\alpha=0.99$ give
$0.6532\le C_{0.99}-\frac{3\sqrt3}{4\pi\cdot0.01}\le0.8680$.

## 7. Numerical experiments and their relevance

All statements in this section are numerical observations. None is used in a proof. The rigorous numbers (interval
certificates) are those of Sections 1, 3, 4, 5 and 9, collected in Table 1; other sections only quote them.

1. **Discretized dual problem.** For fixed $\alpha$ and kernel phase $b$, $V(\alpha,b)$ was approximated by a linear
   program: maximize $\sum_im_iu_i$ subject to $u_i-u_j\le|p_i-p_j|^\alpha$ on an adaptive grid. Polar cells are used about
   both poles and about the midpoint, and constraints are added by column generation. In the refinements that were run the values increased; this is an
   observation about those grids, not a proved monotonicity, and the values have no rigorous error control. Diagonal direction, finest grids:

   | $\alpha$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 |
   |---|---|---|---|---|---|---|---|
   | LP value | 6.71 | 3.68 | 2.72 | 2.31 | 2.11 | 2.17 | 2.38 |

   At $\alpha=\frac12$ the value increases with $b$ on $[0,\frac\pi4]$ (2.015, 2.033, 2.058, 2.074, 2.081 on a medium grid),
   consistent with Theorem 5.4 at finite $\alpha$. At $\alpha=0.1$, $0.2$ and $\alpha\ge0.8$ the grids are too coarse: the certified lower
   bound of Table 1 exceeds the LP value. With the identity term included ($D_\alpha$), the LP gives $2.46$ in the diagonal direction at $\alpha=\frac12$, against
   $C_{1/2}\approx2.10$ on the same grid. The optimizer then uses nearly the full admissible jump between the two evaluation
   points. For $D_\alpha$ the maximizing direction depends on $\alpha$. On identical grids the diagonal beats the axis at
   $\alpha=0.1,0.2,0.3$ (for example $7.162$ against $7.095$ at $\alpha=0.1$), but at $\alpha=0.3$ the direction $b=\pi/8$ gives $3.086$
   against $3.079$ (diagonal). At $\alpha=\frac12$ a direction scan gives $2.492$ (axis),
   $2.501$ ($b=\pi/8$), $2.504$ ($b\approx0.29$) and $2.458$ (diagonal). At $\alpha=0.7$ it gives $2.800$ (axis) and $2.709$ (diagonal). The
   upper bounds of Section 3 are uniform in the direction, so none of this affects a certified statement. The diagonal LP
   values give $D_\alpha-\frac2{\pi\alpha}\approx0.796,0.887,0.957$ at $\alpha=0.1,0.2,0.3$, compatible with the limit $2C_0=0.8047$ of
   Theorem 5.6 (the LP values are about one percent low).

   *Relevance.* At $\alpha=0.3$ and $\frac12$ the certified lower bounds of Table 1 lie about 1 percent below the LP
   values; at $\alpha=0.1$ and $0.2$ they lie above them, so these LP values are under-resolved. This suggests that the
   polygonal witnesses are close to extremal at these exponents and that most of the remaining
   gap is in the upper bounds. It is a numerical conjecture that $C_{1/2}\in[2.09,2.12]$ and $D_{1/2}\approx2.5$.

2. **Structure of the optimal plan.** At $\alpha=\frac12$ the LP transport plan moves mass along circles about each pole
   inside the two half-unit disks, along circles about the midpoint outside the unit disk, and by the reflection
   $w_2\mapsto-w_2$ in between. For the far-field density restricted to a circle $|w|=\rho$ about the midpoint,
   floating-point transport estimates (a linear program on 360 sampled atoms per circle, diagonal direction) exceed the
   dipole value $2a_3\rho^{\alpha-2}$ by about 4 percent at $\rho=1$, 0.8 percent at $\rho=1.5$ and 0.25 percent at $\rho=2$, and
   agree with it to four digits for $\rho\ge5$. *Relevance.* These sampled estimates are numerical evidence, not a proof, that among
   plans that move mass only along circles about the midpoint the far-field part of Theorem 3.1 is close to optimal for
   $\rho\ge1.5$. These estimates say nothing about plans
   that move mass between radii, so they do not show that the far-field part is sharp. The slack of $F$ relative to the
   linear-programming value is about 19 percent at $\alpha=\frac12$; Theorems 3.3 to 3.8 reduce it to about 4 percent
   (Theorems 3.5, 3.6 and 3.7 follow the far-field, middle and pole parts of this plan).

3. **Zero-curve witnesses.** A floating-point prototype that uses a polyline near the zero curve of the increment
   density, with the sign taken from the analytic kernel difference, gave $2.0952$ at $\alpha=\frac12$ and $2.7054$ at $\alpha=0.3$.
   This prototype is not an admissible witness (its values can be discontinuous near the polyline), and these numbers are
   exploratory only. For the admissible witness $p_\alpha\circ(\sigma\operatorname{dist}(\cdot,Z))$ with $Z$ a polyline approximation of
   the zero curve (spacing $0.02$), interval computations at $\alpha=\frac1{10},\frac3{10},\frac12,\frac34,\frac9{10}$ gave enclosures
   such as $[2.05078,2.13523]$ at $\alpha=\frac12$ and $[2.65342,2.75261]$ at $\alpha=\frac3{10}$. They are wider than the polygonal
   enclosures and do not improve the lower bounds of Table 1. Whether the witness built on the exact zero curve improves
   on the polygonal one is open.

4. **Second-order seminorm of the projection profile (Theorem 5.6, Step 1).** A grid search over pairs of points, refined
   by local optimization, gives $\sup$ quotient $=1.000153$, $1.000625$, $1.006149$, $1.019092$ at
   $\alpha=0.05,0.1,0.3,0.5$, that is, $([g]_\alpha-1)/\alpha^2=0.0612,0.0625,0.0683,0.0764$. The analytic value on projection
   pairs is $(\log2)^2/8=0.0601$. The maximizing pairs are near the projection pairs at $t\approx\pi/8$. *Relevance.* These values guided the
   proof of Step 1 of Theorem 5.6, which gives the rigorous bound $1+2\alpha^2$. The proof does not use them. At $\alpha=0.3$ and
   $\frac12$ the certified bounds $1.007$ and $1.021$ of Section 4 (after Theorem 4.6) lie just above the values found here.

5. **Checks of exact formulas.** The moment formula $M_n=(-1)^nR_n/(2n)$ of Theorem 5.4 was checked against an
   independent hypergeometric representation to 30 digits for $n\le10$, and against direct quadrature to $2\times10^{-5}$.
   The finite parts $N(0)$ and $N(\pi/4)$ were checked by 50-digit quadrature. The kernel normalization and the
   homogeneous mode values $\lambda_k(\alpha)=\frac{k-\alpha}{2(k+2+\alpha)}$ of $T_{xx}+iT_{xy}$ on $r^\alpha e^{ik\theta}$ were checked
   to $10^{-16}$. All interval certificates were run by two independent programs where stated in the accompanying artifacts. In
   particular, the polygonal witness of Theorem 4.5 was certified a second time by a separate program (second-order
   midpoint rule on adaptive cells, 80-bit ball arithmetic) at ten exponents from $0.05$ to $0.8$ (enclosure widths $0.017$ to
   $0.126$). At each of the ten, the first program, run with the same shape, gives an interval inside the second program's
   enclosure.

## 8. Comparison of $T_{xx}$, $T_{xy}$ and $R_1^2$

1. **$T_{xx}$ and $T_{xy}$ have the same norm for every $\alpha$**, and every bound in this report applies to both. The
   reason is rotation: $U_{\pi/8}^{-1}T_{xx}U_{\pi/8}=\frac1{\sqrt2}(T_{xx}+T_{xy})$, and more generally
   $U_\beta^{-1}T_{xx}U_\beta=\cos2\beta\,T_{xx}+\sin2\beta\,T_{xy}$. Their norm is also that of the real part of
   $\frac12(R_1+iR_2)^2$ in any direction, and half the norm of the Beurling transform from real to complex Hölder spaces.
   On complex inputs the Beurling transform has a strictly larger norm at every exponent, by the factor $\frac\pi2$ as $\alpha\to0$ and
   $\frac{8\pi}{9\sqrt3}$ as $\alpha\to1$ (Theorem 1.4; at $\alpha=\frac12$ the norm $N_{1/2}$ of $S=T_{xx}+iT_{xy}$ on complex inputs, half that of the Beurling transform, is at least $2.9079$ against $C_{1/2}\le2.1935$), whereas $T_{xx}$, $T_{xy}$ and $R_1^2$ have the same norms on real and complex inputs.
2. **$R_1^2=T_{xx}-\frac12I$ (equivalently $R_2^2$, or $T_{xx}+\frac12I$) has a different norm.** Proved relations:
   - $C_\alpha\le D_\alpha\le C_\alpha+\frac12$ for every $\alpha$;
   - $D_\alpha\le G(\alpha)<F(\alpha)+\frac12$, where the projection pairing of Theorem 3.2 uses the identity term to save
     $F(1-(A_\alpha/a_2)^{1-\alpha})$, and $D_\alpha\le U^D_m(\alpha)$; the reflection coupling of Theorem 3.9 gives the strict
     inequality $D_\alpha<G(\alpha)$;
   - $\alpha D_\alpha\to2/\pi$ and $(1-\alpha)D_\alpha\to3\sqrt3/(4\pi)$, exactly as for $C_\alpha$.
3. **The identity term changes the second term, by exactly $C_0$.** $\lim_{\alpha\to0}(D_\alpha-C_\alpha)=C_0=0.4023257$
   (Theorems 5.4 and 5.6). This lies strictly inside the a priori range $[0,\frac12]$ given by $C\le D\le C+\frac12$.
   The gap $D-C$ equals the second term of $C$ itself, because $N(\pi/4)=\frac12$ and $A_0'=2a_2'(0)$. Thus
   $D_\alpha-\frac2{\pi\alpha}\to2C_0$.
4. **Finite $\alpha$.** The certified upper bounds for $D_\alpha$ exceed those for $C_\alpha$ by $0.40$ to $0.47$ in Table 1.
   The strict inequality $C_\alpha<D_\alpha$ is proved at all ten exponents of Table 1: at
   $\alpha=\frac1{1000},\frac1{100},\frac1{20},\frac1{10},\frac15,\frac3{10}$ by the projection witness of Theorem 4.6, and at
   $\alpha=\frac1{10},\frac15,\frac3{10},\frac12,\frac34,\frac9{10},\frac{99}{100}$ by the half-plane lattice witnesses of Theorem 4.7 (see the boxed inequalities of Section 0).
   The certified gaps $D_\alpha-C_\alpha$ are at least $0.3094$, $0.2821$, $0.2326$, $0.1934$, $0.2147$, $0.2435$, $0.2608$, $0.2560$, $0.2346$ and $0.1625$ at these ten exponents. Strict separation also holds for all sufficiently small
   positive $\alpha$, since $D_\alpha-C_\alpha\to C_0>0$ (item 3); no explicit threshold is claimed. By the continuity of Theorem 1.5 it also
   holds on an explicit closed interval around each of the ten exponents (radii from $5\cdot10^{-8}$ at $\alpha=\frac1{1000}$ to $0.003$ at
   $\alpha=\frac3{10}$; the remarks after Theorem 1.5). A proof of $C_\alpha<D_\alpha$ for every
   $0<\alpha<1$ is still open. Numerically, $D_{1/2}\approx2.5$ against $C_{1/2}\approx2.10$ (Section 7). A clamped witness with an asymmetric
   Hölder profile $t\mapsto M(At_+^\alpha-(1-A)t_-^\alpha)$, admissible for every $\alpha$, was also evaluated in floating
   point. It falls below $L(\alpha)$ for $\alpha\ge0.3$: the clamp $|f|\le\frac12(2X)^\alpha$ costs more than the identity term gains.
5. **Mechanism.** For $C_\alpha$ the lower-bound witnesses of Theorem 4.5 vanish at both evaluation points, and the upper
   bound of Theorem 3.1 charges the local cost at each pole by the reflection constant $a_2(\alpha)$. Whether extremal
   functions for $C_\alpha$ vanish at the evaluation points is not proved. For $R_1^2$ the identity term pays for unequal
   values at the evaluation points. Locally, the projection constant $A_\alpha<a_2(\alpha)$ plus a positive remainder of
   mass $1/\pi$ replaces the reflection constant. This saving appears only through the combination $T_{xx}-\frac12I$, and
   it is invisible to a triangle-inequality argument.


## 9. The remaining gap

**Asymptotic gap.**

| quantity | lower bound | upper bound | status |
|---|---|---|---|
| coefficient of $1/\alpha$ in $C_\alpha$, $D_\alpha$ | $2/\pi$ | $2/\pi$ | sharp |
| $\lim(C_\alpha-\frac2{\pi\alpha})$ | $C_0=0.4023257139\ldots$ | $C_0$ | sharp |
| $\lim(D_\alpha-\frac2{\pi\alpha})$ | $2C_0=0.8046514279\ldots$ | $2C_0$ | sharp |
| coefficient of $1/(1-\alpha)$ in $C_\alpha$, $D_\alpha$ | $3\sqrt3/(4\pi)$ | $3\sqrt3/(4\pi)$ | sharp |

The closed-form upper bounds have the correct coefficient of $1/\alpha$ but not the correct constant term:
$F(\alpha)-\frac2{\pi\alpha}\to0.7220896$ against the sharp $C_0=0.4023257$, and $G(\alpha)-\frac2{\pi\alpha}\to1.1244153$ against the
sharp $2C_0=0.8046514$. The closed forms $F^{**}$, $G^*$ of Theorem 9.3 reduce these limits to $0.4202545$ and $0.8573802$. The
explicit bounds $J_C$, $J_D$ of Theorem 5.7 have the sharp limits $C_0$ and $2C_0$, with an error at most $2.4755\alpha$, respectively $2.7250\alpha$, for
$\alpha\le\frac1{100}$. At $\alpha=0.001$ the best certified upper bound of Table 1 exceeds $\frac2{\pi\alpha}$ by at most $0.4048$ for $C_\alpha$ and $0.8074$ for
$D_\alpha$, against the limits $C_0=0.4023$ and $2C_0=0.8047$; the certified lower bound $L$ exceeds $\frac2{\pi\alpha}$ by at least $0.3994$.

**Finite-$\alpha$ gap.** At the exponents of Table 1, the certified ratio of upper to lower bound for $C_\alpha$ is
1.0001, 1.0004, 1.0024, 1.0059, 1.0155, 1.0271, 1.0500, 1.0564, 1.0333 and 1.0052. The largest is at $\alpha=0.75$. For
$D_\alpha$ the ratios are 1.0002, 1.0020, 1.0148, 1.0343, 1.0568, 1.0665, 1.0778, 1.0700, 1.0435 and 1.0072. The gap for $D_\alpha$ is larger on both sides: at $\alpha=\frac12$ the
numerical value of Section 7 (about $2.50$) is about $2$ percent above the certified lower bound, and the certified upper bound
exceeds it by about $6$ percent. Numerically $D_\alpha-C_\alpha\approx0.4$ at $\alpha=\frac12$ (Section 7). At $\alpha=\frac12$: $2.089155\le C_{1/2}\le2.193410$ and
$2.454214\le D_{1/2}\le2.645079$.

**Theorem 9.1 (uniform comparison near the endpoints).** Let $F_b$ be $F$ with $b_\alpha$ replaced by $\frac{2^{\alpha+1}}{3\pi}$, so that
$F\le F_b$. Let $L_1$ be as in Theorem 4.1 and $H(\alpha)=2^{1-\alpha}(M_\alpha+\frac14)$ as in Theorem 4.4. Then

$$\frac{F_b(\alpha)}{L_1(\alpha)}\le1.0172482934\quad(0<\alpha\le0.005),\qquad \frac{F_b(\alpha)}{H(\alpha)}\le1.0262309397\quad(0.995\le\alpha<1).$$

Hence $L_1(\alpha)\le C_\alpha\le F(\alpha)\le1.0173\,L_1(\alpha)$ on the first interval and $H(\alpha)\le C_\alpha\le F(\alpha)\le1.0263\,H(\alpha)$ on
the second.

*Proof.* At $\alpha=0$, multiply numerator and denominator by $\alpha$. The ratio becomes
$\frac{2a_2s^\alpha/(1-\alpha)}{(\sqrt2-1)^\alpha[4/(\pi(\alpha+2))-\alpha/4]}$, continuous on $[0,0.005]$ with positive denominator. Near $\alpha=1$, with
$\delta=1-\alpha$: $\sin((\alpha+2)t)\ge\frac{\alpha+2}3\sin3t$ on $[0,\frac\pi6]$ (concavity of sine), $\sin^\alpha t\ge\sin t$, and
$\int_0^{\pi/6}\sin3t\sin t\,dt=\frac{\sqrt3}{16}$. With $\delta/\sin(\pi\delta/6)\ge6/\pi$ this gives
$\delta H(\alpha)\ge\frac{(\alpha+1)(\alpha+2)\sqrt3}{8\pi}+\frac{2^{1-\alpha}\delta}4$. The ratio is then at most a nonsingular expression on $[0.995,1]$. Both
expressions are enclosed on the whole interval by 256-bit interval arithmetic, with interval exponent arguments
(not by sampling). $\square$

**Theorem 9.2 (uniform comparison on $(0,1)$).** Let $\ell(\alpha)=L_1(\alpha)$ (Theorem 4.1) for $0<\alpha<\frac1{200}$,
$\ell(\alpha)=H(\alpha)$ (Theorem 4.4) for $\frac{199}{200}<\alpha<1$, and $\ell(\alpha)=I(\alpha,a_0)$ (Theorem 4.5) for
$\frac1{200}\le\alpha\le\frac{199}{200}$, where the shape $a_0$ is fixed on each of the following groups, numbered $0$ to $7$ from left to right (at a shared
endpoint either group may be used, since both statements hold there):

| group | $[\frac1{200},\frac{19}{100}]$ | $[\frac{19}{100},\frac7{20}]$ | $[\frac7{20},\frac12]$ | $[\frac12,\frac35]$ | $[\frac35,\frac7{10}]$ | $[\frac7{10},\frac45]$ | $[\frac45,\frac9{10}]$ | $[\frac9{10},\frac{199}{200}]$ |
|---|---|---|---|---|---|---|---|---|
| $a_0$ | $\frac{14}{25}$ | $\frac{53}{100}$ | $\frac{97}{200}$ | $\frac{89}{200}$ | $\frac{39}{100}$ | $\frac{33}{100}$ | $\frac{53}{200}$ | $\frac15$ |

Then, for every $0<\alpha<1$,

$$\ell(\alpha)\le C_\alpha\le1.0625\,\ell(\alpha),\qquad \ell(\alpha)\le D_\alpha\le1.2894\,\ell(\alpha).$$

On $[\frac1{200},\frac{199}{200}]$ the ratios are at most $1.0624909995$ and $1.2893632771$.

*Proof.* The lower bounds are Theorems 4.1, 4.4 and 4.5 together with $D_\alpha\ge C_\alpha$. On the two end intervals the
upper bounds for $C_\alpha$ are Theorem 9.1. For $D_\alpha$ there, $D_\alpha\le C_\alpha+\frac12$; on $(0,\frac1{200}]$ the function
$L_1(\alpha)=(\sqrt2-1)^\alpha\big(\frac4{\pi\alpha(\alpha+2)}-\frac14\big)$ is a product of two positive decreasing functions, so
$L_1\ge L_1(\frac1{200})\ge126.199$ and $D_\alpha/L_1(\alpha)\le1.0172482934+0.5/126.199\le1.0213$; on $[\frac{199}{200},1)$ the proof of
Theorem 9.1 gives $(1-\alpha)H(\alpha)\ge\frac{(\alpha+1)(\alpha+2)\sqrt3}{8\pi}\ge0.411775$, so $H\ge82.355$ and $D_\alpha/H(\alpha)\le1.0262309397+0.5/82.355\le1.0324$.

On the middle interval let $U_C(\alpha)$, $U_D(\alpha)$ be the right sides of Theorem 3.5 with $m=16$ phase intervals, the
compact part given by the reflection-orbit integral of Theorem 3.4 on $384^2$ rectangles, and the exterior part with $512$
angular cells and $128$ radial intervals. On each group the integer transport plans of the exterior part are chosen once,
at a reference exponent of the group, and kept fixed; feasibility rests on exact integer marginals only. On the groups
in $[\frac7{20},\frac9{10}]$ let also $U^{(3.7)}_C(\alpha)$ be the right side of Theorem 3.7 with $\delta=\frac1{64}$, $m=16$, paired
local circles with $512$ cells and $256$ radial bins (flows chosen by a greedy order of floating distances, hence the same
for all $\alpha$), middle circles of Theorem 3.6 with $512$ cells and $512$ bins (integer plans per group, chosen at the
reference exponent), and the exterior part above.

(i) For fixed plans, $\log U_C$ and $\log U_D$ are convex in $\alpha$. Every term is a nonnegative combination of functions
$c^\alpha$ ($c>0$) or of moments $\int d(\omega)^\alpha\,d\mu(\omega)$ with $\mu\ge0$, $d>0$, which are log-convex by Hölder's
inequality; sums, products, positive multiples and finite maxima of log-convex functions are log-convex. The local terms
$\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}$ (and, for $D$, the Gamma-ratio term plus $\frac12$) have positive second
logarithmic derivative. In the compact part the plan selected at each point by the comparison of the two pair masses
does not depend on $\alpha$, because the difference of the two candidate costs is a fixed multiple of
$h^\alpha+v^\alpha-\delta^\alpha\ge0$. The tail of the exterior part uses an explicit upper replacement of its angular coefficients
that is a moment in $\alpha$. The same holds for $U^{(3.7)}_C$: $S_\alpha(\delta)$ is log-convex, the same-circle local costs are
moments $\int_a^b(c\,r)^\alpha\frac{dr}r$, and all other local and middle costs are nonnegative combinations of $c^\alpha$ with
coefficients that do not depend on $\alpha$.

(ii) For fixed $a$, $I(\alpha,a)/\alpha=\frac12\int_0^\infty(2t)^\alpha J_a(t)\,\frac{dt}t$ with $J_a>0$ (Theorem 4.5), so
$\log(I(\alpha,a)/\alpha)$ is convex.

(iii) Interpolation. Let $a<b$ be consecutive upper nodes with certified $U(a)\le A$, $U(b)\le B$. By (i),
$\log U\le E$ on $[a,b]$, where $E$ is the chord through $(a,\log A)$ and $(b,\log B)$. Let $x_0<x_1<x_2<x_3$ be consecutive lower
nodes of one group with $[x_1,x_2]\subset[a,b]$ and certified enclosures of $I(x_i,a_0)/x_i$ (the lower nodes of each group, all
computed with its shape $a_0$, include one node beyond each end of the group's interval, so $x_0$ and $x_3$ exist for every segment). By (ii), the secant lines $L_1$
through the nodes $x_0,x_1$ (used for $t\ge x_1$) and $L_2$ through $x_2,x_3$ (used for $t\le x_2$), formed with the lower
endpoint at the inner node and the upper endpoint at the outer node, lie below $\log(I(t,a_0)/t)$. For any rational
$c\in[x_1,x_2]$ the functions $E(t)-\log t-L_i(t)$ are convex, so the maximum of $\log(U/I)$ over $[x_1,x_2]$ is at most the
largest of the values of $E-\log t-L_1$ at $x_1,c$ and of $E-\log t-L_2$ at $c,x_2$. These are evaluated in 200-bit ball
arithmetic at exact rational points. Where both $U_C$ and $U^{(3.7)}_C$ are available, each is interpolated separately with
its own plans and the smaller of the two segment bounds is used.

(iv) The nodal certificates are the computations of Theorems 3.4, 3.5 and 4.5 at $59$ upper nodes (spacing $\frac1{40}$
on $[\frac14,\frac9{10}]$, finer towards both ends) and at the lower nodes of each group. The maxima over all segments are
$\log\rho_C\le0.060617$ (attained in the Theorem 3.7 family on $[\frac{27}{40},\frac7{10}]$) and $\log\rho_D\le0.25415$ (rounded). The
ratios stated above are the exponentials of the unrounded certified maxima, not of these rounded logarithms. All nodal certificates were recomputed independently, and the combination was repeated
independently at 256 bits and at 90 digits, with the same constants. $\square$

The constant for $C_\alpha$ is limited by the fixed shapes and plans per group, not by the bounds at a single exponent: at
the exponents of Table 1 the ratios for $C_\alpha$ are smaller. The constant for $D_\alpha$ is limited mainly by the lower
function $\ell$, which bounds $C_\alpha$: already at $\alpha=\frac12$ Table 1 gives $2.645079/2.089155>1.266$ for this quotient. With Theorem 3.5 alone (no Theorem 3.7 family) the same procedure gives
$1.0825$ for $C_\alpha$.

**Theorem 9.3 (closed-form bounds for every exponent).** Put
$\kappa=\frac{209}{500}$, $c_C=\frac{1353}{2500}$, $c_D=\frac{72}{125}$ and

$$F^{**}(\alpha)=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{\kappa}{1-\alpha}+c_C,\qquad
G^*(\alpha)=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac{\kappa}{1-\alpha}+c_D+\frac12 .$$

Then $C_\alpha\le F^{**}(\alpha)$ and $D_\alpha\le G^*(\alpha)$ for every $0<\alpha<1$. As $\alpha\to0$,
$F^{**}-\frac2{\pi\alpha}\to\frac{2398}{2500}-\frac{1+\log2}\pi=0.4202545\ldots$ and $G^*-\frac2{\pi\alpha}\to\frac{747}{500}-\frac2\pi=0.8573802\ldots$
(sharp values $C_0=0.4023257\ldots$ and $2C_0=0.8046514\ldots$; for $F$ and $G$ the limits are $0.7220896$ and $1.1244153$). As
$\alpha\to1$, $(1-\alpha)F^{**}$ and $(1-\alpha)G^*$ tend to $0.418$ (sharp value $\frac{3\sqrt3}{4\pi}=0.4134967\ldots$).

The first term of $F^{**}$ is the local term $2^{1-\alpha}a_2(\alpha)/\alpha$ of Theorem 3.5, and the first term of $G^*$ is its
analogue for $R_1^2$. Part (A) of the proof also gives $C_\alpha\le F^*:=F^{**}+0.0348$; part (B) improves this with the
paired local circles of Theorem 3.7, which bound $C_\alpha$ only. The bound $F^{**}+\frac12$ for $D_\alpha$ is weaker than $G^*$:
$F^{**}+\frac12-G^*=Q(\alpha)-0.0348$ with $Q(\alpha)=\frac{2^{1-\alpha}(a_2(\alpha)-A_\alpha)}\alpha=\frac4\pi\int_0^{\pi/4}\sin2t\,\sin^\alpha t\,\frac{1-\cos^\alpha t}\alpha\,dt$,
which decreases in $\alpha$ (both factors $\sin^\alpha t$ and $\frac{1-\cos^\alpha t}\alpha$ decrease), so $Q(\alpha)>Q(1)=\frac{2\sqrt2}{3\pi}-\frac14=0.0501\ldots$.
Both parts and their computations were checked independently: for (A) with a separate computation of the node at
$\alpha=0$, an analytic maximization on each chord segment in place of the subdivision of step (5), and a separate check of
$[\frac{199}{200},1]$; for (B) with a recomputation of the node at $\alpha=0$ that does not use the transport code, adaptive
dyadic pieces in 320-bit arithmetic on every segment, and a separate series for $a_3$ on $[\frac{199}{200},1]$.

*Proof.* (A) The bound for $D_\alpha$ (and $C_\alpha\le F^*$). (1) Theorem 3.5 with $m=16$ and the compact part of Theorem 3.4 has the form $C_\alpha\le L_C(\alpha)+R(\alpha)$ and
$D_\alpha\le L_D(\alpha)+R(\alpha)$ with the same remainder
$R=\sec\frac\pi{64}\max_j(\widetilde M_\alpha(\phi_j)+E_\alpha(\phi_j))$, $L_C=2^{1-\alpha}a_2/\alpha$, $L_D=2^{1-\alpha}A_\alpha/\alpha+\frac12$. With the
plans of the proof of Theorem 9.2 fixed on each group, $R=R_g$ is one explicit function of $\alpha$ on group $g$, and the two
inequalities hold for every $\alpha$ in the group. (2) By Theorem 9.2 (i), $\log R_g$ is convex. (3) At the $59$ upper nodes of
Theorem 9.2, subtracting the exact lower endpoint of $L_C$ from the certified upper value of $L_C+R_g$ gives an upper value
for $R_g$; the same subtraction for $D$ agrees to $10^{-8}$, and the larger value is kept. (4) Every term of $R_g$ on the first
group has a finite limit as $\alpha\to0^+$ (the integrands of $\widetilde M_\alpha$ are bounded on a fixed compact set, and the series
of $E_\alpha$ is dominated uniformly for $\alpha\le\frac12$), so $R_g$ extends continuously to $\alpha=0$. The same certified
computation, run at $\alpha=0$ with the same grids and plans, gives $R_g(0^+)\le0.993975$; the same run reproduces the stored
certificate at $\alpha=\frac1{200}$ exactly. (5) On each of the $59$ segments between consecutive nodes, $\log R_g$ lies below the
chord of the nodal values. Each segment is cut into $4000$ rational pieces, and on each piece the larger endpoint value of
the exponentiated chord is compared with $\frac\kappa{1-p}+c_D$ at the left end $p$ in 256-bit ball arithmetic. The smallest margin is
$2.4\cdot10^{-5}$, at $\alpha=0$. This proves $R\le\frac\kappa{1-\alpha}+c_D$ on $(0,\frac{199}{200}]$. (6) On $[\frac{199}{200},1)$ use $C_\alpha\le F_b(\alpha)$
(Theorem 9.1) and $D_\alpha\le C_\alpha+\frac12$. With $\delta=1-\alpha$, $\delta F_b(\alpha)=2a_2s^\alpha/\alpha$ with $s=(2a_3+\delta\frac{2^{\alpha+1}}{3\pi})/(2a_2)$,
which is continuous up to $\alpha=1$. The inequalities $2a_2s^\alpha/\alpha<\delta L_C+\kappa+c_D\delta$ and $2a_2s^\alpha/\alpha<\delta(L_D-\frac12)+\kappa+c_D\delta$
are verified on $200$ closed subintervals with interval exponent arguments, with smallest margins $0.0031$ and $0.0029$.
Dividing by $\delta$ gives $F_b<F^*$ and $F_b+\frac12<G^*$ there.

(B) The bound for $C_\alpha$. Theorem 3.7 with $\delta=\frac1{64}$ and $m=16$ gives $C_\alpha\le S_\alpha(\delta)+R_{37}(\alpha)$, with
$S_\alpha(\delta)=\frac{2a_2\delta^\alpha}\alpha+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2}$ and $R_{37}$ equal to $\sec\frac\pi{64}$ times the phase maximum of the
paired local, middle and exterior circle terms. Write $S_\alpha(\delta)=L_C+g(\alpha)$. Since $\int_\delta^{1/2}u^{\alpha-1}du=\frac{2^{-\alpha}-\delta^\alpha}\alpha$,
$g(\alpha)=-2a_2\int_\delta^{1/2}u^{\alpha-1}du+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2}$, which extends continuously to $\alpha=0$ and is
increasing on $[0,\frac78]$, because $a_2$ and the integral are positive and decreasing there ($(\log a_2)'=\frac{\log2}2-\frac1{\alpha+2}<0$ for
$\alpha<0.885$). Fix the plans on each group of Theorem 9.2: greedy local flows, which do not depend on $\alpha$, and middle and
exterior plans chosen at the reference exponent of the group. Then $\log R_{37}$ is convex on each group, by the argument of
Theorem 9.2 (i). Certified upper values of $R_{37}$ at the nodes come from the computations behind Theorem 9.2 (groups $2$ to $6$)
and from new computations with the same grids (groups $0$, $1$, $7$). At $\alpha=0$ every term has a finite limit, given by the
same formulas with powers of positive numbers replaced by $1$ and $\frac{b^\alpha-a^\alpha}\alpha$ by $\log\frac ba$; the certified value is
$R_{37}(0^+)\le3.16526$. On each of the $59$ segments the chord bound for $R_{37}$, the bound for $g$ (monotone for $\alpha\le\frac78$,
enclosed in ball arithmetic beyond) and $\frac\kappa{1-p}+c_C$ are compared on $4000$ rational pieces in 256-bit ball arithmetic. The
smallest margin is $1.6\cdot10^{-4}$, at $\alpha=0$; this proves $g+R_{37}\le\frac\kappa{1-\alpha}+c_C$ on $(0,\frac{199}{200}]$. On $[\frac{199}{200},1)$
step (6) holds with $c_C$ in place of $c_D$, with smallest margin $0.0029$. $\square$

At the exponents of Table 1 (upper endpoints rounded up):

| $\alpha$ | 0.001 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|---|---|---|
| $F^{**}$ | 637.040753 | 64.089516 | 13.189650 | 6.862161 | 3.763643 | 2.801398 | 2.233731 | 2.689226 | 5.078314 | 42.646407 |
| $G^*$ | 637.477946 | 64.527310 | 13.630069 | 7.305753 | 4.213236 | 3.256565 | 2.698894 | 3.165019 | 5.559634 | 43.130775 |

In floating evaluation $F^{**}<F$ for $\alpha$ below about $0.98$ and $G^*<G$ for $\alpha$ below about $0.973$; all four bounds are valid
everywhere, so $\min(F,F^{**})$ and $\min(G,G^*)$ are upper bounds. At the exponents of Table 1, $F^{**}$ exceeds the best certified
bound for $C_\alpha$ by at most $0.17$ percent at $\alpha\le\frac1{10}$ and by at most $2.0$ percent at every exponent of the table; $G^*$
exceeds the best certified value for $D_\alpha$ by at most $0.3$ percent at $\alpha\le\frac1{10}$ and by at most $2.2$ percent at every exponent
of the table. The losses come from the interpolation, from the single constants $c_C$ and $c_D$, which are forced by the node
$\alpha=0$, and near $\alpha=1$ from $\kappa>\frac{3\sqrt3}{4\pi}$.

## 10. Unresolved steps

1. **Exact $C_\alpha$ and $D_\alpha$ at fixed $\alpha$.** Not determined for any $0<\alpha<1$. The certified relative gap for $C_\alpha$
   is at most 5.7 percent at the listed exponents. At $\alpha=0.3$ and $\frac12$ the numerical values of Section 7 lie
   about 1 percent above the certified lower bounds (at smaller $\alpha$ the grids are too coarse), which suggests that the upper bounds carry most of the gap.
2. **Lower bounds for $D_\alpha$ at moderate $\alpha$.** Theorem 4.6 gives certified values, and the strict separation
   $C_\alpha<D_\alpha$, at the listed exponents $\alpha\le\frac3{10}$ (at $\alpha=\frac1{10},\frac15,\frac3{10}$ superseded by the larger values of Theorem 4.7). Its admissibility proof covers $\alpha\le\frac12$, but it does not reach $L(\alpha)$ at
   $\alpha=\frac12$. Theorem 4.7 gives certified values above $L(\alpha)$, and the separation, at
   $\alpha=\frac1{10},\frac15,\frac3{10},\frac12,\frac34,\frac9{10},\frac{99}{100}$; the certified ratio for $D_\alpha$ is still $1.0665$ at $\alpha=0.3$ and $1.0778$
   at $\alpha=\frac12$ (Table 1). Whether $C_\alpha<D_\alpha$ for every $\alpha$ is open; it is proved at the ten exponents of Table 1, on an explicit closed
   interval around each of them (Theorem 1.5 and the remarks after it), and for all sufficiently small $\alpha$. A continuous variant without the
   midline clamp, $f=\frac12(|z-x|^\alpha-|z-y|^\alpha)+\Psi$ with $\Psi$ a signed projection profile on both branches of the graph,
   has proved seminorm at most $2$ for $\alpha\le\frac23$ (see the accompanying artifacts); a numerical search at
   $\alpha=\frac12$ suggests seminorm about $1.14$ and a quotient near $2.13$, which would exceed $L(\frac12)$, but the sharper
   seminorm is not proved and no bound is claimed from it. The numerical optimizers for $D_\alpha$ keep
   the far field of the $C_\alpha$-optimizer together with the full jump $f(x)-f(y)\approx-1$ and one-signed local profiles,
   without the clamp $|f|\le\frac12(2X)^\alpha$ used in Theorem 4.6. Two admissible constructions of that type were checked.
   (a) The balanced cone envelope $\frac12\big(\min_i(v_i+|z-p_i|^\alpha)+\max_i(v_i-|z-p_i|^\alpha)\big)$ of the optimized node values
   $v_i$ at nodes $p_i$ has seminorm at most one for any input values. At $\alpha=\frac12$ it interpolates the linear-programming
   nodes to within $5.2\cdot10^{-13}$, but two independent continuous quadratures of its functional give about $1.65$, against
   the discrete objective $2.49$: between nodes the envelope rises like $d^\alpha$ from each node, and the kernel integrates
   this. (b) Clamping the $C_\alpha$ witness to prescribed pole values $\pm c$ by lattice operations preserves the seminorm,
   but at $\alpha=\frac12$ the functional decreases as $c$ increases from $0$. Neither gives a certified improvement; both
   evaluations are diagnostic. So the node values of the discrete optimizer are not a shortcut to a continuous witness.
   A third construction does increase the functional numerically. For the axis phase, the half-plane lattice lemma
   (see the accompanying artifacts) turns any $F$ on $\{X>0\}$ (coordinates centered at the midpoint of the
   poles) with $[F]\le1$ and $F(x)\le-\frac12$ into an admissible odd $f$ with $D_\alpha\ge2|J|+\frac12$, $J$ the principal-value
   integral of the increment density against $f$ over the half-plane. With $F=\min(g_0+c,\,-\frac12+\lambda P(z-x))$, where $g_0$
   is the signed-distance witness of the exact axis zero set, $P$ the projection profile of Theorem 4.6 rotated by $\frac\pi4$,
   $\lambda$ the reciprocal of its seminorm and $c\approx-0.15$, midpoint quadratures give about $3.03$ ($\alpha=0.3$), $2.46$
   ($\alpha=\frac12$), $2.894$ ($\alpha=\frac34$) and $5.25$ ($\alpha=0.9$, with an estimated seminorm). At $\alpha=0.3$, $\frac12$ and
   $0.9$ they exceed the certified lower bounds $3.0161$, $2.4542$ and $5.2413$ of Table 1; at $\alpha=\frac34$ the value lies slightly
   below the certified lower bound $2.8948$, which uses $c=-\frac3{10}$. All four exceed the certified upper bounds for
   $C_\alpha$. They are
   numerical values, not bounds. At $\alpha=\frac12$ the same witness (with $c=-\frac3{20}$ and $\lambda=\frac{1000}{1021}$) is certified
   by a two-dimensional cell enclosure with the homogeneous tail and the pole-disk lemma at $2.4542$ (Theorem 4.7(iv), (vii)), at $\alpha=0.3$ (with $c=0$, $b=\frac32$, $\lambda=\frac{1000}{1007}$) at
   $2.9418$ (Theorem 4.7(v)), at $\alpha=\frac34$ (with $c=-\frac3{10}$, $b=\frac34$, $\lambda=\frac{50}{53}$) at $2.8948$ (Theorem 4.7(vi), (vii)), and at
   $\alpha=\frac9{10}$ (with $c=-\frac3{10}$, $b=\frac7{20}$, $\lambda=\frac{10}{11}$) at $5.2413$ (Theorem 4.7(vii)). At $\alpha=\frac15$ and $\alpha=0.3$ the witness with
   $c=-\frac1{20}$, $b=\frac38$ and $\lambda=\frac{1000}{1011}$, respectively $\lambda=\frac{1000}{1007}$, is certified at $3.9578$ and $3.0161$ by sharper Stieltjes sums
   (Theorem 4.7(viii)); at $\alpha=\frac1{10}$ the same witness with $c=-\frac1{40}$ and $\lambda=\frac{1000}{1003}$ is certified at $7.0445$, above
   the value $7.0259$ of Theorem 4.6.
3. **Third terms.** For $C_\alpha$ the remainder is $O(\alpha)$ in both directions (Theorem 5.7), but the limit of
   $(C_\alpha-\frac2{\pi\alpha}-C_0)/\alpha$ is not known to exist. Its $\liminf$ is at least the explicit integral $\kappa_C$ of Theorem 5.7(iv)
   (not evaluated numerically) and its $\limsup$ is at most $2.4755$ (Theorem 5.7(iii)). For $D_\alpha$ both remainders are $O(\alpha)$ (Theorem 5.7(v)); the lower constant is not evaluated, and the existence of the limit of $(D_\alpha-\frac2{\pi\alpha}-2C_0)/\alpha$ is open.
4. **Second term at $\alpha\to1$.** Only $0.6532\le C_{0.99}-\frac{3\sqrt3}{4\pi\cdot0.01}\le0.8680$ is known at one exponent.
5. **Finite-$\alpha$ direction maximality.** Whether the diagonal phase maximizes $V(\alpha,b)$ for every fixed $\alpha$ is
   open. Numerics support it at $\alpha=\frac12$ and suggest it may fail for $\alpha\ge0.8$. For $D_\alpha$ the numerics indicate
   that the diagonal is not the maximizing direction at $\alpha=\frac12$ and $\alpha=0.7$ (Section 7), although the diagonal
   attains the sharp second term $2C_0$ of Theorem 5.6. None of the bounds of this report depends on these questions: the upper bounds cover all phases, and the
   lower bounds use one phase.
6. **Uniform-in-$\alpha$ ratio.** Theorem 9.2 gives the ratios $1.0625$ for $C_\alpha$ and $1.2894$ for $D_\alpha$ on all of
   $(0,1)$. They are limited by the fixed polygon shapes and transport plans on each group; for $D_\alpha$ the main
   limitation is that $\ell$ is a lower bound for $C_\alpha$, while the larger lower bounds of Theorems 4.6 and 4.7 are certified
   only at single exponents (item 2).
7. **Sharper explicit upper bounds.** The numerics of Section 7 indicate that an explicit three-region transport plan
   (pole circles, a reflection region, circles about the midpoint) would come within a few percent of the truth at
   $\alpha=\frac12$. The exterior and middle parts are certified finite transports on circles (Theorems 3.5 and 3.6), and
   at every exponent of Table 1 so are the pole disks (Theorem 3.7; at $0.001$ the resulting bound is weaker than Theorem 5.7(ii)).
   A version of Theorem 3.7 for $D_\alpha$ that transports the local terms, with the identity term, together with the cross-disk
   and middle terms is the next step (see the end of this item). Theorem 3.10 lowers the identity term by only about $1.6\cdot10^{-4}$ at $\alpha=\frac12$ (Theorem 3.9 by about
   $1.4\cdot10^{-4}$; the two savings are alternatives and are not added). Two
   floating linear programs (discretization errors not controlled; the programs are in the accompanying artifacts) indicate where
   the remaining slack may lie. For the optimal coupling of the two translated measures $\mu_R$, $R=\frac12$, of Theorem 3.9 they give savings
   of only $0.0005$ to $0.0014$ at $\alpha=0.3,\frac12,\frac34$ and the phases tested. For the functional outside the two pole disks at
   $\alpha=\frac12$ and the phases $\phi_j=j\pi/32$ of Section 3, $j=0,4,8,12,16$, the certified exterior and middle terms of Theorems 3.5 and 3.6 (without the
   middle-arc residual saving, about $0.0025$) exceed the linear-programming value by $0.040$ to $0.068$: about $0.015$ in the exterior
   circles, $0.014$ to $0.040$ in the per-arc plans of the middle region, and $0.011$ to $0.014$ from treating the middle region and the
   exterior separately. The exterior part is slack within the circles (in the plans or the cell bounds) together with the
   discretization uncertainty: on the well-conditioned region $1\le|w-w_0|\le10^3$ about the midpoint $w_0$ of the poles, a program that couples only
   points of the same circle has the same value, to six decimals, as the unrestricted one at $\alpha=\frac12$ and $\frac34$ and at $\phi=0$ and
   $\frac\pi2$, so coupling different circles gains nothing measurable there. The corresponding totals are $0.10$ to $0.13$ at $\alpha=\frac34$ and $0.03$ to $0.05$ at $\alpha=0.3$. When the cross kernels inside
   the two pole disks are included, the certified middle, cross-disk and exterior terms exceed the linear-programming value by $0.050$
   to $0.086$ at $\alpha=\frac12$ (about $0.04$ in the middle region, $0.02$ in the cross-disk plans, $0.015$ in the exterior circles and $0.01$
   from treating the regions separately) and by $0.11$ to $0.15$ at $\alpha=\frac34$. A two-point program, calibrated by its deficit on the local functional
   of a single pole disk (whose exact value is known; the transfer to the full functional is heuristic), puts the largest phase value at about $2.11$ for $C_{1/2}$ and $2.50$ to $2.51$ for $D_{1/2}$. On these
   sampled values, of the excess of about $0.14$ of the certified upper bound for $D_{1/2}$, about $0.08$ is slack in the middle,
   cross-disk and exterior plans, about $0.05$ to $0.06$ comes from bounding the local terms separately from the rest, and less than
   $0.003$ is in the phase interpolation and the identity term; for $C_{1/2}$ nearly all of the excess of about $0.08$ is plan slack.
   With the same calibration, and with the exterior tail included, the largest sampled phase value for $D_\alpha$ is about $2.90$ at
   $\alpha=\frac34$, close to the certified lower bound $2.894834$; at $\alpha=0.3$ the sampled phase values are about $3.08$ to $3.11$, up to
   about $0.09$ above the certified lower bound $3.016191$. A third floating program treats the local functional of $D_{1/2}$ alone (the
   own-pole kernels inside both pole disks of radius $\frac12$ and the two identity atoms). At the phases $0$, $\frac\pi4$, $\frac{11\pi}{32}$ and
   $\frac\pi2$ the certified local term (projection pairing plus $\frac12$) exceeds its value by $0.005$ to $0.018$. On the local functional
   of $C_{1/2}$ the same program falls $0.003$ below the certified local term at $\phi=\frac\pi2$, where that term is attained exactly by a
   signed-distance function. At every other phase modulo $\pi$, in particular at $0$, $\frac\pi4$ and $\frac{11\pi}{32}$, the local functional of $C_\alpha$
   is strictly smaller than the certified term for every $\alpha$ (short proofs are in the accompanying artifacts), so there the gap is not only discretization. Transferring
   the deficit $0.003$ measured at $\phi=\frac\pi2$ to the other phases and to the local functional of $D_{1/2}$, which is a heuristic and
   not an error estimate, leaves about $0.002$ to $0.015$. At $\alpha=\frac34$ and the phases $0$ and $\frac{11\pi}{32}$ the excesses are
   $0.009$ and $0.020$, while the program falls about $0.003$ below the certified local term of $C_{3/4}$ at both phases. So a version of
   Theorem 3.7 for $D_\alpha$ that stays inside the pole disks could gain only about $0.01$ at $\alpha=\frac12$ and about $0.02$ at
   $\alpha=\frac34$; most of the $0.05$ to $0.06$ above requires coupling the disk terms with the cross-disk and middle terms. These are
   numerical observations, not
   proofs; the calibration is assumed, not established. Independently of these programs, the bound
   $|P_Rf(z)|\le\frac{A_\alpha}\alpha R^\alpha[f]_\alpha$ in the proof of Theorem 3.2 is not sharp for any $\alpha$. At $R=1$, in the
   half-lobe $0<v<u$ the pairing sends $p=(u,v)$ to $a(p)=\frac{2uv}{u^2+v^2}(v,u)$, and the gradient of the cost $|p-a|^\alpha$ in $p$,
   taken at $a=a(p)$, has curl $2\alpha^2uv(u^2-v^2)^{\alpha-1}(u^2+v^2)^{-1-\alpha/2}>0$. Re-pairing a cycle of $4n$ small source disks
   on the boundary of the rectangle $[\frac25,\frac45]\times[\frac1{10},\frac15]$, each source to the target of the next one, permutes the
   targets and lowers the cost by an explicit amount. With $n=\lceil10625/\alpha\rceil$ and $\varepsilon=\alpha/(150000n)$ this gives
   $|P_Rf(z)|\le(\frac{A_\alpha}\alpha-\delta_\alpha)R^\alpha[f]_\alpha$ with $\delta_\alpha=\alpha^2\varepsilon^2/12500$, so $G(\alpha)$ remains an upper bound
   with $A_\alpha$ replaced by $A_\alpha-\alpha\delta_\alpha$ (proof in the accompanying artifacts). The gain is about $5\cdot10^{-25}$ at $\alpha=\frac12$ and changes
   no displayed decimal, and whether it adds to the savings of Theorems 3.9 and 3.10 was not checked. It shows that the
   projection plan itself, and not only its coupling with the other terms, is strictly improvable.
8. **Restricted symmetry classes.** For the whole-plane operator norms the question is settled by Theorem 1.1: restricting
   to functions odd or even in each variable does not change $C_\alpha$ or $D_\alpha$. Problems with a fixed evaluation pair near
   the axes, or on bounded domains, were not studied.
9. **Duality.** Theorem 1.3 proves that $C_\alpha$ and $D_\alpha$ are limits of finite-measure transport problems with explicit
   truncation errors. A certified upper bound from a discrete transport plan would in addition need certified cell masses
   and spatial errors much smaller than the uniform bound $h^\alpha|\mu|(\mathbb R^2)$; this was not carried out beyond the circle
   transports of Theorems 3.5 to 3.7.

## 11. Accompanying artifacts

The accompanying artifacts contain a reading-order index that maps the theorems of this report to their complete
written proofs, independent checks, certified data and exact reproduction commands. The proofs are organized by topic:

- the setup and approximation lemma, the angular lemma and the upper bounds;
- the projection, midpoint, orbit, exterior-circle, middle-circle and paired local-circle bounds;
- the witness families;
- the balanced and radial residual couplings of Theorem 3.7 and their evaluation on the existing certificates, with the values
  of Table 1;
- the middle-arc residual cost of Theorem 3.6, its replay on the middle-circle certificates and the resulting values of
  Table 1, including the direct certificates of Theorem 3.7;
- the exact phase interpolation of Theorem 3.8, its independent evaluation and the resulting values of Table 1,
  and the recombination of Theorem 3.6 on the direct certificates at $\alpha=\frac15,\frac{99}{100}$;
- the finer cross-disk enclosures used with Theorem 3.6 ($2048^2$ and $4096^2$ rectangles) and their recombination with
  the phase interpolation;
- the strict saving of Theorem 3.9: disk containment, radial density, the retained-edge cutoff form, the fourth-moment
  bound and its evaluated savings (Section 3; Table 1 uses Theorem 3.10(d)), including the exact radial density and its
  values on the $4096^2$ enclosure;
- the larger disks and the full even-moment saving of Theorem 3.10, including the values without part (c), the values
  for part (c), and the exact geometry check for part (d), with the values of Table 1 and of Theorem 5.7;
- the corollary that $C_\alpha<D_\alpha$ for all sufficiently small $\alpha$;
- the small-$\alpha$ theorems, including the exact second terms of $C_\alpha$ and $D_\alpha$ and the explicit bounds of Theorem 5.7,
  the rational cutoff values used in Table 1, the sharper deficiencies, the rational enclosure of Catalan's constant,
  and the exact exterior series $S$ and its values;
- the endpoint ratio theorem;
- the transport approximation, parity, full-norm and complex-input theorems of Section 1, continuity in the exponent,
  and the existence of extremal functions.

The accompanying artifacts also provide the references and their exact statements, and the direct proof of the periodic
constants of Section 2. The copied papers themselves are not included. The interval-arithmetic certification programs
use Python with python-flint/Arb; their certified output is JSON with interval enclosures, safe decimal endpoints and source hashes.

The accompanying artifacts include the certifier, runner and combination program for Theorem 4.7(v), with its eight chunk
certificates and combined certificate, and the sharper certifier, plans, chunk certificates and independent checks for
Theorem 4.7(viii). They also include the direct Theorem 3.7 certificates at
$\alpha=\frac1{1000},\frac1{100},\frac1{20},\frac1{10},\frac15,\frac{99}{100}$ and their independent audit.
The cell enclosures of Theorem 4.7(iv), (vi) and (vii) include the homogeneous-tail proof and its numerical values,
the pole-disk lemma, the complete fine replays at $\alpha=\frac12$ and $\alpha=\frac34$, and the still finer computations at
those exponents with their structural audits and selected replays.

For part (B) of Theorem 9.3, the accompanying artifacts include the proof, node certificates of groups $0$, $1$, $7$ for the
Theorem 3.7 remainder, the computation at $\alpha=0$, the chord and endpoint checks, and the independent check.
For part (A), they include the proof, node remainders, the computation at $\alpha=0$, the chord and endpoint checks,
and the independent check. The accompanying artifacts also include the exact one-dimensional reductions and finite-part
checks of Section 5, Table 1 with the source family of each entry, and the program that regenerates it from the certificates.
The inputs, outputs and exact commands for the numerical experiments of Section 7 and for the certified polygonal and
lattice witness runs are included in the accompanying artifacts.

The JSON certificates of the five largest collections are packed with relative paths; the accompanying artifacts give
an exact command to restore them. Two collections of intermediate per-row replay records used by the residual-cost
combinations of Theorems 3.6 and 3.7 are not included; the accompanying artifacts give the commands that regenerate them.
Run logs are not included. Recorded source hashes identify the original audited files; the accompanying artifacts are
reading copies with path edits, so those historical hashes need not match the edited copies.

All interval computations use outward rounding: upper bounds are upper interval endpoints rounded up, lower bounds
lower endpoints rounded down. The certificates are deterministic; numerical worker counts are recorded in the accompanying artifacts.

## 12. Time spent

The run started at $T_0=$ 2026-10-28T00:20:16Z (logged start). The planned 16-hour window ran to its cap: the run was stopped
at its scheduled end, 2026-10-28T16:20:16Z. This final version was completed at $T_{\rm end}=$ 2026-10-28T16:35:01Z, over 16 h 14 min after $T_0$.
The time after the stop was used only for this summary, the run record and the packaging of the accompanying artifacts; no
new mathematics or computation was done in it.

Actual work time. Working sessions ran from 00:21Z to 06:21Z, from 06:22Z to 12:22Z and from 12:22Z to 16:12Z,
about 15.8 hours in total, followed by a short closing check at 16:13Z and the final editorial pass after the stop. The
independent verification and the numerical computations ran concurrently over the same window. The proof and verification work
shared a small number of processor cores (from about 01:50Z, one to three cores) on a machine also used by other jobs.
Some numerical runs used multiple worker processes, as recorded in the accompanying artifacts. No remote or cluster computing was used.

