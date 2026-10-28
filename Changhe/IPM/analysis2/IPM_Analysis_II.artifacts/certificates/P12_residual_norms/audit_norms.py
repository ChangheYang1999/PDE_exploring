"""Independent u=1-t integrals and Cartesian order-seven residual audit."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,acb,fmpq,fmpq_poly,ctx
import compact_norms as cn
ctx.prec=640
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
U=fmpq_poly([0,1]);T=1-U


def compose(p,x):
    out=fmpq_poly([])
    for a in reversed(p.coeffs()):out=out*x+a
    return out

def aq(x):return cn.aq(x)

def poly_integral_u(p,exponent):
    result=fmpq(0)
    for k,coef in enumerate(p.coeffs()):
        if coef:
            assert exponent+k>-1,('nonintegrable exact u monomial',exponent,k)
            result+=coef/cn.fq(exponent+k+1)
    return result

def integrate(D,d,delta,weight,rproxy,N):
    # No endpoint division, beta recursion, or norm routine is shared.
    group={};facts=[]
    base=Q(d-3)-(Q(4,5) if weight else 0)-(1 if rproxy else 0)
    bad=False
    for nx in range(d+1):
        harmonics={}
        for (ell,kind,n),p in D[d,nx].items():
            pu=compose(p,T)
            first=next(k for k,a in enumerate(pu.coeffs()) if a)
            exponent=base+ell*delta+2*first
            if exponent<=-1:bad=True
            harmonics.setdefault((kind,n),[]).append((ell,pu))
        for (kind,n),entries in harmonics.items():
            factor=comb(d,nx)*(2 if kind=='c' and n==0 else 1)
            for ell,p in entries:
                for ell2,q in entries:
                    power=ell+ell2
                    group[power]=group.get(power,fmpq_poly([]))+factor*p*q
    if bad:return None
    tp=(1 if d%2 else T)*(T if rproxy else 1)
    s=fmpq(0);ss=fmpq(0)
    g=fmpq_poly([])
    z=fmpq_poly([cn.fq(Q(3,5)),cn.fq(-Q(6,5))])
    for n in range(N+1):
        coeff=fmpq(1)
        for j in range(n):coeff*=cn.fq(Q(4,5)-j)/(j+1)
        g+=coeff*z**n
    nxt=fmpq(1)
    for j in range(N+1):nxt*=cn.fq(Q(4,5)-j)/(j+1)
    eps=abs(nxt)*cn.fq(Q(3,5)**(N+1)/Q(2,5))
    for power,p in group.items():
        exp=base+power*delta/2
        s+=poly_integral_u(p*tp,exp)
        if weight:ss+=poly_integral_u(p*tp*g,exp)
    if not weight:ss=s
    return s,ss,eps

ORDER=7
INDICES=[(i,j) for i in range(ORDER+1) for j in range(ORDER+1-i)]
def pmul(a,b,order=ORDER):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            if i+j+k+l<=order:
                key=i+k,j+l;out[key]=out.get(key,arb(0))+x*y
    return out

def direct_chi(A,c,x,y):
    q=x*x+y*y; oq=1+q;gamma=1/aq(c);v=q/oq
    dq={(1,0):2*x,(0,1):2*y,(2,0):arb(1),(0,2):arb(1)}
    powers=[{(0,0):arb(1)}]
    for _ in range(ORDER):powers.append(pmul(powers[-1],dq))
    mmax=max(m for j,m,k in A);zz=acb(x,y);zp=[acb(1)]
    for _ in range(2*mmax):zp.append(zp[-1]*zz)
    hj={}
    for m in range(mmax+1):
        n=2*m;poly={}
        for i,j in INDICES:
            if i+j<=n:
                z=zp[n-i-j];val=(z.real,-z.imag,-z.real,z.imag)[j%4]
                poly[i,j]=arb(factorial(n)//factorial(n-i-j))*val/(factorial(i)*factorial(j))
        hj[m]=poly
    groups={}
    for (j,m,k),a in A.items():groups.setdefault((j,m),[]).append((k-m,a))
    chi={key:arb(0) for key in INDICES}
    for (j,m),terms in groups.items():
        p=(3+gamma-j*(1-gamma))/2; pref=oq**(p-m);rad=[arb(0) for _ in range(ORDER+1)]
        for l,coeff in terms:
            factor=aq(coeff)*pref*v**l; beta=p-m-l
            binom_q=[arb(comb(l,k))/q**k if k<=l else arb(0) for k in range(ORDER+1)]
            binom_o=[arb(1)]
            for k in range(1,ORDER+1):binom_o.append(binom_o[-1]*(beta-k+1)/(k*oq))
            for k in range(ORDER+1):rad[k]+=factor*sum((binom_q[a]*binom_o[k-a] for a in range(k+1)),arb(0))
        rp={key:arb(0) for key in INDICES}
        for k,val in enumerate(rad):
            for key,co in powers[k].items():rp[key]+=val*co
        prod=pmul(hj[m],rp)
        for key,val in prod.items():chi[key]+=val
    return {key:val*factorial(key[0])*factorial(key[1]) for key,val in chi.items()}

def direct_F(A,c,x,y):
    chi=direct_chi(A,c,x,y);rho={};u={0:{},1:{}}
    for i in range(5):
        for j in range(5-i):rho[i,j]=(-chi[i+2,j+1]-chi[i,j+3])/(factorial(i)*factorial(j))
    for i in range(4):
        for j in range(4-i):
            u[0][i,j]=-chi[i+1,j+2]/(factorial(i)*factorial(j))
            u[1][i,j]=chi[i+2,j+1]/(factorial(i)*factorial(j))
    u[0][0,0]+=aq(c)*x;u[1][0,0]+=aq(c)*y
    u[0][1,0]+=aq(c);u[1][0,1]+=aq(c)
    rx={(i,j):(i+1)*rho[i+1,j] for i in range(4) for j in range(4-i)}
    ry={(i,j):(j+1)*rho[i,j+1] for i in range(4) for j in range(4-i)}
    a=pmul(u[0],rx,3);b=pmul(u[1],ry,3)
    return {(i,j):(a.get((i,j),arb(0))+b.get((i,j),arb(0))-rho[i,j])*factorial(i)*factorial(j)
            for i in range(4) for j in range(4-i)}

def polar_eval(D,delta,xq,yq):
    r2=xq*xq+yq*yq;tq=r2/(1+r2)
    t=aq(tq);r=aq(r2).sqrt();x=aq(xq);y=aq(yq);w=(1-t)**(aq(delta)/2)
    maxn=max(n for fields in D.values() for ell,kind,n in fields)
    co=[arb(1),x/r];si=[arb(0),y/r]
    for n in range(2,maxn+1):co.append(2*co[1]*co[-1]-co[-2]);si.append(2*co[1]*si[-1]-si[-2])
    values={}
    for (d,nx),fields in D.items():
        val=arb(0)
        for (ell,kind,n),p in fields.items():
            pp=arb(0)
            for a in reversed(p.coeffs()):pp=pp*t+aq(a)
            val+=w**ell*pp*(co[n] if kind=='c' else si[n])
        fac=(1-t)**aq(Q(d-1,2))
        if d%2==0:fac*=t.sqrt()
        values[nx,d-nx]=val*fac
    return values

def run(name):
    start=time.monotonic();path=HERE/f'{name}_polynomials.json';np=HERE/f'{name}_norms.json'
    raw=json.loads(path.read_text());saved=json.loads(np.read_text())
    c,A,sha,rawsha=cn.source(name)
    assert raw['canonical_sha256']==sha and raw['source_record_sha256']==rawsha
    assert saved['polynomial_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
    D={tuple(map(int,k.split(','))):cn.dec(v) for k,v in raw['polynomials'].items()};delta=Q(raw['delta'])
    # Regenerate initial polynomials from exact source and test all derivative paths.
    initial,regen=cn.construct(name,write=False)
    assert D==regen
    vals={}
    for label,d,we,rp in [('rF',0,False,True),('F',0,False,False),('DF',1,False,False),('omega_D2F',2,True,False),('omega_D3F',3,True,False)]:
        row=saved['norms'][label];z=integrate(D,d,delta,we,rp,row['weight_N'] if row['status']=='FINITE' else 0)
        if z is None:assert row['status']=='INFINITE';vals[label]={'status':'INFINITE'}
        else:
            S,T,eps=z;assert str(S)==row['base_beta_sum'];assert str(T)==row['weighted_beta_sum']
            if we:assert str(eps)==row['weight_error_rational']
            pref=(aq(Q(5,2))**aq(Q(4,5))) if we else arb(1)
            lo=arb.pi()/2*pref*aq(T-(eps*S if we else 0));hi=arb.pi()/2*pref*aq(T+(eps*S if we else 0))
            assert lo>0 and hi>0
            vals[label]={'status':'FINITE','lower':lo.sqrt().str(80),'upper':hi.sqrt().str(80)}
        print(name,'independent u integral',label,'PASS','sec',time.monotonic()-start,flush=True)
    checks=[]
    for xs,ys in [('0','1/10'),('1','0'),('1/2','1/2'),('1','2'),('3','1'),('60','80'),('0','1000')]:
        xq,yq=Q(xs),Q(ys);v=polar_eval(D,delta,xq,yq);direct=direct_F(A,c,aq(xq),aq(yq))
        ok={f'{i},{j}':v[i,j].is_finite() and q.is_finite() and v[i,j].overlaps(q) for (i,j),q in direct.items()}
        assert all(ok.values()),(name,xs,ys,[(key,v[tuple(map(int,key.split(',')))],direct[tuple(map(int,key.split(',')))]) for key,a in ok.items() if not a])
        checks.append({'point':[xs,ys],'components':ok});print(name,'Cartesian',xs,ys,'PASS',flush=True)
    # construct() updates a timestamp in the polynomial file; preserve original audited bytes.
    # Values are identical and original hash is retained by writing back the original record.
    path.write_text(json.dumps(raw,separators=(',',':'))+'\n')
    assert saved['polynomial_sha256']==hashlib.sha256(path.read_bytes()).hexdigest()
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'verdict':'CONFIRMED',
         'precision_bits':ctx.prec,'canonical_sha256':sha,'polynomial_sha256':saved['polynomial_sha256'],
         'norm_record_sha256':hashlib.sha256(np.read_bytes()).hexdigest(),'norms':vals,'cartesian_checks':checks,
         'elapsed_seconds':time.monotonic()-start}
    (HERE/f'{name}_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print('AUDIT COMPLETE',name,'sec',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'state131')
