"""Fresh-original complex Fourier differentiation audit, no sine recurrence import."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=768
H=Path(__file__).resolve().parent;B=H.parents[1];start=time.monotonic()
sys.path.insert(0,str(B/'source_audit'));import recover_state as rec
rec.HERE=H;rec.COPY=Path('case4/IPM_case4.artifacts')
c0,coeffs,meta=rec.read_state(131);c=Q(str(c0));delta=1-1/c
zero=(Q(0),Q(0))
def inc(F,k,z):
 old=F.get(k,zero);F[k]=(old[0]+z[0],old[1]+z[1])
def clean(F):return {k:z for k,z in F.items() if z!=zero}
def plus(*terms):
 out={}
 for a,F in terms:
  for k,(re,im) in F.items():inc(out,k,(a*re,a*im))
 return clean(out)
def derivative(F,p,axis):
 out={}
 for k,(re,im) in F.items():
  a=(p-k)/2;b=(p+k)/2
  if axis=='x':inc(out,k+1,(a*re,a*im));inc(out,k-1,(b*re,b*im))
  else:inc(out,k+1,(a*im,-a*re));inc(out,k-1,(-b*im,b*re))
 return clean(out)
def conv(F,G):
 out={}
 for k,(a,b) in F.items():
  for l,(c,d) in G.items():inc(out,k+l,(a*c-b*d,a*d+b*c))
 return clean(out)
def csine(a):
 out={}
 for k,v in a.items():out[k]=(Q(0),-v/2);out[-k]=(Q(0),v/2)
 return clean(out)
def ccosine(a):
 out={}
 for k,v in a.items():
  if k==0:inc(out,0,(v,Q(0)))
  else:inc(out,k,(v/2,Q(0)));inc(out,-k,(v/2,Q(0)))
 return clean(out)
def stream(F,p):
 rhs=derivative(F,p,'x');out={}
 for k,z in rhs.items():
  den=k*k-(p+1)**2;assert den;out[k]=(z[0]/den,z[1]/den)
 return clean(out)
def from_potential(C,s):
 lap=plus((1,derivative(derivative(C,s,'x'),s-1,'x')),(1,derivative(derivative(C,s,'y'),s-1,'y')))
 return plus((-1,derivative(lap,s-2,'y')))
def sine(F):
 out={}
 for k,(re,im) in F.items():
  assert not re
  if k>0:
   assert F[-k]==(Q(0),-im);out[k]=-2*im
 return out
C1={}
for (j,m,k),v in zip(rec.CANON,coeffs):
 if j==0:C1[2*m]=C1.get(2*m,Q(0))+Q(str(v))
C=ccosine(C1);T={1:from_potential(C,4-delta)};P={1:stream(T[1],1-delta)};S={}
for n in range(2,9):
 terms=[]
 for i in range(1,n):
  j=n-i;pi=1-i*delta;pj=1-j*delta
  terms.extend([(-1,conv(derivative(P[i],pi+1,'y'),derivative(T[j],pj,'x'))),(1,conv(derivative(P[i],pi+1,'x'),derivative(T[j],pj,'y')))])
 S[n]=plus(*terms);T[n]=plus((1/((n-1)*(c-1)),S[n]));P[n]=stream(T[n],1-n*delta)
 assert not plus((c*(1-n*delta)-1,T[n]),(1,S[n]))
 print('fourier order',n,'seconds',time.monotonic()-start,flush=True)
firstp=H/'recur_sine.json';d=json.loads(firstp.read_text())
assert meta['canonical_serialization_sha256']==d['original_canonical_sha256']
for n in range(1,9):
 row=d['orders'][str(n)];assert T[n]==csine({int(k):Q(v) for k,v in row['density'].items()})
 assert P[n]==csine({int(k):Q(v) for k,v in row['stream'].items()})
 Cp=ccosine({int(k):Q(v) for k,v in row['potential'].items()});p=1-n*delta
 assert from_potential(Cp,p+3)==T[n]
 assert derivative(derivative(Cp,p+3,'x'),p+2,'y')==P[n]
E=sine(S[8]);assert E=={int(k):Q(v) for k,v in d['order8_fixed_defect']['sine_coefficients'].items()}
norm=(arb.pi()*sum((arb(v)**2 for v in E.values()),arb(0))).sqrt();assert norm.overlaps(arb(d['order8_fixed_defect']['norm']['full_circle']))
assert norm>arb('9679.9655') and norm<arb('9679.9656')
# A pre-existing six-branch residual at this same exponent omits the two interactions involving order7.
old=plus(*[term for i in range(2,7) for term in [(-1,conv(derivative(P[i],2-i*delta,'y'),derivative(T[8-i],1-(8-i)*delta,'x'))),(1,conv(derivative(P[i],2-i*delta,'x'),derivative(T[8-i],1-(8-i)*delta,'y')))]] )
oldnorm=(arb.pi()*sum((arb(v)**2 for v in sine(old).values()),arb(0))).sqrt()
for rel,h in d['dependencies'].items():assert sha256((B/rel).read_bytes()).hexdigest()==h
assert d['code_sha256']==sha256((H/'recur_sine.py').read_bytes()).hexdigest()
assert sha256(Path(d['producer_path']).read_bytes()).hexdigest()==d['producer_sha256']
maxC=max(abs(Q(v)) for v in d['orders']['7']['potential'].values())
files=[firstp,H/'recur_sine.py',H.parent/'PROOF.md',B/'source_audit/recover_state.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED independent complex Fourier recurrence, density and potential reconstruction, and order7 comparison','precision_bits':ctx.prec,'all_eight_density_stream_and_potential_orders_match':True,'producer_all70_order7_coefficients_match':True,'new_seven_branch_7_0_full_circle_norm':norm.str(75),'new_seven_branch_7_0_first_quadrant_norm':(norm/2).str(75),'old_six_branch_7_0_full_circle_norm':oldnorm.str(75),'old_six_branch_7_0_first_quadrant_norm':(oldnorm/2).str(75),'order7_max_potential_magnitude':arb(maxC).str(75),'order7_first_density_coefficients':{k:arb(Q(d['orders']['7']['density'][k])).str(40) for k in ['1','3','5']},'new_defect_power':arb(1-8*delta).str(75),'descendant_2_1_power':arb(-1-3*delta).str(75),'strict_full_circle_bounds':['9679.9655','9679.9656'],'dependencies':{str(f.relative_to(B)):sha256(f.read_bytes()).hexdigest() for f in files},'source_json_sha256':meta['source_json_sha256'],'original_canonical_sha256':meta['canonical_serialization_sha256'],'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
H.joinpath('audit_fourier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
