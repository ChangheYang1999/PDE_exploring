# Monotone box costs and a direct transport inverse

2026-10-20. Independent argument written before the checks. This verifies conditional statements in the lead's revision2 section10, not the actual trial inequalities. All numerical applications below are conditional until their interval audit passes.

## Setting and statements

Let Q={(x,y):x>0,y>0}. Let V be a C1 vector field on R2 with a complete C1 flow phi_t, preserving Q, and with div V=2c_l for a real constant c_l. Linear growth |V(X)|<=C(1+|X|) suffices for completeness. Parities V1 odd in x and even in y, V2 even in x and odd in y suffice for quadrant invariance by uniqueness. Suppose V2>=0 on Q, so y(phi_t X) is nondecreasing.

Let w0 be positive C1 on Q. In particular w0 and1/w0 are bounded on every compact subset of Q. Set

T0=-(1+c_l)-(1/2)V dot grad log w0.

This T0 is continuous on Q. The same kappa is used in the box bounds, the complement bound and the inverse norm.

For finitely many closed boxes B_i=[l_i,u_i]x[0,h_i], with0<l_i<u_i and h_i>0, assume either V1<=-v_i<0 on B_i cap Q, or V1>=v_i x>0 there. Let t_i=(u_i-l_i)/v_i in the first case and t_i=log(u_i/l_i)/v_i in the second. For kappa>0 suppose

(T0+kappa)^+<=s_i on B_i cap Q, s_i>=0,
T0+kappa<=0 on Q outside the union of the boxes.

Then each whole orbit visits each box in an interval of length at most t_i, and

sup_X integral_(-infinity)^infinity (T0+kappa)^+(phi_t X) dt <= K:=sum_i s_i t_i.

In particular the orbit-segment cost C_kappa, with factor2 as in topic52, is at most2K. The maximal distributional operator

B=V dot grad-1,
D(B)={h in L2(Q,w0 dX): V dot grad h in L2(Q,w0 dX) distributionally on Q}

is bijective onto L2(Q,w0 dX), and its inverse is

R_-f=-integral_0^infinity exp(-t)f(phi_t X)dt,
||R_-|| <= exp(K)/kappa.

This transport conclusion requires no source, saddle, equilibrium enumeration, strict positive lower bound V2/y, or outward-radius hypothesis, beyond the complete quadrant-preserving flow already assumed. Those additional hypotheses are useful for separate geometric assertions but are not used in this bound. The boxes and their complements must cover all of Q for the stated margin inequalities, including arbitrarily close to its axes and at infinity.

## One interval of residence and its length

Fix an orbit and two times a<b in its visiting set I for one box B=[l,u]x[0,h]. By monotonicity,0<y(t)<=h throughout[a,b]. Suppose there is a time outside B between them. A connected component(alpha,beta) of the open complement of I in[a,b] has endpoints in I. Throughout this component either x<l or x>u, by continuity. Its endpoints therefore have the same x coordinate, l or u respectively.

For V1<0 on B, a component with x<l would approach x(beta)=l from below. Since x'(beta)<0, differentiability instead gives x(beta-epsilon)>l for sufficiently small positive epsilon, a contradiction. A component with x>u would leave x(alpha)=u toward larger x, contradicting x'(alpha)<0. For V1>0 the other endpoints give the same contradictions. Thus[a,b] is contained in I. It follows that I is an interval, possibly empty or a singleton. This uses the velocity sign only at the boundary points with y>0, so no extension of the inequalities to y=0 is needed for open-quadrant orbits.

For the negative case integrate x'<=-v to obtain v(b-a)<=x(a)-x(b)<=u-l. For the positive case integrate(log x)'>=v to obtain v(b-a)<=log(x(b)/x(a))<=log(u/l). Taking the supremum over a,b in I gives the full length bound, including if one initially allows unbounded I.

The same residence theorem holds for boxes[l,u]x[h_minus,h_plus] with0<=h_minus<h_plus, since between two visits the monotone y coordinate stays between the two endpoint y values. This permits subdivisions of the positive-margin region into smaller rectangles.

A sharper version is available without new flow arguments. If V1<=-v(x)<0 on B and (T0+kappa)^+<=s(x) there, with continuous v>0 and s>=0 on[l,u], the strictly decreasing x coordinate gives

