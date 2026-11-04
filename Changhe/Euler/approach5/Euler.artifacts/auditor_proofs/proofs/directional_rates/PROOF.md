# Directional stretching and regular points of vortical invariant sets

## Hypotheses and statements

Let U in C2(R3;R3) solve the rotating Euler profile equation with div U=0,

    B=(cI-omega J)y+U, Omega=curl U, S=(DU+DU^T)/2,

where 0<c<1/2 and omega is any finite real number. Let mu be a compactly supported B-flow-ergodic invariant probability with B and Omega nonzero almost everywhere. Let n=Omega/|Omega|, m=B/|B|, and let u be any measurable unit choice on the one-dimensional forward Oseledets subspace of exponent 2c-1. Then

    integral n dot S n dmu=1,
    integral m dot S m dmu=-c,
    integral u dot S u dmu=c-1.                         (1)

No globally oriented choice of u is needed: its quadratic form is unchanged by sign. Compact support is an explicit hypothesis; the statement here does not cover invariant probabilities with uncontrolled derivative integrability at infinity.

Separately, let K be a compact B-invariant set on which Omega never vanishes. Then every point of K with B nonzero lies in Reg={B cross Omega !=0}. If p in K is a zero of B, the connected vortex line through p meets K only at p. Completeness of the entire vortex line is not required for this last local-to-global intersection assertion. It holds on its maximal interval of existence.

## Proof of the directional rates

The exact spectrum theorem A037 gives the three simple forward exponents

    1+c, 0, 2c-1,

with the first two subspaces spanned by Omega and B respectively. The cocycle and its inverse are uniformly bounded over unit times on the compact invariant support, so Oseledets integrability holds.

For any nonzero tangent vector v propagated by D Phi_t, normalize v(t)=D Phi_t(v)/|D Phi_t(v)|. Since DB=cI-omega J+DU,

    d/dt log|D Phi_t(v)|=c+v(t) dot S(Phi_t x)v(t).

On each invariant one-dimensional Oseledets subspace the quadratic expression agrees with that of any measurable unit section at Phi_t x. It is a bounded measurable function. Birkhoff's theorem and the definition of the Lyapunov exponent therefore imply that its integral equals the exponent minus c. This gives all three equalities in (1). These rates use the transported bracket field and the carrier strain, but do not by themselves use Omega=curl U: they also hold for an independent nonzero bracket eigenfield in the roles where A037 applies.

## Proof of the compact-set assertions

Suppose x in K satisfies Omega(x)=lambda_0 B(x) with B(x) nonzero. The Cauchy transport law gives, along the full B orbit,

    Omega(Phi_t x)=lambda_0 exp(-(1+c)t) B(Phi_t x).

The carrier is bounded on K, so Omega(Phi_t x) tends to zero as t tends to positive infinity. This contradicts the positive minimum of |Omega| on K. Thus all its nonstationary points lie in Reg.

Let gamma be the maximal vortex curve through a zero p of B, parametrized by gamma'=Omega(gamma), gamma(0)=p. The bracket identity [B,Omega]=-(1+c)Omega gives the exact relation

    B(gamma(tau))=(1+c)tau Omega(gamma(tau)).             (2)

For completeness, differentiating both sides along gamma, using D B Omega=D Omega B+(1+c)Omega, gives a linear homogeneous ODE for their difference with zero initial value. Uniqueness proves (2). Omega cannot vanish at a finite parameter on this nonconstant vortex curve by ODE uniqueness. Therefore at every tau nonzero, B is nonzero and parallel to Omega. Such a point cannot lie in K by the first assertion.

## Dependencies and scope

The proof uses A002 (Cauchy transport and the bracket identity), A037 (the exact compact ergodic spectrum), elementary ODE uniqueness and Birkhoff's theorem. It confirms THEORY_B Lemma 6.6 with compact support explicit, and Section 11.1. It supplies no singular-hyperbolic splitting, periodic-orbit density or physical measure in a set containing singularities.
