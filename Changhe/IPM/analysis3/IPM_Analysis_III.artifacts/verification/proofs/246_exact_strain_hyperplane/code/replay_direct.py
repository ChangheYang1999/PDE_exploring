"""Independent direct-solve replay of the input-only metric bounds."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time
from flint import arb,arb_mat,ctx
ctx.prec=768
ctx.threads=1
P=Path(__file__).resolve().parents[1];R=P.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def val(q):q=F(q);return arb(q.numerator)/q.denominator
def ball(x):
 ends=[F(int(x[k][0]))*F(2)**int(x[k][1]) for k in ('lo_binary','hi_binary')]
 return val(sum(ends)/2)+arb(0,val((ends[1]-ends[0])/2).upper())
def positive_norm_squared(x,y):
 z=sum(x[i,0]*y[i,0] for i in range(x.nrows()));assert z>0;return z
start=time.monotonic()
cpath=R/'proofs/239_s1j1_full_input/evidence/check.json';c=json.loads(cpath.read_text())
rpath=R/'proofs/240_s1j1_high_intersections/evidence/exact_constraints.json';r=json.loads(rpath.read_text())
m=json.loads((R/'proofs/242_s1j1_completed_audit/evidence/source/meta.json').read_text())
g=arb_mat([[ball(e) for e in row] for row in c['runs'][1]['scaled_input_Gram']])
a=arb_mat([[ball(e)] for e in c['runs'][1]['exact_scaled_strain']]);b=arb_mat([[val(F.from_float(float(e)))] for e in m['cvec']])
res={}
for name,n in [('whole',38),('high_input',32),('high_graph',29)]:
 q=arb_mat([[int(i==j) for j in range(38)] for i in range(38)]) if name=='whole' else arb_mat([[val(e) for e in row] for row in r[name]['basis_columns']]).transpose()
 G=q.transpose()*g*q;A=q.transpose()*a;D=q.transpose()*(a-b)
 # Interval solves at higher precision, independent of the proposed whitener.
 solA=G.solve(A);solD=G.solve(D)
 an=positive_norm_squared(A,solA).sqrt();dn=positive_norm_squared(D,solD).sqrt();ratio=dn/an
 assert dn<val(F(3253,10**20));assert an>val(F(52024,10**6));assert ratio<val(F(6244,10**19))
 res[name]={'dual_strain_norm':an.str(50),'dual_difference_norm':dn.str(50),'relative_projection_bound':ratio.str(50)}
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS_DIRECT_METRIC_SOLVE_768_BITS','spaces':res,'uniform_directed_constants':{'functional_error_upper':'3253/10^20','strain_norm_lower':'52024/10^6','projection_error_upper':'6244/10^19'},'dependencies':{str(p.relative_to(R)):sha(p) for p in [cpath,rpath,P/'evidence/check.json']},'script_sha256':sha(Path(__file__)),'seconds':time.monotonic()-start,'scope':'Input only. No output matrix read.'}
(P/'evidence/direct_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