integral_I (T0+kappa)^+(phi_t X)dt <= integral_l^u s(x)/v(x) dx.

The positive case has the same formula when V1>=v(x)>0. This follows by substitution dt=dx/V1 and reversal of the limits for decreasing x. It may replace s_i t_i in K. For several boxes the estimate may count an overlapping portion more than once, which is conservative.

## The cost bound and the maximal-domain inverse

The margin assumptions imply pointwise

(T0+kappa)^+ <= sum_i s_i 1_(B_i cap Q).

Integration over the whole orbit and the residence bounds give K. Every finite signed integral of T0+kappa is bounded above by this whole-orbit positive-part integral. In particular, for t>=0 and Y in Q,

log w0(phi_(-t)Y)-log w0(Y)
=integral_0^t 2(T0+1+c_l)(phi_(-s)Y)ds
<=2(1+c_l-kappa)t+2K.

The Jacobian of phi_(-t) is exp(-2c_l t). Therefore S_t f=f composed with phi_t satisfies

||S_t f||_(w0)^2<=exp(2K+2(1-kappa)t)||f||_(w0)^2,
||exp(-t)S_t||<=exp(K-kappa t).

The flow action is strongly continuous in L2(w0). Indeed compactly supported continuous functions in Q are dense; for them continuity follows on compact flow tubes from uniform continuity and the local bounds for the weight. The displayed operator bound, uniform for t in a bounded positive interval, extends this to every f. Thus the vector-valued Bochner integral defining R_- converges, with norm at most exp(K)/kappa.

For completeness its distributional and uniqueness assertions do not require any differentiability beyond C1 of V. On a relatively compact flow tube let h,g be locally L2 with V dot grad h=g distributionally. With a smooth compact convolution kernel eta_epsilon, the commutator is

V(X) dot grad(h*eta_epsilon)(X)-(g*eta_epsilon)(X)
=integral [(V(X)-V(Y)) dot grad eta_epsilon(X-Y)+(div V)(Y) eta_epsilon(X-Y)]h(Y)dY.

The bracket has integral0 in Y, by integration by parts, so h(Y) may be replaced by h(Y)-h(X). On a fixed compact set, C1 bounds for V and translation continuity of h in L2 show that the commutator tends to0 locally in L2: its kernel is bounded by a constant times epsilon^(-2) on a ball of radius O(epsilon), and the translation differences tend uniformly to0 in L2 there. The smoothed equation, integrated along the flow, then passes to the limit in L2 on compact sub-tubes because the finite-time Jacobians are bounded. This proves

h(phi_t X)-h(X)=integral_0^t g(phi_s X)ds

in local L2 and almost everywhere for each fixed finite t. A countable cover suffices whenever a global fixed-time identity is needed.

For f smooth compactly supported in Q, the finite integral R_N=-integral_0^N exp(-t)S_t f dt is C1, and differentiation along the flow gives

B R_N=f-exp(-N)S_N f.

For arbitrary f in L2(w0), approximate by such f. The operator B on its stated maximal domain is closed, since L2(w0) convergence implies local L2 convergence, and distributional derivatives pass to the limit on compact tests. The bound on S_t extends the identity first to R_N f and then, as N tends to infinity, to B R_-f=f. Finally, if Bh=0, apply the local flow identity to g=h. For each fixed t it gives S_t h-h=integral_0^t S_s h ds locally in L2; both sides belong to global L2(w0), so it is a global identity there. Strong continuity of S_s h makes the integral a continuous L2-valued function of t, and extends an identity on rational times to every t. The resulting Banach-space Volterra equation has the unique solution S_t h=exp(t)h, for example by applying the integral form of Gronwall to its difference from exp(t)h on each bounded time interval. Hence

||h||<=exp(K-kappa t)||h||, t>=0,

so h=0. This proves bijectivity and the asserted inverse bound. The argument is on the open quadrant; it asserts no classical trace or distributional equation across a singular weighted axis.

## A shorter conditional non-trapping theorem

