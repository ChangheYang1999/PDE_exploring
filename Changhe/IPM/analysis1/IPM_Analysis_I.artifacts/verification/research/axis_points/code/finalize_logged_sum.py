"""Recover rigorous finalization from a completed logged sum after a fail-safe check.

Arb decimal endpoint strings enclose the exact endpoints; their hull encloses
all original arithmetic values. Only complete quadratures are admitted.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,aa,jsball,utc
ap=argparse.ArgumentParser();ap.add_argument('--tag',required=True);args=ap.parse_args();ctx.prec=192;ctx.threads=1
E=BASE/'research/axis_points/evidence';pp=E/(args.tag+'_partition.json');lp=E/(args.tag+'_run.log');part=json.loads(pp.read_text())
entries=[]
for line in lp.read_text().splitlines():
 try:entries.append(json.loads(line))
 except json.JSONDecodeError:pass
last=[row for row in entries if row.get('stage')=='quadrature'][-1]
assert last['done']==last['total']==len(part['q'])
loaded=BASE/'research/axis_points/code/axis_arb_v2_archived.py'
assert hashlib.sha256(loaded.read_bytes()).hexdigest()==part['script_sha256']
def hull(row):return arb(row['lower']).union(arb(row['upper']))
summation=hull(last['sum']);error=sum((hull(v) for v in part['errors_before_prefactor'].values()),arb(0));assert error>0
cp=BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json';ch=hashlib.sha256(cp.read_bytes()).hexdigest()
assert ch=='16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db'
strain=hull(json.loads(cp.read_text())['strain']);d=Data();assert d.sha==part['input_sha256']
x=aa(F(part['settings']['x']));velocity=x*d.pref*(summation+arb(0,error.upper()));drift=x*(1+strain)/3+velocity
out={'utc':utc(),'status':'POINT_ENCLOSURE_REQUIRES_INDEPENDENT_AUDIT','settings':part['settings'],'input_sha256':d.sha,'quadrature_script_sha256':part['script_sha256'],'finalizer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'partition_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'complete_log_sha256':hashlib.sha256(lp.read_bytes()).hexdigest(),'scalar_certificate_sha256':ch,'quadrature_sum':jsball(summation),'unscaled_error':jsball(error),'velocity_U1':jsball(velocity),'canonical_drift_w':jsball(drift),'seconds_to_last_sum':last['seconds'],'finalization_note':'Completed v2 quadrature was recovered from outward endpoint strings after the display-ball containment assertion failed safe. The tighter recorded endpoint hull is used here; no arithmetic result was discarded or treated as exact.','scope':'Axis point only; no profile existence.'}
(E/(args.tag+'_result.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
