# Axis velocity control and global source uniqueness

Status: proved conditional statements. The result concerns any exact P_2 solution in a specified trial neighborhood, without asserting that such a solution exists.

## A weighted factor norm

Fix L>0 and 0<k<1. Put W(r)=(1+r^2/L^2)^{(k-3)/2}. Let h be C^{2,alpha}_loc, even in x and odd in y, with the canonical velocity specified by K_1(Z)=-z_1z_2/(pi|Z|^4), K_2(Z)=(z_1^2-z_2^2)/(2pi|Z|^4), symmetric annular truncation, and the local term -h e_2/2, and

|h(x,y)| <= epsilon x^2 |y| W(r).

The ratio h/(x^2 y) may be interpreted by continuity when needed at the axes. The displayed inequality itself implies the axis derivative bound

|h_y(x,0)| <= epsilon x^2 W(|x|),

by dividing by |y| and taking y to zero. The strain bound proved in ../function_spaces/PROOF.md is

|c[h]| <= K epsilon,
K=L^2/(1-k) [1/36+sqrt(3)/(8pi)].

We now prove the global axis velocity estimate

|U_1[h](x,0)| <= B epsilon |x|,
B=3L^2/[4(1-k)].

This estimate does not control the full-plane velocity or its derivatives in the same norm.

## Axis kernel and its angular integral

Take x>0. The first component has no local delta term; the second component's local term also vanishes on this axis. Start from the truncated kernel integral on disks centered at the origin, with the small local singularity removed symmetrically. For Y=(a,b) with a,b>0, the product K_1((x,0)-Y)h(Y) is (x-a)b h(a,b)/(pi[(x-a)^2+b^2]^2). Reflection in y gives the same product, since both K_1 and h change sign. Reflection in x gives (x+a)b h(a,b)/(pi[(x+a)^2+b^2]^2), and its y reflection again gives the same product. Including the polar Jacobian r yields the first velocity component

U_1[h](x,0)=(2/pi) integral_0^infty integral_0^{pi/2}
r^2 sin(theta) h(r,theta)
[(x-r cos(theta))/D_-^2+(x+r cos(theta))/D_+^2] dtheta dr,

where D_+-=x^2+r^2 +-2xr cos(theta). The paired rational bracket is O(x/r^4) for fixed x as r tends to infinity. Since h=O(r^k), the full radial integrand is O(r^{k-2}), hence absolutely integrable there. The subtraction K_1(-Y) used to define a convergent canonical kernel has zero integral on every annulus: K_1(-Y)h(Y) is odd in the first coordinate. Thus the symmetric-annular definition agrees with the paired limit, without integration by parts or an unaccounted boundary term. Near Y=(x,0), C^1 regularity and h(x,0)=0 give |h(Y)|<=C|Y-(x,0)|, which makes the local |Z|^{-2} kernel integrable in two dimensions. These observations justify pairing and removing both cutoffs.

Write h=r^3 cos^2(theta)sin(theta)W(r) e(r,theta), with |e|<=epsilon. Use q=1-(1+(r/L)^2)^{-(1-k)/2}, so W(r)dr=L^2 dq/[(1-k)r]. Let beta=r^2/(r^2+x^2). Direct rational simplification yields

U_1[h](x,0)=4xL^2/[pi(1-k)] integral_0^1 integral_0^{pi/2} e(q,theta) Q(beta,theta) dtheta dq,

Q=cos^2(theta)sin^2(theta) beta^2
[1-4beta^2 cos^2(theta)]/[1-4beta(1-beta)cos^2(theta)]^2.

For 0<=beta<=1 set delta=|1-2beta| and D=sin^2(theta)+delta^2 cos^2(theta). The numerator identity is

1-4beta^2 cos^2(theta)=D+4beta(1-2beta)cos^2(theta).

For delta>0, the triangle inequality gives

integral |Q| dtheta <= beta^2 J_0(delta)+4beta^3 delta J_1(delta),

J_0=integral cos^2(theta)sin^2(theta)/D dtheta=pi/[4(1+delta)^2],
J_1=integral cos^4(theta)sin^2(theta)/D^2 dtheta=pi/[4delta(1+delta)^3].

To verify the two integral evaluations, substitute t=tan(theta) and start from

integral_0^infty t^2/[(t^2+a^2)(t^2+b^2)] dt=pi/[2(a+b)],  a,b>0.

This identity follows by partial fractions and the elementary arctangent integral. Differentiate once in a, and then in b, under the integrable positive rational kernels, and set a=1,b=delta. This gives exactly J_0 and J_1. Since beta/(1+delta)<=1/2, the bound is at most pi/16+pi/8=3pi/16. At beta=1/2 the original Q reduces to cos^2(theta)/4 away from theta=0, so the same bound holds directly. The cases beta=0,1 follow by direct evaluation or continuity of the bound.

