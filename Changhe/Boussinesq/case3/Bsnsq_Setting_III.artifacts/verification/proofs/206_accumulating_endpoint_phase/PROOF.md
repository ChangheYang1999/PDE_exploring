# Accumulating equilibria: a trapped neighborhood and a harmonic side

Status: CONFIRMED as the local conditional theorem stated below. The argument is written before executable controls. This is a local necessary-condition theorem, not a construction or exclusion of all smooth B2 profiles. The source consultation and any later candidate wording have separate version-specific audits.

## 1. Statement, coordinates and scope

Let W be C3 on a neighborhood of p=0 in an oriented orthonormal coordinate system (s,z), with W(0)=0 and DW(0)=diag(0,4). Let Theta and Omega be C1 and satisfy

 div W=4, Omega=-curl W,
 W.grad Theta=0, W.grad Omega+Omega=Theta_x.                 (1)

The derivative in the last equation is in the fixed physical horizontal direction, expressed in the (s,z) coordinates if necessary. It is not silently replaced by partial_s. Let k be the unique local nullcline W_z(s,k(s))=0, and f(s)=W_s(s,k(s)). The implicit function theorem gives k(0)=k'(0)=0. Assume f=0 on a negative interval ending at0, and that positive zeros of f accumulate at0. Assume also the endpoint condition

 for every sufficiently small d>0, f is not identically0 on(0,d). (NE)

The accumulating case alone implies the following trapping statement. There are arbitrarily small open neighborhoods U of0 such that every reversed-time trajectory from U stays in U for all positive time and in a compact subset of the original coordinate neighborhood. This assertion does not require the positive zero set to have empty interior.

For the main conclusion suppose additionally that the relatively closed set

 F={s in(0,eps): f(s)=0}

has empty interior. Then the local strong unstable curve of W through0 is a C3 graph C={s=sigma(z)}, with sigma(0)=sigma'(0)=0, and there is a disk N about0 on whose entire side

 N_plus=N intersect {s>sigma(z)}

one has Theta=Theta(0)=L and Omega=0. Consequently W is harmonic there. In particular, each positive zero of f sufficiently near0 is isolated among positive zeros, although accumulation at0 itself is not excluded.

For the later analytic consequences assume all fields smooth. Under accumulating zeros and(NE), Theta-L cannot vanish on any neighborhood of0, even without the empty-interior hypothesis. With empty interior it also cannot vanish on a terminal negative subarc. The harmonic-side obstruction and the continuation, directional Gevrey2, transverse-analyticity, strong-curve and finite-separated-representation exclusions described below follow. No global finite-zero or finite-tree theorem is claimed. General incoming endpoints with nonisolated exterior zeros remain open.

## 2. A small global extension used only to construct coordinates

Use reversed time t>=0, so the vector field is

 s'=P(s,z), z'=-4z+Q(s,z),
 (P,Q)(0)=0, D(P,Q)(0)=0.                                  (2)

Multiply the nonlinear terms by a smooth cutoff on a sufficiently small disk. The resulting N=(P,Q) is globally bounded, C3 with bounded derivatives, and has arbitrarily small global Lipschitz constant ell in the sum norm. Indeed on a disk of radius r its size is O(r^2), its first derivative is O(r), and differentiation of the cutoff contributes O(r^-1)O(r^2)=O(r). Choose ell<=10^-3, shrinking further when needed. The linear part and this bounded Lipschitz perturbation define a complete global flow. The extension agrees with(2) on a smaller original disk. Equations(1) are not asserted outside that disk.

We will construct a center graph and a continuous phase for this extension, then construct invariant neighborhoods whose closures lie entirely in the original disk. This last step is essential to apply(1).

## 3. Construction and regularity of the center graph

