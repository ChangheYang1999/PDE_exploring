"""Complete ordered stream with exact convolution comparisons and dual interval bounds."""
from protocol import *
import argparse,time,resource
import kernels,bounds
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))

def cell_result(d,i,reference):
    started=time.monotonic();c=d.cell(i);bounds.ctx.prec=512;bind(c,reference)
    model=kernels.build(c['arrays']);linear_checks=kernels.validate_actual_linear_maps(model);co=kernels.combine(model,c['elo'],c['ehi']);err=kernels.error_inputs(c['arrays'],model)
    outputs={}
    for name in ['arb512','iv200']:
        _,o=bounds.Engine(name).cell(c,model,co,err);outputs[name]=o
    overlap(outputs['arb512'],outputs['iv200'])
    return {'type':'cell','utc':now(),'cell':i,'a':str(c['a']),'b':str(c['b']),'h':str(c['h']),'array_manifest':c['array_manifest'],'exact_convolutions':model['convolutions'],'all_product_coefficient_equalities':sum(v['coefficients'] for v in model['convolutions']),'actual_linear_identity_checks':linear_checks,'bounds':{n:compact_output(o) for n,o in outputs.items()},'seconds':time.monotonic()-started}

def tail_result():
    inp=bounds.tail_inputs();outputs={}
    for name in ['arb512','iv200']:
        _,out=bounds.tails(bounds.Engine(name),inp);outputs[name]=out
    for a,b in zip(outputs['arb512']['weights'],outputs['iv200']['weights']):assert max(F(a['lower_exact']),F(b['lower_exact']))<=min(F(a['upper_exact']),F(b['upper_exact']))
    out={}
    for name,z in outputs.items():out[name]={k:([compact(v) for v in vals] if isinstance(vals,list) else vals) for k,vals in z.items()}
    return {'status':'PASS_ENTIRE_INNER_OUTER_DERIVATIVE_TAIL_CALCULATIONS','geometry_exact':{'a':str(bounds.A),'b':str(bounds.B),'k':str(bounds.K),'L':str(bounds.L)},'counts':{**inp[-1],'weighted_moment_intersections':3508},'bounds':out}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);ap.add_argument('--resume',action='store_true');args=ap.parse_args();full=args.tag=='full';cells=list(range(7809)) if full else SMOKE
    start=now();tick=time.monotonic();pins,deps,freeze=source()
    if full:
        assert os.getpriority(os.PRIO_PROCESS,0)>=19,'lowest CPU priority required'
        q=load(ROOT/'research/canonical_center_second/evidence/queue_status.json');assert q['status']=='COMPLETE_CENTER_COMPUTATION_AND_AUDIT_REQUIRES_REVIEW','174 serialized computation terminal'
        pre=load(OUT/'preparation_acceptance.json');assert pre['status']=='CONFIRMED_FULL_DERIVATIVE_NORM_PREPARATION_ONLY';rehash(pre['files']);pin(pins,OUT/'preparation_acceptance.json')
    assert when(freeze['utc'])<when(start)
    data_object=data();references=radial_rows();sums={name:[F(0),F(0)] for name in ['arb512','iv200']};counts=0
    header={'type':'header','schema':'full-physical-derivative-norm-v1','cells':cells,'sources':dict(sorted(pins.items())),'parents':deps,'source_freeze_sha256':sha(OUT/'source_freeze.json'),'engines':['arb512','iv200'],'compact_endpoint_bits':128,'replay_cells':REPLAY if full else SMOKE}
    path=OUT/(args.tag+'_rows.jsonl');completed=[];hasher=hashlib.sha256();saved_footer=None
    if path.exists():
        assert args.resume
        with path.open('rb+') as f:
            pos=0
            while True:
                raw=f.readline()
                if not raw:break
                if not raw.endswith(b'\n'):f.truncate(pos);f.seek(pos);break
                z=parse(raw)
                if not pos:assert z==header
                elif z['type']=='cell':
                    assert saved_footer is None and len(completed)<len(cells) and z['cell']==cells[len(completed)];completed.append(z)
                else:
                    assert saved_footer is None and z['type']=='footer' and z['complete'] is True and z['cells']==len(completed)==len(cells) and z['prior_stream_sha256']==hasher.hexdigest();saved_footer=z
                hasher.update(raw);pos=f.tell()
            if not pos:
                raw=(canonical(header)+'\n').encode();f.write(raw);f.flush();os.fsync(f.fileno());hasher.update(raw)
        for row in completed:
            for name in sums:
                for p,v in enumerate(row['bounds'][name]['norm_squares']):sums[name][p]+=dyad(v['hi'])
            counts+=row['all_product_coefficient_equalities']
    else:
        with path.open('xb') as f:raw=(canonical(header)+'\n').encode();f.write(raw);hasher.update(raw)
    restart={'utc':now(),'completed':len(completed),'last_completed':completed[-1]['cell'] if completed else None,'first_uncompleted':cells[len(completed)] if len(completed)<len(cells) else None,'source_freeze_sha256':header['source_freeze_sha256']}
    with (OUT/(args.tag+'_restarts.jsonl')).open('a') as f:f.write(canonical(restart)+'\n')
    tail=tail_result();tp=OUT/(args.tag+'_tails.json')
    if tp.exists():assert load(tp)==tail
    else:write(tp,tail)
    with path.open('ab') as f:
        for i in cells[len(completed):]:
            assert datetime.now(timezone.utc)<datetime(2026,10,22,12,35,tzinfo=timezone.utc),'leave deadline time for audit'
            row=cell_result(data_object,i,references[i]);raw=(canonical(row)+'\n').encode();f.write(raw);f.flush();hasher.update(raw)
            for name in sums:
                for p,v in enumerate(row['bounds'][name]['norm_squares']):sums[name][p]+=dyad(v['hi'])
            counts+=row['all_product_coefficient_equalities']
            if (i+1)%10==0 or i==cells[-1]:os.fsync(f.fileno());print(canonical({'utc':now(),'completed_cell':i,'seconds_last':row['seconds'],'equalities_so_far':counts,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
        if saved_footer is None:
            footer={'type':'footer','utc':now(),'complete':True,'cells':len(cells),'prior_stream_sha256':hasher.hexdigest(),'all_product_coefficient_equalities':counts};f.write((canonical(footer)+'\n').encode());f.flush();os.fsync(f.fileno())
        else:assert saved_footer['all_product_coefficient_equalities']==counts
    results={};ceilings=[]
    for name in sums:
        eng=bounds.Engine(name);squares=[];norms=[]
        for p in range(2):
            exact=sums[name][p]+sum(dyad(tail['bounds'][name][label][p]['hi']) for label in ['inner_norm_squares','outer_norm_squares'])
            v=eng.q(exact);squares.append(bounds.encode(v,name));norms.append(bounds.encode(eng.sqrt(v),name))
        results[name]={'middle_bound_sums_exact':[str(v) for v in sums[name]],'whole_plane_bound_squares':squares,'whole_plane_norm_bounds':norms}
    for p in range(2):ceilings.append(ceiling(max(F(results[name]['whole_plane_norm_bounds'][p]['upper_exact']) for name in results)))
    rehash(pins)
    out={'start_utc':start,'utc':now(),'status':'COMPUTED_COMPLETE_DERIVATIVE_NORM_BOUNDS_REQUIRES_INDEPENDENT_AUDIT' if full else 'PASS_SIX_CELL_DERIVATIVE_PREPARATION_DIAGNOSTIC_ONLY','full_middle':full,'cells':len(cells),'all_product_coefficient_equalities':counts,'rows_sha256':sha(path),'tails_sha256':sha(tp),'restarts_sha256':sha(OUT/(args.tag+'_restarts.jsonl')),'engines':results,'strict_decimal_ceilings':ceilings,'parents':deps,'source_freeze_sha256':header['source_freeze_sha256'],'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'New direct canonical physical derivative upper bounds in weak weighted H1. Smoke omits most cells and is not a full-plane bound. Full result requires complete output audit/replay and actual later review. No inverse or nonlinear closure.'}
    write(OUT/(args.tag+'_summary.json'),out);print(canonical({k:v for k,v in out.items() if k not in ['files','engines']}),flush=True)
if __name__=='__main__':main()
