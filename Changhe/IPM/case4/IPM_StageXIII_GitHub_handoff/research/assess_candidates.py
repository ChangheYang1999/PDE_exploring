"""Absolute-primary and separate historical-relative sampled assessments."""
import argparse
import csv
import math
from absolute_common import *
from absolute_fields import prepare_candidate,fields,residual,exact_dilation_fields


def freeze():
    path=ROOT/'inputs/absolute_assessment_design.json'
    if path.exists():raise ValueError('Assessment coordinates are immutable')
    # Existing 30 frozen regions retain their original independent coordinates.
    old=BASE/'inputs/assessment_grids_stage12.json'
    theta=np.unique(np.r_[np.linspace(0,np.pi/2,193),1e-12,1e-8,1e-4,np.pi/2-1e-4,np.pi/2-1e-8,np.pi/2-1e-12])
    specs={'absolute_dense_log_radius':np.exp(np.linspace(math.log(.02),math.log(1e8),769)),
           'absolute_unseen_large_radius':np.geomspace(512,1e12,129)}
    arrays={};rows={}
    for name,rs in specs.items():
        x=(rs[:,None]*np.cos(theta)).ravel();y=(rs[:,None]*np.sin(theta)).ravel()
        arrays[name+'_x']=x;arrays[name+'_y']=y
        rows[name]={'points':len(x),'r_min':float(min(rs)),'r_max':float(max(rs)),
                    'radial_count':len(rs),'angular_count':len(theta),
                    'coordinates_sha256':array_hash(np.column_stack([x,y]))}
    npz(ROOT/'inputs/absolute_assessment_coordinates.npz',**arrays)
    atomic(path,{'schema':'absolute-primary-independent-assessment-design-v1',
       'created_before_any_new_assessment_values':True,'a_ref':A_REF,'regions':rows,
       'original_30_regions':str(old),'original_30_regions_sha256':digest(old),
       'new_coordinate_file_sha256':digest(ROOT/'inputs/absolute_assessment_coordinates.npz'),
       'selection':'Fixed log-radius and angular grids; no optimization or fitting use.',
       'continuous_supremum_bound_claimed':False})
    print('Frozen original 30 plus two additional absolute-assessment grids.')


def statistics(model,x,y,dilation=1.):
    r=np.hypot(x,y);ff=exact_dilation_fields(model,x,y,dilation);rf=residual(model,x/dilation,y/dilation)
    cl=float(model['p'][0]);wx=cl*x-ff['psiy'];wy=cl*y+ff['psix']
    rho=y*ff['f'];rhox=y*ff['fx'];rhoy=ff['f']+y*ff['fy']
    direct=wx*rhox+wy*rhoy-rho
    density_over_r=np.divide(y,r,out=np.zeros_like(y),where=r>0)*rf
    nf=abs(wx*ff['fx'])+abs(wy*ff['fy'])+abs(ff['q']*ff['f'])
    nr=abs(wx*rhox)+abs(wy*rhoy)+abs(rho)
    a0=float(fields(model,np.array([0.]),np.array([0.]))['f'][0])
    floorf=1e-10*max(1.,abs(a0));floorr=1e-10*max(1.,float(max(abs(rho))))
    relf=abs(rf)/np.maximum(nf,floorf);relr=abs(y*rf)/np.maximum(nr,floorr)
    def maximum(values):
        i=int(np.argmax(abs(values)))
        return {'value':float(abs(values[i])),'xy':[float(x[i]),float(y[i])],
                'radius':float(r[i]),'theta':float(math.atan2(y[i],x[i]))}
    return {'points':len(x),'radius_min':float(min(r)),'radius_max':float(max(r)),
       'a_ref':A_REF,'candidate_a0_for_secondary_floor_only':a0,
       'max_abs_Rf':maximum(rf),'max_abs_Rf_over_a_ref':maximum(rf/A_REF),
       'max_abs_Rrho_over_r_over_a_ref':maximum(density_over_r/A_REF),
       'rms_abs_Rf':float(np.sqrt(np.mean(rf*rf))),
       'rms_Rrho_over_r':float(np.sqrt(np.mean(density_over_r*density_over_r))),
       'relative_Rf_fraction':maximum(relf),'relative_Rrho_fraction':maximum(relr),
       'relative_floor_f':floorf,'relative_floor_rho':floorr,
       'floor_hits_f':int(np.sum(nf<floorf)),'floor_hits_rho':int(np.sum(nr<floorr)),
       'direct_density_minus_y_Rf_max_abs':float(max(abs(direct-y*rf))),
       'density_primary_formula':'Rrho/r=(y/r)*Rf by analytic identity, continuous value zero at r=0',
       'sampled_maxima_only':True,'continuous_supremum_certificate':False}


