"""Independent exact report-change and errata audit. Peer programs remain data."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,gzip,hashlib,io,json,re,sys,tarfile,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0);checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
need('proof before checker',read('data/PROOF_FIRST.json')['checker_exists'] is False)
p=read('data/parameters.json');ctx.prec=p['precision_bits'];doc=(B/'source/THEORY_FINAL.md').read_text();old=(B/'../theory_final_draft53_audit/source/THEORY_FINAL.md').read_text();flat=' '.join(doc.split());readme=(B/'source/T1_README.md').read_text()
need('draft55 digest',sha(B/'source/THEORY_FINAL.md')=='aa2d306329e3a653d089824eebf9ee741c3383af60c17e0bf61f7deee4325169')
changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('all16 changed blocks',changes==read('data/changes.json') and len(changes)==16)
for topic,count in p['accepted_counts'].items():
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count)
for phrase in p['required_phrases']:need('target phrase '+phrase,phrase in flat)
# Archive bytes preserve the input bindings even if the producer later revises a file.
graph=read('data/README_bindings.json');need('graph180',len(graph['bindings'])==180)
need('graph archive binding',sha(B/'source/README_graph.tar.gz')==graph['archive_sha256'])
with tarfile.open(fileobj=io.BytesIO(gzip.decompress((B/'source/README_graph.tar.gz').read_bytes())),mode='r:') as tar:
 need('archive exact180members',len(tar.getmembers())==180)
 for row in graph['bindings']:
  raw=tar.extractfile(row['local']).read();need('README '+row['local'],len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'])
  if row['local'].endswith('.py'):ast.parse(raw.decode(),filename=row['local'])
# Review E8 and E9 from already accepted exact component data and signed pairings.
comp=read('../candidate016_dual_replay_audit/source/components.json')['norms'];lo={k:Q(v['accepted_lower_exact']) for k,v in comp.items()};W=Q(20,21)*2**18
need('E8 sufficient strict square',lo['P2']**2+2**14*lo['G1']**2+2**18*lo['G0']**2+W*Q(p['H_sufficient'])**2>Q(p['007_E2_upper'])**2)
need('E8 margin',Q('1.0139')<Q('.529469576110')/Q(p['H_sufficient'])<Q('1.014'))
for row in read('../theory_final_draft53_audit/verification/result.json')['optimizer_checks']:
 n=str(row['n']);lower,upper=p['optimizer_displacement_intervals'][n];disp=arb(row['one_minus_tstar'])
 need('E9strictsign'+n,arb(row['a_plus_b'])>0 and arb(lower)<disp<arb(upper))
 need('E9loss'+n,arb(row['t1_loss'])>0 and arb(row['t1_loss'])<arb('1e-70'))
# Equality is independent of the total upper and follows coefficientwise.
for N in [3,5,9,33]:
 modes=list(range(1,N,2))
 for loose in [0,1,1000000]:
  for widths in [False,True]:
   L=[Q(n+2,n+3) for n in modes];U=[x+(Q(1,n+5) if widths else 0) for n,x in zip(modes,L)];total=sum(U)+loose
   P=total/N**2+sum((Q(1,n*n)-Q(1,N*N))*u for n,u in zip(modes,U));S=sum(u/Q(n*n) for n,u in zip(modes,U))+(total-sum(L))/N**2
   need(f'E10identity{N}/{loose}/{widths}',S-P==sum(u-l for l,u in zip(L,U))/N**2>=0)
   need(f'E10equality{N}/{loose}/{widths}',(S==P)==(not widths))
# Exactly reproduce the 13 then 20 cumulative comparisons in check_v50.
a0=len(checks);prefix=read('../candidate016_prefix31_hardy_audit/source/N4_prefix_v02.json')
need('Ahashprefix',sha(B/'../candidate016_prefix31_hardy_audit/source/N4_prefix_v02.json')=='01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41')
need('Ahashcomponents',sha(B/'../candidate016_dual_replay_audit/source/components.json')=='a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
need('Aprefixmodes',[int(z['n']) for z in prefix['modes']]==list(range(1,32,2)))
QL=sum(Q(z['q_lower_exact']) for z in prefix['modes']);QU=sum(Q(z['q_upper_exact']) for z in prefix['modes']);RL=Q(prefix['full_rF_square_lower_exact']);RU=Q(prefix['full_rF_square_upper_exact'])
need('Aradial squares',RL==lo['rF']**2 and RU==Q(comp['rF']['accepted_upper_exact'])**2)
ratios=[QL/RU,QL/RL,QU/RU,QU/RL]
for i,x in enumerate(ratios):
 need('Acoarsebounds'+str(i),Q('.988805')<x<Q('.988806'));need('Aoldrefutation'+str(i),x>Q('.9888'))
need('Aextrema',min(ratios)==QL/RU and max(ratios)==QU/RL);countA=len(checks)-a0
mu=Q(97,250)-Q(397,5184);A=Q(8,5)*72;r=Q(1351,10**6);beta=mu-A*r;eta=mu*mu/(4*A);rstar=mu/(2*A);v=beta*r
need('BmuA',mu==Q(201799,648000) and A==Q(576,5))
need('Bbeta',beta==Q(63092119,405000000) and beta>=Q(1557,10000))
need('Bselected',Q(1557,10000)*r==Q(2103507,10**10) and Q(p['selected_threshold'])<=Q(1557,10000)*r)
need('Bvalue',v==Q(85237452769,405000000000000) and v>Q('2.1046e-4'))
need('Boptimum',rstar==Q(201799,149299200) and eta==Q(40722836401,193491763200000))
need('Blossidentity',eta-v==A*(r-rstar)**2>0)
need('Bbudgetinterval',Q('2.1046e-4')<eta<Q('2.1047e-4'));countAB=len(checks)-a0
need('A13 B7 cumulative20',countA==13 and countAB==20)
for i,x in enumerate(ratios):need('E11narrowendpoint'+str(i),Q('.988805059517')<x<Q('.988805059518'))
need('Blossdisplay',eta-v==Q(3583578769,75582720000000000000) and Q('4.740e-11')<eta-v<Q('4.742e-11'))
need('007optimumfactor',Q('756.5312630768')/eta>3594606)
out=(B/'source/T1_check_v50.out').read_text();rv50=(B/'source/T1_REVIEWS_v50.md').read_text();peer=(B/'source/T1_check_v50.py').read_text()
need('peer cumulative count output','13 checks' in out and '20 checks' in out and '33 checks' not in out)
need('single counter initialization',peer.count('n_ok = 0')==1)
need('three erroneous33claims','33 checks' in rv50 and '33 checks, under 1 s' in flat and any('check_v50.py' in l and '33 checks' in l for l in readme.splitlines()))
need('literal universal factor sentence','Every failure factor in this report uses 2.1035e-4' in flat)
need('other ratios are explicitly present','7.6219e-5' in doc and '1.0578e-4' in doc and 'against eta* the 007 factor is above 3594606' in flat)
# Matrix associations and directed factors. No peer code is executed.
matrix=(B/'source/closure_matrix_v153.md').read_text();rows={}
for line in matrix.splitlines():
 cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
 if len(cells)==11 and cells[0].isdigit():rows[int(cells[0])]=cells
need('matrix108rows',set(rows)==set(range(1,109)))
refs=[]
for m in re.finditer(r'(C1-N1-0\d\d|\b0[0-2]\d\b)[^.;]{0,160}?\brows? (\d+)(?: and (\d+))?',flat):
 name=m.group(1);name=name if name.startswith('C1') else 'C1-N1-'+name
 for token in [m.group(2),m.group(3)]:
  if token is None:continue
  n=int(token);need('reference'+str(len(refs)),n in rows and name in rows[n][1]+' '+rows[n][2]);refs.append([name,n])
need('83references',len(refs)==83)
factors=[]
for line in doc.splitlines():
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=6 or not re.match(r'\d',cells[1]) or cells[2]=='-':continue
 d=Q(cells[1].split()[0])
 for j,cap in enumerate(p['ceilings']):
  shown=cells[2+j];q=d/Q(cap);m=re.fullmatch(r'(\d+)(?:\.(\d+))?(?:e(\d+))?',shown);digits=len(m.group(2) or '')-int(m.group(3) or 0);scale=Q(10)**digits;v=q*scale;floor=Q(v.numerator//v.denominator)/scale
  need('factor'+str(len(factors)),Q(shown)==floor<=q);factors.append([cells[0],j,shown])
need('78exactfloors',len(factors)==78)
for n in [69,70,103,104,107,108]:need('OPEN row'+str(n),rows[n][-1].startswith('OPEN'))
need('001affine scope retained','affine class' in flat and 'T4-465' in doc and 'c != c0' in doc)
for token in ['row_refs.py','h18_verdicts.py']:
 line=next(l for l in readme.splitlines() if l.startswith('| checks/'+token+' |'));need('stale input column '+token,'closure_matrix_v151.md' in line.split('|')[-3])
need('currentv153 actual source','closure_matrix_v153.md' in (B/'source/T1_row_refs.py').read_text() and 'closure_matrix_v153.md' in (B/'source/T1_h18_verdicts.py').read_text())
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/THEORY_FINAL.md'),'changed_blocks':len(changes),'README_bindings':180,'references':refs,'distance_factors':factors,'peer_v50_actual_cumulative_checks':20,'peer_v50_incorrect_claimed_checks':33,'eta_star_exact':str(eta),'old_radius_loss_exact':str(eta-v),'source_status':'017 C1 to C3 remain OPEN; 016 bounds subsequently sharpened486','confirmed':'The16changes and E8toE11 have the stated mathematical scope; exact repairs,83references,78floors and180inputhashes pass.','refuted':['universal Every failure factor uses2.1035e-4 scope','33checks claim:13then20cumulative, actual20'],'provenance_correction':'README row_refs and h18_verdicts input columns sayv151 while code/provenance usev153','candidate_integrals_repeated':False,'foreign_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks;180bindings;83references;78factors;',r['elapsed_seconds'],'seconds')
