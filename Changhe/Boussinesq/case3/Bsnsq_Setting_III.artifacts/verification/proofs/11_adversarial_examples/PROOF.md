# Three counterexamples to insufficient verification criteria

Status: explicit smooth fields with complete arguments. None of the three examples is asserted to solve the full B2 system on the whole plane. Their purpose is to identify exactly which inferences fail.

## 1. A perfect core and an incorrect remote annulus

Fix any beta>0, a!=0, v in R, and R>0. Put

    c=1+beta/2, b=4a/beta,
    P(x,y)=cxy-(b/6)x^3+vx,
    Theta_*(x,y)=a x^2, Omega_*(x,y)=b x,
    U_*=(-cx, cy-(b/2)x^2+v).

The relative transport field of this polynomial is

    W_*=((beta-2)x/2, (1+3beta/2)y-(b/2)x^2).

Direct differentiation gives -Delta P=Omega_* and U_*=(-P_y,P_x). The temperature residual is

    a x^2 [2*(beta-2)/2-(beta-2)]=0,

and the vorticity residual is x[b*((beta-2)/2+1)-2a]=0. Thus the polynomial solves all differential profile equations exactly. Its velocity grows quadratically and is inadmissible under U=o(r).

Now define e(t)=exp(-1/t) for t>0 and e(t)=0 for t<=0, and

    chi(s)=e(4-s)/(e(4-s)+e(s-1)).

The denominator is positive for all real s. This is smooth, is one for s<=1, and is zero for s>=4. Set

    Psi_R(X)=chi(|X|^2/R^2) P(X),
    Theta_R(X)=chi(|X|^2/R^2) a x^2,
    U_R=(-Psi_R,y,Psi_R,x), Omega_R=-Delta Psi_R.

These are smooth compactly supported whole-plane fields with the required x parity, no added y parity, Theta_R(0,y)=0, and the exact center values a0=a, c=1+beta/2, b0=4a/beta, U_R(0)=(0,v). Each U_R is sublinear.

Moreover U_R is the ordinary full-plane Biot-Savart velocity of Omega_R. To verify this, convolve the fundamental solution with -Delta Psi_R and integrate by parts twice. The compact support removes boundary terms and the distributional fundamental-solution identity returns Psi_R, up to an irrelevant constant. Differentiation gives U_R. Equivalently, both velocities have the same div-curl data, and both decay at infinity, so their harmonic difference vanishes. There is no artificial elliptic boundary condition in this example.

Every original and desingularized transport residual vanishes exactly on |X|<R. The elliptic residual vanishes everywhere. All original fields vanish outside |X|>=2R, so only the transition annulus can contain a transport defect. The following point proves that the defect is nonzero rather than relying on a general nonexistence theorem.

