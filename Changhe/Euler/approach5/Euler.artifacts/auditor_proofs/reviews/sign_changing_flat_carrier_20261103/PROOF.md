# An isolated flat carrier with both signs of the Euclidean pressure source

Status: independent reconstruction of LIT306, prepared for complete existing coordinator comparison. No full-system scalar or pressure completion is constructed.

## 1. Exact statement and geometry

Fix 0<c<1/2 and any finite omega in R. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J and a=1-2c. Let sigma be a smooth transverse section on a disc about0 in R2, taking values in R3 minus{0}, with det(sigma_1,sigma_2,X(sigma)) nonzero. On a sufficiently small finite flowbox about sigma(0), there exists smooth V satisfying

    div V=0, X.V=0, DV X=-LV, W=curl V.                    (C)

Its zero set is precisely the central X-orbit segment Gamma, and all derivatives of V vanish on Gamma. On every sufficiently small section disc the two actual ratios

    Qnorm=|W|/|V|, Qparallel=|W.X|/|V|

belong to every Lp,0<p<2. For each of them and each finite C0>=0, the positive part (Q-C0/|y|)_+ is not L2 on any centre disc. There are sequences approaching the centre on which tr((DV)^2) is positive, and other such sequences on which it is negative. The same property holds near every point of the smaller orbit segment by exact transport.

All constants depend only on the chosen parameters, fixed geometry and construction. They need not be uniform in omega. The assertion concerns C alone; it does not supply any scalar S or pressure relation of the common-flat system F.

Choose a fixed relatively compact section disc. Write

    m=|X(sigma)|, beta_i=X(sigma).sigma_i/m^2,
    T_i=sigma_i-beta_i X(sigma), g_ij=T_i.T_j,
    j=|det(sigma_1,sigma_2,X(sigma))|=m sqrt(det g),
    nu=1/j, M=g/j, b=(3c-1)beta.

The positive functions m,j and the least eigenvalue of M have positive lower bounds. Every derivative of each fixed order is bounded. The planar rotation J2 sends e_r to e_theta.

## 2. Sparse perturbations preserve a nonzero gradient and all-order flatness

For 0<r<R<exp(-e), set t=log(1/r), f(r)=exp(-t log t), and psi0(y)=integral_0^|y| f(s)ds. Then grad psi0=f e_r, f'=(log t+1)f/r, and every fixed derivative of f is O(r^N) for every N. Indeed f^(k)=r^-k P_k(t)f, with P_(k+1)=(log t+1-k)P_k-P_k'; each P_k is bounded by a constant times (1+log t)^k. The factor exp(-t log t) absorbs every fixed exponential and logarithmic power. The radial function psi0 consequently extends smoothly and flatly at0.

Choose smooth phi compactly supported in the unit disc, with phi(0)=0, grad phi(0)=0 and D2phi(0)=diag(1,-1). Let Mphi>=max(1,sup|grad phi|), epsilon=1/(16Mphi), and for all large integers n put

    r_n=2^-n, y_n=(r_n,0), ell_n=r_n^3/100,
    f_n=f(r_n), eta_n(y)=epsilon f_n ell_n phi((y-y_n)/ell_n).

Take the first index large enough that the discs B_n=B(y_n,ell_n) are disjoint and lie in the section, f_n/2<=f(r)<=2f_n whenever |r-r_n|<=ell_n, and f_(n+1)<=f_n/2. The first comparison follows by integrating (log f)' over an interval of length2ell_n: its variation is O(r_n^2 log log(1/r_n)), which tends to0. The second follows because log(f_(n+1)/f_n)=-integral_(n log2)^((n+1)log2)(log u+1)du tends to minus infinity.

Set psi=psi0+sum eta_n and u=J2 grad psi. On B_n,

    |D^k eta_n|<=C_k f_n ell_n^(1-k).

These bounds decay faster than every power of r_n, and |y| is comparable to r_n on the disc. The disjoint supports therefore give a smooth flat extension of the sum at0, including all derivatives, by successive difference quotients. At any point at most one bump is active and |grad eta_n|<=f_n/16<=f(r)/8. Consequently

    psi_r>=7f/8, |grad psi|<=9f/8,
    div u=0, u_theta=psi_r>0.                              (1)

The perturbation changes the Hessian substantially without creating a critical point off0.

## 3. The generalized radial correction has a small first derivative

Write b_r=b(r e_r).e_r and define

    E(r,s,theta)=exp(integral_s^r b_r(v,theta)dv),
    q(r,theta)=r^-1 integral_0^r s b(s e_r).u(s e_r)
                                      E(r,s,theta)ds,
    w=u+q e_r.                                             (2)

Then q_r=b_r q+b.u-q/r, and div w=b.w exactly. We prove the uniform bounds

    |q|<=C r f, |D_y(q e_r)|<=C f.                          (3)

