"""Stage VIII: nested 20-to-24 parameter 3delta test. No plots or gauges.

Frozen numerical engines are local exact copies. Four 3delta entries are appended;
objective, quadrature, bounds convention and stored assessment grids are preserved.
All writes stay in this directory.
"""
from ipm_portable import output_dir, peak_rss_mib
import argparse
import hashlib
import json
import gzip
from pathlib import Path
import resource
import signal
import time
import importlib
from types import SimpleNamespace
import numpy as np
import psutil
from scipy.linalg import null_space
from scipy.optimize import least_squares
from threadpoolctl import threadpool_info, threadpool_limits
import stage6_engine as w

v=w.v;t=w.t;s=w.s;e=s.e
ROOT=Path(__file__).resolve().parent
OUT = output_dir()
save=t.save
WEIGHTS=(.1,)
CL_STEP_DEFAULT=1e-4
LABELS=[f'{b}_L{tag}' for b in ('S0','B') for tag in ('0','01','03','1')]

def load(name):
    path=OUT/(name+'.json')
    if not path.exists() and path.with_suffix('.json.gz').exists():
        with gzip.open(path.with_suffix('.json.gz'),'rt') as f:return json.load(f)
    if not path.exists():path=ROOT/'inputs'/('start_'+name+'.json')
    return json.loads(path.read_text())


def trap(nodes):
    a=np.asarray(nodes);d=np.empty(len(a))
    d[0]=(a[1]-a[0])/2;d[-1]=(a[-1]-a[-2])/2
    d[1:-1]=(a[2:]-a[:-2])/2
    return d/(a[-1]-a[0])

def far_grid(n=49):
    r=np.geomspace(8.,64.,n);theta=np.linspace(0,np.pi/2,n)
    x,y=s.polar(r,theta)
    weights=np.outer(trap(np.log(r)),trap(theta)).ravel()
    return x,y,weights

class JointProblem(s.Problem):
    def __init__(self,weight):
        assert weight in WEIGHTS
        xi,yi=e.polar_grid(49,49,8.);xf,yf,wf=far_grid()
        super().__init__(3,4,np.r_[xi,xf],np.r_[yi,yf],'fractional2',True)
        self.far_weight=weight;self.n=49;self.aggregation='W'
        self.wi=w.quadrature(49);self.wf=wf
        self.root=np.sqrt(np.r_[self.wi,weight*self.wf])
        self.last_raw=None;self.last_parameters=None
    def fun(self,p):
        self.last_raw=super().fun(p);self.last_parameters=p.copy()
        return self.root*self.last_raw
    def objectives(self):
        a,b=np.split(self.last_raw,2)
        ji=float(self.wi@(a*a)/2);jf=float(self.wf@(b*b)/2)
        return {'J_inner':ji,'J_far':jf,'J_joint':ji+self.far_weight*jf}


v.load=load


def fingerprint(case):
    return hashlib.sha256(np.r_[case['cl'],case['coefficients']].astype('<f8').tobytes()).hexdigest()

def angles(n):
    return np.r_[0,1e-9,1e-6,.001,(np.arange(n)+.37)*np.pi/(2*n),
                 np.pi/2-.001,np.pi/2-1e-6,np.pi/2-1e-9,np.pi/2]


def grid_record(x,y):
    return {'points':len(x),'radius_min':float(min(np.hypot(x,y))),
            'radius_max':float(max(np.hypot(x,y))),
            'coordinate_sha256':hashlib.sha256(np.column_stack([x,y]).tobytes()).hexdigest()}

