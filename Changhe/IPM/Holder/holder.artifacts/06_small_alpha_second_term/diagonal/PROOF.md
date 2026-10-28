# Exact second term for an axis increment of Txy

Status: proved for the fixed-direction increment functional below. This is a lower asymptotic bound for the full operator norm, not a proof that this direction maximizes the full norm.

## Statement

Use the real homogeneous Hölder seminorm and the canonical singular-integral extension in `../../01_setup/PROOF.md`. Let $x=(1/2,0)$, $y=-x$, and

$$E_\alpha=\sup_{[f]_\alpha\le1}|T_{xy}f(x)-T_{xy}f(y)|,
\qquad 0<\alpha<1.$$

Then

$$E_\alpha=\frac2{\pi\alpha}+\frac12+\frac{\log2-1}{\pi}+o(1)
\quad(\alpha\downarrow0).$$

In particular, for the full operator norms,

$$\liminf_{\alpha\downarrow0}\left(C_\alpha-\frac2{\pi\alpha}\right)
\ge\frac12+\frac{\log2-1}{\pi},$$

and the same lower bound holds with $D_\alpha$ in place of $C_\alpha$. The explicit constant is approximately $0.4023257139688609$; its exact expression, not a decimal approximation, is the theorem.

Dependencies: the exact angular constant $a_2(\alpha)$, signed-distance Hölder construction, and compact approximation theorem already proved in the setup and upper-bound folders. All remaining arguments are given here.

## The increment density and its circular finite part

For clarity temporarily write $a=1/2$ and $z=(X,Y)$. The density is

$$\nu(z)=K_{xy}(z-ae_1)-K_{xy}(z+ae_1).$$

It is odd in $Y$ and even in $X$. Its sign in the upper half-plane is positive for $|X|>b(Y)$ and negative for $|X|<b(Y)$, where

$$b(Y)^2=\frac{a^2-Y^2+2\sqrt{Y^4+a^2Y^2+a^4}}3.$$

Indeed, after multiplying by the positive denominator, the numerator has the sign of

$$Y\big((X^2+Y^2)(3X^2-Y^2)-2a^2(X^2+Y^2)-a^4\big).$$

The positive root in $X^2$ is exactly the expression above.

For $Y>0$, the integral of $\nu(X,Y)$ over the full horizontal line is zero. Integration of $K_{xy}$ in $X$, followed by the preceding sign description, gives

$$H(Y):=\int_{\mathbb R}|\nu(X,Y)|dX
=\frac{2Y}{\pi}\left[\frac1{(b(Y)-a)^2+Y^2}
-\frac1{(b(Y)+a)^2+Y^2}\right].$$

To evaluate its logarithmic finite part, introduce $t\in(1,\infty)$ by

$$Y=\frac{2a\sqrt{t(t^2+t+1)}}{t^2-1},
\qquad b(Y)=a\frac{t^2+1}{t^2-1}.$$

These formulas follow by putting $u=(b-a)/Y$, $v=(b+a)/Y$ in the zero equation

$$\frac u{(1+u^2)^2}=\frac v{(1+v^2)^2},$$

then setting $v=t^2u$. They give $u^2=[t(t^2+t+1)]^{-1}$. The parameter $Y$ decreases from infinity to zero as $t$ increases from one to infinity. Direct simplification yields

$$-\pi H(Y)\frac{dY}{dt}
=\frac1t+\frac2{1+t^2}-\frac2{(1+t)^2}.$$

An antiderivative is $\log t+2\arctan t+2/(1+t)$. Since $Y\sim2a/\sqrt t$ at infinity,

$$\lim_{\varepsilon\downarrow0}
\left[\frac2\pi\log\varepsilon+\int_\varepsilon^\infty H(Y)dY\right]
=\frac{2\log(2a)}\pi+\frac12-\frac1\pi.$$

For $a=1/2$, this equals $1/2-1/\pi$.

The horizontal-strip cutoff must now be converted to circular cutoffs around the two poles. Define

$$V=\lim_{\varepsilon\downarrow0}\left[
\frac2\pi\log\varepsilon+\frac12
\int_{\mathbb R^2\setminus(B(x,\varepsilon)\cup B(y,\varepsilon))}|\nu(z)|dz\right].$$

The circular integral contains an additional finite contribution relative to the strip integral. Near either pole the leading kernel is $\pm\sin2\theta/(2\pi r^2)$. Thus the additional contribution, including the factor $1/2$ and the two poles, is

$$\frac1{2\pi}\int_0^{2\pi}|\sin2\theta|\log\frac1{|\sin\theta|}\,d\theta
=\frac1\pi.$$

The equality follows by reducing to the first quadrant and substituting $u=\sin\theta$. The smooth other-pole kernel contributes a vanishing error. Away from the poles, the integral over the removed strip tends to zero by dominated convergence. The angular logarithm is integrable, so the local circular-to-strip limit is justified. Consequently

$$V=\frac12.$$

## Upper asymptotic bound

Fix a sufficiently small $\delta>0$ so the two radius-$\delta$ disks are disjoint. Split the increment into its two local kernels and

