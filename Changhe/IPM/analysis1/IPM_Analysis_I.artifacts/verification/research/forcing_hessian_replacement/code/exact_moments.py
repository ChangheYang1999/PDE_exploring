"""Independent exact rational moment polynomials, followed by interval roots."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,sys
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];iv.dps=120
P=D.parents[1]/'research/localized_forcing/source/runs/forcing/p9_K64_n16_P8_merged.json'
t=time.monotonic();text=P.read_bytes();h=hashlib.sha256(text).hexdigest()
assert h=='b681b9c47d578765965e762aba6ed0a6105c3d1d82f309e98d91375dde7d6d27'
x=json.loads(text);R=x['cells'];m=Q(9363,1000000);ff=Q.from_float
S=x['sup_D_eps']['B94'];sq=ff(S['2_0'])**2+ff(S['0_2'])**2+2*ff(S['1_1'])**2
assert sq<m*m
# Moments of products of (value, gradient, Laplacian, grad Laplacian, bi-Laplacian).
# J3 has coefficients (gradlap^2, lap^2+2 grad.gradlap,2 value.lap+grad^2,value^2).
# J4 has coefficients (bilap^2,4 lap.bilap,2 value.bilap+4 lap^2,4 value.lap,value^2).
Z={k:Q(0) for k in ['vv','vl','ll','bb','bd','dd','ve','le','ee']};ids=[];positive=0
for r in R:
 q=[r[k] for k in ['ci','q','ks','kp']];ids.append(q)
 assert q[0] in range(4096,4109) and q[1] in range(16) and q[2] in range(64) and q[3] in range(8)
 assert ff(r['dmin'])<Q(297,8000)
 a=ff(r['area']);g={k:ff(r[k]) for k in ['G0','G1','GL','GL1','GL2']};c={k:ff(r[k]) for k in ['T0','T1','TL','TL1','TL2']}
 assert a>=0 and all(y>=0 for y in g.values()) and all(y>=0 for y in c.values());positive+=11
 v=c['T0']*g['G0'];b=c['T0']*g['G1']+c['T1']*g['G0']
 l=c['T0']*g['GL']+2*c['T1']*g['G1']+g['G0']*c['TL']
 d=c['T1']*(g['GL']+2*m)+c['T0']*g['GL1']+3*c['TL']*g['G1']+g['G0']*c['TL1']
 e=c['T0']*g['GL2']+g['G0']*c['TL2']+2*c['TL']*(g['GL']+2*m)+4*(c['T1']*g['GL1']+g['G1']*c['TL1'])
 for k,z in [('vv',v*v),('vl',v*l),('ll',l*l),('bb',b*b),('bd',b*d),('dd',d*d),('ve',v*e),('le',l*e),('ee',e*e)]:Z[k]+=a*z
assert len(R)==len(set(tuple(q) for q in ids))==43949 and x['delta']=='33/2000'
poly3=[Z['dd'],Z['ll']+2*Z['bd'],2*Z['vl']+Z['bb'],Z['vv']]
poly4=[Z['ee'],4*Z['le'],2*Z['ve']+4*Z['ll'],4*Z['vl'],Z['vv']]
def val(p,x):
 a=Q(0)
 for c in p[::-1]:a=a*x+c
 return a
def ball(z):return iv.mpf(z.numerator)/z.denominator
def endpoint(t):
 s,m,e,b=t;return Q(-m if s else m)*Q(2)**e
def pack(z):return {'lower':str(endpoint(z._mpi_[0])),'upper':str(endpoint(z._mpi_[1])),'display':str(z)}
res={}
for lam in [1,500]:
 j3=val(poly3,Q(lam*lam));j4=val(poly4,Q(lam*lam));assert j3>0 and j4>0
 a,b=ball(j3),ball(j4);n31=iv.exp(iv.log(a**9*b)/20)
 res[str(lam)]={'J3_exact':str(j3),'J4_exact':str(j4),'N3':pack(iv.sqrt(a)),'N4':pack(iv.sqrt(b)),'N31':pack(n31)}
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-t,'status':'PASS_CONDITIONAL_EXACT_MOMENT_ARITHMETIC','iv_digits':120,'source_sha256':h,'M':str(m),'hessian_squared_exact':str(sq),'hessian_squared_margin':str(m*m-sq),'row_count':len(R),'row_order_sha256':hashlib.sha256(json.dumps(ids,separators=(',',':')).encode()).hexdigest(),'nonnegative_checks':positive,'moments':{k:str(v) for k,v in Z.items()},'polynomial_J3':[str(v) for v in poly3],'polynomial_J4':[str(v) for v in poly4],'results':res,'scope':'Exact positive-polynomial computation conditional on saved derivative hypotheses. Original F outputs and final integrals not used.'}
(D/'evidence/exact_iv.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(R),out['seconds'])
for lam,r in res.items():print(lam,*(r[k]['display'] for k in ['N3','N4','N31']))
