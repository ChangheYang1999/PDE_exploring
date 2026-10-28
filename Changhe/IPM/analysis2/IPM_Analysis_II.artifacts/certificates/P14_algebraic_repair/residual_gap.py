"""Convert completed full-plane derivative certificates to E2 and N_s bounds."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
HERE=Path(__file__).resolve().parent
ctx.prec=768
rows=[]
for name in ['algebraic_n12_m10_k8','algebraic_n12_m10_k16']:
    path=HERE/(name+'_arb_norms.json')
    raw=path.read_bytes();data=json.loads(raw)
    assert data['status'] in ['PENDING_PROOF_AUDIT','CONFIRMED']
    assert len(data['cartesian_checks'])==7
    assert all(len(d['components'])==10 and all(d['components'].values()) for d in data['cartesian_checks'])
    assert data['resumes'][-1]['source_row_rechecked']
    norm={}
    for label,entry in data['norms'].items():
        low,high=arb(entry['lower_ball']),arb(entry['upper_ball'])
        ul,uh=arb(entry['u_lower_ball']),arb(entry['u_upper_ball'])
        assert all(x.is_finite() and x>0 for x in [low,high,ul,uh])
        assert low.overlaps(ul) and high.overlaps(uh)
        norm[label]=(low.lower(),high.upper())
    assert set(norm)=={'rF','F','DF','omega_D2F','omega_D3F'}
    def partial(index):
        return norm['omega_D2F'][index]**2+(128*norm['DF'][index])**2+(512*norm['F'][index])**2
    e_low=partial(0).sqrt()
    e_high=(partial(1)+(512*norm['rF'][1])**2*arb(20)/21).sqrt()
    ss=arb(1)/(2**18)
    ns_low=(1-34*ss)*e_low
    ns_high=e_high**(1-ss)*(2*norm['omega_D3F'][1]**2+16410*e_high**2)**(ss/2)+34*ss*e_high
    ratio=ns_low*1572864
    rows.append({'name':name,'source_record_sha256':hashlib.sha256(raw).hexdigest(),
       'canonical_sha256':data['canonical_sha256'],'norms':{k:{'lower':a.str(75),'upper':b.str(75)} for k,(a,b) in norm.items()},
       'E2_lower':e_low.str(75),'E2_upper_using_Hardy':e_high.str(75),
       'Ns_lower':ns_low.str(75),'Ns_upper':ns_high.str(75),
       'Ns_budget':'1/1572864','Ns_lower_divided_by_budget':ratio.str(75)})
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
        's':'1/262144','method':'V050 upper, V070 lower, Hminus <= ||rF||_2 by parity Hardy',
        'rows':rows,'status':'PENDING_PROOF_AUDIT'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
