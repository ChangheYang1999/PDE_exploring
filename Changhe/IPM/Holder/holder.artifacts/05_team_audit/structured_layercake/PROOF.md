# Exact one-dimensional reduction of the polygonal witness

Status: proved. Interval evaluation of the resulting positive integral is reproducible with the independent code listed below.

## Statement and input function

Fix $a>0$ and $0<\alpha<1$. Work with the real homogeneous Hölder seminorm and the normalized operators in `../../01_setup/PROOF.md`. Let $Z$ consist of the horizontal axis, the vertical segments from $(0,0)$ to $(0,a)$ and from $(1,0)$ to $(1,a)$, the rays from these upper endpoints in directions $120$ and $60$ degrees, and their images under $(x,y)\mapsto(1-x,-y)$. In the upper half-plane give the two outer components of $\mathbb R^2\setminus Z$ sign $+1$ and the component between the broken lines sign $-1$. Reverse the sign under the indicated point reflection. Set

$$f_{\alpha,a}(z)=2^{\alpha-1}\sigma(z)\operatorname{dist}(z,Z)^\alpha.$$

The signed-distance argument in `../structured_witness/PROOF.md` proves $[f_{\alpha,a}]_\alpha\le1$ and $f_{\alpha,a}(0)=f_{\alpha,a}(e_1)=0$. Define

$$K(x,y)=\frac{xy}{\pi(x^2+y^2)^2},\qquad
\nu(x,y)=K(x-1,y)-K(x,y).$$

Then the absolutely convergent output increment

$$I(\alpha,a)=\int_{\mathbb R^2}\nu(z)f_{\alpha,a}(z)\,dz$$

satisfies $C_\alpha,D_\alpha\ge I(\alpha,a)$. The lower bound for $D_\alpha$ uses rotation and the vanishing of both pole values. The approximation lemma in the setup also gives the same lower bound for the supremum over real compactly supported smooth inputs.

We prove the exact formula

$$\boxed{I(\alpha,a)=2^{\alpha-1}\alpha\int_0^\infty t^{\alpha-1}J_a(t)\,dt,\qquad J_a(t)>0.}$$

Every function defining $J_a$ below is elementary. Consequently integrating over any finite positive interval gives a rigorous lower bound. The omitted portions are nonnegative, without an asymptotic approximation or a numerical tail assumption.

## Eroded components and horizontal slices

Write $d(z)=\operatorname{dist}(z,Z)$. In the upper right positive component, the three defining inequalities are

$$y>0,\quad x>1,\quad y<a+\sqrt3(x-1).$$

This is a convex intersection of half-planes. The distance to its boundary equals the minimum of the distances to the three complementary half-planes. Thus its level set $d>t$ is

$$y>t,\qquad x>L_t(y),\qquad
L_t(y)=\max\left(1+t,1+\frac{y-a+2t}{\sqrt3}\right).$$

The other positive component is its reflection in $x=1/2$.

In the central negative component, the rightward inward offset of the left broken line is $x=\ell_t(y)$, where

$$\ell_t(y)=\begin{cases}
t,&y\le a,\\
\sqrt{t^2-(y-a)^2},&a<y<a+t/2,\\
(2t-y+a)/\sqrt3,&y\ge a+t/2.
\end{cases}$$

The circular part is the arc of radius $t$ about $(0,a)$ between the inward normals of the vertical segment and its outgoing ray. Its upper endpoint is at angle $\pi/6$, so its height is $a+t/2$. The ray offset is obtained by shifting its supporting line by normal distance $t$. These formulas can also be checked by orthogonal projection onto the segment, its endpoint, and the ray, respectively. The other central boundary is its reflection $x=1-\ell_t(y)$. Therefore the negative level set is

$$y>t,\quad \ell_t(y)<\frac12,\quad
\ell_t(y)<x<1-\ell_t(y).$$

Other pieces of $Z$ cannot give a smaller distance before an adjacent boundary does: any segment from a point in one component to a nonadjacent piece crosses that component's boundary first. Thus these are the exact level sets, including the circular corners, not polygonal approximations to them.

An $x$-primitive of $\nu$ is

$$F(x,y)=\frac{y}{2\pi}\left(\frac1{x^2+y^2}-\frac1{(x-1)^2+y^2}\right).$$

It obeys $F(1-x,y)=-F(x,y)$ and tends to zero at $x=\pm\infty$. Hence, at each height, the two positive components contribute $-2F(L_t(y),y)$, while the negative central component after sign reversal contributes $2F(\ell_t(y),y)$ when it exists. Reflection in the horizontal axis doubles the result. We obtain

$$J_a(t)=4\left[-\int_t^\infty F(L_t(y),y)\,dy
+\int_{\{y>t:\ell_t(y)<1/2\}}F(\ell_t(y),y)\,dy\right].$$

Both summands are positive. Indeed $F(x,y)<0$ for $x>1/2$ and $F(x,y)>0$ for $x<1/2$, when $y>0$. The positive component has nonzero area for every $t>0$, so $J_a(t)>0$.

