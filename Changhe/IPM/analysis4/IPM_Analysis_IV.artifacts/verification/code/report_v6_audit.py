"""Independent retained-ball and published-table scope audit."""
from read_evidence_bytes import read_bytes as read_evidence_bytes
from datetime import datetime,timezone
from pathlib import Path
from hashlib import sha256
import json,math,time
from flint import arb,fmpz,ctx


def dyadic(m,e):
    a=arb(fmpz(int(m)))*arb(2)**int(e)
    assert a.is_exact()
    return a


def unpack(record):
    m,e,r=record
    mid=dyadic(m,e)
    if r=='0':rad=arb(0)
    else:
        rm,re=r.split('*2^');rad=dyadic(rm,re)
    return mid,rad


def txt(x):return x.str(32,radius=True)


def main():
    start=time.monotonic();ctx.prec=640;root=Path('research/61_report_v6_audit')
    files={'lead_theory.md':Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md'),
           'lead_summary.md':Path('../a4-lead/FINAL_SUMMARY.md'),
           'lead_ld_diag.jsonl':Path('../a4-lead/logs/ld_d2_3_amp5_N290.diag.jsonl')}
    hashes={}
    for name,path in files.items():
        raw=path.read_bytes();hashes[name]=sha256(raw).hexdigest();(root/'sources'/name).write_bytes(raw)
    source=Path('research/53_stream_precision/verification/selected_packed_coefficients.json')
    raw=read_evidence_bytes(source);hashes[str(source)]=sha256(raw).hexdigest();s=json.loads(raw)
    rows=[];ln10=arb(10).log();zero_logs={}
    for field in ('f','g'):
        for ns,cols in s[field].items():
            maxrel=arb(0);location=None;record=None;zero_nonzero=[]
            for q,col in enumerate(cols):
                norm=arb(0)
                for i,packed in enumerate(col):
                    mid,rad=unpack(packed);norm+=abs(arb(mid,rad))
                    if mid==0:
                        if rad!=0:zero_nonzero.append([q,i])
                    else:
                        rel=rad/abs(mid)
                        if rel>maxrel:maxrel,location,record=rel,[q,i],packed
                if q==0:zero_logs[field,int(ns)]=norm.log()/ln10
            rows.append(dict(field=field,n=int(ns),max_individual_relative_radius=txt(maxrel),location=location,
                             exact_packed_record=record,below_1e_70=bool(maxrel<arb('1e-70')),uncertain_zero_entries=zero_nonzero))
    intervals=[]
    for older,newer in ((140,160),(160,180),(179,180)):
        inc=(zero_logs['f',newer]-zero_logs['f',older])/(newer-older)
        intervals.append(dict(older=older,newer=newer,mean_log10_c0_increment=txt(inc),below_claimed_lower_endpoint=bool(inc<arb('-.7030'))))
    data={r['n']:r for line in (root/'sources/lead_ld_diag.jsonl').read_text().splitlines() if (r:=json.loads(line))['n']>=2}
    loga=math.log10(5)
    windows={w:[(n,(data[n]['lcol'][0]-data[n-w]['lcol'][0])/w-loga) for n in range(180,291) if n-w in data and n in data] for w in (1,20)}
    floats={str(w):{'minimum':min(vals,key=lambda x:x[1]),'maximum':max(vals,key=lambda x:x[1]),'outside_count':sum(not(-.7030<=v<=-.7020) for _,v in vals),'count':len(vals),'selected':[x for x in vals if x[0] in (180,200,220,240,260,280,290)]} for w,vals in windows.items()}
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),source_hashes=hashes,retained_ball_checks=rows,exact_interval_windows=intervals,lead_float_windows=floats,actual_elapsed_s=time.monotonic()-start)
    (root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
    code=Path(__file__).read_bytes();(root/'sources/report_v6_audit.py.txt').write_bytes(code)
    print(json.dumps(dict(exact_windows=intervals,lead_float_windows=floats),indent=2))

if __name__=='__main__':main()
