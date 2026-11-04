# Logarithmic growth above the square-root screen

Status: CONFIRMED at the exact conditional scope in A759. No growth premise is inferred from uniform velocity decay alone.

## 1. Exact statement and weights

Let 0<c<1, omega be any finite real number and gamma>=0. Put J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and L=(1-c)I+omega J. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+(DU)(Ay+U)+grad P=0.

Assume, uniformly outside a fixed ball,

    |DU(y)|<=C0 sqrt(r)(log r)^gamma,
    U(y)=o((log r)^(-2gamma)), r=|y|,                     (1)

for a finite C0. Then the conclusions are

    grad P=o((log r)^(-2gamma)), DU->0.                   (2)

No symmetry, helicity, smallness, pressure bound, pressure gauge or integrability is assumed. Constants may depend on the entire fixed profile, compact C2 norms and c,omega,gamma,C0. There is no uniform constant in omega. Gamma=0 is the already confirmed A498 decaying-velocity branch; gamma>0 allows a larger gradient but assumes a quantitative velocity decay. Neither premise follows here from uniform velocity decay alone.

Set G=DU, W=curl U, B=Ay+U, M=sup|U| and m(R)=sup_(|y|>=R)|U(y)|. M is finite. The case M=0 is immediate. Outside a sufficiently large sphere define

    K(r)=sqrt(r)(log r)^gamma, b(r)=(log r)^(2gamma)=K(r)^2/r.

Use b rather than a to avoid confusing this weight with 1-2c in the dynamical results. Choose the starting radius so that

    1/2<=r K'(r)/K(r)<=3/4.                              (3)

Then K(4r)<=4^(3/4)K(r), K(r)<=Cr^(3/4), integral_S^R K(r)dr/r<=2K(R), and b(R)m(R/2)->0. Extend b as a positive nondecreasing bounded weight over the omitted compact ball. Constants absorb comparable-radius weight ratios.

## 2. Pressure normalization precedes every bound

The confirmed A031, independently reproved by A500, identifies the actual pressure gradient with the canonical gradient using U->0, without a derivative bound. Its relevant proof is short. Write Gamma=1/(4pi|x|), F_ij=U_iU_j and p=partial_i partial_j Gamma*F_ij modulo constants, defined by subtracting the far kernel at a fixed point. The Poisson equation gives P-p harmonic distributionally. For any smooth radial unit-mass compact cutoff phi_R,

    ||grad p*phi_R||infinity<=CM^2/R.

The smoothed third derivative of Gamma is L1 and scales with norm R^-1. On the other hand full momentum in divergence form is

    grad P=(4c-1)U-omega JU-div(U tensor Ay+U tensor U).

At each fixed center its radial average tends to zero. For the drift term use the bound CR^-4 integral_(|z-y|<=CR)|z||U(z)|dz and a fixed-ball split; for the quadratic divergence use CM^2/R. Radial means preserve the harmonic gradient of P-p. Hence grad(P-p)=0.

Put N=-Gamma, N_d=chi(./d)N with chi equal to one near zero and supported in radius two. If f=Delta P=-tr(G^2)=-partial_i partial_j F_ij, the exact formula is

    grad P=grad N_d*f-partial_i partial_j grad(N-N_d)*F_ij. (4)

The near kernel has L1 norm at most Cd and radius 2d support. The far kernel has L1 norm at most C/d and O(|x|^-4) tail. Integration by parts against the smooth compact difference N_d-N_e verifies cutoff independence. Thus d can be chosen pointwise without changing the actual gradient. For |y|=R, 0<d<=1,

    |grad P(y)|<=Cd sup_(|z-y|<=2d)|f(z)|
                    +Cm(R/2)^2/d+CM^2/R.                (5)

The final term is the absolute far integral over |z-y|>=R/2.

For fixed epsilon>0, at sufficiently large R one has m(R/2)<=epsilon/b(R). Choose d=epsilon/(b(R)K(R)). The source near y is O(K(R)^2). The two local terms are at most C epsilon K(R)/b(R)=C epsilon R/K(R); the remote term is o(R/K(R)). Constants are independent of epsilon. Therefore

    grad P=o(R/K(R)), b(R)|grad P|=o(K(R)).                (6)

This establishes a finite growth barrier before the unknown weighted supremum is introduced.

## 3. Exterior flow and moving projection

B is locally Lipschitz and has at most linear growth, so its flow is complete. Its radius satisfies cr-M<=r'<=cr+M. Every sufficiently distant point crosses a fixed sphere S>2M/c in finite backward time. For a forward segment from that sphere, with k0=M/c,

    k0+(S-k0)e^(ct)<=r(t)<=(S+k0)e^(ct)-k0,
    r(t)/r(s)<=3e^(c(t-s)), 0<=s<=t.

The first inequalities follow by scalar integration; the strictly positive exterior lower bound on r' proves the finite backward crossing. By (3),

    K(r(t))/K(r(s))<=C exp((3c/4)(t-s)).                  (7)

All sphere data are bounded by compact regularity.