Finally, $d^\alpha=\alpha\int_0^d t^{\alpha-1}\,dt$. Fubini is justified absolutely: near either pole, $|f|=O(r^\alpha)$ and $|\nu|=O(r^{-2})$, while at infinity $|\nu|=O(r^{-3})$ and $|f|=O(r^\alpha)$. This proves the displayed formula for $I$.

## Explicit primitives

For $y>0$, let $\mathcal L_{m,b}(y)$ be a primitive of $F(my+b,y)$. On all intervals used below it is given by

$$\mathcal L_{m,b}(y)=\frac{1}{2\pi(1+m^2)}\left[
\frac12\log\frac{(my+b)^2+y^2}{(my+b-1)^2+y^2}
+m\operatorname{Arg}\bigl(y^2+(my+b)(my+b-1)+iy\bigr)\right],$$

where the argument lies in $(0,\pi)$. This expression follows by integrating $y/((my+b)^2+y^2)$ and subtracting the same expression with $b$ replaced by $b-1$. Direct differentiation verifies it. The difference of arguments is unambiguous because the relevant original arguments have positive imaginary parts. Also $\mathcal L_{m,b}(y)\to0$ as $y\to\infty$.

For the circular boundary $x=t\cos\theta$, $y=a+t\sin\theta$, $0\le\theta\le\pi/6$, put $\zeta=e^{i\theta}$ and

$$Q_q(\theta)=\frac12\log|q+ia+t\zeta|
-\frac12\operatorname{Re}\left[
\frac{t\zeta}{q-ia}-\frac{t^2}{(q-ia)^2}\log((q-ia)\zeta+t)\right],$$

$$\mathcal A_{t,a}(\theta)=\frac{Q_0(\theta)-Q_{-1}(\theta)}{2\pi}.$$

Both complex logarithms use their principal branch. Their arguments have strictly negative imaginary part for $q=0,-1$, $a>0$, and this angle range, so the branch is continuous. Writing $z=q+ia+t e^{i\theta}$ gives

$$\frac{yy'}{|z|^2}=\frac12\frac d{d\theta}\log|z|
-\frac12\operatorname{Re}\frac{z'}{\overline z}.$$

Substitution $\zeta=e^{i\theta}$ integrates the second term to the expression above. Therefore $\mathcal A_{t,a}'(\theta)=F(t\cos\theta,a+t\sin\theta)t\cos\theta$.

## A finite formula for the level integral

Set $s=a+(\sqrt3-2)t$ and $s_+=\max(t,s)$. The positive part in the formula for $J_a/4$ is

$$P_a(t)=\mathcal L_{0,1+t}(t)-\mathcal L_{0,1+t}(s_+)
+\mathcal L_{1/\sqrt3,\,1+(2t-a)/\sqrt3}(s_+).$$

The central negative part is a sum of three terms. The vertical term is

$$N_v=\begin{cases}
\mathcal L_{0,t}(a)-\mathcal L_{0,t}(t),&t<\min(a,1/2),\\0,&\text{otherwise}.
\end{cases}$$

For the circle, define

$$\theta_0=\min\left(\frac\pi6,
\max\left\{\arcsin\max(0,1-a/t),\ \arctan\sqrt{\max(4t^2-1,0)}\right\}\right).$$

If $t<\min(2a,1/\sqrt3)$, let $N_c=\mathcal A_{t,a}(\pi/6)-\mathcal A_{t,a}(\theta_0)$; otherwise let $N_c=0$. The two lower-angle conditions express respectively $y\ge t$ and $x\le1/2$. For the ray, put

$$y_r=\max(t,a+t/2,a+2t-\sqrt3/2),\qquad
N_r=-\mathcal L_{-1/\sqrt3,\,(2t+a)/\sqrt3}(y_r).$$

Then $J_a(t)=4(P_a(t)+N_v+N_c+N_r)$. The formulas agree at their branch endpoints.

## Independent numerical verification and certification rule

`../../code/structured_layercake.py` implements the exact formula with mpmath. It checks the circular primitive by differentiation and evaluates the integral independently of the numerical team's polar quadrature. At $\alpha=a=1/2$ its exploratory value is $2.089173024\ldots$. This value alone is not a certificate.

`../../code/certify_structured_layercake.py` evaluates $J_a$ over interval cells with 160-bit Arb arithmetic. A cell is $[e^s,e^{s+h}]$ with exact rational $s,h$. If $J_a$ has interval enclosure $\mathcal J$, its contribution to $I$ lies in

$$2^{\alpha-1}\mathcal J\,e^{\alpha s}(e^{\alpha h}-1).$$

All weights are positive and evaluated by interval arithmetic. The code sums these enclosures and rounds its lower endpoint downward to a decimal with ten digits after the point. Positivity of $J_a$ proves that the omitted tails only increase $I$. The reported finite-integral upper endpoint is not an upper bound for the full integral. The code uses a stable difference formula for the line primitive and switches to separate logarithms when the ratio is far from one; both formulas are algebraically identical.
