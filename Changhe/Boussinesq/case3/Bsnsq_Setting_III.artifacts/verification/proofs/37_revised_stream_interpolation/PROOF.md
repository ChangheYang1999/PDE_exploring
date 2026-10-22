# Cell interfaces and angular jets in a differentiated stream interpolant

Date:2026-10-20. Status: exact structural counterexamples CONFIRMED;
independent floating-point manufacture is recorded separately.
No existence or nonexistence claim about B2 follows.

## 1. Statement, source and notation

Consider a full-plane stream function Psi=sum P_k(r) sin(k phi), with
x=r sin(phi), y=-r cos(phi), U=(-Psi_y,Psi_x). Let

    t=1-(1+r^2/L^2)^(-1/(2 beta)), beta,L>0,
    p_k=2+(k mod2).

The inspected characteristic rule interpolates S_k=P_k/r^{p_k} at n
interior Gauss-Legendre points independently in each interval of t.
It then forms Ptilde_k=r^{p_k} Stilde_k and differentiates THIS Ptilde
exactly inside each interval to evaluate U. The current production
choice is n=7, hence interpolation degree6. The readonly source is
archived with hashes in candidate_snapshots/num_interp_20261020T1615.
No fitting-lane code is imported or executed in the verifier tests.

This rule has zero pointwise divergence inside each open cell. It
need not have a continuous velocity across radial cell interfaces,
and its piecewise velocity need not have zero distributional
divergence. It also need not have a differentiable velocity at0,
even when every input datum comes from a smooth compactly supported
canonical full-plane stream function. Both defects occur for n=7.

These are defects of exact fixed-resolution representation identities.
Their magnitudes on an actual state require separate measurement;
they do not disprove approximation or convergence of a repaired
method. Finite-dimensional numerical approximants need not themselves
be exact smooth PDE solutions, but these errors must enter the error
budget and refinement programme.

## 2. Exact interpolation remainder

For n-point Gauss-Legendre interpolation on [a,a+h], write Q(t) for
the monic degree-n polynomial with those nodes as roots. The ordinary
Legendre polynomial P_n has leading coefficient 2^{-n} binom(2n,n).
Consequently

    Q(t)=h^n P_n(2(t-a)/h-1)/C_n, C_n=binom(2n,n).

Its values at the endpoints are Q(a)=(-1)^n h^n/C_n and
Q(a+h)=h^n/C_n. For any monic degree-n polynomial S(t), the degree
n-1 interpolant is EXACTLY S(t)-Q(t). This follows since their
difference is monic of degree n and vanishes at all n nodes.
A leading coefficient A multiplies Q by A.

## 3. A nonzero radial-interface velocity jump

Let t0 be an interior interface and let hL,hR be the widths of the
neighboring cells. On those two cells choose

    S(t)=((t-t0)/H)^n, H=max(hL,hR).

The left and right interpolant traces at t0 are

    Stilde_L(t0)=-hL^n/(C_n H^n),
    Stilde_R(t0)=-(-1)^n hR^n/(C_n H^n).

For odd n, their jump (right minus left) is

    J=(hL^n+hR^n)/(C_n H^n)>0.                       (1)

Use k=2 and P_2=r^2 S(t), multiplied by a smooth radial cutoff
identically1 on these cells and compactly supported away from0 and
infinity. This is a smooth compactly supported full-plane stream
function, odd under x reflection, and has no imposed wall. The
velocity from it is reproduced by the ordinary full-plane inverse
of Omega=-Delta Psi: the difference is an entire decaying harmonic
vector field and hence vanishes. The cutoff can be taken smooth
in r^2 and exactly constant on neighborhoods of the two closed cells.

The polar components of the piecewise represented velocity are

    Utilde_r=-k Ptilde_k cos(k phi)/r,
    Utilde_phi=Ptilde_k' sin(k phi).

If r0 corresponds to t0, (1) gives

    [Utilde_r]_{r0}=-2 r0 J cos(2 phi).                (2)

This is nonzero except at isolated angles. Integrating against a
smooth test function supported near the circle and integrating by
parts separately on its two sides shows

    div Utilde=[Utilde_r] delta_{r=r0}                (3)

locally at this interface, since div Utilde=0 in each open cell.
Here delta_{r=r0} means arc-length surface measure in plane
coordinates. Its coefficient can have zero angular average while
still being a nonzero distribution. Thus the vanishing total flux
through a full circle cannot certify local incompressibility.

