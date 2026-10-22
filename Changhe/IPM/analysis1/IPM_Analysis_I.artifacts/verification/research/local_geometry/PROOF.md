# Local normalization, characteristic identities, and failed positivity tests

Status: the propositions below have direct analytic proofs. They do not assert existence of an exact profile. Date: 2026-10-20.

## Normalization under continuous factorization

Suppose $\rho\in C^1$ near zero has the symmetries in PROMPT.md and $\rho(x,y)=x^2y\,a(x,y)$ with $a$ continuous and $a(0)=1$. Suppose $U\in C^1$ near zero has the prescribed velocity parity, is divergence free, and $U=(-\psi_y,\psi_x)$ with $\psi_{xy}(0)=c$. If $(c_lX+U)\cdot\nabla\rho=\rho$, then $3c_l-c=1$.

To avoid differentiating the merely continuous factor, set $\rho_\epsilon(X)=\epsilon^{-3}\rho(\epsilon X)$ and $V_\epsilon(X)=\epsilon^{-1}(c_l\epsilon X+U(\epsilon X))$. On any fixed compact set, $\rho_\epsilon\to x^2y$ uniformly and $V_\epsilon\to AX$ in $C^1$, where parity and incompressibility give $A=\operatorname{diag}(c_l-c,c_l+c)$. The equation is $\operatorname{div}(V_\epsilon\rho_\epsilon)=(1+2c_l)\rho_\epsilon$. Passing to distributions is legitimate by the stated convergence. The limit is $AX\cdot\nabla(x^2y)=x^2y$, which gives $2(c_l-c)+(c_l+c)=1$.

Consequently $DU(0)=\operatorname{diag}(-(3c_l-1),3c_l-1)$ and $DV(0)=\operatorname{diag}(1-2c_l,4c_l-1)$. This argument proves the normalization at the prompt's weak center regularity; a cubic Taylor comparison alone would need more justification.

## Exact perturbation and scalar defect

Assume a linear canonical map $\rho\mapsto U[\rho]$ and write $s[\rho]=\psi[\rho]_{xy}(0)$ and $c[h]=s[h]/3$. Let $\bar\rho$ have normalized center, and define $\bar V=\bar c_l X+U[\bar\rho]$, $G=X\cdot\nabla\bar\rho$, $\epsilon=\bar V\cdot\nabla\bar\rho-\bar\rho$, and

$$\delta=\frac{1+s[\bar\rho]}3-\bar c_l.$$

For a center-preserving correction $h$, the exact admissible exponent is $c_l=\bar c_l+\delta+c[h]$. Direct expansion gives

$$\bar V\cdot\nabla h-h+U[h]\cdot\nabla\bar\rho+c[h]G+(U[h]+c[h]X)\cdot\nabla h=-\epsilon-\delta G-\delta X\cdot\nabla h.$$

Thus when $\delta=0$ the linearization is $Lh=\bar V\cdot\nabla h-h+U[h]\cdot\nabla\bar\rho+c[h]G$. If $\delta\ne0$, the corrected residual is $\epsilon+\delta G$ and the corrected linear transport includes $\delta X\cdot\nabla h$. The omitted scalar defect cannot be treated as exactly zero because it is numerically small.

## Source identities

Suppose $\rho$ is $C^2$, $V$ is $C^1$, the stationary equation and parities hold, and write $w(x)=V_1(x,0)$, $b(x)=\partial_yV_2(x,0)$, $g(x)=\rho_y(x,0)$. Incompressibility of $U$ gives $w'+b=2c_l$. Differentiate the equation in $y$ on the axis. Because $\rho_x(x,0)=V_2(x,0)=0$, its only nonzero terms give

$$w g'+b g=g.$$

If $w(x_*)=0$ and $g(x_*)\ne0$, then $b(x_*)=1$ and $w'(x_*)=2c_l-1$. Velocity parity also gives the off-diagonal entries of $DV(x_*,0)$ equal to zero. If $c_l>1$, both eigenvalues are positive and the point is a hyperbolic source. Positivity of $g$ is stronger than needed for these equalities, but is needed in the integral formulas that divide by it.

