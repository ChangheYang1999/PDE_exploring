"""Exact structural and threshold audit for stronger-energy certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
ctx.prec=384
HERE=Path(__file__).resolve().parent

def partition(rows,threshold):
    paths={r['path']:r for r in rows};assert len(paths)==len(rows)
    def visit(path,tl,th,zl,zh):
        if path in paths:
            row=paths[path]
            assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
            assert arb(row['lower'])>=threshold
            assert not any(q.startswith(path) and q!=path for q in paths)
            return 1
        kids={q[len(path)] for q in paths if q.startswith(path)}
        assert kids in ({'t','T'},{'z','Z'}),(path,kids)
        if kids=={'t','T'}:
            tm=(tl+th)/2;return visit(path+'t',tl,tm,zl,zh)+visit(path+'T',tm,th,zl,zh)
        zm=(zl+zh)/2;return visit(path+'z',tl,th,zl,zm)+visit(path+'Z',tl,th,zm,zh)
    assert visit('',Q(0),Q(1),Q(-1),Q(1))==len(rows)
    return paths

records=[]
for state in (88,131):
    source=json.loads((HERE.parents[1]/'source_audit'/f'state{state:03d}_exact.json').read_text())
    row={'state':state,'certificates':{}}
    for quantity,suffix,threshold in [('A','_factored',-arb(1)/20),('DU','',arb(0)),('N','',arb(0))]:
        path=HERE/f'state{state:03d}_aux_{quantity}{suffix}_certificate.json'
        d=json.loads(path.read_text());assert d['status']=='COMPLETE' and not d['failed'] and d['pending']==0
        assert d['input_sha256']==source['canonical_serialization_sha256']
        assert d['quantity']==quantity
        paths=partition(d['accepted'],threshold)
        if quantity=='A':assert d['factored']
        if quantity=='DU':du_paths=paths
        row['certificates'][quantity]={'leaves':len(paths),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    path=HERE/f'state{state:03d}_coefficient_bounds.json';d=json.loads(path.read_text())
    assert d['input_sha256']==source['canonical_serialization_sha256']
    assert {r['path'] for r in d['leaf_bounds']}==set(du_paths)
    assert len(d['leaf_bounds'])==len(du_paths)
    for leaf in d['leaf_bounds']:
        for field,value in leaf['upper_bounds'].items():
            if field in ('rho_x','rho_y'):bound=arb(11)
            elif field.startswith('rho_'):bound=arb(33)
            elif field in ('chi22','chi31','chi13'):bound=arb(7)/5
            else:bound=arb(26)
            assert arb(value)<=bound,(state,leaf['path'],field,value,bound)
    row['derivative_bounds']={'G':11,'H':33,'J':'7/5','K':26,'D2rho_Frobenius':77,'D3rho_tensor':94,'D2U_tensor':35}
    row['coefficient_file_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    records.append(row)
    print(state,'A/DU/N coverage and every derivative leaf bound passed')
# All rational inequalities in the common stronger-energy argument.
assert Q(16)*11*33<77**2
assert Q(8)*33**2<94**2
assert Q(32)*Q(7,5)*26<35**2
assert Q(12000)*(Q(11,4)-Q(1,20))>=100+5*77**2
assert Q(189)+Q(94,109)<190 and 109**2<12000
assert Q(13,5)+Q(2,5)==3
assert 100-10000*Q(1,20)+Q(190**2,4*Q(2,5))<=3*10000
assert -(1-Q(1,122))/20+3*Q(1,122)==-Q(1,40)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','records':records,'common_rational_energy_inequalities':'passed'}
(HERE/'auxiliary_certificate_audit.json').write_text(json.dumps(out,indent=2)+'\n')
