from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for rel,h in m['inputs'].items():assert sha(B/rel)==h,rel
p=json.loads((B/'data/parameters.json').read_text())
def C(x):
 f=Q(str(x));return arb(f.numerator)/f.denominator
def enclosure(x,den):
 z=(x*den).floor().unique_fmpz();assert z is not None
 lo=Q(int(z),den);hi=lo+Q(1,den);assert C(lo)<x<C(hi)
 return {'lower_exact':str(lo),'upper_exact':str(hi)}
c=Q(p['c']);q=1/c-4;delta=1-1/c;D=5*c-1;alpha=-2*q-2;E=Q(p['E']);assert E==Q(93,250)
S=2*delta*delta/(alpha*(alpha+delta)*(alpha+2*delta));assert S==1/alpha-2/(alpha+delta)+1/(alpha+2*delta)
rows=[];checks=2
for name,angle in p['angles'].items():
 ep=json.loads((B/f'data/{name}_endpoint.json').read_text());A={int(k):Q(v) for k,v in ep['F12'].items()};P={int(k):Q(v) for k,v in ep['P'].items()};th={int(k):Q(v) for k,v in ep['Theta0'].items()}
 ns=set(A)|set(P);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/sum(P.get(n,0)**2 for n in ns)
 bound=(arb.pi()*C(proj)).sqrt()/(4*C(c));t=C(angle)
 def ev(cf,d=False):return sum((C(v)*n*(n*t).cos() if d else C(v)*(n*t).sin()) for n,v in cf.items())
 av,ad,pv,pd=ev(A),ev(A,True),ev(P),ev(P,True);phi=abs(C(q)*(av*pd-ad*pv))/(4*C(c)*(C(q*q)*pv*pv+pd*pd).sqrt())
 H=C(p['H0'][name]);assert H<phi;checks+=1;g0=sum(n*v for n,v in th.items());assert g0>0;checks+=1
 r0=((2*arb.pi()).sqrt()*H*C(E*g0)/(C(D)*bound))**C(1/delta);cap=bound*r0**C(q+1)*C(S).sqrt()
 item={'candidate':name,'H0_integer':p['H0'][name],'Phi':phi.str(45),'B':bound.str(45),'g0_exact':str(g0),'r0':r0.str(45),'cap':cap.str(45),'cap_enclosure':enclosure(cap,10**15),'targets':{}}
 checks+=1
 for key,beta in p['betas'].items():
  ratio=cap/C(beta);crit=C(D)*bound/((2*arb.pi()).sqrt()*H*C(g0))*(bound*C(S).sqrt()/C(beta))**C(delta/(-q-1))
  above=bool(ratio>1);below=bool(ratio<1);assert above != below
  assert above==bool(C(E)<crit) and below==bool(C(E)>crit);checks+=3
  item['targets'][key]={'beta_exact':beta,'ratio':ratio.str(45),'ratio_enclosure':enclosure(ratio,10**9),'Ecrit':crit.str(45),'ceiling_exceeds_target':above,'ceiling_below_target':below};checks+=1
 rows.append(item)
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'checks':checks,'E_exact':str(E),'shape_factor_exact':str(S),'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'verdict':'CONFIRMED conditional full-radial ceiling with E=93/250 and zero other errors; no existence or finite-radius closure'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS',checks,r['utc'],r['elapsed_s'])
for row in rows:print(row['candidate'],'cap',row['cap'],'ratios',[(k,x['ratio']) for k,x in row['targets'].items()])
