# Long-run maximal-log column checks

Status: CONFIRMED finite numerical comparisons. This does not certify every log column or prove an infinite growth law.

## Exact reference

Topic44 gives the full rational top-log profile at delta=2/3 and leading sin(theta). Its stream coefficient b_k at order3k satisfies the exact scalar ratio there, with its separately verified initial b_2 and b_3. The three adjacent top-density profiles are finite rational functions of k times b_k. Evaluating them in exact rational arithmetic, including the low-order reflected frequencies, gives the exact l1 norm of the highest log column. This reference uses no floating-point recursion.

## Comparisons and conditions

The independent script evaluates the reference logarithms with512-bit Arb arithmetic, and compares them with retained snapshots of the team's reported per-column norms. The theory part's amplitude5 data are divided by5^n through subtraction in logarithms, using the exact amplitude homogeneity.

- Theory part double precision: orders7 through320,314 comparisons, maximum inferred relative discrepancy1.309e-13.
- Theory part long double prefix: orders7 through236,230 comparisons, maximum inferred relative discrepancy1.309e-13.
- Numerical experiments regenerated Arb prefix: orders7 through140,134 comparisons, maximum inferred relative discrepancy6.545e-14.
- Numerical experiments running Arb prefix: orders7 through162,159 comparisons, maximum inferred relative discrepancy6.545e-14.

The displayed discrepancies include conversion of log norms to binary64 and subtraction of amplitude logarithms; they are not interval enclosures for the data being checked. Every reported maximal degree also equals the sharp degree bound. In particular the double-precision highest column at order320 agrees with the exact cycle even though that column is very small.

## What this says about the interior maximum

The highest-column agreement does not certify the interior log columns. In the retained double data, max_k log10(k! c_k/c_0) is about-0.613 at order230, -0.235 at240 (index42),2.155 at270 (index48),4.182 at300 (index59), and4.462 at320 (index63). The long-double prefix ends before the largest of these values. Its maximal per-column log discrepancy from double is8.25e-12 at210,1.36e-10 at220, and1.85e-9 at230. These are finite comparisons, not proof of eventual agreement or divergence.

The high-precision numerical prefix reaches162 in the retained snapshot and does not yet test the large interior maximum. The question whether that maximum persists under independent high-precision evaluation remains OPEN here.

## Reproduction

Run ../../code/top_log_numerical_audit.py. Source snapshots and SHA256 hashes are retained under sources/ and verification/checks.json. Actual computation took0.2812779168598354 seconds. Dependencies are the exact finite cycle in topic44, the arithmetic homogeneity in topic01, and the retained source data. All statements above name the exact finite prefixes checked.
