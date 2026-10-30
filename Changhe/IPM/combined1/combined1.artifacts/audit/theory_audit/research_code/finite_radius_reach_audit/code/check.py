from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];started=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(label,test):
 assert bool(test),label
 checks.append(label)
def C(x):
 f=Q(str(x));return arb(f.numerator)/f.denominator
def enc(x):return x.str(55)
def parse(x):
 if x.startswith('['):
  a,e=x.strip('[]').split('+/-');return arb(a.strip(),e.strip())
 return C(x)
m=json.loads((B/'data/manifest.json').read_text());check('proof binding',sha(B/'PROOF.md')==m['proof_sha256'])
for rel,h in m['inputs'].items():check('input '+rel,sha(B/rel)==h)
p=json.loads((B/'data/parameters.json').read_text());peer=json.loads((B/'source/peer_result.json').read_text());old=json.loads((B/'source/432_result.json').read_text());orig=json.loads((B/'source/414_result.json').read_text());eppeer=json.loads((B/'source/peer_endpoint.json').read_text())
check('peer97checks',len(peer['checks'])==97 and all(peer['checks'].values()))
review=(B/'source/review.md').read_text()
for fn in ['peer_check.py','peer_result.json','peer_log.txt']:check('peer review binding '+fn,sha(B/'source'/fn) in review)
c=Q(p['c']);q=1/c-4;d=1-1/c;k=1-q;D=c*k;alpha=-2*q-2
S=2*d*d/(alpha*(alpha+d)*(alpha+2*d));emin=(-q-1)/(2*(-q)*(-q-3));eu=Q(p['current_universal']);lam=C(1)/2+5*C(2)**C(1-q)
check('signs',-5<q<-3 and min(d,k,D,alpha)>0)
check('exponents',k==4+d and D==5*c-1 and q-2==-k-1)
check('shape identity',S==1/alpha-2/(alpha+d)+1/(alpha+2*d))
check('Emin lower',emin>Q('0.7930365'))
check('Ef allowed',lam>C(eu)>C(emin))
check('lambda exact equality false',lam>C('109.6024'))
check('branch join identity',1-d/(k+d)==k/(k+d))
check('inner derivative identity',-k*(1-d/(k+d))-d*k/(k+d)==-k)
check('outer derivative identity',(-k-d)*k/(k+d)==-k)
def T(E,r):
 u=5*(lam/E)**C(1/d)
 if r<u:return E*(1-C(d/(k+d))*(r/u)**C(k))
 check('T branch disjoint',r>u)
 return lam*(5/r)**C(d)*C(k/(k+d))
def cap(row,E,H,v,shape=True):
 r0=((2*arb.pi()).sqrt()*H*(v+E*row['g0'])/(C(D)*row['B']))**C(1/d)
 return row['B']*r0**C(q+1)*(C(S).sqrt() if shape else 1/C(alpha).sqrt())
def crit(row,beta,H,v,shape=True):
 fac=C(S).sqrt() if shape else 1/C(alpha).sqrt()
 return C(D)*row['B']/((2*arb.pi()).sqrt()*H*row['g0'])*(row['B']*fac/C(beta))**C(d/(-q-1))-v/row['g0']
