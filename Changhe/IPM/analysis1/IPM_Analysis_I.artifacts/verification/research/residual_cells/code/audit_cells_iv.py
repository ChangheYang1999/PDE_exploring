"""Independent interval Bernstein conversion by polynomial shifting and finite differences."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/residual_cells/evidence';iv.dps=75

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def fi(v):sg,m,e,_=v;return (-1 if sg else 1)*F(int(m))*F(2)**int(e)
def ends(v):return tuple(map(fi,v._mpi_))
def ball(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1'
 m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return iv.mpf([iq(m-r).a,iq(m+r).b])
def abupper(v):a,b=ends(v);return max(abs(a),abs(b))
def bernbounds(coeff):
 # Independent Horner translation p(z) -> p(w-1), then differences of Bernstein coefficients.
 d=[]
 for v in reversed(coeff):
  v=ball(v)
  if not d:d=[v]
  else:d=[v-d[0]]+[d[i-1]-d[i] for i in range(1,len(d))]+[d[-1]]
 Q=len(coeff)-1
 return max(abupper(sum((d[q]*iq(F(2**q*math.comb(k,q),math.comb(Q,q))) for q in range(k+1)),iv.mpf(0))) for k in range(Q+1))
def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 raw=E/'q16_result.json';rr=E/'q16_replay_result.json';a=json.loads(raw.read_bytes());r=json.loads(rr.read_bytes());src=B/'research/residual_cells/code/certify_cells.py';assert sha(src)==a['source_sha256']==r['source_sha256']=='f5735ca567e0208b6a233fed253136030b538f637a8ab8164f06ab890150c5fd'
 for name in ('primitives.json','angular_fixture.json','zero_radius_replay.json'):
  v=json.loads((E/name).read_bytes());assert v['status']=='PASS' and v['implementation_sha256']==sha(src)
 assert json.loads((E/'zero_radius_replay.json').read_bytes())['result_sha256']==sha(rr)
 for name in ('q16.log','replay.log'):
  v=json.loads((E/name).read_text().splitlines()[-1]);assert v['stage']=='done' and v['cells']==13
 samples=json.loads((B/'research/residual_samples/evidence/sample_result.json').read_bytes());assert [v['cell'] for v in r['cells']]==[v['cell'] for v in samples['samples']]==[v['cell'] for v in a['cells']];assert len(r['cells'])==13
 functional=json.loads((B/'research/residual_samples/evidence/functional_provenance.json').read_bytes());assert functional['status']=='PASS';tr=json.loads((B/'data_exact/modal_v2.json').read_bytes());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')]
 pubp=B/'research/residual_samples/evidence/published_residual_snapshot.json';assert sha(pubp)==r['comparison_sha256']=='439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331';pub=json.loads(pubp.read_bytes(),parse_float=F)
 records=[]
 for old,row,point in zip(a['cells'],r['cells'],samples['samples']):
  ci=row['cell'];assert row['residual_coefficients_z']==old['residual_coefficients_z'] and row['W_upper_exact']==old['W_upper_exact'] and row['W_over_m_upper_exact']==old['W_over_m_upper_exact'];assert [row['left_exact'],row['right_exact']]==point['cell_endpoints_exact'];assert F(row['tc_exact'])==F(point['t_exact'])
  Q=row['degree'];assert Q==16 and len(row['residual_coefficients_z'])==522 and all(len(c)==Q+1 for c in row['residual_coefficients_z']);poly=sum(map(bernbounds,row['residual_coefficients_z']),F(0));tail=sum((F(row[n]['upper_exact']) for n in ('nonpolynomial_remainder','discarded_polynomial_remainder')),F(0));assert tail>=0
  W=poly+tail;u=iv.exp(iq(row['left_exact']))/iq(L);weight=u**3*(1+u*u)**iq((k-3)/2);ml=ends(weight)[0];assert ml>0;Wm=W/ml;pw,pwm=pub['rows'][ci]['W'],pub['rows'][ci]['W_over_m'];assert W<=pw and Wm<=pwm
  rec={'cell':ci,'W_upper_exact_iv':str(W),'Wm_upper_exact_iv':str(Wm),'W_upper_display_iv':str(iq(W)),'Wm_upper_display_iv':str(iq(Wm)),'published_W_exact':str(pw),'published_Wm_exact':str(pwm),'verdict':'CONFIRMED_SELECTED_CELL'};records.append(rec);print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'cell':ci,'verdict':rec['verdict']}),flush=True)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','method':'mpmath.iv75 Horner translation and Bernstein finite-difference conversion; exact rational comparisons','source_sha256':sha(__file__),'cell_source_sha256':sha(src),'original_result_sha256':sha(raw),'replay_result_sha256':sha(rr),'functional_provenance_sha256':sha(B/'research/residual_samples/evidence/functional_provenance.json'),'cells':records,'seconds':time.monotonic()-start,'scope':'13selectedfullcells. Inherits independently enclosed input moments and analytically checked ODE/product remainders. No global or untested-cell bound.'}
 (E/'iv_output_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'stage':'done','status':'PASS','seconds':result['seconds']}),flush=True)
if __name__=='__main__':main()
