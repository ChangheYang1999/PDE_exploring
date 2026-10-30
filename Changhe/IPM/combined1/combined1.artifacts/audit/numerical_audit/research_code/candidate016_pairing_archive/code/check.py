"""Recompute and replay650digit exports of all four candidate016 pairings."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,os,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_pairing_archive'
CID='C1-N1-016-legqs25-quot013'
RAW='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def log(*s):print(now(),*s,flush=True)
def save(p,d):
    with Path(p).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def aq(q):
    q=Q(q);return arb(q.numerator)/arb(q.denominator)
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def inside(small,large):return large.lower()<small.lower() and small.upper()<large.upper()
def main():
    ctx.prec=4096;start=time.monotonic();inputs={};checks={}
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:assert os.environ[k]=='1'
    def bind(p,h=None):
        p=Path(p);v=sha(p);key=str(p.relative_to(R));assert h is None or v==h,(key,v,h)
        assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
    def read(p,h=None):return json.loads(bind(p,h).read_text())
    def check(k,ok):
        assert k not in checks;checks[k]=bool(ok);assert ok,k
    first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
    dual=read(R/'research/candidate016_dual_lower/verification/result.json','e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
    cross=read(R/'research/candidate016_solenoidal_upper/verification/result.json')
    check('old_productions_accepted',all(dual['checks'].values()) and all(cross['checks'].values()))
    for source in [dual,cross]:
        for rel,h in source['inputs'].items():bind(R/rel,h)
    bind(R/'research/candidate016_dual_lower/DISPLAY_SCOPE_v01.md')
    bind(R/'research/candidate016_dual_lower/CUTOFF_CLARIFICATION_v01.md')
    peer=read(R/'research/candidate016_dual_lower/source/N3_exact_vectors.json')
    check('exact_vectors_candidate_and_modes',peer['id']==CID and peer['source_sha256']==RAW and [v['n'] for v in peer['modes']]==[1,3])
    old={}
    crosshash={v['n']:v['sha256'] for v in cross['modes']}
    for n in [1,3]:
        old[n]={'dual':read(R/f'research/candidate016_dual_lower/verification/mode_{n:03d}.json'),
                'cross':read(R/f'research/candidate016_solenoidal_upper/verification/mode_{n:03d}.json',crosshash[n])}
    rawp=R/f'research/candidate_audits/data/{CID}/quot013_legqs25_m9to15_cpu_m16_exact.json';raw=read(rawp,RAW)
    check('shared_candidate_unchanged',sha(R.parent/'c1-shared/candidate_snapshots'/CID/rawp.name)==RAW)
    accepted=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
    sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
    import fields_joint as J
    import weak as W
    M=load('own_archive_positive_poles',R/'research/rational_pole_moments/code/moments.py')
    T,V=J.T,J.V;model=J.ScaledRadial(raw)
    def D(P,b):return (1-2*b*T)*P+2*T*V*P.derivative()
    save(B/'verification/start_v01.json',{'utc':now(),'inputs':inputs,'precision_bits':ctx.prec,'saved_ball_digits':650})
    log('START',len(inputs),'bindings')
    rows=[];lower2=Q(0);improvefloor=Q(0)
    for vector in peer['modes']:
        n=vector['n'];tick=time.monotonic();pby={}
        for label,text in vector['x_rational'].items():
            bst,kst=label.rsplit(',',1);beta,k,x=Q(bst),int(kst),Q(text);b=beta-1
            assert beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0
            pby[b]=pby.get(b,Poly())+x*T**(k+1)
        second={b:D(D(P,b),b) for b,P in pby.items()}
        projection,pairs=W.project(model,n);ph=J.field_hash(projection)
        check(f'mode{n}_complete_projection',all(ph==old[n][kind]['complete_projection_sha256'] and pairs==old[n][kind]['complete_projection_pairs'] for kind in ['dual','cross']))
        log('FRESH_PROJECTION',n,'seconds',time.monotonic()-tick)
        for kind,tests in [('dual',pby),('cross',second)]:
            groups={};factor=1 if kind=='dual' else Q(1,n*n)
            for ell,A in projection.items():
                for b,P in tests.items():
                    e=ell*model.delta/2+b-3
                    groups[e]=groups.get(e,J.Rat())+J.Rat(factor*T*P)*A
            prior=old[n][kind]
            previous=prior['pairing_groups' if kind=='dual' else 'cross_groups']
            groups=[(e,A) for e,A in sorted(groups.items()) if A]
            check(f'mode{n}_{kind}_group_count',len(groups)==len(previous))
            evidence=[];total=arb(0)
            for j,((e,A),prev) in enumerate(zip(groups,previous)):
                numerator=A.numerator_v();order=0
                while numerator and numerator[0]==0:
                    numerator,rem=divmod(numerator,T);assert not rem;order+=1
                assert numerator and e+order>-1
                nh=sha256(str(numerator).encode()).hexdigest()
                epkey='exponent_before_order' if kind=='dual' else 'exponent'
                check(f'mode{n}_{kind}_group{j}_exact_identity',prev[epkey]==str(e) and prev['endpoint_order']==order and prev['numerator_sha256']==nh)
                factors=[(scale,power) for scale,power in zip(J.SCALES,A.powers) if power]
                value,info=M.integral(e+order,numerator,factors)
                assert value.is_finite() and value.rel_accuracy_bits()>150 and info['exact_reconstruction']
                text=value.str(650);parsed=arb(text)
                check(f'mode{n}_{kind}_group{j}_containing_export',parsed.lower()<=value.lower() and value.upper()<=parsed.upper())
                total+=value
                evidence.append({'exponent':str(e),'endpoint_order':order,'numerator_sha256':nh,'integral_ball':text,'relative_accuracy_bits':value.rel_accuracy_bits(),'decomposition':info})
                if (j+1)%16==0:log('GROUPS',n,kind,j+1,len(groups),'seconds',time.monotonic()-tick)
            path=B/f'verification/mode_{n:03d}_{kind}_groups.json'
            save(path,{'utc':now(),'n':n,'kind':kind,'precision_bits':ctx.prec,'saved_ball_digits':650,'groups':evidence,'inputs':inputs})
            exported=json.loads(path.read_text());balls=[arb(v['integral_ball']) for v in exported['groups']]
            replayraw=sum(balls,arb(0));radius=sum((v.rad() for v in balls),arb(0))
            replay=replayraw*arb.pi()/2;full=total*arb.pi()/2
            finalkey='pairing_ball' if kind=='dual' else 'b_ball';original=arb(prior[finalkey])
            check(f'mode{n}_{kind}_absolute_radius',radius.upper()<aq(Q(1,10**250)))
            check(f'mode{n}_{kind}_aggregate_accuracy',replay.rel_accuracy_bits()>700)
            check(f'mode{n}_{kind}_contains_full',replay.lower()<=full.lower() and full.upper()<=replay.upper())
            check(f'mode{n}_{kind}_original_final_contains_replay',inside(replay,original))
            denomkey='gradient_energy_over_pi_exact' if kind=='dual' else 'a_over_pi_exact'
            den=Q(prior[denomkey]);assert den>0
            val=abs(replay)/(arb.pi()*aq(den)).sqrt() if kind=='dual' else replay**2/(arb.pi()*aq(den))
            floorkey='quotient_strict_lower_exact' if kind=='dual' else 'improvement_strict_lower_exact'
            floor=Q(prior[floorkey]);check(f'mode{n}_{kind}_saved_floor_replayed',floor>0 and aq(floor)<val.lower())
            if kind=='dual':lower2+=floor**2
            else:improvefloor+=floor
            oldsum=sum((arb(v['integral_ball']) for v in previous),arb(0))
            check(f'mode{n}_{kind}_old_export_cancellation_visible',oldsum.rad()>1)
            row={'utc':now(),'n':n,'kind':kind,'group_count':len(groups),'group_record':str(path.relative_to(R)),'group_sha256':sha(path),'sum_raw_ball':replayraw.str(650),'sum_group_absolute_radii_ball':radius.str(650),'pairing_replayed_ball':replay.str(650),'pairing_full_precision_ball':full.str(650),'original_pairing_ball':prior[finalkey],'quotient_or_improvement_ball':val.str(650),'strict_floor_exact':str(floor),'old200digit_sum_ball':oldsum.str(50),'replay_relative_accuracy_bits':replay.rel_accuracy_bits(),'elapsed_seconds':time.monotonic()-tick}
            save(B/f'verification/mode_{n:03d}_{kind}_replay.json',row);rows.append(row)
            log('REPLAYED',n,kind,'bits',replay.rel_accuracy_bits(),'floor',str(floor))
    check('same_H_lower_square',lower2==Q(dual['H_lower_square_exact']))
    check('same_improvement_floor_sum',improvefloor==Q(cross['improvement_sum_strict_lower_exact']))
    check('H_floor_replayed',aq(Q(dual['H_strict_lower_exact']))<aq(lower2).sqrt().lower())
    L={k:Q(accepted['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
    E2=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2+Q(20,21)*2**18*lower2
    check('same_E2_lower_square',E2==Q(dual['E2_lower_square_exact']))
    check('E2_floor_replayed',aq(Q(dual['E2_strict_lower_exact']))<aq(E2).sqrt().lower())
    check('actual_E2_order_replayed',Q(dual['E2_strict_lower_exact'])>Q(dual['baseline007_E2_strict_upper_exact']))
    for name,mod in list(sys.modules.items()):
        source=getattr(mod,'__file__',None)
        if source:
            p=Path(source).resolve()
            if p.suffix=='.py' and p.is_relative_to(R):check('import_bound:'+name,str(p.relative_to(R)) in inputs)
    for rel,h in inputs.items():assert sha(R/rel)==h,rel
    result={'utc':now(),'candidate':CID,'raw_sha256':RAW,'precision_bits':ctx.prec,'saved_ball_digits':650,'inputs':inputs,'checks':checks,'check_count':len(checks),'rows':rows,'H_strict_lower_exact':dual['H_strict_lower_exact'],'E2_strict_lower_exact':dual['E2_strict_lower_exact'],'improvement_sum_strict_lower_exact':str(improvefloor),'actual_E2_007_less_than016':True,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED fresh complete pairings and standalone650digit group replay of saved floors; H upper assembly separate'}
    save(B/'verification/result.json',result);log('COMPLETE',len(checks),'checks',time.monotonic()-start)
if __name__=='__main__':main()
