from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,io,json,pickle,struct,sys
import numpy as np
if sys.flags.optimize: raise RuntimeError('optimization forbidden')
ROOT=Path(__file__).resolve().parents[3]; HERE=ROOT/'research/operator_image_joins'
def require(x,label):
 if not x: raise RuntimeError(label)
def digest(p):
 with p.open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()
def decode(x):
 bits=struct.unpack('>Q',struct.pack('>d',x))[0]; exp=(bits>>52)&2047; frac=bits&((1<<52)-1)
 require(exp!=2047,'finite binary64')
 mant=frac+(1<<52) if exp else frac; power=exp-1023-52 if exp else -1074
 return Fraction((-1 if bits>>63 else 1)*mant)*Fraction(2)**power
class SafeNumpy(pickle.Unpickler):
 def find_class(self,module,name):
  if module=='numpy' and name=='ndarray': return np.ndarray
  if module=='numpy' and name=='dtype': return np.dtype
  if module in ('numpy.core.multiarray','numpy._core.multiarray') and name in ('scalar','_reconstruct'): return getattr(np._core.multiarray,name)
  raise RuntimeError('unapproved global')
def direct(coeff,x,deriv=0):
 return sum((Fraction(j if deriv else 1)*coeff[j]*x**(j-deriv) for j in range(deriv,len(coeff))),Fraction(0))
primary=json.loads((HERE/'evidence/compute.json').read_text()); pins={}
for name,h in primary['files'].items(): require(digest(ROOT/name)==h,'primary dependency '+name); pins[name]=h
counts={'binary64_values_decoded':0,'exact_value_traces':0,'exact_derivative_traces':0,'exact_jumps':0,'nonzero_jumps':0,'columns':0}; records=[]
for record in primary['records']:
 meta=SafeNumpy(io.BytesIO((ROOT/record['source']).read_bytes())).load(); summaries=[]; allj=[]
 for col in record['columns']:
  mode,pieces,label=meta['cols'][col['column_index']]; require(mode==0 and label==col['label'],'column identity'); raw=[]
  for left,right,alpha,values in pieces:
   aa,bb=decode(left),decode(right); cc=[decode(float(v)) for v in values]; require(decode(alpha)==0 and bb>aa,'polynomial domain'); counts['binary64_values_decoded']+=3+len(cc)
   raw.append((aa,bb,cc,direct(cc,bb-aa),direct(cc,Fraction(0),1),direct(cc,bb-aa,1)))
  targets=[Fraction(0)]+[(raw[j-1][3]+raw[j][2][0])/2 for j in range(1,len(raw))]+[Fraction(0)]
  slopes=[]
  for j,(aa,bb,cc,rightvalue,leftder,rightder) in enumerate(raw):
   leftcor=targets[j]-cc[0]; rightcor=targets[j+1]-rightvalue; slope=(rightcor-leftcor)/(bb-aa)
   require(cc[0]+leftcor==targets[j] and rightvalue+leftcor+slope*(bb-aa)==targets[j+1],'independent C0')
   pair=(leftder+slope,rightder+slope); expected=tuple(map(Fraction,col['derivative_traces_exact'][j])); require(pair==expected,'all derivative traces match')
   require(aa==Fraction(col['nodes_exact'][j]) and bb==Fraction(col['nodes_exact'][j+1]),'nodes binding')
   slopes.append(pair); counts['exact_derivative_traces']+=2; counts['exact_value_traces']+=2
  jumps=[slopes[0][0]]+[slopes[j][0]-slopes[j-1][1] for j in range(1,len(slopes))]+[-slopes[-1][1]]
  require(jumps==list(map(Fraction,col['derivative_jumps_exact'])),'all jumps agree'); require(all(jumps),'all joins nonzero')
  require(col['nonzero_join_indices']==list(range(len(jumps))),'indices exact'); require(col['first_witness']=={'join_index':0,'t_exact':col['nodes_exact'][0],'jump_exact':col['derivative_jumps_exact'][0]},'witness binding')
  counts['exact_jumps']+=len(jumps); counts['nonzero_jumps']+=sum(x!=0 for x in jumps); counts['columns']+=1; allj.extend(jumps)
  summaries.append({'column_index':col['column_index'],'pieces':len(raw),'internal_nonzero_joins':len(raw)-1,'support_nonzero_joins':2})
 maximum=max(map(abs,allj)); require(maximum==Fraction(record['max_abs_derivative_jump_exact']),'extremum agreement')
 upper=Fraction(maximum.numerator*10**20//maximum.denominator+1,10**20)
 records.append({'M':record['M'],'N':record['N'],'columns':summaries,'uniform_derivative_jump_upper_exact':str(upper),'images_excluded_from_local_H1':record['M']*record['N']})
require(counts['exact_derivative_traces']==4432 and counts['exact_jumps']==2493 and counts['columns']==277,'scope counts')
# Independent exact checks of the finite-difference identity on signed rational data.
checks=0
for J in (Fraction(-7,3),Fraction(1,10**15),Fraction(0)):
 for am in (Fraction(-2,9),Fraction(4,7)):
  for ap in (Fraction(3,11),Fraction(-1,5)):
   for d in (Fraction(1,17),Fraction(1,10**8)):
    lhs=(J+ap*d/2-(-am*d/2))/d; rhs=J/d+(ap+am)/2
    require(lhs==rhs,'secant identity'); checks+=1
for p in [HERE/'evidence/compute.json',Path(__file__)]: pins[str(p.relative_to(ROOT))]=digest(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_IEEE_DECODE_DIRECT_POWER_DERIVATIVES_AND_RECONSTRUCTED_AFFINE_REPAIR','counts':counts,'secant_identity_rational_checks':checks,'records':records,'files':dict(sorted(pins.items())),'scope':'Exact finite derivative traces and local image obstruction only; no floating spectrum or inverse certification.'}
path=HERE/'evidence/independent.json';require(not path.exists(),'immutable');path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','counts','secant_identity_rational_checks')}));print(json.dumps([{k:r[k] for k in ('M','N','uniform_derivative_jump_upper_exact','images_excluded_from_local_H1')} for r in records]))
