"""Restartable exhaustive second method. A complete audited primary pass is required.
All retained coefficients are regenerated and compared before each small row is
committed. No worker concurrency, external writes, servers or JS are used.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,hashlib,argparse,time,resource,platform,fcntl
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import cell_iv,check_cells
if sys.flags.optimize:raise RuntimeError('Assertions must be active')
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_second/evidence';PE=BASE/'research/middle_residual/evidence'
BKEYS=('W_upper_exact','W_over_m_upper_exact','Wm_times_one_plus_u_power_half_upper_exact','Wm_times_one_plus_u_power_half_minus_k_upper_exact')
PKEYS=('coefficient_overlap_checks','center_moment_overlap_checks','shifted_density_overlap_checks','exact_integer_convolutions')

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def canonical(d):return json.dumps(d,sort_keys=True,separators=(',',':')).encode()
def syncdir(path):
 fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY)
 try:os.fsync(fd)
 finally:os.close(fd)
def acquire_lock(path):
 lock=Path(path).open('a+b')
 try:fcntl.flock(lock.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BaseException:lock.close();raise
 return lock
def atomic(path,data):
 path=Path(path);tmp=path.with_name(path.name+'.tmp')
 with tmp.open('w') as f:f.write(json.dumps(data,indent=2)+'\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,path);syncdir(path.parent)
def af(q):q=F(q);return arb(q.numerator)/q.denominator
def aq(x):
 assert x.is_finite() and x.rad()==0
 mantissa,exponent=x.man_exp();return F(int(mantissa))*F(2)**int(exponent)
def up(x):return aq(x.upper())
def strip_displays(value):
 if isinstance(value,dict):return {k:strip_displays(v) for k,v in value.items() if k!='display'}
 if isinstance(value,list):return [strip_displays(v) for v in value]
 return value

def joint(ar,ir,k,L,left,right):
 keys={'W_upper_exact':ir['W']['upper_exact'],'W_over_m_upper_exact':ir['W_over_m']['upper_exact'],BKEYS[2]:ir['weighted']['1/2']['upper_exact'],BKEYS[3]:ir['weighted'][str(F(1,2)-k)]['upper_exact']}
 ans={key:str(max(F(ar[key]),F(keys[key]))) for key in BKEYS}
 ul=af(left).exp()/af(L);ur=af(right).exp()/af(L)
 volume=af(L*L/2)*((1+ur*ur)/(1+ul*ul)).log();assert volume.lower()>0
 l2=arb.pi()*af(F(ans['W_over_m_upper_exact'])**2)*volume
 ans['L2_squared_upper_exact']=str(up(l2));return ans

def validate_saved(row,ci,parts,primary,k,L):
 si,l,r=parts[ci];assert row['type']=='cell' and row['cell']==ci and row['parent_span']==si
 assert (F(row['left_exact']),F(row['right_exact']))==(l,r)
 assert row['primary_row_sha256']==hashlib.sha256(canonical(primary[ci])).hexdigest()
 ir=row['iv'];assert (F(ir['left_exact']),F(ir['right_exact']),F(ir['tc_exact']),F(ir['h_exact']))==(l,r,(l+r)/2,(r-l)/2)
 assert ir['Q']==16 and ir['Pint']==512 and ir['iv_dps']==160
 assert ir['mpmath_version']=='1.3.0' and ir['python_flint_version']=='0.9.0'
 assert tuple(ir[key] for key in PKEYS)==(8874,522,2096,8)
 assert row['primary_scalar_equality_checks']==22
 assert F(ir['max_abs_ODE_lambda_h_exact'])==526*(r-l)/2 and F(ir['max_center_moment_interval_width_exact'])>=0
 for key in ('W','W_over_m','nonpolynomial_remainder','diagnostic_max_density_moment_remainder','L2_squared'):
  lo,hi=F(ir[key]['lower_exact']),F(ir[key]['upper_exact']);assert 0<=lo<=hi
 ret,tail=F(ir['retained_Bernstein_sum_exact']),F(ir['discarded_polynomial_remainder_exact']);assert ret>=0 and tail>=0
 assert F(ir['W']['upper_exact'])>=ret+tail+F(ir['nonpolynomial_remainder']['upper_exact'])
 ml,mh=F(ir['m_left']['lower_exact']),F(ir['m_left']['upper_exact']);assert 0<ml<=mh
 assert F(ir['W_over_m']['upper_exact'])*ml>=F(ir['W']['upper_exact'])
 assert set(ir['weighted'])=={'0','1/2',str(F(1,2)-k)}
 assert ir['weighted']['0']==ir['W_over_m']
 for v in ir['weighted'].values():assert 0<=F(v['lower_exact'])<=F(v['upper_exact'])
 point=ci in (0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808)
 assert ir['independent_point_iv_coefficient_overlaps']==(522 if point else 0)
 assert row['point_checks']=={'independent_point_iv_coefficient_overlaps':522 if point else 0,'independent_point_coefficient_overlaps':522 if point else 0,'independent_point_W_inequalities':4 if point else 0,'linked_prior_direct_angular_checks':5 if point else 0}
 assert row['joint']==joint(primary[ci],ir,k,L,l,r)

def resume(path,header,parts,primary,k,L):
 path=Path(path)
 if path.exists():
  raw=path.read_bytes();lines=raw.splitlines(keepends=True);offset=0
  for index,line in enumerate(lines):
   if not line.endswith(b'\n'):
    assert index==len(lines)-1
    atomic(E/('recovery_'+str(time.time_ns())+'.json'),{'utc':utc(),'file':str(path.relative_to(BASE)),'original_sha256':hashlib.sha256(raw).hexdigest(),'original_bytes':len(raw),'retained_bytes':offset,'reason':'Final line lacks newline, whether or not JSON parses'})
    with path.open('r+b') as f:f.truncate(offset);f.flush();os.fsync(f.fileno())
    raw=raw[:offset];break
   offset+=len(line)
 else:raw=b''
 if not raw:
  with path.open('wb') as f:f.write(canonical(header)+b'\n');f.flush();os.fsync(f.fileno())
  syncdir(path.parent);return []
 lines=raw.splitlines();assert json.loads(lines[0])==header,'Source/input/header changed; use a new verified run'
 rows=[]
 for line in lines[1:]:
  row=json.loads(line);assert len(rows)<7809;validate_saved(row,len(rows),parts,primary,k,L);rows.append(row)
 return rows

def prepare(primary_tag):
 k,L,knots,pub,kp=check_cells.inputs();assert len(knots)==1559
 samples,audits,pointpins=check_cells.point_dependencies();assert sorted(samples)==[0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808]
 pa=PE/(primary_tag+'_output_audit.json');audit=json.loads(pa.read_text());assert audit['status']=='PASS' and audit['cells_audited']==7809
 pp=PE/(primary_tag+'_cells.jsonl');ps=PE/(primary_tag+'_summary.json');assert sha(pp)==audit['completed_output_sha256'] and sha(ps)==audit['summary_sha256']
 assert sha(BASE/'research/middle_residual/code/audit_full_output.py')==audit['source_sha256']
 with pp.open() as f:
  ph=json.loads(next(f));primary=[json.loads(line) for line in f]
 assert ph==audit['run_header'] and len(primary)==7809 and [r['cell'] for r in primary]==list(range(7809))
 ka=PE/'knot_audit.json';kaobj=json.loads(ka.read_text());manifest=PE/'knot_manifest.json';partition=PE/'partition_exact.json'
 assert kaobj['status']=='PASS' and kaobj['footer_read'] and sha(kp)==kaobj['archive_sha256']==ph['knot_input_sha256']
 assert sha(manifest)==kaobj['manifest_sha256']==ph['knot_manifest_sha256'] and sha(partition)==kaobj['partition_sha256']==ph['partition_sha256']
 assert sha(ka)==ph['knot_audit_sha256'];partdata=json.loads(partition.read_text());assert partdata['cells']==7809
 parts=[]
 for si,p in enumerate(partdata['spans']):
  assert p['span']==si and p['first_cell']==len(parts) and type(p['count']) is int and p['count']>0
  a,b=F(p['a_exact']),F(p['b_exact']);assert (a,b)==tuple(knots[si:si+2])
  for j in range(p['count']):parts.append((si,a+(b-a)*F(j,p['count']),a+(b-a)*F(j+1,p['count'])))
 assert len(parts)==7809 and len(partdata['spans'])==1558
 for ci,(si,l,r) in enumerate(parts):assert primary[ci]['parent_span']==si and (F(primary[ci]['left_exact']),F(primary[ci]['right_exact']))==(l,r)
 sourcepaths=[Path(__file__),Path(cell_iv.__file__),Path(check_cells.__file__),Path(__file__).parent/'audit_full.py',Path(__file__).parent/'check_driver.py',Path(__file__).parent/'check_algebra.py',Path(__file__).parent/'check_contracts.py',BASE/'research/middle_second/PROOF.md']
 evidence=[BASE/'research/middle_residual/code/audit_full_output.py',E/'contracts.json',E/'algebra_contracts.json',E/'driver_contracts.json',E/'smoke_strengthened.json',E/'smoke_strengthened_summary.json',pa,pp,ps,ka,manifest,partition,kp,BASE/'data_exact/modal_v2.json']
 joins={}
 for region,endpoint,label,expected_hash in [('inner',knots[0],'ta_exact','0e20d17cdf606d10a9dde40d7d3ca511e509321947aa97a97838c7a84ba70b21'),('outer',knots[-1],'tb_exact','9a3d6cdce158574bd532f44c27b83aecb5007c985bdefa35e4f95e4f81dac9d6')]:
  vp=BASE/('research/'+region+'_cells/evidence/verdict.json');mp=vp.with_name('full_q16_manifest.json');cp=BASE/('research/'+region+'_majorant/evidence/exact_'+region+'_coefficients.json')
  assert sha(vp)==expected_hash;v=json.loads(vp.read_text());c=json.loads(cp.read_text());rm=json.loads(mp.read_text())
  assert v['status']=='CONFIRMED' and v['files'][str(cp.relative_to(BASE))]==sha(cp) and v['files'][str(mp.relative_to(BASE))]==sha(mp)
  assert c['input_sha256']==sha(BASE/'data_exact/modal_v2.json') and F(c[label])==endpoint
  assert F(rm['cells'][-1][1] if region=='inner' else rm['cells'][0][0])==0
  joins[region]={'log_radius_exact':str(endpoint),'verdict_sha256':sha(vp),'relative_cell_boundary_exact':'0'};evidence.extend([vp,mp,cp])
 pins={str(p.relative_to(BASE)):sha(p) for p in sourcepaths+evidence};pins.update(pointpins)
 for key,path in [('cell_core','research/middle_residual/code/cell_core.py'),('fast_moments','research/middle_residual/code/fast_moments.py'),('ball_transport','research/ball_transport/code/dyadic_ball.py')]:
  assert sha(BASE/path)==ph['hashes'][key];pins[path]=sha(BASE/path)
 for f in ['contracts','algebra_contracts']:
  obj=json.loads((E/(f+'.json')).read_text());assert obj['status'].startswith('PASS') and obj['cell_iv_sha256']==sha(Path(cell_iv.__file__))
 smoke=json.loads((E/'smoke_strengthened.json').read_text());ss=json.loads((E/'smoke_strengthened_summary.json').read_text());assert ss['full_output_sha256']==sha(E/'smoke_strengthened.json')
 for path,h in smoke['pins'].items():assert sha(BASE/path)==h
 dc=json.loads((E/'driver_contracts.json').read_text());assert dc['status']=='PASS_DRIVER_AUDITOR_CONTRACTS'
 for path,h in dc['pins'].items():assert sha(BASE/path)==h
 header={'type':'header','schema':'ipm-middle-second-v1','cells_required':7809,'spans_required':1558,'Q':16,'Pint':512,'primary_bits':384,'iv_dps':160,'k_exact':str(k),'L_exact':str(L),'pins':pins,'primary_header':ph,'primary_tag':primary_tag,'point_cells':sorted(samples),'region_boundary_joins':joins}
 return k,L,knots,pub,kp,samples,audits,primary,partdata,parts,header

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full_iv16');ap.add_argument('--primary-tag',default='full_q16');ap.add_argument('--stop-after',type=int,default=7809);args=ap.parse_args()
 assert args.tag.replace('_','').isalnum() and args.primary_tag.replace('_','').isalnum() and 0<args.stop_after<=7809
 lock=acquire_lock(E/(args.tag+'.lock'))
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));ctx.prec=384;ctx.threads=1
 start=time.monotonic();k,L,knots,pub,kp,samples,audits,primary,pd,parts,header=prepare(args.primary_tag)
 outpath=E/(args.tag+'_cells.jsonl');rows=resume(outpath,header,parts,primary,k,L);nextci=len(rows);assert nextci<=args.stop_after
 atomic(E/(args.tag+'_runtime_'+str(os.getpid())+'.json'),{'utc':utc(),'pid':os.getpid(),'python':platform.python_version(),'optimize':sys.flags.optimize,'PYTHONOPTIMIZE':os.environ.get('PYTHONOPTIMIZE'),'single_thread_env':{key:os.environ[key] for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},'source_sha256':sha(Path(__file__)),'initial_completed':nextci})
 data=cell_iv.setup(k,L);seen=0;first=0;footer=False;emit(stage='start_or_resume',completed=nextci,stop_after=args.stop_after)
 with gzip.open(kp,'rt') as inp,outpath.open('ab') as out:
  ih=json.loads(next(inp));assert ih['type']=='header' and ih['spans']==1558 and ih['cells']==7809
  for line in inp:
   item=json.loads(line)
   if item['type']=='complete':assert seen==1558 and first==7809 and item['spans']==1558 and item['cells']==7809 and not inp.read();footer=True;break
   assert item['type']=='span' and item['span']==seen and item['first_cell']==first and item['count']>0
   assert all(item[key]==value for key,value in pd['spans'][seen].items());seen+=1;first+=item['count']
   if first<=nextci:continue
   span=cell_iv.decode_span(item)
   for offset in range(item['count']):
    ci=item['first_cell']+offset
    if ci<nextci:continue
    assert ci==nextci
    if ci>=args.stop_after:break
    si,left,right=parts[ci];tc=(left+right)/2;point=check_cells.primary_point(item,tc,left,right);point['cell']=ci
    ar=check_cells.cell_core.bound_cell(point,k,L,knots,pub,Q=16,keep_coefficients=True);scalar_checks=0
    for key,value in ar.items():
     if key not in ('residual_coefficients_z','seconds'):assert primary[ci][key]==value,(ci,key);scalar_checks+=1
    ir=cell_iv.bound_cell(data,span,left,right,ar,point,samples[ci]['residual_coefficients'] if ci in samples else None)
    pointresult=check_cells.check_point(ci,point,ar,ir,samples,audits)
    row={'type':'cell','cell':ci,'parent_span':si,'left_exact':str(left),'right_exact':str(right),'primary_row_sha256':hashlib.sha256(canonical(primary[ci])).hexdigest(),'primary_scalar_equality_checks':scalar_checks,'iv':strip_displays(ir),'point_checks':pointresult,'joint':joint(primary[ci],ir,k,L,left,right)}
    validate_saved(row,ci,parts,primary,k,L)
    out.write(canonical(row)+b'\n');out.flush();os.fsync(out.fileno());rows.append(row);nextci+=1
    if ci%25==0 or ci in samples:emit(stage='cell_done',cell=ci,Wm_iv=ir['W_over_m']['display'],seconds=time.monotonic()-start)
    if nextci%25==0:atomic(E/(args.tag+'_progress.json'),{'utc':utc(),'cells_complete':nextci,'cells_required':7809,'seconds_this_process':time.monotonic()-start,'source_sha256':sha(Path(__file__))})
   if nextci>=args.stop_after and args.stop_after<7809:break
 assert nextci==args.stop_after
 if args.stop_after==7809:assert footer
 totals={key:sum(r['iv'][key] for r in rows) for key in PKEYS};maxima={key:max(rows,key=lambda r:F(r['joint'][key])) for key in BKEYS}
 sq=sum((F(r['joint']['L2_squared_upper_exact']) for r in rows),F(0));l2=up(af(sq).sqrt())
 summary={'utc':utc(),'status':'COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT' if footer else 'PARTIAL','cells_complete':nextci,'cells_required':7809,'source_footer_read':footer,'run_header':header,'output_sha256':sha(outpath),'counts':totals,'maxima':{key:{'cell':r['cell'],'upper_exact':r['joint'][key]} for key,r in maxima.items()},'L2_squared_upper_exact':str(sq),'L2_upper_exact':str(l2),'maximum_center_moment_interval_width_exact':str(max(F(r['iv']['max_center_moment_interval_width_exact']) for r in rows)),'point_cells_checked':[r['cell'] for r in rows if r['point_checks']['independent_point_coefficient_overlaps']],'seconds_this_process':time.monotonic()-start,'scope':'Only the exact modal trial middle-region zeroth residual; no derivative estimate, inverse, original X3 distance or PDE endpoint.'}
 atomic(E/(args.tag+'_summary.json'),summary);emit(stage='done',status=summary['status'],cells=nextci,seconds=time.monotonic()-start)
 lock.close()
if __name__=='__main__':main()
