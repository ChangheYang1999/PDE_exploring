"""Exact audit of three rounded displays. No peer execution or integrals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,re,os,time
B=Path(__file__).resolve().parents[1];L=B.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
 def ck(v,label):
  checks.append({'check':label,'pass':bool(v)})
  if not v:raise AssertionError(label)
 ck(os.sched_getaffinity(0)=={50,51} and os.getpriority(os.PRIO_PROCESS,0)==19,'assigned affinity and priority')
 m=json.loads((B/'data/manifest.json').read_text())
 for rel,h in m['inputs'].items():ck(sha(B/rel)==h,'binding '+rel)
 first=json.loads((B/'data/PROOF_FIRST.json').read_text());ck(not first['checker_exists'] and first['proof_sha256']==sha(B/'PROOF.md'),'proof first')
 peer=json.loads((B/'source/input_02_result.json').read_text());ck(peer['check_count']==len(peer['checks'])==342 and all(x['pass'] for x in peer['checks']),'peer record internally consistent, not acceptance of all342')
 ck(sha(B/'source/input_02_result.json')=='7f6ab769d8ccf8a7f791b384cf1f9511aaa89370b4f013f97657a1e1622fee62','fixed439 root')
 for r in json.loads((B/'data/initial_sources.json').read_text())['rows']:
  ck(sha(B/r['local'])==r['sha256'],'source copy '+r['local'])
  if r['source_relative'] in peer['inputs']:ck(r['sha256']==peer['inputs'][r['source_relative']],'selected439 binding '+r['source_relative'])
 rp=L/'research/energy_share_attribution_acceptance/source/input_01_report_v01.md';lines=rp.read_text().splitlines();ck(sha(rp)=='7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743','frozen report')
 ck('| residual LB |' in lines[1049] and peer['table_heading_line']==1050,'heading at1050')
 def ball(text):
  a=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',text);ck(a is not None,'parse ball');c,e=map(Q,a.groups());ck(e>=0,'radius nonnegative');return c-e,c+e
 raw=json.loads((B/'source/input_03_d2_G0_ball_2048.json').read_text());d2=(ball(raw['norm_lower_ball'])[0],ball(raw['norm_upper_ball'])[1])
 p016=B/'source/input_04_comparison_G0_rF_G1_P2_v01.json';component=json.loads(p016.read_text())['norms']['rF'];c16=(Q(component['accepted_lower_exact']),Q(component['accepted_upper_exact']))
 old=L/'research/candidate016_complete_forcing_audit/source/component_acceptance.json';ck(sha(p016)==sha(old),'016 byte equal earlier467 acceptance')
 old16=json.loads((L/'research/candidate016_complete_forcing_audit/data/components.json').read_text())['norms']['rF'];ck(c16==(Q(old16['lower_exact']),Q(old16['upper_exact'])),'own467 exact endpoints')
 specs=[(20,1069,'G0 = 4.99',d2,Q('4.99'),Q('.01')),(37,1086,'G0 = 4.99',d2,Q('4.99'),Q('.01')),(80,1129,'7.1457012',c16,Q('7.1457012'),Q('.0000001'))];rows=[]
 for number,line,token,(a,b),d,u in specs:
  hits=[(j+1,s) for j,s in enumerate(lines) if s.startswith('| '+str(number)+' |')];ck(len(hits)==1 and hits[0][0]==line and token in hits[0][1],'frozen row '+str(number))
  ck(0<a<=b<d,'display is not lower bound '+str(number));ck(d-u/2<a<=b<d+u/2,'strict nearest rounding cell '+str(number))
  saved=next(x for x in peer['not_directed_lower_bound'] if x['table_row']==number)
  for key,value in [('display',d),('quantity_lower',a),('quantity_upper',b),('display_minus_upper',d-b)]:ck(Q(saved[key])==value,'independent '+key+' '+str(number))
  ck(saved['frozen_line']==line,'peer line '+str(number));rows.append({'table_row':number,'frozen_line':line,'display_exact':str(d),'lower_exact':str(a),'upper_exact':str(b),'display_minus_upper_exact':str(d-b),'unit_exact':str(u)})
 ck(not peer['new_integrals'] and not peer['candidate_verdict_changes'],'scope only')
 r={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'check_count':len(checks),'checks':checks,'inputs':m['inputs'],'verdict':'CONFIRMED three nearest displays; REFUTED blanket residual LB interpretation','rows':rows,'table_heading_line':1050,'target_sha256':sha(rp),'scope':'Only heading and three counterexamples in N4-439. No acceptance here of its other supplemental checks. Prior certificates explicit premises. No new integral or peer execution.','elapsed_seconds':time.monotonic()-tick}
 with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(m['inputs']),'bindings',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
if __name__=='__main__':main()
