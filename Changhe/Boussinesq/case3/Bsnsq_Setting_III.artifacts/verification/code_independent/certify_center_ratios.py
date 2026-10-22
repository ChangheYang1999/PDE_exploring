"""Packet163 exact rational residual lower bounds; own packet160 moment input."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,hashlib,shutil,time
import numpy as np
import sympy as sp
from certify_center_strain import block,q,encode,bounds

def symbolic_controls():
 x,y,b,c,a,aa,dd,e,f,g=sp.symbols('x y beta c a aa dd e f g',real=True)
 psi=c*x*y+aa*x**3+dd*x*y**2+e*x**3*y+f*x*y**3
 theta=x*x*(a+g*y+x*x+y*y)
 omega=-sp.diff(psi,x,2)-sp.diff(psi,y,2);F=sp.cancel(theta/x**2);G=sp.cancel(omega/x)
 W1=b*x-sp.diff(psi,y);W2=b*y+sp.diff(psi,x);A=sp.cancel(W1/x);at=lambda h:sp.simplify(h.subs({x:0,y:0}));qq=at(G);mm=c-1-b/2
 ft=[A*(2*F+x*sp.diff(F,x)),W2*sp.diff(F,y),-(b-2)*F]
 gt=[A*(G+x*sp.diff(G,x)),W2*sp.diff(G,y),G,-2*F-x*sp.diff(F,x)]
 tests=[('RF',at(sum(ft))+2*mm*a),('RG',at(sum(gt))-((b-c+1)*qq-2*a)),('NF_term1',at(ft[0])-2*(b-c)*a),('NF_term2',at(ft[1])),('NF_term3',at(ft[2])+(b-2)*a),('NG_term1',at(gt[0])-(b-c)*qq),('NG_term2',at(gt[1])),('NG_term3',at(gt[2])-qq),('NG_term4',at(gt[3])+2*a)]
 out=[{'name':k,'difference':str(sp.simplify(v)),'pass':sp.simplify(v)==0} for k,v in tests]
 # Exact rational inputs test either sign, cancellation and triangle bounds.
 rational=[]
 for bb in [Q(1),Q(2),Q(7,2)]:
  for cc in [Q(-2),Q(0),Q(1)+bb/2,Q(5)]:
   for av,qv in [(Q(1),Q(4)/bb),(Q(-2),Q(3)),(Q(0),Q(0))]:
    A0=bb-cc;rf=(2*A0-bb+2)*av;rg=(A0+1)*qv-2*av;nf=abs(2*A0*av)+abs((bb-2)*av);ng=abs(A0*qv)+abs(qv)+abs(2*av)
    ok=abs(rf)<=nf and abs(rg)<=ng and (nf!=0 or rf==0) and (ng!=0 or rg==0)
    rational.append({'beta':str(bb),'c':str(cc),'a':str(av),'q':str(qv),'pass':ok})
 return {'symbolic':out,'rational':rational,'all_passed':all(t['pass'] for t in out+rational)}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('archives',nargs='+');args=p.parse_args();root=Path(args.output);root.mkdir(parents=True,exist_ok=True);(root/'archives').mkdir(exist_ok=True);utc=datetime.now(timezone.utc).isoformat();start=time.monotonic();rows=[]
 for file in args.archives:
  src=Path(file);dest=root/'archives'/src.name;sha=hashlib.sha256(src.read_bytes()).hexdigest()
  if dest.exists():assert hashlib.sha256(dest.read_bytes()).hexdigest()==sha
  else:shutil.copyfile(src,dest)
  with np.load(dest,allow_pickle=False) as z:
   meta={k:z[k].item() for k in z.files if z[k].ndim==0};assert meta.get('source_mode')=='fixed_velocity_block' and meta['eps']==1
   own,cs=block(meta,z['cG']);seed,cf=block(meta,z['cG_f'],True);bb=q(meta['beta']);lam=q(meta['lam']);av=q(z['cF'].ravel()[0]);qv=q(z['cG'].ravel()[0]);inv={}
   for kind,cc in [('self',cs),('forced',cs+lam*cf)]:
    aa=bb-cc;mm=cc-1-bb/2;rf=-2*mm*av;rg=(aa+1)*qv-2*av;nf=abs(2*aa*av)+abs((bb-2)*av);ng=abs(aa*qv)+abs(qv)+abs(2*av);assert nf>0 and ng>0
    vals={'c':cc,'A':aa,'m':mm,'RF':rf,'RG':rg,'NF':nf,'NG':ng,'ratioF':abs(rf)/nf,'ratioG':abs(rg)/ng}
    inv[kind]={'values':{k:encode(v) for k,v in vals.items()},'bounds':{k:bounds(v) for k,v in vals.items()}}
   cert={'schema':'verification-exact-center-ratios-v1','archive':str(dest),'original':str(src),'archive_sha256':sha,'parameters':{'beta':encode(bb),'lambda':encode(lam),'a':encode(av),'q':encode(qv)},'self_block':own,'seed_block':seed,'inverse':inv,'diagnostics':{k:meta[k] for k in ['obj','strain_mismatch','continuation_accepted','converged','inner_converged'] if k in meta},'claim':'Exact center ratios are lower bounds for full-domain normalized suprema of these literal fields; self inverse defines B2, forced is only a labeled diagnostic.'}
   path=root/(src.stem+'.certificate.json');path.write_text(json.dumps(cert,indent=2)+'\n')
   rows.append({'certificate':str(path),'archive_sha256':sha,'beta':float(bb),'lambda':float(lam),'self_ratio_F':float(Q(**{ 'numerator':int(inv['self']['values']['ratioF']['numerator']),'denominator':int(inv['self']['values']['ratioF']['denominator'])})),'forced_m':float(Q(int(inv['forced']['values']['m']['numerator']),int(inv['forced']['values']['m']['denominator']))),'diagnostics':cert['diagnostics']})
 controls=symbolic_controls();data={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'certificates':rows,'controls':controls,'all_controls_passed':controls['all_passed']};(root/'generation.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({k:v for k,v in data.items() if k!='controls'},indent=2));assert controls['all_passed']
if __name__=='__main__':main()
