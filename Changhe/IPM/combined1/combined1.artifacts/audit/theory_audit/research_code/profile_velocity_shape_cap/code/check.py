from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,d in m['inputs'].items():assert sha(B/rel)==d,rel
p=json.loads((B/'data/parameters.json').read_text())
def C(x):
 f=Q(str(x));return arb(f.numerator)/f.denominator
c=Q(p['c']);q=1/c-4;delta=1-1/c;D=1-c*(q-delta);alpha=-2*q-2
S=2*delta*delta/(alpha*(alpha+delta)*(alpha+2*delta))
assert D==5*c-1 and Q(-5)<q<Q(-3) and delta>0
assert S==1/alpha-2/(alpha+delta)+1/(alpha+2*delta)
assert C(S).sqrt()<1/C(alpha).sqrt()
E=Q(p['E']);assert E==Q(583,1000)
rows=[];checks=4
for name,angle in p['angles'].items():
 ep=json.loads((B/'data'/f'{name}_endpoint.json').read_text())
 A={int(k):Q(v) for k,v in ep['F12'].items()};P={int(k):Q(v) for k,v in ep['P'].items()};th={int(k):Q(v) for k,v in ep['Theta0'].items()}
 ns=set(A)|set(P);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/sum(P.get(n,0)**2 for n in ns)
 bound=(arb.pi()*C(proj)).sqrt()/(4*C(c));t=C(angle)
 def ev(cf,d=False):return sum((C(v)*n*(n*t).cos() if d else C(v)*(n*t).sin()) for n,v in cf.items())
 av,ad,pv,pd=ev(A),ev(A,True),ev(P),ev(P,True)
 phi=abs(C(q)*(av*pd-ad*pv))/(4*C(c)*(C(q*q)*pv*pv+pd*pd).sqrt())
 H=C(p['H0'][name]);assert H<phi;checks+=1
 g0=sum(n*v for n,v in th.items());power=1/c+2
 v0=abs((power-1)*sum(n*v/(power*power-n*n) for n,v in th.items()))
 assert g0>0 and v0>0;checks+=1
 item={'candidate':name,'H0_integer':p['H0'][name],'H_point':phi.str(40),'B':bound.str(40),'g0_exact':str(g0),'v0_exact':str(v0),'versions':{}}
 for label,v in [('V_zero',Q(0)),('V_lead',v0)]:
  r0=((2*arb.pi()).sqrt()*H*(C(v)+C(E*g0))/(C(D)*bound))**C(1/delta)
  cap=bound*r0**C(q+1)*C(S).sqrt()
  crude=bound*r0**C(q+1)/C(alpha).sqrt()
  assert cap<C(p['cap_upper']);checks+=1
  assert cap<min(C(b) for b in p['betas'].values());checks+=1
  thresholds={}
  for key,beta in p['betas'].items():
   crit=C(D)*bound/((2*arb.pi()).sqrt()*H)*(bound*C(S).sqrt()/C(beta))**C(delta/(-q-1))/C(g0)-C(v/g0)
   crudecrit=C(D)*bound/((2*arb.pi()).sqrt()*H)*(bound/(C(alpha).sqrt()*C(beta)))**C(delta/(-q-1))/C(g0)-C(v/g0)
   assert crit<C(p['Ecrit_upper'][key])<C(E);checks+=2
   assert crit<crudecrit;checks+=1
   thresholds[key]={'retained_shape':crit.str(40),'crude_cutoff':crudecrit.str(40),'strict_shape_upper':p['Ecrit_upper'][key]}
  item['versions'][label]={'radius':r0.str(40),'cap':cap.str(40),'crude_cap':crude.str(40),'thresholds':thresholds}
 rows.append(item)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'checks':checks,'q_exact':str(q),'delta_exact':str(delta),'shape_factor_exact':str(S),'shape_to_crude':C(alpha*S).sqrt().str(40),'E_exact':str(E),'cap_upper':p['cap_upper'],'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'verdict':'CONFIRMED finite arithmetic; analytic application pending independent review'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n')
for row in rows:
 v=row['versions']['V_zero'];print(row['candidate'],'cap',v['cap'],'thresholds',[(k,x['retained_shape']) for k,x in v['thresholds'].items()])
print('PASS',checks,r['utc'],r['elapsed_s'])
