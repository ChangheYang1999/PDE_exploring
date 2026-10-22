# Smooth forcing with a singular pure-transport inverse at a source

Status: complete standalone argument written before numerical checks. This audits the frozen pure-transport counterexample. It does not refute an inverse retaining the IPM nonlocal term.

## The source eigenvalue requires only C1 regularity

Suppose rho and V are C1 near P, V(P)=0, and V dot grad rho=rho. Evaluating at P gives rho(P)=0. Write Z=X-P. The C1 expansions are

V(P+Z)=DV(P)Z+o(|Z|), grad rho(P+Z)=grad rho(P)+o(1).

Their product is (DV(P)Z) dot grad rho(P)+o(|Z|). Comparing the linear term with the C1 expansion of rho proves

DV(P)^T grad rho(P)=grad rho(P).  (1)

No second derivative of rho was used. At an x-axis equilibrium with the usual density and velocity parity, DV(P)=diag(A_P,mu_P) and grad rho(P)=(0,g), so g!=0 implies mu_P=1. If div V=2c_l, it follows that A_P=2c_l-1. The hypotheses include an exact equation and a nonzero gradient; they are not conclusions about the numerical trial.

## Construction on the frozen source plane

Fix A>0 and use coordinates (s,y). Define

T=A s partial_s+y partial_y-1.

Choose a nondecreasing C-infinity function chi on R equal to0 for s<=1 and1 for s>=2, with chi'>0 on(1,2). For an explicit construction, integrate the positive bump exp(-1/((s-1)(2-s))) on(1,2) and divide by its strictly positive finite integral. Put

phi(s)=s chi'(s), psi(y)=1-chi(|y|), f(s,y)=y phi(s)psi(y).

The apparent absolute value is harmless because psi is constant near0. The forcing f is compactly supported and C-infinity, odd in y, and supported in1<=s<=2. In particular

integral_1^2 phi(z)/z dz=1.  (2)

Define the forward-boundary solution by

h(s,y)=-integral_0^infinity exp(-t) f(exp(A t)s,exp(t)y)dt.  (3)

For s<=0 the integrand is zero. For s>0 its possible t support is a bounded interval, since phi is supported in[1,2]. For s>=2 it is zero. Thus (3) is well defined at every point and smooth on s>0. Along a characteristic, differentiation of the finite integral shows Th=f. Equivalently,

exp(-T)h(exp(A T)s,exp(T)y)-h(s,y)
 =integral_0^T exp(-t)f(exp(A t)s,exp(t)y)dt.  (4)

For every initial point, the left first term is eventually zero, because the forward characteristic leaves the forcing region and the support of h. Formula(3) is therefore the unique solution along each characteristic satisfying this forward-boundary condition. No smoothness at the equilibrium is assumed in that uniqueness statement.

For0<s<1, substitution z=exp(A t)s gives the exact expression

h(s,y)=-(y/A)Q(y s^(-1/A)),
Q(u)=integral_1^2 chi'(z)psi(u z^(1/A))dz.  (5)

The function Q is smooth and even, 0<=Q<=1, equals1 for |u|<=a:=2^(-1/A), and is zero for|u|>=2. In particular Q is not constant. The bound |h|<=|y|/A holds everywhere (for s>=1 the integral only shortens). It proves continuity at the origin. For fixed nonzero y and sufficiently small positive s, h(s,y)=0, so h is also continuous across every other point of s=0. It is compactly supported in0<=s<=2, |y|<=2, and smooth except possibly at(0,0).

For each fixed0<s<1, (5) is exactly -y/A in a neighborhood of y=0. Hence

partial_y h(s,0)=-1/A for0<s<1,
partial_y h(s,0)=0 for s<=0.  (6)

The derivative at s=0 in(6) is an ordinary partial derivative, because h(0,y)=0. A C1 representative is impossible. The continuous representative just constructed is unique among representatives equal almost everywhere; two continuous functions agreeing almost everywhere agree everywhere. Thus this failure cannot be repaired by changing h on a null set.

A local H^sigma function in two dimensions has a C1 representative for sigma>2. Here is the Fourier proof of the needed implication. After multiplication by a compact smooth localization, Cauchy-Schwarz gives

integral |xi| |h_hat(xi)| dxi
 <=||h||_{H^sigma}[integral |xi|^2(1+|xi|^2)^(-sigma)dxi]^(1/2)<infinity

exactly when sigma>2 at infinity; the zero-frequency integral is finite. Its Fourier first derivatives are absolutely integrable, and dominated convergence makes their inverse transforms continuous. The same argument controls the function. Formula(6) therefore proves h is not H^sigma locally near the source for any sigma>2, including3.06.

## A stronger obstruction in the source range A>=3

In fact the example is not even H1 locally when A>=3. Differentiating(5) for s>0, with u=y s^(-1/A), gives

