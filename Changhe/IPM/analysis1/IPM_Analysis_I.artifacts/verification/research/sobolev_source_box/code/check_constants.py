"""Two independent enclosures plus source identity and dependency verification."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
import hashlib,json,sys,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/sobolev_source_box';E=D/'evidence'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for z in iter(lambda:f.read(1<<20),b''):h.update(z)
    return h.hexdigest()
def load(p):return json.loads(p.read_text())
params=load(D/'source/parameters.json');p={k:F(v) for k,v in params['inputs'].items()};counts=Counter();files={};visited=set()
def check_dep(path,digest):
    assert sha(B/path)==digest,path;counts['dependency_hash_comparisons']+=1
    if path in visited:return
    visited.add(path)
    if path.endswith('/evidence/verdict.json'):
        verdict=load(B/path);assert verdict['status'].startswith('CONFIRMED'),path
        for name,h in verdict['files'].items():check_dep(name,h)
for path,digest in params['dependencies'].items():check_dep(path,digest);files[path]=digest
assert load(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')
source=load(B/'research/modal_source/evidence/source_result.json')
audit=load(B/'research/modal_source/evidence/output_audit.json')
assert audit['verdict']=='PASS' and audit['source_result_sha256']==sha(B/'research/modal_source/evidence/source_result.json')
lo,hi=map(F,source['final_root_endpoints_exact'])
assert p['p_lower']<lo<=hi<p['p_upper'];counts['source_bracket']=1
v=source['final_values'];mu_lo,mu_hi=F(v['mu_minus_1']['lower_exact']),F(v['mu_minus_1']['upper_exact'])
g_lo,g_hi=F(v['g']['lower_exact']),F(v['g']['upper_exact'])
modal=load(B/'data_exact/modal_v2.json')
k=F(float.fromhex(modal['scalars_hex']['k']))
Alo,Ahi=2/k-1-mu_hi,2/k-1-mu_lo
assert p['A_lower']<Alo<=Ahi<p['A_upper']
assert -p['defect_center']-p['defect_error']<mu_lo<=mu_hi<-p['defect_center']+p['defect_error']
assert p['g_center']-p['g_error']<g_lo<=g_hi<p['g_center']+p['g_error'];counts['imported_scalar_rounding']=3
assert p['A_lower']-p['MV']*p['R0']>p['m0']>0
assert F('8.6')<p['p_lower']<p['p_upper']<F('8.60006381')
assert p['p_upper']+p['R0']<p['xmax']
assert 0<p['R']<p['R0'] and p['p_lower']-p['R0']>F('8.55')
assert p['R0']<(p['p_lower']-p['R0'])/2 and p['delta_max']<1
assert p['delta_max']==p['R0']/3;counts['geometry_and_m_lower']=6

# Closed-ball regularity in a larger open neighbourhood. No Hessian
# estimate is extrapolated from the original disc to this neighbourhood.
knots=[F(float.fromhex(x)) for x in modal['arrays']['knots']['hex']]
assert len(knots)==1573 and knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8
assert all(a<b for a,b in zip(knots[7:-8],knots[8:-7]))
assert len(set(knots[8:-8]))==1557
assert knots[7]<1<3<knots[-8];counts['exact_simple_interior_knots']=1557
assert p['p_lower']-p['R']-p['regularity_radius']>8
assert p['p_upper']+p['R']+p['regularity_radius']<9
assert p['R0']<p['regularity_radius'] and p['H_exclusion']<p['H'];counts['closed_ball_neighbourhood_checks']=4
# e < 1+1+sum_{j>=1}2^-j=3, strictly because n!>2^(n-1)
# for n>=3; e^3>sum_{j=0}^3 3^j/j!=13. Thus log[8,9] is in (1,3).
assert sum((F(3)**j/F(math.factorial(j)) for j in range(4)),F())==13
assert all(math.factorial(n)>2**(n-1) for n in range(3,12));counts['elementary_exp_diagnostics']=10
low=load(B/'research/n8_coefficient_closure/evidence/checks.json')['exact']
assert p['MV']==F(low['M_V_upper']) and p['Mrho']==F(low['M_rho_upper']) and p['delta_max']==F(low['delta'])
instance=load(B/'research/source_instance/evidence/checks_v2.json')
assert F(instance['cl_exact'])==1/k and list(map(F,instance['source_bracket_exact']))==[p['p_lower'],p['p_upper']]
counts['direct_imported_numeric_links']=5

for margin,want in [(F('0.01')+mu_lo,p['box1']),(F('0.01')-mu_hi,p['box1']),(Alo-10,p['box2']),(F('10.2')-Ahi,p['box2']),(g_lo-29,p['box3']),(30-g_hi,p['box3'])]:assert margin>want;counts['source_box_margins']+=1
assert p['defect_lower']<-mu_hi and F(params['upper_claims']['exclusion_lhs'])<p['defect_lower'];counts['nonstationarity_gap']=2
# Angular averages are checked by the integral recurrence, independently
# of the factorial expression used by the rational numerical engine.
A={(0,0):F(1)}
for n in range(1,7):
    A[n,0]=F(2*n-1,2*n)*A[n-1,0]
    for b in range(1,n+1):
        a=n-b;A[a,b]=A[a,b-1]-A[a+1,b-1]
for (a,b),v in A.items():
    expected=F(math.factorial(2*a)*math.factorial(2*b),4**(a+b)*math.factorial(a)*math.factorial(b)*math.factorial(a+b))
    assert v==expected;counts['exact_angular_recurrence_checks']+=1
for s in (F(153,50),F(61,20),F(31,10)):
    for j in range(3):
        integral=sum((F((-1)**(j-l)*math.comb(j,l))/(s-l-1) for l in range(j+1)),F())
        product=F(math.factorial(j))
        for l in range(j+1):product/=s-1-l
        assert integral==product;counts['exact_radial_identity_checks']+=1
from engine_arb import evaluate as arb_eval
from engine_rational import evaluate as rational_eval
engines={'arb384':arb_eval(params),'rational_machin_isqrt':rational_eval(params)}
for name,vals in engines.items():
    def ends(key):return tuple(F(vals[key][part]) for part in ('lower_exact','upper_exact'))
    for key in vals:
        a,b=ends(key);assert 0<a<=b,(name,key);counts[name+'_positive_enclosures']+=1
    for key,target in params['upper_claims'].items():assert ends(key)[1]<F(target),(name,key,vals[key]);counts[name+'_strict_upper']+=1
    for key,target in params['lower_claims'].items():assert ends(key)[0]>F(target),(name,key,vals[key]);counts[name+'_strict_lower']+=1
    for i in (1,2,3):assert ends('B'+str(i))[1]<p['box'+str(i)];counts[name+'_box_implications']+=1
    assert ends('e0')[1]<ends('mR_lower')[0] and ends('e1')[1]<p['m0'];counts[name+'_motion_implications']+=2
    assert ends('E')[1]<ends('kappa')[0]
    if name=='rational_machin_isqrt':assert ends('kappa')==(F('3.4144'),F('3.4144'))
    assert ends('exclusion_e3')[1]<29 and ends('exclusion_gradient_lower')[0]>0;counts[name+'_nonzero_source_gradient']=2
    assert ends('exclusion_lhs')[1]<p['defect_lower'] and ends('exclusion_radius')[0]>p['H_exclusion'];counts[name+'_exclusion_gap']=2
# h=0 is an exact counterexample to the lead's strict delta_h<delta_max.
assert (p['R0']-0)/3==p['delta_max'];counts['strict_delta_counterexample']=1
# Independent intervals should overlap; this is only a consistency check.
for key in engines['arb384']:
    a,b=(F(engines['arb384'][key][x]) for x in ('lower_exact','upper_exact'))
    c,d=(F(engines['rational_machin_isqrt'][key][x]) for x in ('lower_exact','upper_exact'))
    assert max(a,c)<=min(b,d),key;counts['cross_engine_overlap_diagnostics']+=1
for path in [D/'PROOF.md',D/'ADDENDUM.md',D/'PUBLICATION.md',D/'CLOSURE_NOTES.md',E/'proof_first.json',D/'source/parameters.json',D/'source/lead_r3.md',D/'source/lead_code.py',B/'data_exact/modal_v2.json',B/'research/modal_source/evidence/source_result.json',B/'research/modal_source/evidence/output_audit.json',B/'research/n8_coefficient_closure/evidence/checks.json',B/'research/source_instance/evidence/checks_v2.json']+sorted((D/'code').glob('*.py')):files[str(path.relative_to(B))]=sha(path)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_INDEPENDENT_SOURCE_BOX_ENCLOSURES','counts':dict(counts),'engines':engines,'source_exact':{'k':str(k),'A_lower':str(Alo),'A_upper':str(Ahi),'mu_minus_1_lower':str(mu_lo),'mu_minus_1_upper':str(mu_hi),'g_lower':str(g_lo),'g_upper':str(g_hi)},'files':files,'scope':'Independent scalar and source/provenance verification for PROOF.md. K1-only local uniformity and narrow trial nonstationarity. No global inverse or X3 exclusion.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('engines','source_exact','files')}))
