#!/usr/bin/env python3
"""Scalar interval verification of the proved auxiliary-to-inherited norm bound."""
import argparse,json,hashlib
from pathlib import Path
from flint import arb,ctx
ctx.prec=384
ap=argparse.ArgumentParser();ap.add_argument('--R',default='4e-7')
ap.add_argument('--M',default='1/5');ap.add_argument('--a',default='5/4')
ap.add_argument('--out',type=Path,default=Path(__file__).with_suffix('.json'));args=ap.parse_args()
R,M,a=arb(args.R),arb(args.M),arb(args.a);assert R>0 and M>0 and a>0 and a<=2
delta=arb(1)/10
L=(arb.pi().sqrt()*(arb(9)/20).gamma()/(20*(arb(19)/20).gamma()))
lipDelta=16/(3*arb(3).sqrt())+384/(25*arb(5).sqrt());assert lipDelta<10
r=R/M
terms=[2/a,2*L*r**(arb(1)/21),4*r**(arb(10)/21),
       8*L*r**(arb(11)/21),8*r**(arb(20)/21),10*L*r]
upper=M*sum(terms,arb(0));assert upper<arb('.387')
out={'status':'CERTIFIED_NORM_CONVERSION_AT_STIPULATED_RADII',
     'R':args.R,'auxiliary_M':args.M,'auxiliary_weight_slope':args.a,
     'fractional_Lipschitz_commutator_constant':L.str(80),
     'Delta_weight_Lipschitz_upper':lipDelta.str(70),
     'dimensionless_terms':[v.str(70) for v in terms],
     'inherited_N2_upper':upper.str(80),'verified_inherited_target':'387/1000',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Every function in the specified auxiliary Qa/L2 ball has this inherited N2 bound. No existence or auxiliary-ball invariance is asserted.'}
args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
