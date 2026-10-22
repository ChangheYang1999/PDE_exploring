"""Independent validated JSON import and raw generating function with all core terms.

No fitter code is imported. Binary64 data are exact dyadic coefficients.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import numpy as np
import mpmath as mp

ALLOWED=set('c a0 J Kw m beta hist Nt Ns tmin gauge alpha se gam l gpu_port init nmin n2 cc core fixa0 lam lam0 inner'.split())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rat(v):return str(F(float(v)))
def number(v):
    q=F(v);return mp.mpf(q.numerator)/q.denominator

def export_source(source,destination):
    source=Path(source)
    with np.load(source,allow_pickle=False) as z:
        if set(z.files)-ALLOWED:raise ValueError(('unknown keys',set(z.files)-ALLOWED))
        for key in ('m','J','Kw'):
            if z[key].shape!=() or z[key].dtype!=np.dtype('int64'):raise ValueError(('expected scalar int64',key))
        for key in ('beta','gam'):
            if z[key].shape!=() or z[key].dtype!=np.dtype('float64') or not np.isfinite(z[key]):raise ValueError(('expected finite scalar binary64',key))
        if int(z['m'])!=3 or float(z['beta'])!=3 or float(z['gam'])!=0 or float(z['alpha'])<=0:raise ValueError('unsupported beta/alpha/angular map')
        for key in ('c','a0','se','alpha')+tuple(k for k in ('cc','core') if k in z.files):
            if z[key].dtype!=np.dtype('float64') or not np.isfinite(z[key]).all():raise ValueError(('not finite binary64',key))
        J,K=int(z['J']),int(z['Kw'])
        if J<0 or K<0 or z['c'].shape!=((J+1)*(K+1),):raise ValueError('outer layout')
        c=z['c'].reshape(J+1,K+1)
        result={'source':str(source),'source_sha256':sha(source),'schema':'beta3 alpha-positive gam0 exact dyadic generating function; n/k outer; patch/i/j core',
                's':rat(z['se']),'alpha':rat(z['alpha']),'a':rat(z['a0']),'outer':[[rat(v) for v in row] for row in c],'patches':[]}
        if F(result['s'])<=0:raise ValueError('nonpositive scale')
        if ('cc' in z.files)!=('core' in z.files):raise ValueError('incomplete core schema')
        if 'core' in z.files:
            if z['core'].ndim!=2 or z['core'].shape[1]!=4 or z['cc'].ndim!=1:raise ValueError('core layout')
            offset=0
            for n,m,R,L in z['core']:
                if n!=int(n) or m!=int(m) or n<0 or m<0 or R<=0 or L<=0:raise ValueError('core parameters')
                n,m=int(n),int(m);count=(n+1)*(m+1)
                if offset+count>len(z['cc']):raise ValueError('too few core coefficients')
                cc=z['cc'][offset:offset+count].reshape(n+1,m+1);offset+=count
                result['patches'].append({'R':rat(R),'L':rat(L),'coefficients':[[rat(v) for v in row] for row in cc]})
            if offset!=len(z['cc']):raise ValueError('unused core coefficients')
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,indent=2)+'\n')
    return result

def recurrence(z,n):
    out=[mp.mpf(1)]
    if n>1:out.append(z)
    for _ in range(2,n):out.append(2*z*out[-1]-out[-2])
    return out

def series(coeff,t,w):
    tt,ww=recurrence(2*t-1,len(coeff)),recurrence(2*w-1,len(coeff[0]))
    return mp.fsum(mp.fsum(row[j]*ww[j] for j in range(len(row)))*tt[i] for i,row in enumerate(coeff))

def from_data(data):
    s,alpha,a=[number(data[k]) for k in ('s','alpha','a')]
    if s<=0 or alpha<=0:raise ValueError('positive parameters required')
    def rows(raw):
        if not raw or not raw[0] or any(len(r)!=len(raw[0]) for r in raw):raise ValueError('nonrectangular coefficients')
        return [[number(v) for v in row] for row in raw]
    c=rows(data['outer']);patches=[]
    for d in data['patches']:
        R,L=number(d['R']),number(d['L'])
        if R<=0 or L<=0:raise ValueError('positive patch scales required')
        patches.append((R,L,rows(d['coefficients'])))
    def G(x,e):
        E=1+x*x+(e/s)**6
        t=-mp.log1p(mp.expm1(-alpha)*E**(-mp.mpf(1)/6))/alpha
        w=(e/s)**2*E**(-mp.mpf(1)/3)
        p=series(c,t,w)
        for R,L,cc in patches:
            u=x*x/(R*R+x*x);v=e*e/(R*R+e*e)
            p+=mp.exp(-(x*x+e*e)/(L*L))*series(cc,u,v)
        return x*e*E**(mp.mpf(1)/3)*p
    return G,a

def load_json(path):return from_data(json.loads(Path(path).read_text()))

def endpoint_data(data):
    c=[[F(q) for q in r] for r in data['outer']]
    H=sum((v*(-1)**k for row in c for k,v in enumerate(row)),F(0))
    Pt=sum((v*2*n*n*(-1)**k for n,row in enumerate(c) for k,v in enumerate(row)),F(0))
    Pw=sum((v*(-2)*k*k*(-1)**k for row in c for k,v in enumerate(row)),F(0))
    core=[]
    for p in data['patches']:
        cc=[[F(q) for q in r] for r in p['coefficients']]
        q0=sum((v*(-1)**(i+j) for i,row in enumerate(cc) for j,v in enumerate(row)),F(0))
        qu=sum((-2*i*i*v*(-1)**(i+j) for i,row in enumerate(cc) for j,v in enumerate(row)),F(0))
        qv=sum((-2*j*j*v*(-1)**(i+j) for i,row in enumerate(cc) for j,v in enumerate(row)),F(0))
        core.append({'q0':str(q0),'qu':str(qu),'qv':str(qv),'R':p['R'],'L':p['L']})
    return {'H':str(H),'Pt':str(Pt),'Pw':str(Pw),'patches':core,'s':data['s'],'alpha':data['alpha'],'a':data['a']}
