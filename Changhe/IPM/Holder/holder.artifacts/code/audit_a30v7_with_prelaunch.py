"""Run the unchanged structural auditor and bind the a30 pre-launch record."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
PRODUCER=ROOT.parent/'the lead work/scratch/projcert'
OUT=ROOT/'05_team_audit/stieltjes_v7/a30'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=PRODUCER/'verification/a30v7_prelaunch_hashes.txt'
    lines=source.read_text().splitlines();assert lines[0]=='2026-10-28T10:25:45Z'
    for line in lines[1:]:
        digest,name=line.split(None,1);assert sha(PRODUCER/name)==digest
    log=(PRODUCER/'run_a30v7.log').read_text()
    assert '2026-10-28T11:02:00.414668+00:00 COMPLETE' in log and log.rstrip().endswith('EXIT 0')
    subprocess.run([sys.executable,'-B',str(ROOT/'code/audit_stieltjes_v7.py'),str(PRODUCER/'plans/a30v7.json'),'--out',str(OUT.relative_to(ROOT))],check=True)
    p=OUT/'independent_audit.json';d=json.loads(p.read_text())
    for src in [source,PRODUCER/'run_a30v7.log',Path(__file__)]:
        h=sha(src);dst=OUT/'frozen'/(h[:12]+'_'+src.name);dst.write_bytes(src.read_bytes());assert sha(dst)==h
        d['frozen_sha256'][str(dst.relative_to(ROOT))]=h
    d['provenance_scope']='Producer pre-launch record at2026-10-28T10:25:45Z retained and matched to certifier, queue, plan and launch script; completion2026-10-28T11:02:00Z; no claim of independent pre-launch observation by verifier'
    d['prelaunch_audit_time_utc']=datetime.now(timezone.utc).isoformat()
    p.write_text(json.dumps(d,indent=2)+'\n')
    print(d['prelaunch_audit_time_utc'],'pre-launch record matched')
if __name__=='__main__':main()
