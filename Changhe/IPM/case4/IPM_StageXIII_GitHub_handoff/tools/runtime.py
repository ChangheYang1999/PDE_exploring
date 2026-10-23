"""Process-local relocation of the frozen scientific checkpoint; no byte edits.

SHA-256 always covers original bytes. Only decoded historical absolute path
strings are translated. Numerical scalars, coefficients and relative names are
unchanged. This is a runtime adapter, not a replacement field or solver.
"""
import hashlib
import json
import os
from pathlib import Path
import sys

ORIGINAL = '/Users/caltech/research/IPM_R2_macpro_experiments/stage13_absolute_optimization'
HISTORICAL_ROOTS = (
    ORIGINAL,
    '/Users/caltech/research/IPM_R2_macpro_runs/verification_20261020_01',
    '/Users/caltech/research/IPM_R2_macpro_reference_20261020',
    '/Users/caltech/research/IPM_R2_macpro_experiments/stage11_five_taylor',
    '/Users/caltech/research/IPM_R2_macpro_experiments/stage12_large_scale',
    '/Users/caltech/research/IPM_R2_macpro_experiments/stage12_absolute_loss',
    '/Users/caltech/Changhe/IPM/IPM_R2',
)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


class Runtime:
    def __init__(self, repo, research=None):
        self.repo = Path(repo).expanduser().resolve()
        self.research = Path(research).resolve() if research else self.repo/'research'
        self.mapping = [(ORIGINAL, str(self.research))]
        # Unused provenance paths are deliberately mapped to absent directories,
        # rather than silently falling back to a source-host installation.
        self.mapping += [(old, str(self.repo/'unshipped_provenance'/str(i)))
                         for i, old in enumerate(HISTORICAL_ROOTS[1:])]
        self.translations = set()
        self.blocked = []
        self.allowed_data = [str(self.repo), str(self.research)]
        self.allowed_runtime = sorted(set((str(Path(sys.prefix).resolve()),
                                           str(Path(sys.base_prefix).resolve()))))

    def translate(self, value):
        if isinstance(value, str):
            if any(value == p or value.startswith(p+'/') for p in self.allowed_data):
                return value
            for old, new in self.mapping:
                if value == old or value.startswith(old+'/'):
                    result = new+value[len(old):]
                    self.translations.add((value, result))
                    return result
        return value

    def view(self, value):
        if isinstance(value, dict):
            return {self.translate(k): self.view(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self.view(v) for v in value]
        return self.translate(value)

    def read(self, path):
        return self.view(json.loads(Path(self.translate(str(path))).read_text()))

    def install(self):
        original = json.loads
        def loads(*args, **kwargs):
            return self.view(original(*args, **kwargs))
        json.loads = loads
        def hook(event, args):
            if event not in ('open', 'os.listdir', 'os.scandir') or not args:
                return
            if not isinstance(args[0], (str, bytes, os.PathLike)):
                return
            path = os.path.abspath(os.fsdecode(args[0]))
            if any(path == p or path.startswith(p+'/')
                   for p in self.allowed_data+self.allowed_runtime):
                return
            if any(path == p or path.startswith(p+'/') for p in HISTORICAL_ROOTS):
                self.blocked.append({'event': event, 'path': path})
                raise PermissionError('Original research path forbidden: '+path)
        sys.addaudithook(hook)
        sys.dont_write_bytecode = True
        sys.path.insert(0, str(self.research))

    def record(self):
        return {'research': str(self.research), 'path_mapping': dict(self.mapping),
                'translated_unique_paths': len(self.translations),
                'blocked_original_reads': self.blocked,
                'allowed_interpreter_prefixes': self.allowed_runtime,
                'scientific_bytes_modified': False,
                'denial_scope': 'CPython open/listdir/scandir audit hook; not a native-code sandbox'}
