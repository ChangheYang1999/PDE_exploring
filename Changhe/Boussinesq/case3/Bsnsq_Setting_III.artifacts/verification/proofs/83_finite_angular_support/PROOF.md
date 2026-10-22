# No exact profile with finite angular support

Status: CONFIRMED by the independent verifier; actual Opus5.5 audit86 of the radial ODE checked. Lead review pending. This is a restricted theorem. It does not exclude smooth profiles with infinitely many angular modes and does not decide the B2 endpoint. Actual creation time is recorded in verification/README.md.

## Statement

Let $\beta\ge2$ and $0<\nu\le1/2$. Suppose real smooth functions $\Psi,\Omega,\Theta$ on $\mathbb R^2$ satisfy

$$
\Omega=-\Delta\Psi,\qquad V=(-\Psi_y,\Psi_x),\qquad V(0)=0,\qquad W=\beta X+V,
$$

$$
W\cdot\nabla\Omega+\Omega=\Theta_x,
\qquad W\cdot\nabla\Theta=(\beta-2)\Theta.
$$

Assume $\Psi,\Omega$ are odd under $x\mapsto-x$, $\Theta$ is even, $\Psi_{xy}(0)\ne0$, and $\Theta=a_0x^2+O(|X|^3)$ with $a_0\ne0$. Suppose, uniformly at infinity,

$$
|D^j\Omega(X)|=O(r^{-\nu-j})\quad(0\le j\le2),\qquad
|\Psi(X)|=O(r^{2-\nu}),\quad |\nabla\Psi(X)|=O(r^{1-\nu}),\quad
|\Theta(X)|=O(r^{1-2\nu}). \tag{1}
$$

Then $\Psi$ and $\Theta$ cannot both have finite angular Fourier support with fixed maximal degrees independent of $r$.

For a B2 profile one first replaces its stream function by $\Psi-U_2(0)x$, which produces the actual relative field $V=U-U(0)$ and does not change $\Omega$, the strain, or finite angular support. The full-plane canonical inverse and the derivative conclusions already proved in packets36 and40 supply (1), with $\nu=1/\beta$, for class A. Thus the theorem excludes simultaneous exact finite angular support within the target. No additional velocity field is introduced.

## 1. Highest modes

Use ordinary polar coordinates $X=(r\cos\theta,r\sin\theta)$ and Fourier coefficients multiplying $e^{in\theta}$. Let $N$ and $M$ be the maximal positive degrees of $\Psi$ and $\Theta$. The nonzero mixed second derivative of $\Psi$ forces $N\ge2$, and the temperature jet forces $M\ge2$. The coefficient $\psi_N(r)$ is nonzero as a function. If its vorticity coefficient vanished identically, the radial harmonic equation and smoothness at the origin would give $\psi_N=Ar^N$. Condition (1) and $N\ge2$ would force $A=0$. Thus the maximal vorticity degree is also $N$.

The angular coefficient of degree $M+1$ in $\Theta_x$ is

