# Independent first residual mode in polar variables

## Statement and hypotheses

Let chi be a finite rational combination of the campaign's smooth single-scale potential generators, at a fixed rational c>1. Put delta=1-1/c, t=r^2/(1+r^2), u=1-t and a_j=(j+1)delta/2. Define rho=-partial_y Delta chi and the stream function psi=partial_x partial_y chi, so U=(-partial_y psi,partial_x psi). The independently derived polar representation is

    rho=r sum_(j,n) u^a_j R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,m) u^a_j S_(j,m)(t) sin(m theta),

where n is positive odd, m is positive even, and all polynomials have rational coefficients. The formulas and exact generator conversion are proved in ../weak_probe_audit/PROOF.md and its cited dependencies. Only smooth generators for which that representation is valid are considered here; a generator with an additional scale R!=1 is outside this representation.

For any polynomial P set

    T_(a,k)P=(k-2at)P+2t(1-t)P'.

The first sine coefficient of F=(cX+U).grad rho-rho is

    F_1(r)=r sum_ell u^(ell delta/2) Q_ell(t),

where the following finite sums give every Q exactly. A density term at n=1 contributes

    Q_(j+1) += c T_(a_j,1)R_(j,1)-R_(j,1).              (1)

Every stream-density pair (j,m),(i,n) with |n-m|=1 contributes

    Q_(i+j+2) += -sign(n-m)/2
      [m S_(j,m) T_(a_i,1)R_(i,n)
       +n R_(i,n) T_(a_j,2)S_(j,m)].                   (2)

There are no other contributions. Thus these formulas must agree coefficient by coefficient with N4's Cartesian-product projection when both are applied to the same exact potential.

## Proof

The identities r partial_r t=2t(1-t) and r partial_r u=-2tu imply

    r partial_r[r^k u^a P(t)]=r^k u^a T_(a,k)P.

This proves (1). A stream term gives the polar velocity components

    U_r=-r u^a m S cos(m theta),
    U_theta=r u^a T_(a,2)S sin(m theta).

A density term has radial derivative u^a T_(a,1)R sin(n theta) and angular derivative divided by r equal to u^a nR cos(n theta). Their scalar product is the sum of the two resulting products. Since m is positive even and n is positive odd, m+n>=3. The product cos(m theta)sin(n theta) has first sine coefficient sign(n-m)/2 exactly when |n-m|=1. The product sin(m theta)cos(n theta) has its negative. Multiplying the radial factors yields r u^(a_i+a_j), and a_i+a_j=(i+j+2)delta/2. This proves (2) and exhausts all terms. No estimate or angular truncation is used.

The Cartesian formulation starts instead with U1 rho_x+U2 rho_y, so its angular products include zero cosine modes and require exact cancellation of apparent radial denominators. Both constructions calculate the same smooth scalar expression. Equality of our branch polynomials is a stronger implementation check than point sampling, even where two different branches could have algebraic dependencies for a special delta.

## Verification and scope

The checker reconstructs rho and psi from the copied exact canonical potential, never reading N4's field arrays. It forms (1) and (2) with exact rational polynomials, then reads the frozen N4 first-mode certificate and compares the entire coefficient dictionary. All input and result hashes are recorded. The comparison validates that certificate's first mode only; it establishes no bound on the other residual modes, global norms, inverse operators or candidate existence.
