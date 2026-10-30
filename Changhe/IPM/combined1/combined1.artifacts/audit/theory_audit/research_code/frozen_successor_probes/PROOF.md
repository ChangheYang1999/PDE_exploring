# Independent frozen-probe checks for successor candidates

Status: arithmetic is recorded separately for each candidate and probe. The weak-test theorem is already audited (T4-172, T4-185); this file fixes its precise use and the independent computation.

## Statement and hypotheses

Let c>1, gamma=1/c<1, and let rho be one of the exact smooth canonical candidates named by a data hash. Its canonical velocity u is divergence free and rho,u=O(r^gamma) with differentiated bounds. Put F=(cX+u).grad rho-rho. Suppose real h belongs to L2(R2), its canonical velocity satisfies ||U[h]||2<=||h||2, and rho+h solves the fixed-c profile equation in distributions. For odd n>0 and rational polynomial P divisible by t^((n-1)/2), put

    t=r^2/(1+r^2), W=1-t, phi=r W^2 P(t) sin(n theta),
    Mfield=(2c+1)phi+(cX+u).grad phi,
    I=int F phi, M=||Mfield||2, C=||phi grad rho||2,
    H>=||grad phi||infinity, D=M+C.

Every such correction obeys

    ||h||2 >= 2|I|/(D+sqrt(D^2+4H|I|)).

If F+Lh=0 alone holds, where Lh=(cX+u).grad h-h+U[h].grad rho, then ||h||2>=|I|/D when D>0. A positive computed lower bound is a necessary distance, not an existence certificate.

## Complete weak argument

Divisibility of P makes phi smooth at zero: each monomial is Im(x+iy)^n times a nonnegative integer power of r^2 divided by a positive power of 1+r^2. At infinity phi=O(r^-3) and grad phi=O(r^-4). Thus Mfield and phi grad rho are square integrable, F phi is integrable, and grad phi is bounded. Test the distributional equation with phi times a smooth radial cutoff. The linear terms converge by Cauchy-Schwarz; the quadratic product U[h]h is integrable. The cutoff-gradient errors vanish: its linear coefficient is bounded by a decaying multiple of the L2 tail of h and its quadratic coefficient is bounded by a decaying multiple of the L1 tail of U[h]h. Letting the cutoff radius increase gives

    0=I-int h Mfield+int U[h].grad rho phi-int U[h]h.grad phi.

Absolute values and Cauchy-Schwarz yield |I|<=D||h||2+H||h||2^2. The right side is increasing for nonnegative norm, proving the quadratic root. Omitting the last term proves the linearized bound.

## Independent polar arithmetic

The copied canonical data are reconstructed with our previously audited polar helper, which is independent of N4's Cartesian differentiation and product assembly. Write

    rho=r sum_(j,m) W^alpha_j R_jm(t) sin(m theta),
    psi=r^2 sum_(j,m) W^alpha_j S_jm(t) sin(m theta),
    alpha_j=(j+1)(1-1/c)/2,
    D_b A=b A+2tW A'-2alpha_j t A.

Then u_r=-r sum m W^alpha_j S_jm cos(m theta), u_theta=r sum W^alpha_j D_2 S_jm sin(m theta), and grad rho has radial coefficient D_1 R_jm and angular coefficient m R_jm. Set Q=(1-4t)P+2tW P'. The linear M coefficient is (2c+1)P+cQ. Its velocity products are assembled using the exact sum and difference sine identities, preserving their signs. Their squared norm uses angular orthogonality and includes every radial cross term.

For C squared, the angular coefficients, in units pi/4, are

    2[n=m]-[|n-m|=2ell]+[n+m=2ell]  (sine-sine),
    2[n=m]-[|n-m|=2ell]-[n+m=2ell]  (cosine-cosine),

where ell is the probe mode. These follow by expanding sin(ell theta)^2=(1-cos(2ell theta))/2 and applying product-to-sum. Multiplication by P^2 and the radial factors gives the complete C norm, with no angular truncation.

The pairing is computed directly from c r partial_r rho-rho+u.grad rho, retaining the exact matching sum and difference frequencies. No integration-by-parts pairing from N4 is used. The change of variables r dr=dt/(2W^2) reduces every radial term to a rational polynomial times t W^b, b>-1. Expand the polynomial in W and evaluate each moment

    int_0^1 t W^(b+j) dt=1/((b+j+1)(b+j+2)).

All coefficients remain rational until outward Arb summation. Positivity and overlap with the independently generated N4 intervals are checked. H is independently proved by dyadic interval subdivision and the polynomial mean-value bound on W^2 max(|Q|,ell|P|). The final rational floor lies strictly below the lower endpoint of the resulting radius interval.

## Dependencies and scope

Dependencies: the exact canonical representations previously audited for each named candidate; the polar derivative helper in localized_probe_audit; the audited L2 velocity multiplier bound including its local part; T4-172 and T4-185. There is no quadrature, finite-radius truncation, optimization, inverse estimate, or change of similarity exponent in this check. The separately audited tail-pinning theorem may transfer the conclusion to any c in the same affine correction class when its hypotheses are met. Every source, probe, helper and output is hashed. Each arithmetic conclusion is accepted only for its own recorded candidate and probe.
