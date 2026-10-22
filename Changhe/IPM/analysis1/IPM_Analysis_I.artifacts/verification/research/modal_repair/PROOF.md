# A consistent exactification of the finite modal trial

Date: 2026-10-20. Status: CONFIRMED within the stated scalar and exactification scope, after two completed interval calculations, source audit, and actual Claude Opus 5.5 review. This produces a normalized kinematically admissible trial, not a stationary solution.

## Exact inputs and convention

Take the finite modal data with M>=4, degree-seven clamped splines, simple interior knots t_i, exact dyadic spline coefficients S_mi, inner coefficients D_mj (j=1,...,7), outer coefficients A_mq, exponents bi>4, bo>4-2k, and 0<k<1/2. All inputs are interpreted as their exact binary64 dyadics and exported to exact hexadecimal JSON. Let t_-=first knot and t_+=last knot; the physical joins are exp(t_-) and exp(t_+). The stored separately rounded rmin and R0 are not used as mathematical endpoints.

Define alpha_q=(k-3)-j_q(1-k)-2l_q for the ten distinct nonnegative integer (j_q,l_q) entries listed in the data, with the first entry (0,0). In particular alpha_0=k-3<-2. Assume alpha_0+bo>0, and every outer exponent is less than -2. These finite inequalities can be checked exactly from the inputs.

Let rho=x^2 y sum_{m=0}^{M-1} a_m(r)cos(2m theta). In t=log r, use the spline on [t_-,t_+]. In the inner region use

a_m=delta_m0+sum_{j=1}^7 D_mj exp(2j tau)+exp(bi tau)sum_{i=0}^6 Ei_mi tau^i, tau=t-t_-.

In the outer region use

a_m=sum_q A_mq exp(alpha_q tau)+exp(-bo tau)sum_{i=0}^6 Eo_mi tau^i, tau=t-t_+.

## Unique exact joins

Let J_n denote the n-th t-derivative of the spline at an endpoint, n=0,...,6, and P_n the corresponding derivative of the non-correction inner or outer terms. For a correction exp(b tau)sum_i E_i tau^i, the unique coefficients matching the endpoint jet are

E_i=sum_{j=0}^i (-b)^(i-j)(J_j-P_j)/[(i-j)! j!].

This follows by multiplying the Taylor expansion of the jet difference by exp(-b tau) and equating coefficients. The diagonal coefficient of E_i in the i-th derivative is i!, so uniqueness also follows by a triangular solve. Set b=bi for the inner correction and b=-bo for the outer. Since the endpoint spline jets and all exponents are exact rational numbers, these coefficients are exact rational functions of the inputs for any fixed rational outer A coefficients.

## Exact central strain and normalization slope

The density-mode formula for the canonical strain gives

c=integral_0^infinity r [a_0(r)/4+a_1(r)/8-a_2(r)/8-a_3(r)/8] dr.

The projection follows by multiplying cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4 by cos(2m theta) and selecting the sin(3theta) coefficient; the central strain is the integral of that coefficient divided by r^2. The derivative-free density Green proof is in ../canonical_inverse/PROOF.md and ../axis_inverse/PROOF.md. No modes m>=4 contribute. Every integral converges, since the inner functions are bounded and every outer alpha_q<-2.

Vary only A_00 by a real amount z, recomputing the exact outer correction of mode zero so that all six derivatives and the value remain fixed at t_+. Write alpha=alpha_0. The resulting mode-zero change for tau>=0 is exactly

z B(tau),
B(tau)=exp(alpha tau)-exp(-bo tau)sum_{i=0}^6 [(alpha+bo)tau]^i/i!.

Its central-strain slope is

s=exp(2t_+)/4 integral_0^infinity exp(2tau)B(tau) d tau
 =exp(2t_+)/[4(-alpha-2)] [(alpha+bo)/(bo-2)]^7 >0.

To prove the formula, integrate each exponential monomial: integral_0^infinity exp(-(bo-2)tau)tau^i/i! dt=(bo-2)^(-i-1), and integral exp((alpha+2)tau)dt=1/(-alpha-2). The finite geometric sum then gives the displayed seventh power. Positivity follows from alpha<-2, bo>2 and alpha+bo>0. It also follows pointwise because exp((alpha+bo)tau) exceeds its sixth Taylor polynomial for tau>0.

Let c0 be the canonical strain of the exactly joined trial before this scalar correction. Define

z=(3/k-1-c0)/s,
A_00_star=A_00+z,

