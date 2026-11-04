# Paired strain improves the small-vorticity gap

Status: independent audit of C50, including a rigorous scalar upper-bound certificate. It proves derivative decay below an explicit threshold, not the campaign nonexistence conjecture.

## 1. Exact global statement

Let 0<c<1, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    M=sup |U|<infinity, Omega=curl U.

Use Euclidean vector and operator matrix norms. Suppose W0>0 and |Omega(y)|<=W0 for |y|>=R1. Define

    c_K=(3/(4pi)) integral_S2 |theta cross diag(1,-1,0)theta| dtheta.

For every gamma>c_K W0 there exist alpha in(0,1) and finite K,R such that

    ||DU(y)||<=K |y|^(gamma/c),
    [Omega]_(alpha,B(y,|y|/4))<=exp(K |y|^(gamma/c)), |y|>=R.     (1.1)

Constants may depend on c,omega,M,W0,R1,alpha,gamma and a compact-annulus C2 norm. There is no helicity or prior gradient-bound premise. The rigorous bound c_K<1.77963978 is established below; the decimal 1.77963967918 is only the source quadrature value.

If also U=O(|y|^-kappa), kappa>=0, put delta_star=min(5/4,1/c,(1+kappa)/2) and omega_inf=limsup_(|y|->infinity)|Omega(y)|. Then

    omega_inf<c delta_star/c_K
       implies DU->0 and |Omega|+||DU||<=C/(1+|y|).            (1.2)

The threshold is strict, and omega_inf can be infinite. In particular it belongs to {0} union[c delta_star/c_K,infinity].

## 2. Physical and local inputs, independently rechecked

Sections3-8 of the full A1068-A1074 proof in the team records supply the following inputs; that entire proof was reread for this audit. The zero velocity is immediate, so take M>0. With tau=T-t, s=-log tau, Q=exp(omega sJ), set

    y=exp(sA)x, u=tau^(c-1)Q U(y), xi=tau^-1 Q Omega(y),
    Du=tau^-1 Q DU(y)Q^T, S=sym Du.

The physical vorticity equation is xi_t+u.grad xi=S xi, since the antisymmetric part of Du annihilates xi. On an exterior fixed annulus, |xi|<=w=W0/tau. Choose t0<T sufficiently close to T. For any unit xstar let B_t be the shrinking ball of radius1/4+(2M/c)tau^c about xstar. A characteristic ending in B_t at time t stays at earlier sigma in the convex ball E_(sigma,t) with margin d>=M(t-sigma) inside B_sigma. All balls lie in a fixed annulus. Bounded physical speed gives complete continuation to t0 on each compact preterminal time interval, without a uniform spatial gradient bound.

Write Theta(t)=[xi(t)]_(alpha,B_t), Y=log(e+Theta), Z=M tau^(c-1)+w. The localized Biot-Savart construction gives

    Lambda(sigma,t):=sup_E ||S|| <= wY/alpha+b(sigma,t),
    [S]_(alpha,E)<=C Theta+Cw m(t-sigma)+CZ,                  (2.1)

where b=2w log(1/(M(t-sigma)))+C(1+w+tau^(c-1)), m(h)=(Mh)^(-alpha)(1+log(1/(Mh))). All coefficients may be taken nonnegative. The source cutoff is1 near these balls and has support in 1/16<|x|<16. Its harmonic remainder has two controlled derivatives O(Z). The time kernel m is integrable because alpha<1.

## 3. The exact combined angular coefficient

The strain kernel satisfies, for a unit e,

    e.K(z)f e=-3(e.theta) f.(theta cross e)/(4pi |z|^3).

Its absolute angular integral is exactly1. For unit e,eprime and 0<alpha<=1 put M_alpha=eprime eprime^T-alpha e e^T and

    C_alpha=sup_(e,eprime) (3/(4pi)) integral |theta cross M_alpha theta|.

Thus the absolute combined kernel integrates on a shell to at most C_alpha w log(b/a). The triangle inequality gives C_alpha<=1+alpha. For e=e2,eprime=e1, its squared angular norm is

    theta1^2(1-theta1^2)+alpha^2 theta2^2(1-theta2^2)
                                  +2alpha theta1^2 theta2^2,

