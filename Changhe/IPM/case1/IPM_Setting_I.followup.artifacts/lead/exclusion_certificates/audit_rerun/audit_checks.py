"""Independent exact/interval checks for the audit referee report.

No certificate-generating module of the obstruction certificate is imported. See the informal proofs
for the analytic justification of the quantities checked here.
"""

import os
import resource
import sys

sys.dont_write_bytecode = True
for variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[variable] = "1"
resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
resource.setrlimit(resource.RLIMIT_CPU, (500, 500))

import hashlib
import inspect
import json
from fractions import Fraction as F
from pathlib import Path

import mpmath
from mpmath import iv
from mpmath.libmp import libmpi

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent
COPY = WORKSPACE
LAYOUT = {"01-obstruction": "obstruction_certificate",
          "02-radius": "radius_budget",
          "03-trace-uncertainty": "trace_uncertainty"}


def located(relative):
    # Map the original folder names to the folder names of these artifacts.
    head, _, tail = relative.partition("/")
    return COPY / LAYOUT[head] / tail


iv.dps = 50
checks = []
results = {}


def checked(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def read_json(path):
    # Preserve literal decimal input coefficients and parameters exactly.
    return json.loads(path.read_text(), parse_float=str)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def I(value):
    rational = F(value)
    return iv.mpf(rational.numerator) / iv.mpf(rational.denominator)


def binary_rational(value):
    sign, mantissa, exponent, bitcount = value
    assert bitcount >= 0
    numerator = -mantissa if sign else mantissa
    if exponent >= 0:
        return F(numerator * 2**exponent)
    return F(numerator, 2 ** (-exponent))


def endpoints(value):
    return tuple(binary_rational(x) for x in value._mpi_)


def saved_endpoints(value):
    return F(value["lower"]), F(value["upper"])


def serialize_interval(value):
    lower, upper = endpoints(value)
    return {"lower": str(lower), "upper": str(upper)}


def inside_saved(name, value, saved):
    lower, upper = endpoints(value)
    saved_lower, saved_upper = saved_endpoints(saved)
    checked(name, saved_lower <= lower <= upper <= saved_upper)


def strict_bounds(name, saved, lower, upper):
    left, right = saved_endpoints(saved)
    checked(name, F(lower) < left <= right < F(upper))


def no_elapsed(value):
    if isinstance(value, dict):
        return {
            key: no_elapsed(item)
            for key, item in value.items()
            if key != "elapsed_seconds"
        }
    if isinstance(value, list):
        return [no_elapsed(item) for item in value]
    return value


manifest = read_json(HERE / "sources.json")
for entry in manifest:
    # The originals are not part of these artifacts; only byte-identical
    # copies (entries with a "copy" path) are checked against their digests.
    if entry["copy"] is None:
        continue
    if not entry["copy"].endswith("obstruction_certificate.json"):
        checked(
            "copy unchanged: " + entry["copy"],
            sha256(WORKSPACE / entry["copy"]) == entry["sha256"],
        )

for relative in (
    "01-obstruction/data/obstruction_certificate.json",
    "02-radius/verification/radius_certificate.json",
    "03-trace-uncertainty/verification/analytic_bound_certificate.json",
):
    checked(
        "replay mathematical JSON identical: " + relative,
        no_elapsed(read_json(located(relative)))
        == no_elapsed(read_json(HERE / "expected" / relative)),
    )

reference = read_json(located("01-obstruction/data/fitted_reference.json"))
obstruction = read_json(located("01-obstruction/data/obstruction_certificate.json"))
radius = read_json(located("02-radius/verification/radius_certificate.json"))
analytic = read_json(
    located("03-trace-uncertainty/verification/analytic_bound_certificate.json")
)
A0 = F(reference["A0_exact"])
q_fit = [F(q) for q in reference["q_power_coefficients_exact_decimal"]]
checked("A0 exact", A0 == F("10.150725"))
checked("H lower", F(obstruction["geometry"]["H_lower"]) >= A0)
checked("H upper", F(obstruction["geometry"]["H_upper"]) < 11)
checked("q upper negative", F(obstruction["geometry"]["q_upper"]) < 0)
strict_bounds(
    "obstruction interval", obstruction["values_base"]["B"],
    "0.2830400682", "0.2851567624",
)
strict_bounds("gstar interval", obstruction["gstar"], "0.40222790015", "0.40222790016")
for group, name, bound in (
    ("values_base", "BA", F("0.007")),
    ("values_base", "Be", F("7.1")),
    ("values_box", "BAA", F("0.007")),
    ("values_box", "BAe", F("1.85")),
):
    strict_bounds(group + ":" + name, obstruction[group][name], -bound, bound)

inventory = {key: F(value) for key, value in radius["inventory_exact"].items()}
checked("source second derivative exact", A0 + 8 * sum(q_fit) == inventory["w2star"])
checked("source second derivative decimal", inventory["w2star"] == F("0.7768297940321664"))
checked("astar lower formula", inventory["astar"] == 3 * A0 / 5)
checked("gmin formula", inventory["gmin"] == F(4, 5) * F(1, 4) / F(5, 4))
gstar_lower, _ = saved_endpoints(obstruction["gstar"])
checked("exp(T1) > 4/5", 2 * gstar_lower > F(4, 5))

outward = {
    "varying_parameters": {
        "M": 5616, "Me": 232055, "DN": 27993, "KAv": 30950,
        "Kev": 1163734, "Rvv": 564862, "C2": 581867,
    },
    "fixed_parameters": {
        "M": 5429, "Me": 226640, "DN": 27063, "KAv": 29729,
        "Kev": 1129860, "Rvv": 539662, "C2": 564930,
    },
}
for case, upper in outward.items():
    data = {key: F(value) for key, value in radius["cases"][case]["exact"].items()}
    for key, bound in upper.items():
        checked(case + " upper " + key, data[key] < bound)
    checked(case + " buffer conditions",
            data["Am"] > 2 and data["sigma"] > data["bp"]
            and data["theta"] + data["bm"] > 1
            and data["Gamma0"] > 0 and data["Gamma"] > 0)
    checked(case + " admissible trace radius", data["radius"] < data["delta0"])
    checked(case + " d lower", data["d"] > F("0.2005"))
    checked(case + " dual norm formula", data["DN"] == data["M"] / data["d"])
    checked(
        case + " quadratic formulas",
        data["KAv"] == data["rho"] * data["DN"] * (1 + 1 / data["Ar"])
        and data["Kev"] == data["rho"] * data["Me"] / data["d"]
        and data["Rvv"] == 4 * data["rho"]**2 * data["M"] / data["d"]**2,
    )
    parameter = (
        data["DA"] * data["h"] + data["De"] * data["hp"]
        + data["KAA"] * data["h"]**2 / 2
        + data["KAe"] * data["h"] * data["hp"]
    )
    checked(case + " parameter budget", parameter == data["par"])
    linear = upper["DN"] + upper["KAv"] * data["h"] + upper["Kev"] * data["hp"]
    budget = parameter + linear * data["radius"] + upper["Rvv"] * data["radius"]**2
    expected_budget = (
        F("0.1385033793555") if case == "varying_parameters"
        else F("0.13532849155")
    )
    checked(case + " rounded budget equality", budget == expected_budget)
    checked(case + " strict budget", budget < F("0.14"))
    checked(case + " B > 0.14", F("0.28") - budget > F("0.14"))
    checked(case + " converted radius", data["radius_phi"] == F(4, 415) * data["radius"])
    results[case + "_budget"] = str(budget)

jets = {}
for label, filename in (("K12", "ref_c6g_K12.json"), ("K18", "ref_c6g_K18.json")):
    data = read_json(located("03-trace-uncertainty/verification/" + filename))
    Ai = F(data["A"])
    checked(label + " alignment parameter", Ai == F("10.150725214760579"))
    jets[label] = [A0 / Ai * F(q) for q in data["q_monomial"][:3]]
jets["fitted"] = q_fit[:3]
for label, (q0, q1, q2) in jets.items():
    jets[label] = (q0, q1 - 2 * q0, q2 - 2 * q1 + q0)
for pair, bound in (("K12-K18", "0.50"), ("K12-fitted", "0.53"), ("K18-fitted", "0.032")):
    left, right = pair.split("-")
    separation = sum(abs(x - y) for x, y in zip(jets[left], jets[right]))
    checked(pair + " exact coefficient identity", separation == F(analytic["jet_lower_bounds"][pair]))
    checked(pair + " lower bound", separation > F(bound))
    results[pair + "_jet_sum"] = str(separation)

maxima = []
for degree in (3, 5, 7):
    aa, bb = F(degree - 11, 2), F(9 - degree, 2)
    r = F(1, 2)
    checked("conversion monotonicity " + str(degree), -72 * aa - 330 * bb * r**2 > 0)
    maximum = -72 * aa * r - 110 * bb * r**3
    checked("conversion maximum " + str(degree),
            maximum == F(analytic["conversion_maxima"][str(degree)]))
    maxima.append(maximum)
checked("conversion factor", 1 + max(maxima) == F(415, 4) == F(analytic["norm_conversion"]))

def continuation(d):
    d = I(d)
    t = (I("1.005") + 2 * d) / I("0.965")
    rho_d = t + iv.sqrt(t * t - 1)
    lam = 1 - iv.log(rho_d) / iv.log(I(4))
    cc = d**-3 + d**-5 + d**-7 + 36 * d**-9 + 2 * d**-2
    cc += 6 * iv.exp(I("0.1") * iv.log(I("0.5"))) * d**-3
    return cc, lam


def continuation_bound(cc, lam, delta):
    return cc * iv.exp((1 - lam) * iv.log(I(10)) + lam * iv.log(I(delta)))


for example in analytic["examples"]:
    d = F(example["d"])
    cc, lam = continuation(d)
    checked("lambda positive " + str(d), endpoints(lam)[0] > 0)
    inside_saved("independent C " + str(d), cc, example["C"])
    inside_saved("independent lambda " + str(d), lam, example["lambda"])
    bound = continuation_bound(cc, lam, "1e-7")
    inside_saved("independent continuation " + str(d), bound, example["N_bound_delta_1e-7"])
    if d == F("0.4"):
        checked("194408 is an upper bound", endpoints(bound)[1] < 194408)

cc, lam = continuation(F(1, 20))
threshold = I(10) * iv.exp(iv.log(I("4.5e-6") / (I(10) * cc)) / lam)
checked("exact threshold bracket",
        F("1.4492e-31") < endpoints(threshold)[0]
        <= endpoints(threshold)[1] < F("1.4493e-31"))
lower_cutoff_bound = continuation_bound(cc, lam, "1.4492e-31")
rounded_cutoff_bound = continuation_bound(cc, lam, "1.45e-31")
checked("downward cutoff sufficient", endpoints(lower_cutoff_bound)[1] < F("4.5e-6"))
checked("upward cutoff fails this estimate", endpoints(rounded_cutoff_bound)[0] > F("4.5e-6"))
results["threshold"] = serialize_interval(threshold)
results["bound_at_delta_1.4492e-31"] = serialize_interval(lower_cutoff_bound)
results["bound_at_delta_1.45e-31"] = serialize_interval(rounded_cutoff_bound)

scale, rz = F("1e-9"), F("1.5278125")
checked("necessity counterexample norm bound", 428 * scale < F("4.5e-6"))
checked("necessity counterexample holomorphy bound", scale * rz**3 * (1 + rz**2)**2 < 10)
checked("necessity counterexample observed error", F(9, 128) * scale > F("7e-11"))
sample_bound = F("3e-7") + 10 * F(1, 700)**2 / (4 * F(1, 2)**2)
checked("interpolation example", sample_bound == F(analytic["uniform_error_sample_example"]))

rounding_evidence = {
    "version": mpmath.__version__,
    "module": str(Path(libmpi.__file__).resolve().relative_to(
        Path(mpmath.__file__).resolve().parents[1])),
    "module_sha256": sha256(Path(libmpi.__file__)),
    "functions": {},
}
for function_name in ("mpi_add", "mpi_mul", "mpi_div", "mpi_exp", "mpi_log", "mpi_sqrt", "mpi_pow"):
    function_source = inspect.getsource(getattr(libmpi, function_name))
    rounding_evidence["functions"][function_name] = function_source
(HERE / "installed_rounding.json").write_text(json.dumps(rounding_evidence, indent=2) + "\n")
report = {
    "status": "PASS",
    "mpmath_version": mpmath.__version__,
    "interval_decimal_precision": iv.dps,
    "checks_passed": len(checks),
    "checks": checks,
    "exact_and_interval_results": results,
    "scope": "Arithmetic checks supplement, and do not replace, the informal analytic proofs.",
}
(HERE / "audit_checks.json").write_text(json.dumps(report, indent=2) + "\n")
print("PASS:", len(checks), "independent arithmetic, provenance, and replay checks.")
print("The upward-rounded 1.45e-31 cutoff fails the displayed sufficient estimate.")
print("The downward-rounded 1.4492e-31 cutoff passes that estimate.")