def conditioning(case,prob):
    p=t.parameters(case);J=hybrid_jac(prob,p);r=prob.fun(p)
    D=1/np.linalg.norm(J,axis=0);U,sv,Vt=np.linalg.svd(J*D,full_matrices=False)
    raw=np.linalg.svd(J,compute_uv=False);g=J.T@r
    theta=np.r_[0,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    x,y=s.polar(np.geomspace(.035,8,17),theta);x,y=np.r_[0.,x],np.r_[0.,y]
    ff,design=t.field_design(prob,p,x,y);rad=1+np.hypot(x,y)
    B=np.vstack([design['f'],design['psix']/rad[:,None],design['psiy']/rad[:,None]])/(max(1,abs(ff['f'][0]))*np.sqrt(3*len(x)))
    _,sb,vb=np.linalg.svd(B,full_matrices=False)
    field=np.linalg.svd(J@(vb.T/sb[None,:]),compute_uv=False)
    tangent=t.scale_target(case,x,y,ff)
    exact=np.r_[tangent['f'],tangent['psix']/rad,tangent['psiy']/rad]/(max(1,abs(ff['f'][0]))*np.sqrt(3*len(x)))
    weak=[]
    for k in (1,2,3):
        dp=D*Vt[-k];dp/=np.linalg.norm(B@dp);bf=B@dp
        weak.append({'rank_from_smallest':k,'parameters_per_unit_field':dp.tolist(),
                     'delta_cl':float(dp[0]),'delta_a0':float(design['f'][0]@dp),
                     'physical_scale_cosine':float(abs(bf@exact)/(np.linalg.norm(bf)*np.linalg.norm(exact)))})
    return {'raw_condition':float(raw[0]/raw[-1]),'column_condition':float(sv[0]/sv[-1]),
            'field_condition':float(field[0]/field[-1]),'raw_singular_values':raw.tolist(),
            'column_singular_values':sv.tolist(),'field_singular_values':field.tolist(),
            'weak_directions':weak,'physical_gradient_inf':float(max(abs(g))),
            'column_scaled_gradient_inf':float(max(abs(D*g))),
            'physical_gradient':g.tolist(),'column_scaled_gradient':(D*g).tolist(),
            'frozen_coordinate_gradient_inf':coordinate_gradient(case,g),
            'whitened_gradient_norm':float(np.linalg.norm(U.T@r)),
            'relative_projected_residual':float(np.linalg.norm(U.T@r)/np.linalg.norm(r)),
            'root_mass':float(np.linalg.norm(prob.root))}


def diagnostic(case,x,y):
    """Original physical term sums/floors, globally computed per assessment region."""
    ff={}
    for lo in range(0,len(x),512):
        hi=min(len(x),lo+512);block=s.fields(case,x[lo:hi],y[lo:hi])
        if not ff:ff={k:np.empty(len(x)) for k in block}
        for k in ff:ff[k][lo:hi]=block[k]
    cl=case['cl'];wx=cl*x-ff['psiy'];wy=cl*y+ff['psix']
    t1=wx*ff['fx'];t2=wy*ff['fy'];t3=(cl-1+ff['ratio'])*ff['f'];rf=t1+t2+t3;rr=y*rf
    rho=y*ff['f'];nf=abs(t1)+abs(t2)+abs(t3)
    nr=abs(wx*y*ff['fx'])+abs(wy*(ff['f']+y*ff['fy']))+abs(rho)
    a0=s.fields(case,[0.],[0.])['f'][0];ef=1e-10*max(1,abs(a0));er=1e-10*max(1,float(max(abs(rho))))
    values={'abs_Rf':abs(rf),'abs_Rrho':abs(rr),'normalized_Rf':abs(rf)/np.maximum(nf,ef),
            'normalized_Rrho':abs(rr)/np.maximum(nr,er)}
    fit=rf/np.sqrt(t1*t1+t2*t2+t3*t3+(1e-8*(1+x*x+y*y)**((1/cl-1)/2))**2)
    result={**grid_record(x,y),'epsilon_f':float(ef),'epsilon_rho':float(er),
            'floor_hits_f':int(sum(nf<=ef)),'floor_hits_rho':int(sum(nr<=er)),
            'rms_fitting_residual':float(np.sqrt(np.mean(fit*fit))),
            'rms_normalized_Rf':float(np.sqrt(np.mean(values['normalized_Rf']**2)))}
    for key,a in values.items():
        i=int(np.argmax(a));result['max_'+key]=float(a[i]);result['location_'+key]=[float(x[i]),float(y[i])]
    return result

def assess(args):
    case=load(args.label);coords=load('assessment_grids');records={}
    save(args.label+'_'+args.part+'_source.json',{'cl':case['cl'],'physical_vector_sha256':fingerprint(case)})
    for name,row in coords.items():
        if args.part=='main' and (name.startswith('band_') or name in ('x_axis','y_axis','near_axis','near_origin','origin')):continue
        if args.part=='bands' and not (name.startswith('band_') or name in ('x_axis','y_axis','near_axis','near_origin','origin')):continue
        records[name]=diagnostic(case,np.array(row['x']),np.array(row['y']))
        # Persist each completed region if a resource stop arrives later.
        save(args.label+'_'+args.part+'_diagnostics.json',records)
    save(args.label+'_'+args.part+'_diagnostics.json',records)
    print(json.dumps({'label':args.label,'regions':len(records)},indent=2))

def cross(args):
    case=load(args.label);prob=problem_for(case);r=prob.fun(t.parameters(case))
    rows={'fit49':prob.objectives(),'physical_vector_sha256':fingerprint(case)}
    coords=load('assessment_grids')
    row=coords['inner_validation97'];x,y=np.array(row['x']),np.array(row['y']);raw=w.raw_values(case,x,y)
    ji=float(w.quadrature(97)@(raw*raw)/2)
    row=coords['far_validation_shifted'];x,y=np.array(row['x']),np.array(row['y']);raw=w.raw_values(case,x,y)
    rows['independent_assessment']={'J_inner97':ji,'RMS_inner97':float(np.sqrt(2*ji)),
                          'RMS_far_shifted_midpoint':float(np.sqrt(np.mean(raw*raw))),
                          'no_new_assessment_locations':True}
    save(args.label+'_objectives.json',rows);print(json.dumps({'label':args.label,**rows},indent=2))

def independent(args):
    case=load(args.label);checks=s.independent_checks(case)
    checks['physical_vector_sha256']=fingerprint(case)
    ty=checks['taylor'];ty['signed_center_identity_defect']=case['cl']+ty['strain']-1
    ty['abs_Rf_x2']=abs(ty['Rf_x2']);ty['abs_Rf_y2']=abs(ty['Rf_y2'])
    # Extra inverse and derivative checks in the fitted far band and unseen tail.
    points=[(8.,0.),(0.,64.),(31.,17.),(90.,70.),(230.,150.),(0.,512.),(512.,0.),(200.,1e-9)]
    items=s.basis(case['cl'],case['nm'],case['nk'],case['family']);c=np.array(case['coefficients'])
    source=[(co,a,b+1,p) for co,a,b,p in e.merged(items,c,'fx')]
    xx,yy=np.array(points).T;exact=s.fields(case,xx,yy)
    inv=[e.canonical_inverse(source,points,o) for o in (80,120)]
    refined=None
    if max(abs(inv[0][k][key]-inv[1][k][key]) for k in range(len(points)) for key in ('psi','psix','psiy'))>1e-8:
        refined=[e.canonical_inverse(source,points,o) for o in (240,480)]
    best=refined[-1] if refined else inv[-1]
    rows=[]
    for k,point in enumerate(points):
        rows.append({'point':point,**{f'error_{key}':float(abs(best[k][key]-exact[key][k])) for key in ('psi','psix','psiy')},
                     'quadrature_difference':float(max(abs(inv[0][k][key]-inv[1][k][key]) for key in ('psi','psix','psiy'))),
                     'final_quadrature_order':480 if refined else 120,
                     'refined_quadrature_difference':float(max(abs(refined[0][k][key]-refined[1][k][key]) for key in ('psi','psix','psiy'))) if refined else None,
                     'max_field':float(max(abs(exact[key][k]) for key in ('psi','psix','psiy')))})
    checks['extended_inverse']=rows
    checks['canonical_inverse']['exterior_strain'].update({str(r):e.exterior_strain(source,r) for r in (64,256,512)})
    ft=e.merged(items,c,'f');ht=[(co,a-1,b-1,p) for co,a,b,p in e.merged(items,c,'psi')]
    fv=lambda x,y:e.evaluate(ft,x,y);hv=lambda x,y:e.evaluate(ht,x,y);rv=lambda x,y:y*fv(x,y)
    rf=e.residual(case['cl'],exact,xx,yy);steps=[]
    for h0 in (.002,.001):
        h=h0*np.maximum(1,np.hypot(xx,yy))
        def diff(fun,axis):
            dx,dy=(h,0) if axis==0 else (0,h)
            return (-fun(xx+2*dx,yy+2*dy)+8*fun(xx+dx,yy+dy)-8*fun(xx-dx,yy-dy)+fun(xx-2*dx,yy-2*dy))/(12*h)
        hh=hv(xx,yy);q=hh+xx*diff(hv,0)
        wx=case['cl']*xx-xx*(hh+yy*diff(hv,1));wy=case['cl']*yy+yy*q
        rff=wx*diff(fv,0)+wy*diff(fv,1)+(case['cl']-1+q)*fv(xx,yy)
        rrr=wx*diff(rv,0)+wy*diff(rv,1)-rv(xx,yy)
        steps.append({'relative_step':h0,'Rf_disagreement':float(max(abs(rff-rf))),
                      'Rrho_disagreement':float(max(abs(rrr-yy*rf)))})
    checks['extended_transport_FD']={'points':points,'steps':steps}
    save(args.label+'_independent.json',checks)
    print(json.dumps({'label':args.label,'taylor':ty,'extended_inverse_max':max(row['error_psi'] for row in rows)},indent=2))

def analyze(args):
    case=load(args.label);save(args.label+'_conditioning.json',dict(conditioning(case,problem_for(case)),physical_vector_sha256=fingerprint(case)))


def compare(args):
    case=load(args.label);base=load('baseline_'+case['basin']);result={}
    coords=load('assessment_grids')
    def batched(c,x,y):
        ff={k:[] for k in ('f','psi','psix','psiy')}
        for lo in range(0,len(x),512):
            values=s.fields(c,x[lo:lo+512],y[lo:lo+512])
            for k in ff:ff[k].extend(values[k])
        return {k:np.array(a) for k,a in ff.items()}
    inner=coords['inner_validation97'];xx,yy=np.array(inner['x']),np.array(inner['y'])
    reference=batched(base,xx,yy)['f'];norm=np.linalg.norm(reference)
    ft=e.merged(s.basis(case['cl'],case['nm'],case['nk'],case['family']),case['coefficients'],'f')
    def alignment(logscale):
        scale=np.exp(logscale)
        return float(np.linalg.norm(e.evaluate(ft,xx/scale,yy/scale)-reference)/norm)
    aligned=s.minimize_scalar(alignment,bounds=(np.log(.25),np.log(4.)),method='bounded',options={'xatol':1e-6})
    scale=float(np.exp(aligned.x));aligned_result={}
    for name,region in [('inner','inner_validation97'),('far','far_validation_shifted'),('unseen','true_H65')]:
        row=coords[region];x,y=np.array(row['x']),np.array(row['y'])
        a=batched(base,x,y);b=batched(case,x,y)
        result[name]={key:float(np.linalg.norm(b[key]-a[key])/np.linalg.norm(a[key])) for key in ('f','psi','psix','psiy')}
        aligned_fields=batched(case,x/scale,y/scale)
        aligned_fields['psi']*=scale**2
        for key in ('psix','psiy'):aligned_fields[key]*=scale
        aligned_result[name]={key:float(np.linalg.norm(aligned_fields[key]-a[key])/np.linalg.norm(a[key])) for key in ('f','psi','psix','psiy')}
    save(args.label+'_shapes.json',{'cl_change':case['cl']-base['cl'],'a0_change':case['a0']-base['a0'],
                                  'unaligned_relative_L2':result,'amplitude_adjusted':False,
                                  'postprocessing_spatial_lambda':scale,'spatially_aligned_relative_L2':aligned_result,
                                  'alignment_selected_on':'stored inner97 f values only; diagnostic, candidate unchanged',
                                  'physical_vector_sha256':fingerprint(case)})

# The first twenty coefficient entries retain the original arithmetic/order.
# Only four entries are appended. c00 retains its old elimination at zero new entries.
import math
import sys
OldJointProblem=JointProblem
old_basis=s.basis
old_fields=s.fields
old_parameters=t.parameters

def basis24(cl,nm,nk,family):
    if family!='fractional3':return old_basis(cl,nm,nk,family)
    assert (nm,nk)==(3,5)
    items=old_basis(cl,3,4,'fractional2')
    d,delta=(3+1/cl)/2,(1-1/cl)/2
    for m in range(4):
        chi=[(float((-1)**j*math.comb(2*m,2*j)),2*m-2*j,2*j,d-m-3*delta) for j in range(m+1)]
        psi=e.derivative(e.derivative(chi,0),1)
        rho=[(-c,a,b,p) for c,a,b,p in e.derivative(e.laplace(chi),1)]
        f=e.divide_y(rho);psix=e.derivative(psi,0)
        items.append(dict(f=f,fx=e.derivative(f,0),fy=e.derivative(f,1),psi=psi,
                          psix=psix,psiy=e.derivative(psi,1),ratio=e.divide_y(psix)))
    return items

def dot(M,c):
    """Preserve old BLAS summation at a strict zero-layer embedding."""
    c=np.asarray(c)
    if len(c)==20:return M@c
    return np.ascontiguousarray(M[...,:20])@c[:20]+np.ascontiguousarray(M[...,20:])@c[20:]

def fields24(case,x,y):
    if case['family']!='fractional3':return old_fields(case,x,y)
    mats=e.matrices(basis24(case['cl'],3,5,'fractional3'),x,y)
    return {k:dot(M,case['coefficients']) for k,M in mats.items()}

s.basis=basis24;s.fields=fields24

class Raw24(s.Problem):
    def __init__(self,x,y):super().__init__(3,5,x,y,'fractional3',True)
    def coefficients(self,p):
        _,strain=self.data(p[0])
        # Old free part is evaluated identically before the new part is subtracted.
        c0=(1-p[0]-strain[1:20]@p[1:20]-strain[20:]@p[20:])/strain[0]
        return np.r_[c0,p[1:]]
    def fun(self,p):
        mats,strain=self.data(p[0]);c=self.coefficients(p)
        f={k:dot(M,c) for k,M in mats.items()}
        a=(p[0]*self.x-f['psiy'])*f['fx'];b=(p[0]*self.y+f['psix'])*f['fy']
        reaction=dot(mats['ratio']-strain[None,:],c);d=reaction*f['f']
        w0=(1+self.x**2+self.y**2)**((1/p[0]-1)/2)
        return (a+b+d)/np.sqrt(a*a+b*b+d*d+(1e-8*w0)**2)
    def metadata(self,p):
        self.data(p[0]);return {'cl':float(p[0]),'a0':float(dot(self.center_f,self.coefficients(p)))}

class JointProblem(Raw24):
    def __init__(self,weight=.1):
        assert weight==.1
        nodes=json.loads((ROOT/'inputs/fitting_grid49.json').read_text())
        xi,yi=np.array(nodes['inner']['x']),np.array(nodes['inner']['y'])
        xf,yf=np.array(nodes['far']['x']),np.array(nodes['far']['y'])
        super().__init__(np.r_[xi,xf],np.r_[yi,yf])
        self.far_weight=weight;self.n=49;self.aggregation='W'
        self.wi=w.quadrature(49);self.wf=far_grid()[2]
        self.root=np.sqrt(np.r_[self.wi,weight*self.wf])
        self.last_raw=None;self.last_parameters=None
    def fun(self,p):
        self.last_raw=super().fun(p);self.last_parameters=p.copy()
        return self.root*self.last_raw
    objectives=OldJointProblem.objectives

def problem_for(case):
    return JointProblem(.1) if case['family']=='fractional3' else OldJointProblem(.1)

def parameters(case):
    if case['family']=='fractional3':
        assert (case['nm'],case['nk'],len(case['coefficients']))==(3,5,24)
        return np.r_[case['cl'],case['coefficients'][1:]]
    return old_parameters(case)

def coordinate_gradient(case,g):
    if 'mapping' not in case:return None
    m=case['mapping']
    mapped=np.array(m['column_scale'])*g if 'column_scale' in m else np.array(m['full_coordinate_map']).T@g
    return float(max(abs(mapped)))

def case_at(p,prob,n=49,label='state'):
    new=len(p)==24
    return dict(label=label,nm=3,nk=5 if new else 4,family='fractional3' if new else 'fractional2',
                nr=n,nt=n,rmax=8.,stable_center=True,cl=float(p[0]),
                coefficients=prob.coefficients(p).tolist(),a0=prob.metadata(p)['a0'],
                far_weight=.1,optimization_objective='W',jacobian_cl_relative_step=CL_STEP_DEFAULT,
                coefficient_order='old20_then_3delta_m0_m1_m2_m3' if new else 'original')

def hybrid_jac(prob,p,fun=None,cl_step=None):
    if cl_step is None:cl_step=CL_STEP_DEFAULT
    if len(p)==20:
        def raw(pp):
            if fun is None:return s.Problem.fun(prob,pp)
            fun(pp);return prob.last_raw
        return prob.root[:,None]*w.ORIGINAL_JAC(prob,p,raw,cl_step)
    mats,strain=prob.data(p[0]);c=prob.coefficients(p)
    ff={k:dot(M,c) for k,M in mats.items()}
    dc={k:M[:,1:]-M[:,:1]*strain[None,1:]/strain[0] for k,M in mats.items()}
    qm=mats['ratio']-strain[None,:];q=dot(qm,c)
    dq=qm[:,1:]-qm[:,:1]*strain[None,1:]/strain[0]
    wx=p[0]*prob.x-ff['psiy'];wy=p[0]*prob.y+ff['psix']
    a=wx*ff['fx'];b=wy*ff['fy'];d=q*ff['f']
    da=wx[:,None]*dc['fx']-ff['fx'][:,None]*dc['psiy']
    db=wy[:,None]*dc['fy']+ff['fy'][:,None]*dc['psix']
    dd=q[:,None]*dc['f']+ff['f'][:,None]*dq
    ww=(1+prob.x**2+prob.y**2)**((1/p[0]-1)/2)
    den=np.sqrt(a*a+b*b+d*d+(1e-8*ww)**2);res=(a+b+d)/den
    jc=(da+db+dd)/den[:,None]-res[:,None]*(a[:,None]*da+b[:,None]*db+d[:,None]*dd)/den[:,None]**2
    jc*=prob.root[:,None]
    # Release coefficient workspaces before cl probes rebuild the basis cache.
    del mats,dc,qm,dq,da,db,dd,ff
    h=cl_step*max(1,abs(p[0]));f=prob.fun if fun is None else fun
    values=[]
    for k in (2,1,-1,-2):
        pp=p.copy();pp[0]+=k*h;values.append(f(pp))
    jcl=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
    return np.column_stack([jcl,jc])

t.parameters=parameters;t.hybrid_jac=hybrid_jac
t.case_at=lambda p,prob,label='state':case_at(p,prob,49,label)
t.LOW=np.r_[1.02,np.full(23,-100.)];t.HIGH=np.r_[10.,np.full(23,100.)]

def field_design(prob,p,x,y):
    case=case_at(p,prob);items=s.basis(p[0],case['nm'],case['nk'],case['family'])
    mats=e.matrices(items,x,y)
    strain=np.array([e.evaluate(b['ratio'],[0],[0])[0] for b in items])
    result={k:M[:,1:]-M[:,:1]*strain[None,1:]/strain[0] for k,M in mats.items()}
    h=1e-4*max(1,abs(p[0]));values=[]
    for k in (2,1,-1,-2):
        pp=p.copy();pp[0]+=k*h;values.append(s.fields(case_at(pp,prob),x,y))
    for key in result:
        col=(-values[0][key]+8*values[1][key]-8*values[2][key]+values[3][key])/(12*h)
        result[key]=np.column_stack([col,result[key]])
    return s.fields(case,x,y),result

def scale_target(case,x,y,ff):
    items=s.basis(case['cl'],case['nm'],case['nk'],case['family'])
    terms=e.merged(items,case['coefficients'],'psi')
    pxx=e.evaluate(e.derivative(e.derivative(terms,0),0),x,y)
    pxy=e.evaluate(e.derivative(e.derivative(terms,0),1),x,y)
    pyy=e.evaluate(e.derivative(e.derivative(terms,1),1),x,y)
    return dict(f=-x*ff['fx']-y*ff['fy'],psix=ff['psix']-x*pxx-y*pxy,
                psiy=ff['psiy']-x*pxy-y*pyy)
t.field_design=field_design;t.scale_target=scale_target

def raw_values(case,x,y,batch=512):
    answer=np.empty(len(x));p=parameters(case)
    for lo in range(0,len(x),batch):
        hi=min(len(x),lo+batch)
        prob=Raw24(x[lo:hi],y[lo:hi]) if len(p)==24 else s.Problem(3,4,x[lo:hi],y[lo:hi],'fractional2',True)
        answer[lo:hi]=prob.fun(p)
    return answer
w.raw_values=raw_values

def nest(args):
    """Field and independent residual comparisons on every unchanged stored region."""
    base=load('baseline_'+args.basin);old=OldJointProblem(.1);p=parameters(base)
    assert np.array_equal(old.coefficients(p),base['coefficients'])
    new=JointProblem(.1);pp=np.r_[p,np.zeros(4)]
    embed=case_at(pp,new,label='embedded_'+args.basin);embed['basin']=args.basin
    assert embed['cl']==base['cl'] and embed['coefficients'][:20]==base['coefficients']
    assert embed['coefficients'][20:]==[0.]*4
    save('embedded_'+args.basin+'.json',embed)
    ro=old.fun(p);rn=new.fun(pp);assert np.array_equal(ro,rn)
    objects={'baseline':old.objectives(),'embedded':new.objectives()}
    coords=load('assessment_grids');design=load('grid_design');records={}
    for name,row in coords.items():
        bands=name.startswith('band_') or name in ('x_axis','y_axis','near_axis','near_origin','origin')
        if bands!=(args.part=='bands'):continue
        x,y=np.array(row['x']),np.array(row['y']);assert grid_record(x,y)==design[name]
        diffs={k:0. for k in ('f','fx','fy','psi','psix','psiy','ratio','rho')}
        for lo in range(0,len(x),512):
            xx,yy=x[lo:lo+512],y[lo:lo+512];a=s.fields(base,xx,yy);b=s.fields(embed,xx,yy)
            for k in a:diffs[k]=max(diffs[k],float(max(abs(a[k]-b[k]))))
            diffs['rho']=max(diffs['rho'],float(max(abs(yy*(a['f']-b['f'])))))
        da,db=diagnostic(base,x,y),diagnostic(embed,x,y)
        assert da==db and max(diffs.values())==0.,(name,diffs)
        records[name]={'field_max_abs_differences':diffs,'independent_residuals_identical':True}
        save('nest_'+args.basin+'_'+args.part+'.json',{'passed':False,'completed_regions':records})
    strain=s.fields(embed,[0],[0])['ratio'][0]
    save('nest_'+args.basin+'_'+args.part+'.json',{'passed':True,'objectives':objects,'residual_vector_bitwise':True,
         'old_physical_vector_bitwise':True,'new_coefficients_exact_zero':True,'center_defect':float(pp[0]+strain-1),'completed_regions':records})
    print('Strict nesting passed:',args.basin,args.part,len(records))

def setup(args):
    for basin in ('S0','B'):
        for part in ('main','bands'):assert load('nest_'+basin+'_'+part)['passed']
    case=load('embedded_'+args.basin);p=parameters(case);prob=JointProblem(.1);history=[]
    def counted(pp):
        r=prob.fun(pp);history.append({'evaluation':len(history)+1,'phase':'setup_jacobian_probe',
             'cost':float(r@r/2),**prob.metadata(pp),**prob.objectives()});return r
    J=hybrid_jac(prob,p,counted);counted(p);history[-1]['phase']='setup_residual'
    D=1/np.linalg.norm(J,axis=0)
    mapping=dict(anchor_parameters=p.tolist(),column_scale=D.tolist(),frozen=True,
                 setup_residual_calls=5,setup_jacobian_calls=1,setup_history=history)
    (ROOT/'inputs'/('map_'+args.basin+'_24.json')).write_text(json.dumps(mapping,indent=2))
    rec={}
    # Probe all coefficient columns separately; cl tests include nonzero NEW coefficients.
    for key,point in [('embedding',p),('nonzero_new',p+np.r_[np.zeros(20),[.017,-.013,.009,-.005]])]:
        jj=J if key=='embedding' else hybrid_jac(prob,point)
        errors=[]
        for k in range(1,24):
            h=1e-5*max(1,abs(point[k]));pp=point.copy();pm=point.copy();pp[k]+=h;pm[k]-=h
            fd=(prob.fun(pp)-prob.fun(pm))/(2*h)
            errors.append(float(np.linalg.norm(fd-jj[:,k])/np.linalg.norm(fd)))
        half=hybrid_jac(prob,point,cl_step=5e-5)
        errcl=float(np.linalg.norm(half[:,0]-jj[:,0])/np.linalg.norm(half[:,0]))
        direction=np.cos(np.arange(24)+.31);direction/=np.linalg.norm(direction);h=1e-6
        fd=(prob.fun(point+h*direction)-prob.fun(point-h*direction))/(2*h)
        emix=float(np.linalg.norm(fd-jj@direction)/np.linalg.norm(fd))
        rec[key]=dict(coefficient_relative_errors=errors,cl_step_relative_error=errcl,mixed_relative_error=emix)
        assert max(errors)<2e-4 and errcl<2e-5 and emix<2e-4,rec[key]
    save('setup_'+args.basin+'.json',dict(jacobian_verified=True,checks=rec,dimension=24,
                    frozen_map_reused_through_continuations=True,zero_origin_J_max=float(abs(J[:49]).max())))
    save('embedded_'+args.basin+'_initial_conditioning.json',conditioning(case,prob))
    print(json.dumps(rec,indent=2))

exec(compile((ROOT/'fit_impl.py').read_text(),str(ROOT/'fit_impl.py'),'exec'))
exec(compile((ROOT/'secondary_impl.py').read_text(),str(ROOT/'secondary_impl.py'),'exec'))

original_conditioning=conditioning
def conditioning(case,prob):
    result=original_conditioning(case,prob)
    p=parameters(case);J=hybrid_jac(prob,p)
    theta=np.r_[0,1e-6,.001,(np.arange(17)+.37)*np.pi/34,np.pi/2-.001,np.pi/2-1e-6,np.pi/2]
    x,y=s.polar(np.geomspace(.035,8,17),theta);x,y=np.r_[0.,x],np.r_[0.,y]
    ff,design=field_design(prob,p,x,y);rad=1+np.hypot(x,y)
    scale=max(1,abs(ff['f'][0]))*np.sqrt(3*len(x))
    B=np.vstack([design['f'],design['psix']/rad[:,None],design['psiy']/rad[:,None]])/scale
    ub,sb,vb=np.linalg.svd(B,full_matrices=False);F=vb.T/sb[None,:]
    _,sf,vf=np.linalg.svd(J@F,full_matrices=False)
    target=scale_target(case,x,y,ff)
    exact=np.r_[target['f'],target['psix']/rad,target['psiy']/rad]/scale
    weak=[]
    for k in (1,2,3):
        dp=F@vf[-k];bf=B@dp
        weak.append(dict(rank_from_smallest=k,parameters_per_unit_field=dp.tolist(),
             delta_cl=float(dp[0]),delta_a0=float(design['f'][0]@dp),
             physical_scale_cosine=float(abs(bf@exact)/np.linalg.norm(exact)),new_coefficients=dp[20:].tolist()))
    tangent_dp=np.linalg.lstsq(B,exact,rcond=None)[0]
    result.update(field_weak_directions=weak,field_design_singular_values=sb.tolist(),
          scaling_tangent_projection_relative_defect=float(np.linalg.norm(B@tangent_dp-exact)/np.linalg.norm(exact)),
          scaling_projection_delta_cl=float(tangent_dp[0]),scaling_projection_delta_a0=float(design['f'][0]@tangent_dp))
    if len(p)==24:
        uj,sj,_=np.linalg.svd(J[:,:20],full_matrices=False)
        new=J[:,20:];orth=new-uj@(uj.T@new)
        uf,sf0,_=np.linalg.svd(B[:,:20],full_matrices=False)
        bn=B[:,20:];borth=bn-uf@(uf.T@bn)
        result['new_columns']=dict(jacobian_relative_outside_old_span=(np.linalg.norm(orth,axis=0)/np.linalg.norm(new,axis=0)).tolist(),
            field_relative_outside_old_span=(np.linalg.norm(borth,axis=0)/np.linalg.norm(bn,axis=0)).tolist(),
            physical_gradient=result['physical_gradient'][20:],column_gradient=result['column_scaled_gradient'][20:])
    return result

def layer(args):
    case=load(args.label);assert len(case['coefficients'])==24
    c=np.array(case['coefficients']);items=s.basis(case['cl'],3,5,'fractional3')
    radii=[8,16,32,64,128,256,512];theta=np.array([0.,.07,.2,.45,.7,1.,1.3,np.pi/2])
    rows=[]
    for r in radii:
        x,y=s.polar([r],theta);mats=e.matrices(items,x,y)
        full={k:dot(M,c) for k,M in mats.items()}
        new={k:M[:,20:]@c[20:] for k,M in mats.items()}
        old={k:np.ascontiguousarray(M[:,:20])@c[:20] for k,M in mats.items()}
        mats['rho']=y[:,None]*mats['f']
        for values in (full,new,old):values['rho']=y*values['f']
        # Removing the new layer alone is a diagnostic decomposition, not an admissible refit.
        oldcase=dict(case,coefficients=np.r_[c[:20],np.zeros(4)].tolist())
        metrics={}
        for k in ('f','psi','psix','psiy','rho'):
            terms=mats[k]*c[None,:]
            metrics[k]=dict(full_angular_rms=float(np.sqrt(np.mean(full[k]**2))),
                 new_angular_rms=float(np.sqrt(np.mean(new[k]**2))),
                 new_over_full_L2=float(np.linalg.norm(new[k])/max(1e-30,np.linalg.norm(full[k]))),
                 sum_individual_norms_over_full=float(np.sum(np.linalg.norm(terms,axis=0))/max(1e-30,np.linalg.norm(full[k]))))
        rf=e.residual(case['cl'],full,x,y);rfo=e.residual(case['cl'],old,x,y)
        rows.append(dict(radius=r,fields=metrics,new_layer_coefficients=c[20:].tolist(),
                    full_Rf_RMS=float(np.sqrt(np.mean(rf**2))),without_new_layer_Rf_RMS=float(np.sqrt(np.mean(rfo**2))),
                    removal_breaks_center_identity=True))
    states=case.get('accepted_states',[])
    tail=[q for q in states if q.get('event')=='accepted'][-5:]
    span=np.ptp(np.array([q['parameters'][20:] for q in tail]),axis=0).tolist() if tail else None
    # Center-compensated removal is admissible and isolates the new four coefficients at fixed old free entries.
    p=parameters(case);pp=p.copy();pp[20:]=0;prob=JointProblem(.1)
    prob.fun(p);obj=prob.objectives();prob.fun(pp);removed=prob.objectives()
    source=[(co,a,b+1,powr) for co,a,b,powr in e.merged(items,c,'fx')]
    aa=[];bb=[]
    for n,terms in e.modal_source(source).items():
        for (degree,powr),amplitude in terms.items():
            aa.append(-powr-(degree+2-n)/2);bb.append((degree+2-n)/2)
    assert min(aa)>0 and min(bb)>0
    save(args.label+'_layer.json',dict(coefficients=c[20:].tolist(),last_five_new_coefficient_spans=span,
        radii=rows,representative_angles=theta.tolist(),objective_full=obj,objective_center_compensated_removal=removed,
        canonical_beta_min_a=min(aa),canonical_beta_min_b=min(bb),tail_density_degree=4/case['cl']-3,
        physical_vector_sha256=fingerprint(case),
        note='Diagnostic removals are not separately optimized; coefficient norm is not physical significance.'))

def validate_setup(args):
    case=load(args.label);prob=problem_for(case);p=parameters(case);count=[0];jc=[0]
    def fun(pp):count[0]+=1;return prob.fun(pp)
    def jac(step):jc[0]+=1;return hybrid_jac(prob,p,fun,cl_step=step)
    J=jac(CL_STEP_DEFAULT);r=fun(p);D=1/np.linalg.norm(J,axis=0)
    _,sv,vt=np.linalg.svd(J*D,full_matrices=False);P=D[:,None]*vt.T/sv[None,:]
    g=P.T@(J.T@r);metrics=[]
    for step in (2e-4,1e-4,5e-5,2.5e-5):
        ja=jac(step);ga=P.T@(ja.T@r)
        metrics.append(dict(cl_relative_step=step,whitened_gradient_norm=float(np.linalg.norm(ga)),gradient_change_norm=float(np.linalg.norm(ga-g))))
    dp=-P@g;cost=float(r@r/2);probes=[]
    for factor in (1.,.5,.25,.1,.01,.001,.0001,-.001):
        pp=p+factor*dp
        if np.all(pp>t.LOW[:len(p)]) and np.all(pp<t.HIGH[:len(p)]):
            rr=fun(pp);probes.append(dict(factor=factor,cost=float(rr@rr/2),cost_change=float(rr@rr/2-cost),
                 cl_change=float(factor*dp[0]),physical_step_norm=float(np.linalg.norm(factor*dp))))
    fp=fingerprint(case)
    np.savez_compressed(OUT/(args.label+'_validation_arrays.npz'),r=r,J=J,P=P,g=g)
    result=dict(cost=cost,hybrid_whitened_gradient_norm=float(np.linalg.norm(g)),
         relative_projected_residual=float(np.linalg.norm(g)/np.linalg.norm(r)),predicted_GN_cost_decrease=float(g@g/2),
         GN_parameter_step=dp.tolist(),cl_column_sensitivity=metrics,GN_trial_probes=probes,
         actual_residual_calls=count[0],jacobian_calls=jc[0],diagnostic_coordinate_map=P.tolist(),
         physical_vector_sha256=fp,dimension=len(p),jacobian_cl_relative_step=CL_STEP_DEFAULT)
    save(args.label+'_validation_setup.json',result)
    print(json.dumps({k:result[k] for k in ['relative_projected_residual','actual_residual_calls','predicted_GN_cost_decrease']}))

def validate_batch(args):
    case=load(args.label);setup=load(args.label+'_validation_setup');assert setup['physical_vector_sha256']==fingerprint(case)
    prob=problem_for(case);p=parameters(case);arrays=np.load(OUT/(args.label+'_validation_arrays.npz'))
    r,J,P,g=(arrays[k] for k in ['r','J','P','g']);rows=[];calls=0
    path=OUT/(args.label+'_validation_batch'+str(args.batch)+'.json')
    if path.exists():
        previous=json.loads(path.read_text())
        if previous['physical_vector_sha256']==fingerprint(case):rows=previous['rows'];calls=previous['actual_residual_calls']
    for k in range(args.batch*6,min(len(p),(args.batch+1)*6)):
        direction=P[:,k]
        for physical in (1e-3,5e-4):
            if any(q['direction']==k and q['physical_direction_step']==physical for q in rows):continue
            h=physical/np.linalg.norm(direction);values=[]
            for a in (2,1,-1,-2):
                values.append(prob.fun(p+a*h*direction));calls+=1
            df=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h)
            cv=[float(q@q/2) for q in values]
            rows.append(dict(direction=k,physical_direction_step=physical,fd_gradient_component=float(df@r),
                 fd_cost_gradient_component=(-cv[0]+8*cv[1]-8*cv[2]+cv[3])/(12*h),
                 sampled_coordinate_curvature=(cv[1]-2*setup['cost']+cv[2])/h**2,Jv_absolute_error=float(np.linalg.norm(df-J@direction))))
            save(args.label+'_validation_batch'+str(args.batch)+'.json',dict(physical_vector_sha256=fingerprint(case),rows=rows,actual_residual_calls=calls))
    print('Completed independent gradient batch',args.batch,'calls',calls)

