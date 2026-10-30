"""Own exact arithmetic audit. Never executes peer code or recomputes integrals."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib,json,os,re,time
B=Path(__file__).resolve().parents[1]; L=B.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
 def ck(value,label):
  checks.append({'check':label,'pass':bool(value)})
  if not value:raise AssertionError(label)
 ck(os.sched_getaffinity(0)=={50,51},'assigned affinity')
 ck(os.getpriority(os.PRIO_PROCESS,0)==19,'low priority')
 for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:ck(os.environ[key]=='1',key)
 m=json.loads((B/'data/manifest.json').read_text())
 for rel,h in m['inputs'].items():ck(sha(B/rel)==h,'manifest '+rel)
 first=json.loads((B/'data/PROOF_FIRST.json').read_text())
 ck(not first['checker_exists'] and first['proof_sha256']==sha(B/'PROOF.md'),'proof preceded checker')
 initial=json.loads((B/'data/initial_sources.json').read_text())['rows'];mapped={r['source_relative']:r for r in initial}
 for r in initial:ck(sha(B/r['local'])==r['sha256'],'copied source '+r['source_relative'])
 peer=json.loads((B/'source/N4_result.json').read_text())
 ck(len(peer['checks'])==peer['check_count']==29 and all(x['pass'] for x in peer['checks']),'peer29 consistency only')
 ck(len(peer['inputs'])==10,'ten peer bindings')
 for rel,h in peer['inputs'].items():ck(sha(B/mapped[rel]['local'])==h,'peer input '+rel)
 ck(not peer['new_integrals'] and not peer['candidate_verdict_changes'],'scope unchanged')
 root=json.loads((B/'source/input_06_result.json').read_text())
 ck(sha(B/'source/input_06_result.json')==sha(L/'research/candidate016_complete_forcing_audit/source/baseline007.json'),'root180 byte equal earlier own copy')
 accepted=L/'research/registered_norm_assembly/reviews/N4_180_181/ACCEPTANCE.md'
 ck(sha(accepted)=='691de787ebc1da42cce0c03801aeb1e2de7d3f2613db8dc584157d556048d17f','T4-238 analytic premise acceptance')
 report=(B/'source/input_01_report_v01.md').read_text().splitlines()
 ck(sha(B/'source/input_01_report_v01.md')=='7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743','fixed target report')
 for lo,hi in [(226,227),(993,994)]:
  text=' '.join(report[lo-1:hi]);ck('squared sharpw norm' in text and '72 percent' in text and '14 percent' in text,'frozen disputed lines '+str((lo,hi)))
 def ball(text):
  a=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',text);ck(a is not None,'ball parses')
  c,r=map(Q,a.groups());ck(r>=0,'ball nonnegative radius');return c-r,c+r
 raw0=json.loads((B/'source/input_04_N4_G0.json').read_text());rawD=json.loads((B/'source/input_05_N4_derivatives.json').read_text());ck(rawD['complete'],'full derivative certificate')
 comp={}
 for k,d in [('G0',raw0),('G1',rawD['norms']['G1']),('P2',rawD['norms']['P2'])]:
  a=ball(d['norm_lower_ball']);b=ball(d['norm_upper_ball']);comp[k]=(min(a[0],b[0]),max(a[1],b[1]));ck(0<comp[k][0]<=comp[k][1],'positive component '+k)
 rows=[]
 for name,w in [('E_star',{'P2':1,'G1':2**14,'G0':2**18}),('E_w',{'P2':1,'G1':2**15,'G0':2**20})]:
  saved=next(x for x in peer['energy_shares'] if x['energy']==name);ck(saved['weights']==w,'weights '+name)
  sq={k:(w[k]*a*a,w[k]*b*b) for k,(a,b) in comp.items()};SL=sum(x[0] for x in sq.values());SU=sum(x[1] for x in sq.values());shares={}
  for k,(a,b) in sq.items():
   loose=(a/SU,b/SL);tight=(a/(a+SU-b),b/(b+SL-a));p=saved['shares'][k]
   ck(loose==(Q(p['lower_exact']),Q(p['upper_exact'])),'independent loose endpoints '+name+' '+k)
   ck(0<loose[0]<=tight[0]<=tight[1]<=loose[1]<1,'monotonicity interval '+name+' '+k)
   if name=='E_star':
    target={'P2':14,'G1':72,'G0':14}[k];ck(Q(2*target-1,200)<loose[0]<=loose[1]<Q(2*target+1,200),'nearest percent cell '+k)
    old=root['E_star_energy_shares'][k];ck(Q(old['strict_lower_exact'])<loose[0]<=loose[1]<Q(old['strict_upper_exact']),'root180 share enclosure '+k)
   shares[k]={'loose_exact':[str(x) for x in loose],'tight_exact':[str(x) for x in tight],'tight_midpoint_FLOAT':float(sum(tight)/2)}
  rows.append({'energy':name,'weights':w,'shares':shares})
 sharp=next(x for x in root['instances'] if x['label']=='sharpw')
 ck(sharp['s_exact']=='1/5184' and sharp['w1']==32768 and sharp['w2']==1048576,'actual sharpw parameters')
 U=ball(sharp['upper_comparison']['ball'])[1];a0=comp['G0'][0];bound=2**20*a0*a0/(U*U)
 ck(bound==Q(peer['actual_fractional_sharpw_G0_share_lower_exact']),'independent actual fractional G0 bound')
 ck(4*2**20*a0*a0>U*U,'actual G0 share strictly exceeds one quarter')
 ck(bound>Q(29,200),'actual G0 share exceeds whole14 percent cell')
 ck(peer['disputed_frozen_lines']==[[226,227],[993,994]],'same two targets')
 out={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'verdict':'CONFIRMED N4-438 corrected E_star shares and actual sharpw G0 share>1/4; REFUTED two frozen attributions','check_count':len(checks),'checks':checks,'inputs':m['inputs'],'energy_shares':rows,'actual_fractional_sharpw_G0_share_lower_exact':str(bound),'actual_fractional_sharpw_G0_share_lower_FLOAT':float(bound),'target_sha256':sha(B/'source/input_01_report_v01.md'),'disputed_frozen_lines':[[226,227],[993,994]],'actual_fractional_P2_G1_shares':'OPEN','elapsed_seconds':time.monotonic()-tick,'new_integrals':False,'peer_code_executed':False}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(m['inputs']),'bindings',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
if __name__=='__main__':main()
