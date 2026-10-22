"""Independent symbolic Cartesian construction versus packet132 formulas."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import argparse,json,time
import sympy as sp
from primitive_local_repair import residual_coefficients,project
from primitive_center_certificate import residual_from_jet

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();root=args.root;root.mkdir(exist_ok=True);tic=time.perf_counter()
x,y=sp.symbols('x y');beta,a0,q,d,e,f,g,h=sp.symbols('beta a0 q d e f g h',nonzero=True)
p=-2*a0/(3*beta)-q/3;c=1+beta/2
Psi=c*x*y+p*x**3+q*x*y**2+d*x**3*y+e*x*y**3+f*x**5+g*x**3*y**2+h*x*y**4
Omega=-sp.diff(Psi,x,2)-sp.diff(Psi,y,2);Wx=beta*x-sp.diff(Psi,y);Wy=beta*y+sp.diff(Psi,x)
F=sp.Poly(sp.expand(Wx*sp.diff(Omega,x)+Wy*sp.diff(Omega,y)+Omega),x,y)
Theta=sum(cc*x**(i+1)*y**j/(i+1)for(i,j),cc in F.terms()if i+j<=3)
RT=sp.Poly(sp.expand(Wx*sp.diff(Theta,x)+Wy*sp.diff(Theta,y)-(beta-2)*Theta),x,y)
jet={(1,1):c,(3,0):p,(1,2):q,(3,1):d,(1,3):e,(5,0):f,(3,2):g,(1,4):h}
claim=residual_coefficients(beta,a0,jet)
for key,val in claim.items():assert sp.cancel(RT.coeff_monomial(x**key[0]*y**key[1])-val)==0
for key,val in RT.terms():
    if sum(key)<=4 and key not in claim:assert sp.cancel(val)==0
rows=[]
for b in [Q(21,10),Q(9,4),Q(5,2),Q(3),Q(4),Q(17,3)]:
 for aa in [Q(1),Q(-2)]:
    j={(1,0):Q(7,13),(1,1):1+b/2,(1,2):Q(2,7),(3,1):Q(-3,11),(1,3):Q(5,17),(5,0):Q(-7,19),(3,2):Q(11,23),(1,4):Q(13,29)};j[(3,0)]=(-4*aa/b-2*j[(1,2)])/6
    actual=residual_from_jet(b,j)['R_Theta'];formula=residual_coefficients(b,aa,j)
    assert all(actual.get(k,0)==v for k,v in formula.items())
    changes,corrected=project(b,aa,j);assert not residual_from_jet(b,corrected)['R_Theta'];assert project(b,aa,corrected)[0]==(0,0,0)
    # Actual R^-8 cutoff expansion, including its degree-six/seven terms.
    full=dict(j)
    for (ii,jj),v in zip([(1,3),(5,0),(1,4)],changes):
      for k in range(3):
       for ell in range(k+1):
        key=(ii+2*ell,jj+2*(k-ell))
        if sum(key)>8:continue
        factor=Q((-1)**k)*Q(int(sp.binomial(k+3,3)))*Q(int(sp.binomial(k,ell)))
        full[key]=full.get(key,0)+factor*v
    cert=residual_from_jet(b,full);assert not cert['R_Theta'];assert cert['a0']==aa and cert['strain']==1+b/2 and cert['omega_x']==4*aa/b
    # A deliberate nonzero change after repair must be detected.
    bad=dict(full);bad[(5,0)]=bad.get((5,0),0)+Q(1,97);assert residual_from_jet(b,bad)['R_Theta']
    rows.append({'beta':str(b),'a0':str(aa),'changes':list(map(str,changes)),'exact_RT_through_degree4_zero':True,'center_preserved':True,'idempotent':True,'tamper_detected':True})
result={'status':'ALL_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'symbolic_cartesian_formula_check':True,'cases':rows,'scope':'Finite Taylor projection only; no global thermal equation or existence assertion.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['elapsed_seconds'],flush=True)
