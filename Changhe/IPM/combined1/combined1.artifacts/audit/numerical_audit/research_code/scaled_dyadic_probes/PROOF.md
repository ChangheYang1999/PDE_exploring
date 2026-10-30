# Projected Laplacian norms with positive rational radial poles

## Exact objects and conditional statement

Let c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The smooth S1 reference potential chi is a finite rational combination
of the mono, leg, legq and legqs generators defined below. Its density is
R=-partial_y Delta chi and its canonical velocity is u=(-chi_xyy,chi_xxy).
Let F=(cX+u).grad R-R. All source coefficients must be bound to an
independently audited immutable snapshot, with the forbidden residual
sectors zero and the exact origin identities verified.

The generators are H_m S^(p_j-m) t_A^w v_A^Q L_n(2t_A-1), with
H_m=Re(x+iy)^(2m), S=1+r2, p_j=(3+gamma-j delta)/2,
t_A=r2/(A2+r2), v_A=A2/(A2+r2), nonnegative integer indices and
A in{1,10,100}. L_n is the Legendre polynomial. Mono and leg mean the
Q=0,A=1 cases, with n=0 for mono. Every generator is smooth, and all
coefficients are exact rational numbers stored in the candidate JSON.

For a>=0 and a finite set E of positive odd angular frequencies, define

    J_E(a)^2=sum_(n in E) int_R2 (1+r2)^(2-a)
                                            |Delta Pi_n F|^2 dX,
    N_a(F)=||(1+r2)^((2-a)/2) Delta F||_(L2(R2)).

Here Pi_n is the full-circle sine projection with coefficient
pi^-1 int_0^(2pi) F(r,theta)sin(n theta)dtheta. Orthogonality gives
J_E(a)<=N_a(F), even if the latter is infinite. Complete enclosing balls
for J_E at specified a therefore give projected lower witnesses; they
are not full upper norms of F.

For the registered scalar exclusion additionally assume
1<c<2, chi_xxyy(0)=1-c and a0=R_y(0)>=5c-4. Let d=c-1,
Astar=1+1/c, and H(d)=max_(0<s<d)(d-s)sqrt(4 pi s(1+s)).
The following conclusion is conditional: if a proposed proof scheme
requires

    5^((a-2)/2) N_a(F)<H(d)(1+c-ca)/(1+a), 0<a<Astar,

then any strictly violating cell below excludes that scheme throughout
the cell. The interpretation as FW-T-DYADIC-Y-v1 also requires all the
exact realization, domain, input-hyperplane, canonical velocity, dyadic
partition and absorption assumptions of the independently audited origin
inverse theorem and its frozen Opus reviews. Nothing here proves that
inverse theorem or rules out another scheme or an exact stationary profile.

## Complete residual and derivative construction

Write t=r2/(1+r2) and v=1-t. Generator substitution gives
S^p_j cos(2m theta) times a rational function of t with denominator
(1+99v)^b(1+9999v)^e, where b,e are nonnegative integers. Both factors
are positive on[0,1]. Exact rational sums, products and derivatives
remain in this class. The scaled_weak_backend proof derives the
Cartesian recurrence for every physical field from this identity.
Use that exact recurrence and retain every input angular pair selected
by cos(l theta)sin(m theta)=[sin((m+l)theta)+sin((m-l)theta)]/2.
Signed negative frequencies must be folded with their sign. The exact
linear drift and quadratic products yield

    Pi_n F=r sum_ell v^(ell delta/2) P_ell(t) sin(n theta),

where each P_ell has only the positive denominators above. Division by
t powers is allowed only after checking all required exact numerator
zeros, since denominators are nonzero at t=0.

Let z=ell delta/2 and T_z P=(1-2zt)P+2t(1-t)P'. The polar identity is

    Delta[r v^z P(t)sin(n theta)]
        =r v^(z+1)L(t)sin(n theta),
    tL=T_z(T_z P)-n2 P.

It follows by applying r partial_r twice and subtracting n2, then
multiplying by r^-2=v/t. Derivatives of P include every positive-pole
factor. The exact numerator of the right side must vanish at t=0,
so L is constructed by verified rational division by t.

