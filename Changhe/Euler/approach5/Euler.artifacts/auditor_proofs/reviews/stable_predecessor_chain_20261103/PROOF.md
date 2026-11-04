# Stable predecessors of a vortical equilibrium connection

Status: independent audit of B53, correct with the repairs stated below. This gives necessary configurations, not their exclusion. The compact predecessors need not be equilibria or periodic orbits.

## 1. Exact setting and conclusions

Let 0<c<1/2 and omega be any finite real number. Set Jx=(-x2,x1,0), A=cI-omega J, B=Ax+U, Omega=curl U, a=1-2c and kappa=1+c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, (1-c)U+DU B+omega JU+grad P=0,
    U=o(|x|) uniformly, U.Omega=0 everywhere.

Define H=P+|U|^2/2+(Ax).U, g=U.B and Vort={Omega!=0}. Momentum implies P,H,g are C2. Let p be a vortical carrier equilibrium with

    DB(p)^T U(p)=rho U(p), rho<-a,
    spec DB(p)={rho,kappa,mu}, mu=-a-rho>0.

The submitted B53 assumes rho<=-2a, which is a subset of this strict range. The confirmed A770 gives the regular vortical H-level component M through p as the global unstable manifold W^u(p). On M, g=0 and the level covector rate is rho. Its normalized stream function psi satisfies

    B psi=mu psi, f=nu(B,Omega)=-mu psi, {psi=0}=L,
    nu=i_(grad H/|grad H|^2)vol restricted to M,

where L is the complete vortex line through p, with B=kappa tau Omega. These are the exact A771-A774 dependencies.

Assume one half L+ converges forward to an irrotational carrier equilibrium q. The confirmed endpoint theorem gives U(q)=-Aq!=0, H(q)=H(p)=h0,

    DB(q)^T U(q)=rho U(q),
    spec DB(q)|_(U(q)^perp)={lambda_-,lambda_+},
    lambda_-<=0<lambda_+, lambda_-+lambda_+=3c-rho.

Let gamma+ and gamma- be the two nonconstant orbits of the one-dimensional stable manifold of p, and K+ and K- their respective alpha-limit sets. Then:

1. Each K is compact, nonempty, connected, full-flow invariant and contained in closure Vort. It is neither {p} nor one periodic orbit. If p belongs to a nonpoint K, the corresponding stable branch has zeros of g, all critical for H, at arbitrarily negative times.
2. If K={p'}, then p' is irrotational, U(p')!=0, and for some r'>=0,

       DB(p')^T U(p')=r'U(p'),
       spec DB(p')={r',lambda_u,lambda_s},
       lambda_u>=kappa+r', lambda_s=3c-r'-lambda_u<=-a-2r'<0.

   If D Omega(p')!=0, the spectrum is {r',r'+kappa,-a-2r'}. If r'>0 and D Omega(p')=0, the first inequality is strict.
