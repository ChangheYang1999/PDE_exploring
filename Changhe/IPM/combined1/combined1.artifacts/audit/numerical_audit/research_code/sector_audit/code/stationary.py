"""Independent stationary principal recursion using Cartesian homogeneous fields."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, time
import sys
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from sectors import enc,aq,dx,dy,add,product_cs
ROOT=Path(__file__).resolve().parents[3]

def density(C,s):
    return {n:-v for n,v in dy({n:(s*s-n*n)*v for n,v in C.items()},s-2,'c').items()}

def invert_density(G,s):
    todo=G.copy();C={}
    for n in range(max(G)-1,-1,-2):
        image=density({n:Q(1)},s)
        assert image.get(n+1,0)!=0
        coeff=todo.get(n+1,Q(0))/image[n+1]
        if coeff:C[n]=coeff
        todo=add(todo,image,-coeff)
    assert not todo
    return C

def fields(C,alpha):
    s=alpha+3;G=density(C,s)
    stream=dy(dx(C,s,'c'),s-1,'c')
    return G,{n:-v for n,v in dy(stream,s-2,'s').items()},dx(stream,s-2,'s'),dx(G,alpha,'s'),dy(G,alpha,'s')

if __name__=='__main__':
    ctx.prec=256;start=time.monotonic()
    d=json.loads((ROOT/'research/baseline/data/state131_independent.json').read_text())
    c=Q(d['cl']);g=1/c;delta=1-g
    C0={}
    for (j,m,k),v in zip(d['order'],d['coefficients']):
        if j==0:C0[2*m]=C0.get(2*m,Q(0))+Q(v)
    CP=[C0]; FF=[fields(C0,g)];records=[]
    for j in range(1,9):
        force={}
        for i in range(j):
            k=j-1-i
            Gi,U1i,U2i,RXi,RYi=FF[i]
            Gk,U1k,U2k,RXk,RYk=FF[k]
            force=add(force,product_cs(U1i,RXk))
            force=add(force,product_cs(RYk,U2i))
        alpha=g-j*delta
        Gj={n:v/(j*(c-1)) for n,v in force.items()}
        Cj=invert_density(Gj,alpha+3)
        ff=fields(Cj,alpha)
        assert ff[0]==Gj
        norm=(arb.pi()*aq(sum(v*v for v in force.values()))).sqrt()
        rec={'index':j,'residual_exponent':enc(alpha),'residual_exponent_arb':aq(alpha).str(25),
             'forcing_full_circle_norm':norm.str(40),'max_density_harmonic':max(Gj),
             'potential_cos':{str(n):enc(v) for n,v in sorted(Cj.items())},
             'stationary_density_sin':{str(n):enc(v) for n,v in sorted(Gj.items())},
             'forcing_sin':{str(n):enc(v) for n,v in sorted(force.items())}}
        CP.append(Cj);FF.append(ff);records.append(rec)
        print('branch',j,'exponent',rec['residual_exponent_arb'],'forcing norm',rec['forcing_full_circle_norm'],'highest density harmonic',max(Gj),'seconds',time.monotonic()-start,flush=True)
        out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'canonical_sha256':d['canonical_serialization_sha256'],
             'scope':'Finite exact principal stationary recursion; not convergence or a complete candidate.',
             'elapsed_seconds':time.monotonic()-start,'cl':d['cl'],'leading_potential':{str(n):enc(v) for n,v in C0.items()},'branches':records}
        (ROOT/'research/sector_audit/verification/stationary_principal.json').write_text(json.dumps(out,indent=2)+'\n')