Where $g\ne0$, elementary differentiation gives $(w/g)'=(2c_l-1)/g$. If $g>0$ on $(0,x_*]$, integration from $x$ to $x_*$ gives

$$w(x)=-(2c_l-1)g(x)\int_x^{x_*}\frac{dt}{g(t)}.$$

The further unrenormalized integral compatibility at zero requires an extra convergence assumption. A sufficient hypothesis is $g(x)=x^2(1+O(x^{1+\eta}))$ for some $\eta>0$, together with odd $C^2$ regularity of $w$. Let $J=\int_0^{x_*}(1/g-1/x^2)dt$. Expanding the last formula gives

$$w(x)=-(2c_l-1)x-(2c_l-1)(J-1/x_*)x^2+o(x^2).$$

An odd $C^2$ function has zero quadratic coefficient, so if $2c_l-1\ne0$, then $J=1/x_*$. In particular the sufficient condition $g=x^2(1+O(x^2))$ in the inherited report works. Merely writing $g\sim x^2$ does not guarantee convergence of this integral, so this strengthened compatibility must not be imported into $P_2$ without proof of the missing rate.

## Exact P2 regularity supplies the missing axis rate

Assume now that the exact profile is in $P_2$: $\rho\in C^{2,\alpha}_{\rm loc}(\mathbb R^2)$ for $0<\alpha<1$, and the canonical stream function solves its Poisson equation in distributions. Assume $A=2c_l-1\ne0$, $g>0$ on $(0,x_*]$, and $w(x_*)=0$. Then the integral compatibility in the preceding subsection does follow under these exact-profile hypotheses.

The local analytical dependency is interior Schauder regularity: a distributional solution of $-\Delta u=f$ with $f\in C^{1,\alpha}_{\rm loc}$ is in $C^{3,\alpha}_{\rm loc}$. To apply it here, $f=\rho_x$ has the required regularity. Localizing with a smooth cutoff writes $\psi$ as the Newtonian potential of localized $f$ plus a harmonic distribution. The harmonic distribution is smooth by Weyl's lemma; the localized potential has the stated Schauder regularity. Therefore $U\in C^{2,\alpha}_{\rm loc}$. This is a qualitative regularity input and supplies no certified global constant.

The first subsection gives $w'(0)=-A$. Oddness gives $w''(0)=0$. Write $w=-Ax+e$. Taylor's formula with the Holder continuous second derivative gives

$$|e(x)|\le C_0x^{2+\alpha},\qquad |e'(x)|\le C_1x^{1+\alpha}.$$

For example, on a fixed local interval one may take $C_1=[w'']_{C^\alpha}/(1+\alpha)$ and $C_0=C_1/(2+\alpha)$. The continuous density factor gives $g(x)=x^2a(x,0)$ directly by differentiating in $y$ on the axis, so $g/x^2\to1$.

The undivided equation already derived from the PDE is $wg'=(w'-A)g$. Near zero, choose $x_1>0$ with $C_0x_1^{1+\alpha}\le |A|/2$. Then $|w|\ge |A|x/2$ on $(0,x_1]$, and only on this interval divide by $w$ to obtain

$$\left(\log\frac{g}{x^2}\right)'=\frac{xe'-2e}{xw},\qquad
\left|\log\frac{g(x)}{x^2}\right|\le\frac{2(C_1+2C_0)}{|A|(1+\alpha)}x^{1+\alpha}.$$

The integration constant is zero because $g/x^2\to1$. Thus $g=x^2(1+O(x^{1+\alpha}))$, and $1/g-1/x^2=O(x^{\alpha-1})$ is integrable at zero.

For the global axis step, regularity is available on a neighborhood of the entire segment $[0,x_*]$ because the $P_2$ hypothesis is local on the full plane. Divide the undivided ODE by $g^2$, never by $w$, to get $(w/g)'=A/g$ on $(0,x_*]$. Hence the integral representation remains valid without presupposing that $w$ has no other zeros. With $J=\int_0^{x_*}(1/g-1/x^2)dx$, the established rate gives

$$w(x)=-Ax-A(J-1/x_*)x^2+O(x^{2+\alpha}).$$

