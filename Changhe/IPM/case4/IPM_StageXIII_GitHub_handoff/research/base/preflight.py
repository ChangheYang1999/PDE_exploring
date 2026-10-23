#!/usr/bin/env python3
"""Reproduce the C5 start and verify the complete new chart before fitting."""
import argparse
import time
from stage11_common import *
from c5_chart import build_record

def setup():
    source=reference('c5start');p=parameters(source);ev=Evaluator('preflight_setup');prob=ev.prob
    saved_coeff=np.array(source['coefficients']);native_coeff=prob.coefficients(p)
    assert np.array_equal(native_coeff[1:],saved_coeff[1:])
    center_difference=float(native_coeff[0]-saved_coeff[0])
    assert abs(center_difference)<1e-14,'native center reconstruction differs beyond architecture-scale rounding'
    # The exact saved physical vector is independently reproduced before using
    # the unchanged native center-elimination algorithm for the24 independent p.
    import repro_helpers
    direct=repro_helpers.objectives(e.a,source,read(ROOT/'engine/reference_results/fitting_grids.json')['97'],97)
    assert abs(direct['J_joint']-1.7229166237494318e-6)<1e-13
    r=ev.fun(p);obj=prob.objectives();expected=1.7229166237494318e-6
    assert abs(obj['J_joint']-expected)<1e-13+1e-6*expected
    hp=hp_report(p);assert hp['max_abs']<1e-10 and hp['center_abs']<1e-10
    record=build_record(p,prob);chart=C5Chart(record);lift,T=chart.lift(np.zeros(19),True)
    assert np.array_equal(lift,p)
    C,G=constraints(p,True);sraw=np.linalg.svd(G,compute_uv=False)
    derivative=[]
    for step in (.0002,.0001):
        columns=[]
        for i in range(24):
            h=step*max(1.,abs(p[i]));v=[]
            for k in (2,1,-1,-2):
                q=p.copy();q[i]+=k*h;v.append(hp_values(q))
            columns.append((-v[0]+8*v[1]-8*v[2]+v[3])/(12*h))
        fd=np.array(columns).T
        derivative.append({'relative_step':step,'relative_Frobenius_error':float(np.linalg.norm(fd-G)/np.linalg.norm(G)),
                           'row_relative_errors':(np.linalg.norm(fd-G,axis=1)/np.linalg.norm(G,axis=1)).tolist(),'max_absolute_error':float(np.max(abs(fd-G)))})
    assert max(x['relative_Frobenius_error'] for x in derivative)<1e-5
    J=ev.jac(p);field,B,mr,ff,D,sb=full_tangent(prob,p,T)
    U,sv,Vt=np.linalg.svd(J@field,full_matrices=False)
    assert len(sv)==19 and min(sv)>0
    _,_,vb=np.linalg.svd(B@T,full_matrices=False)
    map19=(vb.T/sb)@(Vt.T/sv)
    assert np.linalg.norm(T@map19-field@(Vt.T/sv))<1e-8*np.linalg.norm(T@map19)
    if (OUT/'chart.json').exists():raise RuntimeError('frozen chart already exists; do not rebuild it')
    atomic(OUT/'chart.json',record)
    atomic(OUT/'fit_map.json',{'anchor_reduced':[0.]*19,'right_map19x19':map19.tolist(),'fixed':True,
        'source_chart_sha256':digest(OUT/'chart.json'),'all_directions_retained':True,'initial_residual_singular_values':sv.tolist()})
    npz(OUT/'preflight_arrays.npz',p=p,r=r,J=J,T=T,field=field,Z=field@(Vt.T/sv),JZ=J@(field@(Vt.T/sv)),B=B)
    atomic(OUT/'preflight_setup.json',{'passed':True,'objective':obj,'expected_J97':expected,'high_precision':hp,
        'independent24_parameter_vector_bitwise_preserved':True,'saved_full_coefficient_vector_reproduced_directly':True,
        'center_reconstruction_difference':center_difference,'exact_saved_vector_objective':direct,
        'native_center_matches_saved_bitwise':bool(np.array_equal(native_coeff,saved_coeff)),
        'full_constraint_raw_singular_values':sraw.tolist(),
        'constraint_Jacobian_FD_checks':derivative,'constraint_tangent_max_abs':float(np.max(abs(G@T))),
        'field_singular_values':sv.tolist(),'field_condition':float(sv[0]/sv[-1]),
        'hybrid_relative':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
        'whitening_error':float(np.linalg.norm((J@T@map19).T@(J@T@map19)-np.eye(19))),
        'chart':{'C2_pair_condition':record['c2_pair_condition'],'C4_normal_condition':record['normal_condition'],
                 'full_constraint_field_singular_values':record['full_constraint_field_singular_values']},'provenance':provenance()})
    atomic(OUT/'c5start.json',source)
    print({'setup_passed':True,'J97':obj['J_joint'],'hybrid_relative':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),'field_condition':sv[0]/sv[-1]},flush=True)

