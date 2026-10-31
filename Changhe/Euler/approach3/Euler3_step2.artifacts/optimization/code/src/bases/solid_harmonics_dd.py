"""D6FP (2026-10-28): the regular solid harmonics P_q(y) = r^l Y_q and their Cartesian derivative tables evaluated with the SAME recurrences and
ladder identities as src/bases/solid_harmonics.py but in double-double arithmetic (two float64 words, about 32 significant digits), then rounded
once to float64. Reason: the verifier's V020 found entries of the first and second derivative tables (degrees 4 to 15) with relative errors up to
6e-10 against a 70-digit reference: the ladder identities subtract nearly equal terms, and the float64 recurrences cannot represent small entries
to 1e-13 relative (SPEC G5 (c)). With 32 internal digits the final rounding dominates (validation/check_angular_dd.py: all 4471080 defined entries
of the nest6 tables equal the verifier's binary64-rounded 70-digit reference). Same conventions and output shapes as eval_solid; the normalization
constants are computed in 60-digit decimal arithmetic and carried as double-double.
Version 2: vectorized over the order m (one tensor (..., 2L+1) per degree l), so the Python loops run over l only."""
from __future__ import annotations
import math
from decimal import Decimal, localcontext
import torch

DT = torch.float64
_SPLIT = 134217729.0          # 2^27 + 1 (Veltkamp split)
_PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798")


def _two_sum(a, b):
    s = a + b; bb = s - a
    return s, (a - (s - bb)) + (b - bb)


def _quick_two_sum(a, b):
    s = a + b
    return s, b - (s - a)


def _split(a):
    t = _SPLIT * a; hi = t - (t - a)
    return hi, a - hi


def _two_prod(a, b):
    p = a * b
    ah, al = _split(a); bh, bl = _split(b)
    err = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, err


class DD:
    """Double-double tensor (hi, lo); elementwise with broadcasting."""
    __slots__ = ("hi", "lo")

    def __init__(self, hi, lo=None):
        self.hi = hi; self.lo = torch.zeros_like(hi) if lo is None else lo

    def __add__(self, o):
        s, e = _two_sum(self.hi, o.hi); e = e + (self.lo + o.lo)
        return DD(*_quick_two_sum(s, e))

    def __neg__(self):
        return DD(-self.hi, -self.lo)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if isinstance(o, DD):
            p, e = _two_prod(self.hi, o.hi); e = e + (self.hi * o.lo + self.lo * o.hi)
            return DD(*_quick_two_sum(p, e))
        o = torch.as_tensor(o, dtype=self.hi.dtype, device=self.hi.device)        # exact single-word factor (coordinate or integer constant tensor)
        p, e = _two_prod(self.hi, o); e = e + self.lo * o
        return DD(*_quick_two_sum(p, e))

    def div(self, b):
        """division by an exact single-word tensor b (broadcastable)."""
        b = torch.as_tensor(b, dtype=self.hi.dtype, device=self.hi.device)
        q1 = self.hi / b
        p, e = _two_prod(q1, b)
        s = ((self.hi - p) - e) + self.lo
        q2 = s / b
        return DD(*_quick_two_sum(q1, q2))

    def to_double(self):
        return self.hi + self.lo

    def __getitem__(self, idx):
        return DD(self.hi[idx], self.lo[idx])


