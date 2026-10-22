"""Independent Fraction saved-output and source-Newton audit, no engine import."""
import os,sys
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
from datetime import datetime,timezone
import json,hashlib,gzip,bisect,time,importlib.util,re,resource
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_archive_second';E=D/'evidence'
def need(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def unique(items):
 out={}
 for k,v in items:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def parse(s):return json.loads(s,object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def load(p):return parse(Path(p).read_text())
def write(p,v):
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()+b'\n'
def main():
 start=now();tick=time.monotonic();pre=load(E/'preflight_manifest.json');need(pre['status']=='ACCEPTED_PREPARATION_ONLY','preparation status')
 for n,h in pre['files'].items():need(sha(B/n)==h,'frozen preparation input '+n)
 spec=importlib.util.spec_from_file_location('accepted_newton_audit',B/'research/full_t_linkage/code/audit_coefficients.py');api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
 summary=load(E/'full_summary.json');stream=E/'full_spans.jsonl';need(summary['status']=='COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT' and summary['output_sha256']==sha(stream) and summary['preflight_sha256']==sha(E/'preflight_manifest.json') and summary['producer_sha256']==sha(D/'code/full.py') and summary['engine_sha256']==sha(D/'code/engine.py'),'actual complete producer binding');lines=stream.read_bytes().splitlines(keepends=True);need(len(lines)==3118 and all(v.endswith(b'\n') for v in lines),'all full rows');head=parse(lines[0]);foot=parse(lines[-1]);forward=[parse(v) for v in lines[1:1559]];backward=[parse(v) for v in lines[1559:-1]];counts={'H':3265568,'I':406638,'J':406638,'I_steps':406638,'J_steps':406638};need(head['type']=='header' and head['schema']=='ipm-canonical-second-v1' and head['full_run'] is True and head['spans']==1558 and head['modes']==261 and head['iv_dps']==200 and head['anchor_checks']==3915,'complete header');need(foot['type']=='complete' and foot['counts']==summary['counts']==counts and foot['prefix_sha256']==hashlib.sha256(b''.join(lines[:-1])).hexdigest(),'complete counters/footer');need(summary['archive_footer_read'] is True and summary['exact_anchor_checks']==3915 and summary['iv_dps']==200,'complete summary flags');times=[head['utc']]+[r['utc'] for r in forward+backward]+[foot['utc'],summary['utc'],start];need(all(datetime.fromisoformat(a)<datetime.fromisoformat(b) for a,b in zip(times,times[1:])),'strict full stream chronology');need(datetime.fromisoformat(summary['start_utc'])<datetime.fromisoformat(head['utc']),'fresh start before header')
 raw=load(B/'data_exact/modal_v2.json');need(head['source_sha256']==sha(B/'data_exact/modal_v2.json')==api.TRIAL_SHA and head['archive_sha256']==sha(B/'research/middle_residual/evidence/original_knots.jsonl.gz')==api.ARCHIVE_SHA and head['normalization_sha256']==sha(B/'research/modal_repair/evidence/independent_gauss_iv.json') and head['preflight_sha256']==sha(E/'preflight_manifest.json'),'full source identity');need(raw['degree']==7,'degree7');t=list(map(api.exact_hex,raw['arrays']['knots']['hex']));knots=sorted(set(t));need(len(t)==1573 and len(knots)==1559,'exact knot count');S=list(map(api.exact_hex,raw['arrays']['S']['hex']));need(len(S)==260*1565,'all original S');sc={k:api.exact_hex(v) for k,v in raw['scalars_hex'].items()};W=[{} for _ in range(262)]
 for m in range(260):
  for freq in [1+2*m,1-2*m,3+2*m,3-2*m]:
   j=(abs(freq)-1)//2;W[j][m]=W[j].get(m,Q(0))+Q(1 if freq>0 else -1,8)
 W=[{m:v for m,v in w.items() if v} for w in W]
 def poly(si,j,basis=None):
  a,b=knots[si:si+2];h=b-a;ell=bisect.bisect_right(t,a)-1
  if basis is None:basis=[api.recursive_basis(t,ell,a+h*Q(k+1,9)) for k in range(8)]
  control=[sum((v*S[m*1565+i] for m,v in W[j].items()),Q(0)) for i in range(ell-7,ell+1)];values=[sum((v*c for v,c in zip(row,control,strict=True)),Q(0)) for row in basis];return api.newton_coefficients(values,Q(-1),Q(9))
 backward_by_span={r['span']:r for r in backward};need([r['span'] for r in forward]==list(range(1558)) and [r['span'] for r in backward]==list(reversed(range(1558))) and len(backward_by_span)==1558,'both exact span orders');saved_checks=0;selected_H_checks=0;zero_target_checks=0;newton_digest=hashlib.sha256();minimum={}
 def moment_records(row,targets,family,si):
  nonlocal saved_checks,zero_target_checks
  need(row['comparisons']==261 and re.fullmatch('[0-9a-f]{64}',row['state_sha256']) is not None,'all moment count/state digest');need([v['mode'] for v in row['samples']]==[1,2,3,261],'exact mandatory sample');seen={}
  for value in [row['worst']]+row['samples']:
   n=value['mode'];need(type(n) is int and 1<=n<=261 and value['family']==family and value['span']==si,'saved moment identity');target=api.archive_interval(targets[n-1]);lo,hi=map(Q,value['candidate']);need(tuple(map(Q,value['target']))==target and target[0]<=lo<=hi<=target[1],'saved candidate contained in actual target');saved_checks+=1;zero_target_checks+=target[0]==target[1]
   simple={k:v for k,v in value.items() if k!='relative_margin'}
   if n in seen:need(seen[n]==simple,'same candidate in repeated saved record')
   seen[n]=simple
  worst=row['worst'];a,b=map(Q,worst['target']);lo,hi=map(Q,worst['candidate']);need(a<b and Q(worst['relative_margin'])==min(lo-a,b-hi)/(b-a)>=0,'exact saved relative margin');minimum[family]=min(minimum.get(family,Q(worst['relative_margin'])),Q(worst['relative_margin']))
 with gzip.open(B/'research/middle_residual/evidence/original_knots.jsonl.gz','rt') as f:
  ah=parse(next(f));need(ah['spans']==1558 and ah['cells']==7809 and ah['hashes']['input']==head['source_sha256'] and ah['hashes']['normalization']==head['normalization_sha256'],'archive header')
  for si in range(1558):
   line=next(f);ar=parse(line);fr=forward[si];br=backward_by_span[si];a,b=knots[si:si+2];need(ar['type']=='span' and ar['span']==si and fr['type']=='forward' and br['type']=='backward' and fr['H_count']==2096 and fr['archive_line_sha256']==hashlib.sha256(line.encode()).hexdigest(),'actual archive row/full H count');need(all(Q(r['a_exact'])==a and Q(r['b_exact'])==b for r in [ar,fr,br]) and Q(ar['polynomial_mid_exact'])==(a+b)/2,'all exact geometry');need(len(ar['i_left'])==len(ar['j_right'])==261 and len(ar['density_polynomials'])==262 and all(len(x)==8 for x in ar['density_polynomials']),'all archive shapes');moment_records(fr,ar['i_left'],'I',si);moment_records(br,ar['j_right'],'J',si)
   for value in [fr['worst_H'],fr['selected_H']]:
    j,power=value['mode'],value['power'];need(0<=j<262 and 0<=power<8,'H index');target=api.archive_interval(ar['density_polynomials'][j][power]);exact=Q(value['exact']);need(tuple(map(Q,value['target']))==target and target[0]<=exact<=target[1],'saved H exact target');
    if 'margin' in value:need(Q(value['margin'])==min(exact-target[0],target[1]-exact),'saved H margin')
   v=fr['selected_H'];hj=int.from_bytes(hashlib.sha256((api.TRIAL_SHA+':H:'+str(si)).encode()).digest()[:4],'big')%261;power=si%8;need(v['mode']==hj and v['power']==power,'predetermined H selection');P=poly(si,hj);exact=sum((P[k]*comb(k,power)*Q(1,2)**(k-power) for k in range(power,8)),Q(0))/(b-a)**power;need(exact==Q(v['exact']),'independent Newton H coefficient');newton_digest.update(canonical([si,hj,power,str(exact)]));selected_H_checks+=1
  af=parse(next(f));need(af['type']=='complete' and af['spans']==1558 and af['cells']==7809 and not f.read(),'actual complete archive footer')
 # Independent exact endpoint jets and triangular correction, all tail modes.
 endpoint=[]
 for si,right in [(0,False),(1557,True)]:
  a,b=knots[si:si+2];h=b-a;ell=bisect.bisect_right(t,a)-1;basis=[api.recursive_basis(t,ell,a+h*Q(k+1,9)) for k in range(8)];rows=[]
  for j in range(262):
   P=poly(si,j,basis);rows.append([sum((P[k]*Q(factorial(k),factorial(k-v)) for k in range(v,8)),Q(0))/h**v if right else P[v]*factorial(v)/h**v for v in range(7)])
  endpoint.append(rows)
 def angular(name,width):
  a=list(map(api.exact_hex,raw['arrays'][name]['hex']));need(len(a)==260*width,'complete tail input');return [[sum((v*a[m*width+i] for m,v in w.items()),Q(0)) for i in range(width)] for w in W]
 hd=angular('D',7);ha=angular('Aout',10);alpha=[sc['k']-3-j*(1-sc['k'])-2*l for j,l in raw['outer_jl']];bi,bo=sc['bi'],sc['bo'];need(len(alpha)==10 and raw['outer_jl'][0]==[0,0],'outer exponents');anchors={'I0_exact':[],'U0_exact':[],'V0_exact':[]}
 def correction(g,beta):
  out=[]
  for v in range(7):out.append((g[v]-sum((comb(v,l)*factorial(l)*out[l]*beta**(v-l) for l in range(v)),Q(0)))/factorial(v))
  return out
 for n in range(1,262):
  m=2*n;C=W[n-1].get(0,Q(0));g=[endpoint[0][n-1][v]-(C if v==0 else 0)-sum((hd[n-1][l]*(2*l+2)**v for l in range(7)),Q(0)) for v in range(7)];e=correction(g,bi);I=C/(m+4)+sum((hd[n-1][l]/(m+6+2*l)+e[l]*(-1)**l*factorial(l)/(m+4+bi)**(l+1) for l in range(7)),Q(0));g=[endpoint[1][n][v]-sum((ha[n][l]*alpha[l]**v for l in range(10)),Q(0)) for v in range(7)];e=correction(g,-bo);need(m+4+bi>0 and m-4+bo>0 and all(m-4-x>0 for x in alpha),'every positive integration denominator');U=sum((ha[n][l]/(m-4-alpha[l]) for l in range(10)),Q(0))+sum((e[l]*factorial(l)/(m-4+bo)**(l+1) for l in range(7)),Q(0));C=W[n].get(0,Q(0));V=C*(alpha[0]+bo)**7/((m-4-alpha[0])*(m-4+bo)**7)
  for key,value in [('I0_exact',I),('U0_exact',U),('V0_exact',V)]:anchors[key].append(str(value))
 for key,values in anchors.items():need(values==head[key],'all exact independent anchors '+key)
 z=load(B/'research/modal_repair/evidence/independent_gauss_iv.json')['values']['A00_correction'];need(head['Z_exact']==[z['lower_exact_dyadic'],z['upper_exact_dyadic']],'same accepted normalization interval');need(saved_checks==15580 and selected_H_checks==1558,'complete saved audit counts')
 for n,h in pre['files'].items():need(sha(B/n)==h,'immutable preparation after audit')
 out={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_ARCHIVE_SAVED_OUTPUT_AND_INDEPENDENT_NEWTON_ANCHOR_AUDIT','counts':counts,'saved_moment_checks':saved_checks,'saved_zero_target_checks':zero_target_checks,'selected_H_Newton_checks':selected_H_checks,'independent_exact_anchors':783,'newton_values_sha256':newton_digest.hexdigest(),'smallest_saved_relative_margins':{k:str(v) for k,v in minimum.items()},'archive_footer_read':True,'output_sha256':sha(stream),'summary_sha256':sha(E/'full_summary.json'),'preflight_sha256':sha(E/'preflight_manifest.json'),'auditor_sha256':sha(Path(__file__)),'source_Newton_auditor_sha256':sha(B/'research/full_t_linkage/code/audit_coefficients.py'),'seconds':time.monotonic()-tick,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'All saved moment witnesses, complete coverage/input/chronology scan, third exact H coefficient per span and all analytic anchors. Does not recompute discarded complete moment candidates; those require the reviewed executed full second propagation.'};write(E/'full_output_audit.json',out);print(json.dumps(out),flush=True)
if __name__=='__main__':main()
