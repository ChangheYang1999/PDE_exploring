# Angular degree and exact sphere quadrature for residual norms

Status: proved conditional statement about exact finite formulas. No numerical error bound or Euler solution is asserted.

## Statement, spaces and notation

Let L_T,L_S,L_P be nonnegative integers. Let H_lm be real homogeneous harmonic polynomials of degree l on R^3. On the open set D=R^3\{0}, put q=|y|^2 and define finite scalar potentials

    T(y)=sum_(l<=L_T,m) f_lm(q) H_lm(y),
    S(y)=sum_(l<=L_S,m) g_lm(q) H_lm(y).

Assume f_lm belong to C^2((0,infinity)) and g_lm belong to C^3((0,infinity)). Define U=curl(Ty)+curl curl(Sy), A=DU with A_ij=partial_j U_i, and Omega=curl U. The derivatives and identities below are understood on D. Let a_lm belong to C^1((0,infinity)) and let the pressure have the finite angular representation

    P(r n)=sum_(l<=L_P,m) a_lm(r) H_lm(n),   r>0, n in S^2.

The coefficients can be complex if real parts are taken in a fixed consistent convention; the same degree bounds apply to real and imaginary parts. No Poisson equation for P is assumed. Let c,w be real constants and let J be the matrix with Jy=(-y_2,y_1,0). Set

    L=(1-c)U+c A y+w(JU-A Jy),
    N=A U+grad P,                R_u=L+N,
    L_Omega=Omega+c DOmega y+w(JOmega-DOmega Jy),
    N_Omega=DOmega U-A Omega,    R_Omega=L_Omega+N_Omega.

At each fixed r>0, the components of the indicated fields are restrictions of polynomials in n with the following degree bounds:

    u=max(L_T,L_S+1)                   for U,
    d=max(L_T+1,L_S+2)                 for A,
    v=max(L_S,L_T+1)                   for Omega,
    e=max(L_S+1,L_T+2)                 for DOmega,
    m=max(u,d+1,d+u,L_P+1)             for L,N,R_u,
    h=max(v,e+1,e+u,d+v)               for L_Omega,N_Omega,R_Omega.

These are upper bounds; vanishing modes and cancellations can lower the actual degrees. Let Q_(N_mu,N_phi) be Gauss-Legendre quadrature in mu=cos(theta) with N_mu nodes, tensorized with N_phi equally spaced azimuths with any common offset, using the exact nodes and weights. If

    2 N_mu-1 >= 2m,   N_phi > 2m,

then in exact arithmetic Q computes every sphere integral of X dot Y exactly when X and Y are chosen from L,N,R_u or any of their separately displayed summands. Consequently it computes their squared L2 norms and Gram matrix exactly. The same statement for L_Omega,N_Omega,R_Omega and their summands holds if

    2 N_mu-1 >= 2h,   N_phi > 2h.

For complex components the Hermitian product X dot conjugate(Y) has the same bound. Dividing the weights by 4pi gives the identical result for normalized sphere means. Subsequent finite radial weighted sums and ratios of these exact angular quantities introduce no angular quadrature error, provided their denominators are nonzero.

## Proof of the degree bounds

