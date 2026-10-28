# Weight variation and the closed cubic trace

## Exact margin variation

Fix the actual vector field V=ell X+U[rho], where div V=2ell. Let q=V.X/r^2 and u=V.grad(theta). For angular exponent a and radial far shift Delta define

 w_(a,Delta)=|x|^(-2a) max(1,r)^(2a-5/4-2Delta).

The pure transport energy is

 Re <-T h,h>_w = int kappa_(a,Delta)|h|^2 w dX,
 kappa_(a,Delta)=1+ell+(mu'/2)q+a tan(theta)u,              (1)

where mu'=-2a for r<1 and mu'=-5/4-2Delta for r>1. The value on r=1 is immaterial for the integral. The weight is continuous there, so splitting the integration by parts at r=1 introduces cancelling interface terms. This identity holds first for the smooth parity core away from the axes and then on any closed realization justified by approximation.

Let b_plus=(|grad rho|-rho_y)/2 and m_(a,Delta)=kappa_(a,Delta)-b_plus. Because b_plus does not depend on the weight,

 m_(a,Delta)-m_(17/4,0)
 =(a-17/4)[tan(theta)u-q 1_(r<1)]-Delta q 1_(r>1).         (2)

This is an exact pointwise formula, not a sampled comparison.

To prove it, write log w=mu(t)-2a log|cos(theta)|. Then V.grad log w=mu' q+2a tan(theta)u. Integrating V.grad(|h|^2)/2 and using div V=2ell gives (1), and subtraction gives (2).

At infinity the actual finite-mode expansion gives q=ell+O(r^(k-1)) and tan(theta)u=O(r^(k-1)), uniformly in theta with the continuous axis extensions. The latter assertion uses parity: each finite angular velocity sine mode is divisible by cos(theta) at the vertical axis. Also b_plus=O(r^(k-1)). Hence

 lim_(r->infinity)m_(a,Delta)=1+(3/8-Delta)ell,             (3)

uniformly in angle and independently of a. A strictly positive limiting margin requires Delta<k+3/8. Formula (3) alone does not establish a positive global margin or any of the nonlocal mapping properties for the new weight.

## The scalar target changes when a changes

The exact polar norm of a lifted remainder with a fixed admissible angular cofactor has radial weight

 g_(a,Delta)(t)=exp((8-2a)t) for t<0,
               exp((27/4-2Delta)t) for t>0.              (4)

The power8 comes from r^6 in |x^2 y|^2 and r^2 in area measure. The scalar axis target associated with this radial norm has the same endpoint powers. Let A beta=d beta'+b beta be the actual scalar axis operator, with d->D>0 and b=O(exp(2t)) at the inner end. Let H be its integrating factor, H->1 at the inner end and H comparable to exp((k-3)t) at the outer end.

For a>4 and Delta<k+3/8, the closed-trace scalar inverse of proof 38 applies with

 sigma=a-4>0, kappa=k+3/8-Delta>0.                         (5)

In particular gamma/(dH) has an integrable reciprocal-weight estimate at both ends, and its integral defines the bounded free cubic coefficient J. If the cutoff graph characterization is also used, require sigma<2, as in that topic.

For a<=4 this same finite-J scalar realization is not surjective onto the full target (4). This is an actual obstruction, not merely failure of one estimate.

For a<4 choose a smooth nonnegative gamma equal1 for t<=-2 and zero for t>=-1. Equation (4) shows gamma belongs to the target because 8-2a>0. But any solution would satisfy

 (beta/H)'=gamma/(dH) -> 1/D as t->-infinity.

It therefore cannot have a finite limit J there.

For a=4 instead choose a smooth nonnegative gamma equal 1/(1+|t|) for t<=-2 and zero for t>=-1. It belongs to the target because its square is integrable, but gamma/(dH) is positive with divergent integral at the inner end. Again beta/H has no finite limit. These examples leave the outer target and its endpoint condition harmless.

The cubic functional is also unbounded even on compactly supported data at these parameters. If a<4, translate a fixed positive bump to t=-N; its target norm tends to zero exponentially, while the integral defining J stays bounded away from zero. If a=4, take gamma_N=N^(-1/2)phi(t/N) with nonnegative nonzero phi supported in (-2,-1). The target norm stays bounded, whereas |J_N| grows like sqrt(N). Thus no bound for a closed cubic trace in the old target norm survives at or below a=4.

## A possible change of parameters, not an established new inverse

The angular and inner radial exponents need not be tied. One may instead consider

 w=|cos(theta)|^(-2a) r^(-2a_0) for r<1,
 w=|cos(theta)|^(-2a) r^(-5/4-2Delta) for r>1,

with a_0>4 fixed. Its scalar inner exponent is 8-2a_0, so the preceding scalar obstruction from lowering a is avoided. Relative to the original weight, the angular variation contributes (a-17/4)tan(theta)u, while the inner radial variation contributes -(a_0-17/4)q. This is only a parameterization and an exact energy identity. The coupling, compactness, high-space embeddings and all numerical margins for this altered family still require separate proofs.

## Scope

The margin formula requested in theory author note25 is correct. It does not authorize reuse of the old Fredholm theorem after an arbitrary parameter change. In particular the proposed a=3.6,3.8 and the critical a=4 cannot preserve the same full scalar target together with a finite closed cubic trace. Values a>4 avoid this specific obstruction, subject to the other hypotheses.
