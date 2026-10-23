#!/usr/bin/env python3
"""Recompute selected saved norm integrands at a higher target precision."""
import argparse,json,hashlib,time,sys
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
from polar_derivative_norms import QNormEvaluator
ap=argparse.ArgumentParser();ap.add_argument('quadrature');ap.add_argument('--dps',type=int,default=120);args=ap.parse_args()
p=Path(args.quadrature);q=json.loads(p.read_text());assert q['status']=='COMPUTED';assert args.dps>q['dps']
rawpath=Path(q['input']);assert hashlib.sha256(rawpath.read_bytes()).hexdigest()==q['input_sha256'];raw=json.loads(rawpath.read_text())
assert raw['source_sha256']==q['source_sha256']
for file,key in [('independent_code/polar_derivative_norms.py','norm_code_sha256'),('independent_code/compact_norm_quadrature.py','code_sha256')]:assert hashlib.sha256(Path(file).read_bytes()).hexdigest()==q[key]
with mp.workdps(args.dps):
    rows=q['rows'];inds={0,len(rows)-1}
    for target in ['.001','.01','.1','1','10','100']:
        inds.add(min(range(len(rows)),key=lambda i:abs(mp.log(mp.mpf(rows[i]['r'])/mp.mpf(target)))))
    for k in range(2,q['kmax']+1):
        for field in ['rho','residual']:
            inds.add(max(range(len(rows)),key=lambda i:mp.mpf(rows[i]['values'][str(k)][field])*mp.mpf(rows[i]['jacobian'])))
record={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','quadrature':str(p),'quadrature_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'source_sha256':q['source_sha256'],'input_sha256':q['input_sha256'],'original_dps':q['dps'],'new_dps':args.dps,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'norm_code_sha256':q['norm_code_sha256'],'rows':[],'scope':'Higher-precision checks at selected nodes, including both extremes, six physical radii and the integrand peaks of each absolute norm. Radius strings retain up to65 digits from the original quadrature. This is a local arithmetic check, not a new full integral or an interval error bound.'}
out=p.parent/f'precision_nodes{q["nodes"]}_{q["dps"]}_{args.dps}.json'
def save():record['updated_utc']=datetime.now(timezone.utc).isoformat();out.write_text(json.dumps(record,indent=2)+'\n')
save();model=QNormEvaluator(raw['coefficients'],raw['L'],raw['kappa'],raw['ell'],dps=args.dps,kmax=q['kmax']);record['inverse_working_dps']=model.workdps;worst=mp.mpf(0)
with mp.workdps(args.dps):
    for i in sorted(inds):
        start=time.monotonic();old=rows[i];r=mp.mpf(old['r']);new=model.at_radius(r);errors={}
        for k in range(2,q['kmax']+1):
            errors[str(k)]={}
            for field in ['rho','residual']:
                a=mp.mpf(old['values'][str(k)][field]);b=new[k][field];den=max(abs(a),abs(b));e=abs(a-b)/den if den else mp.mpf(0);worst=max(worst,e)
                errors[str(k)][field]=mp.nstr(e,55)
        record['rows'].append({'original_index':i,'r':old['r'],'elapsed_seconds':time.monotonic()-start,'relative_errors':errors,'recomputed':{str(k):{field:mp.nstr(v,75) for field,v in row.items()} for k,row in new.items()}})
        save();print(json.dumps({'utc':record['updated_utc'],'state':p.parent.name,'node':i,'nodes_selected':len(inds),'maximum_relative_error_so_far':mp.nstr(worst,10)}),flush=True)
    record['maximum_relative_error']=mp.nstr(worst,65);record['threshold']='1e-35';record['status']='PASS' if worst<mp.mpf('1e-35') else 'REQUIRES_REVIEW'
record['finished_utc']=datetime.now(timezone.utc).isoformat();save()
if record['status']!='PASS':sys.exit(1)
