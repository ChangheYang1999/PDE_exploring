"""Section 13: direct evaluation of the truncated series and its full stationary residual.
usage: evaluate_series.py CKPT --N 10,20,40,80 --R 2,4,8,16,32 [--out notes/eval_TAG.json]
For each truncation N and radius R (z = R^{-delta}):
  tail_k(N,R)  = z^N sup_theta |d_theta^k f_{N+1}|     (weighted difference rho_{N+1} - rho_N and its angular derivatives, k=0..3)
  resid_k(N,R) = sup_theta | sum_{n=N+1}^{2N} z^{n-1} d_theta^k E_n^{(N)}(theta) |,  E_n^{(N)} = sum_{i+j=n, i,j<=N} [(p_i+1) g_i f_j' - p_j g_i' f_j]
  which is exactly R^{-gamma} times the stationary residual (c_l X + u_N).grad rho_N - rho_N of the truncated series
  (orders n <= N cancel identically by the recursion, verified independently by sympy for low N).
Also prints the partial sums S_N(R, theta) = R^{-gamma} rho_N at a few angles to show convergence of the series itself.
Coefficient arithmetic for E_n in the ring of the checkpoint (arb); grid evaluation of sums in float64 on the arb midpoints
(indicative, not certified; the verifier's research/16_certified_residuals gives rigorous enclosures agreeing to 1e-12)."""
import sys, os, json, argparse, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ffcore import *
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dtheta_odd(a, k):
    """k-th angular derivative of sum a_m sin((2m+1)th) evaluated as (coefficients, kind) kind: 'sin' or 'cos'"""
    a = np.asarray(a, dtype=float); w = 2 * np.arange(len(a)) + 1
    c = a * w ** k; kind = ['sin', 'cos', '-sin', '-cos'][k % 4]
    return c, kind
def sup_grid(c, kind, M=None):
    K = len(c); M = M or max(512, 8 * (2 * K + 1)); th = np.linspace(0, math.pi, M)
    w = 2 * np.arange(K) + 1
    if 'sin' in kind: v = np.sin(np.outer(th, w)) @ c
    else: v = np.cos(np.outer(th, w)) @ c
    return float(np.max(np.abs(v)))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ckpt'); ap.add_argument('--N', default='10,20,40,80'); ap.add_argument('--R', default='2,4,8,16,32,64')
    ap.add_argument('--out', default=None); ap.add_argument('--kmax', type=int, default=2)
    args = ap.parse_args()
    ff = FarField.load(args.ckpt); R_ = ff.R
    Ns = [int(x) for x in args.N.split(',')]; Rs = [float(x) for x in args.R.split(',')]
    gamma = R_.to_float(ff.gamma); delta = R_.to_float(ff.delta); cl = R_.to_float(ff.c_l)
    Nmax = max(ff.f); Ns = [N for N in Ns if N + 1 <= Nmax]
    res = {'ckpt': os.path.relpath(args.ckpt, LANE), 'c_l': cl, 'delta': delta, 'gamma': gamma, 'Nmax_available': Nmax, 'rows': []}
    print(f"ckpt {args.ckpt}: c_l={cl:.12f} delta={delta:.12f} orders available {Nmax}; ring {R_.name} prec {getattr(R_, 'prec', None)}")
    ths = [0.3, 0.9, 1.3]
    for N in Ns:
        t0 = time.time()
        # E_n^{(N)} for n = N+1 .. 2N
        E = {}
        for i in range(1, N + 1):
            for j in range(max(1, N + 1 - i), N + 1):
                n = i + j
                P1, P2 = ff.products(ff.g[i], ff.f[j]); pi1 = ff.p(i) + 1; pj = ff.p(j)
                term = [pi1 * x - pj * y for x, y in zip(P1, P2)]
                if n not in E: E[n] = term
                else:
                    acc = E[n]
                    if len(term) > len(acc): acc = acc + [R_.zero] * (len(term) - len(acc))
                    for m in range(len(term)): acc[m] = acc[m] + term[m]
                    E[n] = acc
        Ef = {n: np.array([R_.to_float(x) for x in E[n]]) for n in E}
        # sanity: E_{N+1} = N (c_l - 1) f_{N+1}
        fN1 = np.array([R_.to_float(x) for x in ff.f[N + 1]])
        chk = Ef[N + 1][:len(fN1)] / (N * (cl - 1)); err = float(np.max(np.abs(chk - fN1)) / np.max(np.abs(fN1)))
        for R in Rs:
            z = R ** (-delta)
            row = {'N': N, 'R': R, 'z': z, 'check_E_N+1_vs_f_N+1_relerr': err}
            for k in range(args.kmax + 1):
                c, kind = dtheta_odd(fN1, k); row[f'tail_k{k}'] = z ** N * sup_grid(c, kind)
                # residual sum
                L = max(len(Ef[n]) for n in Ef); tot = np.zeros(L)
                for n in Ef:
                    c2, _ = dtheta_odd(Ef[n], k); tot[:len(c2)] += z ** (n - 1) * c2
                row[f'resid_k{k}'] = sup_grid(tot, kind)
            # partial sums at a few angles
            S = []
            for th in ths:
                s = 0.0
                for n in range(1, N + 1):
                    a = np.array([R_.to_float(x) for x in ff.f[n]]); s += z ** (n - 1) * float(np.sin(th * (2 * np.arange(len(a)) + 1)) @ a)
                S.append(s)
            row['S_N_at_angles'] = S
            res['rows'].append(row)
            print(f"N={N:4d} R={R:7.2f} z={z:.4f} | tail0={row['tail_k0']:.3e} tail1={row['tail_k1']:.3e} | resid0={row['resid_k0']:.3e} resid1={row['resid_k1']:.3e} | S_N(0.3,0.9,1.3)={S[0]:.8f} {S[1]:.8f} {S[2]:.8f} | chk={err:.1e}")
        print(f"   (N={N} done in {time.time()-t0:.1f}s)")
    if args.out: json.dump(res, open(args.out, 'w'), indent=1)
if __name__ == '__main__': main()
