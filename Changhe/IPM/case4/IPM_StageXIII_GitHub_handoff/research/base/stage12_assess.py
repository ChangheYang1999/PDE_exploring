#!/usr/bin/env python3
"""Frozen holdouts and independent full-plane source Green verification.

Run through launch.py. No optimizer, constraint retraction or candidate writer is
called. Saved physical coefficients are used directly, including saved c0.
"""
import argparse
import csv
import hashlib
import io
import json
import math
import os
from pathlib import Path
import struct
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Independent Stage XII assessment requires the resource supervisor')
from stage12_common import np, atomic, read, digest, provenance
from stage12_model import total_fields_saved
import repro_helpers as repro
import taylor_jet as jet

OUT = ROOT/'results/assessment'
OLD = ROOT/'engine/reference_results/assessment_grids.json'
COORDS = ROOT/'inputs/assessment_grids_stage12.json'
DESIGN = ROOT/'inputs/assessment_design_stage12.json'


def assessment_source_identity():
    names=['spectral_basis.py','stage12_model.py','stage12_common.py','stage12_assess.py',
           'repro_helpers.py','c5_chart.py','coefficient_normal_chart.py','continuation_chart.py',
           'stage11_common.py']
    paths=[ROOT/name for name in names]+sorted((ROOT/'engine').glob('*.py'))
    return {str(path.relative_to(ROOT)):digest(path) for path in paths}


def coord_hash(x, y):
    return hashlib.sha256(np.column_stack((x,y)).astype('<f8').tobytes()).hexdigest()


def vector_hash(case):
    packed = struct.pack('<25d', float(case['cl']), *case['coefficients'])
    extra = np.asarray(case.get('extra_coefficients', []), dtype='<f8').tobytes()
    modes = json.dumps(case.get('modes', []), sort_keys=True, separators=(',',':')).encode()
    return hashlib.sha256(packed+extra+modes).hexdigest()


def polar(rs, theta):
    rr, tt = np.meshgrid(np.asarray(rs), np.asarray(theta), indexing='ij')
    x, y = rr*np.cos(tt), rr*np.sin(tt)
    x[np.broadcast_to(np.asarray(theta)==np.pi/2,x.shape)] = 0.
    y[np.broadcast_to(np.asarray(theta)==0.,y.shape)] = 0.
    return {'x':x.ravel().tolist(), 'y':y.ravel().tolist()}


def freeze():
    """Predeclare all holdouts; no profile or residual influences coordinates."""
    old = read(OLD)
    rows = dict(old)
    n = 193
    th = (np.arange(n)+.419)*np.pi/(2*n)
    for name,lo,hi,shift in [('hires_shifted_inner193',.08,8.,.381),
                             ('hires_shifted_far193',8.,64.,.619),
                             ('hires_exterior193',64.,512.,.273)]:
        rr = np.exp(math.log(lo)+(np.arange(n)+shift)/n*math.log(hi/lo))
        rows[name] = polar(rr, th)
    rr = np.exp(math.log(512.)+(np.arange(97)+.287)/97*math.log(16.))
    rows['unseen_beyond512_to8192'] = polar(rr,(np.arange(129)+.537)*np.pi/(2*129))
    rows['far_growth_rings512_to16384'] = polar([512.,1024.,2048.,4096.,8192.,16384.],
                                               np.linspace(0.,np.pi/2,129))
    design = {'schema':'stage12-predetermined-assessment-design-v1',
              'created_epoch':time.time(), 'historical_grids_sha256':digest(OLD),
              'historical_regions':list(old), 'all_regions':list(rows),
              'selection':'Fixed coordinate formulas declared before enriched optimization; no candidate residual used.',
              'new_coordinates_used_for_fitting':False,
              'historical_overlap_note':'Historical inner/far and historical_H grids retain their original fitting overlaps; true_H, shifted and new sets are assessment only.',
              'sampled_maxima_only':True, 'regions':{}}
    for name,row in rows.items():
        rr=np.hypot(row['x'],row['y'])
        design['regions'][name]={'points':len(rr),'coordinate_sha256':coord_hash(row['x'],row['y']),
                                  'radius_min':float(rr.min()),'radius_max':float(rr.max()),
                                  'historical_frozen':name in old}
    # Existing frozen coordinates are immutable. A rerun verifies, never updates.
    if COORDS.exists() or DESIGN.exists():
        saved=read(COORDS); known=read(DESIGN)
        if set(saved)!=set(rows) or any(coord_hash(saved[k]['x'],saved[k]['y'])!=design['regions'][k]['coordinate_sha256'] for k in rows):
            raise ValueError('Existing fixed assessment design differs')
        if known['historical_grids_sha256']!=digest(OLD): raise ValueError('Historical grid changed')
    else:
        atomic(COORDS,rows); atomic(DESIGN,design)
        COORDS.chmod(0o444); DESIGN.chmod(0o444)
    print(json.dumps({'coordinates':str(COORDS),'sha256':digest(COORDS),
                      'design_sha256':digest(DESIGN),'regions':len(rows)}),flush=True)


