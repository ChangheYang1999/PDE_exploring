# Directional Holder control of the localized IPM coupling

## Statement

Fix 0<alpha<1 and 1<=p<2. Let E_p consist of bounded continuous functions h on R^2, even in x and odd in y, with finite norm

 ||h||_(E_p)=||h||_infinity+[h]_x+[h]_(y,p),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,p)=sup |h(x,y)-h(x,y')|/(|x|^p |y-y'|^alpha).

For x=0 the last condition means h(0,y)=0. Let U=(-R_1 R_2,R_1^2) be the canonical velocity. For bounded data its far kernel is subtracted at X=0. Thus U(0)=0 and its distributional Fourier symbols away from frequency0 are

 m_1(xi,eta)=xi eta/(xi^2+eta^2),
 m_2(xi,eta)=-xi^2/(xi^2+eta^2).

Let rho be C4 on a fixed disk B_(delta0), even in x, odd in y, with rho(0,y)=0 and rho=x^2 y+O(r^4) at0. Fix a smooth reflection-invariant cutoff chi, supported in B1 and equal1 on B_(1/2), and set chi_delta(X)=chi(X/delta). For 0<delta<=min(delta0/4,1/4), define

 B_delta h=chi_delta U[h].grad rho,

extended by0 to the whole plane. There is a finite constant C=C(alpha,p,rho,chi,delta0), independent of delta and h, such that

 ||B_delta h||_(E_p)<=C delta^(2-p) ||h||_(E_p).          (1)

In fact the weighted y seminorm of B_delta h with weight |x|^2 is at most C||h||_(E_p). No derivative of h is in the input norm. The same bounded mapping into E_2 holds at p=2, but the small factor in(1) is then absent.

For A>0 and D=2A+1, put T0=-Ax partial_x+Dy partial_y-1, on D(T0)={h in E_p:T0h in E_p distributionally}. If

 kappa_p=1+pA-Dalpha>0,
 C delta^(2-p) max(1,1/kappa_p)<1,                       (2)

then T0+B_delta:D(T0)->E_p is bijective with bounded inverse. For every fixed alpha<1, some p in[1,2) satisfies kappa_p>0, and then(2) holds for sufficiently small delta.

This concerns the frozen transport with the stated localized full-plane velocity coupling. It does not include the strain column, replace T0 by the actual transport, prescribe a disk boundary realization, control the cubic normalization, or prove a nonlinear inverse theorem. Constants here are qualitative finite constants with the displayed dependencies, not numerically certified constants.

## The directional velocity estimate

The estimate behind(1) is

 sup_(|x|<=1) ||U_1[h](x,.)/x||_(C^alpha([-1,1]))
       +sup_(|x|<=1) ||U_2[h](x,.)||_(C^alpha([-1,1]))
 <=C ||h||_(E_p),                                      (3)

for every 1<=p<=2. The quotient at x=0 has a continuous extension. The first term is a Holder norm in y, not a bound on partial_x U_1 throughout the disk.

Choose fixed even one-dimensional cutoffs chi_x,chi_y, equal1 on[-2,2] and supported in[-4,4]. Put g=chi_x chi_y h. Oddness in y gives |h(x,y)|<=[h]_(y,p)|x|^p |y|^alpha. It follows, by the product difference formula on the fixed support and by treating pairs farther than1 separately, that

 ||g(x,.)||_infinity+[g(x,.)]_alpha<=C M |x|^p,
 ||g||_(C^alpha(R^2))<=C M,  M=||h||_(E_p),              (4)

and g vanishes for |x|>4. It retains both reflections. The velocity of h-g on B1 has bounded derivatives through order2, bounded by C||h||_infinity: every differentiated far kernel is absolutely integrable, and the input vanishes on[-2,2]^2. Its first component is odd in x and its value at0 is zero. Taylor's integral formula in x therefore gives the part of(3) for this far velocity. It suffices to prove(3) for compact g satisfying(4).

Use a smooth even frequency cutoff eta_0, equal1 on[-1,1] and zero outside[-2,2]. In the y variable set

 Delta_0=eta_0(D_y),
 Delta_j=eta_0(2^(-j)D_y)-eta_0(2^(1-j)D_y), j>=1.

The kernel of Delta_j has integral0 for j>=1. Taking a difference of g under its convolution gives, with lambda=2^j,

 ||g_j(x,.)||_infinity<=C M |x|^p lambda^(-alpha),
 g_j=Delta_j g.                                        (5)

The low block obeys the same bound without lambda^(-alpha). Each block has the original compact x support and is even in x.

We use the elementary one-dimensional characterization of C^alpha by these blocks. Its forward estimate is the cancellation argument just used. For the converse, bounded blocks with ||f_j||_infinity<=L 2^(-alpha j), and a bounded low block, sum uniformly. A slightly larger frequency cutoff gives ||partial_y f_j||_infinity<=C 2^j ||f_j||_infinity by convolution with its differentiated kernel. To estimate a difference of length d<1, sum the derivative bound over 2^j<=1/d and twice the supremum bound over 2^j>1/d. The two geometric sums are at most C_alpha L d^alpha. For d>=1 use the supremum norm. This proves the characterization used below, including its uniformity in x.

