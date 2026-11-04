"""phi_honest2.py (lane numerics_agent_1): extended-precision (numpy longdouble) evaluation of F_* and its first and second Cartesian derivatives on a fixed-background product
mesh, and of the weighted energies E_0, E_1, E_2 and N_2 = sqrt(E_0 + 2 E_1 + E_2) at the tuples P-S1 = (sigma 1, r0 1/2) and P-S2 = (sigma 7/5, r0 1), from the frozen exact
JSON; the same quantities in binary64 by the same code, for the noise realization.  Purpose: numerics_agent_2 11:45Z (the binary64 second-derivative fields of F_* for 013 are
roundoff-dominated at 2 <= r <= 32); checks the N_2 values of numerics_v05/v06 and the statement of numerics_v06 N20.4(a) about E_1, E_2.  All FLOAT; no bound.
Usage: phi_honest2.py <phi_exact.json> <background.pt> <out.json>
Fields: h_(i,j) = -(phi_(i+2,j) + phi_(i,j+2)) for i+j <= 3; v1_(i,j) = -phi_(i+1,j+1), v2_(i,j) = phi_(i+2,j) for i+j <= 2 (the convention of phi_atoms.atom_slots and phi_fit).
F_d = F0_d + D^d[(c X + u_C).grad h - h + v.grad rho_C] + D^d[v.grad h] by the Leibniz rule (phi_fit.lin and .quad); u_C = (-psi_y, psi_x)."""
import sys, os, json, math, time
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phi_honest as PH
import phi_atoms as PA
import ipm_polar as PL
LD = np.longdouble
DERIVS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
def leibniz(i, j):
    return [(math.comb(i, i1)*math.comb(j, j1), (i1, j1), (i-i1, j-j1)) for i1 in range(i+1) for j1 in range(j+1)]
LEIB = {d: leibniz(*d) for d in DERIVS}
HKEYS = [('h', (i, j)) for i in range(4) for j in range(4-i)]
VKEYS = [(t, (i, j)) for t in ('v1', 'v2') for i in range(3) for j in range(3-i)]
KEYS = HKEYS+VKEYS

def key_series(n):
    S = PA.atom_series(n, omax=5); neg = lambda T: {k: -v for k, v in T.items()}; out = {}
    for (_, (i, j)) in HKEYS: out[('h', (i, j))] = neg(PL.add(S[(i+2, j)], S[(i, j+2)]))
    for (t, (i, j)) in VKEYS: out[(t, (i, j))] = neg(S[(i+1, j+1)]) if t == 'v1' else S[(i+2, j)]
    return out

def accumulate(params, r, dt, log=None):
    rad = {key: {} for key in KEYS}; rl = r.astype(dt); t0 = time.time(); rpow = {}; ks = {}
    conv = lambda v: (dt(v) if isinstance(v, float) else PH.fr2(v, dt))
    for ia, (A_, n, h, b_, t_, d, k) in enumerate(params):
        A = conv(A_)
        if A == 0: continue
        b = conv(b_); t = conv(t_)
        G = PH.radial_jets(n, h, b, t, d, rl, 5, k)
        if n not in ks: ks[n] = key_series(n)
        for key, S in ks[n].items():
            for (a, bb, N, tt), v in S.items():
                if bb not in rpow: rpow[bb] = rl**(-bb) if bb else None
                term = G[a]*PH.fr2(v, dt)
                if bb: term = term*rpow[bb]
                term = term*A
                kk = ('sin' if tt == 's' else 'cos', N)
                rad[key][kk] = rad[key][kk]+term if kk in rad[key] else term
        if log and (ia+1) % 2000 == 0: print(f'  {ia+1} atoms, {time.time()-t0:.0f} s', flush=True)
    return rad

def fstar_derivs(fl, bg, dt):
    """F_d for d in DERIVS (binary64 base fields cast to dt)"""
    c = PH.fr2('4076476460239181/2251799813685248', dt); x, y = bg['x'].astype(dt), bg['y'].astype(dt)
    hf = {k[1]: fl[k] for k in HKEYS}; vf = {k: fl[k] for k in VKEYS}
    rho = {k: v.astype(dt) for k, v in bg['rho'].items()}; psi = {k: v.astype(dt) for k, v in bg['psi'].items()}
    u1 = {d: -psi[(d[0], d[1]+1)] for d in DERIVS}; u2 = {d: psi[(d[0]+1, d[1])] for d in DERIVS}
    out = {}
    for d in DERIVS:
        i, j = d
        lin = c*x*hf[(i+1, j)]+c*y*hf[(i, j+1)]+(c*(i+j)-1)*hf[(i, j)]
        quad = 0
        for cf, d1, d2 in LEIB[d]:
            lin = lin+cf*(u1[d1]*hf[(d2[0]+1, d2[1])]+u2[d1]*hf[(d2[0], d2[1]+1)])
            lin = lin+cf*(rho[(d2[0]+1, d2[1])]*vf[('v1', d1)]+rho[(d2[0], d2[1]+1)]*vf[('v2', d1)])
            quad = quad+cf*(vf[('v1', d1)]*hf[(d2[0]+1, d2[1])]+vf[('v2', d1)]*hf[(d2[0], d2[1]+1)])
        out[d] = bg['F0'][d].astype(dt)+lin+quad
    return out

