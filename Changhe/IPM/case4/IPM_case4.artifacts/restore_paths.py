"""Copy this folder to DEST, replacing path tokens by real prefixes, and report how many files regain their original SHA-256.

Usage: python3 restore_paths.py DEST TOKEN=PREFIX [TOKEN=PREFIX ...]
Example: python3 restore_paths.py ../ipm860_copy @NUM_DIR@=$HOME/ipm860 @WORK_REALPATH@=$HOME/ipm860/work @OUTPUT_REALPATH@=$HOME/ipm860/outputs
Tokens not given stay in place. Files regain their original bytes only if every token they contain is mapped to the
original prefix of the campaign host and the file has no other publication edits (see MANIFEST_PUBLISHED.json).
"""
import hashlib, json, os, shutil, sys

here = os.path.dirname(os.path.abspath(__file__))
dest = os.path.abspath(sys.argv[1])
pairs = [a.split('=', 1) for a in sys.argv[2:]]
man = json.load(open(os.path.join(here, 'MANIFEST_PUBLISHED.json')))
same = 0
for f in man['files']:
    b = open(os.path.join(here, f['path']), 'rb').read()
    if f['paths_tokenized']:
        t = b.decode('utf-8')
        for tok, pre in pairs:
            t = t.replace(tok, pre)
        b = t.encode('utf-8')
    out = os.path.join(dest, f['path'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'wb').write(b)
    shutil.copymode(os.path.join(here, f['path']), out)
    same += hashlib.sha256(b).hexdigest() == f['original_sha256']
print(f"{len(man['files'])} files written to {dest}; {same} match their original SHA-256")
