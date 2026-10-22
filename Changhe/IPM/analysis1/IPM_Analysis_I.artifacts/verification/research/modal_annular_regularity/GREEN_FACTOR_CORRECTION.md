# Correction of the Green prefactor before review

Written 2026-10-21T20:19:34.906528+00:00. Mandatory with PROOF.md. No verdict had been issued.

The stream-mode formula in PROOF.md must read

 psi_n(t)=exp(4t)(J_n(t)-I_n(t))/2.

The printed extra division by n was an error, caught by comparing the previously accepted definition and then independently deriving the Poisson equation. All regularity classes in the statement are unchanged by this correction. The endpoint checker does not use the prefactor. This supplement gives the full independent verification.

Set m=2n, A=H_(n-1), B=H_n, D=d/dt. In polar coordinates partial_x=cos(theta)partial_r-sin(theta)partial_theta/r. The raising contribution of rho's sin((m-1)theta) mode is r^2[A'+(4-m)A]/2; the lowering contribution of sin((m+1)theta) is r^2[B'+(m+4)B]/2. This follows directly from cos(theta)sin(l theta)=[sin((l+1)theta)+sin((l-1)theta)]/2 and sin(theta)cos(l theta)=[sin((l+1)theta)-sin((l-1)theta)]/2.

The moment ODEs are (D+m+4)I=A and (D+4-m)J=-B. Hence

 ((D+4)^2-m^2)(J-I)=-(D+m+4)B-(D+4-m)A.

For a stream mode exp(4t)(J-I)sin(m theta)/2, the negative Laplacian is -exp(2t)[((D+4)^2-m^2)(J-I)]sin(m theta)/2. This is exactly the preceding partial_x rho coefficient. Dividing by another n would instead produce1/n times that coefficient, and is incorrect for n>1. The canonical boundary conditions are those in the exact integral definition; no harmonic strain is added.

The new independent finite audit uses a six-variable jet vector and direct differentiation over Fraction, versus the factored ODE operator and angular raising/lowering coefficients over fmpq. It checks every1<=n<=261. It explicitly rejects the erroneous prefactor for n=2 and n=135. No moment enclosure or bound is inferred from this algebra.
