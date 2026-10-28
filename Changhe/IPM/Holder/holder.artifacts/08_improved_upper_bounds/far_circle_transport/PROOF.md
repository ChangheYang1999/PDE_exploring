# Certified transport on exterior circles

## Statement and scope

Use the real homogeneous Hölder space, quotient definition and operator normalization of `../../01_setup/PROOF.md`. The increment points are $x=1/2$, $y=-1/2$. All statements below hold for $0<\alpha<1$. The exterior increment density is the real phase component of

$$G(re^{i\theta})=\frac1{\pi r^3}\frac{e^{-3i\theta}}{(1-qe^{-2i\theta})^2},\qquad q=\frac1{4r^2},\quad r\ge1.$$

Define the normalized real density

$$g_{q,\phi}(\theta)=\operatorname{Re}\frac{e^{i\phi-3i\theta}}{\pi(1-qe^{-2i\theta})^2}.$$

It satisfies $g(\theta+\pi)=-g(\theta)$. A bound $B_\alpha(q,\phi)$ for its action on functions on the unit circle with Hölder seminorm one gives exterior cost

$$\int_1^\infty r^{\alpha-2} B_\alpha(1/(4r^2),\phi)\,dr
=\int_0^1 u^{-\alpha}B_\alpha(u^2/4,\phi)\,du.$$

The following finite construction bounds this integral rigorously, uniformly on each closed $u$ interval. It can replace the exterior harmonic sum in the midpoint theorem. This proof establishes the construction; a numerical table is valid only after its separate certificate has been audited.

## A circle-cell transport lemma

Partition the circle into $n$ equal half-open angular cells $I_j$ of length $\Delta=2\pi/n$, where $n$ is even and $I_{j+n/2}=I_j+\pi$. For the first $n/2$ cells choose signed rational masses $m_j$. Set $m_{j+n/2}=-m_j$.

For every parameter $q$ in a stated interval, require either $m_j=0$, or that $g_{q,\phi}$ has the constant sign of $m_j$ on $I_j$ and

$$|m_j|\le\int_{I_j}|g_{q,\phi}(\theta)|\,d\theta.$$

Let $T_j$ be any upper bound for the latter integral, also when $m_j=0$. Choose any nonnegative rational transport matrix $\pi_{jk}$ whose row sums are the positive $m_j$ and whose column sums are the magnitudes of the negative $m_k$. Define

$$c_{jk}=\left[2\sin\left(\frac{\min\{\pi,d_{jk}+\Delta\}}2\right)\right]^\alpha,$$

where $d_{jk}\in[0,\pi]$ is the shorter angular distance between cell centers. Then the following quantity bounds the normalized circle functional:

$$B_\alpha=\sum_{j,k}\pi_{jk}c_{jk}
+2^\alpha\sum_{j=0}^{n/2-1}(T_j-|m_j|).$$

This is an upper bound for every density parameter in the specified interval. The transport need not be optimal. Taking the smaller of several independently valid transports is allowed at a fixed parameter interval and exponent.

### Proof

For each nonzero $m_j$, take from the density on $I_j$ the submeasure of mass $|m_j|$ obtained by multiplying its absolute density by $|m_j|/\int_{I_j}|g|$. Couple these submeasures according to $\pi_{jk}$, using product couplings within each pair of cells. All distances between two cells are bounded by the chord used in $c_{jk}$, so this part costs at most the first sum. Choose the submeasure on the opposite cell by central reflection. The residual signed density is then centrally odd, with unchanged sign in each selected cell. Its total variation on the first half-circle is at most $\sum(T_j-|m_j|)$. Pairing each point with its antipode costs exactly $2^\alpha$ times that half-circle variation. This proves the second term. The argument uses ordinary finite measures on a compact circle and no infinite-measure transport duality.

## Verified cell masses

Write $z=e^{i\theta}$ and $F_q(\theta)=z^{-3}/[\pi(1-qz^{-2})^2]$. The convergent series

$$F_q(\theta)=\frac1\pi\sum_{k\ge0}(k+1)q^k e^{-i(2k+3)\theta}$$

implies, for $0\le q\le Q\le1/4$,

