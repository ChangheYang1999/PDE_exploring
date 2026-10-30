"""Whole radial-axis mass from finite exact power antiderivatives."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from pipeline import load,source,DATA
from norms import endpoint
from radial import ar
BASE=ROOT/'research/radial_mass'
def run(name):
 ctx.prec=2048;start=time.monotonic();canonical=source(name);delta=1-1/fmpq(json.loads(canonical.read_text())['cl'])
 D=load(name,0)[0,0];modes={};t=arb_poly([1,-1]);groups={}
 for (ell,kind,n),P in D.items():
  assert kind=='s' and n>0
  q,Q=endpoint(P);assert -4+ell*delta+2*q>-1
  modes.setdefault(n,[]).append((ell,q,arb_poly([ar(v) for v in Q])))
 print('loaded and endpoint checked',time.monotonic()-start,flush=True)
 for n,rows in modes.items():
  for i,(ell,q,P) in enumerate(rows):
   for ell2,q2,Q in rows[i+1:]:assert ((ell-ell2)*delta/2).denominator!=1
   for j in range(i,len(rows)):
    ell2,q2,Q=rows[j];b=-3+(ell+ell2)*delta/2+q+q2
    groups[b]=groups.get(b,arb_poly([]))+P*Q*t*(1 if i==j else 2)
 print('formed',len(groups),'groups',time.monotonic()-start,flush=True)
 results={};radii=['0','1/100','3/100','1/10','3/10','1','3','10','30','100','300','1000','10000','100000','1000000']
 for label,extra in [('G0',False),('rF',True)]:
  primitives=[]
  for b,P in groups.items():
   if extra:b-=1;P=P*t
   assert b>-1
   primitives.append((b+1,arb_poly([v/ar(b+k+1) for k,v in enumerate(P)])))
  def tail(R):
   U=fmpq(1)/(1+R*R);u=ar(U)
   return arb.pi()/2*sum((poly(u)*u**ar(exponent) for exponent,poly in primitives),arb(0))
  total=tail(fmpq(0));assert total>0
  tails=[tail(fmpq(R)) for R in radii];rows=[]
  for i,(R,value) in enumerate(zip(radii,tails)):
   mass=value-(tails[i+1] if i+1<len(tails) else 0);assert mass>0,(label,R,mass)
   rows.append({'inner_radius':R,'outer_radius':radii[i+1] if i+1<len(radii) else 'infinity',
                'tail_squared_mass':value.str(65),'tail_mass_fraction':(value/total).str(45),
                'annular_squared_mass':mass.str(65),'annular_mass_fraction':(mass/total).str(45)})
  results[label]={'total_squared_mass':total.str(75),'norm':total.sqrt().str(65),'annuli':rows}
  print(label,'norm',total.sqrt().str(25),'seconds',time.monotonic()-start,flush=True)
  for row in rows:
   if row['inner_radius'] in ['10','30','100','1000','10000']:print('tail',row['inner_radius'],row['tail_mass_fraction'],flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'precision_bits':ctx.prec,
      'canonical_sha256':sha256(canonical.read_bytes()).hexdigest(),'polynomial_sha256':sha256((DATA/f'{name}_D0.json.gz').read_bytes()).hexdigest(),
      'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'components':results,'elapsed_seconds':time.monotonic()-start}
 (BASE/f'verification/{name}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run(sys.argv[1])
