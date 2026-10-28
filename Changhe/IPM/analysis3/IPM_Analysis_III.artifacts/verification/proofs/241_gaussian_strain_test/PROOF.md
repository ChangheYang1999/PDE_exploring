# An exact Gaussian strain-one direction in the high graph domain

## Statement, spaces and scope

Use the actual normalized joined modal trial rho0, V=ell0 X+U[rho0], T=V.grad-1, and the fixed high correction space H_full=B_H direct-sum X_s and target Y_H=Gamma_H direct-sum X_s from topics123,165,167,171 and174. The remainder has physical parity even in x and odd in y. Its cylinder definitions use t=log r, p(theta)=cos(theta)^2 sin(theta), b=r^3 a, a=r^(9/5) at the inner end and a=r^(-7/2) at the outer end. The fixed orders are s0=41/20, sigma=25/4 and s0<=s<=sigma. The near-vertical cofactor h/(b p) has H^sigma regularity and zero trace. The scalar input has order29/4 and the scalar target order25/4. All cutoffs and the equivalent target norm of proof 177 are fixed as in the conditional closure theorem.

Define one-dimensional functions

 g(y)=-(y^3/6)exp(-y^2),
 a_g(y)=2g(y)-g''(y),
 b_g(y)=g''''(y)-12g''(y)+12g(y),

and the exact Schwartz potential

 v(x,y)=exp(-x^2)[g(y)+(x^2/2)a_g(y)+(x^4/24)b_g(y)].       (1)

Put d=-Delta v. Then d is a nonzero Schwartz function with the physical parities, of the exact form

 d=x^4 y P(x^2,y^2)exp(-x^2-y^2)                         (2)

for a rational polynomial P. Its canonical full-plane stream function and velocity are

 psi[d]=partial_x v, U[d]=(-partial_xy v,partial_xx v),
 c[d]=partial_xxy v(0)=1, J[d]=0.                       (3)

The function d belongs to X_s, with zero scalar input, and to the distributional maximal domain D_H(A0) of the actual moving-tail operator. Its images T d, Lren d and A0 d are in their stated high targets. In particular it is an admissible exact test direction in proof 181 or190. No norm upper bound, inverse estimate or violation of the quantitative closure condition is asserted.

## Polynomial factor and canonical velocity

Expand (1) at x=0. The definitions of a_g and b_g give the identities, as functions of y,

 v=g-(x^2/2)g''+(x^4/24)g''''+O(x^6).                  (4)

The constant and x^2 coefficients of Delta v vanish: respectively -g''+g''=0 and g''''/2-g''''/2=0. The function is even in x and odd in y, and every derivative is a polynomial with rational coefficients times exp(-r^2). Consequently the polynomial multiplying exp(-r^2) in -Delta v is divisible by x^4 and by y, proving (2). This is exact polynomial divisibility, not merely an asymptotic assertion. It also gives d=O(r^5) at the origin with every fixed cylinder derivative, and d/(x^2 y) has zero vertical-axis trace.

The proposed stream function satisfies -Delta(partial_x v)=partial_x d. Both it and its gradient are Schwartz. In Fourier variables, d_hat=|xi|^2 v_hat, so the canonical inverse Laplacian followed by partial_x gives exactly partial_x v, including its extension at zero frequency. No harmonic addition is made. The velocity formula in (3) follows from U=(-psi_y,psi_x).

From (4), v_xx(0,y)=-g''(y). Since g(y)=-y^3/6+O(y^5), g'''(0)=-1 and c[d]=-g'''(0)=1. Thus d is nonzero. Its O(r^5) vanishing gives J[d]=0. In particular c does not vanish on the kernel of J in the smooth high domain. No limiting strain integral or normalization completion is needed.

## High input and maximal-domain membership

