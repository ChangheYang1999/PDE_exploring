"""Require preserved overlap-audit input bytes before publishing the final table."""
from pathlib import Path
import gzip,hashlib,json
from bot_research.experiments.validation.publish_terminal_validation import main as publish


def verify_snapshot_manifest(path,expected_audits):
    s=json.loads(Path(path).read_text())
    assert s['all_inputs_preserved']
    assert set(s['audit_sha256'])==set(map(str,expected_audits))
    expected={}
    for source,sha in s['audit_sha256'].items():
        raw=Path(source).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==sha
        for name,digest in json.loads(raw)['input_snapshot_sha256'].items():
            expected.setdefault((name,digest),set()).add(source)
    pinned={(row['source'],row['source_sha256']) for row in s['rows']}
    assert len(pinned)==len(s['rows'])==s['input_versions']
    assert set(expected)==pinned
    checked={}
    for row in s['rows']:
        key=(row['source'],row['source_sha256'])
        assert set(row['audits'])==expected[key]
        archive=Path(row['archive'])
        assert not archive.is_absolute() and '..' not in archive.parts
        if row['archive'] not in checked:
            raw=archive.read_bytes();plain=gzip.decompress(raw)
            assert hashlib.sha256(raw).hexdigest()==row['archive_sha256']
            assert hashlib.sha256(plain).hexdigest()==row['source_sha256']
            assert len(raw)==row['compressed_bytes'] and len(plain)==row['uncompressed_bytes']
            checked[row['archive']]=(row['source_sha256'],len(raw),len(plain))
        assert checked[row['archive']]==(row['source_sha256'],row['compressed_bytes'],row['uncompressed_bytes'])
    assert len(checked)==s['unique_blobs']
    assert sum(r[1] for r in checked.values())==s['compressed_unique_bytes']
    assert sum(r[2] for r in checked.values())==s['uncompressed_unique_bytes']
    return s


def main():
    E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
    d=json.loads((E/'terminal-candidate-declaration-001.json').read_text());name=d['campaign_name']
    path=R/(name+'-separation-inputs')/'manifest.json'
    verify_snapshot_manifest(path,[R/(name+'-'+kind+'-separation.json') for kind in ('parameter','scenario')])
    publish()
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write('\nThe final overlap-audit input bytes are preserved in '+str(path)+'. Every recorded input version and compressed blob is checked before publication; later appends to team result streams cannot change those retained bytes.\n')

if __name__=='__main__':main()
