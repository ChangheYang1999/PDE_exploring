# Scope of the final conditional-continuation regressions

Status: finite counterexample confirmed 2026-10-31T23:04:43+00:00; the universal ranking claim is refuted.

## Exact claim and hypotheses

The numerical experiments' final regression file uses the printed class-zero multipliers at orders420,423,426,429,432,435,438:

    -0.02541, -0.02551, -0.02562, -0.02572, -0.02582, -0.02593, -0.02603.

Treat these seven printed decimal numbers as exact rationals for this finite diagnostic. Put y_n=log10|a_n|. Compare ordinary least-squares fits y_n=b+cx_n for x_n=log10 n, x_n=1/n, and x_n=n. The first is the power model and the last is the exponential model for the multiplier. This topic checks the claim that the exponential model has the smallest residual on every reported window, specifically the final window420..438. It does not assert any asymptotic law, and it does not identify a regression on printed data with a regression on the complete coefficient vectors.

## Complete finite argument

For m data points let S_x=sum x_n, S_y=sum y_n, S_xx=sum x_n^2, S_xy=sum x_n y_n and S_yy=sum y_n^2. Each list of abscissas here is nonconstant. Therefore D=S_xx-S_x^2/m is strictly positive. Differentiating the quadratic sum of residual squares with respect to b,c gives the unique minimizing slope c=(S_xy-S_x S_y/m)/D and intercept b=(S_y-c S_x)/m. Substitution gives the minimum mean-square residual

    RMS^2=(S_yy-S_y^2/m-(S_xy-S_x S_y/m)^2/D)/m.

Directed arithmetic applied to the exact rational inputs and real logarithms encloses these quantities. A strict upper endpoint for the power RMS below a strict lower endpoint for the exponential RMS disproves the universal comparison. A narrow difference cannot establish which asymptotic model is true. Changing from printed multipliers to the full coefficient-vector multipliers changes the input data and must be identified separately.

The signed change from -0.197 to -0.151 is +0.046. Across28 periods its mean is +0.046/28=23/14000, whereas the magnitude decreases by the negative of this amount. Any negative per-period description must explicitly refer to the magnitude. The actual unrounded order354 and438 increments can have a different mean and are checked separately if claimed.

A range of maxima over orders431..440 is not a range of values at the single order440. At each order the independently checked norm record gives one factorial maximum and its maximizing column; the final ten-order table gives a range over ten separate orders.

## Dependencies and scope

The calculation uses only the frozen printed multiplier table, exact finite least squares, and directed elementary functions. Topic266 independently checks the full coefficient vectors, norm table and conditional reset provenance. Topic215 gives the exact shifted-vector identity. No finite comparison here certifies the canonical sequence after its order329 midpoint reset or chooses an infinite growth law.

## Completed check, V621

On the seven printed multipliers at420..438, the power RMS is [4.2738994993947390780018689797155519302601192293956e-5 +/- 3.46e-55], while the exponential RMS is [4.3527186333050795109355340758467671146647260464923e-5 +/- 3.86e-55]; power is strictly smaller. The signed class-zero increment rises from [-0.196986315397523894674478686043 +/- 2.39e-31] at354 to [-0.150779079423795249278539468002 +/- 2.92e-31] at438; mean increase per period is [0.00165025842763316590699782921575 +/- 1.89e-33]. At440 the single density factorial-hump maximum is [4.79626058549002614719772973607127065688655 +/- 1.12e-42] at column102; the range4.4..5.1 and columns96..102 describes the last ten orders.

REFUTED for the universal exponential-fit ranking on the stated printed data. CONFIRMED for the explicit finite correction; OPEN for infinite growth and canonical uncertainty after the reset.

## Complete final-window replay protocol

For each reported lower endpoint357,370,381,390,400,410,420, select the class-zero density multipliers with n divisible by3 and n<=438. Recompute the three least-squares fits above on both the exact printed decimal inputs and the independently audited unrounded interval inputs from topic266. These are two explicitly different data sets. Each printed coefficient must lie in the rounding interval of the corresponding unrounded coefficient. Each printed regression statistic is checked against its stated last-place rounding interval for the printed-data fit. Repeating at two precisions and comparing the explicit residual sum with the normal-equation identity checks the finite arithmetic. Strictly separated residual balls certify their finite ranking only. Any change in ranking between the two data sets shows that the printed-data comparison cannot select an asymptotic model.

The tables are finite projections of the same conditional-on329 continuation. They contain no additional nonlinear or infinite-tail verification. Extending the independent fit checks to all seven windows does not enlarge the scope of the recurrence audit.

Protocol appended 2026-10-31T23:09:43+00:00.

## Complete replay, V626

Completed 2026-10-31T23:10:08+00:00. All31 printed class-zero multipliers on348..438 fall within their rounding bins for the independently audited unrounded values. All49 printed regression statistics on the seven windows reproduce within their stated rounding bins. There are42 distinct regressions, replayed at768 and1536 bits. The printed-data ranking is exponential, power, inverse-order on the first six windows and power, exponential, inverse-order on420..438. For unrounded data, the ranking is exponential, power, inverse-order on all seven windows. On420..438 the unrounded exponential RMS is [1.10210973362751017459152413685368682908353288e-5 +/- 1.52e-50] and the power RMS is [3.21562770416817745367729361546186455269798319e-5 +/- 2.69e-50]. Thus rounding changes the last-window ranking; the earlier counterexample applies precisely to the stated printed-data table.

CONFIRMED as finite regressions of the specified conditional-on329 continuation. This is a matched class-zero comparison, distinct from fitting every order in V622. No infinite tail model is selected.
