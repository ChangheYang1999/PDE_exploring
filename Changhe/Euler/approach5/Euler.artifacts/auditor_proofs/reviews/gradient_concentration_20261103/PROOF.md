# Gradient concentration, its surviving limits, and the missing derivative estimate

Status: the exact results below are CONFIRMED in A682-A688 and A690. The method-completeness assertions are OPEN in A689. The main bare-decay rotating-profile problem is OPEN.

## 1. Hypotheses and conclusions

Let J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, B(y)=Ay+U(y), W=curl U. Unless a stronger assumption is explicitly stated, suppose c>0, omega is any real number, U in C2(R3;R3) is bounded and divergence free and

    DW B-DU W+W+omega JW=0.                           (K0)

Write M0=sup|U|, m(r)=sup_{|y|>=r}|U(y)| and use operator norms for DU. These hypotheses do not require U tending to zero. If DU is unbounded then M0>0.

The concentration conclusion is that there are z_n tending to infinity, lambda_n=||DU(z_n)|| tending to infinity, k_n tending to infinity, radii rho_n>0 and mu_n=rho_n lambda_n<=4m(|z_n|/2), such that

    ||DU||<=2lambda_n on B(z_n,k_n/lambda_n),
    V_n(x)=[U(z_n+rho_n x)-U(z_n)]/mu_n

converges locally uniformly, after a subsequence, to a nonconstant 2-Lipschitz divergence-free field V. It satisfies V(0)=0 and

    osc_B[0,1] V=1/2, osc_B[0,R] V<=R/2 for R>=1.

There is a unit e, the limit of B(z_n)/|B(z_n)|, such that e.grad V=G is a constant vector with |G|<=1/4. Thus V(x)=g(x-(e.x)e)+(e.x)G. If liminf mu_n/m(|z_n|/2)>0, V is bounded and G=0. If

    sup_B(z_n,Rrho_n)|W|=o(lambda_n) for every fixed R,

then V(x)=Mx with M symmetric, trace free and ||M||=1/4; mu_n/m(|z_n|/2) tends to zero, and DV_n cannot converge uniformly in any neighborhood of zero.

Sections 2-5 prove these statements, a Hessian lower bound, exact stationary limit examples and the passage-time bound. Sections 6-8 give sufficient vorticity and averaged-stretching conditions for DU tending to zero, plus a necessary Holder cost for the remaining strain concentrations. Section 9 explains what is and is not established about proof methods. Section 10 checks the cited stationary-Euler counterexample mechanism against the actual Gavrilov manuscript and proves its disjoint-copy corollary.

## 2. Doubling and the oscillation radius

Put M(y)=||DU(y)||. Given y with M(y)>0 and k>0, either M<=2M(y) on B(y,k/M(y)), or choose x1 there with M(x1)>2M(y). Repeat. At step j the increments are at most k 2^(-j)/M(y). An infinite iteration would stay in the fixed compact closed ball of radius 2k/M(y) while M tends to infinity, contradicting continuity. Thus there is z with M(z)>=M(y), |z-y|<=2k/M(y), and M<=2M(z) on B(z,k/M(z)).

Start with M(y_n) tending to infinity and choose k_n tending to infinity with k_n<=sqrt(M(y_n)). Then |z_n-y_n| tends to zero, lambda_n>=M(y_n), and z_n tends to infinity because M is bounded on compact sets.

Let o_n(rho)=osc_B[z_n,rho] U and rho_max=min(k_n/lambda_n,|z_n|/2). This oscillation is continuous in rho. A top singular vector of DU(z_n), tested at opposite points, gives o_n(rho)>=2rho lambda_n+o(rho). Hence the set

    {0<rho<=rho_max:o_n(rho)>=rho lambda_n/2}

contains an interval adjacent to zero and has a positive maximum rho_n. Every radius in this set obeys rho lambda_n<=4m_n, where m_n=m(|z_n|/2). Therefore mu_n<=4m_n<=4M0 and

    rho_max/rho_n>=min(k_n,lambda_n|z_n|/2)/(4M0) -> infinity.

