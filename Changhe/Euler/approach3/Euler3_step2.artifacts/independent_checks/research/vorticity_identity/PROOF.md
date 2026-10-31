# Curl and divergence of the rotating momentum residual

Status: exact local identities. These statements do not assert the existence of an Euler profile or certify a numerical state.

## Statement and notation

Let D be an open subset of R^3, let U belong to C^3(D;R^3), and let P belong to C^3(D;R). Let c,w be real constants. Set Jy=(-y_2,y_1,0), A=DU with A_ij=partial_j U_i, d=div U, Omega=curl U, and

    W=cy-wJy+U,
    R=(1-c)U+A W+wJU+grad P.

Then, pointwise on D,

    curl R = Omega + DOmega W - A Omega + wJ Omega + d Omega,
    div R = tr(A^2) + Delta P + d + W dot grad d.

In particular, if d vanishes identically, the pressure-independent vorticity residual is

    R_Omega = Omega + DOmega W - A Omega + wJ Omega = curl R,

and div R=tr(A^2)+Delta P. At y=0, if 0 is in D, these formulas hold with W=U(0); no spherical-coordinate limit is involved.

Define the linear momentum operator

    L U=(1-c)U+c DU y+w(JU-DU Jy).

Its curl is

    curl(LU)=Omega+c DOmega y+w(JOmega-DOmega Jy).

Consequently, for divergence-free U,

    R_Omega=curl(LU)+DOmega U-DU Omega.

This last form permits evaluation of the linear contribution through the exact stable potential formula established in ../stable_linear_operator/PROOF.md.

## Proof of the curl identity

For every C^2 vector field, direct differentiation of the Cartesian curl gives

    curl((y dot grad)U)=Omega+(y dot grad)Omega.

The vector rotation generator B(U)=JU-(Jy dot grad)U commutes with curl. To check this without a coordinate convention, put Q_t=exp(tJ). The field Q_t U(Q_t^{-1}y) has derivative B(U) at t=0. Because Q_t is an orientation-preserving orthogonal matrix, the Levi-Civita formula gives curl[Q_t U(Q_t^{-1}y)]=Q_t Omega(Q_t^{-1}y). Differentiate in t to obtain curl B(U)=B(Omega).

The identity (U dot grad)U=grad(|U|^2/2)-U cross Omega follows componentwise by contraction of two Levi-Civita symbols. Taking its curl and using div Omega=0 yields

    curl((U dot grad)U)
      =(U dot grad)Omega-(Omega dot grad)U+(div U)Omega.

The curl of grad P is zero by equality of mixed second derivatives. Adding these formulas to the curl of (1-c)U gives the displayed curl identity, since (1-c)Omega+c Omega=Omega. Applying the same argument without the nonlinear term proves the formula for curl(LU).

## Proof of the divergence identity

The product rule gives

    div((y dot grad)U)=d+y dot grad d,
    div((U dot grad)U)=tr(A^2)+U dot grad d.

For the rotational term,

    div(JU)=sum_(i,j) J_ij partial_i U_j,
    div((Jy dot grad)U)
      =sum_(i,j) J_ji partial_j U_i+(Jy) dot grad d.

The finite sums are equal after interchanging their dummy indices, so div B(U)=-(Jy) dot grad d. Finally div grad P=Delta P. Summing and using (1-c)d+cd=d proves the claim.

## Cartesian Hessian needed by the verifier

For one mode of the field formula in ../field_reconstruction/PROOF.md, let H be a homogeneous harmonic polynomial of degree ell>=1, h=grad H, K=D^2H, T=D^3H, q=|y|^2, and C=h cross y. For smooth real functions f,g of q set

    a=(ell+1)g+2qg',     b=-2ell g',
    a'=(ell+3)g'+2qg'',  a''=(ell+5)g''+2qg''',
    b'=-2ell g'',        b''=-2ell g'''.

The mode is V=f C+a h+b yH. Here primes denote derivatives with respect to q. For any such scalar F(q), write F_j=2F' y_j and F_jk=2F' delta_jk+4F''y_jy_k. Define

    C_j=(K e_j) cross y+h cross e_j,
    C_jk=T(:,j,k) cross y+(K e_j) cross e_k+(K e_k) cross e_j.

Then

    partial_k partial_j V_i
      = f_jk C_i+f_j C_(i,k)+f_k C_(i,j)+f C_(i,jk)
        +a_jk h_i+a_j K_ik+a_k K_ij+a T_ijk
        +b_jk y_i H+b_j(delta_ik H+y_i h_k)
        +b_k(delta_ij H+y_i h_j)
        +b(delta_ij h_k+delta_ik h_j+y_i K_jk).

This is the twice-applied product rule to the three summands of V. The formulas for a',a'',b',b'' are their ordinary derivatives; the formulas for C_j,C_jk follow by differentiating h cross y. Thus the Hessian formula is proved, including at y=0. Sum it over the finite modes, and obtain DOmega by the fixed Cartesian curl contraction of D^2U.

## Dependencies and numerical scope

Dependencies are finite product rules, equality of mixed derivatives, the Cartesian Levi-Civita curl formula, and the cited potential identities. The finite smooth representation satisfies div U=0 in exact arithmetic. Separately rounded field values and derivative tables need not satisfy the numerical identities exactly. The verifier must measure that discrepancy. A pressure quadrature does not become a differentiable or Poisson-consistent numerical field merely by substituting its values into these identities. The pressure-Poisson defect therefore requires its own defined reconstruction and check.
