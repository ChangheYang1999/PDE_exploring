#!/usr/bin/env python3
"""Independent finite integer-beta Green inverse; no fitting-code imports."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import numpy as np
ROOT=Path(__file__).resolve().parent
HELPER=ROOT.parent/'beta2_closed_form/exact_inverse.py'
spec=importlib.util.spec_from_file_location('own_polynomials87',HELPER)
poly=importlib.util.module_from_spec(spec);spec.loader.exec_module(poly)
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dec(x):return mp.nstr(x,65)
def strings(row):return {k:None if v is None else dec(v) for k,v in row.items()}
def qmul(a,p,b):
    out=[0]*(len(a)+2*b*p)
    for j in range(p+1):
        fac=(-1)**j*math.comb(p,j)
        for k,x in enumerate(a):out[k+2*b*j]+=fac*x
    return poly.trim(out)
def compiler(ca,cg,b):
    if type(b) is not int or b<2:raise ValueError('integer beta>=2')
    if ca.ndim!=2 or ca.shape!=cg.shape or min(ca.shape)<1:raise ValueError('shapes')
    if any(ar.dtype.kind!='f' or ar.dtype.itemsize!=8 or not np.isfinite(ar).all() for ar in(ca,cg)):raise ValueError('finite binary64')
    M,N=ca.shape;D=max(float(x).as_integer_ratio()[1] for ar in(ca,cg) for x in ar.flat);ts=poly.cheb_shifted(N)
    def rows(ar):
        result=[]
        for row in ar:
            p=[0]*N
            for x,T in zip(row,ts):
                u,v=float(x).as_integer_ratio();w=u*(D//v)
                for j,y in enumerate(T):p[j]+=w*y
            result.append(poly.trim(p))
        return result
    ap,cp=rows(ca),rows(cg);modes=[]
    for k in range(1,M+1):
        a=cp[k-1];c=cp[k+1] if k+1<M else[0];f=2 if k==1 else 1
        P=[b*x for x in poly.add([f*x for x in qmul(a,2*k,b)],qmul(c,2*k+2,b),-1)]
        Q=[b*x for x in poly.add([f*x for x in a],qmul(c,2,b),-1)]
        L=2*b*(k+1)-1;J=2*b*(k-1)+1
        moment=sum((Fraction(x,j-L) for j,x in enumerate(P) if j!=L),Fraction())
        modes.append({'k':k,'L':L,'J':J,'P':P,'Q':Q,'moment':[moment.numerator,moment.denominator]})
    return {'beta':b,'M':M,'N':N,'denominator':D,'A':ap,'C':cp,'modes':modes}
def radial(comp,t):
    t=mp.mpf(t)
    if not(0<t<1):raise ValueError('Use0<t<1; exact moment handles origin')
    b=comp['beta'];q=1-t**(2*b);qp=-2*b*t**(2*b-1);D=comp['denominator']
    out={'t':t,'q':q,'A':[],'At':[],'C':[],'Ct':[],'X':[],'Y':[]}
    for name in('A','C'):
        for m,coefs in enumerate(comp[name]):
            a,at=poly.horner_pair(coefs,t);a/=D;at/=D
            out[name].append(q**m*a);out[name+'t'].append(q**m*(at+m*qp/q*a))
    for mode in comp['modes']:
        k,L,J=mode['k'],mode['L'],mode['J'];P,Q=mode['P'],mode['Q'];u,v=mode['moment']
        icoef=[-mp.mpf(x)/(j-L) if j!=L else mp.mpf(0) for j,x in enumerate(P)]
        ibar=mp.polyval(list(reversed(icoef)),t)+t**L*mp.mpf(u)/v
        if L<len(P):ibar-=P[L]*t**L*mp.log(t)
        obar=mp.polyval([mp.mpf(Q[j])/(j+J) for j in reversed(range(len(Q)))],t)
        out['X'].append(q**(-k)*ibar/(4*D));out['Y'].append(q**k*obar/(4*D))
    return out
def polar(comp,r,phi):
    b=comp['beta'];r=mp.mpf(r);phi=mp.mpf(phi);t=(1+r*r)**(-mp.mpf(1)/(2*b));v=radial(comp,t)
    psi=mp.fsum((x+y)*mp.sin(2*(j+1)*phi)/(4*(j+1)) for j,(x,y) in enumerate(zip(v['X'],v['Y'])))*t**(1-2*b)
    ur=-mp.fsum((x+y)*mp.cos(2*(j+1)*phi) for j,(x,y) in enumerate(zip(v['X'],v['Y'])))*t**(1-b)/(2*mp.sqrt(v['q']))
    up=mp.fsum((-x+y)*mp.sin(2*(j+1)*phi) for j,(x,y) in enumerate(zip(v['X'],v['Y'])))*t**(1-b)/(2*mp.sqrt(v['q']))
    return psi,ur,up

def cartesian(comp,x,y):
    b=comp['beta'];x,y=mp.mpf(x),mp.mpf(y);r2=x*x+y*y
    if not r2:raise ValueError('Use exact origin moment')
    r=mp.sqrt(r2);t=(1+r2)**(-mp.mpf(1)/(2*b));v=radial(comp,t);phi=mp.atan2(y,x);z=(x*x-y*y)/r2;T,dT=poly.angular_cheb(z,comp['M'])
    A,C,At,Ct=[mp.fsum(a*c for a,c in zip(v[n],T)) for n in('A','C','At','Ct')];Az,Cz=[mp.fsum(a*c for a,c in zip(v[n],dT)) for n in('A','C')]
    tx,ty=-x*t**(2*b+1)/b,-y*t**(2*b+1)/b;zx,zy=4*x*y*y/r2**2,-4*x*x*y/r2**2
    Ax,Ay=At*tx+Az*zx,At*ty+Az*zy;Cx,Cy=Ct*tx+Cz*zx,Ct*ty+Cz*zy;ea,eg=2*b+2,2*b+1
    theta=x*x*y*t**ea*A;omega=x*y*t**eg*C
    thx=2*x*y*t**ea*A+x*x*y*(ea*t**(ea-1)*tx*A+t**ea*Ax);thy=x*x*t**ea*A+x*x*y*(ea*t**(ea-1)*ty*A+t**ea*Ay)
    omx=y*t**eg*C+x*y*(eg*t**(eg-1)*tx*C+t**eg*Cx);omy=x*t**eg*C+x*y*(eg*t**(eg-1)*ty*C+t**eg*Cy)
    ur=-mp.fsum((a+c)*mp.cos(2*(j+1)*phi) for j,(a,c) in enumerate(zip(v['X'],v['Y'])))*t**(1-b)/(2*mp.sqrt(v['q']))
    up=mp.fsum((-a+c)*mp.sin(2*(j+1)*phi) for j,(a,c) in enumerate(zip(v['X'],v['Y'])))*t**(1-b)/(2*mp.sqrt(v['q']))
    u1,u2=(x*ur-y*up)/r,(y*ur+x*up)/r
    # Exact axis identities. This removes sin(k*pi) roundoff, not a denominator floor.
    if x==0:u1=mp.mpf(0)
    if y==0:u2=mp.mpf(0)
    w1,w2=b*x+u1,b*y+u2
    ta=[w1*thx,w2*thy,-(b-2)*theta];tg=[w1*omx,w2*omy,omega,-thx];ra,rg=mp.fsum(ta),mp.fsum(tg);na,ng=mp.fsum(map(abs,ta)),mp.fsum(map(abs,tg))
    return {'x':x,'y':y,'Theta':theta,'Omega':omega,'Theta_x':thx,'Theta_y':thy,'Omega_x':omx,'Omega_y':omy,'U1':u1,'U2':u2,'W1':w1,'W2':w2,'R_Theta':ra,'R_Omega':rg,'N_Theta':na,'N_Omega':ng,'ratio_Theta':abs(ra)/na if na else None,'ratio_Omega':abs(rg)/ng if ng else None}
def axis(comp,r,axis=0):
    b=comp['beta'];r=mp.mpf(r);t=(1+r*r)**(-mp.mpf(1)/(2*b));v=radial(comp,t);scale=t**(1-2*b)
    hs=[scale*(a+c)/(4*(j+1)) for j,(a,c) in enumerate(zip(v['X'],v['Y']))];hp=[scale*(-a+c)/(2*r) for a,c in zip(v['X'],v['Y'])]
    ws=[-2*(j+1) if axis==0 else -2*(j+1)*(-1)**(j+1) for j in range(len(hs))];u=mp.fsum(w*h/r for w,h in zip(ws,hs));du=mp.fsum(w*(p/r-h/r**2) for w,p,h in zip(ws,hp,hs))
    return {'r':r,'U':u,'W':b*r+u,'derivative':b+du}
def moments(ca,cg,comp):
    b=comp['beta'];D=comp['denominator'];Q=comp['modes'][0]['Q'];c=sum((Fraction(x,8*D*(j+1)) for j,x in enumerate(Q)),Fraction());a=sum(map(lambda x:Fraction(float(x)),ca[0]),Fraction());g=sum(map(lambda x:Fraction(float(x)),cg[0]),Fraction())
    return {'c':c,'a0':a,'b0':g,'c_defect':c-(2*b+2),'jet_defect':(2*b+1)*g-2*a}
def divided(comp,x,y):
    """Smooth quotient equations with the grouped Cartesian normalization."""
    x,y=mp.mpf(x),mp.mpf(y);b=comp['beta'];D=comp['denominator'];r2=x*x+y*y
    if not r2:
        Q=comp['modes'][0]['Q']
        c=sum((Fraction(v,8*D*(j+1)) for j,v in enumerate(Q)),Fraction())
        c=mp.mpf(c.numerator)/c.denominator
        a,g=mp.mpf(sum(comp['A'][0]))/D,mp.mpf(sum(comp['C'][0]))/D
        ax=ay=gx=gy=mp.mpf(0);aa,bb=b-c,b+c
    else:
        t=(1+r2)**(-mp.mpf(1)/(2*b));v=radial(comp,t);z=(x*x-y*y)/r2
        T,Tz=poly.angular_cheb(z,comp['M'])
        av,gv,at,gt=[mp.fsum(c*d for c,d in zip(v[n],T)) for n in ('A','C','At','Ct')]
        az,gz=[mp.fsum(c*d for c,d in zip(v[n],Tz)) for n in ('A','C')]
        tx,ty=-x*t**(2*b+1)/b,-y*t**(2*b+1)/b
        zx,zy=4*x*y*y/r2**2,-4*x*x*y/r2**2;ea,eg=2*b+2,2*b+1
        a,g=t**ea*av,t**eg*gv
        ax=t**ea*(at*tx+az*zx)+ea*t**(ea-1)*tx*av
        ay=t**ea*(at*ty+az*zy)+ea*t**(ea-1)*ty*av
        gx=t**eg*(gt*tx+gz*zx)+eg*t**(eg-1)*tx*gv
        gy=t**eg*(gt*ty+gz*zy)+eg*t**(eg-1)*ty*gv
        if y==0:
            ar=axis(comp,abs(x),0);aa=ar['W']/abs(x);bb=2*b-ar['derivative']
        elif x==0:
            ar=axis(comp,abs(y),1);aa=2*b-ar['derivative'];bb=ar['W']/abs(y)
        else:
            uv=cartesian(comp,x,y);aa=uv['W1']/x;bb=uv['W2']/y
    ta=[aa*(2*a+x*ax),bb*(a+y*ay),-(b-2)*a]
    tg=[aa*(g+x*gx),bb*(g+y*gy),g,-(2*a+x*ax)]
    ra,rg=mp.fsum(ta),mp.fsum(tg);na,ng=mp.fsum(map(abs,ta)),mp.fsum(map(abs,tg))
    return {'x':x,'y':y,'a':a,'G':g,'A':aa,'B':bb,
            'R_Theta_div':ra,'R_Omega_div':rg,'N_Theta_div':na,'N_Omega_div':ng,
            'ratio_Theta_div':abs(ra)/na if na else None,
            'ratio_Omega_div':abs(rg)/ng if ng else None}
def load(path):
    with np.load(path,allow_pickle=False) as d:
        keys=('beta','beta_map','L','sigma_a','sigma_G','M','N','Me','Ne','mapname')
        if any(k not in d or d[k].shape!=() for k in keys):raise ValueError('scalar metadata required')
        meta={k:d[k].item() for k in keys};b=meta['beta']
        if type(b) is not float or not math.isfinite(b) or not b.is_integer() or b<2:raise ValueError('integer beta')
        bi=int(b)
        if meta['beta_map']!=b or meta['L']!=1 or meta['mapname']!='t':raise ValueError('map')
        if any(type(meta[k]) is not int or meta[k]<1 for k in('M','N','Me','Ne')):raise ValueError('dimensions')
        if meta['Me']!=2*meta['M'] or meta['Ne']!=2*meta['N']:raise ValueError('collocation convention')
        ea,eg=2*b*meta['sigma_a'],2*b*meta['sigma_G']
        if ea!=2*bi+2 or eg!=2*bi+1:raise ValueError('source rounded integer t exponents')
        ca,cg=d['ca'].copy(),d['cG'].copy()
        if ca.shape!=cg.shape or ca.shape!=(meta['M'],meta['N']):raise ValueError('array orientation')
        meta.update(e_a=ea,e_G=eg,exponent_semantics='Source computes rounded binary64 products first, then uses the resulting integer exponents on t.')
    return ca,cg,bi,meta

def run(path,guess,precisions,points,output,save_exact):
    start=time.monotonic();ca,cg,b,meta=load(path);comp=compiler(ca,cg,b);m=moments(ca,cg,comp);compsec=time.monotonic()-start
    out={'timestamp_start':utc(),'source':str(path),'source_sha256':sha(path),'code_sha256':sha(__file__),'own_helper_sha256':sha(HELPER),'metadata':meta,'compiler_seconds':compsec,'exact_moments':{k:{'numerator':str(v.numerator),'denominator':str(v.denominator)} for k,v in m.items()},'evaluations':[]}
    if save_exact:
        p=ROOT/'data'/(path.stem+'_compiled.json');p.write_text(json.dumps(poly.serialize(comp),separators=(',',':'))+'\n');out['compiled']={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
    for dps in precisions:
        with mp.workdps(dps):
            row={'dps':dps,'moments_decimal':{k:dec(mp.mpf(v.numerator)/v.denominator) for k,v in m.items()},'samples':[]}
            if guess:
                g=mp.mpf(guess);root=mp.findroot(lambda r:axis(comp,r)['W'],(g*mp.mpf('.97'),g*mp.mpf('1.03')),tol=mp.mpf('1e-80'),maxsteps=35,verify=True);a=axis(comp,root);f=cartesian(comp,root,0)['Theta_y'];lam=2*b-a['derivative'];den=abs(lam)+b-2
                row.update(axis=strings(a),f=dec(f),predicted_punctured_ratio=dec(abs(lam-(b-2))/den) if den and f else None)
                row['near_axis']=[strings(cartesian(comp,root,mp.mpf(y))) for y in('1e-2','1e-4','1e-6','1e-8')]
            for xy in points:row['samples'].append(strings(cartesian(comp,*xy)))
            out['evaluations'].append(row);output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'dps':dps,'axis':row.get('axis'),'f':row.get('f'),'ratio':row.get('predicted_punctured_ratio'),'elapsed_seconds':time.monotonic()-start}),flush=True)
    out.update(timestamp_end=utc(),elapsed_seconds=time.monotonic()-start,scope='Exact rational moments and multiprecision full-plane inverse samples. No interval root or numerical error enclosure. Exponent semantics explicitly gated.')
    output.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('state',type=Path);p.add_argument('--guess');p.add_argument('--dps',default='220,300');p.add_argument('--points',type=Path);p.add_argument('--output',type=Path);p.add_argument('--save-exact',action='store_true');a=p.parse_args();points=json.loads(a.points.read_text()) if a.points else[['1','.5'],['3','1'],['10','4'],['100','20']]
    run(a.state,a.guess,[int(x) for x in a.dps.split(',')],points,a.output or ROOT/'verification'/(a.state.stem+'_evaluation.json'),a.save_exact)
