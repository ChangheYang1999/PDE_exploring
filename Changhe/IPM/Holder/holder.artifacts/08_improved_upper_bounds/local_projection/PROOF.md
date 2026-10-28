# A local projection pairing for the diagonal transform

## Statement, spaces and dependencies

Use the real homogeneous Hölder space, seminorm, quotient definition, and kernels in `../../01_setup/PROOF.md`. Let $0<\alpha<1$, and let $C_\alpha,D_\alpha$ be the sharp seminorm constants of $T_{xx}$ and $R_1^2=T_{xx}-I/2$. The same bounds below hold for complex inputs by phase projection.

Retain $a_2(\alpha)$ and $B_\alpha$ from `../../02_upper_bounds/PROOF.md`. Define

$$A_\alpha=\frac2\pi\int_0^{\pi/4}\sin^{\alpha+1}(2t)\,dt
=\frac{\Gamma((\alpha+2)/2)}{2\sqrt\pi\,\Gamma((\alpha+3)/2)}
=2^{-\alpha}a_1(\alpha),$$

$$s^D_\alpha=\frac{(1-\alpha)B_\alpha}{2A_\alpha},\qquad
F_D(\alpha)=\frac{2A_\alpha(s^D_\alpha)^\alpha}{\alpha(1-\alpha)}.
$$

Then

$$\boxed{D_\alpha\le G_{\rm proj}(\alpha):=F_D(\alpha)+\frac12
=F(\alpha)\left(\frac{A_\alpha}{a_2(\alpha)}\right)^{1-\alpha}+\frac12.}$$

Because $\sin 2t<2\sin t$ on $0<t<\pi/4$, this strictly improves the earlier upper bound $F(\alpha)+1/2$ for every $0<\alpha<1$.

Using the independently proved small-exponent finite-part theorem in `../../06_small_alpha_second_term/general_direction/PROOF.md` and the direction maximum in `../../06_small_alpha_second_term/direction_maximum/PROOF.md`, one also obtains

$$\boxed{\limsup_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)
\le 1+\frac{2(\log2-1)}\pi=2C_0,\qquad
C_0=\frac12+\frac{\log2-1}\pi.}$$

Thus the previously proved asymmetric-cusp lower bound and this upper bound give

$$C_0+\frac2\pi\log\cosh\frac\pi4
\le\liminf_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)
\le\limsup_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)
\le2C_0.$$

These inequalities do not assert that the second term of $D_\alpha$ exists.

## A positive-measure decomposition of the local operator

Write the local part of the convolution, for radius $R>0$, as

$$N_Rf(z)=\int_{|w|<R}K_{xx}(w)(f(z-w)-f(z))\,dw.$$

Divide the positive lobes of $\cos2\theta$ into four half-lobes. In each half-lobe, let $t\in(0,\pi/4)$ be the angle from the neighboring zero ray, and let $v_+(t),v_-(t)$ be the positive and negative unit vectors obtained by reflection across that ray. Their angle is $2t$, and both angular densities have magnitude $\sin2t/(2\pi)$. Put

$$\lambda(t)=\cos2t\in(0,1),\qquad q(t)=-\log\lambda(t).$$

The point $\lambda v_-$ is the orthogonal projection of $v_+$ on the ray through $v_-$. Therefore

$$|v_+-\lambda v_-|=\sin2t.$$

Define the paired operator

$$P_Rf(z)=\sum_{j=1}^4\frac1{2\pi}\int_0^{\pi/4}\sin2t
\int_0^R\frac{f(z-rv_{+,j})-f(z-\lambda r v_{-,j})}{r}\,dr\,dt,$$

and the positive convolution operator

$$Q_Rf(z)=\sum_{j=1}^4\frac1{2\pi}\int_0^{\pi/4}\sin2t
\int_{\lambda R}^{R}\frac{f(z-rv_{-,j})}{r}\,dr\,dt.$$

The mass of $Q_R$ is independent of $R$ and equals

$$\kappa=\frac2\pi\int_0^{\pi/4}\sin2t\,(-\log\cos2t)\,dt=\frac1\pi.$$

