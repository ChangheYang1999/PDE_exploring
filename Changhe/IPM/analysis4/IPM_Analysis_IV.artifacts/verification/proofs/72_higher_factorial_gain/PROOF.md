# Higher factorial decay when the leading resonant transfer vanishes

Status: CONFIRMED after independent theory-part review and verifier recheck at 2026-10-31T05:42:01Z. The theorem strengthens the fixed-deficit result of topic67 and does not control the sum over all deficits.

## Statement

Fix an integer Q>=3, delta=2/Q, c=Q/(Q-2), and a nonzero finite real S1 leading sine polynomial. Use the canonical logarithmic recurrence with all resonant stream constants zero. Let R(k) be the exact homogeneous cycle transfer defined in topic67.

Assume that for an integer s>=0 and a nonzero real number lambda_s,

    kR(k)=lambda_s k^(-s)+O(k^(-s-1)).                       (1)

For each fixed integer deficit d>=0, put q=k-1-d. For every density position1<=r<=Q and stream position0<=r<Q,

    limsup_(k->infinity)
      [(k!)^s q! ||[t^q]F_(Qk+r)||_A0]^(1/k)
        <=(d+1)^(s+1)|lambda_s|,                            (2)

and the same inequality holds for G_(Qk+r). Terms with q<0 are omitted. Thus every fixed-deficit column has an additional factor (k!)^(-s) in its decay, up to an arbitrarily small enlargement of the geometric constant.

There are only two possibilities for the exact cycle: either it is eventually identically zero, or(1) holds for a unique integer s>=0. In the first case every fixed-deficit column has finite support in k. In particular, a profile with Lambda=lim kR(k)=0 either has eventual zero transfer or satisfies(2) with s>=1.

## 1. Why the alternatives are exhaustive

For sufficiently large k, the finite Q-step cycle has only finitely many angular offsets from m_k=2k-2, and no negative-frequency reflection changes its formula. Every coefficient is then a rational function of k, with fixed real coefficients determined by the leading data. Topic67 proves that kR(k) is bounded at infinity.

A nonzero bounded rational function has an expansion of the form(1): subtract denominator degree from numerator degree to get the integer -s, and divide leading coefficients to get lambda_s. If the rational function is zero, the cycle is zero at all sufficiently large integer k. The finite-support induction in topic68 then applies without any further harmonic-lattice hypothesis: lower-deficit forcing has finite support, and an eventual zero homogeneous transfer cannot propagate it indefinitely.

## 2. Normalized scalar recurrence

Let a_(k,d) be the resonant sine coefficient in [t^(k-1-d)]G_(Qk). Topic67 gives

    A_(k+1,d)=kR(k)A_(k,d)+S_(k,d),
    A_(k,d)=(k-1-d)! a_(k,d),                               (3)

where S uses only strictly smaller deficits. Set

    B_(k,d)=(k!)^s A_(k,d).

The homogeneous factor in its recurrence is

    (k+1)^s kR(k) -> lambda_s.                              (4)

All linear reconstruction steps at a fixed deficit have norms bounded by a fixed power of k. Changing a block index by a fixed integer changes a factorial ratio by at most a fixed power of k. Therefore the extra normalization (k!)^s preserves that polynomial-loss property.

At deficit0 the inhomogeneous term eventually vanishes. Equation(4) gives the bound |lambda_s| in(2), first for the scalar and then for the other positions in the block.

## 3. The nonlinear induction

Fix d>=1 and suppose(2) holds at smaller deficits. Write p=s+1. Given beta>|lambda_s|, the normalized smaller-deficit columns admit bounds

    ||B_(j,a)|| <= C_a [(a+1)^p beta]^j,  a<d.              (5)

Consider a quadratic term with child block indices i,j, deficits a,b and target block k. The grading of topic67 gives a+b<=d-1; all discrepancies between k and i+j, and between log degrees and block indices, are bounded by constants depending only on d and Q.

The q!-normalization supplies a binomial coefficient. The additional (k!)^s-normalization supplies the s-th power of k!/(i!j!). After changing the bounded index offsets, the resulting coefficient is at most

    C k^M binom(k,i)^(s+1).                                (6)

