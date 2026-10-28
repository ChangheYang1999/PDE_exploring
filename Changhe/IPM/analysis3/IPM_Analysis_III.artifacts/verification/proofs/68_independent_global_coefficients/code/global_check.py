"""Independent original-input Green reconstruction and coefficient boxes."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from datetime import datetime,timezone
import argparse,importlib.util,json,gzip,hashlib,time
from flint import arb,arb_mat,ctx
TOP=Path(__file__).resolve().parents[1]; LANE=TOP.parents[1]
spec=importlib.util.spec_from_file_location('own_source',LANE/'proofs/66_source_zero_exclusion/code/certify.py')
C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
M=C.M;aa=C.aa
# The finite recurrence is also a rigorous interval formula. At512 bits it
# avoids the cost of summing128 terms for each small, nonzero moment.
slow_phi=M.phi_series
M.phi_series=M.phi_direct
CACHE=TOP/'evidence/boundaries.json.gz'
def now():return datetime.now(timezone.utc).isoformat()
def emit(**x):print(json.dumps({'date':now(),**x}),flush=True)
def rec(x):return M.record(x)
def jwrite(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n')
def check_hash(d):assert d.sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
def prepare():
    start=time.monotonic();d=M.Data();check_hash(d);left=[];right={};v=d.initial('I')
    for c,i in enumerate(d.spans):
        left.append([z.str(100) for z in v]);h=d.knots[i+1]-d.knots[i]
        rows=(d.reverse*d.poly(i)).tolist()
        for n in range(1,262):
            ez,ph=d.moments(h,-2*n-4)
            v[n-1]=ez*v[n-1]+aa(h)*sum((rows[j][n-1]*ph[j] for j in range(8)),arb(0))
        if c%100==0:emit(stage='forward',cell=c,seconds=time.monotonic()-start)
    outerI=[z.str(100) for z in v];v=d.initial('J')
    for c,i in enumerate(d.spans[::-1]):
        right[i]=[z.str(100) for z in v];h=d.knots[i+1]-d.knots[i];rows=d.poly(i).tolist()
        for n in range(1,262):
            ez,ph=d.moments(h,4-2*n)
            v[n-1]=ez*v[n-1]+aa(h)*sum((rows[j][n]*ph[j] for j in range(8)),arb(0))
        if c%100==0:emit(stage='backward',cell=c,seconds=time.monotonic()-start)
    # Independent series checks at representative exact widths and all
    # coefficients of the eight moments, including zero and both signs.
    checks=0
    for h in sorted(set(d.knots[i+1]-d.knots[i] for i in d.spans))[::max(1,len(d.widthcounts)//8)]:
        for lam in (-526,-58,-6,0,2):
            z=aa(lam*h);direct=M.phi_direct(z);series=slow_phi(z,N=256)
            assert all(x.overlaps(y) for x,y in zip(direct,series));checks+=8
    out={'date':now(),'status':'PREPARED','bits':ctx.prec,'input_sha256':d.sha,
         'scalar_sha256':hashlib.sha256(M.SCALAR.read_bytes()).hexdigest(),
         'spans':d.spans,'knots':[str(x) for x in d.knots],
         'I_left':left,'J_right':[right[i] for i in d.spans],
         'I_outer':outerI,'J_inner':[z.str(100) for z in v],
         'moment_series_crosschecks':checks,'seconds':time.monotonic()-start}
    with gzip.open(CACHE,'wt') as f:json.dump(out,f)
    emit(stage='prepared',seconds=out['seconds'],cache_bytes=CACHE.stat().st_size)

class EP:
    def __init__(self,terms=None):self.terms={} if terms is None else {F(k):list(v) for k,v in terms.items()}
    def addterm(self,e,p):
        e=F(e);old=self.terms.setdefault(e,[])
        old.extend([arb(0)]*max(0,len(p)-len(old)))
        for j,v in enumerate(p):old[j]+=v
        return self
    def __add__(self,q):
        r=EP(self.terms)
        for e,p in q.terms.items():r.addterm(e,p)
        return r
    def scale(self,c):return EP({e:[aa(c)*v for v in p] for e,p in self.terms.items()})
    def expmul(self,e):return EP({k+F(e):v for k,v in self.terms.items()})
    def deriv(self):return EP({e:[aa(e)*p[j]+(j+1)*p[j+1] if j+1<len(p) else aa(e)*p[j] for j in range(len(p))] for e,p in self.terms.items()})
    def shift(self,s):
        s=aa(s);out=EP()
        for e,p in self.terms.items():
            fac=(aa(e)*s).exp()
            out.addterm(e,[fac*sum((comb(l,j)*p[l]*s**(l-j) for l in range(j,len(p))),arb(0)) for j in range(len(p))])
        return out
    def atzero(self):return sum((p[0] for p in self.terms.values()),arb(0))
    def particular(self,a):
        out=EP()
        for e,p in self.terms.items():
            den=e+F(a);assert den!=0
            q=[arb(0)]*len(p)
            for j in range(len(p)-1,-1,-1):q[j]=(p[j]-(j+1)*q[j+1] if j+1<len(p) else p[j])/aa(den)
            out.addterm(e,q)
        return out
    def range(self,mid,rad,N=28):
        q=self.shift(mid);h=aa(rad);coef=[arb(0)]*(N+1);err=arb(0)
        for e,p in q.terms.items():
            powers=[arb(1)]
            for j in range(1,N+1):powers.append(powers[-1]*aa(e)/j)
            for k,v in enumerate(p):
                assert k<=N
                for j in range(k,N+1):coef[j]+=v*powers[j-k]
                z=aa(abs(e))*h
                err+=arb(v.abs_upper())*h**k*z.exp()*z**(N-k+1)/factorial(N-k+1)
        return C.horner(coef,arb(0,h.upper()))+arb(0,err.upper())
    def sup_left(self):
        out=arb(0)
        for e,p in self.terms.items():
            assert e>0
            out+=sum((arb(v.abs_upper())*factorial(j)/aa(e)**j for j,v in enumerate(p)),arb(0))
        return out.upper()
    def sup_right(self,shift):
        out=arb(0)
        for e,p in self.shift(shift).terms.items():
            assert e<0
            out+=sum((arb(v.abs_upper())*factorial(j)/aa(-e)**j for j,v in enumerate(p)),arb(0))
        return out.upper()

def density_eps(d,side):
    out=[]
    for j in range(262):
        h=EP()
        if side=='inner':
            h.addterm(0,d.constant[j])
            for l in range(7):h.addterm(2*l+2,[d.D[j][l]])
            h.addterm(d.bi,d.Ei[j])
        else:
            for l in range(10):h.addterm(d.alphas[l],[d.A[j][l]])
            h.addterm(-d.bo,d.Eo[j])
        out.append(h)
    return out

def outer_eps(d,cache):
    H=density_eps(d,'outer');I0=list(map(arb,cache['I_outer']));P=[];Q=[];fac=(2*aa(d.tp)).exp()
    for n in range(1,262):
        a=2*n+4;b=2*n-4
        i=H[n-1].particular(a);i.addterm(-a,[I0[n-1]-i.atzero()])
        j=H[n].particular(-b).scale(-1)
        P.append((j+i.scale(-1)).expmul(2).scale(n*fac))
        Q.append((j+i).scale(n).__add__((H[n]+H[n-1]).scale(F(-1,2))).expmul(2).scale(fac))
    GR=[(h.scale(3)+h.deriv()).expmul(2).scale(fac) for h in H]
    GT=[h.expmul(2).scale((2*j+1)*fac) for j,h in enumerate(H)]
    return P,Q,GR,GT

KNOTS=list(map(F,['3/2','7/4','3','4','5','6','7','8','9','10']))
MU=[F(v,16) for v in (4,17,28,27,25,18,4,-10,-17,-19,-20)]
def mu_values(l,r):
    return [v for i,v in enumerate(MU) if not (i and r<KNOTS[i-1]) and not (i<len(KNOTS) and l>KNOTS[i])]
def hull_rationals(xs):return aa(min(xs)).union(aa(max(xs)))
class Angular:
    def __init__(self,count):
        self.count=count;self.theta=[];self.s=[];self.c=[]
        for j in range(count):
            t=(arb.pi()*j/(2*count)).union(arb.pi()*(j+1)/(2*count));self.theta.append(t);self.s.append(t.sin());self.c.append(t.cos())
        self.c2=arb_mat([[(2*n*t).cos() for t in self.theta] for n in range(1,262)])
        self.s2=arb_mat([[(2*n*t).sin() for t in self.theta] for n in range(1,262)])
        self.sj=arb_mat([[((2*j+1)*t).sin() for t in self.theta] for j in range(262)])
        self.cj=arb_mat([[((2*j+1)*t).cos() for t in self.theta] for j in range(262)])
        self.tang=arb_mat([[self.s[k]*2*sum(((-1)**(n-j)*((2*j-1)*t).sin() for j in range(1,n+1)),arb(0)) if n<=8 else arb(0,2*n) for k,t in enumerate(self.theta)] for n in range(1,262)])
    def dot(self,v,a):return (arb_mat([v])*a).tolist()[0]
    def boxes(self,P,Q,GR,GT,l,r,ell):
        q=[ell-x for x in self.dot(P,self.c2)];tan=self.dot(Q,self.tang)
        rr=self.dot(GR,self.sj);rt=self.dot(GT,self.cj)
        d=ell-sum(((-1)**n*P[n-1] for n in range(1,262)),arb(0))
        muv=hull_rationals(mu_values(l,r));mua=hull_rationals(([F(-17,2)] if l<=0 else [])+([F(-5,4)] if r>=0 else []))
        out=[]
        for k in range(self.count):
            gu=(arb(rr[k].abs_upper())**2+arb(rt[k].abs_upper())**2).sqrt().upper()
            dy=rr[k]*self.s[k]+rt[k]*self.c[k]
            bp=(gu-dy.lower())/2
            kap=1+ell+mua*q[k]/2+aa(F(17,4))*tan[k]
            ma=kap-bp;mr=1+ell+muv*q[k]/2-bp
            assert all(v.is_finite() for v in (ma,mr,kap,gu,d,q[k]))
            out.append((ma.lower(),mr.lower(),kap.lower(),gu,q[k]))
        return d,out

def load_cache(d):
    with gzip.open(CACHE,'rt') as f:cache=json.load(f)
    assert cache['input_sha256']==d.sha and cache['spans']==d.spans
    assert cache['knots']==[str(x) for x in d.knots]
    assert cache['scalar_sha256']==hashlib.sha256(M.SCALAR.read_bytes()).hexdigest()
    return cache

def finite(args):
    start=time.monotonic();d=M.Data();check_hash(d);cache=load_cache(d);ang=Angular(args.angular);ell=1/aa(d.k)
    records=[];global_ma=arb.pos_inf();global_mr=arb.pos_inf();global_d=arb.pos_inf();global_kap=arb.pos_inf();global_gr=arb(0)
    def add(label,l,r,P,Q,GR,GT):
        nonlocal global_ma,global_mr,global_d,global_kap,global_gr
        dv,boxes=ang.boxes(P,Q,GR,GT,l,r,ell)
        ma=min(x[0] for x in boxes);mr=min(x[1] for x in boxes);kap=min(x[2] for x in boxes);gr=max(x[3] for x in boxes)
        global_ma=min(global_ma,ma);global_mr=min(global_mr,mr);global_d=min(global_d,dv.lower());global_kap=min(global_kap,kap);global_gr=max(global_gr,gr)
        records.append({'label':label,'left_exact':str(l),'right_exact':str(r),'d':rec(dv),'ma_lower':rec(ma),'mr_lower':rec(mr),'kappa_lower':rec(kap),'gradient_upper':rec(gr),'ma_argmin':min(range(len(boxes)),key=lambda k:boxes[k][0])})
        if len(records)%40==0:emit(stage='finite',cells=len(records),ma=global_ma.str(12),mr=global_mr.str(12),d=global_d.str(12),seconds=time.monotonic()-start)
    if args.part in ('all','middle'):
        for idx,i in enumerate(d.spans):
            if idx<args.start or idx>=args.stop:continue
            a,b=d.knots[i:i+2];rows=d.poly(i).tolist();IL=list(map(arb,cache['I_left'][idx]));JR=list(map(arb,cache['J_right'][idx]))
            for sub in range(args.radial):
                l=a+(b-a)*sub/args.radial;r=a+(b-a)*(sub+1)/args.radial
                mid=aa((l+r)/2);rad=aa((r-l)/2);H,S,rem=C.local_series(rows,IL,JR,a,b,mid,rad)
                v=arb(0,rad.upper());r2=(2*aa(l)).union(2*aa(r)).exp();P=[];Q=[]
                for n in range(1,262):
                    s=C.horner(S[n-1],v)+arb(0,rem[n-1][0])
                    sp=C.horner([(j+1)*S[n-1][j+1] for j in range(C.N)],v)+arb(0,rem[n-1][1])
                    P.append(2*n*r2*s);Q.append(r2*(4*s+sp))
                GR=[];GT=[]
                for j in range(262):
                    h=C.horner([H[p][j] for p in range(8)],v)
                    hp=C.horner([(p+1)*H[p+1][j] for p in range(7)],v)
                    GR.append(r2*(3*h+hp));GT.append(r2*(2*j+1)*h)
                add(['spline',i,sub],l,r,P,Q,GR,GT)
    if args.part in ('all','outer'):
        pe,qe,gre,gte=outer_eps(d,cache)
        for i in range(args.outer_cells):
            l=F(8*i,args.outer_cells);r=F(8*(i+1),args.outer_cells);mid=(l+r)/2;rad=(r-l)/2
            P=[ep.range(mid,rad) for ep in pe];Q=[ep.range(mid,rad) for ep in qe]
            GR=[ep.range(mid,rad) for ep in gre];GT=[ep.range(mid,rad) for ep in gte]
            add(['outer',i],d.tp+l,d.tp+r,P,Q,GR,GT)
    out={'date':now(),'status':'COMPUTED_PENDING_AUDIT','input_sha256':d.sha,'cache_sha256':hashlib.sha256(CACHE.read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),
         'precision_bits':ctx.prec,'angular_cells':args.angular,'radial_subdivisions':args.radial,'outer_cells':args.outer_cells,
         'part':args.part,'start':args.start,'stop':args.stop,'cell_count':len(records),'ma_lower':rec(global_ma),'mr_lower':rec(global_mr),
         'd_lower':rec(global_d),'kappa_lower':rec(global_kap),'gradient_upper':rec(global_gr),'records':records,'seconds':time.monotonic()-start}
    jwrite(TOP/'evidence'/f'{args.tag}.json',out);emit(stage='finished',cells=len(records),ma=global_ma.str(20),mr=global_mr.str(20),d=global_d.str(20),seconds=out['seconds'])

def ends():
    d=M.Data();check_hash(d);cache=load_cache(d);H=density_eps(d,'inner');fac=(2*aa(d.tm)).exp();j0=list(map(arb,cache['J_inner']))
    hb=[h.expmul(2).scale(fac).sup_left() for h in H]
    ib=[H[n-1].particular(2*n+4).expmul(2).scale(fac).sup_left() for n in range(1,262)]
    ps=[];qs=[]
    # n=1: remove the exact common strain before bounding the particular part.
    jpart=H[1].particular(2).scale(-1);jb=jpart.expmul(2).scale(fac).sup_left()
    central=fac*(j0[0]-jpart.atzero());c=3/aa(d.k)-1
    assert central.overlaps(c)
    ps.append(jb+ib[0]);qs.append(jb+ib[0]+(hb[0]+hb[1])/2)
    for n in range(2,262):
        b=2*n-4;bound=arb(j0[n-1].abs_upper())
        for e,p in H[n].terms.items():
            assert e>=0
            for j,v in enumerate(p):
                first=aa(factorial(j))/aa(e+2)**(j+1)
                second=aa(factorial(j))/aa(e+2)**j/(b+2)
                bound+=arb(v.abs_upper())*min(first,second)
        jb=fac*bound
        ps.append(n*(jb+ib[n-1]));qs.append(n*(jb+ib[n-1])+(hb[n]+hb[n-1])/2)
    gr=sum(((h.scale(3)+h.deriv()).expmul(2).scale(fac).sup_left()+(2*j+1)*hb[j] for j,h in enumerate(H)),arb(0))
    ep=sum(ps,arb(0));et=sum((2*n*qs[n-1] for n in range(1,262)),arb(0));ell=1/aa(d.k);A=2*ell-1;D=4*ell-1
    inner={'d_lower':rec(D-ep),'ma_lower':rec(1+ell+aa(F(17,4))*A-aa(F(17,4))*(ep+et)-gr),
           'mr_lower':rec(1+ell-A/8-ep/8-gr),'P_error_upper':rec(ep),'T_error_upper':rec(et),'gradient_upper':rec(gr),'central_check':rec(central)}
    pe,qe,gre,gte=outer_eps(d,cache);ep=sum((p.sup_right(8) for p in pe),arb(0));et=sum((2*n*qe[n-1].sup_right(8) for n in range(1,262)),arb(0));gr=sum((x.sup_right(8) for x in gre+gte),arb(0))
    outer={'d_lower':rec(ell-ep),'ma_lower':rec(1+ell-5*ell/8-5*ep/8-aa(F(17,4))*et-gr),
           'mr_lower':rec(1+ell-5*ell/8-5*ep/8-gr),'P_error_upper':rec(ep),'T_error_upper':rec(et),'gradient_upper':rec(gr)}
    out={'date':now(),'status':'COMPUTED_PENDING_AUDIT','bits':ctx.prec,'input_sha256':d.sha,'cache_sha256':hashlib.sha256(CACHE.read_bytes()).hexdigest(),
         'inner_through_exact':str(d.tm),'outer_from_exact':str(d.tp+8),'inner':inner,'outer':outer,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest()}
    jwrite(TOP/'evidence/ends.json',out);print(json.dumps(out,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('task',choices=['prepare','finite','ends']);ap.add_argument('--bits',type=int,default=512);ap.add_argument('--angular',type=int,default=128);ap.add_argument('--radial',type=int,default=2);ap.add_argument('--outer-cells',type=int,default=160);ap.add_argument('--part',choices=['all','middle','outer'],default='all');ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=1558);ap.add_argument('--tag',default='finite');args=ap.parse_args();ctx.prec=args.bits;ctx.threads=1
    if args.task=='prepare':prepare()
    elif args.task=='ends':ends()
    else:finite(args)
