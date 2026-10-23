"""Additional exact leading-coefficient and finite-provenance checks for result289."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,math,sys
import gmpy2
sys.set_int_max_str_digits(0)
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';checks=[];bindings={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);v=sha(p);ck('binding '+str(p),h is None or v==h);bindings[str(p)]=v
q=lambda s:gmpy2.mpq(str(s))
def smallq(s):
 x=Fraction(s);return gmpy2.mpq(x.numerator,x.denominator)
def reportq(x):return dict(float=float(x),numerator_bits=int(x.numerator.bit_length()),denominator_bits=int(x.denominator.bit_length()),rational_sha256=hashlib.sha256(str(x).encode()).hexdigest())
for p in [Path(__file__),R/'RESULTS_REVIEW_RESOLUTION_PROOF.md',R/'RESULTS_SUPPLEMENT_RANGE_CORRECTION_PROOF.md',V/'PIPELINE.json',V/'SUMMARY.json',V/'hsG_c2.0_N224_log.json']:bind(p)
s=json.loads((V/'SUMMARY.json').read_text());a=json.loads((V/'hsG_c2.0_N224_log.json').read_text());pipe=json.loads((V/'PIPELINE.json').read_text());poly=V/'hsG_c2.0_N224_log.polynomials.json';bind(poly,a['polynomial_sha256']);bind(V/'PIPELINE.json',s['pipeline_sha256'])
ck('summary150passed',s['status']=='PASS' and s['count']==150==len(s['checks'])and all(t['passed']for t in s['checks']));ck('pipeline76passed',pipe['status']=='DONE'and len(pipe['checks'])==76 and all(t['passed']for t in pipe['checks']))
cert=json.loads(poly.read_text());ck('map exact L1 P2',cert['L']==['1','1']and cert['P']==['2','1']);conv=lambda v:gmpy2.mpq(v[0]+'/'+v[1]);H=[conv(t)for t in cert['H_w'][:4]];k=[conv(t)for t in cert['k_w'][:3]];ck('zero polynomial constants',H[0]==k[0]==0);K=H[1]/2;Q=k[1]/4;c2=(H[2]-H[1]/4)/4;c3=(H[3]-H[2]/2-H[1]/32)/8;B=(k[2]-k[1]/4)/4;r2=-c2+2*K*Q
exact=dict(K=K,Q=Q,c2=c2,c3=c3,B_log=B,r2=r2,residual_sqrt=r2/(2*K),residual_log=B/4)
for n,x in exact.items():
 target=smallq(s['states'][0]['far']['values'][n]);ck('exact leading coefficient agrees '+n,abs(x-target)<smallq('1e-70')*max(1,abs(x)),reportq(x))
ck('positive exact K',K>0);ck('positive exact B_log',B>0);ck('negative nonzero exact r2',r2<0);ck('exact r2 decimal interval',smallq('-.2895093241807790')<r2<smallq('-.2895093241807789'));ck('exact B decimal interval',smallq('247.9285695902469')<B<smallq('247.9285695902470'))
a0=q(a['exact']['a']);ch=q(a['exact']['cH']);delta=q(a['exact']['delta']);ck('exact delta identity',delta==1+ch);ck('center parameter range',a0>0 and -1<delta<0);ck('a not exactly1',a0!=1);ratio=abs(delta)/(2+delta);state=s['states'][0];ck('center ratio independent arithmetic',abs(float(ratio)-state['origin_axis_R_Nf_limit'])<1e-19);ck('center ratio not half delta',ratio!=abs(delta)/2);ck('correct drift signs',max(abs(float(t)-v)for t,v in zip([3-delta,1+delta],state['origin_drift_diagonal']))<1e-15)
exact.update(a=a0,delta=delta,axis_center_ratio=ratio)
rules=[(z['order'],z['tail_order'],z['split'])for z in a['levels']];ck('declared physical rules',rules==[(32,96,16.),(48,160,64.),(64,192,128.)]);ck('774points each',all(len(z['points'])==774 for z in a['levels']));w=a['witnesses'];ck('witness rule',(w['order'],w['tail_order'],w['split'])==(88,256,512.));ws={(t['x'],t['y'])for t in w['points']};main={(t['x'],t['y'])for t in a['levels'][-1]['points']};ck('14distinct witnesses and13shared',len(w['points'])==len(ws)==14 and len(ws&main)==13)
mapping=[]
for lev in a['levels']:
 for region,data in lev['regions'].items():
  for metric in ['R','R_Nf','R_Nv']:
   point=data[metric];xy=(point['x'],point['y']);ck('witness contains maximizer '+str(lev['order'])+' '+region+' '+metric,xy in ws);mapping.append(dict(order=lev['order'],region=region,metric=metric,point=list(xy)))
ck('two axis working precisions',[z['working_digits']for z in a['axis_log_runs']]==[270,315]);ck('summary uses final axis series',state['axis_points']==a['axis_log_runs'][-1]['points']);ck('axis radii to1e28',[t['y']for t in state['axis_points']]==['100.0','1000.0','10000.0','1000000.0','100000000.0','1000000000000.0','100000000000000000000.0','10000000000000000000000000000.0'])
ck('local MP target digits',sorted(set(z['target_digits']for z in a['mp_jet_checks']))==[70,100]);working=sorted(set((z['target_digits'],z['working_digits'])for z in a['mp_jet_checks']));ck('local MP working guard',all(b>a for a,b in working));ck('axis bottom minimum at sampled endpoint',a['axis_derivative_samples']['argmin_gy_xaxis']==a['axis_derivative_samples']['range'][1]==1e6)
regions=dict(tiny=[0,.01],inner=[.01,.1],core=[.1,1],annulus=[1,100],far=[100,math.inf],extent10=[0,10],extent100=[0,100],extent10000=[0,10000.000001])
# Extent definitions are verified directly against stored selected point counts and maxima.
for name,(lo,hi)in regions.items():
 pts=[t for t in a['levels'][-1]['points']if lo<=math.hypot(t['x'],t['y'])<hi]
 ck('regional membership count '+name,len(pts)==state['final_regions'][name]['count'],dict(count=len(pts)))
 for metric in ['R','R_Nf','R_Nv']:
  vals=[abs(t[metric])for t in pts if t[metric]is not None];ck('regional maximum '+name+' '+metric,max(vals)==abs(state['final_regions'][name][metric][metric]))
h=json.loads((V/'HANDOFF.json').read_text());step=h['stages'][0];bind(V/'HANDOFF.json');ck('successful summary stage',step['stage']=='summary'and step['status']=='PASS'and step['returncode']==0);bind(V/'SUMMARY.json',step['output_sha256']);elapsed=(datetime.fromisoformat(step['finished_utc'])-datetime.fromisoformat(step['started_utc'])).total_seconds();ck('summary longer than timeout',60<elapsed<100)
reviews=[]
for folder in ['opus_results_shift7_archive','opus_results']:
 for name in ['request.txt','response.json','answer.md','metadata.json']:bind(V/folder/name)
 meta=json.loads((V/folder/'metadata.json').read_text());response=json.loads((V/folder/'response.json').read_text());ck('actual requested Opus5.5 '+folder,meta['requested_model']=='us.anthropic.claude-opus-5-5');ck('actual returned Opus5.5 '+folder,response['model']=='claude-opus-5-5');reviews.append(dict(folder=folder,metadata=meta,returned_model=response['model']))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_FINITE_RESULTS_SUPPLEMENT',count=len(checks),checks=checks,bindings=bindings,exact={n:reportq(x)for n,x in exact.items()},witness_mapping=mapping,local_MP_precisions=working,axis_MP_precisions=[270,315],summary_elapsed_seconds=elapsed,reviews=reviews,scope='Exact leading-coefficient and center arithmetic; finite witnesses and presentation. True inverse error and principal full-plane endpoint remain OPEN.')
(V/'RESULTS_SUPPLEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