Here C,M may depend on d,Q,s. To justify the offset step explicitly, for any fixed nonnegative h and integer x>=h, x!/(x-h)! is a product of h integers at most k when x<=k+O(1), and its reciprocal is at most1. Every shifted factorial ratio is therefore bounded by a fixed power of k. The finitely many endpoint indices are treated as low-child linear terms.

For nonnegative x,y and integer p>=1,

    sum_(i=0)^k binom(k,i)^p x^i y^(k-i)
       <=(x^(1/p)+y^(1/p))^(pk).                           (7)

Indeed set v_i=binom(k,i)x^(i/p)y^((k-i)/p). Then sum_i v_i^p<=(sum_i v_i)^p, and the binomial theorem evaluates the sum.

Use x=(a+1)^p beta and y=(b+1)^p beta in(7). Since a+b+2<=d+1, the forcing in the B recurrence has exponential rate at most

    (d+1)^p beta,                                         (8)

up to the polynomial factor in(6). Linear smaller-deficit terms have no larger rate. The same holds for known higher log columns in the triangular inverses, because they have smaller deficit and only polynomial reconstruction factors.

Variation of constants in(3)-(4) now gives every rate strictly larger than(d+1)^p |lambda_s| for B_(k,d). Let beta decrease to |lambda_s| and absorb the polynomial factors in an arbitrarily small enlargement of the exponential base. This proves(2) by induction.

## 4. Scope and a concrete cancellation family

At s=0 this is exactly topic67. At a zero of the cubic Lambda for f_1=sin(theta)+b sin(3theta), one can compute the next coefficient mu=lim k[kR(k)-Lambda] by a first-order expansion of the finite cycle. If mu is nonzero at that root, then s=1 and the bound in(2) is (d+1)^2|mu|.

The constants and polynomial losses still depend on d. Even an additional factorial in every fixed-deficit column does not justify summing all deficits at once. Full rational-log convergence remains OPEN.

## 5. Exact first correction for the two-mode family

For Q=3 and f_1=sin(theta)+b sin(3theta), define

    P(b)=314-2925b+6735b^2+75b^3,
    M(b)=-3022+34665b-68355b^2-105225b^3.

The finite cycle has the exact asymptotic expansion

    kR(k)=P(b)/259200 + M(b)/(1555200 k) + O(k^-2).          (9)

The following first-order construction derives (9) without fitting finite numerical values. Put u=1/k, m_k=2k-2, delta=2/Q, c=Q/(Q-2), and a_r=(r-1)(c-1). At stage r a high-frequency mode is sin((m_k+s)theta), and its coefficient is a jet h_0+h_1 u. The known low coefficients are F_j and G_i from the ordinary recurrence through order Q. The high stationary denominator is 2ck+a_r.

For a high stream in position i and a low density mode ell in position j=r-i, set P_0=2-delta i and p=1-delta j. Its multipliers c_0+c_1u to output offsets s+ell and s-ell respectively are

    c_0^+=-(ell+p)/(2c),
    c_1^+=(P_0 ell-p(s-2))/(4c)+(ell+p)a_r/(4c^2),
    c_0^-=(p-ell)/(2c),
    c_1^-=(P_0 ell+p(s-2))/(4c)-(p-ell)a_r/(4c^2).          (10)

For a low stream at i with exponent P=2-delta i and frequency ell, and a high density at j=r-i with p_0=1-delta j, the multipliers are

    c_0^+=(P+ell)/(2c),
    c_1^+=(P(s-2)-p_0 ell)/(4c)-(P+ell)a_r/(4c^2),
    c_0^-=(ell-P)/(2c),
    c_1^-=-(P(s-2)+p_0 ell)/(4c)-(ell-P)a_r/(4c^2).         (11)

These follow directly from the sine product rules in -p_j G_i'F_j+P_i G_i F_j' and the expansion of (2ck+a_r)^-1. A low amplitude a times a high jet h contributes a h_0 c_0 at degree0 and a(h_1 c_0+h_0 c_1) at degree1 in u.

Start with G_0 consisting of the unit jet at offset0. Sum (10)-(11) to obtain each high density F_r. For r<Q the Poisson inverse sends an offset s upward with the exact multiplier

    -1/[2(s+1-delta r)],

