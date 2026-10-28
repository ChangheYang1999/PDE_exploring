# The high-space and graph-domain subsets of the pure spline section

## Exact statement and spaces

Use the original exact dyadic knot vector and the 34 clamped degree-seven coarse B-splines b_i of proof 198. For 4<=i<=29 and 1<=m<=3 let

 h_(i,m)=r^3 p(theta)b_i(log r)F_m(theta),
 p(theta)=cos(theta)^2 sin(theta),
 F_m(theta)=cos(2m theta)-(-1)^m.

Every spline is extended by zero outside the coarse knot interval [t_-,t_+]. Any positive fixed column scalings give the same spans below. Let P be the 78-dimensional real span of these functions.

Use the exact high correction and target spaces of proof 173. In detail, sigma=25/4, a_H is the fixed positive smooth radial weight, b_H=r^3 a_H, and

 H_full=E B_H direct-sum X_s, Y_H=E Gamma_H direct-sum X_s,
 E beta=r^3 p beta(t),
 B_H=R chi_0+a_H H^(29/4)(R), Gamma_H=a_H H^sigma(R).

The remainder norm is the sum in squares of ||h/b_H||H^(s(.)) and ||chi h/(b_H p)||H^sigma, with zero vertical cofactor traces. Here 41/20<=s<=sigma, s=sigma in the fixed vertical sectors, and chi equals1 on smaller vertical sectors. All weights are smooth and strictly positive on compact radial intervals. Thus on such a vertical sector the remainder must have its cofactor in local H^sigma. This requirement is weaker by one derivative than the scalar input requirement H^(29/4). It must not be replaced by that scalar requirement when the cofactor trace is zero.

Let A0 be the exact moving-tail, normalized operator of proof 174, on its maximal high graph domain

 D_H(A0)={h in H_full:A0 h in Y_H distributionally}.

Equivalently A0 h=L_ren h+c[h]m0, where L_ren h=(ell0 X+U[rho0]).grad h-h+U[h].grad rho0+c[h]H0, H0=chi0 X.grad rho0/3, and m0 is the fixed target-valued chart column. All canonical conventions are those of topics01 and174. The background is the exactly joined normalized modal trial, not the unmodified raw archive.

Then

 P intersect H_full = span{h_(i,m):6<=i<=27,1<=m<=3},       (1)
 P intersect D_H(A0) = span{h_(i,m):7<=i<=26,1<=m<=3}.     (2)

The dimensions are respectively66 and60. The full78-column section is conforming in the low realization of proof 198. Equations(1)-(2) concern only its intersection with the different high realization. They do not invalidate its low finite-section input Gram. No high operator norm or singular value is computed here.

The accompanying original-data check must verify the exact endpoint jets and interior C6 identities before these index ranges are accepted for the archived knots. The analytic proof does not use rounded jet comparisons.

## Endpoint regularity and the tensor product

For a clamped degree-seven B-spline with simple nonzero spans, b_i vanishes to exact order i at the left endpoint for0<=i<=7. This follows by induction in the Cox-de Boor recurrence, or from the first-span Bernstein-type triangular basis. The right endpoint has the reflected order33-i for26<=i<=33. The first nonzero coefficient has a fixed nonzero sign. Splines with supports separated from an endpoint vanish identically in a neighborhood of it. At every simple interior knot all these splines are C6. The independent exact check below records these facts directly for the original knots.

A compactly supported piecewise smooth function with a first nonzero derivative jump of orderq belongs to H^s(R) for s<q+1/2, and not to H^(q+1/2) locally at that jump. For the upper assertion, its q-th derivative is bounded and piecewise smooth with finitely many jumps. For0<tau<1/2 its fractional seminorm near each jump is bounded by a constant times integral_0^epsilon integral_0^epsilon (u+v)^(-1-2tau)du dv, which is finite; all remaining pairs are controlled by bounded derivatives and compact support. Lower Sobolev orders then follow by Fourier comparison. For the lower assertion the jump supplies the same integral with a positive lower bound and tau=1/2, which diverges. Smooth positive multipliers do not change the first jump order. The same assertions hold after multiplication by a nonzero smooth angular function on an open sector: localize there, integrate against a smooth angular test with nonzero pairing, and use the bounded map from the two-dimensional local Sobolev space to the one-dimensional radial one. The converse follows by tensor-product Fourier estimates.

Every F_m vanishes quadratically at the vertical axis. Hence every h in P has zero vertical cofactor trace, so its unique scalar coordinate in H_full is beta=0. The local high condition is therefore H^sigma for its angular cofactor, not H^(sigma+1). Away from the compact radial support all these inputs vanish; there are no radial weight or tail conditions to check for input membership.

If i>=6 and i<=27, all endpoint zero extensions are at least C5, with piecewise smooth sixth derivatives. Thus b_i belongs to H^s for every s<13/2, in particular H^(25/4). The interior C6 joins are more regular. Multiplying by the fixed smooth angular factors, cutoffs and radial weights gives the required fixed H^sigma sector norm, and global H^sigma controls the variable-order norm since s<=sigma. These functions belong to H_full.

