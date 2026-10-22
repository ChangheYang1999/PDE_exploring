"""Exact Machin widths, source labels and minimum-location record checks."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,ast
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/flow_composition';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def f(x):return F(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def exact_arf(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def atan_box(x,N=40):
 s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(N)),F(0));t=s+(-1)**N*x**(2*N+1)/F(2*N+1);return min(s,t),max(s,t)
a,b=atan_box(F(1,5));c,d=atan_box(F(1,239));pl,pu=16*a-4*d,16*b-4*c
assert F(3)<pl<pu<F(355,113)
ctx.prec=512;ctx.threads=1;pi=arb.pi();pial,piau=exact_arf(pi.lower()),exact_arf(pi.upper());assert pl<=pial<=piau<=pu
widths=[];minimum=None;matches=[]
for ci in (0,4102,7808):
 with np.load(E/f'packet_{ci:04d}.npz',allow_pickle=False) as z:
  for ai,node in enumerate(z['nodes']):
   l,r,dep=map(int,node);dd=f(z['d'][ai]);factor=F(r-l,102400)
   assert pu*factor<=dd and piau*factor<=dd
   widths.append({'ci':ci,'angular_index':ai,'node':[l,r,dep],'d_exact':str(dd),'machin_width_margin_exact':str(dd-pu*factor),'arb_width_margin_exact':str(dd-piau*factor),'coarse_355_113_check':dd>=F(355,113)*factor})
 for method in ('exact','iv'):
  p=E/f'{method}_{ci:04d}.json';q=json.loads(p.read_text())
  for row in q['rows']:
   for result in row['ranges']:
    lo,hi=map(F,result['reference']);tl,th=map(F,result['target']);ms=[lo-tl,th-hi];assert ms==list(map(F,result['margins'])) and min(ms)>=0
    for side,margin in zip(['lower','upper'],ms):
     item={'method':method,'ci':ci,'angular_index':row['angular_index'],'node':row['node'],'function':result['name'],'endpoint':side,'margin_exact':str(margin),'record_sha256':sha(p)}
     if minimum is None or margin<F(minimum['margin_exact']):minimum=item
assert F(minimum['margin_exact'])==F(json.loads((E/'audit_outputs.json').read_text())['smallest_exact_inclusion_margin'])
p=B/'research/flow_certificate/evidence/source/cert_flow.py';text=p.read_text()
assert sha(p)=='bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6'
tree=ast.parse(text);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='FlowCertifier');fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='cell_bounds')
expected=['SP, remP = sums("cos", P)','SC, remC = sums("C", R)','SS, remS = sums("S", R)',
 's_q = [const(cl) - SP[0], MR(-SP[1].m, SP[1].r), MR(-SP[2].m, SP[2].r)]',
 's_lo, s_hi = tensor_range(*s_q, remP)',
 'v2_q = [s_q[k] + SC[k] for k in range(3)]',
 'v2_lo, v2_hi = tensor_range(*v2_q, succ(remP + remC))',
 'v1_q = [s_q[k] - SS[k] for k in range(3)]',
 'v1_lo, v1_hi = tensor_range(*v1_q, succ(remP + remS))',
 'T_q = [(SS[k] * MR.exact(-1.0)) * A_MR + SC[k] * B_MR + s_q[k] * muM for k in range(3)]',
 'one_cl = MR(1.0 + cl.m, succ(cl.r + 2 * U * (1 + abs(cl.m))))',
 'T_q[0] = T_q[0] - const(one_cl)',
 'T_lo, T_hi = tensor_range(*T_q, remT)',
 'return dict(s_lo=s_lo, s_hi=s_hi, v2y_lo=v2_lo, v2y_hi=v2_hi, v1x_lo=v1_lo, v1x_hi=v1_hi, T0_lo=T_lo, T0_hi=T_hi)']
for expr in expected:
 want=ast.dump(ast.parse(expr).body[0],include_attributes=False);nodes=[n for n in fn.body if ast.dump(n,include_attributes=False)==want];assert len(nodes)==1,expr;matches.append({'lineno':nodes[0].lineno,'source_statement':ast.get_source_segment(text,nodes[0])})
par=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAR' for t in n.targets));pars={q.arg:ast.literal_eval(q.value) for q in par.value.keywords};assert pars['a']==(129,20) and pars['b']==(307,100)
proofrec=json.loads((E/'proof_first.json').read_text());addrec=json.loads((E/'addendum_record.json').read_text());suprec=json.loads((E/'final_resolution_first.json').read_text());assert proofrec['proof_sha256']==sha(D/'PROOF.md') and addrec['addendum_sha256']==sha(D/'ADDENDUM.md') and suprec['proof_sha256']==sha(D/'FINAL_REVIEW_RESOLUTIONS.md')
files={str(x.relative_to(B)):sha(x) for x in [p,D/'PROOF.md',D/'ADDENDUM.md',D/'FINAL_REVIEW_RESOLUTIONS.md',E/'proof_first.json',E/'addendum_record.json',E/'final_resolution_first.json',E/'audit_outputs.json',Path(__file__)]}
for ci in (0,4102,7808):
 for name in [f'packet_{ci:04d}.npz',f'exact_{ci:04d}.json',f'iv_{ci:04d}.json']:
  pp=E/name;files[str(pp.relative_to(B))]=sha(pp)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SUPPLEMENTAL_EXACT_WIDTH_LABEL_AND_MARGIN_CHECKS','machin_pi_exact':[str(pl),str(pu)],'arb512_pi_exact':[str(pial),str(piau)],'width_checks':widths,'minimum_margin_location':minimum,'source_semantic_statements':matches,'source_parameters':{'a':list(pars['a']),'b':list(pars['b'])},'chronology':{'proof_first':proofrec['utc'],'addendum_record':addrec['utc'],'final_resolution_first':suprec['utc']},'files':files}
p=E/'final_checks.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'width_checks':len(widths),'source_statements':len(matches),'minimum_margin_location':minimum}))