In particular rho_n<rho_max eventually. Maximality and continuity give o_n(rho_n)=rho_n lambda_n/2, and for 1<R<=rho_max/rho_n the larger-radius oscillation is strictly less than Rrho_n lambda_n/2. The doubling estimate makes V_n 2-Lipschitz on B(0,k_n/(4M0)); V_n(0)=0 and ||DV_n(0)||=1. Arzela-Ascoli on expanding compact balls gives the stated locally uniform limit, including the oscillation equalities and divergence in distributions. No gradient convergence has been assumed.

## 3. The exact rescaled equation and the invariant direction

Write e_n=B(z_n)/|B(z_n)|, T_n=|B(z_n)|/mu_n and Omega_n=curl V_n=W(z_n+rho_n x)/lambda_n. Since |Ay|>=c|y|,

    T_n>=(c|z_n|-M0)/(4M0) -> infinity.

The identities B(y)=B(z_n)+rho_n Ax+mu_n V_n, DU=lambda_n DV_n and DW=(lambda_n/rho_n)D Omega_n give, after division by lambda_n^2,

    T_n(e_n.grad)Omega_n+(V_n.grad)Omega_n-(Omega_n.grad)V_n
      +lambda_n^(-1)[(Ax).grad Omega_n+Omega_n+omega J Omega_n]=0.   (3.1)

On each fixed ball, |V_n|<=2R and |Omega_n|<=4. The latter follows because the operator norm of the skew part of DV_n is |Omega_n|/2. Write the two nonlinear terms as the divergence of V_n tensor Omega_n minus Omega_n tensor V_n, with the indicated advecting index; write (Ax).grad Omega_n as div((Ax) tensor Omega_n)-3c Omega_n. After testing and division by T_n, all remaining terms tend to zero in distributions. Local uniform convergence of V_n gives

    e.grad curl V=0.

G=e.grad V is bounded, divergence free and curl free in distributions. Thus Delta G=0. Weyl's lemma and Liouville imply G is constant. Mollification, followed by the fundamental theorem of calculus along lines parallel to e, proves V(x)=g(x-(e.x)e)+(e.x)G. The oscillation between Re and -Re gives 2R|G|<=R/2 and hence |G|<=1/4.

If mu_n>=delta m_n along a subsequence, |V_n(x)|<=2/delta on balls with radii |z_n|/(2rho_n) tending to infinity. The same limit V is bounded there and G=0. If instead Omega_n tends to zero uniformly on every compact ball, V is harmonic and Lipschitz. Each derivative is a bounded harmonic function, so V=Mx. Curl and divergence give symmetry and zero trace, and osc_B[0,R] Mx=2R||M|| gives ||M||=1/4. Such a V is unbounded; a subsequence with mu_n/m_n bounded below is therefore impossible. Finally, uniform convergence of DV_n near zero would force ||M||=1 from ||DV_n(0)||=1, a contradiction. This completes the concentration theorem.

## 4. Hessian scale and exact example fields

Let z have lambda=||DU(z)||>0, m=m(|z|/2), and rho=2m/lambda<=|z|/2. Choose unit singular vectors v,w with w.DU(z)v=lambda and set f(s)=w.U(z+sv). If K=sup_B[z,rho]||D2U||, then f'(s)>=lambda-K|s|. Integration gives

    f(rho)-f(-rho)>=2rho lambda-Krho^2.

The left side is at most 2m, so K>=lambda^2/(2m). This is a lower bound at a specified far point, not a uniform upper bound or an existence statement for profile concentrations.

The field

    V_sh(x)=(sin(8x2+pi/3)-sin(pi/3))e1/4

is divergence free, stationary Euler with constant pressure, and has ||DV_sh(0)||=1 and global Lipschitz constant2. Its oscillation on B[0,R] equals1/2 for R>=pi/8. For any e in span(e1,e3), e.grad curl V_sh=0 and e.grad V_sh=0. Its nonlinear vorticity bracket also vanishes. Thus it satisfies all the listed vortical-limit properties, including the retained base-point gradient value if C1 convergence were available.

