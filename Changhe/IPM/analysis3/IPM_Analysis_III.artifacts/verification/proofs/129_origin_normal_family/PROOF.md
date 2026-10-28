# The origin angular normal family at each fixed radial frequency

## Exact space, operator and result

Let k=1615536043799051/9007199254740992, ell=1/k, A=2ell-1, D=4ell-1 and Sigma=A+D. Put delta=9/5, s_0=41/20, sigma=25/4. On the first quadrant angular interval I=(0,pi/2), set

 p=cos^2(theta) sin(theta),
 q=-A cos^2(theta)+D sin^2(theta),
 vtheta=Sigma sin(theta) cos(theta).

Use the parity obtained by making the bulk variable v odd across theta=0 and even across theta=pi/2. Let s_-(theta) be any smooth order between s_0 and sigma, equal to s_0 near0 and to sigma on a neighborhood of pi/2. Define the angular Hilbert space H_ang by

 v in H^{s_-(.)}(I),
 u=v/p in H^sigma near pi/2,
 u even across pi/2 and u(pi/2)=0.

The local cofactor norm is added to the bulk norm using fixed smooth cutoffs. The parity extensions specify the endpoint Sobolev norms. Different cutoffs inside fixed constant-order regions give equivalent spaces. The space is complete as a closed graph intersection with a closed trace condition. For the normal family only fixed real xi is considered, so the parameter-dependent Bessel weight(1+xi^2+eta^2)^{s/2} is equivalent to the displayed angular norm, with a constant allowed to depend on xi.

For real xi and complex lambda define

 N_(xi,lambda) v=vtheta v'+[(3+delta+i xi)q-1-lambda]v,
 D(N)={v in H_ang:N_(xi,lambda)v in H_ang in distributions}. (1)

This is its maximal domain, not a boundary condition chosen for the ODE formula. The domain does not depend on lambda or xi, since the changing terms are smooth bounded multipliers. The operator is closed with its graph norm.

Define

 m_x=Sigma(3/2-s_0)+delta A=(3ell-7)/10,
 m_y=Sigma(sigma-1/2)-delta D=(273ell-97)/10,
 lambda_2=delta D-2Sigma=(11-24ell)/5.                    (2)

**Theorem.** For every fixed real xi and every complex lambda with

 Re lambda>max(-m_x,-m_y,lambda_2)=-m_x,                  (3)

N_(xi,lambda):D(N)->H_ang is bijective. Its inverse is bounded into both H_ang and the graph domain. In particular this holds for every real lambda>=0. The bounds are locally uniform in(xi,lambda) inside(3), but no bound uniform as |xi| tends to infinity is proved here. Monotonicity of s_- is not required for this fixed-parameter theorem; a monotone s_- supplied by proof 128 is an allowed choice.

## Exact factor and homogeneous solution

The identity D=2A+1 gives

 3q-1+vtheta p'/p=0.                                    (4)

Indeed, for x=sin^2 theta, q=-A+Sigma x and vtheta p'/p=Sigma(1-3x), so the left side is Sigma-3A-1=0. Therefore writing v=p u reduces(1) to

 N_u u=vtheta u'+[(delta+i xi)q-lambda]u=f_u, f_u=f/p.     (5)

This is one global equation. The different bulk and cofactor zeroth-order constants at the endpoints are not substituted into an unspecified common c(theta).

Put

 a=((delta+i xi)A+lambda)/Sigma,
 alpha=((delta+i xi)D-lambda)/Sigma,
 beta=1+a.

Then a+alpha=delta+i xi, and the nonvanishing homogeneous cofactor solution in the open arc is

 H(theta)=sin(theta)^a cos(theta)^alpha.                  (6)

Powers use the real logarithm of the positive sine and cosine. Direct differentiation proves(5) with zero right side. The homogeneous bulk solution is p H, so its exponents are beta at0 and alpha in the vertical cofactor. Their real parts obey

 Re beta>s_0-1/2=31/20,
 Re alpha<2,
 Re alpha<sigma-1/2=23/4                                (7)

under(3). The last condition follows separately from Re lambda>-m_y and is weaker than Re alpha<2 in this case.

## The vertical endpoint and the selected formula

For f in H_ang, its cofactor f_u near pi/2 is even, has zero value, and lies in H^(25/4). In particular it is O(cos^2 theta), so Re alpha<2 makes the improper integral

 u(theta)=-H(theta) integral_theta^(pi/2)
                 f_u(s)/[H(s)vtheta(s)]ds               (8)

converge for each theta>0. Differentiation on compact subintervals proves N_u u=f_u. Formula(8) has a minus sign. In particular the leading endpoint Taylor coefficient is f_2/[Sigma(alpha-2)], not f_2/[Sigma(2-alpha)].

