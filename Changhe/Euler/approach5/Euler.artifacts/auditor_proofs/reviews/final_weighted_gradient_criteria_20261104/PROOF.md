# Final recheck of the weighted gradient criteria

Status: CONFIRMED in A3258 at the exact existing A757-A759 scope below, after the complete reconstruction postread and complete focused C comparison. No new theorem direction or automatic gradient-growth premise.

## 1. Exact statements and scope

Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and L=(1-c)I+omega J. Suppose 0<c<1, omega is any fixed finite real number, U belongs to C2(R3;R3), P belongs to C1(R3), and

    div U=0, LU+G(Ay+U)+grad P=0, G=DU.

There are two conditional conclusions, each uniform in direction at infinity:

1. For 1/2<=delta<=5/4, c delta<1 and alpha=2delta-1, if G=O(r^delta) and U=o(r^-alpha), then grad P=o(r^-alpha) and G->0.
2. For gamma>=0, if G=O(sqrt(r)(log r)^gamma) and U=o((log r)^(-2gamma)), then grad P=o((log r)^(-2gamma)) and G->0.

Growth constants are finite, with no smallness assumption. Bounds are required only outside a ball. Constants may depend on the fixed profile, compact C2 norms, c, omega and the indicated exponent. There is no asserted uniform bound in omega. No pressure gauge, pressure growth, energy, vorticity integrability, symmetry or helicity assumption is added. In either case U is bounded and tends uniformly to zero. Write M=sup|U|, m(R)=sup_(|y|>=R)|U(y)| and W=curl U. If M=0 every conclusion is immediate. Below M>0.

The downstream Dini and O(1/r) gradient conclusions use A3249 after G->0 has been proved. The natural rate G=O(r^-1/c) additionally uses 1/3<c<1; boundedness and distributional blowdown zero are supplied by U->0. No condition here is inferred from uniform velocity decay alone.

## 2. Pressure normalization before any estimate

Let Gamma=1/(4pi|x|), -Delta Gamma=delta0 and F_ij=U_iU_j. The canonical distribution p=partial_i partial_j Gamma*F_ij is defined modulo constants by far-kernel subtraction at a fixed point. The subtracted kernel is O(|z|^-4), so bounded F suffices at infinity; cancellation against local C2 F handles the singularity and gives a locally C1 representative. Since -Delta p=partial_i partial_j F_ij=-Delta P, P-p is harmonic. For a smooth compact radial unit-mass function phi_R=R^-3 phi(./R),

    ||grad p*phi_R||infinity<=C M^2/R.

Indeed the smoothed third-derivative Newtonian kernel is smooth and L1, with a degree-minus-four tail; its L1 norm scales as R^-1. Momentum in divergence form is

    grad P=(4c-1)U-omega JU-div(U tensor Ay+U tensor U).

At a fixed averaging center the linear averages tend to zero. The quadratic divergence is O(M^2/R). The remaining term is bounded by C R^-4 integral_(|z-y|<=CR)|z||U(z)|dz, which tends to zero after splitting off a fixed ball and then using m(S)->0. Radial averaging preserves the harmonic field grad(P-p); therefore grad P=grad p. No derivative estimate or unknown pressure envelope was used.

Put N=-Gamma, N_d=chi(./d)N, with chi smooth, one near zero and supported in radius two, and f=Delta P=-tr(G^2)=-partial_i partial_j F_ij. Then

    grad P=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij.             (1)

The near kernel has L1 norm Cd and support radius 2d. The far kernel has L1 norm C/d and tail C|x|^-4. The two terms are continuous; integration by parts against the smooth compact difference N_d-N_e proves that (1) is independent of d. Point-dependent choices of d estimate this same actual pressure gradient.

For |y|=R and 0<d<=1, the local far part is at most C m(R/2)^2/d. The remote part is bounded by

    D(R)=C R^-4 integral_(|z|<=2R)|U(z)|^2 dz
         +C integral_(2R)^infinity m(s)^2 s^-2 ds.                    (2)

