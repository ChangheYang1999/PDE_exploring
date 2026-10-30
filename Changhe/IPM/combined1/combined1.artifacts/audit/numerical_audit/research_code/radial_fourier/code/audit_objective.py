from pathlib import Path
from datetime import datetime,timezone
import json,time
from flint import ctx,arb,fmpq,fmpq_poly
from radial import Radial,ar,ZERO
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--bits',type=int,default=768)
    args=parser.parse_args();ctx.prec=args.bits;start=time.monotonic()
    model=Radial(ROOT/'research/baseline/data/state131_independent.json')
    cosine=model.residual_quotient()
    print('residual quotient',len(cosine),'components','max harmonic',max(n for h,n in cosine),flush=True)
    constants={}
    for (h,n),P in cosine.items():constants[n]=constants.get(n,fmpq(0))+P[0]
    assert all(v==0 for v in constants.values()),constants
    polys={}
    for (h,n),P in cosine.items():
        for (k,m),Q in cosine.items():
            if n!=m:continue
            key=h+k
            polys[key]=polys.get(key,ZERO)+P*Q/(2 if n==0 else 4)
    assert sum(P[0] for P in polys.values())==0
    positive=arb(0);records=[]
    for h,P in sorted(polys.items()):
        b=(h+2)*model.delta/2
        beta=1/b;part=fmpq(0)
        for n in range(1,len(P)):
            part+=P[n]*beta
            beta*=fmpq(n)/(n+b)
        val=ar(part)-ar(P[0])*ar(b).digamma()
        positive+=val
        records.append({'h':h,'b':str(b),'degree':P.degree(),'constant_coefficient':str(P[0]),'integral_finite_part':val.str(40)})
        print('integral component',h,'degree',P.degree(),'seconds',time.monotonic()-start,flush=True)
    aref=json.loads((ROOT/'research/radial_fourier/data/objective_reference.json').read_text())['a_ref_exact']
    a=fmpq(aref)
    objective=positive/(2*ar(a)**2)
    assert objective>0,objective
    print('J_abs',objective.str(80),flush=True)
    result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
            'canonical_sha256':model.state['canonical_serialization_sha256'],'a_ref_exact':str(a),
            'method':'Exact rational radial Fourier polynomials, exact angular orthogonality, rational Beta moments and Arb digamma finite parts',
            'elapsed_seconds':time.monotonic()-start,'angular_max_cosine':max(n for h,n in cosine),
            'exact_center_residual_zero':True,'J_abs':objective.str(100),'components':records,
            'scope':'Full radial axis and quadrant normalized J_abs; not a Sobolev residual norm.'}
    (ROOT/'research/radial_fourier/verification'/f'state131_J_{args.bits}.json').write_text(json.dumps(result,indent=2)+'\n')
