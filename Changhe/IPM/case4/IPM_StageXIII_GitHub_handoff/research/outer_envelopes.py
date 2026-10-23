"""Constructive absolute-coefficient outer envelopes for the frozen spaces.

The inequalities are analytic. Their values below use ordinary binary64
arithmetic, so the returned numbers are conservative estimates rather than
outward-rounded rigorous numerical certificates. No candidate is modified.

Core input API: one dictionary per historical basis coefficient, containing
field keys f, fx, fy, psix, psiy, ratio. Each value is a list of monomials
(coefficient, x_power, y_power, (1+r^2)_power), as in the historical engine.
Use either its literal rounded lists or independently generated analytic
potential lists, and retain that distinction in the caller's provenance.
"""
import math

STIRLING = ((1,), (0, 1), (0, -1, 1), (0, 1, -3, 1), (0, -1, 7, -6, 1))
HERMITE_ABS = ((1,), (0, 1), (1, 0, 1), (0, 3, 0, 1), (3, 0, 6, 0, 1))
FIELDS = ("f", "fx", "fy", "psix", "psiy", "ratio")


def falling(value, order):
    return 0 if order > value else math.prod(range(value - order + 1, value + 1))


def sigma_value(mode, cl):
    sigma = mode.get("sigma", 0.)
    if isinstance(sigma, str):
        factor = {"zero": 0, "delta": 1, "2delta": 2, "3delta": 3}[sigma]
        return factor * (1 - 1/cl) / 2
    return float(sigma)


def _radial_bounds(mode, cl, radius):
    """Uniform |F_j|, j<=4, for R=1+r^2 >=1+radius^2."""
    m = int(mode["m"])
    k = max(5 - m, 0)
    u = 1 / (1 + radius * radius)
    tder = [falling(k, j) for j in range(5)]
    if mode["family"] == "global":
        if mode.get("alpha", 0) != 0 or mode.get("beta", 0) != 0:
            raise ValueError("Only the campaign's default Legendre modes have qualified envelopes")
        n = int(mode["n"])
        normal = math.sqrt(2*n + 1) if mode.get("normalize", True) else 1.
        # d_t^h P_n(2t-1) endpoint bound on t in [0,1].
        pder = [0. if h > n else normal * math.factorial(n + h)
                / (math.factorial(h) * math.factorial(n - h)) for h in range(5)]
        jets = [sum(math.comb(h, j) * tder[j] * pder[h-j] for j in range(h + 1))
                for h in range(5)]
        sder = [sum(abs(coef) * u**j * jets[j] for j, coef in enumerate(STIRLING[h]))
                for h in range(5)]
        sigma = sigma_value(mode, cl)
    elif mode["family"] == "local":
        width = float(mode["width"])
        zmin = (math.log1p(radius * radius) - float(mode["center"])) / width
        # For each monomial, maximize z^p exp(-z^2/2) on z>=zmin.
        # If zmin<0 its negative portion is covered by the full positive axis.
        monomial = []
        for p in range(5):
            z = max(0., zmin, math.sqrt(p))
            monomial.append((1. if p == 0 else z**p) * math.exp(-z*z/2))
        gaussian = [sum(c * monomial[p] for p, c in enumerate(HERMITE_ABS[h])) / width**h
                    for h in range(5)]
        st = [sum(abs(coef) * u**j * tder[j] for j, coef in enumerate(STIRLING[h]))
              for h in range(5)]
        sder = [sum(math.comb(h, j) * st[j] * gaussian[h-j] for j in range(h + 1))
                for h in range(5)]
        sigma = 0.
    else:
        raise ValueError("Unknown mode family")
    if sigma < 0:
        raise ValueError("Tail envelopes require nonnegative sigma")
    beta = (3 + 1/cl)/2 - m - sigma
    out = []
    for j in range(5):
        out.append(sder[0])
        if j < 4:
            sder = [abs(beta-j) * sder[h] + sder[h+1] for h in range(4-j)]
    return out, sigma


def assembled_field_bounds(F, degree):
    """Absolute bounds for the normalized algebra in absolute_fields._assemble."""
    H0, H1, H2, H3 = 1., falling(degree, 1), falling(degree, 2), falling(degree, 3)
    D0 = falling(degree, 1) * max(0, degree-1)
    D1 = falling(degree, 2) * max(0, degree-2)
    D2 = falling(degree, 3) * max(0, degree-3)
    Dy = falling(degree, 4) / 3
    d0 = 4*((degree+1)*F[1] + F[2])
    d1 = 4*((degree+2)*F[2] + F[3])
    d2 = 4*((degree+3)*F[3] + F[4])
    return {
        "f": D0*d0 + 2*H0*d1,
        "fx": D1*d0 + (2*D0 + 2*H1)*d1 + 4*H0*d2,
        "fy": Dy*d0 + 4*H1*d1 + 4*H0*d2,
        "psix": H3*F[0] + (6*H2 + 2*H1)*F[1] + (12*H1 + 4*H0)*F[2] + 8*H0*F[3],
        "psiy": H3*F[0] + (6*H2 + 2*H1)*F[1] + (12*H1 + 4*H0)*F[2] + 8*H0*F[3],
        "ratio": D2*F[0] + (4*D1 + 2*D0 + 2*H2)*F[1]
                 + (4*D0 + 8*H1 + 4*H0)*F[2] + 8*H0*F[3]}


