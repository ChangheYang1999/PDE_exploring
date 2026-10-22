"""Independent exact polynomial tail moments and center-preserving repair,130."""
from fractions import Fraction as Q
import json,hashlib
from pathlib import Path


def trim(a):
    a=list(map(Q,a))
    while a and not a[-1]:a.pop()
    return a

def add(*ps):
    out=[Q(0)]*max([len(p)for p in ps]+[0])
    for p in ps:
        for i,c in enumerate(p):out[i]+=c
    return trim(out)

def scale(p,c):return trim([Q(c)*v for v in p])
def mul(p,q):
    out=[Q(0)]*max(0,len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return trim(out)

def diff(p):return trim([i*p[i]for i in range(1,len(p))])
def cheb(n):
    a,b=[Q(1)],[Q(0),Q(1)]
    if not n:return a
    for _ in range(1,n):a,b=b,add(mul([0,2],b),scale(a,-1))
    return b

def D(p):return add(mul([1,0,-1],diff(p)),mul([0,-1],p))
def L(k,p):return add(scale(p,k*k-1),mul([0,-3],diff(p)),mul([1,0,-1],diff(diff(p))))
def moment(m,h,sigma):return sum((v*Q(sigma)**i/(i-m)for i,v in enumerate(h)),Q(0))
def source(beta,p,p1):
    s=1/Q(beta);q=scale(L(2-s,p),-1)
    return add(L(2-2*s,p1),scale(mul(D(p),q),s),scale(mul(p,D(q)),2-s))

def leading_polynomials(beta,labels,C):
    beta=Q(beta)
    if beta<=2:raise ValueError('beta>2 required')
    p,p1=[],[]
    for (i,j,d),cc in zip(labels,C):
        if d not in [0,1]:raise ValueError('unsupported shift')
        if d:continue
        c=Q(cc);t=cheb(j)
        p=add(p,scale(t,c*((-1)**i)))
        if i:p1=add(p1,scale(t,c*2*((-1)**(i-1))*i*i))
    return p,p1

def primitive_polynomial(m,h):
    Qpoly=[]
    for j,v in enumerate(h):Qpoly.append((Qpoly[j-2]if j>=2 else Q(0))+v/(m-j))
    Qpoly=trim(Qpoly)
    if len(Qpoly)>max(0,len(h)-2):return None
    return Qpoly

def data(beta,labels,C):
    beta=Q(beta);m=1-2/beta;p,p1=leading_polynomials(beta,labels,C);h=source(beta,p,p1)
    cp,cm=moment(m,h,1),moment(m,h,-1);temp=primitive_polynomial(m,h)if cp==cm==0 else None
    return {'beta':beta,'m':m,'p':p,'p1':p1,'h':h,'C_plus':cp,'C_minus':cm,'Q_temperature':temp}

def directions(labels):
    labels=list(map(tuple,labels));d0=[Q(0)]*len(labels);d1=d0.copy()
    for i,v in enumerate([Q(1,16),-Q(1,32),-Q(1,16),Q(1,32)]):d0[labels.index((i,0,0))]=v
    d1[labels.index((0,1,0))]=Q(1,8);d1[labels.index((2,1,0))]=-Q(1,8)
    return d0,d1

def repair(beta,labels,C):
    C=list(map(Q,C));r=data(beta,labels,C);m=r['m'];a=(r['C_plus']+r['C_minus'])/(2*(m+2));b=(r['C_plus']-r['C_minus'])/(2*(m+3));h0,h1=directions(labels)
    out=[c+a*u+b*v for c,u,v in zip(C,h0,h1)];z=data(beta,labels,out)
    assert z['C_plus']==z['C_minus']==0 and z['p']==r['p']
    return out,{'a':a,'b':b,'before':r,'after':z}

def serialized(d):
    if isinstance(d,Q):return str(d)
    if isinstance(d,list):return [serialized(t)for t in d]
    if isinstance(d,dict):return {k:serialized(v)for k,v in d.items()}
    return d

def certificate(path):
    path=Path(path);state=json.loads(path.read_text());r=data(state['beta'],state['labels'],state['C'])
    return {'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'exact':serialized(r),
            'verdict':'CONFIRMED_LEADING_PRIMITIVE_COMPATIBILITY'if r['C_plus']==r['C_minus']==0 else'REFUTED_SMOOTH_LEADING_ANGULAR_PRIMITIVE',
            'scope':'Exact conditions for the leading homogeneous primitive. No nearby-profile bound. Actual primitive convergence and angular derivative convergence require the hypotheses in PROOF.md.'}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();out=args.root/'primitive_tail_certificates';out.mkdir(exist_ok=True);summary=[]
    for path in sorted(args.root.glob('*_state.json')):
        cert=certificate(path);dest=out/(path.stem+'_certificate.json');dest.write_text(json.dumps(cert,indent=2)+'\n')
        r=cert['exact'];summary.append({'state':path.name,'sha256':cert['sha256'],'beta':float(Q(r['beta'])),'C_plus':float(Q(r['C_plus'])),'C_minus':float(Q(r['C_minus'])),'verdict':cert['verdict'],'certificate':str(dest.relative_to(args.root))})
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('certificates',len(summary),flush=True)
