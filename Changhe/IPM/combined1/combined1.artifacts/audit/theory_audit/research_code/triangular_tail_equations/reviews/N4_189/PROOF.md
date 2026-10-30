# Independent Cartesian verification of the nonintegrable tail recurrence

## Statement and scope

Fix the exact rational candidate C1-N1-007-d2w-j7-e2bal, whose canonical
potential source has SHA256
153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Write c for its exact cl, gamma=1/c, delta=1-gamma, and
e_j=gamma-j delta. This candidate satisfies1/2<gamma<3/5, so
e_0,e_1,e_2,e_3>-1 and e_4<-1.

For j=0,1,2,3 let Theta_j be its full leading density sine profile at
radial exponent e_j and Psi_j its stream profile at exponent e_j+1.
The exact arithmetic certificate below establishes

    [d_theta^2+(e_j+1)^2] Psi_j
        =-e_j cos(theta) Theta_j+sin(theta) Theta_j',       (1)

and, for j=1,2,3,

    j(c-1) Theta_j
       =sum_(l+m=j-1) [-e_m Psi_l' Theta_m
                             +(e_l+1) Psi_l Theta_m'].    (2)

All angular coefficients are included. The three residual profiles in
(2) have20,30,40 potentially nonzero positive sine frequencies,
respectively. The computation checks all90 of them exactly. It also
compares every coefficient of Theta_j and Psi_j with the independently
computed peer profiles, not only the first density harmonic.

This is a statement about a specified finite rational potential. The
separate theorem that (2) is forced by the distributional equation in a
particular asymptotic chart is T4-234 and requires its own hypotheses
and theory review. No inverse, solution, smallness condition or complete
nonlinear tail chart follows from this algebraic certificate.

## Extracting the tails from complete Cartesian derivatives

Let t=r^2/(1+r^2). In each branch the canonical potential has the form

    chi_j=(1+r^2)^p_j sum_n P_(j,n)(t) cos(n theta),
    2p_j=3+gamma-j delta.

Our previously audited Cartesian recurrence represents every derivative
of total order d as

    (1+r^2)^p_j r^(-d)
        sum_n A_(j,n,d)(t) trig_n(theta).                 (3)

It was obtained by differentiating this expression with respect to x
and y, including derivatives of r and theta; the complete derivation
and independent point tests are in ../radial_fourier/PROOF.md. Since
t tends to1 and (1+r^2)^p_j/r^(2p_j) tends to1, the coefficient of the
leading power r^(2p_j-d) is exactly A_(j,n,d)(1). The omitted terms
are lower by even integer powers of r. In particular this applies to

    rho=-chi_xxy-chi_yyy, psi=chi_xy,
    u1=-chi_xyy, u2=chi_xxy, rho_x, rho_y.

Thus evaluating the full derivative polynomials at1 supplies Theta_j,
Psi_j, both Cartesian velocity profiles, and both density gradient
profiles without using the peer's homogeneous-potential differentiation
formulas. The profile exponents are e_j,e_j+1,e_j,e_j,e_j-1,e_j-1.

## Exact Laurent polynomial checks

Represent a real trigonometric polynomial as a finite Laurent polynomial
in z=exp(i theta) over Q[i]. Encode cosine n by(z^n+z^(-n))/2 and sine n
by(z^n-z^(-n))/(2i). Complex coefficients are stored as pairs of rational
real and imaginary parts. Products are ordinary convolution. Angular
differentiation multiplies the coefficient of z^n by i n. Equality of
Laurent polynomials is therefore exact coefficientwise equality, and
is equivalent to equality of the trigonometric functions.

For each branch recover the polar velocity from the Cartesian one:

    U_r=cos(theta) U1+sin(theta) U2,
    U_theta=-sin(theta) U1+cos(theta) U2.

The verifier checks U_r=-Psi_j' and U_theta=(e_j+1)Psi_j. It also checks
(1), using Laurent multiplication by cos and sin and differentiation,
against the full endpoint fields. These identities independently test
signs, parity and the density-stream convention.

The Cartesian product

    B_j=sum_(l+m=j-1) (U1_l (rho_x)_m+U2_l (rho_y)_m)

has radial exponent e_l+e_m-1=e_j. Computing it by Laurent convolution
gives a direct coefficient map. Separately, using the verified polar
velocity and rho_m=r^(e_m)Theta_m gives the right side of (2). The
verifier requires these two maps to coincide. The dilation term in the
stationary residual contributes

    (c e_j-1)Theta_j=-j(c-1)Theta_j.

Consequently (2) is precisely B_j-j(c-1)Theta_j=0. Every rational
coefficient must be zero; no tolerance, sampling, projection truncation
or numerical quadrature is used.

## Source binding and evidence

Before execution, freeze the peer proof, code, result and full exact
profiles. Check their hashes against the result, and bind the canonical
input to both the own earlier candidate audit and the peer record.
Store all independently extracted density and stream maps, velocities,
recurrence counts, full equality flags, dependency hashes and real runtime
in clearly named verification files. The independent implementation
executes only local own code. Exact zero replay verifies the numerical
claim T4-235, while the informal argument above explains why these finite
checks imply the stated identities.