Outside that sphere set

    e=B/|B|, Pi=I-e tensor e, T=Pi G Pi,
    g=Pi G^T e, h=Ge, sigma=W.e, q=U.e, V=U-qe.

Actual momentum and differentiation give

    h=-(LU+grad P)/|B|, De=Pi(A+G)/|B|,
    D_B e=-omega Je+Pi h.                                (8)

By (1),(6), h=o(1/K), g=O(K) and De=O(K/r). In an oriented orthonormal frame e=e3,

    G=((b11,b12,h1),(b21,b22,h2),(g1,g2,h3)),
    W=(g2-h2,h1-g1,b21-b12).

Thus exactly

    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e,
    g.W=(Pi W).h, e.GW=W.h,
    tr(G^2)=tr(T^2)+2g.h+(e.h)^2.

In particular g.h=o(1) is known from the initial pressure barrier, so a fixed constant already gives

    |f|<=C(1+|T|^2).                                    (9)

This constant does not rely on a later boundedness conclusion for T.

The exact vorticity equation B W=G W-W-omega JW yields

    B sigma=-sigma+e.GW+W.Pi h,
    |e.GW+W.Pi h|<=C|G||h|,
    B|W|<=-[1-|T|-2|h|]|W|.                             (10)

The norm inequality uses g.W=(Pi W).h, eliminating the large shear g. A characteristic with nonzero W has nonzero W at every finite time by its homogeneous linear equation; a zero characteristic remains zero. This justifies norm comparison.

The projected field V has ordinary Euclidean divergence and curl

    div V=-e.h-U.D_e e-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e,
    Pi(DV)Pi=T-q Pi(De)Pi.                               (11)

The formulas include all derivatives of the moving projection. No integrability assumption on a plane distribution is used.

## 4. Local Holder bound at the precise K scale

We need

    log(2+[G]_(1/2,B(y,R/8)))<=CK(R), |y|=R.              (12)

A bound with a larger polynomial in place of K would not suffice in the final little-o step.

Let tau=1-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x. The physical fields u=tau^(c-1)Q_s U(y) and xi=tau^-1 Q_s W(y) solve Euler, with dxi/dt=(grad u)xi along their trajectories. On a fixed annulus about the unit sphere, sufficiently close to t=1,

    |grad u|<=ell(t), |xi|<=w(t),
    ell+w<=C tau^-1 K(tau^-c), |u|<=M tau^(c-1).          (13)

Thus integral_(t0)^t(ell+w)<=CK(tau^-c), by (3) and radial change of variables. Physical velocity is globally bounded on each preterminal time interval, so its trajectories exist completely on that interval without a global derivative bound.

Here is the needed localized elliptic estimate. For a ball E whose enlargement E+d stays within the fixed annulus, 0<d<=1/16,

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +Cw d^-1/2(1+|log d|)+CZ,
    Z=M tau^(c-1)+w.                                    (14)

To see this, cut xi off on a fixed larger annulus and form its Biot-Savart field. Its size is bounded by Cw. The difference from u is harmonic on the inner annulus, since -Delta u=curl xi there, so its derivatives and Holder seminorms on smaller balls are bounded by CZ. The derivative singular kernel has degree minus three and mean zero. Near a point subtract xi at that point, giving the local Holder term. Beyond margin d, the kernel action is bounded by Cw(1+|log d|) and its Lipschitz constant by Cw/d. Interpolating proves the stated, possibly larger, logarithmic error. Only local C2 regularity and local bounded vorticity enter.

Fix a unit point xstar. Take t0 sufficiently late that all following balls stay in the annulus and define

    r0(t)=1/4+(2M/c)tau^c,
    Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))),
    E0(t)=exp(integral_(t0)^t ell(q)dq).

Two trajectories ending in this ball at time t lie at an earlier time q in its enlargement by

    d(q,t)=(M/c)((1-q)^c-tau^c)>=M(t-q).

Since r0(q)=r0(t)+2d(q,t), a further margin d remains for (14). Segments joining the trajectories stay in the convex intermediate ball. Backward Gronwall bounds the earlier pair separation by E0(t)/E0(q) times its terminal value. Subtract the vorticity equations along the paths, divide by the square root of terminal separation, and use (14). The result is

    Theta(t)<=E0(t)^1/2 Theta(t0)
      +integral_(t0)^t (E0(t)/E0(q))^1/2
       [(ell+Cw)Theta+Cw^2 ell1(t-q)+CwZ](q)dq,
    ell1(v)=v^-1/2(1+|log v|).                           (15)

The constants can depend on M>0. The bound d>=M(t-q) gives the indicated kernel, with such constants. Every seminorm is finite before t=1 by local C2 regularity.

Divide by E0(t)^1/2. The kernel ell1 is integrable. The coarse bound K(tau^-c)<=C tau^-3c/4, with 3c/4<1, bounds the inhomogeneous integral by C tau^-6, a deliberately loose polynomial. Integral Gronwall and (13) imply

    Theta(t)<=C tau^-6 exp(CK(tau^-c)).

Use (14) once more with fixed margin. Rescale at tau=R^-1/c; the factor converting the physical gradient Holder seminorm to [G] is tau^(1+c/2). Logarithms of all polynomial factors are bounded by CK(R). This proves (12), uniformly by a finite cover of the sphere.

