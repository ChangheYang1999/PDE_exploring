# Independent audit: proof 247 exact axis identity for residual-subtracted strain tests

Audited (read-only):
- verification/proofs/247_axis_test_identity/PROOF.md
  sha256 c1a71c1651107c32fac3fafa73b5cbb5247b1fe932fd26acec8aadb67bdfe399
- verification/proofs/247_axis_test_identity/AUDIT_CLARIFICATIONS.md (binding)
  sha256 4e7ca8fc3520b7478ab94253edf74e943ef5a2084ee0ccd22a85a5f754a199d3
Both hashes match the prefixes given in the audit request.
Dependencies consulted: proof 167 PROOF.md (chart eq. (1),(3),(12),(13)), proof 190 PROOF.md
(R_d, alpha_0, M_0, n'_0), proof 241 PROOF.md and AUDIT_CLARIFICATIONS.md (Gaussian), proof 01
(strain convention), proof 174 (n(ell0)=0, n'>=3).
Scratch: agent_247/gauss_check.py (exact sympy check of the Gaussian axis velocity only).

## Checks

1. Eq. (4), axis expansion of U[q]. PASS.
   Density even in x, odd in y gives psi odd-odd, U1=-psi_y odd in x, U2=psi_x even in x.
   With U in C1 on the disk: U1(0,y)=0, d_x U1(0,y)=-d_y U2(0,y) (div U=0), so
   U1=-x b'(y)+o(x), U2=b(y)+o(1) pointwise. Only rho0 (background) is differentiated
   afterwards, so C1 of U[h] suffices for (6); the clarification's hypotheses are adequate.

2. Eqs. (5),(6),(7) and the chart column. PASS.
   With rho0=x^2 f+o(x^2), d_x rho0=2xf+o(x), d_y rho0=x^2 f'+o(x^2):
   axis(U[q].grad rho0)=Q f'-2Q' f for Q=U2[q](0,.)  -> (6), and with Q=v the zeta coupling.
   axis(ell0 X.grad rho0)=2 ell0 f+ell0 y f'; adding u f'-2u'f-f gives (5) exactly.
   axis(X.grad rho0)=2f+y f'; axis(T zeta)=0 since zeta=0 on the open disk and T is local;
   hence (7). axis(T h)=0: h=x^4 H, H in C1 gives h, x d_x h, d_y h all O(x^4) locally,
   V1=O(x), V2 bounded, so T h=O(x^4).
   Chart match (proof 167 (1),(3)): rho_ell=rho0+chi_inf(r)(r^q-r^k)Theta, chi_inf=0 on r<=1,
   so zeta=d_ell rho_ell|ell0=-k^2 KP vanishes on r<1 (r_chi=1). n(ell)=3ell-1-c[rho_ell]
   gives nu=n'(ell0)=3-c[zeta]=3+k^2 c[KP]>=3>0, matching proof 190 n'_0. M0=H0+m(ell0),
   m(ell0)=B'(ell0)/nu (removable value), and d/dell F_ell(rho_ell)=X.grad rho0+T zeta
   +U[zeta].grad rho0, so the H0 terms cancel and (1) holds; agrees with proof 190
   M_0=(X.grad rho_0-k^2 L_fix KP)/n'_0. c[f]=d_y U2(0)=psi_xy(0) is the raw strain of
   proof 01. Signs consistent.

3. Coefficient algebra giving (3). PASS.
   f' coefficient: b+(c_h/nu)(y+v)-(c_h/nu)(y+u/ell0)=w.
   f coefficient: -2b'+(2c_h/nu)(1-v')-(c_h/(ell0 nu))(2ell0-1-2u')
   =-2[b'+(c_h/nu)(v'-u'/ell0)]+c_h/(ell0 nu)=-2w'+lambda_h. Verified by hand.
   R_h agrees with proof 190 (1): R_d=A_0 d-alpha_0 c[d]F_0, alpha_0=1/(ell0 n'_0).

4. Eq. (8) and the y-linear cancellation. PASS.
   n(ell0)=0 gives u'(0)=c[rho0]=3ell0-1. Independently: with rho0=x^2 y+O(r^5) and
   U[rho0]=c(-x,y)+O(r^3), the cubic part of F0 is (3ell0-1-c)x^2 y, which is zero exactly
   when c=3ell0-1 (also the y-linear coefficient of (5) is 3ell0-1-u'(0)). v'(0)=3-nu by the
   definition of nu; b'(0)=c_h by definition. Then w'(0)=c_h+(c_h/nu)(1/ell0-nu)=lambda_h.
   w, f odd, f'(0)=1, and w' continuous (C1 velocities) give axis(R_h)=o(y). O(y^3) only
   under smooth (C3) odd expansions, as restricted by the clarification. Correct.

5. Eq. (9), Gaussian application. FAIL.
   With exp(-x^2)=1-x^2+..., V=g+x^2(a_g/2-g)+O(x^4)=g-(x^2/2)g''+O(x^4), so
   b(y)=U2[d](0,y)=V_xx(0,y)=2(a_g/2-g)=-g''(y),
   exactly proof 241 eq. (4). The claim b=2g-g'' omits the -x^2 g contribution of the
   exponential. Exact sympy check: V_xx(0,y)+g''=0 and V_xx(0,y)-(2g-g'')=(y^3/3)exp(-y^2).
   c_d=b'(0)=-g'''(0)=1: PASS (also =V_xxy(0) by sympy). d*exp(r^2) is a polynomial
   divisible by x^4 y (zero remainder): PASS. lambda_g=1/(ell0 nu): PASS.
   Corrected statement: w_g=-g''+(v-u/ell0)/nu, lambda_g=1/(ell0 nu).

6. Scope. PASS.
   Identity (3) is stated as pointwise algebra on |y|<r_chi only; Y_H membership of R_h is
   attributed to prior results (proof 190 (1), proof 241, V283), not to (3). The design
   condition paragraph disclaims existence of h, transition estimates and high-norm
   smallness. No numerical norm, inverse, (S)/(I) decision or profile existence is claimed.
   The zero-cutoff disk restriction is respected and the T zeta term outside it is flagged.

## Findings

B1 (BINDING). Eq. (9) and the sentence before it: "b=2g-g''" is false. The correct axis
   velocity of proof 241's Gaussian is b=V_xx(0,y)=-g''(y), consistent with proof 241 eq. (4).
   Correct to w_g=-g''+(v-u/ell0)/nu (lambda_g=1/(ell0 nu) unchanged). The error is
   b_claimed-b_true=2g=-(y^3/3)exp(-y^2)=O(y^3); it is invisible to c_d=1 and to the (8)
   sign check, but it changes axis(R_d) at its leading nonzero order: with f=y+O(y^3) the
   spurious contribution 2g f'-4g' f equals (5/3)y^3+O(y^5). Any certified evaluation of
   the Gaussian axis test based on (9) would be wrong. Identity (3) itself is unaffected.

R1 (REMARK). Notation: proof 247 (like proof 190) uses zeta=d_ell rho_ell=-k^2 KP, while
   proof 167 eq. (13) uses zeta_ell for M(ell)-chi_0 X.grad rho_ell/3 (=m(ell0) at ell0).
   The definition in proof 247 is explicit, but a cross-reference note would avoid confusion.

R2 (REMARK). "The chart cutoff" should be named chi_infinity (zero on r<=1, so r_chi=1);
   the other chart cutoff chi_0 (in H0) is one near the origin.

R3 (REMARK). Line 55 "The term -2u'f in both formulas" should read -2u'f in (5) and the
   analogous -2b'f in (6).

R4 (REMARK). The PROOF.md phrase "axis(R_h)=O(y^3)" is valid only with the smooth
   expansions; the binding clarification already restricts it (o(y) for the C1 class).

VERDICT: FAIL (binding findings: B1 - eq. (9) Gaussian axis velocity must be b=-g'', w_g=-g''+(v-u/ell0)/nu)

## Addendum: AUDIT_CORRECTION.md

Audited (read-only):
- verification/proofs/247_axis_test_identity/AUDIT_CORRECTION.md
  sha256 5a3dc62bab29e605ec278b122d9b99cddf944fdcf15b2654830bb7c86fdf8a15 (matches 5a3dc62b...)
Re-hashed at addendum time: PROOF.md and AUDIT_CLARIFICATIONS.md unchanged (same sha256 as above).
Scratch: agent_247/corr_check.py (exact sympy check of the correction's claims).

A1. Corrected formulas. PASS.
    States b(y)=partial_xx V(0,y)=-g''(y), w_g=-g''+(v-u/ell0)/nu, lambda_g=1/(ell0 nu),
    and the x^2 coefficient (2g-g'')/2-g=-g''/2. All match check 5 and finding B1
    (sympy: x^2 coefficient of V plus g''/2 is 0; V_xx(0,y)+g''=0).
A2. Explicit trace. PASS. -g''=(y-(7/3)y^3+(2/3)y^5)exp(-y^2): exact sympy identity.
A3. Size of the error. PASS. (2g-g'')-(-g'')=2g=-(y^3/3)exp(-y^2), nonzero for y!=0. Both
    traces have derivative 1 at 0, so the central strain check could not detect the error.
    With f=y+f3 y^3+..., 2g f'-4g'f=(5/3)y^3+(f3-3)y^5+O(y^7); the leading (5/3)y^3 does not
    depend on f3 and agrees with B1.
A4. Notation. PASS. Separating capital V (proof 241's potential v) from lower-case
    v=U2[zeta](0,y) resolves the name clash in (9).
A5. Scope and no new overclaim. PASS. Equations (1)-(8) are unchanged and remain correct
    (checks 1-4). c[d]=1, J[d]=0, zero cofactor and high-domain membership are attributed
    to proof 241 (and its clarification), not to the correction. It states explicitly that
    no full high norm estimate, violation of (I) or (S), or inverse follows.
A6. Resolution of B1. PASS. The correction supersedes equation (9) and the sentence before
    it, and it fully resolves B1. No new binding finding.

Addendum remarks:
AR1 (REMARK). The correction also says it supersedes a sentence in "team note138". That
    file was not part of this audit, so this audit does not check that it was updated.
AR2 (REMARK). The original remarks R1-R4 remain, all non-binding (R1 is partly addressed
    by A4 for the potential name; the zeta_ell clash with proof 167 eq. (13) remains).

UPDATED VERDICT: PASS WITH REMARKS
