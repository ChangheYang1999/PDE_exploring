# Conditional global flow, weighted transport inversion and the far-field cost

2026-10-20. Independent verifier reconstruction, written before the numerical checks. Application status OPEN. The lead's revision1 is preserved in evidence/lead_global_flow_v1.md with its actual capture hash and time. This proof does not certify its hypotheses for the numerical trial.

## 1. Setting, hypotheses and statements

Let Q={(x,y):x>0,y>0}. Let V be a C^1 vector field on the plane, of at most linear growth, with V_1 odd in x and even in y, V_2 even in x and odd in y, and div V=2c_l constant. Suppose:

- Its only equilibria in the closed quadrant are 0 and P=(x_*,0), where x_*>0.
- V_2(0,y)>0 for y>0. On the positive x-axis, V_1<0 before x_* and V_1>0 after x_*.
- DV(0)=diag(-A_0,D_0), A_0,D_0>0; DV(P)=diag(A_P,mu_P), A_P,mu_P>0.
- There are R_0,kappa_0>0 with X dot V(X)>=kappa_0|X|^2 whenever |X|>=R_0.

The notation A_0 is the saddle rate. The sum a+b of weight exponents below is denoted S, to avoid the lead note's two uses of A. Constant divergence and the source linearization imply c_l>0.

We prove the following conditional results.

1. The complete flow phi_t preserves Q. For every X in Q, phi_t X tends to P as t tends to minus infinity, and its radius tends to infinity as t tends to plus infinity.
2. A sufficiently small upper semicircle Sigma about P is a global section: (sigma,t) maps to phi_t sigma as a C^1 diffeomorphism Sigma times R onto Q. Outside fixed sufficiently small neighborhoods of 0 and P and a sufficiently large exterior disk, the total time on any orbit is uniformly bounded. The bound is existential; no numerical transit time is established here.
3. Let w be positive measurable, locally bounded above and away from zero on Q. If

   w(phi_(-t)Y)<=exp(beta t)w(Y), t>=0,

   and kappa=1+c_l-beta/2>0, then

   R_-f=-integral_0^infinity exp(-t) f(phi_t X)dt

   is the bounded inverse of V dot grad-1 on its maximal distributional domain in L^2(Q,w dX), with norm at most1/kappa. The analogous weighted supremum bound is1/(1-beta_m) if m>0 is C^1 and V dot grad log m<=beta_m<1. Neither result needs the non-trapping assumptions once completeness, quadrant invariance and the weight inequality have been established.
4. For positive C^1 reference weight w_0 on Q, set T_0=-(1+c_l)-(V dot grad log w_0)/2. If C_kappa=sup_{X in Q,0<=s<infinity} integral_0^s 2(T_0+kappa)(phi_t X)dt is finite, including all finite forward segments and the zero-length segment, an explicitly defined measurable weight w satisfies

   w_0<=w<=exp(C_kappa)w_0,
   ||R_-||_(L^2(w_0))<=exp(C_kappa/2)/kappa.

   A sufficient condition for C_kappa<infinity is a finite global supremum of T_0 and T_0+kappa<=0 on the three neighborhoods from statement2. The constructed weight need not be C^1; its useful conclusion is a flow inequality.
5. Let 0<k<1, c_l=1/k, and suppose additionally V=c_l X+O(r^k) uniformly at infinity. Suppose that on each compact angular subinterval of(0,pi/2),

   w(r,theta)/(r^(-2gamma) b(theta)) -> 1

   uniformly as r tends to infinity, where b is positive and continuous on that subinterval. If the maximal transport operator has a bounded two-sided inverse and kappa_inf=1+c_l(1-gamma)>0, its norm is at least1/kappa_inf. At kappa_inf=0 no bounded two-sided inverse exists. This lower bound concerns only V dot grad-1, not the coupled IPM operator.

The planar dynamical dependencies are recorded in evidence/planar_dependency.md. Their precise forms used here are: a bounded orbit of a C^1 planar field with finitely many hyperbolic equilibria has, unless its limit set is a single equilibrium or periodic orbit, a limit set containing a connecting orbit between its equilibria; and a periodic orbit has an equilibrium in its Jordan interior. These are the finite-equilibrium Poincare-Bendixson alternative and planar index theorem. All equilibria considered here are hyperbolic. The proof below also supplies a direct local argument excluding the saddle connections it needs; it does not assume a global stable-manifold assertion.

