# Exact transport on four-point reflection orbits

## Statement and scope

Use the real homogeneous Hölder space, kernels and quotient extension of `../../01_setup/PROOF.md`. Let $0<\alpha<1$. This result improves the regular-region term in the midpoint theorem `../midpoint_split/PROOF.md`; all its local and exterior terms remain as stated there.

For $w=X+iY$ in the first quadrant, set

$$h=(2X)^\alpha,\qquad v=(2Y)^\alpha,\qquad d=(2|w|)^\alpha.$$

For nonnegative $a,b$, define

$$\mathcal P_\alpha(w;a,b)
=2\max\{a h+b(d-h),\ a(d-v)+b v\}.$$

Let $E=B_1(0)\setminus(B_{1/2}(1/2)\cup B_{1/2}(-1/2))$ and

$$G(w)=\frac{w}{\pi(w^2-1/4)^2},\qquad Q(w)=\frac1{2\pi(w+1/2)^2}.$$

For $0\le\phi\le\pi/2$, put

$$\widetilde M_\alpha(\phi)
=\int_{E\cap\{X>0,Y>0\}}
\mathcal P_\alpha(w;|\operatorname{Re}G(w)|\cos\phi,
 |\operatorname{Im}G(w)|\sin\phi)\,dA(w)
+\int_{B_{1/2}(1/2)\cap\{Y>0\}}
\mathcal P_\alpha(w;|\operatorname{Re}Q(w)|\cos\phi,
 |\operatorname{Im}Q(w)|\sin\phi)\,dA(w).$$

In every bound of the midpoint theorem, $M_\alpha$ may be replaced by $\widetilde M_\alpha$. In particular, for each integer $m\ge1$,

$$C_\alpha\le\frac{2a_2(\alpha)2^{-\alpha}}\alpha+H_\alpha+
\sec\left(\frac\pi{4m}\right)\max_{0\le j\le m}
\widetilde M_\alpha\left(\frac{j\pi}{2m}\right),$$

$$D_\alpha\le\frac{2A_\alpha2^{-\alpha}}\alpha+\frac12+H_\alpha+
\sec\left(\frac\pi{4m}\right)\max_{0\le j\le m}
\widetilde M_\alpha\left(\frac{j\pi}{2m}\right).$$

The quantities $a_2,A,H$ are explicitly defined in the two preceding proofs. The new regular term is pointwise no larger than the old one. These formulas cover all kernel phases, and also complex inputs by scalar phase projection. They do not claim global optimality of the transport.

## The finite transport problem

Take the four points $(\pm X,\pm Y)$ with $X,Y>0$. For two real coefficients, the signed masses are the linear combination of the horizontal and vertical sign characters. Reflections of the four points allow their magnitudes to be denoted $a,b\ge0$, with masses

$$a+b,\quad a-b,\quad -a+b,\quad -a-b$$

at $(X,Y),(X,-Y),(-X,Y),(-X,-Y)$ respectively.

Suppose $a\ge b$. Send mass $a-b$ along each of the two horizontal edges and the remaining mass $2b$ along the diagonal from $(X,Y)$ to $(-X,-Y)$. The cost in the metric $|z-z'|^\alpha$ is

$$2(a-b)h+2b d.$$

Every transport between the positive and negative masses is described by a number $q\in[0,a-b]$: it sends mass $q$ along each horizontal edge and the remaining masses across the two diagonals. Its cost is $2qh+2(a-q)d$. Since $h\le d$, the displayed plan minimizes that cost at $q=a-b$.

If $b\ge a$, the analogous optimal cost is $2(b-a)v+2ad$. The snowflake triangle inequality gives $h+v\ge d$. Hence the difference between the two linear expressions in the maximum defining $\mathcal P$ is $(a-b)(h+v-d)$, so that maximum equals precisely the cost just computed in both cases.

For any function with $[f]_\alpha\le1$, summing its increments along this explicit transport bounds the signed four-point functional by $\mathcal P$. No general infinite-measure transport duality is invoked.

Also $h,v\le d$, so

$$\mathcal P_\alpha(w;a,b)\le2\max(a,b)d.$$

This is the old antipodal cost. Unless the masses or coordinates are degenerate, the inequality is strict when $a\ne b$.

## Integration and phase interpolation

The midpoint regular density is odd under central reflection. Its real-kernel coefficient is even under conjugation, and its imaginary-kernel coefficient is odd. The domains $E$ and the union of the two local disks are invariant under both reflections. Consequently each four-point orbit has exactly the mass pattern above, with $a,b$ as in the statement. Integrating the finite transport inequality gives $\widetilde M$ as a valid regular-region bound. Absolute convergence follows from the nonsingular kernel denominators on these regions.

For fixed $w$, the cost is the maximum of two nonnegative linear combinations of the absolute values of the two coefficients. It is therefore a seminorm of those coefficients. Its integral is also a seminorm, even in phase and periodic with period $\pi$. The same positive interpolation of neighboring unit vectors used in the midpoint theorem yields the factor $\sec(\pi/(4m))$ for the full phase interval. The local and exterior estimates are unchanged.

## Interval parameterizations

Use the two exact rectangular parameterizations of the midpoint proof. At each rectangle evaluate $h,v,d$ and the maximum formula for $\mathcal P$ with interval arithmetic. The differences $d-h$ and $d-v$ are nonnegative on the true domains; interval subtraction may have a negative lower endpoint but still encloses them. The first-quadrant coordinates may be replaced by their absolute values when rounding straddles zero. The known nonnegative range is used for every fractional power at zero. Thus ordinary rectangle interval quadrature remains rigorous.
