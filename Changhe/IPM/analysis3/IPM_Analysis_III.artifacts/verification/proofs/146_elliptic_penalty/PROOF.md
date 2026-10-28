# The noncharacteristic penalty from the equation

## Statement

Use X_s, A_v,A_u, w,z and R=grad<D>^(-1) as in topics123 and144. Set S=T+C_R on the actual maximal domain D_s={h in X_s:T h in X_s}. Fix 0<epsilon<=1/32 and a bounded real interval of lambda. For every a>0 there is C_a<infinity such that, with f=(S-lambda)h,

 ||W.R w||_2+||W.R z||_2
 <= C||f||_(X_s)+a||h||_(X_s)+C_a||h||_(X_(s-epsilon)).   (1)

Here C is independent of a, though it depends on the fixed order reduction, including N. This is a version of Q5 with an arbitrarily small high-norm error. Its square can be absorbed in the high-frequency energy estimate after the finite penalty coefficient L is fixed. It is sufficient for that estimate and makes no assertion that the unweakened Q5 has already been proved.

Also C_R is bounded on X_(s-epsilon) for the indicated epsilon. These are genuine lower-order spaces with the same radial weights and angular trace convention, with both Sobolev orders reduced by epsilon.

## Boundedness on the lower space

The comparable-annulus proof in proof 123 applies verbatim with s replaced by s-epsilon and sigma replaced by sigma-epsilon. The minimum bulk order is at least41/20-1/32>2, the maximum order is at most25/4, and the coefficient regularity H^(51/8) has a positive surplus. The odd division estimate in the cofactor identity uses one of two derivatives gained by a double commutator and therefore also persists. The six radial matrices depend on the radial weights delta,gamma,k, not on these small changes of Sobolev order. They have the same summable row and column bounds.

There is one change that must not be overlooked: the embedding into the old R_(4,sector) at the exact critical Hardy exponent is unavailable after reducing the order. Use the direct axis-row theorem in proof 140 instead. It gives Gamma_C/a in H^(51/8) from X_(s-epsilon), bounded and compact into H^(25/4), for every epsilon<=1/4. Its lift lies in the trace-unrestricted pair of lower spaces; subtracting it gives the zero trace by the exact axis identity. The resulting C_R is bounded on the closed lower space. No critical four-derivative embedding is presumed.

## Smooth-coefficient comparison

Let B_j be a smooth bounded vector field with all bounded derivatives. Write A=A_v and Q=<D>^(-1)A. Smooth symbolic composition gives, for each component,

 B_j partial_j Q v=Q(B_j partial_j v)+E_j v,

where E_j has relative order -1, up to arbitrarily small logarithmic losses from the smooth variable order. Indeed E_j=B_j[partial_j,Q]-[Q,B_j]partial_j. The first term has order s-1 with logarithms; the second has that same order. Thus

 ||B.R A v||_2<=C||B.grad v||_(H^(s-1))+C_B||v||_(H^(s-epsilon)). (2)

The mapping constant C of Q is fixed independently of B. The cofactor version has constant order sigma and is proved in exactly the same way. No inverse of A is used.

## Approximation of the actual field

The actual W belongs to W^(7,infinity) uniformly on the cylinder. Periodic convolution in theta and ordinary convolution in t give smooth W_j with all bounded derivatives, converging uniformly together with their first six derivatives. In particular W_j-W tends to zero in C^6_b. Multiplication by this difference on H^(s-1) has norm tending to zero: the maximum order is21/4<6 and the minimum is21/20>1, so the product argument of proof 123 applies with a uniform localized H^6 coefficient norm. The constant-order cofactor space H^(sigma-1) obeys the same estimate. This also follows directly by the dyadic product estimate, whose high-coefficient terms have the gap6-21/4=3/4.

Apply (2) with B=W_j. Replacing W_j.R A v by W.R A v costs at most ||W-W_j||_infinity||A v||_2. Replacing W_j.grad v on its right by W.grad v costs at most the small H^(s-1) multiplier norm of W_j-W times ||grad v||_(H^(s-1)), which is bounded by C||v||H^s. Choose j so that the sum of these two coefficients is at most a. We obtain

 ||W.R A v||_2<=C||W.grad v||_(H^(s-1))
                    +a||v||H^s+C_a||v||_(H^(s-epsilon)). (3)

The same j can be used for the cofactor. This argument tolerates constants in the smooth commutator growing with j: they multiply only the lower norm. It does not claim convergence in W^(7,infinity), which is generally false at the spline joins.

## Use of the actual equation

The bulk equation is

 W.grad v=f/b+(1+lambda-beta q)v-C_R h/b,

where beta=b'/b. Its scalar coefficients have the verified W^(7,infinity) regularity. The first term is bounded in H^(s-1) by ||f||X_s. The other two are bounded there by ||h||X_(s-epsilon), since epsilon<1 and C_R is bounded on the lower space.

For u=chi h/(bp), the exact equation has the additional term (W.grad chi)v/p and a different W^(7,infinity) scalar coefficient. The extra coefficient is supported in the fixed angular overlap where p is nonzero and s=sigma. Consequently that term is bounded in H^(sigma-1) by the lower bulk norm, since sigma-epsilon>sigma-1. This proves the same estimate for W.grad u. Insert both equation estimates into (3) to obtain (1).

All identities hold distributionally for h in D_s. Their terms lie in the spaces just displayed, so the smooth symbolic identities extend by ordinary Sobolev density of v and u separately. No approximation preserving the coupled axis constraint or dense transport graph core is required for (1).

## Absorption and scope

Given the finite L in proof 142, choose a so small that the coefficient of a^2||h||X_s^2 in L times the square of (1) is below any prescribed positive energy margin. The remaining terms are C_L||f||X_s^2+C_(L,a)||h||X_(s-epsilon)^2. This supplies the noncharacteristic penalty step with a controllable high-norm error. The principal transport energy formula and its maximal-domain limit are still independent obligations. No numerical value of any constant is certified.