def physical_values(case,x,y):
    x,y=np.asarray(x),np.asarray(y)
    ff=total_fields_saved(case,x,y)
    wx,wy=case['cl']*x-ff['psiy'],case['cl']*y+ff['psix']
    t1,t2,t3=wx*ff['fx'],wy*ff['fy'],(case['cl']-1+ff['ratio'])*ff['f']
    rho=y*ff['f']; rx=y*ff['fx']; ry=ff['f']+y*ff['fy']
    r1,r2,r3=wx*rx,wy*ry,-rho
    ff.update(Rf=t1+t2+t3,Rrho=r1+r2+r3,nf=abs(t1)+abs(t2)+abs(t3),
              nr=abs(r1)+abs(r2)+abs(r3),rho=rho)
    w=(1+x*x+y*y)**((1/case['cl']-1)/2)
    ff['physical_fit']=ff['Rf']/np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*w)**2)
    return ff


def weights(x,y):
    r=np.hypot(x,y); edges=np.r_[0,np.flatnonzero(abs(np.diff(r))>1e-12*np.maximum(1,r[:-1]))+1,len(r)]
    lens=np.diff(edges)
    if len(lens)<2 or not np.all(lens==lens[0]) or lens[0]<2:return None
    nr,nt=len(lens),int(lens[0]); rr=r.reshape(nr,nt)[:,0]
    tt=np.arctan2(y,x).reshape(nr,nt)[-1]
    if not np.all(np.diff(rr)>0) or not np.all(np.diff(tt)>0):return None
    wr=np.r_[0.,repro.trap(np,np.log(rr[1:]))] if rr[0]==0 else repro.trap(np,np.log(rr))
    return np.outer(wr,repro.trap(np,tt)).ravel()


