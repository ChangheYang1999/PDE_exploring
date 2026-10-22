"""Exact source-box arithmetic, symbolic identities and independent Arb/iv constants."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import json,sys,hashlib,time,itertools
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/source_matching/evidence';t0=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
box={'A':[F(10),F(51,5)],'mu':[F(99,100),F(101,100)],'g':[F(29),F(30)]};sigmas=[F(31,10),F(13,4)];rows=[]
for sigma in sigmas:
 vals=[]
 for A,mu,g in itertools.product(*box.values()):
  ky=1+A/2-(sigma-F(1,2))*mu;kx=1+g+mu/2-(sigma-F(1,2))*A
  vals.append({'A':str(A),'mu':str(mu),'g':str(g),'ky':str(ky),'kx':str(kx)})
 ky=min(F(v['ky']) for v in vals);kx=min(F(v['kx']) for v in vals);k=min(ky,kx)
 assert ky==6-(sigma-F(1,2))*F(101,100) and kx==30+F(99,200)-(sigma-F(1,2))*F(51,5) and k>0
 rows.append({'sigma':str(sigma),'corners':vals,'ky':str(ky),'kx':str(kx),'inverse_upper_exact':str(1/k)})
assert [(r['ky'],r['kx'],r['inverse_upper_exact']) for r in rows]==[('1687/500','159/40','500/1687'),('1289/400','489/200','200/489')]
endx=F(1,2)+(30+F(99,200))/F(51,5);endy=F(1,2)+6/F(101,100);assert endx==F(2373,680)<endy==F(1301,202) and min(sigmas)>3 and max(sigmas)<endx
# Check inhomogeneous rates by a different exact expression, including r=0.
rate_checks=0
for sigma in sigmas:
 for A,mu,g in itertools.product(*box.values()):
  for t in [F(0),F(1,10),F(1,2),F(9,10),F(1)]:
   for r2 in [F(0),F(1,100),F(1),F(100),F(10**8)]:
    C=sigma*(A*t+mu*(1-t))*r2/(1+r2)-1-(A+mu)/2-g*t
    upper=-(1+A/2-(sigma-F(1,2))*mu)*(1-t)-(1+g+mu/2-(sigma-F(1,2))*A)*t
    k=min(F(rows[sigmas.index(sigma)]['ky']),F(rows[sigmas.index(sigma)]['kx']));assert C<=upper<=-k;rate_checks+=1
# Exact positive high-frequency example beyond the uniform window, an energy sign only.
sig=F(7,2);A=F(51,5);mu=F(99,100);g=F(29);r2=F(128**2);outside=sig*A*r2/(1+r2)-1-(A+mu)/2-g;assert outside>0
# Symbolic reconstructions, using arbitrary smooth fields where possible.
x,y=s.symbols('x y',real=True);A,mu,g,sigma,c,L,S=s.symbols('A mu g sigma c L S',real=True);u=s.Function('u')(x,y);W=(1+x*x+y*y)**(sigma/2);m=x*x/(x*x+y*y);ns=0

def zero(z):
 global ns
 assert s.simplify(z)==0;ns+=1
Lf=-A*x*s.diff(u/W,x)-mu*y*s.diff(u/W,y)-(A+mu+1+g*m)*u/W
D0=-A*x*s.diff(u,x)-mu*y*s.diff(u,y)-(A+mu)*u/2
C=sigma*(A*x*x+mu*y*y)/(1+x*x+y*y)-1-(A+mu)/2-g*m
zero(W*Lf-D0-C*u)
# Point-row on arbitrary Taylor jets: all unused second/third derivatives cancel.
b,bx,b3,gp,gpp,g3,AP,v20,v11,u1,u1x,u1yy,u2y,u2xy=s.symbols('b bx b3 gp gpp g3 AP v20 v11 u1 u1x u1yy u2y u2xy')
rho=g*y+gp*x*y+gpp*x*x*y/2+g3*y**3;h=b*y+bx*x*y+b3*y**3
V1=AP*x+v20*y*y/2;V2=mu*y+v11*x*y;U1=u1+u1x*x+u1yy*y*y/2;U2=u2y*y+u2xy*x*y
field=V1*s.diff(h,x)+V2*s.diff(h,y)-h+U1*s.diff(rho,x)+U2*s.diff(rho,y)+S*((L+x)*s.diff(rho,x)+y*s.diff(rho,y))/3
zero(s.diff(field,y).subs({x:0,y:0})-((mu-1)*b+g*u2y+gp*u1+S*(g+L*gp)/3))
# General homogeneous factor integrating identity, encoded by its defining derivative.
ph,ph1,beta,J,J1,R,w=s.symbols('ph ph1 beta J J1 R w');D=s.symbols('D')
zero((w*(ph1*(beta+J)+ph*J1)+(mu-1)*ph*(beta+J)-R).subs({ph1:-(mu-1)*ph/w,J1:R/(w*ph)}))
# Origin examples are exact and do not assume a profile.
xp=s.symbols('xp',positive=True);rcoef,bc=s.symbols('rcoef bc');Aval=s.symbols('Aval',positive=True)
for nu in [s.Rational(1,2),s.Rational(2),s.Rational(3)]:
 bb=bc*xp*xp-rcoef/(Aval*nu)*xp**(2+nu);zero(-Aval*xp*s.diff(bb,xp)+2*Aval*bb-rcoef*xp**(2+nu))
bb=xp*xp*(bc-rcoef*s.log(xp)/Aval);zero(-Aval*xp*s.diff(bb,xp)+2*Aval*bb-rcoef*xp*xp)
bb=xp*xp*(bc+s.log(s.log(s.E/xp))/Aval);zero(-Aval*xp*s.diff(bb,xp)+2*Aval*bb-xp*xp/s.log(s.E/xp))
# Scaling commutator with arbitrary density and velocity.
rho=s.Function('rho')(x,y);U=s.Function('U')(x,y);V=s.Function('V')(x,y)
def Euler(z):return x*s.diff(z,x)+y*s.diff(z,y)
Ffield=c*Euler(rho)+U*s.diff(rho,x)+V*s.diff(rho,y)-rho;K=Euler(rho)-rho
LK=c*Euler(K)+U*s.diff(K,x)+V*s.diff(K,y)-K+(Euler(U)-U)*s.diff(rho,x)+(Euler(V)-V)*s.diff(rho,y)
zero(LK-Euler(Ffield)+Ffield)
a20,a02,lam=s.symbols('a20 a02 lam');pol=x*x*y*(1+a20*x*x+a02*y*y)
zero(s.expand((Euler(pol)-pol)).coeff(x,2).coeff(y,1)-2)
zero(s.diff(Euler(pol)-pol,y).subs(y,0)-x*s.diff(s.diff(pol,y).subs(y,0),x))
zero(s.expand(pol.subs({x:lam*x,y:lam*y})/lam).coeff(x,2).coeff(y,1)-lam**2)
# Independent pi enclosure from exact alternating Machin series, not the iv pi constant.
def atan_bounds(q,N):
 q=F(q);sm=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(N)),F());nxt=(-1)**N*q**(2*N+1)/F(2*N+1);return min(sm,sm+nxt),max(sm,sm+nxt)
a,b=atan_bounds(F(1,5),256);d,e=atan_bounds(F(1,239),80);pil=16*a-4*e;pih=16*b-4*d;assert F(3)<pil<pih<F(22,7)
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ae(z):
 assert z.is_finite();out=[]
 for q in [z.lower(),z.upper()]:
  assert q.rad()==0;n,e=q.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def ie(z):return [(-1 if sg else 1)*F(int(n))*F(2)**int(e) for sg,n,e,bc in z._mpi_]
def pack(z):return {'lower_exact':str(z[0]),'upper_exact':str(z[1])}
pii=iv.mpf([ii(pil).a,ii(pih).b]);exports=[]
for row in rows:
 sig=F(row['sigma']);inv=F(row['inverse_upper_exact']);za=ar(inv)/(8*arb.pi()*ar(sig-1)*ar(sig-2)).sqrt();zi=ii(inv)*iv.sqrt(1/(8*pii*ii(sig-1)*ii(sig-2)));ea,ei=ae(za),ie(zi);assert max(ea[0],ei[0])<=min(ea[1],ei[1]);lo=min(ea[0],ei[0]);hi=max(ea[1],ei[1]);pub=(hi//F(1,10**6)+1)*F(1,10**6);assert 0<lo<=hi<pub
 exports.append({'sigma':str(sig),'source_derivative_bound_arb':pack(ea),'source_derivative_bound_iv_machin':pack(ei),'public_strict_upper':str(pub),'scope':'Derivative evaluation norm times the frozen inverse upper bound; not the actual norm of that composition.'})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':sha(B/'research/source_matching/PROOF.md'),'code_sha256':sha(__file__),'parameter_box':{k:[str(v) for v in vs] for k,vs in box.items()},'margins':rows,'window':{'lower':'3','upper_x':str(endx),'upper_y':str(endy)},'rate_inequalities':rate_checks,'symbolic_identities':ns,'outside_window_positive_rate':{'sigma':'7/2','A':'51/5','mu':'99/100','g':'29','r_squared':str(r2),'rate_exact':str(outside),'scope':'Energy sign, not an inverse obstruction'},'machin_pi':{'lower_exact':str(pil),'upper_exact':str(pih),'terms':[256,80]},'derivative_exports':exports,'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-t0,'scope':'Rational frozen parameter theorem and conditional row/matching algebra. No global IPM inverse or candidate enclosure.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':'PASS','rate_checks':rate_checks,'symbolic_identities':ns,'derivative_exports':[{k:v for k,v in z.items() if k in ['sigma','public_strict_upper']} for z in exports],'seconds':out['seconds']}))