The background u0=f e_theta has the already elementary bounds |q0|+|q0_theta|<=Crf, |q0_r|<=Cf, obtained directly from monotonicity of f and differentiation of the integral. For each p_n=J2 grad eta_n, let q_n be its linear contribution to q. A ray meets B_n in an interval of radial length at most2ell_n, with radial coordinate comparable to r_n. On that interval |p_n|<=C epsilon f_n and |D p_n|<=C epsilon f_n/ell_n. Differentiation in theta contributes a factor s to Dp_n. Smooth coefficients and their angular derivatives are uniformly bounded. Therefore

    |q_n|<=C epsilon r_n ell_n f_n/r,
    |q_n_theta|<=C epsilon r_n^2 f_n/r.                     (4)

To obtain the second estimate, integrate the largest derivative term, of size C epsilon r_n f_n/ell_n, over a length at most2ell_n, then include the weight s/r. Terms differentiating b or E are smaller. The smooth compact support permits differentiation before integration; no moving-boundary term is introduced.

A contribution is zero unless r>=r_n-ell_n, which implies r_n/r<=2. Thus (4) bounds |q_n|/r and |q_n_theta|/r by C epsilon f_n. The equation q_n_r=b_r q_n+b.p_n-q_n/r gives |q_n_r|<=C epsilon f_n as well. It also gives |q_n|<=C epsilon r f_n after enlarging the constant.

Let m0 be the first radially eligible index at a given r. If r>=r_m0, monotonicity gives f_m0<=f(r). If r<r_m0, eligibility forces r_m0-ell_m0<=r<r_m0, and the narrow-annulus comparison gives f_m0<=2f(r). All contributing indices on any fixed ray are a subset of this radial tail. Hence

    sum_(contributing n) f_n<=sum_(n>=m0)f_n
                              <=2f_m0<=4f(r).             (5)

This argument avoids a false uniform comparison between f(2r) and f(r). Summing (4) and the radial derivative bounds proves (3). The sums of these first derivatives converge by the displayed majorants, so termwise differentiation here is justified.

For all higher derivatives use the original integral rather than a support estimate. Substituting s=r tau gives

    q=r integral_0^1 tau b(r tau e_r).u(r tau e_r)
        exp(r integral_tau^1 b(r v e_r).e_r dv)d tau.

Every fixed mixed polar derivative of u at radius r tau is bounded by an arbitrarily high power of r tau, uniformly for 0<=tau<=1. Differentiating the other factors gives uniformly bounded coefficients. Differentiation under this fixed-interval integral therefore shows that every mixed derivative of q is O(r^N) for every N. Cartesian derivatives add only fixed negative powers of r. Thus q e_r and w extend smoothly and flatly at0. The positive tangential component in (1) is unaffected by a radial correction, so

    c1 f<=|w|<=c2 f                                         (6)

and w has no other zero.

## 4. Exact lift and Euclidean squared-trace formula

Set v=w/j, h=-beta.v, Phi(y,s)=exp(sA)sigma(y), and

    V(Phi(y,s))=exp(-s)D Phi(y,s)(v(y),h(y)).                (7)

In these coordinates X=partial_s. Thus [X,V]=-V and DV X=(A-I)V=-LV. The conformal orthogonal form of exp(sA), together with h=-beta.v, gives X.V=0. The volume density is exp(3cs)j, so

    div V=exp(-s)j^-1[div w-(3c-1)beta.w]=0.

All three equations C hold, the zero set is exactly Gamma, and V is flat there. Since V(sigma)=T_i v_i and the quotient metric is positive definite, |V(sigma)| is bounded above and below by positive multiples of f.

Let K=D_y^2 psi. By (3),

    D_y v=nu J2 K+O(f), |v|+|h|<=Cf,
    |D_y h|<=C(|K|+f).

For symmetric two-by-two K, tr((J2 K)^2)=-2 det K. This is not yet the Euclidean trace. Put Fmat=D Phi, Z=exp(-s)(v,h). Differentiating V composed Phi=Fmat Z gives exactly

    Fmat^-1 DV(Phi)Fmat=D_z Z+Cmat,
    (Cmat)_i=Fmat^-1(partial_i Fmat)Z, |Cmat|<=Cf.

At s=0, D_z Z has blocks [[D_y v,-v],[D_y h,-h]]. Its squared trace is tr((D_y v)^2)-2(D_y h).v+h^2. Trace is invariant under conjugation, and every term involving Cmat is O(f(|K|+f)). We obtain

    tr((DV)^2)(sigma(y))
       =-2nu(y)^2 det K(y)+O(f(r)(|K(y)|+f(r))).            (8)

The constants are uniform on the fixed small section. This formula retains every moving-frame contribution.

## 5. Positive and negative trace sequences