def diagnostic(case,row,a0,region_name=None):
    x,y=np.asarray(row['x']),np.asarray(row['y']);v=physical_values(case,x,y)
    ef=1e-10*max(1.,abs(a0)); er=1e-10*max(1.,float(np.max(abs(v['rho']))))
    qf=abs(v['Rf'])/np.maximum(v['nf'],ef);qr=abs(v['Rrho'])/np.maximum(v['nr'],er)
    ww=weights(x,y)
    out={'points':len(x),'coordinate_sha256':coord_hash(x,y),'epsilon_f':ef,'epsilon_rho':er,
         'floor_hits_f':int(np.sum(v['nf']<=ef)),'floor_hits_rho':int(np.sum(v['nr']<=er)),
         'Rrho_vs_y_Rf_max_abs':float(np.max(abs(v['Rrho']-y*v['Rf']))),
         'sampled_maxima_only':True,'RMS_convention':'unweighted over every saved node; normalized log-polar weighted RMS separately',
         'density_residual_method':'direct Cartesian W dot grad(rho)-rho, not y*Rf'}
    for name,value in [('abs_Rf',abs(v['Rf'])),('abs_Rrho',abs(v['Rrho'])),('normalized_Rf',qf),('normalized_Rrho',qr)]:
        k=int(np.argmax(value));out['max_'+name]=float(value[k]);out['location_'+name]=[float(x[k]),float(y[k])]
        out['rms_'+name]=float(np.sqrt(np.mean(value**2)))
        out['weighted_rms_'+name]=None if ww is None else float(np.sqrt(ww@(value**2)))
    out['rms_fitting_residual']=float(np.sqrt(np.mean(v['physical_fit']**2)))
    out['weighted_rms_fitting_residual']=None if ww is None else float(np.sqrt(ww@(v['physical_fit']**2)))
    out['max_normalized_Rf_percent']=100*out['max_normalized_Rf']
    out['max_normalized_Rrho_percent']=100*out['max_normalized_Rrho']
    if region_name=='far_growth_rings512_to16384':
        out['growth_rings']=[];gamma=1/case['cl']
        for lo in range(0,len(x),129):
            sl=slice(lo,lo+129);r=float(np.hypot(x[lo],y[lo]));vel=np.hypot(v['psix'][sl],v['psiy'][sl])
            out['growth_rings'].append({'radius':r,'max_abs_rho_over_r_gamma':float(max(abs(v['rho'][sl]))/r**gamma),
                'max_U_over_r_gamma':float(max(vel)/r**gamma),'max_abs_psi_over_r_1plusgamma':float(max(abs(v['psi'][sl]))/r**(1+gamma)),
                'max_abs_psi_over_r2':float(max(abs(v['psi'][sl]))/r**2)})
    return out


