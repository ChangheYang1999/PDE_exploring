# Different source stability orders near the Hardy minimum

## 1. Exact statements and dependencies

Let U be a real C1 divergence-free field on R3. Assume E(R)=integral_(|y|<R)|U|^2 satisfies E(R)/(LR^beta)->1, where L>0 and0<beta<1. Use Cartesian derivatives, sphere measure4pi, and set

    t=(beta-3)/2, k=t+2=(beta+1)/2, m=2-beta,
    D=k^2+2, K0=D/2, H=t^2(k^2+4)/D,
    C_s=mt^2/D, C_n=2kt^2 sqrt(k/(k+3))/D, C_p=C_s+C_n.

For r=|y| define q=tr((DU)^2), Q(r)=integral_S2 q(rn)dn and

    G=integral_(1<r<R)r^(2-beta)|DU|_F^2,
    I=integral_(1<r<R)r^(2-beta)[q]_+,
    N=integral_(1<r<R)r^(2-beta)[-q]_+,
    J=integral_1^R r^(4-beta)[Q(r)]_+dr,
    K_-=integral_1^R r^(4-beta)[-Q(r)]_+dr.

Suppose limsup G/(beta L log R)<=H+delta with0<=delta<=beta. For ell>=1 let lambda_ell=ell(ell+1), K_ell=1+k^2/lambda_ell, x_ell=k^2/(lambda_ell+k^2), and M_ell=t^2+lambda_ell-2beta lambda_ell/(lambda_ell+k^2). Put

    a_beta=m beta(x_1-x_2)/(M_2-H),
    b_beta=(10/beta)(1+H/C_s), c_beta=m/2+b_beta.

Then

    limsup K_-/(beta L log R)<=b_beta delta,
    C_s-a_beta delta<=liminf J/(beta L log R)
       <=limsup J/(beta L log R)<=C_s+c_beta delta.

All constants are positive and finite for each fixed beta. These statements hold at every fixed center with the same gradient budget. The linear order in delta cannot be improved to little-o(delta) in this class. In contrast, deviations of I and N from C_p and C_n can have a nonzero square-root order, with either sign at the same gradient excess.

The proof below reconstructs all eight source sections and56analytical obligations of LIT389, source39329b9b, retained in `verification`. It uses the confirmed tangential envelopes A3152-A3153, rederives the needed matrix estimate, and uses A3053 only in the final Euler application. The entire quantitative estimate also agrees with the now confirmed A3161, but does not require that result as an unproved premise.

## 2. Full-mode localized matrix control

Set z=log r, U(rn)=r^t v(z,n), and A=r^(1-t)DU(rn). Define F_eta,T_eta,G_eta as the integrals against eta(z) of the sphere norms |v|^2, |v_T|^2 and |A|_F^2. The uncut F(R)=beta L log R+o(log R) by Stieltjes integration. Every fixed-width logarithmic velocity strip has O(1) energy. This follows directly from E(R)=O(R^beta), not by differentiating its remainder.

The divergence relation is (partial_z+k)(v.n)+div_S v_T=0. The radial degree-zero mode vanishes because the flux through every sphere is zero. For a normalized real harmonic Y of eigenvalue lambda=ell(ell+1), the poloidal and toroidal fields are fY n+g grad_S Y, with g=(f'+kf)/lambda, and h n cross grad_S Y. Their sphere energies satisfy

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                                      +(lambda-2)f^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].

These identities use the Cartesian derivative, the moving normal, and integral|Hess_S Y|^2=lambda(lambda-1). Write

    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    gamma=t^2+2-H=4beta/D.

