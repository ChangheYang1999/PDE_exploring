# Finite coefficients of the formal parameter curve

Status: finite interval computation CONFIRMED in V313, with independent retained-data replay. This topic makes no claim that the parameter curve is convergent or divergent.

## Exact objects

Use either of the two tuned profiles at delta0=2/3 from119. Let t=delta-delta0 and write the formal shape as

    b(t)=b0+beta1*t+beta2*t^2+... .

The proved formal construction157 fixes one new coefficient at each successive stream resonance. The coefficient beta_j controls the constant free harmonic at order n=3(j+1). With O_b and sigma_k as in157, its nonzero slope is

    C_(j+1)=O_b product_(ell=2)^j sigma_ell / product_(r=2)^(j+1)(6r).

This topic evaluates a finite initial list of beta_j using that formula and independently verifies selected slopes by two separate recurrences. It also recomputes every constant coefficient after each new choice and compares it with the independently tuned pure spatial series.

## Finite Taylor arithmetic and verification

At level j, input the polynomial b0+...+beta_(j-1)*t^(j-1) and set beta_j=0. Carry all j+1 available Taylor coefficients through each nonresonant Cartesian derivative, product and inverse. At each positive stream resonance, the denominator has a simple zero. Check that the numerator's constant enclosure contains zero, use the already established compatibility to remove it, and divide the remaining series by a nonzero power series. Exactly one available Taylor coefficient is lost.

After the jth resonance there is a constant harmonic H0. Set beta_j=(Hstar-H0)/C_(j+1). The affine response argument157 proves this formula when its lower-jet hypotheses hold. Recompute the finite recurrence with this value, and verify that all density and stream constants through order3(j+1) enclose the corresponding independently tuned coefficients. At selected levels, also evaluate the input with beta_j=1 and check H1-H0 against C_(j+1).

All scalar arithmetic is outward-rounded interval arithmetic. The leading algebraic root is enclosed by exact rational bisection of the certified obstruction polynomial. Retain every coefficient as an exact dyadic midpoint/radius pair, so restarting does not lose interval information.

## Interpretation

Finite values of |beta_j/beta_(j-1)|, |beta_j/beta_(j-1)|/j, and (|beta_j|/j!)^(1/j) can suggest a growth regime. They do not prove convergence, Gevrey regularity, divergence or an asymptotic law. The computation cannot replace the all-order formal argument157 or a bound on the full parameter sequence.

Dependencies:119 for the tuned spatial series and exact root;157 for the formal triangular response formula;01 for Cartesian conventions. The original second-jet calculation is retained unchanged in157 as a separate implementation check.

## Completed finite computation

At2048-bit interval precision, both roots were carried through beta12, requiring spatial orders through39. Each root passed15,264 constant density and stream comparisons over the twelve levels and six separate affine-slope checks. All24 exact dyadic coefficient intervals were replayed at4096 bits, with the first two coefficients at each root overlapping the separate calculation157. Actual production elapsed time was2091.35435857391 seconds.

The twelfth coefficients are approximately-5.869462904712018186989132014006711e51 and3.498528942003686503714734034174581e49 at the smaller and larger roots. The last adjacent absolute ratios are123672.20765785333917 and69958.93544243747362. Exact retained interval relative radii are below3.025e-436 and5.723e-462, respectively. These are finite Taylor coefficients, not estimates with a proved asymptotic error. The values, all earlier coefficients, slopes, counts and exact dyadic encodings are in verification; no parameter convergence or divergence is inferred.
