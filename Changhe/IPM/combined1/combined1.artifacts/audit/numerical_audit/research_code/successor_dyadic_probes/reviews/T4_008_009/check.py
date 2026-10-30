"""Own polar fields and rational polynomial squares for dyadic successors."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as P, arb, ctx
sys.set_int_max_str_digits(0)
ctx.prec=2048
BASE=Path(__file__).resolve().parents[1]
T=P([0,1]); V=P([1,-1]); Z=P([])
def digest(p): return sha256(p.read_bytes()).hexdigest()
def ar(x): return arb(x.numerator)/x.denominator
def write(p,d):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(d,indent=2)+'\n')
def main(label):
    start=time.monotonic(); utc=datetime.now(timezone.utc).isoformat()
    manifest=BASE/f'data/{label}_MANIFEST.json'
    frozen=json.loads(manifest.read_text())
    for name,row in frozen.items(): assert digest(BASE/'data'/name)==row['sha256'], name
    canpath=BASE/f'data/{label}_canonical.json'
    can=json.loads(canpath.read_text())
    peer=json.loads((BASE/f'data/{label}_peer_result.json').read_text())
    pm=BASE/f'data/{label}_peer_manifest.json'
    pman=json.loads(pm.read_text())
    assert digest(pm)==peer['manifest_sha256']
    assert digest(canpath) in pman['inputs'].values()
    helper=BASE.parent/'weak_probe_audit/code/reproduce.py'
    spec=importlib.util.spec_from_file_location('own_polar_fields',helper)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c,delta,rho,stream=m.fields(can)
    assert 1<c<2
    assert all(p[0]==0 for (j,n),p in rho.items() if n!=1)
    assert all(p[0]==0 for (j,n),p in stream.items() if n!=2)
    a0=sum((p[0] for (j,n),p in rho.items() if n==1),Q(0))
    strain=2*sum((p[0] for (j,n),p in stream.items() if n==2),Q(0))
    assert a0==Q(can['a0'])==Q(peer['a0_exact'])==Q(pman['a0_exact'])
    assert strain==Q(can['strain'])==Q(pman['strain_exact'])==1-c
    assert a0>=5*c-4
    print(label,'fields',len(rho),len(stream),'origin checks passed',flush=True)
    Dr={key:m.td(p,(key[0]+1)*delta/2,1) for key,p in rho.items()}
    Ds={key:m.td(p,(key[0]+1)*delta/2,2) for key,p in stream.items()}
    common={'candidate':peer['candidate'],'bits':ctx.prec,'manifest_sha256':digest(manifest),
            'code_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),
            'helper_sha256':digest(helper),'c_exact':str(c)}
    energies={}; modefiles={}; comparison_count=0
    for mode in [1,3,7]:
        modepath=BASE/f'verification/{label}_mode{mode}.json'
        peerpath=BASE/f'data/{label}_peer_mode{mode}.json'
        assert digest(peerpath)==peer['mode_result_sha256'][str(mode)]
        pr=json.loads(peerpath.read_text())
        if modepath.exists():
            out=json.loads(modepath.read_text())
            for key in common: assert out[key]==common[key], key
            assert out['peer_sha256']==digest(peerpath)
            print(label,'resumed mode',mode,flush=True)
        else:
            mode_start=time.monotonic(); residual={}; pairs=0
            def add(ell,p):
                if p: residual[ell]=residual.get(ell,Z)+p
            for key,p in rho.items():
                j,n=key
                if n==mode: add(j+1,c*Dr[key]-p)
            for (j,n),q in stream.items():
                dq=Ds[j,n]
                for (i,k),p in rho.items():
                    if k+n!=mode and abs(k-n)!=mode: continue
                    dp=Dr[i,k]
                    if k+n==mode: add(i+j+2,(k*p*dq-n*q*dp)/2)
                    if abs(k-n)==mode: add(i+j+2,(-k*p*dq-n*q*dp)*(1 if k>n else -1)/2)
                    pairs+=1
            terms=[]; endpoints=[]
            for ell,p in residual.items():
                if not p: continue
                d=ell*delta/2
                lap=m.td(m.td(p,d,1),d,1)-mode*mode*p
                L,rem=divmod(lap,T); assert not rem
                L=L(V)
                if L:
                    order=next(k for k,x in enumerate(L) if x)
                    assert ell*delta+2*order-2>0
                    terms.append((ell,L));endpoints.append({'ell':ell,'order':order,'degree':L.degree()})
            groups={}
            for i,(ell,p) in enumerate(terms):
                for j in range(i,len(terms)):
                    ell2,q=terms[j];k=ell+ell2
                    groups[k]=groups.get(k,Z)+(1 if i==j else 2)*V*p*q
            moments=[(k*delta/2+l-2,x) for k,p in groups.items() for l,x in enumerate(p) if x]
            assert all(e>0 for e,x in moments)
            print(label,'mode',mode,'exact moments',len(moments),'seconds',time.monotonic()-mode_start,flush=True)
            weights=[]
            for k,prow in enumerate(pr['weights']):
                a=Q(k,4);assert Q(prow['a'])==a
                energy=arb.pi()/2*sum((ar(x)/ar(a+e) for e,x in moments),arb(0))
                assert energy>0
                norm=energy.sqrt()
                comparisons={name:arb(prow[name]).overlaps(value) for name,value in [('energy',energy),('norm',norm)]}
                assert all(comparisons.values()),(label,mode,str(a))
                weights.append({'a':str(a),'energy':energy.str(110),'norm':norm.str(110),'comparisons':comparisons})
            out={**common,'utc':datetime.now(timezone.utc).isoformat(),'mode':mode,'peer_sha256':digest(peerpath),
                 'pairs':pairs,'endpoints':endpoints,'groups':len(groups),'moments':len(moments),
                 'weights':weights,'elapsed_seconds':time.monotonic()-mode_start}
            write(modepath,out)
            print(label,'mode',mode,'norm0',weights[0]['norm'][:70],flush=True)
        energies[mode]={Q(row['a']):arb(row['energy']) for row in out['weights']}
        comparison_count+=sum(len(row['comparisons']) for row in out['weights'])
        modefiles[mode]=digest(modepath)
    d=c-1
    sstar=(ar(2*d-3)+(ar((2*d-3)**2+16*d)).sqrt())/8
    H=(ar(d)-sstar)*(4*arb.pi()*sstar*(1+sstar)).sqrt()
    assert H.overlaps(arb(peer['H_max']))
    cells=[];edges=[Q(k,4) for k in range(7)]+[1+1/c]
    for k,(l,h) in enumerate(zip(edges,edges[1:])):
        e=Q(k+1,4)
        assert e>=h
        J=sum((energies[n][e] for n in energies),arb(0)).sqrt()
        lower=arb(5)**ar((l-2)/2)*J
        upper=H*ar((1+c-c*l)/(1+l))
        gap=lower-upper;ratio=lower/upper
        assert gap>0 and ratio>1
        pr=peer['seven_cells'][k]
        assert Q(pr['left'])==l and Q(pr['right'])==h and Q(pr['norm_evaluation_at'])==e
        values={'projected_norm':J,'lower':lower,'upper':upper,'gap':gap,'ratio':ratio}
        comparisons={name:arb(pr[name]).overlaps(value) for name,value in values.items()}
        assert all(comparisons.values()), k
        floor=(ratio.lower()*10**8).floor().unique_fmpz();assert floor is not None
        qfloor=Q(floor,10**8)
        assert ratio>ar(qfloor)
        assert ratio>ar(Q(pr['strict_ratio_floor']))
        cells.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(e),
                      **{name:value.str(100) for name,value in values.items()},
                      'strict_ratio_floor':str(qfloor),'comparisons':comparisons,'excluded':True})
        print(label,'cell',str(l),str(h),'ratio',ratio.str(20),'floor',qfloor,flush=True)
    result={**common,'started_utc':utc,'utc':datetime.now(timezone.utc).isoformat(),
            'origin_identities_exact':True,'a0_approx':ar(a0).str(50),'origin_margin':ar(a0-(5*c-4)).str(50),
            'H_max':H.str(100),'s_maximizer':sstar.str(100),'mode_hashes':modefiles,
            'mode_comparison_count':comparison_count,'cell_comparison_count':sum(len(row['comparisons']) for row in cells),
            'seven_cells':cells,'all_seven_excluded':True,'elapsed_seconds':time.monotonic()-start,
            'scope':'Registered origin-inverse dyadic sufficient scheme only; no claim about all exact solutions.'}
    write(BASE/f'verification/{label}_result.json',result)
    print(label,'SUCCESS seconds',result['elapsed_seconds'],flush=True)
if __name__=='__main__': main(sys.argv[1])
