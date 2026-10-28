# Certificates for the weighted high principal matrices

## Exact setting

Use the exact accepted checkpoint131, c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma, and sigma=1/5. For real derivative order k and radius Rk>0 put

    omega_k=(1+r²/Rk²)^((k-1-sigma)/2),
    M_k=(1+c+V.grad log omega_k)I-k sym(DV)+A,
    V=cX+Ubar, A=[[rho_y,-rho_x/2],[-rho_x/2,0]].

The completed certificates prove M_k>=1/2 I globally at(k,Rk)=(1,1),(2,1/2). There are131 and201 leaves respectively, and all leaves were reconstructed at384-bit precision in an independent tree audit. The optional noninteger target(21/10,1/2) has not been certified. It is a principal-matrix certificate only. Full weighted energy bounds require the lower terms in the companion proof.

## Exact compactification

Set t=r²/(1+r²), z=cos(2theta), w=(1-t)^(delta/2), and d_k(t)=Rk²+(1-Rk²)t. The exact potential representation gives

    chi_22=sum_(j=0)^3 w^(j+1) P_22,j(t,z),
    chi_04=sum_(j=0)^3 w^(j+1) P_04,j(t,z),
    chi_31=sin(2theta) sum_(j=0)^3 w^(j+1) P_31,j(t,z),
    chi_13=sin(2theta) sum_(j=0)^3 w^(j+1) P_13,j(t,z).

Every P is an exact rational polynomial, as in the independent unweighted matrix certificate. A third derivative multiplied by x or y, divided by Rk²+r², has the same radial factor w^(j+1)/d_k(t). In particular

    Ubar.X/(Rk²+r²)=sum_(j=0)^3 w^(j+1) P_rad,j(t,z)/d_k(t).

To construct P_rad, differentiate each potential generator three times, form -x chi_xyy+y chi_xxy by the elementary products of sin(theta),cos(theta) with its angular modes, and collect the power t^(k_generator-1+l). No numerical evaluation or fitted coefficient enters these polynomials.

Write tau=k-1-sigma and b=1+(1-k)c. Multiplying M_k by the strictly positive d_k gives a polynomial matrix in t,z,w, with off-diagonal factor sin(2theta). Its common scalar part is

    b d_k(t)+tau c t.

Its remaining entries are the exact sums over j of w^(j+1) times

    upper diagonal: d_k[(k-1)P_22,j-P_04,j]+tau P_rad,j,
    lower diagonal: -k d_k P_22,j+tau P_rad,j,
    off diagonal: d_k[(1-k)P_31,j+(1+k)P_13,j]/2.

Subtracting(1/2)d_k I before certification proves the desired original matrix bound. The denominator is positive on the entire compact rectangle, including t=0 and t=1.

## Continuum enclosure and audit

The script converts each rational polynomial to tensor Bernstein coefficients on[0,1]x[-1,1], subdivides with exact dyadic boxes, and encloses w on each box with Arb. A further degree-four Bernstein transformation retains cancellations among the four powers of w. The smallest eigenvalue is bounded below using enclosed diagonal lower bounds and the off-diagonal absolute upper bound. The polynomial scalar diagonal is included before taking the enclosure.

A successful certificate covers the full compactified quadrant, hence the plane by parity. Its JSON records the source coefficient hash, exact k,Rk,sigma,target, every leaf path and box, and every Arb lower bound. An independent Cartesian field evaluation checks the formula at rational points; a separate certificate audit reconstructs every leaf and verifies its bounds and the exact binary partition. These point checks supplement, and do not replace, the continuum Bernstein proof.

## Auxiliary third-order growth certificate

With k=3, sigma=6/5 and Rk=1/2, the weight is again(1+4r²)^(2/5). The same exact construction certifies M3_aux>=-5/4 I. The282-leaf adaptive certificate and its384-bit full-tree recomputation are in state131_high_symbol_k3_adaptive_auxiliary.json and high_symbol_certificate_audit.json. This auxiliary matrix supports interpolation with a growing third-order norm in ROUTE_U_HIGH_PROOF.md. It is not a dissipative third-order bound.
