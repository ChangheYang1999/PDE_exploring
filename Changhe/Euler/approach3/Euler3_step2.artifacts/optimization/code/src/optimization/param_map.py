"""D6FP: smooth parameter transform between optimizer coordinates (z_c, z_w) and the physical parameters (c_l, omega) (SPEC 5.1):
    c_l = lo + (hi - lo) sigmoid(z_c),  omega = exp(z_w),   lo = 0.4, hi = 0.5.
The optimizer works on z_opt = (reduced coefficients ..., z_c, z_w); expand() maps it to (coefficients ..., c_l, omega) differentiably.
Chain rule (SPEC 5.2): dO/dz_c = (hi - lo) s (1 - s) dO/dc_l,  dO/dz_w = omega dO/domega."""
from __future__ import annotations
import math
import torch

DT = torch.float64


class ParamMap:
    def __init__(self, lo=0.4, hi=0.5, free=True):
        self.lo, self.hi, self.free = float(lo), float(hi), bool(free)

    def to_phys(self, zc, zw):
        s = torch.sigmoid(zc)
        return self.lo + (self.hi - self.lo) * s, torch.exp(zw)

    def to_opt(self, c_l, omega):
        c_l = float(c_l); omega = float(omega)
        if not (self.lo < c_l < self.hi) or not (omega > 0):
            raise ValueError(f"parameters outside the open domain: c_l {c_l}, omega {omega}")
        return math.log((c_l - self.lo) / (self.hi - c_l)), math.log(omega)

    def dphys_dopt(self, zc, zw):
        """(dc_l/dz_c, domega/dz_w) as floats."""
        zc = float(zc); zw = float(zw)
        s = 1.0 / (1.0 + math.exp(-zc))
        return (self.hi - self.lo) * s * (1.0 - s), math.exp(zw)

    def expand(self, z_opt):
        """z_opt (..., z_c, z_w) -> (..., c_l, omega), differentiable."""
        if not self.free:
            return z_opt
        c_l, omega = self.to_phys(z_opt[-2], z_opt[-1])
        return torch.cat([z_opt[:-2], torch.stack([c_l, omega])])

    def reduce(self, z_phys):
        if not self.free:
            return z_phys
        zc, zw = self.to_opt(float(z_phys[-2]), float(z_phys[-1]))
        return torch.cat([z_phys[:-2], torch.tensor([zc, zw], dtype=z_phys.dtype, device=z_phys.device)])

    def describe(self, z_opt):
        """Physical and optimizer values plus the chain-rule factors (for records)."""
        if not self.free:
            return {}
        zc, zw = float(z_opt[-2]), float(z_opt[-1])
        c_l, omega = self.to_phys(torch.tensor(zc), torch.tensor(zw))
        dc, dw = self.dphys_dopt(zc, zw)
        return dict(c_l=float(c_l), omega=float(omega), z_c=zc, z_w=zw, dcl_dzc=dc, domega_dzw=dw)

    def saturation_flag(self, z_opt, edge=0.002, omega_lo=1e-3, omega_hi=1e3):
        """SPEC 5.3: min(c_l - lo, hi - c_l) < edge, omega < omega_lo or omega > omega_hi."""
        d = self.describe(z_opt)
        if not d:
            return False
        return (min(d["c_l"] - self.lo, self.hi - d["c_l"]) < edge) or (d["omega"] < omega_lo) or (d["omega"] > omega_hi)
