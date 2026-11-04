# Exact identities

Part B (Theory Agent B) gives the profile equation, pressure equation, vorticity equation, rotating Bernoulli identity and circulation formula; Part A (Theory Agent A) gives the energy and pressure identities and the translation between the Bernoulli normalizations; Part C (Theory Agent C) gives the exact Fourier system in cylindrical components.

## Part B

## EXACT_IDENTITIES.md (Theory Agent B: Lagrangian part. Bernoulli, angular momentum, circulation, vorticity, stagnation points)
Status line (final at hour 42, 2026-11-04T12:05Z: content frozen; sections 1-12 re-read from scratch in the run with every identity re-derived by hand, one wording precision in (S3); regression in the team records eleven PASS at 10:37Z; originally 2026-11-03T16:45Z, hour-30 deliverable per coordinator Note 90 item 3; re-checked 2026-11-03T22:22Z at the start of the run; (I18) added 2026-11-03T23:50Z; sections 1-12 final at 2026-11-03T23:51Z): sections 1-11 CHECKED (A001-A005, A082, A119 and the verdicts cited in place); section 12 (I10)-(I16) quoted from CONFIRMED sources with verdict numbers; (I17) CONFIRMED (B59-B61 = A1729-A1737, A1792-A1794 for B62; A1738 corrected one general formula; A1797 wording applied); (I18) derived and symbolically checked, with its applications CONFIRMED (B66 = A2457-A2460, B67 = A2515-A2519); B65-B67 add no other exact identity (their tensor evaluations are in the team records Remarks (lviii), (lxi), (lxv)). This file is the one the report cites for the exact identities (section 0.2 of this report). Convention note: sections 1-11 use the prompt's Bernoulli function H = P + |X|^2/2 + c(c-1)|y|^2/2 - omega (Jy).X = P + (Ay).U + |U|^2/2 - c(1-2c)|y|^2/2, while section 12 and the files in the team records, in the team records, in the team records and the report use H = P + |U|^2/2 + (Ay).U; the two differ by the constant-coefficient term c(1-2c)|y|^2/2, so grad H differs by c(1-2c) y and the identities translate by that term (the report's section 0.2 and Theory Agent A's EXACT_IDENTITIES.md (part A) section 0 record the translation, A2104).

Status: every identity below marked [CHECKED] was verified symbolically on generic polynomial fields with the script
in the team records (sympy; c and omega symbolic; two independent random seeds; all checks PASS, log in
in the team records). Identities marked [any U] hold for every C^1 field U and C^1 function P, with no divergence condition and
no equation; the others need div U = 0. "R" denotes the momentum residual, so each identity is an identity of
differential operators; the profile equation is R = 0. The integral and pressure parts (balls, boundary terms,
harmonic ambiguity) are written by Theory Agent A; the Fourier part by Theory Agent C.

### 0. Notation and conventions

c = c_l in (0, 1/2) unless said otherwise; omega in R; J = e_3 x (.), i.e. J v = e_3 x v, J^T = -J, J^2 = -diag(1,1,0).
y_perp = (y_1, y_2, 0), |Jy| = |y_perp|. For a vector field F, DF is the Jacobian (DF)_{ij} = d_j F_i, and (A.grad)F =
(DF) A. S = (DU + DU^T)/2 is the strain, Omega = curl U the vorticity.

    X := c y + U                      (absolute similarity transport field, curl X = Omega)
    B := (c I - omega J) y + U = X - omega J y   (rotating-frame transport field)
    R := (1-c) U + (B.grad) U + omega J U + grad P     (momentum residual; profile equation: R = 0)
    ell := (Jy).U = y_1 U_2 - y_2 U_1 = r U_theta    (angular momentum density about e_3)

Elementary facts [CHECKED]:
    div B = 3c,     curl B = Omega - 2 omega e_3,     (Jy).y = 0,     (Jy).X = (Jy).U = ell,     curl(Jy) = 2 e_3.
The flow of B is written phi_s (s the similarity time); trajectories solve dY/ds = B(Y). "Backward" means s -> -infinity.

### 1. The rotating Bernoulli identity [any U] [CHECKED]

(I1)   R = (1 - 2c) X + Omega x B + grad H,

