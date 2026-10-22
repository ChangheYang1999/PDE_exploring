from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
P=Path('research/330_numerics_wording_rebase');V=P/'verification';src=Path('code_independent/rebase_numerics_wording.py')
for a,b in [(src,V/'checker_before_review.py'),(V/'checks.json',V/'checks_before_review.json'),(P/'PROOF.md',V/'proof_before_review.md'),(V/'freeze.json',V/'freeze_before_review.json')]:
 if not b.exists():b.write_bytes(a.read_bytes())
s=src.read_text().replace('covering119','covering 119').replace('# Independently replay the exact recorded replacements, confined to file mappings.','# Replay the recorded replacements as a determinism/preservation check, not an independent correctness proof.')
needle="for i,d in enumerate(fix316):out['artifacts/README.md']=replace(out['artifacts/README.md'],d['old'],d['new'],f'P316_{i}')"
s=s.replace(needle,needle+"\n# Further count clarification, with the old 95-entry historical count retained.\nout['artifacts/README.md']=replace(out['artifacts/README.md'],'123 states','123 audit entries', 'README_entry_count',count=2,white=False)\n# Keep the generated header's original line boundaries.\nfor i,(old,new) in enumerate([('13630-18144 points, with 145','13630-18144 points,\\nwith 145'),('mathematically distinct field. None','mathematically distinct field.\\nNone')]):\n out['artifacts/consolidated_residuals.md']=replace(out['artifacts/consolidated_residuals.md'],old,new,f'MD_line_boundary_{i}',white=False)")
s=s.replace("elif tag=='new_header_count':p='NUM_REPORT.md'","elif tag=='new_header_count':p='NUM_REPORT.md'\n elif tag=='README_entry_count':p='artifacts/README.md'\n elif tag.startswith('MD_line_boundary_'):p='artifacts/consolidated_residuals.md'")
s=s.replace("ck('artifact_README_equals_P316_approved',out['artifacts/README.md']==Path('research/316_portable_residual_package/verification/approved_README.md').read_text())","ck('artifact_README_equals_P316_plus_count_clarification',out['artifacts/README.md']==Path('research/316_portable_residual_package/verification/approved_README.md').read_text().replace('123 states','123 audit entries'))")
s=s.replace("ck('artifact_MD_equals_P313_approved',out['artifacts/consolidated_residuals.md']==Path('research/313_consolidated_123_state_audit/verification/approved_consolidated_residuals.md').read_text())","ck('artifact_MD_equals_P313_modulo_line_reflow',norm(out['artifacts/consolidated_residuals.md'])==norm(Path('research/313_consolidated_123_state_audit/verification/approved_consolidated_residuals.md').read_text()))")
anchor="ck('manifest_only_one_changed_line'"
addition='''# Decode only the literal header data, not the program. All unsupported AST nodes fail closed.
def header_data(source):
 tree=ast.parse(source); assignments={z.targets[0].id:z.value for z in tree.body if isinstance(z,ast.Assign) and len(z.targets)==1 and isinstance(z.targets[0],ast.Name)}
 reg=assignments['REG_NAMES']; assert isinstance(reg,ast.List)
 regions=[]
 for z in reg.elts:
  assert isinstance(z,ast.Constant) and isinstance(z.value,str); regions.append(z.value)
 def literal(z):
  if isinstance(z,ast.Constant) and isinstance(z.value,str):return z.value
  if isinstance(z,ast.BinOp) and isinstance(z.op,ast.Add):return literal(z.left)+literal(z.right)
  if isinstance(z,ast.Call) and isinstance(z.func,ast.Attribute) and z.func.attr=='join' and isinstance(z.func.value,ast.Constant) and z.func.value.value==', ' and len(z.args)==1 and isinstance(z.args[0],ast.Name) and z.args[0].id=='REG_NAMES' and not z.keywords:return ', '.join(regions)
  raise ValueError(ast.dump(z))
 data=assignments['out']; assert isinstance(data,ast.List)
 return '\\n'.join(literal(z)for z in data.elts)+'\\n'
for label,files in [('frozen',base),('approved',out)]:
 for p in ['code/consolidate_audits.py','artifacts/consolidate_audits.py']:
  ck(label+'_'+p+'_literal_header_exact',header_data(files[p])==files['artifacts/consolidated_residuals.md'].split('## ',1)[0])
ck('header_timestamp_retained_as_historical','Last update of this header 2026-10-22 08:07Z.' in out['NUM_REPORT.md'])
ck('checksum_historical_timestamp_retained','code_sha256.txt refreshed 07:58Z.' in out['artifacts/README.md'])
'''
assert anchor in s;s=s.replace(anchor,addition+anchor)
src.write_text(s)
proof='''# Preservation criterion for the numerical report wording repairs

## Exact statement and dependencies
This packet prepares a coupled six-file adoption proposal: NUM_REPORT.md, artifacts/consolidated_residuals.md, artifacts/README.md, the code/ and artifacts/ copies of consolidate_audits.py, and artifacts/code_sha256.txt. The unchanged CSV is supplied for comparison only. P313 audited 123 keyed audit entries, 121 forced entries and two manufactured controls, covering 119 distinct coefficient archive hashes. Their evaluation sets have 145, 161, 166, 177 or 189 radii and field-dependent 13630 to 18144 points. P316 independently reconstructed all 5904 CSV rows using the artifact and runs input roots. Those completed data audits are dependencies, not repeated PDE evaluations here.

## Argument
A specified string replacement preserves every other byte if its old string has the recorded occurrence count and its target is exactly the original with those occurrences replaced. Comparing the resulting whole files and exact diffs checks that preservation claim. Replaying the same algorithm checks determinism only; it is not an independent proof of the correctness of the chosen wording. The factual justification instead comes from P313, P316 and inspection of the complete changed passages.

Apply the P313 count and grid repairs to the current frozen report, retaining later unrelated header and chronological-heading cleanup. Apply the P316 command-provenance, control and reconstruction-root repairs to the README; additionally describe its two 123-state counts as audit-entry counts. The new report header uses 123 entries covering 119 distinct hashes. A hash distinction is not a proof of mathematically distinct fields. The earlier 13920-point evaluations retain their own historical grid descriptions.

For both identical generator copies, change four header string literals only. The exact prefix, suffix and AST outside their one header assignment remain identical. Thus numerical loops, data resolution and CSV output instructions are preserved. Static parsing checks syntax without executing the generator. A separate whitelist parser reads only string constants, their concatenations, the explicit REG_NAMES string list and its separator. It rejects every other expression. This decodes the literal header data and proves its byte equality with the proposed Markdown header, including newlines. The reflow relative to the older P313 approved Markdown changes whitespace only.

The manifest proposal changes exactly the generator's one digest line to the hash of the proposed code/ source. Its validity is conditional on adopting that source together with the manifest and preserving all other code files. It is not a checksum assertion about the unchanged current NUM tree. Actual adoption and all current code hashes need a subsequent readback. The existing 08:07 header-update and 07:58 checksum-refresh timestamps are deliberately retained as historical events, not claimed preparation or adoption times. The adopter must record the actual later adoption and checksum refresh; this verifier cannot write that event in advance.

All Markdown table rows, README command lines and CSV bytes are preserved. Old numerical assertions remain refuted until actual adoption is observed. This proposal supplies a concrete repair, not evidence that another lane has applied it.

## Scope
No NUM code is imported or executed. No new inverse, PDE or solver evaluation, continuum accuracy, candidate existence, general nonexistence, completed run or actual adoption is asserted. Write only in verification. No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or external posts.
'''
now=datetime.now(timezone.utc).isoformat();(P/'PROOF.md').write_text('Revised '+now+', before revised controls. Initial proof retained in verification/proof_before_review.md.\n\n'+proof)
f=json.loads((V/'freeze.json').read_text());f['utc']=now;f['proof_sha256']=hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest();(V/'freeze.json').write_text(json.dumps(f,indent=2)+'\n')