def complex_table_dd(y, L):
    """Re, Im lists indexed by l of DD tensors (..., 2L+1) holding R_l^m(y), m = -L..L at index m + L (the recurrences of
    solid_harmonics.complex_table in double-double, vectorized over m)."""
    x, yy, z = y[..., 0], y[..., 1], y[..., 2]
    shape = y.shape[:-1]; dev = y.device
    rho = DD(x) * x + DD(yy) * yy + DD(z) * z
    W = 2 * L + 1
    zeros = torch.zeros(shape + (W,), dtype=DT, device=dev)
    Re = []; Im = []
    for l in range(L + 1):
        Re.append(DD(zeros.clone())); Im.append(DD(zeros.clone()))
    # R_m^m along the diagonal (sequential in m, scalar per point), then R_{m+1}^m = z R_m^m, then upward in l for all m at once
    diag_re = [DD(torch.ones(shape, dtype=DT, device=dev))]; diag_im = [DD(torch.zeros(shape, dtype=DT, device=dev))]
    for m in range(1, L + 1):
        pr, pi_ = diag_re[-1], diag_im[-1]
        diag_re.append((pr * x - pi_ * yy).div(torch.full(shape, 2.0 * m, dtype=DT, device=dev)))
        diag_im.append((pi_ * x + pr * yy).div(torch.full(shape, 2.0 * m, dtype=DT, device=dev)))
    for m in range(L + 1):
        Re[m].hi[..., L + m] = diag_re[m].hi; Re[m].lo[..., L + m] = diag_re[m].lo
        Im[m].hi[..., L + m] = diag_im[m].hi; Im[m].lo[..., L + m] = diag_im[m].lo
        if m + 1 <= L:
            v = diag_re[m] * z; w = diag_im[m] * z
            Re[m + 1].hi[..., L + m] = v.hi; Re[m + 1].lo[..., L + m] = v.lo
            Im[m + 1].hi[..., L + m] = w.hi; Im[m + 1].lo[..., L + m] = w.lo
    mvals = torch.arange(-L, L + 1, dtype=DT, device=dev)
    for l in range(2, L + 1):
        # R_l^m = [(2l-1) z R_{l-1}^m - rho R_{l-2}^m] / ((l-m)(l+m)) for 0 <= m <= l-2; entries m = l-1, l already set
        mask = (mvals >= 0) & (mvals <= l - 2)
        denom = torch.where(mask, (l - mvals) * (l + mvals), torch.ones_like(mvals))
        for T in (Re, Im):
            num = (T[l - 1] * z[..., None]) * float(2 * l - 1) - (T[l - 2] * rho.hi[..., None]) if False else ((T[l - 1] * z[..., None]) * torch.full((), float(2 * l - 1), dtype=DT, device=dev)) - _dd_mul_rho(T[l - 2], rho)
            val = num.div(denom)
            T[l].hi = torch.where(mask, val.hi, T[l].hi); T[l].lo = torch.where(mask, val.lo, T[l].lo)
    # negative m: R_l^{-m} = (-1)^m conj(R_l^m)
    sgn = torch.tensor([(-1.0) ** abs(int(m)) for m in range(-L, L + 1)], dtype=DT, device=dev)
    for l in range(L + 1):
        pos = torch.arange(L, 2 * L + 1, device=dev)            # m = 0..L
        neg = torch.arange(L, -1, -1, device=dev)               # m = 0..-L (same |m|)
        for T, s_ in ((Re, 1.0), (Im, -1.0)):
            hi = T[l].hi.clone(); lo = T[l].lo.clone()
            hi[..., neg] = s_ * sgn[pos] * T[l].hi[..., pos]; lo[..., neg] = s_ * sgn[pos] * T[l].lo[..., pos]
            T[l].hi, T[l].lo = hi, lo
    return Re, Im


def _dd_mul_rho(T, rho):
    """DD tensor (..., W) times DD scalar field rho (...)."""
    return T * DD(rho.hi[..., None].expand_as(T.hi), rho.lo[..., None].expand_as(T.lo))


def _shift(T, L, dl, dm):
    """S[l][m] = T[l+dl][m+dm] (zero outside); lists of DD (..., W)."""
    W = 2 * L + 1
    out = []
    for l in range(L + 1):
        lp = l + dl
        hi = torch.zeros_like(T[0].hi); lo = torch.zeros_like(T[0].lo)
        if 0 <= lp <= L:
            # destination index j = m + L, source index j + dm; valid when |m + dm| <= lp and |m| <= l
            m = torch.arange(-L, L + 1, device=hi.device)
            valid = (m.abs() <= l) & ((m + dm).abs() <= lp)
            src = (m + dm + L).clamp(0, W - 1)
            hi = torch.where(valid, T[lp].hi[..., src], hi); lo = torch.where(valid, T[lp].lo[..., src], lo)
        out.append(DD(hi, lo))
    return out


