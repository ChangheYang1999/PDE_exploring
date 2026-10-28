# Certified values for the strict projection remainder

## Statement

Let C_alpha and D_alpha have the homogeneous Euclidean Holder seminorm and circular principal-value conventions in ../../../../01_setup/PROOF.md. Let alpha belong to {3/10, 1/2, 3/4, 9/10}. Write U_alpha for the D upper bound from the accepted phase interpolation certificate in ../../../phase_interpolation/verification/accepted.json. Then the theorem in ../PROOF.md gives

    D_alpha <= U_alpha - eta_alpha,
    eta_alpha = (82/321489) alpha(1-alpha) (11/9)^(alpha-2).

The statement is conditional on acceptance of that analytic theorem. Every source bound here uses radius R=h/2 and puts the whole positive projection remainder of mass 1/2 outside the phase interpolation. Its only change is the strict saving eta_alpha. No existing transport plan is changed.

## Decimal certification

Evaluate eta_alpha as a real ball at 384 bits. Subtract its lower rational endpoint from the already accepted rational upper endpoint U_alpha. Round the result upward to ten decimal places. Recompute the saving at 768 bits in the unsimplified form

    (82/49) alpha(1-alpha) (1/9)^4 (1+2/9)^(alpha-2).

The fresh lower endpoint must be at least the saved 384-bit lower endpoint. Thus the saved decimal is an upper bound for U_alpha-eta_alpha. The procedure checks every source hash, the analytic proof hash and the separate cross-read before writing a CONFIRMED record. This proof is written before the computation. If no such record exists, no numerical endpoint has been accepted.

## Scope

These four bounds apply to real and complex inputs. The saving is uniform in the kernel phase. It vanishes to first order as alpha tends to either endpoint and does not change the previously accepted leading endpoint asymptotics or the constant term at alpha=0. No claim is made here for a local radius other than h/2.