def weight_derivs(r, x, y, sig, r0, dt):
    r = r.astype(dt); x = x.astype(dt); y = y.astype(dt)
    A = 1+r**2/r0**2; W = A**(sig/2); W1 = sig*r/r0**2*A**(sig/2-1); W2 = sig/r0**2*A**(sig/2-1)+sig*(sig/2-1)*2*r**2/r0**4*A**(sig/2-2)
    Wx = W1*x/r; Wy = W1*y/r; Wxx = W2*x**2/r**2+W1*y**2/r**3; Wyy = W2*y**2/r**2+W1*x**2/r**3; Wxy = (W2-W1/r)*x*y/r**2
    return W, Wx, Wy, Wxx, Wxy, Wyy

def n2_weighted(comp, base, r2d, x, y, sig, r0, dt):
    W, Wx, Wy, Wxx, Wxy, Wyy = weight_derivs(r2d, x, y, sig, r0, dt); F = comp[(0, 0)]; b = base.astype(dt)
    g = W*F; gx = W*comp[(1, 0)]+Wx*F; gy = W*comp[(0, 1)]+Wy*F
    gxx = W*comp[(2, 0)]+2*Wx*comp[(1, 0)]+Wxx*F; gxy = W*comp[(1, 1)]+Wx*comp[(0, 1)]+Wy*comp[(1, 0)]+Wxy*F; gyy = W*comp[(0, 2)]+2*Wy*comp[(0, 1)]+Wyy*F
    E0 = float((b*g**2).sum()); E1 = float((b*(gx**2+gy**2)).sum()); E2 = float((b*(gxx**2+2*gxy**2+gyy**2)).sum())
    return {'N2': math.sqrt(E0+2*E1+E2), 'E0': E0, 'E1': E1, 'E2': E2}, (gxx, gxy, gyy, g, gx, gy)

def load_bg(pt):
    import torch
    bg = torch.load(pt, weights_only=False); m = bg['mesh']
    s = m['s'].numpy().astype(np.float64); ws = m['ws'].numpy().astype(np.float64); theta = m['theta'].numpy().astype(np.float64); wth = m['wth'].numpy().astype(np.float64)
    r = np.exp(s); x = r[:, None]*np.cos(theta)[None, :]; y = r[:, None]*np.sin(theta)[None, :]; base = 4*(ws[:, None]*wth[None, :])*(r**2)[:, None]
    bgf = {'x': x, 'y': y, 'F0': {d: bg['F0'][d].numpy() for d in DERIVS}, 'rho': {k: v.numpy() for k, v in bg['rho'].items()}, 'psi': {k: v.numpy() for k, v in bg['psi'].items()}}
    return r, theta, base, bgf, bg['meta']

