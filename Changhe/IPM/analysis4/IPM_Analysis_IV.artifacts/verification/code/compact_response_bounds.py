"""Certified compact-carrier response bounds, with exact integer coverage."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,time,sys,argparse
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,ctx
from pure_cartesian_ball import Tuning,Field,sine,advection,ball,refine_root

def add(*fields):
    out={}
    for f in fields:
        for m,v in f.items():out[m]=out.get(m,arb(0))+v
    return out

def mul(f,g):
    out={}
    for m,a in f.items():
        for n,b in g.items():out[m+n]=out.get(m+n,arb(0))+a*b
    return out

def scale(f,a):return {m:a*v for m,v in f.items()}

def low(f):return {f.lo+j:v for j,v in enumerate(f.poly.coeffs()) if not v.is_zero()}

def high_derivatives(f,alpha,t):
    x={};y={}
    for v,a in f.items():
        minus=t*ball((v-alpha)/2)*a;plus=(1+t*ball((v+alpha)/2))*a
        x[v-1]=x.get(v-1,arb(0))+minus;y[v-1]=y.get(v-1,arb(0))+minus
        x[v+1]=x.get(v+1,arb(0))-plus;y[v+1]=y.get(v+1,arb(0))+plus
    return x,y

class Response:
    def __init__(self,h,Q,b,B=4):
        self.solver=Tuning(h,Q,B);self.h,self.Q,self.B=h,Q,B;self.delta=mpq(2*h,Q)
        self.f={1:sine(self.solver.p(1),1,arb(1))+sine(self.solver.p(1),3,b)}
        self.g={1:self.solver.poisson(self.f[1],1)}
        for n in range(2,Q+1):
            self.f[n]=self.solver.order(n,self.f,self.g)
            if n<Q:self.g[n]=self.solver.poisson(self.f[n],n)
        self.fxy={j:(low(f.derivative()),low(f.derivative(True))) for j,f in self.f.items()}
        self.gxy={j:(low(g.derivative()),low(g.derivative(True))) for j,g in self.g.items()}
    def full(self,k):
        n=k*self.Q;q=2*self.h*k-2
        e=sine(-q,q,arb(1));U={};V={}
        for r in range(1,self.Q+1):
            total=advection(e,self.f[r])
            for s in range(1,r):total=total+advection(V[s],self.f[r-s])+advection(self.g[r-s],U[s])
            U[r]=total.scale(ball((1-self.delta)/(self.delta*(n+r-1))))
            if r<self.Q:V[r]=self.solver.poisson(U[r],n+r)
        return U[self.Q].sine(2*self.h*(k+1)-3)
    def compact(self,t):
        U={};V={}
        for r in range(1,self.Q+1):
            # X_t e=-z/2, Y_t e=z/2.
            FX,FY=self.fxy[r]
            total={m+1:-v/2 for m,v in add(FX,FY).items()}
            for s in range(1,r):
                HX,HY=high_derivatives(V[s],self.delta*s,t);FX,FY=self.fxy[r-s]
                total=add(total,mul(HX,FY),scale(mul(HY,FX),-1))
                HX,HY=high_derivatives(U[s],1+self.delta*s,t);GX,GY=self.gxy[r-s]
                total=add(total,mul(GX,HY),scale(mul(GY,HX),-1))
            den=1+ball(2+self.delta*(r-1))*t
            if den.contains(0):return None
            U[r]=scale(total,ball(1-self.delta)/den)
            if r<self.Q:
                V[r]={}
                for v,a in U[r].items():
                    den1=2*(v+1-self.delta*r);assert den1
                    den2=2*(2+ball(v-1+self.delta*r)*t)
                    if den2.contains(0):return None
                    V[r][v+1]=V[r].get(v+1,arb(0))-a/ball(den1)
                    V[r][v-1]=V[r].get(v-1,arb(0))+t*a/den2
        return 2*U[self.Q].get(2*self.h-1,arb(0))

def ceil(q):return int(-((-q.numerator)//q.denominator))
def floor(q):return int(q.numerator//q.denominator)

def cover(response,K,s,out,max_nodes=100000):
    stack=[(mpq(0),mpq(1,2*response.h*K-2),0,'')];nodes=[];accepted=empty=split=0
    start=time.monotonic()
    while stack:
        a,b,depth,address=stack.pop()
        lower=max(K,ceil((1/b+2)/(2*response.h)));upper=None if not a else floor((1/a+2)/(2*response.h))
        if upper is not None and upper<lower:
            nodes.append(dict(address=address,a=str(a),b=str(b),status='empty',lower=lower,upper=upper));empty+=1;continue
        value=response.compact(ball(a).union(ball(b)))
        if value is not None and abs(value)>ball(s):
            nodes.append(dict(address=address,a=str(a),b=str(b),status='accepted',response=value.str(45,radius=True),lower=lower,upper=upper));accepted+=1
        else:
            if depth>=80:raise AssertionError(('coverage_depth',address,str(a),str(b),str(value),str(s)))
            mid=(a+b)/2;stack.append((mid,b,depth+1,address+'1'));stack.append((a,mid,depth+1,address+'0'));split+=1
        if (accepted+empty+split)%250==0:
            print(json.dumps(dict(stage='coverage',accepted=accepted,empty=empty,split=split,pending=len(stack),elapsed_s=time.monotonic()-start)),flush=True)
            out.with_suffix('.partial.json').write_text(json.dumps(dict(nodes=nodes,stack=[dict(a=str(a),b=str(b),depth=d,address=q) for a,b,d,q in stack],accepted=accepted,empty=empty,split=split),indent=2)+'\n')
        if accepted+empty+split>=max_nodes:raise AssertionError(('coverage_node_limit',max_nodes))
    result=dict(starting_index=K,lower_bound=str(s),accepted=accepted,empty=empty,split=split,nodes=nodes,actual_elapsed_s=time.monotonic()-start)
    out.write_text(json.dumps(result,indent=2)+'\n');return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='1,2,3,4,5');ap.add_argument('--bits',type=int,default=512);ap.add_argument('--probe-only',action='store_true');args=ap.parse_args()
    ctx.prec=args.bits;start=time.monotonic();root=Path('research/149_compact_response_certificates');src=Path('research/146_four_ninths_profiles/verification/algebraic_certificates.json');data=json.loads(src.read_text())
    P=list(map(int,data['primitive_coefficients']));rows=[]
    for index in map(int,args.roots.split(',')):
        b,I=refine_root(P,data['real_roots'][index-1]['interval'],args.bits+32);r=Response(2,9,b);finite=[]
        for k in range(1,17):
            v=r.full(k);assert not v.contains(0)
            if k>=10:
                w=r.compact(ball(mpq(1,4*k-2)));assert w.overlaps(v),('carrier_mismatch',k,str(v),str(w))
            finite.append(v)
        limit=r.compact(arb(0));assert not limit.contains(0)
        # Deliberately conservative dyadic target, shared finite and tail checks.
        least=min([float(abs(v).lower()) for v in finite]+[float(abs(limit).lower())]);s=mpq(1)
        while float(s)>=least/4:s/=2
        assert all(abs(v)>ball(s) for v in finite)
        print(json.dumps(dict(root=index,stage='finite',s=str(s),sigma_limit=limit.str(30,radius=True),min_sample=least,elapsed_s=time.monotonic()-start)),flush=True)
        if args.probe_only:
            for power in [8,12,16,20,24,28,32,40]:
                v=r.compact(arb(0).union(ball(mpq(1,2**power))))
                print(json.dumps(dict(root=index,power=power,enclosure=str(v),separated=v is not None and not v.contains(0))),flush=True)
            continue
        coverage=cover(r,10,s,root/'verification'/('root'+str(index)+'_coverage.json'))
        row=dict(root_index=index,root_interval=I,root_ball=b.str(60,radius=True),s=str(s),finite=[dict(k=k+1,sigma=v.str(60,radius=True)) for k,v in enumerate(finite)],sigma_infinity=limit.str(60,radius=True),full_compact_comparisons=7,all_overlap=True,counts=r.solver.counts,coverage={k:v for k,v in coverage.items() if k!='nodes'})
        rows.append(row);(root/'verification'/('root'+str(index)+'_checks.json')).write_text(json.dumps(row,indent=2)+'\n')
        print(json.dumps(dict(root=index,all_checks_pass=True,coverage=row['coverage'],elapsed_s=time.monotonic()-start)),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=args.bits,source_sha256=sha256(src.read_bytes()).hexdigest(),rows=rows,actual_elapsed_s=time.monotonic()-start,probe_only=args.probe_only)
    (root/'verification'/('probe_checks.json' if args.probe_only else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n')
    for name in ['compact_response_bounds.py','pure_cartesian_ball.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:main()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/149_compact_response_certificates/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
