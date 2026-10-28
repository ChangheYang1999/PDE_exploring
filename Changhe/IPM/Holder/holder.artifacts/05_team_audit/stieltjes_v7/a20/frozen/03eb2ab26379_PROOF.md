# Certified positive Stieltjes sums for the projection cusp

## Statement

Use the real homogeneous Holder seminorm, increment-defined Riesz transforms,
and normalization R_1^2=T_xx-I/2 from ../../01_setup/PROOF.md. Fix 0<alpha<1,
a=1/2, b>0, and a certified number K with [P]_alpha<=K, where

    P(u,v)=1/2[(u^2+v^2)^(alpha/2)
          +sgn(u^2-v^2)(|u^2-v^2|/sqrt(u^2+v^2))^alpha].

Set P(0,0)=0. Let g be the axis polygon signed-distance witness with its
own component signs, as defined in ../axis_clamped_layercake/PROOF.md.
For X>0 define h=2^(alpha-1)X^alpha and

    f(X,Y)=clamp(min(g(X,Y)+t,-1/2+P(X-a,Y)/K),-h,h),

where t>=-1/2. Extend evenly in Y and oddly in X. Then [f]_alpha<=1,
f(a,0)=-1/2, and

    R_1^2 f(a,0)-R_1^2 f(-a,0)
      =1+4 integral_{X>0,Y>0} V(X,Y)(-d_Y f) dX,
    V=2aXY/[pi(((X-a)^2+Y^2)((X+a)^2+Y^2))]>0.

Every finite sum specified below is a lower bound for D_alpha. There is
no assertion that this witness or its parameters are optimal.

## Proof and finite lower sum

The profile seminorm hypothesis and the lattice lemma prove admissibility.
At the pole the minimum is -1/2 because g=P=0 and t>=-1/2. The profile
is nonincreasing in |Y| by ../../07_diagonal_identity_term/full_range_profile/PROOF.md.
The signed distance g has the same monotonicity, proved in
../monotone_axis/PROOF.md. Taking minima and clamping preserve it. That
proof therefore establishes the exact positive integral above, including
its principal-value and infinity justifications.

Choose disjoint X strips of the form X=a+s d, with s in{-1,1} and
0<d_l<d<d_r, restricted to X>0. In a strip choose an increasing finite
sequence of positive ratios v_j and vertical endpoints Y_j(X)=d v_j.
Suppose outward arithmetic proves, uniformly for d in[d_l,d_r],

    f(X,d v_j)-f(X,d v_(j+1)) >= A_j >=0,
    min(V(X,d v_j),V(X,d v_(j+1))) >= B_j >=0.

For fixed X, V is unimodal in Y>0, so its minimum on each vertical
interval is at an endpoint. Its integral against the positive variation
measure on this interval is therefore at least A_j B_j. Integrating X
shows that the strip contributes at least

    (d_r-d_l) sum_j A_j B_j.

Sum over strips, multiply by four and add one. Every omitted strip,
vertical interval and infinite tail has a nonnegative contribution.
The finite logarithmic grid is merely a choice of exact endpoints:
d_j=exp(l+j(r-l)/n), v_j=exp(p+j(q-p)/m), with rational l,r,p,q.
Arb enclosures of these exponentials and of widths give rigorous bounds.
The two signs occupy disjoint strips. A complete-grid merge checks exact
integer coverage, parameters and source hashes before quoting a number.

## Point evaluation contract

The distance to the polygon is the minimum of X and the distances to
its upper inner segment (0,a)--(a,0), upper outer segment
(a,0)--(a+b,b), and upper ray with direction(sqrt(3),1). For Y>=0,
reflected lower pieces cannot be closer. The boundary height is

    B(X)=max(a-X,min(X-a,(X-a+(sqrt(3)-1)b)/sqrt(3))).

The sign is positive for Y<B(X), negative for Y>B(X); an interval
crossing the boundary must enclose both signs. Segment distance uses
the orthogonal projection clipped to the exact parameter interval.
These formulas compute the distance to the actual polygon, not an
unrelated approximation to the exact kernel zero set.

All saved results are partial lower bounds. Printed ball radii can grow
under serialization, so final decimal rounding must use the saved ball's
own lower endpoint. No upper endpoint bounds the complete witness value.
