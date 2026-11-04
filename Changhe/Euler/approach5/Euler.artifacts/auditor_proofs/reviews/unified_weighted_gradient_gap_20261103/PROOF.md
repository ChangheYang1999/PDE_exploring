# Quantitative velocity decay controls polynomial gradient growth

Status: CONFIRMED at the exact conditional scope in A757-A758. No growth premise is inferred from uniform velocity decay alone.

## 1. Exact statement

Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, L=(1-c)I+omega J, with 0<c<1 and any finite real omega. Fix

    1/2 <= delta <= 5/4, c delta < 1, alpha=2delta-1.

Suppose U in C2(R3;R3), P in C1(R3) solve the full equations

    div U=0, LU+(DU)(Ay+U)+grad P=0,
    |DU(y)| <= C0(1+|y|)^delta,
    |U(y)| = o(|y|^-alpha) uniformly at infinity,              (1)

where C0 is finite. The conclusions are

    grad P=o(r^-alpha), DU->0 uniformly as r=|y|->infinity.    (2)

The actual pressure is used. No pressure growth bound, pressure gauge, symmetry, helicity, integrability, small coefficient or small rotation is assumed. Constants can depend on the entire fixed profile, including compact C2 norms, and on c,omega,delta,C0. Uniform constants over omega are not claimed.

Write G=DU, W=curl U, B=Ay+U, F_ij=U_iU_j, M=sup|U| and m(R)=sup_(|y|>=R)|U(y)|. Then M is finite and R^alpha m(R)->0. The case M=0 is immediate, so suppose M>0. All following asymptotic estimates are uniform in direction.

## 2. The actual canonical gradient and its split

We first reproduce the pressure argument of A500, already within the stronger scope of A031. Let Gamma=1/(4pi|x|), so -Delta Gamma=delta0. The canonical p=partial_i partial_j Gamma*F_ij is defined modulo constants by subtracting the far kernel at a fixed point. The subtracted kernel has tail O(|z|^-4), integrable against bounded F. The principal value near the origin is defined by cancellation against the locally C2 field F. Consequently p is a distribution satisfying

    -Delta p=partial_i partial_j F_ij=-Delta P.

Thus H0=P-p is harmonic distributionally and is represented by a smooth harmonic function. For any smooth compactly supported radial phi of integral one, phi_R=R^-3 phi(./R), the kernel D3Gamma*phi is smooth, has O(|x|^-4) tail, and is in L1. Homogeneity gives

    ||grad p*phi_R||infinity <= C M^2/R.                      (3)

Actual momentum, including div B=3c, gives

    grad P=(4c-1)U-omega JU-div(U tensor Ay+U tensor U).       (4)

For each fixed averaging center y, the averages of the first two terms tend to zero by uniform U decay. The quadratic divergence is O(M^2/R). The linear-drift divergence average is bounded by

    C R^-4 integral_(|z-y|<=C R) |z| |U(z)| dz -> 0.

To obtain this limit, split off a fixed compact ball, let R grow, then let the exterior supremum of |U| decrease to zero. Every radial average of grad H0 equals grad H0 itself by the harmonic mean-value property. Subtracting (3) from the averaged (4) proves grad H0=0. Therefore grad P is the canonical gradient, without any bound on G being needed for normalization.

For pointwise estimates put N=-Gamma and N_d=chi(./d)N, where chi is smooth, one near zero and zero outside the radius-two ball. The Poisson source is

    f=Delta P=-tr(G^2)=-partial_i partial_j F_ij.

Integration by parts in the canonical distribution gives

    grad P=Q=grad N_d*f-D3_ij(N-N_d)*F_ij.                   (5)

Here D3_ij denotes grad partial_i partial_j. The near kernel has L1 norm at most Cd and compact support; the far kernel has L1 norm at most C/d and tail O(|x|^-4). Both convolutions are continuous. There is no need to define an undifferentiated far potential. Independence of d can also be checked by integrating f=-partial_i partial_j F_ij against derivatives of the smooth compact difference N_d-N_e. Hence d can be chosen separately at each evaluation point.

At |y|=R and 0<d<=1, split the far convolution into |z-y|<R/2 and its complement. The first part is bounded by C m(R/2)^2/d. On the complement, split at |z|=2R. The resulting bound is

    D(R)=C R^-4 E(2R)+C integral_(2R)^infinity m(s)^2 s^-2 ds,
    E(R)=integral_(|z|<=R)|U(z)|^2 dz.                       (6)

