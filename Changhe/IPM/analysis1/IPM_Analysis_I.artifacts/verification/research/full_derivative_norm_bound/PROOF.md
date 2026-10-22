# Direct whole-plane derivative residual norms for the canonical modal trial

Status at writing: OPEN. This proof is written before implementation. Its numerical application requires complete canonical radial Taylor-model identification, all declared new checks, two independent exact convolution methods, two interval integrations and actual second-model review followed by a later own adjudication. No old physical W target is presumed or enlarged. Any new bound may be coarse.

## Exact statement and dependencies

Use the exact normalized finite modal trial rho, its canonical full-plane velocity U and the constants k,L,c_l=1/k of derivative_end_tails/PROOF.md. Let eps=(c_l X+U).grad rho-rho, t=log r and D=d/dt. The norm is

    ||f||_X^2 = integral [f^2+r^2|grad f|^2] w(r) dX,
    w(r)=L^6 r^-6 (1+r^2/L^2)^(3/2-k).

We compute bounds for ||eps||_X and ||eps-D eps||_X. The density has odd sine frequencies at most nu=521, the stream has even frequencies at most M=522, and eps and all its t derivatives have odd frequencies at most Omega=1043.

The exact middle annulus a<=t<=b has7809 adjacent cells [t_i,t_(i+1)]. The accepted full canonical radial linkage must identify the actual density factor Taylor boxes and canonical P_n,R_n models on every cell. Its stated conditional version is insufficient. On each cell put u=t-t_i, d=t_(i+1)-t_i and h>=d, with522h<1. The scalar interval [e0,e1] contains exp(t_i) and is strictly positive. The actual degree12 P,R coefficient boxes and uniform remainder budgets must have exactly the hashes in the full accepted radial run, as must the original T factor arrays and scalar row. An actual incomplete run is not a premise.

For the middle region write

    rho=r^3 sum_(j=0)^261 H_j(u) sin((2j+1)theta), H_261=0,
    U_r/r=-sum_(n=1)^261 P_n(u) cos(2n theta),
    U_theta/r=sum_(n=1)^261 R_n(u) sin(2n theta).

Each H_j is a polynomial of degree7 whose coefficient intervals come from the exact signed angular map of T. Its interval center and radius are exact dyadics, not the result of an unchecked floating angular transform. The canonical forcing satisfies

    partial_x rho=r^2 sum_n F_n(u)sin(2n theta),
    F_n=[(4-2n)H_(n-1)+(4+2n)H_n+H'_(n-1)+H'_n]/2.

These identities are independently reconstructed using signed sine scattering and the polar derivative formula. The canonical Green equations imply

    P'=-2P+mR, R'=mP-2R-r^2F, m=2n.                    (1)

All input membership and continuity claims are inherited only after their entire fixed parent pin maps and exact array linkage are checked. The canonical trial is C5 away from0 across the spline joins, by the accepted exact annular regularity theorem. The proof below does not establish an inverse or a nonlinear estimate in this norm.

## True velocity jets without differentiating a remainder bound

Let P^c,R^c denote the degree12 center polynomials in the accepted coefficient boxes. Their uniform errors on[0,h] are bounded, mode by mode, by

    eP_n=sum_l rad(P_(n,l)) h^l + rem(P_n),
    eR_n=sum_l rad(R_(n,l)) h^l + rem(R_n).

These are bounds on the functions only. The velocity derivatives are obtained instead from(1). Their polynomial parts and forcing parts are

    P^[0]=P,                         R^[0]=R,
    P^[1]=-2P+mR,                    R^[1]=mP-2R-r^2F,
    P^[2]=(4+m^2)P-4mR-m r^2F,
    R^[2]=-4mP+(4+m^2)R-r^2F'.                        (2)

