from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time,difflib
from flint import arb,ctx
B=Path(__file__).resolve().parents[1]; start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==man['proof_sha256']
for rel,h in man['inputs'].items():assert sha(B/rel)==h,rel
p=json.loads((B/'data/parameters.json').read_text());checks=[]
def check(label,test):
 assert bool(test),label
 checks.append(label)
def C(x):
 f=Q(str(x));return arb(f.numerator)/f.denominator
def enc(x):return x.str(50)
def parse(s):
 if s.startswith('['):
  v,e=s.strip('[]').split('+/-');return arb(v.strip(),e.strip())
 return C(s)
c=Q(p['c']);gam=1/c;q=gam-4;d=1-gam;k=1-q;D=c*k;alpha=-2*q-2;a=-q
check('range',Q(-5)<q<Q(-3) and 0<d<1 and alpha>0)
check('Green exponent',q-2==-k-1)
check('transport exponent',gam-k==q-d)
check('denominator',D==5*c-1 and D==1-c*(q-d))
check('kappa',k==4+d)
check('inner integral coefficient',1-d/(k+d)==k/(k+d))
check('inner derivative identity',(-k)*(1-d/(k+d))-d*k/(k+d)==-k)
check('outer derivative identity',(-k-d)*k/(k+d)==-k)
check('tail target exponent',2*(q+1)==-alpha)
lam=C(1)/2+5*C(2)**C(1-q);e0=C((a-1)/(2*a*(a-3)));R=C(p['Rmax'])
check('lambda greater than Emin',lam>e0)
check('universal lower exceeds quoted',e0>C('7930365/10000000'))
u=5*(lam/e0)**(1/C(d));avg=e0*(1-C(d/(k+d))*(R/u)**C(k));coarse=e0*(1-(R/u)**C(k))
check('ru>Rmax',u>R)
check('average lower',avg>C(p['average_lower']))
check('coarse lower also sufficient',coarse>C(p['average_lower']))
check('strict gap',C(p['average_lower'])>C(p['critical_upper']))
current=C(p['current_universal']);uc=5*(lam/current)**(1/C(d));avgc=current*(1-C(d/(k+d))*(R/uc)**C(k));cc=current*(1-(R/uc)**C(k))
check('current upper above universal floor',current>e0)
check('current switching radius',uc>R)
check('T1 coarse average',cc>C('17277/10000'))
# Compare exact analytic formulas at their joining point, using interval arithmetic.
inner_at_u=e0*(1-C(d/(k+d)));outer_at_u=lam*(5/u)**C(d)*C(k/(k+d))
check('join agreement',inner_at_u.overlaps(outer_at_u))
rows=[];old=json.loads((B/'source/uniform_result.json').read_text())['rows']
for name,angle in p['angles'].items():
 ep=json.loads((B/f'data/{name}_endpoint.json').read_text());A={int(n):Q(v) for n,v in ep['F12'].items()};P={int(n):Q(v) for n,v in ep['P'].items()};th={int(n):Q(v) for n,v in ep['Theta0'].items()}
 ns=set(A)|set(P);pp=sum(P.get(n,0)**2 for n in ns);ap=sum(A.get(n,0)*P.get(n,0) for n in ns);pr=sum(A.get(n,0)**2 for n in ns)-ap**2/pp
 check(name+':positive projection',pp>0 and pr>0)
 betab=(arb.pi()*C(pr)).sqrt()/(4*C(c));t=C(angle)
 def ev(cf,deriv=False):return sum((C(v)*n*(n*t).cos() if deriv else C(v)*(n*t).sin()) for n,v in cf.items())
 av,ad,pv,pd=ev(A),ev(A,True),ev(P),ev(P,True);norm=C(q*q)*pv*pv+pd*pd
 check(name+':positive point denominator',norm>0)
 phi=abs(C(q)*(av*pd-ad*pv))/(4*C(c)*norm.sqrt());g0=sum(n*v for n,v in th.items())
 check(name+':positive H and G lower',phi>0 and g0>0)
 prev=next(x for x in old if x['candidate']==name)
 check(name+':prior B enclosure',betab.overlaps(parse(prev['B'])))
 check(name+':prior Phi enclosure',phi.overlaps(parse(prev['Phi'])))
 check(name+':exact G',Q(prev['g0_exact'])==g0)
 item={'candidate':name,'B':enc(betab),'Phi':enc(phi),'g0_exact':str(g0),'targets':{}}
 for target,beta in p['betas'].items():
  rb=(betab/(C(beta)*C(alpha).sqrt()))**C(1/(-q-1));kc=C(D)*betab*rb**C(d)/((2*arb.pi()).sqrt()*C(g0));crit=kc/phi
  floor_at_beta=e0*(1-C(d/(k+d))*(rb/u)**C(k))
  check(name+target+':r_beta>5',rb>5)
  check(name+target+':r_beta<Rmax',rb<R)
  check(name+target+':critical upper',crit<C(p['critical_upper']))
  check(name+target+':direct strict obstruction',floor_at_beta>crit)
  check(name+target+':common strict obstruction',avg>crit)
  check(name+target+':tail integral target',((betab**2)*rb**C(-alpha)/C(alpha)).overlaps(C(beta)**2))
  item['targets'][target]={'beta_exact':str(beta),'r_beta':enc(rb),'Kcrit_over_Phi':enc(crit),'averaged_floor_at_beta':enc(floor_at_beta),'strict_gap_common':enc(avg-crit)}
 rows.append(item)
