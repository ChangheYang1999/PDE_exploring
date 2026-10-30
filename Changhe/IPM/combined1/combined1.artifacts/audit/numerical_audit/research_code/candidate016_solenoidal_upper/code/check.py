"""Complete candidate016 cross moments for divergence-free upper corrections."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util, json, os, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
R = Path(__file__).resolve().parents[3]
B = R/'research/candidate016_solenoidal_upper'
CID = 'C1-N1-016-legqs25-quot013'
RAW = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
sys.set_int_max_str_digits(0)
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
def log(*s): print(now(), *s, flush=True)
def save(p, d):
    with Path(p).open('x') as f: json.dump(d, f, indent=2); f.write('\n')
def aq(q):
    q=Q(q); return arb(q.numerator)/arb(q.denominator)
def floorq(x, places=24):
    m,e=x.lower().man_exp(); m,e=int(m),int(e)
    v=Fraction(m*2**e) if e>=0 else Fraction(m,2**(-e)); den=10**places
    q=Q(v.numerator*den//v.denominator-1,den)
    assert aq(q)<x.lower()
    return q
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    ctx.prec=4096; started=time.monotonic(); inputs={}; checks={}
    assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
    for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']: assert os.environ[k]=='1'
    def bind(p,h=None):
        p=Path(p); got=sha(p); key=str(p.relative_to(R))
        assert h is None or h==got,(key,h,got)
        assert key not in inputs or inputs[key]==got
        inputs[key]=got; return p
    def read(p,h=None):return json.loads(bind(p,h).read_text())
    def check(k,ok):
        assert k not in checks; checks[k]=bool(ok); assert ok,k
    first=read(B/'verification/PROOF_FIRST.json')
    bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
    manifest=read(B/'source/MANIFEST.json',first['manifest_sha256'])
    for name,rec in manifest['files'].items():bind(B/'source'/name,rec['sha256'])
    fixtures=read(B/'source/own_fixtures.json')
    lower=read(R/'research/candidate016_dual_lower/verification/result.json',
               'e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa')
    check('own_dual_reproduction_accepted',lower['check_count']==38 and all(lower['checks'].values()))
    for rel,h in lower['inputs'].items():bind(R/rel,h)
    bind(R/'research/candidate016_dual_lower/CUTOFF_CLARIFICATION_v01.md')
    oldrows={n:read(R/f'research/candidate016_dual_lower/verification/mode_{n:03d}.json') for n in [1,3]}
    peer=read(R/'research/candidate016_dual_lower/source/N3_exact_vectors.json')
    check('frozen_vectors_candidate',peer['id']==CID and peer['source_sha256']==RAW)
    check('distinct_trial_modes',[row['n'] for row in peer['modes']]==[1,3])
    rawp=R/f'research/candidate_audits/data/{CID}/quot013_legqs25_m9to15_cpu_m16_exact.json'
    raw=read(rawp,RAW)
    check('shared_raw_unchanged',sha(R.parent/'c1-shared/candidate_snapshots'/CID/rawp.name)==RAW)
    sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
    import fields_joint as J
    import weak as W
    M=load('own_solenoidal_moments',R/'research/rational_pole_moments/code/moments.py')
    T,V=J.T,J.V
    def D(P,b):return (1-2*b*T)*P+2*T*V*P.derivative()
    def integral(P,e):
        assert e>-1
        return sum((x/(e+j+1) for j,x in enumerate(P(V))),Q(0))/2
    # Independent rational differentiation in r verifies D, D^2 and the sign.
    X=Poly([0,1]); Y=1+X*X
    def deriv(pair):
        n,d=pair;return n.derivative()*d-n*d.derivative(),d*d
    def logarithmic(pair):
        n,d=deriv(pair);return X*n,d
    def prediction(P,b):
        degree=P.degree(); den=Y**(b+degree)
        num=sum((q*X**(2*j+1)*Y**(degree-j) for j,q in enumerate(P)),Poly())
        return num,den
    manufactured=[]
    for case in fixtures['cases']:
        n,beta,k=case['n'],Q(case['beta']),case['k'];b=beta-1
        assert beta.denominator==1
        P=T**(k+1);P1=D(P,b);P2=D(P1,b)
        rational=(X**(3+2*k),Y**int(beta+k))
        for order,target in [(1,P1),(2,P2)]:
            rational=logarithmic(rational);pred=prediction(target,int(b))
            check(f'fixture{n}_direct_log_derivative{order}',rational[0]*pred[1]==pred[0]*rational[1])
        e=2*b-2; d=integral(P1*P1+n*n*P*P,e)
        a=integral(P1*P1+P2*P2/(n*n),e)
        S,rem=divmod(n*n*P-P2,T);check(f'fixture{n}_regular_source',not rem)
        cross=integral(T*S*P2/(n*n),e)
        p=integral(T*S*P,e);full=integral(T*T*S*S/(n*n),e)
        check(f'fixture{n}_nonzero_a',a>0)
        check(f'fixture{n}_manufactured_sign',cross==-a)
        check(f'fixture{n}_manufactured_pairing',p==d)
        check(f'fixture{n}_exact_upper_identity',full-cross*cross/a==d)
        manufactured.append({'n':n,'d_over_pi':str(d),'a_over_pi':str(a),
                             'b_over_pi':str(cross),'M2_over_pi':str(full)})
    model=J.ScaledRadial(raw)
    check('exact_c',str(model.c)=='4076476460239181/2251799813685248')
    save(B/'verification/start_v01.json',{'utc':now(),'inputs':inputs,'precision_bits':ctx.prec})
    log('START',len(inputs),'bindings',time.monotonic()-started)
    records=[];sumfloor=Q(0)
    for vector in peer['modes']:
        n=vector['n'];tick=time.monotonic();pby={}
        for label,xtext in vector['x_rational'].items():
            bst,kst=label.rsplit(',',1);beta,k,x=Q(bst),int(kst),Q(xtext)
            assert beta>Q(3,2) and k>=-1 and 3+2*k>=n and (3+2*k-n)%2==0
            b=beta-1;pby[b]=pby.get(b,Poly())+x*T**(k+1)
        check(f'mode{n}_nonzero_polynomials',bool(pby) and any(pby.values()))
        firsts={b:D(P,b) for b,P in pby.items()};seconds={b:D(firsts[b],b) for b in pby}
        agroups={}; dgroups={}
        for b,P in pby.items():
            for c,S in pby.items():
                e=b+c-2;assert e>-1
                agroups[e]=agroups.get(e,Poly())+firsts[b]*firsts[c]+seconds[b]*seconds[c]/(n*n)
                dgroups[e]=dgroups.get(e,Poly())+firsts[b]*firsts[c]+n*n*P*S
        avals=[(e,integral(P,e)) for e,P in sorted(agroups.items())]
        a=sum((v for e,v in avals),Q(0));d=sum((integral(P,e) for e,P in dgroups.items()),Q(0))
        check(f'mode{n}_positive_exact_a',a>0)
        check(f'mode{n}_old_gradient_energy',d==Q(oldrows[n]['gradient_energy_over_pi_exact']))
        log('POSITIVE_EXACT_A',n,'groups',len(agroups),'seconds',time.monotonic()-tick)
        projection,pairs=W.project(model,n);ph=J.field_hash(projection)
        check(f'mode{n}_complete_projection_hash',ph==oldrows[n]['complete_projection_sha256'])
        check(f'mode{n}_all_projection_pairs',pairs==oldrows[n]['complete_projection_pairs'])
        groups={}
        for ell,A in projection.items():
            for b,P2 in seconds.items():
                e=ell*model.delta/2+b-3
                groups[e]=groups.get(e,J.Rat())+J.Rat(T*P2/(n*n))*A
        cross=arb(0); evidence=[];minimum=10**9
        for i,(e,A) in enumerate(sorted(groups.items())):
            if not A:continue
            numerator=A.numerator_v();order=0
            while numerator and numerator[0]==0:
                numerator,remainder=divmod(numerator,T);assert not remainder;order+=1
            assert numerator and e+order>-1
            factors=[(scale,power) for scale,power in zip(J.SCALES,A.powers) if power]
            value,info=M.integral(e+order,numerator,factors)
            assert value.is_finite() and value.rel_accuracy_bits()>150 and info['exact_reconstruction']
            minimum=min(minimum,value.rel_accuracy_bits());cross+=value
            evidence.append({'exponent':str(e),'endpoint_order':order,'numerator_sha256':sha256(str(numerator).encode()).hexdigest(),
                             'integral_ball':value.str(200),'decomposition':info})
            if (i+1)%16==0:log('CROSS_GROUPS',n,i+1,len(groups),'seconds',time.monotonic()-tick)
        cross*=arb.pi()/2
        check(f'mode{n}_signed_cross_accuracy',cross.is_finite() and cross.rel_accuracy_bits()>150)
        improvement=cross**2/(arb.pi()*aq(a))
        check(f'mode{n}_positive_improvement',improvement>0 and improvement.rel_accuracy_bits()>150)
        floor=max(Q(0),floorq(improvement));sumfloor+=floor
        check(f'mode{n}_directed_improvement_floor',aq(floor)<improvement.lower())
        row={'utc':now(),'n':n,'a_over_pi_exact':str(a),'old_d_over_pi_exact':str(d),
             'a_group_integrals_over_pi':[{'exponent':str(e),'value':str(v)} for e,v in avals],
             'b_ball':cross.str(200),'b_squared_over_a_ball':improvement.str(200),
             'improvement_strict_lower_exact':str(floor),'complete_projection_sha256':ph,
             'complete_projection_pairs':pairs,'cross_groups':evidence,'minimum_accuracy_bits':minimum,
             'inputs':inputs,'elapsed_seconds':time.monotonic()-tick}
        save(B/f'verification/mode_{n:03d}.json',row);records.append(row)
        log('MODE_COMPLETE',n,'improvement>',str(floor),'seconds',row['elapsed_seconds'])
    for name,mod in list(sys.modules.items()):
        source=getattr(mod,'__file__',None)
        if source:
            path=Path(source).resolve()
            if path.suffix=='.py' and path.is_relative_to(R):check('import_bound:'+name,str(path.relative_to(R)) in inputs)
    for rel,h in inputs.items():assert sha(R/rel)==h,rel
    result={'utc':now(),'candidate':CID,'raw_sha256':RAW,'precision_bits':ctx.prec,'inputs':inputs,
            'checks':checks,'check_count':len(checks),'manufactured_checks':manufactured,
            'modes':[{'n':row['n'],'record':f"research/candidate016_solenoidal_upper/verification/mode_{row['n']:03d}.json",
                      'sha256':sha(B/f"verification/mode_{row['n']:03d}.json"),
                      'improvement_strict_lower_exact':row['improvement_strict_lower_exact']} for row in records],
            'improvement_sum_strict_lower_exact':str(sumfloor),'peer_code_executed':False,
            'complete_Hardy_assembly':'OPEN; requires separately accepted complete M2 upper',
            'analytic_review':'T4 proof plus own independent derivation; Opus follow-up read at final assembly',
            'elapsed_seconds':time.monotonic()-started,
            'verdict':'CONFIRMED complete candidate cross integrals and exact positive trial energies; no standalone H upper value in this record'}
    save(B/'verification/result.json',result)
    log('COMPLETE','improvement sum>',str(sumfloor),'checks',len(checks),'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
