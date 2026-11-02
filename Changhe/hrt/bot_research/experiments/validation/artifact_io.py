"""Atomic evidence files and path-safe diagnostics for independent validation."""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import tempfile


def atomic_json(path, value, *, exclusive=False):
    """Publish complete JSON; exclusive mode never replaces existing evidence."""
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix='.partial-', suffix='.json', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, sort_keys=True, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        if exclusive:
            os.link(temporary, path)
        else:
            os.replace(temporary, path)
        temporary.unlink(missing_ok=True)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def public_diagnostic(text):
    text = text.replace(str(Path.cwd()), '<project>')
    return re.sub(r'/(?:mnt|home|efs|tmp)(?:/[^\s\"\'<>:()\[\],;]*)?', '<local-path>', text)