$$\nu_\delta(z)=K_{xy}(z-x)\mathbf1_{|z-x|\ge\delta}
-K_{xy}(z-y)\mathbf1_{|z-y|\ge\delta}.$$

The angular lemma bounds the two local contributions by

$$\frac{2a_2(\alpha)\delta^\alpha}{\alpha},
\qquad a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

The far density is odd under $z\mapsto-z$. Antipodal pairing therefore bounds its action on $[f]_\alpha\le1$ by

$$2^{\alpha-1}\int_{\mathbb R^2}|\nu_\delta(z)|\,|z|^\alpha dz.$$

For fixed $\delta$, this integral tends to $\frac12\int|\nu_\delta|$ as $\alpha\downarrow0$. Dominated convergence applies because the truncated density is locally bounded and has $O(|z|^{-3})$ decay, while $|z|^\alpha\le1+|z|^{1/2}$ for $0<\alpha\le1/2$. Also

$$\frac12\int|\nu_\delta|
=\frac12\int_{\mathbb R^2\setminus(B(x,\delta)\cup B(y,\delta))}|\nu|+O(\delta^2),$$

since inside either disk only the smooth other-pole kernel remains. Expanding the local term gives

$$\limsup_{\alpha\downarrow0}\left(E_\alpha-\frac2{\pi\alpha}\right)
\le\frac{\log2-1}\pi+\frac2\pi\log\delta
+\frac12\int_{\mathbb R^2\setminus(B(x,\delta)\cup B(y,\delta))}|\nu|+O(\delta^2).$$

Letting $\delta\downarrow0$ proves the upper bound with constant $(\log2-1)/\pi+V$.

## Matching lower asymptotic bound

Let $Z$ be the closure of the zero set of $\nu$ away from the two poles, including the poles themselves. Give each complementary component the sign of $\nu$, and let $v$ be the resulting signed distance. It is 1-Lipschitz by the segment-crossing argument. Define

$$f_\alpha(z)=2^{\alpha-1}\operatorname{sign}(v(z))|v(z)|^\alpha.$$

Then $[f_\alpha]_\alpha\le1$, both center values are zero, and the increment is the nonnegative integral $\int\nu f_\alpha$. Away from the poles, $f_\alpha\to\operatorname{sign}(\nu)/2$ almost everywhere. The same sublinear-growth domination as above proves convergence of the integral outside the two fixed disks to $\frac12\int_{\rm outside}|\nu|$.

We verify that the local singular contribution has the same constant term as the angular extremizer. At $Y=0$ the explicit root satisfies

$$b(Y)=a+O(Y^4).$$

Near each pole the zero set therefore consists of the horizontal axis and a curve whose displacement from the vertical line through the pole is $O(r^4)$ in a radius-$r$ disk. All other zero components stay a fixed distance away. Comparing nearest points on these curves with nearest points on the two perpendicular lines gives

$$v(z)=v_0(z)+O(r^4),$$

where $v_0$ is the signed distance to the two perpendicular lines, with the sign of the own kernel. For equal signs the estimate follows by comparing nearest-point distances; for opposite signs the point lies between the vertical curve and the vertical line, and the sum of its distances is at most their horizontal separation. The closest-point comparison can be restricted to a radius-$2r$ neighborhood, since the pole itself is a zero.

Write $v_0=r\psi(\theta)$, where $|\psi|$ is distance on the unit circle to the nearest coordinate axis, and put $\epsilon=Cr^3$. Thus $v/r=\psi+O(\epsilon)$. The own angular kernel satisfies $|\sin2\theta|\le2|\psi|$. On $|\psi|\ge2\epsilon$, the mean value theorem for the signed power gives a weighted angular error at most a constant times $\alpha\epsilon$. On $|\psi|<2\epsilon$, the set has angular measure $O(\epsilon)$, the kernel factor is $O(\epsilon)$, and the signed powers are bounded uniformly for $0<\alpha\le1/2$. This contribution is $O(\epsilon^2)$. Consequently the weighted angular error is

$$O(\alpha r^3+r^6),$$

uniformly for small $r$ and $0<\alpha\le1/2$. Multiplication by $r^{\alpha-1}$ and radial integration gives local error $O(\alpha\delta^{\alpha+3}+\delta^{\alpha+6})$. The smooth other-pole kernel contributes $O(\delta^{\alpha+2})$. Hence

$$\limsup_{\alpha\downarrow0}
\left|\int_{B(x,\delta)\cup B(y,\delta)}\nu f_\alpha
-\frac{2a_2(\alpha)\delta^\alpha}{\alpha}\right|
=O(\delta^2).$$

Combining this with the outside limit and then sending $\delta\downarrow0$ proves the matching lower bound. The local identity term in $R_1^2$ vanishes for the rotated witness because both center values are zero. This proves the stated lower consequences for $C_\alpha$ and $D_\alpha$.

## Scope

The proof determines the second term for one fixed-direction functional. To identify the second term for the full norm, one must control the circular finite part uniformly over the relative direction of the kernel and increment and prove its maximum. That maximization is not established here. No numerical direction scan can substitute for it.
