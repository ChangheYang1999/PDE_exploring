"""Exact arithmetic for the direct low commutators and sharper weighted theorem."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=512
A=lambda x:arb(Q(x).numerator)/Q(x).denominator
root=Path(__file__).resolve().parents[1]
assert arb(1).exp()>arb(8)/3
assert A(Q(4,9))+5/arb(1).exp()<A(Q(7,3))
assert 173+44*arb.pi()<312
assert 89+20*arb.pi()<152
assert 4*9+6*2+4*36+20==212
assert 4*13+6*2+4*30+16==200
assert 13+4*2+6*30+4*16+420==685
assert 3*13+4*4*2+6*5*30+4*6*16+7*420==4295
assert 4*3*13+6*4*2+4*5*30+6*16==900
assert 2*(Q(4295,2)+685)==5665
smax=Q(1,2**12)
assert (1+212*smax)<2
assert 1+2200*smax<2
assert 2**14*(1+400*smax)+400*smax*2**11<2**15
assert Q(27,5)*(1+212*smax)<6
assert Q(27,5)*152<821
assert A(6)*A(Q(1,2**53)).sqrt()<1
bt=312*12+5665*24;bc=1370*24
lowT=Q(27,5)*bt+Q(16,5)*bc
lowQ=Q(13,2)*1370*(Q(27,5)*12+256)
assert lowT==Q(4298088,5)
assert lowQ==2856724
assert lowT+lowQ==Q(18581708,5)
top=28*12+132*24+2*17*24*3+17*12*Q(9,5)*3
mid=256*512*2+2*256*512*Q(3,2)*2
bot=256*16384*Q(8,3)*4
top=top+(mid+bot)/2048
first=28*12+132*24+17*24*2+17*12*Q(3,2)*2+256*256*Q(8,3)*4
assert top==Q(441164,15)
assert first==Q(2111948,3)
bg=top+first+lowT+lowQ+1644+24
assert bg<2**23
roughlow=Q(27,5)*4096+Q(16,5)*36864
assert roughlow==Q(700416,5)
rtop=Q(14,5)*2**11+2*2**15+Q(9,5)*2**15
rfirst=Q(11,5)*2**11+2**15
rough=rtop+rfirst+12*2**11+roughlow
assert rough==Q(1660928,5) and rough<2**19
s=Q(1,2**30);radius=Q(1,2**41);eta=Q(1,2**46);sqrt_s=Q(1,2**15)
assert 32*eta==radius
rate=Q(1,20)-2**23*s-2**19*radius/sqrt_s
assert rate==Q(11,320) and rate>Q(1,32)
d=2**11*radius/sqrt_s
assert d==Q(1,2**15)
lowrate=Q(1,5)-12*d
assert lowrate==Q(8177,40960) and lowrate>Q(1,6)
contraction=6*2**15*radius/sqrt_s
assert contraction==Q(3,1024) and contraction<Q(1,100)
assert Q(1,5)+Q(4,5)*smax/2<Q(1,4)
assert Q(1,2**18)/eta==2**28
assert 2**23*sqrt_s**-3==2**68
paths=[root/'SHARP_LOW_COMMUTATOR_PROOF.md',root/'SHARP_ROUGH_INVERSE_PROOF.md',root/'ROUGH_INVERSE_PROOF.md',root/'PROOF.md',root/'verification/state131_weighted_gap.json',root.parent/'07_weighted/SHARP_WEIGHTED_H2_PROOF.md',root.parent/'14_homogeneous_weight/REGULARIZED_PROOF.md']
data={'utc':datetime.now(timezone.utc).isoformat(),'status':'ARITHMETIC_PASS','proof_audit':'CONFIRMED V080-V081','s':str(s),'radius':str(radius),'eta':str(eta),'background_component_sum':str(bg),'background_constant':2**23,'rough_component_sum':str(rough),'rough_constant':2**19,'high_rate':str(rate),'high_inverse':32,'low_inverse':6,'contraction':str(contraction),'combined_inverse_constant':2**68,'strict_original_gap_lower_bound':2**28,'dependencies':{str(p.relative_to(root.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'verification/sharp_weighted_constants.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
