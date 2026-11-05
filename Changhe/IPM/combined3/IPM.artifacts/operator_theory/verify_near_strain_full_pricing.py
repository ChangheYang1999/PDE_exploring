#!/usr/bin/env python3
"""Closed-Gamma interval certificate for the complete near strain forms."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb, ctx

def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path)
    ap.add_argument('--strain-scale',default='1');args=ap.parse_args()
    ctx.prec=256
    qrat=F(21,10);srat=F(137,125);nur=F(1,40);eta=F(11,1000000)
    q,s,nu=aa(qrat),aa(srat),aa(nur);pi=arb.pi()
    ell=arb(8).log()/(2*pi.sqrt())
    def Imom(p):return arb(8)**(arb(p)/2)*(arb(p*p)*ell**2/4).exp()*(arb(p)*ell/(2*arb(2).sqrt())).erfc()/p
    scale=aa(F(args.strain_scale));assert scale>=1
    A0=s*(2*pi*scale**2*Imom(2)).sqrt();A1=s*(2*pi*(scale**2*Imom(2)+4*scale**4*Imom(4))).sqrt()
    # Recheck all low-price inequalities used by the new estimates.
    # Scale the displacement cutoff too, retaining the same eta threshold.
    cutoff=arb(1000000)*scale
    low_price=(nu**2*A1**2/(2*pi)+(arb(9)/(50*pi)+128/pi*(cutoff*nu).log())*A0**2).sqrt()
    low_eta=4*A0/(pi.sqrt()*cutoff)
    derivative_price=(nu**4*A1**2/(2*pi)+26*nu**2*A0**2/pi).sqrt()
    assert low_eta<aa(eta)
    def integer_upper(value):
        # FLOAT chooses a rational display; Arb certifies it before any use.
        candidate=int(float(value.mid()))+1
        assert value<candidate
        return candidate
    lowR=integer_upper(low_price);lowN=lowR+integer_upper(derivative_price)
    if F(args.strain_scale)==1:assert lowR==99 and lowN==100
    def E(m,l):return l**(m+1)/4*arb(2)**(-(m+1)/4)*((m+1)/4).gamma()
    def FF(g,m,l):
        if g<=0:return E(m,l)
        C=arb(1) if g<=1 else arb(2)**(g-1)
        return C*(E(m,l)+E(m+2*g,l))
    def price(beta,d,mu):
        i0=FF(beta,arb(1),mu)
        ider=2*d*d*FF(beta-1,arb(1),mu)+64*(FF(beta,arb(7),mu)/mu**8+FF(beta,arb(7),nu)/nu**8)
        iang=(1+nu**2)**beta/8+arb(2)**beta*((1/nu).log()+E(2*beta-1,mu))
        return (A1*A1/(2*pi)*i0+2*A0*A0/pi*(ider+iang)).sqrt()
    cases={10:(202,512,4827),12:(223,696,8276),16:(264,1173,19696),20:(306,1803,38909)}
    rows=[]
    for m,(an,apc,ar) in cases.items():
        mu=arb(m)
        pn=lowN+price(q-2,q,mu);pp=lowR+price(q-1,q-1,mu);pr=lowR+price(q,q,mu)
        if F(args.strain_scale)!=1:an,apc,ar=map(integer_upper,[pn,pp,pr])
        assert pn<an and pp<apc and pr<ar
        eh=qrat*srat*(F(2,m*m)+F(1,4*m**4))
        ey=F(1,200);D=F(1);Ds=F(1,10)
        ct=qrat*qrat*F(an+apc+ar)**2/D+qrat*qrat*F(an)**2/ey
        et=eh+8*qrat*eta+ey
        es=qrat*srat/F(m*m)+2*qrat*eta
        cs=qrat*qrat*F(apc)**2/Ds
        row={'mu':m,'A_n_arb':str(pn),'A_p_arb':str(pp),'A_R_arb':str(pr),
             'rounded_A_n':an,'rounded_A_p':apc,'rounded_A_R':ar,
             'TIS_near_rate':str(et),'TIS_near_weak_price':str(ct),'TIS_p_damping_used':str(D),
             'sandwich_near_rate':str(es),'sandwich_near_weak_price':str(cs),'sandwich_p_damping_used':str(Ds),
             'combined_near_strain_rate':str(et+es),'combined_near_strain_weak_price':str(ct+cs),
             'combined_p_damping_used':str(D+Ds)}
        rows.append(row)
    C=F(4076476460239181,2251799813685248)
    Afar=F(13396752347393121,9007199254740992)
    free_at_half=qrat*C-Afar-F(11,10)-qrat*F(1,2)
    assert free_at_half>0
    out={'status':'NEAR_STRAIN_FULL_PRICING_CERTIFICATE_PASS','arb_precision_bits':ctx.prec,
         'inherited_profile_input':'||Sym Du_star||_infinity,op <= 137/125; inherited, not replayed',
         'frequency_cuts':'psi_lambda=exp(-(|xi|/lambda)^4)','nu':str(nur),
         'strain_scale':args.strain_scale,
         'A0_arb':str(A0),'A1_arb':str(A1),'low_kernel_eta_upper':str(eta),
         'low_kernel_price_R_upper':lowR,'low_kernel_price_nR_upper':lowN,
         'cases':rows,'hypothetical_far_strain_upper':'1/2',
         'p_damping_remaining_if_actual_far_bound_half_is_certified':str(free_at_half),
         'far_strain_half_status':'NOT certified by this script',
         'unestimated_forms':['far TIS','transport remainder','velocity-source remainders'],
         'stationary_existence':'NOT CLAIMED'}
    encoded=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(encoded)
    print(encoded,end='')
if __name__=='__main__':main()
