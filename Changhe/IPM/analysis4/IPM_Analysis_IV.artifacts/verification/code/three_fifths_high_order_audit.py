"""Independent Cartesian equation checks through300 for delta3/5."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, gzip, json, pickle, sys, time, traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq as Q
from flint import arb,ctx
from integer_period_high_order_audit import Laurent,field,ball
from stream_precision_audit import unpack
from pure_cartesian_ball import refine_root
ROOT=Path('research/209_three_fifths_high_order')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x):return x.str(45,radius=True)
def put(path,obj):
    temp=path.with_name(path.name+'.new');temp.write_text(json.dumps(obj,indent=2)+'\n');temp.replace(path)

def one(index,bits):
    started=time.monotonic();ctx.prec=bits;zero=arb(0)
    tag=f'tuned35_r{index}_p1024';source=Path('../a4-num/ckpt')/(tag+'.pkl')
    raw=source.read_bytes();metadata=dict(path=str(source),sha256=sha256(raw).hexdigest(),bytes=len(raw));state=pickle.loads(raw);del raw
    assert state['ring']=='arb' and state['prec']==1024 and str(state['delta_exact'])=='3/5'
    assert max(state['f'])==300 and max(state['g'])==300
    hp=source.with_name(tag+'_H.json');hraw=hp.read_bytes();hs=json.loads(hraw)
    assert hs['delta']=='3/5' and hs['period']==10 and '300' not in hs['H']
    assert all(str(n) in hs['H'] for n in range(10,300,10))
    metadata['harmonic_table']=dict(path=str(hp),sha256=sha256(hraw).hexdigest())
    bp=Path(f'research/202_three_fifths_numerical_audit/verification/root{index}_selected.pkl.gz');braw=gzip.decompress(bp.read_bytes());selected=pickle.loads(braw)
    selection_changes=[];archived_last=max(selected['f'])
    for key in ['f','g']:
        for n in selected[key]:
            assert len(state[key][n])==len(selected[key][n])
            for j,(new,old) in enumerate(zip(state[key][n],selected[key][n])):
                if new==old:continue
                # A snapshot may include its final, deliberately untuned stream
                # kernel. Only that one zero slot may later be filled by tuning.
                assert key=='g' and n==archived_last and n%10==0 and j==3*(n//10)-1
                assert n>40 and n<300 and arb(*unpack(old)).is_zero()
                assert str(n) in hs['H'] and arb(*unpack(new)).overlaps(arb(hs['H'][str(n)]['str']))
                selection_changes.append(dict(kind=key,n=n,index=j,reason='formerly provisional final harmonic now tuned'))
    metadata['archived_selection']=dict(path=str(bp),sha256=sha256(braw).hexdigest(),orders=sorted(selected['f']),permitted_changes=selection_changes);del selected,braw
    rp=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');rd=json.loads(rp.read_text());assert rd['all_checks_pass']
    b,interval=refine_root(rd['primitive_coefficients'],rd['real_roots'][index-1]['interval'],bits+64)
    f={n:[arb(*unpack(v)) for v in state['f'][n]] for n in range(1,301)}
    g={n:[arb(*unpack(v)) for v in state['g'][n]] for n in range(1,301)};del state
    assert f[1][0]==1 and f[1][1].contains(b) and len(f[1])==2
    F={n:field(f[n],True) for n in f};G={n:field(g[n],False) for n in g}
    degree=lambda n:Q(1)-Q(3*n,5)
    FX={n:F[n].derivative(degree(n)) for n in F};FY={n:F[n].derivative(degree(n),True) for n in F}
    GX={n:G[n].derivative(degree(n)+1) for n in G};GY={n:G[n].derivative(degree(n)+1,True) for n in G}
    counts=dict(poisson_coefficients=0,nonlinear_coefficients=0,ordered_pairs=0,compatibility_coordinates=0,harmonic_table_overlaps=0)
    maxres=zero;maxrad=zero;rows=[]
    for n in range(1,301):
        M=sum(map(abs,f[n]),zero);S=sum(map(abs,g[n]),zero);assert M>0 and S>0
        dr=sum((v.rad() for v in f[n]),zero)/sum((abs(v.mid()) for v in f[n]),zero);maxrad=maxrad.max(dr)
        if n<300:
            sr=sum((v.rad() for v in g[n]),zero)/sum((abs(v.mid()) for v in g[n]),zero);maxrad=maxrad.max(sr)
        poisson=GX[n].derivative(degree(n)).scale(-1)+GY[n].derivative(degree(n),True)-FX[n]
        for j,v in enumerate(poisson.poly.coeffs()):
            assert v.contains(0),('Poisson',n,poisson.low+j,text(v));counts['poisson_coefficients']+=1
        if n%10==0:
            k=n//10;assert f[n][3*k-2].contains(0);counts['compatibility_coordinates']+=1
            if n<300:
                assert g[n][3*k-1].overlaps(arb(hs['H'][str(n)]['str']));counts['harmonic_table_overlaps']+=1
        if n>40:
            nonlinear=Laurent()
            for i in range(1,n):
                nonlinear=nonlinear+GX[i]*FY[n-i]-GY[i]*FX[n-i];counts['ordered_pairs']+=1
            lm=ball(Q(3*(n-1),2));residual=nonlinear-F[n].scale(lm)
            for j,v in enumerate(residual.poly.coeffs()):
                assert v.contains(0),('density',n,residual.low+j,text(v));counts['nonlinear_coefficients']+=1
            maxres=maxres.max(sum(map(abs,residual.poly.coeffs()),zero)/(lm*M))
        if n%25==0 or n==299:
            row=dict(n=n,density_norm=text(M),density_root=text((M.log()/n).exp()),density_relative_radius=text(dr))
            if n<300:row.update(stream_norm=text(S),stream_root=text((S.log()/n).exp()),stream_relative_radius=text(sr))
            else:row['stream_status']='untuned final harmonic; excluded'
            rows.append(row)
            progress=dict(checked_at_utc=stamp(),root_index=index,completed_order=n,target_order=300,counts=counts,maximum_relative_nonlinear_residual=text(maxres),maximum_norm_relative_radius=text(maxrad),norms=rows,actual_elapsed_s=time.monotonic()-started)
            put(ROOT/'verification'/f'root{index}_progress.json',progress)
            print(json.dumps({k:progress[k] for k in ['checked_at_utc','root_index','completed_order','actual_elapsed_s']}),flush=True)
    metadata['producer_code']={str(Path('../a4-num/code')/name):sha256((Path('../a4-num/code')/name).read_bytes()).hexdigest() for name in ['ffcore.py','tuned_c3.py','tuned_cQ.py','tuned_general.py']}
    result={**progress,'all_checks_pass':True,'bits':bits,'independent_prefix_order':40,'root_isolating_interval':interval,'source':metadata,'root_input':dict(path=str(rp),sha256=sha256(rp.read_bytes()).hexdigest()),'scope':'Finite interval consistency; the independent producer induction supplies the distinct enclosure argument.'}
    put(ROOT/'verification'/f'root{index}_checks.json',result)
    print(json.dumps(dict(all_checks_pass=True,root_index=index,actual_elapsed_s=time.monotonic()-started)),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--roots',default='4');ap.add_argument('--bits',type=int,default=1536);args=ap.parse_args()
    for index in map(int,args.roots.split(',')):
        try:one(index,args.bits)
        except Exception as exc:
            record=dict(checked_at_utc=stamp(),root_index=index,type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
            put(ROOT/'verification'/f'root{index}_FAILURE.json',record);print(json.dumps(record),flush=True);raise SystemExit(1)
    for name in ['three_fifths_high_order_audit.py','integer_period_high_order_audit.py','integer_period_prefix.py','pure_cartesian_ball.py','stream_precision_audit.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
if __name__=='__main__':main()
