# Axis cusp with variable cone opening

## Statement

Use the real homogeneous Holder space and R_1^2 normalization of
../../01_setup/PROOF.md. Fix 0<alpha<1, b>0, -1/2<=t, and
0<theta<pi/2. Let g be the axis signed-distance polygon from
../axis_clamped_layercake/PROOF.md, a=1/2 and h=2^(alpha-1)X^alpha.
On X>0 set

    P_theta(X,Y)=(sin(theta)|X-a|-cos(theta)|Y|)_+^alpha,
    f=clamp(min(g+t,-1/2+P_theta),-h,h),

and extend evenly in Y and oddly in X. Then [f]_alpha<=1, f(a,0)=-1/2,
and f is nonincreasing in Y>0. In particular its exact R_1^2 increment
is the positive vertical-variation formula of ../monotone_axis/PROOF.md.

## Proof

The quantity inside the alpha power is the Euclidean distance to the
closed double cone |Y|>=tan(theta)|X-a|. This follows by orthogonal
projection onto its two boundary lines, with distance zero in the cone.
Distance to a closed set is 1-Lipschitz, and taking an alpha power makes
it 1-Holder. Thus P_theta has seminorm at most one. The signed-distance
g also has that bound. Minimum, maximum and the half-plane gluing lemma
therefore give [f]<=1. At the pole g=P_theta=0, so t>=-1/2 forces f=-1/2.
Both P_theta and g decrease with Y>=0; so do their minimum and its clamp.
The hypotheses of the positive variation theorem are all satisfied.

This is an admissibility and exact-value representation theorem. No
floating quadrature or optimized angle is certified by this statement.
