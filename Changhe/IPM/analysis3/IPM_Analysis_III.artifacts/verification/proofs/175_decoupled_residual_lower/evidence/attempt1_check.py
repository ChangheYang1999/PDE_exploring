"""Selected-interval lower certificate in the new low target, all angular modes."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math,importlib.util,argparse,time
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
P=load('low_point',LANE/'proofs/105_residual_norm_point_audit/code/check_points.py');G=P.G;ANG=P.ANG;aa=P.aa
RUN=LANE/'proofs/134_residual_green_taylor/evidence/production_28'
CERT=LANE/'proofs/154_residual_final_audit/evidence/final_certificate.json'
SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def exact(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def moments(alpha,beta,n):
 out=[F(1),(alpha-beta)/(alpha+beta)]
 for j in range(1,n):out.append((2*(alpha-beta)*out[j]+(j-alpha-beta)*out[j-1])/(j+alpha+beta))
 return out[:n+1]
def mass(alpha,beta):return 2*aa(alpha).gamma()*aa(beta).gamma()/aa(alpha+beta).gamma()
def score(row):
 l,r=F(row['left']),F(row['right']);b=F(-1,2) if r<=0 else F(123,20)
 m=float(F(row['center_norm']['upper_exact'])+F(row['variation_bound']['upper_exact']))
 return m*m*math.exp(float(b*l))*math.expm1(float(b*(r-l)))/float(b)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=16);ap.add_argument('--bits',type=int,default=384);ap.add_argument('--tag',default='selected');args=ap.parse_args()
 ctx.prec=args.bits;ctx.threads=1;start=time.monotonic()
 cert=json.loads(CERT.read_text());assert cert['status']=='CONFIRMED'
 assert sha(SOURCE)==cert['source_sha256'];assert sha(RUN/'leaves.jsonl')==cert['journal_sha256'];assert sha(RUN/'metadata.json')==cert['metadata_sha256']
 rows=[json.loads(line) for line in (RUN/'leaves.jsonl').read_text().splitlines()]
 rows=sorted(sorted(rows,key=score,reverse=True)[:args.count],key=lambda row:F(row['left']))
 assert len({(row['left'],row['right']) for row in rows})==len(rows)
 assert all(F(x['right'])<=F(y['left']) for x,y in zip(rows,rows[1:]))
 G.M.SOURCE=SOURCE;d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1
 mo=ANG.moments(1044);mn=moments(F(9,10),F(3,2),1044);ma=moments(F(1,2),F(3,2),1044)
 assert ma[0]==1 and ma[1]==F(-1,2) and all(m==0 for m in ma[2:])
 oldmass=ANG.beta_mass();newmass=mass(F(9,10),F(3,2));fourmass=arb.pi()
 result=[];total=arb(0)
 for row in rows:
  l,r=F(row['left']),F(row['right']);t=(l+r)/2
  rh,drh,pp,qq,ppt=P.point(d,cache,t)
  coeff=P.cofactor(P.residual_sines(rh,drh,pp,qq,ell));gamma=ANG.axis(coeff);q=ANG.quotient(coeff)
  alpha=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(rh)),arb(0));alphat=-sum(((-1)**j*(2*j+1)**2*v/2 for j,v in enumerate(drh)),arb(0))
  rate=ell-sum(((-1)**n*v for n,v in enumerate(pp,1)),arb(0));ratet=-sum(((-1)**n*v for n,v in enumerate(ppt,1)),arb(0))
  assert (gamma-(rate*alphat+(D-rate-2*ratet)*alpha)).contains(0)
  oldsq=gamma**2+oldmass*ANG.normalized_square(q,mo)
  newsq=gamma**2+newmass*ANG.normalized_square(q,mn)
  foursq=gamma**2+fourmass*ANG.normalized_square(q,ma)
  # Independent tridiagonal exact angular formula for a=4.
  tri=q[0]**2+sum((x*x/2 for x in q[1:]),arb(0))-q[0]*q[1]-sum((q[j]*q[j+1]/2 for j in range(1,len(q)-1)),arb(0))
  assert (foursq-(gamma**2+fourmass*tri)).contains(0)
  assert newsq.lower()>0 and foursq.lower()>0 and oldsq.lower()>0
  oldn=oldsq.sqrt();newn=newsq.sqrt();fourn=foursq.sqrt()
  assert oldn.overlaps(arb(row['center_norm']['ball']))
  assert newsq.upper()<foursq.lower()<oldsq.lower()
  variation=F(row['variation_bound']['upper_exact'])
  lower=max(F(0),exact(newn.lower())-variation)
  b=F(-1,2) if r<=0 else F(123,20);weight=aa(b*l).exp()*aa(b*(r-l)).expm1()/aa(b)
  energy=aa(lower*lower)*weight;total+=energy
  item={'left':str(l),'right':str(r),'center':str(t),'leaf_id':row['leaf_id'],'new_center_norm':G.rec(newn),'a4_center_norm':G.rec(fourn),'old_center_norm':G.rec(oldn),'old_variation_upper_exact':str(variation),'interval_uniform_norm_lower_exact':str(lower),'new_energy_lower':G.rec(energy),'axis_formula':'PASS','a4_tridiagonal_formula':'PASS','old_center_replay':'PASS'}
  result.append(item)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'leaf_id':row['leaf_id'],'energy':energy.str(16),'total_norm':total.sqrt().str(16),'elapsed_seconds':time.monotonic()-start}),flush=True)
 lower=exact(total.lower());strict=F(math.isqrt((lower*1000000).numerator//(lower*1000000).denominator),1000)
 assert strict**2<lower
 out={'status':'COMPUTED_PENDING_AUDIT','date':datetime.now(timezone.utc).isoformat(),'bits':args.bits,'count':len(result),'uniform_a_interval':['18/5','4'],'lower_test_endpoint':'18/5','energy_lower':G.rec(total),'strict_norm_lower_exact':str(strict),'strict_norm_lower_decimal':f'{float(strict):.3f}','source_sha256':sha(SOURCE),'journal_sha256':sha(RUN/'leaves.jsonl'),'metadata_sha256':sha(RUN/'metadata.json'),'parent_certificate_sha256':sha(CERT),'script_sha256':sha(Path(__file__)),'point_code_sha256':sha(Path(P.__file__)),'global_code_sha256':sha(Path(G.__file__)),'angular_code_sha256':sha(Path(ANG.__file__)),'green_cache_sha256':sha(G.CACHE),'rows':result,'elapsed_seconds':time.monotonic()-start}
 (TOP/'evidence'/f'{args.tag}_{args.bits}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':out['status'],'lower':out['strict_norm_lower_decimal'],'count':len(result),'elapsed_seconds':out['elapsed_seconds']}),flush=True)
if __name__=='__main__':main()
