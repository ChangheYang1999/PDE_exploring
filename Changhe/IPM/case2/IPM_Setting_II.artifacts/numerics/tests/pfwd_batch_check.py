"""PFwdB against PFwd: (1) two identical states = the single-state result to roundoff; (2) a state with p != p_kernel against a
single-state run at that p (tail correction).  Also timing of a batched step for B = 1, 8, 32, 65."""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd
from pfwd_batch import PFwdB
from pfwd_fp import basis
torch.set_default_dtype(torch.float64)
Nr, Nth, lo, hi = 361, 128, -12.0, 10.0
a0 = torch.tensor([0.2390, -0.7141, -0.2124, 0.1220, 0.1070, -0.0270], device='cuda')
def Afun_single(a):
    def f(th):
        s = torch.zeros_like(th)
        for j in range(6): s = s + float(a[j]) * basis(th, j)
        return torch.cos(th) ** 2 * torch.exp(s)
    return f
def Afun_batch(aB):                       # aB [B, 6]
    def f(th):                            # th [B, ...]
        s = torch.zeros_like(th)
        for j in range(6): s = s + aB[:, j].view((-1,) + (1,) * (th.dim() - 1)) * basis(th, j)
        return torch.cos(th) ** 2 * torch.exp(s)
    return f
p0 = 0.4957; ds = 0.02; nst = 60
S = PFwd(Nr, Nth, lo, hi, p0); Af = Afun_single(a0); A = Af(S.th)
g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p0 / 2))[:, None] * A[None, :]
g1 = g.clone()
for n in range(nst): g1, _ = S.step(g1, ds, A, Af)
SB = PFwdB(Nr, Nth, lo, hi, p0, bspline=False)   # the historical Lagrange transport (the comparison target is PFwd); the B-spline scheme is tested in tests/pfwd_bspline_accept.py
aB = torch.stack([a0, a0]); pB = torch.tensor([p0, p0], device='cuda'); AB = Afun_batch(aB)(SB.th[None, :].expand(2, -1))
gB = g[None].expand(2, -1, -1).clone()
gB, dg = SB.evolve(gB, pB, AB, Afun_batch(aB), ds, nst)
print("test 1 (equal p): max |batched - single| = %.3e, %.3e   (dg/ds %s)" % (float((gB[0] - g1).abs().max()), float((gB[1] - g1).abs().max()), dg.tolist()))
# test 2: p != kernel p
p1 = p0 + 0.01
S2 = PFwd(Nr, Nth, lo, hi, p1); A2 = Af(S2.th)
g2 = ((S2.r ** 2 / (1.0 + S2.r ** 2)) ** (1.0 - p1 / 2))[:, None] * A2[None, :]
for n in range(nst): g2, _ = S2.step(g2, ds, A2, Af)
aB = torch.stack([a0, a0]); pB = torch.tensor([p0, p1], device='cuda')
gB0 = ((SB.r[None, :, None] ** 2 / (1.0 + SB.r[None, :, None] ** 2)) ** (1.0 - pB[:, None, None] / 2)) * AB[:, None, :]
gB, dg = SB.evolve(gB0, pB, AB, Afun_batch(aB), ds, nst)
print("test 2 (p = p_k + 0.01 in the batch, kernel at p_k): max |batched - single(p1)| = %.3e; state 0 vs single(p0) %.3e" % (float((gB[1] - g2).abs().max()), float((gB[0] - g1).abs().max())))
# velocity-only comparison at p1
rho2 = S2.r[:, None] ** p1 * g2; Wr2, Wt2 = S2.velocity(rho2)
WrB, WtB = SB.velocity(torch.stack([rho2, rho2]), torch.tensor([p1, p1], device='cuda'))
print("test 2b velocity at p1 via tail correction: %.3e %.3e (scale %.3e)" % (float((WrB[0] - Wr2).abs().max()), float((WtB[0] - Wt2).abs().max()), float(Wr2.abs().max())))
# timing at the production grid
Nr, Nth, lo, hi = 721, 256, -14.0, 10.0
SB = PFwdB(Nr, Nth, lo, hi, p0, bspline=False)   # the historical Lagrange transport (the comparison target is PFwd); the B-spline scheme is tested in tests/pfwd_bspline_accept.py
for B in (1, 8, 32, 65):
    aB = a0[None].expand(B, -1).clone(); pB = torch.full((B,), p0, device='cuda'); AB = Afun_batch(aB)(SB.th[None, :].expand(B, -1))
    gB = ((SB.r[None, :, None] ** 2 / (1.0 + SB.r[None, :, None] ** 2)) ** (1.0 - pB[:, None, None] / 2)) * AB[:, None, :]
    torch.cuda.synchronize(); t0 = time.time()
    gB, dg = SB.evolve(gB, pB, AB, Afun_batch(aB), ds, 20)
    torch.cuda.synchronize(); t1 = time.time()
    T, u0, w0, th0, it, arrived = SB.trace(*SB.velocity(SB.r[None, :, None] ** pB[:, None, None] * gB, pB), pB, torch.arange(1440, device='cuda') * (2 * math.pi / 1440), -13.0)
    torch.cuda.synchronize(); t2 = time.time()
    print("B = %2d: %.3f s per step, trace %.1f s (%d its), GPU mem %.1f GB" % (B, (t1 - t0) / 20, t2 - t1, it, torch.cuda.max_memory_allocated() / 1e9))
