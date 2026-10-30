"""Exact rational Laurent products and independent compact derivatives."""
from pathlib import Path
import importlib.util,time
from flint import fmpq as Q,fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('own_scaled_radial_packed',ROOT/'research/joint_scaled_factored_weak/code/fields_joint.py');J=importlib.util.module_from_spec(spec);spec.loader.exec_module(J)
Rat,T,V=J.Rat,J.T,J.V

def add(out,key,A):
 ell,kind,n=key
 if n<0:n=-n;A=-A if kind=='s' else A
 if not A or kind=='s' and n==0:return
 key=ell,kind,n;out[key]=out.get(key,Rat())+A
 if not out[key]:del out[key]

def combine(*rows):
 out={}
 for factor,field in rows:
  for key,A in field.items():add(out,key,A*Q(factor))
 return out

def trigproduct(kind,m,other,n):
 if kind==other=='c':return [('c',m+n,Q(1,2)),('c',m-n,Q(1,2))]
 if kind==other=='s':return [('c',m-n,Q(1,2)),('c',m+n,Q(-1,2))]
 if kind=='s':return [('s',m+n,Q(1,2)),('s',m-n,Q(1,2))]
 return [('s',m+n,Q(1,2)),('s',m-n,Q(-1,2))]

def align(field,kind):
 groups={}
 for (ell,k,n),A in field.items():
  assert k==kind;groups.setdefault(ell,[]).append((n,A))
 out={}
 for ell,rows in groups.items():
  powers=tuple(max(A.powers[i] for n,A in rows) for i in range(len(J.SCALES)))
  polys={}
  for n,A in rows:
   P=A.P
   for L,a,b in zip(J.LINEARS,powers,A.powers):
    if a>b:P=P*L**(a-b)
   polys[n]=P
  out[ell]=(powers,polys)
 return out

def pack(groups,kind,stride):
 out={}
 for ell,(powers,polys) in sorted(groups.items()):
  center=max(polys);coeffs=[Q(0)]*(stride*(2*center+1))
  for n,P in polys.items():
   for k,q in enumerate(P):
    coeffs[stride*(center+n)+k]+=q
    coeffs[stride*(center-n)+k]+=q if kind=='c' else -q
  out[ell]=center,powers,Poly(coeffs)
 return out

def product(C,S,log=lambda *s:None):
 if not C or not S:return {}
 t0=time.monotonic();cg=align(C,'c');sg=align(S,'s')
 stride=1+max(P.degree() for powers,polys in cg.values() for P in polys.values())+max(P.degree() for powers,polys in sg.values() for P in polys.values())
 cp,sp=pack(cg,'c',stride),pack(sg,'s',stride);products={}
 for ell,(center,powers,P) in sorted(cp.items()):
  for ell2,(center2,powers2,R) in sorted(sp.items()):
   key=ell+ell2,center+center2,tuple(a+b for a,b in zip(powers,powers2))
   products[key]=products.get(key,Poly([]))+P*R
  log('PACKED_BRANCH',ell,'stride',stride,'seconds',time.monotonic()-t0)
 out={}
 for (ell,center,powers),P in sorted(products.items()):
  assert all(P[stride*center+k]==0 for k in range(stride)),('nonzero central Laurent coefficient',ell,center)
  for n in range(1,center+1):
   pos=[P[stride*(center+n)+k]/2 for k in range(stride)]
   assert all(P[stride*(center-n)+k]==-2*pos[k] for k in range(stride)),('Laurent antisymmetry',ell,n)
   A=Rat(Poly(pos),powers);add(out,(ell,'s',n),A)
 log('PACKED_DONE',len(out),'seconds',time.monotonic()-t0)
 return out

def compact_jet(jet,x,y):
 d=x+y;assert d>=3
 return {(j+1,'s' if y%2 else 'c',n):A.divide_t((d+1)//2) for (j,n),A in jet.deriv(x,y).items()}

def backgrounds(jet):
 return {'rho':combine((-1,compact_jet(jet,2,1)),(-1,compact_jet(jet,0,3))),
         'u1':combine((-1,compact_jet(jet,1,2))),
         'u2':compact_jet(jet,2,1),
         'rho_x':combine((-1,compact_jet(jet,3,1)),(-1,compact_jet(jet,1,3))),
         'rho_y':combine((-1,compact_jet(jet,2,2)),(-1,compact_jet(jet,0,4)))}

def residual(jet,log=lambda *s:None):
 B=backgrounds(jet);out={}
 for (ell,kind,n),A in B['rho'].items():
  linear=jet.c*((Rat(1)-ell*jet.delta*Rat(T))*A+2*Rat(T*V)*A.derivative())-A
  add(out,(ell,kind,n),linear)
 out=combine((1,out),(1,product(B['u1'],B['rho_x'],log)),(1,product(B['rho_y'],B['u2'],log)))
 return out,B

def derivative(field,d,axis,delta):
 assert axis in ['x','y'];out={}
 for (ell,kind,n),A in field.items():
  if d%2==0:
   radial=(Rat(1)-(d+ell*delta)*Rat(T))*A+2*Rat(T*V)*A.derivative();angular=A
  else:
   radial=-(d-1+ell*delta)*A+2*Rat(V)*A.derivative();angular=A.divide_t(1) if n else Rat()
  for k,m,factor in trigproduct('c' if axis=='x' else 's',1,kind,n):add(out,(ell,k,m),radial*factor)
  if n:
   sign=(-1 if kind=='c' else 1)*(-1 if axis=='x' else 1)
   for k,m,factor in trigproduct('s' if axis=='x' else 'c',1,'s' if kind=='c' else 'c',n):add(out,(ell,k,m),angular*(sign*n*factor))
 return out

def all_derivatives(F,delta,order=2):
 D={(0,0):F}
 for d in range(order):
  for a in range(d+2):D[d+1,a]=derivative(D[d,0],d,'y',delta) if a==0 else derivative(D[d,a-1],d,'x',delta)
  for a in range(1,d+1):
   other=derivative(D[d,a],d,'y',delta);assert set(other)==set(D[d+1,a]);assert all(A==D[d+1,a][key] for key,A in other.items())
 return D
