# Homogeneous stationary Euler flows of degree $-\alpha$: nonexistence of nontrivial solutions with $C^1$ profiles for $0<\alpha<2$

**Status: SOLVED**

The conjecture of the task is true. For $1<\alpha<2$, every stationary incompressible Euler flow on $\mathbb R^3\setminus\{0\}$ of the form $u=r^{-\alpha}(v+f\omega)$, $p=r^{-2\alpha}P$ with $v,f,P\in C^2(S^2)$ is zero. No symmetry, Beltrami or ansatz assumption is made. The proof (Section 0) is short, and it works for every $0<\alpha<2$ and for profiles of class $C^1$. Its core is a minimum principle for the pressure profile, derived from the angular form of the pressure equation $-\Delta p=\operatorname{tr}\big((Du)^2\big)$: $P$ has no local minimum with a negative value. At points where $v\ne0$ this holds because, at a critical point of $P$, the momentum equation fixes the trace term. At stagnation points it holds because there the Hessian of $P$ is an explicit function of $Dv$. Hence $P\ge0$ on the sphere, and a nonnegative pressure forces the trivial solution. This last step is a known result of Shvydkoy; we also give a two-line argument for it. The range $0<\alpha<2$ is sharp: for every integer $\alpha\ne1$ there are nontrivial potential flows (in particular at $\alpha=0$ and $\alpha=2$), and Abe constructs further solutions for $\alpha>2$ and $\alpha<0$.

The minimum principle and the $C^2$ proof were first found by a second model, acting as referee. We checked them line by line and symbolically. The extension to $C^1$ profiles is ours, and the whole of Section 0 was then audited adversarially by the referee (Section 15). The sign lemma $H\ge0$ proposed in the task is correct (Theorem A, Section 4).

Part II (Sections 5 to 8) contains the results of the route through the Bernoulli function, which we followed before the pressure argument was found:

- a global stream function;
- the singular form $\theta=H^\gamma\eta$ and its defect;
- nonexistence for $C^4$ and real-analytic profiles.

These results answer the specific questions of the task. By Theorem 1, those that assume a nontrivial solution on $S^2$ concern an empty class, and those that prove triviality under an extra hypothesis are special cases of Theorem 1. Those stated for every $C^2$ solution on $S^2$, such as Theorem A and Proposition K, have proofs independent of Theorem 1. Some auxiliary lemmas, on scalar functions, closed forms and capacity (for instance Lemmas 8.4 and 8.6 and the remark after the proof of Theorem L), do not involve the Euler equations and keep independent content.

## 0. Main result

Throughout this section $0<\alpha<2$ (this contains the range $1<\alpha<2$ of the task). The spherical system (E1)-(E3) is derived from the three-dimensional Euler equations in Section 1. We write $Q=|v|^2$, $\nabla$, $\operatorname{div}$ and $\Delta=\operatorname{div}\nabla$ for the operators of the round unit sphere, and $A$ for the field of endomorphisms $A(X)=\nabla_Xv$ of the tangent planes, so that $\operatorname{tr}A=\operatorname{div}v$ and $\nabla_vv=A(v)$. Traces are traces of endomorphisms; in particular $\operatorname{tr}(A^2)$ is in general different from $|A|^2$. A *solution of class $C^k$ on an open set $O\subset S^2$* is a $C^k$ tangent vector field $v$ and functions $f,P\in C^k(O)$ satisfying (E1)-(E3) at every point of $O$.

**Theorem 1 (nonexistence).** Let $0<\alpha<2$. Every solution of (E1)-(E3) of class $C^1$ on $S^2$ is trivial: $v=0$, $f=0$, $P=0$. Equivalently, for $0<\alpha<2$ the only stationary incompressible Euler flow on $\mathbb R^3\setminus\{0\}$ of the form
$$u(r\omega)=r^{-\alpha}\big(v(\omega)+f(\omega)\omega\big),\qquad p(r\omega)=r^{-2\alpha}P(\omega),$$
with $v,f,P\in C^1(S^2)$, is $u=0$, $p=0$. In particular the conjecture of the task (stated there for $C^2$ profiles and $1<\alpha<2$) is true.

The heart of the proof is a minimum principle for the pressure, which is local.

**Theorem 2 (pressure minimum principle).** Let $0<\alpha<2$ and let $(v,f,P)$ be a solution of class $C^2$ on an open set $O\subset S^2$.

1. On $O$,
$$\Delta P=2\alpha P+\big((\alpha-1)^2+1\big)f^2-\operatorname{tr}(A^2). \tag{0.1}$$
2. If $z\in O$, $\nabla P(z)=0$ and $v(z)\ne0$, then $\Delta P(z)=2\alpha P(z)$.
3. If $z\in O$ and $v(z)=0$, then $\nabla P(z)=0$, $P(z)=-\frac12f(z)^2$ and
$$\nabla^2P(z)=f(z)A(z)+\det A(z)\,\mathrm{Id}, \tag{0.2}$$
where $\nabla^2P(z)$ is the Hessian, viewed as the self-adjoint endomorphism $X\mapsto\nabla_X\nabla P$. If moreover $f(z)\ne0$, then $A(z)$ is self-adjoint and $\Delta P(z)\le\frac{\alpha(\alpha-2)}{2}f(z)^2<0$.
4. $P$ has no local minimum in $O$ at which its value is negative.

Item 4 also holds for solutions of class $C^1$ on $O$ (Lemma 0.2 and Proposition 0.3 below).

**Corollary 3 (disks bounded by periodic orbits).** Let $0<\alpha<2$, let $(v,f,P)$ be a solution of class $C^2$ on an open set $O\subset S^2$, and let $\Gamma\subset O$ be a nonconstant periodic orbit of $v$ that bounds an open disk $D$ with $\overline D\subset O$. Then $\min_{\overline D}P<0$, the minimum is attained only at points of $\Gamma$, and at each such point the geodesic curvature of $\Gamma$ toward $D$ is negative: $\langle\nabla_\tau\tau,n\rangle<0$, where $\tau=v/|v|$ and $n$ is the unit normal of $\Gamma$ pointing into $D$.

*Remarks.*

- The range $0<\alpha<2$ is sharp for Theorem 1 at both ends. For $\alpha=2$, $v=0$, $f=c\ne0$, $P=-c^2/2$ is a nontrivial analytic solution ($u=c\,x/|x|^3$, the point source); there $\nabla^2P=0$ and the bound in item 3 becomes the equality $\frac{\alpha(\alpha-2)}2f^2=0$. For $\alpha=0$, constant flows $u=e$ give nontrivial solutions with $P=0$. For $\alpha<0$ the minimum principle can fail: for $\alpha=-1$, the linear strain $u=(x_1,2x_2,-3x_3)$, $p=-\frac12(x_1^2+4x_2^2+9x_3^2)$ has a negative pressure minimum $-\frac92$ at the stagnation points $\pm e_3$ of $v$, where $f=-3$ and $\frac{\alpha(\alpha-2)}{2}f^2>0$. Abe (Section 2) constructs nontrivial homogeneous solutions for $\alpha>2$ (with $u,p$ of class $C^1$ away from the origin) and for $\alpha<0$ (continuous on $\mathbb R^3$), which is consistent with Theorem 1.
- Theorem 2 is local, but Theorem 1 needs the closed sphere: the swirl flows $v=a\sin^{-\alpha}\!\vartheta\,e_\varphi$, $f=0$, $P=-a^2/(2\alpha\sin^{2\alpha}\vartheta)$ ($\vartheta$ the polar angle, $a\ne0$ a constant) are smooth solutions on the sphere minus the two poles, with $P<0$ everywhere; their pressure has no minimum, as it tends to $-\infty$ at the poles. Corollary 3 records what the minimum principle gives on a disk bounded by a periodic orbit, where no boundary condition on $P$ is available.
- The final step of the proof below, $P\ge0\Rightarrow$ trivial, is Corollary 4.4 of Shvydkoy (Section 2), proved there by a Riccati argument along orbits; we give a two-line argument. For $1<\alpha<2$ there is a third: integrating $\operatorname{div}(fv)=Q+2(\alpha-1)f^2+2\alpha P$ (a consequence of (E1), (E2)) over $S^2$ gives $\int(Q+2(\alpha-1)f^2+2\alpha P)\,dS=0$ with a nonnegative integrand.
- Theorem 1 makes the statements about nontrivial solutions in the rest of this report (most of Theorems B-N) vacuous; see the preamble of Part II for what keeps independent content.

### 0.1 The pressure equation

**Lemma 0.1.** For every $C^2$ tangent vector field $v$ on an open subset of the round unit sphere,
$$\operatorname{div}(\nabla_vv)=\operatorname{tr}(A^2)+v(\operatorname{div}v)+Q. \tag{0.3}$$

*Proof.* In local coordinates, with $A^i{}_j=\nabla_jv^i$,
$$\nabla_i(v^j\nabla_jv^i)=(\nabla_iv^j)(\nabla_jv^i)+v^j\nabla_i\nabla_jv^i,\qquad \nabla_i\nabla_jv^i=\nabla_j\nabla_iv^i+R_{kj}v^k,$$
by the Ricci identity. The first term is $A^j{}_iA^i{}_j=\operatorname{tr}(A^2)$, and $v^j\nabla_j\nabla_iv^i=v(\operatorname{div}v)$. On the unit sphere the Ricci tensor is the metric, so $R_{kj}v^kv^j=Q$. $\square$

(As a check of the curvature sign: for the unit field $e_\varphi$ away from the poles, $\nabla_{e_\varphi}e_\varphi=-\cot\vartheta\,e_\vartheta$, whose divergence is $1$, while $\operatorname{div}e_\varphi=0$ and $\operatorname{tr}(A^2)=0$.)

*Proof of Theorem 2.1.* Take the divergence of (E3), $\nabla P=-\nabla_vv+(\alpha-1)fv$, which is a $C^1$ field. By (E1), $\operatorname{div}(fv)=v(f)+f\operatorname{div}v=v(f)-(2-\alpha)f^2$ and $v(\operatorname{div}v)=-(2-\alpha)v(f)$. With (0.3),
$$\Delta P=-\operatorname{tr}(A^2)+(2-\alpha)v(f)-Q+(\alpha-1)\big(v(f)-(2-\alpha)f^2\big)=-\operatorname{tr}(A^2)+v(f)-Q-(\alpha-1)(2-\alpha)f^2 .$$
By (E2), $v(f)-Q=\alpha f^2+2\alpha P$, and $\alpha-(\alpha-1)(2-\alpha)=(\alpha-1)^2+1$. $\square$

Formula (0.1) is the angular form of the classical pressure equation $-\Delta p=\operatorname{tr}\big((Du)^2\big)$ of the Euler equations, but the proof above uses only (E1)-(E3). It was also checked symbolically (Section 15): for arbitrary $C^2$ data $v,f,P$ and symbolic $\alpha$, the difference of the two sides of (0.1) equals $\operatorname{div}R_3-v(R_1)+(\alpha-1)fR_1+R_2$, where $R_1,R_2,R_3$ are the residuals of (E1), (E2), (E3).

### 0.2 Critical points of the pressure

*Proof of Theorem 2.2.* At $z$, (E3) gives $A(v)=\nabla_vv=(\alpha-1)fv$. Let $e_1=v/|v|$ and let $e_2$ complete an orthonormal basis of $T_zS^2$. Then $Ae_1=(\alpha-1)fe_1$, and since $\operatorname{tr}A=-(2-\alpha)f$ by (E1), $\langle Ae_2,e_2\rangle=-f$. In this basis
$$A=\begin{pmatrix}(\alpha-1)f&b\\0&-f\end{pmatrix}$$
for some $b$, so $A^2$ is upper triangular with diagonal entries $(\alpha-1)^2f^2$ and $f^2$, and $\operatorname{tr}(A^2)=((\alpha-1)^2+1)f^2$. Substituting in (0.1) gives $\Delta P(z)=2\alpha P(z)$. No symmetry of $A$ is used; $b$ does not enter. $\square$

*Proof of Theorem 2.3.* At $z$, (E2) reads $0=\alpha f^2+2\alpha P$, so $P(z)=-\frac12f(z)^2$ because $\alpha\ne0$, and (E3) gives $\nabla P(z)=0$. Differentiate the $C^1$ field $\nabla P=-A(v)+(\alpha-1)fv$ at $z$ in the direction $X$:
$$\nabla_X\big(A(v)\big)=(\nabla_XA)(v)+A(\nabla_Xv)=A(AX),\qquad \nabla_X(fv)=X(f)\,v+fAX=fAX\qquad\text{at }z,$$
because $v(z)=0$. Hence $\nabla^2P(z)=-A^2+(\alpha-1)fA$. The Cayley-Hamilton identity $A^2-(\operatorname{tr}A)A+(\det A)\mathrm{Id}=0$ with $\operatorname{tr}A=(\alpha-2)f$ turns this into (0.2). The Hessian of a $C^2$ function is self-adjoint, and so is $\det A\,\mathrm{Id}$; hence $f(A-A^*)=0$, and $A$ is self-adjoint if $f(z)\ne0$. Then $A$ has real eigenvalues $\lambda_1,\lambda_2$ with $\lambda_1+\lambda_2=(\alpha-2)f$, so $\det A=\lambda_1\lambda_2\le\frac14(\alpha-2)^2f^2$, and
$$\Delta P(z)=\operatorname{tr}\nabla^2P(z)=f\operatorname{tr}A+2\det A\le(\alpha-2)f^2+\tfrac12(\alpha-2)^2f^2=\tfrac12\alpha(\alpha-2)f^2<0. \qquad\square$$

*Proof of Theorem 2.4.* Let $z\in O$ be a local minimum of $P$ with $P(z)<0$. Then $\nabla P(z)=0$ and $\nabla^2P(z)\ge0$, so $\Delta P(z)\ge0$. If $v(z)\ne0$, item 2 gives $\Delta P(z)=2\alpha P(z)<0$. If $v(z)=0$, item 3 gives $f(z)^2=-2P(z)>0$ and then $\Delta P(z)<0$. Both cases are contradictory. $\square$

### 0.3 Proof of Theorem 1 and of Corollary 3

*Proof of Theorem 1 for solutions of class $C^2$.* The continuous function $P$ attains its minimum on $S^2$ at some point, which is a local minimum, so by Theorem 2.4 the minimum is nonnegative: $P\ge0$ on $S^2$. Next, $f^2$ attains its maximum at some point $y$. If $f(y)\ne0$, then $2f(y)\nabla f(y)=\nabla(f^2)(y)=0$ gives $\nabla f(y)=0$, and (E2) at $y$ gives
$$0=v(f)(y)=Q(y)+\alpha f(y)^2+2\alpha P(y)\ge\alpha f(y)^2>0,$$
a contradiction. Hence $f\equiv0$. Then (E2) says $Q+2\alpha P=0$, a sum of two nonnegative functions, so $v=0$ and $P=0$. $\square$

*Proof of Corollary 3.* Let $\tau_0>0$ be the period of $\Gamma$ and $x(t)$ a parametrization by the flow of $v$. Since $\frac{d}{dt}f(x(t))=v(f)(x(t))$, integrating (E2) over a period gives
$$\int_0^{\tau_0}P(x(t))\,dt=-\frac1{2\alpha}\int_0^{\tau_0}Q(x(t))\,dt-\frac12\int_0^{\tau_0}f(x(t))^2\,dt<0,$$
because $Q>0$ on a nonconstant orbit. So $\min_{\overline D}P<0$. A point of $D$ where the minimum is attained would be a local minimum of $P$ in $O$ with negative value, which Theorem 2.4 excludes. Let $z\in\Gamma$ be a minimum point. $\Gamma$ is a $C^2$ embedded curve (an orbit of a $C^2$ field), so the geodesic $c(s)=\exp_z(sn)$ lies in $D$ for small $s>0$. Since $P|_\Gamma$ is minimal at $z$, $\tau(P)(z)=0$; since $P(c(s))\ge P(z)$ for small $s\ge0$, $n(P)(z)\ge0$. Along $\Gamma$, $v=|v|\tau$, so $\nabla_vv=v(|v|)\tau+Q\nabla_\tau\tau$ and $\langle\nabla_vv,n\rangle=Q\kappa$ with $\kappa=\langle\nabla_\tau\tau,n\rangle$. The $n$-component of (E3) is therefore $Q\kappa+n(P)=0$, so $\kappa(z)=-n(P)(z)/Q(z)\le0$. Suppose $\kappa(z)=0$. Then $\nabla P(z)=0$, and Theorem 2.2 gives $\Delta P(z)=2\alpha P(z)<0$. On the other hand, if $\sigma$ is an arc-length parametrization of $\Gamma$ with $\sigma(0)=z$, then $(P\circ\sigma)''(0)=\nabla^2P(z)(\tau,\tau)+\langle\nabla P(z),\nabla_\tau\tau\rangle=\nabla^2P(z)(\tau,\tau)$, which is $\ge0$ because $P\circ\sigma$ has a minimum at $0$. Also $P(c(s))-P(z)=\frac12s^2\nabla^2P(z)(n,n)+o(s^2)\ge0$ for small $s>0$, because $(P\circ c)'(0)=0$ and $c$ is a geodesic; so $\nabla^2P(z)(n,n)\ge0$. Hence $\Delta P(z)=\nabla^2P(z)(\tau,\tau)+\nabla^2P(z)(n,n)\ge0$, a contradiction. So $\kappa(z)<0$. $\square$

### 0.4 Solutions of class $C^1$

For a $C^1$ solution the pressure is only $C^1$, and (0.1) and (0.2) have to be read in a weaker sense. Note that for $C^1$ data (E3) requires $P\in C^1$, and (E2) then holds pointwise with continuous terms.

**Lemma 0.2.** Let $(v,f,P)$ be a solution of class $C^1$ on an open set $O\subset S^2$. Then (0.1) holds in the sense of distributions on $O$: with $g=2\alpha P+((\alpha-1)^2+1)f^2-\operatorname{tr}(A^2)\in C^0(O)$,
$$\int_{O}P\,\Delta\varphi\,dS=\int_{O}g\,\varphi\,dS\qquad\text{for all }\varphi\in C^\infty_c(O).$$

*Proof.* First, for every $C^1$ tangent field $w$ on $S^2$, with $B=\nabla w$,
$$\int\langle\nabla_ww,\nabla\varphi\rangle\,dS=-\int\big(\operatorname{tr}(B^2)+|w|^2\big)\varphi\,dS+\int(\operatorname{div}w)\big(w(\varphi)+\varphi\operatorname{div}w\big)\,dS. \tag{0.4}$$
For smooth $w$ this follows from (0.3): the left side is $-\int\operatorname{div}(\nabla_ww)\varphi$, and $-\int w(\operatorname{div}w)\varphi=\int(\operatorname{div}w)\operatorname{div}(\varphi w)$. Both sides of (0.4) are continuous with respect to $C^1$ convergence of $w$, and smooth fields are dense in $C^1$ fields (by smoothing in charts and a partition of unity), so (0.4) holds for $C^1$ fields on $S^2$. Given $\varphi\in C^\infty_c(O)$, choose $\chi\in C^\infty_c(O)$ with $\chi=1$ on a neighbourhood of $\operatorname{supp}\varphi$, and apply (0.4) to the $C^1$ field $w=\chi v$, extended by zero to $S^2$. Every integrand in (0.4) carries a factor $\varphi$ or $\nabla\varphi$, and near $\operatorname{supp}\varphi$ one has $w=v$ and $\nabla w=\nabla v$; so (0.4) holds with $w$ replaced by $v$ and the integrals taken over $O$. All integrations by parts below are against functions with compact support in $O$. Since $\operatorname{div}v=(\alpha-2)f$ and $fv\in C^1$, $\int f\,v(\varphi)=-\int\varphi\operatorname{div}(fv)=-\int\varphi\,(v(f)+(\alpha-2)f^2)$, and the last term of (0.4) equals $(\alpha-2)\int f\,(v(\varphi)+(\alpha-2)f\varphi)=-(\alpha-2)\int\varphi\,v(f)$. Since $P\in C^1$, (E3) gives
$$\int P\Delta\varphi=-\int\langle\nabla P,\nabla\varphi\rangle=\int\langle\nabla_vv,\nabla\varphi\rangle+(1-\alpha)\int f\,v(\varphi)=\int\varphi\Big(-\operatorname{tr}(A^2)-Q+v(f)+(\alpha-1)(\alpha-2)f^2\Big),$$
and (E2) turns the bracket into $g$, exactly as in the proof of Theorem 2.1. $\square$

**Proposition 0.3.** Theorem 2.4 holds for solutions of class $C^1$ on an open set $O\subset S^2$. Consequently Theorem 1 holds for solutions of class $C^1$.

*Proof.* Let $z\in O$ be a local minimum of $P$ with $P(z)<0$. Then $\nabla P(z)=0$. Both cases below take place in a small disk around $z$ contained in $O$.

*Case $v(z)\ne0$.* The algebra in the proof of Theorem 2.2 uses only $A(z)$ and (E1)-(E3) at $z$, so $g(z)=2\alpha P(z)<0$, where $g$ is the continuous function of Lemma 0.2. Take isothermal coordinates $x$ centred at $z$ (for instance stereographic coordinates), in which the metric is $e^{2\lambda}|dx|^2$ and $\Delta=e^{-2\lambda}\Delta_0$, $\Delta_0$ the flat Laplacian. By Lemma 0.2 (with test functions supported in the chart, which we take inside $O$), $\Delta_0P=h:=e^{2\lambda}g$ in the sense of distributions, and $h\le-c<0$ on a disk $\{|x|<\rho\}$. For a mollifier $\rho_\varepsilon$, $P_\varepsilon=P*\rho_\varepsilon$ is smooth on $\{|x|<\rho/2\}$ for small $\varepsilon$, with $\Delta_0P_\varepsilon=h*\rho_\varepsilon\le-c$ there. For a $C^2$ function $w$ with $\Delta_0w\le-c$ on $\{|x|<\rho/2\}$, the circle mean $m_w(r)=\frac1{2\pi}\int_0^{2\pi}w(re^{i\phi})\,d\phi$ satisfies $m_w'(r)=\frac1{2\pi r}\int_{|x|<r}\Delta_0w\,dx\le-\frac{cr}2$, hence $m_w(r)\le w(0)-\frac{cr^2}4$. Apply this to $P_\varepsilon$ and let $\varepsilon\to0$ (uniform convergence): $m_P(r)\le P(z)-\frac{cr^2}4<P(z)$ for $0<r<\rho/2$. This contradicts $P\ge P(z)$ near $z$.

*Case $v(z)=0$.* Then $f(z)^2=-2P(z)>0$ by (E2). Take normal coordinates $x$ centred at $z$, so that $g_{ij}(x)=\delta_{ij}+O(|x|^2)$ and the Christoffel symbols vanish at $0$. Since $v\in C^1$ and $v(0)=0$, $v(x)=A_0x+o(|x|)$ with $A_0=A(z)$ (the coordinate matrix of $A$ at $z$, which is also its matrix in an orthonormal basis); and $A(x)\to A_0$. Hence, by (E3),
$$\nabla P(x)=-A(x)v(x)+(\alpha-1)f(x)v(x)=Lx+o(|x|),\qquad L=-A_0^2+(\alpha-1)f(z)A_0=f(z)A_0+\det A_0\,\mathrm{Id},$$
the last equality by Cayley-Hamilton as before. Lowering the index with $g_{ij}=\delta_{ij}+O(|x|^2)$, the coordinate differential of $P$ is $dP=\sum_{j,m}L_{jm}x^m\,dx^j+\epsilon(x)$ with $|\epsilon(x)|=o(|x|)$. The form $dP$ is exact, so its integral over the circle $\{|x|=r\}$ vanishes, while the integral of the linear part is $\pm(L_{21}-L_{12})\pi r^2$ by Stokes' theorem, and that of $\epsilon$ is $o(r^2)$. Hence $L$ is symmetric. Since $f(z)\ne0$ and $L=f(z)A_0+\det A_0\,\mathrm{Id}$, $A_0$ is symmetric, and as in the proof of Theorem 2.3, $\operatorname{tr}L\le\frac12\alpha(\alpha-2)f(z)^2<0$. Finally $P(x)-P(z)=\int_0^1dP(sx)[x]\,ds=\frac12x^{\mathsf T}Lx+o(|x|^2)$, so a local minimum at $z$ forces $e^{\mathsf T}Le\ge0$ for every unit vector $e$, hence $\operatorname{tr}L\ge0$, a contradiction.

The proof of Theorem 1 given above uses only that $P$ has a nonnegative minimum, that $\nabla f=0$ at a maximum of $f^2$ where $f\ne0$, and (E2); all of this is available for $C^1$ solutions. $\square$

### 0.5 What the rest of the report contains

Section 1 derives (E1)-(E3) from the Euler equations and checks the sign conventions. Section 2 is the literature baseline. Sections 3 and 4 contain the preliminary identities and the sign lemma $H\ge0$ requested in the task (Theorem A); the lemma is correct, and Theorem 1 makes it a statement about the zero solution (by Theorem 2.4 and $P\ge0$ one also has $H=Q+f^2+2P\ge0$ directly). Part II (a list of statements followed by Sections 5-8) collects the results of the route through the Bernoulli function, the stream function and the singular form $\theta=H^\gamma\eta$, which we developed before the pressure argument was found. They answer the specific questions of Sections 4-6 of the task; by Theorem 1, those that assume a nontrivial solution are statements about an empty class (the preamble of Part II lists the exceptions). Sections 9-15 contain the list of verified statements, the scope of the result, tests, literature provenance, the recommended next step, and the verification record.

## 1. Setting and verification of the reduced system

Let $\omega\in S^2$ denote the position on the unit sphere and $\nabla,\operatorname{div},\Delta$ the spherical operators. $\langle\cdot,\cdot\rangle$ is the round metric, $dS$ the area measure, and $\mu$ the area form oriented by the outward normal. $JX=\omega\times X$ is rotation by $+\pi/2$ in the tangent plane, so $\mu(X,JX)=|X|^2$ and $\mu(X,Y)=\langle JX,Y\rangle$. $v^\flat$ is the 1-form dual to $v$, so $(Jv)^\flat=\iota_v\mu$. The scalar vorticity $\zeta$ is defined by $dv^\flat=\zeta\mu$ (it is of class $C^1$ when $v\in C^2$, and continuous when $v\in C^1$), and $Q=|v|^2$. Distances $d(\cdot,\cdot)$ are geodesic.

For $u(r\omega)=r^{-\alpha}(v(\omega)+f(\omega)\omega)$ and $p(r\omega)=r^{-2\alpha}P(\omega)$ one has $u\cdot\nabla=r^{-\alpha}\big(f\,\partial_r+r^{-1}D_v\big)$, where $D_v$ is the ambient derivative along the tangent vector $v$ acting on the angular dependence. Using $D_vv=\nabla_vv-|v|^2\omega$ (with $\nabla_v$ the Levi-Civita derivative of $S^2$) and $D_v(f\omega)=(v\cdot\nabla f)\omega+fv$, one finds
$$(u\cdot\nabla)u=r^{-2\alpha-1}\Big[\nabla_vv+(1-\alpha)fv+\big(v\cdot\nabla f-|v|^2-\alpha f^2\big)\omega\Big],\qquad \nabla p=r^{-2\alpha-1}\big(\nabla P-2\alpha P\omega\big),$$
$$\operatorname{div}u=r^{-\alpha-1}\big((2-\alpha)f+\operatorname{div}v\big).$$
Hence stationary Euler on $\mathbb R^3\setminus\{0\}$ is equivalent to
$$\text{(E1)}\ \ (2-\alpha)f+\operatorname{div}v=0,\qquad \text{(E2)}\ \ v\cdot\nabla f=|v|^2+\alpha f^2+2\alpha P,\qquad \text{(E3)}\ \ \nabla_vv+(1-\alpha)fv+\nabla P=0,$$
which is the system of the task and of Shvydkoy's paper, equations (3a)-(3c). Eliminating $P=\frac12(H-Q-f^2)$ from (E2) gives
$$\text{(T2)}\qquad v\cdot\nabla f=\alpha H+(1-\alpha)Q .$$
Taking the inner product of (E3) with $v$ gives $v\cdot\nabla P=-\tfrac12v\cdot\nabla Q-(1-\alpha)fQ$, hence
$$\text{(T1)}\qquad v\cdot\nabla H=v\cdot\nabla Q+2f\,v\cdot\nabla f+2v\cdot\nabla P=2\alpha fH .$$
These equations were also checked symbolically: the full Cartesian Euler equations for the ansatz were computed in spherical coordinates and reduced to (E1)-(E3), and (T1), (T2) were verified modulo (E1)-(E3) (Section 15). For the $C^2$ solutions of Sections 3 to 8 we use the regularity $H\in C^2$, $\zeta\in C^1$, $\eta=(1-\alpha)v^\flat-df\in C^1$ throughout.

**Notation for Sections 3 to 8.** From Section 3 on, unless stated otherwise, $1<\alpha<2$ and $(v,f,P)$ is a solution of (E1)-(E3) with $v$ a $C^2$ tangent vector field on $S^2$ and $f,P\in C^2(S^2)$. We write $H=|v|^2+f^2+2P\in C^2(S^2)$,
$$\beta=\frac{2-\alpha}{2\alpha}\in\Big(0,\frac12\Big),\qquad \gamma=\frac{1-\alpha}{2\alpha}\in\Big(-\frac14,0\Big),\qquad |\gamma|=\frac{\alpha-1}{2\alpha},\qquad 1+\beta+\gamma=\frac{3}{2\alpha},$$
$$Z=\{H=0\},\qquad U=\{H>0\},\qquad S=\{v=0\},\qquad Z_0=\{z\in Z:\ D^2H(z)=0\}.$$
(After Theorem A, every point of $Z$ is a minimum of $H$, so $\nabla H=0$ on $Z$ and the Hessian $D^2H(z)$ at $z\in Z$ is intrinsically defined.) The solution is *trivial* if $v=f=P=0$; by (E2) this holds as soon as $v=0$ and $f=0$.

## 2. Literature baseline

**Shvydkoy**, *Homogeneous solutions to the 3D Euler system*, Trans. Amer. Math. Soc. 370 (2018), arXiv:1510.03378.

- Spherical reduction (3a)-(3c) and Bernoulli transport (6), which are our (E1)-(E3) and (T1).
- Proposition 2.1 (unrestricted): there are no nontrivial $C^1$ solutions for $\alpha=1$. Shvydkoy notes that this result was obtained independently in unpublished notes of R. Monneau, L. Paszkowski and L. Xue.
- Proposition 3.1 (irrotational class): nontrivial irrotational $C^1$ solutions exist only for $\alpha\in\mathbb Z\setminus\{1\}$; they are built from spherical harmonics and have $H=0$ (for $\alpha=0$, where $u=e$ is constant and $P$ is a constant, $H=|e|^2+2P$ is constant and vanishes for the choice $P=-\frac12|e|^2$).
- Proposition 3.2 (class $H\equiv0$): "for $\alpha\le2$ irrotational solutions are unique in the class of all $C^2$-smooth solutions with $H=0$". For $1<\alpha\le2$ the proof integrates (E2) with $H=0$ to get $(2-\alpha)\int f^2=(1-\alpha)\int|v|^2$, so $f=v=0$ unless $\alpha=2$; at $\alpha=2$ the radial solution $v=0$, $f=$ const, $P=-f^2/2$ survives. For $1<\alpha<2$ the statement is therefore: $H\equiv0$ implies the solution is trivial. We re-derive this in Lemma 3.3. It is an unrestricted statement in the sense that no symmetry is assumed, but it carries the hypothesis $H\equiv0$.
- Identities (21)-(28): with $u_S=(1-\alpha)v^\perp-\nabla^\perp f$, the 3D vorticity is $|x|^{-1-\alpha}(u_S+\zeta\omega)$, and (24a) $u_S\times v=\alpha H\omega$, (24b) $fu_S-\zeta v=-\frac12\nabla^\perp H$, (28b) $v\cdot\nabla\zeta-u_S\cdot\nabla f=f\zeta$. In our notation $u_S=J\eta^\sharp$, and these are Lemma 3.1(c), (b), (h).
- Proposition 4.1 and Corollaries 4.2-4.4 (unrestricted): $f\equiv0$ forces the swirl solution $b=A\sin^{-\alpha}$, $p=-A^2/(2\alpha\sin^{2\alpha})$, which is $C^1$ only for $\alpha\le-1$; so for $1<\alpha<2$, $f\equiv0$ implies triviality. Also $P\ge0$ and $\alpha>0$ imply triviality (Corollary 4.4).
- Lemma 4.5 (unrestricted, $0<\alpha<1$ only): $H\le0$, proved by a trajectory argument. It is not used anywhere below.
- Proposition 5.1 (axisymmetric class): there are no $C^2$ axisymmetric solutions for $0<\alpha<2$. The proof uses the conserved quantity $|H|^{2-\alpha}|a\sin\phi|^{2\alpha}$ (his (40)). For axisymmetric data, $\operatorname{div}(H^\beta v)=0$ says that the flux $H^\beta a\sin\phi$ of $W=H^\beta v$ across latitude circles is constant, and the $2\alpha$-th power of the absolute value of this flux, $|H^\beta a\sin\phi|^{2\alpha}=H^{2-\alpha}|a\sin\phi|^{2\alpha}$, is exactly his conserved quantity. So (40) is the axisymmetric case of the divergence-free field $W$ underlying our stream function $\Psi$ (Section 13).

**Abe**, *Existence of homogeneous Euler flows of degree $-\alpha\notin[-2,0]$*, Arch. Ration. Mech. Anal. 248 (2024), article 30, arXiv:2305.05987. Abe calls a flow Beltrami when its Bernoulli function vanishes, i.e. $H\equiv0$.

