# Lead: prefiltered cubic B-spline interpolation as a drop-in replacement for the numerics' PFwdB.interp
# (same signature, same row convention [row 0 copy, rows 0..Nr-1, top_rows], same bilinear-hull clip on the grid values).
# Prefilter: convolution with sqrt(3) alpha^|k|, alpha = sqrt(3) - 2, |k| <= KH (exact inverse of (1, 4, 1)/6 up to
# |alpha|^(KH+1) ~ 1e-14 for KH = 24); periodic in th, edge-replicated in lr. Evaluation: tensor-product cubic B-spline weights.
# Usage (read-only import from the other code is fine):
#   sys.path.insert(0, 'explore'); import bspline_torch as BT
#   BT.patch(PFwdB)      # every PFwdB.interp call (velocity midpoints and g) becomes the B-spline interpolant
import math
import torch
import torch.nn.functional as Fn

KH = 24
_cache = {}


def _kernel(dev, dtype):
    key = (str(dev), dtype)
    if key not in _cache:
        a = math.sqrt(3.0) - 2.0
        w = [math.sqrt(3.0) * a ** abs(k) for k in range(-KH, KH + 1)]
        _cache[key] = torch.tensor(w, device=dev, dtype=dtype).view(1, 1, -1)
    return _cache[key]


def prefilter(Fp):
    """Fp [B, R, Nth] -> B-spline coefficients C with (C[i-1] + 4 C[i] + C[i+1]) / 6 = Fp[i] in both directions."""
    B, R, N = Fp.shape
    k = _kernel(Fp.device, Fp.dtype)
    X = Fp.reshape(B * R, 1, N)
    X = Fn.conv1d(Fn.pad(X, (KH, KH), mode='circular'), k).reshape(B, R, N)
    X = X.permute(0, 2, 1).reshape(B * N, 1, R)
    X = Fn.conv1d(Fn.pad(X, (KH, KH), mode='replicate'), k).reshape(B, N, R).permute(0, 2, 1)
    return X.contiguous()


def _bw(t):
    t2 = t * t; t3 = t2 * t
    return ((1 - t) ** 3 / 6, (3 * t3 - 6 * t2 + 4) / 6, (-3 * t3 + 3 * t2 + 3 * t + 1) / 6, t3 / 6)


def interp_bspline(self, F, ci, cj, top_rows):
    """F [B, Nr, Nth]; ci, cj [B, ...] fractional indices; top_rows [B, 2, Nth]."""
    Nr, Nth = self.Nr, self.Nth
    B = F.shape[0]
    Fp = torch.cat([F[:, :1], F, top_rows], 1)                        # [B, Nr+3, Nth]: rows -1 .. Nr+1 -> +1
    Cp = prefilter(Fp)
    bidx = torch.arange(B, device=F.device).view((B,) + (1,) * (ci.dim() - 1))
    i0 = torch.floor(ci).long()
    j0 = torch.floor(cj); u = cj - j0; j0 = j0.long()
    i0 = torch.clamp(i0, 0, Nr)
    t = torch.where((ci - i0.double()) > 1.0, torch.ones_like(ci), ci - i0.double())
    wi = _bw(t); wj = _bw(u)
    out = torch.zeros_like(ci)
    for a in range(4):
        ia = (i0 + (a - 1) + 1).clamp(0, Nr + 2)
        rowv = torch.zeros_like(ci)
        for b in range(4):
            jb = torch.remainder(j0 + (b - 1), Nth)
            rowv = rowv + wj[b] * Cp[bidx, ia, jb]
        out = out + wi[a] * rowv
    if getattr(self, 'limiter', True):
        ia0 = (i0 + 1).clamp(0, Nr + 2); ia1 = (i0 + 2).clamp(0, Nr + 2)
        ja0 = torch.remainder(j0, Nth); ja1 = torch.remainder(j0 + 1, Nth)
        c00 = Fp[bidx, ia0, ja0]; c01 = Fp[bidx, ia0, ja1]; c10 = Fp[bidx, ia1, ja0]; c11 = Fp[bidx, ia1, ja1]
        lo = torch.minimum(torch.minimum(c00, c01), torch.minimum(c10, c11))
        hi = torch.maximum(torch.maximum(c00, c01), torch.maximum(c10, c11))
        out = torch.minimum(torch.maximum(out, lo), hi)
    return out


def patch(cls):
    """Replace cls.interp (PFwdB) by the B-spline interpolant; returns the original for restoring."""
    orig = cls.interp
    cls.interp = interp_bspline
    return orig
