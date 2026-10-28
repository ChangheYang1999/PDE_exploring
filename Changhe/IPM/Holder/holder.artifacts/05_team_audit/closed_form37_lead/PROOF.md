# Independent proof audit of the sharper closed form

## Statement and scope

Let 0<a<1. On real homogeneous Holder functions modulo constants use
[f]_a=sup_{x!=y}|f(x)-f(y)|/|x-y|^a. Define T_xx and T_xy by the
circular principal-value kernels in ../../01_setup/PROOF.md, with kernel
differences at infinity. Their common operator norm is C_a. The audited
claim is

    C_a <= 4*2^(-a/2)/(pi*a*(a+2)) + (209/500)/(1-a) + 1353/2500.  (1)

This is an upper bound, not an exact norm. It applies also to smooth
compactly supported functions and, by real phase projection, to complex
inputs for either real-kernel operator. It is not a bound for the complex
combination T_xx+i T_xy.

Status: CONFIRMED in V124. The complete analytic argument and both
independent numerical checks passed. Their records are in
verification/independent_audit.json and verification/alpha0_replay.json.
The source snapshot is immutable; its hashes are in
source/snapshot_manifest.json. The corrected lead proof is saved
separately in verification/lead_PROOF_corrected.md.

## Dependencies and the fixed transport bound

The paired local-circle, middle-circle and exterior-circle theorems in
../../08_improved_upper_bounds, and their common phase interpolation
bound, have already been audited. Their use here gives

    C_a <= S_a + R_g(a),
    S_a = 2*a2(a)*delta^a/a + (1+2delta)^a*delta^2/[2(1-delta)^2],
    a2(a)=2^(1+a/2)/[pi(a+2)],  delta=1/64,
    R_g(a)=sec(pi/64)*max_{j=0,...,16}(L_gj(a)+M_gj(a)+E_gj(a)).

For every group g all finite integer transport plans are fixed before
the exponent is varied. Each cost is a positive distance to the power a,
or an integral of such powers against a positive fixed measure. The
remaining untransported mass is nonnegative and has a fixed distance
upper bound. The local same-circle term is the moment

    c^a*(b^a-r^a)/a = integral_r^b (ct)^a dt/t.

Thus each component, its sum, and their finite maximum are log-convex.
The nodes and group intervals are explicitly listed in source/data/nodes2.json.
The proof of this property for the identical underlying plans is in
../../09_uniform_comparison/pass3/source/PROOF3.md. The local greedy
ordering is independent of a; middle and exterior plans use the group's
single reference exponent, not the evaluation exponent.

## Exact correction and monotonicity

Put LC=2^(1-a)*a2(a)/a and g(a)=S_a-LC. Then

    g(a)=-2*a2(a)*integral_delta^(1/2) r^(a-1) dr
         +(1+2delta)^a*delta^2/[2(1-delta)^2].             (2)

This expression extends continuously to a=0, where the integral is log32.
A monotonicity argument valid for every a>=0 avoids interval dependency:

    -2*a2(a)*integral_delta^(1/2) r^(a-1) dr
      =-(4/pi)*integral_0^(pi/4) sin(2t)
                     integral_delta^(1/2) (2r sin t)^a dr/r dt.

Every base in the negative integral lies between zero and 1/sqrt(2),
so the negative moment increases with a. The positive term in (2) also
increases. Hence g is increasing on [0,infinity). At t=0 the measure
vanishes, so the harmless zero base causes no discontinuity at a=0.

## Nodal and zero-exponent checks

For groups 2 through 6 the auditor checks the exact hash identity of the
previously accepted nodal certificates and subtracts the exact S_a using
outward arithmetic. For groups 0, 1 and 7 it independently merges every
local and middle chunk, checks the fixed geometry, precision and integer
unit, verifies all source hashes, and proves that each required radial
row and phase occurs exactly once. The exterior files are hash-identical
to accepted certificates. Each stored rational remainder is checked
against the independent recombination.