Indeed, the kernel is at most CR^-4 in the first region; in the second, |z-y|>=|z|/2 and spherical integration leaves s^-2 ds. The global bound |U|<=C(1+r)^-alpha yields

    D(R)<=C R^(-1-2alpha)       if 0<=alpha<3/2,
    D(R)<=C R^-4 log(2+R)       if alpha=3/2.                 (7)

In every stated case, R^alpha D(R)->0 and D(R)=o(R^(1-delta)). This includes alpha=1, where the crude bounded-velocity remote estimate would be insufficient for the later weighted conclusion.

Fix epsilon>0 and choose d=epsilon R^(-alpha-delta) at large R. On the near ball, |f|<=C R^(2delta), while m(R/2)<=epsilon R^-alpha after increasing the threshold. Equations (5)-(7) give

    |grad P(y)|<=C epsilon R^(delta-alpha)+D(R).

The constant is independent of epsilon. Since delta-alpha=1-delta, this proves the prior bound

    grad P=o(R^(1-delta)).                                  (8)

In particular the later envelope estimate has an established growth barrier.

## 3. Exterior characteristics and exact carrier projections

B is C1 and grows at most linearly, so its flow is complete in both time directions. Its radius satisfies cr-M<=r'<=cr+M. Every exterior point reaches a fixed sphere of radius S>2M/c in finite backward time: otherwise r'>=cr/2 would force the backward radius below S. Put k=M/c. On forward segments beginning at that sphere,

    k+(S-k)e^(ct)<=r(t)<=(S+k)e^(ct)-k,
    r(t)/r(s)<=3e^(c(t-s)) for 0<=s<=t.                    (9)

These estimates use no bound on DB. Sphere data are bounded by compact regularity.

Outside the sphere define

    e=B/|B|, Pi=I-e tensor e, T=Pi G Pi,
    g=Pi G^T e, h=Ge, sigma=W.e, q=U.e, V=U-qe.

The lower bound |B|>=cr-M and actual momentum give

    h=-(LU+grad P)/|B|,
    De=Pi(A+G)/|B|,
    D_B e=-omega Je+Pi h.                                   (10)

By (1),(8), h=o(r^-delta), g=O(r^delta), and De=O(r^(delta-1)). The following are exact algebraic identities:

    G=T+e tensor g+h tensor e,
    W=g cross e+e cross h+sigma e,
    g.W=(Pi W).h, e.GW=W.h,
    tr(G^2)=tr(T^2)+2g.h+(e.h)^2.                            (11)

For example, in an oriented frame e=e3,

    G=((a,b,h1),(d,f,h2),(g1,g2,h3)),
    W=(g2-h2,h1-g1,d-b),

which verifies both contractions directly. Since g.h is already bounded by (8), there is a fixed constant, established before any unknown envelope bound, such that

    |f|<=C(1+|T|^2).                                        (12)

The vorticity equation B W=G W-W-omega JW gives

    B sigma=-sigma+e.GW+W.Pi h,
    |e.GW+W.Pi h|<=C|G||h|,
    B|W|<=-[1-|T|-2|h|]|W|.                                (13)

The final estimate follows from (11); the rotation term has zero scalar product with W. Along a characteristic ending at nonzero W, the homogeneous linear vorticity equation prevents W from vanishing earlier. Characteristics with W identically zero are harmless. This justifies comparison for its norm.

The ordinary Euclidean divergence and curl of V satisfy

    div V=-e.h-U.D_e e-q div e,
    curl V=e cross h+sigma e-((De)^T U) cross e-q curl e,
    Pi(DV)Pi=T-q Pi(De)Pi.                                  (14)

The large shear g cross e cancels. No integrability of a tangent-plane field is assumed or required.

## 4. A local Holder estimate with exponential growth

We need the bound

    log(2+[G]_(1/2,B(y,R/8)))<=C R^delta, |y|=R.              (15)

It follows locally from physical Euler without any global gradient bound. Set tau=1-t, s=-log tau, Q_s=exp(omega sJ), and y=exp(sA)x. The exact transformed fields are

    u(x,t)=tau^(c-1) Q_s U(y), xi(x,t)=tau^-1 Q_s W(y).

On a fixed annulus about the unit sphere they satisfy physical Euler and

    |grad u|<=ell0(t), |xi|<=w0(t),
    ell0+w0<=C tau^(-1-cdelta), |u|<=M tau^(c-1).             (16)

For each preterminal time interval, the globally bounded physical velocity has complete characteristics. Only its local derivatives on this annulus are used below.

Here is the needed local elliptic estimate. If E has margin d<=1/16 inside the annulus, localization of the Biot-Savart formula yields

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +C w0 d^-1/2(1+|log d|)+C Z0,
    Z0=M tau^(c-1)+w0.                                     (17)

