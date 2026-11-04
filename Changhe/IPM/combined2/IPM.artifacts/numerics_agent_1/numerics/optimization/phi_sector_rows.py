"""phi_sector_rows.py (lane numerics_agent_1): linear far-field sector rows for the correction fit ("far field first", coordinator 03:15Z item 7).
For the leading far-field classes alpha (exact exponents) of the corrected residual F_* = F_C + L_C h + U[h].grad h, the sine coefficient s_(alpha,N) of F_* is
  s_(alpha,N) = s^C_(alpha,N) + sum_m a_m R_m(alpha, N) + (quadratic correction-correction terms, exponents <= 2e - 1 = -6.58, absent above the cutoff),
with R_m the contribution of the unit atom m: dilation term (c alpha - 1) x (density tail of the atom at alpha) plus the advection cross terms of the atom's density
tail by the base's stream classes and of the base's density classes by the atom's stream tail (the algebra of ipm_exact.residual_sectors, here in binary64 from exact
tail coefficients).  Rows: for every class alpha >= alpha_min and mode N: sum_m a_m R_m(alpha, N) = -s^C_(alpha, N)  (cancellation of the far-field class).
Output: npz with C (rows x atoms), b (rows), the class exponents and modes, plus the base coefficients; exact certification of the frozen result is numerical_audit's
(residual_sectors with extra_density, as in phi_far.py).
CLI: phi_sector_rows.py <base_exact_json> <cfg_json> <out_npz> [alpha_min] [qmax_base]"""
import sys, os, json, math, time, pickle
import numpy as np
from gmpy2 import mpq
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import phi_fit as PF, phi_far as PFAR

def sin_times_cos(S, Cc):
    o = np.zeros(len(S)+len(Cc)+1)
    nzS = np.nonzero(S)[0]; nzC = np.nonzero(Cc)[0]
    for a in nzS:
        v = S[a]*Cc[nzC]/2
        np.add.at(o, a+nzC, v)
        d = a-nzC; pos = d > 0; neg = d < 0
        np.add.at(o, d[pos], v[pos]); np.add.at(o, -d[neg], -v[neg])
    return o
def advect(Phi, sigma, G, alpha):
    dG = np.arange(len(G))*G; dPhi = np.arange(len(Phi))*Phi
    t1 = sin_times_cos(Phi, dG); t2 = sin_times_cos(G, dPhi)
    n = max(len(t1), len(t2)); o = np.zeros(n); o[:len(t1)] += sigma*t1; o[:len(t2)] -= alpha*t2
    return o
def to_arr(d, L):
    a = np.zeros(L)
    for N, v in d.items():
        if int(N) < L: a[int(N)] = float(v)
    return a

