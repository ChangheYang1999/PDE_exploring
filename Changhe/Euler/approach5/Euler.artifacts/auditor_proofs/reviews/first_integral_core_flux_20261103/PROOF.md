# First-integral core flux and the angular concentration set

Status: CONFIRMED A730-A735 after full submitted-source, dependency and independent-proof reads.

## 1. Exact profile hypotheses and conclusions

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c, d=p-1, a=1-2c=cd, eta=d/(2p), q=1/eta, Jx=(-x2,x1,0), and A=cI-omega J. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0 everywhere,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1),                       (1)

with finite C. The rate assumptions can instead be supplied by U->0 and DU=O(sqrt(|x|)), using A601. They are not derived from bare decay here.

Write V,W,P2 for the actual velocity, vorticity and canonical pressure tails on D=R3 minus{0}. Set k=(Ax).V, S=P2-|V|^2/2, K=k on S2, h=S on S2, G=W on S2, and pi(x)=exp((omega/c)log|x| J)x/|x|. An admissible f is a continuous nonnegative function on D, constant on EVERY maximal W curve, such that

    f(exp((log r)A/c)w)=r^(-1)f(w).

Examples are f_k=|k|^(1/d), f_S=|S|^(1/(2p)), and f_*=max(f_k,f_S). For an angular set H put

    m_f(H,s)=integral_(H intersect {f<s}) |G| dA.

If U is nonzero, there are C_*,s0>0 with m_f(S2,s)>=C_*s^d for all 0<s<s0. Define Sigma_f to consist of the points having no open neighborhood H with m_f(H,s)=o(s^d). This is a nonempty closed subset of {f=0} intersect support(G). Almost every nonzero W arc has angular liminf distance zero to Sigma_f at both terminal ends.

Under the additional nodal premise

    {k=0} subset {W=0},                             (2)

Sigma_(f_k) is contained in Z_V={w:V(w)=0}. A point of Z_V where grad_T K is differentiable with invertible derivative is not in Sigma_(f_k). Thus V nowhere zero, or the assertion that every point of Z_V has this nondegeneracy, excludes a nonzero profile under(1)-(2). No such nondegeneracy is automatic from(1).

## 2. The general stopped-flow bound

A209-A210 give a volume-preserving C1 diffeomorphism Xi from the complement of a compact null core onto D, with W(Xi y)=D Xi(y)curl U(y). Conjugating the complete C1 original vorticity flow on intervals avoiding the core gives a unique C1 partial flow F_t on the open domain D_t={z:t<t_+(z)}, with determinant1. A360 says almost every initial point with W!=0 has finite lifetimes and tends to0 at both ends. These precise assertions, including lifetime measurability, were checked again in the complete A705-A708 proof. They are extra actual-profile information.

If U!=0 then W!=0; otherwise invertibility of D Xi, continuity across the null core, and harmonic Liouville give U=0. Choose a positive-volume measurable set B in {1<|z|<2,W!=0} with t_+(z)<=T<infinity and F_tz->0 for every z in B. Such a set exists by countable selection of the finite lifetimes. Put M=1+max_(1<=|z|<=2) f(z), so every surviving point of every curve from B has f<M.

Let chi_epsilon be1 inside radius epsilon,0 outside radius2epsilon, and have gradient norm at most C_chi/epsilon. For epsilon<1/4, the fundamental theorem strictly before arrival gives

    1<=integral_0^(t_+(z)) |grad chi_epsilon(F_tz)| |W(F_tz)| dt.

Tonelli on B times[0,T], followed at each time by the injective determinant1 map on B intersect D_t, gives

    |B|<=(C_chi T/epsilon)
          integral_(epsilon<|y|<2epsilon, f(y)<M)|W(y)|dy.       (3)

No map after arrival is used. The flow domain is open in time and space, and its inverse is a C1 local diffeomorphism, so all nonnegative integrals and measurable changes of variables are legitimate.

Twisted polar measure is r^2 dr dA, |W|=r^(-p-1)|G|, and f(y)<M implies f(pi y)<Mr<=2M epsilon. Consequently

    |B|<=C0 T epsilon^(-d) m_f(S2,2M epsilon),
    C0=C_chi integral_1^2 u^(1-p)du>0.               (4)

Put s=2M epsilon. The claimed lower bound holds with C_*=|B|/[C0 T(2M)^d] and, for example, s0=M/2. Dependence of these constants on the actual profile and on f is allowed.

## 3. k, joint scalars, and integrability criteria

The complete A702 proof gives k in C1 and grad k=Ax cross W-aV. Helicity zero makes W.grad k=0 pointwise, hence k is constant on every curve. The actual S is locally Lipschitz, and A531's uniform mollification argument makes it constant on every curve as well. Their twisted degrees are -d and -2p. This proves the asserted examples of admissible f, without a rank relation.

