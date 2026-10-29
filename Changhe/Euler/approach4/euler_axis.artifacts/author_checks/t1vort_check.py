# Lead check of the referee's t1vort claims: axis coefficients T_j, the unmatched coefficient U_1 of z^(-3-1/c),
# the 5D harmonic formula, K^2 S = 1/2, and U_1 for the saved best fields.
import sympy as sp, json, time
t0=time.time()
out={}
s,z,y,p,a=sp.symbols('s z y p a',positive=True)
A,B,C,Pvw,Pww,Pvv=sp.symbols('A B C Pvw Pww Pvv')
u=1+a*s+z**2; v=a*s/u; w=z**2/u
P=A+B*v+C*(w-1)+Pvv*v**2/2+Pvw*v*(w-1)+Pww*(w-1)**2/2
def axis_eta(jp):
    ph=z*u**(-jp)*P
    e=-(8*sp.diff(ph,s)+sp.diff(ph,z,2))
    return sp.simplify(e.subs(s,0))
# p is set to six rational values; both sides are polynomials in p of degree <= 4 (from the expansion of u^(-jp)),
# so agreement at six values proves the identity in p.
pvals=[sp.Rational(2,3),sp.Rational(7,10),sp.Rational(5,7),sp.Rational(37,54),sp.Rational(11,15),sp.Rational(13,19)]
okT={1:True,2:True}; okU=True
for pv in pvals:
    for j in (1,2):
        jp=j*pv
        e=axis_eta(jp)
        F=sp.simplify(e*z**(1+2*jp))
        Fy=sp.simplify(F.subs(z,y**sp.Rational(-1,2)))
        ser=sp.series(Fy,y,0,2).removeO()
        T=sp.simplify(ser.subs(y,0))
        Tclaim=8*a*(jp*A-B+C)-2*jp*(2*jp-1)*A
        okT[j]&= sp.simplify(T-Tclaim)==0
        if j==1:
            U1=sp.simplify(sp.diff(ser,y))
            U1claim=-8*a*(pv*(pv+1)*A-(pv+1)*B+2*(pv+1)*C-Pvw+Pww)+(2*pv+1)*(2*pv+2)*(pv*A+C)
            okU&= sp.simplify(U1-U1claim)==0
out['T1_matches']=bool(okT[1]); out['T2_matches']=bool(okT[2]); out['U1_matches']=bool(okU)
# exponent ordering for k = 1/c in (4/3, 2)
k=sp.symbols('k')
out['ordering_1<k<2']=str(sp.solve_univariate_inequality(sp.And(1+2*k<3+k),k))+' and '+str(sp.solve_univariate_inequality(3+k<1+3*k,k))
# 5D harmonic formula: -Delta_5 (R^-g Y_l) = [l(l+3) + g(3-g)] R^(-g-2) Y_l, check for l = 0..3 with Gegenbauer C_l^(3/2)
g=sp.symbols('g',positive=True); r,zz=sp.symbols('r zz',positive=True)
Rr=sp.sqrt(r**2+zz**2)
ok=True
for l in range(4):
    Y=sp.gegenbauer(l,sp.Rational(3,2),zz/Rr)
    f=Rr**(-g)*Y
    lap=sp.diff(f,r,2)+3/r*sp.diff(f,r)+sp.diff(f,zz,2)
    ok&= sp.simplify(-lap-(l*(l+3)+g*(3-g))*Rr**(-g-2)*Y)==0
out['harmonic_formula_l0to3']=bool(ok)
out['gamma_3_over_4']=str(sp.Rational(3,1)/sp.Rational(3,4)-1)
out['gamma_3_over_5_resonant_l']=[l for l in range(6) if l*(l+3)+4*(3-4)==0]
# numeric: saved fields
import pathlib
base=pathlib.Path('referee/R17/results/best')
num={}
for name in ('c068','c074','free'):
    m=json.load(open(base/name/'metadata.json'))
    c=m['c']; pp=1/(2*c); aa=m['a']
    pol=m['polynomials'][0]
    def coef(J,Kk): return sum(b for jj,kk,b in pol if jj==J and kk==Kk) if False else None
    # P(v,w)=sum b v^j w^k; derivatives at (0,1)
    Av=sum(b for jj,kk,b in pol if jj==0)
    Bv=sum(b for jj,kk,b in pol if jj==1)
    Cv=sum(kk*b for jj,kk,b in pol if jj==0)
    PVW=sum(kk*b for jj,kk,b in pol if jj==1)
    PWW=sum(kk*(kk-1)*b for jj,kk,b in pol if jj==0)
    U1=-8*aa*(pp*(pp+1)*Av-(pp+1)*Bv+2*(pp+1)*Cv-PVW+PWW)+(2*pp+1)*(2*pp+2)*(pp*Av+Cv)
    T1=8*aa*(pp*Av-Bv+Cv)-2*pp*(2*pp-1)*Av
    num[name]=dict(c=c,a=aa,U1=U1,T1_elliptic=T1,T1_transport=m.get('T1_transport'),
                   K2S=m['K2']*m['S'],E=m['E'],referee_U1=m.get('unmatched_integer_axis_coefficient'))
out['saved_fields']=num
out['seconds']=time.time()-t0
print(json.dumps(out,indent=1,default=str))
json.dump(out,open('checks/t1vort_check_output.json','w'),indent=1,default=str)
