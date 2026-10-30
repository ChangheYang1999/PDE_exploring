# Audit of direct scaled-generator origin and far-field assembly

## Statement and scope

Fix a rational c>1, gamma=1/c, delta=1-gamma, and an integer J>=0. For finitely many rational coefficients A and tuples (j,m,w,n,Q,R), assume 0<=j<=J, m,w,n,Q are nonnegative integers, and R is a positive rational. Define p_j=(3+gamma-j delta)/2, s=x^2+y^2, H_m=Re(x+iy)^(2m), and

    chi=sum A H_m (1+s)^(p_j-m)
           (s/(R^2+s))^w (R^2/(R^2+s))^Q
           P_n((s-R^2)/(s+R^2)).

Set rho=-partial_y Delta chi, U1=-chi_xyy, U2=chi_xxy and F=(cX+U).grad rho-rho. The direct origin and far-field assembly in the frozen N4 proof is correct, with exact rational coefficients. In particular its finite prefix is complete for every exponent >=-2 when its stated omitted-exponent bound is below -2. A leading coefficient requires the additional strict comparison with that omitted bound.

This is an analytic audit of N4-084. It does not claim a new execution of its3240 coefficient comparisons. The earlier T4-076/077 independently verified the scaled moment and Cartesian-jet ingredients. Full-plane norms require additional integration and are outside this result.

## Exact origin calculation

The polynomial A_n(v)=(1+v)^n P_n((1-v)/(1+v)) has degree at most n. Legendre parity gives the exact scalar factor

    (-1)^n R^(-2w) s^w (1+s)^(p_j-m)
      A_n(s/R^2)(1+s/R^2)^(-w-Q-n).

Its Taylor series converges for |s|<min(1,R^2). The coefficients are rational by the generalized binomial formula. Since H_m has degree2m and s^w has degree2w, fourth derivatives at zero need only terms through s^(2-m), and vanish for m+w>2. Multiplication by the finite expansions of H_m and s^l gives the exact Cartesian coefficients. If b22=[x^2y^2]chi and b04=[y^4]chi, differentiation gives

    partial_y U2(0)=4b22,
    partial_y rho(0)=-4b22-24b04.

No polar limit or omitted local term occurs in these identities.

## Exterior expansion and differentiated coefficients

For z=r^-2 the scalar factor, after extracting r^(2p_j)cos(2m theta), equals

    R^(2Q) z^Q (1+z)^(p_j-m)
      A_n(R^2 z)(1+R^2 z)^(-w-Q-n).

It is analytic for |z|<min(1,R^-2). The finite family therefore has convergent exterior expansions, with every fixed number of Cartesian derivatives, on r>=r0>max(1,R_i). Write the potential as sum r^(alpha_(j,q)+3) C_(j,q)(theta), where alpha_(j,q)=gamma-j delta-2q. All angular coefficients are rational finite cosine polynomials.

The identities partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r give the four cosine/sine differentiation formulas in the frozen proof. Also Delta(r^b cos(n theta))=(b^2-n^2)r^(b-2)cos(n theta). Thus three derivatives give the density coefficients G and velocity coefficients V1,V2 at exponent alpha; a further derivative gives X,Y for grad rho at exponent alpha-1. Reducing negative angular indices by cosine-even and sine-odd parity preserves every mode.

The potential is smooth on the plane because both denominators are strictly positive. Its parity gives precisely S1 density and the stated velocity parity. In particular the exterior computations are derivatives of the original smooth functions, not a separate formal choice of velocity.

## Products and finite-prefix completeness

The linear contribution is (c alpha_(h,q)-1)G_(h,q). The identity

    alpha_(i,u)+alpha_(j,v)-1=alpha_(i+j+1,u+v)

proves the complete nonlinear convolution

    E_(h,q)=(c alpha_(h,q)-1)G_(h,q)
      +sum_(i+j+1=h,u+v=q)(V1_(i,u)X_(j,v)+V2_(i,u)Y_(j,v)).

Here G is zero for h>J. The nonlinear term has h<=2J+1. Convergent power series justify this product coefficientwise in the common exterior region. The finite sum over branches introduces no further exponents.

Since0<gamma<1, every q>=2 has exponent at most gamma-4<-3. Hence q=0,1 and all h through2J+1 include every exponent >=-2. More generally the omitted part of a rectangular prefix h<=hmax,q<=qmax has exponent at most max(gamma-(hmax+1)delta,gamma-2(qmax+1)); discard the first term if hmax>=2J+1. This follows by monotonicity in both nonnegative indices. Equal rational exponents must be combined before any cancellation or leading-term verdict. A strict upper bound below -2 certifies completeness of the forbidden list; a strict upper bound below a retained nonzero exponent certifies that it is the leading exponent.

These conclusions concern a finite given family. They assert neither convergence of an infinite stationary-branch construction nor a numerical lower bound at a finite radius from a leading term alone.

## Verification evidence

The reviewed N4 proof, direct reduction code, comparison harness and result are frozen under reviews/N4_0027/. Their SHA256 identities are in verification/archive_manifest.json. Its result reports3240 exact C/G/E equalities for005/006,48 manufactured scalar checks and2 origin-jet checks. The analytic statements above were checked directly against the frozen implementation. No additional busy computation was required for this audit.
