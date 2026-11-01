"""Finite dimensionality diagnostics for normalized coefficient vectors.

Read exact dyadic midpoints directly from a numerical checkpoint. These are
floating-point diagnostics, not interval certificates for the infinite series.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, pickle, math
import numpy as np


def normalize(a):
    numbers=[(int(t[0]),int(t[1])) for t in a]
    exponent=max((abs(m).bit_length()+e for m,e in numbers if m),default=0)
    v=[]
    for m,e in numbers:
        if not m:
            v.append(0.);continue
        shift=max(abs(m).bit_length()-53,0)
        trunc=(abs(m)>>shift)*(-1 if m<0 else 1)
        v.append(math.ldexp(float(trunc),e+shift-exponent))
    v=np.asarray(v); v/=np.linalg.norm(v)
    return v


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',default='../a4-num/ckpt/sqrt5_sin1_p1024.pkl');ap.add_argument('--tag',default='sqrt5_sin1');args=ap.parse_args()
    path=Path(args.source);blob=path.read_bytes();data=pickle.loads(blob)
    assert data['ring']=='arb'
    N=max(data['f']); width=max(len(a) for a in data['f'].values())
    raw={n:normalize(a) for n,a in data['f'].items() if n>=max(1,N-180)}
    vectors={n:np.pad(v,(0,width-len(v))) for n,v in raw.items()}
    end=N; start=max(min(vectors),N-127)
    matrix=np.vstack([vectors[n] for n in range(start,end+1)])
    eig=np.linalg.eigvalsh(matrix@matrix.T)[::-1]
    anchor=max(min(vectors),N-128)
    v0,v1=vectors[anchor],vectors[anchor+1]
    basis=np.stack([v0,v1],axis=1); basis=np.linalg.qr(basis)[0]
    c=float(v0@v1)
    lags=[]
    for lag in [1,2,3,4,8,16,32,64,128]:
        if anchor+lag not in vectors:continue
        v=vectors[anchor+lag]
        projection=basis@(basis.T@v)
        lags.append(dict(lag=lag,actual_correlation=float(v0@v),fixed_rotation_cosine=math.cos(lag*math.acos(max(-1,min(1,c)))),distance_from_initial_two_plane=float(np.linalg.norm(v-projection))))
    defects=[]
    for n in [anchor,N-2]:
        v,w,x=vectors[n],vectors[n+1],vectors[n+2]
        corr=float(v@w)
        defects.append(dict(n=n,corr1=corr,corr2=float(v@x),cos2phi=2*corr*corr-1,
                            rotation_recurrence_defect=float(np.linalg.norm(x-2*corr*w+v))))
    target=Path('research/23_correlation_audit');sourcecopy=target/'sources'/(args.tag+'_selected_midpoints.json')
    retained={str(n):data['f'][n] for n in range(anchor,N+1)}
    sourcecopy.write_text(json.dumps(retained)+'\n')
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),source=str(path),source_sha256=sha256(blob).hexdigest(),
             source_selected_midpoints=str(sourcecopy),source_format='Arb dyadic midpoint triples; radii unused in this diagnostic',
             completed_N=N,anchor=anchor,block_start=start,block_end=end,
             eigenvalues_top10=eig[:10].tolist(),fraction_energy_outside_best_two_plane=float(eig[2:].sum()/eig.sum()),
             lags=lags,local_rotation_defects=defects,
             scope='Finite float diagnostics. No singularity exclusion or infinite-dimensional limiting assertion is certified.')
    (target/'verification'/(args.tag+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['source_selected_midpoints','source_sha256']},indent=2),flush=True)

if __name__=='__main__':main()
