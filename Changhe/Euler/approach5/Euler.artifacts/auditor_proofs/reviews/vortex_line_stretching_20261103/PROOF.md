# Material vortex lengths and a necessary loss of directional regularity

Status: A579-A581 CONFIRMED after full independent reconstruction and proof postread. The unconditional statements below concern vortex geometry. The derivative conclusion retains its geometric and Holder hypotheses. Verdicts are recorded separately in the auditor's ledger (AUDIT_LEDGER.md).

## 1. Hypotheses, notation and exact transport

Let U in C2(R3;R3) and P in C1(R3) solve

    (1-c)U+DU(Ay+U)+omega JU+grad P=0, div U=0,
    A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0), 0<c<1,
    M=sup_R3 |U|<infinity, B=Ay+U, W=curl U, S=sym DU.

Omega, used for vorticity in some source files, is denoted W here to distinguish it from the rotation parameter. Every finite real omega is allowed. The C1 field B has a complete flow Phi_s by its linear growth. Curling the equation gives [B,W]=-(1+c)W and therefore

    D Phi_s(y) W(y)=exp((1+c)s) W(Phi_s y).             (1)

This follows by differentiating both sides in s and comparing their linear equations and initial values. In particular a nonzero W stays nonzero on a B-orbit. No global completeness of the W-flow is needed below.

On {W!=0}, xi=W/|W| is C1. A compact positive vortex segment has tangent xi and nonzero W including its endpoints. Let L be its arclength, K=integral |(xi.grad)xi| dl its total curvature and D=log(max |W|/min |W|). Since div W=0,

    d_l log |W|=-div xi, D<=integral |div xi| dl,
    |(xi.grad)xi|<=|Dxi|_F, |div xi|<=sqrt(3)|Dxi|_F.  (2)

All line integrals count arclength with its parametrization. The assertions do not require an embedded segment.

## 2. The exact two-sided estimates

Along the segment d_l(U.xi)=xi.S xi+U.(xi.grad)xi. Thus

    integral xi.S xi dl=[U.xi]_endpoints
                         -integral U.(xi.grad)xi dl,
    |integral xi.S xi dl|<=(2+K)sup_segment |U|.       (3)

Parametrize an initial segment gamma_0(sigma), 0<=sigma<=sigma_1, by gamma_0'=W(gamma_0), and put gamma_s=Phi_s gamma_0. Equation(1) gives partial_sigma gamma_s=exp((1+c)s)W(gamma_s). If L(s) is its length, differentiating the tangent norm yields

    L'(s)=integral_gamma_s (c+xi.S xi)dl,
    integral_0^sigma_1 |W(gamma_s)|d sigma=exp(-(1+c)s)L(s).  (4)

The skew term -omega J has zero quadratic form. Write M_s=sup_gamma_s|U|, K(s),D(s) for its geometric quantities, L0=L(0), and w0_minus,min_gamma_0|W| and w0_plus,max_gamma_0|W|. Define for s>=0

    E(s)=integral_0^s exp(-c tau)(2+K(tau))M_tau d tau.

Integration of(3)-(4) gives

    exp(cs)(L0-E(s))<=L(s)<=exp(cs)(L0+E(s)),         (5)
    |W|<=exp(D(s))w0_plus exp(-s)(1+E(s)/L0),
    |W|>=exp(-D(s))w0_minus exp(-s)(1-E(s)/L0)        (6)

at every point of gamma_s. To obtain(6), compare each value of |W| with its sigma-average, using the multiplicative oscillation exp(D(s)), and use L0/sigma_1 in [w0_minus,w0_plus]. When E(s)>L0 the stated lower bound is negative and hence automatic; no positive lower decay estimate is claimed then. These estimates are independent of helicity and velocity decay.

Suppose at some point of gamma_0 and some tau>0,

    |W(Phi_tau y)|>=exp(mu tau)|W(y)|,
    mu>-1, (1+mu)tau>D(0)+D(tau)=D_total.

Then min_gamma_tau|W|>=exp(mu tau-D_total)w0_plus. The sigma averages and(4) imply L(tau)>=L0 exp((1+c+mu)tau-D_total). Comparing with(5), and bounding K and M on the whole time window by Kstar,Mstar, proves

    L0 <= (2+Kstar)Mstar(1-exp(-c tau))
             /[c(exp((1+mu)tau-D_total)-1)].          (7)

