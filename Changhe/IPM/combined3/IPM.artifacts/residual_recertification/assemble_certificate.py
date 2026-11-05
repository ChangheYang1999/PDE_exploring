"""Independent regional replay, exact coverage check and scalar certification.

Reads fresh source-produced enclosures, not any historical residual summary.
Final threshold comparisons use Fraction exactly. Arb is used only to replay
validated integration, Laurent radial powers and positive energy formulas.
"""
import argparse,gzip,json,math,sys,hashlib,platform
import flint
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,ctx
sys.dont_write_bytecode=True
EXPECTED={'base007':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21','phi013':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'}
SOURCE_PATHS={'base007':'Changhe/IPM/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json','phi013':'Changhe/IPM/combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json'}
C=Q(4076476460239181,2251799813685248)

def A(v):return arb(str(v))
def U(v):return Q(str(v.upper().fmpq()))
def L(v):return Q(str(v.lower().fmpq()))
def enclosure(pair):
    a,b=map(Q,pair);assert a<=b
    return A(a).union(A(b))
def digest(path):
    h=hashlib.sha256()
    with path.open('rb')as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()
def load(path):
    if str(path).endswith('.gz'):
        with gzip.open(path,'rt')as f:return json.load(f)
    return json.loads(path.read_text())
def scalar(v):return {'upper_exact':str(v),'upper_decimal':A(v).str(22)}

def replay_panel(data):
    left,right,c,h=map(Q,[data['left'],data['right'],data['center'],data['halfwidth']])
    assert 0<left<right and c==(left+right)/2 and h==(right-left)/2
    assert data['status']=='CERTIFIED_FINITE_RESIDUAL_PANEL'
    H,R=map(Q,[data['residual_majorant_upper'],data['cauchy_radius']]);K=data['degree'];assert K>=6 and R>2*h
    l2=data['L2'];coeffs=l2['integrand_coefficients']
    polynomial=2*A(h)*arb.pi()*sum((enclosure(coeffs[k])/(k+1)for k in range(0,len(coeffs),2)),arb(0))
    z=A(h/R);tail=A(H)*z**(K+1)/(1-z)
    tail=max(U(tail),Q(l2['residual_remainder_l1_upper']))
    pmax=Q(l2['polynomial_l1_upper']);assert pmax>=0
    error=2*A(h)*arb.pi()*A(c+h)*(2*A(pmax)*A(tail)+A(tail)*A(tail))
    error=max(U(error),Q(l2['analytic_error_upper']))
    upper=max(U(polynomial)+error,Q(l2['energy_upper']))
    lower=max(Q(0),min(L(polynomial)-error,Q(l2['energy_lower'])))
    assert 0<=lower<=upper
    # Replay modal derivative-enclosure integration independently.
    r=enclosure([str(left),str(right)])
    e2=e3=arb(0);seen=[]
    for row in data['high_order']['modal_rows']:
        n=row['n'];assert n>0 and n%2==1 and n not in seen;seen.append(n)
        f,fp,fpp,fppp=map(enclosure,row['derivative_enclosures'])
        b=f-fpp-fp/r+n*n*f/(r*r)
        bp=fp-fppp-fpp/r+(1+n*n)*fp/(r*r)-2*n*n*f/(r*r*r)
        s2=b*b
        s3=b*b+bp*bp+n*n*b*b/(r*r)
        for sign in[-1,1]:
            a=r*b-2*fp+sign*2*n*f/r
            ap=b+r*bp-2*fpp+sign*2*n*(fp/r-f/(r*r))
            s2+=2*a*a
            s3+=2*(a*a+ap*ap+(n+sign)**2*a*a/(r*r))
        e2+=2*A(h)*arb.pi()*r*s2
        e3+=2*A(h)*arb.pi()*r*s3
    e2=max(U(e2),Q(data['high_order']['E2_upper']))
    e3=max(U(e3),Q(data['high_order']['E3_upper']))
    assert e3>=0 and e2>=0
    return lower,upper,e2,e3

