"""Certify contiguous square shells of an exact finite-envelope witness."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from envelope_arb import ArbEnvelope
from envelope_rectangle_core import shell_rectangles,cell_interval
import argparse,json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True)
    p.add_argument('--n',type=int,default=16);p.add_argument('--out',required=True);args=p.parse_args()
    assert args.n>=2 and -40<=args.start<args.stop<=40
    ctx.prec=160;env=ArbEnvelope();started=time.monotonic();rows=[]
    for exponent in range(args.start,args.stop):
        total=arb(0);error=arb(0);nodes=0;verts=0
        rects=shell_rectangles(exponent,args.n)
        for i,rect in enumerate(rects):
            value,err,count=cell_interval(env,rect);total+=4*value;error+=4*err
            nodes+=count['nodes'];verts+=count['vertices']
        row=dict(exponent=exponent,cells=len(rects),integral=total.str(40,more=True),variation_error=error.str(36,more=True),tree_nodes=nodes,vertices=verts)
        rows.append(row);print(row,'seconds',time.monotonic()-started,flush=True)
    paths=['code/envelope_arb.py','code/envelope_rectangle_core.py','code/certify_envelope_rectangles.py','data/envelope_D_half_axis_nodes_symmetric.json']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha='1/2',precision_bits=ctx.prec,n=args.n,shell_start=args.start,shell_stop=args.stop,rows=rows,source_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in paths},elapsed_seconds=time.monotonic()-started,status='Partial exact-mass envelope certificate; requires full shell coverage, endpoint errors and actual identity term.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
