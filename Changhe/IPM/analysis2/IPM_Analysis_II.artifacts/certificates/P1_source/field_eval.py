"""Independent fourth-order Cartesian jet evaluator of exact checkpoint potentials.
Only this lane's exact reconstruction JSON is read. No archived or sibling evaluator is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
from flint import arb,acb,ctx
import json
ORDER=4
INDICES=[(i,j) for i in range(ORDER+1) for j in range(ORDER+1-i)]

def aa(v):
    if isinstance(v,arb):return v
    r=Q(v);return arb(r.numerator)/arb(r.denominator)

def multiply(a,b):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=ORDER:c[i+k,j+l]=c.get((i+k,j+l),arb(0))+v*w
    return c

class State:
    def __init__(self,state=131,precision=256):
        ctx.prec=precision
        self.state=state
        self.data=json.loads(Path(__file__).with_name(f'state{state:03d}_exact.json').read_text())
        self.cl=aa(self.data['exact_parameters']['cl'])
        self.gamma=1/self.cl
        self.groups={}
        for (j,m,k),value in zip(self.data['canonical_order'],self.data['canonical_coefficients']):
            self.groups.setdefault((j,m),[]).append((k-m,aa(value)))
    def evaluate(self,x,y,include_potential_jet=False):
        x=aa(x);y=aa(y);q=x*x+y*y
        assert q>0, 'Use exact origin data at the origin; interval boxes containing q=0 need a Taylor enclosure.'
        oq=1+q;v=q/oq
        qdelta={(1,0):2*x,(0,1):2*y,(2,0):arb(1),(0,2):arb(1)}
        qp=[{(0,0):arb(1)}]
        for _ in range(ORDER):qp.append(multiply(qp[-1],qdelta))
        z=acb(x,y);zp=[acb(1)]
        for _ in range(18):zp.append(zp[-1]*z)
        hjet={}
        for m in range(10):
            n=2*m;jet={}
            for i,jj in INDICES:
                if i+jj>n:continue
                coeff=arb(factorial(n)//factorial(n-i-jj))/arb(factorial(i)*factorial(jj))
                # Re(i^jj z^(n-i-jj)), no floating complex constants.
                w=zp[n-i-jj]
                real=[w.real,-w.imag,-w.real,w.imag][jj%4]
                jet[i,jj]=coeff*real
            hjet[m]=jet
        chi={ij:arb(0) for ij in INDICES}
        for (branch,m),terms in self.groups.items():
            p=(3+self.gamma-branch*(1-self.gamma))/2
            pf=(oq**(p-m));radial=[arb(0) for _ in range(ORDER+1)]
            vp=arb(1)
            for l,coeff in terms:
                if l==0:vp=arb(1)
                else:vp*=v
                base=coeff*pf*vp
                u=p-m-l
                qa=[arb(comb(l,k))/(q**k) if k<=l else arb(0) for k in range(ORDER+1)]
                ob=[arb(1)]
                for k in range(1,ORDER+1):ob.append(ob[-1]*(u-k+1)/(k*oq))
                for d in range(ORDER+1):
                    radial[d]+=base*sum((qa[k]*ob[d-k] for k in range(d+1)),arb(0))
            fjet={ij:arb(0) for ij in INDICES}
            for k,co in enumerate(radial):
                for ij,value in qp[k].items():fjet[ij]+=co*value
            term=multiply(hjet[m],fjet)
            for ij,value in term.items():chi[ij]+=value
        for (i,j),value in chi.items():chi[i,j]=value*factorial(i)*factorial(j)
        rho=-chi[2,1]-chi[0,3]
        rx=-chi[3,1]-chi[1,3];ry=-chi[2,2]-chi[0,4]
        u1=-chi[1,2];u2=chi[2,1]
        b=2*self.cl+1
        m11=b-2*chi[2,2]-chi[0,4];m22=b+chi[2,2];m12=chi[3,1]
        least=(m11+m22-((m11-m22)**2+4*m12*m12).sqrt())/2
        result={'rho':rho,'rho_x':rx,'rho_y':ry,'psi':chi[1,1],
                'u1':u1,'u2':u2,'du11':-chi[2,2],'du12':-chi[1,3],
                'du21':chi[3,1],'du22':chi[2,2],
                'M11':m11,'M12':m12,'M22':m22,'lambda_min_M':least,
                'K':rho-x*rx-y*ry,'residual':(self.cl*x+u1)*rx+(self.cl*y+u2)*ry-rho}
        if include_potential_jet:
            result['potential_derivatives']=chi
        return result

if __name__=='__main__':
    from datetime import datetime,timezone
    import argparse,time
    parser=argparse.ArgumentParser();parser.add_argument('--state',type=int,default=131)
    args=parser.parse_args()
    state=State(args.state,320)
    points=[('0','0.001'),('0','0.1'),('0','1'),('0.5','0.5'),('1','1'),('0','10'),('10','10'),('0','1000')]
    records=[];start=time.monotonic()
    for x,y in points:
        data=state.evaluate(x,y)
        rec={'x':x,'y':y,'fields':{k:v.str(65) for k,v in data.items()}}
        records.append(rec)
        print(args.state,x,y,'Mmin',data['lambda_min_M'].str(16),'R',data['residual'].str(16),flush=True)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':args.state,'precision_bits':320,'elapsed_seconds':time.monotonic()-start,'scope':'Certified individual point enclosures. No assertion between points.','points':records}
    Path(__file__).with_name(f'state{args.state:03d}_field_points.json').write_text(json.dumps(out,indent=2)+'\n')
