"""Reject nonfinite scalar values in completed certificate records.

This supplementary audit addresses an observed python-flint0.9 pitfall where
integer power of a ball centered atzero can be indeterminate. It is not a
replacement for panel coverage, source bindings, or the analytic proofs.
"""
import argparse,json,math
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('directories',type=Path,nargs='+');args=ap.parse_args();ctx.prec=384
    files={};counts={'finite_arb_strings':0,'finite_machine_numbers':0};bad=[]
    def visit(value,path):
        if isinstance(value,dict):
            for key,item in value.items():visit(item,path+'/'+key)
        elif isinstance(value,list):
            for index,item in enumerate(value):visit(item,path+'/'+str(index))
        elif isinstance(value,float):
            if math.isfinite(value):counts['finite_machine_numbers']+=1
            else:bad.append({'path':path,'value':str(value)})
        elif isinstance(value,str):
            try:number=arb(value)
            except(ValueError,TypeError):return
            if number.is_finite():counts['finite_arb_strings']+=1
            else:bad.append({'path':path,'value':value})
    for directory in args.directories:
        for path in sorted(directory.glob('*.json')):
            files[str(path)]=sha256(path.read_bytes()).hexdigest()
            visit(json.loads(path.read_text()),str(path))
    result={'status':'FINITE_SCALARS_CONFIRMED'if not bad else 'NONFINITE_SCALARS_FOUND',
        'files':files,'counts':counts,'nonfinite_values':bad,
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'finished_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Supplementary numerical scalar audit only. No assertion of complete domain coverage or theorem closure.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='files'},indent=2),flush=True)
    assert not bad

if __name__=='__main__':main()
