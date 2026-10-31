# What normalized coefficient flags can establish

## Scope, notation, and hypotheses

This note concerns finite coefficient diagnostics, not existence or nonexistence of an Euler profile. Let a nonzero block have real coefficient matrix A in R^(n x m), with n >= 2 and m >= 1. Let H be a nonempty proper subset of its radial rows. Define E = sum_(k,j) A_(k,j)^2, E_H = sum_(k in H,j) A_(k,j)^2, f = E_H/E, and q = max_(k in {n-2,n-1},j) |A_(k,j)| / max_(k,j) |A_(k,j)|. The implementation's four-row N6 statistic takes H = {3}; its top-two statistic uses rows 2 and 3. All assertions below use exact real arithmetic.

## Proposition 1: unchanged normalized shape does not bound high-mode size

For every real t != 0, q(t A) = q(A), f(t A) = f(A), and E_H(t A) = t^2 E_H(A). Consequently, bounds on the first two quantities alone give no finite upper bound on the high-mode energy or on its growth relative to the reference whenever E_H(A) > 0.

Proof. Both maxima in q are multiplied by |t|. Both squared sums in f are multiplied by t^2. The last identity follows directly from the definition of E_H. Let |t| tend to infinity to obtain the final assertion.

For an explicit four-row, one-column reference take A = (5,1,3,2)^T. Then E = 39, E_H = 4, q = 3/5, and f = 4/39. At t A top-two flag is still raised, q is exactly its reference value, and f is exactly its reference value. All three proposed shape-clearance predicates (reference flag present, q_end <= 1.5 q_start, and f_end <= 2 f_start) therefore hold for every t > 0, while E_H grows by t^2.

This is a counterexample to a universal inference from the normalized predicates alone. It is not an assertion that any of the campaign endpoints follows this artificial family. The actual block energies and physical fields remain to be checked. A leading-tail normalization by itself does not supply an amplitude bound for an independent subleading block; any such bound would need a separate relation for the represented field.

## Proposition 2: restoring a prescribed high-mode fraction

Suppose 0 < E_H < E and 0 < f0 < 1. Multiply exactly the rows in H by

    s = sqrt(f0 (E - E_H) / ((1 - f0) E_H)).

Leave all other rows unchanged. Then the new high-mode fraction equals f0. Any subsequent common nonzero scalar multiplication of the entire block leaves that fraction unchanged.

Proof. The new high-mode energy is s^2 E_H and its complementary energy is E - E_H. Substitution gives

    s^2 E_H / (E - E_H + s^2 E_H) = f0.

The final assertion is Proposition 1 applied to the modified block. The displayed s is the unique positive scaling with this property, since solving f0 = s^2 E_H/(E-E_H+s^2 E_H) yields that value of s^2.

The hypotheses exclude a zero high-mode energy, a block supported only on H, and target fractions 0 and 1. Such cases require explicit handling rather than division by zero. Restoring a rounded decimal f0 restores that decimal, not an unrounded reference fraction. A gauge operation that changes the block other than by a common scalar must be checked again after projection.

## Proposition 3: the half-improvement threshold

For real residual summaries r0 (start) and r1 (end), the inequality

    r_truncated <= r0 - (r0 - r1)/2

is exactly r_truncated <= (r0 + r1)/2. When r1 < r0, this says that at least half of that scalar improvement survives the intervention. It supplies no statement about another norm, domain, or residual ratio, and no bound on the change of its numerator if its denominator changes.

Proof. Expand the right hand side. The scope limitation follows because the inequality has only these three scalars as hypotheses. For a ratio R/D, positive D can grow while R also grows; for example 2/4 < 1/1 despite the larger numerator.

## Application to the proposed 2026-10-29T20:22:14Z rules

Stable q and f establish stable normalized coefficient shape. They do not alone establish that a physical residual improvement is independent of the flagged modes. An intervention on those modes, together with common-domain absolute and relative residuals, would address that attribution more directly. The proposed block-C intervention has the correct algebra under Proposition 2's hypotheses. Its actual reference fraction should be taken from the bound start record, and its effect on both weighted and absolute diagnostics should be reported. A passing scalar half-improvement test remains an empirical test on the chosen state and grids.

## Dependencies and status

Only finite sums, maxima, and real algebra are used. The arguments precede numerical checks. No formal source or Lean build is required or supplied. No Euler field, pressure, or optimizer result is inferred from these propositions.
