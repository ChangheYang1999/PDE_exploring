"""Whole-plane rational Bernstein certificate with exact input binding."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,argparse,gzip,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/scaled_rational_background_cover';SOURCE=R/'research/scaled_background_cover'
sys.path.insert(0,str(R/'research/radial_fourier/code'))
from radial import ar
sys.path.insert(0,str(R/'research/global_matrices/code'))
from cover import endpoints,checktree,extrema,maxabs,eigen
spec=importlib.util.spec_from_file_location('n4_poly_cover',R/'research/candidate_background_cover/code/certify.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
sys.set_int_max_str_digits(0);sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def save(p,d):
 with Path(p).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def inputs():
 prep=json.loads((B/'verification/PREPARE.json').read_text());assert sha(B/'PROOF.md')==prep['proof_sha256']
 ps=[B/'PROOF.md',B/'verification/PREPARE.json',Path(__file__),R/'research/global_matrices/code/cover.py',R/'research/candidate_background_cover/code/certify.py',R/'research/radial_fourier/code/radial.py']
 return {str(p.relative_to(R)):sha(p) for p in ps}
def denbern(D,n,a,b):
 assert n>=D.degree()
 ds=(helper.transform(n,str(a),str(b))*arb_mat([[ar(D[i])] for i in range(n+1)])).entries()
 assert all(d>0 for d in ds),('denominator coefficients not proved positive',n,a,b)
 return ds
def normalize(M,ds):
 assert M.nrows()==len(ds)
 return arb_mat([[M[i,k]/ds[i] for k in range(M.ncols())] for i in range(M.nrows())])
def ranges(P,D,nt,nz,a,b,c,d,delta,J,tau):
 radial=helper.transform(nt,str(a),str(b));angular=helper.transform(nz,str(c),str(d)).transpose();BB={key:radial*M*angular for key,M in P.items()};ds=denbern(D,nt,a,b);NB={key:normalize(M,ds) for key,M in BB.items()}
 wl=(1-ar(b))**ar(delta/2);wh=(1-ar(a))**ar(delta/2)
 W=arb_mat([[sum((ar(Q(comb(n,k)*comb(i,k),comb(J,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(i,n)+1)),arb(0)) for n in range(J+1)] for i in range(J+1)])
 plain={'b':(ar(tau),ar(tau))}
 for lab in ['a','q']:plain[lab]=extrema((W*arb_mat([NB[lab,j].entries() for j in range(J+1)])).entries())
 improved=None;denlower=min(d.lower() for d in ds)
 if b<1:
  multipliers,error=helper.multipliers(nt,a,b,delta,J);large=denbern(D,nt+6,a,b);denlower=min(denlower,min(d.lower() for d in large));improved={'b':(ar(tau),ar(tau))}
  for lab in ['a','q']:
   total=arb_mat(nt+7,nz+1);err=arb(0)
   for j in range(J+1):total+=multipliers[j]*BB[lab,j];err+=error[j]*maxabs(NB[lab,j].entries())
   lo,hi=extrema(normalize(total,large).entries());improved[lab]=((lo-err).lower(),(hi+err).upper())
 return plain,improved,denlower

def fixtures(bits):
 ctx.prec=bits;start=time.monotonic();binds=inputs();v=Poly([1,-1]);D=(1+624*v)**2*(1+2499*v)**3;t=Poly([0,1]);records=[]
 for a,b in [(Q(0),Q(1)),(Q(1,4),Q(1,2)),(1-Q(1,2**20),Q(1)),(1-Q(1,2**20),1-Q(1,2**21))]:
  c,d=Q(-3,4),Q(1,4)
  for kind in ['one','negative_constant','radial_linear','angular_linear','fractional_power']:
   factor=Q(-7,3) if kind=='negative_constant' else Q(1);num=D*t if kind=='radial_linear' else D*factor;nt=num.degree()+3;nz=1 if kind=='angular_linear' else 0;J=1 if kind=='fractional_power' else 0;P={(lab,j):arb_mat(nt+1,nz+1) for lab in ['a','q'] for j in range(J+1)}
   for i,q in enumerate(num):P['a',J][i,int(kind=='angular_linear')]=ar(q)
   plain,improved,den=ranges(P,D,nt,nz,a,b,c,d,Q(2,3),J,Q(0));assert den>0;accuracy=[]
   for frac in [Q(0),Q(1,3),Q(1,2),Q(1)]:
    tv=a+(b-a)*frac;zv=c+(d-c)*frac;value=ar(tv) if kind=='radial_linear' else ar(zv) if kind=='angular_linear' else (1-ar(tv))**ar(Q(1,3)) if kind=='fractional_power' else ar(factor)
    for enclosure in [plain,improved]:
     if enclosure is None:continue
     lo,hi=enclosure['a'];assert value.upper()>=lo and value.lower()<=hi,(kind,tv,value,lo,hi)
     if kind in ['one','negative_constant']:assert hi-lo<arb(2)**-300
    accuracy.append({'t':str(tv),'z':str(zv),'value':value.str(50)})
   records.append({'kind':kind,'a':str(a),'b':str(b),'denominator_coefficients_positive':True,'plain_a':[x.str(60) for x in plain['a']],'correlated_a':None if improved is None else [x.str(60) for x in improved['a']],'points':accuracy})
 out={'utc':now(),'precision_bits':bits,'inputs':binds,'fixture_count':len(records),'point_checks':sum(len(r['points']) for r in records),'records':records,'elapsed_seconds':time.monotonic()-start,'status':'PASS manufactured rational Bernstein arithmetic fixtures'};save(B/'verification/fixtures.json',out);print('FIXTURES_PASS',len(records),out['elapsed_seconds'],flush=True)

def run(name,bits,seconds,tau):
 ctx.prec=bits;start=time.monotonic();binds=inputs();f=B/'verification/fixtures.json';fix=json.loads(f.read_text());assert fix['fixture_count']==20 and fix['inputs']==binds;binds[str(f.relative_to(R))]=sha(f)
 summaryp=SOURCE/f'verification/{name}_reconstruction.json';summary=json.loads(summaryp.read_text());src=R/summary['storage_path'];assert sha(src)==summary['polynomial_sha256']
 for p,h in summary['inputs'].items():assert sha(R/p)==h,p
 with gzip.open(src,'rt') as f:data=json.load(f)
 assert data['raw_sha256']==summary['raw_sha256'] and data['inputs']==summary['inputs'];D=Poly([Q(q) for q in data['denominator']]);fields={(key.split('_')[0],int(key.split('_')[1])):{(i,k):Q(q) for i,k,q in rows} for key,rows in data['polynomials'].items()};J=data['J'];delta=Q(data['delta']);nt=max(D.degree(),max(i for A in fields.values() for i,k in A));nz=max(k for A in fields.values() for i,k in A)
 assert tau>0 and D(1)==1 and data['denominator_positive_on_unit_interval'];P={(lab,j):arb_mat(nt+1,nz+1) for lab in ['a','q'] for j in range(J+1)}
 for i,q in enumerate(D):P['a',0][i,0]=ar(tau*q)
 for (lab,j),A in fields.items():
  out='a' if lab=='ry' else 'q';factor=Q(1) if lab=='ry' else Q(-1,2)
  for (i,k),q in A.items():P[out,j][i,k]=ar(factor*q)
 target=B/f'verification/{name}_theta_{str(tau).replace("/","_")}_{bits}.json';seed=R/'research/candidate_background_cover/verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json'
 for p in [summaryp,src,seed]:binds[str(p.relative_to(R))]=sha(p)
 if target.exists():
  old=json.loads(target.read_text());assert old['inputs']==binds and old['tau']==str(tau);accepted=old['accepted'];queue=old['pending'];inconclusive=old['inconclusive'];elapsed=old['total_elapsed_seconds'];assert all(arb(r['bound'])>=0 for r in accepted)
 else:
  old=json.loads(seed.read_text());assert old['all_pass'];accepted=[];queue=[r['path'] for r in old['accepted']];inconclusive=[];elapsed=0
 checktree(set(queue+[r['path'] for r in accepted]));print('RATIONAL_READY',name,nt,nz,len(queue),'pending',len(accepted),'accepted',flush=True);count=0
 while queue and time.monotonic()-start<seconds:
  path=queue.pop(0);a,b,c,d=endpoints(path);plain,improved,den=ranges(P,D,nt,nz,a,b,c,d,delta,J,tau);bound=eigen(plain,c,d)
  if improved is not None:bound=bound.max(eigen(improved,c,d))
  if bound>=0:accepted.append({'path':path,'bound':bound.str(90),'denominator_coefficient_lower':den.str(50),'pass':True})
  else:
   inconclusive.append({'path':path,'bound':bound.str(40)})
   if len(path)>=52:queue.insert(0,path);print('DEPTH_LIMIT',path,flush=True);break
   children=('t','T') if (b-a)/(1-a)>=(d-c)/2 else ('z','Z');queue.extend(path+ch for ch in children)
  count+=1;leaves=queue+[r['path'] for r in accepted];assert len(leaves)==len(set(leaves));checktree(set(leaves))
  state={'utc':now(),'candidate':name,'raw_sha256':data['raw_sha256'],'tau':str(tau),'precision_bits':bits,'inputs':binds,'reconstruction_inputs':summary['inputs'],'degree_t':nt,'degree_z':nz,'J':J,'accepted':accepted,'pending':queue,'inconclusive':inconclusive,'complete_partition':True,'all_pass':not queue,'stage_elapsed_seconds':time.monotonic()-start,'total_elapsed_seconds':elapsed+time.monotonic()-start,'all_denominator_coefficients_positive':True,'no_spatial_quadrature':True,'status':'OPEN independent rational cover and reconstruction review' if not queue else 'OPEN incomplete rational whole-plane cover'}
  tmp=target.with_suffix('.pending');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(target);print('CELL',count,path,'pass',bool(bound>=0),'bound',bound.str(12),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
 print('STAGE_DONE',name,'accepted',len(accepted),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('stage',choices=['fixtures','cover']);p.add_argument('candidate',nargs='?',default='C1-N1-017-legqs50-quot013');p.add_argument('--bits',type=int,default=1536);p.add_argument('--seconds',type=int,default=420);p.add_argument('--tau',default='2/25');a=p.parse_args()
 if a.stage=='fixtures':fixtures(a.bits)
 else:run(a.candidate,a.bits,a.seconds,Q(a.tau))
