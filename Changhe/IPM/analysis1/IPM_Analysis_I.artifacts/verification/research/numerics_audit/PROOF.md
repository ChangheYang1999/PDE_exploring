# Audit of the numerical inverse's endpoint formulas

Status: five specific implementation defects REFUTED by elementary algebra and executable checks, 2026-10-20. This concerns the source file hashed in evidence/inverse_endpoint_audit.json. It does not refute the full-plane Green formula, the existence of a profile, or every sampled velocity value.

## Central-strain head exponent

For the normalized center rho=x^2 y+o(r^3), a sufficiently regular trial has rho_x=2xy+o(r^2)=r^2 sin(2 theta)+o(r^2). Thus the first source mode f_1 starts with r^2, not r^3. For its leading monomial,

(1/2) integral_0^{r_0} f_1(s)/s ds = f_1(r_0)/4.

The numerics inverse code uses f_1(r_0)/6 in the total strain, through the term (1/2)*(f_1(r_0)/3). Its leading head bias is therefore -f_1(r_0)/12. For the manufactured Gaussian test in that file, f_1=6r^2+O(r^4), the bias at r_0=1e-4 is -5e-9+O(r_0^4), explaining the reported central-strain test error. For X3 evaluated with r_0=L*1e-4, the predicted bias is approximately -4.88e-8, consistent with the discrepancy against the independent all-plane density integral. Higher-order center terms need their own bound after correcting the leading exponent.

The inner Green recurrence's starting formula r_0^2 f_n/(4n+2) is consistent with f_n~r^{2n}; the docstring's statement f_n~r^{2n+1} is inconsistent with that formula. This audit does not establish a rigorous higher-mode head approximation.

## Shifted interpolation nodes

The recurrence's ideal stencil starts at i-(p//2-1). The actual clamped stencil starts at lo, with off=lo-[i-(p//2-1)]. Therefore the actual relative abscissae of the sampled values are

