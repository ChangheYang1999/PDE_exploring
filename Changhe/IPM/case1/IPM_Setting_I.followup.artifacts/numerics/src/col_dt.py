"""Which orbit step matters for a Jacobian column: far step dt or near-P step dt_near.  Central column at one node for several
(dt, dt_near) pairs against the accurate residual (dt 0.005, dt_near 0.02), Npsi 480 everywhere."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
spath = sys.argv[1]; which = sys.argv[2] if len(sys.argv) > 2 else 'far_yaxis'
m0, x, d = ipn.load_state(spath); b, cl = m0.unpack(x); C = float(d['C']); N, M = m0.N, m0.M
m = ipn.Model(N, M, m0.L, device='cuda', beta=m0.beta, nmodes=m0.nmodes, Mq=m0.Mq, Npsi=480); ch = cm.Charac(m)
z = ch.pack(b, cl, C); n = z.numel(); r, _, _ = m0.radii(float(cl)); thd = m0.ang.theta_np * 180 / np.pi
rr = r[1:][:, None] * np.ones((1, M)); tt = thd[None, :] * np.ones((N, 1))
cols = {'far_yaxis': int(np.argmin((np.log(rr / 2e3) ** 2 + ((tt - 88) / 10) ** 2).ravel())), 'mid_x': int(np.argmin((np.log(rr / 3.0) ** 2 + ((tt - 5) / 10) ** 2).ravel())), 'near_origin': int(np.argmin((np.log(rr / 0.5) ** 2 + ((tt - 45) / 10) ** 2).ravel()))}
j = cols[which]; e = torch.zeros(n, device='cuda'); e[j] = 1e-5
def col(dt, dtn, nsteps=None):
    Ff = lambda zz: ch.F_fixed(zz, dt=dt, dt_near=dtn, nsteps=nsteps)
    return (Ff(z + e) - Ff(z - e)) / 2e-5
ref = col(0.005, 0.02)
for dt, dtn in ((0.01, 0.04), (0.01, 0.02), (0.005, 0.04), (0.02, 0.02), (0.02, 0.08), (0.0025, 0.02)):
    t0 = time.time(); c = col(dt, dtn); dd = c - ref
    print(f'{which} col {j} (r {rr.ravel()[j]:.1f}, th {tt.ravel()[j]:.1f}): dt {dt} dt_near {dtn}: |diff| {dd.norm().item():.3e} of {ref.norm().item():.3e}; max entry {dd.abs().max().item():.2e} at row {int(dd.abs().argmax())}; rows>5500 part {dd[5500:].norm().item():.2e}, rows<3000 part {dd[:3000].norm().item():.2e} ({time.time()-t0:.0f}s)', flush=True)
