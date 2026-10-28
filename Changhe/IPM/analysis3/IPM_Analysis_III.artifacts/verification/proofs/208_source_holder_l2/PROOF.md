# A frozen source inverse on bounded Holder functions intersected with L2

## Statement and exact domain

Let A>mu>0 and g>0, put a=g/(A-mu), and assume a mu>1. Fix

 0<alpha<min(1,1/mu).

On R2 set B=diag(A,mu), let M have Fourier multiplier xi^2/(xi^2+eta^2), and define

 X_alpha=C^alpha_b(R2) intersect L2(R2),
 ||f||X=||f||2+||f||infinity+[f]_alpha,
 L0 f=B X.grad f-f-g M f,
 D_alpha={f in X_alpha:B X.grad f belongs to X_alpha distributionally}.

Here [f]_alpha is the global Euclidean Holder seminorm. The value of the multiplier at frequency0 is irrelevant in L2. L0:D_alpha->X_alpha is closed and bijective. Its inverse R0 is bounded X_alpha->X_alpha, with a finite constant depending only on A,mu,g,alpha and the fixed equivalent dyadic norm used in the proof. Its L2 realization satisfies

 ||R0||_(L2->L2)<=1/[1+(A+mu)/2].                     (1)

Unlike proof 26, this statement does not fix or bound the support of the forcing. In particular its X_alpha bound applies to the noncompact image of a localized nonlocal operator. The assumption a mu<A+1 from proof 26's higher-order bounds is not needed here. No numerical value of the X_alpha inverse constant is asserted.

There is also a localized frozen-transport consequence. Let rho be C2 near a source P=(p,0), with rho_x(P)=0 and rho_y(P)=g. In coordinates X=(s,y) centered at P, choose a fixed smooth cutoff chi, equal1 on B_(1/2) and supported in B1. For small delta define

 E_delta h=chi(X/delta){rho_x(P+X) U1[h]
                          +(rho_y(P+X)-g) U2[h]},
 U1hat=xi eta/(xi^2+eta^2), U2=-M.

Then ||E_delta||_(X_alpha->X_alpha)<=C delta^(1-alpha). For sufficiently small delta, L0+E_delta is a closed bijection on the same domain D_alpha. Inside B_(delta/2) its velocity coupling is exactly U[h].grad rho(P+X), and its transport remains the frozen source transport B X.grad. Outside B_delta its coupling is the frozen -gM. This is not an inverse for the actual variable transport or for the global normalized IPM operator.

The exact modal source of proof 15 has 10<A<51/5, 29<g<30 and

 99999997745/10^11<mu<99999997750/10^11<1.

These exact rational bounds imply a mu>1, so every 0<alpha<1 is covered for that source. The background is the joined, scalar-normalized modal trial, not raw X3 and not an exact stationary profile.

## The L2 inverse and the maximal domain

The transport B X.grad has its maximal distributional L2 domain. On every quadrant the unitary logarithmic change

 H(u,v)=exp((u+v)/2)h(plus-or-minus exp(u),plus-or-minus exp(v))

conjugates it to A partial_u+mu partial_v-(A+mu)/2. Cutoffs and convolution in (u,v) give a graph core for this constant directional derivative. The quadrant boundaries have measure zero, and the transport is tangent to them; testing across them or taking axis cutoffs gives the same full-plane maximal domain. M is bounded on L2 with norm at most1 and does not change the domain.

For t>=0 put D_t f(X)=f(exp(Bt)X). Direct Fourier transport gives the semigroup

 S_t=exp(-t)D_t Q_t,
 Q_t(xi,eta)=[(xi^2+eta^2)/(exp(2(A-mu)t)xi^2+eta^2)]^(a/2). (2)

The multiplier Q_t lies between0 and1. Thus

 ||S_t||_(L2->L2)<=exp(-(1+(A+mu)/2)t).                (3)

The ratio in Q_t telescopes under the dilation, proving the semigroup law. Dominated convergence and strong continuity of D_t prove strong continuity on L2. Differentiating its multiplier at0 gives -gM; its time derivative is uniformly bounded by a constant depending on g. Hence its generator on the transport domain is exactly L0. Equivalently, away from frequency0,

 (S_t f)hat(zeta)=exp((a mu-1-A-mu)t)|zeta|^(-a)
                         |exp(-Bt)zeta|^a fhat(exp(-Bt)zeta). (4)