with the three equivalent expressions

    H = P + |X|^2/2 + c(c-1)|y|^2/2 - omega (Jy).X                     (prompt's form)
      = P + B.U - |U|^2/2 - c(1-2c)|y|^2/2                              (circulation form, see section 3)
      = P + |B|^2/2 - omega^2 |y_perp|^2/2 + c(c-1)|y|^2/2.            (rotating-frame form: kinetic energy of the
                                                                        relative velocity plus centrifugal potential)

Proof. For any C^1 fields a, b: (a.grad)b = grad(a.b) - (b.grad)a - a x curl b - b x curl a. With a = Jy, b = X and
curl(Jy) = 2 e_3, (X.grad)(Jy) = JX, X x e_3 = -JX one gets ((Jy).grad)X = grad((Jy).X) + JX - (Jy) x Omega. With
(X.grad)X = grad(|X|^2/2) - X x Omega and (B.grad)U = (B.grad)X - cB:
(B.grad)U = grad(|X|^2/2 - omega (Jy).X) + Omega x B - omega J X - c B. Insert in R, use -omega JX + omega JU =
-c omega Jy and -cB - c omega Jy = -cX, (1-c)U = (1-c)X - c(1-c) y = (1-c)X + grad(c(c-1)|y|^2/2). Collecting gives (I1).
The prompt's boxed identity and its H are therefore correct, with every sign and coefficient as stated. No divergence
condition is used.

Transport of H along the flow of B [any U] [CHECKED]:

(I2)   B.grad H = -(1 - 2c) X.B + B.R,
       X.B = |X|^2 - omega ell = |B|^2 + omega ell - omega^2 |y_perp|^2.

For a solution (R = 0) and 0 < c < 1/2, dH/ds = -(1-2c)(|X|^2 - omega ell) along trajectories. The term omega ell is
the rotating term of the prompt. The sign of dH/ds is indefinite exactly on

    Q := { y : omega ell(y) > |c y + U(y)|^2 }        (the "bad set").

On Q the swirl has the sign of omega and |cy + U|^2 < |omega| |U| |y_perp|; since U is bounded, Q is contained in the ball
|y| <= max(4 |omega| sup|U| / c^2, 2 sup|U| / c) (for |y| >= 2 sup|U|/c one has |cy+U| >= c|y|/2, and then |y| >
4|omega| sup|U|/c^2 contradicts c^2|y|^2/4 < |omega| sup|U| |y|; A082 asked for the maximum). So the Lyapunov
property of H fails only on a bounded set, but it does fail there in general: no exact profile is needed to see this,
the right side of (I2) with R = 0 is a pointwise algebraic expression in (y, U). For omega = 0, Q is empty and H is
strictly decreasing along nonstationary trajectories (CIV (3.31)-(3.33); Euler1 Theorem L2, step 2).

Absolute-frame Bernoulli function [any U] [CHECKED]. With Ht := H + omega ell = P + |X|^2/2 + c(c-1)|y|^2/2 (the
non-rotating Bernoulli function evaluated on the rotating profile),

(I3b)  B.grad Ht = -(1 - 2c) |X|^2 - omega (Jy).grad P + (B + omega Jy).R.

So along trajectories, for a solution, dHt/ds = -(1-2c)|X|^2 - omega d_theta P. The dissipative term now has a sign;
the obstruction has moved into the azimuthal pressure derivative d_theta P = (Jy).grad P (it is the "unsteady pressure
work" of the time-periodic solution seen in the non-rotating similarity frame, where d_s P = -omega d_theta P).
Combination: for every real a, B.grad(H + a ell) = -(1-2c)|X|^2 + (1-2c)(omega - a) ell - a d_theta P (+ residual
terms): no choice of a removes both bad terms. This is the content of approach3 item 8 in a sharper form.

### 2. Angular momentum about the rotation axis [any U] [CHECKED]

(I3)   B.grad ell = -(1 - 2c) ell - (Jy).grad P + (Jy).R.

The rotation rate omega does not appear: (JB).U = c ell + omega y_perp.U and (Jy).(omega J U) = omega y_perp.U cancel.
For a solution, r U_theta is damped at rate 1 - 2c along trajectories up to the pressure torque -d_theta P. For
axisymmetric fields d_theta P = 0 and (I3) is the swirl equation of CIV (4.1), third line, used in their Theorem 4.5.

Consequences for invariant measures (section 4 of in the team records): for every compactly supported invariant probability
measure mu of the flow of B and every solution,
    integral (|X|^2 - omega ell) dmu = 0,    (1-2c) integral ell dmu = - integral d_theta P dmu,
    hence integral |X|^2 dmu = -(omega/(1-2c)) integral d_theta P dmu.
These follow from (I2), (I3) and the fact that integral B.grad f dmu = 0 for every C^1 function f (f bounded on the
support).

### 3. Circulation: the Lie derivative of the velocity 1-form [any U] [CHECKED]

(I4)   (B.grad) U + (DB)^T U = -(1 - 2c) U + grad(|U|^2/2 - P) + R,

i.e. for the 1-form U^flat = U_i dy^i,   L_B U^flat = -(1-2c) U^flat + d(|U|^2/2 - P) + R^flat.

Proof. L_B U^flat has components B_j d_j U_i + U_j d_i B_j = ((B.grad)U)_i + ((DB)^T U)_i, and (DB)^T = cI + omega J
+ (DU)^T, so (DB)^T U = cU + omega JU + grad(|U|^2/2); then (B.grad)U + omega JU = R - (1-c)U - grad P.

Kelvin circulation law. Let C(0) be a closed C^1 curve and C(s) = phi_s(C(0)). For a solution,
    d/ds  oint_{C(s)} U.dl  =  oint_{C(s)} (L_B U^flat)  =  -(1 - 2c) oint_{C(s)} U.dl,
because the exact form d(|U|^2/2 - P) integrates to zero on a closed curve. Hence
    oint_{C(s)} U.dl = e^{(2c-1)s} oint_{C(0)} U.dl,
which is the prompt's boxed circulation identity and CIV (3.27) (their e^{(1-2gamma)tau} Gamma_ss(tau) = Gamma_ss(0)).
X and U have the same circulation (they differ by the exact form d(c|y|^2/2)); B and U differ by -omega (Jy).dl, whose
circulation is -2 omega times the signed area of the projection of the loop on the (y_1, y_2)-plane, so the law is
stated for U (equivalently X), not for B.

Vorticity flux law. Applying d to (I4) (d commutes with L_B, dR^flat = (curl R)^flat-type 2-form):
    L_B sigma = -(1-2c) sigma + (curl R)-term,   sigma := i_Omega vol = dU^flat   (sigma(v,w) = Omega.(v x w)),
so for a solution phi_s^* sigma = e^{(2c-1)s} sigma: the vorticity flux through a surface transported by the flow
is multiplied by e^{(2c-1)s} (Stokes form of the Kelvin law). Equivalently (section 5) [B, Omega] = -(1+c) Omega,
because L_B(i_Omega vol) = i_{[B,Omega]} vol + (div B) i_Omega vol and div B = 3c.

Consequences (proofs in the team records):
(a) The circulation of U around every closed curve invariant under phi_T for some T > 0 (periodic orbits, invariant
    loops) is zero when c != 1/2.
(b) On every compact phi-invariant C^1 surface Sigma (an invariant torus, say), the vorticity Omega is tangent to Sigma
    at some point: integral_Sigma sigma = e^{(2c-1)T} integral_Sigma sigma forces integral_Sigma Omega.n dA = 0.
    (For a closed surface this also follows from div Omega = 0; the statement with content is for a surface with
    boundary that is invariant as a set up to a time shift along its boundary orbits.)
(c) The exponent c = 1/2 is the only one for which circulation is conserved (CIV Remark 3.6).

### 4. Vorticity: equation, commutator, Cauchy formula [div U = 0] [CHECKED]

(I5)   curl R = Omega + (B.grad) Omega - (Omega.grad) U + omega J Omega,
(I5b)  [B, Omega] + (1 + c) Omega = curl R,   where [B, Omega] := (B.grad) Omega - (Omega.grad) B.

The prompt's boxed vorticity equation is (I5) with R = 0. Without div U = 0 both acquire (div U)-terms (checked). For a
solution, (I5) reads along trajectories

    dOmega/ds = (DU - I - omega J) Omega = (DB - (1+c) I) Omega.

Cauchy formula (exact vorticity transport). For a C^2 solution and all a, s:

    D phi_s(a) Omega(a) = e^{(1+c)s} Omega(phi_s(a)).

Proof: both sides solve the linear ODE dM/ds = DB(phi_s a) M with the same initial value Omega(a); for the right side
use (I5) and DB = cI - omega J + DU. (CIV (3.22) is the same formula with omega = 0; the rotation enters only through
DB.) Consequences, all for every omega:
(a) The sets {Omega = 0}, {Omega != 0} and {Omega x B = 0} are invariant under phi_s (D phi_s is invertible and
    D phi_s B(a) = B(phi_s a)).
(b) Vortex lines are mapped to vortex lines: if gamma'(tau) = Omega(gamma(tau)) then phi_s(gamma(tau)) =
    gamma_s(e^{(1+c)s} tau) for the vortex line gamma_s through phi_s(gamma(0)) (forward flow stretches Omega-time by
    e^{(1+c)s}; the backward flow psi_t = phi_{-t} shrinks it by e^{-(1+c)t}). The backward flow shortens every
    vortex segment: a segment of Omega-time length T has, after backward time t, Omega-time length e^{-(1+c)t} T and
    Euclidean length at most sup|Omega| e^{-(1+c)t} T. The vortex line through a vortical point a is therefore
    contained in the backward-stable set of a (all its points have the same backward limit set as a).
(c) At a vortical point a, |D phi_{-t}(a) Omega(a)| = e^{-(1+c)t} |Omega(phi_{-t} a)| <= M e^{-(1+c)t}, M =
    sup of |Omega| over the trapping ball: the backward flow contracts the direction Omega(a) at rate at least 1 + c,
    uniformly on compact subsets of {Omega != 0}. With det D phi_{-t} = e^{-3ct}, the induced map on the quotient
    R^3 / R Omega(a) expands area at least like (|Omega(a)|/M) e^{(1-2c)t}.

Vorticity magnitude [div U = 0] [CHECKED]:

(I7)   B.grad |Omega|^2 = 2 (Omega.S Omega - |Omega|^2) + 2 Omega.curl R.

The term omega J Omega drops out (Omega.J Omega = 0): the rotation does not modify vorticity stretching along
trajectories. Hence for a solution, backward in time, d|Omega|^2/d(-s) >= 2(1 - lambda_max(S))|Omega|^2, and a
vortical point cannot converge backward to a compact invariant set on which lambda_max(S) < 1 (Euler1 step 3 is
omega-independent).

Helicity density [div U = 0] [CHECKED]:

(I8)   B.grad (U.Omega) = -(2-c) U.Omega - Omega.grad P + U.(Omega.grad)U + Omega.R + U.curl R.

The J-terms cancel (Omega.JU + U.JOmega = 0). This is not sign-definite; recorded for completeness.

### 5. Pressure Poisson equation [div U = 0] [CHECKED]

(I6)   div R = Delta P + tr((DU)^2) = Delta P + d_i U_j d_j U_i.

No omega-term survives: div((B.grad)U) contributes + omega Omega_3 and div(omega J U) contributes - omega Omega_3. The
prompt's -Delta P = d_i U_j d_j U_i is therefore correct for every omega. (The harmonic ambiguity and the far-field
behaviour of P are treated by Theory Agent A.)

### 6. Stagnation points of B [solution, C^2]

Let p be a zero of B. Then DB(p) = c I - omega J + DU(p), tr DB(p) = 3c.

(S1) Existence. If U = o(|y|) uniformly, B.y = c|y|^2 + U.y >= c|y|^2/2 for |y| >= R_0, so B points outward on the
     sphere of radius R_0 and has the degree of the identity there; B has at least one zero in the ball (Brouwer).
     The zero need not be the origin when omega != 0 or U(0) != 0.
(S2) Vortical zero (Omega(p) != 0). From (I5b) at p (B(p) = 0): DB(p) Omega(p) = (1+c) Omega(p). So 1 + c is an
     eigenvalue of DB(p) with eigenvector Omega(p), and the other two eigenvalues sum to 3c - (1+c) = 2c - 1 < 0: at
     least one has negative real part; 0 has algebraic multiplicity at most 1, so rank DB(p) >= 2. Dotting with
     Omega(p): Omega.S Omega = |Omega|^2 at p, so lambda_max(S(p)) >= 1 (CIV Theorem 3.8 mechanism; approach3 item 12).
     These statements hold for every omega. Moreover the vortex line through p is an invariant curve: by the Cauchy
     formula, phi_s(gamma_p(tau)) = gamma_p(e^{(1+c)s} tau), so its two branches are forward orbits leaving p tangent to
     Omega(p) (the unstable eigencurve for the eigenvalue 1 + c), and for the backward flow it is the stable curve of p.
(S3) Irrotational zero (Omega(p) = 0). DB(p) = c I + S(p) - omega J with S(p) symmetric traceless. By Bendixson's
     theorem every eigenvalue lambda satisfies c + lambda_min(S) <= Re lambda <= c + lambda_max(S). For omega = 0 and
     lambda_max(S) >= 1 the smallest eigenvalue is <= c - 1/2 < 0 (Euler1 step 4). FOR omega != 0 THIS FAILS:
     example S = diag(1, -1, 0), omega^2 > 1 - c^2: spectrum {c, c +- sqrt(1 - omega^2)} (a complex pair c +- i sqrt(omega^2 - 1) when omega^2 > 1, two real positive numbers when 1 - c^2 < omega^2 <= 1), all real parts positive, so p
     is a sink of the backward flow; and S = diag(lambda, -lambda, 0) with lambda > 1 and omega > lambda gives
     lambda_max(S) > 1 with the same conclusion (in the team records; about 19 percent of random traceless S
     with lambda_max(S) >= 1 and omega in [0, 10] give a backward sink). Such a local configuration is compatible
     with the equation to first order (the pressure Hessian -(S + S^2 + omega [J, S]) is symmetric). This is the
     second place where Euler1's proof breaks under rotation (the first is the Lyapunov property of H).
     in the team records repairs it: a vortical trajectory can only converge backward to a zero p at which DB(p) has an
     eigenvalue with real part >= 1 + c, hence another with real part <= (2c-1)/2 < 0, by the Cauchy formula.
(S4) Local outgoing (CIV Definition 3.7) at a zero p: B(y).(y-p) >= c_*|y-p|^2 near p forces y.(cI + S(p))y >= c_*|y|^2
     (the J-term drops out of the quadratic form), so lambda_min(S(p)) >= c_* - c and lambda_max(S(p)) <= 2(c - c_*);
     with (S2) a vortical zero with local outgoing forces c >= 1/2 + c_*, for every omega (approach3 item 14a).

### 7. Periodic orbits [solution, C^2]

Let gamma be a periodic orbit of B of period T. The monodromy D phi_T(y), y in gamma, has eigenvalue 1 on B(y).
(P1) If Omega != 0 on gamma, the Cauchy formula gives D phi_T(y) Omega(y) = e^{(1+c)T} Omega(y), so the multipliers
     are {1, e^{(1+c)T}, e^{(2c-1)T}} (product e^{3cT}): gamma is a hyperbolic saddle with a 2-dimensional unstable and
     a 2-dimensional stable manifold. For the backward flow the roles are exchanged: the direction Omega is the
     stable one (the unique contracting direction). (approach3 item 8; re-derived.) The circulation of U around gamma is zero (section 3(a)).
(P2) Omega x B cannot vanish identically on gamma unless Omega = 0 on gamma: if Omega = f B on gamma with f != 0,
     the Cauchy formula gives f(phi_s y) = e^{-(1+c)s} f(y), impossible on a periodic orbit.
(P3) If Omega = 0 on gamma, nothing follows from the Cauchy formula at gamma itself; the restriction on gamma as a
     backward limit of vortical points is in the team records (a Floquet exponent >= 1 + c is forced).

### 8. Affine exact solutions (reference examples, not decaying) [CHECKED]

U = A y, P quadratic, solves the profile equation iff M := A + A^2 + omega (JA - AJ) is symmetric (then P = -y.My/2)
and tr A = 0. The family A = diag(s_1, -1-s_1, 1) + v J (any s_1, v, omega) satisfies this (M is diagonal plus the
symmetric matrix omega(2 s_1 + 1)(e_1 e_2^T + e_2 e_1^T)); B = diag(c+s_1, c-1-s_1, c+1) + (v - omega) J. These are
the "rotating strain" examples of Euler1's hostile review; they violate U -> 0 and are used only to test
candidate Lyapunov functions (approach3 item 8).

### 9. Hypotheses actually used (coordinator's labels)

(I1)-(I4), (I2), (I3), (I3b): H0 weakened to U, P in C^1; no divergence; pointwise identities.
(I5)-(I8), Cauchy formula, sections 6-7: H0 (U in C^2 so that DB is C^1 and the variational equation holds; U in
C^{1,1} would do for the Cauchy formula), div U = 0, R = 0 pointwise.
Section 6 (S1) and the trapping used in section 4(c): H1' (U = o(|y|) uniformly); H1 implies H1'.
No symmetry, no integrability, no decay rate, no smallness, no restriction on omega.

### 10. Verification record

in the team records: 28 symbolic checks on generic cubic polynomial fields (U = curl A to have div U = 0, and a
second non-divergence-free U for the [any U] identities), seeds 7 and 11, all PASS (run 2026-11-02T18:32Z and later;
see in the team records). in the team records: the backward-sink example of (S3). The coordinator's independent check
(verify_identities.py (accompanying artifacts)) agrees on (I1), (I2), (I4), (I5), (I5b), (I7) and the angular-momentum law.

### 11. Second-order identity along the vorticity direction [solution, C^2, Omega != 0] [CHECKED]

With n = Omega/|Omega|, a = n.Sn, b = Sn - a n, p_nn = n.D^2P n, and the Lagrangian Riccati equation
dG/ds = -G - G^2 - omega[J,G] - D^2P for G = DU along trajectories (its trace is (I6), its antisymmetric part is (I5)):

(I9)   B.grad a = |b|^2 - a^2 - a - p_nn    (+ 2 (curl R).b/|Omega| + n.(DR) n when R != 0).

The rotation terms cancel; the step (DU - DU^T) n = 0 uses Omega = curl U. Checked with exact rational arithmetic at random
points of random polynomial fields (in the team records). Consequence on invariant measures: in the team records Lemma 6.5.

### 12. Exact identities found in shifts 3-4 (added 12:19Z; each with its verdict; proofs in the files named) [global helicity-free class unless stated]

Notation: a = 1-2c, kappa = 1+c, g = U.B, H = P + |U|^2/2 + (Ay).U, n = U/|U| or n = Omega/|Omega| as stated, S = sym DU, l = grad g.grad H/|grad H|^2.
(I10) Covector law along the vortex line of a vortical carrier equilibrium p (B31 = A673; in the team records Prop. 1): with B = kappa tau Omega on L,
      (B.grad)U = rho U - DB^T U on L, rho the number with DB(p)^T U(p) = rho U(p); hence d/dt log|U| = rho - c - n.Sn (n = U/|U|) and
      n.grad P = |U|(n.Sn - (a + rho)) on L; P = H(p) + |U|^2/2 on the level sheet, where U is normal and B tangent: B = (Ay)^tangential,
      U = -(Ay)^normal (B44 = A771-A774), so |U|^2 + |B|^2 = |Ay|^2 there.
(I11) Rank-ratio transport on zero-g orbits of the vortical closure (Lemma W2.7, A820): on {dH != 0}, l is C^1 and dl wedge dH = 0 on closure{Omega != 0};
      along a B-orbit of the closure through a point with g = 0 and dH != 0: g = 0, H and l constant, dH != 0 for all time, and
      grad H(Phi_t x) = e^{-a l t} DPhi_t(x)^{-T} grad H(x). On an irrotational such orbit grad H = -aU, so U obeys the covector law at the constant rate
      -a l. Along any covector-law orbit: grad P = DU^T U - (a + rho) U (no helicity hypothesis needed for this last line).
(I12) On a flat periodic carrier orbit Gamma (Omega = D Omega = 0, g = 0, covector rate rho; B43 = A766-A767): grad H = -aU, grad g = rho U, d(BH) = rho dH,
      d(Bg) = rho dg on Gamma; SB = (rho - c)U - omega JU - SU (equivalently S(Ay + 2U) = (rho - c)U - omega JU; the form S(Ay) is WRONG, A768);
      grad P = SU - (a + rho)U; (1/T) int_0^T n.Sn dt = rho - c (n = U/|U|); dS/dt + S^2 + S + omega(JS - SJ) = -D^2P on Gamma with trace Delta P = -|S|^2;
      |U|^2 + |B|^2 = |Ay|^2 and int_0^T |B|^2 dt = -omega oint (Jy).dy on Gamma.
(I13) Level stream function and tangential velocity (B43 = A766, in the team records section 4): on a regular level {H = h}, beta_h = i_Omega i_N vol (N = grad H/|grad H|^2)
      is a closed 1-form (div Omega = 0, Omega.grad H = 0); where it is exact, d psi_h = beta_h and the vortex lines are the level curves of psi_h;
      U^T = -g grad_S psi_h and |U^T| = |g||Omega|/|grad H| pointwise on every regular level (the tangential velocity is a surface gradient orthogonal to
      the vortex lines); on a connected source piece with g = G(H), psi_{h_t(h)} o Phi_t = (e^{-at}/h_t'(h)) psi_h + C_t(h) (local law; the global
      normalization clauses are OPEN, A769). On an invariant level (g = 0 on it): B psi = (-a - rho) psi (B34 = A543).
(I14) Transport of the vorticity derivative along an irrotational zero-g orbit with Omega = 0 on its level germ (B51 = A888): D Omega = w tensor dH with
      w = D Omega N tangent, w(Phi_t x) = e^{-(kappa + rho)t} DPhi_t(x) w(x), nu(B, w)(Phi_t x) = e^{(-a - 2 rho)t} nu(B, w)(x) (nu the level area form);
      at a nonflat endpoint q of an upper-window connection nu(B, w) = 0 and D Omega(z(t)) = C e^{-(rho + kappa)t} B tensor dH. More generally (A889, B52):
      at a point where all derivatives of Omega of order < k vanish along the orbit, D^k Omega(Phi_t x)(DPhi_t v_1, ..., DPhi_t v_k) = e^{-kappa t} DPhi_t D^k Omega(x)(v_1, ..., v_k).
(I15) Helicity in the moving vortex frame (B46 = A790-A792, A872; unrestricted class, any omega): with n = Omega/|Omega|, a_n = n.Sn, b = Sn - a_n n,
      eta = U.n = (U.Omega)/|Omega|: (B.grad) eta = -(1-c) eta + U.b - n.grad P; hence int n.grad P dmu = int U.b dmu - (1-c) int eta dmu on compact invariant
      probabilities on the vortical set, and n.grad P = U.Sn pointwise in the helicity-free class; (B.grad) b = -(1 + 2 a_n) b - |b|^2 n - omega Jb - D^2P n + p_nn n
      (A793, the corrected second derivative; the Hessian part of (B.grad)^2 eta is -n.D^2P(B + U) + eta p_nn). Also (I8) in the form (B.grad) h + kappa h = Omega.grad g.
(I16) Floquet and spectral facts used (Section D and A468-A471): a vortical carrier equilibrium has spec DB = {kappa (eigenvector Omega), rho, -a - rho}
      with rho <= -a (A496); a vortical periodic B-orbit has multipliers 1, e^{kappa T}, e^{-aT} (Omega is a Floquet eigenvector); a flat periodic orbit with
      covector rate rho has multipliers 1, e^{rho T}, e^{(3c - rho)T}; the level flow on a zero-g regular level expands dA/|grad H| at the rate 3c - rho (A574;
      the projected field Y = B - (BH) grad H/|grad H|^2 has div_{nu_0} Y = 3c - rho wherever d(BH) = rho dH, A826).
(I17) Tail identities at the scattering direction and the irrotational-boundary identity (B59-B61, in the team records 3f-ter; CONFIRMED A1729-A1737 and, for B62, A1792-A1794; referee the external referee (a second model); folded 2026-11-03T16:53Z). Tail notation: V twisted homogeneous ((X.grad)V = -LV, X = Ax, L = (1-c)I + omega J), div V = 0, W = curl V, k = X.V,
      S = P2 - |V|^2/2, -Laplacian P2 = tr((DV)^2), b = 2-2c, q = b/a. Exact (checked symbolically, in the team records):
      grad k = -aV + X x W;  X.grad k = -ak;  Laplacian k = -2 omega W_3 - X.curl W;  Laplacian S = -tr((DV)^2) - |DV|^2 + V.curl W;
      q(q-1)a^2 = b and (q-1)a = 1;  the rank identity grad k wedge grad S = 0 on {W != 0} contracted with X gives bS grad k = ak grad S, so on each
      component of {W != 0} cap {k != 0}: S = D_C |k|^q.  At a point z with V(z) != 0, W(z) = DW(z) = 0 in the closure of {W != 0} (V, P2 in C^2):
      grad k(z) = -aV(z), D^2k(z) = -a DV(z), Laplacian k(z) = 0, Laplacian S(z) = -2|DV(z)|_F^2, and (limit of the component identities, uniform over
      components, G = |DV(z)|_F^2, v = V(z))
          grad S(z) = (2G k(z)/|v|^2) v,   S(z) = -2G k(z)^2/(b|v|^2),   D^2S(z) = -2G (v tensor v)/|v|^2 + (2G k(z)/|v|^2) DV(z),
      hence |k(z)| = |grad S(z)||V(z)|/(2|DV(z)|_F^2) and |DV(z)|_F^2 >= |grad S(z)|/(2|X(z)|); for one component through z: D_C =
      -2^{q-1}|DV(z)|^{2(q-1)}/(b|V(z)|^q|grad S(z)|^{q-2}) and |D_C||V(z)|^{q-2} >= 3(1-c)/(2|X(z)|^q) (LIT245 (3.2)). Differentiated rank identity at a
      supported point w (F = grad k x grad S vanishes on the open vortical set): DF(w) = 0 if k, S in C^2, D^2F(w) = 0 if C^3 (A1737: with grad k(w) = 0 and
      rank D^2k(w) >= 2 this gives grad S(w) = 0 at C^2 and D^2S(w) = lambda D^2k(w) on the whole space at C^3). General second derivative of k:
      D^2k[h] = -a DV h + (Ah) x W + X x DW h (A1738 corrected a version without the middle term; it vanishes where W = 0). At the scattering direction
      of an escaping W2 trace in the supported nonflat branch (V = W = 0 and DW(w) = 0 at w, so grad k(w) = 0 and D^2k(w) = -a DV(w); Laplacian S(w) = -2|DV(w)|^2;
      D^2S(w) Aw = -(bI + A^T) grad S(w), which is 0 once grad S(w) = 0) these read: (DV(w)h) x grad S(w) = 0 for all h (C^2), which excludes grad S(w) != 0 when
      DV(w) has rank 2; and then, with grad S(w) = 0, (DV(w)h) x (D^2S(w)h) = 0 for all h (C^3), which excludes DV(w) != 0 (A1797 wording).
Verification: the algebra of (I12) was refereed (the external referee (a second model)) and audited (A766-A768) after one error; (I14)-(I15) were audited (A888-A890, A790-A793); the
remaining items are quoted from their confirmed sources. Symbolic check (12:51Z, in the team records): (I15) and (I9) hold on the exact affine
family of section 8 (sign-changing helicity, symbolic parameters) and on the exact pure swirl U = K r^{-(1-c)/c} e_theta (helicity-free; its exactness
confirmed numerically in the team records).

(I18) Exact derivative of the contact defect at an irrotational contact (the run, 2026-11-03T23:50Z; derived in the team records Remark (lxvii) from the consultation the external referee (a second model)
w2flatcontact, re-derived by hand and checked symbolically in the team records: PASS; the identity itself is not separately audited, but its two
applications are: B66 = A2457-A2460, B67 = A2515-A2519). Setting: a point z of the tail with V(z) != 0, W(z) = DW(z) = 0 and z in closure{W != 0}, where Lemma W2.14 (I17) gives
grad k = -aV, grad S = (2Gk/R) V and D^2S = -2G (V tensor V)/R + (2Gk/R) N, with N = DV(z) symmetric trace free, G = |N|_F^2, R = |V|^2. For a unit vector f put
v_f = V.f and Phi_f := d_f S - 2 G k v_f / R (the f-component of the contact identity, so Phi_f(z) = 0). Then, exactly at z,
    d_f Phi_f = -(2G/R) [ (1-a) v_f^2 + k v_f d_f log(G/R) ],      d_f log(G/R) = 2 <N, D^2V[f,.]>_F / G - 2 (V.Nf)/R.
Proof: d_f(d_f S) = f^T D^2S f = -2G v_f^2/R + 2Gk (f^T N f)/R; d_f(2Gkv_f/R) = 2[(d_f G) k v_f + G (-a v_f) v_f + G k (f^T N f)]/R - 2Gk v_f (2 V.Nf)/R^2; subtract and
collect, using d_f G = 2 <N, D^2V[f,.]>. Use: in the nonflat case (B66) the first term dominates with the margin -4 sigma^2 (1-a) and makes Phi_f strictly decreasing
across the vortical approach line, so two extreme contacts on one transverse segment are impossible; in the flat case the second term has no sign from the contact
identities alone (Remark (lxvii)), which is where the two-contact method stops. [derived and symbolically checked; applications CONFIRMED]

## Part A

## EXACT_IDENTITIES.md (part A) (Theory Agent A): integral and pressure part

Status line (2026-11-03 22:20Z, hour-30 deliverable, coordinator Note 90 item 3; final unless a new the auditor verdict
arrives): this file agrees with EXACT_IDENTITIES.md, the file the report cites; the correspondence and the one
change of notation (the Bernoulli function) are in section 0 below. Index rows through C68 (section 5); every row
has an auditor verdict and no Theory Agent A claim is pending. Earlier updates:
22:20Z: index rows C64-C68 (all CONFIRMED). 18:54Z: C63 row CONFIRMED (A2079, A2080). 18:48Z: section 0, 3(c) citation, index rows C55-C63. 15:28Z: C54 row CONFIRMED (A1429). 15:24Z: index row for the Biot-Savart representation (C55, SUBMITTED). 15:08Z: C52 row CONFIRMED (A1355, A1356), C53 row CONFIRMED (A1376-A1378). 15:00Z: index row for the weighted enstrophy gap (C54, SUBMITTED). 14:46Z: index row for the R2 dual bound (C53, SUBMITTED). 14:35Z: index row for DERIVATIVE_GROWTH (C52, SUBMITTED). 14:12Z: C51 CONFIRMED (A1223-A1226). 13:55Z: C50 CONFIRMED (A1171-A1177). 13:50Z: index row for TRANSVERSE (C51, SUBMITTED). 13:19Z: C49 CONFIRMED (A1068-A1074). 13:18Z: index row for SV_PAIR (C50, SUBMITTED). 12:51Z: index row for SMALL_VORTICITY (C49, SUBMITTED). 08:38Z: C36 CONFIRMED (A584-A586), C38 CONFIRMED (A499), C43 CONFIRMED (A579-A581), C44
CONFIRMED as local countertests (A582; necessity reading REFUTED, A583); status columns updated.
05:50Z: C37 CONFIRMED (A485); C39 CONFIRMED (A492, with the literature agent LIT120); C39 row revised.
05:36Z: index row for C39 (POINTWISE_DECAY, Theorem PD); C38 row updated (MD').
05:24Z: C37 row updated (Proposition BP, O(1/abs(y)) rates); index row for C38 (SL, MD).
04:59Z: index row for ORBIT_LAYERS (C37); C34, C35 verdicts A475-A477 recorded.
04:39Z: index row for VORTICITY_GAP (C36). 04:10Z: index row for GRADIENT_GAP (C35).
03:33Z: physical reading of (D1)-(D6) added (section 1); index row for
PHYSICAL_DICTIONARY item 6. 03:15Z: C33 verdicts A435-A436 recorded. 02:15Z: C32 verdicts A408-A412 recorded.
01:55Z: C32 (in the team records) added. 01:27Z: C29-C31 verdicts (A353-A364) recorded; (P7) and section 5 added
(00:19Z); Lemma P and C29, C30 added (00:45Z); C31 (01:18Z).

Companion to EXACT_IDENTITIES.md (Lagrangian part: Bernoulli, circulation, vorticity, stagnation points) and
in the team records (Fourier part). Notation follows Theory Agent B: X = cy + U, B = (cI - omega J)y + U, A = cI - omega J,
Res = momentum residual (1-c)U + B.grad U + omega JU + grad P (called R in Theory Agent B; the profile equation is Res = 0), ell = (Jy).U, q = |U|^2/2,
Omega = curl U, S = sym grad U, h = U.Omega. alpha = 5 - 2/c. E(R), g, eps, A_R as in the team records.

Verification. Every pointwise identity in section 1 and (P1) was checked with sympy, c and omega symbolic:
in the team records (log in the team records, ALL PASS). First-order identities (D1)-(D3h), (D5) are
checked for generic sympy functions U, P with the exact remainder in terms of Res and div U. The second-order
identities (D4), (D6), (P1) are checked on an exactly divergence-free polynomial test field U = curl psi with an
arbitrary polynomial P; the algebraic derivation is given in the text. Transport identities along B (B.grad of
U.B, H, ell, q, y.U) are in in the team records, and the gradient and vorticity equations in
in the team records. These overlap with the coordinator verify_identities.py (accompanying artifacts) and Theory Agent B in the team records
(independent checks of the same identities).

### 0. Agreement with EXACT_IDENTITIES.md (checked 2026-11-03 18:48Z against the 17:47Z version of that file)

Rechecked 2026-11-03 22:54Z against the 22:22Z version of that file. Since 17:47Z Theory Agent B changed only its status line (per its the team records),
and (I1)-(I3), (I6)-(I8), (I15) and section 8 still read as quoted below.

The report (section 0.2) cites EXACT_IDENTITIES.md for the exact identities. Every identity of this file that
also appears there agrees with it:
- Notation. B, A, X, ell, S, Omega and DU (entries d_j U_i) as in Theory Agent B section 0; Res here is R there. In the later
  files of this agent (ENSTROPHY_GAP, NONLINEAR_WEIGHT, NW_OPTIMAL, STRAIN_FORMS_NW) W = curl U = Omega, t = abs(W)^2
  and G = DU.
- Bernoulli function. Here, as in the report (section 0.2) and in Theory Agent B section 12, H = P + abs(U)^2/2 + (Ay).U. The
  identities (I1)-(I2) of Theory Agent B section 1 are written for the prompt's function H_0 = H - c(1-2c)abs(y)^2/2 (the H_0
  of the report's Theorem 2). For a solution, (I1) gives grad H_0 = -(1-2c)X - Omega x B, hence
  grad H = -(1-2c)U - Omega x B = B x Omega - (1-2c)U since X - cy = U; (I2) gives B.grad H_0 = -(1-2c)X.B, hence
  B.grad H = -(1-2c)(X.B - c y.B) = -(1-2c)U.B; and Omega.grad H = -(1-2c)h. These are the forms used in 3(b)-(d)
  below and in the report's section 0.2.
- (D3) is (I3) at Res = 0. (D4) is (I8) with U.(Omega.grad)U = Omega.grad q. (D6) is (I7) at Res = 0 together with
  div B = 3c. (P1) is (I6); without div U = 0 it has the extra terms div U + B.grad(div U). The helicity transport
  B.grad h + (1+c)h = Omega.grad g of 3(d) is the identity quoted in Theory Agent B (I15). The affine solutions of (P3) are those
  of Theory Agent B section 8.
- Not in Theory Agent B's file (agent-local; verdicts in section 5 and in the files named there): the ball versions (B1)-(B6),
  the pressure statements (P2)-(P7), the kinematic identity int phi (abs(S)^2 - abs(W)^2/2) = int U_i U_j d_i d_j phi,
  the weighted transport identities, the Betchov divergence form and the master density D[a, b, g].

### 1. Conservation laws (divergence form)

Each line holds pointwise for C^1 (resp. C^2 for (D4), (D6)) fields with Res = 0 and div U = 0. The remainder
when Res != 0 is stated in the script.

    (D1) energy         (1 - 5c/2)|U|^2 + div(qB + PU) = 0
    (D2) momentum       (1 - 4c)U + omega JU + div(U (x) B + P I) = 0,       (U (x) B)_ij = U_i B_j
    (D3) angular mom.   (1 - 5c) ell + div(ell B + P Jy) = 0                  (omega-free)
    (D3h) horizontal    (1 - 5c) M_K + div(M_K B + P Ky) = omega M_{[J,K]},  M_K = (Ky).U, K antisymmetric;
                        [J, K_1] = K_2, [J, K_2] = -K_1 (K_i = e_i x .), so for Z = M_1 + i M_2:
                        (1 - 5c + i omega) Z + div(Z B + P (K_1 + i K_2) y) = 0
    (D4) helicity       (2 - 4c) h + div(hB + (P - q)Omega) = 0
    (D5) virial         (1 - 5c)(y.U) + div(B(y.U) + Py) = |U|^2 + 3P
    (D6) enstrophy      (1 - 3c/2)|Omega|^2 + div(B|Omega|^2/2) = Omega.S Omega      (pressure-free, omega-free)

Derivations. (D1): dot the equation with U, use U.JU = 0 and div B = 3c. (D2): (B.grad)U = div(U (x) B) - 3cU.
(D3): B.grad ell = (2c-1) ell - (Jy).grad P (Theory Agent B (I3)), div(Jy) = 0. (D3h): B.grad M_K = (2c-1)M_K
+ omega ([J,K]y).U - (Ky).grad P (the term K A y . U - omega (Ky).JU gives omega([J,K]y).U), tr K = 0.
(D4): B.grad h = -(2-c)h - Omega.grad(P - q) (Theory Agent B (I8) with U.(Omega.grad)U = Omega.grad q), div Omega = 0.
(D5): B.grad(y.U) = (2c-1) y.U + |U|^2 - y.grad P. (D6): (4.2) of in the team records with div B = 3c.

Scaling rule (why none of these can exclude natural tails). If a density rho is twisted homogeneous of degree d
(rho(e^{sigma A}y) = e^{c d sigma} rho(y)), then div(rho Ay) = c(d+3) rho. In every identity above the source
coefficient equals c(d+3) for the natural degree d of the density: d = -2(1-c)/c for |U|^2, ell has
d = 1 - (1-c)/c, h has d = -(1-c)/c - 1/c, |Omega|^2 has d = -2/c. For example (D1): 5c - 2 = c(3 - 2(1-c)/c), and
(D6): c(3 - 2/c) = 3c - 2. (D2) and (D3h) carry the rotation in a matrix coefficient that matches the twist.
So for an exact twisted-homogeneous tail each identity reduces, to leading order, to the exact identity of the linear
far-field transport (1-c)U + Ay.grad U + omega JU = 0. This is the structural reason behind THEOREM_A Remark A.9.

Physical reading of the coefficients (PHYSICAL_DICTIONARY items 0 and 6). Under the similarity transform of
PHYSICAL_DICTIONARY item 0 (x = e^{-sA}y, s = -log(T-t)), each of (D1)-(D6) is the similarity form of a local balance
law of the Euler equations, and the coefficient of the density is its self-similar weight w, defined by
int_{e^{-sA}D} (density of u) dx = e^{ws} int_D (density of U) dy: energy |u|^2 dx has w = 2 - 5c, momentum u dx
has 1 - 4c, angular momentum x x u dx has 1 - 5c, helicity u.omega dx has 2 - 4c, the virial x.u dx has 1 - 5c
(not conserved: source |U|^2 + 3P), enstrophy |omega|^2 dx has 2 - 3c (not conserved: source Omega.S Omega), and
volume has -3c. The fluid of a carrier-invariant set D occupies e^{-sA}D at time t. A Lagrangian invariant with
w != 0 therefore vanishes on every invariant object on which it has no flux: the volume of a carrier-invariant
measurable set is 0 or infinite (|Phi_s D| = e^{3cs}|D|); the helicity of a set invariant under both flows is 0
(Moffatt; this is A302 on such sets); the circulation of a periodic carrier orbit is 0 (Kelvin, w = 1 - 2c; A004).
The energy of a material region is not invariant (pressure work through its boundary), which is why on a
carrier-invariant D the integral of (D1) leaves the free constant e_D of C33 with only sum e = 0 found (A435, A436).

### 2. Ball versions with all boundary terms

Let n = y/|y| and R > 0. On S_R: B.n = cR + U.n, because (Jy).n = 0; (Jy).n = 0 and (Ky).n = 0 for every
antisymmetric K; int_{S_R} U.n = 0 and int_{S_R} Omega.n = 0. Integrate over B_R (C^1 fields, divergence theorem).

(B1) Energy. (cR/2) E'(R) + (1 - 5c/2) E(R) = - int_{S_R} (q + P - p) U.n,  for every constant p.
     The constant may be chosen independently for each R (THEOREM_A Lemma A.2.1).

(B2) Momentum. With m(R) = int_{B_R} U:
     ((1 - 4c) I + omega J) m(R) + int_{S_R} [ U (cR + U.n) + (P - p) n ] dS = 0,  for every constant p.
     The pressure enters through int_{S_R}(P - p)n, which is not sign-definite and is the full far-field pressure
     dipole; the constant drops because int_{S_R} n = 0.

(B3) Vertical angular momentum. With Gamma(R) = int_{B_R} ell:
     (1 - 5c) Gamma(R) + c R Gamma'(R) + int_{S_R} ell U.n dS = 0.
     The pressure is absent (P Jy.n = 0 on spheres). The same holds for every axisymmetric weight w(r_perp, z):
     div(w(ell B + P Jy)) = -(1-5c) w ell + ell B.grad w, since grad w . Jy = 0.
     Asymptotics (H0(C^1), Hb, 2/5 <= c < 1): with gamma = 5 - 1/c > 0, R^{-gamma} Gamma(R) -> Gamma_infinity and
         | R^{-gamma} Gamma(R) - Gamma_infinity | <= C R^{-1/c},      R >= 2,
     using only E(R) <= C R^alpha (THEOREM_A; E bounded at c = 2/5) and |ell U.n| <= R|U|^2 on S_R.
     Proof: d/dR(R^{-gamma}Gamma) = -(1/c) R^{-gamma-1} int_{S_R} ell U.n, whose modulus is at most
     (1/c) R^{-gamma} E'(R); integrate by parts on [R, infinity) and use alpha - gamma = -1/c < 0.
     Identification: with Ut_s and U_T as in the team records (0.1) and Theorem B, the substitution y = e^{sA}x and
     (Q_s J y).(Q_s U) = (Jy).U give, for R = e^{cs},
         R^{-gamma} Gamma(R) = int_{B_1} (Jx).Ut_s(x) dx,
     and (Jx)1_{B_1} is a fixed L^2 test function, so weak L^2_loc convergence suffices:
         Gamma_infinity = int_{B_1} (Jx).U_T(x) dx.
     No sign information: this is the vertical angular momentum of the blow-down in the unit ball, of either sign,
     and zero if U_T = 0 (for instance under Corollary B.2).

(B3h) Horizontal angular momentum. With Z(R) = int_{B_R}(M_1 + i M_2):
     (1 - 5c + i omega) Z(R) + c R Z'(R) + int_{S_R} (M_1 + i M_2) U.n = 0 (pressure absent).
     Hence R^{-gamma + i omega/c} Z(R) converges, with the same error O(R^{-1/c}) and under the same hypotheses
     as (B3): Z(R) = Z_infinity R^gamma e^{-i (omega/c) log R} + O(R^{gamma - 1/c}). The horizontal angular momentum
     of a ball spirals with phase -(omega/c) log R, as the twisted tail predicts; Z_infinity is the corresponding
     moment of U_T on B_1.

(B4) Helicity. With Hl(R) = int_{B_R} h:
     c R Hl'(R) + (2 - 4c) Hl(R) + int_{S_R} [ h U.n + (P - p - q) Omega.n ] dS = 0,  for every constant p.

(B5) Virial. Since div U = 0, y.U = div(U|y|^2/2), so int_{B_R} y.U = (R^2/2) int_{S_R} U.n = 0 for every R
     (approach3 item 9). The ball identity of (D5) is then, after int_{S_R} cR(U.n) = 0,
         int_{B_R} (|U|^2 + 3(P - p)) = R int_{S_R} [ (U.n)^2 + (P - p) ] dS,     every constant p,
     a relation between the ball mean and the sphere mean of the pressure. It is the identity recorded in approach3
     item 9; omega does not enter. As approach3 notes, it tests the pressure computation only.

(B6) Enstrophy. With W(R) = int_{B_R}|Omega|^2:
     (cR/2) W'(R) + (1 - 3c/2) W(R) + int_{S_R} (|Omega|^2/2) U.n = int_{B_R} Omega.S Omega.
     Since W' >= 0 and |U.n| <= ||U||_infinity: for every R >= ||U||_infinity / c,
         int_{B_R} Omega.S Omega >= (1 - 3c/2) W(R).
     So on every ball containing the trapping ball the mean strain along the vorticity is at least 1 - 3c/2. This
     threshold is weaker than the pointwise one: (4.2) of in the team records, B.grad|Omega|^2 = 2 Omega.(S - I)Omega, along
     backward orbits (which stay in the trapping ball) forces sup_{supp Omega} lambda_max(S) >= 1 whenever Omega is
     not identically 0. Neither is a contradiction for natural tails.

**Proposition I.1 (total helicity vanishes; CONDITIONAL).** Assume H0(C^2), Hb, 2/5 < c < 1/2 and the natural
derivative rate |grad U(y)| <= C(1+|y|)^{-1/c} (an H3 hypothesis). Then h is integrable and int_{R^3} h = 0, for every
omega.

*Proof.* |h| <= 2|U||grad U|, so int_{A_R}|h| <= C R^{-1/c} |A_R|^{1/2} E(2R)^{1/2} <= C R^{4 - 2/c} by Theorem A, and
4 - 2/c < 0: h is integrable and Hl(R) -> Hl_infinity. Average (B4) over R in [R_0, 2R_0] and use the annulus
pressure decomposition of THEOREM_A Lemma A.3.1 with p = p_{R_0}: ||P - p_{R_0}||_{L^2(A_{R_0})} <= C R_0^{alpha/2}
(from (3.1)-(3.3) and E <= C r^alpha), ||Omega||_{L^2(A_{R_0})} <= C R_0^{3/2 - 1/c},
int_{A_{R_0}} |U|^2|Omega| <= C R_0^{alpha - 1/c}. Then
(1/R_0) int_{R_0}^{2R_0} |flux| dR <= C (R_0^{4 - 3/c} + R_0^{3 - 2/c} + R_0^{4-2/c}) -> 0, and the average of
cR Hl'(R) is at most 2c int_{A_{R_0}}|h| -> 0. Hence (2 - 4c) Hl_infinity = 0. []

This sharpens approach3 item 31 (H_tot = 0 for differentiated twisted-homogeneous tails with P = O(r^{-2alpha})):
no tail form and no pressure decay is assumed; the pressure enters only through A031 and Lemma A.3.1. Like the other
identities it is satisfied by natural tails and is not an obstruction.

### 3. The pressure

(P1) Poisson equation. For every C^2 field U (divergence-free or not),
         div Res = Delta P + d_i U_j d_j U_i + div U + B.grad(div U),
     and the omega-terms cancel identically: div((Ay).grad U) contains -omega J_ji d_j U_i and div(omega JU) contains
     omega J_ik d_i U_k, which are opposite (Theory Agent B (I6) states this as +omega Omega_3 - omega Omega_3). For solutions,
         - Delta P = d_i U_j d_j U_i = d_i d_j (U_i U_j),
     pointwise for U in C^1 (with P in C^2) and in D'(R^3) in the second form. omega does not appear.

(P2) Canonical pressure (bounded U). For F_ij = U_i U_j bounded, the canonical pressure gradient is the tempered
     distribution
         < d_k P_can, phi > = - sum_ij int F_ij T_ij(d_k phi) dx,    T_ij = R_i R_j (symbol -xi_i xi_j/|xi|^2),
     well defined because T_ij(d_k phi) = O(|x|^{-4}) at infinity. Kernel of T_ij: -(1/3) delta_ij delta_0
     + p.v. K_ij, K_ij(w) = (3 w_i w_j - delta_ij |w|^2)/(4 pi |w|^5). P_can itself is defined only modulo
     constants (it is in BMO), and no normalization of the constant is ever needed: every identity above involves P
     only through grad P, through int_{S_R}(P - p)(.).n with a vector field of zero flux, or through
     int (P - p) div(test) (THEOREM_B (i)).

(P3) Harmonic ambiguity, exactly. For a C^1 solution with U bounded, the equation gives
         grad P = -(1-c)U + 3cU - omega JU - div(U (x) Ay) - div(U (x) U),
     a sum of bounded functions and first derivatives of functions of at most linear growth; so grad P is tempered.
     grad P_can is tempered and Delta(P - P_can) = 0 in D', so grad(P - P_can) is the gradient of a harmonic
     polynomial. Under Hb it is zero: the auditor A031 (CONFIRMED). Without Hb the ambiguity is real: the affine exact
     solutions U = Ay of Theory Agent B section 8 (not decaying) have quadratic pressures. The Poisson equation alone, without
     the momentum equation, does not fix the pressure: the auditor A039 (CONFIRMED) gives a smooth decaying swirl whose
     Poisson-only pressure fails to decay pointwise. All statements of this agent use A031 and nothing else about P.

(P4) Annulus decomposition (THEOREM_A Lemma A.3.1, refereed CORRECT by in the team records). Under H0(C^1) and Hb, for each
     R > 0 there is a constant p_R with P = p_R + Pi_1 + Pi_2 + Pi_3 a.e. on B_{2R}, where Pi_1 comes from
     F on {R/2 <= |z| < 4R}, Pi_2 from |z| < R/2, Pi_3 from |z| >= 4R (subtracted kernel), and
         ||Pi_1||_{L^2} <= eps(R/2) E(4R)^{1/2},    |Pi_2| <= (4/pi) R^{-3} E(R/2) on A_R,
         |Pi_3| <= (192/pi) R I(R) on B_{2R},       I(R) = int_{|z|>=4R}|z|^{-4}|U|^2 <= 4 int_{4R}^infinity r^{-5}E.
     Consequence with Theorem A (2/5 < c < 1): ||P - p_R||_{L^2(A_R)} <= C( eps(R/2) R^{alpha/2} + R^{alpha - 3/2} ).
     The gradient version with a smooth cutoff is THEOREM_B section 2: on D_R = {aR<|y|<bR},
     ||grad P||_{L^2(D_R)} <= C R^{alpha/2} [ m(aR/4) + eps(aR/4)/R + R^{(alpha-5)/2} ].

(P5) Pressure torque. d_theta P = (Jy).grad P. int_{S_R} d_theta P = 0 and int w d_theta P = 0 for every
     axisymmetric weight w with enough decay (A034). On every compactly supported B-invariant probability measure mu,
     however, omega int d_theta P dmu = (2c-1) int |X|^2 dmu, which is negative unless X = 0 on supp mu
     (in the team records F.1). So the torque averages to zero against Lebesgue-axisymmetric weights but not against
     invariant measures: this is the precise form of "the defect of the omega = 0 Lyapunov function is the pressure
     torque" (the coordinator Note 3 item 2).

(P6) c = 2/5 (mechanism only; not used in any claim). U is in L^2 with tail O(R^{-5}) (THEOREM_A Proposition A.6).
     The natural tail has |U| ~ |y|^{-3/2}, which is not in L^2, so it is absent; the far-field pressure is then a
     quadrupole of size |y|^{-3} with coefficients int U_iU_j, its gradient is of size |y|^{-4}, and the linear
     transport (1-c)U + Ay.grad U + omega JU = -grad P answers with a forced velocity of size |y|^{-4}, whose
     L^2 tail is R^{-5}. This is why the exponent 5 in Proposition A.6 is the natural limit.

(P7) Fixed representative and decay of the pressure (added 2026-11-03 00:19Z). Pressure from its Poisson equation,
     with the constant never normalized by hand:
     (a) Decaying class (U -> 0 uniformly, C^2), 2/5 <= c < 1/2, every omega: there is one representative P0 (the
         canonical one of A031) with int_{B_R} |P0|^p <= C_p R^alpha for R >= 1 and every 2 <= p < infinity
         (the auditor A277 for p = 2, A292 for p > 2; double Riesz bound on B_{2R} plus the dyadic tail). No pointwise
         decay of P0 follows from this alone (A277).
     (b) Under (D) (and H0(C^2), Hb, 2/5 < c < 1/2): for ANY C^1 pressure P there is a constant p_inf with
         |P - p_inf| + |H - p_inf| <= C|y|^{1-k}, k = (1-c)/c, H = P + q + (Ay).U; and p_inf = 0 for P0. Proof
         (BERNOULLI_ORBIT Lemma H(a), C28): grad H = -(1-2c)U - Omega x B = O(|y|^{-k}) by Theorem T, so H has a uniform
         limit; P - P0 is harmonic and equal to a bounded plus an L^2 function (U in L^4), hence constant. So under
         (D) the pressure normalization is a theorem, not a convention. Sharper for P0 (PHYSICAL_DICTIONARY Lemma P,
         C29, added 00:45Z): |P0(y)| <= C(1+|y|)^{-2k} log(2+|y|), so H - tau = o(|y|^{1-k}) uniformly at infinity.
     (c) Bernoulli function along B-orbits. B.grad H = -(1-2c) U.B and Omega.grad H = -(1-2c) U.Omega (from Theory Agent B (I1)-(I2); see section 0 for H and H_0).
         Integrated forward: H(x) - p_inf = (1-2c) int_0^infinity U.B(Phi_s x) ds, almost everywhere in the decaying
         class (LIT61, A287) and at every x off the forward-bounded set K under (D) (C28). Renormalized coefficient:
         e^{(1-2c)t}(H(Phi_t x) - p_inf) -> kappa(x), with kappa o Phi_t = e^{-(1-2c)t} kappa; a.e. and in L^p_loc,
         p < 2(1-c)/(1-2c) (LIT62-63, A288, A292); under (D), kappa = tau o S with tau(z) = (Az).U~(z), and kappa is in
         L^p_loc exactly for p < 3c/(1-2c) unless tau = 0 (C28, H.4).
     (d) Helicity as a divergence: with g = U.B, div(hB - g Omega) = -(1-2c) h (coord_math (22.2); from the helicity
         transport B.grad h + (1+c) h = Omega.grad g). Under (D), h is in L^1 and int_E h = 0 for every vortex-invariant
         E (C28, H.2; localizes A114, contains A083 = C10).

### 4. Hypotheses used (coordinator labels)

(D1)-(D3h), (D5), (B1)-(B3h) as identities, (B5), (P2): H0 with U, P in C^1; no decay. (D4), (D6), (B4), (B6), (P1):
U in C^2 (P in C^2 follows from the equation, the auditor A032-A034 note). (B6) inequality, (P3): U bounded. (P4): H0(C^1) + Hb
(A031). (B3), (B3h) asymptotics: H0(C^1) + Hb + 2/5 <= c < 1 (through Theorem A). Proposition I.1: H0(C^2) + Hb +
2/5 < c < 1/2 + natural derivative rate (H3). No identity uses omega = 0, symmetry or smallness.

### 5. Index of the later identities of this agent (claims and audit numbers; files in this agent)

| identity | file | claim | audit |
|---|---|---|---|
| Backward Bernoulli integral on cycles, far-surface flux, excursion count | in the team records section 2 | C18 | A149-A152 |
| Endpoint Liouville theorems (Lorentz and weighted) | in the team records | C19 | A165, A166 |
| Weak-profile energy defect | in the team records | C20 | A176-A178 |
| Scattering map, tail, Lamb identities (4.3), (4.4'), (4.6)-(4.8) | in the team records | C21 | A209-A211, A215, A236 |
| Finite-energy remainder T.7, N = gamma int abs(W)^2 | in the team records | C23 | A250 |
| Tail decomposition without (D), T.8 | in the team records | C24 | A251 |
| Adjoint moment identities T.9 | in the team records | C25 | A254, A281 |
| Vortex-line return, Theorem V | in the team records | C26 | A274 |
| Local energy flux f = gamma abs(W)^2 - div J; basin form; energy along B-orbits (B.9) | in the team records | C27 | A275, A276, A282 |
| Lemma H, kappa = tau o S, H.1-H.4 | in the team records | C28 | A295, A296, A302 |
| Physical dictionary: (D) as time-integrated Lipschitz norm, Weber form of (4.7), Lemma P | in the team records | C29 | A353, A354, A355 |
| Bernoulli rewrite f = (2-5c)V.W + div G, basin identities with kappa, invariant-current obstruction | in the team records | C30 | A356-A359 |
| Tail basin: Theorem TB (dissipative tail vortex flow), e^{(2-c)t} h(Phi_t y) -> h~(Sy), master form (3.0) delta int psi'(k_0)h_0 = (k-1) int (k_0 psi'(k_0) + psi(k_0))G_r, k_0 transport (1.2), alpha = S^* beta, Corollary FB | in the team records | C31 | A360-A363; A364 OPEN (summaries, corrected) |
| Mean decay on fixed sets: escaping limit e^{p delta t} int_Q abs(H0 o Phi_t)^p -> int_Q abs(kappa)^p (p < 3c/delta), core identity e^{3ct} int_Q abs(F o Phi_t)^p = int abs(F)^p 1_Q o Psi_t, floor MD.1, crossovers c = 2/7, 2/5, dichotomy MD (d) | in the team records | C32 | A408-A411 CONFIRMED (cond. on (D)); A412 OPEN (closure is a judgment) |
| Refined law on invariant sets: Lemma SI, RE (e_D = int_D(abs(U)^2 - abs(V o S)^2) = gamma^{-1} int_D U.grad P, sum e = 0, ball form O(R^{2-3k} log R)), RH' = TAIL_BASIN (3.1') | in the team records | C33 | A435 CONFIRMED (cond. on (D)); A436 OPEN (route closure) |
| Physical form of Omega.grad H = -delta h (vortex-line Bernoulli law omega.grad beta = -(1-2c)u.omega, beta = (T-t)(p + abs(u)^2/2) + (Ax).u); (D4) as Moffatt's law, weight 2 - 4c; Kelvin form oint_{Phi_s C} U.dy = e^{-(1-2c)s} oint_C U.dy | in the team records item 6 | reading of A302, A004 (not a claim) | - |
| Singular rays (Lemma SR): (T-t)^{1-c} abs(u) and (T-t) abs(grad u) are invariant under (x,t) -> (e^{-sigma A}x, T - e^{-sigma}(T-t)); U -> 0, DU -> 0, abs(DU) = O(abs(y)^{-1/c}) iff the corresponding singular set at time T is empty, otherwise it contains a twisted ray; the last implies (D) | in the team records item 7 | C34 | CONFIRMED A475 (scaling theorem) |
| Gradient gap (Theorem GD): limsup lambda_max(sym DU) < 1 implies abs(DU) <= C(abs(y)^{-kappa/c} log abs(y) + abs(y)^{-1}) (H0(C^2), U bounded, 0 < c < 1); hence DU -> 0 <=> (D) <=> power rate, and lambda_max, abs(DU) have limsup in {0} union [1, infinity]; under Hb, 1/3 < c < 1 also <=> abs(DU) = O(abs(y)^{-1/c}); Sigma_I = Sigma_S | in the team records | C35 | CONFIRMED A476-A477 |
| Vorticity gap (Proposition VG): for bounded DU, abs(DU(y)) <= C[omega*(abs(y)/16)(1 + log abs(y)) + abs(y)^{-1}], omega*(r) = sup over abs(z) >= r of abs(curl U); hence DU -> 0 <=> omega*(r) log r -> 0 <=> vorticity Dini <=> BKM integral away from 0 finite (H0(C^2), 0 < c < 1) | in the team records | C36 | CONFIRMED (A584 at the bounded-U, bounded-DU scope; A585 equivalences); its gap classes are empty by A492 (A586) |
| Bounded pressure and orbit derivative (Proposition BP, from the external referee (a second model) and the auditor; Corollary AV): for bounded U and DU, grad P is bounded, abs(DU Ay) <= C, abs(DU e) + abs(curl U . e) <= C/abs(y) (e = Ay/abs(Ay)); hence DU = S_h + e (x) g + O(1/abs(y)) (planar strain across the orbits plus a transverse gradient); if U -> 0, grad P -> 0 (H0(C^2), 0 < c < 1, any omega, no decay of U) | in the team records | C37 | CONFIRMED (A485) |
| Mean decay (Proposition SL, Theorem MD): for bounded U and DU, int over r < abs(y) < 2r of abs(S_h)^2 <= C r^2 (from int phi tr(DU(r.)^2) = r^{-1} int grad phi . grad P(r.)); abs({r < abs(y) < 2r : abs(curl U) >= delta}) <= C_delta r^2 (occupation bound along the B-flow); r^{-3} int over the annulus of abs(DU)^2 <= C r^{-kappa}; physically the time integral of the L^p norm of grad u on annuli is finite for p < infinity (same hypotheses) | in the team records | C38 | CONFIRMED (A499, as corollaries of A492 and A476; the thin-layer kinematic example is not certified) |
| Pointwise decay (Lemma CP, Proposition PS, Theorem PD): for bounded U and DU (any omega, 0 < c < 1, no decay of U), abs(dF(0)) <= sup abs(F)/rho + (2/alpha)[g]_alpha delta^alpha + 2 sup abs(g) log(rho/delta) (g = dbar F, planar Cauchy-Pompeiu) applied to F = U_1 - i U_2 on discs of radius abs(y)^{1/2} transverse to e, with BP, AV and the polynomial Holder bound of VORTICITY_GAP Step 4, gives ||S_h|| <= C abs(y)^{-1/2} log abs(y), then abs(curl U) + ||DU|| <= C (1 + abs(y))^{-1/8}; the literature agent LIT120 (same mechanism, multiplicative damping) improves this to O(1/abs(y)) | in the team records | C39 | CONFIRMED (A492, with LIT120) |
| Strain threshold (Lemma 1, Theorem ST, Corollaries ST.1-ST.2): exterior B-orbits from abs(y) = R_1 >= 2M/c have abs(c s - log(r/R_1)) <= 1; d abs(W)^2/ds <= 2(lambda_max - 1) abs(W)^2 (self-similar Cauchy stretching, the external referee (a second model)'s); lambda_max <= L outside a ball gives abs(W) <= C r^{(L-1)/c}, ||DU|| <= C r^{max(0,(L-1)/c)}; with A498, limsup lambda_max < 1 + c/2 (bounded U) or lambda_max <= 1 + c/2 + eps (U -> 0) forces DU -> 0; with A507 and abs(U) <= C r^{-kappa}, below 1 + c min(1, (1 + kappa)/2) (H0(C^2), 0 < c < 1, any omega) | in the team records | C40, C41 | C40 CONFIRMED (A506); C41 CONFIRMED (A520) |
| Basin identities for P1 (OB.1-OB.4): int_E phi h = (1/a) int_E H0 Omega.grad phi and int_E h Phi = 0 for Phi measurable for sigma(vortex-invariant sets, H0); quadratic helicity identity div(B w h^2/2) = -(1 - c(1+beta)/2) w h^2 + w h Omega.grad g (B.grad w = c beta w), integrated (Q_0) (1 - c/2) int_D h^2 = int_D h Omega.grad g, equivalently (2 - 5c/2) int_D h^2 = -int_D h Omega.grad(P - q), all tautologies of (E2) and the commutator; Delta H0 = div(B x Omega); int abs(DU)^2 = int abs(Omega)^2, int tr(DU^2) = 0; boundary forms d_nu H0 = eps abs(B x Omega) + a (Ay).nu, gamma e_D = lim int_{dD} chi_R P U.nu = -lim int chi_R P (Ay).nu, (3.2)-(3.3); e_D = 0 for e^{tA}-invariant D, e_D = int_D abs(U)^2 for U in L^2(D); linear helical tail model | in the team records | C42 | PROVED at the A524-A527 scopes (CONFIRMED 07:11Z, recorded 07:19Z): OB.1 integrated scope (A524), OB.2 identities and conditional replacement (A525), OB.3 boundary formulas, arbitrary measurable D (A526), models at reduced scopes (A527); method statement OB OPEN (A529). Band form of the first identity = A328; tautology = gauge of A322; boundary and Poisson forms from the external referee (a second model) p1core |
| Vortex-line stretching (Lemmas VL.0-VL.1, Theorem VL, Corollaries VL.2-VL.5): along a vortex segment, int xi.S xi dl = [U.xi]_ends - int U.kappa n dl and d/dl log abs(W) = -div xi (kinematic); material segments gamma_s = Phi_s o gamma_0 (d gamma_0/d sigma = W) have d gamma_s/d sigma = e^{(1+c)s} W(gamma_s), L' = int (c + xi.S xi) dl, int abs(W(gamma_s)) d sigma = e^{-(1+c)s} L; hence e^{cs}(L_0 - E) <= L <= e^{cs}(L_0 + E), E = int_0^s e^{-c tau}(2 + K) M d tau, and abs(W) <= e^{D} w_0^+ e^{-s}(1 + E/L_0); far-field coherence sup abs(D xi) >= 1/(100 m(r/2)) on unit-window ribbons where W does not decay (or a vortex line of length at most 3.9 m(r/2) with unbounded div xi); conditional DU -> 0 under (H_theta), theta < 1/2 | in the team records | C43 | CONFIRMED (A579 VL.0-VL.2 and Theorem VL, bounded U; A580 VL.3-VL.4 as a conditional theorem; A581 VL.5 with the finite-line and disjunction repairs); uniform in omega; (H_theta) not proved |
| Exact potential profiles (Proposition 8.1, Example 8.2, Proposition 8.3): for phi harmonic on an open set, U = grad phi and P = -(a phi + U.Ay + abs(U)^2/2) solve the profile equation, any c and omega; (y1^2 - y2^2) y3 and e^{k y3} J_2(k rho) cos(2 theta) vanish on the outgoing orbit {y1 = y2 = 0, y3 > 0} with lambda_max = 2 abs(y), resp. (k^2/4) e^{k abs(y)} there; irrotational U with abs(U) <= m on B(y, rho) has norm(DU(y)) <= 3m/rho | in the team records section 8 | C44 | CONFIRMED (A582) as local countertests; local only (a decaying irrotational profile on R^3 is zero); the reading "DU -> 0 needs rho bounded below" REFUTED (A583); m/rho -> 0 suffices |
| Gauge family W = U + lambda y + grad f, Q = H0 - a(lambda abs(y)^2/2 + f): a W + grad Q = B x Omega, curl W = Omega, W^flat ^ dW^flat = (Omega.W) vol, Omega.grad Q = -a Omega.W; on integral surfaces of W^perp, grad_Sigma Q = (B.n) n x Omega; B.W = c lambda abs(y)^2 + O(abs(y)); B.V = abs(B + (omega/2) Jy)^2 - (omega^2/4) abs(Jy)^2; mirror plane: div_2(Omega3 q) = -a Omega3, jet law L_q eta = -(a + 2 beta) eta | in the team records | C47 | PROVED (A852, A856, A858) |
| Localized strain identity: xi_0.S(z) xi_0 = (3/4pi) int (xhat.xi_0) det(xi_0, xhat, (chi W)(z+x)) abs(x)^-3 dx + R, abs(R) <= 5 log 2 abs(grad chi)_inf sup_annulus abs(U) (div U = 0 near B(z, 2 rho)); covector redundancy (Fv) x (Fw) = det(F) F^-T (v x w), so C(Phi_s y) = e^(-as) DPhi_s^-T C(y) follows from (K0); collinear orbits W = k e^(-bs) B; exact profile N1 (omega = 0) | in the team records | C48 | PROVED (A902, A906, A907) |
| Strain kernel and small-vorticity growth (Theorem SV, Corollaries SV.1-SV.2): for unit e, e.(K(z) f)e = -3 (e.theta) f.(theta x e)/(4 pi abs(z)^3) and e.(M f)e = 0, spherical average of 3 abs(cos psi) sin psi = 1, so the log coefficient for sym grad BS f is 1; (grad u) xi = S xi; abs(curl U) <= W_0 outside a ball gives norm(DU) <= K abs(y)^(gamma/c), gamma > (1 + alpha) W_0/alpha; limsup abs(curl U) in {0} union [c/4, infinity) (bounded U), [c/2, infinity) under U = O(1/abs(y)), [1/4, infinity) under the natural tail for 2/5 < c < 1/2 | in the team records | C49 | CONFIRMED (A1068-A1074) |
| Combined pair kernel (Lemma PK, Theorem SV', Corollary SV.1'): e'.(K(z) f)e' - alpha e.(K(z) f)e = -3 f.(theta x M_alpha theta)/(4 pi abs(z)^3), M_alpha = e' e'^T - alpha e e^T; e' e'^T - e e^T has eigenvalues 0, +-sin(beta); c_K = (3/(4 pi)) int abs(theta x diag(1,-1,0) theta) = (6/pi) int_0^(pi/2) sin^2 t E(sin t) dt = 1.7796... < 1.77963978; Theorem SV for every gamma > c_K W_0; gap thresholds c delta_*/c_K, 1/(2 c_K) > 0.28095 under the natural tail | in the team records | C50 | CONFIRMED (A1171-A1177) |
| Carrier-frame transverse block (Theorem TV, Corollaries TV.1-TV.3): with e = B/abs(B), Pi = I - e e^T, T = Pi G Pi, g = Pi G^T e, h = G e: abs(Pi W - e x h) = abs(g), so abs(g) <= abs(W) + abs(h); tr G^2 = tr T^2 + 2 g.h + (e.h)^2; Pi G = T + (Pi h) e^T; B.grad sigma = -sigma + W.h + W.Pi h; Pi DV Pi = T - q Pi De Pi; DU bounded under (V), (W) and a Holder logarithm O(abs(y)^p), p < min(1 + a, 1/c); gap threshold min(c(1+a), 1)/2, 1/2 under the natural tail | in the team records | C51 | CONFIRMED (A1223-A1226) |
| Transverse block in L^2 (Lemma TP) and growth gap (Corollary TV.4): abs(T)^2 = -Delta P + sigma^2 - 2 g.h - (e.h)^2, abs(DU)^2 - abs(curl U)^2 = -Delta P, abs(DU - e g^T)^2 = abs(T)^2 + abs(h)^2 (exact, carrier frame); avg over B(y, rho) of abs(T)^2 <= (3/rho) sup over the sphere of abs(grad P) + sup (sigma^2 + 2 abs(g) abs(h)); with bounded curl, DU = O(abs(y)^delta), delta < min(1 + a, 1/c), implies DU bounded | in the team records | C52 | CONFIRMED (A1355, A1356) |
| R2 dual pairing and bound (Proposition R2.D): for k = theta x M theta, M = diag(1, -1, 0), f = x^2 - y^2 on S^2, theta x k = -grad_S (f/2), Delta_S f = -6 f, div_S k = 0, so int k.(grad_S psi x theta) = -3 int psi f for Lipschitz psi; with psi_2 = sgn(f) dist(theta, {abs(x) = abs(y)}), (9/(4 pi)) int psi_2 f = (36/pi) int_0^1 s (1 - s^2)^(1/2) arcsin(s/sqrt 2) ds = 1.66925368..., hence D_1 > 1.66925; exact on the g_R = 0 subclass (reflection plan) | in the team records Remark R2 | C53 | CONFIRMED (A1376-A1378) |
| Weighted enstrophy and local L^2 Calderon-Zygmund identities (Theorem EG): for a profile and compactly supported phi, int phi W.S W = (1 - 3c/2) int phi abs(W)^2 - (1/2) int abs(W)^2 B.grad phi and int phi abs(S)^2 = (1/2) int phi abs(W)^2 + int U_i U_j d_i d_j phi; B.grad <y>^(-m) = -m <y>^(-m-2) (c abs(y)^2 + y.U); v.S v <= (2/3)^(1/2) abs(S) for traceless symmetric S and unit v (equality at diag(2,-1,-1)/sqrt 6); hence limsup abs(W) < sqrt 3 (1 - (3 - m) c/2) gives int <y>^(-m) abs(W)^2 < infinity | in the team records section 2 | C54 | CONFIRMED (A1429) |
| Biot-Savart representation under Hb (Lemmas VL.A-VL.B): for F in C^1_c, F = BS(curl F) + Q(div F) with BS(f) = (4 pi)^(-1) int f(z) x (y - z) abs(y - z)^(-3) dz, Q(g) = (4 pi)^(-1) int g(z) (y - z) abs(y - z)^(-3) dz; if U is C^1, divergence-free, bounded, U(R.) -> 0 in D' and int <y>^(-m) abs(W)^2 < infinity with m < 1, then U = BS(W); dyadic bounds norm(BS(W_k))_2 <= (35/3)^(1/2) 2^k norm(W_k)_2 and, on B_R with 2^(k-2) >= R, <= (16/3) R^(3/2) 2^(-k/2) norm(W_k)_2 | in the team records sections 0-2 | C55 | CONFIRMED (A1524-A1527) |
| Energy-law inputs (Lemma EH.0): E(R) = int_(B_R) abs(U)^2 <= C R^beta for R >= 2, beta = max(5 - 2/c, 0), and int <y>^(-m-2) abs(U)^2 < infinity for m > 3 - 2/c, from Theorem A under Hb alone; these bound E_R = int U_i U_j d_i d_j phi_R by C R^(beta - 2) | in the team records | C56 | CONFIRMED (A1530, A1531) |
| Lemma NW density: with t = abs(W)^2 and g in C^1, g >= 0, (T) B.grad t = 2(W.SW - t) gives int phi_R [2 g'(t)(t - W.SW) - 3c g(t)] = -F_R, F_R = -int g(t) B.grad phi_R >= 0 for R > sup abs(U)/c; with the kinematic identity, D[a, 0, g] = a(abs(S)^2 - t/2) + 2 g'(t - W.SW) - 3c g and W.SW <= (2/3)^(1/2) abs(S) t | in the team records | C57 | CONFIRMED (A1584-A1586) |
| Minimal weight h' = (3/(2t))(1 - (1 - t/3 - 2ch)^(1/2)), h(0) = 0; endpoint pinning S = phi(t)(W W^T - (t/3) I) when the density vanishes; tr G^3 = tr S^3 + (3/4) W.SW; Betchov divergence form tr G^3 = div(Q - (1/2) U tr G^2), Q_j = U_i G_jk G_ki (div U = 0, no pressure) | in the team records sections 2-7 | C58-C61 | CONFIRMED (A1720-A1725, A1727, A1782-A1789, A1886-A1892, A1984) |
| Master density D[a, b, g] = a abs(S)^2 + b tr S^3 + (3b/4 - 2g') W.SW + 2 g' t - 3c g - a t/2 with int phi_R D = a E_R - F_R + b int phi_R tr G^3; trace-free bounds -tr S^3 <= (-lambda_min)_+ abs(S)^2/2, abs(tr S^3) <= abs(S)^3/6^(1/2); iteration Lemma 0' | in the team records section 0 | C62 | CONFIRMED (A2004-A2005, A2009) |
| Affine reduction for linear weights: at fixed lambda_1 = x and p = lambda_2 lambda_3, abs(S)^2 + b tr S^3 = 2x^2 - 2p + 3bxp is affine in p, so D[1, b, gamma t] >= 0 on the strain set reduces to four endpoint cubics in one variable (Lemmas SF.4, SF.4') | in the team records section 4.4 | C63 | CONFIRMED (A2079, A2080) |
| Exact pair table (Corollary SF.7): for each row (c_row, l, M^2, b, gam), Lemma SF.4' at c = c_row with b l < 2 and gam > 1/(4 kappa_0) reduces positivity to f_1a on [0, 2l], f_1b on [0, l/2], f_1c^L(x) = 2x^2 + l(x - l)(3bx - 2) + M^2(alpha x + delta) on [l/2, 2l] and f_3 on [0, l], each with no real root on the closed interval (Sturm counts) and positive at the left end; the six windows cover 2/5 < c <= 1/2 | in the team records section 4.5 | C64 | CONFIRMED (A2121-A2125) |
| Nonlinear-weight reduction (Lemma SF.8): with alpha(t) = 3b/4 - 2g'(t), delta(t) = 2g'(t) - 3c g(t)/t - 1/2, D[1, b, g](S, W) = A(S) + t (alpha(t) s + delta(t)), s = W.SW/t in [lambda_3, lambda_1], affine in s, so positivity on K x {abs(W) <= M} reduces to F_1a, F_1b, F_1c, F_3 > 0 in (x, t); abs(S)^2 - (3/2) lambda_3^2 = (lambda_1 - lambda_2)^2/2, so -lambda_min(S) <= (2/3)^(1/2) abs(S) (Remark SF.11) | in the team records section 4.6 | C65 | CONFIRMED (A2205-A2210) |
| Linear-weight threshold for the C65 pair (Propositions SF.12-SF.13): Sturm and Farkas certificates; the threshold c* = 0.4472205742... (named c_lin in the report since coordinator Note 129; the report's c* is (2/3)(1 - sqrt(t*/3)), A1644) is the root in (447/1000, 179/400) of an explicit irreducible degree-9 polynomial; identities in Q(c*) with exact interval bounds | in the team records sections 4.7-4.8 | C66, C67 | CONFIRMED (A2291-A2295, A2341-A2345) |
| Endpoint uniqueness (Remark SF.14): at c*, D[a, b, gam t] >= 0 on K x {abs(W) <= M} iff (b, gam) = a (b*, gam*); the Jacobian of (b, gam) -> (f_1a(x_a), f_1a'(x_a)) is -M^2 [(3/2)(x_a^3 + M^2 x_a) + (2 - 3c* - 2x_a)((9/4) x_a^2 + (3/4) M^2)] < 0 | in the team records section 4.8 | C68 | CONFIRMED (A2372-A2373) |

All are necessary conditions; none excludes a profile in 2/5 < c < 1/2.

## Part C. Fourier system

## in the team records: the exact azimuthal Fourier system (Theory Agent C)

Audit: sections 1-6 CONFIRMED by the auditor as A032 (independent moving-frame derivation), section 7 as A033, the
pressure-torque formula of section 5 as A034 (under H1', weaker than H1). Axis bounds are necessary conditions only.

Status: derivation complete; every algebraic identity in sections 2 to 6 is checked symbolically by
in the team records (log: in the team records, result ALL PASS, 2026-11-02T18:22Z), with a
negative control in the team records (two deliberately wrong signs are detected as FAIL).
Labels follow the team protocol. Nothing in this file is a nonexistence result; it is the bookkeeping on which
in the team records and the later notes rest.

### 0. Setting and notation

Profile equation (H0: U in C^2(R^3), P in C^1(R^3), div U = 0):

    (1-c)U + [(cI - omega J)y + U].grad U + omega J U + grad P = 0,       0 < c < 1/2, omega real.   (E)

Notation used throughout the agent:

- X = c y + U,  B = (cI - omega J) y + U = X - omega J y,  div B = 3c.
- J y = e_z x y = r e_theta, Omega = curl U, Gamma = J y . U = r u_theta (angular momentum density).
- Cylindrical coordinates (r, theta, z); orthonormal frame e_r, e_theta, e_z; D = r d_r + z d_z = y.grad (Euler
  operator, scaling generator).
- Rotation generator on vector fields: (LU)(y) = (Jy.grad)U - JU. In cylindrical components LU has components
  d_theta u_r, d_theta u_theta, d_theta u_z. (Proof: U_cart = R(theta) u_cyl with R(theta) = exp(theta J), so
  d_theta U_cart = J U_cart + R d_theta u_cyl.)

Since (B.grad)U + omega JU = (X.grad)U - omega LU, equation (E) is equivalent to

    (1-c)U + c D U + (U.grad)U + grad P = omega L U.                                          (E')

L generates the rotation symmetry of the omega = 0 equation, so a solution of (E) is a relative equilibrium
(rotating wave) of the omega = 0 similarity flow.

### 1. Fourier expansion, reality, regularity

For each (r,z) with r > 0 write

    u_r = sum_m a_m(r,z) e^{i m theta},  u_theta = sum_m b_m e^{i m theta},  u_z = sum_m w_m e^{i m theta},
    P = sum_m p_m e^{i m theta},  u_m := (a_m, b_m, w_m).

Reality: a_{-m} = conj(a_m), and the same for b, w, p.

Convergence. For U in C^2 the cylindrical components are C^2 in theta on r > 0, and d_theta^2 of them is bounded by
C (r^2 |D^2 U| + r |DU| + |U|). Hence |u_m(r,z)| <= m^{-2} sup_theta |d_theta^2 u| and the series converges
absolutely and locally uniformly on r > 0. Every identity below is first proved for the full field and then read
off coefficient by coefficient, so no truncation is involved.

Axis regularity (PROVED, elementary). Let f in C^k(R^3) be complex valued and f_m(r,z) its m-th angular
coefficient. Then, locally uniformly in z, f_m = O(r^{min(|m|,k)}) as r -> 0, and f_m = o(r^k) when |m| > k.
Proof: Taylor-expand f in (x1,x2) at (0,0,z) to order k with remainder o(r^k); a homogeneous polynomial of
degree j in (x1,x2) only contains e^{i n theta} with |n| <= j and n = j mod 2.
Applied to U_1 + i U_2 = (u_r + i u_theta) e^{i theta}, U_1 - i U_2 = (u_r - i u_theta) e^{-i theta}, U_3, P with
k = 2 (k = 1 for P if only P in C^1 is used):

    a_m + i b_m = O(r^{min(|m+1|,2)}),   a_m - i b_m = O(r^{min(|m-1|,2)}),   w_m = O(r^{min(|m|,2)}).

Decay. U -> 0 at infinity (H1) gives sup_theta |u(r,theta,z)| -> 0, hence |u_m(r,z)| -> 0 as r^2 + z^2 -> infinity,
uniformly in m.

### 2. Momentum equations, mode m (verified: momentum_r, momentum_theta, momentum_z)

Write, for a mode-k velocity coefficient u_k and a scalar coefficient f,

    (u_k . grad_l) f := a_k d_r f + (i l / r) b_k f + w_k d_z f      (f carries the phase e^{i l theta}).

For every m in Z, on r > 0:

    (1 - c - i m omega) a_m + c D a_m + d_r p_m
        + sum_{k+l=m} [ (u_k . grad_l) a_l - b_k b_l / r ] = 0,                                  (F1)
    (1 - c - i m omega) b_m + c D b_m + (i m / r) p_m
        + sum_{k+l=m} [ (u_k . grad_l) b_l + a_k b_l / r ] = 0,                                  (F2)
    (1 - c - i m omega) w_m + c D w_m + d_z p_m
        + sum_{k+l=m} (u_k . grad_l) w_l = 0.                                                     (F3)

The only place omega enters is the multiplier -i m omega. In particular the m = 0 equations do not contain omega.
The geometric terms -b_k b_l / r (centrifugal) and +a_k b_l / r (Coriolis-type, from the turning of e_theta)
are kept exactly.

### 3. Incompressibility and pressure (verified: divergence, poisson_source, mode_laplacian)

    (1/r) d_r (r a_m) + (i m / r) b_m + d_z w_m = 0.                                              (F4)

Taking the divergence of (E): the linear terms contribute c div U + (y.grad) div U = 0 and omega div(JU) -
omega div((Jy.grad)U) = 0 (each equals -/+ omega Omega_3), so

    -Delta P = tr((grad U)^2) = d_i U_j d_j U_i     (independent of omega and of c).

Mode form, with Delta_m = d_r^2 + (1/r) d_r - m^2/r^2 + d_z^2 and G_k the frame matrix of grad(u_k e^{ik theta})
divided by e^{ik theta},

    G_k = [[ d_r a_k, (i k a_k - b_k)/r, d_z a_k ],
           [ d_r b_k, (i k b_k + a_k)/r, d_z b_k ],
           [ d_r w_k,  i k w_k / r,       d_z w_k ]],

    Delta_m p_m = - sum_{k+l=m} tr(G_k G_l).                                                     (F5)

Pressure. From (E), grad P is C^1 when U is C^2, so P is automatically C^2 (the auditor remark in A032). For bounded
decaying U the pressure is the canonical one up to an additive constant (the auditor A031, no extra H5 needed). The local
Poisson equation (F5) alone does not determine p_m (harmonic modes r^{|m|}-type solutions of Delta_m p = 0 are not
excluded by (F5) itself); with the canonical pressure, p_m is the mode-m part of R_i R_j (U_i U_j) (Riesz transforms
commute with rotations), so p_m = 0 whenever the mode-m part of U (x) U vanishes, except for the arbitrary additive
constant in p_0. Nothing else in this file depends on the normalization.

### 4. Vorticity modes (verified: vorticity_modes)

    Omega_r,m = (i m / r) w_m - d_z b_m,   Omega_theta,m = d_z a_m - d_r w_m,
    Omega_z,m = (1/r) d_r (r b_m) - (i m / r) a_m.                                                (F6)

### 5. Angular momentum (verified: angular_momentum_identity, angular_momentum_modes)

Multiplying the theta-component of (E) by r gives, with Gamma = r u_theta,

    (1 - 2c) Gamma + B.grad Gamma + d_theta P = 0,                                                (G)

and in modes, with Gamma_m = r b_m,

    (1 - 2c - i m omega) Gamma_m + c D Gamma_m + i m p_m + sum_{k+l=m} (u_k . grad_l) Gamma_l = 0.     (F7)

Consequence (PROVED under H0, H1, using trapping A006): backward B-orbits are bounded, 1 - 2c > 0, so

    Gamma(a) = - int_{-infinity}^0 e^{(1-2c) s} (d_theta P)(Y(s;a)) ds,      Y(.;a) the B-flow from a.

In particular d_theta P = 0 everywhere forces Gamma = 0 everywhere (u_theta = 0).

### 6. The angular mean (m = 0) with Reynolds stresses (verified: stress_form_r, _theta, _z)

Split U = Ubar + U' with Ubar = (a_0, b_0, w_0) and U' = sum_{m != 0}. Brackets <.> denote the theta-average,
so <f' g'> = sum_{m != 0} f_m g_{-m} = 2 sum_{m >= 1} Re(f_m conj(g_m)). Using div U = 0 in the form
e_r.(U.grad)U = (1/r)d_r(r u_r^2) + (1/r)d_theta(u_r u_theta) + d_z(u_r u_z) - u_theta^2/r (and its theta and z
analogues, verified for arbitrary fields with the - u div U correction), the mean equations are

    (1-c) a_0 + c D a_0 + (a_0 d_r + w_0 d_z) a_0 - b_0^2/r + d_r p_0
        = -[ (1/r) d_r (r <u_r'^2>) + d_z <u_r' u_z'> - <u_theta'^2>/r ],                         (M1)
    (1-c) b_0 + c D b_0 + (a_0 d_r + w_0 d_z) b_0 + a_0 b_0 / r
        = -[ (1/r^2) d_r (r^2 <u_r' u_theta'>) + d_z <u_theta' u_z'> ],                           (M2)
    (1-c) w_0 + c D w_0 + (a_0 d_r + w_0 d_z) w_0 + d_z p_0
        = -[ (1/r) d_r (r <u_r' u_z'>) + d_z <u_z'^2> ],                                          (M3)
    (1/r) d_r (r a_0) + d_z w_0 = 0.                                                              (M4)

Mean angular momentum Gamma_0 = r b_0 (the theta-average of (G); <d_theta P> = 0):

    (1-2c) Gamma_0 + (c D + a_0 d_r + w_0 d_z) Gamma_0 = - div_rz ( r <u_r' u_theta'>, r <u_z' u_theta'> ),  (M5)

where div_rz(F_r, F_z) = (1/r) d_r (r F_r) + d_z F_z. omega is absent from (M1) to (M5): the angular mean of a
rotating profile solves the NONROTATING axisymmetric profile system forced by Reynolds stresses. (M5) is the
"eddy generation" equation of approach3 (item 25 there); it is restated here for completeness, not claimed as new.

### 7. DSS form and period map (PROVED, direct computation)

Similarity variables: u(t,x) = (T-t)^{c-1} V(tau, x (T-t)^{-c}), tau = -log(T-t), turn Euler into

    d_tau V + (1-c) V + (c y + V).grad V + grad Q = 0.

The ansatz V(tau, y) = R(omega tau) U(R(-omega tau) y), R(alpha) = exp(alpha J), Q(tau,y) = P(R(-omega tau)y),
reduces this to (E) (the d_tau of the rotation produces omega J U - omega (J eta.grad) U). Consequences:

1. V is time-periodic in tau with period T_omega = 2 pi / |omega| (for omega != 0), i.e. the profile is a
   discretely self-similar solution with trivial spatial twist after one period.
2. Characteristics dy/dtau = c y + V(tau, y) correspond, through eta = R(-omega tau) y, to B-trajectories
   d eta / d tau = B(eta). Since R(omega T_omega) = I, the period (Poincare) map of the time-periodic field is
   exactly the time-T_omega map Phi^B_{T_omega} of the autonomous field B.
3. In cylindrical components V_cyl(tau, r, theta, z) = u_cyl(r, theta - omega tau, z): the angular mode m of V
   oscillates in tau as e^{-i m omega tau}. The tau-average of V over one period is the axisymmetric part
   Ubar = u_0 e^0 of U. Mode m of the profile is exactly the time-frequency -m omega component of V.

Item 2 is the bridge to the conditional criterion of Liu (Theorem 7.3, see the literature agent PREPRINT_AUDIT.md): its
hypothesis "almost every backward orbit of the period map converges to a periodic point" is, for our profiles,
a statement about backward orbits of the autonomous field B (the periodic points of Phi^B_T are exactly the zeros
of B and the points of periodic B-orbits whose minimal period is a rational multiple of T_omega).

### 8. Where omega acts

- (F1) to (F5), (G): omega appears only through -i m omega (and, in physical space, through B . grad).
- Pressure Poisson (F5), vorticity (F6), mean system (M1) to (M5): omega-free.
- Precise cancellation statement: for every rotation-equivariant local density Q(U), DQ(U)[LU] = d_theta Q(U), so the
  identity obtained by applying DQ(U) to (E') and integrating against an axisymmetric weight is the omega = 0
  identity (in the team records, Lemma 1, with its exact hypotheses; the earlier blanket wording here is withdrawn,
  following the auditor's remark in A032). The pressure torque d_theta P is not removed by this mechanism.
