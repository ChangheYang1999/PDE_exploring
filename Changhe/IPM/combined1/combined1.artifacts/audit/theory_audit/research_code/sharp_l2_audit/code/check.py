"""Independent exact LDU, rational kernel, and closure-box certificate."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json,time
ctx.prec=512
root=Path(__file__).resolve().parents[1]
start=time.monotonic()
def atan_bounds(x,N):
 terms=[(-1)**k*x**(2*k+1)/(2*k+1) for k in range(N)]
 partial=sum(terms,F(0));nextterm=(-1)**N*x**(2*N+1)/(2*N+1)
 return min(partial,partial+nextterm),max(partial,partial+nextterm)
a,b=atan_bounds(F(1,5),15);c,d=atan_bounds(F(1,239),5)
pl,pu=16*a-4*d,16*b-4*c
assert F(333,106)<pl<pu<F(355,113)
y=F(1,3);N=8
ll=2*sum((y**(2*k+1)/(2*k+1) for k in range(N)),F(0))
lu=ll+2*y**(2*N+1)/((2*N+1)*(1-y*y))
assert lu<F(1733,2500)
h32=sum((F(1,k) for k in range(1,33)),F(0))
assert h32-5*ll<F(3,5)
eps=F(1,2048);a0=F(1,2)-eps
z=eps*(F(3,5)+2*F(1733,2500))+eps**2*(1/a0**2+1/a0)/2
m=F(393081,250000)
assert pu/(2*(1-z))<m
w=F(1221,1000)
assert w**10>(F(64,5)**5)/6**6
q=F(282094792,10**9)
assert 4*q*q*pl>1
s0=F(1,1024);p=F(283,1000)
assert q*(1+s0)*(1+s0/2)<p
assert w*m<F(48,25)
ku=m;kw=m+F(8,5);tu=3*m/2;tw=3*m/2+F(32,15)
b=1+3*pu*w/4;d=1+pu*w/2
L=w*m*s0;pw=p*(1+L)+q*L
AA=F(4,5)*q+q*(1+4*L)+2*pw;BB=F(9,5)*pw
assert AA+BB<F(8,5)
s2lo=F(7071,5000);s2hi=F(70711,50000)
assert s2lo**2<2<s2hi**2

def pivots(mu,w1,w2):
 g=[[F(1,2)-mu,-F(347,10),F(-5)],[-F(347,10),w1*(F(9,10)-mu)-40,F(-3*w1)],
    [F(-5),F(-3*w1),w2*(2-mu)]]
 p0=g[0][0]
 s11=g[1][1]-g[0][1]**2/p0
 s12=g[1][2]-g[0][1]*g[0][2]/p0
 s22=g[2][2]-g[0][2]**2/p0
 return [p0,s11,s22-s12**2/s11]
rows=[]
for name,w1,w2,mu,mu_fail,C,invroot,r,eta,bl in [
 ('sharp',2**14,2**18,F(259,1000),F(13,50),401,88,F(147,200000),F(76219,10**9),F(1037,10000)),
 ('sharpw',2**15,2**20,F(97,250),F(389,1000),397,72,F(1351,10**6),F(4207,20*10**6),F(1557,10000))]:
 piv=pivots(mu,w1,w2);bad=pivots(mu_fail,w1,w2)
 assert all(x>0 for x in piv) and bad[-1]<0
 root1lo=F(128) if name=='sharp' else 128*s2lo
 ratiohi=F(1,4) if name=='sharp' else s2hi/8
 root2=512 if name=='sharp' else 1024
 k00=2*d+6*b+24*(tw+2*kw)+32*kw
 k01=320*kw/root1lo;k02=2048*kw/root2
 k11=8+24*(tu+ku)+32*ku;k12=80*ku*ratiohi
 k22=8+24*tu+32*ku
 kr=[k00+(k01+k02)/2,k11+(k01+k12)/2,k22+(k02+k12)/2]
 assert all(x<C for x in kr)
 s=F(1,invroot**2);rate=mu-C*s-F(8,5)*r*invroot
 assert rate>=bl and eta<=bl*r
 con=q*invroot*r/2
 assert con<1 and F(7,10)-2*con>0
 cw=max(1+F(32,25)+w1,1+F(w2,w1))
 rows.append({'name':name,'weights':[w1,w2],'mu':str(mu),'LDU_pivots':list(map(str,piv)),
  'next_mu':str(mu_fail),'next_LDU_pivots':list(map(str,bad)),
  'rational_symmetric_row_upper':list(map(str,kr)),'row_upper_float_for_reading':list(map(float,kr)),
  'C':C,'s':str(s),'r':str(r),'eta':str(eta),'rate':str(rate),'rate_lower':str(bl),
  'self_map_slack':str(bl*r-eta),'contraction_upper':str(con),'contraction_upper_float':float(con),
  'slope_margin_lower':str(F(7,10)-2*con),'Cw':str(cw),
  'G0_requirement':str(eta/root2),'G1_requirement_expression':f'{eta}/sqrt({w1})'})
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Exact rational kernel bounds and LDU elimination; floats informational only',
 'kernel_bounds':{'m':str(m),'w':str(w),'pi_interval':[str(pl),str(pu)],'rough_sum_upper':str(AA+BB),
 'rough_upper_float':float(AA+BB),'weight_commutator_upper':str(w*m)},'rows':rows,
 'target_sha256':sha256((root/'source/T2_T4L2_sharp.md').read_bytes()).hexdigest(),
 'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(root/'verification/exact_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
for row in rows: print(row['name'],row['row_upper_float_for_reading'],row['rate'],row['contraction_upper_float'])
print('rough upper',float(AA+BB),'elapsed',result['elapsed_seconds'])
