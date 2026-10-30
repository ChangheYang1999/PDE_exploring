# Combining overlapping commutator compressions without double counting

## Statement

Let K be a self-adjoint Hilbert-Schmidt operator on a Hilbert space. Let P and Q be finite-rank orthogonal projections that commute, and put R=PQ. Then

    ||PKP||HS^2+||QKQ||HS^2-||RKR||HS^2 <= ||K||HS^2.    (1)

If both ranges lie in a reducing space orthogonal to a target space H, their union energy can be subtracted from the full Hilbert-Schmidt budget when bounding K on H. Independent compressions in other orthogonal reducing spaces can be added as in the parity proof.

## Proof

Commutativity gives the orthogonal decomposition

    ran(P+Q-PQ)=ran R + ran(P-R) + ran(Q-R).

Choose orthonormal bases in those three spaces and in their joint orthogonal complement. The first term on the left of(1) sums squared matrix entries whose two indices lie in R or P-R. The second does the same for R or Q-R. Their only common entries have both indices in R, exactly the third term. Thus the left side is a sum of distinct nonnegative squared matrix entries of K. The entries between P-R and Q-R, and all entries involving the joint complement, are not counted. This proves(1). This argument also proves that the left side is nonnegative. No orthogonality of the originally supplied test functions is required, because each compression is evaluated using its Gram matrix.

Commutativity is an essential stated hypothesis. Subtracting a guessed overlap between arbitrary noncommuting test spans would not follow from this proof.

## Application to the completed Poisson data

Use the exact test family from the parity-budget proofs. Let P be the even-even span consisting of radial indices0 through N-1 in each cosine harmonic0,2,...,M, with M even. Let Q be the radial harmonic0 span with indices0 through d-1, where d>=N. Different angular harmonics are orthogonal in L2. The radial span of P is contained in Q, and every nonradial harmonic in P is orthogonal to Q. Therefore P and Q commute; R is precisely the radial span with indices0 through N-1.

Suppose T_ang includes all three complementary parity compressions with radial size N and maximum angular degree M. Let T_rad(d) and T_rad(N) be the independently computed radial compression energies. Then the combined complementary energy is

    T_union=T_ang+T_rad(d)-T_rad(N),                     (2)

and the target S1 absolute operator norm is at most

    sqrt(kappa2-T_union).

This uses only completed matrices and exact overlap data. It does not require any matrix entries between the additional radial tests and the nonradial tests, because those entries were omitted as nonnegative terms in the proof. It does not identify the exact Hilbert-Schmidt norm of the union compression.

The signed S1 theorem can then use the same T_union as its complementary energy, giving the quadratic-form bound

    sqrt(kappa2-T_union-T_H+q^2)

under that theorem's independent hypotheses.

## Data and scope

Every combined record must refer to the same exact canonical candidate and the same K convention. The code checks these identities, requires d>=N and verifies the common radial block entries against the angular matrix. All overlap energies are exact rational numbers. The full kappa2 and final square root are evaluated outward. This is a new algebraic compression lemma awaiting independent theory review. It supplies no theta cover, high inverse or nonlinear closure by itself.
