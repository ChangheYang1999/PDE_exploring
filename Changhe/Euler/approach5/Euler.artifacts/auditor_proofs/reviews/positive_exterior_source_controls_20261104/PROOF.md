# Positive exterior source and constant-gradient controls

## 1. Statement and notation

Fix 0<beta<1 and L>0. Put t=(beta-3)/2, k=t+2=(beta+1)/2, D=k^2+2, m=2-beta and H=t^2(k^2+4)/D. Let e=(0,0,1), Jy=(-y2,y1,0), n=y/|y| and mu=n.e. Define normalized sphere fields

    P(n)=sqrt(3/(8pi D))[k e-t mu n],
    T(n)=sqrt(3/(8pi))Jn.

For each rho in[0,1], there exists a smooth divergence-free U equal on r=|y|>=2 to

    sqrt(beta L) r^t[sqrt(rho)P(n)+sqrt(1-rho)T(n)].       (1)

It has E_0(R)=integral_(|y|<R)|U|^2=LR^beta for R>=2 and E_a(R)=LR^beta+O_a(R^(beta-2)) for every fixed center a. Every derivative of order h is O(r^(t-h)), so U and all its derivatives decay. It has a smooth Poisson pressure, but no C1 pressure makes it a full rotating Euler profile, for any real c,omega.

Let q=tr((DU)^2), where |DU|_F denotes the Frobenius norm. About each center a, F_a,T_a,G_a,I_a integrate respectively r_a^(-beta)|U|^2, r_a^(-beta)|U_tan,a|^2, r_a^m|DU|_F^2 and r_a^m[q]_+ on1<r_a=|y-a|<R. Put Q_a(r)=integral_S2 q(a+r n) and J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr. Then their logarithmic coefficients are

    F_a/(beta L log R)->1,
    T_a/(beta L log R)->tau=1-2rho/D,
    G_a/(beta L log R)->M=rho H+(1-rho)(t^2+2),
    J_a/(beta L log R)->S=m(1-2beta rho/D).              (2)

Each limit has an O_a(1) additive remainder before division. If rho lies between D/(D+3t^2) and D/[2(k+1)], q>=0 outside B2 and I_a has the same coefficient as J_a. Interior rho gives strict exterior positivity. One parameter gives exactly radial positive exterior q; a different parameter makes the exterior gradient norm independent of direction. These are kinematic statements, not Euler solutions. The submitted source is LIT384, SHA256 2a4a7fb8b1a94a1a5cc800d16455de78ecbac5486780433c3a4ebfcc09928597.

## 2. Sphere normalization and both mixed derivative terms

Take Y=sqrt(3/(4pi))mu. Its squared sphere norm is1, its Laplacian is -2Y, and integral|grad_S Y|^2=2. Since

    P=sqrt(2/D)[Y n+(k/2)grad_S Y],

both P and T have norm1, their pointwise inner product is0, and their tangential squared norms integrate to k^2/D and1. The divergence of r^t(f n+w), w tangent, is r^(t-1)[kf+div_S w]. Thus both homogeneous fields in(1) are divergence-free.

In the orthonormal frame(n,p,q), choose p=(e-mu n)/sqrt(1-mu^2) and q perpendicular to the meridional plane. At r=1 the poloidal derivative is

    sqrt(3/(8pi D)) t
      [[2mu,-sigma,0],[k sigma,-mu,0],[0,0,-mu]],
    sigma=sqrt(1-mu^2).                                (3)

This follows by differentiating P in the radial direction and in the two tangent directions: d_n contributes tP, while d_p mu=sigma and d_p n=p. The toroidal derivative has entries only at(1,3),(2,3),(3,1),(3,2). Thus its Frobenius pairing with(3) is0, and the trace pairing is also0 because the transposed positions do not meet the poloidal block. Continuity extends both statements to the poles.

