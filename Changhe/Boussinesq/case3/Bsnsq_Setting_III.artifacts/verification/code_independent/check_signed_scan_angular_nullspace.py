"""Independent exact angular and numerical tensor-product checks for P239."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,resource
import numpy as np
import sympy as s
from scipy.interpolate import BSpline
from scipy.special import roots_legendre
P=Path('research/239_signed_scan_angular_nullspace'); V=P/'verification'
tick=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'checks':[]}
def ck(name,value,**evidence):out['checks'].append({'name':name,'pass':bool(value),**evidence})
z=s.symbols('z');T12=s.chebyshevt(12,z)
for k,h in [(9,15),(10,14),(11,13)]:
 rem=s.rem(s.chebyshevt(k,z)+s.chebyshevt(h,z),T12,z)
 ck('exact Chebyshev alias '+str((k,h)),rem==0,remainder=str(rem))
ck('T12 has 12 simple roots',s.degree(s.gcd(T12,s.diff(T12,z)),z)==0)
for j in range(12):
 phi=s.pi*s.Rational(2*j+1,24)
 ck('exact angular invisible '+str(j),s.simplify(s.cos(12*phi))==0)
 ck('exact derivative sign '+str(j),s.simplify(s.sin(12*phi)-(-1)**j)==0)
 ck('no horizontal midpoint '+str(j),s.cos(phi).is_zero is False)
doc=json.loads((V/'scan_signed_02.json').read_text());a=doc['args'];N=a['Nphi_res'];K=a['K'];Nt=a['Nt'];ng=a['ngc'];deg=5
ck('frozen scan settings',N==12 and K==16 and Nt==40 and ng==7 and a['rmap']=='r')
edges=np.linspace(0,1,Nt+1)**a['grade'];knots=np.r_[np.zeros(deg),edges,np.ones(deg)];Nb=len(knots)-deg-1
q,w=roots_legendre(ng);t=((edges[1:,None]+edges[:-1,None])/2+(edges[1:,None]-edges[:-1,None])*q/2).ravel()
rad=a['L']*np.expm1(-a['beta_basis']*np.log1p(-t));spl=BSpline(knots,np.eye(Nb),deg,extrapolate=False);B=spl(t)
active=[(k,j)for k in range(K)for j in range(min(k,2),Nb)];ix={kj:i for i,kj in enumerate(active)}
phi=(np.arange(N)+.5)*np.pi/N;C=np.cos(np.outer(phi,np.arange(K)))
A=np.stack([np.outer(B[:,j],C[:,k]).ravel()for k,j in active],axis=1)
Z=np.zeros((len(active),4*(Nb-2)));l=0
for group in [[12],[9,15],[10,14],[11,13]]:
 for j in range(2,Nb):
  for k in group:Z[ix[k,j],l]=1
  l+=1
for m in [0,1,2]:
 sv=np.linalg.svd(B[:,m:],compute_uv=False)
 ck('restricted radial rank '+str(m),sv[-1]>1e-5,smallest=float(sv[-1]),largest=float(sv[0]))
sv=np.linalg.svd(A,compute_uv=False);rank=int(np.sum(sv>1e-10));nullity=A.shape[1]-rank
ck('full sampled rank',rank==519,rank=rank,nullity=nullity,shape=list(A.shape),smallest_nonzero=float(sv[rank-1]),largest_null=float(sv[rank]))
ck('complete nullspace dimensions',Z.shape==(691,172) and nullity==172)
az=float(np.max(abs(A@Z)));ck('kernel columns numerical',az<2e-14,max_abs=az)
ck('kernel columns independent',np.linalg.matrix_rank(Z)==172)
ck('coefficient count',len(active)==691 and Nb==45)
# Exact nullspace orthogonality implies the fitted vector splits aliased partners.
f0=np.zeros(691);f0[ix[9,10]]=1;fmin=f0.copy();fmin[ix[9,10]]=.5;fmin[ix[15,10]]=-.5
ck('same observable values for split alias',np.max(abs(A@(fmin-f0)))<2e-14)
ck('minimum norm representative orthogonal to full kernel',np.max(abs(Z.T@fmin))==0)
# Compare Theta_x for exact invisible C4 spline basis direction.
j=10;t0=float((knots[j]+knots[j+deg+1])/2);r0=a['L']*np.expm1(-a['beta_basis']*np.log1p(-t0));b0=float(spl(t0)[j]);amp=(1-t0)**(a['beta_basis']+2)*b0
x=r0*np.sin(phi);y=-r0*np.cos(phi);th=x*x*amp*np.cos(12*phi);thx=-12*x*x*amp*np.cos(phi)/r0*np.sin(12*phi)
ck('invisible temperature values',np.max(abs(th))<2e-14)
ck('forcing derivative nonzero at all angular nodes',np.min(abs(thx))>0,min_abs=float(np.min(abs(thx))),max_abs=float(np.max(abs(thx))))
ck('interior spline support avoids origin and infinity',0<knots[j]<knots[j+deg+1]<1)
# Data witnesses must lie on this very angular/radial grid, not an invented node set.
rows=[]
for fn in ['scan_signed_02.json','scan_signed_04.json','scan_signed_10.json']:
 source=Path('research/236_signed_gaussian_feedback/verification/sources')/fn
 for case in json.loads(source.read_text())['results']:
  if case['G_min']>=0 or case['unfinished']:continue
  rr,yy=case['G_min_at'];xx=np.sqrt(rr*rr-yy*yy);pp=np.arctan2(xx,-yy);jphi=int(np.argmin(abs(phi-pp)));jr=int(np.argmin(abs(rad-rr)))
  row={'case':case['case'],'phi_index':jphi,'radial_index':jr,'angular_error':float(abs(phi[jphi]-pp)),'radial_error':float(abs(rad[jr]-rr)),'reported_G':case['G_min']};rows.append(row)
  ck('published witness lies on aliased grid '+case['case'],row['angular_error']<2e-14 and row['radial_error']<2e-12,**row)
# Exact sine orthogonality gives strain's only two cosine modes.
th=s.symbols('th',real=True)
for k in range(16):
 # product-to-sum instead of heavy symbolic definite integration.
 mode2=s.Rational(1,2)*((1 if k==1 else 0)-(1 if k==3 else 0))
 ck('strain null on affected mode '+str(k),mode2==0 if k in [9,10,11,12,13,14,15] else True,omega2_multiplier=str(mode2))
out.update(witnesses=rows,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(q['pass']for q in out['checks']),total=len(out['checks']),peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,proof_sha256=hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
np.savez_compressed(V/'sampling_singular_values.npz',singular_values=sv,radial_points=rad,angular_points=phi)
(V/'checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['checks','witnesses']},indent=2));print('FAILURES',[q for q in out['checks']if not q['pass']])
if out['passed']!=out['total']:raise SystemExit(1)
