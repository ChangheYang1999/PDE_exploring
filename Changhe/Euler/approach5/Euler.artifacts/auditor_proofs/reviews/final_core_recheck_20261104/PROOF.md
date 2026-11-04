# Final recheck of the core Euler theorem chain

## 1. Statements, notation and reading order

Let J(y1,y2,y3)=(-y2,y1,0), let omega be any fixed finite real number, put A=cI-omega J, and consider

    (1-c)U+[(Ay+U).grad]U+omega JU+grad P=0,
    div U=0                                                     (E)

on all of R3. Write B=Ay+U, Omega=curl U, Phi_t for the B flow and Psi_t=Phi_(-t). Uniform decay means sup_(|y|>=R)|U(y)| tends to zero. The claims rechecked here are the following.

**Energy theorem.** If U and P are C1, 0<c<1, U is bounded and U(R.) tends to zero in distributions on compact sets, then, with E(R)=integral_(|y|<R)|U|^2 and beta=5-2/c: U=0 for c<2/5; at c=2/5 the energy is finite and its exterior tail is O(R^-5); for c>2/5 there is a finite L>=0 with E(R)=L R^beta+O(R^(beta-1)), and L=0 forces U=0. Under uniform decay the error is o(R^(beta-1)). The energy constants can be chosen to depend on c, sup|U| and E(4), without dependence on omega.

**Smooth coverage theorem.** If U is C-infinity, P is C1, 0<c<1/2, (E) holds and U is uniformly sublinear, then almost every point of O={Omega!=0} belongs to one of countably many continuous-time basins of compactly supported, whole-flow-ergodic probabilities nu for Psi. Each nu gives full mass to {B!=0,Omega!=0}, has simple spectrum (a,0,-kappa), a=1-2c>0 and kappa=1+c, and has entropy a for Psi_1 and absolutely continuous unstable conditionals. Its basin has a unique maximal open essential domain D_nu in O, invariant under Psi and locally under the Omega flow, with Leb(D_nu minus Basin(nu))=0, Basin(nu) contained in D_nu and nu(D_nu)=1. Distinct such domains are disjoint. No claim of automatic coverage at C2 is made.

**Conditional helicity-sign theorem.** If U is C-infinity, P is C1, 2/5<=c<1/2, (E) holds, U decays uniformly, and U.Omega has one sign on each D_nu above, with the sign allowed to depend on nu, then U=0. At C2 the same conclusion holds if the countable coverage family, spectrum, entropy and unstable conditional properties just stated are separately assumed. This is a conditional theorem because of the sign premise, and at C2 also because of the coverage premise.

The complete pressure and energy proof is in the team records. The complete coverage construction is the captured report Section 2C, Lemmas 1-29. The complete analytic deduction after coverage is captured Section 2D, Lemmas 1-18 and the proof of Proposition L0. These were read in this shift at the scopes specified in Section 12. The argument below reconstructs the interfaces and the steps most susceptible to hidden hypotheses. It uses the exact curve construction proved in the named Section 2C lemmas, which are dependencies rather than unproved existence assertions.

## 2. The actual pressure, with no growth assumption on P

Let T_ij be the Fourier multiplier -xi_i xi_j/|xi|^2. Its nonlocal kernel is K_ij(x)=(3x_i x_j-delta_ij|x|^2)/(4pi|x|^5), with local distribution -delta_ij delta_0/3. For any compact smooth test phi, T_ij partial_k phi belongs to L1: locally use its L2 multiplier bound, and far away subtract K_ij(x) integral partial_k phi=0 to obtain a |x|^-4 tail. Thus bounded U defines a canonical pressure gradient G by

    <G_k,phi>=-sum_ij integral U_i U_j T_ij(partial_k phi).

Taking divergence of (E) cancels the two rotation contributions and gives -Delta P=partial_i partial_j(U_i U_j). Consequently grad P-G is harmonic as a distribution. Put U_R(z)=U(Rz). Integration by parts in (E) gives

    integral grad P(Rz)phi(z)
      =integral U_R[(4c-1)phi+(Az).grad phi]
       -omega integral JU_R phi
       +R^-1 integral U_R(U_R.grad phi).                    (1)

