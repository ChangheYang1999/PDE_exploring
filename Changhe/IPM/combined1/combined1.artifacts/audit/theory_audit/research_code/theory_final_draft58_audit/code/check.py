"""Independent exact draft58 and R1-052 acceptance. Frozen peer code is data."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,difflib,gzip,hashlib,io,json,re,sys,tarfile,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0);checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
p=read('data/parameters.json');ctx.prec=p['precision_bits'];need('proof first',not read('data/PROOF_FIRST.json')['checker_exists']);doc=(B/'source/THEORY_FINAL.md').read_text();old=(B/'../theory_final_draft55_audit/source/THEORY_FINAL.md').read_text();flat=' '.join(doc.split());readme=(B/'source/T1_README.md').read_text()
need('draft58 digest',sha(B/'source/THEORY_FINAL.md')=='f76c41fb4e5f3733e5f0ac2749120c80a9771349b97ab83f61bcfe86c059f91f')
changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('all31 changes',changes==read('data/changes.json') and len(changes)==31)
for topic,count in p['accepted_counts'].items():
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==len(r['checks'])==count)
for phrase in p['required_phrases']:need('phrase '+phrase,phrase in flat)
graph=read('data/README_bindings.json');need('186 graph bindings',len(graph['bindings'])==186);archives={'prior':B/'../theory_final_draft55_audit/source/README_graph.tar.gz','delta':B/'source/README_delta.tar.gz'};rawfiles={}
for kind,path in archives.items():
 need('archive '+kind,sha(path)==graph[kind+'_archive_sha256'])
 with tarfile.open(fileobj=io.BytesIO(gzip.decompress(path.read_bytes())),mode='r:') as tar:
  for item in tar.getmembers():rawfiles[kind,item.name]=tar.extractfile(item).read()
need('delta exactly9',sum(r['archive']=='delta' for r in graph['bindings'])==9 and sum(k=='delta' for k,n in rawfiles)==9)
for row in graph['bindings']:
 raw=rawfiles[row['archive'],row['local']];need('README '+row['local'],len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'])
 if row['local'].endswith('.py'):ast.parse(raw.decode(),filename=row['local'])
def archivejson(name):
 rows=[r for r in graph['bindings'] if r['local']=='checks/data/'+name];need('unique review input '+name,len(rows)==1);r=rows[0];return json.loads(rawfiles[r['archive'],r['local']])
R18=archivejson('N4418_result_v01.json');R17=archivejson('N4417_result_v03.json');R9=archivejson('N4409_result_v02.json');R10=archivejson('N4410_result.json');comp=archivejson('N4392_comparison.json')['norms'];R398=archivejson('N4398_result.json');R7=archivejson('N4252_result.json')
for r,c in [(R18,4430),(R17,2065)]:need('all producer checks '+str(c),r['check_count']==len(r['checks'])==c and all(r['checks'].values()))
need('one raw016',all(r['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42' for r in [R18,R17,R9,R10]))
need('160 coverage',R17['complete_field_mode_count']==160 and R17['complete_uncomputed_tail_retained'] and R18['all160_source_modes_covered'] and R18['individually_integrated_Hardy_modes']==16 and R18['pairing_group_count']==2130)
need('selected16',[int(x['n']) for x in R18['selected_modes']]==list(range(1,32,2)))
q={int(z['n']):Q(z['q_upper_exact']) for z in R17['modes']};ln={int(z['n']):Q(z['selected_lower']) for z in R18['selected_modes']};jn={int(z['n']):Q(z['selected_improvement']) for z in R18['selected_modes']};RU=Q(R17['full_rF_square_upper_exact']);V=RU/33**2+sum((Q(1,n*n)-Q(1,33**2))*u for n,u in q.items());L=sum(x*x for x in ln.values());J=sum(jn.values());U=V-J
need('matching source prefix',R17['modes']==R9['modes']);need('V exact',V==Q(R17['M2_upper_exact']));need('L exact',L==Q(R18['H_lower_square_exact']));need('U exact',U==Q(R18['H_upper_square_exact']));need('J exact',J==Q(60190270781084901078904854514861671131,25*10**37));need('J1J3',jn[1]+jn[3]==Q(R398['improvement_sum_strict_lower_exact']));need('additional improvement',J-jn[1]-jn[3]>Q('.002101926'))
gap={n:q[n]/n**2-jn[n]-ln[n]**2 for n in q};tail=(RU-sum(q.values()))/33**2;width=U-L
for n,g in gap.items():need('positive mode gap '+str(n),g>0)
need('width identity',width==sum(gap.values())+tail and tail>0);glo=sum(v for n,v in gap.items() if n<=15);ghi=sum(v for n,v in gap.items() if n>=17)
for name,value,bound in [('low modes',glo,'1e-9'),('high modes',ghi,'.000980734'),('tail',tail,'.000524909'),('total',width,'.001505643')]:need('width bound '+name,0<value<Q(bound))
for name,v,rounded in [('high',ghi/width,'.651'),('tail',tail/width,'.349')]:need('share rounding '+name,abs(v-Q(rounded))<Q('.0005'))
for name,v,lo,hi in [('L',L,'.380360210930','.380360210931'),('V',V,'.622626936300','.622626936301'),('U',U,'.381865853175','.381865853176'),('J',J,'.240761083124','.240761083125')]:need('directed '+name,Q(lo)<v<Q(hi))
HL=Q(308366750368225240013184170643,5*10**29);HU=Q(154488238463271634620877708271,25*10**28);EL=Q(628580088526341,10**12);EU=Q(314439512374259,5*10**11)
for name,v in [('H_strict_lower_exact',HL),('H_strict_upper_exact',HU),('E2_strict_lower_exact',EL),('E2_strict_upper_exact',EU)]:need('endpoint '+name,Q(R18[name])==v)
need('H strict squares',HL**2<L<U<HU**2)
def e2(kind,h2):
 c={k:Q(v['accepted_'+kind+'_exact']) for k,v in comp.items()};return c['P2']**2+2**14*c['G1']**2+2**18*c['G0']**2+Q(20,21)*2**18*h2
EL2=e2('lower',L);EU2=e2('upper',U);need('E2 strict squares',EL**2<EL2<EU2<EU**2 and EL2==Q(R18['E2_lower_square_exact']) and EU2==Q(R18['E2_upper_square_exact']))
need('outward12H9E',Q('.616733500736')<HL and HU<Q('.617952953854') and Q('628.580088526')<=EL and EU<Q('628.879024749'));need('Hwidth',HU-HL<Q('.001219454'))
b7=R7['H_input_lower_ball'].strip('[]').split();need('007 H ball shape',b7[1]=='+/-');H7L=Q(b7[0])-Q(b7[2]);E7U=Q(R7['E_upper']['strict_upper_exact']);hg=H7L-HU;eg=EL-E7U
need('E2gap exact',eg==Q('21.759869526341')==Q(R18['E2016_minus_E2007_strict_lower_exact']));need('Hgap',hg>Q('.017571422147005') and hg==Q(R18['H007_minus_H016_strict_lower_exact']))
need('later claimed lower positions',HL<Q('.6167972322')<HU and EL<Q('628.5957005')<EU);need('later claimed upper positions',HU<Q('.6189603636') and EU<Q('629.1263188'));need('n3lower3.6refuted3.65valid',Q('3.64e-11')<abs(HL-Q('.6167335007'))<Q('3.65e-11'))
for s,r,floor in [(Q(1,7744),Q(147,200000),'.6817'),(Q(1,5184),Q(1351,10**6),'.6725')]:
 sa=arb(s.numerator)/s.denominator;ra=arb(r.numerator)/r.denominator;cs=1/(4*arb.pi()*sa*(1+sa)).sqrt();need('slope'+str(s),arb('.7')-cs*ra>arb(floor))
need('K sharp',Q(121000000,12551327)<Q('9.6432'));need('K sharpw',Q(405000000,63092119)<Q('6.4226'))
need('AK2 Young division',Q(63,4)/8==Q(63,32) and Q(61,4)/8<Q(63,32));need('AK2 named S1','AK2, the S1 squared constant 63/32, by T4-301' in flat)
rv=(B/'source/T1_REVIEWS_v51.md').read_text();need('R1 output88','checks passed 88' in (B/'source/T1_check_N4418.out').read_text());need('E12correct cumulative','20 checks in all' in rv and 'counts cumulatively' in rv)
need('selected factor remaining literal','Every sharpw forcing factor quoted in this report is against the selected threshold 2.1035e-4' in flat and 'against eta* the 007 factor is above 3594606' in flat)
first={n:json.loads((B/'../numerical_literal_review_acceptance/source'/f'{n}_weaktests2.json').read_text(),parse_float=Q)['NORM-T-WEAK-v1_a0'] for n in ['007','013']};rat={int(k):abs(Q(v['I_k'])/Q(first['013'][k]['I_k'])) for k,v in first['007'].items()}
need('FLOAT first128 rounding',Q('26.8')<rat[128]<Q('26.9'));need('FLOAT first12floor',Q(9358)<rat[12]<9359)
for k,qv in rat.items():
 if k<=96:need('FLOAT early '+str(k),qv>126)
 if 192<=k<=1024:need('FLOAT later '+str(k),qv<Q('2.1'))
need('FLOAT actual increases',rat[192]<1 and rat[384]<1)
matrix=(B/'source/closure_matrix_v157.md').read_text();rows={}
for line in matrix.splitlines():
 cells=[x.strip() for x in re.split(r'(?<!\\)\|',line.strip())[1:-1]]
 if len(cells)==11 and cells[0].isdigit():rows[int(cells[0])]=cells
need('matrix108',set(rows)==set(range(1,109)));refs=[]
for m in re.finditer(r'(C1-N1-0\d\d|\b0[0-2]\d\b)[^.;]{0,160}?\brows? (\d+)(?: and (\d+))?',flat):
 name=m.group(1);name=name if name.startswith('C1') else 'C1-N1-'+name
 for token in [m.group(2),m.group(3)]:
  if token is None:continue
  n=int(token);need('reference'+str(len(refs)),n in rows and name in rows[n][1]+' '+rows[n][2]);refs.append([name,n])
need('83references',len(refs)==83);factors=[]
for line in doc.splitlines():
 cells=[x.strip() for x in line.strip().strip('|').split('|')]
 if len(cells)!=6 or not re.match(r'\d',cells[1]) or cells[2]=='-':continue
 d=Q(cells[1].split()[0])
 for j,cap in enumerate(p['ceilings']):
  shown=cells[2+j];qv=d/Q(cap);m=re.fullmatch(r'(\d+)(?:\.(\d+))?(?:e(\d+))?',shown);digits=len(m.group(2) or '')-int(m.group(3) or 0);scale=Q(10)**digits;v=qv*scale;floor=Q(v.numerator//v.denominator)/scale;need('floor'+str(len(factors)),Q(shown)==floor<=qv);factors.append([cells[0],j,shown])
need('78floors',len(factors)==78)
for n in [69,70,103,104,107,108]:need('OPEN'+str(n),rows[n][-1].startswith('OPEN'))
for token in ['row_refs','h18_verdicts']:
 line=next(l for l in readme.splitlines() if l.startswith('| checks/'+token+'.py |'));need('v157 README '+token,'closure_matrix_v157.md' in line.split('|')[-3]);need('v157 script '+token,'closure_matrix_v157.md' in (B/'source'/('T1_'+token+'.py')).read_text())
for row in read('data/manifest.json'):need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/THEORY_FINAL.md'),'changed_blocks':31,'README_bindings':186,'references':refs,'distance_factors':factors,'width_parts_exact':{'selected_n_le15':str(glo),'selected_n_ge17':str(ghi),'tail':str(tail),'total':str(width)},'H_interval_exact':[str(HL),str(HU)],'E2_interval_exact':[str(EL),str(EU)],'H_gap_strict_lower_exact':str(hg),'E2_gap_strict_lower_exact':str(eg),'candidate_integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED R1-052 exact recomposition and scoped draft58 repairs. REFUTED R1-052 V8 proximity3.6e-11 and remaining universal selected-threshold wording. Candidate verdicts unchanged;017 whole-field premises remain OPEN.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks;',out['elapsed_seconds'],'seconds')
