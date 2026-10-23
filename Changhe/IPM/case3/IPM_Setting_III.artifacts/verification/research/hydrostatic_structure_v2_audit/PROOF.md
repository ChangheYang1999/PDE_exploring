# Repaired hydrostatic statement, complete independent audit (194)

Written 2026-10-21T09:26:37.049786+00:00, before the v2 verification program. The exact audit target is the frozen body/app v2 identified in verification/INPUTS.json. The mathematical statement and complete independent argument from result193 are reproduced below. The audit confirms their applicability to v2 and checks every additional qualification. This remains a result about the separately defined hydrostatic class, not the original full-plane IPM endpoint.

## Additional hypotheses and conclusions of the repaired text

The expansion premise is now g_D=y+D u+O(D^2) in C^1 on each compact set, c=1+D, with V[g_D]=D V[u]+O(D^2) uniformly on each compact set. The coefficient u is C^2, has even-x/odd-y parity, growth exponent q in (1,2), and a convergent vertical curvature tail. Multiplying the two expansions is legitimate uniformly on compacts. Its coefficient of D is x u_x+y u_y+y+V_2[u]-u. Hence the already proved first-order obstruction applies. No uniform far-field remainder is asserted.

For conditionally convergent tails define A(x)=integral_0^infinity u_xx(x,t) dt. At y=1, the inverse formula gives V_2[u](x,1)=A(x)-integral_0^1(1-t)u_xx(x,t)dt. Thus A is continuous because the equation represents V_2[u] as a continuous function. The first y derivative equals A(x)-integral_0^y u_xx(x,t)dt and is jointly continuous. Odd extension has no jump in that derivative, so its second distributional derivative is -u_xx. This is the required integration-by-parts justification without an unproved uniform-tail hypothesis.

The homogeneous subtraction u-u_y(0)y preserves the homogeneous differentiated equation, parities, growth and tail integrability. The function y is not a solution of the inhomogeneous first-order equation. A tempered distribution supported on eta=0 has finite normal order by the Taylor-cutoff argument reproduced below. Polynomial coefficients in physical y are continuous by pairing with finitely many compactly supported smooth test functions whose polynomial moment matrix is invertible. No pointwise restriction of an arbitrary distribution is used.

For the conditional moment statement put e(t)=g_xx(0,t)-Q t^(p-2), assume integral_0^infinity t|e(t)|dt<infinity, and m0=integral_0^infinity t e(t)dt. Direct subtraction in the inverse yields exactly

V_2(0,y)-Q y^p/[p(1-p)]-m0 = -integral_y^infinity (t-y)e(t)dt.

Its absolute value is at most integral_y^infinity t|e(t)|dt, which tends to zero. This identity is proved; use of m0 within a full density expansion is formal. A homogeneous curvature Q_d y^(d-2) has a weighted core integral proportional to integral_0^y t^(d-1)dt. When Q_d is nonzero and d<=0 this is divergent. At d=0, replacing the small-t part by a regular core produces Q_0 log y plus a matching constant and the tail contribution Q_0. A zero Q_d supplies no such axis term. Thus c=n/(n-1) is a possible logarithmic degree, not a theorem that a logarithm is present.

The isopycnal transport coefficient is c x+H(x,sigma), and H_x in that equation is taken at fixed sigma. The equation gives no sign estimate for Z_x and supplies no exclusion using a maximum principle. It does not rule out every possible maximum-principle method. The whole-circle comparison trace is K sgn(sin theta)|sin theta|^p. For p<1 and K>0 it violates the proved O(|sin theta|) bound near the horizontal axes, while its behavior near the vertical axis is not excluded.

Dilation maps solutions to solutions exactly. At C^2 regularity its tangent g-X.grad g is only guaranteed C^1, so a classical velocity for that tangent is not automatic. All asserted operator-kernel language is formal. At nonzero parameter variation c1, the leading variation -c1 p^2 r^p Theta log r fails a strict O(r^p) bound because Theta(pi/2)=K>0. This says nothing about spaces allowing logarithmic growth. Compatibility of axis functions and the far-field trace with a global solution remains open. The compactness statement retains a common growth constant, common gamma<1, local third-derivative bounds and c_n tending to c>1; it concludes C^2 local convergence only.