For fixed finite omega every term tends to zero under the distributional blow-down hypothesis and boundedness. Homogeneity of T gives G(R.)=O(R^-1) in the same test topology. The assertion remains true for phi(z-x/R) with x fixed, because these tests converge in the compact-test topology and boundedness controls the changing-test error. Apply the harmonic mean-value property using a radial unit-integral test about x. It follows that grad P-G=0 at x. The harmonic remainder is smooth and grad P is continuous, so G also has a continuous representative; the same mean-value argument is valid distributionally. This removes every harmonic pressure-gradient remainder. It does not assume a pressure normalization, a polynomial growth bound for P, or an L-infinity bound for T.

## 3. Annular energy and every boundary limit

Split U tensor U into |z|<R/2, R/2<=|z|<4R and |z|>=4R. In the last piece subtract K_ij(-z). The kernel difference is O(R|z|^-4) on |x|<2R. Since Section 2 identifies the actual gradient, these three pressures differ from P by one constant p_R on B_(2R). Set epsilon(R)=sup_(|y|>=R)|U(y)| and I(R)=integral_(|z|>=4R)|z|^-4|U(z)|^2. Then

    ||P_middle||2 <= epsilon(R/2) E(4R)^(1/2),
    sup_(R<|x|<2R)|P_inner| <= C R^-3 E(R/2),
    sup_(|x|<2R)|P_outer| <= C R I(R),
    I(R) <= 4 integral_(4R)^infinity r^-5 E(r) dr.           (2)

The final integration by parts has a vanishing upper boundary because E(r)=O(r^3); its lower boundary is nonpositive. No flux at infinity is set to zero.

Dotting (E) with U gives the classical identity

    (1-5c/2)|U|^2+div((|U|^2/2)B+PU)=0.

The skew rotation is tangent to every centered sphere. An additive pressure constant integrates to zero against U.n. Hence for g(R)=R^-beta E(R),

    g(R2)-g(R1)=-(2/c) integral_(R1<|y|<R2)
         |y|^(-1-beta)(|U|^2/2+P-p_R)U.(y/|y|).           (3)

Use one constant p_R on each annulus. Equations (2), Cauchy-Schwarz and boundedness show that E(r)=O(r^mu), 0<=mu<=3, implies the absolute annular flux is O(R^mu). Indeed its last pressure term has exponent (3mu-3)/2<=mu. Thus, for every R<=R1<R2<=2R,

    |g(R2)-g(R1)| <= C R^(mu-1-beta).                     (4)

If the exponent is positive, summation from inside improves E to O(R^(mu-1)); at equality it gives that power times log R; if negative, summation towards infinity supplies a finite g limit and the corresponding tail bound. Starting at mu=3, these finite iterations prove the three energy ranges in Section 1. A logarithmic equality case is absorbed in a small positive power before the next iteration. Once g has zero limit, outward summation lowers its energy exponent repeatedly; when the exponent becomes negative, monotonicity of E forces U=0. For beta<0 the inward iteration reaches mu=0, after which each of the three exponent cases gives E(R) tending to zero; this subcritical argument does not presume a previously obtained zero limit for g. Intermediate radii in (4) handle the last incomplete dyadic annulus.

For decaying U, the unsimplified estimate at mu=beta gives

    |g(R)-L| <= C[epsilon(R/2)/R+R^((beta-5)/2)].           (5)

Since beta<3, this is o(R^-1). At c=2/5 write T(R)=integral_(|y|>R)|U|^2 after finite total energy has been established. The same pressure decomposition and the convergent outward sum give

    T(R)<=C R^-1 T(R/2)+C R^-5/2 sqrt(T(R)).               (6)

A power tau improves to min(tau+1,(5+tau)/2). Starting from zero yields 1,2,3,4; Young's inequality in (6) then gives power 5. Finite critical energy by itself is not a vanishing theorem. The energy estimates used no characteristic flow and no derivative bound.

## 4. Complete carrier and exact transported vorticity

For a uniformly sublinear U, B has at most linear growth and satisfies B(y).y>=(c/2)|y|^2 outside a ball. Hence its flow is complete in both time directions. Every forward Psi orbit is bounded; a sufficiently large closed ball Q is strictly forward trapping. Its nested images have a compact invariant intersection K in int Q. Every bounded set eventually enters int Q. These facts use (Jy).y=0 for every omega.

For C2 U, take curl of (E) to obtain

    [B,Omega]=-kappa Omega,
    D Psi_t Omega=e^(-kappa t) Omega composed with Psi_t,
    D Psi_t B=B composed with Psi_t,
    det D Psi_t=e^(-3ct).                                 (7)

