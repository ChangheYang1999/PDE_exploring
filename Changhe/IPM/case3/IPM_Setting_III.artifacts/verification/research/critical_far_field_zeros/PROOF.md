# Critical far-field zeros, saddle resonances and axis sign transfer

Date: 2026-10-20. Status: CONFIRMED by independent reconstruction and 138 exact algebraic checks completed 2026-10-20T17:42:12Z. This gives necessary conditions and conditional exclusions, not existence or nonexistence in the full primary class.

## 1. Statement, notation and dependencies

Let ell>1 and let rho, psi, U be an exact primary profile on R^2:

    W=ell X+U, W.grad rho=rho,
    U=(-psi_y,psi_x), -Delta psi=rho_x,
    rho even in x and odd in y, psi odd in both variables,
    rho smooth, a=rho_y(0)!=0, U=o(|X|),
    |rho|+(1+r)|grad rho|<=C(1+r)^gamma, 0<gamma<1.

Set A=2ell-1, p=1/ell, w(x)=W_1(x,0), g(x)=rho_y(x,0). Write K for the set of points whose forward W-orbit is bounded. The potential P is fixed by grad P=W+rho e_2 and P(0)=0. It exists because curl W=-rho_x. Hdyn means that the origin is the only equilibrium, equivalently every nonzero point tends to the origin backward and escapes forward.

The following previously established results are dependencies, with their exact scope recorded here. The arguments are in ../scaling/PROOF.md, ../local_ipm_continuation/PROOF.md, ../trapped_set_potential/PROOF.md and ../sign_and_local_uniqueness/PROOF.md.

* The origin has DW(0)=diag(A,1). There is no nonzero vertical-axis equilibrium, rho(0,y)/a>0 for y>0, and rho(0,y)/y^p tends to a nonzero K_v of the sign of a.
* The exact profile has exterior symbol bounds |D^j rho|+|D^j U|<=C_j r^(p-j), for every j. The rescalings r^(-p)rho(r,theta) tend in every C^j angular norm to a smooth Theta(theta); Theta(pi/2)=K_v. In particular w=ell x+O(x^p), w'=ell+O(x^(p-1)).
* K is compact, connected, invariant, contains 0, and rho=0 on K. Its complement E consists of the escaping points. The smooth scattering diffeomorphism Q:E -> R^2\{0} preserves each open quadrant, satisfies Q(Phi_t X)=exp(ell t)Q(X), and obeys rho(X)=|Q(X)|^p Theta(arg Q(X)). It extends over the parts of the symmetry axes contained in E. Distinct trajectories in E correspond to distinct radial rays of Q.
* Hdyn is equivalent to w>0 on (0,infinity), to rho/(a y)>0 off the horizontal axis, and to the absence of zeros of Theta in (0,pi). These equivalences use no finiteness assumption on equilibria or angular zeros.
* A smooth equilibrium with a positive simple eigenvalue separated from a nonpositive eigenvalue has a smooth one-dimensional strong unstable manifold. On it the backward distance decays exponentially at any rate smaller than the positive eigenvalue. The contraction construction needed here is given in ../trapped_set_potential/PROOF.md.

The claims proved below are:

1. rho/a has a negative value in y>0 if and only if Theta/a has a negative value in (0,pi). Their nonnegativity assertions are also equivalent.
2. If Hdyn fails, a maximizer z of P on K is a nonzero critical-density equilibrium with eigenvalues lambda<=0 and mu=2ell-lambda>=2ell. Its fast unstable branch gives at least two critical interior angular zeros, reflected about pi/2. There are at least four if this maximizer is off the axes. A critical angular zero has Theta=Theta'=0.
3. If one of these fast-branch angular zeros has finite order k, then k>=2 and there is an integer j, 1<=j<k, such that

       j mu+k lambda=1,
       mu=(2k ell-1)/(k-j), lambda=(1-2j ell)/(k-j)<0.       (1)

   If lambda=0, its angular zero is flat. At an axis maximizer j is odd. If g has finite order m there, k=m and j=1.
