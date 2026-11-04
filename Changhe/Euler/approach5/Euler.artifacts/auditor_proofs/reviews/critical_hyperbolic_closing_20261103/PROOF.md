# Exact stable contraction excludes noninterior vortical zeros

Status: CONFIRMED A960-A964 after the complete independent derivation and postread. The proof uses an explicit integral contraction. The arbitrary-rotation conjecture with bare velocity decay remains OPEN A965. Focused comparison with the existing configured model agents has been requested; no new response or provider runtime attestation is claimed.

## 1. Exact actual-profile statement

Fix 2/5<c<1/2 and any real omega. Set Jx=(-x2,x1,0), A=cI-omega J, a=1-2c>0, kappa=1+c>0 and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy pointwise

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite C. Let B=Ax+U, Omega=curl U and Phi,Gamma be their complete flows. Let E be the set of points escaping forward under B and O its saturation under Gamma. Let L in C1(O) be the established transported scalar extending k composed with the actual scattering diffeomorphism Xi:E->D=R3 minus {0}, where V is the actual velocity tail and k(z)=(Az).V(z).

Then every y in O with Omega(y)!=0 and L(y)=0 is an interior point of {L=0}. Equivalently, every noninterior zero of L in O has Omega=0. On the actual tail, every z in D with W(z)!=0 and k(z)=0, where W=curl V, is an interior point of {k=0}.

Consequently, on every connected component of the open set {Omega!=0} intersect O, the scalar L either vanishes everywhere or is everywhere nonzero with one sign. The analogous statement holds for k on every connected component of {W!=0} in D. No conclusion excludes an open zero region or a flat zero of V in the support of W.

The assumptions of global zero helicity and the natural first-derivative bound remain explicit. No bound on omega other than finiteness is used; constants in the local constructions need not be uniform in omega.

## 2. The compact critical set supplied by prior audits

Assume for contradiction that such a point y0 is not interior to {L=0}. The confirmed regular-node exclusion A897, transferred from E to O by a finite invertible Gamma map as in A934, gives dL(y0)=0. The confirmed closure theorem A936-A939 supplies the ambient closure Cbar of the full joint B,Omega orbit through y0. It is closed, invariant under both complete flows, lies in O, and every point of it is a noninterior zero of L. Throughout Cbar,

    L=dL=0, U.B=U.Omega=0, B cross Omega=aU!=0,
    D Phi_t(y)^T U(Phi_t y)=exp(-at)U(y).                 (1)

The other exact identities used here are

    D Phi_t(y) Omega(y)=exp(kappa t)Omega(Phi_t y),
    B.L=-aL, Omega.L=0.                                  (2)

The first holds globally, and the scalar laws hold on O. The actual bounded velocity makes every backward B half-orbit bounded. Thus

    K=alpha_B(y0)

is nonempty, compact and invariant under the full B flow. It is contained in Cbar. In particular B,Omega,U are nonzero on K and have the strict uniform bounds there needed below. A sufficiently small closed Euclidean neighborhood of K lies in O and in {U!=0}.

Only these first-order consequences of A936-A939 are needed. The proof does not use Hessian flatness, the plane/annulus classification, absence of carrier cycles, recurrence, local maximality of K, or a surface exhaustion. There is no dependence on the candidate being proved.

## 3. Constructing the exact stable direction

Regard U as a Euclidean covector and put N=U/|U|^2 near K. Then U.N=1. Differentiate the last identity in (1) at t=0. On K it gives

    D U B+(DB)^T U=-aU.                                  (3)

Differentiating U.N=1 along B and using (3) shows

    U.(DB N-DN B)=-a.

Because B and Omega span the kernel of the covector U on K, there are unique continuous bounded real functions beta,delta on K such that

    DB N-DN B=-aN+beta B+delta Omega.                     (4)

Their boundedness follows from compactness and B cross Omega=aU!=0. Define on K

    b(x)=-integral_0^infinity exp(-as)beta(Phi_s x) ds,
    d(x)=-integral_0^infinity exp(-(a+kappa)s)delta(Phi_s x) ds,
    Z(x)=N(x)+b(x)B(x)+d(x)Omega(x).                      (5)

