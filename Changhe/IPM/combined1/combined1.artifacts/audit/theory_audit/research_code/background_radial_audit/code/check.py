from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
import importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1];helper=BASE.parent/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T,U,Z=m.T,m.U,m.ZERO;ar,td=m.ar,m.td
H=lambda p:sha256(p.read_bytes()).hexdigest()
def add(rows,j,kind,n,p):
 if n<0:
  n=-n
  if kind=='s':p=-p
 if not p or (kind=='s' and n==0):return
 key=j,kind,n;rows[key]=rows.get(key,Z)+p
 if not rows[key]:del rows[key]
def derive(rows,k,axis,delta):
 out={}
 for (j,kind,n),p in rows.items():
  D=td(p,(j+1)*delta/2,k)
  if axis=='x':
   add(out,j,kind,n+1,(D-n*p)/2);add(out,j,kind,n-1,(D+n*p)/2)
  elif kind=='s':
   add(out,j,'c',n+1,(n*p-D)/2);add(out,j,'c',n-1,(n*p+D)/2)
  else:
   add(out,j,'s',n+1,(D-n*p)/2);add(out,j,'s',n-1,-(D+n*p)/2)
 return out
def normalize(rows):
 out={}
 for key,p in rows.items():
  assert p[0]==0,key
  out[key]=P(list(p)[1:])
 return out
def squares(rows):
 modes={};groups={}
 for (j,kind,n),p in rows.items():modes.setdefault((kind,n),[]).append((j,p(U)))
 for (kind,n),terms in modes.items():
  for i,(j,p) in enumerate(terms):
   for k,q in terms[i:]:
    f=(2 if kind=='c' and n==0 else 1)*(1 if k==j else 2)
    groups[j+k]=groups.get(j+k,Z)+f*U*p*q
 return {k:v for k,v in groups.items() if v}
def plus(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,Z)+v
 return {k:v for k,v in out.items() if v}
def integral(G,delta,r):
 v=1/(1+r*r);out=arb(0)
 for k,p in G.items():
  a=(k+2)*delta/2;assert a>0
  # Horner evaluates the exact finite antiderivative in one outward power.
  Panti=P([x/(a+i) for i,x in enumerate(p)])
  out+=ar(v)**ar(a)*ar(Panti(v))
 return arb.pi()/2*out
def whole(G,delta):return sum((x/((k+2)*delta/2+i) for k,p in G.items() for i,x in enumerate(p) if x),Q(0))
def run():
 start=time.monotonic();ctx.prec=1536
 data=json.loads((BASE/'data/canonical.json').read_text());prior=json.loads((BASE/'data/full_background.json').read_text());target=json.loads((BASE/'source/N4_result.json').read_text())
 c,delta,rho,psi=m.fields(data);Rho={(j,'s',n):p for (j,n),p in rho.items()}
 dx=derive(Rho,1,'x',delta);dy=derive(Rho,1,'y',delta)
 xx=normalize(derive(dx,0,'x',delta));xy=normalize(derive(dx,0,'y',delta));yy=normalize(derive(dy,0,'y',delta))
 assert xy==normalize(derive(dy,0,'x',delta))
 print('second derivatives',len(xx),len(xy),len(yy),'seconds',time.monotonic()-start,flush=True)
 XX,XY,YY=map(squares,[xx,xy,yy]);gx,gy=plus(XX,XY),plus(YY,XY)
 print('square groups',len(gx),len(gy),'seconds',time.monotonic()-start,flush=True)
 r0=Q(1,50);rr=Fraction(float('8356.474846731926'));R=Q(rr.numerator,rr.denominator)
 assert str(R)==target['outer_radius_exact_binary64'] and str(r0)==target['inner_radius']
 energies={}
 for name,G in [('D_rho_x',gx),('D_rho_y',gy)]:
  exact=whole(G,delta);assert exact==Q(prior['norms'][name]['rational_energy_over_pi_half'])
  full=arb.pi()/2*ar(exact);ex0=integral(G,delta,r0);exR=integral(G,delta,R)
  values={'full':full,'origin':full-ex0,'middle':ex0-exR,'exterior':exR}
  assert all(v>0 for v in values.values());assert (values['origin']+values['middle']+values['exterior']).overlaps(full)
  assert all(v.overlaps(arb(target['derivative_squared_masses'][name][key])) for key,v in values.items())
  energies[name]=values;print(name,'all masses agree','seconds',time.monotonic()-start,flush=True)
 K={}
 for region in ['full','origin','middle','exterior']:
  K[region]=((arb(2).log()-arb(1)/2)*energies['D_rho_x'][region]+(3*arb(2).log()-2)*energies['D_rho_y'][region])/(16*arb.pi())
  assert K[region].overlaps(arb(target['kappa_squared_masses'][region]))
 reported=Fraction(target['reported_floating_kappa']);reported=ar(Q(reported.numerator,reported.denominator))
 more={'kappa_full':K['full'].sqrt(),'kappa_exact_middle':K['middle'].sqrt(),'reported_minus_exact_middle':reported-K['middle'].sqrt(),'missing_origin_fraction_of_kappa_squared':K['origin']/K['full'],'missing_exterior_fraction_of_kappa_squared':K['exterior']/K['full']}
 assert all(v.overlaps(arb(target[k])) for k,v in more.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':target['candidate'],'source_sha256':H(BASE/'data/canonical.json'),'proof_sha256':H(BASE/'PROOF.md'),'code_sha256':H(Path(__file__)),'helper_sha256':H(helper),'peer_result_sha256':H(BASE/'source/N4_result.json'),'precision_bits':ctx.prec,'mixed_derivatives_agree_exactly':True,'full_rational_energies_agree':True,'all_17_ball_comparisons_agree':True,'inner_radius':str(r0),'outer_radius':str(R),'derivative_squared_masses':{n:{k:v.str(95) for k,v in rows.items()} for n,rows in energies.items()},'kappa_squared_masses':{k:v.str(95) for k,v in K.items()},**{k:v.str(95) for k,v in more.items()},'elapsed_seconds':time.monotonic()-start}
 (BASE/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print('Kappa',out['kappa_full'],'middle',out['kappa_exact_middle'],'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
