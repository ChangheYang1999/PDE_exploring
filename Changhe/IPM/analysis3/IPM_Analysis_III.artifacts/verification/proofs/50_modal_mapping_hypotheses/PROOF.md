# The selected exact modal density satisfies the coupling hypotheses

## Exact object and conclusion

This statement concerns the normalized, exactly joined modal density defined in proof 04 from the read-only original `analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz`. Every stored double is interpreted as an exact dyadic number. The mathematical inner and outer correction coefficients are recomputed by exact C6 matching; the stored rounded Ei and Eo arrays are not substituted for them. The scalar repair z is the exact real number in proof 04, not a midpoint of its enclosure.

The density satisfies the coefficient assumptions (B1)-(B2) of topics48-49 and the axis-density assumptions of proof 46. In particular those coupling estimates do apply to this density. This assertion is qualitative: it establishes finiteness of the required coefficient constants, without furnishing a numerical upper bound for them.

It does not prove positivity of the axis transport rate, positivity of a Garding margin, injectivity, a numerical inverse bound or a nonlinear existence theorem.

## Structural input checks

The independent code reads the original NPZ directly and checks:

- 260 finite angular modes, degree7, with1565 spline coefficients per mode;
- the first and last knot multiplicities are8, with strictly increasing simple interior knots;
- exact 0<k<1, bi>50 and bo>125;
- the ten outer exponents alpha_q=k-3-j_q(1-k)-2l_q, with the pairs stated in proof 04, all satisfy alpha_q<=k-3;
- 3-bo<k, so the logarithmic outer matching term decays strictly faster than the leading density order r^k;
- the original file hash agrees with the independently used input in the earlier modal calculations.

All arrays used as defining data contain finite binary64 values. Their exact rational interpretations are finite. The code also constructs the endpoint spline jets for all260 modes by the derivative-coefficient recurrence, computes the exact inner and outer matching corrections, and checks all3640 join equations at orders0 through6. The outer scalar repair preserves these equations for every real z by the same linear matching formula.

## Joining and annular regularity

Let J_n be a mode's spline endpoint jet and P_n the jet of its non-correction terms. For b=bi at the inner endpoint and b=-bo at the outer endpoint, define

 E_i=sum_(j=0)^i (-b)^(i-j)(J_j-P_j)/((i-j)!j!), i=0,...,6.

Multiplication by exp(b tau) gives exactly

 sum_(i=0)^n n! b^(n-i) E_i/(n-i)! = J_n-P_n,
                         n=0,...,6.

This is an algebraic identity over the reals, so it also covers the repaired A_00+z coefficient. Degree-seven splines with simple interior knots are C6 there, and the exact matching makes the two external joins C6 as well. A finite trigonometric sum with these radial coefficients is C6 on every compact annulus. Thus all C5 derivatives required by (B2) exist and are bounded on a fixed compact annulus. No fifth derivative at0 is assumed.

## Uniform origin bounds

For t<=t_minus, the cofactor is

 b(t,theta)=1+sum_(m,j)D_mj exp(2j(t-t_minus))cos(2m theta)
       +exp(bi(t-t_minus))sum_(m,i)E_mi(t-t_minus)^i cos(2m theta),

where j>=1, i<=6 and bi>50. Any fixed number of angular derivatives only multiplies a finite mode coefficient by a finite power of2m. Any fixed number of t derivatives preserves the exponential order and the finite logarithmic degree. Hence b-1 and the derivatives needed in (B1) are O(exp(2t)). The axis value A=b(t,pi/2) has A=1+O(exp(2t)), A'=O(exp(2t)), as used in proof 46.

In Cartesian coordinates every m-th derivative of r^d H(theta) is r^(d-m) times a smooth angular function. The degree-five leading correction therefore has derivatives through order5 bounded by C r^(5-m) off0. The faster terms and the logarithmic term satisfy the same upper bounds: r^(bi-2)|log r|^i is bounded near0 for bi>2. Consequently

 |partial^nu(rho-p)(X)|<=C r^(5-|nu|), |nu|<=5, 0<r<r_minus.

On a fixed scaled annulus 1/32<=|X|<=32 this implies uniform C5 bounds for rho(R0 X)/R0^3 as R0->0. The non-polynomial degree-five angular term prevents C5 regularity at0, as proved in proof 33, but does not impair this scaled bound.

## Uniform infinity bounds

Each outer density power has degree

 3+alpha_q=k-j_q(1-k)-2l_q<=k.

The matching correction has degree3-bo<k and a polynomial in log r of degree at most6. Any fixed Cartesian derivative lowers its power by its derivative order and preserves finite logarithmic degree. The strict power gap absorbs those logarithms. Hence

 |partial^nu rho(X)|<=C r^(k-|nu|), |nu|<=5,

for all sufficiently large r, and the cofactor derivatives in (B1) are O(r^(k-3)). The scalar repair changes only finite coefficients of terms already having these orders. Thus rho(R0 X)/R0^k has a uniform C5 norm on the fixed scaled annulus as R0->infinity.

For R0 in the intervening compact range, the rescaled annuli stay in a compact punctured region where rho is C6. The scaling factors R0 and d(R0) are bounded above and away from0 there. This supplies the remaining finite bound in (B2).

## Consequence and scope

The density hypotheses of V049-V052 are therefore verified for the selected exact modal object. On the strong scalar domain B, those results still use the positive-axis assumption (A) that defines H and its Hardy bounds. The pure transport theorem also requires its positive margin. Those are separate transport-coefficient assertions, not consequences of the density bounds proved here.

No table of sampled derivative maxima is used to infer a global bound. The finiteness assertions follow from exact exponent inequalities, finite mode counts, exact joins and compactness of the intervening annuli.