3. If lambda_-<0, S=W^s(q) is a two-dimensional C2 immersed stable manifold, Omega is tangent to S, and M intersect S is exactly the union of the halves of L which converge to q. At each fixed point of L+, a sufficiently small embedded patch of S has the two respective alpha-limits K+ and K- on its two sides, and {p} on the central L+ segment.
4. There is no carrier connection q->p. If K={p'}, there is no connection q->p' contained in closure Vort. This last assertion also holds when lambda_-=0, by Section8's direct scalar argument.

All assertions retain global zero helicity and uniform sublinearity. Neither a gradient bound nor a pressure normalization at infinity is needed. The source's decay hypothesis in its longer consultation proof can be weakened to the uniform sublinearity used here.

## 2. Complete flows and the two scalar transports

Uniform sublinearity gives |B(x)|<=C(1+|x|), so the C2 carrier field has a complete flow Phi_t. Outside a fixed ball,

    d_t |Phi_t x|=c|Phi_t x|+U(Phi_t x).Phi_t x/|Phi_t x|
                  >=(c/2)|Phi_t x|.

Consequently every compact set and all its backward carrier images lie in one compact ball. No boundedness of U on all of R3 is required for this conclusion.

The exact Euler identities and the global rank theorem A413 give

    grad H=B cross Omega-aU, BH=-ag, Omega H=0,
    [B,Omega]=-kappa Omega,
    dH wedge dg=0 on closure Vort.

On R={dH!=0} write l=(grad g.grad H)/|grad H|^2. This is C1. On closure Vort intersect R,

    dg=l dH, dl wedge dH=0.

The second identity follows first on the open vortical set by differentiating the first and then by continuity. Along a regular portion of a carrier orbit in that closure,

    g'=-a l g, (grad H)'=(-a l I-DB^T)grad H.            (1)

If such an orbit contains a point with g=0, then g remains zero on its maximal regular interval. There BH=0 and dl wedge dH=0 give Bl=0. Thus l is one constant and

    grad H(Phi_t x)=exp(rt)D Phi_t(x)^(-T)grad H(x),
    r=-a l(x).                                         (2)

At any finite endpoint this right side is nonzero, because D Phi_t is invertible. Hence the regular interval is the entire real line. This proves the A820 propagation lemma directly. Also Omega g=0 globally: apply Omega to BH=-ag and use [Omega,B]=kappa Omega and Omega H=0.

Let Gamma_tau denote the vortex flow. Its local commutation law is

    Phi_t Gamma_tau x=Gamma_(exp(kappa t)tau) Phi_t x.   (3)

It is complete. A compact set of backward carrier images has a uniform short vortex existence interval |tau|<delta on a slightly larger ball. For each T>=0 the curve

    tau -> Phi_T Gamma_(exp(-kappa T)tau) Phi_(-T)x

extends the vortex solution to |tau|<delta exp(kappa T). Uniqueness identifies all extensions. These intervals exhaust R. Applying (3) to a fixed compact vortex segment and using bounded Omega on its compact set of backward images gives

    |Phi_(-T)Gamma_tau x-Phi_(-T)x|
           <=C_tau exp(-kappa T).

It follows that alpha(Gamma_tau x)=alpha(x) for every finite tau. Completeness here is ambient; it does not imply completeness of a vortex trace on an immersed nonclosed surface.

## 3. Stable branches and critical crossings

The stable eigenvalue rho is simple and negative, and the remaining eigenvalues kappa,mu are positive. The C2 hyperbolic stable-manifold theorem supplies the one-dimensional C2 stable curve. Its two punctured local branches extend to two complete carrier orbits. Each point is vortical because a sufficiently late image is near p and finite-time Cauchy transport preserves nonzero Omega. Backward trapping yields compact alpha-limits. Nested closures of connected backward tails give connectedness; time translation gives full invariance.

Near p, H is a submersion because grad H(p)=-aU(p)!=0, with nonvanishing U supplied by A478. Since the neighborhood is vortical, the rank theorem gives g=G(H). At p,

    G(h0)=0, G'(h0)=-rho/a>0.

The stable eigenline is transverse to ker dH(p): the latter is the unstable spectral plane. Thus H restricted to the stable curve is a local coordinate, and g!=0 on its punctured local branches. Equation(2) now implies that every zero of g on the entire branch has dH=0.

A branch with alpha-limit {p} would lie in W^u(p)=M. On M, g=0, contrary to its forward behavior. This excludes a homoclinic branch, but not p as one point of a larger K.

For the latter case suppose that g has no zeros on an early tail. It has constant sign there, and BH=-ag makes H strictly monotone. Its compact backward orbit closure makes H bounded, so H has a backward limit. If p belongs to K, this limit is h0. At every finite point on this early tail, sign(H-h0)=-sign(g). But the infinitely many backward visits near p have sign(H-h0)=sign(g) from the local function G. This contradiction gives zeros of g at arbitrarily negative times; all have dH=0. Compactness also gives K intersect Crit(H) nonempty.

More generally no K can be wholly regular with r=-a l<=-delta<0 there. On a sufficiently early tail, r<=-delta/2, and g is nonzero by (2). Equation(1) makes |g| grow exponentially backward, contradicting compactness. If one additionally assumes g!=0 on the entire branch, then H is strictly monotone on it and K is contained in a zero-g level H=h1 with h1!=h0. This extra global nonvanishing assumption is not proved.

## 4. An equilibrium predecessor has nonnegative rate

Suppose K={p'}. Then p' is an equilibrium by invariance. It lies in closure Vort. The carrier-origin theorem A478 excludes U(p')=0: B(p')=0 would then force p'=0 and give a vorticity-free neighborhood. Thus grad H(p')=-aU(p')!=0. By rank and differentiation of g at the equilibrium,

    DB(p')^T U(p')=r'U(p'), r'=-a l(p').

On a sufficiently early branch tail, H is regular and g!=0. Equation(1) has coefficient r(t)=-a l(gamma(t))->r'. If r'<0, its solution grows in absolute value exponentially backward, whereas g(gamma(t))->g(p')=0. Therefore r'>=0. The confirmed vortical-equilibrium bound A496 would instead require r'<=-a if Omega(p')!=0. Hence p' is irrotational.

