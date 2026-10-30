# Uniform large-index ceiling for the complete weak test

## Statement and exact inputs

Let R be the exact canonical candidate 007 and U_R its canonical velocity.
Set c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The smooth S1 reference has U_R=O(r^gamma), div U_R=0, and complete
residual F=(cX+U_R).grad R-R in L2(R2). For each integer K>=0 define

    phi_K=r v^2 t^K sin(theta), t=r^2/(1+r^2), v=1-t,
    I_K=int F phi_K,
    M_K=(2c+1)phi_K+(cX+U_R).grad phi_K.

For finite D_K>=||M_K||2 and H_K>=0 put

    m_K=2|I_K|/[D_K+sqrt(D_K^2+4H_K|I_K|)].             (1)

The denominator is positive, as proved below. In particular D_K may be
||M_K||2+||phi_K grad R||2, with any nonnegative gradient upper bound
H_K. Under the separately proved weak stationary-solution hypotheses,
that choice gives the necessary bound ||h||2>=m_K. Here we bound m_K
from above; this gives no upper bound on any solution distance.

Write the complete first-sine residual projection as

    Pi_1 F=r sum_ell v^(ell delta/2) P_ell(t) sin(theta),
    P_ell(1-v)=sum_j q_(ell,j) v^j,
    beta_(ell,j)=ell delta/2+j.

If every nonzero coefficient has beta>4/3, then for every integer
K>=K0>=0,

    m_K <= U(K0),
    U(K0)=sqrt(pi/2)/(c+1) (2K0+3)
                        sum_(ell,j) |q_(ell,j)| B(beta_(ell,j),K0+2). (2)

The finite coefficient test and every numerical upper bound for U are
independently checked below. This is an exact finite representation,
not the truncated far-field expansion used in the numerical model.

## Full-velocity denominator bound

The probe is smooth at the origin: phi_K=y(r^2)^K/(1+r^2)^(K+2).
At infinity phi_K=O(r^-3) and grad phi_K=O(r^-4). Thus M_K belongs
to L2. Integrating over disks and using the vanishing boundary terms,

    int phi_K cX.grad phi_K=-c||phi_K||2^2,
    int phi_K U_R.grad phi_K=0.

The second boundary flux is O(r^(gamma-5)), which vanishes. Smoothness
removes an inner boundary if one is introduced. Therefore

    <phi_K,M_K>=(c+1)||phi_K||2^2,
    D_K>=||M_K||2>=(c+1)||phi_K||2>0.                  (3)

This argument applies to the full transport field. It makes no claim
that ||M_K||2 exceeds the norm of the drift-only expression.

## Exact numerator and uniformity

Angular orthogonality and the change of variable v=(1+r^2)^-1 give

    I_K=(pi/2)sum q_(ell,j) B(beta_(ell,j),K+2),
    ||phi_K||2^2=pi/[2(2K+2)(2K+3)].

Since H_K>=0, (1) is at most |I_K|/D_K. Applying (3), the triangle
inequality to the complete finite coefficient sum, and
sqrt((2K+2)(2K+3))<2K+3 proves m_K<=U(K).

For fixed beta>4/3 the ratio of the corresponding positive summand
at K+1 to its value at K is

    (2K+5)(K+2)/[(2K+3)(K+2+beta)].

It is less than one because the denominator minus the numerator is
(2K+3)(beta-1)-1>0. Each summand decreases for every integer K>=0.
The sum is finite, so U(K)<=U(K0). This proves (2) over the entire
unbounded set of integer indices.

## Independent exact projection reconstruction

Use this lane's audited polar fields

    R=r sum v^a_j R_jn(t) sin(n theta),
    psi=r^2 sum v^a_j S_jm(t) sin(m theta), a_j=(j+1)delta/2.

For g0=1-4t and v=1-t, the weak identity I_K=-int R M_K expresses
its radial polynomial as A_ell+K B_ell. Linear first-sine terms give

    A_(j+1) += -R_j1[(2c+1)+c g0],
    B_(j+1) += -2cv R_j1.

For each pair with |n-m|=1, put sigma=sign(n-m) and
D S=(2-2a_j t)S+2tv S'. Its contributions at ell=j+k+2 are

    A_ell += R_kn[sigma m S_jm g0-D S_jm]/2,
    B_ell += sigma m v R_kn S_jm.

All other angular pairs vanish. Integrating the K term by parts in t
then recovers the exact first-sine residual polynomial

    P_ell=A_ell-2B_ell-t B_ell'
                       +(ell delta/2-1)t(B_ell/v).     (4)

The quotient is exact because B_ell is divisible by v. Boundary terms
vanish by the positive branch exponents and the explicit factor t^2
at the origin. Formula (4) includes every nonlinear pair. The checker
compares its coefficients exactly with the independently assembled
Cartesian projection, then verifies the finite v-endpoint expansion
and its minimum exponent. No agreement of a few sample values replaces
this exact polynomial comparison.

## Numerical verification and interpretation

At each listed K0, evaluate the complete positive Beta sum using Arb
Gamma with exact positive rational inputs. Compare with both peer
containing intervals, verify the peer's strict rational upper bound,
and compare the signed sum with this lane's complete direct pairing.
A positive recurrence in j supplies a separate evaluation. All output
intervals must retain more than 150 relative bits.

An additional explicitly tested K0 can be compared with the independently
proved incumbent 0.004769166867. If U(K0) is strictly smaller, none of
these first-mode tests with K>=K0 can improve that incumbent. This says
nothing about smaller K, other angular modes, or existence of a solution.
All raw coefficient arrays are retained as exact JSON with hashes.
The only new analytic input beyond the earlier complete-projection
proof is (3) and the elementary monotonicity calculation above.
