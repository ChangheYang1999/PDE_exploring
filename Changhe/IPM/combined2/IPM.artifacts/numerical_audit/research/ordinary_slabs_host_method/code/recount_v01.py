"""Auditor-local exact recount of the complete numerics_agent_2 ordinary-slab record."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,gzip,json,time,os,sys
import common_v01 as protocol
P=argparse.ArgumentParser();P.add_argument('--directory',required=True);P.add_argument('--output',required=True);o=P.parse_args()
R=Path.cwd().resolve();CAM=R.parent
assert R.name=='numerical_audit';protocol.environment(50)
assert o.directory=='numerics_agent_2/'+protocol.OUTPUT
D=protocol.named(CAM,o.directory)
OUT=protocol.named(R,o.output);assert OUT.parent==R/'research/ordinary_slabs_host_method/verification'
assert not OUT.exists()
sys.set_int_max_str_digits(0)
start=protocol.stamp();tick=time.monotonic();checks=0
F=('a','b','e','rh','sh','ud','uh');J=protocol.ROOTS
TARGETS=dict(matrix_gap='3/5',gradient='71/500',weak_gradient='1/4',strain='137/125',large_strain='3/2')
def ck(x,label):
 global checks
 checks+=1;assert x,label
h=protocol.digest

def loadz(p):
 with gzip.open(p,'rt') as f:return json.load(f)
def interval(v):
 ck(type(v)is list and len(v)==2,'two endpoints');a,b=map(Q,v);ck(a<=b,'ordered endpoints');return a,b

def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
 v=[a*b for a in x for b in y];return min(v),max(v)
def sq(x):
 a,b=x;return (Q(0)if a<=0<=b else min(a*a,b*b)),max(a*a,b*b)
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def joint(p):return dict(primary=p['matrix']and p['weak_gradient']and p['large_strain'],small_strain=p['matrix']and p['weak_gradient']and p['strain'],small_gradient=p['matrix']and p['gradient']and p['large_strain'],both_small=p['matrix']and p['gradient']and p['strain'])
C=protocol.read(D/'check_v01.json');E=protocol.read(D/'execution_v01.json')
ck(C['status']=='COMPLETED_SOURCE_RECONSTRUCTION','completed source calculation')
ck(E['schema']=='ordinary-slab-host-execution-v1','actual host schema')
ck(E['status']=='COMPLETED' and E['reason']is None and E['exit_code']==0 and E['script_unchanged'] and E['complete_source_record'],'successful source execution')
ck(E['limit_seconds']==7200 and 0<E['elapsed_seconds']<7200 and E['old_process_signals']==0 and not E['own_child_signals'],'bounded successful execution')
a=argparse.Namespace(**{k:E[k] for k in ('request','request_sha256','review','review_sha256','adoption','adoption_sha256')})
QREQ,METHOD,bindings=protocol.authenticate(CAM,a)
ck(bindings==E['bindings'],'complete receipt bindings')
HOST=CAM/'numerics_agent_2';MD=protocol.named(HOST,QREQ['method_directory']);IP=MD/'installation_v01.json';I=protocol.read(IP)
ck(h(IP)==E['installation_sha256'] and I['status']=='INSTALLED_NOT_STARTED','installation')
ck(I['bindings']==bindings,'installation bindings')
for n,z in I['copies'].items():
 path=protocol.named(HOST,n);ck(h(path)==z,'copied input');bindings[str(path.relative_to(CAM))]=z
ck(I['initial_resources']['lane_bytes']<=3000000000-650000000,'installation storage reserve')
ck(I['initial_resources']['filesystem_free_bytes']>=20000000000,'installation filesystem reserve')
ck(not I['initial_processes']['conflicts'],'installation exclusive core')
ck(E['script_sha256']==METHOD['files']['code/check_v01.py'],'source code identity')
ck(E['owner']=='numerics_agent_2' and E['cpu']==49 and E['nice']==19 and E['threads']==1,'host resource contract')
ck(QREQ['output']==protocol.OUTPUT and QREQ['roots']==J,'assigned output and complete roots')
moment=protocol.moment
ck(moment(I['finished_utc'])<=moment(E['started_utc'])<moment(QREQ['no_new_after']),'installation before execution')
ck(moment(E['started_utc'])<=moment(C['started_utc'])<=moment(C['finished_utc'])<=moment(E['finished_utc'])<moment(QREQ['stop_at']),'source chronology')
ck(abs((moment(E['finished_utc'])-moment(E['started_utc'])).total_seconds()-E['elapsed_seconds'])<2,'duration consistency')
ck(h(D/'run_v01.log')==E['log_sha256'] and h(D/'check_v01.json')==E['check_sha256'],'actual output identities')
ck(C['requested_roots']==J and [v['root_index'] for v in C['results']]==J,'complete root order')
ck(E['argv']==['-B',protocol.METHOD+'/code/check_v01.py','--roots',','.join(map(str,J)),'--output',protocol.OUTPUT],'actual command')
ck(C['source_counts']==dict(branches=45,polynomial_coefficients=621400),'complete source counts')
ck(C['compile_precision']==2560 and C['cell_precision']==384,'source precision')
for n,z in C['files'].items():ck(h(protocol.named(CAM,n))==z,'source bound input');bindings[n]=z
for path in [IP,D/'check_v01.json',D/'execution_v01.json',D/'run_v01.log',D/'resource_samples_v01.jsonl',D/'guard_start_v01.json',Path(__file__),Path(protocol.__file__)]:bindings[str(path.relative_to(CAM))]=h(path)
G=protocol.read(D/'guard_start_v01.json')
ck(G['request_sha256']==E['request_sha256'] and G['installation_sha256']==E['installation_sha256'],'actual guard start')
ck(G['initial_resources']['lane_bytes']<=3000000000-650000000 and G['initial_resources']['filesystem_free_bytes']>=20000000000,'actual launch reserve')
ck(not G['initial_processes']['conflicts'],'actual launch exclusive core')
samples=[json.loads(line) for line in (D/'resource_samples_v01.jsonl').read_text().splitlines()]
ck(len(samples)==E['storage_checks'] and samples,'complete resource observations')
for s in samples:
 ck(s['lane_bytes']<2900000000 and s['filesystem_free_bytes']>=20000000000 and s['host_rss_bytes']<30000000000 and not s['conflicts'],'successful resource sample')
 ck(0<=s['elapsed_seconds']<7200 and moment(s['utc'])<moment(QREQ['stop_at']),'sample within budget')
source_path=protocol.named(CAM,protocol.SOURCE)
ck(h(source_path)==protocol.SOURCE_SHA,'complete exact source identity')
source=loadz(source_path)
expected={(i,f)for i,b in enumerate(source['branches'])for f in F if b['polynomials'][f]};ck(len(expected)==310,'nonempty source branches')
records=[]
for result in C['results']:
 j=result['root_index'];sigma=Q(255-2*j,256);rho=Q(1,255-2*j)
 cp=D/f'coefficients_root{j}_v01.json.gz';bp=D/f'cells_root{j}_v01.json.gz'
 ck(h(cp)==result['coefficient_sha256']and h(bp)==result['result_sha256'],'archive identities')
 A,B=loadz(cp),loadz(bp)
 for p in [cp,bp]:bindings[str(p.relative_to(CAM))]=h(p)
 ck(A['root_index']==B['root_index']==j,'root identity')
 ck(Q(A['sigma_exact'])==Q(B['sigma_exact'])==sigma and Q(A['rho_exact'])==Q(B['rho_exact'])==rho,'exact slab geometry')
 ck(B['domain_r_squared']==[str(Q(j,128-j)),str(Q(j+1,127-j))],'squared radius')
 ck(A['source_sha256']=='2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d','exact source')
 ck(A['compile_precision']==2560 and A['cell_precision']==384,'archive precision')
 ck(set(A['coefficients'])==set(A['degrees'])==set(A['tail_uppers'])==set(F),'complete fields')
 branches=set();sums={f:Q(0)for f in F}
 for b in A['branch_records']:
  key=(b['branch'],b['field']);ck(key in expected and key not in branches,'branch identity');branches.add(key)
  ck(type(b['order'])is int and 120<=b['order']<=480 and b['order']%20==0,'finite Taylor order')
  ck(type(b['polynomial_degree'])is int and b['polynomial_degree']>=0,'polynomial degree')
  v=Q(b['tail_upper']);ck(v>=0 and Q(b['polynomial_norm_at_h_upper'])>=0,'positive majorants');sums[b['field']]+=v
 ck(branches==expected,'complete branch field set')
 nc=0;width=source['degree_z']+1
 for f in F:
  rows=A['coefficients'][f];ck(len(rows)==A['degrees'][f]+1,'all retained rows')
  for row in rows:
   ck(len(row)==width,'complete angular row')
   for v in row:interval(v);nc+=1
  ck(sums[f]<=Q(A['tail_uppers'][f])<Q(1,10**6),'containing full field tail')
 ck(B['status']=='COMPUTED'and B['targets']==TARGETS,'source summary')
 nu,na=B['radial_cells'],B['angular_cells'];ck(nu==32 and na==256,'grid size')
 ck(len(B['cells'])==B['cell_count']==nu*na,'all cells')
 seen=set();ext=[None]*5;both={k:True for k in ['primary','small_strain','small_gradient','both_small']};original=both.copy();fails=[]
 for c in B['cells']:
  ui,ai=c['radial_index'],c['angular_index'];ck(type(ui)is int and type(ai)is int and 0<=ui<nu and 0<=ai<na,'cell index');ck((ui,ai)not in seen,'unique cell');seen.add((ui,ai))
  ck(set(c['fields'])==set(F),'field record');v={f:interval(c['fields'][f])for f in F};S=interval(c['sin_squared']);ck(S[0]<=1 and S[1]>=0,'sine range intersects unit interval')
  det=sub(mul(v['a'],v['b']),mul(S,sq(v['e'])));gg=add(sq(v['rh']),mul(S,sq(v['sh'])));ss=add(sq(v['ud']),mul(mul(S,sq(v['uh'])),(Q(1,4),Q(1,4))))
  d=[v['a'][0],v['b'][0],det[0],gg[1],ss[1]]
  exact=dict(matrix=all(x>=0 for x in d[:3]),gradient=d[3]<=Q(71,500)**2,weak_gradient=d[3]<=Q(1,4)**2,strain=d[4]<=Q(137,125)**2,large_strain=d[4]<=Q(3,2)**2)
  sp=c['predicates'];ck(set(sp)==set(exact)and all(type(x)is bool for x in sp.values()),'separate source flags')
  sd=interval(c['determinant']);sg=interval(c['gradient_squared']);st=interval(c['strain_squared'])
  saved=dict(matrix=v['a'][0]>=0 and v['b'][0]>=0 and sd[0]>=0,gradient=sg[1]<=Q(71,500)**2,weak_gradient=sg[1]<=Q(1,4)**2,strain=st[1]<=Q(137,125)**2,large_strain=st[1]<=Q(3,2)**2)
  for k in sp:ck(not sp[k]or saved[k],'reported true flag has sufficient exact saved endpoints')
  sj=joint(sp);ej=joint(exact);ck(c['joint_flags']==sj,'source conjunctions')
  for k in both:original[k]&=sj[k];both[k]&=sj[k]and ej[k]
  if not all(sp.values()):fails.append([ui,ai,sp])
  for k,x in enumerate(d):
   if ext[k]is None or (x<ext[k]if k<3 else x>ext[k]):ext[k]=x
 ck(seen=={(i,k)for i in range(nu)for k in range(na)},'complete product partition')
 ck(B['joint_flags']==result['joint_flags']==original,'source aggregate conjunctions');ck(B['failed_cells']==fails,'recorded failed strong cells')
 area=sum((2*rho/Q(nu*na)for _ in seen),Q(0));ck(area==2*rho,'exact covered normalized area')
 records.append(dict(root_index=j,cell_count=len(seen),coefficient_intervals=nc,branch_fields=len(branches),normalized_area=str(area),domain_r_squared=B['domain_r_squared'],joint_flags=both,rational_extrema=list(map(str,ext)),total_tail_uppers=A['tail_uppers']))
for n,z in bindings.items():ck(h(CAM/n)==z,'unchanged recount inputs')
report=dict(status='CONFIRMED_RECOUNT',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,checks=checks,bindings=bindings,slabs=records,scope='Exact endpoint and product-cover recount following complete independent source reconstruction. Only the individually true joint flags are asserted; no global background or existence theorem.')
with OUT.open('x')as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({k:report[k]for k in ['status','finished_utc','elapsed_seconds','checks']}),flush=True)
