"""Fresh read-only four-candidate residual assessment; no optimization.

Original stateless physical fields and independent whole-axis integration are
reused. Historical floor-based ratios are retained only as labeled comparison
columns; primary relative diagnostics use exact term sums and explicit axis
factorization. No candidate or historical source is written.
"""
import argparse
import csv
import json
import math
from pathlib import Path
import sys
import time

PROJECT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(PROJECT))
from absolute_common import ROOT,BASE,A_REF,np,read,atomic,digest,array_hash,provenance,sources,npz
from absolute_fields_v2 import prepare_candidate,fields,residual
from absolute_chart import hp_report
from highprecision_origin import field_series,residual_series,evaluate_series,origin_diagnostics,add,mul,D
from stage13_integration_v2 import independent_integral,physical_identity
from field_tests import independent_fields
from threadpoolctl import threadpool_limits

TARGETS=('E_f','E_rho','relative_Rf_exact','relative_Rrho_factored')
RADIAL_EDGES=[0.,1e-7,1e-5,1e-3,.02,.1,1.,10.,100.,1e3,1e4,1e6,1e8,1e12,1e16,1e20,float('inf')]

def max_record(values,x,y,region=None):
    valid=np.isfinite(values)
    if not np.any(valid):return {'value':None,'defined_points':0,'region':region}
    indices=np.flatnonzero(valid);i=int(indices[np.argmax(abs(values[valid]))])
    return {'value':float(abs(values[i])),'xy':[float(x[i]),float(y[i])],
        'radius':float(np.hypot(x[i],y[i])),'theta':float(np.arctan2(y[i],x[i])),
        'defined_points':int(np.count_nonzero(valid)),'region':region}

def ratio(numerator,denominator):
    out=np.full_like(numerator,np.nan)
    np.divide(numerator,denominator,out=out,where=denominator>0)
    return out

