"""Exact/ball arithmetic for the weighted rough-inverse proof, not a PDE proof by itself."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import json, hashlib
from flint import arb,ctx
ctx.prec=512
root=Path(__file__).resolve().parents[1]
A=lambda x:arb(Q(x).numerator)/Q(x).denominator
s=Q(1,2**104);radius=Q(1,2**78);eta=radius/24
assert A(s).sqrt()==A(Q(1,2**52))
assert A(Q(4,5))+2/arb(1).exp()<A(Q(5,3))
assert 13+4*2+4*30<256
assert 2*(13+30)<128
assert 7*arb.pi().sqrt()*arb(1).exp()<64
assert 4*arb.pi()<16
assert Q(16,5)*64<256
assert Q(16,5)*16<64
assert A(Q(1,2**53)).sqrt()+A(2**50*s)<1
bg_top_T=28*12+132*24+2*17*24*3+256*512*2
bg_top_Q=Q(17*12*9*3,5)+2*256*512*Q(3,2)*2+256*16384*Q(8,3)*4
assert bg_top_T+bg_top_Q<2**26
bg_first=28*12+132*24+17*24*2+17*12*Q(3,2)*2+256*256*Q(8,3)*4
assert bg_first<2**20
bg_low=A(Q(16,5)*2**42*128*(12*4+32*Q(8,3)*4))*A(2**53).sqrt()
assert bg_low<2**87
bg_dilation=12+12*2**11+A(2**53).sqrt()*2*2**48
assert bg_dilation<2**77
assert 2**26+2**31+2**87+2**77<2**92
assert 1+426*Q(1,2**96)<2
assert 2**14*(1+102*Q(1,2**96))+102*Q(1,2**96)*2**11<2**15
rough_low=A(Q(16,5)*2**42*128*4)*A(2**53).sqrt()
assert rough_low<2**80
assert 2**91*Q(1,2**96)<=Q(1,32)
rough_top=Q(14,5)*2**11+2*2**15+Q(9,5)*2**15
rough_first=Q(11,5)*2**11+2**15
rough_low_energy=12*2**11+Q(1,32)
assert rough_top+rough_first+rough_low_energy<2**19
rate=Q(1,20)-2**92*s-2**19*radius/Q(1,2**52)
assert rate==Q(859,20480) and rate>Q(1,24)
d=2**11*radius/Q(1,2**52)
assert d==Q(1,2**15)
assert Q(1,5)-12*d>Q(1,6)
contraction=6*2**15*radius/Q(1,2**52)
assert contraction==Q(3,1024) and contraction<Q(1,100)
assert 2*69*2<2**9
assert Q(13,2)*(2**11+2**10)<2**15
assert 2*(10240+20480)<2**16
assert 1+2**16+2**13+2**15<2**18
assert 24*2**18<2**23
assert Q(1,5)+Q(4,5)*s/2<Q(1,4)
assert (8/s)*(s/2)+2-4==2
assert 2**13*4*Q(1,2**18)==Q(1,8)
assert 1000<4**5
paths=[root/'PROOF.md',root/'ROUGH_INVERSE_PROOF.md',
 root.parent/'07_weighted/SHARP_WEIGHTED_H2_PROOF.md',
 root.parent/'07_weighted/R2_DERIVATIVE_PROOF.md',
 root.parent/'07_weighted/verification/sharp_weighted_h2_constants.json',
 root.parent/'07_weighted/verification/r2_extra_audit.json',
 root.parent/'14_homogeneous_weight/REGULARIZED_PROOF.md',
 root.parent/'07_weighted/MELLIN_RIESZ_PROOF.md']
data={'status':'ARITHMETIC_PASS','utc':datetime.now(timezone.utc).isoformat(),
 'proof_audit':'CONFIRMED V078','s':str(s),'radius':str(radius),'eta':str(eta),'background_constant':2**92,'rough_constant':2**19,
 'high_rate':str(rate),'high_inverse':24,'low_rate':str(Q(1,5)-12*d),'low_inverse':6,
 'contraction':str(contraction),'background_component_checks':{'top':str(bg_top_T+bg_top_Q),'first':str(bg_first),'low':str(bg_low)},
 'rough_component_sum':str(rough_top+rough_first+rough_low_energy),
 'low_bilinear_coefficient':2**15,'combined_inverse_coefficient':'2^23 s^(-3/2)',
 'dependencies':{str(p.relative_to(root.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'verification/rough_constants.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
