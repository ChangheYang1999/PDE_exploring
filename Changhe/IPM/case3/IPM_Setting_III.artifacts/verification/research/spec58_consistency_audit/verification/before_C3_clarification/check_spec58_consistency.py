"""Result296: full byte comparison and extraction from completed independent audits."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction
import json, hashlib, difflib
import sympy as s
R=Path('research/spec58_consistency_audit');V=R/'verification'
checks=[];bindings={};rounding=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,b,evidence=None):
 checks.append(dict(name=name,passed=bool(b),evidence=evidence))
 if not b:raise AssertionError((name,evidence))
def load(p):
 p=Path(p);bindings[str(p)]=sha(p);return json.loads(p.read_text())
def gate(p,count=None):
 z=load(p);ck('complete '+str(p),z['status']=='PASS' and all(x['passed']for x in z['checks']))
 if count is not None:ck('count '+str(p),len(z['checks'])==z['count']==count)
 return z

def token(name,value,printed,scope='independent'):
 q=Fraction.from_float(value)if isinstance(value,float)else Fraction(value)
 d=Decimal(printed);step=Fraction(Decimal(10)**d.as_tuple().exponent);center=Fraction(d)
 ok=center-step/2<q<center+step/2
 row=dict(name=name,value=str(q),printed=printed,inside=ok,scope=scope);rounding.append(row);ck('rounding '+name,ok,row)

inp=load(V/'INPUTS.json')
for x in inp['files']:ck('frozen '+x['frozen'],sha(x['frozen'])==x['sha256'])
a=(V/'SPEC_v55.md').read_text();b=(V/'SPEC_v58.md').read_text();binds=gate('research/spec55_consistency_audit/verification/CHECKS.json',32)
ck('reviewed v55',sha(V/'SPEC_v55.md')=='2bdd93d3cb10f3235a80d1068dd32013941fb16f44f59c1018988051862f09ef')
ck('new version','Version v58, 2026-10-21T22:55Z' in b)
aa=a.splitlines(True);bb=b.splitlines(True)
changes=load(V/'CHANGES.json');actual=[dict(op=o,old_lines=[i,j],new_lines=[k,l],old=''.join(aa[i:j]),new=''.join(bb[k:l]))for o,i,j,k,l in difflib.SequenceMatcher(a=aa,b=bb,autojunk=False).get_opcodes()if o!='equal']
ck('complete three diff blocks',actual==changes and len(changes)==3)
reverse=bb[:]
for x in reversed(changes):k,l=x['new_lines'];i,j=x['old_lines'];reverse[k:l]=aa[i:j]
ck('full reverse bytes',''.join(reverse)==a)
ck('all earlier mathematics unchanged',a.split(' (G45)',1)[0].replace('Version v55, 2026-10-21T18:26Z','Version v58, 2026-10-21T22:55Z')==b.split(' (G45)',1)[0])
g45old=a.split(' (G45)',1)[1].split('## CHANGELOG',1)[0];g45new=b.split(' (G45)',1)[1].split(' (G46)',1)[0]
ck('G45 append only',g45new.startswith(g45old));hist=b.split('## CHANGELOG\n',1)[1];oldhist=a.split('## CHANGELOG\n',1)[1];ck('old history unchanged',hist.endswith(oldhist));ck('three new history entries',hist[:-len(oldhist)].count('\n- ')==2)

for f,n in [('degree19_grouped_moment_obstruction/verification/dep_1_CHECKS.json',710),('degree19_grouped_moment_obstruction/verification/TYPES12_CHECKS.json',1258),('degree19_grouped_moment_obstruction/verification/TYPES34_CHECKS.json',674),('degree19_grouped_moment_obstruction/verification/PARTITION_CHECKS.json',128),('degree19_grouped_moment_obstruction/verification/FINAL_PROVENANCE_CHECKS.json',131),('degree21_grouped_moment_obstruction/verification/FINAL_CHECKS.json',158),('degree21_grouped_moment_obstruction/verification/REVIEW_BINDINGS.json',159),('report81_installation_audit/verification/CHECKS.json',52)]:gate(Path('research')/f,n)
for f in ['research/degree21_grouped_moment_obstruction/verification/REVIEW_BINDINGS.json','research/report81_installation_audit/verification/FINAL_BINDINGS.json']:
 z=load(f)
 for x in z['files']:ck('existing bound '+x['path'],sha(x['path'])==x['sha256'])
installed=Path('research/report81_installation_audit/verification/installed81.md');bindings[str(installed)]=sha(installed)
ck('installed81 exact',sha(installed)=='872b311acceb9053252137351e9ac91d9234d5eeda3aa86bfcc1a2f614dab183')
flat=' '.join(b.split())
for text in ['checker 292 pending','would give d >= 25, P >= 27/2','checker 288 open','all three R_56, R_45, R_46 divided','d >= 23, P >= 25/2','The class excluded is the class of polynomial axis data only','no degree-uniform residual bound, no statement on limits','NOT a NO endpoint','neither convergence nor its absence established']:
 ck('scope '+text,text in flat)
ck('reported check total',1058+8468+282+335+320+15+16+354==10848)

n192=gate('research/hydrostatic_c2_resolved_192_audit/verification/SUMMARY.json',134)['states'][0]
comp=gate('research/hydrostatic_c2_resolved_192_audit/verification/COMPARISON.json',94)
gate('research/hydrostatic_c2_resolved_192_audit/verification/REVIEW_CHECKS.json',19)
token('E',n192['E'],'-0.957');token('B',n192['b'],'-4.239');token('B-6E',n192['b']-6*n192['E'],'1.5');token('delta',n192['delta'],'-5.4e-5');token('Cp/K',n192['cusp']['Cp_K'],'10.62');token('far raw axis limit',n192['far']['values']['r2'],'-0.5773')
regions=n192['final_regions'];maxw=max((x['R_Nf']for x in regions.values()),key=lambda x:x['R_Nf']);token('774 Rf maximum',maxw['R_Nf'],'4.60e-5');ck('max on vertical axis',maxw['x']==0);ck('774 common points',all(x['common_points']==774 for x in n192['refinements']))
for y,tok in [(1000000,'6.46e-5'),(100000000,'2.34e-5')]:
 row=next(x for x in n192['axis_points']if Fraction(x['y'])==y);token('axis Rf y='+str(y),abs(Fraction(row['R'])/Fraction(row['Nf'])),tok)
prod=comp['producer_record'];token('producer node loss',prod['recorded_nodes_Fmax'],'1.8e-7','producer record only');token('producer annulus Rf',prod['regional_source_grid'][2][3],'4.4e-5','producer record only');token('producer exterior Rf',prod['regional_source_grid'][3][3],'8.8e-5','producer record only');ck('producer diagnostic scope','no optimizer rerun or shared-grid comparison' in prod['scope']);ck('69 accepted updates and failure69',prod['accepted_line_count']==69 and prod['failed_index']==69)

fc=gate('research/hydrostatic_function_space_audit/verification/COMPARISON.json',203);fr=gate('research/hydrostatic_function_space_audit/verification/REVIEW_REPAIRS.json',375)
for i,row in enumerate([x for x in fc['summary']if x['c']==2]):
 for key,toks in [('field',['0.129','0.066','0.0079']),('gradient',['0.33','0.11','0.014']),('pointwise_relative',['0.12','0.061','0.0074'])]:token('pair'+str(i)+' '+key,row['nominal']['annulus'][key],toks[i])
for i,row in enumerate([x for x in fr['additional_regions']if x['c']==2]):
 u=row['additional_regions'];token('full gradient'+str(i),u['full_sample']['gradient']['value'],['1.74','0.53','0.031'][i]);ck('full sample size'+str(i),u['full_sample']['count']==19649);ck('boundary attains full maximum'+str(i),u['full_sample']['gradient']['value']==u['outer_boundary']['gradient']['value'])
vel=gate('research/hydrostatic_velocity_sequence_audit/verification/FINAL_STATISTICS.json',785)
rows=[x for x in vel['statistics']if x['c']==2 and x['mask']=='nominal'];ck('three velocity pairs',len(rows)==3)
for reg in ['inner','subunit','annulus','far']:
 for k in range(3):
  vals=[x['regions'][reg]['maxima'][k]['value']for x in rows];ck('decreasing velocity '+reg+' '+str(k),vals[0]>vals[1]>vals[2],vals)
repair=gate('research/hydrostatic_velocity_table_repair/verification/REVIEW_BINDINGS.json',105)
ck('table disagreements acknowledged',len(vel['failures'])==4)

Y,A,C,B,E,a0=s.symbols('Y A C B E a0');G=a0*Y+E*Y**3;v=A*Y-B*Y**3/3;res=s.expand((C*Y+v)*s.diff(G,Y)-G);delta=s.symbols('delta');rr=s.expand(res.subs(A,1+delta-C));ck('axis linear coefficient',rr.coeff(Y,1)==a0*delta);ck('axis cubic coefficient',s.expand(rr.coeff(Y,3)-((2+3*delta)*E-a0*B/3))==0);ck('exact cubic compatibility',s.expand(rr.coeff(Y,3).subs({delta:0,B:6*E/a0}))==0)
for p in [R/'PROOF.md',V/'INPUTS.json',V/'CHANGES.json',V/'DIFF.txt',V/'SPEC_v55.md',V/'SPEC_v58.md',Path(__file__)]:bindings[str(p)]=sha(p)
out=dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rounding=rounding,bindings=bindings,scope='Incremental extraction and complete text-difference audit, not new candidate evaluation.',qualifications=['G46 producer grid maxima are attributed records, not independent recomputations.','224 for d81 is stale; draft81 is already installed without224.','292 remains open; primary full-plane UNRESOLVED.'])
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],len(rounding),out['utc'])