For smooth compactly supported eta>=0, expansion gives

    integral eta(D_pol-HK_pol)
      =integral eta[f''^2/lambda+b_lambda f'^2+d_lambda f^2]
       -(k+t)/lambda integral eta'f'^2
       -[2t+((k+t)tk-Hk)/lambda]integral eta'f^2
       +tk/lambda integral eta''f^2,
    integral eta(D_tor-HK_tor)
      =lambda integral eta[h'^2+(lambda-2+gamma)h^2]
       -t lambda integral eta'h^2.

Here b_lambda>=1, d_2=0, d_lambda>=4lambda/9 for lambda>=6, and gamma>=4beta/3. For the higher-degree inequality use d_lambda>=lambda-3-2/lambda; after subtracting4lambda/9 the difference is zero at6 and strictly increasing. Let q_pol=f''^2/lambda+b_lambda f'^2+d_lambda f^2 and q_tor=lambda[h'^2+(lambda-2+gamma)h^2], and let Q_eta denote their nonnegative integrated sum. Since f'^2/lambda<=2lambda g^2+2k^2f^2/lambda,

    |Q_eta-(G_eta-HF_eta)|
       <=C_beta integral(|eta'|+|eta''|)|v|^2.

Let a(z) be the three degree-one radial coefficients relative to sqrt(3/(4pi))n_i. Freeze them in

    v0(a,n)=sqrt(3/(4pi))/2[k a-t(a.n)n],
    M0(a,n)=D_y[|y|^t v0(a,y/|y|)] at y=n.

Then integral|M0|^2=H K0|a|^2. For one low coefficient the exact matrix error is2f'^2+[f''+(k+t)f']^2/2, at most3times its nonnegative gap. For higher poloidal modes, D_pol<=3f''^2/lambda+7f'^2+(lambda+16)f^2<=10q_pol. For toroidal modes D_tor<=5q_tor/beta: use D_tor<=2lambda h'^2+lambda(lambda+2t^2)h^2, compare coefficients at lambda=2, and then compare their positive slopes. Orthogonality of integrated matrix families gives

    integral eta integral_S2|A-M0|^2<=(10/beta)Q_eta.

All error constants are independent of degree. C1 regularity makes the harmonic coefficients C1, and the divergence relation makes each f C2. Finite harmonic sums converge in local angular H1 and radial derivative L2; uniform cutoff bounds and monotone convergence of the nonnegative main sums pass the estimates to the entire field. No angular truncation remains.

## 3. Quadratic control of negative spherical source

Put A0=K0|a|^2 and e=integral_S2|A-M0|^2. The frozen sphere integrals are

    integral tr(M0^2)=C_s A0,
    integral|M0|^2=H A0.

If Qflat=integral tr(A^2), matrix expansion and Cauchy-Schwarz give

    Qflat>=C_s A0-2sqrt(H A0 e)-e
          =C_s[sqrt(A0)-sqrt(H e)/C_s]^2
                                      -(1+H/C_s)e.

Thus [-Qflat]_+<=(1+H/C_s)e, including A0=0. This estimate applies after sphere integration. It has no pointwise analogue here because tr(M0(n)^2) has both signs.

For Z=log R choose 0<=eta^+<=1 supported in(0,Z+log2), equal to1 on(log2,Z), with uniformly bounded first two derivatives. Then F_eta/(beta L Z)->1 and G_eta<=G(2R), so limsup Q_eta/(beta L Z)<=delta. Since Qflat=r^(2-2t)Q(r), the z-integral of [-Qflat]_+ is K_-. The upper cutoff controls K_-(R) up to the fixed, finite inner contribution. The matrix estimate proves limsup K_-/(beta L log R)<=b_beta delta without a moving derivative-shell estimate.

## 4. Linear stability of the positive spherical source

For C1 solenoidal U, q=partial_i partial_j(U_iU_j) holds in distributions. Test against phi(r)=r^m eta(log r). Its radial and tangential Hessian coefficients are

    phi''=r^(m-2)[m(m-1)eta+(2m-1)eta'+eta''],
    phi'/r=r^(m-2)[m eta+eta'].

Consequently, with S_eta=integral eta Qflat,

    S_eta=m(1-beta)F_eta+m beta T_eta
       +integral[(2m-1)eta'+eta''](v.n)^2
       +integral eta'|v_T|^2.

The final terms are O(1) for the chosen cutoffs by velocity strips alone. The compact-cutoff inequality in A3153 is

    G_eta>=(t^2+2-2beta)F_eta+2beta T_eta-C.

It follows by the nonnegative poloidal, derivative and toroidal mode weights; their costs all lie above the affine line with slope2beta through(x_1,H). The derivative-weight cutoff has1/lambda and its cost has lambda, so the error is uniform. Since t^2+2-2beta=H-2beta x_1 and m(1-beta+beta x_1)=C_s,

    S_eta<=C_s F_eta+(m/2)(G_eta-HF_eta)+C.

Add the negative-source estimate from Section3, using [Qflat]_+=Qflat+[-Qflat]_+, and use eta^+. This gives the asserted upper bound C_s+c_beta delta.

Choose 0<=eta^-<=1 supported in(0,Z), equal to1 on(log2,Z-log2), with uniformly bounded first two derivatives. Nonnegativity then gives J>=S_eta. A3152 supplies liminf T/(beta L log R)>=d_opt(H+delta); removing velocity strips costs O(1). The exact gap is

    M_2-H=4-8beta k^2/[(6+k^2)(2+k^2)]>10/3>beta.

The first strict inequality follows already by bounding the subtracted term by2/3. Thus H+delta stays in the first affine segment, and

    d_opt(H+delta)=x_1-(x_1-x_2)delta/(M_2-H).

Substitution in the signed-source identity proves the lower coefficient C_s-a_beta delta. The proof never removes a gradient boundary term by assumption.

## 5. Exact mixed source and the moving negative belt

Let mu=n.e3 and use Y_1=sqrt(3/(4pi))mu, Y_3=sqrt(7/(4pi))(5mu^3-3mu)/2. Define the unit-energy poloidal modes p_ell=[Y_ell n+(k/lambda_ell)grad_S Y_ell]/sqrt(K_ell). For an unnormalized polynomial Y set B=(k/lambda)Y', A0=Y-mu B and sigma=sqrt(1-mu^2). In the frame(n,(e3-mu n)/sigma,e_phi), the derivative at r=1 of r^t[Y n+(k/lambda)grad_S Y] is

    D_Y=[[tY, sigma(Y'-B), 0],
         [t sigma B, A0+(1-mu^2)B', 0],
         [0, 0, A0]].

This is a homogeneous Cartesian derivative. The frame formula extends to the poles by continuity of its scalar invariants. For Y=mu, B=k/2 and A0=-t mu/2. For Y=(5mu^3-3mu)/2, B=k(5mu^2-1)/8, and

    A0=mu[(20-5k)mu^2+k-12]/8,
    A0+(1-mu^2)B'=mu[(20-15k)mu^2+11k-12]/8.

Multiplying these two matrices yields

    tr(D_1D_3)=t/8[5(k-4)(k+3)mu^4
                         -6(k^2-4k-6)mu^2-k(7-k)].

For s0=sqrt(k/(k+3)), its integral from-s0 to s0 is

    (t s0/4)[(k-4)(k+3)s0^4
                  -2(k^2-4k-6)s0^2-k(7-k)]
        =-9tk s0/[4(k+3)].

The bracket reduces to-9k/(k+3). Restoring both normalization factors and2pi dmu gives

    integral_(|mu|<s0)tr(Dp_1Dp_3)dn
       =-9sqrt(21)tk s0/[8(k+3)sqrt(K_1K_3)]>0.

For sufficiently small positive or negative epsilon choose the exterior field

    U_ext=sqrt(beta L)r^t[sqrt(1-epsilon^2)p_1+epsilon p_3].

Integrated orthogonality gives velocity coefficient beta L, gradient coefficient H+(M_3-H)epsilon^2, and tangential fraction x_1+(x_3-x_1)epsilon^2. Its normalized source is

    q_epsilon=(1-epsilon^2)tr(Dp_1^2)
       +2epsilon sqrt(1-epsilon^2)tr(Dp_1Dp_3)
       +epsilon^2tr(Dp_3^2).

At epsilon=0 it is a positive multiple of(k+3)mu^2-k. The two zeros+-s0 are simple. Away from small neighborhoods of them, compactness preserves the sign for small epsilon; the implicit function theorem gives exactly one zero in each neighborhood. The positive-part integrals are C2 functions of epsilon. In their first derivatives the moving-endpoint terms vanish because the integrand is zero there. Hence

    integral[-q_epsilon]_+=C_n-A_beta epsilon+O_beta(epsilon^2),
    A_beta=-9sqrt(21)tk s0/[4(k+3)sqrt(K_1K_3)]>0.

The signed sphere integral is exactly C_s+m beta(x_3-x_1)epsilon^2 and remains positive. This follows either from the radial Hessian identity on a homogeneous tail or from integrated mode orthogonality. Therefore the positive sphere integral is C_p-A_beta epsilon+O_beta(epsilon^2), whereas the positive part of the signed sphere integral is exactly C_s+m beta(x_3-x_1)epsilon^2.

## 6. Complete smooth controls and sharp orders

For ell=1,3 put c_1=sqrt(beta L(1-epsilon^2)/K_1) and c_3=sqrt(beta L/K_3)epsilon, and set

    V_ell=f_ell(r)Y_ell n
                 +(r f_ell'(r)+2f_ell(r))grad_S Y_ell/lambda_ell.

Take f_ell=c_ell r^t outside2 and f_ell=c_ell2^(t-ell+1)r^(ell-1) inside2-h, with a smooth transition. Matching their values at2 makes their difference O(h) on the transition, so f and f' remain bounded as h decreases. Each inner field is c_ell2^(t-ell+1)/ell times grad(r^ell Y_ell), smooth at0. Its limiting energy inside2 is2^beta c_ell^2/ell. Since beta/(ell K_ell)<1, the sum is strictly below L2^beta. The transition energy vanishes with h; fix h<1 leaving a positive deficit Delta.

Let psi be a nonnegative smooth radial function supported in r<1/2 and equal to1 near0. Set W=psi(r)Jy with Jy=e3 cross y. This is solenoidal and pointwise perpendicular to both zonal poloidal fields. Thus U_epsilon=V_1+V_3+a0W, with a0=sqrt(Delta/integral|W|^2)>0, has E(2)=L2^beta. Exterior integration gives E_0(R)=LR^beta for R>=2. All exterior derivatives have order r^(t-j).

The critical source weight integrates the homogeneous source as log R. Thus

    G/(beta L log R)->H+(M_3-H)epsilon^2,
    N/(beta L log R)->C_n-A_beta epsilon+O_beta(epsilon^2),
    I/(beta L log R)->C_p-A_beta epsilon+O_beta(epsilon^2),
    J/(beta L log R)->C_s+m beta(x_3-x_1)epsilon^2,
    K_-(R)=O_epsilon(1).

Each moment has only an additional finite core contribution. Set delta_epsilon=(M_3-H)epsilon^2 and restrict epsilon further so delta_epsilon<=beta. The two signs of epsilon give the same delta and opposite leading I,N deviations. Their absolute square-root coefficient is A_beta/sqrt(M_3-H)>0. The nonzero absolute J coefficient relative to delta is m beta(x_1-x_3)/(M_3-H)>0. Thus no uniform little-o square-root improvement for I,N, or little-o linear improvement for J, is possible in this kinematic class. No claim about optimal constants follows.

## 7. Pressure, actual momentum and changes of center

Near0 the field equals grad Phi+a0Jy, with Phi a linear plus cubic harmonic polynomial. Its vorticity is the constant2a0e3 in a whole neighborhood and DU(0)=a0J. For

    F_(c,omega)=(1-c)U+[((cI-omega J)y+U).grad]U+omega JU,

set B=(cI-omega J)y+U. Its curl is Omega+B.grad Omega-(Omega.grad)U+omega JOmega. At0 this equals2a0e3 for every real c,omega. The constant degree-one velocity causes no transport term because Omega is constant nearby. A pressure gradient cannot repair this nonzero curl.

The smooth source q is O(r^(beta-5)). Its Newton potential integral q(x)/(4pi|y-x|)dx is absolutely convergent, since the radial tail has order r^(beta-4), and is smooth with -Delta P=q. This is only the Poisson relation.

Both poloidal fields are even under y->-y and the compact swirl is odd. The cross energy vanishes pointwise, so |U_epsilon|^2 is even. Its ball-energy first center derivative vanishes at0. The second center derivatives equal boundary integrals of first derivatives of |U|^2 and have order R^(beta-2). Taylor's theorem, with fixed center, proves E_a(R)=LR^beta+O_(a,epsilon)(R^(beta-2)). In the exterior, a translation changes the derivative-square or source density by O(r^(2t-3)); after multiplication by the critical weight and radial measure the error is O(r^-2). The positive-part map is Lipschitz, including after the sphere integral. Hence every centered moment above differs by O_(a,epsilon)(1).

For the general inequalities, center invariance follows from the unchanged energy ratio and the same normalized gradient limsup. Outside a sufficiently large fixed ball the radial weights differ by factors1+-eta; ball inclusions shift R by a fixed amount and the omitted inner integrals are finite. Take limsups, then eta->0. This includes infinite limsups and does not translate the Euler equation.

## 8. Euler scope

For a nonzero full rotating profile with U,P in C1, bounded U, U(R.) tending to0 distributionally on compact sets, and2/5<c<1/2, A3053 gives the energy ratio with beta=5-2/c and L>0. The inequalities in Section1 apply for every finite omega if the additional gradient budget holds. Uniform velocity decay provides the bounded distributional premises, not that extra budget.

All eight source sections,56checks and the formal-source scope note have been read. The existing coordinator comparison is reconciled in Section9. Collaboration is through the existing configured model working files; actual provider execution is independently unattested. No new model client, symbolic computation, root evaluation or formal build was used in this audit. The source's optional algebra logs are not certified.

The quantitative estimates and sharp orders are kinematic. No explicit control is an Euler profile. Optimal constants, a full-mode extremum for I at a positive gradient excess, automatic gradient control, automatic source sign and unrestricted rotating nonexistence remain open.


## 9. Independent comparison and both signs of the linear J deviation

The complete coordinator comparison ab5a663e4d0210d883e996e257574d2ca3db70a5e18bd019e3b8c0dab6258a14 has183lines. Its Sections1-8 and remarks R1-R8 have been read. All analytical statements agree with Sections1-8 above. The exact finite-mode and numerical diagnostics are not certified by this audit.

R1 is resolved by specifying 0<=eta^+<=1 and0<=eta^-<=1 in Sections3-4. Such standard smooth cutoffs have the stated fixed-width strips and uniform derivative bounds. R3 is already enforced by choosing |epsilon| below a beta-dependent threshold before applying the implicit function theorem. R4 is correct: the negative-spherical estimate and upper J bound require only finite delta>=0. The stated delta<=beta is a sufficient restriction for the first affine segment in the lower J bound. R5 is retained: this result alone claims no sharpness for K_-. R6 concerns reused notation only.

For R7, the audit uses the already confirmed complete all-mode theorems A3146, A3152 and A3153, with the full-field limit recalled in Section2. The completion and Newton potential in Sections6-7 have been checked directly, not inferred from selected symbolic samples. The Euler use is exactly A3053 with its boundedness, C1/C1 and distributional blow-down premises. For R8, linear versus square-root order is an asymptotic improvement as delta tends to0 for fixed beta; no comparison of the numerical values of the two explicit bounds on the whole interval is claimed.

R2 suggests a positive as well as negative linear deviation of J. This follows analytically from the already confirmed smooth completions in A3157-A3158, without any new numerical test. Take their aligned degree-one poloidal/toroidal mixture with poloidal energy fraction rho=1-theta, where0<theta<1. Its exterior velocity energy is normalized to beta L. The two family coefficients are

    M=H+gamma theta, gamma=4beta/D,
    S=m[1-2beta(1-theta)/D]=C_s+(m/2)gamma theta.

The second equality uses C_s=m[1-2beta/D]. Since S>0, the negative spherical part vanishes outside the core, and J/(beta L log R) tends to S at every fixed center. Set delta=gamma theta and choose theta small enough that delta<=beta. This produces the positive deviation (m/2)delta for arbitrarily small delta. The degree-one/degree-three controls of Sections5-6 produce the negative deviation

    -m beta(x_1-x_3)delta/(M_3-H),

whose coefficient is strictly negative. Both are globally smooth, solenoidal, decaying controls with the exact energy ratio; both fail the full profile momentum equation through the nonzero core curl for every c and omega. Thus a uniform little-o(delta) error is impossible separately in either side of a two-sided estimate for J around C_s. This statement is about order, not the optimal coefficients of either side. It supplies no Euler counterexample.