Independently represent a Cartesian derivative of order q as
r^(1-(q mod2)) v^(floor(q/2)+ell delta/2) Q(t) trig(theta).
Equivalently the numerator in r^(1-q)v^(ell delta/2) form is
t^floor(q/2)Q. If this numerator is B, its radial derivative numerator
is (1-q-ell delta t)B+2t(1-t)B'. Standard Cartesian trigonometric
identities give the n-1,n+1 terms, then division by t^floor((q+1)/2)
returns to the displayed normalization. Apply this twice, compare both
mixed derivatives exactly, and compare xx+yy with the polar L for every
branch and frequency. The algebra is valid for rational positive-pole
functions, and its A=1 specialization must match the audited polynomial
pipeline coefficientwise before any scaled candidate application.

## Endpoint cancellation and finite moments

For each nonzero L, write its numerator in v and remove its exact lowest
nonzero power v^q. Denominators equal1 at v=0 and cause no endpoint
cancellation. Thus L(1-v)=v^q Q(v)/D(v), D positive. Require
ell delta+2q-2>0 for every branch. This makes every diagonal integral
finite at a=0 and hence all cross integrals finite for a>=0.
For one selected mode the complete squared norm is

    (pi/2) sum_(ell,k) int_0^1
      v^(a+(ell+k)delta/2+q_ell+q_k-3) (1-v)
                       Q_ell(v)Q_k(v)/(D_ell(v)D_k(v))dv.

The factor follows from dx=r dr dtheta, r dr=dv/(2v2), r2=(1-v)/v,
the two v^(1+ell delta/2) factors and the weight v^(a-2).
Use each unordered pair with multiplicity2 off the diagonal. Combine
rational functions exactly, retaining all cross terms and positive-pole
powers. No spatial cutoff or quadrature is used.

The scalar proof in rational_pole_moments gives exact partial fractions
for int_0^1 v^b N(v)/D(v)dv, b>-1. Its independent T4 review is accepted
by N4-203. Decompose each fixed rational group once, replay the exact
identity, then reuse that decomposition at the eight specified b+a.
Polynomial parts integrate exactly as rational sums; principal parts use
the audited positive-pole moments with outward Arb arithmetic. Reusing
an exact partial-fraction decomposition is valid because it depends on
N,D and not on the power b. Positive energies and more than150 relative
accuracy bits are required. This arithmetic proof includes both endpoints.

## Seven-cell scalar test and complete implication

The derivative of (d-s)^2 s(1+s) is
(d-s)[d+(2d-3)s-4s2]. Its unique interior maximum has
sstar=(2d-3+sqrt((2d-3)^2+16d))/8. An enclosing ball for H(d)
is obtained by direct substitution, with0<sstar<d checked.

J_E(a) decreases in a by pointwise monotonicity of its nonnegative
integrand. The factor (1+c-ca)/(1+a) decreases on[0,Astar].
Consequently, on any cell[l,h] and for e>=h, the strict inequality

    5^((l-2)/2) J_E(e)>H(d)(1+c-cl)/(1+l)

violates the registered necessary scalar inequality throughout that cell.
Use cells with endpoints0,1/4,...,3/2,Astar and weights e=h except
e=7/4 in the last cell. Exact3/2<Astar<7/4 is checked. The resulting
seven cells cover every0<a<Astar. Under the additional origin-inverse
hypotheses, a>=Astar fails the required positive low rate. Only when
every scalar cell is strictly excluded and all those analytic hypotheses
apply may the stated sufficient scheme be called excluded over0<a<2,
0<s<1 for each fixed finite localization radius. A selected-mode norm
alone cannot assert this broader interpretation.

## Calibration, provenance and scope

Before010, reproduce the007 mode1 and mode3 exact residual projections,
Cartesian Laplacian maps, all eight weighted energies and norms, and
seven-cell quantities from the independently confirmed polynomial result.
Require exact coefficient equality for projections and both derivative
maps, not just point agreement. For010, bind its independent Cartesian
physical point and origin/sector record. These tests complement the
rational-field manufactured fixtures191 and scalar203.

Each result binds candidate, audit, proof, code, positive-pole primitive,
polynomial calibration and analytic-framework hashes. Mode results are
immutable and resumable; only a complete prescribed set yields a cell
report. This proof precedes code execution. All resulting010 values
remain OPEN until independently reviewed at candidate level.