and downward with multiplier u/8+O(u^2). The latter follows by expanding 1/[2(4k+s-5+delta r)]. Thus this is a finite computation in R[u]/(u^2). If H_0+H_1u is the offset1 jet of F_Q, the terminal resonance gives Lambda=-H_0/2 and mu=-H_1/2. Applying this construction in the exact polynomial ring Q[b] gives (9). The source code and coefficient arrays are retained alongside this proof.

The polynomials P and M are coprime. A direct certificate is UP+VM=1, with common denominator D=19306372617932 and

    D U=24014074497265-170337847355521b-193133035907445b^2,
    D V=2488786571649-12393602074097b-137657188815b^2.        (12)

Consequently every root of P has a nonzero first correction mu=M/1555200, so s=1 at all three roots. Exact rational sign bisection gives three disjoint roots, hence all roots of the cubic. Their approximate locations and certified mu intervals are

| b | mu |
|---|---|
| -90.232729881809653230176974210755 +/- 3.26e-31 | 49347.977276519807999427726456682 +/- 4.43e-28 |
| 0.19598724390804628835602429852753 +/- 1.94e-33 | 0.00022773481067505900335485392565091 +/- 4.68e-36 |
| 0.23674263790160694182094991222779 +/- 3.13e-33 | -0.000027402766822634877959683632177192 +/- 2.08e-37 |

Exact rational interval endpoints, rather than the displayed decimal midpoints, are authoritative. They are retained in verification/first_jet.json. The first two positive roots provide low-mode profiles with the fixed-deficit bound (d+1)^2|mu| after normalization by k!q!.

## 6. Verification and scope

The exact jet computation recovers the known pure-sine correction mu=-1511/777600 from the independently derived rational cycle. It is also compared with24 exact finite Cartesian cycles, at b=-1,0,1/10,1/5,1/4,1 and k=32,64,128,256. These comparisons record the finite differences and do not replace the formal jet identity. There are252 exact rational tests of the binomial power inequality. All tests pass; the complete run took0.6697266572155058 seconds of actual elapsed time.

The all-order statement (2) and its proof were independently reviewed and are CONFIRMED; see the closure below. The explicit jet identities, coprimality certificate and isolating intervals are exact finite claims. Neither gives a bound uniform in d, so full rational-log convergence is still OPEN.

## Review closure

2026-10-31T05:42:01Z: The all-order fixed-deficit gain and rational-cycle alternatives are confirmed. The independent review checked the exact inequalities and recurrence shifts. It is retained in sources/lead_review_20261031T0538Z.md. The finite checks supplement the argument; the proof does not rely on finite enumeration.

## 7. Additional exact rational-function audit

An independent check keeps the complete rational dependence on the block index k before expanding at infinity. The Cartesian low-order coefficients supply F_1,F_2,F_3,G_1,G_2,G_3. Write each high frequency as w=2k-2+s. For a high stream and low density at frequency ell, the two Jacobian multipliers are (P_high ell-p_low w)/2 and (P_high ell+p_low w)/2. For a low stream and high density, they are (P_low w-p_high ell)/2 and -(P_low w+p_high ell)/2. Divide by the exact stationary denominator6k+2(r-1). Retain both Poisson channels with exact multipliers -1/[2(w+1+P_high)] and1/[2(w-1-P_high)]. The terminal transfer is -[offset1 of F_3]/2. These identities hold once k exceeds the finite reflection threshold.

For each of four distinct rational b values, compute this full rational function in k and extract its leading two coefficients by exact numerator/denominator polynomial arithmetic. The coefficient of each power of1/k is a polynomial in b of degree at most3: every response term has exactly three leading leaves and all denominators are independent of b. Agreement at four distinct b values therefore proves the polynomial identities for Lambda and mu. This provides an independent check of the truncated-jet implementation. The resulting exact rational functions and comparisons will be retained in verification/exact_rational_first_jet.json.

The additional audit passed at b=-1,0,1/5,1 and at12 exact finite Cartesian cycles. The rational-function numerator and denominator degrees are11 except in the pure-sine specialization, where both are7. Their first two coefficients agree exactly with(9) at all four distinct b values, independently confirming the two cubic polynomial identities. Actual runtime35.164776858873665 seconds. The complete rational functions are retained in verification/exact_rational_first_jet.json.
