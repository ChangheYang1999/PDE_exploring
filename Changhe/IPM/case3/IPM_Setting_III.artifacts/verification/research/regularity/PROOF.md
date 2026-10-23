# A center-regularity test for the numerical representation

Status: exact analytic obstruction for the encoded interpolation class. Quantitative interval evaluations are recorded separately. It is not a nonexistence theorem for the PDE.

## Statement

Let L>0, q>0 and let t=t(r) be the inverse near zero of r=L(1+t)/(1-t)^q. Let

    b(t,theta)=sum_{k=0}^{M-1} Bk(t)cos(2k theta),
    rho(x,y)=y (1+r^2/L^2)^((gamma-1)/2)b(t(r),theta),

where each Bk is a polynomial. If rho extends to a C^2 function at zero with even-x/odd-y parity, then

    partial_t Bk(-1)=0 for every k.

In particular the angular mean B0'(-1) must vanish. This necessary condition applies even if the endpoint angular values are projected to make the first derivative common.

## Proof

The inverse function theorem gives t(0)=-1 and t'(0)=2^q/L, which is nonzero. The radial weight is 1+O(r^2). Hence along each fixed angle,

    rho(r cos theta,r sin theta)
      =r sin(theta)b(-1,theta)
       +r^2 sin(theta)(2^q/L)partial_t b(-1,theta)+O(r^3).

If rho is C^2, its expansion has a linear Taylor polynomial and a homogeneous quadratic Taylor polynomial, with an o(r^2) remainder. Parity forces the quadratic polynomial to vanish: no monomial of total degree two has even x degree and odd y degree. Therefore sin(theta)partial_t b(-1,theta)=0 for every angle. Continuity in theta removes the isolated zeros of sin(theta), so partial_t b(-1,theta)=0 identically. Orthogonality of cosine modes gives each Bk'(-1)=0.

The same Taylor argument gives all smoothness requirements for an analytic radial interpolation: odd powers r^(2j+1) in b(t(r),theta) must vanish, and the coefficient of r^(2j) must be a linear combination of cos(2k theta) with k<=j. These requirements concern the complete radial expansion, including the weight when assessing rho; the weight is analytic in r^2 and does not alter the first forbidden radial term.

## Application and limitations

The saved early numerical checkpoints use the displayed representation, with q called p in their metadata. That map exponent is distinct from the physical far-field exponent 1/c_l. A large q makes t'(0)=2^q/L large, so modest endpoint interpolation defects can produce large physical radial jets.

The necessary condition is exact. Small sampled transport residuals do not imply it. Convergence of such nonsmooth approximants to a smooth exact solution is logically possible, but it must be demonstrated through appropriate jet convergence and independent residual control. Failure of the test rejects a claim that the explicit interpolant itself is C^2; it does not reject every possible smooth PDE solution.

Dependencies: the inverse function theorem, a two-variable Taylor expansion, and finite Fourier orthogonality. No inverse-operator evaluation or PDE solution is used in this obstruction.