4. If all interior angular zeros are simple, Hdyn holds. More generally it holds if every such zero has finite order and no equilibrium has one of the spectra (1). These are extra assumptions.
5. Let b be the largest positive root of w, when such a root exists. On (b,infinity), either g is identically zero or

       g(x)=G x^(p-1)(1+O(x^(p-1))), G=Theta'(0)!=0.        (2)

   The limit identity also holds in the zero case. If b>0 and Theta'(0)!=0, then g(b)!=0 and w'(b)=A.
6. At the first positive root x_1 of w, if g has finite order m, an odd m implies rho/a<0 somewhere just above the interval to its right. No sign change follows from even m.
7. Under the additional assumption that every equilibrium is nondegenerate, failure of Hdyn gives finitely many equilibria, at least five in the whole plane. Positive horizontal-axis equilibria alternate saddle and source, with the specific spectra below. The off-axis source and saddle counts in each quadrant agree. A parity formula relates axis orders to sign-changing angular zeros when the latter are finite in number and order.

None of the above assumes that rho/a is nonnegative, that zeros have finite order, or that the equilibrium set is finite unless that assumption is explicitly present in the claim.

## 2. Sign transfer and the vertical axis

For X in E with y>0, the factor |Q(X)|^p is positive and Q preserves the upper half-plane. Thus the sign of rho(X)/a equals the sign of Theta(arg Q(X))/a. Every interior angle occurs because Q maps each open quadrant onto that quadrant; the vertical direction occurs on the escaping vertical axis. On K, rho=0. This proves both the negative-value equivalence and the nonnegativity equivalence.

For completeness, the vertical-axis fact used in the dependencies has an elementary direct proof. Put f(y)=rho(0,y), h(y)=W_2(0,y). Near zero, f(y)=ay+O(y^3), h(y)=y+O(y^3), so f/a>0 and h>0. Along the axis, h f'=f. If h had a first positive zero, the scalar flow starting below it would stay in the compact interval between 0 and that zero, while its nonzero density would grow as exp(t)f(y_0). This contradicts boundedness of the smooth density on that interval. Hence h>0 for all y>0, and the same ODE propagates the sign of f. Any nonzero vertical-axis equilibrium is therefore impossible. Reflection gives the lower-axis statement.

## 3. The potential maximum is a critical saddle or degenerate equilibrium

Suppose K is not {0}, and let z maximize P on K. Every orbit through z stays in K, where rho=0. There

    d P(Phi_t X)/dt = grad P.W = |W|^2.                    (3)

Consequently W(z)=0.

No maximizer is a hyperbolic source. To justify this without any finiteness assumption, let B=DW(z) have eigenvalues with positive real parts. The matrix

    M=integral_0^infinity exp(-B^T t)exp(-B t) dt

is positive definite and B^T M+M B=I. Along the reversed nonlinear flow near z, the quadratic function (X-z)^T M(X-z) decreases at a uniform exponential rate. A sufficiently small sublevel set V is backward invariant and all its points converge backward to z. If X in V cap K is different from z, (3) gives

    P(X)-P(z)=integral_-infinity^0 |W(Phi_t X)|^2 dt>0.

The integral converges exponentially; its positivity also follows from any short nonstationary segment. This contradicts maximality. Thus V cap K={z}, which makes z an isolated, relatively open and closed point of the connected set K. Since K has another point, that too is impossible.

Differentiate transport at z:

    DW(z)^T grad rho(z)=grad rho(z).                      (4)

If grad rho(z)!=0, one eigenvalue is 1. Since div W=2ell, the other is A>1; z would be a hyperbolic source. Therefore grad rho(z)=0. In particular rho_x(z)=0, so curl W(z)=0 and DW(z) is a real symmetric matrix. It cannot have both eigenvalues positive. Its trace is 2ell, hence the eigenvalues are lambda<=0 and mu=2ell-lambda>=2ell>1. The origin is a source, so z!=0.

The parities imply P(-x,y)=P(x,y)=P(x,-y). Reflect a maximizing z into the closed first quadrant. It is not on the positive vertical axis by Section 2. If z=(b,0), the interval [0,b] is invariant for the scalar axis flow, and hence lies in K. If w'(b)>0, w<0 immediately to the left of b and

    P(b,0)-P(b-epsilon,0)=integral_(b-epsilon)^b w(s) ds<0,

