# Smooth local equations at an interior zero arc

## Statement and notation

At beta=2, consider smooth fields on R^2 satisfying

    div W=4, Omega=-(partial_x W_2-partial_y W_1),
    W.grad Theta=0, W.grad Omega+Omega=partial_x Theta.

These four local equations admit arbitrary smooth zero-curve graphs and, separately, arbitrary smooth temperature on a straight zero curve. They do not force analytic or Gevrey regularity of either datum at all interior zero-arc points. This says neither that arbitrary pairs of curve and temperature data are solvable nor that any example below is an admissible global B2 profile.

A qualification in the superseded I1-I5 draft was false: the first family can satisfy the B2 parity and normalized center data. The universal obstruction for the displayed families is the sublinear far-field velocity condition, not necessarily the center data. Also arbitrary h can produce superlinear velocity; the accurate universal statement is failure of sublinearity, not exact linear growth.

## First exact family

For any smooth real h and constant L define

    W=(0,4y-h(x)), Theta=L+h(x), Omega=h'(x).

Then div W=4 and -curl W=h'. Since Theta and Omega depend only on x while W_1=0, both transport derivatives vanish. The last equation is exactly h'=partial_x Theta. The zero set is the smooth graph y=h(x)/4. The graph is a regular embedded curve regardless of zeros of h', because its x-coordinate derivative is1. For a nonanalytic smooth h it is not an analytic embedded curve: analytic implicit inversion of the nonvertical graph projection would otherwise make h analytic.

Set U=W-2X=(-2x,2y-h(x)) and

    Psi=2xy-H(x), H'(x)=h(x).

Then U=(-Psi_y,Psi_x) and -Delta Psi=h'=Omega. Along x=0 and |y| tending to infinity, U_2=2y-h(0), so |U|/|(0,y)| tends to2. Thus the velocity is never uniformly sublinear. No canonical admissible B2 inverse or far-field condition is established by this local Poisson solution.

For the explicit choice h(x)=x^2, L=0, H=x^3/3,

    Theta=x^2, Omega=2x, Psi=2xy-x^3/3,
    U=(-2x,2y-x^2), W=(0,4y-x^2).

Theta is even and Omega,Psi are odd in x. U(0)=0, Theta(0)=0, grad Theta(0)=0, a0=1, b0=2=4a0/beta and c=Psi_xy(0)=2=1+beta/2. The defining stationary equations hold identically. Hence the assertion that the center data fail for all these examples is refuted. This example has nondecaying vorticity and temperature gradients and superlinear velocity along y=0, so it is not a B2 profile. The failure of admissibility is explicit.

## Second exact family and absence of finite Gevrey bounds

For arbitrary smooth t, let W=(4x,0), Omega=0, Theta=t(y). Direct differentiation gives all four equations, with zero set x=0. Here U=(2x,-2y) is linear, and Theta_xx(0)=0 excludes the required a0 nonzero center normalization.

Define

    F(y)=sum_(j>=1) exp(-j^2) cos(2^j y),
    t(y)=y+F(y)-F(0).

For each integer k>=0 the kth differentiated summand is bounded uniformly by exp(-j^2+k j log2). Completing the square or comparing j beyond2k log2 with exp(-j^2/2) shows that this series of bounds is summable. Repeated uniform differentiation proves F is C-infinity and permits evaluation term by term. F'(0)=0, so t'(0)=1.

For every integer m>=1,

    |F^(2m)(0)|=sum_(j>=1) exp(-j^2+2m j log2).

All summands have the same derivative sign before taking absolute values. Choose a positive integer j nearest m log2. Such a positive nearest integer exists for m>=1 because log2>1/2. Then |j-m log2|<=1/2 and one term gives

    |F^(2m)(0)|>=exp(m^2(log2)^2-1/4).

For any finite sigma>=1 and constants C,A>0, log(C A^(2m)((2m)!)^sigma) is O(m log m), while the lower-bound logarithm is quadratic in m. It eventually exceeds this expression. Since t^(2m)(0)=F^(2m)(0) for m>=1, t belongs to no finite Gevrey class on a neighborhood of0. This is a pointwise obstruction to the usual uniform neighborhood derivative bounds. It applies to the temperature trace along the analytic line x=0, even though its first tangential derivative is nonzero at0.

One can also take h=x+F(x)-F(0) in the first family. Its graph is smooth and nonanalytic at0, with nonzero tangent temperature derivative. This choice is a local-equation illustration and is not asserted to satisfy global B2 parity or center data.

## Scope of the lead's proposed entry

Claims I1 through I4 in work/enter_int1/text.md are confirmed by the arguments above. The source consultation's answer explicitly reports neither an outgoing-endpoint construction nor a general obstruction, so I5 correctly describes that outcome. The proposed parenthetical about all examples' linear growth and failing center data needs repair. A sufficient replacement is: "These solve the local equations but are not B2 profiles: their velocities fail the sublinear far-field condition. The second family also fails the nonzero x^2 temperature-jet condition." The first family need not be excluded on center grounds.

