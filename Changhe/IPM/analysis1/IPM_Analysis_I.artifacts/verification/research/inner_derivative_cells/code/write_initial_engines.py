"""Record a draft implementation after the standalone proof; no production launch."""
from pathlib import Path
import hashlib,ast
R=Path(__file__).resolve().parents[3];D=R/'research/inner_derivative_cells';A=(R/'research/outer_derivative_cells_v2/code/engine_arb.py').read_text()
parent=R/'research/inner_cells/code/cell_arb.py';ph=hashlib.sha256(parent.read_bytes()).hexdigest()
A=A.replace('Analytic falling-factorial remainders, full Fourier Arb convolution.','DRAFT: physical inner Green ODE derivative defects and full Arb convolution.')
A=A.replace("research/outer_cells/code/cell_arb.py","research/inner_cells/code/cell_arb.py").replace('f16dbd13a2362c3ea7f9029af5c7b76ee4ee7a53ece53b9e68251f9641cd122c',ph).replace('outer180_arb_parent','inner181_arb_parent').replace('assert 0<=a<b','assert -5<=a<b<=0')
start=A.index(' beta=d[\'beta\']');end=A.index(' def sums(models):')
block=r''' alpha=d['alpha'];zero=([arb(0)]*(Q+1),[arb(0)]*3)
 def mix(ps,offset,s):return combine([[aa(v) for v in p] for p in ps],[al+offset for al in alpha],s)
 def pn(x,p):return sum((upper(x[l])*fall(l,p)/ha**p for l in range(p,len(x))),arb(0)).upper()
 def multiply(x,y):
  full=arb_poly(x[0])*arb_poly(y[0]);cs=[full[l] for l in range(2*Q+1)];errs=[]
  for p in range(3):
   er=sum((upper(cs[l])*fall(l,p)/ha**p for l in range(Q+1,2*Q+1)),arb(0))
   for j in range(p+1):er+=math.comb(p,j)*(pn(x[0],j)*y[1][p-j]+pn(y[0],p-j)*x[1][j]+x[1][j]*y[1][p-j])
   errs.append(er.upper())
  return cs[:Q+1],errs
 def ode(y0,lam,sig,G):
  lam=aa(lam);sig=arb(sig);poly=[y0]
  for q in range(Q):poly.append(ha*(lam*poly[q]+sig*G[0][q])/(q+1))
  defect=upper(lam*poly[Q]+sig*G[0][Q]);rate=upper(lam)
  e0=(upper(lam*ha).exp()*ha*(defect/(Q+1)+G[1][0])).upper()
  e1=(rate*e0+G[1][0]+defect).upper();e2=(rate*e1+G[1][1]+Q*defect/ha).upper()
  return poly,[e0,e1,e2]
 def point_sum(ps,offset):return sum((aa((al+offset)*tc).exp()*sum((aa(v)*tp[l] for l,v in enumerate(p)),arb(0)) for p,al in zip(ps,alpha)),arb(0))
 def derivative(ps):return [[(3+al)*v+((l+1)*p[l+1] if l+1<len(p) else 0) for l,v in enumerate(p)] for p,al in zip(ps,alpha)]
 rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(d['cs'][:261]):
  rho.append(mix(ps,3,d['R3']));D.append(mix(derivative(ps),3,d['R3']));H.append(scale(rho[-1],arb(2*j+1)))
  es=[[F(0)]]+ps[1:];Eta.append(mix(es,3,d['R3']));ED.append(mix(derivative(es),3,d['R3']))
 E=[zero for _ in range(262)];c=aa(3/d['k']-1)
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;E[j]=add(E[j],add(scale(dt,1/aa(d['k'])),scale(eta,arb(-1))))
  high=scale(add(scale(eta,arb(nu)),scale(dt,arb(-1))),c/2);E[j+1]=add(E[j+1],high)
  low=scale(add(dt,scale(eta,arb(nu))),c/2 if nu==1 else -c/2);dest=(abs(nu-2)-1)//2;E[dest]=add(E[dest],low)
 P=[];S=[];neg2=scale(term([arb(1)],F(-2)),1/d['R2'])
 for n in range(1,262):
  m=2*n;fs=d['forcing'][n-1];A0=d['R4']*point_sum(d['lower'][n-1],4)
  if n==1:B0=d['R4']*point_sum(d['b1'],4)
  else:
   val=aa(m*tc).exp()*d['B0'][n-1]
   for al,p in zip(alpha,fs):
    if any(p):val+=aa((4+al)*tc).exp()*old.moments.integ([aa(x) for x in p],tc,-tc,4+al-m)
   B0=d['R4']*val
  G=mix(fs,4,d['R4']);Am=ode(A0,-m,1,G);Bm=ode(B0,m,-1,G)
  P.append(scale(multiply(neg2,add(Am,Bm)),arb(-1)/2));S.append(scale(multiply(neg2,add(Bm,scale(Am,arb(-1)))),arb(1)/2))
'''
A=A[:start]+block+A[end:]
A=A.replace('le=angular(E,odd,521,True)','le=angular(E,list(range(1,524,2)),523,True)').replace('[arb(0)]*(522*base)+list(le[0])','[arb(0)]*(520*base)+list(le[0])').replace("tleft=d['tb']+a","tleft=d['ta']+a").replace("str(524*h)","str(522*h)")
A=A.replace("if keep:rec['coefficients']=[[out(x) for x in row] for row in coeffs]", "if keep:\n  rec['coefficients']=[[out(x) for x in row] for row in coeffs]\n  rec['input_coefficients']={name:[[out(x) for x in poly] for poly,errs in vals] for name,vals in [('P',P),('S',S),('D',D),('H',H),('E',E)]}")
ast.parse(A);(D/'code/engine_arb.py').write_text(A)
print('DRAFT_ARBITRARY_CELL_ENGINE_WRITTEN',len(A),ph)
