"""Pure-math references for whole-log-radius absolute-loss integration.

This synthetic residual is not an IPM solution or a candidate profile. No
NumPy, historical engine, or numerical campaign is imported here.
"""
import math
from decimal import Decimal, localcontext


def log1pexp(value):
    return value + math.log1p(math.exp(-value)) if value > 0 else math.log1p(math.exp(value))


def radial_amplitude(log_radius, dilation=1.0, amplitude=1.0):
    """A r^6/(1+r^2)^4 evaluated at r/dilation without overflow."""
    if dilation <= 0 or not math.isfinite(dilation):
        raise ValueError("Dilation must be positive and finite")
    value = float(log_radius) - math.log(dilation)
    return amplitude * math.exp(6 * value - 4 * log1pexp(2 * value))


def quotient_residual(log_radius, theta, dilation=1.0, amplitude=1.0):
    return radial_amplitude(log_radius, dilation, amplitude) * math.cos(2 * theta)


def whole_axis_loss(a_ref=1.0, amplitude=1.0):
    if a_ref <= 0 or not math.isfinite(a_ref):
        raise ValueError("Reference amplitude must be positive and finite")
    return amplitude * amplitude / (336 * a_ref * a_ref)


def sampled_supremum_reference(a_ref=1.0, amplitude=1.0, dilation=1.0):
    """Exact continuous synthetic maxima; not a bound for any IPM profile."""
    return {"absolute_quotient": abs(amplitude) * 27 / (256 * a_ref),
            "density_divided_by_radius": abs(amplitude) * 27 / (256 * a_ref),
            "radius": dilation * math.sqrt(3),
            "quotient_angles": [0.0, math.pi / 2],
            "density_divided_by_radius_angle": math.pi / 2}


def radial_integral_tails(log_lower, log_upper, dilation=1.0, precision=80):
    """80-digit analytic radial tails for squared unit-amplitude residual.

    Returns decimal strings. The angular integral is pi/4; to obtain a J_abs
    tail multiply these radial values by amplitude^2/(4*a_ref^2).
    """
    if not log_lower < log_upper:
        raise ValueError("Integration interval must be ordered")
    if dilation <= 0 or not math.isfinite(dilation):
        raise ValueError("Dilation must be positive and finite")
    with localcontext() as context:
        context.prec = precision
        shift = Decimal.from_float(float(dilation)).ln()
        lower = Decimal.from_float(float(log_lower)) - shift
        upper = Decimal.from_float(float(log_upper)) - shift
        q_lower = (2 * lower).exp()
        t = q_lower / (1 + q_lower)
        inner = t**6 / 12 - t**7 / 14
        u = 1 / (1 + (2 * upper).exp())
        outer = sum((Decimal((-1)**j * math.comb(5, j)) * u**(j + 2)
                     / (2 * (j + 2)) for j in range(6)), Decimal(0))
        total = Decimal(1) / 84
        return {"origin": str(inner), "infinity": str(outer),
                "finite_interval": str(total - inner - outer),
                "whole_axis": str(total), "precision_decimal_digits": precision}


def constant_defect_divergence(defect):
    """Necessary negative reference: a nonzero origin constant gives infinity."""
    return {"constant_defect": str(defect), "whole_axis_loss_is_infinite": defect != 0,
            "reason": "For a nonzero limiting residual, integral |Rf|^2 dr/r diverges at zero."}
