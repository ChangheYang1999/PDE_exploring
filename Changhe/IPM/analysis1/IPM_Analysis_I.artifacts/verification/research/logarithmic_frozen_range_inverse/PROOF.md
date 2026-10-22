# Quantitative range inverse and exact compatibility conditions inside the frozen logarithmic strip

Date 2026-10-22T03:30:43.192337+00:00. Standalone proof written before new calculations. Status OPEN pending independent code and actual-model review. Dependencies: logarithmic_frozen_spectrum/PROOF.md and its POSTREVIEW_ADJUDICATION.md identify the full group, maximal domain and actual canonical parameters. This result treats only the global frozen transport, not the full IPM operator.

## Exact statement and spaces

Let A>0, D=2A+1, a real and s>=0. Define Y_(a,s) on x>0,y in R by the norm of F(z,y)=exp((1/2-a)z)h(exp z,y) in the Fourier Sobolev space H^s(R^2). Put

 T=-A x partial_x+D y partial_y-1,
 D(T)={h in Y:Th in Y distributionally},
 c=-A(a-1/2)-1, d_minus=c-D/2, d_plus=d_minus+Ds.

Assume the OPEN interior regime d_minus<0<d_plus. Write u=-d_minus>0 and v=d_plus>0, so u+v=sD. In particular s>0. Define the strictly positive number

 m(u,v,D)=min(u,v)^2                           if min(u,v)<=D,
 m(u,v,D)=D^2+2D(u-D)(v-D)/(u+v-2D)           if min(u,v)>D.             (1)

Then T is injective and has CLOSED range of infinite codimension. There is an explicit orthogonal projection Pi in Y such that

 Ran(T)=ker(Pi),
 ||h||_Y<=m^(-1/2)||Th||_Y for every h in D(T).                         (2)

Consequently each forcing f satisfying Pi f=0 has a UNIQUE solution h in D(T), with ||h||_Y<=m^(-1/2)||f||_Y. The inverse from ker(Pi), with the inherited Y norm, into the base Y has norm EXACTLY1/min(u,v) whenever min(u,v)<=D. The expression m^(-1/2) in the second case is an upper bound only; no exact inverse norm is asserted there. Into the sum graph norm ||h||_Y+||Th||_Y the inverse bound is1+m^(-1/2).

These statements persist on odd-in-y fields and their real subspace. Infinite codimension does not make this a Fredholm inverse or a surjective inverse onto all Y. In particular no full IPM compatibility condition or range estimate is inferred from it.

At the canonical dyadic k, with A=2/k-1 and a=0,s=153/50, one has u=1+1/k<D=4/k-1 and v>0. The exact range-inverse base norm is k/(1+k). This supplies a quantitative inverse only after imposing the entire infinite family of constraints below. The unrestricted frozen operator in that space is still not onto.

## Explicit unitary coordinates and compatibility projection

For eta positive or negative, write B(xi)=1+xi^2, ell(xi)=log(B)/2 and

 tau=log|eta|-ell(xi), eta=sign*sqrt(B)exp(tau),
 W(xi,tau)=[|eta|(B+eta^2)^s]^(1/2),
 (U h)_sign(xi,tau)=exp(iAxi*tau/D)W(xi,tau)Fhat(xi,eta).

The exact Jacobian d eta=|eta|d tau makes this unitary onto two copies of L2(dxi d tau). The original Fourier group is exp((c-D)t)exp(-iAxi*t)Fhat(xi,exp(-Dt)eta). Under U it becomes translation tau->tau-Dt times the positive amplitude with logarithmic derivative

 d(tau)=-u+(u+v)r(tau), r(tau)=exp(2tau)/(1+exp(2tau)).

Thus U T U^(-1)=Q=-D partial_tau+d(tau), on the full domain H^1_tau={V in L2:partial_tau V in L2}, in each copy. This group-level identity identifies the maximal distributional domain and entails no hidden matching at eta=0. The adjoint is Q*=D partial_tau+d on the same derivative domain.

Set

 M(tau)=exp(-u*tau/D)(1+exp(2tau))^(s/2),
 g(tau)=1/M(tau)=exp(u*tau/D)(1+exp(2tau))^(-s/2).

Every Q-kernel solution is C(xi)M, and none is nonzero in L2 because M grows at both ends. Every Q*-kernel solution is C(xi)g. Here g and g' are in L2: their tails are exp(u*tau/D) at minus infinity and exp(-v*tau/D) at plus infinity, and g'=-(d/D)g. Denote

 N_g=||g||_2^2=(1/2) integral_0^infinity q^(u/D-1)(1+q)^(-(u+v)/D)dq.  (3)

Both endpoints converge, so0<N_g<infinity. The equality is just q=exp(2tau); no special-function value or numerical integral is assumed.

In each transformed copy define

 (Pi_U V)(xi,tau)=g(tau)/N_g * integral_R g(t) V(xi,t)dt.               (4)

Cauchy-Schwarz gives a bounded operator of norm1. Direct substitution proves Pi_U^2=Pi_U and self-adjointness because g is real. Its range is exactly ker Q*, an infinite-dimensional closed copy of L2(R_xi). Let Pi=U^(-1)Pi_U U. The exact compatibility conditions are therefore

 integral_R g(tau)(U f)_sign(xi,tau)d tau=0
 for almost every xi and each sign.                                  (5)

