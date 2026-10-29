"""Replace only the first explicit exterior correction for an operator experiment.

This operation generally breaks matching and is never an acceptance repair.
"""
import json
import numpy as np
from numpy.polynomial import Polynomial as Poly,Legendre
from scipy.special import roots_legendre
from independent_farfield import angular_data,evaluate_vector
from angular_tail_projection import project


def first_correction_polynomials(alpha,A,B,degree=None,nangle=128):
    if not 1/3<alpha<1:raise ValueError('open main interval required')
    data=angular_data(alpha,A,B)
    if degree is None:
        return data['A1'],data['B1'],dict(method='full polynomial correction',degree_A=data['A1'].degree(),degree_B=data['B1'].degree())
    if degree<0:raise ValueError('nonnegative correction degree required')
    mu,w=roots_legendre(nangle)
    p=project(2*alpha+1,mu,w,evaluate_vector(data,mu,'G'),degree,degree)
    out=[]
    for key in ['A','B']:
        # C_j^(3/2) = P_(j+1)'. The derivative is taken in Legendre form.
        leg=Legendre([0.])
        for j,c in enumerate(p['projection_'+key+'_gegenbauer']):leg+=c*Legendre.basis(j+1).deriv()
        out.append(leg.convert(kind=Poly))
    return *out,dict(method='velocity-L2 projection at fixed leading tail',quadrature=nangle,projection=p)


def replace_first_correction(field,degree=None,nangle=128):
    A,B=field.leading_polynomials();p=2*field.alpha+1
    A1,B1,info=first_correction_polynomials(field.alpha,A,B,degree,nangle)
    meta=json.loads(json.dumps(field.metadata));e=meta['elements'][2]
    coeff={k:v.copy() for k,v in field.coefficients.items()}
    old_nmax=int(e['nmax']);new_nmax=max(old_nmax,A1.degree(),B1.degree())
    exponents=set();labels_by={}
    for key,target,power in [('phi',A1,p),('q',B1,p+1)]:
        old_labels=e.get('labels_'+key,e['labels'])
        old={(int(n),float(k)):float(v) for (n,k),v in zip(old_labels,field.coefficients[key+'_el2'])}
        powers=sorted({float(k) for n,k in old_labels if abs(k-power)>=1e-10}|{power})
        labels=[(n,k) for n in range(new_nmax+1) for k in powers]
        leg=target.convert(kind=Legendre).coef
        factor=float(e['Rlo'])**power*field.dilation**(power+(key=='phi'))
        values=[]
        for n,k in labels:
            if abs(k-power)<1e-10:values.append(float(leg[n]/factor) if n<len(leg) else 0.)
            else:values.append(old.get((n,k),0.))
        coeff[key+'_el2']=np.asarray(values,dtype=np.float64)
        labels_by[key]=labels;exponents.update(powers)
    e['nmax']=new_nmax;e['exponents']=sorted(exponents)
    e['labels']=[(n,k) for n in range(new_nmax+1) for k in sorted(exponents)]
    index={label:i for i,label in enumerate(e['labels'])}
    for key,labels in labels_by.items():
        e['labels_'+key]=labels;e[key+'_cols']=[index[t] for t in labels]
    provenance=dict(field.provenance)
    provenance['operator_experiment']='Only exterior first correction replaced. Matching generally fails. Not an Euler candidate.'
    new=type(field)(meta,coeff,dilation=field.dilation,provenance=provenance)
    info.update(old_nmax=old_nmax,new_nmax=new_nmax,correction_power=p)
    return new,info
