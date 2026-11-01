# Prime denominators force a first-resonance obstruction

Status: CONFIRMED after independent adversarial review, 2026-10-31T03:52:43Z. See V049 and topic43 for the exact scope and evidence.

## Statement

Let `p>=5` be an odd prime and let `a` be an even integer satisfying `4<=a<p`. Set

\[
 \delta=\frac ap,\qquad c=\frac p{p-a},\qquad f_1(\theta)=\sin\theta.
\]

Generate the pure stationary density and stream coefficients by the recurrence of topic 01, using the unique nonresonant stream inverse through order `p-1`. The first stream resonance is at order `p`, with angular stream index `j_0=a/2-1`. Let `kappa` be the coefficient of `sin((a-3)theta)` in `f_p`.

Then `kappa` is rational with denominator not divisible by `p`, and

\[
 \boxed{\kappa\equiv(-1)^{(a-4)/2}\pmod p.}
 \tag{1}
\]

In particular `kappa!=0`, so the pure stream recurrence is obstructed at its first resonance.

Such rational parameters are dense in `(0,1)`. Consequently hypothesis (H) in topic 15 holds on every nonempty open subinterval of `(0,1)` for this fixed leading datum. Subject to the independently audited Baire argument there, a dense residual set of irrational parameters has zero radius of convergence of its pure far-field density series. This does not say that every irrational parameter diverges; the Brjuno convergence class still has full measure.

## Notation for reduction

Write `Z_(p)` for the rational numbers whose denominator is not divisible by `p`. Coefficientwise congruences below are in `Z_(p)` modulo `p`. We can work with Laurent polynomials in `w=exp(i theta)` after adjoining `i`, since `2` and `i` are units for odd `p`. Identities of rational trigonometric functions can first be checked in the localization that also inverts `cos(theta)` and then returned to Laurent polynomials when the denominators cancel.

Use `s=sin(theta)`, `q=cos(theta)` in this proof only; `q` here is not a continued-fraction denominator. For arbitrary order `n`, the radial density exponent is `1-n delta`, and the stream exponent is `P_n=2-n delta`. Let `D` mean differentiation in `theta` until the generating-function paragraph, where the distinct operator `E=z partial_z` is introduced.

## 1. Reduction of the exact recurrence

The first resonance order is `p`: since `a` is even and coprime to `p`, `n delta` is an even integer first at `n=p`, where it equals `a>=4`. At every order `i<p`, each stream coefficient is

\[
 b_{i,j}=\frac p2\left[
  -\frac{a_{i,j-1}}{p(2j+2)-ia}
  +\frac{a_{i,j}}{p(2j-2)+ia}\right].
 \tag{2}
\]

Every displayed denominator is a unit in `Z_(p)`, because `1<=i<p` and `p` does not divide `a`. Thus, if `f_i` has coefficients in `Z_(p)`, then `g_i` has coefficients in `p Z_(p)` and

\[
 \frac{g_i}{p}\equiv \frac{q f_i}{ia}\pmod p.
 \tag{3}
\]

The identity uses `q sin((2k+1)theta)=(sin((2k+2)theta)+sin(2k theta))/2`. Its zero-frequency contribution when `k=0` is zero, so it introduces no extra mode.

Multiplying (3) by the radial exponents gives, for `i,j<p`,

\[
 P_i g_i\equiv-q f_i,\qquad
 (1-j\delta)g_i'\equiv-\frac ji(q f_i)'\pmod p.
 \tag{4}
\]

The density denominator is `(n-1)(c-1)=(n-1)a/(p-a)`. For `2<=n<=p` it is a unit and is congruent to `-(n-1)`. Induction therefore proves that every `f_n`, `n<=p`, is `p`-integral and that its reduction is obtained from the universal recurrence

\[
 F_1=s,\qquad
 (n-1)F_n=
 \sum_{i+j=n}\left[qF_iF_j'-\frac ji(qF_i)'F_j\right],
 \quad 2\le n\le p.
 \tag{5}
\]

Here the universal sequence can first be defined over the rational numbers for every `n`. For `n<=p`, all denominators introduced in (5) are units modulo `p`, since `i<=n-1<p` and `n-1<p`. Thus reduction of this sequence is legitimate and equals the exact IPM coefficients through order `p`.

