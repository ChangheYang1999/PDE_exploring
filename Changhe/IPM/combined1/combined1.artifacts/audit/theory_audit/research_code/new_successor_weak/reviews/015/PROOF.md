# Independent structure acceptance for candidate015

The exact potential is the rational generator file with SHA256
d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae.
Both lanes expand it as a finite sum of the ordinary potential monomials
specified in ../../PROOF.md. This result concerns that exact smooth S1
reference and its canonical sublinear velocity, at
c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma.

The claim is that the independent canonical coefficient maps coincide,
the origin strain is exactly1-c, the density slope is positive, and the
first four density and stream profiles equal those of007. The last part
has both this lane's direct computation and the following independent
consequence of N4's sector check.

Write e_j=gamma-j delta. For j=0,1,2,3, each density profile Theta_j
uniquely determines its even-sine stream profile Psi_j through

    (partial_theta^2+(e_j+1)^2)Psi_j
        =-e_j cos(theta)Theta_j+sin(theta)Theta_j'.

The eigenvalues on sin(2m theta), m>=1, are nonzero because
0<e_j+1<2. For j=1,2,3 the exact residual coefficient is

    E_j=-j(c-1)Theta_j
        +sum_(l+m=j-1)[-e_m Psi_l' Theta_m
                           +(e_l+1)Psi_l Theta_m'].

This follows by multiplying the homogeneous velocity and density
profiles and applying c r partial_r-1. Every term in the sum uses
strictly lower indices. Therefore, once c and Theta0 are fixed, the
three equalities E_j=0 determine Theta1, Theta2 and Theta3 successively
and uniquely. The stream profiles then agree by the nonresonant
angular equation. The detailed canonical-velocity and remainder
justifications are in the audited triangular_tail_equations/PROOF.md.

N4 independently verifies the common leading density and the exact
vanishing of sectors(h,q)=(1,0),(2,0),(3,0), in its h=j indexing.
Candidate007 already has the same leading profile and these zero
coefficients by the accepted T4-235/N4-189 calculation. The preceding
uniqueness argument therefore proves the four-profile agreement from
N4's inputs, independently of this lane's direct profile comparison.

The two canonical JSON byte hashes differ because their metadata differ.
The checker instead compares all1922 nonzero coefficients as rational
numbers indexed by(j,m,k), rejecting duplicate indices, and verifies c,
the exact origin strain, and the positive origin slope. This validates
the finite data identity; it does not prove any untested global
background bound, residual norm or closure condition.
