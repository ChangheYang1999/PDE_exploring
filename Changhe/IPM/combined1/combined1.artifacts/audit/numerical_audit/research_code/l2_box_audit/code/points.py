"""Rational interval postprocessing of confirmed field triples for T4-019."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/graded_box_audit/code'))
from check import I,atan
BASE=ROOT/'research/l2_box_audit'
def parse(text):
    v=text.strip('[]').split('+/-')
    if len(v)==1:return I(v[0].strip())
    m,r=[Q(x.strip()) for x in v];return I(m-r,m+r)
def absI(x):
    return x if x.a>=0 else -x if x.b<=0 else I(0,max(-x.a,x.b))
source=ROOT/'research/point_witness/verification/cartesian_witnesses.json';data=json.loads(source.read_text())
pi=16*atan(Q(1,5),80)-4*atan(Q(1,239),20);s=I(Q(1,131072));r=I(Q(1,16384))
C0=1/(4*pi*(1+s)).sqrt();C1=1/(8*pi*s*(1+s)).sqrt();rows=[]
for row in data['rows']:
    f={k:parse(v) for k,v in row['fields'].items()};upper=(C1*f['velocity_norm']+C0*(1+f['gradient_norm']))*r+C0*C1*r*r
    gap=absI(f['residual'])-upper;assert gap.a>0
    rows.append({'candidate':row['candidate'],'point':row['point'],'gap':gap.record(),'necessary_upper':upper.record(),'positive_gap':True})
    print(row['candidate'],'positive gap',gap.record()['midpoint_float'],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'s':str(s.a),'radius':str(r.a),'framework':'T4-019 no-H specified ball',
     'source_sha256':sha256(source.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows}
(BASE/'verification/point_gaps.json').write_text(json.dumps(out,indent=2)+'\n')