## 2. A generating identity for the universal sequence

Define formal power series over rational trigonometric functions by

\[
 U(z,\theta)=\sum_{n\ge1}F_n(\theta)z^n,
 \qquad V(z,\theta)=\sum_{n\ge1}\frac{F_n(\theta)}n z^n,
 \qquad A=qV,
\]

so `E A=qU` for `E=z partial_z`. Summing (5) yields

\[
 (1+A_\theta)E U-qU U_\theta=U.
 \tag{6}
\]

Let `h` be any local antiderivative of `sec(theta)`. Define `H=theta+A` and the formal vector field

\[
 \mathcal L=(1+A_\theta)E-(EA)\partial_\theta.
\]

Then `L H=0`. Equation (6) gives `L U=U`, while `L h(theta)=-(EA)/q=-U`. Hence both `U+h(theta)` and `h(H)` are first integrals of `L`. Their difference has zero constant term in `z`. Since `L=E+O(z)`, a formal first integral with zero constant term must vanish: its first nonzero coefficient of degree `n>=1` would be multiplied by `n`. Therefore

\[
 U=h(\theta+A)-h(\theta),\qquad
 E A=v(A):=q\,[h(\theta+A)-h(\theta)].
 \tag{7}
\]

This argument takes place in characteristic zero. The differences of local primitives in (7) have the same formal Taylor series and are independent of the additive constant of `h`. Write

\[
 v(T)=T+\sum_{k\ge2}v_kT^k,
 \qquad v_k=\frac{q}{k!}D^{k-1}(\sec\theta),
 \qquad A_1=qs.
 \tag{8}
\]

The coefficients of `D^r sec(theta)` are integers as rational trigonometric functions. For `k<p`, `v_k` is consequently `p`-integral. The coefficient equation from (7) is

\[
 (n-1)A_n=\sum_{k=2}^n v_k[z^n]A^k.
 \tag{9}
\]

It proves that `A_n` is `p`-integral for `n<p`. At `n=p`, the terms with `k<p` are still integral and the only possible denominator factor `p` comes from `v_p`. Multiplying (9) by `p` gives

\[
 pA_p\equiv-pv_p A_1^p\pmod p,
\]

where the congruence is between integral quantities: `p v_p=q D^(p-1)sec(theta)/(p-1)!`. Since `F_p=pA_p/q`, Wilson's identity `(p-1)! == -1 (mod p)` yields

\[
 F_p\equiv D^{p-1}(\sec\theta)\,(qs)^p\pmod p.
 \tag{10}
\]

## 3. The characteristic-p trigonometric identity

Put `m=(p-1)/2`. In characteristic `p`,

\[
 D^{p-1}(\sec\theta)=(-1)^m\sec\theta-(\sec\theta)^p.
 \tag{11}
\]

Here is a direct verification. In the formal variable `w`,

\[
 \sec\theta=\frac{2w}{1+w^2}
  =2\sum_{k\ge0}(-1)^k w^{2k+1},\qquad D=iw\partial_w.
\]

The operator `(w partial_w)^(p-1)` keeps the monomials whose exponent is not divisible by `p` and kills the others. This follows from Fermat's identity for each integer exponent. The exponents divisible by `p` occur at `k=m+pj`; their subseries is `(-1)^m(sec(theta))^p`, by Frobenius and `2^p=2`. Since `i^(p-1)=(-1)^m`, equation (11) follows as a formal power-series identity and therefore as a rational-function identity.

Equations (10) and (11) give the explicit reduction

\[
 F_p\equiv s^p\left[(-1)^m q^{p-1}-1\right].
 \tag{12}
\]

To read its sine amplitudes, use the finite trigonometric identity, valid for odd `p`,

\[
 \sum_{\ell=0}^{p-1}(-1)^\ell\sin((2\ell+1)\theta)
  =\frac{\sin(p\theta)\cos(p\theta)}{\cos\theta}.
\]

In characteristic `p`, `sin(p theta)=(-1)^m s^p` and `cos(p theta)=q^p`. Thus (12) is exactly

\[
 \boxed{
 F_p\equiv\sum_{\ell=0}^{p-1}(-1)^\ell\sin((2\ell+1)\theta)
            -(-1)^m\sin(p\theta)\pmod p.}
 \tag{13}
\]

