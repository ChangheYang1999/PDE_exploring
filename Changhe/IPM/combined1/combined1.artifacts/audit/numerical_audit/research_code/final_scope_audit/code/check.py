from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,time
from flint import arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/final_scope_audit';sha=lambda p:sha256(p.read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def main():
 start=time.monotonic();ctx.prec=1024;target=B/'verification/result_v01.json';assert not target.exists();inputs={};checks={}
 def read(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h;inputs[str(p.relative_to(R))]=v;return json.loads(p.read_text())
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(str(p),v,h);inputs[str(p.relative_to(R))]=v
 prep=read(B/'verification/PREPARE_v01.json');assert prep['proof_written_before_checker']
 for rel,h in prep['inputs'].items():bind(R/rel,h)
 bind(Path(__file__))
 records={}
 for topic in ['negative_norm007_peer','negative_norm_forcing_assembly','registered_norm_assembly','candidate016_low_order_forcing','candidate016_low_order_forcing_peer']:
  p=R/'research'/topic/'verification/result.json';d=read(p);records[topic]=d
  for rel,h in d.get('inputs',{}).items():bind(R/rel,h)
 h=records['negative_norm007_peer'];a=records['negative_norm_forcing_assembly'];s=records['registered_norm_assembly'];o=records['candidate016_low_order_forcing'];op=records['candidate016_low_order_forcing_peer']
 checks['007_raw']=h['source_sha256']==a['source_sha256']==s['generator_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
 checks['H_acceptance_flags']=h['source_and_fix_bindings_confirmed'] and h['all160modes_covered_once'] and h['peer_totals_reproduced_at512bits'] and h['own_full_norm_strictly_inside_peer'] and h['verdict'].startswith('CONFIRMED coarse')
 lo=Q(h['strict_coarse_lower_exact']);hi=Q(h['strict_coarse_upper_exact'])
 checks['H_coarse_endpoints']=lo==Q('0.6355243760000922') and hi==Q('0.6355322685705510') and ar(lo)<arb(h['peer_lower']).lower() and ar(hi)>arb(h['peer_upper']).upper()
 checks['252_all_comparisons']=all(a['checks'].values()) and a['verdict'].startswith('CONFIRMED') and len(a['instances'])==4
 specs=[('FW-A2-Db','1/262144','1/1572864'),('FW-A2-Da','1/268435456','1/2684354560'),('FW-T-TB-rebal-v1','1/65536','3/327680'),('FW-T-TB-sharp-v1','1/8192','5289/50000000')];rows=[]
 for z,(name,ss,tt) in zip(a['instances'],specs,strict=True):
  key=name;lower=Q(z['strict_necessary_norm_lower']);upper=Q(z['strict_norm_upper']);threshold=Q(tt)
  checks[key+'_parameters']=z['framework']==name and Q(z['s_exact'])==Q(ss) and Q(z['threshold_exact'])==threshold
  checks[key+'_two_sided']=ar(lower)<arb(z['lower_comparison']['ball']).lower() and ar(upper)>arb(z['upper_comparison']['ball']).upper() and 0<threshold<lower<upper
  rows.append({'framework':name,'s_exact':ss,'threshold_exact':tt,'strict_lower_exact':str(lower),'strict_upper_exact':str(upper)})
 sharp=next(z for z in s['instances'] if z['label']=='sharpw');own16=next(z for z in o['instances'] if z['framework']=='FW-T-T4L2-sharpw-v1');peer16=next(z for z in op['instances'] if z['framework']=='FW-T-T4L2-sharpw-v1')
 checks['016_reciprocal_accepted']=all(o['checks'].values()) and all(op['checks'].values()) and Q(peer16['strict_factor'])==Q(own16['threshold_ratio_lower_comparison']['strict_lower_exact'])==3542234
 checks['same_sharpw_parameters']=Q(sharp['threshold_exact'])==Q(own16['sufficient_threshold_exact'])==Q(4207,20000000) and Q(sharp['s_exact'])==Q(own16['s_exact'])==Q(1,5184) and [sharp['w1'],sharp['w2']]==own16['weights']==[32768,1048576]
 checks['lower_factors_order']=Q(own16['threshold_ratio_lower_comparison']['strict_lower_exact'])<Q(sharp['lower_threshold_ratio']['strict_lower_exact'])==Q('3596535.57')
 checks['counterassignments']=arb(sharp['lower_comparison']['ball'])<757<arb(sharp['upper_comparison']['ball']) and arb(own16['forcing_lower_comparison']['ball'])<750<757<800
 report=(B/'source/FINAL_REPORT_1357_v01.md').read_text();lines=report.splitlines()
 snippets={'H_running':'c1-n3\'s enclosure of it for 007 is running, so only lower bounds are certified in those norms.','only_d2_H':'only d2 has a certified ||F||_H.','best_lower_factor':'smallest certified forcing-norm ratio','proper_016_failure_scope':'sufficient test, not an exclusion or a nonexistence result','lower_bounds_no_order':'lower bounds for different candidates do not order'}
 passages={}
 for name,snip in snippets.items():
  hit=[{'line':i+1,'text':line.strip()} for i,line in enumerate(lines) if snip in line]
  checks['passage_'+name]=bool(hit);passages[name]=hit
 checks['accepted_H_before_frozen_report']=datetime.fromisoformat(h['utc'])<datetime.fromisoformat('2026-10-29T13:49:00+00:00') and datetime.fromisoformat(a['utc'])<datetime.fromisoformat('2026-10-29T13:49:00+00:00')
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,v in inputs.items():assert sha(R/rel)==v
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'scope':'Selected passages of frozen report only; no complete report audit or new integral reproduction','checks':checks,'check_count':len(checks),'inputs':inputs,'report_sha256':sha(B/'source/FINAL_REPORT_1357_v01.md'),'passages':passages,'candidate007_H_strict_interval':[str(lo),str(hi)],'candidate007_Ns_strict_intervals':rows,'sharpw_quoted_lower_factors':{'007':sharp['lower_threshold_ratio']['strict_lower_exact'],'016':own16['threshold_ratio_lower_comparison']['strict_lower_exact']},'logical_counterassignments':[[757,750],[757,800]],'findings':[{'claim':'007 H still running and only lower Ns bounds certified','verdict':'REFUTED','reason':'Accepted249 and252 predate this draft and provide the coarse H and four two-sided Ns enclosures.'},{'claim':'007 has the smallest certified forcing-norm ratio','verdict':'OPEN','reason':'Ambiguous comparison set and bound type; literal quoted lower factor ordering is reversed by016, and actual ratio ordering does not follow from those lower comparisons.'},{'claim':'016 sufficient-test failure implies no correction-ball or nonexistence conclusion','verdict':'CONFIRMED','reason':'The frozen late016 section explicitly preserves the accepted374/451 scope.'}],'verdict':'CONFIRMED selected evidence audit; REFUTED two stale007 norm-status sentences; actual cross-candidate ratio ordering remains OPEN from these inputs; no existing exclusion changes'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(inputs),'bindings',sha(target),out['utc'],out['elapsed_seconds'])
if __name__=='__main__':main()
