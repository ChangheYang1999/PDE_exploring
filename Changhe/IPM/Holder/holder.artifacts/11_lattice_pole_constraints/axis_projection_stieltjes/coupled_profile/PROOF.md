# Coupled profile differences in positive Stieltjes sums

## Statement

Use the real homogeneous Holder space, circular principal values and
R_1^2=T_xx-I/2 from ../../../01_setup/PROOF.md. Let 0<alpha<1, b>0,
shift>=-1/2 and [P]_alpha<=K. The polygon-projection witness of the
parent PROOF.md has seminorm at most one and diagonal increment

    1+4 integral_(X>0,Y>0) V(X,Y)(-d_Y f) dX.

All omitted contributions are nonnegative. The parent proof permits
any rigorously established uniform lower bound for each decrease
f(X,Y0)-f(X,Y1), with Y0<Y1. The following additional rule is valid
on a strip X=1/2+s d, d_l<=d<=d_r, s in{-1,1}:

    Y_j=d v_j,  v_0<v_1,
    h=2^(alpha-1)X^alpha,
    G_j=g(X,Y_j)+shift,
    p_j=-1/2+d^alpha phi(v_j)/K,
    phi(v)=1/2[(1+v^2)^(alpha/2)
               +sgn(1-v^2)(|1-v^2|/sqrt(1+v^2))^alpha].

Suppose outward interval arithmetic proves p_0<=G_0 on the strip.
Then the decrease is bounded below by

    max(0,min(delta,p_0+h,h-p_1,2h)),
    delta=d^alpha[phi(v_0)-phi(v_1)]/K,                 (1)

where every entry in the minimum may be replaced by any uniform lower
bound on that entry. The result may be maximized with the original
independent-endpoint lower bound. Thus the new rule never weakens the
certified sum on a fixed grid. It does not assert monotonicity under
changing the grid or cutoff.

## Proof

Fix d. Write A=min(G_0,p_0) and B=min(G_1,p_1). Both G and p are
nonincreasing in Y by the parent monotonicity proof, so A>=B. The
certified branch hypothesis gives A=p_0, whereas B<=p_1. Consequently

    A-B>=p_0-p_1=delta,
    A+h=p_0+h,
    h-B>=h-p_1.

For any real A>=B and h>=0, direct consideration of the two endpoints
relative to[-h,h] gives the exact identity

    clamp(A,-h,h)-clamp(B,-h,h)
       =max(0,min(A-B,A+h,h-B,2h)).

Indeed, if both values lie inside the interval it is A-B; if only
A is above the interval it is h-B; if only B is below it is A+h;
if they span the interval it is2h; and if both are outside on the
same side it is zero. These cases include the boundaries. Substituting
the preceding lower bounds proves (1), since minimum and maximum are
monotone in every argument.

The identity P(s d,d v)=d^alpha phi(v) follows directly from the
homogeneous profile formula; it is independent of s because P is even
in its first coordinate. In particular the common radial factor is
retained in delta. Evaluating the two p endpoints separately would lose
this correlation in interval arithmetic. No derivative or smoothness
hypothesis is needed, even when an endpoint crosses a polygon branch.

For a whole strip, use interval lower endpoints for the four entries
in (1), after proving p_0<=G_0 by disjoint interval bounds. Its positive
part is a uniform nonnegative decrease. The same is true of the old
endpoint rule, so their maximum remains valid. Multiplying by the
parent proof's uniform lower bound for V and the strip width gives
a positive Stieltjes lower sum. This proves the statement.

## Dependencies and scope

The parent proof supplies the exact operator identity, admissibility,
monotonicity, unimodality of V and treatment of all singular and infinite
regions. This lemma supplies only a sharper finite-cell decrease. A
numerical output still requires the separate profile certificate,
complete strip-coverage check, hashes and downward rounding. It is not
an independent assertion that any chosen K is admissible.