To check the harmonic remainder, cut off xi at a fixed distance outside the inner annulus. Its Biot-Savart field has size at most Cw0; subtracting it from u is harmonic on the inner annulus since -Delta u=curl xi there. Harmonic interior estimates control its derivatives and their Holder seminorms by CZ0. For the singular part, the degree-minus-three kernel has zero spherical mean. Its local action on Holder differences is bounded by the local Holder seminorm; beyond the margin its supremum is at most Cw0(1+|log d|) and its Lipschitz bound at most Cw0/d. Interpolating those two bounds gives the displayed, slightly larger, d^-1/2 logarithmic term. This requires only local C2 regularity and the bounded vorticity on the fixed annulus.

Fix xstar on the unit sphere and take t0 sufficiently late that all balls below stay in the fixed annulus. Set

    r0(t)=1/4+(2M/c)tau^c,
    Theta(t)=[xi(t)]_(1/2,B(xstar,r0(t))),
    E0(t)=exp(integral_(t0)^t ell0(q)dq).

Two paths terminating in this ball at t remain at earlier q in the ball enlarged by

    d(q,t)=(M/c)((1-q)^c-tau^c),
    d(q,t)>=M(t-q), r0(q)=r0(t)+2d(q,t).

There is still a margin d for (17). Joining segments stay in the convex intermediate ball and hence in the fixed annulus. Backward Gronwall bounds earlier pair separation by E0(t)/E0(q) times terminal separation. Subtracting xi'=(grad u)xi on the two paths, dividing by the square root of terminal separation, and applying (17) gives

    Theta(t)<=E0(t)^1/2 Theta(t0)
      +integral_(t0)^t (E0(t)/E0(q))^1/2
        [(ell0+Cw0)Theta+Cw0^2 ell1(t-q)+Cw0 Z0](q)dq,
    ell1(v)=v^-1/2(1+|log v|).                              (18)

Divide by E0(t)^1/2. Since cdelta<1, w0^2<=C tau^(-2-2cdelta) has exponent strictly below four. The kernel ell1 is integrable, and w0 Z0 has no larger necessary singularity. The inhomogeneous integral is therefore at most C tau^-6, a deliberately loose monotone bound. Integral Gronwall, with integral(ell0+Cw0)<=C tau^-cdelta, yields

    Theta(t)<=C tau^-6 exp(C tau^-cdelta).

Apply (17) once more with fixed margin. Under the rescaling tau=R^-1/c, the factor taking the physical gradient Holder seminorm to [G] is tau^(1+c/2). Taking logarithms proves (15), uniformly over xstar. A finite cover of the unit sphere makes the constants uniform.

The same logarithmic bound applies to DV and its cut-off divergence/curl. To see this without introducing a pressure seminorm, use

    DV=G-e tensor(G^T e+(De)^T U)-q De.

The coefficients are algebraic expressions in U,B,|B|^-1 and fixed matrices. On the relevant balls U and G have polynomial bounds, |B|^-1<=C/R, and their coefficient Holder seminorms have polynomial bounds by the local mean-value estimate. De is linear in G with these coefficients. Thus the Holder seminorm of DV is at most a polynomial in R times 1+[G]_(1/2). Smooth cutoffs on fixed fractions of R also have only polynomial costs. No bound on the unknown envelope is hidden in this estimate.

## 5. The compact-support logarithmic div-curl estimate

Let v be supported in the radius-2rho ball and unchanged inside radius rho. Write Fv for its divergence and antisymmetric derivative data, epsv=||Fv||infinity and Kv=[Fv]_(1/2). The compact-support Newtonian formula gives, at the center,

    |Dv(0)|<=C[ Kv eta^1/2+epsv(1+log(2rho/eta)) ],
    0<eta<=min(1,rho).                                      (19)

The second derivative kernel has a bounded local distributional term and a mean-zero degree-minus-three part. Inside eta subtract the center value and integrate the Holder difference; outside eta integrate epsv dr/r. There is no harmonic remainder because the whole field is compactly supported.

Use rho=R/32 and eta=(R^2 max(1,Kv))^-2. For large R the near term is at most R^-2, and (15) bounds the logarithmic factor by CR^delta. The cutoff velocity error is at most C m(R/2)/R. These observations apply to both V and U.

## 6. The single weighted envelope iteration

Define the finite, increasing envelope

    w(R)=sup_(|y|<=R) (1+|y|)^alpha |grad P(y)|.

The prior estimate (8) implies

    w(R)<=C(1+R)^delta.                                     (20)

For a trajectory segment (9) of radii r<=R, (1),(10) give

    |h|<=C(1+w(R))r^(-alpha-1)=C(1+w(R))r^-2delta.

