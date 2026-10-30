"""Shared setup for the 860-basis experiments: state 131, exact stationary targets, constraint builders."""
import sys, os, json, math, numpy as np, torch
sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/lib')
import ipm_exact as X, ipm_eval as EV, ipm_opt as OPT
torch.set_num_threads(int(os.environ.get('IPM_THREADS', '1')))
from gmpy2 import mpq
LANE = 'RUN_ROOT/numerics_N1N2/numerics'
CK131 = LANE+'/source_copy/case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json'

def load131():
    J = json.load(open(CK131))
    c, terms, rec, raw = X.load_case4_state(CK131)
    return J, c, terms

def truncated_targets(c, terms, hmax, mcut=9):
    """Sequential targets for branches h=1..hmax when the basis only has angular modes m<=mcut (harmonics <= 2mcut+1):
    G_h^target = truncate_{harm<=2mcut+1}( N_h / (h(c-1)) ) with N_h computed from the ACTUAL lower sectors (G_0 exact, G_1..G_{h-1} = targets).
    Returns dict h -> (G_h sine dict, C_h cos dict (potential moments), alpha_h)."""
    gamma = 1/c; lam = 1-gamma
    E, dens, strm, moments = X.residual_sectors(c, terms, qmax=1)
    G = {0: dens[gamma]}; C = {0: X.invert_density(G[0], gamma+3)}; Phi = {0: X.stream_from_potential(C[0], gamma+3)}
    alpha = {n: gamma-n*lam for n in range(hmax+1)}
    out = {}
    for h in range(1, hmax+1):
        S = {}
        for i in range(h):
            j = h-1-i
            S = X.series_sum(S, X.advect(Phi[i], alpha[i]+1, G[j], alpha[j]))
        Gfull = X.scale(S, mpq(1)/(h*(c-1)))
        Gt = {k: v for k, v in Gfull.items() if k <= 2*mcut+1}
        G[h] = Gt; C[h] = X.invert_density(Gt, alpha[h]+3); Phi[h] = X.stream_from_potential(C[h], alpha[h]+3)
        out[h] = (Gt, C[h], alpha[h], Gfull)
    return out

def add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=(0, 1), branch_targets=None):
    """center; Theta_0 fixed (leading moments of branch 0 for all m present); zero q=1 moments of branches in desc_zero;
    branch leading moments = branch_targets[j] (cos dict harmonic 2m -> value) for the m present in the basis."""
    prob.add_center()
    gamma = 1/c
    sect, moments = X.potential_sectors(terms, 1)
    p0 = X.p_branch(c, 0)
    ms_present = {}
    for g in prob.gens:
        p = OPT.gen_p(g, c); ms_present.setdefault(p, set()).add(int(g['m']))
    if theta0_fix:
        C00 = sect[(p0, 0)]
        for m in sorted(ms_present.get(p0, [])):
            prob.add_moment(m, p0, 0, C00.get(2*m, mpq(0)), f'theta0_m{m}')
    for j in desc_zero:
        pj = X.p_branch(c, j)
        for m in sorted(ms_present.get(pj, [])):
            prob.add_moment(m, pj, 1, mpq(0), f'desc_j{j}_m{m}')
    if branch_targets:
        for j, Cj in branch_targets.items():
            pj = X.p_branch(c, j)
            for m in sorted(ms_present.get(pj, [])):
                prob.add_moment(m, pj, 0, Cj.get(2*m, mpq(0)), f'lead_j{j}_m{m}')
