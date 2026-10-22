# Independent verification of exterior exactness with a prescribed disk

Status: complete informal proof, conditional on the already verified reference construction in packet126 / lead section4.31(a). This proves a smooth configuration with compact annular vorticity forcing. It does not prove a B2 profile. The argument was checked independently from the supplied proof, including the weak/strong contraction and the high-order estimate at one fixed radius. Exact algebra controls were run after writing this proof and passed; they supplement the functional-analytic argument.

Written UTC: 2026-10-21T06:21Z.

## Precise statement

Fix beta>2, a0>0, R0>0 and a reference from packet126 whose polynomial core contains B_R0. Let R_ext be a radius beyond which that reference equals the explicit analytic stream Psi_L. There is a finite R_crit>max(R0,R_ext), depending on this reference, such that for every R>=R_crit there are R1=8R and smooth whole-plane fields Psi, Omega=-DeltaPsi, U=grad_perpPsi, Theta, with grad_perp=(-partial_y,partial_x), such that:

- Psi and Omega are odd in x, Theta is even in x, and Theta vanishes on x=0. The stream, relative velocity, vorticity and temperature agree with the chosen reference on B_R.
- V=U-U(0) is the canonical once-subtracted full-plane inverse of Omega. No independent constant drift or harmonic strain is appended.
- Psi_xy(0)=1+beta/2 and Omega_x(0)=4a0/beta. On B_R0, Psi=l x+cxy-(q0/6)x³, Omega=q0x and Theta=a0x², where c=1+beta/2, q0=4a0/beta and l is the reference linear gauge.
- For W=beta X+V, the thermal equation W.gradTheta=(beta-2)Theta holds everywhere. The whole plane is the backward basin of the source0. There is a smooth odd transported coordinate xi, positive for x>0, with W.gradxi=((beta-2)/2)xi and Theta=a0xi².
- Omega>0 for x>0 and Theta>0 off the axis. Put s=1/beta and m=1-2s. For every derivative order j, |D^jV|<=C_j(1+r)^(1-s-j), |D^jOmega|<=C_j(1+r)^(-s-j), and |D^jTheta|<=C_j(1+r)^(m-j).
- The vorticity residual f=W.gradOmega+Omega-Theta_x vanishes on B_R0 and outside B_R1. It is smooth and compactly supported in the intervening closed annulus. Under the already verified analytic-stream obstruction in packet124, f is not identically zero, so these configurations are not profiles.
- r^s Omega(r cos theta,r sin theta) converges in C^infinity(S1) to a smooth angular function A with A(pi-theta)=-A(theta). For cos theta>0, A(theta)>=kappa1 cos theta with kappa1>0.

The radius R is chosen once using finitely many low norms of a fixed reference, beta and fixed cutoffs. It is not enlarged with derivative order. The construction does not claim vanishing of every residual derivative on the intermediate axis segment. It does not preserve an arbitrarily prescribed exterior stream or a preassigned angular limit.

The phrase “all properties of4.31(a) except exterior agreement” should not replace this explicit list:4.31(a) also contains nonvanishing exterior residual assertions that cannot survive exterior exactness. Its particular numerical drift margins are not needed for the statement above.

## Reference input and its tail estimates

Packet126 constructs a smooth odd reference Psi_* with all the prescribed center data, an exact polynomial core on B_R0, Omega_*>0 on the right half-plane, and whole-plane backward basin. The normalized Theta_*=a0xi_*² solves the thermal equation everywhere. Outside a fixed compact set its stream equals

    -B x [L²+x²+nu(y-h)²]^p,
    p=(1-s)/2, B>0, L>0, 0<nu<=1.

This input is a configuration only. We use no unproved vorticity equation outside the core.

Let D(theta)=cos²theta+nu sin²theta. Differentiating the homogeneous leading stream -B x(x²+nu y²)^p gives

    Omega_*(r e_theta)=r^-s cos(theta) J(theta)
                             +O_symbol(x r^-2-s),
    J=2Bp D^(p-2)[(2-s+nu)cos²theta
                                  +nu(3-s nu)sin²theta].