With alpha=(B cross Omega).dy one has

    d alpha=a i_Omega vol,  Psi_t^*alpha=e^(at)alpha,
    alpha(B)=alpha(Omega)=0,  L_Omega alpha=0.             (8)

These are pointwise C1 form identities; no derivative at infinity is taken. The sets B=0 and Omega=0, and their complements, are invariant under all real carrier times.

For the smooth coverage construction multiply -B by a smooth radial, nonincreasing cutoff equal to one near Q. Its complete compactly supported flow has a smooth time-one diffeomorphism f, equal to Psi_1 near K and along all positive Q orbits. It extends smoothly to S3 with a metric Euclidean near Q. The cutoff introduces no invariant measure with positive exponent outside Q: where the cutoff is positive the radius decreases until the orbit enters Q, while at zero cutoff the field and its derivative vanish. No original orbit relevant to K is changed.

## 5. Expanding arcs and the incoming measure

This section states explicitly the output of the checked curve lemmas. For the abstract pair B,W with div B=d>0, [B,W]=-kappa W and kappa>d, let G be any positive-volume measurable subset of {W!=0} intersect int Q. If s1>=s2>=s3 are the singular values of D Psi_N(x), then

    s3<=e^(-kappa N) max_Q|W|/|W(x)|,
    s1^2>=s1 s2>=e^((kappa-d)N)|W(x)|/max_Q|W|.

A coordinate-direction pigeonhole argument and Fubini give a straight arc D0 in the same open set with a positive-length subset on which the upper tangent exponent is at least (kappa-d)/2. The direction may depend on the point before the finite pigeonhole selection; it is fixed on the selected slice.

Report 2C Lemmas 7-11 prove the needed curve tree for g=f^p. A bounded curve has higher derivatives at most eta times its maximum speed, eta=1/100, so its minimum speed is at least (1-2eta) times that maximum. Taylor polynomials of the derivative, scalar polynomial level cuts and a fixed Vandermonde estimate give at most C_r M_g^(3/(r-1)) nonlarge children. Speed normalization can create many large children; it is not included in that count. All children remain small. Every restriction has affine slope at most 1/100, and distortion between any two tree levels is at most (50/49)^2<2, without multiplication of distortion constants over time.

Because f is C-infinity, choose r sufficiently large and then p sufficiently large so that the large-hyperbolic-time counting exponent is negative. Smoothness is used here to take r large; it is not being inferred from C2. The finite word count gives, for infinitely many n, subsets E_n of a fixed positive-length compact set E on the original arc, with normalized length at least 1/(2n^2), each carrying at least beta_0 n good large times for a fixed beta_0>0. The fixed E consists of density points of the original selected set F, with convergence of its relative density in tree atoms uniform on E. It is the density of F, rather than a density assertion about the varying E_n, that will be used to return to G.

Select a whole time-ell atom whenever it contains a sampled point with a good descendant at some time ell+i, 0<=i<=M. Report 2C Lemma 12 uses relative entropy of the nested original interval partitions to show absolute continuity of the limiting measure along image curves. Its hypotheses are met with L_n=log(1/length(E_n))=O(log n), N_n=floor(sqrt n), N_n L_n/n tending to zero, distortion bound 2, and descendant diameters at most 2 epsilon 100^(-N_n). Truncation at a density ratio K0 discards mass at most log 2/log K0 in the limit; taking K0 to infinity proves absolute continuity. No uniform density bound on E_n is asserted.

The finite window prevents collapse: a selected curve has a large descendant at most M steps later, so its length is at least epsilon/(2 max(1,||Dg||^M)). Its limiting curve is regular and embedded because the tangent cone is uniformly narrow. The finite-window measures increase with M. The increasing limit therefore still gives no mass to constant curves. A selected parent at time ell>=1 has a selected ancestor at ell-1 in window M+1; after taking n and then M to infinity this yields g_*mu>=mu. Equal finite masses imply invariance. The mass lies in [beta_0,1] before normalization and is supported in K.

Every curve in the support of a finite-window curve marginal has original approximants g^(ell_j)(P_j), ell_j tending to infinity, whose original intervals meet E and whose F-density tends to one. These approximants converge in C1 and have uniformly bounded distortion. Each limiting curve and all its backward iterates lie in K, with both diameter and derivative contracting at least as 100^(-k). This is the precise information used next. The construction is proved in report 2C Lemmas 7-15, whose complete proofs were read, rather than imported from an unspecified smooth-dynamics theorem.