For f=f_k, (4) becomes

    integral_(|K|<tau)|G| dA>=C tau.

For f=f_* it becomes

    integral_(|K|<tau, |h|<tau^q)|G| dA>=C tau.       (5)

If G=0 almost everywhere on {f=0} and H=|G|f^(-d) is integrable on {f>0}, then

    m_f(S2,s)<=s^d integral_(0<f<s) H dA=o(s^d),

by dominated convergence. This contradicts(4). In particular either of the following sufficient conditions gives U=0 under(1):

    G=0 a.e. on {K=0}, integral_(K!=0)|G|/|K|<infinity;
    G=0 a.e. on {K=h=0},
    integral_(f_*>0)|G|min(|K|^(-1),|h|^(-eta))<infinity.       (6)

In the second line the minimum is f_*^(-d), with the usual extended positive reciprocals when just one scalar is zero; it is only integrated off their common zero set. This convention avoids an undefined product at simultaneous zeros. The joint condition is weaker than the k-only condition. On a vortical component where h=C_j|K|^q, its weight is |K|^(-1)min(1,|C_j|^(-eta)), so C_j tending to0 creates no additional factor. No assertion that these finite moments follow from(1) is made.

## 4. Local concentration and both terminal directions

The complement of Sigma_f is open by its definition. At f(w)>0, continuity supplies a neighborhood containing no sufficiently small sublevel set. Outside support(G), its mass is zero. Thus Sigma_f is closed and contained in the stated intersection. If empty, a finite cover by neighborhoods of o(s^d) mass contradicts(4). Every compact H disjoint from Sigma_f likewise has m_f(H,s)=o(s^d), by a finite cover.

We give the terminal argument with its selection details. Fix such a compact H. Suppose a positive-volume set of good initial points in the annulus eventually has pi(F_tz) in H for all times close enough to t_+(z). The relevant sets are measurable: t_+ is measurable, the partial flow is continuous, and membership in closed H for every time in a variable open interval can be tested at a countable dense set of times measured backwards from t_+. The radial minima on compact preterminal segments are measurable by the same rational approximation.

A countable selection therefore gives a positive-volume subset B' and numbers T,tau0,rho0>0 such that t_+<=T, the last min(tau0,t_+) units of the trajectory lie angularly in H, and the radius on [0,t1(z)] is at least rho0, where t1(z)=max(0,t_+(z)-tau0). Such a positive minimum exists separately for each initial point because that segment is compact in D. At t1=0 the initial radius is already positive. Endpoints of intervals, if needed, are recovered by continuity and closedness of H.

For epsilon<rho0/2, chi_epsilon is0 at t1 and becomes1 before t_+. Its variation on [t1,t_+) is at least1. Integrate as in Section2, restricting to the measurable condition t>=t1(z). At fixed t this only restricts the subset of the same injective partial-flow domain. All relevant images have f<M and angular coordinate in H. Hence

    |B'|<=C0 T epsilon^(-d) m_f(H,2M epsilon)->0,

a contradiction. If liminf angular distance to Sigma_f were positive, the curve would eventually lie in the compact set H_n={distance to Sigma_f>=1/n} for some n. The countable union of these null sets is null. Reversing the partial flow gives the backward result, using the other finite endpoint of A360. The same proof can be applied on each fixed annulus with its own finite M; a countable annular cover proves the assertion on all D.

The conclusion is liminf distance zero. It does not say every angular accumulation point is in Sigma_f, or that the angular limit exists. The weaker common-zero set in A702 does have a distance-to-zero conclusion; those are different statements.

## 5. Regular k nodes cannot carry the necessary mass

Assume(2). Let w0 have V(w0)!=0. If K(w0)!=0 then w0 is already outside Sigma_(f_k). If K(w0)=0, (2) gives W(w0)=0 and therefore grad k(w0)=-aV(w0)!=0. Homogeneity also gives grad k(w0).Aw0=-a k(w0)=0. A nonzero purely radial grad k=ell w0 would instead have this scalar product ell c, so the tangential gradient of K is nonzero.

The C1 implicit-function theorem provides a small chart in which K is a coordinate, with uniformly bounded area Jacobian on its closure. Thus the area of {|K|<tau} in a smaller chart is at most C tau. By continuity of G and its zero value at every K node, the supremum of |G| over this sublevel portion tends to0. For rigor choose nested chart closures; any violating sequence has a limit in the larger compact chart with K=0, contradicting continuity. The local weighted mass is o(tau), hence o(s^d) for tau=s^d. This excludes w0 from Sigma_(f_k).