# Rebind the independent review without executing its source.
review=(B/'source/review.md').read_text()
log=(B/'source/peer_log.txt').read_text()
for name in ['original_PROOF.md','peer_check.py','peer_log.txt']:
 check('review hash '+name,sha(B/'source'/name) in review)
peerpasses=[x for x in log.splitlines() if x.startswith('PASS ')]
check('16 peer groups',len(peerpasses)==16 and 'ALL PASS (16 checks)' in log and not any(x.startswith('FAIL ') for x in log.splitlines()))
original=json.loads((B/'source/original_result.json').read_text())
check('original proof/result binding',original['proof_sha256']==sha(B/'source/original_PROOF.md'))
for key,value in [('Emin',e0),('ru',u),('common_averaged_floor',avg),('coarse_averaged_floor',coarse),('current_universal_averaged_floor',avgc),('T1_coarse_floor',cc)]:
 check('original '+key,value.overlaps(parse(original[key])))
peer=json.loads((B/'source/peer_inputs.json').read_text())
check('peer exact exponents',Q(peer['q'])==q and Q(peer['delta'])==d and Q(peer['D'])==D)
outer=json.loads((B/'source/outer_result.json').read_text())
outerrows={x['candidate']:x for x in outer['rows']}
check('outer proof/result binding',outer['proof_sha256']==sha(B/'source/outer_PROOF.md'))
for row in rows:
 name=row['candidate'];g0=Q(row['g0_exact'])
 pr=next(x for x in peer['rows'] if x['candidate']==name)
 check(name+': peer original angular data',parse(row['B']).overlaps(parse(pr['B'])) and parse(row['Phi']).overlaps(parse(pr['H_point'])) and g0==Q(pr['G_lower_exact']))
 rout=(lam*C(g0/D))**C(1/d)
 check(name+': outer switch reproduced',rout.overlaps(parse(outerrows[name]['fallback_switch'])))
 row['outer_switch']=enc(rout)
 for target,item in row['targets'].items():
  rb=parse(item['r_beta']);kc=parse(item['Kcrit_over_Phi'])
  ef=e0*(1-C(d/(k+d))*(rb/rout)**C(k))
  relaxed=C('793/1000')*(1-C(d/(k+d))*(rb/rout)**C(k))
  check(name+target+': outer switch beyond cutoff',rout>rb)
  check(name+target+': true floor > .79303648',ef>C('79303648/100000000'))
  check(name+target+': true floor strictly below Emin',ef<e0)
  check(name+target+': outer obstruction',ef>kc)
  check(name+target+': relaxed floor matches426',relaxed.overlaps(parse(outerrows[name]['targets'][target]['fallback_lower'])))
  item['outer_true_Emin_average']=enc(ef)
# The incident copy has three textual differences from the intact12:06 copy.
good=(B/'source/T2_review.md').read_text();bad=(B/'source/historical_incident_review.md').read_text()
recovered=bad.replace('written from --help','written from 2026-10-29T11:59Z').replace('it becomes the factor 0.672041641664145...','it becomes the factor 0.67204164...').replace('Last saved: 2026-10-29T12:12Z','Last saved: 2026-10-29T12:06Z')
check('historical incident relation',recovered==good)
(B/'verification/incident_review.diff').write_text(''.join(difflib.unified_diff(good.splitlines(True),bad.splitlines(True),fromfile='intact_1206',tofile='incident_1212')))
first=(B/'source/R1044_frozen.md').read_text();last=(B/'source/R1044_final.md').read_text()
reviewdiff=list(difflib.unified_diff(first.splitlines(True),last.splitlines(True),fromfile='R1044_1220',tofile='R1044_locked'))
check('R1044 revision inspected',sum(x.startswith(('+','-')) and not x.startswith(('+++','---')) for x in reviewdiff)==13)
(B/'verification/R1044_revision.diff').write_text(''.join(reviewdiff))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'lambda':enc(lam),'Emin':enc(e0),'ru':enc(u),'common_averaged_floor':enc(avg),'coarse_averaged_floor':enc(coarse),'current_universal_switching_radius':enc(uc),'current_universal_averaged_floor':enc(avgc),'T1_coarse_floor':enc(cc),'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'peer_pass_groups':16,'foreign_code_executed':False,'verdict':'CONFIRMED full425 analytic theorem through R1-045; outer-only extension independently verified; historical review provenance repaired'}
(B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(checks),result['utc'],result['elapsed_s'])
for key in ['Emin','ru','common_averaged_floor','coarse_averaged_floor','current_universal_averaged_floor']:print(key,result[key])
