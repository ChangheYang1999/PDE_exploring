# Historical flat periodic orbits: exact scope of the local obstructions

## 1. Statements and hypotheses

Let0<c<1/2, a=1-2c, d=3c and kappa=1+c. Write Jy=e3 cross y, A=cI-omega J, B=Ay+U, W=curl U, g=U.B and H=P+|U|^2/2+(Ay).U. In the profile parts assume U in C2 on an open neighborhood and P in C1, div U=0 and

    (1-c)U+DU B+omega JU+grad P=0.

The equation makes P in C2 locally. Assume zero helicity U.W=0 wherever the level-set arguments are used. Direct identities are

    B cross W=grad H+aU,  BH=-ag,  WH=0,
    [B,W]=-kappa W,
    W(Phi_t x)=exp(-kappa t) D Phi_t(x)W(x).

Let Gamma be a nonstationary periodic B-orbit of period T, with W=DW=0, U nonzero, g=0 and H=H0 on Gamma. In the dynamical assertions also assume the stated flat covector law for a constant real rho,

    U(Phi_t x)=exp(rho t)D Phi_t(x)^(-T)U(x), x in Gamma.

The two cases are Q1: rho<=-2a and Q2: rho>=2-c. The no-periodic-vortex statement below is an additional supplied hypothesis, available in the global uniformly sublinear helicity-free profile class. It is not deduced from the local identities.

At this scope: the two transverse multipliers are positive, W vanishes on the local unstable cylinder and is tangent to the stable cylinder, all small regular H-level annuli have zero circulation, and their vortex flux forms have single-valued streamfunctions. In Q1 each stable-cylinder H-level circle has a W-zero. These facts do not exclude the orbit. A separate explicit analytic irrotational profile family realizes all the displayed on-orbit first- and second-order identities for every real rho and every omega!=0. It lacks vortical accumulation. A C1 transport model with vortical accumulation, zeros on level circles and no closed vortex orbit satisfies only the stated transport identities, not the full profile equation.

The pinned sources are the two historical coordinator notes and the complete supplied periodic-flat proof and answer. Every source, three scripts and the sixteen-check source output were read. The supplied answer reports that its attempted model invocation failed before execution; this audit does not upgrade that attempt to an actual model consultation. The configured coordinator's independent written check is separately present. No new client or computation was used.

## 2. Multipliers, cylinders and level loops

Since B is nonzero on Gamma, its tangent multiplier is1. The periodic covector law gives D Phi_T^T U=exp(rho T)U. The nonzero covector U annihilates B because g=0. Thus the quotient by ker U has multiplier exp(rho T). Since div B=d, Liouville's determinant formula gives the remaining transverse multiplier exp((d-rho)T). Both are positive. In Q1 the stable exponent is rho and the unstable exponent is d-rho; in Q2 these roles are exchanged. In both cases lambda_u>=2-c>kappa.

Let N and S be the local unstable and stable cylinders. For q in N, hyperbolicity gives, for every sufficiently small epsilon>0 and t>=0,

    dist(Phi_-t q,Gamma)<=C exp(-(lambda_u-epsilon)t),
    ||D Phi_t(Phi_-t q)||<=C exp((lambda_u+epsilon)t).

The full derivative estimate follows in a periodic Floquet frame: the coefficient matrix along the backward-asymptotic orbit approaches the periodic matrix; a sufficiently late portion has arbitrarily small perturbation, while the finite remaining portion changes only C. W is locally Lipschitz and zero on Gamma. Cauchy transport therefore bounds |W(q)| by C exp(-(kappa-2epsilon)t). Choosing2epsilon<kappa and taking t to infinity proves W=0 on N. Only W=0 and its Lipschitz bound on Gamma, not DW=0, were needed.

For q in S the normal quotient to TS expands forward at exponent lambda_u. If W(q) has nonzero normal component, the quotient form of Cauchy transport grows at least as exp((lambda_u-kappa-epsilon)t) for small epsilon>0. This contradicts boundedness of W along the forward orbit approaching Gamma. Hence W is tangent to S. This proof uses strict lambda_u>kappa.

