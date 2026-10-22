"""Fixed source, complete canonical parents and authenticated actual review gates."""
import os,sys,json,hashlib,math,importlib.util
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
sys.dont_write_bytecode=True
assert not sys.flags.optimize, 'proof checks require Python assertions'
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
ROOT=Path(__file__).resolve().parents[3];DIR=ROOT/'research/full_derivative_norm_bound_v2';OUT=DIR/'evidence';REV=ROOT/'notes/reviews'
PARENTS={'radial':('research/radial_tm_refined/evidence/verdict.json','CONFIRMED_COMPLETE_FINITE_RADIAL_TAYLOR_MODELS_ENDPOINT_REFINED'), 'canonical':('research/canonical_full_radial_linkage/evidence/verdict.json','CONFIRMED_COMPLETE_CANONICAL_RADIAL_MODELS_ARCHIVE_PREMISE_DISCHARGED'),'tails':('research/derivative_end_tails/evidence/verdict.json','CONFIRMED_CANONICAL_DERIVATIVE_END_TAILS_CONDITIONAL_FULL_PLANE_COMPOSITION')}
TAILSHA='cd74be46c37ccee9f4a29c6bd63c72d1a87065787d781f53c08f6d44962980ee'
SMOKE=[0,2955,4102,4125,4211,7808];REPLAY=[0,1955,2955,4102,4125,4211,7808]
OWN=['PARENT_REBINDING.md','PARENT_REBINDING_SINGLE.md','external_rebindings.json','evidence/rebinding_first.json','evidence/rebinding_six_before_code.json','evidence/v2_code_birth.json','PROOF.md','PROOF_ADJUDICATION.md','evidence/proof_first.json','evidence/proof_adjudication.json','KERNEL_ADJUDICATION.md','evidence/KERNEL_ADJUDICATION.json','SOURCE_SCOPE.md','IMPLEMENTATION_ADDENDUM.md','code/error_diagnostics.py','code/kernels.py','code/bounds.py','code/selfcheck.py','code/protocol.py','code/prepare.py','code/run.py','code/audit.py','code/replay.py','code/review.py','code/finalize.py','code/queue.sh','review_files.json','preparation_question.txt','actual_question.txt']
PREFIX='You are Claude Opus 5.5 collaborating with GPT-6, reviewing a mathematical computer-assisted IPM proof. Restrictions on this delegated task: no JavaScript/TypeScript development or execution; no servers/listeners/tunnels; no RLScience cluster; no Lean/Lake builds; no outside writes; no people contact. Pure text review only. Return a concise substantive FINAL ANSWER, not just internal reasoning. Reconstruct claims and reject gaps. '

def now():return datetime.now(timezone.utc).isoformat()
def when(s):
    v=datetime.fromisoformat(s);assert v.tzinfo is not None;return v

def pairs(ps):
    d={}
    for k,v in ps:assert k not in d;d[k]=v
    return d

def load(p):return json.loads(Path(p).read_text(),object_pairs_hook=pairs,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def parse(s):return json.loads(s,object_pairs_hook=pairs,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False)
def write(p,v):
    p=Path(p);assert p.resolve().is_relative_to(ROOT)
    with p.open('x') as f:f.write(json.dumps(v,indent=2,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
def pin(pins,p,expected=None):
    p=(ROOT/p).resolve();assert p.is_relative_to(ROOT) or p.is_relative_to(ROOT.parent/'ipmA-num')
    n=str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p);h=sha(p)
    assert expected is None or h==expected,('changed',n)
    assert n not in pins or pins[n]==h; pins[n]=h;return h

def rehash(pins):
    for n,h in pins.items():assert sha(ROOT/n)==h,('changed pin',n)

def parents():
    pins={};deps={}
    for label,(name,status) in PARENTS.items():
        v=load(ROOT/name);assert v['status']==status
        got=pin(pins,name,TAILSHA if label=='tails' else None)
        if label!='tails':assert v['cells']==7809 and v['modes']==261 and v['polynomial_degree']==12
        if label=='canonical':assert v['explicit_premise_application']['canonical_moment_condition_discharged'] is True
        substitutions={}
        mapping=load(DIR/'external_rebindings.json')
        for n,h in v['files'].items():
            if n in mapping:
                r=mapping[n];assert h==r['sha256'] and v['files'].get(r['replacement'])==h
                pin(pins,r['replacement'],h);substitutions[n]=r
            else:pin(pins,n,h)
        deps[label]={'path':name,'sha256':got,'status':status,'utc':v['utc'],'pins':len(v['files']),'explicit_content_rebindings':substitutions}
    rv=load(ROOT/PARENTS['radial'][0]);cv=load(ROOT/PARENTS['canonical'][0])
    assert cv['files'][PARENTS['radial'][0]]==deps['radial']['sha256']
    path='research/radial_tm_refined/evidence/full_rows.jsonl';assert path in rv['files'];pin(pins,path,rv['files'][path])
    return pins,deps

def auth(pins,tag,verdict,files=None,question=None):
    m=load(REV/(tag+'_metadata.json'));r=load(REV/(tag+'_response.json'));text=(REV/(tag+'_response.md')).read_text();req=(REV/(tag+'_request.txt')).read_text()
    assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==r['model']=='claude-opus-5-5' and m['stop_reason']==r['stop_reason']=='end_turn' and 'availability_error' not in m
    if files is not None:assert m['files']==files
    assert len(m['files'])==len(set(m['files']))
    pre=req.split('\n\nFILE ',1)[0]
    assert pre.startswith(PREFIX)
    if question is not None:assert pre==PREFIX+question
    assert req==pre+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(ROOT/n).read_text() for n in m['files'])
    assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
    assert text=='\n\n'.join(x['text'] for x in r['content'] if x['type']=='text')+'\n'
    assert text.rstrip().splitlines()[-1]=='VERDICT: '+verdict and text.count('VERDICT:')==1
    assert when(m['start_utc'])<when(m['end_utc'])<datetime.now(timezone.utc)
    for n in m['files']:pin(pins,n)
    for suffix in ['metadata.json','request.txt','response.json','response.md']:pin(pins,REV/(tag+'_'+suffix))
    return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}

