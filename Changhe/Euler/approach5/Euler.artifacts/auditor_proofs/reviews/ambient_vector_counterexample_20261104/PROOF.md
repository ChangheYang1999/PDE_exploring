# Ambient inverse-radius vector counterexamples

## 1. Statement and parameter order

Fix an integer k>=1 and a real C>1/4. There exist a radius R>0, an integer N>=1, and a map u in C-infinity(B_R in C^k;C^N), nonzero at every point except the origin, such that all real partial derivatives of u vanish at the origin and

    |partial_bar u(z)| <= C |u(z)|/|z|,  0<|z|<R.

Here partial_bar_j=(partial_xj+i partial_yj)/2 and the left side is the Euclidean norm of the entire N by k complex derivative array. The target dimension is finite but may depend on both k and C. The construction below uses N=2M. It does not give a prescribed target dimension in each source dimension.

Choose sigma strictly between (1/(4C))^2 and 1, put rho=sqrt(sigma), and choose c0 with 1/4<c0<C rho. These choices are possible because C>1/4. Set epsilon=c0-1/4>0. The construction depends only on compactness of a finite-dimensional sphere, elementary finite-sum Holder and Cauchy-Schwarz inequalities, a smooth step on an interval, and differentiation. Its positive sharpness comparison in Section 6 separately imports the confirmed continuation theorem LIT354.

## 2. A finite family and uniform adjacent-degree ratios

For every unit eta in C^k, the complex-linear form ell_eta(z)=sum_a z_a conjugate(eta_a) has norm one and ell_eta(eta)=1. The open sets of unit vectors zeta satisfying |ell_eta(zeta)|>rho cover the unit sphere. Compactness gives a finite subcover with forms ell_1,...,ell_M. Thus, for every unit zeta,

    rho <= max_j |ell_j(zeta)| <= 1.

Choose an integer n0>=1 large enough that M^(-1/(2n0))>=rho. For n>=n0 define the holomorphic homogeneous vector

    P_n(z)=sigma^(-n/2) (ell_1(z)^n,...,ell_M(z)^n),
    a_n(zeta)=|P_n(zeta)|.

The covering property gives 1<=a_n<=sqrt(M) sigma^(-n/2), so no P_n vanishes at a nonzero point.

For completeness let x_j=|ell_j(zeta)|^2 in [0,1] and S_n=sum_j x_j^n. Holder with exponents (n+1)/n and n+1 gives

    S_n <= S_(n+1)^(n/(n+1)) M^(1/(n+1)).

Consequently S_(n+1)>=M^(-1/n) S_n^((n+1)/n), whereas x_j<=1 implies S_(n+1)<=S_n. Since S_n^(1/(2n))>=rho and M^(-1/(2n))>=rho for n>=n0,

    sigma <= sqrt(S_(n+1)/S_n) <= 1.

After the degree-dependent normalization this becomes

    sqrt(sigma) <= a_(n+1)/a_n <= 1/sqrt(sigma).

The same finite family works for all degrees and directions. Taking successively new covers, or a direct sum over all degrees, is unnecessary.

## 3. Angle, envelope and definition of the map

Take a smooth nondecreasing chi on [0,1], identically zero near 0 and one near 1. Let Mchi=max chi', and take a fixed L>0 with L>=pi Mchi/(4epsilon). Set t0=n0 L and R=exp(-t0). For t in [nL,(n+1)L], n>=n0, put

    theta_n(t)=(pi/2) chi((t-nL)/L).

Then 0<=theta_n'<=2epsilon. Define F(t0)=0 and F'=n+sin^2(theta_n) on each interval. Near an interface t=(n+1)L both prescriptions have the constant derivative n+1, so F is smooth. Every derivative of F of order at least two is bounded uniformly in n. Also

    t/L-1 <= F'(t) <= t/L+1,
    F(t) >= (t^2-t0^2)/(2L)-(t-t0).

For z nonzero let r=|z|, t=-log r, and Q_n(z)=r^(-n)P_n(z). Write C^(2M) as two orthogonal copies of C^M, with isometric inclusions iota_0,iota_1. If j_n is the parity of n, define on the nth interval

    u(z)=exp(-F(t)) [cos(theta_n(t)) iota_(j_n) Q_n(z)
                     +sin(theta_n(t)) iota_(j_(n+1)) Q_(n+1)(z)].

Because |Q_n(z)|=a_n(z/r)>=1 and the two blocks are orthogonal,

    |u(z)|^2=exp(-2F) [cos^2(theta_n) a_n^2
                        +sin^2(theta_n) a_(n+1)^2]
             >=exp(-2F)>0.

This proves nonvanishing away from the origin before any derivative estimate.

## 4. The full derivative array and the constant

