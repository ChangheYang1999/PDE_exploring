"""Independent NPY/IEEE reader and integer round-to-nearest-even geometry audit."""
import sys,os
sys.dont_write_bytecode=True
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from decimal import Decimal
from datetime import datetime,timezone
import ast,json,hashlib,zipfile,math,time
from flint import fmpq as Q
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_intended_partition'

def need(v,s):
 if not v:raise ValueError(s)
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text(),parse_float=Decimal)
def dump(p,x):
 with p.open('x') as f:json.dump(x,f,indent=1);f.write('\n')
def decimalq(v):
 if isinstance(v,int):return Q(v)
 n,d=v.as_integer_ratio();return Q(n,d)
def power(e):return Q(1<<e) if e>=0 else Q(1,1<<(-e))
def decode(bits):
 s=bits>>63;e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite IEEE')
 if e:m+=1<<52
 return (-1 if s else 1)*Q(m)*power(-1074 if e==0 else e-1075)
def hexq(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');mant,expo=s.split('p');a,b=mant.removeprefix('0x').split('.')
 return sign*Q(int(a+b,16))*power(int(expo)-4*len(b))
def roundbits(q):
 q=Q(q);sign=0
 if q<0:sign=1;q=-q
 if q==0:return sign<<63
 n,d=int(q.numerator),int(q.denominator);e=n.bit_length()-d.bit_length()
 if q<power(e):e-=1
 step=max(e-52,-1074);nn=n<<max(-step,0);dd=d<<max(step,0);k,r=divmod(nn,dd)
 if 2*r>dd or (2*r==dd and k&1):k+=1
 if e< -1022:
  need(k<=1<<52,'subnormal carry');bits=k
 else:
  if k==1<<53:k>>=1;e+=1
  need((1<<52)<=k<(1<<53) and -1022<=e<=1023,'normal encoded rounding')
  bits=((e+1023)<<52)+(k-(1<<52))
 return (sign<<63)|bits
def rn(q):return decode(roundbits(q))
def up(q):
 bits=roundbits(q);need(q>=0,'nonnegative successor used');return decode(bits+1)
def npy(z,name):
 data=z.read(name+'.npy');need(data[:6]==b'\x93NUMPY','NPY magic');ver=tuple(data[6:8]);need(ver in [(1,0),(2,0)],'NPY version')
 nbytes=2 if ver==(1,0) else 4;h=int.from_bytes(data[8:8+nbytes],'little');off=8+nbytes+h;head=ast.literal_eval(data[8+nbytes:off].decode('latin1'))
 need(head['descr']=='<f8' and head['fortran_order'] is False,'NPY dtype/order');shape=head['shape'];size=math.prod(shape);payload=data[off:];need(len(payload)==8*size,'NPY payload length')
 bits=[int.from_bytes(payload[8*i:8*i+8],'little') for i in range(size)]
 return {'shape':list(shape),'values':[decode(x) for x in bits],'bits':bits,'sha256':hashlib.sha256(payload).hexdigest()}
start=utc();tick=time.monotonic();first=load(D/'evidence/check.json');geo=load(D/'data_exact/geometry.json');pins={}
for name,h in first['files'].items():need(sha(B/name)==h,'first-stage pin '+name)
part=load(B/geo['partition_source']);nodes=[];prior=None;total=0
for idx,sp in enumerate(part['spans']):
 a,b=Q(sp['a_exact']),Q(sp['b_exact']);n=sp['count'];need(sp['span']==idx and sp['first_cell']==total and n>0 and a<b,'separate span indexing')
 if prior is not None:need(a==prior,'span adjacency')
 # Incremental exact arithmetic, different traversal from first direct interpolation.
 step=(b-a)/n;x=a
 for i in range(n):nodes.append(x);x+=step
 need(x==b,'span exact endpoint');prior=b;total+=n
nodes.append(prior);need(total==7809 and len(part['spans'])==1558,'all middle cells')
bminus,bplus=nodes[0],nodes[-1];U=power(-53);beta=up(U/(1-U));cnt=0;nodecnt=0;shiftcnt=0;globaldelta=Q(0);summary={}
with zipfile.ZipFile(B.parent/'ipmA-num/data/trial_v2_h0.008.npz') as z:
 knots=npy(z,'knots')['values'];need(knots[0]==bminus and knots[-1]==bplus,'independent raw endpoints')
 for name in ['L','k']:need(npy(z,name)['values'][0]==Q(geo['params'][name]['exact']),'weight parameter '+name)
need(0<Q(geo['params']['k']['exact'])<1 and Q(geo['params']['L']['exact'])>0,'weight hypotheses')
for region,count in [('inner',2632),('middle',7809),('outer',8948)]:
 g=geo['regions'][region];arrays={}
 with zipfile.ZipFile(g['npz']) as z:
  for name,v in g['members'].items():
   obj=npy(z,name);need(obj['shape']==v['shape'] and obj['sha256']==v['payload_sha256'],'member bytes '+region+name)
   need(obj['values']==[hexq(s) for s in v['hex']],'all independently decoded IEEE '+region+name);arrays[name]=obj['values']
 if region=='middle':true=nodes;base=Q(0);mm=arrays['tb'];rr=arrays['tb_rad']
 else:
  base=arrays['tmin' if region=='inner' else 't0'][0];need(base==(bminus if region=='inner' else bplus),'base source equality')
  need(arrays['tmin_rad' if region=='inner' else 't0_rad'][0]==0,'zero source base radius')
  origin=base+(-5 if region=='inner' else 0);step=Q(5 if region=='inner' else 17,count);true=[origin]
  for j in range(count):true.append(true[-1]+step)
  mm=arrays['tau'];rr=arrays['tau_rad']
 need(len(mm)==len(rr)==len(true)==count+1,'region shape');maxerr=Q(0);at=0;pos=neg=0
 for i,x in enumerate(true):need(rr[i]>=0 and mm[i]-rr[i]<=x-base<=mm[i]+rr[i],'node box '+region+str(i));nodecnt+=1
 rows=load(B/g['source_rows'])['rows'];need(len(rows)==count,'row bijection')
 for i,row in enumerate(rows):
  need(row['ci']==i,'exact row index');a,b=true[i:i+2];need(a<b,'positive exact cell')
  ah=rn(decimalq(row['t_a']));h=rn(decimalq(row['h']));need(h>=b-a,'true length upper bound')
  # Exact emulation of actual scalar MR subtraction/magnitude, without NumPy.
  mid=rn(mm[i+1]-mm[i]);rad=up(up(up(rr[i+1]+rr[i])+up(beta*abs(mid))));hmr=up(abs(mid)+rad)
  need(hmr==h,'integer IEEE MR reproduction '+region+str(i))
  need(ah==(mm[i] if region=='middle' else rn(base+mm[i])),'independent rounded midpoint '+region+str(i))
  entry=geo['rows'][cnt];need(entry['region']==region and entry['ci']==i,'manifest row bijection')
  need(Q(entry['a'])==a and Q(entry['b'])==b and Q(entry['offset'])==a-ah and Q(entry['h_slack'])==h-(b-a),'every exact row discrepancy')
  err=abs(a-ah)
  if err>maxerr:maxerr=err;at=i
  if a>ah:pos+=1
  if a<ah:neg+=1
  # The actual source uses a scalar width and MR shift boxes, no Arb sigma ball.
  hk=up(h/4);need(hk>=h/4,'Bernstein width')
  for kk in range(4):
   shift=kk*hk;centre=rn(shift);radius=up(U*centre)
   need(centre-radius<=shift<=centre+radius,'Bernstein coherent shift box');shiftcnt+=1
  need(4*hk>=h,'Bernstein coverage');cnt+=1
 result={'cells':count,'hull':[str(true[0]),str(true[-1])],'max_start_error':str(maxerr),'max_start_error_cell':at,'positive_start_errors':pos,'negative_start_errors':neg}
 need(result==first['regions'][region],'all region statistics');summary[region]=result;globaldelta=max(globaldelta,maxerr)
need(cnt==19389 and nodecnt==19392 and shiftcnt==77556,'all counts');need(str(globaldelta)==first['delta'],'max exact delta')
need(summary['inner']['hull'][1]==summary['middle']['hull'][0] and summary['middle']['hull'][1]==summary['outer']['hull'][0],'one annulus')
x=4*globaldelta;need(0<x<1,'small displacement');rational_upper=1/(1-x);ceiling=Q(25000000000001,25000000000000);need(rational_upper<ceiling,'independent rational exp majorant')
iv.dps=110;ball=iv.exp(4*(iv.mpf(int(globaldelta.numerator))/int(globaldelta.denominator)));ends=[]
for sign,m,e,bits in ball._mpi_:need(bits>=0,'finite iv');ends.append((-1 if sign else 1)*Q(int(m))*power(int(e)))
need(1<ends[0]<=ends[1]<rational_upper<ceiling,'independent iv factor')
for name,h in first['files'].items():need(sha(B/name)==h,'stable first pin '+name)
for p in [D/'PROOF.md',D/'ADDENDUM.md',D/'code/check.py',Path(__file__),D/'evidence/check.json',D/'data_exact/geometry.json']:pins[str(p.relative_to(B))]=sha(p)
out={'start_utc':start,'utc':utc(),'status':'PASS_INDEPENDENT_ALL_ROWS_AND_PARAMETER_COVERAGE','rows':cnt,'node_inclusions':nodecnt,'bernstein_shift_boxes':shiftcnt,'regions':summary,'delta':str(globaldelta),'exp4delta_iv_endpoints':[str(q) for q in ends],'independent_rational_exp_upper':str(rational_upper),'loss_ceiling':str(ceiling),'pins':pins,'first_source_pins_checked':len(first['files']),'seconds':time.monotonic()-tick,'scope':'Coherent geometry, source rounding and a conditional weight theorem. No numerical whole-norm sum, physical W membership, historical execution or omitted tail is certified.'};dump(D/'evidence/audit.json',out);print(json.dumps(out,indent=2))
