# Whole-plane derivative norms from independent radial Fourier arithmetic

## Exact class and notation

Let the potential, c>1, delta and canonical rational coefficients be as in ../refit_audit/PROOF.md or ../baseline/PROOF.md. Write ell=h+1. The exact residual has the representation

F(r,theta) = r sum_{ell,n} u^(ell delta/2) Q[ell,n](t) sin(n theta),

t=r^2/(1+r^2), u=1/(1+r^2). This follows from the radial Fourier derivation in ../radial_fourier/PROOF.md before division by sin(theta). Every sum below is finite. Derivatives D^d mean the ordered Cartesian derivative tensor; its squared norm is sum_{a=0}^d binom(d,a) |partial_x^a partial_y^(d-a) F|^2.

## Differentiation

For a term r^(1-d) u^(ell delta/2) P(t) T_n(theta), radial differentiation gives

r^(-d) u^(ell delta/2) [(1-d-ell delta t)P + 2t(1-t)P'] T_n.

The angular part of a Cartesian derivative is r^(-d)u^(ell delta/2) times plus or minus nP. Product-to-sum identities split the result into harmonics n-1 and n+1, with the same signs as in ../baseline/PROOF.md. This gives an exact recurrence at every r>0. Each differentiated branch is a finite sum of smooth Cartesian functions. For the present algebra, divisibility by t^floor(d/2) is verified exactly in each angular component. Removing this factor gives the normalized form

partial^alpha F = r^(1-epsilon) sum u^(floor(d/2)+ell delta/2) Q[alpha,ell,n](t) T_n(theta),

epsilon=d mod 2. Equality of the two mixed-derivative paths is checked as a rational polynomial identity. Origin divisibility or commutation failures are errors, not discarded terms.

## Integrability and exact unweighted integration

Convert each normalized Q(t) to Q(1-u) and remove its exact initial factor u^q. An individual squared branch has radial exponent

b = d-3+ell delta+2q

at u=0. Weighting by r^2 decreases b by 1. Weighting by omega^2, omega=(1+4r^2)^(2/5), decreases b by 4/5. If a nonzero branch has b<=-1, the norm diverges unless another branch cancels its leading power. We check that distinct ell values do not differ by an integer after multiplication by delta/2. Under this check such cancellation cannot occur within a fixed harmonic. Angular orthogonality precludes cancellation across harmonics. Thus the diagonal exponent test is both necessary and sufficient for the finite sums used here.

When all exponents pass, each cross term is integrable by Cauchy-Schwarz. Full-circle angular orthogonality gives pi per nonconstant sine or cosine, and 2pi for the constant cosine. The Jacobian gives a further factor 1/2. A cross product of two different branches has multiplicity two. Tensor component multiplicity is binom(d,a).

For a cross term with endpoint orders q and q', the exponent is

b = d-3+(ell+ell')delta/2+q+q',

modified by -1 for an r^2 weight and -4/5 for omega^2. The remaining polynomial contains a factor (1-u) when d is even, and another such factor for an r^2 weight. Therefore the unweighted squared norm is exactly pi/2 times a rational number, because

integral_0^1 u^b sum_k a_k u^k du = sum_k a_k/(b+k+1).

All integration and cancellation are rational operations. Only multiplication by pi and taking square roots use Arb balls.

## Validated omega weight

After the factor u^(-4/5) is extracted, the remaining weight is (4-3u)^(4/5). Put alpha=4/5 and z=3u/4. The binomial series of (1-z)^alpha has negative coefficients at every positive order. Let P_N(u)=sum_{k=0}^N binom(alpha,k)(-3u/4)^k. For 0<=u<=1,

P_N(u)-epsilon_N <= (1-3u/4)^alpha <= P_N(u),

epsilon_N=4 |binom(alpha,N+1)(-3/4)^(N+1)|.

Indeed each ratio of consecutive absolute coefficients in u is less than 3/4, so the omitted absolute sum is at most four times its first term. Multiplication by the nonnegative radial squared angular norm and integration preserves the inequalities. If S is the exact base integral and T_N is its exact polynomial-weighted integral, the weighted squared norm lies between

(pi/2) 4^(4/5) (T_N-epsilon_N S) and (pi/2) 4^(4/5) T_N.

The calculation checks S>=0 and a positive lower bound. This bounds the complete radial axis with no quadrature or tail omission.

## Dependencies and scope

Dependencies are exact radial Fourier identities, elementary integration of u powers, the binomial theorem inside its uniform convergence interval |z|<=3/4, and orthogonality of full-circle Fourier modes. The weight bound uses its own one-sided expansion, distinct from the previous P12 centered expansion. These are norms of the residual, not an inverse bound or an existence proof. The rF norm is an upper proxy for the Hdot^-1 component only after the separate angular Hardy inequality is supplied; this calculation does not identify it with Hdot^-1.

## Harmonic Hardy proxy for Hdot^-1

For an S1-symmetric real residual write F=sum_{n positive odd} f_n(r) sin(n theta). The homogeneous Hdot^-1 norm is the supremum of integral F phi over smooth compactly supported test functions with ||grad phi||_2<=1. Only the same sine harmonics of phi contribute. Fourier orthogonality and Cauchy-Schwarz give

|integral F phi| <= [pi sum_n integral_0^infinity r^3 f_n(r)^2/n^2 dr]^(1/2)
                  [pi sum_n integral_0^infinity n^2 phi_n(r)^2/r dr]^(1/2).

The second factor is the norm of the angular derivative part of grad phi and is at most ||grad phi||_2. Thus the first factor is a rigorous upper bound for ||F||_Hdot^-1, sharper than ||rF||_2. It is computed by the same r-proxy integral with an additional exact factor 1/n^2 for each harmonic. No equality with the actual negative norm is claimed.

## Exact polynomial product acceleration

A finite cosine polynomial with radial polynomial coefficients can be represented as a Laurent polynomial in z=exp(i theta): twice its coefficients are C_n at both z^n and z^(-n), including two copies when n=0. Similarly, 2i times a sine polynomial has coefficients S_n at z^n and -S_n at z^(-n). Their product is antisymmetric, and the coefficient of positive z^n divided by two is the sine coefficient of the original cosine-sine product. This reproduces cos(n theta)sin(m theta)=[sin((m+n)theta)+sin((m-n)theta)]/2, including zero and negative modes.

To multiply the radial polynomials and Laurent angular polynomials in one exact univariate product, first shift all angular exponents to be nonnegative. Encode t^k z^n as X^(k+B n), where B exceeds the sum of the maximum radial degrees of the two factors. Because every radial product has degree strictly below B, no radial coefficient crosses into a neighboring angular block. Unpacking and undoing the angular shifts therefore recovers the exact bivariate product, coefficient by coefficient. This is an algebraic identity, not sampling or floating FFT. The code compares the packed result to the separate product-to-sum loops on all state131 residual components before using the accelerator on larger refits.

The angular shift may be chosen separately for each branch. For branch i, choose c_i as its largest harmonic and encode the exponents n+c_i. A product of branches i,j then has total shift c_i+c_j. Products with the same branch sum and total shift can be added before unpacking; products with different shifts must be unpacked separately and then added at the actual harmonic index. The coefficient at encoded angular index c_i+c_j+n is still twice the required sine coefficient. This removes leading and trailing zero blocks without changing any coefficient. The `packed_tight.py` implementation uses this variant and records an exact comparison against a previously assembled complete residual before use on a new candidate.

## Ball-polynomial evaluation of the same finite integrals

The exact endpoint orders and distinct effective radial exponents are checked with rational polynomials before conversion to interval arithmetic. Thereafter every rational coefficient and exponent is enclosed in an Arb ball. Polynomial multiplication, grouping, division by the positive integral denominators, and summation give an enclosure of the same exact finite expression proved above. A positive lower endpoint is required for every final squared norm.

For the weighted norm let S be the unweighted polynomial integral after the exact factor u^(-4/5) has been included in the exponents, and let H be the integral after multiplication by the upper binomial polynomial W_N. The pointwise estimate W_N-epsilon<= (1-3u/4)^(4/5)<=W_N implies H-epsilon S<= the weighted integral <=H. Although individual grouped polynomial coefficients may be signed, S is the integral of the original nonnegative square and is nonnegative. Ball evaluation of H-epsilon S is therefore a rigorous lower bound and ball evaluation of H is a rigorous upper bound, without discarding cross terms. Roundoff is bounded by interval arithmetic; the only approximation of the analytic weight is the explicitly bounded binomial remainder. The exact-rational mode formula and earlier state131 norm calculations supply separate implementation comparisons.
