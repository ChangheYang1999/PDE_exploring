"""Independent one-pole expansion, unchanged ordered shapes and recorded row history."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from math import comb
from datetime import datetime,timezone
import ast,hashlib,json,re,shlex,sys,time
from flint import fmpq_poly as Poly,fmpq
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic();checks=[];inputs={}
def read(p,h=None):
 digest=sha(p);assert h is None or digest==h,(p,h,digest);inputs[str(p)]=digest
 return json.loads(p.read_text())
def check(label,condition):
 assert condition,label
 checks.append(label)
man=read(B/'data/manifest.json');check('proof binding',sha(B/'PROOF.md')==man['proof_sha256'])
for name,row in man['inputs'].items():check('input '+name,sha(B/name)==row['sha256']);inputs[str(B/name)]=row['sha256']
a=read(B/'data/candidate026.json','2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3')
quot=read(B/'data/quotient013.json','c0d3536ea961908a8a4d251054192bad0b5b2534435e3c8224fe0424bda5f7fe')
parent=read(B/'data/parent022.json','85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f')
old=read(B/'data/old_basis.json');rank=read(B/'source/T4_prior_rank.json')
check('prior2414 rank through accepted022',rank['potential_dimension']==2414 and rank['density_dimension']==2414 and rank['verdict'].startswith('CONFIRMED'))
for path,h in rank['inputs'].items():check('rank dependency '+path,sha(Path(path))==h);inputs[path]=h
shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
base=list(map(shape,quot['generators']));scaled=lambda scale:[(j,m,('legqs',0,n,4,scale)) for j in (1,2,3) for m in range(9,16) for n in range(12)]
high=[(j,m,('legqs',0,n,4,25)) for j in (1,2,3) for m in range(16,20 if j==1 else 24) for n in range(12)]
expected=base+scaled(25)+high
check('old1922 set',len(base)==len(set(base))==1922 and set(base)==set(map(shape,old['generators'])))
check('parent022 ordered shapes',list(map(shape,parent['generators']))==expected)
check('all2414 actual ordered shapes',list(map(shape,a['generators']))==expected and len(expected)==len(set(expected))==2414 and len(high)==240)
check('exact rational coefficients',all(Q(g['coef']).denominator>0 for g in a['generators']))
c=Q(a['cl_exact']);check('common c',c==Q(parent['cl_exact'])==Q(quot['cl_exact'])==Q(4076476460239181,2251799813685248))
gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)];diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
check('36 noninteger conditions and growth',all(v.denominator!=1 for v in ps+diffs) and 3+gamma<4)
v=Poly([0,1]);witnesses=[];cross=[]
for scale in (25,):
 slope=scale*scale-1;v0=fmpq(-1,slope);L=1+slope*v;Z=2*(1-v)-L
 hom=[Poly([1]),Z]
 for n in range(1,11):hom.append(((2*n+1)*Z*hom[-1]-n*L**2*hom[-2])/(n+1))
 for other in (r for r in (25,) if r!=scale):
  val=1-Q(other*other-1,slope);check('distinct poles '+str((scale,other)),val!=0)
  cross.append({'scale':scale,'other_scale':other,'other_denominator':str(val)})
 for m,n in sorted({(m,spec[2]) for j,m,spec in expected if spec[0]=='legqs' and spec[4]==scale}):
  numerator=scale**8*v**4*(1-v)**m*hom[n]
  expanded=Q(str(numerator(v0)/slope**(4+n)));pole=Q(-1,slope)
  formula=scale**8*pole**4*comb(2*n,n)*(1-pole)**(m+n)/slope**(4+n)
  check('pole recurrence '+str((scale,m,n)),expanded==formula and expanded!=0)
  witnesses.append({'scale':scale,'m':m,'N':n,'pole_order':4+n,'coefficient':str(expanded),'recurrence_equals_formula':True})
check('all180 witnesses and zero crosspoles',len(witnesses)==180 and len(cross)==0)
rows=lambda x:[(1,k) if isinstance(k,int) else tuple(k) for k in x['meta']['pair_k']]
first=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
base_rows=[(1,k) for k in first]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in (0,8,32,128,512)]
heldin=[(n,(n-1)//2+s) for s in (128,512) for n in range(19,32,2)];objective=base_rows+heldin
check('actual81 and parent67 rows',rows(a)==objective and rows(parent)==base_rows and len(set(objective))==81)
text=(B/'source/N1_chain026.sh').read_text();tag=re.search(r'^TAG=([^\s]+)$',text,re.M).group(1);calls=[]
for line in text.splitlines():
 if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
  words=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));args=words[words.index('run_quot.py')+1:];check('redirection suffix',args[-3]=='>' and args[-1]=='2>&1');calls.append(args[:-3])
check('one recorded call',len(calls)==1 and len(calls[0])==11);call=calls[0];meta=a['meta']
check('immediate022 and no additions',meta['parent_json']==Path(call[0]).name=='legqs25_m16to23_gpu_m16_exact.json' and meta['added_legqs'] is None and meta['quotient_meta'] is None)
check('tag and mode',meta['tag']==call[3] and meta['pair_mode']==call[10]=='penalty')
for i,key,want in [(1,'angular_midpoint',180),(2,'steps',60),(5,'middle_order',16),(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)]:check(key,Q(call[i])==Q(str(meta[key]))==want)
check('same hw',Q(call[4])==Q(str(meta['hw']))==Q(str(parent['meta']['hw'])))
check('split weights metadata',meta['n_heldin_rows']==14 and Q(str(meta['wpair_heldin']))==10**16 and meta['desc_zero']==[0,1,2])
check('all launch rows',[(tuple(map(int,z.split(':'))) if ':' in z else (1,int(z))) for z in call[9].split(',')]==objective)
for literal in ['IPM_DEVICE=cuda','IPM_STEPNORM=1','IPM_NHELDIN=14','IPM_WPAIR_HELDIN=1e16']:check('launch '+literal,literal in text)
source=(B/'source/N1_run_quot.py').read_text();ast.parse(source)
for literal in ["PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))",'pair_k=PAIRK','wpair=WLIST','[WPAIR]*(len(PAIRK)-NHELD) + [WHELD]*NHELD','a0 = np.r_[a0, np.zeros(added)]',"sp = ['legqs', w, n, 4, R0]",'w = max(5-m, 0)','a_start = prob.taylor_project(a0, iters=8)']:check('optimizer literal '+literal,literal in source)
check('initial projection before optimize',source.index('a_start = prob.taylor_project')<source.index('optimize2'))
impl=(B/'source/N1_ipm_opt3.py').read_text();ast.parse(impl)
check('weighted rows and meshstep implementation','for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl and 'dRho2' in impl)
log=(B/'source/N1_026.out').read_text()
for literal in [sha(B/'data/candidate026.json'),'generators 2414','pair rows 81 weight 1000000000000.0','per-row weights: first 67 rows 1000000000000.0 ; last 14 rows 1e+16','constraint rows 421','midpoint 180, middle 16']:check('log '+literal,literal in log)
pattern=r'^it\s+(\d+) obj (\S+) -> (\S+) (ACC|rej) pred (\S+) lam (\S+) dRho2 (\S+) dCoef (\S+) '
iters=[dict(zip(['i','before','proposal','flag','pred','lambda','dRho2','dCoef'],z)) for z in re.findall(pattern,log,re.M)]
for z in iters:z['i']=int(z['i']);check('nonnegative displayed steps '+str(z['i']),Decimal(z['dRho2'])>=0 and Decimal(z['dCoef'])>=0)
accepted=[z for z in iters if z['flag']=='ACC'];check('60 attempts', [z['i'] for z in iters]==list(range(1,61)))
check('40 accepted20 rejected',len(accepted)==40)
step_sum=sum((Decimal(z['dRho2']) for z in accepted),Decimal(0))
reg=read(B/'source/register.json');heldpath=B/'source/N1_HELDOUT_026.md';held=heldpath.read_text()
check('heldout hash',sha(heldpath)=='2016d960c982aeffa2b1bef5aaece9b7394e97139d9688b5f6abec3274606d15')
probes=[tuple(map(int,x)) for line in held.splitlines() if line.startswith('- the ') for x in re.findall(r'(\d+):(\d+)',line)]
expected_probes=[tuple(x) for x in reg['pairs']]+[(n,(n-1)//2+s) for n in range(19,32,2) for s in (0,8,32)]
check('all46 probes',probes==expected_probes and len(set(probes))==46)
for n,k in probes:
 powers=[l for j,l in objective if j==n]
 check('analytic nonmember '+str((n,k)),powers==[(n-1)//2+128,(n-1)//2+512] and k not in powers and k>=(n-1)//2 and n%2==1)
check('public register before recorded launch',datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T11:31:00+00:00'))
check('recorded launch in worklog','chain026 launched 11:31Z' in (B/'source/N1_WORKLOG.md').read_text())
sm=read(B/'source/snapshot_manifest.json');check('snapshot identity',sm['id']=='C1-N1-026-heldin1e16-legqs25-m16to23' and sm['basis']['generator_count']==2414 and a['n_free']==2414 and a['n_fixed']==0)
check('per-step projection before norm',impl.index('if taylor: a_new = self.taylor_project(a_new)') < impl.index("drho = self.fields(a_new - a)"))
file_checks=[]
snapshot=B.parents[1]/'../c1-shared/candidate_snapshots/C1-N1-026-heldin1e16-legqs25-m16to23'
for line in (B/'source/SHA256SUMS').read_text().splitlines():
 digest,name=line.split(maxsplit=1); name=name.lstrip('*'); check('snapshot file '+name,sha(snapshot/name)==digest);file_checks.append({'name':name,'sha256':digest})
check('six snapshot files',len(file_checks)==6)
for p in [B/'PROOF.md',Path(__file__)]:inputs[str(p)]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'check_count':len(checks),'raw_sha256':sha(B/'data/candidate026.json'),'potential_dimension':2414,'density_dimension':2414,'dimension_scope':'Full spaces before421 recorded constraints; no tangent rank claim','branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),'exact_objective_rows':objective,'objective_weights_exact':[str(10**12)]*67+[str(10**16)]*14,'outside_analytic_span':probes,'Laurent_witnesses':witnesses,'cross_poles':cross,'iterations':iters,'attempted':60,'accepted':40,'rejected':20,'FLOAT_sum_accepted_rounded_mesh_steps':str(step_sum),'step_scope':'Rounded mesh values include per-step Taylor projection; initial projection, final exact conversion and integration error excluded','heldout_sha256':sha(heldpath),'publisher_code_executed':False,'snapshot_files':file_checks,'independent_N4_comparison':'Peer records frozen; detailed comparison is separate','verdict':'CONFIRMED unchanged actual2414-dimensional spaces, one-pole witnesses and81-row analytic span'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],len(checks),len(witnesses),out['elapsed_seconds'],sha(B/'verification/result.json'),step_sum)
