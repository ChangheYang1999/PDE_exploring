from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,hashlib,json,math,struct
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_rounding'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
def hx(s):
 mant,e=s.split('p');sign=-1 if mant.startswith('-') else 1;mant=mant.lstrip('+-')[2:];a,b=mant.split('.');n=int(a+b,16);return sign*Q(n,16**len(b))*Q(2)**int(e)
def binary(q):
 sign=-1 if q>>63 else 1;e=(q>>52)&2047;m=q&((1<<52)-1);check(e<2047,'finite IEEE');return sign*Q(m if e==0 else m+(1<<52))*Q(2)**(-1074 if e==0 else e-1023-52)
a=json.loads((D/'evidence/compute.json').read_text());pins={}
for n,h in a['files'].items():check(sha(B/n)==h,'input');pins[n]=h
s=json.loads((D/'sources/scalars.json').read_text());vals={}
for r in s['scalars']:
 raw=(B/r['copy']).read_bytes();check(raw[:6]==b'\x93NUMPY' and raw[6:8]==b'\x01\x00','NPY version');n=int.from_bytes(raw[8:10],'little');head=ast.literal_eval(raw[10:10+n].decode());check(head=={'descr':'<f8','fortran_order':False,'shape':()} and len(raw)==10+n+8,'scalar NPY');q=binary(int.from_bytes(raw[-8:],'little'));check(q==hx(r['hex'])==Q(r['exact_value']),'independent scalar');vals[r['member']]=q
records=[];tests=0
for r in a['records']:
 aa,bb=hx(r['a_hex']),hx(r['b_hex']);expected={'ref_J':(vals['t0.npy']-1,vals['t0.npy']),'ref_Jin':(vals['tmin.npy']-1,vals['tmin.npy']),'ref_wide':(vals['tmin.npy'],vals['t0.npy'])}[r['name']];check((aa,bb)==expected,'actual endpoint pair');coef=[hx(c) for c in r['coefficients_hex']]
 for c,s0 in zip(coef,r['coefficients_hex']):check(c==binary(int.from_bytes(struct.pack('<d',float.fromhex(s0)),'little')),'hex vs IEEE coefficient')
 lower=[];upper=[]
 for j in range(5):
  lower.append(coef[j]*math.factorial(j)-(1 if j==0 else 0));upper.append(sum((coef[i]*math.factorial(i)//math.factorial(i-j)*(bb-aa)**(i-j) for i in []),Q(0)))
  upper[-1]=sum((coef[i]*Q(math.factorial(i),math.factorial(i-j))*(bb-aa)**(i-j) for i in range(j,len(coef))),Q(0))
 check(lower==list(map(Q,r['lower_jump_derivatives_exact'])) and upper==list(map(Q,r['upper_trace_derivatives_exact'])),'all direct derivative sums');tests+=10
 if r['name']=='ref_wide':check(Q(12121,10**17)<upper[0]<Q(6061,5*10**16),'strict outward jump bracket')
 else:check(lower==upper==[Q(0)]*5,'unit-width C4')
 records.append({'name':r['name'],'upper_value_exact':str(upper[0]),'value_continuous':lower[0]==upper[0]==0,'C4':all(x==0 for x in lower+upper)})
for p in [D/'evidence/compute.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_HEX_IEEE_NPY_AND_DIRECT_DERIVATIVE_SUMS','endpoint_derivatives_compared':tests,'wide_positive_jump_strict_bounds':['12121/100000000000000000','6061/50000000000000000'],'records':records,'files':pins,'scope':'Exact returned-polynomial values for current source reproduction, not historical/future Gram outputs or singular-vector continuity.'}
with (D/'evidence/independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(out['utc'],out['status'],tests)
