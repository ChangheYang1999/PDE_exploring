# Analytic leading data with prescribed harmonic multipoles

Status: CONFIRMED after independent theory-part review at2026-10-31T05:22Z and the follow-up check below. Written on 2026-10-31. This extends the independently reviewed finite-polynomial theorem in topic58. The result is local in the exterior; no stationary interior extension is asserted.

## Statement and notation

Let 0<delta<1, c=1/(1-delta), gamma=1-delta, and suppose alpha=delta/2 is irrational with finite Brjuno sum Bcal. Write d_n=dist(n delta,2Z). Fix sigma_0>0 and a nonzero real S1 leading profile f with

    F=||f||_(A_sigma_0)<infinity,
    ||a||_(A_sigma)=sum_m |a_hat(m)| exp(sigma |m|).

Prescribe real h_k, k>=2, satisfying H_0(Y_0)=sum_(k>=2) k|h_k|Y_0^k<infinity for some Y_0>0. Use the mixed indices I=(n,k), n>=1,k>=0, and

    mu_I=n delta+2k,  p_I=1-mu_I,  P_I=2-mu_I,  w_I=n+k.

The density and generated-stream recursion is precisely topic58, equations(1)-(2), with F_(1,0)=f and prescribed independent stream G_(0,k)=h_k sin((2k-2)theta). It defines a unique analytic coefficient at every index. There are X,Y>0 such that, for every R>1 satisfying

    R^(-delta)<(sigma_0/2)X,    R^(-2)<(sigma_0/2)Y,

its density, stream and original potential series converge absolutely on r>=R, uniformly with every fixed Cartesian derivative in its natural radial weight. The sums are real analytic in the exterior and solve the exact stationary potential IPM equation. Their explicit form, including the term -h_2 log r in the potential, is the form in topic58 with analytic angular coefficients. The leading density is r^gamma(f+o(1)).

Here is one explicit sufficient choice. Set

    C_P=(1+delta^(-1))/2,   Lambda=1+2 C_P=2+delta^(-1),
    K=2 exp(sigma_0) Lambda(1+2 sigma_0)/(c-1),
    F_*=2 exp(2 Bcal) F,
    H(y)=sum_(k>=2) k|h_k| sigma_0^(k-1)
                          exp((2k-2)sigma_0) y^k.

The series H has a positive radius and equals

    H(y)=exp(-2 sigma_0) H_0(sigma_0 exp(2 sigma_0)y)/sigma_0.

Choose 0<Y<Y_0 exp(-2 sigma_0)/sigma_0 with H(Y)<1/(16K), and put X=1/(16K F_*). These numbers depend only on the displayed norms, delta and its Brjuno sum. There is no claim that the sufficient radius is sharp.

## 1. Uniform stream estimates with two indices

All Poisson divisors are nonzero because n>=1 and delta is irrational. In physical sine amplitudes, a density coefficient at frequency m-1 or m+1 contributes to the stream at an even frequency m>=2 through

    b_m=-a_(m-1)/(2(m+P_I))+a_(m+1)/(2(m-P_I)).

The first denominator has modulus at least d_n, since mu_I-n delta is even; the second is m-2+mu_I>=mu_I>=n delta. Frequency shifts cost at most exp(sigma) in A_sigma. Thus

    ||G_I||_sigma <= exp(sigma_0) C_P ||F_I||_sigma/d_n.       (1)

Both 0<mu_I<=2w_I and |P_I|<=2w_I hold for every density index. Therefore

    |P_I| ||G_I||_sigma
       <= exp(sigma_0) 2 C_P w_I ||F_I||_sigma/d_n.

To control an angular derivative, use m<=|m+P_I|+|P_I| and m<=(m-P_I)+|P_I| in the two channels. Summing the two channel estimates for each input coefficient gives at most

    exp(sigma) [1+|P_I|(1/d_n+1/(n delta))/2].

