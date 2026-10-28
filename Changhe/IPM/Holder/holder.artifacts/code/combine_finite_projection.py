"""Verify exact coverage and combine all errors for a D lower certificate."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx
import argparse,json,hashlib
ctx.prec=192;ROOT=Path(__file__).resolve().parents[1]
def lower_decimal(value,places=10):
    k=int((arb(value.lower())*10**places).floor().unique_fmpz())
    return f'{k//10**places}.{k%10**places:0{places}d}'
def main():
    p=argparse.ArgumentParser();p.add_argument('inputs',nargs='+');p.add_argument('--profile',default='data/profile_constant_certificate.json');p.add_argument('--out',required=True);a=p.parse_args()
    sources=[(ROOT/name,json.loads((ROOT/name).read_text())) for name in a.inputs]
    sources.sort(key=lambda item:item[1]['row_start']);base=sources[0][1];at=0;regular=arb(0)
    keys=['alpha','shape','precision_bits','radial_cells_per_patch','angular_cells','source_hashes','local_leading','local_loss','tail_error','normalizer']
    for path,data in sources:
        assert all(data[k]==base[k] for k in keys)
        assert data['row_start']==at and data['row_stop']>at
        assert data['cells']==(data['row_stop']-data['row_start'])*data['angular_cells']
        at=data['row_stop'];regular+=arb(data['regular_interval'])
    assert at==3*base['radial_cells_per_patch']
    for name,digest in base['source_hashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    profilepath=ROOT/a.profile;profile=json.loads(profilepath.read_text())
    for name,digest in profile['source_hashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    row=next(r for r in profile['rows'] if Fraction(r['alpha'])==Fraction(base['alpha']))
    K=arb(row['safe_upper']);assert K>=arb(row['upper_interval'])
    value=(regular+arb(base['local_leading'])-arb(base['local_loss'])-arb(base['tail_error'])+arb(1)/2)/K
    assert value>0 and value.is_finite()
    paths=[s[0] for s in sources]+[profilepath,Path(__file__)]
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=base['alpha'],shape=base['shape'],precision_bits=ctx.prec,regular_interval=regular.str(45,more=True),profile_upper=str(K),lower_expression_interval=value.str(45,more=True),safe_D_lower=lower_decimal(value),exact_coverage_rows=at,input_hashes={str(s.relative_to(ROOT)):hashlib.sha256(s.read_bytes()).hexdigest() for s in paths},status='Certified lower bound for D, provided the finite witness and component enclosure audits are confirmed. This is not an enclosure of the exact norm.')
    (ROOT/a.out).write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