The integrals converge uniformly. The functions b,d,Z are continuous on K, and U.Z=1. For each full orbit x_t=Phi_t x in K, the functions b_t=b(x_t) and d_t=d(x_t) are differentiable in t, even though no transverse differentiability is required. Shifting the integration limits gives

    b_t'=a b_t+beta(x_t),
    d_t'=(a+kappa)d_t+delta(x_t).                         (6)

The bracket identity in (2) means D Omega B=DB Omega-kappa Omega. Combining (4)-(6) therefore yields

    d Z(x_t)/dt=DB(x_t)Z(x_t)+aZ(x_t).

Uniqueness for the linear variational equation gives the exact formula

    D Phi_t(x)Z(x)=exp(-at)Z(x_t),  t in R.              (7)

Define the frame matrix F(t) with columns (Z(x_t),B(x_t),Omega(x_t)), in that order, and let

    D0=diag(-a,0,kappa).

Then

    F'(t)=DB(x_t)F(t)-F(t)D0,
    det F(t)=Z(x_t).(B(x_t) cross Omega(x_t))=a.          (8)

The entries of F and F inverse are uniformly bounded for all t, by compactness, (5) and the strictly positive determinant a. This proves an invariant splitting with exact stable exponent -a, center exponent 0, and unstable exponent kappa. It is stronger than an unspecified exponential estimate and supplies the rate needed for a merely C1 scalar.

## 4. An explicit nonlinear stable curve with the exact rate

Fix x in K. For a perturbation of the form z(t)=x_t+F(t)w(t), the full equation z'=B(z) is equivalent to

    w'=D0 w+R(t,w),
    R(t,w)=F(t)^(-1)[B(x_t+F(t)w)-B(x_t)-DB(x_t)F(t)w]. (9)

Since B is C2 on a fixed compact neighborhood of K and F,F inverse are uniformly bounded, there exist r0>0 and M>=0, independent of t>=0, such that in the maximum norm, for |w|,|v|<=r0,

    |R(t,w)|<=M|w|^2,
    |R(t,w)-R(t,v)|<=M(|w|+|v|)|w-v|.                  (10)

The radius also ensures x_t+F(t)w lies in O. The derivative D_w R is uniformly Lipschitz on these balls and D_w R(t,0)=0.

Write w=(s,b,u), where these three letters in this section are frame coordinates, not the coefficient functions in (5). Let X_a be the Banach space of continuous functions w:[0,infinity)->R3 with norm

    ||w||_a=sup_(t>=0) exp(at)|w(t)|.

For a real parameter xi, define T_xi on X_a by

    (T_xi w)_s(t)=exp(-at)xi
                 +integral_0^t exp(-a(t-r))R_s(r,w(r)) dr,
    (T_xi w)_b(t)=-integral_t^infinity R_b(r,w(r)) dr,
    (T_xi w)_u(t)=-integral_t^infinity exp(kappa(t-r))R_u(r,w(r)) dr.  (11)

All three integrals converge on a small ball of X_a. For ||w||_a<=rho<=r0, their weighted nonlinear norms are bounded respectively by

    M rho^2/a, M rho^2/(2a), M rho^2/(kappa+2a).

Thus ||T_xi w||_a<=|xi|+M rho^2/a. For two functions in this ball, (10) gives a Lipschitz constant at most 2M rho/a. Choose rho>0 so small that rho<=r0 and 2M rho/a<=1/2. If M=0, only the radius restriction is needed. For |xi|<rho/2 the map T_xi takes the closed rho-ball into itself and is a contraction. Its unique fixed point w_xi solves (9), with stable coordinate s(0)=xi and the neutral and unstable coordinates selected by the convergent future integrals.

Since w_0=0, the contraction estimate also gives the sharp bound

    ||w_xi||_a<=2|xi|.                                  (12)

The map xi->w_xi is C1. To justify this regularity, the integral operator in (11) is C1 in xi and w, with derivative obtained by inserting D_w R into each integral. The estimates in (10) and the uniform Lipschitz bound on D_w R give differentiation in the weighted norm. Its derivative in w has norm at most 1/2. Difference quotients therefore converge to the unique solution of the differentiated contraction equation, or equivalently one may invert I-D_w T by its norm-convergent geometric series. At xi=0, D_w R(t,0)=0 gives

    d w_xi(t)/d xi at xi=0=exp(-at)(1,0,0).              (13)

