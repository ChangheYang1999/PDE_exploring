# Renormalized energy, helicity and residual identities

## Scope and notation

All integrals below are Lebesgue integrals with physical volume or surface measure. The sphere has area4pi; its measure is not normalized. Let c in (2/5,1/2), omega in R, alpha=(1-c)/c and p=3-2alpha. Then1<alpha<3/2 and0<p<1. Let J be the constant skew matrix Jy=e_3 cross y. For U in C^2(R^3;R^3) with div U=0 and P in C^2(R^3), set

\[
 \Omega=\nabla\times U,\qquad W=cy-\omega Jy+U,
\]
\[
 R=(1-c)U+(W\cdot\nabla)U+\omega JU+\nabla P,
 \qquad R_\Omega=\nabla\times R.
\]

These are residuals of an arbitrary field. Neither small numerical residuals nor finite-dimensional coefficients imply R=0.

For r>0 write U_r(n)=U(rn). Suppose that for r>=R_b>0 there are F,H in L^2(S^2;R^3) and orthogonal maps Q_r in SO(3) such that

\[
 U^0_r(n)=r^{-\alpha}Q_r F(Q_r^{-1}n),\qquad
 \Omega^0_r(n)=r^{-\alpha-1}Q_r H(Q_r^{-1}n).
\]

Both fields use the same Q_r. This is the rotating homogeneous-tail hypothesis, stated explicitly; it is not inferred from sampled data. Put

\[
 A=\|F\|_{L^2(S^2)}^2,\quad B=\|H\|_{L^2(S^2)}^2,
 \quad K=\langle F,H\rangle_{L^2(S^2)}.
\]

Assume constants C_U,C_Omega>=0 and delta>p satisfy, for every r>=R_b,

\[
 \|U_r-U^0_r\|_2\le C_Ur^{-\alpha-\delta},\qquad
 \|\Omega_r-\Omega^0_r\|_2\le C_\Omega r^{-\alpha-1-\delta}.
\tag{1}
\]

The first bound suffices for the energy statements. The helicity expansion uses both. Each numerical use of the explicit remainder bounds must justify the constants and the universal quantifier in(1).

## 1. Existence and remainder of the energy finite part

Under the first bound in(1), the limit

\[
 E_{\rm ren}^{A}=\lim_{R\to\infty}
 \left(\int_{|y|<R}|U(y)|^2\,dy-\frac{A R^p}{p}\right)
\tag{2}
\]

exists and is finite. For every R>=R_b,

\[
 \left|E_{\rm ren}^{A}-\left(E(R)-\frac{AR^p}{p}\right)\right|
 \le \frac{2\sqrt A C_U}{\delta-p}R^{p-\delta}
     +\frac{C_U^2}{2\delta-p}R^{p-2\delta},
 \quad E(R)=\int_{|y|<R}|U|^2.
\tag{3}
\]

Proof. Rotation preserves the sphere measure and vector norm, so ||U^0_r||_2=sqrt(A)r^-alpha. Writing V_r=U_r-U^0_r, the identity

\[
 \|U_r\|_2^2-Ar^{-2\alpha}
   =2\langle U^0_r,V_r\rangle+\|V_r\|_2^2
\]

and Cauchy-Schwarz bound its absolute value by
2sqrt(A)C_U r^(-2alpha-delta)+C_U^2 r^(-2alpha-2delta).
By polar integration, E'(r)=r^2||U_r||_2^2. Therefore

\[
 |E'(r)-Ar^{p-1}|
 \le2\sqrt A C_Ur^{p-1-\delta}+C_U^2r^{p-1-2\delta}.
\]

Both powers are integrable at infinity because delta>p. Integrating from R to infinity proves the existence of(2) and bound(3).

If A is not exactly1, replacing A by1 in(2) adds (A-1)R^p/p. Since p>0, that limit cannot be finite unless A=1. A rounded or approximately normalized gauge must not silently be used as an exact one.

## 2. Helicity and its leading exterior contribution

The helicity

\[
 \mathcal H=\int_{\mathbb R^3}U\cdot\Omega\,dy
\]

is absolutely integrable under(1). For every R>=R_b,

\[
 \left|\mathcal H-\int_{|y|<R}U\cdot\Omega\,dy
       -\frac{KR^{2-2\alpha}}{2\alpha-2}\right|
 \le \frac{\sqrt A C_\Omega+\sqrt B C_U}{2\alpha+\delta-2}
          R^{2-2\alpha-\delta}
      +\frac{C_UC_\Omega}{2\alpha+2\delta-2}
          R^{2-2\alpha-2\delta}.
\tag{4}
\]

Proof. Rotations preserve the common inner product, so <U^0_r,Omega^0_r>=K r^(-2alpha-1). Expanding U=U^0+V and Omega=Omega^0+Z gives an error bounded by

