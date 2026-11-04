"""Complete exact-source centered-series and interval-Horner ordinary-slab host audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from flint import arb,arb_mat,arb_poly,fmpq,ctx
import argparse,gc,gzip,json,os,resource,sys,time
B=Path(__file__).resolve().parents[1];R=Path.cwd().resolve();CAM=R.parent
P=argparse.ArgumentParser();P.add_argument('--roots',required=True);P.add_argument('--output',required=True)
opt=P.parse_args();JS=list(map(int,opt.roots.split(',')));out=Path(opt.output)
assert JS == list(range(97,55,-1)) and R.name=="numerics_agent_2"
assert not out.is_absolute() and '..' not in out.parts
V=R/out;V.mkdir(parents=True,exist_ok=True)
assert not (V/'check_v01.json').exists()
assert os.sched_getaffinity(0)=={49} and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(n)=='1' for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
sys.set_int_max_str_digits(0)
FIELDS=('a','b','e','rh','sh','ud','uh');PB=2560;PC=384;MAXN=480;NU=32;NA=256
SOURCE=CAM/'numerics_agent_1/research/source013_background_source/worker_background_v02/research/source013_background_source/verification/source_v01/polynomials.json.gz'
COVER=CAM/'numerical_audit/research/source013_background_cover/verification/manifest_v01.json'
checks=0;tick=time.monotonic()
def stamp():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
start=stamp()
def ck(x,why):
 global checks
 checks+=1
 assert x,why

def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def ball(q):return arb(fmpq(str(q)))
def pair(x):
 ck(x.is_finite(),'finite interval')
 return [str(x.lower().fmpq()),str(x.upper().fmpq())]
def radius(x):
 ck(x.is_finite() and x>=0,'nonnegative finite radius')
 return arb(0,1)*x.upper()
def put(name,obj):
 p=V/name
 if name.endswith('.gz'):
  with p.open('xb') as f:
   with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:g.write((json.dumps(obj,separators=(',',':'))+'\n').encode())
 else:
  with p.open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
 return digest(p)
def binomial_series(x,e,n):
 result=[arb(1)];be=ball(e)
 for j in range(1,n+1):result.append(result[-1]*(be-j+1)*x/j)
 return arb_poly(result)

ck(digest(SOURCE)=='2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d','exact source digest')
cover=json.loads(COVER.read_text())
ck(cover['reference_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21','Candidate007')
ck(cover['source']['fixed_c_exact']=='4076476460239181/2251799813685248','fixed c')
files={str(p.relative_to(CAM)):digest(p) for p in [SOURCE,COVER,B/'PROOF.md',Path(__file__)]}
with gzip.open(SOURCE,'rt') as f:source=json.load(f)
for key,value in [('source_id',cover['source']['id']),('raw_phi_sha256',cover['source']['raw_sha256']),('fields_sha256',cover['source']['fields_sha256']),('reference_sha256',cover['reference_sha256']),('parameters',cover['field_parameters'])]:ck(source[key]==value,'metadata '+key)
ck(len(source['branches'])==45,'45 exact branches')
count=sum(len(v) for b in source['branches'] for v in b['polynomials'].values());ck(count==621400,'621400 coefficients')
ctx.prec=PB;conv={};branches=[];ct=time.monotonic()
for bi,branch in enumerate(source['branches']):
 beta,scale,d=Q(branch['B']),Q(branch['scale']),branch['d']
 ck(beta>=0 and scale>0 and type(d)is int and d>=0,'branch parameters')
 data={}
 for field in FIELDS:
  entries=branch['polynomials'][field]
  if not entries:continue
  nt=max(v[0] for v in entries);nz=max(v[1] for v in entries)
  if nz not in conv:
   C=arb_mat(nz+1,nz+1);C[0,0]=1
   for power in range(1,nz+1):
    for j in range(power//2+1):
     mode=power-2*j;C[power,mode]=arb(fmpq(comb(power,j),2**(power if mode==0 else power-1)))
   conv[nz]=C
  M=arb_mat(nt+1,nz+1);seen=set()
  for i,j,c in entries:
   ck(type(i)is int and type(j)is int and 0<=i<=source['degree_t'] and 0<=j<=source['degree_z'] and (i,j)not in seen,'unique exact index')
   seen.add((i,j));M[i,j]=ball(c)
  C=M*conv[nz];ps=[]
  for j in range(nz+1):
   p=arb_poly([C[i,j] for i in range(nt+1)])
   if p.degree()>=0:ps.append((j,p))
  data[field]=(nt,ps)
 branches.append(dict(index=bi,B=beta,scale=scale,d=d,fields=data))
 if bi%10==0 or bi==44:print(stamp(),'SOURCE_BRANCHES',bi+1,time.monotonic()-ct,flush=True)
L=source['degree_z']+1;del source,conv;gc.collect();compile_seconds=time.monotonic()-ct
results=[]
for J in JS:
 kt=time.monotonic();kstart=stamp();ctx.prec=PB
 sigma=Q(255-2*J,256);rho=Q(1,255-2*J);h=ball(rho);T=arb_poly([ball(1-sigma),ball(-sigma)])
 hp=[arb(1)]
 for j in range(MAXN+1):hp.append(hp[-1]*h)
 G={f:[arb_poly([]) for _ in range(L)] for f in FIELDS};tail={f:arb(0) for f in FIELDS};branch_records=[]
 for b in branches:
  beta,scale,d=b['B'],b['scale'],b['d'];base=1+(scale-1)*sigma;g=(scale-1)*sigma/base
  ck(base>0 and abs(g)*rho<1,'positive denominator and convergent factor')
  cb=ball(sigma)**ball(beta)*ball(base)**(-d)
  eb=binomial_series(arb(-1),-beta,MAXN)*binomial_series(ball(-abs(g)),-Q(d),MAXN)
  pre=[];acc=arb(0)
  for j in range(MAXN+1):acc+=eb[j]*hp[j];pre.append(acc)
  ev=ball(1-rho)**ball(-beta)*ball(1-abs(g)*rho)**(-d)
  exact_series=binomial_series(arb(1),beta,MAXN)*binomial_series(ball(g),-Q(d),MAXN)
  for f,(nt,polys) in b['fields'].items():
   U=[(mode,p(T)) for mode,p in polys]
   norms=[sum((abs(p[i]) for mode,p in U),arb(0)).upper() for i in range(nt+1)]
   weighted=[v*hp[i] for i,v in enumerate(norms)];total=sum(weighted,arb(0))
   chosen=None;upper=None
   for n in range(120,MAXN+1,20):
    partial=sum((weighted[i]*pre[n-i] for i in range(min(nt,n)+1)),arb(0))
    candidate=(cb*(total*ev-partial)).upper()
    ck(candidate.is_finite() and candidate>=0,'nonnegative analytic tail upper')
    if candidate<=ball(Q(1,10**25)) or n==MAXN:chosen=n;upper=candidate;break
   ck(chosen is not None,'finite chosen order')
   tail[f]+=upper
   E=arb_poly([exact_series[j] for j in range(chosen+1)])
   for mode,p in U:
    v=(E*p)*cb;G[f][mode]+=arb_poly([v[j] for j in range(chosen+1)])
   branch_records.append(dict(branch=b['index'],field=f,order=chosen,tail_upper=str(upper.fmpq()),polynomial_degree=nt,polynomial_norm_at_h_upper=str(total.upper().fmpq())))
  if b['index']%10==0 or b['index']==44:print(stamp(),'ROOT',J,'SERIES_BRANCHES',b['index']+1,time.monotonic()-kt,flush=True)
 # Move complete high rows into a rigorously bounded finite tail.
 rows=[];degrees={};coeff_records={};ctx.prec=PC
 for f in FIELDS:
  n=max(p.degree() for p in G[f]);lump=arb(0)
  while n>0:
   rownorm=sum((abs(p[n]) for p in G[f]),arb(0))*ball(rho**n)
   if (lump+rownorm).upper()>ball(Q(1,10**22)):break
   lump+=rownorm;n-=1
  degrees[f]=n;tail[f]=(tail[f]+lump).upper();ck(tail[f]<ball(Q(1,10**6)),'small analytic plus finite tail')
  coeff_records[f]=[[pair(G[f][l][j]+arb(0)) for l in range(L)] for j in range(n+1)]
  rows.extend((f,j) for j in range(n+1))
 coeff_sha=put(f'coefficients_root{J}_v01.json.gz',dict(root_index=J,rho_exact=str(rho),source_sha256=files[str(SOURCE.relative_to(CAM))],compile_precision=PB,cell_precision=PC,sigma_exact=str(sigma),degrees=degrees,tail_uppers={f:str(tail[f].fmpq()) for f in FIELDS},branch_records=branch_records,coefficients=coeff_records))
 CM=arb_mat([[G[f][l][j]+arb(0) for l in range(L)] for f,j in rows])
 second=[sum((arb(l*l)*abs(G[f][l][j]) for l in range(L)),arb(0)).upper() for f,j in rows]
 index={v:j for j,v in enumerate(rows)};angles=[];pi=arb.pi()
 for ai in range(NA):
  p=pi*ball(Q(2*ai+1,2*NA));w=pi/(2*NA);wbox=radius(w)
  value=CM*arb_mat([[(l*p).cos()] for l in range(L)]);deriv=CM*arb_mat([[-l*(l*p).sin()] for l in range(L)])
  rr=[value[j,0]+deriv[j,0]*wbox+radius(w*w*second[j]/2) for j in range(len(rows))]
  angles.append((rr,(p+wbox).sin()**2))
 print(stamp(),'ROOT',J,'CELLS_READY',degrees,{f:float(tail[f].mid()) for f in FIELDS},time.monotonic()-kt,flush=True)
 cells=[];fail=[];extrema=[None]*5;worst=[None]*5
 for ui in range(NU):
  x0=-rho+2*rho*Q(ui,NU);x1=-rho+2*rho*Q(ui+1,NU)
  x=ball((x0+x1)/2)+radius(ball((x1-x0)/2))
  for ai,(angle,S) in enumerate(angles):
   values={}
   for f in FIELDS:
    v=arb(0)
    for j in range(degrees[f],-1,-1):v=v*x+angle[index[(f,j)]]
    values[f]=v+radius(tail[f])
   a,b,e=values['a'],values['b'],values['e'];det=a*b-S*e*e
   gg=values['rh']**2+S*values['sh']**2;ss=values['ud']**2+S*values['uh']**2/4
   predicates=dict(matrix=bool(a>=0 and b>=0 and det>=0),gradient=bool(gg<=ball(Q(71,500)**2)),weak_gradient=bool(gg<=ball(Q(1,4)**2)),strain=bool(ss<=ball(Q(137,125)**2)),large_strain=bool(ss<=ball(Q(3,2)**2)))
   joint=dict(primary=predicates['matrix'] and predicates['weak_gradient'] and predicates['large_strain'],small_strain=predicates['matrix'] and predicates['weak_gradient'] and predicates['strain'],small_gradient=predicates['matrix'] and predicates['gradient'] and predicates['large_strain'],both_small=predicates['matrix'] and predicates['gradient'] and predicates['strain'])
   if not all(predicates.values()):fail.append([ui,ai,predicates])
   ex=[a.lower().fmpq(),b.lower().fmpq(),det.lower().fmpq(),gg.upper().fmpq(),ss.upper().fmpq()]
   for j,v in enumerate(ex):
    if extrema[j] is None or (v<extrema[j] if j<3 else v>extrema[j]):extrema[j]=v;worst[j]=[ui,ai]
   cells.append(dict(radial_index=ui,angular_index=ai,fields={f:pair(v) for f,v in values.items()},sin_squared=pair(S),determinant=pair(det),gradient_squared=pair(gg),strain_squared=pair(ss),predicates=predicates,joint_flags=joint))
 ck(len(cells)==NU*NA,'complete Cartesian cell cover')
 summary=dict(status='COMPUTED',root_index=J,sigma_exact=str(sigma),rho_exact=str(rho),domain_r_squared=[str(Q(J,128-J)),str(Q(J+1,127-J))],joint_flags={key:all(c['joint_flags'][key] for c in cells) for key in ['primary','small_strain','small_gradient','both_small']},started_utc=kstart,finished_utc=stamp(),elapsed_seconds=time.monotonic()-kt,cell_count=len(cells),radial_cells=NU,angular_cells=NA,coefficient_sha256=coeff_sha,targets=dict(matrix_gap='3/5',gradient='71/500',weak_gradient='1/4',strain='137/125',large_strain='3/2'),extrema=dict(zip(['a_lower','b_lower','scaled_determinant_lower','gradient_squared_upper','strain_squared_upper'],map(str,extrema))),extrema_float=list(map(float,extrema)),worst_indices=worst,failed_cells=fail)
 result_sha=put(f'cells_root{J}_v01.json.gz',summary|{'cells':cells})
 results.append(summary|{'result_sha256':result_sha})
 put(f'completion_root{J}_v01.json',results[-1])
 print('ROOT_RESULT',J,summary['status'],summary['extrema_float'],summary['elapsed_seconds'],flush=True)
 del G,CM,coeff_records,cells;gc.collect()
for n,q in files.items():ck(digest(CAM/n)==q,'unchanged bound input')
record=dict(status='COMPLETED_SOURCE_RECONSTRUCTION',requested_roots=JS,started_utc=start,finished_utc=stamp(),elapsed_seconds=time.monotonic()-tick,compile_seconds=compile_seconds,compile_precision=PB,cell_precision=PC,checks=checks,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,source_counts=dict(branches=45,polynomial_coefficients=count),files=files,results=results,scope='Complete independent exact-source and cell reconstruction of only the specified ordinary slabs. Each passing joint flag requires independent actual review. No global background or existence conclusion.')
put('check_v01.json',record)
print('COMPLETED',record['status'],record['finished_utc'],record['elapsed_seconds'],checks,flush=True)
