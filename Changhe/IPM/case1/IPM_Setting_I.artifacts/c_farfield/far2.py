"""Far-field expansion of the normalized residual of a trial to third order (lead, analysis 14.8).
Written independently of the referee's audit script. delta = r^(k-1) (r absolute), alpha_j = k + j (k-1), beta_j = alpha_j + 1.
Formula: rho / (r^k Theta0) = 1 + a1 delta + a2 delta^2 + a3 delta^3 + h r^-2 + (orders beyond delta^3).
Pure-power sector: R_j Theta0 = j (1 - c_l) A_j + sum_{p+q=j-1} [-alpha_q F_p' A_q + beta_p F_p A_q'], A_j = Theta0 a_j,
F_p from A_p by F_{p,n} = G_{p,n} / (4 n^2 - beta_p^2), G the sin(2 n theta) coefficients of alpha_p cos A_p - sin A_p'.
Geometric term: R_h = (c_l (k-2) - 1) h = -2 c_l h. N_v = |rho| + |X.grad rho| + |U.grad rho| expanded with sgn of the
leading U.grad rho. Output: the coefficients q1, q2, qh, q3 of R/N_v = q1 delta + q2 delta^2 + qh r^-2 + q3 delta^3 + ...
usage: python3 far2.py <shape.npz> [theta ...]"""
import sys, json, os
import numpy as np
from numpy.polynomial.chebyshev import chebval, chebder
_here = os.path.dirname(os.path.abspath(__file__))
for _d in ('c7', os.path.join(_here, '..', 'b_fit_domain')):
    if os.path.isdir(_d): sys.path.insert(0, _d)
from trial import Trial
from math import factorial


def coefficients(path, N=1 << 15):
    t = Trial(path); k, L = t.k, t.L; cl = 1/k; a = t.p3-2; r0 = t.origin
    th = 2*np.pi*np.arange(N)/N
    m = np.arange(t.angular+1)
    c, s = np.cos(th), np.sin(th); ac = np.abs(c); sg = np.sign(c)
    cosm = np.cos(2*np.outer(th, m)); dcosm = -2*m*np.sin(2*np.outer(th, m))
    v = ac**a*s**2
    vp = 2*ac**(a+1)*sg*s-a*ac**(a-1)*sg*s**3
    # derivatives in q of b_m(q) and of T(2q-1) at q = 1
    bq = [t.spline(1.0, nu=i) for i in range(4)]
    Tq = [2.0**i*chebval(1.0, chebder(t.singular, i) if i else t.singular) for i in range(4)]
    D = [cosm@bq[i]+Tq[i]*v for i in range(4)]
    Dp = [dcosm@bq[i]+Tq[i]*vp for i in range(4)]
    # H = (k-3) log u + E + sum_i (-1)^i eps^i D_i / i!, eps = 1-q = u^(k-1) (1 + O(u^-2)) = L^(1-k) delta (1 + O(r^-2))
    E, Ep = D[0], Dp[0]
    cc = [None]+[(-1)**i*L**(i*(1-k))*D[i]/factorial(i) for i in (1, 2, 3)]
    ccp = [None]+[(-1)**i*L**(i*(1-k))*Dp[i]/factorial(i) for i in (1, 2, 3)]
    a1 = cc[1]; a2 = cc[2]+cc[1]**2/2; a3 = cc[3]+cc[1]*cc[2]+cc[1]**3/6
    a1p = ccp[1]; a2p = ccp[2]+cc[1]*ccp[1]; a3p = ccp[3]+ccp[1]*cc[2]+cc[1]*ccp[2]+cc[1]**2*ccp[1]/2
    aa = [np.ones(N), a1, a2, a3]; aap = [np.zeros(N), a1p, a2p, a3p]
    pre = L**(3-k)*np.exp(E)
    Th0 = pre*c*c*s
    Th0p = pre*((c**3-2*c*s*s)+c*c*s*Ep)
    A = [Th0*aa[j] for j in range(4)]
    Ap = [Th0p*aa[j]+Th0*aap[j] for j in range(4)]
    alpha = [k+j*(k-1) for j in range(4)]; beta = [x+1 for x in alpha]
    F, Fp = [], []
    for p in range(3):
        g = alpha[p]*c*A[p]-s*Ap[p]
        Gh = np.fft.rfft(g)/N
        sinco = -2*Gh.imag
        jj = np.arange(len(Gh))[2::2]; n = jj//2
        Fn = sinco[2::2]/(4*n*n-beta[p]**2)
        spec = np.zeros(len(Gh), complex); spec[jj] = -0.5j*Fn*N
        F.append(np.fft.irfft(spec, n=N))
        specp = np.zeros(len(Gh), complex); specp[jj] = 0.5*(jj*Fn)*N
        Fp.append(np.fft.irfft(specp, n=N))
    T = [None]
    for j in (1, 2, 3):
        acc = np.zeros(N)
        for p in range(j):
            q = j-1-p
            acc += -alpha[q]*Fp[p]*A[q]+beta[p]*F[p]*Ap[q]
        T.append(acc)                 # U.grad rho at r^alpha_j, times 1 (not normalized)
    sel = (th > 1e-6) & (th < np.pi/2-1e-6)
    with np.errstate(divide='ignore', invalid='ignore'):
        R = [None]+[(j*(1-cl)*A[j]+T[j])/Th0 for j in (1, 2, 3)]
        Tn = [None]+[T[j]/Th0 for j in (1, 2, 3)]
    j_m = np.maximum(m-1, 0)
    h = L*L*((k-3)/2-r0**2*(cosm@(j_m*bq[0]))-t.p3/2*Tq[0]*v)
    Rh = (cl*(k-2)-1)*h
    sgn = np.sign(Tn[1])
    nu = [None]+[((1+alpha[j])*aa[j]+sgn*Tn[j])/(1+k) for j in (1, 2, 3)]
    q1 = R[1]/(1+k)
    q2 = (R[2]-R[1]*nu[1])/(1+k)
    q3 = (R[3]-R[2]*nu[1]-R[1]*(nu[2]-nu[1]**2))/(1+k)
    qh = Rh/(1+k)
    return dict(t=t, k=k, L=L, cl=cl, th=th, sel=sel, q1=q1, q2=q2, q3=q3, qh=qh, R=R, a=aa, h=h, Th0=Th0, Tn=Tn)


