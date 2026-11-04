"""exact_origin.py (lane numerics_agent_1): exact origin data of an exact candidate JSON: a_0 = rho_y(0) (exact rational), the center relation
(B0n) sum_i a_i chi_i,xxyy(0) = 1 - c (EXACT check), and the six R_f Taylor coefficients (center, x^2, y^2, x^4, x^2 y^2, y^4) as exact rationals.
Usage: python3 exact_origin.py cand.json [out.json]"""
import sys, os, json, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_origin as O

def exact_origin(path):
    c, gens, coefs_q, J = OPT.load_candidate_json(path)
    terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
    terms = [t for t in terms if t.get('kind') != 'series']
    OJ = O.OriginJets(terms, degmax=4, exact=True)
    coefs = [t['coef'] for t in terms]
    a0 = OJ.a0(coefs)
    strains = OJ.strains(); center = sum((s*v for s, v in zip(strains, coefs)), mpq(0))
    tay = OJ.Rf_coeffs(c, coefs)
    return {'file': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'cl_exact': X.qstr(c),
            'a0_exact': X.qstr(a0), 'a0_float': X.qfloat(a0), 'center_sum_exact': X.qstr(center), 'one_minus_c_exact': X.qstr(1-c),
            'B0n_exact': bool(center == 1-c), 'Rf_taylor_exact': [X.qstr(X.Q(v)) for v in tay], 'Rf_taylor_float': [X.qfloat(X.Q(v)) for v in tay],
            'taylor_keys': ['1', 'x^2', 'y^2', 'x^4', 'x^2y^2', 'y^4'], 'n_canonical_terms': len(terms)}

if __name__ == '__main__':
    res = exact_origin(sys.argv[1])
    print(json.dumps({k: (v if k != 'a0_exact' else v[:80]+'...') for k, v in res.items()}, indent=1))
    if len(sys.argv) > 2: json.dump(res, open(sys.argv[2], 'w'), indent=1)
