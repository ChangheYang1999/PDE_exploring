"""Explicit current-source structure, input headers, caller and exact scalar linkage."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from types import SimpleNamespace
import ast,hashlib,json,sys,time,zipfile
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];V=B/'research/forcing_v22'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
t0=time.monotonic();sources={'resid':('cert_resid.py','1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053'),'forcing1':('cert_forcing.py','5066d240ea60b89d137025f60fbda4e631b7cf7e67f8ef5968bab307bbeddcd9'),'forcing2':('cert_forcing2.py','012e106b568ec68876058ee0588aa64cfbe9c846dc44523c164424015c238197')};trees={};paths={}
for name,(fn,h) in sources.items():
 p=V/'source/src'/fn;assert sha(p)==h;trees[name]=ast.parse(p.read_text());paths[name]=p
core=next(x for x in trees['resid'].body if isinstance(x,ast.FunctionDef) and x.name=='_cell_core_deriv');cls=next(x for x in trees['resid'].body if isinstance(x,ast.ClassDef) and x.name=='Certifier');value=next(x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name=='cell_core');init=next(x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name=='__init__');scatter=next(x for x in cls.body if isinstance(x,ast.FunctionDef) and x.name=='conv_scatter')
bindings=[]
def norm(x):return ast.dump(x,include_attributes=False)
def bind(root,statement,label):
 expected=ast.parse(statement).body[0];matches=[x for x in ast.walk(root) if type(x) is type(expected) and norm(x)==norm(expected)]
 assert len(matches)==1,(label,len(matches),statement)
 x=matches[0];bindings.append(dict(label=label,line=x.lineno,column=x.col_offset,source=ast.unparse(x)));return x
# Core exact mathematical expressions and enclosing loop ranges, excluding
# radius/truncation arithmetic from the mathematical assertion.
for label,s in [
 ('e2','e2 = e_ta * e_ta'),('e3','e3 = e2 * e_ta'),('e4','e4 = e2 * e2'),('inv_e2','inv_e2 = inv_e * inv_e'),
 ('g_rate','gam = alpha + MR.exact(4.0)'),('g_recurrence','Fi = Fi * gam + poly_deriv(Fi)'),('g_scale','g_list = [gi.scale(e4) for gi in g_list]'),
 ('A_value','A = [self.ode_tm(A0, g_list[0], gsup, -2.0 * n, h_up)]'),('B_value','B = [self.ode_tm(B0, g_list[0], gsup, 2.0 * n, h_up, gsign=-1.0)]'),
 ('minus2n','m2n = MR(-2.0 * n, 0.0)'),('plus2n','p2n = MR(2.0 * n, 0.0)'),
 ('AB_derivatives','for i in range(nder):\n A.append(A[-1].scale(m2n) + g_list[i])\n B.append(B[-1].scale(p2n) - g_list[i])'),
 ('psi','psi = [(A[i] + B[i]).scale(inv4n) for i in range(nder + 1)]'),('BminusA','BmA = [(B[i] - A[i]) for i in range(nder + 1)]'),
 ('Em2','Em2c, Em2r = tm_exp(-2.0, h_up, Q)'),
 ('accP','accP = accP + psi[l].scale(MR.exact(cst))'),('accQ','accQ = accQ + BmA[l].scale(MR.exact(cst))'),
 ('P_append','Pt.append(tm_mul(accP.scale(MR(-1.0 * n, 0.0) * inv_e2), Em2))'),('Q_append','Qt.append(tm_mul(accQ.scale(MR.exact(0.25) * inv_e2), Em2))'),
 ('R_init','Rd = [zero_tm(self.M + 1) for _ in range(nder + 2)]'),('R_rate','a3 = alpha + MR.exact(3.0)'),('R_recurrence','Ri = Ri * a3 + poly_deriv(Ri)'),('R_scale','Rd = [r_.scale(e3) for r_ in Rd]'),
 ('Rhat','Rhat = [TMArr(Rd[i].c * MR(twoj1[:, None], 0.0), succ(Rd[i].r * twoj1)) for i in range(nder + 1)]'),
 ('odd_weight','twoj1 = 2.0 * np.arange(self.M + 1) + 1.0'),('linear','lin = Rd[i + 1].scale(self.c_l) - Rd[i]'),
 ('radial_scatter','E1 = self.conv_scatter(Pt[l].scale(cst), Rd[1 + i - l], hpow, h_up)'),('tangent_scatter','E2 = self.conv_scatter(Qt[l].scale(cst), Rhat[i - l], hpow, h_up, flip2=True)'),
 ('sum','tot = tot + E1 + E2'),('eps_append','eps.append(tot)'),('stash','self._last_eps = eps')]:bind(core,s,label)
# The statements belong to the needed actual loop nesting, not an unused branch.
parents={child:parent for parent in ast.walk(core) for child in ast.iter_child_nodes(parent)}
def ancestors(node):
 out=[]
 while node in parents:node=parents[node];out.append(node)
 return out
loop_checks=[]
for label,inner,outer in [('g_recurrence','range(nder + 1)',None),('R_recurrence','range(nder + 2)',None),('accP','range(i + 1)','range(nder + 1)'),('accQ','range(i + 1)','range(nder + 1)'),('radial_scatter','range(i + 1)','range(nder + 1)'),('tangent_scatter','range(i + 1)','range(nder + 1)'),('eps_append','range(nder + 1)',None)]:
 b=next(x for x in bindings if x['label']==label);node=next(x for x in ast.walk(core) if hasattr(x,'lineno') and x.lineno==b['line'] and x.col_offset==b['column'] and ast.unparse(x)==b['source']);loops=[x for x in ancestors(node) if isinstance(x,ast.For)];assert ast.unparse(loops[0].iter)==inner
 if outer:assert ast.unparse(loops[1].iter)==outer
 loop_checks.append(dict(label=label,loops=[ast.unparse(x.iter) for x in loops]))
stash=next(x for x in core.body if isinstance(x,ast.Assign) and any(ast.unparse(t)=='self._last_eps' for t in x.targets));assert all(not isinstance(x,(ast.If,ast.For,ast.While)) for x in ancestors(stash))
# Binding of the free function to the instance method.
bind(trees['resid'],'Certifier.cell_core_deriv = _cell_core_deriv','method_install')
# Exact selected polynomial-derivative execution. U=0 and successor identity
# intentionally erase floating error rules; this certifies algebra only.
poly=next(x for x in core.body if isinstance(x,ast.FunctionDef) and x.name=='poly_deriv')
class PMR:
 def __init__(self,m,r):self.m=np.asarray(m,dtype=object);self.r=np.asarray(r,dtype=object)
ns={'np':np,'MR':PMR,'succ':lambda x:x,'U':0};exec(compile(ast.Module(body=[poly],type_ignores=[]),str(paths['resid']),'exec'),ns)
polychecks=0
for degree in range(8):
 m=np.empty((8,3),dtype=object);m.fill(F(0));m[degree]=[F(1),F(-3,7),F(11,13)];p=PMR(m,np.zeros_like(m));q=ns['poly_deriv'](p);expected=np.empty_like(m);expected.fill(F(0))
 if degree:expected[degree-1]=degree*m[degree]
 assert np.array_equal(q.m,expected) and np.all(q.r==0);polychecks+=m.size
# The actual angular weight expression, all261entries.
weight=next(x for x in ast.walk(core) if isinstance(x,ast.Assign) and len(x.targets)==1 and ast.unparse(x.targets[0])=='twoj1');w=eval(compile(ast.Expression(weight.value),'<oddweights>','eval'),{'__builtins__':{},'np':np,'self':SimpleNamespace(M=260)})
assert list(map(F,w))==[F(2*j+1) for j in range(261)]
# Reciprocal interval exactly contains1/(4n), with source expression evaluated
# on the same integer n array and source U=2^-53/successor.
inv=next(x for x in ast.walk(core) if isinstance(x,ast.Assign) and len(x.targets)==1 and ast.unparse(x.targets[0])=='inv4n');narr=np.arange(1,262);cap=lambda m,r:(m,r)
mid,rad=eval(compile(ast.Expression(inv.value),'<inv4n>','eval'),{'__builtins__':{},'MR':cap,'succ':lambda x:np.nextafter(x,np.inf),'U':2.0**-53,'n':narr})
for n,(m,r) in enumerate(zip(mid,rad),1):assert F(float(m))-F(float(r))<=F(1,4*n)<=F(float(m))+F(float(r))
bind(core,'inv4n = MR(1.0 / (4 * n), succ(U / (4 * n)))','inv4n')
# Actual caller =4 and immediate _last_eps read in each version, with v2
# importing that constant from the pinnedv1 module.
nder=bind(trees['forcing1'],'NDER = 4','forcing_NDER')
imports=[x for x in trees['forcing2'].body if isinstance(x,ast.ImportFrom) and x.module=='cert_forcing' and any(a.name=='NDER' and a.asname is None for a in x.names)];assert len(imports)==1
caller=[]
for name in ['forcing1','forcing2']:
 main=next(x for x in trees[name].body if isinstance(x,ast.FunctionDef) and x.name=='main')
 st=bind(main,'res = C.cell_core_deriv(h_up, C.e_ta[ci], [(0.0, C.T[ci])], C.A[ci], C.B[ci], C.m_ta[ci], C.wfar_ta[ci], NDER)',name+'_call')
 holders=[x for x in ast.walk(main) if hasattr(x,'body') and isinstance(x.body,list) and st in x.body];assert len(holders)==1
 body=holders[0].body;index=body.index(st);assert norm(body[index+1])==norm(ast.parse('eps = C._last_eps').body[0])
 caller.append(dict(source=name,call_line=st.lineno,read_line=body[index+1].lineno,nder=4))
# Actual headers: no numeric Green arrays loaded and no module import side effects.
prior=json.loads((V/'evidence/finite_audit.json').read_text());ext=prior['external_inputs'];gp=Path(ext['green']['path']);assert sha(gp)==ext['green']['sha256'];headers={}
with zipfile.ZipFile(gp) as z:
 for key in ['T_mid','T_rad','A_mid','A_rad','B_mid','B_rad','tb','tb_rad']:
  with z.open(key+'.npy') as f:
   version=np.lib.format.read_magic(f)
   assert version in [(1,0),(2,0)]
   shape,fort,dtype=(np.lib.format.read_array_header_1_0(f) if version==(1,0) else np.lib.format.read_array_header_2_0(f))
  headers[key]=dict(shape=list(shape),fortran_order=bool(fort),dtype=dtype.str)
expected_shapes={'T_mid':[7809,8,260],'T_rad':[7809,8,260],'A_mid':[7810,261],'A_rad':[7810,261],'B_mid':[7810,261],'B_rad':[7810,261],'tb':[7810],'tb_rad':[7810]}
assert {k:v['shape'] for k,v in headers.items()}==expected_shapes
assert all(x['dtype']=='<f8' for x in headers.values()) and sha(gp)==ext['green']['sha256']
# All multiplicities, using a closed integer counting formula independent of bincount.
lau=json.loads((D/'evidence/laurent.json').read_text());counts=lau['scatter_counts'];closed=[]
for N in range(523):
 s=max(0,min(261,N)-max(1,N-260)+1)
 d=max(0,260-N)+max(0,261-N)
 closed.append(s+d)
assert counts==closed and sum(closed)==2*68121 and closed[522]==0
bind(scatter,'s2 = (-self.S2 if flip2 else self.S2).ravel()','scatter_flip2')
# Verify loop defaults explicitly, without implying the default2 provides five jets.
assert ast.literal_eval(core.args.defaults[-1])==2
for name,(fn,h) in sources.items():assert sha(paths[name])==h
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_CURRENT_RESIDUAL_STRUCTURE_DIMENSIONS_CALLER',bindings=bindings,loop_checks=loop_checks,source_hashes={k:v[1] for k,v in sources.items()},caller=caller,default_nder=2,actual_forcing_nder=4,forcing2_NDER_import_line=imports[0].lineno,external_green=dict(path=str(gp),sha256=ext['green']['sha256'],headers=headers,before_after_hash=True),shape_M=260,shape_Nf=261,spline_degree=7,polynomial_derivative_basis_entries=polychecks,odd_weight_entries=261,reciprocal_interval_checks=261,scatter_multiplicity_entries=523,total_scatter_contributions=sum(closed),maximum_multiplicity=max(closed),source_laurent_sha256=sha(D/'evidence/laurent.json'),code_sha256=sha(Path(__file__)),seconds=time.monotonic()-t0,scope='Selected AST structures and loops, exact basis polynomial derivative algebra, all261 reciprocal boxes, actual shapes/caller. Neither a full surrogate nor an actual floating execution of _cell_core_deriv. Physical models and numerical operation bounds remain OPEN.')
(D/'evidence/source.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(bindings),'bindings',out['seconds'])
