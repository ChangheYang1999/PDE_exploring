# Gradient subtraction in the weak correction-distance test

Status: new T4 result, OPEN pending independent review. The argument is written before the numerical experiment. No existence theorem is asserted.

## Statement and spaces

Use the real S1 stationary equation and all hypotheses of ../angular_weak_probes/PROOF.md. Thus w=(1+r^2)^(-a/2), 0<=a<2, h and its canonical divergence-free velocity U[h] are in L2(w^2 dX), ||w U[h]||2<=C_U||wh||2, and rho+h is stationary at the same c. Let phi be one of that note's smooth odd-angular probes. Write

    m=||wh||2, I=int F(rho;c)phi,
    M_phi=(2c+1)phi+(cX+U[rho]).grad phi,
    M=||M_phi/w||2, H=||grad phi/w^2||infinity,
    A=phi grad rho, B=rho grad phi.

For any real scalar lambda set

    C_lambda=||[(1-lambda)A-lambda B]/w||2.

Then every such stationary correction satisfies

    |I| <= (M+C_U C_lambda)m+C_U Hm^2.                 (1)

Consequently the usual positive quadratic root, with D=M+C_U C_lambda, is a necessary lower bound for m. For an exact rational lambda, C_lambda can be certified directly without taking an approximate optimizer as exact data.

Put C2=||A/w||2^2, B2=||B/w||2^2 and X=int A.B/w^2. If S=C2+2X+B2>0, the exact best scalar choice is

    lambda_*=(C2+X)/S,
    inf_lambda C_lambda^2=(C2 B2-X^2)/S.               (2)

If S=0, then A+B=0 almost everywhere and C_lambda=C_0 for every lambda. A finite-precision evaluation of (2) must enclose every quantity and the denominator away from zero. A rational nearby lambda avoids needing a certified quotient as input. This optimization concerns only the displayed one-dimensional family, not all possible gradients or all test functions.

## Proof

The audited weak identity is

    I=int h M_phi-int U[h].A+int h U[h].grad phi.

The scalar p=rho phi is smooth, and grad p=A+B. Since div U[h]=0 distributionally,

    int U[h].grad p=0.                                (3)

To justify using the noncompact p, multiply it by a smooth cutoff at radius R. Its derivative error is bounded by the L2 tail of wU[h] times the L2 norm of p grad cutoff/w. Here p=O(r^(gamma-3)), so this latter norm is O(R^(a+gamma-3)); it tends to zero for a<2 and gamma<1. The interior integrals converge by weighted Cauchy-Schwarz. Thus (3) holds without imposing a boundary condition at infinity beyond the stated spaces.

Subtract lambda grad p from A in the weak identity, use (3), and apply exactly the previous three Cauchy-Schwarz bounds. This proves (1). Expanding the squared norm gives

    C_lambda^2=C2-2lambda(C2+X)+lambda^2 S.

Completing the square proves (2). Nonnegativity of its numerator is Cauchy-Schwarz; S is the squared norm of grad p/w. If S=0, that gradient is zero as an L2 vector and the correction to A vanishes.

## Exact polar forms for one odd angular mode

Set t=r^2/(1+r^2), W=1-t, and phi=rW^2P(t)sin(N theta), where N is a positive odd integer and t^((N-1)/2) divides P. Let Q=(1-4t)P+2tWP'. Expand the density as

    rho=r sum_i W^ai R_i(t)sin(l_i theta),
    T_i=(1-2ai t)R_i+2tWR_i'.

All l_i are positive integers. Define the integer angular coefficients

    aa(l,m)=2[l=m]-[|l-m|=2N]+[l+m=2N],
    bb(l,m)=2[l=m]-[|l-m|=2N]-[l+m=2N],
    dd(l,m)=2[l=m]+[|l-m|=2N]-[l+m=2N],
    xx(l,m)=[l+m=2N]+sgn(m-l)[|m-l|=2N].

The full sums, with all ordered i,j and all cross terms retained, are

    C2 = pi/8 sum_ij int_0^1 t W^(1-a+ai+aj)
          P^2 [aa(l_i,l_j)T_i T_j
                    +bb(l_i,l_j)l_i l_j R_i R_j] dt,

    B2 = pi/8 sum_ij int_0^1 t W^(1-a+ai+aj)
          R_i R_j [aa(l_i,l_j)Q^2
                    +dd(l_i,l_j)N^2 P^2] dt,

    X = pi/8 sum_ij int_0^1 t W^(1-a+ai+aj)
          [aa(l_i,l_j)P Q T_i R_j
                    +xx(l_i,l_j)N l_i P^2 R_i R_j] dt. (4)

Proof of (4). The radial components of A and B are respectively r W^(ai+2)P T_i sin(N theta)sin(l_i theta) and r W^(ai+2)Q R_i sin(N theta)sin(l_i theta). Their angular components are respectively r W^(ai+2)l_i P R_i sin(N theta)cos(l_i theta) and r W^(ai+2)N P R_i cos(N theta)sin(l_i theta). The aa and bb integrals are already proved in the angular-probe note. Replacing sin(N theta)^2 by cos(N theta)^2 gives dd. Finally,

    int sin(N theta)cos(N theta)cos(l theta)sin(m theta)dtheta
         =pi xx(l,m)/4,

by twice applying product-to-sum, with the sign of m-l retained. The radial Jacobian gives the remaining factor1/2 and power tW^(1-a+ai+aj). This proves every term in (4).

A numerical certificate must provide an exact input hash, the rational probe and lambda, enclosures for C2,B2,X, the resulting C_lambda and root, and a separate full-domain H certificate. The old M,H,I may be reused only for the identical candidate and probe.
