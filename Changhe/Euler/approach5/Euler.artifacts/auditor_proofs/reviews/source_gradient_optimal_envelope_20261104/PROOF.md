# The exact finite-gradient tangential and spherical-source envelope

## 1. Statement and dependencies

Let U be a real C1 divergence-free field on R3, and suppose E(R)=integral_(|y|<R)|U|^2 satisfies E(R)/(LR^beta)->1 with L>0 and0<beta<1. Set t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta. With r=|y| and n=y/r put

    F=integral_(1<r<R)r^(-beta)|U|^2,
    T=integral_(1<r<R)r^(-beta)|U-(U.n)n|^2,
    G=integral_(1<r<R)r^(2-beta)|DU|_F^2,
    q=tr((DU)^2), Q(r)=integral_S2 q(rn)dn,
    J=integral_1^R r^(4-beta)[Q(r)]_+dr,
    I=integral_(1<r<R)r^(2-beta)[q]_+.

Sphere measure is4pi. Suppose limsup G/(beta L log R)<=M<infinity. For ell>=1 let

    lambda_ell=ell(ell+1),
    x_ell=k^2/(lambda_ell+k^2),
    M_ell=t^2+lambda_ell(lambda_ell+t^2-2)/(lambda_ell+k^2).

Then M>=M_1=H=t^2(k^2+4)/(k^2+2). The sequence M_ell strictly increases to infinity. For M_j<=M<=M_(j+1) set

    d(M)=[(M_(j+1)-M)x_j+(M-M_j)x_(j+1)]
                              /(M_(j+1)-M_j).

The values agree at shared endpoints. The claims are

    liminf T/(beta L log R)>=d(M),
    liminf J/log R>=beta m(1-beta)L+m beta^2 L d(M),

and the latter also holds with I in place of J. The T and J bounds are attained at every finite M by a smooth uniformly decaying kinematic field with exact origin energy E(R)=LR^beta for R>=2, all-center error O_a(R^(beta-1)), a smooth Poisson pressure, and nonzero full-momentum curl for every real c,omega. No optimality of I is asserted.

This reconstructs all eight sections of LIT383, source7d79ea70, retained with its70 analytical checks and support note in `verification`. The only prior mathematical inputs are the confirmed logarithmic Hardy lower bound A3125 and the energy theorem A3053 for the conditional profile application. The mode and source identities needed below are restated. Neither LIT381 nor LIT382 is needed for the original proof in Sections2-8.

## 2. All angular modes and the adjacent-degree identity

Write z=log r and U(rn)=r^t v(z,n). Then F=integral|v|^2 dz dn, T=integral|v_T|^2 dz dn and G=integral(|v_z+tv|^2+|grad_S v|^2)dz dn, with Cartesian component differentiation in grad_S. Divergence is (partial_z+k)(v.n)+div_S v_T=0. The radial degree-zero coefficient vanishes, because the flux of the whole-space divergence-free field through every sphere is zero.

