# Independent global matrix-cover verification

## Claim and hypotheses

Let chi be the exact d2 potential defined by the copied rational generators in ../refit_audit/data/d2_generators.json, with c=4076476460239181/2251799813685248. Let rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), V=cX+u, and A=[[rho_y,-rho_x/2],[-rho_x/2,0]]. The verification target is

M=(2c+1)I+sym Du+A >= (19/5)I,
M_k=(1+c+V.grad log omega_k)I-k sym DV+A >= (1/2)I, k=1,2,

on the full plane, where omega_1=(1+r^2)^(-1/10) and omega_2=(1+4r^2)^(2/5). The target is not yet a conclusion until all leaves of the saved covers pass the independent interval calculation. The matrices and their derivative identities are derived in ../background_points/PROOF.md.

## Polynomial coordinates

Put t=r^2/(1+r^2), z=cos(2 theta), w=(1-t)^(delta/2), delta=1-1/c. The domain t in [0,1], z in [-1,1] covers a quadrant and its limiting origin and infinity. The eigenvalues of the matrices are unchanged by the S1 reflections, so a quadrant suffices.

The independent radial differentiation expresses each fourth potential derivative as

chi_ab = sum_j w^(j+1) sum_n P[j,n](t) trig(n theta), a+b=4,

after exactly dividing its numerator by t^2. For even angular n=2m, use cos(2m theta)=T_m(z) and sin(2m theta)=sin(2 theta) U_(m-1)(z), where T and U obey their usual three-term polynomial recurrences. Thus diagonal fields are ordinary polynomials in t,z,w, and each off-diagonal field is sin(2 theta) times such a polynomial.

The scalar e=(X.u)/r^2 is handled without numerical division. The identity e=-partial_theta(chi_xy)/r^2 follows from u=grad-perp(chi_xy). The second derivative chi_xy has only even sine harmonics; multiplying each sine coefficient by its negative angular frequency and dividing its radial numerator by t^2 gives the polynomial for e. Its value at the origin may depend on direction, but the only matrix occurrence of e is multiplied by t, so the matrix extends continuously there.

M-(19/5)I has diagonal constant 2c+1-19/5 and perturbations -2chi22-chi04 and chi22; its off-diagonal is chi31. M1-(1/2)I has diagonal constant 1/2-c t/5 and perturbations -chi04-t e/5 and -chi22-t e/5; its off-diagonal is chi13. Multiply M2-(1/2)I by the strictly positive factor 1+3t. Its diagonal constant is 1/2-c+(3/2+c/5)t; the perturbations are (1+3t)(chi22-chi04)+(16/5)t e and -2(1+3t)chi22+(16/5)t e. The off-diagonal is (1+3t)(3chi13-chi31)/2.

These formulas specify the exact polynomial reconstruction. The algorithm compares the independently reconstructed coefficient arrays with the prior arrays, but the acceptance bounds are computed from the new arrays.

## Polynomial range enclosure

For a polynomial of degrees at most d_t,d_z on a rectangle, transform each variable affinely to [0,1], then express the result in the tensor Bernstein basis. Every Bernstein basis function is nonnegative on the rectangle and the basis sums to one. Consequently, the polynomial lies between the least and greatest Bernstein coefficient. Arithmetic that encloses every coefficient therefore encloses the full polynomial, including all boundaries.

If a local power coefficient is a_k, its Bernstein coefficient at i is sum_(k<=i) a_k binom(i,k)/binom(d,k). The affine restriction of x^k from [a,b] to [0,1] has coefficient binom(k,l)a^(k-l)(b-a)^l at order l. These identities determine the matrix transforms used by the code.

For the branch variable w, the independent interval [ (1-b)^(delta/2), (1-a)^(delta/2) ] is valid on a t-cell [a,b]. Applying the same Bernstein transformation to the finite polynomial in w gives an unconditional enclosure, including cells with b=1.

## Correlated midpoint Taylor improvement

On a cell with b<1, put mu=(a+b)/2 and H=(b-a)/2. For a branch power q=j delta/2, Taylor's formula at mu gives

(1-t)^q = sum_(k=0)^N (-1)^k (q)_k (1-mu)^(q-k) (t-mu)^k/k! + R_q(t).

Here (q)_k is the falling factorial. A uniform error is

|R_q(t)| <= |(q)_(N+1)| H^(N+1)/(N+1)! times
max((1-a)^(q-N-1),(1-b)^(q-N-1)).

All bases are positive because b<1. Both signs of the exponent are covered by the maximum. The Taylor polynomial is represented in Bernstein form on the same t-cell. Multiplying a degree-d Bernstein coefficient B_i by a degree-N coefficient C_k contributes

B_i C_k binom(d,i)binom(N,k)/binom(d+N,i+k)

to output index i+k. Summing these products over branch powers retains their dependence on the same radial variable. The product remainder for each branch is bounded by its Taylor error times the maximum absolute Bernstein coefficient of the branch polynomial. Summing these errors encloses the whole field. The algorithm uses N=6 and a midpoint expansion; the archived verifier used a fourth-order expansion at the left endpoint.

Both the independent-w and correlated-Taylor bounds are valid. Their intersection may be used. A nonnegative bound from either method suffices; an inconclusive bound triggers further work, not a positive verdict.

## Matrix eigenvalues and complete coverage

Suppose a cell supplies diagonal lower bounds a,b and an off-diagonal factor q in [q_l,q_h]. Since the off-diagonal is sqrt(1-z^2) q up to a harmless sign, its magnitude is at most

C=max(|q_l|,|q_h|) sqrt(1-min_(z in cell)|z|^2).

The matrix is bounded below by

(a+b-sqrt((a-b)^2+4C^2))/2,

and also by min(a,b)-C. The larger of these lower bounds remains valid. This follows by monotonicity of the least eigenvalue under positive diagonal additions and by the explicit eigenvalue formula for a symmetric two-by-two matrix. Nonnegative lower bounds certify the stated target after reversing the positive factor 1+3t for M2.

Each saved cover consists of binary paths from the full rectangle. A letter t or T selects the lower or upper radial half, and z or Z selects the lower or upper angular half. The verification checks exact rational endpoints, absence of duplicate or ancestor leaves, and that every nonleaf has exactly the two children of one split axis. Induction on this finite tree proves that the leaves cover the complete rectangle. No numerical area sum is substituted for this tree check.

## Dependencies and scope

The dependencies are the exact profile reconstruction, the independent radial derivative recurrence, elementary trigonometric polynomial identities, Taylor's theorem with remainder, the Bernstein convex-hull property, and outward Arb arithmetic. All copied source data are hashed. The proof gives only these three matrix inequalities for the exact d2 profile. It does not certify the remaining derivative conditions or any residual threshold, and d2 still violates the fixed fourth-derivative cap in (W3).