On Gamma, dH=-aU is nonzero. It detects the transverse rho direction and kills both B and the d-rho direction. Consequently H|S is a submersion across Gamma in Q1, while H|N is such a submersion in Q2. Positivity of the multipliers removes the possible twisted normal line bundle, and compactness gives nearby closed H-level circles on the indicated cylinder. In Q2, d(H|S)=0 along Gamma, so no analogous stable-cylinder level circles follow from this argument.

In Q1, W is tangent to S and annihilates H, so it is tangent to each such level circle. If W has no zero on one circle, its continuous nonzero speed has a positive minimum, giving a nonconstant periodic vortex orbit in finite time. The no-periodic-vortex hypothesis forces at least one zero on each circle. It does not imply W vanishes on the whole circle.

## 3. Circulation and the streamfunction qualification

Choose a small regular H-tube about Gamma. Its level surfaces are annuli. Put alpha=U.dy. For tangent vectors v,w to an H-level surface,

    d alpha(v,w)=W.(v cross w)=0,

because WH=0 and v cross w is normal to the level. Thus alpha is closed on each annulus. In Q1 both B and W are tangent to S, so the tangential restriction of B cross W vanishes and alpha|S=-d(H|S)/a. The distinguished essential loop in S has zero circulation. In Q2 the loop in N has zero circulation because W=0 on N and the same identity holds. A closed one-form on an annulus has all periods determined by one essential loop. Therefore alpha has zero integral over every closed curve in each sufficiently small H-level annulus.

The associated vortex streamfunction requires one further step, not identification of alpha with the flux form. In coordinates (h,theta,s), h=H-H0, write the volume form as dh wedge nu_h, where nu_h is the area form with its transverse density on the annulus. Since W is tangent to each level and divergence-free, beta_h=i_W nu_h is a closed one-form there. Transport a fixed essential loop between levels using a vector Z with ZH=1. Cartan's formula and d alpha=i_W volume give

    d/dh integral_loop(h) alpha
      = integral_loop(h) i_Z d alpha
      = -integral_loop(h) beta_h.

The left side is zero for all small h. Hence beta_h has zero essential period; its other periods vanish by closedness. There is a single-valued streamfunction psi_h with d psi_h=beta_h on each annulus. Kelvin circulation on these particular loops says only0=exp(-at)0.

For precision, the no-periodic-vortex hypothesis implies that a component of a regular-value level of psi_h cannot be a compact curve contained in the annulus interior: such a component would be a periodic vortex curve. A regular arc of a critical-value level may instead approach interior critical points. It need not meet the collar boundary. For example psi(theta,s)=s sin^2 theta on S1 times(-1,1) has the regular zero-level arcs s=0,0<theta<pi and pi<theta<2pi, ending at interior critical points. Thus the historical phrase that every regular level component reaches the boundary is valid with regular value, or with closure disjoint from critical points, specified. It must not exclude saddle or degenerate zero barriers at a critical value. This qualification preserves the intended conclusion that the streamfunction alone gives no flat-orbit exclusion.

## 4. Exact transport model and component accumulation

Take c>1/5 as well as c<1/2, sigma=2a, lambda=d+sigma, p=kappa/sigma>1 and theta in S1. For h>0 define

    phase=theta+log(h)/sigma,
    w=h^p sin^2(phase),
    Bhat=partial_theta-sigma h partial_h+lambda z partial_z,
    What=w partial_theta-z w_theta partial_z,

and set What=0 for h<=0. The first h-derivative of either coefficient is O(h^(p-1)) on bounded z sets; the other derivatives are O(h^p). Thus What is C1 across h=0 and its value and derivative vanish on the central orbit h=z=0.

