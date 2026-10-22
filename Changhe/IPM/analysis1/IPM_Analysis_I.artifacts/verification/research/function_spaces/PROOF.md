# Function-space tests and explicit nonlocal bounds

Status: proved auxiliary statements and counterexamples, 2026-10-20. None is a nonexistence theorem for the full-plane IPM profile. Dependencies are the canonical kernel and central-strain identity proved in `../canonical_inverse/PROOF.md`, elementary scaling, and the compactly supported potential identity in `../local_geometry/PROOF.md`.

## An explicit norm that controls central strain

Let $0<\gamma<1$, $L>0$, and suppose $h$ has the density symmetries and canonical central strain $s[h]=\psi[h]_{xy}(0)$. Assume

$$|h(x,y)|\le \epsilon x^2|y|\left(1+\frac{x^2+y^2}{L^2}\right)^{(\gamma-3)/2}.$$

Then

$$|s[h]|\le \frac{\epsilon L^2}{1-\gamma}\left(\frac1{12}+\frac{3\sqrt3}{8\pi}\right),\qquad |c[h]|\le\frac{\epsilon L^2}{1-\gamma}\left(\frac1{36}+\frac{\sqrt3}{8\pi}\right).$$

Insert this bound into the absolute central-strain density integral. Its radial integral is

$$\int_0^\infty r(1+r^2/L^2)^{(\gamma-3)/2}dr=\frac{L^2}{1-\gamma}.$$

The quadrant angular integral is $J=\int_0^{\pi/2}\cos^2\theta\sin\theta|\sin3\theta|d\theta$. Before taking the absolute value the integrand is $(1+\cos2\theta-\cos4\theta-\cos6\theta)/8$. It changes sign at $\pi/3$, so elementary integration gives $J=\pi/48+3\sqrt3/32$. Multiplication by $4/\pi$ gives the first constant, and division by three gives the scaling-functional constant.

This inequality supplies a bounded scaling functional in a strong weighted factor norm. It is not an inverse estimate. If the factor at zero is to remain normalized, impose its zero correction separately. No claim is made that this is the best norm for transport solvability.

## Explicit influence of an exterior perturbation

Suppose $h$ has the density parity, vanishes on $|Y|<R$, and $|h(Y)|\le H|Y|^\gamma$ for $|Y|\ge R$, where $\gamma<1$. Its canonical velocity in $|X|\le a<R$ is

$$U[h](X)=\int_{|Y|\ge R}\bigl(K(X-Y)-K(-Y)\bigr)h(Y)dY.$$

The subtracted kernel has zero integral against $h$ on every centered annulus by parity. Its subtraction makes the expression absolutely convergent, and coincides with the canonical symmetric truncation. There is no local density term inside the disk.

Identify the kernel vector with the complex number $K_1+iK_2=i/(2\pi\overline z^2)$. For $j\ge0$, differentiating in arbitrary unit directions gives

$$\|D^jK(z)\|\le \frac{(j+1)!}{2\pi}|z|^{-j-2}.$$

The equality of this bound with the complex derivative modulus follows because real directional derivatives multiply by unit complex factors and conjugation preserves their norm. The mean value theorem bounds the subtracted kernel by $|X|/[\pi(|Y|-a)^3]$. Differentiation under the exterior integral is justified by these integrable bounds. For every integer $j\ge1$ with $j>\gamma$,

$$\sup_{|X|\le a}\|D^jU[h](X)\|\le\frac{(j+1)!H}{(1-a/R)^{j+2}(j-\gamma)}R^{\gamma-j}.$$

Indeed, use $|X-Y|\ge |Y|-a\ge(1-a/R)|Y|$ and integrate $r^{\gamma-j-1}$ from $R$ to infinity. Since $U[h](0)=0$ by parity, the velocity itself is at most $a$ times the displayed bound for $j=1$. In particular, an unknown sublinear tail can affect the strain in the core at order $R^{\gamma-1}$; it does not disappear exactly at a numerical cutoff.

The central-strain kernel improves its particular component to

$$|s[h]|\le \frac{4H}{\pi(1-\gamma)}R^{\gamma-1}.$$

Here the full angular integral of $|\sin3\theta|$ is four. These explicit tail bounds require an actual bound $H$ on the exterior perturbation. A numerical two-term continuation supplies no such bound by itself.

## Center normalization is not continuous in an ordinary C2,alpha norm

Fix $0<\alpha<1$ and a smooth radial cutoff $\chi$ supported in the unit disk and equal to one in the disk of radius $1/2$. Let

$$h_\delta(x,y)=x^2y\,\chi((x,y)/\delta),\qquad 0<\delta<1.$$

Each $h_\delta$ has the required parity and a smooth strong center factor with value one at zero. Write $h_\delta(X)=\delta^3 H(X/\delta)$ for fixed smooth compactly supported $H(X)=x^2y\chi(X)$. For $j\le2$, $\|D^jh_\delta\|_\infty=\delta^{3-j}\|D^jH\|_\infty$, and $[D^2h_\delta]_{C^\alpha}=\delta^{1-\alpha}[D^2H]_{C^\alpha}$. Thus $h_\delta\to0$ in global $C^{2,\alpha}$, while the center coefficient stays one. The same sequence tends to zero in any additional fixed far-growth norm, because it is supported near zero.

Therefore center normalization cannot be imposed as a bounded scalar functional on ordinary $C^{2,\alpha}$ alone. The set of functions with center factor value one is not closed in that ambient topology. A Banach formulation must carry stronger factor information or otherwise prove closure using its actual equations. This counterexample does not involve exact IPM solutions.

