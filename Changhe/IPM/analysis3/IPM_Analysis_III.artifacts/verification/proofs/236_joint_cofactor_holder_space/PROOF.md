# A joint cofactor Holder space: mapping, exterior inverse and the remaining normalization problem

## Exact setting and statements

Use the exactly joined normalized trial rho0, the canonical velocity U, strain c, compact cubic column H0 and full moving-tail column M0 from topics217 and228. Set

 k=1615536043799051/9007199254740992, ell=1/k, p=2k-1,
 0<alpha<1, p<beta<k, gamma>4k,
 w_gamma(X)=(1+|X|^2)^(-gamma/2), V=ell X+U[rho0].

Fix a smooth radial chi in [0,1], one on B2 and zero outside B4. For A_R={R<=|X|<=4R}, let [g]_(alpha;A_R) be the full Euclidean two-point Holder seminorm, with both endpoints in A_R and no segment condition. Put

 M_R(g)=||g||_(infinity;A_R)+R^alpha[g]_(alpha;A_R).

Define Z3 as the real space of functions h=x^2 g, where g is continuous on the whole plane, even in x and odd in y, and

 ||h||Z3=||chi g||C^alpha(R2)
       +sup_(j>=0) (2^j)^(2-beta) M_(2^j)(g)
       +||h||L2(w_gamma)<infinity.                       (1)

The continuous cofactor g is uniquely determined by h, including on the vertical axis. This is a space of physical functions, not an abstract product with an additional axis coordinate. The following are qualitative statements; no numerical constants or numerical exterior radius are provided.

1. Z3 is Banach and embeds continuously into Z2 of proof 228. The full coupling C0h=U[h].grad rho0+c[h]M0 and Crenh=U[h].grad rho0+c[h]H0 are bounded on Z3. The actual residual F0 is in Z3. For a smooth radial tau_R, zero on B_R and one outside B_(2R),

 ||tau_R C0||_(Z3->Z3)
 <=C{R^(k-1)+R^(beta+k-gamma/2)
       +(R^(p-beta)+R^(2k-gamma/2))(1+log R)} ->0.       (2)

2. T=V.grad-1, Lren=T+Cren and A0=T+C0 are closed on the same exact maximal domain

 D3={h in Z3:V.grad h in Z3 distributionally}.           (3)

The physical cubic jet J(h), when defined on smooth inputs as the coefficient of x^2 y, is not closable even on smooth zero-strain inputs in this graph.

3. On Omega_R={r>R}, define F_R^(3) by h=x^2g with g continuous on the closure, the same parities, and norm

 ||h||F_R^(3)=sup_(j>=0) r_j^(2-beta) M_(r_j)(g)
                  +||h||L2(Omega_R,w_gamma), r_j=2^j R.

There is no prescribed value on r=R. For sufficiently large R the actual transport T_R is a bijection from its distributional maximal graph D_R^(3) onto F_R^(3), with inverse norm bounded independently of R. If eta_R is smooth radial, zero for r<=5R/4 and one for r>=2R, let E_Rh=eta_Rh on Omega_R and zero inside, and let P_R be exterior restriction. Then

 A_R^(3)=T_R+P_R C0 E_R:D_R^(3)->F_R^(3)               (4)

is also a closed bijection for large R, with uniform inverse bound. The exact transition discrepancy is

 A0(E_Rh)-A_R^(3)h=(eta_R-1)T_Rh+h V.grad eta_R.       (5)

These results do not give a global inverse on Z3, a Fredholm theorem, a closed cubic normalization or nonlinear existence. Proof 234's theorem on Z2 does not decide surjectivity on Z3: its bounded forcing sequence is not bounded in(1). We make no claim about the range of F0 or the dimension of any cokernel on Z3.

## Norm comparisons and completeness

The dyadic annuli overlap. Bounds for M_R on this grid imply bounds on each fixed comparable-radius enlargement, with constants independent of R. For pairs at distance less than a small fixed multiple of R, choose a neighboring dyadic annulus containing both; for more separated points use their supremum bounds. A finite chain of these comparisons covers any fixed enlargement. The grids 2^j and R2^j are equivalent on their common exterior by the same argument.

