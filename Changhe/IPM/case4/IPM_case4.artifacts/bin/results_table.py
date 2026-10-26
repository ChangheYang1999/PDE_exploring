#!/usr/bin/env python3
"""Markdown result table from a gate JSON: results_table.py <gate.json> [prefix]"""
import json, sys
d = json.load(open(sys.argv[1])); prefix = sys.argv[2] if len(sys.argv) > 2 else ''
print('| check | value | tolerance | result |\n|---|---:|---:|---|')
for c in d['checks']:
    if not c['check'].startswith(prefix): continue
    v = c['value']; vs = ('%.3e' % v) if isinstance(v, float) else str(v); ts = ('%.1e' % c['tolerance']) if c['tolerance'] is not None else 'boolean'
    print('| %s | %s | %s | %s |' % (c['check'], vs, ts, 'PASS' if c['passed'] else 'FAIL'))
print('\npassed: %s; manifest %s; began %s; finished %s' % (d.get('passed'), d.get('code_manifest_sha256', '')[:16], d.get('began_utc'), d.get('finished_utc')))
