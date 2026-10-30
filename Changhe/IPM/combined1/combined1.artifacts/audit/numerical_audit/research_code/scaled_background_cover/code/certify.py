"""Exact denominator clearing and complete Bernstein cover; candidate-specific."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,argparse,gzip,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled_background_cover'
sys.path.insert(0,str(ROOT/'research/joint_scaled_factored_weak/code'))
from fields_joint import ScaledRadial,LINEARS,ZERO_POWERS,ar
sys.path.insert(0,str(ROOT/'research/generator_sector_audit/code'))
from direct import origin
sys.path.insert(0,str(ROOT/'research/global_matrices/code'))
from cover import endpoints,checktree,extrema,maxabs,eigen
spec=importlib.util.spec_from_file_location('n4_original_cover',ROOT/'research/candidate_background_cover/code/certify.py');oldcover=importlib.util.module_from_spec(spec);spec.loader.exec_module(oldcover)
spec=importlib.util.spec_from_file_location('n4_scaled_cover_jet',ROOT/'research/multiscale_generators/code/cartesian.py');jetmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(jetmod)
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def save(p,d):
 with Path(p).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def bind_record(d):
 for p,h in d.get('inputs',{}).items():assert sha(ROOT/p)==h,p

def common():
 prep=json.loads((BASE/'verification/PREPARE.json').read_text());assert sha(BASE/'PROOF.md')==prep['proof_sha256']
 ps=[BASE/'PROOF.md',BASE/'verification/PREPARE.json',Path(__file__),ROOT/'research/joint_scaled_factored_weak/PROOF.md',ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/multiscale_generators/code/moments.py',ROOT/'research/generator_sector_audit/code/direct.py',ROOT/'research/global_matrices/code/cover.py',ROOT/'research/candidate_background_cover/code/certify.py',ROOT/'research/candidate_background_cover/PROOF.md',ROOT/'research/radial_fourier/code/radial.py',ROOT/'research/gradient_commutator/PROOF.md']
 return {str(p.relative_to(ROOT)):sha(p) for p in ps}
def build(name,bits):
 ctx.prec=bits;start=time.monotonic();inputs=common();D=ROOT/'research/candidate_audits/data'/name;mp=D/'MANIFEST.json';manifest=json.loads(mp.read_text());e=manifest['coefficient_files'][0];raw=D/e['name'];assert sha(raw)==e['sha256'] and manifest['id']==name
 for p in [mp,raw]:inputs[str(p.relative_to(ROOT))]=sha(p)
 ap=ROOT/f'research/generator_sector_audit/verification/{name}_direct.json'
 if not ap.exists():ap=ROOT/f'research/candidate_audits/verification/{name}.json'
 audit=json.loads(ap.read_text());assert audit['generator_sha256']==sha(raw) and audit['B0n_exact'] and audit['leading_density_equal_state131'];inputs[str(ap.relative_to(ROOT))]=sha(ap)
 model=ScaledRadial(raw);powers=tuple(max(A.powers[i] for field in [model.rx,model.ry] for A in field.values()) for i in range(len(LINEARS)))
 denominator=Poly([1])
 for L,k in zip(LINEARS,powers):denominator*=L**k
 assert denominator(0)>0 and denominator(1)==1 and all(L(0)>=1 and L(1)==1 for L in LINEARS)
 z=Poly([0,1]);T=[Poly([1]),z];U=[Poly([1]),2*z];nmax=max(n//2 for f in [model.rx,model.ry] for j,n in f)
 for k in range(2,nmax+1):T.append(2*z*T[-1]-T[-2]);U.append(2*z*U[-1]-U[-2])
 poly={};cleared=0;cache={}
 for label,field in [('rx',model.rx),('ry',model.ry)]:
  for (j,n),A in field.items():
   assert n%2==0 and (label=='ry' or n>0)
   if A.powers not in cache:
    C=Poly([1])
    for L,k,used in zip(LINEARS,powers,A.powers):assert k>=used;C*=L**(k-used)
    cache[A.powers]=C
   reduced=A.divide_t(2);P=reduced.P*cache[A.powers]
   # Exact multiplication identity before angular expansion.
   test=P
   for L,k in zip(LINEARS,A.powers):test*=L**k
   assert test==reduced.P*denominator
   angular=T[n//2] if label=='ry' else U[n//2-1];out=poly.setdefault((label,j+1),{})
   for i,a in enumerate(P):
    if a:
     for k,b in enumerate(angular):
      if b:out[i,k]=out.get((i,k),Q(0))+a*b
   cleared+=1
  print('CLEARED',name,label,cleared,'seconds',time.monotonic()-start,flush=True)
 poly={key:{ij:q for ij,q in A.items() if q} for key,A in poly.items()};rawdata=json.loads(raw.read_text());quartic=origin(rawdata)
 origins={}
 for label in ['rx','ry']:
  vals={}
  for (lab,j),A in poly.items():
   if lab==label:
    for (i,k),q in A.items():
     if i==0:vals[k]=vals.get(k,Q(0))+q
  origins[label]={k:q for k,q in vals.items() if q}
 assert not origins['rx'] and origins['ry']=={0:Q(quartic['a0'])*denominator(0)}
 points=[]
 for xs,ys in [('1/10','73/100'),('3','4'),('60','80')]:
  x,y=Q(xs),Q(ys);r2=x*x+y*y;t=r2/(1+r2);v=1-t;z0=(x*x-y*y)/r2;sin2=2*x*y/r2;wp=ar(v)**ar(model.delta/2);values={};direct=jetmod.GeneratorJet(raw,xs,ys,4);expected={'rx':-direct.chi(3,1)-direct.chi(1,3),'ry':-direct.chi(2,2)-direct.chi(0,4)}
  for label in ['rx','ry']:
   value=sum((wp**j*sum((ar(q*t**i*z0**k) for (i,k),q in A.items()),arb(0)) for (lab,j),A in poly.items() if lab==label),arb(0))/ar(denominator(t))
   if label=='rx':value*=ar(sin2)
   assert value.overlaps(expected[label]) and value.rel_accuracy_bits()>150,(name,label,value)
   values[label]={'value':value.str(100),'raw_jet_overlap':True,'bits':value.rel_accuracy_bits()}
  points.append({'x':xs,'y':ys,'fields':values})
 calibration={}
 if name=='C1-N1-007-d2w-j7-e2bal':
  assert powers==ZERO_POWERS and denominator==Poly([1]);p=ROOT/f'research/candidate_background_cover/data/{name}_polynomials.json.gz'
  with gzip.open(p,'rt') as f:prior=json.load(f)
  old={tuple([key.split('_')[0],int(key.split('_')[1])]):{(i,k):Q(q) for i,k,q in rows} for key,rows in prior['polynomials'].items()}
  assert poly==old;inputs[str(p.relative_to(ROOT))]=sha(p);calibration={'all_exact007_coefficients_equal':True,'coefficient_count':sum(len(A) for A in poly.values())}
 else:
  p=BASE/'verification/C1-N1-007-d2w-j7-e2bal_reconstruction.json';cal=json.loads(p.read_text());assert cal['calibration']['all_exact007_coefficients_equal'];bind_record(cal);inputs[str(p.relative_to(ROOT))]=sha(p)
 result={'utc':now(),'candidate':name,'raw_sha256':sha(raw),'c_exact':str(model.c),'delta':str(model.delta),'J':max(j for lab,j in poly),'denominator_powers':list(powers),'denominator':[str(q) for q in denominator],'denominator_positive_on_unit_interval':True,'exact_clearing_checks':cleared,'origin_checks':True,'point_checks':points,'calibration':calibration,'polynomials':{f'{lab}_{j}':[[i,k,str(q)] for (i,k),q in sorted(A.items())] for (lab,j),A in poly.items()},'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'foreign_code_executed':False,'status':'OPEN new scaled reconstruction independent review' if not calibration else 'PASS own exact007 reconstruction calibration'}
 path=BASE/f'data/{name}_polynomials.json.gz'
 with path.open('xb') as f:
  with gzip.GzipFile(fileobj=f,mode='wb',compresslevel=2,mtime=0) as stream:stream.write(json.dumps(result,separators=(',',':')).encode())
 summary={k:v for k,v in result.items() if k not in ['polynomials','denominator']};summary.update({'polynomial_sha256':sha(path),'polynomial_bytes':path.stat().st_size,'nonzero_coefficients':sum(len(A) for A in poly.values()),'degree_t':max(i for A in poly.values() for i,k in A),'degree_z':max(k for A in poly.values() for i,k in A),'storage_path':str(path.relative_to(ROOT))})
 save(BASE/f'verification/{name}_reconstruction.json',summary);print('BUILD_DONE',name,'seconds',summary['elapsed_seconds'],'bytes',path.stat().st_size,'degrees',summary['degree_t'],summary['degree_z'],flush=True)

def ranges(P,nt,nz,a,b,c,d,delta,J):
 radial=oldcover.transform(nt,str(a),str(b));angular=oldcover.transform(nz,str(c),str(d)).transpose();B={key:radial*M*angular for key,M in P.items()}
 wl=(1-ar(b))**ar(delta/2);wh=(1-ar(a))**ar(delta/2)
 W=arb_mat([[sum((ar(Q(comb(n,k)*comb(i,k),comb(J,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(i,n)+1)),arb(0)) for n in range(J+1)] for i in range(J+1)])
 plain={lab:extrema((W*arb_mat([B[lab,j].entries() for j in range(J+1)])).entries()) for lab in ['a','b','q']};improved=None
 if b<1:
  multipliers,error=oldcover.multipliers(nt,a,b,delta,J);improved={}
  for lab in ['a','b','q']:
   total=arb_mat(nt+7,nz+1);err=arb(0)
   for j in range(J+1):total+=multipliers[j]*B[lab,j];err+=error[j]*maxabs(B[lab,j].entries())
   lo,hi=extrema(total.entries());improved[lab]=((lo-err).lower(),(hi+err).upper())
 return plain,improved

def cover(name,bits,seconds,tau):
 ctx.prec=bits;start=time.monotonic();common_inputs=common();src=BASE/f'data/{name}_polynomials.json.gz';summaryp=BASE/f'verification/{name}_reconstruction.json';summary=json.loads(summaryp.read_text());assert sha(src)==summary['polynomial_sha256'];bind_record(summary)
 with gzip.open(src,'rt') as f:data=json.load(f)
 assert data['raw_sha256']==summary['raw_sha256'];fields={(key.split('_')[0],int(key.split('_')[1])):{(i,k):Q(q) for i,k,q in rows} for key,rows in data['polynomials'].items()};D=Poly([Q(q) for q in data['denominator']]);J=data['J'];delta=Q(data['delta']);assert tau>0 and D(1)==1
 nt=max(D.degree(),max(i for A in fields.values() for i,k in A));nz=max(k for A in fields.values() for i,k in A);P={(lab,j):arb_mat(nt+1,nz+1) for lab in ['a','b','q'] for j in range(J+1)}
 for lab in ['a','b']:
  for i,q in enumerate(D):P[lab,0][i,0]=ar(tau*q)
 for (lab,j),A in fields.items():
  output='a' if lab=='ry' else 'q';factor=Q(1) if lab=='ry' else Q(-1,2)
  for (i,k),q in A.items():P[output,j][i,k]=ar(factor*q)
 target=BASE/f'verification/{name}_theta_{str(tau).replace("/","_")}_{bits}.json';seed=ROOT/'research/candidate_background_cover/verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json'
 inputs={**common_inputs,str(summaryp.relative_to(ROOT)):sha(summaryp),str(src.relative_to(ROOT)):sha(src),str(seed.relative_to(ROOT)):sha(seed)}
 if target.exists():
  old=json.loads(target.read_text());assert old['inputs']==inputs and old['tau']==str(tau);accepted=old['accepted'];queue=old['pending'];inconclusive=old['inconclusive'];elapsed=old['total_elapsed_seconds'];assert all(arb(row['bound'])>=0 for row in accepted)
 else:
  initial=json.loads(seed.read_text());assert initial['all_pass'];queue=[row['path'] for row in initial['accepted']];accepted=[];inconclusive=[];elapsed=0
 checktree(set(queue+[row['path'] for row in accepted]));print('COVER_READY',name,nt,nz,'pending',len(queue),'accepted',len(accepted),flush=True);count=0
 while queue and time.monotonic()-start<seconds:
  path=queue.pop(0);a,b,c,d=endpoints(path);plain,improved=ranges(P,nt,nz,a,b,c,d,delta,J);bound=eigen(plain,c,d)
  if improved is not None:bound=bound.max(eigen(improved,c,d))
  if bound>=0:accepted.append({'path':path,'bound':bound.str(90),'pass':True})
  else:
   inconclusive.append({'path':path,'bound':bound.str(40)})
   if len(path)>=52:queue.insert(0,path);print('DEPTH_LIMIT',path,flush=True);break
   children=('t','T') if (b-a)/(1-a)>=(d-c)/2 else ('z','Z');queue.extend(path+child for child in children)
  count+=1;leaves=queue+[row['path'] for row in accepted];assert len(leaves)==len(set(leaves));checktree(set(leaves))
  state={'utc':now(),'candidate':name,'raw_sha256':data['raw_sha256'],'tau':str(tau),'precision_bits':bits,'inputs':inputs,'source_reconstruction_inputs':data['inputs'],'denominator_powers':data['denominator_powers'],'degree_t':nt,'degree_z':nz,'J':J,'accepted':accepted,'pending':queue,'inconclusive':inconclusive,'complete_partition':True,'all_pass':not queue,'stage_elapsed_seconds':time.monotonic()-start,'total_elapsed_seconds':elapsed+time.monotonic()-start,'no_spatial_quadrature':True,'no_global_margin_claim':True,'status':'OPEN independent scaled cover review' if not queue else 'OPEN incomplete whole-plane cover'}
  tmp=target.with_suffix('.pending');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(target)
  print('CELL',count,path,'pass',bool(bound>=0),'bound',bound.str(12),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
 print('STAGE_DONE',name,'accepted',len(accepted),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('stage',choices=['build','cover']);p.add_argument('candidate');p.add_argument('--bits',type=int,default=1536);p.add_argument('--seconds',type=int,default=420);p.add_argument('--tau',default='2/25');a=p.parse_args()
 if a.stage=='build':build(a.candidate,a.bits)
 else:cover(a.candidate,a.bits,a.seconds,Q(a.tau))
