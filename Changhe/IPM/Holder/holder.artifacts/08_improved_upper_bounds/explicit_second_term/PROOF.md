# An explicit upper bound with the sharp small-exponent constant term

## Statement and dependencies

Work in the real homogeneous Holder space on the plane with seminorm

    [f]_a = sup_(x != y) |f(x)-f(y)|/|x-y|^a,  0<a<1.

The kernels, circular principal values and extension modulo constants are
those in ../../01_setup/PROOF.md. In particular
K_b(z)=cos(2 arg z-2b)/(2 pi |z|^2), T_xx=T_0, T_xy=T_(pi/4), and
R_1^2=T_xx-I/2. Let C_a and D_a be the corresponding sharp seminorm
constants. The same scalar-operator inequalities hold for complex inputs
by applying the real inequality to each phase projection.

Define

    a2(a) = 2^(1+a/2)/(pi(a+2)),
    A(a) = Gamma((a+2)/2)/(2 sqrt(pi) Gamma((a+3)/2)),
    E(rho) = -log(1-rho^2)/2,
    tau = 1/2-log(3/2),
    R(a,rho) = 2^a(1/2-2 log(rho)/pi)
       + [2^a+(1+2rho)^a] E(rho)
       + (2^(a+1)/pi) a [1/(1-a)+tau].

Then, for every 0<a<1 and every 0<rho<1/2,

    C_a <= H_C(a,rho) := 2 a2(a) rho^a/a + R(a,rho),
    D_a <= H_D(a,rho) := 2 A(a) rho^a/a + 1/2 + R(a,rho).       (1)

In particular the infimum of each right side over 0<rho<1/2 is an
explicit one-parameter upper bound. For 0<a<1/4 one may take rho=sqrt(a).
Writing C0=1/2+(log(2)-1)/pi, this choice satisfies

    H_C(a,sqrt(a)) = 2/(pi a)+C0+O(a log(a)^2),
    H_D(a,sqrt(a)) = 2/(pi a)+2C0+O(a log(a)^2).                (2)

The actual inequalities (1) contain no unspecified constants. The
asymptotic notation in (2) describes their elementary limiting behavior.
The main dependencies are the exact angular pairing in
../../02_upper_bounds/PROOF.md, the phase-uniform projection decomposition
in ../local_projection/PROOF.md, and the independently audited theorem
N(b)<=1/2 in ../../05_team_audit/lead_maximality/PROOF.md. No numerical
integration or finite transport certificate enters this result.

## The two-pole decomposition

By translation, scaling and rotation it suffices to estimate the unit
increment between x=1/2 and y=-1/2, with arbitrary kernel phase b. Put

    nu_b(w) = K_b(x-w)-K_b(y-w),
    D_rho = C \ (B(x,rho) union B(y,rho)),
    V_b(rho) = (1/2) integral_(D_rho) |nu_b(w)| dA(w).

The increment splits into its two center-subtracted own-kernel integrals
on the radius-rho pole disks, plus the integrable density

    mu_b,rho(w) = K_b(x-w) 1_(|x-w|>=rho)
                 - K_b(y-w) 1_(|y-w|>=rho).

Circular angular cancellation makes this identity independent of the
small principal-value cutoff. The two local terms have total bound
2 a2(a) rho^a/a. For R_1^2, the projection decomposition of the cited
lemma replaces that bound, including the full identity contribution,
by 2 A(a) rho^a/a+1/2, uniformly in b. In detail, that decomposition is
N_rho=P_rho+(1/pi)I-Q_rho, where Q_rho is a positive convolution measure
of mass 1/pi. Thus -Q_rho-(1/2-1/pi)I has seminorm at most 1/2; the two
values of P_rho cost at most 2 A(a)rho^a/a. It uses the same regular
measure mu_b,rho.

The regular measure is odd under w -> -w. Its integral against a
normalized Holder input converges absolutely: it is bounded away from
the deleted own poles and decays as |w|^-3 at infinity, whereas
|f(w)-f(0)| <= [f]_a |w|^a. Antipodal pairing therefore gives

    |integral mu_b,rho f|
       <= [f]_a (1/2) integral |mu_b,rho(w)| (2|w|)^a dA(w).   (3)

