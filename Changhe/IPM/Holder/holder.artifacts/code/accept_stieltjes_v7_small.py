"""Bind a structurally checked positive sum after deterministic selected replay."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--ledger',required=True)
    args=ap.parse_args();base=(ROOT/args.folder).resolve();assert base.is_relative_to(ROOT)
    auditpath=base/'independent_audit.json';d=load(auditpath);hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    bind(auditpath)
    for name,h in d['frozen_sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    assert sha(ROOT/'code/audit_stieltjes_v7_small.py')==d['auditor_sha256'];bind(ROOT/'code/audit_stieltjes_v7_small.py')
    apath=ROOT/'05_team_audit/stieltjes_v7/verification/analytic_acceptance.json';aa=load(apath)
    assert aa['verdict']=='CONFIRMED';bind(apath)
    for name,h in aa['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    proofs=list(base.glob('PROOF.md'));assert len(proofs)==1;bind(proofs[0])
    replays=sorted((base/'replay').glob('*.json'));assert len(replays)==3
    selected=[]
    for p in replays:
        r=load(p);matches=[]
        for c in d['chunks']:
            src=load(ROOT/c['path'])
            if all(src[k]==r[k] for k in ('sign','start','stop','left','right','nx','ny')):matches.append((c,src))
        assert len(matches)==1,(p,len(matches))
        c,src=matches[0]
        for key in src:
            if key in ('time_utc','elapsed_seconds','source_hashes'):continue
            assert key in r and src[key]==r[key],(p.name,key,src[key],r.get(key))
        assert sorted(src['source_hashes'].values())==sorted(r['source_hashes'].values())
        for name,h in r['source_hashes'].items():assert sha(Path(name))==h;bind(Path(name))
        bind(p);selected.append(dict(producer=c['path'],replay=str(p.relative_to(ROOT)),all_numerical_fields_identical=True,rules=r['rule_counts']))
    assert {load(p)['sign'] for p in replays}=={-1,1}
    assert any(r['rules']['mv2'] and r['rules']['ref'] for r in selected)
    assert any(r['rules']['v2'] for r in selected)
    safe=Q(d['safe_D_lower']);lower=Q(d['exact_D_lower']);assert safe<=lower<safe+Q(1,10**10)
    bind(Path(__file__))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',
        alpha=d['alpha'],safe_D_lower=d['safe_D_lower'],exact_D_lower=d['exact_D_lower'],
        numerical_scope='Exact coverage and recombination of all chunks; selected deterministic geometric replay, not a full independent replay',
        provenance_scope=d['provenance_scope'],selected_replays=selected,sha256=hashes)
    dst=base/'accepted.json';dst.write_text(json.dumps(out,indent=2)+'\n')
    registry=ROOT/'data/accepted_external_D.json';old=load(registry)
    entries=[r for r in old['entries'] if Q(r['alpha'])!=Q(d['alpha'])]
    entries.append(dict(alpha=d['alpha'],safe_D_lower=d['safe_D_lower'],family='axis projection cusp, positive v7 Stieltjes sum',
        verdict='CONFIRMED',audit=args.ledger,audit_path=str(dst.relative_to(ROOT)),audit_sha256=sha(dst),
        source_path=str(ROOT/d['producer_combined']),source_sha256=sha(ROOT/d['producer_combined'])))
    old['time_utc']=out['time_utc'];old['entries']=entries;registry.write_text(json.dumps(old,indent=2)+'\n')
    print(out['time_utc'],out['alpha'],out['safe_D_lower'],out['verdict'])
if __name__=='__main__':main()
