"""Exact raw-generator conversion and leading profile binding for new successors."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,json,sys,time
from flint import fmpq as Q, fmpq_poly as P
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
T=P([0,1]);Z=P([])
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
helper=ROOT/'research/weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('own_polar',helper);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
def main(label):
    start=time.monotonic();src=BASE/f'data/{label}';manifest=json.loads((src/'MANIFEST.json').read_text())
    frozen=json.loads((src/'FROZEN.json').read_text())
    for name,h in frozen['files'].items():assert H(src/name)==h
    name=manifest['coefficient_files'][0]['name'];rawpath=src/name;raw=json.loads(rawpath.read_text())
    assert H(rawpath)==manifest['coefficient_files'][0]['sha256']
    checksums={line.split()[1]:line.split()[0] for line in (src/'SHA256SUMS').read_text().splitlines() if line.strip()}
    assert checksums[name]==H(rawpath)
    c=Q(raw['cl_exact']);assert 1<c<2
    pot={}
    for g in raw['generators']:
        assert 'p' not in g
        j,m=int(g['j']),int(g['m']);sp=g['spec'];coef=Q(g['coef'])
        assert j>=0 and m>=0 and sp[0] in ['mono','leg']
        if sp[0]=='mono':
            assert len(sp)==2 and int(sp[1])>=0
            poly=T**(m+int(sp[1]))
        else:
            assert len(sp)==3 and min(map(int,sp[1:]))>=0
            w,n=map(int,sp[1:]);poly=T**(m+w)*P([(-1)**(n+k)*comb(n,k)*comb(n+k,k) for k in range(n+1)])
        pot[j,m]=pot.get((j,m),Z)+coef*poly
    entries=sorted(((j,m,k),q) for (j,m),p in pot.items() for k,q in enumerate(p) if q)
    can={'candidate':manifest['id'],'source_sha256':H(rawpath),'cl':str(c),'order':[list(idx) for idx,q in entries],'coefficients':[str(q) for idx,q in entries]}
    _,delta,rho,stream=F.fields(can)
    assert all(p[0]==0 for (j,n),p in rho.items() if n!=1)
    assert all(p[0]==0 for (j,n),p in stream.items() if n!=2)
    a0=sum((p[0] for (j,n),p in rho.items() if n==1),Q(0))
    strain=2*sum((p[0] for (j,n),p in stream.items() if n==2),Q(0))
    assert strain==1-c and a0>0
    can.update(a0=str(a0),strain=str(strain))
    basepath=ROOT/'research/taylor_projection/source/canonical007.json'
    base=json.loads(basepath.read_text());_,_,r0,s0=F.fields(base)
    assert Q(base['cl'])==c
    extract=lambda fields,j:{str(n):str(p(Q(1))) for (jj,n),p in fields.items() if jj==j and p(Q(1))}
    leading=[]
    for j in range(4):
        rr,ss=extract(rho,j),extract(stream,j)
        assert rr==extract(r0,j) and ss==extract(s0,j)
        leading.append({'branch':j,'full_density_equal007':True,'full_stream_equal007':True,'density_modes':len(rr),'stream_modes':len(ss)})
    dest=src/'canonical.json';assert not dest.exists();dest.write_text(json.dumps(can,indent=2)+'\n')
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':manifest['id'],'source_sha256':H(rawpath),'canonical_sha256':H(dest),'code_sha256':H(__file__),'proof_sha256':H(BASE/'PROOF.md'),'helper_sha256':H(helper),'baseline007_sha256':H(basepath),'generators':len(raw['generators']),'canonical_nonzero_terms':len(entries),'origin_identities_exact':True,'a0_exact':str(a0),'strain_exact':str(strain),'leading_four_profiles':leading,'elapsed_seconds':time.monotonic()-start,'status':'Local exact check passed; OPEN independent numerical review.'}
    path=BASE/f'verification/{label}_build.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['a0_exact']},indent=2),flush=True)
if __name__=='__main__':main(sys.argv[1])
