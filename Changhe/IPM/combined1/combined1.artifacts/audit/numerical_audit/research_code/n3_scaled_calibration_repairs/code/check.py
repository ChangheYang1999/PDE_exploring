"""Read only the finite calibration syntax, without executing peer code."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,json,time
R=Path(__file__).resolve().parents[3];B=R/'research/n3_scaled_calibration_repairs'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()

def value(n,env=None):
 env={} if env is None else env
 if isinstance(n,ast.Constant) and isinstance(n.value,int):return Q(n.value)
 if isinstance(n,ast.Name):return env[n.id]
 if isinstance(n,(ast.Tuple,ast.List)):return [value(x,env) for x in n.elts]
 if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -value(n.operand,env)
 if isinstance(n,ast.BinOp):
  a,b=value(n.left,env),value(n.right,env)
  if isinstance(n.op,ast.Add):return a+b
  if isinstance(n.op,ast.Sub):return a-b
  if isinstance(n.op,ast.Mult):return a*b
  if isinstance(n.op,ast.Div):return a/b
  if isinstance(n.op,ast.Pow):assert b.denominator==1;return a**int(b)
 if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and not n.keywords:
  args=[value(x,env) for x in n.args]
  if n.func.id=='Q':return Q(*args)
  if n.func.id=='range':assert all(x.denominator==1 for x in args);return list(map(Q,range(*map(int,args))))
 raise AssertionError(ast.dump(n))

def is_panel_append(n):
 return isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='panels' and n.value.func.attr=='append'

def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h;(inputs.__setitem__(str(p.relative_to(R)),v))
  return json.loads(p.read_text()) if p.suffix=='.json' else None
 bind(B/'PROOF.md');bind(Path(__file__));m=bind(B/'source/MANIFEST.json');assert m['proof_sha256']==sha(B/'PROOF.md')
 for rel,row in m['sources'].items():bind(R/rel,row['sha256'])
 for rel in ['research/n3_scaled_norm_audit/verification/domain.json','research/n3_quadrature_partition/verification/result.json']:
  dep=bind(R/rel)
  for section in ['inputs','source_hashes']:
   for q,h in dep.get(section,{}).items():bind(R/q,h)
 delta=Q(1824676646553933,4076476460239181);checks['exact_delta']=0<delta<Q(1,2)
 tree=ast.parse((B/'source/legqs_tests.py').read_text())
 blocks=[n for n in tree.body if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and isinstance(n.test.left,ast.Constant) and n.test.left.value=='A'];assert len(blocks)==1
 loops=[n for n in ast.walk(blocks[0]) if isinstance(n,ast.For) and isinstance(n.target,ast.Name)]
 def loop(name):return [n for n in loops if n.target.id==name]
 scales=value(loop('a')[0].iter);bases=value(loop('b0')[0].iter);powers=value(loop('i')[0].iter)
 ms=[value(n.iter) for n in loop('m')];small=next(v for v in ms if len(v)==6);large=next(v for v in ms if len(v)==3)
 checks['three_actual_base_classes']=bases==[Q(-37,100),Q(0),delta/2-1]
 checks['actual_small_loops']=scales==list(map(Q,[624,99,2499])) and powers==list(map(Q,range(15))) and small==list(map(Q,range(0,41,7)))
 checks['actual_large_exponents']=large==list(map(Q,[600,1800,2400]))
 rows=[]
 for a in scales:
  for b0 in bases:
   for i in powers:
    for mm in small:
     b=b0+mm;assert a>0 and i>=0 and b>-1
     rows.append({'scale':str(a),'base':str(b0),'m':str(mm),'power':str(i),'exponent':str(b),'admissible':True})
 for mm in large:
  b=Q(-37,100)+mm;assert b>-1
  rows.append({'scale':'624','base':'-37/100','m':str(mm),'power':'23','exponent':str(b),'admissible':True})
 checks['all_813_source_exponents_admissible']=len(rows)==813
 checks['original_45_m_zero_cases_diverge']=delta-Q(3,2)<-1 and len(scales)*len(powers)==45
 body=ast.parse((B/'source/legqs_quadcheck.py').read_text()).body
 starts=[k for k,n in enumerate(body) if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='panels'];assert len(starts)==1
 k=starts[0];panels=value(body[k].value);sourced_statements=1
 for n in body[k+1:]:
  if isinstance(n,ast.For):
   assert isinstance(n.target,ast.Name) and n.target.id=='k' and len(n.body)==1 and not n.orelse and is_panel_append(n.body[0])
   call=n.body[0].value;assert len(call.args)==1 and not call.keywords
   for kk in value(n.iter):panels.append(value(call.args[0],{'k':kk}))
   sourced_statements+=1
  elif is_panel_append(n):
   assert len(n.value.args)==1 and not n.value.keywords
   panels.append(value(n.value.args[0]));sourced_statements+=1
  else:break
 expected=[(Q(0),Q(1,2**12))]+[(Q(1,2**(k+1)),Q(1,2**k)) for k in range(11,0,-1)]+[(1-Q(1,2**k),1-Q(1,2**(k+1))) for k in range(1,46)]+[(1-Q(1,2**46),Q(1))]
 checks['actual_58_panel_list']=[tuple(q) for q in panels]==expected and sourced_statements==4
 checks['positive_panel_lengths']=all(0<=a<b<=1 for a,b in panels)
 checks['ordered_adjacent_full_domain']=panels[0][0]==0 and panels[-1][1]==1 and all(panels[k][1]==panels[k+1][0] for k in range(57))
 mass=sum((b-a for a,b in panels),Q(0));checks['unit_constant_mass']=mass==1
 pairs=0
 for i,(a,b) in enumerate(panels):
  for aa,bb in panels[:i]:assert max(a,aa)>=min(b,bb);pairs+=1
 checks['all_1653_interiors_disjoint']=pairs==1653
 oldmass=Q(3,2)-Q(1,2**12)-Q(1,2**46)
 checks['old_mass_identity']=oldmass==Q(105535936397311,70368744177664)
 assert all(checks.values()),checks
 result={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'inputs':inputs,'base_classes':list(map(str,bases)),'small_cases':810,'large_cases':3,'exponent_cases':rows,'panel_count':len(panels),'panels':[list(map(str,p)) for p in panels],'constant_mass':str(mass),'pairwise_interiors_checked':pairs,'foreign_code_executed':False,'repaired_numerical_tests_executed_here':False,'repaired_numerical_test_outputs_checked':False,'verdict':'CONFIRMED actual source domain and partition repairs only; repaired numerical calibration execution and error bounds OPEN','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(inputs),'bindings','813 admissible moments,58 panels1653pairs','sha',sha(out),'utc',result['utc'],'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
