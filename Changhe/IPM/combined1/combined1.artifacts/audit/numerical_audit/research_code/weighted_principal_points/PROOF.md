# Exact weighted principal values on the horizontal axis

## Statement and scope

Let rho be the smooth case4 state131 density at the exact exponent c in the independently reconstructed canonical potential data. Its velocity is U=(-chi_xyy,chi_xxy), its density is rho=-chi_xxy-chi_yyy, and V=cX+U. For positive a,R let w=(1+r^2/R^2)^(-a/2). Define

b=-V.grad log w=a(c r^2+X.U)/(R^2+r^2),
theta=(sqrt(rho_x^2+rho_y^2)-rho_y)/2,
lambda=b+theta.

This result independently evaluates the seven rational points and weight parameters in the frozen T4 record. At each row the assertion is lambda>c+1. These are pointwise lower witnesses, not a global upper certificate. Their consequence for contractive weighted semigroups uses the separate principal-energy theorem in the frozen T4 proof; the present result does not certify that theorem.

## Derivation and exact evaluation

Differentiating log w gives grad log w=-aX/(R^2+r^2), proving the formula for b. The smaller eigenvalue of [[rho_y,-rho_x/2],[-rho_x/2,0]] is (rho_y-sqrt(rho_x^2+rho_y^2))/2, so its negative is theta. Since rho is odd in y, rho_x vanishes identically on y=0. The velocity U2 also vanishes there by parity. Thus, for x>0,

b=a(c x^2+x U1(x,0))/(R^2+x^2),
theta=(|rho_y(x,0)|-rho_y(x,0))/2.

The independent radial-Fourier differentiation of the canonical potential is proved in ../radial_fourier/PROOF.md. It writes each field as a finite sum of exact rational polynomials in t=r^2/(1+r^2), multiplied by rational powers of 1+r^2 and by elementary Fourier modes. At a nonzero rational axis point t is rational and all cosine modes are one, all sine modes zero. Polynomial evaluation, rational powers, and field summation in outward Arb arithmetic therefore enclose the exact values. The exponent and coefficients come from the exact state131 input. The same computations supply b, theta, lambda and their excess over c+1.

For each row, the verifier checks the exact source identity where applicable, the parity zeros, positivity of the excess, and overlap with every reported T4 nonzero field and derived quantity. Every comparison is recorded. A strictly positive lower endpoint proves the point assertion. Continuity implies the same supremum lower witness on the full plane. No mesh, quadrature, asymptotic truncation or floating optimizer result is used.

## Dependencies and evidence

The code is in code/reproduce.py; the peer target is frozen in peer_data/. Its SHA-256 hash, the independently reconstructed source hash, precision, comparisons and real runtime are recorded in verification/. This is a numerical audit of T4-047's seven axis values. The source, proof and method are fixed before the computation. No Lean build is run.
