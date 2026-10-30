from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib,json,time
from flint import arb,ctx
T=time.monotonic();B=Path(__file__).resolve().parents[1];ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads((B/'data/parameters.json').read_text()); m=json.loads((B/'data/manifest.json').read_text())
for name,row in m['inputs'].items():assert sha(B/'source'/name)==row['sha256']
def A(x):
 f=F(str(x));return arb(f.numerator)/f.denominator
def ball(s):
 if '+/-' not in s:return A(s)
 x,r=s.strip('[] ').split('+/-');return arb(x.strip(),r.strip())
pp=json.loads((B/'source/pointwise_parameters.json').read_text())
r=json.loads((B/'source/pointwise_result.json').read_text())
c=F(pp['c']);q=1/c-4;delta=1-1/c;D=1-c*(q-delta);a=-q
E=(a-1)/(2*a*(a-3));nchecks=0;rows=[]
assert D==5*c-1;nchecks+=1
for x in r['rows']:
 name=x['candidate'];H=A(p['H0'][name]);G=A(x['G_lower_exact']);bv=ball(x['B'])
 assert H<ball(x['H_point']);nchecks+=1
 crit={}
 for key,beta in pp['betas'].items():
  ev=A(D)*bv/((2*arb.pi()).sqrt()*H)*(bv/(A(beta)*A(-2*q-2).sqrt()))**A(delta/(-q-1))/G
  assert ev<A(p['Ecrit_upper'][key]);assert ev<A(E);nchecks+=2
  crit[key]=ev.str(30)
 radius=((2*arb.pi()).sqrt()*H*A(E)*G/(A(D)*bv))**A(1/delta)
 amp=bv*radius**A(q+1)
 crude=amp/A(-2*q-2).sqrt()
 exp=-2*q-2
 shape=amp*A(1/exp-2/(exp+delta)+1/(exp+2*delta)).sqrt()
 assert crude<A(p['crude_cap_upper']);assert shape<A(p['shape_cap_upper']);nchecks+=2
 rows.append({'candidate':name,'integer_H0':int(p['H0'][name]),'Ecrit':crit,'crude_cap':crude.str(30),'shape_cap':shape.str(30)})
d=F(p['distance021']);ratios=[]
for budget,lower in zip(p['ceilings'],p['ratios']):
 value=d/F(budget);assert value>F(lower);nchecks+=1;ratios.append(str(value))
assert F(pp['betas']['fixed_sharpw_ball'])==F('1.3193359375e-6');nchecks+=1
assert F(p['crude_cap_upper'])<F(pp['betas']['fixed_sharpw_ball']);nchecks+=1
assert F(p['newton_eta_lower'])==F(min(p['H0'].values()),2);nchecks+=1
assert F(1,min(p['H0'].values()))<F(p['newton_K_upper']);nchecks+=1
sc=json.loads((B/'source/screening_parameters.json').read_text())
sm=[]
for item in sc['screening_rows']:
 if item['candidate'] in {'015','016','020'}:
  actual=F(item['distance_floor'])-F('25/54684');lo=F(item['displayed_margins'][2]);assert actual>lo;nchecks+=1
  sm.append({'candidate':item['candidate'],'margin_exact':str(actual),'displayed_lower':str(lo)})
res={'completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-T,'precision_bits':ctx.prec,'checks':nchecks,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'parameters_sha256':sha(B/'data/parameters.json'),'Etest_exact':str(E),'rows':rows,'distance_ratios_exact':ratios,'screening_margins':sm,'verdict':'CONFIRMED finite constants with printed integer H0; analytic scope qualifications in PROOF'}
(B/'verification/result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
