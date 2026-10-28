"""Verify all six exact binary lower bounds and the full dependency chain."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from hashlib import sha256
import json
from flint import arb,fmpq,ctx
ctx.prec=768
H=Path(__file__).resolve().parent;B=H.parent
original=Path('case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json')
producer_dir=Path('numerics/data')
rows=[];dependencies={}
for tag,producer_name in [('c8','wnorm_cert_131.json'),('c9','wnorm_cert_multi_131.json')]:
    producer=producer_dir/producer_name
    producer_hash=sha256(producer.read_bytes()).hexdigest()
    pd=json.loads(producer.read_text());records={}
    for cut in [3,4]:
        p=H/(f'audit_{tag}.json' if cut==3 else f'audit_{tag}_Q4.json')
        d=json.loads(p.read_text());records[cut]=d
        assert d['Q']==cut and len(d['rows'])==3
        assert d['source_sha256']==sha256(original.read_bytes()).hexdigest()
        assert d['producer_record_sha256']==producer_hash
        assert d['code_sha256']==sha256((H/f'audit_{tag}.py').read_bytes()).hexdigest()
        for rel,digest in d['dependencies'].items():
            assert sha256((B/rel).read_bytes()).hexdigest()==digest,rel
        dependencies[str(p.relative_to(B))]=sha256(p.read_bytes()).hexdigest()
    assert records[4]['all_binary_endpoints_independently_confirmed']
    r3=records[3]['rows'];r4=records[4]['rows']
    for x,y in zip(r3,r4):
        radial_key='T_power2' if tag=='c8' else 'R_power'
        qkey='test_quotient_lower_ball' if tag=='c8' else 'L_witness_lower'
        remkey='pairing_remainder' if tag=='c8' else 'remainder'
        intkey='L_strict_integer_lower' if tag=='c8' else 'strict_L_integer_lower'
        assert x[radial_key]==y[radial_key]
        pp=pd['results']['2^'+str(y[radial_key])]
        pair=y['producer_binary_lower_man_exp']
        assert pair==pp['L_lower_exact_binary_man_exp']
        assert type(pair[1]) is int and str(int(pair[0]))==pair[0]
        exact=Fraction(int(pair[0]))*Fraction(2)**pair[1]
        b=arb(fmpq(exact.numerator,exact.denominator))
        q=arb(y[qkey]);assert q.is_finite() and q>b and q>y[intkey]
        error=arb(x[remkey])+arb(y[remkey])
        assert abs(arb(x['pairing'])-arb(y['pairing']))<error
        rows.append({'certificate':tag.upper(),'radial_power2':y[radial_key],
                     'exact_binary_man_exp':pair,'strict_independent_margin':(q-b).str(65),
                     'strict_L_integer_lower':y[intkey],
                     'verdict':'CONFIRMED exact binary lower bound for this test'})
    dependencies[str(producer)]=producer_hash
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED all six exact binary endpoints as test lower bounds; all published lower bounds unchanged','rows':rows,'dependencies':dependencies,'source_sha256':sha256(original.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'limitation':'Does not certify provenance as a producer internal machine-ball endpoint. No norm upper bound or existence claim.'}
H.joinpath('audit_binary_summary.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows: print(row['certificate'],row['radial_power2'],row['strict_independent_margin'])
print(out['utc'],out['verdict'])
