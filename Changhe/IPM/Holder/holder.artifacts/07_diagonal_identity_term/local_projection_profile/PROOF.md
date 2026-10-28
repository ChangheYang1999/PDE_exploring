# The two-point inequality

**Status:** proved by elementary analysis. No numerical enclosure or computer-assisted inequality is used.

**Reading order:** statement; elementary estimates; pairs of the same sign; pairs of opposite signs; modified profile. All dependencies are proved below. The question's numerical observations and first-order expansion are not needed.

## Statement

Let $0<\alpha\le 1/4$. For $u=(u_1,u_2)\in\mathbb R^2$, set $r=|u|$, $d(u)=2|u_1u_2|/r$ when $u\ne0$, and $d(0)=0$. Define

$$
g(u)=\frac12\left(r^\alpha+\operatorname{sign}(u_1u_2)d(u)^\alpha\right).
$$

Then

$$
|g(p)-g(q)|\le (1+2\alpha^2)|p-q|^\alpha
\qquad(p,q\in\mathbb R^2).
$$

Consequently, $\widetilde g=g/(1+2\alpha^2)$ satisfies $[\widetilde g]_\alpha\le1$ and

$$
|\widetilde g(u)-g(u)|\le2\alpha^2|u|^\alpha.
$$

## Elementary estimates

The case $p=q$ is immediate; assume $p\ne q$ whenever a two-point quotient is considered below.

For $s,t\ge0$ and $0<\alpha<1$,

$$
|s^\alpha-t^\alpha|\le |s-t|^\alpha,
\qquad
(1+t)^\alpha\le1+\alpha t.
\tag{1}
$$

For the first inequality, when $s=t+h$ with $h>0$, integrate
$\alpha(t+v)^{\alpha-1}\le\alpha v^{\alpha-1}$ over $0<v<h$. The second inequality follows from the decreasing derivative of $x^\alpha$ on $x>0$.

On each closed quadrant, $d$ is $2$-Lipschitz. Indeed, in the interior of a quadrant,

$$
\nabla d(u)=\operatorname{sign}(u_1u_2)
\frac{2(u_2^3,u_1^3)}{|u|^3},
\qquad
|\nabla d(u)|\le2,
\tag{2}
$$

because $u_1^6+u_2^6\le(u_1^2+u_2^2)^3$. Integrate along a segment in the open quadrant and then pass to its closure by continuity.

We shall also use

$$
\sup_{0<t<1}t\log(1/t)=\frac1e,
\qquad
\sup_{0<t<1}t\log^2(1/t)=\frac4{e^2},
\tag{3}
$$

and, for $\beta>0$,

$$
\sup_{0<t<1}t^\beta\log(1/t)=\frac1{e\beta}.
\tag{4}
$$

To verify these formulas, write $t=e^{-z}$, $z>0$, and differentiate $ze^{-z}$, $z^2e^{-z}$, and $ze^{-\beta z}$, respectively. We use only the coarse numerical facts $e>2$ and $2^{1/4}<4/3$.

The following estimate for a power mean will be useful. If $1<k\le4/3$, $0<R\le1$, and

$$
M=\left(\frac{1+R^k}{2}\right)^{1/k},
\qquad m=\frac{1+R}{2},
$$

then

$$
0\le M-m\le\frac{k-1}{8R}(1-R)^2.
\tag{5}
$$

To prove this, put $f(x)=x^k$. On $[R,1]$,
$0\le f''(x)\le k(k-1)R^{k-2}$. Taylor's inequality at $m$, applied to both endpoints and averaged, gives

$$
0\le M^k-m^k
\le\frac{k(k-1)}8 R^{k-2}(1-R)^2.
$$

Since $M\ge m$ and the derivative of $x^k$ is increasing,
$M^k-m^k\ge k m^{k-1}(M-m)$. Dividing and using
$R^{k-2}m^{1-k}\le R^{-1}$ proves (5).

## Pairs with the same sign

First suppose $p,q$ lie in the same open quadrant. Write

$$
D=|p-q|,\qquad m=\min(|p|,|q|),\qquad M=\max(|p|,|q|).
$$

If $D\le m$, the mean value theorem and the reverse triangle inequality give

