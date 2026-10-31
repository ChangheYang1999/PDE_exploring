# Lead review of the verifier's Schwartz pressure reference

Written 2026-10-29T00:07:46Z (date -u). Reviewed file: RUN_ROOT/verifier/research/schwartz_pressure/PROOF.md (sha256 0a8b7f64d7c6392838945fa88ccd3d7702c6d291cf005a5e286f07a6d2714dc8).

Verdict: CORRECT.

Checked steps. With E = exp(-r^2): grad E = -2 y E and Delta E = -6 E + 4 r^2 E. For h = x_1 x_2 (harmonic, homogeneous of
degree 2, y . grad h = 2 h): Delta(E h) = h Delta E + 2 grad E . grad h = (4 r^2 - 6) E h - 8 E h = (4 r^2 - 14) E h. Hence
-Delta P = E [6 - 4 r^2 + beta (14 - 4 r^2) x_1 x_2] = f, and grad P = E [beta (x_2, x_1, 0) - 2 y q]. Uniqueness: the
difference of two decaying C^2 solutions is harmonic and tends to 0, so it vanishes by the maximum principle. Angular
support in degrees 0 and 2: x_1 x_2 restricted to the sphere is a degree-2 harmonic. Green formula: for -Delta P = f
with orthonormal harmonics, P_lm(r) = (2l + 1)^-1 int s^2 f_lm(s) r_<^l / r_>^(l+1) ds, which is the displayed form
(s < r: r^(-l-1) s^(l+2); s > r: r^l s^(1-l)).

Remarks (not errors):
1. The test exercises exactly the cancellation of the far-anchor problem: since P is a Schwartz function, the full
   moments int s^(l+2) f_lm ds vanish for l = 0 and l = 2 (the exterior coefficient r^(-l-1) int_0^r ... tends to the
   full moment, and P decays faster than any power), so at large r the interior Green integral is a difference of
   much larger terms, as for the represented Euler fields. This is the property that makes the test relevant.
2. The far-anchor noise in the campaign sits in l = 0 and l = 1. Adding a dipole term covers l = 1 at no cost:
   with q = 1 + beta x_1 x_2 + gamma x_3, Delta(E x_3) = x_3 Delta E + 2 grad E . e_3 = (4 r^2 - 10) E x_3, so f gains
   gamma (10 - 4 r^2) x_3 E and grad P gains gamma E (e_3 - 2 y x_3). The same proof applies (x_3 is a degree-1
   harmonic). Suggested, not required.
3. The scope statement is right: the source is not a tr(DU^2) of a velocity field, so this qualifies the Poisson chain
   and its precision, not the source assembly.
