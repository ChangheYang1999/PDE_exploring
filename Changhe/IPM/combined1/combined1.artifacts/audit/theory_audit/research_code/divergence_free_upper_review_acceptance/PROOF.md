# Acceptance of the Opus review of the divergence-free upper theorem

Written UTC 2026-10-29T16:02:06.164569+00:00 before the independent finite checker. Read with T4-469 PROOF.md and ERRATA_v01, whose hashes remain unchanged. The independent Opus T2 review is the15:59Z source frozen here. The separate T1 reciprocal domain and sign review remains scheduled; this acceptance does not attribute it to T2.

## The statement being accepted

Let F be real and locally integrable on R2, with finitely many positive angular sine modes, and rF in L2. On the gradient completion of C_c^infty(R2), define H(F) by the dual norm. Let psi be smooth, in that gradient completion, with finitely many positive sine modes, grad psi in L2 and r Delta psi in L2. Set

 A_F=-e_theta r sum_n f_n cos(n theta)/n, M2=||A_F||2^2,
 Z_psi=A_(Delta psi)-grad psi, a=||Z_psi||2^2, b=<A_F,Z_psi>.

Then H(F)^2<=M2+2tb+t^2a for every real t. If a>0, H(F)^2<=M2-b^2/a. Several distinct single-mode tests give H(F)^2<=M2-sum b_j^2/a_j. Several tests at a common frequency require the full positive semidefinite Gram form. Every M2 includes the complete F, even when the trial functions do not. The directed scalar bound needs an upper U>=M2, positive upper A>=a, and nonnegative lower B<=|b|, yielding H(F)^2<=U-B^2/A. No candidate upper, inverse or existence theorem follows without those full inputs.

The original proof and positive-pole supplement have been read in full. The review independently derives the domain, contact-free angular divergence identity, positive polar energies, exact trial admissibility, beta moments, positive-pole substitution, residual energy identity and manufactured examples. The argument below rechecks the analytic steps and provides an independent exact implementation for its added examples. The review's floating Cartesian and mpmath comparisons remain observations; this acceptance does not treat them as interval certificates.

## Complete analytic argument and the review remarks

A_F is L2, with norm squared M2, by angular orthogonality. For a compact smooth phi, angular integration by parts at every radius gives -integral A_F dot grad phi=integral F phi. Both sides are absolutely integrable by the hypotheses, so the identity holds on the whole plane, including the origin. There is no radial boundary or contact term. The same formula applies to Delta psi. Thus div Z_psi=0 and div(A_F+tZ_psi)=F. Cauchy-Schwarz and expansion of the square prove the stated quadratic inequality. Minimization over t proves the scalar correction. Distinct angular frequencies are orthogonal in both polar components, proving the sum rule. This is a vector-field right inverse of divergence, not a claim about invertibility of the stationary IPM linearization.