$$
\big||p|^\alpha-|q|^\alpha\big|
\le\alpha m^{\alpha-1}D
\le\alpha D^\alpha.
$$

The sign in $g$ is constant on the quadrant. Thus (1) and (2) imply

$$
|g(p)-g(q)|
\le\frac{\alpha+2^\alpha}{2}D^\alpha
\le\frac{19}{24}D^\alpha
<D^\alpha.
\tag{6}
$$

Here $\alpha\le1/4$ and $2^\alpha\le4/3$.

Now suppose $D\ge m$, so that $M\le D+m\le2D$. In a negative quadrant,
$0\le g(u)\le |u|^\alpha/2$, and hence

$$
|g(p)-g(q)|\le\frac12M^\alpha
\le2^{\alpha-1}D^\alpha\le D^\alpha.
$$

In a positive quadrant, $|u|^\alpha/2\le g(u)\le|u|^\alpha$, giving

$$
|g(p)-g(q)|\le M^\alpha-\frac12m^\alpha.
$$

Set $t=m/D\in[0,1]$. Since $t\le t^\alpha$, (1) yields

$$
\frac{|g(p)-g(q)|}{D^\alpha}
\le(1+t)^\alpha-\frac12t^\alpha
\le1+\alpha t-\frac12t^\alpha
\le1.
\tag{7}
$$

If $p,q$ lie in opposite quadrants of the same sign, then $p\cdot q\le0$,
so $D\ge\max(|p|,|q|)$. The bounds $0\le g(u)\le|u|^\alpha$ give the same conclusion.

## Pairs with opposite signs

Call the point in a positive quadrant $p$ and the point in a negative quadrant $q$. One direction is immediate:

$$
g(q)-g(p)
\le\frac12\bigl(|q|^\alpha-|p|^\alpha\bigr)
\le\frac12|p-q|^\alpha,
\tag{8}
$$

where (1) and the reverse triangle inequality justify the last step.

For the other direction, the symmetries $u\mapsto-u$ and
$(u_1,u_2)\mapsto(u_2,u_1)$, followed by a common positive dilation, reduce the pair to

$$
p=e^{ia},\qquad q=Ue^{-ib},
\qquad 0<a,b<\frac\pi2,\quad U>0.
$$

Set

$$
s=\sin(2a),\quad t=\sin(2b),\quad
D=|p-q|,\quad R=U^\alpha.
$$

The exact quotient is

$$
Q:=\frac{g(p)-g(q)}{D^\alpha}
=\frac{1-R+s^\alpha+Rt^\alpha}{2D^\alpha}.
\tag{9}
$$

The two geometric estimates used below are

$$
D\ge|1-U|,
\qquad s+t\le2D.
\tag{10}
$$

The first is the reverse triangle inequality. For the second, calculate

$$
D^2=(U-\cos(a+b))^2+\sin^2(a+b)
$$

and

$$
s+t=2\sin(a+b)\cos(a-b)\le2\sin(a+b)\le2D.
$$

If $U\ge1$, then

$$
1-R+s^\alpha+Rt^\alpha
=s^\alpha+t^\alpha+(1-R)(1-t^\alpha)
\le s^\alpha+t^\alpha.
$$

Concavity gives $s^\alpha+t^\alpha\le2((s+t)/2)^\alpha\le2D^\alpha$,
so $Q\le1$.

If $0<U<\alpha$, use $g(p)\le1$, $g(q)\ge0$, and (10):

$$
Q\le(1-U)^{-\alpha}\le(1-\alpha)^{-\alpha}.
$$

Put $z=-\alpha\log(1-\alpha)$. Integration gives
$0\le z\le\alpha^2/(1-\alpha)<1$. For $0\le z<1$,
$e^z\le(1-z)^{-1}$; this follows from
$-\log(1-z)\ge z$. Therefore

$$
(1-\alpha)^{-\alpha}
\le\frac{1-\alpha}{1-\alpha-\alpha^2}
=1+\frac{\alpha^2}{1-\alpha-\alpha^2}
\le1+\frac{16}{11}\alpha^2
\le1+2\alpha^2.
\tag{11}
$$

It remains to consider $\alpha\le U<1$. Set

$$
k=\frac1{1-\alpha},\qquad
M=\left(\frac{1+R^k}{2}\right)^{1/k},
\qquad
\delta=M-\frac{1+R}{2}.
$$