## A fractional axis coefficient is not controlled by P2 proximity alone

Fix a noninteger $p>6$ and the same cutoff. Define

$$h_\delta(x,y)=|x|^p y^3\chi((x,y)/\delta).$$

This has the density parity, is $C^{2,\alpha}$, and factors as $x^2y$ times the continuous function $|x|^{p-2}y^2\chi(X/\delta)$, whose value at zero is zero. Its axis coefficient $\partial_y^3h_\delta(x,0)/6$ equals $|x|^p$ for sufficiently small $|x|$; its local fractional coefficient is exactly one for every $\delta$.

But $h_\delta(X)=\delta^{p+3}H_p(X/\delta)$ with fixed compactly supported $H_p=|x|^py^3\chi$. Scaling gives $\|h_\delta\|_{C^{2,\alpha}}=O(\delta^{p+1-\alpha})$, while the supremum of its center factor is $O(\delta^p)$. Both tend to zero. Its central strain is $O(\delta^{p+2})$ by scaling the absolutely convergent density kernel integral. Thus even adding a continuous factor supremum and the normalization functional does not make this fractional coefficient continuous in the ambient correction space.

The conclusion is limited to the unrestricted function class and the explicitly defined local coefficient. The PDE could impose additional quantitative constraints on exact solutions. An asserted bound on the exact-profile $B_3$ therefore needs those constraints and a proof, not a reference to the trial's fractional term or bare P2 closeness.

## Order-zero coupling is not automatically compact or arbitrarily small

Let $s$ be a nonnegative integer, $0<\alpha<1$, and let $g=(g_1,g_2)$ be smooth near a rectangle away from the coordinate axes, with $g_2$ nonzero at an interior point. Choose a smooth cutoff $b$, supported inside that rectangle and nonzero near that point. Define a potential

$$\Phi_N=N^{-s-\alpha-2}b(X)\cos(Nx),\qquad h_N=-\Delta\Phi_N.$$

Reflect it evenly in $x$ and oddly in $y$ using disjoint supports. It then has density parity and vanishes near the center, so $h_N$ preserves center normalization and $c[h_N]=\Phi_{N,xxy}(0)/3=0$. The exact canonical velocity is $U[h_N]=(-\Phi_{N,xy},\Phi_{N,xx})$. Direct differentiation gives, on the original rectangle,

$$h_N=N^{-s-\alpha}b\cos(Nx)+O_{C^{s,\alpha}}(N^{-1}),\qquad U[h_N]\cdot g=-N^{-s-\alpha}g_2b\cos(Nx)+O_{C^{s,\alpha}}(N^{-1}).$$

To justify the norm remainders, every extra derivative of an oscillatory factor costs at most $N$, and $[e^{iNx}]_{C^\alpha}\le C_\alpha N^\alpha$, which follows by bounding its difference by $\min(2,N|x-x'|)$. A term with prefactor $N^{-s-\alpha-1}$ is therefore $O(N^{-1})$ in $C^{s,\alpha}$ after multiplying by a fixed smooth function.

The sequence $h_N$ is bounded in $C^{s,\alpha}$. The coupling tends to zero uniformly with all derivatives through order $s$. Its top Holder seminorm is nevertheless bounded below: take two points inside the region where $g_2b\ne0$, separated in the $x$ direction by $\pi/N$, whose oscillatory $s$-th derivatives have opposite maximal phase. Their coefficient values converge to the same nonzero value, and division by their separation to the power $\alpha$ cancels the $N^{-\alpha}$ derivative amplitude. Hence no subsequence of the coupling converges in $C^{s,\alpha}$, since any norm limit would have to be zero by uniform convergence. This proves noncompactness of this coupling on that same regularity space.

It also prevents a bound of the form $\|U[h]\cdot g\|_{C^{s,\alpha}}\le\eta\|h\|_{C^{s,\alpha}}+C_\eta\|\nabla\Phi\|_2$ for every arbitrarily small $\eta>0$: the energy of these potentials tends to zero while the ratio of top norms stays positive. This test does not refute compactness relative to some stronger transport graph norm, and does not estimate the actual inverse of $L$.

## Large annuli defeat the old homogeneous H-minus-one forcing space

Suppose $F(r,\theta)=r^\sigma A(\theta)+o(r^\sigma)$ uniformly in angle on large annuli, with continuous nonzero $A$ and $\sigma>-2$. Choose a compactly supported smooth test $\phi$ on $1<r<2$ whose angular projection pairs nontrivially with $A$. Such a choice exists by continuity and localization near a point where $A$ has fixed sign. Put $\phi_R(X)=\phi(X/R)$. In two dimensions, $\|\nabla\phi_R\|_2=\|\nabla\phi\|_2$, whereas

$$\langle F,\phi_R\rangle=R^{\sigma+2}\left(\int |Y|^\sigma A(\arg Y)\phi(Y)dY+o(1)\right).$$

The coefficient is nonzero, so this pairing is unbounded. Thus $F$ is not a bounded functional on homogeneous $\dot H^1$ tests. The test can be symmetrized to match the density parity when $A$ has that parity. Applying this to $G\sim k r^k\Theta_0$ and, conditionally on a nonzero leading defect, $\epsilon\sim r^{2k-1}F_0$ gives the two unweighted obstructions in the prompt. These are forcing-space failures and do not imply profile nonexistence.
