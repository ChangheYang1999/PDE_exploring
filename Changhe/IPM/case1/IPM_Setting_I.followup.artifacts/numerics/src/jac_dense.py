"""Dense Jacobian of the hybrid Psi-map residual (charmap.Charac.F_fixed) by one-sided finite differences, batched with
torch.func.vmap.  Resumable: partial columns are saved every `save_every` batches.
Usage: python3 src/jac_dense.py runs/state.npz tag [batch=32] [eps=1e-5] [dt=0.01] [Npsi] [tau_far]
Output: runs/J_<tag>.pt (dict: J (n x n), F0, z0, args), log on stdout."""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm

LANE = '.'


def main():
    path, tag = sys.argv[1], sys.argv[2]
    batch = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    eps = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-5
    dt = float(sys.argv[5]) if len(sys.argv) > 5 else 0.01
    Npsi = int(sys.argv[6]) if len(sys.argv) > 6 else None
    tau_far = float(sys.argv[7]) if len(sys.argv) > 7 else None      # if given: fixed step count for backward time tau_far at dt, the rest at dt_near
                                                                      # (all orbits are within 0.5 of P by tau = 7 on the X3-lineage states: the research record 07:10Z)
    model, x, d = ipn.load_state(path); b, cl = model.unpack(x); C = float(d['C'])
    if Npsi is not None and Npsi != model.Npsi:
        model = ipn.Model(model.N, model.M, model.L, device='cuda', beta=model.beta, nmodes=model.nmodes, Mq=model.Mq, Npsi=Npsi)
    ch = cm.Charac(model); z = ch.pack(b, cl, C); n = z.numel()
    nsteps = None if tau_far is None else int(tau_far / dt) + int((14.0 - tau_far) / (4 * dt)) + 10
    Ff = lambda zz: ch.F_fixed(zz, dt=dt, dt_near=4 * dt, nsteps=nsteps)
    out = f'{LANE}/runs/J_{tag}.pt'
    t0 = time.time()
    if os.path.exists(out + '.partial'):
        st = torch.load(out + '.partial'); J = st['J'].to(model.dev); F0 = st['F0'].to(model.dev); start = st['next']
        print(f'resuming at column {start}', flush=True)
    else:
        F0 = Ff(z); J = torch.zeros(n, n, device=model.dev); start = 0
        if nsteps is not None:
            Ffull = ch.F_fixed(z, dt=dt, dt_near=4 * dt); dd = (Ffull - F0).abs().max().item()
            print(f'step-cut check: |F_full - F_cut|_inf = {dd:.3e} (nsteps {nsteps})', flush=True)
            assert dd < 1e-11, 'step cut changes the residual: increase tau_far'
    print(f'{tag}: n = {n}, |F0| = {F0.norm().item():.4e}, batch {batch}, eps {eps}, dt {dt}, Npsi {model.Npsi}, nsteps {nsteps}; start {start}', flush=True)
    scale = torch.ones(n, device=model.dev); scale[-2] = 1.0 / 400.0     # c_l column in units of 1/400 (as in the driver's --scl)
    nb = 0
    for s0 in range(start, n, batch):
        idx = torch.arange(s0, min(s0 + batch, n), device=model.dev); B = idx.numel()
        E = torch.zeros(B, n, device=model.dev); E[torch.arange(B, device=model.dev), idx] = eps * scale[idx]
        FB = torch.func.vmap(Ff)(z[None] + E)
        J[:, idx] = ((FB - F0[None]) / (eps * scale[idx])[:, None]).T
        nb += 1
        if nb % 5 == 0 or s0 + B >= n:
            el = time.time() - t0
            print(f'  columns {s0 + B}/{n}  {el/60:.1f} min  ({el/(s0 + B - start)*(n - s0 - B)/60:.1f} min left)', flush=True)
        if nb % 20 == 0:
            torch.save(dict(J=J.cpu(), F0=F0.cpu(), next=s0 + B), out + '.partial')
    torch.save(dict(J=J.cpu(), F0=F0.cpu(), z0=z.cpu(), state=path, eps=eps, dt=dt, scale=scale.cpu(), N=model.N, M=model.M,
                    beta=model.beta, L=model.L, C=C, Npsi=model.Npsi, nsteps=nsteps, tau_far=tau_far), out)
    if os.path.exists(out + '.partial'): os.remove(out + '.partial')
    print(f'saved {out} ({time.time()-t0:.0f}s)', flush=True)


if __name__ == '__main__':
    main()