$$
\frac12\left(\theta_M'-\frac Mr\theta_M\right). \tag{2}
$$

The left side of the vorticity equation has degree at most $2N$. If $M+1>2N$, (2) vanishes. Its solution $\theta_M=Cr^M$ contradicts (1) unless $C=0$, contrary to the definition of $M$. Hence $M+1\le2N$.

Reflection in $x$ sends $\theta$ to $\pi-\theta$. For an odd real stream function its coefficient of degree $N$ is real when $N$ is odd and purely imaginary when $N$ is even. Write

$$
\psi_N=\varepsilon f,\qquad \omega_N=\varepsilon g,
\qquad \varepsilon\in\{1,i\},\quad f,g\in\mathbb R,
\qquad g=-f''-r^{-1}f'+N^2r^{-2}f. \tag{3}
$$

The identity $V\cdot\nabla Q=r^{-1}(\Psi_rQ_\theta-\Psi_\theta Q_r)$ fixes all following signs.

## 2. The case $M+1<2N$

The degree $2N$ coefficient of the vorticity equation gives $f'g-fg'=0$. On a component where $f\ne0$, this means $g=Cf$, with real constant $C$. The resulting regular linear ODE

$$
f''+r^{-1}f'-N^2r^{-2}f+Cf=0 \tag{4}
$$

extends throughout $r>0$. To see that the constant cannot change at a finite zero, uniqueness for (4) implies that a nontrivial solution has nonzero derivative at that zero. Smoothness of $g'$ then determines the same value $C=g'/f'$ on the next component. Equivalently, the unique global solution of (4) extends the first nonzero component and fixes every successive simple zero. There can be no finite accumulation of zeros for that solution. Thus $C$ is one constant on $(0,\infty)$.

If $C=0$, smoothness at the origin gives $f=Ar^N$ and (1) forces zero. If $C<0$, multiply (4) by $rf$ and integrate between small and large radii. The boundary term $rff'$ tends to zero at both ends: at the origin $f=O(r^N)$, while at infinity $f=g/C=O(r^{-\nu})$ and $f'=O(r^{-\nu-1})$. We obtain

$$
\int_0^\infty\left(rf'^2+N^2r^{-1}f^2+|C|rf^2\right)dr=0,
$$

where the equality follows by monotone limits of the nonnegative truncated integrals. Hence $f=0$.

If $C>0$, set $E=f'^2+Cf^2$. Equation (4) yields

$$
E'=-\frac2r f'^2+\frac{2N^2}{r^2}ff'
\ge-\left(\frac2r+\frac{N^2}{\sqrt C\,r^2}\right)E.
$$

Therefore any nonzero solution has $E(r)\ge c r^{-2}$ for large $r$. On the other hand, the derivative bounds in (1), applied to $g=Cf$, give $f'=O(r^{-\nu-1})$ and $f''=O(r^{-\nu-2})$. Substituting into (4), initially using $f=O(r^{-\nu})$, improves this to $f=O(r^{-\nu-2})$. Consequently $E=O(r^{-2\nu-2})=o(r^{-2})$, a contradiction. This excludes $M+1<2N$.

## 3. The remaining highest-mode equations

It remains to consider $M=2N-1$. This $M$ is odd, so the even-in-$x$ temperature coefficient is purely imaginary. Write

$$
\theta_M=i\varepsilon^2h,\qquad h\in\mathbb R.
$$

The coefficients of degrees $N+M$ in the temperature equation and $2N$ in the vorticity equation are respectively

$$
Nfh'-Mf'h=0,\qquad 2N(f'g-fg')=rh'-Mh. \tag{5}
$$

There is an open interval on which both $f$ and $h$ are nonzero. Indeed, on a component of $\{h\ne0\}$ the first equation is the regular linear equation $f'=(N/M)(h'/h)f$. Either $f$ never vanishes there or it is identically zero there. In the latter case the second equation gives $h=Cr^M$ on that component. Such a nonzero function has no finite positive endpoint where $h$ vanishes, so the component must be $(0,\infty)$. Then $f$ vanishes identically, contradicting its degree. Thus every nonzero component of $h$ also has $f\ne0$.

Fix such a component. With $\sigma=\operatorname{sign}f$, put

$$
a=\frac{|f|}{r^N}>0,\qquad
b=-a''-\frac{2N+1}{r}a',\qquad
q=\frac MN=2-\frac1N,\qquad p=q-1=1-\frac1N.
$$

Thus $f=\sigma r^Na$ and $g=\sigma r^Nb$. The first equation in (5) gives $h=Cr^Ma^q$, where $C\ne0$. Since $M+1=2N$, the second becomes

$$
2N(a'b-ab')=Cq a^{q-1}a'.
$$

Divide by $a^2$ and integrate. As $q-2=-1/N$, this yields

$$
b=Ka+\frac{Cq}{2}a^{q-1}.
$$

Therefore $a$ solves the scalar equation

$$
a''+\frac dr a'+Ka+Da^p=0,\qquad
 d=2N+1>0,\quad 0<p=1-\frac1N<1,\quad D=\frac{Cq}{2}\ne0. \tag{6}
$$

The constants $C,K,D$ are initially fixed only on this component. If it extends to infinity, (1) gives $a,a'\to0$, because $N\ge2$ and $\nu>0$.

## 4. No positive tail of (6)

Suppose $a>0$ on an entire tail and $a,a'\to0$. Choose the tail so far out that $Ka+Da^p$ has the sign of $D$ and magnitude at least $|D|a^p/2$.

If $D>0$, every critical point of $a$ on this tail is a strict maximum. Since $a\to0$, its derivative is negative somewhere, and it cannot subsequently change from negative to positive. Hence $a'<0$ eventually. Equation (6) gives

$$
-(r^da')'\ge c r^da^p.
$$

Integrating from $r/2$ to $r$ gives $-r^d a'(r)+(r/2)^d a'(r/2)\ge c_0 r^{d+1}a(r)^p$. The second term on the left is negative, so $-a'(r)\ge c_1r a(r)^p$ for large $r$. Thus $(a^{1-p})'\le-c_1(1-p)r$, which is incompatible with positivity for all large radii.

If $D<0$, every critical point on this tail is a strict minimum. A point with $a'\ge0$ would force $a$ subsequently to increase, since no local maximum is possible; that contradicts $a\to0$. Thus $a'<0$ throughout a sufficiently remote tail. Equation (6) now gives $a''\ge c a^p$. Multiply by $a'<0$ and integrate to infinity, using $a,a'\to0$:

$$
-a'(r)\ge\sqrt{\frac{2c}{p+1}}\,a(r)^{(p+1)/2}.
$$

Since $(p+1)/2<1$, this again forces a zero at finite radius. Therefore (6) has no such positive tail.

## 5. Finite radial zeros

Let $R>0$ be a finite upper endpoint of the chosen component. Smoothness and $h=Cr^Ma^q$ imply $f(R)=h(R)=0$. If $f$ had a simple zero there, $h$ would have a nonzero one-sided leading power $(R-r)^q$ with $1<q<2$, contrary to its smoothness. Thus the positive function $a=\sigma f/r^N$ extends smoothly to $R$ with $a(R)=a'(R)=0$.

Introduce the energy

$$
\mathcal E=\tfrac12a'^2+\tfrac12Ka^2+\frac{D}{p+1}a^{p+1},
\qquad \mathcal E'=-\frac dr a'^2. \tag{7}
$$

If $D>0$, its potential is nonnegative for sufficiently small $a$. On a short interval ending at $R$, $\mathcal E'\ge-B\mathcal E$ for a finite constant $B$. Gronwall gives $\mathcal E(R)>0$ whenever $a$ was nonzero earlier, contradicting $a(R)=a'(R)=0$. Hence $D<0$.

For $D<0$, all critical points sufficiently near $R$ are strict minima. Positivity to the left and convergence to zero force $a'<0$ there. Equation (6) gives $a''\ge c a^p$. As in Section4, integrate after multiplying by $a'<0$, now to the finite endpoint $R$:

$$
-a'(r)\ge c_1 a(r)^{(p+1)/2}.
$$

Put $\kappa=(1-p)/2=1/(2N)$. Integrating $-(a^\kappa)'\ge\kappa c_1$ from $r$ to $R$ gives

$$
a(r)\ge c_2(R-r)^{2N}. \tag{8}
$$

Thus the smooth signed extension $\widetilde a_0=\sigma f/r^N$, agreeing with $a$ on the left, cannot vanish to infinite order at $R$. Let $k\ge2$ be its first nonzero Taylor order. In (6), the leading orders of $a''$ and $Da^p$ are $k-2$ and $kp$; the other two terms have higher orders. Their nonzero coefficients must cancel, so $k-2=kp$, hence $k=2N$. This is an even-order zero, with positive leading coefficient.

Consequently $a$ extends as a positive smooth function on both sides of $R$, except at $R$, and has a factorization

$$
a(r)=(r-R)^{2N}\widetilde a(r),\qquad \widetilde a(R)>0.
$$

Both $a^p=(r-R)^{2N-2}\widetilde a^p$ and $a^q=(r-R)^{4N-2}\widetilde a^q$ are smooth near $R$. The coefficient $h=Cr^Ma^q$ has nonzero Taylor order $4N-2$, so $h$ is nonzero on the right as well. Applying (5) there gives constants $C_+,K_+$. Equality of the $(4N-2)$-nd Taylor coefficient of $h$ forces $C_+=C$, hence $D_+=D$. With $D$ fixed, the smooth function

$$
-a''-\frac dr a'-Da^p
$$

equals $Ka$ on the left and $K_+a$ on the right. Equality of its $2N$-th derivative at $R$, since $a^{(2N)}(R)\ne0$, forces $K_+=K$.

The energy (7) therefore extends with exactly the same constants. It starts from $\mathcal E(R)=0$ and is strictly negative just to the right, because $a'>0$ there and $d/r>0$. It cannot reach another finite endpoint of a nonzero component: the preceding zero analysis would again give $a=a'=0$, hence $\mathcal E=0$, contradicting monotonicity. The fields are smooth at every finite radius, so there is no other way to terminate that component. It thus extends to infinity, where (1) gives $a,a'\to0$ and consequently $\mathcal E\to0$, again contradicting its strictly negative nonincreasing value. This excludes a finite upper endpoint.

The chosen component has neither a finite upper endpoint, by Section5, nor an infinite one, by Section4. This contradiction completes the proof.

## Scope and dependencies

The proof uses exact highest-mode equations, two vorticity derivative bounds, smoothness at finite radial zeros, and the given tails. Its class-A application uses the already proved derivative-tail results. It does not assume analyticity, positivity of the full vorticity or temperature, a horizontal wall, or a fixed physical center. Positivity of the auxiliary radial function $a$ is only its definition on one nonzero mode interval.

The radial zero order $2N$ explains why finite regularity can change the conclusion: a function that stops at such a zero is generally only $C^{2N-1}$. This observation alone does not construct a finite-regularity Boussinesq profile. A finite-mode numerical approximation with a nonzero residual remains allowed, and no lower bound on its residual follows from this theorem.

Verification files are supplementary algebra checks. The argument above is the proof; no numerical run or model response is treated as a proof.