if __name__ == '__main__':
    path = sys.argv[1]
    thetas = [float(x) for x in sys.argv[2:]] or [1.56807, 1.5681, 1.56262, 1.54625, 0.81812]
    out = {}
    for N in (1 << 15, 1 << 16):
        o = coefficients(path, N)
        th = o['th']; k, L = o['k'], o['L']
        for t0 in thetas:
            i = int(np.argmin(np.abs(th-t0)))
            key = '%.5f' % t0
            rec = dict(theta=float(th[i]), q1=float(o['q1'][i]), q2=float(o['q2'][i]), qh=float(o['qh'][i]), q3=float(o['q3'][i]),
                       R1=float(o['R'][1][i]), R2=float(o['R'][2][i]), R3=float(o['R'][3][i]), h=float(o['h'][i]))
            pred = {}
            for rL in (500, 1000, 2000, 4701, 7998, 9503, 1e5, 5e5):
                r = rL*L; d = r**(k-1)
                terms = [rec['q1']*d, rec['q2']*d*d, rec['qh']/r**2, rec['q3']*d**3]
                pred['%g' % rL] = dict(terms=terms, sum=sum(terms), ratio_sum_to_leading=sum(terms)/terms[0])
            rec['pred'] = pred
            out.setdefault(key, {})[str(N)] = rec
            print('N %d theta %.5f  q1 %+.8e  q2 %+.6e  qh %+.6e  q3 %+.6e   (R1 %+.4e R2 %+.4e R3 %+.4e h %+.4e)'
                  % (N, th[i], rec['q1'], rec['q2'], rec['qh'], rec['q3'], rec['R1'], rec['R2'], rec['R3'], rec['h']))
            if N == 1 << 16:
                for rL, p in pred.items():
                    print('    r/L %7s  terms %s  sum %+.4e  sum/leading %.4f' % (rL, ' '.join('%+.3e' % x for x in p['terms']), p['sum'], p['ratio_sum_to_leading']))
    json.dump(out, open(os.path.join(_here, 'far2_' + os.path.basename(path).replace('_shape.npz', '') + '.json'), 'w'), indent=1)