By (2), the cylinder quotients d/b and d/(b p) are smooth. At the inner end they and all their cylinder derivatives are O(r^(5-24/5))=O(r^(1/5)). The second quotient has the factor cos(theta)^2 and hence zero trace at both vertical axes. At the outer end all quotients and every fixed cylinder derivative decay faster than any exponential in t. They therefore belong to every fixed cylinder Sobolev space. Multiplication by the fixed angular cutoff preserves these statements, and H^sigma embeds into the stated variable-order space. Thus d belongs to X_s, and its scalar input is exactly zero. This proves high input membership directly without using mere Schwartz regularity as a substitute for the singular-axis requirements.

Next T d belongs to X_s. At the vertical axis V1=x A(x,y), with A even in x, and V2 is even in x. These are the actual tangent parities. Acting on (2) with V.grad preserves the factor x^4 and physical odd-y parity. On compact annuli the actual normalized cylinder velocity and its divided tangent coefficients are C6 with bounded piecewise seventh weak derivatives, hence W^(7,infinity), by proof 126 and the canonical modal Green formulas. Their angular bandwidth is finite. Their compact localizations therefore belong to H^7. Multiplication by the smooth cylinder derivatives of d gives local H^(25/4) regularity for both the bulk and divided cofactor. It preserves the zero cofactor trace. At the inner end V is its central linear field plus O(r^3), with all fixed cylinder derivatives in the finite modal expansions. Thus T d still vanishes to physical order at least5. At the outer end V=ell0 X+O(r^k), with polynomial bounds for every fixed cylinder derivative, while d and its derivatives have Gaussian decay. The same inner and outer integrability proof applies. Hence T d belongs to X_s. This verifies membership in the exact distributional maximal transport domain, not only input membership.

The bounded high normalized coupling theorem of proof 123 maps d to Y_H. It has scalar row Gamma_C[d] in Gamma_H, and its axis-subtracted remainder is in X_s. Therefore Lren d=T d+U[d].grad rho0+c[d]H0 belongs to Y_H. Proof 167 proves m0 in Y_H, and A0d=Lren d+c[d]m0. Thus A0d belongs to Y_H and d is in the maximal high domain used by topics174 and181. These are unconditional membership facts; actual injectivity is not needed.

For a direct origin check, U[d]=(-x,y)+O(r^3), rho0=x^2y+O(r^5), and H0=x^2y+O(r^5). The cubic part of U[d].grad rho0 is -x^2y, which cancels c[d]H0 exactly. T d has no cubic term. This is why the high-target statement uses the normalized sum. Neither an individual target norm of M0 nor of the uncancelled coupling is used.

## A concrete finite target vector for the necessary scalar test

Put

 Q_d=T d+U[d].grad rho0+H0=Lren d.

Both Q_d and m0 are in Y_H by the preceding argument, and

 A0d=Q_d+m0,
 R_d=Q_d+m0-F0/(ell0 n'_0).                           (5)

The second vector is the residual-subtracted target of proof 190 because c[d]=1. The exact formulas (1)-(3) remove any numerical Poisson solve for this direction. Every remaining calculation still has to enclose the original modal background, the moving-tail column and the same fixed high norm, including its fractional and variable orders and its scalar axis term.

Under the hypotheses(I) and(S) of proof 174, proof 181 implies

 eta_*<=N4 ||Q_d+m0||Y_H,                            (6)

while proof 190 gives ||R_d||Y_H>1956082280. A rigorously checked upper bound violating either necessary inequality would rule out the conjunction(I),(S) in this chart. If(I) is separately assumed, it would refute(S). No such upper bound is supplied here. A small pointwise residual, a low norm, a floating quadrature or a norm in different equivalent units cannot decide (6).

## Dependencies and verification

The polynomial and Fourier identities above are independent of the modal data. A companion exact symbolic calculation will check (2)-(4), c=1 and the zero traces and export rational polynomial coefficients as JSON. This is an algebraic replay of the proof, not a norm certificate. The actual high-domain assertions use topics123,126,165 and167 with their previously checked coefficient regularity, and the necessary inequalities use topics174,177,181 and190. No large coefficient tables or Lean numeral files are generated. Independent independent review is requested before this new witness is adopted as a theorem in the team report.