contradicting maximality. Thus w'(b)<=0 and the fast unstable direction is vertical. Its upper branch lies in the open first quadrant. If z is off-axis, both sufficiently short halves of its strong unstable curve lie in that quadrant.

Every such fast branch is nodal. Its backward distance to z is O(exp(sigma t)) for some 1<sigma<mu. Since rho(z)=0 and rho is smooth,

    |rho(X)|=exp(-t)|rho(Phi_t X)|<=C exp((sigma-1)t) -> 0

as t tends to minus infinity. On the branch, (3) gives P(X)>P(z). Therefore no point of it belongs to K. It escapes forward, and remains in the open quadrant by uniqueness and parity. Distinct halves are distinct trajectories, hence give distinct angular zeros under Q. Reflection about the vertical axis produces a second distinct zero in the upper half-plane, or two more when z is off-axis. All these angles are interior, since Q preserves open quadrants.

## 4. A nodal normal derivative identity

Let X(t) be any nonstationary nodal trajectory. Set q=|W(X(t))|, T=W/q, N=J T, where J is counterclockwise rotation by pi/2, and h=grad rho.N. Since W.grad rho=0 on this orbit, grad rho=hN. Differentiating transport along the flow gives

    d grad rho/dt=(I-DW^T)grad rho.

Using N.N'=0 and q'/q=T^T DW T,

    h'=(1-N^T DW N)h,
    (h/q)'=(1-trace DW)(h/q)=-A(h/q).                    (5)

These are scalar linear identities, including at zeros of h, so no division by h is used.

For a fast branch from the critical equilibrium z of Section 3, grad rho(z)=0 gives |grad rho(X)|<=C|X-z|. On that curve q>=c|X-z| locally because the tangent eigenvalue mu is nonzero. Thus h/q remains bounded as t tends to minus infinity. Formula (5) would make every nonzero h/q grow as exp(-At) in that limit. It must vanish identically. Therefore grad rho=0 along the whole branch.

At a point of the branch in E, differentiating rho=F composed with Q, where F(R,theta)=R^p Theta(theta), gives grad rho=DQ^T grad F. DQ is invertible and Theta=0 there, so grad rho=0 is equivalent to Theta'=0 at the branch angle. This proves the critical-zero assertion. If all interior zeros were simple, Hdyn could not fail.

## 5. Finite transverse order and the saddle spectrum

Use smooth local coordinates (s,n) that straighten one fast branch to n=0, with z=(0,0) and the chosen half s>0. The coordinate directions at z are the fast and slow eigendirections. The vector field has the form

    s'=v(s)+O(n), n'=b(s)n+O(n^2),
    v(s)=mu s+O(s^2), b(s)=lambda+O(s).                    (6)

Suppose the branch angle has finite order k in Theta. The scattering formula and its diffeomorphism show that rho has exactly order k across each nonstationary part of this nodal orbit. Put b_i(s)=partial_n^i rho(s,0)/i!. For s>0 all b_i with i<k vanish identically, while b_k(s)!=0. Smoothness extends the lower vanishing to s=0, and b_k is smooth there. Taylor's theorem in n, including its smooth s-dependence, gives the order-k coefficient equation

    v(s)b_k'(s)+k b(s)b_k(s)=b_k(s).                     (7)

No lower coefficient or derivative of one survives in this equation. For s>0 it integrates to

    b_k(s)=C s^beta E(s), C!=0,
    beta=(1-k lambda)/mu,

where E is smooth and E(0)>0. Indeed [(1-k b(s))/v(s)]-beta/s is smooth at zero, by factoring v(s)=s(mu+O(s)). Since lambda<=0 and mu=2ell-lambda,

    0<beta=k-(2k ell-1)/mu<k.

Smoothness forces beta to be an integer j in {1,...,k-1}; a positive noninteger power has an unbounded derivative after its integer part. Equation (1) follows. In particular lambda<0. If lambda=0, beta=1/(2ell) is noninteger, so no finite k is possible: that angular zero is flat. These arguments also prove the finite-order spectral exclusion of Section 1.