Every j-th derivative of an O_symbol(r^a) remainder is O(r^(a-j)). The shifted quadratic is uniformly positive on annuli after scaling, so this expansion and its differentiated remainders follow from ordinary Taylor expansion in1/r. J is strictly positive because0<s<1/2 and0<nu<=1. Hence for one large R_*,

    Omega_*(X)>=kappa x r^-1-s  (x>0,r>=R_*),
    |D^jV_*|<=C_j r^(1-s-j), |D^jOmega_*|<=C_j r^(-s-j).

The constant term in V_*=grad_perpPsi_*-grad_perpPsi_*(0) is allowed by these velocity bounds.

The temperature symbol estimates require the thermal equation. For tau=log r write a=beta+V_*,r/r and B=(V_*,tan/r)/a. Outside a larger circle a>=beta/2, and every cylindrical derivative of B and V_*,r/(r a) is O(exp(-s tau)). The angular flow obeys z_tau=B(tau,z). Its first derivative is exp(int B_theta), uniformly bounded above and away from0. Higher angular derivatives obey linear scalar equations whose forcing consists of an integrable coefficient times bounded lower derivatives. Induction gives uniform bounds of all orders for the flow and inverse. The equation for H=r^-mTheta_* is

    H_tau+B H_theta= -m V_*,r/(r a) H.

Integration along the flow gives bounded cylindrical derivatives of H, hence |D^jTheta_*|<=C_j r^(m-j). This also proves their local Hölder versions using one further derivative.

Write R_*^v=W_*.gradOmega_*+Omega_*-Theta_*,x. The leading r^-s vorticity is annihilated by beta X.grad+1. Its next term contributes O_symbol(r^-1-s); the advection V_*.gradOmega_* and Theta_*,x are O_symbol(r^-2s). Thus R_*^v=O_symbol(r^-2s). Oddness plus the gradient bound gives |R_*^v|<=C|x|r^-1-2s: for |x|<=r/2 integrate the x derivative along a segment at comparable radius, and elsewhere use the undivided bound.

## Two linear estimates, with their justification

For r>=1 use the weighted local Hölder norm

    ||f||_(gamma;j,alpha)=sup_(|z|=r>=1)
      [sum_(l<=j) r^(gamma+l)|D^lf(z)|
       +r^(gamma+j+alpha)[D^jf]_(alpha;B(z,r/8) intersect {r>=1})].

Fix0<alpha<1. This is equivalent to the C^(j,alpha) norm of r^gamma f on bounded strips in log-radius and angle, uniformly over their position. Only comparable-radius changes are involved in the equivalence.

Choose smooth radial chi=0 on r<=1 and chi=1 on r>=2, and rho=0 on r<=5 and rho=1 on r>=8. Both take values in[0,1]. For an odd e vanishing on B5 put

    P[e](z)=int [G(z-y)-G(-y)-gradG(-y).z]e(y)dy,
    G(z)=-(1/(2pi))log|z|,
    v[e]=grad_perp(chi P[e]),
    b[e]=-2gradchi.gradP[e]-P[e]Delta chi.

For e=O(r^-s), the second-order subtraction makes the tail integral absolutely convergent. Distributionally and then classically,

    -Delta(chi P[e])=e+b[e].

The compact compensator b is supported in1<=r<=2. Separated support gives ||b[e]||_Cj<=C_j||e||_(s;0,0): for potential orders0,1 use the subtractions, and for orders>=2 integrate kernels O(|y|^-order) over |y|>=5. At worst the radial integral is int_5^infinity t^-1-s dt.

The inverse gains one derivative with the exact critical weight:

    ||v[e]||_(s-1;j+1,alpha)<=C_j||e||_(s;j,alpha).       (I)

