"""Complete independent016 frozen-vector and factored first-mode tests."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from types import ModuleType
import json,sys,time,importlib.util
from flint import fmpq as Q,fmpq_poly as Poly,arb,acb,ctx
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_remaining_weak';sys.set_int_max_str_digits(0)
sys.path.insert(0,str(R/'research/joint_scaled_factored_weak/code'))
from fields_joint import Rat,ScaledRadial,TR,VR,T,V,SCALES,ar,field_hash
import weak as W

def module(name,rel):
 spec=importlib.util.spec_from_file_location(name,R/rel);out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
moments=module('remaining016_own_moments','research/rational_pole_moments/code/moments.py')
OLD=module('remaining016_own_frozen_probe','research/successor_weak_probes/code/check.py')
JET=module('remaining016_own_cartesian','research/multiscale_generators/code/cartesian.py')
add,put=W.add,W.put
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def save(p,x):
 with Path(p).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def log(*x):print(now(),*x,flush=True)
def construct(model, P, n):
    P = Rat(P)
    radial = (1-4*TR)*P+2*TR*VR*P.derivative()
    px = [(n+1, (radial-n*P)/2), (n-1, (radial+n*P)/2)]
    py = [(n-1, (radial+n*P)/2), (n+1, (n*P-radial)/2)]
    M, Cx, Cy = {}, {}, {}
    put(M, 0, 's', n, (2*model.c+1)*P+model.c*radial)
    for (j, l), A in model.u1.items():
        for freq, W in px:
            G = A.divide_t(2)*W/2
            put(M, j+1, 's', freq+l, G)
            put(M, j+1, 's', freq-l, G)
    for (j, l), A in model.u2.items():
        for freq, W in py:
            G = A.divide_t(2)*W/2
            put(M, j+1, 's', l+freq, G)
            put(M, j+1, 's', l-freq, G)
    for (j, l), A in model.rx.items():
        G = A.divide_t(2)*P/2
        put(Cx, j+1, 'c', n-l, G)
        put(Cx, j+1, 'c', n+l, -G)
    for (j, l), A in model.ry.items():
        G = A.divide_t(2)*P/2
        put(Cy, j+1, 's', n+l, G)
        put(Cy, j+1, 's', n-l, G)
    return [{k: A for k, A in f.items() if A} for f in [M, Cx, Cy]]


def evaluate(field, model, x, y):
    r2 = x*x+y*y
    r = r2.sqrt()
    v, t = 1/(1+r2), r2/(1+r2)
    z = acb(x/r, y/r)
    powers = [acb(1)]
    for i in range(max(k[2] for k in field)):
        powers.append(powers[-1]*z)
    return r*v*v*sum((v**ar(ell*model.delta/2)*A.evaluate(t, v)*
                    (powers[n].imag if kind == 's' else powers[n].real)
                    for (ell, kind, n), A in field.items()), arb(0))


def point_checks(model, P, n, fields):
    out = []
    for xs, ys in [('1/2', '1/2'), ('3', '4'), ('60', '80')]:
        x, y = ar(Q(xs)), ar(Q(ys))
        vals = model.evaluate(xs, ys)
        r2 = x*x+y*y
        r = r2.sqrt()
        v, t = 1/(1+r2), r2/(1+r2)
        z = acb(x/r, y/r)**n
        p = Rat(P).evaluate(t, v)
        radial = (1-4*t)*p+2*t*v*Rat(P.derivative()).evaluate(t, v)
        pr, pt = v*v*radial*z.imag, n*v*v*p*z.real
        px, py = x/r*pr-y/r*pt, y/r*pr+x/r*pt
        phi = r*v*v*p*z.imag
        expected = [(2*ar(model.c)+1)*phi+(ar(model.c)*x+vals['u1'])*px+
                    (ar(model.c)*y+vals['u2'])*py,
                    phi*vals['rho_x'], phi*vals['rho_y']]
        checks = [evaluate(f, model, x, y).overlaps(e) for f, e in zip(fields, expected)]
        assert all(checks), (xs, ys, checks)
        out.append({'x': xs, 'y': ys, 'M_Cx_Cy_overlap': checks})
    return out


def integrate_groups(groups, delta, offset, label):
    total, records = arb(0), []
    for index, (ell, A) in enumerate(sorted(groups.items())):
        tick = time.monotonic()
        b = offset+ell*delta/2
        assert b > -1
        factors = [(a, k) for a, k in zip(SCALES, A.powers) if k]
        value, info = moments.integral(b, V*A.numerator_v(), factors)
        assert value.rel_accuracy_bits() > 150 or not A
        total += value
        info.update({'ell': ell, 'numerator_degree': A.P.degree()+1,
                     'integral': value.str(90),
                     'elapsed_seconds': time.monotonic()-tick})
        records.append(info)
        print(label, index+1, '/', len(groups), 'ell', ell,
              'bits', value.rel_accuracy_bits(), 'seconds', info['elapsed_seconds'], flush=True)
    return arb.pi()/2*total, records


def energy(fields, model, label):
    groups, count = {}, 0
    for field in fields:
        angular = {}
        for (ell, kind, n), A in field.items():
            assert n > 0 and n%2 == 1
            angular.setdefault((kind, n), []).append((ell, A))
        for terms in angular.values():
            for i, (ell, A) in enumerate(terms):
                for j in range(i+1):
                    ell2, B = terms[j]
                    add(groups, ell+ell2, A*B*(1 if i == j else 2))
                    count += 1
    print(label, 'assembled', len(groups), 'groups', count, 'pairs', flush=True)
    value, records = integrate_groups(groups, model.delta, Q(1), label)
    assert value > 0 and value.rel_accuracy_bits() > 150
    return value, records, count, field_hash(groups)


def pairing_parts(model, Mfield):
    rho = {}
    for (j, n), A in model.rho.items():
        rho.setdefault(n, []).append((j+1, A.divide_t(2)))
    groups, count = {}, 0
    for (ell, kind, n), A in Mfield.items():
        assert kind == 's'
        for ell2, B in rho.get(n, []):
            add(groups, ell+ell2, A*B)
            count += 1
    answer, records = integrate_groups(groups, model.delta, Q(-1), 'Iparts')
    return -answer, records, count, field_hash(groups)


def project(model, target):
    result = {}
    for (j, n), A in model.rho.items():
        if n == target:
            TA = TR*A.derivative()
            L = model.c*(2*TA-3*A+2*TR*(model.p[j]*A-TA))-A
            add(result, j+1, L.divide_t(2))
    quadratic, counts = {}, []
    for C, S in [(model.u1, model.rx), (model.ry, model.u2)]:
        count = 0
        for (i, n), A in C.items():
            for (j, m), B in S.items():
                twice = int(m+n == target)+int(m-n == target)-int(m-n == -target)
                if twice:
                    add(quadratic, i+j+2, A*B*Q(twice, 2))
                    count += 1
        counts.append(count)
    for ell, A in quadratic.items():
        add(result, ell, A.divide_t(4))
    return {k: A for k, A in result.items() if A}, counts


def main():
 ctx.prec=2048;started=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or got==h,(p,h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__),prep['code_sha256'])
 peer=read(B/'source/N3_probe.json','e71575779cd09d4c06bb438fdae06b9c1e6b43d63bb99e7263f1db8040a44f82')
 for name,h in peer['code_sha256'].items():bind(R/'research/candidate016_n3_weak_comparison/source'/name,h)
 for rel in ['research/scaled_weak_backend/PROOF.md','research/joint_scaled_factored_weak/PROOF.md','research/rational_pole_moments/PROOF.md','research/angular_probe_audit/PROOF.md','research/optimized_probe_audit/PROOF.md','research/joint_scaled_factored_weak/verification/fields.json','research/joint_scaled_factored_weak/verification/scalar_joint.json','research/joint_scaled_factored_weak/verification/candidate013.json']:
  bind(R/rel)
 queue=[v for v in globals().values() if isinstance(v,ModuleType)]+list(sys.modules.values());seen=set()
 while queue:
  mod=queue.pop()
  if id(mod) in seen:continue
  seen.add(id(mod));file=getattr(mod,'__file__',None)
  if not file:continue
  p=Path(file).resolve()
  if not p.is_relative_to(R) or p.suffix!='.py':continue
  bind(p);queue.extend(x for x in vars(mod).values() if isinstance(x,ModuleType))
 name=peer['id'];snap=R/'research/candidate_audits/data'/name;manifest=read(snap/'MANIFEST.json');src=bind(snap/manifest['coefficient_files'][0]['name'],peer['source_sha256']);bind(snap/'SHA256SUMS')
 assert sha(src)==manifest['coefficient_files'][0]['sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 for line in (snap/'SHA256SUMS').read_text().splitlines():
  h,f=line.split(None,1);f=f.lstrip('*');assert Path(f).name==f;bind(snap/f,h)
 audit=read(R/f'research/generator_sector_audit/verification/{name}_direct.json');assert audit['generator_sha256']==sha(src) and audit['B0n_exact'] and audit['sector_summary']['all_forbidden_zero']
 probes={}
 for n in [1,7]:
  rel,h,accepted=OLD.PROBES[n];pr=read(R/rel,h);bind(R/accepted);probes[n]=pr
  assert pr['probe_coefficients']==peer['probes']['a0.json' if n==1 else 'n7_a0.json']['probe_coefficients'] and Q(pr['a'])==0 and Q(pr['C_U_exact'])==1
 calp=bind(R/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json','153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316')
 startfile=B/f'verification/start_{datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")}.json';save(startfile,{'utc':now(),'inputs':inputs,'proof_first':True})
 model=ScaledRadial(src);assert model.c==Q(peer['cl']);raw=json.loads(src.read_text());cals=ScaledRadial(calp);oldcal=OLD.Radial(calp);fieldcal={}
 for n in [1,7]:
  P=sum((Q(v)*T**int(k) for k,v in probes[n]['probe_coefficients'].items()),Poly([]));assert not any(P[k] for k in range((n-1)//2))
  ours=construct(cals,P,n);theirs=OLD.helper.construct(oldcal,P,n);checks=[set(a)==set(b) and all(a[k]==Rat(b[k]) for k in a) for a,b in zip(ours,theirs,strict=True)];assert all(checks);fieldcal[str(n)]=checks
 log('007_EXACT_FIELDS_PASS',fieldcal)
 cartesian=[]
 for xs,ys in [('3/7','-2/5'),('21','-9'),('3/10','70')]:
  direct=JET.GeneratorJet(raw,xs,ys,4).fields();val=model.evaluate(xs,ys);check={k:val[k].overlaps(direct[k]) for k in val};assert all(check.values());cartesian.append({'x':xs,'y':ys,'fields':check})
 log('016_CARTESIAN_PASS')
 rows={}
 for label,n in [('n7_a0.json',7),('a0.json',1),('firstmode_K2048.json',1)]:
  tick=time.monotonic();out=B/'verification'/label
  if out.exists():
   row=read(out);assert row['code_sha256']==sha(__file__) and row['raw_sha256']==sha(src);assert all(sha(R/p)==h for p,h in row['inputs'].items());rows[label]=row;continue
  pr=peer['probes'][label];assert pr['angular_mode']==n
  if label.startswith('firstmode'):
   K=2048;assert pr['probe_coefficients']=={'2048':'1'};H=Q(4*(2*K+1))*Q(K)**K/Q(K+2)**(K+2);cover=None
   fields=W.construct(model,n,K);points=W.point_checks(model,n,K,fields);Iparts,pc,pp,ph=W.pairing_parts(model,fields[0],K);projection,counts=W.project(model,n);I,ic=W.integrate_groups(projection,model.delta,Q(-1),K+1,'Idirect');M2,mc,mp,mh=W.energy(fields[:1],model,K,'M2');C2,cc,cp,ch=W.energy(fields[1:],model,K,'C2')
   hp=arb(pr['H_upper']);assert ar(H).upper()<hp.lower() and hp.upper()-ar(H).lower()<ar(Q(1,10**300))
  else:
   P=sum((Q(v)*T**int(k) for k,v in probes[n]['probe_coefficients'].items()),Poly([]));H=Q(probes[n]['H_upper_exact']);cover=OLD.helper.gradient_cover(P,n,H);log('GRADIENT',n,len(cover))
   fields=construct(model,P,n);points=point_checks(model,P,n,fields);Iparts,pc,pp,ph=pairing_parts(model,fields[0]);projection,counts=W.project(model,n);I,ic=integrate_groups({ell:A*P for ell,A in projection.items()},model.delta,Q(-1),'Idirect');M2,mc,mp,mh=energy(fields[:1],model,'M2');C2,cc,cp,ch=energy(fields[1:],model,'C2');assert ar(H).overlaps(arb(pr['H_upper']))
  assert I.overlaps(Iparts) and min(I.rel_accuracy_bits(),Iparts.rel_accuracy_bits())>150
  M,C=M2.sqrt(),C2.sqrt();D=M+C;root=2*abs(I)/(D+(D*D+4*ar(H)*abs(I)).sqrt());floor=Q(int((root.lower()*10**18).floor().unique_fmpz())-1,10**18);assert floor>0 and ar(floor)<root
  comparisons={}
  for key,z in [('pairing_signed',I),('M',M),('C',C),('radius',root)]:
   pb=arb(pr[key]);assert pb.lower()<z.lower() and z.upper()<pb.upper();comparisons[key]={'own':z.str(100),'peer':pr[key],'strict_containment':True}
  assert all(sha(R/p)==h for p,h in inputs.items())
  row={'utc':now(),'candidate':name,'raw_sha256':sha(src),'code_sha256':sha(__file__),'inputs':inputs.copy(),'source_start':str(startfile.relative_to(R)),'source_start_sha256':sha(startfile),'n':n,'probe':label,'probe_coefficients':pr['probe_coefficients'],'exact007_field_calibration':fieldcal,'Cartesian_points':cartesian,'point_checks':points,'pairing':I.str(100),'pairing_parts':Iparts.str(100),'M':M.str(100),'C':C.str(100),'M2':M2.str(100),'C2':C2.str(100),'H_exact':str(H),'H_cover':cover,'radius':root.str(100),'strict_floor':str(floor),'direct_parts_overlap':True,'all_background_modes_retained':True,'whole_plane':True,'direct_moments':ic,'parts_moments':pc,'M_moments':mc,'C_moments':cc,'group_hashes':{'M':mh,'C':ch,'parts':ph},'projection_hash':field_hash(projection),'projection_pairs':counts,'peer_comparisons':comparisons,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED complete independent moments and displayed N3 root; conditional fixed-c distance only'}
  save(out,row);rows[label]=row;log('DONE',label,root.str(40),sha(out))
 result={'utc':now(),'inputs':inputs,'rows':{k:{'path':str((B/'verification'/k).relative_to(R)),'sha256':sha(B/'verification'/k),'strict_floor':v['strict_floor']} for k,v in rows.items()},'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED remaining three N3 weak probes under PROOF hypotheses; no existence or full-norm claim'};save(B/'verification/result.json',result);log('ALL_DONE',sha(B/'verification/result.json'))
if __name__=='__main__':main()
