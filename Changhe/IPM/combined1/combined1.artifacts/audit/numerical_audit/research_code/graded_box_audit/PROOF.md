# Independent rational enclosure of the graded forcing box

## Statement and scope

This audit concerns the scalar inequalities in T4's frozen graded closure theorem, copied to data/T4_PROOF.md. It does not reprove the underlying inverse or nonlinear theorem and does not assert that any reference satisfies its background or forcing hypotheses.

Let s=1/50000, let the component radius vector in order (P,a,b,H) be

r=(1/5000,1/3000000,1/50000000,1/30000000),

and let the forcing bound vector in the same order be

phi=(25/1572864,25/201326592,25/805306368,205/6442450944).

The audit verifies positivity of the four margins, the low feedback denominator, and r-Gamma; it also verifies the claimed contraction ratio less than 3331/1000000. All calculations use exact rational interval endpoints with rationally bounded square roots. This is an independent arithmetic path from T4's Arb256 calculation.

## Definitions

Put n=sqrt(r_P^2+2r_a^2+r_b^2), nu=n/sqrt(s), A=127/50+(653/5)s, B=(9/5)(1+44s), and

m_H=19/5-2s,
m_0=11/4-3882s-(3/10)nu,
m_1=9/10-4290s-(13/10)nu,
m_2=1/2-4708s-(A+B)nu.

Set q=476s+nu, kappa=q/m_H, alpha=347/5+5440s+B nu, beta=10+34816s and

Gamma_b=(phi_b/m_0+phi_H/(m_H sqrt(m_0)))/(1-kappa/sqrt(m_0)),
Gamma_H=phi_H/m_H+kappa Gamma_b,
Gamma_a=(phi_a+(6+1360s)Gamma_b)/m_1,
Gamma_P=(phi_P+alpha Gamma_a+beta Gamma_b)/m_2+sqrt(40/m_2)Gamma_a.

The pointwise gradient bound is d=n/(2 sqrt(pi s(1+s))) and the low contraction ratio is d/(19/5-d).

## Rational interval method

For closed rational intervals, addition and subtraction use endpoint sums and differences. Multiplication takes the smallest and largest of the four endpoint products. Division multiplies by the reversed reciprocal interval and requires that zero be excluded. These rules enclose every real value represented by their inputs.

For a nonnegative rational x=p/q and integer D=10^70, set k=floor(sqrt(floor(p D^2/q))). Then k/D<=sqrt(x)<=(k+1)/D. The first inequality follows from k^2 q<=p D^2; the second follows because p D^2/q<(k+1)^2. Applying this construction separately at both endpoints gives a rational enclosure of the square root of any nonnegative interval.

We enclose pi independently by Machin's identity

pi=16 atan(1/5)-4 atan(1/239).

Indeed tan(2 atan(1/5))=5/12 and tan(4 atan(1/5))=120/119. Subtracting atan(1/239) by the tangent subtraction formula gives tangent one; the resulting angle is between zero and pi/2, hence it is pi/4. The alternating series for atan(x), at positive x<1, lies between an N-term partial sum and that sum plus its first omitted term. Eighty terms for 1/5 and twenty terms for 1/239 suffice far beyond the required precision. All powers and sums are rational.

Evaluate the displayed definitions by these interval rules. If the lower endpoint of a margin or self-map slack is positive, its required strict inequality is proved. If the upper endpoint of the contraction ratio is below 3331/1000000, the stated contraction bound follows. Finally compare the resulting rational intervals with T4's reported ball strings. Overlap checks test agreement with T4 but do not replace our independent positivity checks.

## Dependencies and evidence

The only analytic dependencies are the scalar formulae in the frozen T4 proof, monotonicity of square root, elementary interval arithmetic, the tangent addition formula, and the alternating-series remainder. The adjacent code and verification JSON record exact endpoints, source hashes, and real execution time. No candidate residual is inserted into this forcing box.
