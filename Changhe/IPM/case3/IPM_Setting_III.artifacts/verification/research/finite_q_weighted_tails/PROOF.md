# Explicit weighted tail bounds for a finite smooth Q interpolant

Status: CONFIRMED. Independent informal proof preceded its checker, which passed at 21:00:58Z. Actual Claude Opus5.5 lead reviewed all bounds at 21:03Z. This is a statement about finite coefficient formulas, not a profile theorem.

## Statement and notation

Let L>0, kappa>1, ell>1 and let B_j be real polynomials for 0<=j<M, with B_j=0 for j>=M. Put

\[
 r=L2^{-\kappa}\sigma^{1/2}(1-\sigma)^{-\kappa},\qquad
 \rho=r(1-\sigma)\sin\theta
       \sum_{j=0}^{M-1}\sigma^j B_j(2\sigma-1)\cos(2j\theta).
\]

Here 0<=sigma<1 and the origin is defined by the smooth limiting formula. Its density exponent is 1-1/kappa in (0,1). Take the canonical full-plane inverse and write a=B_0(-1), c=psi_xy(0), h=rho-a y, phi=psi-cxy and v=U-(-cx,cy). For any ell, define

\[
 F=(\ell X+U)\cdot\nabla\rho-\rho-a(\ell+c-1)y.
\]

Let r_core=L2^{-kappa}, z=log(r/r_core). For 2<m<4, the integrals of h^2 and F^2 against r^{-2m}dX converge. The explicit constants below bound both tails after the common factor r_core^{4-2m} has been removed. All constants are computable from exact finite polynomial coefficients. For binary input coefficients, rational arithmetic computes the constants exactly, with rational upper bounds for the remaining exponential factors.

The result supplies analytic truncation bounds. It does not certify the numerical integration on the retained annulus, which needs its own error analysis.

## Dependencies

The canonical modal Green inverse and its uniqueness in the sublinear velocity class are proved in `../angular_log_inverse/PROOF.md` and the earlier canonical inverse proof. The angular logarithmic formulas (4), (7), (9) of the former proof are used below. The weighted center-defect equation is proved separately in `../weighted_center_defect/PROOF.md`. No exact transport equation is assumed here.

## Polynomial bounds

Write B_j(t)=sum_k b_jk T_k(t), and set

\[
 C_j=\sum_k|b_{jk}|,\qquad C'_j=\sum_k k^2|b_{jk}|.
\]

Both are zero for j>=M. On [-1,1], |B_j|<=C_j and |B'_j|<=C'_j, since |T_k|<=1 and |T'_k|<=k^2. The endpoint quotient

\[
 Q_0(t)=\frac{B_0(t)-B_0(-1)}{t+1}
\]

is a polynomial. Let C_Q be the sum of absolute Chebyshev coefficients of Q_0. This quotient is formed by exact polynomial division, without dropping a remainder or replacing the endpoint value by a rounded constraint.

Let h/r=sum_{j=0}^{M-1} h_j(z) sin((2j+1)theta). The coefficients are

\[
 h_0=\sigma[2(1-\sigma)Q_0-a-(1-\sigma)B_1/2],
 \qquad
 h_j=\tfrac12(1-\sigma)\sigma^j(B_j-\sigma B_{j+1}),\quad j\ge1.
\]

Define near-origin bounds

\[
 H_0=2C_Q+|a|+C_1/2,\qquad H_j=(C_j+C_{j+1})/2\quad(j\ge1),
\]

and global bounds

\[
 G_0=|a|+C_0+C_1/2,\qquad G_j=H_j\quad(j\ge1).
\]

All symbols are zero beyond j=M-1. Then |h_0|<=H_0 sigma, |h_j|<=H_j sigma^j for j>=1, and |h_j|<=G_j globally. Put

\[
 D_0=2C_0+4C'_0+C_1+2C'_1,
\]
\[
 D_j=(j+1)(C_j+C_{j+1})+2C'_j+C_{j+1}+2C'_{j+1},\quad j\ge1.
\]

Differentiating the displayed formulas, and using

\[
 \frac{d\sigma}{dz}=
 \frac{2\sigma(1-\sigma)}{1-\sigma+2\kappa\sigma}\le2\sigma,
\]

gives |dot h_0|<=D_0 sigma and |dot h_j|<=D_j sigma^j for j>=1. For j=0 one may differentiate the original coefficient
(1-sigma)(B_0-sigma B_1/2)-a: its sigma derivative is bounded by C_0+2C'_0+C_1/2+C'_1. This avoids differentiating the quotient numerically. The same D_j bound applies globally with sigma^j replaced by 1.

The coordinate relation z=(log sigma)/2-kappa log(1-sigma) implies sigma<=e^{2z}. Hence for z<=0,

\[
 |H|\le H_* e^{2z},\quad |\dot H|\le D_*e^{2z},\quad
 |H_\theta|\le H_\theta^*e^{2z},
\]

where H=h/r, H_*=sum H_j, D_*=sum D_j and H_theta^*=sum(2j+1)H_j. The analogous global bounds are G_*, D_*, G_theta^*.

## Bounds on the nonlocal velocity

Use n_j=2j+2 and the affine-subtracted Green coefficients A_j,B_j^G from the angular logarithmic inverse, reserving B_j for the input polynomial. Thus

