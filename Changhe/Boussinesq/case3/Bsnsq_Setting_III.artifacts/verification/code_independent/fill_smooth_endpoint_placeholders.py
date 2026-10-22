#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import re,json,hashlib
v=Path('research/338_smooth_endpoint_report_entry/verification'); now=datetime.now(timezone.utc).isoformat(); end='10:33'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return' '.join(s.split())
old=dict(re.findall(r"^(ROW|TL|AUDIT_A|VER_A|START)='(.*)'$",(v/'proposed_strings.sh').read_text(),re.M)); new={k:s.replace('HH:MM to HH:MM','10:14 to '+end).replace('MM controls','271 controls')for k,s in old.items()}; raw=(v/'approved_preview_unfilled.md').read_text();filled=raw;expected=norm(raw);checks=[]
def ck(name,t):checks.append(dict(name=name,passed=bool(t)));assert t,name
ck('all_five_strings',set(new)=={'ROW','TL','AUDIT_A','VER_A','START'})
for k in ['ROW','TL','AUDIT_A','VER_A']:
 a,b=old[k],new[k];pat=r'\s+'.join(re.escape(w)for w in a.split());ck('unique_'+k,len(re.findall(pat,filled))==1);filled=re.sub(pat,lambda m:b,filled,count=1);expected=expected.replace(a,b,1)
ck('exact_only_string_substitutions',norm(filled)==expected)
ck('no_unfilled_new_tokens',not re.search(r'\b(MM|NN|PZZZ|HH:MM)\b',norm(filled)))
a=json.loads((v/'math_checks.json').read_text());b=json.loads((v/'entry_checks.json').read_text());ck('primary_271',a['total']==a['passed']==208 and b['total']==b['passed']==63)
ck('no_model_names_in_strings',not re.search(r'Opus|Claude|GPT|astra',json.dumps(new),re.I))
ck('exact_recorded_interval','complete-entry verification 10:14 to 10:33 (P338, 271 controls)'in new['TL'])
ck('no_placeholder_clock_or_three_digit_minutes',not re.search(r'HH:|\b[0-9]{2}:[0-9]{3}\b',filled))
bad=old['TL'].replace('MM','271').replace('HH:MM to HH:MM','10:14 to 10:33')
ck('old_bug_reproduced',bad.count('HH:271')==2)
ck('clock_validator_rejects_old_bug',bool(re.search(r'HH:|\b[0-9]{2}:[0-9]{3}\b',bad)))
(v/'approved_placeholders.json').write_text(json.dumps(new,indent=2)+'\n');(v/'approved_preview.md').write_text(filled)
out=dict(utc=now,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,primary_checks=271,approved_text_sha256=sha(v/'approved_text.md'),approved_preview_sha256=sha(v/'approved_preview.md'),approved_placeholders_sha256=sha(v/'approved_placeholders.json'),code_sha256=sha(Path(__file__)),actual_adoption='OPEN;11:30isproposedonly')
(v/'placeholder_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