For tau=1, Kstar<=1, and either mu0,D_total<=1/2 or mu=-1/4,D_total<=1/4, the right side is at most3.82 Mstar whenever2/5<=c<=1/2. Here is an exact check instead of a parameter grid. The function (1-exp(-c))/c=integral_0^1 exp(-ct)dt decreases in c. The alternating Taylor polynomial through degree5 at2/5 is a strict lower bound for exp(-2/5); the Taylor polynomial through degree4 at1/2 equals211/128 and is a strict lower bound for exp(1/2). Substitution gives

    3[1-sum_(j=0)^5 (-2/5)^j/j!]/[(2/5)(211/128-1)]<191/50.

The displayed left side is14835840/3890625; comparison with191/50 has positive cross-multiplication difference1317375. This is an inequality between rational numbers. No approximate exponential evaluation is used as proof.

## 3. Conditional far-field consequences

Fix R1>=2M/c, with R1>0. Every exterior B-orbit increases in radius, and every exterior point is Phi_s y0 for |y0|=R1 and s>=0. The radial inequalities cr-M<=r'<=cr+M give

    |cs-log(r/R1)|<=1.                               (8)

Let theta>-1/c. Suppose there are positive constants Lstar,wstar,Kstar,Dstar such that every vortical point of this sphere lies on a compact vortex segment satisfying L0>=Lstar,w0_plus<=wstar and, for all s>=0,

    K(s)<=Kstar exp((1+c+c theta)s), D(s)<=Dstar.      (9)

Then

    E(s)<=M[2(1-exp(-cs))/c
              +Kstar(exp((1+c theta)s)-1)/(1+c theta)].

Equations(6),(8) give |W(y)|<=C(1+|y|)^theta outside the sphere. Points with W=0 satisfy the same estimate. If K is bounded in s, the same argument instead gives |W(y)|<=C|y|^(-1/c). If D(s)<=Dstar+c theta_D s, its additional factor adds theta_D to the exponent, with the stated bound understood on the nonnegative oscillation D. Neither(9) nor its uniform choice of segments follows from bounded U.

For completeness, the local logarithmic estimate used for the derivative consequence is proved here. For0<alpha<1 put w=sup_B(y,3)|W|, H=[W]_C^alpha(B(y,3)), M3=sup_B(y,3)|U|. Then

    ||DU(y)||<=C_alpha[M3+w(1+log^+(H/w))].           (10)

The product term is0 if w0. To see this, choose a smooth cutoff chi supported in B(y,3), equal1 on B(y,2), put Gamma(x)=1/(4pi|x|), Z=Gamma*(chi W), V=curl Z. Since -Delta Gamma=delta and div W0,

    curl V=chi W+grad div Z,
    div Z=Gamma*(grad chi.W),

and div Z is harmonic on B(y,2). Thus h=U-V is harmonic there, by div h0 and curl h=-grad div Z, while |V|<=Cw. Interior harmonic estimates give |Dh(y)|<=C(M3+w). The derivative DV is a trace contact term plus a homogeneous mean-zero singular integral. Inside radius epsilon<=1 subtract W(y); its bound is C_alpha H epsilon^alpha. Between epsilon and3 its bound is Cw log(3/epsilon). Taking epsilon^alpha=min(1,w/H) proves(10), with the H0 cases interpreted directly.

Assume(9), theta<1/2, and in addition [W]_C^alpha(B(y,3))<=C(1+|y|)^N for a fixed finite N>=0. If w>=r^-1, the logarithm in(10) is O(log r). If w<r^-1, the elementary bound for w log^+(Cr^N/w) is O(r^-1 log r), after increasing r. Thus

    ||DU(y)||<=C(1+r)^max(theta,0) log(2+r)=o(sqrt r).

The confirmed A498 bounded-velocity derivative screen gives DU->0 for0<c<1. A492 and A476 then give |W|+||DU||<=C/(1+r). This is a conditional derivative theorem. Its geometric and polynomial Holder assumptions have not been established for bare velocity decay.