Put E(t)=ker dH(gamma(t)) and E'=U(p')^perp. Equation(1) makes E(t) invariant under the derivative cocycle. These planes converge to E', and Omega(t) lies in E(t). A normalized defining covector has derivative tending to zero, since its limiting right side in (1) vanishes. Thus one may use frames of E(t) converging to a frame of E', with derivatives tending to zero. In these frames the tangent variational coefficient converges to C=DB(p')|E'.

If s is the largest real part of the eigenvalues of C, an adapted constant norm and Gronwall give, for every epsilon>0 and every sufficiently early tail,

    ||D Phi_T|E(-T)||<=C_epsilon exp((s+epsilon)T).      (4)

For example an adapted quadratic norm follows from the positive matrix integral of exp(t(C-(s+epsilon/2)I))^T times itself; its Lyapunov identity bounds logarithmic growth, and the vanishing coefficient perturbation gives the remaining epsilon/2. A fixed final segment changes only C_epsilon.

The correct Cauchy formula is

    Omega(gamma(0))=exp(-kappa T)
                    D Phi_T(gamma(-T))Omega(gamma(-T)). (5)

Since Omega is bounded on the compact backward orbit closure and the left side is nonzero, (4) forces s>=kappa. The trace of C is 3c-r'. A nonreal pair would have real part (3c-r')/2<kappa. Thus the two eigenvalues are real, one lambda_u>=kappa, and the other lambda_s=3c-r'-lambda_u<=-a-r'<0.

If r'>0, all three eigenvalues are nonzero, and the orbit lies on the two-dimensional unstable manifold of p'. In local unstable coordinates the reversed field has eigenvalues -r',-lambda_u. A Lyapunov norm gives, for beta=min(r',lambda_u) and any small epsilon>0,

    |gamma(-T)-p'|<=C_epsilon exp(-(beta-epsilon)T).

Omega is locally Lipschitz and vanishes at p'. Combining this bound, (4), and (5) implies

    lambda_u-beta>=kappa.

Otherwise the right side of (5) tends to zero after choosing epsilon sufficiently small. This forces beta=r' and lambda_u>=kappa+r'. For r'=0 that is precisely the bound already proved. The trace now gives lambda_s<=-a-2r'. When r'=0, no hyperbolicity or membership in a one-dimensional strong unstable manifold is asserted.

