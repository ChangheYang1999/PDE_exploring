# Unstable conditional density in transverse alpha-length

Written: 2026-11-02T21:53:21Z. A207: CONFIRMED with the flow-orientation and normalization qualifications below.

## Statement

Let B,W be C2 and C1 respectively near a compact invariant set, with complete carrier flow there, and let alpha be a C1 one-form satisfying

    alpha(B)=alpha(W)=0,
    Psi_t*alpha=exp(a t)alpha,    L_W alpha=0,    a>0,

where Psi_t is the backward B flow. Let mu be an invariant probability for F=Psi_1 with simple spectrum (+,0,-), absolutely continuous unstable conditional measures, and

    E^s plus E^0=span(W,B)=ker alpha

at mu-almost every point. In particular alpha is nonzero on the unstable direction there. Then on almost every local unstable conditional plaque, the conditional density is constant with respect to the length element |alpha restricted to the plaque|. The constant normalizes that particular plaque and may vary with the plaque.

This applies to the vortical SRB branch of the smooth or C2 Euler setting, whenever such a measure is given, with alpha=(B cross Omega).dy and a=1-2c. Its proof does not depend on the 2026 existence theorem.

Any C1 holonomy map actually defined by following W orbits preserves alpha. A map following Psi-time s(p) multiplies alpha by exp(a s(p)); one following the forward B flow Phi-time s(p) multiplies it by exp(-a s(p)). Existence of a holonomy between arbitrary one-dimensional curves is not asserted.

## Density proof

Let e^u(x) be a Riemannian unit vector tangent to the unstable manifold, and put A(x)=|alpha_x(e^u(x))|. At regular points A>0. The one-form covariance gives the unstable Jacobian

    J^u F(x)=exp(a) A(x)/A(Fx).

The standard conditional-density formula for a C2 SRB measure gives, for points y,z on one local unstable plaque,

    rho(y)/rho(z)=lim_(N->infinity) product_(n=1..N)
                         J^u F(F^(-n)z)/J^u F(F^(-n)y).

This is the actual formula in Ledrappier-Young Part I, Section 6.1, printed page 533; the convergence and positive local density are justified there by Lemma 6.1.1 and Corollary 6.2. Its hypotheses permit a neutral exponent. Substituting the exact Jacobian telescopes the product to

    [A(y)/A(z)] [A(F^(-N)z)/A(F^(-N)y)].

Choose a recurrent regular base point y and a positive-measure compact Pesin block with A bounded below by a positive constant, uniform local unstable size and uniform C1 control of unstable tangents. Along a subsequence of backward returns of y to that block, z's backward iterates are exponentially close and belong to the same local unstable graph. Their tangent directions approach one another. Since alpha is C1, the last ratio tends to one along this subsequence. The density product has a full limit, so that limit is A(y)/A(z).

This proves rho=C A relative to Riemannian arclength, equivalently constant density relative to |alpha|. The identity extends along the conditional plaque wherever its continuous density is represented. Nonvanishing of alpha on the whole local unstable plaque also follows by taking a sufficiently late backward return and then using its exact pullback law. No global lower bound for A on the support is required.

## Holonomy and signs

Let Gamma_s be the local W flow. Its Lie invariance gives Gamma_s*alpha=alpha. If h(p)=Gamma_(s(p))p, differentiating h adds W(h(p)) ds, which alpha annihilates. Hence h*alpha=alpha.

For h(p)=Psi_(s(p))p, the extra derivative is -B(h(p)) ds and again vanishes under alpha. Thus h*alpha=exp(a s(p))alpha. For the forward carrier flow Phi_t=Psi_(-t), the factor is exp(-a s(p)). This sign must be retained when speaking simply of B-orbit holonomy.

Preservation of alpha-length does not by itself identify normalized conditional probabilities on different plaques: their normalization constants can differ. Nor does it produce a transverse invariant measure or absolute continuity in the stable direction.

## Dependencies and scope

The primary density source is retained in the literature agent as in the team records and its text. Section 6.1, Lemma 6.1.1, and the introductory remark referring to Corollary 6.2 were read directly. Standard recurrence and the local unstable Pesin graph are used only on a compact block. The identities for alpha in the Euler setting were confirmed in A199. No new attractor, regularity of the full support, or Euler contradiction is implied.
