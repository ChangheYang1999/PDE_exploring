"""Lead's quick double-precision look at the recursion (exploratory only; not evidence).
Pseudo-spectral: products on a uniform theta grid, sine coefficients by FFT."""
import numpy as np, sys, math

def run(cl, a1, N, L=None):
    gam = 1.0/cl; dl = 1-gam
    p = lambda n: 1-n*dl
    M1 = max(2*k+1 for k in a1)
    if L is None:
        L = 2*(N*(M1+1)+4)
    th = 2*np.pi*np.arange(L)/L
    # store coefficient arrays (sin(m th) coefficient at index m) and grid values
    F = {}; G = {}
    Fg = {}; Fpg = {}; Gg = {}; Gpg = {}
    def grid_from_sin(c):
        m = np.arange(len(c))
        return (np.sin(np.outer(th, m)) @ c) if len(c) < 64 else sin_eval(c)
    def sin_eval(c):
        # sum c_m sin(m th) via FFT
        Z = np.zeros(L, complex); Z[:len(c)] = c
        return -np.imag(np.fft.fft(Z))*1.0
    def cos_eval(c):
        Z = np.zeros(L, complex); Z[:len(c)] = c
        return np.real(np.fft.fft(Z))
    def sin_coeffs(vals, mmax):
        Z = np.fft.ifft(vals)  # vals = sum c_m sin(m th) -> Z[m] = -c_m/(2i)... use direct formula
        c = np.zeros(mmax+1)
        c[1:] = (-2*np.imag(np.fft.fft(vals))/L)[1:mmax+1]
        return c
    def poisson(n, a):
        P = p(n)+1; pn = p(n)
        mmax = len(a)-1  # odd max freq
        b = np.zeros(mmax+2)
        for m2 in range(2, mmax+2, 2):
            j = m2//2
            am1 = a[2*j-1] if 2*j-1 < len(a) else 0.0
            ap = a[2*j+1] if 2*j+1 < len(a) else 0.0
            b[m2] = ((pn-2*j+1)*am1 + (pn+2*j+1)*ap)/(2*(4*j*j-P*P))
        return b
    a = np.zeros(M1+1)
    for k,v in a1.items(): a[2*k+1] = v
    out = []
    def store(n, a):
        F[n] = a; Fg[n] = sin_eval(a); Fpg[n] = cos_eval(a*np.arange(len(a)))
        b = poisson(n, a); G[n] = b; Gg[n] = sin_eval(b); Gpg[n] = cos_eval(b*np.arange(len(b)))
    store(1, a)
    for n in range(1, N+1):
        if n > 1:
            S = np.zeros(L)
            for i in range(1, n):
                j = n-i
                S += (p(i)+1)*Gg[i]*Fpg[j] - p(j)*Gpg[i]*Fg[j]
            mmax = n*(M1+1)-1
            a = sin_coeffs(S, mmax)/((n-1)*(cl-1))
            a[0::2] = 0.0
            store(n, a)
        al = np.abs(F[n]).sum(); be = np.abs(G[n]).sum(); bep = np.abs(G[n]*np.arange(len(G[n]))).sum()
        d = abs(n*dl - 2*round(n*dl/2))
        out.append((n, al, be, bep, d))
    return out

if __name__ == '__main__':
    cl = float(eval(sys.argv[1])); N = int(sys.argv[2])
    a1 = eval(sys.argv[3]) if len(sys.argv) > 3 else {0:1.0}
    out = run(cl, a1, N)
    for (n, al, be, bep, d) in out:
        if n <= 10 or n % max(1,N//40) == 0:
            print('%4d alpha=%.4e root=%.5f beta=%.3e beta1=%.3e d=%.3e  y=n*alpha/d=%.3e' % (n, al, al**(1.0/n), be, bep, d, n*al/d))
