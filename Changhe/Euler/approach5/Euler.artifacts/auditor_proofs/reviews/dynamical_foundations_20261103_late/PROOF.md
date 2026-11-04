# Repeated audit of entropy, regular basins and vortical limit-set saddles

Status: independent repeated verification of the statements below. The complete D4-D6 report excerpt was read. This is not a new unrestricted nonexistence theorem or a fresh certification of every external source.

## 1. Hypotheses, notation and basic identities

Fix 0<c<1/2 and finite real omega. Let Jx=(-x2,x1,0), A=cI-omega J, U in C2(R3;R3), P in C1(R3), and assume

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U(x)=o(|x|) uniformly at infinity.

Set B=Ax+U, Omega=curl U, a=1-2c>0 and kappa=1+c. Write phi_s for the B flow, psi_t=phi_-t and sigma=i_Omega vol. The profile equation makes grad P continuously differentiable, hence P is C2. Direct differentiation gives div B=3c, [B,Omega]=-kappa Omega, Dphi_s Omega=e^(kappa s)Omega composed phi_s, and phi_s^*sigma=e^(-as)sigma. The one-form law is

    L_B(U.dx)=-a U.dx+d(|U|^2/2-P).

No normalization of P is used. Uniform sublinearity gives |B|<=C(1+|x|), so both directions of phi are complete. For a sufficiently large closed ball D, B.x>=c|x|^2/2 outside D. Thus D traps psi, every compact set enters its interior in a uniform finite time, and Lambda=intersection_(t>=0)psi_t D is compact and invariant. Since |psi_t D|=exp(-3ct)|D|, Lambda is null. These facts use no bound on Omega at infinity and no restriction on omega.

The exact report pin is 02ab05b9f08a856c0d5f9382b24260599257c1b564dd92811836ecf979d4d8da. All 37146 characters of its D4-D6 excerpt were read, together with D0 and the earlier survivor-disk correction. The present proof restates the checked arguments and their dependency boundaries.

## 2. Circulation growth and entropy of the compact core

Assume in addition U is Cr, with integer r>=2, and is nonconstant. If Omega vanished everywhere, each component of U would be harmonic. Interior harmonic gradient estimates on balls of radius R, together with uniform o(R) growth, force DU=0 by letting R tend to infinity. Thus Omega is nonzero somewhere. Stokes' theorem on a small disk normal to that vorticity gives a closed smooth curve of nonzero circulation Gamma. The one-form law gives circulation exp(at)Gamma under psi_t. Move the entire curve into D by a fixed time T. With M=max_D|U|>0, its length at integer time n is at least |Gamma|exp(a(T+n))/M.

Choose a smooth cutoff chi equal to one on a larger ball and zero outside twice that ball, and replace B by B'=Ax+chi U. The radial outward estimate remains valid because |chi U|<=|U|. In the inversion chart z=x/|x|^2, Ax becomes (A-2cI)z=-(cI+omega J)z. Hence B' extends to a Cr field on S3 and its time-minus-one map F' is a Cr diffeomorphism. It agrees with psi_1 on D.

Every finite point enters D under F'. For each invariant probability nu, the nested inverse images of D exhaust S3 minus infinity and the nested forward images intersect in Lambda. Invariance and continuity of measures give nu(Lambda)=1-nu({infinity}). The variational principle, with entropy affinity for this two-set invariant decomposition, gives h_top(F')=h_top(psi_1|Lambda). Inverting the homeomorphism on Lambda leaves its topological entropy unchanged.