Its coefficient is `(-1)^ell` in every odd mode `2ell+1` from `1` to `2p-1`, except that the coefficient at mode `p` is zero.

The resonant density mode is `a-3=2ell+1`, with `ell=(a-4)/2`. Since `4<=a<p`, this index is nonnegative and strictly below `m`. Equation (13) proves (1). In particular no cancellation over the rational numbers can make `kappa` zero.

## 4. Density and the divergence consequence

Let `I` be a nonempty open subinterval of `(0,1)`. There are arbitrarily large odd primes. For all sufficiently large such `p`, the interval `p I` contains an even integer `a` with `4<=a<p`, because consecutive even integers are distance two apart and `I` is bounded away from both endpoints after replacing it by a smaller closed subinterval. Therefore the obstructed parameters in this theorem meet every open interval.

Topic 15 already proves the needed mechanism at each incompatible first resonance: the following density coefficient has a nonzero pole in the parameter, and these poles generate open dense sets where coefficient roots exceed any prescribed constant at arbitrarily late orders. The prime denominators here are unbounded in every interval, so the required arbitrarily late orders are available. Intersecting these open dense sets with the irrationals gives a dense residual set with infinite coefficient-root limsup and hence zero radius of convergence.

The conclusion concerns the pure expansion for the fixed input `sin(theta)`. It does not obstruct a logarithmic repair at rational parameters, does not assert failure at a Brjuno parameter, and does not give an explicitly named divergent irrational. Its measure is zero by the full-measure Brjuno convergence theorem.

## Verification and scope

The finite exact scan in topic 24 provides 21 prime-denominator cases satisfying this theorem, and each exact rational compatibility coefficient has the residue predicted by (1). Separately, direct rational evaluation of the universal recurrence checks every coefficient in (13) for each odd prime through 43. These are diagnostic checks; the all-prime result follows from the proof above.

Dependencies: the exact IPM recurrence and stream inverse in topic 01; the first-resonance obstruction and pole mechanism in topics 03 and 15; elementary formal-series algebra, Fermat's identity, Wilson's identity, and unboundedness of primes. No theorem-prover build or remote computation is used.

## 5. Extension to rational profiles with a nonzero first sine coefficient

The same argument proves a broader statement. Let

\[
 f_1(\theta)=\sum_{m\text{ odd},\ 1\le m\le L}\alpha_m\sin(m\theta),
 \qquad \alpha_m\in\mathbb Q,\quad \alpha_1\ne0.
\]

For every odd prime `p` that divides none of the input denominators or the numerator of `alpha_1`, and every even `4<=a<p`, the first-resonance coefficient satisfies

\[
 \kappa\equiv\alpha_1(-1)^{(a-4)/2}\pmod p,
 \tag{14}
\]

and is nonzero. Consequently incompatible rationals are dense for every such fixed profile, including the exactly extracted Candidate 007 leading density.

To prove this, repeat Sections 1 and 2 with arbitrary `F_1=f_1`. The generating identity is unchanged, and now `A_1=q f_1`. Thus (10) and (11) give

\[
 F_p\equiv f_1^p[(-1)^m q^{p-1}-1]\pmod p,
 \qquad m=(p-1)/2.
\]

By Frobenius, `f_1^p` is the sum of `alpha_k^p sin(k theta)^p` over its odd input frequencies. For every input frequency `k>=3`, its powered sine has only frequencies `kp` and `-kp`. Multiplication by `q^(p-1)` can shift them by at most `p-1`, so the smallest resulting absolute frequency is at least `2p+1`. Such input frequencies do not contribute to the resonant density mode `a-3`, which is positive and below `p`. The only contribution comes from `alpha_1^p sin(theta)^p` and is precisely `alpha_1^p` times (13). Fermat's identity gives `alpha_1^p=alpha_1` modulo `p`. This proves (14).

Only finitely many primes are excluded by the fixed rational input, so the density argument is unchanged. For a nonzero irrational scalar multiple of one of these rational profiles, homogeneity of the exact recurrence also preserves every nonzero compatibility coefficient. The claim does not cover every analytic profile or every finite real coefficient vector.
