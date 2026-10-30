# Independent audit of the recorded radial pairing rules

## Exact statement and scope

Fix the rational canonical candidate C1-N1-007-d2w-j7-e2bal with source
SHA256 153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Write c for its similarity exponent, delta=1-1/c, t=r²/(1+r²) and W=1-t.
Its first sine residual mode has the exact form

    F_1(r)=r sum_ell W^(ell delta/2) P_ell(t).

For each integer k>=0 define phi_k=r W² t^k sin(theta). For any finite list
of positive rational radii r_i and real rational weights w_i, define

    Q_k=pi sum_i w_i t_i^(k+2)
                  sum_ell W_i^(ell delta/2) P_ell(t_i).

This is precisely the finite radial quadrature approximation to
I_k=integral F phi_k dX when the radial integration variable is log r and
the angular integration is performed analytically. Consequently an
outward enclosure of Q_k-I_k certifies the error of that finite sum.
It does not certify that the recorded rational nodes and weights form an
exact Gauss rule or describe the exact arithmetic of a floating program.

## Reconstruction and proof

The canonical field loader gives

    rho=r sum_(j,n) W^((j+1)delta/2) R_(j,n)(t) sin(n theta),
    psi=r² sum_(j,m) W^((j+1)delta/2) S_(j,m)(t) sin(m theta).

Use u=r^(-1)(-psi_theta)e_r+psi_r e_theta. With
T_(a,d)P=(d-2at)P+2tW P', the linear first mode is
c T_(a,1)R-R. For a stream mode m and density mode n, the nonlinear
coefficient in mode n+m is

    [n R T_(a_stream,2)S-m S T_(a_rho,1)R]/2.

The coefficient in mode |n-m| is

    sign(n-m)[-n R T_(a_stream,2)S-m S T_(a_rho,1)R]/2.

Retain only output frequency1. These identities follow directly from
the two sine-cosine product formulas. They independently reconstruct
every polynomial P_ell without relying on the peer's projection code.

Since the angular sine square integral is pi, r dr=dt/(2W²) and r²=t/W,

    I_k=(pi/2) sum_ell integral_0^1
                  t^(k+1) W^(ell delta/2-1) P_ell(t) dt.

Equivalently, with s=log r, r dr=r² ds,

    I_k=pi integral t^(k+2) sum_ell W^(ell delta/2)P_ell(t) ds.

This proves the asserted finite-sum formula. Each branch exponent in the
first integral exceeds -1 for this candidate. Polynomial expansion in W
reduces its integral to beta moments with one positive integer argument.
The recurrence B(b+1,M+1)=M! / product_(j=1)^(M+1)(b+j), followed by
B(b+j+2,M+1)/B(b+j+1,M+1)=(b+j+1)/(b+j+M+2), evaluates them with outward
arithmetic and no numerical quadrature.

For the optional radial split at R, put x_R=1/(1+R²) and
Z(W)=(1-W)^(k+1)P_ell(1-W). For b=ell delta/2-1,

    integral_(r>R) F_ell phi_k dX
      =(pi/2) sum_j Z_j x_R^(b+j+1)/(b+j+1).

All denominators are positive. This follows by termwise integration,
including the zero endpoint by b>-1. Subtract two exterior integrals to
obtain the middle domain and subtract the exterior from I_k to obtain the
interior. Thus the finite-sum error can be distinguished from omitted
radial tails.

## Verification contract

The check reconstructs F_1 from the canonical fields and compares every
rational coefficient with the previously audited frozen first-mode
polynomial. It then evaluates the reconstructed P_ell directly in t at
the peer's recorded rational nodes, whereas the peer primarily evaluates
P_ell(1-W) in W. It recomputes every complete pairing and radial split
locally and checks interval overlap for each finite sum and error.

All comparisons concern this one exact candidate and these recorded
finite node lists. Their usefulness for a changed candidate is an
optimization diagnostic, not a uniform quadrature theorem. No existence,
residual norm, or optimizer convergence assertion follows.
