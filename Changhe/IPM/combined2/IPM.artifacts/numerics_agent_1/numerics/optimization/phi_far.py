"""phi_far.py (lane numerics_agent_1): exact far-field sector table of the corrected residual F_* = F(rho_C + h_phi) and the far part of its weighted norms.
The correction's exterior expansion is exact: an atom a r^(n+2h) (1+r^2)^b (t+r^2)^(-d) P_k(2 ts - 1) sin(n theta) is, for r > max(1, sqrt t), the series
sum_j phi_j r^(tau - 2j) sin(n theta) with rational phi_j (generalized binomials of b, of -d with t^j, and the Legendre polynomial of (1 - t u)/(1 + t u), u = r^-2).
Density h = -Delta phi: Delta(r^s sin n theta) = (s^2 - n^2) r^(s-2) sin n theta.  Stream function psi_h = phi_x (so that U[h] = (-psi_y, psi_x)):
d_x(r^s sin n theta) = r^(s-1) [ (s-n)/2 sin((n+1) theta) + (s+n)/2 sin((n-1) theta) ].
These density and stream tails enter ipm_exact.residual_sectors as extra_density (exact mpq), which returns the exact sector table of F_*: exponent -> sine dict,
with every cross term (advection of each density class by each stream class).  Far part of E_0 = ||W F_*||^2 on r >= R_far by exact angular orthogonality and
numerical radial quadrature of the finite sector sum (no cancellation of raw generator sums).
CLI: phi_far.py <base_exact_json> <phi_json> <out_json> [Fstar_mesh_npy s_npy bg_pt] [qmax] [exp_min] [R_far]"""
import sys, os, json, math, time
import numpy as np
from gmpy2 import mpq, mpz
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import phi_fit as PF
TUPLES = PF.TUPLES

def gen_binom(b, j):
    """generalized binomial coefficient C(b, j) for rational b"""
    out = mpq(1)
    for i in range(j): out = out*(b-i)/(i+1)
    return out

def ser_mul(A, B, J):
    out = [mpq(0)]*(J+1)
    for i, a in enumerate(A):
        if a == 0: continue
        for j, bb in enumerate(B):
            if i+j > J: break
            out[i+j] += a*bb
    return out

def exterior_series(at, J):
    """coefficients phi_j (mpq), j = 0..J, of the atom's unit exterior expansion sum_j phi_j r^(tau - 2j) (tau = n + 2h + 2b - 2d)"""
    b, t, d, k = at['b'], at['t'], at['d'], at.get('k_leg', 0)
    A = [gen_binom(b, j) for j in range(J+1)]                       # (1 + u)^b, u = r^-2
    B = [gen_binom(mpq(-d), j)*t**j for j in range(J+1)]            # (1 + t u)^(-d)
    S = ser_mul(A, B, J)
    if k > 0:
        # y = (1 - t u)/(1 + t u) = (1 - t u) sum_j (-t u)^j
        inv = [(-t)**j for j in range(J+1)]
        y = ser_mul([mpq(1), -t]+[mpq(0)]*(J-1), inv, J)
        P0 = [mpq(1)]+[mpq(0)]*J; P1 = y
        for kk in range(1, k):
            P0, P1 = P1, [((2*kk+1)*v1-kk*v0)/(kk+1) for v1, v0 in zip(ser_mul(y, P1, J), P0)]
        S = ser_mul(S, P1 if k >= 1 else P0, J)
    return S

def correction_tails(atoms, coefs, J=6):
    """exact density and stream tail sectors of the correction: dict alpha(mpq) -> ({N: c}, {N: c}) for density (exponent alpha) and stream (exponent alpha + 1)"""
    dens = {}; strm = {}
    for at, a in zip(atoms, coefs):
        if a == 0: continue
        n = at['n']; tau = at['n']+2*at['h']+2*at['b']-2*at['d']
        for j, pj in enumerate(exterior_series(at, J)):
            if pj == 0: continue
            s = tau-2*j; c = a*pj
            alpha = s-2                                              # density exponent
            D = dens.setdefault(alpha, {}); D[n] = D.get(n, mpq(0))-(s*s-n*n)*c
            P = strm.setdefault(alpha, {})                           # stream function psi_h = phi_x at exponent s - 1 = alpha + 1 (keyed by the density exponent as ipm_exact does: strm[alpha] has exponent alpha + 1)
            P[n+1] = P.get(n+1, mpq(0))+(s-n)/2*c
            if n-1 >= 1: P[n-1] = P.get(n-1, mpq(0))+(s+n)/2*c
            elif n-1 == 0: pass                                      # sin(0) = 0
    return dens, strm