def evaluate(a):
    label=a.label or a.case
    if any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in label):raise ValueError('unsafe label')
    if not math.isfinite(a.dilation) or a.dilation<=0:raise ValueError('positive exact dilation required')
    output=OUT/'assessments'/(label+'.json')
    if output.exists():raise ValueError('Refusing to overwrite saved assessment')
    design=read(ROOT/'inputs/absolute_assessment_design.json')
    assert digest(BASE/'inputs/assessment_grids_stage12.json')==design['original_30_regions_sha256']
    assert digest(ROOT/'inputs/absolute_assessment_coordinates.npz')==design['new_coordinate_file_sha256']
    coords=read(BASE/'inputs/assessment_grids_stage12.json')
    with np.load(ROOT/'inputs/absolute_assessment_coordinates.npz') as data:
        for name in design['regions']:coords[name]={'x':data[name+'_x'].tolist(),'y':data[name+'_y'].tolist()}
    case=load_case(a.case);model=prepare_candidate(case,'center_chart');rows={}
    record={'case':a.case,'label':label,'exact_spatial_dilation':a.dilation,'candidate_sha256':digest(ROOT/'inputs'/(a.case+'.json')),
       'a_ref':A_REF,'center_convention':'center_chart','design_sha256':digest(ROOT/'inputs/absolute_assessment_design.json'),
       'completed':False,'regions':rows,'source_identity':sources(),'native_environment':provenance()}
    for name,xy in coords.items():
        x,y=np.asarray(xy['x']),np.asarray(xy['y']);rows[name]=statistics(model,x,y,a.dilation)
        atomic(output,record)
    record['completed']=True
    record['dense_sampled_E_infinity']=max((v['max_abs_Rf_over_a_ref'] for v in rows.values()),key=lambda x:x['value'])
    record['dense_sampled_density_E_infinity']=max((v['max_abs_Rrho_over_r_over_a_ref'] for v in rows.values()),key=lambda x:x['value'])
    atomic(output,record)
    with output.with_suffix('.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['region','points','Rf_absolute_max','Rf_over_a_ref_max','Rrho_over_r_a_ref_max','relative_Rf_percent','relative_Rrho_percent','Rf_max_x','Rf_max_y'])
        for name,v in rows.items():w.writerow([name,v['points'],v['max_abs_Rf']['value'],v['max_abs_Rf_over_a_ref']['value'],v['max_abs_Rrho_over_r_over_a_ref']['value'],100*v['relative_Rf_fraction']['value'],100*v['relative_Rrho_fraction']['value'],*v['max_abs_Rf']['xy']])
    print(json.dumps({'case':a.case,'completed':True,'sampled_E_infinity':record['dense_sampled_E_infinity'],'sampled_density_E_infinity':record['dense_sampled_density_E_infinity']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['freeze','evaluate']);p.add_argument('--case',choices=['stage11','combined','local','global']);p.add_argument('--label');p.add_argument('--dilation',type=float,default=1.);a=p.parse_args()
    from threadpoolctl import threadpool_limits
    with threadpool_limits(limits=1):freeze() if a.mode=='freeze' else evaluate(a)