Formula(2), not separate singular multipliers at0, defines this operator.

The integral R0 f=-integral_0^infinity S_t f dt converges in L2. Differentiating on the graph core and then using graph closure gives L0 R0=I and R0 L0=I on the maximal L2 domain; the term S_T tends to0 by(3). This proves(1). In particular there is only one solution in that domain. This construction and these domain arguments are the ones independently checked in proof 26, restated here to identify the realization exactly.

## Annular estimate without a support assumption

Fix a smooth homogeneous annular decomposition Delta_N, N=2^j, j in Z, and an inhomogeneous low output block Delta_low. Annular multipliers such as Delta_N |D|^a and Delta_lambda |D|^(-a) have L1 kernel norms bounded by C N^a and C lambda^(-a), respectively. This follows by rescaling a fixed smooth compact annular symbol and integrating its inverse Fourier transform. These statements involve no neighborhood of frequency0.

For an annular input f_N=Delta_N f, formula(4), with slightly enlarged annular cutoffs, gives

 ||Delta_lambda S_t f_N||infinity
 <=C exp((a mu-1)t)(N/lambda)^a ||f_N||infinity.      (5)

Indeed on this input one may write the right side of(4) as exp((a mu-1)t)|D|^(-a)D_t |D|^a. Dilation preserves the supremum norm; the two localized multiplier kernel bounds then prove(5).

A nonzero contribution requires the input annulus and the dilated output annulus to intersect. Since A>mu, this restricts t, up to fixed additive constants, to

 log(lambda/N)/A<=t<=log(lambda/N)/mu,

and requires N<=C lambda. Intersect this time interval with t>=0. Because a mu-1>0, integration of(5) up to the upper endpoint yields

 ||Delta_lambda R0 Delta_N f||infinity
       <=C (N/lambda)^(1/mu)||Delta_N f||infinity,
       N<=C lambda.                                 (6)

The identity behind the exponent is a-(a mu-1)/mu=1/mu. When lambda/N is bounded above and below, the allowed time is bounded and the same estimate holds after adjusting C. Annular cutoff overlap only changes these constants. No mixed L1 norm or compact-support estimate has entered(5)-(6).

For N>=1, cancellation of the annular kernel gives

 ||Delta_N f||infinity<=C N^(-alpha)[f]_alpha.        (7)

For N<1 the two-dimensional Bernstein bound gives

 ||Delta_N f||infinity<=C N||f||2.                   (8)

To check(8), apply Cauchy-Schwarz to convolution with the Delta_N kernel, whose L2 norm scales as N in dimension2. The low input estimate therefore needs only the stated L2 norm.

For lambda>=2, summing(6) with(7)-(8) gives

 ||Delta_lambda R0 f||infinity
 <=C lambda^(-1/mu){[f]_alpha
        sum_(1<=N<=C lambda) N^(1/mu-alpha)
             +||f||2 sum_(N<1) N^(1+1/mu)}
 <=C lambda^(-alpha)([f]_alpha+||f||2).              (9)

Both sums are dyadic. The first is controlled by its largest term because alpha<1/mu. The second converges because 1+1/mu>0. Thus the low-frequency part contributes at most C lambda^(-1/mu)||f||2, which is bounded by the right side of(9). Partial homogeneous sums converge in L2 to f, and R0 is L2-bounded. The displayed absolute bounds after projection identify their uniform limit with Delta_lambda R0 f. No exchange of an uncontrolled infinite sum and an integral is required.

For the low output block, its L2 convolution kernel and(1) give

 ||Delta_low R0 f||infinity<=C||R0 f||2<=C||f||2.     (10)

Equations(9)-(10) imply the bounded classical C^alpha norm: the high blocks sum uniformly, and their differentiated kernels have L1 norm O(lambda). Split a difference of length d<1 into lambda<=1/d and lambda>1/d; the derivative sum and the supremum sum are each O(d^alpha). For d>=1 use the supremum. Conversely, (7) is the direct Holder-to-block estimate. This proves the claimed X_alpha bound without an unstated support parameter.

