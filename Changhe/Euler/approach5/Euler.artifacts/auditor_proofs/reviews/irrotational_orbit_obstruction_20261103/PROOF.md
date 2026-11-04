# Exact irrotational profiles with growing strain along an outgoing orbit

Status: A582 CONFIRMED and A583 corrects a refuted necessity claim, after full independent reconstruction and proof postread. These are exact local obstructions to an inference from shrinking tubes. They are not decaying global counterexamples. Verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md).

## 1. Exact potential construction

Let Omega be an open subset of R3 and phi a harmonic function there. Put U=grad phi, A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0), a=1-2c, and

    P=-a phi-U.Ay-|U|^2/2.                           (1)

For arbitrary real c and omega, U,P are smooth and satisfy the full local incompressible rotating Euler profile equation. Indeed div U=Delta phi=0, DU is symmetric and

    grad(U.Ay)=DU Ay+(cI+omega J)U,
    grad(|U|^2/2)=DU U.

Substitution gives (1-c)U+DU(Ay+U)+omega JU=-grad P. Its vorticity vanishes, so all vorticity transport equations hold. Harmonicity is essential to the incompressibility assertion.

For the outgoing-orbit examples assume c>0. Write cylindrical coordinates rho^2=x^2+y^2 and z, with J along the z-axis. The positive axis is one B=Ay+U orbit in each example below, since U=0 there and z'=cz. Rotation does not change this conclusion for any omega.

## 2. Polynomial and exponential examples

The harmonic polynomial phi=(x^2-y^2)z gives

    U=(2xz,-2yz,x^2-y^2),
    DU(0,0,z)=diag(2z,-2z,0).                        (2)

Its largest strain eigenvalue is2z on the positive axis, so it is not O(sqrt z). For z>=1 and0<m<=1,

    |U|<=2rho z+rho^2<=m/2+m^2/(16z^2)<m
       whenever rho<=m/(4z).                        (3)

The parameter m may itself be a positive function of z bounded by1. Thus arbitrarily small velocity on suitably shrinking tubes is consistent with growing strain.

For any k>0 a second example is

    phi=exp(kz)J_2(k rho)cos(2theta),                (4)
    J_2(t)=sum_(j>=0) (-1)^j (t/2)^(2j+2)/[j!(j+2)!].

Multiplying the series by cos(2theta) writes each term as a scalar multiple of (x^2-y^2)(x^2+y^2)^j. It converges with all derivatives on compact Cartesian sets, including the axis. The series obeys Bessel's equation t^2 J_2''+t J_2'+(t^2-4)J_2=0 by matching coefficients, so the cylindrical Laplacian of(4) vanishes. The quadratic Cartesian term is exp(kz)k^2(x^2-y^2)/8; hence

    DU(0,0,z)=(k^2/4)exp(kz)diag(1,-1,0).            (5)

This is faster than every power of z and grows doubly exponentially in the carrier time s, because z(s)=z(0)exp(cs).

The bounds needed for its tube estimate are exact. For0<t<=1 the alternating positive term magnitudes in J_2 decrease, since their successive ratio is t^2/[4(j+1)(j+3)]<1. In its differentiated series the corresponding ratio is t^2(j+2)/[4(j+1)^2(j+3)]<1. Alternating-series bounds therefore give

    0<J_2(t)<=t^2/8, 0<J_2'(t)<=t/4.                (6)

The horizontal gradient components of(4) are bounded in absolute value respectively by exp(kz)k^2rho|cos(2theta)|/4 and exp(kz)k^2rho|sin(2theta)|/4. Their combined norm is at most exp(kz)k^2rho/4. The vertical component is at most exp(kz)k^2rho/8 when k rho<=1. It follows that

    |U|<=(3/8)k^2rho exp(kz)<=m

whenever rho<=min(1/k,8m exp(-kz)/(3k^2)). This proves the estimate on the whole interval, without the source's numerical grid. Both examples are globally defined smooth exact profiles, but are unbounded and do not decay globally. They satisfy the target local equations for every rotation rate.