Compute using Q_n=exp(nt)P_n and the holomorphicity of P_n. Put theta=theta_n and H=theta'+sin(theta)cos(theta). Direct differentiation of the two scalar radial coefficients gives

    d_t [exp(-F+nt)cos(theta)]=-exp(-F+nt)H sin(theta),
    d_t [exp(-F+(n+1)t)sin(theta)]=exp(-F+(n+1)t)H cos(theta).

The identities use F'-n=sin^2(theta), not an estimate of that difference. Moreover 0<=H<=2epsilon+1/2=2c0. Since

    partial_bar_j t=-z_j/(2r^2),
    sum_j |partial_bar_j t|^2=1/(4r^2),

the derivative array is the outer product of a target vector with partial_bar t. Its squared Euclidean norm factors exactly. Orthogonality of the target blocks gives

    |partial_bar u|^2=exp(-2F) H^2/(4r^2)
                      [sin^2(theta) a_n^2+cos^2(theta) a_(n+1)^2].

To bound the quotient, write q=a_(n+1)/a_n. Both q^2 and q^(-2) are at most 1/sigma. The ratio of the last bracket to the bracket in |u|^2 is at most max(q^2,q^(-2),1), hence at most 1/sigma. Thus

    |partial_bar u|/|u| <= c0/(sqrt(sigma) r) < C/r.

There is no factor depending on the source dimension in this identity: the entire sum of the radial derivative squares was evaluated. The radius is |z|, not a coordinate modulus. This avoids the obstruction to extending a one-variable example simply by ignoring the other coordinates.

## 5. Interfaces and extension at the origin

Near t=(n+1)L the nth angle equals pi/2 and the next angle equals zero. On both sides F' equals n+1 throughout a neighborhood of the interface. Continuity of F therefore gives a single constant d_n with F=(n+1)t+d_n there. Both map formulas reduce to

    u(z)=exp(-d_n) iota_(j_(n+1)) P_(n+1)(z).

They agree on a full annular neighborhood as holomorphic polynomials. This proves smoothness and the derivative bound at every interface, rather than merely equality of the values on its sphere.

For a real multi-index alpha of length m, the derivatives of r^(-n) of order a obey

    |D^a(r^(-n))| <= K_(a,k) (n+1)^a r^(-n-a).

This follows inductively by differentiating the radial power; each derivative contributes one inverse radius and a factor bounded by a constant times n+a. The derivatives of a unit linear form's nth power of order b<=n are bounded by a constant depending on b times (n+1)^b r^(n-b); for b>n they vanish. Leibniz therefore yields

    |D^alpha Q_n(z)| <= K_(m,k) sqrt(M) sigma^(-n/2)
                       (n+1)^m r^(-m).

Derivatives of t of order j>=1 are bounded by K_(j,k)r^(-j). All angle derivatives are bounded uniformly in n, F'=O(1+t), and higher F derivatives are uniformly bounded. Applying the product and chain rules to u gives finite constants A_m,B_m such that, uniformly in direction and interval,

    |D^alpha u(z)| <= A_m(1+t)^B_m
       exp[-F(t)+mt+(n+1)log(1/sigma)/2].

Here n<=t/L, so the positive part of the exponent is only linear in t. The lower bound for F gives a negative quadratic leading term. For every fixed p>0 the bound divided by r^p=exp(-pt) tends to zero. In particular every punctured derivative is o(r^p), uniformly in direction.

Set u(0)=0 and extend each punctured derivative by zero at the origin. Each extended derivative is continuous. Its difference from its value at zero is o(|z|), so it is Frechet differentiable there with zero derivative, not only directionally differentiable. Induction in m proves that these are the actual derivatives of the extended map. Thus u is smooth and all derivatives at zero vanish. The same bounds imply infinite-order vanishing in every finite-power local integral norm.

## 6. Weak coefficient norm and comparison with the positive theorem

Let d=2k and let v_d be the volume of its Euclidean unit ball. Put b(z)=C/|z| off zero and b(0)=0. For every lambda>0,

    measure{z in B_R:b(z)>lambda}=v_d min(R,C/lambda)^d.

For the convention ||b||_(d,infinity)=sup_(lambda>0) lambda measure{b>lambda}^(1/d), this gives exactly

    ||b||_(d,infinity)=C v_d^(1/d),
    lim_(lambda->infinity) lambda^d measure{b>lambda}=v_d C^d.

The differential inequality holds almost everywhere and also at the origin with the assigned b(0), since u and its derivative vanish there. Thus an unrestricted finite-vector continuation theorem for arbitrary finite weak-L^d norm is false. This does not provide a counterexample for every prescribed norm or prescribed target dimension.