For order0, split the relative velocity integral at2r and around z. The remote part is bounded by Cr int_2r^infinity t^-1-s dt, the subtraction at0 by C int_1^2r t^-s dt, and the local singular kernel by Cr^-s int_0^Cr dt. Each is O(r^(1-s)), since0<s<1. For one derivative, on a ball at comparable radius subtract e(z) from the principal-value kernel. After scaling, the local integral is bounded by int_0^1 t^(alpha-1)dt. The Hölder difference over separation d is bounded by

    C int_0^2d t^(alpha-1)dt
              +C d int_2d^1 t^(alpha-2)dt <=C_alpha d^alpha.

The distributional local term is a fixed multiple of e. For higher derivatives, put a cutoff around z and commute derivatives onto e there; derivatives of the cutoff use lower derivatives. Outside that ball the differentiated kernel gives the stated power. The compact compensator is already controlled. This proves(I); no artificial exterior boundary or logarithmic cutoff factor occurs.

For transport let w=beta z+u, a=beta+u_r/r>=beta/2, and suppose the required cylindrical derivatives of u/r are O(r^-s). For gamma=nu0/beta, putting F=r^gamma f transforms

    (w.grad+nu0)f=g

into

    F_tau+B F_theta+(nu0/a-gamma)F=r^gamma g/a,
    B=(u_tan/r)/a.                                      (II)

B and nu0/a-gamma have integrable derivatives in tau. Characteristic integration and differentiation therefore give

    ||f||_(gamma;j,alpha)
     <=C[||f|_(r=1)||_C^(j,alpha)+||g||_(gamma+s;j,alpha)]. (III)

For j=0 the angular characteristic must have a uniform Lipschitz bound, available below from the strong ball. For j>=1 the coefficient regularity C^(j,alpha), including Lipschitz control, suffices. The derivative-of-flow induction used for Theta_* proves the spatial and angular derivative estimates. Subtracting two characteristic equations gives the Hölder estimate; the integrability of coefficient differences and uniform Lipschitz flow bounds prevent growth over successive strips. The PDE then gives radial derivatives; its integral formula gives Hölder differences in log-radius for the highest derivatives. Constants depend on finitely many displayed coefficient norms and the integrable factor1/s. For each smooth coefficient field the argument applies at every order, even when its high norms are large. Uniform high norms over all iterates will be proved separately.

## Scaling and low-regularity fixed point

Choose R>=R_* and R>max(R0,R_ext), and put delta=R^-s. Every later restriction is an upper bound on delta; hence they hold for every R beyond one finite threshold. Define

    omega_R(z)=R^s Omega_*(Rz), v_R(z)=R^(s-1)V_*(Rz),
    theta_R(z)=R^-m Theta_*(Rz), g_R(z)=R^(2s)R_*^v(Rz).

All these quantities have symbol bounds uniform in R with respective weights s,s-1,-m,2s. Only finitely many low reference bounds are used in the contraction: v_R through2,alpha, omega_R and theta_R through3,alpha, and g_R through1,alpha.

Seek an exterior vorticity correction eta(Rz)=R^-2s e(z). Its scaled velocity is

    w_e=beta z+delta v_R+delta²v[e].

Let theta_e solve the thermal equation with incoming trace theta_R on r=1. Define T(e)=q by zero incoming trace and

    (w_e.grad+1)q
     =rho[-g_R+partial_1(theta_e-theta_R)
                            -delta v[e].gradomega_R].   (IV)

All characteristics are radially outgoing when delta is small; the source vanishes on r<=5, hence q does too. Parity is preserved in both equations.

Consider the closed strong ball ||e||_(s;1,alpha)<=K, with odd e=0 on B5, and use the weaker metric ||e1-e2||_(s;0,alpha). Estimates(I)-(III) give

    ||theta_e-theta_R||_(-m;2,alpha)<=C delta² ||e||_(s;1,alpha),
    ||theta_e||_(-m;2,alpha)<=L.                         (V)

Indeed the difference equation has source -delta²v[e].gradtheta_R. The inverse provides2,alpha derivatives of v[e], and the reference has the third derivative needed for the product. Its weight is s-m, one factor r^-s below the critical temperature weight.

