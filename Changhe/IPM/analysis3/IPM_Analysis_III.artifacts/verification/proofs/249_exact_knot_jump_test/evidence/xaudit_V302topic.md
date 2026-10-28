# Independent audit: proof 249 exact spline-knot jumps of the residual-subtracted test

Audited (read-only):
- verification/proofs/249_exact_knot_jump_test/PROOF.md
  sha256 b0f54e54ec043cd8e18434f1be73acf9540689fbf3a446577b1671b17ceaf001 (96 lines),
  matching the expected prefix b0f54e54 and evidence/derivation.json.
Consulted: proof 247 PROOF.md (1),(2) and AUDIT_CORRECTION.md; proof 248 PROOF.md via the
adopted audit xaudit_V298topic.md (axis formulas, nu>0, zeta and U[zeta] smooth); proof 67
PROOF.md (C6 velocity, jump formula (1)); proof 194 PROOF.md plus evidence/check.log,
final_certificate.json, opus_crossaudit_note45.md; proof 68 PROOF.md header and
FINAL_VERIFICATION.md (V077: d>=5.5752); prior audit xaudit_V292topic.md for conventions.
Scratch: agent_249/check249.py (exact sympy; all differences print 0).

## Checks

1. Decomposition (5). PASS.
   c[h]M0=a(X.grad rho0+T zeta+U_zeta.grad rho0) with a=c[h]/nu, and
   -lambda F0=-lambda ell0 X.grad rho0-lambda U0.grad rho0+lambda rho0. The X.grad rho0
   coefficient is a-lambda ell0=0 since lambda=a/ell0; lambda rho0 comes from -lambda(-rho0).
   Hence R_h=T h+a T zeta+(U[h]+a U_zeta-lambda U0).grad rho0+lambda rho0 (sympy: 0).
   M0 and A0 agree with proof 247 (1); R_h, lambda agree with proof 247 (2) (lambda_h=c_h/(ell0 nu)).

2. Smooth-across-knot terms. PASS.
   s_m are C6 with jumping 7th derivative, so rho0 and every theta derivative are C6 in t.
   proof 67 gives V=ell0 X+U0 C6 in t at an interior knot, one-sided analytic, finite angular
   bandwidth, angular derivatives preserving C6 (stream function C7, one derivative). With h,
   zeta, U[h], U_zeta smooth near the circle, T h, T zeta, lambda rho0 and B_h are C6, so their
   sixth t-derivatives have zero jump. Knot in the cutoff transition: chi_inf is smooth, so T zeta
   is still C6; the proof correctly keeps the term and notes zero jump is not zero size.

3. Jump formula (1) and (2). PASS.
   B.grad rho0=(B.e_r/r)d_t rho0+(B.e_theta/r)d_theta rho0 is the correct log-polar form.
   Leibniz in d_t^6: only (B.e_r/r)d_t^7 rho0 contains a 7th derivative; all other products
   have at most 6 t-derivatives of C6 factors, and the coefficient is continuous, so the jump is
   its common trace times [d_t^7 rho0]=r*^3 p S (only the s_m^(7) term of d_t^7(e^(3t)s_m)
   jumps). This gives r*^3 p q_h S. For F0 the full transport V.e_r/r=ell0+U0.e_r/r gives q_0;
   the -rho0 term is C6. This agrees with proof 67 (1). Toy C6 model with independent 7th jumps
   in the density modes and in both velocity radial coefficients: jumps of orders 1..5 vanish and
   the 6th jump equals p(ell0+B.e_r)S exactly (sympy: 0). A C6 velocity adds no 6th jump.

