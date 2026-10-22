"""Direct Arb256 product-rule assembly; no producer routines or F outputs."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time,sys
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=256
P=B/'research/localized_forcing/source/runs/forcing/p9_K64_n16_P8_merged.json'
H='b681b9c47d578765965e762aba6ed0a6105c3d1d82f309e98d91375dde7d6d27'
start=time.monotonic();payload=P.read_bytes();assert hashlib.sha256(payload).hexdigest()==H
raw=json.loads(payload);rows=raw['cells'];assert len(rows)==43949 and raw['delta']=='33/2000'
M=arb(9363)/1000000
# Direct norm of the three independently supplied Cartesian entries.
s=raw['sup_D_eps']['B94'];hg=(arb(s['2_0'])**2+2*arb(s['1_1'])**2+arb(s['0_2'])**2).sqrt();assert hg<M
mom={lam:[arb(0),arb(0)] for lam in [1,500]};identities=[];nonnegative=0
max_new={k:arb(0) for k in ['A','B','L','D','E']}
for row in rows:
 key=tuple(row[k] for k in ['ci','q','ks','kp']);identities.append(key)
 assert 4096<=key[0]<=4108 and 0<=key[1]<16 and 0<=key[2]<64 and 0<=key[3]<8
 assert F.from_float(row['dmin'])<F(297,8000)
 vals=[row[k] for k in ['area','G0','G1','GL','GL1','GL2','T0','T1','TL','TL1','TL2']]
 assert all(x>=0 for x in vals);nonnegative+=len(vals)
 a,g0,g1,gl,gl1,gl2,t0,t1,tl,tl1,tl2=map(arb,vals)
 A=t0*g0;B1=t0*g1+t1*g0;L=t0*gl+2*t1*g1+g0*tl
 # Keep the two Hessian contributions separate in this implementation.
 D1=t1*gl+t0*gl1+2*tl*g1+2*M*t1+g1*tl+g0*tl1
 E=t0*gl2+g0*tl2+2*tl*gl+4*t1*gl1+4*g1*tl1+4*tl*M
 for k,z in zip(max_new,[A,B1,L,D1,E]):max_new[k]=max_new[k].max(z)
 for lam in [1,500]:
  l2=lam**2;mom[lam][0]+=a*(l2*(l2*A+L)**2+(l2*B1+D1)**2)
  mom[lam][1]+=a*(l2*l2*A+2*l2*L+E)**2
assert len(set(identities))==43949
identity_hash=hashlib.sha256(json.dumps(identities,separators=(',',':')).encode()).hexdigest()
def box(x):return {'lower':str(F(str(x.lower().fmpq()))),'upper':str(F(str(x.upper().fmpq()))),'display':str(x)}
results={}
for lam,(j3,j4) in mom.items():
 results[str(lam)]={'J3':box(j3),'J4':box(j4),'N3':box(j3.sqrt()),'N4':box(j4.sqrt()),'N31':box(j3**(arb(9)/20)*j4**(arb(1)/20))}
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_CONDITIONAL_DIRECT_ARITHMETIC','precision_bits':256,'source_sha256':H,'M':'9363/1000000','global_hessian_bound':box(hg),'row_count':len(rows),'row_order_sha256':identity_hash,'nonnegative_checks':nonnegative,'max_new_bounds':{k:box(z) for k,z in max_new.items()},'results':results,'scope':'Only saved area/G/T and global second partials are inputs. Physical residual hypotheses OPEN.'}
(D/'evidence/arb.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['utc'],out['status'],len(rows),out['seconds'])
for lam,r in results.items():print(lam,*(r[k]['display'] for k in ['N3','N4','N31']))