For each $t$ with $\lambda>0$, a radial change of variables with a lower cutoff $\varepsilon$ gives

$$\int_\varepsilon^R\frac{f(z-\lambda rv_-)-f(z-rv_-)}r\,dr
=\int_{\lambda\varepsilon}^{\varepsilon}\frac{f(z-uv_-)}u\,du
-\int_{\lambda R}^R\frac{f(z-uv_-)}u\,du.$$

As $\varepsilon\downarrow0$, the first term tends to $q(t)f(z)$. Its error is bounded by $[f]_\alpha\varepsilon^\alpha/\alpha$. The angular weight is integrable, and so is $\sin2t\,q(t)$. The measure-zero endpoint $\lambda=0$ is irrelevant. Thus

$$\boxed{N_R=P_R+\kappa I-Q_R.}$$

All paired integrals converge at the origin, and $Q_R$ is a finite positive measure supported in $\overline B_R$. These statements remain valid for general Hölder inputs by local integrability.

## The finite-exponent bound

The projection distance gives

$$|P_Rf(z)|\le\frac{A_\alpha}{\alpha}R^\alpha[f]_\alpha.$$

Let $H_R=T_{xx}-N_R$ be the far part. Since $\kappa=1/\pi<1/2$,

$$R_1^2=P_R+H_R-Q_R-(1/2-\kappa)I.$$

The last two terms are the negative of a positive convolution measure of total mass $1/2$. Consequently their Hölder seminorm is at most $[f]_\alpha/2$. The already proved far-derivative estimate gives, for $h=|x-y|$,

$$|R_1^2f(x)-R_1^2f(y)|
\le[f]_\alpha\left(\frac{2A_\alpha}{\alpha}R^\alpha+B_\alpha hR^{\alpha-1}+\frac12h^\alpha\right).$$

Set $R=sh$. The first two terms have their unique minimum at $s=s^D_\alpha$, exactly as in the earlier radius optimization. This proves $G_{\rm proj}$. Approximation by compact smooth inputs, or the homogeneous increment formula directly, extends the inequality to the stated space.

## Sharper small-exponent upper endpoint

Fix evaluation points $x=e_1/2$, $y=-e_1/2$, a kernel phase $b$, and $0<\rho<1/2$. The finite-part proof decomposes the increment into the two local operators $N_{\rho,b}$ and the regular signed measure $m_{\rho,b}$. That proof bounds the regular part uniformly in $b$, with limiting cost $\frac12\|m_{\rho,b}\|_{\rm TV}$ as $\alpha\downarrow0$.

The projection construction rotates with the kernel. The same positive measure $Q_{\rho,b}$ is translated to the two evaluation points, so

$$|Q_{\rho,b}f(x)-Q_{\rho,b}f(y)|\le\kappa[f]_\alpha|x-y|^\alpha=\kappa[f]_\alpha.$$

Together with the remaining identity coefficient, its total cost is at most $[f]_\alpha/2$. Hence the previous local bound $2a_2(\alpha)\rho^\alpha/\alpha$ for $T_{xx}$ can be replaced, for $R_1^2$, by

$$\frac{2A_\alpha\rho^\alpha}{\alpha}+\frac12.$$

This replacement is uniform in $b$ and uses the same regular part. Both $A_0$ and $a_2(0)$ equal $1/\pi$, while

$$A'_0=\frac{\log2-1}\pi,\qquad a'_2(0)=\frac{\log2-1}{2\pi}.$$

For example, the first identity follows from $\int_0^{\pi/2}\sin u\log\sin u\,du=\log2-1$. Thus the change in the limiting constant is

$$\frac12+2(A'_0-a'_2(0))=\frac12+\frac{\log2-1}\pi=C_0.$$

First take the uniform upper limit in $\alpha$, then let $\rho\downarrow0$ as in the finite-part proof. That theorem gives $C_0$ for the original maximum over phases, so the new upper endpoint is $2C_0$. No exchange of an uncontrolled supremum and limit is required: the remainder uniformity is inherited from the finite-part theorem and the replacement is phase independent.
