"""phi_fit.py (lane numerics_agent_1): exact odd-potential correction fit (numerical_audit AT-119 class, coordinator 2026-11-02T22:17Z item 3a / 23:19Z item 4b / 23:43Z item 3a).
Center: an exact campaign-basis candidate C (Candidate 007 itself or C5 = C2-N2-002-c5-comb-ps1); correction h = -Delta phi with
  phi = sum_m a_m r^(n_m + 2 h_m) (1+r^2)^(b_m) (t_m + r^2)^(-d_m) sin(n_m theta),   tau_m = n_m + 2h_m + 2b_m - 2d_m <= mu = 4/c - 3,
velocity v = U[h] = (-phi_xy, phi_xx) (exact, PROOF.md).  Residual of the corrected center rho_C + h:
  F_* = F_C + [V_C . grad h - h + v . grad rho_C] + v . grad h,   V_C = c X + u_C,
quadratic in a.  Objective: ||F_*||_2^2 + sum_tuples wS ||<D>^2 (W F_*)||_2^2 with W = (1 + r^2/r0^2)^(sigma/2) (P-S1: sigma 1, r0 1/2; P-S2: 7/5, 1), on the
product mesh (0.02 <= r <= 1e4, four quadrants).  One exact linear constraint: A + 3B = 0 (ell(h) = 0, PROOF.md (2)); a_* = a_0(C) - 8A reported.
Gauss-Newton with eigen-filtered damping in the constraint null space and the exact quartic line search.  Start: per-mode radial least squares of h to
numerics_agent_2's converged grid h (sine modes on a log-r grid).  Freeze: dyadic rationals, normalizer atom coefficient solved exactly from A + 3B = 0, JSON in the
schema of numerical_audit SCOPE_v01.md (normalizer_b_v01.json).  Everything FLOAT except the exact identities of the frozen file.
CLI: bg <cand_json> <mid> <ang> <out.pt>          build and cache the background fields of C on the mesh
     fit <cfg.json>                                run a fit (configuration file: see make_default_config)
     eval <phi.json> <bg.pt> <out_json> [field_npy] evaluate a frozen correction on the cached mesh (norms, F_* polar field for the FFT N_q routine)
     selftest                                      Jacobian / line-search / origin consistency on a small 007-quotient mesh"""
import sys, os, json, time, math, hashlib
import numpy as np, torch
from fractions import Fraction
from gmpy2 import mpq, mpz
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_optn1 as ON1
import phi_atoms as PA
import phi_honest as PH
import ipm_polar as PL
from exact_origin import exact_origin
DT = torch.float64
DERIVS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
LEIB = O2.LEIB
C_EXACT = mpq('4076476460239181/2251799813685248'); MU = 4/C_EXACT-3; E_EXP = MU-2
TUPLES = {'P-S1': (1.0, 0.5), 'P-S2': (1.4, 1.0)}      # (sigma, r0) of the weights W = (1 + r^2/r0^2)^(sigma/2)

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def q2s(q): return str(mpq(q))

# ------------------------------------------------------------------ atoms
def make_atoms(cfg):
    """atom list from a config: for each odd n in modes: mu branch (tau = mu - 2k) and harmonic branch (tau = -n - 2k) with the given (h, d, t) sets.
    b is fixed by the degree rule: b = (tau - n - 2h + 2d)/2 (exact rational).  The AN-045 normalizer atom (n 3, h 0, b -2, t 1, d 0) is always atom 0."""
    atoms = [dict(n=3, h=0, b=mpq(-2), t=mpq(1), d=0, branch='normalizer', k=0)]
    seen = {(3, 0, mpq(-2), mpq(1), 0)}
    GAMMA = 1/C_EXACT; DELTA = 1-GAMMA
    for grp in cfg['groups']:
        if grp.get('lattice'):
            # far-field lattice tails: for each residual sector class (J, Q) with exponent alpha = gamma - J delta - 2Q < e, atoms with tau = alpha + 2
            # (rational, <= mu), so that h ~ r^alpha sin(n theta) can cancel the base residual's surviving sectors below e (the class allows any rational tau <= mu)
            for (Jc, Qc) in grp['JQ']:
                alpha = GAMMA-Jc*DELTA-2*Qc; tau = alpha+2; assert tau <= MU and tau != MU, (Jc, Qc)
                for n in grp['modes']:
                    for var in grp['variants']:
                        hh, d = var.get('h', 0), var.get('d', 0)
                        for t in (var.get('t', ['1']) if d > 0 else ['1']):
                            tq = mpq(t); b = (tau-n-2*hh+2*d)/2; dd = d
                            if tq == 1: b, dd = b-d, 0
                            key = (n, hh, b, tq, dd)
                            if key in seen: continue
                            seen.add(key); atoms.append(dict(n=n, h=hh, b=b, t=tq, d=dd, branch=f'lattice({Jc},{Qc})', k=0))
            continue
        if grp.get('leg'):
            # Legendre-modulated family per (mode, scale): r^n (t+r^2)^(-Q) (1+r^2)^b P_k(2 ts - 1), k = 0..K, ts = r^2/(t+r^2); same span as the 'poly' family,
            # evaluated stably; the exact expansion into elementary atoms (ts^j = r^(2j) (t+r^2)^(-j)) is done at freeze time
            for n in grp['modes']:
                for br, ks in (('mu', grp.get('k_mu', [0])), ('harm', grp.get('k_harm', []))):
                    for kk in ks:
                        tau = MU-2*kk if br == 'mu' else mpq(-n-2*kk)
                        Q = (n+1)//2+grp.get('Qextra', 0)
                        for t in grp['t']:
                            tq = mpq(t); assert tq != 1, 'Legendre atoms need t != 1 (t = 1 folds into b)'
                            b = (tau-n+2*Q)/2
                            for k in range(grp['K']+1):
                                key = (n, 0, b, tq, Q, k)
                                if key in seen: continue
                                seen.add(key); atoms.append(dict(n=n, h=0, b=b, t=tq, d=Q, branch=br+'-leg', k=kk, k_leg=k))
            continue
        if grp.get('poly'):
            # polynomial family per (mode, scale): r^(n+2j) (t+r^2)^(-(j+Q)) (1+r^2)^b, j = 0..K, Q = ceil((n+1)/2) + Qextra, b from the degree rule
            # (a Legendre basis in ts = r^2/(t+r^2) spans the same space; the SVD with column scaling handles the monomial conditioning)
            for n in grp['modes']:
                for br, ks in (('mu', grp.get('k_mu', [0])), ('harm', grp.get('k_harm', []))):
                    for k in ks:
                        tau = MU-2*k if br == 'mu' else mpq(-n-2*k)
                        Q = (n+1)//2+grp.get('Qextra', 0)
                        for t in grp['t']:
                            for j in range(grp['K']+1):
                                tq = mpq(t); d = j+Q; hh = j; b = (tau-n-2*hh+2*d)/2
                                if tq == 1: b, d = b-d, 0
                                key = (n, hh, b, tq, d)
                                if key in seen: continue
                                seen.add(key); atoms.append(dict(n=n, h=hh, b=b, t=tq, d=d, branch=br+'-poly', k=k))
            continue
        for n in grp['modes']:
            for br, ks in (('mu', grp.get('k_mu', [0])), ('harm', grp.get('k_harm', []))):
                for k in ks:
                    tau = MU-2*k if br == 'mu' else mpq(-n-2*k)
                    for hh in grp.get('h', [0]):
                        # 'd' list: fixed d (steps / far bumps); 'p' list: bumps with inner slope n + 2h and outer slope -p below r = 1, d = ceil((n + 2h + p)/2)
                        dlist = list(grp.get('d', [])) + [int(math.ceil((n+2*hh+pp)/2)) for pp in grp.get('p', [])]
                        for d in dlist:
                            for t in (grp.get('t', ['1']) if d > 0 else ['1']):
                                tq = mpq(t); b = (tau-n-2*hh+2*d)/2; dd = d
                                if tq == 1: b, dd = b-d, 0                          # (1+s)^b (1+s)^(-d) = (1+s)^(b-d): fold, so that exact duplicates are removed
                                key = (n, hh, b, tq, dd)
                                if key in seen: continue
                                seen.add(key); atoms.append(dict(n=n, h=hh, b=b, t=tq, d=dd, branch=br, k=k))
    validate_atoms(atoms)
    return atoms

def validate_atoms(atoms):
    """class membership (PROOF.md): n positive odd integer, h and d nonnegative integers, t positive rational, b rational, tau <= mu exactly (a Legendre factor is degree 0 in r at both ends)"""
    for at in atoms:
        assert isinstance(at.get('k_leg', 0), int) and at.get('k_leg', 0) >= 0, at
        assert isinstance(at['n'], int) and at['n'] > 0 and at['n'] % 2 == 1, at
        assert isinstance(at['h'], int) and at['h'] >= 0 and isinstance(at['d'], int) and at['d'] >= 0, at
        assert isinstance(at['t'], type(mpq(1))) and at['t'] > 0 and isinstance(at['b'], type(mpq(1))), at
        assert at['n']+2*at['h']+2*at['b']-2*at['d'] <= MU, at

def shifted_legendre_coeffs(k):
    """P_k(2x - 1) = sum_j q_j x^j with q_j = (-1)^(k+j) C(k, j) C(k+j, j) (exact)"""
    return [mpq((-1)**(k+j)*math.comb(k, j)*math.comb(k+j, j)) for j in range(k+1)]

def elementary_expansion(at, coef=mpq(1)):
    """list of (coefficient, elementary atom dict) for an atom (Legendre-modulated or not)"""
    k = at.get('k_leg', 0)
    if k == 0: return [(coef, dict(n=at['n'], h=at['h'], b=at['b'], t=at['t'], d=at['d']))]
    return [(coef*q, dict(n=at['n'], h=at['h']+j, b=at['b'], t=at['t'], d=at['d']+j)) for j, q in enumerate(shifted_legendre_coeffs(k)) if q != 0]

def cubic_coeffs(at):
    """(A-coefficient, B-coefficient) of a unit atom (PROOF.md (2)), exact; Legendre atoms through their elementary expansion"""
    if at.get('k_leg', 0) > 0:
        cA = mpq(0); cB = mpq(0)
        for q, el in elementary_expansion(at):
            a_, b_ = cubic_coeffs(el); cA += q*a_; cB += q*b_
        return cA, cB
    return _cubic_coeffs_elem(at)

def _cubic_coeffs_elem(at):
    """(A-coefficient, B-coefficient) of a unit atom (PROOF.md (2)), exact"""
    n, hh, b, t, d = at['n'], at['h'], at['b'], at['t'], at['d']
    tp = t**(-d)
    cA = (tp*(b-d/t) if hh == 0 else (tp if hh == 1 else mpq(0))) if n == 1 else mpq(0)
    cB = tp if (n == 3 and hh == 0) else mpq(0)
    return cA, cB

