"""Collocation sampling in physical coordinates y with a stateful CPU generator.

Regions (PROMPT.md section 10): core ball, logarithmic shells out to R_max, axis tube, origin cluster.
Each sample also carries an importance weight w = (physical volume of region) / (N * density) so that
sum_i w_i f(y_i) approximates the physical integral over the region (dy = r dr dtheta dz).
"""
import math
import torch


def _dirs(g, n):
    v = torch.randn(n, 3, generator=g, dtype=torch.float64)
    return v / v.norm(dim=-1, keepdim=True)


class Sampler:
    REGIONS = ("core", "shell", "axis", "origin")

    def __init__(self, cfg, seed):
        self.cfg = dict(cfg)
        self.g = torch.Generator()
        self.g.manual_seed(int(seed))

    def state_dict(self):
        return {"g": self.g.get_state(), "cfg": self.cfg}

    def load_state_dict(self, sd):
        self.g.set_state(sd["g"].cpu())

    def sample_region(self, name, n):
        c = self.cfg
        g = self.g
        if n <= 0:
            return torch.zeros(0, 3, dtype=torch.float64), torch.zeros(0, dtype=torch.float64)
        if name == "core":
            Rc = c["R_core"]
            u = torch.rand(n, 1, generator=g, dtype=torch.float64)
            y = Rc * u ** (1.0 / 3.0) * _dirs(g, n)
            vol = 4.0 / 3.0 * math.pi * Rc ** 3
            w = torch.full((n,), vol / n, dtype=torch.float64)
        elif name == "shell":
            R0, R1 = c["R_core"], c["R_max"]
            t = torch.rand(n, 1, generator=g, dtype=torch.float64)
            logR = math.log(R0) + t * (math.log(R1) - math.log(R0))
            R = torch.exp(logR)
            y = R * _dirs(g, n)
            # density in R: 1/(R (log R1 - log R0)); volume element 4 pi R^2 dR
            w = (4.0 * math.pi * R[:, 0] ** 3 * (math.log(R1) - math.log(R0))) / n
        elif name == "axis":
            rt, zmin, zmax = c["r_tube"], c.get("z_min", 1e-2), c["R_max"]
            r = rt * torch.sqrt(torch.rand(n, generator=g, dtype=torch.float64))
            th = 2 * math.pi * torch.rand(n, generator=g, dtype=torch.float64)
            t = torch.rand(n, generator=g, dtype=torch.float64)
            az = torch.exp(math.log(zmin) + t * (math.log(zmax) - math.log(zmin)))
            sgn = torch.where(torch.rand(n, generator=g, dtype=torch.float64) < 0.5, -1.0, 1.0)
            z = sgn * az
            y = torch.stack([r * torch.cos(th), r * torch.sin(th), z], -1)
            w = (math.pi * rt ** 2 * 2.0 * az * (math.log(zmax) - math.log(zmin))) / n
        elif name == "origin":
            R0 = c.get("R_origin", 0.5)
            u = torch.rand(n, 1, generator=g, dtype=torch.float64)
            y = R0 * u ** (1.0 / 3.0) * _dirs(g, n)
            vol = 4.0 / 3.0 * math.pi * R0 ** 3
            w = torch.full((n,), vol / n, dtype=torch.float64)
        else:
            raise ValueError(name)
        return y, w

    def sample(self, counts, device):
        """counts: dict region->n. Returns dict region -> (y, w) on device."""
        out = {}
        for name in self.REGIONS:
            n = int(counts.get("n_" + name, 0))
            if n > 0:
                y, w = self.sample_region(name, n)
                out[name] = (y.to(device), w.to(device))
        return out


def fixed_set(cfg, counts, seed, device):
    """A fixed (holdout) set drawn from an independent generator seed."""
    s = Sampler(cfg, seed)
    return s.sample(counts, device)
