# Independent numerical check of the checker's exact-jet formulas (2) and (3) for finite Q data.
# rho = r (1-sig) sin th sum_j sig^j B_j(2 sig - 1) cos(2 j th), r = rc sig^(1/2) (1-sig)^(-kap).
# c = psi_xy(0) = -a/4 + int rho_3 r^-2 dr ; q1 - q2 = int_0^inf t^-3 f_4 dt with
# f_4 = (1/2)(rho_3' - 3 rho_3/r) + (1/2)(rho_5' + 5 rho_5/r) (sin 4th coefficient of rho_x), canonical mode formula.
import mpmath as mp
mp.mp.dps = 30
kap = mp.mpf('1.7'); rc = mp.mpf('0.8')
import random
random.seed(3)
B = [[mp.mpf(random.uniform(-1,1)) for _ in range(4)] for j in range(4)]   # B_j(z) = sum_k B[j][k] z^k
def Bj(j,z): return sum(B[j][k]*z**k for k in range(4)) if j < 4 else 0
def Bjp(j,z): return sum(k*B[j][k]*z**(k-1) for k in range(1,4))
def r_of(s): return rc*mp.sqrt(s)*(1-s)**(-kap)
def sig_of(r):
    # invert r = rc sqrt(s) (1-s)^-kap, monotone in s
    return mp.findroot(lambda s: mp.log(r_of(s)) - mp.log(r), (mp.mpf('1e-40'), 1-mp.mpf('1e-30')), solver='anderson')
def b(n,s):   # coefficient of sin(n th) in rho/r
    if n == 1: return (1-s)*(Bj(0,2*s-1) - s*Bj(1,2*s-1)/2)
    k = (n-1)//2
    return (1-s)*(s**k*Bj(k,2*s-1) - s**(k+1)*Bj(k+1,2*s-1))/2
dlogr = lambda s: ((1-s)+2*kap*s)/(2*s*(1-s))
a = Bj(0,-1)
# (2): c via int b3 dlog r
c_num = -a/4 + mp.quad(lambda s: b(3,s)*dlogr(s), [0,mp.mpf('0.5'),1])
c_formula = -a/4 + mp.quad(lambda s: ((1-s)/4+kap*s/2)*(Bj(1,2*s-1)-s*Bj(2,2*s-1)), [0,1])
# (3): q1 - q2 = int e^{-2u} f4 du, u = log t; f4 = (1/2)(b3' - 2 b3) + (1/2)(b5' + 6 b5), ' = d/du
def du(fn, s):   # d/du = d(sig)/du * d/dsig, d sig/du = 1/dlogr
    return mp.diff(lambda ss: fn(ss), s)/dlogr(s)
def f4(s): return (du(lambda ss: b(3,ss), s) - 2*b(3,s))/2 + (du(lambda ss: b(5,ss), s) + 6*b(5,s))/2
# int e^{-2u} f4 du = int (rc^2/r^2)/rc^2 f4 dlogr dsig
q1mq2 = mp.quad(lambda s: f4(s)*(1-s)**(2*kap)/s/rc**2*dlogr(s), [0,mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75'),1])
Hc_num = rc**2*q1mq2
Hc_formula = -Bj(1,-1)/4 + mp.quad(lambda s: (1-s)**(2*kap)*(1+(2*kap-1)*s)*(Bj(2,2*s-1)-s*Bj(3,2*s-1)), [0,1])
print('c  numeric', mp.nstr(c_num,15), ' formula (2)', mp.nstr(c_formula,15), ' diff', mp.nstr(c_num-c_formula,3))
print('Hc numeric', mp.nstr(Hc_num,15), ' formula (3)', mp.nstr(Hc_formula,15), ' diff', mp.nstr(Hc_num-Hc_formula,3))
# also (1): b_c, e_c from direct Taylor of rho along axes: rho_y(0,y) = a + 3 e y^2, rho_y(x,0) = a + b x^2
fm = lambda s: (1-s)*sum((-s)**j*Bj(j,2*s-1) for j in range(4))
fp = lambda s: (1-s)*sum(s**j*Bj(j,2*s-1) for j in range(4))
s0 = mp.mpf('1e-12'); r0 = r_of(s0)
e_num = (fm(s0)-a)/r0**2; b_num = (fp(s0)-a)/r0**2   # rho/y on axes: a + e y^2 (x=0), a + b x^2 (y=0)
bc = 2*Bjp(0,-1)-a+Bj(1,-1); ec = 2*Bjp(0,-1)-a-Bj(1,-1)
print('b_c numeric', mp.nstr(rc**2*b_num,10), ' formula', mp.nstr(bc,10)); print('e_c numeric', mp.nstr(rc**2*e_num,10), ' formula', mp.nstr(ec,10))
print('raw diffs', c_num-c_formula, Hc_num-Hc_formula)
print('Hc_num 30d', mp.nstr(Hc_num,30)); print('Hc_for 30d', mp.nstr(Hc_formula,30))
wrong = -Bj(1,-1)/4 + mp.quad(lambda s: (1-s)**(2*kap)*((1-s)/4+kap*s/2)*(Bj(2,2*s-1)-s*Bj(3,2*s-1)), [0,1])
print('factor-1/4 variant (should differ)', mp.nstr(wrong,15))
print('type', type(Hc_num), type(Hc_formula))
