"""Independent exact axis jet from immutable generator records; no peer execution."""
import hashlib,json,math,sys,time
from pathlib import Path
from datetime import datetime,timezone
from flint import fmpq
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[3]
TOP=Path(__file__).resolve().parents[1]
START=time.monotonic(); checks={}; inputs={}
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p,want=None):
    p=p.resolve();h=sha(p)
    if want is not None:assert h==want,(str(p),h,want)
    inputs[str(p.relative_to(BASE))]=h
    return p

def ck(k,v):
    assert k not in checks,k
    checks[k]=bool(v)
    assert v,k

def Q(x):return fmpq(str(x))
def conv(d):return {str(k):str(v) for k,v in sorted(d.items())}
proof=bind(TOP/'PROOF.md','f7ee0b3fe4410b18febf0a1626fddef765afec5723812cff965b126758cd1fc7')
bind(Path(__file__))
manifest=bind(TOP/'source/MANIFEST.json','23e287ff3b0658ecebc17290c2749b1d598d3c6379db72953e2d7b88fcdf30d4')
for name,r in json.loads(manifest.read_text()).items():bind(TOP/'source'/name,r['sha256'])
first=json.loads(bind(TOP/'verification/PROOF_FIRST.json').read_text())
ck('proof_precedes_code',first['proof_sha256']==sha(proof) and first['checker_exists'] is False)
raw=bind(BASE/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json','ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21')
old=json.loads(bind(BASE/'research/candidate_audits/verification/C1-N1-007-d2w-j7-e2bal.json','2c0f1e9206c1da0781acc49566b5114614b2afa870fd7105301acbeac619ed96').read_text())
d=json.loads(raw.read_text());c=Q(d['cl_exact']);gamma=1/c
ck('exact_c',c==Q('4076476460239181/2251799813685248'))
ck('old_same_candidate',old['candidate']=='C1-N1-007-d2w-j7-e2bal')
ck('old_same_generator',old['generator_sha256']==sha(raw))
ck('old_structural_claims',old['snapshot_hashes_confirmed'] and old['all_forbidden_zero'])
A={i:Q(0) for i in range(5)};B={i:Q(0) for i in range(4)}
used=[];summands=0
for index,g in enumerate(d['generators']):
    m=g['m'];j=g['j'];spec=g['spec'];w=spec[1]
    ck(f'generator_schema_{index}',isinstance(m,int) and m>=0 and isinstance(j,int) and j>=0 and isinstance(w,int) and w>=0 and spec[0] in ['leg','mono'])
    if m+w>4:continue
    a=Q(g['coef']);p=(3+gamma-j*(1-gamma))/2
    if spec[0]=='leg':
        n=spec[2];ck(f'leg_degree_{index}',isinstance(n,int) and n>=0)
        stripes=[(w+h,(-1)**(n-h)*math.comb(n,h)*math.comb(n+h,h)) for h in range(min(n,4-m-w)+1)]
    else:stripes=[(w,1)]
    used.append(index)
    for power,leg in stripes:
        binomial=Q(1)
        for ell in range(5-m-power):
            if ell:binomial*= (p-m-power-ell+1)/ell
            s=power+ell;deg=m+s;v=a*leg*binomial*((-1)**m)
            A[deg]+=v
            if deg:B[deg-1]+=(s-m*(2*m-1))*v
            summands+=1
r={};u={}
for j in [1,3,5]:
    r[j]=-(j+3)*(j+2)*(j+1)*A[(j+3)//2]-2*(j+1)*B[(j+1)//2]
    u[j]=2*(j+1)*B[(j+1)//2]
F={k:(c*k-1)*r[k]+sum((u[p]*q*r[q] for p in u for q in r if p+q-1==k),Q(0)) for k in [1,3,5]}
ck('axis_density_matches_structural_a0',r[1]==Q(old['a0_exact']))
ck('exact_constant_Rf_zero',F[1]==0)
ck('quartic_Rf_above_20899e15',F[5]>Q('20899/1000000000000000'))
ck('quartic_Rf_below_20900e15',F[5]<Q('20900/1000000000000000'))
ck('quartic_exceeds_uniform_2e13',F[5]>Q('1/5000000000000'))
report=(TOP/'source/report.md').read_text().splitlines()
ck('frozen_claim_line54',('five Taylor equations' in report[53]) and ('2e-13' in report[53]))
for key,h in inputs.items():ck('stable_'+key,sha(BASE/key)==h)
res={'utc':utc(),'scope':'Exact candidate007 axis Taylor coefficients; refutes only saved-candidate universal 2e-13 tolerance. No new PDE existence claim.', 'candidate':old['candidate'],'inputs':inputs,'checks':checks,'check_count':len(checks),'generator_count':len(d['generators']),'used_generator_indices':used,'finite_summand_count':summands,'c_exact':str(c),'chi_axis_A_exact':conv(A),'chi_x2_B_exact':conv(B),'rho_axis_exact':conv(r),'uy_axis_exact':conv(u),'F_axis_exact':conv(F),'Rf_y4_lower_exact':'20899/1000000000000000','Rf_y4_upper_exact':'20900/1000000000000000','Rf_y4_float_diagnostic':float(F[5]),'verdicts':{'exact_axis_statement':'CONFIRMED','universal_saved_tolerance_2e13':'REFUTED'},'elapsed_seconds':time.monotonic()-START}
out=TOP/'verification/result.json';assert not out.exists();out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'utc':res['utc'],'checks':len(checks),'used_generators':len(used),'summands':summands,'Rf_y4_float':float(F[5]),'sha256':sha(out),'elapsed_seconds':res['elapsed_seconds']}))