## 4. A necessary loss of directional regularity

Now assume U->0 and2/5<=c<=1/2. Put m(R)=sup_(|z|>=R)|U(z)|. Choose r0>=2R1 so3.9m(r/2)<=r/2 for r>=r0. If |y|=r>=r0, W(y)!=0 and

    |W(Phi_1 y)|>=exp(-1/4)|W(y)|,                  (11)

then m=m(r/2)>0. If a compact forward vortex segment gamma_0 beginning at y has length3.9m, let Gamma_y be the material ribbon Phi_s gamma_0 for0<=s<=1. Then

    sup_Gamma_y |Dxi|_F>=1/(100m).                   (12)

Every point of gamma_0 is at distance at most3.9m from y, hence at radius>=r/2>=R1; all its forward B-orbits remain outside that radius. Thus M_s<=m. Suppose the supremum in(12) were smaller. Initially K(0)<.039. While K<=1, equations(5) and monotonicity in c give for0<=s<=1

    E(s)<=3m(1-exp(-c))/c<2.48m,
    L(s)<=m[3.9exp(c)+3(exp(c)-1)/c]<10.4m.          (13)

For the second bound both summands increase in c, so their maximum is9.9exp(1/2)-6. The exact series bound exp(1/2)<33/20 gives this expression<10.335. For example its degree4 partial sum is211/128 and its remaining positive terms sum to at most1/3520. The first bound follows from the degree3 alternating lower bound on exp(-2/5). These joint estimates avoid combining incompatible separate maxima. Consequently K(s)<.104 on this whole time window by continuity. Equation(2) gives

    D(0)+D(1)<sqrt(3)(3.9+10.4)/100<1/4,

where squaring reduces the last inequality to3(143/10)^2<625. Equation(7) contradicts3.9m<=3.82m, proving(12).

There is an endpoint qualification. If the compact segment of length3.9m does not exist because the maximal forward arclength is finite and at most3.9m, then along that maximal curve

    sup |div xi|=infinity, and hence sup |Dxi|_F=infinity.  (14)

Indeed a finite-arclength curve is Cauchy at its forward endpoint q. If W(q)!=0, the arclength ODE extends it, contrary to maximality. Thus W(q)=0. The integral of |div xi| must be infinite by integrating d_l log|W|, although its interval of integration is finite. This also handles equality of the total arclength with3.9m when the endpoint is a zero and the compact segment is unavailable. The source's strict inequality alone misses that case.

If |W(Phi_s y0)| fails to tend to0 on an exterior B-orbit, there are arbitrarily large s satisfying(11) with y=Phi_s y0. Otherwise all sufficiently late unit steps would decrease by exp(-1/4); compactness of one time interval and iteration would force convergence to0. At every selected point either(12) holds on the stated compact ribbon or the finite-length alternative(14) holds. The finite-length curve stays within3.9m of that point. Since its radius tends to infinity, m tends to0. Thus the direction derivatives are unbounded on these nearby curves or ribbons. One must retain this disjunction instead of naming a nonexistent length3.9m ribbon.

## 5. Scope, dependencies and verification

The material identities, the window estimate and the alternative(12)-(14) use the full profile equation, bounded U, and only the extra decay and c-range explicitly stated. They hold for every finite omega. The numerical constants and algebraic transport do not involve omega; constants depending on a particular profile's geometric bounds are not claimed universal across profiles.

The separate circulation estimate in C43 section5 follows if an oriented flux obeys Gamma>=phi r^-b>0 and Gamma>=theta|W(y)|L^2, while Stokes and |U|<=m on its boundary give Gamma<=mL. Then L>=Gamma/m and |W(y)|<=m^2/(theta Gamma)<=m^2r^b/(theta phi). Those geometric hypotheses are extra, and no Kelvin argument supplies them here.

No Deng-Hou-Yu or Constantin-Fefferman-Majda theorem or historical attribution is needed or certified. The numerical tests in the source are not used. Every exponential constant above is checked by an explicit Taylor bound and a rational inequality. No computation was needed. The full actual configured-model source was read and its proof reconstructed, with continuing file exchange through in the team records. A498,A492,A476 are the only later derivative-screen inputs; they are not inputs to the geometric estimates.
