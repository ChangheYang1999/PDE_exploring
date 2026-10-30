"""Independent exact rational interval audit of T4-019's scalar box."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/graded_box_audit/code'))
from check import I,atan
BASE=ROOT/'research/l2_box_audit'
def parse(text):
    v=text.strip('[]').split('+/-')
    if len(v)==1:return I(v[0].strip())
    m,r=[Q(x.strip()) for x in v];return I(m-r,m+r)
def det(A):
    if len(A)==1:return A[0][0]
    return sum(((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A[0]))),Q(0))
def run():
    start=time.monotonic();old=json.loads((BASE/'data/T4_box.json').read_text())
    G=[[Q('1/4'),Q('-347/10'),Q(-5)],[Q('-347/10'),Q('53048/5'),Q(-49152)],[Q(-5),Q(-49152),Q(458752)]]
    minors=[det([row[:k] for row in G[:k]]) for k in range(1,4)]
    assert all(v>0 for v in minors);assert [str(v) for v in minors]==old['positive_leading_minors']
    C=[[Q(4708),Q('85/2'),Q(68)],[Q(0),Q(4290),Q(340)],[Q(0),Q(0),Q(3882)]]
    rows=[sum((abs((C[i][j]+C[j][i])/2) for j in range(3)),Q(0)) for i in range(3)]
    assert max(rows)<4800;assert [str(v) for v in rows]==old['commutator_symmetric_row_sums']
    smax=Q(1,1024);rough=Q(127,50)+Q(653,5)*smax+Q(9,5)*(1+44*smax)
    assert rough<5 and str(rough)==old['rough_As_plus_Bs_at_maximum_s']
    s=I(Q(1,131072));r=I(Q(1,16384));eta=I(Q(1,163840));pi=16*atan(Q(1,5),80)-4*atan(Q(1,239),20)
    beta=I('1/4')-4800*s-5*r/s.sqrt();image=eta/beta;gradient=r/(2*(pi*s*(1+s)).sqrt());contraction=gradient/2
    assert beta.a>Q(1,10) and image.b<r.a and gradient.b<Q(6234,1000000) and contraction.b<Q(312,100000)
    values={'high_decay_beta':beta,'selfmap_radius_upper':image,'gradient_bound':gradient,'L2_contraction_ratio':contraction}
    overlaps={}
    for key,v in values.items():
        w=parse(old[key]);overlaps[key]=max(v.a,w.a)<=min(v.b,w.b);assert overlaps[key]
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Exact rational determinants and rational intervals; Machin pi and integer square roots',
         'source_sha256':{p.name:sha256(p.read_bytes()).hexdigest() for p in [BASE/'data/T4_PROOF.md',BASE/'data/T4_box.json',Path(__file__)]},
         'positive_minors':[str(v) for v in minors],'commutator_symmetric_row_sums':[str(v) for v in rows],'rough_maximum':str(rough),
         'values':{k:v.record() for k,v in values.items()},'overlaps':overlaps,'all_scalar_conditions_pass':True,'elapsed_seconds':time.monotonic()-start}
    (BASE/'verification/rational_box.json').write_text(json.dumps(out,indent=2)+'\n');print('all scalar conditions and overlaps passed',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run()
