"""Field and complete candidate013 calibrations for radius50 factored weak tests."""
from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,sys,time
from hashlib import sha256
from flint import arb,ctx,fmpq as Q,fmpq_poly as Poly
from fields50 import Rat,ScaledRadial,T,V,TR,LINEARS,ar,field_hash
import weak as W
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled50_factored_weak'
sys.set_int_max_str_digits(0)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
J=module('n4_factored50_cartesian',ROOT/'research/multiscale_generators/code/cartesian.py')
R=module('n4_factored50_radial',ROOT/'research/radial_fourier/code/radial.py')
O=module('n4_factored50_oldfields',ROOT/'research/scaled_weak_backend/code/fields.py')
sys.path.insert(0,str(ROOT/'research/scaled_weak_backend/code'))
OW=module('n4_factored50_oldweak',ROOT/'research/scaled_weak_backend/code/weak_v3.py')
# Use the identical legacy class object loaded by its own weak module.
O=sys.modules['fields']
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def write(name,record):
    with (BASE/'verification'/name).open('x') as f:json.dump(record,f,indent=2);f.write('\n')
def convert(A):return Rat(A.P,(A.powers[0],0,A.powers[1]))
def equal(left,right,conversion):
    return set(left)==set(right) and all(left[k]==conversion(P) for k,P in right.items())
def gradient(K,n,bound):
    v=Poly([0,1]);B=2*K+4
    q=v*v*(-3+B*v);eq=Poly([-6,9*K+18,-B*(K+3)])
    assert (1-v)*q.derivative()-K*q==v*eq
    disc=3*(K+2)*(11*K+6);assert disc==(9*K+18)**2-24*B*(K+3)
    root=arb(disc).sqrt();rr=[((9*K+18)-root)/(2*B*(K+3)),((9*K+18)+root)/(2*B*(K+3))]
    assert all(0<x and x<1 for x in rr)
    amplitudes=[abs(x*x*(1-x)**K*(-3+B*x)) for x in rr]
    x=ar(Q(2,K+2));amplitudes.append(n*x*x*(1-x)**K)
    assert all(a<ar(bound) for a in amplitudes)
    return {'critical_equation':[str(c) for c in eq],'discriminant':disc,'radial_roots':[x.str(100) for x in rr],'amplitudes':[x.str(100) for x in amplitudes],'angular_root_exact':str(Q(2,K+2)),'H_upper_exact':str(bound),'strict_bound_all_critical_points':True,'endpoint_values_exact':['0','0']}

