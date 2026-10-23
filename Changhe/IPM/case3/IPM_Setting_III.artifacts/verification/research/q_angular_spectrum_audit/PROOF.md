# What the quotient's angular spectrum measures

Verifier result 106, written 2026-10-21 before its supporting code.

## Statements and scope

There are three distinct statements.

1. For the finite Q representation used by the numerics lane, every cosine coefficient of q=rho/(a y) can be evaluated directly from the stored radial Chebyshev coefficients, without angular sampling or a discrete cosine transform. This is an exact identity for the saved finite formula, not a statement about a limiting field.
2. A fractional horizontal-axis density term with angular exponent kappa contributes quotient cosine coefficients of order j^(-kappa), not j^(-kappa-1), provided its leading coefficient is nonzero and the remaining terms satisfy the stated endpoint regularity assumptions. Division by y removes one power of angle. At the vertical axis division by y does not remove a power.
3. Finitely many measured Fourier coefficients alone do not bound the amplitude of a fractional endpoint singularity. Additional information, such as a solved frozen angular equation and controlled remainders, is necessary. This statement does not deny constraints imposed by that equation.

These are representation and diagnostic statements. They do not prove convergence, determine a limiting regularity class, or supply a profile.

## 1. Exact coefficients of a saved finite Q formula

Let L>0, kappa_map>1, s in [0,1), and

    r = L sqrt(s) [2(1-s)]^(-kappa_map),
    rho = y (1-s) sum_(j=0)^(M-1) s^j B_j(2s-1) cos(2j theta),
    B_j(t)=sum_(h=0)^N b_(j,h) T_h(t),
    a=rho_y(0)=B_0(-1) != 0.

Here kappa_map is the radial map parameter, not the axis exponent used below. The quotient extended to the axes is

    q=sum_(j=0)^(M-1) c_j(r) cos(2j theta),
    c_j(r)=(1-s)s^j B_j(2s-1)/a.                         (1)

For j>=M, c_j is exactly zero. The equality follows simply by division; extension at y=0 uses the displayed smooth formula. The monotone map has a unique s for every r>0: d log r/ds=[1+(2kappa_map-1)s]/[2s(1-s)]>0, and the endpoint values are zero and infinity. All B_j can be computed by Chebyshev recurrence or Clenshaw summation without converting to ill-conditioned floating monomials.

A midpoint cosine transform on J angular nodes in [0,pi/2] is exact in exact arithmetic for this finite polynomial when J>=M. This follows by the finite geometric sum of exp(i m pi(l+1/2)/J) and cosine product identities. Its floating evaluation can nevertheless return a roundoff floor where (1) is much smaller or exactly zero. A slope fitted to coefficients at that floor has no tail interpretation. Every fixed finite representation is an angular trigonometric polynomial, so it has a zero tail; smoothness of a limit requires control as M increases.

## 2. Fractional axis exponents after taking the quotient

Fix a positive radius. Suppose an odd-in-y density perturbation near the horizontal axis has the local form

    h(r,theta) = C_x r^d sign(theta)|theta|^kappa
                 times an even smooth factor equal to one at zero,

where kappa>1 is not an integer. Suppose away from this endpoint the cutoff portion is smooth and vanishes before the other axis. Then, since y=r sin(theta),

    h/(a y) = (C_x/a) r^(d-1)|theta|^(kappa-1)
              times an even smooth factor equal to one at zero.              (2)

For an even quotient on both axes, its j>=1 cosine coefficient on the quadrant is (4/pi)int_0^(pi/2) q(theta)cos(2j theta)dtheta. Formula (2) therefore has leading coefficient

    c_j^x ~ (4/pi)(C_x/a)r^(d-1) Gamma(kappa)
             cos(pi kappa/2) (2j)^(-kappa).                (3)

The cosine factor is nonzero for noninteger kappa. The leading term is absent when C_x=0. The smooth factor changes only lower-order asymptotics; this requires its derivatives to have the corresponding local Taylor bounds, not merely a pointwise little-o remainder.

