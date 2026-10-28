from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json
ctx.prec=384
A=lambda q:arb(Q(q).numerator)/Q(q).denominator
s=Q(1,32);a=s/2;pi=arb.pi()
cgrad=1/(2*(pi*A(s*(1+s))).sqrt())
cholder=2**(-A(a))/pi.sqrt()*(A(2+a).gamma()*A(s-a).gamma()/A(2+s).gamma()).sqrt()
cmoment=cholder/A(1+a)*pi**A(Q(1,256))
checks={'E0_exact':Q(20,21)*(Q(19,5)-Q(11,4))==1,'E1_absorb':16*(Q(11,4)-Q(1,2))>=30,'cross_round':Q(347,5)+Q(10,4)<72,'E2_absorb':2**14*(Q(1,2)-Q(1,10))>=5224,'interpolation_rate':(1-s)*Q(1,10)-s*Q(3,2)==Q(1,20),'gradient_less_2':cgrad<2,'holder_less_5':cholder<5,'moment_less_5':cmoment<5,'moment_gap':256*(1+a)+2-260==2,'combined':(1+3+5+2)*20<240}
assert all(checks.values()),checks
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':384,'checks':checks,'gradient_constant':cgrad.str(60),'holder_constant':cholder.str(60),'moment_constant':cmoment.str(60),'theta':str(s),'alpha':str(a),'inverse_bound':20}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
