# Full even-moment saving for the radial reflection coupling

## Statement and exact scope

Fix0<alpha<1. Use the Euclidean homogeneous Holder seminorm on real or complex scalar functions on R^2. The circular principal-value kernels, the increment extension modulo constants, and the diagonal identity R_1^2=T_xx-I/2 are those of ../../../../01_setup/PROOF.md. The positive local measure is the finite measure mu_R=Q_R+(1/2-1/pi)delta_0 of ../../PROOF.md, of total mass1/2. Its kernel phase may be arbitrary.

Let c,a be positive constants with c+a=1. Assume that the two disks of radius aR centered at the two negative-axis points of radius cR lie in the support of Q_R, that a<=c/2, and that on each disk the radial density about its center

    w_c(r)=1/[2pi R^2(c+r/R)^2], 0<=r<=aR,

is bounded above by the Q_R density. These hypotheses are proved for c=3/4,a=1/4 by V195,V206. The proposed pair c=1487/2000,a=513/2000 may also be used if its independent containment audit is accepted. No numerical computation of containment is assumed here.

For h=|x-y|>0, set s=R/h and assume0<2as<1. Write

    B_m(c)=integral_0^a t^m/(c+t)^2 dt,
    A_n(alpha)=2alpha product_(k=1)^(2n-1)(k-alpha)/(n!)^2,
    g_n(alpha,s,c)=A_n(alpha) s^(2n) B_(2n+1)(c).

All these quantities are positive. Then

    |mu_R*f(x)-mu_R*f(y)|
        <= [1/2-sum_(n>=1)g_n(alpha,s,c)] h^alpha [f]_alpha.       (1)

Every finite partial sum may replace the infinite sum in(1). For N>=1, if q=(2as)^2<1, its omitted tail obeys

    0<=sum_(n>N)g_n <= g_(N+1)/(1-q).                            (2)

The same bound holds for N=0 with the evident interpretation. These statements concern one explicit coupling, not the optimal transport cost of the two measures.

For the perturbed cutoff plan of the accepted J_D(alpha,rho), with0<rho<1/2, put

    B_m^rho(c)=B_m(c)-rho^2 a^(m+1)/[(m+1)(1-rho)^2].

Each B_m^rho is positive. Let g_n^rho=A_n(alpha)rho^(2n)B_(2n+1)^rho(c). Then

    D_alpha <= J_D(alpha,rho)-sum_(n>=1)g_n^rho.                  (3)

Every finite partial sum is valid, and the same tail estimate holds with s=rho. The independently accepted sharper-deficiency J_D may replace J_D, because its retained projection flows are identical. Subtract this saving only from the original translation-cost base, never from an upper endpoint from which a reflection saving has already been removed.

## Reflection identity and its convergent expansion

The radial submeasure on a disk is invariant under reflection of the coordinate parallel to x-y about the disk center. Couple this submeasure at x to the reflected submeasure at y, and use the original translation coupling on the rest of mu_R. The two marginals remain unchanged. If u is displacement from the disk center and u_parallel is its component parallel to x-y, the reflected distance divided by h is |1+2u_parallel/h|. Its reflection partner has distance |1-2u_parallel/h|. Our assumption gives |2u_parallel/h|<=2as<1, so both bases are positive.

For |v|<1 the binomial series is absolutely convergent. Since0<alpha<1, binom(alpha,2n)<0 for every n>=1. Hence

    1-[(1+v)^alpha+(1-v)^alpha]/2
       =sum_(n>=1)(-binom(alpha,2n))v^(2n),                     (4)
    -binom(alpha,2n)
       =alpha product_(k=1)^(2n-1)(k-alpha)/(2n)! >0.

All terms in(4) are nonnegative. They may therefore be integrated term by term, either by monotone convergence or by uniform absolute convergence on |v|<=2as. There is no sign cancellation or unbounded-endpoint limit in this step.

## Moment normalization

There are two disks. On either disk use r=Rt and an angular coordinate theta measured from x-y. The density times area is t dt dtheta/[2pi(c+t)^2]. Also v=2st cos(theta), and

    integral_0^(2pi) cos(theta)^(2n) dtheta
       =2pi binom(2n,n)/4^n.

The saving contributed by the nth term, including both disks, is therefore

    2(-binom(alpha,2n))(2s)^(2n)
      binom(2n,n)B_(2n+1)(c)/4^n
      =A_n(alpha)s^(2n)B_(2n+1)(c)=g_n.

The original translation cost is mu_R(R^2)=1/2. The absolute increment inequality for each coupled pair proves(1), for complex as well as real scalar inputs. The first two terms are exactly

    g_1=alpha(1-alpha)[2B_3(c)]s^2,
    g_2=alpha(1-alpha)(2-alpha)(3-alpha)[B_5(c)/2]s^4.

Thus this formula reproduces the previously checked quadratic and quartic savings with no change in normalization. The sixth-order term is

    g_3=alpha(1-alpha)(2-alpha)(3-alpha)(4-alpha)(5-alpha)
          B_7(c)s^6/18.

## Tail bound

The positive defining integral gives B_(m+2)<=a^2B_m. Also

    A_(n+1)/A_n=(2n-alpha)(2n+1-alpha)/(n+1)^2<4.

Consequently g_(n+1)<=q g_n with q=(2as)^2<1. Summing a geometric majorant gives(2). The estimate concerns the numerical evaluation of this chosen coupling; it is not a bound on the difference from the optimal coupling.

## Retained cutoff density

In the cutoff proof, only retained translation edges may be replaced. The accepted flow-deletion bound retains at least w_c-H on each disk, with H=1/[2pi(1-rho)^2]. Because c+a=1,

    w_c>=1/(2pi rho^2)>H

for0<rho<1/2. After r=rho t, the corresponding radial weight becomes

    t[1/(c+t)^2-rho^2/(1-rho)^2]dt dtheta/(2pi).

It is strictly positive. Its mth radial moment is B_m^rho. The previous reflection and moment calculation therefore gives(3), without modifying any residual mass or any cost outside these retained edges. The inequality B_(m+2)^rho<=a^2B_m^rho follows from the same positive weight, so its series has the same geometric tail bound.

## Exact evaluation and dependencies

For integer m>=2 the moments have the exact finite formula

    B_m(c)=(-c)^m(1/c-1)+m(-c)^(m-1)log(1/c)
        +sum_(j=2)^m binom(m,j)(-c)^(m-j)(1-c^(j-1))/(j-1).

This follows from u=c+t and the binomial theorem; c+a=1 fixes the upper endpoint at1. It permits rational interval evaluation of every finite sum whenever c,alpha,s are rational and log(1/c) is enclosed. Positivity is established by the integral, not by cancellation-prone floating evaluation.

The only analytic dependencies are the positive-measure decomposition and reflection construction, the accepted disk containment and radial minorant, and the retained-edge estimate for the cutoff version. Principal values and convergence at infinity are unchanged because the modification acts on finite local submeasures.

Status at creation: OPEN pending independent lead cross-read. The proof was written before any higher-moment numerical evaluation. No new decimal operator bound is accepted by this file alone.