$$|F_q'|\le M_1(Q)=\frac{3(1+Q)}{\pi(1-Q)^3},\qquad
|F_q''|\le M_2(Q)=\frac{9(1+4Q+Q^2)}{\pi(1-Q)^4}.$$

Indeed $2k+3\le3(k+1)$ and $(2k+3)^2\le9(k+1)^2$; summing $(k+1)^2Q^k$ and $(k+1)^3Q^k$ gives the two bounds. They apply to every real phase component.

Evaluate $g$ at the cell midpoint with interval arithmetic in $q$. The interval enlarged by $M_1\Delta/2$ encloses $g$ throughout that angular cell. If its sign is definite, the midpoint rule with the second-derivative bound encloses the signed cell mass by

$$\Delta\,g(\theta_j)+[-M_2\Delta^3/24,M_2\Delta^3/24].$$

Round a lower bound for its magnitude downward to an integer multiple of a chosen positive rational unit. This yields an admissible $m_j$. Use the corresponding upper mass bound as $T_j$. If the sign is not definite, put $m_j=0$ and use $T_j=\Delta\sup_{I_j}|g|$, with the first-derivative enclosure. These rules remain valid when an angular cell contains a zero or the parameter interval contains a moving zero.

## An explicit adjacent-lobe transport

Discard zero masses when forming consecutive runs of one sign, retaining their actual angular cell indices for costs. If there are $2k$ alternating runs, write the positive-run masses as $p_i$ and the following negative-run magnitudes as $n_i$, in circular order. They satisfy $\sum p_i=\sum n_i$.

Let $d_0=0$ and $d_{i+1}=d_i+n_i-p_i$. For any rational

$$\max_i(-d_i)\le t\le\min_i(p_i-d_i),$$

put $x_i=t+d_i$. The positive run $i$ sends its leftmost mass $x_i$ to the preceding negative run, and its rightmost mass $p_i-x_i$ to the following negative run. The identity

$$p_i-x_i+x_{i+1}=n_i$$

proves that every negative run receives exactly its required mass. Split boundary cells fractionally when a mass cut passes through a cell. Pair each source and destination part in order starting at their common boundary. A finite greedy merge of their rational cell masses gives a rational transport matrix with exactly the stated row and column sums.

If the feasible interval is empty, the antipodal transport always exists and is used instead. Trying several rational $t$ values and selecting any one by a floating heuristic does not affect validity, because each selected matrix is checked by exact rational row and column sums. No optimality assertion is needed.

## Radial integration and the infinite tail

On a closed interval $[u_0,u_1]\subset(0,1]$, construct a uniform circle bound with $q\in[u_0^2/4,u_1^2/4]$. Its exterior contribution is at most

$$B_\alpha\frac{u_1^{1-\alpha}-u_0^{1-\alpha}}{1-\alpha}.$$

For the remaining interval $0<u<v$, use the harmonic majorant from `../midpoint_split/PROOF.md`, scaled to radius $1/v$:

$$\frac{2a_3(\alpha)v^{1-\alpha}}{1-\alpha}
+2\sum_{k\ge1}\frac{(k+1)4^{-k}a_{2k+3}(\alpha)v^{2k+1-\alpha}}{2k+1-\alpha}.$$

The same Jensen bounds for $a_{2k+3}$ and positive geometric remainder apply. All series terms are nonnegative. This treats the infinite radial tail exactly as a proved bound, without a numerical cutoff assumption.

## All phases

For each fixed phase-grid node, add the near-circle bound, the regular-region reflection bound, and the new exterior bound. The exact full increment functional is linear in the two phase coefficients. Therefore, if $U_j$ bounds its norm at phase $\phi_j=j\pi/(2m)$, the full scalar operator norm is at most

$$\sec\left(\frac\pi{4m}\right)\max_j U_j.$$

This last inflation applies to the full node bound. A smaller alternative is to keep a phase-independent near estimate outside the interpolation and apply the inflation only to the sum of the regular and exterior functional bounds. Indeed that sum is itself a linear phase-dependent functional after the two local operators have been subtracted. The absolute error bound for the local part is uniform in phase. The same reasoning holds for the diagonal bound with the local projection replacement and its additional mass $1/2$.

The construction is a rigorous finite upper-bound procedure. Until its implementation and data are audited, it does not by itself certify any new displayed decimal value.
