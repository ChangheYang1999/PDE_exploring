#!/usr/bin/env python3
"""Outward scalar verification of SOURCE_Q_NORM_BOUND.md."""
import argparse
from datetime import datetime,timezone
from fractions import Fraction as F
import json
from pathlib import Path
from flint import arb,ctx

def aa(x):
    z=F(x)
    return arb(z.numerator)/z.denominator

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    inputs={'f':'0.0000007961207','n':'0.00555458','c_W':'9619/5000',
            'T0':'0.0000018314','T1':'0.000004383','T2':'0.00001049','T3':'0.133465'}
    q=aa('21/10');f=aa(inputs['f']);n=aa(inputs['n']);K=aa(inputs['c_W'])*n
    d1=f**(1-1/q)*K**(1/q);d2=f**(1-2/q)*K**(2/q)
    T=[aa(inputs[f'T{j}']) for j in range(4)]
    H2=(T[0]+2*T[1]+T[2]).sqrt();H3=(T[0]+3*T[1]+3*T[2]+T[3]).sqrt()
    A2=H2+4*d1+12*f;A3=H3+7*d2+130*d1+1391*f
    upper=A2**aa('9/10')*A3**aa('1/10')
    assert upper<aa('1/125')
    result={'status':'SOURCE_Q_NORM_SCALAR_CERTIFICATE_PASS','inherited_input_uppers':inputs,
            'q':'21/10','homogeneous_K_upper_arb':str(K),'d1_upper_arb':str(d1),'d2_upper_arb':str(d2),
            'A2_upper_arb':str(A2),'A3_upper_arb':str(A3),'Q_source_upper_arb':str(upper),
            'Q_source_rational_upper':'1/125','bits':ctx.prec,'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Analytic integer-product and interpolation bound; inherits the specified combined2 tensor and multiplier certificates. No existence assertion.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
