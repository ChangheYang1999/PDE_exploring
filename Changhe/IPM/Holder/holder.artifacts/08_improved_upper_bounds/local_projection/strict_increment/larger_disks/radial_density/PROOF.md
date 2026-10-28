# Radial density in the inscribed disks

## Statement and dependencies

Use the homogeneous Euclidean Holder seminorm, measure mu_(R,beta), and local projection decomposition of the parent proofs, with real or complex inputs and0<alpha<1. The exact disk-containment argument in ../PROOF.md is a dependency. Set

    J = 653/288 - (63/8) log(4/3),
    eta_rad(alpha,s) = J s^2 alpha(1-alpha)(1+s/2)^(alpha-2),  0<s<2.

The proposed measure increment bound is

    |mu_(sh,beta)*f(x)-mu_(sh,beta)*f(y)|
        <= (1/2-eta_rad(alpha,s)) h^alpha [f]_alpha,
    |x-y|=h.

It is uniform in the kernel phase beta. Moreover J>7/4608, so it strictly improves the constant-density saving in ../general_radius/PROOF.md for every alpha and every0<s<2. In that proof's two operator upper bounds, replace eta_alpha(s) by eta_rad(alpha,s). In particular the old optimizing radius s_D remains admissible. All statements in this note are OPEN pending independent cross-read. No decimal is asserted.

## Reflection-invariant density below Q

The two disks of radius R/4 centered at distance3R/4 from the origin on the two negative kernel axes lie in Q_R's support. Write c for either center, u=z-c, rho=|u|, and t=rho/R. For a point on the radius-rho circle about c, its angular deviation d from the corresponding axis satisfies |sin d|<=rho/(3R/4)=4t/3. Its distance from the origin is at most R(3/4+t). Therefore the density of Q_R is at least

    w_R(rho) = [1-(32/9)t^2] / [2 pi R^2 (3/4+t)^2],
    0<=t<=1/4.

The numerator is positive on the entire interval. Remove from each disk this radial density with respect to area. It is a positive submeasure of Q_R and is invariant under reflection through any diameter of the selected disk. The remainder and the identity atom remain positive, and the total mass of all terms is still1/2.

Reflect each removed measure in the line through its center perpendicular to the increment direction e. The coupling has the same marginals as before; the evaluation displacement is(h-2u_parallel)e. Since R=sh withs<2, its length is positive. After division byh it lies in[1-s/2,1+s/2]. The linear term in the Taylor estimate for t^alpha integrates to zero by reflection symmetry. Its second derivative is at most

    -alpha(1-alpha)(1+s/2)^(alpha-2)

on that interval. The cost saving from the two disks, divided byh^alpha, is thus at least

    4 alpha(1-alpha)(1+s/2)^(alpha-2) h^(-2)
      * integral_disk u_parallel^2 w_R(|u|) du
    = 2 s^2 alpha(1-alpha)(1+s/2)^(alpha-2)
      * integral_0^(1/4) t^3 [1-(32/9)t^2]/(3/4+t)^2 dt.

The first equality uses integral_0^(2pi) cos(theta)^2 dtheta=pi. The disk measure is finite and compactly supported, so every coupling integral converges. Only the Holder increment inequality is used, which also covers complex-valued inputs.

## Exact integral and strict comparison

Foru=t+3/4, an antiderivative of the last rational integrand is

    F(u) = -(8/9)u^4 + (40/9)u^3 - (19/2)u^2 + (51/4)u
           - (63/16)log u - 27/(64u).

Direct differentiation gives(t^3-(32/9)t^5)/(t+3/4)^2. Its endpoint difference is

    integral_0^(1/4) t^3 [1-(32/9)t^2]/(3/4+t)^2 dt
        = 653/576 - (63/16)log(4/3).

Twice this integral equals J. The integral is positive, so there is no need to infer positivity from subtraction of close decimal values.

For0<=t<=1/4, the density factor[1-(32/9)t^2]/(3/4+t)^2 is at least7/9: its numerator is at least7/9 and its denominator at most1. It is strictly greater at everyt<1/4. Consequently

    J > 2*(7/9)*integral_0^(1/4) t^3 dt = 7/4608.

This proves the strict improvement without numerical evaluation. The remaining positive measure is coupled by translation, and the old proof adds the unchanged paired local and regular far bounds. All singular-integral normalization, convergence at infinity and modulo-constant issues are inherited from the local projection theorem, whose decomposition is unchanged.