At a=0 all positive transport distances have cost one. If the extracted
positive mass is m and the half-variation upper bound is V, transport plus
residual costs m+(V-m)=V. Therefore the zero-exponent limit is independent
of the transport plan. Local radial weights become log(b/r), and middle
weights become the lengths of their radial parameter intervals. The
exterior limit is the already independently recomputed exterior variation
plus its positive-series tail. No operator at exponent zero is defined.
Only the continuous limit of this auxiliary positive remainder is used.

The separate replay script recomputes all 256 local rows and 512 middle
rows, each with 512 angular cells and 17 phases. It imports no optimizer
or transport routine. The own local angular integral is exact. The cross
term uses the midpoint rule with its proved second-derivative bound;
cells whose sign is unresolved use an interval absolute-value bound.
The same derivative and sign rules apply to middle cells. Exact rational
interval endpoints are saved for every row. Its target is

    R_0(0) <= 158263/50000 = 3.16526.                     (3)

## Independent interpolation and the endpoint

Write kappa=209/500 and c=1353/2500. Between consecutive nodes x<y with
certified bounds rx,ry, log-convexity gives

    R_g(a) <= exp(log(rx)+(a-x)*[log(ry)-log(rx)]/(y-x)).

The independent checker subdivides each segment into adaptive dyadic
rational pieces [p,q], checks exact coverage, and uses

    exp(chord(a)) <= max(exp(chord(p)),exp(chord(q))),
    g(a) <= g(q),
    kappa/(1-a)+c >= kappa/(1-p)+c.

A strictly positive outward lower bound for the difference proves (1)
on that closed piece. This partition differs from the lead's fixed grid.
The exact union of groups is [0,199/200].

For 199/200<=a<1, the previously proved analytic bound gives

    (1-a) C_a <= (2*a2(a))^(1-a)
      *[2*a3(a)+(1-a)*2^(a+1)/(3pi)]^a/a,
    a3(a)=(3/pi)*integral_0^(pi/6) sin(3t)*(2sin t)^a dt.

The independent checker evaluates this against
(1-a)*LC+kappa+c*(1-a) on 100 closed rational intervals of
[199/200,1]. The positive expansion used is

    a3(a)=(3/pi)*sum_{k>=0} c_k*4^(-k-1)
                *2(a+5+2k)/[(a+2+2k)(a+4+2k)],
    c_0=1, c_(k+1)=c_k*(2k+1)/(2k+2).

After N terms, 0<=c_k<=1 bounds the remainder by
3*4^(-N)/[pi(a+2+2N)]. The checker uses N=100 and 320-bit
outward arithmetic. The scaled expression is continuous at a=1;
division by 1-a is used only for a<1. Successful checks prove (1).

## Comparison with the diagonal closed form

The older diagonal bound is

    G*(a)=2^(1-a)*A(a)/a + kappa/(1-a)+269/250,
    A(a)=Gamma(1+a/2)/[2sqrt(pi)Gamma(3/2+a/2)].

To justify retaining it rather than adding 1/2 to (1), more than A<a2
is needed, since c has decreased by 87/2500. Define

    Q(a)=2^(1-a)*(a2(a)-A(a))/a
      =(4/pi)*integral_0^(pi/4) sin(2t)*(sin t)^a
                            *[1-(cos t)^a]/a dt.

Both positive factors (sin t)^a and [1-(cos t)^a]/a decrease with a.
The latter assertion follows by writing it as
integral_0^(-log cos t) exp(-as) ds. Consequently for 0<a<=1,

    Q(a)>=Q(1)=2sqrt(2)/(3pi)-1/4 > 87/2500.

For the last strict inequality even sqrt(2)>7/5 and pi<22/7 suffice.
Therefore the right side of (1), plus 1/2, is strictly larger than G*(a).
This comparison is exact and does not require sampling exponents.

## Reproduction and evidence

Run, one process at a time and single-threaded:

    python3 code/audit_closed_form37_lead.py
    python3 code/replay_closed_form37_alpha0.py

The scripts are in the code directory at the artifacts root. The zero replay is
checkpointed and can be resumed unchanged after a command timeout.
The numerical records include their code hashes, exact rational interval
endpoints, and actual UTC completion times. No optimization result is
accepted merely because the optimizer reports success.