For the last identity, D(r^2F)=r^2(2F+F'), which cancels the2r^2F term from-2R'. Thus no derivative of a uniform Taylor-model remainder is assumed. Define A_l(P,R) and B_l(P,R), l=0,1,2, to be the polynomial parts of P^[l],R^[l] in(2). Their center polynomials substitute P^c,R^c. Their uniform errors follow from the displayed linear maps, for example

    eA_1=2eP+m eR, eB_1=m eP+2eR,
    eA_2=(4+m^2)eP+4m eR,
    eB_2=4m eP+(4+m^2)eR.

Let H^[p]=(D+3)^p H, p=0,1,2,3. Its center coefficients are obtained by exact polynomial differentiation before summing coefficient absolute values. Its error coefficients are the sums of the absolute linear weights times the original H radii. The identity D^p rho=r^3 H^[p] follows term by term. The second implementation checks each center derivative by repeated differentiation plus multiplication by3. Angular derivatives multiply each sine mode by its exact frequency.

Define the Wiener norm of a real angular polynomial as the sum of its complex Fourier coefficient magnitudes. For a pure sine or cosine series this equals the sum of the magnitudes of its real sine or cosine coefficients. It is submultiplicative, by the convolution formula and triangle inequality. For any polynomial center C(u,theta)=sum_(q,l)c_(q,l)u^l e^(iqtheta), its whole-cell Wiener bound is sum_(q,l)|c_(q,l)|h^l. Weighted sums with|q| give a theta-derivative bound. No value at a finite set of radii is used as a supremum.

## Exact finite residual polynomials

Applying Leibniz's rule directly to the residual gives

    D^p eps = c_l D^(p+1)rho-D^p rho
       +sum_(l=0)^p binom(p,l)
          [D^l(U_r/r)D^(p-l+1)rho
           +D^l(U_theta/r)partial_theta D^(p-l)rho].    (3)

There are two radial factors in(3): r^3 times a polynomial expression in H and the polynomial velocity parts, and r^5 times a polynomial expression in F,H. Write their exact center versions as V_p(u,theta),W_p(u,theta), so the centered expression is r^3 V_p+r^5 W_p. Both are odd sine series. The degree bounds are19 for V_p and14 for W_p. The forcing terms are explicitly

    W_0=0,
    W_1=-[sum F_n sin(mtheta)] partial_theta H^[0],
    W_2=[sum mF_n cos(mtheta)]H^[1]
         -2[sum F_n sin(mtheta)]partial_theta H^[1]
         -[sum F'_n sin(mtheta)]partial_theta H^[0].    (4)

Here H^[p] denotes its sine series and all factors in(4) use their center polynomials. The signs in(4) use U_r/r=-P and U_theta/r=R. This is independent of any saved derivative residual polynomial.

One implementation forms all polynomial products with signed complex Fourier coefficients. For positive odd frequency q the coefficient of H is-i H_q/2, and at-q it is+i H_q/2. The cosine velocity coefficient is-P_n/2 at both signs of m; the imaginary coefficient of the sine velocity is-R_n/2 at+m and+R_n/2 at-m. Angular differentiation multiplies a Fourier coefficient by iq. Keeping the imaginary numerator of a pure sine series produces real rational convolution arrays. A real sine coefficient is-2 times its positive-frequency imaginary numerator.

A jet polynomial encodes derivatives by coefficients f^[p]/p! at z^p, p<=2. Multiplying two such polynomials and taking p! times the coefficient of z^p gives precisely the Leibniz sum in(3). Terms of degree3 and4 in z are discarded only after multiplication; they cannot affect degrees0,1,2. The linear density terms are added exactly. The independent identity check compares these jet coefficients with direct binomial sums at every mode and degree occurring in the input construction, including the forcing terms(4).

The scalar c_l is rational. Every input coefficient is dyadic. Common powers of2 and a fixed positive integer denominator can therefore clear all denominators before multiplication. The common scale is retained exactly and never rounded. The signed angular indices are shifted into nonnegative indices; the sum of the two shifts is subtracted on extraction. In a one-variable encoding, the radial stride exceeds the largest radial degree of any product, and the angular stride exceeds every radial-and-jet index. Consequently the coefficient map is injective on every product support. A carry into another formal variable is impossible by these degree inequalities. These inequalities and the recovered frequency and radial ranges must be checked for every actual array shape.

## Two independent exact convolution methods

Method A multiplies integer polynomials directly using flint fmpz_poly. Method B reduces the same declared integer input coefficient arrays modulo several pairwise coprime positive odd moduli less than2^63, multiplies with nmod_poly, and reconstructs signed coefficients by an independently coded integer Chinese remainder algorithm. The moduli need not be prime: convolution is valid in each ring Z/mZ, and Chinese remainder uniqueness requires pairwise coprimality only.

For inputs x,y, every product coefficient has absolute value at most

    C=min(length(x),length(y))*max_i|x_i|*max_j|y_j|.

Choose a product of pairwise coprime moduli Q>2C. Chinese remainder reconstruction gives one residue r in[0,Q); interpret r as r when2r<Q, and as r-Q otherwise. The true coefficient is an integer in[-C,C], so this representative is uniquely the true coefficient. This proves the second method without assuming a floating FFT error estimate. GCD tests, modular input residues, the strict product bound and reconstruction congruences are exact. Negative coefficients and zero polynomials must be included in manufactured tests. Every coefficient of every actual product must agree with the direct integer method; sampling is insufficient. The implementations may share the mathematical input arrays but may not import one another's output coefficients.

The new proof depends on exact integer and modular library multiplication, as ordinary exact arithmetic dependencies. It does not describe two calls to the same integer multiplication as independent methods. The modular algorithm reconstructs through a different ring computation and its own CRT implementation.

## Certified errors of the centered expression

For any two true factors A,B with center factors A_c,B_c and uniform Wiener errors eA,eB, submultiplicativity gives

    ||AB-A_c B_c||_W
       <= eA(||B_c||_W+eB)+||A_c||_W eB.              (5)

Apply(5) to every term of(3) using the polynomial velocity parts in(2). Include the linear density error |c_l|eH^[p+1]+eH^[p]. Summing with the exact binomial factors gives a nonnegative bound dV_p for the error of V_p. Applying(5) to the four products in(4), with its coefficient2 where present, gives dW_p. Bounds for mF, F' and theta H use their exact integer mode or polynomial derivative weights before evaluating the positive sums. All center Wiener norms in this paragraph are bounds on the entire cell[0,h]. Both interval engines independently evaluate every positive sum. The error bounds include the original coefficient radii, uniform P/R remainder budgets and every mixed error product.

The same residual-frequency bound Omega applies to the error: exact and centered expressions both have only odd frequencies at most1043. Thus the theta derivative of an error is bounded by Omega times its Wiener bound, without differentiating a radial inequality.

## Combining r^3 and r^5 before taking absolute values

Let z0=e0^2, z1=e1^2, zc=(z0+z1)/2 and ze=(z1-z0)/2, all exact positive rational quantities with ze>=0. Choose the fixed integer J=12 and

    T_J(u)=sum_(j=0)^J (2u)^j/j!,
    R_J=exp(2h)(2h)^(J+1)/(J+1)!.

Taylor's integral remainder gives |exp(2u)-T_J(u)|<=R_J on[0,h]. Form the exact polynomial

    G_p=V_p+zc T_J W_p, degree at most26.               (6)

Its coefficients are combined before their magnitudes are summed. The common-factor division is exact. The true residual satisfies

    ||D^p eps-r^3 G_p||_W <= r^3 d_p,
    d_p=dV_p+z1 exp(2h)dW_p
          +[ze exp(2h)+zc R_J]||W_p||_W.              (7)

Indeed r^2=exp(2t_i)exp(2u); split its discrepancy from zc T_J into the scalar interval error and exponential Taylor remainder, then use(5) and the actual centered W_p norm. This accounts for all scalar-exponential correlation by a valid overestimate. The theta error is at most Omega d_p.

Let g_p=sum_(q,l)|G_(p,q,l)|h^l and gtheta_p=sum_(q,l)|q G_(p,q,l)|h^l, where the sums use complex coefficients, or equivalently the corresponding real sine sums with the factor2 explicitly restored. Set

    B_p=e1^3 exp(3h)(g_p+d_p),
    C_p=e1^3 exp(3h)(gtheta_p+Omega d_p).

Then ||D^p eps||_W<=B_p and ||partial_theta D^p eps||_W<=C_p everywhere in the true cell, p=0,1,2. Only C_0,C_1 are needed in the final norms. These are physical derivative bounds, obtained from the ODE and exact products, not from derivatives of a zero-order residual majorant.

## Exact radial norm integration on the middle annulus

The full-circle sine/cosine Parseval identity gives integral |f|^2 dtheta<=pi||f||_W^2. Also r^2|grad f|^2=|D f|^2+|partial_theta f|^2. In t coordinates the radial weight is

    v(t)=exp(2t)w(exp(t))
        =L^6 exp(-4t)(1+exp(2t)/L^2)^(3/2-k).

Its logarithmic derivative is -4+(3-2k)exp(2t)/(L^2+exp(2t)), which is strictly negative because0<k<1/2. Therefore integral_(t_i)^(t_(i+1))v(t)dt<=d v(t_i), using the exact true width d, not a rounded inward width. The two middle norm squares are bounded by

    pi sum_i d_i v(t_i)[B_0^2+B_1^2+C_0^2],
    pi sum_i d_i v(t_i)[(B_0+B_1)^2+(B_1+B_2)^2+(C_0+C_1)^2]. (8)

Every scalar exponent, power and sum in(7)-(8) is evaluated with Arb512 and independently with mpmath.iv200. Scalar target intervals are not imported as unchecked real values. The exact geometry agrees with all original partition knots and the accepted radial run. Entire coverage, no gaps and common canonical data are mandatory.

## Infinite inner and exterior regions

This part repeats the analytic derivative-tail formulas on r<=exp(a) and r>=exp(b), so no finite collar is omitted. The accepted topic178 statement at a-5,b+17 alone would not cover these regions.

For the inner density remainder eta=rho-x^2 y, use the exact coefficients c_(j,lambda,l) from inner_majorant and their exact differentiated coefficients

    c^[p]_(j,lambda,l)=sum_(q=0)^p binom(p,q)(3+lambda)^(p-q)
                                (l+q)!/l! c_(j,lambda,l+q), p<=3.

For lambda>2 put x=l/(lambda-2) and M_(lambda,l)=x^l exp(-(lambda-2)x), with0^0=1. At lambda=2 only l=0 occurs and M=1. Differentiating x^l exp(-(lambda-2)x) proves that this is the maximum on x>=0. Define

    dH_p=exp(-2a)sum_(j,lambda,l)|c^[p]_(j,lambda,l)|M_(lambda,l).

Then ||D^p eta||_W<=dH_p r^5 on the entire inner disk. The accepted T=0 constants C_r,C_theta bound the strain-subtracted normalized velocities by C_r r^2,C_theta r^2. Apply the Green recursions and residual formulas of topic178 with R_i=exp(a), replacing its d_p by these dH_p. Explicitly, F0=1+R_i^2(dH1+nu dH0), F1=2+R_i^2[dH2+(nu+1)dH1+nu dH0], s0=C_r,q0=C_theta, s1=2s0+M q0,q1=M s0+2q0+F0, s2=2s1+M q1,q2=M s1+2q1+F1. For p=0,1,2,

    b_p=|c_l|dH_(p+1)+dH_p+|3/k-1|(dH_(p+1)+nu dH_p)
        +sum_(l=0)^p binom(p,l)3^(p-l)[(3/2)s_l+q_l]
        +R_i^2 sum_(l=0)^p binom(p,l)[s_l dH_(p-l+1)+q_l nu dH_(p-l)].

The same exact cubic cancellation, ODE identities and Leibniz rule prove ||D^p eps||_W<=b_p r^5. Set CI=pi L^6(1+R_i^2/L^2)^(3/2-k)R_i^6/6. The inner norm squares are bounded by CI[(1+Omega^2)b0^2+b1^2] and CI[(1+Omega^2)(b0+b1)^2+(b1+b2)^2]. The O(r^5) function and O(r^4) gradient estimates justify extension of the weak derivative across0; the boundary term is O(delta^6).

For the exterior inherit the entire accepted coefficientwise majorant from topic178, not merely a pointwise bound. With tau=t-b>=0, each exponent gamma<0 and coefficient C_(gamma,l)>=0 bounds the sum of absolute residual coefficients. Its derivative coefficients are

    C^[p]_(gamma,l)=sum_(q=0)^p binom(p,q)|gamma|^(p-q)(l+q)!/l! C_(gamma,l+q).

Put CO=L^(3+2k)exp(-(1+2k)b)(1+L^2 exp(-2b))^(3/2-k), sigma=1+2k-2gamma>0. The exact integral is integral_0^infinity tau^(2l)exp(-sigma tau)dtau=(2l)!/sigma^(2l+1). Define Lp=sum C^[p]_(gamma,l)sqrt(CO (2l)!/sigma^(2l+1)). Minkowski and Parseval give exterior norm squares pi[(1+Omega^2)L0^2+L1^2] and pi[(1+Omega^2)(L0+L1)^2+(L1+L2)^2]. The second engine uses J0=1/sigma and Jn=(n/sigma)J_(n-1), independently of the factorial formula.

The coefficient derivatives, inner maxima and all tail integrals must be recomputed completely with both methods for these new endpoints. An accepted result at a different cutoff is not substituted.

## Final criterion, audit and scope

Add the two end squares and the complete middle sums(8), then take square roots with outward rounding. Any displayed terminating decimal is strictly larger than the upper endpoint from both independent interval engines. No old target bound is increased and then called verified; this is a new direct norm enclosure, whose magnitude and limitations are reported honestly.

The exhaustive stream records every exact cell endpoint, linked candidate-array hashes, modular moduli and strict reconstruction bound, product sizes and whole-coefficient equality counts, positive bound enclosures, and completed integration sums. It has immutable source and parent pins, a unique ordered row per cell and a final footer. Missing or duplicate cells, changed sources, nonfinite arithmetic, an inward scalar interval, a missing Fourier factor, a negative error radius, a failed CRT comparison or an incomplete canonical parent leave the result OPEN. A second output auditor must validate complete saved coverage and comparisons, regenerate an explicitly declared set of full cells including both ends and any restart neighbors, and check the final sums by a separately ordered reduction. Selected replay supplements, rather than replaces, full two-method coverage.

The underlying functions are C1 across all interfaces; the two circles have measure zero. Thus the three-region norm-square addition is legitimate. This establishes only numerical bounds for eps and eps-D eps of the exact canonical modal trial in the stated weak weighted H1 norm. It is neither a norm distance to the published X3 nor an inverse estimate. The weak graph nonlinear discontinuity result remains valid and prevents treating this norm calculation as a nonlinear closing estimate. No IPM existence or exclusion endpoint follows on its own.
