# Kernels, rotations, and homogeneous Hölder spaces

Status: independently proved. These statements do not rely on a published sharp-norm formula.

## Statement and conventions

Fix $0<\alpha<1$. Write

$$[f]_\alpha=\sup_{x\ne y}\frac{|f(x)-f(y)|}{|x-y|^\alpha},\qquad
\dot C^\alpha(\mathbb R^2)=\{f:[f]_\alpha<\infty\}/\mathbb R.$$

Initially $f$ is real and belongs to $C_c^\infty(\mathbb R^2)$. The Fourier convention is $\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx$. Set $R_j=\partial_j(-\Delta)^{-1/2}$. For $z=r(\cos\theta,\sin\theta)\ne0$, let

$$K_{xx}(z)=\frac{\cos2\theta}{2\pi r^2},\qquad
K_{xy}(z)=\frac{\sin2\theta}{2\pi r^2}.$$

The associated principal-value convolution operators satisfy

$$T_{xx}=R_1^2+\tfrac12I,\qquad T_{xy}=R_1R_2.$$

Their multipliers, away from $\xi=0$, are

$$m_{xx}(\xi)=\frac{\xi_2^2-\xi_1^2}{2|\xi|^2},\qquad
m_{xy}(\xi)=-\frac{\xi_1\xi_2}{|\xi|^2}.$$

They extend canonically to operators modulo constants on $\dot C^\alpha$. Their operator norms agree. If $C_\alpha$ is this common norm and $D_\alpha$ is the norm of $R_1^2$, then $C_\alpha\le D_\alpha\le C_\alpha+1/2$. Also $C_\alpha\ge1/2$ and $D_\alpha\ge1$.

## Distributional calculation

The fundamental solution for $-\Delta$ in two dimensions is $G(z)=-(2\pi)^{-1}\log|z|$. Indeed, away from zero it is harmonic, while its outward radial derivative on a circle of radius $\epsilon$ is $-1/(2\pi\epsilon)$, with total flux $-1$. Integration by parts against a smooth compactly supported test function gives $-\Delta G=\delta_0$.

Away from zero,

$$\partial_i\partial_jG(z)=\frac{2z_i z_j-\delta_{ij}|z|^2}{2\pi|z|^4}.$$

To identify the local term, first differentiate $G$ once. Its first derivative is locally integrable. Integrating the next derivative over $|z|>\epsilon$ gives the displayed ordinary derivative plus the inner-boundary contribution

$$-\frac1{2\pi}\int_0^{2\pi}\omega_i\omega_j\varphi(\epsilon\omega)\,d\theta
\longrightarrow-\frac12\delta_{ij}\varphi(0).$$

The principal-value part exists because its angular mean is zero and $\varphi(z)-\varphi(0)=O(|z|)$. Consequently

$$\partial_i\partial_jG=\operatorname{pv}\frac{2z_i z_j-\delta_{ij}|z|^2}{2\pi|z|^4}
-\frac12\delta_{ij}\delta_0.$$

This proves the kernel signs, factors of $\pi$, and the diagonal local contribution. It also checks the trace: $R_1^2+R_2^2=-I$, while the two trace-free kernels sum to zero.

The Fourier symbols follow directly from $\widehat{\partial_j f}=i\xi_j\widehat f$ and the multiplier $|\xi|^{-1}$ of $(-\Delta)^{-1/2}$. Thus the symbol of $R_iR_j$ is $-\xi_i\xi_j/|\xi|^2$. The value assigned at the single point $\xi=0$ has no effect on the operator on test functions. On homogeneous spaces, additive constants are handled by the quotient definition rather than by assigning a multiplier at zero.

## Definition when the input grows at infinity

Choose a basepoint $b\in\mathbb R^2$. For $K=K_{xx}$ or $K_{xy}$, define

$$\mathcal T_bf(x)=\lim_{M\to\infty}\lim_{\epsilon\downarrow0}
\int_{|z-b|<M}\bigl(K(x-z)\mathbf1_{|x-z|>\epsilon}
-K(b-z)\mathbf1_{|b-z|>\epsilon}\bigr)(f(z)-f(b))\,dz.$$

The two local singularities are interpreted separately. Near $z=x$, replace $f(z)-f(b)$ by $f(z)-f(x)$; the removed constant has zero principal-value integral on every annulus centered at $x$. The remaining integrand is bounded in absolute value by $[f]_\alpha |z-x|^{\alpha-2}/(2\pi)$ and is locally integrable. The same argument applies at $b$. At infinity the kernel difference is $O(|x-b|\,|z-b|^{-3})$, while $|f(z)-f(b)|\le[f]_\alpha|z-b|^\alpha$. Its radial absolute integral is bounded by a constant times $\int_M^\infty r^{\alpha-2}\,dr$, which converges exactly in the range used here.

