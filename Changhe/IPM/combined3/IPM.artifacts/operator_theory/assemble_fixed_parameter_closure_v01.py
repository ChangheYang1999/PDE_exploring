#!/usr/bin/env python3
"""Strict final numerical consumer for the local-Q fixed-parameter theorem.

Missing/invalid inputs never yield PASS. This script does not run or alter
any producer. It verifies binding and cover completeness, recomputes the
actual scalar join, and records both exterior and tangent Garding prices.
"""
import argparse,importlib.util,json,math,sys
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx,fmpq as Q
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ART=HERE.parent;IPM=ART.parents[1]
SOURCES={'base007':'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21',
         'phi013':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'}
CEX=F(4076476460239181,2251799813685248)
RAT_R=F(381377,10**12);RAT_B2=F(2087491,10**6)
RAT_F2=F(7961207,10**13);RAT_N=F(759,100000);RAT_BETA=F(7,10)
PATHS={'matrix':ART/'actual_matrix_v01/result.json',
       'local':ART/'local_energy_coefficients_v01/result.json',
       'source_constants':ART/'finite_rank/Q_source_certificate_v01/result.json',
       'source_envelopes':ART/'source_envelopes_v01/result.json',
       'far_source':ART/'Q_far_source_highpass_result.json',
       'forcing':ART/'source_Q_from_integer_tensors.json',
       'L2':ART/'coercivity_residual/L2_signed_far_v05/result.json',
       'L2_replay':ART/'ROOT_DIRECT_L2_REPLAY.json',
       'structure':HERE/'structure013_result.json',
       'nonlinear_scalar':HERE/'nonlinear_core_scalar_result.json',
       'nonlinear_replay':ART/'ROOT_NONLINEAR_CORE_REPLAY.json',
       'envelope_replay':ART/'ROOT_SOURCE_ENVELOPE_REPLAY.json',
       'local_replay':ART/'ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json'}
STATUS={'matrix':'CERTIFIED_ACTUAL_MATRIX','local':'CERTIFIED_LOCAL_Q_COEFFICIENTS',
        'source_constants':'CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS',
        'source_envelopes':'CERTIFIED_RADIAL_NEAR_SOURCE_ENVELOPES',
        'far_source':'CERTIFIED_ACTUAL_FAR_Q_SOURCE_LOW_HIGH_BOUNDS',
        'forcing':'CERTIFIED_Q_SOURCE_FROM_INTEGER_TENSORS','L2':'CERTIFIED_DIRECT_L2',
        'L2_replay':'ROOT_DIRECT_L2_REPLAY_AND_RADIUS_PASS','structure':'EXACT_STRUCTURE_CHECK_PASS',
        'nonlinear_scalar':'NONLINEAR_CORE_SCALAR_CONTINUUM_PASS',
        'nonlinear_replay':'ROOT_NONLINEAR_CORE_REPLAY_PASS',
        'envelope_replay':'ROOT_SOURCE_ENVELOPE_REPLAY_PASS',
        'local_replay':'ROOT_LOCAL_COEFFICIENT_ASSEMBLY_PASS'}
INHERITED_F2={
 'numerical_audit/research/source013_norms/verification/unweighted_publication_v01/result.json':
 '92cb0e5f48f470a76c723bd42355763211813031895f415c245fc8b5a9707c77',
 'theory_audit/research/source013_norms_actual_audit/verification/check_v01.json':
 '5374d423c0dbedc0fc8c69c74e0f4b6e423d3ee64eab340cf11afa1d654a08a2'}

def read(p):return json.loads(Path(p).read_text())
def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
    if isinstance(x,arb):return x
    x=F(x);return arb(x.numerator)/arb(x.denominator)
def upper(x):
    x=arb(x);assert x.is_finite();return x.abs_upper()
def maxupper(values):return max(upper(x) for x in values)
def dump(v):return aa(v).str(80)
def hashes(mapping,base=ART):
    assert mapping,('missing binding dictionary',str(base))
    for name,h in mapping.items():
        p=base/name;assert p.exists() and digest(p)==h,('binding',str(p),h)
def source_identity(d):
    assert d==SOURCES,('source identity',d)
def complete_leaves(leaves,max_depth):
    paths={p['path'] for p in leaves};assert len(paths)==len(leaves)
    def walk(prefix):
        if prefix in paths:
            assert not any(p.startswith(prefix) and p!=prefix for p in paths)
            return
        assert len(prefix)<max_depth
        walk(prefix+'0');walk(prefix+'1')
    walk('')
def cover(folder,cfg,adaptive=False,require_pass=False,limit=None,selected=None):
    r0,r1,ratio=F(cfg['rmin']),F(cfg['rmax']),F(cfg['ratio']);N=cfg['panels']
    assert r0>0 and r1>r0 and ratio>1 and N>0
    assert r0*ratio**(N-1)<r1<=r0*ratio**N,('exact cover geometry',str(folder))
    rows={};chunk_hashes={}
    files=sorted(ART/name for name in selected) if selected is not None else sorted(folder.glob('chunk_*.json'))
    for p in files:
        if selected is not None:assert digest(p)==selected[str(p.relative_to(ART))]
        d=read(p);assert d['configuration']==cfg
        chunk_hashes[str(p.relative_to(ART))]=digest(p)
        for row in d['rows']:
            i=row['index']
            if limit is not None and i>=limit:continue
            if i in rows:assert rows[i]==row
            rows[i]=row
            if adaptive:complete_leaves(row['leaves'],cfg['max_depth'])
            if require_pass:
                assert row['pass'],('failed panel',str(folder),i)
                for leaf in row['leaves']:
                    if 'pass' in leaf:
                        assert leaf['pass']
                        assert all(math.isfinite(leaf[k]) and leaf[k]>=0 for k in ['min_aa','min_dd','min_determinant'])
                    if 'strain_pass' in leaf:
                        assert leaf['strain_pass'] and math.isfinite(leaf['strain_square_upper']) and leaf['strain_square_upper']<=2.25
    expected=cfg['panels'] if limit is None else limit
    assert sorted(rows)==list(range(expected)),('incomplete cover',str(folder),len(rows),expected)
    return rows,chunk_hashes
def geometry(cfg,index,path):
    lo=F(cfg['rmin'])*F(cfg['ratio'])**index
    hi=min(F(cfg['rmin'])*F(cfg['ratio'])**(index+1),F(cfg['rmax']))
    for bit in path:
        mid=(lo+hi)/2
        if bit=='0':hi=mid
        else:assert bit=='1';lo=mid
    assert lo>0 and hi>lo
    return lo,hi

def validate(inputs):
    b007=IPM/'combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json'
    phi=IPM/'combined2/IPM.artifacts/exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json'
    assert digest(b007)==SOURCES['base007'] and digest(phi)==SOURCES['phi013']
    all_chunks={};configs={};rows_by_key={}
    for key in ['matrix','local','source_constants','source_envelopes']:
        d=inputs[key];cfg=d['configuration'];configs[key]=cfg
        source_identity(cfg['source_hashes']);hashes(cfg.get('bindings',cfg.get('code_hashes',{})))
        prefix=(key=='matrix' and d['status']=='CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR')
        if prefix:
            assert read(ART/'actual_matrix_v01/configuration.json')==cfg;hashes(d['bindings'])
            limit=d['used_base_panels'];assert 0<limit<=cfg['panels'] and not d['missing_base_panels']
            rows,ch=cover(ART/'actual_matrix_v01',cfg,True,True,limit,d['used_chunk_sha256'])
            endpoint=min(F(cfg['rmin'])*F(cfg['ratio'])**limit,F(cfg['rmax']))
            assert F(d['core_endpoint_exact'])==endpoint>=F(d['exterior_start'])
            origin=read(PATHS['matrix'].parent/'origin.json')
            assert origin['meta']['bindings']==d['bindings'] and origin['meta']['radius']==cfg['rmin']
            assert origin['origin']==d['origin_detail'] and d['origin_detail']['exact_strain_and_constant_harmonic_checks'] is True
            audit=inputs['matrix_prefix_audit'];hashes(audit['bindings'])
            assert audit['used_base_panels']==limit and audit['values_identical'] is True
            required=[PATHS['matrix'],PATHS['matrix'].parent/'origin.json',HERE/'assemble_matrix_prefix_signed_far_v01.py',
                      ART/'actual_matrix_v01/configuration.json',HERE/'signed_matrix_far_price_v01.json']
            assert all(str(p.relative_to(ART)) in audit['bindings'] for p in required)
            price=read(HERE/'signed_matrix_far_price_v01.json');assert price['status']=='SIGNED_MATRIX_FAR_PRICE_COMPLETE';hashes(price['bindings'])
            far=[v for v in price['rows'] if v['radius']==d['exterior_start']];assert len(far)==1 and far[0]['passes_beta_7_over_10']
            assert arb(d['exterior_lower'])>=aa(RAT_BETA) and d['exterior_detail']==far[0]
            replay=inputs['matrix_far_replay'];source_identity(replay['source_hashes'])
            assert replay['price_result_sha256']==digest(HERE/'signed_matrix_far_price_v01.json')
            assert replay['program_sha256']==digest(ART/'verify_signed_matrix_far_independent.py')
            assert replay['all_required_field_and_remainder_powers_strictly_negative'] and replay['published_containment_checks']
            assert F(replay['radius'])==F(d['exterior_start']) and arb(replay['recomputed_matrix_lower'])>=aa(RAT_BETA)
        else:
            assert read(PATHS[key].parent/'configuration.json')==cfg
            rows,ch=cover(PATHS[key].parent,cfg,key in ['matrix','local'],key in ['matrix','local'])
        rows_by_key[key]=rows;all_chunks.update(ch)
    mat=inputs['matrix'];assert F(mat['configuration']['beta'])==RAT_BETA
    assert not mat['failed_base_panels'] and arb(mat['origin_lower'])>=aa(RAT_BETA) and arb(mat['exterior_lower'])>=aa(RAT_BETA)
    local=inputs['local'];assert F(local['strain_op_upper'])==F(3,2) and not local['failed_strain_panels']
    assert arb(local['origin']['S'])<aa(F(3,2)) and arb(local['exterior']['S'])<aa(F(3,2))
    for row in rows_by_key['local'].values():assert all(p['strain_pass'] for p in row['leaves'])
    lrep=inputs['local_replay'];hashes(lrep['input_sha256'])
    assert digest(ART/'verify_local_coefficient_assembly.py')==lrep['program_sha256']
    assert lrep['panels']==configs['local']['panels'] and lrep['all_leaf_partitions_and_strain_flags_checked'] is True
    assert lrep['input_sha256']['local_energy_coefficients_v01/result.json']==digest(PATHS['local'])
    assert aa(F(3,2))<aa(CEX)
    # This configuration/producer is the reviewed original weight a=2.
    assert 'weight_a' not in mat['configuration'] or F(mat['configuration']['weight_a'])==2
    src=inputs['source_constants'];assert len(src['core_energies'])==6
    assert all(arb(v).is_finite() and arb(v)>0 for v in src['core_energies'])
    far=inputs['far_source'];source_identity(far['source_hashes']);hashes(far['bindings'])
    force=inputs['forcing'];source_identity(force['source_hashes']);assert F(force['fixed_c'])==CEX
    assert force['exact_tensor_upper_checks'] is True and F(force['f2_upper'])==RAT_F2
    assert digest(ART/'verify_source_Q_from_integer_tensors.py')==force['code_sha256']
    tensor=IPM/'combined2/IPM.artifacts/theory_audit/research/source013_moment_refinement/verification/result_v01.json'
    assert digest(tensor)==force['inherited_tensor_sha256']
    inherited=read(tensor)
    assert inherited['source']['id']=='C2-N1-013' and inherited['source']['raw_sha256']==SOURCES['phi013']
    assert Q(inherited['source']['fixed_c_exact'])==Q(CEX.numerator,CEX.denominator)
    orders=[]
    for row in inherited['tensor_energies']:
        j=row['order'];rounded=F(force['rounded_tensor_energies'][j])
        assert Q(rounded.numerator,rounded.denominator)>=Q(row['upper_exact']);orders.append(j)
    assert sorted(orders)==[0,1,2,3]
    assert F(force['rational_upper'])==RAT_N and arb(force['Q_F_upper'])<aa(RAT_N)
    # Bind the inherited actual L2 residual certificate and its independent audit.
    old_art=IPM/'combined2/IPM.artifacts';hashes(INHERITED_F2,old_art)
    publication,audit=[read(old_art/name) for name in INHERITED_F2]
    assert publication['status']=='CERTIFIED_NORMS' and publication['kind']=='unweighted'
    assert publication['source']['raw_sha256']==SOURCES['phi013']
    assert F(publication['source']['fixed_c_exact'])==CEX
    assert audit['status']=='PASS' and audit['unweighted_result_sha256']==digest(old_art/next(iter(INHERITED_F2)))
    vals=publication['output']['values'];assert F(vals['norm_interval_exact'][1])<RAT_F2
    assert F(vals['energy_interval_exact'][1])<RAT_F2*RAT_F2
    # Independently re-evaluate the source integer arithmetic, no old CE input.
    T0,T1,T2,T3=map(arb,force['rounded_tensor_energies']);f=aa(RAT_F2)
    d3=T3.sqrt()+3*T2.sqrt()+18*T1.sqrt()+36*T0.sqrt()
    d1=f**aa(F(2,3))*d3**aa(F(1,3));d2=f**aa(F(1,3))*d3**aa(F(2,3))
    A2=(T0+2*T1+T2).sqrt()+4*d1+12*f
    A3=(T0+3*T1+3*T2+T3).sqrt()+7*d2+130*d1+1391*f
    assert A2**aa(F(9,10))*A3**aa(F(1,10))<aa(RAT_N)
    structural=inputs['structure'];assert structural['input_sha256']==SOURCES
    assert F(structural['fixed_c_exact'])==CEX and structural['original_equals_elementary_exactly'] is True
    assert structural['base_normalization_c_plus_strain_equals_one'] is True
    assert F(structural['correction_strain'])==0 and F(structural['correction_A_plus_3B'])==0
    assert structural['rho_star_origin_slope_greater_than_one'] is True and arb(structural['rho_star_origin_slope_arb'])>1
    assert inputs['nonlinear_scalar']['target']=='53/50' and inputs['nonlinear_scalar']['intervals']==3210
    nr=inputs['nonlinear_replay'];hashes(nr['source_and_result_sha256'])
    assert nr['scalar_results_identical'] is True and nr['original_files_unchanged'] is True
    assert digest(ART/'verify_nonlinear_core_independent_replay.py')==nr['program_sha256']
    assert digest(ART/nr['replay_result_relative_path'])==nr['replay_result_sha256']==digest(PATHS['nonlinear_scalar'])
    er=inputs['envelope_replay'];hashes(er['input_sha256'])
    assert er['all_assembly_values_identical'] is True and er['original_files_unchanged'] is True
    assert digest(ART/'verify_source_envelopes_replay.py')==er['program_sha256']
    assert digest(ART/'root_source_envelopes_replay/result.json')==er['replay_result_sha256']
    assert er['input_sha256']['source_envelopes_v01/result.json']==digest(PATHS['source_envelopes'])
    # Direct L2 certificate, its exact used chunks, and coordinator replay.
    L2=inputs['L2'];lcfg=L2['source_configuration'];source_identity(lcfg['source_hashes'])
    hashes(lcfg['code_hashes'],ART/'coercivity_residual')
    assert digest(ART/'coercivity_residual/assemble_L2_signed_far_v05.py')==L2['assembler_sha256']
    assert digest(PATHS['L2'].parent/'far_expansion.cache.json')==L2['far_cache_sha256']
    cache_binding=read(PATHS['L2'].parent/'far_expansion.cache.json')['binding']
    source_identity(cache_binding['source_hashes']);hashes(cache_binding['background_code_hashes'],ART/'coercivity_residual')
    assert cache_binding['degree']==L2['far_expansion_degree']
    assert cache_binding['cache_builder_sha256'] in [digest(ART/'coercivity_residual'/name) for name in ['assemble_L2_signed_far_v04.py','assemble_L2_signed_far_v05.py']]
    out=ART/'coercivity_residual/L2_cert_v04';assert read(out/'configuration.json')==lcfg
    lr={}
    for name,h in L2['used_chunk_sha256'].items():
        p=out/name;assert digest(p)==h;d=read(p);assert d['configuration']==lcfg
        all_chunks[str(p.relative_to(ART))]=h
        for row in d['rows']:
            if row['index']<L2['core_panels_used']:
                assert row['index'] not in lr and row['theta_pass'];lr[row['index']]=row
    assert sorted(lr)==list(range(L2['core_panels_used']))
    assert L2['theta_origin_pass'] and L2['theta_core_pass'] and L2['theta_exterior_pass'] and not L2['theta_failed_panel_indices']
    assert arb(L2['beta_L2_lower'])>aa(RAT_B2)
    assert aa(CEX)+1-upper(L2['kappa_HS_upper'])-upper(L2['theta_upper'])>aa(RAT_B2)
    replay=inputs['L2_replay'];assert replay['actual_result_sha256']==digest(PATHS['L2']) and replay['assembly_values_identical'] is True
    assert F(replay['certified_radius_rational'])==RAT_R and RAT_R*RAT_B2>RAT_F2
    return rows_by_key,all_chunks

def constants(inputs,rows):
    loc=inputs['local'];cfg=loc['configuration']
    env={}
    for key in ['B0','H1','H2','Hu']:
        env[key]=maxupper([loc['origin'][key],loc['exterior'][key],loc['global_envelopes'][key]]+
                         [p[key] for row in rows['local'].values() for p in row['leaves']])
    B0,H1,H2,Hu=[env[k] for k in ['B0','H1','H2','Hu']]
    q=aa(F(21,10));c=aa(CEX);omega=arb(4);s=aa(F(3,2));Minf=1+(2-q)*c
    K1=2*omega*arb(2).sqrt()*(Minf+s)+omega*Hu+omega*arb(2).sqrt()*B0+omega*H1+q*omega*(1+1/arb(2).sqrt())*H1/2+(1+q)/2*H2
    K0=omega*((8-2*q)*c+4+B0+(2-q/2)*H1/2)
    K1=maxupper([K1,loc['E1_local_upper']]);K0=maxupper([K0,loc['E0_local_upper']])
    wu=[]
    for row in rows['local'].values():
        for leaf in row['leaves']:
            lo,hi=geometry(cfg,row['index'],leaf['path']);l=aa(lo)
            wu.append(upper(leaf['Hu'])*(1+4*l*l).sqrt()/l)
    for end,key in [('origin','rmin'),('exterior','rmax')]:
        r=aa(cfg[key]);wu.append(upper(loc[end]['Hu'])*(1+4*r*r).sqrt()/r)
    Wu2=maxupper(wu)
    src=inputs['source_constants']
    core=[sum((arb(rows['source_constants'][i]['energy_upper'][str(j)]) for i in sorted(rows['source_constants'])),arb(0)) for j in range(6)]
    totals=[core[j]+arb(src['tail_energies']['origin'][j])+arb(src['tail_energies']['exterior'][j]) for j in range(6)]
    assert all(v.is_finite() and v>0 for v in totals)
    Db={j+1:maxupper([totals[j].sqrt(),src['D_b_L2_upper'][str(j+1)]]) for j in range(4)}
    Dxb={2:maxupper([(totals[4]+4*totals[0]).sqrt(),src['D_xb_L2_upper']['2']]),
         4:maxupper([(totals[5]+16*totals[2]).sqrt(),src['D_xb_L2_upper']['4']])}
    HS=maxupper([src['H1_upper'],src['tail_energies']['origin_H1_bound'],src['tail_energies']['exterior_H1_bound']]+
                [row['H1_upper'] for row in rows['source_constants'].values()])
    def moment(D,m,sigma):
        ss=aa(sigma)
        cc=1/(2*(arb.pi()*ss/2).cos().sqrt()*(1-ss)**((1-ss)/4)*(1+ss)**((1+ss)/4))
        return cc*D[m]**((1-ss)/2)*D[m+2]**((1+ss)/2)
    def source_A(sigma):return moment(Db,2,sigma)+2*moment(Dxb,2,sigma)+4*moment(Db,1,sigma)
    A2=maxupper([source_A(F(0)),src['A_s_upper']['2']]);Aq=maxupper([source_A(F(1,10)),src['A_s_upper']['21/10']])
    M2u=(Db[1]*Db[3]).sqrt()/2;M3u=(Db[2]*Db[4]).sqrt()/2
    M3xu=((Dxb[2]+(arb(2).sqrt()+1)*Db[1])*(Dxb[4]+(arb(2).sqrt()+1)*Db[3])).sqrt()/2
    R3=aa(F(51,1000))*(M3u+2*M3xu+6*M2u)
    qdelta=q*aa(F(1,10));damping=c+1-aa(RAT_BETA)
    assert damping>0 and F(7,100)**2<F(51,1000)**2*F(19,10)
    near={r['cut_R']:r for r in inputs['source_envelopes']['rows']}
    far={r['R']:r for r in inputs['far_source']['rows']}
    sources={}
    for rb in [10000,30000,100000]:
        a0=upper(near[rb]['a0']);a1=upper(near[rb]['a1']);bf=upper(far[rb]['B'])
        bn=(a0*a0+4*a1*a1).sqrt();epfar=3*bf*bf/(4*damping)
        sources[rb]={'Bnear':bn,'Bfar':bf,'far_rate':epfar}
    return {'K1':K1,'K0':K0,'Wu2':Wu2,'source_H1':HS,'source_A2':A2,'source_Aq':Aq,
            'Db':Db,'Dxb':Dxb,'M2u':M2u,'M3u':M3u,'M3xu':M3xu,'R3_coefficient':R3,
            'local_Taylor_coefficient':qdelta*Wu2/2,'weighted_f_damping':damping,'source_splits':sources,
            'envelopes':env}

def scalar_scan(cons,args):
    spec=importlib.util.spec_from_file_location('ipm_nonlinear_Q_consumer',ART/'finite_rank/Qnorm_nonlinear_bound.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    q=F(21,10);delta=F(1,10);qr=aa(q);cq=qr*(qr-1)/2
    step=F(args.step);mlo=F(args.mmin);mhi=F(args.mmax);assert 0<mlo<=mhi<=F(1,2) and step>0
    grid=[mlo+i*step for i in range(int((mhi-mlo)//step)+1)]
    if grid[-1]!=mhi:grid.append(mhi)
    if args.selected_M and F(args.selected_M) not in grid:grid.append(F(args.selected_M))
    assert all(0<m<=F(1,2) for m in grid)
    R=aa(RAT_R);beta=aa(RAT_BETA);n=aa(RAT_N);beta2=aa(RAT_B2);S1=5/(11*arb.pi()).sqrt()
    rows=[];best=None;per={};objects={}
    for mr in sorted(grid):
        M=aa(mr);ratio=R/M
        NL=arb(module.calculate(str(RAT_R),str(mr),args.bits)['L_Q']);assert NL.is_finite()
        for rb,ss in cons['source_splits'].items():
            terms=[('local_gradient',cons['K1'],2/q),('local_scalar',cons['K0'],2*(1-delta/q)),
                   ('lower_source_near',ss['Bnear'],1-delta/q),('transport_second',cons['local_Taylor_coefficient'],1/q),
                   ('transport_third',cons['R3_coefficient'],1-1/q),('source_principal',qr*cons['source_H1'],1/q),
                   ('source_second',cq*cons['source_A2'],1-delta/q),('source_fractional',cq*cons['source_Aq'],F(1))]
            rates={name:a*ratio**aa(e) for name,a,e in terms}
            bg=ss['far_rate']+sum(rates.values(),arb(0));b=beta-bg-NL
            margin=b*M*M-n*M;linear=b*M-n;contract=S1*M/beta2
            assert all(v.is_finite() for v in [bg,b,margin,contract])
            row={'M':str(mr),'source_split_radius':rb,'background_loss':dump(bg),'nonlinear_loss':dump(NL),
                 'frozen_exterior_decay':dump(b),'forcing_n':str(RAT_N),'selfmap_energy_margin':dump(margin),
                 'selfmap_linear_margin':dump(linear),'contraction_ratio':dump(contract),'far_source_rate':dump(ss['far_rate']),
                 'rates':{name:dump(v) for name,v in rates.items()},'strict_selfmap_pass':bool(b>0 and margin>0 and contract<1)}
            rows.append(row);objects[mr,rb]=(margin,row,terms,rates,NL)
            if rb not in per or margin.lower()>per[rb][0].lower():per[rb]=(margin,row)
            if best is None or margin.lower()>best[0].lower():best=(margin,row)
    if args.selected_M:
        m=F(args.selected_M)
        choices=[objects[m,rb] for rb in cons['source_splits'] if not args.selected_Rb or rb==args.selected_Rb]
        assert choices;chosen=max(choices,key=lambda z:float(z[0].lower()))
        # FLOAT only selects a candidate; all final inequalities remain Arb.
        selected=chosen[1]
    else:selected=best[1]
    m=F(selected['M']);rb=selected['source_split_radius'];_,_,terms,rates,NL=objects[m,rb];ratio=R/aa(m)
    eps=cons['source_splits'][rb]['far_rate']+sum(((1-aa(e/2))*rates[name] for name,a,e in terms),arb(0))
    weak=sum((aa(e/2)*rates[name]/(ratio*ratio) for name,a,e in terms),arb(0))
    bglobal=beta-eps
    tangent_margin=(bglobal-NL)*aa(m)**2-n*aa(m)-weak*R*R
    er=F(math.ceil(float(eps.upper())*10**6)+1,10**6);cr=F(math.ceil(float(weak.upper()))+1)
    assert aa(er)>eps and aa(cr)>weak
    rounded_margin=(beta-aa(er)-NL)*aa(m)**2-n*aa(m)-aa(cr)*R*R
    tangent={'background_epsilon_arb':dump(eps),'background_weak_C_arb':dump(weak),
             'background_strong_decay_arb':dump(bglobal),'identity_selfmap_margin_arb':dump(tangent_margin),
             'rounded_epsilon_upper':str(er),'rounded_weak_C_upper':str(cr),'rounded_selfmap_margin_arb':dump(rounded_margin),
             'method':'AM-GM tangent at X/Y=(R/M)^2, theta=rate exponent/2; global background form only'}
    passed=bool(selected['strict_selfmap_pass'] and tangent_margin>0 and rounded_margin>0)
    return {'scan_rows':rows,'best_by_radius':{str(k):v[1] for k,v in per.items()},'selected':selected,'global_background_tangent':tangent,
            'strict_pass':passed,'gradient_embedding':dump(S1)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'fixed_parameter_closure_v01.json')
    ap.add_argument('--bits',type=int,default=512);ap.add_argument('--mmin',default='2/25');ap.add_argument('--mmax',default='1/2')
    ap.add_argument('--step',default='1/1000');ap.add_argument('--selected-M',dest='selected_M');ap.add_argument('--selected-Rb',dest='selected_Rb',type=int)
    args=ap.parse_args();ctx.prec=args.bits
    prefix=HERE/'matrix_prefix_signed_far_v01/result.json'
    if (not PATHS['matrix'].exists() and prefix.exists() and
        read(prefix).get('status')=='CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR'):
        PATHS['matrix']=prefix;STATUS['matrix']='CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR'
        PATHS['matrix_prefix_audit']=ART/'independent_closure_audit/matrix_prefix_audit.json'
        STATUS['matrix_prefix_audit']='INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS'
        PATHS['matrix_far_replay']=ART/'ROOT_SIGNED_MATRIX_FAR_REPLAY.json'
        STATUS['matrix_far_replay']='ROOT_SIGNED_MATRIX_FAR_REPLAY_PASS'
    record={'finished_utc':datetime.now(timezone.utc).isoformat(),'consumer_sha256':digest(Path(__file__)),
            'fixed_c':str(CEX),'q':'21/10','weight':'sqrt(1+4r²)','R':str(RAT_R),'beta_L2_rational':str(RAT_B2),
            'f2_upper':str(RAT_F2),'Q_forcing_upper':str(RAT_N),'matrix_beta':'7/10',
            'matrix_certificate_path':str(PATHS['matrix'].relative_to(ART))}
    missing=[k for k,p in PATHS.items() if not p.exists()]
    if missing:
        record.update(status='INCOMPLETE_CERTIFICATE_INPUTS',missing_inputs=missing,
                      available_input_sha256={k:digest(p) for k,p in PATHS.items() if p.exists()},stationary_existence='NOT CLAIMED')
        args.output.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='available_input_sha256'},indent=2));return
    try:
        inputs={k:read(p) for k,p in PATHS.items()}
        for k,d in inputs.items():assert d['status']==STATUS[k],('status',k,d['status'])
        rows,chunk_hashes=validate(inputs);cons=constants(inputs,rows);scan=scalar_scan(cons,args)
        a0=arb(inputs['structure']['rho_star_origin_slope_arb']);M=aa(F(scan['selected']['M']))
        slope=a0-5/(11*arb.pi()).sqrt()*M;assert slope>0
        record.update(status='FINAL_NUMERICAL_CLOSURE_PASS' if scan['strict_pass'] else 'FINAL_NUMERICAL_CLOSURE_NOT_PROVED',
                      all_input_bindings_and_covers_checked=True,input_sha256={k:digest(p) for k,p in PATHS.items()},
                      input_paths={k:str(p.relative_to(ART)) for k,p in PATHS.items()},
                      chunk_sha256=chunk_hashes,nonlinear_code_sha256=digest(ART/'finite_rank/Qnorm_nonlinear_bound.py'),
                      inherited_source_report_sha256=digest(IPM/'combined2/IPM.report.md'),
                      inherited_F_L2_certificate_sha256=INHERITED_F2,
                      constants={k:({str(i):dump(v) for i,v in z.items()} if isinstance(z,dict) and k not in ['source_splits'] else dump(z))
                                 for k,z in cons.items() if k!='source_splits'},
                      source_splits={str(rb):{k:dump(v) for k,v in d.items()} for rb,d in cons['source_splits'].items()},
                      positive_origin_slope_lower=dump(slope),**scan,
                      analytic_proof_dependencies=['LOCAL_Q_BACKGROUND_IDENTITY_v01.md','Q_TRANSPORT_SECOND_TAYLOR_v01.md',
                                                   'Q_FORCED_EVOLUTION_BRIDGE_v02.md','NONLINEAR_CORE_AND_Q_REVIEW_v01.md',
                                                   '../finite_rank/Q_SOURCE_FRACTIONAL_COMMUTATOR.md'],
                      stationary_existence='Numerical premises complete only if status PASS; apply the listed independently reviewed analytic proofs. Consumer still requires independent review.')
    except Exception as e:
        record.update(status='INVALID_OR_INCOMPLETE_CERTIFICATE_INPUT',error=repr(e),stationary_existence='NOT CLAIMED')
        args.output.write_text(json.dumps(record,indent=2)+'\n');raise
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['status','R','matrix_beta','Q_forcing_upper','selected','global_background_tangent','positive_origin_slope_lower']},indent=2))
if __name__=='__main__':main()
