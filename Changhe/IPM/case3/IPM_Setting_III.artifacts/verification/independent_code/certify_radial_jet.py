"""Arb enclosure of the mean first radial jet, using exact JSON inputs.

The mathematical interpolant uses exact Chebyshev-Radau nodes. Numeric nodal
values are interpreted as their exact binary64 dyadic rationals. This is a
certificate for a finite interpolant, not for the existence of a PDE solution.
"""
import json,sys,argparse
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=256
ap=argparse.ArgumentParser();ap.add_argument('checkpoints',nargs='+');ap.add_argument('--tag',default='');args=ap.parse_args()
out=[]
for filename in args.checkpoints:
    path=Path(filename)
    data=np.load(path,allow_pickle=False)
    b=np.asarray(data['b'],float)
    N=int(data['N']); M=int(data['M'])
    means=[sum((Fraction(float(v)) for v in row),Fraction(0))/M for row in b]
    inputs={'source_npz':str(path),'N':N,'M':M,'map_power_hex':float(data['p']).hex(),'length_hex':float(data['L']).hex(),'mean_radial_values':[[str(x.numerator),str(x.denominator)] for x in means]}
    input_file=Path('research/regularity/verification')/(path.stem+'_input.json')
    input_file.write_text(json.dumps(inputs,indent=2)+'\n')
    # All values used by the certificate are read from its serialized JSON input.
    cert=json.loads(input_file.read_text())
    vals=[arb(fmpq(int(a),int(b))) for a,b in cert['mean_radial_values']]
    nodes=[-(2*arb.pi()*j/(2*N+1)).cos() for j in range(N+1)]
    bary=[]
    for j in range(N+1):
        prod=arb(1)
        for k in range(N+1):
            if k!=j: prod*=nodes[j]-nodes[k]
        bary.append(1/prod)
    derivative=sum((bary[j]/bary[0]/(nodes[0]-nodes[j])*(vals[j]-vals[0]) for j in range(1,N+1)),arb(0))
    fp=Fraction(float.fromhex(cert['map_power_hex']))
    fl=Fraction(float.fromhex(cert['length_hex']))
    power=arb(fmpq(fp.numerator,fp.denominator))
    length=arb(fmpq(fl.numerator,fl.denominator))
    physical=derivative*(power*arb(2).log()).exp()/length
    row={'utc':datetime.now(timezone.utc).isoformat(),'input':str(input_file),'precision_bits':ctx.prec,'mean_dt_b_at_minus1':str(derivative),'mean_dr_b_at_zero':str(physical),'dt_interval_excludes_zero':not derivative.contains(0),'dr_interval_excludes_zero':not physical.contains(0),'verdict':'REFUTED C2 for the mathematical interpolant' if not physical.contains(0) else 'OPEN'}
    out.append(row); print(json.dumps(row),flush=True)
Path('research/regularity/verification/arb_first_jets'+args.tag+'.json').write_text(json.dumps(out,indent=2)+'\n')
