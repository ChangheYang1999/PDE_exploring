"""Packet119 exact controls plus separately implemented SymPy PDE expansion."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,random,time
import sympy as sp
import exact_bivariate as P
from formal_center_recursion import run,base_stream,temperature,harmonic,poisson_right_inverse

start=time.monotonic();root=Path('research/119_flat_center_realization/verification')
root.mkdir(exist_ok=True);rng=random.Random(421119)
x,y=sp.symbols('x y')
symq=lambda q:sp.Rational(Q(q).numerator,Q(q).denominator)
def from_rows(rows):
    return sum(symq(r['coefficient'])*x**r['x_power']*y**r['y_power'] for r in rows)
def symbolic_check(data):
    beta=symq(data['parameters']['beta']);psi=from_rows(data['final_psi']);theta=from_rows(data['final_theta'])
    W1=beta*x-sp.diff(psi,y);W2=beta*y+sp.diff(psi,x)
    omega=-sp.diff(psi,x,2)-sp.diff(psi,y,2)
    ft=sp.Poly(sp.expand(W1*sp.diff(theta,x)+W2*sp.diff(theta,y)-(beta-2)*theta),x,y)
    go=sp.Poly(sp.expand(W1*sp.diff(omega,x)+W2*sp.diff(omega,y)+omega-sp.diff(theta,x)),x,y)
    badT=[(k,str(v)) for k,v in ft.terms() if sum(k)<=data['max_temperature_degree'] and v]
    badO=[(k,str(v)) for k,v in go.terms() if sum(k)<=data['max_vorticity_degree'] and v]
    assert not badT and not badO,(badT,badO)
    return {'sympy_exact_temperature_coefficients_zero_through':data['max_temperature_degree'],
            'sympy_exact_vorticity_coefficients_zero_through':data['max_vorticity_degree'],
            'full_polynomial_residual_terms':{'temperature':len(ft.terms()),'vorticity':len(go.terms())}}

cases=[]
for beta,N,changes in [(Q(4),12,{}),(Q(9),12,{}),(Q(25,9),12,{}),
                        (Q(4),8,{j:Q(rng.randint(-3,3),23) for j in range(4,11)})]:
    label=f'b{str(beta).replace("/","_")}_N{N}'+('_harmonic' if changes else '')
    ts=time.monotonic();data=run(beta,1,N,changes)
    data['created_utc']=datetime.now(timezone.utc).isoformat()
    path=root/(label+'.json');path.write_text(json.dumps(data,indent=2)+'\n')
    # Reload decimal/rational strings from the archive; independently differentiate.
    loaded=json.loads(path.read_text());control=symbolic_check(loaded)
    if not changes:
        expected=32*(2*beta+1)*(3*beta+5)/(9*beta*beta*(beta+1)*(beta+2))
        actual={ (r['x_power'],r['y_power']):Q(r['coefficient']) for r in loaded['initial_R_Omega_degree2']}
        assert actual=={(1,1):expected},(beta,actual,expected)
        if beta==4:
            D4={(r['x_power'],r['y_power']):Q(r['coefficient']) for r in loaded['stages'][0]['correction']}
            D5={(r['x_power'],r['y_power']):Q(r['coefficient']) for r in loaded['stages'][1]['correction']}
            assert D4=={(1,3):Q(17,810)},D4
            assert D5=={(3,2):Q(157,19440),(1,4):Q(-17957,5443200)},D5
        if beta==9:
            D4={(r['x_power'],r['y_power']):Q(r['coefficient']) for r in loaded['stages'][0]['correction']}
            assert D4=={(1,3):Q(256,120285)},D4
    cases.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                  'beta':str(beta),'N':N,'harmonic_changes':bool(changes),
                  'elapsed_seconds':time.monotonic()-ts,**control})
    print(json.dumps(cases[-1]),flush=True)
# Separate symbolic rank/kernel checks and random exact right-inverse inputs.
ranks=[]
for n in range(1,15):
    dom=[x**i*y**(n+2-i) for i in range(1,n+3,2)]
    cod=[(i,n-i) for i in range(1,n+1,2)]
    mat=sp.Matrix([[sp.Poly(-sp.diff(v,x,2)-sp.diff(v,y,2),x,y).coeff_monomial(x**i*y**j)
                   for v in dom] for i,j in cod])
    hp=sum(symq(v)*x**i*y**j for (i,j),v in harmonic(n+2).items())
    assert sp.expand(sp.diff(hp,x,2)+sp.diff(hp,y,2))==0
    assert mat.rank()==len(cod) and len(dom)-mat.rank()==1
    H={key:Q(rng.randint(-9,9),31) for key in cod};D=poisson_right_inverse(H,n)
    dp=sum(symq(v)*x**i*y**j for (i,j),v in D.items())
    assert sp.expand(-sp.diff(dp,x,2)-sp.diff(dp,y,2)-sum(symq(v)*x**i*y**j for (i,j),v in H.items()))==0
    ranks.append({'n':n,'domain_dimension':len(dom),'range_dimension':len(cod),'rank':int(mat.rank())})
# Verify the triangular dependence by changing all stream degrees >=n+2 and
# subtracting the explicit diagonal Omega_n term from the full residual.
independence=[]
beta=Q(25,9);a0=Q(1);l=(beta-2)/2;m=1+3*beta/2
base,_=base_stream(beta,a0,14)
for n in range(1,10):
    psis=[base]
    change={}
    for d in range(n+2,15):
        for i in range(1,d+1,2):change[i,d-i]=Q(rng.randint(-7,7),37)
    psis.append(P.add(base,change));Ns=[]
    for psi in psis:
        th=temperature(beta,a0,psi,n+1)
        go=P.homogeneous(P.pde(beta,psi,th,n)[1],n)
        om=P.homogeneous(P.scale(P.lap(psi),-1),n)
        diag={key:(key[0]*l+key[1]*m+1)*v for key,v in om.items()}
        Ns.append(P.add(go,P.scale(diag,-1)))
    assert Ns[0]==Ns[1],n
    independence.append({'n':n,'all_higher_stream_degrees_perturbed':list(range(n+2,15)),
                         'N_n_unchanged_exactly':True})
out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED',
     'elapsed_seconds':time.monotonic()-start,'cases':cases,'rank_and_kernel_checks':ranks,
     'triangular_independence':independence,
     'code_hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
         Path(__file__).with_name('formal_center_recursion.py'),Path(__file__).with_name('exact_bivariate.py')]}}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'cases':len(cases),'rank_checks':len(ranks),'independence_checks':len(independence)},indent=2),flush=True)
