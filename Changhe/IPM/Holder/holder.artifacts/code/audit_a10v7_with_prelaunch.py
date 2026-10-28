"""Audit all a10 chunks and retain producer pre-launch and verifier in-run records."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];P=ROOT.parent/'the lead work/scratch/projcert';OUT=ROOT/'05_team_audit/stieltjes_v7/a10'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 source=P/'verification/a10v7_prelaunch_hashes.txt';lines=source.read_text().splitlines();assert lines[0]=='2026-10-28T11:06:33Z'
 for line in lines[1:]:
  h,name=line.split(None,1);assert sha(P/name)==h
 log=(P/'run_a10v7.log').read_text();assert '2026-10-28T11:44:50.750480+00:00 COMPLETE' in log and log.rstrip().endswith('EXIT 0')
 original=(ROOT/'code/audit_stieltjes_v7.py').read_text();updated=(ROOT/'code/audit_stieltjes_v7_small.py').read_text()
 assert updated==original.replace('if alpha==Q(1,5):','if alpha in (Q(1,20),Q(1,10),Q(1,5)):')
 producerold=(P/'combine_v7.py').read_text();producernew=(P/'combine_v7b.py').read_text()
 expected=producerold.replace("elif alpha==F(1,5):","elif alpha in [F(1,20),F(1,10),F(1,5)]:")
 assert [ast.dump(n) for n in ast.parse(producernew).body[1:]]==[ast.dump(n) for n in ast.parse(expected).body[1:]]
 subprocess.run([sys.executable,'-B',str(ROOT/'code/audit_stieltjes_v7_small.py'),str(P/'plans/a10v7.json'),'--out',str(OUT.relative_to(ROOT))],check=True)
 path=OUT/'independent_audit.json';d=json.loads(path.read_text());assert len(d['chunks'])==20
 for src in [source,P/'run_a10v7.log',P/'combine_v7b.py',Path(__file__)]:
  h=sha(src);dst=OUT/'frozen'/(h[:12]+'_'+src.name);dst.write_bytes(src.read_bytes());assert sha(dst)==h;d['frozen_sha256'][str(dst.relative_to(ROOT))]=h
 observed=OUT/'observed_in_run';manifest=json.loads((observed/'manifest.json').read_text())
 assert manifest['observed_time']=='2026-10-28T11:16:04.465553+00:00'
 for name,h in manifest['files'].items():
  src=observed/name;assert sha(src)==h,name
  if name!='run_a10v7.log':assert sha(P/name)==h,name
  d['frozen_sha256'][str(src.relative_to(ROOT))]=h
 d['frozen_sha256'][str((observed/'manifest.json').relative_to(ROOT))]=sha(observed/'manifest.json')
 d['provenance_scope']='Producer pre-launch record at2026-10-28T11:06:33Z matched to completed certifier, queue, plan, launch script and combiner; verifier in-run observation at11:16Z retained; no claim of independent pre-launch observation'
 d['prelaunch_audit_time_utc']=datetime.now(timezone.utc).isoformat();path.write_text(json.dumps(d,indent=2)+'\n');print(d['prelaunch_audit_time_utc'],'pre-launch and in-run evidence retained')
if __name__=='__main__':main()
