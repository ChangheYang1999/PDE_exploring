# Full-plane interval values of the X3 velocity on the axis

Status: CONFIRMED point enclosures after exact cover/rule checks, full Arb real quadrature, an independent mpmath.iv complex remainder computation, final provenance audit and actual Claude Opus5.5 follow-up review. This is a trial-field point certificate, not an existence theorem.

## Statement and exact input

Use the exact binary64-input X3 function defined in ../canonical_inverse/PROOF.md and data_exact/x3.json. Its exponent is exactly

S(q,theta)=sum_{m=0}^{200} chi(s)^{max(m-1,0)} b_m(q) cos(2m theta) + s^{p/2} cos(theta)^{p-2} sin(theta)^2 T(2q-1),

where chi(s)=s/[r0^2+(1-r0^2)s], p and all spline and Chebyshev coefficients have their exact input definitions. The chi exponent is max(m-1,0), including zero for both m=0 and m=1. For a positive exact rational x, set beta(q)=L^2 s/[L^2 s+x^2(1-s)], where s=1-(1-q)^{2/(1-k)}. By ../axis_control/PROOF.md,

U_1(x,0)=x P integral_0^1 integral_0^{pi/2} exp(S(q,theta)) Q(beta(q),theta) dtheta dq,
P=4L^2/[pi(1-k)],
Q=cos^2(theta)sin^2(theta) beta^2 [1-4beta^2 cos^2(theta)]/[1-4beta(1-beta)cos^2(theta)]^2.

The removable or integrable singular behavior at q=q(x),theta=0 is treated by removing a radial strip and bounding its integral analytically. No quadrature samples are used as substitutes for a singular-region bound.

## Removed strips

Choose exact rationals 0<q_a<q(x)<q_b<1, verified by outward evaluation of q(x). Since the angular integral of |Q| is at most 3pi/16 uniformly in beta, and exp(S)<=M=exp(Csum+C_T B_p), the absolute integral of the whole removed strip is bounded by

E_hole=(q_b-q_a)(3pi/16)M.

The two radial endpoint strips of combined width 2eta have the same bound with q_b-q_a replaced by 2eta. This bound covers their entire angular range and has no hidden principal-value cancellation.

For the angular strip pi/2-d<=theta<=pi/2, put t=pi/2-theta. For real beta in [0,1], the denominator 1-4beta(1-beta)cos^2(theta) is at least 1-t^2. Thus

|Q| <= t^2 (1+4d^2)/(1-d^2)^2,
exp(S) <= exp(Csum+C_T d^{p-2}).

Its integral over all q is bounded by the last exponential times d^3(1+4d^2)/[3(1-d^2)^2]. Double-counting removed-strip intersections is harmless.

## Radial complex remainder

Partition each retained radial knot span into intervals of length ell=2h. Extend that span's degree-seven spline polynomial to the rectangle with real center midpoint and radius 3h, and imaginary radius 2h. This rectangle contains every disk of radius R=2h centered on the interval. Verify the analytic power branches and nonzero rational denominators on the entire rectangle.

Let beta now be complex. Put D_c=(1-2beta)^2 and verify Re(D_c)>0. For every real theta,

Re[1-4beta(1-beta)cos^2(theta)] = sin^2(theta)+Re(D_c)cos^2(theta) >= d_q,
d_q=min(1,inf Re(D_c))>0.

Consequently |Q| <= cos^2(theta)sin^2(theta) B^2(1+4B^2)/d_q^2, where B bounds |beta|. If M_q bounds exp(|S|) on the radial rectangle with real theta, integrating the angular weight gives pi/16. The radial Gauss error on the cell is bounded by

ell C_n M_q B^2(1+4B^2) pi/(16 d_q^2),
C_n=(n!)^4/[(2n+1)((2n)!)^2].

This is the Cauchy-Gauss bound from ../canonical_inverse/PROOF.md with ell/R=1. The analytic strip may cross knots, since only the polynomial extension of the original real span is used.

## Angular complex remainder

On the retained real radial domain, monotonicity of beta gives |1-2beta|>=delta_0>0, using the two sides of the removed strip. Choose an angular interval of physical length d_j=2h_j. Its complex rectangle has real radius 2h_j and imaginary radius h_j. Write z=t+iv. For real beta, delta=|1-2beta| in [delta_0,1], and

Re[sin^2(z)+delta^2 cos^2(z)]
=sin^2(t)+delta^2 cos^2(t) -(1-delta^2)cos(2t)sinh^2(v)
>=delta_0^2+(1-delta_0^2)sin^2(t)-sinh^2(h_j).

Compute a strictly positive lower bound d_theta for the last expression throughout the real projection of the rectangle. Then

|Q(beta,z)| <= |cos(z)|^2 |sin(z)|^2 [1+4|cos(z)|^2]/d_theta^2.

The real radial spline convexity bounds exp(S) in this angular rectangle exactly as in the scalar-strain certificate. Also verify Re(cos z)>0 to fix the fractional angular power branch. The angular cell error is bounded by d_j C_n 2^{2n} times these kernel and exponential bounds. Summing is valid because all radial quadrature weights are positive and their total is at most one.

## Final enclosure and scope

The real tensor Gauss sum is evaluated using outward Arb balls with exact input conversion. Add a centered ball whose radius is the sum of both complex remainder bounds and all removed-strip bounds, then multiply by xP. Combine with the independently audited strain interval to enclose bar-w(x)=x(1+bar-c)/3+U_1(x,0).