def source_modes(case,radii,angular_factor=2):
    """Independent sine transform of rho_x=y*f_x, with no fitted psi used."""
    mmax=max([3]+[int(m['m']) for m in case.get('modes',[])])
    count=mmax+1; L=angular_factor*(count+1)
    theta=np.arange(1,L)*np.pi/(2*L)
    sine=np.sin(np.outer(theta,2*np.arange(1,count+1)))
    answer=np.empty((len(radii),count))
    # At most about four thousand Cartesian points per native fields call.
    block=max(1,4096//len(theta))
    for lo in range(0,len(radii),block):
        rr=np.asarray(radii[lo:lo+block]); xx=(rr[:,None]*np.cos(theta)).ravel(); yy=(rr[:,None]*np.sin(theta)).ravel()
        ff=total_fields_saved(case,xx,yy)
        source=(yy*ff['fx']).reshape(len(rr),len(theta))
        answer[lo:lo+len(rr)]=(2/L)*(source@sine)
    return answer


def green_once(case,points,order,angular_factor=2,separator=8192.,source_function=None):
    """Composite finite integral plus actual infinite compactified tail.

    The separator is an integration partition, never a Poisson boundary.
    Both source and its Fourier projection are independent of fitted psi.
    """
    gamma=1/case['cl']; aa=1-gamma
    if not 0<aa<1:raise ValueError('Canonical subquadratic branch requires cl>1')
    radii=np.array([math.hypot(*p) for p in points]);positive=radii[radii>0]
    separator=max(float(separator),float(max(positive,default=0.)))
    breaks=sorted(set([0.,.03125,.0625,.125,.25,.5,1.,2.,4.,8.,16.,32.,64.,128.,256.,512.,1024.,2048.,4096.,separator]+positive.tolist()))
    breaks=[r for r in breaks if r<=separator]
    for mode in case.get('modes',[]):
        if mode['family']=='local':
            for k in [-3,-2,-1,0,1,2,3]:
                ss=float(mode['center'])+k*float(mode['width'])
                if ss>0:
                    r=math.sqrt(math.expm1(ss))
                    if 0<r<separator:breaks.append(r)
    breaks=sorted(set(breaks))
    z,w=np.polynomial.legendre.leggauss(order)
    nodes=[]; ds=[]
    for lo,hi in zip(breaks[:-1],breaks[1:]):
        if lo==0:
            nodes.extend((hi*(z+1)/2).tolist());ds.extend((hi*w/2).tolist())
        else:
            l,h=math.log(lo),math.log(hi);rr=np.exp(l+(h-l)*(z+1)/2)
            nodes.extend(rr.tolist());ds.extend(((h-l)*w*rr/2).tolist())
    nodes=np.asarray(nodes); ds=np.asarray(ds)
    source_function=source_modes if source_function is None else source_function
    gn=source_function(case,nodes,angular_factor); nn=2*np.arange(1,gn.shape[1]+1)
    u=(z+1)/2; uw=w/2
    tail_r=separator*u**(-1/aa)
    tg=source_function(case,tail_r,angular_factor)
    scaled_tail=separator**2/aa*np.sum(uw[:,None]*u[:,None]**((nn[None,:]-2)/aa-1)*tg,axis=0)
    strain_finite=.5*float(np.sum(ds*gn[:,0]/nodes));strain_tail=float(scaled_tail[0]/(2*separator**2))
    answer=[]
    for (x,y),r in zip(points,radii):
        if r==0:
            answer.append({'psi':0.,'psix':0.,'psiy':0.,'strain':strain_finite+strain_tail,
                           'strain_finite':strain_finite,'strain_infinite_tail':strain_tail});continue
        inside=nodes<r;outside=nodes>r
        ii=np.sum(ds[inside,None]*r*(nodes[inside,None]/r)**(nn[None,:]+1)*gn[inside],axis=0)
        oo=np.sum(ds[outside,None]*r*r/nodes[outside,None]*(r/nodes[outside,None])**(nn[None,:]-2)*gn[outside],axis=0)
        tails=(r/separator)**nn*scaled_tail;oo+=tails
        pp=(ii+oo)/(2*nn);dp=(-ii+oo)/(2*r);theta=math.atan2(y,x)
        sine=np.sin(nn*theta);cosine=np.cos(nn*theta)
        value=float(pp@sine);rad=float(dp@sine);ang=float((nn*pp)@cosine)
        answer.append({'psi':value,'psix':math.cos(theta)*rad-math.sin(theta)*ang/r,
                       'psiy':math.sin(theta)*rad+math.cos(theta)*ang/r,
                       'psi_infinite_tail':float((tails/(2*nn))@sine),
                       'highest_source_mode':int(nn[-1])})
    return answer,{'radial_order_per_interval':order,'angular_factor':angular_factor,
                   'radial_finite_nodes':len(nodes),'infinite_tail_nodes':order,'finite_separator':separator,
                   'maximum_sampled_tail_radius':float(max(tail_r)),
                   'infinite_tail_retained':True,'finite_radial_breakpoints':breaks,
                   'tail_mapping':'u=(separator/s)^(1-gamma), 0<u<=1; u=0 is s=infinity',
                   'source':'rho_x=y*f_x evaluated without psi; finite sine projection',
                   'angular_bandwidth':int(nn[-1])}


def inverse(case):
    points=[(0.,0.),(.3,.2),(1.,.7),(2.,1.5),(0.,2.),(2.,0.),(8.,0.),(0.,64.),
            (31.,17.),(90.,70.),(230.,150.),(0.,512.),(512.,0.),(200.,1e-9),
            (1000.,700.),(0.,8192.),(8192.,0.)]
    exact=total_fields_saved(case,*np.array(points).T)
    previous=None;orders=[];fine=None;qerror=None;center_qerror=None
    for order in [24,48,96,192]:
        computed,metadata=green_once(case,points,order,2)
        orders.append(metadata)
        if previous is not None:
            qerror=max(abs(u[k]-v[k]) for u,v in zip(previous,computed) for k in ('psi','psix','psiy'))
            scaled=max(abs(u[k]-v[k])/(1e-7+1e-9*abs(exact[k][i])) for i,(u,v) in enumerate(zip(previous,computed)) for k in ('psi','psix','psiy'))
            center_qerror=abs(previous[0]['strain']-computed[0]['strain'])
            if scaled<.2 and center_qerror<2e-9:
                fine=computed;break
        previous=computed;fine=computed
    angular,angular_meta=green_once(case,points,orders[-1]['radial_order_per_interval'],4)
    aerror=max(abs(u[k]-v[k]) for u,v in zip(fine,angular) for k in ('psi','psix','psiy'))
    ascaled=max(abs(u[k]-v[k])/(1e-7+1e-9*abs(exact[k][i])) for i,(u,v) in enumerate(zip(fine,angular)) for k in ('psi','psix','psiy'))
    acenter=abs(fine[0]['strain']-angular[0]['strain'])
    rows=[];passed=True
    for i,(point,computed) in enumerate(zip(points,angular)):
        row={'point':list(point),'computed':computed}
        for key in ('psi','psix','psiy'):
            error=abs(computed[key]-float(exact[key][i]));tol=1e-7+1e-9*abs(exact[key][i])
            row[key+'_abs_error']=error;row[key+'_tolerance']=float(tol)
            passed &= error<=tol
        rows.append(row)
    center_error=abs(angular[0]['strain']-exact['ratio'][0])
    # qerror is also retained; full pointwise limits avoid overly strict global
    # absolute convergence at far points with O(r^(1+gamma)) stream functions.
    qpassed=len(orders)>1 and scaled<.2 and center_qerror<2e-9
    passed &= center_error<=1e-8 and ascaled<.2 and acenter<2e-9 and qpassed
    return {'method':'Independent source sine modes; composite radial Green integrals plus compactified entire infinite tail',
            'points':rows,'orders':orders,'angular_refinement':angular_meta,'last_orders_max_abs_difference':qerror,
            'last_orders_max_tolerance_fraction':None if len(orders)<2 else scaled,
            'radial_center_strain_refinement_difference':center_qerror,
            'angular_refinement_max_abs_difference':aerror,'angular_max_tolerance_fraction':ascaled,
            'angular_center_strain_refinement_difference':acenter,'center_strain_abs_error':float(center_error),
            'center_strain_tolerance':1e-8,'passed':bool(passed),'infinite_tail_retained':True,
            'boundary_note':'8192 is a quadrature partition only. No outer boundary value is imposed.'}


def manufactured():
    """Closed-form density tests of the new quadrature, independently of basis."""
    points=[(0.,0.),(.2,.3),(1.,.4),(2.,3.),(0.,2.),(2.,0.),(31.,17.),(512.,0.),(1000.,700.),(0.,8192.)]
    results=[]
    for exponent in [1,2]:
        def source(case,radii,angular_factor):
            rr=np.asarray(radii);value=np.zeros((len(rr),4))
            value[:,0]=-exponent*rr*rr/(1+rr*rr)**(exponent+1)
            return value
        exact=[]
        for x,y in points:
            q=x*x+y*y
            if q==0:exact.append({'psi':0.,'psix':0.,'psiy':0.,'strain':-.25});continue
            integral=q-np.log1p(q) if exponent==1 else np.log1p(q)+1/(1+q)-1
            h=-integral/(2*q*q)
            hp=-(1+q)**(-exponent)/(2*q)+integral/q**3
            exact.append({'psi':x*y*h,'psix':y*h+2*x*x*y*hp,'psiy':x*h+2*x*y*y*hp})
        rows=[]
        for order in [24,48,96]:
            computed,meta=green_once({'cl':1.88359472051,'modes':[]},points,order,source_function=source)
            error=max(abs(a[k]-b[k]) for a,b in zip(computed,exact) for k in ('psi','psix','psiy'))
            strain=abs(computed[0]['strain']+.25)
            rows.append({'order':order,'maximum_field_error':error,'center_strain_error':strain,'quadrature':meta})
        results.append({'density':'y/(1+r^2)^'+str(exponent),'refinements':rows,
                        'passed':rows[-1]['maximum_field_error']<1e-9 and rows[-1]['center_strain_error']<1e-10})
    out={'schema':'stage12-manufactured-infinite-tail-Green-v1','cases':results,
         'source_sha256':assessment_source_identity(),'environment':provenance(),'passed':all(r['passed'] for r in results)}
    atomic(OUT/'manufactured_green.json',out);print(json.dumps(out),flush=True)
    if not out['passed']:raise SystemExit(2)


def taylor(case):
    hp=jet.high_precision(case['cl'],case['coefficients'],prec=70)
    values=[float(x) for x in hp['constraints']+hp['fourth']]
    return {'high_precision':hp,'maximum_five_defect':max(map(abs,values)),'passed':max(map(abs,values))<1e-10,
            'extra_jets_exactly_zero':True,
            'justification':'Each actual new chi mode has analytic homogeneous Taylor order >=10; rho/y begins order6, psi/(xy) begins order6. Core center and f,psi jets needed by C5 are unchanged for arbitrary new coefficients and c_l derivatives.',
            'new_coefficients_nonzero':int(np.count_nonzero(case.get('extra_coefficients',[])))}


def regularity(case):
    x=np.array([.3,1.,2.,31.,.4]);y=np.array([.2,.7,0.,17.,1e-5])
    ff=total_fields_saved(case,x,y);parity=0.
    for sx,sy in [(-1,1),(1,-1),(-1,-1)]:
        other=total_fields_saved(case,sx*x,sy*y)
        for key,sign in [('f',1),('fx',sx),('fy',sy),('psi',sx*sy),('psix',sy),('psiy',sx),('ratio',1)]:
            parity=max(parity,float(max(abs(other[key]-sign*ff[key]))))
    rows=[]
    for factor in [.002,.001]:
        h=factor*np.maximum(1.,np.hypot(x,y));center=ff['psi'];lap=np.zeros(len(x))
        for axis in [0,1]:
            dx,dy=(h,0) if axis==0 else (0,h)
            vals=[total_fields_saved(case,x+j*dx,y+j*dy)['psi'] for j in [-2,-1,1,2]]
            lap+=(-vals[0]+16*vals[1]-30*center+16*vals[2]-vals[3])/(12*h*h)
        err=-lap-y*ff['fx'];rows.append({'relative_step':factor,'Poisson_max_abs_difference':float(max(abs(err)))})
    return {'parity_max_abs':parity,'parity_passed':parity<1e-9,
            'independent_Cartesian_Poisson':rows,'finite_difference_truncation_retained':True,
            'analytic_Poisson_identity':'-Delta chi_xy = partial_x(-partial_y Delta chi) by commutation; no extra harmonic strain'}


def physical_comparisons(case,reference_paths):
    theta=np.r_[0.,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    coords=polar(np.geomspace(.035,8.,17),theta)
    x,y=np.r_[0.,coords['x']],np.r_[0.,coords['y']]
    current=total_fields_saved(case,x,y);rad=1+np.hypot(x,y);rows=[]
    for path in reference_paths:
        reference=read(path);other=total_fields_saved(reference,x,y)
        scale=max(1.,abs(other['f'][0]))*math.sqrt(3*len(x))
        delta=np.r_[current['f']-other['f'],(current['psix']-other['psix'])/rad,(current['psiy']-other['psiy'])/rad]
        rows.append({'reference_path':str(path.resolve()),'reference_sha256':digest(path),
                     'reference_vector_sha256':vector_hash(reference),'distance':float(np.linalg.norm(delta)/scale),
                     'delta_cl':case['cl']-reference['cl'],'delta_a0':float(current['f'][0]-other['f'][0]),
                     'reference_a0':float(other['f'][0]),'normalization':float(scale)})
    return {'points':len(x),'coordinate_sha256':coord_hash(x,y),'comparisons':rows,
            'metric':'norm(concat(delta_f,delta_psix/(1+r),delta_psiy/(1+r)))/(max(1,abs(reference_a0))*sqrt(3*N))',
            'spatial_alignment_performed':False}


def csv_write(path,record):
    keys=['region','points','coordinate_sha256','max_abs_Rf','max_normalized_Rf','max_abs_Rrho','max_normalized_Rrho',
          'rms_abs_Rf','rms_abs_Rrho','rms_fitting_residual','weighted_rms_fitting_residual','floor_hits_f','floor_hits_rho',
          'location_normalized_Rf','location_normalized_Rrho']
    stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=keys);writer.writeheader()
    for name,row in record['regions'].items():
        rr={k:row.get(k) for k in keys};rr['region']=name
        for k,v in rr.items():
            if isinstance(v,list):rr[k]=json.dumps(v)
        writer.writerow(rr)
    path.write_text(stream.getvalue())


def evaluate(args):
    if not COORDS.exists():raise ValueError('Freeze and hash assessment coordinates before optimization')
    case=read(args.candidate);modes=case.get('modes',[]);extra=case.get('extra_coefficients',[])
    if len(extra)!=len(modes) or len(case['coefficients'])!=24:raise ValueError('Invalid saved physical vector')
    if not all(math.isfinite(v) for v in [case['cl']]+case['coefficients']+extra):raise ValueError('Nonfinite saved vector')
    began=time.time();coords=read(COORDS);design=read(DESIGN)
    record={'schema':'stage12-independent-physical-assessment-v1','label':args.label,'part':args.part,
            'candidate_path':str(args.candidate.resolve()),'candidate_sha256':digest(args.candidate),'physical_vector_sha256':vector_hash(case),
            'coordinate_file_sha256':digest(COORDS),'design_file_sha256':digest(DESIGN),
            'source_sha256':assessment_source_identity(),'source_identity_scope':'actual numerical dependencies; excludes unrelated campaign scripts',
            'environment':provenance(),'started_epoch':began,
            'cl':case['cl'],'a0':float(total_fields_saved(case,[0.],[0.])['f'][0]),
            'core_coefficients':case['coefficients'],'extra_coefficients':extra,'modes':modes,
            'regions':{},'optimization_performed':False,'completed':False}
    output=OUT/(args.label+'_'+args.part+'.json')
    if args.part in ['all','regions']:
        for name,row in coords.items():
            if coord_hash(row['x'],row['y'])!=design['regions'][name]['coordinate_sha256']:raise ValueError('Frozen coordinate mismatch: '+name)
            record['regions'][name]=diagnostic(case,row,record['a0'],name);atomic(output,record)
            print(args.label+' '+name+' complete',flush=True)
    if args.part in ['all','inverse']:
        record['canonical_inverse']=inverse(case)
    if args.part in ['all','structure']:
        record['taylor']=taylor(case);record['regularity']=regularity(case)
        references=[ROOT/'inputs/stage11_endpoint.json']+args.reference
        record['physical_fields']=physical_comparisons(case,references)
    if args.part in ['all','regions']:
        import stage12_model
        record['objective97']=stage12_model.objective_saved(case,n=97)
    record['completed']=True;record['elapsed_seconds']=time.time()-began
    record['checks_passed']=all(record.get(key,{}).get('passed',True) for key in ['canonical_inverse','taylor'])
    if 'regularity' in record:record['checks_passed'] &= record['regularity']['parity_passed']
    atomic(output,record)
    if record['regions']:csv_write(output.with_suffix('.csv'),record)
    print(json.dumps({'output':str(output),'checks_passed':record['checks_passed'],'elapsed':record['elapsed_seconds']}),flush=True)
    if not record['checks_passed']:raise SystemExit(2)


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='mode',required=True)
    sub.add_parser('freeze')
    sub.add_parser('manufactured')
    ev=sub.add_parser('evaluate');ev.add_argument('--candidate',type=Path,required=True);ev.add_argument('--label',required=True)
    ev.add_argument('--part',choices=['all','regions','inverse','structure'],default='all')
    ev.add_argument('--reference',type=Path,action='append',default=[],help='Additional saved candidates for the historical physical-field metric')
    args=parser.parse_args()
    if args.mode=='freeze':freeze()
    elif args.mode=='manufactured':manufactured()
    else:
        if not args.label or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-' for c in args.label):raise ValueError('Unsafe output label')
        evaluate(args)


if __name__=='__main__':main()