Integration in q proves |U_1[h](x,0)|<=3epsilon xL^2/[4(1-k)]. Parity gives the negative axis and the value at zero.

## Unique positive-axis source for an exact solution

Let rho be an exact normalized canonical P_2 solution with c_l>1/2 and g(x)=rho_y(x,0)>0 for all x>0. Here P_2 includes rho in C^{2,alpha}_loc, the center factorization with a(0)=1, the PDE and parity, and the canonical condition U(X)=o(|X|). The regularity of the canonical Poisson inverse gives U in C^{2,alpha}_loc, so g and w below are C^1 on (0,infinity). Set w(x)=c_l x+U_1(x,0) and A=2c_l-1>0. Differentiate V dot grad(rho)=rho in y on y=0, where rho, rho_x and V_2 vanish, to get w g'+V_{2,y}g=g. Since V=c_l X+U and div(U)=0, w'+V_{2,y}=2c_l. These give

w g'+(2c_l-w'-1)g=0,
(w/g)'=A/g>0.

No division by w is used. For completeness, write U(X)=DU(0)X+o(r). The parity and incompressibility give DU(0)=diag(-c,c). Rescale rho(RX)/R^3 to x^2y and pass to the stationary equation in distributions on a compact set. The limiting linear transport identity is (3c_l-c)x^2y=x^2y, hence c=3c_l-1. This passage uses uniform convergence of the continuous factor and C^1 convergence of U(RX)/R; derivatives of the factor are not assumed. It follows that w(x)=-Ax+o(x), so w is negative for small positive x. Canonical sublinearity gives w(x)/x -> c_l>0 at infinity. The intermediate value theorem supplies a positive root. Strict monotonicity of w/g makes it unique. At the root x_*, g(x_*)>0 forces w'(x_*)=A and V_{2,y}(x_*,0)=1. Parity makes the off-diagonal entries of DV on the axis zero. The equilibrium is therefore a source with eigenvalues A and 1.

This statement excludes additional equilibria on the positive x-axis only. It says nothing about equilibria away from the axes.

## Application to a nontrivial X3 neighborhood

Let bar-rho be the exact dyadic-input X3 density, and let rho=bar-rho+h be an exact normalized P_2 solution satisfying the weighted factor bound with epsilon<=1/100 and the same L,k in W. The background axis derivative is

bar-g(x)=x^2 W(x) exp(S(q,0)).

The degree-7 B-spline basis is nonnegative and sums to one on [0,1]. Thus each b_m is between its minimum and maximum coefficients, including its first zero coefficient. On the axis cos(2m theta)=1 and 0<=chi^{max(m-1,0)}<=1. Therefore S(q,0)>=-Csum, Csum=sum_m max_i |coefficient_{i,m}|. The singular term contains sin^2(theta), so it vanishes identically on this axis. The independent interval check in evidence/constants.json gives

exp(-Csum)>0.0135,  K<7,

and the audited scalar strain satisfies bar-c>15. The scalar evidence is ../canonical_inverse/evidence/strain_arb_20_32_result.json, SHA256 16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db; its independent audit verdict is recorded in ../canonical_inverse/evidence/audit_verdict.json. Here bar-c=psi[bar-rho]_{xy}(0) whereas c[h]=psi[h]_{xy}(0)/3 perturbs the scaling parameter. Consequently

g(x)>0.0035 x^2 W(x)>0,
c_l=(1+bar-c)/3+c[h] > 16/3-7/100 >1.

Every such exact solution has exactly one positive-axis source, by the preceding theorem. This is a conditional geometric conclusion on the weighted factor ball of radius 0.01. It is not a claim of existence in that ball.

For source localization, let bar-c_l=(1+bar-c)/3 and bar-w(x)=bar-c_l x+bar-U_1(x,0). Then

|w(x)-bar-w(x)| <= (B+K) epsilon |x|.

Thus any certified numbers 0<a<b satisfying

bar-w(a)+(B+K)epsilon a<0,
bar-w(b)-(B+K)epsilon b>0

place the exact solution's unique source in (a,b). The required bar-w point enclosures are not yet supplied by this lemma. Floating trial roots cannot be substituted for them.

## Dependencies and scope

The proof uses the canonical kernel, the exact strain functional, the independently proved normalization and axis identities, elementary rational integrals, and the scalar/input certificates cited above. It supplies explicit operator constants for an axis trace and a conditional global uniqueness theorem. It supplies neither a full linear inverse nor a nonlinear closing estimate.
