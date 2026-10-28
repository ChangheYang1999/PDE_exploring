# Independent certification record

Updated 2026-10-28T01:52:10Z.

The proof is ../PROOF.md. Run with Python 3:

    python3 code/certify_structured_layercake.py --step 10000 --out data/structured_layercake_certificate_fine.json

The source hash, real completion time, arithmetic precision, exact parameters and safe decimal lower endpoint are in the JSON. The run used 800000 cells on exp([-40,40]) and certified C_(1/2),D_(1/2)>=2.0888866916. Its interval upper endpoint bounds only the finite integral. Nonnegative omitted tails justify the lower conclusion.

Branch conditions use interval min/max: vertical and circular contributions extend by zero at their endpoints. A branch is skipped only when the whole interval is outside its active range. Complex logarithm branches are fixed by the proof. All nonfinite results raise; no NaN is silently replaced by zero. The only clipping is max(J,0), justified by the proved positivity of J.