## Scope and independent verification

The mathematical argument below was completed before its 58 exact/manufactured checks. The present comparison adds source freezing, preservation checks for all six displayed formulas, and direct algebra checks for the newly explicit premise, conditional-tail identity and moment remainder. The actual Opus5.5 lead's hand review is frozen as evidence of collaboration. The external referee review reports that its own requested Bedrock consultation lacked credentials; that failed request is not counted as a model review. No original YES or NO follows.

## Reproduced complete argument and dependencies

# Hydrostatic structure, far field and the regular c=1 obstruction

Written 2026-10-21, before the independent verification code. This is result193. It audits the exact v1 body and appendix of proposed3.74, frozen in verification/INPUTS.json. The argument below was independently reconstructed. It concerns the limiting hydrostatic problem, not an established limit or a solution of full-plane Setting III.

## Statement, hypotheses and dependencies

Write X=(x,y), r=|X|, E=X.grad, c>1, p=1/c, D=c-1 and A=2c-1. Assume g in C2(R2), even in x and odd in y, g_y(0)=1, and one C and 0<gamma<1 such that

    |g| <= C(1+r)^gamma,
    |grad g| <= C(1+r)^(gamma-1),
    |g_xx| <= C(1+r)^(gamma-2).

For y>=0 set

    h=T1 g=-int_y^infinity g_x(x,t)dt,
    T2 g=int_0^y t g_xx(x,t)dt+y int_y^infinity g_xx(x,t)dt,
    a=cx+h, b=cy+T2 g, W=(a,b).

Extend the velocity by its parities. Suppose a g_x+b g_y=g. These hypotheses, including the horizontal Hessian bound, are essential. The conclusions are the boundary law, the isopycnal identities, a continuous uniform leading far field with linear vanishing at horizontal axes, and compactness in this class. A separate theorem excludes a C2 first-order coefficient u at c=1 with the growth and convergent-line-inverse assumptions stated below. Higher far-field coefficients and parameter variations remain formal.

Dependencies are result175 for the canonical limiting inverse and result184, in its repaired result186 form, for the axis lemma. To make their use precise: G(y)=g(0,y), v(y)=cy+T2g(0,y) satisfy

    vG'=G, v(0)=0, v'(0)=1, v''=-g_xx(0,y),
    v'=c+int_y^infinity g_xx(0,t)dt,
    v,G,G'>0 for y>0,
    G=K y^p(1+O(y^(gamma-1))), 0<K<infinity, gamma>=p.

Here is a short proof of the needed axis facts. Parity gives T1g(0,y)=0; transport gives vG'=G. Differentiating the absolutely convergent line integral gives the displayed v derivatives. The normalization and the identity divided by y give v'(0)=1. At a first positive zero of v, the equation G'=G/v on the preceding interval makes G positive and increasing, contradicting vG'=G at that zero. Thus v and G,G' stay positive. The inverse bound gives v=cy+O(y^gamma); consequently 1/v-1/(cy)=O(y^(gamma-2)) is integrable at infinity. Integration of (log G)'=1/v proves the stated positive finite K and error. Growth forces p<=gamma.

## 1. Inverse regularity and fixed-horizontal-coordinate decay

Evenness implies g_x(0,t)=0. Integrating g_xx in x gives, on each bounded x interval,

    |g_x(x,t)| <= C |x|(1+t)^(gamma-2),
    |g(x,y)-G(y)| <= C x^2(1+y)^(gamma-2).

The constants can be taken independent of x for these weaker bounds, since the exponent gamma-2 is negative and |(s,t)|>=t. The sharper integrable bound yields

    h_x=-int_y^infinity g_xx(x,t)dt
        =O((1+|x|+y)^(gamma-1)).

