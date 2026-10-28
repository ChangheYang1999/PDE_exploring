# The exact second term for the diagonal Riesz transform

## Theorem and conventions

For $0<\alpha<1$, equip real functions on $\mathbb R^2$, modulo constants, with

$$[f]_\alpha=\sup_{p\ne q}\frac{|f(p)-f(q)|}{|p-q|^\alpha}.$$

Let $T_{xx}$ and $T_{xy}$ have principal-value kernels

$$K_{xx}(z)=\frac{z_1^2-z_2^2}{2\pi|z|^4},\qquad K_{xy}(z)=\frac{z_1z_2}{\pi|z|^4},$$

and set $R_1^2=T_{xx}-I/2$. For functions of finite homogeneous Hölder seminorm, singular-integral increments are defined by subtracting the value at each local pole and using the kernel difference at infinity, as proved in `../../01_setup/PROOF.md`. Write $C_\alpha=\|T_{xx}\|=\|T_{xy}\|$ and $D_\alpha=\|R_1^2\|$ for these seminorm operator norms. These norms equal the suprema over real $C_c^\infty$ inputs, by the compact approximation theorem in the same reference.

Then

$$\boxed{D_\alpha=\frac2{\pi\alpha}+1+\frac{2(\log2-1)}\pi+o(1)\qquad(\alpha\downarrow0).}$$

Together with the proved expansion for $C_\alpha$, this gives

$$\boxed{D_\alpha-C_\alpha\longrightarrow C_0:=\frac12+\frac{\log2-1}\pi.}$$

In particular the exact additive second term of $D_\alpha$ is $2C_0$. No formula for the full finite-exponent sharp norm is asserted.

The proof uses three previously checked results: the phase-uniform local-projection upper bound in `../../08_improved_upper_bounds/local_projection/PROOF.md`; the circular finite part in `../../06_small_alpha_second_term/diagonal/PROOF.md`; and the elementary local-profile bound in `../local_projection_profile/PROOF.md`. The global assembly argument is proved in `../projection_assembly/PROOF.md`. The operator-value argument, including the effect of the clamp, is given below.

## The upper limit

The local-projection theorem gives

$$\limsup_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)\le2C_0.$$

For context, that theorem replaces the local angular constant $a_2(\alpha)$ by

$$A_\alpha=\frac{\Gamma((\alpha+2)/2)}{2\sqrt\pi\,\Gamma((\alpha+3)/2)}$$

and puts the remaining local measure together with the identity term into a positive measure of mass $1/2$. Since $A_0=1/\pi$ and $A'_0=(\log2-1)/\pi$, this changes the trace-free second term by exactly $C_0$. The estimate is uniform in the kernel phase, so it bounds the full norm.

## The witness

Rotation conjugates $T_{xx}-I/2$ to $T_{xy}-I/2$ without changing the seminorm. We therefore use the functional

$$\Phi_\alpha(f)=(T_{xy}-I/2)f(x)-(T_{xy}-I/2)f(y),\qquad x=(1/2,0),\quad y=-x.$$

The separation is one. Define

$$\nu(z)=K_{xy}(z-x)-K_{xy}(z-y).$$

In the right half-plane its sign is that of $Y(X-b(Y))$, where

$$b(Y)^2=\frac{1/4-Y^2+2\sqrt{Y^4+Y^2/4+1/16}}3.$$

It is centrally odd, and its zero set has area zero. These facts follow from the exact numerator calculation in the diagonal finite-part proof.

Let $s(z)$ be signed distance to the graph $\Gamma=\{(b(Y),Y)\}$, positive to its right. Put $V(z)=(s(z),Y)$ and $S(u)=2u_1u_2/|u|$, with $S(0)=0$. Set $\rho=\alpha$ and, for $X>0$, define

$$F_\alpha(z)=-\frac12+\frac12\min(|V(z)|,\rho)^\alpha
+\frac12\operatorname{sgn}(S(V(z)))|S(V(z))|^\alpha,$$

