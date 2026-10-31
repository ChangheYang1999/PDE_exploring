"""Parameterized compact audit. No full unsaved norm is reconstructed."""
import datetime,hashlib,json,math,os,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2]

def audit_record(path, *, seed, pressure_phase, core_radius, pressure_levels,
                 angles=(42,84)):
    if os.sched_getaffinity(0)!={35} or os.environ.get('CUDA_VISIBLE_DEVICES')!='':
        raise RuntimeError('CPU35 with GPU hidden required')
    p=Path(path).resolve();p.relative_to(R)
    now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    raw=p.read_bytes();start=now();tick=time.monotonic();d=json.loads(raw);checks=[]
    def ck(name,ok):
     checks.append(dict(name=name,pass_=bool(ok)))
     if not ok:raise AssertionError(name)
    def close(a,b,rtol=3e-12,atol=1e-28):
     return (a is b) if a is None or b is None else math.isclose(float(a),float(b),rel_tol=rtol,abs_tol=atol)
    ck('fixture_close_detects_change',close(2./3,2./3) and not close(2./3,2./3+1e-6))
    ck('explicitly incomplete with one coarse level',d['complete'] is False and len(d['levels'])==1 and d['partial_level']['index']==1);ck('CPU',d['device']=='cpu');ck('main_L6',d['leading_degree']==6);ck('unmodified_full_coefficients','no projection' in d['coefficient_policy']);ck('raw_source_moments',not d['zero_source_moments_imposed']);ck('seed',d['seed']==seed)
    ck('angles',(d['holdout_angular']['n_mu'],d['holdout_angular']['n_phi'])==angles);ck('phase',d['holdout_angular']['phase']==float(np.random.default_rng(seed).uniform(.01,.99)));ck('pressure_phase',d['pressure_phase']==pressure_phase);ck('common_reference',d['reference_core_radius']==core_radius and d['common_physical_reference_R0']==.3)
    ck('pressure_ladders',[(l['n_r_per_panel'],l['n_mu'],l['n_phi']) for l in d['levels']]==pressure_levels)
    for f,h in d['source_sha256'].items():ck('source:'+f,sha(R/f)==h)
    for f,h in d['input_sha256'].items():ck('input:'+f,sha(Path(d['input'])/f)==h)
    for q in d['prerequisites']:ck('prerequisite:'+q['path'],sha(q['path'])==q['sha256'])
    for k in ['radial_refinement_plan','cpu_plan']:ck(k,sha(R/d[k]['path'])==d[k]['sha256'])
    sp=d['storage_policy'];ck('compact_plan',sha(R/sp['plan'])==sp['plan_sha256']);ck('parent',sha(R/'scripts/verify_holdout_v6_cpu.py')==sp['parent_driver_sha256']);ck('serializer',sha(R/'scripts/compact_array_witness_v1.py')==sp['serializer_sha256']);ck('honest_storage',not sp['large_raw_arrays_retained'] and sp['full_array_audit_requires_recomputation'] and not sp['source_batch_disk_cache'] and not sp['angular_disk_cache'])
    archives=[]
    for wi,meta in enumerate([d['field_witnesses'],*[l['array_witnesses'] for l in d['levels']]]):
     f=Path(meta['path']);ck('witness_hash:'+str(wi),sha(f)==meta['sha256']);ck('witness_size:'+str(wi),f.stat().st_size==meta['stored_bytes']);
     with np.load(f,allow_pickle=False) as archive:z={k:archive[k] for k in archive.files};manifest=json.loads(str(z['witness_manifest_json']));ck('witness_manifest:'+str(wi),manifest=={k:v for k,v in meta.items() if k not in ['path','sha256','stored_bytes']})
     for k,v in manifest['arrays'].items():
      tag=str(wi)+':'+k;ck('shape_count:'+tag,math.prod(v['shape'])==v['elements']);ck('bytes:'+tag,v['nbytes']==v['elements']*np.dtype(v['dtype']).itemsize)
      if v['full_array_retained']:
       x=z[k];ck('full_shape:'+tag,list(x.shape)==v['shape'] and x.dtype.str==v['dtype']);ck('full_hash:'+tag,hashlib.sha256(x.tobytes(order='C')).hexdigest()==v['C_order_bytes_sha256']);ck('finite_full:'+tag,np.isfinite(x).all())
      else:
       ix=z[k+'_flat_indices'];x=z[k+'_flat_values'];expected=np.unique(np.linspace(0,v['elements']-1,min(64,v['elements']),dtype=np.int64)) if v['elements'] else np.empty(0,np.int64);ck('sample_indices:'+tag,np.array_equal(ix,expected));ck('sample_values_finite:'+tag,np.isfinite(x).all());ck('sample_shape:'+tag,x.size==v['witness_count']==ix.size and x.dtype.str==v['dtype'])
     archives.append(z)
    f=archives[0];r=f['radii'];dirs=f['directions'];aw=f['angular_weights'];ck('radial_order',np.all(r>0) and np.all(np.diff(r)>0));ck('sphere',np.max(abs(np.sum(dirs**2,axis=1)-1))<1e-14);ck('positive_weights',np.all(aw>0) and abs(sum(aw)-1)<2e-14);ck('point_count',len(r)*len(dirs)==d['holdout_points_total'])
    alpha=(1-d['c_l'])/d['c_l'];summ=[]
    for li,lev in enumerate(d['levels']):
     ck('no_source_cache:'+str(li),not lev['source_cache']['enabled']);ck('radial_green:'+str(li),lev['pressure_metadata']['method']=='full-space radial Green integral')
     for name,fam in lev['families'].items():
      rows=fam['shells'];denkeys=['weighted_linear_denominator','weighted_nonlinear_denominator','weighted_single_term_denominator'];totalmax=max(sum(row['term_rms']) for row in rows)
      for i,row in enumerate(rows):
       tag=f'{li}:{name}:{i}';rn=row['residual_rms'];un=row['U_rms'];ln=row['linear_rms'];nn=row['nonlinear_rms'];tn=row['term_rms'];aa=sum(tn[:3]);bb=sum(tn[3:]);rk=row['reference_radius'];rat=lambda a,b:a/b if b>0 else None
       vals=dict(rho_u=rat(rn,aa+bb),rho_u_six_term=rat(rn,sum(row['six_term_rms'])),rho_lin=rat(rn,aa),rho_nl=rat(rn,bb),sigma_u=rat(rn,tn[0]),physical_residual_over_U=rat(rn,un),weighted_absolute_residual=(1+rk)**(2*alpha+1)*rn,weighted_linear_denominator=(1+rk)**alpha*aa,weighted_nonlinear_denominator=(1+rk)**(2*alpha+1)*bb,weighted_single_term_denominator=(1+rk)**alpha*tn[0],absolute_r_alpha_residual=rk**alpha*rn,absolute_r_2alpha_plus1_residual=rk**(2*alpha+1)*rn,gram_nonlinear_to_linear_ratio=rat(nn,ln),gram_cosine=rat(row['gram_inner_product'],ln*nn),nonlinear_cancellation_ratio=rat(nn,bb),pressure_gradient_rms=tn[4])
       vals['rho_sp']=max(vals['rho_lin'],vals['rho_nl']) if aa>0 and bb>0 else None
       for k,v in vals.items():ck('identity:'+tag+':'+k,close(v,row[k]))
       ck('triangle:'+tag,abs(ln-nn)<=rn+2e-13*(ln+nn) and rn<=ln+nn+1e-28);ck('peak_identity:'+tag,close(row['pi_u'],row['peak_factor']*row['rho_u']) and close(row['pi_nl'],row['peak_factor']*row['rho_nl']))
       x,w=np.polynomial.legendre.leggauss(row.get('n_radial_per_panel',row['radial_nodes']));x=(x+1)/2;edges=row.get('panel_edges',[row['inner_radius'],row['outer_radius']]);rr=np.concatenate([(lo**3+x*(hi**3-lo**3))**(1./3) for lo,hi in zip(edges[:-1],edges[1:])]);ii=np.searchsorted(r,rr);dist=np.minimum(abs(r[np.minimum(ii,len(r)-1)]-rr),abs(r[np.maximum(ii-1,0)]-rr));ck('domain_nodes:'+tag,np.all(dist<2e-13*rr));ck('domain_count:'+tag,len(rr)==row['radial_nodes'])
       flags=[]
       if sum(tn)<1e-14*totalmax:flags.append('total_term_sum_small')
       if 0<i<len(rows)-1 and sum(tn)<1e-3*min(sum(rows[i-1]['term_rms']),sum(rows[i+1]['term_rms'])):flags.append('total_term_sum_small_both_neighbors')
       for k in denkeys:
        if row[k]<1e-14*max(v[k] for v in rows):flags.append(k+'_small_global')
        if 0<i<len(rows)-1 and row[k]<1e-3*min(rows[i-1][k],rows[i+1][k]):flags.append(k+'_small_both_neighbors')
       ck('flags:'+tag,flags==row['denominator_flags'] and row['peak_factor_exceeds_30']==(row['peak_factor']>30))
       if li:
        prev=d['levels'][li-1]['families'][name]['shells'][i];rf=row['pressure_refinement'];delta=rf['gradP_difference_rms'];dr=abs(rn-prev['residual_rms']);ck('pressure_refinement:'+tag,close(dr,rf['residual_norm_difference']) and close(delta-dr,rf['reverse_triangle_slack']) and close(delta/tn[4],rf['relative_to_current_gradP']) and close(delta/bb,rf['relative_to_current_nonlinear_denominator']));ck('reverse_triangle:'+tag,dr<=delta+1e-14*max(rn,prev['residual_rms']))
      for k,v in fam['summary'].items():
       if k.endswith('_max'):ck('maximum:'+str(li)+':'+name+':'+k,close(v,max((r[k[:-4]] for r in rows if r[k[:-4]] is not None),default=None)))
      ck('flagged_shells:'+str(li)+':'+name,fam['summary']['flagged_shells']==[i for i,row in enumerate(rows) if row['denominator_flags']]);ck('equal_shell_rms:'+str(li)+':'+name,close(fam['summary']['rho_u_equal_shell_rms'],math.sqrt(sum(row['rho_u']**2 for row in rows)/len(rows))))
      if li==len(d['levels'])-1:summ.append(dict(family=name,summary=fam['summary'],refinement='OPEN: second pressure level incomplete'))
    ck('record unchanged',p.read_bytes()==raw)
    return dict(started_utc=start,completed_utc=now(),elapsed_seconds=time.monotonic()-tick,
        complete=True,all_checks_pass=all(c['pass_'] for c in checks),check_count=len(checks),
        checks=checks,input=str(p),input_sha256=hashlib.sha256(raw).hexdigest(),
        script_sha256=sha(Path(__file__)),summary=summ,
        scope='Partial-result audit only: completed coarse-level provenance, saved field and pressure witnesses, scalar norm identities and summary arithmetic. No second level or source witness is available. Full unsaved fields and norms are not reconstructed; no pressure-refinement or complete-holdout verdict.')
