"""Create separately defined exact fields B/C and compare with literal field A.
Derivation: research/exact_parameter_fields/PROOF.md, written before code.
"""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import copy,hashlib,json,random,time
import mpmath as mp
from smooth_mp_primitives import SmoothMP,rational
from smooth_far_coefficients import at_point
from q_exact_jets import chebyshev_in_sigma

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encoded(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
def save(p,d):Path(p).write_text(json.dumps(d,indent=2)+'\n')
def numbers(data):return [[rational(v)for v in row]for row in data['chebyshev_coefficients']]
def density_moment(coeff,alpha):
    a=sum(((-1)**j*v for j,v in enumerate(coeff[0])),F(0));K=sum(((-1)**k*sum(row,F(0))for k,row in enumerate(coeff)),F(0))
    def power(k):return chebyshev_in_sigma([(-1)**j*v for j,v in enumerate(coeff[k])])if k<len(coeff)else [F(0)]
    B1,B2=power(1),power(2)
    integ=sum((v/F(j+1)for j,v in enumerate(B1)),F(0))-sum((v/F(j+1)for j,v in enumerate(B2)),F(0))+sum((v/(j+1+1/alpha)for j,v in enumerate(B2)),F(0))
    return a,-a/4+integ/(4*alpha),K

def project(coeff,alpha,ell):
    coeff=copy.deepcopy(coeff);a,c,K=density_moment(coeff,alpha)
    v=4*alpha*(1-ell-c);u=(a-K+2*v)/2
    while len(coeff)<2:coeff.append([F(0),F(0)])
    for row in coeff[:2]:
        while len(row)<2:row.append(F(0))
    for i,w in [(0,u),(1,v)]:coeff[i][0]+=w;coeff[i][1]+=w
    assert density_moment(coeff,alpha)==(a,1-ell,a)
    return coeff,u,v

def manufactured():
    rng=random.Random(20261021);count=0
    for alpha in [F(1,7),F(1,4),F(3,10),F(2,5)]:
        for N in range(1,6):
            for M in range(1,6):
                C=[[F(rng.randint(-19,19),rng.randint(1,23))for j in range(N+1)]for k in range(M)]
                ell=F(1)/(1-2*alpha)
                a,c,K=density_moment(C,alpha);new,u,v=project(C,alpha,ell);twice,uu,vv=project(new,alpha,ell)
                assert twice==new and uu==vv==0;count+=4
                inp={'alpha':encoded(alpha),'length':encoded(F(1)),'cl':encoded(ell),'chebyshev_coefficients':[[encoded(z)for z in row]for row in C]}
                model=SmoothMP(inp,digits=35);assert model.a0==a and model.c==c;count+=2
                for k in range(len(C)):
                    for j in range(len(C[k])):
                        expected=u if k==0 and j<2 else v if k==1 and j<2 else F(0)
                        assert new[k][j]-C[k][j]==expected;count+=1
    return {'utc':utc(),'status':'PASS','exact_checks':count,'method':'Random rational arrays,100(alpha,N,M) cases; exact projection, idempotence, coefficient support, and independent source-tail versus density-moment strain.'}

def main():
    root=Path('research/exact_parameter_fields');folder=root/'verification';folder.mkdir(exist_ok=True)
    gate=Path('research/smooth_full_inverse_primitives/verification/manufactured.json')
    if not gate.exists():
        candidates=list((root.parent/'smooth_full_inverse_primitives/verification').glob('*.json'))
        gate=next(x for x in candidates if json.loads(x.read_text()).get('status')=='PASS')
    assert json.loads(gate.read_text())['status']=='PASS'
    result={'started_utc':utc(),'status':'RUNNING','proof_sha256':sha(root/'PROOF.md'),'code_sha256':sha(__file__),'primitive_gate':str(gate),'primitive_gate_sha256':sha(gate),'manufactured':manufactured(),'cases':[]}
    output=folder/'AUDIT.json'
    def checkpoint():result['updated_utc']=utc();save(output,result)
    checkpoint();print(json.dumps(result['manufactured']),flush=True)
    points=[[0,0],[0,1],[.1981136536202562,.5762572325117884],[.19825771173583176,.5762076860908608],[.00800986137674711,1.7256723212410504e-10],[.00309218611001119,3.09218611001119e-11],[6e11,8e11],[6e249,8e249]]
    for tag in ['common1000_moments_cl2.5_N36M32','common1000_moments_cl2.5_N40M36']:
        start=time.monotonic();oldpath=Path('evidence/smooth_exact_jets')/tag/'exact_input.json';old=json.loads(oldpath.read_text());assert sha(old['source'])==old['source_sha256']
        dest=folder/tag;dest.mkdir(exist_ok=True)
        A=copy.deepcopy(old);A['field']='A: literal saved binary formula';A['source_exact_input_sha256']=sha(oldpath)
        B=copy.deepcopy(A);B['field']='B: same coefficients, exact alpha=3/10';B['alpha']=encoded(F(3,10));B['scope']='This JSON defines a separate finite density with exact alpha3/10; exponent_stored is original provenance only, not used to define this new field.'
        C=copy.deepcopy(B);C['field']='C: exact alpha3/10, projected c=1-ell and K=a';co,u,v=project(numbers(B),F(3,10),F(5,2));C['chebyshev_coefficients']=[[encoded(x)for x in row]for row in co];C['scope']='This exact JSON defines a separate finite density with corrected coefficients. The source NPZ supplies only the starting coefficients. Its field is not silently reinterpreted.';C['projection']={'u':str(u),'v':str(v)}
        case={'tag':tag,'source_sha256':old['source_sha256'],'original_exact_input_sha256':sha(oldpath),'points':points,'fields':[]};result['cases'].append(case);checkpoint()
        for label,inp in [('A',A),('B',B),('C',C)]:
            fieldpath=dest/(label+'.exact.json');save(fieldpath,inp)
            coeff=numbers(inp);alpha=rational(inp['alpha']);a,c,K=density_moment(coeff,alpha)
            item={'label':label,'exact_input':str(fieldpath),'exact_input_sha256':sha(fieldpath),'a_exact':str(a),'c_exact':str(c),'K_exact':str(K),'center_defect_exact':str(F(5,2)+c-1),'K_minus_a_exact':str(K-a),'p_exact':str(1-2*alpha),'ell_p_minus_one_exact':str(F(5,2)*(1-2*alpha)-1),'precision_rows':[]}
            case['fields'].append(item);checkpoint()
            if label=='C':assert F(5,2)+c-1==K-a==0
            for digits in (75,110):
                model=SmoothMP(inp,digits=digits);assert model.c==c and model.a0==a
                row={'digits':digits,'points':[]};item['precision_rows'].append(row)
                for x,y in points:
                    tick=time.monotonic();fields=model.fields(x,y)
                    with mp.workdps(max(fields['working_digits'],digits+20)):
                        far=at_point(model,x,y)if mp.hypot(x,y)>1e6 else None
                        if far is not None:
                            rem=mp.mpf(fields['R'])-mp.mpf(far['R_two_terms']);r=mp.hypot(mp.mpf(x),mp.mpf(y));pp=mp.mpf(model.p.numerator)/model.p.denominator
                            far['remainder_over_r_3p_minus2']=mp.nstr(rem/r**(3*pp-2),digits)
                    row['points'].append({'field':fields,'far_comparison':far,'seconds':time.monotonic()-tick});checkpoint()
                print(json.dumps({'utc':utc(),'tag':tag,'field':label,'digits':digits,'center_defect':float(F(5,2)+c-1),'peak_Nf':row['points'][2]['field']['R_Nf'],'far_R':row['points'][-1]['field']['R']}),flush=True)
            with mp.workdps(130):
                comparisons=[]
                for aa,bb in zip(item['precision_rows'][0]['points'],item['precision_rows'][1]['points']):
                    arow,brow=aa['field'],bb['field'];errors={}
                    for key in ['rho','R','Nf','Nv','U1','U2','rho_x','rho_y','R_Nf','R_Nv']:
                        if arow[key]is not None:
                            av,bv=mp.mpf(arow[key]),mp.mpf(brow[key]);errors[key]=mp.nstr(abs(av-bv)/(1+abs(bv)),30)
                    comparisons.append(errors)
                item['precision_comparisons']=comparisons
            checkpoint()
        case['elapsed_seconds']=time.monotonic()-start;case['status']='COMPUTED';checkpoint()
    result['status']='COMPUTED';result['finished_utc']=utc();checkpoint()
if __name__=='__main__':main()