## 2. Completeness, invariant neighborhoods and saddle exclusion

The linear growth bound and Gronwall's inequality keep a trajectory in a bounded disk on every finite time interval in either direction. C^1 local existence and uniqueness therefore extend it to all real times. Both axes are invariant. An interior orbit cannot reach an axis at finite time, since uniqueness backward from that point would force it to have lain on the axis already. Thus Q is invariant.

The quotients V_1/x and V_2/y extend continuously to their respective axes. For example

V_1(x,y)/x=integral_0^1 partial_x V_1(sx,y)ds.

This identity follows from V_1(0,y)=0. The other quotient is identical with the coordinates interchanged. In a small square about0 they are bounded by

V_1/x<=-A_0/2, V_2/y>=D_0/2.

No Q orbit can converge to0 in forward time: if it did, it would eventually stay in this square, but y would grow at least exponentially from a positive value. No Q orbit converges to0 backward, since x grows at least exponentially in backward time. For a closed-quadrant connecting orbit tending to0 forward, the same argument forces y=0; for one tending to0 backward it forces x=0. Consequently no nonconstant homoclinic orbit at0 exists. The two axes meet only at0, and an orbit cannot jump from one axis to the other.

At P let q=|X-P|^2 and m_P=min(A_P,mu_P). Differentiability gives

V dot grad q=2A_P(x-x_*)^2+2mu_P y^2+o(q)>=m_P q

on0<q<=delta for some delta>0. Every sufficiently small circle is strictly outward crossed. Such a disk is backward invariant, and q(phi_(-t)X)<=exp(-m_P t)q(X) after entry. No forward orbit can enter any of these disks from outside. In particular P cannot belong to the omega-limit of any other orbit.

At large radius, d(log r)/dt>=kappa_0. The exterior of the R_0 disk is forward invariant. A backward orbit starting there enters the closed disk in time at most log(r/R_0)/kappa_0. To justify the endpoint of this bound, if no entry had occurred by that time, integration of the strict exterior inequality would give r<=R_0. The closed disk is backward invariant. Once a forward orbit enters the exterior, its radius grows at least exponentially.

## 3. Non-trapping and the global section

There is no periodic orbit in the closed quadrant. An orbit meeting an axis stays in that one-dimensional invariant set, where no nonconstant periodic solution exists. A periodic orbit in Q is a Jordan curve with its whole bounded interior in Q: the interior lies in the convex hull of the curve, which has positive distance from both axes. The planar index theorem would force an interior equilibrium, contrary to the assumed list0,P. Equivalently, constant positive divergence rules out this periodic orbit by the planar divergence theorem.

Suppose a forward Q orbit never enters the exterior disk. Its omega-limit is nonempty, compact, connected and invariant. P is excluded by the source disks. If the limit contains no equilibrium, the planar alternative gives a periodic orbit, already excluded. If it contains only0, that alternative makes it either the singleton0 or a set containing an orbit from0 back to0. The local quotient argument excludes both alternatives. Thus the forward orbit must reach the exterior and tend to infinity.

A backward orbit is eventually in the fixed compact disk. If P belongs to its alpha-limit, it enters a source disk at some backward time, stays there and converges to P. Otherwise its alpha-limit has only the possible equilibrium0; the same planar alternative applied to -V contradicts either convergence to0 or a homoclinic connection. This proves statement1.

Choose eps_P<min(sqrt(delta),x_*/2), and shrink it if necessary, and define

Sigma={P+eps_P(cos theta,sin theta):0<theta<pi}.

Every Q orbit enters this source disk in backward time and escapes in forward time. It meets Sigma exactly once because every crossing is outward. The map Phi(sigma,t)=phi_t sigma is bijective. Transversality makes its derivative nonsingular; the inverse function theorem supplies a C^1 local inverse at every point. Bijectivity makes these local inverses agree, proving the global C^1 assertion.

## 4. Uniform transit, including the incoming separatrix