\[
 (\sqrt A C_\Omega+\sqrt B C_U)r^{-2\alpha-1-\delta}
     +C_UC_\Omega r^{-2\alpha-1-2\delta}.
\]

Multiplication by r^2 and integration gives(4). Cauchy-Schwarz also bounds the sphere integral of |U.Omega| by ||U_r||_2||Omega_r||_2. Its leading radial power is r^(1-2alpha), which is integrable because alpha>1. On bounded balls continuity supplies integrability. This proves absolute convergence.

## 3. Exact finite-ball energy identity

For every R>0, without any tail hypothesis,

\[
 \int_{|y|<R}U\cdot R\,dy
 =\left(1-\frac52c\right)E(R)+\frac{cR}{2}E'(R)
   +\int_{|y|=R}\left(P+\frac12|U|^2\right)U\cdot n\,dS.
\tag{5}
\]

Proof. Let k=|U|^2/2. Skew symmetry gives U.JU=0, and div W=3c. Hence

\[
 U\cdot R=(1-c)|U|^2+W\cdot\nabla k+U\cdot\nabla P
 =\left(1-\frac52c\right)|U|^2+\nabla\cdot(Wk+PU).
\]

On the sphere, Jy.n=0 and W.n=cR+U.n. The divergence theorem and E'(R)=int_(|y|=R)|U|^2 dS yield(5).

Suppose in addition to(1) there are finite constants M_U,M_P with

\[
 |U(rn)|\le M_Ur^{-\alpha},\qquad
 |P(rn)|\le M_Pr^{-2\alpha}\quad(r\ge R_b,\ n\in S^2).
\tag{6}
\]

Then the nonlinear boundary term in(5) has absolute value at most
4pi(M_P+M_U^2/2)M_U R^(2-3alpha), which tends to zero. Moreover

\[
 1-\frac52c=-\frac{cp}{2}.
\]

The divergent terms in (1-5c/2)E(R)+(cR/2)E'(R) cancel exactly. Bound(3) and its derivative estimate imply

\[
 \lim_{R\to\infty}\int_{|y|<R}U\cdot R\,dy
   =\left(1-\frac52c\right)E_{\rm ren}^{A}.
\tag{7}
\]

This is an improper ball limit; absolute integrability of U.R has not been asserted. If R=0 identically and all stated hypotheses hold, then E_ren^A=0, since1-5c/2 is nonzero.

## 4. Exact helicity identity

For every R>0, without tail hypotheses,

\[
 \int_{|y|<R}(\Omega\cdot R+U\cdot R_\Omega)\,dy
 =(2-4c)\int_{|y|<R}U\cdot\Omega\,dy
 +\int_{|y|=R}\left[W(U\cdot\Omega)
                    +\Omega\left(P-\frac12|U|^2\right)\right]\cdot n\,dS.
\tag{8}
\]

Proof. The curl identity proved in ../vorticity_identity/PROOF.md gives

\[
 R_\Omega=\Omega+(W\cdot\nabla)\Omega-(\Omega\cdot\nabla)U+\omega J\Omega.
\]

Set h=U.Omega and k=|U|^2/2. On adding Omega.R and U.R_Omega, the rotation terms cancel, since Omega.JU+U.JOmega=0. The transport terms sum to W.grad h, and U.((Omega.grad)U)=Omega.grad k. Thus

\[
 \Omega\cdot R+U\cdot R_\Omega
 =(2-c)h+W\cdot\nabla h+\Omega\cdot\nabla(P-k)
 =(2-4c)h+\nabla\cdot[Wh+\Omega(P-k)],
\]

using div W=3c and div Omega=0. Integration proves(8). In particular the sign in the pressure flux is P-k, not P+k.

Assume(6) and additionally |Omega(rn)|<=M_Omega r^(-alpha-1). The linear part of the boundary flux is bounded in absolute value by4pi c M_U M_Omega R^(2-2alpha). The remaining parts are bounded by
4pi M_Omega(M_P+3M_U^2/2)R^(1-3alpha).
Both tend to zero. The rotation part of W has zero normal component. Consequently

\[
 \lim_{R\to\infty}\int_{|y|<R}(\Omega\cdot R+U\cdot R_\Omega)\,dy
 =(2-4c)\mathcal H.
\tag{9}
\]

If R=0 identically, then R_Omega=0 identically. Since2-4c>0, equation(9) implies \(\mathcal H=0\).

## Dependencies and limitations

The proof uses polar integration, Cauchy-Schwarz, the divergence theorem and the separately proved rotating vorticity identity. It does not establish the tail bounds, pressure decay, exact gauge, or zero residual of any saved numerical state. Equations(3) and(4) are rigorous error bounds only after their constants and hypotheses are established. Quadrature refinement and sampled decay can support numerical observations but cannot replace those hypotheses. This result has not been formalized.
