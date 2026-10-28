"""Exact arithmetic audit of retained-coefficient fractional bounds."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
ctx.prec=512
BASE=Path(__file__).resolve().parents[2]
def A(x):
 x=Q(x);return arb(x.numerator)/x.denominator
K=1+Q(547,2048)
assert K==Q(2595,2048) and 2*K<4
assert A(6*K)*(2/arb.pi()).sqrt()<8
P0=Q(1,512);P1=Q(1,1024);P2=Q(3)
G=507*P0+40*P1+P2
assert G==Q(2063,512) and Q(15,4)*G<16
assert arb(8)+arb(2).sqrt()<16
Smax=Q(1,4096)
assert 16*(1+400*Smax)+1600*Smax<32
assert 4*(1+2200*Smax)<8
assert 32+4<40
low=Q(27,5)*8+Q(16,5)*40
upper=Q(14,5)*4+2*32+Q(9,5)*32
first=Q(11,5)*4+32
native=48
rough=low+upper+first+native
assert low==Q(856,5) and upper==Q(664,5) and first==Q(204,5)
assert rough==Q(1964,5) and rough<400
assert 69*2==138 and 138*2==276
bilinear=(276+4)*Q(13,2)
assert bilinear==1820 and bilinear<2048
# Retain the previously proved smooth constant without any improved assumptions.
smooth_top=Q(441164,15);smooth_first=Q(2111948,3);smooth_low=Q(18581708,5)
smooth=smooth_top+smooth_first+smooth_low+1644+24
assert smooth<2**23
s=3*Q(1,2**31);radius=5*Q(1,2**32);eta=Q(1,2**35)
root=A(s).sqrt();tau=A(radius)/root
beta=A(Q(1,20)-2**23*s)-400*tau
rational_rate=Q(1,20)-Q(3,256)-Q(625,49152)
assert rational_rate==Q(6283,245760) and rational_rate>Q(1,40)
assert beta>A(rational_rate) and 40*eta==radius
lipschitz=4*tau
low_rate=A(Q(1,5))-12*lipschitz
contraction=6*2048*tau
assert low_rate>A(Q(1,6)) and contraction<A(Q(25,64))<A(Q(2,5))
assert lipschitz<A(Q(1,4096))
assert Q(1,5)+Q(4,5)*s/2<Q(1,4)
# Four outputs: L, adapted Holder, moment, strain.
assert 1+128+16+32<256
assert 1+Q(64,3)+Q(1,256)<32
four=40*256/(root*A(s))
assert four<arb(2)**58
assert 40*(A(Q(2,3))**A(Q(3,2)))<32
files=['18_fractional_constants/PROOF.md','16_weighted_fractional/PROOF.md','16_weighted_fractional/ROUGH_INVERSE_PROOF.md','16_weighted_fractional/SHARP_ROUGH_INVERSE_PROOF.md','16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md','16_weighted_fractional/REFERENCE_AUDIT.md','07_weighted/SHARP_WEIGHTED_H2_PROOF.md','17_weight_radius/PROOF.md','17_weight_radius/RESIDUAL_PROOF.md','17_weight_radius/verification/annular_residual.json','16_weighted_fractional/ANNULAR_RESIDUAL_PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED V090','precision_bits':ctx.prec,'localization':str(K),'gradient_bound':4,'gradient_holder_bound':8,'growth_localization':str(G),'growth_bound':16,'product_Hs_bound':16,'weighted_product_bound':32,'rough_low_commutator':str(low),'rough_top':str(upper),'rough_first':str(first),'rough_native_low':native,'rough_total':str(rough),'rough_rounded':400,'bilinear':str(bilinear),'bilinear_rounded':2048,'smooth_total':str(smooth),'smooth_rounded':2**23,'s':str(s),'radius':str(radius),'residual_threshold':str(eta),'high_decay_lower':beta.str(70),'rational_decay_lower':str(rational_rate),'high_inverse_upper':40,'low_decay_lower':low_rate.str(70),'low_inverse_upper':6,'lipschitz_bound':lipschitz.str(70),'contraction_upper':contraction.str(70),'four_output_bound':four.str(70),'four_output_rounded':str(2**58),'gap_power_R32':117,'gap_power_R35':124,'dependencies':{f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
