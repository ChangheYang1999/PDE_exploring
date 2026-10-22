# Moving-center reconstruction, signed scaling, and observer changes

Status: independently proved identities. They apply to an exact profile; an approximate profile reconstructs an approximate physical solution with the scaled residuals displayed below.

## Hypotheses and notation

Let beta>0, tau=T-t>0, z_* lie on the vertical axis, and let the profiles solve the equations in the prompt with U=(-Psi_y,Psi_x), -Delta Psi=Omega and v0=U(0). Reflection in x makes v0 vertical. The canonical inverse must specify how this absolute constant is fixed; the relative inverse alone does not determine it.

Define

    z_c(t)=z_*-v0 tau^beta/beta,
    X=(z-z_c(t))/tau^beta,
    omega(t,z)=tau^-1 Omega(X),
    theta(t,z)=tau^(beta-2) Theta(X),
    u(t,z)=tau^(beta-1) U(X),
    psi(t,z)=tau^(2beta-1) Psi(X).

Then z_c'=tau^(beta-1)v0=u(t,z_c), so the center is material. Direct differentiation gives

    partial_t X=(beta X-v0)/tau,
    omega_t+u.grad_z omega-theta_z1 = tau^-2 R_Omega(X),
    theta_t+u.grad_z theta = tau^(beta-3) R_Theta(X),
    -Delta_z psi-omega = tau^-1 E(X).

These identities prove reconstruction and its residual scaling. They do not supply bounded or finite-energy physical initial data. If beta>2 and Theta is nonzero, the bounded-temperature exclusion implies that the spatial temperature is unbounded at every fixed t<T in the sublinear velocity class.

## The material center in fixed similarity coordinates

Put Y=(z-z_*)/tau^beta=X-v0/beta and define bar f(Y)=f(Y+v0/beta) for each profile. Then

    beta Y+bar U(Y)=beta X+U(X)-v0=W(X).

Thus the translated profiles obey the fixed-center similarity equations, while their distinguished material point is Y_c=-v0/beta and satisfies beta Y_c+bar U(Y_c)=0. This coordinate identity does not set U(0)=0 or make the required quadratic jet occur at Y=0. A numerical method that uses the fixed-center equations and imposes the B2 jet at Y=0 without this shift solves a different constrained problem when v0 is nonzero.

## Signed spatial scaling

For every real lambda != 0 define

    Theta_lambda(X)=lambda Theta(X/lambda),
    Omega_lambda(X)=Omega(X/lambda),
    Psi_lambda(X)=lambda^2 Psi(X/lambda),
    U_lambda(X)=lambda U(X/lambda).

The chain rule preserves both transport equations, the elliptic relation, and the parity. It gives

    beta_lambda=beta,
    a0_lambda=a0/lambda,
    b0_lambda=b0/lambda,
    c_lambda=c,
    v0_lambda=lambda v0.

Sublinear velocity and polynomial control are preserved. Taking lambda=a0 normalizes a0=1, including a0<0. The negative transformation is a true symmetry of the displayed vorticity-temperature system. Using x parity, lambda=-1 can equivalently be written as reflection in y with Theta and Omega changing sign and the appropriately transformed velocity. It is not an assumption of y symmetry.

The canonical relative inverse is covariant under this scaling by its uniqueness. An absolute inverse prescription must also transform covariantly for the displayed v0 scaling to hold without a further observer adjustment. A finite-part convention with an externally fixed length scale must be checked separately. The PDE identities alone cannot certify an unstated absolute convention.

## A time-dependent observer change must translate all fields

For a C^2 vertical displacement a(t), the exact transformed fields are

    theta_new(t,z)=theta(t,z-a(t)),
    omega_new(t,z)=omega(t,z-a(t)),
    u_new(t,z)=u(t,z-a(t))+a'(t).

The terms from differentiating z-a(t) cancel the added transport velocity. The vorticity and temperature equations are therefore unchanged. A stream is

    psi_new(t,z)=psi(t,z-a(t))+a'_2(t) z_1,

up to an irrelevant additive function of time. The material center becomes z_c+a. A uniform acceleration is absorbed into a linear pressure in the momentum formulation.

In particular, adding a profile velocity d corresponds to a(t)=-d tau^beta/beta and a'(t)=d tau^(beta-1). It changes the absolute drift from v0 to v0+d and translates the physical scalar fields. Adding tau^(beta-1)d to u while leaving theta and omega as the same functions of (t,z) is generally false as a symmetry: their equations acquire tau^(beta-1)d.grad theta and tau^(beta-1)d.grad omega.

## Audit scope

CONFIRMED: prompt reconstruction, signed scaling, unchanged beta, and a0=1 normalization with a compatible canonical convention.

REFUTED if read literally: the lead SPEC A5 and interim FINAL_REPORT statement that adding velocity and replacing the center alone leaves the same physical theta and omega solving their equations. It is repaired by the translations above.

OPEN: a complete published absolute-velocity convention for the nonintegrable-tail branch. Relative PDE computations are meaningful before it is fixed, but a final physical reconstruction must state it explicitly.

Update 2026-10-20T16:27:02.207984+00:00: the previous OPEN convention item is resolved by
SPEC v7 A5. The lead explicitly selects v0=0 for reconstruction while
retaining every vertical v0 through the translated-field observer
change proved above. This is a declared representative, not an added
vanishing moment or a restriction to B1. The relative kernel remains
the canonical object and its ordinary truncated drift is diagnostic.
Verdict: CONFIRMED as a complete stated observer convention.
