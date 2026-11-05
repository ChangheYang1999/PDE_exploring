"""Reuse checked L2 core panels with a signed homogeneous far certificate.

For r>=R, factor out the leading negative gradient power r^p. Exact far
coefficients and uniform differentiated analytic tails enclose each remaining
angular coefficient independently of r. The signed theta function is positive
homogeneous and decreasing in its second argument, so it is bounded by the
leading angular cover plus all explicitly charged normalized remainders.
No old chunk configuration or frozen source file is modified.
"""
import argparse,json
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx,fmpq as Q
from fields013 import Evaluator,C,rational_arb,SOURCE_HASHES
from asymptotics013 import Expansion
import certify_L2_013 as original

HERE=Path(__file__).resolve().parent


def signed_far(expansion,R,nt=2048):
    components=[expansion.field('rho',1,0),expansion.field('rho',0,1)]
    power=max(p for component in components for kind,n,p in component)
    assert power<0
    leading=[];errors=[]
    for derivative,component in zip([(1,0),(0,1)],components):
        leading.append({(kind,n):arb(a)for(kind,n,p),a in component.items()if p==power})
        error=sum((arb(abs(a))*R**rational_arb(p-power)
                   for(kind,n,p),a in component.items()if p<power),arb(0))
        for a,p in expansion.remainder_terms('rho',*derivative,R):
            assert p<power
            error+=a*R**rational_arb(p-power)
        errors.append(error.abs_upper())
    maximum=arb(0);worst=None
    for index in range(nt):
        theta=arb.pi()*(2*index+1)/(4*nt)+arb(0,arb.pi()/(4*nt))
        values=[]
        for modes in leading:
            value=arb(0)
            for(kind,n),coefficient in modes.items():
                trig=(n*theta).sin()if kind=='s'else(n*theta).cos()
                value+=coefficient*trig
            values.append(value)
        aa=values[0].abs_upper()+errors[0];bb=values[1].lower()-errors[1]
        # theta(a,b) increases with |a| and decreases with b, for all real b.
        bound=((aa*aa+bb*bb).sqrt()-bb)/2
        if bound.upper()>maximum:
            maximum=bound.upper();worst=index
    bound=(R**rational_arb(power)*maximum).upper()
    return {'theta_upper':bound.str(80),'common_gradient_power':str(power),
            'normalized_remainders':[error.str(80)for error in errors],
            'normalized_theta_upper':maximum.str(80),'angular_arcs':nt,
            'worst_angular_index':worst,'endpoint':R.str(80)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-out',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--panels',type=int,default=2016)
    ap.add_argument('--far-only',action='store_true');ap.add_argument('--angular-arcs',type=int,default=2048);ap.add_argument('--expansion-degree',type=int,default=24)
    args=ap.parse_args();config=json.loads((args.source_out/'configuration.json').read_text())
    assert config['source_hashes']==SOURCE_HASHES and config['code_hashes']==original.bindings()
    assert 0<args.panels<config['panels'];ctx.prec=config['precision']
    e=Evaluator(config['precision'],2,-1);near=Expansion(e,'origin',12);far=Expansion(e,'far',args.expansion_degree)
    ratio=rational_arb(Q(config['ratio']));R=rational_arb(Q(config['rmin']))*ratio**args.panels
    tail=signed_far(far,R,args.angular_arcs);T=rational_arb(Q(config['theta']))
    args.out.mkdir(parents=True,exist_ok=True)
    own_hash=sha256(Path(__file__).read_bytes()).hexdigest()
    if args.far_only:
        result={'status':'CERTIFIED_SIGNED_FAR_THETA'if arb(tail['theta_upper'])<T else 'FAR_THETA_TARGET_FAILED',
                'far_theta':tail,'source_configuration':config,'assembler_sha256':own_hash,
                'panels_required':args.panels,'far_expansion_degree':args.expansion_degree,'finished_utc':datetime.now(timezone.utc).isoformat()}
        (args.out/'far_theta_result.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result,indent=2),flush=True);return
    rows={};chunks={}
    for file in sorted(args.source_out.glob('chunk_*.json')):
        record=json.loads(file.read_text());assert record['configuration']==config
        used=False
        for row in record['rows']:
            if row['index']<args.panels:
                assert row['index']not in rows;rows[row['index']]=row;used=True
        if used:chunks[file.name]=sha256(file.read_bytes()).hexdigest()
    assert sorted(rows)==list(range(args.panels))
    integrals={}
    for key in [('rho',2,0),('rho',1,1),('rho',0,2)]:
        core=sum((arb(row['radial_integrals'][str(key)])for row in rows.values()),arb(0))
        origin=near.tail_L2_bound(*key,config['rmin']);exterior=far.tail_L2_bound(*key,R)
        integrals[str(key)]={'core_squared_upper':core.str(80),'origin_L2_upper':origin.str(80),
            'exterior_L2_upper':exterior.str(80),'total_squared_upper':(core+origin**2+exterior**2).str(80)}
    xx,xy,yy=[arb(integrals[str(key)]['total_squared_upper'])for key in [('rho',2,0),('rho',1,1),('rho',0,2)]]
    kappa=(((arb(2).log()-arb(1)/2)*(xx+xy)+(3*arb(2).log()-2)*(xy+yy))/(16*arb.pi())).sqrt()
    bx=near.point_bound('rho',1,0,config['rmin']);by_rem=near.point_bound('rho',0,1,config['rmin'],True)
    leading=[(kind,n,coefficient)for(kind,n,p),coefficient in near.field('rho',0,1).items()if p==0]
    assert all(kind=='c'and n==0 for kind,n,coefficient in leading)
    assert not any(p==0 for(kind,n,p)in near.field('rho',1,0))
    a0=sum((arb(coefficient)for kind,n,coefficient in leading),arb(0))
    nearpass=bool(bx**2<4*T*(a0-by_rem+T)and a0-by_rem+2*T>0)
    farpass=bool(arb(tail['theta_upper'])<T);corepass=all(row['theta_pass']for row in rows.values())
    beta=rational_arb(C)+1-T-kappa
    result={'status':'CERTIFIED_DIRECT_L2'if nearpass and farpass and corepass else 'THETA_COVER_FAILED',
            'source_configuration':config,'assembler_sha256':own_hash,'used_chunk_sha256':chunks,
            'core_panels_used':args.panels,'far_expansion_degree':args.expansion_degree,'core_endpoint':R.str(80),'far_theta':tail,
            'theta_origin_pass':nearpass,'theta_core_pass':corepass,'theta_exterior_pass':farpass,
            'theta_failed_panel_indices':[i for i,row in rows.items()if not row['theta_pass']],
            'theta_upper':config['theta'],'integrals':integrals,'kappa_HS_upper':kappa.str(80),
            'beta_L2_lower':beta.str(80),'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Whole-plane Candidate013 scalar coercivity. Exact signed far expansion replaces only the far theta bound; all Hessian tails remain charged. Operator realization and high-order closure are separate.'}
    (args.out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