Thus the scalar source in (13) is at most C(1+w(R))r^-delta. Because cdelta<1, the radius-ratio bound in (9) allows its convolution against damping one. The bounded initial-sphere term decays as R^-1/c and is smaller. Therefore

    |sigma(y)|<=C(1+w(R))R^-delta, |y|=R.                    (21)

Also |U||De|<=C r^-delta. The h terms and cutoff errors decay at least as r^-2delta. Apply (14),(15),(19) on a fixed-fraction ball about y, enlarging the envelope radius to 2R to cover every needed exterior trajectory. This yields

    |T(y)|<=C(1+w(2R)).                                     (22)

In particular this estimate does not require w to be bounded beforehand.

Put

    K_y=1+sup_(|z-y|<=2)|T(z)|, mu_R=m(R/2)+R^-2.

Then R^alpha mu_R->0 because alpha<=3/2. Choose d=mu_R/K_y in (5), which lies in (0,1] for large R. The already fixed bound (12) makes the near term at most Cd K_y^2. The local far term is at most Cmu_R^2/d, and the remote term is D(R). Consequently

    |grad P(y)|<=C mu_R K_y+D(R),
    K_y<=C(1+w(4R)).                                        (23)

Multiply by R^alpha. Both C R^alpha mu_R and R^alpha D(R) tend to zero. Given any fixed sufficiently small q>0, separate off a compact ball and take the supremum to obtain

    w(R)<=C_S+q w(4R) for large R.                          (24)

The constant C_S can depend on the chosen starting radius, but not on R. Iterating n times leaves a remainder bounded using (20) by

    q^n w(4^n R)<=Cq^n+C(4^delta q)^n R^delta.

Choose q4^delta<1 and let n tend to infinity. Thus w is bounded. Equation (22) then makes T bounded. Returning to (23) with bounded K_y proves the actual little-o estimate

    grad P=o(R^-alpha).                                     (25)

This is the only envelope iteration. Its prior pressure barrier and fixed source constant were established in Sections 2-3, so it is not circular.

## 7. Recovery of the full gradient

From (1),(10),(25), h=o(R^-2delta). The scalar source in (13) is o(R^-delta). Integrate from an arbitrarily large fixed sphere where its coefficient is at most epsilon; cdelta<1 controls the convolution and the initial data term is smaller. Let the exterior radius tend to infinity, then epsilon tend to zero. This proves sigma=o(R^-delta). Moreover |U||De|=o(R^-delta).

By (14), the cut-off divergence/curl data of V are o(R^-delta), including the smaller velocity cutoff error. Their product with the O(R^delta) logarithm in (19) tends to zero. Hence DV->0, and (14) gives T->0.

Choose beta with cdelta<beta<1. On a sufficiently large exterior region, the homogeneous inequality (13) gives B|W|<=-beta|W|. Equation (9) and bounded sphere data imply

    |W|<=C R^(-beta/c).

Finally cut off U itself. Its divergence/curl data are O(R^-beta/c)+o(R^-2delta). Applying (15),(19) gives

    |G(y)|<=R^-2+C R^(delta-beta/c)+o(R^-delta)->0.

This proves (2). Only now may one use the confirmed A476/A492 for Dini decay and DU=O(1/r), or A477 for DU=O(r^-1/c) when 1/3<c<1. None of these consequences was used to prove boundedness of G.

## 8. Scope in the target range and verification questions

The result holds for every finite omega, with parameter-dependent constants. It remains conditional on both estimates in (1). It proves neither nonexistence at bounded-gradient scope nor a polynomial bound on DU from U->0 alone. The endpoint cdelta=1 is excluded.

In the target range 2/5<c<1/2, the confirmed energy theorem A053 already implies U=0 whenever U=o(r^-k), where k=(1-c)/c. Our alpha=2delta-1 reaches this threshold exactly when delta=1/(2c). Thus for each such c, the additional gradient-screen content of this argument lies in

    1/2<=delta<1/(2c).

For delta>=1/(2c), its velocity premise alone gives the stronger zero conclusion. At delta=5/4 this is true for every target c, even though the isolated decay condition o(r^-3/2) does not by itself imply L2 membership. This distinction affects the result's significance, not the validity of the argument above for its larger stated c range.

The entire source was read before this independent reconstruction. An additional focused configured-model comparison is requested on the general-delta Holder estimate, the fixed source bound before the envelope, the remote kernel bound including alpha=3/2, and the outward remainder. Existing file collaboration is with the coordinator configured with the primary model; actual provider runtime is not independently attested. No new model client, computation or formalization is used.
