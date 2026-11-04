# Independent audit of sign-changing envelope carriers and unbounded strain ratio

Date: 2026-11-03T23:48:06.504041+00:00
Status: local carrier constructions CONFIRMED A2588-A2595; full-system and global extensions OPEN A2596.

## 1. Exact local theorem and two fixed Hessians

Fix 0<c<1/2, a finite omega, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J and a=1-2c. Let sigma be a smooth transverse section through x0=sigma(0)!=0. Restrict to a relatively compact disc and finite flowbox before choosing the envelope. There is a finite Cstar>=1, depending only on this fixed geometry, c,omega and a fixed smooth bump, such that for every positive finite-valued lambda:(0,rho1)->(0,infinity) tending to infinity at zero, a smaller disc and flowbox carry a smooth V with

    div V=0, X.V=0, DV X=-LV, W=curl V.                    (C)

V is zero and flat to every order exactly on the central X-orbit Gamma, and is nonzero off it. The actual section ratios

    Qn=|W|/|V|, Qp=|W.X|/|V|

satisfy Qn+Qp<=Cstar+lambda(r)/r, r=|y|>0. Each is in Lp for every 0<p<2, and each (Qj-C0/r)_+ fails to be L2 on every centre disc for every finite C0>=0. The Euclidean scalar T=tr((DV)^2) has both signs arbitrarily near every point of Gamma and is zero on Gamma. This scalar would be the source in -Delta P2=T if a pressure completion existed; no such completion is part of the construction.

For LIT307 take a fixed Hessian H*=diag(1,-1). For LIT308 take H*=diag(M11(0),-M22(0)), with the positive definite M defined below. In the latter construction there are points approaching Gamma at which W is nonzero and

    |sym DV|_F^2/|W|^2 -> infinity.

Both matrices have negative determinant. This single proof treats the two submitted constructions with their respective fixed H*. Lambda, the lower-case envelope lambda, and the matrix L are distinct quantities. No measurability of lambda is required and no uniformity in omega is asserted. The sources are pinned at 83f5d189c3db3c0e84b34915fe82ae57eee6799a14fac911cb797ed486781ff1 and d019e0cf7debdb4134e2341b0c29c09e9612b91caf556e299ddb7df42ac726a9.

## 2. Geometry and bounds fixed before the envelope

On the section set m=|X(sigma)|, beta_i=X.sigma_i/m2, T_i=sigma_i-beta_i X, g_ij=T_i.T_j, j=|det(sigma_1,sigma_2,X)|=m sqrt(det g), nu=1/j, M=g/j and b=(3c-1)beta. On the fixed smaller disc m,j and the least eigenvalue of M are bounded below by positive constants. All fixed-order derivatives of these smooth coefficients are bounded.

Choose phi smooth and compactly supported in the unit disc, with grad phi(0)=0 and D2phi(0)=H*, by cutting off its quadratic form. Choose epsilon=1/(16 max(1,sup|grad phi|)). These choices depend on the fixed geometry only. Suppose temporarily that f is positive, nondecreasing, smooth and flat with every derivative at zero. Set rn=2^-n, yn=(rn,0). Let elln<=rn/100 give disjoint bump discs Bn and assume

    fn/2<=f(r)<=2fn on |r-rn|<=elln, fn=f(rn),
    f_(n+1)<=fn/2,
    fn elln^(1-k)=O(rn^N) for all fixed k,N.               (2)

Define

    psi(y)=integral_0^|y| f(s) ds
           +sum_n epsilon fn elln phi((y-yn)/elln),
    u=J2 grad psi, J2(v1,v2)=(-v2,v1).

Each gradient perturbation is at most fn/16<=f/8. At most one is present at a point, so psi_r>=7f/8 and |grad psi|<=9f/8. The kth derivative of the nth perturbation is bounded by Ck fn elln^(1-k). Assumption (2) makes all these derivatives vanish faster than every power at zero. Difference quotients give a smooth flat extension. The radial background has the same property. Also div u=0.

For polar unit vectors er,etheta, write br=b.er and define

    E(r,s,theta)=exp(integral_s^r br(v,theta)dv),
    q(r,theta)=r^-1 integral_0^r s b(s er).u(s er) E(r,s,theta) ds,
    w=u+q er.                                            (3)