## 6. Ergodic components, irrotational mass and capture

Generic regular points on one incoming curve have the same backward Birkhoff averages because its backward diameter tends exponentially to zero. A fixed countable test family therefore gives one measurable ergodic-component label on almost every such curve. Disintegration by that label preserves the curvewise absolutely continuous representation.

A nonconstant incoming curve contains at most one equilibrium of B: two distinct equilibria would have unchanged backward distance. Thus the invariant measure gives zero mass to B=0. At a two-sided regular point, boundedness of Dg^n B=B composed with g^n for all integer n puts B in the zero Oseledets space. Backward contraction of the incoming tangent gives a positive exponent; determinant e^(-pdn) gives the remaining negative exponent. The spectrum is consequently (p chi,0,-p(d+chi)), all simple. The curves lie in the full one-dimensional unstable manifolds by exponential backward approach.

Their absolutely continuous mixture implies absolute continuity of conditional measures on full subordinate unstable plaques. To justify this extension, a set null for leaf length on almost every subordinate plaque is null on every relevant embedded incoming curve: cover its intersection with the full-measure set by countably many leaf neighborhoods inside those plaques. Disintegration then gives zero mass. The usual entropy lower bound for absolutely continuous unstable conditionals and Ruelle's upper bound give entropy p chi. These are explicit external dynamical dependencies at compact C2 scope.

There is no mass on W=0. If there were, one finite-window curve would carry a positive-length compact set of regular points there. Choose a point where its tangent is the unstable direction. Its strong stable curve lies in W=0. Here is the relevant local argument. In a Lyapunov norm along a point with stable exponent -lambda, a nearby stable orbit approaches at rate e^((-lambda+epsilon)n). The C2 map has Lipschitz derivative on their compact orbit neighborhood. Comparing the two derivative cocycles gives a full conorm bound at least C e^((-lambda-3epsilon)n) on the nearby orbit. Since W vanishes on the base orbit and is C1, its value on the nearby orbit is at most C e^((-lambda+epsilon)n). Transport multiplies this conorm by e^(p kappa n), forcing the initial W value to vanish if 4epsilon<p kappa. This proof needs the full conorm bound, not an estimate only on the stable tangent.

The incoming curve and its carrier translate form a C1 surface transverse to that stable curve. A transverse-intersection persistence argument, obtained from Brouwer's theorem in a small coordinate ball, forces the approximating carrier surfaces to meet W=0 as well. But every original approximant lies on a carrier image of D0 contained in {W!=0}, an invariant set. This contradiction excludes the claimed irrotational mass.

For an ergodic g-component with W!=0 almost everywhere, recurrence and (7) identify the exponent of W as -p kappa. Thus chi=kappa-d. Averaging the component over carrier times in [0,p] gives a whole-flow-ergodic measure nu. Entropy affinity for a measurable kernel of invariant probabilities and the integer-iterate law give h_nu(Psi_1)=kappa-d. Time-one ergodicity is not assumed. Averaged test functions are included in the original countable Birkhoff test family, so the selected generic points belong to the continuous-time basin of nu.

A positive-length compact set of regular generic points on an incoming curve thickens under the carrier and W flows to a positive-volume product set. The three tangent directions are unstable, central and stable, hence independent. For sufficiently close original approximants, the first coordinate of the inverse product chart maps their image across that compact parameter set. Its Lipschitz bound gives a fixed positive fraction of approximant arclength in the basin. Bounded distortion pulls this fraction back to P_j. Since the complement of F in P_j has relative length tending to zero, a point of F, hence of the originally prescribed G, lies in this basin. This is a capture statement about the original positive-volume set; obtaining a physical measure somewhere else would not suffice.

Every probability of the required class has a positive-volume Borel basin. Distinct basins are disjoint, so there are only countably many. If the complement of their union in O had positive volume, invariance and eventual entry into Q would give a positive-volume set G there. The capture just proved is a contradiction. Apply this argument with d=3c and kappa=1+c. The strict inequality kappa>d is exactly c<1/2. This proves the coverage assertion.

## 7. Positive densities and essential domains

