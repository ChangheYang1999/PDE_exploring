# Lead review of two verifier proofs on the represented far tail

Written 2026-10-28T22:29:40Z (date -u). Files reviewed (verifier side, research/):
- represented_tail_decay/PROOF.md, sha256 7cd74e83c930858e9d6cec3984d248186c60f8dbcfc41fc954ba555f5ca34503 (22:18:48Z);
- homogeneous_tail_quadrature/PROOF.md, sha256 52092208b81ae31a8c0862c3014566addbd3a0ed9835794a42c7bbf6313f58d8 (22:25:30Z).
Both formal/ folders state that no proof assistant was used. This review checks each step by hand; it is not a
machine-checked proof.

## 1. represented_tail_decay: verdict CORRECT, under two named conditions

Channel exponents checked against the production code (numerics experiment copy, src/equations/fields.py lines 160-185,
and the frozen CONVENTIONS.md lines 24-26):
- A (toroidal, T = r^l (s/R0)^-(alpha+l) sum a Phi, twisted): potential ~ r^-alpha, velocity ~ r^-alpha.
- C (poloidal, S = r^l (s/R0)^-(alpha+l-1) sum b Phi, twisted): S ~ r^(1-alpha), velocity ~ r^-alpha.
- B (toroidal, power 2 alpha + 1 + l, twisted, core damping): velocity ~ r^-(2 alpha + 1).
- D (poloidal, power 2 alpha + l, twisted, core damping): S ~ r^-(2 alpha), velocity ~ r^-(2 alpha + 1).
- E (poloidal, power 2 l + 1, untwisted, l >= 2 only, lmask [0, 1]): S ~ r^-(l+1), velocity ~ r^-(l+2).
These agree with the proof. The twist psi = kappa log b of the proof is the production
beta(r) = omega/(2 c_l) log(1 + r^2/R0^2) = (omega/c_l) log(s/R0).
Parameter derivatives add only powers of log r, absorbed by any decay margin beta < alpha, as the proof states.
The representation is a single globally smooth formula (no interior/exterior matching surface), which settles my
earlier review point (c) of notes/pressure_moments_review.md (C^2 regularity across a matching radius): there is no
matching radius.

Conditions under which the consequence (exact-field l = 0, 1 source moments vanish, with their parameter and
coefficient derivatives) applies to the campaign:
(i) the displayed formula is the production field; the evidence is the verifier's field agreement V007, V010, V016,
    V017 on the hashed field sources (it transfers only while fields.py, radial.py, solid_harmonics.py and
    tail_constraints.py keep those hashes);
(ii) the reduced tail map (elimination of the top coefficients) is nonsingular on the parameter set used.
Accepted as a campaign argument for exact fields. Raw discrete moments remain diagnostics; they say how large the
discretization or rounding error of the moment integral is, not whether the exact moment vanishes.

## 2. homogeneous_tail_quadrature: verdict CORRECT

Checked step by step:
- Separated field identities. From curl(Tx) = grad T x x and curl curl(Sx) = 2 grad S + (D^2 S) x - x Lap S with
  T = f(rho) H, S = g(rho) H, Euler homogeneity and Lap H = 0, I recover U = f (grad H x x) + A grad H + B x H with
  A = (l+1) g + 2 rho g', B = -2 l g', and every term of DU, including A' = (l+3) g' + 2 rho g'' and B' = -2 l g''.
- Rotating dilation identity. A direct argument: for fixed lambda > 0 put M = lambda Q with Q = R_(-kappa log lambda).
  The leading potentials satisfy T o M = lambda^-alpha T and S o M = lambda^(1-alpha) S. For a linear similarity
  M = lambda Q, grad(T o M) x x = Q^T (grad T x x) o M and curl curl((S o M) x) = lambda Q^T (curl curl(S x)) o M.
  Hence U(Mx) = lambda^-alpha Q U(x), DU(Mx) = lambda^-(alpha+1) Q DU(x) Q^T, and tr(DU^2)(Mx) = lambda^-(2 alpha + 2)
  tr(DU^2)(x), which is the proof's identity. I suggest writing the step this way: "rotation equivariance of curl"
  with an r-dependent rotation is correct only because M_lambda is a constant similarity for each lambda.
- Coefficient phase. With Y_lm = y_lm(theta) exp(i m phi) and n = R_t n', the coefficient gains exp(i m t),
  t = kappa log r: correct for the production twist cos(m(phi + beta)). The sign check on an independent radius that
  the proof requires is necessary.
- Parameter derivatives. alpha_c = -1/c^2, kappa_c = -w/c^2, kappa_w = 1/c give B_c = A (2/c^2 - i m w/c^2) and
  B_w = A i m/c: correct.
- Exterior integral. The antiderivative s^E (log s/E - 1/E^2) of s^(E-1) log s and the condition Re E < 0 give
  I0 [A + B (log a - 1/E)]: correct. The real parts for b = l + 2 (l = 0, 1), b = 1 - l, b = 1, b = 0 are right.
- Subtraction identity: algebraic, correct; it changes no moment and imposes no constraint.

Remarks for the implementation (not defects of the proof):
(a) In the even-m class the l = 0 and l = 1 parts of the source have m = 0 only, so s^(i m kappa) = 1 in both moments;
    the oscillating factor matters for the exterior Newton integrals of l >= 2, m != 0.
(b) After subtracting the leading tail, the remainder F - L still contains relative corrections of integer order
    (1/s from Phi_k(x) at x = 1 - 2 R0/(s + R0), 1/s^2 from s versus r) and non-integer order (s^-(alpha+1) from B, D;
    s^(alpha-4) from E). With t = a/s, the dipole remainder integrand still behaves like a fractional power of t at
    t = 0 (about t^(2 alpha - 2) for the 1/s correction), so Gauss-Legendre convergence stays algebraic. The order
    ladder must show the observed rate; if it is still slow, subtract the next integer-order term or grade the last
    interval.
(c) Scope: this is an accurate independent reference for the moments. Any use in the production pressure (an
    exterior-only l = 0, 1 formula) stays under the conditions of team notes 22:19Z: the production discrete
    moments must decrease under quadrature refinement, both formulas must agree to the G4(c) tolerance, and the
    change of O1 must be reported; otherwise it is a harmonic correction, which the task forbids.

## 3. What the raw moments of 22:24Z mean, and one question that matters for deliverable D

The verifier's raw moments on the saved nest6 (0.45, 1) input (l = 1: 1.7e-4 at radial order 12, 1.1e-4 at order 20;
c_l-derivative 2.8e-2 and 1.9e-2) are quadrature observations of the independent integrator. Their slow decrease is
explained by the endpoint power t^(2 alpha - 3) = t^(-5/9) at alpha = 11/9 of the unsubtracted l = 1 integrand. They
must not be read as a nonzero exact moment (section 1) or as a production error until the tail subtraction is in.
Question: the production solver integrates the exterior in log s with the factor (s/R0)^-p0 removed and the interior
on [0, r_0] in r. Does its own l = 0, 1 moment, evaluated at the outermost node and in the limit, carry a quadrature
error of comparable size? A discretization error of the moments enters P at the far anchors amplified by about
(r/R0)^(2 alpha - 1) (l = 0) and (r/R0)^(2 alpha - 2) (l = 1) relative to the true r^-(2 alpha) decay. That is a
systematic error of the residual at the anchors (deliverable D), distinct from the rounding noise that limits the
G1 far-anchor block. Numerics and verifier: report the production moments and their refinement with the same
diagnostic as far_noise_split.py.
