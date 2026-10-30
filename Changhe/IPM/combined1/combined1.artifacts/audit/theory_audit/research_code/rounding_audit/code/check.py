from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
from math import comb
import importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
helper=BASE.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('ownpolar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T,U,Z=m.T,m.U,m.ZERO
ar,td,fields=m.ar,m.td,m.fields
H=lambda p:sha256(p.read_bytes()).hexdigest()
def rat(s):
 f=Fraction(s);return Q(f.numerator,f.denominator)
def canonical(gens,c):
 polys={}
 for g in gens:
  j,n=g['j'],g['m'];sp=g['spec'];coef=rat(g['coef'])
  if sp[0]=='mono':v=T**(n+sp[1])
  else:
   assert sp[0]=='leg';w,k=sp[1:]
   v=T**(n+w)*P([(-1)**(k+i)*comb(k,i)*comb(k+i,i) for i in range(k+1)])
  polys[j,n]=polys.get((j,n),Z)+coef*v
 pairs=sorted(((j,n,k),q) for (j,n),v in polys.items() for k,q in enumerate(v) if q)
 return {'cl':str(c),'order':[list(key) for key,q in pairs],'coefficients':[str(q) for key,q in pairs]},polys

def point(c,delta,rho,psi,x,y):
 r2=x*x+y*y;r=ar(r2).sqrt();t=r2/(1+r2);u=1/(1+r2);ct=ar(x)/r;st=ar(y)/r
 sn=[arb(0),st];cn=[arb(1),ct]
 for n in range(2,max(n for j,n in list(rho)+list(psi))+1):
  sn.append(sn[-1]*ct+cn[-1]*st);cn.append(cn[-1]*ct-sn[-2]*st)
 powers={j:ar(u)**ar((j+1)*delta/2) for j,n in list(rho)+list(psi)}
 density=arb(0);rr=arb(0);rt=arb(0);ur=arb(0);ut=arb(0)
 for (j,n),v in rho.items():
  a=(j+1)*delta/2;power=powers[j];value=ar(v(t));density+=r*power*value*sn[n]
  rr+=power*ar(td(v,a,1)(t))*sn[n];rt+=power*n*value*cn[n]
 for (j,n),v in psi.items():
  a=(j+1)*delta/2;power=powers[j];ur-=r*power*n*ar(v(t))*cn[n];ut+=r*power*ar(td(v,a,2)(t))*sn[n]
 rx=ct*rr-st*rt;ry=st*rr+ct*rt;u1=ct*ur-st*ut;u2=st*ur+ct*ut
 vx=ar(c*x)+u1;vy=ar(c*y)+u2;F=vx*rx+vy*ry-density
 return dict(rho=density,rho_x=rx,rho_y=ry,u1=u1,u2=u2,residual=F,velocity_norm=(vx*vx+vy*vy).sqrt(),gradient_norm=(rx*rx+ry*ry).sqrt())

def hom(c,delta,rho,psi,h):
 out={}
 def add(n,q):
  if n<0:n,q=-n,-q
  if n and q:out[n]=out.get(n,Q(0))+q
 for (i,n),v in rho.items():
  e=1/c-i*delta
  if i==h:add(n,(c*e-1)*v(1))
  for (j,k),s in psi.items():
   if i+j+1!=h:continue
   ee=1/c-j*delta;vv=v(1)*s(1)/2
   add(n+k,vv*(-k*e+n*(1+ee)));add(n-k,vv*(-k*e-n*(1+ee)))
 return {n:q for n,q in out.items() if q}

def run():
 start=time.monotonic();ctx.prec=1024
 data=json.loads((BASE/'data/exact_generators.json').read_text());target=json.loads((BASE/'source/N4_result.json').read_text())
 c=rat(data.get('cl_exact',data.get('cl')));gens=[];diffs=[]
 for g in data['generators']:
  a=Fraction(g['coef']);b=Fraction(float(a));assert float(g['coef_float'])==float(a)
  diffs.append(abs(a-b));gens.append(dict(g,coef=str(b)))
 canon,pot=canonical(data['generators'],c);canb,potb=canonical(gens,c)
 def mapping(d):return {tuple(k):rat(v) for k,v in zip(d['order'],d['coefficients']) if rat(v)}
 ref=json.loads((BASE/'data/exact_canonical.json').read_text());refb=json.loads((BASE/'source/N4_rounded_canonical.json').read_text())
 assert mapping(canon)==mapping(ref);assert mapping(canb)==mapping(refb)
 rounded_peer=json.loads((BASE/'source/N4_rounded_generators.json').read_text())
 assert len(gens)==len(rounded_peer['generators'])
 assert all(a==b for a,b in zip(gens,rounded_peer['generators']))
 cc,delta,rho,psi=fields(canon);cc2,delta2,rhob,psib=fields(canb);assert cc==cc2==c and delta==delta2
 def origin(r,s):return sum((v(0) for (j,n),v in r.items() if n==1),Q(0)),2*sum((v(0) for (j,n),v in s.items() if n==2),Q(0))
 a0,strain=origin(rho,psi);a0b,strainb=origin(rhob,psib)
 assert a0==rat(ref['a0']) and strain==rat(ref['strain']) and strain==1-c
 assert a0b==rat(refb['a0']) and strainb==rat(refb['strain'])
 assert strainb-strain==rat(target['strain_difference'])
 assert ar(a0b-a0).overlaps(arb(target['a0_difference_ball']))
 assert sum(d!=0 for d in diffs)==target['changed_coefficients'] and len(diffs)==target['coefficient_count']
 assert max(diffs)==Fraction(target['maximum_absolute_coefficient_error'])
 assert not hom(c,delta,rho,psi,0) and not hom(c,delta,rhob,psib,0)
 assert not hom(c,delta,rho,psi,1)
 leading=hom(c,delta,rhob,psib,1);assert leading
 norm=(arb.pi()*ar(sum((v*v for v in leading.values()),Q(0)))).sqrt()
 assert norm.overlaps(arb(target['leading_nonzero_forbidden_sector']['rounded_full_circle_norm']))
 assert 2/c-1==rat(target['leading_nonzero_forbidden_sector']['exponent']) and 2/c-1>-1
 Cp={n:v(1) for (j,n),v in pot.items() if j==0 and v(1)};Cpb={n:v(1) for (j,n),v in potb.items() if j==0 and v(1)}
 Gp={n:v(1) for (j,n),v in rho.items() if j==0 and v(1)};Gpb={n:v(1) for (j,n),v in rhob.items() if j==0 and v(1)}
 assert (Cp==Cpb)==target['leading_potential_unchanged'];assert (Gp==Gpb)==target['leading_density_unchanged']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':target['candidate'],'precision_bits':ctx.prec,'proof_sha256':H(BASE/'PROOF.md'),'code_sha256':H(Path(__file__)),'helper_sha256':H(helper),'source_sha256':H(BASE/'data/exact_generators.json'),'peer_result_sha256':H(BASE/'source/N4_result.json'),'canonical_maps_agree_exactly':True,'rounded_generator_vectors_agree_exactly':True,'coefficient_count':len(diffs),'changed_coefficients':sum(d!=0 for d in diffs),'maximum_coefficient_error':str(max(diffs)),'strain_difference':str(strainb-strain),'a0_difference':ar(a0b-a0).str(80),'leading_sector':{'h':1,'q':0,'exponent':str(2/c-1),'sine_coefficients':{str(k):str(v) for k,v in leading.items()},'full_circle_norm':norm.str(95)},'rounded_residual_not_in_L2':True,'points':[]}
 print('origin and leading sector agree, norm',norm.str(28),'seconds',time.monotonic()-start,flush=True)
 for row in target['points']:
  x,y=map(rat,row['point']);a=point(c,delta,rho,psi,x,y);b=point(c,delta,rhob,psib,x,y)
  diff={k:b[k]-a[k] for k in a};comp={k:v.overlaps(arb(row['differences'][k])) for k,v in diff.items()};assert all(comp.values()),comp
  e=diff['rho'];ex=diff['rho_x'];ey=diff['rho_y'];v1=diff['u1'];v2=diff['u2']
  expanded=(ar(c*x)+a['u1'])*ex+(ar(c*y)+a['u2'])*ey+v1*a['rho_x']+v2*a['rho_y']+v1*ex+v2*ey-e
  assert expanded.overlaps(diff['residual'])
  assert a['residual'].overlaps(arb(row['exact_residual'])) and b['residual'].overlaps(arb(row['rounded_residual']))
  out['points'].append({'point':row['point'],'differences':{k:v.str(95) for k,v in diff.items()},'comparisons':comp,'exact_residual':a['residual'].str(95),'rounded_residual':b['residual'].str(95),'residual_identity_agrees':True})
  print('point',row['point'],'dF',diff['residual'].str(28),flush=True)
 out['elapsed_seconds']=time.monotonic()-start
 (BASE/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print('seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
