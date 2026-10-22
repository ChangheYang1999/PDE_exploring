# Draft implementation status

2026-10-22T00:58:52.821178+00:00. Two draft engines have been written after the proof. They have passed Python AST parsing only and have not been imported or evaluated. The sole heavy179 computation is running, so181 numerical probes are deferred until it terminates. No preparation acceptance, source freeze or numerical181 verdict exists.

engine_arb.py uses physical Green ODEs, falling-factorial analytic derivative tails and full signed Fourier Arb convolution. engine_iv.py uses density-moment ODEs with a closed finite recurrence, analytic differentiation before Taylor expansion and integer center-radius convolution. The latter compares all62688 input derivative coefficients across the two methods if primary inputs are supplied, in addition to17226 residual polynomial coefficients. Those are code obligations, not executed counts.

Next: complete actual code review and own audit, resolve any issues before freezing, then serialize probes after179terminal. Probe small cell[-1/100,0], interior[-2,-19/10] and broad[-5,-24/5]. All44 cells and independent aggregate audit/maximizer replay are required for any final inner bound. Full input/tail/canonical pins must be bound via explicit current source maps. Do not reuse accepted oldW as derivative evidence. Retain this draft history.