so C_alpha>=1. M_1 has eigenvalues0, plus/minus sin(beta), where beta is the angle between the two unit vectors. Orthogonal invariance and M_alpha=M_1+(1-alpha)ee^T give

    C_alpha<=c_K+1-alpha.                                (3.1)

Hence any gamma>c_K W0 admits alpha<1 with C_alpha W0/alpha<gamma. Alpha=1 is never used in the Holder estimate.

## 4. Exact series and the only computation

With theta=(sin t cos phi,sin t sin phi,cos t), the squared norm for diag(1,-1,0) is sin^2 t(1-sin^2 t cos^2(2phi)). Integrating phi gives

    c_K=(6/pi) integral_0^(pi/2) sin^2 t E(sin t)dt
        =(3pi/2) sum_(n>=0) b_n q_n,
    b0=1, b_n=r_n^2/(1-2n), r_n=(2n-1)!!/(2n)!!,
    q_n=(2n+1)!!/(2n+2)!!.

Here E(k)=integral_0^(pi/2) sqrt(1-k^2 sin^2 v)dv. The binomial expansion of1-sqrt(1-z) has nonnegative coefficients, so monotone convergence justifies both integrations and the series also at k=1. Every b_n for n>=1 is negative. Every finite partial sum is therefore an upper bound for c_K, with no estimated numerical remainder required.

The predeclared question and PASS criterion are in the team records. A one-core, low-priority Arb computation at160-bit precision through n=20000 gives

    (3pi/2) sum_(n=0)^20000 b_n q_n
      in [1.7796397789106419577757627028750602633170855 +/- 5.98e-44],

strictly below the exact rational177963978/100000000. The recorded PASS proves c_K<1.77963978. The source script explicitly tests only1.78, although its displayed partial sum suggests the sharper value; our independent comparison tests the claimed rational threshold directly. This calculation is only a scalar bound. Source quadrature and Monte Carlo are not used as proof.

## 5. Pair estimate with the separated scales retained

At time sigma<t take p1,p2 in E_(sigma,t), lambda=|p1-p2|<1, and xr=p2+r(p1-p2). Define

    Gamma=eprime.S(p1)eprime-alpha integral_0^1 e.S(xr)e dr,
    epsilon=min(d/2,exp(-Y(sigma)/alpha)), rho=epsilon+2lambda.

For each kernel integral split into B(x,epsilon), B(p1,rho) minus B(x,epsilon), and the exterior of B(p1,rho), where x=p1 or xr. In the first part, subtract the local source value and use zero spherical mean to get at most epsilon^alpha Theta/alpha<=1/alpha in absolute value. Each middle part has absolute bound w log((rho+lambda)/epsilon)<=Cw+w log^+(lambda/epsilon). Both bounds are valid also for the negative alpha weight.

In the far region, replacing xr by p1 costs at most Cw lambda/rho<=Cw because the kernel derivative is O(r^-4). The common kernel then gives C_alpha w log^+(1/rho)+Cw. Harmonic terms cost CZ. Since lambda<1,

    Gamma<=C_alpha w log(1/epsilon)
              +(1+alpha-C_alpha)w log^+(lambda/epsilon)+C(1+w+Z).

Using d>=M(t-sigma) gives

    Gamma<=(C_alpha/alpha)wY+(1+alpha)w log(1/(M(t-sigma)))
       +(1+alpha-C_alpha)w log^+(lambda exp(Y/alpha))+C(1+w+Z).   (5.1)

The separation-dependent term cannot be discarded. It is the main extra issue compared with simply adding two individual strain bounds.

## 6. Exact pair transport

For two characteristics Xi(sigma), write Delta=xi(X1)-xi(X2), lambda=|X1-X2|>0 and H=|Delta|/lambda^alpha. Subtracting the exact vorticity equations gives

    Delta'=S(X1)Delta+(S(X1)-S(X2))xi(X2).

The logarithmic separation derivative is integral_0^1 e.S(xr)e dr. The norm of Delta is absolutely continuous; at almost every zero its derivative is zero. Choosing any unit eprime there and eprime=Delta/|Delta| elsewhere yields almost everywhere

    H'<=Gamma H+w[S]_(alpha,E).

