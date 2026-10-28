"""Own original-input source-neighborhood Hessian certificate."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import sys,importlib.util,json,hashlib,argparse,time
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
spec=importlib.util.spec_from_file_location('source_data',LANE/'proofs/15_modal_source/code/certify.py')
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
aa=M.aa;record=M.record;now=M.now;emit=M.emit
A=F(4841405518533377,562949953421312);B=F(4841405518533711,562949953421312);DELTA=F(33,2000)

def bounds():
    lo=aa(A-3*DELTA).log();hi=(aa(B+3*DELTA)**2+aa(3*DELTA)**2).log()/2
    th=(aa(3*DELTA)/aa(A-3*DELTA)).atan()
    return lo,hi,th

def interval(a,b):return a.union(b)
def horner(p,x):
    out=arb(0)
    for v in p[::-1]:out=out*x+v
    return out

def prepare():
    d=M.Data();lo,hi,th=bounds()
    spans=[i for i in d.spans if aa(d.knots[i+1])>=lo and aa(d.knots[i])<=hi]
    IL=d.propagate('I',spans[0]);JR=d.propagate('J',spans[-1]); cache={}
    for i in spans:
        mat=d.poly(i);rows=mat.tolist();cache[i]={'rows':rows,'IL':IL[:]}
        h=d.knots[i+1]-d.knots[i];rev=(d.reverse*mat).tolist()
        for n in range(1,262):
            ez,ph=d.moments(h,-2*n-4)
            IL[n-1]=ez*IL[n-1]+aa(h)*sum((rev[j][n-1]*ph[j] for j in range(8)),arb(0))
    for i in spans[::-1]:
        rows=cache[i]['rows'];cache[i]['JR']=JR[:];h=d.knots[i+1]-d.knots[i]
        for n in range(1,262):
            ez,ph=d.moments(h,4-2*n)
            JR[n-1]=ez*JR[n-1]+aa(h)*sum((rows[j][n]*ph[j] for j in range(8)),arb(0))
    out={'date':now(),'bits':ctx.prec,'original_sha256':d.sha,'scalar_sha256':hashlib.sha256(M.SCALAR.read_bytes()).hexdigest(),
         'knots':{str(i):[str(d.knots[i]),str(d.knots[i+1])] for i in spans},'spans':{str(i):{'rows':[[v.str(190) for v in row] for row in c['rows']],'IL':[v.str(190) for v in c['IL']],'JR':[v.str(190) for v in c['JR']]} for i,c in cache.items()}}
    f=TOP/'evidence/boundary_cache.json';f.write_text(json.dumps(out,indent=2)+'\n');emit(stage='boundary_cache_saved',spans=spans)

def differentiate_map(q,m,axes):
    terms={('s',m):[F(1)]}
    for ax in axes:
        nxt={}
        for (kind,k),co in terms.items():
            for sign in (1,-1):
                freq=k+sign
                # D+q-m for +; D+q+m for -.
                c=q-sign*k; p=[F(0)]*(len(co)+1)
                for j,v in enumerate(co):p[j]+=c*v/2;p[j+1]+=v/2
                nk=kind;sg=1
                if ax=='y':
                    nk='c' if kind=='s' else 's'
                    sg=(-sign if kind=='s' else sign)
                if sg==-1:p=[-v for v in p]
                old=nxt.setdefault((nk,freq),[F(0)]*len(p))
                for j,v in enumerate(p):old[j]+=v
        terms=nxt;q-=1
    result={}
    for (kind,k),p in terms.items():
        if k==0 and kind=='s':continue
        sg=-1 if k<0 and kind=='s' else 1;k=abs(k)
        out=result.setdefault((kind,k),[F(0)]*len(p))
        for j,v in enumerate(p):out[j]+=sg*v
    return {key:p for key,p in result.items() if any(p)}

MAPS={}
for label,axes,q,count in [('rxx','xx',3,262),('rxy','xy',3,262),('ryy','yy',3,262),('pxxx','xxx',4,261),('pxxy','xxy',4,261),('pxyy','xyy',4,261),('pyyy','yyy',4,261)]:
    MAPS[label]=[differentiate_map(q,2*n+1 if q==3 else 2*n+2,axes) for n in range(count)]

N=20

def local_series(rows,IL,JR,t0,t1,mid,radius):
    width=aa(t1-t0);ell=mid-aa(t0);rr=aa(t1)-mid
    assert ell>0 and rr>0
    H=M.shift_rows(rows,ell/width,width) # physical Taylor coefficients H^(j)/j!
    Sf=[];rems=[]
    for n in range(1,262):
        a=2*n+4;b=2*n-4
        pi=M.phi_series(-a*ell);pj=M.phi_series(-b*rr)
        iv=(-a*ell).exp()*IL[n-1]+sum(((-1)**j*H[j][n-1]*ell**(j+1)*pi[j] for j in range(8)),arb(0))
        jv=(-b*rr).exp()*JR[n-1]+sum((H[j][n]*rr**(j+1)*pj[j] for j in range(8)),arb(0))
        ic=[iv];jc=[jv]
        for j in range(1,N+1):
            hi=H[j-1][n-1] if j<=8 else arb(0);hj=H[j-1][n] if j<=8 else arb(0)
            ic.append((hi-a*ic[-1])/j);jc.append((b*jc[-1]-hj)/j)
        Sf.append([(v-u)/2 for u,v in zip(ic,jc)])
        # Exact particular polynomial and exponential homogeneous amplitudes.
        ip=arb(0);jp=arb(0)
        for j in range(7,-1,-1):
            ip=(H[j][n-1]-(j+1)*ip)/a
            if b:jp=(H[j][n]+(j+1)*jp)/b
        ib=abs(iv-ip).upper();jb=abs(jv-jp).upper() if b else arb(0)
        errors=[]
        for j in range(4):
            ei=ib*a**j*(aa(a)*radius).exp()*(aa(a)*radius)**(N-j+1)/factorial(N-j+1)
            ej=jb*abs(b)**j*(aa(abs(b))*radius).exp()*(aa(abs(b))*radius)**(N-j+1)/factorial(N-j+1) if b else arb(0)
            errors.append(((ei+ej)/2).upper())
        rems.append(errors)
    return H,Sf,rems

def component_coeffs(label,H,Sf,rems):
    density=label.startswith('r');nmax=262 if density else 261;degree=7 if density else N
    out={};err={}
    for n in range(nmax):
        f=[H[j][n] for j in range(8)] if density else Sf[n]
        for key,p in MAPS[label][n].items():
            poly=out.setdefault(key,[arb(0) for j in range(degree+1)])
            for j,c in enumerate(p):
                if not c:continue
                for l in range(j,degree+1):poly[l-j]+=aa(c*F(factorial(l),factorial(l-j)))*f[l]
                if not density:err[key]=err.get(key,arb(0))+aa(abs(c))*rems[n][j]
    return out,err

def evaluate(args):
    f=TOP/'evidence/boundary_cache.json';cache=json.loads(f.read_text());assert cache['bits']>=ctx.prec
    lo,hi,th=bounds();records=[];maxv=arb(0);maxr=arb(0);start=time.monotonic()
    for ispan,raw in cache['spans'].items():
        t0,t1=[F(x) for x in cache['knots'][ispan]]
        left=max(lo,aa(t0));right=min(hi,aa(t1));assert left<right
        rows=[[arb(v) for v in row] for row in raw['rows']];IL=[arb(v) for v in raw['IL']];JR=[arb(v) for v in raw['JR']]
        for j in range(args.radial):
            l=left+(right-left)*j/args.radial;r=left+(right-left)*(j+1)/args.radial
            mid=(l+r)/2;rad=((r-l)/2).upper();v=arb(0,rad);ef=interval(l,r).exp()
            H,Sf,rems=local_series(rows,IL,JR,t0,t1,mid,rad)
            coeff={}
            for label in MAPS:
                pol,err=component_coeffs(label,H,Sf,rems)
                coeff[label]={key:horner(p,v)+arb(0,err.get(key,arb(0)).upper()) for key,p in pol.items()}
            localv=arb(0);localr=arb(0)
            for k in range(args.angular):
                angle=interval(th*k/args.angular,th*(k+1)/args.angular)
                trig={key:((key[1]*angle).sin() if key[0]=='s' else (key[1]*angle).cos()) for key in set().union(*(set(c) for c in coeff.values()))}
                vals={label:ef*sum((value*trig[key] for key,value in co.items()),arb(0)) for label,co in coeff.items()}
                rv=(vals['pxxx']**2+3*vals['pxxy']**2+3*vals['pxyy']**2+vals['pyyy']**2).upper().sqrt().upper()
                rr=(vals['rxx']**2+2*vals['rxy']**2+vals['ryy']**2).upper().sqrt().upper()
                localv=max(localv,rv);localr=max(localr,rr)
                records.append({'span':int(ispan),'radial_cell':j,'angular_cell':k,'t_interval':record(interval(l,r)),'theta_interval':record(angle),'derivatives':{key:record(val) for key,val in vals.items()},'MV_upper':record(rv),'Mrho_upper':record(rr)})
            maxv=max(maxv,localv);maxr=max(maxr,localr)
            emit(stage='radial_cell',span=ispan,index=j,MV=localv.str(15),Mrho=localr.str(15),seconds=time.monotonic()-start)
    s=F(31,10);cut=F(64,49);ec=3*s+F(9,2)*(s+F(1,2))*cut
    E=aa(DELTA)*(aa(ec)*maxv+3*maxr)
    out={'date':now(),'status':'COMPUTED_PENDING_AUDIT','bits':ctx.prec,'delta':str(DELTA),'cutoff_gradient':str(cut),'E_coefficient':str(ec),'cache_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'radial_subdivisions_per_span':args.radial,'angular_subdivisions':args.angular,'Taylor_degree':N,'MV_upper':record(maxv),'Mrho_upper':record(maxr),'E_upper':record(E),'frozen_margin':str(F(1687,500)),'strict_margin':bool(E<aa(F(1687,500))),'cells':records,'seconds':time.monotonic()-start}
    (TOP/'evidence'/f'{args.tag}_result.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='finished',MV=maxv.str(25),Mrho=maxr.str(25),E=E.str(25),strict_margin=out['strict_margin'])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('task',choices=['prepare','evaluate']);p.add_argument('--bits',type=int,default=512);p.add_argument('--radial',type=int,default=8);p.add_argument('--angular',type=int,default=8);p.add_argument('--tag',default='coarse');args=p.parse_args();ctx.prec=args.bits;ctx.threads=1
    if args.task=='prepare':prepare()
    else:evaluate(args)