Take the Fourier transform only in y, using exp(-iy eta). For eta!=0 the inverse of -partial_x^2+eta^2 has kernel exp(-|eta||x|)/(2|eta|). Therefore

 U_1=-i eta partial_x(-partial_x^2+eta^2)^(-1),
 U_2=-I+eta^2(-partial_x^2+eta^2)^(-1).                 (6)

In particular U_1 has x convolution kernel i eta sgn(x) exp(-|eta||x|)/2. Its x derivative is the sum of i eta times the identity and convolution with -i eta |eta| exp(-|eta||x|)/2. These formulas are distributional and apply to the band-limited blocks.

For j>=1, insert a slightly larger smooth y-frequency cutoff, equal1 on the support of Delta_j and supported where c lambda<=|eta|<=C lambda. Fourier inversion in eta and repeated integration by parts show that the y-integrated absolute kernel of U_1 on this band is bounded by

 C lambda exp(-c lambda |z|),                          (7)

where z is the x displacement. The convolution part of partial_x U_1 has the corresponding bound C lambda^2 exp(-c lambda |z|); its identity part has a y kernel of L1 norm at most C lambda. The convolution part of U_2 has bound(7), in addition to its identity part. To justify the bounds uniformly, set eta=lambda omega. Derivatives in omega of exp(-|omega|lambda|z|) introduce powers of lambda|z|; these are absorbed by a smaller positive exponential rate. Two integrations in omega give an integrable factor(1+lambda|y|)^(-2), and its y integral removes one factor lambda. All cutoff constants are fixed.

For 1<=p<=2,

 integral lambda exp(-c lambda|x-x'|)|x'|^p dx'
 <=C_p(|x|^p+lambda^(-p)).                              (8)

This follows from |x'|^p<=2^(p-1)(|x|^p+|x'-x|^p) and the elementary exponential moments. Equations(5)-(8) give

 ||U_1[g_j](x,.)||_infinity
       <=C M lambda^(-alpha)(|x|^p+lambda^(-p)),
 ||partial_x U_1[g_j](x,.)||_infinity
       <=C M lambda^(1-alpha)(|x|^p+lambda^(-p)).       (9)

The second formula is a continuous derivative in x. This follows either directly from(6), since g_j is continuous in x, or by the integral identity for the locally integrable derivative kernel. Oddness gives U_1[g_j](0,y)=0.

If lambda|x|<=1, integrate the second estimate in(9) from0 to x. If lambda|x|>=1, use the first estimate. For 0<|x|<=1 this gives

 lambda^alpha ||U_1[g_j](x,.)/x||_infinity
 <=C M times
     lambda^(1-p), if lambda|x|<=1,
     |x|^(p-1),    if lambda|x|>=1.
 <=C M.                                               (10)

The series of these quotient blocks converges uniformly because alpha>0. Every block has a continuous limit as x tends to0, and(10) provides a summable majorant. Thus the quotient extends continuously there. The block characterization proves its uniform C^alpha_y bound.

For U_2, compactness of the x support and(5) give the simpler bound ||g_j||_infinity<=C M lambda^(-alpha). The L1 kernel bounds in(7), together with the identity term in(6), imply ||U_2[g_j]||_infinity<=C M lambda^(-alpha). This gives its high-block C^alpha_y bound.

For completeness, the low blocks require no gap from eta=0. On |x|<=1 the x convolution variable meets |x'|<=4, so |x-x'|<=5. The low-cutoff multipliers eta exp(-|eta||z|), eta|eta| exp(-|eta||z|), and |eta| exp(-|eta||z|), with |z|<=5, have uniformly bounded L2 norms and first weak derivative L2 norms as functions of eta. Their inverse Fourier kernels have uniformly bounded L1 norms by Cauchy-Schwarz with(1+y^2)^(-1) and Plancherel. The identity part of partial_x U_1 has a smooth low-frequency differentiated kernel. Formula(6) therefore bounds partial_x U_1[g_0] and U_2[g_0] uniformly on |x|<=1. Oddness and integration in x bound U_1[g_0]/x. A larger low-frequency cutoff and its differentiated kernel then bound their y derivatives. The low blocks have the required C^alpha_y norms. This completes(3).

The ordinary local C^alpha norm of U[h] is also at most C_alpha M. For compact g this follows directly from its mean-zero order-zero kernel: split a difference of length d at radius2d, use the Holder difference of g in the near region, and the first derivative of the kernel in the far region. The radial integrals are d^alpha/alpha and d^alpha/(1-alpha). The separated far velocity was already controlled. Hence, using U(0)=0,

 ||U[h]||_(C^alpha(B1))<=C M,
 sup_(B_delta)|U[h]|<=C delta^alpha M.                (11)