For a homogeneous harmonic polynomial H of degree l, elementary Cartesian differentiation gives

    curl(f(q)H(y)y)=f(q)(grad H cross y),
    curl curl(g(q)H(y)y)
      =((l+1)g(q)+2qg'(q)) grad H-2l g'(q)yH.

At fixed r these have angular degrees at most l and l+1, respectively. One Cartesian derivative of a polynomial times a radial coefficient either lowers the polynomial degree by one or differentiates the radial coefficient, introducing one factor y. The corresponding bounds for their derivatives are l+1 and l+2. Finite sums therefore give u and d.

The potential curl identity proved in ../vorticity_potentials/PROOF.md is

    curl(T_f+P_g)=T_b+P_f,
    b(q)=-4qg''(q)-(4l+6)g'(q),
    b'(q)=-4qg'''(q)-(4l+10)g''(q).

Thus Omega has toroidal degrees at most L_S and poloidal degrees at most L_T. Applying the preceding bounds after this interchange gives v and e. The stated regularity supplies all derivatives used here. Degree-zero scalar modes contribute zero to these curl fields, which is compatible with the upper bounds.

For a pressure term a_lm(r)H_lm(n), write it as b_lm(q)H_lm(y), where b_lm(q)=a_lm(sqrt(q))q^(-l/2). This is C^1 for q>0. Its Cartesian gradient is b_lm grad H_lm+2b_lm' y H_lm and has angular degree at most l+1. Consequently grad P has degree at most L_P+1.

Multiplication by y or Jy adds at most one angular degree; multiplication by J adds none. A product of two polynomial components has degree at most the sum of their degrees. These rules give the bounds u,d+1 for L, d+u,L_P+1 for N, and hence m for every displayed momentum summand. They give v,e+1 for L_Omega and e+u,d+v for N_Omega, hence h for the vorticity expressions. This proves all degree bounds without using the pressure equation or an Euler equation.

## Proof of quadrature exactness

A dot product of vector polynomials of component degrees at most m is a scalar polynomial of degree at most 2m. It suffices to integrate a Cartesian monomial of total degree D<=2m. Substituting

    n=(sqrt(1-mu^2)cos(phi), sqrt(1-mu^2)sin(phi), mu)

gives azimuthal Fourier frequencies of absolute value at most D. The equally spaced N_phi-point rule integrates every such frequency exactly when N_phi>D: its nonconstant frequency sums are zero, independently of the common offset. The remaining azimuthal mean vanishes if either the x or y exponent is odd. Otherwise it is a constant times (1-mu^2)^j mu^k of degree 2j+k<=D. The Gauss-Legendre rule integrates it exactly if 2N_mu-1>=D. Linearity proves the momentum statement. Replacing m by h proves the vorticity statement. Real and imaginary parts, conjugation, normalization of the weights and finite radial weighted summation preserve the conclusion. This also proves the cross-term assertion rather than inferring it only from squared norms.

## Degree-6 campaign substitution and scope

The relevant saved field metadata gives L_T=15 and L_S=14. The independent pressure synthesis uses L_P=36. These imply

    u=15, d=16, v=16, e=17, m=37, h=32.

Squared momentum terms and their Gram products therefore have degree at most74, and squared vorticity terms degree at most64. The42-by-84 rule satisfies 2*42-1=83>=74 and84>74. The48-by-96 rule also satisfies both conditions. These substitutions apply only to states and implementations with the checked channel and pressure cutoffs. A parameter change or radial twist that changes only radial coefficients preserves the degree bounds; an increase of angular cutoff requires a new bound.

The theorem concerns complete origin-centered spheres. It does not apply directly to displaced balls, polar caps, incomplete angular grids, sampled maxima, absolute helicity, pointwise ratios, or nonpolynomial angular weights. The pressure coefficients can contain angular projection error while the quadrature of their finite synthesis still meets the theorem. Numerical nodes, harmonic tables, source projection, field evaluation, cancellation and summation all incur floating-point errors that are not bounded here. In particular a numerical angular refinement comparison remains useful, but cannot be advertised as an enclosed error. Radial integration and pressure consistency require their own checks. No exact Euler field, rigorous residual bound, Tier acceptance or continuum maximum follows.

## Dependencies

The Cartesian potential formula and its derivative count are established in ../angular_source_projection/PROOF.md. The vorticity potential identity is established in ../vorticity_potentials/PROOF.md, and ../vorticity_identity/PROOF.md gives the connection to the curl of the momentum equation under the stronger regularity required there. The finite Fourier sum and Gauss-Legendre polynomial exactness are the quadrature facts used above. No formal proof or Lean/Lake build has been attempted.
