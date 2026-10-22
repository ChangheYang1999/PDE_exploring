# Moment-stable inverse and moving-hit derivatives for selected inputs

Written2026-10-21 before the new refinement evaluator. Exact identities below are proved; floating results remain diagnostics.

## 1. Scope and source class

Use the P210 active coefficient map at fixed beta>2, a0, lambda and native forcing. Write D=I-qq^T/(q^Tq) and d=Dv. The direction velocity is Z=V[xG_d], with the canonical once-subtracted whole-plane inverse; W_h=W_0+hZ. The two selected v are the saved matrix's weakest coefficient singular vector and its independently computed weakest physical-metric singular vector, normalized by the full-plane G norm of P205. This selection supplies test vectors, not continuum eigenfunctions.

The new computation changes only this lane's inverse evaluation and differentiation: it reuses P202's moment-stable base inverse, recomputes each direction by the same exact moment identity, and compares analytic moving-hit sensitivities with centered parameter differences. It does not reuse NUM code. The native sources are C4 or better, odd in x, and decay at infinity at the recorded algebraic rate. All inverse integrals extend over the plane.

## 2. The second-mode inverse identity

Set X=(r sin(phi),-r cos(phi)) and expand Omega=sum_{n>=1} H_n(r)sin(n phi). For n>=2 the canonical radial Green solution has

 Psi_n(r)/r = r/(2n) [A_n(r)+B_n(r)],
 partial_r Psi_n(r) = r/2 [-A_n(r)+B_n(r)],
 A_n(r)=integral_0^1 t^(n+1) H_n(rt) dt,
 B_n(r)=integral_1^infinity t^(1-n) H_n(rt) dt.

These formulas follow by solving -(Psi_n''+Psi_n'/r-n^2 Psi_n/r^2)=H_n with regularity at zero and no added exterior harmonic component, or by differentiating the integrals directly. The n=1 term uses the center-velocity subtraction as in P200; it is left unchanged here.

For n=2, substitute u=rt to get B_2(r)=integral_r^infinity H_2(u)du/u. Let M_2=integral_0^infinity H_2(u)du/u, which converges for these sources. Then

 B_2(r)=M_2-integral_0^r H_2(u)du/u.

This is exactly the same canonical inverse, with no added strain. For the native divided cosine basis, sin(phi)cos(k phi)=(sin((k+1)phi)-sin((k-1)phi))/2 for k>=1. Hence H_2(r)=r(a_1(r)-a_3(r))/2. Write t=1-(1+(r/L)^2)^(-1/(2b)), b=beta_basis. The odd cosine amplitudes are a_k=(1-t)^(b+1) [r/sqrt(r^2+L^2)] sum_j z_kj B_j(t). The radial identity

 (1-t)^(b+1) [r/sqrt(r^2+L^2)] dr/dt=bL

gives M_2=(bL/2) sum_j (z_1j-z_3j) integral_0^1 B_j(t)dt, with inactive coefficients omitted. A degree-d normalized B-spline integrates to (knot_(j+d+1)-knot_j)/(d+1). Therefore M_2=-2 c(z), agreeing with the independently derived center-strain functional. Exact rational arithmetic on the saved binary floating inputs evaluates this finite expression exactly for those inputs; converting that rational result to float is still rounded. A tiny residual moment of Dv is retained, not silently reset to zero.

## 3. Stream interpolation and regularity

Put s=log r and f_n(s)=Psi_n(r)/r. If p_n=Psi_n/r and d_n=partial_r Psi_n are node data, then f_s=d_n-p_n. The radial Poisson equation gives

 f_ss=(n^2-1)f-2 f_s-rH_n,
 f_sss=(n^2-1)f_s-2 f_ss-rH_n-r^2 H_n'.

The first identity follows by writing Psi=r f(log r) in the radial equation. Differentiating it with respect to s proves the second. A piecewise degree-seven Hermite polynomial matching f and its first three s derivatives at each node is C3 globally on the finite interpolation annulus. Its stream therefore gives a C2 velocity there. This is still an interpolated approximation of the exact inverse; C2 regularity alone supplies no interpolation-error enclosure. Node refinement and direct inverse values provide sampled controls.

## 4. Exact finite-time sensitivity formulas

Assume the C2 fields W_h depend smoothly on h and all tested backward trajectories hit |X|=delta transversely with W_0.n>0 on a common compact flow tube. At h=0 solve backward X'=-W_0(X), X(0)=Y, with hitting time T. The fixed-backward-time derivative p=partial_h X_h|_0 obeys

 p'=-DW_0(X)p-Z(X), p(0)=0.

At the hit S=X(T), set n=S/delta and F=W_0(S).n. Differentiating |X_h(T_h)|=delta yields n.(p(T)-W_0(S)T_h')=0, hence

 T_h'=n.p(T)/F, S_h'=p(T)-W_0(S)T_h', n_h'=S_h'/delta.

These signs use backward time. In particular n.S_h'=0 is an exact tangency control.

At the boundary set theta0=a0 S_x^2, v0=(2a0 S_x,0), N=(beta-2)theta0-W_0(S).v0, g0=v0+nN/F and omega0=4a0 S_x/beta. Differentiate these algebraic expressions using S_h', W_h(S_h)'=DW_0(S)S_h'+Z(S), and the quotient rule to obtain the initial sensitivity. The denominator F is nonzero by hypothesis.

Use a common forward variable tau in[0,1]. The trajectory point is X_h(T_h(1-tau)), whose derivative at fixed tau is p(T(1-tau))-W_0(X)(1-tau)T_h'. Let v=(g_x,g_y,omega) and

 A(X) = blockdiag((beta-2)I-DW_0(X)^T,-1), with A_(3,1)=1.

Then dv/dtau=T A v. Its derivative w=partial_h v obeys

 dw/dtau=T_h' A v+T(Aw+A_h'v),
 (A_h')_(1:2,1:2)=-(D(DW_0)(X)[X_h']+DZ(X))^T,

and the other derivative entries vanish. Differentiation under the finite-time ODE is valid for C2 velocity and smooth parameter dependence. Finally

 Theta(Y)=exp((beta-2)T)theta0,
 partial_h Theta=exp((beta-2)T)[(beta-2)T_h' theta0+theta0_h'].

These formulas give the derivative of the finite-cutoff scalar map. They are independently compared with parameter differences, which do not use this sensitivity system. No infinite backward-time limit is claimed.

## 5. Interpretation and controls

The refinement checks exact-moment/strain agreement, the derivative of native radial modes against an independent finite difference, moment inverse against Cartesian Duffy quadrature, coarse versus fine C2 stream grids, two small cutoff radii plus a larger cutoff, two ODE tolerances, and analytic sensitivities versus at least two parameter-difference steps. P202's manufactured parameter family is a dependency validating the same sensitivity implementation. All quadrature success flags and all discrepancies remain recorded.

A discrepancy between the physical value of J_h v and the independently reconstructed derivative can include the coefficient fit. Neither method supplies an error enclosure. The spread of a finite set of variants is not an upper bound on the true error. Thus even a discrepancy that persists under this refinement is evidence that those two sampled derivatives disagree, not a proof about an exact operator or a B2 profile.