The integral differentiates locally uniformly in x, so h is C1, h_y=g_x, and b_y=c-h_x is continuous. No b_x is asserted. To obtain |h|<=C'(1+r)^gamma, for large |x| split its t integral at |x|: below this point use |g_x|<=C(1+sqrt(x^2+t^2))^(gamma-1), above use the fixed-x bound. If y>|x|, only the second bound is needed. The same split in the two integrals defining T2 proves |T2g|<=C'(1+r)^gamma; in the first integral one may instead bound by int_0^y t(1+t)^(gamma-2)dt. Thus |V|<=C'(1+r)^gamma. These estimates also justify all compact-parameter differentiations of the line integrals used below.

## 2. Boundary law, inverse-density coordinates and relative area

Put k(x)=g_y(x,0), a0(x)=a(x,0). Differentiate transport in y at y=0. Oddness gives g=g_x=g_yy=0 there; b=a_y=0 and b_y=c-h_x. Therefore

    a0 k'=(a0'-A)k.

If k>0 everywhere, division is legal and (a0/k)'=A/k. Since a0(0)=0,

    a0(x)=A k(x) int_0^x dt/k(t).

In particular a0>0 on x>0. There a0=cx+O(x^gamma), a0'=c+O(x^(gamma-1)), hence

    k'/k=(p-1)/x+O(x^(gamma-2)).

The error is integrable at infinity. Integrating it gives a finite real limit for log(x^(1-p)k(x)), with remainder O(x^(gamma-1)). Exponentiation and evenness prove

    k(x)=L |x|^(p-1)(1+O(|x|^(gamma-1))), 0<L<infinity.

Now assume g_y>0 on y>=0. For fixed x, g(x,0)=0 and g(x,y)=G(y)+o(1) tends to infinity. The inverse y=Y(x,sigma) of sigma=g(x,y) therefore exists on [0,infinity), is C2, and Z=Y_sigma=1/g_y(x,Y)>0. Set H(x,sigma)=h(x,Y). Differentiating g(x,Y)=sigma yields

    g_x=-Y_x/Z, H_sigma=h_y Z=-Y_x,
    H(x,sigma)=int_sigma^infinity Y_x(x,s)ds.

The last identity is an absolutely convergent change of variables in the canonical h integral. Write a_tilde=cx+H, b_tilde=b(x,Y). Transport says b_tilde=a_tilde Y_x+sigma Z. At fixed physical y the chain rule gives

    a_x=partial_x a_tilde+Y_x^2/Z,
    b_y=(-Y_x^2+a_tilde Z_x+Z+sigma Z_sigma)/Z.

Adding these and using div W=2c proves

    partial_x((cx+H)Z)+sigma Z_sigma=A Z.

At sigma=0: Y=0, Z=1/k, Z(0,0)=1, H_sigma=0 and Z_sigma=-g_yy Z^3=0. At fixed x, g~K y^p gives Y~(sigma/K)^c. Since a g_x=O(y^(2gamma-2))=o(y^p) and b=cy+O(y^gamma), transport gives g_y~pK y^(p-1), hence Z~c K^(-c) sigma^(c-1). The fixed-x line estimate gives H->0.

At x=0, twice differentiating g(x,Y)=sigma gives

    Y_xx(0,G(y))=-g_xx(0,y)/G'(y)=v''(y)/G'(y).

Changing variables d sigma=G'(y)dy proves the absolutely convergent identity int_0^infinity Y_xx(0,sigma)d sigma=int_0^infinity v''dy=c-1=D. Integrating the first transformed equation on [0,S] and using int_0^S sigma Z_sigma=S Z-Y gives

    partial_x int_0^S (cx+H)Z d sigma+S Z(x,S)=2c Y(x,S).

Only compact-interval differentiation is used. Rewriting the equation as (cx+H)Z_x+sigma Z_sigma=(D-H_x)Z supplies no sign for Z_x; no sign of H_x has been proved.

Without the assumption g_y>0 define M(x)=int_0^infinity(G(y)-g(x,y))dy. The fixed-x bounds for the integrand and its first two x derivatives are integrable and locally uniform in x. Thus M is C2,

    M'=h(x,0), M''=-int_0^infinity g_xx(x,t)dt,
    M''(0)=D.

