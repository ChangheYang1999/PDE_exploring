"""Generic source-bound application of the audited exact center formula."""
from pathlib import Path
import argparse,json
from core_generating_mp import export_source,sha
from core_center_certificate import certify
ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--out',required=True);a=ap.parse_args()
out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
data=export_source(a.source,out/'input.json');c=certify(data)
c.update(input_sha256=sha(out/'input.json'),script_sha256=sha(__file__),pure_formula_sha256=sha('code/core_center_certificate.py'),importer_sha256=sha('code/core_generating_mp.py'),proof_sha256=sha('research/core_generating_center/PROOF.md'),patch_count=len(data['patches']))
(out/'certificate.json').write_text(json.dumps(c,indent=2)+'\n')
print(data['source'],'a_center',c['a_center']['display'] if c['a_center'] else None,'D',c['D']['display'],'prompt',c['ratios']['prompt']['display'] if c['ratios']['prompt'] else None,flush=True)
