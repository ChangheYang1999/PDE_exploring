"""Projected Laplacian norms with exact Cartesian/polar identities and cells."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,importlib.util,json,sys,time
from flint import arb,arb_poly,fmpq as Q,fmpq_poly as Poly,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/successor_dyadic_probes'
HELP=ROOT/'research/successor_weak_probes/code/check.py'
spec=importlib.util.spec_from_file_location('successor_fields',HELP);W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from norms import derivative,ar,T,U,ZERO
Radial=W.Radial
WEIGHTS=[Q(k,4) for k in range(8)]
REF=ROOT/'research/projected_laplacian_audit/verification/candidate007_modes13.json'
REFCELLS=ROOT/'research/origin_dyadic_ceiling/verification/candidate007_modes13.json'
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def new(path,record):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
def origin(data):
    c=Q(data['cl']);a0=strain=Q(0)
    for (j,m,k),coef in zip(data['order'],data['coefficients'],strict=True):
        if k>2 or m>2:continue
        p=(3+1/c-j*(1-1/c))/2;v=Q(1)
        for z in range(2-k):v*=(p-k-z)/(z+1)
        b,d=[(2,1),(0,-1),(-6,1)][m]
        a0-=(4*b+24*d)*v*Q(coef);strain+=4*b*v*Q(coef)
    assert a0==Q(data['a0']) and strain==1-c and 1<c<2 and a0>=5*c-4
    return a0,strain

def maximum(c):
    d=c-1;s=Poly([0,1]);f=(d-s)**2*s*(1+s)
    assert f.derivative()==(d-s)*(d+(2*d-3)*s-4*s*s)
    star=(ar(2*d-3)+ar((2*d-3)**2+16*d).sqrt())/8
    assert 0<star<ar(d)
    return star,(ar(d)-star)*(4*arb.pi()*star*(1+star)).sqrt()

def cells(records,modes,c,hmax):
    A=1+1/c;assert Q(3,2)<A<Q(7,4)
    vals={(n,Q(z['a'])):arb(z['energy']) for n in modes for z in records[n]['weights']}
    out=[];points=[Q(k,4) for k in range(7)]+[A]
    for l,h in zip(points[:-1],points[1:]):
        e=Q(7,4) if h==A else h
        norm=sum((vals[n,e] for n in modes),arb(0)).sqrt()
        lower=arb(5)**ar((l-2)/2)*norm
        upper=hmax*ar((1+c-c*l)/(1+l));gap=lower-upper;ratio=lower/upper
        passes=bool(gap>0)
        floor=Q(int(float(ratio)*10**8)-1,10**8)
        assert ratio>ar(floor)
        out.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(e),
                    'selected_modes':modes,'projected_norm':norm.str(100),
                    'lower':lower.str(100),'upper':upper.str(100),'gap':gap.str(100),
                    'ratio':ratio.str(100),'strict_ratio_floor':str(floor),'excluded':passes})
    return out

def run(name,modes):
    start=time.monotonic();ctx.prec=2048
    src=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
    auditpath=ROOT/f'research/candidate_audits/verification/{name}.json'
    audit=json.loads(auditpath.read_text());data=json.loads(src.read_text())
    assert H(src)==audit['canonical_sha256'] and audit['all_forbidden_zero'] and audit['snapshot_hashes_confirmed']
    model=Radial(src);assert model.state['source_sha256']==audit['generator_sha256']
    assert model.c==Q(4076476460239181,2251799813685248)
    a0,strain=origin(data);star,hmax=maximum(model.c)
    old=json.loads(REF.read_text());refrows={(z['mode'],Q(z['a'])):z for z in old['rows']}
    previous_cells=json.loads(REFCELLS.read_text())
    paths=[src,auditpath,Path(__file__),BASE/'PROOF.md',HELP,
           ROOT/'research/angular_probe_audit/code/check.py',ROOT/'research/optimized_probe_audit/code/check.py',
           ROOT/'research/radial_fourier/code/radial.py',ROOT/'research/whole_plane_norms/code/norms.py',
           ROOT/'research/origin_dyadic_ceiling/source/T4_origin_dyadic_inverse_PROOF.md',
           ROOT/'research/origin_dyadic_ceiling/source/T4_origin_spectral_line_PROOF.md',
           ROOT/'research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v13.md',
           ROOT/'research/origin_dyadic_ceiling/reviews/T1_REVIEWS_v14.md',REF,REFCELLS]
    inputs={str(p.relative_to(ROOT)):H(p) for p in paths}
    dest=BASE/'verification'/name
    manifest={'candidate':name,'bits':ctx.prec,'modes':modes,'weights':list(map(str,WEIGHTS)),
              'c_exact':str(model.c),'inputs':inputs,'a0_exact':str(a0),'strain_exact':str(strain)}
    if (dest/'manifest.json').exists():assert json.loads((dest/'manifest.json').read_text())==manifest
    else:new(dest/'manifest.json',manifest)
    mh=H(dest/'manifest.json');records={}
    print('loaded',name,'seconds',time.monotonic()-start,flush=True)
    for n in modes:
        outpath=dest/f'mode_{n:03d}.json'
        if outpath.exists():
            row=json.loads(outpath.read_text());assert row['manifest_sha256']==mh;records[n]=row;continue
        tick=time.monotonic();projected,counts=W.project(model,n)
        F={(ell,'s',n):p for ell,p in projected.items()}
        dx=derivative(F,0,'x',model.delta);dy=derivative(F,0,'y',model.delta)
        assert derivative(dx,1,'y',model.delta)==derivative(dy,1,'x',model.delta)
        xx=derivative(dx,1,'x',model.delta);yy=derivative(dy,1,'y',model.delta)
        cart={k:xx.get(k,ZERO)+yy.get(k,ZERO) for k in set(xx)|set(yy)}
        cart={k:p for k,p in cart.items() if p}
        polar={};terms=[];endpoints=[]
        for ell,p in sorted(projected.items()):
            d=ell*model.delta/2
            td=lambda v:(1-2*d*T)*v+2*T*U*v.derivative()
            numerator=td(td(p))-n*n*p
            if not numerator:continue
            lap,rem=divmod(numerator,T);assert not rem
            polar[ell,'s',n]=lap
            end=lap(U);q=next(i for i,v in enumerate(end) if v)
            coeff=Poly(list(end)[q:]);assert ell*model.delta+2*q-2>0
            terms.append((ell,q,arb_poly([ar(v) for v in coeff])))
            endpoints.append({'ell':ell,'order':q,'degree':coeff.degree()})
        assert cart==polar and terms
        groups={};one_minus=arb_poly([1,-1])
        for i,(ell,q,p) in enumerate(terms):
            for j in range(i,len(terms)):
                ell2,q2,v=terms[j];b=(ell+ell2)*model.delta/2+q+q2-3
                assert b>-1
                prod=(1 if i==j else 2)*one_minus*p*v
                groups[b]=groups.get(b,arb_poly([]))+prod
        moments=[(b+j+1,v) for b,p in groups.items() for j,v in enumerate(p)]
        assert all(b>0 for b,v in moments)
        weights=[]
        for a in WEIGHTS:
            energy=arb.pi()/2*sum((v/ar(a+b) for b,v in moments),arb(0))
            assert energy>0 and energy.rel_accuracy_bits()>150
            norm=energy.sqrt();checks={}
            if name.startswith('C1-N1-007-') and n in [1,3]:
                assert old['source_sha256']==H(src)
                checks['independent007_Cartesian_norm_overlap']=norm.overlaps(arb(refrows[n,a]['norm']))
                assert all(checks.values())
            weights.append({'a':str(a),'energy':energy.str(100),'norm':norm.str(100),
                            'relative_accuracy_bits':energy.rel_accuracy_bits(),'calibration':checks})
        record={'utc':datetime.now(timezone.utc).isoformat(),'mode':n,'manifest_sha256':mh,
                'projection_pairs':counts,'projection_sha256':W.poly_hash(projected),
                'exact_Cartesian_polar_trace_equal':True,'exact_mixed_derivatives_equal':True,
                'Laplacian_sha256':W.poly_hash(polar),'endpoints':endpoints,
                'radial_groups':len(groups),'monomial_moments':len(moments),'weights':weights,
                'elapsed_seconds':time.monotonic()-tick}
        new(outpath,record);records[n]=record
        print('mode',n,'N0',weights[0]['norm'][:38],'seconds',record['elapsed_seconds'],flush=True)
    cover=cells(records,modes,model.c,hmax);calibration=[]
    if name.startswith('C1-N1-007-'):
        cc=cells(records,[1,3],model.c,hmax)
        for row,peer in zip(cc,previous_cells['cells'],strict=True):
            check={k:arb(row[k]).overlaps(arb(peer[k])) for k in ['lower','upper','gap','ratio']}
            assert all(check.values()) and row['excluded']
            calibration.append(check)
    result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'bits':ctx.prec,
            'manifest_sha256':mh,'mode_result_sha256':{str(n):H(dest/f'mode_{n:03d}.json') for n in modes},
            'selected_modes':modes,'a0_exact':str(a0),'origin_threshold_margin':str(a0-(5*model.c-4)),
            's_maximizer':star.str(100),'H_max':hmax.str(100),'seven_cells':cover,
            'all_seven_excluded':all(z['excluded'] for z in cover),'candidate007_cell_calibration':calibration,
            'complete_upper_norm':False,'elapsed_seconds':time.monotonic()-start,
            'verdict':'OPEN independent numerical peer; conditional scheme exclusion only when every cell passes'}
    new(dest/'result.json',result)
    print('DONE',name,'all7',result['all_seven_excluded'],'seconds',result['elapsed_seconds'],flush=True)
    for z in cover:print(z['left'],z['right'],z['ratio'][:50],z['excluded'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate',nargs='+');p.add_argument('--modes',type=int,nargs='+',default=[1,3,7]);a=p.parse_args()
    assert a.modes==sorted(set(a.modes)) and all(n>0 and n%2 for n in a.modes) and {1,3}<=set(a.modes)
    for name in a.candidate:run(name,a.modes)
