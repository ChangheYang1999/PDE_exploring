"""Far-field weak probe from the EXACT sector table: for large k the pairing I_k = int F phi_k dX is dominated by r of order sqrt(k) where F equals its
exact far-field expansion sum_e r^e S_e(theta) (convergent beyond some radius).  I_k^far(k) = | sum_e sigma_e T_e(k) |, sigma_e = pi s_1(e) (sin theta
coefficient of the sector, exact rational), T_e(k) = (1/2) B(k + (e+3)/2, (1-e)/2) (exact Beta integral of r^(e+2) t^k u0^2 over r > 0).  The part of the
pairing from r < R is bounded by G0 ||phi_k||_(L2(r<R)) <= G0 t_R^k sqrt(pi/12) (Cauchy-Schwarz), and the truncation of the sector list at exp_min is
reported through the size of the last terms.  D_k: A_k exact (astra formula), B_k and C_k scaled from the k = 4096 FLOAT mesh values by
(k/4096)^(gamma/2 - 3/2) (ESTIMATE).  argv: exact_json exp_min G0 weaktests2_json out_json"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import mpmath as mp, time, hashlib
mp.mp.dps = 40
path = sys.argv[1]; EXP_MIN = float(sys.argv[2]); G0 = float(sys.argv[3]); wt = json.load(open(sys.argv[4])); outp = sys.argv[5]
c, gens, coefs_q, _ = OPT.load_candidate_json(path); cf = X.qfloat(c); gamma = 1/cf
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
t0 = time.time(); E, dsec, ssec, mom = X.residual_sectors(c, terms, 3, exp_min=X.mpq(EXP_MIN)); print('sectors to', EXP_MIN, 'in', time.time()-t0, 's', flush=True)
secs = []
for ex_, Sd in E.items():
    if 1 in Sd and Sd[1] != 0:
        secs.append((X.qfloat(ex_), X.qfloat(Sd[1]), math.sqrt(math.pi*sum(float(X.qfloat(v))**2 for v in Sd.values()))))
secs.sort(key=lambda z: -z[0])
print('sectors with a sin(theta) component (exponent, s_1, full-circle norm):'); [print(f'  e {e:+.4f}  s_1 {s1:+.6e}  norm {nm:.4e}') for e, s1, nm in secs]
def T(e, k): return mp.mpf(1)/2*mp.beta(k+(e+3)/2, (1-e)/2)
def A(k): return math.sqrt(math.pi/(2*(2*k+2)*(2*k+3))*(1+2*cf+3*cf*cf-6*cf*cf/(2*k+5)))
W = wt['NORM-T-WEAK-v1_a0']; kref = max(int(k) for k in W); Bref, Cref = W[str(kref)]['B_k'], W[str(kref)]['C_k']
print(f'reference k {kref}: A {W[str(kref)]["A_k"]:.4e} (exact formula {A(kref):.4e}) B {Bref:.4e} C {Cref:.4e}')
rows = []
for lk in [3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]:
    k = int(round(10**lk))
    terms_k = [(e, float(mp.pi*s1*T(e, k))) for e, s1, nm in secs]
    Ifar = abs(sum(v for e, v in terms_k)); lead = terms_k[0][1]; last = terms_k[-1][1]
    Ak = A(k); Bk = Bref*(k/kref)**(gamma/2-1.5); Ck = Cref*(k/kref)**(gamma/2-1.5); Dk = Ak+Bk+Ck
    near = {R: G0*(R*R/(1+R*R))**k*math.sqrt(math.pi/12) for R in (30, 100, 300, 1000, 3000)}
    rpeak = math.sqrt((2*k+secs[0][0]+2)/(2-secs[0][0]))
    m = Ifar/Dk
    rows.append({'k': k, 'r_peak_dr': rpeak, 'I_far': Ifar, 'leading_term': lead, 'last_term': last, 'A_k': Ak, 'B_k_est': Bk, 'C_k_est': Ck, 'm_far_est': m, 'near_field_bound_by_R': near, 'terms': terms_k})
    print(f'k {k:>11d} r_peak {rpeak:8.1f}  I_far {Ifar:.4e} (lead {lead:+.3e}, last {last:+.3e})  A {Ak:.3e} B {Bk:.2e} C {Ck:.2e}  m_far {m:.4e}  near bound R=100 {near[100]:.1e} R=300 {near[300]:.1e} R=1000 {near[1000]:.1e}', flush=True)
json.dump({'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'exp_min': EXP_MIN, 'G0_used': G0, 'sectors_sin1': secs, 'rows': rows,
           'label': 'I_far EXACT-formula (float evaluation of exact sector sums; sector list truncated at exp_min); A_k exact formula; B_k, C_k scaled ESTIMATES; near-field bound G0 t_R^k sqrt(pi/12) rigorous given G0'}, open(outp, 'w'), indent=1)
print('written', outp)
