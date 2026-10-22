"""Draft the independent density-moment derivative engine after the analytic proof."""
from pathlib import Path
import hashlib,ast
R=Path(__file__).resolve().parents[3];D=R/'research/inner_derivative_cells';A=(R/'research/outer_derivative_cells_v2/code/engine_iv.py').read_text()
parent=R/'research/inner_cells/code/cell_integer_iv.py';ph=hashlib.sha256(parent.read_bytes()).hexdigest()
A=A.replace('Analytically differentiated inputs, compressed integer interval convolution.','DRAFT: density-moment inner ODE defects and integer interval convolution.').replace('research/outer_cells/code/cell_integer_iv.py','research/inner_cells/code/cell_integer_iv.py').replace('34b9b2a7d6784f71051946093c7a55d1e4d2acf57b23f399f0bffacb5c402797',ph).replace('outer180_iv_parent','inner181_iv_parent').replace('assert 0<=a<b','assert -5<=a<b<=0')
start=A.index(" beta=d['beta']");end=A.index(' def sums(models):')
block=r''' alpha=d['alpha'];zero=([iv.mpf(0)]*(Q+1),[iv.mpf(0)]*3)
 def mix(ps,offset,s):return combine([[iq(v) for v in p] for p in ps],[al+offset for al in alpha],s)
 def pn(poly,p):return top(sum((abs(poly[l])*falling(l,p)/ha**p for l in range(p,len(poly))),iv.mpf(0)))
 def multiply(x,y):
  poly=[iv.mpf(0)]*(2*Q+1)
  for j,u in enumerate(x[0]):
   for l,v in enumerate(y[0]):poly[j+l]+=u*v
  errors=[]
  for p in range(3):
   er=sum((abs(poly[l])*falling(l,p)/ha**p for l in range(Q+1,2*Q+1)),iv.mpf(0))
   for j in range(p+1):er+=math.comb(p,j)*(pn(x[0],j)*y[1][p-j]+pn(y[0],p-j)*x[1][j]+x[1][j]*y[1][p-j])
   errors.append(top(er))
  return poly[:Q+1],errors
 def ode(y0,lam,sig,G):
  ell=iq(lam*h);powers=[iv.mpf(1)]
  for q in range(1,Q+1):powers.append(powers[-1]*ell)
  poly=[]
  for q in range(Q+1):
   val=y0*powers[q]/math.factorial(q)
   for l in range(q):val+=sig*ha*G[0][l]*math.factorial(l)*powers[q-l-1]/math.factorial(q)
   poly.append(val)
  defect=top(abs(iq(lam)*poly[Q]+sig*G[0][Q]));rate=iq(abs(lam))
  e0=top(iv.exp(abs(ell))*ha*(defect/(Q+1)+G[1][0]));e1=top(rate*e0+G[1][0]+defect);e2=top(rate*e1+G[1][1]+Q*defect/ha)
  return poly,[e0,e1,e2]
 def derivative(ps):return [[(al+3)*p[l]+((l+1)*p[l+1] if l+1<len(p) else 0) for l in range(len(p))] for al,p in zip(alpha,ps)]
 Hhat=[mix(ps,0,iv.mpf(1)) for ps in d['cs']];rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(d['cs'][:261]):
  rho.append(mix(ps,3,d['R3']));D.append(mix(derivative(ps),3,d['R3']));H.append(scale(rho[-1],iq(2*j+1)))
  es=[[F(0)]]+ps[1:];Eta.append(mix(es,3,d['R3']));ED.append(mix(derivative(es),3,d['R3']))
 E=[zero for _ in range(262)];c=iq(3/d['k']-1)
 def sine_add(nu,model,scalar):
  assert nu!=0;dest=(abs(nu)-1)//2;E[dest]=add(E[dest],scale(model,scalar if nu>0 else -scalar))
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;sine_add(nu,dt,1/iq(d['k']));sine_add(nu,eta,iq(-1))
  for freq in [nu+2,nu-2]:sine_add(freq,dt,-c/2)
  for freq in [nu+2,2-nu]:sine_add(freq,eta,c*nu/2)
 er2=scale(term([iv.mpf(1)],F(2)),d['R2']);P=[];S=[]
 for n in range(1,262):
  m=2*n;i0=iv.mpf(0)
  for al,p in zip(alpha,d['cs'][n-1]):
   if any(p):
    q=old.inverse_explicit(p,m+4+al);val=sum((x*tc**l for l,x in enumerate(q)),F(0));i0+=iv.exp(iq(al*tc))*iq(val)
  im=ode(i0,-m-4,1,Hhat[n-1]);avg=scale(add(Hhat[n-1],Hhat[n]),iq(F(1,2)));Adiv=multiply(er2,add(avg,scale(im,iq(-m))))
  if n==1:Bdiv=mix(d['b1'],2,d['R2'])
  else:
   j0=iv.exp(iq((m-4)*tc))*d['J0'][n-1]
   for al,p in zip(alpha,d['cs'][n]):
    if any(p):j0+=iv.exp(iq(al*tc))*old.integrals.integrate(p,tc,-tc,4-m+al)
   jm=ode(j0,m-4,-1,Hhat[n]);Bdiv=multiply(er2,add(scale(jm,iq(m)),scale(avg,iq(-1))))
  P.append(scale(add(Adiv,Bdiv),iq(F(-1,2))));S.append(scale(add(Bdiv,scale(Adiv,iq(-1))),iq(F(1,2))))
 cross_input_checks=0;cross_input_hash=hashlib.sha256()
 if primary is not None:
  assert primary['Q']==Q and primary['left_exact']==str(a) and primary['right_exact']==str(b)
  for name,models in [('P',P),('S',S),('D',D),('H',H),('E',E)]:
   targets=primary['input_coefficients'][name];assert len(targets)==len(models)
   for j,(poly,er) in enumerate(models):
    assert len(targets[j])==len(poly)==Q+1
    for p in range(3):
     for l in range(p,Q+1):
      target=targets[j][l];factor=F(falling(l,p),1)/h**p;lo,hi=F(target['lower_exact'])*factor,F(target['upper_exact'])*factor;v=poly[l]*iq(factor);vlo,vhi=ends(v)
      assert max(lo,vlo)<=min(hi,vhi),('inner independent input jets disjoint',name,j,p,l)
      cross_input_hash.update((name+' '+str(j)+' '+str(p)+' '+str(l)+' '+str(lo)+' '+str(hi)+' '+str(vlo)+' '+str(vhi)+'\n').encode());cross_input_checks+=1
  assert cross_input_checks==(4*261+262)*(3*Q)
'''
A=A[:start]+block+A[end:]
A=A.replace('if n<261:','if n<262:').replace("t=d['tb']+a","t=d['ta']+a").replace('str(524*h)','str(526*h)').replace("'exact_Green_scalar_checks':d['exact_Green_scalar_checks']","'cross_method_input_jet_checks':cross_input_checks,'cross_method_input_jet_sha256':cross_input_hash.hexdigest(),'moment_modes':261")
ast.parse(A);(D/'code/engine_iv.py').write_text(A);print('DRAFT_IV_ENGINE_WRITTEN',len(A),ph)
