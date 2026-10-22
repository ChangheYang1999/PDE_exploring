"""Independent exact/interval audit of the completed full middle-region output.

This does not pretend to re-create unsaved Bernstein coefficients. The complete
Arb computation is independently implemented relative to the numerics lane;
this auditor checks its partition, scalar bounds, weights, maxima and provenance.
"""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from importlib.metadata import version
from mpmath import iv
BASE=Path(__file__).resolve().parents[3]
E=BASE/'research/middle_residual/evidence'
iv.dps=150
PINS={
 'driver':'c702a3f4370cabde16d8e37f77af03efc84f7b75a4a6ea5f022407750a8328c1',
 'cell_core':'a7679c9586f83e203d09fe3f8028e150f7da41082d769fa495840a82be71fdc1',
 'fast_moments':'63e7d5e3543ed72b1e383e6945394b52069d30489d7b32e4bc56f424931f7156',
 'ball_transport':'6525060f436bf553f3b4a42e403ad2c27dc69d6a82a1460634995f95e755e3c3',
 'archive_audit':'c4bdd40b67e364c759b069efb7e5a70c0a3bb583c3aae4d9cb3177772f040ef2',
}
BKEYS=('W_upper_exact','W_over_m_upper_exact','Wm_times_one_plus_u_power_half_upper_exact','Wm_times_one_plus_u_power_half_minus_k_upper_exact')
RKEYS=('retained_Bernstein_sum','nonpolynomial_remainder','discarded_polynomial_remainder','max_Green_remainder')
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def fr(v):
 sg,m,e,bc=v;assert bc>=0,'non-finite interval endpoint';return (-1 if sg else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert finite(x),'non-finite interval';return tuple(fr(v) for v in x._mpi_)
def finite(x):return all(v[3]>=0 for v in x._mpi_) # zero has bitcount0; no infinities/nan allowed

def audit(tag,partial=False):
 start=time.monotonic();source=Path(__file__)
 libraries={k:version(k) for k in ('python-flint','mpmath','numpy')}
 assert libraries=={'python-flint':'0.9.0','mpmath':'1.3.0','numpy':'2.5.0'}
 fixture_path=E/'nonfinite_guard_checks.json';fixture=json.loads(fixture_path.read_bytes())
 assert fixture['status']=='PASS' and fixture['auditor_sha256']==sha(source)
 assert fixture['source_sha256']==sha(source.parent/'check_output_nonfinite.py')
 paths={'driver':source.parent/'run_cells.py','cell_core':source.parent/'cell_core.py','fast_moments':source.parent/'fast_moments.py','ball_transport':BASE/'research/ball_transport/code/dyadic_ball.py','archive_audit':source.parent/'audit_knots.py'}
 assert {k:sha(p) for k,p in paths.items()}==PINS
 op=E/(tag+'_cells.jsonl');raw=op.read_bytes();assert raw.endswith(b'\n')
 lines=raw.splitlines();head=json.loads(lines[0]);rows=[json.loads(v,parse_float=F) for v in lines[1:]]
 assert head['schema']=='ipm-middle-cell-bounds-v1' and head['cells_required']==7809 and head['degree']==16 and head['precision_bits']==384 and head['hashes']==PINS
 assert 0<len(rows)<=7809
 if not partial:assert len(rows)==7809
 trp=BASE/'data_exact/modal_v2.json';assert sha(trp)==head['modal_input_sha256']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 data=json.loads(trp.read_bytes());k,L=[F.from_float(float.fromhex(data['scalars_hex'][s])) for s in ('k','L')];assert 0<k<1 and L>0
 assert k==F(head['k_exact']) and L==F(head['L_exact'])
 knots=sorted(set(F.from_float(float.fromhex(v)) for v in data['arrays']['knots']['hex']));assert len(knots)==1559
 depfiles={'knot_manifest_sha256':E/'knot_manifest.json','knot_audit_sha256':E/'knot_audit.json','partition_sha256':E/'partition_exact.json','setup_checks_sha256':E/'setup_checks.json','knot_input_sha256':E/'original_knots.jsonl.gz','comparison_sha256':BASE/'research/residual_samples/evidence/published_residual_snapshot.json','point_crosscheck_sha256':BASE/'research/residual_samples/evidence/sample_result.json'}
 for key,p in depfiles.items():assert sha(p)==head[key],key
 ka=json.loads(depfiles['knot_audit_sha256'].read_bytes());assert ka['status']=='PASS' and ka['footer_read'] and ka['source_sha256']==PINS['archive_audit'] and ka['archive_sha256']==head['knot_input_sha256'] and ka['manifest_sha256']==head['knot_manifest_sha256']
 assert ka['partition_sha256']==head['partition_sha256']
 setup=json.loads(depfiles['setup_checks_sha256'].read_bytes());assert setup['status']=='PASS'
 for filename,label in [('cell_core.py','cell_core'),('fast_moments.py','fast_moments')]:assert setup['hashes'][filename]==PINS[label]
 for filename in ('check_setup.py','modal_setup.py'):assert setup['hashes'][filename]==sha(source.parent/filename)
 partition=json.loads(depfiles['partition_sha256'].read_bytes());assert partition['schema']=='ipm-middle-partition-v1' and partition['input_sha256']==head['modal_input_sha256'] and partition['grid_sha256']=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
 assert partition['cells']==7809 and len(partition['spans'])==1558
 expected=[]
 for i,p in enumerate(partition['spans']):
  assert p['span']==i and p['first_cell']==len(expected) and isinstance(p['count'],int) and p['count']>0
  left,right=F(p['a_exact']),F(p['b_exact']);assert (left,right)==tuple(knots[i:i+2]);count=p['count']
  for j in range(count):expected.append((i,left+(right-left)*F(j,count),left+(right-left)*F(j+1,count)))
 assert len(expected)==7809 and all(expected[i][2]==expected[i+1][1] for i in range(7808))
 pub=json.loads(depfiles['comparison_sha256'].read_bytes(),parse_float=F);assert len(pub['rows'])==7809
 maxima={key:None for key in BKEYS};remainders={key:None for key in RKEYS};counts={'W_below_published':0,'Wm_below_published':0};l2=iv.mpf(0);checks=[]
 for ci,row in enumerate(rows):
  parent,left,right=expected[ci];assert row['type']=='cell' and row['cell']==ci and row['parent_span']==parent and row['degree']==16
  assert F(row['left_exact'])==left and F(row['right_exact'])==right and F(row['tc_exact'])==(left+right)/2 and F(row['h_exact'])==(right-left)/2
  # Dimensional A/B ODE rates are +/-2n, n<=261. The distinct
  # scaled-density moment integration has rates up to526; audit_knots pins it.
  assert F(row['max_abs_lambda_h_exact'])==522*(right-left)/2
  bounds={key:F(row[key]) for key in BKEYS};assert all(v>=0 for v in bounds.values())
  for key in RKEYS:
   lo,hi=(F(row[key][s]) for s in ('lower_exact','upper_exact'));assert 0<=lo<=hi
   if remainders[key] is None or hi>remainders[key]['upper']:remainders[key]={'cell':ci,'upper':hi}
  W=bounds[BKEYS[0]];Wm=bounds[BKEYS[1]]
  assert W>=sum((F(row[key]['upper_exact']) for key in RKEYS[:3]),F(0))
  ml,mh=(F(row['m_left'][s]) for s in ('lower_exact','upper_exact'));assert 0<ml<=mh and Wm*ml>=W
  rl,rr=iv.exp(iq(left)),iv.exp(iq(right));ul,ur=rl/iq(L),rr/iq(L)
  weight=ul**3*iv.exp(iq((k-3)/2)*iv.log(1+ul*ul));wl,wh=ends(weight)
  assert 0<ml<=wl<=wh<=mh,(ci,'m enclosure')
  for label,fresh in [('r_left',rl),('r_right',rr)]:
   a,b=ends(fresh);assert F(row[label]['lower_exact'])<=a<=b<=F(row[label]['upper_exact']),(ci,label)
  for name,power in [('half',F(1,2)),('half_minus_k',F(1,2)-k)]:
   assert F(row['weight_power_'+name+'_exact'])==power
   umax=ur if power>=0 else ul
   factor=iv.exp(iq(power)*iv.log(1+umax));fresh=iq(Wm)*factor
   assert finite(fresh) and ends(fresh)[1]<=bounds['Wm_times_one_plus_u_power_'+name+'_upper_exact'],(ci,name)
  for key in BKEYS:
   if maxima[key] is None or bounds[key]>maxima[key]['upper']:maxima[key]={'cell':ci,'upper':bounds[key],'left_exact':str(left),'right_exact':str(right)}
  assert pub['rows'][ci]['ci']==ci
  for own,reported,field,counter in [(W,'W','published_W_exact','W_below_published'),(Wm,'W_over_m','published_Wm_exact','Wm_below_published')]:
   pw=pub['rows'][ci][reported];assert F(row[field])==pw
   if own<=pw:counts[counter]+=1
   expected_label='CONFIRMED_SELECTED_CELL' if own<=pw else 'NOT_SHARP_ENOUGH'
   assert row['W_comparison' if field=='published_W_exact' else 'Wm_comparison']==expected_label
  # Parseval gives integral_theta |epsilon|^2 <= pi W^2.
  # Integrating r/(1+(r/L)^2) gives L^2/2 log of the endpoint ratio.
  integral=iq(L*L/2)*iv.log((1+ur*ur)/(1+ul*ul));assert ends(integral)[0]>0
  l2+=iv.pi*iq(Wm*Wm)*integral
  if ci%1000==0:print(json.dumps({'utc':utc(),'checked':ci+1,'cells_in_file':len(rows)}),flush=True)
  if ci in (0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808):checks.append(ci)
 summary_path=E/(tag+'_summary.json');summary=json.loads(summary_path.read_bytes())
 assert summary['cells_complete']==len(rows) and summary['run_header']==head and summary['output_sha256']==hashlib.sha256(raw).hexdigest() and summary['hashes']==PINS
 assert summary['input_sha256']==head['knot_input_sha256']
 if not partial:assert summary['source_footer_read'] and summary['status']=='COMPUTED_REQUIRES_INDEPENDENT_OUTPUT_AUDIT'
 for key,r in maxima.items():
  old=summary['maxima'][key];assert old['cell']==r['cell'] and F(old['bound_exact'])==r['upper'] and old['left_exact']==r['left_exact'] and old['right_exact']==r['right_exact']
 result={'utc':utc(),'status':'PASS_PARTIAL_TEST' if partial else 'PASS','method':'Exact-rational coverage, remainder decomposition and comparisons; independent mpmath.iv150 weights and radii, exhaustive maxima, canonical dependency hashes, and a Parseval/Wiener L2 bound','source_sha256':sha(source),'library_versions':libraries,'nonfinite_fixture_sha256':sha(fixture_path),'completed_output_sha256':sha(op),'summary_sha256':sha(summary_path),'run_header':head,'cells_audited':len(rows),'maxima':{key:{**r,'upper':str(r['upper'])} for key,r in maxima.items()},'remainder_maxima':{key:{'cell':r['cell'],'upper_exact':str(r['upper'])} for key,r in remainders.items()},'published_comparisons':counts,'L2_squared_upper_exact':str(ends(l2)[1]),'L2_upper_exact':str(ends(iv.sqrt(l2))[1]),'L2_display':str(iv.sqrt(l2)),'L2_definition':'Square root of integral over the full two-dimensional annulus t_0<=log(r)<=t_S, 0<=theta<=2pi, of |epsilon(r,theta)/m(r)|^2 r dr dtheta/(1+(r/L)^2). The residual is the real sine series sum_{n=0}^{521} epsilon_n(r) sin((2n+1)theta); Parseval factor pi.','selected_locations_present':checks,'seconds':time.monotonic()-start,'scope':'Middle-region R0 and this explicit L2 bound only. Inherits the audited independent full Arb Taylor/Bernstein computation and moment archive; does not recompute unsaved Bernstein coefficients. No center/exterior/derivative norm, X3 distance, inverse or endpoint.'}
 dest=E/(tag+'_output_audit.json');dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','status':result['status'],'cells':len(rows),'seconds':result['seconds']}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--tag',default='full_q16');ap.add_argument('--partial',action='store_true');a=ap.parse_args();audit(a.tag,a.partial)
