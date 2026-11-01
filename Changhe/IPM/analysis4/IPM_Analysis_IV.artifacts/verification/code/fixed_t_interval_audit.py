"""Independent fixed-log polynomial evaluations of retained exact dyadic balls."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack

def text(x):return x.str(32,radius=True)
def main():
    start=time.monotonic();ctx.prec=640;root=Path('research/66_fixed_t_intervals')
    src=Path('research/64_log_precision_updates/verification/log_sin1_c3_p512_N210_20261031T050158Z/selected_packed_coefficients.json')
    raw=src.read_bytes(); data=json.loads(raw)
    leadsrc=Path('../a4-lead/logs/tprof_d2_3_amp5_N260.jsonl'); leadraw=leadsrc.read_bytes()
    (root/'sources/lead_tprofile.jsonl').write_bytes(leadraw)
    leads={r['n']:r for r in map(json.loads,leadraw.splitlines())}
    ts=[-40,-20,-10,-5,-2,-1,0,1,2,5,10,20,40]
    rows=[];largest_error=0.;largest=None;l10=arb(10).log()
    for field in ['f','g']:
        for ns,packed in sorted(data[field].items(),key=lambda item:int(item[0])):
            n=int(ns); cols=[[arb(*unpack(v)) for v in col] for col in packed]
            L=max(map(len,cols)); colnorm=[sum(map(abs,col),arb(0)) for col in cols]
            for t in ts:
                value=[arb(0)]*L; absolute=arb(0)
                for q in range(len(cols)-1,-1,-1):
                    value=[v*t+(cols[q][m] if m<len(cols[q]) else arb(0)) for m,v in enumerate(value)]
                    absolute=absolute*abs(t)+colnorm[q]
                norm=sum(map(abs,value),arb(0));assert norm>0
                lg=norm.log()/l10;lgabs=absolute.log()/l10
                lead=leads[n];idx=lead['t'].index(t); key='lF' if field=='f' else 'lG'
                errors=[abs(float(lg.mid())-lead[key][idx]),abs(float(lgabs.mid())-lead[key+'abs'][idx])]
                if max(errors)>largest_error:largest_error=max(errors);largest=[field,n,t]
                rows.append(dict(field=field,n=n,t=t,norm=text(norm),absolute_coefficient_sum=text(absolute),log10_norm=text(lg),
                    log10_absolute_sum=text(lgabs),log10_cancellation=text(lgabs-lg),root=text((norm.log()/n).exp()),
                    log10_weighted_term=text(lg-arb(2)*(n-1)*t/(3*l10)),
                    relative_interval_radius=text(norm.rad()/abs(norm.mid())),lead_log10_errors=errors))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
        source_path=str(src),source_sha256=sha256(raw).hexdigest(),lead_source_path=str(leadsrc),lead_sha256=sha256(leadraw).hexdigest(),
        delta='2/3',input='sin(theta)',canonical_resonant_constants_zero=True,precision_bits=640,
        rows=rows,count=len(rows),maximum_lead_log10_difference=largest_error,maximum_difference_location=largest,
        actual_elapsed_s=time.monotonic()-start)
    (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['fixed_t_interval_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
if __name__=='__main__':main()