$$h_\alpha(z)=\frac12(2X)^\alpha,\qquad
f_\alpha(z)=\max\{-h_\alpha(z),\min(h_\alpha(z),F_\alpha(z))\}.$$

Extend $f_\alpha$ oddly under $z\mapsto-z$, with value zero on $X=0$. Then

$$f_\alpha(x)=-\frac12,\qquad f_\alpha(y)=\frac12.$$

The local-profile theorem proves

$$\left[\frac12\bigl(|u|^\alpha+\operatorname{sgn}(S(u))|S(u)|^\alpha\bigr)\right]_\alpha
\le1+2\alpha^2\qquad(0<\alpha\le1/4).$$

The assembly theorem therefore gives

$$[f_\alpha]_\alpha\le1+O(\alpha^2).\tag{1}$$

Its proof is uniform over all pairs, including mixed pairs across the freezing radius. The geometric distortion is $O(\alpha\rho^3)$, so it is smaller than the local $O(\alpha^2)$ loss.

For each fixed $z$ off the zero set, $\rho^\alpha=\alpha^\alpha\to1$, and both nonzero powers in the profile tend to one. Thus

$$f_\alpha(z)\longrightarrow\frac12\operatorname{sgn}\nu(z).\tag{2}$$

Also $|f_\alpha(z)|\le(2|z|)^\alpha/2$, which gives uniform sublinear-growth domination for $0<\alpha\le1/4$.

## Local value before clamping

Choose a fixed sufficiently small $0<\delta<1/8$. For $u$ with $|u|=r<\delta$, the graph expansion $b(Y)=1/2+O(Y^4)$ gives

$$V(x+u)=u+O(r^4),\tag{3}$$

uniformly in the angle. This signed-distance comparison follows by restricting nearest points to a radius-$2r$ neighborhood of $x$ and comparing the graph with its vertical tangent. When the signs differ, the point lies between the graph and the tangent and the sum of the distances is bounded by their horizontal separation.

Compare $F_\alpha(x+u)+1/2$ with the planar frozen profile

$$G_{\alpha,\rho}(u)=\frac12\min(r,\rho)^\alpha+
\frac12\operatorname{sgn}(S(u))|S(u)|^\alpha.$$

The radial term of $G$ is constant on each circle and integrates to zero against $K_{xy}$. Its other term gives exactly

$$\int_{|u|<\delta}K_{xy}(u)G_{\alpha,\rho}(u)\,du
=\frac{A_\alpha\delta^\alpha}{\alpha}.\tag{4}$$

Indeed the angular integral is $(4\pi)^{-1}\int_0^{2\pi}|\sin2\theta|^{\alpha+1}\,d\theta=A_\alpha$.

We record uniform error bounds for the comparison. From (3), the two radial arguments are comparable to $r$, and the clipped power has derivative bounded by a constant times $\alpha r^{\alpha-1}$ on the interval between them. Its pointwise error is $O(\alpha r^{\alpha+3})$.

Since $S$ is 2-Lipschitz, (3) also gives

$$S(V(x+u))/r=\sin2\theta+O(r^3).$$

Put $\epsilon=Cr^3$. On $|\sin2\theta|\ge2\epsilon$, the mean value theorem for the signed power, after multiplication by the angular kernel weight $|\sin2\theta|$, bounds the angular error by $O(\alpha\epsilon)$. On the remaining set, the angular measure and the kernel weight are each $O(\epsilon)$, while the powers are uniformly bounded. The integrated angular error there is $O(\epsilon^2)$. After radial integration, the total difference in (4) is consequently

$$O(\alpha\delta^{\alpha+3}+\delta^{\alpha+6}),\tag{5}$$

uniformly for small $\alpha$ and independently of $\rho$.

## The clamp error

The upper clamp is inactive on $B(x,\delta)$. In fact $|V(x+u)|\le2\delta$, $\rho<1$, and hence

$$F_\alpha(x+u)\le\frac12(2\delta)^\alpha
\le\frac12(1-2\delta)^\alpha\le h_\alpha(x+u).$$

