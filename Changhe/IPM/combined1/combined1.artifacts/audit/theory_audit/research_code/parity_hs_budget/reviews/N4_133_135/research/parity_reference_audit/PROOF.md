# Radial commutator compressions for d2, candidate 005 and candidate 007

## Statement, hypotheses and notation

The exact references are d2, C1-N1-005-d2w-j7-x3 and
C1-N1-007-d2w-j7-e2bal. Their canonical rational potential and independently
confirmed background derivative energies are identified by hashes in
each verification record. Each density rho is smooth, even in x, odd in y,
and has the differentiated sublinear tails required by the audited
Hilbert-Schmidt commutator identity.

Put a=rho_x, b=rho_y, R_j=partial_j(-Delta)^(-1/2), and

    K = [R1,[R1,b]]/2 - [R1,[R2,a]]/2,
    kappa^2 = ((log 2-1/2)||Da||_2^2
                        +(3 log 2-2)||Db||_2^2)/(16 pi).

For n=0,...,11 let f_n be the nth derivative in z of
(z^2+r^2)^(-1/2), evaluated at z=1, and let h_n=-Delta f_n.
Let G_ij=<h_j,h_i> and B_ij=<K h_j,h_i>. For each nested dimension
d in {1,2,4,8,12}, define T_d=tr((G_d^-1 B_d)^2). Then

    0 <= T_d <= kappa^2,
    ||K restricted to S1||_op <= sqrt(kappa^2-T_d).        (1)

All values in the computation are full-plane values. A theta allowance
c-1-sqrt(kappa^2-T_d) is only an allowance: no full-plane theta bound is
asserted by this calculation. The conditional low-generator use is the
one independently reviewed in R1-016. No high inverse, admissible
nonlinear radius or existence theorem follows from (1).

## Proof of the inequality and exact matrix formulas

The double commutators are self-adjoint. Expanding their terms and
checking reflection signs shows that K commutes with both coordinate
reflections. Its four parity subspaces reduce it. All h_n are even-even,
so their span is orthogonal to the even-odd target S1. In an orthonormal
basis adapted to these subspaces, the squared entries of the finite
compression and of the S1 block are disjoint parts of the full
Hilbert-Schmidt sum. Thus their squared Hilbert-Schmidt norms add to at
most kappa^2, and the operator norm on S1 is at most its Hilbert-Schmidt
norm. The compressed squared norm is tr((G^-1 B)^2): conjugate to the
orthonormal matrix G^-1/2 B G^-1/2 and use cyclicity of trace. This proves
(1) once the following exact G and B are identified.

The nonunitary Fourier transform of f_n is
2 pi (-|xi|)^n exp(-|xi|)/|xi|. After applying -Delta, Plancherel and polar
integration give

    G_ij/pi = (-1)^(i+j) (i+j+3)! / 2^(i+j+3).

These Fourier functions are a nonzero radial factor times distinct
monomials, so they are independent and G is positive definite.

Write t=r^2 and primes for derivatives in t. The Poisson relation
(-Delta)^(1/2)f_n=-f_(n+1) and the velocity symbols give

    R_j h_n = -partial_j f_(n+1),
    U1[h_n] = -partial_xy f_n,  U2[h_n] = partial_xx f_n.

Set H_i=-4(f_i'+t f_i''),

    A_ij = -2(H_i f_j''+H_j f_i'')-4 f_(i+1)' f_(j+1)',
    D_ij = H_i f_j'+H_j f_i'.

Expansion of the symmetric velocity-gradient pairing minus its signed
principal part gives

    B_ij = integral [a xy A_ij + b(D_ij-x^2 A_ij)] dX.

Only the sin(2 theta) coefficient a2 of a and the constant and
cos(2 theta) coefficients b0,b2 of b survive angular integration.
Consequently

    B_ij/pi = integral_0^infinity
             [t A_ij(a2-b2-2b0)/4 + D_ij b0] dt.           (2)

The independent Cartesian potential differentiation constructs a2,b0,b2.
Each term is (1+t)^(-alpha) P(t/(1+t)), with rational alpha and rational
polynomial P. Each f_n is the exact finite Legendre formula

    f_n(t)=(-1)^n n! (1+t)^(-(n+1)/2)
                          P_n((1+t)^(-1/2)).

Thus (2) reduces to rational linear combinations of
Beta(l+2,k+alpha-2) and Beta(l+1,k+alpha-1). The code checks every second
parameter positive. For positive integer m and positive rational q,
Beta(m,q)=(m-1)!/[q(q+1)...(q+m-1)], so all these entries are exact
rational numbers. This uses the gradient directly; the independent
peer construction integrates by parts against rho.

Finally exact inversion of the rational Gram matrix gives T_d. Every
matrix entry, all Gram LDL pivots, and the exact captured energies are
compared with the frozen peer records. The already confirmed background
energies supply kappa^2, and outward ball arithmetic encloses its
logarithms, square roots and allowances. Therefore these checks are
independent reproductions of (1) for the three named exact references.

## Dependencies and evidence

The proof uses the audited gradient-commutator identity, the Poisson
Fourier identity, Cartesian differentiation and elementary beta
integration. R1-016 reviews the parity reduction and conditional
low-generator extension. The original independent radial audit is
../parity_budget_audit/PROOF.md. Each new record contains its candidate
identity and every source/proof/code hash, all exact matrices and the
scalar comparisons. Passing one candidate does not certify another.
