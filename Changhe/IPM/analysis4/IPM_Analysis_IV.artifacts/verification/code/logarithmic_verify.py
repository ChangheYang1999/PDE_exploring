"""Independent exact Cartesian verification of polynomial logarithmic channels.

All computations stay finite. Agreement at these orders is not evidence for
convergence of an infinite logarithmic expansion. Run from the lane directory.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json

import cartesian_verify as cv
from cartesian_verify import C, I, Q, qs, Field, sin_field, cos_field


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[k] if k < len(a) else C()) +
                 (b[k] if k < len(b) else C()) for k in range(n)])


def pscale(a, value):
    return trim([x*value for x in a])


def pder(a):
    return trim([a[k]*k for k in range(1, len(a))])


def pintegrate(a):
    return trim([C()] + [a[k]/(k+1) for k in range(len(a))])


def inv_linear(a, value):
    """Solve (D+value)y=a, choosing zero integration constant if value=0."""
    if not value:
        return pintegrate(a)
    ans, term = [], list(a)
    value = Q(value)
    while term:
        ans = padd(ans, pscale(term, 1/value))
        term = pscale(pder(term), -1/value)
    return ans


@dataclass
class LogField:
    """r**q sum_t (log r)**t sum_k terms[t][k] exp(i*k*theta)."""
    q: object
    terms: dict

    def __post_init__(self):
        self.q = Q(self.q)
        self.terms = {t: cv.clean(v) for t, v in self.terms.items() if cv.clean(v)}

    @staticmethod
    def pure(field):
        return LogField(field.q, {0: field.modes})

    def scale(self, a):
        return LogField(self.q, {t: {k: v*a for k, v in d.items()}
                                  for t, d in self.terms.items()})

    def __add__(self, other):
        assert self.q == other.q
        out = {t: dict(v) for t, v in self.terms.items()}
        for t, values in other.terms.items():
            dest = out.setdefault(t, {})
            for k, v in values.items():
                cv.put(dest, k, v)
        return LogField(self.q, out)

    def __sub__(self, other):
        return self + other.scale(-1)

    def __mul__(self, other):
        out = {}
        for t, values in self.terms.items():
            for s, rhs in other.terms.items():
                dest = out.setdefault(t+s, {})
                for k, v in values.items():
                    for l, w in rhs.items():
                        cv.put(dest, k+l, v*w)
        return LogField(self.q+other.q, out)

    def diff(self, axis):
        ans = LogField(self.q-1, {})
        for t, values in self.terms.items():
            f = Field(self.q, values)
            h = f.dx() if axis == 'x' else f.dy()
            ans = ans + LogField(self.q-1, {t: h.modes})
            if t:
                trig = cos_field(-1, {1: Q(t)}) if axis == 'x' else sin_field(-1, {1: Q(t)})
                ans = ans + LogField(self.q-1, {t-1: (f*trig).modes})
        return ans

    def dx(self):
        return self.diff('x')

    def dy(self):
        return self.diff('y')

    def dt(self):
        return LogField(self.q, {t-1: {k: v*t for k, v in d.items()}
                                 for t, d in self.terms.items() if t})

    def euler(self):
        return self.scale(self.q) + self.dt()

    def laplace(self):
        return self.dx().dx()+self.dy().dy()

    def zero(self):
        return not self.terms

    def degree(self):
        return max(self.terms, default=-1)

    def mode_polynomials(self):
        n = self.degree()+1
        modes = set().union(*(d.keys() for d in self.terms.values())) if self.terms else set()
        return {k: trim([self.terms.get(t, {}).get(k, C()) for t in range(n)]) for k in modes}

    @staticmethod
    def from_modes(q, modes):
        out = {}
        for k, poly in modes.items():
            for t, v in enumerate(poly):
                if v:
                    out.setdefault(t, {})[k] = v
        return LogField(q, out)

    def amplitudes(self, kind):
        result = {}
        for t, d in sorted(self.terms.items()):
            f = Field(self.q, d)
            a = f.sine() if kind == 'sine' else f.cosine()
            result[str(t)] = {str(k): qs(v) for k, v in a.items()}
        return result


def poisson(rho):
    rhs = rho.dx()
    P = rho.q+1
    result, resonant = {}, []
    for k, h in rhs.mode_polynomials().items():
        # k^2-(P+D)^2 = -(D+P-k)(D+P+k).
        b = inv_linear(pscale(h, -1), P-k)
        b = inv_linear(b, P+k)
        if k*k == P*P:
            # The chosen harmonic convention is b(0)=0.
            b[0] = C()
            b = trim(b)
            if k > 0:
                resonant.append(k)
        result[k] = b
    psi = LogField.from_modes(P, result)
    assert (psi.laplace().scale(-1)-rhs).zero()
    return psi, sorted(resonant)


def from_potential(chi):
    rho = chi.laplace().dy().scale(-1)
    psi = chi.dx().dy()
    ux = chi.dx().dy().dy().scale(-1)
    uy = chi.dx().dx().dy()
    assert (ux+psi.dy()).zero()
    assert (uy-psi.dx()).zero()
    return rho, psi, ux, uy


def reconstruct(rho, psi):
    s = rho.q+3
    remainder = rho
    answer = LogField(s, {})
    top = max((abs(k) for d in rho.terms.values() for k in d), default=1)
    for l in range(top-1, -1, -2):
        # Obtain the real sine-amplitude polynomial of the top density mode.
        amplitude = []
        for t in range(remainder.degree()+1):
            f = Field(rho.q, remainder.terms.get(t, {})).sine()
            amplitude.append(C(f.get(l+1, Q(0))))
        amplitude = trim(amplitude)
        if not amplitude:
            continue
        if l:
            poly = pscale(amplitude, -2)
            factors = (s-l, s+l, s-2-l)
        else:
            poly = pscale(amplitude, -1)
            factors = (s, s, s-2)
        for v in factors:
            poly = inv_linear(poly, v)
        basis = LogField(s, {
            t: cos_field(s, {l: a.re}).modes for t, a in enumerate(poly) if a
        })
        assert all(not a.im for a in poly)
        answer = answer+basis
        image = from_potential(basis)[0]
        remainder = remainder-image
        assert all(abs(k) < l+1 for d in remainder.terms.values() for k in d)
    assert remainder.zero()
    rr, pp, ux, uy = from_potential(answer)
    assert (rr-rho).zero()
    difference = psi-pp
    if not difference.zero():
        assert difference.degree() == 0
        amplitudes = Field(psi.q, difference.terms[0]).sine()
        assert len(amplitudes) == 1
        k, h = next(iter(amplitudes.items()))
        assert psi.q == -k and k >= 2 and k % 2 == 0
        if k == 2:
            correction = LogField(s, {1: cos_field(s, {0: -h}).modes})
        else:
            correction = LogField.pure(cos_field(s, {k-2: h/((k-2)*(k-1))}))
        answer = answer+correction
    rr, pp, ux, uy = from_potential(answer)
    assert (rr-rho).zero() and (pp-psi).zero()
    return answer, ux, uy


def solve_dilation(source, c, n):
    a = (n-1)*(c-1)
    out = {}
    for k, poly in source.mode_polynomials().items():
        # (a-cD) f = source.
        out[k] = inv_linear(pscale(poly, -1/c), -a/c)
    f = LogField.from_modes(source.q, out)
    assert (f.scale(a)-f.dt().scale(c)-source).zero()
    return f


def run(c, initial, N):
    c = Q(c)
    delta = 1-1/c
    rho, psi, chi, velocities = {}, {}, {}, {}
    rows = []
    for n in range(1, N+1):
        p = 1-n*delta
        if n == 1:
            f = LogField.pure(sin_field(p, initial))
            source = LogField(p, {})
        else:
            source = LogField(p, {})
            for i in range(1, n):
                j = n-i
                ux, uy = velocities[i]
                source = source+ux*rho[j].dx()+uy*rho[j].dy()
            f = solve_dilation(source, c, n)
        g, resonance_modes = poisson(f)
        pot, ux, uy = reconstruct(f, g)
        # The equation is verified using the same original potential derivatives.
        residual = f.euler().scale(c)-f+source
        assert residual.zero()
        rho[n], psi[n], chi[n], velocities[n] = f, g, pot, (ux, uy)
        assert f.degree() <= max(0, n-2)
        assert g.degree() <= n-1
        rows.append({
            'n': n, 'p': qs(p), 'density_log_degree': f.degree(),
            'stream_log_degree': g.degree(), 'potential_log_degree': pot.degree(),
            'resonant_stream_modes_with_nonzero_forcing': resonance_modes,
            'density': f.amplitudes('sine'), 'stream': g.amplitudes('sine'),
            'potential': pot.amplitudes('cosine'),
            'original_potential_identities_exact': True,
            'stationary_coefficient_exactly_zero': True,
        })
        print(json.dumps({'c': qs(c), 'n': n, 'f_log': f.degree(),
                          'g_log': g.degree(), 'chi_log': pot.degree()}), flush=True)
    return {'c': qs(c), 'delta': qs(delta), 'orders': N,
            'initial': {str(k): qs(v) for k, v in initial.items()},
            'free_resonant_stream_constant': 'b_j(0)=0', 'rows': rows}


def main():
    cases = [run(Q(9)/5, {1: Q(1)}, 10),
             run(Q(2), {1: Q(1)}, 9),
             run(Q(5)/3, {1: Q(1), 3: Q(1)}, 11)]
    pure = json.loads(Path('research/01_recurrence/verification/single_mode_c9_5_N8.json').read_text())['recursion']
    for row, original in zip(cases[0]['rows'], pure['rows']):
        for field in ('density', 'stream', 'potential'):
            assert row[field] == {'0': original[field]}
    obstructions = json.loads(Path('research/03_resonances/verification/exact_probes.json').read_text())
    for case, name, n in [(cases[0], 'c9_5_sin1', 9), (cases[1], 'c2_sin1', 8)]:
        h = Q(obstructions[name]['poisson_forcing_at_resonance'])
        log_coefficient = Q(case['rows'][n-1]['stream']['1']['2'])
        assert log_coefficient == h/4
    out = {
        'checked_at_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'cartesian_engine_sha256': sha256(Path(cv.__file__).read_bytes()).hexdigest(),
        'scope': 'Finite exact formal identities through and beyond the first resonances; no convergence claim.',
        'cases': cases,
        'pure_c9_5_orders_1_through_8_identical': True,
        'first_resonant_log_coefficients_equal_h_over_4': True,
    }
    target = Path('research/10_logarithmic_channels/verification/cartesian_log_checks.json')
    target.write_text(json.dumps(out, indent=2)+'\n')
    print('All polynomial-log Cartesian identities and pure-prefix comparisons pass.', flush=True)


if __name__ == '__main__':
    main()
