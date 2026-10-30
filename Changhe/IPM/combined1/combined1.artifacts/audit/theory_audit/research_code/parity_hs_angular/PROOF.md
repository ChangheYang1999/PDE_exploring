# Finite angular blocks in the symmetry-resolved commutator budget

## Exact statement

Use the real smooth S1 background, its canonical Riesz operators and self-adjoint Hilbert-Schmidt operator K from ../parity_hs_budget/PROOF.md. Assume that proof's gradient approximation and full-plane coefficient hypotheses. Its known complete Hilbert-Schmidt energy is kappa^2. Let H_{++}, H_{-+}, H_{--}, H_{+-} denote the four coordinate parity spaces, with H_{+-} the target S1 space.

In each of the three other parity spaces choose a finite linearly independent real family h_i. Let G_p and B_p be its L2 Gram and K-compression matrices. Then

    ||K restricted to S1||op^2 <= kappa^2-T,
    T=sum_{p=++,-+,--} tr(G_p^-1 B_p G_p^-1 B_p).           (1)

In particular the right side is nonnegative. The low semigroup and inverse rate is at least c+1-theta-sqrt(kappa^2-T), if this is positive, under the same complete transport and maximal-domain assumptions as the radial proof. This supplies no high-space estimate or nonlinear closure on its own.

## Budget proof

K commutes with coordinate reflections: rho_x is odd in both coordinates, rho_y is even in both, and each R_j reverses the corresponding coordinate parity. Expand both double commutators to verify the assertion term by term. Therefore the four parity spaces reduce K orthogonally. In each parity block choose an orthonormal basis beginning with the selected finite span. The complete Hilbert-Schmidt sum contains all squared entries from each finite compression and every entry of the S1 block as disjoint nonnegative summands. The three finite sums are exactly the traces in(1), by the isometry S G_p^-1/2 from coefficient space. Dropping all remaining terms proves(1).

No assertion that a compression approximates the entire block is needed. Every additional independently certified energy contribution improves the upper bound. The finite Gram matrices must be positive definite, and their inverses and entries must be computed with exact or validated arithmetic. A sampled matrix is not a certificate.

## Poisson-derived angular families

Let g_z=(z^2+r^2)^(-1/2), and f_n=partial_z^n g_z at z=1. For m>=0 define C_m=Re(partial_x+i partial_y)^m and, for m>=1, S_m=Im(partial_x+i partial_y)^m. Use either operator D_m, and set

    f_{m,n}=D_m f_n, h_{m,n}=-Delta f_{m,n}.

The Poisson identity (-Delta)^(1/2)g_z=-partial_z g_z, proved in the radial dependency, gives

    U1[h]=-partial_xy f, U2[h]=partial_xx f,
    Rj[h]=-partial_j D_m f_{n+1}.                         (2)

All these are smooth rational functions of x,y and (1+r^2)^(1/2), with sufficient decay for every pairing below. The parity of C_m f_n is((-1)^m,+); that of S_m f_n is((-1)^(m+1),-). Thus all cosine families and the even sine families belong to the three complementary blocks. Odd sine families are deliberately not subtracted from the S1 budget.

The functions are linearly independent. Their Fourier transforms have a common nonzero radial factor |xi| exp(-|xi|), multiplied by a nonzero constant times |xi|^(m+n) cos(m angle) or sin(m angle). Different angular harmonics are orthogonal. Within one harmonic the distinct n give independent monomials. This proves positive definiteness of each Gram matrix.

## Pairing formula without half-order numerical differentiation

For any two tests i,j from one parity block, use the explicit rational functions h_i, U_i, v_i=(R1 h_i,R2 h_i) from(2). Define

    A_ij=(h_i U1_j+h_j U1_i-v1_i v2_j-v2_i v1_j)/2,
    B_ij=(h_i U2_j+h_j U2_i)/2+v1_i v1_j.

The signed decomposition gives

    <K h_j,h_i>=integral[rho_x A_ij+rho_y B_ij]
               =integral rho(-partial_x A_ij-partial_y B_ij). (3)

The last identity follows by integration by parts on expanding disks. Boundary terms tend to zero because the tests decay as rational derivatives of g_1 and rho grows sublinearly. No contact term is discarded: this is the ordinary L2 Riesz multiplier identity and the exact symmetric decomposition, rather than a pointwise strain calculation.

Represent each test kernel by finitely many monomials x^u y^v (1+r^2)^(-p), with rational coefficients and half-integer p. Differentiation and multiplication are exact in this representation. Products and the differentiated kernel in(3) have integer p.

## Exact moments

For a monomial x^u y^v (1+r^2)^(-p), define

    A_n(u,v)=pi^-1 integral_0^(2pi) cos(theta)^u sin(theta)^v sin(n theta) dtheta.

The sine expansion of(cos(theta)+i sin(theta))^n expresses A_n as a rational number. Each even power integral satisfies

    pi^-1 integral cos^(2a)(theta) sin^(2b)(theta) dtheta
      =2(2a)!(2b)!/[4^(a+b) a! b! (a+b)!],

and each integral with an odd exponent is zero. A nonzero density pairing has u+v odd. Put q=(u+v+1)/2. For the exact density expansion

    rho=r sum_{j,n}(1+r^2)^(-a_j)P_{j,n}(t)sin(n theta),
    t=r^2/(1+r^2), a_j=(j+1)(1-1/c)/2,

its contribution to(3), divided by pi, is

    (A_n(u,v)/2) sum_l P_{j,n,l}
        Beta(q+l+1,p+a_j-q-1).                            (4)

Every second beta parameter is checked positive before integration. Since the first parameter is a positive integer and the second is rational, (4) is exactly rational. Gram pairings use the same even angular formula and Beta((u+v)/2+1,p-(u+v)/2-1)/2. Terms whose angular integral vanishes contribute zero. All boundaries and all radii are included in these exact integrals.

The arithmetic checks Gram positivity by exact LDL, verifies that the constant-gradient background rho=y gives K=0 for every matrix entry, and compares the radial subblock with the independently assembled radial formula. These are internal algebra checks. An independent theory review and an independent numerical path remain required before a new candidate bound is called certified in the campaign.

## Scope and dependencies

The analytic inputs are the independently audited signed decomposition and full-plane gradient-commutator identity, elementary coordinate parity, the proved Poisson family identity and explicit beta moments. The theorem is new and remains OPEN pending T1/T2 review. Numerical applications have their own hashes, precision, timings and status. Improving this sufficient low bound does not undo any independently proved residual-distance obstruction for a candidate.