Differentiating the integrals in t shows that z_xi(t)=x_t+F(t)w_xi(t) solves z'=B(z) for all t>=0. Uniqueness identifies it with Phi_t(z_xi(0)). Hence xi->z_xi(0) is a C1 curve through x with tangent Z(x), and for a fixed bound C_F on |F(t)|,

    |Phi_t(z_xi(0))-Phi_t x|<=2C_F|xi|exp(-at).         (14)

This exact rate follows directly from the quadratic forcing in (9). There is no loss in the exponent, no assumed global stable foliation, and no invocation of a closing theorem.

## 5. C1 criticality forces the scalar to vanish on this curve

Since K is compact, lies in O and L=dL=0 on K, continuity of DL gives a modulus epsilon(r) tending to zero as r decreases to zero, such that for q in K and small |v|,

    |L(q+v)|<=epsilon(|v|)|v|.                          (15)

For example, use the supremum of |DL| at points whose distance to K is at most r, within the fixed compact neighborhood. The segment from q to q+v stays in that neighborhood, so the fundamental theorem of calculus proves (15).

The scalar law B.L=-aL and (14)-(15) imply for every t>=0,

    |L(z_xi(0))|=exp(at)|L(Phi_t(z_xi(0)))|
       <=2C_F|xi| epsilon(2C_F|xi|exp(-at)).             (16)

The right side tends to zero. Thus L(z_xi(0))=0 for every sufficiently small xi. Uniformity of the little-o estimate on K is essential and follows exactly from its compactness; pointwise criticality at a moving sequence of unrelated points would not suffice.

## 6. Vorticity saturation gives an open zero neighborhood

Use the local C1 map

    Psi(xi,t,s)=Gamma_s(Phi_t(z_xi(0)))

near (0,0,0). The scalar laws in (2) and Section 5 make L identically zero on its image. The derivative columns at (0,0,0), in the displayed order, are Z(x),B(x),Omega(x). Their determinant is a>0 by (8). The C1 inverse-function theorem shows that the image contains an open neighborhood of x in O. Therefore x is an interior point of {L=0}.

But x lies in K, hence in Cbar, where every point is a noninterior zero by Section 2. This contradiction excludes the initial point y0 and proves the original-profile assertion in Section 1.

For the tail statement, transfer any z through y=Xi inverse(z) in E. The C1 scattering diffeomorphism preserves interiors of zero sets, and its established vorticity pushforward preserves nonvanishing. Thus a noninterior vortical zero of k would give the excluded y. The component conclusions follow because, on the open vortical set, the scalar zero set is both relatively closed and relatively open. A connected component on which the scalar never vanishes has one sign by continuity.

## 7. Sources, verification and scope

The analytic question is whether the compact backward limit set of a noninterior critical joint leaf can remain on the boundary of the transported scalar's zero set. The pass criterion is an exact exp(-at) stable curve and a full-rank local saturation. Sections 3-6 provide both by explicit integral equations; all convergence, derivative regularity and domain conditions are stated.

The first-order critical-closure inputs are A936-A939 in the independently checked proof in the team records. A897 and its finite-vortex transfer are also used there. The exact transport of the velocity covector and of Omega are essential; replacing them by a generic hyperbolicity bound would not establish (16) at C1 regularity.

During the audit, Fisher, Petty and Tikhomirov, Nonlocally Maximal and Premaximal Hyperbolic Sets, arXiv:1510.05933v1, was obtained and Sections 1-2 and the relevant discussion in Section 4 were inspected. Its Theorem 2.5 supplies ambient shadowing and expansivity near arbitrary hyperbolic flow sets, without claiming that every such set has a locally maximal extension. The direct proof above does not depend on that theorem, on periodic shadowing, or on an assertion that a nearby periodic point lies in Cbar. The manuscript is retained only as evidence of the alternative route examined.

No numerical experiment, symbolic computation or formal build is needed. The exact hypotheses of the statement, especially global zero helicity and natural gradient decay, remain additional assumptions beyond the campaign's bare-decay target. Open scalar-zero regions and flat tail-velocity zeros are not excluded. No full nonexistence theorem for every smooth decaying rotating profile is asserted.

