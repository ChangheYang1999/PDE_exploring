"""Read-only authenticated inputs and the accepted complete-owner contracts."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip, importlib.util, json, os, shutil, sys, time
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/source013_near_norms'
CHUNK = 'research/source013_near_admission'
COVER = 'research/source013_near_cover'
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(ROOT / CHUNK / 'code'))
import contract_v02 as contract
import chunks_v01 as chunks
LONG_MH = '4bb8d2adf05b2a16ad09067e88cf1c24e714e6529222746985e12183895d99bb'
LONG_RH = 'b45103ffd8b6a5f86d80fde7ad709e6873f395465fb6ad94f0114eaef3a2bfd2'
SHORT_MH = '490d4b6407a69fda73b0b466f61c780506b5a18c5d6034da6e3f87d4ec5ad6ce'
SHORT_RH = 'efa0057cfb2a0009f7e73e552f01aeea2d20fb43306cb07134df40ed45e2bfbd'
CORRECTION_SOURCE = {'id': 'C2-N1-013', 'raw_sha256': 'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a',
          'canonical_sha256': '2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33',
          'fields_sha256': '3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb',
          'fixed_c_exact': '4076476460239181/2251799813685248'}
ENDPOINT_SOURCE = {'reference_sha256': 'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21',
                   'raw_phi_sha256': CORRECTION_SOURCE['raw_sha256'], **{k: CORRECTION_SOURCE[k] for k in ['canonical_sha256', 'fields_sha256', 'fixed_c_exact']}}
SOURCE = dict(ENDPOINT_SOURCE)
ENDPOINT_GEOMETRY = {'minimum_scale_exact': '1/8', 'origin': {'radius_exact': '1/4096', 'analytic_radius_exact': '1/64', 'outer_radius_exact': '1/32', 'degree': 36}, 'exterior': {'radius_exact': '10000'}}

def stamp():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

def digest(path):
    d = sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            d.update(block)
    return d.hexdigest()

def safe(name):
    return Path(contract.path(name))

def local(name):
    return ROOT / safe(name)

def read(path):
    with Path(path).open() as f:
        return json.load(f)

def put(path, value):
    with Path(path).open('x') as f:
        json.dump(value, f, indent=2); f.write('\n')

def load(name, path):
    path = local(path); sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def resources():
    total = 0
    for base, dirs, files in os.walk(ROOT, followlinks=False):
        dirs[:] = [d for d in dirs if not (Path(base) / d).is_symlink()]
        for name in files:
            p = Path(base) / name
            if not p.is_symlink():
                try: total += p.stat().st_size
                except FileNotFoundError: pass
    free = shutil.disk_usage(ROOT).free
    assert total < 2_950_000_000 and free >= 20_000_000_000
    return {'owner_lane_bytes': total, 'filesystem_free_bytes': free}

def environment():
    assert os.sched_getaffinity(0) == {50} and os.getpriority(os.PRIO_PROCESS, 0) >= 19
    assert sys.version_info[:3] == (3, 12, 13)
    assert all(os.environ.get(k) == '1' for k in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'])
    assert time.time() < contract.CUTOFF
    resources()

class Registry:
    """Hash each distinct named dependency on entry and again after all reads."""
    def __init__(self):
        self.files = {}
        self.external = {}
    def path(self, name, external=False):
        if external:
            assert isinstance(name, str) and '\\' not in name
            p = Path(name)
            assert not p.is_absolute() and len(p.parts) > 2 and p.parts[0] == '..'
            assert p.parts[1] in ['theory_audit', 'numerics_agent_1', 'numerics_agent_2'] and '..' not in p.parts[2:] and str(p) == name
            return ROOT / p
        return local(name)
    def bind(self, name, expected, external=False):
        assert isinstance(expected, str) and len(expected) == 64 and all(ch in '0123456789abcdef' for ch in expected)
        entries = self.external if external else self.files
        path = self.path(name, external)
        if name in entries:
            assert entries[name] == expected
        else:
            assert digest(path) == expected, name
            entries[name] = expected
        return path
    def mapping(self, files, external=False):
        assert isinstance(files, dict)
        for name, expected in files.items():
            self.bind(name, expected, external)
    def json(self, name, expected, compressed=False):
        path = self.bind(name, expected)
        if compressed:
            with gzip.open(path, 'rt') as stream: return json.load(stream)
        return read(path)
    def actual_review(self, name, expected, fields, own):
        review = self.json(name, expected)
        assert review['status'] == 'BOUND' and review['audit_ids']
        for key, value in fields.items(): assert review[key] == value, key
        assert all(review['own_bindings'].get(k) == v for k, v in own.items())
        self.mapping(review['own_bindings']); self.mapping(review['external_dependencies'], True)
        assert review['external_dependencies'], 'Independent actual review required'
        return review
    def final(self):
        for external, entries in [(False, self.files), (True, self.external)]:
            for name, expected in entries.items(): assert digest(self.path(name, external)) == expected, name
        assert time.time() < contract.CUTOFF
        resources()