The already confirmed LIT354 theorem, A2977, applies at coefficient 1/(4|z|), in every finite target dimension, to locally integrable distributional solutions with the stated full derivative-array bound and infinite-order L1 integral vanishing. The present smooth map satisfies the regularity and flatness parts of that class. Combining the positive theorem with the construction for every C>1/4 proves sharpness of the universal inverse-radius constant when all finite target dimensions are allowed. The positive part is an explicit imported theorem; it is not reproved by the construction. No sharp higher-dimensional logarithmic correction, scalar counterexample, Euler-carrier estimate or Euler profile follows.

## 7. Reading and designated status

The submitted source 26ecb8e2eeeb468398fc5a315591110a238701ee29bb663893ae87e76b7891f8, all six sections and fourteen numbered estimates, and its 38 manual checks and verification plan were read. The independent argument above was submitted for the existing configured model Theory Agent C  comparison. Section8 records that completed comparison; no positive verdict was assigned before it. Actual provider execution is independently unattested.


## 8. Completed comparison and diagnostic limitations

The complete eight-item C06:01:07 comparison agrees with the finite cover, Holder ratio, fixed-family parameter order, exact full derivative array, polynomial seams, all-order extension and coefficient norm. The source and reconstruction hashes in the comparison match the submitted files. The derivative array has rank at most one, so its operator and Euclidean norms agree in this construction. The positive continuation input remains the separately confirmed LIT354 theorem. This proves universal inverse-radius sharpness over finite targets, not a prescribed-target statement from this construction.

The entire script and both logs were read, without rerunning them. The final log has37passing checks:13symbolic identities,2exact specific parameter checks for the six-vector family in C2,7negative controls (six exact and one numerical), and15finite numerical sample checks. The symbolic identities for that family, together with max_i |n_i|>=1/sqrt(3) on the unit sphere in R3, justify the exact cover parameter rho=17/20; the other exact check gives n0=6. These certify that particular example, not every family by computation. The general proof is Section2.

The numerical checks use60decimal-digit mpmath arithmetic,400sampled directions per configuration,31degree norms and30adjacent pairs, finite differences at eight points per configuration, and two sampled seam radii. The cutoff derivative maximum is estimated on a finite grid and multiplied by1.02; it is not a certified global supremum. Thus even the chosen numerical annulus lengths are diagnostics, not a proof of the universal derivative bound. All such conclusions instead follow from the analytic construction with the actual supremum. The first log has20passing checks followed by a string-minus-mpmath TypeError. Its retained text has the absolute agent prefix replaced by a relative prefix, with original and retained hashes recorded. The final script converts the parameter to mpmath before subtracting. The source of the first run was not retained separately, so the assertion that no other code changed is not independently certified.

The optional C remark that every weak-norm value above v_d^(1/d)/4 is realized follows by choosing C accordingly. Its reference to smaller norms as open must retain the already proved smallness regimes, including the one-variable vector result A2920; it is not an assertion that every smaller-norm case is unsettled. These qualifications do not change the construction or its sharpness comparison. No fixed-target, higher-dimensional logarithmic, scalar or Euler conclusion is inferred here. Actual provider execution is independently unattested.


## 9. Additional coordinator comparison

The complete coordinator comparison of 2026-11-04T06:02:51Z was read, including all nine items and three remarks. It independently checks the cover, adjacent-degree ratio, envelope, full derivative array, seams, all-order extension and weak coefficient norm. These agree with Sections 1-6. Its report suggestion is valid for LIT356 alone; fixed-target statements belong to subsequent constructions.

The complete retained script and log were also read without execution. They report six passing numerical checks: finite-difference array and vector norms at 40 points, 20,000 samples each for Holder and the quadratic-form ratio, 200 finite-difference checks of the radial gradient, and a finite lambda grid for the weak norm. The first local calculation substitutes a cubic step for the smooth cutoff, as disclosed. None establishes a universal inequality, a globally valid smooth gluing or a certified supremum. All such assertions instead follow from the analytic proof above. The transcript provides no new theorem premise. The coordinator is configured as model; provider execution is independently unattested.


## 10. Confirmed source-status revision

The source revision f02b906370fb4f6d1cbdaac2875a690354944eed99d56dd605d1b5e43a910e8d differs from the submitted source only in its status, the already confirmed sharpness sentence, and the new confirmation Section 7. Every changed passage was read. A2999-A3000 support the positive labels, A3001 supplies the diagnostic qualifications, and A3002 remains the scope boundary for this construction. The coordinator comparison is already checked in Section 9 above. The source accurately says that the literature agent did not itself read or rerun the diagnostic scripts. Its closing description of LIT357 and LIT358 as separate submissions belongs to its recorded confirmation checkpoint; LIT357 was subsequently confirmed in A3005. The construction is byte-unchanged, and no stronger target, logarithmic or Euler assertion is introduced.
