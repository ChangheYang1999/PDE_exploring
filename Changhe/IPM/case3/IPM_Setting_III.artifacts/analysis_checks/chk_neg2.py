# s = -1 (signed hydrostatic problem) analogue of 3.78: symbolic inner equations for both signs, and an
# independent ODE check of the count (outward integration of the bounded even/odd solutions from small z).
import sympy as sp, mpmath as mp, numpy as np
from scipy.integrate import solve_ivp
x,y,z,p,K,c=sp.symbols('x y z p K c',positive=True)
mu=(p+1)/2; q=mu*p+p-1; n=mu*p; se=(p+2)*(p-1)/(p+1)
h=sp.Function('h'); w=sp.Function('w')
for sg in (1,-1):
    u=y**q*h(x/y**mu); W=y**n*w(x/y**mu)
    E1=((c*x*sp.diff(u,x)+c*y*sp.diff(u,y)-u)+p*K*y**(p-1)*W)/y**q          # transport, velocity W times d_y f_p
    E2=(sp.diff(W,y,2)+sg*sp.diff(u,x,2))/y**(n-2)                          # V_2yy = -sg g_xixi
    E1=sp.simplify(E1.subs(x,z*y**mu).subs(c,1/p)); E2=sp.simplify(E2.subs(x,z*y**mu))
    # eliminate w with E1: w = -[(mu-c)h + c(1-mu) z h']/(pK); compare with (th-p)(th-se)(th-p-2)h = 2 sg lam h''
    wsol=sp.solve(sp.Eq(E1,0),w(z))[0]
    lhs=sp.simplify(E2.subs(w(z),wsol).doit())
    H=sp.Function('H')
    th=lambda f: z*sp.diff(f,z)
    hh=h(z)
    L=th(th(th(hh)))  # build (th-p)(th-se)(th-p-2) h
    def op(f,a): return sp.expand(th(f)-a*f)
    Lh=op(op(op(hh,p+2),se),p)
    lam=4*p**2*K/((p+1)**2*(1-p))
    target=Lh-2*sg*lam*sp.diff(hh,z,2)
    ratio=sp.simplify(sp.expand(lhs)/sp.expand(target))
    print('sign',sg,': E2 after elimination / [(th-p)(th-s)(th-p-2)h - 2 sg lam h\'\'] =',ratio)
# ---------- numerical count for s = -1 (X = +lam/z^2), K = 1
mp.mp.dps=30
def run(pv):
    pv=mp.mpf(pv); lam=4*pv**2/((pv+1)**2*(1-pv)); sev=(pv+2)*(pv-1)/(pv+1)
    a1=-pv/2; a2=(1-pv)/2; b1=pv/(pv+1); b2=mp.mpf(2)
    # asymptotic series at X -> +inf for u = X^{-a} sum c_k X^{-k}: coefficients from the ODE
    # T(T+b1-1)(T+b2-1)u = X(T+a1)(T+a2)u, T X^m = m X^m: c_{k+1} from X^{-a-k} balance:
    # (m)(m+b1-1)(m+b2-1) c_k = (m-1+a1)(m-1+a2) c_{k+1}, m = -a-k, i.e. c_{k+1} = m(m+b1-1)(m+b2-1)c_k/((m-1+a1)(m-1+a2))
    def ser(a,X,N=None):
        cs=[mp.mpf(1)]; terms=[]
        for k in range(60):
            m=-a-k; den=(m-1+a1)*(m-1+a2)
            if den==0: break
            cs.append(m*(m+b1-1)*(m+b2-1)*cs[-1]/den)
        # optimal truncation
        s=0; best=None
        for k,ck in enumerate(cs):
            t=ck*X**(-a-k)
            if best is not None and abs(t)>abs(best): break
            s+=t; best=t
        return s
    def hfun(a,zz):  # h = z^p u(lam/z^2), with derivatives by mp.diff
        return zz**pv*ser(a,lam/zz**2)
    z0=mp.mpf('0.12')
    out={}
    for name,a in (('E',a1),('O',a2)):
        f=lambda zz: hfun(a,zz)
        y0=[float(f(z0)),float(mp.diff(f,z0)),float(mp.diff(f,z0,2))]
        out[name]=y0
    P=float(pv); S=float(sev); LAM=float(lam)
    # (th-p)(th-S)(th-p-2)h = -2 LAM h''  with th = z d/dz: expand th^3 h = z^3h''' + 3z^2h'' + zh', th^2 h = z^2h''+zh'
    e1=P+S+P+2; e2=P*S+P*(P+2)+S*(P+2); e3=P*S*(P+2)
    def rhs(zz,Y):
        h0,h1,h2=Y
        # z^3 h''' + 3 z^2 h'' + z h' - e1 (z^2 h'' + z h') + e2 z h' - e3 h + 2 LAM h'' = 0
        h3=-(3*zz**2*h2+zz*h1-e1*(zz**2*h2+zz*h1)+e2*zz*h1-e3*h0+2*LAM*h2)/zz**3
        return [h1,h2,h3]
    zs=[20.,50.,100.,200.]
    res={}
    for name,y0 in out.items():
        sol=solve_ivp(rhs,[float(z0),zs[-1]],y0,method='Radau',rtol=1e-11,atol=1e-14,dense_output=True)
        res[name]=[sol.sol(zz) for zz in zs]
    # gamma (coefficient of z^{p+2}): estimate h''/((p+2)(p+1) z^p) at large z
    print('p=%.6f lam=%.6f'%(P,LAM))
    for name in ('E','O'):
        g=[r[2]/((P+2)*(P+1)*zz**P) for r,zz in zip(res[name],zs)]
        print('  %s: h(z0)=%.6e h\'(z0)=%.6e ; z^{p+2} coefficient estimates at z=20,50,100,200: %s'%(name,out[name][0],out[name][1],' '.join('%.6e'%v for v in g)))
    gE=res['E'][-1][2]; gO=res['O'][-1][2]
    kappa=-gE/gO   # E + kappa O has no z^{p+2} at z=200 (estimate)
    cE=mp.gamma(a1)*mp.gamma(1-b1+a1)*mp.gamma(a2-a1)/mp.gamma(b2-a1)
    cO=mp.gamma(a2)*mp.gamma(1-b1+a2)*mp.gamma(a1-a2)/mp.gamma(b2-a2)
    # G = cE X^{-a1}(..) + cO X^{-a2}(..); in terms of the normalized series E,O (leading coeff 1 in X): G = cE E + cO O
    print('  combination without z^{p+2}: O/E ratio from ODE %.8f ; Meijer-G ratio cO/cE %.8f'%(kappa,float(cO/cE)))
    print('  => the admissible-at-infinity bounded solution has odd/even ratio %.4f != 0: not C^1 at the axis'%kappa)
for pv in ('0.25','0.5','0.75','0.41421356237309515'):
    run(pv)
