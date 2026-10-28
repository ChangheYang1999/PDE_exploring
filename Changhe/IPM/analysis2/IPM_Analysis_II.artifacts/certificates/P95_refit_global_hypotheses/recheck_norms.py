"""Independent power restriction and Taylor convolution for derivative norms."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,argparse
from flint import arb,arb_mat,ctx
from recheck_fast import A,restrict,convert,T,endpoints,tree,maxabs
sys.set_int_max_str_digits(0)
here=Path(__file__).parent

def make_fields(d,e,kind):
 raw={key:{(i,z):F(v) for i,z,v in rows} for obj in [d,e] for key,rows in obj['polynomials'].items()}
 if kind=='fourth':defs={'d22':{'chi22':1},'d13':{'chi13':1},'d31':{'chi31':1},'ry':{'chi22':-1,'chi04':-1},'rx':{'chi31':-1,'chi13':-1}}
 elif kind=='D2u':defs={s:{s:1} for s in ['chi41','chi32','chi23','chi14']}
 elif kind=='D2rho':defs={'rxx':{'chi41':-1,'chi23':-1},'rxy':{'chi32':-1,'chi14':-1},'ryy':{'chi23':-1,'chi05':-1}}
 else:defs={s:{s:1} for s in ['u1','u2']}
 out={}
 for label,terms in defs.items():
  for j in range(6):
   pp={}
   for k,factor in terms.items():
    for ik,v in raw[f'{k}_{j}'].items():pp[ik]=pp.get(ik,F(0))+factor*v
   out[label,j]={ik:v for ik,v in pp.items() if v}
 return out,list(defs)

def upper_fields(P,nt,nz,a,b,c,d,delta,labels):
 from math import comb,factorial
 radial=restrict(nt,str(a),str(b));angular=T(nz,str(c),str(d)).transpose();powers={key:radial*v*angular for key,v in P.items()};bern={key:convert(nt)*v for key,v in powers.items()}
 wl=(1-A(b))**A(delta/2);wh=(1-A(a))**A(delta/2)
 W=arb_mat([[sum((A(F(comb(n,l)*comb(i,l),comb(5,l)))*wl**(n-l)*(wh-wl)**l for l in range(min(n,i)+1)),arb(0)) for n in range(6)] for i in range(6)])
 bounds={label:maxabs((W*arb_mat([bern[label,j].entries() for j in range(6)])).entries()) for label in labels}
 if b==1:return bounds
 N=4;mult={};err={}
 for j in range(6):
  q=j*delta/2;fall=F(1);v=[]
  for l in range(N+1):
   if l:fall*=q-l+1
   v.append(A((-1)**l*fall/factorial(l))*A(b-a)**l*(1-A(a))**A(q-l))
  mm=arb_mat(nt+N+1,nt+1)
  for i in range(nt+1):
   for l in range(N+1):mm[i+l,i]=v[l]
  mult[j]=mm;err[j]=A(abs(fall*(q-N))/factorial(N+1))*A(b-a)**(N+1)*(1-A(b))**A(q-N-1)
 for label in labels:
  summ=arb_mat(nt+N+1,nz+1);error=arb(0)
  for j in range(6):summ+=mult[j]*powers[label,j];error+=err[j]*maxabs(bern[label,j].entries())
  upper=maxabs((convert(nt+N)*summ).entries())+error
  bounds[label]=bounds[label].min(upper.upper())
 return bounds

def ratios(vals,kind,a,b,c,d,delta):
 sq=lambda label:vals[label]**2
 co=(1+A(d))/2;si=(1-A(c))/2;sin2=arb(1) if c<=0<=d else 1-A(min(abs(c),abs(d)))**2
 t=A(b);w2=(1-A(a))**A(delta)
 if kind=='fourth':
  velocity=2*sq('d22')+sin2*(sq('d13')+sq('d31'));density=sq('ry')+sin2*sq('rx')
  return {'Du_fixed':velocity*w2/A(F(196,25)),'Drho_fixed':density*w2/256,'Du_decay':velocity/484,'Drho_decay_half':density/8649}
 if kind=='D2u':
  velocity=si*(sq('chi41')+3*sq('chi23'))+co*(3*sq('chi32')+sq('chi14'))
  return {'D2u_fixed':velocity*t*w2/9,'D2u_decay':velocity*t*t/3136}
 if kind=='D2rho':
  density=si*(sq('rxx')+sq('ryy'))+2*co*sq('rxy');peak=F(1,4) if a<=F(1,2)<=b else max(a*(1-a),b*(1-b))
  return {'D2rho_fixed':density*A(peak)*w2/9,'D2rho_weighted':density*t*w2/64,'D2rho_decay_half':density*t*t/8649}
 return {'u_decay':(co*sq('u1')+si*sq('u2'))/484}

def main(args):
 ctx.prec=640;start=time.monotonic();src=here/args.file;cert=json.loads(src.read_text());assert cert['status']=='COMPLETE';name=cert['name'];pp=here/f'{name}.polynomials.json';ee=here/f'{name}.derivatives.json';d=json.loads(pp.read_text());e=json.loads(ee.read_text());assert cert['source_sha256']==sha256(pp.read_bytes()).hexdigest() and cert['derivatives_sha256']==sha256(ee.read_bytes()).hexdigest();delta=F(d['delta']);assert delta>F(4,9)
 S,labels=make_fields(d,e,cert['kind']);nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p);P={}
 for key,p in S.items():
  mm=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():mm[i,k]=A(v)
  P[key]=mm
 paths={v['path'] for v in cert['accepted']};assert len(paths)==len(cert['accepted']);tree(paths);rows=[]
 for row in cert['accepted']:
  a,b,c,d=endpoints(row['path']);assert list(map(str,[a,b]))==row['t'] and list(map(str,[c,d]))==row['z'];vals=upper_fields(P,nt,nz,a,b,c,d,delta,labels);rat=ratios(vals,cert['kind'],a,b,c,d,delta);assert all(v<=1 for v in rat.values()),(row['path'],rat);rows.append({'path':row['path'],'ratios':{k:v.str(85) for k,v in rat.items()},'pass':True})
  if len(rows)%10==0:print(len(rows),'PASS',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'precision_bits':ctx.prec,'primary_sha256':sha256(src.read_bytes()).hexdigest(),'polynomials_sha256':sha256(pp.read_bytes()).hexdigest(),'derivatives_sha256':sha256(ee.read_bytes()).hexdigest(),'rows':rows,'leaves':len(rows),'seconds':time.monotonic()-start};src.with_name(src.stem+'.recheck.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],len(rows),'PASS',out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('file');main(ap.parse_args())
