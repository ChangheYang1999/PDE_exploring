#!/usr/bin/env python3
"""Actual signed-K exterior matrix bounds; current matrix cover untouched."""
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,time
from pathlib import Path
from flint import arb,fmpq as Q,ctx
HERE=Path(__file__).resolve().parent;ART=HERE.parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(ART/'coercivity_residual'))
from fields013 import Evaluator,C,SOURCE_HASHES,rational_arb
from asymptotics013 import Expansion
def hashfile(p):return sha256(Path(p).read_bytes()).hexdigest()
def scaled(ex,name,i,j,r,shift):
    out=arb(0)
    for (_,_,p),a in ex.field(name,i,j).items():
        assert p+shift<0
        out+=arb(abs(a))*r**rational_arb(p+shift)
    for a,p in ex.remainder_terms(name,i,j,r):
        assert p+shift<0
        out+=a*r**rational_arb(p+shift)
    return out
def main():
    ctx.prec=384;tick=time.monotonic();e=Evaluator(384,1,1);ex=Expansion(e,'far',12)
    l2p=ART/'coercivity_residual/L2_signed_far_v05/result.json';l2=json.loads(l2p.read_text())
    assert l2['status']=='CERTIFIED_DIRECT_L2' and l2['source_configuration']['source_hashes']==SOURCE_HASHES
    signed=l2['far_theta'];p=Q(signed['common_gradient_power']);assert p<0
    nt=arb(signed['normalized_theta_upper']).abs_upper();R0=arb(signed['endpoint'])
    c=rational_arb(C);q=arb(21)/10;beta=arb(7)/10;rows=[]
    for radius in [10000,30000,100000,300000,1000000]:
        r=arb(radius);assert r>R0
        ux=scaled(ex,'u1',0,0,r,-1);uy=scaled(ex,'u2',0,0,r,-1)
        uf=(ux*ux+uy*uy).sqrt()
        sf=ex.point_bound('u1',1,0,r)+(ex.point_bound('u1',0,1,r)+ex.point_bound('u2',1,0,r))/2
        theta=nt*r**rational_arb(p)
        lower=1+(2-q)*c-c/(1+4*r*r)-uf-q*sf-theta
        assert lower.is_finite()
        rows.append({'radius':radius,'u_over_r_upper':uf.str(80),'strain_upper':sf.str(80),'signed_K_loss_upper':theta.str(80),
                     'matrix_lower':lower.str(80),'passes_beta_7_over_10':bool(lower>=beta)})
    files=[Path(__file__),ART/'coercivity_residual/fields013.py',ART/'coercivity_residual/asymptotics013.py',l2p]
    out={'status':'SIGNED_MATRIX_FAR_PRICE_COMPLETE','source_hashes':SOURCE_HASHES,'fixed_c':str(C),'q':'21/10','weight_a':'2',
         'expansion_degree':12,'signed_theta_origin':signed,'rows':rows,
         'bindings':{str(p.relative_to(ART)):hashfile(p) for p in files},'elapsed_seconds':time.monotonic()-tick,
         'finished_utc':datetime.now(timezone.utc).isoformat(),'scope':'Actual exterior matrix only; no core or full stationary claim'}
    dest=HERE/'signed_matrix_far_price_v01.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