The supremum bound gives |g|<=CN R^(beta-2), hence |h|<=CN R^beta. On an annulus, multiplication by x^2 gives

 ||h||infinity+R^alpha[h]_(x,alpha)<=C R^2 M_R(g),
 R^(2+alpha)[h]_(y,2,alpha)=R^(2+alpha)[g]_(y,alpha)
                                      <=R^2 M_R(g).

The horizontal product estimate uses |x^2-x'^2|<=CR|x-x'| for nearby points and the supremum for distant ones. Locally multiplication by x^2 sends chi g in C^alpha to chi h in E2 with a bounded norm. The cofactor itself, rather than a bound inferred from a pointwise jet, supplies the divided vertical estimate. Thus Z3 embeds into Z2 and c is bounded by proof 228.

For completeness, a Cauchy sequence in(1) has cofactor limits uniformly on every compact set and in each indicated Holder norm, with consistent limits on overlaps. Its weighted h limit agrees locally with x^2g and has finite weighted norm. Passing the difference estimates to the limit and then the uniform supremum over all annuli proves convergence in(1). The value of g on x=0 is the limit from x!=0; distinct cofactor values cannot represent the same continuous h. This proves the Banach assertion.

Smooth radial cutoffs with scale-R derivative bounds multiply M_R with uniform constants. For pairs crossing a cutoff boundary, use the global smooth cutoff's difference bound and the cofactor supremum; no segment through an excluded inner disk is required. The same argument applies to a smooth even-even coefficient whose scaled supremum and first derivative are bounded. These facts also prove the stated extension and restriction norm bounds.

## Full divided velocity and complete mapping

Write N=||h||Z3. Proof 234 proves the following stronger consequence of Z2 membership on all fixed comparable-radius annuli with R>=2:

 ||U[h]||infinity+R^alpha[U[h]]C^alpha<=CN R^beta,
 ||U1[h]/x||infinity+R^alpha[U1[h]/x]C^alpha<=CN R^(beta-1). (6)

Both seminorms are full two-variable seminorms. The second conclusion is not inferred from ordinary regularity of U1. Its proof is the partial Fourier kernel in y, applied to compactly localized h=x^2g, and the inner/comparable/outer decomposition with two separated-kernel derivatives. It needs only -2<beta<1 and bounded vertical Holder cofactors, so it applies here.

The corresponding fixed-disk bounds hold at the origin. To see this without dividing an ordinary Holder estimate by x, localize h with a radial cutoff supported in a fixed disk. Its cofactor is bounded and C^alpha, and the compact quotient lemma of proof 234 gives U1/x in full C^alpha. The ordinary compact Riesz estimate gives U2 in C^alpha. The remote part has the canonical subtracted kernel; its first two output derivatives are integrable against the tail |h(Y)|<=CN|Y|^beta because beta<1. Odd-x parity gives U1/x as the integral of its first x derivative along the horizontal segment. Its full first derivatives are bounded using the second kernel derivatives. This proves the required disk estimates and the continuous axis extension.

Let a1=rho0_x/x and a2=rho0_y/x^2. The exact finite-mode background gives on distant annuli

 M_R(a1)<=C R^(k-2), M_R(a2)<=C R^(k-3).

Both divisions extend continuously across the axis and are locally Lipschitz at the origin. Indeed rho0=x^2y+O(r^5) with its exact finite divided angular expansion; its divided derivatives are a1=2y+O(r^3), a2=1+O(r^2), with bounded first derivatives there. The C6 radial joins away from zero provide more regularity than needed. Therefore the identity

 (U[h].grad rho0)/x^2=a1(U1[h]/x)+a2 U2[h]              (7)

holds with a full C^alpha cofactor on every compact set and

 M_R((U[h].grad rho0)/x^2)<=CN R^(beta+k-3).            (8)

This is the new horizontal cofactor bound needed for(1).