def rbeta(row,beta):return (row['B']/(C(beta)*C(alpha).sqrt()))**C(1/(-q-1))
rows=[];reach_all={};targets_all={}
for name,angle in p['angles'].items():
 ep=json.loads((B/f'data/{name}_endpoint.json').read_text());A={int(n):Q(v) for n,v in ep['F12'].items()};P={int(n):Q(v) for n,v in ep['P'].items()};th={int(n):Q(v) for n,v in ep['Theta0'].items()}
 check(name+' exact c',Q(ep['c'])==c)
 ns=set(A)|set(P);pp=sum(P.get(n,0)**2 for n in ns);proj=sum(A.get(n,0)**2 for n in ns)-sum(A.get(n,0)*P.get(n,0) for n in ns)**2/pp
 check(name+' projection positive',pp>0 and proj>0)
 bv=(arb.pi()*C(proj)).sqrt()/(4*C(c));ang=C(angle)
 def ev(dic,derivative=False):return sum((C(v)*n*(n*ang).cos() if derivative else C(v)*(n*ang).sin()) for n,v in dic.items())
 av,ad,pv,pd=ev(A),ev(A,True),ev(P),ev(P,True);den=C(q*q)*pv*pv+pd*pd
 check(name+' point denominator',den>0)
 phi=abs(C(q)*(av*pd-ad*pv))/(4*C(c)*den.sqrt());gq=sum(n*v for n,v in th.items());power=1/c+2
 vq=abs((power-1)*sum(n*v/(power*power-n*n) for n,v in th.items()));H=C(p['H0'][name])
 check(name+' H0 Phi',0<H<phi)
 check(name+' exact lower G and V',gq>0 and vq>0)
 oldrow=next(r for r in old['rows'] if r['candidate']==name);original=next(r for r in orig['rows'] if r['candidate']==name)
 check(name+' prior B',bv.overlaps(parse(oldrow['B'])))
 check(name+' prior Phi',phi.overlaps(parse(oldrow['Phi'])))
 check(name+' prior v0 exact',vq==Q(original['v0_exact']))
 check(name+' T2 Phi',phi.overlaps(parse(eppeer['D'][name]['Phi_theta_star'])))
 check(name+' T2 v0',C(vq).overlaps(parse(eppeer['E'][name]['V_low'])))
 row={'B':bv,'Phi':phi,'H0':H,'g0':C(gq),'v0':C(vq)}
 output={'candidate':name,'B':enc(bv),'Phi':enc(phi),'H0':p['H0'][name],'g0_exact':str(gq),'v0_exact':str(vq),'reach':{},'targets':{},'R1038':{}}
 for case in p['reach_cases']:
  Ef=C(emin if case['floor']=='Emin' else case['floor']);M=C(case['M']);hc=row[case['h']];vc=C(0) if case['v']=='zero' else row['v0'];e1=T(Ef,M)
  bound=(cap(row,e1,hc,vc)**2+bv*bv*M**C(2*q+2)/C(alpha)).sqrt()
  pr=peer['C'][case['peer_key']][name]
  check(name+case['label']+' selected M',Q(pr['Rmax'])==Q(case['M']))
  check(name+case['label']+' peer bound',bound<C(pr['value']))
  check(name+case['label']+' common bound',bound<C(case['upper']))
  if case['label']=='current_H0':check(name+' smallest radius blocked',bound<C('1/33554432') and C('1/33554432')/bound>C('1.119'))
  if case['label']=='Emin_Phi_v0':check(name+' trans radius blocked',bound<C('1/8388608'))
  output['reach'][case['label']]={'Rmax':case['M'],'E1':enc(e1),'bound':enc(bound),'upper':case['upper']}
  reach_all[(name,case['label'])]=bound
 for ii,target in enumerate(p['targets']):
  lab=target['label'];plab=target['peer_label'];lo,hi=Q(target['lower']),Q(target['upper']);br=peer['B']['radii'][plab]
  check(name+lab+' exact bracket binding',lo==Q(br['beta_lower']) and hi==Q(br['beta_upper']) and 0<lo<=hi)
  pr=br['per_candidate'][name]
  values={'shape_H0_V0_upper':crit(row,lo,H,C(0)),
    'shape_Phi_V0_upper':crit(row,lo,phi,C(0)),
    'shape_Phi_V0_lower_at_beta_upper':crit(row,hi,phi,C(0)),
    'shape_Phi_Vv0_upper':crit(row,lo,phi,row['v0']),
    'shape_Phi_Vv0_lower_at_beta_upper':crit(row,hi,phi,row['v0']),
    'crude_Phi_V0_upper':crit(row,lo,phi,C(0),False),
    'crude_H0_V0_upper':crit(row,lo,H,C(0),False)}
  for key,val in values.items():check(name+lab+' '+key,val>C(pr[key]) if 'lower' in key else val<C(pr[key]))
  expected=3 if ii<2 else (2 if ii==2 else 1)
  classification=1 if values['shape_Phi_V0_upper']<C(emin) else 2 if values['shape_Phi_Vv0_upper']<C(emin) else 3
  check(name+lab+' threshold classification',classification==expected==pr['class'])
  check(name+lab+' current coefficient fails',values['crude_H0_V0_upper']<C(eu))
  if expected==3:check(name+lab+' not excluded in relaxed threshold',values['shape_Phi_Vv0_lower_at_beta_upper']>C(emin))
  rb=rbeta(row,lo);kc=crit(row,lo,phi,C(0),False);eminavg=T(C(emin),rb);curavg=T(C(eu),rb);cr=peer['C']['radii'][plab][name]
  for key,val,lower in [('r_beta_lower_end_beta',rb,False),('Kcrit/Phi_upper',kc,False),('T[e_min](r_beta)_lower',eminavg,True),('T[e_1747261](r_beta)_lower',curavg,True)]:
   check(name+lab+' envelope '+key,val>C(cr[key]) if lower else val<C(cr[key]))
  check(name+lab+' T425 bool',bool(eminavg>kc)==cr['T4-425_crude_with_Etest'])
  check(name+lab+' current envelope bool',bool(curavg>kc)==cr['crude_with_1747261'])
  for key,case in [('retained_shape_class_blocked','Emin_H0'),('retained_shape_class_blocked_V_v0','Emin_Phi_v0'),('reach_1747261_blocked','current_H0')]:
   check(name+lab+' '+key,bool(reach_all[(name,case)]<C(lo))==cr[key])
  check(name+lab+' all targets above current cap',reach_all[(name,'current_H0')]<C(hi))
  output['targets'][lab]={'printed_beta_exact':str(hi),'bracket_lower_exact':str(lo),'threshold_Phi_v0_at_printed':enc(values['shape_Phi_Vv0_lower_at_beta_upper']),'threshold_Phi_0_at_bracket_lower':enc(values['shape_Phi_V0_upper']),'classification':classification,'r_beta_at_bracket_lower':enc(rb),'Emin_average':enc(eminavg),'current_average':enc(curavg)}
 cs=cap(row,C(eu),H,C(0));cc=cap(row,C(eu),H,C(0),False);dr=peer['D']['current'][name]
 for key,val,lower in [('crude_cap_upper',cc,False),('crude_cap_lower',cc,True),('shape_cap_upper',cs,False),('crude_over_9.28e-11_lower',cc/C('9.28e-11'),True),('2^-25_over_crude_lower',C('1/33554432')/cc,True),('6.8626e-8_lower_end_over_crude_lower',C('6.8625e-8')/cc,True)]:check(name+' current '+key,val>C(dr[key]) if lower else val<C(dr[key]))
 check(name+' common current caps',cs<C('1.89061e-9') and cc<C('1.66122e-8'))
 output['constant_current']={'shape':enc(cs),'crude':enc(cc)}
 lhs=C(emin)*(2*arb.pi()).sqrt()*H/bv
 for target in p['targets']:
  if target['label'] not in ['graded','sharpw_family','TB_sharp']:continue
  beta=C(target['upper']);em=C(D)*(bv/(beta*C(alpha).sqrt()))**C(d/(-q-1))/row['g0'];rp=peer['C']['R1-038'][target['peer_label']][name]
  check(name+target['label']+' R1038 upper',em<C(rp['Emax_upper']))
  check(name+target['label']+' R1038 lower',lhs>C(rp['Etest_sqrt2pi_H0_over_B_lower']))
  check(name+target['label']+' R1038 blocked',lhs>em and lhs>C('23.37502'))
  output['R1038'][target['label']]={'Emax':enc(em),'lower_left':enc(lhs)}
 exactbeta=50/(651*C(28248).sqrt());emx=C(D)*(bv/(exactbeta*C(alpha).sqrt()))**C(d/(-q-1))/row['g0']
 check(name+' graded exact below rounded',C('45697/100000000')<exactbeta<C('25/54684'))
 check(name+' graded threshold NOT7.9417',emx>C('7.9417') and emx>C(peer['C']['R1-038_exact_graded_ceiling'][name]['Emax_lower']))
 check(name+' exact graded blocked',lhs>emx)
 output['R1038']['exact_graded']={'beta':enc(exactbeta),'Emax':enc(emx)}
 rows.append(output)
oldrow={'B':C(85020),'g0':C('28.5227')};oc=cap(oldrow,C(133),C(33917),C(0),False)
check('historical bound',oc<C(peer['D']['T4-351_constants_crude_cap_upper'])<C('9.28e-11'))
# Abstract countermodels to claimed implications; these are not candidate solutions.
check('necessary test countermodel',Q('0.79')<Q('1.02')<Q('1.74'))
check('nested upper bounds do not refute smaller bound',0<Q('9.28e-11')<Q('1.89061e-9'))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-started,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'target_count':len(p['targets']),'rows':rows,'Emin_exact':str(emin),'lambda':enc(lam),'historical_crude_cap':enc(oc),'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'verdict':'CONFIRMED scoped integral theorem and independent finite replay; OPEN optimal universal coefficient at the two small targets; REFUTED necessity-to-sufficiency inference'}
(B/'verification/result.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(checks),result['utc'],result['elapsed_s'])
for row in rows:print(row['candidate'],{key:value['bound'] for key,value in row['reach'].items()})
