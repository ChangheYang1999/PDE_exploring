"""Independent exact homogeneous Cartesian calculus for the IPM far field.

No source-project or other-lane module is imported. Fields are Laurent Fourier
polynomials with exact Gaussian-rational coefficients. Cartesian derivatives,
not the angular advection formula, build every nonlinear coefficient.

Run from the lane directory with the supplied Python, CPU affinity and low
priority. All output paths and recorded input paths are relative.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from typing import Mapping

from gmpy2 import mpq


def Q(x=0):
    return x if isinstance(x, mpq) else mpq(x)


def qs(x):
    x = Q(x)
    return f"{x.numerator}/{x.denominator}"


@dataclass(frozen=True)
class C:
    re: mpq = Q(0)
    im: mpq = Q(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, C) else C(Q(x), Q(0))

    def __add__(self, other):
        z = C.of(other)
        return C(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-C.of(other))

    def __rsub__(self, other):
        return C.of(other) + (-self)

    def __mul__(self, other):
        z = C.of(other)
        return C(self.re*z.re - self.im*z.im,
                 self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def __truediv__(self, real):
        real = Q(real)
        return C(self.re/real, self.im/real)

    def __bool__(self):
        return bool(self.re or self.im)


I = C(Q(0), Q(1))


def clean(d):
    return {k: C.of(v) for k, v in d.items() if v}


def put(d, k, v):
    value = d.get(k, C()) + v
    if value:
        d[k] = value
    else:
        d.pop(k, None)


@dataclass
class Field:
    """r**q times a finite sum modes[k]*exp(i*k*theta)."""
    q: mpq
    modes: dict[int, C]

    def __post_init__(self):
        self.q = Q(self.q)
        self.modes = clean(self.modes)

    def scale(self, a):
        return Field(self.q, {k: v*a for k, v in self.modes.items()})

    def __add__(self, other):
        assert self.q == other.q, (qs(self.q), qs(other.q))
        d = dict(self.modes)
        for k, v in other.modes.items():
            put(d, k, v)
        return Field(self.q, d)

    def __sub__(self, other):
        return self + other.scale(-1)

    def __mul__(self, other):
        d = {}
        for k, v in self.modes.items():
            for l, w in other.modes.items():
                put(d, k+l, v*w)
        return Field(self.q+other.q, d)

    def dx(self):
        d = {}
        for k, v in self.modes.items():
            put(d, k+1, v*((self.q-k)/2))
            put(d, k-1, v*((self.q+k)/2))
        return Field(self.q-1, d)

    def dy(self):
        d = {}
        for k, v in self.modes.items():
            put(d, k+1, I*v*((k-self.q)/2))
            put(d, k-1, I*v*((self.q+k)/2))
        return Field(self.q-1, d)

    def laplace(self):
        # Deliberately use Cartesian derivatives, not a diagonal multiplier.
        return self.dx().dx() + self.dy().dy()

    def sine(self):
        result = {}
        assert not self.modes.get(0, C()), self.modes.get(0)
        for k in sorted(k for k in self.modes if k > 0):
            v = self.modes[k]
            assert v.re == 0, (k, v)
            assert self.modes.get(-k, C()) == -v, (k, v)
            if v.im:
                result[k] = -2*v.im
        assert len(self.modes) == 2*len(result)
        return result

    def cosine(self):
        result = {}
        for k in sorted(k for k in self.modes if k >= 0):
            v = self.modes[k]
            assert v.im == 0
            if k:
                assert self.modes.get(-k, C()) == v
                result[k] = 2*v.re
            else:
                result[0] = v.re
        assert len(self.modes) == 2*len(result) - (0 in result)
        return result

    def zero(self):
        return not self.modes


def sin_field(q, coeffs: Mapping[int, mpq]):
    d = {}
    for k, a in coeffs.items():
        a = Q(a)
        assert k > 0
        if a:
            d[k], d[-k] = -I*(a/2), I*(a/2)
    return Field(Q(q), d)


def cos_field(q, coeffs: Mapping[int, mpq]):
    d = {}
    for k, a in coeffs.items():
        a = Q(a)
        assert k >= 0
        if a:
            if k == 0:
                d[0] = C(a)
            else:
                d[k] = d[-k] = C(a/2)
    return Field(Q(q), d)


class Resonance(ValueError):
    pass


def poisson(rho: Field):
    rhs = rho.dx()
    stream_exponent = rho.q+1
    result = {}
    for k, h in rhs.modes.items():
        denominator = k*k-stream_exponent*stream_exponent
        if denominator == 0:
            raise Resonance(f"active Poisson resonance q={qs(rho.q)}, mode={k}")
        result[k] = h/denominator
    psi = Field(stream_exponent, result)
    assert (psi.laplace().scale(-1)-rhs).zero()
    return psi


def from_potential(chi: Field):
    rho = chi.laplace().dy().scale(-1)
    psi = chi.dx().dy()
    # Direct third derivatives of chi, retaining the original formulation.
    ux = chi.dx().dy().dy().scale(-1)
    uy = chi.dx().dx().dy()
    assert (psi.dy().scale(-1)-ux).zero()
    assert (psi.dx()-uy).zero()
    return rho, psi, ux, uy


def reconstruct_potential(rho: Field):
    remaining = dict(rho.sine())
    coefficients = {}
    max_mode = max(remaining, default=1)
    assert max_mode % 2 == 1
    for l in range(max_mode-1, -1, -2):
        image = from_potential(cos_field(rho.q+3, {l: Q(1)}))[0].sine()
        diagonal = image.get(l+1, Q(0))
        if diagonal == 0:
            raise Resonance(f"singular pure potential q={qs(rho.q)}, column={l}")
        a = remaining.get(l+1, Q(0))/diagonal
        if a:
            coefficients[l] = a
        for k, v in image.items():
            remaining[k] = remaining.get(k, Q(0))-a*v
            if remaining[k] == 0:
                del remaining[k]
    assert not remaining, remaining
    chi = cos_field(rho.q+3, coefficients)
    rr, pp, ux, uy = from_potential(chi)
    assert (rr-rho).zero()
    return chi, pp, ux, uy


def displayed_poisson(rho: Field):
    a = rho.sine()
    p = rho.q
    b = {}
    for k in range(2, max(a, default=-1)+2, 2):
        h = ((p-k+1)*a.get(k-1, Q(0)) +
             (p+k+1)*a.get(k+1, Q(0)))/2
        den = k*k-(p+1)**2
        if den == 0:
            if h:
                raise Resonance("active displayed Poisson resonance")
            continue
        if h:
            b[k] = h/den
    return sin_field(p+1, b)


def recurrence(c, initial, order, require_potential=True):
    c = Q(c)
    delta = 1-1/c
    rho, psi, chi, velocity = {}, {}, {}, {}
    records = []
    for n in range(1, order+1):
        p = 1-n*delta
        forcing = Field(p, {})
        if n == 1:
            current = sin_field(p, initial)
        else:
            for i in range(1, n):
                j = n-i
                ux, uy = velocity[i]
                forcing = forcing + ux*rho[j].dx() + uy*rho[j].dy()
            current = forcing.scale(1/((n-1)*(c-1)))
        rho[n] = current
        psi[n] = poisson(current)
        assert (psi[n]-displayed_poisson(current)).zero()
        if require_potential:
            cc, pp, ux, uy = reconstruct_potential(current)
            assert (pp-psi[n]).zero()
            chi[n] = cc
        else:
            ux, uy = psi[n].dy().scale(-1), psi[n].dx()
        velocity[n] = ux, uy
        residual = current.scale(c*p-1)+forcing
        assert residual.zero()
        row = {"n": n, "p": qs(p),
               "density": {str(k): qs(v) for k, v in current.sine().items()},
               "stream": {str(k): qs(v) for k, v in psi[n].sine().items()},
               "poisson_exact": True, "stationary_residual_exact_zero": True,
               "direct_potential_verified": require_potential}
        if n in chi:
            row["potential"] = {str(k): qs(v) for k, v in chi[n].cosine().items()}
        records.append(row)
        print(json.dumps({"n": n, "density_degree": max(current.sine(), default=0),
                          "terms": len(current.sine()), "verified": True}), flush=True)
    return {"c": qs(c), "gamma": qs(1/c), "delta": qs(delta), "rows": records}


def extract_candidate(path):
    path = Path(path)
    raw = path.read_bytes()
    data = json.loads(raw)
    manifest_path = path.parent/'MANIFEST.json'
    manifest = json.loads(manifest_path.read_text())
    digest = sha256(raw).hexdigest()
    expected = next(row['sha256'] for row in manifest['coefficient_files']
                    if row['name'] == path.name)
    assert digest == expected
    c = Q(data['cl_exact'])
    assert c == Q(manifest['c_l_exact'])
    coefficients = {}
    count = 0
    for row in data['generators']:
        if row['j'] != 0:
            continue
        # At t=1, t**h and t**w P_n(2t-1) both equal one.
        assert row['spec'][0] in ('mono', 'leg'), row['spec']
        m = 2*int(row['m'])
        coefficients[m] = coefficients.get(m, Q(0))+Q(row['coef'])
        count += 1
    coefficients = {k: v for k, v in coefficients.items() if v}
    chi = cos_field(3+1/c, coefficients)
    rho, psi, ux, uy = from_potential(chi)
    assert (psi-poisson(rho)).zero()
    sector_path = path.parent/'sector_table.json'
    sector_digest = sha256(sector_path.read_bytes()).hexdigest()
    assert sector_digest == manifest['sector_table']['sha256']
    return {"input": path.as_posix(), "input_sha256": digest,
            "manifest": manifest_path.as_posix(),
            "manifest_sha256": sha256(manifest_path.read_bytes()).hexdigest(),
            "sector_table_sha256": sector_digest,
            "c": qs(c), "gamma": qs(1/c), "delta": qs(1-1/c),
            "branch_zero_generators": count,
            "potential": {str(k): qs(v) for k, v in chi.cosine().items()},
            "density": {str(k): qs(v) for k, v in rho.sine().items()},
            "stream": {str(k): qs(v) for k, v in psi.sine().items()},
            "status": "exact extraction; not an exact stationary solution claim"}


def self_checks():
    x = cos_field(1, {1: Q(1)})
    y = sin_field(1, {1: Q(1)})
    one = cos_field(0, {0: Q(1)})
    assert (x.dx()-one).zero() and x.dy().zero()
    assert (y.dy()-one).zero() and y.dx().zero()
    assert (x*x+y*y-cos_field(2, {0: Q(1)})).zero()
    count = 0
    for s in (Q('17/5'), Q('7/3'), Q('-11/7'), Q('-25/9')):
        for l in range(0, 20, 2):
            f = cos_field(s, {l: Q('7/13')})
            assert (f.dx().dy()-f.dy().dx()).zero()
            # Independent diagonal polar Laplacian check.
            assert (f.laplace()-cos_field(s-2, {l: Q('7/13')*(s*s-l*l)})).zero()
            rho, psi, ux, uy = from_potential(f)
            assert (psi.laplace().scale(-1)-rho.dx()).zero()
            assert (ux.dx()+uy.dy()).zero()
            assert (poisson(rho)-psi).zero()
            cc, pp, vx, vy = reconstruct_potential(rho)
            assert (cc-f).zero()
            count += 1
    return {"cartesian_basis_cases": count, "all_exact": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate')
    parser.add_argument('--out', required=True)
    parser.add_argument('--order', type=int, default=5)
    parser.add_argument('--c', default='9/5')
    parser.add_argument('--initial', default='1:1')
    parser.add_argument('--stream-only', action='store_true')
    args = parser.parse_args()
    result = {"date_utc": datetime.now(timezone.utc).isoformat(),
              "implementation": "exact Cartesian homogeneous differentiation",
              "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "self_checks": self_checks()}
    if args.candidate:
        extracted = extract_candidate(args.candidate)
        result['extraction'] = extracted
        c = extracted['c']
        initial = {int(k): Q(v) for k, v in extracted['density'].items()}
    else:
        c = args.c
        initial = {int(k): Q(v) for term in args.initial.split(',')
                   for k, v in [term.split(':')]}
    result['recursion'] = recurrence(c, initial, args.order,
                                    require_potential=not args.stream_only)
    result['completed_utc'] = datetime.now(timezone.utc).isoformat()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': out.as_posix(), 'sha256': sha256(out.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
