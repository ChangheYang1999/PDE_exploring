"""Candidate-shaped all-index response test with dense compact Laurent algebra."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,sys,time,argparse
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb,arb_poly,ctx
from pure_cartesian_ball import Tuning,sine,ball,refine_root
from compact_response_bounds import Response,low,ceil,floor

class Laurent:
    def __init__(self,lo=0,poly=None):
        self.lo=lo;self.poly=arb_poly([] if poly is None else poly)
    def __add__(self,o):
        lo=min(self.lo,o.lo)
        def align(p,m):return arb_poly([arb(0)]*(m-lo)+p.coeffs())
        return Laurent(lo,align(self.poly,self.lo)+align(o.poly,o.lo))
    def scale(self,a):return Laurent(self.lo,self.poly*a)
    def __sub__(self,o):return self+o.scale(-1)
    def __mul__(self,o):return Laurent(self.lo+o.lo,self.poly*o.poly)
    def coefficient(self,m):return self.poly[m-self.lo] if m>=self.lo else arb(0)
    def shift(self,d):return Laurent(self.lo+d,self.poly)
    def derivatives(self,alpha,t):
        N=len(self.poly);x=[arb(0)]*(N+2);y=[arb(0)]*(N+2)
        for j,a in enumerate(self.poly.coeffs()):
            v=self.lo+j
            minus=t*ball((v-alpha)/2)*a
            plus=(1+t*ball((v+alpha)/2))*a
            x[j]+=minus;y[j]+=minus;x[j+2]-=plus;y[j+2]+=plus
        return Laurent(self.lo-1,x),Laurent(self.lo-1,y)

def pack(v):
    m,e=v.mid().man_exp();r,re=v.rad().man_exp()
    return [str(m),int(e),str(r),int(re)]
def unpack(v):
    m,e,r,re=v
    return Fraction(int(m))*Fraction(2)**e,Fraction(int(r))*Fraction(2)**re

class CandidateResponse(Response):
    def __init__(self,b,fixed):
        self.h,self.Q,self.B=2,9,20;self.solver=Tuning(self.h,self.Q,self.B);self.delta=mpq(4,9)
        first=sine(self.solver.p(1),3,b)
        for m,a in fixed.items():first=first+sine(self.solver.p(1),int(m),ball(mpq(a)))
        self.f={1:first};self.g={1:self.solver.poisson(first,1)}
        for n in range(2,10):
            self.f[n]=self.solver.order(n,self.f,self.g)
            if n<9:self.g[n]=self.solver.poisson(self.f[n],n)
        assert self.f[9].sine(1).contains(0)
        self.fxy={j:(low(f.derivative()),low(f.derivative(True))) for j,f in self.f.items()}
        self.gxy={j:(low(g.derivative()),low(g.derivative(True))) for j,g in self.g.items()}
        def xy(v):
            a,b=v.derivative(),v.derivative(True)
            return Laurent(a.lo,a.poly),Laurent(b.lo,b.poly)
        self.fxyd={j:xy(f) for j,f in self.f.items()}
        self.gxyd={j:xy(g) for j,g in self.g.items()}
    def dense(self,t):
        U,V={},{}
        for r in range(1,10):
            FX,FY=self.fxyd[r];total=(FX+FY).shift(1).scale(-arb(1)/2)
            for s in range(1,r):
                HX,HY=V[s].derivatives(self.delta*s,t);FX,FY=self.fxyd[r-s]
                total=total+HX*FY-HY*FX
                HX,HY=U[s].derivatives(1+self.delta*s,t);GX,GY=self.gxyd[r-s]
                total=total+GX*HY-GY*HX
            den=1+ball(2+self.delta*(r-1))*t
            if den.contains(0):return None
            U[r]=total.scale(ball(1-self.delta)/den)
            if r<9:
                lo=U[r].lo;data=[arb(0)]*(len(U[r].poly)+2)
                for j,a in enumerate(U[r].poly.coeffs()):
                    if a.is_zero():continue
                    v=lo+j;den1=2*(v+1-self.delta*r);assert den1
                    den2=2*(2+ball(v-1+self.delta*r)*t)
                    if den2.contains(0):return None
                    data[j+2]-=a/ball(den1);data[j]+=t*a/den2
                V[r]=Laurent(lo-1,data)
        return 2*U[9].coefficient(3)

def cover(response,s,out):
    K=46;top=mpq(1,182)
    stack=[(mpq(0),top,0,'')];nodes=[];splits=accepted=empty=0;start=time.monotonic()
    while stack:
        a,b,depth,address=stack.pop()
        lower=max(K,ceil((1/b+2)/4));upper=None if not a else floor((1/a+2)/4)
        if upper is not None and upper<lower:
            nodes.append(dict(address=address,a=str(a),b=str(b),status='empty',lower=lower,upper=upper));empty+=1
        else:
            value=response.dense(ball(a).union(ball(b)))
            if value is not None and abs(value)>ball(s):
                packed=pack(value);m,r=unpack(packed);assert abs(m)-r>Fraction(str(s))
                nodes.append(dict(address=address,a=str(a),b=str(b),status='accepted',response_exact_dyadic=packed,lower=lower,upper=upper));accepted+=1
            else:
                if depth>=90:raise AssertionError(('coverage_depth',address,str(a),str(b),str(value)))
                mid=(a+b)/2;stack.append((mid,b,depth+1,address+'1'));stack.append((a,mid,depth+1,address+'0'));splits+=1
        if (splits+accepted+empty)%250==0:
            progress=dict(accepted=accepted,empty=empty,split=splits,pending=len(stack),elapsed_s=time.monotonic()-start)
            print(json.dumps(dict(stage='coverage',**progress)),flush=True)
            out.with_suffix('.partial.json').write_text(json.dumps(dict(nodes=nodes,stack=[dict(a=str(a),b=str(b),depth=d,address=q) for a,b,d,q in stack],**progress),indent=2)+'\n')
        if len(nodes)>40000:raise AssertionError('coverage leaf limit')
    # Replay the partition and every exclusion independently with Fraction arithmetic.
    previous=Fraction(0);target=Fraction(1,182)
    for node in sorted(nodes,key=lambda v:Fraction(v['a'])):
        a,b=Fraction(0),target
        for digit in node['address']:
            mid=(a+b)/2
            if digit=='0':b=mid
            else:a=mid
        assert a==Fraction(node['a'])==previous and b==Fraction(node['b'])
        previous=b
        if node['status']=='accepted':
            m,r=unpack(node['response_exact_dyadic']);assert abs(m)-r>Fraction(str(s))
        else:
            lowq=(1/b+2)/4;lower=max(K,-((-lowq.numerator)//lowq.denominator))
            assert a
            upq=(1/a+2)/4;upper=upq.numerator//upq.denominator
            assert upper<lower
    assert previous==target
    result=dict(starting_index=K,lower_bound=str(s),nodes=nodes,accepted=accepted,empty=empty,split=splits,exact_replay_pass=True,actual_elapsed_s=time.monotonic()-start)
    out.write_text(json.dumps(result,indent=2)+'\n');return result

def run():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=int,default=3);ap.add_argument('--cover',action='store_true');args=ap.parse_args()
    ctx.prec=768;start=time.monotonic();root=Path('research/158_candidate_shaped_response');out=root/'verification'
    source=Path('research/156_candidate_shaped_compatibility/verification/polynomial.json');roots=Path('research/156_candidate_shaped_compatibility/verification/checks.json')
    d=json.loads(source.read_text());rd=json.loads(roots.read_text());rr=rd['roots'][args.root-1]
    b,I=refine_root(d['primitive_coefficients_ascending'],rr['interval'],832)
    response=CandidateResponse(b,d['fixed_normalized_coefficients']);finite=[]
    for k in range(1,53):
        v=response.full(k);assert not v.contains(0),('finite_zero',k,str(v))
        if k>=46:
            w=response.dense(ball(mpq(1,4*k-2)));assert w is not None and w.overlaps(v),('full_dense',k,str(v),str(w))
        finite.append(dict(k=k,sigma=v.str(65,radius=True),exact_dyadic=pack(v)))
        if k%10==0:print(json.dumps(dict(stage='finite',root=args.root,k=k,elapsed_s=time.monotonic()-start)),flush=True)
    limit=response.dense(arb(0));assert not limit.contains(0)
    for t in [mpq(0),mpq(1,182),mpq(1,256)]:
        a=response.dense(ball(t));v=response.compact(ball(t));assert a is not None and v is not None and a.overlaps(v)
    allvals=[unpack(row['exact_dyadic']) for row in finite]+[unpack(pack(limit))]
    least=min(abs(m)-r for m,r in allvals);assert least>0
    s=Fraction(1)
    while s>=least/4:s/=2
    norm=1+abs(b)+sum((abs(ball(mpq(v))) for m,v in d['fixed_normalized_coefficients'].items() if int(m)!=1),arb(0))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),root_index=args.root,source_sha256=sha256(source.read_bytes()).hexdigest(),root_source_sha256=sha256(roots.read_bytes()).hexdigest(),arithmetic_bits=768,root_interval=I,root_ball=b.str(65,radius=True),leading_norm=norm.str(65,radius=True),finite=finite,starting_tail_index=46,full_dense_overlap_indices=list(range(46,53)),sparse_dense_overlap_count=3,sigma_infinity=limit.str(65,radius=True),sigma_infinity_exact_dyadic=pack(limit),lower_bound=str(s),counts=response.solver.counts,all_finite_checks_pass=True,actual_elapsed_s=time.monotonic()-start)
    dest=out/f'root{args.root}_checks.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['root_index','leading_norm','sigma_infinity','lower_bound','actual_elapsed_s']}),flush=True)
    if args.cover:
        c=cover(response,mpq(str(s)),out/f'root{args.root}_coverage.json')
        result['coverage']={k:v for k,v in c.items() if k!='nodes'};result['all_index_lower_bound_proved']=True
        result['actual_elapsed_s']=time.monotonic()-start
        dest.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(root_index=args.root,all_index_lower_bound_proved=True,coverage=result['coverage'],actual_elapsed_s=time.monotonic()-start)),flush=True)
    for name in ['candidate_shaped_response.py','pure_cartesian_ball.py','compact_response_bounds.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
    (out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/158_candidate_shaped_response/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