For odd y the two sign constraints coincide; the family indexed by xi remains infinite. Real odd fields have transformed relation V(-xi,tau)=-conjugate(V(xi,tau)), preserved by Pi_U and Q. Infinitely many real independent C can be chosen as i times real even functions.

One can equivalently write(5) in the original Fourier variables as

 integral_0^infinity eta^(-c/D+iAxi/D) Fhat_f(xi,sign*eta)d eta=0,       (6)

for almost every xi and both signs. This is a complex Mellin moment, not a pointwise trace at eta=0. To justify it, U^(-1)g equals a nonzero xi-dependent scalar times

 |eta|^(-(c+iAxi)/D)(1+xi^2+eta^2)^(-s).

The weighted Fourier pairing with Fhat_f cancels the Sobolev weight and conjugates its phase, giving(6). The scalar is B^(s/2-u/(2D)+iAxi/(2D)), never zero. Each integral is absolutely defined for almost every xi by the weighted Cauchy-Schwarz inequality, since this adjoint vector lies in that one-dimensional weighted Fourier fibre. No unweighted L2 bound on the raw moment in xi is claimed; the normalized transformed projection(4) is the bounded map.

## The coercive identity, with its minimum calculated exactly

For a smooth compact V(xi,tau), integration by parts gives

 ||QV||_2^2=D^2||partial_tau V||_2^2+
 integral_(xi,tau) [d(tau)^2+D d'(tau)] |V|^2 dxi d tau.              (7)

Indeed the cross term is -2D Re integral d*(partial_tau V)*conjugate(V)
 =-D integral d*partial_tau|V|^2=D integral d'|V|^2.
The sign is PLUS. Because d,d' are bounded, smooth compact functions are dense in H^1_tau (truncate and mollify in both variables), and all terms are continuous in that norm. Thus(7) extends to the full maximal domain, with no assumed boundary trace.

Using r in(0,1), d=-u+(u+v)r and d'=2(u+v)r(1-r), the potential in(7) is the quadratic

 W0(r)=u^2+2(u+v)(D-u)r+(u+v)(u+v-2D)r^2.                           (8)

Its infimum for0<r<1 equals its minimum on[0,1]. If u+v<=2D it is concave or linear, so the minimum is min(u^2,v^2). If u+v>2D, its vertex is

 r_*=(u-D)/(u+v-2D).

This vertex lies strictly inside[0,1] exactly when u>D and v>D. Otherwise the minimum is at an endpoint, again min(u^2,v^2). At an interior vertex direct completion of the square yields

 W0(r_*)=D^2+2D(u-D)(v-D)/(u+v-2D).

If min(u,v)<=D, the vertex cannot be interior in the convex case, which proves all of(1). Its positivity is explicit, not an unchecked compactness argument. Formula(7) now proves(2).

## Closed range, existence, uniqueness and sharpness

The operator Q is closed on H^1_tau and(2) bounds it below in the ambient L2 norm. Suppose QV_n tends to f in L2. Then(2) makes V_n Cauchy in L2. If V_n->V, closedness gives V in D(Q) and QV=f. Hence Ran(Q) is closed. In a Hilbert space its orthogonal complement is ker Q*, as follows directly from the adjoint definition; consequently Ran(Q)=(ker Q*)^perp=ker Pi_U. This proves existence for precisely(5), with the bound in(2). The kernel calculation gives uniqueness, also already implied by the bound. Transferring by U proves every assertion about T.

When min(u,v)<=D, (1) and(2) give norm at most1/min(u,v). For the opposite inequality choose normalized smooth packets

 V_N=phi(xi) N^(-1/2)chi((tau-N^2)/N)

if v<=u, or center -N^2 if u<=v, with ||phi||_2=||chi||_2=1 and chi supported in(-1,1). They belong to D(Q), and ||partial_tau V_N||=||chi'||/N. On their supports d tends uniformly to v or -u respectively, so ||QV_N||->min(u,v). Their forcings QV_N automatically lie in Ran(Q), and the inverse sends them to unit V_N. Hence its norm is at least1/min(u,v), proving sharpness. The same packets with phi=i times real even phi_0 and real chi establish sharpness in the real odd subspace. The full real case follows as well.

For the graph bound, ||h||+||Th||<=(m^(-1/2)+1)||f||. Also the equation directly gives ||partial_tau U h||<=D^(-1)(1+max(u,v)m^(-1/2))||f|| if such a transformed derivative bound is needed. This is a derivative along tau only; it is not a gain of all physical Sobolev derivatives.

## Scope and verification plan

This proof strengthens the earlier interior-strip result by CLOSEDNESS, exact compatibility projection and an explicit range inverse. It does not change that model's infinite cokernel and failure of surjectivity, or turn the strip into resolvent. The full variable/nonlocal IPM linearization has different couplings and may have a different range; nothing here identifies its solvability constraints. At a=0 this is a potential frozen component of a future formulation only, not an a posteriori theorem, no distance bound and no PDE endpoint.

The primary path will independently check(8), its vertex value and the signs/exponents in(6), then decode the actual parameters from the NPZ. A separate exact-polynomial path will derive the adjoint/Mellin exponent directly in the original Fourier weighted pairing, reconstruct the quadratic by independent coefficients and decode k from integer hexadecimal JSON with fmpq. Representative exact cases include both minima regimes and their boundary. Any displayed scalar enclosure will use exact rational comparisons. Actual Claude Opus5.5 review and later own adjudication are required before acceptance. Source pins establish byte identity only.
