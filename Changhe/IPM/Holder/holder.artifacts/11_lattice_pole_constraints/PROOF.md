# Imposing pole values by lattice operations

## Statement

Use the real homogeneous Holder space and Riesz conventions in
`../01_setup/PROOF.md`. Fix 0<alpha<1, x=(1/2,0), y=-x, and 0<=c<=1/2.
Let F be a globally Holder function with [F]_alpha<=1, F(-z)=-F(z),
and F(x)=F(y)=0. Define

$$L_c(z)=\max\{-c-|z-x|^\alpha,c-|z-y|^\alpha\},$$
$$U_c(z)=\min\{-c+|z-x|^\alpha,c+|z-y|^\alpha\},$$
$$f_c(z)=\max\{L_c(z),\min\{F(z),U_c(z)\}\}.$$

Then L_c<=U_c, [f_c]_alpha<=1, f_c is centrally odd,
f_c(x)=-c, f_c(y)=c, and f_0=F. Thus, for any real normalized
kernel K_beta=cos(2 theta-2 beta)/(2 pi r^2),

$$D_\alpha\ge \operatorname{pv}\int
[K_\beta(z-x)-K_\beta(z-y)]f_c(z)\,dz+c.$$

The right side is the increment of a rotated R_1^2. Its denominator
is one since |x-y|=1. A negative value can be replaced by its absolute
value, but the displayed one-sided lower bound suffices.

## Proof

Each cone has Holder seminorm at most one. This follows from the
triangle inequality and |s^alpha-t^alpha|<=|s-t|^alpha.
The minimum and maximum of finitely many functions with seminorm at
most one have the same bound: compare each function at the two points,
then take the same minimum or maximum. Consequently all three displayed
functions have seminorm at most one.

The only nonautomatic comparison needed for L_c<=U_c is
2c<=|z-x|^alpha+|z-y|^alpha. It follows from 2c<=1,
|x-y|<=|z-x|+|z-y| and subadditivity of the power alpha.
At x the upper and lower intervals collapse to -c, and similarly at y
to c. The identities L_c(-z)=-U_c(z) and F(-z)=-F(z) show that projection
onto this interval commutes with central negation. For c=0 the original
Holder inequalities at the two poles put F between L_0 and U_0.

Central oddness yields |f_c(z)|<=2^(alpha-1)|z|^alpha. Thus the increment
converges at infinity by the dipole decay, and at the poles after
subtracting their values by alpha>0. The local term of R_1^2 is -I/2;
its increment equals c. Rotation invariance gives the stated lower
bound for D_alpha, including when beta is not an axis direction.
The compact smooth test-class approximation from the setup proof makes
this a lower bound for the originally specified supremum as well.

## Polygonal specialization

Let a>0 and let Z be the centrally symmetric zero set comprising the
horizontal axis and, from x and y, vertical segments of height a followed
by rays at angles pi/3 and 2pi/3. Use the signed-distance C witness F
proved in `../05_team_audit/structured_witness/PROOF.md`, translated
by (-1/2,0) to the present midpoint coordinates. Its value in the first
quadrant is

$$F(X,Y)=2^{\alpha-1}\operatorname{sgn}(X-b(Y))
\min\{Y,d((X,Y),\Gamma_a)\}^{\alpha},\qquad
b(Y)=1/2+(Y-a)_+/\sqrt3.$$

Here Gamma_a is the right vertical segment and its outgoing ray.
The function is even in X and odd in Y, hence centrally odd.
For beta=pi/4, nu=K_xy(z-x)-K_xy(z-y) is also even in X and odd in Y.
The modified f_c has only the central symmetry. Nevertheless its full
integral is exactly

$$2\int_{X,Y>0}\nu(X,Y)
\{P_{[L_c,U_c]}(F(X,Y))-P_{[L_c,U_c]}(-F(X,Y))\}\,dX\,dY,$$

because L_c,U_c are even in Y. This is a useful two-dimensional integral
formula, not a certified numerical value. Singular and exterior errors
must still be bounded for any numerical lower-bound claim.
