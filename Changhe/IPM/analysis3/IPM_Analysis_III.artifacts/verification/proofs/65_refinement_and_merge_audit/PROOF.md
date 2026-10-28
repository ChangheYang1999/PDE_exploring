# Audit of the revised range, refinement and merge algorithms

## Scope

This audits the four exact source snapshots in evidence. It does not
certify an uncompleted production output. All range conclusions assume
finite outward input coefficient balls and correct exact cell endpoints.
The older range algorithm is treated separately in topics55 and58.

## Finite-cell merging at order20 and pruning

For an exponential polynomial sum_e exp(e s)p_e(s), 0<=s<=h, replacing
a cluster by its base e0 and truncating exp((e-e0)s) at order J gives
an absolute remainder bounded by

 exp(max(e0,0)h) sum_a |c_a|h^a
       times (|e-e0|h)^(J+1) exp(|e-e0|h)/(J+1)!.

This estimate holds for every nonnegative integer J, every base and
every cluster. Thus changing J from40 to20 and changing the floating
cluster-width preference to1 do not alter validity. They affect only
tightness. The code accumulates these errors in outward ball arithmetic,
and the subsequent Taylor and exact-endpoint hull argument is the one
proved in proof 58.

The new pruning branch computes a coefficient-sum bound B for the
merged polynomial and adds the complete merge remainder R. It returns
[-u,u] only when u, an upward conversion of B+R, is below its heuristic
tolerance. This is valid because |f|<=B+R<=u. In particular the branch
does not set small modes to zero. The tolerance and its floating
comparison affect speed, not enclosure. A positive number below the
binary64 subnormal range must still be converted upward, as the audited
fup routine does.

The revised finite-cell method is therefore sound under its stated
input conditions. As before, cancellation accuracy must already be
present in the primitive coefficient balls before this range step.

## Adaptive angular refinement

Let I be an exact angular interval. Suppose eval(I) returns finite
lower bounds m(I),a(I) valid throughout I. If it is split into closed
halves I1,I2, then

    min(m(I1),m(I2)), min(a(I1),a(I2))

are valid lower bounds on I. Repeating this argument proves validity
at every finite recursion depth. The stopping threshold and depth
limit need not be mathematically optimal. Taking the maximum of a
coarse lower bound and the refined lower bound is also valid. The
snapshot follows exactly this rule.

The theta_ball construction uses an outward center ball and an upward
radius bound for half the difference of endpoint balls. It covers the
exact interval corresponding to those endpoints, including when the
endpoints contain the rounded value of pi. Child endpoints are formed
by ball arithmetic from the same parent endpoint balls. Thus there is
no uncovered angular gap. The original coarse construction uses a
binary64 radius enlarged by 1+1e-15. For the specified positive normal
widths pi/(2 ntheta), ntheta=16 or64, its excess exceeds the two relevant
rounding errors. The refined constructor uses the clearer directed
conversion and does not need that argument.

Every accepted global certificate must establish finite bounds for
every leaf and complete coverage of all radial cells, including the
two half-lines. A check only on the first angular entry of each cell
is not a full coverage check. The current recursive function does not
explicitly reject non-finite leaf values. Python min(a,nan) can equal
a, and max(a,nan) can equal a; such a leaf can therefore be hidden by
aggregation. The actual finite arithmetic in the present formulas may
rule this out, but a reusable acceptance guard should check it rather
than rely on aggregate finiteness. No claim here asserts an actual
production NaN.

## Velocity and derivative formulas for the zero-set test

With polar rates q=V_r/r and u=V_theta/r, orthonormality gives

    |V|/r=sqrt(q^2+u^2).

Taking the least absolute value of each enclosing interval and then
the square root gives a lower bound. The directed endpoint conversions
in minabs are conservative on intervals of either sign, and zero is
used when the interval contains0.

Write c=cos(theta),s=sin(theta), and let
 R=psi_rr, T=psi_rtheta/r, Q=psi_thetatheta/r^2,
 P=psi_r/r, H=psi_theta/r^2.
Then

 psi_xx=c^2 R-2sc T+s^2 Q+s^2 P+2sc H,
 psi_yy=s^2 R+2sc T+c^2 Q+c^2 P-2sc H,
 psi_xy=sc R+(c^2-s^2)T-sc Q-sc P-(c^2-s^2)H.

These follow by applying partial_x=c partial_r-s partial_theta/r
and partial_y=s partial_r+c partial_theta/r twice. Together with
DV=[[ell-psi_xy,-psi_yy],[psi_xx,ell+psi_xy]], these confirm the
snapshot's four derivative entries. Its scalar du also bounds the
Euclidean operator norm. In the orthonormal polar frame the Hessian is
[[R,T-H],[T-H,Q+P]]. Its norm is at most
max(|R|,|Q+P|)+|T-H|, which is bounded by
s_tt+2 s_t+s_tth+s_thth+s_th in the code's nonnegative sums. The returned
du has one additional nonnegative s_tth term. Rotation by the fixed
matrix in U=(-psi_y,psi_x) preserves this norm. Thus Lip(V)<=ell+sup du;
the four interval entries can alternatively give a sharper bound.

Excluding a few boxes near an approximate source from a positive
|V|/r test does not by itself prove hypothesis(Z). The complete omitted
region must be covered by a separate uniqueness argument, and the
origin and half-lines must remain included in the stated domain. The
certified source bracket from proof 15 should determine which box is
omitted; a rounded source coordinate may locate that box but is not
itself a uniqueness certificate.

## A concrete defect in the archived merge

The archived merge_margin.py lists only

    M_lo,Q,BP_up,GR_up,DU_up,MU,MA_lo,TANG.

It does not merge M_ref,MA_ref,NREF,VLO,DV. The summary routine then
silently substitutes unrefined M_lo and MA_lo, and the zero-set summary
receives VLO=None. This loses the advertised refinement and zero-set
results. It does not improve a lower bound unsafely: the substituted
coarse bounds are weaker. But it cannot be presented as a certificate
using the refined minima or as a zero-set certificate.

A repair can merge all floating arrays on the computed-cell mask and
merge the integer NREF on that same mask. Testing NREF for non-NaN is
wrong, since uncomputed integer entries are zero. The merger should
also require identical cell endpoints, angular endpoints, background
identity and parameters, disjoint ownership, and complete coverage
before a global summary is accepted. The present report's independent
acceptance step will check those conditions from the actual arrays.

## Verdict and evidence

CONFIRMED: the new order20 merging and nonzero pruning bound; the
finite adaptive refinement rule; the polar Hessian and velocity-norm
formulas, under finite enclosing inputs.
REFUTED: that the archived merge retains refined or zero-set data.
OPEN: acceptance of a complete actual global coefficient certificate,
and coverage of any region excluded around the source.

The companion check uses exact-source snapshots, independent stable
moment comparisons, a pruning example below binary64 range, a symbolic
polar-Hessian check, and a small aggregation counterexample. These are
supplementary tests; the enclosure and coverage arguments above give
the mathematical scope of their conclusions.
