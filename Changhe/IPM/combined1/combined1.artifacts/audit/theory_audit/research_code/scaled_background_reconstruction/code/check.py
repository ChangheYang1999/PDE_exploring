"""Exact independent polar-to-polynomial reconstruction, with local origin jet."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb,factorial
from functools import lru_cache
import gzip,json,importlib.util,sys,time
from flint import fmpq as Q, fmpq_poly as Poly, arb,ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()

def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

@lru_cache(None)
def cheb(kind,k):
 if kind=='T' and k==0:return Poly([1])
 out=[Q(0)]*(k+1)
 for a in range(k//2+1):
  i=k-2*a
  if kind=='T':out[i]=Q(k*(-1)**a*factorial(k-a-1)*2**i,2*factorial(a)*factorial(i))
  else:out[i]=Q((-1)**a*comb(k-a,a)*2**i)
 return Poly(out)

def binom(a,n):
 out=Q(1)
 for k in range(n):out*=(a-k)/Q(k+1)
 return out

def origin(data,c):
 delta=1-1/c;b=[Q(0)]*3;count=0;summands=0
 for g in data['generators']:
  m=int(g['m']);kind=g['spec'][0];w0=int(g['spec'][1])
  assert kind in ['mono','leg','legq','legqs'] and m>=0 and w0>=0
  if m+w0>2:continue
  n=0 if kind=='mono' else int(g['spec'][2]);q=int(g['spec'][3]) if kind in ['legq','legqs'] else 0
  R=Q(g['spec'][4]) if kind=='legqs' else Q(1);assert R>0
  p=(3+1/c-int(g['j'])*delta)/2;count+=1
  for k in range(min(n,2-m-w0)+1):
   length=2-m-w0-k;d=w0+q+k
   series=sum((binom(p-m,i)*binom(Q(-d),length-i)/R**(2*(length-i)) for i in range(length+1)),Q(0))
   factor=Q(g['coef'])*((-1)**(n+k)*comb(n,k)*comb(n+k,k))/R**(2*(w0+k))
   b[m]+=factor*series;summands+=1
 b0,b1,b2=b;a22=2*b0-6*b2;a04=b0-b1+b2
 return {'a0':-4*a22-24*a04,'strain':4*a22,'x2y2_coefficient':a22,'y4_coefficient':a04},count,summands

if __name__=='__main__':
 start=time.monotonic();ctx.prec=2048
 manifest=json.loads((BASE/'data/manifest.json').read_text());assert sha(BASE/'PROOF.md')==manifest['proof_sha256']
 for rel,h in manifest['files'].items():assert sha(ROOT/rel)==h,rel
 peer=json.loads((BASE/'source/N4_reconstruction.json').read_text());raw=BASE/'data/017.json'
 assert sha(raw)==peer['raw_sha256']=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114'
 assert sha(BASE/'data/N4_polynomials.json.gz')==peer['polynomial_sha256']=='6887cdc6cdcc02fd0a7733d0343188df67c42c653e1a82ec033b2a207a08e872'
 data=json.loads(raw.read_text());engine=load('independent_gradient',ROOT/'research/scaled_hessian_audit/code/check.py');f=engine.f
 c,delta,rho,stream=f.fields(data);rx,kx=engine.derive(rho,1,'s','x',delta);ry,ky=engine.derive(rho,1,'s','y',delta)
 assert kx=='s' and ky=='c'
 print('POLAR FIELDS',len(rx),len(ry),'seconds',time.monotonic()-start,flush=True)
 common=tuple(max(A.powers[i] for field in [rx,ry] for A in field.values()) for i in range(2));assert common==(0,19)
 D=(1+2499*f.V)**19
 # Check every closed Chebyshev polynomial against its defining recurrence.
 z=Poly([0,1]);chebchecks=0
 for kind in ['T','U']:
  assert cheb(kind,0)==Poly([1]);assert cheb(kind,1)==z*(1 if kind=='T' else 2)
  for k in range(2,81):assert cheb(kind,k)==2*z*cheb(kind,k-1)-cheb(kind,k-2);chebchecks+=1
 maps={};clearing=0
 for label,field in [('rx',rx),('ry',ry)]:
  for (j,n),A in field.items():
   assert n%2==0 and (label=='ry' or n>0)
   den=Poly([1])
   for L,power in zip(f.F.LINEARS,A.powers):den*=L**power
   complement,remainder=divmod(D,den);assert not remainder
   cleared=A.P*complement;assert cleared*den==A.P*D;clearing+=1
   angle=cheb('T',n//2) if label=='ry' else cheb('U',n//2-1)
   out=maps.setdefault(f'{label}_{j+1}',{})
   for i,a in enumerate(cleared):
    if a:
     for k,b in enumerate(angle):
      if b:out[i,k]=out.get((i,k),Q(0))+a*b
  print('EXPANDED',label,'seconds',time.monotonic()-start,flush=True)
 maps={key:{ij:v for ij,v in vals.items() if v} for key,vals in maps.items()}
 with gzip.open(BASE/'data/N4_polynomials.json.gz','rt') as handle:target=json.load(handle)
 assert target['raw_sha256']==sha(raw) and Q(target['delta'])==delta and Q(target['c_exact'])==c
 assert D==Poly([Q(q) for q in target['denominator']])
 assert set(maps)==set(target['polynomials'])
 counts={};digests={};count=0
 for key,rows in target['polynomials'].items():
  expected={(i,k):Q(q) for i,k,q in rows};assert len(rows)==len(expected)
  assert maps[key]==expected,key
  counts[key]=len(expected);count+=len(expected);h=sha256()
  for (i,k),q in sorted(expected.items()):h.update(f'{i},{k}:{q}\n'.encode())
  digests[key]=h.hexdigest()
 assert count==40082==peer['nonzero_coefficients']
 assert max(i for vals in maps.values() for i,k in vals)==103==peer['degree_t']
 assert max(k for vals in maps.values() for i,k in vals)==80==peer['degree_z']
 print('ALL COEFFICIENTS EQUAL',count,'seconds',time.monotonic()-start,flush=True)
 O,ot,os=origin(data,c);assert c+O['strain']==1 and O['a0']>0
 op=json.loads((BASE/'source/N4_direct.json').read_text());assert op['generator_sha256']==sha(raw)
 originchecks={k:v==Q(op['origin'][k]) for k,v in O.items()};assert all(originchecks.values())
 originpolys={}
 for label in ['rx','ry']:
  values={}
  for key,field in maps.items():
   if key.startswith(label+'_'):
    for (i,k),q in field.items():
     if i==0:values[k]=values.get(k,Q(0))+q
  values={k:v for k,v in values.items() if v};originpolys[label]=values
 assert not originpolys['rx'];assert originpolys['ry']=={0:O['a0']*D(0)}
 points=[]
 for p in peer['point_checks']:
  vals=f.evaluation(c,delta,rho,stream,p['x'],p['y']);rows={}
  for label in ['rx','ry']:
   value=vals['rho_x' if label=='rx' else 'rho_y'];assert value.overlaps(arb(p['fields'][label]['value'])) and value.rel_accuracy_bits()>150
   rows[label]={'value':value.str(100),'peer_overlap':True,'bits':value.rel_accuracy_bits()}
  points.append({'x':p['x'],'y':p['y'],'fields':rows})
 result={'utc':now(),'candidate':peer['candidate'],'raw_sha256':sha(raw),'peer_polynomial_sha256':sha(BASE/'data/N4_polynomials.json.gz'),'precision_bits':ctx.prec,'polar_group_counts':{'rx':len(rx),'ry':len(ry)},'exact_clearing_checks':clearing,'closed_chebyshev_recurrence_checks':chebchecks,'all_exact_coefficients_equal':True,'nonzero_coefficients':count,'coefficient_counts':counts,'coefficient_sha256':digests,'denominator_powers':list(common),'denominator_degree':D.degree(),'degree_t':103,'degree_z':80,'origin':{k:str(v) for k,v in O.items()},'origin_contributing_generators':ot,'origin_contributing_summands':os,'origin_N4_checks':originchecks,'origin_polynomial_checks':True,'point_checks':points,'inputs':{**manifest['files'],str((BASE/'PROOF.md').relative_to(ROOT)):sha(BASE/'PROOF.md'),str((BASE/'data/manifest.json').relative_to(ROOT)):sha(BASE/'data/manifest.json'),str(Path(__file__).relative_to(ROOT)):sha(__file__)},'foreign_code_executed':False,'complete_cover_claimed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED full exact candidate017 gradient reconstruction and independent origin jet'}
 with (BASE/'verification/result.json').open('x') as handle:json.dump(result,handle,indent=2);handle.write('\n')
 print('DONE',result['utc'],'seconds',result['elapsed_seconds'],flush=True)
