"""Own source projection and moment replay for candidate017 dual/residual trials."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util, json, os, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
R=Path(__file__).resolve().parents[3]
B=R/'research/candidate017_dual_residual_replay'
CID='C1-N1-017-legqs50-quot013'
RAW='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def log(*s):print(now(),*s,flush=True)
def save(p,d):
    with Path(p).open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def aq(q):
    q=Q(q);return arb(q.numerator)/arb(q.denominator)
def endpointq(x,upper=False,places=40):
    y=x.upper() if upper else x.lower();m,e=y.man_exp();m,e=int(m),int(e)
    v=Fraction(m*2**e) if e>=0 else Fraction(m,2**(-e));den=10**places
    out=Q(v.numerator*den//v.denominator+(2 if upper else -1),den)
    assert aq(out)>x.upper() if upper else aq(out)<x.lower();return out

def inside(small,large):return large.lower()<small.lower() and small.upper()<large.upper()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    ctx.prec=4096;start=time.monotonic();inputs={};checks={}
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:assert os.environ[k]=='1'
    def bind(p,h=None):
        p=Path(p);v=sha(p);key=str(p.relative_to(R));assert h is None or h==v,(key,h,v)
        assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
    def read(p,h=None):return json.loads(bind(p,h).read_text())
    def check(k,ok):
        assert k not in checks;checks[k]=bool(ok);assert ok,k
    schema=read(B/'verification/PROOF_FIRST_v03.json');bind(B/'SCHEMA_PROOF_v03.md',schema['supplement_sha256']);check('schema_before_v03',not schema['checker_exists'])
    first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
    manifest=read(B/'source/MANIFEST.json',first['manifest_sha256'])
    for name,rec in manifest['files'].items():bind(B/'source'/name,rec['sha256'])
    peer=read(B/'source/N3_dual.json');hres=read(B/'source/N3_hres.json');hardy=read(B/'source/N3_hardy.json')
    for name,obj in [('dual',peer),('hres',hres),('hardy',hardy)]:check(name+'_identity',obj['id']==CID and obj['source_sha256']==RAW)
    check('dual_code_identity',peer['code_sha256']==sha(B/'source/N3_legqs_hdual.py'))
    check('hres_historical_code_identifier_well_formed',len(hres['code_sha256'])==64 and all(c in '0123456789abcdef' for c in hres['code_sha256']))
    historical_hres_code_matches_current=(hres['code_sha256']==sha(B/'source/N3_legqs_hres.py'))
    modes=list(range(1,32,2));check('sixteen_distinct_dual_modes',[v['n'] for v in peer['modes']]==modes)
    check('sixteen_distinct_hres_modes',[v['n'] for v in hres['modes']]==modes)
    # These accepted roots validate the own algorithms and017 source graph.
    # No numerical016 component is transferred to017.
    roots=[('research/candidate016_pairing_archive/verification/result.json','c3e148aaab94ed6b50920f114c80260cb7f0061756398a90f6f444fa6b0367c6'),
           ('research/candidate017_three_weak_peer/verification/result_v02.json',None),
           ('research/candidate017_sector_peer/verification/result.json',None)]
    frozen=read(B/'source/OWN_ROOTS.json')
    for rel,h in roots:
        root=read(R/rel,h or frozen[rel])
        flag=(root['checks']==159 and root['all_three_additional_exact_maps_compared'] and root['first_four_density_stream_profiles_equal007']) if rel.endswith('candidate017_sector_peer/verification/result.json') else all(root['checks'].values())
        check('accepted:'+rel,root['verdict'].startswith('CONFIRMED') and flag)
        for dep,digest in root['inputs'].items():bind(R/dep,digest)
    rawp=R/f'research/candidate_audits/data/{CID}/quot013_legqs50_m9to15_cpu_m16_exact.json';raw=read(rawp,RAW)
    check('shared_candidate_unchanged',sha(R.parent/'c1-shared/candidate_snapshots'/CID/rawp.name)==RAW)
    for rel,h in frozen.items():bind(R/rel,h)
    sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
    import fields_joint as J
    import weak as W
    M=load('own017_positive_poles',R/'research/rational_pole_moments/code/moments.py')
    T,V=J.T,J.V;model=J.ScaledRadial(raw)
    check('exact_c_delta',str(model.c)=='4076476460239181/2251799813685248' and str(model.delta)=='1824676646553933/4076476460239181')
    def D(P,b):return (1-2*b*T)*P+2*T*V*P.derivative()
    def integralpoly(P,e):
        assert e>-1;return sum((q/(e+j+1) for j,q in enumerate(P(V))),Q(0))/2
    def energies(vector,n,label):
        pby={}
        for key,text in vector['x_rational'].items():
            bst,kst=key.rsplit(',',1);beta,k,x=Q(bst),int(kst),Q(text)
            check(f'n{n}_{label}_admissible_'+key,beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0)
            b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
        check(f'n{n}_{label}_basis_count',len(vector['x_rational'])==vector['basis_size'])
        p1={b:D(P,b) for b,P in pby.items()};p2={b:D(p1[b],b) for b in pby};dg={};ag={}
        for b,P in pby.items():
            for c,S in pby.items():
                e=b+c-2;assert e>-1
                dg[e]=dg.get(e,Poly())+p1[b]*p1[c]+n*n*P*S
                ag[e]=ag.get(e,Poly())+p1[b]*p1[c]+p2[b]*p2[c]/(n*n)
        ds=[{'exponent':str(e),'integral_exact':str(integralpoly(P,e))} for e,P in sorted(dg.items())]
        aa=[{'exponent':str(e),'integral_exact':str(integralpoly(P,e))} for e,P in sorted(ag.items())]
        d=sum((Q(v['integral_exact']) for v in ds),Q(0));a=sum((Q(v['integral_exact']) for v in aa),Q(0))
        check(f'n{n}_{label}_energy_positive',d>0 and a>0)
        check(f'n{n}_{label}_exact_peer_energy',d==Q(vector['grad_psi_sq_over_pi_exact']))
        return pby,p2,d,a,ds,aa
    def moments(groups,n,label):
        evidence=[];total=arb(0)
        for j,(e,A) in enumerate(sorted(groups.items())):
            if not A:continue
            numerator=A.numerator_v();order=0
            while numerator and numerator[0]==0:
                numerator,rem=divmod(numerator,T);assert not rem;order+=1
            check(f'n{n}_{label}_g{j}_endpoint',bool(numerator) and e+order>-1)
            factors=[(scale,power) for scale,power in zip(J.SCALES,A.powers) if power]
            value,info=M.integral(e+order,numerator,factors)
            check(f'n{n}_{label}_g{j}_moment',value.is_finite() and value.rel_accuracy_bits()>150 and info['exact_reconstruction'])
            text=value.str(650);parsed=arb(text)
            check(f'n{n}_{label}_g{j}_outward_export',parsed.lower()<=value.lower() and value.upper()<=parsed.upper())
            total+=value;evidence.append({'exponent':str(e),'endpoint_order':order,'numerator_sha256':sha256(str(numerator).encode()).hexdigest(),'integral_ball':text,'relative_accuracy_bits':value.rel_accuracy_bits(),'decomposition':info})
        path=B/f'verification/n{n:03d}_{label}_groups.json';save(path,{'utc':now(),'n':n,'kind':label,'precision_bits':ctx.prec,'saved_ball_digits':650,'groups':evidence,'inputs':inputs})
        saved=json.loads(path.read_text());balls=[arb(v['integral_ball']) for v in saved['groups']]
        radius=sum((v.rad() for v in balls),arb(0));replay=sum(balls,arb(0))*arb.pi()/2;full=total*arb.pi()/2
        check(f'n{n}_{label}_absolute_radius',radius.upper()<aq(Q(1,10**200)))
        check(f'n{n}_{label}_aggregate_accuracy',replay.rel_accuracy_bits()>600)
        check(f'n{n}_{label}_replay_contains_full',replay.lower()<=full.lower() and full.upper()<=replay.upper())
        rec={'kind':label,'record':str(path.relative_to(R)),'sha256':sha(path),'group_count':len(evidence),'sum_absolute_radii_ball':radius.str(650),'value_ball':replay.str(650),'relative_accuracy_bits':replay.rel_accuracy_bits()}
        log('MOMENT_REPLAY',n,label,len(evidence),'bits',replay.rel_accuracy_bits());return replay,rec
    def pairing(projection,tests,n,label,factor=Q(1)):
        groups={}
        for ell,A in projection.items():
            for b,P in tests.items():
                e=ell*model.delta/2+b-3;groups[e]=groups.get(e,J.Rat())+J.Rat(factor*T*P)*A
        return moments(groups,n,label)
    save(B/'verification/start_v01.json',{'utc':now(),'inputs':inputs,'precision_bits':ctx.prec,'saved_ball_digits':650})
    log('START',len(inputs),'bindings');rows=[];lower2=Q(0);sumquotients=arb(0)
    hr={r['n']:r for r in hres['modes']};hy={r['n']:r for r in hardy['modes']}
    for vector in peer['modes']:
        tick=time.monotonic();n=vector['n'];pby,p2,d,a,ds,aa=energies(vector,n,'dual')
        projection,pairs=W.project(model,n)
        check(f'n{n}_complete_projection_nonempty',bool(projection) and all(projection.values()))
        log('PROJECTION',n,len(projection),'branches','seconds',time.monotonic()-tick)
        p,prec=pairing(projection,pby,n,'dual');quotient=abs(p)/(arb.pi()*aq(d)).sqrt()
        check(f'n{n}_peer_dual_pairing_containment',inside(p,arb(vector['F_psi'])))
        check(f'n{n}_peer_dual_quotient_containment',inside(quotient,arb(vector['LB'])))
        l=endpointq(quotient);check(f'n{n}_strict_positive_dual',l>0);lower2+=l*l;sumquotients+=quotient**2
        row={'utc':now(),'n':n,'dual_exact_coefficient_count':len(vector['x_rational']),'dual_beta_count':len(pby),'dual_d_over_pi_exact':str(d),'dual_a_over_pi_exact':str(a),'dual_d_groups':ds,'dual_a_groups':aa,'complete_projection_sha256':J.field_hash(projection),'complete_projection_pairs':pairs,'complete_projection_components':len(projection),'dual_group_record':prec,'dual_quotient_ball':quotient.str(650),'dual_quotient_strict_lower_exact':str(l),'inputs':inputs}
        if n in [1,3]:
            rb,r2,rd,ra,rds,ras=energies(hr[n],n,'hres');rp,rprec=pairing(projection,rb,n,'hres_dual');rbval,rbrec=pairing(projection,r2,n,'hres_cross',Q(1,n*n))
            groups={}
            for ell,A in projection.items():
                for ell2,C in projection.items():
                    e=(ell+ell2)*model.delta/2-4;groups[e]=groups.get(e,J.Rat())+J.Rat(T*T)*A*C
            qn,qrec=moments(groups,n,'rF_square')
            check(f'n{n}_rF_positive',qn>0)
            check(f'n{n}_peer_rF_square',inside(qn,arb(hy[n]['rF_n_sq'])))
            check(f'n{n}_peer_hres_rF',inside(qn.sqrt(),arb(hr[n]['rFn'])))
            dd=arb.pi()*aq(rd);aa2=arb.pi()*aq(ra);rg2=qn+2*n*n*(rbval-rp)+n*n*(aa2+dd)
            check(f'n{n}_residual_square_positive_accurate',rg2>0 and rg2.rel_accuracy_bits()>600)
            rg=rg2.sqrt();grad=dd.sqrt();resquot=abs(rp)/grad;lb2=grad-rg/n;ub=grad+rg/n
            check(f'n{n}_hres_grad_containment',inside(grad,arb(hr[n]['grad_psi'])))
            check(f'n{n}_hres_residual_containment',inside(rg,arb(hr[n]['residual_r_g'])))
            lower=max(endpointq(resquot),endpointq(lb2));upper=endpointq(ub,True)
            check(f'n{n}_hres_bounds_consistent',aq(lower)<ub.lower() and ub<qn.sqrt()/n)
            row['residual_trial']={'coefficient_count':len(hr[n]['x_rational']),'beta_count':len(rb),'d_over_pi_exact':str(rd),'a_over_pi_exact':str(ra),'d_groups':rds,'a_groups':ras,'pairing':rprec,'cross':rbrec,'rF_square':qrec,'rF_square_ball':qn.str(650),'residual_square_ball':rg2.str(650),'residual_ball':rg.str(650),'gradient_ball':grad.str(650),'duality_quotient_ball':resquot.str(650),'triangle_lower_ball':lb2.str(650),'upper_ball':ub.str(650),'H_mode_strict_lower_exact':str(lower),'H_mode_strict_upper_exact':str(upper)}
            log('HRES_COMPLETE',n,'Hn lower',str(lower),'upper',str(upper),'residual',rg.str(30))
        row['elapsed_seconds']=time.monotonic()-tick;row['utc']=now();path=B/f'verification/mode_{n:03d}.json';save(path,row)
        rows.append({'n':n,'record':str(path.relative_to(R)),'sha256':sha(path),'quotient_strict_lower_exact':str(l),'independent_hres':n in [1,3]})
        log('MODE_COMPLETE',n,'dual',quotient.str(35),'seconds',row['elapsed_seconds'])
    total=sumquotients.sqrt();check('full_peer_dual_sum_containment',inside(total,arb(peer['H_lower_ball'])))
    Hfloor=endpointq(aq(lower2).sqrt(),places=30)
    for name,mod in list(sys.modules.items()):
        source=getattr(mod,'__file__',None)
        if source:
            p=Path(source).resolve()
            if p.suffix=='.py' and p.is_relative_to(R):check('import_bound:'+name,str(p.relative_to(R)) in inputs)
    for rel,h in inputs.items():assert sha(R/rel)==h,rel
    result={'utc':now(),'candidate':CID,'raw_sha256':RAW,'precision_bits':ctx.prec,'saved_ball_digits':650,'inputs':inputs,'checks':checks,'check_count':len(checks),'modes':rows,'H_dual_sum_ball':total.str(650),'H_lower_square_exact':str(lower2),'H_strict_lower_exact':str(Hfloor),'complete_H_upper':'OPEN: other residual/Hardy source integrals not reproduced','complete_E2_and_017_less_than007':'OPEN: G0/G1/P2 and complete H upper not independently reproduced','peer_hres_historical_code_matches_frozen_current':historical_hres_code_matches_current,'peer_hres_historical_code_sha256_claimed':hres['code_sha256'],'peer_hres_frozen_current_code_sha256':sha(B/'source/N3_legqs_hres.py'),'peer_hres_historical_code_execution_provenance':'UNOBSERVED; exact proposed vectors checked by own formulas','peer_code_executed':False,'peer_F_cache_read':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED complete sixteen dual trials and individual residual-trial enclosures for modes1 and3 only'}
    save(B/'verification/result.json',result);log('COMPLETE',len(checks),'checks','H>',str(Hfloor),'seconds',time.monotonic()-start)
if __name__=='__main__':main()