Consequently H(t) is bounded by its initial value times the integrated Gamma exponential plus the corresponding forcing integral. The initial value is bounded uniformly by Theta0 on a fixed compact annulus. Also

    lambda(sigma)<=lambda(t) exp(integral_sigma^t Lambda).       (6.1)

No division by a possibly zero vorticity difference is used in the resulting inequality.

## 7. Uniform remainder estimate from C49

Set F=K tau^-gamma, theta=W0/gamma and D(sigma,t)=F(t)-F(sigma). Under Y<=F on the earlier interval, Section6 of A1068-A1074 gives

    integral_sigma^t Lambda <=(theta/alpha+beta_K)D+r_K,
    beta_K->0, r_K->0 uniformly in sigma<t<T.                    (7.1)

This remains true for any fixed enlargement of the coefficient of b, with possibly different beta_K,r_K. For completeness, split the singular logarithm as

    log(1/(M(v-tau_t)))=log(1/(Mv))+log(v/(v-tau_t)).

The first part is bounded by C/K times F'. Cut the second logarithm at N=sqrt K. Its constant part costs O(K^-1/2)D, and the remainder integral is at most C exp(-sqrt K)/(1-exp(-sqrt K)). This proves the uniform estimate even at the time diagonal. It is not an application of ordinary Gronwall to a nonseparable kernel.

## 8. The extra loss is uniformly small on small terminal pairs

Assume theta_c=C_alpha theta/alpha<1, and take K large so eta_K=1-theta-alpha beta_K>0. Split terminal pairs at ell_t=(4w(t)exp(-F(t)))^(1/alpha). For lambda(t)>=ell_t the trivial vorticity bound gives H(t)<=exp(F(t))/2.

For lambda(t)<ell_t, (6.1)-(7.1) give

    log(lambda(sigma)exp(F(sigma)/alpha))
          <=L_t-(eta_K/alpha)D(sigma,t),
    L_t=(1/alpha)log^+(4w(t))+r_K.

The third term in(5.1) therefore integrates to at most L_t integral_(I_t)w, where I_t={sigma:D<alpha L_t/eta_K}; we used0<=1+alpha-C_alpha<=alpha<1. Put z_t=alpha L_t tau_t^gamma/(eta_K K). Uniform boundedness of tau^gamma(1+log^+(4W0/tau)) makes z_t<=1/2 for large K. Direct time integration gives

    integral_(I_t)w <=(W0/gamma)[-log(1-z_t)]
                    <=(2log2 W0/gamma)z_t.

The last inequality follows because [-log(1-z)]/z is increasing up to z=1/2. Thus the full extra loss is at most

    C/K sup_(0<tau<=tau0) tau^gamma[(1/alpha)log^+(4W0/tau)+r_K]^2,

which tends to zero. This is uniform in the pair and in the terminal time.

## 9. Closing the improved barrier