Comparison with the odd $C^{2,\alpha}$ expansion proves $J=1/x_*$. The source location and positive-$g$ interval remain hypotheses, not consequences of a sampled trial. For quantitative use, the local Holder bound and the interval $x_1$ must be certified.

## The unweighted potential energy

Let $\Phi\in C_c^\infty(\mathbb R^2)$ be even in $x$ and odd in $y$, and put $h=-\Delta\Phi$. Then the canonical stream function for $h$ is $\Phi_x$, and $U[h]=(-\Phi_{xy},\Phi_{xx})$. Let $\bar\rho,\bar U$ be $C^1$, with $\operatorname{div}\bar U=0$, and $\bar V=\bar c_lX+\bar U$. All integrations below have compact support. Twice integrating by parts gives

$$-\int(\bar V\cdot\nabla h)\Phi=\int\nabla\Phi^T(2\bar c_lI+S(\bar U))\nabla\Phi.$$

Indeed, integration of the transport term once gives $\int h(\bar V\cdot\nabla\Phi+2\bar c_l\Phi)$. Replacing $h$ by $-\Delta\Phi$ produces $\int\nabla\Phi^TD\bar V^T\nabla\Phi+\frac12\int\bar V\cdot\nabla|\nabla\Phi|^2+2\bar c_l\int|\nabla\Phi|^2$. The middle integral equals $-\bar c_l\int|\nabla\Phi|^2$, cancelling the scalar part of $D\bar V$.

The term $+\int h\Phi$ equals $\int|\nabla\Phi|^2$. For the coupling, use divergence free $U[h]$ to get

$$-\int U[h]\cdot\nabla\bar\rho\,\Phi=\int\bar\rho(-\Phi_{xy}\Phi_x+\Phi_{xx}\Phi_y)=\int(\bar\rho_y\Phi_x^2-\bar\rho_x\Phi_x\Phi_y).$$

For the final equality, the first summand gives $\frac12\int\bar\rho_y\Phi_x^2$, while integrating the second in $x$ gives $-\int\bar\rho_x\Phi_x\Phi_y-\int\bar\rho\Phi_x\Phi_{xy}$, supplying the other half. Therefore

$$-\int L_0h\,\Phi=\int\nabla\Phi^TM_\Phi\nabla\Phi,\qquad M_\Phi=(1+2\bar c_l)I+S(\bar U)+\begin{pmatrix}\bar\rho_y&-\bar\rho_x/2\\-\bar\rho_x/2&0\end{pmatrix}.$$

If the background satisfies the center normalization exactly, then $M_\Phi(0)=\operatorname{diag}(2-\bar c_l,5\bar c_l)$. For $\bar c_l>2$ its first entry is negative. This creates actual negative parity-compatible tests even with $c[h]=0$: choose a small rectangle in the first quadrant where $M_{11}<-\eta<0$, a nonzero smooth cutoff $b$ supported there, and $\Phi_N=N^{-1}b\cos(Nx)$. Reflect evenly in $x$ and oddly in $y$, with disjoint supports away from both axes. Then $\Phi_x=-b\sin(Nx)+O(N^{-1})$ and $\Phi_y=O(N^{-1})$. Integration shows the quadratic form tends to $\frac12\int M_{11}b^2<0$ on the reflected supports; the oscillatory part tends to zero by integration by parts. Since $\Phi$ vanishes near zero, $c[h]=\Phi_{xxy}(0)/3=0$ and $h$ preserves the center factorization. Thus a uniformly positive bound in this pairing is false. This proves no claim about spectrum or invertibility.

## The old damping coefficient at the source

Where the continuous axis extension of $a_{tr}=\partial_x\bar V_2/\bar V_2$ exists, $d=1-\partial_x\bar V_1+a_{tr}\bar V_1$. At an exact source point with $b(x_*)=1$, the quotient has a finite local axis extension if the needed derivatives of $V$ exist, and $d(P)=1-w'(x_*)=2-2c_l$. Hence for $c_l>1$ the old global positive-damping hypothesis is false. Taking a smaller Holder exponent cannot change this sign.

## Scope

The source test is conditional on a source satisfying the stated identities; a sampled root of the trial does not certify one for an exact profile. The energy obstruction concerns this unweighted pairing only. The complete inverse problem and any geometry-adapted replacement remain open.