Under g_y>0 it is also the signed area between inverse graphs: M(x)=int_0^infinity(Y(x,sigma)-Y(0,sigma))d sigma. For completeness, compare graph areas with common density cutoff S. The leftover rectangular strip tends to zero because g(x,y)-G(y)=O(x^2 y^(gamma-2)) and inverse slopes are comparable to y^(1-p). Thus |Y(x,sigma)-Y(0,sigma)|=O(x^2 y^(gamma-p-1)) at y~(sigma/K)^c. Multiplication by d sigma comparable to y^(p-1)dy gives the integrable bound O(x^2 y^(gamma-2))dy. This additional area interpretation is not needed by the proposed text.

## 3. Leading far field without a horizontal derivative of V2

Write W=w e_r+q e_theta. For sufficiently large R, w>=cr/2 on r>=R, w=cr+O(r^gamma), q=O(r^gamma). Define a real-angle flux coordinate

    I(r,theta)=int_0^theta r w(r,s)ds.

The distributional divergence of W is2c and W is continuous. Mollify in the full plane, use the divergence theorem on an annular sector, then pass to the uniform-on-compact limit. The flux on theta=0 vanishes because b(x,0)=0. It follows that

    I_r=2cr theta-q(r,theta), I_theta=rw>0.

These formulas show I is C1 even though b_x was not assumed. The lifted map theta->I(r,theta) is strictly increasing and onto R, since I_theta has a positive lower bound for each r. Its inverse is C1. In radial time trajectories solve theta'=q/(rw). Substitute z=I(r,theta). Then

    z'=2cr I^(-1)(r,z), partial_z RHS=2c/w.

The right side is continuous and locally Lipschitz in z. On each finite radial interval it has at most linear growth, so solutions exist uniquely, forward and backward. They depend C1 on the initial angle omega at r=R. This proves trajectory uniqueness by an explicit scalar equation, without invoking a C1 theorem for W itself.

Let tau=int_R^r ds/w(s,theta(s,omega)) and delta=tau-p log(r/R). Differentiating the z equation with respect to omega gives

    partial_omega z=R w(R,omega) exp(2c tau),
    J:=partial_omega theta=R w(R,omega) exp(2c tau)/(r w(r,theta)).

Both |theta'| and |delta'| are O(r^(gamma-2)), uniformly in omega. Consequently theta->Omega(omega), delta->delta_inf(omega) uniformly with errors O(r^(gamma-1)). The last displayed identity then gives uniform convergence

    J -> w(R,omega) exp(2c delta_inf(omega))/(cR)>0.

The limiting function is continuous and has a positive minimum on a period. Uniform convergence of functions and derivatives proves Omega is C1. Periodicity, backward uniqueness and invariance of the axes give Omega(omega+2pi)=Omega(omega)+2pi and Omega(0)=0, Omega(pi/2)=pi/2, Omega(pi)=pi. The positive derivative makes it a C1 circle diffeomorphism.

Transport along these C1 curves gives d_tau g=g. Thus

    r^(-p)g(r,theta(r,omega))=R^(-p)exp(delta(r,omega))g(R,omega)

converges uniformly to Phi(omega)=R^(-p)exp(delta_inf(omega))g(R,omega). The inverses of theta(r,.) converge uniformly to Omega^(-1), by their common positive derivative bound for large r. Therefore

    g(r,theta)=r^p Theta(theta)+o(r^p), Theta=Phi composed with Omega^(-1),

uniformly in theta. In particular g=O((1+r)^p), Theta is continuous and has the density parities, and Theta(pi/2)=K. The trace on the initial circle is C1 and vanishes at both horizontal axes. Multiplication by the bounded continuous exponential and composition with the C1 inverse angle map yield |Theta(theta)|<=C''|sin theta|. No differentiability of delta_inf is needed for this bound.

