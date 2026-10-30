"""Finite independent checks of the frozen draft43 delta; no integral replay."""
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
m=read('data/manifest.json');req('proof written first',m['proof_written_before_checker'])
for p,h in m['inputs'].items():req('binding '+p,sha(B/p)==h)
for f in ['data/input_sources.json','data/additional_sources.json']:
 for z in read(f)['inputs']:req('frozen copy '+z['local'],sha(B/z['local'])==z['sha256'])
text=(B/'source/THEORY_FINAL.md').read_text();old=(B/'source/accepted_draft39.md').read_text();normal=' '.join(text.split())
req('exact draft43',sha(B/'source/THEORY_FINAL.md')=='a3b59ce9cedb7c9c3307c4bff1fac47af57bfa076717c1d426dfc487c2218c21' and len(text.splitlines())==1933)
changes=[{'tag':t,'old_start':a,'old_stop':z,'new_start':b,'new_stop':y} for t,a,z,b,y in difflib.SequenceMatcher(None,old.split(),text.split(),autojunk=False).get_opcodes() if t!='equal']
req('all48changed blocks',len(changes)==48 and changes==read('data/changes.json'))
req('all comparison blocks present',sum(z.startswith('CHANGE ') for z in (B/'source/word_changes.txt').read_text().splitlines())==48)
for base,n in [('draft39',237),('brackets',166),('preview2',415),('forcing',318),('repairs',107),('reach',948)]:
 j=read('source/'+base+'_result.json');req(base+' accepted count',j['check_count']==n);req(base+' proof linkage',j['proof_sha256']==sha(B/'source'/f'{base}_PROOF.md'))
p=read('data/parameters.json');ceilings=list(map(Q,p['ceilings']));table=[]
for line in text.splitlines():
 if not line.startswith('| '):continue
 v=[a.strip() for a in line.strip('|').split('|')]
 if len(v)!=6 or not re.match(r'^(?:d2|Mpen2|0\d\d)$',v[0]) or v[2]=='-':continue
 floor=Q(v[1].split()[0]);ratios=[]
 for k,c in enumerate(ceilings):
  ratio=floor/c;req(v[0]+' table factor '+str(k),ratio>Q(v[k+2])>1,ratio);ratios.append({'ratio_exact':str(ratio),'printed_lower':v[k+2]})
 table.append({'candidate':v[0],'strict_floor':str(floor),'ratios':ratios})
prior=read('source/draft39_result.json');req('23 numeric rows',len(table)==23)
req('22 inherited rows identical',[r for r in table if r['candidate']!='026']==prior['table'])
weak=read('source/026_weak_result.json');req('026 proof link',weak['inputs']['RUN_ROOT/theory_audit_T4/research/candidate026_weak/PROOF.md']==sha(B/'source/026_weak_PROOF.md'))
req('026 accepted strict floor',Q(weak['strict_lower_exact'])==Q('0.001355907204057457'))
req('026 truncated strictly downward',Q(table[-1]['strict_floor'])<Q(weak['strict_lower_exact']) and table[-1]['candidate']=='026')
req('026 complete gradient and comparisons',weak['gradient_certificate']['complete_critical_point_check'] and all(weak['comparisons'].values()))
bp=read('data/bracket_parameters.json');squares=[]
for r in bp['rows']:
 mu=Q(r['mu']);C=Q(r['C']);cu=Q(r['cU']);w2=Q(r['sqrtW2'])**2;value=4*mu**3/(27*C*cu**2*w2)
 upper=Q(bp['rebal_corrected_upper'] if r['name']=='TB-rebal' else r['printed'])
 req(r['name']+' exact positive ceiling',value>0)
 req(r['name']+' upward display',value<upper**2,value)
 req(r['name']+' common scalar ceiling',value<Q(bp['common_scalar_upper'])**2)
 saved=next(z for z in read('source/brackets_result.json')['rows'] if z['name']==r['name']);req(r['name']+' independent square',value==Q(saved['supremum_square_exact']))
 squares.append({'name':r['name'],'square_exact':str(value),'upper_exact':str(upper)})
 if r['name']=='TB-rebal':
  oldr=Q('3.5125e-7');req('old TB display below exact',oldr**2<value);req('TB relative change',value/oldr**2<Q('1.0000136')**2)
