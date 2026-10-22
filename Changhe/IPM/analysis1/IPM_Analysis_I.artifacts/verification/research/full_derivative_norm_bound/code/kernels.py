"""Exact dyadic inputs and integer vs modular/CRT Fourier jet convolution."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import sys
sys.dont_write_bytecode=True
import math,hashlib
from fractions import Fraction as F
from flint import fmpz_poly,nmod_poly
assert not sys.flags.optimize
D=1615536043799051;N=9007199254740992;J=12;NJ=math.factorial(J)

def dyadic(arrays):
    rows=[];emin=0
    for a in arrays:
        shape=a.shape;out=[]
        for x in a.flat:
            v=float(x);assert math.isfinite(v)
            n,d=v.as_integer_ratio();e=-(d.bit_length()-1);assert d==1<<(-e)
            if n:emin=min(emin,e)
            out.append((n,e))
        rows.append((shape,out))
    return [([n<<(e-emin) if n else 0 for n,e in row],shape) for shape,row in rows],emin

def reshape(v,shape):
    if len(shape)==1:return v
    assert len(shape)==2 and len(v)==shape[0]*shape[1]
    return [v[j*shape[1]:(j+1)*shape[1]] for j in range(shape[0])]

def scaled(arrays):
    vals,e=dyadic(arrays);return [reshape(v,shape) for v,shape in vals],e

def differentiate(a,rate=0):
    return [rate*v+(j+1)*a[j+1] if j+1<len(a) else rate*v for j,v in enumerate(a)]

def density(T,absolute=False):
    assert len(T)==8 and all(len(r)==260 for r in T)
    # Collect the exact signed map before applying radii.
    weights=[{} for _ in range(262)]
    for m in range(260):
        for base in (1,3):
            for q in (base+2*m,base-2*m):
                assert q%2 and q!=0
                j=(abs(q)-1)//2;assert 0<=j<262
                weights[j][m]=weights[j].get(m,0)+(1 if q>0 else -1)
    H=[[sum((abs(w) if absolute else w)*T[l][m] for m,w in weights[j].items()) for l in range(8)] for j in range(262)]
    assert H[-1]==[0]*8
    # Independent tridiagonal angular identities for every coefficient.
    for l in range(8):
        def t(m):return T[l][m] if 0<=m<260 else 0
        if not absolute:
            expected=[2*t(0)-t(2),2*t(0)+t(1)-t(2)-t(3)]
            expected += [t(j)+t(j-1)-t(j+1)-t(j+2) for j in range(2,262)]
            assert [H[j][l] for j in range(262)]==expected
    return H

def hjets(H):
    out=[]
    for p in range(4):
        hp=[]
        for row in H:
            direct=[sum(math.comb(p,q)*3**(p-q)*math.factorial(l+q)//math.factorial(l)*row[l+q] for q in range(min(p,len(row)-1-l)+1)) for l in range(8)]
            repeated=row[:]
            for _ in range(p):repeated=differentiate(repeated,3)
            assert direct==repeated;hp.append(direct)
        out.append(hp)
    return out

def forcing(H,absolute=False):
    ans=[]
    for n in range(1,262):
        m=2*n;a=H[n-1];b=H[n];aa=differentiate(a);bb=differentiate(b)
        ans.append([(abs(4-m) if absolute else 4-m)*a[l]+(4+m)*b[l]+aa[l]+bb[l] for l in range(8)])
    return ans

def velocity(P,R,absolute=False):
    a=[[],[],[]];b=[[],[],[]]
    for n,(pr,rr) in enumerate(zip(P,R),1):
        assert len(pr)==len(rr)==13;m=2*n
        a[0].append(pr);b[0].append(rr)
        a[1].append([(2 if absolute else -2)*p+m*r for p,r in zip(pr,rr)])
        b[1].append([m*p+(2 if absolute else -2)*r for p,r in zip(pr,rr)])
        a[2].append([(4+m*m)*p+(4*m if absolute else -4*m)*r for p,r in zip(pr,rr)])
        b[2].append([(4*m if absolute else -4*m)*p+(4+m*m)*r for p,r in zip(pr,rr)])
    return a,b

def digest_integers(xs):
    h=hashlib.sha256()
    for x in xs:
        v=int(x);n=max(1,(abs(v).bit_length()+8)//8);b=v.to_bytes(n,'little',signed=True);h.update(len(b).to_bytes(4,'little'));h.update(b)
    return h.hexdigest()

def exact_product(x,y):
    assert x and y and all(type(v) is int for v in x+y)
    size=len(x)+len(y)-1;C=min(len(x),len(y))*max(map(abs,x))*max(map(abs,y))
    za=fmpz_poly(x)*fmpz_poly(y);answer=[int(za[j]) for j in range(size)]
    assert all(abs(v)<=C for v in answer)
    if C==0:
        assert not any(answer);return answer,{'lengths':[len(x),len(y)],'coefficients':size,'coefficient_bound':str(C),'moduli':[],'modulus_product':'1','all_equal':True,'sha256':digest_integers(answer)}
    Q=1;m=(1<<61)-1;mods=[];out=[0]*size
    while Q<=2*C:
        while math.gcd(Q,m)!=1:m-=2
        assert 1<m<1<<63 and m%2
        xm=[v%m for v in x];ym=[v%m for v in y];z=nmod_poly(xm,m)*nmod_poly(ym,m)
        inv=pow(Q,-1,m);assert Q*inv%m==1
        out=[a+Q*((int(z[j])-a)%m*inv%m) for j,a in enumerate(out)]
        assert all(0<=v<Q*m for v in out)
        mods.append(m);Q*=m;m-=2
    assert Q>2*C
    for j,v in enumerate(out):
        s=v if 2*v<Q else v-Q
        assert s==answer[j],('CRT mismatch',j,s,answer[j])
    return answer,{'lengths':[len(x),len(y)],'coefficients':size,'coefficient_bound':str(C),'moduli':mods,'modulus_product':str(Q),'all_equal':True,'sha256':digest_integers(answer)}

def pack_velocity(jets,radstride,jetout,sine):
    jetcount=len(jets);degree=len(jets[0][0])-1
    assert len(jets[0])==261 and degree<radstride and jetcount<=jetout
    stride=radstride*jetout;out=[0]*(523*stride)
    for p,rows in enumerate(jets):
        for n,row in enumerate(rows,1):
            for sign in (-1,1):
                offset=(261+sign*n)*stride+p*radstride
                for l,v in enumerate(row):out[offset+l]=(sign if sine else 1)*v
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def pack_density(jets,radstride,jetout,imaginary):
    degree=len(jets[0][0])-1;assert len(jets[0])==262 and degree<radstride
    stride=radstride*jetout;out=[0]*(522*stride)
    for p,rows in enumerate(jets):
        for j,row in enumerate(rows[:261]):
            for sign in (-1,1):
                offset=(261+j if sign==1 else 260-j)*stride+p*radstride
                for l,v in enumerate(row):out[offset+l]=(sign if imaginary else 1)*v
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def get_positive(z,radstride,jetout,p,degree):
    stride=radstride*jetout;assert 0<=p<jetout and degree<radstride
    def get(j):return z[j] if j<len(z) else 0
    rows=[]
    for index in range(522,1044):
        mirror=1043-index
        row=[get(index*stride+p*radstride+l) for l in range(degree+1)]
        assert all(get(mirror*stride+p*radstride+l)==-v for l,v in enumerate(row)),('sine antisymmetry',index,p)
        rows.append(row)
    return rows

def smul(rows,k):return [[k*v for v in row] for row in rows]
def add(a,b):assert len(a)==len(b);return [x+y for x,y in zip(a,b)]

def build(arrays):
    [P,R],ep=scaled([arrays['P_mid'],arrays['R_mid']]);[T],et=scaled([arrays['T_mid']]);eh=et-3
    H=density(T);Hp=hjets(H);Fn=forcing(H);ef=eh-1;Fp=[differentiate(row) for row in Fn];Aj,Bj=velocity(P,R)
    # All jet coefficients are literal derivative / factorial Fourier coefficients.
    av=[smul(Aj[p],-2 if p<2 else -1) for p in range(3)]
    bv=[smul(Bj[p],-2 if p<2 else -1) for p in range(3)]
    ht=[smul(Hp[p+1],-2 if p<2 else -1) for p in range(3)]
    hc=[[[ (2*j+1)*(2 if p<2 else 1)*v for v in row] for j,row in enumerate(Hp[p])] for p in range(3)]
    x1=pack_velocity(av,20,5,False);y1=pack_density(ht,20,5,True)
    x2=pack_velocity(bv,20,5,True);y2=pack_density(hc,20,5,False)
    assert len(x1)+len(y1)-1<=1044*100 and len(x2)+len(y2)-1<=1044*100
    z1,r1=exact_product(x1,y1);z2,r2=exact_product(x2,y2)
    size=max(len(z1),len(z2));base=[(z1[j] if j<len(z1) else 0)+(z2[j] if j<len(z2) else 0) for j in range(size)]
    eB=ep+eh-4;eV=min(eB,eh-1);V=[]
    for p in range(3):
        rows=get_positive(base,20,5,p,19)
        for j,row in enumerate(rows):
            for l in range(20):
                linear=(-N*Hp[p+1][j][l]+D*Hp[p][j][l]) if j<261 and l<8 else 0
                row[l]=(D*math.factorial(p)*row[l]<<(eB-eV))+(linear<<(eh-1-eV))
        V.append(rows)
    # W2 radial forcing product, with Fourier scales ef-1 and eh-1.
    mf=[[2*n*v for v in row] for n,row in enumerate(Fn,1)]
    a=pack_velocity([mf],15,1,False);b=pack_density([smul(Hp[1],-1)],15,1,True)
    assert len(a)+len(b)-1<=1044*15
    za,ra=exact_product(a,b);wa=get_positive(za,15,1,0,14)
    # First-order jet for the two angular forcing terms.
    bf=[smul(Fn,2),Fp];ch=[[[ (2*j+1)*v for v in row] for j,row in enumerate(Hp[p])] for p in range(2)]
    a=pack_velocity(bf,15,3,True);b=pack_density(ch,15,3,False)
    assert len(a)+len(b)-1<=1044*45
    zb,rb=exact_product(a,b);w1=get_positive(zb,15,3,0,14);w2=get_positive(zb,15,3,1,14)
    w2=[[2*(v+u) for v,u in zip(rowa,rowb)] for rowa,rowb in zip(w2,wa)]
    W=[[[0]*15 for _ in range(522)],w1,w2];eW=ef+eh-3
    return {'H':H,'Hp':Hp,'F':Fn,'Fp':Fp,'Aj':Aj,'Bj':Bj,'ep':ep,'eh':eh,'ef':ef,'V':V,'eV':eV,'W':W,'eW':eW,'convolutions':[r1,r2,ra,rb]}

def combine(model,e0,e1):
    zc=(e0*e0+e1*e1)/2;ze=(e1*e1-e0*e0)/2;assert zc>0 and ze>=0
    ez=-(zc.denominator.bit_length()-1);assert zc.denominator==1<<(-ez);zm=zc.numerator
    eV=model['eV'];eW=model['eW'];eg=min(eV,ez+eW);expints=[(1<<j)*NJ//math.factorial(j) for j in range(J+1)]
    # Independent exact Taylor coefficient recurrence.
    for j in range(J):assert expints[j+1]*(j+1)==2*expints[j]
    gs=[];gts=[];ws=[]
    for p in range(3):
        g=[0]*27;gt=[0]*27;w=[0]*15
        for j,(vr,wr) in enumerate(zip(model['V'][p],model['W'][p])):
            q=2*j+1
            for l in range(15):w[l]+=2*abs(wr[l])
            for l in range(27):
                vi=vr[l] if l<20 else 0
                wi=sum(wr[k]*expints[l-k] for k in range(max(0,l-J),min(14,l)+1))
                gi=(vi*NJ<<(eV-eg))+(zm*D*wi<<(ez+eW-eg))
                g[l]+=2*abs(gi);gt[l]+=2*q*abs(gi)
        gs.append(g);gts.append(gt);ws.append(w)
    return {'g':gs,'gtheta':gts,'wnorm':ws,'eg':eg,'gden':D*NJ,'zc':zc,'ze':ze}

def sumabs(rows,angular=False):
    assert rows and all(len(x)==len(rows[0]) for x in rows)
    return [sum((2*j+1 if angular else 1)*abs(row[l]) for j,row in enumerate(rows)) for l in range(len(rows[0]))]

def error_inputs(arrays,model):
    [pr,rr],er=scaled([arrays['P_rad'],arrays['R_rad']]);assert all(v>=0 for rows in (pr,rr) for row in rows for v in row)
    [prem,rrem],erem=scaled([arrays['P_rem'],arrays['R_rem']]);assert all(v>=0 for row in (prem,rrem) for v in row)
    [T],etr=scaled([arrays['T_rad']]);assert all(v>=0 for row in T for v in row)
    Hr=density(T,True);Hpr=hjets(Hr);Fr=forcing(Hr,True);Fpr=[differentiate(row) for row in Fr]
    ar,br=velocity(pr,rr,True)
    # Remainder radii are constants; the ODE maps require no derivative bound.
    arem=[[0] for _ in range(3)];brem=[[0] for _ in range(3)]
    for n,(p,r) in enumerate(zip(prem,rrem),1):
        m=2*n
        for l,va,vb in [(0,p,r),(1,2*p+m*r,m*p+2*r),(2,(4+m*m)*p+4*m*r,4*m*p+(4+m*m)*r)]:arem[l][0]+=va;brem[l][0]+=vb
    norms={}
    def store(name,rows,e,angle=False):norms[name]={'coeff':sumabs(rows,angle),'power':e,'denominator':1}
    for p in range(3):
        store('A'+str(p),model['Aj'][p],model['ep']);store('B'+str(p),model['Bj'][p],model['ep'])
        store('eA'+str(p),ar[p],er);store('eB'+str(p),br[p],er)
        norms['remA'+str(p)]={'coeff':arem[p],'power':erem,'denominator':1};norms['remB'+str(p)]={'coeff':brem[p],'power':erem,'denominator':1}
    for p in range(4):
        store('H'+str(p),model['Hp'][p],model['eh']);store('TH'+str(p),model['Hp'][p],model['eh'],True)
        store('eH'+str(p),Hpr[p],etr-3);store('eTH'+str(p),Hpr[p],etr-3,True)
    for name,rows,e in [('F',model['F'],model['ef']),('Fp',model['Fp'],model['ef']),('eF',Fr,etr-4),('eFp',Fpr,etr-4)]:store(name,rows,e)
    store('mF',[[2*n*v for v in row] for n,row in enumerate(model['F'],1)],model['ef'])
    store('emF',[[2*n*v for v in row] for n,row in enumerate(Fr,1)],etr-4)
    return norms

def validate_actual_linear_maps(model):
    """All actual input coefficients, separately derived polar map and ODE iteration."""
    H=model['H'];Hp=model['Hp'];F2=[[0]*8 for _ in range(261)];count=0
    for j,row in enumerate(H[:261]):
        q=2*j+1
        for l,v in enumerate(row):
            dr=3*v+((l+1)*row[l+1] if l<7 else 0)
            # 2 cos(theta)(D+3)H sin(qtheta)-2 sin(theta)qH cos(qtheta).
            for freq,coef in [(q+1,dr),(q-1,dr),(1+q,-q*v),(1-q,-q*v)]:
                if freq:
                    n=abs(freq)//2;assert 1<=n<=261
                    F2[n-1][l]+=(1 if freq>0 else -1)*coef
    assert F2==model['F'];count+=261*8
    for n in range(261):
        m=2*(n+1)
        for l in range(13):
            a=model['Aj'][0][n][l];b=model['Bj'][0][n][l]
            for p in range(1,3):
                a,b=-2*a+m*b,m*a-2*b
                assert a==model['Aj'][p][n][l] and b==model['Bj'][p][n][l];count+=2
    # Validate every actual H jet coefficient independently of the packed products.
    for p in range(4):
        for j,row in enumerate(H):
            for l in range(8):
                direct=sum(math.comb(p,k)*3**(p-k)*math.factorial(l+k)//math.factorial(l)*row[l+k] for k in range(min(p,7-l)+1))
                assert direct==Hp[p][j][l];count+=1
    return count
