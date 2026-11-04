# Currents on a regular backward attractor

Date: 2026-11-02T22:06:14Z. A217 confirms the stated current identities. A218 leaves the extra assertion about flow-current homology OPEN.

## Exact hypotheses

Let U be a C2 rotating Euler profile, let 0<c<1/2, let omega be any finite real number, and set B=(cI-omega J)y+U, Omega=curl U, a=1-2c>0. Let Lambda be a compact basic hyperbolic attractor for the flow Psi of -B, contained in the region where B, Omega and B cross Omega are nonzero. Let nu be its flow-invariant SRB probability. Set alpha=(B cross Omega) dot dy. The exact profile identities are Psi_t^*alpha=e^(at)alpha and alpha=a U^flat+dHt. The one-dimensional unstable bundle admits the continuous orientation and normalization alpha(Z)=1. The A207 density formula says unstable conditionals have constant density in alpha-arclength, with constants depending on the plaque.

For a C1 one-form beta and a continuous two-form gamma define

    T(beta)=int beta(Z) dnu,
    T_B(beta)=int beta(B) dnu,
    R(gamma)=int gamma(B,Z) dnu.

All these integrals are finite, since the fields are bounded on the regular compact set.

## Confirmed identities and proof

The unstable bundle is invariant and one-dimensional. Applying alpha to DPsi_t Z shows DPsi_t Z=e^(at) Z composed with Psi_t. In particular Z is differentiable along B trajectories and [B,Z]=aZ in this directional sense.

Local disintegration in the intrinsic alpha-coordinate s has the form ds times a transverse measure; the normalizing plaque lengths are absorbed in that transverse measure. For a test function supported in one such chart, integration of its s derivative vanishes. A partition of unity then gives T(dg)=0 for every C1 g. This is a closed current. Full-flow invariance gives T_B(dg)=0 as well.

Cartan's formula gives

    d beta(B,Z)=B(beta(Z))-Z(beta(B))-a beta(Z).

The first term integrates to zero by carrier invariance; the directional derivative exists and is continuous by the exact transport of Z, although Z need not be ambient C1. The second integrates to zero by closedness of T, since beta(B) is C1. Thus

    boundary R = -a T.

This directly makes T null-homologous as a current in every open neighborhood of Lambda. It does not require an isotopy argument.

Integrating alpha=a U^flat+dHt against Z gives

    T(U^flat)=1/a.

Also T(y dot dy)=0, so for X=cy+U one has T(X^flat)=1/a. Since dU^flat=i_Omega vol and vol(B,Omega,Z)=1,

    R(dU^flat)=-1=-a T(U^flat).

These identities are consistent. None excludes the attractor.

## Unsupported flow-current homology inference

The final sentence of coordinator Section 18 says that both T and T_B are null-homologous because Psi_1 is isotopic to the identity and rescales T. This only applies to T. In fact (Psi_1)_*T=e^a T, whereas (Psi_1)_*T_B=T_B. The isotopy therefore supplies no equation killing the class of T_B. No independent proof of its vanishing in an arbitrary trapping neighborhood was supplied.

Here is a counterexample to that inference from the flow and rescaled unstable-current data alone. Let M=[[2,1],[1,1]], with unstable eigenvalue lambda>1, eigenvector v, and left eigen-covector ell normalized by ell(v)=1. On the compact mapping torus (x,1) identified with (Mx,0), put a=log lambda, B=-partial_t, Z=e^(-at)v and alpha=e^(at)ell dot dx. The seam identities Mv=lambda v and ell M=lambda ell show these tensors are smooth and well defined. The flow Psi of -B has DPsi_s Z=e^(as)Z composed with Psi_s and Psi_s^*alpha=e^(as)alpha. Haar probability is invariant, has constant alpha-length conditionals on unstable plaques, and makes T closed. The previous current calculation still gives boundary R=-aT.

However dt is a globally defined closed one-form and T_B(dt)=-1. Hence T_B is not null-homologous. This mapping-torus example is not an Euler profile in Euclidean space and does not have the specified negative divergence. It refutes the stated homological inference, not a possible stronger Euler theorem. For an actual Euler attractor the extra flow-current assertion remains OPEN; it may not be labeled PROVED from Section 18.

## Scope and verification

Read coordinator in the team records Section 18 in full. Independently checked signs, current boundaries, the directional regularity needed for Cartan's formula, and the mapping-torus seam. A207 supplies the conditional-density input. Extending this calculation to a nonuniform vortical SRB measure would additionally require integrability of Z and control of the integrations; that extension is not asserted here.
