# Strict projection savings at a general local radius

## Statement

Use the real or complex homogeneous Euclidean Holder seminorm with 0<alpha<1 and the operators modulo constants from ../../../../../01_setup/PROOF.md. Define

    a_n(alpha) = (n/pi) integral_0^(pi/(2n)) sin(nt)(2 sin t)^alpha dt,  n=1,2,3,
    A_alpha = Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)),
    b_alpha = min{(a_3(alpha)+a_1(alpha))/2, 2^(alpha+1)/(3pi)},
    B_alpha = 2a_3(alpha)/(1-alpha) + b_alpha,
    s_D = (1-alpha) B_alpha/(2 A_alpha).

For 0<s<2 put

    eta_alpha(s) = (7 s^2/4608) alpha(1-alpha)(1+s/2)^(alpha-2).

Subject to the independent cross-read of the larger-disk lemma in ../PROOF.md, the proposed all-exponent estimate is

    D_alpha <= inf_(0<s<2) [2 A_alpha s^alpha/alpha + B_alpha s^(alpha-1) + 1/2 - eta_alpha(s)].

In particular 0<s_D<2 and

    D_alpha <= 2 A_alpha s_D^alpha/[alpha(1-alpha)] + 1/2 - eta_alpha(s_D).

Thus the previously proved optimized local projection bound has an explicit strictly positive improvement at every exponent. Setting s=1/2 gives the saving eta_star(alpha) from the parent proof. No numerical endpoint is asserted here.

## Scaling the disk coupling

Fix an increment of length h and choose R=sh. The larger-disk lemma is geometric in units of R: in each negative kernel lobe it inscribes a disk of radius R/4 centered at distance 3R/4 from the origin. Their density lower bound is

    c_R = 7/(18 pi R^2).

Remove c_R times area on each disk from the positive remainder Q_R. Reflect the uniform mass about the line through each disk center perpendicular to the increment direction. If u denotes the displacement from that center, the two evaluation arguments are separated by (h-2u_parallel)e, where e is the increment direction. Since |2u_parallel|<=R/2=sh/2<h, the distance is positive.

After division by h, the normalized transport distances lie in [1-s/2,1+s/2]. The concavity estimate used in the parent proof therefore gives a total saving, after division by h^alpha, of

    c_R pi (R/4)^4 h^(-2) alpha(1-alpha)(1+s/2)^(alpha-2)
      = eta_alpha(s).

The positive remainder and identity atom have total mass 1/2, so their normalized increment cost is at most 1/2-eta_alpha(s). The paired local contributions cost at most 2A_alpha s^alpha/alpha, and the accepted derivative bound for the regular far part costs at most B_alpha s^(alpha-1). Their sum proves the first inequality. The kernels, local identity terms and convergence are those of the already proved local projection decomposition in ../../../PROOF.md and the angular derivative estimate in ../../../../../02_upper_bounds/PROOF.md.

## The old optimizing radius is admissible

The change of variable u=nt gives

    a_n(alpha) = (2^alpha/pi) integral_0^(pi/2) sin u sin(u/n)^alpha du.

Consequently a_3(alpha)<=a_1(alpha)=2^alpha A_alpha, and b_alpha<=a_1(alpha). It follows that

    s_D = a_3(alpha)/A_alpha + (1-alpha)b_alpha/(2A_alpha)
         <= 2^(alpha-1)(3-alpha) < 2.

For the last strict inequality, the function 2^(alpha-1)(3-alpha) is increasing on [0,1]: its logarithmic derivative is log 2-1/(3-alpha)>=log 2-1/2>0. Its value at alpha=1 is 2. Positivity of s_D follows from that of its defining integrals.

The first two terms of the old bound are minimized at s_D, and there their sum equals 2A_alpha s_D^alpha/[alpha(1-alpha)], as proved in the earlier local projection note. Substitution gives the second displayed inequality. The gain is strictly positive for every 0<alpha<1. This result is conditional until its analytic cross-read is recorded.