4. Axis trace and (3). PASS.
   r^3 p=x^2 y. Parity (density x-even y-odd; U1 x-odd, U2 y-odd) gives the x^2 y factor for
   every term; T h keeps x^4. Angular division at the axis of finite-bandwidth C6 coefficients
   (U0) and of smooth ones keeps C6 traces, so the theta->pi/2 limit commutes with one-sided
   t-derivatives. gamma=e^(-3t)G: all exp(-3t) Leibniz terms but one involve lower jumps, zero
   since R_h, F0 are C5. S(pi/2)=sum(-1)^m j_m=[A^(7)]=j_A. At theta=pi/2, e_r=(0,1), so
   q_h(pi/2)=B_h2(0,r*)/r*=(b+a v-(a/ell0)u)/r*=w/r* with proof 247's w=b+a(v-u/ell0), and
   q_0(pi/2)=ell0+u/r* (proof 67's d). gamma_q=axis(q)/y is correct: both limits equal the
   continuous quotient q/(x^2 y) at (0,r).
   1D cross-check through proof 248's axis formula axis(R_h)=w f'-2w'f+lambda f+aDz with
   f=yA(log y): the coefficient of A^(7) in d_t^6(axis/y) is w/y (sympy), as claimed; but w
   enters up to its 7th derivative, so the 1D route needs w C7, i.e. u C7 (see check 6).

5. Ratio (4) and signs. PASS.
   (w/r*)j_A / ((ell0+u/r*)j_A)=w/(ell0 r*+u). Both jumps are right minus left, so the ratio
   does not depend on orientation. Nonvanishing: V077 gives d=ell0+u/r>=5.5752 at every radius,
   so ell0 r+u>0. j_A!=0 at knot 700: proof 194 evidence (check.log CONFIRMED,
   nonzero_axis_jump true, exact Fraction arithmetic, join orders 0..6 checked) and cross-audit
   note45 (jump of A^(7) about -9.3e8). t* value: 4958764014967233/2^51=2.20213359..., matching.
   Gaussian: b=-g'' (proof 247 AUDIT_CORRECTION, not 2g-g''), c[d]=1 so a=1/nu. d=x^4 y P exp(-r^2)
   gives smooth H and U[d], so the local hypotheses hold.

6. u is C7 although U0 is only asserted C6. PASS.
   div U=0 gives u'(y)=d_y U2(0,y)=-d_x U1(0,y); at theta=pi/2, d_x=-(1/r)d_theta (correct).
   d_theta U1 has C6 radial coefficients, so u' is C6 in t (equivalently in y), u is C7. Consistent
   with the 2D statement, which never differentiates U0 seven times and needs only C6 traces of
   d_theta U1 after angular division.

7. Scope. PASS.
   Only exact one-knot derivative jumps and their ratio are claimed. No high-norm ratio,
   fractional seminorm, value or bound of w, (I)/(S) violation, inverse or profile claim. Smooth
   parts, other knots, angular remainder and cutoff transition are explicitly not estimated.
   The local hypotheses on h are stated as local; no global high membership is inferred.
   Status is stated as pending audit; no new computation.

## Findings

No BINDING findings.

R1 (REMARK). Citation of j_A!=0. proof 194 PROOF.md itself is conditional ("must establish
   j_A!=0"); the nonzero jump is recorded in its evidence (check.log, final_certificate.json,
   V198) and in note45. Citing V198/the evidence would be more precise. Content is correct.

R2 (REMARK). The u-C7 paragraph is not needed for the 2D proof of (1)-(3), but it is exactly
   what makes the 1D axis route (proof 248 identity) consistent, since d_t^6 of -2w'f involves
   w^(7). The scratch check confirms the 7th derivative of w appears there.

R3 (REMARK). Stronger fact, not needed: with psi C7 (proof 67), U_r=-(1/r)d_theta psi is C7 in t
   everywhere on the annulus; only U_theta is limited to C6. "Asserted only C6" is accurate but
   conservative.

R4 (REMARK). The interchange of theta->pi/2 with one-sided t-derivatives is justified tersely
   (finite bandwidth for rho0 and U0, smoothness for the rest). It is correct: each divided
   coefficient is a finite sum of C6 (one-sided analytic) radial functions times smooth angular
   functions, so joint regularity holds uniformly up to the axis.

R5 (REMARK). Cosmetic: "the second denominator" (line 59) means ell0 r*+u(r*); the letter v here
   is U2[zeta] on the axis, not proof 241's potential (as already noted in AUDIT_CORRECTION).

VERDICT: PASS WITH REMARKS