Multiplication by R^(2-beta) in(8) yields R^(k-1). Integrating its physical pointwise bound CN r^(beta+k-1) gives the weighted tail CN R^(beta+k-gamma/2). This exponent is negative because beta<k and gamma>4k. The exact full column has M_R(M0/x^2)<=C R^(p-2)(1+log R), and its local cofactor is C^alpha, by the exact differentiated finite-mode formula in proof 217. Its weighted tail is C R^(2k-gamma/2)(1+log R). These facts and bounded c give(2), including the cutoff-crossing pairs. All exponents in(2) are strictly negative.

The residual has M_R(F0/x^2)<=C R^(p-2), and its origin cofactor is O(r^3) with bounded first derivative, from the exact normalized cubic cancellation and finite divided origin expansion. The joins have at least the regularity needed for C^alpha. Its weighted norm is finite for gamma>4k. Consequently F0 is in Z3. The compact column H0 has a locally Lipschitz cofactor and is in Z3. This proves the mapping claims for C0,Cren and the unnormalized velocity coupling.

Convergence in Z3 implies local uniform convergence of h and thus distributional convergence. If h_n and V.grad h_n converge in Z3, multiplication and distributional differentiation identify the second limit with V.grad h. Thus(3) is closed. Subtracting the bounded coupling gives equality of the full-expression and transport maximal domains and proves closedness of Lren and A0. This argument does not assume smooth functions are dense in a Holder norm.

## Nonclosability of the physical cubic jet

Choose a smooth radial cutoff zeta, one near zero and compactly supported in B1, and put

 H(X)=x^2 y zeta(X), h_epsilon(X)=epsilon^3 H(X/epsilon)
                                      =x^2 y zeta(X/epsilon).

Then J(h_epsilon)=1. Its cofactor g_epsilon=y zeta(X/epsilon) has C^alpha norm at most C epsilon^(1-alpha). Thus h_epsilon tends to zero in Z3, including its weighted L2 norm.

Near the origin write V=Vlin+W, Vlin=(-A x,D y), A=2ell-1, D=4ell-1. The exact divided origin expansion gives W1=x O(r^2), W2=y O(r^2), with the corresponding first derivative bounds. Dividing the transport image by x^2 gives

 (V.grad h_epsilon-h_epsilon)/x^2
 =V.grad g_epsilon+(2V1/x-1)g_epsilon.

The linear-field terms have C^alpha norm at most C epsilon^(1-alpha). The W terms have norm at most C epsilon^(3-alpha): rescale to the fixed unit disk, use W=O(epsilon^3), W1/x=O(epsilon^2), and the smooth fixed profile of g_epsilon. Thus h_epsilon also tends to zero in the exact T graph.

The canonical kernel scaling gives c[h_epsilon]=epsilon^2 c[H]. Choose a fixed smooth physical-parity q supported away from the origin and from the vertical axis, with c[q]=1 and J(q)=0. Such a function exists because the strain kernel is nonzero on an open set; put a bump there and take its parity projection, then normalize its nonzero integral. Its cofactor and full graph image belong to Z3. Replace h_epsilon by h_epsilon-c[h_epsilon]q. This has c=0, retains J=1, and tends to zero in the transport graph. Bounded C0 proves convergence in the full graph. Therefore J is not closable. Merely strengthening the horizontal cofactor norm to C^alpha for alpha<1 does not recover the cubic derivative trace.

## Exterior inverse with the same actual time change

On sufficiently large radii use the already verified actual quantities of proof 228,

 a=V1/x>ell/2, W=V/a, q=1/a,
 Psi_t the forward W flow, m_t=exp(-integral_0^t q(Psi_s X)ds).

Their estimates, valid on r>=R0/2 and all t>=0, are

 |Psi_t X| comparable to r exp(t), ||D Psi_t||<=C exp(t),
 det D Psi_t comparable to exp(2t), (Psi_t X)_1=exp(t)x,
 m_t comparable to exp(-kt), |D m_t|<=C exp(-kt)r^(k-2).

All constants are independent of a larger chosen R. The exact x-coordinate identity gives, for f=x^2 g_f,

 f(Psi_t X)/x^2=exp(2t)g_f(Psi_t X).

Scaled full Holder comparison of close point pairs, and supremum comparison of distant pairs, yields

 ||exp(2t)g_f(Psi_t .)||ann,cofactor
                             <=C exp(beta t)||f||ann,cofactor. (9)

