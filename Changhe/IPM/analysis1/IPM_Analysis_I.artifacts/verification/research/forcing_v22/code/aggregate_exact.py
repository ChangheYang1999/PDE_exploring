"""Independent exact nine-moment expansion plus iv160 fractional powers."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,sys
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];iv.dps=160;start=time.monotonic();p=D/'source/runs/forcing/v22_p9_merged.json';raw=p.read_bytes();h=hashlib.sha256(raw).hexdigest();assert h=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
x=json.loads(raw);R=x['cells'];z={k:Q(0) for k in ['vv','vl','ll','bb','bd','dd','ve','le','ee']};ids=[];positive=0;ff=Q.from_float
for row in R:
 ids.append([row['ci'],row['q'],32*row['bs']+row['ks'],4*row['bp']+row['kp']]);a,v,b,l,d,e=[ff(row[k]) for k in ['area','F0','F1','FL','FL1','FL2']]
 assert min(a,v,b,l,d,e)>=0;positive+=6
 for name,y in [('vv',v*v),('vl',v*l),('ll',l*l),('bb',b*b),('bd',b*d),('dd',d*d),('ve',v*e),('le',l*e),('ee',e*e)]:z[name]+=a*y
assert len(R)==len(set(tuple(k) for k in ids))==43949
p3=[z['dd'],z['ll']+2*z['bd'],2*z['vl']+z['bb'],z['vv']];p4=[z['ee'],4*z['le'],2*z['ve']+4*z['ll'],4*z['vl'],z['vv']]
def horner(c,t):
 r=Q(0)
 for a in reversed(c):r=r*t+a
 return r
def vi(q):return iv.mpf(q.numerator)/q.denominator
def ep(t):
 sign,m,e,bc=t
 assert sign in (0,1) and m>=0 and bc>=0 and ((m==0 and e==0 and bc==0) or (m>0 and int(m).bit_length()==bc)),t
 return Q(-m if sign else m)*Q(2)**e
def box(q):return {'lower':str(ep(q._mpi_[0])),'upper':str(ep(q._mpi_[1])),'display':str(q)}
ceilings={'1':['0.7759','893.16','1.5700'],'500':['1.8107','1638.56','3.5769']};res={}
for lam in [1,500]:
 j3=horner(p3,Q(lam**2));j4=horner(p4,Q(lam**2));saved=x['results'][str(float(lam))];assert 0<j3<ff(saved['I3']) and 0<j4<ff(saved['I4'])
 b3,b4=vi(j3),vi(j4);norms=[iv.sqrt(b3),iv.sqrt(b4),iv.exp((9*iv.log(b3)+iv.log(b4))/20)]
 qs=list(map(Q,ceilings[str(lam)]));assert j3<qs[0]**2 and j4<qs[1]**2 and j3**9*j4<qs[2]**20
 # Also verify the reported binary64 norm endpoints enclose the saved I3,I4.
 c3,c4,c31=[ff(saved[k]) for k in ['bound_order3','bound_order4','bound_order_3_1']]
 i3,i4=ff(saved['I3']),ff(saved['I4']);assert i3<=c3**2 and i4<=c4**2 and i3**9*i4<=c31**20
 assert c3<qs[0] and c4<qs[1] and c31<qs[2]
 res[str(lam)]={'J3_exact':str(j3),'J4_exact':str(j4),'saved_I3_margin':str(i3-j3),'saved_I4_margin':str(i4-j4),'N3':box(norms[0]),'N4':box(norms[1]),'N31':box(norms[2]),'strict_ceiling':ceilings[str(lam)],'saved_output_power_tests':'PASS'}
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_V22_CONDITIONAL_EXACT_AGGREGATION','iv_digits':160,'source_sha256':h,'row_count':len(R),'row_order_sha256':hashlib.sha256(json.dumps(ids,separators=(',',':')).encode()).hexdigest(),'nonnegative_checks':positive,'moments':{k:str(v) for k,v in z.items()},'polynomial_J3':list(map(str,p3)),'polynomial_J4':list(map(str,p4)),'results':res,'scope':'Independent finite exact arithmetic on saved row endpoints, physical model validity OPEN.'}
(D/'evidence/aggregate_exact_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds')
for k,r in res.items():print(k,*(r[z]['display'] for z in ['N3','N4','N31']))