For two inputs the temperature difference has source -delta²v[e1-e2].gradtheta_e2. The strong bound in(V) and the weak inverse estimate give

    ||theta_e1-theta_e2||_(-m;1,alpha)
                       <=C delta²||e1-e2||_(s;0,alpha).

Using(III) in(IV),

    ||T(e)||_(s;1,alpha)<=C_*(1+delta K),
    ||T(e1)-T(e2)||_(s;0,alpha)
                  <=C_*delta(1+K)||e1-e2||_(s;0,alpha). (VI)

In the second estimate the additional source is -delta²v[e1-e2].grad T(e2). Its required gradient is supplied by the strong1,alpha bound of T(e2). The temperature difference enters with one derivative and is controlled in the weak norm by the preceding estimate. All these sources have weight2s. This explicitly resolves the derivative loss without asserting a contraction in the strong norm.

Choose K=2C_* and then delta sufficiently small for self-mapping, contraction factor<=1/2, and radial speed>=beta r/2. C_* can be fixed first by requiring delta times the low reference norms and delta²K to remain below fixed small constants.

The strong ball is complete in the weak metric. A weakly convergent sequence has locally uniformly bounded first derivatives with equicontinuous alpha-Hölder bounds. Subsequences converge locally for the derivatives, which are identified with the distributional derivative of the given weak limit. The weighted bounds pass to the limit on each annulus, and then globally by their uniform constant. Closed parity and support conditions pass as well. Banach's theorem yields a fixed point. Starting from e0=0 yields smooth iterates en, because smooth inputs give smooth inverse and transport outputs at every order by(I)-(III). Their high norms need not yet be uniform.

## All derivatives at one fixed R

Put en+1=T(en), vn=v[en], un=delta v_R+delta²vn, wn=beta z+un, Pn=gradtheta_en. Differentiating the thermal equation gives exactly

    (wn.grad+2)Pn=-(Dun)^T Pn.                           (VII)

The other equation is(IV) with q=en+1. Uniform low bounds supply

    |un|/r+|Dun|<=D r^-s, |Pn|<=L r^-2s,

as well as critical symbols through order1 for en,Pn and order2 for vn. On the collar3<=r<=4 all derivatives of vn are uniformly bounded: en vanishes on B5, so its potential is separated from its source there. Transport from r=1 gives all derivatives of Pn on r=4 uniformly in n. All derivatives of en vanish there.

Let epsilon=s/4, Hk=8D(k+2), and

    w_(gamma,k)=r^(gamma+k-1-epsilon) exp(Hk r^-s/2).

Define energies over r>4:

    Enk=||w_(s,k) D^k en||_2,
    Tnk=||w_(2s,k) D^k Pn||_2,
    Bnk=||w_(s,k) D^(k+1)vn||_2.

Ordered Euclidean derivative tensors are used throughout. The principal dilation commutator is k beta times the tensor. Since div wn=2beta, for nu0=beta gamma the exact weighted coefficient is

    nu0+k beta-div(w_(gamma,k)^2 wn)/(2w_(gamma,k)^2)
     =1/4-(gamma+k-1-epsilon)un,r/r
                            +(Hk s/2)(beta+un,r/r)r^-s. (VIII)

For gamma=s or2s, |gamma+k-1-epsilon|+(k+1)<=2(k+2). Since beta+un,r/r>=beta/2 and s beta=1, the last term supplies at least2D(k+2)r^-s. Thus(VIII) absorbs the k ordered-slot actions of Dun, and the extra vector-slot action in(VII), leaving at least1/4. Crucially the tensor bound is(k+1)|Dun|, with no faster-growing hidden commutator constant.

Integration by parts from4 toS has nonnegative outer flux, which tends to0 for each smooth iterate because it is O(S^-2epsilon). The incoming flux is0 for en+1 and bounded at each order for Pn. A differentiated equation with weighted source norm F consequently gives unknown norm<=4F+Ck. The constants Ck may be large and order dependent; they do not change R.

The highest elliptic coupling has coefficient1:

    Bnk<=Enk+Ck,                                        (IX)

