"""Finite audit of two frozen publications. No candidate integrals or peer code."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import difflib,gzip,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
def req(name,ok,value=None):
 assert bool(ok),(name,str(value));checks.append({'claim':name,'value':None if value is None else str(value)})
m=read('data/manifest.json');req('proof before checker',m['proof_written_before_checker'])
for p,h in m['inputs'].items():req('binding '+p,sha(B/p)==h)
for p,key in [('data/initial_sources.json','files'),('data/accepted_sources.json','inputs')]:
 for r in read(p)[key]:req('accepted source '+r['local'],sha(B/r['local'])==r['sha256'])
pub=(B/'source/theory_v08.md').read_text();draft=(B/'source/THEORY_FINAL.md').read_text();pflat=' '.join(pub.split());dflat=' '.join(draft.split())
req('publication digest',sha(B/'source/theory_v08.md')=='a35184b753f57216c6b4bc01052317c508fe5439fda65b682b0cecb098be8bc9')
req('draft52 digest',sha(B/'source/THEORY_FINAL.md')=='82b4d9db1e5e25af3add32fedc87ae469191044735f2f749f4c80033c8f57451')
for tag,text,old,count in [('published',pub,'source/accepted_preview2.md',156),('draft52',draft,'source/accepted_draft43.md',72)]:
 changes=[{'tag':t,'old_start':a,'old_stop':z,'new_start':b,'new_stop':y} for t,a,z,b,y in difflib.SequenceMatcher(None,(B/old).read_text().split(),text.split(),autojunk=False).get_opcodes() if t!='equal']
 req(tag+' all changed blocks',changes==read('data/changes.json')[tag] and len(changes)==count)
for tag,n in [('brackets',166),('preview2',415),('draft43',263),('coverage',806),('supplement',257),('dyadic015',739),('WU3',320),('dyadic017',1070),('TB',199),('affine001',957),('forcing016',8874),('roundingWU3',364),('dual016',2099)]:
 j=read('source/'+tag+'_result.json');req(tag+' check count',j.get('check_count',j.get('checks_passed'))==n);req(tag+' proof link',j['proof_sha256']==sha(B/'source'/f'{tag}_PROOF.md'))
params=read('data/factor_parameters.json');factor_rows=[]
for r in params['table_rows']:
 rid=r['id'];lines=[s for s in pub.splitlines() if s.startswith('| '+rid+' |')];req(rid+' unique test row',len(lines)==1)
 cells=[s.strip() for s in lines[0].strip('|').split('|')];req(rid+' printed factor in cell',r['factor'] in cells)
 k=len(r['factor'].split('.')[1]);ratio=Q(r['p'])/Q(r['t']);req(rid+' downward factor',ratio//Q(1,10**k)*Q(1,10**k)==Q(r['factor']) and Q(r['factor'])>1)
 factor_rows.append({'id':rid,'ratio_exact':str(ratio),'printed_floor':r['factor']})
req('24 published factors',len(factor_rows)==24)
ceilings=list(map(Q,read('data/table_parameters.json')['ceilings']));table=[]
for line in draft.splitlines():
 if not line.startswith('| '):continue
 v=[s.strip() for s in line.strip('|').split('|')]
 if len(v)!=6 or not re.match(r'^(?:d2|Mpen2|0\d\d)$',v[0]) or v[2]=='-':continue
 floor=Q(v[1].split()[0]);ratios=[]
 for k,c in enumerate(ceilings):
  ratio=floor/c;req(v[0]+' distance factor '+str(k),ratio>Q(v[k+2])>1);ratios.append({'ratio_exact':str(ratio),'printed_lower':v[k+2]})
 table.append({'candidate':v[0],'strict_floor':str(floor),'ratios':ratios})
req('26 distance rows and78factors',len(table)==26)
req('23 inherited rows', [r for r in table if r['candidate'] not in ['002','003','004']]==read('source/draft43_result.json')['table'])
for rid,floor in [('002','1.56361352'),('003','0.22988134'),('004','1.40009623')]:
 req(rid+' accepted floor',next(r for r in table if r['candidate']==rid)['strict_floor']==str(Q(floor)))
bp=read('data/bracket_parameters.json');squares=[]
for r in bp['rows']:
 mu,C,cu,w=map(Q,[r['mu'],r['C'],r['cU'],r['sqrtW2']]);sq=4*mu**3/(27*C*cu**2*w**2);upper=Q(bp['rebal_corrected_upper'] if r['name']=='TB-rebal' else r['printed'])
 req(r['name']+' positive ceiling square',sq>0);req(r['name']+' outward upper',sq<upper**2);req(r['name']+' common upper',sq<Q('3.7930e-6')**2)
 req(r['name']+' accepted square',sq==Q(next(z for z in read('source/brackets_result.json')['rows'] if z['name']==r['name'])['supremum_square_exact']));squares.append({'name':r['name'],'square':str(sq)})
mu,C,cu,s,r,w=Q(297,1000),Q(402),Q(8,5),Q(1,4096),Q(1536,1000000),Q(512)
rate=mu-C*s-cu*r*64;req('counterexample positive high margin',rate>0);req('counterexample radius exactly3e-6',r/w==Q('3e-6'));req('counterexample exceeds stale cap',r/w>Q('2.7e-6'))
gsq=Q(2500,651**2*28248);req('graded exact square',gsq==Q(625,2992882662));req('graded upper and1/2000',gsq<Q(25,54684)**2<Q(1,2000)**2)
coverage=read('source/coverage_result.json')['weak_candidates'];req('24 candidate coverage',len(coverage)==24 and {z['number'] for z in coverage}==set(range(2,27))-{11})
for z in coverage:
 I,D,H=map(Q,[z['I_lower_exact'],z['D_upper_exact'],z['H_upper_exact']]);gap=I-D/1000-H/1000000
 req(str(z['number'])+' strict common1/1000 gap',gap>0 and gap==Q(z['positive_gap_exact']))
req('all-weight originalfloorbL ceiling below1/1000',Q('4.1069e-6')<Q(1,1000))
for z in read('source/roundingWU3_result.json')['rows']:
 lo,hi=Q(z['sqrt_supremum_strict_outer_lower']),Q(z['sqrt_supremum_strict_outer_upper']);disp=Q(z['six_digit_rounded_display']);unit=Q(1,10**11)
 req(z['label']+' six-significant-figure rounding',disp-unit/2<lo<hi<disp+unit/2)
 req(z['label']+' positive rational witness',Q(z['exact_f_at_test_mu'])>0)
supp=next(z for z in read('source/supplement_result.json')['rows'] if z['candidate']=='017' and z['n']==21 and z['K']==522)
req('017 diagnostic accepted strict floor',Q(supp['strict_sharp_floor'])>=Q('0.000596123050327423'))
dual=read('source/dual016_result.json');elo=Q(dual['E2_strict_lower_exact']);ehi=Q(dual['007_E2_strict_upper_exact'])
req('actual identicalE2 strict gap',elo-ehi>=Q('1.572166921614'))
req('dualH accepted printed floor',Q(dual['H_strict_lower_exact'])==Q('0.529469576110512066428681'))
req('retains runtime pairing premise',dual['candidate_pairing_integrals_repeated'] is False and dual['coarse_group_sum_is_a_pairing_reproduction'] is False)
app=read('data/appendix_bindings.json')['rows'];hist=read('data/historical_bindings.json')['rows'];req('139 hash claims',len(app)==139)
req('134 same-time full matches',sum(z['status']=='MATCH' for z in app)==134)
for z in app:
 req('appendix hash syntax '+z['path'],bool(re.fullmatch('[0-9a-f]{64}',z['sha256_claimed'])))
 if z['status']=='MATCH':req('appendix full-match receipt '+z['path'],z['sha256_claimed']==z['sha256_current'])
 else:
  h=next(h for h in hist if h['path']==z['path']);raw=gzip.decompress((B/h['local_gzip']).read_bytes());req('exact historical object '+z['path'],hashlib.sha256(raw).hexdigest()==z['sha256_claimed'] and len(raw)==h['prefix_bytes'])
idx=(B/'source/snapshot_INDEX.md').read_text();line=next(s for s in idx.splitlines() if s.startswith('C1-N1-028-'))
req('028 registered beforepublication', '2026-10-29T15:24:01Z' in line and '2026-10-29T15:25:44Z' in (B/'source/numerics_v15.md').read_text())
req('v08 cites indexalreadyincluding028',sha(B/'source/snapshot_INDEX.md')==next(z['sha256_claimed'] for z in app if z['path'].endswith('candidate_snapshots/INDEX.md')))
for literal in ['below 2.7e-6','only as framework inapplicability','028 is a reserved ID without a registered snapshot','No exclusion is a nonexistence statement: each concerns the fixed c and the stated balls']:
 req('record exact publication defect '+literal,literal in pflat)
req('record stale017 diagnostic', 'N4-259 (017 bound at (21, 522), OPEN)' in dflat)
for p,h in m['inputs'].items():req('inputs unchanged '+p,sha(B/p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'publication_sha256':sha(B/'source/theory_v08.md'),'draft52_sha256':sha(B/'source/THEORY_FINAL.md'),'factor_rows':factor_rows,'distance_rows':table,'family_squares':squares,'counterexample_high_margin_exact':str(rate),'counterexample_L2_radius_exact':str(r/w),'appendix_full_matches':134,'appendix_exact_historical_recoveries':5,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'candidate_integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED finite mathematics and coverage; REFUTED specified stale cap and literal scope/status claims; no existence closure'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['utc'],out['elapsed_seconds'])
