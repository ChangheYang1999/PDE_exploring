# Transport on the truncated middle circles

## Statement and conventions

Use the real homogeneous Hölder seminorm and singular-integral increments of `../../01_setup/PROOF.md`. Let x=(1/2,0), y=-x, and define the complex increment kernel

$$G(z)=\frac{z}{\pi(z^2-1/4)^2}=\frac1{2\pi}\left((z-1/2)^{-2}-(z+1/2)^{-2}\right).$$

Changing the sign of the imaginary component changes only the phase convention. For a phase phi, put nu_phi=Re(exp(i phi)G). Let

$$E=B(0,1)\setminus(B(x,1/2)\cup B(y,1/2)).$$

The finite procedure below produces an upper bound for

$$\left|\int_E\nu_\phi(z)f(z)\,dA(z)\right|\le M_\phi(\alpha)[f]_\alpha,\qquad0<\alpha<1.$$

It bounds a nonsingular part of the increment. The local and exterior pieces are treated in the previously proved midpoint and exterior-circle theorems. This note asserts a general certificate procedure; a numerical value is a theorem only after its input enclosures and exact transport constraints have been checked.

## Coordinates and measure

Write r=sin(t), 0<t<pi/2. On the upper half of E, the allowed angles are

$$\theta=\pi/2+t s,\qquad -1\le s\le1.$$

Indeed exclusion of the two radius-1/2 pole disks is equivalent to |cos(theta)|<=r. The lower half is the image under z to -z. At fixed t define

$$z(t,s)=\sin(t)\exp(i(\pi/2+t s)),\qquad
w_\phi(t,s)=t\sin(t)\cos(t)\operatorname{Re}(e^{i\phi}G(z(t,s))).$$

Since dA=r dr dtheta, the middle functional is

$$\int_0^{\pi/2}\int_{-1}^1w_\phi(t,s)\big(f(z(t,s))-f(-z(t,s))\big)\,ds\,dt.$$

This uses G(-z)=-G(z). No singular limit is involved: every point of E is at distance at least 1/2 from both poles.

## Uniform cell masses on a radial bin

Partition t into closed bins [a,b] and s into N equal cells of width h=2/N. For each upper-half cell j, suppose a real interval J_j contains its signed mass integral for every t in the bin. Require additionally that the density has a fixed sign on that cell whenever a nonzero model mass is extracted. Let T_j be an upper bound for its total variation. Choose a rational signed mass m_j of the same sign, with

$$|m_j|\le\inf_{t\in[a,b]}\left|\int_{\text{cell }j}w_\phi(t,s)\,ds\right|.$$

If the sign is not certified, take m_j=0. Set m_(j+N)=-m_j for the reflected lower cell. At every t one may extract this exact mass from the actual signed cell measure by proportional scaling. The unextracted measure is centrally odd, and its half-plane total variation is at most

$$R=\sum_{j=0}^{N-1}T_j-\sum_{j=0}^{N-1}|m_j|.$$

The extraction need not be chosen continuously in t: an explicit proportional formula is measurable, and the upper bound is pointwise in t.

## Exact finite transport and cell distances

Choose any nonnegative rational transport pi_ij from positive model cells to negative model cells whose row and column sums equal their exact masses. Pair the extracted submeasures by product couplings on each cell pair. For an upper bound c_ij on the alpha power of the distance between any two points in those cells, uniformly over the radial bin, the extracted part costs at most sum pi_ij c_ij. Pair the centrally odd remainder antipodally. Its cost is at most (2 sin b)^alpha R.

Here are explicit distance bounds. First reduce each cell index modulo N to an integer in {0,...,N-1}; let k be the ordinary absolute difference of these reduced indices. If both cells are in the same half-plane, their angular difference is at most 2b(k+1)/N, so one can take

$$c^{\rm same}_k=\left[2\sin b\;\sin\left(\min\{\pi/2,b(k+1)/N\}\right)\right]^\alpha.$$

If they lie in opposite half-planes, their angular separation is pi plus or minus t times the difference of their s coordinates. Therefore

$$c^{\rm opposite}_k=\left[2\sin b\;\cos\left(a\max\{0,k-1\}/N\right)\right]^\alpha.$$

Both bounds allow all points of each cell, rather than only its midpoint. The bin contribution is at most

$$(b-a)\left(\sum_{i,j}\pi_{ij}c_{ij}+(2\sin b)^\alpha R\right).$$

Summing these contributions proves the asserted middle-region upper bound. A heuristic may select the finite plan; rigorous validity requires only exact nonnegativity, exact marginal conservation, and the proved distance and measure enclosures.

## One explicit interval enclosure for the masses

For fixed t, differentiate in s. On E,

$$|G'(z)|\le16/\pi,\qquad |G''(z)|\le96/\pi.$$

These follow directly from the two pole terms and their distance lower bound 1/2. With W=t sin(t) cos(t), r=sin(t),

$$|\partial_s w_\phi|\le Wt\,16r/\pi=:L_1(t),$$

$$|\partial_s^2w_\phi|\le Wt^2(16r+96r^2)/\pi=:L_2(t).$$

Use upper interval bounds L1,L2 on each bin. If an interval Jmid encloses w_phi(t,s_mid) for every t in the bin, then Jmid+[-L1 h/2,L1 h/2] encloses the density on the full cell. This certifies its sign when zero is excluded. Its signed mass is enclosed by

$$hJ_{\rm mid}+[-L_2h^3/24,L_2h^3/24].$$

For a fixed-sign cell this also gives its total variation interval. Without a fixed sign, h times the upper absolute density bound suffices. Rounding the lower absolute mass down to an exact multiple of 2^(-44) is an admissible model extraction. This is the same positive-submeasure principle as the independently checked exterior-circle construction.

All quantities remain bounded at t=0 and t=pi/2. Endpoints have measure zero. Interval implementations may clip sin and cos to [0,1], using their known signs on this parameter range, to avoid spurious negative endpoints from outward rounding.