partial_s h=s^(1/A-1)u^2 Q'(u)/A^2,
partial_y h=-(Q(u)+u Q'(u))/A.  (7)

The change y=s^(1/A)u implies

integral_{epsilon<s<delta, a s^(1/A)<y<2s^(1/A)} |partial_s h|^2 dsdy
 =A^(-4)[integral_epsilon^delta s^(3/A-2)ds]
          [integral_a^2 u^4|Q'(u)|^2du].  (8)

The angular factor is strictly positive. There is a useful lower bound independent of the chosen smooth step: since Q(a)=1 and Q(2)=0, Cauchy-Schwarz gives

integral_a^2 u^4|Q'(u)|^2du
 >=[integral_a^2 u^(-4)du]^(-1)
 =3/[2^(3/A)-1/8].  (9)

For A>=3 the radial integral in(8) diverges as epsilon decreases to0, including logarithmic divergence at A=3. Taking delta small enough places the entire integration region inside any chosen neighborhood of0. If h were locally H1, its weak derivative would agree with the classical derivative on the open set s>0, contradicting(8). Consequently no local H1 membership is possible for A>=3.

The equation still holds distributionally. To justify this without assuming H1, the classical derivative in(7) is locally L1 for every A>0: integration in y gives the radial exponent2/A-1>-1. The y derivative is bounded on the source chart. In integration by parts across s=epsilon, the boundary integral of h against a fixed smooth test function is bounded by a constant times epsilon^(2/A), because |h|<=C epsilon^(1/A) and its y support there has length O(epsilon^(1/A)). This tends to0. Hence the distributional derivative has no delta term on s=0, and Th=f across that line as well. This proves (3) is a compact continuous distributional solution with smooth forcing, rather than merely a formula on a punctured domain.

For the illustrative exact A=2/k-1, k=1615536043799051/9007199254740992, A>3. The jump in(6), exponent3/A-2, and the lower bound (8)-(9) can be enclosed without numerically integrating the smooth step. At delta=1/2 and epsilon<delta the latter lower bound is

[3/(A^4(2^(3/A)-1/8))]
 [epsilon^(3/A-1)-(1/2)^(3/A-1)]/(1-3/A).  (10)

This is a lower bound for an integral over the displayed curved region. It is not a measured derivative norm of the IPM numerical profile.

## A full-plane parity extension, with its limits stated

The counterexample can be placed at two reflected sources without a parity defect. Choose L>4, c_l=(A+1)/2, a smooth cutoff chi_+(x) equal to1 on[L-1/2,L+5/2] and supported in(L-1,L+3), and a smooth even cutoff eta(y) equal to1 for|y|<=5/2 and supported in|y|<3. Define

P_+(x,y)=chi_+(x)eta(y)[A L-(A-c_l)x]y,
Psi(x,y)=P_+(x,y)-P_+(-x,y),
U=(-Psi_y,Psi_x), V=c_l(x,y)+U.

The stream function Psi is odd in x and y. Thus V1 is odd in x and even in y, while V2 is even in x and odd in y. The perturbation U is smooth and compactly supported, div V=2c_l, and U=o(r). On the entire support of h(x-L,y), including a neighborhood of its boundary, V=(A(x-L),y); at the reflected support the corresponding field is(A(x+L),y). These assertions follow by direct differentiation of the displayed linear-times-y polynomial and the identity A=2c_l-1.

Set H(x,y)=h(x-L,y)+h(-x-L,y) and F(x,y)=f(x-L,y)+f(-x-L,y). The supports are disjoint. H is compact and continuous, even in x and odd in y, and F is smooth with these parities. Direct change of variables in the distributional equation gives

(V dot grad-1)H=F.

It has the same local lack of H1 at both sources if A>=3, and lacks local H^sigma for sigma>2 for every A>0. The forcing and solution vanish near the origin. This extension supplies the relevant parity and sublinear perturbation of dilation. It does not construct an exact IPM profile for which this V is the transport field, does not establish every global flow hypothesis, and does not remove the nonlocal term from the full linearization. Its conclusion is confined to the pure-transport regularity argument.

## Exact series for the illustrative constant checks

For0<z<1, integration of the geometric series for1/(1-z^2) gives

log((1+z)/(1-z))=2 sum_{n=0}^infinity z^(2n+1)/(2n+1).

After retaining n=0,...,N-1 the positive tail is at most2 z^(2N+1)/[(2N+1)(1-z^2)]. Use z=1/3 for log2 and z=2/3 for log5, and log10=log2+log5. For x>=0, the tail of sum_{n=0}^N x^n/n! is at most x^(N+1)/[(N+1)!(1-x/(N+2))] when x<N+2, since all later term ratios are bounded by x/(N+2). Monotonicity extends these bounds to a positive interval input x by using its upper endpoint in the tail. These positive series give an interval method independent of a library power call for (9)-(10). Values for epsilon=10^(-m), m=1,2,3, use epsilon^(3/A-1)=exp(m(1-3/A)log10) and (1/2)^(3/A-1)=exp((1-3/A)log2).

## Dependencies and numerical verification plan

All characteristic, distributional and local regularity arguments needed here are supplied above. The source eigenvalue identity(1) assumes only C1 regularity and an exact equation. No canonical inverse or profile existence theorem is used in the counterexample.

Symbolic differentiation will check(5)-(8), the homogeneous equation where the forcing vanishes, the global cutoff-free source patch and its divergence. Arb512 power functions will be compared with mpmath.iv using a rational positive atanh series for log2 and a positive exponential series with a proved tail. Exact rational inequalities will verify A>3 and the divergence exponent. A fresh higher-precision audit will check (10) at epsilon=1/10,1/100,1/1000. These are illustrative constants for the explicit smooth-forcing construction, not PDE error enclosures. The full nonlocal inverse and the IPM endpoint remain open.