If g_y>0 on y>=0, g(R,omega)>0 on the upper semicircle, hence Theta>0 there. As omega->0, g(R,omega)=R k(R)omega+o(omega). Continuity of delta_inf and the inverse function theorem at0 yield Theta(theta)=L' theta+o(theta), where

    L'=c R^(2-p) k(R) exp(-A delta_inf(0))/a0(R).

The boundary identity k'/k=a0'/a0-A/a0 integrates on the horizontal trajectory to

    k(r)=k(R) a0(r)/a0(R) exp(-A delta(r,0))(r/R)^(-Ap).

Since Ap=2-p and a0(r)/r->c, comparison with the boundary limit shows L'=L. These results exclude the signed global trace K sign(sin theta)|sin theta|^p, since it is not O(|sin theta|) for p<1. They do not exclude agreement with it only near the vertical axis. They provide neither convergence of derivatives of the rescaled density nor leading velocity asymptotics. Indeed the supplied horizontal-Hessian bound gives only partial_xx[R^(-p)g(RX)]=O(R^(gamma-p)) on a fixed annulus, and gamma>=p.

## 4. No regular first-order coefficient at c=1

Theorem. There is no u in C2(R2), even in x and odd in y, satisfying |u(X)|<=C(1+r)^q for some1<q<2, such that the improper integrals int_y^infinity u_xx(x,t)dt converge for every x and y>=0 and

    (E-1)u+T2u=-y, y>=0.

Only the value of T2 is required; T1 need not exist for this theorem. The improper integral need not converge absolutely or uniformly in x. If a hydrostatic family admitted g=y+D u+O(D^2), c=1+D and V[g]=D V[u]+O(D^2) in a topology justifying substitution, the coefficient of D in transport would be exactly this equation. The theorem excludes this particular regular expansion, not every family as c decreases to1.

First extend T2 oddly. For fixed x, write A(x)=int_0^infinity u_xx(x,t)dt, which exists by hypothesis. The canonical formula becomes

    T2u(x,y)=y A(x)-int_0^y (y-t)u_xx(x,t)dt, y>=0.

The equation identifies T2u with the jointly continuous function -y-(E-1)u. At y=1 the preceding formula expresses A(x) as this continuous value plus a compact integral of a continuous function. Thus A is continuous, locally bounded in x. This detail justifies Fubini and distributional integration by parts in y, even without a uniform-tail hypothesis. Across y=0 the odd extension has continuous first derivative A(x), so no delta mass occurs. Consequently (T2u)_yy=-u_xx in distributions on R2. The commutator (Eu)_yy=(E+2)u_yy gives

    u_xx=(E+1)u_yy.                                    (L)

Put w=u-u_y(0)y. It obeys(L), is even in x and odd in y, and w(0)=grad w(0)=0. Taylor's theorem gives |w|<=Cr^2 near0. Since q<2, after enlarging C it follows that |w|<=Cr^2 globally and also |w|<=C(1+r)^q globally. It is a tempered distribution. With Fourier coordinates(kappa,eta) and Lambda=kappa partial_kappa+eta partial_eta, transformation of(L) gives

    eta^2(Lambda+3) what+kappa^2 what=0.

For example, Fourier(E+1)u_yy=-(Lambda+1)(-eta^2 uhat)=eta^2(Lambda+3)uhat, fixing the sign and the constant3.

On eta!=0 introduce the smooth chart alpha=kappa/eta, beta=eta. A scalar distribution is pulled back with the usual Jacobian factor in its action on test functions; first-order differential operators transform by the chain rule. In this chart Lambda=beta partial_beta, so

    beta partial_beta what=-(3+alpha^2)what.

Multiplication by the smooth nonzero factor |beta|^(3+alpha^2) makes its beta derivative zero. A distribution with zero derivative in one coordinate is constant in that coordinate: test functions of zero beta integral are beta derivatives of compactly supported test functions, so it annihilates all of them. Hence

    what=|beta|^(-3-alpha^2)S_+(alpha) on beta>0,
    what=|beta|^(-3-alpha^2)S_-(alpha) on beta<0,

for distributions S_+,S_-. In particular what(lambda .)=lambda^(-3-alpha^2)what on these charts for lambda>0.

