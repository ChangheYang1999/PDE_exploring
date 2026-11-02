"""Check campaign archives, explicit data certificates and loaded-source receipts."""
from datetime import datetime, timezone
from pathlib import Path
import argparse, hashlib, json, time
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--campaigns',nargs='+',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args();start=time.perf_counter();audits=[];inputs={}
    for name in args.campaigns:
        folder=Path(name)
        assert not folder.is_absolute() and '..' not in folder.parts
        freeze_path=folder/'freeze.json';freeze=json.loads(freeze_path.read_text())
        inputs[str(freeze_path)]=digest(freeze_path)
        manifest_files=[p for p in freeze['source_sha256'] if p.endswith('.json') and digest(p)==freeze['manifest_sha256']]
        assert len(manifest_files)==1,manifest_files
        manifest_path=manifest_files[0];manifest=json.loads(Path(manifest_path).read_text())
        for p,h in manifest['input_sha256'].items():
            assert freeze['source_sha256'].get(p)==h,p
        archive_count=0
        for p,h in freeze['source_sha256'].items():
            path=Path(p);assert not path.is_absolute() and '..' not in path.parts
            assert digest(path)==h,p
            assert digest(folder/'sources'/path)==h,p
            archive_count+=1
        data=[p for p in manifest['input_sha256'] if '/data/' in p and p.endswith('.json')]
        assert 'bot_research/bots/counters/data/maze_layouts_001.json' in data
        if any('guarded_maze' in o['spec'] for o in manifest['opponents']):
            assert 'bot_research/bots/counters/data/maze_guards_001.json' in data
        results=0
        for job in json.loads((folder/'jobs.json').read_text()):
            path=folder/'results'/(job['id']+'.json')
            assert path.exists(),str(path)
            row=json.loads(path.read_text())
            for field in ('source_sha256','source_sha256_at_end'):
                for p,h in row[field].items():assert freeze['source_sha256'].get(p)==h,p
            assert not row['source_changed_during_match']
            results+=1
        assert results==manifest.get('expected_conditions',2*len(manifest['candidates'])*len(manifest['opponents']))
        audits.append(dict(campaign=str(folder),archived_inputs=archive_count,explicit_data=data,results=results,all_passed=True))
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,checker_sha256=digest(__file__),inputs=inputs,campaigns=audits,all_passed=True,scope='Byte identity of declared inputs, archives and source attestations. Complete results required. This does not independently replay game outcomes.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:v for k,v in output.items() if k not in ('inputs',)}))


if __name__=='__main__':main()