If D Omega(p')!=0, A469 permits only the spectral families

    {r',r'+kappa,-a-2r'},
    {r',(-a-r')/2,(1+4c-r')/2}.

Both level eigenvalues of the second family are strictly below kappa when r'>=0 and 0<c<1/2. It is excluded. The first family is the stated necessary spectrum, not a realization theorem.

## 5. Strict inequality for a flat hyperbolic predecessor

Suppose r'>0, D Omega(p')=0 and lambda_u=kappa+r'. The three eigenvalues are distinct. On the local unstable manifold choose eigenvector coordinates v; its reversed equation is

    v'=-diag(r',lambda_u)v+O(|v|^2).

The preceding estimate gives integrability of |v(t)| over t>=0. Therefore

    d_t log|v|<=-r'+C|v|

integrates to the exact estimate |gamma(-T)-p'|<=C exp(-r'T). The moving level-plane coefficient differs from its diagonalizable limiting matrix by O(|gamma(t)-p'|), since DB and the normalized level covector are C1. This is integrable on the backward tail. Gronwall in an eigenvector norm consequently improves (4) to C exp(lambda_u T), without epsilon.

First-order flatness gives |Omega(gamma(-T))|=o(exp(-r'T)). In (5), equality lambda_u=kappa+r' now gives |Omega(gamma(0))|=o(1), a contradiction. Hence lambda_u>kappa+r' in this case. This refinement is in the longer source proof even though it was omitted from the condensed B53 statement.

## 6. A periodic orbit cannot be the whole predecessor

Suppose K is one nonconstant periodic carrier orbit Gamma. The confirmed exponent-transfer theorem A098 gives a forward exponent at least kappa on its orbit probability. The flow exponent is zero and the transverse exponents sum to 3c. A complex-conjugate Floquet pair has real parts 3c/2<kappa and is impossible. The transverse exponents are thus lambda_u>=kappa and lambda_s=3c-lambda_u<=-a<0. Floquet multipliers may initially have negative signs; their moduli give these exponents and hyperbolicity. The approaching branch lies in the two-dimensional unstable manifold of the periodic orbit.

If Gamma is irrotational, the local unstable-manifold and Floquet estimates give

    dist(gamma(-T),Gamma)<=C_epsilon exp(-(lambda_u-epsilon)T),
    ||D Phi_T(gamma(-T))||<=C_epsilon exp((lambda_u+epsilon)T).

A periodic adapted norm, or a double-period frame if needed, justifies the latter estimate. Local Lipschitz continuity of Omega, its vanishing on Gamma, and (5) yield

    |Omega(gamma(0))|<=C_epsilon exp((-kappa+2epsilon)T)->0,

a contradiction.

If Gamma is vortical, Omega and B are independent on it. Parallelism at one point would be preserved with ratio exp(-kappa t), contradicting periodicity. The Cauchy law gives the positive multipliers 1,exp(kappa T0),exp(-a T0), where T0 is the period. Short vortex arcs through Gamma form a two-dimensional surface tangent to B,Omega; (3) contracts their transverse parameter backward at rate kappa. Uniqueness of the local unstable manifold identifies that surface with it. A sufficiently early branch point is Gamma_tau z for z on the periodic orbit. Completeness and (3), together with Omega H=0, give

    H(Phi_t Gamma_tau z)=H(Phi_t z)

for every real t. The right side is periodic and the left side tends to h0 as t tends to infinity. Hence both are constant, forcing g=0 on the branch, contrary to Section3. The argument excludes one periodic orbit as the entire K, not as a proper subset of a larger K.

## 7. The hyperbolic endpoint's stable surface

Assume lambda_-<0. Then q is hyperbolic, with stable eigenvalues rho,lambda_- and unstable eigenvalue

    lambda_+=3c-rho-lambda_-=kappa+mu-lambda_->kappa.

Its C2 stable manifold S has dimension two. In a local C2 chart straightening S to z=0, its normal carrier component is z b(u,z), where b(q)=lambda_+. The transformed Omega is C1. The normal component w of Omega along an orbit of S satisfies

    w'=(b(u(t),0)-kappa)w.

Tangential derivatives of the normal carrier component vanish on z=0, so there is no additional term. The coefficient is eventually positive, whereas w tends to zero at the irrotational equilibrium q. Thus w is zero, and finite-time Cauchy transport gives Omega tangent to the whole global S.

At q, dH restricted to the stable spectral plane is nonzero: dH is a nonzero left eigenvector of rate rho and annihilates the unstable spectral subspace; if it also annihilated the stable subspace it would vanish. This argument includes the possibility rho=lambda_-. Continuity gives transversality of S and the regular H-level near q. The constant-rate covector law (2) along L+ transports it to each fixed point of L+.

If x belongs to M intersect S, then f=nu(B,Omega) tends to zero as its forward orbit tends to q. The level normal stays nonzero near q. Since f=-mu psi and psi(Phi_t x)=exp(mu t)psi(x), it follows that psi(x)=0. Thus x lies on L. Conversely any half of L converging to q lies in both M and S. Both halves must be allowed unless a separate argument distinguishes their endpoints.

Fix x0=Gamma_tau0 p on L+ and a small embedded patch S0 about x0. Its finite vortex translate T=Gamma_(-tau0)S0 is a C1 surface through p. It is tangent to Omega and B, because differentiation of (3) gives

    D Gamma_tau B=B composed with Gamma_tau-kappa tau Omega composed with Gamma_tau.

Also H composed with Gamma_tau=H, so dH is nonzero on T_p T. The plane T_p T is DB(p)-invariant, contains Omega(p), and is transverse to the level plane. Its eigenvalues are kappa and rho. In a graph chart formed by a linear projection, the restricted carrier field is C1, enough for the hyperbolic stable-manifold theorem. Its stable curve is the ambient local stable curve of p, by uniqueness. The inverse-function theorem for vortex arcs through that curve therefore gives coordinates

    y=Gamma_(tau0+s) z, z in W^s_loc(p), |s| small,

on a smaller S0, with the pair (s,z) unique. Equation(3)'s backward estimate gives alpha(y)=alpha(z). Thus the two sides inherit respectively K+ and K-, while z=p gives {p}. This is a local patch statement at each fixed x0, not a classification of all sectors of S.

## 8. No return, including a semihyperbolic q

A connection q->p would be one stable branch of p with single-equilibrium predecessor q. Section4 would give the covector rate of q nonnegative, contrary to rho<0. This proves no return without a hyperbolicity hypothesis at q.

For a possible connection eta from q to p' contained in closure Vort, H is regular on an early tail near q. There r(t)=-a l(eta(t))->rho<0 and g(eta(t))->g(q)=0. Equation(1) forces g to vanish identically on that early tail: any nonzero solution grows exponentially backward. Equation(2) then makes the whole orbit regular and zero-g with one constant rate. Its limit at q identifies this rate as rho, and its limit at p' identifies it as r'. This contradicts r'>=0>rho.

This proof covers lambda_-=0. The submitted explanation using only the one-dimensional unstable curve of q does not by itself cover that case: a semihyperbolic equilibrium can have other backward-converging center trajectories. No assumption that all such trajectories lie on the strong unstable curve is made here. A return orbit outside closure Vort is not excluded by this rank argument.

## 9. Vortex traces on the stable surface

Ambient vortex completeness does not imply completeness of the trace in S. The central trace L+ reaches p, which is outside S, at finite vortex parameter tau=0. Its q-end has tau growing like exp(kappa t), hence infinite vortex time.

For a nearby noncentral y in the patch of Section7, write y=Gamma_(tau0+s)z with z on a punctured stable branch of p. That z is outside S because its forward limit is p rather than q. The component of vortex parameters for which this line lies in S and which contains y is open and omits the finite parameter of z. It has a finite endpoint between them. The complete ambient vortex flow reaches a finite point there. It is outside S, because local uniqueness and tangency would otherwise extend the trace. Its vorticity is nonzero, since a nonconstant C1 integral curve cannot reach a zero at finite time. Conservation of H excludes p and q as that noncentral endpoint, since H(z)!=h0 near p. No classification of the opposite end or global properness follows.

## 10. The exact reduced polynomial model and its limitations

The consultation's model is checked algebraically, without running its script. In coordinates (x,s,z) put

    A0=1-x^2, f=-2kappa x(1-x^2), b=kappa(1+4x^2),
    F=b s(1-s), d=3c-f'-F_s,
    Bmod=(f,F,dz), Omod=(0,A0(1-s)^2,2A0(1-s)z).

Then div Bmod=3c and div Omod=0. If w=A0(1-s)^2, then Omod=(0,w,-w_s z). The identity f A0'=(b-kappa)A0 gives

    f w_x+F w_s-F_s w=-kappa w.

Differentiating this identity in s and using d_s=-F_ss gives the z component of [Bmod,Omod]=-kappa Omod. This verifies the full bracket.

The equilibria pmod=(0,0,0), qmod=(0,1,0), rmod+=(1,0,0), rmod-=(-1,0,0) have diagonal carrier spectra

    pmod: {-2kappa,kappa,3c+kappa}, Omod=e2;
    qmod: {-2kappa,-kappa,3c+3kappa}, Omod=D Omod=0;
    rmod: {4kappa,5kappa,3c-9kappa}, Omod=0,D Omod!=0.

The bounded scalar orbits on s=z=0 connect each rmod to pmod, and that on x=z=0,0<s<1 connects pmod to qmod. These particular orbits are complete. The latter has vortex parameter tau=s/(1-s) and Bmod=kappa tau Omod. Define Hmod=h(x), gmod=-f h'/a with h=x+2x^2. Then Omod Hmod=0, Bmod Hmod=-a gmod and dHmod wedge dgmod=0; at x=-1/4,s=z=0 both gmod and dHmod vanish and gmod changes sign. The covector rates at pmod and rmod are respectively -2kappa and 4kappa.

This is only a model of the displayed transport and scalar equations. Set Umod=Bmod-A(x,s,z). At pmod, curl Umod=2omega e3 differs from Omod=e2, while Umod=0 and grad Hmod=e1 violate the Lamb identity. At (0,1/2,0), Umod.Omod=(1-c)/16 and Umod.Bmod=kappa(1-c)/16, whereas gmod=0. Thus helicity zero and the definition of g also fail. Defining pressure from Hmod does not fix momentum: at pmod its gradient is e1 and all the other momentum terms vanish. The field does not decay or satisfy uniform sublinearity.

Global completeness also fails: on x=z=0,s>1 the carrier logistic equation blows up in finite backward time, and the vortex equation s'=(1-s)^2 blows up in finite forward time. The model therefore does not realize all global assumptions, and does not refute a possible global exclusion of critical crossings for actual Euler profiles.

## 11. Other source consequences checked

When omega=0, F0=c|x|^2/2-H/a satisfies B F0=|B|^2. On a compact backward orbit closure it has a backward limit and is constant on K. Invariance makes B=0 on K. The confirmed all-equilibria backward-limit theorem then makes K={p'}, with the preceding classification, and strict monotonicity gives F0(p')<F0(p)<F0(q). The nonrotating global class is already excluded by the separate nonrotating theorem; this is an independent conditional identity. When omega!=0 an extra term omega(Jx).B appears, with no sign asserted.

For a periodic carrier orbit of period T, integrating BH=-ag gives integral_0^T g=0. Since g=|B|^2-(Ax).B, integration of the radial derivative gives

    integral_0^T |B|^2=-omega integral_0^T (Jx).x'.

Subtracting the mean horizontal position and applying Cauchy-Schwarz and the periodic zero-mean inequality ||z||_2<=(T/(2pi))||z'||_2 gives T>=2pi/|omega| for a nonconstant orbit when omega!=0. The inequality follows componentwise from the Fourier coefficients and their nonzero frequencies. It asserts no existence or competing upper period bound.

If a hyperbolic equilibrium r belongs to a nonpoint K, the standard entry-exit argument supplies nonconstant full orbits in K intersect W^s(r) and K intersect W^u(r). For completeness, choose a sufficiently small hyperbolic isolating neighborhood with some K-point outside. Apply it to the approaching orbit of -B. Visits approaching r must have earlier entries and later exits; their distances in time from the closest visits tend to infinity by |B(x)|<=C|x-r|. Limit entry points stay in the neighborhood for all forward -B time, and limit exit points for all backward -B time. The local hyperbolic characterizations put them on the respective stable and unstable manifolds. They are nonzero boundary points; invariance gives their full orbits. This does not imply K has a periodic orbit, nor that it lies entirely in Vort.

## 12. Source repairs, scope and evidence

The complete 423-line consultation proof and the condensed Proposition13 were read. The source B53 Cauchy expression in part(c) has exp(+kappa T), which must be exp(-kappa T) as in(5). Its subsequent spectral inequality uses the correct sign and is valid after repair. Part(e) needs Section8's argument, or a hyperbolicity restriction, to justify the semihyperbolic endpoint case. The report-ready Theorem VL(11) needs an explicit rho<=-2a and connection premise; the base setting alone allows rho=-a and does not make p hyperbolic. The corrected proof here in fact covers rho<-a.

The original query to the consultant misstated the D6 hypothesis as applying to every vortical-point backward limit, rather than a limit set wholly contained in Vort. The consultation correctly declines that stronger input. No such extension is used here. The individual K+ and K- need not coincide; their union need not be connected. Neither the scalar-crossing model nor compactness forces a return chain. Classification and exclusion of general nonpoint predecessors remain open.

Dependencies: A048/A413/A468/A469/A478/A496/A770-A774/A820 and A098, plus the C2 hyperbolic stable-manifold and Floquet theorems with their hypotheses explicitly checked above. The only source computation is an exact polynomial check; it was independently verified symbolically by hand here. No numerical experiment, formal build, new client or agent was used.

The longer consultant source reports that its attempted model credential preflight failed, so no such invocation is counted. The Theory Agent B agent's received source and notes are from its configured model collaboration and were compared directly; provider runtime is not independently attested. Focused further replies are counted only upon receipt.


## 13. Completed second referee comparison

The complete 492-line w1stable2 answer was read, including every displayed estimate and its final limitation. It independently supplies the same negative Cauchy sign, nonnegative predecessor rate, moving-plane Lyapunov norm, matching unstable approach estimate, intrinsic embedded-patch qualification and semihyperbolic scalar repair. Its polynomial check and incompleteness warnings agree with Section10. Its nonrotating singleton conclusion correctly invokes A122. The source's use of the term crossing does not imply transversality or nondegeneracy.

The updated main Proposition13, read after its 12:31Z repair, includes the sublinearity argument, negative sign, embedded patch, closure-Vort qualification and scalar proof. Those repairs are confirmed. The compressed Theorem VL(11) still needs to state the lower-rate and specified-connection premises explicitly; its base setting includes rho=-a. The two scope issues must not be conflated: the proposition body has the lower-window premise, while the report summary has not yet restored it.

This second referee is a the second model/the external referee (a second model) response, not a model response. The Theory Agent B parent configuration is model as corrected in the team records and A1010; existing configured model collaboration comes from the coordinator, Theory Agent A and Theory Agent C. The failed nested credential request is not a review. No computation was rerun in this agent; the polynomial identities were checked by hand in Section10.
