"""Independent exact Cartesian jet audit of an augmented primitive stream."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
from exact_bivariate import ordinary_stream_jet,unit_power,mul,add,scale
from primitive_center_certificate import residual_from_jet,coefficients
from primitive_tail_moments import data

def jet_from_state(state,degree=10):
    beta=Q(state['beta']);C=list(map(Q,state['C']))
    psi,_=ordinary_stream_jet(beta,state['labels'],C,[Q(0)]*len(C),degree)
    for row in state.get('extra_stream_terms',[]):
        power={(int(row['x_power']),int(row['y_power'])):Q(row['coefficient'])}
        cut=unit_power({(2,0):Q(1),(0,2):Q(1)},Q(row['R_power'])/2,degree)
        psi=add(psi,mul(power,cut,degree))
    return psi

def certificate(path):
    path=Path(path);state=json.loads(path.read_text());beta=Q(state['beta']);a0=Q(state.get('a0','1'))
    # Check the stated power decay before omitting extra terms from tail moments.
    for t in state.get('extra_stream_terms',[]):
        assert t['x_power']+t['y_power']+Q(t['R_power'])<2-2/beta
    psi=jet_from_state(state,10);r=residual_from_jet(beta,psi,6);low={k:v for k,v in r['R_Theta'].items()if sum(k)<=4}
    tail=data(beta,state['labels'],state['C'])
    center=r['strain']==1+beta/2 and r['omega_x']==4*a0/beta and r['a0']==a0
    return {'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':str(beta),
       'center_exact':center,'through_degree4_zero':not low,'leading_moments_exact_zero':tail['C_plus']==tail['C_minus']==0,
       'R_Theta_through_degree6':coefficients(r['R_Theta']),'verdict':'REFUTED_AS_EXACT_FIELD'if r['R_Theta']else'OPEN',
       'scope':'Literal exact integral field only. No quadrature certification or nearby-profile estimate.'}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args();out=a.root/'joint_exact_certificates';out.mkdir(exist_ok=True);summary=[]
    for path in sorted(a.root.glob('*_state.json')):
        row=certificate(path);dest=out/(path.stem+'_certificate.json');dest.write_text(json.dumps(row,indent=2)+'\n')
        summary.append({k:v for k,v in row.items()if k!='R_Theta_through_degree6'}|{'state':path.name,'nonzero_thermal_coefficients':[{'x_power':v['x_power'],'y_power':v['y_power'],'coefficient':float(Q(v['coefficient']))}for v in row['R_Theta_through_degree6']]})
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('certificates',len(summary),flush=True)
