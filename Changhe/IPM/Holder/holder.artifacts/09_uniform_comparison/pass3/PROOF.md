# A sharper uniform comparison from fixed paired-circle plans

## Statement and scope

Let 0<alpha<1 and let [f]_alpha be the Euclidean homogeneous Holder
seminorm of a real-valued function on R^2, modulo additive constants.
Use the increment-defined singular integrals of ../../01_setup/PROOF.md:
T_xx has principal-value kernel cos(2 theta)/(2 pi r^2), T_xy has kernel
sin(2 theta)/(2 pi r^2), and R_1^2=T_xx-I/2. Write C_alpha for the common
seminorm norm of T_xx and T_xy, and D_alpha for that of R_1^2. These are
also the suprema over nonconstant compact smooth tests.

Define ell as follows. For 0<alpha<1/200 put

    ell(alpha)=(sqrt(2)-1)^alpha [4/(pi alpha(alpha+2))-1/4].

For 199/200<alpha<1 put

    J(alpha)=integral_0^(pi/6) sin((alpha+2)t) sin(t)^alpha dt,
    M(alpha)=(alpha+1) 2^(alpha-1) J(alpha)/cos((alpha+2)pi/6),
    ell(alpha)=2^(1-alpha)(M(alpha)+1/4).

On the intervening closed interval let ell(alpha)=I(alpha,a), where I is
the positive polygonal layer-cake integral in
../../05_team_audit/structured_layercake/PROOF.md. Use these fixed shapes:

| Exponent interval | Shape a | Plan reference exponent |
|---|---|---|
| [1/200,19/100] | 14/25 | 1/20 |
| [19/100,7/20] | 53/100 | 27/100 |
| [7/20,1/2] | 97/200 | 17/40 |
| [1/2,3/5] | 89/200 | 11/20 |
| [3/5,7/10] | 39/100 | 13/20 |
| [7/10,4/5] | 33/100 | 3/4 |
| [4/5,9/10] | 53/200 | 17/20 |
| [9/10,199/200] | 1/5 | 24/25 |

At a shared endpoint use the group on the right, except that 199/200
belongs to the last group. The proposed sharper conclusion is

    ell(alpha) <= C_alpha <= 1.0625 ell(alpha),
    ell(alpha) <= D_alpha <= 1.2894 ell(alpha).

The analytic implication and independent recombination below are proved.
The numerical conclusion is conditional on complete local and middle
nodal replay until the verification ledger explicitly accepts it. The
previous independently certified C factor 1.0825 remains valid meanwhile.
All statements concern homogeneous seminorms, not full Holder norms.

## The fixed upper family

Set delta=1/64, m=16, phi_j=j*pi/(2m), and q=sec(pi/(4m)). In groups 2
through 6, numbering from zero, define

    V(alpha)=S(alpha)+q max_(0<=j<=m) [L_j(alpha)+W_j(alpha)+E_j(alpha)],
    S(alpha)=4*2^(alpha/2)*delta^alpha/[pi alpha(alpha+2)]
             +(1+2delta)^alpha*delta^2/[2(1-delta)^2].

The three other terms are the paired local-circle, middle-circle and
exterior-circle costs in ../../08_improved_upper_bounds, respectively.
Use 512 cells on each local circle and 256 equal radial intervals in
[delta,1/2]. At each phase and radial interval select the exact integer
flow returned by transport_greedy from the cell masses and midpoint
Euclidean distances. The order and the resulting flow are independent
of alpha. Use integer unit 2^44.

For the middle circles use 512 cells per half-circle, 512 equal intervals
in the parameter t in [0,pi/2], and integer unit 2^44. At each phase,
interval and exponent group choose the plan returned by best_plan with
17 trials using the group's reference exponent in the table. Keep this
integer plan fixed throughout that group. The exterior cost is exactly
the group's already certified exterior plan from ../lead_certificate.

The transport theorems prove C_alpha<=V(alpha). They require feasible
integer flows and rigorous upper costs, not optimality of the floating
plan selection. The exact marginal equalities and all mass residuals are
checked in the certificate procedures. Their residual mass is bounded
using a fixed upper endpoint independent of alpha.

## Log-convexity without changing plans

For any nonnegative measure mu, a positive moment integral
integral d^alpha dmu is log-convex in alpha, by Holder's inequality.
Finite sums and maxima of positive log-convex functions are log-convex.
The first summand of S has logarithmic second derivative
alpha^(-2)+(alpha+2)^(-2)>0, and its second summand is log-linear.

For a local radial interval [a,b], a same-circle transport edge contributes

    p c^alpha (b^alpha-a^alpha)/alpha
      = p integral_a^b (cr)^alpha dr/r,

