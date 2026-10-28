"""Original-data source annulus and exact finite homological gaps."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];TOP=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
CERT=ROOT/'proofs/15_modal_source/evidence/source_512_result.json'
def aa(q):
 q=F(q);return arb(q.numerator)/q.denominator
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pack(x):
 def dy(q):
  n,e=q.mid().man_exp();return [str(n),int(e)]
 return {'display':x.str(42),'lower_binary':dy(x.lower()),'upper_binary':dy(x.upper())}
start=time.monotonic();ctx.threads=1
assert sha(SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(SRC,allow_pickle=False) as npz:
 k=F.from_float(float(npz['k']));knots=[F.from_float(float(v)) for v in npz['knots']]
assert k==F(1615536043799051,9007199254740992)
cert=json.loads(CERT.read_text());a,b=map(F,cert['source_bracket']);l,r=map(F,cert['source_span'])
assert any((x,y)==(l,r) for x,y in zip(knots,knots[1:]))
mu=(F(99999997745,10**11),F(99999997750,10**11));A=(2/k-mu[1],2/k-mu[0])
assert F(10)<A[0]<A[1]<F(51,5)
assert 10*mu[1]<A[0] and A[1]<11*mu[0]
records=[]
for degree in range(2,12):
 for m in range(degree+1):
  n=degree-m
  for component in (0,1):
   u=m-(component==0);v=n-u-(component==1)
   vals=[u*2/k+v*z for z in mu];lo,hi=min(vals),max(vals)
   assert lo>0 or hi<0
   gap=min(abs(lo),abs(hi));assert gap>F(3,20)
   records.append({'degree':degree,'m':m,'n':n,'component':component,'denominator_interval':[str(lo),str(hi)],'absolute_lower':str(gap)})
assert len(records)==150
minrec=min(records,key=lambda z:F(z['absolute_lower']))
assert F(99,100)<mu[0] and 12*F(99,100)>A[1]
replays=[]
for bits in (256,384):
 ctx.prec=bits
 left=aa(a)-aa(l).exp();right=aa(r).exp()-aa(b)
 assert left>aa(F(1,1000)) and right>aa(F(1,1000))
 assert aa(a).log()>aa(l) and aa(b).log()<aa(r)
 replays.append({'bits':bits,'left_physical_gap':pack(left),'right_physical_gap':pack(right),'source_log_lower':pack(aa(a).log()),'source_log_upper':pack(aa(b).log())})
out={'checked_at':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(SRC),'source_certificate_sha256':sha(CERT),'script_sha256':sha(Path(__file__)),'k':str(k),'mu_interval':[str(q) for q in mu],'A_interval':[str(q) for q in A],'source_bracket':[str(a),str(b)],'source_span':[str(l),str(r)],'original_consecutive_knots':True,'homological_denominators':records,'minimum_gap_record':minrec,'minimum_gap_display':float(F(minrec['absolute_lower'])),'certified_all_gaps_gt':'3/20','backward_rate':'99/100','convergence_exponent_lower':str(12*F(99,100)-A[1]),'certified_source_analytic_disk_radius':'1/1000','annulus_replays':replays,'seconds':time.monotonic()-start,'scope':'Uses previously certified source and mu box plus exact divergence identity; no numerical conjugacy radius or inverse constant.'}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['checked_at'],'minimum homological gap',out['minimum_gap_display'],'seconds',out['seconds'])
for z in replays:print(z['bits'],z['left_physical_gap']['display'],z['right_physical_gap']['display'])
