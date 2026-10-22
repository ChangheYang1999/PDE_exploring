"""Full omitted-cell audit using two directed, stable distance formulas."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_geometry';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):return [aq(x.lower()),aq(x.upper())] if isinstance(x,arb) else list(map(mq,x._mpi_))
def rec(x):lo,hi=ends(x);return {'lower_exact':str(lo),'upper_exact':str(hi),'display':[float(lo),float(hi)]}
def overlap(a,b):al,ah=ends(a);bl,bh=ends(b);assert max(al,bl)<=min(ah,bh)
start=time.monotonic();inp=E/'geometry_inputs.json';data=json.loads(inp.read_text())
for rel,h in data['files'].items():assert sha(B/rel)==h,rel
results={};total_unique=0;total_cases=0
for tag,run in data['runs'].items():
 pmin,pmax,p0,eps=map(F,[run['p_min_exact'],run['p_max_exact'],run['p0_exact'],run['epsilon_exact']]);assert p0-eps==pmin and p0+eps==pmax
 delta=F(run['delta_max_exact_decimal']);R=3*delta;a=F(run['selected_first_exact']);b=F(run['selected_last_exact']);theta_lo=F(run['theta_cap_exact'][0])
 coverage=[]
 assert pmin>R and 0<theta_lo<F(1,2)
 for engine,q,exp,sin in [('arb512',qa,lambda x:x.exp(),lambda x:x.sin()),('iv180',qi,iv.exp,iv.sin)]:
  rl,rh=exp(q(a)),exp(q(b));sine=sin(q(theta_lo))
  assert ends(rl)[1]<pmin-R and ends(rh)[0]>pmax+R and ends(sine)[0]>R/pmin
  coverage.append({'engine':engine,'first_radius':rec(rl),'last_radius':rec(rh),'cap_sine':rec(sine),'needed_sine_exact':str(R/pmin),'cap_lower_exact':str(theta_lo)})
 angular_node_checks=0;radial_node_checks=0
 for j,ang in enumerate(run['angular']):
  lo,hi=F(ang['lo_exact']),F(ang['hi_exact'])
  assert lo<=theta_lo*j/run['ntheta']<=theta_lo*(j+1)/run['ntheta']<=hi
  angular_node_checks+=2
 assert F(run['angular'][0]['lo_exact'])<=0
 for rad in run['radial']:
  left=F(rad['cell_left_exact']);h=F(rad['h_up_exact']);k=rad['k']
  assert h>=F(rad['cell_right_exact'])-left
  assert F(rad['t_lo_exact'])<=left+k*h/run['K']<=left+(k+1)*h/run['K']<=F(rad['t_hi_exact'])
  radial_node_checks+=2
 target={};cases=0
 for mask in run['masks']:
  d=F(mask['delta']);assert len(mask['omitted_per_radial'])==run['K']
  assert pmin>F(mask['cutoff_float_exact'])>=3*d
  for k,angles in enumerate(mask['omitted_per_radial']):
   assert len(angles)==len(set(angles)) and all(0<=j<run['ntheta'] for j in angles)
   for j in angles:
    key=(mask['ci'],k,j);target[key]=max(d,target.get(key,F()));cases+=1
 fullgrid=len(run['radial'])*run['ntheta']
 assert sum(fullgrid-v for v in run['counts'].values())==cases
 angles=[]
 for ang in run['angular']:
  lo=max(F(0),F(ang['lo_exact']));hi=F(ang['hi_exact']);assert 0<=lo<=hi<F(1,2)
  aa=qa(lo);mi=qi(lo);c=aa.cos();s=aa.sin();ci=iv.cos(mi);sh=iv.sin(mi/2)
  overlap(c,ci)
  angles.append((c,s,ci,sh))
 lower_gap=None;where=None;counts={'lower_endpoint':0,'upper_endpoint':0,'interior':0};unique=0;arb_iv_checks=0;maxthi=None;radial_examples=[]
 for rad in run['radial']:
  tl,th=F(rad['t_lo_exact']),F(rad['t_hi_exact']);assert tl<th
  maxthi=th if maxthi is None else max(maxthi,th)
  ar,br=qa(tl).exp(),qa(th).exp();air,bir=iv.exp(qi(tl)),iv.exp(qi(th));overlap(ar,air);overlap(br,bir)
  # One common rational outer radial box, taking the hull of both engines.
  rlo=min(ends(ar)[0],ends(air)[0]);rhi=max(ends(br)[1],ends(bir)[1]);assert rlo>0
  aa,bb,pa=qa(rlo),qa(rhi),qa(p0);ai,bi,pi=qi(rlo),qi(rhi),qi(p0)
  for j in range(run['ntheta']):
   key=(rad['ci'],rad['k'],j)
   if key not in target:continue
   d=target[key];threshold=(3*d+eps)**2;c,s,ci,sh=angles[j];rc=pa*c;rci=pi*ci
   if ends(rc)[1]<rlo and ends(rci)[1]<rlo:
    kind='lower_endpoint';r=aa;ri=ai
   elif ends(rc)[0]>rhi and ends(rci)[0]>rhi:
    kind='upper_endpoint';r=bb;ri=bi
   else:
    assert rlo<=ends(rc)[0]<=ends(rc)[1]<=rhi and rlo<=ends(rci)[0]<=ends(rci)[1]<=rhi,(key,'ambiguous clamp')
    kind='interior';r=rc;ri=rci
   if kind=='interior':
    da=(pa*s)**2
    # sin(alpha)^2=4 sin(alpha/2)^2 (1-sin(alpha/2)^2).
    si2=sh**2;di=4*pi**2*si2*(1-si2)
   else:
    da=(r-pa*c)**2+(pa*s)**2
    di=(ri-pi)**2+4*ri*pi*sh**2
   al,ah=ends(da);il,ih=ends(di);assert max(al,il)<=min(ah,ih),(key,'engine disjoint')
   gap=min(al,il)-threshold
   assert gap>0,(tag,key,str(d),float(gap))
   if lower_gap is None or gap<lower_gap:
    lower_gap=gap;where={'ci':rad['ci'],'k':rad['k'],'theta_index':j,'largest_omitted_delta_exact':str(d),'radial_outer_exact':[str(rlo),str(rhi)],'arb_squared_distance':rec(da),'iv_squared_distance':rec(di),'threshold_squared_exact':str(threshold)}
   counts[kind]+=1;unique+=1;arb_iv_checks+=1
  if len(radial_examples)<2:radial_examples.append({'ci':rad['ci'],'k':rad['k'],'radius_lo':rec(ar),'radius_hi':rec(br)})
  if rad['k']==0 and rad['ci']%10==0:
   print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'run':tag,'ci':rad['ci'],'unique':unique,'seconds':time.monotonic()-start}),flush=True)
   (E/'progress.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'run':tag,'ci':rad['ci'],'unique':unique,'seconds':time.monotonic()-start},indent=2)+'\n')
 assert unique==len(target)
 counter=[]
 if tag=='fine0165':
  armax=qa(maxthi).exp();irmax=iv.exp(qi(maxthi));upper=max(ends(armax)[1],ends(irmax)[1]);overlap(armax,irmax)
  for d in ['0.05','0.1','0.2']:
   witness=pmin+2*F(d);assert witness>upper
   counter.append({'delta_exact':str(F(d)),'witness_radius_lower_exact':str(witness),'coordinate_radius_arb_upper':rec(armax),'coordinate_radius_iv_upper':rec(irmax),'positive_gap_exact':str(witness-upper)})
 results[tag]={'angular_node_checks':angular_node_checks,'radial_node_checks':radial_node_checks,'coverage':coverage,'all_mask_omissions':cases,'unique_omitted_boxes':unique,'distance_engine_pairs':arb_iv_checks,'clamp_cases':counts,'minimum_squared_gap_exact':str(lower_gap),'worst_gap_box':where,'fine_large_disc_counterexamples':counter,'radial_examples':radial_examples}
 total_unique+=unique;total_cases+=cases
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_N8_COORDINATE_GEOMETRY_ONLY','counts':{'omitted_cell_delta_pairs':total_cases,'unique_omitted_boxes':total_unique,'two_engine_distance_pairs':total_unique,'fine_actual_domain_counterexamples':3},'results':results,'seconds':time.monotonic()-start,'scope':'Complete coordinate coverage only for intended deltas; no paired polynomial-domain or derivative certificate accepted.','files':{str(p.relative_to(B)):sha(p) for p in [inp,Path(__file__),D/'PROOF.md',E/'proof_first.json']}}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','counts','seconds']}),flush=True)
