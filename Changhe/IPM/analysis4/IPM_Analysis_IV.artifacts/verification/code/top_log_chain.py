"""Symbolic maximal-log resonance chain at delta=2/3, sin(theta) input."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
import sympy as s
from laurent_log_audit import L,Q,Poly,parse


def low_modes(N=6):
    F,G,XF,YF,XG,YG={},{},{},{},{},{}
    for n in range(1,N+1):
        p=1-Q(2,3)*n
        non=L(p,0,[])
        for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
        F[n]=parse(p,{1:['1']}) if n==1 else non.scale(Q(1,2*(n-1)))
        XF[n],YF[n]=F[n].X(),F[n].Y()
        if n==N:break
        P=p+1; rhs=XF[n]; out=[]
        for idx,v in enumerate(rhs.a[0].coeffs()):
            m=idx-rhs.M; den=m*m-P*P
            assert den or not v
            out.append(v/den if den else Q(0))
        G[n]=L(P,rhs.M,[Poly(out)]);XG[n],YG[n]=G[n].X(),G[n].Y()
        assert (XG[n].X().scale(-1)+YG[n].Y()-XF[n]).zero()
    def sine(A):return {k:s.Rational(str(2*A.a[0][A.M+k])) for k in range(1,A.M+1) if A.a[0][A.M+k]}
    return {n:sine(v) for n,v in F.items()},{n:sine(v) for n,v in G.items()}


def symbolic_chain():
    k=s.symbols('k',integer=True,positive=True);m=2*k-2
    lowf,lowg=low_modes()
    d=s.Rational(2,3)
    f={};g={0:{0:s.Integer(1)}}
    def add(out,j,v):out[j]=out.get(j,0)+v
    def highg_lowf(gcols,fcols,Pi,pj):
        out={}
        for shift,b in gcols.items():
            K=m+shift
            for ell,a in fcols.items():
                add(out,shift+ell,b*a*(Pi*ell-pj*K)/2)
                add(out,shift-ell,b*a*(Pi*ell+pj*K)/2)
        return out
    def lowg_highf(gcols,fcols,Pi,pj):
        out={}
        for ell,b in gcols.items():
            for shift,a in fcols.items():
                K=m+shift
                add(out,shift+ell,b*a*(Pi*K-pj*ell)/2)
                add(out,shift-ell,b*a*(-Pi*K-pj*ell)/2)
        return out
    for r in range(1,4):
        n=3*k+r;out={}
        for i in range(r):
            # i=0,1,2 means stream at 3k+i, low density r-i.
            for j,v in highg_lowf(g[i],lowf[r-i],2-d*(3*k+i),1-d*(r-i)).items():add(out,j,v)
        for i in range(1,r):
            for j,v in lowg_highf(lowg[i],f[r-i],2-d*i,1-d*(3*k+r-i)).items():add(out,j,v)
        f[r]={j:s.factor(v/(2*(n-1))) for j,v in out.items() if s.cancel(v)!=0}
        if r<3:
            P=2-d*n;out={}
            for shift,a in f[r].items():
                add(out,shift+1,-a/(2*(m+shift+1+P)))
                add(out,shift-1,a/(2*(m+shift-1-P)))
            g[r]={j:s.factor(v) for j,v in out.items() if s.cancel(v)!=0}
    # The next resonant density channel is frequency 2k-1 = m+1.
    ratio=s.factor(-f[3][1]/(2*k))
    init=s.factor(-lowf[6][1]/2)
    return k,m,f,g,ratio,init,lowf,lowg


def main():
    start=time.monotonic();k,m,f,g,ratio,init,lowf,lowg=symbolic_chain()
    b3=s.factor(-init*(f[3][1]-f[3][-5]).subs(k,2)/4)
    print('b_2 =',init,'b_3 =',b3,flush=True)
    print('b_(k+1)/b_k =',ratio,flush=True)
    print('lim k * ratio =',s.limit(k*ratio,k,s.oo),flush=True)
    out=Path('research/44_maximal_log_chain/verification');out.mkdir(parents=True,exist_ok=True)
    data=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        parameter='delta=2/3,c=3',input='sin(theta)',
        normalized_density={str(r):{str(j):str(v) for j,v in cols.items()} for r,cols in f.items()},
        normalized_stream={str(r):{str(j):str(v) for j,v in cols.items()} for r,cols in g.items()},
        low_density={str(n):{str(j):str(v) for j,v in cols.items()} for n,cols in lowf.items()},
        low_stream={str(n):{str(j):str(v) for j,v in cols.items()} for n,cols in lowg.items()},
        b2=str(init),b3=str(b3),successive_ratio=str(ratio),lim_k_times_ratio=str(s.limit(k*ratio,k,s.oo)),
        valid_symbolic_offsets='k>=4 without frequency reflection; profiles reflected at k=2,3; scalar ratio valid k>=3',
        actual_elapsed_s=time.monotonic()-start)
    (out/'symbolic_chain.json').write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':main()
