"""Differentiate the Cartesian recurrence at delta=2/3 with fixed leading shape."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq
from flint import arb,arb_poly,ctx
import sympy as sp
from pure_cartesian_ball import Field,Tuning,ball,refine_root,sine

class DField:
    def __init__(self,a,da,lo=0,v=None,d=None):
        self.a,self.da,self.lo=mpq(a),mpq(da),lo
        self.v=arb_poly([] if v is None else v);self.d=arb_poly([] if d is None else d)
    def scale(self,c,dc=0):return DField(self.a,self.da,self.lo,self.v*c,self.d*c+self.v*dc)
    def __add__(self,o):
        assert self.a==o.a and self.da==o.da
        lo=min(self.lo,o.lo)
        def align(p,offset):return arb_poly([arb(0)]*(offset-lo)+p.coeffs())
        return DField(self.a,self.da,lo,align(self.v,self.lo)+align(o.v,o.lo),align(self.d,self.lo)+align(o.d,o.lo))
    def __sub__(self,o):return self+o.scale(-1)
    def __mul__(self,o):return DField(self.a+o.a,self.da+o.da,self.lo+o.lo,self.v*o.v,self.d*o.v+self.v*o.d)
    def derivative(self,y=False):
        N=max(len(self.v),len(self.d));v=[arb(0)]*(N+2);d=[arb(0)]*(N+2)
        for j in range(N):
            m=self.lo+j
            for offset,factor,sign in [(0,ball((self.a+m)/2),1),(2,ball((self.a-m)/2),-1 if y else 1)]:
                v[j+offset]+=self.v[j]*factor*sign
                d[j+offset]+=(self.d[j]*factor+self.v[j]*ball(self.da/2))*sign
        return DField(self.a-1,self.da,self.lo-1,v,d)
    def coefficient(self,m,derivative=False):
        p=self.d if derivative else self.v
        return p[m-self.lo] if m>=self.lo else arb(0)
    def sine(self,m,derivative=False):return 2*self.coefficient(m,derivative)

def adv(g,f):return g.derivative()*f.derivative(True)-g.derivative(True)*f.derivative()
def poisson(f):
    rhs=f.derivative();P=f.a+1;N=max(len(rhs.v),len(rhs.d));v=[];d=[]
    for j in range(N):
        m=rhs.lo+j;den=m*m-P*P;dden=-2*P*f.da
        if den:
            value=rhs.v[j]/ball(den);der=rhs.d[j]/ball(den)-value*ball(dden/den)
        else:
            assert rhs.v[j].contains(0) and rhs.d[j].contains(0);value=der=arb(0)
        v.append(value);d.append(der)
    return DField(P,f.da,rhs.lo,v,d)

def run():
    ctx.prec=1024;start=time.monotonic();root=Path('research/151_fixed_shape_parameter_limit')
    data=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json').read_text())
    alg=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_roots.json').read_text())
    P=sp.Poly(sp.sympify(alg['sturm_sequence'][0]),sp.Symbol('b'),domain=sp.QQ);coeff=[str(v) for v in reversed(P.all_coeffs())]
    rows=[];delta=mpq(2,3)
    for row in data['rows']:
        b,I=refine_root(coeff,row['root_interval'],1088)
        f0=sine(1-delta,1,arb(1))+sine(1-delta,3,b)
        f={1:DField(1-delta,-1,f0.lo,f0.poly)};g={1:poisson(f[1])}
        for n in range(2,7):
            total=DField(1-n*delta,-n)
            for i in range(1,n):total=total+adv(g[i],f[n-i])
            factor=(1-delta)/(delta*(n-1));dfactor=-1/(delta*delta*(n-1))
            f[n]=total.scale(ball(factor),ball(dfactor))
            if n<6:g[n]=poisson(f[n])
        assert f[6].sine(1).contains(0)
        Hlim=f[6].sine(1,True)/12+f[6].sine(3)/8
        solver=Tuning(1,3);ft,gt,hs=solver.prefix(b,6)
        Hstar=hs[0]['H'];sigma=hs[0]['sigma'];difference=Hlim-Hstar;residue=sigma*difference/18
        assert not residue.contains(0)
        # Replace only the removable-limit harmonic and recompute the next obstruction.
        g6=solver.poisson(ft[6],6,Hlim);gfixed=dict(gt);gfixed[6]=g6;ffixed=dict(ft)
        for n in range(7,10):
            ffixed[n]=solver.order(n,ffixed,gfixed)
            if n<9:gfixed[n]=solver.poisson(ffixed[n],n)
        obstruction=ffixed[9].sine(3)
        assert obstruction.overlaps(sigma*difference)
        for n in range(1,7):
            for m in range(1,4*n,2):assert f[n].sine(m).overlaps(ft[n].sine(m))
        text=lambda v:v.str(65,radius=True)
        r=dict(root_index=row['root_index'],root_interval=I,root_ball=text(b),density6_sin1=text(f[6].sine(1)),density6_sin1_delta_derivative=text(f[6].sine(1,True)),density6_sin3=text(f[6].sine(3)),H6_limit=text(Hlim),H6_tuned=text(Hstar),difference=text(difference),sigma2=text(sigma),obstruction9=text(obstruction),stream9_pole_residue=text(residue),residue_excludes_zero=True,all_density_values_match=True,next_obstruction_matches_affine_formula=True)
        rows.append(r);print(json.dumps(r),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=1024,rows=rows,actual_elapsed_s=time.monotonic()-start)
    (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['fixed_shape_parameter_limit.py','pure_cartesian_ball.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
    files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
if __name__=='__main__':
    try:run()
    except Exception as exc:
        import traceback
        fail=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/151_fixed_shape_parameter_limit/verification/FAILURE.json').write_text(json.dumps(fail,indent=2)+'\n');print(json.dumps(fail),flush=True);raise SystemExit(1)
