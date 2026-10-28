"""Independent structural audit of the finite compactified matrix certificates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
HERE=Path(__file__).resolve().parent
ctx.prec=320
results=[]
for state in (88,131):
    d=json.loads((HERE/f'state{state:03d}_compact_certificate.json').read_text())
    p=json.loads((HERE/f'state{state:03d}_compact_polynomials.json').read_text())
    s=json.loads((HERE.parents[1]/'source_audit'/f'state{state:03d}_exact.json').read_text())
    assert d['status']=='COMPLETE' and not d['failed'] and d['pending']==0
    assert d['input_sha256']==p['input_sha256']==s['canonical_serialization_sha256']
    paths={r['path']:r for r in d['accepted']};assert len(paths)==len(d['accepted'])
    def visit(path,tl,th,zl,zh):
        if path in paths:
            row=paths[path]
            assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
            assert arb(row['lower'])>=arb(19)/5
            assert not any(q.startswith(path) and q!=path for q in paths)
            return 1
        kids={q[len(path)] for q in paths if q.startswith(path)}
        assert kids in ({'t','T'},{'z','Z'}),(path,kids)
        if kids=={'t','T'}:
            mid=(tl+th)/2
            return visit(path+'t',tl,mid,zl,zh)+visit(path+'T',mid,th,zl,zh)
        mid=(zl+zh)/2
        return visit(path+'z',tl,th,zl,mid)+visit(path+'Z',tl,th,mid,zh)
    n=visit('',Q(0),Q(1),Q(-1),Q(1));assert n==len(paths)
    origin={}
    for label in ('chi22','chi04','chi31'):
        zcoeff={}
        for j in range(4):
            for i,k,v in p['polynomials'][f'{label}_{j}']:
                assert 0<=i<=28 and 0<=k<=11
                if i==0:zcoeff[k]=zcoeff.get(k,Q(0))+Q(v)
        zcoeff={k:v for k,v in zcoeff.items() if v}
        assert all(k==0 for k in zcoeff), (state,label,zcoeff)
        origin[label]=zcoeff.get(0,Q(0))
    assert origin['chi22']==Q(s['exact_parameters']['strain'])
    assert origin['chi31']==0
    assert -origin['chi22']-origin['chi04']==Q(s['exact_parameters']['a0'])
    results.append({'state':state,'leaves':n,'coverage':'complete exact binary partition','minimum_claim':'19/5','origin_identities':'exact','input_sha256':d['input_sha256'],'certificate_sha256':hashlib.sha256((HERE/f'state{state:03d}_compact_certificate.json').read_bytes()).hexdigest()})
    print(state,'coverage',n,'leaves; all lower bounds >=19/5; exact origin identities OK')
report={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','states':results}
(HERE/'compact_certificate_audit.json').write_text(json.dumps(report,indent=2)+'\n')
