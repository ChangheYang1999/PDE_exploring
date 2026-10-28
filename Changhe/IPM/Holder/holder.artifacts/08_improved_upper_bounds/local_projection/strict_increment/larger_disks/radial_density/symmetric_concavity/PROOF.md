# Symmetric concavity improves the reflection saving

## Statement and exact scope

Let 0<alpha<1. On real or complex functions on R^2 use

    [f]_alpha = sup_(x!=y) |f(x)-f(y)|/|x-y|^alpha.

Let mu be a positive finite measure of mass M. Suppose it contains two radial area submeasures, each with density w(|u|)>=0 on a disk centered at c_+ or c_-, of common radius R/4. The disks are disjoint. Let |x-y|=h>0 and assume R=s h with 0<s<2. Put

    I_w = integral_0^(R/4) r^3 w(r) dr.

All moments are finite for the application below. The following measure inequality is valid:

    |int f(x-z) dmu(z)-int f(y-z) dmu(z)|
        <= [M-4 pi alpha(1-alpha) I_w/h^2] h^alpha [f]_alpha.       (1)

Convolution with an individual unbounded input can be normalized at one point if necessary; the integral of the difference is absolutely convergent whenever mu has compact support. Only this difference is asserted when absolute convolutions are not defined.

In the local diagonal projection decomposition, mu=mu_(R,beta) has mass 1/2, consisting of a positive compact remainder Q_(R,beta) of mass 1/pi and an origin atom of mass 1/2-1/pi. In the two disks of radius R/4 centered at distance 3R/4 on the negative kernel axis, the support and density comparisons in the parent proof give

    w(r) = [1-(32/9)t^2]/[2 pi R^2 (3/4+t)^2],  t=r/R,
    4 pi I_w = J R^2,
    J=653/288-(63/8)log(4/3)>7/4608.

Consequently (1) gives the stronger proposed increment bound

    |int [f(x-z)-f(y-z)] dmu_(s h,beta)(z)|
       <= [1/2-J s^2 alpha(1-alpha)] h^alpha [f]_alpha.           (2)

It is uniform in the kernel phase beta. In every unperturbed diagonal bound to which the parent radial-density result applies, its saving eta_rad(alpha,s) may therefore be replaced by

    eta_sym(alpha,s)=J s^2 alpha(1-alpha).

For the modified diagonal cutoff plan of ../cutoff_plan/PROOF.md, 0<rho<=1/3, the stronger saving is

    eta_cut_sym(alpha,rho)
       = alpha(1-alpha)[J rho^2-rho^4/(512(1-rho)^2)].             (3)

Thus the explicitly defined J_D(alpha,rho) in that proof obeys the proposed bound D_alpha<=J_D(alpha,rho)-eta_cut_sym(alpha,rho). Here D_alpha is the operator seminorm of R_1^2=T_xx-I/2, with kernel K_xx(z)=(z_1^2-z_2^2)/(2pi|z|^4), circular principal values, and the homogeneous Holder extension modulo constants. The definition and every term of J_D remain as in that dependency. For all 0<rho<1/2 the same change removes the factor (1+rho/2)^(alpha-2) from E(alpha,rho) in ../cutoff_plan/all_radii/PROOF.md.

The new scalar concavity argument is proved here. The application to Q and J_D also depends on the parent disk containment, density and surviving-edge proofs. These applications remain OPEN until all those dependencies and this proof receive an independent cross-read. No numerical bound is asserted.

## Proof of the symmetric scalar estimate

For 0<=v<1 define

    q(v)=[(1-v)^alpha+(1+v)^alpha]/2.

The function t -> t^(alpha-2) is convex on (0,infinity), since its second derivative is (alpha-2)(alpha-3)t^(alpha-4)>0. Therefore

    q''(v)=-alpha(1-alpha)[(1-v)^(alpha-2)+(1+v)^(alpha-2)]/2
           <= -alpha(1-alpha).

Using q(0)=1 and q'(0)=0, integration twice gives

    q(v)<=1-alpha(1-alpha)v^2/2.                                (4)

The same formula is valid for negative v by evenness, and at |v|=1 by continuity. The inequality is strict for 0<|v|<=1. It uses the average of the two opposite displacements, which removes the loss from bounding curvature at the largest displacement alone.

## Exact marginals and the moment calculation

Write e=(x-y)/h. For the radial submeasure centered at c, replace its translation pairing by the pairing between source coordinate z=c+u and target coordinate c+u-2(u dot e)e. The latter is the reflection of u in the line perpendicular to e, so it preserves the radial submeasure exactly. The evaluation difference is

    (x-c-u)-(y-c-u+2(u dot e)e)=(h-2u dot e)e.

Its length is h(1-2u dot e/h), positive because 2|u dot e|/h<=s/2<1. Pairing u with its reflection inside the cost integral and applying (4) bounds the new cost on this disk by

    h^alpha int [1-2alpha(1-alpha)(u dot e)^2/h^2] w(|u|)du.

For one disk, int (u dot e)^2 w(|u|)du=pi I_w. The two disks together therefore save at least 4pi alpha(1-alpha) h^(alpha-2) I_w. The rest of mu is coupled by translation at cost h^alpha per unit mass. Its positivity is preserved since only submeasures were removed. This proves (1). Applying the Holder inequality to the coupling proves it for complex inputs as well.

The parent radial integral is 4pi I_w=J R^2, giving (2). The surviving density for the cutoff plan is w-H, with H=1/[2pi(1-rho)^2] and R=rho at h=1. The removed constant-density moment is

    4pi H integral_0^(rho/4) r^3dr=rho^4/[512(1-rho)^2].

This gives (3), with its strict positivity inherited from J>7/4608 and rho/(1-rho)<=1/2. The positive-part version at larger radii uses the same reflection and the same estimate (4); only the radial moment changes. Every remaining transport edge, origin atom, singular-integral term and far-field estimate is unchanged. The strict improvement relative to the parent constants follows from (1+s/2)^(alpha-2)<1 for s>0.
