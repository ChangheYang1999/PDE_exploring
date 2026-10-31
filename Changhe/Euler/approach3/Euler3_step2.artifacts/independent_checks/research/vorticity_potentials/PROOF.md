# Vorticity in the same finite potential representation

Status: exact identities. These formulas reduce the cost of evaluating the vorticity and its Jacobian on tensor grids. They make no claim that a numerical state solves Euler.

## Statement

Let ell be a positive integer, H a real homogeneous harmonic polynomial of degree ell on R^3, and q=|y|^2. Let I be an open interval containing [0,infinity), f belong to C^2(I), and g belong to C^3(I). Only their restrictions to nonnegative q matter. Define

    C(y)=grad H(y) cross y,
    T_f(y)=f(q) C(y),
    P_g(y)=((ell+1)g(q)+2qg'(q)) grad H(y)-2ell g'(q)yH(y).

Then U=T_f+P_g is divergence free, and

    curl U=T_b+P_f,
    b(q)=-4qg''(q)-(4ell+6)g'(q),
    b'(q)=-4qg'''(q)-(4ell+10)g''(q).

The first identity holds on R^3, including at y=0. Its Cartesian derivative is obtained by differentiating T_b+P_f once. Only b,b',f,f',f'' are needed, so g''' is sufficient and no fourth radial derivative is required.

For a finite sum of modes these statements hold term by term. A smooth radial twist is incorporated by splitting each sine/cosine pair into the two real terms with their own scalar f,g; the polynomial H in each term has no radial dependence.

## Proof

The established finite-potential formula gives

    T_f=curl(f(q)H(y)y),
    P_g=curl curl(g(q)H(y)y).

Therefore div T_f=div P_g=0, and curl T_f=P_f. Also curl P_g=curl curl T_g. The identity curl curl V=grad div V-Delta V and div T_g=0 imply curl P_g=-Delta T_g.

Every Cartesian component of C is a homogeneous polynomial of degree ell. It is harmonic: in each component epsilon_ijk (partial_j H)y_k, the Laplacian is epsilon_ijk ((partial_j Delta H)y_k+2 partial_k partial_j H), which vanishes because Delta H=0 and the Hessian is symmetric. Euler's homogeneous polynomial identity therefore gives y dot grad C_i=ell C_i and Delta C_i=0.

The product rule, grad g(q)=2g'(q)y and Delta g(q)=4qg''(q)+6g'(q), now give

    Delta(g(q)C_i)
      =(4qg''+6g')C_i+4g' y dot grad C_i
      =(4qg''+(4ell+6)g')C_i.

Thus curl P_g=T_b with b as stated. Differentiating b gives b'=-4qg'''-(4ell+10)g''. All terms are Cartesian products of polynomials and smooth functions of q, so this argument also holds at the origin. Finally the derivative of P_f uses f'' by the explicit formula, and that of T_b uses only b'. This proves every claim.

## Tensor-grid consequence and scope

For r>0, H(rn)=r^ell H(n), grad H(rn)=r^(ell-1)grad H(n), and the successive polynomial derivatives scale by their corresponding degrees. Consequently the already-qualified tensor-grid first-derivative assembly can evaluate U,DU,Omega,DOmega from the radial pairs (f,g) and (b,f), respectively. The origin must use the Cartesian formula rather than separate negative powers of r.

For stable linear momentum potentials (f_L,g_L), curl(LU)=T_bL+P_fL needs only g_L'' and f_L'. It does not require the undefined third derivative of a truncated stable radial jet. This quantity can be combined with DOmega U-DU Omega to form the pressure-independent vorticity residual under the hypotheses of ../vorticity_identity/PROOF.md.

Dependencies: ../field_reconstruction/PROOF.md, the Cartesian curl identities, harmonicity and homogeneity of H, and ordinary product differentiation. These exact identities do not bound floating-point error or quadrature error.