The phase is Bhat-invariant. Hence Bhat w=-kappa w. Since partial_theta commutes with Bhat, the product rule gives Bhat w_theta=-kappa w_theta and

    div Bhat=-sigma+lambda=d,
    div What=w_theta-w_theta=0,
    [Bhat,What]=-kappa What.

With Hhat=h and ghat=sigma h/a one has Bhat Hhat=-a ghat, What Hhat=0 and dHhat wedge dghat=0. On every positive-h circle of z=0 there are zeros and nonzero arcs. Along a vortex curve h is constant and theta'=w>=0. At a barrier sin(phase)=0, both w and w_theta vanish, so What=0 for every z. Uniqueness for the C1 vector field prevents crossing a barrier in finite time. A nonconstant vortex trajectory therefore cannot close, even when z!=0. Nevertheless the central periodic orbit belongs to the closure of nonzero What.

This model has product volume; no assertion makes it a Euclidean curl field of U with Bhat=Ay+U. It confirms only a limitation of transport, flatness, rank and no-closed-vortex arguments.

The independent linear carrier Bhat also has the open invariant set h>0,z>0 accumulating on the central orbit and disjoint from both invariant cylinders. Thus invariant open-set accumulation does not force intersection with either cylinder. In a genuine profile the closure of the whole vortical set need not be replaced without proof by the closure of one specified vortical component. If a specified component meets S, the inclination argument supplies limiting unstable pieces in its closure, which is consistent with W=0 on N.

## 5. Rank identities and intersections with the cylinders

Assume additionally dH wedge dg=0 on the closure of a particular vortical component E. Near Gamma define the continuous scalar

    r(x)=-a (grad g.grad H)/|grad H|^2.

Since BH=-ag, the rank identity gives Bg=r(x)g. The flat gradient law grad g=rho U and grad H=-aU on Gamma give r=rho there. In Q1, a nonzero g along an orbit in closure(E) intersect N would grow without bound backward as the orbit approaches Gamma, since r is uniformly negative sufficiently near Gamma. This contradicts g tending to0 there. Therefore g=0 and, by BH=-ag and convergence, H=H0 on that intersection. In Q2 the same proof runs forward on closure(E) intersect S, since r is positive. These are conclusions only on the stated intersections.

On a submersion coordinate box contained in W!=0, the same rank identity says g=f(H). It does not provide one function across disconnected pieces or across an irrotational gap. The scalar example H=h, g=f(h)+chi(z), where chi(z)=exp(-1/z^2) for z<0 and0 otherwise, has zero rank defect on z>=0, flat at the separating plane, while the rank identity fails in the other half. This refutes only the continuation inference from the rank identity, not the full profile equations.

## 6. The exact irrotational family with arbitrary rho

Fix any0<c<1/2, omega!=0, real rho and R>0. Put

    m=2c-rho,
    ell=-R^2(rho/2+3m^2/(8c)),
    b0=-m/4+3m^2/(8c),
    q0=-3m^2/(32cR^2),
    phi=ell log(r/R)+b0(r^2-2z^2)
         +q0(r^4-8r^2z^2+(8/3)z^4),
    U=grad phi,
    P=-a phi-|U|^2/2-(Ay).U,

on the domain r=sqrt(y1^2+y2^2)>0. The three potential terms are harmonic: Delta log r=0, Delta(r^2-2z^2)=0 and the quartic Laplacian is16r^2-8(4z^2+2r^2)+32z^2=0. Thus U is analytic and divergence-free, W=0 and H=-a phi. Writing M=Hess phi, differentiation gives grad P=-aU-MB-A^TU. The momentum left side becomes (1-c-a)U+omega JU-A^TU=0. This is an exact local solution, with its full pressure determined.

On Gamma={r=R,z=0}, direct substitution yields

    U=-cR e_r, B=-omega R e_theta,
    M=diag(rho-c,-c,m),
    phi_rrr=-(rho+3m^2/c)/R, phi_rzz=3m^2/(cR).