At an axis maximizer z=(b,0), the strong unstable curve is x=b+chi(y) with chi smooth, even, and chi(0)=chi'(0)=0. Choose s=y, n=x-b-chi(y). Reflection sends (s,n) to (-s,n), and rho is odd under that reflection. Hence every b_i(s) is odd. The first nonzero Taylor power j of b_k is therefore odd.

Suppose in addition that g has finite order m at b. The axis ODE in Section 6 gives lambda=-A/(m-1), mu=2ell-lambda. Starting with b_0=0, argue successively for i=1,...,m-1. Once the lower coefficients vanish, b_i obeys (7) with i in place of k, and its exponent beta_i=(1-i lambda)/mu lies strictly between 0 and 1. Smoothness forces b_i=0. At order m,

    b_m'(0)=g^(m)(b)/m! !=0,

because chi'(0)=0. Thus b_m is nonzero on a sufficiently short punctured half. Smooth transport between transverse sections preserves vanishing order, so the full escaping orbit and its angle have order exactly m. Here beta_m=1, proving k=m, j=1.

## 6. Outer-axis asymptotics and the last root

Differentiate the transport equation once in y at y=0. Using div W=2ell and the parities gives

    w g'=(w'-A)g.                                      (8)

Where w!=0, this scalar homogeneous ODE implies that g is either identically zero on the interval or has a fixed nonzero sign. If b is the largest positive root, w>0 on (b,infinity). The exterior symbol bounds imply

    (w'-A)/w=(p-1)/x+O(x^(p-2)).                         (9)

The remainder is integrable at infinity. A nonzero solution has the form (2), with G!=0; its relative error follows by integrating the remainder from x to infinity. In the zero case G=0. The C^1 convergence of the angular rescalings identifies

    Theta'(0)=lim_(x->infinity) x^(1-p)g(x)=G,           (10)

since partial_theta rho(x cos theta,x sin theta) at theta=0 is x g(x).

Assume G!=0 and b>0. Set alpha=w'(b)>=0, which follows from w>0 to the right. The scalar orbit x(t)>b tends to b as t tends to minus infinity. If alpha=0, the transport equation along it is g_dot=(w'(x(t))-A)g. Its coefficient tends to -A. Every nonzero g would therefore grow exponentially backward, contradicting boundedness near b. Thus alpha>0. If g(b)=0, smoothness and the simple root of w imply that g/w is bounded near b, whereas

    d(g/w)/dt=-A(g/w).                                  (11)

This again contradicts nonzero bounded backward behavior. Thus g(b)!=0. Evaluating (8) at b now forces alpha=A, as asserted. No assertion about g at the last root is made when G=0.

## 7. First-root parity and nondegenerate counting

Let x_1 be the first positive root of w. Then w>0 and g/a>0 on (0,x_1). At any simple root b with alpha=w'(b)!=0 and a nonzero adjacent g, smooth division gives

    g'/g=(1-A/alpha)/(x-b)+H(x),

where H is smooth. On either punctured side,

    g=C_side |x-b|^(1-A/alpha) E(x),                    (12)

with E smooth and positive. Smoothness and nonzero C_side force the exponent to be a nonnegative integer. If alpha<0, it is an integer m>=2 and alpha=-A/(m-1). If alpha>0, it is less than 1 and must equal 0, so alpha=A and g(b)!=0. Matching the first nonzero derivative forces a nonzero coefficient on the other side. The sign flips at a downward root exactly when m is odd, and does not flip at an upward root.

In particular an odd finite order m at the first root makes g/a<0 immediately to its right. Since rho(x,y)/y tends to g(x) as y tends to zero, rho/a is negative in an open region just above that axis interval. One can choose any compact subinterval on which g/a<0 and then a uniform small positive y-range. Section 2 transfers this to a negative angular value. At a degenerate first root the separately proved flat-jet alternative is not replaced by (12); no parity-based sign conclusion is drawn there.

Now impose that every equilibrium is nondegenerate. They are all in a compact set. An infinite sequence would accumulate at an equilibrium where the inverse function theorem for W forbids other nearby zeros. Hence there are finitely many. If Hdyn fails, w has a positive root. Since w>0 near zero and for sufficiently large x, all simple positive roots number 2J, J>=1, and alternate downward and upward crossings. Repeatedly applying (12) propagates nonzero g on every interval and gives:

    downward roots: (-A/(m_j-1), 2ell+A/(m_j-1)), m_j>=2;
    upward roots: (A,1), g!=0.                           (13)