The same logarithmic bound holds for DV and its cut-off divergence and curl. Indeed

    DV=G-e tensor(G^T e+(De)^T U)-q De,
    De=Pi(A+G)/|B|.

Coefficients are algebraic in U,B,|B|^-1 and fixed matrices. Their Holder seminorms have polynomial bounds plus a polynomial multiple of [G], by the mean-value estimate for U,B, |B|>=cr-M, and |G|=O(K). The displayed expression is polynomial of fixed degree in these quantities. Taking the logarithm of its product bound adds only O(log R) to (12). No pressure seminorm or unproved global regularity appears.

## 5. A quantitative local div-curl estimate

Cut a vector field v off in a ball of radius 2rho, keeping it unchanged in radius rho. Let Fv comprise its divergence and antisymmetric derivatives, epsilon_v=||Fv||infinity and H_v=[Fv]_(1/2). The Newtonian reconstruction and the mean-zero degree-minus-three derivative kernel give

    |Dv(0)|<=C[H_v eta^1/2+epsilon_v(1+log(2rho/eta))].    (16)

Inside eta subtract Fv(0); outside eta use epsilon_v and integrate dr/r. The local distributional term costs C epsilon_v. Compact support removes harmonic ambiguity. Choose rho=R/32 and eta=(R^2 max(1,H_v))^-2. For large R, eta<rho, the first term is at most R^-2, and (12) bounds the logarithm by CK(R). Thus

    |Dv(0)|<=CR^-2+C epsilon_v K(R).                     (17)

Use comparable fixed-fraction radii throughout. The cutoff error in Fv is bounded by C sup|v|/R. Its Holder coefficients have only polynomial growth, so they do not change the logarithmic bound.

## 6. One weighted pressure contraction

Define the finite, nondecreasing envelope

    w_*(R)=sup_(|y|<=R)b(|y|)|grad P(y)|.

Equation (6) and compact regularity give w_*(R)<=CK(R). On an exterior characteristic ending at radius R, (8) gives

    |h|<=C(1+w_*(R))/(b(r)r)=C(1+w_*(R))/K(r)^2.

The forcing in the scalar equation (10) is at most C(1+w_*(R))/K(r). Integrate it with damping one; by (7), the convolution is bounded by C/K(R), since 3c/4<1. The sphere term has the same bound. Hence, at radius R,

    |sigma|<=C(1+w_*(R))/K(R).                           (18)

Also |U||De|<=C/K, and the cutoff error m(R/2)/R is O(1/K^2), because b(R)m(R/2) is bounded. Apply (11),(17) on a fixed-fraction ball about y. Comparable radii allow the envelope w_*(2R), and yield

    |T(y)|<=C(1+w_*(2R)).                                (19)

Set k_y=1+sup_(|z-y|<=2)|T(z)|, mu_R=m(R/2)+R^-2, and choose d=mu_R/k_y in (5). At large R, d<=1. The source bound (9) gives near cost C mu_R k_y, and m(R/2)^2/d<=mu_R k_y. Thus

    |grad P(y)|<=C mu_R k_y+CM^2/R,
    k_y<=C(1+w_*(4R)).                                  (20)

Here b(R)mu_R->0 and b(R)/R->0. Multiply (20) by b(R), take the supremum, and isolate a fixed compact ball. For any sufficiently small fixed q>0, after increasing that ball,

    w_*(R)<=C_S+q w_*(4R).

The iterated remainder is at most Cq^n K(4^nR)<=C(q4^(3/4))^n K(R). Choose q4^(3/4)<1 and let n tend to infinity. This proves w_* bounded. Equation (19) then bounds T. Return to (20) with k_y bounded to obtain b(R)|grad P(y)|->0. This proves the first conclusion in (2).

## 7. Full derivative decay

The new pressure bound and (1),(8) give h=o(1/K^2). The scalar forcing in (10) is o(1/K). Integrate from a larger sphere where its coefficient is at most epsilon, using (7) and 3c/4<1; let R grow and then epsilon decrease. This gives sigma=o(1/K). Also |U||De|=o(1/K). Equation (11), including the cutoff term, therefore gives div-curl data o(1/K) for V. Equation (17) yields DV->0 and then T->0.

Choose beta with 3c/4<beta<1. Outside a larger sphere the last inequality in (10) gives W=O(R^-beta/c), by exterior characteristic integration. Finally apply (17) to the cut-off U itself. Its divergence vanishes, its curl is W, and the cutoff error is O(m(R/2)/R). Consequently

    |G(y)|<=CR^-2+CK(R)R^-beta/c+o(1/K(R))->0,

because K(R)<=CR^3/4 and beta/c>3/4. This proves (2).

Afterward A476/A492 give Dini decay and G=O(1/r); for c>1/3, A477 gives G=O(r^-1/c). These stronger bounds are consequences only and were not used to establish boundedness or decay in this proof. There is no numerical or formal computation. The actual pressure normalization, the prior barrier, the fixed source constant, and the finite-growth outward remainder have been kept in their logical order.
