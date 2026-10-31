# Cartesian finite differences for pressure consistency

Date: 2026-10-29. Status: proved finite-difference identities and conditional truncation bounds. The bounds become numerical error bounds only when their derivative and evaluation-error hypotheses have been established.

## Statement

Let x be a point of R^3, let h>0, and suppose the three closed line segments x+t e_j, -2h<=t<=2h, j=1,2,3, lie in an open set on which P is C6. Define

    D_j,h P(x) = [P(x-2h e_j)-8P(x-h e_j)
                    +8P(x+h e_j)-P(x+2h e_j)]/(12h),
    L_j,h P(x) = [-P(x-2h e_j)+16P(x-h e_j)-30P(x)
                    +16P(x+h e_j)-P(x+2h e_j)]/(12h^2),
    L_h P(x) = sum_j L_j,h P(x).

For k=5,6 write M_j,k for the supremum of |partial_j^k P| on the j-th segment. Then

    |D_j,h P(x)-partial_j P(x)| <= h^4 M_j,5/18,
    |L_h P(x)-Delta P(x)| <= h^4 sum_j M_j,6/54.          (1)

These constants are convenient bounds, not optimal constants. If each pressure value in the formulas is replaced by a value with absolute error at most epsilon, then the extra error is at most 3 epsilon/(2h) in each gradient component, and at most 16 epsilon/h^2 in the Laplacian. Thus for a classical solution of -Delta P=f,

    |-L_h P_tilde(x)-f(x)|
       <= h^4 sum_j M_j,6/54 + 16 epsilon/h^2.             (2)

If the compared source value also has error at most eta, add eta to (2). No assumption on divergence or an Euler residual is needed for these statements.

## Proof

For fixed j put g(t)=P(x+t e_j). Expand g at zero through degree four. The first-derivative stencil annihilates the monomials of degrees zero, two, three and four, and gives one on t. Its Taylor remainder has absolute value at most M_j,5 |t|^5/120. Summing the four absolute weighted remainder bounds gives

    M_j,5 h^4 (32+8+8+32)/(12*120) = M_j,5 h^4/18.

For the second-derivative stencil expand through degree five. It annihilates all monomials of degree zero through five except t^2, on which it gives two. Its remainder is at most M_j,6 |t|^6/720. The four noncentral remainder contributions total

    M_j,6 h^4 (64+16+16+64)/(12*720) = M_j,6 h^4/54.

Adding the three component bounds proves (1). The sum of absolute first-stencil coefficients is 18/(12h)=3/(2h). The sum of absolute second-stencil coefficients is 64/(12h^2)=16/(3h^2). Adding the latter over three axes proves the evaluation-error bounds and (2).

## Application and limits

The independent full-space Green pressure is evaluated at every stencil point's actual radius, with those radii included as quadrature-panel edges. The check compares its Cartesian differences with an independently assembled analytic gradient and with tr(DU DU) from the differentiable represented velocity. It does not obtain a second derivative by substituting the source into the radial Poisson equation. Consequently it tests signs, angular synthesis, radial integration and the association of the source with the differentiated field.

The ratios between successive h values are observations. Fourth-order convergence is expected only where truncation dominates; quadrature and roundoff errors are amplified by h^-1 and h^-2. A small defect does not prove that the pressure is the exact Newton potential, and it does not show that the Euler momentum residual vanishes. The analytic pressure convention and its uniqueness are established conditionally in ../pressure_consistency/PROOF.md. The canonical field's smoothness is established in ../represented_tail_decay/PROOF.md. No bounds on M_j,k or epsilon for the saved numerical state are claimed here.