assuming the induction bounds at lower order. To prove it, choose zeta=0 on r<=3 and1 on r>=4, and ak=zeta w_(s,k). Apply the planar div-curl identity to each vector ak D^Ivn, |I|=k. On its support div vn=0 and curl vn=-en; the compensating b[en] is inside r<=2. Triangle inequalities over ordered tensors give

    ||ak D^(k+1)vn||_2
      <=||ak D^k en||_2+3||gradak D^kvn||_2.

The coefficient3 is harmless; the leading coefficient of Enk is exactly1. On r>4,

    |gradak|<=Ck r^-1 w_(s,k),
    r^-1 w_(s,k)=w_(s,k-1)exp(4D r^-s).

So the last term is bounded by the previous velocity energy. The compact collar is uniformly smooth. The div-curl identity is justified by an outer cutoff: akD^Ivn=O(r^-epsilon), and cutoff errors are O(S^-2epsilon). No uniform high-order weighted singular-integral constant is assumed.

For clarity, all intermediate products in the differentiated equations are lower order in this induction. The previous energies imply H^(k-1) bounds Ck r^epsilon for r^s en and r^(2s)Pn on rescaled annuli, and H^k bounds Ck r^epsilon for r^(s-1)vn. For an intermediate commutator the two available remaining Sobolev orders are nonnegative and sum to k-2. For k>=4, either one is at least2 and supplies L-infinity while the other supplies L2, or both are1 and supply L4 each. These are the ordinary two-dimensional Sobolev embeddings on fixed annuli. For k=2,3 use the low pointwise bounds on D²vn, grad en and grad Pn, with the previous L2 estimates for the other factor. Products gain r^-s from the non-dilation velocity factor. Two factors cost r^(2epsilon) and the weighted energy gains r^-epsilon, giving at most Ck r^(-s+epsilon) per annulus. Its squared dyadic sum is finite. Derivatives of rho are compactly supported; reference derivatives have uniform symbols. Thus all intermediate terms are uniformly bounded, without a new smallness condition depending on k.

The only remaining highest-order coupling in(VII) is -delta²(D^kDvn)^T Pn. Using the pointwise Pn bound, the weight ratio r^s and(IX), its source norm is<=delta²L4^-s Enk+Ck. In(IV), the only highest coupling is rho D^k(Pn)_1, whose weight ratio is r^-s. Therefore

    Tnk<=4delta²L4^-s Enk+Ck,
    E_(n+1),k<=4*4^-s Tnk+Ck,
    E_(n+1),k<=16delta²L4^-2s Enk+Ck.                    (X)

Require once that32delta²L<=1. The recurrence factor is<=1/2 for every k. Since e0=0, induction gives uniform Enk,Tnk,Bnk for every k. Orders0,1 were supplied by the strong ball. This proves high regularity of the limit, not merely an a priori estimate for unknown derivatives: uniform local Sobolev bounds pass to the weak limit of the smooth iterates; the weak contraction and(V) identify that limit with e and gradtheta_e. Sobolev embedding at arbitrary order gives smoothness.

## Restore the critical powers and the angular limit

The energy estimates first give, on rescaled annuli,

    |D^je|<=Cj r^(-s+epsilon-j),
    |D^jP|<=Cj r^(-2s+epsilon-j),
    |D^jv[e]|<=Cj r^(1-s+epsilon-j).

Commute Cartesian derivatives through the fixed-point equations and keep only the dilation commutator on the left. For D^jP the damping is2+j beta and its source is O(r^(-3s+2epsilon-j)). For D^je the damping is1+j beta and its source is O(r^(-2s+2epsilon-j)); the term D^jP is even better than this bound. The low velocity bound gives physical travel time t=s log(r/4)+O(1), uniformly in angle. A transport equation with damping beta gamma and source O(r^(-gamma-sigma)), sigma>0, has solution O(r^-gamma), by its integrating-factor formula along the outgoing characteristic. Here sigma=s-2epsilon=s/2>0. Hence

    |D^je|<=Cj r^(-s-j), |D^jP|<=Cj r^(-2s-j).