nodes_actual[a]=a-(p//2-1)+off.

The function _shifted_weights uses the minus sign before off. This integrates the polynomial interpolant on different abscissae. To expose the error without a PDE or asymptotic estimate, set the exponential weight to one and pass the values of the linear function on the actual nodes. In the function's mistaken coordinates these values equal t+2*off. Its returned integral is 1/2+2*off, although the correct integral over [0,1] is 1/2.

The executable test invokes the actual read-only function with off=-2,-1,1,2 and confirms the predicted incorrect answers. No files in the numerics lane are modified and Python bytecode writes are disabled. The required repair is to use +off in the interpolation abscissae, or to redefine off consistently throughout both recurrences.

## Other inspected details

The actual velocity implementation has U_r=-psi_theta/r and U_theta=psi_r, which agrees with U=(-psi_y,psi_x). An earlier module-level docstring still states the opposite signs. This is a documentation error, not a present velocity-sign failure. The recurrence carries an explicit dt multiplier. The exterior least-squares fit remains a floating approximation with no certified tail remainder. Correcting the two endpoint formulas therefore will not by itself create a rigorous inverse evaluator.

## False Arb enclosures at exact interior knots

The numerical X3Arb.bspline_values method converts the Arb endpoints to binary64 and selects spans with the strict inequalities knot[j+1]>lo and knot[j]<hi. At an exact interior knot, lo=hi equals that knot. Neither adjacent span passes. The empty-list fallback chooses the first span, even for a knot deep inside the interval. Narrow Arb boxes around a knot have the same failure when both endpoints round to that knot.

For example, knot number 100 is the exact stored binary64 value about 0.262063639263482. B_{0,7} is identically zero there because its support ends at knot number 8. The current function returns the first-span polynomial extension, about -5.4388e16, with a narrow ball excluding zero. The code audit repeats this at knots 30,100,200,300, including a radius ball obtained by inverting q exactly and mapping back to q. The full H enclosure is disjoint from the independent Arb polynomial evaluation at all four tested points, so the error is not limited to an unused basis coefficient.

The repair must select all potentially intersecting closed spans with outward comparisons, and explicitly evaluate on their intersections or otherwise bound each span extension. Nearest-rounded binary64 endpoint selection is not an outward interval decision. At an exact shared knot either adjacent correct polynomial gives the common spline value; the first-span fallback does not.

The H_r implementation also divides chi^{m-1} by chi at r=0, returning NaN instead of the removable derivative limit. This is an unsupported center evaluation, not a finite false enclosure. The executable evidence is evidence/arb_knot_audit.json, with the audited file's hash and actual returned balls. Until repaired and rechecked, the advertised point/box enclosure guarantee is false.

## New modal trial: missing constant in the strain constraint

The source modal_fit.py now defines, on r<rmin,

a_0=1+sum_{j=1}^7 D_{0j}(r/rmin)^{2j}+inner correction,

while every fitted basis column represents only the variable terms. For rho=x^2 y sum_m a_m(r)cos(2m theta), direct trigonometric projection gives

c=integral_0^infty r[a_0/4+a_1/8-a_2/8-a_3/8]dr.

Indeed the canonical strain is c=(1/pi) integral_0^infty integral_0^{2pi} rho(r,theta) sin(3theta) r^{-2} dtheta dr. Substitution of rho=r^3 cos^2(theta)sin(theta) sum a_m cos(2m theta) gives the stated measure r dr. The exact identity cos^2(theta)sin(theta)sin(3theta)=1/8+cos(2theta)/8-cos(4theta)/8-cos(6theta)/8 gives the four weights after full-circle integration. All remaining modes vanish by orthogonality. Evidence affine_strain_audit.json independently computes these weights as exact Laurent coefficients. It also extracts and executes the actual source expressions for c_now and c_after with zero variable coefficients, obtaining zero, while the actual Trial evaluator retains a_0=1 on the inner region. This test isolates the affine offset; it does not present the zero coefficients as a joined admissible trial.

The constant one in a_0 on [0,rmin] contributes rmin^2/8. The current c_now and c_after in main use only kappa times the fitted coefficient vectors, so both omit this fixed affine contribution. The normalization correction therefore targets the wrong affine hyperplane. The missing term is about 7.31803730382829e-6 for the currently stored rmin. This algebraic error is independent of floating point cancellation and must be repaired before certifying normalization. Exact joins and exact elementary relations between stored log endpoints and radii must also be defined; a numerical constrained least-squares solve alone does not enforce literal exact identities.

## New modal trial: primitive subtraction loses the cell moment

The API explicitly defines integral_exp_poly(lam, coeffs, tau0, tau1) as the integral of e^{lam tau} times the polynomial in ascending unscaled powers of tau between the supplied limits. Trial cells use tau=t-t_a. The exponential-polynomial antiderivative is analytically correct, but the float64 subtraction in expoly.integral_exp_poly and trial_green.integ_vec is not a reliable small-cell evaluator. With the actual binary64 inputs h=0.008, lambda=2 and p(tau)=c tau^7, c=float(h^{-7}), both return exactly zero for the integral from zero to h. Independent Arb summation gives an enclosure inside

[0.00101432512053290584,0.00101432512053290585].

With h=0.001 the routines return -4194304, although the integral is positive and about 0.00012522242234349. These are actual read-only calls of the numerics routines. The independent enclosure uses

integral_0^h exp(lambda t)c t^d dt
= c h^{d+1} sum_{j>=0}(lambda h)^j/[j!(d+j+1)].

For lambda h>0 all terms are positive; after j=39 the remainder is at most the j=40 term divided by 1-lambda h/41. This bound is applied with exact dyadic inputs and outward Arb arithmetic. The source hashes, six test outputs and proof evidence are in evidence/modal_trial_audit.json. Stable scaled moments or a sufficiently precise interval implementation are required. This does not refute the algebraic Green recurrences.

The currently stored trial_h0.008.npz predates the changed class: it lacks Ei, Eo, bi, bo and p, which current Trial.__init__ requires. Therefore no assertion that this stored file is the completed new trial is made, and no exact-join verdict is inferred from it.

## Center regularity of the proposed modal representation

High angular modes multiplied by r^{2j}, j>=1, do not obstruct P_2 regularity after the x^2 y prefactor. Each such density term is homogeneous of degree 3+2j near zero with a smooth angular factor, hence is C^{2,alpha} for every alpha<1. The inner correction r^{bi}(log r)^i, bi>0, likewise gives density derivatives of order at most three bounded near zero, with the third derivatives tending to zero after the x^2 y prefactor. Its factor tends to zero. Thus a finite-mode trial of this form has the required continuous center factor and P_2 center regularity, provided the joins away from zero are made exactly C^{2,alpha}. No smooth-center claim follows.

## Center conditions for the new representation

The local P_2 assertion assumes finitely many modes; exactly a_0(0)=1 and no constant inner term in any other mode; powers r^{2j} with integer j>=1; exact positive correction exponents b_i>0; and exact C^{2,alpha} joins away from zero. Multiplication by x^2y gives homogeneous degree 3+2j terms with smooth angular factors, whose third derivatives are locally bounded. Log corrections have third derivatives O(r^{b_i}|log r|^6), also bounded. Second derivatives are therefore locally Lipschitz across the origin. The factor tends uniformly to one. None of this proves exact joins of the presently stored data, nor a smooth center factor. In particular a noninteger positive b_i need not preserve arbitrarily high regularity.
