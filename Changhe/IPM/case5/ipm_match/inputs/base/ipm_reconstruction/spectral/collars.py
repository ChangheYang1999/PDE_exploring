"""Independent sample of Taylor origin and two-term exterior analytic extensions.
All fields physical variables represented by scaled Fourier coefficient triples.
"""
from spectral import *
from polar_origin import PolarOrigin
def collars(d):
 f,g,p=int(d['nf']),int(d['ng']),int(d['p']);c,a,li,lo=[float(d[k]) for k in ['c','a','li','lo']]
 O=PolarOrigin(g,c,a);inner=O.value_jet(d['raw'],with_terms=True);s=1/c;delta=1-s;q=1+s
 def ti(t):
  rate=2*np.arange(g);w=np.exp((t+li)[:,None]*rate);v=w@inner;dt=(w*rate)@inner;dtt=(w*rate**2)@inner
  return v[:,:g],dt[:,:g],v[:,g:2*g],dt[:,g:2*g],dtt[:,g:2*g],v[:,2*g:],dt[:,2*g:]
 n=max(2*f,2*g)+2;l=2*np.arange(n)+1;k=l+1;theta=(np.arange(6*n+12)+.5)*np.pi/(2*(6*n+12))
 so=np.sin(np.outer(theta,l));co=np.cos(np.outer(theta,l))*l;se=np.sin(np.outer(theta,k));ce=np.cos(np.outer(theta,k))*k
 s0=2/len(theta)*se.T@(np.cos(theta)[:,None]*so);s1=2/len(theta)*se.T@(np.sin(theta)[:,None]*co)
 P1=(s*s0-s1)/(k[:,None]**2-q*q);q2=2*s;P2=((2*s-1)*s0-s1)/(k[:,None]**2-q2*q2)
 A=np.zeros(n);G=np.zeros(n);U=np.zeros(n);last=d['v_o'][-1];A[:f]=last[:f];G[:g]=last[f:f+g];U[:g]=last[f+g:]
 G1=P1@A;C2=(2/len(theta))*so.T@(-s*(ce@G1)*(so@A)+q*(se@G1)*(co@A))/(c-1);C1=A-np.exp(-delta*lo)*C2
 P=P1@C1;Q=P2@C2;H=G-P-np.exp(-delta*lo)*Q
 def to(t):
  z=np.exp(-delta*t)[:,None];h=H*np.exp(-(t-lo)[:,None]*(k+q));F=C1+z*C2;Fd=-delta*z*C2;G=P+z*Q+h;Gd=-delta*z*Q-(k+q)*h;Gdd=delta**2*z*Q+(k+q)**2*h
  return F,Fd,G,Gd,Gdd,q*G+Gd,q*Gd+Gdd
 ai=eval_side(np.linspace(-li-30,-li,14),ti,g,g,1.,c,False,384,6)
 ao=eval_side(np.r_[lo,lo+np.geomspace(.0001,80,21)],to,n,n,s,c,True,384,6)
 # Direct primal subtraction at remote t loses raw accuracy (rho ~ exp(s*t)).
 # Factor the known c*s=1 and A_t=-delta*z*C2 analytically before testing raw T.
 nt=8*n+16;angles=2*np.pi*(np.arange(nt)+.2718)/nt
 so2=np.sin(np.outer(l,angles));co2=l[:,None]*np.cos(np.outer(l,angles));ce2=k[:,None]*np.cos(np.outer(k,angles));se2=np.sin(np.outer(k,angles))
 ts=np.r_[lo,lo+np.geomspace(1.e-5,80.,60)];f0,ft0,g0,gt0,_,uu,_=to(ts)
 br=-c*delta*(C2@so2)[None,:]-(g0@ce2)*((s*f0+ft0)@so2)+(uu@se2)*(f0@co2)
 rawfac=(s-delta)*ts;rawfac=np.exp(np.minimum(rawfac,700.))
 factored=dict(weighted_T=float(np.max(abs(br)*np.exp(-delta*ts)[:,None])),raw_T=float(np.max(abs(br)*rawfac[:,None])),endpoint_t=float(ts[-1]),note='finite sampled collar only; cancellation-free c*s=1 form')
 t0=np.array([0.]);vleft=d['v_i'][-1];vright=d['v_o'][0]
 ql=2*vleft[f:f+g]+evalpoly(d['edge_i'],d['v_i'],p,t0,1)[0,f:f+g]
 qr=q*vright[f:f+g]+evalpoly(d['edge_o'],d['v_o'],p,t0,1)[0,f:f+g];jump=qr-ql
 vt=to(np.array([lo]));v0=ti(np.array([-li]));org=np.r_[v0[0][0],v0[2][0],v0[5][0]]
 innerpoint=d['v_i'][0];trace=np.r_[innerpoint[:min(f,g)]-org[:min(f,g)],innerpoint[f:]-org[g:]]
 return dict(origin=ai,far=ao,far_factored=factored,Jkinematic=float(jump[0]),Jdiff=abs(float(jump[0]-d['J'])),Jhigh_kinematic=float(np.max(abs(jump[1:]))),higher_jump=float(d['higher']),origin_jump=float(np.max(abs(trace))),origin_last_degree=float(np.max(abs(inner[-1]))),far_ujump=float(np.max(abs(U-vt[5][0]))),far_C1_last=float(C1[-1]),origin_basis_cond=O.tangent_condition)
if __name__=='__main__':
 for path in sys.argv[1:]:
  p=Path(path);q=np.load(p);o=collars(q);p.with_suffix('.collar.json').write_text(json.dumps(o,indent=2));print(p.stem,o['Jkinematic'],o['Jhigh_kinematic'],o['origin']['transport'],o['far']['transport'],o['origin']['poisson'],o['far']['poisson'],flush=True)
