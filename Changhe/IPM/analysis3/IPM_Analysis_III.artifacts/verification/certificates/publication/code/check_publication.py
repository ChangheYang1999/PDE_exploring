"""Read-only snapshot checks of publication files. Writes only its own lane output.

No mathematical code is executed. Reports describe the observed snapshot, not a
future publication. File identity is not proof validity or replay portability.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import re
import time

ROOT = Path(__file__).resolve().parents[3]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--lead', type=Path, default=ROOT.parent/'s2-lead')
parser.add_argument('--numerics', type=Path, default=ROOT.parent/'s2-num')
parser.add_argument('--label', default='snapshot')
args = parser.parse_args()
if not re.fullmatch(r'[A-Za-z0-9_-]+', args.label):
    raise ValueError('label must be a simple file-name component')
lead = args.lead.resolve()
num = args.numerics.resolve()
art = lead/'artifacts'
started = datetime.now(timezone.utc)
tick = time.monotonic()
out = ROOT/'certificates/publication/evidence'/f'{args.label}_{started:%H%M%S}.json'
assert out.resolve().is_relative_to(ROOT)
assert not out.exists()
errors = []
cache = {}
unstable = []
read_signatures = {}


def files(root):
    ans = []
    for base, dirs, names in os.walk(root, followlinks=False):
        dirs.sort()
        for n in dirs:
            p = Path(base)/n
            if p.is_symlink():
                errors.append({'type':'directory_symlink', 'path':str(p)})
        for n in sorted(names):
            ans.append(Path(base)/n)
    return ans


def digest(p):
    p = Path(p)
    if p.is_symlink() or not p.is_file():
        errors.append({'type':'not_regular_file', 'path':str(p)})
        return None
    st = p.stat()
    signature = (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)
    read_signatures[p] = signature
    if (p, signature) in cache:
        return cache[p, signature]
    h = hashlib.sha256()
    with p.open('rb') as f:
        while block := f.read(1024*1024):
            h.update(block)
    after = p.stat()
    if signature != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns):
        unstable.append(str(p))
    value = h.hexdigest()
    cache[p, signature] = value
    return value


def same(source, target, category):
    a, b = digest(source), digest(target)
    ans = {'category':category, 'source':str(source), 'target':str(target),
           'source_sha256':a, 'target_sha256':b, 'matches':a is not None and a == b}
    if not ans['matches']:
        errors.append({'type':'copy_mismatch', **ans})
    return ans


def parse_hashes(path, parent):
    ans = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64}) [ *](.+)', line)
        if not match:
            errors.append({'type':'unparsed_hash_line','path':str(path),'line':line})
            continue
        checksum, name = match.groups()
        target = (parent/name).resolve()
        if not target.is_relative_to(parent.resolve()) or target == parent.resolve():
            errors.append({'type':'unsafe_hash_path','path':str(path),'name':name})
            continue
        relative = str(target.relative_to(parent.resolve()))
        if relative in ans:
            errors.append({'type':'duplicate_hash_path','path':str(path),'name':name})
        ans[relative] = checksum
    return ans


manifest_path = art/'MANIFEST.sha256'
manifest_before = digest(manifest_path)
manifest = parse_hashes(manifest_path, art)
manifest_checks = []
for rel, expected in sorted(manifest.items()):
    actual = digest(art/rel)
    row = {'path':rel, 'expected':expected, 'actual':actual, 'matches':expected == actual}
    manifest_checks.append(row)
    if not row['matches']:
        errors.append({'type':'manifest_mismatch', **row})
actual_files = {str(p.relative_to(art)) for p in files(art) if p != manifest_path}
missing_entries = sorted(actual_files-set(manifest))
missing_files = sorted(set(manifest)-actual_files)
if missing_entries or missing_files:
    errors.append({'type':'manifest_inventory', 'unlisted_files':missing_entries, 'absent_files':missing_files})

copies = []
copies.append(same(lead/'S2_THEORY_18H_REPORT.md',lead/'FINAL_REPORT.md','main_report'))
companions = ['S2_L2_THEORY.md','S2_CALPHA_THEORY.md','S2_C_FUNCTIONAL.md',
              'S2_BASIS_CERTIFICATION.md','S2_NUMERICAL_CERTIFICATES.md','S2_CLOSURE.md','S2_RESTART.md','SPEC.md']
for name in companions:
    copies.append(same(lead/name, art/name, 'lead_companion'))
for name in ['VERIFY_REPORT.md','FINAL_VERIFICATION.md','THEOREM_MAP.md']:
    copies.append(same(ROOT/name, art/'verification'/name, 'verifier_handoff'))
for tree in ['code','certificates']:
    for p in files(ROOT/tree):
        if p == out:
            continue
        copies.append(same(p, art/'verification'/p.relative_to(ROOT), 'verifier_'+tree))

proof_root = ROOT/'proofs'
proof_files = files(proof_root)
small = [p for p in proof_files if p.stat().st_size <= 2097152]
large = [p for p in proof_files if p.stat().st_size > 2097152]
for p in small:
    copies.append(same(p, art/'verification/proofs'/p.relative_to(proof_root), 'verifier_proof'))
large_hash_path = art/'verification/LARGE_EVIDENCE_NOT_COPIED.sha256'
large_size_path = art/'verification/LARGE_EVIDENCE_NOT_COPIED.sizes'
large_listed = parse_hashes(large_hash_path, proof_root)
large_sizes = {}
for line in large_size_path.read_text().splitlines():
    n, name = line.split('\t', 1)
    rel = str(Path(name))
    large_sizes[rel] = int(n)
expected_large = {str(p.relative_to(proof_root)) for p in large}
if set(large_listed) != expected_large or set(large_sizes) != expected_large:
    errors.append({'type':'omission_inventory', 'expected':sorted(expected_large),
                   'hash_list':sorted(large_listed), 'size_list':sorted(large_sizes)})
omissions = []
for p in large:
    rel = str(p.relative_to(proof_root))
    row = {'path':rel,'bytes':p.stat().st_size,'actual_sha256':digest(p),
           'listed_sha256':large_listed.get(rel),'listed_bytes':large_sizes.get(rel),
           'absent_from_package':not (art/'verification/proofs'/rel).exists()}
    row['matches'] = (row['actual_sha256'] == row['listed_sha256'] and row['bytes'] == row['listed_bytes']
                      and row['absent_from_package'])
    omissions.append(row)
    if not row['matches']:
        errors.append({'type':'omission_mismatch', **row})
package_proof_names = {str(p.relative_to(art/'verification/proofs')) for p in files(art/'verification/proofs')}
small_names = {str(p.relative_to(proof_root)) for p in small}
if package_proof_names != small_names:
    errors.append({'type':'proof_inventory', 'unexpected':sorted(package_proof_names-small_names),
                   'missing':sorted(small_names-package_proof_names)})

for p in files(num/'artifacts'):
    copies.append(same(p,art/'numerics/artifacts'/p.relative_to(num/'artifacts'),'numerics_artifact'))
for name in ['NUM_REPORT.md','S2_BASIS_CERTIFICATION.md','S2_NUMERICAL_CERTIFICATES.md','S2_RESTART.md']:
    copies.append(same(num/name,art/'numerics'/name,'numerics_report'))
for p in sorted((lead/'work/audit').glob('*.md')):
    copies.append(same(p,art/'theory_notes/audit'/p.name,'lead_audit'))

HASH = re.compile(r'^[0-9a-f]{64}$')
relations = []
records = []
topics = []


def resolve_dependency(key):
    p = Path(key)
    if p.is_absolute():
        return p
    for p in [ROOT/key, ROOT/'proofs'/key]:
        if p.is_file():
            return p
        if p.is_dir() and (p/'PROOF.md').is_file():
            return p/'PROOF.md'
    return ROOT/key


def relation(record, key, path, expected):
    actual = digest(path)
    row = {'record':str(record.relative_to(ROOT)), 'key':key,'path':str(path),
           'expected':expected,'actual':actual,'matches':actual==expected}
    relations.append(row)
    if not row['matches']:
        errors.append({'type':'audit_dependency_mismatch', **row})


for d in sorted(proof_root.iterdir()):
    if not d.is_dir() or not re.match(r'^\d+_', d.name):
        continue
    topics.append({'topic':d.name,'proof_sha256':digest(d/'PROOF.md'),
                   'binding_sidecars':[p.name for p in sorted(d.glob('AUDIT*.md'))]})
    for name in ['audit_record.json','final_audit.json','derivation.json','correction_record.json']:
        rp = d/'evidence'/name
        if not rp.is_file():
            continue
        j = json.loads(rp.read_text())
        records.append({'path':str(rp.relative_to(ROOT)),'sha256':digest(rp)})
        for key, dest in [('proof_sha256','PROOF.md'),('clarification_sha256','AUDIT_CLARIFICATIONS.md'),
                          ('clarifications_sha256','AUDIT_CLARIFICATIONS.md'),('correction_sha256','AUDIT_CORRECTION.md'),
                          ('adoption_sha256','AUDIT_ADOPTION.md')]:
            if HASH.fullmatch(str(j.get(key,''))):
                relation(rp,key,d/dest,j[key])
        if j.get('audit_file') and HASH.fullmatch(str(j.get('audit_sha256',''))):
            relation(rp,'audit_sha256',resolve_dependency(j['audit_file']),j['audit_sha256'])
        for key in ['files','dependencies','extra_dependencies','additional_dependencies']:
            ds = j.get(key,{})
            if not isinstance(ds,dict):
                continue
            for k,h in ds.items():
                if isinstance(k,str) and isinstance(h,str) and HASH.fullmatch(h):
                    relation(rp,key+':'+k,resolve_dependency(k),h)
        ds = j.get('original_source',{})
        if isinstance(ds,dict) and ds.get('path') and HASH.fullmatch(str(ds.get('sha256',''))):
            relation(rp,'original_source',resolve_dependency(ds['path']),ds['sha256'])
links = []
for rp in [ROOT/'FINAL_VERIFICATION.md',ROOT/'THEOREM_MAP.md',proof_root/'INDEX.md']:
    for target in re.findall(r'\]\(([^)]+)\)',rp.read_text()):
        if ':' in target or target.startswith('#'):
            continue
        p = (rp.parent/target.split('#')[0]).resolve()
        row = {'record':str(rp.relative_to(ROOT)),'target':target,'exists':p.exists()}
        links.append(row)
        if not row['exists']:
            errors.append({'type':'missing_handoff_link', **row})
manifest_after = digest(manifest_path)
if manifest_before != manifest_after:
    errors.append({'type':'manifest_changed_during_check','before':manifest_before,'after':manifest_after})
for p, signature in read_signatures.items():
    try:
        st = p.stat()
        current = (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)
    except FileNotFoundError:
        current = None
    if current != signature:
        unstable.append(str(p))
for p in sorted(set(unstable)):
    errors.append({'type':'file_changed_during_read','path':p})
finished = datetime.now(timezone.utc)
answer = {'started_utc':started.isoformat(),'finished_utc':finished.isoformat(),
          'seconds':time.monotonic()-tick,'script_sha256':digest(Path(__file__)),
          'method':'Local read-only SHA256 and byte-count snapshot. No proof or numerical code executed. No claim that external sources or omitted caches are included. No statement about later edits. The certificate being written is not part of its own input inventory.',
          'manifest_before':manifest_before,'manifest_after':manifest_after,
          'counts':{'manifest_files':len(manifest_checks),'copied_files':len(copies),'small_proof_files':len(small),
                    'omitted_large_proof_files':len(large),'proof_topics':len(topics),'audit_records':len(records),
                    'explicit_hash_relations':len(relations),'handoff_links':len(links),'errors':len(errors)},
          'all_checks_pass':not errors,'errors':errors,'manifest_checks':manifest_checks,'copy_checks':copies,
          'omissions':omissions,'proof_topics':topics,'audit_records':records,'audit_hash_checks':relations,'links':links}
out.write_text(json.dumps(answer,indent=2)+'\n')
print(json.dumps({'output':str(out.relative_to(ROOT)),'sha256':digest(out),
                  'started':answer['started_utc'],'finished':answer['finished_utc'],'seconds':answer['seconds'],
                  'counts':answer['counts'],'all_checks_pass':answer['all_checks_pass'],'errors':errors[:20]},indent=2))