The external Yomdin volume-growth theorem, in the precise curve version previously checked against Gromov, bounds the exponential growth of this one curve by h_top(F')+R(F')/r, where R(F')=lim_n n^-1 log max(1,sup|D(F'^n)|). Subadditivity gives the limit. Therefore

    a<=h_top(phi_1|Lambda)+R(F')/r.

For smooth U the same cutoff and curve work for every r; R(F') is fixed and finite. Letting r tend to infinity gives h_top(phi_1|Lambda)>=a. Nonconstant is essential: nonzero constant sublinear profiles are not covered by this conclusion.

## 3. No loss term when vorticity is nonzero on the core

For C2 U, assume Omega is nowhere zero on Lambda. Nested compact convergence gives an iterate K=psi_N D with a neighbourhood on which Omega is nowhere zero. K has nonempty interior, is forward invariant under F=psi_1, and its invariant core is Lambda.

Cover K by finitely many C1 flow boxes of Omega, with uniformly smaller boxes. Choose constants so a sufficiently short plaque arc from a smaller box remains in its larger box and any two nearby points on one plaque have a joining plaque arc of length at most C times their distance. Choose a small transverse disk S in the interior of K, meeting each plaque in its fixed box at most once. Orient it so A0=integral_S sigma>0. Then integral_(F^n S) sigma=exp(an)A0.

Fix a small Bowen radius delta and consider E=S intersected with one Bowen ball for times 0 through n. The terminal points F^n(E) lie in a common smaller box. Its transverse plaque projection is injective on F^n(E): two points on one terminal plaque can be joined by a short plaque arc, pulled back by F^-1, and replaced by a short plaque arc in the preceding box. A uniform bound on DF^-1 and sufficiently small delta keep each pulled-back arc in that preceding larger box. At time zero choose the fixed box of S. Its one-point intersection property then makes the two initial points equal.

F preserves the kernel line of sigma. On each larger box sigma=g(q,z)dq1 wedge dq2, with g bounded, and each F^n S remains transverse. Injectivity on F^n(E) bounds its positive sigma integral by one constant M, independent of n and the Bowen ball. A cover of K by r_(n+1)(K,delta) such balls therefore gives exp(an)A0<=M r_(n+1). It follows that h_top(F|K)>=a. Every invariant probability on K is carried by Lambda, so the variational principle gives h_top(F|Lambda)>=a. No assumption of global bounded vorticity is used.

## 4. Regular invariant sets and the trichotomy

For every x,s,v, the determinant identity gives

    (B cross Omega)(phi_s x).Dphi_s v
      =exp(-as)(B cross Omega)(x).v.

Indeed B transports with Dphi_s, Omega transports with exp(-kappa s)Dphi_s, and det Dphi_s=exp(3cs). On a compact invariant set K where B, Omega and B cross Omega are nonzero, their norms and angles are uniformly controlled. The plane Ecu=span(B,Omega) is invariant. In its uniformly controlled frame, Dphi_s(u B+v Omega)=u B(phi_s x)+v exp(kappa s)Omega(phi_s x), so its norm is bounded below by C^-1|u B+v Omega| for s>=0. Its quotient contracts at rate a by the displayed covector law. The dominated-complement graph-transform theorem gives an invariant complementary stable line with rate -a. The other lines have exponents zero and kappa, respectively. Thus the backward flow has rates a, zero and -kappa.

If Omega(x)=lambda B(x) with lambda nonzero on a bounded full orbit, then Omega(phi_s x)=lambda exp(-kappa s)B(phi_s x). Its forward limit meets {Omega=0}; read backward, its backward limit meets {B=0}. Hence every vortical point has a backward limit set which is either entirely regular, contains a zero of B, or contains a zero of Omega. The cases need not be disjoint. This conclusion itself does not exclude any of the three alternatives.

## 5. Completeness of vortex lines and attracting regular sets

The vorticity flow chi_tau is complete even though Omega need not be bounded globally. For initial points in a fixed compact set, all psi_s images for s>=0 lie in one compact ball. On a slightly larger ball the C1 field Omega has a uniform local existence time delta. For |tau|<=delta exp(kappa s), define

    z_s(tau)=phi_s(chi_(exp(-kappa s)tau)(psi_s x)).

The Cauchy law gives z_s'=Omega(z_s), z_s(0)=x. Uniqueness makes these curves agree on overlaps, and their domains exhaust the whole real tau axis. Thus chi is complete and psi_t chi_tau=chi_(exp(-kappa t)tau)psi_t. Every compact vortex segment consequently contracts in distance at rate exp(-kappa t), after putting the whole segment in a backward-trapping ball. On a regular compact hyperbolic set these curves are precisely the global strong-stable leaves of psi, by the local stable manifold theorem and uniqueness.

Let G be a nonempty compact invariant regular set containing the local strong-unstable leaf through each of its points. At x in G, the map (s,r,tau) mapping to chi_tau(psi_s gamma_x(r)), where gamma_x parametrizes that unstable leaf, has three independent derivative columns. The inverse function theorem gives an open neighbourhood whose points lie on short vortex segments through G. A finite cover makes their lengths uniformly bounded. The exact contraction just proved gives dist(psi_t z,G)<=C exp(-kappa t) on that neighbourhood. A smaller distance neighbourhood N satisfies psi_t closure(N) subset N for every sufficiently large t, and intersection_(t>=0)psi_t closure(N)=G. The basin is open and G is locally maximal.

## 6. Minimal regular attractors and coverage

The closure of a weak-unstable leaf contained in a compact regular hyperbolic set is unstable-saturated, by continuous dependence of local unstable leaves. Intersections of chains of nonempty compact invariant saturated subsets remain nonempty and saturated. A minimal such subset A therefore equals the closure of the weak-unstable leaf through each of its points. It is attracting by Section 5.

This minimality gives transitivity at arbitrarily large times. Fix relative open sets V1,V2 meeting A. For each y in A there are s_y in R and an integer n_y>=0 for which psi_(s_y+n_y) Wloc^u(psi_-n_y y) meets V2. Choose an interior intersection; continuous dependence preserves it for every y' in a relative neighbourhood N_y. Take a finite cover N_(y_i), and let nstar=max n_i and sstar=max |s_i|. Choose x in V1 intersect A and a small unstable interval I through x contained in V1 intersect A. Uniform expansion gives Wloc^u(psi_t x) subset psi_t I for every t>=t0. Given T0, take t>=t0+nstar+sstar+T0 and choose i with psi_t x in N_(y_i). Then psi_(s_i+n_i) Wloc^u(psi_(t-n_i)x) lies in psi_(t+s_i)I and meets V2, while t+s_i>=T0. This proves the asserted transitivity. Applying it to a countable base and every integer lower time bound, Baire's theorem gives a residual set of points with forward psi limit A. The hyperbolic closing theorem applies because A is locally maximal, nonsingular and nonwandering; periodic orbits are dense. A contains a two-dimensional weak-unstable leaf, so it is not a single orbit.

Two such attractors with intersecting basins are equal. A common basin point has a nonempty limit set in their intersection. A dense-limit orbit in either attractor then enters the other's open basin, proving each inclusion. Thus the basins are pairwise disjoint and there are only countably many of them.

For coverage, suppose a positive-measure set of regular backward-limit points is outside all these basins. By countable uniform lower bounds on |Omega| and |B cross Omega|, eventual trapping, and inner regularity of measure, choose a compact positive-measure survivor E whose future psi orbit stays in one fixed compact regular region. Its forward-orbit closure C is compact, forward invariant and of positive measure. Its full invariant core K is regular hyperbolic.

Choose a time T large enough for strict domination and inverse unstable contraction on K. Extend the continuous splitting to a neighbourhood and replace C by psi_(mT)C inside it. The extension is required to be invariant only on K. Its inverse unstable norm stays uniformly below one along every orbit of the new C, so the nonuniform expansion condition holds everywhere there. These are exactly the hypotheses of Alves-Pinheiro Theorem A on printed pages 3-4, reread in this audit. It yields a local unstable interval I contained in K, not directly a whole leaf.

Choose p in the interior of I and a subsequence f^(n_j)p tending to q in K, with f=psi_T. For each fixed m, the images f^(n_j-m)I have both intrinsic endpoint distances tending to infinity. They contain a uniform local unstable interval about f^(n_j-m)p. Taking limits gives Wloc^u(f^-m q) subset K for every m>=0. Apply f^m and take the union, then flow-saturate, to obtain a full weak-unstable leaf in K. Its closure contains a minimal attractor A as above. Since A lies in the closure of the forward orbit of E, its open basin meets that orbit, contradicting the choice of E. This proves almost-everywhere coverage of the regular alternative only.

The basin of A is exactly the union of the complete vortex lines through A, by the local representation in Section 5 and transport of chi. It contains no zero of B, Omega or B cross Omega, because those closed sets are invariant and disjoint from A. Its volume is infinite: it is nonempty, open and fully invariant, while phi_s scales volume by exp(3cs). The compact invariant A itself has zero volume.

## 7. Regular plaques and attractor entropy

A compact regular invariant set L cannot contain a two-dimensional plaque generated by B and Omega. If it did, the continuous family of local forward-stable curves through that plaque would form an injective local product. Invariance of domain would give an open set all of whose forward B orbits are bounded. This lies in Lambda, contrary to its zero volume. Here one uses local product structure on the regular hyperbolic set, not a global smooth stable foliation.

For a basic backward attractor A, the covector law gives the exact unstable Jacobian

    Ju_t(x)=exp(at)g(x)/g(psi_t x),

where g is the absolute value of B cross Omega on a unit unstable vector. It is continuous and bounded above and below away from zero. Hence the geometric unstable potential integrates to -a for every invariant probability. The external Bowen-Ruelle zero-pressure theorem for a C2 basic attracting flow and the variational principle give h_top(psi_1|A)=a. This uses the individual attractor theorem; it is not inferred from a lower bound for entropy of the whole core.

## 8. Vortical nonsingleton limit sets and the entrance argument

Let K be a nonsingleton backward limit set, with Omega nowhere zero on K, and p in K satisfy B(p)=0. At every regular point of K, B and Omega are independent: dependence would force Omega to tend to zero along a full orbit in K, by Section 4, contradicting its positive minimum. The complete vortex line through p satisfies

    phi_s chi_tau p=chi_(exp(kappa s)tau)p,
    B(chi_tau p)=kappa tau Omega(chi_tau p).

It therefore meets K only at p. This statement is about the entire vortex line.

At p the eigenvalue kappa has eigenvector Omega(p); the other two eigenvalues sum to 2c-1=-a. If both had negative real parts, Y=-B would have a hyperbolic equilibrium with one-dimensional stable manifold equal to the vortex line through p. Its stable manifold would meet K only at p.

The following entrance argument rules this out for a nonsingleton omega-limit set of a precompact Y orbit. Choose a small closed ball about p such that K has a point outside the ball and every forward orbit remaining in the ball lies in the local stable manifold. There are arbitrarily late visits near p preceded by arbitrarily late visits outside the ball. Take the last boundary entrance s_n before a visit t_n with x(t_n)->p. A local Lipschitz estimate gives |x(t_n)-p|>=R exp(-L(t_n-s_n)), so t_n-s_n tends to infinity. A convergent subsequence of boundary points x(s_n) tends to z in K distinct from p. Continuous dependence shows the entire forward orbit of z stays in the ball. Thus z is in the stable manifold, a contradiction.

Consequently at least one remaining eigenvalue has nonnegative real part. A nonreal conjugate pair would have both real parts -a/2<0, so both eigenvalues are real. They can be written lambda3<0<=lambda2, with lambda2+lambda3=-a. The backward unstable rate is -lambda3=lambda2+a. No upper bound lambda2<kappa is proved, and lambda2=0 is allowed. The hypothesis that K is an actual nonsingleton limit set is indispensable to the entrance argument; an arbitrary compact invariant set does not supply its late entrances.

## 9. External dependencies, comparison and limits

The retained primary Alves-Pinheiro statement was reread in full at its precise hypotheses: positive invariance of C, a continuous splitting on C invariant and dominated only on its full invariant core, and nonuniform expansion on a positive-volume subset. Thus no contraction of the neutral center direction was assumed. The complete earlier correction Section 6 was also reread. The Yomdin, graph-transform, invariant-manifold, hyperbolic closing and Bowen-Ruelle inputs retain their previously checked scopes; this pass does not claim a new complete reading of those books or papers.

The report is the existing theory-agent argument, repeatedly compared with the independent corrections. A fresh companion-agent recheck requested by the coordinator remains useful but is not substituted for a proof here. Existing configured model file collaboration continues; actual provider execution is not independently attested.

No conclusion here supplies decay at a prescribed rate, a pressure boundary limit, the exclusion of singular or zero-vorticity backward limits, or a proof of unrestricted rotating Euler nonexistence. The cited kinematic realizations and finite-network theorem in the report's remarks were read as citations only, not independently reconstructed again in this pass. The report's self-contained wording remains subject to its explicit external-source qualification.
