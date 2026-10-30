"""Compare direct generator algebra to exact canonical and symbolic checks."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q, ctx
from direct import ROOT,origin,sectors,origin_radial
from sectors_flint import sectors as canonical_sectors,aq
from cartesian import GeneratorJet
from moments import coefficients

BASE = ROOT/'research/generator_sector_audit'
def digest(path): return sha256(path.read_bytes()).hexdigest()

def real_candidate(name):
    start = time.monotonic()
    source = ROOT/f'research/candidate_audits/data/{name}/normalized_generators.json'
    canonical = source.with_name('canonical.json')
    data,state = json.loads(source.read_text()),json.loads(canonical.read_text())
    alpha,C,G,E,grouped,summary = sectors(data,qmax=1,hmax=7)
    old_alpha,old_C,old_G,old_E = canonical_sectors(state,qmax=1,hmax=7)
    assert C == old_C and G == old_G and E == old_E
    assert summary['all_forbidden_zero'] and summary['leading_certified_by_complete_prefix']
    o = origin(data)
    assert o['strain'] == Q(state['strain']) and o['a0'] == Q(state['a0'])
    total = sum(len(v) for x in (C,G,E) for v in x.values())
    return {'candidate':name,'source_sha256':digest(source),
            'canonical_sha256':digest(canonical),'summary':summary,
            'potential_density_residual_all_exactly_equal':True,
            'nonzero_coefficient_equalities':total,
            'origin_strain_and_a0_exactly_equal':True,
            'strain':str(o['strain']),'a0_ball':aq(o['a0']).str(60),
            'elapsed_seconds':time.monotonic()-start}

def synthetic():
    import sympy as sp
    z=sp.symbols('z'); rows=[]; qmax=3
    gens=[]
    for j,m,w,n,qd,R in [(0,0,0,3,0,Q(1,2)),(1,1,0,2,1,Q(3,2)),
                         (2,0,2,4,0,Q(10)),(1,3,1,1,2,Q(5,3)),
                         (3,2,0,0,3,Q(2)),(2,1,1,3,1,Q(4,5))]:
        c=Q(7,4);p=(3+1/c-j*(1-1/c))/2
        def s(a):return sp.Rational(str(a))
        H=R**(2*qd)*z**qd*(1+z)**s(p-m)*(1+s(R*R)*z)**(-w-qd) \
            *sp.legendre(n,(1-s(R*R)*z)/(1+s(R*R)*z))
        values=coefficients(p,m,w,n,qd,R,qmax)
        for k,value in enumerate(values):
            expected=Q(str(sp.diff(H,z,k).subs(z,0)/sp.factorial(k)))
            assert value==expected
        O=z**w*s(R)**(-2*w)*(1+z)**s(p-m)*(1+z/s(R*R))**(-w-qd) \
            *sp.legendre(n,(z-s(R*R))/(z+s(R*R)))
        for k,value in enumerate(origin_radial(p,m,['legqs',w,n,qd,str(R)],qmax)):
            expected=Q(str(sp.diff(O,z,k).subs(z,0)/sp.factorial(k)))
            assert value==expected
        gens.append({'j':j,'m':m,'spec':['legqs',w,n,qd,str(R)],'coef':str(Q(j+1,m+2))})
        rows.append({'j':j,'m':m,'w':w,'n':n,'Q':qd,'R':str(R),
                     'exact_far_field_equalities':qmax+1,'exact_origin_equalities':qmax+1})
    data={'cl':'7/4','generators':gens}
    direct=origin(data);jet=GeneratorJet(data,'0','0',order=4)
    strain=jet.chi(2,2)
    a0=-strain-jet.chi(0,4)
    assert strain.contains(aq(direct['strain'])) and a0.contains(aq(direct['a0']))
    return {'fixtures':rows,'origin_jet_strain':strain.str(60),'origin_jet_a0':a0.str(60),
            'exact_strain':str(direct['strain']),'exact_a0':str(direct['a0']),
            'both_exact_origin_values_contained':True}

if __name__=='__main__':
    start=time.monotonic();ctx.prec=1024
    result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'code_sha256':digest(Path(__file__)),
            'direct_code_sha256':digest(BASE/'code/direct.py'),
            'proof_sha256':digest(BASE/'PROOF.md'),
            'moment_code_sha256':digest(ROOT/'research/multiscale_generators/code/moments.py'),
            'cartesian_code_sha256':digest(ROOT/'research/multiscale_generators/code/cartesian.py'),
            'angular_code_sha256':digest(ROOT/'research/sector_audit/code/sectors_flint.py'),
            'real_candidates':[real_candidate(n) for n in sys.argv[1:]],
            'synthetic':synthetic(),'elapsed_seconds':time.monotonic()-start}
    dest=BASE/'verification/direct_comparisons.json';assert not dest.exists()
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('Exact checks passed',result['elapsed_seconds'],flush=True)