For the unnormalized toroidal field r^(t-1)Jy, the derivative at r=1 is J+(t-1)(Jn) tensor n. Here n.Jn=0, J:(Jn tensor n)=1-mu^2, |J|_F^2=2 and tr(J^2)=-2. Therefore

    |D(r^t T)|_F^2=3/(8pi)[1+t^2+(1-t^2)mu^2],
    tr(D(r^t T)^2)=3/(4pi)[-t+(t-1)mu^2].             (4)

Squaring(3) gives

    |D(r^t P)|_F^2=3t^2/(8pi D)[1+k^2+(5-k^2)mu^2],
    tr(D(r^t P)^2)=3t^2/(4pi D)[(k+3)mu^2-k].        (5)

The off-diagonal product in the trace is negative; replacing trace-square with the Frobenius norm would lose this sign. Integrating mu^2 gives4pi/3, so the gradient integrals are t^2+2 and H. The vanishing mixed terms proves the formula for M in(2).

## 3. Exact exterior source sign and radial choice

Equations(4)-(5) yield

    q(rn)=3beta L r^(beta-5)/(4pi)[a+b mu^2],
    a=-rho k t^2/D-(1-rho)t,
    b=rho t^2(k+3)/D+(1-rho)(t-1).                    (6)

The affine expression in mu^2 is nonnegative on[0,1] exactly when a>=0 and a+b>=0. Since -t>0, these give respectively

    rho<=D/(D-kt)=D/[2(k+1)],
    rho>=D/(D+3t^2).

Both endpoints lie strictly in(0,1), and the lower one is smaller because 3t^2+kt=t(4k-6)>0. Strict inequalities give strict positivity in all directions. The coefficient b is strictly increasing and vanishes at

    rho_s=(1-t)D/[(1-t)D+t^2(k+3)].                    (7)

At the lower endpoint, a>0 and a+b=0, so b<0. At the upper endpoint, a=0 and a+b>0, so b>0. Hence rho_s lies strictly inside the interval.

The pure toroidal signed sphere integral is m; the pure poloidal integral is m t^2/D. Since t^2=D-2beta, their mixture is S=m(1-2beta rho/D)>0 for every rho. At rho_s, (6) is independent of mu and thus

    q(y)=beta L S(rho_s) r^(beta-5)/(4pi)>0.           (8)

The4pi factor is the full sphere area. This proves the J coefficient for all rho and the I coefficient in the nonnegative interval.

## 4. Constant gradient norm and amplitude comparison

The squared gradient in(1) is3beta L r^(beta-5)/(8pi) times A+B mu^2, with

    A=rho t^2(1+k^2)/D+(1-rho)(1+t^2),
    B=rho t^2(5-k^2)/D+(1-rho)(1-t^2).

Here t^2>1 and5-k^2>0. Thus B increases from a negative value to a positive one and vanishes uniquely at

    rho_d=(t^2-1)D/(7t^2-D),                           (9)

because7t^2-D=(t^2-1)D+t^2(5-k^2). It follows that0<rho_d<1. At this value the sphere integral beta L M_d forces

    |DU|_F^2=beta L M_d r^(beta-5)/(4pi).

The limit superior of r^((5-beta)/2)|DU|_F therefore has square beta L M_d/(4pi). Since (t^2+2)-H=4beta/D>0 and rho_d<1, M_d>H.

The poloidal maximum of(5) is9t^2/(4pi D), attained at the poles. The toroidal maximum of(4) is3(1+t^2)/(8pi), attained at the equator. The latter is strictly smaller: D<3 and1+t^2<2t^2 imply D(1+t^2)<6t^2. The mixture norm squared is a pointwise convex combination, and1-rho_d>0, so its maximum is strictly below the poloidal maximum. Thus

    beta L H/(4pi)<D_inf^2<9beta L t^2/(4pi D).        (10)

This disproves exporting the stronger pure-poloidal amplitude to the whole energy class. It does not refute a theorem that additionally assumes G/(beta L log R)->H, since M_d>H. No simultaneous realization of(7) and(9) is asserted.