Since d_n<=1 and n>=1, this is bounded by exp(sigma_0) Lambda w_I/d_n. Consequently

    max(|P_I| ||G_I||_sigma, ||partial_theta G_I||_sigma)
       <= exp(sigma_0) Lambda w_I ||F_I||_sigma/d_n.          (2)

This estimate does not use finite angular support. The absolute Fourier sums justify the coefficientwise passage to analytic data.

## 2. The shrinking-strip norm

Put s=sigma_0-sigma and define

    nu_I=sup_(0<=sigma<sigma_0) s^(w_I-1)||F_I||_sigma.

The elementary Nagumo estimate proved in topic14 states: if ||a||_sigma<=nu s^(-ell), then

    ||a'||_sigma <=(ell+1)nu s^(-ell-1),                     (3)

including ell=0. Thus a right density child D satisfies ||F_D'||_sigma<=w_D nu_D s^(-w_D).

For a prescribed stream child A=(0,k), define

    nu_(0,k)=|h_k| sigma_0^(k-1) exp((2k-2)sigma_0).

Its exact single-frequency expression gives

    max(|P_A|||G_A||_sigma, ||G_A'||_sigma)
       <=2k nu_(0,k) s^(-(k-1)).                           (4)

Indeed s<=sigma_0 and its frequency and |P_A| both equal 2k-2. For generated stream children use (2), with the bound defining nu_A.

For every right density child, |p_D|<=2w_D. In the stationary recursion the first nonlinear term therefore has strip power s^(-(w_I-1)), while the second has power s^(-(w_I-2)). Bounding its additional factor s by sigma_0 gives

    (c-1)(w_I-1) nu_I
      <= exp(sigma_0) Lambda(1+2 sigma_0)
          sum_(A+D=I) w_A w_D nu_A nu_D / e_A,              (5)

where e_A=d_(n_A) for a generated child and e_A=1 for a prescribed child. The coefficient exp(sigma_0)Lambda is at least2, so it also dominates (4). The induction begins with nu_(1,0)=F. At every fixed index the children have smaller w and are finite in number, so (5) also proves that nu_I is finite.

Let Z_I=w_I nu_I for density indices and Z_(0,k)=k nu_(0,k) for prescribed streams. Multiplying (5) by w_I/((c-1)(w_I-1)) in its solved form and using w_I/(w_I-1)<=2 yields

    Z_I <=K sum_(A+D=I) Z_A Z_D/e_A.                       (6)

The inverse divisor again belongs only to a generated stream child. The angular derivative has not introduced an additional divisor or an additional tree mark.

## 3. The same marked-tree estimate

Use the exact trees and marked nodes of topic58. An admissible density tree with n leading-density leaves and s independent-multipole leaves has n+s-1 interactions and n-1 marked nodes. Each mark supplies a factor d_(n_v)^(-1). A marked proper descendant has strictly smaller density mass. Adding an output-root mark preserves that property and gives n marks.

The Brjuno packing lemma from topics13 and58 therefore gives, with M=n-1 or M=n,

    product_(marks v) d_(n_v)^(-1)<=2^M exp(2n Bcal).       (7)

In (6), the stream multiplier constants have already been absorbed in K. There are no further C_P factors at the internal nodes. The positive analytic solution

    W=F_* x+H(y)+K W^2,
    W(x,y)=(1-sqrt(1-4K(F_*x+H(y))))/(2K)                  (8)

majorizes all allowed tree weights; its extra tree shapes only increase coefficients. Equation(7), also with the output-root mark, proves

    w_I nu_I <= [x^n y^k]W,
    w_I nu_I/d_n <= [x^n y^k]W.                           (9)

Combining (1) with (9) also gives

    w_I sup_sigma s^(w_I-1)||G_I||_sigma
         <=exp(sigma_0) C_P [x^n y^k]W.                   (10)

The selected X,Y satisfy F_*X+H(Y)<1/(8K). Hence W is analytic on a neighborhood of the closed polydisc |x|<=X,|y|<=Y, and its nonnegative coefficient sum there is finite.

## 4. Potential reconstruction and convergence

For every index, mu_I is not an even integer. The infinite-angular potential inverse in topic14 applies with n delta replaced by mu_I. For mu_I>=3, its bound is

    ||C_I||_sigma <=(3/|4-mu_I|+1)||F_I||_sigma/d_n.       (11)

All small distances from mu_I to an even integer are at least d_n. Only finitely many indices have mu_I<3 or |4-mu_I|<1. For these indices the downward recurrence for the density-to-Laplacian inverse has at most polynomial growth in the angular frequency. An arbitrarily small strip decrease makes it bounded, exactly as established by equations(6)-(8) of topic14. The subsequent angular Laplacian inverse has no kernel. This reconstructs a unique even analytic potential at each generated index, and its mixed derivative equals G_I by uniqueness of the Poisson inverse.

Evaluate (9)-(10) first at sigma=sigma_0/2, so s=sigma_0/2. For x=r^(-delta), y=r^(-2), the normalized density terms have weights x^(n-1)y^k. Their absolute norm sum at r=R is bounded by the density-index portion of

    (s/x) W(x/s,y/s).

The apparent factor1/x creates no problem: each density index has n>=1, so each actual weight x^(n-1)y^k decreases as r increases. One bounds the sum at R. The strict inequalities in the theorem give a polydisc margin. The generated stream has the same bound times exp(sigma_0)C_P. Equation(11) gives the late potential terms, with a uniform constant outside the finitely many exceptional indices. Those finitely many potential terms are analytic on, for example, sigma_0/4. Thus all three sums converge in that positive strip.

The independent stream and potential multipoles converge there too. Indeed the choice of Y ensures

    R^(-2)<(sigma_0/2)Y<Y_0 exp(-2 sigma_0)/2,

so their angular weights and any fixed polynomial in k are summable with a strict geometric margin. The isolated term -h_2 log r is real analytic for r>0 and obeys its natural weighted derivative bounds.

Each radial differentiation introduces a factor of size at most a constant times w_I and one inverse power of r. The polydisc margin absorbs every fixed power of w_I. Angular differentiation is controlled by decreasing the positive strip once more. Thus every fixed Cartesian derivative converges uniformly on r>=R in the corresponding radial weight, and locally on complex neighborhoods in the exterior. The sums are real analytic.

All identities from the original potential pass to the sums. Absolute convergence permits multiplication and regrouping the stationary series by (n,k), and each coefficient vanishes by its recursion. The leading-density limit follows by dominated convergence. This proves the theorem.

## Scope and dependencies

The proof requires analytic leading data, finite Brjuno sum, and geometrically bounded prescribed harmonic coefficients. It does not prove rational logarithmic convergence, unrestricted stability in delta, or a stationary whole-plane extension. It preserves the same independent multipole parameters as the finite-polynomial theorem. Its new step is the two-index shrinking-strip norm and the stream estimate(2); the tree geometry is unchanged.

Dependencies: the exact recurrence and potential identities in topic01, the Brjuno arithmetic lemma in topic13, the Nagumo estimate and infinite-angular potential inverse in topic14, and the marked-tree proof in topic58. Finite arithmetic checks of the new uniform multiplier constants will be retained alongside this proof; they are checks of the estimates, not substitutes for their derivation.

## Completed finite checks

The exact multiplier audit checks26542 single-mode cases and79626 inequalities, including multipole index1000000 and frequencies adjacent to resonance. All pass. Actual elapsed time was1.0340365539304912 seconds. The results and source snapshot are retained in verification/ and sources/. The independent review confirms the complete theorem. The explicit upper restriction on Y makes the prescribed multipole radius margin immediate from the stated input Y_0.

## Review closure 2026-10-31T05:23:35Z

The theory part independently checked the two-channel derivative bound, the Nagumo powers, the w/(w-1) factor, the marked-tree constants, and the final rescaling. Its one wording observation is resolved by explicitly choosing Y below Y_0 exp(-2 sigma_0)/sigma_0. This is an allowed smaller positive choice and changes no existence claim. The complete argument is CONFIRMED; it may be labeled PROVED. The retained review is in sources/.
