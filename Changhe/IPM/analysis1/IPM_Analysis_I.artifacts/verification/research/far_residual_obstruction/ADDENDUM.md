# Explicit realization and scope clarifications

2026-10-21. This addendum is part of the statement and proof. The original
proof-first text is retained unchanged. Its fixed exterior radius is denoted
R_b=exp(tplus) below; the radius tending to infinity in the weak tests is
an independent variable S.

The hypothetical profile class requires rho=rho0+h to be an actual locally
regular profile, in particular it includes the task's P2 and stronger
classes. Its canonical velocity is locally L2, has the specified parities,
is divergence free and has curl -partial_x rho in distributions. Its growth
is sublinear uniformly in angle, or, more generally, satisfies

 ||U[rho]||_{L2(B_S)}=o(S^2).

The latter is the precise growth hypothesis needed in the proof. Uniform
pointwise o(r), together with local L2 integrability, implies it. The
stationary equation is understood distributionally as

 div((c X+U[rho])rho)-(2c+1)rho=0.

Local regularity makes the product meaningful. After subtraction, products
involving the L2 difference need only the integrability proved in Section4.
For a fixed translated center x, B_S(x) is contained in B_(S+|x|), so the
same growth bound holds. Compact mollification preserves this estimate and
parities. The harmonic argument in Section3 therefore identifies the actual
velocity difference with the L2 Fourier multiplier, without any assumption
of pointwise decay of that multiplier.

The perturbation h_eta in Section5 preserves the density's local center
condition a(0)=1 because it vanishes near zero. This phrase alone does not
claim preservation of the nonlocal central strain or of 3c-c_star=1 at
fixed c. The limited-scope conclusion can also be proved within that
additional normalization, as follows.

For a radial factor b vanishing near zero, let g=x^2 y b(r). The exact
canonical strain functional is

 c_star[g]=+PV integral y(3x^2-y^2)/(pi r^6) g(X)dX
         =+(1/4) integral_0^infinity r b(r)dr.                     (A1)

Here the local -g_y(0)/4 term vanishes. The canonical formula is
-g_y(0)/4-(K_s*g)(0), with K_s(Y)=y(3x^2-y^2)/(pi r^6).
Since K_s is odd, evaluating the convolution at zero gives the plus sign
in (A1). Indeed the angular integrand is
cos^2(theta)sin^2(theta)(3cos^2(theta)-sin^2(theta))/pi, whose integral
is 1/4: both integrals of cos^4 sin^2 and cos^2 sin^4 are pi/8. Thus a
nonnegative nonzero smooth compactly supported radial b_c away from zero
gives c_star[g_c]!=0. For the tail direction in Section5, b_eta is
eta chi(r)r^(beta-3), and its strain integral converges because beta<1.
Replace it by

 h_eta^N=h_eta-(c_star[h_eta]/c_star[g_c])g_c.                       (A2)

This perturbation has zero strain, vanishes near zero, preserves parity,
retains the identical non-L2 far tail and has weighted factor norm O(|eta|).
Its canonical velocity is sublinear: finite angular Green modes of the
far density power r^beta give O(r^beta) particular velocity and O(r^-3)
homogeneous terms; the compact correction contributes O(r^-3) at infinity.
Consequently rho0+h_eta^N preserves c_star and the exact fixed-c center
normalization as well. The affine L2 class still contains no weighted-factor
neighborhood of rho0 even after these normalizations. This construction is
an admissible trial perturbation, not an assertion of stationarity.

The first Opus 5.5 review accepted the annular argument conditional on its
coefficient check, and requested explicit realization and normalization
wording. These clarifications address those requests. Its reported count
of "three" realization requirements actually lists four; all four are
stated above. The exact coefficient is now checked over the complete
certified normalization intervals by two separate methods. Closure and
source auditing are recorded separately.

The first closure review correctly identified that the initial addendum
confused (K_s*g)(0) with the integral of K_s(Y)g(Y), reversing (A1). The
positive sign above is independently checked from Green: the frequency-two
source of g is f_1=r^2 b+r^3 b'/4, so its inner growing stream coefficient
is (1/4) integral f_1(r)/r dr=(1/8) integral r b(r)dr. Since
r^2 sin(2theta)=2xy, the strain is +(1/4) integral r b(r)dr. The compact
ratio in (A2) and the nonexistence proof are unchanged. The old negative
sign is refuted, not retained as an alternative convention. The original
closure bundle is archived and a new whole-bundle review is required.