The integral of the kernel difference against any constant is zero. One way to check this is to truncate each kernel in its own centered ball, where angular cancellation makes both integrals zero, and then compare the shifted outer balls. The symmetric difference has area $O(M|x-b|)$, while $|K|=O(M^{-2})$, so the discrepancy tends to zero. Therefore the subtraction of $f(b)$ changes no increment and the construction is invariant under adding a constant to $f$.

It follows directly from the convergent difference formula that

$$\mathcal T_bf(x)-\mathcal T_bf(y)=\mathcal T_yf(x),\qquad
\mathcal T_bf(b)=0.$$

Changing $b$ only changes the output by an additive constant. For compactly supported smooth $f$, the ordinary principal-value convolution exists at each point, and $\mathcal T_bf(x)=Tf(x)-Tf(b)$. The upper-bound proof in `../02_upper_bounds/PROOF.md` establishes that these increments have finite alpha-Hölder seminorm. No density of $C_c^\infty$ in the full homogeneous space is asserted or needed for defining this extension.

## Rotation and the norm equality

Let $Q_\beta$ be counterclockwise rotation by $\beta$, and let $U_\beta f(x)=f(Q_\beta x)$. This is an isometry for the Euclidean Hölder seminorm, on real inputs and on the quotient by constants. A change of variables in the principal-value kernels gives

$$U_\beta^{-1}T_{xx}U_\beta
=\cos(2\beta)T_{xx}+\sin(2\beta)T_{xy}.$$

The same equality follows from evaluating $m_{xx}(Q_\beta^{-1}\xi)$. In particular, $U_{\pi/4}^{-1}T_{xx}U_{\pi/4}=T_{xy}$. The inverse conjugacy gives both directions of the norm comparison, proving equality. These identities also hold for the increment definition above, because rotation transforms the basepoint and any resulting normalization difference is constant.

Rotation by $\pi/2$ conjugates $T=T_{xx}$ to $-T$. Hence $T-I/2$ and $T+I/2$ have equal norm $D_\alpha$. Since $T=((T-I/2)+(T+I/2))/2$, the triangle inequality now gives the stronger comparison

$$C_\alpha\le D_\alpha\le C_\alpha+1/2.$$

For the elementary lower bounds, take the bounded homogeneous-space input $f(x)=\cos x_1$. The verified multipliers, or direct integration of the kernels, give $R_1^2f=-f$ and $T_{xx}f=-f/2$ modulo constants. Its Hölder seminorm is finite and nonzero for every $0<\alpha<1$. Therefore $D_\alpha\ge1$ and $C_\alpha\ge1/2$. The approximation lemma in the upper-bound proof transfers these lower bounds to the suprema over smooth compactly supported inputs.

## Complex convention

Define the classical Beurling transform $B$ here by the kernel $-1/(\pi z^2)$ on the complex plane. Its multiplier is $(\xi_1-i\xi_2)^2/|\xi|^2$. Complex conjugation of the operator, meaning $\overline{B\overline f}$, has kernel $-1/(\pi\overline z^2)$. Hence

$$T_{xx}+iT_{xy}=-\tfrac12\overline{B\overline{\cdot}}
=\tfrac12(R_1+iR_2)^2.$$

There is also an exact real-input norm relation. Write $S=T_{xx}+iT_{xy}$. For every fixed output increment,

$$|Sf(x)-Sf(y)|=\sup_\gamma|\operatorname{Re}(e^{-i\gamma}(Sf(x)-Sf(y)))|.$$

Every scalar projected operator is $\cos\gamma T_{xx}+\sin\gamma T_{xy}$, which is rotation-conjugate to $T_{xx}$ and has norm $C_\alpha$. Taking the suprema in either order shows

$$\|S\|_{\text{real }\dot C^\alpha\to\text{complex }\dot C^\alpha}=C_\alpha,
\qquad
\|B\|_{\text{real }\dot C^\alpha\to\text{complex }\dot C^\alpha}=2C_\alpha.$$

This statement restricts the input to real functions. No equality with the norm on arbitrary complex inputs is asserted.

## Dependencies and scope

The proof uses distributional integration by parts, the Fourier derivative convention, and elementary kernel cancellation. The homogeneous extension needs $0<\alpha<1$. It does not cover endpoint Lipschitz spaces or arbitrary pointwise definitions at infinity. No full inhomogeneous $C^\alpha$ operator norm is claimed.
