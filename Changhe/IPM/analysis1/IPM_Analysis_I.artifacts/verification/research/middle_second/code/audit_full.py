"""Separate saved-output auditor: exact coverage/counts, Arb768 scalar integrals.
This does not regenerate unsaved polynomial coefficients. Their full-run source
and completed comparison counts remain explicit dependencies of the result.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,argparse,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,ctx
if sys.flags.optimize:raise RuntimeError('Assertions must be active')
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_second/evidence';PE=BASE/'research/middle_residual/evidence'
BKEYS=('W_upper_exact','W_over_m_upper_exact','Wm_times_one_plus_u_power_half_upper_exact','Wm_times_one_plus_u_power_half_minus_k_upper_exact')
POINTS=(0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808)
COUNTS={'coefficient_overlap_checks':8874,'center_moment_overlap_checks':522,'shifted_density_overlap_checks':2096,'exact_integer_convolutions':8}

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def aq(q):q=F(q);return arb(q.numerator)/q.denominator
def exact(x):
 assert x.is_finite() and x.rad()==0
 mantissa,exponent=x.man_exp();return F(int(mantissa))*F(2)**int(exponent)
def endpoints(x):
 assert x.is_finite()
 return exact(x.lower()),exact(x.upper())
def upper(x):return endpoints(x)[1]
def interval(v,positive=False):
 lo,hi=F(v['lower_exact']),F(v['upper_exact']);assert 0<=lo<=hi
 if positive:assert lo>0
 return lo,hi

def required_pins(primary_tag):
 names={
  'research/middle_second/PROOF.md','research/middle_second/code/audit_full.py',
  *('research/middle_second/code/'+name+'.py' for name in ['cell_iv','check_cells','run_full','check_driver','check_algebra','check_contracts']),
  *('research/middle_second/evidence/'+name+'.json' for name in ['contracts','algebra_contracts','driver_contracts','smoke_strengthened','smoke_strengthened_summary']),
  *('research/middle_residual/code/'+name+'.py' for name in ['cell_core','fast_moments','audit_full_output']),
  'research/ball_transport/code/dyadic_ball.py','data_exact/modal_v2.json',
  *('research/middle_residual/evidence/'+name for name in ['partition_exact.json','original_knots.jsonl.gz','knot_manifest.json','knot_audit.json',primary_tag+'_cells.jsonl',primary_tag+'_summary.json',primary_tag+'_output_audit.json']),
  *('research/residual_samples/evidence/'+name+'.json' for name in ['sample_result','laurent_output_audit']),
  *('research/residual_samples/code/'+name+'.py' for name in ['certify_samples','audit_output_laurent']),
 }
 for region in ['inner','outer']:
  names.update(['research/'+region+'_cells/evidence/verdict.json','research/'+region+'_cells/evidence/full_q16_manifest.json','research/'+region+'_majorant/evidence/exact_'+region+'_coefficients.json'])
 return names
def check_required_pins(head):assert required_pins(head['primary_tag'])<=set(head['pins'])

def check_region_joins(knots):
 joins={}
 for region,endpoint,label,expected in [('inner',knots[0],'ta_exact','0e20d17cdf606d10a9dde40d7d3ca511e509321947aa97a97838c7a84ba70b21'),('outer',knots[-1],'tb_exact','9a3d6cdce158574bd532f44c27b83aecb5007c985bdefa35e4f95e4f81dac9d6')]:
  p=BASE/('research/'+region+'_cells/evidence/verdict.json');assert sha(p)==expected;v=json.loads(p.read_text());assert v['status']=='CONFIRMED'
  cp=BASE/('research/'+region+'_majorant/evidence/exact_'+region+'_coefficients.json');mp=p.with_name('full_q16_manifest.json')
  assert sha(cp)==v['files'][str(cp.relative_to(BASE))] and sha(mp)==v['files'][str(mp.relative_to(BASE))]
  c=json.loads(cp.read_text());manifest=json.loads(mp.read_text());assert c['input_sha256']==sha(BASE/'data_exact/modal_v2.json')
  assert F(c[label])==endpoint and F(manifest['cells'][-1][1] if region=='inner' else manifest['cells'][0][0])==0
  joins[region]={'log_radius_exact':str(endpoint),'verdict_sha256':sha(p),'relative_cell_boundary_exact':'0'}
 return joins

def inspect_row(row,ci,expected,primary,k,L,point_audits):
 si,l,r=expected;assert row['type']=='cell' and row['cell']==ci and row['parent_span']==si
 assert (F(row['left_exact']),F(row['right_exact']))==(l,r)
 assert row['primary_row_sha256']==hashlib.sha256(canon(primary)).hexdigest()
 assert row['primary_scalar_equality_checks']==22
 ir=row['iv'];assert (F(ir['left_exact']),F(ir['right_exact']),F(ir['tc_exact']),F(ir['h_exact']))==(l,r,(l+r)/2,(r-l)/2)
 assert ir['Q']==16 and ir['Pint']==512 and ir['iv_dps']==160 and ir['mpmath_version']=='1.3.0' and ir['python_flint_version']=='0.9.0'
 for key,value in COUNTS.items():assert ir[key]==value
 assert F(ir['max_abs_ODE_lambda_h_exact'])==263*(r-l) and F(ir['max_center_moment_interval_width_exact'])>=0
 for key in ('W','W_over_m','nonpolynomial_remainder','diagnostic_max_density_moment_remainder','L2_squared'):interval(ir[key])
 retained,discarded=F(ir['retained_Bernstein_sum_exact']),F(ir['discarded_polynomial_remainder_exact']);assert retained>=0 and discarded>=0
 W=F(ir['W']['upper_exact']);M=F(ir['W_over_m']['upper_exact'])
 assert W>=retained+discarded+F(ir['nonpolynomial_remainder']['upper_exact'])
 ml,mh=interval(ir['m_left'],positive=True);assert M*ml>=W
 ul=aq(l).exp()/aq(L);ur=aq(r).exp()/aq(L)
 # Different expression and higher-precision engine than iv production.
 m=ul**3*(1+ul**2)**aq((k-3)/2);fl,fu=endpoints(m);assert 0<ml<=fl<=fu<=mh
 powers=(F(0),F(1,2),F(1,2)-k);assert set(ir['weighted'])==set(map(str,powers)) and ir['weighted']['0']==ir['W_over_m']
 for delta in powers:
  interval(ir['weighted'][str(delta)])
  assert upper(aq(M)*(1+ur)**aq(delta))<=F(ir['weighted'][str(delta)]['upper_exact']),(ci,'iv weight',str(delta))
 volume=aq(L*L/2)*((1+ur**2)/(1+ul**2)).log();assert endpoints(volume)[0]>0
 assert upper(arb.pi()*aq(M*M)*volume)<=F(ir['L2_squared']['upper_exact']),(ci,'iv L2')
 ivbounds=(W,M,F(ir['weighted']['1/2']['upper_exact']),F(ir['weighted'][str(F(1,2)-k)]['upper_exact']))
 for key,value in zip(BKEYS,ivbounds):assert F(row['joint'][key])==max(F(primary[key]),value)
 jm=F(row['joint']['W_over_m_upper_exact']);assert F(row['joint']['L2_squared_upper_exact'])>=upper(arb.pi()*aq(jm*jm)*volume)
 haspoint=ci in POINTS
 assert ir['independent_point_iv_coefficient_overlaps']==(522 if haspoint else 0)
 assert row['point_checks']=={'independent_point_iv_coefficient_overlaps':522 if haspoint else 0,'independent_point_coefficient_overlaps':522 if haspoint else 0,'independent_point_W_inequalities':4 if haspoint else 0,'linked_prior_direct_angular_checks':5 if haspoint else 0}
 if haspoint:
  old=point_audits[ci];assert F(old['t_exact'])==(l+r)/2 and len(old['angular_checks'])==5
  for key,value,pkey in [('W',W,'W_upper_exact'),('W_over_m',M,'W_over_m_upper_exact')]:assert F(old[key]['upper_exact'])<=min(value,F(primary[pkey]))
 return retained,discarded,F(ir['nonpolynomial_remainder']['upper_exact'])

def audit(tag,partial=False):
 ctx.prec=768;ctx.threads=1;start=time.monotonic();assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 op=E/(tag+'_cells.jsonl');raw=op.read_bytes();assert raw.endswith(b'\n');lines=raw.splitlines();head=json.loads(lines[0]);rows=[json.loads(line) for line in lines[1:]]
 assert head['type']=='header' and head['schema']=='ipm-middle-second-v1' and head['cells_required']==7809 and head['spans_required']==1558
 assert (head['Q'],head['Pint'],head['primary_bits'],head['iv_dps'])==(16,512,384,160)
 assert 0<len(rows)<=7809
 if not partial:assert len(rows)==7809
 check_required_pins(head)
 for path,h in head['pins'].items():
  p=BASE/path;assert p.resolve().is_relative_to(BASE) and sha(p)==h,(path,'source/input changed')
 assert head['pins']['research/middle_second/code/audit_full.py']==sha(Path(__file__))
 trp=BASE/'data_exact/modal_v2.json';assert sha(trp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 tr=json.loads(trp.read_text());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][key])) for key in ('k','L')]
 assert 0<k<F(1,2) and L>0 and F(head['k_exact'])==k and F(head['L_exact'])==L
 knots=sorted({F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']});assert len(knots)==1559
 assert head['region_boundary_joins']==check_region_joins(knots)
 # Independent covering reconstruction from raw exact input knots and audited counts.
 part=json.loads((PE/'partition_exact.json').read_text());assert part['input_sha256']==sha(trp) and part['cells']==7809 and len(part['spans'])==1558
 expected=[]
 for si,p in enumerate(part['spans']):
  a,b=knots[si:si+2];count=p['count'];assert type(count) is int and count>0 and p['span']==si and p['first_cell']==len(expected)
  assert (F(p['a_exact']),F(p['b_exact']))==(a,b)
  for j in range(count):expected.append((si,((count-j)*a+j*b)/count,((count-j-1)*a+(j+1)*b)/count))
 assert len(expected)==7809 and all(expected[i][2]==expected[i+1][1] for i in range(7808))
 pt=head['primary_tag'];pa=PE/(pt+'_output_audit.json');primary_audit=json.loads(pa.read_text());assert primary_audit['status']=='PASS' and primary_audit['cells_audited']==7809
 pp=PE/(pt+'_cells.jsonl');assert sha(pp)==primary_audit['completed_output_sha256']
 assert sha(BASE/'research/middle_residual/code/audit_full_output.py')==primary_audit['source_sha256']
 with pp.open() as f:ph=json.loads(next(f));primary=[json.loads(line) for line in f]
 assert ph==head['primary_header']==primary_audit['run_header'] and len(primary)==7809
 assert sha(PE/'partition_exact.json')==head['pins']['research/middle_residual/evidence/partition_exact.json']==ph['partition_sha256']
 assert sha(PE/'original_knots.jsonl.gz')==ph['knot_input_sha256']
 source_sample=BASE/'research/residual_samples/evidence/sample_result.json';source_point=BASE/'research/residual_samples/evidence/laurent_output_audit.json'
 point=json.loads(source_point.read_text());assert point['status']=='PASS' and point['sample_result_sha256']==sha(source_sample) and point['direct_angular_checks']==65
 point_audits={r['cell']:r for r in point['samples']};assert sorted(point_audits)==list(POINTS)==head['point_cells']
 for p,h in point['dependencies'].values():assert sha(BASE/p)==h
 maxima={};remmax={};totals={key:0 for key in COUNTS};sq=F(0);width=F(0);pointcells=[]
 for ci,row in enumerate(rows):
  old=primary[ci];si,l,r=expected[ci]
  assert old['cell']==ci and old['parent_span']==si and (F(old['left_exact']),F(old['right_exact']))==(l,r)
  assert F(old['weight_power_half_exact'])==F(1,2) and F(old['weight_power_half_minus_k_exact'])==F(1,2)-k
  ul,ur=aq(l).exp()/aq(L),aq(r).exp()/aq(L)
  ml,mh=interval(old['m_left'],positive=True);a0,b0=endpoints(ul**3*(1+ul**2)**aq((k-3)/2));assert ml<=a0<=b0<=mh
  assert F(old['W_over_m_upper_exact'])*ml>=F(old['W_upper_exact'])
  for key,power in [(BKEYS[2],F(1,2)),(BKEYS[3],F(1,2)-k)]:assert F(old[key])>=upper(aq(F(old['W_over_m_upper_exact']))*(1+ur)**aq(power))
  rem=inspect_row(row,ci,expected[ci],primary[ci],k,L,point_audits)
  for key in BKEYS:
   value=F(row['joint'][key])
   if key not in maxima or value>F(maxima[key]['upper_exact']):maxima[key]={'cell':ci,'upper_exact':str(value)}
  for key,value in zip(('retained_Bernstein','discarded_degree17_32','nonpolynomial'),rem):
   if key not in remmax or value>F(remmax[key]['upper_exact']):remmax[key]={'cell':ci,'upper_exact':str(value)}
  for key in COUNTS:totals[key]+=row['iv'][key]
  sq+=F(row['joint']['L2_squared_upper_exact']);width=max(width,F(row['iv']['max_center_moment_interval_width_exact']))
  if ci in POINTS:pointcells.append(ci)
  if ci%1000==0:print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'checked':ci+1}),flush=True)
 sp=E/(tag+'_summary.json');summary=json.loads(sp.read_text());assert summary['run_header']==head and summary['cells_complete']==len(rows) and summary['output_sha256']==sha(op)
 assert summary['counts']==totals and summary['maxima']==maxima and F(summary['L2_squared_upper_exact'])==sq and F(summary['maximum_center_moment_interval_width_exact'])==width
 assert summary['point_cells_checked']==pointcells and F(summary['L2_upper_exact'])>=upper(aq(sq).sqrt())
 if not partial:assert summary['source_footer_read'] and summary['status']=='COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT' and pointcells==list(POINTS)
 def rounded(q):
  z=F(q)*10**12;return str(F(-((-z.numerator)//z.denominator),10**12))
 public={key:rounded(v['upper_exact']) for key,v in maxima.items()};public['L2']=rounded(summary['L2_upper_exact'])
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PARTIAL_TEST' if partial else 'PASS','method':'Independent exact covering/counts and Arb768 weights/integrals, both-method maxima, point dependencies, completed source/header/summary pins. Unsaved coefficient generation is not repeated by this auditor.','source_sha256':sha(Path(__file__)),'output_sha256':sha(op),'summary_sha256':sha(sp),'run_header':head,'cells_audited':len(rows),'counts':totals,'maxima':maxima,'remainder_maxima':remmax,'L2_squared_upper_exact':str(sq),'L2_upper_exact':summary['L2_upper_exact'],'public_upper_exact':public,'maximum_center_moment_interval_width_exact':str(width),'point_cells_checked':pointcells,'region_boundary_joins':head['region_boundary_joins'],'seconds':time.monotonic()-start,'scope':summary['scope']}
 out=E/(tag+'_output_audit.json');tmp=out.with_suffix('.json.tmp')
 with tmp.open('w') as f:f.write(json.dumps(result,indent=2)+'\n');f.flush();os.fsync(f.fileno())
 os.replace(tmp,out);fd=os.open(E,os.O_RDONLY|os.O_DIRECTORY)
 try:os.fsync(fd)
 finally:os.close(fd)
 print(json.dumps({'status':result['status'],'cells':len(rows),'seconds':result['seconds']}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full_iv16');ap.add_argument('--partial',action='store_true');args=ap.parse_args();audit(args.tag,args.partial)
