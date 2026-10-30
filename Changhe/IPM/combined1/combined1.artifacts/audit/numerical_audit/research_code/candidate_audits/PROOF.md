# Independent audit of immutable candidate snapshots

## Exact statement and scope

Each audit takes one immutable snapshot of an S1 potential, its manifest, and its checksums. Coefficients are rational strings. The potential is

chi=sum_(j,m) H_m(x,y) R^(p_j-m) P_(j,m)(t),
R=1+x²+y², t=(x²+y²)/R,
p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma,
H_m=Re(x+iy)^(2m).

Every generator polynomial is either t^h or t^w L_n(2t-1), where L_n is the ordinary Legendre polynomial. The resulting canonical coefficients a_(j,m,k) are exact rationals in

chi=sum a_(j,m,k) r^(2k) R^(p_j-k) cos(2m theta).

The audit verifies exact coefficient conversion, fixed c and leading angular density, the strain condition, and all residual sectors with exponent at least -2. Matching a decimal loss is not a certification of a full-plane norm. A failed forbidden sector excludes the unweighted framework, even when the optimization loss is small.

## Conversion and origin conditions

Use the recurrence L_0=1, L_1=z and (n+1)L_(n+1)=(2n+1)zL_n-nL_(n-1). If P(t)=sum_l b_l t^l, then H_m R^(p-m)P(t)=sum_l b_l r^(2(m+l))R^(p-(m+l))cos(2m theta), so k=m+l. The independently implemented recurrence and all summations use exact rational arithmetic.

The strain is partial_y U_2(0)=chi_xxyy(0), and a0=partial_y rho(0)=-chi_xxyy(0)-chi_yyyy(0). Only degree-four terms in the Taylor expansion of chi contribute. For k<=2, their radial coefficient is binomial(p_j-k,2-k). For m=0,1,2, the coefficients of x²y² and y⁴ in H_m r^(4-2m) are respectively (2,1),(0,-1),(-6,1). Thus strain is four times the first coefficient, and a0 is minus four times the first minus24 times the second. Terms with k>2 do not contribute. The exact normalized strain condition is strain=1-c.

## Full-plane sectors

At infinity,

r^(2k)R^(p_j-k)=r^(2p_j)sum_(q>=0) binomial(p_j-k,q)r^(-2q).

Termwise differentiation of each homogeneous harmonic uses

partial_x[r^s cos(n theta)]
= r^(s-1)((s+n)cos((n-1)theta)+(s-n)cos((n+1)theta))/2,

partial_y[r^s cos(n theta)]
= r^(s-1)(-(s+n)sin((n-1)theta)+(s-n)sin((n+1)theta))/2,

and the corresponding sine identities. Product-to-sum identities form the advective product. The residual F=(cX+U) dot grad rho-rho has sectors r^(gamma-h delta-2q)E_(h,q)(theta). The h index of an interaction between branches i and j is i+j+1. Linear transport contributes (c(gamma-h delta-2q)-1) times the density coefficient of branch h.

For the fixed c, q>=2 has exponent below -3.4 and h>=6,q=0 is below -2. Consequently checking all q=0,1 and h through at least5 detects every forbidden sector. The identically zero (0,0) sector is included. Each angular coefficient is stored exactly, and the full-circle norm is sqrt(pi sum_(n odd) E_n²). A nonzero sector with exponent e>=-1 prevents F from being square integrable. A nonzero sector with e>=-2 also prevents the homogeneous H^-1 norm from being finite: for each nonzero odd angular mode, the exterior radial Green energy scales as integral r^(2e+3)dr. Distinct powers cannot cancel the leading nonzero power, and sine modes are orthogonal. At equality the integral diverges logarithmically.

## Dependencies and limits

This audit uses the independent coefficient recurrence in refit_audit/code/convert.py and the homogeneous derivative identities in sector_audit/code/sectors_flint.py. Their correctness and reproduction checks are documented in the adjacent topic proofs. The snapshot's files are copied into this lane and their SHA-256 hashes are checked before computation. No code from the candidate-producing lane is executed. Numerical enclosures use Arb; source decimal or floating values are comparison targets only. Passing these checks verifies necessary structural conditions, not the nonlinear existence hypotheses.

## Pointwise necessary correction test

Let s>0 and suppose the exact correction h has H^(2+s) norm at most r, with the usual Fourier multiplier (1+|xi|^2)^((2+s)/2). For an S1 field, h and its velocity U[h] are evaluated through the canonical Fourier realization. Fourier Cauchy-Schwarz and polar integration give

|h(X)|, |U[h](X)| <= C0 r,    |D h(X)| <= C1 r,
C0=[4 pi (1+s)]^(-1/2), C1=[8 pi s(1+s)]^(-1/2).

For the vector velocity the sum of the squared multiplier moduli is bounded by one; the gradient bound is the largest directional evaluation norm. These bounds also apply to any stronger correction norm that dominates H^(2+s). The independently audited proof and the Fourier normalization are recorded in the point_witness topic.

If rho+h is an exact stationary solution at the same c, expansion of its equation gives

0=F+(cX+U[rho]).D h-h+U[h].D rho+U[h].D h.

Consequently, at every point,

|F(X)| <= r[C1 |cX+U[rho](X)|+C0(1+|D rho(X)|)] + C0 C1 r^2.

A strictly positive difference between the left and right sides excludes the specified correction ball. It does not depend on sufficient linear inverse conditions and does not exclude a different radius or norm. Cartesian Taylor evaluation of the exact potential provides the fields used in the certificate. A separate radial derivative recurrence supplies an implementation cross-check, and frozen-source hashes identify the candidate.

## Candidates designed for the three-component space

For a candidate intended for the no-negative-norm framework, report the cancellations at exponents at least -1 separately from those at exponents at least -2. The exact membership argument in ../membership_contracts/PROOF.md shows that only (1,0), (2,0), (3,0) must vanish for the three-component energy and weighted third derivative. Surviving exponents between -2 and -1 are permitted there and prohibit the baseline negative norm. Therefore an `all_forbidden_zero=false` field in the original audit output refers to the baseline H criterion; it is not a rejection of the no-H candidate. Check the exact sector rows and state both conclusions explicitly.
