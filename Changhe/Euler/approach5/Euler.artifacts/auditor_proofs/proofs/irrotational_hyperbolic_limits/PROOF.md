# Irrotational hyperbolic limits and transported C1 fields

## Statements and hypotheses

Let B be a complete C2 vector field on R3 and let Psi_t be the flow of X=-B. Let W be C1 and suppose, for some kappa>0,

    W(Psi_t x)=exp(kappa t) DPsi_t(x) W(x),  t>=0.

The zero set Z={W=0} is invariant. Let K be a compact invariant hyperbolic set for Psi, containing no zero of B and lying in Z.

1. If the strong stable dimension on K is one, then every strong or weak stable manifold through K lies in Z. No divergence assumption is needed for this assertion.
2. Suppose div B=d is a positive constant, kappa>=d, and the strong stable dimension is two. Then a neighborhood of K lies in Z.
3. Under div B=d>0 and kappa>=d, if K is also locally maximal, every a with dist(Psi_t a,K)->0 belongs to Z. In the one-dimensional stable case kappa>0 alone is sufficient.

For the Euler profile take W=Omega, d=3c and kappa=1+c. For 0<c<1/2 one has kappa>d. Thus no vortical point has its backward limit inside a nonsingular locally maximal uniformly hyperbolic subset of {Omega=0}. This is a conditional exclusion, not an exclusion of all irrotational backward limits or mixed limits.

The proof uses the C2 stable-manifold theorem with uniform leafwise regularity, and the local stable-set characterization for nonsingular locally maximal hyperbolic flow sets. These are the explicit hyperbolic inputs. Their roles are described below. The curl relation is not used.

## The general curve comparison

The coordinator's Lemma 16.1 has a still more elementary form. Suppose x is in Z and a C1 curve gamma joins x to a. Assume all Psi_t gamma lie in one compact Q and there are C>=1 and e(t)>0 such that

    length(Psi_t gamma)<=C e(t),
    |DPsi_t(a)v|>=C^(-1)e(t)|v| for every v and t>=0.

Integrating DW along Psi_t gamma and using W(Psi_t x)=0 gives

    |W(Psi_t a)|<=C e(t) sup_Q |DW|.

Transport gives the reverse bound C^(-1)exp(kappa t)e(t)|W(a)|. Cancellation implies

    |W(a)|<=C^2 sup_Q|DW| exp(-kappa t).

Let t tend to infinity. This proves the lemma exactly as stated. For the one-dimensional stable case below, tangency gives a simpler comparison than constructing the full center-unstable cone claimed in the coordinator's first proof.

## One-dimensional stable leaves

Let q in K and let a be on a sufficiently short local strong stable arc through q. The transport identity gives the local flow commutation law

    Psi_t flow_W^u(a)=flow_W^{exp(-kappa t)u}(Psi_t a).

It can be used for every t>=0 with a fixed sufficiently small |u|. Indeed Psi_t a stays in a compact neighborhood of K, where W has a uniform local flow interval; the W-time on the right only decreases. The bracket identity and ODE uniqueness identify the right side with the Psi-orbit of flow_W^u(a). Its distance from Psi_t a is at most C |u| exp(-kappa t).

Since Psi_t a approaches Psi_t q exponentially with the same phase, flow_W^u(a) does so as well. The characterization of the strong stable manifold therefore places this W-curve in that stable manifold. Differentiating in u proves that W(a) is tangent to the one-dimensional strong stable leaf. The same argument holds at every point on the short stable arc I from q to a.

Put F=Psi_1 and J_n(z)=|DF^n restricted to T_z I|. Stable leaves of a C2 flow have uniform C^{1+beta} bounds on these local disks for some beta>0. Thus g(z)=log|DF restricted to the stable tangent| is uniformly beta-Hölder along the leaf. Intrinsic leaf distances contract exponentially. For z in I,

    |log J_n(z)-log J_n(a)|
      <=sum_(j=0)^(n-1) C (rho^j length(I))^beta <=D,

where 0<rho<1 and D is independent of n and z. Consequently

    length(F^n I)<=exp(D) J_n(a) length(I).

