"""Independent full radial Green reconstruction from original modal NPZ."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial,comb
from collections import Counter
import argparse,bisect,hashlib,json,time
import numpy as np
from flint import arb,arb_mat,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
SOURCE=LANE/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
SCALAR=LANE/'proofs/04_modal_scalar/evidence/recomputed.json'
def now():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def rat(x):return F.from_float(float(x))
def aa(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def record(x):
    def q(v):
        m,e=v.man_exp();return F(int(m))*F(2)**int(e)
    return {'ball':x.str(60),'lower_exact':str(q(x.lower())),'upper_exact':str(q(x.upper()))}
def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out
def linear(a,c,d):
    out=[F(0)]*(len(a)+1)
    for i,x in enumerate(a):out[i]+=c*x;out[i+1]+=d*x
    return out
def endpoint_jets(knots,co):
    values=[];degree=7
    for j in range(7):
        values.append(co[0])
        co=[degree*(co[i+1]-co[i])/(knots[i+degree+1]-knots[i+1]) for i in range(len(co)-1)]
        knots=knots[1:-1];degree-=1
    return values
def match(jets,nonjets,b):
    diff=[x-y for x,y in zip(jets,nonjets)]
    out=[sum(((-b)**(i-j)*diff[j]/(factorial(i-j)*factorial(j)) for j in range(i+1)),F(0)) for i in range(7)]
    for j in range(7):assert sum((F(comb(j,i))*b**(j-i)*factorial(i)*out[i] for i in range(j+1)),F(0))==diff[j]
    return out
def projection():
    out=[]
    for m in range(260):
        d={}
        for f in (1+2*m,1-2*m,3+2*m,3-2*m):
            n=(abs(f)-1)//2;d[n]=d.get(n,F(0))+F(1 if f>0 else -1,8)
        out.append([(n,w) for n,w in d.items() if w])
    return out
P=projection()
def project_mode_rows(rows):
    cols=len(rows[0]);out=[[arb(0) for j in range(cols)] for n in range(262)]
    for m,row in enumerate(rows):
        values=[aa(v) for v in row]
        for n,w in P[m]:
            for j,v in enumerate(values):out[n][j]+=aa(w)*v
    return out
def phi_direct(z):
    if z==0:return [arb(1)/(j+1) for j in range(8)]
    assert not z.contains(0)
    ez=z.exp();out=[(ez-1)/z]
    for j in range(1,8):out.append((ez-j*out[-1])/z)
    return out
def phi_series(z,N=128):
    out=[arb(0) for j in range(8)];term=arb(1)
    for n in range(N):
        for j in range(8):out[j]+=term/(j+n+1)
        term*=z/(n+1)
    M=abs(z).upper();tail=M.exp()*M**N/factorial(N)
    return [v+arb(0,(tail/(N+j+1)).upper()) for j,v in enumerate(out)]
def shift_rows(rows,u,h):
    return [[sum((aa(comb(l,j))*rows[l][n]*u**(l-j) for l in range(j,8)),arb(0))/h**j for n in range(262)] for j in range(8)]

class Data:
    def __init__(self):
        raw=np.load(SOURCE,allow_pickle=False);self.sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        assert self.sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
        assert int(raw['M'])==260 and int(raw['p'])==7
        self.knots=[rat(v) for v in raw['knots']];t=self.knots
        assert t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8
        assert all(t[j]<t[j+1] for j in range(7,len(t)-8))
        self.spans=[j for j in range(7,len(t)-8) if t[j]<t[j+1]];assert len(self.spans)==1558
        self.k=rat(raw['k']);self.L=rat(raw['L']);self.bi=rat(raw['bi']);self.bo=rat(raw['bo'])
        self.tm=t[0];self.tp=t[-1];assert 0<self.k<F(1,2) and self.bi>4 and self.bo>3-self.k
        pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
        self.alphas=[self.k-3-j*(1-self.k)-2*l for j,l in pairs]
        sr=json.loads(SCALAR.read_text());assert sr['input_sha256']==self.sha
        self.z=arb(sr['normalization_correction_z']['ball']);assert self.z<0
        D=[[rat(v) for v in row] for row in raw['D']]
        A=[[rat(v) for v in row] for row in raw['Aout']]
        Ei=[];Eo=[]
        for m in range(260):
            co=[rat(v) for v in raw['S'][m,:8]];jm=endpoint_jets(t[:],co)
            co=[rat(v) for v in raw['S'][m,-8:][::-1]]
            jp=[(-1)**j*v for j,v in enumerate(endpoint_jets([-x for x in t[::-1]],co))]
            inn=[F(m==0 and j==0)+sum((D[m][l]*(2*l+2)**j for l in range(7)),F(0)) for j in range(7)]
            out=[sum((A[m][l]*self.alphas[l]**j for l in range(10)),F(0)) for j in range(7)]
            Ei.append(match(jm,inn,self.bi));Eo.append(match(jp,out,-self.bo))
        self.D=project_mode_rows(D);self.Ei=project_mode_rows(Ei)
        # Change the exact outer object by z, including its matched correction.
        A=[[aa(x) for x in row] for row in A];Eo=[[aa(x) for x in row] for row in Eo]
        A[0][0]+=self.z
        for j in range(7):Eo[0][j]-=self.z*aa((self.alphas[0]+self.bo)**j/F(factorial(j)))
        self.A=project_mode_rows(A);self.Eo=project_mode_rows(Eo)
        self.constant=project_mode_rows([[F(int(m==0))] for m in range(260)])
        self.control=[]
        for j in range(raw['S'].shape[1]):
            values=[aa(rat(v)) for v in raw['S'][:,j]];out=[arb(0) for n in range(262)]
            for m,value in enumerate(values):
                for n,w in P[m]:out[n]+=aa(w)*value
            assert out[-1]==0;self.control.append(out)
        self.reverse=arb_mat([[(-1)**j*comb(l,j) if l>=j else 0 for l in range(8)] for j in range(8)])
        self.widthcounts=Counter(t[j+1]-t[j] for j in self.spans);self.moment_cache={};self.audits=[]
    def poly(self,span):
        t=self.knots;a,b=t[span:span+2];h=b-a;basis={span:[F(1)]}
        for d in range(1,8):
            nb={}
            for i in range(span-d,span+1):
                u=v=[F(0)]
                if i in basis and t[i+d]!=t[i]:u=linear(basis[i],(a-t[i])/(t[i+d]-t[i]),h/(t[i+d]-t[i]))
                if i+1 in basis and t[i+d+1]!=t[i+1]:v=linear(basis[i+1],(t[i+d+1]-a)/(t[i+d+1]-t[i+1]),-h/(t[i+d+1]-t[i+1]))
                nb[i]=add(u,v)
            basis=nb
        assert [sum((v[j] for v in basis.values()),F(0)) for j in range(8)]==[F(1)]+[F(0)]*7
        weights=arb_mat([[aa(basis[i][j]) for i in range(span-7,span+1)] for j in range(8)])
        return weights*arb_mat(self.control[span-7:span+1])
    def initial(self,side):
        out=[]
        for n in range(1,262):
            m=2*n
            if side=='I':
                index=n-1;v=self.constant[index][0]/(m+4)
                v+=sum((self.D[index][j]/(m+6+2*j) for j in range(7)),arb(0))
                v+=sum((self.Ei[index][j]*(-1)**j*factorial(j)/aa(m+4+self.bi)**(j+1) for j in range(7)),arb(0))
            else:
                index=n;assert all(m-4-a>0 for a in self.alphas) and m-4+self.bo>0
                v=sum((self.A[index][j]/aa(m-4-self.alphas[j]) for j in range(10)),arb(0))
                v+=sum((self.Eo[index][j]*factorial(j)/aa(m-4+self.bo)**(j+1) for j in range(7)),arb(0))
            out.append(v)
        return out
    def moments(self,h,lam):
        key=(h,lam)
        if key in self.moment_cache:return self.moment_cache[key]
        z=aa(lam*h);values=phi_direct(z);ez=z.exp()
        if self.widthcounts[h]>=3:self.moment_cache[key]=(ez,values)
        if len(self.audits)<20 and lam in (-6,-526,0,2) and (not self.audits or str(h)!=self.audits[-1]['width']):
            alt=phi_series(z)
            assert all(a.overlaps(b) for a,b in zip(values,alt))
            self.audits.append({'width':str(h),'lambda':lam,'check':'direct primitive overlaps independent 128-term series'})
        return ez,values
    def propagate(self,side,target):
        vals=self.initial(side)
        spans=[i for i in self.spans if i<target] if side=='I' else [i for i in self.spans[::-1] if i>target]
        for count,span in enumerate(spans,1):
            h=self.knots[span+1]-self.knots[span];mat=self.poly(span)
            if side=='I':mat=self.reverse*mat
            rows=mat.tolist()
            for n in range(1,262):
                index=n-1 if side=='I' else n;lam=-2*n-4 if side=='I' else 4-2*n
                ez,phi=self.moments(h,lam)
                vals[n-1]=ez*vals[n-1]+aa(h)*sum((rows[j][index]*phi[j] for j in range(8)),arb(0))
                assert vals[n-1].is_finite()
            if count%100==0 or count==len(spans):emit(stage='propagation',side=side,spans_done=count,spans_total=len(spans))
        return vals
    def evaluate(self,x,span,rows,Ileft,Jright):
        a,b=self.knots[span:span+2];h=aa(b-a);t=x.log();ell=t-aa(a);rr=aa(b)-t
        assert ell>0 and rr>0
        H=shift_rows(rows,ell/h,h);IV=[];JV=[]
        for n in range(1,262):
            m=2*n;pi=phi_series(-(m+4)*ell);pj=phi_series((4-m)*rr)
            ii=(-(m+4)*ell).exp()*Ileft[n-1]+sum(((-1)**j*H[j][n-1]*ell**(j+1)*pi[j] for j in range(8)),arb(0))
            jj=((4-m)*rr).exp()*Jright[n-1]+sum((H[j][n]*rr**(j+1)*pj[j] for j in range(8)),arb(0))
            IV.append(ii);JV.append(jj)
        S=sum((2*n*(IV[n-1]-JV[n-1]) for n in range(1,262)),arb(0))
        C=sum((2*n*((2*n+1)*IV[n-1]+(2*n-1)*JV[n-1]-H[0][n-1]-H[0][n]) for n in range(1,262)),arb(0))
        w=x/aa(self.k)+x**3*S/2;mu=1/aa(self.k)+x*x*C/2;wp=1/aa(self.k)-x*x*C/2
        g=x*x*sum(((2*j+1)*H[0][j] for j in range(262)),arb(0))
        assert (wp+mu).overlaps(2/aa(self.k))
        return dict(w=w,mu=mu,wprime=wp,g=g)

def main(args):
    ctx.prec=args.bits;ctx.threads=1;start=time.monotonic();d=Data()
    a=F(4841405518533377,562949953421312);b=F(4841405518533711,562949953421312)
    mid=aa((a+b)/2).log();span=next(i for i in d.spans if aa(d.knots[i])<mid<aa(d.knots[i+1]))
    assert aa(d.knots[span])<aa(a).log() and aa(b).log()<aa(d.knots[span+1])
    emit(stage='prepared',span=span,source_left=str(d.knots[span]),source_right=str(d.knots[span+1]),seconds=time.monotonic()-start)
    IL=d.propagate('I',span);JR=d.propagate('J',span);rows=d.poly(span).tolist();results={}
    for label,x in [('a',aa(a)),('b',aa(b)),('whole',aa(a).union(aa(b)))]:
        values=d.evaluate(x,span,rows,IL,JR);results[label]={k:record(v) for k,v in values.items()}
        if label=='a':assert values['w']<0
        if label=='b':assert values['w']>0
        if label=='whole':
            for key,lo,hi in [('wprime',10,F(51,5)),('mu',F(99,100),F(101,100)),('g',29,30)]:assert aa(lo)<values[key]<aa(hi),(key,record(values[key]))
        emit(stage='source',label=label,values=results[label],seconds=time.monotonic()-start)
    out={'date':now(),'status':'COMPUTED_PENDING_OUTPUT_AUDIT','input_sha256':d.sha,'scalar_input_sha256':hashlib.sha256(SCALAR.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'bits':args.bits,'source_bracket':[str(a),str(b)],'source_span':[str(d.knots[span]),str(d.knots[span+1])],'all_radial_spans':len(d.spans),'stream_modes':261,'scalar_correction':record(d.z),'results':results,'moment_crosschecks':d.audits,'seconds':time.monotonic()-start,'scope':'exact normalized modal source; no raw X3 source or global inverse'}
    (TOP/'evidence'/f'{args.tag}_result.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='finished',seconds=out['seconds'])
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=512);ap.add_argument('--tag',default='source_512');main(ap.parse_args())
