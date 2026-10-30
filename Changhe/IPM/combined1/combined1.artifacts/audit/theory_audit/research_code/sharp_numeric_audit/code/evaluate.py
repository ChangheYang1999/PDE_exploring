from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
import json,time
from flint import arb,ctx
base=Path(__file__).resolve().parents[1];ctx.prec=768;start=time.monotonic()
def ar(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
def digest(p):return sha256(p.read_bytes()).hexdigest()
old=json.loads((base/'source/N4_T2_R3.json').read_text());norms={};hashes={}
for key in ('G0','G1','P2','Q3'):
 path=base/'source'/f'd2_{key}.json';d=json.loads(path.read_text())
 norms[key]=(arb(d['norm_lower_ball']),arb(d['norm_upper_ball']));hashes[key]=digest(path)
rows=[];points=[]
for name,s,w1,w2,R,eta in [('sharp',Fraction(1,7744),2**14,2**18,Fraction(147,200000),Fraction(76219,10**9)),('sharpw',Fraction(1,5184),2**15,2**20,Fraction(1351,10**6),Fraction(4207,20000000))]:
 sa=ar(s);radius=ar(R);C0=1/(4*arb.pi()*(1+sa)).sqrt();C1=1/(8*arb.pi()*sa*(1+sa)).sqrt()
 for num in ('002','003','004'):
  path=base/'source'/f'{num}_fields.json';d=json.loads(path.read_text());f={k:arb(v) for k,v in d['fields'].items()}
  A=C1*f['velocity_norm']+C0*(1+f['gradient_norm']);B=C0*C1
  limit=A*radius+B*radius**2;gap=abs(f['residual'])-limit;assert gap>0
  points.append({'framework':'FW-T-T4L2-'+name+'-v1','candidate':d['candidate'],'s':str(s),'R':str(R),'point':d['point'],
                 'input_sha256':digest(path),'necessary_upper':limit.str(80),'positive_gap':gap.str(80),'excludes_ball':True})
 lower=((1-ar(Fraction(48,25))*sa)**2*norms['P2'][0]**2+w1*norms['G1'][0]**2+w2*norms['G0'][0]**2).sqrt()
 E=(norms['P2'][1]**2+w1*norms['G1'][1]**2+w2*norms['G0'][1]**2).sqrt()
 Cw=max(Fraction(1)+Fraction(32,25)+w1,Fraction(1)+Fraction(w2,w1))
 upper=E*((2*norms['Q3'][1]**2/E**2+ar(Cw))**ar(s/2))+ar(Fraction(48,25))*sa*E
 ratio=lower/ar(eta);row=old['rows'][len(rows)]
 assert lower.overlaps(arb(row['d2_X_lower']));assert upper.overlaps(arb(row['d2_X_upper']));assert ratio.overlaps(arb(row['d2_lower_ratio']))
 rows.append({'framework':row['framework'],'s':str(s),'eta':str(eta),'Cw':str(Cw),'X_lower':lower.str(80),'X_upper':upper.str(80),
              'lower_threshold_ratio':ratio.str(80),'N4_conversion_overlap':True})
record={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':digest(base/'PROOF.md'),'code_sha256':digest(Path(__file__)),
        'N4_target_sha256':digest(base/'source/N4_T2_R3.json'),'component_sha256':hashes,'point_exclusions':points,'d2_raw_conversion':rows,
        'precision_bits':ctx.prec,'elapsed_seconds':time.monotonic()-start}
(base/'verification/results.json').write_text(json.dumps(record,indent=2)+'\n')
for p in points:print(p['framework'],p['candidate'],p['positive_gap'][:54])
for r in rows:print(r['framework'],r['X_lower'][:54],r['lower_threshold_ratio'][:54])
print('seconds',record['elapsed_seconds'])