For the polynomial case, alpha in [0,3/2] gives D(R)=O(R^-1-2alpha) for alpha<3/2 and D(R)=O(R^-4 log(2+R)) at alpha=3/2. Thus R^alpha D(R)->0 and D(R)=o(R^(1-delta)). Choose d=epsilon R^(-alpha-delta) after m(R/2)<=epsilon R^-alpha. The near bound |f|<=CR^(2delta) and (1) give

    grad P=o(R^(1-delta)).                                          (3)

All constants multiplying epsilon are independent of epsilon. For the logarithmic case set

    K(r)=sqrt(r)(log r)^gamma, b(r)=(log r)^(2gamma)=K(r)^2/r.

Beyond a fixed S, 1/2<=rK'/K<=3/4. Hence K(4r)<=4^(3/4)K(r), K(r)<=Cr^(3/4) and integral_S^R K(r)dr/r<=2K(R). Extend b positively and nondecreasingly to the omitted ball. Here D(R)<=CM^2/R. With m(R/2)<=epsilon/b(R), choose d=epsilon/(b(R)K(R)). This proves

    grad P=o(R/K(R)), b(R)|grad P|=o(K(R)).                           (4)

These are prior growth barriers, not consequences of a later contraction.

## 3. Complete exterior flow and the exact cancellations

Set B=Ay+U. Its locally Lipschitz, at most linear field has a complete flow. Its radius satisfies cr-M<=r'<=cr+M. Every point outside S>2M/c has a finite backward crossing of S: otherwise r'>=cr/2 would force its backward radius below S. Writing k=M/c, forward segments from S obey

    k+(S-k)e^(ct)<=r(t)<=(S+k)e^(ct)-k,
    r(t)/r(s)<=3e^(c(t-s)) for 0<=s<=t.                              (5)

No global derivative bound is used for completeness. Sphere data are bounded by compact regularity. In the exterior define

    e=B/|B|, Pi=I-e tensor e, T=Pi G Pi,
    g=Pi G^T e, h=Ge, sigma=W.e, q=U.e, V=U-qe.

Momentum and differentiation give

    h=-(LU+grad P)/|B|, De=Pi(A+G)/|B|,
    D_B e=-omega Je+Pi h,
    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e,
    g.W=(Pi W).h, e.GW=W.h,
    tr(G^2)=tr(T^2)+2g.h+(e.h)^2.                                   (6)

For example, in a positive frame e=e3, the rows of G are (a,b,h1),(d,f,h2),(g1,g2,h3), and W=(g2-h2,h1-g1,d-b), verifying both contractions. By (3), g=O(r^delta), h=o(r^-delta) in the first case. By (4), g=O(K), h=o(1/K) in the second. Consequently, before introducing any envelope, there is a fixed C with

    |f|<=C(1+|T|^2).                                                (7)

The vorticity equation B W=G W-W-omega JW and (6) yield

    B sigma=-sigma+e.GW+W.Pi h,
    |e.GW+W.Pi h|<=C|G||h|,
    B|W|<=-(1-||T||-2|h|)|W|.                                     (8)

The last estimate is homogeneous. A nonzero vorticity value cannot have a zero earlier on its characteristic, by uniqueness of the linear transport equation. Zero trajectories cause no difficulty. Ordinary Euclidean differentiation gives

    div V=-e.h-U.D_e e-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e,
    Pi(DV)Pi=T-q Pi(De)Pi.                                         (9)

The g cross e term has canceled. This is not an assumption about integrable tangent planes.

## 4. The precise logarithmic derivative cost

The local estimate required below is

    log(2+[G]_(1/2,B(y,R/8)))<=C H(R),                              (10)

where H(R)=R^delta in case 1 and H(R)=K(R) in case 2. Here and below seminorms use Euclidean distance. To verify (10), set tau=1-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x. Physical Euler has u=tau^(c-1)Q_s U(y), xi=tau^-1 Q_s W(y). On a fixed annulus about the unit sphere,

    |u|<=M tau^(c-1), |grad u|<=ell(t), |xi|<=w(t),
    ell+w<=C tau^-1 H(tau^-c).

On each compact preterminal interval these bounded velocities have complete characteristics. With a margin d<=1/16 inside that annulus, local Biot-Savart and harmonic interior estimates give

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+|log d|)+CZ, Z=M tau^(c-1)+w.                  (11)

