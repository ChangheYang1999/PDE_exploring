# reconstruct the configuration at the real root (lead): pair U (value 6), quintic V (value 2), A_0 = 1, d = 23
import pickle, mpmath as mp
mp.mp.dps = 50
D = pickle.load(open('case25b.pkl', 'rb')); x = mp.mpf(D['eta']); p = mp.mpf(D['p'])
d, A0, al, be, m = 23, 1, 6, 2, 5
T = A0*x - d; dl = al - be
q = (-dl*x*(2*x - p) + T*p*x - T*x**2)/T
uroots = mp.polyroots([1, -p, q], extraprec=100)
def psum(rts, l): return sum(r**l for r in rts)
# V = v^5 + c1 v^4 + ... + c5: c1..c4 from M_1..M_4 (Newton), c5 from dl x U'... the relation be-version: dl*x*V'(x) - T*V(x) = 0
# Newton: p_l + c1 p_{l-1} + ... + l c_l = 0 ; M_l = A0 (x-1)^l + al pU_l + be pV_l = 0 -> pV_l
pV = [None] + [-(A0*(x - 1)**l + al*psum(uroots, l))/be for l in range(1, m)]
c = [mp.mpf(1)]
for l in range(1, m):
    c.append(-(pV[l] + sum(c[i]*pV[l - i] for i in range(1, l)))/l)
# c5 from dl*x*V'(x) - T*V(x) = 0, V(x) = sum c_i x^(m-i), V'(x) = sum (m-i) c_i x^(m-i-1)
Vx0 = sum(c[i]*x**(m - i) for i in range(m)); Vpx = sum((m - i)*c[i]*x**(m - i - 1) for i in range(m))
c5 = (dl*x*Vpx - T*Vx0)/T; c.append(c5)
vroots = mp.polyroots(c, maxsteps=500, extraprec=200)
nodes = [(al, r) for r in uroots] + [(be, r) for r in vroots]
print('eta', mp.nstr(x, 25), 'n', mp.nstr((x - d)/2, 25), 'T', mp.nstr(T, 10))
print('pair (value 6):', [mp.nstr(r, 15) for r in uroots], 'discriminant', mp.nstr(p**2 - 4*q, 10))
print('five nodes (value 2):', [mp.nstr(r, 15) for r in vroots])
allr = [r for _, r in nodes]
print('min distance between nodes', mp.nstr(min(abs(a - b) for i, a in enumerate(allr) for b in allr[i+1:]), 8),
      '| min |node|', mp.nstr(min(abs(a) for a in allr), 8), '| min |node - eta|', mp.nstr(min(abs(a - x) for a in allr), 8),
      '| min |node - (eta - 1)|', mp.nstr(min(abs(a - (x - 1)) for a in allr), 8))
print('real nodes:', sum(1 for r in allr if abs(mp.im(r)) < mp.mpf(10)**-30))
e = len(allr) - 1
for l in range(1, e + 1):
    Ml = A0*(x - 1)**l + sum(w*r**l for w, r in nodes)
    print('M_%d' % l, mp.nstr(abs(Ml), 5), end='; ')
pi_p = sum(1/(x - r) for r in allr)
S = sum(w/(x - r) for w, r in nodes) + T/x
print("\npi'(eta)/pi(eta)", mp.nstr(abs(pi_p), 5), '| sum A_j/(eta - zeta_j) + T/eta', mp.nstr(abs(S), 5))
# original nodes v_j = zeta_j/(eta - 1), z = eta/(eta - 1); u_j = 1/v_j - 1 (u-poles), tau = 1 - v (squares alpha^2)
print('v_j:', [mp.nstr(r/(x - 1), 12) for r in allr])
print('tau_j = 1 - v_j (alpha^2):', [mp.nstr(1 - r/(x - 1), 12) for r in allr])
