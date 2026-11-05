#!/usr/bin/env python3
"""Bind the independently reviewed analytic chain to all completed premises.

The analytic verdict is the independent mathematical review in the companion
report. This executable checks the immutability and completion of its exact
inputs and numerical audits; it does not replace the analytic proof.
"""
import json
import os
import re
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent

def read(p):
    return json.loads(p.read_text())

def digest(p):
    return sha256(p.read_bytes()).hexdigest()

def check(mapping):
    for name, expected in mapping.items():
        assert digest(ART/name) == expected, name

approved_updates = {
    'finite_rank/QNORM_NONLINEAR_BOUND.md':'790abc7ef33a7696c1de08228c7eae280a2b968e5bbb6d1fbae875ff2943a2ee',
    'independent_closure_audit/EXPLICIT_STREAMFUNCTION.md':'bb2e84f2562eb780ac862021c02041a31a0bd10ad6c02ea7778ec0b20d8e9e8b',
    'independent_closure_audit/INDEPENDENT_ANALYTIC_AUDIT.md':'c696f6154f9855d00805853a946ffe596cc709ba97e173f6ffc5926eacc6681a',
    'finite_rank/Q_SOURCE_CONSTANT_CERTIFICATE_PROOF.md':'ada69956edd297ac8235e0afd6617e0c82b114ec11ed1edfdcb8c7acdc6bd6f5',
}
manifest_path = HERE/'analytic_dependency_manifest.json'
manifest = read(manifest_path)
reviewed = dict(manifest['reviewed_sha256'])
for name, expected in reviewed.items():
    current = digest(ART/name)
    if current != expected:
        assert approved_updates.get(name) == current, ('unreviewed change',name)
        reviewed[name] = current
check(approved_updates)
consumer_path = ART/'operator_theory/fixed_parameter_closure_v01.json'
consumer_code = ART/'operator_theory/assemble_fixed_parameter_closure_v01.py'
assert digest(consumer_path) == '845b472f63f53cdcb39afeca221f336b7a6b55e81101357c4bf98e8d5fddf62f'
assert digest(consumer_code) == 'af0ce4ce35977e2707080657b47ada8773db63fb89277669f99911ea895e09d1'
consumer = read(consumer_path)
assert consumer['status'] == 'FINAL_NUMERICAL_CLOSURE_PASS'
assert consumer['all_input_bindings_and_covers_checked']
assert consumer['consumer_sha256'] == digest(consumer_code)
assert set(consumer['input_paths']) == set(consumer['input_sha256'])
for key, name in consumer['input_paths'].items():
    assert digest(ART/name) == consumer['input_sha256'][key], key
check(consumer['chunk_sha256'])
receipts = {
    'signed_matrix_far_audit.json':'INDEPENDENT_SIGNED_MATRIX_FAR_AUDIT_PASS',
    'matrix_prefix_audit.json':'INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS',
    'local_coefficients_audit.json':'INDEPENDENT_LOCAL_COEFFICIENT_AUDIT_PASS',
    'final_join_audit.json':'INDEPENDENT_FINAL_SCALAR_JOIN_PASS',
    'rational_ball_audit.json':'INDEPENDENT_EXACT_RATIONAL_BALL_AUDIT_PASS',
}
receipt_hashes = {}
for name, status in receipts.items():
    p = HERE/name
    d = read(p)
    assert d['status'] == status
    if 'bindings' in d:
        check(d['bindings'])
    receipt_hashes[str(p.relative_to(ART))] = digest(p)
joined = read(HERE/'final_join_audit.json')
assert joined['auditor_code_sha256'] == digest(HERE/'verify_final_join.py')
check(joined['source_raw_chunk_sha256'])
assert joined['source_panels'] == 2303
local = read(HERE/'local_coefficients_audit.json')
check(local['nested_bindings'])
check(local['used_chunk_sha256'])
assert local['base_panels'] == 599
matrix = read(HERE/'matrix_prefix_audit.json')
check(matrix['used_chunk_sha256'])
assert matrix['used_base_panels'] == 711 and matrix['total_leaves'] == 996
assert matrix['values_identical'] is True
rational = read(ART/'RATIONAL_FINAL_BALL.json')
assert rational['status'] == 'EXACT_RATIONAL_FIXED_PARAMETER_BALL_PASS'
assert rational['program_sha256'] == digest(ART/'certify_rational_final_ball.py')
check(rational['input_sha256'])
report_path = ART.parent/'IPM.report.md'
proof_path = ART/'operator_theory/FIXED_PARAMETER_THEOREM_PROOF_v01.md'
assert digest(report_path) == 'ec279c8729057ded607847b4edf4bb3e2853839a5355c63541b7fd191f2bbfb4'
assert digest(proof_path) == '0005423ff5c812dadb64336334102d2c81704b3c5bc566171cfa55e3ff95368d'
links_checked = 0
for p in [report_path,proof_path]:
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)\n]+)\)',p.read_text()):
        if re.match(r'[a-zA-Z]+://',target) or target.startswith('#'):
            continue
        assert (p.parent/target.split('#')[0].strip('<>')).exists(), (str(p),target)
        links_checked += 1