def values(model,x,y):
    x=np.asarray(x,float);y=np.asarray(y,float);r=np.hypot(x,y)
    ff=fields(model,x,y);rf=residual(model,x,y);cl=float(model['p'][0])
    wx=cl*x-ff['psiy'];wy=cl*y+ff['psix']
    nf=abs(wx*ff['fx'])+abs(wy*ff['fy'])+abs(ff['q']*ff['f'])
    rho=y*ff['f'];rhox=y*ff['fx'];rhoy=ff['f']+y*ff['fy']
    nr=abs(wx*rhox)+abs(wy*rhoy)+abs(rho)
    # N_rho=|y|*N_rho_factored exactly for the smooth symmetry class.
    nrf=abs(wx*ff['fx'])+abs((ff['q']+1)*(ff['f']+y*ff['fy']))+abs(ff['f'])
    a0=float(model['_assessment_a0'])
    # These are the *existing* historical floors, explicitly secondary only.
    old_floorf=1e-10*max(1.,abs(a0));old_floorr=1e-10*max(1.,float(max(abs(rho))))
    out={'E_f':abs(rf)/A_REF,
        'E_rho':abs(np.divide(y,r,out=np.zeros_like(y),where=r>0)*rf)/A_REF,
        'relative_Rf_exact':ratio(abs(rf),nf),
        'relative_Rrho_factored':ratio(abs(rf),nrf),
        'relative_Rrho_raw':ratio(abs(y*rf),nr),
        'legacy_relative_Rf':abs(rf)/np.maximum(nf,old_floorf),
        'legacy_relative_Rrho':abs(y*rf)/np.maximum(nr,old_floorr),
        'abs_Rrho':abs(y*rf),'abs_Rf':abs(rf)}
    return out,{'nf_zero':int(np.count_nonzero(nf==0)),
        'nrho_zero':int(np.count_nonzero(nr==0)),
        'nrho_factored_zero':int(np.count_nonzero(nrf==0)),
        'density_raw_axis_undefined':int(np.count_nonzero(y==0)),
        'legacy_floor_f':old_floorf,'legacy_floor_rho':old_floorr,
        'legacy_floor_hits_f':int(np.count_nonzero(nf<old_floorf)),
        'legacy_floor_hits_rho':int(np.count_nonzero(nr<old_floorr)),
        'direct_density_minus_yRf_max_abs':float(max(abs(wx*rhox+wy*rhoy-rho-y*rf))),
        'physical_vs_stable_Rf_max_abs':float(max(abs(wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']-rf)))}

def statistics(model,x,y,region):
    vv,diagnostics=values(model,x,y)
    return {'region':region,'points':len(x),'radius_min':float(min(np.hypot(x,y))),
        'radius_max':float(max(np.hypot(x,y))),
        'maxima':{k:max_record(v,x,y,region) for k,v in vv.items()},
        'diagnostics':diagnostics,'sampled_only':True,'continuous_supremum_certificate':False}

def frozen_grids():
    design=read(ROOT/'inputs/absolute_assessment_design.json')
    old=BASE/'inputs/assessment_grids_stage12.json';new=ROOT/'inputs/absolute_assessment_coordinates.npz'
    if digest(old)!=design['original_30_regions_sha256'] or digest(new)!=design['new_coordinate_file_sha256']:
        raise ValueError('Frozen 32-region coordinates changed')
    grids=read(old)
    with np.load(new,allow_pickle=False) as arrays:
        for name in design['regions']:grids[name]={'x':arrays[name+'_x'],'y':arrays[name+'_y']}
    if len(grids)!=32:raise ValueError('Expected exactly32 predetermined regions')
    return {name:(np.asarray(row['x']),np.asarray(row['y'])) for name,row in grids.items()}

def refine(model,seed,target):
    radius=float(seed['radius']);theta=float(seed['theta']);s=math.log(radius);rows=[]
    for level,(sw,tw,count) in enumerate(((.12,.04,25),(.03,.01,33),(.0075,.0025,49),(.001875,.000625,65))):
        ss=np.linspace(s-sw,s+sw,count);tt=np.unique(np.clip(np.linspace(theta-tw,theta+tw,count),0,np.pi/2))
        rr=np.exp(ss)[:,None];angles=tt[None,:]
        x=(rr*np.cos(angles)).ravel();y=(rr*np.sin(angles)).ravel()
        # Retain exact axes rather than floating cos(pi/2).
        x[np.tile(tt==np.pi/2,len(ss))]=0.;y[np.tile(tt==0,len(ss))]=0.
        vv,_=values(model,x,y);peak=max_record(vv[target],x,y,'local_refinement')
        rows.append({'level':level,'log_radius_half_width':sw,'angular_half_width':tw,
            'points':len(x),'peak':peak})
        s=math.log(peak['radius']);theta=peak['theta']
    return {'seed':seed,'target':target,'levels':rows,'sampled_only':True,'continuous_supremum_certificate':False}

def bands(model,x,y):
    r=np.hypot(x,y);vv,_=values(model,x,y);rows=[]
    for lo,hi in zip(RADIAL_EDGES[:-1],RADIAL_EDGES[1:]):
        use=(r>=lo)&(r<hi)
        if np.any(use):rows.append({'lo':lo,'hi':'infinity' if not math.isfinite(hi) else hi,
            'points':int(np.count_nonzero(use)),
            'maxima':{k:max_record(v[use],x[use],y[use],'radial_band') for k,v in vv.items()}})
    return rows

def origin_checks(model):
    ff=field_series(model,24)['fields'];rows=[]
    for radius in (.005,.01,.02):
        theta=np.linspace(0,np.pi/2,33);x=radius*np.cos(theta);y=radius*np.sin(theta)
        x[-1]=0.;y[0]=0.
        p20=residual_series(model,20)['residual'];p24=residual_series(model,24)['residual']
        a=evaluate_series(p20,x,y);b=evaluate_series(p24,x,y)
        tx=radius*math.cos(7*math.pi/32);ty=radius*math.sin(7*math.pi/32)
        ref=independent_fields(model,tx,ty,85)['Rf']
        value=float(evaluate_series(p24,tx,ty));tol=1e-18+1e-7*abs(ref)
        rows.append({'radius':radius,'order20_vs24_max_abs':float(max(abs(a-b))),
            'independent85digit_xy':[tx,ty],'independent85digit_Rf':ref,'order24_Rf':value,
            'difference_abs':abs(value-ref),'tolerance_abs':tol,'passed':abs(value-ref)<=tol})
    poly=residual_series(model,24)['residual']
    cl=D.from_float(float(model['p'][0]));wx=add({(1,0):cl},ff['psiy'],D(-1),24);wy=add({(0,1):cl},ff['psix'],order=24)
    terms=[mul(wx,ff['fx'],24),mul(wy,ff['fy'],24),mul(ff['q'],ff['f'],24)]
    directional=[]
    for angle in np.linspace(0,np.pi/2,17):
        xx=float(math.cos(angle));yy=float(math.sin(angle))
        if angle==np.pi/2:xx=0.
        if angle==0:yy=0.
        denominator=[];numerator=[]
        for degree in range(0,25,2):
            numerator.append(float(evaluate_series({k:v for k,v in poly.items() if sum(k)==degree},xx,yy)))
            denominator.append(sum(abs(float(evaluate_series({k:v for k,v in term.items() if sum(k)==degree},xx,yy))) for term in terms))
        nd=next((2*i for i,v in enumerate(numerator) if v!=0),None);dd=next((2*i for i,v in enumerate(denominator) if v!=0),None)
        limit=None if dd is None or (nd is not None and nd<dd) else (0. if nd is None or nd>dd else abs(numerator[nd//2])/denominator[dd//2])
        directional.append({'theta':float(angle),'Rf_leading_degree':nd,'Nf_leading_degree':dd,'relative_Rf_directional_limit':limit,
            'Rf_degree2_coefficient':numerator[1],'Nf_degree2_coefficient':denominator[1]})
    return {'origin_exact_center_defect_decimal':'0 by analytic center elimination',
        'literal_serialized_center_defect_decimal':model['center_metadata']['literal_center_defect'],
        'analytic_c0_decimal':model['center_metadata']['analytic_c0'],
        'a0':model['_assessment_a0'],'strain_plus_cl_minus1':float(ff['q'].get((0,0),0)),
        'residual_coefficients_through_degree8':{f'{i},{j}':str(v) for (i,j),v in sorted(poly.items()) if i+j<=8},
        'residual_degree_l1':residual_series(model,24)['degree_l1_coefficients'],
        'even_x_even_y_Rf_parity':all(i%2==0 and j%2==0 for i,j in poly),
        'origin_quadrature_orders20_24':origin_diagnostics(model,.02,A_REF,(20,24)),
        'overlap_checks':rows,'passed':all(z['passed'] for z in rows),
        'quotient_relative_at_origin':'0/0 undefined; directional limits below retain the actual nonzero numerical quadratic constraint defects',
        'relative_Rf_directional_origin_limits':directional,
        'density_ratio_axis_extension':'|Rf|/[|wx fx|+|(q+1)(f+y fy)|+|f|]; raw Rrho/Nrho undefined on y=0',
        'rigorous_remainder_bound':False}

def do_candidate(label,path,out,latest=False):
    began=time.time();out.mkdir(parents=True,exist_ok=False);case=read(path)
    model=prepare_candidate(case,'center_chart');p=model['p'];extra=model['extra']
    model['_assessment_a0']=float(fields(model,[0.],[0.])['f'][0])
    record={'schema':'stage13_v3_independent_residual_assessment_v1','label':label,
        'candidate_path':str(path.resolve()),'candidate_sha256':digest(path),
        'physical_identity':physical_identity(case,p,extra),'cl':float(p[0]),'a0':model['_assessment_a0'],
        'a_ref':A_REF,'center_metadata':model['metadata'],'HP_Taylor':hp_report(p),
        'environment':provenance(),'source_identity':sources(),'assessment_worker_sha256':digest(Path(__file__)),
        'frozen32_regions':{},'additional_regions':{},'refinements':{},'completed':False,
        'optimization_performed':False,'coefficients_modified':False,
        'relative_primary_denominator_floor':None,
        'definitions':{'E_f':'abs(Rf)/fixed a_ref','E_rho':'abs(Rrho)/(r*fixed a_ref), continuous0 atorigin',
            'relative_Rf_exact':'abs(Rf)/(|wx fx|+|wy fy|+|q f|), denominator0 meansundefined',
            'relative_Rrho_factored':'abs(Rf)/(|wx fx|+|(q+1)(f+y fy)|+|f|), axis extension of abs(Rrho)/Nrho',
            'legacy_relative_columns':'Historical existing floored values for comparison only; never primary or optimization quantities'},
        'continuous_supremum_certificate':False}
    destination=out/'assessment.json';atomic(destination,record)
    grids=frozen_grids();allx=[];ally=[]
    for name,(x,y) in grids.items():
        record['frozen32_regions'][name]=statistics(model,x,y,name);allx.append(x);ally.append(y);atomic(destination,record)
    record['frozen32_maxima']={target:max((row['maxima'][target] for row in record['frozen32_regions'].values()),key=lambda z:-1 if z['value'] is None else z['value']) for target in TARGETS+('legacy_relative_Rf','legacy_relative_Rrho','abs_Rrho')}
    radii=np.geomspace(1e-12,1e20,129);xx=np.r_[radii,np.zeros_like(radii),0.];yy=np.r_[np.zeros_like(radii),radii,0.]
    record['additional_regions']['exact_axes_origin']=statistics(model,xx,yy,'exact_axes_origin')
    record['origin']=origin_checks(model);atomic(destination,record)
    # Same additional resolution levels for every candidate, fixed before evaluation.
    for level,(nr,nt) in enumerate(((769,199),(1537,397))):
        rr=np.geomspace(.02,1e12,nr)[:,None];angles=np.linspace(0,np.pi/2,nt)
        x=(rr*np.cos(angles)).ravel();y=(rr*np.sin(angles)).ravel();x[np.tile(angles==np.pi/2,nr)]=0.;y[np.tile(angles==0,nr)]=0.
        name='independent_resolution_level'+str(level)
        record['additional_regions'][name]=statistics(model,x,y,name)
        record['additional_regions'][name]['design']={'radial_count':nr,'angular_count':nt,'rmin':.02,'rmax':1e12,'x_sha256':array_hash(x),'y_sha256':array_hash(y)}
        atomic(destination,record)
    # Remote radial bands with near-axis probes, independent of the training rule.
    rr=np.geomspace(1e8,1e20,121)[:,None]
    tt=np.unique(np.r_[np.linspace(0,np.pi/2,257),np.geomspace(1e-12,.01,33),np.pi/2-np.geomspace(1e-12,.01,33)])
    x=(rr*np.cos(tt)).ravel();y=(rr*np.sin(tt)).ravel();x[np.tile(tt==np.pi/2,121)]=0.;y[np.tile(tt==0,121)]=0.
    record['additional_regions']['distant_1e8_to1e20']=statistics(model,x,y,'distant_1e8_to1e20')
    record['distant_radial_bands']=bands(model,x,y)
    for target in TARGETS:
        seeds=[row['maxima'][target] for row in list(record['frozen32_regions'].values())+list(record['additional_regions'].values())]
        seeds.sort(key=lambda z:-1 if z['value'] is None else z['value'],reverse=True)
        selected=[];seen=set()
        for seed in seeds:
            if seed['value'] is None or seed.get('radius',0)<=0:continue
            key=(round(math.log(seed['radius']),1),round(seed['theta'],1))
            if key not in seen:seen.add(key);selected.append(seed)
            if len(selected)==4:break
        record['refinements'][target]=[refine(model,seed,target) for seed in selected]
        atomic(destination,record)
    record['frozen32_radial_bands']=bands(model,np.concatenate(allx),np.concatenate(ally))
    record['fresh_independent_integral']=independent_integral(case,p,extra,workers=1,target_abs=1e-16)
    atomic(destination,record)
    if latest:
        record['tight_independent_integral']=independent_integral(case,p,extra,workers=1,target_abs=1e-18)
        # Rebind only the source provider in this process; no source file changes.
        import stage12_assess as green
        original=green.total_fields_saved
        try:
            green.total_fields_saved=lambda saved,x,y:fields(model,x,y)
            record['canonical_inverse']=green.inverse(case)
            record['canonical_inverse']['provider']='stateless unrounded analytic-center fields_v2; processlocal binding only'
            record['canonical_inverse']['source_sha256']=digest(BASE/'stage12_assess.py')
        finally:green.total_fields_saved=original
        checks=[]
        for target in ('E_f','E_rho'):
            peak=max((z['levels'][-1]['peak'] for z in record['refinements'][target]),key=lambda z:z['value'])
            x,y=peak['xy'];ref=independent_fields(model,x,y,85)['Rf'];got=float(residual(model,[x],[y])[0])
            tolerance=1e-12+1e-7*abs(ref)
            checks.append({'target':target,'xy':[x,y],'stateless_Rf':got,'independent85digit_Rf':ref,'difference_abs':abs(got-ref),'tolerance_abs':tolerance,'passed':abs(got-ref)<=tolerance})
        record['peak_independent85digit_checks']=checks
    record['refined_maxima']={target:max((z['levels'][-1]['peak'] for z in record['refinements'][target]),key=lambda z:z['value']) for target in TARGETS}
    record['completed']=True;record['seconds']=time.time()-began
    record['passed']=bool(record['HP_Taylor']['max_abs']<1e-10 and record['HP_Taylor']['physical_bounds'] and record['origin']['passed'] and record['fresh_independent_integral']['accuracy_passed'] and record.get('tight_independent_integral',{}).get('accuracy_passed',True) and record.get('canonical_inverse',{}).get('passed',True) and all(z['passed'] for z in record.get('peak_independent85digit_checks',[])))
    atomic(destination,record)
    with (out/'regions.csv').open('w') as stream:
        writer=csv.writer(stream);writer.writerow(['region','points']+list(TARGETS)+['legacy_Rf','legacy_Rrho'])
        for name,row in record['frozen32_regions'].items():writer.writerow([name,row['points']]+[row['maxima'][k]['value'] for k in TARGETS+('legacy_relative_Rf','legacy_relative_Rrho')])
    print(json.dumps({'label':label,'passed':record['passed'],'seconds':record['seconds'],'J_abs':record['fresh_independent_integral']['J_abs'],'frozen32_maxima':record['frozen32_maxima'],'refined_maxima':record['refined_maxima']}),flush=True)
    return record

def main(args):
    output=args.output.resolve()
    if output.exists():raise ValueError('Fresh output directory required')
    output.mkdir(parents=True)
    candidates=[('stage11',ROOT/'inputs/stage11.json'),('stage12_global',ROOT/'inputs/global.json'),
        ('stage13_v1',ROOT/'campaign/global181/snapshots/accepted_00000006.json'),
        ('stage13_v3_accepted278',ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json')]
    selected=[row for row in candidates if not args.labels or row[0] in args.labels]
    summary={'schema':'stage13_fresh_four_candidate_comparison_v1','completed':False,'candidates':{}}
    for label,path in selected:
        record=do_candidate(label,path,output/label,label.startswith('stage13_v3'))
        summary['candidates'][label]={'path':str(output/label/'assessment.json'),'sha256':digest(output/label/'assessment.json'),
            'candidate_path':str(path),'candidate_sha256':digest(path),'passed':record['passed']}
        atomic(output/'summary.json',summary)
    summary['completed']=True;summary['passed']=all(z['passed'] for z in summary['candidates'].values());atomic(output/'summary.json',summary)
    if not summary['passed']:raise SystemExit(2)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--labels',nargs='*')
    with threadpool_limits(limits=1,user_api='blas'):main(parser.parse_args())
