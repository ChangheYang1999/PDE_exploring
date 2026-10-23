"""Independent Q weighted residual and strain diagnostics with explicit tail bounds.

Requires both our manufactured strain checks and our cross-inverse comparison.
No producer numerical code is imported. Whole-plane truncation is bounded from
exact binary coefficients; annular quadrature is refined but not enclosed.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math
import numpy as np
from angular_log_inverse import QAngular,AngularLogInverse,weighted_diagnostic
from q_weighted_tail_bounds import constants,tails,serialize

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);args=ap.parse_args()
for gate in ['research/angular_log_inverse/verification/strain_checks.json','evidence/angular_q_crosscheck.json',
             'research/finite_q_weighted_tails/verification/checks.json']:
 assert json.loads(Path(gate).read_text())['status']=='PASS',gate
model=QAngular(args.snapshot);cc=constants(model.coeff,model.kappa,model.cl)
outdir=Path('evidence/q_weighted')/args.tag;outdir.mkdir(parents=True,exist_ok=True)
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),tag=args.tag,snapshot=args.snapshot,metadata=model.meta,
            a=model.a,c=model.c,delta=model.cl+model.c-1,log_core=model.log_core,
            endpoint_quotient_rounding_l1=model.quotient_rounding_l1,coefficient_bounds=serialize(cc),rows=[])

def save():
 result['updated_utc']=datetime.now(timezone.utc).isoformat()
 (outdir/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')

for m in [2.5,3.]:
 preliminary=weighted_diagnostic(model,m,32,8,-12.,60.)
 base_norm=preliminary['h_norm_squared_in_core_units'];assert base_norm>0
 lo=-16;hi=64
 # The preliminary annulus supplies only a practical positive scale. Final
 # tail bounds themselves are exact rationals and do not use that estimate.
 while True:
  bounds=tails(cc,m,lo,hi)
  if float(bounds['h_lower']+bounds['F_lower'])<=1e-11*base_norm:break
  lo-=4
  if lo < -200:raise ArithmeticError('Near-origin tail target needs a wider safe window')
 while True:
  bounds=tails(cc,m,lo,hi)
  if float(bounds['h_upper']+bounds['F_upper'])<=1e-11*base_norm:break
  hi+=8
  if hi > 500:raise ArithmeticError('Exterior tail target needs a wider safe window')
 for order,radial,lower,upper in [(32,10,lo,hi),(64,14,lo,hi),(128,20,lo,hi),(128,20,lo-4,hi+8)]:
  row=weighted_diagnostic(model,m,order,radial,float(lower),float(upper))
  tb=tails(cc,m,lower,upper);Th=float(tb['h_lower']+tb['h_upper']);Tf=float(tb['F_lower']+tb['F_upper'])
  nh=row['h_norm_squared_in_core_units'];nf=row['F_norm_squared_in_core_units']
  row['exact_rational_tail_bounds']=serialize(tb)
  row['tail_h_over_quadrature_h']=Th/nh;row['tail_F_over_quadrature_h']=Tf/nh
  row['ratio_range_if_annular_quadrature_exact']=[math.sqrt(nf/(nh+Th)),math.sqrt((nf+Tf)/nh)]
  row['scope']='Exact rational tail bounds; annular quadrature is refined but not certified. The displayed ratio range assumes those annular values exact, so it is not an interval certificate of the full norm ratio.'
  result['rows'].append(row);save()
  print(json.dumps({'utc':result['updated_utc'],'tag':args.tag,**{k:row[k] for k in ['m','inverse_order','radial_order','z_window','E','identity_defect','tail_h_over_quadrature_h','tail_F_over_quadrature_h']}}),flush=True)

# Retain both a core-relative grid and a wide physical log-radius grid. Axes
# are included; these are lower estimates of global strain and radial compression.
z_core=np.linspace(-16.,24.,241)
physical_logr=np.arange(-160.,301.,2.)*math.log(10.)
logr=np.unique(np.concatenate((model.log_core+z_core,physical_logr)))
theta=np.linspace(0,math.pi/2,4*model.M+17)
result['strain_samples']=[]
for order in [64,128]:
 field=AngularLogInverse(model,order).fields(logr,theta)
 row={'inverse_order':order,'radii':len(logr),'angles':len(theta)}
 for name,values,origin in [('sigma',field['strain'],abs(model.c)),('radial_compression',-field['ur'],abs(model.c)),
                             ('gradient',field['gradient_norm'],abs(model.a))]:
  i,j=np.unravel_index(np.argmax(values),values.shape)
  sampled=float(values[i,j]);row[name]=dict(sampled_max=max(sampled,origin),origin=origin,
     largest_nonzero_radius_value=sampled,log10_radius=float(logr[i]/math.log(10.)),theta=float(theta[j]),
     origin_larger=bool(origin>sampled))
 row['sigma_over_D']=row['sigma']['sampled_max']/(model.cl-1)
 result['strain_samples'].append(row);save();print(json.dumps({'utc':result['updated_utc'],'tag':args.tag,'strain':row}),flush=True)
result['finished_utc']=datetime.now(timezone.utc).isoformat();result['status']='COMPUTED'
result['scope']='Independent finite coefficient diagnostics. Canonical velocity is the separately implemented angular logarithmic Green inverse, previously cross-checked with the real-space cancellation inverse. Weighted tails have exact rational bounds, retained-annulus values only quadrature refinement. Sampled strain and radial compression maxima are lower estimates. No uniform residual, proximity theorem, or endpoint verdict.'
save()