## 5. Smooth core and exact energy, including the cross term

For radial g put V_g=gY n+(rg'+2g)grad_S Y/2. The divergence cancels exactly. If g is constant near0, then V_g=sqrt(3/(4pi))g e there, a smooth constant vector. Set b0=sqrt(2beta L rho/D) and A0=sqrt(3beta L(1-rho)/(8pi)). On2-epsilon<r<2 interpolate g from2^t to r^t and w from2^(t-1) to r^(t-1), using a smooth cutoff theta with derivative O(1/epsilon). The endpoint values match at2, so the differences being interpolated are O(epsilon); g,g' and w stay bounded independently of epsilon. Hence the energy in the shrinking transition annulus tends to0.

For U_base=b0 V_g+A0 w Jy, the poloidal and toroidal parts are pointwise perpendicular. Its limiting energy in B2 is

    [b0^2+(8pi A0^2/3)/5]2^beta.

The desired energy L2^beta equals [b0^2 D/2+8pi A0^2/3]2^beta/beta. Each nonzero term has a strict positive deficit because beta<D/2 and beta<5, including rho=0 or1. Fix epsilon sufficiently small to keep a deficit Delta>0.

Let psi>=0 be smooth radial, supported in B_(1/2) and equal to1 near0. Add lambda psi Jy. It remains solenoidal and perpendicular to the poloidal field. Its additional energy is

    lambda^2 I+2lambda B0,
    I=integral psi^2|Jy|^2>0,
    B0=A0 2^(t-1)integral psi|Jy|^2>=0.

This strictly increasing function of lambda>0 ranges from0 to infinity, so exactly one positive lambda fills Delta. This cross term cannot be dropped when A0>0. The exterior shell energy is beta L r^(beta-1); integration from2 gives the exact energy law. Smoothness and all derivative bounds follow from the fixed smooth core and homogeneous exterior.

## 6. Fixed centers and all logarithmic coefficients

The poloidal part is even under inversion and the toroidal part odd; their pointwise orthogonality makes |U|^2 even. Thus the first derivative at a=0 of E_a(R) is integral_(S_R)|U|^2 n=0. A second center derivative is a boundary integral of grad|U|^2, bounded uniformly on each fixed bounded set of centers by O(R^2 R^(2t-1))=O(R^(beta-2)). Taylor expansion in a proves the centered energy remainder. The velocity itself need not be odd or even.

At the origin, homogeneity yields all coefficients in(2) with finite inner errors. Translating by a fixed a changes U by O_a(r^(t-1)), DU by O_a(r^(t-2)) and q by O_a(r^(2t-3)). Tangential projections have the same relative O_a(1/r) error. For F,T the density difference is O_a(r^(2t-1)); with weight r^(-beta) and Jacobian r^2 this is O_a(r^-2)dr. For G,I,J the corresponding density difference is O_a(r^(2t-3)); weight r^(2-beta) and Jacobian give the same integrable r^-2 error. Use the1-Lipschitz property of positive part before and after sphere integration separately. Fixed inner regions contribute finite constants. These estimates prove every O_a(1) remainder, even if q is negative in the core.

## 7. Pressure and the nonzero momentum curl

Let N(y)=1/(4pi|y|), so -Delta N is the Dirac mass. Define P0=sum_(i,j)(D_iD_j N)*(U_iU_j), including the distributional Hessian's delta contribution. Smooth local data permit the principal value; the remote kernel is O(r^-3), and each dyadic tail is O(R^(beta-3)), summable because beta<3. Thus P0 is a distribution satisfying

    -Delta P0=partial_i partial_j(U_iU_j)=tr((DU)^2)=q.

The last equality uses divergence freedom. Local elliptic regularity for the smooth q gives smooth P0. This is only the Poisson equation.

Near0 the completed field is exactly U=d e+a Jy, with d=b0 sqrt(3/(4pi))2^t and a=A0 2^(t-1)+lambda>0. Substitution into the nonpressure full-profile expression gives

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU
       =(1-c)d e+a Jy+a^2J^2y.

The omega terms cancel since DU=aJ and Je=0. As J^2 is symmetric, the last term has zero curl; the displayed expression has curl2a e. The gradient of any C1 scalar has distributional curl0, so no pressure can repair this residual. This holds for every real c and omega. In the same core q=tr(a^2J^2)=-2a^2<0. Exterior positivity is therefore not global positivity.

## 8. Scope and verification

The construction shows that the natural energy law, decay of all derivatives, solenoidality and the Poisson equation alone allow strictly positive, even radial, quadratic source throughout the exterior. An obstruction must use further full-momentum information. The constant-gradient choice separately bounds possible universal derivative-amplitude improvements and keeps the minimum-gradient hypothesis distinction explicit.

All eight source sections, all fifty analytical obligations and the support note were read; the preceding calculations reconstruct every substantive claim. No external theorem beyond elementary spherical identities and local Poisson regularity, no finite-mode approximation to the Euler PDE, numerical experiment or formal build is used. The existing A comparison has now been read in full and checked in Section9. The main arbitrary-omega nonexistence problem remains OPEN.


## 9. Existing comparison and analytical refinements

The existing A comparison, eleven checks and remarks R1-R5, agrees with Sections1-8. Its exact retained bytes are in the team records. The collaborator is configured as model; provider execution is not independently attested. Its diagnostic script and sampled inequalities are not certified. The following refinements have independent analytical proofs.

First, substituting tau=1-2rho/D into m[(1-beta)+beta tau] gives exactly S=m(1-2beta rho/D). Thus the spherical-source lower bound from LIT379 is an equality in its logarithmic coefficient for every member of this family. On the nonnegative-source interval the same is true for I. This statement concerns that source inequality alone, not equality in the separate Cauchy-Schwarz gradient tradeoff.

At rho=1 the exterior is the pure poloidal endpoint. Formula(5) gives negative source exactly on |mu|<sqrt(k/(k+3)). Integration with dOmega=2pi dmu gives its normalized negative coefficient

    C_n=2k t^2 sqrt(k/(k+3))/D.

Its signed coefficient is C_s=m t^2/D; its positive coefficient is C_s+C_n. The maximum gradient coefficient is9t^2/(4pi D), exactly the endpoint amplitude D_*^2/(beta L). These are exterior and logarithmic equalities; they do not assert that two separately chosen smooth cores are identical. Since rho_+<1, this endpoint has both source signs.

Finally, without imposing source positivity, the exact squared amplitude of the aligned one-parameter family is

    3beta L/(8pi) max(A(rho),A(rho)+B(rho)).

The first affine function has slope -(D+t^2)/D<0. The second equals6rho t^2/D+2(1-rho), and has positive slope because3t^2-D=2(k-1)(k-5)>0. Since B(0)<0<B(1), their unique intersection rho_d lies in(0,1). The maximum decreases up to rho_d and increases afterwards. Thus rho_d is the unique amplitude minimizer within this aligned family. Its value is beta L M_d/(4pi); this value supplies an upper bound for the infimum over any larger class containing these controls. The strict inequality below D_* in(10) is not itself an attained optimum for a larger class. Nor does this optimization impose q>=0. The source-positive family optimization is a separate question addressed in LIT387.

R1 is the basis orientation already fixed in(3): replacing p by -p changes both off-diagonal signs and neither invariant. R2 also follows without an axis limit by differentiating r^t[ke-t mu n] and r^(t-1)Jy in Cartesian coordinates; their Frobenius and trace pairings vanish because every scalar product involving the meridional vectors e,n and their cross product is zero. No numerical value or grid enters any conclusion. The original construction and these refinements retain all hypotheses and the non-Euler scope stated above.