For completeness, this asymptotic can be proved without inferring it from a log-log fit. Write m=floor(kappa) and alpha=kappa-m in (0,1). Integrate the cut-off power theta^(kappa-1) by parts m times. At zero every preceding derivative vanishes because its power is positive. Terms in which derivatives hit the cutoff are smooth and supported away from zero, so repeated integration by parts makes their transforms decay faster than every power. The remaining derivative equals Gamma(kappa)/Gamma(alpha) theta^(alpha-1). After the change of variables u=2j theta, its oscillatory integral tends to

    int_0^infinity u^(alpha-1) cos(u+m pi/2) du
       = Gamma(alpha) cos(pi alpha/2+m pi/2).

The integral converges by integration by parts on its tail, since 0<alpha<1; its tail is O(R^(alpha-1)). Its value follows by damping with exp(-epsilon u), evaluating the Gamma integral as Gamma(alpha)(epsilon-i)^(-alpha), and letting epsilon decrease to zero. The damped and undamped tail bounds justify this limit. These operations give (3). Expanding the even smooth factor supplies the same calculation at powers kappa+1,kappa+3,...; a finite expansion with a sufficiently differentiable remainder proves that those terms are lower order.

At the vertical axis let t=pi/2-theta, and suppose instead h=C_y r^d |t|^p times a smooth even factor with value one at zero. Now y=r cos(t) is nonzero there, so the quotient has exponent p. Its contribution is

    c_j^y ~ (-1)^j (4/pi)(C_y/a)r^(d-1) Gamma(p+1)
             cos(pi(p+1)/2)(2j)^(-p-1),                  (4)

when p is noninteger and the same endpoint assumptions hold. If both endpoints are present their contributions add, with their respective powers and signs. One endpoint, or isolated measured coefficients, may have zero amplitude.

For the frozen source exponents in the team's already checked angular system, kappa_x=(A d-1)/(A-1) and p_y=(a-d+1)/(A-1). Equations (3)-(4) give quotient powers j^(-kappa_x) and (-1)^j j^(-p_y-1). At A=5,d=12/5, kappa_x=11/4. The horizontal quotient exponent is therefore -11/4, not -15/4. This corrects the exponent used in NUM_REPORT4L(c21); it is not an amplitude bound or a conclusion that such a mode occurs in the saved iterates.

## 3. An exact spectrum test and the finite-data limitation

Let nu>0 be noninteger and F(theta)=|sin(theta)|^nu, extended with the quotient parities. Write F=c_0+sum_(j>=1)c_j cos(2j theta). Put I_j=int_0^(pi/2) sin(theta)^nu cos(2j theta)dtheta. Then

    c_j/c_0 = 2 I_j/I_0   (j>=1),
    I_j/I_(j-1) = (2j-2-nu)/(2j+nu).                    (5)

To prove the recurrence, multiply sin(theta)F'=nu cos(theta)F by cos((2j-1)theta) and integrate. The integrated derivative term has zero endpoint boundary terms. Product-to-sum gives -j I_j+(j-1)I_(j-1)=(nu/2)(I_j+I_(j-1)), which is (5). The integral I_0 is finite and positive. Thus for rational nu all normalized coefficients in (5) are exact rational numbers. Their ratios also show decay exponent nu+1, in agreement with (3) after nu=kappa-1. This test can compare powers over increasing j without any numerical angular differentiation or quadrature.

For any finite J0, subtract the exact cosine polynomial

    H(theta)=F(theta)-c_0-sum_(j=1)^J0 c_j cos(2j theta).

Every coefficient of H through J0 is zero. The subtracted polynomial is analytic at the axes and cannot change the noninteger |theta|^nu coefficient at zero. Multiplying H by any constant gives an arbitrarily large fractional coefficient with the same vanishing finite set of measured coefficients. This proves statement3 for unrestricted endpoint data. H need not solve the frozen angular equation, and this argument is not being used as a counterexample to a theorem that assumes that equation. It shows precisely why a quantitative coefficient-amplitude inference must use and validate those extra hypotheses.

## Verification requirements

Saved-state checks must preserve the exact binary input coefficients and actual map exponent. Use at least two arithmetic precisions for (1), give the physical radii and inverse-map defects, retain signed coefficients, and identify exact zeros imposed by M. No independent inverse-velocity computation is claimed for this density-only diagnostic; the same frozen coefficient data have separate canonical inverse checks elsewhere.

Supporting tests should include exact recurrence (5), an independent manufactured cosine transform and Chebyshev evaluation, and direct saved-state coefficient comparisons. They do not turn a finite spectrum into a regularity theorem.
