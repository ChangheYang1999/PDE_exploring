from pathlib import Path
from fractions import Fraction as F
from flint import fmpq
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_archive_dependencies';E=D/'evidence'
now=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
load=lambda p:json.loads(p.read_text())
start=now();pins={}
def read(n):
 p=B/n;pins[n]=sha(p);return load(p)
s=read('research/modal_source/evidence/source_result.json');c=read('research/source_instance/evidence/checks_v2.json');j=read('research/source_jet_corrections/evidence/checks.json')
i=s['initial_root_proof'][0];a,b=F(i['a_exact']),F(i['b_exact']);l,h=map(F,c['source_bracket_exact']);p,q=map(F,s['final_root_endpoints_exact'])
assert a<l<p<q<h<b
assert F(i['w_a']['upper_exact'])<0<F(i['w_b']['lower_exact']) and F(i['wprime_on_box']['lower_exact'])>0
margin=F(j['exact_ranges']['D']['lower_exact'])-F('6.70197e-7')
assert F('8.97547e-13')<margin<F('8.97548e-13')
Q=lambda x:fmpq(str(x))
assert Q(a)<Q(l)<Q(p)<Q(q)<Q(h)<Q(b)
assert Q(i['w_a']['upper_exact'])<0<Q(i['w_b']['lower_exact']) and Q(i['wprime_on_box']['lower_exact'])>0
margin2=Q(j['exact_ranges']['D']['lower_exact'])-fmpq(670197,10**12)
assert margin2==Q(margin) and fmpq(897547,10**18)<margin2<fmpq(897548,10**18)
for path in [Path(__file__),D/'REVIEW_RESOLUTION.md']:pins[str(path.relative_to(B))]=sha(path)
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_INITIAL_BRACKET_UNIQUENESS_AND_D_MARGIN_COMPARISONS','nested_brackets_exact':list(map(str,[a,l,p,q,h,b])),'initial_derivative_lower_exact':i['wprime_on_box']['lower_exact'],'strict_coarse_in_initial_margins':[str(l-a),str(b-h)],'D_margin_exact':str(margin),'D_margin_strict_interval':['8.97547e-13','8.97548e-13'],'methods':['Fraction exact comparisons','fmpq exact comparisons, integer rational decimal constants'],'scope':'Saved independent25 derivative certificate covers coarse89 bracket. Root identification uses same canonical drift plus uniqueness; no new field evaluation.','files':pins}
with (E/'resolution_checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','strict_coarse_in_initial_margins','D_margin_strict_interval']}))
