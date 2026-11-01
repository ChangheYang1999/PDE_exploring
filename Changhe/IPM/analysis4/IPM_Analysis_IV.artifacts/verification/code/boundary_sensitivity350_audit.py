"""Independent norms for one perturbed and one midpoint continuation."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, gc, json, pickle, re, sys, time, traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from flint import arb, ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT = Path('research/244_final_sensitivity350')

def stamp(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(x): return x.str(42, radius=True)
def put(path, obj):
    tmp = path.with_name(path.name + '.new')
    tmp.write_text(json.dumps(obj, indent=2) + '\n'); tmp.replace(path)

def norms(path, end):
    raw = path.read_bytes()
    meta = dict(path=str(path), sha256=sha256(raw).hexdigest(), bytes=len(raw))
    state = pickle.loads(raw); del raw
    assert (state['A'], state['B'], state['ring'], state['prec']) == ('2','3','arb',512)
    assert max(state['f']) >= end
    meta.update(maximum_order=max(state['f']), flags={k:state.get(k) for k in ['radii_reset_at','perturbed_seed']})
    data = {}; zero = arb(0); count = 0
    for n in range(330,end+1):
        row = {}
        for field in ['f','g']:
            cols = []
            for col in state[field][n]:
                values = [arb(*unpack(v)) for v in col]
                count += len(values)
                cols.append(sum(map(abs, values), zero))
            total = sum(cols,zero); assert total > 0
            row[field] = dict(total=total, columns=cols)
        data[n] = row
    del state; gc.collect()
    meta['coefficient_positions'] = count
    return meta, data

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--through',type=int,default=340)
    args=parser.parse_args(); end=args.through; started=time.monotonic();ctx.prec=768
    mp=Path('../a4-num/ckpt/log_sin1_c3_from329.pkl')
    pp=Path('../a4-num/ckpt/log_sin1_c3_pert329.pkl')
    mm,mid=norms(mp,end);print(json.dumps(dict(stage='midpoint_loaded',time=stamp())),flush=True)
    pm,pert=norms(pp,end);print(json.dumps(dict(stage='perturbed_loaded',time=stamp())),flush=True)
    tablep=Path('../a4-num/notes/compare_pert.txt');table=tablep.read_bytes()
    parsed={}
    for line in table.decode().splitlines():
        bits=line.split()
        if bits and bits[0].isdigit(): parsed[int(bits[0])]=bits
    log10=arb(10).log(); rows=[]; comparisons=0; mismatches=[]
    for n in range(330,end+1):
        dm=(pert[n]['f']['total']/mid[n]['f']['total']).log()/log10
        dn=(pert[n]['g']['total']/mid[n]['g']['total']).log()/log10
        cols=[abs((a/b).log()/log10) for a,b in zip(pert[n]['f']['columns'],mid[n]['f']['columns']) if a>0 and b>0]
        largest=arb(0)
        for v in cols: largest=largest.max(v)
        row=dict(n=n,dM=pack(dm),dN=pack(dn),dR=pack(dn-dm),maximum_column_difference=pack(largest),
                 dM_display=text(dm),dN_display=text(dn),dR_display=text(dn-dm),maximum_column_difference_display=text(largest),
                 density_relative_norm_change=text((dm*log10).exp()-1),stream_relative_norm_change=text((dn*log10).exp()-1),
                 density_norm_change_below_1e8=abs(dm)<arb('1e-8'),stream_norm_change_below_1e8=abs(dn)<arb('1e-8'),
                 every_density_column_change_below_1e8=largest<arb('1e-8'))
        if n in parsed:
            cells=parsed[n]
            for value,printed in zip([dm,dn,dn-dm,largest],cells[2:6]):
                exponent=int(printed.lower().split('e')[1])
                tolerance=arb('0.0051')*(arb(10)**exponent)
                if not value.overlaps(arb(printed,tolerance)): mismatches.append(dict(n=n,value=text(value),printed=printed,tolerance=text(tolerance),absolute_error=text(abs(value-arb(printed)))))
                comparisons+=1
        rows.append(row)
    monotonic=[]
    for i in range(1,len(rows)):
        n=rows[i]['n']; previous=n-1
        for field,label in [('f','M'),('g','N')]:
            a=abs((pert[previous][field]['total']/mid[previous][field]['total']).log()/log10)
            b=abs((pert[n][field]['total']/mid[n][field]['total']).log()/log10)
            if b>a: monotonic.append(dict(field=label,previous=previous,n=n,previous_difference=text(a),difference=text(b)))
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,bits=768,orders=[330,end],
                scope='Finite differences between two selected input configurations; no box stability bound.',
                midpoint_source=mm,perturbed_source=pm,printed_comparisons=comparisons,printed_rounding_mismatches=mismatches,all_printed_roundings_match=not mismatches,rows=rows,
                consecutive_increases=monotonic,table=dict(path=str(tablep),sha256=sha256(table).hexdigest()),
                actual_elapsed_s=time.monotonic()-started)
    out=ROOT/'verification'/f'checks_N{end}.json';put(out,result)
    (ROOT/'sources'/f'compare_pert_N{end}.txt').write_bytes(table)
    for name in ['boundary_sensitivity350_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:
        (ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,orders=[330,end],printed_comparisons=comparisons,rounding_mismatches=mismatches,consecutive_increases=monotonic,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)

if __name__=='__main__':
    try:main()
    except Exception as exc:
        d=dict(checked_at_utc=stamp(),type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
        put(ROOT/'verification'/'FAILURE.json',d);print(json.dumps(d),flush=True);raise SystemExit(1)
