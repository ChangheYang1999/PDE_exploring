"""Float screening for unresolved angular polynomial directions."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,hashlib,time
BASE=Path(__file__).resolve().parents[1]
def run():
    start=time.monotonic();rows=[]
    for M in [9,59,69]:
        K=2*M+2
        for N in [96,128,140,160,192,256]:
            z,w=np.polynomial.legendre.leggauss(N)
            for rule in ['gauss','midpoint']:
                if rule=='gauss':theta=(z+1)*np.pi/4;weights=w*np.pi/4
                else:theta=(np.arange(N)+.5)*np.pi/(2*N);weights=np.full(N,np.pi/(2*N))
                for space in ['density','quotient']:
                    k=np.arange(K)[:,None]
                    if space=='density':B=np.sqrt(4/np.pi)*np.sin((2*k+1)*theta)
                    else:B=np.sqrt(4/np.pi)*np.cos(2*k*theta);B[0]/=np.sqrt(2)
                    G=(B*weights)@B.T;ev=np.linalg.eigvalsh(G)
                    err=np.abs(G-np.eye(K));i,j=np.unravel_index(np.argmax(err),err.shape)
                    rows.append({'M':M,'rule':rule,'order':N,'space':space,'dimension':K,
                                 'lambda_min':float(ev[0]),'lambda_max':float(ev[-1]),
                                 'worst_relative_energy_error':float(max(abs(ev[0]-1),abs(ev[-1]-1))),
                                 'largest_entry_error':float(err[i,j]),'worst_entry_indices':[int(i),int(j)]})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'FLOAT worst-case screening',
         'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start,'rows':rows}
    (BASE/'verification/gram.json').write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:
        if row['M'] in [59,69] and row['order'] in [128,160,192] and row['space']=='density':print(row,flush=True)
if __name__=='__main__':run()
