# A projection witness up to exponent one half

## Statement

Use the homogeneous Hölder space and operator normalization in
`../../01_setup/PROOF.md`. Let 0<alpha<=1/2, a>0, and
0<rho<=min(1,a/7). Let Gamma_a, its signed distance s_a, V=(s_a,Y),
Pi=2|s_a Y|/|V|, the profile F and the clamped centrally odd function f be
exactly as in `../finite_projection_witness/PROOF.md`.

For 0<u<1 set R=u^alpha, k=1/(1-alpha), and

$$K_\alpha=\max\left\{1,\sup_{0<u<1}
\min\left((1-u)^{-\alpha},
\left(\frac{1+R^k}{2}\right)^{1/k}
+\frac{1-R}{2(1-u)^\alpha}\right)\right\}.$$

Then [f]_alpha<=K_alpha, f(x)=-1/2, f(y)=1/2, and

$$D_\alpha\ge\frac{J_\alpha(a,\rho)+1/2}{K_\alpha}.$$

The quadrant formula for J, and its explicit local and tail error bounds,
are unchanged. All these statements concern the real homogeneous
seminorm; the compact smooth test class gives the same lower bounds.
This is a proved family, not an assertion of an optimal profile constant
or of an exact operator norm.

## Local profile at the larger exponents

The local projection profile g has the same definition as in
`../local_projection_profile/PROOF.md`. Its same-quadrant estimates extend
to alpha<=1/2: for distance D<=min(|p|,|q|), the quotient is at most
(alpha+2^alpha)/2<1, because 1/2+sqrt(2)<2. For D>=min(|p|,|q|), a negative
quadrant gives 2^(alpha-1)<=1; a positive quadrant gives
(1+t)^alpha-t^alpha/2<=1+alpha t-t^alpha/2<=1. Opposite quadrants of equal
sign have D>=max(|p|,|q|), also giving a quotient at most one.

For opposite signs, the ordering g(q)-g(p) is bounded by D^alpha/2 as
before. Normalize the positive point to radius one and denote the negative
radius by u. If u>=1, the same concavity argument gives quotient at most
one. If u<1, the range bound gives (1-u)^(-alpha). The exact weighted
power-mean maximization with sin(2a)+sin(2b)<=2D gives the other displayed
bound. This holds for every alpha<1. Thus [g]_alpha<=K_alpha for the full
range in this theorem. Continuity covers the axes and origin.

K_alpha is finite. Near u=0 use the first bound, which tends to one. Near
u=1 use the second: M-(1+R)/2 tends to zero quadratically in 1-R, and
(1-R)(1-u)^(-alpha)=O((1-u)^(1-alpha)). The explicit endpoint bounds in
`../refined_profile_constant/PROOF.md` remain valid, since its power-mean
Taylor estimate holds for 1<k<=2: the second derivative of x^k on [R,1]
is bounded by k(k-1)R^(k-2).

## Global assembly

The frozen planar profile is the minimum of g and a profile of seminorm
at most one, so it has seminorm at most K_alpha. Outside the frozen set,
the curved profile has seminorm at most one for alpha<=2/3, by its
2sqrt(2)-Lipschitz same-sign bound and its distance-to-zero-set bound for
opposite signs. These are the estimates in the earlier assembly proof.

The piecewise-linear graph agrees exactly with its vertical segment for
nearest-point purposes in B(x,sqrt(3)a/2). Hence the local map V equals
z-x throughout B(x,6rho), since 6/7<sqrt(3)/2. A frozen point satisfies
|V(p)|<=rho and thus |p-x|<=rho, as previously proved.

For a mixed pair p,q with R0=|q-x|>=6rho, the only ordering that is not
bounded immediately by the outer profile has quotient at most

$$\frac12\left[\left(\frac{\rho}{R_0-\rho}\right)^\alpha
+\left(\frac{2R_0}{R_0-\rho}\right)^\alpha\right]
\le\frac12\left(5^{-\alpha}+(12/5)^\alpha\right)\le1.$$

The last expression is convex in alpha, equals one at zero, and at one
half is (1+2sqrt(3))/(2sqrt(5))<1; squaring reduces this to 4sqrt(3)<7.
This covers all remaining pairs. Clamping to the same barriers and
extending centrally oddly preserves max(K_alpha,1)=K_alpha. Finally
rho<=1 ensures that the radial frozen value B=min(|V|,rho)^alpha is at
most one, so the earlier exact clamp-amplitude formula applies verbatim.
Its integral and local/tail estimates therefore prove the lower bound.