Apply Section7 to the other lower-order terms in(5.1). For all small terminal pairs and every earlier rho,

    integral_rho^t Gamma <=(theta_c+beta'_K)D(rho,t)+r'_K,
    beta'_K->0, r'_K->0.

The constants include the small loss of Section8. Let kappa_K=1-theta_c-beta'_K>0. Dividing the pair transport estimate by exp(F(t)), its initial term is at most exp(r'_K)Theta0 exp(-F(t0)). The Cw Theta forcing contributes at most

    exp(r'_K) C W0 tau0^gamma/(gamma K kappa_K),

because w/F'<=W0 tau0^gamma/(gamma K). The remaining forcing Cw^2 m+CwZ has integral at most C tau_t^-2. Its normalized contribution is at most

    C exp(r'_K) tau_t^-2 exp(-kappa_K K tau_t^-gamma).

The supremum of this expression tends to zero. All three contributions tend to zero uniformly. Thus, for large fixed K, every small terminal pair has H(t)<=exp(F(t))/4; the large pairs have the earlier one-half bound. Hence Theta(t)<=exp(F(t))/2 whenever Y<=F earlier.

Theta is continuous on compact preterminal intervals. Parameterize the moving closed ball by a fixed unit ball. The Holder quotient extends by zero to its diagonal uniformly in time because xi has a locally bounded spatial derivative and alpha<1; its maximum is continuous. Taking K so Y(t0)<F(t0) and exp(F(t0))/2>e, a first contact Y=F would contradict the preceding half bound. Therefore Y<F up to T. This supplies a direct continuation proof at the stated C2 profile regularity.

## 10. Returning to the profile and the strict decay gap

The unchanged local estimate on a smaller fixed ball gives

    ||Du(xstar,t)||<=(W0 K/alpha)tau^(-1-gamma)+Ctau^-1.

Choose tau=|y|^(-1/c), making xstar a unit vector. Multiply by tau in the exact derivative scaling. The Holder scaling is

    [Omega]_(alpha,B(y,|y|/4))
       =tau^(1+c alpha)[xi]_(alpha,B(xstar,1/4)).

Both yield(1.1), uniformly in direction. Rotations are orthogonal, so every finite omega is covered.

For(1.2), choose omega_inf<W0<c delta_star/c_K and c_K W0<gamma<c delta_star, then alpha as in Section3. Let delta=gamma/c. If delta<1/2, A498(A) turns the polynomial bound into DU->0. Otherwise delta<5/4, c delta<1, and U=O(r^-kappa)=o(r^(1-2delta)); A757 applies. Only after this gradient decay is established do A492 and A476 give Omega and DU of order1/r. There is no circular use of that final decay in the growth estimate.

The thresholds are c/(2c_K)>0.28095c for bounded U, at least c/c_K>0.5619c when kappa>=1, and1/(2c_K)>0.28095 for the natural velocity tail with2/5<c<1/2. In the last case delta_star=1/(2c). Equality and all values above the threshold remain open to this method.

For every fixed physical rho>0, tau||xi||_(|x|>=rho) tends to omega_inf by exact rescaling. Below the bounded-velocity threshold, ||Du||_(|x|>=rho)<=C rho^-1 tau^(c-1). This is an exterior estimate, not a global continuation theorem.

## 11. The divergence-free refinement and its exact limits

For M symmetric and k(theta)=theta cross Mtheta, let phi in C1(S2) and Phi(z)=phi(theta)/|z|^2. Then grad Phi=(grad_S phi-2phi theta)/|z|^3. Adding this gradient to the far-shell kernel changes its integral against the localized divergence-free source only by sphere boundary terms and cutoff-divergence terms. Each is O(w) with constants depending on phi. The angular coefficient for fixed directions can therefore be replaced by

    d_alpha(e,eprime)=inf_phi (3/(4pi)) integral_S2
                    sqrt(|k-grad_S phi|^2+4phi^2).

The theorem needs the supremum over the pair directions and uniform remainder constants. For any fixed positive tolerance, compactness of the direction-pair space supplies these: choose an almost-minimizing phi at each pair, then a finite neighborhood cover using continuous dependence of the integrand on M. Take the maximum of the finitely many phi-dependent constants. Use a coefficient strictly above that supremum, so the tolerance is absorbed. The additional condition gamma>W0 retains the required theta<1 for backward separation. This completes the quantifiers left implicit in source Remark R2.

At alpha=1, rotational invariance and homogeneity reduce the optimized coefficient to sin(beta) times the coefficient for diag(1,-1,0). For that diagonal matrix k=(yz,xz,-2xy). Its spherical divergence is zero, but div_S(k/|k|)=-2xyz/|k|^3 away from its zeros, so the unrestricted maximizing direction field is not divergence free in general.

The reported optimization values near1.712 are not certified and were not rerun. They neither prove a lower bound for the infimum nor exclude further gains from other phi. The source sentence that this form of the constraint does not bring the coefficient near1 is unsupported if meant as a mathematical obstruction. It can only describe the tested finite-dimensional trials.

## 12. Evidence and scope

All seven C50 sections, its full check script, and the full twelve-section C49 independent proof were read. The principal combined-kernel theorem and its strict conditional corollaries pass. The independent scalar certificate, script and actual timestamp are retained; the source numerical optimizer is not a proof input.

Continuing file-based collaboration is with Theory Agent A, configured as the primary model. Its runtime provider identity is not independently attested. No additional client or agent is launched. A focused response to the R2 quantifier and lower-bound limitations is requested through the agent notes.

There is no proof above the strict threshold, no proof of vorticity decay from velocity decay alone, no endpoint or optimality assertion, and no resolution of the arbitrary-helicity bare-decay nonexistence conjecture.
