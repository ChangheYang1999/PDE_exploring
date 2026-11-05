#!/usr/bin/env python3
import json,argparse
from pathlib import Path
from flint import arb,ctx

def calculate(R='0.0000004549261',M='.387',bits=256):
 ctx.prec=bits;q=arb(21)/10;R=arb(R);M=arb(M);theta=(q-2)/q
 def B(p):
  s=(p+1)/q
  return (4*q*(arb.pi()*s).sin()).rsqrt()*(1-s)**(-(1-s)/2)*s**(-s/2)
 B0,B1=B(0),B(1);Cs=B1/4;Ca=B0/arb(2).sqrt();S=1/(2*(arb.pi()*(q-1)*(q-2)).sqrt())
 r=R/M;z=q*r**(1/q);v=Ca*M*r**(1-1/q)
 L0=q*Cs*R**theta*M**(1-theta)+arb(53)/100*S*M
 C=q*arb(2)**(q-2)*(B1*R**theta*M**(1-theta)+S*M)
 P=arb(2)**(q-1)*(Ca+B0)*M*r**(1-1/q);T=q*arb(2)**(q-2)*(Ca+B1)*M*r**(1-1/q)
 L=L0*(1+2*z)**2+4*C*(arb(1)/2+z)*z+2*(q*v+P+T)
 return {'status':'RIGOROUS_ARB_NONLINEAR_Q_LOSS','R':str(R),'M':str(M),'q':'21/10','L_Q':L.str(70),'L0_unweighted':L0.str(60),'z_ratio':z.str(60),'commutator_operator_C':C.str(60),'lower_order_P':P.str(60),'lower_order_T':T.str(60),'test_norm_condition':'Q(g)>=M and||g||2<=R; coefficient||k||2<=R,Q(k)<=M','bits':bits}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--R',default='0.0000004549261');p.add_argument('--M',default='.387');p.add_argument('--output',type=Path,required=True);a=p.parse_args();z=calculate(a.R,a.M);a.output.write_text(json.dumps(z,indent=2)+'\n');print(json.dumps(z,indent=2))
