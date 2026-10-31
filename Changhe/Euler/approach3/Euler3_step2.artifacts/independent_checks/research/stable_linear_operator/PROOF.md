# Exact potential formula for the rotating linear momentum operator

Date: 2026-10-28. Status: proved algebraic identity. This is not an Euler existence result or a numerical accuracy certificate.

## Statement, spaces and notation

Let c and w be real constants, c nonzero. Put J(x,y,z)=(-y,x,0), D_r=y dot grad, and partial_phi=(Jy) dot grad. For a differentiable vector field V, define L_J V=DV(Jy)-JV and

    A V = (1-c)V + c D_r V - w L_J V.

If T is a complex-valued C^2 scalar function and S is a complex-valued C^3 scalar function on an open rotation-invariant subset of R^3, then for U=curl(Ty)+curl curl(Sy),

    A U = curl((B_T T)y) + curl curl((B_S S)y),
    B_T = (1-c) + c D_r - w partial_phi,
    B_S = (1-2c) + c D_r - w partial_phi.

The same identity holds for real and imaginary parts. The nonlinear momentum residual is exactly

    R = A U + DU U + grad P.

No pressure equation is assumed in this identity.

For the following scalar formula take R0>0, r=|y|, s=sqrt(r^2+R0^2), alpha=(1-c)/c and psi=(w/c)log(s/R0). Let H be a homogeneous harmonic polynomial of degree ell satisfying partial_phi H=i m H, where ell is a nonnegative integer and m is an integer. Let nu,b be real constants and B a C^1 function of s. For

    F(y) = (s/R0)^(-nu) B(s) exp(i m psi(s)) H(y),
    delta = b + c ell - c nu,

the exact scalar identity is

    (b + c D_r - w partial_phi)F
      = (s/R0)^(-nu) exp(i m psi) H
        * { [delta + (c nu - i m w) R0^2/s^2] B(s)
             + c r^2/s B'(s) }.

On a domain containing the origin the formula is read through the smooth Cartesian expressions s=sqrt(|y|^2+R0^2), H(y), and exp(i m psi(s)). It introduces no polar-axis division. If B is smooth on an interval containing [R0,infinity), the resulting scalar functions are smooth on R^3.

For a main toroidal mode, b=1-c and nu=alpha+ell, so delta=0. For a main poloidal mode, b=1-2c and nu=alpha+ell-1, again delta=0. If B(s)=C(x(s)), x=(s-R0)/(s+R0), its final derivative term is

    c r^2/s * [2 R0/(s+R0)^2] C'(x).

Extra envelope factors, including core damping, must be included in B and differentiated. A channel with a different nu retains its actual delta. These qualifications are required for equality with the original representation.

## Proof

For any C^2 vector field V, componentwise differentiation and the product rule give

    D_r curl V = curl(D_r V) - curl V.

Applying this twice gives D_r curl curl V = curl curl(D_r V) - 2 curl curl V whenever the indicated derivatives exist. For V=Ty, D_r V=(D_r T+T)y. Hence

    D_r curl(Ty) = curl((D_r T)y).

For V=Sy the twice-applied identity gives

    D_r curl curl(Sy) = curl curl((D_r S-S)y).

To handle rotation, let Q_t=exp(tJ), an orientation-preserving orthogonal matrix. The pullback of a vector field is V_t(y)=Q_t^(-1)V(Q_t y). The Cartesian curl transformation law, obtained by substituting this expression into the Levi-Civita formula for curl and using det Q_t=1, is

    curl V_t(y) = Q_t^(-1)(curl V)(Q_t y).

Differentiation at t=0 gives curl(L_J V)=L_J(curl V). Applying it twice gives the corresponding double-curl identity. Also

    L_J(Ty) = (partial_phi T)y,

because D(Ty)(Jy)=(partial_phi T)y+T Jy, and J(Ty)=T Jy. Substituting the radial and rotational commutation identities into A U proves the first display. Expanding A U + DU U gives (1-c)U + DU(cy-wJy+U)+wJU, exactly the pressure-free part of the specified momentum residual.

For the scalar formula, homogeneity gives D_r H=ell H, while s depends only on r and satisfies D_r s=r^2/s. Thus

    D_r[(s/R0)^(-nu)] = -nu r^2/s^2 (s/R0)^(-nu),
    D_r B(s) = r^2/s B'(s),
    D_r exp(i m psi) = i m (w/c) r^2/s^2 exp(i m psi).

The radial factors have zero partial_phi derivative, and partial_phi H=i m H. The product rule therefore gives the coefficient of B as

    b + c ell - c nu r^2/s^2 + i m w(r^2/s^2-1).

Using r^2/s^2=1-R0^2/s^2 yields delta+(c nu-i m w)R0^2/s^2. This proves the scalar formula. The two main-envelope cancellations follow by c alpha=1-c. The Chebyshev-coordinate formula follows by direct differentiation of x(s).

## Dependencies and scope

Only the product rule, Cartesian curl formula and orthogonal covariance of curl are used; the covariance has been justified above. No source code is used in the proof. The exponential convention assumes partial_phi H=i m H; a representation using the conjugate harmonic must conjugate the i m terms consistently.

The identity suggests a stable evaluation of the linear momentum term because it removes the analytically zero main-envelope constant before numerical summation. It does not establish stability of a particular implementation, does not remove all possible cancellation, does not prove that cancellation caused the observed G1 failures, and does not alter the objective, basis, channel counts or pressure. Any implementation must be checked against the original formula at ordinary radii, against extended precision at far radii, and by the registered derivative tests.
