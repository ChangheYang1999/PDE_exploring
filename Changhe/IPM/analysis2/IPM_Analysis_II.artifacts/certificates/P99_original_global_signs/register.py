"""Register only the completed, independently checked target records named on argv."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import json,sys,subprocess
p=Path(__file__).resolve().parent;root=p.parents[2];sha=lambda x:sha256(x.read_bytes()).hexdigest();records=[];files={}
for name in sys.argv[1:]:
 src=p/name;a=json.loads(src.read_text());chk=src.with_name(src.stem+'.recheck.json');b=json.loads(chk.read_text());assert a['status']=='COMPLETE' and not a['failed'] and not a['pending_paths'];assert b['all_pass'] and b['primary_sha256']==sha(src);assert b['kind']==a['kind'] and b['target']==a['target'] and b['root_t']==a['root_t'];assert b['leaves']==len(a['accepted']);poly=root/'research/96_original_auxiliary_recomputation/verification/polynomials.json';assert a['source_sha256']==b['polynomials_sha256']==sha(poly);records.append({'file':name,'kind':a['kind'],'target':a['target'],'root_t':a['root_t'],'leaves':b['leaves']});files[name]=sha(src);files[chk.name]=sha(chk)
assert records
for name in ['compute.py','recheck.py']:files[name]=sha(p/name)
alg=root/'research/96_original_auxiliary_recomputation/verification/audit.json';basealg=json.loads(alg.read_text());assert basealg['all_pass'] and basealg['polynomials_sha256']==sha(poly);files['96_audit.json']=sha(alg);files['96_polynomials.json']=sha(poly)
now=datetime.now(timezone.utc).isoformat();a={'utc':now,'all_pass':True,'records':records,'files_sha256':files,'proof_sha256':sha(p.parent/'PROOF.md')};(p/'audit.json').write_text(json.dumps(a,indent=2)+'\n');(p/'AUDIT.md').write_text('# Audit\n\nOnly the named records in audit.json are registered. Each has a complete directed tree, no pending or failed cells, and an independent direct-power recheck at448bits. The exact original source is bound through the independently audited topic96 polynomials.\n')
parts=[]
for r in records:
 tl=F(r['root_t'][0]);th=F(r['root_t'][1]);domain='on the whole plane' if tl==0 and th==1 else f'on the compactified radial interval t in[{tl},{th}], t=r^2/(1+r^2)'
 if r['kind']=='A':statement=f'A >= -{r["target"]} I'
 elif r['kind']=='rho_scaled':statement=f'rho_y >= {r["target"]}(1+r^2)^(-delta/2)>0 at finite radius'
 elif r['kind']=='symDU':statement=f'||sym Du|| <= {r["target"]}'
 else:statement=f'{r["kind"]} >= {r["target"]} I'
 parts.append(statement+' '+domain+f' ({r["leaves"]} independently checked leaves)')
text='For the exact original state131: '+ '; '.join(parts)+'. All decimal targets are exact rationals. No floating trigonometric bound is an input.'
a={'topic':'99_original_global_signs','title':'Independent original-state density sign and matrix bounds','claim':text,'method':'Complete directed Bernstein covers and independent direct-power leaf checks, bound to the exact original coefficients.','result':text,'scope':'Only the registered targets. No certificate of every intermediate polar-table field enclosure or nonlinear existence is inferred.','team_note':'Opus5.5 and numerics: please review the exact target list in audit.json and the standalone proof. These supply independent replacement certificates for their stated inequalities.','checkpoint':'Registered independent original density/sign/matrix targets; continue remaining covers and final report audit.'};(p/'register.json').write_text(json.dumps(a,indent=2)+'\n');subprocess.run([sys.executable,str(root/'research/tools/register_result.py'),str(p/'register.json')],check=True)
