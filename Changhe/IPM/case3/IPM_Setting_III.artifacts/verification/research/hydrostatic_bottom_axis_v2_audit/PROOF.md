# Revised bottom analytic data, axis divergence and source representation

Written 2026-10-21T10:31:36.207157+00:00 before the executable checks for result204. This is a standalone proof of the revised section3.75 and AppendixA.3.75 in verification/INPUTS.json. The full independent argument of result202 is retained, with the regularity hypothesis corrected. No original SettingIII endpoint follows.

## Equations and precise regularity

Write x for xi. Fix c>1, p=1/c, D=c-1 and A=2c-1. The hydrostatic density g is even in x and odd in y and satisfies g_y(0,0)=1. The bounds used here are

    |g| <= C(1+|x|+y)^gamma,
    |grad g| <= C(1+|x|+y)^(gamma-1),
    |g_xx| <= C(1+|x|+y)^(gamma-2),       0<gamma<1.

On y>=0 define

    h=-int_y^infinity g_x(x,t)dt,
    b=cy+int_0^y t g_xx(x,t)dt+y int_y^infinity g_xx(x,t)dt.

The local equations are

    h_y=g_x,    b_y=c-h_x,    (cx+h)g_x+b g_y=g.             (1)

Assume g is C2. Evenness gives |g_x(x,t)|<=C_x(1+t)^(gamma-2), locally uniformly in x, by integration from x=0. Thus the first integral and its x derivative converge locally uniformly; h is C1, h_y=g_x and h_x=-int_y^infinity g_xx. The second formula gives continuous b and continuous b_y=c-h_x. These estimates alone do not give b_x.

If h is C1 and b is continuous with continuous b_y, and the triple solves(1), b(x,0)=0 and h(x,y)->0 for fixed x as y->infinity, integrating the first two equations forces exactly these canonical formulas. Conversely a C2 solution of the hydrostatic transport equation supplies the equations in(1) with h C1 and b continuous with continuous b_y. The stronger C1 conclusion for b follows on every open set where g_y is nonzero, from b=[g-(cx+h)g_x]/g_y. The revised statement makes exactly the regularity conclusion proved here, and asserts no b_x derivative.

The distinction is real at the level of the stated estimates. For 0<alpha<1 set phi(y)=y exp(-y^2), psi(x)=exp(-x^2)(1+|x|^(2+alpha)) and g=psi phi. This g is C2, normalized, has both parities and all three bounds. Its canonical second component is V2=psi''(x) sqrt(pi) erf(y)/4. For fixed y>0 its nonconstant leading term at x=0 is a positive multiple of |x|^alpha, so V2 is not differentiable there. This is not a transport solution and does not refute the stronger converse for actual solutions. It shows why the bounds alone cannot justify that converse.

## Analytic existence and uniqueness from the bottom

Let k be positive, even and real analytic on R with k(0)=1. Put zeta(x)=int_0^x k(t)^(-1)dt, a0=A k zeta and h0=a0-cx. These are real analytic; zeta is odd and strictly increasing. If an analytic parity triple solves(1) with g(x,0)=b(x,0)=0 and g_y(x,0)=k, differentiation of transport at y=0 gives

    a0 k'=(a0'-A)k.

Oddness of a0 eliminates the integration constant in (a0/k)'=A/k, so h0 is forced even if it is not prescribed as extra data.

Write g=sum g_(2n+1)y^(2n+1), h=sum h_(2n)y^(2n), b=sum b_(2n+1)y^(2n+1). For n>=1, the first two equations give h_(2n)=g_(2n-1)'/(2n) and b_(2n+1)=-h_(2n)'/(2n+1). Also b1=1-a0 k'/k. The transport coefficient is

    a0 u'+[(2n+1)b1-1]u=F_n,        u=g_(2n+1),

where F_n depends only on previous coefficients and their derivatives. In particular F1=-k'^2/2+k k''/6. Substitute u=k^(2n+1)w(zeta) to obtain

    (A zeta d_zeta+2n)w=F_n/k^(2n+1).

For any m>0 the bounded inverse is E_m^(-1)f=int_0^1 t^(m-1)f(t^A zeta)dt. Differentiating t^m f(t^A zeta) proves the equation; homogeneous solutions on either side are constant multiples of |zeta|^(-m/A). Boundedness at zero forces both constants to vanish. This proves the stated coefficient uniqueness, but convergence still needs an argument.

