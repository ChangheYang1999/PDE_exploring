#!/usr/bin/env python3
"""Independent numerical tests against analytic whole-axis residual references.

Run only with the new absolute-loss workspace's resource supervisor. This
worker performs no candidate fitting and imports no Stage XII campaign worker.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True

if not os.environ.get("IPM_RESOURCE_SESSION"):
    raise RuntimeError("Manufactured numerical tests require the resource supervisor")

import numpy as np
from manufactured_reference import (whole_axis_loss, radial_integral_tails,
                                    constant_defect_divergence, sampled_supremum_reference)


def quadrature(log_lower, log_upper, dilation, radial_order, angular_order, a_ref, amplitude):
    """Composite log-radius Gauss integration independent of candidate evaluator."""
    rz, rw = np.polynomial.legendre.leggauss(radial_order)
    az, aw = np.polynomial.legendre.leggauss(angular_order)
    angles = (az + 1) * math.pi / 4
    angles_weights = aw * math.pi / 4
    angular = float(angles_weights @ np.cos(2 * angles)**2)
    breaks = np.linspace(log_lower, log_upper, int(math.ceil((log_upper - log_lower) / 2)) + 1)
    value = 0.0
    shift = math.log(dilation)
    for left, right in zip(breaks[:-1], breaks[1:]):
        s = (left + right) / 2 + (right - left) * rz / 2
        shifted = s - shift
        radial = np.exp(6 * shifted - 4 * np.logaddexp(0, 2 * shifted))
        value += float((rw * (right - left) / 2) @ (radial * radial))
    return amplitude**2 * angular * value / (math.pi * a_ref**2)


def run(args):
    root = Path(__file__).resolve().parent
    expected = whole_axis_loss(args.a_ref, args.amplitude)
    rows = []
    checks = []
    for dilation in [1., 2., 16., 256., 1024.]:
        for lower, upper in [(-8., 8.), (-12., 12.), (-16., 16.)]:
            previous = None
            for radial_order, angular_order in [(12, 16), (24, 32), (48, 64)]:
                value = quadrature(lower, upper, dilation, radial_order, angular_order,
                                   args.a_ref, args.amplitude)
                tails = radial_integral_tails(lower, upper, dilation)
                factor = args.amplitude**2 / (4 * args.a_ref**2)
                inner, outer = factor * float(tails["origin"]), factor * float(tails["infinity"])
                exact_window = factor * float(tails["finite_interval"])
                error = abs(value - exact_window)
                tolerance = 2e-13 * max(expected, np.finfo(float).tiny)
                rows.append({"dilation": dilation, "log_interval": [lower, upper],
                             "radial_order_per_interval": radial_order,
                             "angular_order": angular_order, "quadrature_value": value,
                             "analytic_finite_window_value": exact_window,
                             "absolute_quadrature_error": error,
                             "quadrature_change_from_previous": None if previous is None else abs(value - previous),
                             "exact_origin_tail": inner, "exact_infinity_tail": outer,
                             "tail_completed_value": value + inner + outer,
                             "whole_axis_reference": expected,
                             "finite_window_exactly_scale_invariant": False,
                             "tolerance": tolerance,
                             "passed": error <= tolerance})
                # Low-order quadrature is a convergence demonstration, not an acceptance gate.
                if radial_order == 48:
                    checks.append({"name": "finite_window_quadrature", "dilation": dilation,
                                   "interval": [lower, upper], "error": error,
                                   "tolerance": tolerance, "passed": error <= tolerance})
                previous = value
        shift = math.log(dilation)
        shifted_value = quadrature(-12 + shift, 12 + shift, dilation, 48, 64,
                                   args.a_ref, args.amplitude)
        base_value = quadrature(-12, 12, 1., 48, 64, args.a_ref, args.amplitude)
        err = abs(shifted_value - base_value)
        checks.append({"name": "co_moving_finite_window_covariance", "dilation": dilation,
                       "error": err, "tolerance": 2e-13 * expected,
                       "passed": err <= 2e-13 * expected,
                       "whole_axis_accuracy_claim_from_this_check_alone": False})
    fixed_rows = [row for row in rows if row["log_interval"] == [-8., 8.]
                  and row["radial_order_per_interval"] == 48]
    fixed_change = abs(fixed_rows[-1]["quadrature_value"] - fixed_rows[0]["quadrature_value"])
    checks.append({"name": "negative_fixed_window_invariance", "absolute_change_1_to_1024": fixed_change,
                   "passed": fixed_change > 1e-3 * expected,
                   "meaning": "Correctly detects significant lost tail from holding a finite window fixed."})
    negative = constant_defect_divergence(1e-30)
    checks.append({"name": "negative_nonzero_origin_constant", "passed": negative["whole_axis_loss_is_infinite"],
                   "constant_defect": negative["constant_defect"]})
    maxima = sampled_supremum_reference(args.a_ref, args.amplitude)
    output = {"schema": "absolute_loss_manufactured_tests_v1", "created_epoch": time.time(),
              "synthetic_residual": "A r^6/(1+r^2)^4 cos(2 theta); not an IPM profile",
              "reference_amplitude": args.a_ref, "amplitude": args.amplitude,
              "whole_axis_loss_reference": expected, "exact_synthetic_maxima": maxima,
              "quadratures": rows, "checks": checks, "negative_origin_reference": negative,
              "source_sha256": {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                                for name in ["manufactured_reference.py", "manufactured_tests.py"]},
              "passed": all(row["passed"] for row in checks)}
    target = root / "results" / "manufactured_tests.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError("Preserve prior manufactured result; choose a fresh workspace for changes")
    temporary = target.with_suffix(".json.partial")
    temporary.write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    temporary.replace(target)
    print(json.dumps({"output": str(target), "passed": output["passed"],
                      "checks": len(checks)}), flush=True)
    return 0 if output["passed"] else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--a-ref", type=float, default=23.95065822465609)
    parser.add_argument("--amplitude", type=float, default=1.)
    sys.exit(run(parser.parse_args()))
