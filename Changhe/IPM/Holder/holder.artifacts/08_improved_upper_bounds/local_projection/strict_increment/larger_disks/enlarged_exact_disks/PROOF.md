# A slightly larger pair of disks for the exact radial coupling

## Statement

Use the real or complex homogeneous Euclidean Holder seminorm [f]_alpha on R^2, 0<alpha<1, the principal-value kernels and quotient extension of ../../../../../01_setup/PROOF.md, and the positive local measure mu_R=Q_R+(1/2-1/pi)delta_0 from ../../../PROOF.md. Fix the exact rational constants

    c=1487/2000, a=1-c=513/2000, d=3/4-c=13/2000.

The two disks B(cRn,aR) and B(-cRn,aR), where n is the negative kernel axis, lie in the support of Q_R. Their exact largest radial minorant about either center is

    w_c(r)=1/[2pi R^2(c+r/R)^2], 0<=r<=aR.

Define positive moments

    J_c=2 integral_0^a t^3/(c+t)^2 dt,
    K_c=(1/2) integral_0^a t^5/(c+t)^2 dt.

For h=|x-y|>0, R=s h and 0<s<1/(2a), the reflection argument gives

    |mu_R*f(x)-mu_R*f(y)|
      <= [1/2-alpha(1-alpha)J_c s^2
          -alpha(1-alpha)(2-alpha)(3-alpha)K_c s^4]
         h^alpha [f]_alpha.                               (1)

In particular s=1/2 is admissible. This statement does not automatically improve the optimized global G at every exponent, since its radius s_D might exceed 1/(2a). The previously accepted disks continue to supply that global strict improvement.

For any 0<rho<1/2, the retained-cutoff plan also gives

    D_alpha <= J_D(alpha,rho)
       -p[J_c rho^2-a^4 rho^4/(2(1-rho)^2)]
       -q[K_c rho^4-a^6 rho^6/(12(1-rho)^2)],              (2)
    p=alpha(1-alpha), q=p(2-alpha)(3-alpha).

The sharper-deficiency version of J_D may replace the original J_D after independent acceptance, since it retains the same flows. Both square brackets are positive. The proof concerns these fixed disks, not the globally optimal inscribed disks or transport coupling.

## Containment by an explicit quadratic lower bound

Scale R=1 and orient n horizontally. The outer containment is immediate from c+a=1. Write s0=sin(theta), with 0<=theta<=pi/4, for a point of the inner lobe boundary r=sin(2theta). The squared distance from that boundary point to (c,0), minus a^2, is

    P_c(s0)=2c-1-4c s0+4s0^2+4c s0^3-4s0^4.

Set tau=s0-1/3. Since 0<=s0<=1/sqrt(2)<3/4, one has -1/3<=tau<=5/12. At c=3/4 the exact identity and concavity bound in ../PROOF.md give

    P_(3/4)=1/162+(2/27)tau
                 +tau^2(13/3-(7/3)tau-4tau^2)
             >=1/162+(2/27)tau+(8/3)tau^2.

The dependence on c is affine. Its derivative is

    2-4s0+4s0^3=22/27-(8/3)tau+4tau^2+4tau^3.

Because tau<=5/12, the last two terms are at most (17/3)tau^2. Thus

    P_c(s0)>=A+B tau+C tau^2,
    A=1/162-22d/27,
    B=2/27+8d/3,
    C=8/3-17d/3.

For d=13/2000, C>0 and 4AC-B^2>0, as can be checked by exact rational arithmetic. Therefore the quadratic is strictly positive on the entire real line. This proves that the proposed disk does not meet the inner boundary. Moreover a/c<1/sqrt(2), so the disk stays between the two boundary rays. Its center lies inside the lobe and the disk is connected, hence the disk lies in the lobe support. The second disk follows by central symmetry.

## Radial density and costs

Here a<c/2. The exact density calculation of ../exact_radial_density/PROOF.md, with arbitrary c and 0<=t<=a, has derivative

    d g_t(v)/dv = 2t[-c^3+3ct^2+2t^3 v]/[c^2+2ctv+t^2]^3 <=0,
    -1<=v<=1.

Its minimum is g_t(1)=1/(c+t)^2. Equality at the outward point proves the stated radial-minorant claim. The reflection displacement satisfies |2u_parallel/h|<=2as<1. Applying the accepted even quadratic and quartic concavity estimate and integrating its moments gives (1).

All moments can be evaluated by the exact identity, valid because c+a=1,

    B_n(c)=integral_0^a t^n/(c+t)^2 dt
      =(-c)^n(1/c-1)+n(-c)^(n-1)log(1/c)
       +sum_(j=2)^n binom(n,j)(-c)^(n-j)(1-c^(j-1))/(j-1),
    J_c=2B_3(c), K_c=B_5(c)/2.

No approximate geometric containment is used. These formulas and positive defining integrals avoid a numerical cancellation argument for positivity.

## Retained edges

On either disk, w_c>=1/(2pi rho^2)>H=1/[2pi(1-rho)^2] for rho<1/2. The accepted flow-deletion argument therefore retains the positive radial density w_c-H. The removed constant-density moments are

    4pi H integral_0^(a rho) r^3 dr=a^4 rho^4/[2(1-rho)^2],
    pi H integral_0^(a rho) r^5 dr=a^6 rho^6/[12(1-rho)^2].

Reflection replaces only these retained translation edges. The residual and all other costs are unchanged. Positivity of w_c-H proves positivity of the bracketed moments in (2). All the modified measures are finite; the accepted principal-value and infinity arguments are unaffected.

## Status

Written before numerical evaluation. OPEN pending exact rational checks and independent lead review. Numerical gains must be certified against the original adverse upper endpoints, not subtracted again from endpoints already improved by another reflection coupling.
