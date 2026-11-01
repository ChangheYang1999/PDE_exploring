"""Inventory local report links and explicitly spelled ledger evidence paths."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time
start=time.monotonic();now=datetime.now(timezone.utc)
base=Path('artifacts/final_audit')/now.strftime('%Y%m%dT%H%M%SZ');base.mkdir(parents=True,exist_ok=True)
compressed={r['original']:r for p in Path('artifacts/storage').glob('json_compression_*.json') for r in json.loads(p.read_text())['rows']}
def resolve(p):
    p=Path(p)
    if p.exists():return dict(status='exists',resolved=str(p),directory=p.is_dir())
    key=str(p)
    if key in compressed:
        row=compressed[key]
        return dict(status='recorded_lossless_gzip',resolved=row['archive'],exists=Path(row['archive']).exists())
    if Path(key+'.gz').exists():return dict(status='gzip_companion',resolved=key+'.gz')
    if Path(key+'.recipe.json').exists():return dict(status='reconstruction_recipe',resolved=key+'.recipe.json')
    archive=Path(key.removesuffix('.gz')+'.archive.json')
    if archive.exists():return dict(status='checkpoint_archive_recipe',resolved=str(archive))
    return dict(status='missing')
files=[p for p in Path('.').glob('*.md') if p.name not in ['PROMPT.md','SHIFT_PROMPT.md']]+list(Path('research').glob('*/PROOF.md'))
links=[]
for p in files:
    for n,line in enumerate(p.read_text().splitlines(),1):
        for target in re.findall(r'\]\(([^)]+)\)',line):
            if target.startswith(('http:','https:','mailto:','#')):continue
            target=target.split('#')[0].strip('<>')
            if not target:continue
            q=p.parent/target
            if target in {'1-delta',r'p_j+\partial_t',r't,\theta','a/p','i-j','1-i/n','1-z/R'}:
                links.append(dict(source=str(p),line=n,target=target,status='mathematical_expression',review='Explicitly inspected formula, not a file link.'))
                continue
            links.append(dict(source=str(p),line=n,target=target,**resolve(q)))
ledger=Path('VERIFY_REPORT.md');text=ledger.read_text();evidence=[]
for target in dict.fromkeys(re.findall(r'(?<![\w/])(?:research|artifacts|code)/[A-Za-z0-9_./-]+\.(?:json(?:\.gz)?|pkl(?:\.gz)?|md|py|txt|out|log)',text)):
    evidence.append(dict(target=target,**resolve(target)))
def counts(rows):
    out={}
    for r in rows:out[r['status']]=out.get(r['status'],0)+1
    return out
result=dict(at=now.isoformat(timespec='seconds'),scope='Existence/reconstruction inventory of local Markdown links and explicit research/artifacts/code filenames in the ledger. External links, bare prose abbreviations and anchor validity are not checked. This is not an arithmetic or mathematical audit.',files=len(files),ledger_sha256=sha256(ledger.read_bytes()).hexdigest(),markdown_link_counts=counts(links),ledger_evidence_counts=counts(evidence),links=links,ledger_evidence=evidence,actual_elapsed_s=time.monotonic()-start)
(base/'local_reference_inventory.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'final_local_reference_inventory.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['links','ledger_evidence']}))
for row in links+evidence:
    if row['status']=='missing':print(json.dumps(row))