## A uniform quantitative finite-part bound

The finite-part theorem states

    N(b) = lim_(eps -> 0) [V_b(eps)+(2/pi)log(eps)] <= 1/2.

On a pole disk, subtract the absolute value of its own kernel. Exact
annular integration of |K_b| gives

    N(b) = V_b(rho)+(2/pi)log(rho)+Delta_b(rho),

where Delta_b(rho) is one half of the integral, over both disks, of
|nu_b| minus the absolute own kernel. The reverse triangle inequality
bounds its absolute value by one half of the integral of the absolute
cross kernel on both disks. For one disk this is at most

    (1/(2pi)) integral_0^rho integral_0^(2pi)
        r/[1+r^2-2r cos(theta)] dtheta dr
      = integral_0^rho r/(1-r^2) dr = E(rho).

The two identical estimates and the factor one half give
|Delta_b(rho)|<=E(rho). Hence

    V_b(rho) <= 1/2-(2/pi)log(rho)+E(rho).                    (4)

This calculation also proves existence and absolute convergence of the
local difference used to pass to the finite part. On the two disks,
mu_b,rho consists precisely of the smooth cross kernels. Since
2|w|<=1+2rho there, their total contribution to (3) is at most

    (1+2rho)^a E(rho).                                      (5)

## An explicit tail bound with angular cancellation

On D_rho intersect {|w|<=1}, bound (2|w|)^a by 2^a. On |w|>1 all points
belong to D_rho, because rho<1/2. Use 2^a as a base weight there as well,
and estimate the positive excess separately. The complex increment is,
up to conjugation and a unit phase,

    G(w) = w/[pi(w^2-1/4)^2]
         = (1/pi) sum_(n>=0) (n+1)4^-n w^(-2n-3), |w|>1/2.

Consequently, for r>1,

    integral_0^(2pi) |nu_b(r exp(i theta))| dtheta
      <= (4/pi) sum_(n>=0) (n+1)4^-n r^(-2n-3).

Here each cosine of the nonzero integer frequency 2n+3 has angular
absolute integral 4, independent of its phase. Absolute convergence
justifies the expansion, and positivity justifies exchanging the upper
series and radial integral. Therefore the excess in (3) is at most

    (2^(a+1)/pi) integral_1^infty (r^a-1)
          sum_(n>=0) (n+1)4^-n r^(-2n-2) dr
      = (2^(a+1)/pi) a sum_(n>=0)
          (n+1)4^-n/[(2n+1-a)(2n+1)].

The n=0 term is 1/(1-a). For n>=1, use 2n+1-a>=2n and the exact identity

    sum_(n>=1) (n+1)4^-n/[2n(2n+1)]
      = sum_(n>=1) 4^-n [1/(2n)-1/(2(2n+1))]
      = 1/2-log(3/2) = tau.

This proves the tail term in R(a,rho). Equations (3), (4) and (5) give
exactly R(a,rho), and adding the local estimates proves (1).

## Small-exponent evaluation

The elementary expansions of the local angular constants are

    a2(0)=A(0)=1/pi,
    a2'(0)=(log(2)-1)/(2pi),  A'(0)=(log(2)-1)/pi.

For rho=sqrt(a), rho^a=exp((a/2)log(a)). Thus the local C term equals

    2/(pi a)+(1/pi)log(a)+2a2'(0)+O(a log(a)^2).

The corresponding D local term replaces 2a2'(0) by 2A'(0)+1/2.
In R(a,sqrt(a)), the first term is
1/2-(1/pi)log(a)+O(a|log(a)|), the two E terms are O(a), and the tail
term is O(a). The logarithms cancel. Substitution gives (2). All these
expansions are scalar expansions of explicit smooth functions at zero,
with a log(a) -> 0. No exchange of a supremum and a limit is used.

## Scope

These are global homogeneous seminorm bounds and therefore apply to
compact smooth real test functions as well. They do not assert bounded
supremum norms. Combining (1) with any previously proved upper bound by
taking the minimum is valid. Numerical optimization of rho is optional:
any displayed admissible rho already gives a theorem.
