# Independent checks for V186 (all_radii), V188 (symmetric_concavity) and fourth_moment.
import sympy as sp, mpmath as mp
mp.mp.dps = 40
t, q, v, al, rho = sp.symbols('t q v alpha rho', positive=True)
# V186: sign polynomial, quadratic, root formula, p(1/4)
p = 1 - sp.Rational(32,9)*t**2 - q**2*(sp.Rational(3,4)+t)**2
quad = (sp.Rational(32,9)+q**2)*t**2 + sp.Rational(3,2)*q**2*t - (1 - sp.Rational(9,16)*q**2)
print('p == -quad:', sp.simplify(p + quad) == 0)
print('discriminant identity:', sp.simplify(sp.Rational(9,16)*q**4 + (sp.Rational(32,9)+q**2)*(1-sp.Rational(9,16)*q**2) - (sp.Rational(32,9)-q**2)) == 0)
ts = (sp.sqrt(sp.Rational(32,9)-q**2) - sp.Rational(3,4)*q**2)/(sp.Rational(32,9)+q**2)
for qq in [sp.Rational(1,10), sp.Rational(1,2), sp.Rational(9,10)]:
    print(' root check q=%s: p(t*)=%s' % (qq, sp.N(p.subs({q:qq, t:ts.subs(q,qq)}), 30)))
print('p(1/4) =', sp.expand(p.subs(t, sp.Rational(1,4))))
# w - H sign: multiply (1-32t^2/9)/(2 pi rho^2 (3/4+t)^2) - 1/(2 pi (1-rho)^2) by 2 pi rho^2 (3/4+t)^2
w = (1 - sp.Rational(32,9)*t**2)/(2*sp.pi*rho**2*(sp.Rational(3,4)+t)**2); H = 1/(2*sp.pi*(1-rho)**2)
print('sign identity:', sp.simplify((w-H)*2*sp.pi*rho**2*(sp.Rational(3,4)+t)**2 - p.subs(q, rho/(1-rho))) == 0)
# J, I integral, K, B_n
f3 = lambda x: x**3*(1-mp.mpf(32)/9*x**2)/(mp.mpf(3)/4+x)**2
f5 = lambda x: x**5*(1-mp.mpf(32)/9*x**2)/(mp.mpf(3)/4+x)**2
I3 = mp.quad(f3, [0, mp.mpf(1)/4]); J = mp.mpf(653)/288 - mp.mpf(63)/8*mp.log(mp.mpf(4)/3)
print('2*int t^3.. =', 2*I3, ' J =', J, ' diff', 2*I3-J, ' J/(7/4608) =', J/(mp.mpf(7)/4608))
c = mp.mpf(3)/4
def B(n):
    return (-c)**n*(1/c-1) + n*(-c)**(n-1)*mp.log(1/c) + sum(mp.binomial(n,j)*(-c)**(n-j)*(1-c**(j-1))/(j-1) for j in range(2,n+1))
for n in [3,5,7]:
    print(' B_%d formula - quad =' % n, B(n) - mp.quad(lambda x: x**n/(c+x)**2, [0, mp.mpf(1)/4]))
K = (B(5) - mp.mpf(32)/9*B(7))/2
print('K =', K, ' quad K =', mp.quad(f5, [0, mp.mpf(1)/4])/2)
# moments of cos^2, cos^4
print('int cos^2 =', mp.quad(lambda th: mp.cos(th)**2, [0, 2*mp.pi])/mp.pi, ' int cos^4 / (3pi/4) =', mp.quad(lambda th: mp.cos(th)**4, [0, 2*mp.pi])/(3*mp.pi/4))
# H moments: 4 pi H int_0^{rho/4} r^3 = rho^4/(512(1-rho)^2);  pi H int r^5 = rho^6/(49152 (1-rho)^2)
r = sp.symbols('r', positive=True)
print('H r^3:', sp.simplify(4*sp.pi*H*sp.integrate(r**3,(r,0,rho/4)) - rho**4/(512*(1-rho)**2)) == 0)
print('H r^5:', sp.simplify(sp.pi*H*sp.integrate(r**5,(r,0,rho/4)) - rho**6/(49152*(1-rho)**2)) == 0)
# fourth-moment scalar inequality A(v) <= 1 - p v^2/2 - q v^4/24, sampled; symmetric quadratic version
worst2 = worst4 = mp.mpf(-1)
for a in [mp.mpf(k)/1000 for k in (1,10,100,300,500,750,900,990,999)]:
    P = a*(1-a); Q = a*(1-a)*(2-a)*(3-a)
    for k in range(1, 400):
        vv = mp.mpf(k)/400
        A = ((1-vv)**a + (1+vv)**a)/2
        worst2 = max(worst2, A - (1 - P*vv**2/2)); worst4 = max(worst4, A - (1 - P*vv**2/2 - Q*vv**4/24))
print('max A-(quadratic bound) =', worst2, ' max A-(quartic bound) =', worst4, '(both must be <= 0)')
# derivative identities
A = ((1-v)**al + (1+v)**al)/2
print("A'''' identity:", sp.simplify(sp.diff(A, v, 4) + al*(1-al)*(2-al)*(3-al)*((1-v)**(al-4)+(1+v)**(al-4))/2) == 0)
print('A(0), A1, A2, A3 at 0:', [sp.simplify(sp.diff(A, v, k).subs(v, 0)) for k in range(4)])
