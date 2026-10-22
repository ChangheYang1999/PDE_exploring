# Scope audit of the entered lineage-one Jacobian report

## Statements and hypotheses

This packet audits NUM_REPORT section7m(ii)(g), frozen below, against P234's independently recomputed finite arrays. The state has 1332 active coefficients, degree-five splines on56 intervals with grade3/2, L=3/2 and radial exponent beta=3.0060477873545817. The report describes the stored forward-difference matrix J_h of a fitted forced map, not an exact continuum derivative. P234 already checks its linear algebra. This packet does not repeat that computation or promote the approximate state to a root.

Two exact scope statements are needed. First, finitely many difference quotients at nonzero steps do not determine the derivative at the base point in the class of smooth maps. In particular, an unstable difference matrix does not alone imply that the exact local Picard iteration is unstable or that accelerated mixing caused observed convergence. Second, squared coefficient energies assigned to large-radius spline indices are not the physical mass of the represented field and do not establish support at their Greville radii. The support of each B-spline must be read from its knots.

## 1. Smooth counterexample for the sampled derivative inference

Let h_min>0 be the smallest of finitely many positive forward-difference steps. Fix0<delta<h_min. For0<=s<1 set chi(s)=exp(1-1/(1-s)), and for s>=1 set chi(s)=0. The composite chi(x^2/delta^2) is smooth on the real line: it is smooth near0 and is flat at x=+-delta, since exp(-1/u) extended by0 is smooth and flat at u=0. Define

    T(x)=2x[1-chi(x^2/delta^2)].

Then T(0)=0 and T'(0)=2[1-chi(0)]=0. By continuity of T', there is a neighborhood of0 on which |T'|<1/2. The mean-value theorem gives |T(x)|<=|x|/2 there. Thus iteration from a sufficiently small point stays in that neighborhood and converges geometrically to the exact fixed point0. Nevertheless, every tested step h>=h_min has chi(h^2/delta^2)=0 and

    [T(h)-T(0)]/h=2.

The sampled scalar matrix has spectral radius2 and its values agree across every tested step. This proves that even perfect agreement of a finite step study does not rule out a locally contractive smooth map without a derivative error estimate or further assumptions. It is a counterexample to the inference, not a model of NUM's particular fitting map and not evidence that its actual derivative is stable. The observed Anderson run and the unstable stored matrix may be reported separately as consistent empirical facts.

## 2. Coefficients, spline support and physical norm

For a degree-five B-spline B_j with clamped knot vector (t_i), its support is [t_j,t_(j+6)], and it is positive on the open nonempty knot intervals inside that support. The Greville parameter is the arithmetic mean of t_(j+1),...,t_(j+5). Its physical radial image is a representative point, not the support endpoint. The map r(t)=L((1-t)^(-beta)-1) is strictly increasing on[0,1). Therefore the support in r is exactly the image of those endpoint parameters, with infinity at1.

In particular, a coefficient vector supported on one outer radial index represents a field that is generally nonzero throughout the interior of that spline's radial support, including below its Greville radius. Squared Euclidean coefficient energies sum |c_kj|^2; the physical squared norm is a quadratic form c^T H c, where H contains radial Jacobians, envelopes and nonzero overlaps of adjacent B-splines. It is not the diagonal identity form. The native coefficient and physical norms therefore measure different quantities. Reported concentration in the last three coefficient indices can be retained as a coefficient statement, with Greville radii explicitly labeled as proxies and no support assertion.

## 3. Matrix interpretation and dependencies

For A=I-J_h, nonsingularity and singular values are finite-array properties. If the exact smooth map has a nearby fixed point and the true augmented derivative there is nonsingular, the implicit-function theorem applies at that root. Neither existence of that root nor persistence of the sampled ranks follows solely from a small residual. P216 gives a separate exact no-root counterexample with the same affine scalar mismatch equation. At the current stored point, m_beta is nonzero and a linearized tangent exists as an array kernel; it is not a proof of an actual branch or stationary point. A comparison to the sampled lineage-two vertex should retain that qualification.

Dependencies: P234 for the independently recomputed matrices, P216 for the root warning, elementary smooth cutoff calculus and the mean-value theorem, and the standard definition and support property of the specified B-spline basis. New checks below freeze the report, verify numerical rounding against P234, and compute actual support endpoints and Greville proxies. They are finite arithmetic controls. The exact statements above precede them. No formal proof assistant is used. The complete B2 problem remains OPEN.
