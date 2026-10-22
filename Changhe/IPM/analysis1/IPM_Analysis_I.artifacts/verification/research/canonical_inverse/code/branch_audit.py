"""Explicit branch-domain audit for every Cauchy rectangle in the scalar certificate."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx
from strain_arb import Data,aa,jsball
BASE=Path(__file__).resolve().parents[3];ctx.prec=160;ctx.cap=8;ctx.threads=1
start=time.monotonic();d=Data();part=json.loads((BASE/'research/canonical_inverse/evidence/strain_arb_20_32_partition.json').read_text())
minima={k:None for k in ('Re_1_minus_q','Re_s','abs_chi_denominator','Re_cos_theta')}
def record(k,x):
 assert x>0,(k,x)
 if minima[k] is None or x<minima[k]:minima[k]=x
for left,right in part['q']:
 a,b=F(left),F(right);mid=aa((a+b)/2);h=aa((b-a)/2)
 q=acb(arb(mid,(3*h).upper()),arb(0,(2*h).upper()))
 record('Re_1_minus_q',(1-q).real.lower())
 s=1-(1-q).pow(acb(d.b),analytic=True)
 record('Re_s',s.real.lower())
 den=s+d.r0**2*(1-s)
 record('abs_chi_denominator',den.abs_lower())
for left,right in part['theta_over_pi_half']:
 a,b=F(left),F(right);mid=aa((a+b)/2)*arb.pi()/2;h=aa((b-a)/2)*arb.pi()/2
 z=acb(arb(mid,(2*h).upper()),arb(0,h.upper()))
 record('Re_cos_theta',z.cos().real.lower())
out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':d.sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'radial_boxes':len(part['q']),'angular_boxes':len(part['theta_over_pi_half']),'strict_positive_margins':{k:jsball(v) for k,v in minima.items()},'seconds':time.monotonic()-start,'status':'PASS'}
(BASE/'research/canonical_inverse/evidence/branch_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