The algorithm records exact partition endpoints, all error components, input and script hashes, and arithmetic precision. It is independent of the numerics lane's modal Green recurrence and floating endpoint primitive. A resulting point sign concerns the canonical X3 drift. Existence and uniqueness of an exact profile's source require the conditional neighborhood theorem in ../axis_control/PROOF.md; no statement of profile existence follows from this computation.

The uniform 3pi/16 strip bound is proved in ../axis_control/PROOF.md, section "Axis kernel and its angular integral". The singular point is q_star=1-(1+(x/L)^2)^((k-1)/2). The actual Opus 5.5 follow-up in ../../notes/reviews/axis_strip_resolution_response.md rederived J_0,J_1 and closed the earlier missing-reference objection.

## Independent complex coefficient majorants

A second implementation, code/audit_complex_iv.py, uses mpmath.iv at 65 decimal digits, exact rational Cox polynomials and absolute coefficient disc bounds. For the radial rectangle, |q-mid|<=sqrt(13) h, so a polynomial sum c_j(q-mid)^j has absolute value at most sum |c_j|(sqrt(13)h)^j. If interval wrapping prevents a branch or denominator check, the complex rectangle is subdivided; the original real integration cell and its polynomial remain fixed. Every final subrectangle must pass all checks.

The chi bound used in this implementation is valid because 0<r0^2<1 and Re(s)>0 on each verified complex rectangle. Set a=r0^2 and b=1-a. Then

|a+bs|^2=b^2|s|^2+2ab Re(s)+a^2 >= b^2|s|^2,

hence |chi|=|s/(a+bs)|<=1/b. The implementation takes the smaller of this bound and the direct interval quotient bound. Fractional powers use the verified right-half-plane branches, both for 1-q and s. In the angular calculation Re(cos z)>0 is checked explicitly.

The tensor error decomposition is (I_q-Q_q)I_theta f + Q_q(I_theta-Q_theta)f. The first term uses the radial analytic bounds integrated in real theta. The second uses uniform angular error bounds and the nonnegative radial Gauss weights, whose sum is at most one. There is no additional mixed remainder.

The second remainder computation finished at 2026-10-20T15:37:31Z, in 297.32 seconds. It checked 1041 radial cells and 1046 complex subrectangles at x=7, and 978 cells and 990 subrectangles at x=10. The angular partitions had 107 and 108 cells. Both recomputed enclosures are inside the public bounds below. This implementation reuses the single complete rigorous real tensor sum at each point; it is an independent error-bound computation, not a second entire quadrature. Final source/provenance audit is recorded separately.

| quantity | outward public enclosure |
| --- | --- |
| U_1(7,0) | [-54.520,-54.459] |
| canonical bar-w(7) | [-15.492,-15.432] |
| U_1(10,0) | [-41.680,-41.590] |
| canonical bar-w(10) | [14.07,14.17] |


## Library and immutable-run audit

The executed library versions were mpmath1.3.0, python-flint0.9.0 and FLINT3.6.0. The actual installed mpmath sources are snapshotted in evidence/library_libmpi.py and evidence/library_ctx_iv.py. The complex power dispatch is exp(y log x), with complex interval log formed from the real interval log of absolute value and interval atan2. The latter uses directed corner bounds on the right half-plane. Complex sine and cosine explicitly use real interval trigonometric and hyperbolic formulas. There is no point-evaluation fallback in the operations used here. The right-half-plane branch hypotheses are checked on every rectangle. As with Arb, the elementary outward arithmetic implementation is part of the trusted computational base; neither a finite test set nor the mathematical proof formally verifies either arithmetic library.

The mpmath1.3.0 documentation states the enclosure contract for iv.mpf and iv.mpc and also states that interval support is experimental. Its source location is `https://www.mpmath.org/doc/current/contexts.html`, accessed2026-10-20. For this reason the audit checks the particular dispatch paths actually used, rather than inferring that every mpmath function supports intervals. An additional180 interval-containment comparisons against384-bit Acb values are regression checks, not a proof of the libraries.

code/audit_library_and_provenance.py completed with PASS at2026-10-20T15:47:20Z. It checks the exact Cox recursion uses the physical coordinate q-mid, every retained cell lies in one original real knot span, exact rational tilings of both integration axes, the removed strips, input hashes, partition hashes, run settings and complete real-sum counts. It binds the complex and downstream audits to those same files. Full hashes and installed-source snapshots are in evidence/library_provenance_audit.json. The x=7 real sum comprises99,802,752 nodes and the x=10 sum94,639,104 nodes. The original x=7 run completed its sum before a later overly strict strain-hull assertion failed; code/finalize_logged_sum.py reconstructs the final enclosure from that completed logged outward sum, as separately audited. No failed partial quadrature is treated as complete.


Final review: actual Claude Opus5.5 accepted the closure of G1-G4 in ../../notes/reviews/axis_complex_closure_response.md. The independent verifier inspected the snapshotted dispatch formulas in addition to the executable string checks. The angular maximum is200, or201 modes, as the exact input states. The exponent formula above corrects a transcription that wrote maximum201 in that review packet; all executed loops use maximum200. code/audit_final_addendum.py records the input check, explicit q_a<q_star<q_b interval tests for both points, and immutable hashes of the earlier cover and downstream audits. Its output is evidence/final_addendum.json. The statement and public intervals are now CONFIRMED within the stated arithmetic trust base.
