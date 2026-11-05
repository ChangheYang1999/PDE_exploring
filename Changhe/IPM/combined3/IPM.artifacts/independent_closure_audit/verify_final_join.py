#!/usr/bin/env python3
"""Independent full scalar join from raw source energies and displayed formulas.

Does not import the main consumer or the nonlinear scalar producer. Writes
only in this audit directory, and remains pending until all premises exist.
"""
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ART = HERE.parent
ctx.prec = 512

def read(path):
    return json.loads(path.read_text())

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def aa(value):
    value = F(value)
    return arb(value.numerator)/arb(value.denominator)

def upper(value):
    value = arb(value)
    assert value.is_finite()
    return value.abs_upper()

def bindings(mapping):
    assert mapping
    for name, expected in mapping.items():
        assert digest(ART/name) == expected, name

PATHS = {
    'source':ART/'finite_rank/Q_source_certificate_v01/result.json',
    'matrix':HERE/'matrix_prefix_audit.json',
    'local':HERE/'local_coefficients_audit.json',
    'consumer':ART/'operator_theory/fixed_parameter_closure_v01.json',
    'forcing':ART/'source_Q_from_integer_tensors.json',
    'structure':ART/'operator_theory/structure013_result.json',
    'envelope':ART/'source_envelopes_v01/result.json',
    'far_source':ART/'Q_far_source_highpass_result.json',
    'L2':ART/'coercivity_residual/L2_signed_far_v05/result.json',
}
STATUS = {
    'source':'CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS',
    'matrix':'INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS',
    'local':'INDEPENDENT_LOCAL_COEFFICIENT_AUDIT_PASS',
    'consumer':'FINAL_NUMERICAL_CLOSURE_PASS',
    'forcing':'CERTIFIED_Q_SOURCE_FROM_INTEGER_TENSORS',
    'structure':'EXACT_STRUCTURE_CHECK_PASS',
    'envelope':'CERTIFIED_RADIAL_NEAR_SOURCE_ENVELOPES',
    'far_source':'CERTIFIED_ACTUAL_FAR_Q_SOURCE_LOW_HIGH_BOUNDS',
    'L2':'CERTIFIED_DIRECT_L2',
}

