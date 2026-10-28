# Independent audit: proof 248 global axis identity with the exact cutoff terms

Audited (read-only):
- verification/proofs/248_global_axis_test_identity/PROOF.md
  sha256 4497829f15140cafbd962a9f6baf1bb09a95d333222b80908be15c0108f052f5
  (matches the expected prefix 4497829f and evidence/derivation.json).
Consulted: proof 247 PROOF.md, AUDIT_CLARIFICATIONS.md, AUDIT_CORRECTION.md, AUDIT_ADOPTION.md;
prior audit xaudit_V292topic.md; proof 167 PROOF.md (eq. (1),(3),(7), lines on the far
expansion and the finite knot interval); proof 190 PROOF.md (statement); proof 241 PROOF.md
and AUDIT_CLARIFICATIONS.md.
Scratch: agent_248/check248.py (exact sympy, symbolic functions; all differences print 0).

## Checks

1. Definitions. PASS.
   proof 167 (1): rho_ell=rho0+chi_inf(r)(r^q-r^k)Theta, q=1/ell, so d/dell r^q=-r^q log(r)/ell^2
   and zeta=-k^2 chi_inf log(r) r^k Theta=-k^2 chi_inf log(r) P_inf, zero on r<=1; equals
   proof 190 zeta=-k^2 KP. n(ell)=3ell-1-c[rho_ell] gives nu=3-c[zeta]=n'_0>=3>0. M0 equals
   proof 190 M_0=(X.grad rho0+L_fix zeta)/n'_0 since L_fix zeta=T zeta+U[zeta].grad rho0.
   lambda=a/ell0=c[h]/(ell0 nu)=alpha_0 c[h] (proof 190 (1)) and equals proof 247 lambda_h; a k=a/ell0
   because ell0=1/k exactly. R_h=A0 h-lambda F0 is proof 190's R_d.

