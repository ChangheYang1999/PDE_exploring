# Audit of finite-scale radial moment certificates

## Exact statement

Let alpha,beta>-1 be rational. Let z_i be rational in [0,1), and nu_i arbitrary rational, with finitely many factors. Then

    I=integral_0^1 t^alpha (1-t)^beta product_i(1-z_i t)^(-nu_i) dt

admits arbitrarily narrow rigorous enclosures by the geometric-partition Taylor algorithm below. Its inputs and finite polynomial coefficients are exact rationals; positive powers and the final outward error are enclosed with ball arithmetic. This theorem applies to individually integrable moments. A signed combination whose individual terms diverge must be simplified exactly first.

## Independent derivation of the partition and error

Choose J>=2 with 2^-J<=1-z_i for every i. Use partition points 0,1/2,3/4,...,1-2^-J,1. On an interval [l,l+h], write t=l+hx. Extract x^alpha on the first interval and (1-x)^beta on the last, together with their positive constant factors. Every remaining factor is (1+q x)^e times a positive constant.

For an interior left-power factor q=h/l<=1/2. For a nonfinal right-power factor |q|=h/(1-l)=1/2. A denominator factor has |q|=z h/(1-zl). On nonfinal cells, z h/(1-zl)<=h/(1-l)=1/2. On the final cell, l=1-h and h<=1-z imply z h<=1-z, so again z h/(1-z+zh)<=1/2. Thus every analytic factor is regular on the closed complex disk |x|<=3/2, using the branch equal to one at zero.

Let G be their finite product. Its first N+1 Taylor coefficients are obtained exactly by truncated binomial convolution. For real e, the coefficient bound

    |binom(e,k)| <= |e|(|e|+1)...(|e|+k-1)/k!

follows directly from |e-j|<=|e|+j. Hence on |x|=rho=3/2,

    |G(x)| <= M=product(1-rho|q|)^(-|e|).

Every base is at least1/4. Cauchy's estimate bounds the coefficient of degree k by M rho^-k. Summing k>N gives the uniform error E=M rho^(-N-1)/(1-rho^-1) on [0,1].

If C>0 is the extracted constant, the cell integral is enclosed by

    C sum_(k=0)^N g_k mu_k +/- C E mu_0.

Only one endpoint weight is nontrivial on a cell. Thus mu_k=1/(alpha+k+1) on the first cell; on the last, mu_0=1/(beta+1) and mu_k=mu_(k-1) k/(beta+k+1); on interior cells mu_k=1/(k+1). These are exact rational numbers. The last recurrence follows by integration by parts in the beta integral.

For fixed input, the finite partition, constants and M values are fixed. The analytic remainder tends geometrically to zero. Increasing arithmetic precision controls the remaining ball widths. Therefore the algorithm terminates for any prescribed positive width. The copied implementation follows these formulas, including the Jacobian h and an outward rational upper endpoint for the error radius.

## Independent closed-form checks

For alpha=beta=-1/2, substitute t=sin²(theta), then x=tan(theta), to obtain

    J(z)=integral_0^1 [t(1-t)]^-1/2/(1-zt) dt
        =2 integral_0^infinity dx/[1+(1-z)x²]
        =pi/sqrt(1-z).

Differentiation under the integral is permitted for fixed z<1, by domination on a compact z-neighborhood. Therefore

    integral [t(1-t)]^-1/2/(1-zt)² dt
       =J(z)+z J'(z)=pi(2-z)/[2(1-z)^(3/2)].

For distinct z,w, partial fractions give the two-factor value

    [z J(z)-w J(w)]/(z-w).

For the polynomial numerator (1-zt)², expand it and use

    Beta(m+1/2,n+1/2)
      =pi (2m)! (2n)!/[4^(m+n) m! n! (m+n)!],

which follows from Beta(1/2,1/2)=pi and the two beta recurrences. These formulas test fractional singularities at both endpoints, nearby denominator singularities, repeated poles, two scales and negative nu.

The eight original T4 fixtures use elementary antiderivatives or ordinary integer beta integrals. They are also reproduced from the copied moment routine and compared with their saved intervals. Passing fixtures validate those finite instances, while the preceding derivation supplies the general analytic argument.

## Scope and dependencies

The source T4 proof, implementation, fixtures and original results are frozen under source/ with their original hashes. The independent checker evaluates the closed forms above and uses only the copied integration routine for its candidate enclosures. No source directory is executed or modified.

For whole-plane use, substitution t=r²/(1+r²) gives the exact factor1/2 and exponent beta=gamma+sum nu-alpha-2 in the radial integral with numerator r^(2alpha+1), factor(1+r²)^(-gamma) and factors(R_i²+r²)^(-nu_i). Scales below one can first be made at least one by rescaling r. This reduces an already derived, individually integrable radial expression to the theorem. It does not construct that expression, prove candidate far-field cancellation, or certify a whole-plane candidate norm by itself.
