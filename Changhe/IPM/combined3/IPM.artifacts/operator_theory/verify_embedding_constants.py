#!/usr/bin/env python3
"""Exact rational certificate for OPERATOR_BRIDGE_v01, (11) and its ratio.

No third-party packages or floating-point comparisons are needed.
The classical rational inequality pi > 157/50 is used as an analytic input.
"""
from fractions import Fraction as F
import json

sqrt10_up = F(31623, 10000)
pi_low = F(157, 50)
C_up = F(28, 25)
assert sqrt10_up**2 > 10
# C_W^2 = (10+sqrt(10))^2/(44*pi).
numerator_up = (10 + sqrt10_up)**2
denominator_low = 44 * pi_low
assert numerator_up < C_up**2 * denominator_low
beta = F(7, 4)
M = F(1, 2)
ratio_up = C_up * M / beta
assert ratio_up == F(8, 25)
print(json.dumps({
    "status": "EXACT_RATIONAL_CHECK_PASS",
    "analytic_input": "pi > 157/50",
    "sqrt10_upper": str(sqrt10_up),
    "gradient_embedding_upper": str(C_up),
    "rational_squared_margin": str(C_up**2 * denominator_low - numerator_up),
    "beta_L2_lower": str(beta),
    "high_radius_upper": str(M),
    "strict_contraction_ratio_upper": str(ratio_up),
    "stationary_existence": "NOT_CLAIMED: full-form estimate and self-map remain required"
}, indent=2))