Use the isopycnal inverse y=Y(x,sigma), with Z=Y_sigma and H=h(x,Y). Near the bottom it exists because k>0. Direct chain rules give

    H_sigma=-Y_x,
    d_x[(cx+H)Z]+sigma Z_sigma=A Z.

Set I2Z=int_0^sigma(sigma-s)Z(x,s)ds. Then H=h0-d_x I2Z and

    a0 Z_x+sigma Z_sigma+(a0'-A)Z=d_x[Z d_x I2Z].          (2)

Conversely an analytic even-in-both-variables solution Z of(2) with Z(x,0)=1/k gives Y=int_0^sigma Z and its analytic inverse g. Define h=H(x,g) and b=[(cx+H)Y_x+sigma Z] at sigma=g. Substitution proves transport and h_y=g_x. To check the last derivative without assuming it, put B=(cx+H)Y_x+sigma Z. At fixed y,

    h_x=H_x-H_sigma Y_x/Z,
    b_y=B_sigma/Z.

Since H_sigma=-Y_x and Y_xsigma=Z_x, the terms involving Y_x^2 cancel in h_x+b_y, leaving H_x+1+(cx+H)Z_x/Z+sigma Z_sigma/Z. Equation(2), equivalently the isopycnal flux equation, makes this c. Hence b_y=c-h_x. Parities and all prescribed bottom data follow from evenness of Z.

For a quantitative existence estimate, fix R. Extend zeta and its inverse to complex neighborhoods of the compact interval, then choose a centered symmetric rectangle Omega in the zeta plane whose closure is contained in the inverse's domain, contains zeta([-R,R]), and on which kappa(zeta)=k(x(zeta)) has no zeros. Such a rectangle exists by the inverse function theorem and injectivity on a slightly larger real interval, after reducing its height. The compact containment is needed: it ensures finite M=sup|1/kappa| and N0=sup|kappa|.

For W=kappa Z, equation(2) becomes

    (A zeta d_zeta+sigma d_sigma)W
      =d_zeta[(W/kappa^2)d_zeta(I2W/kappa)],   W(zeta,0)=1. (3)

Let d(zeta)=dist(zeta,boundary Omega) and ||f||_j=sup|f|d^j. Multiplication adds the indices. For j>=1, Cauchy on a disc of radius d/(j+1) gives ||f'||_(j+1)<=e(j+1)||f||_j; for j=0 use radius d/2, giving 2<=e. Since d(t^A zeta)>=d(zeta), ||E_m^(-1)f||_m<=||f||_m/m.

Writing W=sum W_m sigma^m, W0=1, yields for m>=1

    E_m W_m=sum_(i+j=m-2) d_zeta[(W_i/kappa^2)d_zeta(W_j/kappa)]/[(j+1)(j+2)].

Odd coefficients vanish. For U_m=||W_m||_m the inner derivative costs e(j+1), the outer derivative costs em, and the three inverse kappa factors cost M^3. The inverse E_m divides by m. Thus, more sharply than needed,

    U_m <= e^2 M^3 sum_(i+j=m-2) U_i U_j/(j+2)
         <= e^2 M^3 sum_(i+j=m-2) U_i U_j.

Induction gives U_(2l)<=(e^2 M^3)^l Cat_l<=(4e^2 M^3)^l. Therefore the series converges normally on |sigma|<d(zeta)/(2e M^(3/2)). On |sigma|<=rho=d/(4e M^(3/2)), |W-1|<=sum_(l>=1)4^(-l)=1/3.

For fixed zeta set Q(sigma)=kappa Y(sigma). On the rho disc, Q'=W has real part at least2/3. Integrating along a chord proves injectivity. Also |Q(sigma)-sigma|<=|sigma|/3. On |sigma|=rho and for |kappa y|<rho/2, Rouche's theorem gives one zero of Q(sigma)-kappa y, since rho/3+rho/2<rho. This proves the image contains |y|<rho/(2N0). Joint analytic inversion yields the triple on a neighborhood of [-R,R]x{0}, with real height at least d0/(8e M^(3/2)N0), where d0=min_(zeta([-R,R]))d>0.

Every analytic triple has the bounded coefficients already determined. Identity of its Taylor series with the constructed one proves equality near the segment, and the real-analytic identity theorem extends equality to the component of the common domain containing it. Smooth triples with the same k have the same bottom jets, because h=h0+int_0^y g_x and b=int_0^y(c-h_x) are then smooth locally and the coefficient calculation applies to derivatives. No smooth uniqueness or common height on all of R follows.

## Triangular axis recursion and a residual set of divergent series

Let G be odd and smooth, with G'>0, and put v=G/G', Q=G/G'^2. The formal x recursion in result186/section3.73 uses g0=G, b0=v, a1=2c-v', g2=-v''/2 and g_(2n+2)=-b_(2n)''/[(2n+1)(2n+2)]. We claim

    g_(2n)=Q^n G^(3n)/(2n)!+R_n(G,...,G^(3n-1)).           (4)

Here each R_n is a rational function of the displayed jet with powers of G' as denominators. For n=1, the top derivative in v'' is -G G'''/(G')^2, proving(4). Suppose(4) holds through n. The coefficient of x^(2n) in transport gives

    b_(2n)G'=g_(2n)-v g_(2n)'-2n a1 g_(2n)
       -sum_(i+j=n,i,j>=1)[2j a_(2i+1)g_(2j)+b_(2i)g_(2j)'],
    a_(2i+1)=-b_(2i)'/(2i+1).

The only derivative of order3n+1 on the right is in -v g_(2n)'. All other terms have order at most3n, using that b_(2i) has order3i+1 and i,j<n in the sum. Differentiating twice in the next recursion gives the coefficient (v/G')Q^n/(2n+2)!=Q^(n+1)/(2n+2)! of G^(3n+3); all others have smaller order. This completes the induction.

The reference axis datum G_* is defined by v_*=cy-D arctan y and G_*'/G_*=1/v_*, with G_*'(0)=1. Its properties from186 are independently reused: it is odd analytic, G_*'>=c1(1+|y|)^(p-1), G_*~K_*y^p as y->infinity, v_*''=2Dy/(1+y^2)^2, and v_*'''(0)=2D. It has a holomorphic extension to a sufficiently thin uniform strip: at large real part v_* has no zero by its linear leading term, and on a compact real segment its only zero is the removable simple zero at0. A thinner strip avoids the other zeros and arctan's poles; integrating the removable logarithmic derivative constructs G_* there.

Fix delta,alpha>0 with such a strip. The real vector space B of odd strip-holomorphic phi, real on R, with phi'(0)=0 and norm sup|exp(alpha z^2)phi(z)| is Banach: multiplication by exp(alpha z^2) identifies it with a closed real subspace of bounded holomorphic functions. Cauchy on a fixed smaller circle about each real y gives, for each fixed j,

    |phi^(j)(y)|<=C_j||phi|| exp(-alpha y^2/2).

Choose a sufficiently small open ball N around0. The polynomial lower bound for G_*' ensures G_*'+phi'>0 uniformly on R. The rational expression

    v''=-G''/G'-G G'''/(G')^2+2G(G'')^2/(G')^3

shows that v''-v_*'' decays faster than any power at infinity, uniformly with size O(||phi||). On a fixed compact interval it is uniformly small, together with its derivative. Near0, oddness gives v''(0)=0 and closeness of v''' to v_*''' gives v''>0; away from0 on a compact positive interval use the positive minimum of v_*''; at infinity compare the Gaussian error with its positive y^(-3) tail. Reducing the same ball gives all three conclusions simultaneously. The formula for v-v_* gives a Gaussian times a polynomial, so v-cy=O(1). In fact these additive Gaussian perturbations preserve the leading K_*, which is stronger than the stated existence of some positive K_G.

Fix y0>0. Formula(4) makes every g_(2n)(y0) a continuous function on G_*+N. For integer m>=1 let S_m be the subset where |g_(2n)(y0)|<=m^(2n) for all n>=1. It is relatively closed. Every sequence of coefficients with finite root limsup belongs to some S_m, by enlarging m for finitely many initial coefficients.

For beta>0 define

    P_n(z)=z^3(z^2-y0^2)^(3n) exp[-(alpha+beta n)z^2].

It belongs to B and vanishes to order3n at y0. On the strip its weighted norm is at most C2 C3^n: with t=Re z, bound |z^2-y0^2| by t^2+delta^2+y0^2 and split exp(-beta n t^2) into two equal factors, one bounding |z|^3 uniformly for n>=1 and the other bounding the polynomial raised to n. Direct differentiation gives

    P_n^(3n)(y0)=(3n)! y0^3(2y0)^(3n)exp[-(alpha+beta n)y0^2].

For a fixed G in any relative open ball and sufficiently small eps, both perturbations G+-eps P_n/||P_n|| remain in that ball for every n. They leave the lower jets in(4) unchanged, including Q(y0)>0, and change g_(2n)(y0) by absolute magnitude at least eps C4 C5^n(3n)!/(2n)!, with C4,C5>0 independent of n. Since (3n)!/(2n)!>=(2n+1)^n, this eventually exceeds2m^(2n). One of the two signs is outside S_m. Thus S_m has empty interior; the complement of their union is a dense countable intersection of open subsets of the Baire space G_*+N. Every datum there has infinite root limsup and zero x-series radius. An analytic local triple would have exactly these formal coefficients, which is impossible. This proves generic analytic failure, not divergence for G_* and not failure of smooth solutions.

## Source trajectories and the exact Z representation

Assume now an actual C2 hydrostatic solution in the displayed class with g_y>0 throughout y>=0. Its axis asymptotic G(y)~K y^p and the evenness estimate |g(x,y)-G(y)|<=C_x(1+y)^(gamma-2) imply g(x,y)->infinity for every fixed x. Hence its isopycnal inverse Y exists for every sigma>=0 and is C2. The established inverse derivative bounds give

    |h_x(x,y)|<=C'(1+|x|+y)^(gamma-1),
    |h(x,y)|<=C'[(1+|x|)^gamma-1].                         (5)

The second follows by integrating h_x from x=0. Only the bound on h itself passes directly to H=h(x,Y). The first bound does not automatically pass to H_x, since H_x=h_x-g_x^2/g_y at y=Y.

The vector field T=(cx+H) d_x+sigma d_sigma is C1. In backward time s=-tau, sigma=sigma0 exp(-s). For |x| above a fixed large R, the sublinear bound on H makes cx+H have the sign of x and magnitude at least c|x|/2. Thus backward trajectories stay in a compact x interval and exist for all s>=0. On that interval Y(x,sigma)->0 uniformly as sigma->0, because min k>0. Hence cx+H converges uniformly to a0=A k zeta. This has the sign of x. For each eps>0, sufficiently late backward velocity is strictly inward on eps<=|x|<=R; it reaches |x|<eps and cannot cross outward. Consequently every trajectory tends to(0,0), including trajectories on sigma=0.

At the source the derivative matrix of T is diag(A,1): H_x(0,0)=D and H_sigma(0,0)=-Y_x(0,0)=0. Continuity of DT gives P.T(P)>=|P|^2/2 in a small half-disc. Integrating along the already convergent trajectory yields |P_tau|<=C exp(tau/2) for tau<=0, after increasing C to cover the finite initial segment.

Near the source, k is C1, and h_x(x,0)-D=a0'-A=a0 k'/k=O(|x|). Also h_x(x,Y)-h_x(x,0)=int_0^Y g_xx dt=O(sigma). Evenness gives g_x=O(x) and g_y is bounded below nearby, so H_x-D=O(|x|+sigma). Therefore int_-infinity^0 |D-H_x|(P_tau)dtau is finite. Expanding the isopycnal flux equation gives TZ=(D-H_x)Z. Since Z(P_tau)->Z(0,0)=1,

    Z(P)=exp[int_-infinity^0 (D-H_x)(P_tau)dtau].           (6)

For sigma=0 this also recovers Z=1/k directly, since D-h0'=-a0 k'/k. The fixed-point identity H=int_sigma^infinity Y_x ds follows by changing variables in the canonical h integral: Y_x=-g_x/g_y and ds=g_y dy. Formula(6), followed by Y=int_0^sigma Z and that integral, is an identity at actual solutions. No space of inputs, differentiability, contraction, or global existence theorem for the map has been supplied. Dilation gives Y_l=lY(x/l,sigma/l) and H_l=lH(x/l,sigma/l) by direct inversion.

## Frozen symbols and cusp example

At a frozen point, the perturbation equations for density u and velocities z,w are b u_y+a u_x-u+g_x z+g_y w=0, z_y=u_x, w_y=-z_x, where a=cx+h. Taking the determinant for exp(lambda y+i eta x) gives

    b lambda^3+(i a eta-1)lambda^2+i g_x eta lambda+g_y eta^2=0.

On an interior vertical-axis point, a=g_x=0 and b=v>0, g_y=G'>0. The three leading roots are (G'/v)^(1/3)|eta|^(2/3) times the cube roots of -1, with O(1) corrections. The positive real part is half that leading amplitude. Off axis with a,g_y,b nonzero, two roots are +-sqrt(i g_y eta/a)+O(1), and one is -i a eta/b+O(1). The corresponding horizontal Gevrey readings, and the function/parameter/dilation count, are formal statements only. The x-evolution frozen roots of186 instead grow in real part like the3/2 power of vertical frequency.

The explicit cusp trace in part(e) is exactly result197, whose standalone proof and83 independent checks are already complete. Its canonical inverse, monotonicity, moment Cp=0, both signs under compact angular perturbation, and strictly negative nonzero transport term are confirmed there. The lower bounds that preserve signs refer to the compact unit-circle arc 1<=y/|x|<=2; homogeneity then propagates each sign to the cone. There cannot be positive uniform lower bounds for the decaying derivatives on the entire unbounded cone. The actual lead Opus5.5 review of197 is frozen here and its algebra and scope agree with our independent derivation. Its finite-cutoff numerical Cp check is supplemental; our prior whole-tail calculation does not omit that tail.

## Scope of the independent argument

Parts(a)(i)-(ii), (b), (c), the formal symbol algebra in(d), and the cusp construction in(e) are confirmed with the revised hypotheses stated below. None supplies an original or hydrostatic global profile, a nonexistence endpoint, or selection of c.

Dependencies:186/section3.73 for axis positivity/asymptotics and its explicit arctan data,193/194 for isopycnal global identities, and197 for the exact homogeneous trace. Frozen sources and executable evidence are kept separately under verification. No Lean/Lake proof is attempted or authorized.


## Revised statement and positive-axis qualification

The reviewed v2 source weakens both directions of the canonical equivalence to h C1 and b continuous with continuous b_y. The integral argument above therefore proves its full equivalence. The counterexample above concerns only the stronger, now removed inference from the bounds. The v2 complex neighborhood, finite M and N0, j=0 Cauchy radius and image-disc argument agree with the quantitative proof above. Its open Banach ball and n>=1 closed sets give the stated Baire result. The source proof uses the sublinear bound for H itself and the local radial differential inequality; it does not assume a corresponding global bound for H_x.

The positivity qualification in the frozen symbol is necessary. Consider the exact local triple g=y, h=(c-1)x, b=y for any c>1. It solves all three local equations and all parities, but is not in the global sublinear class. On x=0,y=1 its determinant is lambda^3-lambda^2+eta^2; after setting t=|eta|^(2/3), lambda=t z, its roots tend to the cube roots of -1 and the maximal real part divided by t tends to1/2. At x=0,y=-1 the determinant is -lambda^3-lambda^2+eta^2. Its scaled roots tend to the cube roots of1 and the maximal real part divided by t tends to1. Thus the earlier formula could not hold at both signs of y. The revised text states it only at positive axis points, where v,G' are positive. This qualification is sufficient. The determinant formulation also covers lambda=0 without dividing by it.

On the unit-circle arc arctan1<=theta<=arctan2, all four strict quantities in the compact perturbation argument have positive minima. Homogeneity preserves their signs at every nonzero radius. The derivatives scale as r^(p-1), so their lower bounds cannot be positive uniformly on the entire unbounded cone. The revised text uses exactly the compact-arc argument. The formal dimension count is a conditional local index argument only. No assertion of global discreteness, selection of c, smooth uniqueness, convergence of the reference axis series, or solution of the original equation is made.

## Revised verdict and dependencies

The proof uses the explicitly stated hydrostatic class and inverse, the axis datum G_* and recursion established in result186, and the independently proved cusp trace formulas of result197. Their relevant arguments are repeated above; the frozen result202 records the auxiliary symbolic and manufactured checks. The external hostile review is an referee review, not an Opus review. Actual Opus5.5 collaboration is through the lead and the already checked result197 review. No failed Opus invocation is counted as a review. Subject to the transcription checks below, v2 is CONFIRMED in its stated local, generic, or formal scope. The full-plane SettingIII YES/NO question remains OPEN.
