"""Finite transfer of accepted literal findings across one header change."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_final_freeze_transfer'
def main():
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 inputs={};checks=[]
 def bind(rel,want=None):
  p=R/rel;assert p.resolve().is_relative_to(R);h=hashlib.sha256(p.read_bytes()).hexdigest();assert want is None or h==want;inputs[rel]=h;return p
 def ck(value,label):
  checks.append({'check':label,'pass':bool(value)});assert value,label
 manifest=json.loads(bind('research/numerics_final_freeze_transfer/verification/PROOF_FIRST.json').read_text());ck(not manifest['checker_exists'] and not manifest['result_exists'],'proof first')
 for rel,h in manifest['inputs'].items():bind(rel,h);ck(True,'frozen '+rel)
 oldresult=json.loads((R/'research/numerics_final_repairs/verification/result_v03.json').read_text())
 for rel,h in oldresult['inputs'].items():bind(rel,h);ck(True,'accepted '+rel)
 ck(all(oldresult['checks'].values()),'all old finite checks passed')
 ck(oldresult['display_transfer_count']==600,'same 600-display scope')
 old=(R/'research/numerics_final_repairs/source/report_v03.md').read_bytes().splitlines(keepends=True);new=(B/'source/report.md').read_bytes().splitlines(keepends=True)
 ck(len(old)==len(new),'same line count');changed=[i for i,(a,b) in enumerate(zip(old,new)) if a!=b];ck(changed==[2],'only line3 changed')
 ck(old[2].startswith(b'Status: ') and new[2].startswith(b'Status: FINAL (frozen 2026-10-29T18:30:12Z'),'status line and stated freeze')
 ck(old[:2]+old[3:]==new[:2]+new[3:],'every other byte unchanged')
 ck(b'only errata requested by an audit' in new[2] and b'CONFIRMED by N4-424 and T4-496' in new[2],'read header scope')
 bind(str(Path(__file__).relative_to(R)))
 output={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'old_report_sha256':hashlib.sha256(b''.join(old)).hexdigest(),'new_report_sha256':hashlib.sha256(b''.join(new)).hexdigest(),'changed_line':3,'old_header':old[2].decode(),'new_header':new[2].decode(),'unchanged_other_lines':len(old)-1,'transferred_display_count':600,'source_integrals_recomputed':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED transfer of N4-424 finite literal scope; no mathematical status promotion'}
 with target.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
 print(output['utc'],len(checks),'checks',len(inputs),'bindings',hashlib.sha256(target.read_bytes()).hexdigest())
if __name__=='__main__':main()
