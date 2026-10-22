# Canonical meaning of the complete refined radial models

Written 2026-10-21T20:28:31.953517+00:00 before this topic's new code. This is a conditional composition theorem and acceptance protocol. No full radial result has yet completed.

## Exact statement and hypotheses

Use the exact normalized finite modal trial of topic15, based on data_exact/modal_v2.json SHA57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6. Its scalar normalization is the exact finite real defined there, and its dependent joining coefficients are recomputed exactly. Use the canonical whole-plane Green convention, with no adjustable harmonic xy strain. Topic166 independently proves the qualitative finite-mode canonical integral definition and regularity. It does not provide numerical moment enclosures.

Let t=log r. Let t_0,...,t_7809 be the exact rational partition in research/middle_residual/evidence/partition_exact.json, SHA56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2. Its1558 parent spans are the original distinct spline knots and its child intervals are exact equal subdivisions. Let h_c be the declared positive scalar upper bound on t_(c+1)-t_c and E_c the declared positive interval containing exp(t_c).

Assume the following accepted finite results, with all their unchanged files and mandatory supplements. Topic99 proves every local factor Taylor coefficient T_(c,k,j), all7809cells, k=0,...,7 and j=0,...,259, belongs to the corresponding box in cert_green.npz. Topic98 proves every canonical dimensional A_n(t_c), B_n(t_c), all7810boundaries and n=1,...,261, belongs to its box in the same file, conditional on the canonical moment archive hypothesis. Topic162 must have a completed actual full verdict proving its degree12 P/R coefficient and remainder membership on all7809cells, for every point in each full input box. This requires its full fresh computation, candidate regeneration, independent particular audit, replay, completed actual review and later independent adjudication. Preparation and four-cell smoke output do not satisfy this hypothesis.

The canonical moment hypothesis is that the I_n(a),J_n(b) balls at every original span endpoint in original_knots.jsonl.gz SHA c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648 contain the defining exact moments of this trial. H polynomial membership is already supplied by99. This topic retains the I/J hypothesis even if a separate independent archive computation later closes it; that later composition must cite its actual accepted result explicitly.

For every c=0,...,7808 and n=1,...,261 the conclusion, after all acceptance checks below, is that on0<=u<=t_(c+1)-t_c,

 P_n(t_c+u)=2n psi_n(exp(t_c+u))/exp(2(t_c+u)),
 R_n(t_c+u)=psi_n'(exp(t_c+u))/exp(t_c+u)

belong to the corresponding runtime degree12 interval-coefficient polynomials plus their fixed symmetric remainder intervals authenticated by162. The prime on psi is differentiation with respect to r. Their degree0through12 Taylor coefficients at u=0 belong to the stated coefficient boxes. All adjacent actual child cells cover the complete finite middle annulus. This conclusion is conditional only on the stated canonical archive membership and the accepted finite computational dependencies, not on any independence assumption about true coefficient errors.

## Independent reconstruction of the canonical radial system

Write rho=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta), with H_261=0. The canonical scaled integrals are

 I_n(t)=integral_-infinity^t exp(-(2n+4)(t-s))H_(n-1)(s)ds,
 J_n(t)=integral_t^infinity exp(-(2n-4)(s-t))H_n(s)ds.

Their derivatives are I_n'=-(2n+4)I_n+H_(n-1), J_n'=(2n-4)J_n-H_n, and psi_n(r)=r^4(J_n-I_n)/2. Absolute convergence and this normalization are proved analytically in166 with its mandatory Green correction. Put m=2n and S=(H_(n-1)+H_n)/2. Define

 A=e^(4t)(S-mI_n), B=e^(4t)(mJ_n-S),
 F=[(4-m)H_(n-1)+(4+m)H_n+H'_(n-1)+H'_n]/2.

For A, differentiation gives e^(-4t)A'=4S+S'-4mI-m[-(m+4)I+H_(n-1)] =4S+S'+m^2I-mH_(n-1). The expression -m e^(-4t)A+F has the same H coefficients and derivative term. Hence A'=-mA+e^(4t)F. The same substitution for B gives B'=mB-e^(4t)F. The sum gives A+B=2m psi_n. Differentiating the displayed psi formula gives B-A=2r psi_n'. These are exact identities without numerical approximation.

