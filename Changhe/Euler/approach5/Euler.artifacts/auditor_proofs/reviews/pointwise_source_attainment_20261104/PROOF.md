# A single field attaining the critical source coefficient

## 1. Statement and audit scope

Fix 0<beta<1 and L>0. Let J(y1,y2,y3)=(-y2,y1,0) and e3=(0,0,1). Set t=(beta-3)/2, k=(beta+1)/2, m=2-beta and K=beta m(1-beta). There is a smooth, odd, divergence-free U:R3->R3 with the following properties. For each fixed center a, define

    E_a(R)=integral_(|y-a|<R) |U|^2,
    I_a(R)=integral_(1<|y-a|<R) |y-a|^m [tr((DU)^2)]_+,
    G_a(R)=integral_(1<|y-a|<R) |y-a|^m |DU|_F^2.

Then E_0(R)=LR^beta for R>=2, and for every epsilon>0,

    E_a(R)=LR^beta+O_(a,epsilon)(R^(beta-2+epsilon)).

For each integer h>=0 and epsilon>0, |D^hU(y)|<=C_(h,epsilon)|y|^(t-h+epsilon) outside a fixed ball. Thus every unscaled derivative tends uniformly to zero. At every fixed center,

    I_a(R)/log R -> KL,
    G_a(R)/log R -> +infinity.

A smooth Poisson pressure exists, but no C1 pressure makes U a full rotating Euler profile for any real c,omega. This is a kinematic attainment theorem. It concerns a logarithmic coefficient, not equality at every radius or a finite-norm Hardy quotient. The input is LIT380, SHA256 2056b6a97616115b809a5aee57975278ac78178ac41fc453a849a0b646e714ef, including all nine sections,54 analytical checks and its source note. Comparison and final verdict are recorded separately.

## 2. Angular fields with arbitrarily small excess

We reconstruct the ingredient rather than assuming that a varying family can be glued without cost. Put A=2(t^2+t+1), D=-2tk. Here D>0 and A-D=m(1-beta)>0. Choose 1<p<min(3,A/D). For delta>0 let z solve

    z''=V_delta'(z)/2, V_delta(z)=(delta^2+z^2)^(-p)(1-z^2),
    z(0)=0, z'(0)=delta^(-p).

Conservation gives z'^2=V_delta(z). Its quarter-period is the integral from0 to1 of (delta^2+s^2)^(p/2)/sqrt(1-s^2). This is uniformly bounded above and below as delta->0. The second-order smooth ODE continues across the two turning points and gives a smooth odd periodic solution. Its derivative energy is four times the integral of (delta^2+s^2)^(-p/2)sqrt(1-s^2). Restriction to 0<s<delta proves divergence at least of order delta^(1-p).

Direct differentiation gives

    A z'^2+D z z''
      =[A-Dp z^2/(delta^2+z^2)]z'^2-D z^2(delta^2+z^2)^(-p).