## 3. What ball smallness actually proves

If Delta phi0 on B(y,rho), U=grad phi and sup_ball|U|<=m, then

    ||DU(y)||_op<=3m/rho.                            (7)

For a unit vector e the scalar u=U.e is harmonic. Mean value and the divergence theorem on any smaller ball give

    grad u(y)=|B_r|^-1 integral_(partial B_r)u n dS,
    |grad u(y)|<=3m/r.

Let r increase to rho and then take the supremum over e. This proves(7) without needing boundary smoothness of phi on the radius-rho closed ball. The source statement is valid with its implicit harmonicity hypothesis made explicit; U=grad phi alone would not suffice.

The scaling is sharp up to a bounded factor for(2). Center the ball at(0,0,Y),Y>0. The limiting boundary point(rho,0,Y) has |U|=rho sqrt(4Y^2+rho^2)>=rho||DU(0,0,Y)||. On the entire ball,

    sup |U|<=2rho(Y+rho)+rho^2
             =rho||DU(0,0,Y)||[1+3rho/(2Y)].        (8)

A boundary value is understood as a limit of values inside the open ball.

The precise sufficient conditions from(7) are m/rho=O(sqrt |y|) for that derivative growth bound, and m/rho->0 for derivative decay. A radius bounded below together with m->0 is sufficient for the second, but is not necessary: rho=sqrt m->0 still gives m/rho=sqrt m->0. Thus the source's sentence that derivative decay needs radius bounded below is false. Nor is a universal statement about what every proof must use established by(7). What(2)-(6) refute is a universal local inference from arbitrarily narrow low-velocity tubes alone.

## 4. The canonical-pressure distinction in the constant-strain core

For the affine irrotational field U=Gy with G=diag(lambda,-lambda,0), formula(1) gives

    D^2 P_pot=-G-G^2+omega(GJ-JG).                  (9)

Indeed the quadratic part U.Ay has symmetric Hessian GA+A^T G, and a+2c=1. The rotational commutator in(9) is symmetric. This verifies the same local calculation in the A505 cusp core, where the velocity equals this field.

If P_N is the canonical Newtonian pressure of the global A505 velocity and R its momentum residual, then inside that core R=grad(P_N-P_pot). For the quarter-turn matrix Q the global construction obeys U(Qy)=-Q U(y), so DU(Qy)=-Q DU(y)Q^T and tr((DU)^2)(Qy)=tr((DU)^2)(y). Its Newtonian pressure is therefore invariant under Q. The velocity has this signed transformation, not ordinary equivariance. A scalar invariant under that quarter turn has an axial Hessian diag(alpha,alpha,beta). Consequently

    (DR)_11-(DR)_22
      =-[(D^2P_pot)_11-(D^2P_pot)_22]=2lambda.      (10)

Thus its global canonical pressure fails the local exact-pressure equation. Equation(10) is the already confirmed A505 distinction, not a new Euler counterexample. In a true globally decaying profile A031,A500 fix the canonical pressure gradient. On any connected irrotational region where U=grad phi, its canonical pressure and(1) differ by a constant. Local harmonic potentials need not be globally single valued on an arbitrary multiply connected irrotational region; the assertion always holds on each such potential patch.

A globally irrotational decaying profile is zero, because Delta U=grad div U-curl curl U=0 and its bounded harmonic components vanish by Liouville. The examples above therefore leave global nonexistence unresolved. They do not establish the existence of a global decaying profile with unbounded vorticity, or exhaust every possible route to the derivative screen.

## 5. Verification and scope

The full C44 source, including its A505 addition, was read. The polynomial algebra, entire Bessel series, alternating bounds, all endpoint estimates and pressure Hessian were independently reconstructed here; no numerical evaluation was needed. The configured-model source and continuing file exchange provide the model collaboration. No external theorem beyond elementary harmonic mean value and Liouville is imported. All local assertions explicitly retain incompressibility and the chosen exact pressure, and all examples explicitly fail the global decay hypothesis.