The physical growth bounds give two incompatible Fourier dilation bounds. For a Schwartz test function phi, Fourier scaling gives, up to a harmless transform convention,

    <what(lambda .),phi>=lambda^(-2) int w(Y/lambda) phihat(Y)dY.

For 0<lambda<=1 its absolute value is bounded by C lambda^(-q-2) times the fixed Schwartz seminorm int(1+|Y|)^q|phihat(Y)|dY. The global quadratic bound gives C lambda^(-4) int|Y|^2|phihat(Y)|dY for all lambda>0. Thus lambda^(q+2)what(lambda .) is uniformly bounded in S' as lambda decreases to0, and lambda^4what(lambda .) is uniformly bounded as lambda increases to infinity.

In each compact subset of eta!=0, the explicit dilation law says that e^(t f)what is a bounded family of distributions for t>=0, first with f=alpha^2-(q-1), then with f=1-alpha^2. The bounds use fixed finite-order test seminorms. If f>=f0>0 on the support of a compactly supported test chi, then

    |<what,chi>|=|<e^(t f)what,e^(-t f)chi>|
       <= C ||e^(-t f)chi||_(C^N) ->0.

Derivatives of the decaying exponential produce polynomial factors in t, dominated by e^(-t f0). Therefore what vanishes where alpha^2>q-1 and where alpha^2<1. These two open sets cover eta!=0, since q-1<1. Hence what is supported in the line eta=0.

For clarity, here is the distribution fact needed to finish, including its order issue. A tempered distribution supported on eta=0 has finite normal order globally. Choose N at least its finite Schwartz derivative order. Taylor-expand a test function in eta at0, using a fixed cutoff equal to1 near0. The remainder and its first N normal jets vanish on the line. Multiplying the remainder by a cutoff in eta/epsilon does not change its pairing with the supported distribution; its weighted derivatives up to order N tend to0 as epsilon->0, by Taylor's formula and the Schwartz decay in kappa. The remainder therefore pairs to0. The distribution depends only on the finitely many normal jets, so it is a finite sum sum_(j<=N) T_j(kappa) delta^(j)(eta), with tempered coefficient distributions T_j. Inverse Fourier transformation gives w=sum_(j<=N)y^j t_j(x) distributionally. To avoid evaluating a distribution at a point, choose smooth compactly supported functions of y whose first N+1 polynomial moments form an invertible matrix. Pairing the last identity in y recovers each t_j as a linear combination of integrals of the continuous function w against these tests. Thus every t_j is continuous; the polynomial identity is pointwise. For fixed x the growth bound q<2 then forces all coefficients of y^j, j>=2, to vanish. Oddness removes the constant term. Thus w=y B(x).

The function B is C2, for example B(x)=w(x,1). Equation(L) gives B''=0, evenness makes B constant, and w_y(0)=0 makes it zero. Therefore u=u_y(0)y. The left side of the claimed inhomogeneous equation is then0, contradicting -y. This proves the theorem.

In particular O((1+r)log(2+r)) growth is excluded, since it is bounded by every power q>1. In contrast K_D y^(1/(1+D)) on y>0 is independent of x, has zero hydrostatic velocity, and solves c y G'=G. If K_D=1+kappa1 D+kappa2 D^2+o(D^2), its first two coefficients at fixed y>0 are

    u=y(kappa1-log y),
    w2=y(kappa2+(1-kappa1)log y+(log y)^2/2).

The first is not C1 at0. The superficially regularized outer expression -y log r has u_xx(0,y)=-1/y for y>0, so its canonical upper line integral diverges. These examples do not evade the theorem's hypotheses. No theorem here rules out singular inner limits, unmatched remote strains or families whose first-order inverse does not converge to V[u].

## 5. Formal higher far field and an exact moment statement

