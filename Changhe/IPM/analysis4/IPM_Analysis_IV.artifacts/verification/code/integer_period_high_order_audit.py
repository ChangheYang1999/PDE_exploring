"""Finite Cartesian checks of source Q5/Q6 balls; no source convolution routines."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from functools import lru_cache
import argparse, gzip, json, pickle, sys, time, traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq as Q
from flint import arb, arb_poly, fmpq, ctx
from stream_precision_audit import unpack
from integer_period_prefix import inputs
from pure_cartesian_ball import refine_root
ROOT = Path('research/191_integer_period_high_order')
ZERO = arb(0)

def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')

def text(x):
    return x.str(45, radius=True)

def put(path, obj):
    tmp = path.with_name(path.name + '.new')
    tmp.write_text(json.dumps(obj, indent=2) + '\n')
    tmp.replace(path)

@lru_cache(None)
def ball(q):
    return arb(fmpq(str(q)))

class Laurent:
    def __init__(self, low=0, coefficients=None):
        self.low = low
        self.poly = arb_poly([] if coefficients is None else coefficients)
    def scale(self, c):
        return Laurent(self.low, self.poly * c)
    def __add__(self, other):
        low = min(self.low, other.low)
        a = arb_poly([ZERO] * (self.low-low) + self.poly.coeffs())
        b = arb_poly([ZERO] * (other.low-low) + other.poly.coeffs())
        return Laurent(low, a+b)
    def __sub__(self, other):
        return self + other.scale(-1)
    def __mul__(self, other):
        return Laurent(self.low+other.low, self.poly*other.poly)
    def derivative(self, degree, y=False):
        values = self.poly.coeffs()
        out = [ZERO] * (len(values)+2)
        for j, v in enumerate(values):
            mode = self.low+j
            out[j] += v * ball((degree+mode)/2)
            out[j+2] += v * ball((degree-mode)/2) * (-1 if y else 1)
        return Laurent(self.low-1, out)

def field(values, odd):
    degree = 2*(len(values)-1) + int(odd)
    out = [ZERO] * (2*degree+1)
    for j, value in enumerate(values):
        mode = 2*j + int(odd)
        if mode == 0:
            assert value.is_zero(), 'constant sine coordinate must be zero'
        else:
            out[degree+mode] = value/2
            out[degree-mode] = -value/2
    return Laurent(-degree, out)

def main(args):
    started = time.monotonic()
    ctx.prec = args.bits
    period = args.Q
    root_index = args.root
    base_order = 50 if period == 5 else 60
    base_topic = '180_period_five_numerical_audit' if period == 5 else '185_period_six_numerical_audit'
    tag = f'tunedQ5_r{root_index}_p1024' if period == 5 else f'tuned13_r{root_index}_p1024'
    prefix = ROOT/'verification'/f'Q{period}_root{root_index}'
    source = Path('../a4-num/ckpt')/(tag+'.pkl')
    raw = source.read_bytes()
    metadata = dict(path=str(source), sha256=sha256(raw).hexdigest(), bytes=len(raw))
    state = pickle.loads(raw)
    del raw
    assert state['ring'] == 'arb' and state['prec'] == 1024
    assert str(state['delta_exact']) == str(Q(2, period))
    assert max(state['f']) == 300 and max(state['g']) == 300
    harmonic_source = source.with_name(tag+'_H.json')
    harmonic_raw = harmonic_source.read_bytes()
    harmonics = json.loads(harmonic_raw)
    metadata['harmonic_table'] = dict(path=str(harmonic_source), sha256=sha256(harmonic_raw).hexdigest())
    assert '300' not in harmonics['H']
    assert all(str(n) in harmonics['H'] for n in range(2*period, 300, period))
    base_path = Path('research')/base_topic/'verification'/f'root{root_index}_selected.pkl.gz'
    base_raw = gzip.decompress(base_path.read_bytes())
    selected = pickle.loads(base_raw)
    assert all(state[key][n] == selected[key][n] for key in ['f','g'] for n in selected[key])
    metadata['archived_selection'] = dict(path=str(base_path), sha256=sha256(base_raw).hexdigest(), orders=sorted(selected['f']))
    del selected, base_raw
    coefficients, intervals, _, root_paths = inputs(period)
    b, interval = refine_root(coefficients, intervals[root_index-1], args.bits+64)
    f = {n:[arb(*unpack(v)) for v in state['f'][n]] for n in range(1,301)}
    g = {n:[arb(*unpack(v)) for v in state['g'][n]] for n in range(1,301)}
    del state
    assert f[1][0] == 1 and f[1][1].contains(b) and len(f[1]) == 2
    F = {n:field(f[n], True) for n in f}
    G = {n:field(g[n], False) for n in g}
    degree = lambda n: Q(1)-Q(2*n,period)
    FX = {n:F[n].derivative(degree(n)) for n in F}
    FY = {n:F[n].derivative(degree(n), True) for n in F}
    GX = {n:G[n].derivative(degree(n)+1) for n in G}
    GY = {n:G[n].derivative(degree(n)+1, True) for n in G}
    counts = dict(poisson_coefficients=0, nonlinear_coefficients=0, ordered_pairs=0, compatibility_coordinates=0, harmonic_table_overlaps=0)
    maximum_residual = ZERO
    maximum_norm_radius = ZERO
    rows = []
    for n in range(1,301):
        M = sum(map(abs, f[n]), ZERO)
        S = sum(map(abs, g[n]), ZERO)
        assert M > 0 and S > 0
        density_radius = sum((v.rad() for v in f[n]), ZERO) / sum((abs(v.mid()) for v in f[n]), ZERO)
        maximum_norm_radius = maximum_norm_radius.max(density_radius)
        if n < 300:
            stream_radius = sum((v.rad() for v in g[n]), ZERO) / sum((abs(v.mid()) for v in g[n]), ZERO)
            maximum_norm_radius = maximum_norm_radius.max(stream_radius)
        poisson = GX[n].derivative(degree(n)).scale(-1) + GY[n].derivative(degree(n), True) - FX[n]
        for j,v in enumerate(poisson.poly.coeffs()):
            assert v.contains(0), ('Poisson',n,poisson.low+j,text(v))
            counts['poisson_coefficients'] += 1
        if n % period == 0 and n >= 2*period:
            assert f[n][n//period-2].contains(0)
            counts['compatibility_coordinates'] += 1
            if n < 300:
                assert g[n][n//period-1].overlaps(arb(harmonics['H'][str(n)]['str']))
                counts['harmonic_table_overlaps'] += 1
        if n > base_order:
            nonlinear = Laurent()
            for i in range(1,n):
                nonlinear = nonlinear + GX[i]*FY[n-i] - GY[i]*FX[n-i]
                counts['ordered_pairs'] += 1
            linear_multiplier = ball(Q(2*(n-1),period-2))
            residual = nonlinear - F[n].scale(linear_multiplier)
            for j,v in enumerate(residual.poly.coeffs()):
                assert v.contains(0), ('nonlinear',n,residual.low+j,text(v))
                counts['nonlinear_coefficients'] += 1
            relative_residual = sum(map(abs,residual.poly.coeffs()), ZERO)/(linear_multiplier*M)
            maximum_residual = maximum_residual.max(relative_residual)
        if n % 25 == 0 or n == 299:
            row = dict(n=n, density_norm=text(M), density_root=text((M.log()/n).exp()), density_relative_radius=text(density_radius))
            if n < 300:
                row.update(stream_norm=text(S), stream_root=text((S.log()/n).exp()), stream_relative_radius=text(stream_radius))
            else:
                row['stream_status'] = 'untuned final harmonic; excluded'
            rows.append(row)
            progress = dict(checked_at_utc=stamp(), period=period, root_index=root_index, completed_order=n, target_order=300, counts=counts, maximum_relative_nonlinear_residual=text(maximum_residual), maximum_norm_relative_radius=text(maximum_norm_radius), norms=rows, actual_elapsed_s=time.monotonic()-started)
            put(prefix.with_name(prefix.name+'_progress.json'), progress)
            print(json.dumps({k:progress[k] for k in ['checked_at_utc','period','root_index','completed_order','actual_elapsed_s']}), flush=True)
    code_names = ['ffcore.py','tuned_cQ.py'] if period == 5 else ['ffcore.py','tuned_general.py','tuned_c3.py']
    metadata['producer_code'] = {str(Path('../a4-num/code')/name):sha256((Path('../a4-num/code')/name).read_bytes()).hexdigest() for name in code_names}
    result = {**progress, 'all_checks_pass':True, 'bits':args.bits, 'independent_prefix_order':base_order, 'root_isolating_interval':interval, 'source':metadata, 'root_inputs':{str(p):sha256(p.read_bytes()).hexdigest() for p in root_paths}, 'scope':'Finite interval consistency and source-bound norms; residual containment alone does not establish simultaneous exact solvability or an infinite radius.'}
    put(prefix.with_name(prefix.name+'_checks.json'), result)
    (ROOT/'sources'/'integer_period_high_order_audit.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(all_checks_pass=True, period=period, root_index=root_index, actual_elapsed_s=time.monotonic()-started)), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--Q', type=int, choices=[5,6], required=True)
    parser.add_argument('--root', type=int, required=True)
    parser.add_argument('--bits', type=int, default=1536)
    args = parser.parse_args()
    try:
        main(args)
    except Exception as exc:
        failure = dict(checked_at_utc=stamp(), period=args.Q, root_index=args.root, type=type(exc).__name__, error=str(exc), frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification'/f'Q{args.Q}_root{args.root}_FAILURE.json', failure)
        print(json.dumps(failure), flush=True)
        raise SystemExit(1)
