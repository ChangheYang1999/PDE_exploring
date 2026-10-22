"""Exact physical-axis knot jumps; no numerics-lane imports.

Derivation: research/169_exact_spline_knot_regularity/PROOF.md.
This generator differentiates coefficient arrays. The separate checker
uses exact polynomial value samples instead.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json, shutil, time
import numpy as np


def enc(q):
    return {'numerator':str(q.numerator),'denominator':str(q.denominator)}


def dcoeff(knots, coeff, degree):
    knots=list(knots); coeff=list(coeff)
    for d in range(degree,0,-1):
        den=[knots[j+d+1]-knots[j+1] for j in range(len(coeff)-1)]
        assert all(v>0 for v in den)
        coeff=[d*(coeff[j+1]-coeff[j])/den[j] for j in range(len(den))]
        knots=knots[1:-1]
    return knots,coeff


def axis_coeff(z, name, K, nb):
    arr=z[name].reshape(K,nb)
    return [sum(((-1)**(n//2)*Q.from_float(float(arr[n,j])) for n in range(0,K,2) if j>=n//2),Q(0)) for j in range(nb)]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('archives',nargs='+');args=ap.parse_args()
    root=Path(args.output);root.mkdir(parents=True,exist_ok=True);(root/'archives').mkdir(exist_ok=True)
    start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();rows=[]
    for arg in args.archives:
        src=Path(arg);target=root/'archives'/src.name;sha=hashlib.sha256(src.read_bytes()).hexdigest()
        if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==sha
        else:shutil.copyfile(src,target)
        with np.load(target,allow_pickle=False) as z:
            p=int(z['deg']);N=int(z['Nt']);K=int(z['K']);grade=float(z['grade']);b=float(z['beta_basis']);L=float(z['L'])
            assert str(z['rmap'])=='r2' and p>=1 and N>=1 and K>=1 and grade>0 and b>0 and L>0
            edges=np.linspace(0.,1.,N+1)**grade;kraw=np.r_[np.zeros(p),edges,np.ones(p)];knots=[Q.from_float(float(v)) for v in kraw];nb=len(knots)-p-1
            fields={}
            for name in ['cF','cG']:
                coeff=axis_coeff(z,name,K,nb);dk,dc=dcoeff(knots,coeff,p);assert len(dc)==N and dk==[Q.from_float(float(v)) for v in edges]
                jumps=[dc[j]-dc[j-1] for j in range(1,N)]
                fields[name]={'axis_coefficients':[enc(v) for v in coeff],'interval_pth_derivatives':[enc(v) for v in dc],'jumps':[enc(v) for v in jumps], 'nonzero_count':sum(v!=0 for v in jumps)}
            out={'schema':'verification-exact-spline-axis-jumps-v1','created_utc':utc,'archive':str(target),'original':str(src),'sha256':sha,'degree':p,'Nt':N,'K':K,'grade_hex':grade.hex(),'basis_beta_hex':b.hex(),'L_hex':L.hex(),'knots_hex':[float(v).hex() for v in kraw],'fields':fields,'claim':'A nonzero jump witnesses failure of C^degree of the literal represented physical field at a positive x-axis knot point. No nearby-field exclusion.'}
            dest=root/(src.stem+'.knots.json');dest.write_text(json.dumps(out,indent=2)+'\n')
            rows.append({'certificate':str(dest),'archive_sha256':sha,'degree':p,'F_nonzero_knots':fields['cF']['nonzero_count'],'G_nonzero_knots':fields['cG']['nonzero_count']})
    d={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'certificates':rows}
    (root/'generation.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))

if __name__=='__main__':main()
