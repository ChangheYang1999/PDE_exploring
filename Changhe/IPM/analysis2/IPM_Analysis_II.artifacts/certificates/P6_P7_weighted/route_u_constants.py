from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json,sys
from flint import arb,ctx
ctx.prec=384
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy/verification'))
from compact_matrix import A
D=8256;Z=16512
C2=2*D*256+2*4096+4*8192+2*1048576
assert C2<2**23 and 4*Z<2**17
assert 2**46+2**17<2**47
assert Q(2**53,40)>2**47
C3=D*256+3*35+2*2**14+3*77*256+6*2**14+2*2**84
assert C3<2**86 and Z<2**15
assert 2**172+2**15<2**173
assert Q(2**173,40)-2**173>=-Q(3,2)*2**173
th=Q(1,122);al=th/2
assert (1-th)/40-Q(3,2)*th==Q(1,80)
cgrad=1/(2*(arb.pi()*A(th)*(1+A(th))).sqrt())
hold=2**(-A(al))/arb.pi().sqrt()*((2+A(al)).gamma()*(A(th)-A(al)).gamma()/(2+A(th)).gamma()).sqrt()
assert cgrad<4 and hold<9
p=512;kap=516;gap=p*(1+al)+2-kap
assert gap==Q(6,61)
cmom=(2*arb.pi()/A(gap))**(arb(1)/p)*hold/(1+A(al))
assert cmom<10
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'E2_E1_coefficient':str(2**53),'E3_E2_coefficient':str(2**173),'E2_decay':'1/40','E3_growth':'3/2','theta':str(th),'alpha':str(al),'interpolated_decay':'1/80','inverse':80,'gradient_embedding':cgrad.str(60),'gradient_holder_embedding':hold.str(60),'rounded_gradient':4,'rounded_gradient_holder':9,'moment_p':p,'moment_kappa':kap,'moment_radial_gap':str(gap),'moment_embedding':cmom.str(60),'rounded_moment':10,'scope':'Requires completed M3_aux>=-5/4 certificate, in addition to V036.'}
(HERE/'route_u_constants.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
