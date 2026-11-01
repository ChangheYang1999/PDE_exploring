"""Second parameter jet checked by an independent Cartesian Taylor recurrence."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, sys, time
sys.dont_write_bytecode = True
from gmpy2 import mpq
from flint import arb, arb_poly, ctx
import sympy as sp
from pure_cartesian_ball import Tuning, Field, ball, refine_root
from parameter_regularization_slope import order6_bderivative

class JetField:
    def __init__(self, a, da, lo=0, jets=None, order=2):
        self.a, self.da, self.lo = mpq(a), mpq(da), int(lo)
        self.jets = [arb_poly([]) for _ in range(order+1)] if jets is None else [arb_poly(v) for v in jets]
        self.order = len(self.jets)-1
    def coefficient(self, m, d=0):
        return self.jets[d][m-self.lo] if m >= self.lo else arb(0)
    def sine(self, m, d=0):
        return 2*self.coefficient(m,d)
    def value(self):
        return Field(self.a,self.lo,self.jets[0])
    def truncate(self,d):
        assert 0 <= d <= self.order
        return JetField(self.a,self.da,self.lo,self.jets[:d+1])
    def __add__(self,o):
        assert (self.a,self.da)==(o.a,o.da)
        lo=min(self.lo,o.lo)
        def align(v,offset):
            return arb_poly([arb(0)]*(offset-lo)+v.coeffs())
        return JetField(self.a,self.da,lo,[align(self.jets[d],self.lo)+align(o.jets[d],o.lo) for d in range(min(self.order,o.order)+1)])
    def scale(self,c):
        if not isinstance(c,list):
            return JetField(self.a,self.da,self.lo,[v*c for v in self.jets])
        order=min(self.order,len(c)-1)
        return JetField(self.a,self.da,self.lo,[sum((self.jets[j]*c[d-j] for j in range(d+1)),arb_poly([])) for d in range(order+1)])
    def __sub__(self,o):
        return self+o.scale(-1)
    def __mul__(self,o):
        order=min(self.order,o.order)
        return JetField(self.a+o.a,self.da+o.da,self.lo+o.lo,[sum((self.jets[j]*o.jets[d-j] for j in range(d+1)),arb_poly([])) for d in range(order+1)])
    def derivative(self,y=False):
        length=max(map(len,self.jets),default=0)
        result=[]
        for d in range(self.order+1):
            out=[arb(0)]*(length+2)
            for j in range(length):
                m=self.lo+j
                current=self.jets[d][j]
                prev=self.jets[d-1][j] if d else arb(0)
                out[j]+=current*ball((self.a+m)/2)+prev*ball(self.da/2)
                out[j+2]+=(current*ball((self.a-m)/2)+prev*ball(self.da/2))*(-1 if y else 1)
            result.append(out)
        return JetField(self.a-1,self.da,self.lo-1,result)

def quotient(a,b,order):
    out=[]
    for d in range(order+1):
        value=a[d] if d<len(a) else arb(0)
        value-=sum((b[j]*out[d-j] for j in range(1,min(d,len(b)-1)+1)),arb(0))
        out.append(value/b[0])
    return out

def poisson(f,n,counts):
    rhs=f.derivative();P=f.a+1
    resonant=n>=6 and n%3==0
    order=f.order-int(resonant)
    assert order>=0
    length=max(map(len,rhs.jets),default=0)
    data=[[arb(0)]*length for _ in range(order+1)]
    for j in range(length):
        m=rhs.lo+j
        if m==0 or m%2:
            for d in range(f.order+1):
                assert rhs.jets[d][j].contains(0),('support',n,m,d)
                counts['support_zero_checks']+=1
            continue
        den=[ball(m*m-P*P),ball(-2*P*f.da),ball(-f.da*f.da)]
        vals=[v[j] for v in rhs.jets]
        if m*m==P*P:
            assert resonant and vals[0].contains(0),('obstruction',n,m,str(vals[0]))
            counts['compatible_simple_divisions']+=1
            vals,den=vals[1:],den[1:]
        output=quotient(vals,den,order)
        for d,v in enumerate(output):data[d][j]=v
    g=JetField(P,f.da,rhs.lo,data)
    check=g.derivative().derivative().scale(-1)+g.derivative(True).derivative(True)-rhs.truncate(order)
    for d,poly in enumerate(check.jets):
        for v in poly.coeffs():
            assert v.contains(0),('poisson',n,d,str(v))
            counts['poisson_jet_coefficient_checks']+=1
    return g

def prefix(b,beta1,beta2,N=12):
    coeff=[]
    for d,v in enumerate([b,beta1,beta2]):
        row=[arb(0)]*7
        row[0],row[6]=-v/2,v/2
        if d==0:row[2],row[4]=arb(-1)/2,arb(1)/2
        coeff.append(row)
    f={1:JetField(mpq(1,3),-1,-3,coeff)}
    counts=dict(support_zero_checks=0,compatible_simple_divisions=0,poisson_jet_coefficient_checks=0,ordered_products=0)
    g={1:poisson(f[1],1,counts)}
    for n in range(2,N+1):
        total=JetField(1-mpq(2*n,3),-n)
        for i in range(1,n):
            total=total+g[i].derivative()*f[n-i].derivative(True)-g[i].derivative(True)*f[n-i].derivative()
            counts['ordered_products']+=1
        factor=quotient([ball(mpq(1,3)),arb(-1)],[ball(mpq(2,3)),arb(1)],total.order)
        f[n]=total.scale([v/(n-1) for v in factor])
        if n!=12:g[n]=poisson(f[n],n,counts)
    return f,g,counts

def run():
    ctx.prec=1536
    start=time.monotonic();root=Path('research/157_formal_parameter_curve')
    algpath=Path('research/119_tuned_rational_series/verification/algebraic_roots.json')
    numpath=Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json')
    alg=json.loads(algpath.read_text());initial=json.loads(numpath.read_text())
    P=sp.Poly(sp.sympify(alg['sturm_sequence'][0]),sp.Symbol('b'),domain=sp.QQ)
    coeff=[str(v) for v in reversed(P.all_coeffs())]
    rows=[];text=lambda v:v.str(75,radius=True)
    for old in initial['rows']:
        b,I=refine_root(coeff,old['root_interval'],1664)
        solver=Tuning(1,3);ft,gt,hs=solver.prefix(b,12)
        assert [v['n'] for v in hs]==[6,9,12]
        H6,H9=hs[0]['H'],hs[1]['H'];sigma2=hs[0]['sigma']
        _,g0,c0=prefix(b,arb(0),arb(0),N=6)
        Hlim=g0[6].sine(2)
        Ob=order6_bderivative(b)
        beta1=12*(H6-Hlim)/Ob
        fzero,gzero,c1=prefix(b,beta1,arb(0),N=9)
        fone,gone,c2=prefix(b,beta1,arb(1),N=9)
        C3=sigma2*Ob/(12*18)
        observed=gone[9].sine(4)-gzero[9].sine(4)
        assert observed.overlaps(C3) and not C3.contains(0)
        beta2=(H9-gzero[9].sine(4))/C3
        ff,gg,c3=prefix(b,beta1,beta2,N=12)
        compared=0
        for n in range(1,13):
            for m in range(1,4*n,2):
                assert ff[n].sine(m).overlaps(ft[n].sine(m)),('density_constant',n,m)
                compared+=1
            if n<12:
                for m in range(2,4*n+1,2):
                    assert gg[n].sine(m).overlaps(gt[n].sine(m)),('stream_constant',n,m)
                    compared+=1
        assert ff[12].sine(5).contains(0)
        assert gzero[6].sine(2).overlaps(H6)
        assert not beta2.contains(0)
        linear_residue=hs[1]['sigma']*(gzero[9].sine(4)-H9)/24
        assert not linear_residue.contains(0)
        row=dict(root_index=old['root_index'],root_interval=I,beta1=text(beta1),beta2=text(beta2),second_derivative=text(2*beta2),predicted_beta2_slope=text(C3),observed_beta2_slope=text(observed),H9_linear_curve=text(gzero[9].sine(4)),H9_tuned=text(H9),linear_curve_stream12_pole_residue=text(linear_residue),density12_obstruction=text(ff[12].sine(5)),constant_coefficient_comparisons=compared,counts=[c0,c1,c2,c3],all_checks_pass=True)
        rows.append(row)
        print(json.dumps({k:row[k] for k in ['root_index','beta1','beta2','predicted_beta2_slope','linear_curve_stream12_pole_residue']}),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=1536,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Second parameter jet through the next density compatibility only; formal all-order theorem requires analytic review.')
    (root/'verification/second_jet_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['formal_parameter_jet.py','pure_cartesian_ball.py','parameter_regularization_slope.py','fixed_shape_parameter_limit.py']:
        (root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and p.suffix!='.log'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        failure=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(v.filename).name,line=v.lineno) for v in traceback.extract_tb(exc.__traceback__)])
        Path('research/157_formal_parameter_curve/verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure),flush=True)
        raise SystemExit(1)
