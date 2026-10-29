#!/usr/bin/env python3
"""Check algebra and reject deliberately invalid finite certificates."""
import copy,json,time
from pathlib import Path
from fractions import Fraction as F
import sympy as sp
from ring_seed_certificate import load_exact,parameters,power_bound_valid,check_case
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parent

def main():
    start=time.perf_counter();checks=[]
    def check(name,test):
        if not test:raise AssertionError(name)
        checks.append(name)
    def rejects(name,row,cert):
        try:check_case(row,cert)
        except ValueError:checks.append(name);return
        raise AssertionError(name)
    rows=load_exact(LANE/'research/decaying_ring_seed/data/lead_ring_t2_params.json')
    location=LANE/'research/decaying_ring_seed/verification/certificates'
    for i,row in enumerate(rows):
        cert=json.loads((location/f'case_{i:03d}.json').read_text());out=check_case(row,cert)
        check(f'case_{i}_positive_global_bound',F(out['minimum_certified_H_lower'])>0)
        check(f'case_{i}_two_zeros',out['zero_count_in_closed_half_plane']==2)
    row=rows[0];cert=json.loads((location/'case_000.json').read_text())
    bad=copy.deepcopy(cert);bad['cells'][0]['power_lower']='1000';rejects('reject false power bound',row,bad)
    bad=copy.deepcopy(cert);bad['cells'][0]['left']='1/100';rejects('reject gap at zero',row,bad)
    bad=copy.deepcopy(cert);bad['cells'].pop();rejects('reject uncovered terminal interval',row,bad)
    bad=copy.deepcopy(cert);bad['cutoff']='1/100';rejects('reject unproved tail',row,bad)
    bad=copy.deepcopy(cert);bad['root_bracket']['left']='2';rejects('reject invalid root bracket',row,bad)
    badrow=copy.deepcopy(row);badrow['Finf']=F(1000);rejects('reject negative B',badrow,cert)
    check('exact lower-bound power inequality',power_bound_valid(F(1,2),F(4),F(1,2),True))
    check('exact upper-bound power inequality',power_bound_valid(F(1,2),F(4),F(1,2),False))
    check('reject strict false lower power',not power_bound_valid(F(3,5),F(4),F(1,2),True))
    x,n=sp.symbols('x n',positive=True);S=(1-(n-1)*x)/(1+x)**2
    check('S derivative',sp.simplify(sp.diff(S,x)-((n-1)*x-(n+1))/(1+x)**3)==0)
    s,z,f3,c=sp.symbols('s z f3 c');phi=z*f3*(s+z*z)**3
    eta=-8*sp.diff(phi,s)-4*s*sp.diff(phi,s,2)-sp.diff(phi,z,2)
    check('origin eta split',sp.expand(eta+66*f3*(s*s*z+2*s*z**3+z**5))==0)
    for aa,bb,want in [(2,1,3*c),(1,3,3+12*c),(0,5,6+21*c)]:
        check(f'origin divisor {aa} {bb}',sp.expand((1+c)*(1-aa)+(1+4*c)*bb-want)==0)
    data=dict(all_passed=True,checks=checks,count=len(checks),elapsed_seconds=time.perf_counter()-start)
    atomic_json(ROOT/'results/ring_seed_certificate_tests.json',data);print(json.dumps(data,indent=2))
if __name__=='__main__':main()