and recompute the outer correction by the exact join formulas. Then c_star=c0+s z=3/k-1 exactly, and c_l=1/k satisfies 3c_l-c_star=1. The division is justified by the proved positive slope. The number z, the resulting A_00_star, and the recomputed mode-zero outer join coefficients are exact real numbers defined by convergent integrals and arithmetic. They need not be rational. A ball enclosing z is not an exact replacement for this definition. Every downstream enclosure must be uniform over that ball or independently recompute a narrower enclosure of the same exact value.

## Admissibility and residual scope

The angular sum is finite. Near zero its nonconstant core terms are homogeneous of degree 2j and smooth on the unit circle; they need not be Cartesian polynomials. After multiplication by x^2y, the smallest nonconstant homogeneous degree is five, so the density is C^{2,alpha} for every alpha<1, with continuous factor tending to one. The inner logarithmic corrections have radial power bi; the assumed bi>4 makes the factor continuous and the density C^{2,alpha} for every alpha<1, even after up to two derivatives of the finite logarithmic powers. The joins are C^6 in log radius and therefore in physical radius away from zero. Interior simple knots give C^6 spline regularity. At infinity the leading density grows like r^k, with its first derivative O(r^(k-1)). The canonical sublinear velocity exists and is unique by the kernel proof in ../trial_regularities/PROOF.md.

Consequently this exactified density satisfies the kinematic conditions of P_2 with exact center normalization and exponent matching; it has not been shown to satisfy the stationary equation required for P_2 membership. It is not claimed to satisfy transport. Its far leading linear transport term vanishes at c_l=1/k. Here is a qualitative bound for the remaining residual, without a numerical constant. The finite list of exponents satisfies alpha_q <= 2k-4 for q>0; the verifier checks this exactly. Thus rho=r^k Theta(theta)+O(r^(2k-1)), with differentiated versions of this estimate. The outer join correction has density power 3-bo<2k-1, so its finitely many logarithms are absorbed in the remainder. For each even stream mode m>=2, the density-mode Green formula uses

J_m=r^(m-1) integral_r^infinity t^(-m) a_{m+1}(t) dt,
I_m=r^(-m-1) integral_0^r t^m a_{m-1}(t) dt,

where a_j are the odd angular density coefficients. The bounds a_j=O(r^k) imply J_m=O(r^k), since m-k-1>0, and I_m=O(r^k)+O(r^(-m-1)). There are finitely many modes. Oddness of the stream function in both Cartesian coordinates allows only sin(2n theta), n>=1; hence there is no zero stream mode. The canonical sublinear condition excludes the affine velocity from a harmonic xy term. The local density term in the tangential velocity is also O(r^k), so U=O(r^k). Therefore U dot grad(rho)=O(r^(2k-1)), while (k^(-1)r partial_r-1)rho=O(r^(2k-1)). The unweighted residual tends to zero at infinity because k<1/2. These are asymptotic bounds for the exact definition, not validated finite residual constants. A quantitative residual norm, a distance to X3, and a full inverse estimate are separate obligations.

## Numerical verification method

The companion verifier projects the four relevant spline modes in exact rational arithmetic, reconstructs each cell by an independent Cox recurrence, and integrates exp(2t) times that polynomial using the stable scaled-series moments and proved tails from ../exponential_moments/PROOF.md. This is different from the numerics lane's floating least-squares constraints and Arb primitive subtraction. The independent exact Cox routine returns coefficients of the local variable t-(a+b)/2: its two recursion factors are (mid-t_i)+z and (t_{i+d+1}-mid)-z. Thus evaluation at z=-(b-a)/2 or +(b-a)/2 gives the appropriate endpoint jet, and the binomial translation in the integration loop correctly moves the expansion to the left endpoint. The rational partition has strictly increasing interior knots. Each full-cell argument satisfies 2(b-a)<1, checked exactly; the moment routine additionally splits using a certified upper bound and asserts the series-tail hypothesis |z|<N+1. Its conversion aa(p/q)=arb(p)/q encloses the exact rational. Thus N=64 obeys the previously proved tail condition with ample margin. All radii and scalar-correction values are recorded as enclosures of the exact definitions above. No large numeral-filled formal source is generated.

## Cost of exactification relative to the common-endpoint literal trial

For j>=1 and b>0, sup_{t>=0} t^j exp(-bt)=(j/b)^j exp(-j), by differentiation; for j=0 the supremum is 1. Denote this number by E_j(b). Let R_-=exp(t_-) and R_+=exp(t_+). Write W(r)=(1+(r/L)^2)^((k-3)/2). For any factor difference h=x^2 y delta a define its factor norm as sup_{r,theta}|delta a(r,theta)|/W(r), with values on the axes interpreted by the explicit factor formula. If Delta Ei_mj and Delta Eo_mj are the exact jet coefficients minus the stored ones, then the factor-norm change caused by the joins is at most