def main():
    base_json, cfg_json, out_npz = sys.argv[1:4]; alpha_min = mpq(sys.argv[4]) if len(sys.argv) > 4 else mpq(-9, 2); qmax = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    t0 = time.time()
    c, gens, coefs_q, Jb = OPT.load_candidate_json(base_json); cf = float(c)
    cache = out_npz.replace('.npz', f'_base_q{qmax}.pkl')
    if os.path.exists(cache):
        E_b, dens_b, strm_b = pickle.load(open(cache, 'rb'))
    else:
        terms = X.generators_to_terms(c, [dict(g, coef=q) for g, q in zip(gens, coefs_q)])
        E_b, dens_b, strm_b, _ = X.residual_sectors(c, terms, qmax, exp_min=alpha_min-1)
        pickle.dump((E_b, dens_b, strm_b), open(cache, 'wb'))
    print(f'base sectors (qmax {qmax}): {len([e for e in E_b if E_b[e]])} residual classes, {len(dens_b)} density classes; {time.time()-t0:.0f} s', flush=True)
    cfg = json.load(open(cfg_json)); atoms = PF.make_atoms(cfg); n = len(atoms)
    L = 2*max(at['n'] for at in atoms)+8
    densb = {al: to_arr(G, L) for al, G in dens_b.items() if G}; strmb = {al: to_arr(P, L) for al, P in strm_b.items() if P}
    # rows: dict (alpha mpq) -> dict N -> dict m -> value  (sparse)
    rows = {}
    def addrow(al, arr, m):
        if al < alpha_min: return
        R = rows.setdefault(al, {})
        for N in np.nonzero(arr)[0]:
            R.setdefault(int(N), {})[m] = R.get(int(N), {}).get(m, 0.0)+float(arr[N])
    for m, at in enumerate(atoms):
        nmode = at['n']; tau = at['n']+2*at['h']+2*at['b']-2*at['d']
        ser = PFAR.exterior_series(at, 3)
        for j, pj in enumerate(ser):
            s = tau-2*j; al = s-2
            if al < alpha_min or pj == 0: continue
            dcoef = -float((s*s-nmode*nmode)*pj)                 # density tail coefficient at exponent al, mode nmode
            D = np.zeros(L); D[nmode] = dcoef
            P = np.zeros(L); P[nmode+1] = float((s-nmode)/2*pj)
            if nmode-1 >= 1: P[nmode-1] = float((s+nmode)/2*pj)
            # dilation
            addrow(al, (cf*float(al)-1)*D, m)
            # cross terms: base stream (keyed by density exponent ab, stream exponent ab + 1) advecting the atom's density; the atom's stream (exponent al + 1) advecting base densities
            for ab, Phi in strmb.items():
                ex = ab+al-1
                if ex < alpha_min: continue
                addrow(ex, advect(Phi, float(ab)+1, D, float(al)), m)
            for ab, G in densb.items():
                ex = al+ab-1
                if ex < alpha_min: continue
                addrow(ex, advect(P, float(al)+1, G, float(ab)), m)
        if m % 2000 == 0: print(f'  atom {m}/{n} {time.time()-t0:.0f} s', flush=True)
    # assemble dense rows for (alpha, N) with any atom contribution or a nonzero base coefficient
    Eb = {al: to_arr(S, L) for al, S in E_b.items() if S}
    classes = sorted(set(rows.keys())|{al for al in Eb if al >= alpha_min}, key=lambda q: -q)
    Cr = []; bv = []; meta = []
    for al in classes:
        R = rows.get(al, {}); base_arr = Eb.get(al, np.zeros(L))
        Ns = sorted(set(R.keys())|set(np.nonzero(base_arr)[0].tolist()))
        for N in Ns:
            row = np.zeros(n)
            for m, v in R.get(N, {}).items(): row[m] = v
            if not row.any():
                meta.append((str(al), float(al), N, float(base_arr[N]), 'uncancellable: no atom contributes')); continue
            Cr.append(row); bv.append(-float(base_arr[N])); meta.append((str(al), float(al), N, float(base_arr[N]), 'row'))
    C = np.array(Cr); b = np.array(bv)
    unc = [mm for mm in meta if mm[4] != 'row']
    np.savez(out_npz, C=C, b=b, classes=np.array([mm[0] for mm in meta if mm[4] == 'row']), class_float=np.array([mm[1] for mm in meta if mm[4] == 'row']), modes=np.array([mm[2] for mm in meta if mm[4] == 'row']), base_coef=np.array([mm[3] for mm in meta if mm[4] == 'row']), alpha_min=str(alpha_min), qmax=qmax, n_atoms=n, cfg=cfg_json, base=os.path.basename(base_json))
    print(f'rows: {C.shape[0]} (classes {len(classes)}: {[round(float(a), 4) for a in classes]}); uncancellable base coefficients (no atom): {len(unc)}, largest |coef| {max([abs(mm[3]) for mm in unc], default=0):.3e}; {time.time()-t0:.0f} s -> {out_npz}')
    print('base coefficient norms per class (rows):', {round(float(al), 4): round(float(np.sqrt(sum(float(Eb.get(al, np.zeros(L))[N])**2 for N in range(L)))), 3) for al in classes})

if __name__ == '__main__':
    main()