## 8. Independent comparison with LIT195

The complete eight-section source in the team records was subsequently read and compared to Sections 1-6 above. Its theorem and its boundary conclusion have precisely the same actual-profile hypotheses. It is independently CONFIRMED A970.

The source uses the opposite bracket remainder notation: [B,N]=aN+bB+dOmega, while (4) writes -[B,N]=-aN+beta B+delta Omega. Thus its b,d equal -beta,-delta. Its positive future integrals f,g therefore equal our b,d in (5), and its vector S is our Z. Both frame equations and determinants are identical. This resolves the apparent sign difference without changing either proof.

The source first uses a weight beta with a/2<beta<a. Its three integral operator bounds are 1/(a-beta), 1/beta and 1/(kappa+beta). Each is valid for forcing bounded in that weighted norm. The quadratic remainder has even faster decay, so these bounds are conservative but sufficient. Its small fixed-point ball and parameter derivative estimates follow from the same C2 remainder as (10).

For its fixed point the forcing is bounded by C eta^2 exp(-2beta t). Since 2beta>a, the stable integral is at most C eta^2 exp(-at)/(2beta-a), and the two future integrals have bounds C eta^2 exp(-2beta t)/(2beta) and C eta^2 exp(-2beta t)/(kappa+2beta). These are exactly its Section 5 formulas. They give the same exp(-at) separation as (14), after which its uniform C1 modulus and full-rank saturation coincide with Sections 5-6 above.

The construction above contracts directly at weight a by retaining quadratic decay in the estimates. The source contracts at a smaller weight and then improves the rate. Both are valid at C2, neither needs a Holder estimate for DL, and neither uses the Hessian-flatness arguments, higher tail regularity, a recurrent point or a closing theorem. The source's order of the carrier and vortex maps cyclically permutes the derivative columns and leaves their determinant a unchanged.

This comparison is a mathematical source audit. The source was written in the literature agent the second model agent; it is not a model response. The requested focused comparison with the existing configured model agents remains separately pending, and provider runtime is not attested.


## 9. Fresh upstream and contraction audit

The complete eight-section proof above, the complete six-section critical-closure proof, the complete origin-separation proof A478 and the compact-plaque part of A118 were reread independently. The repeated audit is CONFIRMED A1061 at the exact hypotheses of Section1.

The ordering of the domain argument is essential. H,Q,g and their differentials first extend to the ambient closure without using L there. Their covector transport excludes a velocity zero by A478 and gives B cross Omega=aU!=0 on that closure. Only then can its intersection with the compact vortex core be treated as a compact regular invariant set. A118 excludes its joint plaque: local strong-stable saturation of a center-unstable plaque is an open set of forward-bounded points, contrary to the nullity supplied by div B=3c. The compactness, nonsingularity and hyperbolicity needed for that saturation are all local to this compact invariant set. The argument does not need a global stable foliation or a periodic orbit. This removes the core before invoking continuity of L on the closure.

On the resulting compact backward limit K, the integrals in (5) need only continuous bounded beta,delta and their along-orbit derivatives in (6). Neither Z nor the frame is differentiated transversely. The fixed-point argument needs C2 of B on a fixed compact neighborhood, which the original profile provides. The three weighted quadratic bounds in Section4 were recomputed; all denominators are positive, and the stable bound is M rho^2/a even at the exact weight a. The parameter derivative is justified in the same weighted norm using the uniformly Lipschitz derivative of the remainder. The stable curve is C1 in its parameter, as required by the final inverse-function theorem.

The scalar estimate in (15) is uniform on K. Consequently its little-o factor survives the multiplication by exp(at) in (16), and the stable curve lies in the zero set. The local saturation has determinant a, not merely an unspecified nonzero sign. Every map acts inside O for the small parameters used. These checks reveal no circularity, hidden C2 assumption on L, second derivative of the scattering map, or extension of the tail flow through its deleted origin.

This reread confirms the existing A963 conclusion; it supplies no exclusion of interior zero regions or supported flat tail zeros. The later common-pressure-zero result A1057 remains conditional on the same HF/natural actual-profile class. Focused configured-model feedback on this contraction remains pending; the upstream A478 coordinator source and the separately received198199 review do not count as a new focused response.