For a normalized real harmonic Y of degree ell>=1, write nu=ell(ell+1). A poloidal component is fY n+g grad_S Y, with g=(f'+kf)/nu; a toroidal component is h n cross grad_S Y. Their energies are

    K_pol=f^2+(f'+kf)^2/nu, T_pol=(f'+kf)^2/nu,
    D_pol=(f'+tf)^2+[f''+(k+t)f'+tkf]^2/nu
                         +(nu+2)f^2-4f(f'+kf)+(f'+kf)^2,
    K_tor=T_tor=nu h^2,
    D_tor=nu[(h'+th)^2+nu h^2].

The angular identities follow from differentiating the normal, integral|grad Y|^2=nu and integral|Hess_S Y|^2=nu(nu-1). Orthogonality of distinct harmonics, and integration by parts between gradient and rotated-gradient harmonics, remove all cross terms after sphere integration. These are identities for the full spherical energy, not pointwise identities.

Fix adjacent eigenvalues lambda=j(j+1), mu=(j+1)(j+2). Define

    A=lambda+mu+2t^2-2,
    B=(lambda+k^2)(mu+k^2)/k^2-2beta.

They are positive, and t^2-A+B=lambda mu/k^2. For a smooth compactly supported nonnegative eta, direct expansion and integration of cross derivatives gives

    integral eta(D_pol-A K_pol+B T_pol)
      =integral eta[f''^2/nu+b_nu f'^2+d_nu f^2]
       -(k+t)/nu integral eta'f'^2
       -[2t+((k+t)tk-Ak+Bk)/nu]integral eta'f^2
       +tk/nu integral eta''f^2,
    b_nu=2+(k^2+lambda mu/k^2)/nu>0,
    d_nu=(nu-lambda)(nu-mu)/nu.

For example, before factorization the last coefficient is nu+2t^2-A-2+k^2(t^2-A+B)/nu, which equals nu-lambda-mu+lambda mu/nu. No spherical eigenvalue lies strictly between lambda and mu, so d_nu>=0 for every permitted mode. This is the precise discrete-spectral input.

The toroidal identity is

    integral eta(D_tor-AK_tor+BT_tor)
       =nu integral eta[h'^2+(nu+lambda mu/k^2)h^2]
          -t nu integral eta'h^2.

Its main terms are nonnegative. All cutoff errors have absolute value at most C_(beta,j) integral(|eta'|+|eta''|)K. In particular f'^2/nu<=2nu g^2+2k^2 f^2/nu<=C_beta K, uniformly in nu>=2. No sign is assigned to a cutoff integral.

## 3. C1 passage and finite-radius inequality

For C1 U each coefficient f,g,h is C1 on a compact z interval, and the divergence equation makes f C2. Apply the displayed identities to finite harmonic sums. Their energies converge in the angular H1 and radial-derivative L2 norms by Parseval. The cutoff estimates are uniform in the highest degree. Nonnegative main sums may also pass monotonically. Consequently

    G_eta>=A F_eta-B T_eta
                   -C_(beta,j)integral(|eta'|+|eta''|)|v|^2

for the full C1 field.

Choose eta=eta_R supported in0<z<log R, equal to1 on log2<=z<=log(R/2), and with uniformly bounded first two derivatives. The fixed inner strip has finite energy. The outer strip has velocity energy at most (R/2)^(-beta)E(R)=O(1). Thus F_eta=F+O(1), T_eta<=T and G_eta<=G. As B>0,

    G(R)>=A F(R)-B T(R)-C_(U,beta,j).

The proof uses no boundary value of DU, no derivative of an energy remainder and no derivative decay at infinity. The finite number j is chosen for the bound; it is not a truncation of U.

## 4. The envelope and the positive-source bound

Stieltjes integration by parts gives F(R)=R^(-beta)E(R)-E(1)+beta integral_1^R r^(-beta-1)E(r)dr=beta L log R+o(log R). Divide the preceding inequality by beta L log R and use the gradient limsup to get liminf T/(beta L log R)>=(A-M)/B.

Rewrite M(lambda)=t^2+lambda-2beta lambda/(lambda+k^2). Its derivative is1-2beta k^2/(lambda+k^2)^2>0 for lambda>=2, so the sequence is increasing and unbounded. Direct substitution yields A-Bx_j=M_j and A-Bx_(j+1)=M_(j+1). Hence (A-M)/B=d(M) on the adjacent interval. The Hardy lower bound already gives M>=M_1. Every other adjacent-pair bound holds at both endpoints of this interval, so its affine interpolation cannot improve d(M) there.

To obtain J, use q=partial_i partial_j(U_iU_j) distributionally. Test against a smooth nonnegative radial function equal to r^m on2<r<R, zero on B1 and outside B_(2R), and bounded above by r^m. The uncut Hessian is m r^(-beta)(I-beta n tensor n). It pairs with U tensor U as m r^(-beta)[(1-beta)|U|^2+beta|U_T|^2]. The fixed inner error is bounded; differentiated outer cutoffs cost at most C R^(-beta)E(2R)=O(1). The uncut Hessian is positive, although the compact test is not convex. Radiality bounds the pairing above by J(2R) plus a fixed error. Replace R by R/2 and use the O(1) strip bound for F,T. This proves

    J(R)>=m[(1-beta)F(R)+beta T(R)]-C.

The stated J bound and the I bound follow, since J<=I. Ball inclusions give the energy ratio with the same L at every fixed center; the proof there uses that center's own assumed gradient bound. No translation invariance of the profile equation is invoked.

## 5. Smooth fields attaining every adjacent interpolation

Let theta=(M_(j+1)-M)/(M_(j+1)-M_j). Choose normalized zonal harmonics Y_j,Y_(j+1), and define K_ell=1+k^2/lambda_ell,

    b_j^2=beta L theta/K_j,
    b_(j+1)^2=beta L(1-theta)/K_(j+1).

For each of these two degrees put

    V_ell=f_ell(r)Y_ell n
                   +(r f_ell'(r)+2f_ell(r))grad_S Y_ell/lambda_ell.

This is divergence-free for every smooth f_ell. Take f_ell=b_ell r^t for r>=2. Inside2-epsilon use b_ell 2^(t-ell+1)r^(ell-1), and join smoothly on the shrinking annulus. The interior vector is b_ell 2^(t-ell+1)/ell times grad(r^ell Y_ell), hence smooth at0. The two scalar formulas agree at2. Their difference is O(epsilon) on the annulus, which compensates the cutoff derivative O(1/epsilon); f_ell and f_ell' remain bounded for fixed j. The transition energy therefore tends to zero with epsilon.

Spherical orthogonality persists for arbitrary radial coefficients. The interior limiting energy is

    2^beta[b_j^2/j+b_(j+1)^2/(j+1)].

Indeed the ell summand integrates b_ell^2 2^(2t-2ell+2)r^(2ell-2)(1+lambda_ell/ell^2)r^2dr from0 to2, giving b_ell^2 2^beta/ell. Since beta<ell K_ell, this is strictly less than L2^beta after summing. Choose a small positive epsilon leaving deficit D0>0.

Let eta0 be radial smooth, equal to1 near0 and supported in r<1/2. Define J(y1,y2,y3)=(-y2,y1,0), W=eta0(r)Jy, I0=integral|W|^2>0, a0=sqrt(D0/I0). W is divergence-free and pointwise orthogonal to each zonal poloidal field. Then U=V_j+V_(j+1)+a0W is smooth, solenoidal, and has E(2)=L2^beta. Its exterior sphere energy is beta L r^(beta-3), yielding E(R)=LR^beta for every R>=2. Its homogeneous tail decays uniformly and |D^hU|<=C_h r^(t-h) for every h. The same construction works at theta=0 or1, with one inactive component.

## 6. Exact coefficients and translations

The exterior mode orthogonality gives T=beta L[theta x_j+(1-theta)x_(j+1)]log R+O(1) and G=beta L[theta M_j+(1-theta)M_(j+1)]log R+O(1). These are beta L d(M) and beta L M.

For any homogeneous solenoidal field of degree t, let K0,T0 be its spherical velocity and tangential energies. Against a radial test psi supported away from0, the divergence identity gives

    integral r^2Q(r)psi(r)dr
        =integral[(K0-T0)r^(beta-1)psi''
                               +T0 r^(beta-2)psi']dr.

Two integrations by parts in the first term and one in the second give Q(r)=m[(1-beta)K0+beta T0]r^(beta-5). For the mixed tail K0=beta L, T0=beta Ld(M), so its coefficient is strictly positive. This proves equality for J. No pointwise sign for q and no equality for I has been used.

At a fixed center a, ball inclusions give E_a(R)=LR^beta+O_a(R^(beta-1)), without needing parity of the mixed tail. Translation changes the velocity by O_a(r^(t-1)) and its derivative by O_a(r^(t-2)). The resulting tangential squared-density difference is O_a(r^(2t-1)); gradient-square and q differences are O_a(r^(2t-3)). After the critical weight and radial Jacobian, all are O_a(r^-2). The positive-part map is1-Lipschitz, also after sphere integration. Thus T,G,J have O_a(1) differences at any fixed center and the same leading coefficients. These examples attain the infima both when the gradient limit equals M and when only its limsup is bounded by M.

## 7. Poisson pressure and failure of Euler momentum

Let N(y)=1/(4pi|y|), so -Delta N=delta0. Define P0 as the distributional convolution sum_ij(partial_i partial_jN)*(U_iU_j), with its local delta term and principal value. Smooth subtraction handles the local singularity. A distant dyadic shell contributes at most C R^-3 E_a(2R)=O(R^(beta-3)); these terms are summable. On bounded observation sets derivatives may fall on the separated distant kernel. The compact smooth part is handled locally. This constructs smooth P0 with -Delta P0=q.

Consider the full profile residual without pressure,

    R=(1-c)U+[((cI-omega J)y+U).grad]U+omega JU.

For j=1, the field near0 is U=d e3+(S+a0J)y, where e3=(0,0,1) and S=diag(s,s,-2s). Choose the degree-two harmonic sign so s>=0; s=0 if absent. The Jacobian of R is M0+M0^2+omega(JM0-M0J), M0=S+a0J. S commutes with J, so the last term vanishes. The constant axial term has no effect on this Jacobian. Its antisymmetric part is a0(1+2s)J, and curl R=2a0(1+2s)e3!=0.

For j=2, U(0)=0 and DU(0)=S+a0J, with the same s>=0 choice. The quadratic contribution from degree three has its second derivative multiplied by U(0) when the transport is differentiated, so the same curl holds at0. For j>=3, U(0)=0 and DU(0)=a0J, and curl R(0)=2a0e3. All cases remain valid at endpoint mixtures. A C1 pressure gradient has zero distributional curl. Thus no pressure can solve the full equation for any real c or omega, even though the Poisson equation is solved.

## 8. Continuous comparison and Euler scope

The continuous curve h(x)=k^2/x+2beta x+2-4beta is strictly convex and strictly decreasing for0<x<=x_1. It has h(x_ell)=M_ell. Its inverse is

    d_cont(M)=2k^2/[M+4beta-2
                         +sqrt((M+4beta-2)^2-8beta k^2)].

At an interior convex combination of two distinct x values, strict convexity gives h(d(M))<M. Since h is decreasing, d(M)>d_cont(M) between consecutive M_ell, with equality at the discrete endpoints. This verifies the improvement over the continuous-degree root directly from the displayed scalar function.

For a bounded C1 velocity and C1 pressure solving the full rotating profile PDE, with U(R.)->0 distributionally on compact sets and2/5<c<1/2, A3053 gives beta=5-2/c and the required energy ratio with L>0 unless U=0. A finite gradient coefficient remains an additional premise. The result applies without imposing velocity symmetry and for every finite omega. An exterior bound |DU|_F<=D r^(-1/c) supplies M=4piD^2/(beta L). Neither that bound nor finite M follows here from uniform decay alone. The controls are axisymmetric fields in the larger kinematic class, not actual Euler examples. The finite-M pointwise-source optimum, actual-profile optimum and main conjecture remain open.

All source sections and70 obligations were read, and the displayed identities reconstructed analytically. The complete existing C comparison is checked below. Configured model collaboration is through files; actual provider execution is independently unattested. No mathematical computation, build or fresh external retrieval was used.


## 9. A second proof from nonnegative mode weights

The complete nine-item C comparison of09:53:56Z is retained in the team records. Its items1-5 agree with Sections2-8. Its alternative proof can be made precise as follows, using the sphere identity reconstructed in A3146. For each degree ell and eigenvalue lambda, sum over its real harmonics and put

    a_ell=integral eta sum f_ell,m^2,
    p_ell=integral eta sum f_ell,m'^2/lambda>=0,
    tau_ell=integral eta sum lambda h_ell,m^2>=0,
    delta_ell=p_ell-(k/lambda)integral eta' sum f_ell,m^2.

Then the integrated tangential poloidal energy is k^2 a_ell/lambda+delta_ell. With Z_w=integral eta|partial_z v_T|^2>=0, the sphere identity gives exactly

    G_eta=sum_ell[(lambda+t^2-2)a_ell+2lambda delta_ell+lambda tau_ell]
                +t^2 F_eta+Z_w
                +(k+2)integral eta' f^2-t integral eta'|v|^2,

where f=v.n. Indeed the radial derivative term in that identity is twice integral eta|partial_z f|^2. Replacing it by 2lambda delta_ell adds 2k integral eta'f^2; combined with the original -t integral eta'f^2 this is (k+2)integral eta'f^2.

The numbers delta_ell themselves need not be nonnegative. Replace them by p_ell and keep their boundary terms as errors. All such errors are bounded by C_beta integral|eta'| |v|^2: even the factor2lambda in G cancels the denominator lambda. Up to these errors, F and T are sums of nonnegative weights with the following pairs (tangential fraction, derivative cost):

    weight K_ell a_ell: (x_ell,M_ell),
    weight p_ell:       (1,t^2+2lambda),
    weight tau_ell:     (1,t^2+lambda),
    K_ell=1+k^2/lambda.

The additional Z_w is nonnegative derivative cost with no velocity weight. The polygon joining the points (x_ell,M_ell), in increasing x order, and then (1,t^2+2), is convex. The left edges are chords of the strictly convex h from Section8. Their slopes are negative, whereas the last edge has slope2beta>0. Every displayed atom lies on or above this polygon. Each supporting affine inequality may therefore be summed over countably many modes. The local H1 convergence and the uniform error bound justify the sum for C1 fields. This gives the same lower affine inequalities as Section2, with only eta' errors. Equivalently one may apply countable Jensen to the finite total nonnegative velocity weight; no sign is assigned to delta_ell.

## 10. The matching upper tangential bound

The last edge of this polygon also gives a useful additional inequality. Algebraically the exact identity from Section9 is

    G_eta=(t^2+2)F_eta-2beta R_eta
       +sum_ell[(lambda-2)K_ell a_ell+2(lambda-1)delta_ell
                                      +(lambda-2)tau_ell]
       +Z_w+(k+2)integral eta'f^2-t integral eta'|v|^2,
    R_eta=F_eta-T_eta.

For the a coefficient the identity is M_ell-(t^2+2)+2beta(1-x_ell)=lambda-2. Replace delta_ell by p_ell; the resulting error is uniformly bounded by the velocity strip norm because (lambda-1)/lambda<=1. All remaining sums are nonnegative. Choosing the same cutoff as Section3 gives

    G(R)>=(t^2+2-2beta)F(R)+2beta T(R)-C.

Thus the hypotheses of Section1 imply

    limsup T/(beta L log R)
       <=min(1,1+(M-t^2-2)/(2beta))
        =min(1,x_1+(M-H)/(2beta)).

Together with Section4 this supplies sharp lower and upper limits for the possible normalized tangential energy. At M=H both bounds equal x_1, recovering the tangential conclusion of A3149. The upper bound is attained for H<=M<=t^2+2 by mixing the normalized degree-one poloidal field with the normalized degree-one toroidal field r^(t-1)Jy. Their velocity and derivative cross terms integrate to zero, so the energy-weighted costs are H and t^2+2, and their fractions are x_1 and1. Choose the poloidal fraction rho=(t^2+2-M)/(t^2+2-H). The resulting fraction is rho x_1+(1-rho).

Here is a smooth completion, to keep this attainment statement in the whole-space class. Interpolate the poloidal radial coefficient to a constant inside radius2 as in Section5, and interpolate the coefficient of Jy to its value at2, giving a linear toroidal core. The limits of the interior energies per unit tail spherical energy are respectively 2^beta/(1+k^2/2) and2^beta/5. Both are strictly less than2^beta/beta. The shrinking transition annuli have vanishing energy, so their mixture has a positive deficit at radius2. A nonnegative compact radial swirl a eta0 Jy fills it: the energy increment is a^2 I0+2a B0 with I0>0 and B0>=0, hence there is one positive solution for the required deficit. The poloidal cross term is zero, while the existing toroidal cross term is precisely B0 and must be retained. The resulting field has exact E(R)=L R^beta outside2, all derivative decay and the usual all-center O(R^(beta-1)) remainder. Weighted T and G change by O(1) under a fixed translation. Its Poisson pressure is smooth by Section7. Its core is d e3+a_total Jy with a_total>0, so curl of the full momentum residual is2a_total e3 for every c,omega.

For M>=t^2+2 the pure degree-one toroidal construction has fraction1 and gradient cost t^2+2<=M, and therefore attains the upper bound for the stated limsup constraint. This does not assert an exact gradient cost M in that range.

## 11. Nonzonal and translation refinements; limits of certification

C's nonzonal refinement is also valid. Any real normalized harmonic in either degree has the same integrated norm identities. For nonzonal modes the compact swirl cross term is not necessarily pointwise zero, but its sphere integral vanishes, since it is a constant multiple of the integral of the angular derivative of a smooth spherical harmonic. Thus the energy completion still works. At degree two let the symmetric trace-free core matrix be S. For M0=S+a0J, the skew part of M0+M0^2+omega[J,M0] has curl vector2a0(e3-S e3): the commutator [J,S] is symmetric, and SJ+JS has axial vector -S e3 when tr S=0. Choosing the harmonic sign ensures S e3!=e3. At j=1 a possibly nonaxial constant velocity changes only the constant residual because the core is affine. At j=2 the quadratic term is still multiplied by U(0)=0 in the differentiated transport. Hence the nonzonal controls also fail full momentum for every c,omega.

The weaker centered energy error in mixed consecutive degrees can be necessary. For the normalized harmonics Y1=sqrt(3/(4pi))mu and Y2=sqrt(5/(16pi))(3mu^2-1), let v1=Y1 n+(k/2)grad_S Y1 and v2=Y2 n+(k/6)grad_S Y2. Direct polynomial integration gives

    integral_S2 (v1.v2)n3 = sqrt(15)(4+k^2)/30 != 0.

Indeed v1.v2 is the product of the two normalization constants times mu[(3-k^2/2)mu^2+k^2/2-1], and integrating mu^2 and mu^4 gives the displayed value. For two nonzero amplitudes the first center derivative of the energy has a nonzero multiple of R^(beta-1). Flipping Y2 to choose the core sign changes only this coefficient's sign. A fixed nonzero axial shift therefore has an R^(beta-1) leading error, with O(R^(beta-2)) Taylor remainder. No unjustified parity improvement is available for this family.

The symbolic scripts, sampled grids, quadrature decimals and earlier failed diagnostic run in C's note are not certified here. Only the analytical arguments and explicit formulas reconstructed above are confirmed. The finite-M pointwise positive-source optimum, actual-Euler optima and automatic finite gradient control remain open. None of the kinematic equality fields is a counterexample to the original conjecture.
