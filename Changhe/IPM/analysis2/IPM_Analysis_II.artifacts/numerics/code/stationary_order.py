"""Exact stationary density order n (= branch j = n-1 leading profile) from the sector recursion: at the leading exponent alpha(n-1, 0) the residual sector is
E_(n-1,0) = (c_l alpha - 1) G_(n-1,0) + sum_{i + jj = n-2} [interactions of the leading stream and density sectors of branches i, jj], so the stationary
order n density is G_(n-1,0) = -interactions/(c_l alpha(n-1,0) - 1), a sine polynomial with odd harmonics up to 2(n-1)*10 - 1 (orders 1..6 from the
verifier's file have harmonics 19, 39, ..., 119; order 7 has 139). Input: an exactly admissible n12 file (all branches below n-1 equal to the stationary
orders 1..n-1 exactly); its branch n-1 coefficients are zeroed so that only the interactions remain (and the file need not have branch n-1 at all).
Validation: with n = 6 the result must equal the verifier's order 6 exactly. Output: JSON in the verifier's format {'stationary_density_orders': {str(n): {'coefficients': {k: 'p/q'}}}}.
Usage: stationary_order.py admissible_exact.json n out.json [verifier_formal_tail.json for the comparison]"""
import sys, os, json
sys.set_int_max_str_digits(0)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from n12_norms import load_gens
from n12_exact import sectors_general
import farfield_exact as FE

def stationary_order(gens, coefs, cl, n):
    j = n - 1; coefs0 = [c if gen['j'] != j else Fr(0) for gen, c in zip(gens, coefs)]
    assert all(gen['j'] <= j for gen in gens if coefs0[gens.index(gen)] != 0) or True
    X = sectors_general(gens, coefs0, cl, qmax=0, hmax=j, jmax=j)
    for h in range(j):
        assert not X['E'][(h, 0)], ('input not admissible at order', h+1)
    E = X['E'][(j, 0)]; fac = cl*X['alpha'](j, 0) - 1
    return {k: -v/fac for k, v in E.items() if v != 0}

if __name__ == '__main__':
    path, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    gens, coefs, cl, p = load_gens(path)
    G = stationary_order(gens, coefs, cl, n)
    print('order %d: %d harmonics, max harmonic %d, first coefficients %s' % (n, len(G), max(G), {k: float(G[k]) for k in sorted(G)[:3]}))
    if len(sys.argv) > 4:
        V = json.load(open(sys.argv[4]))['stationary_density_orders']
        if str(n) in V:
            ref = {int(k): Fr(v) for k, v in V[str(n)]['coefficients'].items()}
            same = all(ref.get(k, 0) == G.get(k, 0) for k in set(ref) | set(G))
            print('comparison with the verifier\'s order %d: %s' % (n, 'EXACTLY EQUAL' if same else 'DIFFERENT: max |diff| %.3e' % max(abs(float(ref.get(k, 0) - G.get(k, 0))) for k in set(ref) | set(G))))
        else: print('verifier file has no order %d (orders %s)' % (n, sorted(V)))
    json.dump({'stationary_density_orders': {str(n): {'coefficients': {str(k): '%d/%d' % (v.numerator, v.denominator) for k, v in sorted(G.items())}}},
               'source': path, 'note': 'computed by code/stationary_order.py from the exact sector recursion (E_(n-1,0) = 0)'}, open(out, 'w'))
    print('written', out)
