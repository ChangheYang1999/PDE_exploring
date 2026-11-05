#!/usr/bin/env python3
"""Executed scalar certificate for LOWBAND_LOCALIZED_PRICING_v01.

All analytic comparisons are exact rational; coefficient moments use Arb.
The profile-dependent input is the inherited actual strain bound 137/125.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb, ctx

def aa(x):
    x=F(x)
    return arb(x.numerator)/arb(x.denominator)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    ctx.prec=256
    pi_low,pi_up=F(157,50),F(22,7)
    assert pi_up-pi_low>0
    assert pi_up-pi_low**3/18+pi_up**5/600<2
    # exp(7/10)>2 => log(2)<7/10.
    assert sum((F(7,10)**i/F(__import__('math').factorial(i)) for i in range(4)),F(0))>2
    assert 2*(2+F(7,10))/pi_low<2
    # exp(5/4)>16/5 => 1+8 exp(-5/4)<7/2.
    assert sum((F(5,4)**i/F(__import__('math').factorial(i)) for i in range(4)),F(0))>F(16,5)
    nu=F(1,40);delta=nu**2
    assert F(1,2)+delta/2+delta**2/4<F(3,5)
    assert F(1,2)+3*delta/4+3*delta**2/4+delta**3/4<1
    variation_up=F(7,2)+F(587,20)*delta+F(761,40)*delta**2
    assert variation_up<4
    assert F(12)+32*delta+F(6121,200)*delta**2<13
    assert F(1,4)+delta/2+delta**2/4<1
    pi=arb.pi();ell=arb(8).log()/(2*pi.sqrt());strain=aa(F(137,125))
    def moment(p):
        return arb(8)**(arb(p)/2)*(arb(p*p)*ell**2/4).exp()*(arb(p)*ell/(2*arb(2).sqrt())).erfc()/p
    I2,I4=moment(2),moment(4)
    A0=strain*(2*pi*I2).sqrt();A1=strain*(2*pi*(I2+4*I4)).sqrt()
    assert A0<5 and A1<23
    cutoff=arb(1000000);an=aa(nu)
    eta=4*A0/(pi.sqrt()*cutoff)
    price=(an**2*A1**2/(2*pi)+(arb(9)/(50*pi)+128/pi*(cutoff*an).log())*A0**2).sqrt()
    price_D=(an**4*A1**2/(2*pi)+26*an**2*A0**2/pi).sqrt()
    assert price<99
    eta_up=F(11,1000000)
    assert eta<aa(eta_up)
    assert price_D<1
    q=F(21,10);mixed=796*q;rate=8*q*eta_up
    assert mixed==F(8358,5) and rate==F(231,1250000)
    young=F(1,4000)
    weak=mixed**2/(4*young);total_rate=rate+young
    assert weak==2794246560
    assert total_rate==F(1087,2500000)
    inherited_rate_room=F(2328694018,10**12)
    inherited_price_room=F(9941475955)
    assert total_rate<inherited_rate_room and weak<inherited_price_room
    out={
      'status':'LOWBAND_LOCALIZED_TIS_CERTIFICATE_PASS',
      'arb_precision_bits':ctx.prec,
      'inherited_profile_input':{'global_S_operator_sup_upper':'137/125','status':'inherited certified bound; not replayed by this script'},
      'frequency_cut':'exp(-(|xi|/nu)^4)',
      'nu':str(nu),'spatial_displacement_cutoff':1000000,
      'kernel_variation_rational_upper':str(variation_up),
      'erflog_width_arb':str(ell),'I2_arb':str(I2),'I4_arb':str(I4),
      'A0_upper_arb':str(A0),'A1_upper_arb':str(A1),
      'kernel_price_upper_arb':str(price),'kernel_high_loss_arb':str(eta),
      'derivative_kernel_price_upper_arb':str(price_D),
      'rounded_price_R_and_pR':'99','rounded_price_nR':'100','rounded_kernel_high_loss':str(eta_up),
      'TIS_low_definition':'TIS(chi*S;G)-TIS(chi*S;(1-psi_nu)*G)',
      'TIS_low_rate_upper':str(total_rate),'TIS_low_weak_price_upper':str(weak),
      'remaining_original_plan_rate_room':str(inherited_rate_room-total_rate),
      'remaining_original_plan_price_room':str(inherited_price_room-weak),
      'other_commutator_forms':'NOT CERTIFIED by this calculation',
      'stationary_existence':'NOT CLAIMED'
    }
    encoded=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(encoded)
    print(encoded,end='')
if __name__=='__main__':main()
