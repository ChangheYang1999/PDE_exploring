"""Repair the report's phi-remainder norm using exact rational arithmetic.

The scalar certificate is deliberately reused from ../03-norm-and-radius. Its three origin
perturbation constants are replaced by the bounds proved in section 7 of
../../exclusion_theorem/audited_estimate/02-remainder/PROOF.md.
No original source is modified or executed as __main__. All output stays here.
"""

import hashlib
import json
import resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))

SOURCE = (Path(__file__).resolve().parents[1]
          / "03-norm-and-radius/verification/rational_certificate.py")
DESTINATION = Path(__file__).resolve().parent
text = SOURCE.read_text()
body = text.split('if __name__ == "__main__":')[0]
start = body.index("    Z1 = max(")
end = body.index("\n    # Endpoint-anchored", start)
replacement = """    Z1 = max(
        [r**(j-1)+F(11-j,2)*r**8+F(9-j,2)*r**10 for j in (3,5,7)]
        + [r**7/((6+sigma)*(7+sigma))])/A0
    D1 = max(
        [(j-1)*r**(j-1)+8*F(11-j,2)*r**8+10*F(9-j,2)*r**10
         for j in (3,5,7)]
        + [(8+sigma)*r**7/((6+sigma)*(7+sigma))])/A0
    J1 = max(
        [j*(j-1)*r**(j-3)+72*F(11-j,2)*r**6+110*F(9-j,2)*r**8
         for j in (3,5,7)]
        + [r**5])/A0
"""
repaired = body[:start] + replacement + body[end:]
namespace = {"__file__": str(DESTINATION / "norm_repair.py")}
exec(compile(repaired, "<audited scalar certificate with phi bounds>", "exec"),
     namespace)

cases = {
    "computed_parameters": ("10.150725", "0.0135206", "0.06", "0.0003", "1"),
    "A4_parameter_widths": ("4", "0.0625", "0.06", "0.0003", "0.5"),
    "A4_fixed_parameters": ("4", "0.0625", "0", "0", "0.5"),
}
output = {
    "source": "../03-norm-and-radius/verification/rational_certificate.py",
    "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
    "scope": "Three revised origin bounds; all other audited scalar formulas reused.",
    "cases": {name: namespace["cert"](*args) for name, args in cases.items()},
}
(DESTINATION / "norm_repair.json").write_text(json.dumps(output, indent=2) + "\n")
for name, data in output["cases"].items():
    print(name)
    for key in ("delta0", "DN", "M", "Me", "KAv", "Kev", "Rvv", "C2",
                "epsilon_formula", "epsilon_decade"):
        value = data["rounded_down"].get(key, data["rounded_up"][key])
        print(f"  {key}: {value}")