- Theorem 1.1: no rotational Beltrami solutions in $C^1$ for $1\le\alpha\le2$, and none in $C^2$ for $\alpha<1$; existence of axisymmetric Beltrami solutions for $\alpha>2$ and for $\alpha<0$, with the stated regularity.
- Theorem 1.3: every radially irrotational ($\zeta\equiv0$) $C^2$ solution with nonconstant Bernoulli function is axisymmetric without swirl.
- Theorems 1.4 and 1.5 (rotational axisymmetric solutions without swirl, and all rotational axisymmetric solutions, respectively): nonexistence for $1\le\alpha\le2$ in $C^1$, and in $C^2$ for $-2<\alpha<1$ (Theorem 1.4, which also covers $\alpha=-2$ under a condition on the axis) and for $0\le\alpha<1$ (Theorem 1.5); existence for $\alpha>2$ and $\alpha<-2$.
- Theorems 1.7 and 1.8 concern 2D homogeneous flows; in particular there exist 2D reflection-symmetric $(-\alpha)$-homogeneous solutions for $1<\alpha<2$. These are planar and do not bear on the 3D question.

These are restricted classifications (Beltrami, axisymmetric, $\zeta\equiv0$ via Theorem 1.3, two-dimensional).

**Later work located** (arXiv search, October 2026): K. Abe, N. Sato and C. Xie, *Minus one homogeneous Euler flows are geodesible*, arXiv:2606.18655 (main result: $(-1)$-homogeneous flows in dimension $n\ge4$ are geodesible; their Theorem 5.1 also excludes $(-\alpha)$-homogeneous geodesible solutions, i.e. those with $\iota_u du=0$ for the flat metric, for $1<\alpha\le n-1$, apart from the irrotational one at $\alpha=n-1$. For $n=3$ the condition $\iota_udu=0$ says $u\times\operatorname{curl}u=0$, so the Bernoulli function is constant and, for $\alpha\ne0$, zero; this is the class $H\equiv0$ already covered by Shvydkoy's Proposition 3.2); L. Li, X. Yan and Z. Yang, *Rigidity for homogeneous solutions to the two-dimensional Euler equations in sector-type domains*, arXiv:2512.18700; M. P. Coiculescu, *Ill-posedness of the Euler equations linearized around homogeneous steady states*, arXiv:2609.06313 (planar, linear); X. Luo and R. Shvydkoy, *2D homogeneous solutions to the Euler equation*, Comm. Partial Differential Equations 40 (2015) 1666-1687, arXiv:1409.4322, with the addendum in Comm. Partial Differential Equations 42 (2017), arXiv:1608.00061. None of these treats unrestricted 3D solutions with $1<\alpha<2$.

**Unrestricted 3D baseline for $1<\alpha<2$ before this report**, as far as we found: triviality under the hypotheses $H\equiv0$ (Shvydkoy, Prop. 3.2), $f\equiv0$ (Prop. 4.1), $P\ge0$ (Cor. 4.4), and $\zeta\equiv0$ (Abe, Theorem 1.3 combined with Theorems 1.4 and 1.1); and nonexistence at the endpoint $\alpha=1$.

**Maximum principles.** Maximum principles are a standard tool for stationary and self-similar problems in fluid mechanics. D. Chae, *Euler's equations and the maximum principle*, Math. Ann. 361 (2015) 51-66, arXiv:1308.1051, applies a maximum principle to the vorticity in the far field of the self-similar Euler equations to exclude discretely self-similar blow-up. V. Šverák, *On Landau's solutions of the Navier-Stokes equations*, J. Math. Sci. (N.Y.) 179 (2011) 208-228, arXiv:math/0604550, classifies the smooth $(-1)$-homogeneous solutions of the stationary Navier-Stokes equations; Shvydkoy (his Section 5.1) notes that this proof uses a maximum principle. Minimum principles for the pressure itself, obtained from the pressure equation, are classical for irrotational flows, where $\Delta p=-|Du|^2\le0$; see for instance A. Constantin and W. Strauss, *Pressure beneath a Stokes wave*, Comm. Pure Appl. Math. 63 (2010) 533-557, and T. Lyons, *The pressure distribution in extreme Stokes waves*, Nonlinear Anal. Real World Appl. 31 (2016) 77-87, arXiv:1601.06026. For viscous flows the head pressure $p+\frac12|u|^2$ satisfies a maximum principle, which is used in Liouville theorems for the stationary Navier-Stokes equations (for example D. Chae, *Liouville-type theorems for the forced Euler equations and the Navier-Stokes equations*, Comm. Math. Phys. 326 (2014) 37-48, arXiv:1306.5839). The principle of Section 0 is of a different kind. It concerns the angular profile $P$ of a homogeneous rotational flow, and a minimum point of $P$ is not a critical point of $p$ in $\mathbb R^3$, since there $\nabla p=-2\alpha r^{-2\alpha-1}P\,\omega$. A minimum principle for the pressure of a general stationary Euler flow is false: the planar rotation $u=(-x_2,x_1)$, $p=\frac12(x_1^2+x_2^2)-1$, has a negative strict pressure minimum. The final step of our proof of Theorem 1, "$P\ge0$ implies trivial", is Shvydkoy's Corollary 4.4 (proved there by a Riccati inequality along orbits), although we give a different two-line argument. We did not find the pressure minimum principle of Section 0, or Theorem 1, in the literature we checked; an independent literature search by the referee (Section 15) did not find them either.

**Further recent work located** (arXiv, October 2026):

- Y. Huang and A. Karakhanyan, *A monotonicity formula for almost self-similar suitable weak solutions to the stationary Navier-Stokes equations in $\mathbb R^5$*, arXiv:2511.02579. Their Theorem 4.1 states that a $(-1)$-homogeneous stationary Euler field $V\in W^{1,2}_{\rm loc}(\mathbb R^5)$ with pressure in $L^1_{\rm loc}$ has vanishing radial component and vanishing Bernoulli function ($f=|v|^2+2p=0$).
- K. Abe, J. Gómez-Serrano and I.-J. Jeong, *Homogeneous steady states for the generalized surface quasi-geostrophic equations*, arXiv:2510.03009. They prove existence and nonexistence of odd-symmetric homogeneous steady states of the generalized SQG equations in the plane, in different parameter ranges.
- H. Choi and M. P. Coiculescu, *Multi-sink solutions to the self-similar Euler equations*, arXiv:2602.15152. They construct planar homogeneous steady states with velocity cusps along rays.

None of these concerns the three-dimensional problem with $0<\alpha<2$.

## 3. Identities

**Lemma 3.1.** For every $C^2$ solution:

- (a) $\nabla_vv=\nabla(Q/2)+\zeta Jv$;
- (b) $\nabla H=-2f\eta^\sharp-2\zeta Jv$;
- (c) $\eta(v)=-\alpha H$;
- (d) $d\eta=(1-\alpha)\zeta\mu$;
- (e) $\iota_v\mu\wedge\eta=\alpha H\mu$, and hence $dH\wedge\eta=-2\alpha H\zeta\mu$;
- (f) for $\phi\in C^1$ on an open interval containing the values of $H$ on an open set $O$: $\operatorname{div}(\phi(H)v)=f\,[2\alpha H\phi'(H)-(2-\alpha)\phi(H)]$ on $O$;
- (g) for $\phi$ as in (f): $d(\phi(H)\eta)=[(1-\alpha)\phi(H)-2\alpha H\phi'(H)]\,\zeta\mu$ on $O$;
- (h) $v\cdot\nabla\zeta=f\zeta+(1-\alpha)\langle Jv,\nabla f\rangle$.

*Proof.*

(a) For any vector field, $(\nabla_vv)^\flat=\iota_vdv^\flat+\tfrac12dQ$, and $\iota_v(\zeta\mu)=\zeta(Jv)^\flat$.

(b) By (E3) and (a), $\nabla P=-\nabla(Q/2)-\zeta Jv-(1-\alpha)fv$. Hence $\nabla H=\nabla Q+2f\nabla f+2\nabla P=2f\nabla f-2(1-\alpha)fv-2\zeta Jv$.

(c) $\eta(v)=(1-\alpha)Q-v\cdot\nabla f=-\alpha H$ by (T2).

(d) $d\eta=(1-\alpha)dv^\flat$.

(e) Since $S^2$ is 2-dimensional, $0=\iota_v(\mu\wedge\eta)=\iota_v\mu\wedge\eta+\eta(v)\mu$, so $\iota_v\mu\wedge\eta=-\eta(v)\mu=\alpha H\mu$. By (b), $dH=-2f\eta-2\zeta\iota_v\mu$, so $dH\wedge\eta=-2\zeta\,\iota_v\mu\wedge\eta=-2\alpha H\zeta\mu$.

(f) $\operatorname{div}(\phi(H)v)=\phi'(H)\,v\cdot\nabla H+\phi(H)\operatorname{div}v$; now use (T1) and (E1).

(g) $d(\phi(H)\eta)=\phi'(H)\,dH\wedge\eta+\phi(H)\,d\eta$; now use (d) and (e).

(h) Apply $d$ to the 1-form version of (E3), $d(Q/2+P)+\zeta\iota_v\mu+(1-\alpha)fv^\flat=0$. Use $d(\iota_v\mu)=(\operatorname{div}v)\mu$, $a\wedge\iota_v\mu=a(v)\mu$ for 1-forms $a$, and $df\wedge v^\flat=-\langle\nabla f,Jv\rangle\mu$. This gives $v\cdot\nabla\zeta+\zeta\operatorname{div}v+(1-\alpha)(f\zeta-\langle\nabla f,Jv\rangle)=0$; then use (E1). $\square$

Identities (b), (c), (d), (e), (f) and (h) were also verified symbolically (Section 15). Taking $\phi(h)=h^\gamma$ in (g) on $O=U$ gives $(1-\alpha)h^\gamma-2\alpha\gamma h^\gamma=0$, because $2\alpha\gamma=1-\alpha$. So **$\theta=H^\gamma\eta$ is a closed $C^1$ form on $U$**, as stated in the task. Taking $\phi(h)=h^\beta$ in (f) gives $\operatorname{div}(H^\beta v)=0$ on $U$, because $2\alpha\beta=2-\alpha$.

**Lemma 3.2.** $\operatorname{div}(fv)=\alpha H+(1-\alpha)Q-(2-\alpha)f^2$.

*Proof.* $\operatorname{div}(fv)=v\cdot\nabla f+f\operatorname{div}v$; use (T2) and (E1). $\square$

**Lemma 3.3 (global identities and stagnation points).**

1. $\alpha\int H\,dS=(2-\alpha)\int f^2\,dS+(\alpha-1)\int|v|^2\,dS$. Hence a nontrivial solution has $\int H\,dS>0$, and $H\equiv0$ forces triviality.
2. $\int f\,dS=0$.
3. If $v(x)=0$ then $H(x)=0$. Hence $\emptyset\ne S\subset Z$.
4. $|H|\le C|v|$ on $S^2$, where $C$ depends on $\|\nabla f\|_\infty$ and $\|v\|_\infty$.

*Proof.*

1. Integrate Lemma 3.2 over $S^2$. If the solution is nontrivial then $(v,f)\not\equiv0$, so the right side is positive.
2. Integrate (E1).
3. At $x$, (E2) reads $0=\alpha f^2+2\alpha P$, so $H(x)=f^2+2P=0$. The hairy ball theorem gives a zero of $v$.
4. By (T2), $\alpha|H|\le|v||\nabla f|+(\alpha-1)|v|^2$. $\square$

Thus $H$ vanishes somewhere and, if the solution is nontrivial, has positive mean. The positive mean alone does not determine the sign of $H$ pointwise; the sign is settled by Theorem A.

## 4. Theorem A: $H\ge0$

Fix $\chi\in C^\infty(\mathbb R)$, nondecreasing, with $\chi=0$ on $(-\infty,1]$ and $\chi=1$ on $[2,\infty)$. For $\varepsilon>0$ define
$$\psi_\varepsilon(h)=\chi(-h/\varepsilon)\,(-h)^\beta\ \ (h<0),\qquad \psi_\varepsilon(h)=0\ \ (h\ge0).$$
$\psi_\varepsilon$ is $C^\infty$ on $\mathbb R$ because it vanishes on $(-\varepsilon,\infty)$. Hence $W_\varepsilon=\psi_\varepsilon(H)v$ is a $C^2$ vector field on $S^2$.

**Step 1 (exact divergence).** For $h<0$, put $s=-h$ and $t=s/\varepsilon$. Then
$$2\alpha h\psi_\varepsilon'(h)-(2-\alpha)\psi_\varepsilon(h)=2\alpha s\Big[\chi'(t)\frac{s^\beta}{\varepsilon}+\beta\chi(t)s^{\beta-1}\Big]-(2-\alpha)\chi(t)s^\beta=2\alpha\,\varepsilon^\beta\,t^{1+\beta}\chi'(t),$$
using $2\alpha\beta=2-\alpha$. Let $F(t)=t^{1+\beta}\chi'(t)$ for $t>0$ and $F(t)=0$ for $t\le0$. By Lemma 3.1(f),
$$\operatorname{div}W_\varepsilon=2\alpha\,\varepsilon^\beta f\,F(-H/\varepsilon)\quad\text{on }S^2,\qquad \|\operatorname{div}W_\varepsilon\|_\infty\le2^{2+\beta}\alpha\|f\|_\infty\|\chi'\|_\infty\,\varepsilon^\beta .$$

**Step 2 (integration).** $fW_\varepsilon$ is $C^1$, so $\int_{S^2}\operatorname{div}(fW_\varepsilon)\,dS=0$, that is,
$$I_\varepsilon:=\int W_\varepsilon\cdot\nabla f\,dS=-\int f\operatorname{div}W_\varepsilon\,dS=-2\alpha\varepsilon^\beta\int f^2F(-H/\varepsilon)\,dS\ \longrightarrow\ 0\qquad(\varepsilon\to0),$$
since $\beta>0$.

**Step 3 (sign).** By (T2), $W_\varepsilon\cdot\nabla f=\psi_\varepsilon(H)\,[\alpha H+(1-\alpha)|v|^2]$. Where $\psi_\varepsilon(H)\ne0$ we have $H<0$, and there the bracket is at most $\alpha H<0$ because $\alpha>1$. So $W_\varepsilon\cdot\nabla f\le0$ everywhere.

**Step 4 (contradiction).** Suppose $H(x_0)=-4\delta<0$. Choose a closed disk $D\ni x_0$ of positive area with $H\le-2\delta$ on $D$. For $\varepsilon\le\delta$ we have $\chi(-H/\varepsilon)=1$ on $D$, so
$$I_\varepsilon\le\int_D(-H)^\beta\alpha H\,dS\le-\alpha(2\delta)^{1+\beta}|D|<0$$
uniformly in $\varepsilon$, contradicting Step 2. Hence $H\ge0$. $\square$

*Remarks.*

- No property of the zero set or of $\{H<0\}$ is used; the divergence theorem is applied on the closed sphere to $C^1$ fields.
- The hypotheses enter as follows: $\alpha>1$ gives the sign in Step 3, and $\alpha<2$ gives $\beta>0$, which makes the defect in Step 2 vanish. At $\alpha=2$ one has $\beta=0$, the defect is of order one, and the argument fails.
- The same argument works at $\alpha=1$, where the bracket in Step 3 equals $H$.

## Part II. The route through the Bernoulli function

The results of this part were obtained before we found the pressure argument of Section 0. Most statements below either assume that the solution is nontrivial or prove triviality under an extra hypothesis. By Theorem 1, statements of the first kind concern an empty class, and statements of the second kind are weaker than Theorem 1. Statements made for every $C^2$ solution on $S^2$, such as Theorem A and Proposition K, are proved without Theorem 1. Some auxiliary lemmas in Sections 5 to 8 (for instance Lemma 8.4 on scalar functions, Lemma 8.6 on capacity, and the remark on closed $L^2$ forms after the proof of Theorem L) do not involve the Euler equations. We keep them for three reasons.

- They answer the specific questions in Sections 4 to 6 of the task: the sign lemma, the singular form $\theta$, and the regularized forms and their defect.
- They use the sign and the transport law of the Bernoulli function and the topology of $S^2$, but not the value of the curvature (Section 10.2).
- Several of them are local statements.

Their proofs are in Sections 5 to 8. Throughout Part II, $1<\alpha<2$, $(v,f,P)$ is a $C^2$ solution on $S^2$, and the notation of Section 1 is used.

### Statements of Part II

**Theorem A (sign of the Bernoulli function).** $H\ge0$ on $S^2$.

**Theorem B (structure of a nontrivial solution).** Assume the solution is nontrivial. Then $\emptyset\ne S\subset Z$, $U\ne\emptyset$, and:

1. $W=H^\beta v$ is Hölder continuous of exponent $2\beta$ and divergence free in $\mathcal D'(S^2)$. There is $\Psi\in C^{1,2\beta}(S^2)\cap C^3(U)$ with $W=J\nabla\Psi$. Its critical set is exactly $Z$, and $\Psi$ is constant along every orbit of $v$.
2. $\Psi(Z)$ has Lebesgue measure zero. $\Psi$ is constant on each connected component of $Z$.
3. For every $c\notin\Psi(Z)$ the level set $\Psi^{-1}(c)$ is empty or a finite disjoint union of periodic orbits of $v$ contained in $U$. Almost every point of $U$ lies on a periodic orbit.
4. On $U$ the 1-form $\theta=H^\gamma\eta$, $\eta=(1-\alpha)v^\flat-df$, is $C^1$ and closed. For every periodic orbit $\Gamma\subset U$ of period $T$,
$$\oint_\Gamma\theta=-\alpha\int_0^TH^{1+\gamma}\,dt<0,\qquad \int_0^Tf\,dt=0,\qquad \alpha\int_0^TH\,dt=(\alpha-1)\int_0^T|v|^2\,dt=(\alpha-1)\Big|\int_D\zeta\,dS\Big|,$$
where $D$ is either component of $S^2\setminus\Gamma$. Both components of $S^2\setminus\Gamma$ meet $Z$.
5. For every connected component $V$ of $U$, both $S^2\setminus V$ and $\partial V$ are disconnected. In particular no component of $U$ is simply connected, and no component of $U$ has connected boundary.

**Theorem C (thick shells).** If the solution is nontrivial, there are $c_0,\varepsilon_0>0$ such that
$$|\{\varepsilon\le H\le2\varepsilon\}|\ \ge\ c_0\,\varepsilon^{(\alpha-1)/(2\alpha)}\qquad(0<\varepsilon\le\varepsilon_0).$$
The same lower bound (with a different constant) holds inside each component of $S^2\setminus\Gamma$ for every periodic orbit $\Gamma\subset U$. Consequently, if
$$\liminf_{s\to0^+}\ s^{-(\alpha-1)/(2\alpha)}\,\big|\{0<H\le s\}\big|=0,$$
the solution is trivial.

**Proposition D (the singular one-form).** Assume the solution is nontrivial.
1. $\int_U H^\gamma|\zeta|\,dS=+\infty$.
2. No locally integrable 1-form on $S^2$ that coincides with $\theta$ on $U$ is closed in the sense of distributions (nor is any distributional extension; see the remark after the proof). If such an extension $\tilde\theta$ exists, $d\tilde\theta$ is a nonzero distribution supported in $Z$, and $\langle d\tilde\theta,G\circ\Psi\rangle=\alpha\int G'(\Psi)H^{3/(2\alpha)}dS$ for $G\in C^1(\mathbb R)$.
3. For $\Theta_\varepsilon=(H+\varepsilon)^\gamma\eta$ one has exactly $d\Theta_\varepsilon=(1-\alpha)\varepsilon(H+\varepsilon)^{\gamma-1}\zeta\mu$. The part of this defect carried by $Z$ is $(1-\alpha)\varepsilon^\gamma\zeta\,\mu\llcorner Z$ and satisfies $\int_ZG(\Psi)\zeta\,dS=0$ for all $G\in C^1$. The part carried by $U$ tends to zero on compact subsets of $U$, but its pairing with $G(\Psi)$ converges to $\alpha\int G'(\Psi)H^{3/(2\alpha)}dS$, which is nonzero for $G(s)=s$. So, tested against functions of $\Psi$, a defect concentrating at $Z$ is always present for a nontrivial solution. (We do not prove that these defects converge as measures on $S^2$; only the pairings with $G\circ\Psi$ are controlled.)
4. Pairings with functions of $H$ alone carry no information: $\int\psi(H)\zeta\,dS=0$ for every continuous $\psi$.

**Theorem E (Hessian obstruction).** Assume the solution is nontrivial. Then for every periodic orbit $\Gamma\subset U$, each component of $S^2\setminus\Gamma$ contains a point of $Z_0$. The set $Z_0$ is closed and invariant under the flow of $v$. At every stagnation point $z$, $f(z)\nabla f(z)=0$ and $f(z)\zeta(z)=0$; and $z\in Z_0$ holds if and only if $\zeta(z)=0$, $\nabla f(z)=0$, and either $f(z)=0$ or $D^2f(z)=(1-\alpha)Dv(z)$. In that case $Dv(z)$ is symmetric with trace $-(2-\alpha)f(z)$.

**Theorem F (conditional nonexistence).** Each of the following conditions implies that the solution is trivial.

- (F1) $D^2H(z)\ne0$ for every $z\in Z$. (This covers zero sets consisting of nondegenerate minima, Morse-Bott minima, and minima where the Hessian has rank one.)
- (F2) There are an open set $N\supset Z_0$, $C>0$ and $\kappa>(\alpha-1)/(2\alpha)$ with $|\{x\in N:0<H(x)\le s\}|\le Cs^\kappa$ for all small $s>0$.
- (F3) $Z$ is contained in the union of finitely many points and finitely many rectifiable curves, and $H(x)\ge c\,\mathrm{dist}(x,Z)^n$ near $Z$ for some $c>0$ and $n<2\alpha/(\alpha-1)$; or $Z$ is finite and the same holds with $n<4\alpha/(\alpha-1)$. (Note $2\alpha/(\alpha-1)>4$ and $4\alpha/(\alpha-1)>8$ on the whole interval.)
- (F4) $Z$ is finite and $Dv(z)\ne0$ at every $z\in Z$.
- (F5) $\zeta=0$ on $\{0<H<\varepsilon_1\}$ for some $\varepsilon_1>0$ (for instance $\zeta\equiv0$).
- (F6) $H\le C\,\mathrm{dist}(\cdot,Z)^k$ on $S^2$ for some $k>4\alpha/(2-\alpha)$; or $Z$ is contained in finitely many points and rectifiable curves and the same holds for some $k>2\alpha/(2-\alpha)$ (Theorem L.5, which also gives a version on one side of a periodic orbit).

For real-analytic solutions, (F3) applies whenever the Łojasiewicz exponent $n$ in $H\ge c\,\mathrm{dist}(\cdot,Z)^n$ is smaller than $2\alpha/(\alpha-1)$. We have no bound on $n$; the analytic case is settled instead by Theorem J, by a different argument.

The finite-$Z$ parts of (F3) and (F4) are superseded by Theorem L.3. If $1<\alpha<\frac32$ and $Z$ is contained in finitely many points and rectifiable curves, then (F3) and (F6) together exclude every exact power law $c\,\mathrm{dist}(\cdot,Z)^k\le H\le C\,\mathrm{dist}(\cdot,Z)^k$ near $Z$, since $2\alpha/(2-\alpha)<2\alpha/(\alpha-1)$ in that range.

**Theorem G (finite zero set).** (Vacuous by Theorem L.3: no nontrivial solution has finite $Z$. The statement records what the 2-jet analysis gives at an extremal point of $\Psi$.) Assume the solution is nontrivial and $Z$ is finite. Then $Z=S$. Let $z$ be a point where $\Psi$ attains its maximum or its minimum; there are at least two such points. Then:
1. a punctured neighbourhood of $z$ lies in $U$, and $z$ is surrounded by periodic orbits $\Gamma$ that shrink to $z$, whose inner disks meet $Z$ only at $z$, and which all have the same value $\oint_\Gamma\theta=-p<0$;
2. $z\in Z_0$, and $f(z)=0$, $\nabla f(z)=0$, $Dv(z)=0$, $\zeta(z)=0$;
3. the quadratic part $h\mapsto D^2v(z)[h,h]$ of $v$ at $z$ vanishes for some $h\ne0$;
4. $H(x)\le C\,d(x,z)^4$ near $z$;
5. every periodic orbit $\Gamma$ around $z$ contained in the geodesic disk $B(z,\rho)$ has period $T(\Gamma)\ge c\,\rho^{-3(\alpha+1)/(\alpha-1)}$.

**Proposition H (the top end).** Assume the solution is nontrivial and $M=\max\Psi$ is an isolated point of $\Psi(Z)$. Then for some $\delta>0$, $\Psi^{-1}((M-\delta,M))$ is a finite disjoint union of open annuli, each foliated by periodic orbits along which $\oint\theta$ is constant. The periods tend to $+\infty$ as the level tends to $M$. Every Hausdorff limit of these orbits is a compact, connected, flow-invariant subset of $Z\cap\Psi^{-1}(M)$ containing a stagnation point. The same holds at $\min\Psi$.

**Theorem I (no uniformly rotating isolated zeros).** (Also a consequence of Theorem L.2; see the remark after the proof of Theorem L.) Assume the solution is nontrivial and let $z$ be an isolated point of $Z$. Let $(r,\varphi)$ be geodesic polar coordinates centred at $z$ and $v_\varphi=\langle v,e_\varphi\rangle$. Then there are no $r_0>0$, $c\in(0,1)$, $D\ge1$ and nondecreasing $m:(0,r_0)\to(0,\infty)$ with $m(2r)\le Dm(r)$ for $0<r<r_0/2$ such that, for one of the two orientations,
$$c\,m(r)\le v_\varphi\quad\text{and}\quad |v|\le m(r)/c\qquad(0<r<r_0).$$
In particular, let $v$ be $C^k$ near $z$ ($k\ge1$), let $y$ be normal coordinates centred at $z$, and suppose the Taylor polynomial of order $k$ of $v$ at $z$ is not zero. Then its lowest-degree nonzero homogeneous part $V$ has a characteristic direction: $\langle V(y),Jy\rangle=0$ for some $y\ne0$, where $J$ is the rotation by $\pi/2$ of $\mathbb R^2\cong T_zS^2$. For example, $Dv(z)$ cannot have nonreal eigenvalues. The proof rests on an inequality valid on every periodic orbit (Lemma 8.1): along a family of periodic orbits with $\ell\bar a^{1/\alpha}/|\oint\theta|\to0$ ($\ell$ the length, $\bar a$ the arithmetic mean of the speed), the harmonic mean of the speed must become much smaller than its arithmetic mean.

**Theorem J (real-analytic solutions).** If $v$, $f$ and $P$ are real analytic on $S^2$, the solution is trivial. More precisely, the following local statement holds. Let the solution be $C^2$ and nontrivial, let $M=\max\Psi$ be an isolated point of $\Psi(Z)$, let $A$ be one of the annuli of Proposition H, and let
$$L=\bigcap_{c<M}\overline{A\cap\{\Psi>c\}} .$$
Then $v,f,P$ are not all real analytic on any neighbourhood of $L$. The proof resolves the singularities of $v$ near $L$ by finitely many point blow-ups and shows, using an Euler-specific bound $H\circ\pi\le Cm^2$ in terms of the monomial factor $m$ of the lifted field, that $\oint_\Gamma H^{1+\gamma}\,dt\to0$ along the orbits of $A$ as $\Psi\to M$. This contradicts the constancy of $\oint\theta=-\alpha\oint H^{1+\gamma}dt$ in $A$.

**Proposition K (the zero set).** For every $C^2$ solution, $Z=S$ and $v=f=P=0$ at every point of $Z$; and $f^2<H$ on $U$. In particular the solution vanishes identically on the interior of $Z$, and $f(z)=0$ at every stagnation point.

We say that a compact set $K\subset S^2$ has *capacity zero* if for every $\varepsilon>0$ there is a Lipschitz function $\phi:S^2\to[0,1]$ with $\phi=1$ on a neighbourhood of $K$ and $\int(|\nabla\phi|^2+\phi^2)\,dS<\varepsilon$. This is the vanishing of the Sobolev $W^{1,2}$ capacity; for compact sets it is equivalent to the vanishing of the logarithmic capacity (Adams and Hedberg 1996), but we use only the definition. Points, and more generally countable compact sets, have capacity zero, while connected compact sets with more than one point do not (Section 8).

**Theorem L (square integrability of $\theta$; zero sets of capacity zero).** Assume the solution is nontrivial, and let $\tilde\theta$ be the measurable 1-form equal to $\theta$ on $U$ and to $0$ on $Z$. Put $\lambda_*=\frac{2-\alpha}{4\alpha}$.
1. For $0\le\lambda<\lambda_*$, $\int_UH^{-2\lambda}|\theta|^2dS<\infty$. In particular $\tilde\theta\in L^2(S^2)$.
2. Let $\Gamma\subset U$ be a periodic orbit, $D$ a component of $S^2\setminus\Gamma$, and $N\subset U$ a closed annular neighbourhood of $\Gamma$. For $0\le\lambda<\lambda_*$ there is $c>0$ such that $\int_UH^{2\lambda}|\nabla\phi|^2dS\ge c$ for every Lipschitz $\phi:S^2\to[0,1]$ with $\phi=1$ near $Z\cap D$ and $\operatorname{supp}\phi\subset D\setminus N$. In particular ($\lambda=0$) the compact set $Z\cap D$ does not have capacity zero.
3. Consequently, if $Z$ has capacity zero, the solution is trivial. In particular every $C^2$ solution whose zero set $Z$ is finite or countable is trivial.
4. If $M=\max\Psi$ is an isolated point of $\Psi(Z)$, then the limit set $L$ of Theorem J above (for any of the annuli of Proposition H) is a connected compact subset of $Z$ with more than one point.
5. Let $\Gamma\subset U$ be a periodic orbit and $D$ a component of $S^2\setminus\Gamma$. There are no $C$ and $k>4\alpha/(2-\alpha)$ with $H\le C\,\mathrm{dist}(\cdot,Z)^k$ on $D$. If $Z\cap D$ is contained in finitely many points and rectifiable curves, there are no $C$ and $k>2\alpha/(2-\alpha)$ with this property.

Item 1 with $\lambda=0$, and item 3 for finite $Z$, were first obtained by the referee (Section 15). Theorem L.3 makes Theorem G and condition (F4) above vacuous (they describe a configuration that does not exist), and it also implies Theorem I (see the remark after the proof of Theorem L). We keep those results because their proofs are correct and give local information that may be useful elsewhere. Item 2 is sharp for what square integrability alone can give: a closed $L^2$ form on the complement of two disjoint compact sets of positive capacity can have a nonzero period around one of them (remark after the proof of Theorem L).

**Theorem M (where the defect lives).** Assume the solution is nontrivial, and let $T=d\tilde\theta$ be the distribution $\langle T,\varphi\rangle=-\int d\varphi\wedge\tilde\theta$, which lies in $H^{-1}(S^2)$ by Theorem L.1.
1. At every $z\in Z$ the eigenvalues of $Dv(z)$ are purely imaginary or zero. At every $z\in Z_0$ one has $\nabla f(z)=0$, $\zeta(z)=0$ and $Dv(z)=0$, and there is $C$ such that for all $z\in Z_0$ and $x\in S^2$, with $r=d(x,z)$,
$$|v(x)|+|f(x)|\le Cr^2,\qquad|\nabla f(x)|+|\zeta(x)|\le Cr,\qquad H(x)\le Cr^4 .$$
In particular $H\le C\,\mathrm{dist}(\cdot,Z_0)^4$.
2. $\operatorname{supp}T\subset Z_0\cap\partial Z$.
3. There are $C,r_0>0$ such that $\int_{B(z,r)\cap U}|\theta|^2\,dS\le C\,r^{4/\alpha}$ for every $z\in Z_0$ and $0<r\le r_0$.
4. Every nonempty relatively open subset of $\operatorname{supp}T$ has positive $(2/\alpha)$-dimensional Hausdorff measure $\mathcal H^{2/\alpha}$. For every periodic orbit $\Gamma\subset U$ and each component $D$ of $S^2\setminus\Gamma$, $\operatorname{supp}T\cap D\ne\emptyset$; hence $\mathcal H^{2/\alpha}(Z_0\cap\partial Z\cap D)>0$, and $Z_0\cap\partial Z\cap D$ has Hausdorff dimension at least $2/\alpha>1$. Consequently, if $\mathcal H^{2/\alpha}(Z_0\cap\partial Z)=0$, for example if $Z_0\cap\partial Z$ is contained in a countable union of rectifiable curves or has Hausdorff dimension less than $2/\alpha$, the solution is trivial.
5. (Collar theorem.) Let $\Lambda\subset Z$ be a $C^2$ Jordan curve and let $F:(\mathbb R/\ell\mathbb Z)\times[0,y_0]\to S^2$ be a $C^2$ embedding with $F(\cdot,0)$ a parametrization of $\Lambda$ and $F(s,y)\in U$ for $y>0$. Then $\oint\theta=0$ on the curves $F(\cdot,y)$, $0<y\le y_0$. Consequently, if $M=\max\Psi$ is an isolated point of $\Psi(Z)$, the limit set $L$ of each annulus of Proposition H is not a $C^2$ Jordan curve.

Item 1 at points of $Z_0$, item 2 and item 5 were first obtained by the referee (Section 15), together with the lower bound $2(2-\alpha)/\alpha$ for the Hausdorff dimension of the support, which item 4 improves to $2/\alpha$. The eigenvalue statement of item 1 at all points of $Z$, and items 3 and 4, are ours. Item 4 contains Theorem L.3, because a compact set of positive $\mathcal H^s$ measure for some $s>0$ has positive capacity (by Frostman's lemma it carries a probability measure $\nu$ with $\nu(B(x,r))\le Cr^s$, whose logarithmic energy is finite; Carleson 1967, Adams and Hedberg 1996). It also shows that rectifiable or piecewise smooth boundaries $\partial Z$ cannot occur, for zero sets with or without interior. The exponent $2/\alpha$ is the scaling of the local bounds in items 1 and 3; for $C^2$ solutions we do not know whether it can be raised, but higher regularity beats it (Theorem N).

**Theorem N (vanishing jets on the support of the defect; finite regularity).** Assume the solution is nontrivial, let $T$ be as in Theorem M and $K=\operatorname{supp}T$, and for a compact set $E$ put $N_r(E)=\{x:\mathrm{dist}(x,E)<r\}$ and $A_E(r)=|U\cap N_r(E)|$.
1. All covariant derivatives of $v$ and $f$ of order at most two vanish at every point of $K$. If $v$ and $f$ are of class $C^k$ on a neighbourhood of $K$ for an integer $k\ge2$, all their derivatives of order at most $k$ vanish on $K$.
2. Let $\Gamma\subset U$ be a periodic orbit, $D$ a component of $S^2\setminus\Gamma$ and $E=K\cap D$. Then $A_E(r)/r^{2-2/\alpha}\to+\infty$ as $r\to0$, and $E$ is not $\sigma$-finite for $\mathcal H^{2/\alpha}$.
3. Let $k\ge2$ be an integer and $0\le\sigma\le1$ with $k+\sigma\ge2\alpha$. If $v$ and $f$ are of class $C^{k,\sigma}$ on a neighbourhood of $K$ (where $C^{k,0}=C^k$), the solution is trivial. In particular, for every $1<\alpha<2$ every solution with $v,f\in C^4$ is trivial; for $1<\alpha\le\frac32$ every solution with $v,f\in C^3$ is trivial; and for $1<\alpha\le1+\frac\sigma2$ every solution with $v,f\in C^{2,\sigma}$ is trivial.

Theorem N was first obtained by the referee (Section 15), building on Theorem M; we checked every step. The key observation is that, by Theorem M.4, no nonempty relatively open part of $K$ lies on a $C^1$ curve, so by the implicit function theorem no first derivative of $v$ or $f$ can have a nonzero differential at a point of $K$. The gain in item 3 comes from an energy bound that keeps the area of $U$ near $K$ (Lemma 8.7): if $v,f$ vanish to order $m$ on $K$, the defect carried by $N_r(K)$ is $O(r^{m/\alpha-2}A_K(4r))$, and $A_K(r)\to0$ even when $K$ has positive area. Item 3 contains the global statement of Theorem J (not its local form). Item 2 excludes, for $C^2$ solutions, defect supports whose exterior layers are thin along a sequence of scales, $A_E(r_j)=O(r_j^{2-2/\alpha})$, for example sets with $|N_r(E)\setminus E|\le Cr$, even when $E$ has positive area (Section 10.2).

**Verdict on the proposed sign lemma.** The lemma "$H\ge0$ for $1<\alpha<2$" of Section 4 of the task is **correct**; the cutoff route proposed there works without any assumption on the zero set (Theorem A). The proof was independently audited by a second model, which found no gap.

**Answers to the questions of Section 6 of the task, in brief.** These answers concern a nontrivial solution, as the questions do; by Theorem 1 there is none. For such a solution the singular form $\theta=H^\gamma\eta$ never has a distributionally closed $L^1$ extension, and $H^\gamma\zeta\notin L^1(U)$ (Proposition D). Its extension $\tilde\theta$ by zero is nevertheless square integrable, even with the weight $H^{-2\lambda}$ for $\lambda<(2-\alpha)/(4\alpha)$ (Theorem L.1). So $d\tilde\theta$ is a nonzero distribution in $H^{-1}(S^2)$ supported in $Z$. It cannot be carried by a set of capacity zero (Theorem L.2, L.3); in fact its support lies in $Z_0\cap\partial Z$, where $v$ and $f$ vanish with all their derivatives of order at most two, and on each side of every periodic orbit it has non-$\sigma$-finite $\mathcal H^{2/\alpha}$ measure (Theorems M and N). The regularization $(H+\varepsilon)^\gamma\eta$ has an exactly computable exterior derivative. Its defect concentrates near $Z$, and its pairing with $G(\Psi)$ has a nonzero limit. We identify this limit only as a functional on functions of $\Psi$ (equivalently, a distribution on the value line of $\Psi$); we do not prove that the defects converge to a measure on $S^2$. Pairing with the stream function gives the identity behind Theorem C, which yields a sign-definite contradiction in particular when the shells $\{\varepsilon\le H\le2\varepsilon\}$ have area $o(\varepsilon^{|\gamma|})$ along a sequence. The Euler equations constrain the 2-jet of the solution at points of $Z_0$ (Theorem E, Theorem G), and this suffices under nondegenerate or controlled finite-order hypotheses (Theorem F). For real-analytic solutions the singular form can be followed through a resolution of singularities, and the flux $\oint\theta$ is then forced to tend to zero at the top end of $\Psi$ (Theorem J). Theorem L.5 bounds how flat $H$ can be near $Z$ from above, and (F3) from below under geometric hypotheses on $Z$. For solutions of class $C^4$ (more generally $C^{k,\sigma}$ with $k+\sigma\ge2\alpha$) the defect cannot exist, which proves triviality (Theorem N.3). What we cannot exclude, for $C^2$ solutions, is a defect support of the size just described whose exterior layers $U\cap N_r(K)$ are thick (Theorem N.2); that was the remaining obstacle of this route (Section 10.2), and Theorem 1 removes it.

## 5. Proof of Theorem B

From now on the solution is assumed nontrivial unless stated otherwise. By Theorem A and Lemma 3.3, $\emptyset\ne S\subset Z$ and $U\ne\emptyset$. Every point of $Z$ is a minimum of $H$, so $\nabla H=0$ on $Z$.

**Lemma 5.1 (Glaeser-type bound).** Let $L$ be the maximum over $S^2$ of the operator norm of the covariant Hessian $\nabla^2H$. Then:

- $|\nabla H|^2\le2LH$ on $S^2$;
- $\sqrt H$ is Lipschitz with constant $(L/2)^{1/2}$;
- $H(x)\le\frac L2\,d(x,Z)^2$;
- $H^\beta$ is Hölder continuous of exponent $2\beta$.

*Proof.*

- Fix $x$ and a unit vector $e$, and let $g(t)=H(\exp_x(te))$. Then $g\ge0$ and $|g''|\le L$, so $0\le g(t)\le g(0)+g'(0)t+Lt^2/2$ for all $t$. The choice $t=-g'(0)/L$ gives $g'(0)^2\le2Lg(0)$; if $L=0$, then $g$ is affine and nonnegative, so $g'(0)=0$. Take $e=\nabla H/|\nabla H|$.
- On $U$, $|\nabla\sqrt H|\le(L/2)^{1/2}$. For $x,y\in S^2$ and a minimizing geodesic between them, either the geodesic lies in $U$ and we integrate, or we compare $\sqrt H(x)$ and $\sqrt H(y)$ with the value $0$ at the first and last points of the geodesic in $Z$. Either way $|\sqrt H(x)-\sqrt H(y)|\le(L/2)^{1/2}d(x,y)$.
- The bound $H\le\frac L2d(x,Z)^2$ follows because $\sqrt H=0$ on $Z$.
- $H^\beta=(\sqrt H)^{2\beta}$ and $t\mapsto t^{2\beta}$ is $2\beta$-Hölder on $[0,\infty)$. $\square$

**Lemma 5.2.** $W=H^\beta v$ lies in $C^{0,2\beta}(S^2)\cap C^2(U)$, and $\int W\cdot\nabla\varphi\,dS=0$ for every $\varphi\in C^1(S^2)$.

*Proof.* Hölder continuity follows from Lemma 5.1 and the Lipschitz continuity of $v$. Smoothness on $U$ is clear.

Let $W^+_\varepsilon=\chi(H/\varepsilon)H^\beta v$, which is $C^2$ because $\chi(H/\varepsilon)$ vanishes near $\{H\le\varepsilon\}$. Lemma 3.1(f) with $\phi(h)=\chi(h/\varepsilon)h^\beta$ (extended by $0$ for $h\le0$) gives, by the computation of Section 4 with $h$ in place of $-h$,
$$\operatorname{div}W^+_\varepsilon=2\alpha\varepsilon^\beta f\,(H/\varepsilon)^{1+\beta}\chi'(H/\varepsilon),\qquad |\operatorname{div}W^+_\varepsilon|\le2^{2+\beta}\alpha\|f\|_\infty\|\chi'\|_\infty\varepsilon^\beta .$$
Also $|W^+_\varepsilon-W|\le(2\varepsilon)^\beta\|v\|_\infty$. Hence
$$\int W\cdot\nabla\varphi=\lim\int W^+_\varepsilon\cdot\nabla\varphi=-\lim\int\varphi\operatorname{div}W^+_\varepsilon=0.\ \ \square$$

**Lemma 5.3 (stream function).** There is $\Psi\in C^{1,2\beta}(S^2)$ with $\nabla\Psi=-JW=-H^\beta Jv$, that is, $W=J\nabla\Psi$. Moreover $\Psi\in C^3(U)$, and $\nabla\Psi(x)=0$ if and only if $x\in Z$.

*Proof.* Let $\Psi$ be the mean-zero weak solution of $\Delta\Psi=\operatorname{div}(-JW)$. Since $-JW\in C^{0,2\beta}$, Schauder theory for the Laplace-Beltrami operator with right side in divergence form gives $\Psi\in C^{1,2\beta}$.

Consider the continuous field $X=\nabla\Psi+JW$. In the sense of distributions, $\operatorname{div}X=0$ by construction. Also $\operatorname{curl}X=-\operatorname{div}(JX)=-\operatorname{div}(J\nabla\Psi)+\operatorname{div}W=0$. Here $\operatorname{div}(J\nabla\Psi)=0$ because $\int\langle J\nabla\Psi,\nabla\varphi\rangle dS=\int d\Psi\wedge d\varphi=\int d(\Psi\,d\varphi)=0$, first for smooth $\Psi$ and then by approximation; and $\operatorname{div}W=0$ by Lemma 5.2.

So $X^\flat$ is a continuous 1-form with $dX^\flat=0$ and $\delta X^\flat=0$ weakly. By elliptic regularity it is a smooth harmonic 1-form, and it vanishes because $H^1_{dR}(S^2)=0$. Thus $\nabla\Psi=-H^\beta Jv$. This field is $C^2$ on $U$, so $\Psi\in C^3(U)$. Finally $|\nabla\Psi|=H^\beta|v|$, and $v=0$ implies $H=0$. $\square$

**Lemma 5.4 (flow).** The flow $\varphi_t$ of $v$ is complete and $C^2$, and:

- (a) $H(\varphi_tx)=H(x)\exp\big(2\alpha\int_0^tf(\varphi_sx)\,ds\big)$, so $Z$ and $U$ are invariant;
- (b) $\Psi(\varphi_tx)=\Psi(x)$.

*Proof.* (a) is (T1) integrated along orbits. For (b), $\frac d{dt}\Psi(\varphi_tx)=\langle\nabla\Psi,v\rangle=-H^\beta\langle Jv,v\rangle=0$. $\square$

**Lemma 5.5.** $|\Psi(Z)|=0$, where $|\cdot|$ is Lebesgue measure on $\mathbb R$.

*Proof.* We treat $Z\setminus S$ and $S$ separately.

*Points of $Z\setminus S$.* Let $z\in Z\setminus S$. Choose a $C^2$ arc $\sigma:(-\delta,\delta)\to S^2$ with $\sigma(0)=z$ transverse to $v$. Then $\Phi(s,y)=\varphi_s(\sigma(y))$ is a $C^2$ diffeomorphism from $(-\delta,\delta)^2$ onto a neighbourhood $V_z$ of $z$, for $\delta$ small. By Lemma 5.4(b), $\Psi(\Phi(s,y))=g(y):=\Psi(\sigma(y))$, and $g\in C^1$.

Since $Z$ is invariant, $Z\cap V_z=\Phi((-\delta,\delta)\times Y)$ with $Y=\{y:\sigma(y)\in Z\}$. For $y\in Y$, $g'(y)=\langle\nabla\Psi(\sigma(y)),\sigma'(y)\rangle=0$. Hence $\Psi(Z\cap V_z)\subset g(\{g'=0\})$, which is null by the one-dimensional Sard lemma for $C^1$ functions. (Proof of that lemma: cover $\{g'=0\}\cap[-\delta',\delta']$ by an open set on which $|g'|<\kappa$, made of disjoint intervals $I_k$; then $|g(I_k)|\le\kappa|I_k|$, and $\kappa$ is arbitrary.) Countably many $V_z$ cover $Z\setminus S$.

*Points of $S$.* Let $L_1$ be a Lipschitz constant of $v$, so $|v(x)|\le L_1d(x,S)$. Since $d(x,Z)\le d(x,S)$, Lemma 5.1 gives
$$|\nabla\Psi(x)|=H^\beta|v|\le C_0\,d(x,S)^{2\beta+1}=C_0\,d(x,S)^{2/\alpha}.$$
Fix finitely many charts with uniformly bi-Lipschitz coordinate maps whose compact coordinate squares $[-1,1]^2$ cover $S^2$. For $\delta\in(0,1)$, divide each square into at most $4\delta^{-2}$ subsquares $q$ of side $\delta$. If $q$ meets $S$ at a point $s_0$, every point $x$ of $q$ is joined to $s_0$ by a coordinate segment of length at most $C\delta$ along which $d(\cdot,S)\le C\delta$. Hence $|\Psi(x)-\Psi(s_0)|\le C\delta\cdot C_0(C\delta)^{2/\alpha}$, so $\Psi(q)$ lies in an interval of length $C'\delta^{1+2/\alpha}$. Summing over the at most $C\delta^{-2}$ such subsquares,
$$|\Psi(S)|\le C''\delta^{2/\alpha-1}\to0\qquad(\delta\to0),$$
because $\alpha<2$. $\square$

*Remark.* This lemma replaces the Morse-Sard theorem, which is not available for a $C^{1,2\beta}$ function. It uses the specific structure $\nabla\Psi=-H^\beta Jv$ and the condition $\alpha<2$. At $\alpha=2$ the exponent $2/\alpha-1$ is zero.

**Lemma 5.6 (regular levels).**

- (a) For $c\notin\Psi(Z)$, $\Psi^{-1}(c)$ is empty or a finite disjoint union of $C^3$ Jordan curves in $U$, each of which is a single periodic orbit of $v$.
- (b) The set of points of $U$ that do not lie on a periodic orbit has measure zero.
- (c) Each component of $U$ contains a periodic orbit.

*Proof.*

- (a) $\Psi^{-1}(c)$ is compact and contained in $U$, where $\Psi$ is $C^3$ with nonvanishing gradient. So it is a compact 1-manifold, that is, finitely many circles. Each circle is invariant (Lemma 5.4), and $v$ is nonvanishing and tangent to it, so the circle is one periodic orbit.
- (b) Non-periodic points of $U$ lie in $E=U\cap\Psi^{-1}(\Psi(Z))$. $\Psi(Z)$ is compact, so $E$ is measurable. By the coarea formula on $U$, $\int_E|\nabla\Psi|\,dS=\int_{\Psi(Z)}\mathcal H^1(E\cap\Psi^{-1}(c))\,dc=0$. Since $|\nabla\Psi|>0$ on $U$, $|E|=0$.
- (c) A component $V$ of $U$ is open, so it contains a periodic point; the orbit of that point is connected and lies in $U$, hence in $V$. $\square$

**Lemma 5.7 (periodic orbits).** Let $\Gamma\subset U$ be a periodic orbit of period $T$, parametrized by $x(t)$. Then:

- (a) $\int_0^Tf(x(t))\,dt=0$;
- (b) $\alpha\int_0^TH\,dt=(\alpha-1)\int_0^T|v|^2dt$, and $\int_0^T|v|^2dt=|\int_D\zeta\,dS|$ for each component $D$ of $S^2\setminus\Gamma$;
- (c) $\oint_\Gamma\theta=-\alpha\int_0^TH^{1+\gamma}dt<0$, with $\Gamma$ oriented by the flow;
- (d) each component of $S^2\setminus\Gamma$ meets $Z$.

*Proof.*

- (a) By Lemma 5.4(a), $H(x(T))=H(x(0))>0$ forces $\int_0^Tf=0$.
- (b) Integrate (T2) over a period: $0=f(x(T))-f(x(0))=\alpha\int H\,dt+(1-\alpha)\int|v|^2dt$. Moreover $\int_0^T|v|^2dt=\oint_\Gamma v^\flat$, and Stokes' theorem on $\bar D$ gives $\oint_{\partial D}v^\flat=\int_D\zeta\,dS$ with $\partial D=\pm\Gamma$.
- (c) $\theta(v)=H^\gamma\eta(v)=-\alpha H^{1+\gamma}$ by Lemma 3.1(c).
- (d) If a component $D$ did not meet $Z$, then $\bar D\subset U$, and Stokes' theorem for the closed $C^1$ form $\theta$ would give $\oint_\Gamma\theta=\pm\int_Dd\theta=0$, contradicting (c). $\square$

**Lemma 5.8.** For every component $V$ of $U$, $S^2\setminus V$ and $\partial V$ are disconnected, and $V$ is not simply connected.

*Proof.* By Lemma 5.6(c), $V$ contains a periodic orbit $\Gamma$, so $S^2\setminus V\subset S^2\setminus\Gamma$. If $S^2\setminus V$ were connected, it would lie in one component of $S^2\setminus\Gamma$. The other component would then lie in $V\subset U$, contradicting Lemma 5.7(d).

So $S^2\setminus V=F_1\sqcup F_2$ with $F_1,F_2$ disjoint, nonempty and closed. Each $F_i$ contains a point of $\partial V$. Indeed, $F_i$ is not open, because $S^2$ is connected, so some $y\in F_i$ has every neighbourhood meeting $V\cup F_j$. Small neighbourhoods of $y$ miss the closed set $F_j$, so they meet $V$, and $y\in\bar V\setminus V=\partial V$. Thus $\partial V$ is the disjoint union of the nonempty closed sets $\partial V\cap F_i$, so it is disconnected.

A domain in $S^2$ with disconnected complement is not simply connected. $\square$

*Proof of Theorem B.* Item 1 is Lemmas 5.2, 5.3 and 5.4. In item 2, $|\Psi(Z)|=0$ is Lemma 5.5. Moreover, for a connected component $K$ of $Z$, $\Psi(K)$ is a connected subset of the null set $\Psi(Z)$, hence a point. Items 3, 4 and 5 are Lemmas 5.6, 5.7 and 5.8, together with the closedness of $\theta$ shown after Lemma 3.1. $\square$

*Further consequences.* Let $\nu=\Psi_*(H^{3/(2\alpha)}dS)$. By the coarea formula and $H=0$ on $Z$, $\nu$ is absolutely continuous, with density
$$g(c)=\int_{\Psi^{-1}(c)}\frac{H^{3/(2\alpha)}}{|\nabla\Psi|}\,d\ell=\sum_j\int_0^{T_j}H^{1+\gamma}dt=\frac1\alpha\sum_j\Big|\oint_{\Gamma_j}\theta\Big|$$
for $c\notin\Psi(Z)$, where $\Gamma_j$ are the orbits forming $\Psi^{-1}(c)$. Here we used $|\nabla\Psi|=H^\beta|v|$, $d\ell=|v|dt$ and $\frac3{2\alpha}-\beta=1+\gamma$.

On an interval $I$ of $\mathbb R\setminus\Psi(Z)$, the map $\Psi:\Psi^{-1}(I)\to I$ is a proper submersion. By Ehresmann's theorem, $\Psi^{-1}(I)$ is a finite union of annuli foliated by periodic orbits. On each annulus the orbits are homotopic in $U$, so $\oint\theta$ is constant. Hence $g$ is constant on each component of $\mathbb R\setminus\Psi(Z)$.

## 6. Thick shells and the singular one-form

**Lemma 6.1 (shell identity).** For $\varepsilon>0$ let $\Theta_\varepsilon=\chi(H/\varepsilon)H^\gamma\eta$, extended by zero where $H\le\varepsilon$. Then $\Theta_\varepsilon$ is a $C^1$ form on $S^2$ and
$$d\Theta_\varepsilon=-2\alpha\,(H/\varepsilon)\chi'(H/\varepsilon)\,H^\gamma\zeta\,\mu .$$
For every $G\in C^1(\mathbb R)$,
$$\int G'(\Psi)\,\chi(H/\varepsilon)\,H^{3/(2\alpha)}\,dS=-2\int G(\Psi)\,(H/\varepsilon)\chi'(H/\varepsilon)\,H^\gamma\zeta\,dS. \tag{6.1}$$
Let $\Gamma\subset U$ be a periodic orbit of period $T$, let $D$ be a component of $S^2\setminus\Gamma$, and let $\varepsilon<\frac12\min_\Gamma H$. Then
$$\alpha\int_0^TH^{1+\gamma}dt=2\alpha\,\Big|\int_D(H/\varepsilon)\chi'(H/\varepsilon)H^\gamma\zeta\,dS\Big|. \tag{6.2}$$

*Proof.* $\phi(h)=\chi(h/\varepsilon)h^\gamma$ is smooth on $\mathbb R$ (it vanishes for $h\le\varepsilon$). Using $2\alpha\gamma=1-\alpha$,
$$(1-\alpha)\phi-2\alpha h\phi'=-2\alpha(h/\varepsilon)\chi'(h/\varepsilon)h^\gamma .$$
Lemma 3.1(g) then gives $d\Theta_\varepsilon$.

Since $\nabla\Psi=-H^\beta Jv$ and $(Jv)^\flat=\iota_v\mu$, we have $d\Psi=-H^\beta\iota_v\mu$. Lemma 3.1(e) gives
$$d\Psi\wedge\eta=-\alpha H^{1+\beta}\mu\quad\text{on }S^2. \tag{6.3}$$
$G(\Psi)\Theta_\varepsilon$ is a $C^1$ form, and
$$d(G(\Psi)\Theta_\varepsilon)=G'(\Psi)\,d\Psi\wedge\Theta_\varepsilon+G(\Psi)\,d\Theta_\varepsilon=-\alpha\big[G'(\Psi)\chi(H/\varepsilon)H^{3/(2\alpha)}+2G(\Psi)(H/\varepsilon)\chi'(H/\varepsilon)H^\gamma\zeta\big]\mu .$$
Integration over $S^2$ gives (6.1).

For (6.2), note that $\Theta_\varepsilon=\theta$ near $\Gamma$. Stokes' theorem on $\bar D$ gives $\int_Dd\Theta_\varepsilon=\pm\oint_\Gamma\theta$, and we conclude with Lemma 5.7(c). $\square$

**Proof of Theorem C.** Let $m=\min\Psi$ and $M=\max\Psi$, and take $G(s)=s-\frac{m+M}2$, so $|G(\Psi)|\le\frac{M-m}2$. Choose $\varepsilon_0>0$ with $A_0:=\int_{\{H\ge2\varepsilon_0\}}H^{3/(2\alpha)}dS>0$. This is possible because $U\ne\emptyset$.

For $\varepsilon\le\varepsilon_0$, the left side of (6.1) is at least $A_0$, since $\chi\ge0$ and $\chi(H/\varepsilon)=1$ where $H\ge2\varepsilon$. On the support of $\chi'(H/\varepsilon)$ we have $\varepsilon\le H\le2\varepsilon$, hence $H/\varepsilon\le2$ and $H^\gamma\le\varepsilon^\gamma$. Therefore
$$A_0\le2(M-m)\|\chi'\|_\infty\int_{\{\varepsilon\le H\le2\varepsilon\}}H^\gamma|\zeta|\,dS\le2(M-m)\|\chi'\|_\infty\|\zeta\|_\infty\,\varepsilon^{\gamma}\,|\{\varepsilon\le H\le2\varepsilon\}|. \tag{6.4}$$
This gives the global bound with $c_0=A_0/(2(M-m)\|\chi'\|_\infty\|\zeta\|_\infty)$. (The inequality itself shows $M>m$ and $\zeta\not\equiv0$.)

In the same way, (6.2) gives, for $\varepsilon<\frac12\min_\Gamma H$,
$$|D\cap\{\varepsilon\le H\le2\varepsilon\}|\ \ge\ \varepsilon^{|\gamma|}\,\frac{\int_0^TH^{1+\gamma}dt}{4\|\chi'\|_\infty\sup_D|\zeta|}.$$
Finally, $|\{0<H\le2\varepsilon\}|\ge c_0\varepsilon^{|\gamma|}$ for $\varepsilon\le\varepsilon_0$ contradicts the liminf hypothesis. $\square$

**Corollary 6.2 (condition F5).** If $\zeta=0$ on $\{0<H<\varepsilon_1\}$ for some $\varepsilon_1>0$, the solution is trivial.

*Proof.* For $\varepsilon<\varepsilon_1/2$ the right side of (6.1) vanishes, while for a nontrivial solution the left side is at least $A_0>0$. $\square$

In particular, radially irrotational solutions ($\zeta\equiv0$) are trivial. For $1<\alpha<2$ this agrees with what follows from Abe's Theorems 1.3, 1.4 and 1.1.

**Lemma 6.3.** $\int\psi(H)\zeta\,dS=0$ for every $\psi\in C^0([0,\infty))$. Equivalently, $H_*(\zeta\,dS)=0$. In particular $\int_Z\zeta\,dS=0$.

*Proof.* First let $\psi\in C^1([0,\infty))$ and define
$$\phi(h)=-\frac{h^\gamma}{2\alpha}\int_0^h\psi(s)s^{-\gamma-1}ds\qquad(h>0),\qquad\phi(0)=-\frac{\psi(0)}{\alpha-1}.$$
The integral converges because $-\gamma-1>-1$. Write $\psi(s)=\psi(0)+s\psi_1(s)$ with $\psi_1$ continuous. Then $\phi(h)=\phi(0)-\frac{1}{2\alpha}h^\gamma\int_0^h\psi_1(s)s^{-\gamma}ds$. The last term is $O(h)$, and its derivative $\gamma h^{\gamma-1}\int_0^h\psi_1s^{-\gamma}ds+\psi_1(h)$ has a limit as $h\to0$. Hence $\phi\in C^1([0,\infty))$, and $\phi$ solves $(1-\alpha)\phi-2\alpha h\phi'=\psi$; this is checked by differentiation, using $2\alpha\gamma=1-\alpha$.

Extend $\phi$ to a $C^1$ function on $\mathbb R$. Then $\phi(H)\eta$ is a $C^1$ form, and Lemma 3.1(g) gives
$$0=\int d(\phi(H)\eta)=\int\psi(H)\zeta\,dS.$$
General continuous $\psi$ follow by uniform approximation. Finally take $\psi_n(h)=\max(0,1-nh)$. $\square$

**Proof of Proposition D.**

1. By the first inequality in (6.4), $\int_{\{\varepsilon\le H\le2\varepsilon\}}H^\gamma|\zeta|\ge c_1:=A_0/(2(M-m)\|\chi'\|_\infty)$ for every $\varepsilon\le\varepsilon_0$. The shells for $\varepsilon_k=4^{-k}\varepsilon_0$ are pairwise disjoint, so $\int_UH^\gamma|\zeta|\ge\sum_kc_1=\infty$.

2. Let $\tilde\theta\in L^1$ coincide with $\theta$ on $U$. Its distributional exterior derivative is $\langle d\tilde\theta,\varphi\rangle:=-\int d\varphi\wedge\tilde\theta$; this pairing extends by density to $\varphi\in C^1$. For $\varphi\in C^\infty_c(U)$ we get $-\int d\varphi\wedge\theta=\int\varphi\,d\theta=0$, so $d\tilde\theta$ is supported in $Z$. For $\varphi=G\circ\Psi$, using (6.3) and $d\Psi=0$ on $Z$,
$$\langle d\tilde\theta,G\circ\Psi\rangle=-\int_UG'(\Psi)\,d\Psi\wedge H^\gamma\eta=\alpha\int G'(\Psi)H^{3/(2\alpha)}dS .$$
For $G(s)=s$ this equals $\alpha\int H^{3/(2\alpha)}dS>0$.

3. With $\phi(h)=(h+\varepsilon)^\gamma$,
$$(1-\alpha)\phi-2\alpha h\phi'=(h+\varepsilon)^{\gamma-1}\big[(1-\alpha)(h+\varepsilon)-(1-\alpha)h\big]=(1-\alpha)\varepsilon(h+\varepsilon)^{\gamma-1},$$
which gives the formula for $d\Theta_\varepsilon$. As in Lemma 6.1, but now using only $G(\Psi)\in C^1$,
$$\alpha\int G'(\Psi)(H+\varepsilon)^\gamma H^{1+\beta}dS=(1-\alpha)\varepsilon^\gamma\int_ZG(\Psi)\zeta\,dS+(1-\alpha)\int_UG(\Psi)\,\varepsilon(H+\varepsilon)^{\gamma-1}\zeta\,dS. \tag{6.5}$$
The left side is bounded uniformly in $\varepsilon$ (dominated by $H^{3/(2\alpha)}$) and converges to $\alpha\int G'(\Psi)H^{3/(2\alpha)}$. On $U$,
$$\varepsilon^{-\gamma}\varepsilon(H+\varepsilon)^{\gamma-1}=\big(\varepsilon/(H+\varepsilon)\big)^{1-\gamma}\le1,$$
and this tends to $0$ pointwise. So the last term of (6.5) is $o(\varepsilon^\gamma)$ by dominated convergence. Multiplying (6.5) by $\varepsilon^{-\gamma}=\varepsilon^{|\gamma|}\to0$ yields $\int_ZG(\Psi)\zeta\,dS=0$. Consequently the $U$-term of (6.5) converges to $\alpha\int G'(\Psi)H^{3/(2\alpha)}dS$. On each compact $K\subset U$, $\varepsilon(H+\varepsilon)^{\gamma-1}\le\varepsilon(\min_KH)^{\gamma-1}\to0$ uniformly, so this defect concentrates at $Z$.

4. This is Lemma 6.3. $\square$

*Interpretation.* Item 2 shows that the route "extend $H^\gamma\eta$ across $Z$ to a closed form on $S^2$ and integrate" cannot work. This also holds for extensions that are only distributions: if $\tilde\theta$ is a distributional 1-form on $S^2$ that coincides with $\theta$ on $U$ and satisfies $d\tilde\theta=0$, then, since the de Rham cohomology of currents on $S^2$ agrees with that of smooth forms and $H^1(S^2)=0$, $\tilde\theta=dg$ for a distribution $g$. On $U$, $dg=\theta$ is continuous, so $g|_U$ is a $C^1$ function and $\theta$ is exact on $U$, contradicting $\oint_\Gamma\theta<0$ (Lemma 5.7). Item 3 shows that the naive bound $O(\varepsilon^\gamma)$ for the regularization error is not the issue: against test functions $G\circ\Psi$, the $Z$-part cancels exactly and the $U$-part is $o(\varepsilon^\gamma)$. The $U$-part nevertheless has a nonzero limit against $G\circ\Psi$, concentrated near $Z$. We have identified this limit only as a functional on functions of $\Psi$: if $g=d\nu/dc$ is the density of Section 5, the pushforwards of the defects under $\Psi$ converge in the sense of distributions on the value line to $-\alpha g'$. We do not know whether the defects converge as measures on $S^2$, and the number $\alpha\int H^{3/(2\alpha)}dS$ obtained for $G(s)=s$ is a first moment in $\Psi$, not a total mass (each $d\Theta_\varepsilon$ has total integral zero by Stokes). Any contradiction along this route must come from showing that the defect concentrating at $Z$ cannot produce this moment. Theorem C quantifies what this requires: the shells must have area at least $c\,\varepsilon^{|\gamma|}$.

## 7. The Hessian obstruction (Theorem E)

**Lemma 7.1.** Let $z\in Z$ with $D^2H(z)\ne0$. Then there are an open neighbourhood $B_z$ of $z$ and $C_z$ such that $|\{x\in B_z:H(x)\le s\}|\le C_z\sqrt s$ for all $s>0$.

*Proof.* $D^2H(z)$ is positive semidefinite, because $z$ is a minimum, and nonzero. So there is a unit vector $e$ with $D^2H(z)[e,e]=\lambda>0$. Choose chart coordinates $(x,y)$ centred at $z$ with $\partial_y=e$ at $z$. At a critical point the coordinate Hessian equals the covariant one, so $\partial_y^2H(z)=\lambda$. Since $H\in C^2$, $\partial_y^2H\ge\lambda/2$ on a coordinate square $B=[-\delta,\delta]^2$.

For fixed $x$, $h(y)=H(x,y)$ is strongly convex on $[-\delta,\delta]$ and nonnegative. If $h(y_1),h(y_2)\le s$, then at the midpoint $m$,
$$0\le h(m)\le\tfrac12(h(y_1)+h(y_2))-\tfrac{\lambda}{16}(y_2-y_1)^2,$$
so $|y_2-y_1|\le4\sqrt{s/\lambda}$. By Fubini, the coordinate area of $\{H\le s\}\cap B$ is at most $8\delta\sqrt{s/\lambda}$, and the spherical area is comparable. $\square$

**Proof of Theorem E, first assertion.** Let $\Gamma\subset U$ be a periodic orbit and $D$ a component of $S^2\setminus\Gamma$, and suppose $D\cap Z_0=\emptyset$. The set $Z\cap\bar D=Z\cap D$ is compact, because $\Gamma\subset U$. By Lemma 7.1 it is covered by finitely many open sets $B_{z_1},\dots,B_{z_k}$, with $|\{x\in B_{z_i}:H\le s\}|\le C_i\sqrt s$.

The compact set $\bar D\setminus\bigcup_iB_{z_i}$ does not meet $Z$, so $H\ge h_0>0$ there. For $2\varepsilon<h_0$ we get $|D\cap\{\varepsilon\le H\le2\varepsilon\}|\le\sum_iC_i\sqrt{2\varepsilon}$. The local bound of Theorem C gives $|D\cap\{\varepsilon\le H\le2\varepsilon\}|\ge c\,\varepsilon^{|\gamma|}$. Since $|\gamma|<\frac14<\frac12$, these are incompatible as $\varepsilon\to0$. $\square$

**Lemma 7.2.** $Z_0$ is closed and invariant under the flow.

*Proof.* Closedness holds because $\nabla^2H$ is continuous and $Z$ is closed.

For invariance, write $H\circ\varphi_t=H\cdot E_t$ with $E_t(x)=\exp(2\alpha\int_0^tf(\varphi_sx)ds)$, which is $C^2$ (Lemma 5.4(a)). Take second derivatives at $z\in Z$, where $H$ and $\nabla H$ vanish and $\varphi_tz\in Z$. This gives
$$D^2H(\varphi_tz)[D\varphi_tX,D\varphi_tX]=E_t(z)\,D^2H(z)[X,X].$$
Since $D\varphi_t$ is invertible, $D^2H(\varphi_tz)=0$ if and only if $D^2H(z)=0$. $\square$

**Lemma 7.3 (stagnation points).** Let $z\in S$, and write $A=Dv(z)$, $g=\nabla f(z)$, $F=D^2f(z)$ (covariant derivatives at $z$). Then
$$D^2H(z)=2\,g\otimes g-2f(z)\big[(1-\alpha)A-F\big]-2\zeta(z)\,JA, \tag{7.1}$$
$\operatorname{tr}A=-(2-\alpha)f(z)$, $\zeta(z)$ is the rotational part of $A$, $f(z)g=0$, and $f(z)\zeta(z)=0$. Moreover, $z\in Z_0$ if and only if $\zeta(z)=0$, $g=0$, and either $f(z)=0$ or $F=(1-\alpha)A$. If $z\in Z_0$, then $A$ is symmetric with trace $-(2-\alpha)f(z)$.

*Proof.* Differentiate Lemma 3.1(b) covariantly at $z$, where $v(z)=0$, $\eta^\sharp(z)=-g$ and $\nabla\eta^\sharp(z)=(1-\alpha)A-F$. This gives (7.1). The trace identity is (E1) at $z$. Also $\nabla H(z)=2f(z)g=0$.

In an oriented orthonormal frame write $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, so that $\zeta(z)=c-b$. The antisymmetric part of $A$ is $\frac{\zeta(z)}2J$, and that of $JA$ is $\frac{\operatorname{tr}A}2J$. Since $D^2H(z)$ is symmetric, the antisymmetric part of (7.1) must vanish:
$$-\zeta(z)\big[(1-\alpha)f(z)+\operatorname{tr}A\big]J=\zeta(z)f(z)J=0 .$$

- If $f(z)\ne0$: then $\zeta(z)=0$ and $g=0$, and $D^2H(z)=-2f(z)[(1-\alpha)A-F]$ vanishes if and only if $F=(1-\alpha)A$.
- If $f(z)=0$: then $\operatorname{tr}A=0$ and
$$\operatorname{tr}D^2H(z)=2|g|^2-2\zeta(z)\operatorname{tr}(JA)=2|g|^2+2\zeta(z)^2,$$
using $\operatorname{tr}(JA)=b-c=-\zeta(z)$. So $D^2H(z)=0$ forces $g=0$ and $\zeta(z)=0$; conversely these two conditions make (7.1) vanish.

In all cases $z\in Z_0$ gives $\zeta(z)=0$, that is, $A$ is symmetric. $\square$

Formula (7.1) and the two algebraic consequences were also verified symbolically (Section 15).

**Lemma 7.4.** Let $z\in S$. If $f(z)>0$, every point whose forward orbit converges to $z$ lies in $Z$. If $f(z)<0$, the same holds for backward orbits.

*Proof.* If $\varphi_tx\to z$ and $f(z)>0$, then $\int_0^tf(\varphi_sx)ds\to\infty$. By Lemma 5.4(a), boundedness of $H$ then forces $H(x)=0$. $\square$

*Remark.* If $f(z)\ne0$, then $\operatorname{tr}A\ne0$, so $A$ has an eigenvalue whose real part has the sign of $-f(z)$. By the stable manifold theorem (or its strong-stable version for a non-hyperbolic point), some orbit other than $z$ converges to $z$ in the corresponding time direction. So $z$ is not isolated in $Z$. Hence isolated points of $Z$ satisfy $f=0$.

**Lemma 7.5 (vanishing on the zero set; Proposition K).** For every $C^2$ solution:

1. $Z=S$, and $v=f=P=0$ at every point of $Z$;
2. $f^2<H$ on $U$.

*Proof.* 1. Let $a=\max_Zf$, attained at $z\in Z$. If $v(z)\ne0$, the orbit of $z$ lies in $Z$ (Lemma 5.4(a)), and on $Z$ (T2) reads $v\cdot\nabla f=-(\alpha-1)|v|^2$. So $f(\varphi_tz)>a$ for small $t<0$, which is impossible. Hence $v(z)=0$. Suppose $a>0$. Then $\operatorname{tr}Dv(z)=\operatorname{div}v(z)=-(2-\alpha)a<0$, so $Dv(z)$ has an eigenvalue with negative real part. By the stable manifold theorem (for a hyperbolic sink or saddle the usual stable manifold, and if the other eigenvalue is zero the strong stable manifold), there is $x\ne z$ with $\varphi_tx\to z$ as $t\to+\infty$. If $x\in U$, this contradicts Lemma 7.4. If $x\in Z$, then $x\notin S$ (it is not a fixed point), so $t\mapsto f(\varphi_tx)$ is strictly decreasing by (T2) and tends to $a$; hence $f(x)>a$, which is again impossible. Therefore $\max_Zf\le0$. In the same way, if $b=\min_Zf$ were negative, it would be attained at a stagnation point $z$ with $\operatorname{tr}Dv(z)>0$, the unstable manifold would give $x\ne z$ with $\varphi_tx\to z$ as $t\to-\infty$, Lemma 7.4 excludes $x\in U$, and $x\in Z$ would give $f(x)<b$. So $f=0$ on $Z$. If $x\in Z\setminus S$, then $f$ is strictly decreasing along the orbit of $x$, which lies in $Z$; this contradicts $f=0$ on $Z$. Hence $Z\subset S$, and $Z=S$ by Lemma 3.3. Finally $P=\frac12(H-|v|^2-f^2)=0$ on $Z$.

2. Let $\Gamma\subset U$ be a periodic orbit and put $y=f/\sqrt H$, a $C^1$ function on $U$. By (T1) and (T2),
$$v\cdot\nabla y=\alpha\sqrt H\,(1-y^2)-(\alpha-1)\frac{|v|^2}{\sqrt H}. \tag{7.2}$$
At a point of $\Gamma$ where $y|_\Gamma$ is maximal or minimal the left side vanishes, and $v\ne0$ there by part 1, so $y^2<1$ at that point. Hence $y^2<1$ on all of $\Gamma$. Points of periodic orbits are dense in $U$ (Lemma 5.6(b)), so $y^2\le1$ on $U$. If $y(x)=\pm1$ at some $x\in U$, then $x$ is a local extremum of $y$, so $v\cdot\nabla y(x)=0$, while (7.2) gives $v\cdot\nabla y(x)=-(\alpha-1)|v(x)|^2/\sqrt{H(x)}<0$. So $f^2<H$ on $U$. $\square$

*Consequences.* By part 1, $f(z)=0$ at every stagnation point. So in Lemma 7.3 and Theorem E, $z\in Z_0$ if and only if $\zeta(z)=0$ and $\nabla f(z)=0$, and then $Dv(z)$ is symmetric and trace free. The solution vanishes identically on the interior of $Z$, so its support is $\overline U$. The first assertion $Z=S$ of Theorem G holds without assuming that $Z$ is finite. Both parts of Lemma 7.5 were first obtained by the referee (Section 15).

*Proof of Theorem E.* Combine the first assertion with Lemmas 7.2 and 7.3. $\square$

## 8. Conditional nonexistence, finite zero sets, the top end, analytic solutions, square integrability of $\theta$, the support of $d\tilde\theta$, and finite regularity

**Proof of Theorem F.**

*(F2).* Suppose the solution is nontrivial and (F2) holds. The set $K=Z\setminus N$ is compact and contained in $Z\setminus Z_0$. Cover it by finitely many sets $B_{z_i}$ from Lemma 7.1, and let $O=N\cup\bigcup_iB_{z_i}$. Then $H\ge h_0>0$ on $S^2\setminus O$. For $2\varepsilon<h_0$,
$$|\{\varepsilon\le H\le2\varepsilon\}|\le|\{x\in N:0<H\le2\varepsilon\}|+\sum_iC_i\sqrt{2\varepsilon}\le C\big((2\varepsilon)^\kappa+\sqrt{2\varepsilon}\big).$$
This contradicts Theorem C, because $\kappa>|\gamma|$ and $\frac12>|\gamma|$.

*(F1)* is the case $Z_0=\emptyset$ (take $N=\emptyset$).

*(F3).* Let $H\ge c\,d(\cdot,Z)^n$ on a neighbourhood $O$ of $Z$; then $H\ge h_0>0$ off $O$. For $s<h_0$, $\{0<H\le s\}\subset\{d(\cdot,Z)\le t\}$ with $t=(s/c)^{1/n}$.

- If $Z$ lies in a finite union of points and rectifiable curves of total length $\ell$, cover the curves by about $\ell/t$ balls of radius $2t$. This gives $|\{d(\cdot,Z)\le t\}|\le C(\ell t+t^2)$. Hence $|\{0<H\le s\}|\le Cs^{1/n}$, and Theorem C applies when $1/n>|\gamma|$, that is, $n<2\alpha/(\alpha-1)$.
- If $Z$ is finite, the bound is $Ct^2=Cs^{2/n}$, and Theorem C applies when $n<4\alpha/(\alpha-1)$.

For real-analytic data with $H\not\equiv0$, $Z$ is a compact analytic subset of $S^2$ of dimension at most one, hence a finite union of points and analytic arcs. Łojasiewicz's inequality gives $H\ge c\,d(\cdot,Z)^n$ for some $n$, and the first case applies if $n<2\alpha/(\alpha-1)$. (Theorem J below treats all analytic solutions without this restriction.)

*(F4)* follows from Theorem G.2 below. *(F5)* is Corollary 6.2. $\square$

**Proof of Theorem G.** Assume the solution is nontrivial and $Z$ is finite.

*Step 0.* A finite invariant set consists of fixed points, so $Z=S$. $\Psi(Z)$ is finite, and $m<M$ (Theorem C). Let $z$ satisfy $\Psi(z)=M$; the minimum is treated with $-\Psi$. Points where $\Psi=M$ are critical, so they lie in $Z$.

*Step 1 (surrounding orbits).* Choose $r_0>0$ small with $\bar B(z,r_0)\cap Z=\{z\}$. For $0<r\le r_0$, $m(r):=\max_{\partial B(z,r)}\Psi<M$. Let $c\in(m(r),M)$ with $c\notin\Psi(Z)$. Following a geodesic from $z$, $\Psi$ takes the value $c$ inside $B(z,r)$. Since $\Psi<c$ on $\partial B(z,r)$, every component $\Gamma$ of $\Psi^{-1}(c)$ meeting $B(z,r)$ lies in $B(z,r)\setminus\{z\}\subset U$, and it is a periodic orbit by Lemma 5.6.

By Lemma 5.7(d), the component $D$ of $S^2\setminus\Gamma$ contained in $B(z,r)$ meets $Z$, so $D\cap Z=\{z\}$. By the same argument, every periodic orbit in $B(z,r_0)\setminus\{z\}$ encloses $z$. Two such orbits are disjoint and nested, and they bound a closed annulus $A\subset U$. Since $d\theta=0$ on $U$, Stokes' theorem gives either $\oint_{\Gamma_1}\theta=\oint_{\Gamma_2}\theta$ or $\oint_{\Gamma_1}\theta=-\oint_{\Gamma_2}\theta$, depending on the flow orientations. The second option is impossible because both integrals are negative. So all of them equal $-p$ for one $p>0$.

*Step 2 ($z\in Z_0$).* Apply Theorem E to such a $\Gamma$ and its inner disk $D$, which meets $Z$ only at $z$.

*Step 3 ($f(z)=0$).* If $f(z)\ne0$, then $f$ has a fixed sign on a small $B(z,r)$, and $\int_0^Tf\,dt\ne0$ along an orbit $\Gamma\subset B(z,r)$. This contradicts Lemma 5.7(a).

*Step 4 ($Dv(z)=0$).* By Lemma 7.3 with $f(z)=0$, $\zeta(z)=0$, $\nabla f(z)=0$, and $A=Dv(z)$ is symmetric with trace zero. The index of $v$ at $z$ is $+1$: $v$ is tangent to the Jordan curve $\Gamma$, and $z$ is the only zero of $v$ inside it. If $A\ne0$, its eigenvalues are $\pm\lambda$ with $\lambda>0$, and $z$ would be a nondegenerate saddle of index $-1$. Hence $A=0$.

*Step 5 (quadratic part).* In chart coordinates centred at $z$, $v(h)=\frac12V(h)+o(|h|^2)$ with $V(h)=D^2v(z)[h,h]$. Suppose $V(h)\ne0$ for all $h\ne0$. Then on small circles $|h|=r$, $v$ and $V$ are homotopic through nonvanishing fields, because $|v-\frac12V|=o(r^2)$ while $|V|\ge cr^2$. So the index of $v$ at $z$ equals the degree of $V/|V|:S^1\to S^1$. Since $V(-h)=V(h)$, this map factors through the double cover $S^1\to\mathbb{RP}^1$, so its degree is even. This contradicts index $+1$.

*Step 6 ($H=O(r^4)$).* Near $z$ we have $f=O(r^2)$, $\nabla f=O(r)$, $v=O(r^2)$ and $\zeta=O(r)$, using $\zeta(z)=0$ and $\zeta\in C^1$. Hence $\eta^\sharp=O(r)$. Lemma 3.1(b) gives $|\nabla H|\le C r^3$, and integrating from $z$ gives $H\le Cr^4$.

*Step 7 (periods).* Let $\Gamma\subset B(z,\rho)$ be a periodic orbit around $z$ of period $T$, with inner disk $D\subset B(z,\rho)$. By Hölder's inequality with exponents $1/(1+\gamma)$ and $1/|\gamma|$, together with Lemma 5.7(b),
$$\frac p\alpha=\int_0^TH^{1+\gamma}dt\le\Big(\int_0^TH\,dt\Big)^{1+\gamma}T^{|\gamma|},\qquad \int_0^TH\,dt=\frac{\alpha-1}\alpha\Big|\int_D\zeta\,dS\Big|\le C\rho\cdot\rho^2 .$$
Hence $T\ge c\,\rho^{-3(1+\gamma)/|\gamma|}=c\,\rho^{-3(\alpha+1)/(\alpha-1)}$. $\square$

*Remark.* The bound of Step 7 is very strong: the exponent $3(\alpha+1)/(\alpha-1)$ exceeds $9$ on the whole interval. For a degenerate centre with $|v|\simeq r^2$ one expects periods of order $r^{-1}$. So the flow near $z$ must be extremely slow along part of each orbit, but the $C^2$ hypotheses do not exclude this.

**Proof of Proposition H.** Since $M$ is isolated in $\Psi(Z)$, there is $\delta>0$ with $(M-\delta,M)\cap\Psi(Z)=\emptyset$.

*Annuli.* The map $\Psi:\Psi^{-1}((M-\delta,M))\to(M-\delta,M)$ is a proper submersion, since preimages of compact subintervals are compact subsets of $U$. By Ehresmann's theorem and Lemma 5.6, the domain is a finite union of annuli $A_j$ foliated by the periodic orbits $\Gamma_{j,c}=A_j\cap\Psi^{-1}(c)$. These orbits are freely homotopic in $A_j\subset U$ with consistent flow orientation, so $\oint_{\Gamma_{j,c}}\theta=-p_j$ is constant, with $p_j>0$.

*Periods.* As $c\to M$, $\sup_{\{\Psi\ge c\}}H\to0$. Otherwise, by compactness there would be a point with $\Psi=M$ and $H>0$, which is impossible because maxima of $\Psi$ lie in $Z$. Hence
$$T(\Gamma_{j,c})\ge\frac{p_j}{\alpha}\big(\max_{\Gamma_{j,c}}H\big)^{-(1+\gamma)}\to\infty .$$

*Limits.* Let $c_n\to M$ and let $\Gamma_n=\Gamma_{j,c_n}\to K$ in the Hausdorff metric. Then $K$ is compact, connected, and contained in $\Psi^{-1}(M)\subset Z$. $K$ is invariant: if $x_n\in\Gamma_n$ and $x_n\to x$, then $\varphi_tx=\lim\varphi_tx_n\in K$.

*Stagnation point.* Suppose $K$ contains no zero of $v$. By the Poincaré-Bendixson theorem on $S^2$, the $\omega$-limit set of a point of $K$ is then a periodic orbit $\gamma_0\subset K$, of period $T_0$, say. Take $z_0\in\gamma_0$ and a short $C^1$ transversal $\Sigma$ through $z_0$. For large $n$, $\Gamma_n$ crosses $\Sigma$ at a point $x_n$ close to $z_0$. By continuous dependence and the flow box at $z_0$, the orbit of $x_n$ returns to $\Sigma$ at a time $t_n\to T_0$. A periodic orbit meets a transversal at most once (the monotonicity lemma of Poincaré-Bendixson theory, valid on $S^2$). So $t_n=T(\Gamma_n)$, which is bounded, contradicting $T(\Gamma_n)\to\infty$. $\square$

*Remark (not part of the results).* We expect that $K$ cannot be a hyperbolic polycycle. The idea: near hyperbolic saddles $H\le C\min(|x|,|y|)^2$ in linearizing coordinates, so the contribution of each passage to $\int H^{1+\gamma}dt$ tends to zero, which would contradict the constancy of $p_j$. We have not written a complete proof (it needs $C^1$ linearization and uniform passage estimates), and we do not claim it.

**Lemma 8.1 (speed nonuniformity on periodic orbits).** Let $\Gamma\subset U$ be a periodic orbit of length $\ell$ and period $T$. Let $\bar a=\ell^{-1}\oint_\Gamma|v|\,d\ell$ be the arclength mean of the speed and $\bar h=\ell/T$ its harmonic mean (so $\bar h\le\bar a$). Then
$$\Big(\frac{\bar h}{\bar a}\Big)^{|\gamma|}\ \le\ K_\alpha\,\frac{\ell\,\bar a^{1/\alpha}}{|\oint_\Gamma\theta|},\qquad K_\alpha=\alpha\Big(\frac{\alpha-1}{\alpha}\Big)^{1+\gamma}. \tag{8.1}$$

*Proof.* By Lemma 5.7(c), $|\oint_\Gamma\theta|=\alpha\int_0^TH^{1+\gamma}dt$. Hölder's inequality with exponents $1/(1+\gamma)$ and $1/|\gamma|$ gives $\int_0^TH^{1+\gamma}dt\le(\int_0^TH\,dt)^{1+\gamma}T^{|\gamma|}$. By Lemma 5.7(b), $\int_0^TH\,dt=\frac{\alpha-1}\alpha\int_0^T|v|^2dt=\frac{\alpha-1}\alpha\oint_\Gamma|v|\,d\ell=\frac{\alpha-1}\alpha\,\ell\bar a$. With $T=\ell/\bar h$ and $(1+\gamma)+|\gamma|=1$,
$$|\textstyle\oint_\Gamma\theta|\le K_\alpha\,\ell\,\bar a^{1+\gamma}\,\bar h^{-|\gamma|}.$$
Divide by $\bar a^{|\gamma|}$ and use $1+\gamma-|\gamma|=1+2\gamma=1/\alpha$. $\square$

So along any family of periodic orbits with $|\oint\theta|$ bounded below (for instance a family of mutually homotopic orbits in $U$) and $\ell\,\bar a^{1/\alpha}\to0$, the speed becomes extremely nonuniform: $\bar h/\bar a\le C(\ell\,\bar a^{1/\alpha})^{2\alpha/(\alpha-1)}$.

**Proof of Theorem I.** Suppose $r_0,c,D,m$ exist; reversing the orientation if necessary, $v_\varphi\ge c\,m(r)>0$ on $0<r<r_0$. Shrinking $r_0$, we may assume $r_0<\pi/2$ and $B(z,r_0)\setminus\{z\}\subset U$. Put $K=e^{2\pi/c^2}$.

*Step 1 (orbits near $z$).* On the punctured disk, $\dot\varphi=v_\varphi/\sin r>0$ and $|\dot r|\le|v|$. Hence
$$\Big|\frac{d\log r}{d\varphi}\Big|\le\frac{|v|\sin r}{r\,v_\varphi}\le c^{-2}.$$
Let $x$ be a periodic point with $d(x,z)<r_0/K$; by Theorem B such points are dense near $z$. Along its orbit, until $\varphi$ has increased by $2\pi$, $\log r$ changes by at most $2\pi/c^2$. So this arc stays in $B(z,r_0)$ and returns to the geodesic ray through $x$. That ray (inside $B(z,r_0)\setminus\{z\}$) is a transversal, since $v_\varphi>0$, and a periodic orbit meets a transversal arc in at most one point. So the arc closes up after exactly one turn. Thus the orbit $\Gamma$ of $x$ is a Jordan curve winding once around $z$, contained in an annulus $\rho/K\le r\le\rho$, where $\rho=\max_\Gamma r$.

*Step 2 (common $\theta$-period).* Two such orbits are disjoint Jordan curves around $z$ in $B(z,r_0)\setminus\{z\}\subset U$, both traversed with $\varphi$ increasing. They bound an annulus in $U$, so by Stokes' theorem they have the same value $\oint\theta=-p<0$.

*Step 3 (estimates).*

- Length: $\ell=\int_0^T|v|\,dt\le c^{-2}\int_0^Tv_\varphi\,dt=c^{-2}\int_0^{2\pi}\sin r\,d\varphi\le2\pi\rho/c^2$.
- Mean speed: $\bar a\le\max_\Gamma|v|\le m(\rho)/c$.
- Harmonic mean: $\bar h\ge\min_\Gamma|v|\ge c\,m(\rho/K)$. With $j=\lceil\log_2K\rceil$, applying the doubling inequality at the radii $\rho/2^i<r_0/2$ ($1\le i\le j$) and using that $m$ is nondecreasing gives $m(\rho)\le D^jm(\rho/2^j)\le D^jm(\rho/K)$. So $\bar h\ge c\,D^{-j}m(\rho)$.

Hence $\bar h/\bar a\ge c^2D^{-j}$. Inserting this into (8.1),
$$(c^2D^{-j})^{|\gamma|}\le K_\alpha\,\frac{2\pi\rho}{c^2}\Big(\frac{m(\rho)}{c}\Big)^{1/\alpha}\frac1p .$$
Letting $x\to z$ gives $\rho\to0$, with $m(\rho)\le m(r_0/2)$, which is a contradiction.

*The $C^k$ statement.* Let $j\le k$ be the degree of $V$, and suppose $\langle V(y),Jy\rangle\ne0$ for all $y\ne0$. Fix the orientation so that $c_V=\min_{|y|=1}\langle V(y),Jy\rangle>0$; then $\langle V(y),Jy\rangle\ge c_V|y|^{j+1}$ by homogeneity. In normal coordinates $r=|y|$, the vector field $\partial_\varphi$ is $Jy$, and the metric is $dr^2+\sin^2r\,d\varphi^2$. Hence $v_\varphi=\frac{\sin r}{r}\,\langle v,Jy/r\rangle_{\mathrm{eucl}}$ and $|v|\le|v|_{\mathrm{eucl}}$. Taylor's theorem gives $v=V+o(r^j)$ in these coordinates. So $v_\varphi\ge\frac{c_V}2r^j$ and $|v|\le Cr^j$ for small $r$. The hypothesis of the first part therefore holds with $m(r)=r^j$ and $D=2^j$. A real $2\times2$ matrix $A$ with $\langle Ay,Jy\rangle=0$ for some $y\ne0$ has $y$ as a real eigenvector, which gives the example. $\square$

*Remarks.*

- Theorem I applies in particular at the extremal points of $\Psi$ in Theorem G, and more generally at every isolated point of $Z$, with no finiteness assumption on $Z$. It complements Theorem G: a degenerate centre must have strongly nonuniform speed along its orbits. For $k=2$, Theorem G.3 gives the stronger conclusion $V(h)=0$ for some $h\ne0$, but only at extremal points of $\Psi$ when $Z$ is finite.
- Step 3 only needs, along a sequence of periodic orbits with a common value of $\oint\theta$, that $\inf\bar h/\bar a>0$ and $\ell\,\bar a^{1/\alpha}\to0$. Any centre with such a sequence of orbits is excluded by the same argument. We expect this to cover centres that rotate uniformly after a quasi-homogeneous rescaling, but we have not verified that such a rescaling preserves the two estimates in the original metric, so we do not claim it.

**Proof of Theorem J.** Throughout, $q=1+\gamma=\frac{\alpha+1}{2\alpha}$ and $r=q-\frac12=\frac1{2\alpha}$.

*Reduction to the local form.* Suppose that $v,f,P$ are real analytic on $S^2$ and that the solution is nontrivial. Then $H$ is analytic and not identically zero (Lemma 3.3), so $Z$ is a compact analytic subset of $S^2$, and it has finitely many connected components (Bierstone and Milman 1988, Corollary 2.7). $\Psi$ is constant on each of them (Theorem B.2), so $\Psi(Z)$ is finite and $M$ is isolated in $\Psi(Z)$. The local form applies with $W=S^2$ and gives a contradiction.

For the local form, assume that the solution is $C^2$ and nontrivial, that $M$ is isolated in $\Psi(Z)$, and that $v,f,P$ are analytic on an open set $W\supset L$, where $A$, $A_c=A\cap\{\Psi>c\}$ and $L$ are as in the statement. Write $\Gamma_c=A\cap\Psi^{-1}(c)$, the periodic orbit of Proposition H at level $c$. We derive a contradiction in seven steps.

*Step 1 (constant flux, localization).* By Proposition H and Lemma 5.7(c) there is $p>0$ with
$$\int_{\Gamma_c}H^q\,dt=\frac p\alpha\qquad(M-\delta<c<M), \tag{8.2}$$
where $dt$ is the time measure on the periodic orbit $\Gamma_c$. The sets $\overline{A_c}$ are compact, connected and decrease as $c$ increases, so $L$ is nonempty, compact and connected; since $\Psi=M$ on $L$ and points where $\Psi$ is maximal are critical, $L\subset Z$. For every open set $O\supset L$ there is $c_0<M$ with $\overline{A_{c_0}}\subset O$: otherwise there are $c_n\uparrow M$ and $z_n\in\overline{A_{c_n}}\setminus O$, and any limit point of $(z_n)$ lies in $L\setminus O$. Points of $L$ are limits of points of $A\subset U$, where $v\ne0$ (Lemma 7.5), so $v$ does not vanish identically on any connected open set meeting $L$.

*Step 2 (resolution).* For a vector field $V=V_1\partial_x+V_2\partial_y$ near $0\in\mathbb R^2$, the blow-up chart $x=\xi$, $y=\xi s$ carries the $\pi$-related field
$$\widehat V=V_1(\xi,\xi s)\,\partial_\xi+\frac{V_2(\xi,\xi s)-sV_1(\xi,\xi s)}{\xi}\,\partial_s, \tag{8.3}$$
which is analytic when $V$ is analytic and $V(0)=0$. Thus a point blow-up centred at a zero of an analytic field lifts the field to an analytic field (the other chart is symmetric).

**Lemma 8.2 (resolution).** Let $W'\Subset W$ be an open neighbourhood of $L$, chosen small enough. There are a real-analytic surface $\widetilde W$ and a proper analytic map $\pi:\widetilde W\to W'$, a composition of finitely many blow-ups of points, such that, with $\mathcal D=\pi^{-1}(Z\cap W')$:

- (R1) every point of $\mathcal D$ has analytic coordinates $(x,y)$ centred at it in which $\mathcal D$ is $\{y=0\}$ or $\{xy=0\}$;
- (R2) in such coordinates, the vector field $\hat v$ on $\widetilde W$ that is $\pi$-related to $v$ is analytic and equals $mX$, where $X$ is an analytic vector field with isolated zeros and $m=x^iy^ju$ with $u$ an analytic unit, $i,j\ge0$, and $i=0$ (resp. $j=0$) unless $\{x=0\}$ (resp. $\{y=0\}$) is contained in $\mathcal D$; moreover $\pi^*\mu=\varrho\,dx\wedge dy$ with $\varrho=x^{i'}y^{j'}u'$, $u'$ an analytic unit, and $i'>0$ (resp. $j'>0$) only if $\{x=0\}$ (resp. $\{y=0\}$) is an exceptional curve;
- (R3) at every zero of $X$, the linear part $DX$ has a nonzero eigenvalue;
- (R4) $\pi$ is an analytic diffeomorphism from $\widetilde W\setminus \mathcal D$ onto $W'\setminus Z$, and $m\ne0$, $X\ne0$ off $\mathcal D$.

The generator $X$ is determined by the chart only up to an analytic unit factor, which changes $m$ by the inverse factor. All statements below are local and insensitive to this choice; the foliation by orbits of the local generators is globally defined on $\widetilde W\setminus \mathcal D$ and on a neighbourhood of $\mathcal D$ off the zeros of $X$.

*Proof.* Every centre below is a zero of the current lift of $v$; by (8.3) the lift stays analytic, and since zeros of the lift lie over $S=Z$ (Lemma 7.5), $\pi$ is an isomorphism off $\pi^{-1}(Z)$. Near each point of $\overline{W'}$, factor $v=gX_0$, where $g$ is a greatest common divisor of the two components (the ring of convergent power series in two variables is factorial) and $X_0$ has an isolated zero or none. The factors are unique up to units, so they define a global saturated foliation and a scalar divisor $\{g=0\}$.

First, resolve the complexified divisor of $g$ by point blow-ups, together with the exceptional curves already created, into normal crossings (embedded resolution of plane curves; Bierstone and Milman 1997, (0.2)(2), Theorems 1.6 and 1.10). The centres can be taken on the strict transform of $\{g=0\}$, where the current lift vanishes, because the strict transform of a common factor of the components stays a factor of the lifted field. If two complex conjugate nonreal branches meet at a real point after this, one more real blow-up at that point separates their strict transforms from the real locus; afterwards only real branches pass through real points, so the coordinates in (R1) can be taken real. Second, blow up once each isolated point of $Z\cap\overline{W'}$ not yet blown up; there are finitely many, and afterwards $\pi^{-1}(Z\cap W')$ is a normal-crossing curve without isolated points. Third, apply Seidenberg's reduction to the saturated foliation (Seidenberg 1968; see Cano 2004, pp. 910-912; real version by complexification and conjugation-equivariant choice of centres, Dumortier 1977): finitely many further point blow-ups, centred at singular points of the foliation on $\mathcal D$, after which every singular point of the saturated generator has a linear part with a nonzero eigenvalue. Point blow-ups at points of a normal-crossing divisor preserve normal crossings, and a monomial $x^iy^j$ times a unit pulls back to a monomial times a unit (for example $x^iy^j=\xi^{i+j}s^j$ in the chart $x=\xi$, $y=\xi s$). Saturating the lifted generator removes only a power of the new exceptional coordinate, so the lift of $v$ is a monomial in the divisor coordinates times a unit times a saturated generator. This gives (R2) for $m$, and $i,j\ge0$ because the lift is analytic. For $\varrho$: the Jacobian of one point blow-up in the chart $x=\xi$, $y=\xi s$ is $\xi$, and analytic coordinate changes have unit Jacobians, so the product over the tower has the stated form. Zeros of $\hat v$, hence of $m$ and $X$, lie in $\mathcal D$, because $v\ne0$ off $Z$. Each construction is finite over a compact neighbourhood of $L$; shrinking $W'$ we obtain (R1)-(R4). $\square$

The referee (Section 15) checked that the order of the three constructions is legitimate and that only the weak conclusion (R3) of the reduction theorem is needed. Resolving only the real zero set would not suffice: the real zero set of $y(x^2+y^2)$ is the smooth line $\{y=0\}$, but this function is not a monomial times a unit there.

*Step 3 (the Euler bound).* Write $\widetilde H=H\circ\pi$, $\tilde f=f\circ\pi$, $\widetilde P=P\circ\pi$.

**Lemma 8.3.** Let $\mathcal B$ be a closed coordinate rectangle contained in a larger chart as in (R1)-(R2), and suppose that every component of $\mathcal D\cap\mathcal B$ is invariant under $X$. Then, for a constant $C$ depending on $\mathcal B$,
$$0\le\widetilde H\le Cm^2\quad\text{and hence}\quad\widetilde H^q\le C|m|\,\widetilde H^{\,r}\qquad\text{on }\mathcal B. \tag{8.4}$$
If $\mathcal D\cap\mathcal B=\{y=0\}$, then $\widetilde H\le Cy^2$ on $\mathcal B$; if $\mathcal D\cap\mathcal B=\{xy=0\}$, then $\widetilde H\le C\min(x^2,y^2)\le C|xy|$ on $\mathcal B$.

*Proof.* If $\{x=0\}\subset \mathcal D$ it is invariant, so $X^x=xe_1$ with $e_1$ analytic; similarly $X^y=ye_2$ if $\{y=0\}\subset \mathcal D$, and the same holds for every exceptional axis, since exceptional curves lie in $\mathcal D$. Hence $X(m)/m=ie_1+je_2+X(u)/u$ and $X(\varrho)/\varrho$ are bounded on $\mathcal B$ (terms for axes not in $\mathcal D$ are absent).

- Since $v\circ\pi=d\pi(mX)$ and $d\pi$ is bounded, $|v\circ\pi|\le C|m|$.
- Off $\mathcal D$, pulling back $\mathcal L_v\mu=(\operatorname{div}v)\mu$ gives $(\operatorname{div}v)\circ\pi\,\varrho\,dx\wedge dy=d(\iota_{mX}\varrho\,dx\wedge dy)$, that is,
$$(\operatorname{div}v)\circ\pi=m\Big(\operatorname{div}_0X+\frac{X(m)}m+\frac{X(\varrho)}\varrho\Big),$$
where $\operatorname{div}_0$ is the coordinate divergence. By continuity this holds on $\mathcal B$, so (E1) gives $|\tilde f|\le C|m|$.
- Let $g$ be the round metric and put $b=(\pi^*g)(X,\cdot)$, an analytic 1-form, and $s=b(X)=|d\pi X|^2$. Then $\pi^*v^\flat=mb$. For any vector field, $(\nabla_vv)^\flat=\mathcal L_vv^\flat-\frac12d|v|^2$. Using $\mathcal L_{mX}\sigma=m\mathcal L_X\sigma+\sigma(X)\,dm$ for 1-forms $\sigma$,
$$\mathcal L_{mX}(mb)=m^2\mathcal L_Xb+ms\,dm+mX(m)\,b,\qquad \tfrac12d(m^2s)=ms\,dm+\tfrac12m^2ds .$$
The terms with $dm$ cancel, so $\pi^*\big((\nabla_vv)^\flat\big)=m^2\big(\mathcal L_Xb-\frac12ds\big)+mX(m)\,b$, whose coefficients are $O(m^2)$. By (E3), $d\widetilde P=-\pi^*\big((\nabla_vv)^\flat\big)-(1-\alpha)\tilde f\,mb$, so the coefficients of $d\widetilde P$ are $O(m^2)$.
- $\widetilde P=0$ on $\mathcal D$ by Lemma 7.5. If $\{y=0\}\subset \mathcal D$, integrate the $dy$ coefficient of $d\widetilde P$ from $(x,0)$: $|\widetilde P(x,y)|\le C|x|^{2i}\int_0^{|y|}t^{2j}\,dt\le Cm(x,y)^2$, using the lower bound for $|u|$. If only $\{x=0\}\subset \mathcal D$, integrate in $x$.

Hence $\widetilde H=|v\circ\pi|^2+\tilde f^2+2\widetilde P\le Cm^2$, and $\widetilde H^q=\widetilde H^{1/2}\widetilde H^{\,r}\le C|m|\widetilde H^{\,r}$. For the last assertion: $\widetilde H\ge0$ is $C^2$ and vanishes on $\mathcal D$, so $\widetilde H$ and $\nabla\widetilde H$ vanish on each axis contained in $\mathcal D$, and Taylor's formula in the normal direction gives $\widetilde H\le C\,\mathrm{dist}(\cdot,\text{axis})^2$. $\square$

If $t\mapsto\varphi_tx$ is an orbit arc of $v$ in $U\cap W'$ and $\tilde x(t)=\pi^{-1}(\varphi_tx)$, then $\dot{\tilde x}=m(\tilde x)X(\tilde x)$, so the local $X$-time $\tau$ satisfies $d\tau/dt=m$, and for positive measures
$$\int H^q\,dt=\int\frac{\widetilde H^q}{|m|}\,|d\tau|. \tag{8.5}$$

*Step 4 (the lifted limit set).* Choose $W''\Subset W'$ containing $L$, and $c_0$ with $\overline{A_{c_0}}\subset W''$ (Step 1). For $c_0\le c<M$ let $K_c$ be the closure of $\pi^{-1}(A_c)$ and $\widetilde\Gamma_c=\pi^{-1}(\Gamma_c)$, a periodic leaf of the foliation in $\widetilde W\setminus \mathcal D$. The $K_c$ are compact (they lie in $\pi^{-1}(\overline{A_{c_0}})$ and $\pi$ is proper), connected (by (R4)) and decreasing, so $\widetilde L=\bigcap_cK_c$ is nonempty, compact and connected, and $\widetilde L\subset\pi^{-1}(L)\subset \mathcal D$.

- (a) For every open $O\supset\widetilde L$, $\widetilde\Gamma_c\subset O$ for $c$ close to $M$ (as in Step 1), and every point of $\widetilde L$ is a limit of points of $\widetilde\Gamma_{c_n}$ with $c_n\to M$.
- (b) $\widetilde L$ is invariant under the local flow of every local generator $X$: flow approximating points of $\widetilde\Gamma_{c_n}$ for a fixed small time; they stay on their leaves, and the limits lie in every $K_c$.
- (c) (Transversals.) Let $F=\Psi\circ\pi$. On $\widetilde W\setminus \mathcal D$, $dF\ne0$ and $dF(X)=0$, because $d\Psi\ne0$ and $d\Psi(v)=0$ on $U$. So if $\sigma$ is a $C^1$ arc in $\widetilde W\setminus \mathcal D$ transverse to $X$, then $F\circ\sigma$ is strictly monotone, and $\sigma$ meets each $\widetilde\Gamma_c$ (a subset of $F^{-1}(c)$) at most once.
- (d) $\widetilde L$ is not a point. Suppose $\widetilde L=\{\tilde z\}$. Take a coordinate disk $N$ centred at $\tilde z$ in which $X$ has no zero other than possibly $\tilde z$, and in which $\mathcal D$ consists of one or two axes reaching $\partial N$. For $c$ close to $M$, $\widetilde\Gamma_c$ lies in the interior of $N$ and bounds a disk in $N$, which contains a zero of $X$ by the index theorem; so $\tilde z$ lies inside $\widetilde\Gamma_c$. An axis arc from $\tilde z$ to $\partial N$ then meets $\widetilde\Gamma_c$, which is impossible since $\widetilde\Gamma_c\cap \mathcal D=\emptyset$.
- (e) If $\tilde z\in \mathcal D$ and $X(\tilde z)$ is transverse to a branch $\mathcal D_1$ of $\mathcal D$ through $\tilde z$, then $\tilde z\notin\widetilde L$. Indeed, in a flow box around $\tilde z$, $\mathcal D_1$ is a transversal, and every local orbit through a smaller neighbourhood $N_1$ of $\tilde z$ meets $\mathcal D_1$. A leaf $\widetilde\Gamma_c$ is disjoint from $\mathcal D$ and invariant, so it misses $N_1$, contradicting (a).

*Step 5 (local structure of $\widetilde L$).* Let $\tilde z\in\widetilde L$.

*Regular points.* If $X(\tilde z)\ne0$, the local orbit through $\tilde z$ lies in $\widetilde L\subset \mathcal D$ by (b), hence in one analytic branch of $\mathcal D$, which is therefore invariant. A second branch through $\tilde z$ would be transverse to $X(\tilde z)$, which (e) excludes. Choose analytic flow-box coordinates on a closed rectangle $\mathcal B=[-d_1,d_1]\times[-d_2,d_2]$ around $\tilde z$ with
$$X=\partial_x,\qquad \mathcal D\cap\mathcal B=\{y=0\}. \tag{8.6}$$
A new defining function of the same smooth branch differs from the old one by a unit, so (R2) holds in these coordinates.

*Singular points.* Let $X(\tilde z)=0$, and take a chart around $\tilde z$ in which $\tilde z$ is the only zero of $X$. By (d) and connectedness, $\widetilde L$ contains points arbitrarily close to $\tilde z$ other than $\tilde z$. They are regular, so they lie on invariant branches of $\mathcal D$ through $\tilde z$ (for a small chart). Choose coordinates in which an invariant branch is $\{y=0\}$:
$$X=\hat a_1(x,y)\,\partial_x+y\,\hat b_1(x,y)\,\partial_y,\qquad \hat a_1(x,0)=a_0x^k(1+O(x)),\ a_0\ne0,\ k\ge1,$$
where $\hat a_1(\cdot,0)\not\equiv0$ because the zero is isolated. The eigenvalues $\lambda=\partial_x\hat a_1(0)$ and $\mu=\hat b_1(0)$ are real, and $(\lambda,\mu)\ne(0,0)$ by (R3).

We claim that a second branch of $\mathcal D$ passes through $\tilde z$ and is invariant. Suppose not. Then near $\tilde z$, $\widetilde L\subset\{y=0\}$. Take a rectangle $N=[-d_1,d_1]\times[-d_2,d_2]$ in the chart, with $d_1$ small and then $d_2$ small enough that $\hat a_1$ has the sign of $a_0(\pm d_1)^k$ on the vertical sides $\{x=\pm d_1\}$, which are transverse to $X$ off $\mathcal D$. For every $\varepsilon\in(0,d_2)$, by compactness and (a), the leaves $\widetilde\Gamma_c$ with $c$ close to $M$ meet $N$ only in $\{|y|<\varepsilon\}$. A whole leaf cannot lie in $N$: it would lie in one of the half-rectangles $\{\pm y>0\}$, where $X$ has no zero, contradicting the index theorem. So every component of $\widetilde\Gamma_c\cap N$ that is not a single point is an orbit arc entering $N$ through one vertical side and leaving through a vertical side; the horizontal sides are not reached since $\varepsilon<d_2$, and $\mathcal D$ is not reached since the leaf is compact and disjoint from $\mathcal D$.

- If $k$ is odd, $X$ points into $N$ on both vertical sides (if $a_0<0$) or out of $N$ on both (if $a_0>0$), so no such arc exists.
- If $k$ is even, then $\lambda=0$, so $\mu\ne0$. The strong stable manifold (if $\mu<0$) or strong unstable manifold (if $\mu>0$) of $\tilde z$ is a $C^1$ invariant curve tangent to the $\mu$-eigenvector, which is transverse to $\{y=0\}$; near $\tilde z$ it is a graph $x=h(y)$ with $h(0)=0$. Take $\varepsilon$ so small that $|h(y)|<d_1/2$ for $|y|\le\varepsilon$. The two vertical sides now have the same horizontal flow direction, so an entrance-exit arc runs from one vertical side to the other within one half-strip, and $x-h(y)$ changes sign along it. So the arc meets the strong manifold, and by uniqueness the leaf would be contained in it; but the points of that curve other than $\tilde z$ converge to $\tilde z$ in one time direction, so it contains no periodic leaf.

In both cases the leaves with $c$ close to $M$ miss a neighbourhood of $\tilde z$, contradicting (a). This proves the claim. So $\tilde z$ is a corner of two invariant branches of $\mathcal D$, and in suitable coordinates
$$X=x\,\hat a(x,y)\,\partial_x+y\,\hat b(x,y)\,\partial_y,\qquad(\hat a(0),\hat b(0))=(\lambda,\mu)\ne(0,0). \tag{8.7}$$

*Step 6 (number of passages).* Consider one closed quadrant of (8.7), after reflection $\mathcal Q=[0,d_1]\times[0,d_2]$ with $d_1,d_2\le1$, and its outer sides $\Sigma_1=\{y=d_2,\ 0<x\le d_1\}$ and $\Sigma_2=\{x=d_1,\ 0<y\le d_2\}$, which lie off $\mathcal D$. Suppose first $\mu\ne0$. Choose $d_1,d_2$ so small that $\hat b$ has the sign of $\mu$ and $|\hat b|\ge|\mu|/2$ on $\mathcal Q$, and that $\hat a$ has the sign of $\lambda$ on $\mathcal Q$ if $\lambda\ne0$. If $\lambda=0$, note that $\hat a(x,0)\ne0$ for small $x>0$ (otherwise $X$ would vanish on a segment of $\{y=0\}$); fix such a $d_1$, then choose $d_2$ so small that $\hat a(d_1,y)$ has the sign of $\hat a(d_1,0)$ for $0\le y\le d_2$. Then $\Sigma_1$ and $\Sigma_2$ are transversals with fixed crossing directions, and $y$ is strictly monotone along orbits in the interior of $\mathcal Q$. If $\mu=0$, then $\lambda\ne0$, and we exchange the roles of $x$ and $y$.

A whole leaf cannot lie in $\mathcal Q$, since a coordinate is strictly monotone along orbits there. For a fixed leaf, compactness and disjointness from $\mathcal D$ exclude endpoints on the axes. So every component of $\widetilde\Gamma_c\cap\mathcal Q$ other than a single point is an orbit arc from a point of $\Sigma_1\cup\Sigma_2$ where $X$ points into $\mathcal Q$ to a point where it points out. If $\Sigma_1$ and $\Sigma_2$ are both inward or both outward, there is no such arc. Otherwise exactly one of them is inward, every arc starts on it, and by Step 4(c) there is at most one arc. (A single point of contact at the corner $(d_1,d_2)$ carries no time.)

In a flow box (8.6), the leaves with $c$ close to $M$ meet $\mathcal B$ only in $\{0<|y|<d_2\}$, by compactness and Step 4(a). Along $X=\partial_x$ the coordinate $x$ increases, so each component of $\widetilde\Gamma_c\cap\mathcal B$ enters through $\{x=-d_1\}$ and has $X$-duration $2d_1$. The entrance side consists of the two transversals $\{x=-d_1,\ 0<\pm y\le d_2\}$, so by Step 4(c) there are at most two components.

*Step 7 (passage estimates and conclusion).* For a flow box $\mathcal B$ let $\varepsilon_c(\mathcal B)$ be the supremum of $|y|$ over $\widetilde\Gamma_c\cap\mathcal B$; for a quadrant $\mathcal Q$ let $\varepsilon_c(\mathcal Q)$ be the supremum of $\min(x,y)$ over $\widetilde\Gamma_c\cap\mathcal Q$ (zero if the intersection is empty). Since the boxes lie in larger charts and every limit point of the leaves $\widetilde\Gamma_c$ as $c\to M$ lies in $\widetilde L\subset\mathcal D$,
$$\varepsilon_c(\mathcal B)\to0,\qquad\varepsilon_c(\mathcal Q)\to0\qquad(c\to M). \tag{8.8}$$

By (8.4) and (8.5), the integrand $\widetilde H^q/|m|$ is at most $C\widetilde H^{\,r}$, hence at most $C|y|^{2r}=C|y|^{1/\alpha}$ in a flow box and at most $C(xy)^r$ in a quadrant. In a flow box the contribution of $\widetilde\Gamma_c$ to $\int_{\Gamma_c}H^q\,dt$ is therefore at most $4d_1C\,\varepsilon_c(\mathcal B)^{1/\alpha}$.

In a quadrant with $\mu<0$ (so $\hat b\le-|\mu|/2$ on $\mathcal Q$, and $y$ decreases along orbits), put $K_0=\sup_{\mathcal Q}|\hat a|$,
$$\nu=\min\Big(r,\frac{r|\mu|}{4K_0}\Big)\ (\nu=r\text{ if }K_0=0),\qquad w=x^\nu y^r,\qquad\kappa=\frac{r|\mu|}4 .$$
On the interior of $\mathcal Q$, $X(\log w)=\nu\hat a+r\hat b\le\nu K_0-\frac{r|\mu|}2\le-\kappa$, and $(xy)^r\le w$ because $x\le1$ and $\nu\le r$. If there is a passage, it enters through $\Sigma_1$ at a point $(x_0,d_2)$, and $x_0\le\varepsilon_c(\mathcal Q)$ as soon as $\varepsilon_c(\mathcal Q)<d_2$. Along the passage, parametrized by $X$-time from its entrance, $w(\tau)\le w(0)\exp(-\kappa\tau)$, so its contribution is at most
$$C\int_0^\infty x_0^\nu d_2^{\,r}\exp(-\kappa\tau)\,d\tau\le\frac C\kappa\,\varepsilon_c(\mathcal Q)^\nu,$$
independently of the duration of the passage. If $\mu>0$, then $X(\log w)\ge\kappa$, the passage leaves through $\Sigma_1$, and integrating backwards from the exit point gives the same bound. If $\mu=0$, exchange $x$ and $y$ (then $\lambda\ne0$).

Cover $\widetilde L$ by the interiors of finitely many flow boxes and corner neighbourhoods, each corner neighbourhood being the union of four quadrants. By Step 4(a), for $c$ close to $M$ the leaf $\widetilde\Gamma_c$ lies in the union. Summing the nonnegative contributions,
$$\frac p\alpha=\int_{\Gamma_c}H^q\,dt\le\sum_{\text{boxes}}C_{\mathcal B}\,\varepsilon_c(\mathcal B)^{\rho_{\mathcal B}}\longrightarrow0\qquad(c\to M),$$
with finitely many constants $C_{\mathcal B}$ and exponents $\rho_{\mathcal B}>0$ independent of $c$. This contradicts $p>0$. $\square$

*Remarks.*

- The proof of the local form uses analyticity only through Lemma 8.2. It applies verbatim to any $C^2$ solution for which $M$ is isolated in $\Psi(Z)$ and a map $\pi$ with (R1)-(R4) exists over a neighbourhood of $L$, with $X$, $m$ and $\varrho$ of class $C^1$, the units bounded away from zero, and the local structure of Step 5 (isolated zeros of $X$, analytic continuation of invariance along a branch of $\mathcal D$, and $\hat a_1(\cdot,0)$ with an isolated zero of finite order). We do not know an Euler-specific way to produce such a map for $C^2$ or $C^\infty$ data.
- The proof does not need the remark after Proposition H on hyperbolic polycycles: at the top level all limits lie in $Z$, and after resolution the passages near corners are controlled by the weight $w$.
- The round metric enters only through the boundedness of $\pi^*g$, of $d\pi$, and of the coefficients in Lemma 8.3. The arguments of Theorems A and B, Proposition H, Lemma 7.5 and Theorem J never use the value of the curvature, so the same conclusion holds for the system (E1)-(E3) written with the Levi-Civita connection and area form of any real-analytic metric on $S^2$. We state this only as an observation; the referee's audit concerned the round metric.

**Proof of Theorem L.** Throughout, the solution is nontrivial. By Lemma 7.5, $v=f=0$ on $Z$ and $f^2<H$ on $U$. We write $d=\mathrm{dist}(\cdot,Z)$, which is 1-Lipschitz.

**Lemma 8.4 (a scalar inequality).** Let $g\in C^2(S^2)$ and $1<\rho<2$. Then $\nabla g=0$ almost everywhere on $\{g=0\}$, and
$$\int_{\{g\ne0\}}|g|^{\rho-2}|\nabla g|^2\,dS\ \le\ \frac1{\rho-1}\int|g|^{\rho-1}|\Delta g|\,dS<\infty .$$

*Proof.* Near a point of $\{g=0,\ \nabla g\ne0\}$ this set is a $C^1$ curve, so $\{g=0,\ \nabla g\ne0\}$ is a countable union of null sets. For $\delta>0$ let $\Phi_\delta(t)=(t^2+\delta^2)^{\rho/2}$. Then
$$\Phi_\delta''(t)=\rho\,(t^2+\delta^2)^{\rho/2-2}\big(\delta^2+(\rho-1)t^2\big)\ge\rho(\rho-1)(t^2+\delta^2)^{(\rho-2)/2},\qquad|\Phi_\delta'(t)|=\rho|t|(t^2+\delta^2)^{(\rho-2)/2}\le\rho|t|^{\rho-1},$$
using $\rho-1\le1$ and $\rho-2<0$. Since $\Phi_\delta\circ g\in C^2$, integration by parts on the closed sphere gives $\int\Phi_\delta''(g)|\nabla g|^2=-\int\Phi_\delta'(g)\Delta g$. Hence $\rho(\rho-1)\int(g^2+\delta^2)^{(\rho-2)/2}|\nabla g|^2\le\rho\int|g|^{\rho-1}|\Delta g|$. As $\delta\downarrow0$ the integrand increases to $|g|^{\rho-2}|\nabla g|^2$ on $\{g\ne0\}$, and monotone convergence gives the claim. $\square$

**Lemma 8.5 (Lipschitz test functions).** If $g:S^2\to\mathbb R$ is Lipschitz and $\operatorname{supp}g$ is a compact subset of $U$, then $\int_Udg\wedge\theta=0$.

*Proof.* Choose an open set $O$ with $\operatorname{supp}g\subset O$ and $\overline O\subset U$ compact. Using a finite partition of unity and mollification in charts, there are smooth $g_k$ supported in $\overline O$ with $g_k\to g$ uniformly, $\sup_k\|dg_k\|_\infty<\infty$ and $dg_k\to dg$ almost everywhere. For each $k$, $g_k\theta$ is a $C^1$ form with compact support in $U$, so $\int dg_k\wedge\theta=\int d(g_k\theta)=0$, because $d\theta=0$ on $U$. Since $\theta$ is bounded on $\overline O$, dominated convergence gives the claim. $\square$

**Lemma 8.6 (capacity).**
1. If $K$ has capacity zero and $V\supset K$ is open, then for every $\varepsilon>0$ there is a Lipschitz $\phi:S^2\to[0,1]$ with $\phi=1$ near $K$, $\operatorname{supp}\phi$ a compact subset of $V$, and $\int|\nabla\phi|^2<\varepsilon$. Compact subsets of sets of capacity zero have capacity zero.
2. Countable compact sets have capacity zero.
3. A connected compact set $K$ with more than one point does not have capacity zero.

*Proof.* 1. Let $\chi$ be Lipschitz with values in $[0,1]$, $\chi=1$ near $K$ and compact support in $V$. If $\phi_n$ are as in the definition with $\int(|\nabla\phi_n|^2+\phi_n^2)\to0$, then $\chi\phi_n$ has the required properties for large $n$, since $\|\nabla(\chi\phi_n)\|_2\le\|\nabla\phi_n\|_2+\|\nabla\chi\|_\infty\|\phi_n\|_2$. The second sentence is immediate from the definition.

2. For a point $z$ and $0<r<R<\pi/2$, let $\phi=1$ on $B(z,r)$, $\phi=\log(R/d(\cdot,z))/\log(R/r)$ on $B(z,R)\setminus B(z,r)$, and $\phi=0$ elsewhere. Then $\int|\nabla\phi|^2=\frac{2\pi}{\log^2(R/r)}\int_r^R\frac{\sin s}{s^2}\,ds\le\frac{2\pi}{\log(R/r)}$ and $\int\phi^2\le|B(z,R)|$; both are small when $R$ is small and $r\ll R$. If $K=\{z_1,z_2,\dots\}$ is compact and $\varepsilon>0$, choose such $\phi_i$ for $z_i$ with $\int(|\nabla\phi_i|^2+\phi_i^2)<2^{-i}\varepsilon$ and $\phi_i=1$ on an open set $O_i\ni z_i$. Finitely many $O_i$ cover $K$, and the maximum $\phi$ of the corresponding $\phi_i$ is Lipschitz, equals $1$ near $K$, and satisfies $|\nabla\phi|^2+\phi^2\le\sum_i(|\nabla\phi_i|^2+\phi_i^2)$ almost everywhere.

3. Let $a\ne b$ be points of $K$, $\delta=d(a,b)\le\pi$, and let $\phi$ be Lipschitz with values in $[0,1]$ and $\phi=1$ near $K$. For $0<s<\delta$ the circle $C_s=\partial B(a,s)$ separates $a$ from $b$, so it meets $K$ and $\max_{C_s}\phi=1$. If $\min_{C_s}\phi\le\frac12$, then $\int_{C_s}|\nabla\phi|\,d\ell\ge\frac12$ and, by Cauchy-Schwarz, $\int_{C_s}|\nabla\phi|^2d\ell\ge\frac1{4\cdot2\pi\sin s}\ge\frac1{8\pi}$. Otherwise $\int_{C_s}\phi^2d\ell\ge\frac{2\pi\sin s}4$. Integrating over $s\in[\delta/4,\delta/2]$ in geodesic polar coordinates gives $\int(|\nabla\phi|^2+\phi^2)\ge\frac\delta4\min\big(\frac1{8\pi},\frac\pi2\sin\frac\delta4\big)>0$, independently of $\phi$. $\square$

*Item 1.* Fix $\lambda\in[0,\lambda_*)$ and put $e=2\gamma-2\lambda$. Since $2\gamma-2\lambda_*=-\frac12$, we have $-\frac12<e\le2\gamma<0$. On $U$, $H^{-2\lambda}|\theta|^2=H^e|\eta|^2\le2H^e\big((\alpha-1)^2|v|^2+|\nabla f|^2\big)$.

For the first term, let $\varepsilon>0$ and $w_\varepsilon=(H+\varepsilon)^e\in C^2(S^2)$. By Lemma 3.2 and (T1),
$$\operatorname{div}(w_\varepsilon fv)=w_\varepsilon\big[\alpha H-(\alpha-1)|v|^2-b_\varepsilon f^2\big],\qquad b_\varepsilon=(2-\alpha)-2\alpha e\,\frac H{H+\varepsilon}\ \ge\ 2-\alpha .$$
Integrating over $S^2$ gives $(\alpha-1)\int w_\varepsilon|v|^2\le\alpha\int w_\varepsilon H$. Both integrands vanish on $Z$; on $U$, $w_\varepsilon H\le H^{1+e}$ and $w_\varepsilon\to H^e$ as $\varepsilon\to0$. By Fatou's lemma,
$$(\alpha-1)\int_UH^e|v|^2\,dS\ \le\ \alpha\int_UH^{1+e}\,dS<\infty,$$
since $1+e>0$.

For the second term, apply Lemma 8.4 with $g=f$ and $\rho=2+2e\in(1,2)$. On $U\cap\{f\ne0\}$ we have $0<f^2<H$, and $e<0$, so $H^e<|f|^{2e}=|f|^{\rho-2}$. On $\{f=0\}$, $\nabla f=0$ almost everywhere. Hence $\int_UH^e|\nabla f|^2\le\int_{\{f\ne0\}}|f|^{\rho-2}|\nabla f|^2<\infty$. This proves item 1.

*Item 2.* Since $\Gamma\subset U$, $K=Z\cap D=Z\cap\overline D$ is compact. We may take the boundary curves of $N$ smooth. Choose a smooth $\psi:S^2\to[0,1]$ with $\psi=1$ on $D\setminus N$ and $\psi=0$ on $S^2\setminus(D\cup N)$. Then $d\psi$ is supported in $N$, and Stokes' theorem for the closed form $\theta$ on $N$ gives
$$\int d\psi\wedge\theta=\int_Nd(\psi\theta)=\pm\oint_{\Gamma'}\theta=\pm\oint_\Gamma\theta\ne0,$$
where $\Gamma'$ is the boundary curve of $N$ in $D$ (on the other boundary curve $\psi=0$), which is homotopic to $\Gamma$ in $N$; the last inequality is Lemma 5.7(c).

Let $\phi$ be as in item 2 and put $g=\psi(1-\phi)$. Since $1-\phi$ vanishes on an open set $O\supset K$, the support of $g$ lies in the compact set $(D\cup N)\setminus O$, which is disjoint from $Z$; so Lemma 8.5 applies. Since $d\psi=0$ on the support of $\phi$, $dg=d\psi-\psi\,d\phi$, and
$$0=\int_Udg\wedge\theta=\int d\psi\wedge\theta-\int_U\psi\,d\phi\wedge\theta .$$
By Cauchy-Schwarz, $\big|\oint_\Gamma\theta\big|\le\big(\int_UH^{2\lambda}|\nabla\phi|^2\big)^{1/2}\big(\int_UH^{-2\lambda}|\theta|^2\big)^{1/2}$, and the last factor is finite by item 1. This gives item 2 with $c=|\oint_\Gamma\theta|^2/\int_UH^{-2\lambda}|\theta|^2$. If $K$ had capacity zero, Lemma 8.6.1 with $V=D\setminus N$, which is open and contains $K$, would give admissible $\phi$ with $\int|\nabla\phi|^2$ arbitrarily small, contradicting the case $\lambda=0$.

*Item 3.* If $Z$ has capacity zero, so does $Z\cap D$ for every $D$ as in item 2 (Lemma 8.6.1). A nontrivial solution has $U\ne\emptyset$ and therefore a periodic orbit in $U$ (Lemma 5.6(c)), which contradicts item 2. Countable compact sets have capacity zero (Lemma 8.6.2).

*Item 4.* Let $A$, $A_c=A\cap\{\Psi>c\}$, $\Gamma_c$ and $L$ be as in Theorem J, with $M-\delta<c<M$. Since $\Psi$ restricted to $A$ is a proper submersion onto $(M-\delta,M)$, the closure of $A_c$ is $A_c\cup\Gamma_c\cup L$. The connected set $A_c$ lies in one component $D_c^+$ of $S^2\setminus\Gamma_c$, and the points of $D_c^+$ close to $\Gamma_c$ lie in $A_c$ (a collar of $\Gamma_c$ in $A$ has one side in $A_c$ and the other in $\{\Psi<c\}$). Let $R=D_c^+\setminus A_c$. Then $R$ is closed: a limit point of $R$ is not in the open set $A_c$, and it is not on $\Gamma_c=\partial D_c^+$ by the collar property, so it lies in $D_c^+\setminus A_c$. Moreover the topological boundary of $R$ lies in $L$: if $x\in R$ and every neighbourhood of $x$ meets $A_c$ (small neighbourhoods lie in $D_c^+$), then $x\in\overline{A_c}\setminus(A_c\cup\Gamma_c)\subset L$.

Suppose $L=\{z\}$. Then every point of $R\setminus\{z\}$ is an interior point of $R$, so $R\setminus\{z\}$ is open and closed in the connected set $S^2\setminus\{z\}$. It is not all of $S^2\setminus\{z\}$, because $\Gamma_c\not\subset R$, so $R\subset\{z\}$. Since $A_c\subset U$, $Z\cap D_c^+\subset R\subset\{z\}$, a set of capacity zero; this contradicts item 2 for $\Gamma=\Gamma_c$ and $D=D_c^+$. So $L$ has more than one point; it is compact, connected and contained in $Z$ by Step 1 of the proof of Theorem J.

*Item 5.* Choose $N$ as in item 2 and let $d_0>0$ be smaller than $\mathrm{dist}(\Gamma,Z)$ and than the minimum of $d$ on $N$. For $n>2/d_0$ let $\chi_n=\min(1,\max(0,nd-1))$, and let $\phi_n=1-\chi_n$ on $D$ and $\phi_n=0$ off $D$. Since $\chi_n=1$ on $\{d\ge2/n\}$, which contains a neighbourhood of $\Gamma$ and the set $N$, $\phi_n$ is Lipschitz, its support lies in $D\setminus N$, and $\phi_n=1$ on $D\cap\{d<1/n\}$, an open set containing $Z\cap D$. Moreover $|\nabla\phi_n|\le n$ almost everywhere, and $\nabla\phi_n=0$ almost everywhere outside $D\cap S_n$, $S_n=\{1/n<d<2/n\}$.

Suppose $H\le C\,d^k$ on $D$ with $k>4\alpha/(2-\alpha)$, and put $\lambda=1/k<\lambda_*$. Since $nd<2$ on $S_n$,
$$\int_UH^{2\lambda}|\nabla\phi_n|^2\le C^{2\lambda}n^2\int_{D\cap S_n}d^2\,dS\le4C^{2\lambda}\,|D\cap S_n|\longrightarrow0,$$
because the sets $S_n$ are contained in $\{0<d<2/n\}$, which decrease to the empty set. This contradicts item 2.

If $Z\cap D$ lies in finitely many points and rectifiable curves of total length $\ell$ and $k>2\alpha/(2-\alpha)$, choose $\lambda<\lambda_*$ with $2\lambda k>1$. A segment from a point of $D$ to a point of $Z\setminus D$ crosses $\Gamma$, so for $r<\mathrm{dist}(\Gamma,Z)$ the set $\{x\in D:d(x)<r\}$ lies in the $r$-neighbourhood of $Z\cap D$, whose area is at most $C'(\ell r+r^2)$ (proof of (F3)). Hence
$$\int_UH^{2\lambda}|\nabla\phi_n|^2\le C^{2\lambda}n^2\Big(\frac2n\Big)^{2\lambda k}\big|\{x\in D:d(x)<2/n\}\big|\le C''n^{1-2\lambda k}\longrightarrow0,$$
again contradicting item 2. $\square$

*Remarks.*

- (Theorem I.) Under the hypothesis of Theorem I, Step 1 of its proof gives a periodic orbit $\Gamma\subset B(z,r_0)\setminus\{z\}\subset U$ winding once around $z$. The component of $S^2\setminus\Gamma$ containing $z$ lies in $B(z,r_0)$, so it meets $Z$ only at $z$, which contradicts Theorem L.2. Lemma 8.1 is not needed for this.
- (Sharpness of item 2.) The proof of item 2 for $\lambda=0$ uses only that $\theta$ is a closed $C^1$ form on $U$, that $\tilde\theta\in L^2$, and that $\int d\psi\wedge\theta\ne0$. These properties alone do not exclude sets $Z\cap D$ of positive capacity. Let $K_1,K_2\subset S^2$ be disjoint compact sets, neither of capacity zero, and $V=S^2\setminus(K_1\cup K_2)$. Let $\mathcal A$ be the affine set of Lipschitz functions on $S^2$ equal to $1$ near $K_1$ and to $0$ near $K_2$, let $\mathcal V$ be the vector space of Lipschitz functions vanishing near $K_1\cup K_2$ (so $\mathcal A+\mathcal V=\mathcal A$), and let $\kappa=\inf_{\phi\in\mathcal A}\int|\nabla\phi|^2$. Truncation to $[0,1]$ does not increase the energy, so $\kappa$ is also the infimum over $\phi\in\mathcal A$ with values in $[0,1]$. Then $\kappa>0$: otherwise there are $\phi_n\in\mathcal A$ with values in $[0,1]$ and $\int|\nabla\phi_n|^2\to0$; by Poincaré's inequality a subsequence converges in $W^{1,2}$ to a constant $c\in[0,1]$, and $(\phi_n-c)/(1-c)$ (if $c\ne1$) or $1-\phi_n$ (if $c=1$), truncated to $[0,1]$, shows that $K_1$ or $K_2$ has capacity zero. Now let $\phi_n\in\mathcal A$ be a minimizing sequence with values in $[0,1]$. Since $\frac12(\phi_n+\phi_m)\in\mathcal A$, the parallelogram law gives $\|\nabla\phi_n-\nabla\phi_m\|_2^2\le2\|\nabla\phi_n\|_2^2+2\|\nabla\phi_m\|_2^2-4\kappa\to0$, and with Poincaré's inequality (the means are bounded) a subsequence converges in $W^{1,2}$ to some $u$, with $\int|\nabla u|^2=\kappa$. For $h\in\mathcal V$ and $t\in\mathbb R$, $\phi_n+th\in\mathcal A$, so $\int|\nabla u+t\nabla h|^2\ge\kappa=\int|\nabla u|^2$; differentiating at $t=0$ gives $\int\langle\nabla u,\nabla h\rangle=0$. Taking $h\in C^\infty_c(V)$ shows that $u$ is weakly harmonic, hence smooth and harmonic, on $V$ (Weyl's lemma). Each $\nabla\phi_n$ vanishes on a neighbourhood of $K_1\cup K_2$, so $\nabla u=0$ almost everywhere on $K_1\cup K_2$, and $\omega=\star du$ is a closed smooth 1-form on $V$ with $\int_V|\omega|^2=\kappa$. For smooth $\psi\in\mathcal A$ one has $\psi-\phi_n\in\mathcal V$, so $\int_Vd\psi\wedge\omega=\int\langle\nabla\psi,\nabla u\rangle=\int\langle\nabla\phi_n,\nabla u\rangle\to\kappa$, that is, $\int_Vd\psi\wedge\omega=\kappa\ne0$. Choosing in addition $0\le\psi\le1$, the coarea formula gives $\int_Vd\psi\wedge\omega=\int_0^1\big(\int_{\{\psi=t\}}\omega\big)\,dt$, where for almost every $t\in(0,1)$ the level set $\{\psi=t\}$ is a finite union of smooth circles in $V$ (by Sard's theorem; $d\psi$ has compact support in $V$), oriented by $\mu$ and $d\psi$. Hence $\omega$ has a nonzero period on some circle $C\subset V$; by Stokes' theorem both components of $S^2\setminus C$ meet $K_1\cup K_2$. Here $K_1,K_2$ may be totally disconnected, for example Cantor sets of positive Hausdorff dimension, which have positive capacity (L. Carleson, *Selected problems on exceptional sets*, 1967). So excluding totally disconnected zero sets of positive capacity, or continua, needs more of the Euler structure than item 1.

**Proof of Theorem M.** Throughout, the solution is nontrivial, so Lemma 7.5 ($Z=S$, $v=f=P=0$ on $Z$, $f^2<H$ on $U$) and Theorem L.1 are available. Balls and distances are geodesic, $r_0\le1$ is smaller than a quarter of the injectivity radius, and $C$ denotes constants that depend only on $\alpha$ and the solution and may change from line to line.

*Item 1.* Let $z\in Z$. Then $v(z)=0$ and $f(z)=0$, so $\operatorname{tr}Dv(z)=\operatorname{div}v(z)=-(2-\alpha)f(z)=0$ and the eigenvalues of $Dv(z)$ are $\pm\kappa$ with $\kappa^2\in\mathbb R$. Suppose $\kappa>0$. Then $z$ is a hyperbolic saddle of the $C^2$ field $v$, and by the stable manifold theorem there is a nonstationary trajectory $x(t)$ with $d(x(t),z)\le Ce^{-\kappa t/2}$ for $t\ge0$. Since $v(x(0))\ne0$ and $Z=S$, $x(0)\in U$, and by (T1)
$$H(x(t))=H(x(0))\exp\Big(2\alpha\int_0^tf(x(s))\,ds\Big).$$
Since $|f(x(s))|\le C\,d(x(s),z)$ is integrable on $[0,\infty)$, the right side has a positive limit as $t\to\infty$, while the left side tends to $H(z)=0$. Hence $\kappa^2\le0$.

Now let $z\in Z_0$. Differentiating Lemma 3.1(b) at $z$, where $f=0$, $v=0$ and $\eta=-df$, gives
$$D^2H(z)=2\nabla f(z)\otimes\nabla f(z)-2\zeta(z)\,J\,Dv(z),\qquad\operatorname{tr}D^2H(z)=2|\nabla f(z)|^2+2\zeta(z)^2,$$
because $\operatorname{tr}(J\,Dv)=-\zeta$ in an oriented orthonormal frame. So $D^2H(z)=0$ forces $\nabla f(z)=0$ and $\zeta(z)=0$ (this is also part of Theorem E). Then $Dv(z)$ is symmetric, since $\zeta(z)$ is its antisymmetric part, and traceless; its eigenvalues are real, hence zero by the first part, and so $Dv(z)=0$.

For the bounds, let $z\in Z_0$ and $r=d(x,z)<r_0$. Taylor's formula along the minimizing geodesic from $z$ to $x$ (for $v$, applied to the parallel transport of $v$ back to $T_zS^2$) and the global $C^2$ bounds give $|v(x)|+|f(x)|\le Cr^2$ and $|\nabla f(x)|+|\zeta(x)|+|\eta(x)|\le Cr$. By Lemma 3.1(b), $|\nabla H|\le2|f||\eta|+2|\zeta||v|\le Cr^3$ on the geodesic, and integrating along it gives $H(x)\le Cr^4$. For $r\ge r_0$ the bounds hold after enlarging $C$.

*Item 2.* Let $\Theta_\varepsilon$ be the $C^1$ forms of Lemma 6.1. Since $|\Theta_\varepsilon|\le|\tilde\theta|$ and $\Theta_\varepsilon\to\tilde\theta$ pointwise, $\Theta_\varepsilon\to\tilde\theta$ in $L^1$ by Theorem L.1, and for smooth $\varphi$, Stokes' theorem on $S^2$ gives
$$\langle T,\varphi\rangle=-\lim_{\varepsilon\to0}\int d\varphi\wedge\Theta_\varepsilon=\lim_{\varepsilon\to0}\int\varphi\,d\Theta_\varepsilon,\qquad d\Theta_\varepsilon=-2\alpha\,\frac H\varepsilon\,\chi'\Big(\frac H\varepsilon\Big)H^\gamma\zeta\,\mu .$$
$T$ vanishes on $U$ by Lemma 8.5 and on the interior of $Z$ because $\tilde\theta=0$ there. Let $z\in Z\setminus Z_0$, and let $B_z$ and $C_z$ be as in Lemma 7.1. The form $d\Theta_\varepsilon$ is supported in $\{\varepsilon\le H\le2\varepsilon\}$, where $H^\gamma\le\varepsilon^\gamma$ because $\gamma<0$, so
$$\int_{B_z}|d\Theta_\varepsilon|\le4\alpha\|\chi'\|_\infty\|\zeta\|_\infty\,\varepsilon^\gamma\,|\{x\in B_z:H(x)\le2\varepsilon\}|\le C\varepsilon^{\gamma+1/2}=C\varepsilon^{1/(2\alpha)}\longrightarrow0 .$$
So $T$ vanishes on $B_z$, and $\operatorname{supp}T\subset Z_0\cap\partial Z$. (This is the local form of the proof of Theorem E, first assertion.)

*Item 3.* Fix $z\in Z_0$ and $0<r\le r_0$, and let $\chi$ be smooth with values in $[0,1]$, $\chi=1$ on $B(z,r)$, $\operatorname{supp}\chi\subset B(z,2r)$, $|\nabla\chi|\le C/r$ and $|\Delta\chi|\le C/r^2$, with $C$ independent of $z$ and $r$ (take $\chi=\chi_0(d(z,\cdot)/r)$ with a fixed profile $\chi_0$). By item 1, $|v|+|f|\le Cr^2$ and $H\le Cr^4$ on $B(z,2r)$. On $U$, $|\theta|^2=H^{2\gamma}|\eta|^2\le2(\alpha-1)^2H^{2\gamma}|v|^2+2H^{2\gamma}|\nabla f|^2$.

For the first term let $w_\varepsilon=(H+\varepsilon)^{2\gamma}\in C^2(S^2)$. As in the proof of Theorem L.1 (with $e=2\gamma$), Lemma 3.2 and (T1) give
$$\operatorname{div}(w_\varepsilon fv)=w_\varepsilon\big[\alpha H-(\alpha-1)|v|^2-b_\varepsilon f^2\big],\qquad b_\varepsilon=(2-\alpha)+2(\alpha-1)\frac H{H+\varepsilon}\ge0 .$$
Multiplying by $\chi$ and integrating over $S^2$,
$$(\alpha-1)\int\chi w_\varepsilon|v|^2\le\alpha\int\chi w_\varepsilon H+\int w_\varepsilon|f||v||\nabla\chi| .$$
On $U$, $w_\varepsilon H\le H^{1+2\gamma}=H^{1/\alpha}$ and, since $f^2<H$, $w_\varepsilon|f|\le H^{2\gamma+1/2}=H^\beta$; on $Z$ both vanish. So the right side is at most $Cr^{4/\alpha}\cdot r^2+Cr^{4\beta}\cdot r^2\cdot r^{-1}\cdot r^2\le Cr^{4/\alpha+1}$, because $4\beta+3=4/\alpha+1$. By Fatou's lemma, $\int_{B(z,r)\cap U}H^{2\gamma}|v|^2\le Cr^{4/\alpha+1}$.

For the second term put $\rho=2+4\gamma=2/\alpha\in(1,2)$ and let $\Phi_\delta$ be as in Lemma 8.4. Since $\Phi_\delta\circ f\in C^2$,
$$\int\chi\,\Phi_\delta''(f)|\nabla f|^2=-\int\chi\,\Phi_\delta'(f)\Delta f+\int\Phi_\delta(f)\Delta\chi .$$
On $B(z,2r)$, $|\Phi_\delta'(f)|\le\rho|f|^{\rho-1}\le Cr^{2\rho-2}$ and $\Phi_\delta(f)\le(Cr^4+\delta^2)^{\rho/2}$, so the right side is at most $Cr^{2\rho}+C(Cr^4+\delta^2)^{\rho/2}$. Using $\Phi_\delta''(t)\ge\rho(\rho-1)(t^2+\delta^2)^{(\rho-2)/2}$ and monotone convergence as $\delta\to0$, $\int_{B(z,r)\cap\{f\ne0\}}|f|^{\rho-2}|\nabla f|^2\le Cr^{2\rho}=Cr^{4/\alpha}$. On $U\cap\{f\ne0\}$ we have $0<f^2<H$ and $2\gamma<0$, so $H^{2\gamma}<|f|^{4\gamma}=|f|^{\rho-2}$; and $\nabla f=0$ almost everywhere on $\{f=0\}$ (Lemma 8.4). Hence $\int_{B(z,r)\cap U}H^{2\gamma}|\nabla f|^2\le Cr^{4/\alpha}$, which proves item 3.

*Item 4.* For a Lipschitz function $g$ we put $\langle T,g\rangle=-\int dg\wedge\tilde\theta$. If $g$ vanishes on a neighbourhood of $\operatorname{supp}T$, then $\langle T,g\rangle=0$: mollifying in charts as in Lemma 8.5 gives smooth $g_k$ that vanish on a fixed neighbourhood of the compact set $\operatorname{supp}T$, with $\sup_k\|dg_k\|_\infty<\infty$ and $dg_k\to dg$ almost everywhere, so $\langle T,g_k\rangle=0$ and dominated convergence applies.

Let $O$ be open with $O\cap\operatorname{supp}T\ne\emptyset$, and suppose $\mathcal H^{2/\alpha}(O\cap\operatorname{supp}T)=0$. Choose a smooth $\varphi$ supported in $O$ with $\langle T,\varphi\rangle\ne0$. The compact set $K=\operatorname{supp}T\cap\operatorname{supp}\varphi$ lies in $Z_0$ (item 2) and has $\mathcal H^{2/\alpha}(K)=0$. Fix $n\ge1$. By the definition of Hausdorff measure and compactness, there are finitely many balls $B(z_i,r_i)$ with $z_i\in K$, $0<r_i\le\min(r_0,1/n)/2$, covering $K$, with $\sum_ir_i^{2/\alpha}<1/n$. Let $\phi_i=\min\{1,\max\{0,2-d(\cdot,z_i)/r_i\}\}$, which equals $1$ on $B(z_i,r_i)$, vanishes off $B(z_i,2r_i)$ and has $|\nabla\phi_i|\le1/r_i$, and let $\phi_n=\max_i\phi_i$. Then $\phi_n$ is Lipschitz, equals $1$ on a neighbourhood of $K$, vanishes outside $E_n=\bigcup_iB(z_i,2r_i)$, and $|\nabla\phi_n|\le\sum_ir_i^{-1}\mathbf 1_{B(z_i,2r_i)}$ almost everywhere. The function $\varphi(1-\phi_n)$ vanishes on a neighbourhood of $\operatorname{supp}T$ (near $K$ because $\phi_n=1$, and on the open set $S^2\setminus\operatorname{supp}\varphi$), so
$$\langle T,\varphi\rangle=\langle T,\varphi\phi_n\rangle=-\int\phi_n\,d\varphi\wedge\tilde\theta-\int\varphi\,d\phi_n\wedge\tilde\theta .$$
The first integral is at most $\|d\varphi\|_\infty\int_{E_n}|\tilde\theta|$, which tends to zero because $|E_n|\le C\sum_ir_i^2\le C/n$ and $\tilde\theta\in L^1$. By Cauchy-Schwarz and item 3 (applied at $z_i\in Z_0$ with radius $2r_i\le r_0$), the second is at most
$$\|\varphi\|_\infty\sum_i\frac1{r_i}\int_{B(z_i,2r_i)}|\tilde\theta|\le\|\varphi\|_\infty\sum_i\frac1{r_i}\,|B(z_i,2r_i)|^{1/2}\big(C(2r_i)^{4/\alpha}\big)^{1/2}\le C\sum_ir_i^{2/\alpha}\le\frac Cn .$$
Letting $n\to\infty$ gives $\langle T,\varphi\rangle=0$, a contradiction. So $\mathcal H^{2/\alpha}(O\cap\operatorname{supp}T)>0$.

Now let $\Gamma$, $D$, $N$ and $\psi$ be as in the proof of Theorem L.2, so that $\langle T,\psi\rangle=-\int d\psi\wedge\theta=\mp\oint_\Gamma\theta\ne0$. The function $\psi$ vanishes on the open set $S^2\setminus(D\cup N)$, which contains $Z\setminus D$ because $N\subset U$. If $\operatorname{supp}T\cap D$ were empty, $\psi$ would vanish on a neighbourhood of $\operatorname{supp}T\subset Z\setminus D$, and $\langle T,\psi\rangle=0$. Hence $\operatorname{supp}T\cap D\ne\emptyset$, and the previous paragraph with $O=D$ and item 2 give $\mathcal H^{2/\alpha}(Z_0\cap\partial Z\cap D)\ge\mathcal H^{2/\alpha}(\operatorname{supp}T\cap D)>0$. A nontrivial solution has a periodic orbit in $U$ (Lemma 5.6(c)), so $\mathcal H^{2/\alpha}(Z_0\cap\partial Z)>0$. Finally, a countable union of rectifiable curves has $\sigma$-finite $\mathcal H^1$ measure, hence zero $\mathcal H^{2/\alpha}$ measure, since $2/\alpha>1$.

*Item 5.* Write $C_y=F(\cdot,y)$, oriented by increasing $s$, and $I(y)=\oint_{C_y}\theta$ for $0<y\le y_0$. Since $\theta$ is closed on $U$ and the curves $C_y$, $y>0$, bound annuli in $F((\mathbb R/\ell\mathbb Z)\times(0,y_0])\subset U$, Stokes' theorem shows that $I(y)=I$ is independent of $y$. By compactness, $F^*dS=a\,ds\,dy$ with $0<a_0\le a\le a_1$, $|\partial_sF|\le C$, and the function $y\circ F^{-1}$ has bounded gradient on the image. On $\Lambda$, $v=f=0$ (Lemma 7.5), $H=0$ and $\nabla H=0$ ($H\ge0$), so Taylor's formula in $y$ gives, uniformly in $s$,
$$H(F(s,y))\le Cy^2,\qquad|v(F(s,y))|+|f(F(s,y))|\le Cy .$$
On $U$, Lemma 3.2 and (T1) give the exact identity
$$\operatorname{div}(H^{2\gamma}fv)=\alpha H^{1/\alpha}-(\alpha-1)H^{2\gamma}|v|^2-\alpha H^{2\gamma}f^2,$$
since $4\alpha\gamma-(2-\alpha)=-\alpha$. Let $\chi\in C_c^\infty((1/2,3))$ with values in $[0,1]$, $\chi=1$ on $[1,2]$, and $\chi_r=\chi(y/r)$ for $0<r<y_0/3$; its support is a compact subset of the open collar, which lies in $U$. Multiplying by $\chi_r$ and integrating,
$$(\alpha-1)\int\chi_rH^{2\gamma}|v|^2\le\alpha\int\chi_rH^{1/\alpha}+\int H^{2\gamma}|f||v||\nabla\chi_r|\le Cr^{2/\alpha}\cdot r+Cr^{2\beta}\cdot r\cdot r^{-1}\cdot r\le Cr^{2/\alpha},$$
using $H^{2\gamma}|f|\le H^\beta\le Cr^{2\beta}$ and $1+2\beta=2/\alpha$. So $\int_{F(\{r<y<2r\})}H^{2\gamma}|v|^2dS\le Cr^{2/\alpha}$.

For the tangential derivative of $f$, let $h_y(s)=f(F(s,y))$. Then $\|h_y\|_\infty\le Cy$ and $\|h_y''\|_\infty\le C$, because $f$ and $F$ are $C^2$. The one-dimensional form of Lemma 8.4 (same proof, with periodic integration by parts in $s$) gives, with $\rho=2/\alpha$,
$$\int_{\{h_y\ne0\}}|h_y|^{\rho-2}|h_y'|^2ds\le\frac1{\rho-1}\int_0^\ell|h_y|^{\rho-1}|h_y''|\,ds\le Cy^{\rho-1},$$
and $h_y'=0$ almost everywhere on $\{h_y=0\}$. As in item 3, $H^{2\gamma}\le|f|^{\rho-2}$ where $f\ne0$, so $\int_0^\ell H^{2\gamma}|\partial_s(f\circ F)|^2ds\le Cy^{\rho-1}$.

Put $\vartheta(s,y)=\theta_{F(s,y)}(\partial_sF)=H^\gamma\big((1-\alpha)\langle v,\partial_sF\rangle-\partial_s(f\circ F)\big)$. The two bounds give
$$\int_r^{2r}\!\!\int_0^\ell|\vartheta|^2\,ds\,dy\le C\int_{F(\{r<y<2r\})}H^{2\gamma}|v|^2dS+C\int_r^{2r}y^{\rho-1}dy\le Cr^{2/\alpha}.$$
Since $I=\int_0^\ell\vartheta(s,y)\,ds$ for every $y$, Cauchy-Schwarz on each curve and integration over $r<y<2r$ give $r|I|^2\le\ell\,Cr^{2/\alpha}$, that is $|I|\le Cr^{(2/\alpha-1)/2}=Cr^\beta$. Letting $r\to0$ gives $I=0$.

For the consequence, suppose $L$ is a $C^2$ Jordan curve, and let $A_c$, $\Gamma_c$ and $D_c^+$ be as in the proof of Theorem L.4, so that $\overline{A_c}=A_c\cup\Gamma_c\cup L$. The open connected set $A_c$ is disjoint from $\Gamma_c\cup L$ ($\Gamma_c\subset U$, $L\subset Z$, $\Psi>c$ on $A_c$) and its boundary lies in $\Gamma_c\cup L$, so it is a component of $S^2\setminus(\Gamma_c\cup L)$. Its closure contains both curves, so it is the component between them, and by the Schoenflies theorem $\overline{A_c}$ is a closed annulus with boundary curves $\Gamma_c$ and $L$. Choose a smooth vector field $X$ transverse to $L$ and pointing into $A_c$, a $C^2$ parametrization $\lambda$ of $L$, and $F(s,y)=\phi^X_y(\lambda(s))$; for small $y_0$ this is a $C^2$ embedding with $F(s,y)\in A_c\subset U$ for $0<y\le y_0$, so the first part gives $\oint_{C_y}\theta=0$. Through $F$, $C_y$ is homotopic in $\overline{A_c}$ to the boundary curve $L$, so it is essential in $\overline{A_c}$, and so is $\Gamma_c$. The inclusion of $\overline{A_c}\setminus L=A_c\cup\Gamma_c$ into $\overline{A_c}$ is a homotopy equivalence, so $C_y$ and $\Gamma_c$ are freely homotopic, up to orientation, inside $A_c\cup\Gamma_c\subset U$. Since $\theta$ is closed on $U$, $\oint_{\Gamma_c}\theta=\pm\oint_{C_y}\theta=0$, contradicting Lemma 5.7(c). $\square$

*Remarks.*

- Item 1 says that every stagnation point is elliptic or nilpotent in the linear approximation, and item 2 that the charge sits only where $v$, $f$, their first derivatives and $\zeta$ vanish (by Theorem N.1 even the second derivatives of $v$ and $f$ vanish on $\operatorname{supp}T$, hence also $d\zeta$). The proof of item 4 is the proof of Theorem L.2 with balls adapted to $\operatorname{supp}T$: the $L^2$ bound of Theorem L.1 controls the pairing of $T$ with cutoffs through capacity, and the local bound of item 3 controls it through $\sum r_i^{2/\alpha}$.
- At Lebesgue density points of $Z$ the same proof gives $o(r^{4/\alpha})$ in item 3, because all derivatives of $v$ and $f$ up to order two vanish there (if a component $u$ of $v$ or $f$ had a nonzero homogeneous Taylor polynomial $p_j$ of lowest order $j\le2$ at such a point $z$, then $u\ne0$ on the intersection of a small ball around $z$ with an open cone on which $|p_j|\ge c|h|^j$, and this set lies in $U$ and has positive density at $z$), but the exponent stays $4/\alpha<4$, which is not enough to exclude $\operatorname{supp}T$ of positive area.
- The collar theorem uses a uniformly $C^2$ one-sided collar of $\Lambda$; this proof does not cover $C^1$ curves, and it does not apply to orbits that accumulate on a curve without a full collar on one side.

**Proof of Theorem N.** Throughout, the solution is nontrivial, $\rho=2/\alpha\in(1,2)$, $K=\operatorname{supp}T$, which is a compact subset of $Z_0\cap\partial Z$ by Theorem M.2, and $r_1\le1$ is smaller than a sixteenth of the injectivity radius. We use the pairing $\langle T,g\rangle=-\int dg\wedge\tilde\theta$ for Lipschitz $g$, and the fact, shown in the proof of Theorem M.4, that it vanishes when $g$ vanishes on a neighbourhood of $K$.

**Lemma 8.7 (energy near a compact part of $Z$).** For every $m\ge2$ there is $C$, depending only on $\alpha$ and $m$, with the following property. Let $E\subset Z$ be compact, $0<r\le r_1$ and $a>0$, and suppose that on $N_{8r}(E)$
$$|v|+|f|\le ar^m,\qquad|\nabla v|+|\nabla f|\le ar^{m-1},\qquad|\Delta f|\le ar^{m-2}. \tag{8.9}$$
Then
$$\int_{N_{2r}(E)}|\tilde\theta|^2\,dS\le C\,a^\rho\,r^{m\rho-2}\,A_E(4r).$$

*Proof.* Let $x\in N_{8r}(E)$, let $z\in E$ be a nearest point and let $\gamma$ be a minimizing geodesic from $z$ to $x$; every point of $\gamma$ is within $\mathrm{dist}(x,E)$ of $z$, so $\gamma\subset N_{8r}(E)$. By Lemma 3.1(b) and $|\zeta|\le\sqrt2|\nabla v|$, $|\nabla H|\le2|f||\eta|+2|\zeta||v|\le Ca^2r^{2m-1}$ on $N_{8r}(E)$, and since $H(z)=0$,
$$0\le H\le Ca^2r^{2m}\quad\text{on }N_{8r}(E). \tag{8.10}$$
Let $\{z_i\}$ be a maximal $r$-separated subset of $E$ (finite by compactness). The balls $B(z_i,r)$ cover $E$, so the balls $B(z_i,3r)$ cover $N_{2r}(E)$. Fix a smooth $\chi_0:[0,\infty)\to[0,1]$ equal to $1$ on $[0,3]$ and to $0$ on $[7/2,\infty)$, put $\chi_i=\chi_0(d(z_i,\cdot)/r)$ and $\chi=\sum_i\chi_i$. At each point $x$ at most $C$ of the $\chi_i$ are nonzero, because the disjoint balls $B(z_i,r/2)$ with $d(z_i,x)<4r$ lie in $B(x,5r)$. Hence
$$\chi\ge1\text{ on }N_{2r}(E),\qquad\operatorname{supp}\chi\subset N_{4r}(E),\qquad0\le\chi\le C,\quad|\nabla\chi|\le C/r,\quad|\Delta\chi|\le C/r^2 .$$
For the velocity term we argue as in item 3 of Theorem M, with this $\chi$:
$$(\alpha-1)\int\chi w_\varepsilon|v|^2\le\alpha\int\chi w_\varepsilon H+\int w_\varepsilon|f||v||\nabla\chi| .$$
Both integrands on the right vanish on $Z$ and outside $N_{4r}(E)$, and on $U$ they are at most $\chi H^{1/\alpha}$ and $H^\beta|v||\nabla\chi|$. By (8.10) and (8.9) the right side is at most $Ca^\rho(r^{m\rho}+r^{m\rho-1})A_E(4r)$, using $2\beta+1=\rho$. Fatou's lemma gives $\int_{N_{2r}(E)\cap U}H^{2\gamma}|v|^2\le Ca^\rho r^{m\rho-1}A_E(4r)$.

For the gradient term let $\Phi_\delta(t)=(t^2+\delta^2)^{\rho/2}$ as in Lemma 8.4. Since $\int\Delta\chi=0$,
$$\int\chi\,\Phi_\delta''(f)|\nabla f|^2=-\int\chi\,\Phi_\delta'(f)\Delta f+\int\big(\Phi_\delta(f)-\delta^\rho\big)\Delta\chi .$$
Both integrands on the right vanish on $Z$ (where $f=0$ and $\Phi_\delta'(0)=0$) and outside $N_{4r}(E)$. Since $s\mapsto s^{\rho/2}$ is concave with value $0$ at $0$, it is subadditive, so $0\le\Phi_\delta(t)-\delta^\rho\le|t|^\rho$; also $|\Phi_\delta'(t)|\le\rho|t|^{\rho-1}$. So the right side is at most $C\big[(ar^m)^{\rho-1}ar^{m-2}+(ar^m)^\rho r^{-2}\big]A_E(4r)=Ca^\rho r^{m\rho-2}A_E(4r)$. As in Lemma 8.4, monotone convergence as $\delta\to0$ gives $\int_{N_{2r}(E)\cap\{f\ne0\}}|f|^{\rho-2}|\nabla f|^2\le Ca^\rho r^{m\rho-2}A_E(4r)$. On $U\cap\{f\ne0\}$, $H^{2\gamma}<|f|^{\rho-2}$, and $\nabla f=0$ almost everywhere on $\{f=0\}$. Since $|\tilde\theta|^2\le2(\alpha-1)^2H^{2\gamma}|v|^2+2H^{2\gamma}|\nabla f|^2$ on $U$ and $r\le1$, the lemma follows. $\square$

**Lemma 8.8 (defect of a neighbourhood).** Let $E\subset K$ be relatively open and closed in $K$, and let $\psi$ be smooth and vanish on a neighbourhood of $K\setminus E$. Then for every $r>0$
$$|\langle T,\psi\rangle|\le\big(\|d\psi\|_\infty+r^{-1}\|\psi\|_\infty\big)\int_{N_{2r}(E)}|\tilde\theta|\,dS .$$
If moreover (8.9) holds on $N_{8r}(E)$ with $r\le r_1$, then $|\langle T,\psi\rangle|\le C_\psi\,a^{1/\alpha}\,r^{m/\alpha-2}A_E(4r)$.

*Proof.* Let $\phi_r=\min\{1,\max\{0,2-\mathrm{dist}(\cdot,E)/r\}\}$, which equals $1$ on $N_r(E)$, vanishes off $N_{2r}(E)$ and has $|\nabla\phi_r|\le1/r$. The function $\psi(1-\phi_r)$ vanishes on $N_r(E)$ and on a neighbourhood of the compact set $K\setminus E$, hence on a neighbourhood of $K$, so $\langle T,\psi\rangle=\langle T,\psi\phi_r\rangle=-\int\phi_r\,d\psi\wedge\tilde\theta-\int\psi\,d\phi_r\wedge\tilde\theta$, which gives the first bound. For the second, $\tilde\theta=0$ on $Z$, so by Cauchy-Schwarz and Lemma 8.7,
$$\int_{N_{2r}(E)}|\tilde\theta|\le A_E(2r)^{1/2}\big(Ca^\rho r^{m\rho-2}A_E(4r)\big)^{1/2}\le Ca^{\rho/2}r^{m\rho/2-1}A_E(4r),$$
and $\rho/2=1/\alpha$. $\square$

*Item 1.* By Theorem M.1, $v$, $\nabla v$, $f$ and $\nabla f$ vanish on $Z_0\supset K$. Let $z\in K$ and take a chart around $z$. The coordinate components $v^1,v^2$ and $f$ are $C^2$, and their first partial derivatives vanish on $K$, since they differ from the covariant ones by Christoffel terms multiplied by $v$. Suppose that some second partial derivative of $u\in\{v^1,v^2,f\}$ is nonzero at $z$, say $\partial_j\partial_iu(z)\ne0$. Then $g=\partial_iu$ is $C^1$, vanishes on $K$ near $z$, and $dg(z)\ne0$. By the implicit function theorem there is an open set $O\ni z$ in which $\{g=0\}$ is a $C^1$ embedded arc. So $K\cap O$ is a nonempty relatively open subset of $K$ contained in a $C^1$ arc. Such an arc is a countable union of compact arcs of finite length, so $\mathcal H^{2/\alpha}(K\cap O)=0$ because $2/\alpha>1$, which contradicts Theorem M.4. Hence all second partial derivatives vanish on $K$, and so do the covariant ones, which differ from them by terms involving only derivatives of order at most one. If $v,f\in C^k$ near $K$ and all derivatives of order at most $j-1$ vanish on $K$, where $3\le j\le k$, the same argument applied to a partial derivative $g$ of order $j-1$, which is $C^1$, shows that all derivatives of order $j$ vanish on $K$.

*Item 2.* Let $a(r)=\sup_{N_{8r}(K)}\big(|\nabla^2v|+|\nabla^2f|\big)$. By item 1, continuity and compactness, $a$ is nondecreasing with $a(r)\to0$ as $r\to0$. For $x\in N_{8r}(K)$, integrating twice along a minimizing geodesic from a nearest point of $K$ (using parallel transport for $v$) gives
$$|v|+|f|\le Ca(r)r^2,\qquad|\nabla v|+|\nabla f|\le Ca(r)r,\qquad|\Delta f|\le Ca(r)\qquad\text{on }N_{8r}(K),$$
so (8.9) holds with $m=2$ on $N_{8r}(E)$, for every compact $E\subset K$, with every $a>0$ such that $a\ge Ca(r)$.

Let $\Gamma$, $D$, $N$ and $\psi$ be as in the proof of Theorem L.2. Since $\Gamma\subset U$, $E=K\cap D=K\cap\overline D$ is relatively open and closed in $K$, and $\psi$ vanishes on the open set $S^2\setminus(D\cup N)$, which contains $K\setminus E$. By Lemma 8.8, for $0<r\le r_1$,
$$0<\Big|\oint_\Gamma\theta\Big|=|\langle T,\psi\rangle|\le C_\psi\,a^{1/\alpha}\,r^{2/\alpha-2}A_E(4r)\qquad\text{for every }a>0\text{ with }a\ge Ca(r).$$
If $a(r)=0$, letting $a\downarrow0$ gives a contradiction; hence $a(r)>0$, and taking $a=Ca(r)$ gives $A_E(4r)/r^{2-2/\alpha}\ge c\,a(r)^{-1/\alpha}\to\infty$, which is the first claim.

For the second claim, apply Lemma 8.7 with $E=\{z\}$, $z\in K$, where $A_{\{z\}}(4r)\le Cr^2$. With Cauchy-Schwarz this gives, uniformly in $z\in K$ and $0<r\le r_1$,
$$\int_{B(z,2r)}|\tilde\theta|\le b(r)\,r^{1+\rho},\qquad b(r)=Ca(r)^{1/\alpha}\to0 .$$
Suppose $E=\bigcup_{n\ge1}E_n$ with $\mathcal H^\rho(E_n)<\infty$, and fix $\varepsilon>0$. Choose $\delta_n\in(0,r_1]$ with $b(\delta_n)\big(1+\mathcal H^\rho(E_n)\big)\le\varepsilon2^{-n}$. By the definition of Hausdorff measure, $E_n$ is covered by countably many open balls $B(z_{n,i},r_{n,i})$ with $z_{n,i}\in E_n$, $r_{n,i}<\delta_n$ and $\sum_ir_{n,i}^\rho\le C(1+\mathcal H^\rho(E_n))$, the constant depending only on the normalization of $\mathcal H^\rho$. All these balls together cover the compact set $E$; take a finite subcover $B(z_j,r_j)$, $j=1,\dots,J$, and let $\phi=\max_j\phi_j$ with $\phi_j$ as in the proof of Theorem M.4. As in that proof, $\psi(1-\phi)$ vanishes on a neighbourhood of $K$ (near $E$ because $\phi=1$, near $K\setminus E$ because $\psi=0$), so
$$\Big|\oint_\Gamma\theta\Big|=|\langle T,\psi\phi\rangle|\le\sum_j\Big(\|d\psi\|_\infty+\frac{\|\psi\|_\infty}{r_j}\Big)\int_{B(z_j,2r_j)}|\tilde\theta|\le C_\psi\sum_jb(r_j)r_j^\rho\le C_\psi\sum_nb(\delta_n)\,C\big(1+\mathcal H^\rho(E_n)\big)\le C\,C_\psi\,\varepsilon .$$
Letting $\varepsilon\to0$ gives a contradiction. So $E$ is not $\sigma$-finite for $\mathcal H^{2/\alpha}$.

*Item 3.* Cover a neighbourhood of $K$ by finitely many charts. By item 1, all partial derivatives of order at most $k$ of the components of $v$ and of $f$ vanish on $K$. For $x$ close to $K$, let $z\in K$ be a nearest point; for $r$ small, $x$, $z$ and the segment between them lie in one chart. Taylor's formula with integral remainder of order $k$, together with the $\sigma$-Hölder continuity (or, for $\sigma=0$, the boundedness) of the derivatives of order $k$, gives $|\partial^\beta u(x)|\le C\,\mathrm{dist}(x,K)^{k+\sigma-|\beta|}$ for $|\beta|\le k$ and $u\in\{v^1,v^2,f\}$. So (8.9) holds on $N_{8r}(K)$ with $m=k+\sigma$ and a fixed $a$, for all small $r$. Let $\psi$ be any smooth function. Lemma 8.8 with $E=K$ gives
$$|\langle T,\psi\rangle|\le C_\psi\,r^{(k+\sigma)/\alpha-2}A_K(4r)\le C_\psi\,A_K(4r)$$
for small $r\le1$, because $(k+\sigma)/\alpha\ge2$. The open sets $U\cap N_{4r}(K)$ decrease to $U\cap K=\emptyset$ as $r\to0$, so $A_K(4r)\to0$, even if $K$ has positive area. Hence $T=0$. But a nontrivial solution has a periodic orbit in $U$ (Lemma 5.6(c)), and for the function $\psi$ of the proof of Theorem L.2, $\langle T,\psi\rangle=\mp\oint_\Gamma\theta\ne0$. This contradiction proves item 3. $\square$

*Remarks.*

- For $C^2$ solutions the vanishing of the 2-jets on $K$ improves the local bound of Theorem M.3 only by a factor $a(r)\to0$, not by a power of $r$. This is why item 2 gives a criterion on the thickness of the exterior layers of $K$ and not a new dimension bound.
- Item 1 concerns $K=\operatorname{supp}T$ only. No such vanishing is established at points of $Z_0\setminus K$.

## 9. Verified lemmas

"Proved" means a complete proof is given in this report. "Symbolic" means the algebra was also checked with sympy (Section 15). "Audited" means the statement and proof were checked by an independent second model acting as a referee (Section 15).

| Statement | Where | Status |
|---|---|---|
| Bochner identity $\operatorname{div}(\nabla_vv)=\operatorname{tr}(A^2)+v(\operatorname{div}v)+Q$ on the unit sphere | Lemma 0.1 | proved, symbolic |
| Pressure equation $\Delta P=2\alpha P+((\alpha-1)^2+1)f^2-\operatorname{tr}(A^2)$ | Theorem 2.1 | proved, symbolic (modulo (E1)-(E3), symbolic $\alpha$), audited |
| $\Delta P=2\alpha P$ at critical points of $P$ with $v\ne0$ | Theorem 2.2 | proved, audited |
| At stagnation points: $P=-\frac12f^2$, $\nabla^2P=fA+\det A\,\mathrm{Id}$; if $f\ne0$, $A$ is self-adjoint and $\Delta P\le\frac{\alpha(\alpha-2)}2f^2$ | Theorem 2.3 | proved, symbolic (Cayley-Hamilton step and bound), audited |
| **Pressure minimum principle: no negative local minimum of $P$ ($0<\alpha<2$)** | Theorem 2.4, Proposition 0.3 | **proved, audited** ($C^2$ and $C^1$) |
| **Nonexistence of nontrivial $C^1$ solutions on $S^2$ for $0<\alpha<2$** | Theorem 1 | **proved, audited** |
| Pressure minimum on a disk bounded by a periodic orbit is negative, lies on the orbit, where the inward geodesic curvature is negative | Corollary 3 | proved, audited |
| Distributional pressure equation for $C^1$ solutions | Lemma 0.2 | proved, audited |
| Version of Theorem 2.4 and of Theorem 1 ($C^2$ and $C^1$) for metrics on $S^2$ with curvature $K\ge1$; item 2 becomes $\Delta P=2\alpha P+(1-K)Q$ | Section 10.1 | proved, symbolic (formula), audited |
| Reduction of stationary Euler to (E1)-(E3); (T1), (T2) | Section 1 | proved, symbolic |
| Identities (a)-(h): $\eta(v)=-\alpha H$, $dH\wedge\eta=-2\alpha H\zeta\mu$, $d\eta=(1-\alpha)\zeta\mu$, $\nabla H=-2f\eta^\sharp-2\zeta Jv$, weighted divergence, vorticity transport | Lemma 3.1 | proved, symbolic |
| $d(H^\gamma\eta)=0$ and $\operatorname{div}(H^\beta v)=0$ on $U$ | after Lemma 3.1 | proved, symbolic |
| $H\equiv0$ implies trivial; $v=0\Rightarrow H=0$; $\alpha\int H=(2-\alpha)\int f^2+(\alpha-1)\int|v|^2$ | Lemma 3.3 | proved |
| **Sign lemma $H\ge0$ for $1<\alpha<2$** | Theorem A | **correct**: proved, audited |
| $W=H^\beta v$ is $C^{0,2\beta}$ and weakly divergence free; global $\Psi\in C^{1,2\beta}$ | Lemmas 5.1-5.3 | proved, audited |
| $|\Psi(Z)|=0$; regular levels are periodic orbits; a.e. point of $U$ periodic | Lemmas 5.5, 5.6 | proved, audited |
| Period identities; $\oint\theta<0$; both sides of a periodic orbit meet $Z$; complements of components of $U$ disconnected | Lemmas 5.7, 5.8 | proved, audited |
| Shell identity and thick-shell bound $|\{\varepsilon\le H\le2\varepsilon\}|\ge c_0\varepsilon^{|\gamma|}$ | Lemma 6.1, Theorem C | proved, audited |
| No closed $L^1$ or distributional extension of $\theta$ (nontrivial solutions); exact defect of $(H+\varepsilon)^\gamma\eta$; $H_*(\zeta dS)=0$ | Proposition D, Lemma 6.3 | proved, audited |
| Hessian sublevel bound; $Z_0$ meets both sides of every periodic orbit; $Z_0$ invariant; 2-jet at stagnation points | Lemmas 7.1-7.3, Theorem E | proved, audited; (7.1) symbolic |
| Conditional nonexistence (F1)-(F5); (F6) is Theorem L.5 | Theorem F | proved, audited |
| Finite $Z$: degenerate centre with $f=\nabla f=Dv=\zeta=0$, degenerate quadratic part, $H=O(r^4)$, period bound | Theorem G | proved, audited; vacuous by Theorem L.3 |
| Top end: periods $\to\infty$, limit set contains a stagnation point | Proposition H | proved, audited |
| Speed nonuniformity on periodic orbits; no uniformly rotating isolated zero of $H$ | Lemma 8.1, Theorem I | proved, audited; Theorem I also follows from Theorem L.2 |
| $Z=S$ and $v=f=P=0$ on $Z$; $f^2<H$ on $U$ | Lemma 7.5 (Proposition K) | proved, audited (first found by the referee) |
| Resolution near the top limit set; Euler bound $H\circ\pi\le Cm^2$; real-analytic solutions are trivial | Lemmas 8.2, 8.3, Theorem J | proved, audited (gaps in the draft found by the referee, all repaired) |
| $\int_UH^{-2\lambda}|\theta|^2<\infty$ for $\lambda<(2-\alpha)/(4\alpha)$; scalar inequality $\int|f|^{\rho-2}|\nabla f|^2<\infty$ | Theorem L.1, Lemma 8.4 | proved, audited; case $\lambda=0$ first found by the referee |
| Zero set has positive capacity on both sides of every periodic orbit; $Z$ of capacity zero (finite, countable) implies trivial | Theorem L.2, L.3, Lemmas 8.5, 8.6 | proved, audited; finite $Z$ first found by the referee |
| Top-end limit set $L$ is not a point; flatness bound $H\le C\,\mathrm{dist}(\cdot,Z)^k$ impossible for $k>4\alpha/(2-\alpha)$ (F6) | Theorem L.4, L.5 | proved, audited |
| A closed $L^2$ form with a nonzero period around a compact set of positive capacity exists | remark after Theorem L | proved (variational argument written out in the remark) |
| Eigenvalues of $Dv$ on $Z$ imaginary or zero; $\nabla f=\zeta=Dv=0$ on $Z_0$; $H\le C\,\mathrm{dist}(\cdot,Z_0)^4$ | Theorem M.1 | proved, audited; first found by the referee (at $Z_0$), extended to all of $Z$ by us |
| $\operatorname{supp}d\tilde\theta\subset Z_0\cap\partial Z$ | Theorem M.2 | proved, audited; first found by the referee |
| Local energy $\int_{B(z,r)\cap U}|\theta|^2\le Cr^{4/\alpha}$ at $Z_0$; positive $\mathcal H^{2/\alpha}$ measure of every relatively open piece of $\operatorname{supp}d\tilde\theta$ | Theorem M.3, M.4 | proved, audited |
| Collar theorem: zero period next to a $C^2$ Jordan curve of $Z$ with a one-sided collar in $U$; top-end limit set not a $C^2$ Jordan curve | Theorem M.5 | proved, audited; first found by the referee |
| Energy bound keeping the $U$-area (Lemma 8.7); defect of a neighbourhood (Lemma 8.8) | Lemmas 8.7, 8.8 | proved; first found by the referee, checked by us |
| Vanishing of 2-jets ($k$-jets for $C^k$ data) on $\operatorname{supp}d\tilde\theta$; thick exterior layers and non-$\sigma$-finiteness for $C^2$ data; triviality for $C^{k,\sigma}$, $k+\sigma\ge2\alpha$, in particular for $C^4$ | Theorem N | proved; first found by the referee, checked by us; the 2-jet statement also proposed independently in a second audit; report version audited (Section 15) |
| Local shear solutions $u=\rho^{-\alpha}a(\varphi)e_1$ with fat stagnation sets have $d\tilde\theta=0$ | Section 11 | proved (direct computation) |
| Exclusion of hyperbolic polycycles as limit sets in Proposition H | remark after Prop. H | not proved, not claimed (not needed for Theorem J) |

The audits and the corrections they led to are described in Section 15.

## 10. Remaining obstacle

### 10.1 Scope of Theorem 1

For the problem posed in the task there is no remaining obstacle. Theorem 1 proves nonexistence for $1<\alpha<2$ and $C^2$ profiles, and more. The following is what Theorem 1 does not cover.

- **Other exponents.** The range $0<\alpha<2$ is sharp at both ends, and outside $[0,2]$ nontrivial solutions exist: potential flows for integer $\alpha$, and Abe's solutions for $\alpha>2$ and $\alpha<0$ (remarks after Corollary 3, Section 11).
- **Lower regularity.** The proof evaluates the equations pointwise at a minimum point of $P$. For $C^1$ profiles it also uses the distributional pressure equation with a continuous right-hand side. Suppose instead that $v,f$ are only Hölder continuous and $P\in L^1(S^2)$, and that $u,p$ solve the Euler equations in the sense of distributions on $\mathbb R^3\setminus\{0\}$. Testing with functions of the form $\psi(|x|)\chi(x/|x|)$ and using the homogeneity, one finds that $(v,f,P)$ then satisfies the conservative system
$$\operatorname{div}v=(\alpha-2)f,\qquad \operatorname{div}(fv)=Q+2(\alpha-1)f^2+2\alpha P,\qquad \operatorname{div}(v\otimes v)+(3-2\alpha)fv+\nabla P=0$$
in the sense of distributions on $S^2$, the second equation being the radial and the third the tangential momentum equation. For $C^1$ profiles this system is equivalent to (E1)-(E3), since $\operatorname{div}(fv)=v(f)+f\operatorname{div}v$ and $\operatorname{div}(v\otimes v)=(\operatorname{div}v)v+\nabla_vv$. By weak solutions of (E1)-(E3) we mean distributional solutions of this system. Testing the second equation with $1$ gives $2\alpha\int P\,dS=-\int(Q+2(\alpha-1)f^2)\,dS$, so for $1<\alpha<2$ a nonzero weak solution has $P<0$ on a set of positive measure. For weak solutions the argument of Theorem 1 does not apply, because neither the trace term at a critical point nor the Hessian at a stagnation point is defined. As far as we know it is open whether such weak homogeneous solutions exist for $0<\alpha<2$ (Section 14).
- **Local solutions.** Theorem 2 is local. A solution on a proper open subset of $S^2$, however, need not have an interior pressure minimum, as the swirl flows show. On a disk bounded by a periodic orbit, what survives is Corollary 3. It does not exclude such local solutions, and we have not settled the local charge problem of Section 10.2. That problem no longer bears on the global question.
- **Other metrics.** The system (E1)-(E3) can be written for any smooth metric on $S^2$, with its Levi-Civita connection, area form and Gaussian curvature $K$; for metrics other than the round one it is no longer derived from the Euler equations in $\mathbb R^3$. The Bochner identity then reads $\operatorname{div}(\nabla_vv)=\operatorname{tr}(A^2)+v(\operatorname{div}v)+KQ$ (the proof of Lemma 0.1, with $R_{kj}=Kg_{kj}$), and (0.1) becomes
$$\Delta P=2\alpha P+\big((\alpha-1)^2+1\big)f^2-\operatorname{tr}(A^2)+(1-K)Q .$$
At a critical point $z$ of $P$ with $v(z)\ne0$ the algebra of the proof of Theorem 2.2 is unchanged, so item 2 of Theorem 2 is replaced by $\Delta P(z)=2\alpha P(z)+(1-K(z))Q(z)$. If $K\ge1$ and $P(z)<0$, this is still at most $2\alpha P(z)<0$, which is all that the proof of item 4 uses. The stagnation-point computation of Theorem 2.3 does not involve $K$, so item 3 holds as stated. Hence item 4 of Theorem 2 and Theorem 1 hold on $S^2$ with any smooth metric of curvature $K\ge1$, also for solutions of class $C^1$: in Lemma 0.2 the function $g$ acquires the continuous term $(1-K)Q$, and Proposition 0.3 uses only $g(z)\le2\alpha P(z)<0$ in the case $v(z)\ne0$, isothermal coordinates (which exist for every smooth metric) and, in the case $v(z)=0$, normal coordinates. This generalization was noted by the referee. Where $K<1$ the step at nonstagnant critical points fails. Within the proof of Theorem 1 this is the only place where the value of the curvature enters; the proof also uses that the surface is closed (existence of a minimum of $P$ and of a maximum of $f^2$). It is the kind of curvature input that the last observation of Section 10.2 identifies as necessary for any proof along the lines of Part II.

### 10.2 The obstacle of the Bernoulli route (Part II)

This subsection records where the route of Part II stopped before the pressure argument was found. By Theorem 1 none of the configurations below occurs on the round sphere. We keep the description because it shows what the methods of Part II can and cannot reach. The observations at its end concern local solutions and other metrics, and they remain valid.

Collecting the results, a nontrivial $C^2$ solution, if one exists, has the following properties.

- $Z=S$, the solution vanishes at every point of $Z$, and $f^2<H$ on $U$ (Proposition K). Almost every point of $U$ lies on a periodic orbit, and $\oint\theta=-\alpha\int H^{1+\gamma}dt<0$ on each of them (Theorem B).
- The distribution $T=d\tilde\theta$, $\langle T,\varphi\rangle=-\int d\varphi\wedge\tilde\theta$, lies in $H^{-1}(S^2)$ (Theorem L.1) and is nonzero: $\langle T,\Psi\rangle=\alpha\int H^{3/(2\alpha)}dS$ (Proposition D.2), and on each side $D$ of a periodic orbit $\Gamma$ its pairing with the cutoff $\psi$ of the proof of Theorem L.2 is $\pm\oint_\Gamma\theta\ne0$.
- Its support $K$ lies in $Z_0\cap\partial Z$ (Theorem M.2). On $K$, $v$ and $f$ vanish together with all their derivatives of order at most two (Theorem N.1), so $H=o(\mathrm{dist}(\cdot,K)^4)$ near $K$.
- For every periodic orbit $\Gamma\subset U$ and each side $D$ of $\Gamma$, the set $E=K\cap D$ is nonempty, is not $\sigma$-finite for $\mathcal H^{2/\alpha}$ (so it has Hausdorff dimension at least $2/\alpha>1$ and is not contained in countably many rectifiable curves), and its exterior layers are thick: $|U\cap N_r(E)|/r^{2-2/\alpha}\to\infty$ (Theorem N.2). In particular $Z\cap D$ has positive capacity (Theorem L.2).
- $v$ and $f$ are not of class $C^{k,\sigma}$ near $K$ with $k+\sigma\ge2\alpha$ (Theorem N.3); in particular they are not $C^4$, and not $C^3$ if $\alpha\le\frac32$.
- $H$ is not bounded by $C\,\mathrm{dist}(\cdot,Z)^k$ with $k>4\alpha/(2-\alpha)$ on any side of a periodic orbit (Theorem L.5). On the other hand, combining Theorems C and E with Lemma 7.1, for every open $N\supset Z_0$ there are $c_N,s_N>0$ with
$$|\{x\in N:\ 0<H(x)\le s\}|\ \ge\ c_N\,s^{(\alpha-1)/(2\alpha)}\qquad(0<s\le s_N), \tag{10.1}$$
because outside $N$ the zero set is covered by finitely many Hessian boxes, where the sublevel area is $O(\sqrt s)=o(s^{|\gamma|})$.
- If $M=\max\Psi$ is isolated in $\Psi(Z)$, the top annuli of Proposition H have limit sets $L$ that are nondegenerate continua of stagnation points (Theorem L.4) and are not $C^2$ Jordan curves (Theorem M.5); the periods of the orbits tend to infinity, $\int_{\Gamma_c}H^{1+\gamma}dt$ is constant along each annulus, and $v,f,P$ are not all real analytic on any neighbourhood of $L$ (Theorem J).

**The open case of Part II.** What the results of Part II do not exclude is a solution of class $C^2$ (or $C^3$ when $\alpha>\frac32$, or $C^{2,\sigma}$ with $\sigma<2(\alpha-1)$) whose defect support $K$ has the size and the thick exterior layers just described. Geometries of $K\cap D$ that are not excluded by the estimates above include the following. We do not claim that any of them is compatible with all of (E1)-(E3), or that it is realized by a solution.

1. **Fractal boundaries.** $Z$ has interior, and $K\cap D\subset\partial Z$ is a curve-like set that is not $\sigma$-finite for $\mathcal H^{2/\alpha}$ (so its Hausdorff dimension lies in $[2/\alpha,2]$), on which the derivatives of $v$ and $f$ of order at most two vanish, while $v,f$ are not of class $C^{k,\sigma}$ with $k+\sigma\ge2\alpha$ near it.
2. **Fat or totally disconnected sets.** Compact sets of positive area, or Cantor-type sets that are not $\sigma$-finite for $\mathcal H^{2/\alpha}$, whose complements penetrate them densely enough that $|U\cap N_r(K)|/r^{2-2/\alpha}\to\infty$. For example, let $b>1$ and let $C_b\subset[0,1]$ be the fat Cantor set obtained by removing, at stage $n$, a central open interval of length $c\,2^{-bn}$ from each of the $2^{n-1}$ remaining intervals ($c$ small). The product $E_b=C_b\times C_b$, placed in a chart, is totally disconnected, has positive area and satisfies $|N_r(E_b)\setminus E_b|\le Cr^{1-1/b}$. Since $U\cap N_r(E)\subset N_r(E)\setminus E$ for $E\subset Z$, Theorem N.2 excludes $E_b$ (and finite unions of separated copies) as $K\cap D$ when $b\ge\alpha/(2-\alpha)$, since then $|U\cap N_r(E_b)|/r^{2-2/\alpha}\le Cr^{1-1/b-(2-2/\alpha)}$ stays bounded; for $1<b<\alpha/(2-\alpha)$ the criterion does not apply. (This example is the referee's, Section 15; we checked it and use it only as an illustration.)
3. **Continuum top ends** whose limit set $L$ is a nondegenerate continuum which is not a $C^2$ Jordan curve, near which the solution is $C^2$ but not analytic, and where the defect enclosed by the orbits of the annulus is carried by a set of the size just described. (We do not claim that $L$ itself has dimension at least $2/\alpha$: the region enclosed by the annulus may contain parts of $U$ besides $L$.)
4. **Non-isolated extrema of $\Psi(Z)$.** If $\max\Psi$ is a limit of other values of $\Psi(Z)$, Proposition H does not apply, and one has to work with the ends of the annuli over the gaps of $\Psi(Z)$, whose limit sets can contain orbits in $U$. (By contrast, $Z$ contains no nonstationary periodic orbit, since $Z=S$.)

For real-analytic solutions, and for all solutions of class $C^4$, none of these occurs (Theorems J and N.3).

Three observations indicate what a proof of the open case along the lines of Part II must use.

- **Local information near $Z$ does not suffice.** The local shear solutions of Section 11 are actual Euler solutions near a point of $S^2$ whose stagnation set can be a fat Cantor family of arcs with thick exterior layers, with the derivatives of $v,f$ of order at most two vanishing there (so $v,f=o(\mathrm{dist}^2)$) and, for suitable profiles, $v,f$ not $O(\mathrm{dist}^{2+\delta})$ for any $\delta>0$, and with $\theta$ square integrable. For them $\tilde\theta$ is exact and $T=0$. So the quantitative inputs of Theorems M and N (jets on $Z$, local energy bounds) cannot by themselves force a higher vanishing order on $K$; a proof must use that $T\ne0$ near $K$, that is, the periodic orbits around $K$ and their nonzero periods, or global structure. Likewise, the weighted bound of Theorem L.1 is locally sharp: for the exact local solution $u=x_3x_2^{-\alpha-1}e_1$ (with $p=0$) the integrand $H^{-2\lambda}|\theta|^2$ is integrable near a point of $\{x_3=0\}$ exactly when $\lambda<\lambda_*$ (referee's example, checked by us).
- **No regularity bootstrap.** Stationary Euler does not regularize. In the coordinates $(\Psi,\int\theta)$ on $U$ the round-sphere condition is a fourth-order equation for $k=H^{1+\gamma}$ whose principal symbol is degenerate (characteristic covectors proportional to $d\Psi$), and the shear solutions with non-analytic profile show that $C^\infty$ solutions need not be analytic in $U$ (referee's computation, Section 15). Nor does local regularity improve: the shear solution of Section 11 with profile $a(\varphi)=1+\chi(\varphi)|\varphi|^3$ is $C^2$ but not $C^3$ near the arc $\{\varphi=0\}$, with $H>0$ there. So no local argument can raise the regularity of a $C^2$ solution to $C^4$ in order to apply Theorem N.3; a bootstrap would have to use global structure.
- **The metric.** The arguments of Part II use (E1)-(E3) written with the Levi-Civita connection and the area form, and never the value of the curvature. They do use the topology of $S^2$ (for instance the hairy ball theorem in Lemma 3.3 and $H^1_{dR}(S^2)=0$ for the stream function), and Theorem J uses real analyticity of the metric (remark after its proof). So the value of the curvature cannot be what drives them. On an annulus foliated by periodic orbits, the system is locally underdetermined if the metric is free: in the coordinates $(\Psi,S)$ with $dS=\theta$, any positive function $k=H^{1+\gamma}$ with $\partial_Sf+H^{-\gamma}>0$, where $f=-\partial_Sk/(2(1+\gamma))$, defines a solution for a metric determined by $k$ (this computation was carried out by the referee and checked by us; we do not use it). The referee also derived from the Gauss-Bonnet formula on the orbits of a top annulus a necessary integrability condition, which does not lead to a contradiction. So a proof for the open case either does not use the value of the curvature, and then rests on how the solution closes up at $Z$ around a set carrying a nonzero charge, or must use the curvature of the round sphere. The proof of Theorem 1 does the latter (Section 10.1).

**The local charge problem.** An earlier version of this report recommended the following problem as the next step, because a negative answer would have proved the conjecture. Fix $1<\alpha<2$. Do there exist an open disk $W\subset S^2$ and a $C^2$ solution $(v,f,P)$ of (E1)-(E3) on $W$ (round metric) with the following two properties?

- $Z\cap W$ is a nonempty compact subset of $W$, and $H>0$ on $W\setminus Z$.
- Some periodic orbit $\Gamma\subset W\setminus Z$ encloses $Z\cap W$, and $\oint_\Gamma\theta\ne0$.

Theorem 1 settles the global question without this problem, and Corollary 3 is what the pressure argument gives on such a disk. Corollary 3 implies that the orbit $\Gamma$ of a local solution as above must have negative inward geodesic curvature at every point where $P|_\Gamma$ is minimal. Corollary 3 does not exclude every such configuration, and the local problem is not settled here; it no longer has consequences for the global question.

## 11. Counterexamples and tests

We separate actual Euler solutions from examples that satisfy only part of the reduced system.

**Tests of Section 0.** In each of the following exact solutions we computed the quantities of Theorem 2 by hand. Where stated, they were also checked symbolically.

- *Point source, $\alpha=2$:* $v=0$, $f=c$, $P=-c^2/2$, $u=c\,x/|x|^3$, with a constant $c\ne0$. Every point is a stagnation point, $A=0$, and (0.2) gives $\nabla^2P=0$, which is correct. Every point is a minimum of $P$ with negative value; this is allowed only because the bound $\frac{\alpha(\alpha-2)}2f^2$ of Theorem 2.3 vanishes at $\alpha=2$.
- *Constant flows, $\alpha=0$:* $u=e$ with $e\in\mathbb R^3\setminus\{0\}$, $v=e-(e\cdot\omega)\omega$, $f=e\cdot\omega$, $P=0$. At the stagnation points $\pm e/|e|$ one has $f=\pm|e|$ and $P=0\ne-\frac12f^2$. This shows that the relation $P=-\frac12f^2$ at stagnation points needs $\alpha\ne0$.
- *Linear strain, $\alpha=-1$:* $u=(x_1,2x_2,-3x_3)$, $p=-\frac12(x_1^2+4x_2^2+9x_3^2)$. On the sphere, near $e_3$ in the coordinates $(x_1,x_2)$, $P=-\frac92+4x_1^2+\frac52x_2^2$ exactly, and since the metric in these coordinates is $\delta_{ij}+O(|x|^2)$, $\nabla^2P(e_3)=\operatorname{diag}(8,5)$. Also $f(e_3)=-3$, and the tangential part of $u$ is $v=(4x_1,5x_2)+O(|x|^3)$, so $A(e_3)=\operatorname{diag}(4,5)$, $\operatorname{tr}A=9=(\alpha-2)f$ and $\det A=20$. Formula (0.2) gives $fA+\det A\,\mathrm{Id}=\operatorname{diag}(-12+20,-15+20)=\operatorname{diag}(8,5)$, as it should. The minimum $-\frac92$ is negative, and this is consistent with Theorem 2 only because $\alpha<0$: the right side of the bound in Theorem 2.3 is $\frac{\alpha(\alpha-2)}2f^2=\frac{27}2>0$.
- *Rigid rotation, $\alpha=-1$:* $u=e_3\times x$, $p=\frac12(x_1^2+x_2^2)$. Here $P=\frac12\sin^2\vartheta\ge0$, its minima are the poles, and these are stagnation points with $f=0$.
- *Swirl flows, $0<\alpha<2$, with a nonzero amplitude:* see the remarks after Corollary 3 and the first example below. $P<0$ everywhere, and $P$ has no minimum on the sphere minus the poles.
- *Symbolic checks.* The identity (0.1) was verified symbolically on the following exact solutions: the rigid rotation and the strain ($\alpha=-1$), the point source ($\alpha=2$), the dipole $u=\nabla(x_3|x|^{-3})$ ($\alpha=3$), and a cubic harmonic potential flow ($\alpha=-2$). For the cubic flow $u=\nabla(x_1x_2x_3)$ one has exactly $f=3x_1x_2x_3$, $v=\nabla_{S^2}(x_1x_2x_3)$, $P=-\frac12(Q+f^2)$ and $v(f)=3Q$, which is (E2) for $\alpha=-2$; sympy confirms that the residual of (E2) is identically zero.

**Actual Euler solutions (outside the hypotheses).**

- *Swirl flow* $u=C\,(r\sin\vartheta)^{-\alpha}e_\varphi$ ($\vartheta$ the polar angle, $C\ne0$ a constant), i.e. $v=C\sin^{-\alpha}\vartheta\,e_\varphi$, $f=0$, $P=-\frac{C^2}{2\alpha}\sin^{-2\alpha}\vartheta$. This solves (E1)-(E3) on $S^2$ minus the poles, so it is an actual 3D Euler solution off the $x_3$-axis (Shvydkoy, Proposition 4.1). Here:
  - $H=(1-\frac1\alpha)C^2\sin^{-2\alpha}\vartheta$, which is positive for $1<\alpha<2$ (and negative for $0<\alpha<1$); for $1<\alpha<2$, $\theta=H^\gamma\eta$ is a constant multiple of $d\varphi$, closed but not exact on the punctured sphere;
  - $W=H^\beta v$ has stream function $\Psi=\text{const}\cdot\cot\vartheta$, which is unbounded.
  
  The example shows what goes wrong without global regularity. Every latitude circle is a periodic orbit with $\oint\theta\ne0$, and both complementary disks contain a pole, where the solution is singular instead of $H$ vanishing. It is consistent with Theorem B item 4 and shows that global regularity on $S^2$ is essential to the argument. It does not show that $C^2$ is a sharp regularity threshold. (Verified symbolically.)
- *Radial source at $\alpha=2$*: $v=0$, $f=c$, $P=-c^2/2$, $u=c\,x/|x|^3$. This is a smooth actual solution with $H\equiv0$, at the excluded endpoint $\alpha=2$. For $1<\alpha<2$, (E1) gives $(2-\alpha)\int f=0$. So no family of solutions with $\alpha\to2^-$ can converge, even in $C^0$, to this solution with $c\ne0$; perturbation from it is ruled out.
- *Local shear solutions.* Let $(\rho,\varphi)$ be polar coordinates in the $(x_2,x_3)$-plane, and let $a$ be a $C^2$ function of $\varphi\in\mathbb R/2\pi\mathbb Z$. Then $u=\rho^{-\alpha}a(\varphi)e_1$, $p=0$, is an exact stationary Euler solution off the $x_1$-axis, homogeneous of degree $-\alpha$: $u$ depends only on $(x_2,x_3)$ and is parallel to $e_1$, so $\operatorname{div}u=0$ and $(u\cdot\nabla)u=0$. On $S^2$, with $t\in(0,\pi)$ the angle from $e_1$ (so the metric is $dt^2+\sin^2t\,d\varphi^2$), it gives
$$f=a(\varphi)\cos t\,\sin^{-\alpha}t,\qquad v=-a(\varphi)\sin^{1-\alpha}t\,e_t,\qquad P=0,\qquad H=a(\varphi)^2\sin^{-2\alpha}t,$$
and a direct computation from $\eta=(1-\alpha)v^\flat-df$ and $H^\gamma=|a|^{2\gamma}\sin^{\alpha-1}t$ gives
$$\theta=\alpha\,b(\varphi)\,\frac{dt}{\sin^2t}-\alpha\,b'(\varphi)\cot t\,d\varphi=-\alpha\,d\big(b(\varphi)\cot t\big),\qquad b=\operatorname{sgn}(a)|a|^{1/\alpha},$$
on $\{a\ne0\}$. The zero set of $H$ is the union of the meridian arcs $\{\varphi\in C\}$, $C=a^{-1}(0)$, which may be any closed set; for instance $C$ can be a fat Cantor set and $a$ can be chosen so that $a,a',a''$ vanish on $C$ while $a$ is not $O(\mathrm{dist}(\cdot,C)^{2+\delta})$ for any $\delta>0$. By the one-dimensional form of the scalar inequality of Lemma 8.4, $|a|^{(\rho-2)/2}|a'|\in L^2$ for $\rho=2/\alpha$, so $b$ is absolutely continuous with $b'=\alpha^{-1}|a|^{2\gamma}a'$ on $\{a\ne0\}$ and $b'=0$ almost everywhere on $C$. Hence $\tilde\theta=d\big(-\alpha\,b(\varphi)\cot t\big)$ in the sense of distributions, with a potential in $W^{1,2}_{\rm loc}$, and $d\tilde\theta=0$. These solutions are singular at $\pm e_1$ and their orbits in $U$ are meridian arcs, not periodic orbits. They show that a stagnation set with the size and thick exterior layers of Theorem N.2, and with vanishing 2-jets but no vanishing of order $2+\delta$, occurs for actual local Euler solutions, but with zero defect; see the first observation in Section 10.2. With $a>0$ smooth and not analytic, they also show that $C^\infty$ solutions need not be analytic on $U$ (an observation of the referee). With $a(\varphi)=1+\chi(\varphi)|\varphi|^3$, where $\chi\ge0$ is smooth, equal to $1$ near $0$ and supported in $(-1,1)$, one has $a\ge1$, $a\in C^2$ and $a\notin C^3$ near $0$, so $v,f$ are $C^2$ but not $C^3$ near the arc $\{\varphi=0\}$, while $H=a^2\sin^{-2\alpha}t>0$: a $C^2$ local solution need not be locally $C^3$. (Checked by hand.)
- *Potential flows* $u=\nabla(r^{1-\alpha}Y)$ require $1-\alpha\in\{l,-l-1\}$ for a spherical harmonic of degree $l$, i.e. $\alpha\in\mathbb Z$ (Shvydkoy, Proposition 3.1). There are none for $1<\alpha<2$.

**Examples satisfying only reduced equations.**

- *Rigid rotation* $v=e_3\times\omega$ (so $|v|=\sin\vartheta$), $f=0$, $P=-\frac{\sin^2\vartheta}{2\alpha}$.
  - It satisfies (E1), (E2), (T1) and (T2) on all of $S^2$, with $H=\frac{\alpha-1}\alpha\sin^2\vartheta\ge0$.
  - It fails (E3): the residual is $-\frac{\alpha+1}{2\alpha}\sin2\vartheta\,e_\vartheta$.
  - $d(H^\gamma\eta)\ne0$ on $U$, since Lemma 3.1(b) fails.
  
  It is therefore not an Euler solution. It is instructive because it satisfies every integral identity of the form $\int\operatorname{div}(\Phi(f,H)v)\,dS=0$: here $f\equiv0$, $\alpha H=(\alpha-1)|v|^2$, and $v$ is a divergence-free Killing field preserving $H$. So no argument using only (E1), (E2), (T1), (T2) and such identities can prove nonexistence. The tangential momentum equation, through the closedness of $\theta$, is essential. (Verified symbolically.)
- *Degree-one ansatz.* Let $v=\nabla(c\cdot\omega)+J\nabla(d\cdot\omega)=c-(c\cdot\omega)\omega+\omega\times d$ with $c,d\in\mathbb R^3$, with $f$ determined by (E1) and $P$ by (E2). Then $c=d=0$ is forced for every $1<\alpha<2$. Write $a=c\cdot\omega$, $b=d\cdot\omega$, $e=(d\times c)\cdot\omega$ and $t=2-\alpha$. Since $\Delta a=-2a$ and $\operatorname{div}J\nabla b=0$, (E1) gives $f=2a/t$. Substituting into (E3) gives the tangential residual
$$R=\lambda\,a\nabla a-\frac2t\,a\,(\omega\times d)+\delta\,b\nabla b+\kappa\nabla e,\qquad \lambda=\frac{(\alpha-3)(\alpha+2)}{t^2}<0,\quad \delta=\frac{\alpha+1}{\alpha}>0,\quad \kappa=\frac{\alpha^2-\alpha-1}{\alpha t}$$
(this closed form was found by the independent referee and verified symbolically). Under $\omega\mapsto-\omega$, the functions $a,b,e$ and the field $\omega\times d$ are odd, while $\nabla a,\nabla b,\nabla e$ are even. The odd part of $R=0$ is $\frac12\nabla(\lambda a^2+\delta b^2)=0$, so the quadratic form $\omega^T(\lambda cc^T+\delta dd^T)\omega$ is constant on $S^2$ and $\lambda cc^T+\delta dd^T$ is a multiple of the identity. Its rank is at most two, so it vanishes: $|\lambda|cc^T=\delta dd^T$. Hence either $c=d=0$, or $c$ and $d$ are nonzero and parallel. In the second case $e=0$, and the even part of $R=0$ becomes $a\,(\omega\times d)=0$ on $S^2$, which fails at any $\omega$ with $c\cdot\omega\ne0$ and $\omega\nparallel d$. So $c=d=0$. This is a restricted finite-dimensional class and serves only as a sanity check.

**Consistency checks of the framework.**

- At the endpoint $\alpha=1$ one has $\gamma=0$, so $\theta=\eta=-df$ is exact on $S^2$. The proofs of Theorem A and of Lemmas 5.1-5.7 go through at $\alpha=1$ ($\beta=\frac12$, $2/\alpha-1=1>0$; in Lemma 5.3 one gets $\Psi\in C^{1,\kappa}$ for every $\kappa<1$). If $U\ne\emptyset$, a periodic orbit in $U$ has $\oint\theta=-\int H\,dt<0$, which contradicts exactness. If $U=\emptyset$, then $H\equiv0$, and Lemma 3.3's identity at $\alpha=1$, $\int H=\int f^2$, gives $f\equiv0$. Then $P=-|v|^2/2$, (E3) reduces to $\zeta Jv=0$, so $\zeta=0$ on the dense set $\{v\ne0\}\cup\operatorname{int}\{v=0\}$ and hence everywhere. Together with $\operatorname{div}v=0$ this makes $v^\flat$ harmonic, so $v=0$. This reproduces the known nonexistence at $\alpha=1$ (Shvydkoy, Proposition 2.1) by a different route, and serves only as a consistency check.
- The linearization of (E1)-(E3) at the trivial solution is $\operatorname{div}v=-(2-\alpha)f$, $P=0$, which has an infinite-dimensional kernel (every smooth tangent field $v$, with $f=-\operatorname{div}v/(2-\alpha)$). So the implicit-function theorem cannot be applied directly at the trivial solution. We did not investigate bifurcation or constrained reductions.

## 12. Other strategies examined

- **The pressure (successful).** Part II worked with the Bernoulli function $H$, whose sign and transport law (T1) carry no information about the curvature of the sphere. The pressure equation (0.1) does contain the curvature, through the Bochner identity. At critical points of $P$ the momentum equation determines the trace term, and this gives the minimum principle of Section 0. We had not examined the pressure equation before; the referee found the argument while working on the local charge problem of Section 10.2.
- **Global integrated identities.** All identities of the form $\int\operatorname{div}(\Phi(f,H)v)=0$, together with Lemma 3.3 and $\int f\,k(H)\,dS=0$, are satisfied by the reduced-only rigid rotation above. They cannot give a contradiction alone.
- **Trajectory arguments for the sign of $H$.** Along an orbit in $\{H<0\}$, (T2) shows that $f$ is strictly decreasing. For $1<\alpha<2$ this alone gives no contradiction, so the divergence (invariant measure) argument of Theorem A is needed.
- **Hodge theory and topology.** These are incorporated in Theorems B and E: $H^1_{dR}(S^2)=0$ gives the global stream function, and the closed form $\theta$ forces nontrivial topology of $U$.
- **Vorticity equation.** Lemma 3.1(h) is the stationary vorticity equation in spherical form. It is not used in the proofs of Theorems A to I, which rely on (a)-(g); those follow directly from (E1)-(E3). We did not find a further use of (h).
- **Spectral obstructions.** Beyond the degree-one ansatz we did not pursue a spherical-harmonic analysis. The equations are quadratic, and we did not find a spectral quantity with a definite sign.
- **Changing the form or the test functions.** Adding to $\tilde\theta$ an exact form $dg$ with $g\in W^{1,2}(S^2)$ does not change $T$, and the pairings of $T$ with functions of $\Psi$ are given for every solution by the identity of Proposition D.2, so neither can produce a contradiction by itself.
- **Regularity bootstrap.** Stationary Euler does not regularize. The shear solutions of Section 11 show that $C^\infty$ solutions need not be analytic on $U$, and that a $C^2$ local solution with $H>0$ need not be $C^3$. So Theorem N.3 cannot be applied to $C^2$ solutions by first improving their regularity by a local argument.
- **Perturbation near the endpoints.** At $\alpha=1$ there are no nontrivial solutions. At $\alpha=2$ the radial source cannot be continued (Section 11). Bifurcation from the trivial solution is degenerate.

## 13. Literature provenance

- **Section 0.** Formula (0.1) is the angular form of the classical pressure equation $-\Delta p=\operatorname{tr}\big((Du)^2\big)$ for the Euler equations. Lemma 0.1 is the classical Bochner identity for vector fields (with the Ricci identity). The following were first obtained by the referee, an independent second model (Section 15), in answer to a question of ours about the local charge problem of Section 10.2:
  - the pressure minimum principle (Theorem 2, items 2 to 4), with the Hessian formula (0.2);
  - the $C^2$ proof of Theorem 1;
  - the version for curvature $K\ge1$ (Section 10.1);
  - Corollary 3, for $1<\alpha<2$.

  The finish of the proof of Theorem 1 through the maximum of $f^2$ was suggested in an internal review that the referee ran with a second instance of the same model. The alternative finish by integrating $\operatorname{div}(fv)$ is the referee's. The step "$P\ge0$ implies trivial" is Shvydkoy's Corollary 4.4. Ours are the extension to $C^1$ solutions (Lemma 0.2 and Proposition 0.3), the range $0<\alpha<2$ in Corollary 3, the written proofs in Section 0, and the tests in Section 11. Maximum principles are a standard tool for stationary and self-similar problems (Chae 2015; Šverák's work on Landau solutions; Section 2). We did not find the pressure minimum principle, or Theorem 1, in the literature we searched. We make no claim of novelty beyond that statement.
- The spherical system, the Bernoulli transport law (T1), Propositions 2.1, 3.1, 3.2, 4.1 and Corollary 4.4 are due to Shvydkoy (2018). Identities (b), (c) and (h) of Lemma 3.1 are his (24b), (24a) and (28b), rewritten via $u_S=J\eta^\sharp$.
- The identities $\eta(v)=-\alpha H$, $dH\wedge\eta=-2\alpha H\zeta\mu$, $d\eta=(1-\alpha)\zeta\mu$ and $d(H^\gamma\eta)=0$ were stated in the task; we proved and checked them.
- Lemma 6.3 is a consequence of Shvydkoy's Remark 6.2, equation (62), which states $\int_{S^2}\zeta H^n\,dS=0$ for all integers $n\ge0$ (in our notation); polynomial approximation on the range of $H$ gives Lemma 6.3. We rederived it by a different argument. Similarly, the identities $\int f\,k(H)\,dS=0$ mentioned in Section 12 extend his Lemma 6.1, equation (60).
- The weight $H^\beta$ and the divergence-free field $H^\beta v$ have an axisymmetric predecessor in Shvydkoy's conserved quantity (40), used in his Proposition 5.1. Abe (2024) uses the analogous conserved quantity in the axisymmetric class.
- The nonexistence results for the Beltrami, axisymmetric and radially irrotational classes are Abe's (Theorems 1.1, 1.3, 1.4, 1.5) and Shvydkoy's (Proposition 5.1). Corollary 6.2 recovers the consequence "$\zeta\equiv0$ implies trivial" for $1<\alpha<2$, which also follows from Abe's results.
- The sign lemma $H\ge0$ and the cutoff strategy for proving it were proposed in the task. Theorem A carries out that strategy.
- The tools are standard:
  - the Glaeser-type inequality $|\nabla H|^2\le2LH$ for nonnegative $C^2$ functions (G. Glaeser, *Racine carrée d'une fonction différentiable*, Ann. Inst. Fourier 13 (1963) 203-210);
  - Schauder estimates;
  - the coarea formula;
  - Sard's lemma in one dimension;
  - Ehresmann's fibration theorem;
  - the Poincaré-Bendixson theorem and the monotonicity of transversal crossings;
  - the stable manifold theorem (P. Hartman, *Ordinary Differential Equations*, 2nd edition, Birkhäuser 1982, reprinted by SIAM 2002);
  - the Poincaré index theorem;
  - Łojasiewicz's inequality.
- Lemma 7.5 (Proposition K) was first obtained by the referee (an independent second model, Section 15) and checked by us. Theorem J was drafted by us; the referee found gaps in the draft (order of the resolution steps, localization, flow-box coordinates, transversal counts) and supplied the repairs incorporated in Section 8.
- The resolution theory used in Lemma 8.2: A. Seidenberg, *Reduction of singularities of the differential equation $A\,dy=B\,dx$*, Amer. J. Math. 90 (1968) 248-269, in the form stated by F. Cano, *Reduction of the singularities of codimension one singular foliations in dimension three*, Ann. of Math. 160 (2004) 907-1011, pp. 910-912; the real case as in F. Dumortier, *Singularities of vector fields on the plane*, J. Differential Equations 23 (1977) 53-106, and F. Dumortier, J. Llibre and J. C. Artés, *Qualitative theory of planar differential systems* (Springer, 2006), Chapter 3; embedded resolution and monomialization: E. Bierstone and P. Milman, *Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant*, Invent. Math. 128 (1997) 207-302, (0.2)(2) and Theorems 1.6 and 1.10; finiteness of connected components of compact analytic sets: E. Bierstone and P. Milman, *Semianalytic and subanalytic sets*, Publ. Math. IHES 67 (1988) 5-42, Corollary 2.7.
- Theorem L: item 1 for $\lambda=0$ and item 3 for finite $Z$ were first obtained by the referee; the weighted form of item 1, items 2, 4 and 5, and the capacity form of item 3 are ours. Theorem M: item 1 at points of $Z_0$, item 2 (with a weaker dimension bound) and item 5 were first obtained by the referee; the eigenvalue statement of item 1 at all points of $Z$, and items 3 and 4, are ours. Theorem N, with Lemmas 8.7 and 8.8 and the fat Cantor example of Section 10.2, was first obtained by the referee, building on Theorem M; we checked every step and wrote the proof given in Section 8. The local shear solutions of Section 11 are elementary parallel shear flows; the referee used them to show that analyticity fails in $U$, and the computation of $\theta$ and of $d\tilde\theta=0$ for them is ours. The locally sharp example for $\lambda_*$ in Section 10.2 is the referee's.
- Potential theory and geometric measure theory used in Theorems L, M and N: Sobolev capacity and its relation to logarithmic capacity (D. R. Adams and L. I. Hedberg, *Function Spaces and Potential Theory*, Springer 1996); Hausdorff measures, covering arguments and Frostman's lemma (P. Mattila, *Geometry of Sets and Measures in Euclidean Spaces: Fractals and Rectifiability*, Cambridge University Press 1995); positive logarithmic capacity, hence positive Sobolev capacity, of compact planar sets of positive Hausdorff dimension (L. Carleson, *Selected Problems on Exceptional Sets*, Van Nostrand 1967); the implicit function theorem.
- The shell identity, Theorems B through G, I and J, Lemma 8.1 and Propositions D and H (except Lemma 6.3, see above), and the parts of Theorems L and M credited to us above, were derived in this work. We did not find them in the literature we searched (Section 2). We make no claim of novelty beyond that statement, and some of them may be known in other contexts, for example weighted invariant measures for flows with a transported Bernoulli function.

## 14. Recommended next research step

**Weak homogeneous solutions below $C^1$.** Fix $0<\alpha<2$ (or first $1<\alpha<2$). Decide whether there is a nonzero pair
$$u(r\omega)=r^{-\alpha}\big(v(\omega)+f(\omega)\omega\big),\qquad p(r\omega)=r^{-2\alpha}P(\omega),$$
with $v,f\in C^{0,\sigma}(S^2)$ for some $0<\sigma<1$ and $P\in L^1(S^2)$, that solves the stationary Euler equations $\operatorname{div}u=0$, $\operatorname{div}(u\otimes u)+\nabla p=0$ in the sense of distributions on $\mathbb R^3\setminus\{0\}$.

Here is why this is the natural next question. Theorem 1 needs $v,f\in C^1$. It uses the equations pointwise at a minimum point of $P$, and near it the continuity of $Dv$. In the weak setting neither the trace term $\operatorname{tr}(A^2)$ at a critical point nor the Hessian identity (0.2) at a stagnation point is available. On the other hand, weak solutions of the stationary Euler equations satisfy an h-principle (A. Choffrut and L. Székelyhidi, *Weak solutions to the stationary incompressible Euler equations*, arXiv:1401.4301). So a negative answer would extend Theorem 1, and a positive answer would show that some regularity hypothesis is needed; it would not by itself show that $C^1$ is the optimal threshold. Two concrete first steps:

- *Toward nonexistence:* prove the minimum principle for profiles in $W^{1,q}(S^2)$, $q>2$. For such profiles $\operatorname{tr}(A^2)\in L^{q/2}$, and (0.1) should hold in the sense of distributions by the density argument of Lemma 0.2 (we have not written this out). The task is to replace the pointwise evaluation at the minimum point by an estimate on small disks around it, using $\Delta P$ in place of the Hessian.
- *Toward existence:* adapt convex integration to the homogeneous ansatz. Because of the ansatz the problem becomes one on $S^2$ for $(v,f,P)$, with the conservative weak form of (E1)-(E3) given in Section 10.1. For $1<\alpha<2$ any such solution must have $P<0$ on a set of positive measure. The reason is the second equation of that weak form, $\operatorname{div}(fv)=Q+2(\alpha-1)f^2+2\alpha P$ (for $C^1$ profiles a consequence of (E1) and (E2), third remark after Corollary 3), which is the radial momentum equation. Testing it with the constant function $1$ gives $2\alpha\int P\,dS=-\int(Q+2(\alpha-1)f^2)\,dS$, which is negative unless $v=f=0$; and if $v=f=0$, the same equation gives $P=0$. Equivalently, test the momentum equation $\operatorname{div}(u\otimes u)+\nabla p=0$ with the radial field $\psi(|x|)x$, $\psi\in C^\infty_c(0,\infty)$, and use the homogeneity: the result is $\int_0^\infty r^{2-2\alpha}\psi(r)\,dr$ times the same integral. This argument needs only the weak form of the equations and $Q,f^2,P\in L^1(S^2)$.

## 15. How the results were verified

- **Proofs.** The proofs of the results stated as theorems, propositions, lemmas and corollaries are written out in full in this report and were checked step by step. Remarks that use standard facts cite them, and statements marked "not proved" in Section 9 are not claimed.
- **Symbolic checks.** These were done with sympy:
  - for Section 0, with a script written independently of the referee's: in coordinates on the round sphere and for arbitrary functions and symbolic $\alpha$, the Bochner identity (0.3), and the difference of the two sides of (0.1), which equals $\operatorname{div}R_3-v(R_1)+(\alpha-1)fR_1+R_2$ with $R_1,R_2,R_3$ the residuals of (E1)-(E3); the Hessian computation at a stagnation point, the Cayley-Hamilton reduction to (0.2), and the bound of Theorem 2.3 in the form $\frac{\alpha(\alpha-2)}2f^2-(f\operatorname{tr}A+2\det A)=\frac12\big(\lambda_1-\lambda_2\big)^2\ge0$ for $A$ self-adjoint with eigenvalues $\lambda_1,\lambda_2$; and (0.1) on the exact solutions listed in Section 11; and, for a general conformal metric $e^{2\lambda}(dx^2+dy^2)$ with curvature $K=-e^{-2\lambda}\Delta_0\lambda$ and arbitrary $v,f,P$, the Bochner identity with the term $KQ$ and the version of (0.1) with the term $(1-K)Q$ of Section 10.1 (again modulo the residuals of (E1)-(E3));
  - the reduction of the Cartesian Euler equations to (E1)-(E3), (T1), (T2) and the identities of Lemma 3.1, including the cutoff and shell derivative formulas (all residuals zero);
  - the vorticity transport identity (h) as $\operatorname{curl}$(E3) combined with (E1);
  - formula (7.1), the vanishing of its antisymmetric part up to $\zeta f J$, and the trace formula;
  - the stagnation-point classification;
  - the swirl and rigid-rotation examples;
  - the closed form of the residual $R$ for the degree-one ansatz (the difference between $R$ and the stated formula reduces to zero modulo $|\omega|^2=1$).

  These checks confirm algebraic identities; they are not certificates for the analytic arguments, which rest on the written proofs.
- **Independent audit.** This report was written by an AI model, which also carried out most of the research. A second, independent AI model (GPT-6, run through the Codex tool) was used as a referee, as a parallel researcher on specific questions, and for literature and algebra checks. Results first obtained by the referee are marked as such where they are stated (Theorem 2 and the $C^2$ proof of Theorem 1, Proposition K, Theorems L, M, N, Section 13). The referee was asked to find errors, and all its claims were checked by us before being used. Verification in this report therefore means an independent audit by a second model plus our own line-by-line check, not a formal proof check.
  - For Section 0, the referee found the pressure minimum principle and the $C^2$ proof of Theorem 1 while working on the local charge problem of Section 10.2. It also ran an internal review with a second instance of the same model, which confirmed the argument and suggested the finish through the maximum of $f^2$, and it checked the pressure identity symbolically. We checked every step by hand: the Bochner identity and its curvature sign, the coefficient of $v(f)$ after taking the divergence of (E3), the cancellation of $\operatorname{tr}(A^2)$ at nonstagnant critical points (which needs no symmetry of $A$), the order of differentiation and evaluation at stagnation points, and Cayley-Hamilton. We also checked these steps with a symbolic script of our own (above). We then wrote Section 0, adding the extension to $C^1$ solutions, and submitted it, together with Section 1, to an adversarial audit by the referee with a list of points to attack. The audit found the reduction, Lemma 0.1, Theorems 1 and 2, Corollary 3, Lemma 0.2 and Proposition 0.3 correct. It confirmed (0.1) independently by a Euclidean computation of $\operatorname{tr}((Du)^2)$ in a tangent-radial block form, and it gave the exact formula $\Delta P=\frac{\alpha(\alpha-2)}2f^2-\frac12(\lambda_1-\lambda_2)^2$ at stagnation points with $f\ne0$. It showed by an example why the exactness of $dP$ is needed in the $C^1$ stagnation case (a matrix $A_0$ satisfying the trace condition with $L$ not symmetric). It found three minor defects, which we corrected:
    - Theorem 2 claimed item 4 for $C^1$ solutions on an open set, but Lemma 0.2 and Proposition 0.3 were stated on $S^2$. We added the localization by a cutoff.
    - The swirl remark needed the amplitude $a\ne0$.
    - The remark on $\alpha<0$ was narrowed to the example $\alpha=-1$, and the regularity of Abe's solutions for $\alpha<0$ (continuous) is now stated.

    A final audit of the whole assembled report, again adversarial and with a list of points to attack, found no gap in Theorem 1, for $C^2$ or for $C^1$ profiles, and confirmed the reduction of Section 1 for $C^1$ profiles, the computations of Section 0 and the tests of Section 11. It found errors and overstatements in the surrounding material, which we corrected:
    - Section 10.1 claimed that item 2 of Theorem 2 holds verbatim for metrics with $K\ge1$. It holds with the additional term $(1-K)Q\le0$, which suffices; the $C^1$ case is now included.
    - Several claims that Part II does not depend on the metric did not distinguish the value of the curvature from the topology of $S^2$, and from the analyticity of the metric used in Theorem J.
    - Some summaries omitted the hypothesis that the solution is nontrivial (the positive mean of $H$, the nonzero defect, the absence of closed extensions of $\theta$), and a table row omitted the hypothesis $f\ne0$.
    - The fat Cantor example of Section 10.2 also excludes the endpoint $b=\alpha/(2-\alpha)$.
    - The candidate geometries of Section 10.2 were described as compatible with all constraints. They are only not excluded by the stated estimates, and Hausdorff dimension at least $2/\alpha$ does not imply that a set is not $\sigma$-finite for $\mathcal H^{2/\alpha}$.
    - The remark that regularity cannot be bootstrapped rested on an example about analyticity. It now uses a shear solution that is $C^2$ but not $C^3$, proposed by the referee, and it is stated as a local fact.
    - The weak formulation in Sections 10.1 and 14 is now the conservative system on $S^2$.
    - A normalization of the pressure at $\alpha=0$ in Section 2 was wrong.
    - In this section two literature overlaps had been conflated, and some cross-references pointed in the wrong direction.
    - The cubic test of Section 11 rested on a numerical residual; it is now an exact computation.
    - The capacity remark after the proof of Theorem L was a sketch; it is now written out, following the referee's completion of the argument.

    The referee had no network access during this audit. A separate literature audit by the referee, with web access, searched for Theorem 1 and for the pressure minimum principle and checked the citations of Sections 2 and 13. It found neither result in the literature it searched. It corrected several citations (titles and publication data, the qualifier "rotational" in Abe's Theorems 1.4 and 1.5, and the independent treatment of $\alpha=1$ by Monneau, Paszkowski and Xue mentioned by Shvydkoy), and we checked these corrections against the papers where they were available. The final audit also asked that the attribution of results to the two models be removed from the mathematical text. We kept it in a factual form, because the provenance of the results and the method of verification have to be stated.
  - For Theorem A, the referee checked the proof in full and found it correct, with no gap. In particular it confirmed that the cutoff vector field is $C^2$, that its divergence is exactly $2\alpha\varepsilon^\beta f\,t^{1+\beta}\chi'(t)$, and that the sign argument needs no assumption on the zero set.
  - For Theorems B to H (Sections 5 to 8), the referee checked every lemma and step and found all stated theorems correct as stated, including the Hölder and Schauder regularity in Lemmas 5.1-5.3, the covering estimate $|\Psi(S)|\le C\delta^{2/\alpha-1}$, the constants and inequality directions in Theorem C, the $C^1$ regularity of $\phi$ in Lemma 6.3, the order of the limits in Proposition D.3, the rank-one case of Lemma 7.1, formula (7.1) and its antisymmetric part, the index and parity arguments and the period bound in Theorem G, and the transversal argument in Proposition H. It found errors in the surrounding interpretation, which have been corrected in this version: an earlier version called the limiting defect of Proposition D a measure and its $\Psi$-moment a total mass; listed periodic orbits inside $Z_0$ as a remaining configuration (they cannot exist, Section 10.2); asserted a localized form of (10.1) near $\partial(\operatorname{int}Z)$; posed an earlier version of the recommended next step (a local degenerate centre, since made obsolete by Theorem L.3) on geodesic disks, for which the reduction from Theorem G fails; described the degree-one ansatz test by a Gröbner computation at finitely many parameter values (replaced by the analytic argument in Section 11, whose residual formula the referee supplied); claimed a false dependency on Lemma 3.1(h); and omitted the overlap of Lemma 6.3 with Shvydkoy's Remark 6.2, equation (62), and, separately, the overlap of the class $H\equiv0$ with the geodesible solutions excluded by Theorem 5.1 of Abe, Sato and Xie. It also asked that several statements of the form "nothing bounds the vanishing order" be weakened to "we found no bound", which has been done.
  - For Lemma 8.1 and Theorem I, the referee found the constant in (8.1), the logarithmic radial bound, the one-turn closure, the doubling step and the conversion to normal coordinates correct. It asked for the doubling hypothesis to be restricted to $0<r<r_0/2$ and applied downward, for the informal summary of Lemma 8.1 to state the correct regime $\ell\bar a^{1/\alpha}/|\oint\theta|\to0$, and for the quasi-homogeneous extension in the remark to be stated as conditional. These changes have been made.
  - Lemma 7.5 was found by the referee while auditing a weaker statement of ours (that $v$ and $f$ vanish almost everywhere on $Z$), and its inequality $f^2<H$ while auditing a description of the flow on $U$ in the coordinates $(\Psi,\int\theta)$, which is not part of this report. We checked both proofs step by step, including the three eigenvalue cases for the orbit converging to $z$ and the formula for $dy/dt$, which we rederived from (T1) and (T2).
  - For Theorem J, the referee audited a draft of ours and judged it correct with fixable gaps, and wrote out a repaired proof. The gaps were: the reduction theorem for foliations alone does not give the resolution properties (R1)-(R4) for the vector field with its scalar factor and the Jacobian (repaired by the order of the steps in Lemma 8.2: first the divisor of the common factor, then the isolated zeros, then the saturated foliation; it also supplied the example $y(x^2+y^2)$ showing that the real zero set alone does not suffice); the localization of the annulus before lifting; the sign of the time change (positive time measures are used in (8.5)); a flow-box argument that did not exclude entry through the top side (replaced by genuine flow-box coordinates (8.6)); and the counting of passages, which it simplified using $F=\Psi\circ\pi$. It checked the cancellation of the $dm$ terms in Lemma 8.3, the odd and even $k$ argument and the corner estimates, and found no defect there. We checked each repair against our draft and independently rechecked the lift formulas, the integration giving $|P\circ\pi|\le Cm^2$, and that every centre of a blow-up is a zero of the lift of $v$. The proof in Section 8 is the repaired one.
  - For the coordinates $(\Psi,\int\theta)$ of Section 10.2, the referee confirmed the local reduction for any metric, with a corrected sign of the area form; we reran its symbolic script and checked its formula for $d(f/\sqrt H)/dt$, which gives $f^2<H$, by hand from (T1) and (T2).
  - For Theorem L, the referee first proved item 1 with $\lambda=0$ and item 3 for finite $Z$, in answer to a question about a top end for a free metric; we checked every step (the weighted divergence identity and its coefficient of $f^2$, the convex regularization in Lemma 8.4, the integration by parts, the logarithmic divergence on small circles). A separate audit of our weighted version and of items 2, 4 and 5 found all of them valid. It found a normalization defect in a draft definition of capacity (a definition using only $\int|\nabla\phi|^2$ declares $S^2$ itself of capacity zero), which we had already repaired by including $\int\phi^2$; it asked for the compact-support argument in item 2 and the closure formula and collar argument in item 4, which are in Section 8; and it supplied the locally sharp example for $\lambda_*$ quoted in Section 10.2.
  - For Theorem M, items 1 (at points of $Z_0$) and 2 were first obtained by the referee in answer to a question about totally disconnected zero sets, with the dimension bound $2(2-\alpha)/\alpha$, and item 5 in answer to a question about continuum top ends. We checked both proofs line by line (the Laplacian of $H$ at a zero, the exponent in $d\Theta_\varepsilon$, the sublevel bound, the saddle argument, the strip identity and the one-dimensional lemma along collar curves). An adversarial audit of our write-up then found items 1 to 5 correct. While writing the version in Section 8 we corrected three defects of our own draft that the audit had not flagged: the support statement now cites Lemmas 6.1 and 7.1; the covering estimate in item 4 carries the factor $\|\varphi\|_\infty$; the top-end corollary of item 5 uses the closed annulus and a homotopy equivalence.
  - Theorem N, Lemmas 8.7 and 8.8 and the fat Cantor example were first obtained by the referee, in answer to a question about defect supports of positive area; an audit of Theorem M independently proposed the vanishing of second derivatives on $K$. We checked every step: the cutoff with bounded overlap, the use of $f=0$ on $Z$ to keep the factor $A_E$, the implicit function step, the covering argument for non-$\sigma$-finiteness, the Taylor bounds for $C^{k,\sigma}$ data and the exponent bookkeeping. A final line-by-line audit of the written proofs of Theorems M and N in Section 8 found all items correct and asked for six minor corrections, which we made: the case $a(r)=0$ in the proof of N.2 is now treated explicitly; the remark after Theorem M no longer says that the whole $1$-jet of $\zeta$ vanishes on $\operatorname{supp}T$ without citing N.1; two support statements for cutoffs were made precise ("vanishes outside", and a profile vanishing on $[7/2,\infty)$); the vanishing of second derivatives at density points of $Z$ is now justified; and two remarks were narrowed to what is proved (the $C^1$ case of the collar theorem, and second derivatives at points of $Z_0\setminus K$). It also confirmed the Taylor bounds for $C^{k,\sigma}$ data and the endpoint case $k+\sigma=2\alpha$, where $A_K(4r)\to0$ replaces a power of $r$.
  - Further referee answers are used only as remarks or not at all: an analysis of top ends in the coordinates $(\Psi,\int\theta)$ (which corrected signs in our notes and showed, by a counterexample, that a description of slow orbit arcs we had proposed does not follow; those notes are not part of this report); a version of Theorem J for $C^\infty$ data with a Łojasiewicz bound at an isolated centre, superseded by Theorem L.3 and not checked line by line; an exclusion of top ends at a point with positive definite leading term, superseded by Theorem L.4; and the curvature analysis mentioned in Section 10.2 (degenerate symbol, failure of analyticity, a Gauss-Bonnet condition at the top end), whose symbolic formulas we did not recheck by hand, apart from the shear solutions.
  - In several answers the referee reported that its own attempt to consult a further model failed for lack of credentials; no other model contributed.
  - The referee searched the literature through October 2026 and found no unrestricted nonexistence theorem for globally $C^2$ profiles with $1<\alpha<2$; it noted that its search does not certify absence from the whole literature. A final priority search (with web access) and a citation check of Sections 2 and 13 are described in the audit record above; they did not find Theorem 1 or the pressure minimum principle, which is not a proof of novelty.