def main():
    out = {'finished_utc':datetime.now(timezone.utc).isoformat(),
           'auditor_code_sha256':digest(Path(__file__))}
    pending = {key:('MISSING' if not path.exists() else read(path)['status'])
               for key,path in PATHS.items()
               if not path.exists() or read(path)['status'] != STATUS[key]}
    if pending:
        out.update(status='INDEPENDENT_FINAL_JOIN_PENDING', pending_inputs=pending,
                   stationary_existence='NOT CLAIMED')
        (HERE/'final_join_audit.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out,indent=2))
        return
    data = {key:read(path) for key,path in PATHS.items()}
    for key in ['matrix','local']:
        bindings(data[key]['bindings'])
    bindings(data['local']['nested_bindings'])
    for name, expected in data['local']['used_chunk_sha256'].items():
        assert digest(ART/name) == expected
    assert data['consumer']['all_input_bindings_and_covers_checked'] is True
    assert digest(ART/'operator_theory/assemble_fixed_parameter_closure_v01.py') == data['consumer']['consumer_sha256']
    src = data['source']
    cfg = src['configuration']
    bindings(cfg['code_hashes'])
    assert read(PATHS['source'].parent/'configuration.json') == cfg
    ratio, rmin, rmax = map(F,[cfg['ratio'],cfg['rmin'],cfg['rmax']])
    N = cfg['panels']
    assert rmin > 0 and ratio > 1 and rmin*ratio**(N-1) < rmax <= rmin*ratio**N
    rows, chunks = {}, {}
    for path in sorted(PATHS['source'].parent.glob('chunk_*.json')):
        chunk = read(path)
        assert chunk['configuration'] == cfg
        chunks[str(path.relative_to(ART))] = digest(path)
        for row in chunk['rows']:
            i = row['index']
            assert 0 <= i < N
            if i in rows:
                assert rows[i] == row
            rows[i] = row
    assert sorted(rows) == list(range(N))
    core = [sum((upper(rows[i]['energy_upper'][str(j)]) for i in range(N)),arb(0))
            for j in range(6)]
    total = [core[j]+upper(src['tail_energies']['origin'][j])+upper(src['tail_energies']['exterior'][j])
             for j in range(6)]
    assert all(x > 0 and x.is_finite() for x in total)
    Db = {j+1:max(total[j].sqrt().abs_upper(),upper(src['D_b_L2_upper'][str(j+1)]))
          for j in range(4)}
    Dxb = {2:max((total[4]+4*total[0]).sqrt().abs_upper(),upper(src['D_xb_L2_upper']['2'])),
           4:max((total[5]+16*total[2]).sqrt().abs_upper(),upper(src['D_xb_L2_upper']['4']))}
    H1 = max([upper(src['H1_upper']),upper(src['tail_energies']['origin_H1_bound']),
              upper(src['tail_energies']['exterior_H1_bound'])]+
             [upper(rows[i]['H1_upper']) for i in range(N)])
    def moment(D,m,sigma):
        sigma = aa(sigma)
        C = 1/(2*(arb.pi()*sigma/2).cos().sqrt()
               *(1-sigma)**((1-sigma)/4)*(1+sigma)**((1+sigma)/4))
        return C*D[m]**((1-sigma)/2)*D[m+2]**((1+sigma)/2)
    def source_A(sigma):
        return moment(Db,2,sigma)+2*moment(Dxb,2,sigma)+4*moment(Db,1,sigma)
    A2 = max(source_A(0).abs_upper(),upper(src['A_s_upper']['2']))
    Aq = max(source_A(F(1,10)).abs_upper(),upper(src['A_s_upper']['21/10']))
    c, q, delta = aa('4076476460239181/2251799813685248'), aa('21/10'), aa('1/10')
    R, beta2, f2, n, beta = map(aa,['381377/1000000000000','2087491/1000000',
                                  '7961207/10000000000000','759/100000','7/10'])
    assert R*beta2 > f2 and arb(data['L2']['beta_L2_lower']) > beta2
    selected = data['consumer']['selected']
    M = aa(selected['M'])
    rb = selected['source_split_radius']
    assert 0 < M <= aa('1/2')
    r = R/M
    K1 = upper(data['local']['reconstructed_K1'])
    K0 = upper(data['local']['reconstructed_K0'])
    Wu2 = upper(data['local']['reconstructed_Wu2'])
    env = next(row for row in data['envelope']['rows'] if row['cut_R'] == rb)
    far = next(row for row in data['far_source']['rows'] if row['R'] == rb)
    Bnear = (upper(env['a0'])**2+4*upper(env['a1'])**2).sqrt()
    Bfar = upper(far['B'])
    e_far = 3*Bfar*Bfar/(4*(c+1-beta))
    M2u = (Db[1]*Db[3]).sqrt()/2
    M3u = (Db[2]*Db[4]).sqrt()/2
    M3xu = ((Dxb[2]+(arb(2).sqrt()+1)*Db[1])
             *(Dxb[4]+(arb(2).sqrt()+1)*Db[3])).sqrt()/2
    R3 = aa('51/1000')*(M3u+2*M3xu+6*M2u)
    cq = q*(q-1)/2
    terms = [
        ('local_gradient',K1,F(20,21)),
        ('local_scalar',K0,F(40,21)),
        ('lower_source_near',Bnear,F(20,21)),
        ('transport_second',q*delta*Wu2/2,F(10,21)),
        ('transport_third',R3,F(11,21)),
        ('source_principal',q*H1,F(10,21)),
        ('source_second',cq*A2,F(20,21)),
        ('source_fractional',cq*Aq,F(1)),
    ]
    rates = {name:coefficient*r**aa(power) for name,coefficient,power in terms}
    e_bg = e_far+sum(rates.values(),arb(0))
    # Independently evaluate the nonlinear formula, with no producer import.
    def Bp(p):
        s = (p+1)/q
        return (4*q*(arb.pi()*s).sin()).rsqrt()*(1-s)**(-(1-s)/2)*s**(-s/2)
    B0,B1 = Bp(0),Bp(1)
    Cs,Ca = B1/4,B0/arb(2).sqrt()
    S1 = 5/(11*arb.pi()).sqrt()
    theta = (q-2)/q
    z = q*r**(1/q)
    v = Ca*M*r**(1-1/q)
    L0 = q*Cs*R**theta*M**(1-theta)+aa('53/100')*S1*M
    Cc = q*arb(2)**(q-2)*(B1*R**theta*M**(1-theta)+S1*M)
    P = arb(2)**(q-1)*(Ca+B0)*M*r**(1-1/q)
    T = q*arb(2)**(q-2)*(Ca+B1)*M*r**(1-1/q)
    NL = L0*(1+2*z)**2+4*Cc*(aa('1/2')+z)*z+2*(q*v+P+T)
    b = beta-e_bg-NL
    margin = b*M*M-n*M
    contraction = S1*M/beta2
    assert b > 0 and margin > 0 and contraction < 1
    assert (e_bg-arb(selected['background_loss'])).abs_upper() < arb('1e-50')
    assert (NL-arb(selected['nonlinear_loss'])).abs_upper() < arb('1e-50')
    assert (margin-arb(selected['selfmap_energy_margin'])).abs_upper() < arb('1e-50')
    eps = e_far+sum(((1-aa(power)/2)*rates[name] for name,coefficient,power in terms),arb(0))
    weak = sum((aa(power)/2*rates[name]/(r*r) for name,coefficient,power in terms),arb(0))
    tangent = data['consumer']['global_background_tangent']
    er, cr = aa(tangent['rounded_epsilon_upper']),aa(tangent['rounded_weak_C_upper'])
    assert er > eps and cr > weak
    rounded_margin = (beta-er-NL)*M*M-n*M-cr*R*R
    assert rounded_margin > 0
    Ldelta = delta*arb.pi().sqrt()*((1-delta)/2).gamma()/(2*(1-delta/2).gamma())
    inherited_N = M*(1+2*Ldelta*r**aa(F(1,21))+4*r**aa(F(10,21))
                       +8*Ldelta*r**aa(F(11,21))+8*r**aa(F(20,21))+10*Ldelta*r)
    assert inherited_N < aa('387/1000')
    slope = arb(data['structure']['rho_star_origin_slope_arb'])-S1*M
    assert slope > 0
    out.update(status='INDEPENDENT_FINAL_SCALAR_JOIN_PASS',
               input_sha256={key:digest(path) for key,path in PATHS.items()},
               source_raw_chunk_sha256=chunks,source_panels=N,
               source_Db={str(j):v.str(80) for j,v in Db.items()},
               source_Dxb={str(j):v.str(80) for j,v in Dxb.items()},
               source_H1=H1.str(80),source_A2=A2.str(80),source_Aq=Aq.str(80),
               R='381377/1000000000000',M=selected['M'],source_split_radius=rb,
               rates={name:value.str(80) for name,value in rates.items()},far_rate=e_far.str(80),
               background_loss=e_bg.str(80),nonlinear_loss=NL.str(80),
               exterior_decay=b.str(80),selfmap_energy_margin=margin.str(80),
               contraction_ratio=contraction.str(80),rounded_global_margin=rounded_margin.str(80),
               inherited_N_upper=inherited_N.str(80),origin_slope_lower=slope.str(80),
               comparison_with_main='Independently reconstructed scalar values agree to1e-50; all independent inequalities are strict in512-bit Arb.',
               scope='Independent arithmetic confirmation of the actual chosen closure. The separately reviewed analytic implication and all source certificate proofs are essential to a stationary theorem.')
    (HERE/'final_join_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_raw_chunk_sha256','input_sha256']},indent=2))

if __name__ == '__main__':
    main()