sum_{m,j}|Delta Ei_mj| E_j(bi)/W(R_-) + sum_{m,j}|Delta Eo_mj| E_j(bo-(3-k))/W(R_+).

For the inner part, W(r)>=W(R_-) when r<=R_-. For the outer part W(R_+)/W(R_+ exp(t))<=exp((3-k)t). These two inequalities and the triangle inequality over angular modes prove the bound. The scalar correction costs at most |z|/W(R_+), since 0<=B(t)<=exp((k-3)t). These are distances to the literal modal formula with the same exact knot endpoints. They are not distances directly to X3; no sampled fit error is upgraded to a rigorous bound.

## Independent Gaussian verification

A second calculation of all scalar integrals uses exact derivative B-spline coefficients and mpmath.iv at 85 decimal digits. It neither imports the Cox polynomial reconstruction nor the exponential-moment routine. If a degree-p B-spline has coefficients c_i and knots t_i, differentiation gives coefficients

d_i=p(c_{i+1}-c_i)/(t_{i+p+1}-t_{i+1})

on the knot vector with its first and last entries removed. This follows by differentiating the defining B-spline recursion and collecting adjacent terms. Repeat through order seven. On original span i, the j-th derivative has active coefficient indices i-7 through i-j. B-spline nonnegativity and partition of unity therefore bound its absolute value by the maximum absolute value of these exact coefficients. Clamping makes the endpoint value equal the first or last active coefficient, so the same recurrence independently supplies all endpoint jets and join corrections.

For each span [a,b], put F(t)=exp(2t)S(t), where S is the four-mode projection. The Leibniz formula gives

sup |F^(24)| <= exp(2b) sum_{j=0}^7 binom(24,j) 2^(24-j) max_active |S_j|.

The twelve-node Gaussian rule on an interval of length h has error at most

h^25 (12!)^4/[25(24!)^3] sup |F^(24)|.

To obtain this constant, subtract the degree-23 Hermite interpolant at the twelve roots, each counted twice. Its pointwise error is F^(24)(xi) pi_12(t)^2/24!, where pi_12 is the monic nodal polynomial. Integrating its square, using Legendre orthogonality and the leading coefficient of P_12, gives the displayed constant. This argument holds on each closed spline span because its polynomial extension is smooth there; derivatives across different spans are not used.

Each Gaussian root is enclosed by exact dyadic endpoints with opposite exact signs of P_12; all twelve intervals are disjoint and contained in (-1,1), hence they cover exactly the twelve roots. The weights 2/[(1-x^2)P_12'(x)^2] are evaluated by mpmath.iv from those enclosures. De Boor's point recurrence encloses the spline at each node. The full sum and the explicitly accumulated Gaussian remainder use mpmath.iv, including exp at every endpoint. The inner and outer integrals are independently formed from exact rational monomial integrals. The slope, scalar correction, and both global factor costs are then recomputed in that engine.

The first full run used 320-bit Arb, 64-term moments, and 1558 spans, and checked all 3640 endpoint jet identities exactly. The second used Gauss12 and 85-digit mpmath.iv on all 1558 spans. Their strain, positive slope, scalar correction, and factor-cost intervals overlap. The evidence files retain exact dyadic endpoints for the second method. Agreement is additional evidence; soundness rests on the preceding separate remainder arguments and their source audits.

## Final audit and public bounds

The exact input, both executed source files, and the prior audited Cox and moment sources are hash-pinned in evidence/audit_verdict.json. Additional exact checks establish the degree, modal count, validity and distinctness of all exponent pairs, and every exponent inequality above. The original run files retain their pre-audit status for provenance; the separate dated audit verdict supersedes that status only for the stated claim.

Both interval calculations imply c0 in [15.7260878319246786225638146971829, 15.7260878319246786225638146971831] and z in [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20]. The join cost is below 4.076e-10, the scalar cost is below 3.562e-13, and their sum is below 4.080e-10 in the weighted factor norm. The last bound concerns the common-endpoint literal modal trial, not X3.

The two implementations differ in endpoint-jet reconstruction, middle integral evaluation, and interval engines. They share the exact input and the analytic join, slope, outer and inner integral, and cost formulas. Agreement tests those implementations and arithmetic; the shared formulas rely on the proofs above. The second script compares scalar outputs, not every individual join coefficient. Python integer and Fraction arithmetic and the outward arithmetic implementations of python-flint/Arb and mpmath.iv are trusted computational dependencies. No formal verification of either numerical library is claimed.

Actual Claude Opus 5.5 accepted the formulas and Gaussian remainder, after follow-up on the exact-real dependent coefficients. Its qualifications about shared formulas, extra input checks and arithmetic trust were verified and incorporated. No transport residual, linear inverse, closing inequality or existence verdict follows.
