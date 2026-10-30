from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb, ctx
ctx.prec = 256
mu=F(297,1000)
G=[[F(1,2)-mu, -F(347,10), -F(5)],
   [-F(347,10), 2**14*(F(9,10)-mu)-40, -F(3*2**14)],
   [-F(5), -F(3*2**14), F(2**14*44)-2**18*mu]]
a,b,c=G[0]; _,d,e=G[1]; _,_,f=G[2]
minors=[a,a*d-b*b,a*(d*f-e*e)-b*(b*f-e*c)+c*(b*e-d*c)]
assert all(x>0 for x in minors)
s=F(1,2**16); r=F(3,2**15); eta=r/10
rate=mu-4800*s-5*r*256
assert rate == F(13641,128000)
assert rate>F(1,10)
S=arb(s.numerator)/s.denominator
R=arb(r.numerator)/r.denominator
dgrad=R/(2*(arb.pi()*S*(1+S)).sqrt())
q=dgrad/(arb(19)/5-dgrad)
assert dgrad<arb('0.00662')
assert q<arb('0.0018')
assert dgrad<arb(7)/10
result={'mu':str(mu),'G':[[str(x) for x in row] for row in G],
 'leading_principal_minors':[str(x) for x in minors],
 's':str(s),'r':str(r),'eta':str(eta),'rate':str(rate),
 'gradient_upper_enclosure':str(dgrad),'contraction_enclosure':str(q),
 'a0_lower_input':'7/10','gain_over_old_eta':str(eta/F(1,1572864)),
 'scope':'Exact matrix arithmetic plus Arb256; analytic hypotheses are not numerical certificates.'}
Path(__file__).resolve().parents[1].joinpath('verification/rationals.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
