"""Own complete sixteen-mode dual and solenoidal moments, with replayable exports."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util, json, os, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
R=Path(__file__).resolve().parents[3]
B=R/'research/candidate016_multimode_dual_cross'
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
def floorq(x,places=40):
    m,e=x.lower().man_exp();m,e=int(m),int(e)
    v=Fraction(m*2**e) if e>=0 else Fraction(m,2**(-e));den=10**places
    out=Q(v.numerator*den//v.denominator-1,den)
    assert aq(out)<x.lower();return out
def inside(small,large):return large.lower()<small.lower() and small.upper()<large.upper()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def polyhash(P):
    h=sha256();h.update(str(len(P)).encode()+b'\n')
    for q in P:h.update(str(q).encode()+b'\n')
    return h.hexdigest()
def main():
    ctx.prec=4096;start=time.monotonic();inputs={};checks={}
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:assert os.environ[k]=='1'
    def bind(p,h=None):
        p=Path(p);v=sha(p);key=str(p.relative_to(R))
        assert h is None or h==v,(key,h,v)
        assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
    def read(p,h=None):return json.loads(bind(p,h).read_text())
    def check(k,ok):
        assert k not in checks;checks[k]=bool(ok);assert ok,k
    first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
    manifest=read(B/'source/MANIFEST.json',first['manifest_sha256'])
    for name,rec in manifest['files'].items():bind(B/'source'/name,rec['sha256'])
    peer=read(B/'source/N3_full_vectors.json','be23f5d3debcaebd6c14f850404d49bf7e579770c1db5396463fe7be0edf4834')
    check('peer_identity',peer['id']==CID and peer['source_sha256']==RAW and peer['code_sha256']==sha(B/'source/N3_legqs_hdual.py'))
    modes=list(range(1,32,2));check('sixteen_distinct_modes',[v['n'] for v in peer['modes']]==modes)
    archive=read(R/'research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6')
    check('accepted_archive',archive['check_count']==566 and all(archive['checks'].values()))
    for rel,h in archive['inputs'].items():bind(R/rel,h)
    for row in archive['rows']:bind(R/row['group_record'],row['group_sha256'])
    olddual=read(R/'research/candidate016_dual_lower/verification/result.json','e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
    oldcross=read(R/'research/candidate016_solenoidal_upper/verification/result.json','e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603')
    deepdual={v['n']:Q(v['strict_floor_exact']) for v in archive['rows'] if v['kind']=='dual'}
    deepcross={v['n']:Q(v['strict_floor_exact']) for v in archive['rows'] if v['kind']=='cross'}
    accepted=read(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
    for rel,h in accepted['inputs'].items():bind(R/rel,h)
    check('accepted_four_components',all(accepted['checks'].values()))
    production=read(R/'research/candidate016_scaled_norm_peer/source/N4_norms_partial_v01.json','7e7b51a4473936d0ee9803fb12df45851ab42a10c0974787feed7c6728e0a58c')
    for rel,h in production['inputs'].items():bind(R/rel,h)
    expected=production['fields']['D0_0'];check('accepted_complete_field_size',expected['component_count']==1360)
    reference={tuple(v['key']):v for v in expected['components']}
    rawp=R/f'research/candidate_audits/data/{CID}/quot013_legqs25_m9to15_cpu_m16_exact.json';raw=read(rawp,RAW)
    check('shared_candidate_unchanged',sha(R.parent/'c1-shared/candidate_snapshots'/CID/rawp.name)==RAW)
    sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
    import fields_joint as J
    import weak as W
    M=load('own_multimode_positive_poles',R/'research/rational_pole_moments/code/moments.py')
    T,V=J.T,J.V;model=J.ScaledRadial(raw)
    check('exact_delta',str(model.delta)=='1824676646553933/4076476460239181')
    def D(P,b):return (1-2*b*T)*P+2*T*V*P.derivative()
    def polynomial_integral(P,e):
        assert e>-1
        return sum((q/(e+j+1) for j,q in enumerate(P(V))),Q(0))/2
    save(B/'verification/start_v01.json',{'utc':now(),'inputs':inputs,'precision_bits':ctx.prec,'saved_ball_digits':650})
    log('START',len(inputs),'bindings')
    rows=[];lower2=Q(0);stronger2=Q(0);improvements=Q(0);strongerimprovements=Q(0);quotient_square_balls=arb(0)
    for vector in peer['modes']:
        tick=time.monotonic();n=vector['n'];pby={}
        for label,text in vector['x_rational'].items():
            bst,kst=label.rsplit(',',1);beta,k,x=Q(bst),int(kst),Q(text)
            assert beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0
            b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
        check(f'n{n}_basis_labels',len(vector['x_rational'])==vector['basis_size'])
        check(f'n{n}_nonzero_trials',bool(pby) and any(pby.values()))
        p1={b:D(P,b) for b,P in pby.items()};p2={b:D(p1[b],b) for b in pby}
        dg,ag={},{}
        for b,P in pby.items():
            for c,S in pby.items():
                e=b+c-2;assert e>-1
                dg[e]=dg.get(e,Poly())+p1[b]*p1[c]+n*n*P*S
                ag[e]=ag.get(e,Poly())+p1[b]*p1[c]+p2[b]*p2[c]/(n*n)
        ds=[{'exponent':str(e),'integral_exact':str(polynomial_integral(P,e))} for e,P in sorted(dg.items())]
        aa=[{'exponent':str(e),'integral_exact':str(polynomial_integral(P,e))} for e,P in sorted(ag.items())]
        d=sum((Q(v['integral_exact']) for v in ds),Q(0));a=sum((Q(v['integral_exact']) for v in aa),Q(0))
        check(f'n{n}_positive_exact_d',d>0);check(f'n{n}_positive_exact_a',a>0)
        check(f'n{n}_peer_exact_energy',d==Q(vector['grad_psi_sq_over_pi_exact']))
        log('EXACT_ENERGIES',n,'seconds',time.monotonic()-tick)
        projection,pairs=W.project(model,n)
        wanted={ell:v for (ell,kind,m),v in reference.items() if kind=='s' and m==n}
        check(f'n{n}_all_reference_branches',set(projection)==set(wanted))
        components=[]
        for ell,A in sorted(projection.items()):
            ref=wanted[ell];P=A.P
            for L,current,target in zip(J.LINEARS,A.powers,ref['powers']):
                if target>=current:P*=L**(target-current)
                else:
                    P,rem=divmod(P,L**(current-target));check(f'n{n}_ell{ell}_exact_denominator_reduction',not rem)
            ph=polyhash(P)
            check(f'n{n}_ell{ell}_full_cartesian_field_identity',P.degree()==ref['degree'] and ph==ref['numerator_sha256'])
            components.append({'ell':ell,'own_powers':list(A.powers),'reference_powers':ref['powers'],'reference_numerator_sha256':ph})
        log('COMPLETE_PROJECTION',n,len(projection),'branches','seconds',time.monotonic()-tick)
        values={};groupfiles=[]
        for kind,tests,factor in [('dual',pby,Q(1)),('cross',p2,Q(1,n*n))]:
            groups={}
            for ell,A in projection.items():
                for b,P in tests.items():
                    e=ell*model.delta/2+b-3
                    groups[e]=groups.get(e,J.Rat())+J.Rat(factor*T*P)*A
            evidence=[];total=arb(0)
            for j,(e,A) in enumerate(sorted(groups.items())):
                if not A:continue
                numerator=A.numerator_v();order=0
                while numerator and numerator[0]==0:
                    numerator,rem=divmod(numerator,T);assert not rem;order+=1
                check(f'n{n}_{kind}_g{j}_endpoint',bool(numerator) and e+order>-1)
                factors=[(scale,power) for scale,power in zip(J.SCALES,A.powers) if power]
                value,info=M.integral(e+order,numerator,factors)
                check(f'n{n}_{kind}_g{j}_moment',value.is_finite() and value.rel_accuracy_bits()>150 and info['exact_reconstruction'])
                text=value.str(650);parsed=arb(text)
                check(f'n{n}_{kind}_g{j}_export',parsed.lower()<=value.lower() and value.upper()<=parsed.upper())
                total+=value
                evidence.append({'exponent':str(e),'endpoint_order':order,'numerator_sha256':sha256(str(numerator).encode()).hexdigest(),'integral_ball':text,'relative_accuracy_bits':value.rel_accuracy_bits(),'decomposition':info})
            path=B/f'verification/n{n:03d}_{kind}_groups.json'
            save(path,{'utc':now(),'n':n,'kind':kind,'precision_bits':ctx.prec,'saved_ball_digits':650,'groups':evidence,'inputs':inputs})
            saved=json.loads(path.read_text());balls=[arb(v['integral_ball']) for v in saved['groups']]
            radius=sum((v.rad() for v in balls),arb(0));replay=sum(balls,arb(0))*arb.pi()/2;full=total*arb.pi()/2
            check(f'n{n}_{kind}_absolute_radius',radius.upper()<aq(Q(1,10**200)))
            check(f'n{n}_{kind}_aggregate_accuracy',replay.rel_accuracy_bits()>600)
            check(f'n{n}_{kind}_replay_contains_full',replay.lower()<=full.lower() and full.upper()<=replay.upper())
            values[kind]=replay
            groupfiles.append({'kind':kind,'record':str(path.relative_to(R)),'sha256':sha(path),'group_count':len(evidence),'sum_absolute_radii_ball':radius.str(650),'pairing_ball':replay.str(650),'full_precision_pairing_ball':full.str(650),'relative_accuracy_bits':replay.rel_accuracy_bits()})
            log('PAIRING_REPLAY',n,kind,len(evidence),'groups','bits',replay.rel_accuracy_bits(),'seconds',time.monotonic()-tick)
        quotient=abs(values['dual'])/(arb.pi()*aq(d)).sqrt();improvement=values['cross']**2/(arb.pi()*aq(a))
        check(f'n{n}_positive_quotient',quotient>0);check(f'n{n}_positive_improvement',improvement>0)
        check(f'n{n}_peer_pairing_display',inside(values['dual'],arb(vector['F_psi'])))
        check(f'n{n}_peer_quotient_display',inside(quotient,arb(vector['LB'])))
        lf=floorq(quotient);jf=floorq(improvement);check(f'n{n}_strict_positive_floors',lf>0 and jf>0)
        lower2+=lf**2;improvements+=jf
        chosenlf=max(lf,deepdual.get(n,Q(0)));chosenjf=max(jf,deepcross.get(n,Q(0)))
        stronger2+=chosenlf**2;strongerimprovements+=chosenjf;quotient_square_balls+=quotient**2
        row={'utc':now(),'n':n,'exact_coefficient_count':len(vector['x_rational']),'beta_count':len(pby),'d_over_pi_exact':str(d),'a_over_pi_exact':str(a),'d_groups':ds,'a_groups':aa,'complete_projection_sha256':J.field_hash(projection),'complete_projection_pairs':pairs,'component_identity_checks':components,'group_records':groupfiles,'quotient_ball':quotient.str(650),'improvement_ball':improvement.str(650),'quotient_strict_lower_exact':str(lf),'improvement_strict_lower_exact':str(jf),'selected_quotient_strict_lower_exact':str(chosenlf),'selected_improvement_strict_lower_exact':str(chosenjf),'inputs':inputs,'elapsed_seconds':time.monotonic()-tick}
        path=B/f'verification/mode_{n:03d}.json';save(path,row)
        rows.append({'n':n,'record':str(path.relative_to(R)),'sha256':sha(path),'quotient_strict_lower_exact':str(lf),'improvement_strict_lower_exact':str(jf),'selected_quotient_strict_lower_exact':str(chosenlf),'selected_improvement_strict_lower_exact':str(chosenjf)})
        log('MODE_COMPLETE',n,'Hquotient',quotient.str(35),'improvement',improvement.str(35),'seconds',row['elapsed_seconds'])
    check('peer_full_trial_sum',inside(quotient_square_balls.sqrt(),arb(peer['H_lower_ball'])))
    check('deeper_selection_not_weaker',stronger2>=lower2 and strongerimprovements>=improvements)
    Hfloor=floorq(aq(lower2).sqrt(),30);strongH=floorq(aq(stronger2).sqrt(),30)
    L={k:Q(accepted['norms'][k]['accepted_lower_exact']) for k in ['G0','G1','P2']}
    core=L['P2']**2+2**14*L['G1']**2+2**18*L['G0']**2
    E2=core+Q(20,21)*2**18*lower2;strongE2=core+Q(20,21)*2**18*stronger2
    Efloor=floorq(aq(E2).sqrt(),12);strongEfloor=floorq(aq(strongE2).sqrt(),12)
    check('actual_E2_order',Efloor>Q(olddual['baseline007_E2_strict_upper_exact']))
    for name,mod in list(sys.modules.items()):
        source=getattr(mod,'__file__',None)
        if source:
            p=Path(source).resolve()
            if p.suffix=='.py' and p.is_relative_to(R):check('import_bound:'+name,str(p.relative_to(R)) in inputs)
    for rel,h in inputs.items():assert sha(R/rel)==h,rel
    result={'utc':now(),'candidate':CID,'raw_sha256':RAW,'precision_bits':ctx.prec,'saved_ball_digits':650,'inputs':inputs,'checks':checks,'check_count':len(checks),'modes':rows,'H_trial_sum_ball':quotient_square_balls.sqrt().str(650),'H_lower_square_exact':str(lower2),'H_strict_lower_exact':str(Hfloor),'improvement_sum_strict_lower_exact':str(improvements),'selected_H_lower_square_exact':str(stronger2),'selected_H_strict_lower_exact':str(strongH),'selected_improvement_sum_strict_lower_exact':str(strongerimprovements),'selection_rule':'maximum within modes1 and3; one trial per angular mode, never add same-mode trials','E2_lower_square_exact':str(E2),'E2_strict_lower_exact':str(Efloor),'selected_E2_lower_square_exact':str(strongE2),'selected_E2_strict_lower_exact':str(strongEfloor),'baseline007_E2_strict_upper_exact':olddual['baseline007_E2_strict_upper_exact'],'actual_E2_007_less_than016':True,'peer_code_executed':False,'complete_upper_assembly':'OPEN until accepted complete M2 and independent analytic review','elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED complete sixteen-mode dual quotients and solenoidal improvements; numerical upper assembly separate'}
    save(B/'verification/result.json',result);log('COMPLETE',len(checks),'checks','H>',str(Hfloor),'E2>',str(Efloor),'seconds',time.monotonic()-start)
if __name__=='__main__':main()