For completeness, cut off xi at a fixed exterior margin. Subtracting its Biot-Savart field from u leaves a harmonic field, since -Delta u=curl xi there; it need not be curl free. Its derivatives are bounded by CZ. The mean-zero degree-minus-three kernel acts boundedly on the local Holder difference. Beyond d its supremum is Cw(1+|log d|) and its derivative is Cw/d, which give (11) by interpolation.

For centers on the unit sphere use moving radius r0(t)=1/4+(2M/c)tau^c, starting late enough to stay in the annulus. Backward displacements are at most d(q,t)=(M/c)((1-q)^c-tau^c), with r0(q)=r0(t)+2d and d>=M(t-q), leaving the elliptic margin d. Pair separation is bounded by E0(t)/E0(q), E0=exp(integral ell). Subtract xi'=(grad u)xi on a pair of paths and apply (11). If Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))),

    Theta(t)<=E0(t)^1/2 Theta(t0)
      +integral_(t0)^t (E0(t)/E0(q))^1/2
        [(ell+Cw)Theta+Cw^2 ell1(t-q)+CwZ](q)dq,
    ell1(v)=v^-1/2(1+|log v|).                                    (12)

The initial seminorm is finite by local C2 regularity. The kernel ell1 is integrable. In case 1, cdelta<1; in case 2, H(tau^-c)<=C tau^(-3c/4) with 3c/4<1. In either case the inhomogeneous term in (12), after division by E0^1/2, is bounded by Ctau^-6. Integral Gronwall gives

    Theta(t)<=C tau^-6 exp(C H(tau^-c)).                            (13)

For case 2 the exponent uses integral tau^-1 K(tau^-c)dt=(1/c)integral K(r)dr/r<=2K(tau^-c)/c. Replacing it by the coarse power bound at this point would lose the needed tradeoff. Apply (11) with fixed margin and rescale by tau^(1+c/2); a finite cover of the unit sphere proves (10).

The same logarithmic bound applies to DV and its cut-off divergence/curl data: DV=G-e tensor(G^T e+(De)^T U)-qDe. Its coefficients in U,B,|B|^-1 and fixed matrices have polynomial Holder bounds on these balls, by bounded U, polynomial G and |B|>=cr-M. De is linear in G with these coefficients. Thus their logarithms cost only O(log R), dominated by H(R); no pressure seminorm or envelope bound is hidden here.

For a compact field v supported in a ball of radius 2rho and unchanged near its center, let epsv be the supremum and Kv the 1/2-Holder seminorm of its divergence and antisymmetric derivative data. The Newtonian formula gives

    |Dv(center)|<=C[Kv eta^1/2+epsv(1+log(2rho/eta))].               (14)

Inside eta, subtract the center value of the mean-zero singular kernel and integrate the Holder difference; from eta to 2rho integrate epsv dr/r, including the bounded local distributional term. Compact support removes any harmonic ambiguity. Set rho=R/32 and eta=(R^2 max(1,Kv))^-2. Then the first term is at most R^-2 and the logarithm is at most CH(R). The cutoff velocity error is C m(R/2)/R. These estimates apply to V and to U.

## 5. Polynomial envelope and recovery

Let w_*(R)=sup_(|y|<=R)(1+|y|)^alpha|grad P(y)|. Equation (3) supplies w_*(R)<=C(1+R)^delta. On a trajectory ending at radius R, (6) gives |h|<=C(1+w_*(R))r^-2delta. The scalar source in (8) is then at most C(1+w_*(R))r^-delta. Its convolution with damping one is bounded, because (5) and cdelta<1 give

    |sigma(y)|<=C(1+w_*(R))R^-delta.

The initial-sphere term O(R^-1/c) is smaller. Also |U||De|<=Cr^-delta. Apply (9),(10),(14), with a fixed-fraction ball and a harmless enlarged radius for all backward segments. This gives

    |T(y)|<=C(1+w_*(2R)).                                         (15)

