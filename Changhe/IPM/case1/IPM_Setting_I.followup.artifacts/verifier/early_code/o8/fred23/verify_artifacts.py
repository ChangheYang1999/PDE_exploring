"""Read-only audit of exact certificate endpoints, displayed bounds and inputs."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import resource
resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
import ast
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(rel):
    return json.loads((ROOT/rel).read_text())


def endpoints(row):
    lo, hi = F(row["lower"]), F(row["upper"])
    assert lo <= hi
    return lo, hi


def inside(row, lo, hi):
    aa, bb = endpoints(row)
    assert F(lo) < aa <= bb < F(hi), (aa, bb, lo, hi)


def magnitude(row, bound):
    assert max(map(abs, endpoints(row))) < F(bound)


def main():
    for item in load("INPUTS.json"):
        for p in (Path(item["source"]), ROOT.parent/item["copy"]):
            assert hashlib.sha256(p.read_bytes()).hexdigest() == item["sha256"], p

    cert = load("01-obstruction/data/obstruction_certificate.json")
    inside(cert["values_base"]["B"], ".2830400682", ".2851567624")
    inside(cert["gstar"], ".40222790015", ".40222790016")
    for group, key, bound in (("values_base","BA",".007"),
                              ("values_base","Be","7.1"),
                              ("values_box","BAA",".007"),
                              ("values_box","BAe","1.85")):
        magnitude(cert[group][key], bound)
    A0, e0 = F("10.150725"), 1/F("8.6000638")**2
    assert F(cert["geometry"]["H_lower"]) >= A0
    assert F(cert["geometry"]["H_upper"]) < 11
    assert F(cert["geometry"]["q_upper"]) < 0

    rc = load("02-radius/verification/radius_certificate.json")
    inventory = {k:F(v) for k,v in rc["inventory_exact"].items()}
    displayed = dict(Z="1.84", n="1.89", D="2.43", J="47.11", Eo=".246",
                     Ha="13.24", K0="3.18", Hk="9.78", w2S="31.53",
                     w2H="123.51", g2S="39.0625", g2H="248.4375",
                     g3S="244.140625", g3H="2329.1015625")
    for key, value in displayed.items():
        assert inventory[key] <= F(value)
    assert inventory["astar"] == F("6.090435")
    assert inventory["w2star"] == F(".7768297940321664")
    assert inventory["W0"] == F(25,9)
    assert inventory["gs"] == F(2,5)
    assert inventory["gmin"] == F(4,25)
    for name, row in rc["cases"].items():
        e = {k:F(v) for k,v in row["exact"].items()}
        varying = name == "varying_parameters"
        uppers = dict(M=5616, Me=232055, DN=27993, KAv=30950, Kev=1163734,
                      Rvv=564862, C2=581867) if varying else dict(
                      M=5429, Me=226640, DN=27063, KAv=29729, Kev=1129860,
                      Rvv=539662, C2=564930)
        for k,v in uppers.items():
            assert e[k] <= v, (name,k)
        assert e["d"] > F(".2005")
        assert e["delta0"] > F(".0997" if varying else ".1002")
        assert e["sigma"] > e["bp"] and e["theta"]+e["bm"] > 1
        assert 0 < e["radius"] < e["delta0"]
        assert e["par"]+e["linear"]*e["radius"]+e["Rvv"]*e["radius"]**2 < F(".14")
        assert e["radius_phi"] == F(4,415)*e["radius"]
        assert e["radius"] == F(".0000045" if varying else ".000005")
        assert e["par"] == F(".0025959" if varying else "0")
    assert F(".0025959")+F("30199.1202")*F(".0000045")+564862*F(".0000045")**2 == F(".1385033793555")
    assert 27063*F(".000005")+539662*F(".000005")**2 == F(".13532849155")

    # Independently recompute the exact three jets from the copied input data.
    fit = load("01-obstruction/data/fitted_reference.json")
    qs = {"fitted":list(map(F,fit["q_power_coefficients_exact_decimal"]))}
    for k in (12,18):
        item = json.loads((ROOT/f"03-trace-uncertainty/verification/ref_c6g_K{k}.json").read_text(),parse_float=str)
        qs[f"K{k}"] = [A0/F(item["A"])*F(x) for x in item["q_monomial"]]
    def jets(q):
        return {3:q[0],5:q[1]-2*q[0],7:q[2]-2*q[1]+q[0]}
    numerical = load("03-trace-uncertainty/verification/numerical_comparison.json")
    for name, row in numerical["pairs"].items():
        a,b = name.split("-")
        ja,jb = jets(qs[a]),jets(qs[b])
        exact = {str(k):ja[k]-jb[k] for k in ja}
        assert exact == {k:F(v) for k,v in row["jet_differences_exact"].items()}
        lower = sum(map(abs,exact.values()))
        assert lower == F(row["jet_sum_exact"])
        assert lower > F(".50" if name=="K12-K18" else ".53" if name=="K12-fitted" else ".032")

    analytic = load("03-trace-uncertainty/verification/analytic_bound_certificate.json")
    for row, upper in zip(analytic["examples"], ("2.177e9","3.520e7","1.472e6","387554","194408")):
        assert endpoints(row["N_bound_delta_1e-7"])[1] < F(upper)
        inside(row["lambda"], 0, 1)
    inside(analytic["examples"][0]["delta_threshold"], "1.4492e-31", "1.4493e-31")
    assert F(analytic["uniform_error_sample_example"]) == F(10147,490000000)
    assert F(10147,490000000) < F("2.071e-5")

    for rel in ("INDEX.md","VERIFICATION.md","01-obstruction/PROOF.md",
                "02-radius/PROOF.md","03-trace-uncertainty/PROOF.md",
                "04-exclusion/PROOF.md","collaboration/STATUS.md"):
        assert (ROOT/rel).is_file()
    # Parsing does not execute imported code or create bytecode.
    for p in ROOT.rglob("*.py"):
        ast.parse(p.read_text(),filename=str(p))
    print("PASS: provenance; exact obstruction and derivative enclosures; inventory;")
    print("displayed constants; both radius budgets and norm conventions; exact jets;")
    print("analytic-bound examples; reading-order proof files; Python syntax.")
    print("Numerical suprema and K12/K18 obstruction values were not promoted to certificates.")


if __name__ == "__main__":
    main()
