"""Static Markdown navigation inspection. No project modules are imported."""
import argparse
from collections import Counter, deque
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

BASE = Path('bot_research/experiments/validation')
OUT = BASE / 'reviews/final_navigation_001'
ANALYSIS = BASE / 'analysis'
ROOT_INDEX = ANALYSIS / 'README.md'
SKIP_PARTS = {'verification', 'inputs', 'archives', 'source_snapshots', 'sources'}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.now(timezone.utc).isoformat()

def visible_markdown(text):
    lines = text.splitlines(keepends=True)
    result = []
    fence = None
    for line in lines:
        m = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if m:
            marker = m.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            result.append(' ' * (len(line.rstrip('\n'))) + ('\n' if line.endswith('\n') else ''))
            continue
        if fence is not None:
            result.append(' ' * (len(line.rstrip('\n'))) + ('\n' if line.endswith('\n') else ''))
            continue
        result.append(re.sub(r'(`+)(.*?)\1', lambda m: ' ' * len(m.group(0)), line))
    return ''.join(result)

def links(text):
    clean = visible_markdown(text)
    definitions = {}
    for m in re.finditer(r'^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', clean, re.M):
        definitions[' '.join(m.group(1).lower().split())] = m.group(2).strip('<>')
    found = []
    inline_spans = []
    for m in re.finditer(r'!?\[([^\]\n]*)\]\(', clean):
        start = m.end()
        depth = 1
        i = start
        angle = i < len(clean) and clean[i] == '<'
        while i < len(clean) and depth:
            if clean[i] == '\\':
                i += 2
                continue
            if clean[i] == '(':
                depth += 1
            elif clean[i] == ')':
                depth -= 1
            i += 1
        if depth:
            continue
        body = clean[start:i - 1].strip()
        if body.startswith('<') and '>' in body:
            dest = body[1:body.index('>')]
        else:
            dest = body.split()[0] if body else ''
        found.append((clean.count('\n', 0, m.start()) + 1, m.group(1), dest, 'inline'))
        inline_spans.append((m.start(), i))
    for m in re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', clean):
        key = ' '.join((m.group(2) or m.group(1)).lower().split())
        if key in definitions:
            found.append((clean.count('\n', 0, m.start()) + 1, m.group(1), definitions[key], 'reference'))
    # No shortcut reference links occur in the current inputs; record definitions for scope.
    return sorted(found), len(definitions)