The remaining external input is precise. Ledrappier-Young Part I, Theorem A (1.5), applies to a C2 diffeomorphism of a compact Riemannian manifold preserving a Borel probability. Equality in the entropy formula gives absolutely continuous unstable conditionals. Lemma 3.1.1 supplies subordinate partitions; Corollary 6.1.4 supplies strictly positive finite densities on their elements, and Corollary 6.2 removes the ergodicity assumption. Thus a full conditional-measure set is a full arclength set on almost every selected one-dimensional plaque. Absolute continuity alone would not give this equivalence of null sets.

The compact cutoff model of Section 4 has the same measure, derivatives, spectrum and entropy on K. Its full unstable manifolds through K stay in K: an orbit that crosses an exterior sphere under the backward map cannot return, by the outward radial inequality for B. Thus the source theorem applies to the required original plaques. The regularity is C2 or better, and a central exponent is allowed. No inference from whole-flow ergodicity to time-one ergodicity is used.

Thicken a plaque's full-arclength generic set under the two transverse flows. The resulting open product box is almost entirely in its basin. Define D_nu as the union of all open subsets of O with this property. Second countability gives Leb(D_nu minus Basin(nu))=0; the construction gives nu(D_nu)=1. Carrier invariance follows by preservation of null sets. Local W saturation follows from

    Psi_t Gamma_s x=Gamma_(s e^(-kappa t)) Psi_t x,

initially for uniformly short W times on the compact closure of the forward carrier orbit. Hence the two points have the same basin limits. Membership is constant along any existing W segment. A basin point has a positive time average against a compact bump supported in D_nu with positive nu integral, so some carrier image lies in D_nu; invariance puts the original point there. Distinct domains cannot overlap on an open set because their disjoint basins would both have full volume in it. These steps prove exactly the domain claims of Section 1.

The retained Part I PDF was checked again against the author-hosted copy, which returned HTTP 200 and the identical SHA256 8f611bce4e328a50c3def42ce78f2d882ed24186e66867b6558c41588829d7a7. The precise theorem, density and nonergodic passages were reread. This is a source-statement and transfer audit, not a new proof of the entire external entropy theorem.

## 8. The complete vortex flow and recurrence

Now assume U is C2 and bounded. Although Omega need not be bounded on all of R3, its autonomous flow is complete. For a fixed bounded set of initial points, their forward Psi orbits stay in a fixed compact ball. The C1 field Omega has a uniform local time delta on a slightly larger ball. Given any vortex time s, choose T>=0 so that |s|e^(-kappa T)<delta and define

    Gamma_s x=Phi_T Gamma_local_(s e^(-kappa T)) Psi_T x.

Uniqueness and (7) make this independent of the sufficiently large T and give the actual continuation of the local solution. It is C1 locally in x and s. The carrier radial bound gives, for compact initial sets,

    |Gamma_s x| <= C(1+|s|)^(c/kappa).                     (9)

The global conjugacy also gives |Psi_t Gamma_s x-Psi_t x|<=C_x |s|e^(-kappa t) for all sufficiently large t, with s fixed. Both carrier orbits are bounded, so their time averages against every bounded continuous test agree. Therefore every Gamma_s preserves each basin. It preserves O as well, and is a C1 diffeomorphism. It maps every open set almost entirely in a basin to another such set, and its inverse does the same. Thus Gamma_s D_nu=D_nu for every real s. This is the global invariance needed below; mere local existence of segments in an open domain would not by itself prove it. These arguments are written fully in captured Section 2D, Lemmas 9(c) and 13(iii).

Since div Omega=0, Gamma_s preserves volume. The volume of a ball containing its iterates up to time N is O(N^(3c/kappa))=o(N) when c<1/2. A positive-volume bounded wandering set would have N disjoint equal-volume iterates in that ball, a contradiction. This argument for every integer time step gives almost-everywhere positive and negative recurrence on bounded measurable sets. It invokes neither finite total volume of the ambient space nor bounded vorticity at infinity.

Set H=P+|U|^2/2+(Ay).U and h=U.Omega. Direct algebra in (E) gives

    aU+grad H=B cross Omega,
    Omega.grad H=-a h,
    B.grad H=-a U.B.                                      (10)

On an invariant open domain where h has one sign, H is monotone on every vortex orbit. If h were strictly nonzero at some point, continuity would give an open set of initial points whose H changes by a fixed nonzero amount in a fixed short time. Almost-everywhere recurrence in that set contradicts monotonicity and continuity of H. Thus h=0 on each signed essential domain.

