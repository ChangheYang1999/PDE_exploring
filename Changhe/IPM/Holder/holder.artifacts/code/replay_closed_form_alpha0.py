"""Independent alpha-zero upper remainder with no transport-plan selection.

At exponent zero the four-point orbit cost is max(a,b), off null axes.
Every positive exterior chord has cost one. Hence the extracted flow and
its residual sum to the half-circle variation bound, independent of the
chosen integer flow. This evaluates the same mathematical limit with a
simpler enclosure, using 192-bit Arb and exact rational geometry.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,time
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/closed_form_lead'
ctx.prec=192
pi=arb.pi()
def record(v):
 assert v.is_finite()
 return dict(lower=str(v.lower().fmpq()),upper=str(v.upper().fmpq()),display=v.str(35,more=True))
def main():
 start=time.monotonic();n=384;m=16;nt=512;nr=128;v=arb(1)/4
 phases=[((pi*j/(2*m)).cos(),(pi*j/(2*m)).sin()) for j in range(m+1)]
 compact=[arb(0) for _ in phases]
 for i in range(n):
  u=(arb(i)/n).union(arb(i+1)/n);p=pi*u/2;r=p.sin();s=u/2
  wm=r*p.cos()*p*pi;wc=s*pi
  for j in range(n):
   t=(arb(j)/n).union(arb(j+1)/n);theta=pi/2-p+p*t
   z=acb(r*theta.cos(),r*theta.sin())
   g=z/(pi*(z*z-arb(1)/4)**2)
   zc=acb(1+s*(pi*t).cos(),s*(pi*t).sin())
   h=1/(2*pi*zc*zc)
   gr,gi=abs(g.real),abs(g.imag);hr,hi=abs(h.real),abs(h.imag)
   for k,(c,sn) in enumerate(phases):
    compact[k]+=wm*arb.max(gr*c,gi*sn)+wc*arb.max(hr*c,hi*sn)
  if i%32==0:print('compact',i,n,time.monotonic()-start,flush=True)
 compact=[z/(n*n) for z in compact]
 far=[arb(0) for _ in phases];width=2*pi/nt
 points=[]
 for j in range(nt//2):
  th=pi*(2*j+1)/nt;points.append(acb(th.cos(),th.sin()))
 for b in range(nr):
  ul=v+(1-v)*b/nr;uh=v+(1-v)*(b+1)/nr
  q=(ul*ul/4).union(uh*uh/4);qu=arb(q.upper())
  M1=3*(1+qu)/(pi*(1-qu)**3)
  M2=9*(1+4*qu+qu*qu)/(pi*(1-qu)**4)
  values=[z**(-3)/(pi*(1-q*z**(-2))**2) for z in points]
  spread=arb(0,(M1*width/2).upper())
  taylor=arb(0,(M2*width**3/24).upper())
  for k,(c,sn) in enumerate(phases):
   tv=arb(0)
   for z in values:
    mid=z.real*c-z.imag*sn;domain=mid+spread
    if domain>0:bound=mid*width+taylor
    elif domain<0:bound=-mid*width+taylor
    else:bound=width*abs(domain)
    tv+=arb(bound.upper())
   far[k]+=tv*(uh-ul)
  if b%16==0:print('far',b,nr,time.monotonic()-start,flush=True)
 N=24;tail=2*v/pi
 for k in range(1,N):tail+=2*(k+1)*arb(4)**(-k)*v**(2*k+1)/(pi*(2*k+1))
 tail+=arb(0).union((1+arb(1)/N)*arb(4)**(-N)*v**(2*N+1)/(pi*(1-arb(1)/4)))
 far=[z+tail for z in far]
 total=[x+y for x,y in zip(compact,far)];mx=total[0]
 for z in total[1:]:mx=arb.max(mx,z)
 result=mx/(pi/(4*m)).cos();target=arb(993975)/1000000
 assert result<target,(result,target)
 data=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,
  compact_cells=n,phases=m,far_angles=nt,far_radial=nr,tail_terms=N,
  compact=[record(z) for z in compact],far=[record(z) for z in far],
  remainder=record(result),target='0.993975',margin=record(target-result),
  elapsed_seconds=time.monotonic()-start,auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  verdict='CONFIRMED alpha-zero remainder <=0.993975 by independent geometric recomputation with all transport dependence eliminated at the limit.')
 (BASE/'verification').mkdir(exist_ok=True)
 (BASE/'verification/alpha0_replay.json').write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({k:data[k] for k in ['time_utc','remainder','margin','elapsed_seconds']},indent=2))
if __name__=='__main__':main()
