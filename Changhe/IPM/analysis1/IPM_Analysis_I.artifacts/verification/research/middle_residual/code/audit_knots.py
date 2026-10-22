"""Archive structure, partition, width and canonical cross-method audit."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
from fast_moments import aa,phi_values,integral,shift_poly
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_residual/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def ff(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def main():
 ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 kp=E/'original_knots.jsonl.gz';mp=E/'knot_manifest.json';manifest=json.loads(mp.read_bytes());assert sha(kp)==manifest['output_sha256']
 dp=BASE/'data_exact/modal_v2.json';tr=json.loads(dp.read_bytes());assert sha(dp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 knots=sorted(set(F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']));assert len(knots)==1559
 gp=BASE.parent/'ipmA-num/data/cert_green.npz';assert sha(gp)=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 with np.load(gp,allow_pickle=False) as gg:
  parents=gg['parent'];assert parents.ndim==1 and len(parents)==7809 and np.issubdtype(parents.dtype,np.integer)
  counts=np.bincount(parents,minlength=1558);assert len(counts)==1558 and all(counts>0)
  assert np.array_equal(parents,np.repeat(np.arange(1558),counts))
  partition=[];first=0;minwidth=None;maxspan=F(0)
  for si,(a,b,count) in enumerate(zip(knots[:-1],knots[1:],counts)):
   count=int(count);width=(b-a)/count;minwidth=width if minwidth is None else min(minwidth,width);maxspan=max(maxspan,b-a)
   partition.append({'span':si,'first_cell':first,'count':count,'a_exact':str(a),'b_exact':str(b)})
   for q in range(count):
    x=a+q*width;m=F.from_float(float(gg['tb'][first+q]));r=F.from_float(float(gg['tb_rad'][first+q]));assert r>=0 and m-r<=x<=m+r
   first+=count
  assert first==7809 and len(gg['tb'])==len(gg['tb_rad'])==7810
  m=F.from_float(float(gg['tb'][-1]));r=F.from_float(float(gg['tb_rad'][-1]));assert r>=0 and m-r<=knots[-1]<=m+r
 pp=E/'partition_exact.json';pp.write_text(json.dumps({'schema':'ipm-middle-partition-v1','input_sha256':sha(dp),'grid_sha256':sha(gp),'cells':7809,'spans':partition},indent=2)+'\n')
 # Smallest nonzero midpoint argument is width: rate 2 times half a child width.
 args=[minwidth,-minwidth,526*maxspan,-526*maxspan];argument_checks=[]
 for z in args:
  ph=phi_values(z);argument_checks.append({'z_exact':str(z),'minimum_accuracy_bits':min(v.rel_accuracy_bits() for v in ph)})
 sp=BASE/'research/residual_samples/evidence/sample_result.json';assert sha(sp)=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c';points={r['cell']:r for r in json.loads(sp.read_bytes())['samples']}
 minbits={'i_left':None,'j_right':None,'density_polynomials':None};maxrad={key:F(0) for key in minbits};cross=[];ballcount=0;seen=0;footer=False
 with gzip.open(kp,'rt') as f:
  head=json.loads(next(f));assert head['hashes']==manifest['hashes'] and head['cells']==7809 and head['spans']==1558 and head['comparison_grid_sha256']==sha(gp)
  dep={'source':Path(__file__).parent/'build_knot_moments.py','setup':Path(__file__).parent/'modal_setup.py','fast_moments':Path(__file__).parent/'fast_moments.py','input':dp,'normalization':BASE/'research/modal_repair/evidence/independent_gauss_iv.json','Cox':BASE/'research/canonical_inverse/code/exact_audit.py','ball_transport':BASE/'research/ball_transport/code/dyadic_ball.py'}
  assert {k:sha(p) for k,p in dep.items()}==head['hashes']
  for line in f:
   assert line.endswith('\n');rec=json.loads(line)
   if rec['type']=='complete':
    assert seen==1558 and rec['spans']==1558 and rec['cells']==7809 and not f.read();footer=True;break
   part=partition[seen];assert rec['type']=='span' and all(rec[k]==v for k,v in part.items());seen+=1
   a,b=F(rec['a_exact']),F(rec['b_exact']);mid=(a+b)/2;assert F(rec['polynomial_mid_exact'])==mid
   pol=[[import_ball(v) for v in p] for p in rec['density_polynomials']];I=list(map(import_ball,rec['i_left']));J=list(map(import_ball,rec['j_right']))
   assert len(pol)==262 and all(len(p)==8 for p in pol) and len(I)==len(J)==261 and all(v==0 for v in pol[-1])
   for key,seq in [('i_left',I),('j_right',J),('density_polynomials',[v for p in pol for v in p])]:
    for v in seq:
     assert v.is_finite();ballcount+=1;maxrad[key]=max(maxrad[key],ff(v.rad()))
     if not v.is_exact():
      bits=int(v.rel_accuracy_bits());minbits[key]=bits if minbits[key] is None else min(bits,minbits[key])
   for ci in sorted(points.keys() & set(range(rec['first_cell'],rec['first_cell']+rec['count']))):
    old=points[ci];q=ci-rec['first_cell'];left=a+(b-a)*F(q,rec['count']);right=a+(b-a)*F(q+1,rec['count']);tc=(left+right)/2
    assert old['t_exact']==str(tc) and old['cell_endpoints_exact']==[str(left),str(right)]
    cache={};count=0
    for n in range(1,262):
     x=aa(-(2*n+4)*(tc-a)).exp()*I[n-1]+integral(pol[n-1],tc-mid,tc-a,-(2*n+4),True,cache)
     y=aa((4-2*n)*(b-tc)).exp()*J[n-1]+integral(pol[n],tc-mid,b-tc,4-2*n,False,cache)
     assert x.overlaps(import_ball(old['i'][n-1])) and y.overlaps(import_ball(old['j'][n-1]));count+=2
    jets=[shift_poly(p,tc-mid) for p in pol]
    for p,op in zip(jets,old['density_polynomial_at_point']):
     for x,y in zip(p,op):assert x.overlaps(import_ball(y));count+=1
    cross.append({'cell':ci,'ball_comparisons':count})
   if seen%200==0:print(json.dumps({'utc':utc(),'spans_audited':seen,'seconds':time.monotonic()-start}),flush=True)
 assert footer and sorted(v['cell'] for v in cross)==sorted(points)
 result={'utc':utc(),'status':'PASS','source_sha256':sha(__file__),'archive_sha256':sha(kp),'manifest_sha256':sha(mp),'partition_sha256':sha(pp),'sample_sha256':sha(sp),'spans':seen,'cells':7809,'boundary_balls_checked':7810,'balls_checked_finite':ballcount,'minimum_relative_accuracy_bits':minbits,'maximum_ball_radii_exact':{k:str(v) for k,v in maxrad.items()},'minimum_child_width_exact':str(minwidth),'maximum_parent_width_exact':str(maxspan),'moment_argument_endpoint_checks':argument_checks,'sample_crosschecks':cross,'footer_read':footer,'seconds':time.monotonic()-start,'scope':'Structure, source linkage, finite widths, canonical midpoint comparison at13cells. Enclosure follows the separately audited recurrences; no independent second full archive integration.'}
 (E/'knot_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