Here is a full endpoint Sobolev estimate. Set z=cos theta near pi/2 and K(z)=(1-z^2)^(a/2). Equation(5), with u=K w, becomes

 N_u(Kw)=-Sigma(1-z^2)K [z w'-alpha w].                  (9)

Multiplication by K and its reciprocal is bounded on every fixed local Sobolev space, with bounds locally uniform in the parameters. The transformed forcing F=-f_u/[Sigma(1-z^2)K] is even, belongs to H^sigma and has zero value. Remove its two nonzero possible Taylor coefficients of degree2 and4. The remaining R belongs to H^(6+1/4) and has zero traces of derivatives0 through5. The odd traces vanish by evenness. All the removed traces are continuous functionals because their orders are less than sigma-1/2.

The polynomial terms of degree j=2,4 are solved by z^j/(j-alpha). These denominators are nonzero under Re alpha<2. For the remainder use

 T_alpha R(z)=integral_0^1 tau^(-alpha-1)R(tau z)dt.

For a smooth approximating R with those six zero traces, differentiate six times. Scaling in L2 gives the integrable factor tau^(6-Re alpha-3/2). Scaling the one-quarter difference seminorm of the sixth derivative gives tau^(6+1/4-Re alpha-3/2). Both integrals converge since Re alpha<2. Thus the sixth derivative of T_alpha R is bounded in H^(1/4) on a fixed half-interval by a constant times ||R||_H^sigma. Its traces0 through5 are zero, and the elementary repeated-integration Poincare estimate controls all lower derivatives. Approximation proves the assertion for every R in the stated closed trace subspace. This proves T_alpha R in H^sigma with zero value and even extension. The estimates also justify(8) in this Sobolev class. Smooth coefficient factors in(9) preserve the same conclusions.

The homogeneous term H cannot belong to the vertical cofactor space unless its coefficient is zero. With Re alpha<2, the even extension of z^alpha is not in H^(25/4), except for alpha=0, when it is smooth but its nonzero axis value violates the trace condition. For completeness, if Re alpha<=-1/2 it already fails L2. Otherwise damp the one-sided power and use

 integral_0^infinity z^alpha exp(-(epsilon+i eta)z)dz
 =Gamma(alpha+1)(epsilon+i eta)^(-alpha-1).

Adding its reflected transform and then removing the damping gives a leading Fourier coefficient -2 Gamma(alpha+1) sin(pi alpha/2) times |eta|^(-alpha-1). A cutoff equal to1 near0 changes only terms with faster decay, by integration by parts away from0. The leading coefficient vanishes in this range exactly for a nonnegative even integer alpha. Otherwise its H^sigma square integral at high frequency converges exactly when Re alpha>sigma-1/2. The same calculation with a difference of reflected transforms proves the odd-power criterion used below, with the exceptional smooth odd integers. Nonreal alpha has the same strict real-part threshold. No such allowed power lies below2 while having zero value. This proves the local uniqueness needed at the vertical endpoint.

## The horizontal endpoint

Set z=sin theta near0 and K_x(z)=(1-z^2)^((2+alpha)/2). Since v=p u, its homogeneous solution is K_x z^beta. Direct substitution gives

 N_(xi,lambda)(K_x w)=Sigma(1-z^2)K_x [z w'-beta w].      (10)

The transformed forcing F=f/[Sigma(1-z^2)K_x] is odd and belongs to H^(41/20). Remove its degree-one Taylor coefficient. This trace exists since s_0>3/2. The remaining odd R has zero value and first derivative and can be extended, with a bounded norm, to an odd compactly supported H^s_0 function on the line with these same zero traces.

A local particular solution for R is

 T_beta^- R(z)=-integral_1^infinity tau^(-beta-1)R(tau z)dt.

On the full line the H^s_0 scaling estimate for tau>=1 is

 ||R(tau .)||_H^s_0<=tau^(s_0-1/2)||R||_H^s_0.

Therefore the integral is bounded in H^s_0 whenever Re beta>s_0-1/2, exactly the first condition in(7). It solves z w'-beta w=R in distributions. The degree-one term has the smooth particular solution F_1 z/(1-beta), with beta!=1 under(7). Any further local solution differs by C z^beta. Its odd extension belongs to H^s_0 because Re beta>s_0-1/2. Smooth cutoff powers give a norm locally bounded in beta within that open half-plane; if beta happens to be a smooth odd integer, membership is easier and does not invalidate the strict sufficient condition.

The solution selected by(8) has a finite value at any fixed interior angle. Its difference from the preceding local particular solution therefore fixes a finite coefficient C. Evaluation there is bounded by the vertical endpoint estimate, the integral on a compact intervening arc and the H_ang norm of f. Hence the selected v belongs to the horizontal H^s_0 parity space, with a bound locally uniform in the parameters. This checks membership of the full solution, not just the existence of a formal Frobenius exponent.

## Interior, maximal domain and bijectivity

On any closed subarc inside I, vtheta is smooth and bounded away from zero. The local first-order inverse is an operator of order minus one plus a smooth homogeneous term. It maps variable-order H^{s_-(.)} to H^{s_-(.)+1} locally. This follows either from the one-dimensional elliptic parametrix and the scalar variable-order calculus already checked in proof 123, or by localizing the primitive and separating its smooth off-diagonal kernel. No monotonicity between separated points is needed at a fixed parameter. Compact interior coverings and the two endpoint estimates prove ||v||_H_ang<=C_(xi,lambda)||f||_H_ang for(8).

The endpoint extensions have the required parity and zero vertical trace. Since the operator vanishes to first order in its endpoint transport coefficient, these extensions introduce no boundary delta; ordinary distributional differentiation of a locally Sobolev function with the specified parity gives exactly(1). In particular Nv=f in H_ang, so v lies in the maximal domain and ||v||_graph<= (C_(xi,lambda)+1)||f||. If Nv=0, the solution on the open arc is a multiple of p H, and vertical membership forces its coefficient to vanish. Thus the inverse is both a left and right inverse on the exact domain. Closedness follows independently because N is continuous from H_ang to distributions and H_ang embeds continuously in distributions.

All denominators and the real-part gaps in the endpoint integral estimates stay away from zero on compact parameter subsets of(3). The interior coefficient multipliers vary continuously there. This proves the stated local parameter uniformity. It supplies no estimate on an unbounded xi set.

## What changes without the trace or the parity

The explanation in the theory author draft needs two distinctions. Failure of convergence of the unregularized integral(8) is not by itself non-surjectivity: one may subtract Taylor coefficients and integrate a finite part. A discrete kernel at a parameter is also not automatically a failure of Fredholmness.

If the vertical zero trace is omitted while evenness is retained, at xi=0 and lambda=delta D the explicit cofactor

 u=sin(theta)^delta, v=p sin(theta)^delta

is a nonzero kernel element. It is smooth and even at the vertical endpoint and has nonzero vertical trace. At the horizontal endpoint its bulk exponent is1+delta=14/5>s_0-1/2, so it really belongs to that enlarged domain. Thus invertibility fails at this positive parameter. More generally the same formula with exponent delta+i xi gives a kernel at lambda=(delta+i xi)D.

If evenness at the vertical endpoint is omitted but a zero value is retained, work on a one-sided angular space without reflection parity there. At xi=0 and lambda=delta D-Sigma, the cofactor

 u=sin(theta)^(delta-1) cos(theta), v=p u

is a nonzero kernel element. It has zero value and a nonzero first normal derivative, and its horizontal bulk exponent is delta=9/5>s_0-1/2. A signed extension across the vertical endpoint is smooth there. For arbitrary xi the corresponding complex parameter is lambda=(delta+i xi)D-Sigma. This is the first-derivative mode removed by evenness.

Both examples are in the full operator graph, with image zero. They establish non-invertibility at the stated discrete parameters of the enlarged spaces. In the even space without the zero trace, the operator is actually Fredholm of index0 at the resonance, not non-Fredholm. To prove this, decompose that space into its vertical trace and the zero-trace subspace H_ang. A fixed smooth lift of the trace gives the block form

 [delta D+i xi D-lambda, 0; B, N_0],

where N_0 is the bijection proved above and B is a bounded finite-rank column. The same splitting applies to the maximal graph domain: subtracting the smooth lift preserves it. At the resonant parameter the range is the closed codimension-one zero-trace target, and the kernel has dimension one. Hence its Fredholm index is0. The first-derivative resonance has the analogous index0 statement in a one-sided space with zero value: split off the first normal derivative, and use the same proof above on the subspace with both value and first derivative zero. In that proof remove all Taylor degrees2 through5 instead of only the even ones; the remainder estimate and horizontal estimate are unchanged. Away from such Taylor resonances, an integral requiring a finite-part interpretation can still define a valid inverse. The theorem above uses the true even zero-trace remainder space and avoids both positive resonances.

## Dependencies and limitations

The operator and its normalization are derived from(4), not from a sign convention imported from an unrelated X3 state. Proof 128 supplies a permitted smooth origin order. Standard one-dimensional Sobolev trace, cutoff power and fractional difference norms are used in the explicit estimates above; the only variable-order ingredient is the already verified local scalar calculus of proof 123.

This is a theorem about the exact origin normal family at each fixed xi. It does not identify the globally selected low inverse with a high inverse, and it does not prove parameter-uniform normal invertibility, an end parametrix, finite-regularity propagation, the global H3 estimate, low injectivity or nonlinear existence. Those steps remain separate obligations. The angular Taylor resonances here use the cofactor radial power delta=9/5. They are not the different scalar B-space spectral threshold of proof 106.