def main():
    base_json, phi_json, out_json = sys.argv[1:4]
    fmesh = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] != 'none' else None; smesh = sys.argv[5] if len(sys.argv) > 5 else None; bgpt = sys.argv[6] if len(sys.argv) > 6 else None
    qmax = int(sys.argv[7]) if len(sys.argv) > 7 else 4; exp_min = mpq(sys.argv[8]) if len(sys.argv) > 8 else mpq(-8); R_far = float(sys.argv[9]) if len(sys.argv) > 9 else 300.0
    t0 = time.time()
    c, gens, coefs_q, Jb = OPT.load_candidate_json(base_json)
    terms = X.generators_to_terms(c, [dict(g, coef=q) for g, q in zip(gens, coefs_q)])
    Jp = json.load(open(phi_json)); atoms, _ = PF.atoms_from_json(Jp); coefs = [mpq(at['coefficient_exact']) for at in Jp['atoms']]
    dens_c, strm_c = correction_tails(atoms, coefs)
    extra = [(alpha, dens_c[alpha], strm_c.get(alpha, {})) for alpha in dens_c]
    print(f'correction tails: {len(extra)} density exponents from {float(min(dens_c))} to {float(max(dens_c))}; {time.time()-t0:.0f} s', flush=True)
    E_base, dens_b, strm_b, mom = X.residual_sectors(c, terms, qmax, exp_min=exp_min)
    print(f'base sectors done ({len([e for e in E_base if E_base[e]])} nonzero classes); {time.time()-t0:.0f} s', flush=True)
    E_star, dens_s, strm_s, _ = X.residual_sectors(c, terms, qmax, extra_density=extra, exp_min=exp_min)
    print(f'corrected sectors done ({len([e for e in E_star if E_star[e]])} nonzero classes); {time.time()-t0:.0f} s', flush=True)
    def tofloat(E): return sorted([(X.qfloat(e), {int(N): X.qfloat(v) for N, v in S.items() if v != 0}) for e, S in E.items() if S], key=lambda kv: -kv[0])
    Eb = tofloat(E_base); Es = tofloat(E_star)
    def toexact(E): return sorted([(str(e), {int(N): str(v) for N, v in S.items() if v != 0}) for e, S in E.items() if S], key=lambda kv: -float(mpq(kv[0])))
    Eb_exact = toexact(E_base); Es_exact = toexact(E_star)
    # far-field energies on r >= R_far: per mode N, f_N(r) = sum_e s_(e,N) r^e; E0 = pi sum_N int W^2 f_N^2 r dr; plain L2 the same with W = 1
    rr = np.geomspace(R_far, 1e9, 4000); dlogr = np.log(rr[1]/rr[0])
    def energies(Ef):
        Nset = sorted({N for _, S in Ef for N in S}); out = {'L2': 0.0}
        for name in TUPLES: out['E0_'+name] = 0.0
        modeE0 = {}
        for N in Nset:
            f = np.zeros_like(rr)
            for e, S in Ef:
                if N in S: f += S[N]*rr**e
            w = rr*rr*dlogr                         # r dr = r^2 dlog r
            out['L2'] += math.pi*float(np.sum(f*f*w))
            for name, (sig, r0) in TUPLES.items():
                v = math.pi*float(np.sum((1+rr*rr/r0**2)**sig*f*f*w)); out['E0_'+name] += v; modeE0.setdefault(name, {})[N] = v
        out['mode_shares_E0_P-S2'] = {int(N): v/out['E0_P-S2'] for N, v in sorted(modeE0['P-S2'].items(), key=lambda kv: -kv[1])[:8]} if out['E0_P-S2'] > 0 else {}
        # convergence check: the last decade's share
        return out
    en_b = energies(Eb); en_s = energies(Es)
    # the float sector sums cancel catastrophically at moderate r (coefficients up to 1e11 against values of 1e-9); energies from larger R_far are the reliable ones
    en_alt = {}
    for Rf in (3000.0, 10000.0, 30000.0):
        rr = np.geomspace(Rf, 1e9, 4000); dlogr = np.log(rr[1]/rr[0]); en_alt[str(Rf)] = {'base': energies(Eb), 'star': energies(Es)}
    rr = np.geomspace(R_far, 1e9, 4000); dlogr = np.log(rr[1]/rr[0])
    res = {'sector_table_base': [(e, S) for e, S in Eb], 'sector_table_star': [(e, S) for e, S in Es], 'sector_table_base_exact': Eb_exact, 'sector_table_star_exact': Es_exact, 'far_energies_from_R': en_alt,'base_json': os.path.basename(base_json), 'phi_json': os.path.basename(phi_json), 'phi_sha256': sha256_file(phi_json), 'qmax': qmax, 'exp_min': str(exp_min), 'R_far': R_far, 'r_max_quadrature': 1e9,
           'sectors_base': [(e, len(S)) for e, S in Eb], 'sectors_star': [(e, len(S)) for e, S in Es],
           'leading_star_class': {'exponent': Es[0][0], 'coefficients': Es[0][1]} if Es else None,
           'leading_base_class': {'exponent': Eb[0][0], 'coefficients': Eb[0][1]} if Eb else None,
           'far_energies_base': en_b, 'far_energies_star': en_s,
           'label': 'exact sector table (rational) of F_* with the correction tails as extra sectors; energies are float quadratures of the finite sector sums on r >= R_far (no raw-sum cancellation); FLOAT'}
    # validation and combination with the mesh near part
    if fmesh and bgpt:
        import torch
        F = np.load(fmesh); s = np.load(smesh); r = np.exp(s); bg = torch.load(bgpt, weights_only=False); th = bg['mesh']['theta'].numpy(); ws = bg['mesh']['ws'].numpy(); wth = bg['mesh']['wth'].numpy()
        F0 = bg['F0'][(0, 0)].numpy()
        def sector_field(Ef, rsel):
            out = np.zeros((rsel.sum(), len(th)))
            for e, S in Ef:
                ang = np.zeros(len(th))
                for N, v in S.items(): ang += v*np.sin(N*th)
                out += (r[rsel]**e)[:, None]*ang[None, :]
            return out
        val = {}
        for (lo, hi) in ((300, 1000), (1000, 3000), (3000, 10000)):
            sel = (r >= lo) & (r < hi)
            Fb_sec = sector_field(Eb, sel); Fs_sec = sector_field(Es, sel)
            val[f'[{lo},{hi})'] = {'base_mesh_rms': float(np.sqrt((F0[sel]**2).mean())), 'base_sector_rms': float(np.sqrt((Fb_sec**2).mean())), 'base_rel_rms_diff': float(np.sqrt(((F0[sel]-Fb_sec)**2).mean())/np.sqrt((Fb_sec**2).mean())),
                                   'star_mesh_rms': float(np.sqrt((F[sel]**2).mean())), 'star_sector_rms': float(np.sqrt((Fs_sec**2).mean())), 'star_rel_rms_diff': float(np.sqrt(((F[sel]-Fs_sec)**2).mean())/np.sqrt((Fs_sec**2).mean()))}
        res['validation_mesh_vs_sectors'] = val
        base_w = 4*np.outer(ws*r**2, wth); near = r < R_far
        comb = {}
        for name, (sig, r0) in TUPLES.items():
            W2 = (1+r**2/r0**2)**sig
            e0_near = float((base_w[near]*W2[near, None]*F[near]**2).sum()); e0_far_mesh = float((base_w[~near]*W2[~near, None]*F[~near]**2).sum())
            comb[name] = {'E0_near_mesh': e0_near, 'E0_far_mesh_raw': e0_far_mesh, 'E0_far_sectors': en_s['E0_'+name], 'E0_combined': e0_near+en_s['E0_'+name]}
        l2_near = float((base_w[near]*F[near]**2).sum()); comb['L2'] = {'near_mesh': l2_near, 'far_mesh_raw': float((base_w[~near]*F[~near]**2).sum()), 'far_sectors': en_s['L2'], 'G0_combined': math.sqrt(l2_near+en_s['L2'])}
        res['combined_with_mesh_near_part'] = comb
    json.dump(res, open(out_json, 'w'), indent=1, default=str)
    print(json.dumps({k: res[k] for k in ('far_energies_base', 'far_energies_star', 'validation_mesh_vs_sectors', 'combined_with_mesh_near_part') if k in res}, indent=1, default=str)); print('total %.0f s' % (time.time()-t0))

if __name__ == '__main__':
    main()
