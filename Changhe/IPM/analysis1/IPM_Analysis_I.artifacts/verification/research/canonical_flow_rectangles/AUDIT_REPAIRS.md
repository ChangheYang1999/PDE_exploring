# Implementation attempts before acceptance

The first run, 2026-10-21T22:55:19Z, rejected its own mpmath endpoint parser because the installed exact mantissa type is mpz. The second version uses operator.index, verifies finite bit count and sign, and converts exactly. The original code, birth and failure log are in attempts/001_iv_endpoint_integer_type.

The second run, 22:55:47Z, rejected the actual iv output because that independent method emits the ranges in s,v1x,v2y,T0 order, while the exact method emits s,v2y,v1x,T0. Version3 enforces each method's actual fixed order, retains function labels for every target lookup, and matches analytic errors by function name. No output arrays or inherited results were changed. The previous source, birth and log are in attempts/002_method_range_order. Both failed runs produced no accepted checks or targets.

The actual accepted topic125 methods are deliberately different. Their named intervals are compared with the corresponding named binary targets; an assumption of common array position cannot identify the functions. The current code retains exact name/order checks and exact count checks. These are implementation corrections after the already reviewed mathematical proof, and before the complete check and its actual review.
