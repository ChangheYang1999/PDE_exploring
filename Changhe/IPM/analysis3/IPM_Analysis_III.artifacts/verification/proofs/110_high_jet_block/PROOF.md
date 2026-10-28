# Higher-order compactness of the free jet block

## Spaces, coefficients and theorem

Use the actual low scalar realization of proof 38, with sigma=1/4, kappa=k+3/8, d bounded away from zero, D=4ell-1 and

 A beta=d beta'+(D-d-2d')beta,
 H=exp(-integral_(negative infinity)^t (D-d-2d')/d),
 beta=Hz in B, z(+infinity)=0.

The norm of B includes |J|, z' in its exponential weight, and both Hardy terms, as specified in proof 38. Set g(t)=exp(-t/2) on t<0 and exp(27t/4) on t>0. Let G_N=H_g^N, the Hilbert space whose weak derivatives through order N belong to L2(g dt). Define

 B_N={beta in B:A beta in G_N},
 ||beta||_(B_N)^2=||beta||_B^2+||A beta||_(G_N)^2.

Assume d belongs to W^(N+1,infinity) locally, is globally bounded above and below by positive constants, and its derivatives through order N+1 are bounded. Require d-D and its positive-order derivatives to be O(exp(2t)) at negative infinity, and d-ell and its positive-order derivatives to be O(exp(-(1-k)t)) at positive infinity. Assume alpha belongs to W^(N+1,infinity) locally, is bounded at negative infinity, has alpha^(j)=O(exp(2t)) there for1<=j<=N+1, and has alpha^(j)=O(exp((k-3)t)) at positive infinity for0<=j<=N+1. The cutoff chi_0 equals1 near negative infinity, vanishes near positive infinity, and has bounded weak derivatives through order N. These conditions hold for the actual modal background for integers0<=N<=6.

Let E beta=x^2 y beta(log r). The complete normalized axis coupling from this input satisfies

 beta -> Gamma_(E beta): B_N -> G_N

and is Hilbert-Schmidt. In conjunction with proof 109, the full axis row is Hilbert-Schmidt, hence compact, on

 E B_N direct-sum R_(max(N-2,0),s) -> G_N.                 (1)

In particular, choosing Gamma_H=G_6 makes the compactness hypothesis J2 of the block continuation theorem valid on every high remainder domain continuously embedded in R_(4,s). This is a precise sufficient condition for J2, not a proof of the other high-space hypotheses.

## The scalar graph gives one radial derivative

Choose a smooth cutoff chi(t) equal1 at negative infinity and0 at positive infinity. The scalar endpoint estimates give the norm equivalence

 ||beta||_(B_N) equivalent to |J|+||beta-J chi||_(G_(N+1)).  (2)

Here and below equivalence constants are finite and depend on the displayed coefficient bounds; no numerical value is asserted.

To prove the base integrability in (2), write beta-J=H(z-J)+J(H-1) at the left endpoint. H is bounded there, H-1=O(exp(2t)), and the weight for z-J is exactly g. At the right endpoint H^2 g is comparable to the weight for z. Thus v=beta-J chi belongs to L2(g dt), with a norm bounded by ||beta||_B. Write p=(D-d-2d')/d. The scalar equation is

 v'=(A beta)/d-pv-J(p chi+chi').                           (3)

The last coefficient belongs to G_N by its decay at the left endpoint and its compact support at the right endpoint. Multiplication by p and1/d is bounded on G_j for0<=j<=N by the Leibniz rule and the stated bounded weak derivatives. Starting from v in G_0 and A beta in G_N, (3) proves v in G_1, then G_2, and so on through G_(N+1), with the claimed bound. Conversely (3) and the same product estimates put A beta in G_N when v is in G_(N+1). The low B norm is then controlled by |J| and the weighted H1 norm using the scalar Hardy realization. This proves (2), as well as completeness of B_N.

Weighted one-dimensional H1 evaluation now gives, for0<=j<=N,

 |beta(t)|<=C||beta||_(B_N), t<=0,
 |beta^(j)(t)|<=C exp(t/4)||beta||_(B_N), t<=0, j>=1,
 |beta^(j)(t)|<=C exp(-27t/8)||beta||_(B_N), t>=0.          (4)

For example on the left apply the ordinary H1 evaluation bound to exp(-t/4)v and its derivatives; on the right apply it to exp(27t/8)beta. The exponentials have constant logarithmic derivatives, so the needed H1 norms follow directly from (2). These estimates are for continuous representatives through order N and hold uniformly up to the endpoints of the two half-lines.

## Canonical finite-mode formula

The exact Green calculation in proof 46 gives

 P(t)=integral_(exp(t))^infinity s beta(log s) ds,
 Q(t)=exp(-4t) integral_0^(exp(t)) s^5 beta(log s) ds,
 S(t)=exp(-6t) integral_0^(exp(t)) s^7 beta(log s) ds,
 c=(1/4) integral_0^infinity s beta(log s) ds,
 V_beta=P/4-Q/4+S/2,
 V_beta'=Q-3S.                                           (5)

These are the canonical full-plane velocity traces; no independent harmonic field is added. Every integral converges by (4). Differentiation gives

 P'=-exp(2t)beta,
 Q'=exp(2t)beta-4Q,
 S'=exp(2t)beta-6S.                                      (6)

At negative infinity P-4c, Q and S, and their derivatives through order N+1, have B_N-dual norm at most C exp(2t). Indeed their undifferentiated integrals use the bounded beta estimate in (4), and repeated use of (6) uses derivatives of beta only through order N. At positive infinity P,Q,S and their derivatives through order N+1 have dual norm at most C exp(-11t/8). For P this follows by direct integration of exp(2t)beta; for Q,S split the moment at t=0. Their inner moment contributions decay as exp(-4t), exp(-6t), while the remaining integrals decay as exp(-11t/8). Equation (6) preserves these bounds under differentiation.

## Complete coupling and Hilbert-Schmidt proof

The axis row equals

 Gamma_(E beta)=(alpha'-alpha)V_beta-2alpha V_beta'
                            +c chi_0(alpha+alpha'/3).      (7)

Near negative infinity, use the exact cancellation

 Gamma_(E beta)=(alpha'-alpha)(V_beta-c)
                              -2alpha V_beta'+(4/3)c alpha'. (8)

The coefficient assumptions and (5)-(6) show that every weak derivative of (7) through order N is a bounded evaluation functional on B_N whose dual norm is at most C exp(2t) for sufficiently negative t. At positive infinity chi_0=0, and the corresponding dual norm is at most C exp((k-35/8)t). On the fixed intermediate interval the dual norms are bounded almost everywhere. The possible jumps in the highest coefficient derivative do not affect these L2 statements.

Their squared g-weighted bounds integrate, with endpoint exponents7/2 and2k-2. Let (e_j) be an orthonormal basis of B_N. Tonelli and the Hilbert-space representation of each evaluation functional give

 sum_j ||Gamma_(E e_j)||_(G_N)^2
 =sum_(q=0)^N integral g(t) ||[beta -> partial_t^q Gamma_(E beta)(t)]||_(B_N*)^2 dt
 <infinity.

Weak differentiation follows first from (5)-(7) for smooth beta and then from the bounds and graph approximation, or directly from (3) and the absolutely convergent moment formulas. Thus the map is Hilbert-Schmidt. Combining it with the result of proof 109 proves (1).

## Scope

The theorem supplies the previously separate free-jet compactness obligation for an explicit integer-order scalar target. It does not assert that G_6 is the only suitable target, or that the high remainder transport estimate holds. The block X=Err+C_R E still needs its complete two-dimensional high-target mapping, and the actual high remainder domain must be checked to embed into R_(4,s). No inverse norm, injectivity or nonlinear existence follows from (1) alone.
