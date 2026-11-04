# Exact infinite Fourier equations and their scope

## Statement

Let `U in C^2(R^3;R^3)` and `P in C^1(R^3)` solve the rotating profile equation, with finite real `c,omega` and `div U=0`. On `r>0`, write the cylindrical components as `u=(u_r,u_theta,u_z)`, and their angular Fourier coefficients as `u_m=(a_m,b_m,w_m)`. Write `p_m` for the pressure coefficients. Then the momentum, divergence, pressure, vorticity and mean equations in Sections 2-6 below hold for every integer mode, without truncation.

If additionally `c>0`, `c!=1/2`, and `U=o(|y|)` uniformly, the angular-momentum representation in Section 7 holds when `c<1/2`. If `omega!=0`, the exact periodic reformulation in Section 8 holds. No conclusion here makes the angular mean an unforced Euler profile or proves that a nonzero mode vanishes.

This is an independent audit of in the team records. Only the explicitly stated results below are confirmed. A general assertion that all invariant quantities are independent of omega would require further qualifications.

## 1. Cylindrical geometry and convergence

Let `R(theta)=exp(theta J)`. The Cartesian vector is `U=R(theta)u`. Consequently

\[
 (Jy\cdot\nabla)U-JU=R(\theta)\partial_\theta u.
\]

The rotation part of the equation is therefore `-omega partial_theta u`, with no extra component terms. The ordinary convective derivative contributes

\[
 ((U\cdot\nabla)U)_{\rm cyl}
 =u_r\partial_ru+\frac{u_\theta}{r}\partial_\theta u+u_z\partial_zu
       +\frac{u_\theta}{r}(-u_\theta,u_r,0).
\]

These identities follow by differentiating `e_r` and `e_theta`: `partial_theta e_r=e_theta` and `partial_theta e_theta=-e_r`.

On every compact subset of `r>0`, two angular derivatives of `u` are continuous and bounded. Thus its Fourier coefficients are locally uniformly `O((1+|m|)^-2)`, and its Fourier series converges absolutely and locally uniformly. First spatial derivatives have one continuous angular derivative. Products can either be defined directly by angular integration or by convolution: Cauchy-Schwarz and the angular `L^2` bounds show absolute convergence of each fixed convolution coefficient. These bounds are locally uniform. This also covers the quadratic pressure source, whose factors are first derivatives. No claim of absolute convergence of the series of second derivatives is necessary.

Although only `P in C^1` was assumed, the equation expresses `grad P` using `C^1` quantities, so `P` is in fact `C^2`. Pressure equations below can alternatively be interpreted distributionally before making this observation.

## 2. Momentum and divergence

Set `D=r partial_r+z partial_z` and, for a mode-l scalar `f_l`, define

\[
 T_{k,l}f_l=a_k\partial_rf_l+(il/r)b_kf_l+w_k\partial_zf_l.
\]

Taking angular coefficients of the preceding full-field identities gives

\[
\begin{aligned}
0={}&(1-c-im\omega)a_m+cDa_m+\partial_rp_m
       +\sum_{k+l=m}(T_{k,l}a_l-b_kb_l/r),\\
0={}&(1-c-im\omega)b_m+cDb_m+(im/r)p_m
       +\sum_{k+l=m}(T_{k,l}b_l+a_kb_l/r),\\
0={}&(1-c-im\omega)w_m+cDw_m+\partial_zp_m
       +\sum_{k+l=m}T_{k,l}w_l,\\
0={}&r^{-1}\partial_r(ra_m)+(im/r)b_m+\partial_zw_m.
\end{aligned}
\]

Reality is exactly `u_-m=conjugate(u_m)`, and likewise for pressure.

## 3. Pressure and vorticity

In the orthonormal cylindrical frame the mode coefficient of `DU` is

\[
 G_m=\begin{pmatrix}
 \partial_ra_m&(ima_m-b_m)/r&\partial_za_m\\
 \partial_rb_m&(imb_m+a_m)/r&\partial_zb_m\\
 \partial_rw_m&imw_m/r&\partial_zw_m
 \end{pmatrix}.
\]

Orthogonal change of frame preserves `tr((DU)^2)`. The already checked Poisson identity therefore gives

\[
 (\partial_r^2+r^{-1}\partial_r-m^2/r^2+\partial_z^2)p_m
       =-\sum_{k+l=m}\operatorname{tr}(G_kG_l).
\]

The curl coefficients are

\[
 \Omega_{r,m}=imw_m/r-\partial_zb_m,\quad
 \Omega_{\theta,m}=\partial_za_m-\partial_rw_m,\quad
 \Omega_{z,m}=r^{-1}\partial_r(rb_m)-ima_m/r.
\]

Neither of these local identities fixes harmonic pressure terms. Under the hypotheses of the canonical-pressure theorem A031, the gradient has no nonconstant harmonic ambiguity. Any statement that a pressure mode is absent must account for the additive constant in mode zero; the local Poisson equation alone does not suffice.

## 4. Axis regularity

If a scalar Cartesian field `f` is `C^k`, its Taylor polynomial in the horizontal variables at `(0,0,z)` contains only angular frequencies of magnitude at most its degree. The remainder is locally uniformly `o(r^k)` in `z`. Thus

\[
 f_m=O(r^{\min(|m|,k)}),\qquad f_m=o(r^k)\quad\hbox{if }|m|>k.
\]

