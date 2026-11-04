# Conditional sign propagation for the original work

## 1. Exact class and already verified inputs

Fix2/5<c<1/2 and any finite real omega. Put a=1-2c>0, b=2(1-c)=a+1, p=(1-c)/c, A=cI-omega J, Jx=e3 cross x. Let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+DU(Ay+U)+omega JU+grad P=0, div U=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

Let Pinf be the actual pressure limit and define

    B=Ay+U, Omega=curl U,
    H=P-Pinf+|U|²/2+(Ay).U,
    Q=P-Pinf-|U|²/2, g=H-Q=U.B.

The confirmed C47/C49 inputs give a complete B flow Phi_t, its flow-invariant forward-escaping region E, a C1 diffeomorphism Xi:E->D=R3 minus{0}, actual tails V,W=curl V,P2, and W(Xi(y))=D Xi(y)Omega(y). They also give H,Q,g in C2, H(Phi_t y)->0, BH=-ag, and dH wedge dQ=0 where Omega!=0 in E. Completeness uses the linear growth and local Lipschitz continuity of B; no nonexistent terminal physical-time flow is assumed.

Write X=Ax, k=X.V, S=P2-|V|²/2. The terminal coefficient sigmabar=pbar1-2V.grad P2 is the actual coefficient of C51, including c=3/7. A1492-A1496 verified the resonant coefficient; no arbitrary harmonic pressure addition is allowed. These are dependencies of this theorem, not consequences of velocity decay alone.

## 2. The strict terminal alternatives

For x=Xi(y), y_t=Phi_t y, the established expansions give

    exp(at)g(y_t)->k(x),
    exp(bt)g(y_t)->-(1+a)S(x) if k(x)=0,
    exp((a+2)t)g(y_t)->-(a+2)sigmabar(x)/2
                                      if k(x)=S(x)=0. (1)

Thus any one of

    k<0; k=0<S; k=S=0<sigmabar

makes g(y_t)<0 for all sufficiently large t. Reversing each strict sign gives eventually positive g. Each conclusion follows from a nonzero scalar limit with a positive exponential normalization. The third alternative uses the actual resonant theorem at c=3/7; the others do not. No conclusion follows from (1) when all three coefficients vanish.

## 3. Regular points of H preserve zero or nonzero work

If Omega(y)!=0, then Omega(y_t)!=0 for every real t. Indeed its transport is the invertible linear Cauchy law Omega(y_t)=exp(-(1+c)t)D Phi_t(y)Omega(y). On any interval J where grad H(y_t)!=0, rank gives

    grad g=lambda grad H,
    lambda=(grad g.grad H)/|grad H|²,
    d g(y_t)/dt=-a lambda(y_t)g(y_t).              (2)

The coefficient is continuous, in fact C1 near each trajectory point. Integrating (2) between any two finite times in J gives a nonzero exponential multiplier. Therefore g either vanishes throughout J or nowhere there. Every finite boundary time of {t:g(y_t)!=0} must have grad H(y_t)=0: otherwise a small regular interval around that zero time contradicts (2).

If grad H(y_t)!=0 for every t>=0 and the terminal sign is negative, (2) propagates eventual negativity back to every t>=0. Finally BH=-ag and the zero limit of H give

    H(y_t)=a integral_t^infinity g(y_s)ds<0.       (3)

The improper integral is finite because it equals H(y_t)/a; its one-signed integrand makes it absolutely convergent. This proves all of C52(a)-(c).

## 4. The open-neighbourhood criterion and its converse tests

Let O be open in E and forward invariant under Phi_t. Suppose O intersect{Omega!=0} is dense in O, grad H never vanishes on that vortical subset, and every vortical point of Xi(O) has one of the strict negative terminal alternatives of Section2. For any vortical y in O, forward invariance and the Cauchy law retain both regularity and vorticity on its entire forward orbit. Invertibility of D Xi makes Xi(y) vortical. Section3 proves g(y)<0, and density plus continuity gives g<=0 throughout O.

Conversely, if g<=0 on the late part of one orbit, it cannot have a positive terminal alternative. If g<=0 on such a forward-invariant O, this applies to every point of Xi(O), giving

    k<=0; S>=0 on{k=0}; sigmabar>=0 on{k=S=0}.

These are necessary conditions. They do not replace density, regularity or strict terminal signs in the sufficient criterion. A point in supp W only ensures some nearby vorticity, not a dense vortical subset. The case k=S=sigmabar=0 remains uncovered. Thus the claimed neighbourhood of a common flat orbit has not been constructed.

## 5. The regular-work critical surface and transverse crossings

The exact identity grad H=B cross Omega-aU shows that at Omega=0, critical points of H are precisely zeros of U. At a vortical critical point p of H, BH=-ag gives g(p)=0. Assume also grad g(p)!=0. Vorticity remains nonzero and g remains a C2 submersion in a neighbourhood. Rank then implies H=F(g) there for some C2 one-variable function F: in submersion coordinates all derivatives of H tangent to the g levels vanish. Since grad H(p)=0, F'(0)=0 and

    Hess H(p)=F''(0) grad g(p) tensor grad g(p).

Differentiating BH=-ag at p cancels the derivative-of-B term because grad H(p)=0. Therefore Hess H(p)B(p)=-a grad g(p), and

    F''(0)(B.grad g)(p)=-a.                       (4)

Both factors are nonzero. If F''(0)>0, work crosses from positive to negative; if F''(0)<0, the reverse crossing occurs. Continuity of F'' and F''(0)!=0 makes F' vanish only at0 locally. Thus the critical set of H near p is exactly the C2 surface{g=0}, transverse to B, and nearby crossings have the same direction. This is conditional geometry and does not construct such a point in a global profile.

For the extended remark, set N={y in E:Omega(y)!=0, grad g(y)!=0}, and let L be the connected component through p of N intersect{g=0}. On N, mu=(grad H.grad g)/|grad g|² is C1 and dH=mu dg. Taking the exterior derivative gives dmu wedge dg=0. Hence mu is locally constant along every g-level, and connectedness of L yields mu=mu(p)=0 on L. Submersion charts give mu=m(g) with m C1. On overlapping charts at a point of L the two functions agree on an interval containing0, so their derivatives at0 agree. A chain of such overlaps along L makes m'(0)=F''(0) constant on L. Formula(4) makes B.grad g=-a/F''(0) constant there as well. Connected components of this regular surface are path connected, so the overlap-chain argument needs no extra global topology assumption.

## 6. Audit verdict and exact limitations

The complete source, including its Remark2 extension through15:40:59Z, was read. Every section of this reconstruction was postread. C52(a)-(e) and the conditional crossing geometry are confirmed at Section1's zero-helicity and natural-derivative class. No common-flat neighbourhood, sign of F'' in an actual profile, arbitrary-helicity theorem or bare-decay theorem follows. Original and tail vorticities remain distinct throughout. All omega are admitted, with no division by omega. No computation or formal build was needed. The existing configured model source supplies the collaborator's argument; its provider runtime is unattested. The general campaign conclusion remains open.
