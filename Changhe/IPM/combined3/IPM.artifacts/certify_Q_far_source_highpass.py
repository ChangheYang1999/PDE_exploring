#!/usr/bin/env python3
"""Actual far Q source low/high bounds; not a full energy certificate."""
from datetime import datetime,timezone
from hashlib import sha256
import json
from pathlib import Path
import sys,time
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'coercivity_residual'))
from fields013 import Evaluator,rational_arb,C,SOURCE_HASHES
from asymptotics013 import Expansion

def main():
    start=time.monotonic()
    ctx.prec=384
    e=Evaluator(384,max_density_order=2,max_velocity_order=0)
    expansion=Expansion(e,'far',degree=12)
    mu=arb(1);alpha=arb(7)/4;pi=arb.pi()
    def moment(s):
        return arb(2)**(s/2)*(1+s/2).gamma()/mu**s
    m1,m3=moment(arb(1)),moment(arb(3))
    M2=5/mu**2;M3=3*(2*pi).sqrt()/mu**3
    Calpha=arb(2)**((alpha-1)/2)*2/(2-alpha)
    Ialpha=2*m1+arb(2)**alpha*moment(alpha)
    Cstar=4*arb(2).sqrt()/pi.sqrt()+(pi/2).sqrt()
    rows=[]
    for Rint in [1000,10000,30000,100000]:
        R=arb(Rint)
        bx=expansion.point_bound('rho',1,0,R)
        by=expansion.point_bound('rho',0,1,R)
        xx=expansion.point_bound('rho',2,0,R)
        xy=expansion.point_bound('rho',1,1,R)
        yy=expansion.point_bound('rho',0,2,R)
        # Multiplication by r preserves monotonicity of every Hessian
        # majorant; verify this for both the exact finite part and tail.
        for i,j in [(2,0),(1,1),(0,2)]:
            assert all(power+1<0 for kind,n,power in
                       expansion.field('rho',i,j))
            assert all(power+1<0 for a,power in
                       expansion.remainder_terms('rho',i,j,R))
        B=(bx*bx+by*by).sqrt()
        D=(xx*xx+2*xy*xy+yy*yy).sqrt()
        Lb=D+2*B/R
        # eta=0 on [0,R], eta=1 on [2R,infinity),
        # |eta'|<=2/R. W<=4R+1 throughout its transition.
        Ld=(2+2*(4+1/R))*B+(4+1/R**2).sqrt()*R*D
        UH=(Ld*M2+8*B*M3)/R**2
        term1=B*(2*R)**(1-alpha)*Calpha*Ialpha
        term2=(arb(3).sqrt()+1)*Lb*m1
        term3=arb(3).sqrt()*B*(2*m1/R+8*m3/R**2)
        EH=UH+(term1+term2+term3)/2
        epsE=2*EH
        epsC=2*Cstar*Lb/mu
        low=(arb(3).sqrt()+1)*B
        row={'R':Rint,'B':B.str(75),'D':D.str(75),
             'Lb':Lb.str(75),'Ld':Ld.str(75),
             'E_UH_norm':UH.str(75),
             'E_high_norm':EH.str(75),
             'E_high_cross_error':epsE.str(75),
             'Cvs3_high_cross_error':epsC.str(75),
             'joint_source_high_cross_error':(epsE+epsC).str(75),
             'joint_source_low_p2_coefficient':low.str(75),
             'global_half_dilation_minus_source_low':
                 (arb(21)/10*rational_arb(C)/2-low).str(75)}
        rows.append(row)
        print(row,flush=True)
    files=[Path(__file__),HERE/'Q_FAR_WEIGHT_COMMUTATOR_HIGHPASS.md',
           HERE/'finite_rank/CENTRAL_ODD_WEIGHTED_BEURLING.md',
           HERE/'finite_rank/GAUSSIAN_RIESZ_HIGHPASS_FAR.md',
           HERE/'coercivity_residual/fields013.py',
           HERE/'coercivity_residual/asymptotics013.py']
    result={'status':'CERTIFIED_ACTUAL_FAR_Q_SOURCE_LOW_HIGH_BOUNDS',
            'mu':'1','alpha':'7/4',
            'cutoff':'eta=0 r<=R, eta=1 r>=2R, |eta prime|<=2/R',
            'source_hashes':SOURCE_HASHES,
            'bindings':{str(p.relative_to(HERE)):
                        sha256(p.read_bytes()).hexdigest() for p in files},
            'rows':rows,'elapsed_seconds':time.monotonic()-start,
            'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Cvs3 and Q weight-source form for eta*grad rho only. '
                    'All low/high cross errors included. No near-source, '
                    'transport, complete linear energy or existence claim.'}
    (HERE/'Q_far_source_highpass_result.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(result['status'],flush=True)

if __name__=='__main__':
    main()