Conversely write h as a combination of all78 columns. At the left endpoint the fourth radial cofactor jump is a nonzero constant times sum_m a_(4,m) F_m. Membership in H^sigma forces it to vanish, since sigma>9/2. The functions F_1,F_2,F_3 are linearly independent on every nonempty open angular interval: a trigonometric polynomial vanishing there vanishes identically, and its distinct highest frequencies then force every coefficient to be zero. Thus a_(4,m)=0 for everym. The fifth jump next forces a_(5,m)=0, since sigma>11/2. The identical right-end argument eliminates i=29 and28, in that order. This proves(1). Possible cancellation between different radial orders has been handled in increasing order; cancellation between angular modes does not enlarge the stated span.

## The high transport graph

Write the actual cylinder transport as W=q(t,theta)partial_t+vartheta(t,theta)partial_theta, where q=(ell0 X+U[rho0]).X/r^2. Its vertical-axis value is the strictly positive coefficient d(t)>=5.5752 verified for the actual modal trial in proof 76. In particular q is nonzero on an open vertical angular interval at each finite endpoint t_-,t_+. This is the only sign information used here. The exact background and all relevant angularly divided coefficients are C6 or better in t before one differentiation; their first-derivative products are locally H^s for s<13/2, by the finite-mode and exact-join regularity already checked in topics50 and126.

First take7<=i<=26. The spline b_i is C6 after zero extension and belongs to H^s for every s<15/2. Its first derivative belongs to H^s for s<13/2, which includes sigma. The exact transport image, after division by r^3 p, is

 q b_i' F_m+b_i[vartheta F_m'+(3q+(p'/p)vartheta-1)F_m]. (3)

The divided angular coefficient is regular by axis tangency and parity. Equation(3) is locally H^sigma in every vertical sector and has zero cofactor trace. The compact radial support controls all end weights. Away from the vertical sector, the same formula has fixed H^sigma regularity and hence the required variable-order regularity. Thus the transport image lies in X_s.

The remaining normalized coupling and chart terms lie in Y_H. One can use the bounded high coupling already proved for this exact realization. Its regularity is also direct for these finite angular inputs: the canonical velocity consists of finite angular Green modes whose radial equations have piecewise smooth coefficients; it is locally H^sigma after all indicated axis divisions, while grad rho0 has local H^sigma regularity since the density has exact C6 joins. Their products are H^sigma because sigma>1 on the two-dimensional cylinder. The axis traces themselves here have the same radial regularity from the finite-mode formulas. At the origin compact support of h gives an analytic velocity with linear strain c[h](-x,y); the normalized term cancels the cubic density part and leaves physical orderr^5, hence cofactor orderr^(2-9/5) after division byb_Hp. At infinity the compact input gives U[h]=O(r^-2), and grad rho0=O(r^(k-1)); after division byb_H=r^(-1/2) the output is O(r^(k-5/2)), which decays. Any fixed number of t or angular derivatives preserves these strict end powers. The fixed columnm0 belongs toY_H by proof 167. These observations justify full image membership, including both tails and the axis coordinate. They prove the inclusion from right to left in(2).

To prove the reverse inclusion start with h inP intersectH_full, so onlyi=6,...,27 occur. If anyi=6 coefficient is nonzero, the input's sixth radial cofactor derivative has a nonzero jump G(theta) at t_-. In(3), the first term therefore has a fifth-derivative jump q(t_-,theta)G(theta). The other transport terms are C5 there, so cannot cancel that fifth jump. The normalized nonlocal coupling and chart column already belong toY_H for this H_full input, by the same bounded-coupling argument and the finite-mode regularity just given. They cannot cancel a non-H^sigma singularity by addition of anH^sigma function. Becauseq is nonzero on an open vertical interval andG is a nonzero trigonometric polynomial, the fifth jump does not vanish on some smaller open interval. The transport image fails even localH^(11/2), hence failsH^sigma. Membership of A0h inY_H is impossible. Thus everyi=6 coefficient vanishes. The reflected argument at t_+ eliminatesi=27. The remaining span is exactly that in(2).

This argument does not require the image axis trace to be nonzero: the transport contribution has zero trace, and the failure is detected on an open sector next to the axis. The subtraction of the smooth axis coordinate of the bounded coupling cannot remove it. The cutoff strain column, the far-tail chart column and smooth normalization corrections likewise cannot repair the radial jump.

## Dependencies and acceptance

Proof 198 defines and independently reconstructs the exact coarse spline basis and low input norm. Topics173 and174 define the actual high space, graph and chart. Topics50,76,123,126,140 and167 provide the actual axis positivity, finite-mode coefficients, joins and normalized high coupling. This proof supplies the endpoint classification and the distinction between high input and high graph membership. The exact endpoint calculation is independently replayed by de Boor polynomials; its source and proof hashes are recorded with the verdict. No new numerical operator bound is claimed.

## Exact verification result

At2026-10-28T13:59:10.038769+00:00 the original-data computation completed216 exact Cox/de Boor polynomial comparisons,884 exact C6 interior joins, and both endpoint jets through order7 for all34 splines. The first nonzero endpoint orders are exactlyi on the left fori<=7 and33-i on the right fori>=26; all other endpoint polynomials vanish identically. It confirms the66-column high-input and60-column high-graph subsets, with their positions in the declared S1M4P metadata stored in evidence/check.json. Runtime was0.934seconds on one thread. The current producer's q=3 is independently visible in the saved section.py and basis.py snapshots. These are exact regularity and index statements. No output Gram or high-norm finite singular value is certified.
