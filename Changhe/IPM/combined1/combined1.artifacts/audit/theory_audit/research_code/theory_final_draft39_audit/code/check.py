"""Independent finite draft audit, with accepted analytic and integral dependencies."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import difflib,hashlib,json,re,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads((B/p).read_text());checks=[]
def req(name,test,value=None):
 assert bool(test),(name,str(value));checks.append({'claim':name,'value':None if value is None else str(value)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
m=read('data/manifest.json');req('proof first',m['proof_written_before_checker'])
for p,h in m['inputs'].items():req('binding '+p,sha(B/p)==h)
for f in ['data/input_sources.json','data/additional_sources.json']:
 for z in read(f)['inputs']:req('copied '+z['local'],sha(B/z['local'])==z['sha256'])
text=(B/'source/THEORY_FINAL.md').read_text();old=(B/'source/accepted_draft38.md').read_text();normal=' '.join(text.split())
req('actual frozen draft39',sha(B/'source/THEORY_FINAL.md')=='28f5f6ce4bd47463335e8b76b07bdfb53a1c6445bd9e1f0552a81dbb1ae5b97b' and len(text.splitlines())==1897)
changes=[z for z in difflib.SequenceMatcher(None,old.split(),text.split(),autojunk=False).get_opcodes() if z[0]!='equal']
req('all88changes',len(changes)==88);req('complete352-line comparison',len((B/'source/word_changes.txt').read_text().splitlines())==352)
prior=read('source/draft38_result.json');reach=read('source/reach_result.json');fix=read('source/repairs_result.json');forcing=read('source/forcing_result.json')
for label,j,proof,n in [('draft38',prior,'draft38_PROOF.md',548),('reach',reach,'reach_PROOF.md',948),('repairs',fix,'repairs_PROOF.md',107),('forcing',forcing,'forcing_PROOF.md',318)]:
 req(label+' accepted count',j['check_count']==n)
 req(label+' proof dependency',j['proof_sha256']==sha(B/'source'/proof))
req('N4forcing linkage',forcing['peer_sha256']==sha(B/'source/N4_forcing_result.json'))
p=read('data/parameters.json');ceilings=list(map(Q,p['ceilings']));table=[]
for line in text.splitlines():
 if not line.startswith('| '):continue
 v=[a.strip() for a in line.strip('|').split('|')]
 if len(v)!=6 or not re.match(r'^(?:d2|Mpen2|0\d\d)$',v[0]) or v[2]=='-':continue
 floor=Q(v[1].split()[0]);ratios=[]
 for k,ceiling in enumerate(ceilings):
  ratio=floor/ceiling;req(v[0]+' exact table factor '+str(k),ratio>Q(v[k+2]),ratio)
  ratios.append({'ratio_exact':str(ratio),'printed_lower':v[k+2]})
 table.append({'candidate':v[0],'strict_floor':str(floor),'ratios':ratios})
req('22table rows',len(table)==22)
x={k:Q(v) for k,v in p['sharpw'].items()};rate=x['mu']-x['C']*x['s']-x['cU']*x['r']*72
req('exact high rate',rate==Q(63092119,405000000));req('conservative rate',rate>Q('0.1557'));req('inverse rate',1/rate<Q('6.4226'))
req('self-map slack',x['r']-x['eta']/Q('0.1557')==Q(7,1557000000));req('exact-rate self map',x['r']-x['eta']/rate>0)
contract=ar(x['r']/x['betaL'])/(2*(arb.pi()*ar(x['s']*(1+x['s']))).sqrt());req('contraction',contract<ar('0.0137200'),contract)
ceiling=(2*ar(x['mu'])/3)*(ar(x['mu']/(3*x['C']))).sqrt()/(ar(x['cU'])*ar(x['w2']).sqrt());req('sharpw ceiling',ceiling<ar('0.0000028496'),ceiling)
small=[]
for name,floor in [('007','0.004769166867'),('013','0.00199234339'),('014','0.00198301351067')]:
 for radius in [Q(1,2**25),Q('6.8626e-8')]:
  ratio=Q(floor)/radius;req(name+' Db factor '+str(radius),ratio>28895,ratio);small.append({'candidate':name,'radius_exact':str(radius),'ratio_exact':str(ratio)})
newrows=[]
for name,floor,printed in [('025','0.002065801265578052',['544.6','724.9','4.518']),('026','0.001355907204057457',['357.4','475.8','2.965'])]:
 j=read('source/'+name+'_weak_result.json');req(name+' strict floor',Q(j['strict_lower_exact'])==Q(floor))
 req(name+' complete gradient check',j['gradient_certificate']['complete_critical_point_check'])
 req(name+' all final comparisons',all(j['comparisons'].values()))
 ratios=[]
 for k,ceiling in enumerate(ceilings):
  ratio=Q(floor)/ceiling;req(name+' full bound factor '+str(k),ratio>Q(printed[k]),ratio);ratios.append(str(ratio))
 newrows.append({'candidate':name,'floor':floor,'ratios_exact':ratios,'rounded_lower_factors':printed})
point=read('source/026_point_result.json');origin=read('source/026_origin_result.json');shapes=read('source/026_shapes_result.json')
req('026 point positive',arb(point['uniform_graded_gap'])>0 and all(arb(z['gap'])>0 for z in point['ball_exclusions']))
req('026 origin exact',origin['c_plus_strain']=='1' and origin['a0_positive'])
req('026 rank and objective',shapes['potential_dimension']==shapes['density_dimension']==2414 and len(shapes['exact_objective_rows'])==81 and len(shapes['outside_analytic_span'])==46)
c=Q(4076476460239181,2251799813685248);q=1/c-4;d=1-1/c;k=1-q;D=5*c-1;alpha=-2*q-2;Emin=(-q-1)/(2*(-q)*(-q-3));lam=arb(1)/2+5*arb(2)**ar(1-q)
req('exact Emin',Emin==Q(reach['Emin_exact']));req('corrected lambda',lam>ar('109.6024') and lam.overlaps(arb(prior['lambda'])),lam)
req('large radius remainder',lam*(arb(5)/18860)**ar(d)>ar('2.74'))
req('small radius remainder',lam>ar('2.74'))
proj=arb(prior['N1_projection']);req('corrected projection',ar('13.75867597')<proj<ar('13.758676'))
S=ar(2*d*d/(alpha*(alpha+d)*(alpha+2*d)));beta=50/(arb(651)*arb(28248).sqrt());endpoint=[]
for r in reach['rows']:
 name=r['candidate'];bb=arb(r['B']);g0=ar(r['g0_exact']);v0=ar(r['v0_exact']);Phi=arb(r['Phi']);H0=arb(r['H0'])
 def cap(E,H,V):
  r0=((2*arb.pi()).sqrt()*H*(V+g0*E)/(ar(D)*bb))**ar(1/d)
  return bb*r0**ar(q+1)*S.sqrt()
 def avg(Ef,M):
  u=5*(lam/Ef)**ar(1/d)
  if ar(M)<u:return Ef*(1-ar(d/(k+d))*(ar(M)/u)**ar(k))
  return lam*(5/ar(M))**ar(d)*ar(k/(k+d))
 row={'candidate':name,'caps':{}}
 for key,Ef,H,V,M,upper in [('Emin_H0',ar(Emin),H0,arb(0),114000,'1.43912e-7'),('Emin_Phi_v0',ar(Emin),Phi,v0,122000,'1.14141e-7'),('current_H0',ar('1.747261'),H0,arb(0),108000,'2.66323e-8')]:
  value=(cap(avg(Ef,M),H,V)**2+bb**2*ar(M)**ar(2*q+2)/ar(alpha)).sqrt()
  req(name+' independent split cap '+key,value<ar(upper) and value.overlaps(arb(r['reach'][key]['bound'])),value);row['caps'][key]=value.str(90)
 def critical(beta,H,V):return ar(D)*bb/((2*arb.pi()).sqrt()*H*g0)*(bb*S.sqrt()/beta)**ar(d/(-q-1))-V/g0
 for rad,lower in [(Q(1,2**25),'1.020385'),(Q('6.8626e-8'),'0.8711127')]:
  t=critical(ar(rad),Phi,v0);req(name+' open Db numerical necessary threshold '+str(rad),t>ar(lower)>ar(Emin))
 req(name+' trans under V',critical(ar(Q(1,2**23)),Phi,v0)<ar(Emin))
 req(name+' first large target',critical(ar('3.5125e-7'),H0,arb(0))<ar(Emin))
 t=lambda bt:ar(D)*(bb/(bt*ar(alpha).sqrt()))**ar(d/(-q-1))/g0
 req(name+' printed normalized threshold',t(ar(Q(25,54684)))<ar('7.9417'))
 req(name+' exact graded normalized threshold',t(beta)>ar('7.942167'))
 req(name+' unnormalized exact graded bound',t(beta)*bb/((2*arb.pi()).sqrt()*999745)<ar('0.2694533'))
 req(name+' independent current shape',cap(ar('1.747261'),H0,arb(0))<ar('1.89061e-9'))
 req(name+' independent current crude',cap(ar('1.747261'),H0,arb(0))/(S*ar(alpha)).sqrt()<ar('1.66122e-8'))
 endpoint.append(row)
req('007 published forcing factor',Q('756.5312630768')/Q('2.1035e-4')>Q('3596535.57'))
for literal in ['c[h] = 0','if K = 0 the majorant is linear','No exact solution near any candidate has been shown to exist.','Etest is a lower bound on valid constants, not a proved admissible one','all exponents well above delta','a failed sufficient condition','original graded box; the FW-T-DYADIC-Y-v1 list above is separate']:
 req('retained scope '+literal,literal in normal)
for p,h in m['inputs'].items():req('unchanged '+p,sha(B/p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'word_change_blocks':len(changes),'table_rows':len(table),'table':table,'small_Db_ratios':small,'new_candidate_ratios':newrows,'endpoint':endpoint,'lambda':lam.str(90),'projection':proj.str(90),'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'source_sha256':sha(B/'source/THEORY_FINAL.md'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED changed conditional mathematics and22table rows; REFUTED current026-OPEN status by446-450; three publication updates and scope clarifications in the proof; no inverse or existence closure'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',len(table),'table rows',out['utc'],out['elapsed_seconds'])
