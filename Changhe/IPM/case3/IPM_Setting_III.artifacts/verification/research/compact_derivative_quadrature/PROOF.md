# Whole-plane derivative-norm quadrature in the compact radial variable

Written 2026-10-21 UTC before implementation. This extends result102 by a change of radial variable. It is an exact integral identity and a numerical quadrature design, not a certified quadrature error bound.

Let f be a real finite sine expansion f=r sum_(n>=1) d_n(log r) sin(n theta), with the smooth-origin and sublinear-symbol bounds of a finite Q density or its canonical transport residual. Use the full ordered Cartesian derivative norm. For integer k>=2, define

    S_k(s)=sum_n sum_(j=0)^k binom(k,j) [P_(k,j,n)(E)d_n]^2,
    E=2s(1-s)/(1+(2kappa-1)s) d/ds,
    P_(k,j,n)(z)=prod_(i=0)^(j-1)(z+1-n-2i)
                  prod_(h=0)^(k-j-1)(z+1+n-2h).

Empty products equal one. In the Q map r=L sqrt(s)[2(1-s)]^(-kappa), L>0 and kappa>1, one has

    ||D^k f||_2^2
      = pi 2^(kappa(2k-4)-k-1) L^(4-2k)
        int_0^1 s^(1-k) (1-s)^(kappa(2k-4)-1)
                 [1+(2kappa-1)s] S_k(s) ds.                 (1)

Proof. Logarithmic differentiation of the map gives

    d(log r)/ds=[1+(2kappa-1)s]/[2s(1-s)].

This is strictly positive on (0,1); the map is a bijection onto (0,infinity). Substitute this derivative and r^(4-2k) into result102's positive annular formula, first over any compact subinterval of (0,1). Smoothness at zero and the symbol bounds at infinity give square integrability for k>=2 as proved there. The integrands are nonnegative. Increasing the compact subintervals to (0,1), monotone convergence proves (1). No finite physical radius or omitted interior disc occurs in (1), and no integration by parts is used.

The apparent powers at s=0 in (1) are canceled by smoothness of the complete differentiated field. This cancellation must be resolved numerically; replacing it by a cutoff is not justified by the identity. At s=1, d_n=O(1-s), and the logarithmic derivatives have the same bound. The integrand is O((1-s)^(1+kappa(2k-4))) for each finite mode, except for harmless higher-order logarithmic terms in the canonical inverse. The exponent is at least one. This shows integrability at that endpoint; it does not give a numerical error constant. The Q fields are smooth at zero but their analytic continuation can be poorly conditioned when the polynomial degree is high.

For reproducible numerical integration, apply Gauss-Legendre quadrature on (0,1), using positive nodes and weights and evaluating the independent full-plane inverse at every node. The radial Jacobian multiplies the positive logarithmic-radius integrand of result102. Compare distinct node counts at common precision. The quadrature approximates the entire integral (1), including physical radii arbitrarily large as s approaches one, but it remains numerical evidence without an enclosure. A finite quadrature has no largest-domain boundary condition. Record its extreme sampled radii and the contributions of physical shells to detect concentration and underresolution. Separate the absolute density and residual norms, and do not infer smooth limiting regularity from their ratio.

The first pilot based on eleven broad log-radius panels with six versus ten nodes per panel gave large differences in residual derivative norms. Those pilot values are not converged. Compact quadrature is introduced to resolve the many radial oscillations of high-degree saved polynomials, including endpoint clustering. The two new node counts are resolution tests, not a proof that the second is adequate. Further subdivision or higher counts remain required if they disagree.

An independent manufactured integral is available for every order. Let g(x,y)=y exp(-r^2) and h=-Delta g=4y(2-r^2)exp(-r^2). Cartesian Fourier differentiation or direct Gaussian integration gives

    ||D^k g||_2^2=pi 2^(k-3)(k+1)!,
    ||D^k h||_2^2=pi 2^(k-1)(k+3)!.

For completeness, the Fourier multiplier of the full ordered derivative norm is (xi_1^2+xi_2^2)^k. The transform of g is a constant times xi_2 exp(-|xi|^2/4). Its radial Gaussian moment ratio between order k and zero is 2^k(k+1)!, while direct integration gives ||g||_2^2=pi/8. Multiplication by |xi|^2 to form h shifts k by two, yielding the second formula. This argument does not use the polar differential polynomials. It supplies whole-plane target integrals for testing (1), the compact-map Jacobian and quadrature refinement. A numerical test of these targets supports the implementation, not every candidate's convergence.

Dependencies: result102, the Q inverse regularity proved there, change of variables, monotone convergence for nonnegative integrands, and elementary Gaussian integration.
