"""Guarded preparation checks for an absolute-loss model; never optimize."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Derivative checks must run under the resource supervisor')

import numpy as np
from absolute_chart import AbsoluteC5Chart, constraint_jacobian, hp_report
from absolute_model import AbsoluteLossProblem, FrozenLogMesh, tensor_gauss_mesh, array_hash

ROOT=Path(__file__).resolve().parent


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.partial')
    with tmp.open('w') as stream:
        json.dump(value,stream,indent=2,allow_nan=False);stream.write('\n')
        stream.flush();os.fsync(stream.fileno())
    tmp.replace(path)


def norm_error(actual,reference):
    return float(np.linalg.norm(actual-reference)/max(np.linalg.norm(reference),1e-300))


def run(args):
    began=time.time();candidate=json.loads(args.candidate.read_text())
    directory=ROOT/'results/derivatives'/args.label
    if directory.exists():raise ValueError('Derivative output exists; saved results cannot be overwritten')
    directory.mkdir(parents=True)
    base_mesh=tensor_gauss_mesh(-8.,16.,args.radial_panels,args.radial_order,args.angular_order,'derivative_test_only_finite_interval')
    # Include both sides of the Taylor/direct evaluator switch, and explicit
    # large-radius sites. A positive log-trapezoid rule is adequate for this
    # derivative test; no integration-accuracy conclusion is drawn from it.
    radial_probe_values=np.asarray([.005,.01,.015,.019,.02,.021,.03,.04,.1,.5,1.,2.,8.,64.,256.,1024.,8192.])
    ss=np.unique(np.r_[-8.,16.,base_mesh.s,np.log(radial_probe_values)])
    sw=np.empty(len(ss));sw[0]=(ss[1]-ss[0])/2;sw[-1]=(ss[-1]-ss[-2])/2
    sw[1:-1]=(ss[2:]-ss[:-2])/2
    z,tw=np.polynomial.legendre.leggauss(args.angular_order);angles=(z+1)*np.pi/4;tw*=np.pi/4
    s,t=np.meshgrid(ss,angles,indexing='ij')
    mesh=FrozenLogMesh(s.ravel(),t.ravel(),np.outer(sw,tw).ravel(),'derivative_switch_and_far_probe_finite_mesh')
    problem=AbsoluteLossProblem(candidate,mesh,args.a_ref,block_size=args.block_size)
    p,extra=problem.p,problem.extra
    r=problem.fun();full=problem.jacobian()
    rng=np.random.default_rng(120109)
    raw_directions=[]
    for i in range(24):
        v=np.zeros(problem.physical_columns);v[i]=1
        raw_directions.append(('core_'+str(i),v))
    indices=range(len(extra)) if args.full_coefficients else sorted(set([0,len(extra)//2,len(extra)-1])) if len(extra) else []
    for i in indices:
        v=np.zeros(problem.physical_columns);v[24+i]=1
        raw_directions.append(('extra_'+str(i),v))
    for i in range(4):
        v=rng.normal(size=problem.physical_columns);v/=np.linalg.norm(v)
        raw_directions.append(('all_physical_random_'+str(i),v))
    report={'schema':'absolute_loss_derivative_preparation_v1','label':args.label,
        'candidate_path':str(args.candidate.resolve()),'candidate_sha256':digest(args.candidate),
        'a_ref':args.a_ref,'a_ref_is_fixed_optimization_independent':True,
        'center_convention':'center_chart','mesh':mesh.record(),
        'finite_mesh_objective':float(r@r/2),'raw_physical_columns':problem.physical_columns,
        'extra_modes':len(extra),'analytic_cl_chain_includes':['transport','core_exponents','extra_exponents','all_spatial_field_derivatives','eliminated_center_c0','implicit_C5_correction'],
        'integration_error_control_claimed':False,'optimization_performed':False,
        'explicit_radial_probe_values':radial_probe_values.tolist(),
        'thresholds':{'raw_two_step_relative':3e-5,'feasible_two_step_relative':1e-3,
            'operator_relative':1e-10,'adjoint_scaled':1e-12,'C5_absolute':1e-10},
        'raw_checks':[],'feasible_checks':[],'operator_checks':[],
        'all_extra_coefficients_directly_FD_checked':bool(args.full_coefficients or len(extra)<=3),
        'source_sha256':{name:digest(ROOT/name) for name in ('absolute_model.py','absolute_chart.py','absolute_derivative_checks.py','absolute_fields.py','highprecision_origin.py')},
        'base_manifest_sha256':digest(ROOT/'provenance/base_manifest.json'),
        'resource_session':os.environ['IPM_RESOURCE_SESSION'],
        'resource_run':os.environ.get('IPM_RESOURCE_RUN'),'completed':False,'passed':False}
    output=directory/'checks.json';atomic(output,report)
    saved={'residual':r,'raw_jacobian':full,'s':mesh.s,'theta':mesh.theta,'weights':mesh.weights,'p':p,'extra':extra}
    for name,direction in raw_directions:
        analytic=full@direction
        amplitude=max(1.,abs(p[int(np.argmax(abs(direction[:24])))]) if name.startswith('core_') else 1.)
        steps=[2e-5*amplitude,1e-5*amplitude]
        rows=[]
        for h in steps:
            probes=[]
            for factor in (2,1,-1,-2):
                probes.append(problem.fun(p+factor*h*direction[:24],extra+factor*h*direction[24:]))
            fd=(-probes[0]+8*probes[1]-8*probes[2]+probes[3])/(12*h)
            rows.append({'step':h,'relative_error':norm_error(fd,analytic),
                'max_abs_error':float(np.max(abs(fd-analytic))),
                'analytic_norm':float(np.linalg.norm(analytic)),'FD_norm':float(np.linalg.norm(fd))})
            saved[name+'_fd_'+str(len(rows))]=fd
        report['raw_checks'].append({'direction':name,'input_sha256':array_hash(direction),'steps':rows,
            'passed':bool(all(x['relative_error']<3e-5 for x in rows))})
        atomic(output,report)

    try:
        chart=AbsoluteC5Chart(p)
        tangent=chart.base_tangent
        reduced=problem.feasible_jacobian(tangent)
        report['core_geometry']={'tangent_constraint_error':float(np.linalg.norm(constraint_jacobian(p)@tangent)),
            'complete_24_rank':int(np.linalg.matrix_rank(chart.complete)),
            'complete_24_condition':float(np.linalg.cond(chart.complete)),
            'all_19_core_directions_retained':True,'free_cl_tangent_norm':float(np.linalg.norm(tangent[0])),
            'base_independent_HP':hp_report(p)}
        saved['core_tangent']=tangent;saved['reduced_jacobian']=reduced
        core_dirs=[]
        for i in range(19):
            v=np.zeros(19+len(extra));v[i]=1
            core_dirs.append(('feasible_core_'+str(i),v))
        for i in range(4):
            v=rng.normal(size=19+len(extra))
            physical=np.r_[tangent@v[:19],v[19:]]
            v/=max(np.linalg.norm(physical),1e-300)
            core_dirs.append(('feasible_mixed_'+str(i),v))
        for name,direction in core_dirs:
            physical_length=np.linalg.norm(tangent@direction[:19])
            h1=min(5e-4,5e-4/max(physical_length,1e-300))
            rows=[]
            for h in (h1,h1/2):
                try:
                    probes=[];defects=[]
                    for factor in (2,1,-1,-2):
                        pp=chart.lift_delta(factor*h*direction[:19]);defects.append(hp_report(pp)['max_abs'])
                        probes.append(problem.fun(pp,extra+factor*h*direction[19:]))
                    fd=(-probes[0]+8*probes[1]-8*probes[2]+probes[3])/(12*h)
                    analytic=reduced@direction
                    rows.append({'step':h,'nominal_core_parameter_length':h*physical_length,
                        'relative_error':norm_error(fd,analytic),'max_abs_error':float(np.max(abs(fd-analytic))),
                        'maximum_HP_defect':max(defects),'completed':True})
                    saved[name+'_fd_'+str(len(rows))]=fd
                except (ValueError,np.linalg.LinAlgError) as exc:
                    rows.append({'step':h,'completed':False,'failure':str(exc)})
            report['feasible_checks'].append({'direction':name,'input_sha256':array_hash(direction),
                'steps':rows,'passed':bool(all(x.get('completed') and x['relative_error']<1e-3 and x['maximum_HP_defect']<1e-10 for x in rows))})
            atomic(output,report)
        operator=problem.operator(tangent)
        for i in range(3):
            v=rng.normal(size=reduced.shape[1]);v/=np.linalg.norm(v)
            w=rng.normal(size=reduced.shape[0]);w/=np.linalg.norm(w)
            jv=operator@v;jtw=operator.rmatvec(w)
            denom=np.linalg.norm(w)*np.linalg.norm(jv)+np.linalg.norm(v)*np.linalg.norm(jtw)
            row={'direction':i,'Jv_relative':norm_error(jv,reduced@v),
                'JT_relative':norm_error(jtw,reduced.T@w),
                'adjoint_scaled':float(abs(w@jv-v@jtw)/max(denom,1e-300))}
            row['passed']=bool(max(row['Jv_relative'],row['JT_relative'])<1e-10 and row['adjoint_scaled']<1e-12)
            report['operator_checks'].append(row)
        report['feasible_chart_completed']=True
    except (ValueError,np.linalg.LinAlgError) as exc:
        report['feasible_chart_completed']=False;report['feasible_chart_failure']=str(exc)
    artifact=directory/'arrays.npz'
    with artifact.open('wb') as stream:np.savez_compressed(stream,**saved)
    report.update(completed=True,arrays_path=str(artifact),arrays_sha256=digest(artifact),
        elapsed_seconds=time.time()-began,fun_calls=problem.fun_calls,jac_calls=problem.jac_calls)
    report['passed']=bool(all(x['passed'] for x in report['raw_checks']) and report.get('feasible_chart_completed')
        and len(report['feasible_checks'])==23 and all(x['passed'] for x in report['feasible_checks'])
        and len(report['operator_checks'])==3 and all(x['passed'] for x in report['operator_checks']))
    report['interpretation']='Preparation of residual/Jacobian on a fixed finite test mesh; this does not certify whole-axis integration or launch optimization.'
    atomic(output,report)
    print(json.dumps({'path':str(output),'passed':report['passed'],'elapsed_seconds':report['elapsed_seconds']}),flush=True)
    if not report['passed']:raise SystemExit(2)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate',required=True,type=Path)
    parser.add_argument('--label',required=True)
    parser.add_argument('--a-ref',required=True,type=float)
    parser.add_argument('--full-coefficients',action='store_true')
    parser.add_argument('--radial-panels',type=int,default=8)
    parser.add_argument('--radial-order',type=int,default=4)
    parser.add_argument('--angular-order',type=int,default=16)
    parser.add_argument('--block-size',type=int,default=256)
    args=parser.parse_args()
    if '/' in args.label or '\\' in args.label:parser.error('Simple label required')
    run(args)


if __name__=='__main__':main()
