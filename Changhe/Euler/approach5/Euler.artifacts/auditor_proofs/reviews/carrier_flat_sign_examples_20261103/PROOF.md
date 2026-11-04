# Flat carrier fields with either sign of the stress trace

## 1. Statement and scope

Fix real parameters \(0<c<1/2\), \(\omega\in\mathbb R\), and \(0<\theta_0<\pi/2\). Let
\[
 Jx=e_3\times x,\quad A=cI-\omega J,\quad X=Ax,\quad
 L=(1-c)I+\omega J,\quad a=1-2c,\quad p=(1-c)/c>1.
\]
Derivatives use the convention \((DV)_{ij}=\partial_jV_i\), and matrix norms are Frobenius norms. Write \(D_s=\operatorname{sym}DV\), \(W=\operatorname{curl}V\) and \(k=X\cdot V\).

There are smooth fields \(V_+,V_-\) on the complement \(Z\) of the third coordinate axis, flat at every point of the cone \(\theta=\theta_0\), with
\[
 \operatorname{div}V_\pm=0,\qquad k=0,\qquad (DV_\pm)X=-LV_\pm,
 \qquad \nabla k=X\times W-aV_\pm.
\]
Each field is nonzero on precisely one side of that cone. On an explicit open neighborhood of the cone, \(\operatorname{tr}((DV_+)^2)\geq0\), and for the other field \(\operatorname{tr}((DV_-)^2)\leq0\). Both signs are strict on the respective nonzero side. In particular, near \(x_0=(\sin\theta_0,0,\cos\theta_0)\), the sharp constant in the pressure-free local unique-continuation theorem A2348 is \(\sqrt2\): at that constant its conclusion fails for every finite \(C_0\geq0\).

No pressure or auxiliary scalar is constructed. These are examples for the displayed equations alone, not examples in the full setting (F), and not smooth decaying whole-space Euler profiles. Smoothness here is only on \(Z\). The singular behavior at the origin and possible axis behavior are not removed.

## 2. Construction and all carrier identities

Let \(r=|x|\), \(\theta\in(0,\pi)\) and use the smooth orthonormal frame \((e_r,e_\theta,e_\phi)\) on \(Z\). An azimuth angle need not be globally selected: the frame vectors themselves are single-valued smooth functions on \(Z\). For any smooth \(g\) on \((0,\pi)\), set
\[
 m=(\omega/c)\sin\theta\,g,\qquad
 n={ (2-p)\omega\over c\sin\theta}\int_\theta^{\theta_0}\sin^2s\,g(s)\,ds,
 \qquad V_g=r^{-p}(me_r+ne_\theta+ge_\phi).
\]
The derivative matrix in this moving orthonormal frame is \(r^{-p-1}M\), where
\[
 M=\begin{pmatrix}
 -pm&m'-n&-g\\
 -pn&m+n'&-g\cot\theta\\
 -pg&g'&m+n\cot\theta
 \end{pmatrix}.
\]
Indeed the three directional derivatives are \(\partial_r\), \(r^{-1}\partial_\theta\) and \((r\sin\theta)^{-1}\partial_\phi\), applied also to the frame vectors. The frame identities are
\(\partial_\theta e_r=e_\theta\), \(\partial_\theta e_\theta=-e_r\), \(\partial_\theta e_\phi=0\),
\(\partial_\phi e_r=\sin\theta e_\phi\), \(\partial_\phi e_\theta=\cos\theta e_\phi\), and \(\partial_\phi e_\phi=-\sin\theta e_r-\cos\theta e_\theta\).

The defining integral gives
\[
 (\sin\theta n)'=-(2-p)m\sin\theta,\qquad n'=-(2-p)m-n\cot\theta.
\]
Taking the trace of \(M\) proves divergence zero. Since \(X=r(ce_r-\omega\sin\theta e_\phi)\), its scalar product with \(V_g\) is zero. Homogeneity gives \((x\cdot\nabla)V_g=-pV_g\), and rotation equivariance gives \(((Jx)\cdot\nabla)V_g=JV_g\). Combining them proves \((DV_g)X=-LV_g\).

For any such field, \(DV-(DV)^T\) acts on a vector \(y\) as \(W\times y\). Therefore
\[
 \nabla(X\cdot V)=A^TV+(DV)^TX=(A^T-L)V+X\times W=-aV+X\times W.
\]
All identities hold pointwise on \(Z\). In particular \(W\ne0\) wherever \(V_g\ne0\), since \(a>0\).

## 3. Flatness and the positive sign

Define \(G(t)=e^{-1/t}\) for \(t>0\), and \(G(t)=0\) for \(t\leq0\). This is smooth and flat at zero. For \(t>0\),
\[
 G'=G/t^2,\qquad \int_0^tG(s)\,ds=\int_0^ts^2G'(s)\,ds\leq t^2G(t).
\]
Set \(g_+(\theta)=G(\theta_0-\theta)\), \(g_-(\theta)=G(\theta-\theta_0)\) and \(V_\pm=V_{g_\pm}\). On the zero side of either \(g\), the whole integration interval defining \(n\) is also in the zero side. Thus \(V_+\) vanishes for \(\theta\geq\theta_0\) and \(V_-\) for \(\theta\leq\theta_0\). Continuity of every derivative across the cone shows infinite-order vanishing there. The azimuthal component is strictly positive on the other side, proving the stated nonvanishing.

