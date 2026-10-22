"""Independent Arb512 and mpmath.iv200 positive error and norm integration."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json
from flint import arb,ctx,fmpq_poly,fmpq
from mpmath import iv
ctx.prec=512;ctx.threads=1;iv.dps=200
K=F(1615536043799051,9007199254740992);L=F(8614738245908811,1125899906842624)
A=F(-685794559684773,140737488355328);B=F(2289893859708677,281474976710656);OMEGA=1043;NU=521;M=522
ROOT=Path(__file__).resolve().parents[3]

def endpoint(x,name):
    if name=='arb512':
        assert x.is_finite();out=[]
        for v in [x.lower(),x.upper()]:m,e=v.man_exp();out.append(F(int(m))*F(2)**int(e))
    else:
        out=[]
        for s,m,e,b in x._mpi_:assert b>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
    assert out[0]<=out[1];return out

def encode(x,name):
    a,b=endpoint(x,name);return {'lower_exact':str(a),'upper_exact':str(b)}

class Engine:
    def __init__(self,name):
        assert name in ['arb512','iv200'];self.name=name
        if name=='arb512':ctx.prec=512;self.exp=lambda x:x.exp();self.sqrt=lambda x:x.sqrt();self.pi=arb.pi()
        else:iv.dps=200;self.exp=iv.exp;self.sqrt=iv.sqrt;self.pi=iv.pi
    def q(self,v):
        v=F(v)
        return arb(v.numerator)/v.denominator if self.name=='arb512' else iv.mpf(v.numerator)/v.denominator
    def polynomial(self,cs,h,e=0,den=1):
        assert den>0 and all(v>=0 for v in cs)
        if self.name=='arb512':
            out=self.q(0)
            for v in reversed(cs):out=out*h+self.q(v)
        else:
            out=self.q(0);power=self.q(1)
            for v in cs:out+=self.q(v)*power;power*=h
        return out*self.q(F(2)**e/den)
    def cell(self,c,model,co,inputs):
        q=self.q;h=q(c['h']);e1=q(c['ehi']);d=c['b']-c['a'];assert 0<d<=c['h'] and c['elo']>0
        norms={name:self.polynomial(v['coeff'],h,v['power'],v['denominator']) for name,v in inputs.items()}
        for label in ['A','B']:
            for p in range(3):norms['e'+label+str(p)]+=norms['rem'+label+str(p)]
        def pe(a,b):return norms['e'+a]*(norms[b]+norms['e'+b])+norms[a]*norms['e'+b]
        dv=[]
        for p in range(3):
            v=q(1/K)*norms['eH'+str(p+1)]+norms['eH'+str(p)]
            for l in range(p+1):v+=comb(p,l)*(pe('A'+str(l),'H'+str(p-l+1))+pe('B'+str(l),'TH'+str(p-l)))
            dv.append(v)
        dw=[q(0),pe('F','TH0'),pe('mF','H1')+2*pe('F','TH1')+pe('Fp','TH0')]
        ex=self.exp(2*h);remainder=ex*(2*h)**13/factorial(13)
        bs=[];cs=[];errors=[]
        for p in range(3):
            wn=self.polynomial(co['wnorm'][p],h,model['eW'])
            err=dv[p]+e1**2*ex*dw[p]+(q(co['ze'])*ex+q(co['zc'])*remainder)*wn
            g=self.polynomial(co['g'][p],h,co['eg'],co['gden']);gt=self.polynomial(co['gtheta'][p],h,co['eg'],co['gden'])
            bs.append(e1**3*self.exp(3*h)*(g+err));cs.append(e1**3*self.exp(3*h)*(gt+OMEGA*err));errors.append(err)
        weight=q(L**6)*self.exp(q(-4*c['a']))*(1+self.exp(q(2*c['a']))/q(L**2))**q(F(3,2)-K)
        fac=self.pi*q(d)*weight
        values=[fac*(bs[0]**2+bs[1]**2+cs[0]**2),fac*((bs[0]+bs[1])**2+(bs[1]+bs[2])**2+(cs[0]+cs[1])**2)]
        out={'B':[encode(v,self.name) for v in bs],'C':[encode(v,self.name) for v in cs[:2]],'dV':[encode(v,self.name) for v in dv],'dW':[encode(v,self.name) for v in dw],'error':[encode(v,self.name) for v in errors],'norm_squares':[encode(v,self.name) for v in values]}
        assert all(endpoint(v,self.name)[0]>=0 for v in values)
        return values,out

def inner_coefficients(data):
    assert F(data['ta_exact'])==A and len(data['rows'])==262
    bi=F(data['bi_exact']);sums=[{} for _ in range(4)];equalities=0
    for j,row in enumerate(data['rows']):
        assert row['j']==j and F(row['C'])==(F(1,4) if j<2 else 0)
        family=[(F(2*i+2),[F(v)]) for i,v in enumerate(row['D'])]+[(bi,[F(v) for v in row['Ei']])]
        assert len(row['D'])==len(row['Ei'])==7
        if j==261:assert all(v==0 for rate,cs in family for v in cs)
        for rate,cs in family:
            pol=fmpq_poly([fmpq(v.numerator,v.denominator) for v in cs])
            for p in range(4):
                for l in range(len(cs)):
                    v=sum((F(comb(p,q)*factorial(l+q),factorial(l))*(3+rate)**(p-q)*cs[l+q] for q in range(min(p,len(cs)-1-l)+1)),F(0))
                    assert v==F(str(pol[l]));equalities+=1
                    assert (rate==2 and l==0) or rate>2
                    key=(rate,l);sums[p][key]=sums[p].get(key,F(0))+abs(v)
                r=fmpq((3+rate).numerator,(3+rate).denominator);pol=pol.derivative()+r*pol
    assert equalities==14672;return sums,equalities

def outer_derivatives(data):
    assert data['schema']=='ipm-canonical-residual-coefficient-upper-v1' and len(data['rows'])==1864
    out=[{} for _ in range(3)];count=0;coeffs=0
    for row in data['rows']:
        g=F(row['gamma_exact']);cs=[F(v) for v in row['coefficients_upper_exact']];assert g<0 and 1+2*K-2*g>0 and all(v>=0 for v in cs) and g not in out[0]
        coeffs+=len(cs);pol=fmpq_poly([fmpq(v.numerator,v.denominator) for v in cs])
        for p in range(3):
            vals=[]
            for l in range(len(cs)):
                v=sum((F(comb(p,q)*factorial(l+q),factorial(l))*abs(g)**(p-q)*cs[l+q] for q in range(min(p,len(cs)-1-l)+1)),F(0))
                assert v==F(str(pol[l]));count+=1;vals.append(v)
            out[p][g]=vals;r=abs(g);pol=pol.derivative()+fmpq(r.numerator,r.denominator)*pol
    assert coeffs==3508 and count==10524;return out,count

def tail_inputs():
    load=lambda n:json.loads((ROOT/n).read_text())
    sums,ni=inner_coefficients(load('research/inner_majorant/evidence/exact_inner_coefficients.json'))
    derivs,no=outer_derivatives(load('research/derivative_end_tails/evidence/coefficient_upper_bounds.json'))
    inner=load('research/inner_majorant/evidence/inner_result.json');assert inner['cases'][0]['T_exact']=='0'
    def checked(v):
        lo,hi=F(v['lower_exact']),F(v['upper_exact']);b=v['ball'];m=F(b['mid_m'])*F(2)**int(b['mid_e']);r=F(b['rad_m'])*F(2)**int(b['rad_e']);assert r>=0 and lo<=m-r<=m+r<=hi and hi>=0;return hi
    cr=checked(inner['cases'][0]['values']['C_r']);ct=checked(inner['cases'][0]['values']['C_theta'])
    return sums,derivs,cr,ct,{'inner_derivative_equalities':ni,'outer_derivative_equalities':no}

def tails(engine,inputs):
    sums,derivs,cr,ct,_=inputs;q=engine.q;exp=engine.exp;sqrt=engine.sqrt;pi=engine.pi
    ri2=exp(q(2*A));ds=[];maxima=0
    for row in sums:
        z=q(0)
        for (rate,l),v in row.items():
            if rate==2:assert l==0;mv=q(1)
            else:
                x=F(l)/(rate-2)
                # Arb substitutes the critical point; iv uses exp(-l) exactly.
                mv=q(x)**l*exp(q(-(rate-2)*x if engine.name=='arb512' else -l))
            z+=q(v)*mv;maxima+=1
        ds.append(exp(q(-2*A))*z)
    ss=[q(cr)];rs=[q(ct)];f0=1+ri2*(ds[1]+NU*ds[0]);f1=2+ri2*(ds[2]+(NU+1)*ds[1]+NU*ds[0])
    ss.append(2*ss[0]+M*rs[0]);rs.append(M*ss[0]+2*rs[0]+f0);ss.append(2*ss[1]+M*rs[1]);rs.append(M*ss[1]+2*rs[1]+f1)
    bs=[]
    for p in range(3):
        z=q(1/K)*ds[p+1]+ds[p]+q(abs(3/K-1))*(ds[p+1]+NU*ds[p])
        for l in range(p+1):z+=comb(p,l)*3**(p-l)*(q(F(3,2))*ss[l]+rs[l])+ri2*comb(p,l)*(ss[l]*ds[p-l+1]+rs[l]*NU*ds[p-l])
        bs.append(z)
    ci=pi*q(L**6)*(1+ri2/q(L**2))**q(F(3,2)-K)*exp(q(6*A))/6
    inner=[ci*((1+OMEGA**2)*bs[0]**2+bs[1]**2),ci*((1+OMEGA**2)*(bs[0]+bs[1])**2+(bs[1]+bs[2])**2)]
    co=q(L)**q(3+2*K)*exp(q(-(1+2*K)*B))*(1+q(L**2)*exp(q(-2*B)))**q(F(3,2)-K)
    ls=[q(0),q(0),q(0)];weights=[]
    for g,cs in derivs[0].items():
        rate=1+2*K-2*g;js=[]
        if engine.name=='arb512':js=[q(F(factorial(2*l))/rate**(2*l+1)) for l in range(len(cs))]
        else:
            jv=1/q(rate);js=[jv]
            for n in range(1,2*len(cs)-1):
                jv=q(F(n)/rate)*jv
                if n%2==0:js.append(jv)
        for l,jv in enumerate(js):
            w=sqrt(co*jv);weights.append(encode(w,engine.name))
            for p in range(3):ls[p]+=q(derivs[p][g][l])*w
    assert len(weights)==3508
    outer=[pi*((1+OMEGA**2)*ls[0]**2+ls[1]**2),pi*((1+OMEGA**2)*(ls[0]+ls[1])**2+(ls[1]+ls[2])**2)]
    values=[inner[i]+outer[i] for i in range(2)]
    return values,{'inner_norm_squares':[encode(v,engine.name) for v in inner],'outer_norm_squares':[encode(v,engine.name) for v in outer],'inner_d':[encode(v,engine.name) for v in ds],'inner_B':[encode(v,engine.name) for v in bs],'outer_L':[encode(v,engine.name) for v in ls],'inner_maxima':maxima,'weights':weights}