Set E=exp(t_c), q_+=B(t_c+u)/(E^2 exp(2u)) and q_-=A(t_c+u)/(E^2 exp(2u)). Then

 q_+'=(m-2)q_+-E^2 exp(2u)F(t_c+u), q_+(0)=B(t_c)/E^2,
 q_-'=-(m+2)q_-+E^2 exp(2u)F(t_c+u), q_-(0)=A(t_c)/E^2.

The desired P=(q_++q_-)/2 and R=(q_+-q_-)/2 follow. These are exactly162's finite input ODEs. Their solution exists and is unique by the explicit formula q(u)=exp(lambda u)[q(0)+sign E^2 integral_0^u exp((2-lambda)v)F(t_c+v)dv]. Subtracting two such solutions with the same data also proves uniqueness directly.

## Forcing map, input identity and application

With a_j=0 outside0<=j<=259, the exact angular conversion is

 H_0=(2a_0-a_2)/8,
 H_1=(2a_0+a_1-a_2-a_3)/8,
 H_j=(a_(j-1)+a_j-a_(j+1)-a_(j+2))/8 for j>=2.

Indeed x^2y/r^3=(sin(theta)+sin(3theta))/4. Multiplication by cos(2j theta) scatters the signed odd frequencies1+2j,1-2j,3+2j,3-2j, each with signed coefficient1/8. Collecting them gives precisely the displayed rows including repeated low frequencies. Substitution into F gives a rational linear form in T_(c,k,j), with derivative weights k+1 from T_(c,k+1,j), and no derivative term at k=7. For each collected scalar linear form sum w_l x_l on independent intervals [b_l-r_l,b_l+r_l], its exact image is [sum w_l b_l-sum abs(w_l)r_l, sum w_l b_l+sum abs(w_l)r_l]. The triangle inequality gives containment and choosing endpoints according to the coefficient signs attains each endpoint. Consequently162's exhaustive whole-box F-image tests require no additional canonical forcing assumption once the T boxes are linked.

This topic's independent artifact reader will compare all seven original input arrays per cell, T_mid,T_rad,A_mid,A_rad,B_mid,B_rad and scalar, with the corresponding authenticated162manifest hashes. It reads original ZIP/NPY bytes directly without NumPy or any162source import. Thus it has a different input path from162's NumPy array-slice auditor. Each NPY header must specify finite-dimensional C-order little-endian float64 of the exact declared shape. It consumes every entry of each archive member, so an early EOF, trailing bytes, wrong shape or unsupported representation is rejected. It hashes each contiguous cell record and compares every selected manifest identity. It also reconstructs the exact parent and child endpoints directly from hexadecimal original knots and rational partition data, and decodes the scalar h by integer IEEE754 fields. All exact child widths must be positive and at most h. The saved row's exact endpoints must match this partition. Canonical A/B and T membership are inherited from98/99, on these same cells and dimensional conventions.

The actual exp(t_c) membership and all F, P and R candidate containments come from162's accepted complete two-method computation. This topic does not rerun those millions of numerical comparisons or replace them by witness hashes. Its new exact symbolic audit independently constructs all forcing weights and the canonical ODE identities by two finite algebraic routes. Its new byte audit establishes input identity; mathematical membership is supplied by the accepted finite lemmas. It verifies every pin of98,99,166and162 before composition, checks162's complete7809-cell/261-mode/degree12count and its independent closure scanner's54,663original input hashes, and binds the actual accepted verdict hashes in its output. No unauthenticated historical numerical run is identified with these runtime models.

Select the true canonical T,A,B,E values in the identified boxes. The whole-input-box theorem of162 contains this possibly correlated point. Its ODE solution equals the true canonical solution by the derived identity and uniqueness. The theorem holds on[0,h_c], hence on the actual child interval. The artificial overhang beyond t_(c+1) uses a polynomial extension only and is not identified with the next true spline span. Shared endpoints and the exact complete partition give coverage of the closed finite middle annulus. This proves the conclusion.

## Scope and acceptance

A four-cell diagnostic on0,2955,4102,7808 may validate the new parser and finite identity checks against frozen smoke records. It cannot accept this full theorem. The full check must refuse to run without an actual completed162verdict, and a new actual-output review and later own adjudication must precede any final167verdict. This proof and any preparation review are not a completed full result.

No angular tensor product assembly, Bernstein spatial classification, full flow inequality, physical residual derivative majorant, infinite tail, X3 distance, global inverse, nonlinear closure, solution or decisive IPM endpoint follows. In particular107's angular result and162's radial result alone do not certify their complete physical product computation.
