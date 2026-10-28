"""Audit the retained enclosures against exact rational endpoints and original bytes."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import json, hashlib
from flint import arb, ctx
ctx.prec=512
TOP=Path(__file__).resolve().parents[1]
ROOT=TOP.parents[1]
D=json.loads((TOP/'evidence/recomputed.json').read_text())
ORIGINAL=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert hashlib.sha256(ORIGINAL.read_bytes()).hexdigest()==D['input_sha256']
assert hashlib.sha256((TOP/'code/recompute.py').read_bytes()).hexdigest()==D['script_sha256']
intervals={
 'c0': ('15.7260878319246786225638146971829','15.7260878319246786225638146971831'),
 'normalization_correction_z': ('-1.198605236453734890460334164888e-20','-1.198605236453734890460334164887e-20'),
 'slope': ('3386927.83874448932844599542335954','3386927.83874448932844599542335956'),
 'c_X_bound': ('0.00362844569114920751639699158385338','0.00362844569114920751639699158385339'),
 'middle_taylor_absolute_remainder': ('0','7.82e-183'),
}
def a(s):
 f=Fraction(s)
 return arb(f.numerator)/f.denominator
for name,(lo,hi) in intervals.items():
 val=arb(D[name]['ball'])
 assert a(lo)<val and val<a(hi), (name,val,lo,hi)
result={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS',
 'source_sha256':D['input_sha256'],'computed_script_sha256':D['script_sha256'],
 'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'checks':['Original source bytes match copied input','Original computation script unchanged','Every retained ball lies strictly within the stated exact decimal interval'],
 'exact_decimal_enclosures':intervals,
 'limitation':'This output audit checks arithmetic enclosures and identity; the formula and code proof are separately audited in PROOF.md and VERIFY_REPORT.md.'}
(TOP/'evidence/output_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
