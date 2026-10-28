# A homogeneous lower bound and the sharp endpoint at alpha = 1

Status: independently proved. The spaces, kernels, and normalized increments are those of `../../01_setup/PROOF.md`. All input functions below are real.

## Statement

For $0<\alpha<1$, put

$$J_\alpha=\int_0^{\pi/6}\sin((\alpha+2)t)\sin^\alpha t\,dt,$$

$$M_\alpha=\frac{(\alpha+1)2^{\alpha-1}}{\cos((\alpha+2)\pi/6)}J_\alpha.$$

Then the sharp homogeneous seminorm constants, equivalently the suprema over real smooth compactly supported functions, satisfy

$$C_\alpha\ge 2^{1-\alpha}(M_\alpha+\tfrac14),\qquad
D_\alpha\ge 2^{1-\alpha}M_\alpha.$$

In conjunction with the upper bound in `../../02_upper_bounds/PROOF.md`, this proves

$$\lim_{\alpha\uparrow1}(1-\alpha)C_\alpha
=\lim_{\alpha\uparrow1}(1-\alpha)D_\alpha
=\frac{3\sqrt3}{4\pi}.$$

In fact both sharp constants equal $3\sqrt3/(4\pi(1-\alpha))+O(1)$ at this endpoint. The finite-alpha inequalities contain all constants explicitly.

## The input and its exact seminorm

Let $Z_3$ be the union of the three lines on which $\cos3\theta=0$, and let

$$u_3(z)=\operatorname{sign}(\cos3\arg z)\operatorname{dist}(z,Z_3),\qquad u_3(0)=0.$$

The signed-distance argument in the angular lemma proves that $u_3$ is globally 1-Lipschitz. Thus

$$f_\alpha(z)=2^{\alpha-1}\operatorname{sign}(u_3(z))|u_3(z)|^\alpha$$

has $[f_\alpha]_\alpha=1$. Equality follows on reflected pairs across a zero line. Write $f_\alpha(r,\theta)=r^\alpha F_\alpha(\theta)$. With $L=\pi/6$, its angular function satisfies

$$F_\alpha(\theta)=2^{\alpha-1}\sin^\alpha(L-\theta),\qquad 0\le\theta\le L.$$

It is even in $\theta$ and changes sign under $\theta\mapsto\theta+\pi/3$. In particular $f_\alpha$ is odd under $z\mapsto-z$. Its values at $e=(1,0)$ and $-e$ are $1/2$ and $-1/2$.

## An angular potential

Set $\beta=\alpha+2\in(2,3)$. Solve

$$g''+\beta^2g=F_\alpha,\qquad g'(0)=0,\quad g(L)=0$$

on $[0,L]$. Since $\cos(\beta L)>0$, this problem has a unique solution. Variation of constants gives

$$g(0)=-\frac{2^{\alpha-1}}{\beta\cos(\beta L)}
\int_0^L\sin(\beta t)\sin^\alpha t\,dt.$$

Extend $g$ evenly across 0 and oddly across $L$, and continue with sign change after every angle $\pi/3$. The extended $g$ is $C^{2,\alpha}$: at $L$ both $g(L)$ and $F_\alpha(L)$ vanish, hence $g''(L)=0$, which supplies the matching second derivative for the odd extension. The even extension at 0 uses $g'(0)=0$; the angular input $F_\alpha$ is continuous there, though it has a corner. No derivative of $F_\alpha$ is needed for the second derivative of $g$ to match. More directly, the reflected equation has a continuous alpha-Hölder right side and matching value and first derivative, and therefore gives a $C^{2,\alpha}$ solution.

Define $U(r,\theta)=-r^\beta g(\theta)$ and $U(0)=0$. The polar Laplacian gives $-\Delta U=f_\alpha$. Since $\beta>2$, the first and second derivatives extend continuously to zero, with zero value there. There is no distribution supported at the origin: integration by parts on an excised disk has boundary errors bounded by constants times $\varepsilon^\beta$ and $\varepsilon^{\beta+1}$ against a fixed smooth test function, and these vanish.

The function $V=\partial_{xx}U$ is globally alpha-Hölder. Indeed it is homogeneous of degree alpha with a $C^\alpha$ angular function. To check the global assertion, for radii $r\ge s$ first compare radially, using $r^\alpha-s^\alpha\le(r-s)^\alpha$, and then angularly at radius $s$. The chord distance between the radius-$s$ points is at most twice the original point distance, so the angular Hölder estimate completes the bound. This argument establishes finiteness, without asserting an unnecessary sharp constant for $V$.

## Agreement with the singular integral

Let $A f=R_1^2f$ be the normalized homogeneous singular integral already constructed. Distributionally,

$$-\Delta(Af)=\partial_{xx}f.$$

Here this identity follows first for smooth compactly supported inputs from the verified Fourier multiplier, and then for $f_\alpha$ by the seminorm-preserving local approximation in the upper-bound proof. Normalized output increments converge locally uniformly, since they converge pointwise and have a common alpha-Hölder bound. Their distributions therefore converge, so the multiplier identity passes to the limit.

The same distribution identity holds for $V=\partial_{xx}U$. Consequently $Af-V$ is harmonic on the whole plane and has growth at most a constant times $1+|x|^\alpha$. Such a harmonic function is constant: the interior gradient estimate on a radius-$R$ ball bounds its gradient at a fixed point by a constant times $R^{\alpha-1}+R^{-1}$, which tends to zero. This elementary harmonic estimate follows by differentiating the Poisson formula at the center of the ball. Thus $Af$ and $V$ give identical increments. This step removes any ambiguity from polynomial additions to a potential.

On the positive first coordinate axis, $U(x,0)=-x^\beta g(0)$. Hence

$$V(e)=-\beta(\beta-1)g(0)=M_\alpha.$$

Both $U$ and $V$ are odd under $z\mapsto-z$, and $V(0)=0$. Thus

$$Af(e)-Af(-e)=2M_\alpha.$$

Adding $f/2$ gives the increment $2M_\alpha+1/2$ for $T_{xx}$. Dividing by $|e-(-e)|^\alpha=2^\alpha$ proves both finite-alpha lower bounds. The approximation lemma transfers them to the smooth compactly supported suprema.

## Endpoint coefficient

At alpha = 1 the integral has the exact value

$$J_1=\int_0^{\pi/6}\sin3t\sin t\,dt
=\frac{\sqrt3}{16}.$$

Also $\cos((\alpha+2)\pi/6)\sim\pi(1-\alpha)/6$. Therefore

$$(1-\alpha)M_\alpha\longrightarrow\frac{3\sqrt3}{4\pi}.$$

For the upper bound, $a_3(1)=3\sqrt3/(8\pi)$ and $a_2(1)>0$. Its splitting parameter tends to $a_3(1)/a_2(1)$, so $(1-\alpha)F(\alpha)\to2a_3(1)=3\sqrt3/(4\pi)$. The added local constant $1/2$ does not affect the limit for $D_\alpha$. Smooth dependence of the displayed integrals near alpha = 1 gives bounded remainders in both explicit bounds, proving the stated $O(1)$ conclusions.

## Dependencies and limitations

This proof uses the normalization audit, exact angular signed-distance input, the established explicit upper bound, and elementary harmonic uniqueness. No numerical output or literature claim is needed. The homogeneous family need not attain the exact finite-alpha operator norm.