def directions(start,stop):
    chart=C5Chart(read(OUT/'chart.json'));ev=Evaluator('preflight_directions')
    data=np.load(OUT/'preflight_arrays.npz');p=data['p'];r=data['r'];Z=data['Z'];JZ=data['JZ']
    identity=derivative_identity()
    for i in range(start,min(stop,19)):
        path=OUT/('preflight_direction_'+str(i).zfill(2)+'.json')
        if path.exists():
            old=read(path)
            if old.get('identity')!=identity:raise ValueError('existing preflight derivative provenance differs; preserve and review rather than skip')
            continue
        direction=Z[:,i];dq=np.linalg.solve(np.array(read(OUT/'chart.json')['complete_map22x22']),direction[chart.free22])[:19]
        rows=[]
        for physical in (.004,.002):
            h=physical/np.linalg.norm(direction);vv=[];ratios=[];defects=[]
            for k in (2,1,-1,-2):
                pp=chart.lift(k*h*dq);vv.append(ev.fun(pp,'feasible_FD'))
                ratios.append(float(np.linalg.norm(pp-p)/(abs(k)*physical)));defects.append(hp_report(pp)['max_abs'])
            fd=(-vv[0]+8*vv[1]-8*vv[2]+vv[3])/(12*h)
            rows.append({'physical_step':physical,'coordinate_step':float(h),'relative_J_error':float(np.linalg.norm(fd-JZ[:,i])/np.linalg.norm(JZ[:,i])),
                         'FD_gradient':float(fd@r),'FD_gradient_over_rnorm':float(fd@r/np.linalg.norm(r)),
                         'actual_to_linear_step_ratios':ratios,'max_high_precision_defect':max(defects)})
        atomic(path,{'direction':i,'rows':rows,'identity':identity,'provenance':provenance()})
        print({'direction':i,'relative_J_errors':[x['relative_J_error'] for x in rows]},flush=True)

def finish():
    rows=[read(OUT/('preflight_direction_'+str(i).zfill(2)+'.json')) for i in range(19)]
    identity=derivative_identity()
    for i,row in enumerate(rows):
        assert row['direction']==i and row['identity']==identity
        assert [r['physical_step'] for r in row['rows']]==[.004,.002]
        assert all(np.isfinite(r['relative_J_error']) and np.isfinite(r['FD_gradient']) for r in row['rows'])
    maxerror=max(x['relative_J_error'] for d in rows for x in d['rows'])
    maxhp=max(x['max_high_precision_defect'] for d in rows for x in d['rows'])
    fd=np.array([[x['FD_gradient_over_rnorm'] for x in d['rows']] for d in rows])
    result={'passed':maxerror<1e-4 and maxhp<1e-10,'complete_directions':19,'physical_steps':[.004,.002],
            'maximum_reduced_Jacobian_relative_error':maxerror,'maximum_HP_feasibility_defect':maxhp,'FD_relative':np.linalg.norm(fd,axis=0).tolist(),
            'hybrid_relative':read(OUT/'preflight_setup.json')['hybrid_relative'],'identity':identity,
            'explanation':'Derivative accuracy threshold1e-4 reflects historical rounded-exponent FD noise; stationarity threshold remains unchanged1e-5.'}
    atomic(OUT/'preflight_complete.json',result)
    print(result,flush=True)
    if not result['passed']:raise SystemExit(1)

if __name__=='__main__':
    from threadpoolctl import threadpool_limits
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['setup','directions','finish']);parser.add_argument('--start',type=int,default=0);parser.add_argument('--stop',type=int,default=19);args=parser.parse_args()
    with threadpool_limits(limits=1):
        if args.mode=='setup':setup()
        elif args.mode=='directions':directions(args.start,args.stop)
        else:finish()
