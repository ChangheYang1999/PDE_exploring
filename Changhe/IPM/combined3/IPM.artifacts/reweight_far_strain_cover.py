#!/usr/bin/env python3
"""Reuse a whole-plane actual strain cover with a broader erflog cut.

The original saved panel bound includes a scalar nonnegative cut. Recover
a valid underlying strain bound by exact rational division by the exact
binary64 cut upper used by that producer, then apply the new cut upper.
No field is resampled. Partial coverage is explicitly not a certificate.
"""
import argparse
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('far_strain_producer',HERE/'certify_far_strain.py')
producer=importlib.util.module_from_spec(spec);spec.loader.exec_module(producer)

def aa(q):
    q=F(q)
    return arb(q.numerator)/q.denominator

def upper_double(x):return np.nextafter(float(x.upper()),np.inf)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--scale',default='2');ap.add_argument('--bound',default='9/25')
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    scale,bound=F(args.scale),F(args.bound);assert scale>=1 and bound>0
    cfg=json.loads((args.source/'configuration.json').read_text())
    assert cfg['bindings']==producer.bindings()
    ctx.prec=cfg['precision'];ratio=aa(cfg['ratio']);rmin=aa(cfg['rmin']);rmax=aa(cfg['rmax'])
    rows={};files={}
    for file in sorted(args.source.glob('chunk_*.json')):
        rec=json.loads(file.read_text());assert rec['configuration']==cfg
        files[file.name]=sha256(file.read_bytes()).hexdigest()
        for row in rec['rows']:
            assert row['index'] not in rows
            rows[row['index']]=row
    converted=[]
    for index,row in sorted(rows.items()):
        right=rmin*ratio**(index+1)
        if right>rmax:right=rmax
        old=F(float(upper_double(1-producer.chi(right))))
        new=F(float(upper_double(1-producer.chi(right/aa(scale)))))
        assert old>0 and 0<new<=old
        square=F(row['upper_square_float'])*new**2/old**2
        converted.append({'index':index,'new_upper_square_exact':str(square),
                          'pass':square<=bound**2})
    complete=sorted(rows)==list(range(cfg['panels']))
    inner=aa('137/125')*(1-producer.chi(rmin/aa(scale)))
    exterior=None;endpoint_pass=False
    result_path=args.source/'result.json'
    if complete and result_path.exists():
        old_result=json.loads(result_path.read_text())
        assert old_result['configuration']==cfg
        exterior=arb(old_result['exterior_upper_arb'])
        endpoint_pass=bool(inner<=aa(bound) and exterior<=aa(bound))
    ok=complete and endpoint_pass and all(r['pass'] for r in converted)
    out={'status':'CERTIFIED_REWEIGHTED_FAR_STRAIN' if ok else 'PARTIAL_OR_FAILED_NO_CERTIFICATE',
         'cut_scale':str(scale),'operator_sup_upper':str(bound),
         'source_configuration':cfg,'source_chunk_sha256':files,
         'panels_present':len(rows),'complete':complete,'inner_upper_arb':str(inner),
         'exterior_upper_arb':str(exterior) if exterior is not None else None,
         'failed_panels':[r['index'] for r in converted if not r['pass']],
         'largest_core_square_display_float':max([float(F(r['new_upper_square_exact'])) for r in converted],default=0.),
         'panel_results':converted,
         'finished_utc':datetime.now(timezone.utc).isoformat(),
         'scope':'Actual (1-chi(r/scale))*Sym Du013 bound; inherits the explicitly identified inner strain input.'}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_configuration','source_chunk_sha256','panel_results']},indent=2))

if __name__=='__main__':main()
