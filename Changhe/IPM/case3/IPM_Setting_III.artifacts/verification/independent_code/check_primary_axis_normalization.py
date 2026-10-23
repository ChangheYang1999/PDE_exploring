from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_axis_normalization_closure';V=R/'verification';dest=V/'CHECKS.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('source '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
def number(d):return F(int(d['numerator']),int(d['denominator']))
def functionals(C):return sum((-1)**j*c for j,c in enumerate(C[0])),sum((-1)**k*c for k,row in enumerate(C)for c in row)
for c,a,k in [([[F(0),F(1)]],F(-1),F(1)),([[F(0)],[F(1)]],F(0),F(-1)),([[F(2),F(3)],[F(5),F(7)]],F(-1),F(-7))]:ck('manufacture '+str(c),functionals(c)==(a,k))
for p in [__file__,R/'PROOF.md',ROOT/'research/scaling/PROOF.md']:bind(p)
old=json.loads(bind(ROOT/'research/primary_common_mp_sample/verification/FINAL_BINDINGS.json','0750932980dcee8cd6b52aa57f053718f1e8143941a2d931e71358fd6e5f33db'));ck('334 accepted',old['status']=='CONFIRMED_FINITE_PRIMARY_COMMON_MP_SAMPLE'and all(x['passed']for x in old['checks']))
ref=json.loads(bind(ROOT/'research/primary_common_mp_sample/verification/CHECKS.json'));I=json.loads(bind(ROOT/'research/primary_fresh_sample/verification/INPUTS.json'));rows=[]
for ent in I['states']:
 d=json.loads(bind(ent['exact_input'],ent['exact_input_sha256']));C=[[number(x)for x in row]for row in d['chebyshev_coefficients']];alpha=number(d['alpha']);ell=number(d['cl']);L=number(d['length']);p=1-2*alpha;s=1/(1-p);a,K=functionals(C);r=K/a;delta=r-1;bound=F(101,50)*abs(delta);prior=next(z for z in ref['rows']if z['N']==ent['N'])
 ck('actual coefficients '+str(ent['N']),L==1 and ell==F(5,2)and alpha==F(5404319552844595,18014398509481984));ck('slope independently matches334 '+str(ent['N']),a==F(prior['a_exact']));ck('actual exponent matches334 '+str(ent['N']),p==F(prior['p_exact']));ck('chart positive '+str(ent['N']),a!=0 and K!=0 and r>0);ck('length bound hypotheses '+str(ent['N']),1<s<2 and abs(delta)<=F(1,100));ck('binary exponent defect '+str(ent['N']),ell*p-1==F(1,2**54))
 rows.append(dict(N=ent['N'],source_sha256=ent['source_sha256'],exact_input_sha256=ent['exact_input_sha256'],a_exact=str(a),K_exact=str(K),K_minus_a_exact=str(K-a),K_over_a_minus1_exact=str(delta),p_exact=str(p),ell_p_minus1_exact=str(ell*p-1),s_exact=str(s),L_axis_distance_from1_upper_bound_exact=str(bound),display=dict(a=float(a),K=float(K),K_minus_a=float(K-a),K_over_a_minus1=float(delta),L_axis_distance_from1_upper_bound=float(bound))))
for q,h in bindings.items():ck('final stable '+q,hashlib.sha256(Path(q).read_bytes()).hexdigest()==h)
out=dict(status='PASS_EXACT_PRIMARY_AXIS_NORMALIZATION_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,rows=rows,scope='Exact coefficient functionals and rigorous finite-formula length bound, not an IPM solution or a parameter uncertainty enclosure.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print(json.dumps([dict(N=x['N'],**x['display'])for x in rows],indent=2))
