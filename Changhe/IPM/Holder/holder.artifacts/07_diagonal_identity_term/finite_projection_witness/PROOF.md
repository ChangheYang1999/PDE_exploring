# An explicit finite-exponent projection witness

## Statement and spaces

Use the real homogeneous Hölder space, compact-test equivalence, and operator normalization of `../../01_setup/PROOF.md`. Let 0<alpha<=1/4, 0<a<=1, and 0<rho<=a/6. Put x=(1/2,0), y=-x. Define the graph

$$\Gamma_a=\{(b_a(Y),Y):Y\in\mathbb R\},\qquad
b_a(Y)=\frac12+\frac{(|Y|-a)_+}{\sqrt3}.$$

Let s_a be signed distance to this graph, positive on its right, and let V=(s_a,Y), Pi=2|s_a Y|/|V|, with Pi=0 at V=0. On X>0 put

$$F=-\frac12+\frac12\min(|V|,\rho)^\alpha
+\frac12\operatorname{sgn}(s_aY)\Pi^\alpha,\qquad
h=\frac12(2X)^\alpha,$$

and f=max(-h,min(h,F)). Extend f centrally oddly and give it value zero on X=0. Then

$$[f]_\alpha\le 1+2\alpha^2,\qquad f(x)=-1/2,\quad f(y)=1/2.$$

Consequently

$$D_\alpha\ge\frac{J_\alpha(a,\rho)+1/2}{1+2\alpha^2},$$

where J is the absolutely convergent integral specified below. The sharper constant K_alpha proved in `../refined_profile_constant/PROOF.md` may replace the denominator 1+2alpha^2. This is a rigorous lower-bound family, not a claim of optimality. Its numerical evaluation requires a separate enclosure.

## Global regularity with an explicit constant

The local-profile theorem in `../local_projection_profile/PROOF.md` gives [g_alpha]<=1+2 alpha^2. The frozen planar profile is the minimum of g_alpha and rho^alpha/2+sign(S)|S|^alpha/2, S=2u1u2/|u|. The latter has seminorm at most one, so freezing preserves the stated bound.

The outer curved profile has seminorm at most one for alpha<=2/3, exactly as in `../projection_assembly/PROOF.md`: S composed with V is 2sqrt(2)-Lipschitz, and Pi<=2dist(.,Gamma_a union {Y=0}). Equal-sign pairs use (2sqrt(2))^alpha/2<=1; opposite-sign pairs use the intervening zero set and concavity.

For |z-x|<sqrt(3)a/2, the nearest graph point lies on its vertical segment and V(z)=z-x. Indeed an oblique upper-ray projection can lie beyond its endpoint only if Y+(X-1/2)/sqrt(3)>a; the lower ray has the reflected condition. Neither can hold in that ball, by Cauchy-Schwarz. The endpoint itself is farther than the vertical projection when |Y|<a. Thus the entire ball B(x,5rho) has the planar bound, since 5a/6<sqrt(3)a/2.

If |V(p)|<=rho, then |Y_p|<=rho and a nearest graph point has ordinate of absolute value at most 2rho<a. It lies on the vertical segment. Therefore |p-x|=|V(p)|<=rho. For a mixed pair with this p and R=|q-x|>=5rho, the argument of the general assembly proof gives, in the only adverse ordering,

$$\frac{F(q)-F(p)}{|p-q|^\alpha}
\le\frac12\left[\left(\frac\rho{R-\rho}\right)^\alpha
+\left(\frac{2R}{R-\rho}\right)^\alpha\right]
\le\frac12\left(4^{-\alpha}+(5/2)^\alpha\right)\le1.$$

The last function is convex in alpha, equals one at zero, and is below one at 1/4: 4^(-1/4)<5/7 and (5/2)^(1/4)<9/7. The other ordering follows directly from F<=H and F(q)=H(q), where H is the outer profile. These cases cover every pair in the right half-plane. Clamping to [-h,h] and the central odd extension preserve the larger Hölder bound, as proved in the general assembly argument.

## A nonnegative amplitude for the odd part

Let Q be the open first quadrant. For (X,Y) in Q set

$$P=\Pi^\alpha,\qquad H=(2X)^\alpha,\qquad B=\min(|V|,\rho)^\alpha,$$

$$M=\max\left(0,\min\left(P,H,\frac{P+H+B-1}{2}\right)\right).$$

Then

$$f(X,Y)-f(X,-Y)=\operatorname{sgn}(s_a(X,Y))M(X,Y).$$

To check this identity, write the two unclamped values as -A+d and -A-d, where A=(1-B)/2>=0, d=P/2, and first take s_a>0. The difference of their clamps to [-H/2,H/2] is max(0,min(2d,H,d+H/2-A)). The case s_a<0 reverses the sign. Continuity includes s_a=0.

Put

$$\nu(X,Y)=\frac{(X-1/2)Y}{\pi((X-1/2)^2+Y^2)^2}
-\frac{(X+1/2)Y}{\pi((X+1/2)^2+Y^2)^2}.$$

Central oddness and reflection in Y give the exact expression

$$J_\alpha(a,\rho)=2\int_Q\nu(X,Y)\operatorname{sgn}(s_a(X,Y))M(X,Y)\,dX\,dY.$$

At the pole x, M=O(|z-x|^alpha), so the local integral is absolutely convergent. At infinity use |f|<=(2|z|)^alpha/2 and nu=O(|z|^(-3)). The identity term in the unit increment of T_xy-I/2 is exactly 1/2. Rotation transfers its norm to D_alpha, proving the lower bound.

## Explicit local and exterior errors for certification

Choose 0<delta<=min(rho,1/4). In the upper half of B(x,delta), V=z-x, Pi=r|sin(2theta)|, and B=r^alpha. The cap H does not reduce P, since r<=delta<1-2delta. The third argument of the minimum gives

$$M\ge P-\frac{\alpha r}{1-2\delta}.$$

Here use P<=r^alpha and (1-(2X)^alpha)_+<=2alpha r/(1-2delta). The own-pole kernel has the sign of s_a. Its exact leading integral, including the factor two, is 2A_alpha delta^alpha/alpha, with A_alpha as in the local-projection theorem. Its possible loss is at most 2alpha delta/(pi(1-2delta)). The other-pole kernel has absolute value at most (1+delta)r/[pi(1-delta)^4], and M<=r^alpha. Hence

$$J_{\rm local}\ge\frac{2A_\alpha\delta^\alpha}{\alpha}
-\frac{2\alpha\delta}{\pi(1-2\delta)}
-\frac{2(1+\delta)\delta^{\alpha+3}}{(1-\delta)^4(\alpha+3)}.$$

For a cutoff R>1 in distance from x on Q, the centrally reflected omitted region is contained in {|z|>L}, L=R-1/2. Since

$$|G(z)|\le\frac{|z|}{\pi(|z|^2-1/4)^2},$$

its absolute contribution is at most

$$E_{\rm tail}=\frac{2^\alpha L^{\alpha-1}}{(1-\alpha)(1-1/(4L^2))^2}.$$

The remaining compact integral uses z=x+r exp(i theta), delta<=r<=R, 0<=theta<=theta_max(r), with theta_max=pi for r<=1/2 and theta_max=acos(-1/(2r)) otherwise. The Jacobian is r dr dtheta. After r=exp(u), it is r^2 theta_max du dt, 0<=t<=1. Enclosing this compact integral by interval quadrature, adding the local lower bound, subtracting E_tail and adding 1/2, then dividing by 1+2alpha^2 gives a fully explicit certified lower bound for D_alpha.
