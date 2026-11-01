# Amplitude normalization of tuning-response bounds

Status: the scaling follows from the admitted homogeneous response theorem240; the explicit counterexample is independently checked at512 and1024 bits (V521).

## Statement

Fix h>=2 and Q>2h with gcd(h,Q)=1, and let sigma_k(f) denote the coefficient of the next compatibility obstruction per unit free stream harmonic at order kQ, for a finite odd-sine leading profile f. Then for every real epsilon,

    sigma_k(epsilon f)=epsilon^Q sigma_k(f).

Consequently a unit-profile bound |sigma_k(f)|>s implies |sigma_k(epsilon f)|>|epsilon|^Q s for epsilon nonzero. It does not imply the unscaled bound s for arbitrary nonzero epsilon. This changes no convergence theorem obtained by scaling the whole series after proving a unit-profile certificate.

## Proof

The low density and stream coefficients at order r before the first free harmonic are homogeneous of degree r in f, by induction on the quadratic recurrence and linear Poisson inverse. In the response recursion, the initial perturbation is a unit stream harmonic and therefore has degree zero in f. At response stage r, the direct term multiplies it by a degree-r low field. Every other term multiplies a degree-j propagated perturbation by a degree-(r-j) low field. Inductively all response fields at stage r are homogeneous of degree r. The final compatibility coefficient at r=Q has degree Q. Scaling f by epsilon gives the asserted identity, including epsilon=0.

For a compatible tuned full sequence at nonzero epsilon, its order-n density, stream and free coefficients scale by epsilon^n. Thus the convergence variable is |epsilon|r^(-delta), with delta=2h/Q, and the sufficient radius gains the factor |epsilon|^(1/delta). The previously certified radii already have this factor. Their proofs remain valid.

## Explicit normalization check

The unit sin7 profile at delta4/5 has first response approximately1.94701466744668482055e-5. At epsilon=1/2 the response is smaller by2^5, approximately6.08442083577089006422e-7, which is below2^-20. Fresh512-bit and1024-bit Cartesian response evaluations verify these inequalities, with agreement at the first three response indices for both unit and half amplitude. The numerical response inequalities in Corollary T_(Q,h).9(c) are therefore correct for epsilon=1; if they refer to the displayed general-amplitude profiles, they require the factor |epsilon|^Q.

Dependencies:01 for the recurrence,144 for the finite response recursion,240 for homogeneous degree Q,241 for the unit sin7 certificate. This is a normalization correction, not a failure of existence, uniqueness or any admitted exterior radius.
