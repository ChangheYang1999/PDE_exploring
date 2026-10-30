"""Independent exact 25/100 pole, raw-shape and recorded-objective audit."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import ast,hashlib,json,re,shlex,sys,time
from flint import fmpq_poly as Poly, fmpq
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic();checks=[];inputs={}
def read(p,h=None):
 d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p)]=d
 return json.loads(p.read_text())
manifest=read(B/'data/manifest.json');assert sha(B/'PROOF.md')==manifest['proof_sha256']
for name,row in manifest['inputs'].items():assert sha(B/name)==row['sha256'];inputs[str(B/name)]=row['sha256']
a=read(B/'data/candidate023.json','d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df')
p=read(B/'data/phase1.json','637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb')
parent=read(R/'higher_mode_rank_audit/data/parent016.json','a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
old=read(B/'data/old_basis.json');rank=read(B/'source/T4_prior_rank.json');assert rank['verdict'].startswith('CONFIRMED')
for path,h in rank['inputs'].items():assert sha(Path(path))==h;inputs[path]=h
shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
scaled=lambda r:[(j,m,('legqs',0,n,4,r)) for j in (1,2,3) for m in range(9,16) for n in range(12)]
olds=list(map(shape,old['generators']));expected=olds+scaled(25)+scaled(100)
assert len(olds)==len(set(olds))==1922
assert list(map(shape,parent['generators']))==olds+scaled(25)
assert list(map(shape,p['generators']))==list(map(shape,a['generators']))==expected
assert len(expected)==len(set(expected))==2426
checks.append('all2426 actual and phase-one ordered shapes; parent016')
c=Q(a['cl_exact']);assert c==Q(p['cl_exact'])==Q(parent['cl_exact'])==Q(4076476460239181,2251799813685248)
gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)]
diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
assert all(v.denominator!=1 for v in ps+diffs) and 3+gamma<4
peer=read(B/'source/N4_result.json','12ea208edba6115273b8cf65766c50d29cac0e92379c902d919661a0e742ecb2')
assert list(map(str,ps))==peer['branch_exponents'] and list(map(str,diffs))==peer['noninteger_differences']
checks.append('all36 noninteger conditions and growth below4')
peerw={(w['scale'],w['m'],w['N']):Q(w['Laurent_coefficient']) for w in peer['Laurent_witnesses']}
v=Poly([0,1]);witnesses=[];cross=[]
for scale,other in [(25,100),(100,25)]:
 slope=scale*scale-1;v0=fmpq(-1,slope);L=1+slope*v;Z=2*(1-v)-L
 h0=Poly([1]);h1=Z;hom=[h0,h1]
 for n in range(1,11):hom.append(((2*n+1)*Z*hom[-1]-n*L**2*hom[-2])/(n+1))
 crossvalue=1-Q(other*other-1,slope);assert crossvalue!=0
 cross.append({'scale':scale,'other_scale':other,'other_denominator':str(crossvalue)})
 for m in range(9,16):
  for n in range(12):
   numerator=scale**8*v**4*(1-v)**m*hom[n]
   expanded=Q(str(numerator(v0)/slope**(4+n)))
   pole=Q(-1,slope);formula=scale**8*pole**4*comb(2*n,n)*(1-pole)**(m+n)/slope**(4+n)
   assert expanded==formula==peerw[scale,m,n] and expanded!=0
   witnesses.append({'scale':scale,'m':m,'N':n,'pole_order':4+n,'coefficient':str(expanded),'recurrence_equals_formula':True})
assert len(witnesses)==168;checks.append('168 homogenized Legendre recurrence witnesses and two distinct poles')
rows=lambda d:[(1,k) if isinstance(k,int) else tuple(k) for k in d['meta']['pair_k']]
n1=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
objective=[(1,k) for k in n1]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in (0,8,32,128,512)]
assert rows(parent)==rows(p)==rows(a)==objective and len(objective)==len(set(objective))==67
script=(B/'source/N1_chain023.sh').read_text();tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1)
calls=[]
for line in script.splitlines():
 if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
  words=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));calls.append(words[words.index('run_quot.py')+1:])
assert len(calls)==2
for call,d,steps,fn in zip(calls,(p,a),(12,28),('N1_023_phase1.out','N1_023_phase2.out'),strict=True):
 assert [(tuple(map(int,z.split(':'))) if ':' in z else (1,int(z))) for z in call[9].split(',')]==objective
 meta=d['meta'];assert Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag']
 for i,key,value in [(1,'angular_midpoint',180),(2,'steps',steps),(5,'middle_order',16)]:assert int(call[i])==meta[key]==value
 for i,key,value in [(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)]:assert Q(call[i])==Q(str(meta[key]))==value
 assert Q(call[4])==Q(str(meta['hw']))==Q('0.952380952380952')
 assert call[10]==meta['pair_mode']=='penalty'
 text=(B/'source'/fn).read_text();assert [int(x) for x in re.findall(r'^it\s+(\d+) obj ',text,re.M)]==list(range(1,steps+1))
 assert sha(B/('data/phase1.json' if steps==12 else 'data/candidate023.json')) in text
 assert 'generators 2426' in text and 'pair rows 67 weight 1000000000000.0' in text and 'per-row weights:' not in text
 checks.append(str(steps)+' recorded iterations and exact displayed launch parameters')
assert p['meta']['parent_json']=='quot013_legqs25_m9to15_cpu_m16_exact.json'
assert a['meta']['parent_json']=='legqs25p100_m9to15_gpu_m16_s12_exact.json'
assert p['meta']['added_legqs']=='1,2,3:9:15:100:12' and a['meta']['added_legqs'] is None
beforepath=R/'candidate021_shapes/source/N1_run_quot020.py';before=beforepath.read_text();inputs[str(beforepath)]=sha(beforepath)
after=(B/'source/N1_run_quot.py').read_text();parts=[]
for text in (before,after):
 tree=ast.parse(text);parsers=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='_parse']
 assigns=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in n.targets)]
 assert len(parsers)==len(assigns)==1;parts.append((ast.dump(parsers[0],include_attributes=False),ast.dump(assigns[0],include_attributes=False)))
 assert any(isinstance(n,ast.Call) and any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in n.keywords) for n in ast.walk(tree))
assert parts[0]==parts[1]
impl=(B/'source/N1_ipm_opt3.py').read_text();ast.parse(impl);assert 'for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl
checks.append('unchanged row parser and objective propagation inspected as text')
reg=read(B/'source/register.json');sm=read(B/'source/snapshot_manifest.json')
assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:46:00+00:00')<datetime.fromisoformat(sm['created_utc'].replace('Z','+00:00'))
probes=[tuple(x) for x in reg['pairs']]+[(n,(n-1)//2+s) for n in range(19,32,2) for s in (0,8,32,128,512)]
assert len(probes)==len(set(probes))==60
assert all(n>17 and n%2 and k>=(n-1)//2 and all(n!=j for j,l in objective) for n,k in probes)
assert peer['raw_sha256']==sha(B/'data/candidate023.json') and peer['potential_dimension']==peer['density_dimension']==2426 and peer['recorded_iterations']==[12,28]
assert peer['exact_objective_rows']==[list(x) for x in objective] and {(r['n'],r['K']) for r in peer['probe_rows']}==set(probes)
checks.append('public25 register timing and all60 probes outside analytic span')
for f in (B/'PROOF.md',Path(__file__)):inputs[str(f)]=sha(f)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'raw_sha256':sha(B/'data/candidate023.json'),'potential_dimension':2426,'density_dimension':2426,'recorded_iterations':[12,28],'exact_objective_rows':objective,'outside_analytic_span':probes,'Laurent_witnesses':witnesses,'cross_poles':cross,'publisher_code_executed':False,'scope':'Parent016 and two recorded023 stages; earlier history not independently replayed; no statistical-independence claim','verdict':'CONFIRMED actual2426-dimensional potential and density spaces, fresh25/100 pole certificate, and67-row analytic span'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],len(checks),len(witnesses),out['elapsed_seconds'],sha(B/'verification/result.json'))
