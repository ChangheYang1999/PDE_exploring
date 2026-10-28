"""Read-only exact table and explicit dependency integrity audit."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'05_team_audit/final_integrity'

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        while block:=f.read(1024*1024):h.update(block)
    return h.hexdigest()

def decimal(q,n,up):
    scale=10**n
    a,b=(q*scale).as_integer_ratio()
    k=-((-a)//b) if up else a//b
    return f'{k//scale}.{k%scale:0{n}d}'

def find_endpoint(obj,a,kind):
    if 'entries' in obj:
        return [Q(x['safe_D_lower']) for x in obj['entries'] if Q(x['alpha'])==a and x['verdict']=='CONFIRMED']
    rows=obj.get('rows',[obj]);out=[]
    for row in rows:
        aa=row.get('alpha',row.get('alpha_or_epsilon'))
        if aa is None or Q(aa)!=a:continue
        if row.get('mode','finite')!='finite':continue
        if kind=='upper_C':keys=['safe_upper_C','safe_upper']
        elif kind=='upper_D':keys=['safe_upper_D','safe_upper']
        elif kind=='lower_C':keys=['safe_decimal_lower_10_places']
        else:keys=['safe_D_lower','safe_D_lower_10_places']
        for key in keys:
            if key not in row:continue
            if key=='safe_upper' and row.get('operator')!=kind[-1]:continue
            out.append(Q(row[key]))
    return out

TABLE=ROOT/'data/verified_table.json'
table=json.loads(TABLE.read_text());checks=[];pending=[];edges=[];visited=set();digests={};problems=[]

def resolve(name,parent):
    p=Path(name)
    candidates=[p] if p.is_absolute() else [ROOT/p,parent/p,ROOT/'code'/p]
    if not p.is_absolute():
        for ancestor in [parent,*parent.parents]:
            if ancestor==ROOT.parent:break
            candidates.extend([ancestor/p,ancestor/'code'/p])
    for p in candidates:
        if p.is_file():return p.resolve()
    return candidates[0].resolve()

def edge(origin,name,expected):
    p=resolve(name,origin.parent)
    if not p.is_file():
        problems.append(dict(origin=str(origin.relative_to(ROOT)) if origin.is_relative_to(ROOT) else str(origin),name=name,expected=expected,problem='missing'))
        return
    actual=digests.setdefault(str(p),sha(p)) if str(p) not in digests else digests[str(p)]
    record=dict(origin=str(origin.relative_to(ROOT)) if origin.is_relative_to(ROOT) else str(origin),name=name,resolved=str(p),expected=expected,actual=actual)
    edges.append(record)
    if expected!=actual:problems.append(dict(record,problem='digest_mismatch'))
    if p.suffix=='.json' and expected==actual:pending.append(p)

for row in table['rows']:
    a=Q(row['alpha']);values={}
    for kind,selected in [('upper_C','selected_upper_C'),('upper_D','selected_upper_D'),('lower_C','selected_lower'),('lower_D','selected_lower_D')]:
        item=row[selected];q=Q(item['exact_safe_endpoint']);p=ROOT/item['source'];obj=json.loads(p.read_text())
        assert q in find_endpoint(obj,a,kind),(a,kind,q,p)
        assert row[kind]==decimal(q,6,kind.startswith('upper')),(a,kind)
        values[kind]=q;pending.append(p.resolve())
    assert row['lower_C_and_D']==row['lower_C']
    assert row['C_ratio_upper']==decimal(Q(row['upper_C'])/Q(row['lower_C']),6,True)
    assert values['lower_C']<=values['upper_C'] and values['lower_D']<=values['upper_D']
    checks.append(dict(alpha=str(a),endpoints_and_rounding='PASS',C_ratio_upper_4_places=decimal(Q(row['upper_C'])/Q(row['lower_C']),4,True),D_ratio_upper_4_places=decimal(Q(row['upper_D'])/Q(row['lower_D']),4,True),D_minus_C_lower=str(values['lower_D']-values['upper_C']),D_minus_C_lower_4_places=decimal(values['lower_D']-values['upper_C'],4,False)))
for name,digest in table['input_sha256'].items():edge(TABLE,name,digest)
edge(TABLE,'code/build_verified_table.py',table['source_sha256'])
# The top table hash map includes superseded inputs. These identities are checked,
# but recursion starts only from the selected endpoint files.
selected_pending=[(ROOT/row[k]['source']).resolve() for row in table['rows'] for k in ['selected_upper_C','selected_upper_D','selected_lower','selected_lower_D']]
pending=selected_pending
while pending:
    p=pending.pop()
    if p in visited:continue
    visited.add(p)
    obj=json.loads(p.read_text())
    for key in ['sha256','source_hashes','input_hashes','input_sha256']:
        value=obj.get(key)
        if not isinstance(value,dict):continue
        for name,digest in value.items():
            if isinstance(digest,str) and re.fullmatch('[a-f0-9]{64}',digest):edge(p,name,digest)
    if p.name=='accepted_external_D.json':
        for item in obj['entries']:
            edge(p,item['audit_path'],item['audit_sha256'])
            edge(p,item['source_path'],item['source_sha256'])
links=re.findall(r'\]\(([^)]+)\)',(ROOT/'THEOREM_MAP.md').read_text())
missing=[p for p in links if not (ROOT/p).exists()]
assert not missing,missing
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),scope='Exact active endpoint and decimal checks; explicit dependency identities only; no new cell replay.',table_sha256=sha(TABLE),script_sha256=sha(Path(__file__)),proof_sha256=sha(OUT/'PROOF.md'),map_sha256=sha(ROOT/'THEOREM_MAP.md'),map_links_checked=len(links),rows=checks,dependency_json_files=len(visited),dependency_edges=len(edges),unique_files_hashed=len(digests),problems=problems,edges=edges)
(OUT/'integrity.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['edges']},indent=2))
