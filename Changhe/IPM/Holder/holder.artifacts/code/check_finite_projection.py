"""Independent vectorized distance and clamp checks, diagnostics only."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json
from finite_projection_diagnostic import amplitude

def witness(z,alpha,a=1.):
    flip=np.where(z[:,0]<0,-1.,1.);p=z*flip[:,None]
    X=p[:,0];Y=p[:,1]
    vertical=np.hypot(X-.5,Y-np.clip(Y,-a,a))
    distances=[vertical]
    for side in [-1.,1.]:
        v=np.column_stack([X-.5,Y-side*a]);direction=np.array([.5,side*np.sqrt(3)/2])
        projected=np.maximum(v@direction,0)
        distances.append(np.linalg.norm(v-projected[:,None]*direction,axis=1))
    dist=np.minimum.reduce(distances)
    signed=dist*np.sign(X-.5-np.maximum(abs(Y)-a,0)/np.sqrt(3))
    radius=np.hypot(signed,Y)
    S=np.divide(2*signed*Y,radius,out=np.zeros_like(radius),where=radius>0)
    F=-.5+.5*np.minimum(radius,a/6)**alpha+.5*np.sign(S)*abs(S)**alpha
    h=.5*(2*X)**alpha
    return flip*np.clip(F,-h,h)

def main():
    rng=np.random.default_rng(971284)
    n=250000
    centers=np.array([[0,0],[.5,0],[-.5,0],[.5,1],[.5,-1],[-.5,1],[-.5,-1]])
    p=centers[rng.integers(0,len(centers),n)]+rng.normal(size=(n,2))*10**rng.uniform(-8,4,(n,1))
    q=p+rng.normal(size=(n,2))*10**rng.uniform(-9,4,(n,1))
    q[n//2:]=centers[rng.integers(0,len(centers),n-n//2)]+rng.normal(size=(n-n//2,2))*10**rng.uniform(-8,4,(n-n//2,1))
    distances=np.linalg.norm(p-q,axis=1);valid=distances>0
    c=json.loads(Path('data/profile_constant_certificate.json').read_text());rows=[]
    for text,alpha in [('1/20',.05),('1/10',.1),('1/5',.2),('1/4',.25)]:
        fp=witness(p,alpha);fq=witness(q,alpha)
        ratios=abs(fp[valid]-fq[valid])/distances[valid]**alpha
        K=float(next(r['safe_upper'] for r in c['rows'] if r['alpha']==text))
        Q=abs(p[:20000]);op=Q.copy();op[:,1]*=-1
        error=float(np.max(abs(witness(Q,alpha)-witness(op,alpha)-amplitude(Q[:,0],Q[:,1],alpha,1.,1/6))))
        assert np.all(np.isfinite(ratios)) and max(ratios)<=K+1e-7 and error<1e-10
        rows.append(dict(alpha=text,pairs=len(ratios),maximum_quotient=float(max(ratios)),proved_upper=K,odd_amplitude_max_error=error))
    Path('data/finite_projection_pair_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Random stress checks only. They are not the admissibility proof.',rows=rows),indent=2)+'\n')
    print(rows)
if __name__=='__main__':main()