def mode_field_constants(mode, cl, radius, beta=None, alpha=None):
    """Uniform constants for f<=C r^beta, grad f<=D r^(beta-1), etc."""
    if radius < 1 or cl <= 1:
        raise ValueError("Need radius>=1 and cl>1")
    gamma = 1/cl
    beta = gamma - 1 if beta is None else beta
    alpha = gamma if alpha is None else alpha
    F, sigma = _radial_bounds(mode, cl, radius)
    degree = 2 * int(mode["m"])
    raw = assembled_field_bounds(F, degree)
    A = (3+gamma)/2
    R_orders = {"f": 2., "fx": 2.5, "fy": 2.5, "psix": 1.5, "psiy": 1.5, "ratio": 2.}
    targets = {"f": beta, "fx": beta-1, "fy": beta-1,
               "psix": alpha, "psiy": alpha, "ratio": alpha-1}
    scale = abs(float(mode.get("scale", 1.)))
    answer = {}
    for field in FIELDS:
        power = A-sigma-R_orders[field]
        actual_degree = 2*power
        if actual_degree > targets[field] + 1e-12:
            raise ValueError("Requested envelope exponent is below a mode's growth exponent")
        ratio_factor = (1+1/radius**2)**max(0., power)
        answer[field] = scale * raw[field] * ratio_factor * radius**(actual_degree-targets[field])
    return answer


def outer_loss_envelope(cl, core_coefficients, core_term_lists, modes, extra_coefficients,
                        radius, a_ref):
    """Constructive uniform analytic field envelope, evaluated in binary64.

    Does not exploit leading linear or nonlinear coefficient cancellations.
    Caller must bind the exact core term representation in provenance.
    """
    if not (radius >= 1 and cl > 1 and a_ref > 0):
        raise ValueError("Need radius>=1, cl>1, a_ref>0")
    if len(core_coefficients) != len(core_term_lists) or len(modes) != len(extra_coefficients):
        raise ValueError("Coefficient and field-term counts differ")
    gamma = 1/cl
    # Tiny historical rounding shifts are retained in the bounding exponents.
    degrees = {field: [] for field in FIELDS}
    for coefficient, item in zip(core_coefficients, core_term_lists):
        if coefficient == 0:
            continue
        for field in FIELDS:
            degrees[field].extend(xpower+ypower+2*power for value,xpower,ypower,power in item[field] if value != 0)
    beta = max([gamma-1] + degrees["f"]
               + [d+1 for field in ("fx", "fy") for d in degrees[field]])
    alpha = max([gamma] + degrees["psix"] + degrees["psiy"]
                + [d+1 for d in degrees["ratio"]])
    if beta >= 0 or alpha >= 1:
        raise ValueError("These envelopes do not establish integrable sublinear tails")
    target = {"f": beta, "fx": beta-1, "fy": beta-1,
              "psix": alpha, "psiy": alpha, "ratio": alpha-1}
    bound = {field: 0. for field in FIELDS}
    for coefficient, item in zip(core_coefficients, core_term_lists):
        for field in FIELDS:
            bound[field] += abs(coefficient) * sum(abs(value) * radius**(xpower+ypower+2*power-target[field])
                                                   * (1+1/radius**2)**max(0., power)
                                                   for value,xpower,ypower,power in item[field])
    for coefficient, mode in zip(extra_coefficients, modes):
        if coefficient:
            one = mode_field_constants(mode, cl, radius, beta, alpha)
            for field in FIELDS:
                bound[field] += abs(coefficient) * one[field]
    C = bound["f"]
    D = math.hypot(bound["fx"], bound["fy"])
    V = math.hypot(bound["psix"], bound["psiy"])
    W = bound["ratio"]
    A = cl*D + abs(cl-1)*C
    B = V*D + W*C
    eta = alpha+beta-1
    terms = [A*A*radius**(2*beta)/(-2*beta),
             2*A*B*radius**(beta+eta)/(-beta-eta),
             B*B*radius**(2*eta)/(-2*eta)]
    return {"radius": radius, "reference_amplitude": a_ref,
            "field_constants": bound, "beta_f": beta, "alpha_U": alpha,
            "residual_exponents": [beta, eta], "residual_constants": [A, B],
            "outer_loss_estimate_from_uniform_analytic_envelope": sum(terms)/(2*a_ref*a_ref),
            "outer_integral_convergent_under_envelope": True,
            "analytic_uniform_inequality": True,
            "outward_rounded_numerical_certificate": False,
            "leading_cancellations_assumed": False,
            "method": "Coefficient-absolute old monomials; bounded Legendre derivatives; normalized harmonic derivatives; polynomial-Gaussian local envelopes."}