Thus the whole plane has at least the origin, one symmetric saddle pair and one symmetric source pair, for at least five equilibria. If M=sum_(j=1)^J m_j, the exterior sign of g/a is (-1)^M.

Every nondegenerate equilibrium is a source or saddle. Indeed a nonzero density gradient forces eigenvalues (1,A) by (4), while a zero density gradient makes DW symmetric, and the trace is positive. The origin has index +1, axis sources and saddles cancel in total index, and no nonzero vertical-axis equilibria exist. On a sufficiently large circle W is homotopic through nonzero fields to ell X, with winding number 1. Removing small disks about the finitely many zeros and applying Stokes to

    (W_1 dW_2-W_2 dW_1)/|W|^2

shows that the sum of their local indices equals 1. Reflections preserve the determinant sign and group off-axis equilibria into quadruples. Therefore each quadrant contains equally many off-axis sources and saddles.

The exterior g is nonzero, so (10) gives Theta'(0)!=0. If all first-quadrant angular zeros are finite in number and order, exactly the odd-order ones change sign. Near pi/2 the sign is that of a, while near 0 it is the sign of g in (2). Thus, writing N_odd for the number of odd-order zeros in (0,pi/2),

    N_odd = sum_j m_j modulo 2.                          (14)

Even-x reflection pairs upper-half-plane angular zeros with the same order and excludes pi/2 as a zero. Without the stated finiteness and order hypotheses, no finite counting formula is asserted.

## 8. A local coupled model with an even-order axis saddle

For every ell>1 and kappa>0 let A=2ell-1 and define smooth fields on R^2 by

    psi=(ell x-(A/kappa)sin(kappa x))y,
    U=(-psi_y,psi_x),
    W=((A/kappa)sin(kappa x), (2ell-A cos(kappa x))y),
    rho=A(1+cos(kappa x))y.                               (15)

They have the required parities and satisfy the coupled equations pointwise. In detail div W=2ell, curl W=A kappa sin(kappa x)y=-rho_x, and

    W.grad rho=A y[-A sin(kappa x)^2
                     +(2ell-A cos(kappa x))(1+cos(kappa x))]
              =A y(1+cos(kappa x))=rho,

because 2ell-A=1. Their center slope is a=2A and c=psi_xy(0)=ell-A=1-ell. At b=pi/kappa,

    w'(b)=-A,
    g(x)=(A kappa^2/2)(x-b)^2+O((x-b)^4),
    DW(b,0)=diag(-A,4ell-1).

This realizes the local k=2,j=1 saddle resonance and a nonnegative density in the upper half-plane, with no sign reversal at that saddle.

This is not an admissible profile: at x=0 its density grows linearly in y, and on y=0 its velocity has U_1=-ell x+bounded. Both the sublinear density condition and U=o(r) fail. Its infinitely many axis roots also lie outside the compact-trapped-set setting. It refutes the assertion that the local coupled equations force odd transverse order or a sign reversal at every saddle; it is not a counterexample to any global theorem under the primary hypotheses.

## 9. A sufficient radial condition

If there is eps>0 with X.U(X)>=-(ell-eps)|X|^2 everywhere, then X.W(X)>=eps|X|^2. Thus W has no nonzero equilibrium. More directly, along any nonzero orbit d|X|^2/dt>=2eps|X|^2, so it escapes forward and tends to zero backward. Completeness follows from the already established global bounded first derivative of W. This proves Hdyn. The condition is additional; constant positive divergence alone does not imply it. A sufficient stronger condition is sup_X ||DU(X)||<ell, since U(0)=0 and integration along a segment bounds |U(X)| by sup||DU|| |X|.

## 10. A canonical non-profile that tests both residual normalizations

Fix ell=2 and a in {1,-1}. Set tau=-2+(5/2)a and

    rho=a y(1+r^2)^(-1/4)(1-2x^2/(1+r^2))
                         +4tau x^2 y exp(-r^2).