2. Axis coefficients at every y. PASS.
   Parity: U1 odd, U2 even in x; U1(0,y)=0, d_x U1(0,y)=-d_y U2(0,y) by div U=0; with U in C1
   this gives U1=-xQ'+o(x), U2=Q+o(1) pointwise (locally uniformly on compacts). With a C1
   cofactor q=x^2 G, d_x q=2xG(0,y)+o(x), d_y q=x^2 G_y(0,y)+o(x^2). Hence
   axis(U[q].grad rho0)=Q f'-2Q'f, axis(ell0 X.grad F)=ell0(yF'+2F); this gives D f, K_b f, D z,
   y f'+2f and K_v f (D z uses the transport U[rho0], so K_u, and the -zeta term). sympy with a
   parity, divergence-free model including x^3, x^4 corrections: all five differences 0.
   zeta and U[zeta]: zeta is C-infinity on R^2 (zero on r<=1, smooth cutoff, r^k log r smooth
   on r>0, finite-bandwidth Theta), and its cofactor -k^2 chi_inf log(r) r^(k-2) Theta/cos^2 is
   smooth near the axis because Theta is a trig polynomial vanishing to even order at x=0. The
   log factor is harmless since r>=1 on supp zeta. U[zeta]=d/dell U[z_ell] is the canonical
   global velocity of proof 167 (7), with every derivative; it is smooth also on |y|<1 where
   zeta=0 but v need not vanish. Thus the expansion is valid for U[zeta] at every y.
   axis(T h)=0: h=x^4 H, H in C1 gives d_x h=O(x^3), d_y h=O(x^4); V1=ell0 x+U1[rho0]=O(x),
   V2 locally bounded, so T h=O(x^4) at every y (sympy: 0).

3. Identity (1). PASS.
   axis(R_h)=K_b f+a[yf'+2f+K_v f+Dz]-lambda Df. f' coefficient: b+ay+av-lambda(ell0 y+u)
   =b+a(v-u/ell0)=w. f coefficient: -2b'+2a-2av'-lambda(2ell0-1-2u')
   =-2(b'+av'-au'/ell0)+lambda=-2w'+lambda. Hence axis(R_h)=K_w f+lambda f+aDz.
   sympy: identity (1) difference 0 with generic ell0, a, nu.

4. Identity (2). PASS.
   Homogeneity: lim P_inf(x,ty)/x^2=t^(k-2) f_inf(y) for t>0 (substitute x=tx'); oddness in y
   gives f_inf=A sign(y)|y|^(k-2), A=f_inf(1)=lim Theta/cos^2 at the upper axis. Existence of the
   limit needs only quadratic vanishing of Theta. y f_inf'=(k-2)f_inf for both signs (sympy),
   and E f_inf=(ell0(k-2)+2ell0-1)f_inf=(ell0 k-1)f_inf=0. On x=0, r=|y|, so
   chi(y)=chi_inf(|y|) is the correct restriction, and z=-k^2 chi log|y| f_inf.

5. Identity (3). PASS.
   D=E+K_u holds identically (sympy 0). For z=phi f_inf, phi=-k^2 chi log|y|:
   D(phi f_inf)=phi D f_inf+(ell0 y+u)phi' f_inf, D f_inf=K_u f_inf, phi'=-k^2(chi' log|y|+chi/y),
   chi'=sign(y)chi_inf'(|y|). This is the displayed D z. Then
   -a k^2(ell0 y)(chi/y) f_inf=-a k chi f_inf (k^2 ell0=k) combines with lambda f=a k f to
   a k e_chi; the rest is the bracket in (3) with the stated signs. sympy, y>0 and y<0 with a
   symbolic cutoff: (1)-(3)=0 at ell0=1/k; for generic ell0 the residual is
   -/+A a k t^(k-2)(ell0 k-1)(k log t+1)chi, confirming exactly where ell0 k=1 enters.
   The zero convention for chi-products is consistent: chi=0 on |y|<=1, where f_inf is singular
   at 0 but never used, and chi vanishes to infinite order at |y|=1.

6. Identity (4), local reduction, Gaussian. PASS.
   On |y|>=R_chi, chi=1 and chi'=0 (also at |y|=R_chi by smoothness); (3) becomes (4) (sympy 0).
   On |y|<1, z and z' vanish, so (1) is proof 247 (3) with the same w and lambda_h; at |y|=1 all
   z-terms vanish. Gaussian: b=V_xx(0,y)=-g'', -g''=(y-(7/3)y^3+(2/3)y^5)exp(-y^2) (sympy 0),
   b'(0)=1=c[d], a=1/nu, lambda=k/nu. This is the corrected trace of proof 247 AUDIT_CORRECTION,
   not 2g-g''. d=x^4 y P exp(-r^2) gives H smooth and U[d] Schwartz, so the hypotheses hold.

7. Scope. PASS.
   Only pointwise scalar identities are claimed. No high-norm, fractional, bulk or transition
   bound; the transition term is kept explicitly in (3). High-target membership of R_h is
   attributed to proof 190 (1) and proof 241/V283, not to (1). No prescribed-trace construction,
   (I)/(S) violation, inverse or profile claim. Status is stated as pending audit.
   The hypothesis H in C1 (with U[h] in C1 and parity) suffices for the h-terms at every y,
   including y at the background joins, because the h-hypotheses do not interact with the
   joins. The joins affect only rho0 and U[rho0]; line 16 assumes their needed C1 cofactor and
   velocity regularity there (see R1).

## Findings

No BINDING findings.

R1 (REMARK). Background regularity at the finite radial joins is an imported assumption
   (PROOF.md line 16), not proved here. It is consistent with proof 167 (density C6 and piecewise
   smooth on the knot interval, velocity of the same regularity), which with the x^2 factor and
   x-evenness gives a C4 cofactor rho0/x^2 and C1 u. The identity needs only C1 cofactor of rho0
   and C1 U[rho0] near the axis; a citation to proof 167 at line 16 would make this explicit.

R2 (REMARK). The C1 regularity and parity of U[zeta] on the whole axis are used implicitly
   (line 76, "C1 coefficients"). They hold by proof 167 (7) and local smoothness of zeta (check 2),
   and line 101 correctly notes that U[zeta] need not vanish where zeta does.

R3 (REMARK). The phrase "explicit leading linear dilation term cancels exactly" (line 64)
   combines two separate exact cancellations: E f_inf=0 (needs ell0 k=1) and
   a k^2 ell0 chi f_inf=a k chi f_inf against lambda f (needs k^2 ell0=k). Both are correct.

R4 (REMARK). Notation: a, b, v here (a=c[h]/nu, b=U2[h](0,.), v=U2[zeta](0,.)) clash with
   proof 241's weight a, b=r^3 a and potential v. "log(r)" in (2)-(4) means log|y| on the axis.
   The definitions in PROOF.md are explicit, so this is cosmetic.

R5 (REMARK). The continuous value at y=0 and the axis limit near the origin are inherited from
   proof 247 (zero-cutoff region); proof 248 adds nothing there, which is correct since all
   zeta and chi terms vanish on |y|<=1.

VERDICT: PASS WITH REMARKS
