"""Independent binding of actual022 to the accepted abstract dimension."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,hashlib,json,shlex,re,time,sys
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic();inputs={};checks=[]
def read(p,h=None):
 d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p)]=d
 return json.loads(p.read_text())
man=read(B/'data/manifest.json')
assert sha(B/'PROOF.md')==man['proof_sha256']
for name,row in man['inputs'].items():assert sha(B/name)==row['sha256'];inputs[str(B/name)]=row['sha256']
a=read(B/'data/candidate022.json','85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f')
p=read(B/'data/phase1.json','2a13c07969eb37af27c68a0336fa7f28a9f1747119e1f7ad4623302f58d5fd4f')
old=read(R/'higher_mode_rank_audit/data/parent016.json','a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
rank=read(R/'higher_mode_rank_audit/verification/result.json')
assert rank['verdict'].startswith('CONFIRMED')
for path,h in rank['inputs'].items():
 f=Path(path) if Path(path).is_absolute() else R/'higher_mode_rank_audit'/path
 assert sha(f)==h;inputs[str(f)]=h
abstract=read(R/'higher_mode_rank_audit/source/N4_shapes.json')
shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
actual=list(map(shape,a['generators']));base=list(map(shape,old['generators']))
blocks=[(1,m) for m in range(16,20)]+[(j,m) for j in (2,3) for m in range(16,24)]
extra=[(j,m,('legqs',0,k,4,25)) for j,m in blocks for k in range(12)]
assert actual==list(map(shape,p['generators']))==list(map(shape,abstract['generators']))==base+extra
assert len(actual)==len(set(actual))==rank['potential_dimension']==rank['density_dimension']==2414
assert Q(a['cl_exact'])==Q(p['cl_exact'])==Q(old['cl_exact'])==Q(4076476460239181,2251799813685248)
checks+=['all2414 shapes and exact c','phase-one and final shapes equal accepted abstract list']
rows=lambda d:[(1,k) if isinstance(k,int) else tuple(k) for k in d['meta']['pair_k']]
expected=rows(old)
assert rows(a)==rows(p)==expected and len(expected)==len(set(expected))==67
n1=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
assert expected==[(1,k) for k in n1]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in (0,8,32,128,512)]
script=(B/'source/N1_chain022.sh').read_text()
calls=[]
for line in script.splitlines():
 if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
  words=shlex.split(line);calls.append(words[words.index('run_quot.py')+1:])
assert len(calls)==2
for call,d,steps,fn in zip(calls,(p,a),(12,28),('N1_022_phase1.out','N1_022_phase2.out')):
 rr=[tuple(map(int,v.split(':'))) if ':' in v else (1,int(v)) for v in call[9].split(',')]
 assert rr==expected
 meta=d['meta']
 for i,key,value in [(1,'angular_midpoint',180),(2,'steps',steps),(5,'middle_order',16)]:assert int(call[i])==meta[key]==value
 for i,key,value in [(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)]:assert Q(call[i])==Q(str(meta[key]))==value
 assert call[10]==meta['pair_mode']=='penalty'
 text=(B/'source'/fn).read_text();iterations=[int(x) for x in re.findall(r'^it\s+(\d+) obj ',text,re.M)]
 assert iterations==list(range(1,steps+1))
 assert sha(B/('data/phase1.json' if steps==12 else 'data/candidate022.json')) in text
 assert 'generators 2414' in text and 'pair rows 67 weight 1000000000000.0' in text
 checks.append(str(steps)+' recorded iterations and launch parameters')
assert p['meta']['parent_json']=='quot013_legqs25_m9to15_cpu_m16_exact.json'
assert a['meta']['parent_json']=='legqs25_m16to23_gpu_m16_s12_exact.json'
assert p['meta']['added_legqs']=='1,2,3:16:23:25:12' and a['meta']['added_legqs'] is None
checks.append('exact two-stage lineage and addition only in first stage')
oldpath=R/'candidate021_shapes/source/N1_run_quot020.py';before=oldpath.read_text();inputs[str(oldpath)]=sha(oldpath)
after=(B/'source/N1_run_quot.py').read_text()
parts=[]
for text in (before,after):
 tree=ast.parse(text)
 parsers=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='_parse']
 assigns=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in n.targets)]
 assert len(parsers)==len(assigns)==1
 parts.append((ast.dump(parsers[0],include_attributes=False),ast.dump(assigns[0],include_attributes=False)))
 assert any(isinstance(n,ast.Call) and any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in n.keywords) for n in ast.walk(tree))
assert parts[0]==parts[1];checks.append('unchanged current row parser inspected as text')
c=Q(a['cl_exact']);p1=(3+1/c-(1-1/c))/2
witness=4*33*32*(p1-16-Q(4,625))
assert str(witness)==rank['density31_origin_coefficient'] and witness!=0
manifest=read(B/'source/snapshot_manifest.json')
assert 'outside the N4-160 n <= 31 sweep' in manifest['notes']
support=sorted({2*m+s for j,m in blocks for s in (-1,1)})
assert support==list(range(31,48,2));checks.append('mode31 witness refutes full-support disjointness')
reg=read(B/'source/register.json')
assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:32:00+00:00')<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
probes=[tuple(x) for x in reg['pairs']]+[(n,(n-1)//2+s) for n in range(19,32,2) for s in (0,8,32,128,512)]
assert len(probes)==len(set(probes))==60
assert all(n>17 and n%2 and k>=(n-1)//2 and (n,k) not in expected for n,k in probes)
checks.append('all25 registered and35 diagnostic probes outside analytic span')
peer=read(B/'source/N4_result.json')
assert peer['raw_sha256']==sha(B/'data/candidate022.json')
assert peer['potential_dimension']==peer['density_dimension']==2414 and peer['recorded_iterations']==[12,28]
assert peer['density31_origin_coefficient']==str(witness)
assert peer['exact_objective_rows']==[list(x) for x in expected]
assert {(r['n'],r['K']) for r in peer['probe_rows']}==set(probes)
for f in (B/'PROOF.md',Path(__file__)):inputs[str(f)]=sha(f)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,
 'raw_sha256':sha(B/'data/candidate022.json'),'potential_dimension':2414,'density_dimension':2414,'recorded_iterations':[12,28],
 'all_actual_shapes_equal_accepted_abstract':True,'exact_objective_rows':expected,'outside_analytic_span':probes,
 'density31_origin_coefficient':str(witness),'density_new_mode_support':support,'publisher_code_executed':False,
 'scope':'Parent016 and two recorded022 stages; earlier history not replayed; no statistical-independence claim',
 'verdict':'CONFIRMED actual dimension and67-row span; REFUTED complete support outside the through31 sweep'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'))
