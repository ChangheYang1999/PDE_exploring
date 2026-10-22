"""All saved v2.2 row contributions by direct Arb512 arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,sys
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];ctx.prec=512;start=time.monotonic();p=D/'source/runs/forcing/v22_p9_merged.json';raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest();assert h=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
x=json.loads(raw);rows=x['cells'];assert len(rows)==43949
mom={k:[arb(0),arb(0)] for k in [1,500]};reg={r:[0,arb(0)] for r in ['inside','transition','straddle']};ids=[];nonnegative=0
for r in rows:
 key=(r['ci'],r['q'],r['bs']*32+r['ks'],r['bp']*4+r['kp']);ids.append(key)
 assert 4096<=key[0]<=4108 and 0<=key[1]<16 and 0<=key[2]<64 and 0<=key[3]<8
 values=[r[k] for k in ['area','F0','F1','FL','FL1','FL2']];assert all(v>=0 for v in values);nonnegative+=6
 a,v,b,l,d,e=map(arb,values);reg[r['regime']][0]+=1;reg[r['regime']][1]+=a
 for lam in [1,500]:
  l2=lam*lam;mom[lam][0]+=a*(l2*(l2*v+l)**2+(l2*b+d)**2);mom[lam][1]+=a*(l2*l2*v+2*l2*l+e)**2
assert len(set(ids))==43949
for k,(n,_) in reg.items():assert n==x['regime_count'][k]
def box(z):return {'lower':str(F(str(z.lower().fmpq()))),'upper':str(F(str(z.upper().fmpq()))),'display':str(z)}
res={}
for lam,(j3,j4) in mom.items():
 saved=x['results'][str(float(lam))];assert j3<arb(saved['I3']) and j4<arb(saved['I4'])
 res[str(lam)]={'J3':box(j3),'J4':box(j4),'N3':box(j3.sqrt()),'N4':box(j4.sqrt()),'N31':box(j3**(arb(9)/20)*j4**(arb(1)/20)),'saved_I3_margin':box(arb(saved['I3'])-j3),'saved_I4_margin':box(arb(saved['I4'])-j4)}
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_V22_CONDITIONAL_DIRECT_AGGREGATION','precision_bits':512,'source_sha256':h,'row_count':len(rows),'row_order_sha256':hashlib.sha256(json.dumps(ids,separators=(',',':')).encode()).hexdigest(),'nonnegative_checks':nonnegative,'regimes':{k:{'rows':v[0],'area':box(v[1])} for k,v in reg.items()},'results':res,'scope':'Saved positive row endpoints only. Physical model enclosures and actual forcing norm OPEN.'}
(D/'evidence/aggregate_arb.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds')
for k,r in res.items():print(k,*(r[z]['display'] for z in ['N3','N4','N31']))
