"""Independent exact rational certificate for T2-R2; no special functions."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
start=time.monotonic();ROOT=Path(__file__).resolve().parents[1]
def atan_bounds(q,n):
    total=sum(((-1)**k*q**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
    other=total+(-1)**n*q**(2*n+1)/Q(2*n+1)
    return min(total,other),max(total,other)
a,b=atan_bounds(Q(1,5),15);c,d=atan_bounds(Q(1,239),5)
pi_lo,pi_hi=16*a-4*d,16*b-4*c
assert Q(333,106)<pi_lo<pi_hi<Q(355,113)
log2_lo=2*sum((Q(1,3)**(2*k+1)/Q(2*k+1) for k in range(4)),Q(0))
h32=sum((Q(1,k) for k in range(1,33)),Q(0))
assert h32-5*log2_lo<Q(3,5)
s0=Q(1,1024);a0=(1-s0)/2
v=(Q(3,5)+1/a0)*s0/2
m_derived=pi_hi/(2*(1-v));m=Q(1573,1000)
assert 0<v<1 and m_derived<m
w=Q(1221,1000)
assert w**10>Q(64,5)**5/Q(6)**6
q0=Q(2821,10000)
assert q0**2>1/(4*pi_lo)
p=q=Q(283,1000)
assert q0*(1+s0)*(1+s0/2)<p
ku=m;kw=m+Q(8,5);tu=3*m/2;tw=tu+Q(32,15)
bessel=1+3*pi_hi*w/4;dilation=1+pi_hi*w/2
K=[[Q(0) for _ in range(4)] for _ in range(4)]
K[0][0]=2*dilation+6*bessel+24*(tw+2*kw)+32*kw
K[0][1]=kw*Q(320,128);K[0][2]=kw*4
K[1][1]=8+24*(tu+ku)+32*ku;K[1][2]=20*ku
K[2][2]=8+24*tu+32*ku
# sqrt(20/21)<1 gives a harmless rational overestimate of the H row.
K[3][2]=28*ku;K[3][3]=2
rows=[sum((K[i][j]+K[j][i] for j in range(4)),Q(0))/2 for i in range(4)]
assert max(rows)<402
L=w*m*s0;Pw=p*(1+L)+q*L;Tw=1+4*L
A=Q(4,5)*q+q*Tw+2*Pw;B=Q(9,5)*Pw;low=q+p
assert A>low and A+B<Q(8,5)
s=Q(1,8192);radius=Q(43,50000);eta=Q(5289,50000000)
sqrt2_hi=Q(141421357,100000000);assert sqrt2_hi**2>2
beta=Q(297,1000)-402*s-Q(8,5)*radius*64*sqrt2_hi
assert beta>Q(123,1000) and eta==Q(123,1000)*radius
sqrtpi_lo=Q(17724538,10000000);assert sqrtpi_lo**2<pi_lo
dgrad=32*sqrt2_hi/sqrtpi_lo*radius
contraction=dgrad/(Q(19,5)-dgrad)
assert dgrad<Q(2196,100000) and contraction<Q(59,10000) and dgrad<Q(7,10)
def record(q):return {'exact':str(q),'display_float':float(q)}
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
'method':'Exact rational bounds; Machin pi; harmonic and log-series bound gamma<3/5; integrated digamma bound; no numerical gamma or square-root calls.',
'pi_interval':[str(pi_lo),str(pi_hi)],'gamma_upper':'3/5','m_derived_upper':record(m_derived),
'constants':{k:str(x) for k,x in [('m',m),('w',w),('q',q),('p',p)]},
'K_upper':[[str(x) for x in row] for row in K],
'symmetric_rows_upper':[record(x) for x in rows],
'rough_A_upper':record(A),'rough_B_upper':record(B),'rough_total_upper':record(A+B),
'beta_lower':record(beta),'gradient_upper':record(dgrad),'low_contraction_upper':record(contraction),
'eta':str(eta),'radius':str(radius),'s':str(s),
'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/rational_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('rows:',[float(x) for x in rows]);print('rough:',float(A+B),'beta:',float(beta),'contraction:',float(contraction))
