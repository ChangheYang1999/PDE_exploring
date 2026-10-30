from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json, time
from flint import arb, ctx
import sympy as sp

B = Path(__file__).resolve().parents[1]
start = time.monotonic()
ctx.prec = 768

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def a(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator

manifest = json.loads((B / 'source/MANIFEST.json').read_text())
for name, row in manifest['files'].items():
    assert sha(B / 'source' / name) == row['sha256']
assert manifest['files']['NUMERICS_FINAL.md']['sha256'] == '2aba92677db6a2360b76562c29ab485d1edc1d2834f9fa6c93baedeb2d1945fb'
p = json.loads((B / 'data/parameters.json').read_text())
mu, C, b, smax, dc, q = [Q(p[k]) for k in ['mu', 'C', 'b', 's_max', 'commutator', 'q']]
Rmax = 2*a(mu)/(3*a(b)) * (a(mu)/(3*a(C))).sqrt()
unrestricted = Rmax/1024
A = (arb(1601)**a(Q(4,5))*a(q*q)+32768*a(q)+1048576).sqrt()
annular = Rmax/((1-a(dc*smax))*A)
old = json.loads((B / 'source/scalar_envelopes.json').read_text())
assert unrestricted.overlaps(arb(old['unrestricted_ceiling']))
assert annular.overlaps(arb(old['specialized_annular_ceiling']))
assert annular < a('2.839272409e-6') < unrestricted < a(p['general_ceiling'])
ratio016 = Q(p['distance016'])/Q(p['general_ceiling'])
assert Q('515.9') < ratio016 < 516
weak = json.loads((B / 'source/weak017_n23.json').read_text())
root = arb(weak['radius'])
assert root > a(p['n23_safe_floor'])
assert root < a(p['n23_printed_floor'])
assert Q(weak['strict_lower_exact']) == Q(p['n23_safe_floor'])
point_ratios = {}
for tag in ['007', '009']:
    d = json.loads((B / 'source' / ('point'+tag+'.json')).read_text())
    u = d['uniform_values']
    gu, gg = arb(u['uniform_point_upper']), arb(u['uniform_positive_gap'])
    graded_ratio = (gu+gg)/gu
    fixed = next(x for x in d['finite_boxes'] if x['framework']=='FW-T-T4L2-sharpw-v1')
    su, sg = arb(fixed['upper']), arb(fixed['gap'])
    scalar_ratio = (su+sg)/su
    assert (gu+gg).overlaps(su+sg)
    assert arb(fixed['radius']) > a(Q(1,2**14))
    if tag == '007':
        assert 4 < graded_ratio < 5 and 4 < scalar_ratio < 5
    else:
        assert 2 < graded_ratio < 3 and 3 < scalar_ratio < 4
    point_ratios[tag] = {'graded':str(graded_ratio), 'sharpw':str(scalar_ratio)}
near_ratio = Q(p['near_after'])/Q(p['near_before'])
mid_change = Q(p['mid_after'])/Q(p['mid_before'])-1
assert 38 < near_ratio < 39 and Q('0.26') < mid_change < Q('0.27')
G0 = arb(json.loads((B/'source/G0_007.json').read_text())['rows'][0]['own_upper'])
Xrecords = json.loads((B/'source/X_007.json').read_text())['instances']
Xrow = next(x for x in Xrecords if x['label']=='sharpw')
Xlower = arb(Xrow['lower_comparison']['ball'])
assert G0 < a(p['G0_upper']) and Xlower > a(p['X_lower'])
share_cap = Q(1024)*Q(p['G0_upper'])/Q(p['X_lower'])
assert share_cap < Q('0.510') and share_cap**2 < Q('0.261')
# Exact algebra, no floating trigonometry.
cc, ss, ar, br, dr = sp.symbols('cc ss ar br dr')
rot = sp.Matrix([[cc,-ss],[ss,cc]])
pol = sp.Matrix([[ar,br],[br,dr]])
cart = rot*pol*rot.T
assert sp.expand(sum(x*x for x in cart)-(cc*cc+ss*ss)**2*(ar*ar+2*br*br+dr*dr)) == 0
v = sp.Matrix([ar,br]); cv = rot*v
assert sp.expand(sum(x*x for x in cv)-(cc*cc+ss*ss)*(ar*ar+br*br)) == 0
M, N = p['M'], p['N']; dmax = 4*M+3
full_N = 2*M+2; component_N = 2*M+3
indices = set()
for i in range(1,dmax+1,2):
    for j in range(1,dmax+1,2):
        indices.add((i+j)//2)
        indices.add(abs(i-j)//2)
assert max(indices)==dmax and dmax < 2*full_N
assert dmax+2 < 2*component_N and dmax+2 < 2*N
out = {
    'utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':time.monotonic()-start,
    'precision_bits':ctx.prec,
    'inputs':{str(x):sha(x) for x in [B/'PROOF.md',Path(__file__),B/'data/parameters.json',B/'source/MANIFEST.json']},
    'all_frozen_hashes_verified':True,
    'unrestricted_ceiling':str(unrestricted),'specialized_annular_ceiling':str(annular),
    'conservative_016_ratio_exact':str(ratio016),
    'n23_root':str(root),'printed_floor_above_root':True,'safe_floor_below_root':True,
    'point_ratios':point_ratios,
    'reported_near_ratio_exact':str(near_ratio),'reported_mid_relative_increase_exact':str(mid_change),
    'G0_share_upper_exact':str(share_cap),'G0_squared_share_upper_exact':str(share_cap**2),
    'hessian_and_gradient_orthogonal_invariance':True,
    'full_tensor_min_sufficient_N':full_N,'individual_component_min_sufficient_N':component_N,
    'actual_N':N,'cosine_indices_checked':len(indices),'all_checks_pass':True,
    'scope':'Arithmetic and inference audit. Accepted integrals imported, not rerun. No FLOAT continuum certification or existence closure.'}
with (B/'verification/result.json').open('x') as f:
    json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='inputs'},indent=2))
