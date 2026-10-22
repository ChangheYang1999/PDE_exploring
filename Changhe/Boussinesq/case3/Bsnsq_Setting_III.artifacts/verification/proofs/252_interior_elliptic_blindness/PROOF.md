# Interior Poisson residuals do not bound velocity error, even with matching center jets

## Exact statement and scope

Fix a disk B_R centered at0, a finite nonnegative integer J and a positive number M. There exist smooth compactly supported full-plane functions deltaPsi and deltaOmega=-Delta deltaPsi with the prompt's odd x-reflection symmetry such that:

1. deltaOmega vanishes on B_R, and deltaU=(-deltaPsi_y,deltaPsi_x) is exactly its canonical full-plane velocity. It vanishes outside B_(2R), hence is sublinear. The exact inverse identity below excludes an added global harmonic velocity.
2. Every derivative of deltaU at0 through order J vanishes. In particular its center velocity and strain vanish. All vorticity jets at0 vanish.
3. At a fixed nonzero point of B_R, |deltaU|=M. Its divergence and its vorticity vanish identically throughout B_R. Every harmonic polynomial moment of deltaOmega is zero.

Consequently neither an interior Poisson residual, even if known to vanish on an entire disk rather than at a finite sample, nor this residual combined with center jets, sublinear behavior, and these exterior harmonic moments yields a bound on the interior velocity error. Applied to a target pair (Psi,Omega), the approximate stream Psi+deltaPsi has the same interior Poisson residual as Psi and preserves the target velocity jet at0 through order J, while its velocity error at the chosen point is arbitrarily large. The convention throughout is Omega=partial_y U_1-partial_x U_2, the negative of the usual planar curl, exactly as fixed by PROMPT.md. The approximate stream is the canonical inverse of Omega+deltaOmega, not of the unchanged target Omega. The missing error is an exterior source residual. A verified full-plane residual or an independent full-plane velocity comparison detects it.

This is a diagnostic counterexample, not a B2 profile and not evidence that a particular numerical inverse has this error. It strengthens the affine harmonic manufacture in P171 by maintaining global sublinearity, no added harmonic velocity, and arbitrarily many matching center jets. It does not invalidate the usefulness of sampled elliptic residuals; it specifies the additional information that they do not supply.

## Construction and full-plane inverse

Let eta(t)=exp(-1/t) for t>0 and0 for t<=0. Define

    chi(s)=eta(4-s)/(eta(4-s)+eta(s-1)).

The denominator is strictly positive for every real s. The usual one-sided derivative formulas for eta are finite sums of powers of1/t times exp(-1/t), all tending to0 as t decreases to0. Thus eta and chi are smooth. We have chi=1 on s<=1 and chi=0 on s>=4. Choose an odd integer N>=max(3,J+2), and let

    P_N(x,y)=Re((x+i y)^N),
    s=(x^2+y^2)/R^2,
    deltaPsi=A P_N chi(s).

P_N is a real homogeneous harmonic polynomial of degree N. Reflection x to-x gives (-1)^N P_N=-P_N, so the required parity holds. The cutoff is radial and even. All fields are smooth, and deltaPsi vanishes outside B_(2R), with every derivative matching0 there. On B_R it equals the harmonic polynomial A P_N, so deltaOmega=0 there.

