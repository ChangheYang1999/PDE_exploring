"""Selected complete middle cells, primary regeneration and independent iv checks."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,gzip,hashlib,argparse,time,resource
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import ctx
import cell_iv
BASE=Path(__file__).resolve().parents[3];PE=BASE/'research/middle_residual/evidence';E=BASE/'research/middle_second/evidence'
sys.path.insert(0,str(BASE/'research/middle_residual/code'))
from fast_moments import aa,integral,shift_poly
import cell_core
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball,export_ball

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def primary_point(item,tc,left,right):
 a,b=F(item['a_exact']),F(item['b_exact']);center=F(item['polynomial_mid_exact']);delta=tc-center;hl=tc-a;hr=b-tc
 polys=[[import_ball(v) for v in p] for p in item['density_polynomials']]
 I=list(map(import_ball,item['i_left']));J=list(map(import_ball,item['j_right']));ivals=[];jvals=[];cache={}
 for n in range(1,262):
  rate=-2*n-4;ivals.append(aa(rate*hl).exp()*I[n-1]+integral(polys[n-1],delta,hl,rate,True,cache))
  rate=4-2*n;jvals.append(aa(rate*hr).exp()*J[n-1]+integral(polys[n],delta,hr,rate,False,cache))
 jets=[shift_poly(p,delta) for p in polys]
 return {'cell_endpoints_exact':[str(left),str(right)],'t_exact':str(tc),'density_polynomial_at_point':[[export_ball(x) for x in p] for p in jets],'i':list(map(export_ball,ivals)),'j':list(map(export_ball,jvals))}

def inputs():
 trp=BASE/'data_exact/modal_v2.json';assert sha(trp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 tr=json.loads(trp.read_text());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')]
 knots=sorted(set(F.from_float(float.fromhex(x)) for x in tr['arrays']['knots']['hex']))
 pp=BASE/'research/residual_samples/evidence/published_residual_snapshot.json';assert sha(pp)=='439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331'
 pub=json.loads(pp.read_text(),parse_float=F);kp=PE/'original_knots.jsonl.gz';assert sha(kp)=='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
 return k,L,knots,pub,kp

def point_dependencies():
 sp=BASE/'research/residual_samples/evidence/sample_result.json';ap=BASE/'research/residual_samples/evidence/laurent_output_audit.json'
 sample=json.loads(sp.read_text());audit=json.loads(ap.read_text())
 assert sha(sp)==audit['sample_result_sha256']=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c'
 assert audit['status']=='PASS' and audit['coefficients_audited']==6786 and audit['direct_angular_checks']==65
 assert sha(BASE/'research/residual_samples/code/audit_output_laurent.py')==audit['source_sha256']
 assert sha(BASE/'research/residual_samples/code/certify_samples.py')==audit['sample_source_sha256']==sample['source_sha256']
 for path,h in audit['dependencies'].values():assert sha(BASE/path)==h
 assert len(sample['samples'])==len(audit['samples'])==13
 return {x['cell']:x for x in sample['samples']},{x['cell']:x for x in audit['samples']},{str(p.relative_to(BASE)):sha(p) for p in [sp,ap,BASE/'research/residual_samples/code/certify_samples.py',BASE/'research/residual_samples/code/audit_output_laurent.py']}

def check_point(ci,point,ar,ir,samples,audits):
 if ci not in samples:
  assert ir['independent_point_iv_coefficient_overlaps']==0
  return {'independent_point_iv_coefficient_overlaps':0,'independent_point_coefficient_overlaps':0,'independent_point_W_inequalities':0,'linked_prior_direct_angular_checks':0}
 old=samples[ci];assert len(old['residual_coefficients'])==522 and len(ar['residual_coefficients_z'])==522 and ir['independent_point_iv_coefficient_overlaps']==522
 assert old['t_exact']==point['t_exact'] and old['cell_endpoints_exact']==point['cell_endpoints_exact']
 assert audits[ci]['t_exact']==point['t_exact']
 for actual,saved in zip(ar['residual_coefficients_z'],old['residual_coefficients']):
  a,b=cell_iv.ball_ends(actual[0]);u,v=cell_iv.ball_ends(saved);assert max(a,u)<=min(b,v)
 for key,pkey in [('W','W_upper_exact'),('W_over_m','W_over_m_upper_exact')]:
  upper=F(audits[ci][key]['upper_exact']);assert upper<=F(ar[pkey]) and upper<=F(ir[key]['upper_exact'])
 return {'independent_point_iv_coefficient_overlaps':522,'independent_point_coefficient_overlaps':522,'independent_point_W_inequalities':4,'linked_prior_direct_angular_checks':len(audits[ci]['angular_checks'])}

def run(cells,tag):
 assert not sys.flags.optimize;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));ctx.prec=384;ctx.threads=1
 start=time.monotonic();k,L,knots,pub,kp=inputs();data=cell_iv.setup(k,L);targets=set(cells);saved={};samples,audits,point_pins=point_dependencies()
 with (PE/'full_q16_cells.jsonl').open() as f:
  header=json.loads(next(f))
  for line in f:
   row=json.loads(line)
   if row['cell'] in targets:saved[row['cell']]=row
   if row['cell']>=max(targets):break
 assert set(saved)==targets,'Smoke cells must be present in current completed primary output'
 results=[]
 with gzip.open(kp,'rt') as f:
  ih=json.loads(next(f));assert ih['type']=='header'
  for line in f:
   item=json.loads(line)
   if item['type']=='complete':break
   here=sorted(targets.intersection(range(item['first_cell'],item['first_cell']+item['count'])))
   if not here:continue
   span=cell_iv.decode_span(item);a,b=span['a'],span['b']
   for ci in here:
    offset=ci-item['first_cell'];left=a+(b-a)*F(offset,item['count']);right=a+(b-a)*F(offset+1,item['count']);tc=(left+right)/2
    point=primary_point(item,tc,left,right);point['cell']=ci
    ar=cell_core.bound_cell(point,k,L,knots,pub,Q=16,keep_coefficients=True)
    scalar_checks=0
    for key,value in ar.items():
     if key not in ('residual_coefficients_z','seconds'):
      assert saved[ci][key]==value,('primary regeneration differs',ci,key);scalar_checks+=1
    ir=cell_iv.bound_cell(data,span,left,right,ar,point,samples[ci]['residual_coefficients'] if ci in samples else None)
    assert ir['coefficient_overlap_checks']==8874 and ir['center_moment_overlap_checks']==522 and ir['shifted_density_overlap_checks']==2096
    point_result=check_point(ci,point,ar,ir,samples,audits)
    ar.pop('residual_coefficients_z')
    result={'cell':ci,'primary_scalar_equality_checks':scalar_checks,'arb':ar,'independent_iv_integer':ir,'independent_point_comparison':point_result}
    results.append(result);targets.remove(ci)
    print(json.dumps({'utc':utc(),'cell':ci,'iv_seconds':ir['seconds'],'Wm_iv':ir['W_over_m']['display'],'coefficient_checks':ir['coefficient_overlap_checks']}),flush=True)
   if not targets:break
 assert not targets
 paths=[Path(__file__),Path(cell_iv.__file__),BASE/'research/middle_second/code/check_algebra.py',E/'algebra_contracts.json',BASE/'research/middle_second/PROOF.md',BASE/'research/middle_second/code/check_contracts.py',E/'contracts.json',BASE/'research/middle_residual/code/cell_core.py',BASE/'research/middle_residual/code/fast_moments.py',BASE/'research/ball_transport/code/dyadic_ball.py']
 pins={str(p.relative_to(BASE)):sha(p) for p in paths};pins.update(point_pins)
 result={'utc':utc(),'status':'PASS_SELECTED_COMPLETE_CELLS','pins':pins,'archive_sha256':sha(kp),'primary_header':header,'cells':results,'seconds':time.monotonic()-start,'scope':'Selected cells only; no exhaustive second-method certificate.'}
 dest=E/(tag+'.json');tmp=dest.with_name(dest.name+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,dest);assert json.loads(dest.read_text())==result
 print(json.dumps({'utc':utc(),'status':result['status'],'seconds':result['seconds']}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--cells',required=True);ap.add_argument('--tag',required=True);args=ap.parse_args();run([int(s) for s in args.cells.split(',')],args.tag)