Choose eps_0>0 so small that the square B_0=[0,eps_0]^2 is disjoint from the source disk, eps_0<x_*-eps_P, and the quotient inequalities of section2 hold there. Choose R_1>max(R_0,x_*+eps_P,sqrt(2)eps_0). Let K be the part of the closed R_1 quadrant disk outside the open source disk and the relatively open square[0,eps_0)^2. Changes on the finitely many transverse boundary crossings do not affect occupation time.

Parametrize Sigma by theta in(0,pi). Before its unique section crossing an orbit lies in the source disk. After its first radius-R_1 crossing it stays outside the large disk. The first large-circle crossing time H(theta) is finite and continuous on(0,pi), by continuous dependence and the nonzero radial derivative at the crossing. It is bounded on compact angular subsets.

At theta=0, the endpoint lies on the outgoing positive x-axis. Its orbit reaches R_1 in finite time because V_1>0 on the compact axis segment in question. The crossing is transverse. Continuous dependence extends H continuously to this endpoint.

At theta=pi, the section endpoint lies between0 and P on the x-axis. It reaches x=eps_0 in finite time t_1, with V_1<0 there. Nearby Q trajectories reach the same vertical line by time t_1+1, at entries(eps_0,y_in) with y_in>0 and y_in tending to0. On B_0, x decreases and y increases, and y grows at least at rate D_0/2. Thus each trajectory exits in finite time through y=eps_0 and cannot leave through either coordinate axis or the right edge. Put M_0=sup_(B_0)V_2/y<infinity. Its box residence time satisfies

t_box>=log(eps_0/y_in)/M_0,
x_out<=eps_0 exp(-A_0 t_box/2).

Hence x_out tends to0 as theta tends to pi. The limiting point(0,eps_0) on the y-axis flows to radius R_1 in a finite time H_1, again by positivity on a compact axis segment. Its crossing is transverse. Nearby exit points therefore reach that circle within H_1+1. Time inside the small square is not counted in K. The total occupation of K is at most t_1+H_1+2 for all theta sufficiently close to pi. Together with the other endpoint and compact middle angles, this proves a finite uniform bound tau_*.

These arguments hold for every sufficiently small choice of eps_0 and eps_P and every sufficiently large R_1 satisfying the stated conditions; the resulting tau_* can depend on all three choices. The same conclusion for a smaller requested outer radius follows by bounding its occupation set by the one for an enlarged radius R_1. This avoids assuming without justification that an arbitrarily chosen source semicircle lies inside the original R_0 disk.

## 5. Weighted transport and the maximal domain

Let S_t f=f composed with phi_t on Q. Liouville's formula gives det Dphi_t=exp(2c_l t). The weight hypothesis and a change of variables give

||S_t f||_w^2=exp(-2c_l t)integral_Q |f(Y)|^2 w(phi_(-t)Y)dY
 <=exp((beta-2c_l)t)||f||_w^2.

The family S_t is a strongly continuous semigroup on L^2_w. To check continuity, first use continuous compactly supported functions: nearby flow maps have a common compact support and uniform convergence, while w is bounded on that compact. Such functions are dense in L^2_w, by truncation and smoothing inside Q. The uniform operator bound for t in a small interval extends continuity to every vector.

For each f, the vector-valued Bochner integral R_-f=-integral_0^infinity exp(-t)S_t f dt exists because ||exp(-t)S_t||<=exp(-kappa t). Write R_T for the bounded operator obtained by integrating up toT. The operators R_T converge in operator norm, with tail at most exp(-kappa T)/kappa, to R_-. This does not assert Bochner measurability of t maps to S_t in the operator-norm topology. The limit has norm at most1/kappa. Differentiation in distributions, or first on smooth compactly supported test data followed by approximation, gives

(V dot grad-1)R_T f=f-exp(-T)S_T f.

Here V dot grad h means div(Vh)-2c_l h as a distribution on Q. The maximal-domain operator is closed: weighted convergence implies local L^2 convergence, so both this distribution and its proposed L^2_w value pass to the limit. Consequently R_-f is in the maximal domain and solves the equation.