Write C=chi(r^2/R^2), C'=chi'(r^2/R^2). At y=0, the exact temperature residual simplifies to

    R_Theta = a x^2 [2c C(1-C)+2 (x^2/R^2) C' (beta-c C)].

This follows from U_1=-c x C on y=0, Theta_x=2ax C+2ax^3 C'/R^2, Theta_y=0 there, and 2c=beta+2. As s decreases to 1 from above, C approaches 1 and C'/(1-C) tends to minus infinity. For beta!=2, beta-c C tends to the nonzero number (beta-2)/2, so the derivative term dominates and the bracket is nonzero near s=1. For beta=2, the bracket is 4(1-C)(C+s C'), which is positive sufficiently near s=1. An explicit computation at s=5/2 gives C=1/2, C'=-2/9 and

    bracket = 19c/18 - 10 beta/9 = 19/18 - 7 beta/12,

which is nonzero except beta=38/21. For that exceptional beta, the near-s=1 argument still applies. Consequently this compact field is not a stationary profile.

As R tends to infinity, the family agrees exactly with the inadmissible polynomial on every fixed compact set. Its local residuals and local center normalization therefore converge perfectly while its limiting velocity fails U=o(r). There is no uniform far-field admissibility estimate. This example refutes the sufficiency of core residuals, even when combined with exact center matching and a correct whole-plane inverse. It does not refute the prompt's requirement to check the actual far-field continuation and its residual.

The script code_independent/test_cutoff_trap.py samples the core, annulus, exterior, both signs of y, and both coordinate axes, at three R and three finite-difference steps. It also tests the independent Cartesian inverse. The cutoff is smooth but nonanalytic, and coarse inverse quadrature has substantial errors; refined results must be read from verification/cutoff_inverse_refined.json and verification/cutoff_inverse_order512.json. At order 512, the maximum relative-velocity errors for R=8,16,32 are respectively 2.53e-12, 1.49e-11 and 2.26e-11 on the stated sample points. The y=0 residual formula was separately checked by seven-point differences at five beta values, including the exceptional midpoint cancellation; see verification/normalizers_and_cutoff_algebra.json. No coarse inverse pass is claimed.

## 2. One absolutely convergent drift component need not give a radially weighted L1 norm

Let chi_0 be smooth, zero for y<=1 and one for y>=2, with 0<=chi_0<=1. Define

    Omega(x,y)=chi_0(y) x y^(-3/4) exp(-x^2/y)   for y>1,
    Omega(x,y)=0                                for y<=1.

This is globally smooth and odd in x. It is uniformly O((1+r)^(-1/4)). For |x|<=y this follows from maximizing x exp(-x^2/y), whose size is O(sqrt(y)); for |x|>y the exponential dominates every power of |x|. The compact y transition causes no problem.

Its vertical center component is absolutely convergent. Indeed for y>=2,

    integral_R |x Omega(x,y)|/(x^2+y^2) dx
      <= y^(-11/4) integral_R x^2 exp(-x^2/y) dx
      = C y^(-5/4),

which is integrable in y. The transition region is also integrable.

On the other hand, in sqrt(y)/2<=x<=sqrt(y), y>=4, one has |Omega|>=c y^(-1/4), 1+r<=C y, and the interval has length comparable to sqrt(y). Therefore

    integral_R |Omega(x,y)|/(1+sqrt(x^2+y^2)) dx
      >= c y^(-3/4).

This diverges after integration in y. Thus

    integral |x Omega|/r^2 < infinity,
    integral |Omega|/(1+r) = infinity.

The relative inverse is still well-defined and sublinear by research/03_inverse because Omega has uniform power decay. This is a div-curl and inverse example, not a transported profile. It proves that a radial weighted-L1 theorem cannot be applied merely from absolute convergence of the single displayed drift component without a further argument from the PDE.

## 3. A vanishing circular drift can depend on the cutoff shape

Fix 0<delta<1 and define the globally smooth odd-in-x density

    Omega(x,y)=(x^3-3xy^2)/(1+x^2+y^2)^((3+delta)/2).

In polar coordinates its only angular factor is cos(3 phi). For every circle radius R, the vertical center integral truncated at R vanishes exactly, because integral_0^(2pi) cos(phi)cos(3phi)dphi=0.

For a positive smooth shape function h(phi), truncate instead at 0<=r<R h(phi). The leading radial integral gives

    v_h(R)=R^(1-delta)/(2pi(1-delta))
           * integral cos(phi)cos(3phi) h(phi)^(1-delta)dphi + O(1).

To justify the error, subtract the leading r^(-delta) tail from the radial density r^3/(1+r^2)^((3+delta)/2); its remainder is O(r^(-delta-2)), which is integrable in dr. The estimate is uniform when h is bounded above and below away from zero.

Take h(phi)=1+epsilon cos(2phi), for a fixed sufficiently small nonzero epsilon. Expanding this positive smooth factor and using

    integral cos(phi)cos(3phi)cos(2phi)dphi=pi/2

gives

    v_h(R)=[epsilon/4+O(epsilon^2)]R^(1-delta)+O(1).

For sufficiently small fixed nonzero epsilon the coefficient is nonzero, so this cutoff diverges although every circular truncation is zero. Both cutoffs respect x reflection. The example does not say that every conditional integral must depend on every cutoff; it refutes the general inference that circular cancellation alone defines a shape-independent absolute velocity.

## Dependencies and scope

Only explicit differentiation, compact-support integration by parts, the fundamental solution of -Delta, elementary one-dimensional bounds and Fourier trigonometric orthogonality are used. The inverse uniqueness and growth statements are proved in research/03_inverse. These examples do not imply nonexistence of a true B2 profile. They specify errors that a verifier must be able to detect.
