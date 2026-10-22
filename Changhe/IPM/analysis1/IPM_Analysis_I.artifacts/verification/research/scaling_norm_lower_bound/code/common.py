"""Exact input selection, reviewed sources, complete parent and result gates."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,importlib.util
sys.dont_write_bytecode=True
assert not sys.flags.optimize
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[name]='1'
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/scaling_norm_lower_bound';E=D/'evidence';REV=ROOT/'notes/reviews'
UP=ROOT/'research/full_derivative_norm_bound_v2/code/protocol.py'
assert hashlib.sha256(UP.read_bytes()).hexdigest()=='b57406959b9857d3acf994d7c1067fe4f534fa3b2362d2ddc3ed785be2cdcdcf'
spec=importlib.util.spec_from_file_location('scaling184_protocol',UP);u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
load,sha,write,pin,rehash,auth,when,now=u.load,u.sha,u.write,u.pin,u.rehash,u.auth,u.when,u.now
FIXED=['PROOF.md','THEOREM_ADJUDICATION.md','evidence/THEOREM_ADJUDICATION.json','evidence/proof_first.json','evidence/constants.json','evidence/input_manifest.json','code/cox_monomial.py','code/deboor_legendre.py','code/weights.py','code/selfcheck.py','evidence/selfcheck.json','code/common.py','code/run.py','code/audit.py','code/replay.py','code/gate.py','code/queue.sh','review_files.json','workflow_question.txt','preparation_question.txt','actual_question.txt']
GRAPH='research/modal_graph_scaling/evidence/verdict.json';GRAPHSHA='2fa46f4d33275590ab3df7ce88409198590c96f34c9f3e5d3ebb94289bf010c5'
MODAL='research/modal_repair/evidence/audit_verdict.json';MODALSHA='c17c7f4dfbc86ac789838d59d846f5641cae59577dd8e62987edd31904dab6b8'
INPUT='data_exact/modal_v2.json';INPUTSHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'

def post(pins,tag,review,stem):
    a=D/(stem+'.md');p=E/(stem+'.json');z=load(p);rh=sha(REV/(tag+'_response.json'))
    assert z['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and z['request_id']==review['request_id'] and z['input_sha256']==review['input_sha256'] and z['response_sha256']==rh and z['adjudication_sha256']==sha(a) and z['all_substantive_objections_resolved'] is True
    assert when(review['end_utc'])<when(z['utc'])<datetime.now(timezone.utc)
    assert review['request_id'] in a.read_text() and rh in a.read_text()
    fs=load(REV/(tag+'_metadata.json'))['files'];assert str(a.relative_to(ROOT)) not in fs and str(p.relative_to(ROOT)) not in fs
    pin(pins,a);pin(pins,p);return z

def parents():
    pins={};pin(pins,GRAPH,GRAPHSHA);pin(pins,MODAL,MODALSHA);pin(pins,INPUT,INPUTSHA)
    g=load(ROOT/GRAPH);assert g['status']=='CONFIRMED_ACTUAL_MODAL_GRAPH_SCALING_AND_NONZERO_IMAGE'
    for n,h in g['files'].items():pin(pins,n,h)
    m=load(ROOT/MODAL);assert m['verdict']=='CONFIRMED' and m['input_and_source_hashes_verified'] is True
    for n,h in m['source_and_evidence_sha256'].items():pin(pins,n,h)
    c=load(E/'constants.json')
    for n,h in c['canonical_identity_files'].items():assert pins.get(n)==h==sha(ROOT/n)
    rehash(pins);return pins

def input_data():
    import cox_monomial as a, deboor_legendre as b
    assert sha(ROOT/INPUT)==INPUTSHA
    x=load(ROOT/INPUT);assert x['degree']==7
    for name,shape in [('S',[260,1565]),('knots',[1573])]:
        z=x['arrays'][name];assert z['shape']==shape
        count=1
        for dim in shape:count*=dim
        assert len(z['hex'])==count
    ka=list(map(a.decode,x['arrays']['knots']['hex']));kb=list(map(b.decode,x['arrays']['knots']['hex']));assert ka==kb
    flat=x['arrays']['S']['hex'];sa=[list(map(a.decode,flat[j*1565:(j+1)*1565])) for j in range(260)];sb=[list(map(b.decode,flat[j*1565:(j+1)*1565])) for j in range(260)];assert sa==sb
    spans=[i for i in range(len(ka)-1) if ka[i]<ka[i+1]]
    assert spans==list(range(7,1565)) and all(ka[i]<=ka[i+1] for i in range(1572))
    assert all(v==ka[0] for v in ka[:8]) and all(v==ka[-1] for v in ka[-8:])
    c=load(E/'constants.json');manifest=load(E/'input_manifest.json')
    assert manifest['full_spans']==spans and len(set(manifest['smoke_spans']))==3 and all(i in spans for i in manifest['smoke_spans'])
    assert manifest['endpoints_exact']=={str(i):[str(ka[i]),str(ka[i+1])] for i in spans}
    for name in ['k','L']:
        assert a.decode(x['scalars_hex'][name])==b.decode(x['scalars_hex'][name])
        assert F(str(a.decode(x['scalars_hex'][name])))==F(c[name])
    assert 0<F(c['k'])<F(1,2) and F(c['L'])>0
    return (ka,sa),(kb,sb),c,manifest

def source():
    z=load(E/'source_freeze.json');expected={str((D/n).relative_to(ROOT)):sha(D/n) for n in FIXED};assert z['files']==dict(sorted(expected.items()))
    p=parents()
    for n,h in z['files'].items():pin(p,n,h)
    pin(p,E/'source_freeze.json');pin(p,UP)
    first=load(E/'proof_first.json');assert first['proof_sha256']==sha(D/'PROOF.md') and first['code_files']==[]
    sc=load(E/'selfcheck.json');assert sc['source_sha256']==sha(D/'code/selfcheck.py') and sc['status']=='PASS_MANUFACTURED_SCALING_NORM_ARITHMETIC_ONLY' and sc['actual_modal_spans_executed']==0
    fs=load(D/'review_files.json')['workflow'];assert len(fs)==len(set(fs)) and {str((D/n).relative_to(ROOT)) for n in FIXED}<=set(fs)
    r=auth(p,'scaling_lower_workflow','CONFIRM_SCALING_NORM_SOURCE_PENDING_NUMERICAL_COMPUTATION',fs,(D/'workflow_question.txt').read_text());ad=post(p,'scaling_lower_workflow',r,'WORKFLOW_ADJUDICATION');assert when(ad['utc'])<when(z['utc'])
    return p

def accepted_preparation():
    p=source();v=load(E/'preparation.json');assert v['status']=='ACCEPTED_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY'
    for n,h in v['files'].items():pin(p,n,h)
    pin(p,E/'preparation.json');return p

def selected(tag):
    assert tag in ['smoke','full'];return load(E/'input_manifest.json')[tag+'_spans']

def verify_row(z,span):
    import weights as w
    assert z['type']=='cell' and z['span']==span and z['source_freeze_sha256']==sha(E/'source_freeze.json')
    assert z['methods']['cox_monomial']==z['methods']['deboor_legendre']
    r=z['methods']['cox_monomial'];assert [r['a'],r['b']]==load(E/'input_manifest.json')['endpoints_exact'][str(span)] and F(r['Q'])>=0 and r['density_coefficients']==2088
    assert len(r['density_coefficients_sha256'])==64
    for side in ['left','right']:
        a=w.valid(z['weights']['arb512'][side]);b=w.valid(z['weights']['iv220'][side]);assert max(a[0],b[0])<=min(a[1],b[1])
    for eng in ['arb512','iv220']:
        assert F(z['weights'][eng]['left']['lower_exact'])<=F(z['weights'][eng]['right']['upper_exact'])

def rows(tag):
    p=E/(tag+'_rows.jsonl');out=[]
    if p.exists():
        with p.open() as f:
            for line in f:out.append(u.parse(line))
    spans=selected(tag);assert len(out)<=len(spans)
    for i,z in enumerate(out):verify_row(z,spans[i])
    return out

def summarize(tag,rr):
    import weights as w
    assert len(rr)==len(selected(tag))>0
    by={}
    for eng,root,conv,ep in [('arb512',w.root_arb,w.enclose_a,w.apair),('iv220',w.root_iv,w.enclose_i,w.ipair)]:
        data=rr if eng=='arb512' else list(reversed(rr));sums={}
        for side in ['left','right']:
            z=sum((conv(row['weights'][eng][side]) for row in data),conv({'lower_exact':'0','upper_exact':'0'}))
            sums[side]=ep(z)
        roots={side:root(sums[side]) for side in ['left','right']}
        by[eng]={'endpoint_weighted_sum_squares':sums,'endpoint_weighted_sum_roots':roots}
    q=w.downward(min(F(by[eng]['endpoint_weighted_sum_roots']['left']['lower_exact']) for eng in by))
    assert F(q)>0 and all(F(q)**2<F(by[eng]['endpoint_weighted_sum_squares']['left']['lower_exact']) for eng in by)
    return {'status':'COMPUTED_CANONICAL_SCALING_NORM_LOWER_BOUND_REQUIRES_AUDIT_AND_REVIEW','tag':tag,'complete_middle':tag=='full','spans':selected(tag),'cells':len(rr),'source_freeze_sha256':sha(E/'source_freeze.json'),'rows_sha256':sha(E/(tag+'_rows.jsonl')),'engines':by,'strict_norm_lower_decimal':q,'density_coefficient_equalities':2088*len(rr),'exact_square_integral_equalities':len(rr),'scope':'Strict whole-plane lower bound from exactly the selected finite annuli; right endpoint sum bounds only their union. No whole-plane upper norm or inverse quotient.'}