For M=diag(1,-1,0)/4, V_st=Mx is an irrotational stationary Euler field with pressure -x.M^2x/2. It has the required limit oscillations, ||M||=1/4, and e.grad V_st=0 for e=e3. It satisfies the limiting conclusions of the small-vorticity branch. That branch explicitly forbids C1 convergence at the base point.

The previously confirmed polynomial local profile U=grad((y1^2-y2^2)y3) has U(0,0,n)=0 and ||DU(0,0,n)||=2n. Its exact rescaling is

    [U((0,0,n)+rho x)-U(0,0,n)]/(2n rho)
      =diag(1,-1,0)x+(rho/n)(x1x3,-x2x3,(x1^2-x2^2)/2).

For rho/n tending to zero this converges smoothly on compact sets to 4V_st. This polynomial field is unbounded, so it is not a BU sequence under the boundedness hypothesis and does not realize the selected oscillation scale.

These examples show that the displayed limit equations and oscillations alone do not contradict. They do not construct any bounded global profile with unbounded derivative or realize a proposed BU limit for such a profile.

## 5. Each passage through a concentration ball

Fix R. For large n the doubling ball contains B(z_n,Rrho_n), and ||DB||<=||A||+2lambda_n there. Thus

    e_n.B(y)>=beta_n:=|B(z_n)|-(||A||+2lambda_n)Rrho_n>0.

Along each connected time interval inside the ball, e_n.(y-z_n) increases at least beta_n and has total range at most2Rrho_n. The interval has duration at most

    sigma_n<=2R/[lambda_n(T_n-2R-||A||R/lambda_n)]
             =O(R/(lambda_n T_n))=o(1/lambda_n).       (5.1)

The fundamental matrix of W'=(DU-I-omega J)W differs from the identity by at most exp((2lambda_n+1+|omega|)sigma_n)-1=O(R/T_n). Along a nonzero-vorticity passage the absolute change of log|W| obeys the same bound. Thus the relative change tends to zero on each such passage. This says nothing by itself about the number of returns or the accumulation of growth over many passages.

The coefficients lambda_n^(-1) and the stream factor T_n in (3.1) are exact. An anisotropic limit over lengths comparable to T_n is not established: neither compactness on those boxes nor smallness of T_n/lambda_n is supplied.

## 6. Local logarithmic div-curl estimate and derivative decay

For fixed alpha in (0,1), let

    w(y)=sup_B(y,3)|W|, H(y)=[W]_(C^alpha(B(y,3))),
    M3(y)=sup_B(y,3)|U|.

There is a constant C_alpha independent of y such that

    ||DU(y)||<=C_alpha[M3(y)+w(y)(1+log^+(H(y)/w(y)))]. (6.1)

When w=0 define its entire displayed contribution to be0. To verify (6.1), multiply U by a smooth cutoff equal to1 near y and supported in B(y,2). Use Delta U=-curl W. In Delta(chi U), write the terms involving DU as divergences of U tensor grad chi, so their contribution to DU(y) is bounded by C M3(y); the additional cutoff terms involving W are bounded by Cw. The principal term is the order-zero Calderon-Zygmund kernel applied to chi W. On the inner unit ball its kernel has zero spherical mean. Split at radius delta: the Holder cancellation gives C H delta^alpha, and the annulus gives Cw log(1/delta). Choose delta=min(1,(w/H)^(1/alpha)) when w,H>0. The degenerate cases follow directly. This proves (6.1) with no global norm or pressure assumption.

Now suppose U is a full C2/C1 profile, 0<c<1, U tends uniformly to zero, and

    w(y)(1+log^+(H(y)/w(y)))=O(|y|^(1/2)).            (LV)

Then (6.1) gives DU=O(|y|^(1/2)). A498 proves DU tends to zero under precisely these assumptions, and A492/A476 give |DU|+|W|=O((1+|y|)^(-1)). For c>1/3, A477 additionally gives the natural rates

    |DU|+|W|=O((1+|y|)^(-1/c)),
    |U|=O((1+|y|)^(-(1-c)/c)).                       (6.2)