In particular Gamma is periodic with period2pi/|omega|, g=0 and H constant. In cylindrical carrier equations theta'=-omega, r'=cr+phi_r and z'=cz+phi_z, the transverse linearization is diag(rho,3c-rho). These are Floquet exponents. They are not the pointwise eigenvalues of DB in a fixed Cartesian frame; one has det(DB-lambda I)=(3c-rho-lambda)(lambda^2-rho lambda+omega^2).

Let N0=(rho-c)^2+c^2+m^2=|M|^2. Since

    g=phi_r(cr+phi_r)+phi_z(cz+phi_z),

one obtains grad g=rho U and the diagonal Hessian entries

    g_rr=-cR phi_rrr+2rho(rho-c)=rho(rho-c)+2N0,
    (Hess g)_theta,theta=g_r/R=-c rho,
    g_zz=-cR phi_rzz+2cm+2m^2=rho m.

All mixed entries vanish by axisymmetry and evenness in z. Therefore

    Hess g=rho M+(2|M|^2/|U|^2)U tensor U,
    Hess H=-aM.

The covector law also holds on Gamma: differentiating U along its rotation gives dU/dt=-DB^T U+rho U, as is seen directly in the (e_r,e_theta,e_z) frame. Its integrated form is the one in Section1. The rank defect dH wedge dg is zero, and differentiating it once leaves canceling M terms and a wedge of parallel U covectors. Thus its first derivatives vanish too.

Every real rho is allowed, including both Q1 and Q2. For omega=0 the formulas still solve the equation, but Gamma is a circle of equilibria, not a nonstationary periodic orbit; no period is asserted in that case. W is zero throughout the domain, so no point of Gamma is in the closure of W!=0. The fields are not globally smooth through the axis or uniformly sublinear at infinity. These are exact local tests of specified on-orbit identities only.

## 7. Second-order redundancy and precise limitations

At any point with W=DW=0, M=DU is symmetric and traceless and D2U is a fully symmetric tensor, trace-free in each pair by div U=0. Put F=A+M and T_v=(v.grad)M. Direct differentiation gives

    Hess g=T_(B+U)+MF+F^TM,
    Hess P=-(1-c)M-T_B-MF-omega JM,
    Hess H=Hess P+M^2+T_B+MA+A^TM=-aM.

Thus Hess H=-aM is redundant with differentiated momentum at this flat jet. The trace of Hess g is2|M|^2; the trace of the flat Hessian formula in Section6 is the same identity. It supplies no additional rate restriction.

The historical pointwise tensor-completion observation also has its stated limited meaning. If B,U are orthogonal and nonzero, prescribing the symmetric trace-free contractions T_B and T_U requires T_B U=T_U B. Given this compatibility, all tensor components in an orthogonal frame (B,U,n) are fixed except T_nnn; the remaining trace equation fixes that one. The two other trace equations hold by the prescribed trace-free contractions. This constructs a pointwise harmonic cubic tensor. It alone constructs neither periodic first-jet data nor a neighborhood profile. Section6 separately supplies actual local examples with arbitrary rho for the specific on-orbit equations.

The endpoint stable-cylinder reasoning in coordinator_own Section4 was explicitly unfinished for Q2. This audit does not turn it into a new theorem. In the Q1 subcase where stable decay and flatness remove the flow-direction component of W, the remaining strong-stable component is removed by WH=0 because H is transverse to that direction. At an equality exponent, an exact contraction estimate without an epsilon loss needs the additional one-dimensional return-map distortion argument already identified in the historical note. The elementary epsilon-loss estimates of Section2 alone do not prove that endpoint.

The family and model therefore establish limitations of the named arguments, not nonexistence or existence of a globally smooth decaying vortical profile. They do not classify every restriction imposed by vortical accumulation, solve the flat-orbit witness problem or settle the unrestricted arbitrary-helicity conjecture. Those questions remain OPEN. No numerical or symbolic computation was executed in this audit; the direct proof, rather than the source script outputs, establishes the formulas.