def main():
    phip, bgp, outp = sys.argv[1], sys.argv[2], sys.argv[3]; savep = sys.argv[4] if len(sys.argv) > 4 else None
    P = json.load(open(phip)); params = PH.params_from_json_atoms(P['atoms'])
    r, theta, base, bgf, meta = load_bg(bgp); r2d = r[:, None]*np.ones((1, len(theta)))
    print(f'{len(params)} atoms; mesh {len(r)} x {len(theta)} from {os.path.basename(bgp)}; 22 fields to order 3 (h) and 2 (v)', flush=True)
    res = {'label': 'FLOAT (longdouble against binary64, same code); no bound', 'phi_json': os.path.relpath(phip), 'phi_sha256': __import__('hashlib').sha256(open(phip, 'rb').read()).hexdigest(),
           'background_pt': os.path.relpath(bgp), 'mesh': {'Nr': len(r), 'Nt': len(theta)}, 'tuples': {}, 'rows': [], 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    comps = {}; g2 = {}
    for name, dt in (('binary64', np.float64), ('longdouble', LD)):
        T0 = time.time(); rad = accumulate(params, r, dt, log=True); fl = PH.assemble(rad, theta, dt, nr=len(r)); comps[name] = fstar_derivs(fl, bgf, dt)
        print(f'{name} pass {time.time()-T0:.0f} s', flush=True)
    for tname, (sig, r0) in {'P-S1': (1.0, 0.5), 'P-S2': (1.4, 1.0)}.items():
        res['tuples'][tname] = {}
        for name, dt in (('binary64', np.float64), ('longdouble', LD)):
            n2, gg = n2_weighted(comps[name], base, r2d, bgf['x'], bgf['y'], sig, r0, dt); res['tuples'][tname][name] = n2; g2[(tname, name)] = gg
            print(f'{tname} {name}: N_2 {n2["N2"]:.6e}  E_0 {n2["E0"]:.4e}  E_1 {n2["E1"]:.4e}  E_2 {n2["E2"]:.4e}', flush=True)
        # noise field energies of the second-derivative part
        gb, gl = g2[(tname, 'binary64')], g2[(tname, 'longdouble')]
        dE2 = float((base*((gb[0]-gl[0].astype(np.float64))**2+2*(gb[1]-gl[1].astype(np.float64))**2+(gb[2]-gl[2].astype(np.float64))**2)).sum())
        res['tuples'][tname]['E2_noise_field_energy_binary64_minus_longdouble'] = dE2
        print(f'{tname}: energy of the binary64-minus-longdouble second-derivative field {dE2:.4e} (share of the binary64 E_2: {dE2/res["tuples"][tname]["binary64"]["E2"]:.3f})', flush=True)
    if savep:
        # dump of the longdouble fields (rounded to binary64 for storage) in the PHIEVAL-style layout of numerics_agent_2's nq_hankel2.py: <prefix>_s_fine.npy (log r), _theta_fine.npy,
        # _WFgrid_PS1_ij.npy and _WFgrid_PS2_ij.npy (ij in 00, 10, 01, 20, 11, 02: the weighted field g = W F_* and its Cartesian derivatives), _Fgrid_ij.npy (unweighted F_* derivatives),
        # _base_weights.npy (the quadrature weights 4 ws wth r^2 of the fixed background mesh).  FLOAT.
        np.save(savep+'_s_fine.npy', np.log(r)); np.save(savep+'_theta_fine.npy', theta); np.save(savep+'_base_weights.npy', base)
        IJ = {(0, 0): '00', (1, 0): '10', (0, 1): '01', (2, 0): '20', (1, 1): '11', (0, 2): '02'}
        for d, ij in IJ.items(): np.save(f'{savep}_Fgrid_{ij}.npy', comps['longdouble'][d].astype(np.float64))
        for tname, tag in (('P-S1', 'PS1'), ('P-S2', 'PS2')):
            gxx, gxy, gyy, g, gx, gy = g2[(tname, 'longdouble')]
            for arr, ij in ((g, '00'), (gx, '10'), (gy, '01'), (gxx, '20'), (gxy, '11'), (gyy, '02')): np.save(f'{savep}_WFgrid_{tag}_{ij}.npy', arr.astype(np.float64))
        json.dump({'label': 'FLOAT longdouble derivative fields of F_* (rounded to binary64 for storage); no bound', 'phi_json': os.path.relpath(phip), 'phi_sha256': res['phi_sha256'],
                   'background_pt': os.path.relpath(bgp), 'mesh': res['mesh'], 'grid': 'log-radius polar product mesh; s = log r (midpoint radii), theta = quarter-plane midpoint angles in (0, pi/2); fields on the first quadrant; quadrature weight base = 4 ws wth r^2',
                   'files': ['_s_fine.npy', '_theta_fine.npy', '_base_weights.npy', '_Fgrid_ij.npy', '_WFgrid_PS1_ij.npy', '_WFgrid_PS2_ij.npy'], 'tuples': res['tuples'], 'utc': res['utc']},
                  open(savep+'_fields.json', 'w'), indent=1)
        print('saved longdouble fields with prefix', savep, flush=True)
    # per-radius rms of F_xx (P-S1 weighted gxx) in both precisions
    gb, gl = g2[('P-S1', 'binary64')][0], g2[('P-S1', 'longdouble')][0].astype(np.float64)
    for rv in [0.3, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 20.0, 32.0, 50.0, 150.0]:
        i = int(np.argmin(np.abs(r-rv))); rms = lambda a: float(math.sqrt(np.mean(a[i]**2)))
        res['rows'].append({'r': float(r[i]), 'rms_WFxx_binary64': rms(gb), 'rms_WFxx_longdouble': rms(gl), 'rms_diff': rms(gb-gl)})
        print(f'r = {r[i]:8.3f}: rms W F_xx binary64 {rms(gb):.4e}  longdouble {rms(gl):.4e}  diff {rms(gb-gl):.3e} ({100*rms(gb-gl)/max(rms(gb),1e-300):.0f} percent)', flush=True)
    json.dump(res, open(outp, 'w'), indent=1); print('written', outp, flush=True)

if __name__ == '__main__': main()
