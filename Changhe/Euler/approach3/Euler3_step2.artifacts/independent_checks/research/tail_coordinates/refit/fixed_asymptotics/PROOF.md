# A finite refit retains the target representation's leading exponent

## Statement and hypotheses

Let H = L²(S²; R³) with surface area measure, and let Q(t):H->H, t in R, be a group of linear isometries representing axial rotation of a vector field. Fix a reference radius R0>0, and write rho=r/R0. For i in {s,t}, fix real numbers alpha_i and kappa_i, a nonzero F_i in H, and functions e_i(rho) in H with ||e_i(rho)||_H -> 0 as rho -> infinity. Assume that the source and target fields on spheres satisfy

    U_i(R0 rho, .) = rho^(-alpha_i) [Q(kappa_i log rho) F_i + e_i(rho)].

Then

    rho^(alpha_i) ||U_i(R0 rho, .)||_H -> ||F_i||_H > 0.

In particular, the logarithmic decay exponent is fixed:

    log ||U_i(R0 rho, .)||_H / log rho -> -alpha_i.

If alpha_s>alpha_t, then

    ||U_t(R0 rho, .)||_H / ||U_s(R0 rho, .)||_H
      = rho^(alpha_s-alpha_t) [||F_t||_H / ||F_s||_H + o(1)] -> infinity,

and

    ||U_t(R0 rho, .)-U_s(R0 rho, .)||_H / ||U_s(R0 rho, .)||_H -> infinity.

A fit on finitely many radii cannot change any of these conclusions while their hypotheses hold. In particular, fitting coefficients in a fixed target representation does not import the source's asymptotic decay exponent.

## Proof

The reverse triangle inequality and the isometry of Q give

    | ||Q(kappa_i log rho)F_i + e_i(rho)||_H - ||F_i||_H |
      <= ||e_i(rho)||_H -> 0.

Multiplication by the radial power proves the first limit. The norm in brackets is eventually positive and its logarithm tends to the finite number log ||F_i||_H. Dividing the identity for the logarithm of the norm by log rho proves the exponent formula. Taking the quotient of the two norm asymptotics gives the displayed norm ratio. Its leading constant is positive, so the ratio diverges when alpha_s>alpha_t. Finally, the reverse triangle inequality gives

    ||U_t-U_s||_H / ||U_s||_H >= ||U_t||_H / ||U_s||_H - 1,

which also tends to infinity. Finite-radius fitting enters none of these steps and cannot override the hypotheses.

## Why the fitted amplitude has no unconditional sign rule

Consider the restricted scalar-amplitude example with a fixed unit F in H, with no angular rotation. Let positive radii rho_1,...,rho_N and positive weights w_1,...,w_N be given. Fit a target a rho^(-alpha_t) F to a source rho^(-alpha_s) F by minimizing

    L(a) = sum_j w_j ||a rho_j^(-alpha_t)F - rho_j^(-alpha_s)F||_H².

The coefficient of a² is positive, so the unique minimizer is

    a_* = [sum_j w_j rho_j^(-alpha_t-alpha_s)]
          / [sum_j w_j rho_j^(-2 alpha_t)].

This follows by expanding the square and setting its linear derivative to zero. Equivalently a_* is a positive weighted average of rho_j^(-(alpha_s-alpha_t)), with weights proportional to w_j rho_j^(-2 alpha_t). If alpha_s>alpha_t and every rho_j>1, then 0<a_*<1. If every rho_j<1, then a_*>1. Thus the decay-exponent difference alone does not determine whether a fitted amplitude is above or below one; the sampled radii and weights matter even in this one-dimensional model. A general vector fit with phase differences and several channels needs its own analysis.

## Campaign application and scope

For the small-move control, the represented target pair is (c_l,omega)=(0.451,1.01); the source pair is (0.45,1). The exact exponents are alpha_s=11/9 and alpha_t=549/451, so

    alpha_s-alpha_t = 20/4059 > 0.

The fixed target representation and its tail constraints use alpha_t and kappa_t=1010/451. Changing finitely many allowed coefficients leaves these rates in the representation. When the target leading F is nonzero, the preceding norm conclusion applies, assuming the established finite-representation remainder. The measured target F_norm2 about0.934087 is a finite numerical observation, not an interval proof of nonvanishing. Even a tiny nonzero F would give the stated asymptotic exponent; a vanishing F would instead require examination of the next term.

A fitted field can approximate the source on the finite fitting domain and transition to its own target asymptotic law only at much larger radii. Large cancellation coefficients can delay that transition. Neither the transition radius nor a uniform remainder bound is determined here. The fit's poor nonlinear residual and gauge cost are measured separately; their cause is not established by this exponent calculation.

Dependencies: elementary Hilbert-space norm inequalities, positive weighted least squares, and the stated representation expansion. For the campaign's expansion, read research/represented_tail_decay/PROOF.md and research/finite_tail_integrability/PROOF.md. No theorem-prover verification or global numerical error enclosure is claimed.
