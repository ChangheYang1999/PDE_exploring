"""Recheck the peer's seven-cell arithmetic using independent N4 norms."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx, fmpq as Q

BASE=Path(__file__).resolve().parents[1]
def H(p): return sha256(p.read_bytes()).hexdigest()
def ar(q): return arb(q.numerator)/q.denominator
def run():
    start=time.monotonic();ctx.prec=1024
    target=BASE/'verification/T4_116_cover_confirmation.json';assert not target.exists()
    ownfile=BASE/'verification/d2.json';own=json.loads(ownfile.read_text())
    archive=BASE/'peer_review/T4_116'
    peer=json.loads((archive/'d2_cover.json').read_text())
    assert peer['code_sha256']==H(archive/'cover.py')
    assert peer['proof_sha256']==H(archive/'UNIFORM_COVER.md')
    assert peer['source_sha256']==H(BASE/'source/T4_d2_2048.json')
    assert peer['all_seven_cells_pass']
    norms={Q(r['a']):arb(r['weighted_laplacian_norm']) for r in own['weights']}
    c=Q(own['c']);A=1+1/c
    assert A<Q(7,4)
    count=0;rows=[]
    for j,p in enumerate(peer['cells']):
        l,h=Q(j,4),Q(j+1,4)
        assert Q(p['left'])==l and Q(p['right'])==h
        assert Q(p['restricted_to_a_less_than'])==A
        J=norms[h] if j<6 else norms[Q(3,2)]**2/norms[Q(5,4)]
        lower=arb(5)**ar((l-2)/2)*J
        ceiling=(8*arb.pi()).sqrt()*ar((1+c-c*l)**2/(1+l))
        values={'Y_lower_bound':lower,'ceiling_upper_bound':ceiling,
                'gap':lower-ceiling,'ratio':lower/ceiling}
        assert values['gap']>0 and values['ratio']>1
        for k,v in values.items():
            assert v.overlaps(arb(p[k])), (j,k)
            count+=1
        rows.append({'left':str(l),'right':str(h),
                     **{k:v.str(85) for k,v in values.items()}})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'own_norms_sha256':H(ownfile),'peer_cover_sha256':H(archive/'d2_cover.json'),
         'code_sha256':H(Path(__file__)),'precision_bits':ctx.prec,
         'all_seven_cells_confirmed':True,'component_overlaps':count,'cells':rows,
         'last_cell_method':'Cauchy-Schwarz at5/4,3/2,7/4; independent of N4 endpointA',
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Arithmetic cover confirmed. Use for the stated dyadic scheme still needs independent theory review of its continuous plateau estimate. The N4 endpointA norm is not peer-reproduced here.'}
    target.write_text(json.dumps(out,indent=2)+'\n')
    print('All seven cells agree; component overlaps',count,'seconds',out['elapsed_seconds'])
if __name__=='__main__':run()