def validate_finish(args):
    case=load(args.label);result=load(args.label+'_validation_setup');fp=fingerprint(case)
    assert result['physical_vector_sha256']==fp
    arrays=np.load(OUT/(args.label+'_validation_arrays.npz'));r,J,P,g=(arrays[k] for k in ['r','J','P','g'])
    batches=[load(args.label+'_validation_batch'+str(k)) for k in range((len(parameters(case))+5)//6)]
    assert all(q['physical_vector_sha256']==fp for q in batches)
    rows=[]
    for physical in (1e-3,5e-4):
        checks=sorted([q for b in batches for q in b['rows'] if q['physical_direction_step']==physical],key=lambda q:q['direction'])
        assert [q['direction'] for q in checks]==list(range(result['dimension']))
        fdg=np.array([q['fd_gradient_component'] for q in checks])
        rows.append(dict(physical_direction_step=physical,whitened_gradient_norm_from_fd_residuals=float(np.linalg.norm(fdg)),
             fd_gradient_change_norm=float(np.linalg.norm(fdg-g)),fd_cost_gradient_norm=float(np.linalg.norm([q['fd_cost_gradient_component'] for q in checks])),
             fd_cost_gradient_components=[q['fd_cost_gradient_component'] for q in checks],fd_gradient_components=fdg.tolist(),
             Jv_absolute_errors=[q['Jv_absolute_error'] for q in checks],sampled_coordinate_curvatures=[q['sampled_coordinate_curvature'] for q in checks]))
    result['independent_directional_checks']=rows
    result['actual_residual_calls']+=sum(q['actual_residual_calls'] for q in batches)
    if result['dimension']==24:
        prob=problem_for(case);p=parameters(case);records=[]
        for rel in (1e-4,5e-5):
            grad=[]
            for k in range(20,24):
                h=rel*max(1,abs(p[k]));values=[]
                for a in (2,1,-1,-2):
                    pp=p.copy();pp[k]+=a*h;values.append(prob.fun(pp))
                df=(-values[0]+8*values[1]-8*values[2]+values[3])/(12*h);grad.append(float(df@r))
            records.append(dict(relative_parameter_step=rel,physical_gradient=grad,column_gradient=(np.array(grad)/np.linalg.norm(J[:,20:],axis=0)).tolist(),actual_residual_calls=16))
        result['new_coefficient_independent_gradients']=records;result['actual_residual_calls']+=32
    save(args.label+'_stationarity.json',result)
    print(json.dumps({'relative_projected_residual':result['relative_projected_residual'],
       'FD_relative_projected_residual':[q['whitened_gradient_norm_from_fd_residuals']/np.linalg.norm(r) for q in rows],
       'actual_residual_calls':result['actual_residual_calls']}))

def cl_accuracy(args):
    case=load(args.label);p=parameters(case);prob=problem_for(case)
    setup=load(args.label+'_validation_setup');assert setup['physical_vector_sha256']==fingerprint(case)
    arrays=np.load(OUT/(args.label+'_validation_arrays.npz'));P=arrays['P'];r=arrays['r'];norm=np.linalg.norm(r)
    checked=load(args.label+'_stationarity')
    fd=np.array(checked['independent_directional_checks'][-1]['fd_gradient_components'])
    rows=[];columns=[];previous=None
    for step in (5e-5,2.5e-5,1.25e-5,6.25e-6,3.125e-6):
        J=hybrid_jac(prob,p,cl_step=step);g=P.T@(J.T@r);columns.append(J[:,0].copy())
        raw=np.linalg.svd(J,compute_uv=False);eq=np.linalg.svd(J/np.linalg.norm(J,axis=0),compute_uv=False)
        rows.append(dict(cl_relative_step=step,relative_projected_residual=float(np.linalg.norm(g)/norm),
             gradient_difference_from_independent=float(np.linalg.norm(g-fd)/norm),
             gradient_change_from_previous=float(np.linalg.norm(g-previous)/norm) if previous is not None else None,
             raw_condition=float(raw[0]/raw[-1]),column_condition=float(eq[0]/eq[-1])))
        previous=g
    rich=[]
    for k in range(len(columns)-1):
        JJ=J.copy();JJ[:,0]=(16*columns[k+1]-columns[k])/15;g=P.T@(JJ.T@r)
        rich.append(dict(coarse_relative_step=rows[k]['cl_relative_step'],fine_relative_step=rows[k+1]['cl_relative_step'],
             gradient_difference_from_independent=float(np.linalg.norm(g-fd)/norm),relative_projected_residual=float(np.linalg.norm(g)/norm)))
    save(args.label+'_cl_accuracy.json',dict(physical_vector_sha256=fingerprint(case),steps=rows,richardson=rich,
         actual_residual_calls=20,jacobian_calls=5,metric='fixed original validation P; independent residual differences at physical step .0005'))
    print(json.dumps({'steps':rows,'richardson':rich},indent=2))

def map_check(args):
    case=load(args.label);mapping=case['mapping'];anchor=np.array(mapping['anchor_parameters'])
    q=np.array(case['coordinate_vector']);p=parameters(case);rows=[]
    for order in ('C','F'):
        F=np.array(mapping['full_coordinate_map'],order=order);recovered=anchor+F@q
        rows.append(dict(order=order,bitwise_physical_vector_equal=bool(np.array_equal(recovered,p)),
                         max_parameter_difference=float(max(abs(recovered-p)))))
    result=dict(physical_vector_sha256=fingerprint(case),checks=rows)
    if args.label=='B_secondary':
        base=load('B_primary');assert np.array_equal(anchor,parameters(base))
        arrays=np.load(OUT/'B_24_validation_arrays.npz');J=arrays['J'];P=arrays['P'];r=arrays['r']
        F=np.array(mapping['full_coordinate_map'],order='F');sv=np.linalg.svd(J@F,compute_uv=False)
        accurate=hybrid_jac(problem_for(base),parameters(base),cl_step=6.25e-6)
        checked=load('B_24_stationarity');fd=np.array(checked['independent_directional_checks'][-1]['fd_gradient_components'])
        transform=np.linalg.solve(P,F);gfd=transform.T@fd/mapping['cost_scale']
        g=F.T@(accurate.T@r)/mapping['cost_scale']
        result['anchor_coordinate_check']=dict(mapped_J_condition=float(sv[0]/sv[-1]),
             normalized_objective_gradient_relative_error=float(np.linalg.norm(g-gfd)/np.linalg.norm(gfd)),
             full_map_condition=float(np.linalg.cond(F)),all_singular_directions_retained=True,
             accurate_cl_relative_step=6.25e-6)
    save(args.label+'_map_layout_check.json',result)
    print(json.dumps(result))

def main():
    global CL_STEP_DEFAULT
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['nest','setup','fit','secondary','assess','cross','independent','analyze','validate_setup','validate_batch','validate_finish','cl_accuracy','map_check','compare','layer'])
    parser.add_argument('--label',default='trial');parser.add_argument('--candidate',default='S0_24')
    parser.add_argument('--basin',choices=['S0','B'],default='S0');parser.add_argument('--weight',type=float,choices=[.1],default=.1)
    parser.add_argument('--initial',default='embedded_S0');parser.add_argument('--calls',type=int,default=180)
    parser.add_argument('--resume');parser.add_argument('--grid',type=int,choices=[49],default=49)
    parser.add_argument('--objective',choices=['W'],default='W');parser.add_argument('--part',choices=['main','bands'],default='main')
    parser.add_argument('--batch',type=int,choices=[0,1,2,3],default=0)
    parser.add_argument('--cl-step',type=float,choices=[1e-4,5e-5,2.5e-5,1.25e-5,6.25e-6,3.125e-6],default=1e-4)
    args=parser.parse_args()
    CL_STEP_DEFAULT=args.cl_step
    if '--cl-step' not in sys.argv and args.mode in ('assess','cross','independent','analyze','validate_setup','validate_batch','validate_finish','compare','layer'):
        CL_STEP_DEFAULT=load(args.label).get('jacobian_cl_relative_step',1e-4)
    try:
        with threadpool_limits(limits=1):globals()[args.mode](args)
    finally:
        use=resource.getrusage(resource.RUSAGE_SELF)
        save(args.mode+'_'+args.label+'_process.json',dict(peak_rss_mib=peak_rss_mib(use),cpu_seconds=use.ru_utime+use.ru_stime,
               threads_at_exit=psutil.Process().num_threads(),nice=psutil.Process().nice(),threadpools=threadpool_info()))

if __name__=='__main__':main()

