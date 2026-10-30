from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,h in m['inputs'].items():assert sha(B/rel)==h,rel
p=json.loads((B/'data/parameters.json').read_text());peer=json.loads((B/'source/T2_result.json').read_text())['C']
def C(x):
 f=Q(str(x));return arb(f.numerator)/f.denominator
def power2(x):return C(2)**C(x)
def parse(s):
 if s.startswith('['):
  v,e=s.strip('[]').split('+/-');return arb(v.strip(),e.strip())
 return C(s)
checks=[]
def check(label,x):
 assert bool(x),label
 checks.append(label)
def lower(label,x,b):check(label,x>C(b))
def upper(label,x,b):check(label,x<C(b))
c=Q(p['c']);q=1/c-4;delta=1-1/c;D=5*c-1;alpha=-2*q-2
check('parameters',Q(-5)<q<Q(-3) and D==1-c*(q-delta) and 0<delta<q+5)
Sigma=C(1)/2+power2(3-q)+power2(1-q)+power2(2-q)/C(q+5)
eps=Q(1,4);a=q-eps
Cala=C(1)/2+power2(3-a)+power2(a+2)/C(-a)+power2(-a-2)/C(-a-3)+power2(2-a)/C(a+5)+power2(1-a)
for key,x in [('Sigma_q_lower',Sigma),('2^-q_lower',power2(-q)),('D_delta_lower',C(D)),('C_a+L_a_at_eps_1/4_lower',Cala),('gain_(4+delta)/(4+2delta)_lower',C((4+delta)/(4+2*delta)))]:lower(key,x,peer[key])
rows=[]
for name,angle in p['angles'].items():
 ep=json.loads((B/f'data/{name}_endpoint.json').read_text());A={int(k):Q(v) for k,v in ep['F12'].items()};P={int(k):Q(v) for k,v in ep['P'].items()};th={int(k):Q(v) for k,v in ep['Theta0'].items()}
 ns=set(A)|set(P);pp=sum(P.get(n,0)**2 for n in ns);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/pp
 check(name+':projection',pp>0 and proj>0)
 bound=(arb.pi()*C(proj)).sqrt()/(4*C(c));t=C(angle)
 def ev(cf,d=False):return sum((C(v)*n*(n*t).cos() if d else C(v)*(n*t).sin()) for n,v in cf.items())
 av,ad,pv,pd=ev(A),ev(A,True),ev(P),ev(P,True);norm=C(q*q)*pv*pv+pd*pd
 check(name+':point_denominator',norm>0)
 phi=abs(C(q)*(av*pd-ad*pv))/(4*C(c)*norm.sqrt());g0=sum(n*v for n,v in th.items());C0=bound/(2*arb.pi()).sqrt();pr=peer[name]
 lower(name+':Phi',phi,pr['Phi_lower']);upper(name+':C0',C0,pr['C0_upper']);check(name+':g0_overlap',C(g0).overlaps(parse(pr['g0'])))
 item={'candidate':name,'B':bound.str(45),'Phi':phi.str(45),'g0_exact':str(g0),'targets':{}}
 for key,beta in p['betas'].items():
  target=pr[p['peer_target_keys'][key]]
  rb=(bound/(C(beta)*C(alpha).sqrt()))**C(1/(-q-1));kc=C(D)*bound*rb**C(delta)/((2*arb.pi()).sqrt()*C(g0));ec=kc/phi
  jm=Sigma*(5/rb)**C(delta);jm25=Cala*(5/rb)**C(eps);room=kc/C0;struct=power2(-q)*Sigma
  check(name+key+':radius_gt5',rb>5)
  values={'r_beta_upper':rb,'Kcrit_upper':kc,'Ecrit_upper':ec,'Ecrit_minus_583/1000_upper':ec-C('583/1000'),'J_over_H_lower':jm,'J_over_H_lower_eps_1/4':jm25,'J_Phi_over_Kcrit_lower':jm*phi/kc,'room_Kcrit_over_C0_upper':room,'structural_J_over_C0_lower':struct,'structural_ratio_lower':struct/room,'structural_ratio_without_2^-q_lower':Sigma/room}
  for label,v in values.items():
   if label.endswith('_upper'):upper(name+key+label,v,target[label])
   else:lower(name+key+label,v,target[label])
  check(name+key+':main_block',jm*phi>kc)
  if key=='sharpw_rounded_ceiling':check(name+':factor_over40',jm>40*(ec-C('583/1000')))
  item['targets'][key]={k:v.str(45) for k,v in values.items()}
 rows.append(item)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'checks':checks,'check_count':len(checks),'Sigma':Sigma.str(45),'q_exact':str(q),'delta_exact':str(delta),'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'verdict':'CONFIRMED campaign obstruction for the specified uniform majorant; R<=r_grad asserted necessity is REFUTED and unnecessary; conditional structural variant retained'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS',len(checks),r['utc'],r['elapsed_s'])
for row in rows:print(row['candidate'],'sharpw',row['targets']['sharpw_rounded_ceiling']['J_over_H_lower'],row['targets']['sharpw_rounded_ceiling']['J_Phi_over_Kcrit_lower'])
