"""Own exact rational B-spline and Arb exponential moments, no prior evaluator imports."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[v]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial, comb
import json,hashlib,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
TOP=Path(__file__).resolve().parents[1]
INP=ROOT/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
ctx.prec=384;ctx.threads=1

def rat(v): return F(*float(v).as_integer_ratio())
def aa(v):
    if isinstance(v,F): return arb(v.numerator)/v.denominator
    return arb(v)
def ball(v):return {'ball':v.str(60),'lower':v.lower().str(70),'upper':v.upper().str(70)}
def stamp():return datetime.now(timezone.utc).isoformat()
def emit(**v):print(json.dumps({'date':stamp(),**v}),flush=True)

def pmul_linear(p,a,b):
    out=[F(0)]*(len(p)+1)
    for j,v in enumerate(p):out[j]+=a*v;out[j+1]+=b*v
    return out

def padd(a,b):
    out=[F(0)]*max(len(a),len(b))
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    return out

def deboor_poly(knots,coef,degree,span):
    left,right=knots[span:span+2];width=right-left
    assert width>0
    d=[[coef[span-degree+j]] for j in range(degree+1)]
    for lev in range(1,degree+1):
        for j in range(degree,lev-1,-1):
            idx=span-degree+j;den=knots[idx+degree-lev+1]-knots[idx]
            assert den>0
            a=(left-knots[idx])/den;b=width/den
            d[j]=padd(pmul_linear(d[j-1],1-a,-b),pmul_linear(d[j],a,b))
    assert len(d[-1])==degree+1
    return d[-1]

def jets(poly,width,right):
    return [sum((poly[i]*F(factorial(i),factorial(i-j))*(F(1) if right or i==j else F(0)) for i in range(j,len(poly))),F(0))/width**j for j in range(7)]

def derivative_endpoints(knots,co,degree):
    left=[];right=[]
    for n in range(7):
        left.append(co[0]);right.append(co[-1])
        if n<6:
            ds=[]
            for i in range(len(co)-1):
                den=knots[i+degree+1]-knots[i+1]
                assert den>0
                ds.append(degree*(co[i+1]-co[i])/den)
            knots=knots[1:-1];co=ds;degree-=1
    return left,right

def matched(jets,nonjets,b):
    diff=[x-y for x,y in zip(jets,nonjets)]
    out=[sum(((-b)**(i-j)*diff[j]/(factorial(i-j)*factorial(j)) for j in range(i+1)),F(0)) for i in range(7)]
    for j in range(7):
        val=sum((F(comb(j,i))*b**(j-i)*factorial(i)*out[i] for i in range(j+1)),F(0))
        assert val==diff[j]
    return out

def moments(z,N=64):
    zz=aa(z);result=[arb(0) for i in range(8)];power=arb(1)
    for n in range(N):
        for i in range(8):result[i]+=power/(n+i+1)
        power*=zz/(n+1)
    tails=[zz.exp()*power/(N+i+1) for i in range(8)]
    return [v+arb(0,t.upper()) for v,t in zip(result,tails)],tails

def main():
    started=time.monotonic();data=np.load(INP,allow_pickle=False)
    assert int(data['p'])==7 and int(data['M'])==260
    knots=list(map(rat,data['knots']));p=7
    assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8
    spans=[j for j in range(p,len(knots)-p-1) if knots[j]<knots[j+1]]
    assert len(spans)==1558
    assert all(knots[j]<knots[j+1] for j in range(7,len(knots)-8))
    weights=[F(1,4),F(1,8),-F(1,8),-F(1,8)]
    project=lambda arr:[sum((weights[m]*rat(arr[m,j]) for m in range(4)),F(0)) for j in range(arr.shape[1])]
    co=project(data['S']);di=project(data['D']);ao=project(data['Aout'])
    assert len(co)==len(knots)-p-1
    k=rat(data['k']);L=rat(data['L']);bi=rat(data['bi']);bo=rat(data['bo'])
    pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
    alphas=[k-3-j*(1-k)-2*l for j,l in pairs]
    assert 0<k<F(1,2) and bi>4 and bo>2 and all(a<-2 for a in alphas) and alphas[0]+bo>0
    tm,tp=knots[0],knots[-1]
    Pm=deboor_poly(knots,co,p,spans[0]);Pp=deboor_poly(knots,co,p,spans[-1])
    jm=jets(Pm,knots[spans[0]+1]-knots[spans[0]],False)
    jp=jets(Pp,knots[spans[-1]+1]-knots[spans[-1]],True)
    dm,dp=derivative_endpoints(knots[:],co[:],p)
    assert jm==dm and jp==dp
    innerjets=[F(1,4)*(n==0)+sum((di[j]*(2*j+2)**n for j in range(7)),F(0)) for n in range(7)]
    outerjets=[sum((ao[j]*alphas[j]**n for j in range(10)),F(0)) for n in range(7)]
    ei=matched(jm,innerjets,bi);eo=matched(jp,outerjets,-bo)
    inner_r=F(1,8)+sum((di[j]/(2*j+4) for j in range(7)),F(0))+sum((ei[i]*(-1)**i*factorial(i)/(bi+2)**(i+1) for i in range(7)),F(0))
    outer_r=sum((ao[q]/(-alphas[q]-2) for q in range(10)),F(0))+sum((eo[i]*factorial(i)/(bo-2)**(i+1) for i in range(7)),F(0))
    inner=(2*aa(tm)).exp()*aa(inner_r);outer=(2*aa(tp)).exp()*aa(outer_r)
    total=arb(0);terr=arb(0)
    emit(stage='start',input_sha256=hashlib.sha256(INP.read_bytes()).hexdigest(),spans=len(spans),inner=ball(inner),outer=ball(outer),endpoint_jet_checks='exact equality, orders 0..6, both ends')
    for done,j in enumerate(spans,1):
        left,right=knots[j:j+2];width=right-left
        poly=deboor_poly(knots,co,p,j)
        ms,ts=moments(2*width)
        pref=(2*aa(left)).exp()*aa(width)
        total+=pref*sum((aa(poly[i])*ms[i] for i in range(8)),arb(0))
        terr+=pref*sum((abs(aa(poly[i]))*ts[i] for i in range(8)),arb(0))
        if done%100==0 or done==len(spans):emit(stage='middle',done=done,total=len(spans),seconds=time.monotonic()-started,partial=ball(total))
    c0=inner+total+outer
    slope=(2*aa(tp)).exp()/aa(4*(-alphas[0]-2))*aa(((alphas[0]+bo)/(bo-2))**7)
    correction=(3/aa(k)-1-c0)/slope
    cc=1/(aa(L)**2*(11*arb.pi()*(1-2*aa(k))).sqrt())
    s=arb(31)/10
    result={'date':stamp(),'verdict':'COMPUTED_PENDING_INDEPENDENT_OUTPUT_AUDIT','input':str(INP.relative_to(ROOT)),'input_sha256':hashlib.sha256(INP.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':ctx.prec,'method':'Own exact rational span-polynomial de Boor; 64-term Arb exponential moments with Taylor remainder; exact projected joins checked by derivative-coefficient recursion','spans':len(spans),'k_exact':str(k),'L_exact':str(L),'c0':ball(c0),'slope':ball(slope),'normalization_correction_z':ball(correction),'target_c':ball(3/aa(k)-1),'c_X_bound':ball(cc),'inner':ball(inner),'middle':ball(total),'outer':ball(outer),'middle_taylor_absolute_remainder':ball(terr),'seconds':time.monotonic()-started,'scope':'Exact-joined modal central strain and its exact-real scalar repair only. No X3 strain, residual norm, source coefficient or inverse.'}
    out=TOP/'evidence/recomputed.json';out.write_text(json.dumps(result,indent=2)+'\n')
    emit(stage='finished',**result)
if __name__=='__main__':main()
