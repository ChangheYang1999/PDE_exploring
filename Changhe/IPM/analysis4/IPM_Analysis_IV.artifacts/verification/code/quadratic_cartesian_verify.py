"""Exact Q(sqrt(5)) extension of the independent Cartesian verifier.

The Cartesian differential calculus is unchanged. A separate adapter lets the
numerics lane's polynomial-convolution implementation use the same exact field
for a coefficient-by-coefficient comparison. No other-lane files are written.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import math
import sys
from gmpy2 import mpq
import cartesian_verify as cv


@dataclass(frozen=True)
class Q5:
    a: mpq = mpq(0)
    b: mpq = mpq(0)

    def __post_init__(self):
        object.__setattr__(self,'a',mpq(self.a))
        object.__setattr__(self,'b',mpq(self.b))

    @staticmethod
    def of(x):
        if isinstance(x,Q5): return x
        assert not isinstance(x,float), 'floating inputs are not exact field data'
        return Q5(mpq(str(x)))

    @staticmethod
    def decode(x):
        a,b=x.split('|')
        return Q5(mpq(a),mpq(b))

    def encode(self): return str(self.a)+'|'+str(self.b)
    def __bool__(self): return bool(self.a or self.b)
    def __float__(self): return float(self.a)+float(self.b)*math.sqrt(5)
    def __neg__(self): return Q5(-self.a,-self.b)
    def __eq__(self,other):
        try: other=self.of(other)
        except (TypeError,ValueError,AssertionError): return False
        return self.a==other.a and self.b==other.b
    def __add__(self,other):
        other=self.of(other)
        return Q5(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __sub__(self,other): return self+(-self.of(other))
    def __rsub__(self,other): return self.of(other)+(-self)
    def __mul__(self,other):
        other=self.of(other)
        return Q5(self.a*other.a+5*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self,other):
        other=self.of(other)
        norm=other.a*other.a-5*other.b*other.b
        assert norm!=0
        return self*Q5(other.a/norm,-other.b/norm)
    def __rtruediv__(self,other): return self.of(other)/self
    def __pow__(self,n):
        assert isinstance(n,int)
        if n<0: return Q5(1)/(self**(-n))
        ans=Q5(1)
        base=self
        while n:
            if n&1: ans=ans*base
            n//=2
            if n: base=base*base
        return ans


class Poly:
    def __init__(self,values): self.values=list(values)
    def __mul__(self,other):
        values=[Q5() for _ in range(len(self.values)+len(other.values)-1)]
        for i,a in enumerate(self.values):
            for j,b in enumerate(other.values): values[i+j]=values[i+j]+a*b
        return Poly(values)


class RingQ5:
    name='exact_qsqrt5'
    zero=Q5()
    def scalar(self,x): return Q5.of(x)
    def poly(self,x): return Poly(x)
    def coeffs(self,p,n): return (p.values+[Q5()]*n)[:n]
    def to_float(self,x): return float(x)
    def to_str(self,x): return x.encode()
    def is_zero(self,x): return not x
    def absf(self,x): return abs(float(x))


def main():
    sys.dont_write_bytecode=True
    # Patch only scalar conversion in this process. The original source stays unchanged.
    cv.Q=Q5.of
    cv.qs=lambda x:Q5.of(x).encode()
    module_path=Path('../a4-num/code/ffcore.py')
    source_data=module_path.read_bytes()
    source_hash=sha256(source_data).hexdigest()
    snapshot=Path('research/01_recurrence/verification/source_snapshots')/('ffcore_'+source_hash+'.py')
    snapshot.parent.mkdir(parents=True,exist_ok=True)
    if not snapshot.exists(): snapshot.write_bytes(source_data)
    spec=importlib.util.spec_from_file_location('numerics_ffcore_q5',module_path)
    module=importlib.util.module_from_spec(spec)
    exec(compile(source_data,snapshot.as_posix(),'exec'),module.__dict__)
    c=Q5(mpq(5,4),mpq(1,4))
    assert 1-1/c==Q5(0,mpq(1,5))
    cases=[]
    for initial in [{1:Q5(1)},{1:Q5(1),3:Q5(1)}]:
        result=cv.recurrence(c,initial,5,require_potential=True)
        inputs=[initial.get(k,Q5()) for k in range(1,max(initial)+1,2)]
        engine=module.FarField(RingQ5(),c,inputs)
        comparisons=0
        for row in result['rows']:
            n=row['n']
            if n>1: assert engine.step()==n
            generated={
                'density':{str(2*k+1):x for k,x in enumerate(engine.f[n]) if x},
                'stream':{str(2*k):x for k,x in enumerate(engine.g[n]) if x},
                'potential':{str(2*k):x for k,x in enumerate(engine.chi_coeffs(n)) if x},
            }
            for kind in generated:
                expected={k:Q5.decode(v) for k,v in row[kind].items() if Q5.decode(v)}
                assert expected==generated[kind],(initial,n,kind)
                comparisons+=len(expected)
        cases.append({'initial':{str(k):v.encode() for k,v in initial.items()},
                      'recursion':result,'exact_matching_coefficients':comparisons})
    out={
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'field_encoding':'a|b means a+b*sqrt(5), with a and b exact rationals',
        'adapter_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'cartesian_engine_sha256':sha256(Path('code/cartesian_verify.py').read_bytes()).hexdigest(),
        'numerics_module_sha256':source_hash,
        'numerics_source_snapshot':snapshot.as_posix(),
        'cases':cases,
    }
    path=Path('research/01_recurrence/verification/quadratic_field_comparison.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Both exact quadratic-field cases agree through order five, including potential reconstruction.')


if __name__=='__main__':
    main()
