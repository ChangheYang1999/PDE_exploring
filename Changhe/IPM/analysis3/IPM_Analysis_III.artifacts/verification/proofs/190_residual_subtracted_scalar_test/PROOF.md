# A finite residual-subtracted scalar test

## Exact setting and statement

Use the exact normalized modal trial rho_0, k=1615536043799051/9007199254740992, ell_0=1/k, the canonical IPM velocity and the moving-tail chart of topics174 and181. Its outer cutoff is zero for r<=1, lies in[0,1], and is one outside a fixed disk. Write

 F_0=F_ell0(rho_0), eta_*=||F_0||Y_H,
 KP=chi_infinity(r) r^k log(r) Theta(theta),
 zeta=partial_ell rho_ell|ell0=-k^2 KP,
 n'_0=3-c[zeta]>=3, alpha_0=1/(ell_0 n'_0),
 H_0=chi_0 X.grad rho_0/3,
 L_fix d=(ell_0 X+U[rho_0]).grad d-d+U[d].grad rho_0,
 L_ren d=L_fix d+c[d]H_0,
 A_0d=L_fix d+c[d]M_0=L_ren d+c[d]m_0,
 M_0=H_0+m_0=(X.grad rho_0-k^2 L_fix KP)/n'_0.

The high target Y_H carries the fixed norm of proof 177, including the scalar a_*H^(25/4) summand. Its graph domain is the high realization on which the inverse estimate in proof 174 is asserted. In particular every test direction below must belong to that domain. The terms L_fix d and M_0 need not belong to Y_H separately. Define their finite combination

 R_d=A_0d-alpha_0 c[d]F_0.                              (1)

For every such d, R_d belongs to Y_H. Put

 Q=rho_0-U[rho_0].grad rho_0-k L_fix KP,
 Q_ren=Q-ell_0 n'_0 H_0.

Then Q_ren belongs to Y_H and the following identities hold:

 ell_0 n'_0 M_0=F_0+Q,
 Q_ren=ell_0 n'_0 m_0-F_0,
 R_d=L_ren d+alpha_0 c[d]Q_ren.                        (2)

Suppose the actual hypotheses(I) and(S) of proof 174 hold in this same high norm. For every actual high-domain direction with c[d]!=0,

 ||R_d||Y_H/|c[d]| >= (1/N_4-alpha_0) eta_*,
 N_4=-n(4).                                           (3)

In the present chart0<N_4<453/50 by proof 181 and alpha_0<=k/3. The certified bound eta_*>38666592266 of proof 187 therefore gives the strict necessary inequality

 ||R_d||Y_H/|c[d]|
 > 3990663377048576117076359567/2040130631198834688
 > 1956082280.                                        (4)

Consequently a certified upper bound ||R_d||Y_H<=1956082280 |c[d]| for one actual test direction with nonzero strain would refute(S). No such upper bound or violating direction is certified in this topic.

## Proof of the finite identities and membership

Differentiation of the moving-tail residual gives n'_0 M_0=X.grad rho_0+L_fix zeta=X.grad rho_0-k^2 L_fix KP. Since ell_0 k=1,

 ell_0 n'_0 M_0=ell_0 X.grad rho_0-k L_fix KP.

The exact residual identity ell_0 X.grad rho_0=F_0+rho_0-U[rho_0].grad rho_0 now proves the first identity in(2). Subtract ell_0 n'_0 H_0 to obtain the second. Proof 167 proves m_0 in Y_H, and proof 177 proves F_0 in Y_H. Thus Q_ren belongs to Y_H. This proof of membership retains both the cubic and leading far cancellation; it does not estimate the individual uncancelled terms of Q in the target norm.

Equation(1) is a difference of two target elements, so it belongs to Y_H for every direction in the asserted domain. Substituting A_0d=L_ren d+c[d]m_0 and the second identity in(2) gives the last identity. The vector L_ren d=A_0d-c[d]m_0 is also in Y_H. Thus every term on the right in this final split has a finite target norm.

For a direct check of the cancellation at the origin, KP vanishes there and L_fix KP=U[KP].grad rho_0 has cubic coefficient-c[KP]. Consequently Q has coefficient1+c[rho_0]+k c[KP]=3ell_0+k c[KP]=ell_0 n'_0. Subtraction of ell_0 n'_0 H_0 removes it exactly. At infinity the leading part of k L_fix KP is k ell_0 r^k Theta=r^k Theta, which cancels the leading density term of Q. The remaining terms, including logarithms, are already controlled by the Y_H-valued identity above.

## Proof of the necessary inequality

The scalar-radius theorem of proof 181 says that(I) and(S) imply

 eta_* |c[d]| <= N_4 ||A_0d||Y_H

for every direction in the high realization. By(1), the triangle inequality gives

 ||A_0d||Y_H/|c[d]| <= alpha_0 eta_*+||R_d||Y_H/|c[d]|.

Combine these inequalities and divide by the positive N_4 to obtain(3). Unlike the refuted separate M_0 norm test, both summands here are elements of Y_H.

Because n'_0>=3, alpha_0<=k/3. Since N_4<453/50,

 1/N_4-alpha_0 > 50/453-k/3 > 0.

The second inequality is an exact rational comparison using the displayed k. Multiplying by the strict lower bound for eta_* gives

 (1/N_4-alpha_0)eta_* > (50/453-k/3)38666592266
 =3990663377048576117076359567/2040130631198834688.

The final rational is greater than1956082280, proving(4) and its stated countertest. These comparisons do not use a floating estimate of n'_0, N_4, an inverse norm or an angular multiplier norm.

## Scope and verification

This validates the algebraic residual-subtraction route outlined in the theory author's12:53Z status while making the finite target split explicit. It does not validate a norm of M_0 or of Q separately. Their nonzero cubic terms put them outside Y_H, as in proof 188. A point lower bound for R_d cannot supply the upper bound required to apply the countertest. A finite-section approximation to d or to A_0d would require a rigorous error bound in this same high norm before(4) could decide(S).

The exact rational threshold is checked in the companion script; the script verifies the accepted derivative-difference certificate hash and records the proof and input identities. The inequality is a conditional theorem. Actual base injectivity, a certified upper bound for a chosen R_d and the truth or failure of(S) remain OPEN.

Dependencies: topics167,174,181,187 and188. All quantities refer to the exact normalized joined modal trial, not an assumption that the raw X3 approximation solves the stationary equation.
