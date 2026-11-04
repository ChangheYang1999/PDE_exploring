# Direct recheck of the natural pointwise tail inputs

This rechecks the two pointwise inputs already used in A477. It adds no claim that velocity decay implies a derivative hypothesis, and it does not require construction of a scattering map.

## 1. Exact statement

Fix 0<c<1 and any finite real omega. Let J(y1,y2,y3)=(-y2,y1,0), U in C2(R3;R3) and P in C1(R3) solve

    (1-c)U+B.grad U+omega JU+grad P=0, div U=0,
    B=(cI-omega J)y+U.

Assume M=sup_R3 |U|<infinity and the exterior derivative supremum m(r)=sup_(|y|>=r)||DU(y)||, in the matrix operator norm, satisfies

    integral_1^infinity m(r)dr/r<infinity.

Then Omega=curl U obeys |Omega(y)|<=C(1+|y|)^(-1/c) for a finite profile-dependent C. If additionally 1/3<c<1 and U(R .) tends to zero in distributions, then also |U(y)|<=C'(1+|y|)^(1-1/c). The first conclusion needs neither the blow-down premise nor c>1/3. No pressure-growth condition is imposed. The constants need not be uniform in omega or the profile.

For the second conclusion we use the following more general elementary fact: a bounded solenoidal C1 field U with |curl U(y)|<=K(1+|y|)^(-beta), 1<beta<3, and vanishing distributional blow-down equals its absolutely convergent Biot-Savart integral and satisfies |U(y)|<=C_beta K(1+|y|)^(1-beta).

## 2. Direct Dini transport

The field B is continuously differentiable with at most linear growth, so its flow exists for every finite positive and negative time. Since Jy dot y=0, along a nonzero trajectory its radius satisfies

    cr-M<=r'<=cr+M.

Choose R1>max(1,2M/c). The flow is strictly radially outward on and outside that sphere. Every exterior point has a finite backward crossing of it: before crossing the backward radius decreases at least exponentially, since r'>=cr/2 forward, and so cannot remain above R1 for all backward time. The first crossing is unique along the exterior segment. Parametrize that segment by gamma(s), 0<=s<=t, starting at radius R1 and ending at y. Then

    r'>=cr/2,    r(t)<=(R1+M/c)exp(ct).

Taking the curl of the equation gives B.grad Omega=DU Omega-Omega-omega J Omega. Skewness of J implies

    d_s |Omega(gamma(s))|<=(-1+m(r(s)))|Omega(gamma(s))|.

This holds where the norm is differentiable; the squared-norm equation and Gronwall justify the integrated inequality through zeros. A zero remains zero by uniqueness of the linear transport equation. Monotonicity of r gives

    integral_0^t m(r(s))ds <= (2/c) integral_(R1)^infinity m(r)dr/r=:D<infinity.

The Dini premise also ensures `m(r)<infinity for r>1`, since m is nonincreasing. Consequently

    |Omega(y)|<=exp(D-t) sup_(|z|=R1)|Omega(z)|
              <=exp(D)(R1+M/c)^(1/c) sup_(|z|=R1)|Omega(z)| |y|^(-1/c).

Compact regularity extends this bound to C(1+|y|)^(-1/c). This proves the first conclusion without an angular scattering expansion.

## 3. Harmonic recovery of the velocity

Assume the general fact's hypotheses, put Omega=curl U and N(x)=1/(4pi|x|), and define

    V(x)=(1/(4pi)) integral_R3 Omega(z) cross (x-z)/|x-z|^3 dz.

The integral converges absolutely. Local boundedness of Omega controls the integrable kernel singularity, and the far integral is bounded by a constant times integral_1^infinity r^(-beta)dr. Continuity follows by making the singular ball uniformly small and using dominated convergence on its complement.

For R=|x|>=2, split into |z|<=R/2, |x-z|<=R/2, the remaining part of |z|<=2R, and |z|>2R. The respective bounds are C K R^-2 R^(3-beta), C K R^-beta R, C K R^-2 R^-beta R^3, and C K integral_(2R)^infinity r^-beta dr. Each is at most C_beta K R^(1-beta). Here beta<3 controls the first region and beta>1 controls the last. For bounded x the same integral estimates give a uniform bound. Thus V is bounded and decays uniformly as claimed.

The sign of the displayed kernel is that of curl(N*Omega). The undifferentiated Newton integral need not converge and is not used. Instead, test the absolutely convergent kernel integral against a compactly supported -Delta phi and use -Delta N=delta0 to obtain -Delta V=curl Omega in distributions. Fubini is justified by local integrability and the far bound C(1+|z|)^(-2)|Omega(z)|, integrable since beta>1. Since div U=0, also -Delta U=curl Omega. Hence U-V is an entire bounded distributionally harmonic field, so Weyl's lemma and the bounded harmonic Liouville theorem make it a constant vector h.

For every compactly supported test phi, V(Rz) tends to zero for z!=0 and is uniformly bounded, so its distributional blow-down vanishes by dominated convergence. The same premise for U forces h=0. Therefore U=V. Taking beta=1/c in the first conclusion proves the second exactly when 1/3<c<1.

## 4. Dependencies and scope

The short submitted checks are direct transport and harmonic recovery. The complete existing A addendum and C comparison agree after independent checking. The new arrangement states the same hypotheses and arguments together. It relies only on the displayed transport estimates, the elementary potential calculation and bounded harmonic Liouville, not on numerical or formal verification.

These are the same two pointwise bounds used in the final physical-annulus Holder step of A477. This proof does not itself estimate DU, construct the scattering map or classify physical singular sets. In particular it does not infer the Dini premise from bounded or decaying velocity and does not prove profile nonexistence. The statement that a constant-rate estimate with an arbitrary small exponent loss cannot be upgraded merely by sending that loss to zero remains a statement about that estimate; it is not a nonimplication theorem for the full profile equation.
