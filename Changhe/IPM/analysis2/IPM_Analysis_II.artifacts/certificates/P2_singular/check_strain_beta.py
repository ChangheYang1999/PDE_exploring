"""Recompute the full-plane strain integral by exact beta integrals.
No center-elimination or Taylor-strain formula is used to evaluate the angular integral.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
from datetime import datetime,timezone
import json

def falling(a,n):
    value=Q(1)
    for i in range(n):value*=a-i
    return value

def beta_integer(n,b):
    assert n>=1 and b>0
    out=Q(factorial(n-1))
    for j in range(n):out/=b+j
    return out

def integral_derivative(l,v,d,j):
    """Integral_0^infty q^j d^d/dq^d [q^l (1+q)^v] dq."""
    ans=Q(0)
    for i in range(d+1):
        coefficient=comb(d,i)*falling(Q(l),d-i)*falling(v,i)
        if not coefficient:continue
        power=l-d+i+j
        assert power>=0
        second=-v+i-power-1
        assert second>0
        ans+=coefficient*beta_integer(power+1,second)
    return ans

base=Path(__file__).resolve().parents[2]
for state in [88,131]:
    data=json.loads((base/f'source_audit/state{state:03d}_exact.json').read_text())
    cl=Q(data['exact_parameters']['cl']);gamma=1/cl
    angular=Q(0);terms=[]
    for (branch,m,k),coeftext in zip(data['canonical_order'],data['canonical_coefficients']):
        if m not in [1,2]:continue
        p=(3+gamma-branch*(1-gamma))/2
        l=k-m;v=p-k
        if m==1:
            value=-8*integral_derivative(l,v,2,0)-2*integral_derivative(l,v,3,1)
        else:
            value=40*integral_derivative(l,v,1,0)+20*integral_derivative(l,v,2,1)+2*integral_derivative(l,v,3,2)
        term=Q(coeftext)*value
        angular+=term
        if term:terms.append({'generator':[branch,m,k],'integral_per_unit_coefficient':str(value),'contribution':str(term)})
    a0=Q(data['origin_rho_coefficients']['(0, 1)'])
    strain=angular-a0/4
    assert strain==Q(data['exact_parameters']['strain'])
    assert strain+cl==1
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'method':'Exact beta integral of the sin(3 theta) density coefficient, with the local term -a0/4. All m=1 and m=2 generators integrated, including high radial orders.','angular_integral_divided_by_pi_exact':str(angular),'angular_integral_decimal':float(angular),'local_term_exact':str(-a0/4),'strain_exact':str(strain),'strain_decimal':float(strain),'normalization_defect_exact':str(strain+cl-1),'nonzero_integrated_generator_contributions':terms,'source_state_sha':data['canonical_serialization_sha256']}
    dest=Path(__file__).with_name(f'state{state:03d}_strain_beta.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(state,'angular',float(angular),'local',float(-a0/4),'strain',float(strain),'defect',strain+cl-1)