We have proved Sigma_(f_k) subset Z_V. At any point of Z_V, k=0 and(2) gives W=0; twisted homogeneity propagates both zeros along its entire twisted ray. The set Sigma_(f_k) is nonempty for U!=0, so a stagnation ray is necessary. No premise about S, its sign, its order, or exterior vorticity density is used in this step.

## 6. Nondegenerate critical points at the available regularity

Assume(2), let w0 in Z_V, and assume grad_T K is differentiable at w0 with invertible derivative. Since grad k=-aV+Ax cross W, both terms vanish at w0. Work in a smooth local chart centered there and write x=0 for w0, rho=|x|, Z={K=0}, delta=distance to Z. Chart metric factors are uniformly comparable and only change constants.

There is a symmetric invertible matrix H with

    grad K(x)=Hx+o(|x|),
    K(x)=one half x.Hx+o(|x|^2).                    (7)

Symmetry follows from K being C1 and its gradient differentiable at0, for example by applying the zero circulation identity of grad K to small rectangles and dividing by their area. Invertibility gives |grad K(x)|>=c1 rho near0.

First, |K(x)|>=c2 rho delta. If |K(x)|>=c1 rho^2/4, use delta<=rho since0 is a node. Otherwise follow a unit-speed descending gradient curve for |K|, whose continuous vector field has a Peano solution off Z. Until it reaches Z or leaves rho/2<=|x'|<=3rho/2, the decrease rate is at least c1 rho/2. It must reach zero within length2|K(x)|/(c1 rho)<rho/2; it cannot leave the annulus first because its speed is1. Continuation on the compact annulus is legitimate until the first zero. This proves the lower bound, with harmless chart constants. Uniqueness of this auxiliary gradient curve is unnecessary.

Second, a dyadic annulus of radius R has a nodal delta-tube of area at most C R sigma for 0<sigma<=R, uniformly at small R. To see this, (7) makes R^(-2)K(R xi) converge in C1 on 1/4<=|xi|<=2 to the nondegenerate quadratic form. If that form is definite, there are no zeros there for small R. If indefinite, its zeros have four angular branches and its angular derivative stays nonzero on narrow neighborhoods of each branch. For each fixed rescaled radius, monotonicity in angle gives exactly one root in each such neighborhood, with bounded radial derivative by the C1 implicit-function theorem. The four graphs have uniformly bounded length and slope. Their tubes have area at most C times their width. Using the enlarged annulus treats nearby zeros just outside the original annulus. For sigma comparable to R, the elementary area bound C R^2 suffices. This proves the asserted uniform tube estimate without a C2 neighborhood assumption or an unproved global Morse lemma.

By actual tail regularity A538, G is Holder continuous with each exponent alpha in(0,1). Premise(2) gives G=0 on Z, so |G|<=L delta^alpha locally. On {|K|<tau} in a dyadic annulus of radius R, the first bound gives delta<=C tau/R. For R>=C' sqrt(tau), the tube estimate and this Holder bound give mass at most

    C R(tau/R)(tau/R)^alpha
        =C tau^(1+alpha)R^(-alpha).

The sum over those dyadic annuli is at most C tau^(1+alpha/2). The remaining inner disk has area O(tau) and |G|<=L rho^alpha=O(tau^(alpha/2)), so gives the same bound. Thus in a fixed neighborhood of w0,

    integral_(|K|<tau)|G| dA=O(tau^(1+alpha/2))=o(tau).          (8)

This excludes w0 from Sigma_(f_k). Only differentiability of the gradient at the point, not a continuous Hessian nearby, was used. It is nevertheless an additional premise not supplied by C^(1,alpha) regularity of V.

## 7. Limits, tests, and the continuing model comparison

A regular node with nonzero G can have mass of order tau, so without(2) this method does not exclude it. The scalar tests K=x and constant G, or K=x^2 with G=|x| on a rectangle of unit tangential length, give respectively2 tau and tau for the sublevel mass; doubling the tangential length gives2 tau in the second test. They are kinematic mass tests, not actual Euler profiles. A degenerate critical curve can therefore meet the required order. Neither flat nodes nor arbitrary critical curves are classified by(8).

All arguments concern actual profiles in(1), through the finite-time core-return theorem. No density, A2, rank extension, angular truncation or small-rotation argument is hidden in them. Global zero helicity and the derivative premise remain. The general conjecture stays open.

The full CO43 source is archived in verification. It is an actual mathematical continuation by the coordinator configured as the primary model of the previously requested A705-A708 comparison, with explicit use of its determinant1 partial domains, finite lifetimes and critical shell exponent. I independently checked the extension, including both terminal directions and the low-regularity local estimate. This counts as received collaboration, unlike a pending or failed nested request; it is not an independent attestation of provider runtime. No new client, agent, numerical job or formal build was used.
