# Conditional arithmetic audit of the order350 midpoint continuation

Status: CONFIRMED finite conditional arithmetic, V372. No claim about the discarded input uncertainty is made.

## Exact scope

The numerical experiments continued its canonical logarithmic recurrence at delta=2/3 after replacing every coefficient ball through order329 by its midpoint. This changes the computational initial state. Narrow balls subsequently produced by that recurrence enclose arithmetic values for that loaded state only. They do not enclose the original canonical coefficients unless the discarded input uncertainty is separately propagated. Topic160 and V364 explain this distinction.

This audit independently checks norms, polynomial evaluations and Poisson identities in the supplied order350 checkpoint. It retains exact selected coefficient arrays at orders348,349,350 and hashes the complete source. The unretained earlier arrays are used only for finite diagnostic sums; their derived ball summaries and the source fingerprint are retained. There is no new nonlinear recurrence check at these high orders and no new infinite convergence theorem.

## Methods

For each logarithmic order q, the angular Wiener norm is the sum of the absolute values of the sine coefficients. The plain norm sums these column norms. Factorial column norms multiply the qth column by q!. A strict maximizing-column certificate compares its full interval with every other column interval.

For n=348,349,350, let P=2-2n/3, let F[q,j] denote the coefficient of t^q sin((2j+1)theta), and G[q,j] the coefficient of t^q sin(2j theta), where t=log r. With missing entries set to zero, the independently checked Poisson identity is

    (4j^2-P^2)G[q,j] - 2P(q+1)G[q+1,j] - (q+1)(q+2)G[q+2,j]
      = ((P-2j)F[q,j-1]+(q+1)F[q+1,j-1]
          +(P+2j)F[q,j]+(q+1)F[q+1,j])/2.

At exact resonance the canonical constant G[0,j] is zero. The identity comes directly from applying the polar Laplacian to each t-polynomial and from differentiating the density in x.

The t-polynomials are evaluated by Horner's rule, independently of the source's power-accumulation loop. Absolute sums of the evaluated Fourier coefficients bound the angular norm. The cancellation statistic is the logarithm of the absolute column sum divided by that evaluated norm. At each t this is a finite arithmetic statistic of the loaded continuation, not a tail estimate.

Stream mass is partitioned by the exact rational distance min(|P+2j|,|P-2j|). Distances greater than4 are collected as far. Density-near shares follow the source's expressly stated diagnostic cutoff, rather than introducing a new theorem about concentration. All comparisons with printed numbers retain their rounding tolerance.

## Dependencies and interpretation

Only the stored arrays, exact rational indexing, elementary interval arithmetic and the algebraic Poisson identity enter the audit. The original recurrence's signs were independently proved and checked at low orders earlier in the campaign. These checks cannot promote the reset continuation to a certified approximation of the original infinite series. The latter problem remains open.

## Audit outcome, 2026-10-31T14:04:58+00:00

Orders324..350 include 1351611 coefficient positions. At348..350 all121800 Poisson coefficients and the canonical resonant constant pass. The first audit checks97 rounded mode-share entries; the replay checks6 norms,689 factorial-column comparisons,16 printed t-profile values and42 band values. Density/stream slopes over324..350 are -0.57938783705527378336 and -0.54996014549122461555. Original audit took 30.24565396970138 seconds; separate replay took 3.257252864073962 seconds. Source SHA256 c02ada1019962542fa9dbcf7429eacd57f5c1fadeaf44a4788a2a7a0676f4733. Selected archive hash ba29ad73976c2bab6a40a6683ce7bfdfa9a614f0aa65d2ea012358e49cc5dd5c.

The14:01 source correction explicitly agrees with this scope (V373). The two literal descriptions inV374 fail by the norm and band counterexamples retained in verification/narrative_counterexamples.json. Overall decay within a finite window does not imply pointwise monotonicity or infinite convergence.

## Finite period-three descriptions

An exact period-three pattern would repeat its normalized shares and its logarithmic three-order increments. Even when the intended claim is approximate, a stated numerical range must contain the computed intervals. Subtracting the independently retained log-norm balls at n and n+3 encloses the corresponding increment, without a new recurrence run. Comparing the share balls at341 and344 tests the statement that they repeat to three decimal digits. These checks concern the conditional reset continuation only. They cannot establish or disprove eventual asymptotic periodicity, and no finite nearly constant sequence of increments implies infinite convergence. The dated arithmetic results are retained in verification/period3_counterexamples.json.

## Counterexample replay, 2026-10-31T14:27:44+00:00

At orders 330 to 333, the stream log-norm increment is enclosed by [-1.0369736989040247078482442341556440 +/- 2.90e-35], outside the asserted range -1.8 to -1.6. The density increment at 336 to 339 is [-1.5845902525107328863941037222804199 +/- 3.52e-35], outside -1.63 +/- 0.02. The combined shift-2 and shift-3 shares at 341 and 344 are approximately 0.920568664488 and 0.927776966727; their difference is [0.0072083022393743491519482623936092098 +/- 3.27e-38]. They do not repeat to three decimal digits. An exact finite period-three assertion also fails. These are refutations of the stated finite descriptions, not of a possible limiting cycle. The conditional status of all these numbers is unchanged.
