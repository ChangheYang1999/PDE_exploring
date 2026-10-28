# Joint transport on the two local circles

## Exact decomposition

Use the homogeneous Holder seminorm, quotient operator definition and
normalized kernels in `../../01_setup/PROOF.md`. Set x=(1/2,0), y=-x,
0<R<=1/2 and 0<alpha<1. Write

$$K_\phi(z)=\operatorname{Re}(e^{i\phi}/z^2)/(2\pi),\qquad
\nu_\phi(z)=K_\phi(z-x)-K_\phi(z-y).$$

For 0<r<R and 0<=theta<2pi put z_r(theta)=x+r exp(i theta), and

$$w_\phi(r,\theta)=\frac{\cos(2\theta-\phi)}{2\pi}
-\frac{r^2}{2\pi}\operatorname{Re}
\frac{e^{i\phi}}{(1+r e^{i\theta})^2}.$$

The contribution from the two local disks to the increment equals

$$\int_0^R\!\frac{dr}{r}\int_0^{2\pi}
 w_\phi(r,\theta)[f(z_r(\theta))-f(-z_r(\theta))]d\theta.$$

This follows by polar coordinates in B(x,R), central oddness of nu,
and reflection of the disk B(y,R). The own kernel has angular mean zero;
therefore the improper integral at zero is interpreted after subtracting
f(x) and f(y) in those terms. Its convergence follows from alpha>0.
The other-pole kernel is smooth and integrable on the disks.

For the diagonal Riesz transform, choose any nonnegative measurable
lambda on (0,R) with integral lambda(r) dr/r=1/2. Add the atoms
-lambda(r) delta_x+lambda(r) delta_y to the signed circle measure at each
radius. Integrating them gives exactly -[f(x)-f(y)]/2. For example,

$$\lambda_p(r)=\frac p2(r/R)^p,\qquad p>0,$$

has the required integral. This is an exact redistribution of the
identity term, with no estimate or extra term.

## Transport bound

For each r, the circle measure and the optional two atoms have total
mass zero and are centrally odd. Any nonnegative finite measure on
ordered pairs whose first marginal minus its second marginal equals
this signed measure gives

$$\left|\int f\,d\mu_r\right|
\le [f]_\alpha\int |z-z'|^\alpha d\pi_r(z,z').$$

Indeed write the left functional as the integral of f(z)-f(z') and
apply the definition of the seminorm. Equality of separate positive
and negative marginals is sufficient but not necessary; additional
canceling flow through intermediate supports is allowed.
Integrate this bound against dr/r. A finite certified sum requires
actual measure domination for extracted cell masses, exact flow
balances and upper bounds for all pair distances.

A useful finite construction partitions angle and radius. On a radial
interval [a,b], extract exact nonnegative masses from angular cells
uniformly for all r in that interval, using a certified fixed sign and
a lower bound for the absolute angular integral. Pair these extracted
masses by exact rational flows. Pair the unextracted centrally odd
remainder with its central reflection. If M_j(r) bounds its total
variation in the right-circle cell, that contribution costs at most
(1+2b)^alpha M_j(r). For same-circle flow, a certified angular chord
bound c gives the integrated cost

$$m c^\alpha(b^\alpha-a^\alpha)/\alpha.$$

For flow between the two circles, use the supremum of the distance over
the two angular cells and r in [a,b], multiplied by m log(b/a).
Atoms can be included as zero-radius supports. If lambda varies over
[a,b], only its certified common lower mass can enter a constant flow;
the remaining mass must be included in the remainder bound.

Below a positive cutoff delta, the already proved local estimates and
the exact omitted identity mass bound give an explicit error. No
numerical constant is asserted until these conditions are checked.
In particular, a floating discrete transport optimum is diagnostic only.

## Certified angular cells and the omitted small disks

For a radial bin [a,b] with 0<a<b<=1/2, let h=2pi/N and
I_j=[phi/2+pi/4+jh,phi/2+pi/4+(j+1)h]. These endpoints align the
zeros of the own-pole angular kernel. The own-pole mass is evaluated
exactly by the sine antiderivative. Put

$$q(r,\theta)=\frac{r^2}{2\pi}\operatorname{Re}
 \frac{e^{i\phi}}{(1+r e^{i\theta})^2}.$$

Twice differentiating the complex expression gives

$$\left|\partial_\theta^2q\right|
 \le \frac{b^3(1+2b)}{\pi(1-b)^4}=:L_2.$$

Indeed the second derivative before taking the real part is
$r^3e^{i(\phi+\theta)}(1-2re^{i\theta})/
[\pi(1+re^{i\theta})^4]$. Thus its cell integral is enclosed by
$h q(r,\theta_j)+[-L_2h^3/24,L_2h^3/24]$, with interval evaluation
uniform over r in [a,b]. A direct interval evaluation of w on the whole
cell certifies its sign. If the sign is fixed, this mass enclosure
bounds the absolute mass from above and below. Otherwise take no
extracted mass and bound the cell variation by h times the certified
supremum of |w|. Extracted masses are rounded down to multiples of
2^{-44}. This is a measure domination statement, not a midpoint
replacement of the continuous density.

For same-circle cells let k be their circular index distance. Their
angular separation is at most min(pi,2pi(k+1)/N), so the unit-radius
chord bound is $2\sin(\pi\min(k+1,N/2)/N)$. For opposite-circle cells
the distance is $|1+r(e^{i\theta}+e^{i\eta})|$. For fixed angles its
square is a convex quadratic in r, so its maximum over [a,b] occurs
at a or b. Complex interval evaluation at these two endpoints gives
a valid uniform upper bound over the angular cells. Each exact
nonnegative integer flow is checked to have precisely the specified
signed marginals before these costs are summed.

For 0<delta<1/2, the omitted two disks have the explicit C-bound

$$S_\alpha(\delta)=\frac{2a_2(\alpha)\delta^\alpha}{\alpha}
 +\frac{(1+2\delta)^\alpha\delta^2}{2(1-\delta)^2},\qquad
 a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

The first term is the two own-pole circular estimates. On the right
circle the variation of the other-pole density is at most
$r^2/(1-r)^2$; pair it with its central reflection at distance at
most 1+2delta, then integrate dr/r. This gives the second term.

## Completion with the other spatial regions

Let L_alpha(phi) be the sum of the certified radial-bin costs on
[delta,1/2], W_alpha(phi) the already certified middle-region cost,
and E_alpha(phi) the exterior cost. These regions are disjoint up to
null boundaries and exhaust the plane outside the two omitted disks.
There is no separate smooth cross-disk term: it is already included
in w. For phases phi_j=j*pi/(2m), j=0,...,m, the full estimate is

$$C_\alpha\le S_\alpha(\delta)+\sec\frac{\pi}{4m}
 \max_j\{L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)\}.$$

Reflection in the horizontal axis sends phi to -phi, and changing the
operator sign sends phi to phi+pi. Thus it suffices to cover
[0,pi/2]. Between consecutive nodes the density is the positive sine
interpolation of the two endpoint densities. The coefficient sum is
at most sec(pi/(4m)); apply the triangle inequality to the remainder
functional after removing the two small disks, then add their uniform
bound S_alpha(delta). All statements hold for 0<alpha<1 and real
homogeneous Holder functions modulo constants as defined in the setup.
The optional identity redistribution above is not covered by this
C-only phase formula: it needs its own phase range and interpolation
correction before it can certify a D-bound.
