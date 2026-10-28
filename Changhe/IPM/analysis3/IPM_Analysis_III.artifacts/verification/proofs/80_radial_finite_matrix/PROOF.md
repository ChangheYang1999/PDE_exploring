# Independent matrix check for the radial L2 finite section

## Exact conditional statement

Use the radial Hilbert space H_R and maximal transport domain D_rad of
proof 76. The operator is Lfix=(V.grad-1)+U[.].grad rho. Let phi_j be the
169 trial columns specified by the archived metadata: degree-seven
radial B-splines, exact C3 endpoint extensions by inner and outer
powers, and the single cutoff cubic column J, with angular factors
cos^2(theta) sin(theta) cos(2m theta), 0<=m<4. There is no varying-tail,
KP, TAU, or normalization-strain column in this section.

The test vectors are e^(3t) psi_i(t) sin((2N+1)theta), with69 active
compact radial splines and 0<=N<12. Let P_N be the H_R orthogonal
projection onto the trial space and Q_M the H_R orthogonal projection
onto this test space. Suppose the exported matrix intervals enclose
all of the exact pairings defined below, and the trial columns belong
to D_rad. Then the acceptance calculation proves

 ||Q_M Lfix h||_H_R >= 0.510914 ||h||_H_R

for every h in the trial space. The decimal is the exact rational
255457/500000. This is a finite-dimensional assertion. The enclosure
hypothesis is not independently established by this matrix calculation.
Neither this statement nor its enclosure hypothesis gives a bound on
the continuum complement or proves injectivity of Lfix.

## Pairings and angular normalization

Write h=e^(3t) sum_m b_m(t) Phi_m(theta), where
Phi_m=cos^2(theta)sin(theta)cos(2m theta). Spatial area contributes
e^(2t) dt dtheta, so all radial pairings have weight e^(8t+mu_R(t)).
The exact angular trial Gram is

 A_mm'=(I(m-m')+I(m+m'))/2,
 I(d)=pi/8 if d=0, pi/32 if |d|=1,
      -pi/16 if |d|=2, -pi/32 if |d|=3, and0 otherwise.

This follows by expanding cos^4(theta)sin^2(theta) as
1/16+cos(2theta)/32-cos(4theta)/16-cos(6theta)/32 and using Fourier
orthogonality. Thus G_ij=<phi_i,phi_j>_H_R is the exported domain Gram
without any additional mode weight or scalar-coordinate Gram.

For each odd output mode the common test Gram is

 H_ii'=pi integral psi_i(t)psi_i'(t)e^(8t+mu_R(t))dt,

where the prime on the index i' is an index, not a derivative. If
Lfix phi_j=e^(3t)sum_N g_Nj(t)sin((2N+1)theta), set

 (B_N)_ij=pi integral g_Nj(t)psi_i(t)e^(8t+mu_R(t))dt.

The squared projected norm for coefficient vector x is

 x^T K x,  K=sum_(N=0)^11 B_N^T H^(-1) B_N.                 (1)

Both pi factors are already in the exported entries. There is no
extra division by an angular Sobolev weight, unlike the S0 section
in proof 62. Inactive first and last test splines are deleted exactly.

## Verified congruences

Decode every exported ball as midpoint m*2^e plus radius r*2^er, with
all four numbers integers. Reconstruct G,H and all B_N independently
of the numerics team's certification code. From high-precision
midpoint Cholesky calculations, choose exact dyadic upper triangular
matrices T and S with nonzero diagonal. They are invertible, regardless
of the accuracy of the approximate Cholesky factors used to choose them.

Use outward interval arithmetic to form

 G1=T^T G T, H1=S^T H S, C_N=S^T B_N T.

The acceptance inequalities ||G1-I||_infinity<1 and
||H1-I||_infinity<1 prove both exact symmetric Grams positive definite.
Direct ball inversion of H1 and (1) give

 K1=sum_N C_N^T H1^(-1) C_N.

This is a congruence of the exact projected image Gram, not an
approximate inverse lower bound. For s=255457/500000, put
M=K1-s^2 G1. Choose a floating Cholesky factor L of its midpoint as an
exact dyadic lower triangular matrix with nonzero diagonal. If the
ball calculation proves

 ||L^(-1) M L^(-T)-I||_infinity<1,

then every exact symmetric matrix M enclosed is positive definite.
Indeed the spectral norm of the symmetric error is bounded by its
infinity norm. Thus K1>=s^2G1, proving the finite-section inequality.

Floating arithmetic is used only to choose exact change-of-basis
matrices. All accepting inequalities use exact integers and Arb balls.
The code snapshots the input metadata, reported certificate and matrix
export, records their hashes and checks the original density identity.

## Conformity and limits of this check

The rational Vandermonde endpoint construction gives exact C3 joins,
and the interior B-splines have C6 joins. Near0 the ordinary columns
are O(r^5) and J is exactly x^2y. At infinity the slowest ordinary
column is O(r^(2k-1)), with 2k-1<-3/8. These bounds and their first
scaled derivatives put the columns and their transport images in H_R;
V has bounded scaled coefficients. Weighted Riesz boundedness then
puts U[phi_j].grad rho in H_R. Thus these are conforming trial columns
when constructed by the stated exact prescription. Test vectors need
only be in H_R for the orthogonal projection; the retained ones also
have zero extensions in H1 locally.

This analytic description does not establish that every exported ball
was computed from the prescribed column. Full original-data entry
recomputation, coverage of every integration cell, and the exported
arithmetic pipeline are separate audits. The present verdict remains
conditional on the exact-pairing enclosure hypothesis.