def make_default_config():
    return {'background_pt': 'numerics/optimization/phi_bg/C5_mid24_ang180.pt', 'target_modes': 'numerics/h0_data/H0C_C5_750x80_inner2_converged_h_modes.npy',
            'target_s': 'numerics/h0_data/H0C_C5_750x80_inner2_s_coarse.npy', 'tag': 'phi_c5_a', 'steps': 60, 'lam0': 1e-6, 'tmax': 4.0,
            'wL2': 1.0, 'sobolev': {'P-S1': 0.0, 'P-S2': 0.0},
            'groups': [{'modes': list(range(1, 32, 2)), 'k_mu': [0, 1], 'k_harm': [0], 'h': [0, 1, 2], 'd': [0, 1, 3, 6], 't': ['1/64', '1/16', '1/4', '1', '4', '16', '64', '256']},
                       {'modes': list(range(33, 64, 2)), 'k_mu': [0], 'k_harm': [], 'h': [0, 1], 'd': [0, 1, 3], 't': ['1/4', '1', '4', '16']},
                       {'modes': list(range(65, 96, 2)), 'k_mu': [0], 'k_harm': [], 'h': [0, 1], 'd': [0, 2], 't': ['1', '4']}]}

# ------------------------------------------------------------------ background cache
def build_background(cand_json, mid, ang, out_pt, dev, rcut=0.02, rmax=1e4):
    t0 = time.time()
    c, gens, coefs_q, J = OPT.load_candidate_json(cand_json); assert mpq(c) == C_EXACT if not hasattr(c, 'numerator') else mpq(str(c)) == C_EXACT
    mesh = build_mesh(mid, ang, rcut, rmax, dev)
    prob = ON1.ProblemN1(gens, c, mesh, r_cut=rcut, r_max=rmax)
    a = np.array([X.qfloat(v) for v in coefs_q])
    Fd = prob.fields(a); comp = prob.F_components(Fd, DERIVS)
    org = exact_origin(cand_json)
    bg = {'rho': {d: Fd[('rho', d)].cpu() for d in Fd if False}, 'meta': {}}
    bg['rho'] = {k[1]: v.cpu() for k, v in Fd.items() if k[0] == 'rho'}
    bg['psi'] = {k[1]: v.cpu() for k, v in Fd.items() if k[0] == 'psi'}
    bg['F0'] = {d: comp[d].cpu() for d in DERIVS}
    G0 = math.sqrt(float(torch.sum(prob.base*comp[(0, 0)]**2)))
    bg['meta'] = {'cand_json': os.path.relpath(cand_json, LANE), 'cand_sha256': sha256_file(cand_json), 'n_generators': len(gens), 'mid': mid, 'ang': ang, 'rcut': rcut, 'rmax': rmax,
                  'Nr': mesh.Nr, 'Nt': mesh.Nt, 'a0_exact': org['a0_exact'], 'a0_float': org['a0_float'], 'G0_mesh': G0, 'build_s': time.time()-t0, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    bg['mesh'] = {'s': mesh.s.cpu(), 'ws': mesh.ws.cpu(), 'theta': mesh.theta.cpu(), 'wth': mesh.wth.cpu()}
    torch.save(bg, out_pt)
    print(f'background {os.path.basename(cand_json)} on {mesh.Nr} x {mesh.Nt}: G0 {G0:.8e}, a0 {org["a0_float"]}, keys rho {sorted(bg["rho"])} psi {sorted(bg["psi"])}, {time.time()-t0:.0f} s -> {out_pt}', flush=True)
    return bg

def load_background(pt, dev):
    bg = torch.load(pt, weights_only=False)
    m = bg['mesh']; mesh = EV.Mesh(m['s'].numpy(), m['ws'].numpy(), m['theta'].numpy(), m['wth'].numpy(), dev)
    for grp in ('rho', 'psi', 'F0'): bg[grp] = {k: v.to(dev) for k, v in bg[grp].items()}
    return bg, mesh

# ------------------------------------------------------------------ the fit problem
class PhiFit:
    def __init__(self, bg, mesh, atoms, wL2=1.0, sobolev=None, dmax_h=3, verbose=True, extra_l2_weights=None, sobolev_rmax=None):
        t0 = time.time()
        self.mesh, self.atoms, self.n = mesh, atoms, len(atoms); dev = mesh.device; self.dev = dev; self.dmax_h = dmax_h
        assert dmax_h >= 1 and (not sobolev or all(w == 0 for w in sobolev.values()) or dmax_h >= 3), 'Sobolev rows need dmax_h >= 3'
        self.c = float(C_EXACT); self.a0_bg = mpq(bg['meta']['a0_exact']); self.bg_meta = bg['meta']
        self.rho, self.F0 = bg['rho'], bg['F0']; psi = bg['psi']
        self.u1 = {d: -psi[(d[0], d[1]+1)] for d in DERIVS}; self.u2 = {d: psi[(d[0]+1, d[1])] for d in DERIVS}
        r = mesh.r[:, None]*torch.ones_like(mesh.W); self.x = r*mesh.cos[None, :]; self.y = r*mesh.sin[None, :]; self.r = r
        self.base = 4*mesh.W*r**2
        # atom slots
        self.gslots = [PA.atom_slots(at['n'], at['h'], at['b'], at['t'], at['d'], mesh, dmax_h=dmax_h, k=at.get('k_leg', 0)) for at in atoms]
        self.keys = list(self.gslots[0].keys())
        Nmax = max(N for sl in self.gslots for key in sl for (_, N, _) in sl[key]); self.tabs = PL.Tables(mesh, Nmax+1)
        self._build_fast()
        # exact constraint row A + 3B = 0
        self.cAB = [cubic_coeffs(at) for at in atoms]
        self.crow = np.array([float(cA+3*cB) for cA, cB in self.cAB])
        # rows: L2 plus Sobolev tuples
        self.rowspecs = [(wL2*self.base, {(0, 0): 1.0}, 'L2')] if wL2 > 0 else []
        self.sobolev = sobolev or {}
        for name, w in self.sobolev.items():
            if w > 0: self.rowspecs += self.sobolev_rows(w, *TUPLES[name], name, rmax=sobolev_rmax)
        for spec in (extra_l2_weights or []):           # weighted L2 rows ||W F_*||_2^2, W = (1 + r^2/r0^2)^(sigma/2): the E_0 part of N_2 at (sigma, r0), no derivatives needed; optional 4th entry rmin masks the rows to r >= rmin
            sig, r0, w = spec[:3]; rmin = spec[3] if len(spec) > 3 else None
            W2 = (1+self.r**2/r0**2)**sig
            if rmin is not None: W2 = W2*(self.r >= rmin).to(DT)
            self.rowspecs.append((w*self.base*W2, {(0, 0): 1.0}, f'WL2_s{sig}_r{r0}'+(f'_rmin{rmin:g}' if rmin else '')))
        assert self.rowspecs, 'no rows'
        self.sqw = [torch.sqrt(w) for w, _, _ in self.rowspecs]
        # radial rows whose weight vanishes identically (masked Sobolev rows beyond rmax) are dropped from the row vectors: row_keep[k] is a boolean radial mask or None
        self.row_keep = []
        for w, _, _ in self.rowspecs:
            nz = (w.abs().sum(1) > 0)
            self.row_keep.append(None if bool(nz.all()) else nz)
        self.build_time = time.time()-t0
        if verbose: print(f'PhiFit: {self.n} atoms, {len(self.rowspecs)} row types, mesh {mesh.Nr} x {mesh.Nt}, Nmax {Nmax}, build {self.build_time:.1f} s', flush=True)
    def weight_derivs(self, sig, r0):
        r = self.r; x, y = self.x, self.y
        A = 1+r**2/r0**2; W = A**(sig/2); W1 = sig*r/r0**2*A**(sig/2-1); W2 = sig/r0**2*A**(sig/2-1)+sig*(sig/2-1)*2*r**2/r0**4*A**(sig/2-2)
        Wx = W1*x/r; Wy = W1*y/r; Wxx = W2*x**2/r**2+W1*y**2/r**3; Wyy = W2*y**2/r**2+W1*x**2/r**3; Wxy = (W2-W1/r)*x*y/r**2
        return W, Wx, Wy, Wxx, Wxy, Wyy
    def sobolev_rows(self, w, sig, r0, name, rmax=None):
        """the six rows of ||<D>^2 (W F_*)||^2 (E_0 + 2E_1 + E_2) with weight w; rmax restricts the rows to r <= rmax (near-field second-derivative control at a fraction of the rows)"""
        W, Wx, Wy, Wxx, Wxy, Wyy = self.weight_derivs(sig, r0); base = self.base
        if rmax is not None: base = base*(self.r <= rmax).to(DT)
        return [(w*base, {(0, 0): W}, name), (2*w*base, {(1, 0): W, (0, 0): Wx}, name), (2*w*base, {(0, 1): W, (0, 0): Wy}, name),
                (w*base, {(2, 0): W, (1, 0): 2*Wx, (0, 0): Wxx}, name), (2*w*base, {(1, 1): W, (0, 1): Wx, (1, 0): Wy, (0, 0): Wxy}, name), (w*base, {(0, 2): W, (0, 1): 2*Wy, (0, 0): Wyy}, name)]
    def _build_fast(self):
        dev = self.dev; Nr = self.mesh.Nr; self.fast = {}
        for key in self.keys:
            per_typ = {}
            for i in range(self.n):
                for typ, N, arr in self.gslots[i][key]: per_typ.setdefault(typ, {}).setdefault(N, []).append((i, arr))
            self.fast[key] = {}
            for typ, slots in per_typ.items():
                Ns = sorted(slots); S = len(Ns); C = max(len(slots[N]) for N in Ns)
                Ms = []; Is = np.zeros((S, C), dtype=np.int64)
                for s_, N in enumerate(Ns):
                    cols = torch.stack([arr for _, arr in slots[N]], 1)
                    if cols.shape[1] < C: cols = torch.cat([cols, torch.zeros(Nr, C-cols.shape[1], dtype=DT, device=dev)], 1)
                    Ms.append(cols); Is[s_, :len(slots[N])] = [i for i, _ in slots[N]]
                self.fast[key][typ] = (torch.stack(Ms, 0), torch.as_tensor(Is, device=dev), self.tabs.tab[typ][torch.as_tensor(Ns, device=dev)])
    # ---- fields of a state and field matrices of all atoms on a radial chunk
    def fields(self, a):
        at = torch.as_tensor(np.asarray(a, float), dtype=DT, device=self.dev); out = {}
        for key in self.keys:
            tot = torch.zeros(self.mesh.Nr, self.mesh.Nt, dtype=DT, device=self.dev)
            for typ, (M, I, T) in self.fast[key].items(): tot += torch.einsum('snc,sc->sn', M, at[I]).T@T
            out[key] = tot
        return out
    def key_matrix(self, key, rs):
        nr = rs.stop-rs.start; Nt = self.mesh.Nt
        out = torch.zeros(nr*Nt, self.n, dtype=DT, device=self.dev)
        for typ, (M, I, T) in self.fast[key].items():
            S, _, C = M.shape
            outer = M[:, rs, :][:, :, None, :]*T[:, None, :, None]                      # (S, nr, Nt, C)
            out.index_add_(1, I.reshape(-1), outer.permute(1, 2, 0, 3).reshape(nr*Nt, S*C))
        return out.view(nr, Nt, self.n)
    # ---- residual components: F_* = F0 + lin(h, v) + quad(v, h)
    @staticmethod
    def _m(cf, f): return cf[..., None]*f if f.dim() == 3 else cf*f
    def lin(self, hf, vf, d, rs=slice(None)):
        """D^d [V_C . grad h - h + v . grad rho_C] for fields hf[(i,j)] (i+j <= 3), vf[('v1'/'v2', (i,j))] (i+j <= 2); state (2D) or atom-matrix (3D) fields"""
        i, j = d; c = self.c; m = self._m
        out = m(c*self.x[rs], hf[(i+1, j)])+m(c*self.y[rs], hf[(i, j+1)])+(c*(i+j)-1)*hf[(i, j)]
        for cf, d1, d2 in LEIB[d]:
            out = out+cf*(m(self.u1[d1][rs], hf[(d2[0]+1, d2[1])])+m(self.u2[d1][rs], hf[(d2[0], d2[1]+1)]))
            out = out+cf*(m(self.rho[(d2[0]+1, d2[1])][rs], vf[('v1', d1)])+m(self.rho[(d2[0], d2[1]+1)][rs], vf[('v2', d1)]))
        return out
    def quad(self, va, hb, d, rs=slice(None)):
        """D^d [va . grad hb]; one of the two may be an atom-matrix (3D) field"""
        m = lambda p, q: (p[..., None]*q if (q.dim() == 3 and p.dim() == 2) else (p*q[..., None] if (p.dim() == 3 and q.dim() == 2) else p*q))
        out = None
        for cf, d1, d2 in LEIB[d]:
            term = cf*(m(va[('v1', d1)], hb[(d2[0]+1, d2[1])])+m(va[('v2', d1)], hb[(d2[0], d2[1]+1)]))
            out = term if out is None else out+term
        return out
    @staticmethod
    def split(fld):
        hf = {k[1]: v for k, v in fld.items() if k[0] == 'h'}; vf = {k: v for k, v in fld.items() if k[0] != 'h'}
        return hf, vf
    @property
    def derivs(self):
        return [d for d in DERIVS if sum(d) <= self.dmax_h-1]
    def comps(self, a, fld=None):
        if fld is None: fld = self.fields(a)
        hf, vf = self.split(fld)
        comp = {d: self.F0[d]+self.lin(hf, vf, d)+self.quad(vf, hf, d) for d in self.derivs}
        return comp, fld
    def rows(self, comp, rs=slice(None)):
        out = []
        for k, (w, cd, _) in enumerate(self.rowspecs):
            sw = self.sqw[k][rs]; val = sw*sum((cd[d][rs] if torch.is_tensor(cd[d]) else cd[d])*comp[d][rs] for d in cd)
            keep = self.row_keep[k][rs] if self.row_keep[k] is not None else None
            out.append(val[keep] if keep is not None else val)
        return out
    def set_soft_rows(self, Cmat, bvec, weights, name='sector'):
        """soft exact-linear rows w_i (C_i a - b_i) added to the least squares (far-field sector cancellation with budget weights)"""
        self.linrows = (torch.as_tensor(Cmat, dtype=DT, device=self.dev), torch.as_tensor(bvec, dtype=DT, device=self.dev), torch.as_tensor(weights, dtype=DT, device=self.dev), name)
    def lin_values(self, a):
        if not hasattr(self, 'linrows'): return None
        Ct, bt, wt, _ = self.linrows; at = torch.as_tensor(np.asarray(a, float), dtype=DT, device=self.dev)
        return wt*(Ct@at-bt)
    def objective(self, a, fld=None):
        comp, fld = self.comps(a, fld); R = self.rows(comp)
        parts = {}
        for (w, cd, name), rv in zip(self.rowspecs, R): parts[name] = parts.get(name, 0.0)+float(torch.sum(rv*rv))
        lv = self.lin_values(a)
        if lv is not None: parts[self.linrows[3]] = float(torch.sum(lv*lv))
        return sum(parts.values()), parts, comp, fld
    # ---- longdouble (honest) residual of the L2 rows: the binary64 atom sum of the fitted state carries a roundoff floor (coefficients to 1e10 on atoms of size 2^-27; numerics_v06 N20)
    def honest_L2(self, a):
        """F_* on the mesh from the longdouble evaluation of the correction (CPU, numpy longdouble); binary64 array (Nr, Nt)"""
        if not hasattr(self, '_hbg'):
            m = self.mesh; cpu = lambda t: t.detach().cpu().numpy().astype(np.float64)
            self._hbg = {'r': cpu(m.r), 'theta': cpu(m.theta), 'bgf': {'x': cpu(self.x), 'y': cpu(self.y), 'F0': cpu(self.F0[(0, 0)]), 'rho_x': cpu(self.rho[(1, 0)]), 'rho_y': cpu(self.rho[(0, 1)]),
                         'psi_x': cpu(self.u2[(0, 0)]), 'psi_y': cpu(-self.u1[(0, 0)])}}
            self._hparams_fixed = [(int(at['n']), int(at['h']), str(at['b']), str(at['t']), int(at['d']), int(at.get('k_leg', 0))) for at in self.atoms]
        params = [(float(aj),)+fx for aj, fx in zip(np.asarray(a, float), self._hparams_fixed)]
        H = self._hbg
        return PH.honest_fields_fstar(params, H['r'], H['theta'], H['bgf'])
    def _hbg_base(self):
        if not hasattr(self, '_hbase'): self._hbase = self.base.detach().cpu().numpy().astype(np.float64)
        return self._hbase
    def _L2_row_slices(self, rchunk=16):
        """positions of the L2 rows inside the row vector of jacobian_full (same chunk layout)"""
        assert self.rowspecs[0][2] == 'L2' and self.row_keep[0] is None
        Nr, Nt = self.mesh.Nr, self.mesh.Nt; pos = 0; out = []
        for r0_ in range(0, Nr, rchunk):
            rs = slice(r0_, min(Nr, r0_+rchunk)); nr = rs.stop-rs.start
            out.append((rs, pos)); 
            for k, _ in enumerate(self.rowspecs):
                pos += (nr if self.row_keep[k] is None else int(self.row_keep[k][rs].sum()))*Nt
        return out
    def replace_L2_rows(self, rv, Fh):
        """overwrite the L2 rows of rv (binary64 residual rows) by sqrt(w) * Fh (longdouble F_* as binary64)"""
        Ft = torch.as_tensor(Fh, dtype=DT, device=self.dev); Nt = self.mesh.Nt
        for rs, pos in self._L2_row_slices():
            nr = rs.stop-rs.start; rv[pos:pos+nr*Nt] = (self.sqw[0][rs]*Ft[rs]).reshape(-1)
        return rv
    def objective_honest(self, a):
        """objective with the L2 part from the longdouble residual; returns (f, parts, comp, fld, Fh)"""
        f, parts, comp, fld = self.objective(a); Fh = self.honest_L2(a)
        w = self.rowspecs[0][0]; parts['L2'] = float(torch.sum(w*torch.as_tensor(Fh, dtype=DT, device=self.dev)**2))
        parts['L2_binary64'] = float(torch.sum(w*comp[(0, 0)]**2))
        return sum(v for k, v in parts.items() if k != 'L2_binary64'), parts, comp, fld, Fh
    # ---- Gauss-Newton normal equations over radial chunks
    def normal_equations(self, a, rchunk=16):
        comp, fld = self.comps(a); hf, vf = self.split(fld)
        n = self.n; Nr, Nt = self.mesh.Nr, self.mesh.Nt
        G = torch.zeros(n, n, dtype=DT, device=self.dev); g = torch.zeros(n, dtype=DT, device=self.dev); phi = 0.0
        for r0_ in range(0, Nr, rchunk):
            rs = slice(r0_, min(Nr, r0_+rchunk)); nr = rs.stop-rs.start
            rvec = torch.cat([x.reshape(-1) for x in self.rows(comp, rs)], 0); phi += float((rvec*rvec).sum())
            KM = {key: self.key_matrix(key, rs) for key in self.keys}
            hm = {k[1]: v for k, v in KM.items() if k[0] == 'h'}; vm = {k: v for k, v in KM.items() if k[0] != 'h'}
            hs = {k: v[rs] for k, v in hf.items()}; vs = {k: v[rs] for k, v in vf.items()}
            Md = {d: self.lin(hm, vm, d, rs)+self.quad(vm, hs, d, rs)+self.quad(vs, hm, d, rs) for d in self.derivs}
            del KM, hm, vm
            Jparts = []
            for k, (w, cd, _) in enumerate(self.rowspecs):
                M = None
                for d in cd:
                    cf = cd[d][rs][..., None] if torch.is_tensor(cd[d]) else cd[d]
                    M = cf*Md[d] if M is None else M+cf*Md[d]
                Mw = M*self.sqw[k][rs][..., None]
                if self.row_keep[k] is not None: Mw = Mw[self.row_keep[k][rs]]
                Jparts.append(Mw.reshape(-1, n))
            Jc = torch.cat(Jparts, 0); del Jparts, Md
            G += Jc.T@Jc; g += Jc.T@rvec
            del Jc
        return G, g, phi
    def gn_dirs(self, a, lams, G, g):
        """damped GN directions in the null space of the constraint row (eigen-filtered, column-scaled); the constraint violation is corrected too"""
        At = torch.as_tensor(self.crow[None, :], dtype=DT, device=self.dev); dt = torch.as_tensor([-(self.crow@a)], dtype=DT, device=self.dev)
        if not hasattr(self, '_null'):
            U, S, Vh = torch.linalg.svd(At, full_matrices=True); self._null = (U, S, Vh)
        U, S, Vh = self._null; rank = 1
        Vr = Vh[:rank]; Z = Vh[rank:].T
        dp = Vr.T@((U[:, :rank].T@dt)/S[:rank])
        GZ = Z.T@(G@Z); gZ = Z.T@(g+G@dp)
        colnorm = torch.sqrt(torch.diagonal(GZ).clamp(min=0)); colnorm[colnorm == 0] = 1
        GZs = GZ/colnorm[:, None]/colnorm[None, :]; gZs = gZ/colnorm
        evals, evecs = torch.linalg.eigh(GZs); proj = evecs.T@gZs
        out = []
        for lm in lams:
            dmp = evals+lm; keep = dmp > 0
            coef = torch.zeros_like(proj); coef[keep] = proj[keep]/dmp[keep]
            eta = -(evecs@coef)/colnorm; delta = dp+Z@eta
            out.append((delta.cpu().numpy(), float(-(2*delta@g+delta@(G@delta)))))
        return out
    def line_search(self, a, delta, tmax=4.0, honest_F=None):
        """exact quartic objective along a + t delta (F_* is quadratic in a); returns (t, phi(t), phi(0)).
        honest_F = (Fh(a), Fh(a+delta), Fh(a-delta)) longdouble L2 fields: the L2 rows of the three row lists are replaced by them (the binary64 increments carry
        the same roundoff as the residual itself, so a binary64 line search cannot see a decrease of the size of the floor)"""
        R0 = self.rows(self.comps(a)[0]); Rp = self.rows(self.comps(a+delta)[0]); Rm = self.rows(self.comps(a-delta)[0])
        if honest_F is not None:
            for R, Fh in zip((R0, Rp, Rm), honest_F): R[0] = self.sqw[0]*torch.as_tensor(Fh, dtype=DT, device=self.dev)
        if hasattr(self, 'linrows'): R0 = R0+[self.lin_values(a)]; Rp = Rp+[self.lin_values(a+delta)]; Rm = Rm+[self.lin_values(a-delta)]
        c = [0.0]*5
        for f0, fp, fm in zip(R0, Rp, Rm):
            L = (fp-fm)/2; Q = (fp+fm)/2-f0; ip = lambda u, v: float(torch.sum(u*v))
            c[0] += ip(f0, f0); c[1] += 2*ip(f0, L); c[2] += ip(L, L)+2*ip(f0, Q); c[3] += 2*ip(L, Q); c[4] += ip(Q, Q)
        phi = lambda t: c[0]+c[1]*t+c[2]*t*t+c[3]*t**3+c[4]*t**4
        roots = np.roots([4*c[4], 3*c[3], 2*c[2], c[1]]) if c[4] != 0 else np.roots([3*c[3], 2*c[2], c[1]])
        cands = [float(rt.real) for rt in roots if abs(rt.imag) < 1e-9*max(1.0, abs(rt.real)) and 0 < rt.real <= tmax]+list(np.geomspace(1e-5, tmax, 400))
        tb = min(cands, key=phi)
        if not (phi(tb) < c[0]*(1-1e-12)): tb = 0.0
        return tb, phi(tb), c[0], c
    # ---- reports
    def exact_AB(self, a_exact):
        A = sum(q*cA for q, (cA, cB) in zip(a_exact, self.cAB)); B = sum(q*cB for q, (cA, cB) in zip(a_exact, self.cAB))
        return A, B
    def n2_weighted(self, comp, sig, r0):
        W, Wx, Wy, Wxx, Wxy, Wyy = self.weight_derivs(sig, r0); F = comp[(0, 0)]
        g = W*F; gx = W*comp[(1, 0)]+Wx*F; gy = W*comp[(0, 1)]+Wy*F
        gxx = W*comp[(2, 0)]+2*Wx*comp[(1, 0)]+Wxx*F; gxy = W*comp[(1, 1)]+Wx*comp[(0, 1)]+Wy*comp[(1, 0)]+Wxy*F; gyy = W*comp[(0, 2)]+2*Wy*comp[(0, 1)]+Wyy*F
        E0 = float(torch.sum(self.base*g**2)); E1 = float(torch.sum(self.base*(gx**2+gy**2))); E2 = float(torch.sum(self.base*(gxx**2+2*gxy**2+gyy**2)))
        return {'N2': math.sqrt(E0+2*E1+E2), 'E0': E0, 'E1': E1, 'E2': E2, 'sup_WF': float(g.abs().max())}
    def bg_margins(self, fld):
        """BG-3 type margins of the CORRECTED background (eval_bg2.py convention, theory_agent_1 screen matrix): beta = -max lambda_max(q Sym DV_* + Kmat_* - (c + 1 + sigma V_*.X/(r0^2 + r^2)) I)
        with V_* = cX + u_C + U[h_phi], Kmat_* = [[-d_y rho_*, d_x rho_*/2], [d_x rho_*/2, 0]], rho_* = rho_C + h_phi; mesh values (0.02 <= r <= 1e4), min(mesh, origin cap) is the quotable number.  FLOAT."""
        hf, vf = self.split(fld); cf = self.c; r = self.r; cs = self.x/r; sn = self.y/r
        u1 = self.u1[(0, 0)]+vf[('v1', (0, 0))]; u2 = self.u2[(0, 0)]+vf[('v2', (0, 0))]
        u1x = self.u1[(1, 0)]+vf[('v1', (1, 0))]; u1y = self.u1[(0, 1)]+vf[('v1', (0, 1))]; u2x = self.u2[(1, 0)]+vf[('v2', (1, 0))]; u2y = self.u2[(0, 1)]+vf[('v2', (0, 1))]
        rx = self.rho[(1, 0)]+hf[(1, 0)]; ry = self.rho[(0, 1)]+hf[(0, 1)]
        s11 = cf+u1x; s22 = cf+u2y; s12 = 0.5*(u1y+u2x); k11 = -ry; k12 = 0.5*rx; e = cf+(u1*cs+u2*sn)/r
        out = {}
        for name, q, sig, r0 in (('P-S1', 2.1, 1.0, 0.5), ('P-S2', 2.1, 1.4, 1.0), ('P-BG1', 2.6, 1.4, 0.25), ('P-BG2', 2.5, 1.4, 0.5), ('P-Q2', 2.4, 1.0, 0.25)):
            aW = sig*e*r**2/(r0**2+r**2); a11 = q*s11+k11-(cf+1+aW); a22 = q*s22-(cf+1+aW); a12 = q*s12+k12
            lam = 0.5*(a11+a22)+torch.sqrt((0.5*(a11-a22))**2+a12**2); idx = int(torch.argmax(lam)); i, jj = divmod(idx, self.mesh.Nt)
            out[name] = {'q': q, 'sigma': sig, 'r0': r0, 'beta_mesh': -float(lam.max()), 'at_r': float(self.mesh.r[i]), 'at_theta': float(self.mesh.theta[jj]), 'origin_cap': cf+1-q, 'beta_quotable_min_mesh_cap': min(-float(lam.max()), cf+1-q)}
        # also the uncorrected background on the same mesh for comparison
        s11 = cf+self.u1[(1, 0)]; s22 = cf+self.u2[(0, 1)]; s12 = 0.5*(self.u1[(0, 1)]+self.u2[(1, 0)]); k11 = -self.rho[(0, 1)]; k12 = 0.5*self.rho[(1, 0)]; e = cf+(self.u1[(0, 0)]*cs+self.u2[(0, 0)]*sn)/r
        for name, q, sig, r0 in (('P-S1', 2.1, 1.0, 0.5), ('P-S2', 2.1, 1.4, 1.0), ('P-BG1', 2.6, 1.4, 0.25), ('P-BG2', 2.5, 1.4, 0.5), ('P-Q2', 2.4, 1.0, 0.25)):
            aW = sig*e*r**2/(r0**2+r**2); a11 = q*s11+k11-(cf+1+aW); a22 = q*s22-(cf+1+aW); a12 = q*s12+k12
            lam = 0.5*(a11+a22)+torch.sqrt((0.5*(a11-a22))**2+a12**2); out[name]['beta_mesh_uncorrected_base'] = -float(lam.max())
        return out
    def beta0_screen(self, fld):
        """(B-L2) screen of the corrected density rho_* = rho_C + h_phi (c1-n1 diag2 formulas, FLOAT on the mesh): theta = sup(|grad rho| - rho_y)/2, kappa by the Hilbert-Schmidt route"""
        hf, vf = self.split(fld); base = self.base
        rx = self.rho[(1, 0)]+hf[(1, 0)]; ry = self.rho[(0, 1)]+hf[(0, 1)]; rxx = self.rho[(2, 0)]+hf[(2, 0)]; rxy = self.rho[(1, 1)]+hf[(1, 1)]; ryy = self.rho[(0, 2)]+hf[(0, 2)]
        th = float(((torch.sqrt(rx**2+ry**2)-ry)/2).max())
        Drx2 = float(torch.sum(base*(rxx**2+rxy**2))); Dry2 = float(torch.sum(base*(rxy**2+ryy**2)))
        kap = math.sqrt(((math.log(2)-0.5)*Drx2+(3*math.log(2)-2)*Dry2)/(16*math.pi))
        return {'theta': th, 'kappa_mesh': kap, 'beta0_mesh': self.c+1-th-kap, 'sup_grad_rho_star': float(torch.sqrt(rx**2+ry**2).max()), 'sup_D2_rho_star': float(torch.sqrt(rxx**2+2*rxy**2+ryy**2).max())}
    def weighted_bands(self, comp):
        """radius-band (dyadic) and mode-band shares of E_0 = ||W F_*||^2, and radius-band shares of E_1, E_2, at P-S1 and P-S2 (mesh values; FLOAT)"""
        out = {}; r = self.mesh.r; th = self.mesh.theta; Nt = len(th)
        Ns = torch.arange(1, 2*Nt, 2, dtype=DT, device=self.dev); S = torch.sin(Ns[:, None]*th[None, :])
        bands = [(1, 31), (33, 63), (65, 95), (97, 159), (161, 10**6)]
        for name, (sig, r0) in TUPLES.items():
            W, Wx, Wy, Wxx, Wxy, Wyy = self.weight_derivs(sig, r0); F = comp[(0, 0)]
            g = W*F; gx = W*comp[(1, 0)]+Wx*F; gy = W*comp[(0, 1)]+Wy*F
            gxx = W*comp[(2, 0)]+2*Wx*comp[(1, 0)]+Wxx*F; gxy = W*comp[(1, 1)]+Wx*comp[(0, 1)]+Wy*comp[(1, 0)]+Wxy*F; gyy = W*comp[(0, 2)]+2*Wy*comp[(0, 1)]+Wyy*F
            e0 = self.base*g**2; e1 = self.base*(gx**2+gy**2); e2 = self.base*(gxx**2+2*gxy**2+gyy**2)
            E0, E1, E2 = float(e0.sum()), float(e1.sum()), float(e2.sum())
            rad = {}
            for j in range(-6, 14):
                m = ((r >= 2.**j) & (r < 2.**(j+1))).to(DT)[:, None]
                sh = (float((e0*m).sum())/E0, float((e1*m).sum())/E1, float((e2*m).sum())/E2)
                if max(sh) > 0.005: rad[f'[{2.**j:g},{2.**(j+1):g})'] = [round(v, 4) for v in sh]
            gk = (g@S.T)*(2.0/Nt); Ek = (self.mesh.ws[:, None]*r[:, None]**2*gk**2).sum(0)*math.pi; Ek = Ek/float(Ek.sum())
            modes = {}
            for (lo, hi) in bands:
                sel = (Ns >= lo) & (Ns <= hi); modes[f'N {lo}..{min(hi, int(Ns[-1]))}'] = round(float(Ek[sel].sum()), 4)
            out[name] = {'E0': E0, 'E1': E1, 'E2': E2, 'radius_band_shares_E0_E1_E2': rad, 'mode_band_shares_E0': modes}
        return out
    def far_tail_estimate(self, comp, r_lo=2000.0):
        """estimate of the omitted far part r > r_max of ||F_*||^2 and of E_0 = ||W F_*||^2 at P-S1, P-S2: per angular mode, a power law |F_N(r)| = C r^alpha is fitted
        on r_lo <= r <= r_max (least squares in log-log on the mesh radii) and integrated analytically beyond r_max with W^2 approximated by (r^2/r0^2)^sigma (its leading term).
        FLOAT and HEURISTIC (power-law extrapolation of the sampled tail); modes with fewer than four usable nodes or alpha >= -1.9 (nonintegrable with the P-S2 weight) are reported separately."""
        F = comp[(0, 0)]; r = self.mesh.r; th = self.mesh.theta; Nt = len(th); rmax = float(r.max())
        Ns = torch.arange(1, 2*Nt, 2, dtype=DT, device=self.dev); S = torch.sin(Ns[:, None]*th[None, :]); Fk = (F@S.T)*(2.0/Nt)   # (Nr, Nm) sine coefficients
        sel = (r >= r_lo); rs = r[sel]; out = {'r_lo': r_lo, 'r_max': rmax, 'L2_tail': 0.0, 'E0_tail_P-S1': 0.0, 'E0_tail_P-S2': 0.0, 'modes_used': 0, 'modes_skipped': 0, 'alpha_range': [None, None]}
        alphas = []
        for k in range(Fk.shape[1]):
            f = Fk[sel, k].abs(); good = f > 0
            if int(good.sum()) < 4: out['modes_skipped'] += 1; continue
            x = torch.log(rs[good]); y = torch.log(f[good]); xm = x.mean(); ym = y.mean()
            alpha = float(((x-xm)*(y-ym)).sum()/((x-xm)**2).sum()); logC = float(ym-alpha*xm)
            if alpha >= -1.9 or not math.isfinite(alpha): out['modes_skipped'] += 1; continue
            C2 = math.exp(2*logC); alphas.append(alpha); out['modes_used'] += 1
            # int_{rmax}^inf C^2 r^(2 alpha) r dr * pi (full circle, sin^2 average 1/2 times 2 pi) = pi C^2 rmax^(2 alpha + 2)/(-(2 alpha + 2))
            out['L2_tail'] += math.pi*C2*rmax**(2*alpha+2)/(-(2*alpha+2))
            for name, (sig, r0) in TUPLES.items():
                pw = 2*alpha+2*sig+2
                if pw < 0: out['E0_tail_'+name] += math.pi*C2*r0**(-2*sig)*rmax**pw/(-pw)
                else: out['E0_tail_'+name] = float('inf')
        if alphas: out['alpha_range'] = [min(alphas), max(alphas)]
        out['note'] = 'HEURISTIC power-law extrapolation of the sampled tail beyond r_max; W^2 replaced by its leading power; not a bound'
        return out
    def report(self, a, comp=None, fld=None, target=None):
        if comp is None: comp, fld = self.comps(a)
        hf, vf = self.split(fld); F = comp[(0, 0)]; base = self.base
        A = float(sum(q*float(cA) for q, (cA, cB) in zip(a, self.cAB))); B = float(sum(q*float(cB) for q, (cA, cB) in zip(a, self.cAB)))
        out = {'G0': math.sqrt(float(torch.sum(base*F**2))), 'supF': float(F.abs().max()),
               'h_L2': math.sqrt(float(torch.sum(base*hf[(0, 0)]**2))), 'sup_h': float(hf[(0, 0)].abs().max()), 'grad_h_inf': float(torch.sqrt(hf[(1, 0)]**2+hf[(0, 1)]**2).max()),
               'A': A, 'B': B, 'ell_float': 2*A+6*B, 'a_star': float(self.a0_bg)-8*A, 'constraint_viol': float(self.crow@a)}
        if (1, 0) in comp: out['G1'] = math.sqrt(float(torch.sum(base*(comp[(1, 0)]**2+comp[(0, 1)]**2))))
        if ('v1', (1, 0)) in vf: out['DU_frob_inf'] = float(torch.sqrt(vf[('v1', (1, 0))]**2+vf[('v1', (0, 1))]**2+vf[('v2', (1, 0))]**2+vf[('v2', (0, 1))]**2).max())   # sampled max of the Frobenius norm of DU[h_phi] (>= operator norm pointwise; not a certified sup)
        if (0, 2) in comp:
            for name, (sig, r0) in TUPLES.items():
                n2 = self.n2_weighted(comp, sig, r0); out['N2_'+name] = n2['N2']; out['E012_'+name] = [n2['E0'], n2['E1'], n2['E2']]
            out['BG_margins_corrected'] = self.bg_margins(fld)
            out['beta0_screen'] = self.beta0_screen(fld)
            out['weighted_bands'] = self.weighted_bands(comp)
            out['far_tail_estimate'] = self.far_tail_estimate(comp)
        if target is not None: out['h_minus_target_L2'] = math.sqrt(float(torch.sum(base*(hf[(0, 0)]-target)**2)))
        # dyadic L2 shares of F_*
        r = self.mesh.r; shares = {}
        for j in range(-6, 14):
            msk = ((r >= 2.**j) & (r < 2.**(j+1))).to(DT)[:, None]
            shares[f'[{2.**j:g},{2.**(j+1):g})'] = float(torch.sum(base*msk*F**2))/out['G0']**2
        out['dyadic_shares'] = {k: v for k, v in shares.items() if v > 1e-4}
        return out
    # ---- start value from the grid h
    def target_field(self, modes_npy, s_npy):
        from scipy.interpolate import CubicSpline
        H = np.load(modes_npy); s = np.load(s_npy); Nt_ = H.shape[1]; Ns = np.arange(1, 2*Nt_, 2)
        sm = self.mesh.s.cpu().numpy(); sm_c = np.clip(sm, s[0], s[-1])
        Hm = np.stack([CubicSpline(s, H[:, k])(sm_c) for k in range(Nt_)], 1)             # (Nr, Nt_) mode values on the mesh radii
        Hm[sm > s[-1]] = 0.0
        th = self.mesh.theta.cpu().numpy(); T = np.sin(np.outer(Ns, th))                     # (Nt_, Nt)
        self.target_modes = (torch.as_tensor(Hm, dtype=DT, device=self.dev), Ns)
        return torch.as_tensor(Hm@T, dtype=DT, device=self.dev)
    def start_from_target(self, rcond=1e-9):
        """per-mode weighted radial least squares of h = sum a_m H_m to the target modes; then the normalizer coefficient from A + 3B = 0"""
        Hm, Ns = self.target_modes; w = (self.mesh.ws*self.mesh.r**2).cpu().numpy(); sw = np.sqrt(w)
        a = np.zeros(self.n); info = {}
        for n in sorted({at['n'] for at in self.atoms}):
            idx = [m for m, at in enumerate(self.atoms) if at['n'] == n and at['branch'] != 'normalizer']
            if n not in Ns or not idx: continue
            k = int(np.where(Ns == n)[0][0]); tgt = Hm[:, k].cpu().numpy()
            cols = []
            for m in idx:
                sl = self.gslots[m][('h', (0, 0))]; assert len(sl) == 1 and sl[0][0] == 'sin' and sl[0][1] == n, sl
                cols.append(sl[0][2].cpu().numpy())
            Acol = np.stack(cols, 1)*sw[:, None]; bvec = tgt*sw
            sol, res, rank, sv = np.linalg.lstsq(Acol, bvec, rcond=rcond)
            a[idx] = sol
            fit = Acol@sol; info[n] = {'rel_resid': float(np.linalg.norm(fit-bvec)/max(np.linalg.norm(bvec), 1e-300)), 'rank': int(rank), 'n_atoms': len(idx), 'target_L2': float(math.sqrt(math.pi*np.sum(bvec**2)))}
        # constraint: normalizer atom 0 carries B with coefficient 1: a_0 = -(A_rest + 3 B_rest)/3
        A = sum(q*float(cA) for q, (cA, cB) in zip(a, self.cAB)); Brest = sum(q*float(cB) for m, (q, (cA, cB)) in enumerate(zip(a, self.cAB)) if m != 0)
        a[0] = -(A+3*Brest)/3
        return a, info
    # ---- driver
    def optimize(self, a0, steps=30, lam0=1e-6, lam_min=1e-14, lam_max=1e2, tmax=4.0, lam_factors=(0.1, 0.3, 1.0, 3.0, 10.0), log=None, ckpt=None, stop_file=None, target=None, report_every=1):
        a = np.array(a0, float); lam = lam0; hist = []
        def say(msg):
            print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
        for it in range(1, steps+1):
            if stop_file and os.path.exists(stop_file): say(f'STOP file seen at it {it}'); break
            t0 = time.time()
            G, g, fcur = self.normal_equations(a)
            lams = [min(max(lam*f, lam_min), lam_max) for f in lam_factors]
            dirs = self.gn_dirs(a, lams, G, g)
            cands = []
            for lm, (delta, pred) in zip(lams, dirs):
                t, phit, phi0, _ = self.line_search(a, delta, tmax=tmax)
                if t > 0: cands.append((phit, lm, t, delta, pred))
            good = [cn for cn in cands if cn[2] >= 0.3]
            best = min(good, key=lambda cn: cn[0]) if good else (min(cands, key=lambda cn: cn[0]) if cands else None)
            if best is None:
                lam = min(lam*100, lam_max); ok = False; fnew = fcur; lmb = lam; tb = 0.0; pred = 0.0
            else:
                phit, lmb, tb, delta, pred = best
                a_new = a+tb*delta; fnew, parts, comp, fld = self.objective(a_new)
                ok = fnew < fcur
                if ok: a = a_new; lam = lmb if good else min(lmb*10, lam_max)
                else: lam = min(lmb*10, lam_max)
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} lam {lmb:.1e} t {tb:.3f} pred {pred:.3e}'
            if ok:
                msg += ' parts '+' '.join(f'{k}:{v:.3e}' for k, v in parts.items())
                if it % report_every == 0:
                    rp = self.report(a, comp, fld, target); hist.append(dict(it=it, obj=fnew, lam=lmb, t=tb, **{k: v for k, v in rp.items() if not isinstance(v, (dict, list))}))
                    msg += ' | '+' '.join(f'{k} {v:.5e}' if isinstance(v, float) else '' for k, v in rp.items() if not isinstance(v, (dict, list)))
            msg += f' ({time.time()-t0:.1f}s)'
            say(msg)
            if ckpt and ok: np.save(ckpt, a)
        return a, hist

    # ---- direct least squares on the Jacobian (the problem is nearly linear; the atom columns are collinear to 1e-16, so J^T J is useless)
    def jacobian_full(self, a, rchunk=16):
        comp, fld = self.comps(a); hf, vf = self.split(fld)
        n = self.n; Nr, Nt = self.mesh.Nr, self.mesh.Nt
        nrows_total = sum((Nr if k_ is None else int(k_.sum()))*Nt for k_ in self.row_keep)
        J = torch.empty(nrows_total, n, dtype=DT, device=self.dev); rv = torch.empty(nrows_total, dtype=DT, device=self.dev)
        pos = 0
        for r0_ in range(0, Nr, rchunk):
            rs = slice(r0_, min(Nr, r0_+rchunk)); nr = rs.stop-rs.start
            rvec = torch.cat([x.reshape(-1) for x in self.rows(comp, rs)], 0)
            KM = {key: self.key_matrix(key, rs) for key in self.keys}
            hm = {k[1]: v for k, v in KM.items() if k[0] == 'h'}; vm = {k: v for k, v in KM.items() if k[0] != 'h'}
            hs = {k: v[rs] for k, v in hf.items()}; vs = {k: v[rs] for k, v in vf.items()}
            Md = {d: self.lin(hm, vm, d, rs)+self.quad(vm, hs, d, rs)+self.quad(vs, hm, d, rs) for d in self.derivs}
            del KM, hm, vm
            Jparts = []
            for k, (w, cd, _) in enumerate(self.rowspecs):
                M = None
                for d in cd:
                    cf = cd[d][rs][..., None] if torch.is_tensor(cd[d]) else cd[d]
                    M = cf*Md[d] if M is None else M+cf*Md[d]
                Mw = M*self.sqw[k][rs][..., None]
                if self.row_keep[k] is not None: Mw = Mw[self.row_keep[k][rs]]
                Jparts.append(Mw.reshape(-1, n))
            Jc = torch.cat(Jparts, 0); del Jparts, Md
            J[pos:pos+len(rvec)] = Jc; rv[pos:pos+len(rvec)] = rvec; pos += len(rvec)
            del Jc
        if hasattr(self, 'linrows'):
            Ct, bt, wt, _ = self.linrows; at = torch.as_tensor(np.asarray(a, float), dtype=DT, device=self.dev)
            J = torch.cat([J, wt[:, None]*Ct], 0); rv = torch.cat([rv, wt*(Ct@at-bt)], 0)
        return J, rv, comp, fld
    def set_constraints(self, Cmat, bvec):
        """general exact-linear constraints C a = b (rows: the normalizer row A + 3B = 0 is always included first); null-space basis Z and particular solution a_p by SVD"""
        C = np.vstack([self.crow[None, :], Cmat]) if Cmat is not None and len(Cmat) else self.crow[None, :]; b = np.r_[0.0, bvec] if Cmat is not None and len(Cmat) else np.zeros(1)
        Ct = torch.as_tensor(C, dtype=DT, device=self.dev); bt = torch.as_tensor(b, dtype=DT, device=self.dev)
        # row scaling for the rank decision (the sector rows span many orders of magnitude)
        rn = torch.linalg.norm(Ct, dim=1); rn[rn == 0] = 1.0; Cs = Ct/rn[:, None]; bs = bt/rn
        U, S, Vh = torch.linalg.svd(Cs, full_matrices=True)
        rank = int((S > 1e-12*S[0]).sum())
        a_p = Vh[:rank].T@((U[:, :rank].T@bs)/S[:rank])
        Z = Vh[rank:].T
        self.cons = {'C': Ct, 'b': bt, 'Z': Z, 'a_p': a_p.cpu().numpy(), 'rank': rank, 'rows': C.shape[0]}
        resid = float(torch.linalg.norm(Ct@a_p-bt)); print(f'constraints: {C.shape[0]} rows, rank {rank}, null space dimension {Z.shape[1]}, particular-solution residual {resid:.3e}, |a_p| max {float(a_p.abs().max()):.3e}', flush=True)
        return self.cons['a_p']
    def optimize_svd_constrained(self, a0, steps=4, lam_rels=(0.0, 1e-15, 1e-13, 1e-11, 1e-9, 1e-7), tmax=8.0, log=None, ckpt=None, stop_file=None, target=None, svd_cut=1e-15):
        """as optimize_svd, with the least squares restricted to the null space of all linear constraints (a = a_p + Z y); the start a0 must satisfy them"""
        a = np.array(a0, float); hist = []; Z = self.cons['Z']; C = self.cons['C']; bt = self.cons['b']
        def say(msg):
            print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
        say(f'constraint violation at start: {float(torch.linalg.norm(C@torch.as_tensor(a, dtype=DT, device=self.dev)-bt)):.3e}')
        for it in range(1, steps+1):
            if stop_file and os.path.exists(stop_file): say(f'STOP file seen at it {it}'); break
            t0 = time.time()
            J, rv, comp, fld = self.jacobian_full(a); fcur = float(rv@rv)
            JZ = J@Z; del J
            cn = torch.linalg.norm(JZ, dim=0); cn[cn == 0] = 1.0; JZ /= cn[None, :]
            U, S, Vh = torch.linalg.svd(JZ, full_matrices=False); del JZ
            Utr = U.T@rv; del U
            smax = float(S[0]); rank = int((S > svd_cut*smax).sum()); cands = []
            for lr in lam_rels:
                filt = S/(S*S+lr*smax*smax); filt[S <= svd_cut*smax] = 0
                dy = -(Vh.T@(filt*Utr))/cn
                delta = (Z@dy).cpu().numpy()
                t, phit, phi0, _ = self.line_search(a, delta, tmax=tmax)
                if t > 0: cands.append((phit, lr, t, delta))
            del S, Vh, Utr
            if not cands: say(f'it {it:3d} obj {fcur:.6e}: no decrease; stop'); break
            phit, lr, tb, delta = min(cands, key=lambda cn_: cn_[0])
            a_new = a+tb*delta; fnew, parts, comp, fld = self.objective(a_new); ok = fnew < fcur
            if ok: a = a_new
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} lam_rel {lr:.0e} t {tb:.3f} rank {rank}/{Z.shape[1]} smax {smax:.3e} cands '+' '.join(f'{lr_:.0e}:{p:.3e}@{t_:.2f}' for p, lr_, t_, _ in sorted(cands, key=lambda cn_: cn_[1]))
            if ok:
                rp = self.report(a, comp, fld, target); hist.append(dict(it=it, obj=fnew, lam_rel=lr, t=tb, **{k: v for k, v in rp.items() if not isinstance(v, (dict, list))}))
                msg += ' | parts '+' '.join(f'{k}:{v:.3e}' for k, v in parts.items())+' | '+' '.join(f'{k} {v:.5e}' for k, v in rp.items() if isinstance(v, float))
                msg += f' | constraint violation {float(torch.linalg.norm(C@torch.as_tensor(a, dtype=DT, device=self.dev)-bt)):.3e}'
            msg += f' ({time.time()-t0:.1f}s)'
            say(msg)
            if ckpt and ok: np.save(ckpt, a)
            if ok and (fcur-fnew) < 1e-4*fcur: say('relative decrease below 1e-4: converged'); break
        return a, hist
    def optimize_svd(self, a0, steps=8, lam_rels=(0.0, 1e-15, 1e-13, 1e-11, 1e-9, 1e-7), tmax=8.0, log=None, ckpt=None, stop_file=None, target=None, svd_cut=1e-15, tsqr_rows=None, honest=False):
        """each step: full Jacobian, constraint eliminated through the normalizer atom (a_0 = -(sum_{m>=1} c_m a_m)/c_0), thin SVD, Tikhonov-regularized
        LS directions for several relative lambda, exact quartic line search each, best accepted."""
        a = np.array(a0, float); hist = []
        c = self.crow; assert abs(c[0]) > 0; cr = torch.as_tensor(c[1:]/c[0], dtype=DT, device=self.dev)
        def say(msg):
            print(msg, flush=True)
            if log: open(log, 'a').write(msg+'\n')
        for it in range(1, steps+1):
            if stop_file and os.path.exists(stop_file): say(f'STOP file seen at it {it}'); break
            t0 = time.time()
            J, rv, comp, fld = self.jacobian_full(a)
            if honest:
                th0 = time.time(); Fh = self.honest_L2(a); fcur_b64 = float(rv@rv); rv = self.replace_L2_rows(rv, Fh); say(f'    honest L2 residual: G0 longdouble {math.sqrt(float(np.sum(self._hbg_base()*Fh**2))):.6e}; sqrt of the all-rows binary64 objective {math.sqrt(fcur_b64):.3e} -> with longdouble L2 rows {math.sqrt(float(rv@rv)):.3e}; {time.time()-th0:.0f}s')
            fcur = float(rv@rv)
            J[:, 1:] -= J[:, :1]*cr[None, :]; Jr = J[:, 1:]                                   # constraint elimination in place (a second 20 GB matrix broke the 213k-row run with CUDA OOM)
            cn = torch.linalg.norm(Jr, dim=0); cn[cn == 0] = 1.0; Jr /= cn[None, :]           # column scaling: the atom columns span 1e24 in norm (t^(-d) factors)
            if tsqr_rows and Jr.shape[0] > tsqr_rows:
                # tall-skinny QR in row chunks (each chunk below the 2^31-entry cuSOLVER limit): min ||Jr x - rv|| = min ||R2 x - y2|| + const
                Rs, ys = [], []
                for i0 in range(0, Jr.shape[0], tsqr_rows):
                    Qi, Ri = torch.linalg.qr(Jr[i0:i0+tsqr_rows].contiguous()); Rs.append(Ri); ys.append(Qi.T@rv[i0:i0+tsqr_rows]); del Qi
                del Jr, J; torch.cuda.empty_cache()
                Q2, R2 = torch.linalg.qr(torch.cat(Rs, 0)); y2 = Q2.T@torch.cat(ys, 0); del Rs, ys, Q2
                U, S, Vh = torch.linalg.svd(R2, full_matrices=False); del R2
                Utr = U.T@y2; del U, y2
            else:
                U, S, Vh = torch.linalg.svd(Jr, full_matrices=False); del Jr, J
                Utr = U.T@rv; del U
            smax = float(S[0]); rank = int((S > svd_cut*smax).sum())
            cands = []
            for lr in lam_rels:
                filt = S/(S*S+lr*smax*smax); filt[S <= svd_cut*smax] = 0
                dred = -(Vh.T@(filt*Utr))/cn
                d0 = -(cr@dred)
                delta = torch.cat([d0[None], dred]).cpu().numpy()
                # the constraint violation of a itself is removed as well
                viol = float(c@a); delta[0] -= viol/c[0]
                if honest:
                    t, phit, phi0, _ = self.line_search(a, delta, tmax=tmax, honest_F=(Fh, self.honest_L2(a+delta), self.honest_L2(a-delta)))   # longdouble quartic
                else:
                    t, phit, phi0, _ = self.line_search(a, delta, tmax=tmax)
                if t > 0: cands.append((phit, lr, t, delta))
            del S, Vh, Utr
            if not cands:
                say(f'it {it:3d} obj {fcur:.6e}: no decrease along any direction ({"longdouble" if honest else "binary64"} quartic line search); stop'); break
            phit, lr, tb, delta = min(cands, key=lambda cn: cn[0])
            a_new = a+tb*delta
            if honest: fnew, parts, comp, fld, Fh_new = self.objective_honest(a_new)
            else: fnew, parts, comp, fld = self.objective(a_new)
            ok = fnew < fcur
            if ok: a = a_new
            msg = f'it {it:3d} obj {fcur:.6e} -> {fnew:.6e} {"ACC" if ok else "rej"} lam_rel {lr:.0e} t {tb:.3f} rank {rank}/{len(c)-1} smax {smax:.3e} cands '+' '.join(f'{lr_:.0e}:{p:.3e}@{t_:.2f}' for p, lr_, t_, _ in sorted(cands, key=lambda cn: cn[1]))
            if ok:
                rp = self.report(a, comp, fld, target)
                if honest: rp['G0_honest'] = math.sqrt(float(np.sum(self._hbg_base()*Fh_new**2)))
                rp['max_abs_a'] = float(np.abs(a).max()); rp['L1_a'] = float(np.abs(a).sum())
                hist.append(dict(it=it, obj=fnew, lam_rel=lr, t=tb, **{k: v for k, v in rp.items() if not isinstance(v, (dict, list))}))
                msg += ' | parts '+' '.join(f'{k}:{v:.3e}' for k, v in parts.items())+' | '+' '.join(f'{k} {v:.5e}' for k, v in rp.items() if isinstance(v, float))
            msg += f' ({time.time()-t0:.1f}s)'
            say(msg)
            if ckpt and ok: np.save(ckpt, a)
            if ok and (fcur-fnew) < 1e-4*fcur: say('relative decrease below 1e-4: converged'); break
        return a, hist
    # ---- freeze to exact rationals and write the JSON
    def freeze(self, a, path, meta, denom_bits=80):
        D = mpz(2)**denom_bits
        qs = [mpq(mpz(int(round(float(v)*float(D)))), D) for v in a]
        A_rest = sum(q*cA for m, (q, (cA, cB)) in enumerate(zip(qs, self.cAB)) if m != 0); B_rest = sum(q*cB for m, (q, (cA, cB)) in enumerate(zip(qs, self.cAB)) if m != 0)
        qs[0] = -(A_rest+3*B_rest)/3                                                     # the normalizer atom (B-coefficient 1) closes A + 3B = 0 exactly
        A, B = self.exact_AB(qs); assert A+3*B == 0
        a_star = self.a0_bg-8*A
        cap_margin = a_star-mpq(21, 10)*(2*C_EXACT-2)                     # AT-167 / coordinator 00:44Z item 2: the origin cap c + 1 - q is attained only if a_* >= q(2c - 2)
        cap_ok = cap_margin >= 0 and a_star > 0
        if not cap_ok: print('WARNING: frozen fit violates the origin cap condition a_* >= q(2c - 2) at q = 21/10 (margin %s); labelled FAILING' % float(cap_margin), flush=True)
        atoms = [dict({'coefficient_exact': q2s(q), 'n': at['n'], 'h': at['h'], 'b_exact': q2s(at['b']), 'scale_exact': q2s(at['t']), 'd': at['d'], 'branch': at['branch'], 'tau_exact': q2s(at['n']+2*at['h']+2*at['b']-2*at['d'])},
                      **({'legendre_degree': at['k_leg']} if at.get('k_leg', 0) > 0 else {}))
                 for q, at in zip(qs, self.atoms) if q != 0]
        merged = {}
        for q, at in zip(qs, self.atoms):
            if q == 0: continue
            for cq, el in elementary_expansion(at, q):
                key = (el['n'], el['h'], q2s(el['b']), q2s(el['t']), el['d']); merged[key] = merged.get(key, mpq(0))+cq
        atoms_elem = [{'coefficient_exact': q2s(v), 'n': kk[0], 'h': kk[1], 'b_exact': kk[2], 'scale_exact': kk[3], 'd': kk[4]} for kk, v in merged.items() if v != 0]
        J = {'schema_version': 'ipm-potential-correction-v1', 'id': meta.get('id', 'DRAFT'), 'role': meta.get('role', 'normalized odd-potential correction (AT-119 class) of an exact campaign-basis center'),
             'reference_sha256': REF007_SHA, 'c_exact': q2s(C_EXACT), 'mu_exact': q2s(MU), 'e_exact': q2s(E_EXP),
             'definition': 'phi=sum coefficient_exact Im(x+iy)^n (x^2+y^2)^h (1+x^2+y^2)^b_exact (scale_exact+x^2+y^2)^(-d); h_phi=-Delta phi; U[h_phi]=(-phi_xy,phi_xx). Degree rule tau = n+2h+2b-2d <= mu = 4/c-3 holds for every atom (tau_exact given).',
             'center': {'base_candidate_id': meta.get('base_id'), 'base_exact_sha256': self.bg_meta['cand_sha256'], 'base_exact_json': self.bg_meta['cand_json'].split('/')[-1], 'a0_base_exact': q2s(self.a0_bg),
                        'composite_correction': 'h_* = (rho_base - rho_007) + h_phi; rho_* = rho_007 + h_* = rho_base + h_phi; u_* = u_base + U[h_phi]; F_* = F_base + L_base h_phi + U[h_phi].grad h_phi', 'ell_base_minus_007': '0 (both candidates satisfy the exact center row c + ell(rho) = 1)'},
             'atoms': atoms, 'n_atoms_nonzero': len(atoms), 'n_atoms_total': self.n,
             'atoms_elementary': atoms_elem, 'n_atoms_elementary': len(atoms_elem),
             'legendre_convention': 'an atom with legendre_degree k carries the extra factor P_k(2 ts - 1), ts = (x^2+y^2)/(scale_exact + x^2 + y^2), P_k the Legendre polynomial; P_k(2 ts - 1) = sum_j (-1)^(k+j) C(k,j) C(k+j,j) ts^j, so the atom equals the sum of elementary atoms (h + j, d + j) with those rational multiples; atoms_elementary is that expansion summed over all atoms (same function, large cancelling coefficients: evaluate the Legendre form in finite precision, the elementary form only in exact or high-precision arithmetic)',
             'exact_identities': {'A_cubic': q2s(A), 'B_cubic': q2s(B), 'A_plus_3B': '0', 'ell_h_phi': '0', 'origin_density_slope_h_phi': q2s(-8*A), 'a_star_exact': q2s(a_star), 'a_star_float': float(a_star),
                                  'a_star_minus_q_times_2c_minus_2_at_q_21_10': q2s(cap_margin), 'origin_cap_condition_q_21_10': 'PASS (exact)' if cap_ok else 'FAILING (exact)', 'a_star_positive': bool(a_star > 0)},
             'sector_e_correction': {'formula': 'f_e^*(theta) = f_e^C(theta) + (c e - 1) sum_{tau_m = mu} a_m (n_m^2 - mu^2) sin(n_m theta); the coefficient of sin(n theta) added to the (3,1) sector (exponent e) of the base residual, exact rationals; atoms with tau < mu do not touch this sector',
                                     'c_e_minus_1_exact': q2s(C_EXACT*E_EXP-1),
                                     'added_sine_coefficients': {str(n): q2s((C_EXACT*E_EXP-1)*sum(q*(at['n']**2-MU**2) for q, at in zip(qs, self.atoms) if at['n'] == n and at['n']+2*at['h']+2*at['b']-2*at['d'] == MU)) for n in sorted({at['n'] for q, at in zip(qs, self.atoms) if q != 0 and at['n']+2*at['h']+2*at['b']-2*at['d'] == MU})}},
             'conversion_policy': f'binary64 optimizer coefficients rounded to the nearest multiple of 2^-{denom_bits}; the normalizer atom (n 3, h 0, b -2, t 1, d 0; AN-045) coefficient then solved exactly from A + 3B = 0',
             'fit_meta': meta}
        if hasattr(self, 'cons'):
            af = torch.as_tensor([float(q) for q in qs], dtype=DT, device=self.dev); viol = (self.cons['C']@af-self.cons['b']).abs()
            J['sector_constraints'] = {'rows': int(self.cons['rows']), 'max_violation_frozen_binary64': float(viol.max()), 'note': 'linear far-field sector rows (binary64 coefficients from exact tails and the base classes) imposed in the fit; the frozen rationals satisfy them to the stated level; exact sector values of the frozen function: numerical_audit / phi_far.py'}
        txt = json.dumps(J, indent=1); open(path, 'w').write(txt)
        return sha256_bytes(txt.encode()), qs, J