Apply this to `U_1+iU_2=e^{i theta}(u_r+i u_theta)` and its counterpart with the minus sign. It gives

\[
 a_m+ib_m=O(r^{\min(|m+1|,2)}),\quad
 a_m-ib_m=O(r^{\min(|m-1|,2)}),\quad
 w_m=O(r^{\min(|m|,2)}).
\]

These are necessary conditions. They are not asserted to characterize all Cartesian `C^2` vector fields. In particular `O(r^{|m|})` for arbitrarily large modes would be unjustified with only two derivatives.

## 5. Angular momentum modes

Put `Gamma=r u_theta`. Multiplying the full theta momentum equation by `r` and using `B r=cr+u_r` gives

\[
 (1-2c)\Gamma+B\cdot\nabla\Gamma+\partial_\theta P=0.
\]

Thus `Gamma_m=r b_m` satisfies

\[
 (1-2c-im\omega)\Gamma_m+cD\Gamma_m+imp_m
        +\sum_{k+l=m}T_{k,l}\Gamma_l=0.
\]

## 6. The mean is forced

Let `a=a_0,b=b_0,w=w_0`; subtract these cylindrical means to define `u'`. Put `Q_ij=<u_i' u_j'>`, where brackets are the angular average. Parseval gives

\[
 Q_{ij}=\sum_{m\ne0}(u_i)_m(u_j)_{-m}
       =2\sum_{m\ge1}\operatorname{Re}((u_i)_m\overline{(u_j)_m}).
\]

Using `div U=0` to put convection in tensor-divergence form, and integrating angular derivatives over a full period, gives

\[
\begin{aligned}
(1-c)a+cDa+(a\partial_r+w\partial_z)a-b^2/r+\partial_rp_0
 &=-r^{-1}\partial_r(rQ_{rr})-\partial_zQ_{rz}+Q_{\theta\theta}/r,\\
(1-c)b+cDb+(a\partial_r+w\partial_z)b+ab/r
 &=-r^{-2}\partial_r(r^2Q_{r\theta})-\partial_zQ_{\theta z},\\
(1-c)w+cDw+(a\partial_r+w\partial_z)w+\partial_zp_0
 &=-r^{-1}\partial_r(rQ_{rz})-\partial_zQ_{zz},\\
r^{-1}\partial_r(ra)+\partial_zw&=0.
\end{aligned}
\]

Multiplying the second equation by `r` gives, with `Gamma_0=rb`,

\[
 (1-2c)\Gamma_0+(cD+a\partial_r+w\partial_z)\Gamma_0
 =-\operatorname{div}_{r,z}(rQ_{r\theta},rQ_{z\theta}),
\]

where `div_(r,z)(F,G)=r^-1 partial_r(rF)+partial_zG`.

The explicit rotation multiplier vanishes in mode zero. The Reynolds stresses need not vanish, and depend on all nonzero modes. Consequently a nonrotating or axisymmetric Liouville theorem cannot be applied to the mean by discarding this forcing.

## 7. Backward angular-momentum representation

Assume `0<c<1/2` and uniform sublinearity. The field `B` has a complete flow, and every backward orbit lies in a compact set, by A006. With `a_*=1-2c>0`, integrate

\[
 \frac{d}{ds}\big(e^{a_*s}\Gamma(\Phi_sx)\big)
       =-e^{a_*s}\partial_\theta P(\Phi_sx).
\]

Both `Gamma` and `partial_theta P=(Jy) dot grad P` are bounded on that compact orbit closure. The past endpoint term tends to zero and the integral converges absolutely. Therefore

\[
 \Gamma(x)=-\int_{-\infty}^0e^{(1-2c)s}
                          \partial_\theta P(\Phi_sx)\,ds.
\]

In particular an axisymmetric pressure forces `U_theta=0`. This does not by itself prove that the remaining components are axisymmetric or zero.

## 8. Exact periodic reformulation

Let `R_t=exp(omega t J)` and define

\[
 V(t,y)=R_tU(R_t^{-1}y),\qquad Q(t,y)=P(R_t^{-1}y).
\]

Direct differentiation gives

\[
 \partial_tV+(1-c)V+(cy+V)\cdot\nabla V+\nabla Q=0,
 \qquad \operatorname{div}V=0.
\]

When `omega!=0`, both fields have period `T=2pi/|omega|` (possibly nonminimal). If `y(t)` solves the similarity characteristic equation, then `eta(t)=R_t^-1 y(t)` satisfies `eta'=B(eta)`. At time `T`, `R_T=I`, so the characteristic period map is precisely `Phi_T^B`. Cylindrical mode m has time factor `exp(-im omega t)`.

A point of a nonconstant B-periodic orbit of minimal period `tau` is periodic for `Phi_T` exactly when `tau/T` is rational. This is only a description of the periodic points. It does not imply that almost every backward orbit converges to one. The conditional theorem A011 retains that extra dynamical hypothesis.

## Verification evidence and limitations

The spectral agent's in the team records and its saved log were inspected. They check exact symbolic identities for test modes 0,1,2 using Cartesian derivatives. The negative-control script deliberately reverses one geometric sign and one rotation sign. These are useful algebra checks, not an infinite-mode theorem. The arbitrary-mode calculation and convergence argument above supply the latter. No computation was rerun by this audit.
