"""Independent saved-input checks: exact inner LDL and existing pure block."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib
from flint import ctx
ROOT=Path(__file__).resolve().parents[3];TOP=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('pack_reader',ROOT/'proofs/198_pure_spline_input_gram/code/check.py');r=importlib.util.module_from_spec(sp);sp.loader.exec_module(r);ctx.prec=768;ctx.threads=1
q=json.loads((TOP/'evidence/check.json').read_text());e=json.loads((TOP/'evidence/exact_inputs.json').read_text())
assert r.sha(TOP/'code/check.py')==q['script_sha256'];assert r.sha(TOP/'PROOF.md')==q['proof_sha256']
for p,h in q['dependencies'].items():assert r.sha(ROOT/p)==h
R=[[F(x) for x in row] for row in e['inner_radial_Gram']];L=[[F(i==j) for j in range(7)] for i in range(7)];D=[]
for i in range(7):
 d=R[i][i]-sum(L[i][j]**2*D[j] for j in range(i));assert d>0;D.append(d)
 for v in range(i+1,7):L[v][i]=(R[v][i]-sum(L[v][j]*L[i][j]*D[j] for j in range(i)))/d
assert all(R[i][j]==sum(L[i][v]*D[v]*L[j][v] for v in range(7)) for i in range(7) for j in range(7))
oldpath=ROOT/'proofs/198_pure_spline_input_gram/evidence/gram_512_640.json';old=json.loads(oldpath.read_text())['runs']['S1M4P'];decl=old['basis_declaration'];lookup={bi:j for j,(bi,m,s) in enumerate(decl) if m==1};assert sorted(lookup)==list(range(4,30))
G=q['runs'][1]['scaled_input_Gram'];overlaps=0
for bi in range(4,30):
 i=bi+3;oi=lookup[bi];s=F(e['scales'][i]);os=F(decl[oi][2])
 for bj in range(4,30):
  j=bj+3;oj=lookup[bj];t=F(e['scales'][j]);ot=F(decl[oj][2]);assert r.unpack(G[i][j]).overlaps(r.unpack(old['exact_scaled_input_Gram'][oi][oj])*r.aa(os*ot/(s*t)));overlaps+=1
assert r.unpack(q['runs'][1]['maximum_stored_strain_absolute_error'])<r.aa(F(2053,10**20))
assert r.unpack(q['runs'][1]['maximum_stored_nonzero_strain_relative_error'])<r.aa(F(2701,10**19))
out={'date':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_INPUT_ONLY','check_sha256':r.sha(TOP/'evidence/check.json'),'exact_inputs_sha256':r.sha(TOP/'evidence/exact_inputs.json'),'script_sha256':r.sha(__file__),'existing_pure_Gram_sha256':r.sha(oldpath),'exact_positive_inner_LDL':list(map(str,D)),'pure_Gram_overlap_checks':overlaps,'precision_bits':768,'stored_strain_absolute_bound':'2053/10^20','stored_strain_relative_bound':'2701/10^19','scope':'Full exact input only, no output/complement claim.'}
(TOP/'evidence/audit_saved.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='exact_positive_inner_LDL'},indent=2))