Assume, only for formal coefficient calculations, a smooth angular homogeneous field f_p=r^p Theta(theta), with the density parities, and a full expansion which can be differentiated and inserted term by term into the canonical inverse. The leading inverse is homogeneous of degree p for0<p<1. Since grad f_p has degree p-1, the first quadratic term has degree2p-1 and transport gives

    [c(2p-1)-1] f_(2p-1)+V[f_p].grad f_p=0,
    f_(2p-1)=V[f_p].grad f_p/D.

On the positive vertical axis put K=Theta(pi/2), Q=pK+Theta''(pi/2). Polar differentiation gives (f_p)_xx(0,y)=Q y^(p-2). Direct integration, with both endpoints convergent because0<p<1, gives

    T2[f_p](0,y)=Q y^p/[p(1-p)],
    f_(2p-1)(0,y)=KQ y^(2p-1)/[(1-p)D].

Repeated quadratic interactions generate degrees d_n=np-(n-1), and c d_n-1=-(n-1)D!=0 for n>=2. There is no transport denominator resonance within this hierarchy. This does not guarantee existence of the hierarchy: the canonical lower-endpoint integral of a homogeneous curvature of degree d_n-2 stops converging when d_n<=0. A degree-zero density term can contribute logarithms to the velocity after an inner contribution is retained. The possible degree-zero values are c=n/(n-1). A logarithm is permitted, not compelled if its curvature coefficient vanishes. In particular the homogeneous inverse formula may not be used literally at degrees<=0 without matching a core.

The following moment statement is exact and does not presume the full hierarchy. Suppose int_0^infinity t|g_xx(0,t)-Q t^(p-2)|dt<infinity. With e(t)=g_xx(0,t)-Q t^(p-2), let m0=int_0^infinity t e(t)dt. Subtract the integrable-at-zero weighted power in the first inverse integral and its convergent upper tail in the second. Then

    T2g(0,y)=Q y^p/[p(1-p)]+m0+o(1),

because int_0^y t e(t)dt->m0 and |y int_y^infinity e(t)dt|<=int_y^infinity t|e(t)|dt->0. In the formal expansion of1/v, a constant m0 contributes -m0/(c^2 y^2). Integration of G'/G=1/v then contributes K m0 c^(-2)y^(p-1) to G. This is a contribution, not necessarily the entire coefficient at that power: other formal terms may coincide with it. The weighted moment hypothesis may fail for an actual g and has not been deduced from the leading trace theorem.

There is a separate angular regularity obstruction for a smooth-coefficient formal expansion. Put F(s)=f_p(1,s) and

    q(s)=p(p-1)F(s)-2(p-1)sF'(s)+s^2 F''(s).

For x>0, f_p=x^p F(y/x), so (f_p)_xx(x,t)=x^(p-2)q(t/x). Smooth angular parity gives q(s)=O(s) at0 and q(s)=Q s^(p-2)+O(s^(p-4)) at infinity. The latter also follows from f_p(u,1)=K+Q u^2/2+O(u^4) nearu=0. Hence

    C_p(Theta)=int_0^infinity s[q(s)-Q s^(p-2)]ds

converges. For S=y/|x|, substitute the homogeneous expression in the two inverse integrals and subtract the power term. The integral over[0,S] has remainder C_p+O(S^(p-2)); the upper-tail remainder after multiplication by S is O(S^(p-2)). Therefore, as |x|/y->0,

    T2[f_p](x,y)=Q y^p/[p(1-p)]+C_p|x|^p+O(x^2 y^(p-2)).

The first velocity component is O(x y^(p-1)) near the positive vertical axis, since f_px=O(x t^(p-2)) for t>=y, and f_px=O(x y^(p-2)) there. Thus T1[f_p] f_px contributes O(x^2) at fixed y>0. The non-differentiable term in f_(2p-1) is

    pK C_p |x|^p y^(p-1)/D.

Since p<1 and K>0, a formal expansion whose coefficients are C1 in x near that axis must have C_p=0. A smooth actual g need not possess such a uniform expansion: an angular boundary region can invalidate termwise differentiation. This is a necessary condition for the stipulated formal expansion, not nonexistence of hydrostatic solutions. No sign theorem for C_p has been established here.

## 6. Dilation, parameter variation and compactness