## The coupling bound

Taylor division and the C4 hypotheses give

 rho_x=x a_1, rho_y=x^2 a_2,
 ||a_1||_(infinity,B_delta)<=C delta,
 ||D a_1||_(infinity,B_delta)+||a_2||_(infinity,B_delta)
                    +||D a_2||_(infinity,B_delta)<=C. (12)

For example a_1=integral_0^1 rho_xx(sx,y)ds and a_2=integral_0^1(1-s)rho_xxy(sx,y)ds; oddness in y makes a_1(0,0)=0. The constants in(12) depend only on the fixed local C4 norm.

Set V_1=U_1/x, using the extension in(3). Then

 B_delta h=x^2 chi_delta(a_1 V_1+a_2 U_2).             (13)

For the y Holder seminorm of the first coefficient in parentheses, (3),(12) and the cutoff give

 [chi_delta a_1 V_1]_(C^alpha_y)<=C delta^(1-alpha) M.

For the second coefficient, [chi_delta a_2]_(C^alpha_y)<=C delta^(-alpha), while (11) bounds U_2 by C delta^alpha M on the cutoff support. Its product difference, together with(3), gives

 [chi_delta a_2 U_2]_(C^alpha_y)<=C M.

These are global y estimates after extension by0. Pairs across the support boundary follow from the same product differences on a fixed larger neighborhood; pairs separated from that neighborhood use the supported supremum bound. Consequently

 [B_delta h]_(y,2)<=C M,
 [B_delta h]_(y,p)<=C delta^(2-p) M.                   (14)

The second implication uses the x support |x|<=delta; when |x|>delta the whole y slice vanishes.

For the x seminorm, the product chi_delta grad rho has supremum at most C delta^2 and ordinary alpha seminorm at most C delta^(2-alpha). Combining these with(11) proves [B_delta h]_x<=C delta^2 M. The supremum is at most C delta^(2+alpha) M. These bounds and(14) prove(1), also proving the stated bounded E_2 endpoint mapping.

## Frozen inversion and the exponent range

Proof 25 proves on the stated maximal domain that kappa_p>0 implies

 ||T0^(-1)||_(E_p->E_p)<=max(1,1/kappa_p),
 T0^(-1)f=-integral_0^infinity exp(-s) f(exp(-As)x,exp(Ds)y)ds.

The missing x-difference factor in this maximum is1/(1+Aalpha)<=1. For the sum norm used here the displayed maximum therefore applies exactly. B_delta is bounded on E_p by(1). Under(2), invert I+B_delta T0^(-1) by its norm-convergent Neumann series and set

 (T0+B_delta)^(-1)=T0^(-1)(I+B_delta T0^(-1))^(-1).

This gives both surjectivity into D(T0) and injectivity there. The graph domain is unchanged by bounded perturbation. For alpha<1,

 (Dalpha-1)/A < (D-1)/A=2.

Choosing p in[1,2) strictly larger than the left side yields kappa_p>0. Since2-p>0, a sufficiently small delta then satisfies(2). Thus the previous0.5227 limitation of the p=1 estimate is not a barrier for this frozen localized coupling.

## A direct counterexample to derivative necessity

There are even compact inputs in every E_p for which partial_x U_1 is unbounded but B_delta h belongs to every E_p. Choose a point Q in the first quadrant inside B_(delta/2), with a small ball about it disjoint from both axes and its three reflected copies. Let phi_Q be a smooth cutoff in that ball, equal1 near Q, and put

 P_0=phi_Q |(x-Q_x)+(y-Q_y)|^(2+alpha),
 P(x,y)=P_0(x,y)+P_0(-x,y)-P_0(x,-y)-P_0(-x,-y),
 h=-Delta P.

Then P is compact C^(2,alpha), h is compact C^alpha with the required parity, and h vanishes near both axes. Thus h belongs to every E_p. The compact stream psi=partial_x P solves -Delta psi=partial_x h, so its canonical velocity is exactly

 U[h]=(-P_xy,P_xx).

Near Q, U_1=-(2+alpha)(1+alpha)|s|^alpha, s=(x-Q_x)+(y-Q_y). Its x derivative is unbounded as s tends to0. The velocity is compact C^alpha and vanishes near the axes, so chi_delta U[h].grad rho remains in every E_p. No harmonic velocity or approximate kernel formula is used in this example.

## Dependencies and status

The proof uses the canonical velocity identities from proof 01, the elementary frozen resolvent from proof 25, and the local C4 factorization already checked for the exact modal trial in proof 33. All additional kernel estimates are proved above. There is no numerical claim. The full actual-transport, strain-bordering and nonlinear questions remain open where previously open. An independent cross-audit of(3), especially its low-frequency block and the cutoff product, is requested before the theory author integrates the improved exponent range.
