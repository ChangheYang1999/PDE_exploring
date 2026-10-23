# Tails of a tanh network with directional and logarithmic radial inputs

Date: 2026-10-23. Status: proved statement about the documented representation, not a theorem excluding all networks or all Euler profiles.

## Statement and hypotheses

Let the input features be ξ(y)=y/sqrt(l²+|y|²) and t(y)=log(1+|y|²/l²)/s, with l,s>0. Let F(ξ,t) be a finite feedforward network with a tanh first hidden layer, smooth subsequent tanh hidden layers and a linear output. For every first-layer neuron j suppose its coefficient a_j of t is nonzero. Let ε=min_j 4|a_j|/s>0. Then, uniformly on the unit sphere with the first angular derivative and radial derivative measured by R∂_R,

    F(ξ(Rn),t(Rn)) = F_infinity + O(R^-ε),

where F_infinity is independent of n. The statement holds componentwise. The pressure and potential networks may have different ε. If a radial coefficient is exactly zero, this conclusion need not hold because that neuron retains its angular input.

For a Q-projected vector potential correction

    A_corr(y)=(1+R²/L²)^((d+1)/2) [F(y)+QF(Qy)]/2

with d+1≠0 and Q=diag(-1,-1,1), the leading correction is

    A_corr(Rn)=L^(-(d+1)) R^(d+1) F_infinity,3 e_z
               + O(R^(d+1-min(ε,2))).

Consequently its leading velocity is the axisymmetric swirl

    U_corr(Rn)=L^(-(d+1))(d+1)F_infinity,3 R^d (n₂,-n₁,0)
               + O(R^(d-min(ε,2))).

A scalar pressure correction with envelope (1+R²/L²)^d has constant leading angular coefficient. These conclusions concern the documented dir_log feature set with zero envelope shifts.

## Proof

At y=Rn, ξ=n+O(R^-2) uniformly with angular derivatives, and t=(2/s)log R-(2/s)log l+O(R^-2). The j-th first-layer preactivation is therefore

    (2a_j/s)log R + b_j(n) + O(R^-2),

where b_j and its angular derivatives are bounded. Since a_j≠0, it tends uniformly to the sign-determined infinity. The elementary expansion tanh z=1-2 exp(-2z)+O(exp(-4z)) as z→+infinity, and its negative counterpart, give

    tanh(preactivation_j)=sign(a_j)+O(R^(-4|a_j|/s)).

Differentiating the same expansion in n or with R∂_R preserves this order. Subsequent affine maps and tanh maps have bounded derivatives in a neighborhood of the limiting vector, so the asserted estimate propagates through the network.

The Q projection of a constant vector is its vertical component. The potential envelope is L^(-(d+1))R^(d+1)(1+O(R^-2)). Multiplying the expansions and taking curl gives the velocity formula, because ∇R^(d+1)×e_z=(d+1)R^(d-1)(y₂,-y₁,0). The scalar projection preserves a constant. This proves the claims.

## Consequence for Euler balance

For d=1-1/c, the linear similarity operator has multiplier -cδ on a velocity correction of degree d-δ. Its residual is therefore of the same degree d-δ. The natural convection and pressure-gradient terms have degree 2d-1=d-1/c. Any nonzero correction with 0<δ<1/c decays too slowly to be balanced at that nonlinear order. Thus slow saturation corrections require cancellation, zero coefficients or a changed tail representation; a small linear-relative residual is insufficient.

This is an asymptotic statement, not a computed lower bound for an arbitrary checkpoint. Network coefficients can cancel, and exactly zero radial weights permit angular limits. A small ε can place the asymptotic regime beyond any accessible sampling radius. The present model family therefore contains exceptions, but generic nonzero radial weights do not provide a freely learned leading angular tail. A separate bounded-direction network for the leading potential, together with explicit subleading envelope families, avoids this particular restriction and is a permitted next representation to compare.

The prompt's seed already supplies nonzero n=2 leading content. Adding a generic correction of the form above changes its leading tail only by an axisymmetric swirl, while the pressure's learned leading correction is constant. This is a restriction on how that seed's leading angular functions can be repaired, not proof that no solution lies in the representation.