Estimate(I), with one additional derivative to control local Hölder seminorms, restores the exact velocity symbols. The thermal equation and transported trace similarly give the claimed Theta bounds.

## Assembly, positivity, and canonical inverse

Return to X=Rz and set eta(Rz)=R^-2s e(z). Define

    Psi=Psi_*+chi(X/R)Phi[eta],
    Phi[eta](Rz)=R^(2-2s)P[e](z).

The correction is identically0 on B_R, and

    Omega(Rz)=R^-s[omega_R(z)+delta(e+b[e])(z)].

The scaled relative drift is exactly wn with en replaced by e. In particular the center velocity subtraction is unchanged, rather than fitted independently. Theta equals the reference in B_R and R^mtheta_e(X/R) outside. Matching is smooth: the cutoff is flat at r=1, the drift coefficients agree to all orders there, and the noncharacteristic transport equation with identical trace determines matching normal derivatives successively.

The inverse estimates and oddness give |e+b[e]|<=C_ax K|z1|r^-1-s. Choose R larger once so C_axKdelta<=kappa/2. The reference lower bound then gives strict positive vorticity for x>0 outside B_R; inside it positivity is unchanged. All backward exterior trajectories reach B_R in finite time, and cannot leave it backwards because its boundary is outward. Within it they are reference trajectories, hence tend to0. The flow is complete since W has at most linear growth. Transporting xi_* from the boundary gives smooth odd xi and Theta=a0xi², positive off the axis.

The correction velocity has divergence0, negative curl equal to the actual added vorticity including b[e], sublinear growth, and value0 at the center. It agrees with the canonical relative inverse: the difference has entire harmonic components, is sublinear, and vanishes at0; the interior harmonic gradient estimate on larger and larger balls forces that difference to be constant, hence0. Thus the cutoff did not append an unadvertised strain or exterior multipole.

Outside4R the compensator is absent. Rescaling(IV) gives

    (W.grad+1)eta=rho(X/R)[Theta_x-W.gradOmega_*-Omega_*].

Consequently the total residual there is(rho-1)[Theta_x-W.gradOmega_*-Omega_*], hence0 outside8R. In B_R0 both stream and normalized temperature are unchanged, so the polynomial core solves both equations. This proves the compact forcing assertion.

For r>8R the vorticity equation is exact. The normalized angular equation for r^sOmega has its transport coefficient and all other coefficients O(r^-s), and normalized source r^sTheta_x=O(r^-s), with all cylindrical derivatives. Its characteristic flow converges with every angular derivative, by the integrable-coefficient induction already proved. The integrated scalar equation also converges with every derivative. Composition with the limiting inverse angular flow therefore gives the C^infinity angular limit. The pointwise positivity margin passes to the limit and yields A>=kappa1 cos theta on the right semicircle.

## Scope, source corrections, and dependencies

This proves the precise configuration theorem stated at the start, conditional on the independently audited reference construction. The choice R>R_ext makes the annulus R_ext<|X|<R nonempty. On this annulus the stream equals the analytic Psi_L; packet124 proves that both B2 equations cannot hold on such an open set. The configurations produced here are therefore nonprofiles. The forcing has not been removed.

Two typographical corrections are required in the supplied extexact2 proof: its first vorticity asymptotic must have a plus sign before O_sym(x r^-2-s), and its displayed axis asymptotic must have a plus sign before O(r^-2-s). The subsequent estimates use precisely those additive remainders and are valid. The explicit theorem above also avoids the overbroad shorthand about retaining every property of4.31(a).

Dependencies: the packet126 reference construction; elementary local Hölder estimates for the explicitly subtracted logarithmic inverse (proved above); scalar transport and Banach contraction; planar div-curl integration by parts; two-dimensional Sobolev embeddings and weak compactness. The proof establishes no claim for beta<=2, no small annular forcing norm in the original fixed normalization, no whole-axis intermediate flatness, and no full B2 endpoint.
