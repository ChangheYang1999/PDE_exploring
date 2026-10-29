# Lead check of the verifier's exact frozen-constraint repair proof (pole functional, envelope expansions, column derivatives).
import sympy as sp, json, datetime
R,mu,g,k=sp.symbols('R mu gamma k',positive=True)
F=sp.Function('F')
res=[]
def chk(name,ok): res.append(dict(check=name,ok=bool(ok))); print('PASS' if ok else 'FAIL',name)
f=R**(-g)*F(mu)
lap5=sp.diff(f,R,2)+4/R*sp.diff(f,R)+((1-mu**2)*sp.diff(f,mu,2)-4*mu*sp.diff(f,mu))/R**2
G=sp.simplify(-lap5*R**(g+2))
pole=G.subs(mu,1).doit()
target=g*(3-g)*F(1)+4*sp.Subs(sp.diff(F(mu),mu),mu,1).doit()
chk('-Delta_5 (R^-gamma F) = R^(-gamma-2) [gamma(3-gamma)F(1) + 4F\'(1)] at mu = 1',sp.simplify((pole-target).doit())==0)
Z=mu*(1-mu**2)
chk('L_gamma(Z) = -8 for all gamma',sp.simplify(g*(3-g)*Z.subs(mu,1)+4*sp.diff(Z,mu).subs(mu,1)+8)==0)
for j in range(0,6):
    h=mu*sp.legendre(2*j,mu)
    chk('mu P_%d: value 1 and derivative 1 + j(2j+1) at mu = 1'%(2*j),h.subs(mu,1)==1 and sp.diff(h,mu).subs(mu,1)==1+j*(2*j+1))
t=sp.symbols('t',positive=True)  # t = 1/R
for kk in [sp.Rational(4,3)+sp.Rational(1,100),sp.Rational(3,2),sp.Rational(19,10),sp.Rational(199,100)]:
    p=kk/2
    gp=sp.series((1/t)*(1+t**-2)**(-p)*t**(1-kk),t,0,6).removeO()   # g_p / R^(1-k) as a series in t = 1/R
    chk('g_p = R^(1-k) - p R^(-1-k) + O(R^(-3-k)) (k=%s)'%kk,sp.simplify(gp-(1-p*t**2+p*(p+1)/2*t**4))==0)
    pw={'A':1-kk,'B':1-2*kk,'C':-1-kk,'D':1-3*kk}
    chk('four potential powers distinct and ordered A > B > C > D (k=%s)'%kk,pw['A']>pw['B']>pw['C']>pw['D'])
    omitted={'g_2p next':-1-2*kk,'g_(p+1) next':-3-kk,'g_3p next':-1-3*kk,'g_p third':-3-kk}
    chk('omitted envelope terms below R^(1-3k) (k=%s)'%kk,all(v<pw['D'] for v in omitted.values()))
# correction algebra: changes -8h0, -8h1, 8p h0 - 8h2, -8h3 cancel d1, d2, dU, d3
d1,d2,dU,d3,p=sp.symbols('d1 d2 dU d3 p')
h0=d1/8; h1=d2/8; h2=dU/8+p*h0; h3=d3/8
chk('displayed corrections cancel the four differences',[sp.simplify(x) for x in (d1-8*h0,d2-8*h1,dU+8*p*h0-8*h2,d3-8*h3)]==[0,0,0,0])
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_checks=len(res),all_pass=all(r['ok'] for r in res),checks=res)
json.dump(out,open('author_checks/frozen_constraint_proof_check_output.json','w'),indent=1)
print('checks',len(res),'all pass',out['all_pass'])