where p>=0 is the fixed transported mass and c is its fixed chord bound.
An opposite-circle edge contributes p e^alpha log(b/a), where e is a
fixed upper bound for its Euclidean length throughout the interval.
The centrally paired residual contributes
R(1+2b)^alpha log(b/a), where R>=0 is its fixed mass bound. All are
positive moments. Thus each L_j is log-convex.

For a middle interval [a,b], let r_max bound sin(t) throughout it.
Every edge cost is a fixed mass times one of the fixed bases

    2 r_max sin(b(k+1)/512),
    2 r_max cos(a max(0,k-1)/512)

raised to alpha, and multiplied by b-a. Here k is the corresponding
nonnegative cell displacement. The allowed displacements make both
bases nonnegative. The residual has base 2r_max. Therefore W_j is
log-convex. The exterior costs E_j are log-convex by the fixed-plan and
positive harmonic-tail argument in ../lead_certificate/PROOF.md.
Consequently V is log-convex on each exponent group.

The fixed polygon lower function has the positive representation

    I(alpha,a)/alpha
      = (1/2) integral_0^infinity (2t)^alpha J_a(t) dt/t,
    J_a(t)>0.

Therefore log(I(alpha,a)/alpha) is convex. Each group uses the same
shape at all its upper and lower nodes, including the neighboring lower
nodes required for extrapolation of secant slopes.

## Interpolation and taking the smaller valid bound

Let [a,b] be a consecutive pair of upper nodes and let A,B be rigorous
upper values of a fixed upper family at these nodes. Its logarithm is
bounded on [a,b] by the affine interpolant E of log A and log B.
For four consecutive lower nodes x0<x1<x2<x3, let l_i and u_i be positive
lower and upper enclosures of I(x_i,a0)/x_i. Convexity gives

    L1(t)=log l_1+(t-x1)(log l_1-log u_0)/(x1-x0)
           <= log(I(t,a0)/t),                 t>=x1,
    L2(t)=log l_2+(x2-t)(log l_2-log u_3)/(x3-x2)
           <= log(I(t,a0)/t),                 t<=x2.

Choose any rational c in [x1,x2]. On [x1,c] use L1 and on [c,x2] use L2.
The functions E(t)-log t-L_i(t) are convex, so their four endpoint
values give an upper bound for log(U(t)/I(t,a0)) on [x1,x2]. The chosen
c approximates the intersection of the two lower lines; its accuracy is
irrelevant to validity. All four maxima use outward interval arithmetic.

Apply this procedure separately to the former upper family U_C and the
new family V. If their certified ratio bounds on [a,b] are rho_old and
rho_new, then C_alpha/I(alpha,a0)<=min(rho_old,rho_new) on that interval.
This uses two pointwise valid inequalities. It does not assert that the
minimum of log-convex functions is log-convex.

## Numerical evidence and endpoint completion

The independent program ../../code/check_uniform3.py verifies every
source hash, all 256 local rows and 17 phases, all 512 middle rows and
all 27 reference/exponent pairs. It independently forms the nodal sums
and all 58 upper-interval comparisons at 256-bit Arb precision. The
saved result is verification/independent_recombination.json:

    C_alpha/I(alpha,a) <= 1.0624909995,
    D_alpha/I(alpha,a) <= 1.2893632770.

The second bound is the already accepted previous certificate, unchanged.
The largest C interval is [27/40,7/10]. A separate 90-decimal evaluation
using the same adverse endpoints and recorded rational splits checks
every segment and gives a maximum of 1.06249099940321874843..., below the
displayed decimal. Its evidence is verification/mpmath_recombination.json.
High-precision agreement is a cross-check; the outward Arb calculation
and soundness theorems provide certification.

The endpoint arguments of ../endpoints/PROOF.md give C/ell<1.0263 and
D/ell<1.0324 outside [1/200,199/200]. Thus complete acceptance of the new
nodal certificates implies the stated whole-interval factors. The lower
inequalities are the previously verified admissible witness bounds and
C_alpha<=D_alpha. No new approximation, principal-value or infinity
convergence assertion is needed here.

## Provenance and remaining acceptance condition

The source programs and lead statements are frozen under source/, the
input certificates under data/, and the replay outputs under
verification/local and verification/mid. The source_manifest.json records
original paths and SHA256 hashes. ../../code/run_uniform3_replay.py runs
each bounded replay chunk sequentially in one of two workers.
../../code/compare_uniform3_replay.py checks exact coverage, every interval
comparison and the hash provenance. Completion requires every new nodal
entry to pass this replay, followed by a dated CONFIRMED ledger entry.
The proof above deliberately distinguishes this condition from agreement
of a few nodal values or a successful recombination of unverified inputs.
