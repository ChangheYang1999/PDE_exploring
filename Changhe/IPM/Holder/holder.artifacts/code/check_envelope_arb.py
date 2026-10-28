"""Brute-force independent checks of the certified finite-tree evaluator."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from envelope_arb import ArbEnvelope
from envelope_witness import Envelope
import numpy as np,time,json
ctx.prec=160

def main():
    tree=ArbEnvelope();floating=Envelope();rng=np.random.default_rng(117779)
    points=np.vstack([[[.5,0],[-.5,0],[0,0],[.5,.5]],rng.normal(size=(100,2))*10**rng.uniform(-7,6,(100,1))])
    start=time.monotonic();counts=[];errors=[]
    floats,_=floating.evaluate(points)
    for index,point in enumerate(points):
        x,y=[arb(str(v)) for v in point];value,nearest=tree.evaluate(x,y);counts.append(tree.last_counts.copy())
        # Different control flow, full scan, no spatial pruning.
        upper=[];lower=[];dist=[]
        for px,py,v in tree.exact:
            d=((x-px)**2+(y-py)**2).sqrt();r=d.sqrt();upper.append(v+r);lower.append(v-r);dist.append(d)
        U=upper[0];L=lower[0];D=dist[0]
        for a,b,d in zip(upper[1:],lower[1:],dist[1:]):U=arb.min(U,a);L=arb.max(L,b);D=arb.min(D,d)
        reference=(U+L)/2
        assert value.overlaps(reference) and nearest.overlaps(D)
        errors.append(abs(float(value.mid())-floats[index]))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),queries=len(points),all_bruteforce_intervals_overlap=True,max_float_difference=max(errors),average_vertices=float(np.mean([x['vertices'] for x in counts])),maximum_vertices=max(x['vertices'] for x in counts),average_tree_nodes=float(np.mean([x['nodes'] for x in counts])),elapsed_seconds=time.monotonic()-start,status='Exact-interval tree versus independent full scan; floating comparison is diagnostic only')
    Path('data/envelope_tree_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