For lambda>0 define g_lambda(X)=lambda g(X/lambda). Substitution t=lambda s in the two inverse formulas gives V[g_lambda](X)=lambda V[g](X/lambda); g_lambda has center slope1. Thus it preserves steady transport at fixed c. The formal derivative is d=g-Eg. It cannot vanish identically: that would make g degree-one homogeneous, and differentiability and normalization at0 would force g=y, contrary to sublinear growth. Under sufficient differentiability and legal passage of derivatives through V, d lies in the formal kernel

    L_g u=(cX+V[g]).grad u-u+V[u].grad g.

At a nonsteady input with residual R, the exact scaling identity is R[g_lambda](X)=lambda R[g](X/lambda), hence L_g(g-Eg)=R-E R whenever the derivative is legal. Small sampled R alone does not control its derivative E R. This identity is relevant to the separate numerical singular-vector audit.

A formal variation of c gives L_g u+c1 E g=0. At a fixed angular trace, differentiation of r^(1/c) produces -c1 p^2 r^p Theta log r. This is not bounded in the strict weighted-sup norm sup_(r>=1) r^(-p)|u| when c1 and Theta are nonzero. It may belong to spaces allowing a logarithmic loss; 'fixed weight' should mean the strict stated bound. No existence count or parameter-selection rule follows from a formal kernel, the axis recurrence, or the frozen horizontal Cauchy symbol.

Compactness theorem. Let c_n->c>1 and g_n in C3(R2) obey the above parities and slope normalization, with the three weighted bounds using a single C,gamma, and sup_(|X|<=R)|D3g_n|<=C_R for every R. Suppose their canonical hydrostatic transport residuals tend to0 uniformly on compact subsets of y>=0. Then a subsequence converges in C2 locally to a C2 solution in the same weighted class, with slope1 and parameter c.

Proof. The parities fix g_n(0)=0, grad g_n(0)=(0,1), and D2g_n(0)=0. The local third derivative bounds therefore bound all lower derivatives and make D2g_n uniformly Lipschitz on each disc. Arzela-Ascoli, applied consistently to derivatives, and a diagonal subsequence give convergence in C2 locally. The parities, normalization and pointwise weighted inequalities pass to the limit. For a compact set |x|,y<=R, the bounds |g_nx(x,t)|<=C_R(1+t)^(gamma-2) and |g_nxx(x,t)|<=C(1+t)^(gamma-2) give uniform integrable tails. First truncate the line integrals at T, pass to the limit on the bounded intervals by C2 convergence, then let T increase to infinity uniformly on the compact set. The integral int_0^y t g_nxx dt is already compact. This proves V[g_n]->V[g] locally uniformly. Passing to the residual proves steady transport. The axis lemma gives c>=1/gamma. Nothing upgrades the limit to C-infinity or proves that original profiles obey the common bounds.

## 7. Verification design and present scope

The preceding proof precedes the code. Independent symbolic checks will test chain rules, commutators, Fourier constants, degree arithmetic, the moment contribution and dilation. Independent manufactured numerical tests will use g=y(1+x^2+y^2)^(-1/4), whose inverse-density coordinate is explicit, rather than the producer's test field. This density has positive vertical derivative and the required parities but is not steady. Its nonzero transport residual must be retained in transformed identities. A separate divergence-constant manufactured velocity will test the flux-coordinate Jacobian at two numerical integration resolutions. Pure homogeneous angular inputs will check the finite-part constant by two distinct convergent integral formulas. These are checks of formulas and implementations, not proofs of existence.

The hypotheses and conclusions in parts(a)-(c) and the compactness statement of proposed3.74 are supported by the proof above. Recommended precision repairs are to call the excluded full-plane sine-power trace its signed extension, to specify the strict weighted-sup meaning in(e), and to include the continuous A(x) justification and the supported-distribution lemma in(c). Algebra in(d) is conditional/formal except the explicitly weighted-moment implication, which is exact. A later verification record supplies code results and the final verdict for each frozen text version. The original endpoint remains UNRESOLVED.
