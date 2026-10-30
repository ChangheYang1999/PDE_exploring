"""Independent finite decimal and phase audit. No quadrature is certified."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
def exactdata(n):return json.loads((B/'source'/n).read_text(),parse_float=Q)
def rounding(q,literal):
 a,*ee=literal.lower().split('e');e=int(ee[0]) if ee else 0;places=len(a.split('.')[1]) if '.' in a else 0;unit=Q(10)**(e-places);return 2*abs(q-Q(literal))<=unit
for x in read('data/manifest.json'):need('binding '+x['local'],sha(B/x['local'])==x['sha256'])
p=read('data/parameters.json');j=read('source/N4_result.json');need('626 source checks pass',j['check_count']==len(j['checks'])==626 and all(j['checks'].values()) and j['display_failures']==[]);need('own proof first',not read('data/PROOF_FIRST.json')['checker_exists']);ast.parse((B/'source/N4_check.py').read_text())
special={'PROOF.md':'source/N4_PROOF.md','ERRATA_v02.md':'source/N4_ERRATA.md','source/MANIFEST.json':'source/N4_manifest.json','source/PROOF_FIRST_v02.json':'source/N4_proof_first_v02.json','code/check_v02.py':'source/N4_check.py','source/023_s12_exact.json':'../candidate023_shapes/data/phase1.json'}
for path,digest in j['bindings'].items():
 rel=path.split('research/numerics_final_literal_audit/',1)[1];local=special.get(rel,rel);need('all N4 input '+rel,sha(B/local)==digest)
report=(B/'source/report.md').read_text().splitlines();reg=[(n,k) for n in p['register_n'] for k in p['register_K']];need('25 register',len(reg)==25)
data={n:exactdata(n+'_weaktests3.json') for n in ['016','022','023','024','025','026','027','028','023_s12']}
def val(n,p):return Q(data[n]['probes'][f'{p[0]}:{p[1]}']['m_lower_bound'])
peer={(r['comparison'],tuple(r['probe'])):r for r in j['probe_rows']};need('200 unique peer rows',len(peer)==len(j['probe_rows'])==200)
pat=re.compile(r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)');rows=[];counts={};display_count=0
for line,new,old,offset in p['blocks']:
 group=pat.findall(report[line-1]);need('complete line '+str(line)+' '+str(offset),len(group)==(50 if line in [210,212] else25));group=group[offset:offset+25];need('ordered register '+new+'/'+old,[(int(n),int(k)) for n,k,*_ in group]==reg)
 ratios=[]
 for n,k,od,nd,fd in group:
  probe=(int(n),int(k));a,b=val(old,probe),val(new,probe);name=new+'/'+old;need('positive inputs '+name+' '+n+':'+k,a>0 and b>0);q=b/a;row=peer[name,probe]
  need('same exact operands '+name+' '+n+':'+k,a==Q(row['old_exact']) and b==Q(row['new_exact']) and q==Q(row['ratio_exact']))
  need('same displayed literals '+name+' '+n+':'+k,{'old':od,'new':nd,'factor':fd}==row['display'])
  for field,value,literal in [('old',a,od),('new',b,nd),('factor',q,fd)]:need('rounding '+name+' '+n+':'+k+' '+field,rounding(value,literal));display_count+=1
  ratios.append(q);rows.append({'comparison':name,'probe':list(probe),'ratio_exact':str(q)})
 cc={'count':len(ratios),'decreased':sum(q<1 for q in ratios),'equal':sum(q==1 for q in ratios),'increased':sum(q>1 for q in ratios),'min_ratio_exact':str(min(ratios)),'max_ratio_exact':str(max(ratios))};need('complete counts '+new+'/'+old,cc==j['comparison_counts'][new+'/'+old]);counts[new+'/'+old]=cc
need('exactly600 displays',display_count==600 and len(rows)==200)
first={n:exactdata(n+'_weaktests2.json') for n in ['007','013']};need('common first-mode rule',first['007']['rule']==first['013']['rule']);need('common full source register',list(first['007']['NORM-T-WEAK-v1_a0'])==list(first['013']['NORM-T-WEAK-v1_a0']));fr={}
for k,x in first['007']['NORM-T-WEAK-v1_a0'].items():
 if int(k)<=128:
  a=abs(Q(x['I_k']));b=abs(Q(first['013']['NORM-T-WEAK-v1_a0'][k]['I_k']));need('first source positive '+k,a>0 and b>0);fr[int(k)]=a/b
need('all first-mode values match',[{'k':n,'q':str(q)} for n,q in fr.items()]==[{'k':x['k'],'q':x['improvement_exact']} for x in j['first_mode_rows_k_le128']])
need('full register extrema indices',min(fr,key=fr.get)==128 and max(fr,key=fr.get)==12)
for key,value in [('first_min',fr[128]),('first_max',fr[12])]:q,l,u=map(Q,p[key]);need(key+' exact identity and bounds',value==q and l<q<u)
need('universal thousandfold saved claim false',fr[128]<1000 and 'are three orders of magnitude below' in report[15]);need('selected range phrase', 'factors 27 (k = 128)' in report[179])
need('raw phase1 identity',data['023_s12']['sha256']==sha(B/'../candidate023_shapes/data/phase1.json')=='637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb')
need('raw final identity',data['023']['sha256']==sha(B/'../candidate023_shapes/data/candidate023.json')=='d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df')
a=val('023_s12',(19,600))/val('016',(19,600));b=val('023',(19,600))/val('016',(19,600))
need('12step exact witness',a==Q(363131360839284770,8175262909452811) and Q('44.4183')<a<Q('44.4184'))
need('final exact witness',b==Q(213918009600561160,8175262909452811) and Q('26.1664')<b<Q('26.1666'))
need('phase label refuted for displayed witness',rounding(b,'26.2') and not rounding(a,'26.2') and '023 (016 + scale 100, 12 steps)' in report[205])
pr={probe:val('023',probe)/val('023_s12',probe) for probe in reg};need('all25phase ratios match',[{'probe':list(probe),'ratio_exact':str(q)} for probe,q in pr.items()]==[{'probe':x['probe'],'ratio_exact':x['ratio_exact']} for x in j['phase_final_over12_rows']])
need('phase extrema indices',min(pr,key=pr.get)==(23,900) and max(pr,key=pr.get)==(29,1200))
for key,value in [('phase_min',pr[23,900]),('phase_max',pr[29,1200])]:q,l,u=map(Q,p[key]);need(key+' exact identity and bounds',value==q and l<q<u)
need('phase universal range refuted',pr[23,900]<Q('.94') and pr[29,1200]>Q('1.04') and 'registered probes at phase-2/phase-1 ratios 0.94 to 1.04' in report[205])
for name,d in first.items():need(name+' explicit unbounded diagnostic','FLOAT (not bounds)' in d['label'] and 'finite asymptotic far correction' in d['label'])
need('exact far report claim needs qualification','add an exact far part from the surviving sectors' in report[243])
prior=read('../candidate024_shapes/verification/result.json');need('024 accepted hash distinction',prior['current_heldout_sha256']=='e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab' and prior['reconstructed_sha256']=='58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5')
need('024 internal attribution conflict',"current file's hash is e171c051..., recorded in my 09:13Z WORKLOG" in report[206] and 'hash cited there is the pre-typo-fix text' in report[213])
need('all six findings present',len(j['issues'])==6 and sum(x['verdict']=='REFUTED' for x in j['issues'])==5 and sum(x['verdict']=='OPEN' for x in j['issues'])==1)
for x in read('data/manifest.json'):need('unchanged '+x['local'],sha(B/x['local'])==x['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'display_count':display_count,'probe_rows':rows,'comparison_counts':counts,'first_mode_ratios_exact':{str(k):str(v) for k,v in fr.items()},'phase_final_over12_exact':{f'{n}:{k}':str(v) for (n,k),v in pr.items()},'first_mode_extrema_exact':{'minimum':str(fr[128]),'maximum':str(fr[12])},'phase_extrema_exact':{'minimum':str(pr[23,900]),'maximum':str(pr[29,1200])},'PDE_or_quadrature_bounds_asserted':False,'unobserved_write_times_asserted':False,'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED N4-420 finite arithmetic and six source-scope findings. Five literal saved-data/text claims REFUTED; complete exact far-part claim OPEN. No candidate verdict changes.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],len(checks),'checks',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