Put K_y=1+sup_(|z-y|<=2)|T(z)| and mu_R=m(R/2)+R^-2. Then R^alpha mu_R->0. Choosing d=mu_R/K_y in (1) and using the already fixed (7), the near term is Cd K_y^2, the local far term Cmu_R^2/d, and the remote term D(R). Hence

    |grad P(y)|<=C mu_R K_y+D(R), K_y<=C(1+w_*(4R)).                (16)

After multiplying by R^alpha and separating a compact ball, any fixed small q>0 is available in w_*(R)<=C_S+q w_*(4R). The remainder satisfies

    q^n w_*(4^nR)<=Cq^n+C(q4^delta)^nR^delta ->0

when q4^delta<1. Thus w_* and T are bounded. Returning to (16) proves R^alpha grad P->0. Now h=o(r^-2delta), the scalar source is o(r^-delta), and its damped integral, started at an arbitrarily large fixed sphere, gives sigma=o(r^-delta). Also |U||De|=o(r^-delta). The divergence/curl data of the cutoff V are o(R^-delta); (14) therefore gives DV->0, and (9) gives T->0.

Choose cdelta<beta<1. Equations (5),(8) give W=O(R^-beta/c). Applying (14) to the cutoff U, whose data are O(R^-beta/c)+o(R^-2delta), proves

    |G(y)|<=R^-2+C R^(delta-beta/c)+o(R^-delta) ->0.

This completes case 1. The endpoint cdelta=1 was never included.

## 6. Logarithmic envelope and recovery

Define w_*(R)=sup_(|y|<=R)b(|y|)|grad P(y)| using the positive compact extension of b. Equation (4) gives w_*(R)<=CK(R) outside a fixed ball. Since b m->0, (6) implies |h|<=C(1+w_*(R))/K(r)^2 along a trajectory ending at R. Its scalar source is at most C(1+w_*(R))/K(r). Equations (5) and rK'/K<=3/4 control the damped convolution, because 3c/4<1. Thus

    |sigma(y)|<=C(1+w_*(R))/K(R), |T(y)|<=C(1+w_*(2R)).              (17)

For the second estimate use (9),(10),(14), |U||De|=O(1/K), and the smaller cutoff error O(1/K^2). The local pressure choice d=mu_R/K_y from (16) now gives |grad P(y)|<=Cmu_R K_y+CM^2/R. Both b(R)mu_R and b(R)/R tend to zero. Therefore w_*(R)<=C_S+q w_*(4R), with any fixed small q after choosing S. Its remainder is bounded by C(q4^(3/4))^nK(R), which tends to zero for q4^(3/4)<1. Consequently w_* and T are bounded, and returning to the pressure bound proves b grad P->0.

Now h=o(1/K^2), the scalar source is o(1/K), and its damped convolution gives sigma=o(1/K). Also |U||De|=o(1/K). Equations (9),(10),(14) imply T->0. Choose 3c/4<beta<1. Then W=O(R^-beta/c), and applying (14) to U gives

    |G(y)|<=R^-2+C K(R)R^-beta/c+o(1/K(R)) ->0,

using K(R)<=CR^(3/4). This completes case 2. Gamma is nonnegative throughout this standalone statement.

## 7. Target-range significance and dependencies

For 2/5<c<1/2, the already confirmed energy theorem A053, freshly reconstructed as A3235, gives U=0 under U=o(r^-k), k=(1-c)/c. Indeed its energy coefficient is L=lim R^(-(5-2/c)) integral_(|y|<=R)|U|^2; since 3-2k=5-2/c>0, that velocity premise gives L=0 by radial integration and a fixed-ball split. The zero-coefficient theorem then applies. Here alpha>=k exactly when delta>=1/(2c). Thus case 1 provides an additional derivative screen only for delta<1/(2c) in the target range. This observation does not assert that o(r^-3/2) implies L2.

Dependencies used in the argument are the explicitly derived pressure, flow, local elliptic and transport estimates above. The downstream consequences use the accepted A3249 only after G->0. The target-range comparison uses A3235 only at its stated energy scope. The captured earlier independent proofs and source proofs are listed in the team records. This recheck proves neither an automatic polynomial/logarithmic gradient bound from U->0 nor the unresolved nonexistence conjecture. No computation or formalization is claimed. Existing configured model file collaboration is requested, with its provider runtime independently unattested.