The restriction c>1/3 in this cited deduction must be retained. The source's wider clause asserting (6.2) for every0<c<1 is not established by those references. The entire campaign target is inside the confirmed range.

Two sufficient special cases are w=O(r^(1/2)/log r) with polynomial H, and bounded w with H<=exp(Csqrt(r)). For the latter use

    w log^+(H/w)<=w log^+H+w log^+(1/w)
                    <=(sup w) Csqrt(r)+1/e.

For the former, when w>=r^(-1) the logarithm is O(log r), and when w<r^(-1) use w log^+(H/w)<=w log^+H+w log^+(1/w)=O(log r/r). These observations cover arbitrarily small w and H.

## 7. Whole-segment stretching threshold

For bounded U and c>0 the field B has at most linear growth and a complete C1 flow. Choose R1>0 with R1>=2M0/c. The radial derivative lies between cr-M0 and cr+M0. Every point z with r=|z|>R1 reaches the sphere R1 in backward time s(z), and outside that sphere radial growth is strictly positive. Integrating the two radial bounds gives

    (1/c)log((cr+M0)/(cR1+M0))<=s(z)
           <=(1/c)log((cr-M0)/(cR1-M0)).

The denominators are positive if M0>0; the M0=0 case is immediate. Consequently |cs(z)-log(r/R1)|<=log2<1.

If W(z)!=0, the linear vorticity ODE excludes zeros anywhere along the segment. Put xi=W/|W| and S=sym DU. Rotation is skew, so

    d/ds log|W|=xi.Sxi-1.

Let C1=sup_{|y|<=R1}|W(y)|. It is positive whenever such a segment exists. Integration gives

    average_segment xi.Sxi
       >=1+[log|W(z)|-log C1]/s(z).                  (7.1)

In particular |W(z_n)|>=d|z_n|^(1/2), d>0, forces these averages to be at least1+c/2-o(1).

Conversely suppose U tends to zero,0<c<1, H is polynomially bounded, and for every such far segment the average is at most1+c/2-epsilon with a fixed epsilon>0. Then the exact vorticity law gives

    |W(z)|<=C1 exp((c/2-epsilon)s(z))
            <=C |z|^(1/2-epsilon/c).                (7.2)

The two-sided time bound justifies this for either sign of c/2-epsilon. On neighboring fixed-radius balls the same rate holds for w. The logarithmic estimate in Section6 gives (LV), since r^(-epsilon/c)log r is bounded. Thus DU tends to zero. No pointwise strain bound follows from this averaged hypothesis, and the endpoint average1+c/2 remains unresolved by this argument.

## 8. Small vorticity forces strain limits and a large Holder seminorm

Suppose in addition U tends to zero and |W(y)|<=C(1+|y|)^delta for some delta<1/2. For any BU sequence with lambda_n/|z_n|^(1/2) tending to infinity, every fixed-radius rescaled ball remains at radius comparable to |z_n|. Hence

    sup_B(z_n,Rrho_n)|W|/lambda_n
       <=C_R |z_n|^delta/lambda_n ->0.

The strain alternative of Section3 follows. The local estimate and w log^+(H/w)<=w log^+H+1/e give

    lambda_n<=C[1+|z_n|^delta(1+log(2+H(z_n)))].

Since lambda_n tends to infinity, absorb the constant term into half of lambda_n. There are a,b>0 independent of n such that

    log(2+H(z_n))>=a lambda_n/|z_n|^delta-b,
    log(2+H(z_n))/|z_n|^(1/2-delta) -> infinity.       (8.1)

This also handles delta<0. No hypothesis that H is polynomial is used here. If it were polynomial, the remaining sequence would be impossible. This is exactly the additional cost of the unresolved strain branch, not its exclusion without a modulus assumption.

If the small-vorticity alternative fails, a subsequence has some fixed R,d>0 and points in B(z_n,Rrho_n) with |W|>=d lambda_n. At super-half-power concentrations (7.1) applies at those points. Equation(5.1) still controls only a single connected passage, not the full history of the large vorticity.

