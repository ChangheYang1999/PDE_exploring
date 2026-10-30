# Independent point witnesses for newly published candidates

## Statement and scope

Fix a real smooth S1 potential from an immutable candidate snapshot. Write c for its exact exponent, gamma=1/c, delta=1-gamma, t=r²/(1+r²), and u=1-t. The snapshot describes

chi=sum_(j,m) H_m(x,y) (1+r²)^(p_j-m) T_(j,m)(t),
p_j=(3+gamma-j delta)/2, H_m=Re(x+iy)^(2m).

The coefficient of each generator is an exact rational. T is a monomial or a shifted Legendre polynomial times a monomial. Define rho=-partial_y Delta chi, psi=partial_x partial_y chi, U=(-partial_y psi,partial_x psi), V=cX+U and F=V.Drho-rho. The construction below evaluates all these fields at a specified nonzero rational point using exact rational polynomial operations and rigorous Arb powers. It is independent of the Cartesian Taylor evaluator used by N4.

At every such point, an exact stationary correction h in H^(2+s), at the same c, must obey

|F| <= r_h[C1 |V|+C0(1+|Drho|)]+C0 C1 r_h²,
C0=(4pi(1+s))^(-1/2), C1=(8pi s(1+s))^(-1/2),

where r_h bounds ||h||_(H^(2+s)). A positive certified gap excludes that ball. The necessary radius is at least 2|F|/(A+sqrt(A²+4B|F|)), with A=C1|V|+C0(1+|Drho|), B=C0C1. This follows by expanding the exact stationary equation and using the independently audited Fourier point bounds in ../residual_witness/PROOF.md. This argument requires no sufficient inverse theorem or background matrix condition. It excludes only the specified chart and ball.

## Exact conversion from generator data

The identity

L_n(2t-1)=sum_(k=0)^n (-1)^(n+k) binom(n,k)binom(n+k,k)t^k

follows from Rodrigues' formula for the Legendre polynomial, by differentiating t^n(t-1)^n n times and dividing by n!. Since H_m=r^(2m)cos(2m theta), the potential takes the form

chi=sum u^(-p_j) P_(j,n)(t) cos(n theta), n=2m.

For a monomial generator t^h, P gains coef*t^(m+h). For t^w L_n(2t-1), it gains the exact shifted polynomial times coef*t^(m+w). The implementation checks the full coefficient dictionary against the independently converted N4 canonical file; that comparison is a separate check, not an input to its conversion.

## Polar differentiation

For a polynomial P define A_p P=2ptP+2tuP'. Then r partial_r[u^(-p)P]=u^(-p)A_pP. The polar Laplacian therefore gives

Delta[u^(-p)P cos(n theta)] = r^(-2)u^(-p)(A_p²P-n²P)cos(n theta).

Put B=A_p²P-n²P and E=A_p B-2B. Since partial_y=sin(theta)partial_r+cos(theta)r^(-1)partial_theta, the density contributions at harmonics n-1 and n+1 are respectively (E+nB)/2 and -(E-nB)/2, with a common r^(-3)u^(-p). Negative sine indices are folded by sin(-n theta)=-sin(n theta). After terms at equal (j,n) are combined, their numerator is divisible by t², by regularity at the origin and direct polynomial verification. Since r^(-3)u^(-p)t² = r u^((j+1)delta/2), this yields

rho=r sum u^a R_(j,n)(t) sin(n theta), a=(j+1)delta/2.

Twice differentiating the original cosine term gives stream numerators

(A_p-n-2)(A_p-n)P/4 at harmonic n+2,
-(A_p+n-2)(A_p+n)P/4 at harmonic n-2.

The same folding and exact division by t² yield

psi=r² sum u^a S_(j,n)(t) sin(n theta).

Define T_(a,k)P=(k-2at)P+2tuP'. Then

rho_r=sum u^a T_(a,1)R sin(n theta),
rho_theta/r=sum u^a nR cos(n theta),
U_r=-r sum u^a nS cos(n theta),
U_theta=r sum u^a T_(a,2)S sin(n theta).

Converting these radial and angular components to Cartesian coordinates gives the five required fields. The signs follow from U=(-psi_y,psi_x), whose radial component is -psi_theta/r. The residual is formed from these fields, not from a separately stored residual polynomial.

## Rigorous evaluation and dependencies

At a rational nonzero (x,y), r², t and u are exact rationals. Every polynomial is evaluated exactly at t. The only remaining nonrational operations are r=sqrt(r²), the positive powers u^a, and arithmetic in r, x/r and y/r. Arb encloses these operations. Harmonics are formed from the addition recurrence for sine and cosine, without sampled angular quadrature. The final JSON records the source and code hashes, precision, real elapsed time, field intervals and point gaps. Interval overlap with a prior calculation is an independent reproduction check; the sign of the newly computed gap itself supplies the exclusion.

This result does not establish continuum supremum bounds, full-plane residual norms or candidate existence. No Lean or other proof assistant is run under the campaign restrictions.
