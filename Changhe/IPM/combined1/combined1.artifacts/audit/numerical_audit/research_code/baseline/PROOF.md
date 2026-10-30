# Exact checkpoint interpretation and independent differentiation

## Statement, hypotheses, and notation

A case4 checkpoint specifies rational numbers by binary64 hexadecimal strings: c > 1, 59 free low coefficients, 800 high coefficients, and the 26 frozen Legendre normalizers. Its potential is

chi(x,y) = sum_{j=0}^3 sum_{m=0}^9 sum_{k=m}^{25} a[j,m,k] r^(2k) (1+r^2)^(p[j]-k) cos(2m theta),

where p[j]=(3+1/c-j(1-1/c))/2. At the origin the expression means its smooth continuation H_m(x,y) (r^2)^(k-m) (1+r^2)^(p[j]-k), where H_m=Re(x+iy)^(2m). Define rho=-partial_y Delta chi and U=(-partial_xyy chi, partial_xxy chi). The audit treats every saved hexadecimal number as its exact rational value. Decimal display arrays are not inputs.

The high coefficient h[j,m,n] multiplies N[n] t^v P_n(2t-1) (1+r^2)^p[j] cos(2m theta), with t=r^2/(1+r^2) and v=max(5,m). Expanding the Legendre polynomial gives exactly the canonical coefficients. The recurrence P_0=1, P_1=z, (n+1)P_(n+1)=(2n+1)zP_n-nP_(n-1) performs this expansion using rational arithmetic. The low block has k<=4 and enters directly.

## Center elimination

Write the degree-four Taylor part of chi as A x^4+B x^2 y^2+C y^4. Then partial_xxy chi=4B y to first order, so the center strain is 4B. The basis contributions to 4B are: 4p(p-1) for (m,k)=(0,0); 8(p-1) for (0,1); 8 for (0,2); and -24 for (2,2). All other basis terms contribute zero. This follows by multiplying the binomial series for (1+r^2)^(p-k) by the homogeneous polynomial H_m(r^2)^(k-m) through degree four. Since p[0]>3/2, its first strain coefficient is nonzero. The equation 4B=1-c therefore determines a[0,0,0] uniquely in rational arithmetic. The high block begins at degree ten and has no center contribution.

The center density derivative is a0=-(4B+24C). The residual F=(cX+U).grad rho-rho has linear y coefficient (c+4B-1)a0=0. Higher Taylor residual coefficients need not vanish exactly merely because their saved floating displays are small.

## Independent Cartesian derivatives in polar form

For A(r)=r^d(1+r^2)^b, A'=d r^(d-1)(1+r^2)^b+2b r^(d+1)(1+r^2)^(b-1). The polar identities partial_x=cos(theta) partial_r-sin(theta) partial_theta/r and partial_y=sin(theta) partial_r+cos(theta) partial_theta/r, followed by product-to-sum identities, give

partial_x[A cos(n theta)] = (A'+nA/r) cos((n-1)theta)/2 + (A'-nA/r) cos((n+1)theta)/2,

partial_y[A cos(n theta)] = (A'-nA/r) sin((n+1)theta)/2 - (A'+nA/r) sin((n-1)theta)/2,

partial_x[A sin(n theta)] = (A'+nA/r) sin((n-1)theta)/2 + (A'-nA/r) sin((n+1)theta)/2,

partial_y[A sin(n theta)] = (A'+nA/r) cos((n-1)theta)/2 - (A'-nA/r) cos((n+1)theta)/2.

Repeated differentiation is finite and exact for r>0. This is an alternative to the previous audit's point-centered Cartesian jet algebra. Evaluation in ball arithmetic encloses individual field values; it does not bound unsampled regions or global norms.

## Dependencies and scope

Dependencies are polynomial algebra, the Legendre recurrence, the binomial Taylor series at r=0, and the displayed polar differentiation identities. Source interpretation is checked against the saved canonical serialization hash and the prior independent reconstruction, but neither comparison proves that a checkpoint solves the PDE. No formal Lean artifact is produced in this run.
