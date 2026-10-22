"""Exact public-bound and final primary evidence linkage, separate from the frozen core."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,ast
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from importlib.metadata import version
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/middle_residual/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
 audit=load(E/'full_q16_output_audit.json');summary=load(E/'full_q16_summary.json');public=load(E/'primary_completion_summary.json');ka=load(E/'knot_audit.json');sp=load(E/'setup_provenance.json')
 assert audit['status']=='PASS' and audit['cells_audited']==7809 and summary['status']=='COMPUTED_REQUIRES_INDEPENDENT_OUTPUT_AUDIT' and summary['source_footer_read'] is True
 assert summary['cells_complete']==summary['cells_required']==7809 and summary['run_header']==audit['run_header']
 assert public['output_audit_sha256']==sha(E/'full_q16_output_audit.json') and public['output_sha256']==audit['completed_output_sha256']==sha(E/'full_q16_cells.jsonl')
 assert audit['summary_sha256']==sha(E/'full_q16_summary.json')
 assert audit['source_sha256']==sha(B/'research/middle_residual/code/audit_full_output.py')
 fixture=load(E/'nonfinite_guard_checks.json');assert fixture['status']=='PASS' and fixture['auditor_sha256']==audit['source_sha256'] and fixture['source_sha256']==sha(B/'research/middle_residual/code/check_output_nonfinite.py')
 assert audit['run_header']['partition_sha256']==ka['partition_sha256']==sha(E/'partition_exact.json') and ka['footer_read'] is True
 assert ka['archive_sha256']==audit['run_header']['knot_input_sha256']==sha(E/'original_knots.jsonl.gz')
 assert ka['source_sha256']==sha(B/'research/middle_residual/code/audit_knots.py')
 width=F(ka['minimum_child_width_exact']);span=F(ka['maximum_parent_width_exact'])
 assert [F(v['z_exact']) for v in ka['moment_argument_endpoint_checks']]==[width,-width,526*span,-526*span]
 assert all(v['minimum_accuracy_bits']>200 for v in ka['moment_argument_endpoint_checks'])
 assert sp['status']=='PASS' and sp['setup_body_identical_to_confirmed_sample_source'] is True
 for rel,h in sp['hashes'].items():assert sha(B/rel)==h
 assert {k:version(k) for k in sp['versions']}==sp['versions']==audit['library_versions']
 original=(B/'research/residual_samples/code/certify_samples.py').read_text();extracted=(B/'research/middle_residual/code/modal_setup.py').read_text()
 setup_body=extracted.split('def setup():\n',1)[1].split(' return dict(',1)[0]
 sample_body=original.split('def main():\n',1)[1].split(" path=BASE/'data_exact/modal_v2.json'",1)[1].split(' # The comparison artifact',1)[0]
 sample_body=" path=BASE/'data_exact/modal_v2.json'"+sample_body
 assert setup_body==sample_body
 # Independently compare integers, including squared L2, never displayed decimals.
 bounds={'W_upper_exact':F('0.000134943'),'W_over_m_upper_exact':F('0.000291625'),'Wm_times_one_plus_u_power_half_upper_exact':F('0.000427591'),'Wm_times_one_plus_u_power_half_minus_k_upper_exact':F('0.000372741')}
 checks=[]
 for key,upper in bounds.items():
  exact=F(audit['maxima'][key]['upper']);assert exact<upper==F(public['public_strict_bounds'][key]);assert audit['maxima'][key]['cell']==4125
  checks.append({'quantity':key,'audited_upper_exact':str(exact),'strict_public_upper_exact':str(upper),'strict_gap_exact':str(upper-exact)})
 ul2=F('0.000523709');assert F(audit['L2_upper_exact'])<ul2==F(public['L2_strict_upper_exact']) and F(audit['L2_squared_upper_exact'])<ul2**2
 files=[Path(__file__),B/'research/middle_residual/PROOF.md',E/'full_q16_output_audit.json',E/'full_q16_summary.json',E/'full_q16_cells.jsonl',E/'primary_completion_summary.json',E/'knot_audit.json',E/'setup_provenance.json',E/'nonfinite_guard_checks.json',B/'research/middle_residual/code/audit_full_output.py',B/'research/middle_residual/code/check_output_nonfinite.py',E/'partition_exact.json',E/'original_knots.jsonl.gz']
 for rel in sp['hashes']:files.append(B/rel)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_PRIMARY_COMPLETION_LINKS_AND_PUBLIC_BOUNDS','source_sha256':sha(__file__),'strict_exact_comparisons':checks,'L2_strict_upper_exact':str(ul2),'L2_square_comparison':True,'primary_full_footer_confirmed':True,'exact_partition_and_canonical_archive_links':True,'setup_body_byte_identical':True,'moment_phi_526_span_gate_minimum_bits':min(v['minimum_accuracy_bits'] for v in ka['moment_argument_endpoint_checks']),'files':{str(p.relative_to(B)):sha(p) for p in sorted(set(files))},'scope':'Local executable source/output/public-bound checks. Primary computation accepted separately; full secondary coefficient regeneration OPEN. This audit does not regenerate coefficients or supply any PDE endpoint.'}
 (E/'primary_completion_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['files','strict_exact_comparisons']}))
if __name__=='__main__':main()
