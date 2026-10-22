"""Independent exact replay: differentiate G through X=x²,Y=eta²,e=E.

Does not import the certificate generator. Bernstein coefficients use the
homogenization identity and every rectangle is independently pulled back.
No numerical sampling accepts a certificate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,datetime,hashlib,json,time,platform
import sympy as s


def derive_polynomial(coeff,a0):
    X,Y,e=s.symbols('X Y e', positive=True)
    t,w=s.symbols('t w', positive=True)
    c=[[s.Rational(v) for v in row] for row in coeff]
    p=sum(s.Rational(2-j,6)*c[j][0] for j in range(len(c)))
    d=p*(s.Rational(a0)-70)/14
    def dx(f):return s.diff(f,X)+s.diff(f,e)
    def dy(f):return s.diff(f,Y)+3*Y**2*s.diff(f,e)
    answer=0
    substitutions={X:(1-t**6-w**3)/t**6,Y:w/t**2,e:t**-6}
    for j,row in enumerate(c):
        for k,cjk in enumerate(row):
            if not cjk:continue
            f=cjk*Y**(3*k)*e**(s.Rational(2-j,6)-k)
            A=f+2*X*dx(f)+2*Y*dy(f)+4*X*Y*dx(dy(f))
            answer+=s.expand(t**2*A.subs(substitutions,simultaneous=True))
    f=d*Y/e
    A=f+2*X*dx(f)+2*Y*dy(f)+4*X*Y*dx(dy(f))
    answer+=s.expand(t**2*A.subs(substitutions,simultaneous=True))
    answer=s.Poly(s.expand(answer),t,w)
    return {(int(i),int(j)):F(str(v)) for (i,j),v in answer.terms()}


def pullback(poly,tl,th,wl,wh):
    out={}
    for (i,j),a in poly.items():
        for p in range(i+1):
            for q in range(j+1):
                out[p,q]=out.get((p,q),F(0))+a*comb(i,p)*tl**(i-p)*(th-tl)**p*comb(j,q)*wl**(j-q)*(wh-wl)**q
    return {k:v for k,v in out.items() if v}


def homogenized_bernstein(poly,n,m):
    # (1+s)^n(1+z)^m B(s/(1+s),z/(1+z))
    homogeneous={}
    for (i,j),a in poly.items():
        for p in range(i,n+1):
            for q in range(j,m+1):
                homogeneous[p,q]=homogeneous.get((p,q),F(0))+a*comb(n-i,p-i)*comb(m-j,q-j)
    return {(p,q):homogeneous.get((p,q),F(0))/(comb(n,p)*comb(m,q)) for p in range(n+1) for q in range(m+1)}


def reconstruct_power(bern,n,m):
    out={}
    for (i,j),b in bern.items():
        for p in range(i,n+1):
            for q in range(j,m+1):
                out[p,q]=out.get((p,q),F(0))+b*comb(n,i)*comb(m,j)*comb(n-i,p-i)*comb(m-j,q-j)*(-1)**(p-i+q-j)
    return {k:v for k,v in out.items() if v}


def rectangle(path):
    tl,th,wl,wh=F(0),F(1),F(0),F(1)
    for ch in path:
        if ch=='0':th=(tl+th)/2
        elif ch=='1':tl=(tl+th)/2
        elif ch=='2':wh=(wl+wh)/2
        elif ch=='3':wl=(wl+wh)/2
        else:raise ValueError(ch)
    return tl,th,wl,wh


def cover(paths,prefix=''):
    if prefix in paths:
        if any(p!=prefix and p.startswith(prefix) for p in paths):return False
        return True
    nextchars={p[len(prefix)] for p in paths if p.startswith(prefix)}
    if nextchars not in ({'0','1'},{'2','3'}):return False
    return all(cover(paths,prefix+c) for c in nextchars)


def replay(root):
    start=time.monotonic();data=json.loads((root/'input.json').read_text());cert=json.loads((root/'certificate.json').read_text())
    assert F(data['a0'])!=0
    recorded={(r['t_power'],r['w_power']):F(r['coefficient']) for r in data['polynomial']}
    derived=derive_polynomial(data['coeff'],data['a0'])
    assert recorded==derived,'Symbolic mixed derivative disagrees with polynomial'
    assert cert['input_sha256']==hashlib.sha256((root/'input.json').read_bytes()).hexdigest()
    n,m=cert['degree'];assert n>=max(i for i,j in derived) and m>=max(j for i,j in derived)
    assert cert['verdict']=='CONFIRMED_CHART'
    leaves=cert['leaves'];paths={leaf['path'] for leaf in leaves}
    assert len(paths)==len(leaves) and cover(paths),'Incomplete or overlapping tree'
    bounds=[]
    for leaf in leaves:
        tl,th,wl,wh=rectangle(leaf['path'])
        if leaf['kind']=='outside':assert tl**6+wl**3>1
        else:
            local=pullback(derived,tl,th,wl,wh)
            bern=homogenized_bernstein(local,n,m)
            assert reconstruct_power(bern,n,m)==local,'Complete Bernstein basis reconstruction failed'
            lower=min(bern.values());assert lower>0
            assert lower==F(int(leaf['minimum_numerator']),int(leaf['denominator']))
            bounds.append(lower)
    assert min(bounds)==F(cert['lower_bound'])
    out=dict(software=dict(python=platform.python_version(),sympy=s.__version__),utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),verdict='CONFIRMED_EXACT_CHART',independent_symbolic_G_derivative=True,full_Bernstein_basis_reconstruction=True,finite_tree_coverage=True,leaf_count=len(leaves),lower_bound=str(min(bounds)),lower_bound_float=float(min(bounds)),center_sum=data['center_sum'],exact_center_completion=data['exact_center_completion'],c20_change=data['c20_change'],source_sha256=data['source_sha256'],input_sha256=cert['input_sha256'],certificate_sha256=hashlib.sha256((root/'certificate.json').read_bytes()).hexdigest(),replay_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,scope='Only exact chart positivity; no vorticity PDE conclusion. Center completion, if present, changes the source coefficients by the recorded exact rational.')
    (root/'independent_replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('roots',nargs='+');args=ap.parse_args()
    for root in args.roots:replay(Path(root))
