"""Exact rational first-correction polynomial for the saved L=1 states.

Interprets binary coefficient values exactly, beta=2 or3 exactly, and repairs
only the envelope exponents to the intended exact formulas. No interval
arithmetic is needed for the finite rational trigonometric identity.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from profile_data import CoefficientProfile
from far_coefficients import evaluate


def add_sin(dst,n,v):
    if n<0:n=-n;v=-v
    if n and v:dst[n]=dst.get(n,F(0))+v

def sin_cos(s,c):
    out={}
    for n,a in s.items():
        for m,b in c.items():
            add_sin(out,n+m,a*b/2);add_sin(out,n-m,a*b/2)
    return {n:v for n,v in out.items() if v}

def linear(*terms):
    out={}
    for scale,p in terms:
        for n,v in p.items():add_sin(out,n,scale*v)
    return {n:v for n,v in out.items() if v}

def endpoint(c,first=False):
    return {2*l:sum((F.from_float(float(v))*((-1)**n)*(-2*n*n if first else 1)
                      for n,v in enumerate(row)),F(0)) for l,row in enumerate(c)}

def encode(p):return {str(n):{'numerator':str(v.numerator),'denominator':str(v.denominator)} for n,v in sorted(p.items())}

def main():
    start=time.monotonic();rows=[]
    for tag in ['published_gauss_N112','published_gauss_N144','published_gauss_N176','published_beta2_N112']:
        path=Path('data/control_snapshots')/(tag+'.npz');obj=CoefficientProfile(path)
        if obj.length!=1 or obj.mapname!='t' or obj.beta_map!=obj.beta or obj.beta not in [2,3]:
            raise ValueError('This exact certificate is only for L1 t-map beta2/3')
        beta=F.from_float(obj.beta);d=1/beta;q=1-2*d;alpha=2-d
        tb={1:F(1,4),3:F(1,4)};ob={2:F(1,2)}
        t0=sin_cos(tb,endpoint(obj.ca));t1=sin_cos(tb,endpoint(obj.ca,True))
        o0=sin_cos(ob,endpoint(obj.cg));o1=sin_cos(ob,endpoint(obj.cg,True))
        psi={n:v/(n*n-alpha*alpha) for n,v in o0.items()}
        ur={n:-n*v for n,v in psi.items()};up={n:alpha*v for n,v in psi.items()}
        tp={n:n*v for n,v in t0.items()};op={n:n*v for n,v in o0.items()}
        dt=linear((q,sin_cos(t0,ur)),(F(1),sin_cos(up,tp)),(F(-1),t1))
        do=linear((-d,sin_cos(o0,ur)),(F(1),sin_cos(up,op)),(-q,sin_cos(t0,{1:F(1)})),(F(1),sin_cos({1:F(1)},tp)),(F(-1),o1))
        cert={}
        for label,p in [('thermal',dt),('vorticity',do)]:
            if not p:raise AssertionError('Polynomial unexpectedly vanishes')
            n=max(p,key=lambda n:abs(p[n]));v=p[n];bound=F(3,4)*abs(v)
            # pi>3 and |a_n| <= (4/pi)||p||_infinity give this exact lower bound.
            cert[label]={'sine_coefficients':encode(p),'largest_coefficient_frequency':n,
                'largest_coefficient':{'numerator':str(v.numerator),'denominator':str(v.denominator)},
                'sup_lower_bound_rational':{'numerator':str(bound.numerator),'denominator':str(bound.denominator)},
                'sup_lower_bound_decimal_approximation':float(bound),
                'nonzero':True}
        angles=np.array([.13,.6,1.25]);vf=evaluate(obj,angles)
        maxdiff={}
        for label,p,key in [('thermal',dt,'D_T'),('vorticity',do,'D_O')]:
            vals=np.array([sum(float(v)*np.sin(n*a) for n,v in p.items()) for a in angles])
            maxdiff[label]=float(np.max(abs(vals-vf[key])))
        rows.append({'tag':tag,'snapshot_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                     'beta_exact':str(beta),'metadata':obj.metadata(),'certificates':cert,
                     'floating_crosscheck_angles':angles.tolist(),'floating_crosscheck_max_difference':maxdiff})
    result={'timestamp':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
        'interpretation':'Binary ca,cG exact; L1 and beta2/3 exact; envelope sigma_a=1+1/beta,sigma_G=1+1/(2beta) exact intended powers, not their binary rounded NPZ values.',
        'method':'Fraction arithmetic, independently multiplied finite sine/cosine polynomials; nonzero exact first-correction mismatch',
        'bound_proof':'For sine coefficient a_n, |a_n|<=4||D||_infty/pi, hence ||D||_infty>3|a_n|/4 when a_n!=0.',
        'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path('runs/tail_rational_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'timestamp':result['timestamp'],'elapsed_seconds':result['elapsed_seconds'],
        'rows':[{'tag':x['tag'],'bounds':{k:v['sup_lower_bound_decimal_approximation'] for k,v in x['certificates'].items()},
        'max_difference':x['floating_crosscheck_max_difference']} for x in rows]},indent=2))
if __name__=='__main__':main()
