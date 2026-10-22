"""Explicit external input and physical partition binding for the geometry transfer."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,ast,math,time
import numpy as np
D=Path(__file__).resolve().parents[1];B=D.parents[1];P=B/'research/forcing_composed_cutoff';tic=time.monotonic()
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def ff(x):assert math.isfinite(x);return Q.from_float(float(x))
g=read(B/'research/localized_forcing/evidence/geometry_arb.json');green=Path(g['green_path']);trial=Path('numerics/data/trial_v2_h0.008.npz')
expected={'green':'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1','trial':'a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'}
assert sha(green)==expected['green']==g['green_sha256'] and sha(trial)==expected['trial']
part=B/'research/middle_residual/evidence/partition_exact.json';partition=read(part);points=[];last=None
for span in partition['spans']:
 a,z=Q(span['a_exact']),Q(span['b_exact']);n=span['count'];assert n>0 and a<z and span['first_cell']==len(points)
 if last is not None:assert a==last
 points.extend(a+(z-a)*j/n for j in range(n));last=z
points.append(last);assert len(points)==7810
with np.load(green,allow_pickle=False) as z:tb=z['tb'];tr=z['tb_rad']
assert len(tb)==len(tr)==7810
for p,t,r in zip(points,tb,tr):assert ff(r)>=0 and ff(t)-ff(r)<=p<=ff(t)+ff(r)
local=0
for c in g['cells']:
 i=c['ci'];assert ff(c['tb'])==ff(tb[i]) and ff(c['tb_rad'])==ff(tr[i]);assert ff(c['next_tb'])==ff(tb[i+1]) and ff(c['next_tb_rad'])==ff(tr[i+1]);local+=4
assert local==52
# Exact source statements and evaluated binary constants, not a filename comparison.
assignments=[];constants={}
for label,root in [('prior',P),('v22',D)]:
 src=root/'source/src/cert_forcing.py';tree=ast.parse(src.read_text());nodes=[]
 for n in tree.body:
  if isinstance(n,ast.Assign) and any(any(isinstance(t,ast.Name) and t.id in {'XSTAR_LO','XSTAR_HI','XSTAR','XRAD'} for t in ast.walk(target)) for target in n.targets):nodes.append(n)
 assert len(nodes)==3
 ns={'np':np};exec(compile(ast.Module(body=nodes,type_ignores=[]),'selected_source_constants','exec'),ns)
 constants[label]={k:float(ns[k]).hex() for k in ['XSTAR_LO','XSTAR_HI','XSTAR','XRAD']}
 assignments.append([ast.dump(n,include_attributes=False) for n in nodes])
 assert ff(ns['XRAD'])>=0 and ff(ns['XSTAR'])-ff(ns['XRAD'])<=ff(ns['XSTAR_LO'])<=ff(ns['XSTAR_HI'])<=ff(ns['XSTAR'])+ff(ns['XRAD'])
assert assignments[0]==assignments[1] and constants['prior']==constants['v22']
raw=read(D/'source/runs/forcing/v22_p9_merged.json');assert list(map(float.fromhex,[constants['v22']['XSTAR_LO'],constants['v22']['XSTAR_HI']]))==raw['x_star_bracket']
# Do not silently claim a missing source definition has been compared.
old=ast.parse((P/'source/src/cert_forcing2.py').read_text());new=ast.parse((D/'source/src/cert_forcing2.py').read_text());bodies={}
for name in ['cart_derivative_table','faa_di_bruno_tables','Recentre','add_const']:
 aa=[n for n in old.body if getattr(n,'name',None)==name];bb=[n for n in new.body if getattr(n,'name',None)==name]
 if not aa and not bb:bodies[name]='ABSENT_BOTH_NO_INHERITED_CLAIM';continue
 assert len(aa)==len(bb)==1 and ast.dump(aa[0],include_attributes=False)==ast.dump(bb[0],include_attributes=False)
 bodies[name]='IDENTICAL_AST:'+hashlib.sha256(ast.dump(bb[0],include_attributes=False).encode()).hexdigest()
# Check the cited jet producer and consumer names occur in the exact frozen files.
rtext=(D/'source/src/cert_resid.py').read_text();r_tree=ast.parse(rtext);r_nodes=[n for n in r_tree.body if isinstance(n,ast.FunctionDef) and n.name=='_cell_core_deriv'];assert len(r_nodes)==1
src2=(D/'source/src/cert_forcing2.py').read_text();assert 'eps = C._last_eps' in src2 and 'C.cell_core_deriv(' in src2 and 'C = Certifier(green, trial, Q=12)' in src2
assert 'Certifier.cell_core_deriv = _cell_core_deriv' in rtext and 'self._last_eps = eps' in rtext
assert sha(green)==expected['green'] and sha(trial)==expected['trial']
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tic,status='PASS_V22_EXTERNAL_INPUT_CANONICAL_GEOMETRY_AND_SOURCE_BINDING',external_inputs={k:{'path':str(v),'sha256':expected[k],'bytes':v.stat().st_size,'checks_before_and_after':True} for k,v in [('green',green),('trial',trial)]},canonical_points_checked=7810,local_endpoint_equalities=local,partition_sha256=sha(part),constants=constants,source_constant_assignments_identical=True,source_bodies=bodies,residual_producer='_cell_core_deriv -> self._last_eps -> C._last_eps',source_sha256={p.name:sha(p) for p in (D/'source/src').iterdir() if p.is_file()},scope='The new certificate is interpreted on this exact canonical partition and source bracket. Current external inputs are explicitly pinned and agree with the prior geometry proof. No historical runtime attestation, residual coefficient soundness or physical forcing norm follows.')
(D/'evidence/source_geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],'seconds')