## 9. Bernoulli normalization and the product-box argument

For 2/5<=c<1/2 the energy theorem gives E(R)<=C R^beta, with 0<=beta<1. The pressure can therefore be normalized by one constant p_inf so that its far kernel integral is absolutely convergent, since integral_(|z|>R)|z|^-3|U(z)|^2 is finite. Put P0=P-p_inf and H0=H-p_inf. The local multiplier bound and the far kernel estimate give

    integral_(B_R) P0^2 <= C R^beta,
    integral_(B_R) H0^2 <= C R^(beta+2),
    R^-3 integral_(B_R) H0^2 ->0.                        (11)

The constants in this Bernoulli estimate may depend on finite omega. The energy theorem's stronger independence of omega is not asserted for every later constant.

For any bounded measurable Q0, Phi_t(Q0) lies in a ball of radius C e^(ct), and its inverse volume Jacobian is e^(-3ct). Consequently

    integral_(Q0) H0(Phi_t y)^2 dy <= C e^(c(beta-1)t)
                                  = C e^(-2at).          (12)

Its time average tends to zero as well. In the product box

    y=Gamma_tau Psi_r gamma(s)

inside D_nu, h=0 implies that H0 is constant along the vortex direction. The flow relation then gives H0(Phi_t y)=H0(Phi_(t-r)gamma(s)). Positive conditional densities provide full arclength of points gamma(s) generic in both carrier directions. They lie in supp nu, and the entire chosen plaque lies there by density and closedness. The time average of the right-hand square is therefore integral H0^2 dnu. Boundedness on the compact support justifies integration over the product box. Equation (12) forces that integral to be zero. Continuity gives H0=0 on supp nu. The product identity then gives H0=0 on every carrier translate of the full-volume generic subset of the box, and continuity gives zero on the open invariant union of all carrier translates of that box. A nonnegative continuous bump supported in the box and positive at its center in supp nu has positive nu integral. Every basin point visits this box by its time-average characterization, hence belongs to that invariant union. Thus H0=0 on the basin, and finally on D_nu by continuity and its full-volume basin property. Coverage gives H0=0 throughout O, since a continuous function zero almost everywhere in an open set is zero there.

This argument uses ordinary volume only in bounded boxes. It neither integrates H0 over a possibly infinite-volume basin nor assumes H0 belongs to L2(R3).

## 10. Irrotational holes and the final positive test

Continuity gives grad H0=0 on closure(O). On its boundary Omega=0, so (10) gives U=0 there. Let Z={Omega=0} and define V=U on int Z and V=0 elsewhere. On every compact ball this extension is Lipschitz: compare points in different pieces along their connecting segment, using the first exit and last entry at which U vanishes. Its almost-everywhere derivatives agree with those of U in int Z and vanish on its zero set. For the latter assertion, take a differentiability point that is a density point of the zero set. A nonzero derivative would keep V nonzero in a cone of positive relative volume near that point, contradicting density one. Thus div V=curl V=0 distributionally, including a possibly positive-volume boundary. V is harmonic, vanishes on the nonempty open set O, and therefore vanishes everywhere. If O is empty originally, U is bounded and harmonic and decay already gives U=0.

It follows that grad H0=0 throughout R3. The normalized mean in (11) fixes its constant as zero. Equation (10) now gives U.B=0 and hence P0=|U|^2/2. The pressure Poisson equation becomes

    Delta(|U|^2/2)+partial_i partial_j(U_i U_j)=0.          (13)

Test with chi_R sqrt(1+|y|^2), where chi_R is a nonnegative smooth cutoff equal to one on B_R and zero outside B_(2R). Terms differentiating chi_R are bounded in absolute value by C E(2R)/R, which tends to zero because beta<1. The remaining integral is nonnegative: the Hessian of sqrt(1+|y|^2) is positive definite and its Laplacian is positive. On any fixed ball the cutoff equals one for all sufficiently large R. Equation (13) and the vanishing boundary error force |U|^2 to integrate to zero there against a strictly positive weight. Thus U=0 everywhere. This proves the conditional theorem, retaining exactly its sign and coverage premises.

## 11. Ordinary nonrotating comparison

