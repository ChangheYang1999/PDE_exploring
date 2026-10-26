"""Record the import closure a test actually loaded: every module in sys.modules whose file lives under the lane's work tree."""
import hashlib, sys
from pathlib import Path
WORK = Path(__file__).resolve().parents[1]

def loaded_closure():
    rows = {}
    for name, mod in list(sys.modules.items()):
        f = getattr(mod, '__file__', None)
        if not f: continue
        p = Path(f).resolve()
        try: rel = str(p.relative_to(WORK))
        except ValueError: continue
        if p.suffix != '.py' or not p.exists(): continue
        rows[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return {'work_root': str(WORK), 'count': len(rows), 'files': dict(sorted(rows.items()))}