In detail g_f on the image annulus has size N(r exp(t))^(beta-2) and seminorm N(r exp(t))^(beta-2-alpha); the composition's Lipschitz factor exp(t) cancels the alpha factor, and exp(2t) supplies the remaining two powers. Nearby starting segments may enter r<R but stay in r>=R0/2, where the variational bound holds; the endpoint evaluations of f remain in Omega_R. Distant pairs use values. Thus no boundary extension of f is being assumed.

The scaled first derivative bound on m_t and the smooth multiplier 1/a give convergence and the annular bound for

 Q_R f(X)=-integral_0^infinity m_t(X)(f/a)(Psi_t X)dt,
 ||Q_R f||ann,cofactor<=C||f||ann,cofactor/(k-beta).     (10)

The quotient formula also converges uniformly on compact subsets of the closed exterior, including its vertical axis. It therefore defines the continuous cofactor required in F_R^(3).

For the weighted norm, the same change of variables as proof 228 gives

 ||f(Psi_t .)||L2(Omega_R,w_gamma)
                     <=C exp((gamma/2-1)t)||f||L2(Omega_R,w_gamma).

If gamma<2+2k this proves a bound with denominator k+1-gamma/2. If gamma>=2+2k, use the pointwise bound from(10), |Q_Rf|<=CNr^beta, to obtain

 ||Q_Rf||L2<=C N R^(beta+1-gamma/2)
                    /((k-beta)sqrt(gamma-2beta-2)).     (11)

Its radial exponent is at most beta-k<0 and its square-root denominator is positive. These two regimes cover every gamma>4k with constants independent of large R.

The cocycle relation differentiates(10) along each W orbit and gives V.grad Q_Rf=Q_Rf+f. C1 flow boxes turn this continuous orbit identity into a distributional identity. Conversely a maximal-domain solution obeys the same orbit relation off the vertical axis, and continuity extends it through that axis. Its terminal physical value after multiplication by m_t is bounded by C exp((beta-k)t)r^beta and tends to zero. Thus Q_RT_Rh=h and T_RQ_Rf=f. This proves a bijection on the exact maximal domain, without a smooth-core density assumption or an imposed inner trace.

Finally E_R and P_R are uniformly bounded, and E_R maps the exterior graph into D3 because V.grad eta_R is a bounded scaled C1 multiplier on its annulus. Equation(2), applied with a tail cutoff equal one on Omega_R, shows ||P_RC0E_R||->0. The Neumann series

 (A_R^(3))^(-1)=Q_R(I+P_RC0E_RQ_R)^(-1)

is a genuine two-sided inverse when the displayed perturbation has norm less than one. Expanding the transport of eta_Rh proves(5). No middle-region matching follows from this construction.

## Why the existing turning packets no longer give a bounded test sequence

On a fixed positive-height compact annulus, the cofactor of the packets in proof 234 is phi(x/q)cos(x/epsilon)g_*(y). At a fixed height with g_* nonzero, choose two nearby abscissas inside the region phi=1, separated by pi epsilon, where the cosine is1 and-1. Such points exist for q/epsilon tending to infinity. Their C^alpha quotient is at least c epsilon^(-alpha). The compact zero-strain correction there vanishes because it was supported outside the thin trajectory cone. Therefore the packet norms in Z3 diverge at least at this rate. Their boundedness in Z2 is insufficient for an open-mapping contradiction on Z3. This is a statement about that specific proof, not evidence that the new global operator is onto.

## Dependencies and current scope

Proof 234 supplies the full divided-velocity lemma; its independent audit is pending. Topics228 and its audit clarifications supply the exact exterior geometry, weighted estimates and all canonical conventions. Topics217 and the source reconstruction supply divided background and column expansions. The current proof establishes the norm, mapping, nonclosable jet and exterior statements from these inputs. It does not transfer any local-to-global inverse theorem, assert compactness of patching errors, or give nonlinear estimates. The full global problem on this stronger space remains OPEN. No computation is needed and no new numerical certificate is claimed.