The radial equation q_r=br q+b.u-q/r implies div w=b.w exactly. We next bound its first derivative without losses involving elln^-1 or f'.

For the background u0=f etheta, monotonicity gives |q0|+|q0_theta|<=Crf and |q0_r|<=Cf. For a single bump a ray intersects its disc in total radial length at most 2elln. Its velocity is bounded by C epsilon fn and its angular derivative by C epsilon rn fn/elln. Differentiate the smooth integrand under the integral sign; it is unnecessary to differentiate moving support endpoints. Bounded derivatives of b and E give

    |qn|<=C epsilon rn elln fn/r,
    |qn_theta|<=C epsilon rn2 fn/r.

These quantities vanish for r<rn-elln. If a bump is radially eligible, rn/r<=2. The radial equation now also bounds |qn_r|,|qn|/r and |qn_theta|/r by C epsilon fn. If m0 is the first radially eligible index, either r>=r_m0, when monotonicity gives f_m0<=f(r), or |r-r_m0|<=ell_m0, when (2) gives f_m0<=2f(r). The eligible indices form a radial tail, while the indices contributing on an individual ray are only a subset. The geometric decrease in (2) therefore gives sum_eligible fn<=2f_m0<=4f(r). It follows that

    |q|<=Crf, |D(q er)|<=Cf.                             (4)

This argument never compares f(2r) to f(r). Its constants depend only on the fixed geometry and bump. For higher derivatives substitute s=r tau in (3), obtaining r times an integral on the fixed interval [0,1]. Every fixed polar derivative of u(r tau er) is uniformly flat, while derivatives of the remaining coefficients have at worst fixed powers of r^-1 upon conversion to Cartesian coordinates. Flatness absorbs those powers, so q er is smooth and flat to all orders at zero.

## 3. Exact lift, ratios and the Euclidean trace

Let Phi(y,s)=exp(sA)sigma(y), set v=w/j, h=-beta.v, and define

    V(Phi(y,s))=exp(-s)D Phi(y,s)(v(y),h(y)).              (5)

In these coordinates X is partial_s, so [X,V]=-V and DV X=(A-I)V=-LV. The conformal linear flow and h+beta.v=0 give X.V=0. Its volume density is exp(3cs)j; hence

    div V=exp(-s)j^-1[div w-(3c-1)beta.w]=0.

Thus (C) is exact. Since w_theta=psi_r>=7f/8 and the lift is invertible, its zero set is precisely Gamma. All derivatives are flat there. On the section |V| is bounded above and below by positive geometry constants times f.