For psi=u(r)sin(n theta), v(y)=u(exp y), direct polar differentiation gives

 Z_psi=-(v'/r)sin(n theta)e_r-(v''/(nr))cos(n theta)e_theta.

Consequently a/pi=int(v'^2+v''^2/n^2)dy and b=(pi/n^2)int r f_n v'' dr. These formulas follow directly from the explicit field, without a radial boundary integration. This confirms the review's optional R1 shorter derivation. The original proof's stronger decay hypotheses remain sufficient. The scalar integral for b converges absolutely since r^2 f_n and v'' are L2(dy). The positive trial formula has a>0 unless the test vanishes, using the stated gradient space and angular Hardy inequality.

R2 is correct as a completeness qualification: grouping only equal exponents and equal denominator factors supplies a sufficient endpoint-integrability test. It need not detect cancellation between exponents differing by integers or denominators put over a common positive denominator. Such missed cancellation rejects a valid integral rather than producing an invalid value. A more permissive exact checker may first put denominators over a common positive denominator, then group exponents modulo integers and remove exact numerator powers. The original T4-469 certificate rule is sound and need not be changed to accept already verified integrals.

R3 is correct for every admissible finite-mode psi, not only one mode. Let Phi be the Riesz representative of F, which exists since H(F)<=sqrt(M2). With g=F+Delta psi, Phi-psi represents g, and expanding the gradient square gives H(F)^2=2p-d+H(g)^2, where p=integral Fpsi and d=||grad psi||2^2. Linearity of A and its orthogonality identity with gradients give ||A_F+Z_psi||2^2=2p-d+||A_g||2^2. Moreover p-d=<g,psi><=H(g)sqrt(d)<=||A_g||2 sqrt(d), proving the triangle comparison. No candidate residual integration is inferred.

R4 is a correct limit extension provided its additional distributional-convergence and L2-vector-series hypotheses are retained. In particular rF in L2 on the entire plane and F locally integrable suffice for the extension in the separately proposed T4-474 proof. The original469 statement remains finite-mode. R5 correctly requires complete-source upper data. A lower dual value below a Hardy upper does not check the latter.

## One necessary-condition wording is false

Section1.5 of the review says that r Delta psi is in L2 "exactly when beta_min>3/2". The original T4 proof used this as a sufficient condition only. For the ungrouped trial parameters that necessity statement is false: take n=3 and

 u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2),
 t=r^2/(1+r^2).

The two ungrouped terms have beta_min=3/2, but their leading terms cancel. The resulting function is smooth at the origin, has u=O(r^-2) with differentiated bounds at infinity, and has grad psi and r Delta psi in L2. It lies in the gradient completion by smooth radial cutoff. Thus a complete grouped profile can be admissible even when the sufficient bound on ungrouped beta_min fails. This example is outside the exact trial subfamily declared in469, which imposes every beta>3/2; all statements about that subfamily and all candidate test inputs are unchanged. The checker verifies the rational identity and positive finite trial energies of this example. The review should replace "exactly when" by "under the sufficient hypothesis" or restrict a necessity claim to a noncancelling leading term.

## Independent exact examples and their verification method

Write any radial trial as u=r sum_b(1-t)^b P_b(t), with rational b and polynomial P_b. Define D_bP=(1-2bt)P+2t(1-t)P'. For one angular frequency the polarized energies are

 d(u,v)/pi=(1/2)sum_(b,c) int_0^1(1-t)^(b+c-2)[D_bP D_cQ+n^2PQ]dt,
 a(u,v)/pi=(1/2)sum_(b,c) int_0^1(1-t)^(b+c-2)[D_bP D_cQ+(D_b^2P)(D_c^2Q)/n^2]dt.

They follow from u_y=r sum w^b D_bP, u_yy=r sum w^b D_b^2P and dy=dt/(2tw). All pairs in the saved tests have b+c-2>-1. Each integral of t^j(1-t)^q is the exact rational j!/product_(i=1)^(j+1)(q+i). No quadrature is used.

For F=-Delta R in the same mode, gradient orthogonality to divergence-free fields gives p=d(R,psi), b=-a(R,psi), H(F)^2=d(R,R) and M2=d(R,R)+a(R,R). The checker uses these bilinear identities to reproduce every rational example in the review, including the two-exponent test, the scalar mismatch, the half-test residual identity and the full2x2 Gram block. Positivity of the exact Gram determinant justifies its inverse. The known Riesz representative gives a genuine exact H value for these fixtures; it is not an assumption about016.

The positive-pole example is rechecked by a separate elementary rational antiderivative. Its source is f_3=r w^(5/2)t(1-2t)/(1+3w)^2 and its test u_3=r^3(1+r^2)^-3. Formula(11) becomes

 b/pi=(1/18)int_0^1 w^(3/2)t^3(1-2t)(9-48t+48t^2)/(1+3w)^2 dt.

Set w=z^2. The resulting integrand is a rational even polynomial divided by(1+3z^2)^2. Exact polynomial division leaves R0+R2 z^2. Decompose that remainder as A times the derivative of z/(1+3z^2), plus B/(1+3z^2), with A=(R0-R2/3)/2 and B=(R0+R2/3)/2. Integration from0 to1, using arctan(sqrt3)=pi/3, gives

 b/pi=-28442/9009+(34256/59049)sqrt3*pi.

The checker verifies the rational-polynomial identities and these exact coefficients, then encloses the resulting scalar with Arb. This confirms the review's closed form while retaining its mpmath comparison as FLOAT. It is a test with pole3 and does not certify the candidate016 pole624 integrals, which have their own accepted source-specific certificates.

All new example coefficients and asserted rational values are in exact JSON. The manifest binds the complete Opus review, code and output and the original469 sources. Copied peer code is read, never executed. The review source reports59checks and the final60.33-second run, with its preceding test failures explicitly retained in that source. This lane records its own real runtime separately. Only the existing Opus5.5 theory lanes are used; configured identity is us.anthropic.claude-opus-5-5 and the actual provider identity is unobservable. No additional model call, server, JavaScript/TypeScript, cluster or numerical worker is launched.