The lower clamp needs a separate estimate because the radial term has been frozen. When $|V|\le\rho$, the unclamped profile is at least $-1/2$. When $|V|>\rho$, its possible deficit below $-1/2$ is at most

$$\frac12\bigl(|S(V)|^\alpha-\rho^\alpha\bigr)_+
\le\frac\alpha2\log_+\frac{2r}{\rho}.$$

For the last inequality, $|S(V)|\le|V|\le2r<1$, and the derivative of $t\mapsto e^{\alpha t}$ is at most $\alpha$ for $t\le0$. Also

$$\bigl(1/2-h_\alpha(x+u)\bigr)_+\le C\alpha r.$$

Thus the pointwise change caused by the lower clamp is at most

$$C\alpha r+\frac\alpha2\log_+\frac{2r}{\rho}.$$

Integration against the absolute local kernel bounds its contribution by

$$O\left(\alpha\delta+\alpha\log_+^2\frac{2\delta}{\rho}\right).\tag{6}$$

For $\rho=\alpha$ and fixed $\delta$, this tends to zero as $\alpha\downarrow0$. A bound merely of order $O(\alpha r)$ would miss the effect of freezing; (6) includes it.

Combining (4), (5) and (6), and using $f_\alpha(x)=-1/2$, yields

$$\limsup_{\alpha\downarrow0}
\left|\int_{|u|<\delta}K_{xy}(u)
\bigl(f_\alpha(x+u)-f_\alpha(x)\bigr)\,du
-\frac{A_\alpha\delta^\alpha}{\alpha}\right|=O(\delta^6).\tag{7}$$

Central oddness of $f_\alpha$ and evenness of $K_{xy}$ give the opposite local value at $y$.

## The regular part and the finite part

Subtract the two local kernels of radius $\delta$ from the increment. The remaining density is

$$\mu_\delta(z)=K_{xy}(z-x)\mathbf1_{|z-x|\ge\delta}
-K_{xy}(z-y)\mathbf1_{|z-y|\ge\delta}.$$

It is integrable and decays as $O(|z|^{-3})$ at infinity. Equations (2) and the growth bound justify dominated convergence. Outside the two disks $\mu_\delta=\nu$, while inside them only a smooth other-pole kernel remains. Consequently

$$\lim_{\alpha\downarrow0}\int\mu_\delta(z)f_\alpha(z)\,dz
=\frac12\int_{\mathbb R^2\setminus(B(x,\delta)\cup B(y,\delta))}|\nu(z)|\,dz+O(\delta^2).\tag{8}$$

The independently computed circular finite part is

$$\lim_{\delta\downarrow0}\left[
\frac2\pi\log\delta+
\frac12\int_{\mathbb R^2\setminus(B(x,\delta)\cup B(y,\delta))}|\nu(z)|\,dz\right]=\frac12.\tag{9}$$

Finally, the identity term contributes exactly $-\tfrac12(f_\alpha(x)-f_\alpha(y))=1/2$. For fixed $\delta$,

$$\frac{2A_\alpha\delta^\alpha}{\alpha}
=\frac2{\pi\alpha}+\frac2\pi\log\delta+
\frac{2(\log2-1)}\pi+o(1).$$

Insert (7) and (8), first take the lower limit in $\alpha$, and then let $\delta\downarrow0$ using (9). This proves

$$\liminf_{\alpha\downarrow0}\left(\Phi_\alpha(f_\alpha)-\frac2{\pi\alpha}\right)
\ge1+\frac{2(\log2-1)}\pi=2C_0.$$

The same estimates show $\Phi_\alpha(f_\alpha)=O(1/\alpha)$. Dividing by the seminorm bound (1) changes this value by only $O(\alpha)$, so the lower bound holds for $D_\alpha$. The upper limit proved earlier gives the stated expansion. Compact approximation transfers the lower bound to the original supremum over smooth compactly supported real inputs.
