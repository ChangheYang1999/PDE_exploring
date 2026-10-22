# Whole-cell axis monotonicity for the canonical modal trial

Status: proof written before computation. Numerical conclusions are conditional until the recorded checks and independent output audit pass. This is a local geometric certificate, not a stationary PDE existence or exclusion theorem.

## Exact statement and inputs

Let rho be the exactly normalized finite modal trial in ../modal_repair/PROOF.md, with its canonical whole-plane inverse in ../modal_green/PROOF.md. Write rho=r^3 sum_{j=0}^{260} C_j(t) sin((2j+1)theta), t=log r, and C_261=0. The exact scalar is c_l=1/k with k=1615536043799051/9007199254740992. Define w(x)=c_l x+U_1(x,0) and mu(x)=c_l+partial_y U_2(x,0).

We consider the exact cell [exp(a),exp(b)] with

a=4844989642942217/2251799813685248,
b=4847141258835159/2251799813685248,
t_c=(a+b)/2=302879090680543/140737488355328,
h=(b-a)/2.

Each C_j is the exact spline polynomial on one original knot span containing [a,b], not a Taylor approximation. The output audit checks that no original knot lies in (a,b). The independently integrated 261 canonical density moments I_n,J_n at t_c, and the 262 degree-at-most-seven density polynomials C_j(t_c+delta), are taken from the exact dyadic ball records of ../residual_samples/evidence/sample_result.json, cell4102. That earlier result proved the moment enclosures from both infinite endpoints using the exact trial data, and checked their provenance and all finite modes. This certificate shares those audited endpoint moment enclosures; it performs two different continuations across the cell. It does not claim two independent integrations from infinity.

The proposed quantitative conclusion is w'(x)>10 on the entire exact cell and opposite strict signs of x w(x) at its exact endpoints. If the computed bounds are stronger, their explicit rational versions will be recorded. These imply exactly one zero of w on that cell. The prior local root bracket in ../modal_source/evidence/source_result.json is separately proved and will be checked to lie strictly inside this cell. No signs on other cells are asserted here.

## Reconstructed identities

For m=2n, n=1,...,261, the normalized canonical density moments satisfy

I=r^{-(m+4)} integral_0^r s^{m+3} C_{n-1}(log s) ds,
J=r^{m-4} integral_r^infinity s^{3-m} C_n(log s) ds.

Thus

I' = -(m+4) I + C_{n-1},
J' = (m-4) J - C_n.

The Green formula and integration by parts give the stream coefficient psi_n=r^4(J-I)/2. Therefore U_1(x,0)=-sum m psi_n/x, and

w=c_l r+(r^3/2) sum m(I-J),
F=r w=c_l r^2+(r^4/2) sum m(I-J),
mu=c_l+(r^2/2) sum m[(m+1)I+(m-1)J-C_{n-1}-C_n],
w'=2c_l-mu.

To verify the last two formulas without assuming stationarity, differentiate w using d/dr=r^{-1}d/dt and the two moment ODEs. Its derivative is c_l+(r^2/2) sum m[-(m+1)I-(m-1)J+C_{n-1}+C_n]. The divergence-free inverse gives w'+mu=2c_l. Also F_t-F=r^2 w'. These identities are purely kinematic; the trial need not solve the stationary density equation.

## Method A: finite closed polynomial particular solution

For y'=lambda y+s C(delta), C=sum_{j=0}^7 c_j delta^j, lambda nonzero and s=+1 or -1, put

P_j=-s sum_{l=j}^7 (l!/j!) c_l/lambda^{l-j+1}.

Then P'-lambda P=s C, by cancellation of successive terms. The exact solution is y(delta)=P(delta)+exp(lambda delta)[y(0)-P(0)]. For lambda=0 it is y(0)+s sum c_j delta^{j+1}/(j+1). Apply this with lambda=-(m+4),s=1 for I and lambda=m-4,s=-1 for J. This is a finite exact formula, with no exponential-series truncation. Arb evaluates exp with outward balls. Interval coefficients contain the exact polynomial; their correlations may be discarded for an upper bound.

