# Candidate 007 publication transcription audit

Status: PROVED in V599, admitted 2026-10-31T22:01:31+00:00, within the exact scope below.

## Statement and scope

The ten rational coefficients in Section 8.5 of the frozen theory report equal the leading density obtained from Candidate 007's authoritative exact JSON. Its stored similarity exponent, the archived leading potential, density and stream coefficients, and the manifest hashes agree with that source. This is an input and transcription claim, not a claim that the stored candidate or its infinite recursion solves the stationary equation.

## Source and notation

Use the source JSON named in `../02_candidate007/data/leading_exact.json`, with its adjacent manifest and sector table. Put c equal to `cl_exact`, gamma=1/c, q=3+gamma and s=q-2. In the source's generator convention, the leading radial term is r^q C(theta), where C(theta)=sum_m C_m cos(2m theta). A branch-zero generator contributes its exact coefficient to C_m. Other branches have smaller exponents. Both source radial basis types tend to one after removing the leading radial power: t^h tends to one, and t^w P_h(2t-1) tends to P_h(1)=1. Thus C_m is the sum of all branch-zero coefficients at index m.

## Polar derivation

The polar Laplacian gives Delta(r^q C)=r^(q-2) sum_m D_m cos(2m theta), with D_m=(q^2-4m^2)C_m. For every nonnegative integer ell,

    d_y(r^s cos(ell theta))
      = r^(s-1)[(s-ell)sin((ell+1)theta)
                 -(s+ell)sin((ell-1)theta)]/2.

The convention sin(-theta)=-sin(theta) handles ell=0. Consequently rho=-d_y Delta chi has leading degree gamma and coefficients

    a_1 = -(q-2)D_0 + q D_1/2,
    a_(2k+1) = (2k-q+2)D_k/2 + (q+2k)D_(k+1)/2,  k>=1.

Absent D_m are zero. Independently differentiating the potential twice gives psi=d_x d_y chi. The x derivative is

    d_x(r^q cos(ell theta))
      = r^(q-1)[(q-ell)cos((ell+1)theta)
                 +(q+ell)cos((ell-1)theta)]/2.

Apply the displayed y formula at radial degree q-1 to each resulting cosine term. This derives every stream coefficient directly from the same potential without calling the Cartesian implementation or the angular Poisson inverse. As a check, the resulting b_j must satisfy

    2[4j^2-(gamma+1)^2] b_j
      = (gamma-2j+1)a_(2j-1) + (gamma+2j+1)a_(2j+1).

## Verification method and dependencies

The replay uses Python Fraction arithmetic, direct generator aggregation, and the displayed polar identities. It checks the source and sector-table hashes against the source manifest and the archived extraction, every stored potential/density/stream coefficient, and every numerator and denominator in the frozen publication table. The theorem excerpt is frozen before parsing. All displayed parameter equalities are exact rational equalities. The source generator convention and original independent Cartesian derivation are documented in topics 01 and 02. No numerical fit, limit or convergence inference is used.

## Completed verification

Direct rational polar differentiation agrees with all416 branch-zero generators, ten nonzero potential moments, ten density coefficients, ten stream coefficients, ten Poisson identities and all ten published exact numerator/denominator pairs in the frozen Section8.5. Source, manifest and sector-table hashes match. The exact parameter is c=4076476460239181/2251799813685248, delta=1824676646553933/4076476460239181. Arithmetic runtime 0.038188585080206394seconds.

The finite input and transcription identities are PROVED. This does not establish exact stationarity of the candidate, compatibility at its first resonance, or infinite convergence at its stored rational exponent.