gsq=Q(50**2,651**2*28248);req('graded exact square',gsq==Q(625,2992882662));req('graded rational upper',gsq<Q(25,54684)**2);req('graded decimal upper',gsq<Q('4.5717e-4')**2)
x={k:Q(v) for k,v in p['sharpw'].items()};rate=x['mu']-x['C']*x['s']-x['cU']*x['r']*72
req('exact high rate',rate==Q(63092119,405000000));req('positive conservative rate',rate>Q('0.1557'));req('inverse rate',1/rate<Q('6.4226'))
req('self map exact slack',x['r']-x['eta']/Q('0.1557')==Q(7,1557000000));req('exact rate self map',x['r']>x['eta']/rate)
contract=ar(x['r']/x['betaL'])/(2*(arb.pi()*ar(x['s']*(1+x['s']))).sqrt());req('contraction factor',contract<ar('0.0137200'),contract)
c=Q(4076476460239181,2251799813685248);q=1/c-4;d=1-1/c;alpha=-2*q-2;D=5*c-1;Emin=(-q-1)/(2*(-q)*(-q-3));beta=ar(gsq).sqrt();endpoint=[]
for r in read('source/reach_result.json')['rows']:
 name=r['candidate'];bb=arb(r['B']);g0=ar(r['g0_exact'])
 def threshold(b):return ar(D)*(bb/(b*ar(alpha).sqrt()))**ar(d/(-q-1))/g0
 pt=threshold(ar(Q(25,54684)));ex=threshold(beta);actual=ex*bb/((2*arb.pi()).sqrt()*999745)
 req(name+' printed normalized cutoff',pt<ar('7.9417'),pt);req(name+' exact normalized cutoff',ex>ar('7.942167'),ex)
 req(name+' actual budget cutoff',actual<ar('0.2694533')<ar(Emin),actual)
 req(name+' cutoff monotonicity between printed and exact',ex>pt)
 endpoint.append({'candidate':name,'printed_normalized':pt.str(90),'exact_normalized':ex.str(90),'actual_budget_exact_graded':actual.str(90)})
forcing=read('source/forcing_result.json');req('ten forcing instances',len(forcing['instances'])==10)
for r in forcing['instances']:
 sq=Q(r['square_exact']);eta=Q(r['threshold_exact']);fl=Q(r['strict_integer_factor'])
 req(r['framework']+' integer factor',sq>(fl*eta)**2)
 req(r['framework']+' common lower factor',fl>=3542234)
 req(r['framework']+' finite threshold and s',eta>0 and Q(r['s_exact'])>=0)
ledger=(B/'source/N4_ledger.md').read_text()
for num in [377,378,379,380]:req('reciprocal acceptance present '+str(num),'## N4-'+str(num)+'.' in ledger)
for literal in ['E sqrt(2 pi) H_max/B < Emax(b)','original graded box; the FW-T-DYADIC-Y-v1 list above is separate','The dyadic rows of 025 and 026 are untested.','at its four targets','at the FW-A2-Db radii an improved valid constant is OPEN','smallest ratio above 3542234','a failed sufficient condition, which neither orders actual norms or distances nor excludes anything','No exact solution near any candidate has been shown to exist.','c[h] = 0']:
 req('scope '+literal,literal in normal)
req('no stale026 current status','C1-N1-026 (registered 13:12:37Z) is RULED OUT' in normal)
for p,h in m['inputs'].items():req('unchanged '+p,sha(B/p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'word_change_blocks':len(changes),'table_rows':len(table),'table':table,'ceiling_squares':squares,'endpoint':endpoint,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'source_sha256':sha(B/'source/THEORY_FINAL.md'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED changed mathematics and23distance rows, normalized endpoint condition, corrected ceiling and026/016 scope repairs; no full-matrix audit or existence closure'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',len(table),'rows',out['utc'],out['elapsed_seconds'])
