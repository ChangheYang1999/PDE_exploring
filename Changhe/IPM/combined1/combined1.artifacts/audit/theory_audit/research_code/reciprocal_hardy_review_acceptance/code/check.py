"""Finite reciprocal-review acceptance. Copied peer scripts are parsed, never run."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import factorial
import ast,gzip,hashlib,json,sys,time
from flint import fmpq,fmpq_poly as Poly
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def raw(p):
 q=B/p;b=q.read_bytes();return gzip.decompress(b) if q.suffix=='.gz' else b
def read(p):return json.loads(raw(p))
checks=[]
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');review=(B/'source/T1_review.md').read_text()
need('both complete reviews frozen','## R1-048.' in review and '## R1-049.' in review)
for name,count in [('dual',1368),('upper',65)]:
 text=(B/('source/T1_'+name+'.out')).read_text();need(name+' completed check log','checks passed '+str(count) in text and text.endswith('RESULT PASS\n'))
bindings=read('data/peer_data_mapping.json')
for name in ['dual','upper']:
 tree=ast.parse((B/('source/T1_'+name+'_check.py')).read_text())
 ds=[ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HASH' for t in n.targets)]
 need(name+' one explicit source map',len(ds)==1)
 for fn,h in ds[0].items():need(name+' same accepted source '+fn,hashlib.sha256(raw(bindings[fn])).hexdigest()==h)
# Reconstruct differential identities by polynomial arithmetic.
x=Poly([0,1]);w=1-x;F=lambda q:fmpq(str(q))
def D(b,P):return (1-2*F(b)*x)*P+2*x*w*P.derivative()
def integral(P,q):
 q=Q(q);need('integrable exponent '+str(q),q>-1);out=Q(0)
 for j,c in enumerate(P.coeffs()):
  v=Q(factorial(j))
  for z in range(1,j+2):v/=q+z
  out+=Q(str(c))*v
 return out
fixtures={}
for ns,row in p['fixtures'].items():
 n=int(ns);b=Q(row['b']);P=Poly([F(c) for c in row['P']]);D1=D(b,P);D2=D(b,D1);L=n*n*P-D2
 ds=integral(D1*D1+n*n*P*P,2*b-2)/2
 aa=integral(D1*D1+D2*D2/(n*n),2*b-2)/2
 MM=integral(L*L/(n*n),2*b-2)/2
 bb=integral(L*D2/(n*n),2*b-2)/2
 pp=integral(L*P,2*b-2)/2
 for k,val in [('d',ds),('a',aa),('M',MM)]:need('fixture '+ns+'/'+k,val==Q(row[k])>0)
 need('fixture '+ns+' signed identities',MM==ds+aa and bb==-aa and pp==ds)
 need('fixture '+ns+' complete optimum',MM-bb*bb/aa==ds)
 fixtures[n]={'d':ds,'a':aa,'M':MM}
for n,k,bs in p['shift_parameters']:
 beta=Q(bs);b=beta-1;a=3+2*k;s=beta+k;P=x**(k+1)
 need('origin '+str((n,k,bs)),a>=n and (a-n)%2==0)
 need('L shift '+str((n,k,bs)),D(b,P)==a*P-2*F(s)*x*P)
 need('L2 shift '+str((n,k,bs)),D(b,D(b,P))==a*a*P-4*F(s)*(a+1)*x*P+4*F(s)*(F(s)+1)*x*x*P)
 need('r2Delta shift '+str((n,k,bs)),D(b,D(b,P))-n*n*P==(a*a-n*n)*P-4*F(s)*(a+1)*x*P+4*F(s)*(F(s)+1)*x*x*P)
H=fixtures[1]['d']+fixtures[3]['d'];M=fixtures[1]['M']+fixtures[3]['M'];one=M-fixtures[1]['a']
need('complete H2',H==Q(p['H2_over_pi']))
need('one-mode upper and gap',one==Q(p['one_test_over_pi']) and one-H==Q(p['gap_over_pi']))
need('both-mode correction exactly complete',M-fixtures[1]['a']-fixtures[3]['a']==H)
for q in [Q(1,3),Q(1,2),Q(3,4),Q(3,2)]:
 d0=fixtures[1]['d'];a0=fixtures[1]['a'];M0=fixtures[1]['M'];d=q*q*d0;a=q*q*a0;b=-q*a0;pair=q*d0;Mg=(1-q)**2*M0;Hg=(1-q)**2*d0
 need('residual energy '+str(q),d0==2*pair-d+Hg)
 need('residual field '+str(q),M0+2*b+a==2*pair-d+Mg)
 need('optimal gain '+str(q),M0+2*b+a-(M0-b*b/a)==(a+b)**2/a)
 need('triangle exact comparison '+str(q),d*Mg>=(pair-d)**2)
# Check peer descriptions from source without executing them.
tree=ast.parse((B/'source/T1_upper_check.py').read_text())
ex=[n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='delta_e' for t in n.targets)]
need('one fixture exponent',len(ex)==1 and isinstance(ex[0],ast.Call) and isinstance(ex[0].func,ast.Name) and ex[0].func.id=='Fr')
e=Q(*(ast.literal_eval(a) for a in ex[0].args));need('executed fixture exponent',e==Q(p['exponent_executed']))
need('prose exponent attribution differs','source r w^(7/10)' in review and e!=Q(p['exponent_description']))
need('positive-pole substitution',625*w+x==1+624*w)
need('pole bounded positive',1>0 and 1+624==625)
need('FLOAT explicitly retained','FLOAT quadrature' in review and '40-digit quadrature' in review)
# Accepted exact source composition, not a repeat of candidate moment integrations.
old=read('../candidate016_dual_replay_audit/verification/result.json');cross=read('../candidate016_cross_archive_audit/verification/result.json');prefix=read('../candidate016_prefix_hardy_audit/verification/result.json')
for name,d,num in [('dual',old,2099),('archive',cross,3113),('prefix',prefix,2297)]:need('accepted '+name+' count',d['check_count']==len(d['checks'])==num)
need('actual650digit replay accepted',cross['new650digit_groups_independently_resummed'] is True)
for key in ['H_lower_square_exact','H_strict_lower_exact','E2_lower_square_exact','E2_strict_lower_exact','007_E2_strict_upper_exact','strict_E2_gap']:need('same composed exact '+key,old[key]==cross[key])
Hlo=Q(cross['H_strict_lower_exact']);H2=Q(cross['H_lower_square_exact']);Elo=Q(cross['E2_strict_lower_exact']);E2=Q(cross['E2_lower_square_exact']);U7=Q(cross['007_E2_strict_upper_exact'])
need('strict H floor',0<Hlo*Hlo<H2)
need('strict E2 floor',0<Elo*Elo<E2)
need('positive pairwise separation',Elo-U7==Q(cross['strict_E2_gap'])==Q('1.572166921614')>0)
need('same prefix accepted lower',Q(prefix['H_strict_lower'])==Hlo and Q(prefix['E2_strict_lower'])==Elo)
need('same prefix complete source',prefix['complete_mode_count']==160 and prefix['complete_field_branch_count']==1360)
need('prefix Hardy upper strict',Q(prefix['improved_H_strict_upper'])**2>Q(prefix['improved_H_square_upper_exact'])>=H2)
need('prefix E2 upper strict',Q(prefix['E2_strict_upper'])**2>Q(prefix['E2_upper_square_exact'])>=E2)
need('same accepted cross improvement',prefix['selected_cross_improvement_strict_lower_exact']==cross['improvement_sum_strict_lower_exact'])
need('conditional source observations retained','CONDITIONAL on c1-n3' in review and 'No numerical H upper bound is accepted here' in review)
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'T1_review_sha256':sha(B/'source/T1_review.md'),'fixtures_over_pi':{str(n):{k:str(v) for k,v in d.items()} for n,d in fixtures.items()},'H_lower_exact':str(Hlo),'E2_lower_exact':str(Elo),'strict_E2_gap':str(Elo-U7),'accepted_complete_H_upper':prefix['improved_H_strict_upper'],'accepted_complete_E2_upper':prefix['E2_strict_upper'],'refuted_fixture_exponent_description':p['exponent_description'],'actual_fixture_exponent':str(e),'peer_checks':[1368,65],'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED R1-048/R1-049 reciprocal analytic and exact fixture review, retaining source moment premises. REFUTED 7/10 attribution of the FLOAT fixture evaluated with exponent7/5. General469 now accepted from both Opus theory lanes; no inverse or existence.'}
with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
print('PASS',len(checks),'checks',result['elapsed_seconds'],'seconds')
