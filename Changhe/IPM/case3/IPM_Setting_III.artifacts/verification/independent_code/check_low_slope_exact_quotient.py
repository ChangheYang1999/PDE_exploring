"""Exact dyadic-axis witnesses; proof precedes code. Only frozen local inputs."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,math
from q_checkpoint_reader import QCheckpoint
from q_exact_jets import jets,value


def clenshaw(cc,t):
    b1=b2=F(0)
    for c in cc[:0:-1]:
        b0=F(float(c))+2*t*b1-b2;b2,b1=b1,b0
    return F(float(cc[0]))+t*b1-b2


def quotient(cc,a,s):
    return (1-s)*sum(((-s)**j*clenshaw(row,2*s-1) for j,row in enumerate(cc)),F(0))/a


def packed(q):return {'exact':str(q),'approx':float(q)}

started=datetime.now(timezone.utc).isoformat();count=0
# Manufactured Chebyshev recurrence and Cartesian-polynomial conversion.
for n in range(12):
    cc=[F(0)]*(n+1);cc[n]=F(1)
    for t in (F(-1),F(-3,4),F(0),F(1,3),F(1)):
        a,b=F(1),t
        for _ in range(n):a,b=b,2*t*b-a
        assert clenshaw(cc,t)==a;count+=1
rows=[]
for tag,name in [('LSF_CL3P0_N64_A1','lsF_cl3.0_N64_a1.pt'),('LSR_CL3P0_N96_A1','lsR_cl3.0_N96_a1.pt')]:
    src=Path('evidence/low_slope_20261021T0427Z')/name
    m=QCheckpoint(src);j=jets(m.coeff,m.kappa,m.cl);a=j['a']
    assert a>0 and j['e_core']>0 and a*j['delta']!=0;count+=3
    assert value(j['axis_minus_polynomial'],F(0))==a;count+=1
    assert j['axis_minus_polynomial'][1]==j['e_core'];count+=1
    witnesses=[]
    for k in [4,6,8,10,11,12,14,16,20,24,30,36]:
        s=F(1,2**k);q=quotient(m.coeff,a,s)
        assert q==value(j['axis_minus_polynomial'],s)/a;count+=1
        logy=math.log(m.L)-m.kappa*math.log(2)+.5*math.log(float(s))-m.kappa*math.log1p(-float(s))
        witnesses.append({'sigma':str(s),'q':packed(q),'q_minus_one':packed(q-1),'q_above_one':q>1,'approximate_y':math.exp(logy)})
    assert any(w['q_above_one'] for w in witnesses);count+=1
    rows.append({'tag':tag,'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'a':packed(a),'e_core':packed(j['e_core']),'q_y_derivative_at_sigma_zero':packed(j['e_core']/a),'canonical_delta':packed(j['delta']),'a_delta':packed(a*j['delta']),'witnesses':witnesses,'global_q_le_one':'REFUTED','smooth_finite_density':'CONFIRMED','nonflat_rho_minus_a_y':'CONFIRMED','exact_profile':'REFUTED'})
out=Path('research/low_slope_state_audit/verification');out.mkdir(parents=True,exist_ok=True)
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':count,'proof_sha256':hashlib.sha256(Path('research/low_slope_state_audit/PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'scope':'Exact finite formulas and exact compact-coordinate inequalities. Decimal physical coordinates approximate. Not a theorem about existence or exclusion of any exact IPM branch.'}
(out/'EXACT_QUOTIENT_WITNESSES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':count,'finished_utc':result['finished_utc'],'rows':[{'tag':r['tag'],'a':r['a']['approx'],'e_core':r['e_core']['approx'],'witness_1_over_2048':next({'sigma':w['sigma'],'q_minus_one':w['q_minus_one']['approx'],'y':w['approximate_y']} for w in r['witnesses'] if w['sigma']=='1/2048')} for r in rows]},indent=2))
