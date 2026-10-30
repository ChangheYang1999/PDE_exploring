"""Complete finite origin jet from harmonic Laplacians and Cartesian derivatives."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,math,sys,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0);checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
need('proof first',not read('data/PROOF_FIRST.json')['checker_exists']);p=read('data/parameters.json');raw=B/'../rounding_audit/data/exact_generators.json';need('raw exact hash',sha(raw)==p['raw_sha256']);data=json.loads(raw.read_text());c=Q(data['cl_exact']);need('exact c',c==Q(p['c']));gamma=1/c;delta=1-gamma
peer=read('source/N4_result.json');need('peer own finite checks',peer['check_count']==len(peer['checks'])==3005 and all(peer['checks'].values()));need('peer exact identity',peer['candidate']==p['candidate'] and Q(peer['c_exact'])==c and peer['generator_count']==len(data['generators'])==2982)
for name in ['N4_check.py','N1_check.py']:ast.parse((B/'source'/name).read_text())
def add_into(out,key,v):
 out[key]=out.get(key,Q(0))+v
 if not out[key]:del out[key]
def add(a,b,scale=Q(1)):
 out=dict(a)
 for k,v in b.items():add_into(out,k,v*scale)
 return out
def diff(a,dx,dy):
 out={}
 for (i,j),v in a.items():
  if i>=dx and j>=dy:
   factor=math.prod(range(i-dx+1,i+1))*math.prod(range(j-dy+1,j+1));add_into(out,(i-dx,j-dy),v*factor)
 return out
def harmonic_radial(m,s):
 out={}
 for k in range(m+1):
  h=(-1)**k*math.comb(2*m,2*k)
  for q in range(s+1):add_into(out,(2*m-2*k+2*q,2*k+2*(s-q)),Q(h*math.comb(s,q)))
 return out
def product(a,b,degree):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():
   if i+j+k+l<=degree:add_into(out,(i+k,j+l),v*w)
 return out
chi={};lap={};used=[];summands=0;radial=[]
for index,g in enumerate(data['generators']):
 m,j,spec=g['m'],g['j'],g['spec'];w=spec[1]
 need('generator schema '+str(index),isinstance(m,int) and m>=0 and isinstance(j,int) and j>=0 and isinstance(w,int) and w>=0 and spec[0] in ['mono','leg'])
 if m+w>4:continue
 used.append(index);a=Q(g['coef']);p_j=(3+gamma-j*delta)/2
 if spec[0]=='mono':terms=[(w,1)]
 else:
  n=spec[2];need('Legendre degree '+str(index),isinstance(n,int) and n>=0);terms=[(w+h,(-1)**(n-h)*math.comb(n,h)*math.comb(n+h,h)) for h in range(min(n,4-m-w)+1)]
 for power,leg in terms:
  bn=Q(1)
  for ell in range(5-m-power):
   if ell:bn*=Q(p_j-m-power-ell+1,ell)
   s=power+ell;v=a*leg*bn;pol=harmonic_radial(m,s);chi=add(chi,pol,v)
   direct=add(diff(pol,2,0),diff(pol,0,2));spectral={} if s==0 else {k:4*s*(2*m+s)*x for k,x in harmonic_radial(m,s-1).items()}
   need('harmonic Laplacian '+str(summands),direct==spectral)
   lap=add(lap,spectral,v);radial.append({'source_generator':index,'m':m,'s':s,'coefficient_exact':str(v)});summands+=1
need('complete relevant generators',used==peer['used_generator_indices'] and len(used)==60)
need('complete finite radial summands',summands==peer['finite_summand_count']==140)
need('complete Laplacian agreement',lap==add(diff(chi,2,0),diff(chi,0,2)))
rho={k:-v for k,v in diff(lap,0,1).items()};ux={k:-v for k,v in diff(chi,1,2).items()};uy=diff(chi,2,1)
need('potential parity and cutoff',all(i%2==j%2==0 and i+j<=8 for i,j in chi))
need('density and vertical velocity parity',all(i%2==0 and j%2==1 and i+j<=5 for i,j in rho) and all(i%2==0 and j%2==1 and i+j<=5 for i,j in uy))
need('horizontal velocity parity',all(i%2==1 and j%2==0 and i+j<=5 for i,j in ux))
F={(i,j):(c*(i+j)-1)*v for (i,j),v in rho.items()};F=add(F,product(ux,diff(rho,1,0),5));F=add(F,product(uy,diff(rho,0,1),5));F={k:v for k,v in F.items() if v}
need('residual parity',all(i%2==0 and j%2==1 and i+j<=5 for i,j in F))
need('exact constant quotient',F.get((0,1),Q(0))==0)
for i in range(5):need('N4 potential axis '+str(i),chi.get((0,2*i),Q(0))==Q(peer['chi_axis_A_exact'][str(i)]))
for i in range(4):need('N4 potential x2 '+str(i),chi.get((2,2*i),Q(0))==Q(peer['chi_x2_B_exact'][str(i)]))
for j in [1,3,5]:
 for name,pol,key in [('density',rho,'rho_axis_exact'),('vertical velocity',uy,'uy_axis_exact'),('residual',F,'F_axis_exact')]:need('N4 '+name+' axis '+str(j),pol.get((0,j),Q(0))==Q(peer[key][str(j)]))
coeff={};bounds={}
for key,(lo,hi) in p['directed_intervals'].items():
 i,j=map(int,key.split(','));v=F.get((i,j+1),Q(0));need('strict interval '+key,Q(lo)<v<Q(hi));need('tolerance failure '+key,abs(v)>Q(p['tolerance']));coeff[key]=str(v);bounds[key]=[lo,hi]
need('largest is positive y4',Q(coeff['0,4'])==max(abs(Q(v)) for v in coeff.values()))
report=(B/'source/NUMERICS_FINAL_1702.md').read_text().splitlines();need('frozen report hash',sha(B/'source/NUMERICS_FINAL_1702.md')=='3c10441009b5d7932df153d145673148264de2f20c32e2ec601c6ed28077eedf');need('universal claim lines53to54','five Taylor equations' in ' '.join(report[52:54]) and '2e-13 for every candidate' in ' '.join(report[52:54]))
need('exact center normalization',c+uy.get((0,1),Q(0))==1 and rho.get((0,1),Q(0))>0)
def serialize(pol):return {f'{i},{j}':str(v) for (i,j),v in sorted(pol.items())}
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'manifest_sha256':sha(B/'data/manifest.json'),'candidate':p['candidate'],'raw_sha256':p['raw_sha256'],'generator_count':len(data['generators']),'used_generator_indices':used,'finite_summand_count':summands,'potential_radial_terms':radial,'potential_jet_exact':serialize(chi),'Laplacian_jet_exact':serialize(lap),'density_jet_exact':serialize(rho),'horizontal_velocity_jet_exact':serialize(ux),'vertical_velocity_jet_exact':serialize(uy),'residual_jet_exact':serialize(F),'quotient_constant_exact':'0','quotient_nonconstant_coefficients_exact':coeff,'directed_intervals':bounds,'tolerance':p['tolerance'],'all_five_exceed_tolerance':True,'N4_axis_coefficients_equal':True,'exact_center_relation':True,'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED exact candidate007 Taylor coefficients and N4-419; REFUTED uniform saved-candidate2e-13 tolerance for every one of the five equations in this candidate. Exact center and existing framework verdicts unchanged.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),'checks',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
