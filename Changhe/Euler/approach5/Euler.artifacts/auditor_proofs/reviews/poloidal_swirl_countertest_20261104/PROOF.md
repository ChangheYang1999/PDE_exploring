# Independent audit of the poloidal-swirl pressure countertest

Status: independent reconstruction and full existing coordinator comparison complete; designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). Source: in the team records, pinned in the team records.

## 1. Exact statement and scope

Let rho^2=x^2+y^2, r^2=rho^2+z^2 and b=sqrt(6). On R3 set

    V=(z(x-by),z(y+bx),-r^2),
    E=rho^4+9rho^2 z^2+z^4,
    P=2E/17+z^4/34.

Then V and P are homogeneous polynomials of degrees two and four, respectively, div V=0, E=|V|^2 and -Delta P=tr((DV)^2). They have V(0)=DV(0)=P(0)=0 and P>=2|V|^2/17. V has only the origin as a zero; the displayed ratio has infimum 2/17 attained on the punctured plane z=0. Upon normalization this gives Gamma_2>=2/17 for the all-quadratic Poisson optimization of LIT318. This is not a maximization over pressures or velocities. The fields are not stationary Euler fields or rotating self-similar profiles with the displayed pressure, and do not decay.

## 2. Algebraic identities

The derivative matrix is

    DV=[[z,-bz,x-by],[bz,z,y+bx],[-2x,-2y,-2z]].

Its trace is zero. The diagonal-square contribution to tr((DV)^2) is 6z^2, the xy pair contributes -2b^2 z^2=-12z^2, and the xz and yz pairs together contribute -4rho^2. Thus tr((DV)^2)=-4rho^2-6z^2.

The horizontal square norm is (1+b^2)rho^2 z^2=7rho^2 z^2. Adding r^4 gives E as stated. In particular V_z=-r^2 already proves that V has only one zero.

The identities Delta rho^4=16rho^2, Delta(rho^2 z^2)=2rho^2+4z^2 and Delta z^4=12z^2 give Delta E=34rho^2+48z^2. Hence

    Delta P=4rho^2+(96/17+6/17)z^2=4rho^2+6z^2.

All equations hold classically everywhere, so also distributionally. The pressure has no added constant, and all center normalizations follow from homogeneity.

## 3. Ratio and admissible normalization

The pointwise defect P-2E/17 is exactly z^4/34. At any z=0 with rho>0, E=rho^4>0 and the defect is zero. This proves the exact minimum for this particular pair.

Write angle brackets for normalized sphere measure. Rotational symmetry and integration of z in [-1,1] give <z^4>=1/5 and <x^2 z^2>=<y^2 z^2>=1/15. Thus <rho^4>=8/15, <rho^2 z^2>=2/15 and <E>=29/15. Set Q=sqrt(15/29)V and R=15P/29. Then <|Q|^2>=1, div Q=0, -Delta R=tr((DQ)^2), and R>=2|Q|^2/17. This is exactly the required feasible point for Gamma_2; no compactness or attainment theorem is needed to infer its lower bound.

Since sqrt(30)>5, the fixed-swirl optimum (6-sqrt(30))/24 is less than 1/24, while 2/17>1/10. The improvement is strict. Also 2/17<1/6. It does not decide whether Gamma_2 exceeds 1/6, nor the optimal smooth threshold. Any upper bound for Gamma_2 has its own separate dependencies and audit status.

## 4. Exclusion from the full profile problem

Let J(x,y,z)=(-y,x,0). The cylindrical components are V_r=rho z, V_theta=b rho z and V_z=-r^2; hence V is equivariant for rotations about the z-axis and DV(Jx)=JV. Euler homogeneity gives DV(x)=2V. The residual in the rotating similarity equation at parameters c and omega is therefore

    (1-c)V+DV((cI-omega J)x+V)+omega JV+grad P
      =(1+c)V+DV(V)+grad P.

The first term has degree two and the remaining two have degree three. If this identity vanished in a centered open ball, restriction to tx, division by t^2 and t tending to zero would give (1+c)V(x)=0 for every x in that ball. For 0<c<1/2 the coefficient is positive and V(x) is nonzero off the origin, a contradiction. The cancellation is exact for every real omega. No single-rotation approximation is used.

On the z-axis, DV(V)=(0,0,2z^3) and P=5z^4/34, giving grad P=(0,0,10z^3/17). Thus the stationary residual is (0,0,44z^3/17), which is nonzero for z!=0. Quadratic growth also violates profile decay independently. This is a countertest only to conflating a fixed-velocity optimum with the all-velocity problem; it is not a counterexample to any confirmed Euler nonexistence theorem.

## 5. Verification and dependencies

All six source sections were read. The reconstruction above uses exact polynomial differentiation, b^2=6, sphere moments, scaling and distinct homogeneous degrees. No numerical search or optimization output is used as proof. No computation was needed for these identities. The source's numerical experiment is motivational and has not been independently rerun in this audit. No formal source or Lean/Lake build is supplied.

The completed existing configured model coordinator comparison is recorded in Section 6; its actual provider runtime is independently unattested. No new model client or agent was launched.

## 6. Completed coordinator comparison

All five items of in the team records and the complete shared in the team records were read. They agree with the exact identities and scope above. The comparison says the pair fails the profile equation for every real c, which can also be checked: Section 4 excludes every c other than -1 by homogeneous degrees, while at c=-1 the displayed nonzero stationary residual remains. Thus there is no exceptional similarity parameter, and the cancellation of omega is exact. The main application needs only 0<c<1/2.

The improvement of the lower bound for Gamma2 does not identify an optimizing velocity or pressure. In particular it does not contradict the fixed-velocity optimum of LIT319. The existing coordinator is configured as model; actual provider runtime is independently unattested. Its shared exact-check log was read but not rerun. No numerical optimization output or new computation is a proof dependency.
