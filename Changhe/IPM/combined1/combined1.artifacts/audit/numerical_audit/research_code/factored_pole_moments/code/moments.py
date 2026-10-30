"""Finite positive-pole moments retaining (1-v)^m as a scalar power."""
from pathlib import Path
import importlib.util
from flint import arb, fmpq as Q, fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('n4_exact_pole_decomposition',ROOT/'research/rational_pole_moments/code/moments.py')
OLD=importlib.util.module_from_spec(spec);spec.loader.exec_module(OLD)
ar=OLD.ar

def beta(a,b):
    a,b=Q(a),Q(b);assert a>0 and b>0
    return ar(a).gamma()*ar(b).gamma()/ar(a+b).gamma()

def pole_moments(b,m,a,maximum,verify_direct=True):
    b,a=Q(b),Q(a)
    assert b>-1 and isinstance(m,int) and m>=0 and a>0 and isinstance(maximum,int) and maximum>=0
    base=beta(b+1,m+1)
    def direct(k):
        return base*(-ar(a)).hypgeom_2f1(arb(k),ar(b+1),ar(b+m+2),bc=True,abc=True)
    vals=[base];rows=[]
    if maximum:vals.append(direct(1))
    for k in range(2,maximum+1):
        numerator=ar(b+m+3-k)*vals[k-2]-ar(a*(b+2-k)+b+m+4-2*k)*vals[k-1]
        vals.append(numerator/ar((k-1)*(a+1)))
    for k,value in enumerate(vals):
        assert value.is_finite() and value>0
        row={'k':k,'recurrence_accuracy_bits':value.rel_accuracy_bits()}
        if verify_direct:
            other=base if k==0 else direct(k)
            assert value.overlaps(other) and other>0 and other.is_finite()
            row.update({'direct_overlap':True,'direct_accuracy_bits':other.rel_accuracy_bits()})
        rows.append(row)
    return vals,rows

def integral(b,m,numerator,factors,verify_direct=True):
    b=Q(b);assert b>-1 and isinstance(m,int) and m>=0
    polynomial,parts,merged,degree=OLD.decompose(numerator,factors)
    moment=beta(b+1,m+1);total=arb(0)
    for j,c in enumerate(polynomial):
        total+=ar(c)*moment
        moment*=ar((b+j+1)/(b+m+j+2))
    cache={};checks={}
    for a,d in merged:
        cache[a],checks[str(a)]=pole_moments(b,m,a,d,verify_direct)
    for a,k,c in parts:total+=ar(c)*cache[a][k]
    assert total.is_finite()
    return total,{'b':str(b),'m':m,'factors':[[str(a),d] for a,d in merged],
        'numerator_degree':numerator.degree(),'denominator_degree':degree,
        'polynomial_degree':polynomial.degree(),'principal_parts':len(parts),
        'exact_decomposition_replayed':True,'pole_power_checks':checks,
        'relative_accuracy_bits':total.rel_accuracy_bits()}