For alpha in {1/4,1/2,3/4}, let X_alpha be the space of continuous two-component histories on the whole real line with norm sup_t e^(-alpha|t|)|q(t)|_1. Define the linear integration operator

 (AF)_s(t)=integral_0^t F_s(r)dr,
 (AF)_z(t)=integral_-infinity^t exp[-4(t-r)] F_z(r)dr.

Its operator norm is at most a_alpha=1/alpha+1/(4-alpha). The first bound follows by integrating e^(alpha|r|) between0 and t; the second follows from |r|<=|t|+|t-r|. For each a in R solve

 q_a=(a,0)+A[N(q_a)].                                      (3)

The map is a contraction since ell a_alpha<1. It maps X_alpha to itself; boundedness of N makes the integrals finite and gives at most linear growth in the first component. Its unique fixed point exists for every a. The solutions in the three spaces coincide, since X_(1/4) is contained in the other two spaces and uniqueness applies. At alpha=1/4,

 ||q_a-q_b||_alpha <= |a-b|/(1-ell a_alpha).                  (4)

Put h(a)=(q_a)_z(0). The history solves(2), and a finite time translate belongs to X_alpha. It satisfies(3) with parameter equal to its first component at the translated time. Uniqueness therefore makes M={(a,h(a))} invariant. Every equilibrium belongs to M: its constant history satisfies(3), since at an equilibrium P=0 and Q=4z.

Here are explicit regularity details needed below. Products of histories in X_alpha and X_beta belong to X_(alpha+beta), with the product of norms as a bound. Let eta=1/4. The linearized equation

 v_a=(1,0)+A[DN(q_a)v_a]

has a unique solution in X_eta with a uniform norm bound. Taylor expansion with bounded D2N, together with(4), shows that q_(a+d)-q_a-d v_a has X_(2eta) norm O(d^2): move its linear term A DN(q_a) to the left and invert by the convergent Neumann series on X_(2eta). Differences of the equations for v_a and v_b then show ||v_a-v_b||_(2eta)=O(|a-b|), using the product estimate. Evaluation at t=0 proves h is C1 with h'(a)=(v_a)_z(0).

The equation

 u_a=A[DN(q_a)u_a+D2N(q_a)[v_a,v_a]]

has a unique solution in X_(2eta). A second difference-quotient argument, now using bounded D3N and products in X_(3eta), gives v_(a+d)-v_a-d u_a=o(d) in X_(3eta), and continuity of u_a in that space. For example, the variation in D2N contributes O(d)|v_a|^2|q_(a+d)-q_a|/|d| in the corresponding product norm, and every inverse I-A DN remains bounded at weight3eta. Thus h is C2. This sufficient proof does not require differentiability of a nonlinear substitution map on a single weighted space.

At a=0, q_0=0 and v_0=(1,0); hence h(0)=h'(0)=0 and h(a)=O(a^2). The z integral for v_a bounds |h'| by ell/[(4-eta)(1-ell a_eta)]. In particular h' is uniformly O(ell). Invariance gives

 h'(s)P(s,h(s))=-4h(s)+Q(s,h(s)).                            (5)

## 4. Exponential tracking with a continuous phase

Set v=z-h(s) and G(s)=P(s,h(s)). Subtract(5) from(2). The transformed equations are exactly

 s'=G(s)+A_1(s,v)v,
 v'=(-4+B_1(s,v))v,                                         (6)