def ladder_tables_dd(Re, Im, L):
    """(dx, dy, dz) derivative tables as (Re, Im) lists: d/dz R_l^m = R_{l-1}^m, (dx + i dy) R = -R_{l-1}^{m+1}, (dx - i dy) R = R_{l-1}^{m-1}."""
    Azr, Azi = _shift(Re, L, -1, 0), _shift(Im, L, -1, 0)
    Pr, Pi = _shift(Re, L, -1, 1), _shift(Im, L, -1, 1)
    Mr, Mi = _shift(Re, L, -1, -1), _shift(Im, L, -1, -1)
    half = torch.full((), 2.0, dtype=DT, device=Re[0].hi.device)
    dxr = [(Mr[l] - Pr[l]).div(half) for l in range(L + 1)]; dxi = [(Mi[l] - Pi[l]).div(half) for l in range(L + 1)]
    dyr = [-((Pi[l] + Mi[l]).div(half)) for l in range(L + 1)]; dyi = [(Pr[l] + Mr[l]).div(half) for l in range(L + 1)]
    return (dxr, dxi), (dyr, dyi), (Azr, Azi)


def _norm_constant(l, m):
    """sqrt((2l+1)(l-m)!/(4 pi (l+m)!)) times l! (m = 0) or sqrt(2) (l+m)! (m > 0), in a LOCAL 60-digit decimal context (no process-global side effect;
    verifier note 2026-10-28T22:40Z)."""
    with localcontext() as ctx:
        ctx.prec = 60
        N = (Decimal(2 * l + 1) * Decimal(math.factorial(l - m)) / (Decimal(4) * _PI * Decimal(math.factorial(l + m)))).sqrt()
        if m == 0:
            return N * Decimal(math.factorial(l))
        return Decimal(2).sqrt() * N * Decimal(math.factorial(l + m))


_CONST_CACHE = {}


def real_from_complex_dd(Re, Im, modes, L):
    like = Re[0].hi[..., 0]
    out = []
    for (l, m, t) in modes:
        if l > L:
            out.append(torch.zeros_like(like)); continue
        key = (l, m)
        if key not in _CONST_CACHE:
            c = _norm_constant(l, m); hi = float(c); lo = float(c - Decimal(hi)); _CONST_CACHE[key] = (hi, lo)
        hi, lo = _CONST_CACHE[key]
        src = Re[l] if (m == 0 or t == 0) else Im[l]
        v = src[..., L + m]
        c_dd = DD(torch.full_like(like, hi), torch.full_like(like, lo))
        out.append((v * c_dd).to_double())
    return torch.stack(out, dim=-1)


def eval_solid_dd(y, modes, L, nderiv=2):
    """Same interface as solid_harmonics.eval_solid: A0 (..., Nq), A1 (3, ..., Nq), A2 (3, 3, ..., Nq), computed in double-double and rounded once."""
    y = torch.as_tensor(y, dtype=DT)
    Re, Im = complex_table_dd(y, L)
    A0 = real_from_complex_dd(Re, Im, modes, L)
    if nderiv == 0:
        return A0, None, None
    d = ladder_tables_dd(Re, Im, L)
    A1 = torch.stack([real_from_complex_dd(dr, di, modes, L) for (dr, di) in d], dim=0)
    if nderiv == 1:
        return A0, A1, None
    A2 = []
    for i in range(3):
        dd = ladder_tables_dd(d[i][0], d[i][1], L)
        A2.append(torch.stack([real_from_complex_dd(dr, di, modes, L) for (dr, di) in dd], dim=0))
    return A0, A1, torch.stack(A2, dim=0)
