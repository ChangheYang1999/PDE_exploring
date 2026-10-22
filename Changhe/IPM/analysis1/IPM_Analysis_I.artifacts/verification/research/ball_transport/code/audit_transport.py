"""Exact Fraction checks across different import precisions and cancellation scales."""
import json,hashlib,random
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
from dyadic_ball import export_ball,import_ball
BASE=Path(__file__).resolve().parents[3]
def dyad(v):
 m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def endpoints(x):
 m,r=dyad(x.mid()),dyad(x.rad());return m-r,m+r
ctx.prec=320;cases=[arb(0),arb(1),arb(1,'1.23451'),arb(1,'1.23451e-70'),arb(1)/3,arb(2).sqrt(),arb('1e-300'),arb('-1e300','1e220')]
rng=random.Random(20261020)
for _ in range(64):
 m=rng.randrange(-2**300,2**300);e=rng.randrange(-1500,1000);r=rng.randrange(0,2**30);f=e-rng.randrange(1,500)
 cases.append(arb((m,e),(r,f)))
records=[]
for index,x in enumerate(cases):
 ctx.prec=320;lo,hi=endpoints(x);saved=json.loads(json.dumps(export_ball(x)));m=F(saved['mid_m'])*F(2)**int(saved['mid_e']);r=F(saved['rad_m'])*F(2)**int(saved['rad_e']);assert m-r==lo and m+r==hi
 for precision in (8,16,53,128,256,512):
  ctx.prec=precision;back=import_ball(saved);bl,bh=endpoints(back);assert bl<=lo and hi<=bh,(index,precision)
  records.append({'case':index,'import_bits':precision,'verdict':'CONTAINED'})
for bad in (' 12','+12','1_000','01','-0','',12):
 sample=export_ball(arb(1));sample['mid_m']=bad
 try:import_ball(sample)
 except ValueError:pass
 else:raise AssertionError(('bad integer accepted',bad))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','cases':len(cases),'comparisons':len(records),'import_bits':[8,16,53,128,256,512],'python_flint_version':flint.__version__,'FLINT_version':flint.__FLINT_VERSION__,'source_sha256':hashlib.sha256((Path(__file__).parent/'dyadic_ball.py').read_bytes()).hexdigest(),'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Independent exact rational endpoint containment after real JSON round trip; finite zero/tiny/huge/cancellation values, import precision below and above export precision','scope':'Computational check of implementation. General containment follows the standalone lemma, conditional on outward Arb arithmetic and exact man_exp contract.'}
(BASE/'research/ball_transport/evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
