"""Own rational Cartesian Taylor audit of a stream-only primitive, packet131."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
from exact_bivariate import ordinary_stream_jet,lap,diff,add,scale,dot_grad,trunc


def residual_from_jet(beta,psi,degree=4):
    beta=Q(beta);psi=dict(psi);psi.pop((1,0),None)
    omega=scale(lap(psi),-1)
    W=(add({(1,0):beta},scale(diff(psi,1),-1)),add({(0,1):beta},diff(psi,0)))
    F=add(dot_grad(W,omega,degree+2),omega);F=trunc(F,degree+2)
    assert all(i%2 for i,j in F),'source parity failed'
    theta={(i+1,j):a/(i+1)for(i,j),a in F.items()}
    residual=trunc(add(dot_grad(W,theta,degree),scale(theta,-(beta-2))),degree)
    return {'Theta':theta,'Omega':omega,'R_Theta':residual,'strain':psi.get((1,1),Q(0)),'omega_x':omega.get((1,0),Q(0)),'a0':theta.get((2,0),Q(0))}

def coefficients(p):return [{'x_power':i,'y_power':j,'coefficient':str(c)}for(i,j),c in sorted(p.items())]
def certificate(path):
    path=Path(path);state=json.loads(path.read_text());beta=Q(state['beta']);C=list(map(Q,state['C']));D=[Q(0)]*len(C)
    psi,_=ordinary_stream_jet(beta,state['labels'],C,D,8);r=residual_from_jet(beta,psi)
    center=r['strain']==1+beta/2 and r['omega_x']==4*Q(state.get('a0','1'))/beta and r['a0']==Q(state.get('a0','1'))
    return {'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':str(beta),'strain':str(r['strain']),'omega_x':str(r['omega_x']),'a0':str(r['a0']),'prescribed_center_exact':center,'R_Theta':coefficients(r['R_Theta']),
        'verdict':'REFUTED_AS_EXACT_FIELD'if r['R_Theta']else'OPEN','scope':'Only literal serialized field; no nearby-profile estimate. Vorticity identity applies to the exact integral, not an unchecked quadrature.'}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);args=ap.parse_args();out=args.root/'primitive_center_certificates';out.mkdir(exist_ok=True);summary=[]
    for path in sorted(args.root.glob('*_state.json')):
        c=certificate(path);dest=out/(path.stem+'_certificate.json');dest.write_text(json.dumps(c,indent=2)+'\n')
        summary.append({'state':path.name,'sha256':c['sha256'],'beta':float(Q(c['beta'])),'center_exact':c['prescribed_center_exact'],'verdict':c['verdict'],'nonzero_thermal_coefficients':[{'x_power':v['x_power'],'y_power':v['y_power'],'coefficient':float(Q(v['coefficient']))}for v in c['R_Theta']],'certificate':str(dest.relative_to(args.root))})
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('certificates',len(summary),flush=True)