def endpoint_origin(data):
    radius=Q(data['radius_exact']);assert radius>0 and data['fixed_c_exact']==str(C)
    raw=data.get('residual_uniform_enclosures',data.get('residual_derivative_enclosures'))
    b=Q(raw['0,0']['uniform_abs_upper_exact'])
    f2=max(U(arb.pi()*A(radius)*A(radius)*A(b)*A(b)),Q(data['F_L2_energy_upper_exact']))
    ts=([Q(row['energy_upper_exact'])for row in data['G_ordered_tensor_energies']]if 'G_ordered_tensor_energies'in data else list(map(Q,data['G_ordered_tensor_energy_uppers_exact'])))
    assert len(ts)==4 and all(t>=0 for t in ts)
    e2=(A(ts[0]).sqrt()+(2*A(ts[2])).sqrt())**2
    e3=e2+(A(ts[1]).sqrt()+(2*A(ts[3])).sqrt())**2
    return radius,f2,U(e2),U(e3)

def endpoint_far(data,radius_override=None,remainder_factor=Q(1)):
    radius=Q(data['radius_exact'])if radius_override is None else Q(radius_override);assert radius>0 and data['fixed_c']==str(C)
    norms={}
    for row in data['derivatives']:
        key=row['i'],row['j'];assert key not in norms
        values=[]
        for w in[0,1]:
            bound=arb(0)
            for is_tail,items in[(False,row['finite_absolute_powers']),(True,row['remainder_absolute_powers'])]:
                for item in items:
                    p=Q(item['power'])+w;assert p< -1
                    coefficient=U(A(item['coefficient_bound']))*(remainder_factor if is_tail else 1);assert coefficient>=0
                    bound+=A(coefficient)*A(radius)**A(p+1)/A(-2*p-2).sqrt()
            bound*=(2*arb.pi()).sqrt()
            # Existing parsed norm is another containing upper; the maximum
            # makes this independent replay conservative under serialization.
            v=max(U(bound),U(A(row['norm_upper'][str(w)])))
            values.append(v)
        norms[key]=values
    assert set(norms)=={(i,k-i)for k in range(4)for i in range(k+1)}
    Ns=[];Bs=[]
    for k in range(4):
        Ns.append(sum((math.comb(k,i)*A(norms[i,k-i][0])**2 for i in range(k+1)),arb(0)).sqrt())
        Bs.append(sum((math.comb(k,i)*A(norms[i,k-i][1])**2 for i in range(k+1)),arb(0)).sqrt())
    ls=[Ns[k]+2*Bs[k]+(2*arb(k*(k+1)).sqrt()*Ns[k-1]if k else 0)for k in range(4)]
    e2=(ls[0]+arb(2).sqrt()*ls[2])**2
    e3=e2+(ls[1]+arb(2).sqrt()*ls[3])**2
    return radius,U(Ns[0]**2),U(e2),U(e3)

