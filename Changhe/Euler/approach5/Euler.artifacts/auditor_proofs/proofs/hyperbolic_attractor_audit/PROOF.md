# Vorticity on a nonsingular hyperbolic backward attractor

## Statement and precise assumptions

Let c be in (0,1/2), omega real, and let U in C^2(R^3), P in C^1(R^3)
solve the complete divergence-free profile equation. Assume U=o(|y|)
uniformly. Write B=cy-omega Jy+U, Omega=curl U, Psi_t=Phi_-t and a=1-2c.
Let A be a compact uniformly hyperbolic attractor for Psi, with B nonzero
on A. Assume its strong stable foliation on the open basin is a C^1
foliation. Here a C^1 foliation means local C^1 diffeomorphism charts whose
coordinate lines or planes are the strong stable leaves; no C^1 transverse
derivative of a unit tangent field is silently assumed.

Then Omega is tangent to the strong stable leaves. If Omega vanishes at
z in A, it vanishes on the weak stable manifold W^s(z). If Omega vanishes
on A, it vanishes throughout the basin. These are CO4(a,b), with the proof
below repairing the dimension omission in the submitted proof. No Livsic,
SRB, or entropy claim is included in this verdict.

## Hyperbolic estimates used

For a nonsingular uniformly hyperbolic flow, exponentially decaying tangent
vectors at a point in the basin are exactly the tangent space E^ss to its
strong stable leaf. Along each such orbit the strong stable derivative is
bounded by C_x exp(-lambda t), for some lambda>0, after absorbing the finite
initial segment into C_x. Each basin point belongs to W^ss(z) for some
z in A. These are the standard strong stable foliation properties contained
in the hypothesis. The flow direction is transported by
D Psi_t B(x)=B(Psi_t x), whose norm stays bounded and is eventually bounded
away from zero. On A there is the uniformly hyperbolic splitting
E^ss+R B+E^u, with bounded angles and uniform expansion on E^u.

The exact Cauchy formula gives

    D Psi_t(x) Omega(x)=exp(-(1+c)t) Omega(Psi_t x).

The orbit on the right is bounded, so the vector on the left decays
exponentially. Therefore Omega(x) is tangent to E^ss throughout the basin.

## One-dimensional leaf lemma with C^1 charts

Let W be a C^1 divergence-free field tangent to a C^1 one-dimensional
foliation. In a foliated chart F(s,z), z in R^2, write

    W(F(s,z))=w(s,z) d_s F(s,z),  J=det DF,

choosing the chart orientation so J>0. Both w and J are continuous. The
change-of-variables formula for divergence, in distributions, gives

    d_s(J w)=0.

This may also be proved directly by applying the divergence theorem to
foliated boxes: lateral faces have zero flux, and the two transverse fluxes
are the integrals of Jw. As this holds on every transverse sub-box,
continuity gives J(s,z)w(s,z) independent of s for every z. Thus if W
vanishes at one point of a leaf, it vanishes along that connected leaf.
Overlapping charts propagate the conclusion. This argument avoids claiming
that a C^1 foliation necessarily has a C^1 unit tangent field.

If dim E^ss=1, apply this lemma with W=Omega, since div curl U=0.
Zeros propagate along strong stable leaves. They also propagate along B
orbits by the Cauchy formula, so the conclusion holds on the weak stable
manifold, the union of strong stable leaves over the orbit of z.

## The omitted two-dimensional stable case

If dim E^ss=2, the basin tangent space is E^ss+R B. Every two-vector
therefore contains at least one stable factor. The derivative estimates
above give, for each x in the basin,

    ||wedge^2 D Psi_t(x)|| <= C_x exp(-lambda t).

Let sigma=i_Omega vol=d(U^flat). The exact vorticity two-form law is

    Psi_t^*sigma=exp(a t)sigma.

Since sigma is bounded along the compact backward orbit,

    |sigma(x)| <= C_x exp(-(a+lambda)t).

Letting t tend to infinity gives Omega(x)=0 throughout this part of the
basin, independently of whether vanishing on A was assumed.

The remaining rank possibility dim E^ss=0 cannot occur: on the compact
attractor, the two unstable directions expand uniformly and the flow
direction has uniformly bounded norm above and below. Bounded splitting
angles would force det D Psi_t to grow exponentially. But its exact value
is exp(-3ct), a contradiction. These arguments also apply componentwise
when the stable rank differs on different components.

Thus the one-dimensional leaf proof plus the two-dimensional two-form
proof establish the entire stated result. The original argument's use of
a one-dimensional lemma for all stable dimensions was incomplete, but the
claim has this repair.

## Scope and dependencies

The uniform hyperbolicity and C^1 foliation are H6, not consequences of the
Euler equation or decay. A recurrent set with singularities, a merely
Hölder foliation, or a nonuniformly hyperbolic attractor is not covered.
The argument uses the exact Cauchy and two-form identities already confirmed
in the team records and the explicitly stated stable-foliation
properties. It does not exclude a vortical hyperbolic attractor with
one-dimensional stable leaves.

Audit recorded: 2026-11-02T18:46:07Z
