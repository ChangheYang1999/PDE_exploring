# Coordinate reflection symmetry leaves the whole-plane norms unchanged

## Statement

Fix 0<alpha<1 and signs chi_1,chi_2 in {-1,1}. Use the Euclidean
seminorm

    [f]_alpha = sup_{p != q} |f(p)-f(q)| / |p-q|^alpha

on real functions on R^2. Let X_chi be the class of functions satisfying

    f(-z_1,z_2)=chi_1 f(z_1,z_2),
    f(z_1,-z_2)=chi_2 f(z_1,z_2).

Let A be any one of T_xx, T_xy, R_1^2, with kernels, centered circular
principal values, and the homogeneous extension modulo constants from
../01_setup/PROOF.md. In particular R_1^2=T_xx-I/2. Then

    sup_{0 != f in C_c^infinity(R^2) intersect X_chi}
          [Af]_alpha/[f]_alpha
      = ||A||_{dot C^alpha(R^2) -> dot C^alpha(R^2)}.

The same equality holds if the restricted supremum is taken over all
finite-seminorm functions that have a representative in X_chi. Thus
restriction to functions odd in both variables, even in both variables,
or of either mixed coordinate parity does not improve the global
whole-plane constants: they remain C_alpha for T_xx and T_xy, and
D_alpha for R_1^2.

The output seminorm is taken over all pairs of points in R^2. There is
no bound on the support radius or on the location of the pair. The
statement makes no claim for a prescribed bounded domain, a fixed
increment near the origin, or additional size or support restrictions.

## Construction and exact seminorm bound

Take any nonzero real f in C_c^infinity(R^2), and any p != q. Choose R>0
such that the support of f, p, and q are contained in B(0,R). Write
M=[f]_alpha>0 and A_0=||f||_infinity. For L>R set a_L=(L,L).
For epsilon=(epsilon_1,epsilon_2) in {-1,1}^2 put

    Q_epsilon=diag(epsilon_1,epsilon_2),
    chi(epsilon)=chi_1^((1-epsilon_1)/2)
                 chi_2^((1-epsilon_2)/2),
    F_L(z)=sum_epsilon chi(epsilon) f(Q_epsilon z-a_L).

The four summands are supported in the disjoint balls
B(Q_epsilon a_L,R). Their mutual distances are at least 2L-2R.
The finite sum is smooth and compactly supported. Substitution and
reindexing give F_L(Q_delta z)=chi(delta)F_L(z), so F_L belongs to X_chi.

Choose L large enough that

    2 A_0 <= M (2L-2R)^alpha.                                (1)

Then [F_L]_alpha<=M. To check this for an arbitrary pair z,w, there are
four cases. If both lie in the same support ball, at most its one
summand is nonzero at either point, and its seminorm is M. If one lies
in a support ball and the other lies outside all four balls, the latter
value is zero; comparison with the same globally defined summand again
gives the bound M|z-w|^alpha. If the points lie in different balls,
|F_L(z)-F_L(w)|<=2A_0 and |z-w|>=2L-2R, so (1) applies. If neither lies
in a ball, both values are zero. These cases include points where the
summand itself vanishes and all boundary points.

## The other three copies have vanishing influence on the increment

The identity summand, epsilon=(1,1), is f(z-a_L). By translation
invariance its contribution to the output increment at a_L+p,a_L+q
is exactly Af(p)-Af(q).

For either K=K_xx or K_xy, direct differentiation in polar coordinates
gives

    |grad K(z)|=1/(pi |z|^3),       z != 0.                  (2)

Every point of the segment joining a_L+p to a_L+q lies in B(a_L,R).
Its distance from each of the other support balls is at least 2L-2R.
Those three convolution integrals are therefore ordinary smooth
integrals in a neighborhood of the segment; they require no principal
value. The mean value theorem, (2), and invariance of the L^1 norm under
reflections and translations give for each such summand g

    |Tg(a_L+p)-Tg(a_L+q)|
      <= |p-q| ||f||_1 / [pi (2L-2R)^3].                  (3)

For R_1^2 the same estimate holds: the extra local term -g/2 vanishes
at both evaluation points. Summing (3), for all three operators A,

    |AF_L(a_L+p)-AF_L(a_L+q) - (Af(p)-Af(q))|
      <= 3 |p-q| ||f||_1 / [pi (2L-2R)^3].              (4)

This estimate proves convergence for the actual principal-value
operator on the compact smooth test functions. There is no assertion
that the individual output values for a growing homogeneous input
have a canonical normalization.

## Equality of norms

Let N_chi denote the restricted compact-smooth supremum in the theorem.
The accepted whole-plane upper bounds imply N_chi is finite. By the
seminorm estimate and (4),

    |Af(p)-Af(q)|
      <= N_chi M |p-q|^alpha
         +3 |p-q| ||f||_1/[pi(2L-2R)^3].

Let L tend to infinity while f,p,q,R remain fixed. Divide by
M|p-q|^alpha, then take the supremum over p,q and over compact smooth f.
This proves that the unrestricted compact-smooth norm is at most N_chi.
The reverse inequality follows from inclusion of the test classes.
The setup and approximation proofs identify the unrestricted
compact-smooth supremum with the homogeneous-space operator norm.

Finally the restricted homogeneous supremum lies between its restricted
compact-smooth counterpart and the unrestricted homogeneous norm.
These endpoints are equal, proving the second assertion. In the
quotient by constants, the phrase "has a representative in X_chi"
avoids imposing a parity condition on an unspecified representative.

## Dependencies and scope

The proof uses only the setup and approximation theorems in
../01_setup/PROOF.md and ../02_upper_bounds/PROOF.md, the explicit kernel
gradients (2), and translations, reflections, and the mean value
theorem. It does not use rotation to identify restricted input spaces.
No numerical experiment, literature sharpness claim, or proof-assistant
build is needed.
