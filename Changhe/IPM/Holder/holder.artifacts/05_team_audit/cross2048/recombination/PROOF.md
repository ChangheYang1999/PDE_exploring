# Recombination with the finer cross-disk enclosure

## Statement and dependencies

For each alpha in {1/5,3/10,1/2,3/4,9/10,99/100}, let D_alpha denote the norm of R_1^2 for the homogeneous Euclidean C^alpha seminorm on compact smooth real scalar functions on R^2. The same constant applies to complex scalar inputs, by the accepted real-direction argument in 01_setup/PROOF.md. The kernel convention, the positive local projection measure and its mass 1/2 are fixed in the existing proofs.

Write A_alpha=Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)) and

    S_alpha=2^(1-alpha) A_alpha/alpha+1/2.

Let U_j be the nonnegative upper bound for the regular increment functional at phase j*pi/32 obtained below. With delta=pi/32, put

    H_delta(u,v)=u                              if v<=u cos(delta),
                  v                            if u<=v cos(delta),
                  sqrt(u^2+v^2-2uv cos(delta))/sin(delta) otherwise.

Then

    D_alpha <= S_alpha + max_(0<=j<16) H_delta(U_j,U_(j+1)).

This follows from the accepted unequal-phase interpolation theorem V177. The identity and positive local contribution S_alpha is added after interpolation. Its atom and positive measure have not been included in the cross-disk integrals or in the phase interpolation.

## Construction of the phase bounds

The adjacent proof ../PROOF.md supplies the rigorous rectangle enclosure of the smooth cross-disk contribution. In all six cases X_j is the smaller of the old accepted printed upper endpoint and the newly audited printed upper endpoint. Printed balls c +/- r are interpreted as the exact rational upper endpoint c+r, never as their midpoint or an unverified producer decimal.

For alpha=1/5 and99/100, use the already accepted V179 phase construction. If M_j is its accepted middle upper endpoint, g_j its accepted balanced-residual saving, and E_j the smaller accepted exterior endpoint, set

    U_j=M_j-g_j+X_j+E_j.

Equivalently this is the exact stored V179 phase upper bound minus its old cross upper endpoint plus X_j. The independent recombination checks both constructions and their equality. All input claims are unchanged except the smaller certified cross term.

For the other four exponents, let W_j and E_j be the printed upper endpoints of the accepted middle-circle and exterior-circle enclosures, and g_j the accepted V168 balanced-residual gain. Set

    U_j=W_j+X_j+E_j-g_j.

The old-cross version is checked against every accepted V168 phase upper bound. The new version is also checked from above by the accepted V168 bound with its old cross endpoint replaced by X_j. In particular it does not spend a middle-residual saving twice.

The frozen lead recombinations are comparison targets only. All 102 phase endpoints are recomputed as exact rationals from accepted inputs and newly audited cross enclosures. All input hashes are checked. The gamma, trigonometric and square-root evaluations are enclosed at384 bits. An independent768-bit calculation uses the algebraically equivalent amplitude

    sqrt(u^2+((v-u cos(delta))/sin(delta))^2)

in the interior case. The endpoint cases use certified lower bounds on cos(delta). The final decimal is the rational ceiling at ten decimal places. This proves that the recorded decimal is an upper bound. No pending strict-projection saving is used.

## Scope of the computational evidence

The cross source is identical to the previously audited V052 interval code, with a finer subdivision. The producer's complete interval sum and unchanged source hashes, the complete independent Cartesian diagnostics, and the rectangle enclosure proof jointly support the cross input. No full independent2048-cell interval rerun is claimed. The scalar recombination is independently repeated at two precisions. The accepted.json file binds the exact sources, output, standalone proofs, arithmetic code and independent checks.
