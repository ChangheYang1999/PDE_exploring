"""Resolve inverse versus retained-annulus quadrature errors of a frozen Q state."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math
from angular_log_inverse import QAngular,weighted_diagnostic
from q_weighted_tail_bounds import constants,tails,serialize

ap=argparse.ArgumentParser();ap.add_argument('diagnostic');ap.add_argument('--tag',required=True);args=ap.parse_args()
old=json.loads(Path(args.diagnostic).read_text());model=QAngular(old['snapshot'])
cc=constants(model.coeff,model.kappa,model.cl)
out=Path('evidence/q_weighted_refinement')/args.tag;out.mkdir(parents=True,exist_ok=True)
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source_diagnostic=args.diagnostic,
            snapshot=old['snapshot'],metadata=model.meta,rows=[])
for m in [2.5,3.]:
 base=[r for r in old['rows'] if r['m']==m][-1];lo,hi=base['z_window']
 for inv,rad,width,ang in [(128,32,1.,8*model.M+32),(192,32,1.,8*model.M+32),(256,32,1.,8*model.M+32)]:
  row=weighted_diagnostic(model,m,inv,rad,lo,hi,panel_width=width,angles=ang)
  tb=tails(cc,m,int(lo),int(hi));Th=float(tb['h_lower']+tb['h_upper']);Tf=float(tb['F_lower']+tb['F_upper'])
  nh=row['h_norm_squared_in_core_units'];nf=row['F_norm_squared_in_core_units']
  row['panel_width']=width;row['exact_rational_tail_bounds']=serialize(tb)
  row['tail_h_over_quadrature_h']=Th/nh;row['tail_F_over_quadrature_h']=Tf/nh
  row['ratio_range_if_annular_quadrature_exact']=[math.sqrt(nf/(nh+Th)),math.sqrt((nf+Tf)/nh)]
  result['rows'].append(row);result['updated_utc']=datetime.now(timezone.utc).isoformat()
  (out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({k:row[k]for k in ['m','inverse_order','radial_order','angles','E','identity_defect']}),flush=True)
result['status']='COMPUTED';result['scope']='One inverse order at a time with a fixed refined radial/angular rule; exact omitted-tail bounds, but retained-annulus values are not interval enclosures. No profile-proximity assertion.'
result['finished_utc']=datetime.now(timezone.utc).isoformat();(out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
