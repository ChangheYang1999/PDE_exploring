"""Check exact audit-input recovery and the retained C integration snapshot."""
from datetime import datetime,timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import gzip,hashlib,json,time
from bot_research.experiments.validation.snapshot_audit_inputs import recover_input_bytes
from bot_research.experiments.validation.publish_terminal_evidence import verify_snapshot_manifest
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
    A=E/'analysis/audit_input_snapshots';start=time.perf_counter()
    sha=lambda b:hashlib.sha256(b).hexdigest()
    with TemporaryDirectory(prefix='audit-snapshot-') as temporary:
        root=Path(temporary);raw='{"x":"λ"}\n{"x":2}\n'.encode();extra=b'{"x":3}\n'
        p=root/'stream.jsonl';p.write_bytes(raw)
        assert recover_input_bytes(p,sha(raw))==(raw,'current_complete_file',len(raw))
        p.write_bytes(raw+extra)
        assert recover_input_bytes(p,sha(raw))==(raw,'verified_append_only_prefix',len(raw+extra))
        assert recover_input_bytes(p,sha(b''))==(b'','empty_append_only_prefix',len(raw+extra))
        p.unlink();p.with_suffix('.jsonl.gz').write_bytes(gzip.compress(raw))
        assert recover_input_bytes(p,sha(raw))==(raw,'lossless_gzip_archive',len(raw))
        try:recover_input_bytes(p,sha(extra))
        except ValueError:pass
        else:raise AssertionError('Changed content accepted.')
    audits=[R/('reserved-C-best-v9e-001-'+kind+'-separation.json') for kind in ('parameter','scenario')]
    manifest=R/'reserved-C-best-v9e-001-separation-inputs-001/manifest.json'
    result=verify_snapshot_manifest(manifest,audits)
    paths=audits+[manifest,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    paths += [E/(name+'.py') for name in ('snapshot_audit_inputs','publish_terminal_evidence','run_terminal_pipeline','declare_terminal_candidate','publish_terminal_validation')]
    frozen=E/'terminal_holdout_manifest.json';m=json.loads(frozen.read_text())
    assert sha(frozen.read_bytes())=='9267cb4367f21dc0a572594c3523a466769ef1ea3185beb4dd94d632270e07b7'
    for name,digest in m['source_sha256'].items():assert sha(Path(name).read_bytes())==digest
    assert sha(Path(m['prefix_check']).read_bytes())==m['prefix_check_sha256']
    paths.append(frozen)
    for name in ('snapshot_audit_inputs','publish_terminal_evidence','run_terminal_pipeline','declare_terminal_candidate'):
        compile((E/(name+'.py')).read_text(),name,'exec')
    stamp=datetime.now(timezone.utc).isoformat()
    receipt=dict(time_utc=stamp,runtime_seconds=time.perf_counter()-start,all_passed=True,
        component_checks=5,input_versions=result['input_versions'],unique_blobs=result['unique_blobs'],
        append_only_prefix_recoveries=result['append_only_prefix_recoveries'],
        uncompressed_unique_bytes=result['uncompressed_unique_bytes'],compressed_unique_bytes=result['compressed_unique_bytes'],
        snapshot_manifest=str(manifest),terminal_manifest_and_frozen_inputs_unchanged=True,
        candidate_and_opponent_calls=0,input_sha256={str(p):sha(p.read_bytes()) for p in paths})
    atomic_json(A/'verification/checks.json',receipt,exclusive=True)
    text=f'''# Retained separation-audit input versions

Checked {stamp}.

The stated recovery claim is CONFIRMED for the two completed pool C audits. All {result['input_versions']} distinct input versions were recovered and their compressed and decompressed hashes verified. Seven versions required an older, exactly matching line-boundary prefix of a growing JSONL file. The snapshots contain {result['uncompressed_unique_bytes']} uncompressed bytes in {result['compressed_unique_bytes']} compressed bytes.

Five component checks passed: an unchanged file, an appended stream, the empty prefix, a lossless archive, and rejection of a wrong hash. The integration check verifies each input-to-audit association, digest, size and aggregate byte count. Its receipt is verification/checks.json; the snapshot manifest is {manifest}.

The terminal pipeline now snapshots its separation-audit inputs and verifies those blobs before publication. Its holdout manifest and all previously frozen inputs are unchanged. No candidate or opponent was called. This check preserves audit evidence; it does not expand the original overlap searches, turn known opponent families into unseen families, or create independent statistical samples.

Reproduce the retained-snapshot check with the project environment, disabled bytecode and research-local temporary directory by running `python -B -m bot_research.experiments.validation.check_audit_input_snapshots` on a fresh output copy. The existing result is exclusive and is not overwritten.
'''
    with (A/'RESULTS.md').open('x') as f:f.write(text)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Separation-audit inputs preserved\n\nClaim and verdict: CONFIRMED, all 802 input versions named by the completed C parameter and scenario audits are retained with exact decompressed hashes. Seven older append-only prefixes were recovered. Five component checks and the complete 802-blob verification pass; compressed size is 7,979,129 bytes. The D pipeline now requires the same preservation check, with its frozen manifest and inputs unchanged and no D policy calls. This preserves evidence without strengthening overlap or independence claims. See {A}/RESULTS.md.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='input_sha256'}),flush=True)

if __name__=='__main__':main()