where

 A_1(s,v)=integral_0^1 P_z(s,h(s)+uv)du,
 B_1(s,v)=integral_0^1 [Q_z-h'(s)P_z](s,h(s)+uv)du.

The bound on h' gives, after the preceding choice of ell, |G'|<=mu=1/10, |A_1|<=ell and 4-B_1>=lambda=7/2. Let psi_t denote the complete scalar flow of s'=G(s). Its positive-time derivative and that of its inverse obey

 e^(-mu t)|a-b| <= |psi_t(a)-psi_t(b)| <= e^(mu t)|a-b|,
 |v(t)|<=|v(0)|e^(-lambda t).                                (7)

For a trajectory Y(t), define b_t=psi_(-t)(s(t)). Differentiating the scalar flow identity yields

 b_t'=(partial_s psi_(-t))(s(t)) A_1(s(t),v(t))v(t).

Thus |b_t'|<=ell |v(0)|e^[-(lambda-mu)t], and b_t converges. Define pi(Y)=lim_t b_t. The convergence is uniform on bounded sets of initial points, so pi is continuous. Direct integration gives

 |pi(Y)-s(Y)| <= ell|v(Y)|/(lambda-mu).                       (8)

Shifting the time origin and passing to the limit through a fixed scalar flow gives

 pi(Phi_tY)=psi_t(pi(Y)),   pi(a,h(a))=a.                     (9)

Apply the upper Lipschitz bound in(7) to the tail of b_t and use the v estimate. With c=lambda-2mu=33/10,

 |s(t)-psi_t(pi(Y))|
   +|z(t)-h(psi_t(pi(Y)))| <= C |v(0)|e^(-ct).               (10)

The two errors are added. A product of them would not be the needed tracking estimate. Uniqueness of the tracking base follows from the lower bound in(7), because c>mu: two different scalar base points cannot approach one another as fast as the right side of(10).

## 5. Identifying the zero-phase fiber and the entire side

Construct the strong curve separately on t>=0, specifying z(0)=b and solving

 s(t)=-integral_t^infinity P(s(r),z(r))dr,
 z(t)=e^(-4t)b+integral_0^t e^[-4(t-r)]Q(s(r),z(r))dr.         (11)

In the norm sup_(t>=0)e^(3t)|q(t)|_1, the contraction constant is at most ell(1/3+1)<1. The fixed point has norm O(|b|). The same decaying-history space admits bounded first, second and third derivatives of the integral map: products of decaying histories only improve decay, and N has bounded derivatives. Differentiating the fixed-point equation and inverting the linear contraction therefore proves C3 dependence on b. At b=0 its derivative is (0,e^-4t), so the initial points form a C3 graph s=sigma(z), with sigma(0)=sigma'(0)=0. Time translation and uniqueness give local invariance.

For sufficiently small b this entire trajectory lies in the original disk. Since N(q)=O(|q|^2) there, its initial e^-3t decay gives s=O(e^-6t) and z=a_b e^-4t+O(e^-6t), where

 a_b=b+integral_0^infinity e^(4r) Q(q(r))dr=b+O(b^2).

Substitution then improves the remainders to O(e^-8t). This identifies the usual strong unstable curve of W.

If pi(Y)=0, estimate(10) gives decay faster than e^-3t. The first component tends to0 and the orbit satisfies(11), so it is on this curve. Conversely an orbit from(11) tracks the zero scalar orbit; uniqueness of tracking in(7),(10) makes its phase0. Hence pi^-1(0)=C locally.

Choose a small rectangle in which the whole local graph C divides the rectangle into the two connected sets s>sigma(z) and s<sigma(z). The continuous phase is nonzero on either set and therefore has a constant sign on each. On the center graph pi(a,h(a))=a, and sigma(h(a))=O(a^4). Small positive a belongs to the first side and small negative a to the second. Thus

 pi(Y)>0 if and only if s(Y)>sigma(z(Y))                     (12)

near0. This proves full-side identification, without assuming a differentiable foliation or an unjustified openness property of the phase.

## 6. Original-domain trapping by equilibrium barriers

Zeros of G and f coincide in the local s interval. If f(s)=0, the point(s,k(s)) is an equilibrium; it lies on M, so h(s)=k(s) and G(s)=0. Conversely G(s)=0 and invariance(5) give a full equilibrium; uniqueness of the nullcline yields h(s)=k(s) and f(s)=0.

Choose b<0 in the negative zero interval and a>0 a zero of f, both as close to0 as desired. The scalar interval[b,a] is invariant in both time directions, since its endpoints are equilibria and a scalar solution cannot cross an equilibrium by uniqueness. Fix small nu>0 and put

 U={Y: b<pi(Y)<a, |v(Y)|<nu}.                               (13)

This is an open neighborhood of0. Equations(7),(9) make it invariant for every positive reversed time. By(8), every Y in its closure satisfies b-Cnu<=s(Y)<=a+Cnu and |z(Y)-h(s(Y))|<=nu. Choosing a,|b|,nu small enough puts its closure in a fixed compact subset of the disk where the extension equals the original system. Thus all trajectories starting in U obey(1) for all reversed time. They stay in that compact subset. There is a disk N about0 contained in U and in the rectangle of(12).

The positive zeros are essential to this construction. A trajectory with positive scalar phase at an incoming endpoint has no such arbitrarily close positive barrier and exits a sufficiently small center interval in reversed time. Tracking after that exit for an artificial extension says nothing about the original equations.

## 7. Thermal factorization and harmonicity

Write theta(s)=Theta(s,h(s)). It is C1. On the invariant graph,(1) implies G theta'=0. On(0,a) minus F, theta'=0. Empty interior of the relatively closed F means its complement is dense, so continuity of theta' gives theta'=0 everywhere on(0,a). Therefore theta=L on[0,a]. This step would fail for a merely continuous theta: a Cantor function can be constant on complementary gaps and still be nonconstant. C1 regularity is used exactly here.

For Y in U, conservation along the original reversed flow gives Theta(Phi_tY)=Theta(Y), while G theta'=0 gives theta(psi_t pi(Y))=theta(pi(Y)). By(10) the two points at which Theta is evaluated approach each other, and both remain in a common compact subset of its domain. Uniform continuity yields the exact factorization

 Theta(Y)=theta(pi(Y)).                                     (14)

Consequently Theta=L on the open, reversed-invariant set U_plus=U intersect {pi>0}. Its physical derivative Theta_x vanishes there. The vorticity equation in reversed time is Omega'=Omega-Theta_x, hence Omega(Phi_tY)=e^t Omega(Y) on U_plus. Boundedness of Omega on the compact trapping set forces Omega(Y)=0. Equations(12) and(13) prove the asserted identities on all of N_plus. Harmonicity follows from constant divergence and zero curl. If initially W is only C3, these harmonic equations are classical and interior harmonic regularity gives real analyticity on N_plus.

For each small s>0 the nullcline point(s,k(s)) belongs to N_plus since k(s)=O(s^2) and sigma(k(s))=O(s^4)<s. The analytic implicit function theorem makes k and f analytic on a neighborhood of each such s. An accumulation of positive zeros at one positive s would force f to vanish on an interval, contrary to empty interior. Thus these positive zeros are locally discrete. This does not prohibit zeros approaching the boundary point0.

For completeness, each positive gap of F inside(0,a) has two positive equilibrium endpoints. There cannot be a gap with left endpoint0, because positive zeros accumulate at0. The scalar reversed trajectory is monotone in a gap and converges to one endpoint; at a zero it is stationary. Tracking gives the same limit for each full trajectory. An open-basin density theorem is unnecessary for(14) and the harmonic-side conclusion.

## 8. Smooth flatness and the obstruction to analytic continuation

Assume now smoothness. On the negative zero interval f vanishes, so it is flat at0. The following elementary jet argument needs(NE) but not empty interior. If Theta-L had first nonzero homogeneous term P_m, the thermal equation at degree m gives 4z partial_z P_m=0, hence P_m=c s^m, c nonzero. Because k(s)=O(s^2), partial_s Theta(s,k(s))=mc s^(m-1)+O(s^m), nonzero for every sufficiently small positive s. On that nullcline the thermal equation is f(s) partial_s Theta(s,k(s))=0. It would force f to vanish on an interval, violating(NE). Thus Theta-L is flat. The vorticity equation at0 gives Omega(0)=0; any first nonzero homogeneous term Q_m would satisfy(4z partial_z+1)Q_m=0, impossible since its monomial multipliers are4j+1>0. Thus Omega is flat as well.

If W were analytic on a full neighborhood of0, its analytic nullcline and reduced f would extend the negative zero interval to a positive one, violating(NE). In particular Omega cannot vanish on a full neighborhood, since div W=4 and curl W=0 would make W harmonic and analytic there.

More generally assume the harmonic-side conclusion of Section7. No real analytic field V on a neighborhood of0 can agree with W on that whole side. Agreement up to the boundary gives equal full jets. The analytic nullcline k_an of V_z has the same jet as k, and its reduced analytic f_an has the zero jet of f. Hence f_an is identically0 near0. The points(s,k_an(s)) for positive small s are in the side of agreement because sigma(k_an(s))=O(s^4)<s. Uniqueness of the original nullcline gives k_an=k there and f=0 on a positive interval, contradicting(NE). The contradiction requires an interval of zeros, not the absence of every individual positive zero.

## 9. Consequences and checked dependencies

First, the no-isothermal-neighborhood statement needs only accumulating zeros,(NE) and smoothness. If Theta=L on a neighborhood of0, choose the compact trapping neighborhood U from Section6 inside it. The vorticity ODE used in Section7 now gives Omega=0 on all of U. The preceding analytic contradiction applies. No empty-interior premise entered. Under empty interior, if Theta=L on a terminal negative subarc, choose b there. Section7 gives theta=L on the positive interval too, so(14) makes Theta=L on a full neighborhood, again impossible. These are statements about every sufficiently small terminal subarc, not arbitrary subarcs away from0.

The remaining consequences use the harmonic side proved here and the explicitly proved analytic lemmas in P199, P203 and P204. Their dependence on the endpoint type is as follows.

1. Positive-area analytic agreement. In a small rectangle the side s>sigma(z) is connected. Real analyticity and the elementary Fubini/one-variable identity argument show that a real analytic field agreeing with W on a subset of positive area in every neighborhood of0 agrees on the entire side. Section8 rules this out.

2. Directional Gevrey2. Put w=s+iz, K=W_s-iW_z+4iz, S=w-K/2 and R=conjugate(S). Then partial_wbar K=i Omega/2; S is holomorphic on the side, tangent to the identity at0 and formally holomorphic at0. The defect E=conjugate(S(conjugate(S(w))))-w equals S_star(S(w))-w and is holomorphic on a disk D_M={Re w>M|w|^2} inside the side, for sufficiently large M. Its jet is zero: on the negative zero arc R(w)=w, and restriction of any first nonzero holomorphic Taylor term of E to that arc would be nonzero. On kappa(s)=s+ik(s), the exact identity is

 E(kappa(s))=-f(s)/2 [1+integral_0^1 conjugate(S'(kappa(s)-t f(s)/2))dt]
              =-f(s)(1+O(s)).                              (15)

The horizontal segment is inside the side regardless of the sign of f: its real coordinate is s+o(s), while sigma(k(s))=O(s^4). Also kappa(s) belongs to D_M. Condition(NE), not nonvanishing for every s, supplies nonzero values of E arbitrarily close to0. The tangent-disk Gevrey2 uniqueness lemma proved completely in P203 applies without any change: derivative bounds imply |E(w)|<=C exp(-c/|w|); inversion takes D_M to a half-plane, where the submean inequality forces a holomorphic function with this uniform decay to be0. The composition estimates and the conversion of one fixed real direction to complex derivatives require only holomorphicity on these domains. Thus the directional W bound is excluded. The compact directional-Gevrey cutoff and Cauchy-transform argument of P203 then transfer a hypothetical directional Omega bound on a full disk to W and give the same contradiction. Orders greater than2 and bounds on just individual lines or narrower sectors remain unexcluded. This paragraph uses the full proofs in P203 Sections2-5 as dependencies, not a new unproved uniqueness assertion.

3. Transverse analyticity. If Omega(s,.) were real analytic on a fixed transverse interval for all sufficiently small s>0, the open interval of zeros supplied by the harmonic side at each s would extend to that full transverse interval. W is then harmonic on a right rectangle. An analytic trace of U on s=0 gives an analytic boundary trace of K. Subtract its holomorphic extension; Schwarz reflection of the zero boundary values extends K analytically across the diameter. The positive analytic nullcline lies inside that right rectangle, contradicting Section8. The physical affine addition from U to W is analytic and changes no trace hypothesis.

4. Analyticity of the strong curve. If sigma were analytic, use chi(t)=sigma(t)+it as a conformal coordinate and chi_star(zeta)=conjugate(chi(conjugate(zeta))). Tangency of W=2(w-R(w)) to C is equivalent to

 Im[chi'(t) S(chi(t))]=Im[chi'(t) conjugate(chi(t))].

Thus H(zeta)=chi'(zeta)[S(chi(zeta))-chi_star(zeta)] is holomorphic on the side and real on its boundary. Schwarz reflection extends H. Division by the nonzero chi' extends S and hence W analytically across C, contradicting Section8. Two analytic branches continuing through0 have equal jets because C is smooth, and would give one analytic germ. This proves the branch version also.

5. Finite separated representations. Under precisely the finite-rank, trace-continuity and C1-positive-s coefficient hypotheses of P199, choose finitely many positive s slices spanning the coefficient vectors. These slices are analytic in z on a common small interval, because each lies in the harmonic side there. Their finite combination reconstructs a field V on a right rectangle, with an analytic trace at s=0. For fixed positive s, div V-4 and curl V are analytic in z and vanish on an interval where V=W; thus both vanish throughout the interval. K_V is holomorphic, and reflection of its analytic trace extends it across s=0. It agrees with W on the original side, contradicting Section8. There is no assumption here that f has a fixed sign on all positive s.

Each dependency is local. None of these steps gives the global finite-zero, source-basin, finite-tree, support-direction or axis conclusions proved elsewhere under stronger outgoing/incoming hypotheses.

## 10. Audit notes and unresolved cases

The lead consultation's displayed tracking equation(17) omitted a plus between its two absolute values. Its following argument proves the sum estimate(10), which is used here. A continuous phase alone does not make the inverse image of a dense set dense. Our proof does not make that inference: it first proves the C1 center trace is constant using continuity of its derivative. There is no appeal to a center-manifold or invariant-foliation theorem without proof.

If empty interior is dropped, the positive center trace can vary on positive equilibrium intervals. The proof of a whole harmonic side above then fails. If accumulating positive zeros are dropped, the compact trapping neighborhood may fail, as at incoming endpoints. Neither failure is a counterexample satisfying(1), and neither licenses a general exclusion. No full-plane inverse or global B2 profile has been constructed by the local extension in Section2. No computation, formalization or model opinion substitutes for the arguments above.

## 11. Independent audit of the lead's barrier proof

Candidate work/enter_xx/text_v1.md gives a second proof, using a neighboring strong unstable curve instead of the phase factorization. Here is a standalone justification of its additional steps. Smoothness of the physical field permits a C5 center graph in Section3 by choosing eta small enough that6eta<4 and repeating its product-space differentiation up to order5. Only finitely many derivatives are needed. Straighten this graph and the transverse strong curve simultaneously by local coordinates u=s-sigma(z), v=z-h(s). The derivative at0 is the identity. Each curve becomes a coordinate axis, and the negative equilibrium half-arc is v=0,u<=0. The transformed field is at least C3. Factoring first by v and then by u gives the forward equations

 u'=g(u)+u v c(u,v), v'=v d(u,v), d>2,                      (16)

with c bounded and g=0 for u<=0. The positive coordinate on the center graph increases with the original s near0, so the positive zero set G of g accumulates at0 and has empty interior exactly when the original F does. The physical divergence4 is not generally the ordinary divergence of this nonlinear-coordinate field. At an equilibrium, however, its derivative is conjugate to the physical derivative, so its trace is4.

Fix a sufficiently small positive zero q1=(u1,0). Its coordinate derivative is upper triangular, with eigenvalues lambda=g'(u1), nu=4-lambda. Since g'(0)=0, arrange |lambda|<1 and hence nu>3. The eigenvector for nu has nonzero v component since lambda!=nu. To construct its strong unstable curve without any regularity ambiguity, return to the original smooth physical coordinates at q1. Write W(q1+h)=A h+N(h), with N=O(|h|^2), and let P_lambda,P_nu be the two fixed spectral projections. On t<=0 solve

 h(t)=r e^(nu t)e_nu
       +integral_-infinity^t [e^(lambda(t-y))P_lambda
                              +e^(nu(t-y))P_nu]N(h(y))dy.   (17)

In norm sup_(t<=0)e^(-nu t)|h(t)|, a quadratic bound has integral constants bounded by fixed multiples of1/(2nu-lambda) and1/nu. Both denominators are positive. On a small ball the map has Lipschitz constant O(radius), so it is a contraction. More explicitly, the linear integral operator maps histories of weight2nu into histories of weightnu, with those two denominators. It is not bounded from weightnu to itself. The quadratic substitution N maps a small ball of weightnu histories smoothly into weight2nu histories: its first derivative gains a factor from DN(h)=O(|h|), and its jth derivative for j>=2 gains j exponential factors, at least two. Uniform continuity of each D^jN on the compact physical ball proves continuity of these derivatives. Thus the contraction and its inverse I-DT give smooth dependence on r to every finite order in the original physical coordinates. Time translation gives h_r(t+a)=h_(r exp(nu a))(t) for a<=0. Invariance means negative invariance and forward invariance only while the orbit remains in the local curve neighborhood. The solution is h=r e^(nu t)e_nu+O(r^2e^(2nu t)); time-translation uniqueness gives a smooth locally invariant curve with backward limit q1 on both branches. Its image in the C4 chart is a C4 curve. Since its tangent has nonzero v component it is a graph u=sigma1(v), with sigma1(0)=u1. No all-order smoothness of a C3 transformed vector field is needed.

Shrink the graph interval to |v|<=rho1 so 0<sigma1(v)<2u1. It does not meet C: a common nonzero point would have both p and q1 as its unique backward limit; the equilibria cannot be common points either. Positivity also follows directly by continuity after shrinking, and m=min sigma1>0 on the closed interval. Consider

 R={0<u<sigma1(v), |v|<rho1}.                               (18)

The left and right graph edges are invariant orbit arcs, with the two equilibrium points included. A solution cannot cross either by uniqueness. On the top edge backward v'=-v d is strictly negative, and on the bottom it is strictly positive. At a corner the same sign moves inward from the horizontal edge while tangency preserves the graph edge. More formally, a finite first exit through a graph is excluded by uniqueness, and an exit through a horizontal edge is excluded by its strict inward derivative. Thus R and its compact closure remain in this local box under backward flow. Choose u1 first, then rho1, so its closure is in a prescribed original disk. It contains all positive-side points of a sufficiently small disk around p since it contains{0<u<m,|v|<rho1}. This gives the asserted full-side trapping.

An elementary local scalar argument proves the needed limit statement without a global planar-limit-set theorem. On every such backward trajectory, |v(t)|<=rho1 e^-2t and u(t) is bounded. Its scalar limit set is the interval[liminf u,limsup u], and it lies in[0,u1] since sigma1(v(t)) tends to u1. If g(a)!=0 at a limit point, choose a small interval around a where g has a fixed sign and |g|>=k>0. For large t the perturbation uvc has magnitude below k/2, so the backward u derivative has a fixed sign and magnitude at least k/2 whenever u is in that interval. A trajectory cannot converge to a there. Nor can it revisit the interval infinitely often: every passage has the same orientation, and returning from the exit side to the entry side would require an opposite passage. The endpoint cases use the same one-sided passage argument. Thus every limit point is a zero of g. If G contains no interval, a connected subset of{0} union G in[0,u1] is a singleton. Since v tends to0, the full trajectory converges to one equilibrium.

The thermal trace on v=0 is C1 and satisfies g partial_u Theta=0; density of the complement of G and continuity of that derivative make it constant=L on[0,u1]. Transport and the just-proved convergence give Theta=L on R. The vorticity ODE and compactness give Omega=0 there. This proves the candidate's(b) by an independent route. The no-isothermal-neighborhood argument(a) uses the same R without empty interior: assuming Theta=L on a disk already gives Omega=0 on R. On u<0, g=0 and backward log|u| changes by at most sup|c| |v(0)|/2, so all orbits from a sufficiently small negative-side box stay in the original disk and converge to negative points on gamma. Under that isothermal assumption they too have Omega=0. Continuity fills u=0, giving a full harmonic neighborhood and contradicting(NE).

These steps justify the barrier construction with the regularity understood in physical coordinates. The candidate's reference to constant-divergence planar limit sets can be replaced by the local scalar argument above. The transformation is used to study orbits, not to replace the physical derivative Theta_x or the physical divergence by coordinate partial derivatives.

## 12. Manufactured controls and their limits

For algebraic controls take a smooth scalar g and the physical field W0=(g(s),(4-g'(s))z). Its physical divergence is4. Its vorticity is Omega0=g''(s)z. With Theta0=0, its vorticity equation has residual

 z[g(s)g'''(s)+(5-g'(s))g''(s)].                              (19)

This is generally nonzero; the controls are kinematic fields, not solutions of(1).

Use the nonlinear chart u=s exp(a z), v=z. Its derivative is nonsingular and its Jacobian is exp(a z). The pushed-forward field is

 A(u,v)=exp(a v)g(u exp(-a v))
          +a u v[4-g'(u exp(-a v))],
 B(u,v)=v[4-g'(u exp(-a v))].                                (20)

Its ordinary coordinate divergence is4+a v[4-g'(u exp(-a v))], generally not4. At q=(q,0) with g(q)=0, however, the derivative has trace4, eigenvalues lambda=g'(q),nu=4-lambda, and fast eigenvector(aq,1). The curve u=q exp(a v) is exactly invariant and has this tangent. Its backward trajectory is v(t)=v0 exp(-nu t),u(t)=q exp(a v(t)). Together with the invariant curve u=0 when g(0)=0, it bounds the finite strip of Section11 whenever the base scalar interval[0,q] has equilibrium endpoints.

The explicit polynomial g(s)=s^2(q-s) supplies exact finite-barrier and non-PDE residual controls. It has no negative zero interval and no accumulating endpoint; neither is claimed. Separately g(s)=exp(-1/s^2)sin(1/s) for s>0 and0 for s<=0 is smooth and flat, with positive zeros1/(n pi) accumulating at0 and empty interior. At its first positive zero q=1/pi, direct differentiation gives g'(q)=pi^2 exp(-pi^2)<1 and g''(q)=exp(-pi^2)(4pi^5-2pi^3)>0. Formula(19) at that zero and any z>0 is z(5-g'(q))g''(q)>0. Thus the same divergence identity holds, but(19) again is not identically0. Its use only checks the distinction between kinematic accumulation and the coupled equations. No numerical trajectory over a finite time is presented as proof of an infinite-time limit or a B2 profile.

Publication UTC: 2026-10-21T20:54:01.515502+00:00. Candidate v2 SHA256: 19a27b36cd4046c8bf04d0134f9dca8ef5d41ee664f677ff7ec35eacd01264f5. The candidate regularity clarification and model availability limits are recorded in verification/SUMMARY.md.