The distributional rotated gradient of the DISCONTINUOUS represented
stream function would contain an additional singular tangential
measure. The code evaluates only ordinary cellwise derivatives;
it does not represent that singular measure. Therefore there is no
contradiction with the distributional identity div grad-perp=0.

Even if an interpolation scheme enforces stream-value continuity,
stream-derivative jumps may create a vorticity sheet. Smooth-profile
checks need velocity derivatives and the elliptic residual as well
as zero distributional divergence.

## 4. High angular-mode leakage at the origin

Let [0,h] be the first cell and use k=4, so the rule takes p_k=2.
Set, throughout that cell,

    S(t)=(t/h)^n, P_4(r)=r^2 (t(r)/h)^n, n=7.          (4)

Multiply P_4 by a smooth compactly supported cutoff equal1 on a
neighborhood of the entire cell. This is again a smooth canonical
full-plane manufacture. In fact t(r)=r^2 a(r^2), with a positive
smooth function near0. Hence (4) times sin(4phi) is r^{16} times a
smooth radial function times sin(4phi). Since r^4 sin(4phi) is a
homogeneous harmonic polynomial and16-4 is even and nonnegative,
the field is smooth at0.

The interpolation remainder in section2 gives exactly

    Stilde(0)=1/C_7=1/3432=:c>0.                      (5)

Thus the represented stream has leading term

    Psitilde=c r^2 sin(4phi)+O(r^4).

This homogeneous term has angular frequency4 but degree2. It is not
a quadratic polynomial, so the represented velocity cannot be
differentiable at0. One can see the contradiction directly. Along
both coordinate axes, its directional velocity derivatives are the
columns of the matrix -4c I. Along the ray (x,y)=r(1,1)/sqrt(2), the
actual leading velocity is +4c(x,y), whereas the matrix predicted
from the axes gives -4c(x,y). Their difference divided by r has
norm8c=8/3432. Higher O(r^4) stream terms contribute only O(r^3)
velocity and do not alter this limit.

The issue is the minimum angular order, not just odd/even radial
parity. A smooth kth stream mode near0 must have powers r^{k+2j},
j>=0; for k=1 the relative-velocity subtraction removes the first
r term, leaving r^3. Interpolating after division only by r^2 or
r^3 does not enforce the missing zeros of higher modes. A suitable
inner representation factors r^k for k>=2 and r^3 for k=1, or
explicitly imposes the equivalent vanishing derivatives in t.
This describes a local requirement; it does not prescribe a globally
well-conditioned numerical basis.

## 5. Scope of the independent computation

The script code_independent/revised_stream_interpolation_audit.py
uses Legendre-series fitting and analytic differentiation, which is
a separate implementation from the fitting lane's monomial matrix
and Torch Horner evaluator. It checks the endpoint formulas, the
velocity directional contradiction and one-sided interface traces
at several n and Nt values. It does not import or execute teammate
code and does not identify any production state as a candidate.

The theoretical constants(1) and(5) are exact. Numerical discrepancies
from them measure the verifier's own floating-point calculation;
no interval enclosure or a posteriori existence certificate is claimed.

Dependencies: polynomial interpolation, Legendre endpoint and leading
coefficient identities, smooth radial cutoffs, elementary harmonic
Liouville uniqueness and distributional integration by parts. No B2
transport equation is assumed in the manufactures, which are tests
of a numerical velocity representation only.

## 6. Recorded numerical result

The independent run took0.056612 seconds. Across n=3,5,7 and
Nt=32,40,64 for beta=2.5,3, the center endpoint identity was reproduced
to maximum absolute error1.95e-15. Across twelve interface checks
with Nt=16,32,40,64, the jump formula agreed to1.84e-15. A separate
angular quadrature of the weak divergence had relative error at most
6.21e-12 against its exact value.

At beta=3,Nt=40,n=7, the predicted origin directional discrepancy is
8/3432=0.002331002331002331. At r=1e-4 times the first-cell outer
radius, the computed value is0.002331001007404687. At interface20
of Nt=40, the normalized manufactured jump in S is0.000535958939276854;
the normal-velocity jump at phi=0.37 is-0.004231863584833088. These
are manufactured magnitudes, not production-state residuals.

The constructions change with the cell width through their chosen
normalization. The table is an identity check across discretizations,
not a convergence study of one fixed manufactured function.
