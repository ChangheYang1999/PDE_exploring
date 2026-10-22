# A fixed radial tail exponent does not give an unconstrained similarity exponent

Status: independent representation audit. This diagnoses a finite parameter family and an intermediate snapshot. It is not a nonexistence theorem for the B2 equations.

## Statement and representation

Use x=r sin(phi), y=-r cos(phi), and represent Theta=x^2 F, Omega=xG by finitely many cosine modes. Let b>0 be a fixed basis parameter, L>0 and

    t=1-(1+r/L)^(-1/b).

Near t=1, let every radial coefficient be (1-t)^p times a polynomial in t, as is true on the last interval of a finite clamped spline basis. For F choose p=b+2; for G choose p=b+1. Multiplication by t^min(k,2), or deleting finitely many coefficients at the origin, does not alter this endpoint structure. Let beta be the separate exponent used in the PDE.

Unless the entire leading angular coefficient of F vanishes, temperature has a smooth angular asymptotic

    Theta(r e(theta))=r^(1-2/b) A_b(theta)+O(r^(1-3/b)+r^(-2/b))

with A_b not identically zero. A nontrivial exact B2 profile in this family, with a sublinear canonical velocity, must then have beta=b. A finite-box least-squares fit with beta different from b cannot remove this leading far-field transport defect.

## Derivation

Set h=1-t. The finite endpoint polynomials give F=h^(b+2)[P_0(theta)+h P_1(theta)+...], with finite smooth angular coefficients. Since h=(L/r)^(1/b)(1+O(r^(-1))), multiplication by x^2 gives the stated leading power. The expansion can be differentiated at fixed angle because it comes from explicit smooth finite functions, not an arbitrary little-o remainder. Similarly Omega has leading degree -1/b unless its leading coefficient vanishes.

These fields have uniformly power-decaying vorticity. The independently established canonical inverse estimate therefore gives |V|<=C r^(1-delta) for some delta>0. At an angle where A_b is nonzero,

    W.grad Theta-(beta-2)Theta
      =[beta(1-2/b)-(beta-2)]r^(1-2/b) A_b+o(r^(1-2/b))
      =2(1-beta/b)r^(1-2/b)A_b+o(r^(1-2/b)).

The V term is lower order because grad Theta=O(r^(-2/b)). Hence exact equality forces beta=b. Equivalently, the independently proved angular temperature limit has degree 1-2/beta and nonzero angular coefficient, which must match this explicitly differentiated finite representation.

If the first j endpoint coefficient functions vanish identically and the next does not, the actual leading degree is 1-(2+j)/b. The same computation forces

    beta=2b/(2+j),  j a nonnegative integer.

If every endpoint polynomial coefficient vanishes, F is identically zero outside its last nonzero spline interval and Theta is bounded. For beta>2 that is impossible for a nontrivial profile by the temperature transport theorem. For beta=2, compact support also contradicts the previously proved finite-temperature-Lp exclusion. Thus an exact finite-family profile cannot evade all leading powers by an identically zero exterior temperature.

The discrete exponent restriction is a property of this finite basis with fixed b. It does not quantize beta for the PDE, since a different representation or changing b with beta removes the restriction. For b=3 and beta>=2 the only allowed values from the displayed formula are beta=3 (j=0) and beta=2 (j=1). Updating the basis parameter or demonstrating a controlled approximation sequence is needed for a general free-beta search.

## Horizontal normalized residual limits

Suppose the leading temperature and vorticity coefficients on y=0 are nonzero. Write m_b=1-2/b. Then on that ray

    Theta(r,0)~A_0 r^m_b,  Omega(r,0)~C_0 r^(-1/b).

The canonical V is lower order than beta X. Its contribution to either transport equation is lower order, as are the source Theta_x and all higher vorticity terms relative to the leading vorticity term. The prompt's original grouped pointwise normalizers therefore give

    |R_Theta|/N_Theta -> |beta m_b-(beta-2)|/[beta |m_b|+|beta-2|],
    |R_Omega|/N_Omega -> |1-beta/b|/[1+beta/b].

The denominators in these formulas are positive for the intermediate parameters below. They are not artificial floors. The numerator at beta=b vanishes, so subleading terms would then need a separate audit.

## Serialized intermediate state

The char2 snapshot archived at 14:04:57 UTC has beta=2.565219672568257, b=3 and L=1.5. Its endpoint coefficients give

    A_0=0.231031053151114,
    C_0=-2.61032655929686,
    temperature degree=1/3,
    required temperature degree=0.220339676407662.

These endpoint coefficients are identical under both recorded source versions, because the extra t factor tends to one and the origin mask leaves the final clamped coefficient unchanged. Thus the predicted horizontal normalized limits are

    |R_Theta|/N_Theta -> 0.204080124798805,
    |R_Omega|/N_Omega -> 0.0781245580609937.

This is a precise far-field rejection of that intermediate state, independently of the origin smoothness defect. It is not a claim that later iterates have the same coefficients or that the authors submitted this state as a successful candidate. The numbers are independently computed from the serialized last coefficients with a cosine recurrence; the full finite-difference and value-sample evidence is recorded separately.

Dependencies: finite polynomial expansion on the last spline interval, elementary differentiation of the explicit radial map, the independently proved whole-plane inverse growth estimate, and the exact B2 transport equations. No fitting-lane code is imported.
