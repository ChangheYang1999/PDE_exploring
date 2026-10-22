"""Manufactured exact polynomials and truncated powers for packet169.

Known scalar functions provide independent values and derivative jumps.
The derivative generator and de Boor finite-difference checker are both
checked against these functions; equality between implementations alone
is not counted as a manufactured control.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb,factorial
from datetime import datetime,timezone
import json,time,sys
from certify_spline_knot_jumps import dcoeff
from check_spline_knot_jumps import value,derivative_by_values

start=time.monotonic();rows=[]
for p in [1,2,3,5]:
    edges=[Q(0),Q(1,7),Q(2,5),Q(3,4),Q(1)]
    knots=[Q(0)]*p+edges+[Q(1)]*p;nb=len(knots)-p-1
    functions=[]
    for m in range(p+1):
        c=[]
        for j in range(nb):
            a=knots[j+1:j+p+1]
            c.append(sum((__import__('functools').reduce(lambda x,y:x*y,z,Q(1)) for z in combinations(a,m)),Q(0))/comb(p,m))
        functions.append((f'monomial_{m}',c,lambda x,m=m:x**m,lambda left,right,m=m:Q(factorial(p)) if m==p else Q(0)))
    for tau in edges[1:-1]:
        c=[]
        for j in range(nb):
            product=Q(1)
            for k in knots[j+1:j+p+1]:product*=max(k-tau,Q(0))
            c.append(product)
        functions.append((f'truncated_power_at_{tau}',c,lambda x,tau=tau:max(x-tau,Q(0))**p,lambda left,right,tau=tau:Q(factorial(p)) if left>=tau else Q(0)))
    for name,c,fun,known in functions:
        dk,dc=dcoeff(knots,c,p);assert dk==edges
        count=0
        expected=[]
        for i,(left,right) in enumerate(zip(edges[:-1],edges[1:])):
            for j in range(1,10):
                x=left+(right-left)*Q(j,10)
                assert value(knots,c,p,x)==fun(x);count+=1
            known_d=known(left,right);expected.append(known_d)
            assert dc[i]==known_d
            assert derivative_by_values(knots,c,p,left,right)==known_d
        jumps=[b-a for a,b in zip(dc[:-1],dc[1:])]
        if name.startswith('monomial'):assert all(j==0 for j in jumps)
        else:assert sum(j!=0 for j in jumps)==1 and sum(jumps)==factorial(p)
        rows.append({'degree':p,'function':name,'exact_value_tests':count,'exact_derivative_tests':2*len(dc),'jumps':[str(j) for j in jumps],'pass':True})
# Explicit angular jump polynomials show two ways the axis test can miss.
# For a single pth-derivative jump J, a mode1 has value0 atcos(phi)=0
# but3J/5 atcos(phi)=3/5,sin(phi)=4/5, wherephysicalx is nonzero.
J=Q(factorial(5));odd_axis=J*0;odd_offaxis=J*Q(3,5)
# Even modes0and2with equaljump haveaxis J-J=0 andoffaxis18J/25.
even_axis=J-J;even_offaxis=J*(1+(2*Q(3,5)**2-1))
assert odd_axis==even_axis==0 and odd_offaxis!=0 and even_offaxis!=0
negative={'odd_mode_axis_can_miss_jump':{'axis':str(odd_axis),'offaxis':str(odd_offaxis),'pass':True},'even_mode_cancellation_can_miss_jump':{'axis':str(even_axis),'offaxis':str(even_offaxis),'pass':True}}
d={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'manufactured_functions':rows,'function_count':len(rows),'exact_value_count':sum(r['exact_value_tests'] for r in rows),'exact_derivative_count':sum(r['exact_derivative_tests'] for r in rows),'scope_controls':negative,'all_passed':True}
out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='manufactured_functions'},indent=2))