def run(args):
    ctx.prec=args.precision
    root=Path(args.repo_root).resolve();work=Path(args.workdir).resolve();finite=work/args.finite_dir
    dependencies={}
    for key,relative in SOURCE_PATHS.items():
        path=root/relative;actual=digest(path);assert actual==EXPECTED[key];dependencies[relative]=actual
    op,fp=work/args.origin_file,work/args.far_file
    origin,far=load(op),load(fp)
    for data in[origin,far]:assert data.get('source_hashes',data.get('source_sha256'))==EXPECTED
    rmin,oL2,oE2,oE3=endpoint_origin(origin)
    if far['status']=='RETARGETED_FAR_CERTIFICATE':
        primary_path=work/far['primary_file'];assert digest(primary_path)==far['primary_sha256']
        primary=load(primary_path);oldR,newR=Q(primary['radius_exact']),Q(far['radius_exact'])
        rad=Q(primary['analytic_u_radius_exact']);assert 0<newR<=oldR
        zold,znew=1/(oldR*oldR*rad),1/(newR*newR*rad);assert 8*znew<1
        factor=((1-8*zold)/(1-8*znew))**2
        assert factor==Q(far['remainder_amplification_exact']) and factor>=1
        rmax,fL2,fE2,fE3=endpoint_far(primary,newR,factor)
    else:
        rmax,fL2,fE2,fE3=endpoint_far(far)
        if far.get('expansion_degree',0)>2:
            prefix_path=work/args.far_prefix_file;prefix=load(prefix_path)
            assert prefix['source_hashes']==EXPECTED and Q(prefix['fixed_c'])==C
            assert prefix['expansion_degree']>=2
            assert far['residual_finite_terms']==prefix['residual_finite_terms']
    config=load(finite/'configuration.json');assert config['source_hashes']==EXPECTED
    # The enlarged origin encloses fresh coefficient data generated by the
    # small-disk producer; bind those bytes as an explicit dependency.
    if 'field_data_sha256'in origin:
        field_path=work/'origin_certificate.json'
        assert digest(field_path)==origin['field_data_sha256']
        field_data=load(field_path)
        assert field_data['source_sha256']==EXPECTED and Q(field_data['fixed_c_exact'])==C
    assert Q(config['rmin'])==rmin and Q(config['rmax'])==rmax
    count=config['panels'];previous=rmin;totals=[Q(0)]*4;rows=[]
    missing=[i for i in range(count)if not(finite/('panel_%05d.json.gz'%i)).exists()]
    if missing:
        print(json.dumps({'status':'INCOMPLETE_NO_WHOLE_PLANE_CERTIFICATE','missing_panels':missing,'completed_panels':count-len(missing),'expected_panels':count},indent=2));return
    for i in range(count):
        path=finite/('panel_%05d.json.gz'%i);data=load(path)
        assert data['index']==i and Q(data['left'])==previous
        previous=Q(data['right']);assert previous<=rmax
        values=replay_panel(data)
        totals=[a+b for a,b in zip(totals,values)]
        rows.append({'index':i,'sha256':digest(path),'energy_lower':str(values[0]),'energy_upper':str(values[1]),'E2_upper':str(values[2]),'E3_upper':str(values[3])})
        if(i+1)%50==0:print('REPLAY',i+1,'/',count,flush=True)
    assert previous==rmax
    l2=totals[1]+oL2+fL2;e2=totals[2]+oE2+fE2;e3=totals[3]+oE3+fE3
    thresholdA=Q('7.96121055107e-7');strongA=Q('7.961207e-7');thresholdB=Q('.094')
    passA=l2<thresholdA**2;passB=e2**9*e3<thresholdB**20
    output={'status':'PASS'if passA and passB else 'FAIL','source_hashes':EXPECTED,'fixed_c_exact':str(C),'coverage':{'origin_radius_exact':str(rmin),'far_radius_exact':str(rmax),'finite_panels':count,'exact_coverage_up_to_null_boundary_circles':True},'Task_A':{'verdict':'PASS'if passA else'FAIL','threshold_exact':str(thresholdA),'energy_upper_exact':str(l2),'norm_upper':A(l2).sqrt().str(50),'stronger_threshold_pass':l2<strongA**2},'Task_B':{'verdict':'PASS'if passB else'FAIL','threshold_exact':str(thresholdB),'E2_upper_exact':str(e2),'E3_upper_exact':str(e3),'Q_upper':(A(e2)**(arb(9)/20)*A(e3)**(arb(1)/20)).str(50),'exact_comparison':'E2^9 * E3 < (47/500)^20','exact_comparison_pass':passB},'region_uppers':{'origin':{'L2_energy':str(oL2),'E2':str(oE2),'E3':str(oE3)},'finite':{'L2_energy':str(totals[1]),'E2':str(totals[2]),'E3':str(totals[3])},'far':{'L2_energy':str(fL2),'E2':str(fE2),'E3':str(fE3)}},'raw_inputs_sha256':{str(p.relative_to(work)):digest(p)for p in[op,fp,finite/'configuration.json',work/'origin_certificate.json']+([work/args.far_prefix_file]if far.get('expansion_degree',0)>2 else[])},'panel_replay':rows,'source_files':dependencies,'program_files_sha256':{p.name:digest(p)for p in sorted(work.glob('*.py'))},'algorithm_sources_sha256':{relative:digest(root/relative)for relative in['Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/fields013.py','Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/asymptotics013.py']},'runtime':{'python':platform.python_version(),'python_flint':flint.__version__},'precision_bits':args.precision,'historical_residual_evidence_used':False,'assembler_sha256':digest(Path(__file__))}
    (work/args.output).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items()if k not in['panel_replay','region_uppers','source_files','raw_inputs_sha256']},indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo-root',required=True);p.add_argument('--workdir',default=str(Path(__file__).resolve().parent));p.add_argument('--finite-dir',default='finite_data_core');p.add_argument('--origin-file',default='origin_large_certificate.json');p.add_argument('--far-file',default='far_degree6.json');p.add_argument('--far-prefix-file',default='far_certificate.json');p.add_argument('--precision',type=int,default=1024);p.add_argument('--output',default='validated_summary.json');run(p.parse_args())