For an explicit source formula, Euler's identity gives X.grad P_N=N P_N, while grad s=2X/R^2 and Delta s=4/R^2. The product rule therefore yields

    Delta(P_N chi(s))=(4/R^2) P_N [s chi''(s)+(N+1)chi'(s)],
    deltaOmega=-(4A/R^2)P_N[s chi''+(N+1)chi'].

Its support lies in the closed annulus R<=r<=2R. Define Gamma(X)=-(1/(2pi))log|X|, so -Delta Gamma=delta_0 in distributions. Because deltaPsi is smooth with compact support, convolution and distributional integration by parts give

    Gamma*deltaOmega=Gamma*(-Delta deltaPsi)
                    =(-Delta Gamma)*deltaPsi=deltaPsi.

All logarithmic convolutions in this identity are absolutely integrable: the source is smooth with compact support, and the logarithmic singularity is locally integrable. Differentiation gives exactly the ordinary full-plane Biot-Savart velocity, with the prompt's kernel K(Z)=(Z_2,-Z_1)/(2pi|Z|^2). Thus the displayed compact velocity is canonical. No unspecified boundary value or harmonic addition is used. Its zero center value means that relative and absolute velocity coincide for this perturbation.

For every real harmonic polynomial H, ordinary integration by parts on a disk containing the support, where all boundary derivatives of deltaPsi vanish, gives

    integral_R2 H deltaOmega=-integral_R2 deltaPsi Delta H=0.

This covers the mass and every harmonic multipole. It does not assert that all nonharmonic polynomial moments vanish. Those identities are consistent with the velocity vanishing outside the larger disk.

## Center jets and arbitrarily large interior velocity

On B_R the perturbation velocity is the derivative of a degree N homogeneous polynomial. It has degree N-1, so all its derivatives at0 through order N-2 vanish. By the choice N>=J+2 this includes the required J derivatives. Since deltaOmega is identically0 near0, it has every zero jet there. For N=3,

    P_3=x^3-3xy^2,
    deltaU=(6Axy,3A(x^2-y^2)) on B_R.

This shows explicitly that both U(0) and DU(0), hence the B2 center strain, remain unchanged.

Choose r0=R/2. At X0=(r0,0), P_N,x=N r0^(N-1) and P_N,y=0. Taking A=M/(N r0^(N-1)) gives deltaU(X0)=(0,M). The amplitude M is arbitrary. The divergence identity follows from equality of mixed derivatives, and the vorticity is zero on B_R by harmonicity. Thus the claimed interior error is compatible with exact vanishing of every interior elliptic and divergence diagnostic.

For a general canonical target pair, linearity shows Psi+deltaPsi is the canonical inverse of the modified source Omega+deltaOmega, whenever the original inverse is well defined. Holding the target Omega fixed instead gives an error residual deltaOmega supported outside the checked disk. The correct inverse of that fixed source is unique in the chosen full-plane gauge; the perturbation does not supply a second inverse of the same source. It supplies an approximation error that the stated local tests cannot distinguish. Other B2 transport residuals or whole-plane error estimates are additional tests and may distinguish it immediately.

## Size of the exterior error

The example does not make the full exterior residual small. With the displayed normalization,

    ||deltaOmega||_infinity=(M/R) C_N,
    C_N=(2^(N+1)/N) max_(1<=s<=4)
          s^(N/2)|s chi''(s)+(N+1)chi'(s)| > 0.

If the bracket were identically zero, (s^(N+1)chi')'=0 on(1,4); the flat endpoint derivative would force chi'=0 there, contrary to chi(1)=1 and chi(4)=0. At X0 the distance to the source annulus is at least R/2, so the canonical kernel and annular area give the elementary estimate

    M=|deltaU(X0)| <= 3 R ||deltaOmega||_infinity.

This illustrates a bound using information over the entire source support. Such information is absent from an interior residual measurement.

## Verification and dependencies

Before coding, the proof fixes the exact bump, source, parity, center order, inverse convention and scope. The controls will differentiate the polynomial and a symbolic radial cutoff in Cartesian coordinates, check the source formula and exact center derivatives for several N, and compare a separately implemented physical annulus quadrature against the known interior velocity. That quadrature is a floating-point manufactured test, not needed as a premise of the proof. It imports no numerical-lane evaluator and uses no GPU, JavaScript/TypeScript, server, cluster, Lean or Lake. Dependencies are the displayed product rule, elementary smooth bump construction, the logarithmic fundamental solution and integration by parts with compact support. No theorem about the coupled B2 equations follows.
