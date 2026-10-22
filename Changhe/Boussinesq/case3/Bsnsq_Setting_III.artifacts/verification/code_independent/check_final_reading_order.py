"""Finite navigation audit; not a proof-quality or execution verifier."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
r=Path('research/350_final_reading_order_audit');v=r/'verification'
start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def ck(name,value,detail=None): checks.append(dict(name=name,passed=bool(value),detail=detail))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
prep=json.loads((v/'preparation.json').read_text());ck('proof_before_checks',prep['prepared_utc']<start.isoformat());ck('proof_hash',digest(r/'PROOF.md')==prep['proof_sha256'])
folders=sorted((p for p in Path('research').iterdir() if p.is_dir()),key=lambda p:int(p.name.split('_')[0]));ids=[int(p.name.split('_')[0]) for p in folders]
ck('topic_identifiers_unique',len(ids)==len(set(ids)));ck('numeric_order',ids==sorted(ids));inventory=[]
lines=['# Complete topic catalog','',f'Snapshot {start.isoformat()}. This is chronological navigation. File existence is not a proof-quality verdict. Read the [root summary](../FINAL_VERIFIER_SUMMARY.md), each proof\'s dependencies and its scoped verdict for mathematical reading order.','']
for p in folders:
    proof=p/'PROOF.md';ck('proof_exists_'+p.name,proof.is_file());content=proof.read_text();ck('proof_nonempty_'+p.name,bool(content.strip()))
    h=next((line.lstrip('#').strip() for line in content.splitlines() if line.startswith('#')),p.name)
    h=h.replace('[','(').replace(']',')');links=[f'[proof]({p.name}/PROOF.md)']
    for rel,label in [('SUMMARY.md','results'),('verification/SUMMARY.md','verification results'),('INDEX.md','packet index')]:
        if (p/rel).is_file(): links.append(f'[{label}]({p.name}/{rel})')
    lines.append(f'- {int(p.name.split("_")[0])}. {h}: '+', '.join(links)+'.')
    inventory.append(dict(topic=p.name,proof=str(proof),proof_sha256=digest(proof),bytes=proof.stat().st_size))
Path('research/CATALOG.md').write_text('\n'.join(lines)+'\n')
entry_files=['INDEX.md','FINAL_VERIFIER_SUMMARY.md','research/INDEX.md','research/CATALOG.md'];link_inventory=[]
for name in entry_files:
    p=Path(name);links=[]
    for target in re.findall(r'\]\(([^\n]+?)\)',p.read_text()):
        if '://' in target or target.startswith('#'):continue
        q=(p.parent/target.split('#')[0]).resolve();ck('link_'+name+'_'+target,q.exists())
        links.append(dict(target=target,exists=q.exists()))
    link_inventory.append(dict(file=name,sha256=digest(p),links=links))
s=Path('FINAL_VERIFIER_SUMMARY.md').read_text();ck('summary_open','No accepted YES or NO endpoint has been established.' in s);ck('summary_not_both_inverses_everywhere','not a claim that every broad-grid point received both inverse calculations' in s);ck('summary_not48active','48 active' in s);ck('catalog_scope','File existence is not a proof-quality verdict' in Path('research/CATALOG.md').read_text())
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,code_sha256=digest(__file__),proof_sha256=digest(r/'PROOF.md'),passed=sum(c['passed'] for c in checks),total=len(checks),topic_count=len(folders),proof_inventory=inventory,entry_files=link_inventory,checks=checks)
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:val for k,val in out.items() if k not in ['proof_inventory','entry_files','checks']},indent=2))
for c in checks:
    if not c['passed']:print('FAILED',c)
