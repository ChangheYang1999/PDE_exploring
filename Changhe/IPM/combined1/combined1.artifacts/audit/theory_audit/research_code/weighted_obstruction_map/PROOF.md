# Independent audit of the weighted energy obstruction map

## Statement and hypotheses

Let c>1, gamma=1/c, delta=1-gamma. Consider a finite smooth S1 potential

    chi=sum_(j,m) Re(z^(2m)) (1+r^2)^(p_j-m) P_(j,m)(t),
    p_j=(3+gamma-j delta)/2, t=r^2/(1+r^2), j>=0,

where each P is a polynomial and the sum is finite. Define rho=-partial_y Delta chi, u=(-partial_xyy chi,partial_xxy chi), and V=cX+u. Assume that u is the canonical velocity and that the compact signed decomposition in ../principal_energy_obstruction/PROOF.md holds. The exact state131 input belongs to this finite family; its canonical identification is an existing campaign dependency.

For 0<=a<2 and R>0 set w=(1+r^2/R^2)^(-a/2),

    b=a V.X/(R^2+r^2),
    lambda=b+(|D rho|-rho_y)/2,
    Lambda=ess sup lambda.

If the real part of the conjugated linearized operator, with any bounded compact additive correction, is at most -beta times the squared L2 norm on the compact smooth S1 core, then

    beta <= c+1-Lambda <= c+1-ac.                         (1)

This remains true on the normalized cores covered by the principal obstruction theorem. Thus a positive rate requires a<1+gamma. Rate2 requires a<=1-gamma. Neither condition proves a positive rate or an inverse estimate.

For any fixed nonzero point X with V.X>0, lambda decreases as R increases. Therefore a certified strict inequality lambda(X)>c+1 at R=R0 excludes a positive energy rate for every 0<R<=R0. The accompanying calculation seeks six such axis witnesses for the parameter endpoints in T1 TP-3. Finite numerical records are separate from the proof of (1).

## Homogeneity count

Write q=r^2 and G(q)=(1+q)^d P(q/(1+q)), where d=p_j-m. Direct differentiation gives

    G^(k)(q)=(1+q)^(d-k) Q_k(t),
    Q_0=P,
    Q_(k+1)=(d-k)Q_k+(1-t)Q_k'.                         (2)

This follows from dt/dq=(1+q)^(-2), so it is an identity, not an asymptotic expansion. Each Q_k is a polynomial bounded on0<=t<=1. Each Cartesian derivative of z^m zbar^m or z^(2m)G(q) lowers the total growth exponent by one: differentiating the monomial lowers its degree by one, while differentiating G adds one coordinate and lowers the radial power by two. Induction gives D^k chi=O(r^(3+gamma-k)) for r>=1, uniformly in angle. The finitely many j>=0 only lower this exponent. Smoothness controls r<=1.

Consequently u=O(r^gamma), D rho=O(r^(gamma-1)), and u=o(r) because gamma<1. In particular D rho and b are bounded. Uniformly in angle,

    a(c r^2+X.u)/(R^2+r^2) -> ac,
    (|D rho|-rho_y)/2 ->0.

Thus lambda->ac and Lambda>=ac. The first inequality in(1) is the independently reviewed T4-047 theorem. This proves the claimed rate ceiling. The endpoint a=1+gamma gives beta<=0 as well; no strict asymptotic margin is needed for that exclusion.

A profile-like power r^gamma is square-integrable against w^2 at infinity exactly when a>1+gamma, since the radial integral is proportional to integral r^(2gamma-2a+1)dr. This explains the threshold but does not replace the operator argument or assert that a patched profile power is an exact neutral mode.

## Axis witnesses and monotonicity

The independent polar reconstruction writes

    rho=r sum_(j,n) u0^a_j R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,n) u0^a_j S_(j,n)(t) sin(n theta),
    u0=1-t, a_j=(j+1)delta/2, u=(-psi_y,psi_x).

On the positive x axis,

    rho_x=u2=0,
    rho_y=sum u0^a_j n R_(j,n)(t),
    u1=-r sum u0^a_j n S_(j,n)(t).

All polynomial coefficients and rational points are exact. Positive powers are enclosed by Arb. The code verifies both Z=c r^2+r u1>0 and

    a Z/(R0^2+r^2)+(abs(rho_y)-rho_y)/2-(c+1)>0.

For R<=R0 the denominator is smaller and Z positive, so the same point remains a strict witness. This verifies an entire interval of R values, without interpreting sampled maxima as upper bounds. For a=8/5, the all-R exclusion also follows directly from(1).

## Status and limitations

The homogeneity and monotonicity arguments independently confirm the analytic part of T1 TP-3. The six numerical endpoint witnesses, if all checks pass, cover its58 discrete claimed entries and additionally all positive R below the listed endpoints. Their exact data and output hashes belong in the audit ledger.

T1's nonpositive sampled maxima remain FLOAT observations. An upper certificate for Lambda requires a full-plane bound. The displayed velocity-constant/rate ratios should be read as budgets for the selected sufficient constant: an upper estimate for the true velocity norm cannot supply a lower bound for the true norm. General nonlocal changes of inner product and stationary inverse arguments lie outside the obstruction.