def post(pins,tag,review,stem):
    v=load(OUT/(stem+'.json'));a=DIR/(stem+'.md');rh=sha(REV/(tag+'_response.json'))
    assert v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(a) and v['all_substantive_objections_resolved'] is True
    assert when(review['end_utc'])<when(v['utc'])<datetime.now(timezone.utc)
    assert review['request_id'] in a.read_text() and rh in a.read_text()
    m=load(REV/(tag+'_metadata.json'));assert str(a.relative_to(ROOT)) not in m['files'] and str((OUT/(stem+'.json')).relative_to(ROOT)) not in m['files']
    pin(pins,a);pin(pins,OUT/(stem+'.json'));return v

def source():
    # Original actual kernel review applies only to these identical copied bytes.
    for n in ['code/kernels.py','code/bounds.py','code/selfcheck.py','code/error_diagnostics.py']:
        assert sha(DIR/n)==sha(ROOT/'research/full_derivative_norm_bound'/n)
    f=load(OUT/'source_freeze.json');expected={str((DIR/n).relative_to(ROOT)):sha(DIR/n) for n in OWN};assert f['files']==dict(sorted(expected.items()))
    assert load(OUT/'proof_first.json')['proof_sha256']==sha(DIR/'PROOF.md')
    p,deps=parents();m=load(OUT/'parent_manifest.json');assert m['parents']==deps and m['files']==dict(sorted(p.items()))
    kr=auth(p,'full_derivative_norm_kernel_resolution','CONFIRM_DERIVATIVE_KERNEL_AND_DIAGNOSTICS_ONLY');post(p,'full_derivative_norm_kernel_resolution',kr,'KERNEL_ADJUDICATION')
    for n,h in f['files'].items():pin(p,n,h)
    for n in ['source_freeze.json','parent_manifest.json']:pin(p,OUT/n)
    return p,deps,f

def data():
    p=ROOT/'research/radial_tm_refined/code/common.py';spec=importlib.util.spec_from_file_location('radial_179_data',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.Data()

def radial_rows():
    rows=[]
    with (ROOT/'research/radial_tm_refined/evidence/full_rows.jsonl').open() as f:
        for line in f:
            z=parse(line)
            if z['type']=='cell':assert z['cell']==len(rows);rows.append(z)
    assert len(rows)==7809;return rows

def bind(c,row):
    assert c['i']==row['cell'] and str(c['a'])==row['a'] and str(c['b'])==row['b'] and str(c['h'])==row['h'] and c['array_manifest']==row['array_manifest']

def dyad(v):
    m,e=v;assert type(m) is str and type(e) is int and len(m)<1000 and abs(e)<100000
    return F(int(m))*F(2)**e

def compact_q(v,upper):
    v=F(v);assert v>=0
    n,d=v.numerator,v.denominator;assert d==1<<(d.bit_length()-1)
    shift=max(0,n.bit_length()-128);unit=1<<shift
    a=(n+unit-1)//unit if upper else n//unit;e=shift-(d.bit_length()-1)
    out=[str(a),e];assert (dyad(out)>=v if upper else dyad(out)<=v)
    return out

def compact(v):
    lo,hi=F(v['lower_exact']),F(v['upper_exact']);assert 0<=lo<=hi
    return {'lo':compact_q(lo,False),'hi':compact_q(hi,True)}

def compact_output(o):return {k:[compact(v) for v in rows] for k,rows in o.items()}

def overlap(a,b):
    assert a.keys()==b.keys()
    for key in a:
        assert len(a[key])==len(b[key])
        for x,y in zip(a[key],b[key]):assert max(F(x['lower_exact']),F(y['lower_exact']))<=min(F(x['upper_exact']),F(y['upper_exact'])),key

def ceiling(v,den=10**9):
    v=F(v);n=v.numerator*den//v.denominator+1;assert F(n,den)>v
    return str(n//den)+'.'+str(n%den).zfill(len(str(den))-1)
