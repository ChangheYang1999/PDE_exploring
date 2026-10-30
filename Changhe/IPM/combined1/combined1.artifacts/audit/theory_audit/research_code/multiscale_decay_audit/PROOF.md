# Independent decay audit for the multiscale candidate010 generators

## Statement

Let c>1, delta=1-1/c, p_j=(3+1/c-j delta)/2, and j,m,w,n be nonnegative integers. Let R>0 be fixed. Set

    H_m(x,y)=Re(x+i y)^(2m),
    t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2),
    G=H_m(1+r^2)^(p_j-m)t_R^w u_R^4 P_n(2t_R-1),

where P_n is the degree-n Legendre polynomial. Then G is smooth onR2. Every Cartesian derivative of total orderk and every further finite number of logarithmic radial or angular derivatives is O(r^(2p_j-8-k)) onr>=1. Consequently the density and velocity obtained by the campaign's fixed third-order Cartesian potential operators satisfy

    (r partial_r)^ell [u/r]=O(r^(-delta-j delta-8)),
    (r partial_r)^ell D rho=O(r^(-delta-j delta-8))

for every finiteell, uniformly inangle. Both fields have finitely many angular modes. Adding finitely many such generators to a finite canonical single-scale potential preserves the T4-097 decay hypotheses with exponentdelta. It also preserves bounded positive-order derivatives ofu andrho, as needed by the new origin argument, though normalization must be checked separately.

This confirms the multiscale decay claim in theory_v02 section8 for the exact candidate010 once its generator metadata have been checked. It asserts no background matrix bounds, inverse, residual certificate or closure.

## Proof at the origin

H_m is a polynomial. The functions(1+r^2)^(p_j-m), (R^2+r^2)^(-1), t_R and u_R are smooth globally because their denominators are strictly positive. Integer powersw and4 and the polynomialP_n preserve smoothness. ThereforeG is smooth, and so are all of its Cartesian derivatives. No singular polar expression is used at the origin.

## Proof at infinity

Forr>=1, H_m=r^(2m)cos(2mtheta) andu_R^4=R^8r^(-8)t_R^4. Thus exactly

    G=r^(2p_j-8) cos(2mtheta) b(logr),
    b=(1+r^(-2))^(p_j-m) R^8 t_R^(w+4) P_n(2t_R-1).

All logarithmic derivatives ofb are bounded onr>=1. To see this directly, E=r partial_r sends z=r^-2 to-2z, andz belongs to[0,1]. The factor(1+z)^(p_j-m) is smooth on this compact interval. AlsoE t_R=2t_R(1-t_R); every repeatedE derivative of a polynomial in t_R is again a polynomial in t_R, hence bounded on[0,1]. The product rule proves the assertion for every derivative order. Angular derivatives ofcos(2mtheta) are bounded.

Now

    partial_x=r^-1(cos theta E-sin theta partial_theta),
    partial_y=r^-1(sin theta E+cos theta partial_theta).

Induction onk shows that eachk-th Cartesian derivative ofG is r^(2p_j-8-k) times a finite sum of products of trigonometric polynomials and bounded logarithmic derivatives ofb. RepeatedE or angular differentiation preserves this form. This proves the first bound.

The potential operators definingrho andu contain exactly three Cartesian derivatives, with constant coefficients. Henceu/r andD rho have exponent2p_j-12. Since2p_j=3+1/c-jdelta, this equals-delta-jdelta-8. Finite angular content is preserved by the displayed Cartesian derivative formulas. The same reasoning for canonical generators withoutu_R^4 gives the known exponent-delta-jdelta. A finite sum is thereforeO(r^-delta), including at least the first three logarithmic derivatives required byT4-097.

For positive-order derivatives ofu andrho the slowest possible exponent is1/c-1<0 from the canonicalj=0terms. At infinity they are bounded, and smoothness gives boundedness on compact sets. This proves the additional regularity statement. The constants may depend onR and on all finite coefficients; no uniform-in-R quantitative claim is made.

## Exact metadata check and evidence

The frozen ipm_exact.py docstring and branch parse define precisely the abovelegqs term. The local metadata checker reads the frozen exact generator JSON without executing that source. It checks the manifest's coefficient hash, c, all generator kinds and nonnegative integer indices, and records the multiscale counts, branch range, angular range, w, n, Q andR values. It checksQ=4 andR in{10,100}. The canonicalmono andleg terms satisfy the same smoothness proof withQ=0. This suffices for the analytic applicability claimed here. Exact center normalization and sector cancellation have separate audits and are not assumed from the manifest.

The argument independently redoes the published decay derivation. It uses no numerical quadrature, sampled far-field estimates, or external asymptotic theorem.
