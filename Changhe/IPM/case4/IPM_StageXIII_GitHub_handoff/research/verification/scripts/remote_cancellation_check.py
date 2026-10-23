"""Independent high-precision remote-field diagnosis, no fitting or writes to inputs."""
import argparse
import importlib.util
import math
from pathlib import Path
import sys
import time

PROJECT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(PROJECT))
from absolute_common import np,read,atomic,digest,provenance
from absolute_fields_v2 import prepare_candidate,fields,residual
from field_tests import independent_fields
from threadpoolctl import threadpool_limits

def main(args):
    began=time.time()
    if args.output.exists():raise ValueError('Fresh output file required')
    audit_source=PROJECT/'farfield_asymptotic_audit_20261022_0836/coefficients_audit.py'
    spec=importlib.util.spec_from_file_location('original_farfield_coefficients',audit_source)
    audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
    case=read(args.candidate);model=prepare_candidate(case,'center_chart');cl=float(model['p'][0]);gamma=1/cl;lam=1-gamma
    potentials,_=audit.potential_layers(model,6);F,Phi,_=audit.physical_layers(potentials,gamma,lam,6)
    E,_,_=audit.residual_layers(F,Phi,cl,gamma,lam,6)
    rows=[]
    for radius in (1e12,1e16,1e20):
        for theta in (0.,math.pi/6,math.pi/2):
            x=radius*math.cos(theta);y=radius*math.sin(theta)
            if theta==0:y=0.
            if theta==math.pi/2:x=0.
            high=independent_fields(model,x,y,85)
            # Compare at the actual binary64 point rather than its intended radius.
            r=math.hypot(x,y);angle=math.atan2(y,x);tt=np.asarray([angle])
            series_rho=sum(r**(gamma-k*lam-2*q)*float(audit.evaluate(a,tt)[0]) for (k,q),a in E.items())
            series_rf=sum(r**(gamma-k*lam-2*q-1)*float(audit.evaluate_cosines(audit.quotient_cosines(a)[0],tt)[0]) for (k,q),a in E.items())
            got=float(residual(model,[x],[y])[0]);ff=fields(model,[x],[y]);rf85=high['Rf'];rho85=y*rf85
            density_direct=(cl*x-float(ff['psiy'][0]))*y*float(ff['fx'][0])+(cl*y+float(ff['psix'][0]))*(float(ff['f'][0])+y*float(ff['fy'][0]))-y*float(ff['f'][0])
            error=abs(series_rf-rf85)/max(abs(rf85),1e-300)
            row={'radius':radius,'theta':theta,'xy':[x,y],'Rf_85digit_cartesian':rf85,'Rrho_85digit_cartesian':rho85,
                'Rf_analytic_q6_series':series_rf,'Rrho_analytic_q6_series':series_rho,
                'series_vs_85digit_Rf_relative_error':error,'series_vs_85digit_Rrho_absolute_error':abs(series_rho-rho85),
                'stateless_binary64_Rf':got,'stateless_binary64_Rrho_from_yRf':y*got,'stateless_binary64_direct_Rrho':density_direct,
                'binary64_vs_85digit_Rf_relative_error':abs(got-rf85)/max(abs(rf85),1e-300),
                'direct_density_binary64_error_abs':abs(density_direct-rho85),
                'series_vs_HP_tolerance_relative':1e-8,'passed':error<=1e-8}
            if radius==1e20 and theta==math.pi/2:
                higher=independent_fields(model,x,y,110);error2=abs(higher['Rf']-rf85)/max(abs(higher['Rf']),1e-300)
                row['Rf_110digit_cartesian']=higher['Rf'];row['precision85_vs110_Rf_relative_error']=error2
                row['precision_refinement_tolerance_relative']=1e-20;row['passed'] &=error2<=1e-20
            rows.append(row)
            atomic(args.output,{'completed':False,'rows':rows,'candidate_sha256':digest(args.candidate)})
    record={'schema':'stage13_remote_residual_cancellation_high_precision_check_v1','completed':True,'passed':all(z['passed'] for z in rows),
        'candidate_path':str(args.candidate.resolve()),'candidate_sha256':digest(args.candidate),
        'worker_sha256':digest(Path(__file__)),'original_coefficient_worker_sha256':digest(audit_source),
        'environment':provenance(),'cl':cl,'gamma':gamma,'leading_density_residual_power':2*gamma-1,
        'rows':rows,'seconds':time.time()-began,
        'reference':'85-digit independent Cartesian Taylor arithmetic at actual evaluation point; one110-digit precision check',
        'coefficient_arithmetic':'Original immutable finite-Fourier/binomial coefficient implementation; q0..6, exact leading linear cancellation used in recurrence',
        'normalization_note':'Cartesian reference uses algebraic sqrt(2n+1), whereas original coefficient/production routines use their mathematically equivalent historical binary64 gammaln/exp expression. Differences are retained.',
        'scope':'Selected-point diagnosis only; no rigorous all-angle/asymptotic remainder bound, no coefficients changed, no optimization',
        'binary64_extreme_remote_samples_certified':False}
    atomic(args.output,record)
    print(record['passed'],flush=True)
    if not record['passed']:raise SystemExit(2)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    with threadpool_limits(limits=1,user_api='blas'):main(p.parse_args())
