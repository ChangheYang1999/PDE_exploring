"""Bit-level input reconstruction, decimal rounding cells, Arb and iv scalar checks."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal
from datetime import datetime,timezone
import gzip,json,hashlib,sys,time
import sympy as s
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_scalar_aggregation';ctx.prec=384;ctx.threads=1;iv.dps=150
assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def bits(n):
 sign=n>>63;exp=(n>>52)&2047;sig=n&((1<<52)-1);assert exp<2047
 if exp: sig+=1<<52;power=exp-1023-52
 else:power=-1074
 return (-1 if sign else 1)*F(sig)*F(2)**power
def ae(x):
 assert x.is_finite();out=[]
 for z in [x.lower(),x.upper()]:
  assert z.rad()==0;a,b=z.man_exp();out.append(F(int(a))*F(2)**int(b))
 return out
def ie(x):
 out=[]
 for sign,m,e,bc in x._mpi_:assert bc>=0;out.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 return out
def aq(x):return arb(x.numerator)/x.denominator
def iq(x):return iv.mpf(x.numerator)/x.denominator
start=time.monotonic();first=json.loads((D/'evidence/compute.json').read_text());assert first['status']=='PASS_EXACT_SAVED_SCALAR_AGGREGATION_PHYSICAL_OPEN';pins=dict(first['files'])
for n,h in pins.items():assert sha(B/n)==h
sources={name:json.loads((D/'sources'/file).read_text(),parse_float=str)['rows'] for name,file in [('middle','runs__cert_deriv_middle.json'),('inner','runs__cert_deriv_regions_inner.json'),('outer','runs__cert_deriv_regions_outer.json')]}
c,z=s.symbols('c z',real=True);a,b,d,e,g=s.symbols('a b d e g');R=s.Matrix([[c,-z],[z,c]]);H=R*s.Matrix([[a-e,b-g],[b-g,d+e]])*R.T
expected=[c*c*a-2*c*z*b+z*z*d+(z*z-c*c)*e+2*c*z*g,z*z*a+2*c*z*b+c*c*d+(c*c-z*z)*e-2*c*z*g,c*z*a+(c*c-z*z)*b-c*z*d-2*c*z*e+(z*z-c*c)*g]
for q,r in zip([H[0,0],H[1,1],H[0,1]],expected):assert s.expand(q-r)==0
logr=s.diag(-1,1);assert s.trace(logr.T*logr)==2
# Coefficients acting on the ordered first six input scalars, then optional single fields.
coeff={'W':[1,0,0,0,0,0],'gradient':[0,1,1,0,0,0],'second_partial':[0,1,2,1,2,1]}
maxima={};rm={q:{} for q in sources};intervalmax={};count=0;decoded=0;exact_comparisons=0;intervals=0;footer=None
with gzip.open(D/'data_exact/rows.jsonl.gz','rt') as f:
 header=json.loads(next(f));keys=header['keys'];assert header['schema']=='derivative-scalar-bits-v1' and header['rows']==19389
 for line in f:
  r=json.loads(line)
  if r['type']=='complete':footer=r;assert not f.read();break
  region,ci=r['region'],r['cell'];source=sources[region][ci];assert source['ci']==ci and set(r['bits'])==set(keys);vals={}
  for name,h in r['bits'].items():
   n=int(h,16);assert len(h)==16 and n<(1<<63);v=bits(n);prev=bits(n-1) if n else -F(2)**-1074;nxt=bits(n+1);q=F(Decimal(str(source[name])));lo=(prev+v)/2;hi=(nxt+v)/2
   assert lo<=q<=hi and (not n&1 or lo<q<hi);vals[name]=v;decoded+=1
  assert vals['m_inf']>0 and all(v>=0 for v in vals.values())
  v=[vals[name] for name in keys[:6]];nums={name:sum((F(cc)*x for cc,x in zip(cs,v)),F(0)) for name,cs in coeff.items()};nums.update({'eps_minus_Eeps':vals['W_eps_minus_dteps'],'K':vals['W_K'],'EK':vals['W_dtK']})
  calcs={name:(q,False) for name,q in nums.items()};calcs.update({'weighted_'+name:(q,True) for name,q in nums.items()});assert set(calcs)==set(r['values_exact'])
  for name,(num,weighted) in calcs.items():
   den=vals['m_inf'];factor=vals['wf_sup'] if weighted else F(1);q=num*factor/den;assert q==F(r['values_exact'][name]);exact_comparisons+=1
   ar=ae(aq(num)*aq(factor)/aq(den));ir=ie(iq(num)*iq(factor)/iq(den));assert ar[0]<=q<=ar[1] and ir[0]<=q<=ir[1];intervals+=2
   u=max(ar[1],ir[1])
   if name not in intervalmax or u>F(intervalmax[name]['upper_exact']):intervalmax[name]={'region':region,'cell':ci,'upper_exact':str(u)}
   hit={'region':region,'cell':ci,'upper_exact':str(q),'t_a_display_only':float(source['t_a'])}
   if name not in maxima or q>F(maxima[name]['upper_exact']):maxima[name]=hit
   if name not in rm[region] or q>F(rm[region][name]['upper_exact']):rm[region][name]=hit
  count+=1
assert footer and footer['rows']==count==19389 and maxima==first['maxima'] and rm==first['regions']
for name,cap in [('gradient',F(839,2000)),('second_partial',F(3566,5))]:assert F(intervalmax[name]['upper_exact'])<cap
# This printed middle-region number is an additional source assertion, not a physical lower bound.
r5=F(rm['middle']['eps_minus_Eeps']['upper_exact']);printed=F(427,1000);assert r5>printed
for p in [D/'evidence/compute.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_BIT_DECIMAL_AND_TWO_INTERVAL_SCALAR_RECONSTRUCTION_PHYSICAL_OPEN','rows':count,'decoded_binary64_fields':decoded,'exact_scalar_comparisons':exact_comparisons,'interval_enclosures':intervals,'symbolic_polar_Hessian_identities':3,'log_r_Frobenius_squared_exact':'2','maxima':maxima,'interval_maxima':intervalmax,'printed_R5_0427_dominates_saved_middle_maximum':False,'saved_R5_middle_maximum_exact':str(r5),'printed_R5_exact':str(printed),'library_versions':{'python_flint':flint.__version__,'arb_bits':ctx.prec,'mpmath':mpmath.__version__,'iv_dps':iv.dps},'files':dict(sorted(pins.items())),'seconds':time.monotonic()-start,'scope':'All saved scalar expressions checked; physical derivative majorants, denominator validity, covering and tails remain open. Failure of the printed0.427 to dominate a certificate maximum is not a physical residual lower bound.'}
with (D/'evidence/independent.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','rows','decoded_binary64_fields','exact_scalar_comparisons','interval_enclosures','printed_R5_0427_dominates_saved_middle_maximum','seconds']}))
