"""Sequential, idle-priority Cartesian domain/interpolant diagnostics."""
import json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
cases=[
 ('fft_g2048_L4_C3_k7.json',['--grid','2048','--radius','4','--cutoff','3']),
 ('fft_g4096_L16_C12_k7.json',['--grid','4096','--radius','16','--cutoff','12']),
 ('fft_g2048_L8_C6_k5.json',['--grid','2048','--radius','8','--cutoff','6','--degree','5']),
 ('fft_g2048_L8_C6_k9.json',['--grid','2048','--radius','8','--cutoff','6','--degree','9']),
 ('fft_g2048_L8_C6_v01_k7.json',['--grid','2048','--radius','8','--cutoff','6','--source',str(HERE.parent/'coercivity_residual/residual_modal_v01.float.json')]),
]
for filename,args in cases:
    out=HERE/filename
    if out.exists():continue
    print('START',filename,flush=True)
    command=['chrt','--idle','0','env','OPENBLAS_NUM_THREADS=1','OMP_NUM_THREADS=1',sys.executable,'-B',str(HERE/'fft_pairing.py'),*args,'--out',str(out)]
    with (HERE/(filename+'.log')).open('w')as stream:subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,check=True,cwd=HERE)
    result=json.loads(out.read_text());print('DONE',filename,{k:result[k]for k in ['Q','D_cutoff','h_edge_max','D_high_frequency_fraction','elapsed_seconds']},flush=True)