## 9. What the audit does not establish

The listed limit examples rule out deriving a contradiction from only their shared necessary limit properties. They do not show that all constraints inherited from the exact profile equation have been listed. No sequence of bounded global profiles has been constructed with the shear limit, and no such strain sequence has been constructed either. Consequently the source's universal claims that every blow-up proof must use outside information or the profile time scale are not proved. New local identities, a next-order estimate or an additional compactness consequence have not been exhausted.

The statement that a proof must use pressure explicitly together with W=curl U is likewise not a necessity theorem. Indeed on all R3, (K0) and div U=0 say that

    F=(1-c)U+DU(Ay+U)+omega JU

has zero curl. Since R3 is simply connected, F=-grad P for a global pressure, unique up to a constant. A proof formulated entirely with (K0) can therefore already encode the existence of pressure. What fails in the cited countertests is a particular reduced list of estimates, not this exact equivalence.

Under U tending to zero and0<c<1, the following equivalence is valid: DU tends to zero if and only if there is no BU sequence with lambda_n/|z_n|^(1/2) tending to infinity. One direction is immediate from global boundedness of DU. For the other, if DU fails to tend to zero, A498 forces limsup ||DU(y)||/sqrt(|y|)=infinity. Start doubling at points with ||DU(y_n)||>=n sqrt(|y_n|); the shifts tend to zero and lambda_n only increases, so the BU sequence has the required ratio. This is an exact reformulation, not a proof that such sequences are absent.

## 10. Published stationary example and the disjoint-copy construction

Gavrilov's A steady Euler flow with compact support, arXiv:1810.08020v1, states and constructs a nonzero C-infinity stationary Euler velocity supported in a small neighborhood of a circle. The complete seven-page manuscript was read, including its analytic construction and its pressure-level cutoff in Section3. Thus this input is source-checked, not recalled from an abstract. It is a theorem about stationary Euler, not rotating self-similar profiles.

Take one such pair (v,q). Normalize q=0 on the unbounded component outside a ball containing supp v. The stationary equation gives grad q=0 there, so both v and q are supported in a fixed ball after enlarging the ball if needed. Rescale that ball to the unit ball. Choose a point x* with d=||Dv(x*)||>0, amplitudes a_n=2^(-n), desired derivative values L_n tending to infinity, and positive b_n<=min(1/4,a_n d/L_n). Let z_n=3n e1 and set

    u(x)=sum_n a_n v((x-z_n)/b_n),
    p(x)=sum_n a_n^2 q((x-z_n)/b_n).

The enlarged support balls are disjoint and locally finite. Therefore u,p are C-infinity; every point lies in at most one nonzero summand. Each scaled pair satisfies div u=0 and (u.grad)u+grad p=0, including support boundaries because the seed pair is smooth. Thus their sum is an exact stationary solution. Since a_n tends to zero and the centers escape, u tends uniformly to zero. Yet at z_n+b_n x*,

    ||Du||=(a_n/b_n)d>=L_n.

Also int|u|^2=||v||_2^2 sum a_n^2 b_n^3<infinity. This nonzero stationary solution cannot satisfy the campaign profile equation in the target range: the already confirmed finite-energy profile theorem would force it to vanish. It demonstrates precisely why stationary-Euler velocity decay, even with its full pressure relation, does not imply a derivative bound. It does not settle (T-H3).

## 11. Verification record and dependencies

The complete source in the team records, including its10:05Z addition LV.3, was read and all displayed new statements were recomputed by hand. No numerical or symbolic calculation was necessary. The source's old check logs are not treated as this agent's computation or as proof of compactness. A498,A492,A476,A477 supply the stated derivative implication and rate conclusions; their exact scopes were checked in the earlier independent proofs. A582 supplies only the explicitly unbounded polynomial profile. The compact stationary seed in Section10 is the cited published theorem, with its actual manuscript archived in verification.

A focused request to the existing configured model agent asks it to correct the rate range and universal method language; no additional model client is launched. Provider runtime is not independently attested. Public read-only reference retrieval is the only external operation.
