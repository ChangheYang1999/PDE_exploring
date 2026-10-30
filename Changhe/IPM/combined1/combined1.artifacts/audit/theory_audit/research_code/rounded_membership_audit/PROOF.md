# Independent weighted membership audit of rounded candidate007

## Exact statement

Fix c=4076476460239181/2251799813685248. Replace each exact coefficient of C1-N1-007-d2w-j7-e2bal by its correctly rounded binary64 value interpreted as an exact rational, keeping c and all generators exact. Let F_b be the residual of this second exact function. Define W_a(F_b)=||(1+r^2)^(-a/2)F_b||_2 and N_a(F_b)=||(1+r^2)^((2-a)/2)Delta F_b||_2, for a>=0. Both norms are finite if and only if a>2/c. At equality both squared integrals diverge logarithmically. These claims concern coefficient conversion only, not the exact rational candidate or all errors of a floating evaluator.

## Proof and dependence on the audited sector

T4-117 independently reconstructed the coefficient conversion, origin jets and leading residual sector. Its exact polynomial calculation gives F_b=r^alpha A(theta)+O(r^(alpha-epsilon)), where alpha=2/c-1 is strictly between0and1, epsilon>0 and A is a nonzero finite sum of positive odd sine modes. The preceding sector vanishes exactly. The finite single-scale generators have analytic expansions in r^-2 after their finitely many fractional radial factors are removed. Their products do also. Consequently the remainder and its first two radial and angular derivatives obey the corresponding lower-power estimates uniformly in theta.

The polar Laplacian therefore gives Delta F_b=r^(alpha-2)B(theta)+O(r^(alpha-epsilon-2)), with B=alpha^2 A+A''. For A=sum A_n sin(n theta), orthogonality yields ||B||_2^2=pi sum(n^2-alpha^2)^2 A_n^2 >=(1-alpha^2)^2||A||_2^2>0. The nonzero leading sector survives differentiation; there is no harmonic exception since0<alpha<1andn>=1.

For sufficiently large r, the angular L2 norms of r^-alpha F_b and r^(2-alpha)Delta F_b are bounded above and below by positive constants. Both squared weighted radial integrals are thus comparable to integral_R^infinity r^(2alpha+1-2a)dr. This converges exactly when a>alpha+1=2/c. At equality the power is-1. Compact-region integrals are finite by the smooth positive-denominator generators and their exact origin cancellations. This proves necessity and sufficiency for both norms.

For the low component of the registered dyadic Y norm, replacing1+r^2by1+r^2/Rw^2 with any fixed Rw>0 changes the far-field weight only by a positive limiting factor. Thus F_b is outside Y whenever a<=2/c. No assertion of Y membership in the other direction is made.

## Evidence and scope

The frozen source manifest verifies every hash in N4-131, including the T4-117 proof and output. Its exact threshold is4503599627370496/4076476460239181. The positive leading norm from T4-117 is about7.17546119049e-13; its size does not alter the integrability criterion. N4's numerical lower coefficient is not needed beyond the already independently certified strict positivity. This proof independently confirms N4-131's analytic conclusion without rerunning an existing numerical certificate.
