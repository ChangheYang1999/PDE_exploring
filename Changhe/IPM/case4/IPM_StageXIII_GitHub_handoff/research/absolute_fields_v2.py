"""Versioned origin-order20 evaluation of the unchanged analytic potential.

All coefficients, modes, unrounded exponents, center identity and PDE remain
identical to v1. Only the Taylor truncation order at r<=.02 is increased from
12 to20, consistently for every field, residual and full raw derivative.
"""
from absolute_fields import (np,KEYS,CORE_ORDER,prepare_candidate,center_data,
    core_matrices,_assemble,_falling,_core_exponents,_offsets,_decimal_center)
from absolute_fields import fields as fields_v1,residual as residual_v1
from highprecision_origin import field_series,residual_series,evaluate_series

ORIGIN_ORDER=20
ORIGIN_RADIUS=.02


def fields(prepared,x,y,derivatives=False,block_size=2048):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.ravel();y=y.ravel()
    small=np.hypot(x,y)<=ORIGIN_RADIUS;large=~small;columns=24+len(prepared['extra'])
    out={key:np.empty(len(x)) for key in KEYS+('q',)}
    dout={key:np.empty((len(x),columns)) for key in out} if derivatives else None
    if np.any(large):
        value=fields_v1(prepared,x[large],y[large],derivatives,block_size)
        ff,df=value if derivatives else (value,None)
        for key in out:
            out[key][large]=ff[key]
            if derivatives:dout[key][large]=df[key]
    if np.any(small):
        series=field_series(prepared,order=ORIGIN_ORDER,derivatives=derivatives)
        for key in out:
            out[key][small]=evaluate_series(series['fields'][key],x[small],y[small])
            if derivatives:
                for column,poly in enumerate(series['derivatives'][key]):
                    dout[key][small,column]=evaluate_series(poly,x[small],y[small])
    return (out,dout) if derivatives else out


def residual(prepared,x,y,derivatives=False):
    x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));x=x.ravel();y=y.ravel()
    small=np.hypot(x,y)<=ORIGIN_RADIUS;large=~small
    result=np.empty(len(x));jacobian=np.empty((len(x),24+len(prepared['extra']))) if derivatives else None
    if np.any(large):
        value=residual_v1(prepared,x[large],y[large],derivatives)
        rr,jj=value if derivatives else (value,None)
        result[large]=rr
        if derivatives:jacobian[large]=jj
    if np.any(small):
        series=residual_series(prepared,order=ORIGIN_ORDER,derivatives=derivatives)
        result[small]=evaluate_series(series['residual'],x[small],y[small])
        if derivatives:
            for column,poly in enumerate(series['derivatives']):
                jacobian[small,column]=evaluate_series(poly,x[small],y[small])
    return (result,jacobian) if derivatives else result


def exact_dilation_fields(prepared,x,y,factor,derivatives=False):
    factor=float(factor)
    if not factor>0:raise ValueError('Positive exact dilation required')
    value=fields(prepared,np.asarray(x)/factor,np.asarray(y)/factor,derivatives)
    ff,df=value if derivatives else (value,None)
    multipliers={'f':1.,'fx':1/factor,'fy':1/factor,'psi':factor*factor,
        'psix':factor,'psiy':factor,'ratio':1.,'q':1.}
    ff={key:array*multipliers[key] for key,array in ff.items()}
    if derivatives:df={key:array*multipliers[key] for key,array in df.items()}
    return (ff,df) if derivatives else ff