def main():
    start=time.monotonic();ctx.prec=2048
    a=Rat(Poly([1,2,3]),(2,3,1));b=Rat(Poly([2,-1]),(1,2,2));checks=[]
    for t in [Q(0),Q(1,10),Q(1,2),Q(1)]:
        checks.extend([(a+b).exact_value(t)==a.exact_value(t)+b.exact_value(t),(a*b).exact_value(t)==a.exact_value(t)*b.exact_value(t)])
    N=a.P;D=LINEARS[0]**2*LINEARS[1]**3*LINEARS[2]
    checks.extend([a.derivative()==Rat(N.derivative()*D-N*D.derivative(),(4,6,2)),Rat(D,(2,3,1))==1,Rat(D,(2,3,1)).derivative()==0,(a*TR**4).divide_t(4)==a]);assert all(checks)
    fixtures=[{'cl_exact':'7/4','generators':[
        {'j':0,'m':0,'spec':['mono',0],'coef':'2/7'},
        {'j':1,'m':1,'spec':['leg',2,3],'coef':'-3/11'},
        {'j':2,'m':2,'spec':['legq',1,4,2],'coef':'5/13'},
        {'j':0,'m':0,'spec':['legqs',5,3,4,10],'coef':'-7/17'},
        {'j':3,'m':3,'spec':['legqs',2,4,4,50],'coef':'11/19'},
        {'j':2,'m':1,'spec':['legqs',4,2,0,100],'coef':'-13/23'},
        {'j':1,'m':2,'spec':['legqs',3,0,1,50],'coef':'17/29'}]},
        {'cl_exact':'9/5','generators':[
        {'j':0,'m':0,'spec':['legqs',0,0,0,50],'coef':'1'},
        {'j':0,'m':2,'spec':['legqs',0,3,2,100],'coef':'-2/3'},
        {'j':2,'m':1,'spec':['legqs',0,2,1,50],'coef':'4/5'}]}]
    rows=[]
    for index,data in enumerate(fixtures):
        tick=time.monotonic();model=ScaledRadial(data);mixed=[]
        for x in range(1,5):
            for y in range(1,5-x):
                previous=model.deriv(x-1,y)
                alternate=model.differentiate(previous,x+y-1,'s' if y%2 else 'c','x')
                mixed.append(alternate==model.deriv(x,y))
        assert all(mixed)
        for x in range(5):
            for y in range(5-x):model.fields[f'chi_{x}_{y}']=(model.deriv(x,y),x+y,'s' if y%2 else 'c')
        points=[]
        for xs,ys in [('1/2','1/3'),('3','4'),('60','80')]:
            jet=J.GeneratorJet(data,xs,ys,4);expected=jet.fields();actual=model.evaluate(xs,ys)
            equalities={key:actual[key].overlaps(expected[key]) for key in ['rho','u1','u2','rho_x','rho_y','residual']}
            for x in range(5):
                for y in range(5-x):equalities[f'chi_{x}_{y}']=actual[f'chi_{x}_{y}'].overlaps(jet.chi(x,y))
            assert len(equalities)==21 and all(equalities.values())
            points.append({'x':xs,'y':ys,'comparisons':equalities})
        oldmodel=O.ScaledRadial({**data,'generators':[g for g in data['generators'] if g['spec'][0]!='legqs' or g['spec'][-1]!=50]})
        oldprobe=OW.construct(oldmodel,T**3,7);newprobe=W.construct(ScaledRadial(oldmodel.state),7,3)
        probechecks=[equal({key:A*TR**3 for key,A in field.items()},oldfield,convert) for field,oldfield in zip(newprobe,oldprobe,strict=True)]
        assert all(probechecks)
        rows.append({'exact_fixture':data,'mixed_derivatives':mixed,'points':points,'small_factored_probe_exact_checks':probechecks,'elapsed_seconds':time.monotonic()-tick})
        print('MANUFACTURED',index,'passed',time.monotonic()-tick,flush=True)
    src007=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
    original=R.Radial(src007);model=ScaledRadial(src007);comparisons={}
    for name in ['rho','u1','u2','rx','ry']:
        comparisons[name]=equal(getattr(model,name),getattr(original,name),Rat)
    for key,field in original.derivatives.items():comparisons[str(key)]=equal(model.deriv(*key),field,Rat)
    assert all(comparisons.values());print('007 EXACT FIELDS',len(comparisons),flush=True)
    src010=ROOT/'research/candidate_audits/data/C1-N1-010-d2w-j7-x3bal-legqs/d2w_j7_n4_X3bal_legqs_mid180_exact.json'
    original=O.ScaledRadial(src010);model=ScaledRadial(src010);comparisons010={}
    for name in ['rho','u1','u2','rx','ry']:
        comparisons010[name]=equal(getattr(model,name),getattr(original,name),convert)
    for key,field in original.derivatives.items():comparisons010[str(key)]=equal(model.deriv(*key),field,convert)
    assert all(comparisons010.values());print('010 EXACT FIELDS',len(comparisons010),flush=True)
    fields=W.construct(model,7,3);oldfields=OW.construct(original,T**3,7)
    small=[equal({k:A*TR**3 for k,A in field.items()},oldfield,convert) for field,oldfield in zip(fields,oldfields,strict=True)];assert all(small)
    points010=W.point_checks(model,7,3,fields)
    paths=[BASE/'verification/scalar2499.json',BASE/'code/scalar2499.py',Path(__file__),BASE/'PROOF.md',BASE/'code/weak.py',BASE/'code/fields50.py',
        ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/factored_pole_moments/verification/result.json',
        ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/multiscale_generators/code/cartesian.py',ROOT/'research/radial_fourier/code/radial.py',
        ROOT/'research/scaled_weak_backend/code/fields.py',ROOT/'research/scaled_weak_backend/code/weak_v3.py',
        ROOT/'research/scaled_weak_backend/verification/fields.json',src007,src010]
    oldresult=ROOT/'research/scaled_weak_backend/verification/C1-N1-010-d2w-j7-x3bal-legqs_n7.json'
    oldrecord=json.loads(oldresult.read_text());paths.append(oldresult)
    for rel,digest in oldrecord['inputs'].items():
        p=ROOT/rel;assert sha(p)==digest;paths.append(p)
    out={'utc':now(),'precision_bits':ctx.prec,'rational_checks':checks,'manufactured':rows,'candidate007_exact_fields':comparisons,'candidate010_exact_fields':comparisons010,'candidate010_small_probe_exact':small,'candidate010_probe_points':points010,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent review; field fixtures passed'}
    write('fields.json',out)
    n,K=21,522;src013=ROOT/'research/candidate_audits/data/C1-N1-013-pairU-from007/canonical.json';model=ScaledRadial(src013)
    acceptedpath=ROOT/'research/factored_monomial_audit/verification/result.json';accepted=json.loads(acceptedpath.read_text())
    assert accepted['canonical_sha256']==sha(src013) and accepted['n']==n and accepted['K']==K and all(accepted['peer_comparisons'].values())
    bound=Q(accepted['H_upper_exact']);sup=gradient(K,n,bound)
    fields=W.construct(model,n,K);points=W.point_checks(model,n,K,fields)
    Iparts,pc,pp,ph=W.pairing_parts(model,fields[0],K)
    projection,counts=W.project(model,n);I,ic=W.integrate_groups(projection,model.delta,Q(-1),K+1,'Idirect')
    assert I.overlaps(Iparts) and min(I.rel_accuracy_bits(),Iparts.rel_accuracy_bits())>150
    M2,mc,mp,mh=W.energy(fields[:1],model,K,'M2');C2,cc,cp,ch=W.energy(fields[1:],model,K,'C2')
    M,C=M2.sqrt(),C2.sqrt();D=M+C;radius=2*abs(I)/(D+(D*D+4*ar(bound)*abs(I)).sqrt())
    vals={'pairing':I,'pairing_by_parts':Iparts,'normM2':M2,'normC2':C2,'M':M,'C':C,'D':D,'radius':radius}
    overlaps={key:value.overlaps(arb(accepted[key])) for key,value in vals.items()};assert all(overlaps.values()),overlaps
    floor=Q(accepted['strict_lower_exact']);assert ar(floor)<radius
    paths.extend([src013,acceptedpath,BASE/'verification/fields.json'])
    out={'utc':now(),'candidate':'C1-N1-013-pairU-from007','n':n,'K':K,'precision_bits':ctx.prec,
        'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'canonical_sha256':sha(src013),'raw_sha256':accepted['raw_sha256'],
        'point_checks':points,'field_sha256':[field_hash(f) for f in fields],'projection_sha256':field_hash(projection),
        'M_group_sha256':mh,'C_group_sha256':ch,'parts_group_sha256':ph,'M_pairs':mp,'C_pairs':cp,'parts_pairs':pp,'projection_pairs':counts,
        'M_moments':mc,'C_moments':cc,'parts_moments':pc,'direct_moments':ic,**{k:v.str(100) for k,v in vals.items()},
        'gradient_certificate':sup,'H_upper_exact':str(bound),'strict_lower_exact':str(floor),'strict_floor_verified':True,
        'accepted013_overlaps':overlaps,'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent review; complete accepted013 reproduced'}
    write('candidate013.json',out);print('DONE',out['utc'],'radius',radius.str(30),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
