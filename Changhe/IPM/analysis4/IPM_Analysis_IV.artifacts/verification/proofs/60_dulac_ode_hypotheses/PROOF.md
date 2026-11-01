# Why the scalar Dulac ODE theorem does not directly settle full IPM

Status: CONFIRMED hypothesis audit. This rules out a direct application of one theorem, not convergence of the IPM logarithmic series and not every possible adaptation of the method.

## Statement

In the full angular IPM generating system, the stream indicial family has positive real roots tending to infinity with angular frequency. Consequently no finite shift of the radial series order moves all these roots out of the open right half-plane. The finite-dimensional indicial reduction used in the scalar algebraic ODE Dulac theorem cited below therefore does not apply uniformly to this full system.

Every fixed angular band has only finitely many such roots. The independently confirmed projected convergence theorem in topic55 explains why the fixed-band case behaves differently. It does not justify passing to the unrestricted band.

## The source theorem and the relevant proof step

Reference: Irina Goryuchkina and Renat Gontsov, *On the convergence of formal Dulac series satisfying an algebraic ODE*, arXiv:1712.08044v1, 21 December2017. The arXiv record lists the journal publication as Sb. Math.210(9),2019,1207-1221.

Theorem1 concerns one scalar polynomial ODE in x, y and finitely many Euler derivatives. Along its formal solution, the derivative with respect to each dependent-variable slot has a common lowest valuation and a constant coefficient there; the highest-derivative coefficient is nonzero. It proves sectorial convergence of the Dulac series. In Lemma1 a finite initial segment is removed so that the shifted indicial polynomial has no zero in the open right half-plane. Lemma3 then controls its polynomial-in-log inverse by scaling the nilpotent differentiation matrix relative to the series order.

Only these hypotheses and proof steps are used in this audit. The IPM calculation below is independent.

## Exact IPM indicial calculation

Let delta in (0,1), gamma=1-delta, z=r^(-delta), and E=z partial_z. Write the generated stream as

    psi = r^(1+gamma) G(z,theta).

Since r partial_r acts on this expression as 1+gamma-delta E, the angular-radial factor of the Poisson operator is

    L(E,partial_theta)
       = -(partial_theta)^2-(2-delta-delta E)^2.               (1)

This follows from Delta=r^(-2)((r partial_r)^2+partial_theta^2). It holds equally when the coefficients contain log z: the Euler derivative acts on both the power and its logarithmic coefficient.

On the S1 stream harmonic sin(2j theta), j>=1, (1) becomes the scalar quadratic

    L_j(lambda) = (2j)^2-(2-delta-delta lambda)^2.

Its roots are

    lambda_j^+ = (2j+2)/delta-1,
    lambda_j^- = (2-2j)/delta-1.                             (2)

For any fixed integer ell>=0, replacing G by z^ell times a tail changes E to E+ell. The roots therefore change to lambda_j^+ minus ell and lambda_j^- minus ell. Since lambda_j^+ tends to positive infinity, infinitely many shifted roots remain in the open right half-plane for every finite ell.

In particular, for j satisfying 2j+2>delta(ell+1), the shifted positive root is strictly positive. This proves the statement without any numerical estimate or assumption on arithmetic properties of delta.

## Relation to resonances and harmonic multipoles

The coefficient at stationary order n has z power n-1. Substituting lambda=n-1 in L_j gives

    L_j(n-1) = 4j^2-(2-n delta)^2.

Its zero condition is exactly n delta=2(j+1), the already derived stream resonance condition. Thus the unbounded indicial family is the same family responsible for high-order resonances, rather than an unrelated auxiliary operator.

The homogeneous radial branch z^(lambda_j^+) contributes

    r^(1+gamma) z^(lambda_j^+)
       = r^(2-delta-delta lambda_j^+) = r^(-2j).

These are the exterior harmonic stream multipoles. Their existence does not itself prevent convergence. It explains why a finite scalar indicial polynomial is not a faithful replacement for the full angular operator.

Angular coupling also prevents treating theta as an independent passive parameter in a scalar ODE: (1) contains theta derivatives, and the stationary equation couples angular derivatives and products. Fourier expansion gives an infinite coupled system. A fixed finite Fourier projection produces a finite system, but its constants can depend on the cutoff.

## What would be needed for an extension

A proof for the unrestricted rational logarithmic series would need a uniform estimate for this family together with the angular nonlinear convolution, or a different reduction whose hypotheses are actually established. Scalar Dulac convergence alone supplies neither estimate.

Topic28 gives a concrete complementary warning: a geometric bound for the plain density coefficient norm does not control the polynomial-log Poisson inverse in the growing near-resonant band. Topic55 proves convergence after fixing the angular band; its constant includes a finite maximum over the exceptional orders, which is allowed to deteriorate with bandwidth.

This audit makes no assertion that the published scalar theorem is false, that its methods cannot be extended, or that the rational IPM logarithmic series diverges. The full convergence question remains open in this campaign.

## Dependencies and evidence

The proof uses only the polar Laplacian, the exact weighted stream ansatz, and the elementary roots of a quadratic polynomial. The primary source was inspected directly at its exact arXiv version. Source identification and the real inspection time are retained in sources/source_record.json.
