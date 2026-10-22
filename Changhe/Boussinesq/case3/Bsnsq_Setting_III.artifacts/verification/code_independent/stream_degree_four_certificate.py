"""Own bivariate Taylor rejection through R_Theta degree4, R_Omega degree3.

Evaluates actual field polynomials directly, without any six-pivot moments.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,hashlib
import exact_bivariate as P
from stream_local_jet_certificate import parse

def checks(data):
    beta,labels,C,D=parse(data)
    psi,theta=P.ordinary_stream_jet(beta,labels,C,D,6)
    rt,ro=P.pde(beta,psi,theta,6)
    rt,ro=P.trunc(rt,4),P.trunc(ro,3)
    return {'beta':str(beta),'R_Theta_through_degree4':P.serialize(rt),
        'R_Omega_through_degree3':P.serialize(ro),
        'nonzero':{'temperature':bool(rt),'vorticity':bool(ro)},
        'prescribed_lower_coefficients_zero':not P.trunc(rt,3) and not P.trunc(ro,2),
        'verdict':'REFUTED_AS_EXACT_FIELD' if rt or ro else 'OPEN',
        'scope':'exact Taylor coefficients of this serialized field; no nearby-profile estimate'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args()
    out=a.root/'degree_four_certificates';out.mkdir(exist_ok=True);rows=[]
    for path in sorted(a.root.glob('*_state.json')):
        data=json.loads(path.read_text());cert=checks(data)
        cert.update(source_path=str(path.resolve()),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            created_utc=datetime.now(timezone.utc).isoformat())
        target=out/(path.stem+'_certificate.json');target.write_text(json.dumps(cert,indent=2)+'\n')
        loaded=json.loads(target.read_text())
        assert all(loaded[k]==v for k,v in checks(json.loads(path.read_text())).items())
        rows.append({'state':path.name,'source_sha256':cert['source_sha256'],'certificate':str(target.relative_to(a.root)),
            'verdict':cert['verdict'],'prescribed_lower_coefficients_zero':cert['prescribed_lower_coefficients_zero'],
            'R_Theta_float':[{**v,'coefficient':float(Q(v['coefficient']))}for v in cert['R_Theta_through_degree4']],
            'R_Omega_float':[{**v,'coefficient':float(Q(v['coefficient']))}for v in cert['R_Omega_through_degree3']]})
        print(path.name,cert['verdict'],'lower_zero',cert['prescribed_lower_coefficients_zero'],flush=True)
    (out/'summary.json').write_text(json.dumps(rows,indent=2)+'\n')
    print('COMPLETE',len(rows),flush=True)
if __name__=='__main__':main()