def anchors(text):
    counts = Counter()
    result = set(re.findall(r'<a\s+(?:name|id)=[\"\']([^\"\']+)[\"\']', text, flags=re.I))
    for line in text.splitlines():
        m = re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not m:
            continue
        title = re.sub(r'<[^>]+>', '', m.group(1)).lower()
        title = re.sub(r'[^\w\-\s]', '', title)
        slug = re.sub(r'\s', '-', title)
        n = counts[slug]
        counts[slug] += 1
        result.add(slug if n == 0 else f'{slug}-{n}')
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args()
    assert os.sched_getaffinity(0) == {28}
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 19
    assert sys.dont_write_bytecode and not sys.flags.optimize
    for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        assert os.environ.get(key) == '1'
    assert (Path.cwd() / '.venv/bin/python').exists()
    assert Path(os.environ['TMPDIR']).resolve() == (Path.cwd() / 'bot_research/tmp').resolve()
    destination = OUT / args.name
    destination.mkdir(exist_ok=False)
    archive = destination / 'inputs'
    archive.mkdir()
    started = stamp()
    inventory = subprocess.run(['rg', '--files', str(ANALYSIS), '-g', '*.md'], check=True, capture_output=True, text=True).stdout.splitlines()
    eligible = [Path(p) for p in inventory if not SKIP_PARTS.intersection(Path(p).relative_to(ANALYSIS).parts)]
    extra_roots = [BASE / 'reviews/frr3_extension_review_001/INDEX.md', BASE / 'reviews/frr3_extension_review_001/PROOF.md', BASE / 'reviews/frr5_frr6_final_fortress_001/README.md', BASE / 'reviews/frr5_frr6_final_fortress_001/finite_matrix_extension/INDEX.md']
    queue = deque(sorted(set(eligible + extra_roots)))
    documents = {}
    edges = []
    external = []
    non_markdown_targets = {}
    ref_count = 0
    while queue:
        path = queue.popleft()
        if str(path) in documents:
            continue
        data = path.read_bytes()
        text = data.decode('utf-8')
        compressed = gzip.compress(data, mtime=0)
        archive_path = archive / (digest(data) + '.gz')
        if not archive_path.exists():
            archive_path.write_bytes(compressed)
        parsed, refs = links(text)
        ref_count += refs
        documents[str(path)] = {'sha256': digest(data), 'bytes': len(data), 'archive': str(archive_path), 'archive_sha256': digest(compressed), 'headings': [s for s in text.splitlines() if re.match(r'^#{1,6}\s', s)], 'anchors': sorted(anchors(text)), 'local_links': 0, 'text': text}
        for line, label, target, kind in parsed:
            split = urlsplit(target)
            if split.scheme or split.netloc:
                external.append({'source': str(path), 'line': line, 'target': target})
                continue
            dest_raw = unquote(split.path)
            if dest_raw.startswith('/'):
                resolved = Path(dest_raw.lstrip('/'))
                interpretation = 'repository-root-relative'
            else:
                resolved = Path(os.path.normpath(str(path.parent / dest_raw))) if dest_raw else path
                interpretation = 'source-relative'
            outside = resolved.is_absolute() or '..' in resolved.parts
            exists = (not outside) and resolved.exists()
            entry = {'source': str(path), 'line': line, 'label': label, 'target': target, 'resolved': str(resolved), 'fragment': unquote(split.fragment), 'kind': kind, 'interpretation': interpretation, 'exists': exists, 'outside_project': outside}
            edges.append(entry)
            documents[str(path)]['local_links'] += 1
            if exists and resolved.is_file() and resolved.suffix.lower() == '.md':
                queue.append(resolved)
            elif exists:
                non_markdown_targets[str(resolved)] = {'kind': 'directory' if resolved.is_dir() else 'file', 'bytes': resolved.stat().st_size if resolved.is_file() else None}
    for edge in edges:
        if edge['fragment'] and edge['resolved'] in documents:
            edge['anchor_exists'] = edge['fragment'] in documents[edge['resolved']]['anchors']
        else:
            edge['anchor_exists'] = None
    graph = {}
    for edge in edges:
        if edge['exists'] and edge['resolved'] in documents:
            graph.setdefault(edge['source'], set()).add(edge['resolved'])
    reached = set()
    todo = [str(ROOT_INDEX)]
    while todo:
        path = todo.pop()
        if path not in reached:
            reached.add(path)
            todo.extend(graph.get(path, set()) - reached)
    root_edges = [e for e in edges if e['source'] == str(ROOT_INDEX)]
    proof_paths = sorted(p for p in documents if Path(p).name == 'PROOF.md')
    result_paths = sorted(p for p in documents if Path(p).name == 'RESULTS.md')
    unreachable_proofs = [p for p in proof_paths if p not in reached]
    unreachable_results = [p for p in result_paths if p not in reached]
    status_excerpts = []
    for path, doc in documents.items():
        if Path(path).name in {'README.md', 'INDEX.md'}:
            for n, line in enumerate(doc['text'].splitlines(), 1):
                if re.search(r'\b(?:OPEN|pending|future work|prepar|no .*result|not yet)\b', line, flags=re.I):
                    status_excerpts.append({'path': path, 'line': n, 'text': line})
    top_level_targets = sorted({e['resolved'] for e in root_edges if e['exists'] and e['resolved'] in documents})
    summary = {
        'schema': 'static-navigation-inspection-001', 'started_utc': started, 'completed_utc': stamp(),
        'model': 'GPT-6 Astra', 'role': 'independent source-only navigation reviewer',
        'scope': {'root': str(ROOT_INDEX), 'all_current_analysis_markdown': True, 'analysis_excluded_path_components': sorted(SKIP_PARTS), 'extra_roots': [str(p) for p in extra_roots], 'recursive_following': 'existing local Markdown targets only', 'non_markdown_targets': 'existence and file size only; contents not read', 'anchor_method': 'ATX headings and explicit HTML name/id anchors; not a full CommonMark renderer', 'reference_method': 'inline and explicit reference links; fenced code and inline code excluded', 'not_performed': ['policy calls', 'Engine calls', 'games', 'replays', 'tests', 'data authentication', 'new mathematical proofs', 'strength evaluation']},
        'counts': {'initial_analysis_markdown_inventory': len(inventory), 'eligible_current_analysis_markdown': len(eligible), 'documents_read_and_archived': len(documents), 'root_local_links': len(root_edges), 'root_distinct_markdown_targets': len(top_level_targets), 'local_link_occurrences': len(edges), 'external_link_occurrences_not_checked': len(external), 'reference_definitions': ref_count, 'non_markdown_targets_checked_for_existence': len(non_markdown_targets), 'missing_local_targets': sum(not e['exists'] for e in edges), 'missing_atx_or_explicit_anchors': sum(e.get('anchor_exists') is False for e in edges), 'markdown_documents_reachable_from_root': len(reached), 'standalone_proofs': len(proof_paths), 'standalone_proofs_unreachable_from_root': len(unreachable_proofs), 'result_pages': len(result_paths), 'result_pages_unreachable_from_root': len(unreachable_results)},
        'root_distinct_markdown_targets': top_level_targets, 'missing_links': [e for e in edges if not e['exists']], 'missing_anchors': [e for e in edges if e.get('anchor_exists') is False], 'unreachable_proofs': unreachable_proofs, 'unreachable_results': unreachable_results, 'historical_status_excerpts': status_excerpts,
        'input_documents': {p: {k: v for k, v in d.items() if k != 'text'} for p, d in sorted(documents.items())},
        'edges': edges, 'non_markdown_target_existence': non_markdown_targets, 'external_links_not_checked': external,
    }
    raw = json.dumps(summary, indent=2, sort_keys=True).encode() + b'\n'
    result_path = destination / 'INSPECTION.json'
    result_path.write_bytes(raw)
    print(json.dumps({'inspection': str(result_path), 'sha256': digest(raw), 'counts': summary['counts'], 'unreachable_proofs': unreachable_proofs, 'missing_links': summary['missing_links'], 'missing_anchors': summary['missing_anchors']}, indent=2))

if __name__ == '__main__':
    main()
