# The first profile derivative needed to cross a rational exponent

Status: PROVED finite regularization criterion. The derivative and approach checks are V294; the independent analytic review at11:52Z is recorded in V306.

## Statement

Let delta0=2/3, and let b0 be either exact real root of the sextic P6 in119. Consider a real analytic function b(delta) near delta0 with b(delta0)=b0. At nonresonant delta use the pure stationary recurrence with leading density

    f_1(delta,theta)=sin(theta)+b(delta)sin(3theta).

Let O_b=P6'(b0)/35818438656000000. Let H_lim and H_star denote the fixed-shape limiting and tuned order6 stream harmonics from151. Then O_b is nonzero. All density and stream coefficients through order9 extend analytically to delta0 if and only if

    b'(delta0)=12(H_star-H_lim)/O_b.                       (1)

In the parameter c=1/(1-delta), the required derivative is one ninth of(1). This is a statement about a finite prefix. It does not establish convergence of a parameter-dependent infinite series, or removal of every later resonance.

## Proof

Every coefficient before order6 is a rational function of delta and b, with nonzero relevant denominators near(delta0,b0). The first obstruction is analytic there and equals P6(b)/35818438656000000 when delta=delta0. Its derivative along the profile curve is therefore

    d a_(6,1)/d delta = partial_delta a_(6,1)+O_b b'(delta0).

The order6 resonant stream coefficient has a removable singularity because its numerator vanishes at(delta0,b0). The quotient rule for a simple vanishing denominator, derived in151, gives its limiting value

    H6_curve=H_lim+O_b b'(delta0)/12.                      (2)

All other order6 coefficients are analytic. Orders7 and8 have no stream resonance at delta0, so all their coefficients are analytic. The limiting order9 density obstruction equals

    sigma_2(H6_curve-H_star),

because the finite recurrence through the next obstruction is affine in the inserted order6 harmonic. The number sigma_2 is nonzero by119. The resonant order9 stream denominator has a simple zero; hence its quotient extends analytically exactly when this obstruction vanishes. Substitution of(2) gives(1).

There are finitely many other Fourier modes through order9. Their denominators are nonzero at delta0, so a sufficiently small common parameter neighborhood avoids all their zeros. The identically absent zero stream mode causes no singularity. Thus removing the single order9 obstruction removes all singularities of this finite prefix.

The polynomial P6 is irreducible over the rationals in characteristic zero, so it is square-free. Therefore P6'(b0) and O_b are nonzero, making(1) a unique finite slope. Finally d delta/d c=1/c^2=1/9 at c=3, giving the stated conversion.

## Verification and scope

The certificate evaluates O_b directly from the exact sextic and independently differentiates the Cartesian recurrence with respect to b. It compares those two intervals, then computes the slope from(1). A nonzero slope, together with151, explains why a fixed leading shape fails the finite continuity test. Higher profile derivatives and later resonances remain unrestricted here.

## Certified slopes and approach checks

The corrected1536-bit calculation gives b'(delta0)=-4.2923862068337210640192012046824808829176513166497398790128004208 for the smaller root and5.8016929269331980151098739057370619342687748788029280578244186394 for the larger root. The corresponding c derivatives are-0.47693180075930234045 and0.64463254743702200168. Full outward-rounded intervals appear in verification/checks.json.

For both roots the derivative O_b from the exact primitive polynomial overlaps an independent derivative of the Cartesian recurrence with respect to b. At delta=delta0 plus or minus2^(-p), p=30,60,100, direct nonresonant recurrence checks give |(delta-delta0)g_(9,4)-Res|<10000|delta-delta0| for the fixed shape. Along the linear profile with the certified slope, |g_(6,2)-H_star|<10000|delta-delta0| and |g_(9,4)|<100. These are twelve finite approach checks, not a substitute for the analytic proof.

The first derivative comparison failed because the saved Sturm polynomial is monic, whereas the obstruction uses the primitive sextic. Multiplying its derivative by the exact leading coefficient176703765525000 fixes the normalization. The failed check and correction are preserved; no theorem hypothesis changed.