All these arcs lie in a compact set. Since W(F^n q)=0 and W is locally Lipschitz,

    |W(F^n a)|<=L exp(D) J_n(a) length(I).

Tangency and the transport law give the exact equality

    |W(F^n a)|=exp(kappa n) J_n(a)|W(a)|.

Cancel J_n(a)>0 and send n to infinity. Hence W(a)=0. Advancing any point of a global stable leaf into a local leaf proves the global assertion. Invariance of Z and flow saturation give the weak stable assertion. No differentiable transverse stable foliation is assumed: only uniform regularity along each stable disk is used.

## Two stable dimensions

A local strong stable disk now has dimension two. Flowing it for a short interval gives an open three-dimensional neighborhood of each q in K, by transversality to the nonzero flow direction. Let a lie in one of these flow-saturated disks, and incorporate its fixed phase into q.

The stable tangent plane at a contracts uniformly exponentially. The flow vector satisfies DPsi_t B(a)=B(Psi_t a), and its norm stays bounded above and away from zero after making the local disk small. The tangent plane and flow line are uniformly transverse along the forward orbit. It follows that

    ||DPsi_t(a)||<=C_a,  t>=0.

The constant divergence gives det DPsi_t(a)=exp(-dt). The smallest singular value therefore satisfies

    min_|v|=1 |DPsi_t(a)v|>=C_a^(-2) exp(-dt).

Combining with transport yields

    |W(a)|<=C_a^2 exp((d-kappa)t)|W(Psi_t a)|.

The last factor tends to zero because the orbit approaches K, where W vanishes. Thus kappa>=d suffices, including equality. This proves W=0 on each such open disk saturation and hence on a neighborhood of K. The coordinator's stricter kappa>d version is a valid special case. Its classification as finitely many attracting periodic orbits is not needed for this argument.

## From approach to K to a stable leaf

For a nonsingular locally maximal hyperbolic flow set, every point whose forward orbit converges in distance to K lies on a weak stable leaf of a point of K. The local form used here can be obtained with a finite system of small transverse flow boxes. On their transverse sections, local maximality and hyperbolic shadowing give a shadowing orbit in K for every sufficiently late orbit that remains in the isolating neighborhood. The unstable difference must vanish: otherwise forward expansion would force exit. The remaining transverse difference contracts exponentially. Smooth dependence of the short passage times makes the successive time corrections bounded by these exponentially contracting differences. Their sum converges, giving one limiting constant phase. Absorb this phase into the point of K. The original orbit is then on its global strong stable manifold. This explains why a time reparametrization with unbounded drift is not the conclusion used here.

Apply the preceding two cases. With div B=d>0, stable dimension zero cannot occur on a nonsingular compact hyperbolic set: two uniformly expanding transverse directions and a bounded nonzero flow direction would make the full forward Psi-Jacobian grow exponentially, contrary to exp(-dt). Different stable-index components can be treated separately. This proves statement 3.

Local maximality enters only this stable-set characterization, not the two leafwise assertions. It must not be dropped merely because K is compact and hyperbolic.

## Why the rate qualification matters

In a solid torus with coordinates (theta,x,y), let

    X=partial_theta-chi1 x partial_x-chi2 y partial_y,
    W=y^m partial_x,

where chi1>m chi2>0 and m is a positive integer. Then the central periodic orbit is an attractor, W is smooth and divergence free, W vanishes on that orbit, and

    [X,W]=(chi1-m chi2)W.

Thus transport holds with kappa=chi1-m chi2>0, but W is nonzero at nearby points with y!=0. Here d=chi1+chi2>kappa. This local model refutes extending the two-dimensional stable assertion using only kappa>0. It does not satisfy the global Euler hypotheses and is not an Euler counterexample.

## Audit scope

This confirms CO14's curve lemma and its intended profile corollary. The general nonprofile form must retain the divergence and rate condition in the two-dimensional stable case and hence in the unrestricted-index version of part (c). The proof also validates the corresponding hyperbolic section of the gamma_core response independently of its claims about nonhyperbolic limits. No statement about positive-volume approach to a general irrotational set follows from this proof.
