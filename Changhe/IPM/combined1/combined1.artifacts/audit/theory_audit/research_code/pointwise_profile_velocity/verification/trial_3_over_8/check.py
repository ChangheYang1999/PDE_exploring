from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,time,math,sys
from flint import fmpq as Q,arb,ctx
from geometry import velocity,dot
B=Path(__file__).resolve().parents[1];start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==m['proof_sha256']
assert sha(B/'code/geometry.py')==m['geometry_sha256']
for rel,d in m['inputs'].items():assert sha(B/rel)==d,rel
p=json.loads((B/'data/parameters.json').read_text());ctx.prec=p['precision_bits']
E=Q(p['E']);assert E==Q(3,8);scale=Q(p['profile_scale'])
M=p['theta_cells'];D=p['witness_cells'];N=p['initial_projective_cells'];maxdepth=p['max_depth']
conv=lambda x:arb(x.p)/x.q
pi=arb.pi();hk=pi/(4*M)
rows=[]
print('START',datetime.now(timezone.utc).isoformat(),flush=True)

def quad(co,ca,sa):return co[0]+co[1]*ca+co[2]*sa

def abc(x,y,z):return ((x+z)/2,(x-z)/2,y)

for name in p['candidates']:
 st=time.monotonic();ep=json.loads((B/'data'/f'{name}_endpoint.json').read_text());c=Q(ep['c']);q=1/c-4
 assert -5<q<-3
 ff=[{int(n):Q(v) for n,v in ep['F12'].items()},{int(n):scale*Q(v) for n,v in ep['P'].items()}]
 vv=[velocity(f,q+2) for f in ff]
 polys=[dot(vv[0],vv[0]),dot(vv[0],vv[1]),dot(vv[1],vv[1])]
 modes=sorted(set().union(*(x.keys() for x in polys)))
 assert all(n%2==0 for n in modes)
 coeff={n:abc(*(conv(d.get(n,Q(0))) for d in polys)) for n in modes}
 F=[];FP=[]
 for j in range(M):
  th=pi*(2*j+1)/(4*M)
  sc={n:(n*th).sin_cos() for n in modes}
  F.append(tuple(sum((co[k]*sc[n][1] for n,co in coeff.items()),arb(0)) for k in range(3)))
  FP.append(tuple(sum((-n*co[k]*sc[n][0] for n,co in coeff.items()),arb(0)) for k in range(3)))
 QW=[];QF=[]
 for d in range(D+1):
  ph=pi*d/(2*D);values=[]
  for f in ff:
   fv=sum((conv(v)*(n*ph).sin() for n,v in f.items()),arb(0))
   fd=sum((n*conv(v)*(n*ph).cos() for n,v in f.items()),arb(0))
   values.append((conv(q)*fv,fd))
  a,b=values
  w=abc(a[0]**2+a[1]**2,a[0]*b[0]+a[1]*b[1],b[0]**2+b[1]**2)
  QW.append(w);QF.append(tuple(float(v.mid()) for v in w))
 print('PREPARED',name,'seconds',time.monotonic()-st,flush=True)
 stack=[(Fraction(-1,2)+Fraction(j,N),Fraction(-1,2)+Fraction(j+1,N),0) for j in reversed(range(N))]
 cells=[];attempts=0;point_checks=0;rejected=0
 while stack:
  l,r,depth=stack.pop();attempts+=1
  mid=(l+r)/2;half=(r-l)/2
  am=pi*arb(mid.numerator)/mid.denominator;h=pi*arb(half.numerator)/half.denominator
  sa,ca=(2*am).sin_cos()
  ialpha=arb(am,h);sia,cia=(2*ialpha).sin_cos()
  af=float(mid)*math.pi;caf=math.cos(2*af);saf=math.sin(2*af)
  witness=max(range(D+1),key=lambda k:QF[k][0]+QF[k][1]*caf+QF[k][2]*saf)
  base=tuple(conv(E*E)*x for x in QW[witness])
  M2=sum((n*n*abs(quad(co,cia,sia)) for n,co in coeff.items()),arb(0))
  err2=M2*hk*hk/2
  minimum=None;minj=None;passed=True
  for j in range(M):
   t=tuple(base[k]-F[j][k] for k in range(3))
   slope=2*(-t[1]*sa+t[2]*ca)
   rem=2*(t[1]*t[1]+t[2]*t[2]).sqrt()*h*h
   low=quad(t,ca,sa)-abs(slope)*h-rem
   err1=abs(quad(FP[j],cia,sia))*hk
   gap=low-err1-err2;point_checks+=1
   if not gap>0:
    passed=False;rejected+=1;break
   gl=gap.lower()
   if minimum is None or gl<minimum:minimum=gl;minj=j
  if passed:
   cells.append({'left_pi':str(l),'right_pi':str(r),'depth':depth,'witness_index':witness,'minimum_gap_lower':minimum.str(30),'minimum_theta_cell':minj,'theta_cells_checked':M})
  else:
   if depth>=maxdepth:
    failure={'candidate':name,'left':str(l),'right':str(r),'depth':depth,'theta_cell':j,'gap':str(gap),'utc':datetime.now(timezone.utc).isoformat()}
    (B/'verification/failure.json').write_text(json.dumps(failure,indent=2)+'\n')
    raise AssertionError(failure)
   stack.append((mid,r,depth+1));stack.append((l,mid,depth+1))
  if attempts%32==0:
   print('PROGRESS',name,attempts,'accepted',len(cells),'pending',len(stack),'checks',point_checks,'seconds',time.monotonic()-st,flush=True)
 cells.sort(key=lambda x:Fraction(x['left_pi']))
 assert Fraction(cells[0]['left_pi'])==Fraction(-1,2) and Fraction(cells[-1]['right_pi'])==Fraction(1,2)
 assert all(Fraction(cells[j]['right_pi'])==Fraction(cells[j+1]['left_pi']) for j in range(len(cells)-1))
 assert all(Fraction(x['left_pi'])<Fraction(x['right_pi']) and x['theta_cells_checked']==M for x in cells)
 row={'candidate':name,'q_exact':str(q),'attempts':attempts,'rejected_parent_cells':rejected,'accepted_projective_cells':len(cells),'theta_point_checks':point_checks,'accepted_rectangle_count':len(cells)*M,'max_depth':max(x['depth'] for x in cells),'elapsed_s':time.monotonic()-st,'cells':cells}
 rows.append(row)
 print('CANDIDATE PASS',name,len(cells),row['max_depth'],row['elapsed_s'],flush=True)
 (B/'verification/progress.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'completed':rows},indent=2)+'\n')
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'E_exact':str(E),'profile_scale_exact':str(scale),'theta_cells':M,'witness_cells':D,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'geometry_sha256':sha(B/'code/geometry.py'),'manifest_sha256':sha(B/'data/manifest.json'),'rows':rows,'verdict':'CONFIRMED finite certificate; analytic and numerical independent review pending','finite_radius_claimed':False}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n')
print('ALL PASS',r['utc'],r['elapsed_s'],flush=True)