## Return to the exact X_alpha graph

The multiplier M is bounded on X_alpha. On every high annulus, an enlarged cutoff makes its convolution kernel have uniformly bounded L1 norm, so the high block bound follows from(7). The low block of M f has supremum at most C||f||2 because the compact low-frequency symbol times the bounded multiplier M has an L2 inverse Fourier kernel. Its L2 norm is at most ||f||2. The block argument just used therefore gives

 ||M f||X<=C_alpha||f||X.                            (11)

The same proof applies to U1 and U2. It follows from(11) that h in X_alpha with L0 h in X_alpha distributionally has B X.grad h in X_alpha, and conversely. Thus the stated domain D_alpha is also the maximal X_alpha domain of L0.

For f in X_alpha, the L2 inverse already constructed has h=R0 f in X_alpha by(9)-(10). The equation gives B X.grad h=f+h+g M h in X_alpha, so h lies in D_alpha. This proves surjectivity. Any homogeneous solution in D_alpha belongs to the L2 maximal domain and is zero by the L2 inverse. Finally the graph is closed: X_alpha convergence implies L2 and local uniform convergence, and applying B X.grad is continuous into distributions. This proves closedness on exactly D_alpha. The argument does not require smooth compact functions to be norm dense in the large Holder space, or strong continuity of the flow in that Holder norm.

## Local variation of the source coupling

Let b1(X)=rho_x(P+X) and b2(X)=rho_y(P+X)-g. They vanish at0 and are C1 near0. For b_(j,delta)=chi(X/delta)b_j(X),

 ||b_(j,delta)||infinity<=C delta,
 ||D b_(j,delta)||infinity<=C,
 [b_(j,delta)]_alpha<=C delta^(1-alpha).             (12)

The last inequality follows by splitting differences at delta. The constant depends on the fixed local C2 norm of rho and on chi. Product differences and the L2 supremum estimate give

 ||b_(j,delta) f||X<=C delta^(1-alpha)||f||X,

including pairs across the cutoff boundary. Combining this with(11) proves ||E_delta||<=C delta^(1-alpha). Since E_delta is bounded on X_alpha, the domain remains D_alpha. If C delta^(1-alpha)||R0||<1, factor

 L0+E_delta=(I+E_delta R0)L0,
 (L0+E_delta)^(-1)=R0(I+E_delta R0)^(-1).

The norm-convergent Neumann series proves the stated localized frozen-transport inverse, with norm at most ||R0||/[1-C delta^(1-alpha)||R0||]. Its actual-coefficient equality concerns only the velocity coupling in the indicated small source disk. The drift has not been changed.

## Why this is not a normalized global source space

The raw physical central strain c is not bounded on X_alpha, even on smooth compact densities with the global case1 parity and J=0. Choose a nonzero smooth nonnegative radial function beta supported in 1<r<2, and set H=x^2 y beta(r). Direct angular integration of the canonical kernel gives

 c[H]=(1/4)integral_1^2 r beta(r)dr>0.

For h_epsilon(X)=epsilon^alpha H(X/epsilon),

 ||h_epsilon||infinity=epsilon^alpha||H||infinity,
 [h_epsilon]_alpha=[H]_alpha,
 ||h_epsilon||2=epsilon^(alpha+1)||H||2,
 c[h_epsilon]=epsilon^(alpha-1)c[H].                 (13)

Every h_epsilon is smooth, compact, even in x and odd in y, and vanishes on a neighborhood of0, so J(h_epsilon)=0. Equation(13) gives a bounded X_alpha sequence with unbounded strain for every alpha<1. Thus the normalized column cannot be added as a bounded rank-one perturbation on this space merely by citing the frozen source theorem. Additional origin control or a separately supplied scalar is needed. The same space is unchanged by translation to the source coordinates, so this limitation is not a coordinate convention.

The source theorem also leaves the actual variable-transport perturbation, source-to-origin matching, far-tail realization, closed cubic normalization and nonlinear estimates open. It proves no actual global inverse or profile existence. Topics15 and26 supply the certified source association and the semigroup conventions; all changes of the function space and every new mapping and domain step are proved above. Independent independent cross-audit is requested.