At the bump centre y_n, its Hessian and the radial Hessian are diagonal in the fixed planar coordinates:

    K(y_n)=diag(f'_n+A_n, f_n/r_n-A_n),
    A_n=epsilon f_n/ell_n.

The ratio (f'_n+f_n/r_n)/A_n is bounded by a constant times (ell_n/r_n)(log log(1/r_n)+2), hence tends to0. Thus det K(y_n)=-A_n^2(1+o(1)). The error in (8), divided by A_n^2, is O(f_n/A_n+(f_n/A_n)^2), which tends to0. Since nu is bounded below away from0, the actual Euclidean trace is positive at all sufficiently late bump centres.

Choose a fixed angular sector about pi, disjoint from all the small bump discs. Its entire rays avoid every bump. Both p_n and its integrated radial correction q_n vanish there, so the original radial carrier is recovered on an open sector. The eigenvalues of K are f' and f/r. Formula (8) becomes

    tr((DV)^2)=-2nu^2 ff'/r+O(ff'+f^2/r+f^2)<0

near0 in that sector, since f'>=f/r and the error/main ratio is O(r). In particular z_n=(-r_n,0) gives the negative sequence.

The exact transport from C is

    DV(exp(sA)x)=exp(-s)exp(sA)DV(x)exp(-sA).

The trace therefore scales by exp(-2s). Both sign sequences transport to every point of the smaller central orbit; the trace is zero on that orbit by flatness.

## 6. Actual curl ratios and the endpoint failure

The lift and its derivative bounds give |W|<=C(|K|+f) on the section. Since |V|>=c f and f is comparable to f_n on B_n,

    Qnorm+Qparallel
       <=C[1+(log log(1/r)+1)/r
                     +sum ell_n^-1 indicator_(B_n)].       (9)

For 0<p<2 the background pth-power integral converges by the substitution t=log(1/r), yielding an exponential exp(-(2-p)t) times a logarithmic power. The disjoint bump terms contribute at most C_p sum ell_n^(2-p), a convergent geometric series. Subadditivity for p<=1 and the two-term power inequality for p>1 complete the bound. Thus both actual ratios lie in every asserted Lp.

For a direct lower bound work on the fixed untouched sector. Pull back the velocity one-form to the section as theta_i=V(sigma).sigma_i. It equals theta=Mw, with M=g/j positive definite. Differentiate its planar curl. The leading radial derivative is

    partial_1 theta_2-partial_2 theta_1
       =f' e_theta^T M e_theta+O(f/r).

Indeed D(f e_theta)=f' e_theta tensor e_r-(f/r)e_r tensor e_theta; derivatives of M and of q0 e_r contribute O(f), and the remaining basis derivative is O(f/r). The leading coefficient has a fixed positive lower bound. On the other hand C gives X cross W=aV, so

    W=(W.X)X/m^2+a(V cross X)/m^2.

Using d(theta) on the section and its fixed orientation sign delta gives

    partial_1 theta_2-partial_2 theta_1
       =W.(sigma_1 cross sigma_2)
       =delta j(W.X)/m^2+O(f).

Since rf'/f=log log(1/r)+1 tends to infinity, the leading term dominates the O(f/r) error. Hence both Qparallel and Qnorm are at least a positive multiple of log log(1/r)/r on this fixed positive-angle sector. For any finite C0, their positive parts above C0/r are eventually bounded below by half that quantity. Its square integral diverges because it contains a positive multiple of integral (log log(1/r))^2 dr/r. No L2+C0/r majorant is possible on any centre disc. This lower bound is direct and uses no continuation theorem.

## 7. Comparison and exact limits

All seven sections of the LIT306 submission were read. The sensitive first-derivative estimate uses the short radial support of the angular derivative, not a pointwise small-Hessian assertion. The contributing indices on a ray need only be a subset of the radial tail in (5). The all-order extension follows from the fixed-interval integral and smooth flatness of u. The Euclidean sign depends on (8), including its moving-frame correction. These are the steps to be compared by the existing coordinator agent.

The constructed field retains exact carrier equations, an isolated flat orbit, every subcritical Lp bound and failure of every L2+C0/r majorant. Those retained properties therefore do not force a nonpositive pressure source near the orbit. The result is consistent with LIT305, whose uniformly negative sign applied to its specific radial circulating family. No scalar S, its first-integral identity, its sign or zero set, or its pressure-Poisson relation is supplied. Positive trace somewhere in every neighbourhood is one necessary condition from C61, not sufficient for a full-F solution. No global decaying Euler profile or unrestricted nonexistence proof follows.

Comparison completed 2026-11-03T23:48:50.865754+00:00: all eleven items of the existing coordinator comparison were read in full, pinned as in the team records, sha256 c44f40c8b84b94f3da9a39c41a3cf724d79ffb5d277f1aa34eb21a384caf52de. The submitted source hash exactly matches its original pin. The radial-tail wording clarification is already explicit in Section3. No mathematical gap was found. The local conclusions are CONFIRMED A2580-A2586; broader conclusions are OPEN A2587. Existing configured model collaboration was through files; provider execution is not independently attested.
