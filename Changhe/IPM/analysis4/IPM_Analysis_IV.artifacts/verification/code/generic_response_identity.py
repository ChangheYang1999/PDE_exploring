"""Cartesian generic response identity over exact Q(k), interpolating only in b."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import ast,gzip,json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq,fmpq_poly
import sympy as sp
import tuned_cartesian_exact as ce
ROOT=Path('research/173_generic_response_identity')


def quotient(a,b):
    q,r=divmod(a,b);assert not r
    return q


class Rat:
    def __init__(self,n=0,d=1,normalized=False):
        if isinstance(n,Rat):
            assert d==1;self.n,self.d=n.n,n.d;return
        n=n if isinstance(n,fmpq_poly) else fmpq_poly([fmpq(str(n))])
        d=d if isinstance(d,fmpq_poly) else fmpq_poly([fmpq(str(d))])
        assert d
        if not n:self.n,self.d=fmpq_poly([]),fmpq_poly([1]);return
        if not normalized:
            g=n.gcd(d);n,d=quotient(n,g),quotient(d,g)
        lead=d[d.degree()]
        self.n,self.d=n/lead,d/lead
    def __bool__(self):return bool(self.n)
    def __neg__(self):return Rat(-self.n,self.d,True)
    def __add__(self,o):
        o=Rat(o)
        if not self:return o
        if not o:return self
        g=self.d.gcd(o.d);a,b=quotient(self.d,g),quotient(o.d,g)
        n=self.n*b+o.n*a
        if not n:return Rat(0)
        h=n.gcd(g)
        return Rat(quotient(n,h),a*quotient(o.d,h),True)
    __radd__=__add__
    def __sub__(self,o):return self+-Rat(o)
    def __rsub__(self,o):return Rat(o)+-self
    def __mul__(self,o):
        o=Rat(o)
        if not self or not o:return Rat(0)
        g,h=self.n.gcd(o.d),o.n.gcd(self.d)
        return Rat(quotient(self.n,g)*quotient(o.n,h),quotient(self.d,h)*quotient(o.d,g),True)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Rat(o);assert o
        return self*Rat(o.d,o.n,True)
    def __rtruediv__(self,o):return Rat(o)/self
    def __eq__(self,o):
        o=Rat(o);return self.n*o.d==o.n*self.d
    def __str__(self):return f'({self.n})/({self.d})'


Rat.zero=Rat(0);Rat.one=Rat(1)


def main():
    start=time.monotonic()
    ce.K=Rat;ce.R=Rat;ce.k=Rat(fmpq_poly([0,1]));ce.MOD=None
    ce.p=lambda n:1-Rat(4)*n/9
    lowpath=Path('research/144_general_rational_response_limit/verification/h2_Q9.json')
    low=json.loads(lowpath.read_text());b=sp.Symbol('b')
    fixed={}
    for label in ['low_density','low_stream']:
        fixed[label]={}
        for n,field in low[label].items():
            terms={ast.literal_eval(m):fmpq_poly([fmpq(str(c)) for c in reversed(sp.Poly(sp.sympify(v),b).all_coeffs())]) for m,v in field['signed_laurent'].items()}
            fixed[label][int(n)]=(Rat(field['radial_exponent']),terms)
    genpath=Path('research/164_four_ninths_response_minima/verification/reduced_generic.json.gz')
    gen=json.loads(gzip.decompress(genpath.read_bytes()))
    cols=[fmpq_poly([fmpq(v) for v in row]) for row in gen['numerator_by_b_degree']]
    den=fmpq_poly([fmpq(v) for v in gen['denominator']]);assert len(cols)<=10
    rows=[]
    for value in [0,1,-1,2,-2,3,-3,4,-4,5]:
        begin=time.monotonic()
        def load(label):
            return {n:ce.F(q,{m:Rat(pol(value)) for m,pol in terms.items()}) for n,(q,terms) in fixed[label].items()}
        ff,gg=load('low_density'),load('low_stream')
        n=9*ce.k;e=ce.sine(ce.p(n)+1,(4,-2));U={};V={};supports=[]
        for r in range(1,10):
            total=ce.adv(e,ff[r])
            for s in range(1,r):total=total+ce.adv(V[s],ff[r-s])+ce.adv(gg[r-s],U[s])
            U[r]=total.scale(Rat(5)/(4*(n+r-1)));U[r].check_sine()
            assert all(abs(a)==4 and abs(offset+2 if a==4 else offset-2)<=4*r-1 for a,offset in U[r].v)
            if r<9:V[r]=ce.poisson(U[r])
            supports.append(dict(r=r,density_terms=len(U[r].v),stream_terms=len(V[r].v) if r<9 else None))
        actual=2*U[9].v.get((4,1),Rat.zero)
        numerator=sum((col*value**j for j,col in enumerate(cols)),fmpq_poly([]))
        expected=Rat(numerator,den)
        assert actual==expected,('generic identity',value)
        row=dict(b=value,exact_rational_identity=True,numerator_degree=actual.n.degree(),denominator_degree=actual.d.degree(),supports=supports,actual_elapsed_s=time.monotonic()-begin,
            numerator_sha256=sha256(str(actual.n).encode()).hexdigest(),denominator_sha256=sha256(str(actual.d).encode()).hexdigest())
        rows.append(row)
        (ROOT/'verification/partial.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n')
        print(json.dumps(row),flush=True)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,degree_bound_in_b=9,distinct_specializations=10,rows=rows,actual_elapsed_s=time.monotonic()-start,
        inputs={str(p):dict(sha256=sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in [lowpath,genpath]})
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['generic_response_identity.py','tuned_cartesian_exact.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__=='__main__':main()