We justify the characteristic identity on the maximal distributional domain directly. This avoids differentiating a merely C^1 flow-box Jacobian in a transverse direction. Suppose h,g are in L^p_loc(Q), 1<=p<infinity, and V dot grad h=g in distributions. Fix compact sets K inside the interior of K' inside Q, with positive separation, and use a smooth nonnegative unit-integral mollifier eta_epsilon supported in the epsilon disk. On K let h_epsilon=h*eta_epsilon. Direct distributional integration by parts gives

V dot grad h_epsilon=g*eta_epsilon+r_epsilon,
r_epsilon(X)=integral [(V(X)-V(Y)) dot grad eta_epsilon(X-Y)+(div V)(Y)eta_epsilon(X-Y)]h(Y)dY.

The bracket integrates to0 in Y. Subtracting h(X) inside that integral, the C^1 bound on V gives

||r_epsilon||_(L^p(K)) <= C sup_(|z|<=epsilon) ||h(.-z)-h||_(L^p(K')) -> 0.

Here C is independent of epsilon: the first kernel has uniformly bounded L^1 norm since |V(X)-V(Y)|<=C|X-Y|; the divergence kernel does also. Local translation continuity follows by extending h from a larger compact neighborhood and multiplying by a cutoff equal to1 near K'. This proves the displayed convergence, including p=1.

Fix any compact initial patch and a finite flow-time interval. Its flow tube is compact in Q. For the smooth h_epsilon, the ordinary chain rule gives

h_epsilon(phi_t X)-h_epsilon(X)=integral_0^t (g*eta_epsilon+r_epsilon)(phi_s X)ds.

The Jacobian and inverse Jacobian are uniformly bounded on this finite tube. Thus both sides converge in L^p on the initial patch, uniformly for t in the finite interval, to the identity with h and g. This supplies an absolutely continuous L^p-valued orbit representative; Fubini supplies an absolutely continuous representative along almost every orbit in the patch. Exhaustion by countably many patches and time intervals gives the characteristic identity for every fixed finite time, almost everywhere. No nonvanishing assumption on V is needed for this mollifier argument.

For a homogeneous maximal-domain solution, take g=h. The resulting integral equation, or multiplication by exp(-t), gives S_t h=exp(t)h. Therefore

||h||_w<=exp(-kappa t)||h||_w,

forcing h=0. Applying this uniqueness to h-R_-(V dot grad-1)h proves the left-inverse identity on the maximal domain. Together with the right inverse already proved, this establishes the two-sided inverse. None of this argument requires the global section. Distributional statements are on Q; no classical density trace on an axis follows.

For the weighted supremum define X_m={h measurable: ess sup_Q |h|/m<infinity}, modulo equality almost everywhere, and D_m={h in X_m: V dot grad h is represented by an element of X_m}. The C^1 bound on log m gives m(phi_t X)<=exp(beta_m t)m(X). The pointwise time integral defining R_-f exists for almost every X by Fubini and this bound, and gives

||R_-f||_(X_m)<=||f||_(X_m)/(1-beta_m).

For a finite T, R_T f obeys the same distributional identity as in L^2, by local approximation on finite flow tubes, and exp(-T)S_T f tends to0 in X_m. The local distributional closedness then gives the right inverse in D_m. A homogeneous solution satisfies S_t h=exp(t)h by the mollifier argument, since h is locally L^2. The weighted supremum bound gives ||h||_(X_m)<=exp(-(1-beta_m)t)||h||_(X_m), proving uniqueness and the left inverse. No strong continuity on all of X_m is assumed. For continuous data the integral and its characteristic identity are pointwise.

On compactly supported smooth h, integration by parts separately verifies

Re integral (V dot grad h-h) conjugate(h) w dX
 =integral [-(1+c_l)-(V dot grad log w)/2]|h|^2 w dX

when w is C^1. This identity checks the sign and the factor1/2 in the weight condition.

## 6. The bounded orbit correction

Let a_0=2(T_0+kappa), and assume C_kappa<infinity. Define

psi(X)=sup_(s>=0) integral_(-s)^0 a_0(phi_tau X)dtau.

For fixed s the integral is continuous in X. Thus psi is lower semicontinuous and measurable. The zero-length segment gives psi>=0, and the segment bound gives psi<=C_kappa. For t>=0, use s=s'+t in the supremum at phi_t X. Changing integration variables gives

psi(phi_t X)>=psi(X)+integral_0^t a_0(phi_tau X)dtau.

With X=phi_(-t)Y and w=w_0 exp(psi), integrate V dot grad log w_0=-2(T_0+1+c_l) along the backward segment. The preceding inequality then gives exactly

log w(phi_(-t)Y)-log w(Y)<=2(1+c_l-kappa)t.

The weight is locally bounded above and below because w_0 is and psi is bounded. Section5 applies with beta=2(1+c_l-kappa), giving ||R_-||_w<=1/kappa. The equivalence of the two weighted norms yields

||R_-f||_(w_0)<=exp(C_kappa/2)||f||_(w_0)/kappa.

No derivative of psi or classical smoothness of w has been asserted or used.

If T_0 has finite global supremum, T_0+kappa is nonpositive off K, and the total time in K is at most tau_*, every orbit segment has integral at most2tau_* sup_Q(T_0+kappa)^+. This proves the finiteness criterion. Negative limiting margins are useful only when they give uniform neighborhood inequalities, including near the axes. To use strict endpoint limits, first choose kappa below the negative of each of the three limiting margins. Choose a corner neighborhood, a source neighborhood and an exterior neighborhood on which T_0+kappa<=0. Then shrink eps_0 and eps_P to lie inside these neighborhoods and satisfy the dynamical conditions of sections2 to4, and enlarge R_1 to include the bounded complement of the exterior neighborhood. Only after these choices obtain tau_* from section4. Compactness and continuous extension to the remaining axis pieces give a finite supremum of T_0 on K for the conic weights. A qualitative finite C_kappa proves existence of a finite transport inverse bound, but supplies no certified value of that bound.

## 7. Conic weights, endpoint margins and the extra tail hypothesis

Let a,b>0, S=a+b, gamma real, R>0 and p>0. Set

w_0=|x|^(-2a)|y|^(-2b)(1+(r/R)^p)^(2(S-gamma)/p).

Equivalently w_0=|cos theta|^(-2a)|sin theta|^(-2b)M(r), where

M(r)=r^(-2S)(1+(r/R)^p)^(2(S-gamma)/p),
-(r/2)M'(r)/M(r)=mu(r)=gamma+(S-gamma)/(1+(r/R)^p).

Writing s=X dot V/r^2, direct logarithmic differentiation gives

T_0=-(1+c_l)+a(V_1/x-s)+b(V_2/y-s)+mu(r)s.

Near0 the form T_0=-(1+c_l)+aV_1/x+bV_2/y+(mu-S)s and continuity of the quotients imply the direction-independent limit

T_corner=-(1+c_l)-aA_0+bD_0.

Indeed s is bounded and mu-S tends to0. At P, s and V_1/x tend to0, whereas V_2/y tends to mu_P. The radial factor is smooth there, so

T_source=-(1+c_l)+b mu_P.

To obtain a UNIFORM full-quadrant far limit, add the explicit hypothesis

sup_(theta in(0,pi/2)) (|U_1/x|+|U_2/y|) -> 0,
V=c_l X+U.

Then s tends uniformly to c_l and

T_far=-(1+c_l)+gamma c_l=-kappa_inf.

The weaker estimate |U|=O(r^k) by itself does not control these component quotients uniformly near an axis. A sufficient quantitative condition is |DU(X)|=O(r^(k-1)) at infinity with the stated parities, together with |U|=O(r^k): if x<=r/2, integrate partial_x U_1 from0 to x along a segment whose radius is at least(sqrt(3)/2)r; if x>r/2 use |U_1|/x<=2|U|/r. Apply the analogous argument to U_2/y. Thus these two explicit bounds give quotient decay O(r^(k-1)). Finite angular power-tail formulas for the actual trial can also verify the stronger hypothesis, but no such global numerical check is supplied by this note.

For the exactly normalized modal scalar c_l=1/k, c=3/k-1, the saddle rates are A_0=2/k-1 and D_0=4/k-1. At a=129/20,b=307/100,gamma=1129/1000 and k equal to the pinned exact modal rational, all three illustrative margins with mu_P=1 are strictly negative. The mu_P=1 source value is a frozen illustration; an actual source enclosure can be substituted with outward rounding. The arithmetic certificate also substitutes the previously independently certified actual modal source enclosure for mu_P, verifies0<mu_P<1 and obtains a strictly negative actual source margin. This uses the pinned source_result.json and its pinned output_audit.json. The actual numerical flow assumptions remain separate.

For the coupling principal symbol, a separate elementary calculation gives

b(X,xi,eta)=(rho_x xi eta-rho_y xi^2)/(xi^2+eta^2),
max_(xi^2+eta^2=1)b=(sqrt(rho_x^2+rho_y^2)-rho_y)/2.

This follows by finding the larger eigenvalue of the symmetric2by2matrix with entries(-rho_y,rho_x/2;rho_x/2,0). It is a pointwise symbol identity only. In particular the measurable orbit weight from section6 does not automatically have the differentiability needed for a smooth pseudodifferential sharp Garding argument. No such coupled weighted estimate is established here.

## 8. A rigorous lower bound from the far dilation

Fix a compact angular interval I contained in(0,pi/2), a nonzero smooth angular bump a_I supported inside I, and a nonzero real smooth bump chi supported in(0,1). Put t=log r, choose L tending to infinity and T tending to infinity, and define

h_(T,L)(r,theta)=r^(gamma-1)L^(-1/2)chi((log r-T)/L)a_I(theta).

These are smooth functions of compact support inside Q. Under the reference asymptotic measure r^(-2gamma)b(theta)r dr dtheta, their squared norm is the fixed positive number

integral_0^1 chi(v)^2 dv times integral_I a_I(theta)^2 b(theta)dtheta.

The actual norm differs by a factor tending uniformly to1 as T tends to infinity. The same statement holds for the norms estimated below, since every support has r>=exp(T).

For the dilation field c_l X, direct differentiation gives

(c_l r partial_r-1)h_(T,L)=-kappa_inf h_(T,L)
 +c_l r^(gamma-1)L^(-3/2)chi'((t-T)/L)a_I(theta).

The second term has norm at most C/L times the fixed h norm. On I, the Euclidean gradient obeys

|grad h_(T,L)|<=C r^(gamma-2)L^(-1/2)(|chi|+|chi'|/L).

The angular derivative of a_I is included in C. Consequently the O(r^k) velocity error contributes a norm at most C exp(-(1-k)T)(1+1/L). Let T=L tend to infinity. We have proved

||(V dot grad-1)h_(L,L)+kappa_inf h_(L,L)||_w / ||h_(L,L)||_w -> 0.

If a bounded two-sided inverse R exists, h=R(V dot grad-1)h gives 1<=||R|| times the limiting ratio kappa_inf. This proves ||R||>=1/kappa_inf when kappa_inf>0. When kappa_inf=0 the same sequence contradicts bounded invertibility. Reflection of the compact angular bump into the other quadrants with any desired parity gives the same ratio for the parity subspace on the plane.

This argument uses no numerical orbit integration, no high-order tail derivative, no source equilibrium and no topological flow hypothesis. It needs the stated weight asymptotics and the O(r^k) field error on a fixed angular sector. It does not give a lower bound for the inverse of V dot grad-1 plus the nonlocal coupling and normalization terms.

## 9. Verification plan and scope

The code will independently evaluate the exact scalar margins and kappa_inf by rational arithmetic, Arb and a differently arranged mpmath.iv formula. It will check the conic logarithmic derivative in exact rational variables, the orbit-correction inequality on exact finite piecewise-constant paths as an algebraic contract, and the symmetric-matrix symbol identity. These contracts do not prove the planar topology or the infinite-time functional analysis; those are proved above under explicit standard dependencies.

No certified H1 to H4 data, finite tau_*, orbit cost C_kappa, actual conic supremum, smooth weight suitable for a global Garding theorem, coupled IPM inverse, derivative estimate, contraction, existence, exclusion or decisive endpoint follows here. The current trial's forcing-space center obstruction remains in force.