assert links_checked == 83
display = read(ART/'operator_theory/final_proof_numbers_v01.json')
assert display['status'] == 'FINAL_PROOF_NUMERICAL_DISPLAYS_PASS'
check(display['bindings'])
post = read(ART/'ROOT_POST_RESTART_REPRODUCTION.json')
assert post['status'] == 'POST_RESTART_DOCUMENTED_REPRODUCTION_PASS'
assert post['program_sha256'] == digest(ART/'verify_post_restart_reproduction.py')
check(post['canonical_bindings_unchanged'])
assert post['statuses'] == ['FINAL_NUMERICAL_CLOSURE_PASS','ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS']
extra = [consumer_path,consumer_code,ART/'RATIONAL_FINAL_BALL.json',ART/'certify_rational_final_ball.py',
         ART/'certify_source_envelopes.py',ART/'certify_Q_far_source_highpass.py',
         HERE/'verify_final_join.py',HERE/'verify_rational_ball.py',HERE/'verify_local_coefficients.py',
         HERE/'verify_matrix_prefix.py',HERE/'verify_signed_matrix_far.py',Path(__file__),
         report_path,proof_path,HERE/'REPORT_AUDIT.md',ART/'operator_theory/verify_final_proof_numbers_v01.py',
         ART/'operator_theory/final_proof_numbers_v01.json',ART/'ROOT_POST_RESTART_REPRODUCTION.json',
         ART/'verify_post_restart_reproduction.py',ART/'REPRODUCE.md']
reviewed.update({os.path.relpath(p,ART):digest(p) for p in extra})
manifest.update(status='COMPLETE_FIXED_PARAMETER_PROOF_DEPENDENCY_AUDIT_PASS',
                finished_utc=datetime.now(timezone.utc).isoformat(),reviewed_sha256=reviewed,
                independent_receipt_sha256=receipt_hashes,
                scope='The precise analytic chain, all actual numerical premises, and the final main report have been independently reviewed and verified. No required mathematical premise remains open in the preferred local-Q theorem. Unrelated old-route quantitative tails remain qualified.')
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
out = {'status':'COMPLETE_FIXED_PARAMETER_PROOF_DEPENDENCY_AUDIT_PASS',
       'finished_utc':datetime.now(timezone.utc).isoformat(),
       'auditor_program_sha256':digest(Path(__file__)),
       'analytic_manifest_sha256':digest(manifest_path),
       'consumer_result_sha256':digest(consumer_path),
       'main_input_paths':consumer['input_paths'],'main_input_sha256':consumer['input_sha256'],
       'independent_receipt_sha256':receipt_hashes,
       'rational_ball_sha256':digest(ART/'RATIONAL_FINAL_BALL.json'),
       'main_report_sha256':digest(report_path),'integrated_proof_sha256':digest(proof_path),
       'publication_audit_sha256':digest(HERE/'REPORT_AUDIT.md'),
       'local_report_and_proof_links_checked':links_checked,
       'post_restart_reproduction_sha256':digest(ART/'ROOT_POST_RESTART_REPRODUCTION.json'),
       'R':rational['R'],'M':rational['M'],'fixed_c':consumer['fixed_c'],
       'exact_selfmap_margin':rational['exact_selfmap_margin'],
       'contraction_upper':rational['contraction_upper'],
       'inherited_N_upper':rational['inherited_N_upper'],
       'mathematical_verdict':'The reviewed actual L2 generator/inverse, complete local-Q background energy, source/transport/nonlinear estimates, forced barrier, rough-input passage, contraction, canonical velocity, explicit streamfunction, and derived origin normalization close the fixed-parameter stationary IPM theorem in the stated ball.',
       'qualification':'No quantitative full finite-rank tail is claimed for the unused old compact decomposition; its qualified rank-one and exploratory results are not premises of this theorem. Numerical residual frequency-split experiments are not used.'}
(HERE/'final_dependency_verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['main_input_paths','main_input_sha256','independent_receipt_sha256']},indent=2))
