# Smoothness conditions for the polar representation near the center

Status: independent audit of the formula in NUM_REPORT.md and the current serialization source. This diagnoses representations and intermediate iterates, not existence or nonexistence of B2 profiles.

## 1. Necessary Taylor structure

Use x=r sin(phi), y=-r cos(phi). If a Cartesian function F is smooth at the origin, the coefficient f_k(r) of cos(k phi) in its angular expansion has, at every finite Taylor order, only powers r^(k+2j), j>=0. In particular f_k=O(r^k), and the k=0 coefficient has no linear radial term.

Proof. Taylor expand F in x,y with the differentiable remainder to any chosen finite order. A homogeneous polynomial of degree n restricted to the circle is a trigonometric polynomial of modes at most n, all of parity n. Integrating against cos(k phi) removes every term except n>=k with n-k even. The remainder estimate passes through the angular integral. Since the Taylor order is arbitrary, the assertion holds at every order. No claim that a smooth Taylor series converges is needed.

For a smooth even-in-x Theta vanishing on x=0, repeated one-dimensional division in x gives a smooth F with Theta=x^2 F. For a smooth odd Omega, Omega=xG with smooth G. Thus both divided fields must satisfy these angular Taylor restrictions. Smoothness on the invariant axis away from the origin does not imply this center property.

## 2. The radial map and a directly detectable defect

The documented map is t=1-(1+r/L)^(-1/beta_b), so t=r/(beta_b L)+O(r^2). Take a finite number of angular modes and spline degree d>=1. Consider the zero angular mode D(t) C_0(t), where D=(1-t)^p and C_0=sum_j c_(0j) B_j(t) is a clamped spline. At t=0, C_0(0)=c_(00), and

    C_0'(0)=d [c_(01)-c_(00)] / k_(d+1),
    q = [C_0'(0)-p c_(00)]/(beta_b L).

Here d is the spline degree and k_(d+1)>0 is its first positive knot, with zero-based indexing. Therefore the zero mode is c_(00)+q r+O(r^2). A nonzero q contradicts Cartesian smoothness of the divided field.

For either representation discussed below, the angular modes k>=1 start at least at r^min(k,2). On the x-axis, odd k vanish because cos(k pi/2)=0. All even k>=2 contribute O(r^2). Consequently the original fields have the one-dimensional forms

    Theta(x,0)=a0 x^2+q_F x^2|x|+O(x^4),
    Omega(x,0)=b0 x+q_G x|x|+O(x^3).

The remainders on either open half-axis are analytic on the interval before the first positive knot for these spline formulas, so they may be differentiated at the indicated order. The one-sided third derivatives of Theta tend to +/-6q_F and the one-sided second derivatives of Omega tend to +/-2q_G. If q_F or q_G is nonzero, the respective field is not C^3 or C^2 at the origin. This defect is not removed by an exact point value a0=1. Conversely q_F=q_G=0 is only necessary, not sufficient: higher odd radial powers and high angular modes must also obey all the Taylor restrictions in Section 1.

## 3. Two source versions, the same obstruction

NUM_REPORT.md describes f_k=D t^min(k,2) sum_j c_(kj) B_j. The source bq3core.py read at 14:06 UTC instead uses f_k=D sum_(j>=min(k,2)) c_(kj) B_j, with no additional t power. Its modification time is 13:59:59 UTC, after the running char2 job began at 13:43:58 UTC. The saved state has no source hash or representation version. The report formula cannot therefore be assumed to identify every off-center field in that state without further provenance.

Both formulas have exactly the same k=0 component and origin values. Both also permit high modes k>=3 at order r^2, contrary to the necessary r^k behavior. Removing the first two clamped coefficients improves vanishing order but does not enforce the correct angular Taylor structure.

For the saved intermediate state read at 14:04:57 UTC, hash 087f1d6951084420c6621d40c7a0890feb6a5d28bcbb1133694c1c42668b4a78, the independently computed zero-mode coefficients are

    q_F = 0.0673428486178,
    q_G = -6.75233411032,
    a0 = 0.999921888626,
    b0 - 4/beta = -0.0478351428916,
    beta = 2.565219672568257.

Independent angular averaging of value samples at radii 1e-2 through 1e-9 tends to the same q_F and q_G. This intermediate coefficient state fails the smooth-center requirement under either recorded version. It is not a submitted successful candidate. The result does not assert that its later iterates or a repaired representation must fail. Evidence is in verification/numerics_char2_origin_20261020T1404.json and candidate_snapshots/num_char2_20261020T1404/.

## 4. A compatible alternative map

A radial coordinate preserving smooth Taylor powers is

    t_new=1-(L^2/(L^2+r^2))^(1/(2 beta_b)).

It is analytic in r^2 near zero and has the same far-field scale 1-t_new~r^(-1/beta_b). Use angular factor

    (r/sqrt(L^2+r^2))^k cos(k phi).

The numerator r^k cos(k phi) is a homogeneous polynomial in x,y. Multiplication by any smooth function of r^2 therefore preserves Cartesian smoothness at zero. The factor remains bounded at infinity, so envelopes (1-t_new)^(beta_b+2) for F and (1-t_new)^(beta_b+1) for G retain the intended leading far-field exponents. The full subleading expansion changes: the radial map now has corrections in r^(-2), while the old map had corrections in r^(-1); endpoint spline powers still supply their r^(-j/beta_b) ladder. For a small first positive knot h, its radius changes from approximately beta_b L h to L sqrt(2 beta_b h), which changes resolution near the center. This is a representation proposal, not a convergence claim. Fifth-degree splines at ordinary simple interior knots are only C^4; exact C^infinity would require smoother radial functions or a controlled smoothing step. Their finite regularity should be stated when they are used as numerical approximants.

## 5. Characteristic reconstruction has a separate domain hypothesis

For beta>2, the local source-jet formula reconstructs Theta on the backward basin of the origin. A complete numerical use must record every orbit that does not enter the prescribed small center neighborhood and must not assign center data to a different backward limit. There is no theorem here that the origin basin covers the plane.

For beta=2, the required local zero curve contains nonzero points arbitrarily close to the origin. Each such point is an equilibrium and its backward orbit stays there. A procedure requiring every point to enter an arbitrarily small origin ball therefore cannot represent that branch globally with only the origin jet. Data along a stagnation curve or an analytically justified replacement are required. This is a limitation of that reconstruction, not a beta=2 nonexistence theorem.

Dependencies: finite Taylor expansion and trigonometric orthogonality, smooth one-dimensional division, the elementary clamped-spline endpoint derivative formula, and the previously proved beta=2 zero curve. No fitting-lane implementation is imported or executed by the verifier reader.

Audit 2026-10-20T14:26:06.569409+00:00: actual claude-opus-5-5 independently confirmed the calculation and alternative map in opus_reviews/04_polar_regularization/answer.md. The explicit finite-mode, local-interval, necessary-only, and leading-tail qualifications above incorporate its checked comments.
