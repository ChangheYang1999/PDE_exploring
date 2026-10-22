# Exact moments of the recorded fitted power functions

2026-10-21, before the exact arithmetic audit. Interpret each recorded binary64 mode1 coefficient A_j and exponent q_j literally as exact dyadic numbers, and fix its recorded positive outer radius R. For q_j<0, the synthetic exterior source f_1(s)=sum A_j(s/R)^q_j, s>=R, has strain contribution

M=(1/2)int_R^infty f_1(s)/s ds=(1/2)sum A_j/(-q_j).

The integral converges termwise because the sum is finite and q_j<0; substitution s/R proves the identity. Consequently M is an exact rational function of these finite recorded dyadics. For two synthetic fits at the same R, their strain difference is the exact difference of these rational moments. The zero-source fit has M=0. These facts do not assert that a fit represents X3 outside R. They also do not replace the analytic exponents of the exact formula by rounded exponents; this statement is explicitly about the separately defined synthetic functions.

Arb and mpmath.iv calculations can independently enclose the exact rational M and fixed-R differences. Any comparison with the saved full-grid c value is a comparison of recorded quantities, not an a posteriori integration error. The ext1e11 moment is at a different R and cannot be compared directly to the baseline without the intervening source integral; that intervening integral is only a floating diagnostic in this topic.