Take its canonical velocity. These are smooth sublinear fields with the required parity, a0=a, and vertical-axis coefficient K_v=a. Their center strain is exactly -1. To prove the latter, the third sine coefficient of the first summand is -(a/2)r^3(1+r^2)^(-5/4). The canonical formula c=-a/4+integral rho_3/r^2, justified by the cancellation and endpoint arguments in ../inverse/PROOF.md, gives c_base=-5a/4 because integral_0^infinity r(1+r^2)^(-5/4)dr=2. The Gaussian summand has third coefficient tau r^3 exp(-r^2) and strain tau/2. The chosen tau therefore makes c=-1. Neither the slope nor the far-field trace is changed by the Gaussian summand.

The leading angular density is

    Theta=a sin(theta)(1-2cos(theta)^2).

It has simple zeros at pi/4 and3pi/4. This contradicts no theorem because transport fails. In detail, for a=1,p=1/2 the leading angular source p cos(theta)Theta-sin(theta)Theta' is

    -sin(2theta)+(5/8)sin(4theta).

The angular inverse -Phi''-(3/2)^2 Phi=source gives

    Phi=-(4/7)sin(2theta)+(1/22)sin(4theta),
    u_r=-Phi', u_theta=(3/2)Phi.

At theta=pi/4, Theta=0, Theta'=sqrt(2), u_theta=-6/7. Hence the leading nonlinear coefficient is B=-6sqrt(2)/7. The actual density has no r^0 correction: its next term is O_symbol(r^(-3/2)). The canonical inverse bounds imply U=a r^(1/2)u+O(1); multiplied by grad rho=O(r^(-1/2)), the error vanishes. It follows that on this ray

    R -> -6sqrt(2)/7

for either sign of a. More precisely rho and X.grad rho tend to zero, while U.grad rho tends to this nonzero limit, so |R|/Nv tends to1. On the other hand the two scaling transport components have opposite leading terms of magnitude sqrt(2)r^(1/2), giving

    Nf ~ 2sqrt(2)r^(1/2),
    |R|/Nf ~ (3/7)r^(-1/2) ->0.

Thus a decaying Nf ratio alone can conceal a fixed absolute defect on a nodal ray. The independent numerical test uses both denominators, checks the origin strain by velocity extrapolation and recomputes the far defect. This example is a non-profile even though it satisfies the canonical inverse, center relation, smoothness and sublinear growth. It does not address the existence of any exact sign-changing or negative-slope profile.

## 11. Strain required by a critical escaping zero of finite order

Continue with the exact-profile hypotheses and critical potential maximizer q of Sections3-5. We proved grad rho(q)=0 and that DW(q) has eigenvalues lambda<=0 and mu=2ell-lambda. Since curl U(q)=-rho_x(q)=0 and div U=0, the matrix DU(q)=DW(q)-ell I is real symmetric and traceless. Its eigenvalues are lambda-ell and ell-lambda. Hence

    |DU(q)|_op=ell-lambda, |DU(q)|_Frob=sqrt(2)(ell-lambda).

If the escaping far zero has finite order k>=2, the already proved resonance gives j mu+k lambda=1 for some integer1<=j<=k-1. Solving it yields

    -lambda=(2j ell-1)/(k-j) >= (2ell-1)/(k-1).

The inequality follows by cross multiplication: its numerator difference is (j-1)(2k ell-1)>=0. Therefore

    |DU(q)|_op >= ell+(2ell-1)/(k-1).

In particular a double zero forces j=1 and |DU(q)|_op=3ell-1, with Frobenius norm sqrt(2)(3ell-1). For larger k the displayed value is a lower bound. A flat zero is not covered by this finite-order resonance estimate. These are necessary strains at the critical maximizer of an exact profile; they do not follow just from an angular zero of an arbitrary field.

## 12. Scope of the audit

These arguments independently confirm the five consequences in the lead's 17:25 UTC request and the critical-zero and resonance extensions in its independent hdyn3 draft. Their use of smoothness, scattering, nodal invariance and the potential is explicit above. Degenerate equilibria, flat angular zeros, even-order nodal branches and negative a remain possible within the analysis. No verified condition forces Hdyn in the full admissible class, and even Hdyn would not by itself prove existence or nonexistence. Numerical sampling cannot certify the absence of a flat zero or every equilibrium.

