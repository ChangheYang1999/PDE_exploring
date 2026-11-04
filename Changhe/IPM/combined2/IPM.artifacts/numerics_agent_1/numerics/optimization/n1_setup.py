"""Shared setup for lane numerics_agent_1 (N1): paths relative to the lane, state 131 reference, exact stationary targets, constraint builders.
All paths are derived from this file's location; nothing absolute."""
import sys, os, json, math, numpy as np, torch
HERE = os.path.dirname(os.path.abspath(__file__)); NUM = os.path.dirname(HERE); LANE = os.path.dirname(NUM)
sys.path.insert(0, os.path.join(NUM, 'lib'))
import ipm_exact as X, ipm_eval as EV, ipm_opt as OPT, ipm_opt2 as O2, ipm_farpart as FP
sys.path.insert(0, os.path.join(NUM, 'n2_code'))
import ipm_polar as _PL; _PL.rderiv_table(8)      # build the module-level radial-derivative table once at the largest order used anywhere (the cache ignores later amax arguments)
try:
    import ipm_legqs; ipm_legqs.install()        # numerics_agent_2's analytic radial jets for legqs generators (validated against autograd to 1e-12 by numerics_agent_2)
except Exception as _e:
    print('ipm_legqs not installed:', _e)
torch.set_num_threads(int(os.environ.get('IPM_THREADS', '1')))
from gmpy2 import mpq
CK131 = os.path.join(NUM, 'source_copy', 'accepted_00000131.json')
SO12 = os.path.join(NUM, 'far_field', 'state131_stationary_orders_0_12.json')
REF007 = os.path.join(NUM, 'ref007', 'd2w_j7_n4_E2bal_mid180_exact.json')
REF007_SHA = 'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'

def load131():
    J = json.load(open(CK131))
    c, terms, rec, raw = X.load_case4_state(CK131)
    return J, c, terms

def stationary_targets(jmax):
    SO = json.load(open(SO12))
    return {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, jmax+1)}

def add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=None):
    """center; Theta_0 fixed (leading moments of branch 0 for all m present); zero q=1 moments of branches in desc_zero;
    branch leading moments = branch_targets[j] (cos dict harmonic 2m -> value) for the m present in the basis.  (c1-n1 candA_setup, unchanged.)"""
    prob.add_center()
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

def build_mesh(MID, ANG, RCUT, RMAX, dev, origin_order=48):
    s, ws, bl = EV.whole_axis_radial(origin_order=origin_order, middle_order=MID); keep = (np.exp(s) >= RCUT) & (np.exp(s) <= RMAX); s, ws = s[keep], ws[keep]
    th, wth = EV.angular_midpoint(ANG); return EV.Mesh(s, ws, th, wth, dev)

def sha256_file(path):
    import hashlib; return hashlib.sha256(open(path, 'rb').read()).hexdigest()