For $X,Y\ge0$ with $X+Y\le2$, one has

$$
\frac{X^\alpha+RY^\alpha}{2}\le M.
\tag{12}
$$

For completeness, on $X+Y=2$ the strictly concave function
$X^\alpha+R(2-X)^\alpha$ is maximized at
$X/(2-X)=R^{-1/(1-\alpha)}$. Substitution gives the maximum
$2^\alpha(1+R^{1/(1-\alpha)})^{1-\alpha}=2M$.
When $X+Y<2$, increasing one coordinate reduces the problem to $X+Y=2$.

Apply (12) with $X=s/D$, $Y=t/D$, using (10). Equations (9) and (10) give

$$
\begin{aligned}
Q
&\le M+\frac{1-R}{2(1-U)^\alpha}\\
&=1+\delta+
\frac12(1-U^\alpha)\bigl((1-U)^{-\alpha}-1\bigr).
\end{aligned}
\tag{13}
$$

We bound the two error terms separately. Since $U\ge\alpha$,

$$
R\ge\alpha^\alpha
=e^{-\alpha\log(1/\alpha)}
\ge1-\frac1e>\frac12.
$$

Moreover, $1-R\le\alpha\log(1/U)$ and $k-1\le4\alpha/3$.
By (5) and (3),

$$
\begin{aligned}
0\le\delta
&\le\frac{\alpha}{3}(1-R)^2\\
&\le\frac{\alpha^3}{3}\log^2(1/\alpha)\\
&\le\frac4{3e^2}\alpha^2
\le\frac13\alpha^2.
\end{aligned}
\tag{14}
$$

For the other error term, $1-e^{-x}\le x$ and $e^x-1\le xe^x$ for $x\ge0$
give

$$
\frac12(1-U^\alpha)\bigl((1-U)^{-\alpha}-1\bigr)
\le\frac{\alpha^2}{2}
\log(1/U)\log(1/(1-U))(1-U)^{-\alpha}.
\tag{15}
$$

If $U\le1/2$, then
$\log(1/(1-U))\le2U$ and $(1-U)^{-\alpha}\le2^\alpha\le4/3$.
The right side of (15) is consequently at most

$$
\frac43\alpha^2U\log(1/U)
\le\frac4{3e}\alpha^2
\le\frac23\alpha^2.
$$

If $U\ge1/2$, put $v=1-U$. Then $\log(1/U)\le2v$, and the right side of (15) is at most

$$
\alpha^2v^{1-\alpha}\log(1/v)
\le\frac{\alpha^2}{e(1-\alpha)}
\le\frac4{3e}\alpha^2
\le\frac23\alpha^2,
$$

by (4). Substituting these estimates and (14) into (13) proves
$Q\le1+\alpha^2$ throughout $\alpha\le U<1$.

Together with (8) and (11), this proves the claimed two-point bound for all nonzero points off the axes. The function $g$ is continuous: at the axes its signed $d^\alpha$ term tends to zero, and at the origin $0\le g(u)\le|u|^\alpha\to0$. Thus all pairs involving axes follow by taking limits with $|p-q|>0$. Pairs involving the origin also satisfy the stronger bound directly from $g(0)=0$ and $g(u)\le|u|^\alpha$. The constants are uniform, so the proof includes all angular and radial degeneracies.

## Modified profile

For $0<\alpha\le1/4$, define

$$
\widetilde g(u)=\frac{g(u)}{1+2\alpha^2}.
$$

The proved seminorm estimate gives $[\widetilde g]_\alpha\le1$. Also,

$$
|\widetilde g(u)-g(u)|
=\frac{2\alpha^2}{1+2\alpha^2}g(u)
\le2\alpha^2|u|^\alpha.
$$

Homogeneity and the stated symmetries are preserved. Since
$\int_0^{2\pi}|\sin(2\theta)|\,d\theta=4$,

$$
\int_0^{2\pi}|\sin(2\theta)|
|\widetilde g(e^{i\theta})-g(e^{i\theta})|\,d\theta
\le8\alpha^2=o(\alpha).
$$

## Verification scope

The proof is analytic and does not depend on sampling, optimization, interval arithmetic, or an external mathematical result. No formalization is claimed.