Subdivide [-h,h] into a recorded integer number of exact rational subintervals. Direct interval evaluation of the finite particular solution can lose its cancellations, so evaluate that exact solution only at the exact subinterval center z_c. On the subinterval write z=delta-z_c, |z|<=d. Let M_C and M_Cp enclose |C| and |Cprime| there, and let y_c enclose the exact value at z_c. Variation of constants gives M_y=exp(|lambda|d)(|y_c|+d M_C). Since yprimeprime=lambda^2 y+s lambda C+s Cprime, Taylor's theorem with integral remainder gives

y(delta)=y_c+(lambda y_c+s C(z_c))z+error,
|error|<=d^2 [lambda^2 M_y+|lambda|M_C+M_Cp]/2.

This is a stable local affine enclosure with a second-derivative bound. It is independent of Method B's order-Q residual calculation. Interval Horner arithmetic bounds C,Cprime. The exact rational subintervals cover the whole exact cell. Evaluate endpoint signs separately by the finite closed formula at delta=-h,+h. No rounded radius is substituted into the exact endpoints.

## Method B: density ODE Taylor enclosure

Let v=delta/h in [-1,1], ell=lambda h and g_j=c_j h^j. The equation is y_v=ell y+s h g(v). For order Q>=8 define

p_q=y(0) ell^q/q!+s h sum_{0<=j<q} g_j j! ell^{q-1-j}/q!, 0<=q<=Q,

with g_j=0 for j>7. Coefficient cancellation gives the residual p'-ell p-s h g=-(ell p_Q+s h g_Q)v^Q. The exact error vanishes at v=0, so variation of constants gives, for |v|<=1,

|y(v)-p(v)| <= exp(|ell|) |ell p_Q+s h g_Q|/(Q+1).

For negative v the reversed integral obeys the same absolute bound. All quantities on the right are outward interval upper bounds. This provides an independently derived remainder, without reusing the numerics lane's Green Taylor models or Bernstein arithmetic. mpmath.iv evaluates it at the recorded precision, and evaluates p(v) on the same exact rational subdivisions. Every one of the 261 moments is included. A fresh higher-precision Arb calculation of selected subcells and endpoint data will audit the stored enclosures.

## Uniqueness and coverage

The canonical finite trial is C^1 on this closed positive-radius cell. If the certified derivative is strictly positive everywhere, w is strictly increasing by the mean value theorem. If F(exp(a))<0<F(exp(b)), multiplication by positive x preserves signs, so the intermediate value theorem produces a zero and strict monotonicity makes it unique. A separately verified root bracket strictly inside the cell identifies that zero with the previously isolated source candidate.

The numerics output prints a coarse outer enclosure [r_lo,r_hi]. Its right endpoint is obtained from an upper estimate for exp(b-a). It can be larger than exp(b); a certificate over [a,b] is not automatically a certificate over all radii up to that printed r_hi. Our conclusion concerns the exact cell. The discrepancy and its size will be recorded rather than silently enlarging the domain. Global axis signs require all remaining exact cells and both tails to pass separate checks. Neither local monotonicity nor a conditional global flow estimate establishes a full linear inverse.

## Verification evidence and limits

All imported records, scripts, proof text, run times, selected subintervals, exact rational output endpoints and reviewer exchanges are to be pinned by SHA256. Python-flint Arb and mpmath.iv provide independent outward transcendental arithmetic. The proof's endpoint moment dependency remains explicit. Actual Opus5.5 reviews the proof and final source/output bundle; its advice is checked rather than accepted on authority. A failed check is preserved with its cause before repair.

The first actual Opus5.5 proof review accepted the displayed ODEs, but its own illustrative integral definitions had an erroneous ds/s and an inner exponent shift. Those formulas are not used. The correct radial definitions are displayed above and agree with the already audited Green proof. Its sentence that the factor m cancels in U1 is also not adopted: m remains in the finite sum. The later stable Method A refinement and exact-span check are included in the final source/output review.
