# Full Holder regularity of the divided first velocity and the turning obstruction

## Statements, spaces and scope

Fix 0<alpha<1. Let h(x,y)=x^2 g(x,y) be even in x, compactly supported in [-L,L]^2, with g bounded and uniformly C^alpha in y. Its value at x=0 can be assigned arbitrarily. Set

 K=||g||infinity+sup_x [g(x,.)]C^alpha(R).

Assume h is continuous, so its canonical IPM velocity agrees with the usual order-zero multiplier. Use the convention

 U1[h]^hat(xi,eta)=xi eta/(xi^2+eta^2) h^hat(xi,eta).

Then U1[h]/x has a continuous extension through x=0 and

 ||U1[h]/x||C^alpha([-L',L']xR)<=C_(alpha,L,L') K.       (1)

Here the full two-variable C^alpha norm includes the supremum. No horizontal regularity of g, no bound for partial_x h, and no bound for partial_x U1 are hypotheses. The constant is qualitative. The proof below also applies by approximation to bounded measurable g with the stated uniform vertical regularity.

For the exact normalized joined trial of proof 232, let Z2_(alpha,beta,gamma) and D2 be EXACTLY the physical-parity Banach space and maximal transport graph domain of proof 228. Thus

 k=1615536043799051/9007199254740992, ell=1/k,
 2k-1<beta<k, gamma>4k,
 ||h||Z2=||chi h||E2+sup_(R=2^j,j>=0) R^(-beta) N_R(h)
                         +||h||L2((1+r^2)^(-gamma/2)),
 N_R(h)=||h||infinity+R^alpha[h]_(x,alpha)
                         +R^(2+alpha)[h]_(y,2,alpha),
 D2={h in Z2:V.grad h in Z2 in distributions}, V=ell X+U[rho0].

The annular seminorms have both endpoints in R<=r<=4R; the vertical one divides by x^2|Delta y|^alpha. E2 is the corresponding unscaled global directional norm. The cutoff chi is smooth radial, one on B2 and zero outside B4. All functions are even in x, odd in y, continuous and zero on the vertical axis. The full coupling is C0 h=U[h].grad rho0+c[h]M0, and Cren h=U[h].grad rho0+c[h]H0, with the exact normalized moving-tail column M0 and compact cubic column H0 of topics217,228. T=V.grad-1, A0=T+C0 and Lren=T+Cren are closed on D2 by proof 228.

The following strengthening of the divided bound of proof 228 holds, for h in Z2 and on every fixed comparable-radius annulus with R>=2:

 ||U1[h]/x||infinity+R^alpha[U1[h]/x]C^alpha
                                      <=C ||h||Z2 R^(beta-1).  (2)

The Holder seminorm in(2) is in BOTH variables. The same estimate, with changed constants and scale bounded above and below, holds on compact annuli away from the origin.

With the actual simple turn certified in proof 232, all three maps T,Lren,A0:D2->Z2 are NOT onto whenever alpha>1/2. This improves proof 232's full-coupling threshold alpha>2/3. It does not decide alpha<=1/2, the range of the actual residual, injectivity, the dimension of the cokernel, a global inverse in other spaces, or nonlinear existence. No new arithmetic certificate is needed. The actual turn and the stationary-phase construction are those already derived in proof 232; their separate independent audit is pending. This proof is an independently derived strengthening, also pending that audit and its own independent review.

## Partial Fourier kernel and dyadic facts

Write D=partial_y and B=|D_y|. Fourier inversion in x of (xi^2+eta^2)^(-1) gives e^(-|eta||x-s|)/(2|eta|). Applying -partial_x partial_y yields the exact formula

 U1[h](x,.)=(1/2)D integral_R sign(x-s) e^(-|x-s|B)h(s,.) ds.  (3)

The sign is consistent with the specified positive multiplier. Its distributional x derivative is

 F(x):=partial_x U1[h](x)
       =D h(x)-(1/2)D B integral_R e^(-|x-s|B)h(s) ds.        (4)

Use a smooth homogeneous dyadic partition in the y frequency, supported where c lambda<=|eta|<=C lambda with lambda=2^j, j in Z. Set g_j=Delta_j^y g and h_j=x^2 g_j. The horizontal support remains [-L,L]. For j>=0, vertical Holder regularity and the zero integral of the dyadic kernel give

 G_j:=||g_j||infinity<=C K lambda^(-alpha).                 (5)

For j<0 boundedness gives G_j<=C K. Since g has uniformly bounded compact y support, the homogeneous low-frequency remainder tends to zero; this also follows directly from its convolution bound C K L 2^j. Thus the dyadic sum represents h distributionally and uniformly in the usual increasing frequency truncations.

For a function supported in this y-frequency band and any nonnegative integers m,n, the y convolution operator D^m B^n e^(-u B) has L1 kernel norm at most

 C_(m,n) lambda^(m+n) exp(-c lambda u), u>=0.               (6)

A fattened smooth band cutoff is inserted in this formula. To see(6), rescale eta=lambda z. On the fixed two-sided compact annulus, each of the first two z derivatives of (iz)^m|z|^n exp(-lambda u|z|) times the cutoff is bounded by a polynomial in lambda u times exp(-c0 lambda u). Absorb the polynomial by decreasing c0. Two integrations by parts in the inverse Fourier integral give an integrable bound C exp(-c lambda u)(1+|y|)^(-2). Scaling gives(6). The same argument proves the band Bernstein estimate ||D v||infinity<=C lambda||v||infinity.

These facts hold with constants independent of j,u,x. Absolute convergence of the x integrals follows from compact horizontal support and(6). We use only finite derivative orders below.

## A uniform bound on each divided velocity block

Let u_j=U1[h_j], q_j=u_j/x, and G=G_j, lambda=2^j. All norms below are uniform in y and in |x|<=L'. Evenness of h_j makes u_j odd in x, so u_j(0)=0. We show

 for lambda>=1: ||q_j||infinity<=C G,
                  ||partial_x q_j||infinity<=C lambda G;   (7)
 for lambda<=1: ||q_j||infinity+||partial_x q_j||infinity
                                                    <=C lambda G. (8)

The derivative is a weak derivative when the x dependence is merely measurable. The corresponding Lipschitz representative is used.

First suppose lambda>=1. Extending the elementary upper bound |h_j(s)|<=s^2 G to all real s can only increase the following integrals. For every x,

 integral_R exp(-c lambda|x-s|) s^2 ds
                           <=C(lambda^(-1)x^2+lambda^(-3)). (9)

Equations(3),(4),(6),(9) imply

 |u_j(x)|<=C G(x^2+lambda^(-2)),
 |partial_x u_j(x)|<=C lambda G(x^2+lambda^(-2)).           (10)

When |x|>=lambda^(-1), divide the first bound by |x| and use

 partial_x q_j=(partial_x u_j)/x-u_j/x^2

to get |q_j|<=C G(|x|+lambda^(-1)) and |partial_x q_j|<=C G(lambda|x|+1). These imply(7) on this part of the bounded strip.

For |x|<=lambda^(-1), write the second term in(4) as H(x). It is even in x. Since

 partial_x^2 e^(-|x-s|B)=B^2 e^(-|x-s|B)-2B delta_(x=s),

we have in distributions

 H''(x)=-(1/2)D B^3 integral e^(-|x-s|B)h_j(s)ds
                                      +D B^2 h_j(x).      (11)

Equations(6),(9), and |x|<=lambda^(-1) give |H''(x)|<=C lambda G. The convolution term H has a continuous first derivative; equivalently(11) gives H in W^(2,infinity) on this strip. Its evenness gives H'(0)=0. Therefore

 |H(x)-H(0)|<=C lambda G x^2,
 |D h_j(x)|<=C lambda G x^2,
 |F(x)-F(0)|<=C lambda G x^2.                              (12)

At the axis, (4),(6),(9) give |F(0)|=|H(0)|<=C G/lambda. Since u_j is odd,

 q_j(x)=integral_0^1 F(tx)dt,
 partial_x q_j(x)=(F(x)-integral_0^1 F(tx)dt)/x.            (13)

The identities hold almost everywhere, extend by continuity, and do not differentiate h_j in x. Equations(12),(13) yield |q_j|<=C G/lambda and |partial_x q_j|<=C lambda G|x|. This proves(7) in the remaining strip and gives its continuous axis value.

For lambda<=1 use compact horizontal support rather than(9). For |x|<=L', the integral in(4) is bounded by C_L G, so |F(x)|<=C lambda G. Thus(13) gives |q_j|<=C lambda G. The input term D h_j(x) has magnitude C lambda G x^2 and value zero at x=0. Formula(11) gives |H''|<=C(lambda^4+lambda^3)G<=C lambda^3 G on this strip. Evenness again implies |F(x)-F(0)|<=C lambda G x^2. Equation(13) gives |partial_x q_j|<=C lambda G|x|<=C lambda G. This proves(8). The constants depend only on L,L' and the chosen dyadic cutoff.

Every q_j retains its y frequency support. Hence the Bernstein estimate and(7) give ||partial_y q_j||infinity<=C lambda G for lambda>=1. For lambda<=1,(8) gives the stronger bound C lambda^2 G, in particular C lambda G. From(5),(7), for a pair of points at distance d<=1 in the output strip,

 |q_j(X)-q_j(X')|<=C K min(lambda^(-alpha),
                                       d lambda^(1-alpha)), j>=0. (14)

Sum j below and above the integer where lambda d is about1. The two geometric series are bounded by C_alpha K d^alpha since 0<alpha<1. The high-frequency suprema are summable as well. For j<0,(8) is summable and gives a Lipschitz norm bounded by C K. Thus sum_j q_j converges uniformly, satisfies(1), and defines the continuous extension through x=0. Distributionally x sum_j q_j=U1[h], by(3) and dyadic reconstruction. It is consequently the canonical quotient. This proves(1).

## Scaling and the complete annular estimate

Put N=||h||Z2. Proof 228's parity comparison, repeated here, gives |h(x,y)|<=C N x^2 R^(beta-2) on a comparable-radius annulus by comparing (x,y) with (x,-y). Smooth radial localization to that annulus preserves the divided vertical seminorm. After X=R Z and amplitude division by R^beta, the localized density is Z_1^2 g(Z), with g bounded and uniformly vertically C^alpha by C N; it has compact support in a fixed rectangle. Formula(1) applies, and homogeneity of the order-zero canonical velocity proves(2) for this comparable-radius part.

Split the rest of the density into |Y|<R/4 and |Y|>8R with smooth overlapping transitions. For the inner part, beta>-2 gives L1 mass at most C N R^(beta+2). Separated kernels and their first two output derivatives are O(R^(-2)), O(R^(-3)), O(R^(-4)). Near x=0 in the output annulus, y is comparable to R, so the whole segment from (0,y) to (x,y) remains separated from the source. Odd-x parity gives

 U1(x,y)/x=integral_0^1 partial_x U1(tx,y)dt.

Both its x and y derivatives are bounded by the second kernel derivatives, C N R^(beta-2), and its value by C N R^(beta-1). Away from this axis neighborhood division by |x| comparable to R gives the same estimates. The outer part uses the canonical subtraction: its kernel is O(R|Y|^(-3)), its first derivative O(|Y|^(-3)), and its second derivative O(|Y|^(-4)). Integration against |h(Y)|<=C N |Y|^beta converges because beta<1 and gives the identical bounds. All near-axis segments remain separated from this outer source. Distant point pairs use the supremum, and nearby pairs use these derivatives on enlarged comparable annuli. This proves the full C^alpha estimate(2). The fixed compact-annulus version follows by the same decomposition, with the local E2 factor covering bounded source radii and the scaled norm controlling the remote tail.

## Stronger all-future coupling difference

Use the actual simple turning height s_* of proof 232. It is certified strictly inside one analytic cell, with a=V1/x satisfying a(0,s_*)=0 and a_y(0,s_*)>0. Choose a small initial-height interval I strictly below it, with a(0,y) nonzero on I. For trajectories Phi_t(q,y)=(x_t,y_t), q small and y in I, proof 232 proves uniformly for all t>=0

 x_t comparable to q exp(ell t), r_t comparable to exp(ell t),
 |Delta x_t|<=C q exp(ell t) delta,
 |Delta y_t|<=C exp(ell t) delta, delta=|y-y'|.             (15)

These are actual orbits, including their full infinite future. The estimates follow from V1=x a, the positive vertical axis speed, and the integrability of the exact far errors DV-ell I and Da along the orbit.

Set a1=rho0_x/x and a2=rho0_y/x^2. At far radius r,

 a1=O(r^(k-2)), a2=O(r^(k-3)),
 (U[h].grad rho0)/x^2=a1(U1[h]/x)+a2 U2[h].               (16)

Their first derivatives cost r^(-1). Proof 228 gives ||U2||infinity+r^alpha[U2]C^alpha<=C N r^beta. Formula(2) supplies the same full two-variable estimate for U1/x with degree beta-1. Comparing the points in(15), whose total separation is O(r delta), proves

 |Delta[(U[h].grad rho0)/x^2]|<=C N r^(beta+k-3)delta^alpha.

Also |Delta(x_t^2)|<=C q^2 r^2 delta. Consequently the UNDIVIDED complete velocity coupling satisfies

 |Delta(U[h].grad rho0)(Phi_t)|
                    <=C N q^2 r_t^(beta+k-1)delta^alpha.  (17)

On the bounded initial portion the same estimate holds with radius bounded. Multiplication by e^(-t) makes the far integral converge because

 ell(beta+k-1)-1=ell(beta-1)<0.

The strain column contributes at most C N q^2 delta after integration: bounded c, smooth compact H0, and the exact M0 cofactor bound O(r^(2k-3)(1+log r)) with one more derivative costing r^(-1) give exponent ell(2k-1)-1=1-ell<0. Since delta<=delta^alpha, (17) proves for C=Cren or C0

 |integral_0^infinity e^(-t)
       [Ch(Phi_t(q,y))-Ch(Phi_t(q,y'))]dt|
                                      <=C N q^2 delta^alpha. (18)

This removes the factor q^(alpha-1) in proof 232's cruder difference estimate. No bound on horizontal derivatives of h or of U1 is used.

## Non-surjectivity on the exact maximal domain

For completeness, here is how(18) combines with the forcing and turning construction of proof 232. Take f_(epsilon,q)=x^2 phi(x/q)cos(x/epsilon)g_*(y), even in x and odd in y, where g_* is smooth near the two reflected turning heights and positive at s_*; phi is a compact cutoff equal to one along the trajectory passage near the positive turn. Subtract a smooth compact zero-jet function supported outside the thin trajectory cone times its bounded strain coefficient to enforce c[f]=0. All forcings have J=0. Their Z2 norms are bounded independently of epsilon,q provided q^2<=epsilon^alpha: the horizontal oscillatory bound is C q^2 epsilon^(-alpha), the cutoff variation is C q^(2-alpha), and the divided vertical bound is fixed. All supports lie in a fixed compact annulus and the correction has uniformly bounded norm.

Parametrize the orbit passage by height s. Its abscissa X(s;q,y) satisfies dX/ds=V1(X,s)/V2(X,s), X(y;q,y)=q. In the analytic turn neighborhood, X/q tends smoothly to Lambda(s;y)=exp(integral_y^s a(0,v)/V2(0,v)dv). The phase X/q has exactly one nondegenerate critical point, because a_y(0,s_*)>0, and its critical value v_q(y) has derivative bounded away from zero on I because a(0,y) is nonzero there. Keep the EXACT q-dependent phase. Uniform one-dimensional stationary phase, with compact smooth amplitude positive at the critical point, gives, for lambda=q/epsilon tending to infinity,

 I_f(q,y)=integral_0^infinity e^(-t) f(Phi_t(q,y))dt
 =q^2 lambda^(-1/2)B_q(y)cos(lambda v_q(y)+pi/4)
                                          +O(q^2/lambda),

with B_q bounded below positively and uniformly C1. Proof 232 supplies a complete elementary stationary-phase proof and uniform derivative bounds. Choose y,y' tending to a fixed point of I at distance comparable to lambda^(-1) so the two cosine values are1 and-1. Then

 |I_f(q,y)-I_f(q,y')|>=b q^2 lambda^(-1/2).               (19)

The zero-strain correction vanishes along these orbits. For any maximal-domain solution (T+C)h=f, the distributional flow-box equation and local continuity give

 h(q,y)=-I_f(q,y)+integral_0^infinity e^(-t)Ch(Phi_t(q,y))dt.

The terminal term vanishes by beta<k and the annular supremum bound. This uses the exact maximal domain, without any smooth-core density assumption. The input-space vertical norm gives |h(q,y)-h(q,y')|<=C N q^2|y-y'|^alpha. Equations(18),(19) therefore imply

 b q^2 lambda^(-1/2)<=C N q^2 lambda^(-alpha).            (20)

For T the coupling integral is absent and the same inequality follows. If any of these closed operators were surjective from its Banach graph domain onto Z2, the open mapping theorem would give choices of preimages with ||h||Z2<=K||f||Z2, with uniform K. Injectivity or a bounded linear right inverse is not required. Choose epsilon=n^(-1), q=n^(-kappa), with alpha/2<kappa<1. Then q^2<=epsilon^alpha and lambda tends to infinity. The bounded forcing norms make N uniformly bounded, whereas(20) forces N>=c lambda^(alpha-1/2). This is impossible for alpha>1/2. The stated non-surjectivity follows.

## Dependencies and verification

The new analytic content is(1),(2),(18), proved above. Proof 228 supplies exact spaces, bounded full coupling, closedness and the ordinary annular velocity estimates. Proof 232 supplies the independently computed simple-turn certificate, actual all-future orbit bounds, exact forcing construction, uniform stationary-phase lemma and maximal-domain characteristic argument. The latter steps have been restated above to specify exactly how the stronger estimate changes the threshold. All arithmetic and operators refer to the same normalized joined trial. Separate independent review is required before team theorem adoption. No assertion at alpha=1/2 is made; the geometric series and stationary-phase argument above provide no contradiction at that endpoint.
