"""Rational interval extensions of saved Cartesian point certificates."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/l2_box_audit/code'))
from sharp_snapshot_points import I,atan,parse,absolute

def digest(path):return sha256(path.read_bytes()).hexdigest()
def run(name):
 start=time.monotonic()
 source=ROOT/f'research/candidate_audits/verification/{name}_point.json'
 canonical=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
 d=json.loads(source.read_text());data=json.loads(canonical.read_text())
 assert d['canonical_sha256']==digest(canonical)
 pi=16*atan(Q(1,5),80)-4*atan(Q(1,239),20)
 f={k:parse(d['fields'][k]) for k in ['residual','velocity_norm','gradient_norm','rho_x','rho_y']}
 theta=(f['gradient_norm']-f['rho_y'])/2
 c=Q(data['cl']);gap=theta-(c-1)
 rows=[]
 for label,s,r in [('sharp',Q(1,7744),Q(147,200000)),('sharpw',Q(1,5184),Q(1351,1000000))]:
  C0=1/(4*pi*(1+s)).sqrt();C1=1/(8*pi*s*(1+s)).sqrt()
  B=C1*f['velocity_norm']+C0*(1+f['gradient_norm']);A=C0*C1
  upper=B*r+A*r*r;dist=2*absolute(f['residual'])/(B+(B*B+4*A*absolute(f['residual'])).sqrt())
  pointgap=absolute(f['residual'])-upper
  rows.append({'framework':'FW-T-T4L2-'+label+'-v1','s':str(s),'radius':str(r),'necessary_upper':upper.record(),'gap':pointgap.record(),'strict_positive_gap':pointgap.a>0,'necessary_H2s_radius_lower':dist.record()})
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'point':d['point'],'canonical_sha256':digest(canonical),'point_record_sha256':digest(source),'code_sha256':digest(Path(__file__)),'point_proof_sha256':digest(ROOT/'research/l2_box_audit/PROOF.md'),'signed_proof_sha256':digest(ROOT/'research/background_points/PROOF.md'),'theta_at_point':theta.record(),'theta_minus_c_minus_1':gap.record(),'signed_criterion_fails_even_kappa_zero':gap.a>0,'sharp_ball_exclusions':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Saved point fields only; no new field evaluation or global upper bound. Fixed exact c.'}
 dest=ROOT/f'research/candidate_audits/verification/{name}_point_extensions.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 print(name,'theta',float((theta.a+theta.b)/2),'signed gap',float((gap.a+gap.b)/2),'sharp gaps',[float((parse_record(q['gap']).a+parse_record(q['gap']).b)/2) for q in rows],flush=True)
def parse_record(r):return I(Q(r['lower']),Q(r['upper']))
if __name__=='__main__':
 for name in sys.argv[1:]:run(name)
