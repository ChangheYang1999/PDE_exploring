"""Exact later-resonance audit for one high-harmonic leading profile."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, sys, time, traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from laurent_log_audit import L, Q, Poly, parse
ROOT=Path('research/197_high_harmonic_tuning')
DELTA=Q(4,9);CMINUS=Q(4,5)
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def exponent(n):return 1-n*DELTA
def coefficient(a,m):
    assert len(a.a)<=1
    return 2*a.a[0][a.M+m] if a.a and a.M+m>=0 else Q(0)
def poisson(a):
    h=a.X();P=a.q+1;out=[]
    for i,x in enumerate(h.a[0].coeffs() if h.a else []):
        m=i-h.M;den=m*m-P*P
        if not den:
            assert not x,('nonzero resonant forcing',str(P),m,str(x))
            out.append(Q(0))
        else:out.append(x/den)
    g=L(P,h.M,[Poly(out)])
    assert (g.X().X().scale(-1)+g.Y().Y()-h).zero()
    return g
class Chain:
    def __init__(self,mode):
        self.mode=mode;self.F={};self.G={};self.FX={};self.FY={};self.GX={};self.GY={};self.pairs=0;self.poisson_checks=0
    def set_f(self,n,f):self.F[n]=f;self.FX[n]=f.X();self.FY[n]=f.Y()
    def set_g(self,n,g):self.G[n]=g;self.GX[n]=g.X();self.GY[n]=g.Y()
    def density(self,n):
        total=L(exponent(n),0,[])
        for i in range(1,n):
            j=n-i;total=total+self.GX[i]*self.FY[j]-self.GY[i]*self.FX[j];self.pairs+=1
        f=total.scale(1/((n-1)*CMINUS))
        assert (f.scale(-(n-1)*CMINUS)+total).zero()
        return f
    def stream(self,n):
        g=poisson(self.F[n]);self.poisson_checks+=1;self.set_g(n,g)
    def initialize(self):
        self.set_f(1,parse(exponent(1),{str(self.mode):['1']}));self.stream(1)
        for n in range(2,10):self.set_f(n,self.density(n));self.stream(n)
        assert coefficient(self.F[9],1)==0
    def response(self,k):
        n=9*k;e=parse(exponent(n)+1,{str(4*k-2):['1']});EX=e.X();EY=e.Y();U={};UX={};UY={};V={};VX={};VY={}
        for r in range(1,10):
            total=EX*self.FY[r]-EY*self.FX[r]
            for s in range(1,r):
                j=r-s
                total=total+VX[s]*self.FY[j]-VY[s]*self.FX[j]+self.GX[j]*UY[s]-self.GY[j]*UX[s]
            U[r]=total.scale(1/((n+r-1)*CMINUS));UX[r]=U[r].X();UY[r]=U[r].Y()
            if r<9:V[r]=poisson(U[r]);VX[r]=V[r].X();VY[r]=V[r].Y()
        return coefficient(U[9],4*k+1),U
    def block(self,k):
        n=9*k;provisional={}
        for r in range(1,10):
            m=n+r;f=self.density(m);self.set_f(m,f);provisional[r]=f
            if r<9:self.stream(m)
        R=coefficient(self.F[n+9],4*k+1);sigma,U=self.response(k)
        support={self.mode*s+t for s in range(-9,10,2) for t in range(-8,9,2)}
        support_allows=3 in support or 8*k-1 in support
        if not support_allows:assert not sigma
        row=dict(k=k,free_stream_order=n,next_resonance=n+9,constant_exact=str(R),response_exact=str(sigma),response_nonzero=bool(sigma),support_allows_response=support_allows)
        if sigma:
            H=-R/sigma;self.set_g(n,self.G[n]+parse(exponent(n)+1,{str(4*k-2):[str(H)]}))
            for r in range(1,10):
                m=n+r;f=self.density(m);assert (f-provisional[r]-U[r].scale(H)).zero(),('affine replay',m)
                self.set_f(m,f);self.stream(m)
            assert coefficient(self.F[n+9],4*k+1)==0
            row.update(tuned_harmonic_exact=str(H),corrected_affine_checks=9,corrected_compatibility_exact_zero=True)
            if k==1:
                previous=Path('research/36_free_multipole_compatibility/verification')/f'sin{self.mode}.json';old=json.loads(previous.read_text())
                assert sigma==Q(old['slope_exact']) and H==Q(old['tuned_beta_exact'])
                row.update(previous_first_tuning_matches=True,previous_source=str(previous),previous_source_sha256=sha256(previous.read_bytes()).hexdigest())
        else:row.update(obstructed_for_every_current_harmonic=bool(R))
        return row

def main(args):
    start=time.monotonic();chain=Chain(args.mode);chain.initialize();rows=[]
    for k in range(1,args.blocks+1):
        row=chain.block(k);row.update(checked_at_utc=stamp(),actual_elapsed_s=time.monotonic()-start)
        (ROOT/'verification'/f'sin{args.mode}_block{k}.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
        print(json.dumps({key:value for key,value in row.items() if not key.endswith('_exact')}),flush=True)
        if row.get('obstructed_for_every_current_harmonic') or not row['response_nonzero']:break
    result=dict(checked_at_utc=stamp(),leading_mode=args.mode,delta='4/9',c='9/5',complete=True,rows=rows,ordered_products=chain.pairs,poisson_identity_checks=chain.poisson_checks,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification'/f'sin{args.mode}_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['high_harmonic_tuning.py','laurent_log_audit.py']:(ROOT/'sources'/name).write_bytes((Path('code')/name).read_bytes())
    print(json.dumps(dict(complete=True,mode=args.mode,blocks=len(rows),obstruction=rows[-1].get('obstructed_for_every_current_harmonic'),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',type=int,default=13);ap.add_argument('--blocks',type=int,default=3);args=ap.parse_args()
    try:main(args)
    except Exception as e:
        failure=dict(checked_at_utc=stamp(),mode=args.mode,error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
        (ROOT/'verification'/f'sin{args.mode}_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