The examples concern interior arc points. They provide no compact equilibrium component, outgoing endpoint, full-plane canonical profile, or B2 YES/NO endpoint. No regularity assertion for a prescribed nonvertical analytic arc and arbitrary trace follows from these separate families. Dependencies: differentiation, uniform convergence of derivative series, the analytic implicit function theorem for the graph observation, and the elementary factorial bound log((2m)!)<=2m log(2m). No numerical computation is needed for the proof.

## Updated J1-J6 draft: center-preserving non-Gevrey graph

The lead superseded I1-I5 by work/enter_int1/text_v2.md at18:48Z. Its revised example is also valid, with a0 nonzero as in the prompt. Set C=0 and

    h(x)=a0 x^2+F(x)-F(0)-F''(0)x^2/2.

The previously proved uniform derivative convergence shows F is smooth and even. Taylor's theorem through order3, with bounded fourth derivative near0, gives h=a0 x^2+O(x^4) and h'=2a0 x+O(x^3). Thus h(0)=h'(0)=0, h''(0)=2a0. The graph family has W(0)=0, DW(0)=diag(0,4), all required x-parities, Theta(0,y)=0, and the center jet just described. Integrating even h from0 gives odd H and hence odd Psi=2xy-H. Its center strain is2. These are local center and Poisson identities, not proof that the forbidden linear strain is produced by the admissible canonical inverse.

For m>=2, h^(2m)(0)=F^(2m)(0), so the same quadratic exponential lower bound excludes every finite Gevrey order. To justify the stronger assertion about an unparametrized regular embedded graph, we supply the needed closure argument below. Therefore J1-J6 are correct as locally scoped statements. In J6 a constant observer velocity changes no far-field conclusion. For the arbitrary graph family W(0) need not vanish; it does vanish in the center-preserving specialization. The v2 text correctly separates these cases.

## Gevrey graph lemma with its closure argument

A Gevrey-sigma function on an interval, sigma>=1, has bounds |f^(n)|<=C A^n(n!)^sigma on each fixed smaller compact interval. Write s=sigma-1>=0. The divided Taylor coefficients obey |a_n|<=C A^n(n!)^s.

Composition preserves such bounds. The coefficient of order n>=1 of f(g(t)) is the sum over k and positive integers n1+...+nk=n of a_k product b_(ni). The factorial inequality k! product(ni!)<=n! follows by successively minimizing the multinomial coefficient at fixed n,k (move units from smaller positive parts into a largest part), leaving parts (n-k+1,1,...,1), whose multinomial coefficient n!/(n-k+1)! is at least k!. Hence each product of Gevrey factors is bounded by (n!)^s. The remaining geometric constants sum over binomial(n-1,k-1) compositions and are bounded by a new exponential B^n. The same estimate holds uniformly at each point of a compact interval by using uniform derivative bounds and a compact image interval. Multiplying by n! proves composition closure.

For inverse closure suppose f' is bounded away from0 on a small interval. At an arbitrary base point translate f to have value0 and write f(t)=a1 t(1+q(t)), q(t)=sum_(j>=1) q_j t^j. Uniformly, |a1|>=c>0 and |q_j|<=D A^j((j+1)!)^s for suitable D,A. The formal Lagrange identity gives the inverse divided coefficient

    b_n=(1/n) a1^(-n) [t^(n-1)](1+q(t))^(-n).

This is an identity for each finite derivative jet, so no analyticity of f is assumed. Expanding in powers of q, every product has positive indices j1+...+jk=n-1. The inequality product((ji+1)!)<=n! follows by repeatedly using (a+1)!(b+1)!<=(a+b+1)! for a,b>=1. Thus a common factor (n!)^s bounds the factorial contribution. The remaining absolute sum is bounded by the coefficient of order n-1 of (1-Q(t))^(-n), where Q(t)=D A t/(1-A t) has nonnegative coefficients. Choose a fixed r>0 with Ar<1 and Q(r)<=1/2. Positivity gives that coefficient at most r^(-(n-1))2^n. Together with c^(-n)/n this is an exponential bound times (n!)^s, uniformly in the base point. The usual smooth inverse exists since f' is nonzero; its jets are the formal inverse jets, so this proves its Gevrey bound. The factorial inequalities used here also include the k=1 and n=1 cases directly.

Now suppose gamma(t)=(xi(t),eta(t)) is a regular Gevrey-sigma parametrization of the graph y=h(x)/4 near0. Its tangent is nonvertical (indeed horizontal in the center-preserving example), so xi'(0) is nonzero. By inverse and composition closure, h(x)=4 eta(xi^(-1)(x)) would be Gevrey-sigma. This contradicts the already proved derivative lower bound. Thus the graph admits no regular parametrization of any finite Gevrey order. Degenerate parametrizations with zero tangent are not covered and are not the meaning of regular embedded Gevrey graph.