The full independent proof in the team records was reread through its current Section 10. Its exact theorem is separate: in dimensions 2 and 3, U,P in C1, omega=0, 0<c<1/2, (E) and uniform sublinearity imply U is constant, hence zero under decay. No new reading of the complete Liu manuscript is claimed by this subsection.

The four delicate points remain sound. The vorticity two-form transport is obtained by first integrating the C1 one-form identity and then taking its exterior derivative in distributions; no spatial derivative of continuous vorticity is assumed. The local null graph near a backward-unstable equilibrium follows from a bounded-orbit terminal variation-of-constants formula. A countable cover of open equilibrium neighborhoods then covers all convergent bad trajectories; it does not require a countable equilibrium set. For a connected nonpoint backward limit set, the inverse-function cylinder argument at rank d-1 produces a critical interval. A quadratic transverse Bernoulli bound and a first-exit path-length estimate force convergence, so such a nonpoint set has rank at most d-2. In dimension 3 its positive trace then leaves only the spectrum {3c,0,0}, while in dimension 2 it contradicts the positive trace. These steps, followed by the harmonic sublinear Liouville argument, prove the ordinary theorem as written.

For omega!=0 its Bernoulli derivative acquires the unsigned extra term described in that proof. Neither a coordinate rotation nor a relative-periodic reformulation supplies the missing global limit-set hypothesis. The ordinary theorem is not an unconditional rotating theorem.

## 12. Reading evidence, collaboration and limits

The report capture is the immutable bc3e3ddb assembly, whose Sections 0-10 and Appendix A are byte-identical to the approved ff5d4283 assembly. Its extracted Sections 2A, 2C and 2D and their complete hashes are in the team records. Actual fresh reading covered the complete nine-section energy reconstruction; Section 2C statements, all 29 smooth-construction lemmas and proofs, the finite-regularity outline and external-input list; and Section 2D statements, all 18 analytic lemmas, the main proof, corollaries and external-input list. Historical provenance lists, all supplementary source papers and every proof of finite-regularity refinements were not freshly rechecked. An oversized initial display and a later source-index search were truncated; they are not counted as complete readings. The bounded follow-up displays, rather than those truncated outputs, support the stated coverage.

The complete existing Theory Agent A  in the team records, including its two addenda and numbering correction, was reread and captured. Its independent pressure exponents, carrier Jacobian, zero-extension, cutoff constants and coverage-transfer checks agree with the reconstruction above. It explicitly excludes a fresh external-source reading; the present targeted Ledrappier-Young reading supplies that separate source check. This is collaboration with the existing configured model A agent and coordinator, not a newly invoked model. Provider-side execution is independently unattested. The current author PDF identity check is retained at in the team records. No unsuccessful or unreturned browser request is counted as retrieval evidence.

The argument supplies no automatic helicity sign, no unconditional C2 coverage, no automatic finite normalized gradient budget and no general rotating nonexistence result in the target interval. It does not strengthen the fixed-positive-excess sharpness claim or the finite-regularity theorem. The original conjecture remains OPEN. All new files are inside this agent.

## 13. Final independent comparison and disposition

The complete 146-line Theory Agent A  in the team records, written at 12:29Z after the request at 12:14:36Z, was read and retained as in the team records. Its six analytical checks agree: the actual pressure gradient, all intermediate radii in the energy bootstrap, complete recurrent vortex flow, strictly positive conditional densities, return from a bounded product box to every basin point, and zero extension across an irrotational boundary of arbitrary volume. A independently reread the corresponding report passages and the precise Ledrappier-Young theorem and corollaries. This is collaboration with the existing configured model agent, with the provider limitation stated in Section 12.

The five optional remarks were checked separately. The subcritical energy endgame and continuity of the canonical gradient are now explicit above. The argument only uses a box inside D_nu and the compact support of nu; it does not require supp nu to lie in D_nu. Constants in (11)-(12) may depend on omega. The density-point proof of the zero-set derivative assertion is included. The global-domain invariance step in Section 8 is also now explicit and agrees with the full existing Section 2D proof. None changes a theorem hypothesis or supplies an automatic helicity sign.

The comparison describes a 23-item symbolic diagnostic and a superseded run with a sign error in its diagnostic expression. Neither script nor log was read or rerun here, and neither is part of this verdict. The full Euler curl and scalar identities were checked analytically, with the residual sign curl Res=[B,Omega]+kappa Omega. Only the analytical comparison is adopted. The evidence manifest records both the original proof hash compared by A and this expanded version.
