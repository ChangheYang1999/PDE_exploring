"""Outward lower certificate for the axis polygon clamp.
Soundness: 11_lattice_pole_constraints/axis_clamped_layercake/PROOF.md.
Only nonnegative components are omitted; no numerical quadrature error model.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
ctx.prec=256
A=arb(1)/2;PI=arb.pi();RT2=arb(2).sqrt();RT3=arb(3).sqrt()
SKIP={'triangle':0,'positive_first':0,'negative_first':0,'arc':0,'uncertain_triangle':0,'uncertain_positive_first':0,'uncertain_negative_first':0,'uncertain_arc':0}

def aa(q):
    q=Q(q);return arb(q.numerator)/q.denominator

def primitive(x,y,m,zero_y=False):
    if zero_y:
        assert x<A and x>0
        lg=acb(((A-x)/(A+x)).log(),PI)
    else:
        z=acb(x,y);lg=(-2*A/(z+A)).log1p()
    out=-(lg/acb(1,m)).imag/(2*PI)
    assert out.is_finite()
    return out

def line(m,d,lo,hi=None,hi_zero=False):
    low=primitive(lo,m*lo+d,m)
    high=arb(0) if hi is None else primitive(hi,arb(0) if hi_zero else m*hi+d,m,zero_y=hi_zero)
    return high-low

def arc_primitive(v,b,s):
    v=v.intersection((-1/RT2).union(-arb(1)/2))
    w=acb(s*v,s*(1-v*v).sqrt());c=acb(A+b,b);z=c+w
    az=(-2*A/(z+A)).log1p()/(2*A)
    bc=-1/((c*c-A*A)*w)-2*c/(c*c-A*A)**2*w.log()+(z-A).log()/(2*A*(A-c)**2)-(z+A).log()/(2*A*(A+c)**2)
    out=-A/(2*PI)*(az-s*s*bc).imag
    assert out.is_finite()
    return out

def include_test(lo,hi,name):
    if lo<hi:return True
    SKIP[name]+=1
    if not lo>=hi:SKIP['uncertain_'+name]+=1
    return False

def positive_mass(u,s,b):
    ans=arb(0);lo=arb.max(u,s);hi=A-RT2*s
    if include_test(lo,hi,'triangle'):
        ans+=line(arb(-1),hi,lo,hi,hi_zero=True)
    d1=-A-RT2*s;d2=((RT3-1)*b-A-2*s)/RT3
    cross=(d2-d1)/(1-1/RT3)
    lo=arb.max(u,arb.max(A+RT2*s,A-(RT3-1)*b+2*s))
    if include_test(lo,cross,'positive_first'):
        ans+=line(arb(1),d1,lo,cross)
    ans+=line(1/RT3,d2,arb.max(lo,cross))
    assert ans.is_finite()
    return arb.max(arb(0),2*ans)

def negative_mass_magnitude(u,s,b):
    # The exact arguments satisfy u >= A+s. Dependency may prevent Arb proving it.
    left=A+b-s/RT2;right=A+b-s/2;ans=arb(0)
    if include_test(u,left,'negative_first'):
        ans+=line(arb(1),-A+RT2*s,u,left)
    low=arb.max(u,left)
    if include_test(low,right,'arc'):
        v=(low-A-b)/s
        ans+=arc_primitive(-arb(1)/2,b,s)-arc_primitive(v,b,s)
    ans+=line(1/RT3,((RT3-1)*b-A+2*s)/RT3,arb.max(u,right))
    assert ans.is_finite()
    return arb.max(arb(0),2*ans)

def safe_lower(value,places=10):
    k=int((arb(value.lower())*10**places).floor().unique_fmpz())
    sign='-' if k<0 else '';k=abs(k)
    return f'{sign}{k//10**places}.{k%10**places:0{places}d}'

def main():
    p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True)
    p.add_argument('--part',choices=['plus','mid','minus'],required=True);p.add_argument('--cells',type=int,default=4096)
    p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int)
    p.add_argument('--left');p.add_argument('--right');p.add_argument('--out',required=True)
    args=p.parse_args();alpha=aa(args.alpha);b=aa(args.b);assert 0<alpha<1 and b>0
    stop=args.cells if args.stop is None else args.stop;assert 0<=args.start<stop<=args.cells
    left=Q(args.left or ('1/10000000' if args.part=='mid' else '-20'))
    right=Q(args.right or ('24' if args.part=='mid' else '30'));assert left<right
    c=2**(alpha-1);power=1/alpha;step=(right-left)/args.cells;total=arb(0);started=time.monotonic()
    def U(t):return (t/c)**power
    for i in range(args.start,stop):
        x=aa(left+i*step).union(aa(left+(i+1)*step))
        if args.part=='mid':
            ee=(-x).exp();t=-(-x).expm1()/2
            val=positive_mass(U(t),U(arb(1)/2-t),b)*ee/2
        else:
            t=x.exp()
            if args.part=='plus': val=positive_mass(U(t),U(t+arb(1)/2),b)*t
            else:val=negative_mass_magnitude(U(t+arb(1)/2),U(t),b)*t
        assert val.is_finite() and val>=0,(i,val)
        total+=val*aa(step)
        if i%256==0:print(i,stop,round(time.monotonic()-started,3),flush=True)
    paths=[Path(__file__),ROOT/'11_lattice_pole_constraints/axis_clamped_layercake/PROOF.md',ROOT/'11_lattice_pole_constraints/half_plane/PROOF.md',ROOT/'11_lattice_pole_constraints/axis_reduction/PROOF.md']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(Q(args.alpha)),b=str(Q(args.b)),part=args.part,cells=args.cells,start=args.start,stop=stop,left=str(left),right=str(right),precision_bits=ctx.prec,included_integral_enclosure=total.str(55,more=True),safe_integral_lower_10_places=safe_lower(total),skipped_components=SKIP,elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Rigorous partial lower bound, conditional on the soundness proof and complete coverage merge. The upper endpoint is not an upper bound for the complete witness integral.')
    target=ROOT/args.out;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['part','included_integral_enclosure','safe_integral_lower_10_places','elapsed_seconds']},indent=2))
if __name__=='__main__':main()
