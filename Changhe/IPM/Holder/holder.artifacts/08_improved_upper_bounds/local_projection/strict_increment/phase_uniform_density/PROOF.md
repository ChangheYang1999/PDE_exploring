# A phase-uniform reflection density stronger than the radial minimum

## Statement and scope

Use the real or complex scalar homogeneous Holder seminorm of the setup proof. Let mu_R=Q_R+(1/2-1/pi)delta_0 be the positive local measure of ../../PROOF.md, with mass 1/2. Its two negative-axis lobes contain disks of radius aR centered at plus and minus cR on that axis, where a+c=1 and 0<a<=c/2. The accepted disk-containment theorem supplies c=c_* or any rational c>=c_* below 3/4. No new containment assertion is required.

Let h be the distance between the two output points, s=R/h, and assume 2as<1. Define, for integer n>=1,

    I_n(c)=integral_0^a x^(2n) sqrt(a^2-x^2)/(c^2+2cx+a^2) dx,
    H_n(alpha,s,c)=2^(2n+2)/pi * (-binom(alpha,2n)) s^(2n) I_n(c).

Every H_n is positive for 0<alpha<1. For every integer N>=1 and every orientation of the kernel axis relative to the output increment,

    |mu_R*f(x)-mu_R*f(y)|
       <= [1/2-sum_(n=1)^N H_n(alpha,s,c)] h^alpha [f]_alpha.    (1)

The infinite positive sum is also valid. These are costs of a specified reflection coupling, not optimal transport costs. They improve the radial-minimum moment savings for the same disks, term by term.

For the retained-cutoff version, R/h=rho<1/2, replace I_n(c) by

    I_n^rho(c)=I_n(c)-rho^2/(1-rho)^2 * integral_0^a x^(2n)sqrt(a^2-x^2) dx.  (2)

The resulting H_n^rho may be subtracted from the original translation-cost cutoff upper bound J_D. No previously subtracted reflection saving may be subtracted again.

## The local density and its two derivatives

Scale R=1 and take the positive disk center c e, where e is its negative kernel axis. At u of length r<=a and v=(u.e)/r, the density of Q_R, multiplied by 2pi, is

    q_r(v)=[c^2+2crv+r^2(2v^2-1)]/[c^2+2crv+r^2]^2.

The atom lies outside the two disks. Direct differentiation gives

    q_r'(v)=2r[-c^3+3cr^2+2r^3v]/[c^2+2crv+r^2]^3,
    q_r''(v)=4r^2[3c^4-8c^2r^2-4cr^3v+r^4]/[c^2+2crv+r^2]^4.

For 0<=r<=c/2 and -1<=v<=1 the first derivative is nonpositive: its bracket is at most c^3[-1+3/4+1/4]=0. The second is nonnegative: writing t=r/c<=1/2, its bracket divided by c^4 is at least 3-8t^2-4t^3+t^4>=3-2-1/2=1/2. Thus q_r is decreasing and convex on [-1,1]. The denominators are positive since r<c.

## Reflection coupling for an arbitrary direction

Let hhat be the direction of the output increment and write u=r(cos(theta) hhat+sin(theta) hhat_perp). Reflection F in the line perpendicular to hhat replaces cos(theta) by -cos(theta), preserving r. Let gamma be the angle between e and hhat. The smaller of the densities at u and Fu is

    min(q_r(v(u)),q_r(v(Fu)))
      =q_r(|cos(gamma)cos(theta)|+sin(gamma)sin(theta)).         (3)

Use this smaller density on the disk for the reflection coupling; it is invariant under F and is a submeasure of Q_R. Couple the rest by translation. This preserves both marginals. The average distance factor of a reflected pair is

    [(1+2sr cos(theta))^alpha+(1-2sr cos(theta))^alpha]/2.

Both bases are positive by 2as<1. The saving is the positive even series

    sum_(n>=1)(-binom(alpha,2n))(2sr cos(theta))^(2n).

For each n its angular weight is even under theta -> -theta. Pair these two angles in (3). Convexity of q_r gives

    [q_r(A+B)+q_r(A-B)]/2 >= q_r(A) >= q_r(|cos(theta)|),
    A=|cos(gamma)cos(theta)|, B=sin(gamma)sin(theta).

Here A+B and A-B belong to [-1,1], since each is a scalar product of unit vectors. The last inequality uses A<=|cos(theta)| and the decreasing property. Consequently the moment saving at every orientation is at least its value when the negative axis is parallel to hhat. The opposite disk has the same estimate by central symmetry. This establishes a uniform bound without discarding all angular variation of the density.

## Exact one-dimensional moments

In the parallel orientation, write u=(x,y), with x in the hhat direction. The reflected subdensity, multiplied by 2pi, is

    [(c+|x|)^2-y^2]/[(c+|x|)^2+y^2]^2.

On the first quadrant, integration in y from zero to sqrt(a^2-x^2) is exact, because this density is the y derivative of y/[(c+x)^2+y^2]. The result is

    sqrt(a^2-x^2)/(c^2+2cx+a^2).

There are four quadrants and two disks, and the density normalization is 1/(2pi). Multiplying by the nth even distance term gives exactly H_n above. Positivity permits termwise integration by monotone convergence; uniform convergence also follows from 2as<1. The original radial minimum q_r(1)=1/(c+r)^2 is at most q_r(|cos(theta)|), and is strictly smaller on a set of positive area. Therefore every H_n strictly exceeds the corresponding radial-minimum saving for the same c,a,s and exponent.

## Retained cutoff density

In the accepted cutoff construction, the density removed from each disk is bounded by the constant 1/[2pi(1-rho)^2]. After scaling by R=rho, the normalized bound is kappa=rho^2/(1-rho)^2<1. Since q_r(v)>=q_r(1)=1/(c+r)^2>=1, both original and reflected densities retain at least q_r(v)-kappa>0. Subtracting a constant preserves the decreasing and convex properties. The same argument therefore applies, and integration of that constant over the first quadrant gives exactly (2).

## A simple explicit lower bound for the quadratic moment

Put A=c^2+a^2 and B=2c. The convexity of x -> 1/(A+Bx), with probability weight proportional to x^2 sqrt(a^2-x^2), gives

    I_1(c) >= [pi a^4/16]/[c^2+a^2+64ca/(15pi)].              (4)

Indeed the total weight is pi a^4/16 and its mean x is 32a/(15pi), since integral_0^a x^3 sqrt(a^2-x^2) dx=2a^5/15. Thus the quadratic term alone permits the explicit saving

    alpha(1-alpha)s^2 * a^4/[2(c^2+a^2+64ca/(15pi))].         (5)

For the retained-cutoff case subtract alpha(1-alpha)s^2*kappa*a^4/2 from (5). The exact positive integrals I_n allow further directed evaluation, but no numerical operator bound is asserted here before a separate acceptance record.

## Status and dependencies

Written before numerical evaluation. The independent lead cross-read is saved in verification/lead_note60.md; the acceptance status is recorded in verification/accepted.json. Dependencies are the accepted positive-measure decomposition, disk containment, reflection coupling, even binomial series, and retained-density bound. This note changes only finite local submeasures; it leaves all principal values, behavior at infinity, and the diagonal identity term unchanged.
