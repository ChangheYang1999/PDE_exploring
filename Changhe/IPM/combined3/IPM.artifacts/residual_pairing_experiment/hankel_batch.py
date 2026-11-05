"""Sequential idle-priority FFTLog convergence and exterior diagnostics."""
import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
base=['--rmin','1e-8','--rmax','1e22','--kmin','1e-15','--bias','-1','--splits','1e-9,1e-7,1e-6,.0001,.01,1']
cases=[
 ('hankel_full_n16384_bm1_r22.json',['--nodes','16384','--extended']),
 ('hankel_full_n32768_bm1_r22.json',['--nodes','32768','--extended']),
 ('hankel_full_n65536_smooth_bm1_r22.json',['--nodes','65536','--extended']),
 ('hankel_full_n131072_bm1_r22.json',['--nodes','131072','--extended']),
 ('hankel_full_k5.json',['--nodes','65536','--extended','--degree','5']),
 ('hankel_full_k9.json',['--nodes','65536','--extended','--degree','9']),
 ('hankel_full_farstride2.json',['--nodes','65536','--extended','--far-stride','2']),
 ('hankel_full_kmax500.json',['--nodes','65536','--extended','--kmax','500']),
 ('hankel_full_kmax2000.json',['--nodes','65536','--extended','--kmax','2000']),
]
for C in [3,6,12,24,48,96,192,384,1000,10000,1e6]:
    cases.append((f'hankel_cut{C:g}_extent.json',['--nodes','32768','--extended','--cutoff',str(C),'--kmin','1e-8']))
for filename,args in cases:
    out=HERE/filename
    if out.exists():continue
    print('START',filename,flush=True)
    command=['chrt','--idle','0','env','OPENBLAS_NUM_THREADS=1','OMP_NUM_THREADS=1',sys.executable,'-B',str(HERE/'hankel_pairing.py'),*base,*args,'--out',str(out)]
    with (HERE/(filename+'.log')).open('w')as stream:subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,check=True,cwd=HERE)
    result=json.loads(out.read_text());print('DONE',filename,{k:result[k]for k in ['Q','D_with_kmin','fL2','best_gaussian_split','elapsed_seconds']},flush=True)
