"""Second hydrostatic axis inverse on frozen numeric states. Result190."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,argparse,time
sys.set_int_max_str_digits(0)
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint
from q_mp_primitives import guard_digits
from hydrostatic_axis_primitive import primitive,AxisPrimitive,mnum
root=Path('research/hydrostatic_axis_primitive/verification')
source=Path('research/hydrostatic_state_audit/verification')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()

def state(tag):
 src=source/'states'/(tag+'.pt');q=QLocalCheckpoint(src);base=json.loads((source/(tag+'.json')).read_text());polys=primitive(q.exact_coefficients(),q.kappa)
 cert={key:[[str(v.numerator),str(v.denominator)]for v in val]if isinstance(val,list)else[str(val.numerator),str(val.denominator)]for key,val in polys.items()}
 certpath=root/(tag+'.polynomial.json');certpath.write_text(json.dumps(cert,indent=2)+'\n')
 chosen={}
 for region in ['core','annulus','far']:
  row=base['regions'][region]['R_Nf']
  if row['x']==0:chosen[float(row['y'])]=dict(region=region,original=row)
 # Include center scale as a witness even if the sampled peak is off axis.
 if not chosen:chosen[.219]=dict(region='independent_probe',original=None)
 path=root/(tag+'.json');out=dict(tag=tag,started_utc=now(),status='RUNNING',source_sha256=sha(src),polynomial_sha256=sha(certpath),code_sha256=sha(__file__),primitive_sha256=sha('independent_code/hydrostatic_axis_primitive.py'),proof_sha256=sha(root.parent/'PROOF.md'),points=[])
 path.write_text(json.dumps(out,indent=2)+'\n')
 for y,info in sorted(chosen.items()):
  row=dict(y=y,source_region=info['region'],primary_result=info['original'],refinements=[])
  for digits,order in [(70,24),(70,40),(100,56)]:
   t0=time.monotonic()
   with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
    a=AxisPrimitive(polys,q.kappa,q.L,q.cl);Y=mnum(y);vals=a.residual(Y,order)
    # Scalar differentiation of the polynomial density as an independent gy check.
    gdiff=mp.diff(lambda z:z*__import__('hydrostatic_axis_primitive').evaluate(a.H,a.coordinate(z)),Y)
    gy_error=abs(gdiff-vals['gy'])
    row['refinements'].append(dict(target_digits=digits,working_digits=mp.mp.dps,order=order,seconds=time.monotonic()-t0,gy_scalar_diff_error=mp.nstr(gy_error,digits),values={k:mp.nstr(v,digits)if v is not None else None for k,v in vals.items()}))
   path.write_text(json.dumps({**out,'current_point':row},indent=2)+'\n');print(now(),tag,'y',y,'order',order,'NF',row['refinements'][-1]['values']['R_Nf'][:24],flush=True)
  with mp.workdps(120):
   r1,r2,r3=row['refinements'];row['refinement_differences']={k:dict(order24_40=str(abs(mp.mpf(r1['values'][k])-mp.mpf(r2['values'][k]))),order40_56=str(abs(mp.mpf(r2['values'][k])-mp.mpf(r3['values'][k]))))for k in ['V2','R','R_Nf','R_Nv']}
   if info['original']:
    row['primary_differences']={k:str(abs(mp.mpf(r3['values'][k])-mp.mpf(info['original'][k])))for k in ['g','gy','V2','R','R_Nf','R_Nv']}
  out['points'].append(row);path.write_text(json.dumps(out,indent=2)+'\n')
 out.update(status='DONE',finished_utc=now());path.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,'DONE',flush=True)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tags',required=True);args=ap.parse_args()
 gate=json.loads((root/'GATE.json').read_text());assert gate['status']=='PASS'and gate['code_sha256']==sha('independent_code/hydrostatic_axis_primitive.py')
 meta=json.loads((source/'METADATA_RECHECK.json').read_text());confirmed={s['tag']for s in meta['states']if s['verdict'].startswith('CONFIRMED')}
 for tag in args.tags.split(','):
  assert tag in confirmed;state(tag)
if __name__=='__main__':main()
