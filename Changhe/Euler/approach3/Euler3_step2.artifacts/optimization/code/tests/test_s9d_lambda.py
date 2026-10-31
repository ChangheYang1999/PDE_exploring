"""S9d weight helper (lead registration 2026-10-25T17:20:02Z; verifier repairs 18:32Z): skip before any division; no chain on skip; lambda_k = sqrt(kappa C0 / b0)."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from s9d_lambda import s9d_weights

def test_b0_zero():
    w = s9d_weights(C0=1e-6, E_ren=0.0, ratio=0.0)
    assert w["skip"] and w["lambda_by_kappa"] is None and w["b0"] == 0.0, w     # both targets met AND b0 = 0: skipped before the division
    w = s9d_weights(C0=1e-6, E_ren=0.0, ratio=0.0, target=-1.0)                 # targets impossible, b0 = 0: the division guard must catch it
    assert w["skip"] and "b0" in w["reason"] and w["lambda_by_kappa"] is None, w
    print("  b0 = 0: skipped before division:", w["reason"])

def test_targets_met():
    w = s9d_weights(C0=1e-6, E_ren=0.03, ratio=-0.04)
    assert w["skip"] and w["lambda_by_kappa"] is None and abs(w["b0"] - 0.0025) < 1e-15, w
    print("  both targets met: skipped:", w["reason"])
    w = s9d_weights(C0=1e-6, E_ren=0.03, ratio=-0.06)                              # one target missed: chain runs
    assert not w["skip"] and w["lambda_by_kappa"] is not None

def test_normal():
    C0, E, H = 7.21912895394085e-07, -1.5116074445115828, -0.7187675795940742
    w = s9d_weights(C0, E, H)
    b0 = E * E + H * H
    assert not w["skip"] and abs(w["b0"] - b0) < 1e-18
    for k in (0.1, 1.0, 10.0, 100.0):
        assert abs(w["lambda_by_kappa"]["%g" % k] - math.sqrt(k * C0 / b0)) <= 1e-17 * math.sqrt(k * C0 / b0)
    assert abs(w["lambda_by_kappa"]["1"] - 0.0005076221723711057) < 1e-18          # the 17:28Z CPU test value on the S11 smoke state
    w2 = s9d_weights(float("nan"), E, H); assert w2["skip"] and "C0" in w2["reason"]
    print("  normal case: lambda(kappa 1) = %.17g" % w["lambda_by_kappa"]["1"])

if __name__ == "__main__":
    test_b0_zero(); test_targets_met(); test_normal(); print("S9D LAMBDA TESTS PASSED")
