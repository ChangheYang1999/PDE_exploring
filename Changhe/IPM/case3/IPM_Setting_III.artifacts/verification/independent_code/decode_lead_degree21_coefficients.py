"""Result288: restrictive, data-only decoder of lead polynomial coefficient files."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import pickle,pickletools,io,json,hashlib
from functools import reduce
from operator import mul
from exact_degree21 import C,h,encode,prim,degree
R=Path('research/lead_degree21_resultant_route_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[]
def integer(n):
 if not isinstance(n,int):raise ValueError('Integer constructor requires an integer')
 return C.constant(n)
def symbol(name,*args,**kwargs):
 if name!='x' or args or kwargs:raise ValueError('Only the coefficient variable x=eta is admitted')
 return h
def add(*args):return sum(args,C.constant(0))
def multiply(*args):return reduce(mul,args,C.constant(1))
def power(a,b):
 # The pickled expression may use its Integer constructor for the exponent.
 if isinstance(b,int):n=b
 else:
  if b.total_degree()>0:raise ValueError('Nonconstant exponent')
  n=int(b(0,0,0))
 if not 0<=n<=3000:raise ValueError('Exponent outside the coefficient-file degree cap')
 return a**n
allowed={('sympy.core.add','Add'):add,('sympy.core.mul','Mul'):multiply,('sympy.core.power','Pow'):power,('sympy.core.numbers','Integer'):integer,('sympy.core.symbol','Symbol'):symbol}
def load(data):
 stack=[];memo={};marker=object()
 def marked():
  k=len(stack)-1
  while k>=0 and stack[k] is not marker:k-=1
  if k<0:raise pickle.UnpicklingError('Missing marker')
  values=stack[k+1:];del stack[k:];return values
 for op,arg,pos in pickletools.genops(data):
  name=op.name
  if name in ['PROTO','FRAME']:continue
  if name in ['BININT1','BININT2','BININT','LONG1','LONG4','SHORT_BINUNICODE','BINUNICODE']:stack.append(arg)
  elif name=='EMPTY_DICT':stack.append({})
  elif name=='EMPTY_LIST':stack.append([])
  elif name=='MARK':stack.append(marker)
  elif name=='MEMOIZE':memo[len(memo)]=stack[-1]
  elif name in ['BINGET','LONG_BINGET']:stack.append(memo[arg])
  elif name=='STACK_GLOBAL':
   symbol_name=stack.pop();module=stack.pop();key=(module,symbol_name)
   if key not in allowed:raise pickle.UnpicklingError('Disallowed constructor '+str(key))
   stack.append(key)
  elif name=='TUPLE':stack.append(tuple(marked()))
  elif name in ['TUPLE1','TUPLE2','TUPLE3']:
   k=int(name[-1]);values=tuple(stack[-k:]);del stack[-k:];stack.append(values)
  elif name=='NEWOBJ':
   args=stack.pop();key=stack.pop()
   if type(key)is not tuple or key not in allowed or type(args)is not tuple:raise pickle.UnpicklingError('Invalid constructor')
   stack.append(allowed[key](*args))
  elif name=='APPENDS':
   values=marked()
   if type(stack[-1])is not list:raise pickle.UnpicklingError('APPENDS target')
   stack[-1].extend(values)
  elif name=='SETITEMS':
   values=marked()
   if type(stack[-1])is not dict or len(values)%2:raise pickle.UnpicklingError('SETITEMS target')
   for k in range(0,len(values),2):stack[-1][values[k]]=values[k+1]
  elif name=='SETITEM':
   value=stack.pop();key=stack.pop()
   if type(stack[-1])is not dict:raise pickle.UnpicklingError('SETITEM target')
   stack[-1][key]=value
  elif name=='STOP':
   if len(stack)!=1:raise pickle.UnpicklingError('Invalid final stack')
   return stack[0]
  else:raise pickle.UnpicklingError('Unsupported opcode '+name)
 raise pickle.UnpicklingError('Missing STOP')
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
try:load(b"cos\nsystem\n(S'not executed'\ntR.")
except pickle.UnpicklingError:ck('arbitrary global rejected',True)
else:ck('arbitrary global rejected',False)
try:symbol('unlisted')
except ValueError:ck('unlisted symbol rejected',True)
else:ck('unlisted symbol rejected',False)
raw5=load((V/'producer_t5b_21.pkl').read_bytes());ck('V exact dictionary',set(raw5)=={'L','core'} and len(raw5['L'])==2);raw6=load((V/'producer_t6d_21.pkl').read_bytes());ck('VI plain integer vector',set(raw6)=={'L2'} and isinstance(raw6['L2'],list)and all(type(n)is int for n in raw6['L2']))
vals5=[prim(a)for a in raw5['L']];val6=C.from_dict({(0,0,k):a for k,a in enumerate(raw6['L2'])if a});ck('V degrees',[degree(p,2)for p in vals5]==[316,370]);ck('V core degree',degree(raw5['core'],2)==90);ck('VI degree',degree(val6,2)==1222)
out=dict(status='PASS',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,source_sha256={name:sha(V/name)for name in ['producer_t5b_21.pkl','producer_t6d_21.pkl']},proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),typeV=dict(H=encode(vals5[0]),J=encode(vals5[1]),core=encode(prim(raw5['core']))),typeVI=dict(J=encode(prim(val6))),scope='Coefficient data only; mathematical identities not yet checked')
(V/'COEFFICIENTS.json').write_text(json.dumps(out,indent=2)+'\n');print('DATA ONLY PASS',len(checks),out['utc'])