An exact trace computation gives
\[
 \operatorname{tr}((DV)^2)=r^{-2p-2}T,
\]
\[
 T=p^2m^2+(m+n')^2+(m+n\cot\theta)^2+2pn^2+2pg^2
       -2pnm'-2\cot\theta\,gg'.
\]
Put \(q=|\omega|/c\) and \(\beta=|2-p|q/\sin(\theta_0/2)\). Choose \(0<\delta\leq\theta_0/2\) such that
\[
 \delta^2(1+\delta^2)p\beta q<\cot\theta_0.
\]
Such a choice exists for every fixed \(c,\omega,\theta_0\), including \(q=0\). On the positive field's nonzero side with \(t=\theta_0-\theta\in(0,\delta)\),
\[
 |n|\leq\beta t^2G(t),\quad |m'|\leq q(1+t^{-2})G(t),\quad
 g'=-G(t)/t^2,\quad\cot\theta\geq\cot\theta_0.
\]
All terms of \(T\) except the last two are nonnegative. Consequently
\[
 T\geq2G(t)^2\left({\cot\theta_0\over t^2}-p\beta q(1+t^2)\right)>0.
\]
On the other side and on the cone, \(DV_+=0\). This proves the nonnegative trace on \(\theta_0-\delta<\theta<\theta_0+\delta\).

## 4. The negative sign with explicit constants

Put
\[
 k_1=\cot\theta_0,\quad k_2=\cot((\theta_0+\pi/2)/2)>0,\quad
 \beta_1=|2-p|q/\sin\theta_0,
\]
\[
 C_1=p^2q^2+((p-1)q+k_1\beta_1)^2+(q+k_1\beta_1)^2
       +2p\beta_1^2+2p+4p\beta_1q>0,
\]
\[
 \delta_1=\min\{1,(\pi/2-\theta_0)/2,\sqrt{k_2/C_1}\}>0.
\]
For \(V_-\), on its nonzero side let \(t=\theta-\theta_0\in(0,\delta_1)\). Then \(k_2\leq\cot\theta\leq k_1\), \(g'=G/t^2\), and
\[
 |n|\leq\beta_1t^2G\leq\beta_1G,\qquad |m|\leq qG,
\]
\[
 |m+n'|\leq((p-1)q+k_1\beta_1)G,\quad
 |m+n\cot\theta|\leq(q+k_1\beta_1)G,\quad
 |2pnm'|\leq4p\beta_1qG^2.
\]
Applying these bounds to every term of the exact trace yields
\[
 T\leq(C_1-2k_2/t^2)G^2<0.
\]
The last inequality follows from \(t^2<\delta_1^2\leq k_2/C_1\). On the zero side and the cone all derivatives vanish. The claimed nonpositive sign therefore holds throughout the open neighborhood \(Z\cap\{|\theta-\theta_0|<\delta_1\}\). No condition on the sign or magnitude of \(\omega\) was imposed.

## 5. Sharpness, and a direct ratio check

For every real matrix \(DV\),
\[
 \operatorname{tr}((DV)^2)=|D_s|^2-|W|^2/2.
\]
The positive field thus satisfies \(|W|\leq\sqrt2|D_s|+C_0|V|\) for every \(C_0\geq0\), while it is flat at \(x_0\) and is nonzero in every neighborhood. This proves failure of the conclusion of A2348 at the endpoint, within exactly its pressure-free class. A2348 already supplies the strict side of the threshold.

For completeness the limiting ratio can also be checked directly without invoking unique continuation. Approach \(\theta_0\) along the nonzero side at fixed \(r=1\) and azimuth. Let \(q_0=\omega/c\) with its sign. The integral bound and the equation for \(n'\) imply \(n=O(t^2g)\), \(n'=O(g)\), while \(m'=q_0\sin\theta\,g'+O(g)\). Thus
\[
 M=g'v\otimes e_\theta+O(g),\qquad
 v=q_0\sin\theta\,e_r+e_\phi,\qquad v\perp e_\theta,\quad |v|\geq1.
\]
For this rank-one leading term the symmetric part has squared norm \((g')^2|v|^2/2\), and its curl has squared norm \((g')^2|v|^2\). Since \(|g/g'|=t^2\to0\), both examples satisfy
\[
 { |W|\over|D_s|}\longrightarrow\sqrt2,\qquad { |V|\over|D_s|}\longrightarrow0.
\]
The denominator is nonzero sufficiently near the cone on the nonzero side. For the positive field the first ratio stays strictly below \(\sqrt2\); for the negative field it stays above. These limits show directly that no finite \(C_0\) repairs a bound with a fixed coefficient \(\kappa<\sqrt2\) near the cone.

## 6. Dependencies and audit boundary

The constructive proof uses only the displayed spherical derivative formulas, the fundamental theorem of calculus and elementary estimates. The comparison with the full flat-point system uses its previously checked definition (A2127-A2132); A2348 supplies the strict unique-continuation theorem, and A2230-A2234 supply the exclusion of a nonpositive stress trace in that full system.

Both sign examples obey every equation from (F) that contains neither its scalar S nor its pressure P. An argument using only those equations and flatness of V cannot exclude either sign. An exclusion in (F) must therefore use an additional scalar or pressure property. In particular the negative example cannot be extended to the full hypotheses of the already proved nonpositive-trace exclusion. Whether a positive-trace example can satisfy all of (F), the common-flat-point obstruction itself, and global decaying-profile nonexistence remain open.

The entire C65 source, its supplementary checker and its output were read. Their exact bytes are registered in the team records. The proof above is independent of the numerical checks and requires no local computation or global characteristic completeness.