Write H=D2psi. By (4), Dv=nu J2 H+O(f), Dh=O(|H|+f). Differentiating (5), dividing by |V| and using the bump Hessian bound yields

    Qn+Qp<=C[1+f'/f+1/r+sum_n elln^-1 1_Bn].            (6)

The finite constant C>=1 is fixed before f or lambda, because (2) has fixed comparison constants.

The Euclidean trace needs the derivative of the moving frame. Put F=D Phi and Z=exp(-s)(v,h). The matrix DV is conjugate to D_z Z+K, with columns K_i=F^-1(partial_i F)Z=O(f). At s=0,

    D_z Z = [[Dv,-v],[Dh,-h]],
    tr((D_z Z)^2)=tr((Dv)^2)-2(Dh).v+h2.

Because H is symmetric, tr((J2 H)^2)=-2det H. All the remaining terms are O(f(|H|+f)). Therefore

    T(sigma(y))=-2nu(y)^2 det H(y)+O(f(r)(|H(y)|+f(r))).  (7)

This is the physical Euclidean derivative, not the derivative in a frozen coordinate frame. Differentiating the exact carrier transport gives

    DV(exp(sA)x)=exp(-s)exp(sA)DV(x)exp(-sA),
    T(exp(sA)x)=exp(-2s)T(x).                             (8)

## 4. Smooth factor and bump radii for an arbitrary envelope

Fix C from (6), put Cstar=C and D0=402C. Only now choose lambda. Choose T1 large enough that exp(1-T1) is within the given and fixed geometric discs and lambda(r)>=4D0 for every smaller positive r. Define

    mu(t)=sqrt(inf_{0<r<=exp(1-t)} lambda(r)/D0), t>=T1.

This is finite by evaluating the infimum at any one positive radius, nondecreasing, at least two and divergent. No measurability of lambda is used. For integers n>=2 choose Tn with T2>=T1+1, T_(n+1)>=Tn+1 and mu(t)>=n+1 for t>=Tn. With a fixed smooth nondecreasing step chi, zero at arguments <=0 and one at arguments >=1, set

    Lambda(t)=sum_{n>=2} chi(t-Tn),
    G(t)=integral_T1^t Lambda(s)ds,
    f(r)=exp(-G(log(1/r))).                              (9)

The sum is locally finite and at most one step has a nonzero derivative at any t. Every positive-order derivative of Lambda is bounded. Counting the completed and active steps gives Lambda+1<=mu, and Lambda tends to infinity. With M1=sup|chi'|, integrating its derivative bound gives Lambda(t)<=M1(t-T1).

The derivative recurrence

    f^(k)(r)=r^-k Pk(log(1/r))f(r),
    P0=1, P_(k+1)=(Lambda-k)Pk-Pk'

and bounded derivatives of Lambda imply |Pk(t)|<=Ck(1+t)^k for large t. Since G(t)>=Nt-C_N for every fixed N, all derivatives of f are flat. Also f'=Lambda f/r>=0 and f>0.

For tn=n log2 and sufficiently large n choose

    elln=rn/[100(1+Lambda(tn))^2].                        (10)

The discs are disjoint since elln<=rn/100. On |r-rn|<=elln, the variation of t is at most 1/[50(1+Lambda(tn))^2]. The derivative bound for Lambda makes the corresponding variation of log f at most (Lambda(tn)+M1)/[50(1+Lambda(tn))^2], tending to zero. Thus the factor-two comparison in (2) holds. Further, f_(n+1)/fn<=exp(-Lambda(tn)log2)<=1/2 eventually. Finally elln^-1<=C(1+tn)^2/rn, so every fn elln^(1-k) is flat in rn. All of (2) holds after choosing the starting index; the constant C of (6) is unchanged.

For r=exp(-t), Lambda(t)+1<=(Lambda(t)+1)^2<=mu(t)^2<=lambda(r)/D0. On Bn, r<=2rn<exp(1-tn), so also (1+Lambda(tn))^2<=lambda(r)/D0 and r/elln<=200(1+Lambda(tn))^2. At most one bump is present. Equation (6) gives

    Qn+Qp<=C+201C lambda(r)/(D0 r)<=Cstar+lambda(r)/r.      (11)

For integration do not use lambda as a majorant. The independent linear bound for Lambda and (10) give

    Qn+Qp<=C_lambda[1+(1+log(1/r))^2/r].                  (12)

For 0<p<2, its pth-power polar integral is bounded by a multiple of integral exp(-(2-p)t)(1+t)^(2p)dt, which converges. This proves the stated Lp assertions even for a nonmeasurable envelope.

## 5. Positive and negative sequences and endpoint failure

At yn, no other bump occurs and

    H(yn)=An H*+diag(fn',fn/rn), An=epsilon fn/elln,
    (fn'+fn/rn)/An=1/[100epsilon(1+Lambda(tn))]->0.

Since det H*<0, det H(yn)=An2 det H*+o(An2). The error in (7) is o(An2), because fn/An=elln/epsilon->0. Hence T(sigma(yn))>=c0 An2>0 for some fixed c0 and all sufficiently large n.

A fixed positive-angle sector around theta=pi misses every bump and every radial ray through a bump. All bump velocities and their Volterra corrections vanish there. The background Hessian has eigenvalues f' and f/r; equation (7) gives

    T=-2nu2 ff'/r+O(ff'+f2/r+f2)<0

at sufficiently small radii. The error divided by ff'/r is O(r+r/Lambda+r2/Lambda), tending to zero. Thus yn and zn=(-rn,0) give both signs; (8) propagates the conclusion to every point of Gamma. Flatness makes T zero on Gamma.

For endpoint failure use this untouched sector. The pullback of V.dx is the one-form with coefficient vector Mw. Direct differentiation there gives

    curl_y(Mw)=f' etheta^T M etheta+O(f/r).

The leading coefficient is uniformly positive. Differentiating X.V=0 and using transport yields X cross W=aV, and therefore

    W=(W.X)X/m2+a(V cross X)/m2,
    curl_y(Mw)=W.(sigma_1 cross sigma_2)
              =delta j(W.X)/m2+O(f),                    (13)

where delta is the fixed orientation. Since f'/(f/r)=Lambda tends to infinity and |V| is comparable to f, both Qp and Qn are bounded below by c1 Lambda(log(1/r))/r on a smaller fixed-angle sector. Its square integral contains integral Lambda(t)^2dt and diverges. For every fixed C0 the same remains true after subtracting C0/r and taking the positive part. Thus no nonnegative L2 function can majorize the remainder. This conclusion uses the actual ratios and no endpoint continuation theorem.

## 6. The metric-dependent cancellation and unbounded strain ratio

For LIT308 only, H*=diag(M11(0),-M22(0)). For symmetric H define

    ell_M(H)=M22 H11+M11 H22-2M12 H12.

Then det H*<0 and ell_(M(0))(H*)=0 exactly. At any point the principal derivative of Mw is M J2 H, so its (2,1) entry minus its (1,2) entry is precisely ell_M(H). The derivatives of M and of q er contribute only O(f). Hence

    curl_y(Mw)=ell_(M(y))(H)+O(f).

At yn, smoothness gives |ell_(M(yn))(H*)|<=C rn. Substituting the Hessian from Section5 yields

    |curl_y(Mw)(yn)|<=C[rn An+fn'+fn/rn+fn].

Use (13), its exact decomposition of W, and the bounds on j,m to obtain

    |W(sigma(yn))|<=C[rn An+fn'+fn/rn+fn]=o(An).

There is no missing transverse component of W: the exact carrier identity fixes that component to a(V cross X)/m2=O(f). Also W is nonzero at every yn, since X cross W=aV, a>0 and V!=0 there.

For a real derivative matrix D, decompose D into its symmetric and skew parts. They are Frobenius-orthogonal, tr(D2)=|sym D|_F^2-|skew D|_F^2, and |curl V|2=2|skew DV|_F^2. Thus

    |sym DV|_F^2=T+|W|2/2.

By Section5 T>=c0 An2 at yn, while |W|/An tends to zero and is nonzero. Their quotient tends to infinity. All metric, bump and epsilon choices precede Cstar and lambda, so this cancellation does not change the prescribed-envelope quantifiers.

## 7. Scope, comparison questions and exact unresolved claims

The constructions satisfy only (C). They show that its exact equations, an isolated infinitely flat orbit, subcritical Lp bounds, endpoint failure and an arbitrarily slowly diverging envelope above inverse radius are compatible with both signs of T. The second also has no finite upper bound on the strain-to-vorticity ratio near the orbit. This does not establish the fixed scalar, its transport, its vorticity first integral, its required sign or zero set, or the common-flat pressure relation.

In particular C61 and C62 are not refuted. Their necessary sign or strain tests are not contradicted solely by these retained carrier properties. These are local consistency constructions, not smooth decaying Euler profiles or counterexamples to the conjecture. No global extension or impossibility of another full-system completion is proved.

Both complete submitted sources were read. The sensitive points for the existing model-configured comparison are the radial-tail sum in Section2, the order of constants and the one-unit shift in Section4, the moving-frame term in Section3 and the conversion from tangential curl cancellation to the full Euclidean W in Section6. No numerical computation or formal build is needed. The complete eleven-item coordinator comparison of 23:51Z was read and pinned in the team records. It agrees with the independent calculations. Its two wording points are already handled here: monotonicity after a bump radius and the expanded error ratio in Section5. The verdicts are CONFIRMED A2588-A2595 at this local carrier scope, with full-system and global extensions OPEN A2596. The comparison does not assert that the scalar hypotheses of C61 or C62 have been met.
