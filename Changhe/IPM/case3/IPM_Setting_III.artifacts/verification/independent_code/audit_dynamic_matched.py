"""Matched-time DR audit with independently reconstructed new basis and full inverse.
All CPU work is one-threaded. No producer modules are imported.
"""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,hashlib,json,math,time
import numpy as np
import mpmath as mp
from scipy.special import roots_legendre
from q_local_checkpoint import QLocalCheckpoint
from q_local_angular import LocalAngular
from q_exact_jets import jets,pack
from q_mp_primitives import MPQPrimitives,guard_digits,mf
from complementary_inverse_charts import point_fields
from audit_dynamic_snapshots import grid,summary,mp_value
from direct_inverse import cartesian_gradient


def compact_exact(v):
 if isinstance(v,F):
  out={'approx':float(v),'numerator_bits':v.numerator.bit_length(),'denominator_bits':v.denominator.bit_length(),'exact_hex_sha256':hashlib.sha256((hex(v.numerator)+'/'+hex(v.denominator)).encode()).hexdigest()}
  if max(v.numerator.bit_length(),v.denominator.bit_length())<8000:out['exact']=str(v)
  return out
 if isinstance(v,dict):return {k:compact_exact(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [compact_exact(x) for x in v]
 return v

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='matched_main');ap.add_argument('--times',default='20,0,5,10,15');ap.add_argument('--sizes',default='64,96,128');ap.add_argument('--suffix',default='');ap.add_argument('--skip-grid',action='store_true');args=ap.parse_args()
 folder=Path('research/dynamic_local_reconstruction/verification')/args.tag;folder.mkdir(parents=True,exist_ok=True)
 gate=Path('research/dynamic_local_reconstruction/verification/READER_GATE.json');assert json.loads(gate.read_text())['status']=='PASS'
 result={'started_utc':utc(),'status':'RUNNING','code_sha256':sha(__file__),'reader_sha256':sha('independent_code/q_local_checkpoint.py'),'proof_sha256':sha('research/dynamic_local_reconstruction/PROOF.md'),'gate_sha256':sha(gate),'states':[],'scope':'Independent full inverse of saved densities. Exact binary shifted-node convention recorded. Finite sampled checks; no uniform bounds or continuum convergence claim.'}
 def save():result['updated_utc']=utc();(folder/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
 save()
 points=[(.5,.5),(3.,0.),(0.,3.),(6.,8.),(30.,40.)]
 for tau in map(int,args.times.split(',')):
  for N in map(int,args.sizes.split(',')):
   src=Path('numerics/runs')/f'drY_C3.0_N{N}{args.suffix}_tau{tau:08.3f}.pt'
   if not src.exists():raise FileNotFoundError(src)
   frozen=folder/src.name;frozen.write_bytes(src.read_bytes());q=QLocalCheckpoint(frozen);assert float(q.data['tau'])==tau
   q.save_snapshot(folder/(src.stem+'.numeric.npz'));(folder/(src.stem+'.nodes.json')).write_text(json.dumps([float(x).hex() for x in q.tk],indent=2)+'\n')
   cw=float(q.data['cw']);cx=float(q.data['cx']);C=float(q.data['C']);assert cw>0
   row={'N':N,'M':q.M,'tau':tau,'frozen':str(frozen),'sha256':sha(frozen),'basis':q.basis,'rcond':float(q.data['rcond']),'cw':cw,'cx':cx,'producer_c':float(q.data['c']),'node_reconstruction':q.node_reconstruction_details(),'grid':[],'points':[]}
   result['states'].append(row);save();start=time.monotonic()
   coeff=q.exact_coefficients();row['conversion_seconds']=time.monotonic()-start
   jj=jets(coeff[:4],F(q.kappa),F(C));row['exact_center']=compact_exact({k:v for k,v in jj.items()if not k.endswith('polynomial')})
   row['canonical_c']=float(jj['c']);row['c_error']=float(jj['c']-F(float(q.data['c'])))
   row['a0star']=float(jj['a']/F(cw));row['normalized_center_defect']=float(F(C)+jj['c']/F(cw)-1)
   row['cubic_b']=float(jj['b_core'])*2**(2*q.kappa)/q.L**2;row['cubic_e']=float(jj['e_core'])*2**(2*q.kappa)/q.L**2
   model=LocalAngular(q);row['double_quadrature_strain']=model.c
   # Full upper half vertical strain moment, all exterior radii integrated to infinity.
   row['moments']=[]
   for order in [(N+6)//2,N+12]:
    gl,gw=roots_legendre(order);rr=[]
    for R in [0.,1.,10.,100.]:
     t0=-1. if R==0 else float(q.coordinates(np.array(R))[0]);t=t0+(1-t0)*(gl+1)/2;s=(1+t)/2
     it=((1-t)/16+q.kappa*s/4)*(q.polynomial(1,t)-s*q.polynomial(2,t))
     rr.append(float((1-t0)/2*np.sum(gw*it)))
    row['moments'].append({'order':order,'radii':[0,1,10,100],'values':rr})
   save()
   if not args.skip_grid:
    r=np.unique(np.r_[np.geomspace(.002,1,22),np.geomspace(1.02,100,22),np.geomspace(110,1e4,12)])
    theta=np.unique(np.r_[1e-6,.0007,(np.arange(27)+.37)*math.pi/(2*27),math.pi/2-1e-6]);logr=np.log(r)
    for order in [96,192]:
     z=grid(model,logr,theta,order,cw,C,cx);s,peaks=summary(z,logr,theta)
     row['grid'].append({'order':order,'radii':len(r),'angles':len(theta),'summary':s,'peaks':peaks});save()
   # Quadrature at requested physical points uses an independent log-radius Green rule.
   x=np.array([p[0] for p in points]);y=np.array([p[1] for p in points]);lr=np.log(np.hypot(x,y));theta=np.arctan2(y,x)
   quadvals=point_fields(model,lr,theta,order=192)
   for pt,v in zip(points,quadvals):row['points'].append({'point':list(pt),'quadrature_fields':v,'multiprecision':[]})
   for digits in [50,80]:
    with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
     mm=MPQPrimitives(coeff,F(q.L),F(q.kappa),F(C))
     for pt in row['points']:
      x,y=pt['point'];v=mm.at(mf(x),mf(y));gx,gy=v['gradient'];ux,uy=v['U'];rho=v['rho']
      tx=(mf(C)*mf(x)+ux/mf(cw))*gx/mf(cw);ty=(mf(C)*mf(y)+uy/mf(cw))*gy/mf(cw)
      rs=tx+ty-rho/mf(cw);nf=abs(tx)+abs(ty)+abs(rho/mf(cw));nv=abs(rho/mf(cw))+abs(mf(x)*gx+mf(y)*gy)/mf(cw)+abs(ux*gx+uy*gy)/mf(cw)**2
      v.update(rho_star=rho/mf(cw),gradient_star=[gx/mf(cw),gy/mf(cw)],U_star=[ux/mf(cw),uy/mf(cw)],R_star=rs,Nf_star=nf,Nv_star=nv,Rstar_Nf=abs(rs)/nf if nf else None,Rstar_Nv=abs(rs)/nv if nv else None,G=mf(cw)*rho-(mf(cx)*mf(x)+ux)*gx-(mf(cx)*mf(y)+uy)*gy)
      v['identity_error']=rs+v['G']/mf(cw)**2
      pt['multiprecision'].append({'digits':digits,'work_digits':mp.mp.dps,'fields':mp_value(v,digits)})
     save()
   with mp.workdps(100):
    for pt in row['points']:
     a,b=[item['fields'] for item in pt['multiprecision']]
     pt['precision_Rstar_abs_difference']=str(abs(mp.mpf(a['R_star'])-mp.mpf(b['R_star'])))
     # Cartesian finite differences of direct shifted density, distinct from all spectral differentiation.
     x,y=pt['point'];fd=[]
     for h in [2e-3,8e-4,3e-4]:
      gx,gy=cartesian_gradient(q.rho,float(x),float(y),h)
      fd.append({'h':h,'gradient':[float(gx),float(gy)],'absolute_errors':[float(abs(mp.mpf(float(gx))-mp.mpf(b['gradient'][0]))),float(abs(mp.mpf(float(gy))-mp.mpf(b['gradient'][1])))]})
     pt['finite_difference']=fd
   row['elapsed_seconds']=time.monotonic()-start;row['status']='COMPUTED';save();print(json.dumps({'utc':utc(),'N':N,'tau':tau,'c':row['canonical_c'],'a0star':row['a0star'],'elapsed':row['elapsed_seconds']}),flush=True)
 result['status']='COMPUTED';result['finished_utc']=utc();save()

if __name__=='__main__':main()