\[
 P_j=\frac{B_j^G-A_j}{2},\qquad
 E_j=\frac{n_j(A_j+B_j^G)-h_j-h_{j+1}}2,
\]

and v_r/r=-sum n_j P_j cos(n_j theta), v_theta/r=sum E_j sin(n_j theta).

For z<=0, the lower integrals obey

\[
 |A_j(z)|\le A_j^*e^{2z},\qquad A_j^*=H_j/(n_j+4),
\]

because |h_j(z-u)|<=H_j e^{2(z-u)} for all u>=0. For j=0,

\[
 B_0^G(z)=-\int_{-\infty}^z h_1(t)dt,
 \qquad |B_0^G(z)|\le (H_1/2)e^{2z}.
\]

For j>=1, the upper integral has kernel e^{-2ju}. Since
|h_{j+1}(t)|<=H_{j+1}min(e^{2(j+1)t},1), split its integral at u=-z. This gives

\[
 |B_j^G(z)|\le H_{j+1}
 \left[\frac{e^{2jz}-e^{2(j+1)z}}2+\frac{e^{2jz}}{2j}\right]
 \le H_{j+1}\frac{j+1}{2j}e^{2z}.
\]

Set B_0^*=H_1/2, B_j^*=H_{j+1}(j+1)/(2j) for j>=1, and

\[
 V_r^*=\sum_j\frac{n_j(A_j^*+B_j^*)}{2},\qquad
 V_\theta^*=\sum_j\frac{n_j(A_j^*+B_j^*)+H_j+H_{j+1}}2.
\]

Then |v_r/r|<=V_r^*e^{2z} and |v_theta/r|<=V_theta^*e^{2z} for z<=0.

For global bounds, replace A_j^* by A_j^g=G_j/(n_j+2). Replace B_j^* for j>=1 by B_j^g=G_{j+1}/(n_j-2). The special n=2 primitive is

\[
 B_0^G(z)=-\int_0^\sigma
 \left(\frac{1-u}{4}+\frac{\kappa u}{2}\right)
 [B_1(2u-1)-u B_2(2u-1)]du.
\]

Therefore |B_0^G|<=B_0^g=(C_1+C_2)(1+2kappa)/8. Define V_r^g and V_theta^g by the same sums as above using A^g,B^g,G in place of A^*,B^*,H. These bound the velocity defect globally. Also

\[
 |c|\le c^g:=|a|/4+B_0^g
\]

by the canonical center formula. This bound needs no numerical evaluation of c.

## Bounds on the corrected residual

The exact identity, independent of whether the density is a profile, is

\[
 F/r=(\ell+U_r/r)(H+\dot H)+(U_\theta/r)H_\theta-H
       +a[(v_r/r)\sin\theta+(v_\theta/r)\cos\theta].
\]

The affine velocity has radial and angular components -c cos(2theta), c sin(2theta). Since e^{2z}<=1 for z<=0, the preceding bounds give |F/r|<=F_*e^{2z}, where

\[
 F_*=(\ell+c^g+V_r^*)(H_*+D_*)
       +(c^g+V_\theta^*)H_\theta^*+H_*+|a|(V_r^*+V_\theta^*).
\]

Globally |F/r|<=F_g, with

\[
 F_g=(\ell+c^g+V_r^g)(G_*+D_*)
       +(c^g+V_\theta^g)G_\theta^*+G_*+|a|(V_r^g+V_\theta^g).
\]

All factors are nonnegative exact expressions in coefficient bounds and parameters.

## Tail integrals and finite-window ratio bounds

After division by r_core^{4-2m}, the scalar norm of h on a log-radius interval is int e^{(4-2m)z}|H|^2 dz dtheta, and similarly for F/r. For z0<=0<=z1,

\[
 I_{h,-}\le\frac{2\pi H_*^2}{8-2m}e^{(8-2m)z_0},\qquad
 I_{F,-}\le\frac{2\pi F_*^2}{8-2m}e^{(8-2m)z_0},
\]
\[
 I_{h,+}\le\frac{2\pi G_*^2}{2m-4}e^{-(2m-4)z_1},\qquad
 I_{F,+}\le\frac{2\pi F_g^2}{2m-4}e^{-(2m-4)z_1}.
\]

This proves convergence for every 2<m<4. For a purely rational certificate, use 2pi<7 and e^{-t}<=2^{-floor(t)} for t>=0. At rational m,z0,z1 each displayed upper bound then has an exact rational enlargement. No radius or coefficient is converted to an enormous or tiny floating point field.

If I_h^A>0 and I_F^A are the exact annular integrals and T_h,T_F are the total tail bounds, the full-plane ratio satisfies

\[
 \sqrt{I_F^A/(I_h^A+T_h)}
 \le \|F\|_m/\|h\|_m
 \le \sqrt{(I_F^A+T_F)/I_h^A}.
\]

If annular quadrature gives certified lower and upper intervals, substitute their appropriate endpoints. Without such intervals, these expressions are diagnostics based on quadrature with proved tail control, not certified full-plane norm ratios. In particular a small center defect is still recorded separately: the uncorrected residual R has a divergent weighted norm whenever a(ell+c-1)!=0 and m>=2.