This is separate from the inverse proof. Assume the two parity conditions stated above and add V2(x,y)>=m0 y for x>=0,y>0, with m0>0. Suppose P=(x*,0), x*>0, is an equilibrium, V1(x,0)<0 on0<x<x*, V1(x,0)>0 onx>x*, DV(0)=diag(-A,D) with A,D>0, and DV(P)=diag(Ap,mu) with Ap,mu>0. Assume also X dot V(X)>=k0|X|^2 for |X|>=R0, k0>0. Then every X in Q has backward limit P and |phi_t X| tends to infinity as t tends to infinity. No Poincare-Bendixson theorem is needed.

Indeed y(phi_t X)>=exp(m0t)y(X) gives forward escape and y(phi_(-t)X)<=exp(-m0t)y(X) gives backward approach to the x-axis. The radial inequality prevents backward escape to infinity: the closed radius-R0 disk is backward invariant, and a point outside enters within log(|X|/R0)/k0 backward time. Thus the backward orbit is eventually compact. Its alpha-limit set is nonempty, compact, connected and invariant, all by continuity of a complete flow and nested closures of connected half-orbits. It lies on the x-axis. Also x*<R0 because P is an equilibrium.

For every axis point x>0 distinct from x*, the one-dimensional backward axis orbit tends monotonically to x*, using the asserted signs and continuity. Thus if such a point belongs to the alpha set, so does P, by invariance and closedness. Near P, differentiability gives d/dt|X-P|^2>=lambda|X-P|^2 for some lambda>0. A sufficiently small closed disk about P is backward invariant and distances there decay exponentially in backward time. Any alpha set containing P therefore equals{P}. If there is no regular positive axis point, connectedness leaves only{0} or{P}. The case{0} is impossible for an open-quadrant orbit: in a small square V1/x<=-A/2 by parity and continuity. Eventual backward residence there would give x(phi_(-t)X)>=C exp(At/2)>0 tending to infinity, a contradiction. This completes the proof without a stable-manifold theorem.

## Conditional rational box constants and rounding

The specific numerical target proposed by the lead is B=[4.80,6.82]x[0,2.85], V1<=-13, T0<=1.23 on B, and T0<=-0.22 outside B. Assume also the complete quadrant-preserving constant-divergence flow and V2>=0. The residence bound is exactly101/650.

At kappa=1/5 the above upper-bound expression is

exp(K)/kappa=5 exp(1111/5000).

The claim that this expression equals, or is bounded above by,6.2 is to be checked and refuted if its certified lower endpoint exceeds6.2. This refutes the numerical deduction from the stated constants, not the possibility of some different argument proving an actual inverse bound6.2.

The same outside margin permits every0<kappa<=11/50, including equality. For fixed box constants the bound is

F(kappa)=exp((123/100+kappa)101/650)/kappa.

Its logarithmic derivative is101/650-1/kappa, strictly negative for0<kappa<=11/50. Thus its smallest value over this admissible interval occurs at kappa=11/50 and equals

(50/11) exp(2929/13000).

The interval audit will enclose both expressions by Arb exponential balls and an independent mpmath.iv positive Taylor series with an explicit geometric tail. For0<=z<1 and N>=0, the exponential series truncated after degreeN has remainder bounded by z^(N+1)/(N+1)! divided by1-z/(N+2), because the successive tail-term ratios are at most z/(N+2). The independent calculation uses N=128, both exact rational series sums and directed iv arithmetic; it checks the iv enclosure contains both rational endpoints. The saved-output auditor independently reconstructs the rational partial sum by direct powers and factorials. Together with the proved geometric remainder this is a complete rational certificate for the two scalar expressions, even without relying on either interval library exponential implementation. All decimal publication bounds are exact rational comparisons. No orbit integration or finite-domain field evaluation is included here.

## Scope and dependencies

The analytic statements above are standalone. Their application to the normalized X3 trial remains conditional on the global sign, box and complement certificates and the required smooth complete flow. Topic53 provides exterior outward drift and axis-quotient decay, but cannot fill the bounded-region obligations. Topic52 is a compatible, independently reviewed transport-domain and orbit-weight analysis, not a numerical input needed here. The actual normalization scalar comes from the pinned data only if these statements are applied to the trial.

Replacing T0 by a continuous E0=T0+bplus with bplus>=0 gives the same cost bound for E0. It also bounds the cost for T0 and hence the same pure transport inverse. It does not make an arbitrary measurable orbit correction a smooth weight, prove a Garding estimate, control the nonlocal IPM coupling, or supply a coupled inverse. No decisive endpoint follows.
