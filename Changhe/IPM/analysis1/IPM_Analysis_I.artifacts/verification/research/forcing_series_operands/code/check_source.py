"""Bind all saved scalar operands to selected frozen source expressions."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,copy,hashlib,json,sys,time,math
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S));tic=time.monotonic();ctx.prec=128
from midrad import MR,U,succ
from cert_forcing import Cell,BiTM,XSTAR,XRAD
from cert_forcing2 import add_const
ff=lambda x:Q.from_float(float(x))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
reg=json.loads((D/'evidence/regeneration.json').read_text());rows=json.loads((D/'evidence/blocks.json').read_text());assert len(rows)==832
for f,h in reg['pins'].items():assert sha(B/f)==h,f
src=(S/'cert_forcing2.py').read_text();tree=ast.parse(src);main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
def expression(name):
 nodes=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(ast.unparse(t)==name for t in n.targets)];assert len(nodes)==1,(name,len(nodes));return nodes[0].value
names=['c0','uq','Umax','xr','tail','coef'];expr={k:expression(k) for k in names}
first=next(n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(ast.unparse(t)=='Wb' for t in n.targets) and isinstance(n.value,ast.Call) and ast.unparse(n.value.func)=='pw[0].scale');expr['coef0']=first.value.args[0]
for k in reg['source_expressions']:assert ast.unparse(expr[k])==reg['source_expressions'][k],k
compiled={k:compile(ast.Expression(body=copy.deepcopy(v)),'frozen_'+k,'eval') for k,v in expr.items()}
base={'float':float,'succ':succ,'U':U,'arb':arb,'MR':MR,'comb':math.comb,'Kser':16,'add_const':add_const};counts={k:0 for k in expr};uq_arrays=0
with np.load(D/'evidence/operands.npz',allow_pickle=False) as z:d={k:z[k].copy() for k in z.files}
for n,r in enumerate(rows):
 ci,q,bs,bp=[r[k] for k in ['ci','q','bs','bp']];assert tuple(d['indices'][n])==(ci,q,bs,bp)
 cell=Cell(r['H'],r['W'],12,8);qb=BiTM(MR(d['q_mid'][n].copy(),d['q_rad'][n].copy()),float(d['q_rem'][n]),cell);ns=dict(base,qb=qb)
 c0=eval(compiled['c0'],ns);assert c0==r['c0']==float(d['q_mid'][n,0,0]);counts['c0']+=1;ns['c0']=c0
 uq=eval(compiled['uq'],ns);assert np.array_equal(uq.c.m,d['uq_mid'][n]) and np.array_equal(uq.c.r,d['uq_rad'][n]) and uq.r==d['uq_rem'][n];counts['uq']+=1;uq_arrays+=235;ns['uq']=uq
 Umax=eval(compiled['Umax'],ns);assert Umax==r['Umax'];counts['Umax']+=1;ns['Umax']=Umax
 xr=eval(compiled['xr'],ns);assert xr==r['xr'];counts['xr']+=1;ns['xr']=xr
 assert bool(xr<0.6)==r['active'];assert c0>0
 if r['active']:
  ns['c0a']=arb(c0);tail=eval(compiled['tail'],ns);assert tail==r['tail'];counts['tail']+=1
  z=eval(compiled['coef0'],ns);assert float(z.m)==d['coef_mid'][n,0] and float(z.r)==d['coef_rad'][n,0];counts['coef0']+=1
  for k in range(1,17):
   ns['k']=k;z=eval(compiled['coef'],ns);assert float(z.m)==d['coef_mid'][n,k] and float(z.r)==d['coef_rad'][n,k];counts['coef']+=1
 else:assert r['tail']==0 and (d['coef_mid'][n]==0).all() and (d['coef_rad'][n]==0).all()
# Reconstruct the exact partition independently of the saved local geometry.
part=json.loads((B/'research/middle_residual/evidence/partition_exact.json').read_text());pts=[];last=None
for s in part['spans']:
 a,z=Q(s['a_exact']),Q(s['b_exact']);count=s['count'];assert count>0 and a<z and s['first_cell']==len(pts)
 if last is not None:assert last==a
 pts.extend(a+(z-a)*j/count for j in range(count));last=z
pts.append(last);assert len(pts)==7810
G=Path('numerics/data/cert_green.npz')
with np.load(G,allow_pickle=False) as z:tb=z['tb'][4096:4110].copy();tr=z['tb_rad'][4096:4110].copy()
for i in range(14):assert ff(tb[i])-ff(tr[i])<=pts[4096+i]<=ff(tb[i])+ff(tr[i])
for r in rows:
 i=r['ci']-4096;assert r['tb']==float(tb[i]) and r['tb_rad']==float(tr[i]);assert pts[r['ci']+1]-pts[r['ci']]<=ff(r['h'])<=64*ff(r['hk']);assert ff(r['H'])==32*ff(r['hk']) and ff(r['W'])==2*ff(r['wk'])
assert {(r['ci'],r['q'],r['bs'],r['bp']) for r in rows}=={(ci,q,bs,bp) for ci in range(4096,4109) for q in range(16) for bs in range(2) for bp in range(2)}
raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());p1,p2=map(ff,raw['x_star_bracket']);assert ff(XSTAR)-ff(XRAD)<=p1<p2<=ff(XSTAR)+ff(XRAD)
# The batched Recentre expressions act separately on each leading-axis entry.
rec=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='Recentre');many=next(n for n in rec.body if isinstance(n,ast.FunctionDef) and n.name=='many');calls=sorted({ast.unparse(n.func) for n in ast.walk(many) if isinstance(n,ast.Call)})
assert calls==['BiTM','MR','MR.exact','app.append','aps.append','float','len','np.stack','np.zeros_like','range'],calls
assert ast.unparse(expression('rec_list'))=='REC.many([D[k] for k in keys] + [Ucell, Vcell], a_s, a_p, blockcell)'
assert ast.unparse(expression('qb'))=='ub * ub + vb * vb'
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-tic,'status':'PASS_SELECTED_FROZEN_EXPRESSION_LINKAGE','scalar_counts':counts,'uq_array_entries_compared':uq_arrays,'exact_partition_points':7810,'canonical_local_knots':14,'block_parameter_checks':832,'complete_block_keys':832,'expressions':{k:ast.unparse(v) for k,v in expr.items()},'recentre_many_call_whitelist':calls,'source_pins':reg['pins'],'value_equality_scope':'All selected native scalar values and array entries equal numerically; signed-zero bits are not compared. This is expression-level linkage of a contemporary replay, not full historical execution or physical Taylor-model validation.'}
(D/'evidence/source_linkage.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],out['seconds'],counts)