The bracket is positive. The integral of its negative part is at most a fixed multiple of integral_0^1 s^(2-p)/sqrt(1-s^2), hence uniformly bounded. Rescaling the period to2pi preserves both this bound and divergence of the derivative energy M_delta. Periodic integration by parts gives integral ZZ''=-M_delta. Therefore

    integral [A Z'^2+D ZZ'']_+/M_delta -> A-D=m(1-beta).

Choose a smooth even belt cutoff chi supported in pi/4<theta<3pi/4. For fixed delta and integer n tending to infinity put

    g=-(k/n)chi(theta)Z(n(theta-pi/2)),
    h=-(g'+cot(theta)g)/k.

Then kh+g'+cot(theta)g=0, h is even and g odd under theta->pi-theta. The spherical derivative matrix of r^t(h e_r+g e_theta), divided by r^(t-1), is

    [t h, h'-g, 0; t g, h+g', 0; 0,0,h+cot(theta)g].

Its trace-square is chi^2[A Z'^2+D ZZ'']+O_delta(1/n), uniformly on the sphere. Indeed h=chi Z'+O_delta(1/n), h'=n chi Z''+O_delta(1), and g=O_delta(1/n); the term2tgh' has leading coefficient -2tk=D. The diagonal leading coefficient is t^2+(1-k)^2+1=A.

Periodic averaging follows by integration of a bounded primitive of each mean-zero periodic integrand against the derivative of the fixed smooth belt weight. The map x->[x]_+ is1-Lipschitz, so the error remains negligible after taking positive parts. Normalize by the positive square root of integral(h^2+g^2). First choosing delta, then n, produces blocks (h_j,g_j) with

    integral(h_j^2+g_j^2)=1, T_j=integral g_j^2->0,
    integral[q_j]_+<=m(1-beta)+delta_j, delta_j->0.

The first T_j, and any later T_j, can be made as small as desired. There is no uniform angular derivative claim. Smooth extension across the poles holds because the blocks vanish near them. Their vector fields are odd under inversion. The smooth toroidal unit field

    T=sqrt(3/(8pi))sin(theta)e_phi

is also odd, has squared sphere norm1 and is pointwise perpendicular to every meridional block.

## 3. Exact sphere energy during transitions

Write s=log r and U=r^t v. A varying meridional field

    v_P=a(s)h_j e_r+(a(s)+a'(s)/k)g_j e_theta

is divergence-free because f_s+kf+div_S w=0. A toroidal field b(s)T is divergence-free for arbitrary b. Fix epsilon_j in(0,1/2] tending to0. A constant interval of type j has a=sqrt(beta L(1-epsilon_j)) and b=sqrt(beta L epsilon_j).

Join consecutive types by reducing the old amplitude to0 and then increasing the new amplitude. Use fixed smooth scalar paths, flat at their endpoints, stretched until |a'|<=k epsilon_j sqrt(beta L)/8 on the half using block j. The two blocks are never simultaneously active. With H_j=1-T_j, the meridional squared norm is

    N_P=H_j a^2+T_j(a+a'/k)^2
       <=beta L[1-epsilon_j+epsilon_j/4+epsilon_j^2/64]
       <=beta L(1-epsilon_j/2).

Define b=sqrt(beta L-N_P). Its argument stays strictly positive. This makes b smooth with the required flat jets at every endpoint. At the middle a=0 and b=sqrt(beta L), independently of the block. The two halves therefore join smoothly. Perpendicularity gives integral|v|^2=beta L at every s.

Fix all these transition paths before placing them. Let W_j be their finite lengths. All their derivative constants are finite, including the a'' contribution to DU and higher derivatives of the square root.

## 4. Source cost and one simultaneous placement

In the orthonormal cylindrical frame an axisymmetric field has derivative matrix

    [u_rho,rho, -u_phi/rho, u_rho,z;
     u_phi,rho, u_rho/rho, u_phi,z;
     u_z,rho, 0, u_z,z].

Its trace-square has toroidal part -2(u_phi/rho)u_phi,rho and no meridional-toroidal cross term, also when the toroidal amplitude varies. The identity extends across the axis by smoothness. On a constant type-j interval, subadditivity of positive parts bounds the sphere source density by

    d_j<=beta L[(1-epsilon_j)(m(1-beta)+delta_j)+epsilon_j C_T],

where C_T is the finite positive-source integral of the homogeneous unit toroidal field. Thus limsup d_j<=KL.

The source scales as r^(beta-5) times a smooth expression in v and its first s and angular derivatives. Its weighted radial measure is exactly ds. Let D_j be the finite nonnegative integral source cost of transition j; it is independent of its location. For each j,h, let C_(j,h)>=1 bound the coefficient of r^(t-h) in |D^h U| both on transition j and on the constant interval of type j+1. Fix these constants before selecting locations.

Choose transition start points S_j recursively so that

    S_1>log2+1, S_(j+1)>S_j+W_j+1,
    sum_(i<=j)(D_i+W_i)<=S_j/j,
    log(max_(0<=h<=j+3) C_(j,h))<=S_j/j.

Every requirement is a lower bound on the next S_j and involves already fixed quantities. There is no circular dependence and no finite accumulation of transitions. For S_j<=S<S_(j+1), all transition cost incurred by S is at most sum_(i<=j)D_i<=S/j, even if S lies inside transition j. This is o(S). All sufficiently late constant intervals have source density at most KL+eta for any fixed eta>0; earlier intervals have finite total cost. Consequently limsup I_0(R)/log R<=KL at every radius.

For fixed h,epsilon and sufficiently large j, C_(j,h)<=exp(S_j/j)<=r^epsilon on transition j and its following interval. The preceding constant interval uses the previous index. The finitely many early intervals only alter a finite constant. Thus the same single placement gives all the derivative bounds of Section1, for all h and epsilon. Since t-h<0, those bounds imply uniform decay of each derivative.

## 5. Core completion and exact energy

Choose a smooth radial chi0, zero for r<=1 and one for r>=2, with 0<=chi0<=1. On1<r<2 extend the first block by

    A_1 r^t[chi0 h_1 e_r+(chi0+r chi0'/k)g_1 e_theta]
       +B_1 chi0 r^t T.

This is smooth, odd and divergence-free, zero in B1 and equal with all derivatives to the first constant interval at r=2. Define C0=integral_1^2 r^(beta-1)(chi0+r chi0'/k)^2. Direct orthogonality gives

    E_base(2)<=L(2^beta-1)
      +L(1-epsilon_1)T_1[beta C0-(2^beta-1)].

C0 is independent of the angular block. Choose its first tangential norm small enough that the absolute last term is less than L/2. The deficit D0=L2^beta-E_base(2) then exceeds L/2. Add a0 eta(r)Jy, where eta is smooth, equals1 near0 and vanishes for r>=1/2, and a0>0 normalizes its squared norm to D0. This support is disjoint from the base. Its divergence is0 because grad eta is radial and y.Jy=0. Its energy adds exactly. Therefore E_0(2)=L2^beta. The sphere energy outside2 is beta L r^(beta-1), so E_0(R)=LR^beta for all R>=2. In particular the total energy is infinite.

## 6. Lower coefficient and fixed centers

For a C1 solenoidal field q=tr((DU)^2)=partial_i partial_j(U_iU_j) in distributions. Let f be a smooth nonnegative radial function, zero in B1, equal to r^m outside B2, bounded above by r^m. Test against f times a radial cutoff chi(y/R), equal to1 on B_R and zero off B_(2R). Outside B2,

    D^2 f=m r^(-beta)(I-beta e_r tensor e_r).

The inner term is bounded. Terms differentiating the outer cutoff are bounded by C R^(-beta)E_0(2R)=O(1). The remaining Hessian is nonnegative. The test itself is not claimed convex. Define F=integral_(1<r<R)r^(-beta)|U|^2 and T_R=integral_(1<r<R)r^(-beta)|U_tan|^2. The positive source bounds the tested source, giving first an I_0(2R) bound and then

    I_0(R)>=m[(1-beta)F(R)+beta T_R]-C.

Replacing2R by R loses only a bounded annular weighted energy. Exact E_0 gives F=beta L log R+O(1). Together with the upper bound this proves I_0/log R->KL and T_R=o(log R).

The energy density e=|U|^2 is even. For fixed R, its integral over B_R(a) has first center derivative0 at a=0. Its second center derivative is a boundary integral of grad e. The derivative estimates give |grad e|<=C_epsilon r^(beta-4+epsilon), so this integral is O(R^(beta-2+epsilon)), uniformly for centers in a fixed bounded set. Taylor's formula proves the stated all-center remainder.

Similarly |grad q|<=C_epsilon r^(beta-6+epsilon). After translating by fixed a, the difference of the positive sources is bounded by this derivative times |a|. Multiplication by the weight and sphere Jacobian leaves O(r^(-2+epsilon)), integrable at infinity when epsilon<1. Bounded regions contribute finite constants. Hence I_a(R)-I_0(R)=O_a(1). The lower-bound argument at each center, now with its energy remainder, gives T_a(R)=o(log R).

## 7. Divergence of the weighted gradient coefficient

At any fixed center write U(a+r n)=r^t v(s,n)=r^t(f n+w). Solenoidality gives f_s+kf+div_S w=0. Choose0<=eta_S<=1 on the logarithmic interval, equal to1 except in two fixed-width endpoint strips and with uniformly bounded derivative. Their weighted velocity energies are O(1), by the energy ratio. Multiplication by eta_S f and integration by parts yields

    k integral eta_S f^2
      =integral eta_S grad_S f.w+(1/2)integral eta_S' f^2.

The coefficient +1/2 is positive; the last integral has no fixed sign and is bounded in absolute value. Cartesian spherical differentiation gives grad_S f=(grad_S v)^T n+w. Also

    G_a(R)=integral [|v_s+t v|^2+|grad_S v|^2] ds dS.

Cauchy-Schwarz and the strip bounds therefore give

    k F_a(R)<=sqrt(G_a(R) T_a(R))+(k+1)T_a(R)+C_a.

Since F_a/log R->beta L and T_a/log R->0, the square root exceeds (k beta L/2)log R eventually. In particular T_a>0 then. Squaring and dividing proves G_a/log R->infinity. This is an all-radius conclusion because source attainment was proved at every radius; no subsequence inference is being strengthened silently.

## 8. Pressure, full momentum and precise consequences

Let N(y)=1/(4pi|y|). The distributional Hessian convolution sum_(i,j) partial_i partial_j N*(U_iU_j), including its local distributional term, defines P0. Local subtraction of the smooth density handles the principal value. On distant annuli the absolute kernel integral is at most C R^-3 E_y(2R)=O(R^(beta-3)), summable. For derivatives on compact observation sets, split off a compactly supported density and differentiate only the distant kernel. This proves smoothness. Distributional differentiation, justified by these tail bounds, gives -Delta P0=q.

The full profile equation is (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0. Near0, U=My with M=a0J. The nongradient profile expression is

    (1-c)My+M(cI-omega J)y+M^2y+omega JMy=(M+M^2)y.

M commutes with J and M^2 is symmetric. Its curl is2a0 e3, nonzero. A C1 pressure gradient has distributional curl0, so no pressure or harmonic addition can solve the full equation for any c,omega.

The radial positive spherical-source moment lies between the same lower bound of Section6 and I_a, because [integral_S q]_+<=integral_S[q]_+. Its logarithmic coefficient is therefore also KL at every fixed center. The weighted tangential fraction tends to0. These statements settle single-field and zero-fraction attainment in this smooth kinematic class. They do not establish full-Euler optimality, a uniform weighted derivative bound, a counterexample to nonexistence, or any automatic source integrability. In fact G_a/log R diverges although every unscaled derivative decays.

## 9. Independent comparison and additional bounds

The existing Theory Agent A comparison, retained as in the team records, SHA256 a9b67436a89ccace43dc426ee60989f73395f78b0a7dc35c82e5adccace20ad7, has been read in full. Its ten checks and seven remarks agree with the reconstruction above. It is from the configured model agent; actual provider execution is independently unattested. Its diagnostic script, numerical samples and execution log are not certified by this audit. The proof uses the analytical identities instead.

On each half-transition, the derivative bound uses the epsilon and angular block of that half. Equivalently both halves may use the minimum of their two epsilons. This is the precise reading required for the source's indices and is already the choice in Section3. The paths and all of their derivative constants are fixed before their locations. Adding path lengths to the lower bounds on those locations cannot create a circular dependence.

The unit-energy toroidal field T=sqrt(3/(8pi)) sin(theta)e_phi has scaled source

    q_T=-2c_T^2[1+(t-1)sin(theta)^2], c_T^2=3/(8pi).

Writing mu=cos(theta), positivity holds for mu^2<-t/(1-t)=(3-beta)/(5-beta). Direct integration of this quadratic on that interval gives

    integral_S2[q_T]_+=(3-beta)^(3/2)/sqrt(5-beta),
    integral_S2 q_T=2-beta.

These are the pointwise positive and signed coefficients, respectively; they cannot be interchanged. The upper bound for a good block is consequently beta L[(1-epsilon_j)(C+delta_j)+epsilon_j h_beta]. Its toroidal proportion tends to zero as chosen. Independently, the necessary tangential-fraction conclusion shows that a fixed positive toroidal fraction would prevent minimum source attainment.

For every epsilon>0 the derivative estimate of Section4 gives G_a(R)<=C_(a,epsilon)R^(2epsilon). Choosing a smaller epsilon shows G_a(R)=o(R^p) for every fixed p>0, while Section7 gives G_a(R)/log R->infinity. If r^(1-t)|DU|_F were bounded at infinity, integration would instead give G_0(R)=O(log R), a contradiction. Thus that rescaled gradient is unbounded, despite its bound O(r^epsilon) for every epsilon>0 and the decay of every unscaled derivative.

Section7 is a general consequence of the source lower bound and solenoidality: any C1 divergence-free field with the energy law and I_a(R)/log R->K_beta L has T_a(R)=o(log R) and G_a(R)/log R->infinity at that same center. The construction proves the source limit at all fixed centers, hence the conclusion holds at all of them. Neither a source liminf alone nor an unquantified sequence of near-minimal values permits strengthening this to an all-radius statement.