def atoms_from_json(J):
    atoms = [dict(n=int(at['n']), h=int(at['h']), b=mpq(at['b_exact']), t=mpq(at['scale_exact']), d=int(at['d']), branch=at.get('branch', '?'), k=0, k_leg=int(at.get('legendre_degree', 0))) for at in J['atoms']]
    validate_atoms(atoms)
    return atoms, np.array([float(mpq(at['coefficient_exact'])) for at in J['atoms']])

# ------------------------------------------------------------------ CLI
def main():
    cmd = sys.argv[1]; dev = torch.device(os.environ.get('IPM_DEVICE', 'cuda'))
    if cmd == 'bg':
        cand, mid, ang, out = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        rmax = float(sys.argv[6]) if len(sys.argv) > 6 else 1e4
        os.makedirs(os.path.dirname(out), exist_ok=True); build_background(cand, mid, ang, out, dev, rmax=rmax)
    elif cmd == 'fit':
        cfg = json.load(open(sys.argv[2])); tag = cfg['tag']; out = os.path.join(HERE, 'phi_runs', tag); os.makedirs(out, exist_ok=True)
        logf = os.path.join(out, tag+'.log')
        def say(m):
            print(m, flush=True); open(logf, 'a').write(m+'\n')
        say(f'# phi_fit {tag} start {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} cfg {json.dumps(cfg)}')
        bg, mesh = load_background(os.path.join(LANE, cfg['background_pt']), dev)
        atoms = make_atoms(cfg)
        pf = PhiFit(bg, mesh, atoms, wL2=cfg.get('wL2', 1.0), sobolev=cfg.get('sobolev'), dmax_h=cfg.get('dmax_h', 3), extra_l2_weights=[tuple(x) for x in cfg.get('extra_l2_weights', [])], sobolev_rmax=cfg.get('sobolev_rmax'))
        say(f'background {bg["meta"]["cand_json"]} sha {bg["meta"]["cand_sha256"]} mesh {mesh.Nr}x{mesh.Nt} G0 {bg["meta"]["G0_mesh"]:.8e}; atoms {pf.n}; build {pf.build_time:.0f}s')
        target = pf.target_field(os.path.join(LANE, cfg['target_modes']), os.path.join(LANE, cfg['target_s']))
        tnorm = math.sqrt(float(torch.sum(pf.base*target**2))); say(f'target h: mesh L2 {tnorm:.6e}')
        if cfg.get('init'):
            a0 = np.load(os.path.join(LANE, cfg['init'])); assert len(a0) == pf.n
        elif cfg.get('start', 'zero') == 'zero':
            a0 = np.zeros(pf.n)
        else:
            a0, info = pf.start_from_target(rcond=cfg.get('rcond', 1e-9))
            say('start LS per mode: '+' '.join(f'n{n}:{v["rel_resid"]:.2e}({v["n_atoms"]}/{v["rank"]})' for n, v in sorted(info.items())))
        f0, parts, comp, fld = pf.objective(a0); rp = pf.report(a0, comp, fld, target)
        say(f'start obj {f0:.6e} parts {parts} | '+' '.join(f'{k} {v:.5e}' for k, v in rp.items() if isinstance(v, float)))
        if cfg.get('honest'):
            fh, ph, _, _, Fh = pf.objective_honest(a0); say(f'start honest obj {fh:.6e} parts {ph}; G0 longdouble {math.sqrt(float(np.sum(pf._hbg_base()*Fh**2))):.6e}; max|a| {np.abs(a0).max():.3e} L1 {np.abs(a0).sum():.3e}')
        np.save(os.path.join(out, tag+'_start.npy'), a0)
        if cfg.get('soft_sector_rows'):
            sr = cfg['soft_sector_rows']; Cz = np.load(os.path.join(LANE, sr['npz']), allow_pickle=True); assert int(Cz['n_atoms']) == pf.n
            al = Cz['class_float']; Rb = sr.get('R', 1e4); tail = sr.get('tail', 0.01)
            budget = tail*np.sqrt(np.maximum(-2*al-4.8, 1e-9))*Rb**(-al-2.4)        # P-S2 far-field budget per class (FF_BUDGET_v01 rule: a unit coefficient's weighted tail beyond R)
            weights = sr['w']/budget
            pf.set_soft_rows(Cz['C'], Cz['b'], weights)
            say(f'soft sector rows: {Cz["C"].shape[0]} rows, weight w/budget with w {sr["w"]}, budgets per class {sorted({round(float(a_), 4): float(f"{b_:.3g}") for a_, b_ in zip(al, budget)}.items(), reverse=True)}')
        if cfg.get('constraints_npz'):
            Cz = np.load(os.path.join(LANE, cfg['constraints_npz']), allow_pickle=True); assert int(Cz['n_atoms']) == pf.n, 'constraint rows built for another dictionary'
            a0 = pf.set_constraints(Cz['C'], Cz['b'])
            say(f'sector constraints: {Cz["C"].shape[0]} rows from {cfg["constraints_npz"]} (classes {sorted(set(np.round(Cz["class_float"], 4).tolist()), reverse=True)}); start = particular solution (|a| max {np.abs(a0).max():.3e})')
            a, hist = pf.optimize_svd_constrained(a0, steps=cfg['steps'], tmax=cfg.get('tmax', 2.0), log=logf, ckpt=os.path.join(out, tag+'_coefs.npy'), stop_file=os.path.join(out, 'STOP'), target=target, lam_rels=tuple(cfg.get('lam_rels', (0.0, 1e-15, 1e-13, 1e-11, 1e-9, 1e-7))), svd_cut=cfg.get('svd_cut', 1e-15))
        elif cfg.get('method', 'svd') == 'svd':
            a, hist = pf.optimize_svd(a0, steps=cfg['steps'], tmax=cfg.get('tmax', 2.0), log=logf, ckpt=os.path.join(out, tag+'_coefs.npy'), stop_file=os.path.join(out, 'STOP'), target=target, lam_rels=tuple(cfg.get('lam_rels', (0.0, 1e-15, 1e-13, 1e-11, 1e-9, 1e-7))), svd_cut=cfg.get('svd_cut', 1e-15), tsqr_rows=cfg.get('tsqr_rows'), honest=bool(cfg.get('honest', False)))
        else:
            a, hist = pf.optimize(a0, steps=cfg['steps'], lam0=cfg.get('lam0', 1e-6), tmax=cfg.get('tmax', 4.0), log=logf, ckpt=os.path.join(out, tag+'_coefs.npy'), stop_file=os.path.join(out, 'STOP'), target=target)
        np.save(os.path.join(out, tag+'_coefs.npy'), a)
        f1, parts, comp, fld = pf.objective(a); rp = pf.report(a, comp, fld, target)
        if cfg.get('honest'):
            fh, parts, comp, fld, Fh = pf.objective_honest(a); rp['G0_honest'] = math.sqrt(float(np.sum(pf._hbg_base()*Fh**2))); rp['max_abs_a'] = float(np.abs(a).max()); rp['L1_a'] = float(np.abs(a).sum())
            say(f'FINAL honest obj {fh:.6e} (binary64 obj {f1:.6e}); G0 longdouble {rp["G0_honest"]:.6e} against binary64 {rp["G0"]:.6e}; max|a| {rp["max_abs_a"]:.3e} L1 {rp["L1_a"]:.3e}')
        say(f'FINAL obj {f1:.6e} parts {parts} | '+' '.join(f'{k} {v:.5e}' for k, v in rp.items() if isinstance(v, float)))
        say('FINAL dyadic shares of ||F_*||^2: '+json.dumps(rp['dyadic_shares']))
        meta = {'tag': tag, 'lane': 'numerics_agent_1', 'base_id': cfg.get('base_id'), 'config': cfg, 'mesh': {'Nr': mesh.Nr, 'Nt': mesh.Nt, 'mid': bg['meta']['mid'], 'ang': bg['meta']['ang'], 'rcut': bg['meta']['rcut'], 'rmax': bg['meta']['rmax']},
                'target_modes_sha256': sha256_file(os.path.join(LANE, cfg['target_modes'])), 'steps_accepted': len(hist), 'final_objective': f1, 'final_report_mesh_FLOAT': {k: v for k, v in rp.items()}, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        sha, qs, J = pf.freeze(a, os.path.join(out, tag+'_phi_exact.json'), meta)
        af = np.array([float(q) for q in qs]); f2, parts2, comp2, fld2 = pf.objective(af); rp2 = pf.report(af, comp2, fld2, target)
        say(f'FROZEN json sha256 {sha}: obj {f2:.6e} (binary64 {f1:.6e}) G0 {rp2["G0"]:.6e} a_star {J["exact_identities"]["a_star_exact"][:40]}... A {J["exact_identities"]["A_cubic"][:30]}...')
        np.save(os.path.join(out, tag+'_Fstar_mesh.npy'), comp2[(0, 0)].cpu().numpy()); np.save(os.path.join(out, tag+'_s_mesh.npy'), mesh.s.cpu().numpy())
        json.dump({'meta': meta, 'history': hist, 'frozen_sha256': sha, 'frozen_report_mesh_FLOAT': rp2, 'parts_frozen': parts2}, open(os.path.join(out, tag+'_summary.json'), 'w'), indent=1)
        say('DONE')
    elif cmd == 'eval':
        phij, bgpt, outj = sys.argv[2], sys.argv[3], sys.argv[4]; fnpy = sys.argv[5] if len(sys.argv) > 5 else None
        J = json.load(open(phij)); bg, mesh = load_background(bgpt, dev)
        assert J['center']['base_exact_sha256'] == bg['meta']['cand_sha256'], 'background mismatch'
        atoms, a = atoms_from_json(J)
        pf = PhiFit(bg, mesh, atoms, wL2=1.0, sobolev=None)
        f, parts, comp, fld = pf.objective(a); rp = pf.report(a, comp, fld)
        A, B = pf.exact_AB([mpq(at['coefficient_exact']) for at in J['atoms']]); assert A+3*B == 0 and q2s(A) == J['exact_identities']['A_cubic']
        res = {'phi_json': os.path.basename(phij), 'phi_sha256': sha256_file(phij), 'background': bg['meta'], 'mesh': {'Nr': mesh.Nr, 'Nt': mesh.Nt}, 'report_FLOAT': rp, 'A_B_exact_recomputed': [q2s(A), q2s(B)], 'label': 'FLOAT (binary64 quadrature on the stated product mesh; not bounds)'}
        print(json.dumps({k: v for k, v in rp.items()}, indent=1)); json.dump(res, open(outj, 'w'), indent=1)
        if fnpy: np.save(fnpy, comp[(0, 0)].cpu().numpy()); np.save(fnpy.replace('.npy', '_s.npy'), mesh.s.cpu().numpy())
    elif cmd == 'selftest':
        selftest(dev)

def selftest(dev):
    """007 quotient background on a small mesh; a handful of atoms; checks: (1) F_* at a = 0 equals F_007; (2) Jacobian against the exact quartic along a direction;
    (3) normal-equation gradient against finite differences; (4) constraint row against the series at the origin"""
    cand = os.path.join(NUM, 'ref007', 'd2w_j7_n4_E2bal_mid180_quot_exact.json'); pt = os.path.join(HERE, 'phi_bg', 'selftest_007quot_mid8_ang60.pt'); os.makedirs(os.path.dirname(pt), exist_ok=True)
    if not os.path.exists(pt): build_background(cand, 8, 60, pt, dev)
    bg, mesh = load_background(pt, dev)
    cfg = {'groups': [{'modes': [1, 3, 5, 7], 'k_mu': [0], 'k_harm': [0], 'h': [0, 1], 'd': [0, 2], 't': ['1/4', '4']}]}
    atoms = make_atoms(cfg); pf = PhiFit(bg, mesh, atoms, wL2=1.0, sobolev={'P-S1': 1e-6})
    a = np.zeros(pf.n); f0, parts, comp, fld = pf.objective(a)
    print('(1) a = 0: G0* = %.10e against background G0 %.10e' % (pf.report(a, comp, fld)['G0'], bg['meta']['G0_mesh']))
    rng = np.random.default_rng(1); a = 1e-3*rng.standard_normal(pf.n); a[0] = 0.0
    a -= pf.crow*(pf.crow@a)/(pf.crow@pf.crow)
    G, g, phi = pf.normal_equations(a)
    d = 1e-3*rng.standard_normal(pf.n); d -= pf.crow*(pf.crow@d)/(pf.crow@pf.crow)
    t, phit, phi0, c = pf.line_search(a, d, tmax=1.0)
    gd = float(2*torch.as_tensor(d, device=dev, dtype=DT)@g); dGd = float(torch.as_tensor(d, device=dev, dtype=DT)@(G@torch.as_tensor(d, device=dev, dtype=DT)))
    print('(2) quartic c1 %.8e vs 2 g.d %.8e (rel %.1e); c2 (incl. 2 r0.Q) %.8e vs d.G.d %.8e; phi0 %.8e vs normal-eq phi %.8e' % (c[1], gd, abs(c[1]-gd)/abs(gd), c[2], dGd, c[0], phi))
    eps = 1e-6; fp = pf.objective(a+eps*d)[0]; fm = pf.objective(a-eps*d)[0]
    print('(3) FD directional derivative %.8e vs c1 %.8e' % ((fp-fm)/(2*eps), c[1]))
    hf, vf = pf.split(fld); comp, fld = pf.comps(a); hf, vf = pf.split(fld)
    A = sum(q*float(cA) for q, (cA, cB) in zip(a, pf.cAB)); B = sum(q*float(cB) for q, (cA, cB) in zip(a, pf.cAB))
    i0 = int(torch.argmin(mesh.r)); r0 = float(mesh.r[i0]); th = mesh.theta
    hy = hf[(0, 1)][i0]; v2y = vf[('v2', (0, 1))][i0]
    print('(4) origin: h_y at r %.3f: mean %.6e (expect -8A = %.6e); phi_xxy mean %.6e (expect 2A+6B = %.6e)' % (r0, float(hy.mean()), -8*A, float(v2y.mean()), 2*A+6*B))
    print('    atoms:', [(at['n'], at['h'], str(at['b'])[:12], str(at['t']), at['d'], at['branch']) for at in atoms[:6]], '...', pf.n)

if __name__ == '__main__':
    main()
