"""Independent source-bound preview audit; no foreign code executes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,re,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads((B/p).read_text())
checks=[]
def need(n,t,v=None):
 assert bool(t),(n,str(v))
 checks.append({'claim':n,'value':None if v is None else str(v)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
m=load('data/manifest.json');need('proof bound',sha(B/'PROOF.md')==m['proof_sha256'])
for p,h in m['inputs'].items():need('input '+p,sha(B/p)==h)
s=(B/'sources/theory_v08_preview1.md').read_text();compact=' '.join(s.split())
need('exact preview',sha(B/'sources/theory_v08_preview1.md')=='d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06')
need('all 769 lines',len(s.splitlines())==769)
old={r['row']:r for r in load('sources/factors_result.json')['rows']}
tree=ast.parse((B/'sources/t1_factors.py').read_text())
literal=next(ast.literal_eval(z.value) for z in tree.body if isinstance(z,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ROWS' for t in z.targets))
new={r[0].split()[0]:r for r in literal};need('24 literal rows',len(new)==len(old)==24)
md={}
for line in s.splitlines():
 if re.match(r'^\| [DSOU PRAK][1-5] \|',line):
  cols=[v.strip() for v in line.strip('|').split('|')];md[cols[0]]=cols
need('24 Markdown rows',len(md)==24)
rows=[]
for key,r in new.items():
 a=old[key];p=Q(r[1]);t=Q(r[3]);ratio=p/t;k=4 if ratio<100 else 2;scale=10**k;floor=Q((ratio*scale).numerator//(ratio*scale).denominator,scale)
 need(key+' source numerator',p==Q(a['numerator_exact']))
 need(key+' source threshold',t==Q(a['threshold_exact']))
 need(key+' source factor',floor==Q(a['downward_factor_exact']))
 for idx,value,name in [(2,p,'numerator'),(3,t,'threshold')]:
  match=re.match(r'^([0-9.eE+-]+(?:/[0-9]+)?)',md[key][idx]);need(key+' Markdown '+name,match is not None and Q(match[1])==value)
 need(key+' printed factor',Q(md[key][4])==floor)
 need(key+' failure',floor>1 and floor<=ratio)
 rows.append({'row':key,'p':str(p),'t':str(t),'ratio':str(ratio),'factor':str(floor),'k':k})
need('S2 corrected','6782715.40' in s and new['S2'][1]=='516.9717852723')
for text in ['not all the inequalities needed for existence','necessary only in this model','OPEN, not false','initial projection ... excluded','not a lower bound on the actual velocity','not a published requirement file']:
 need('scope retained '+text,text in compact)
for name,result,proof in [('factors','factors_result.json','factors_PROOF.md'),('outer','outer_result.json','outer_PROOF.md'),('reach','reach_result.json','reach_PROOF.md'),('universal','universal_result.json','universal_PROOF.md'),('draft38','draft38_result.json','draft38_PROOF.md'),('average','average_result.json','average_PROOF.md')]:
 d=load('sources/'+result);need(name+' accepted proof',d['proof_sha256']==sha(B/'sources'/proof))
outer=load('sources/outer_result.json')
for r in outer['rows']:
 n=r['candidate'];t=r['targets']
 for key,bound in [('sharpw_rounded_ceiling','8.647'),('TB_sharp_rounded_ceiling','7.287')]:
  need(n+' kernel '+key,arb(t[key]['thresholds']['93/250']['fallback'])<ar(bound))
 for field,bound in [('constant','13.27'),('fallback','14.41')]:need(n+' fixed kernel '+field,arb(t['fixed_sharpw_ball']['thresholds']['93/250'][field])<ar(bound))
 need(n+' no graded room',t['original_graded_ceiling']['thresholds']['93/250']['no_room'])
for r in load('sources/universal_result.json')['rows']:
 need(r['candidate']+' constant universal cap',arb(r['versions']['without_velocity_asymptotic']['delta_shape_cap'])<ar('1.421e-7'))
reach=load('sources/reach_result.json');emin=Q(reach['Emin_exact'])
for r in reach['rows']:
 n=r['candidate']
 for key,bound in [('Emin_H0','1.43912e-7'),('Emin_Phi_v0','1.14141e-7'),('current_H0','2.66323e-8')]:need(n+' variable cap '+key,arb(r['reach'][key]['bound'])<ar(bound))
 for key,lo in [('Db_fixed','1.020385'),('Db_family','0.8711127')]:
  v=arb(r['targets'][key]['threshold_Phi_v0_at_printed']);need(n+' small target '+key,v>ar(lo) and v>ar(emin))
 need(n+' trans excluded',arb(r['targets']['trans_fixed']['threshold_Phi_v0_at_printed'])<ar(emin))
need('trans bound below target',Q('1.14141e-7')<Q(1,2**23))
need('current bound below smallest target',Q('2.66323e-8')<Q(1,2**25))
need('lambda corrected',arb(outer['lambda'])>ar('109.6024'))
weak=load('sources/T4_025_weak.json');dist=Q(weak['strict_lower_exact'])
need('025 exact floor',dist==Q('0.002065801265578052') and arb(weak['radius'])>ar(dist))
for name,ceil,ratio in [('graded',Q(25,54684),Q('4.518')),('TB',Q('3.7930e-6'),Q('544.6'))]:need('025 factor '+name,dist/ceil>ratio)
need('025 stale OPEN text','C1-N1-025 (016\'s exact JSON plus 744 functions; 2918 generators; registered 12:50:59Z; rows 99 and 100): OPEN.' in compact)
need('025 contrary current text','Matrix v130 (13:27Z) records 025 RULED OUT' in compact)
need('scalar to dyadic overreach text','This completes the dyadic rows of the matrix; it cannot change a closure question' in compact)
need('number erratum inconsistency','Items 67 to 72 change no number or verdict.' in compact and 'the printed digits of R1-043 are repaired outward' in compact)
obs=load('data/appendix_observations.json');need('75 full appendix observations',len(obs['rows'])==75)
for r in obs['rows']:need('observed source exists '+r['path'],r['observed_sha256'] is not None)
changed=[r for r in obs['rows'] if r['observed_sha256']!=r['published_sha256']]
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'factor_rows':rows,'appendix_count':len(obs['rows']),'appendix_changed_since_generation':changed,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'preview_sha256':sha(B/'sources/theory_v08_preview1.md'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED corrected scoped factors and endpoint majorants; REFUTED stale 025 status and unrestricted scalar-to-dyadic inference; publication repairs in PROOF'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks;',len(rows),'factors;',len(changed),'mutable source changed;',result['utc'],result['elapsed_s'])
