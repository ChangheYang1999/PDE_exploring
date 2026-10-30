from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def A(x):
 x=Q(x);return arb(x.numerator)/x.denominator
def run(hfree):
 start=time.monotonic();s=A(Q(5,262144))
 if hfree:
  rs=['0.0002023','0.000000332','0.0000000184'];fs=['0.0000178042','0.000000139096','0.0000000347739']
 else:
  rs=['0.0002022','0.0000003347','0.00000001899','0.00000006686'];fs=['0.0000176771','0.000000138102','0.0000000345255','0.0000000353781']
 r=list(map(A,rs));f=list(map(A,fs));n=(r[0]**2+2*r[1]**2+r[2]**2).sqrt();nu=n/s.sqrt()
 aa=A(Q(127,50))+A(Q(653,5))*s;bb=A(Q(9,5))*(1+44*s)
 m0=A(2 if hfree else Q(11,4))-3882*s-A(Q(3,10))*nu
 m1=A(Q(9,10))-4290*s-A(Q(13,10))*nu;m2=A(Q(1,2))-4708*s-(aa+bb)*nu
 alpha=A(Q(347,5))+5440*s+bb*nu;beta=10+34816*s;c1=6+1360*s
 assert all(v>0 for v in [m0,m1,m2]);extra={}
 if hfree:b=f[2]/m0
 else:
  mH=A(Q(19,5))-2*s;q0=476*s+nu;den=1-q0/(mH*m0.sqrt());assert den>0
  b=(f[2]/m0+f[3]/(mH*m0.sqrt()))/den;H=f[3]/mH+(q0/mH)*b
  extra={'mH':mH.str(80),'q0':q0.str(80),'feedback_denominator':den.str(80)}
 a=(f[1]+c1*b)/m1;P=(f[0]+alpha*a+beta*b)/m2+(40/m2).sqrt()*a
 gamma=[P,a,b] if hfree else [P,a,b,H];slacks=[x-y for x,y in zip(r,gamma)];assert all(v>0 for v in slacks)
 d=n/(2*(arb.pi()*s*(1+s)).sqrt());q=d/2 if hfree else d/(A(Q(19,5))-d);assert q<1
 return {'hfree':hfree,'r_exact':rs,'forcing_exact':fs,'s_exact':'5/262144','m0':m0.str(80),'m1':m1.str(80),'m2':m2.str(80),'Gamma':[v.str(80) for v in gamma],'positive_selfmap_slacks':[v.str(80) for v in slacks],'ng':n.str(80),'d':d.str(80),'low_contraction':q.str(80),'elapsed_seconds':time.monotonic()-start,**extra}
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'source_sha256':hashlib.sha256((ROOT/'source/theory_v01.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'boxes':[run(False),run(True)]}
(ROOT/'verification/boxes.json').write_text(json.dumps(out,indent=2)+'\n')
for b in out['boxes']:print('Hfree',b['hfree'],'Gamma',b['Gamma'],'q',b['low_contraction'])
