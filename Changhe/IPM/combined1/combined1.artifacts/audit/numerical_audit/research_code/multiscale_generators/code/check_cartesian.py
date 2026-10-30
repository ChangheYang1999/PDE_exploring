"""Cross-check scaled generator jets against canonical jets and symbolic derivatives."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,time
from flint import arb,ctx
from cartesian import GeneratorJet
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1]
def digest(p):return sha256(p.read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
start=time.monotonic();ctx.prec=1024
old=load('old_cartesian',ROOT/'research/point_witness/code/cartesian.py')
rows=[]
for name in ['d2','Mpen2']:
    p=ROOT/f'research/refit_audit/data/{name}_canonical.json'
    for x,y in [('0','1'),('3/7','3/16'),('100','200')]:
        a=GeneratorJet(p,x,y);b=old.CartesianJet(p,x,y)
        checks={f'{i},{j}':a.chi(i,j).overlaps(b.chi(i,j)) for i in range(5) for j in range(5-i)}
        checks.update({k:v.overlaps(b.fields()[k]) for k,v in a.fields().items()})
        assert all(checks.values()),(name,x,y,checks)
        rows.append({'name':name,'point':[x,y],'source_sha256':digest(p),'checks':checks})
for name in ['C1-N1-002-7branch-frf','C1-N1-003-8branch-frf','C1-N1-004-4branch-l2fw']:
    folder=ROOT/f'research/candidate_audits/data/{name}'
    p=folder/'normalized_generators.json';q=folder/'canonical.json'
    a=GeneratorJet(p,'3/7','3/16');b=old.CartesianJet(q,'3/7','3/16')
    checks={f'{i},{j}':a.chi(i,j).overlaps(b.chi(i,j)) for i in range(5) for j in range(5-i)}
    checks.update({k:v.overlaps(b.fields()[k]) for k,v in a.fields().items()})
    assert all(checks.values()),(name,checks)
    rows.append({'name':name,'point':['3/7','3/16'],'source_sha256':digest(p),'canonical_sha256':digest(q),'checks':checks})
print('canonical comparisons',len(rows),'seconds',time.monotonic()-start,flush=True)
# Independent exact symbolic differentiation in Cartesian coordinates.
import sympy as S
x,y=S.symbols('x y',real=True);s=x*x+y*y
synthetic=[]
for m,w,n,q,R,px,py in [(0,5,0,0,10,'1/3','2/5'),(1,4,1,4,100,'50','100/3'),(2,3,3,4,10,'1','2'),(2,3,2,0,S.Rational(1,2),'0','1'),(0,0,3,4,100,'0','0'),(2,0,1,0,10,'0','0')]:
    # c=5/2, j=1 gives p=7/5 exactly.
    data={'cl':'5/2','generators':[{'j':1,'m':m,'spec':['legqs',w,n,q,str(R)],'coef':'1'}]}
    jet=GeneratorJet(data,px,py)
    H=sum(S.binomial(2*m,k)*(-1)**(k//2)*x**(2*m-k)*y**k for k in range(0,2*m+1,2))
    expr=H*(1+s)**(S.Rational(7,5)-m)*(s/(R*R+s))**w*(R*R/(R*R+s))**q*S.legendre(n,(s-R*R)/(s+R*R))
    checks={};largest=arb(0)
    for i in range(5):
        for j in range(5-i):
            exact=S.diff(expr,x,i,y,j).subs({x:S.Rational(px),y:S.Rational(py)})
            # Sympy produces a decimal evaluation, so this is an accuracy check,
            # not an independent interval enclosure.
            approximate=arb(str(S.N(exact,180)))
            error=abs(jet.chi(i,j)-approximate);threshold=arb('1e-160')*(1+abs(approximate))
            assert error<threshold,(m,w,n,q,R,px,py,i,j,error)
            checks[f'{i},{j}']=True;largest=largest.max(error)
    synthetic.append({'m':m,'w':w,'n':n,'Q':q,'R':str(R),'point':[px,py],
                      'all_15_symbolic_derivatives_agree_to_160_relative_decimal_places':True,
                      'largest_absolute_difference':largest.str(40)})
    print('symbolic',len(synthetic),'seconds',time.monotonic()-start,flush=True)
# Exact origin vanishing of degree >=10, with no floating zero threshold.
origin=[]
for m,w,n,q,R in [(0,5,0,0,10),(1,4,11,4,100),(2,3,3,4,10),(9,0,11,0,100)]:
    data={'cl':'5/2','generators':[{'j':1,'m':m,'spec':['legqs',w,n,q,str(R)],'coef':'7/11'}]}
    jet=GeneratorJet(data,'0','0',order=9)
    assert all(value.is_zero() for value in jet.values.values())
    origin.append({'m':m,'w':w,'n':n,'Q':q,'R':R,'all_55_jets_exactly_zero':True})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
     'canonical_comparisons':rows,'synthetic_comparisons':synthetic,'origin_comparisons':origin,
     'own_code_sha256':digest(BASE/'code/cartesian.py'),'driver_sha256':digest(Path(__file__)),
     'old_code_sha256':digest(ROOT/'research/point_witness/code/cartesian.py'),
     'proof_sha256':digest(BASE/'PROOF.md'),'elapsed_seconds':time.monotonic()-start,
     'scope':'Symbolic decimal comparisons are accuracy checks; canonical Arb comparisons are interval overlaps, not new global certificates.'}
p=BASE/'verification/cartesian_comparisons.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('complete seconds',out['elapsed_seconds'],flush=True)
