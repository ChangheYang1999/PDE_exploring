import importlib.util,sympy as s,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
TOP=Path(__file__).resolve().parents[1];p=TOP/'code/certify.py';sp=importlib.util.spec_from_file_location('nh',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
x,y=s.symbols('x y',positive=True);r=s.sqrt(x*x+y*y);theta=s.atan(y/x)
count=0
for q,orders in [(3,['xx','xy','yy']),(4,['xxx','xxy','xyy','yyy'])]:
 for n in range(1,6):
  for e in [0,1,2]:
   f=s.expand_trig(r**(q+e)*s.sin(n*theta))
   for axes in orders:
    target=f
    for ax in axes:target=s.diff(target,x if ax=='x' else y)
    formula=0
    for (kind,k),poly in m.differentiate_map(q,n,axes).items():
     coefficient=sum(s.Rational(c.numerator,c.denominator)*e**j for j,c in enumerate(poly))
     formula+=coefficient*(s.sin(k*theta) if kind=='s' else s.cos(k*theta))
    formula=s.expand_trig(formula)*r**(q+e-len(axes))
    assert s.simplify(target-formula)==0,(q,n,e,axes)
    count+=1
v=s.symbols('v');S=126*v**5-420*v**6+540*v**7-315*v**8+70*v**9
assert s.expand(s.diff(S,v)-630*v**4*(1-v)**4)==0
assert s.expand(S+S.subs(v,1-v)-1)==0
assert all(s.diff(S,v,j).subs(v,z)==0 for j in range(1,5) for z in [0,1])
assert s.integrate(S,(v,0,1))==s.Rational(1,2)
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','cartesian_symbolic_checks':count,'cutoff_symbolic_checks':'PASS','certify_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(TOP/'evidence/algebra_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
