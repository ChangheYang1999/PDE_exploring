"""Independent exact audit of refitted potentials. No sibling code imported."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import factorial
import hashlib, json, sys
from flint import arb, ctx
ctx.prec=384
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'source_audit'))
sys.path.insert(0,str(BASE/'05_tails/verification'))
from recover_state import taylor_generator, derivative, polymul, polyadd, choose
from check_tail import density_stream, advection, add_sine

def aa(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)

def legendre_shift(n):
    # Three-term Legendre recurrence with argument 2t-1.
    if n==0:return [Q(1)]
    p0,p1=[Q(1)],[Q(-1),Q(2)]
    for k in range(1,n):
        x=[Q(0)]*(len(p1)+1)
        for i,v in enumerate(p1):x[i]-=(2*k+1)*v;x[i+1]+=2*(2*k+1)*v
        for i,v in enumerate(p0):x[i]-=k*v
        p0,p1=p1,[v/(k+1) for v in x]
    return p1

def canonical(d):
    out={}
    for g in d['generators']:
        j,m,a=g['j'],g['m'],Q(g['coef']);s=g['spec']
        if s[0]=='mono':p=[Q(1)];offset=s[1]
        else:
            assert s[0]=='leg'
            offset,n=s[1:];p=legendre_shift(n)
        for ell,v in enumerate(p):
            key=(j,m,m+offset+ell)
            out[key]=out.get(key,Q(0))+a*v
    return {k:v for k,v in out.items() if v}

def clean(d):return {k:v for k,v in d.items() if v}
def norm(d):return (arb.pi()*aa(sum((v*v for v in d.values()),Q(0))/4)).sqrt()
def encpoly(d):return {','.join(map(str,k)) if isinstance(k,tuple) else str(k):str(v) for k,v in sorted(d.items())}

def tail(A,c):
    gamma=1/c;delta=1-gamma;J=max(j for j,m,k in A)
    G={};P={};E={}
    for j in range(J+1):
        for q in range(2):
            pot={};pj=(3+gamma-j*delta)/2
            for (jj,m,k),a in A.items():
                if jj==j:pot[2*m]=pot.get(2*m,Q(0))+a*choose(pj-k,q)
            g,p=density_stream(clean(pot),2*pj-2*q)
            G[j,q]=clean(g);P[j,q]=clean(p)
    for h in range(2*J+2):
        for q in range(2):
            ex=gamma-h*delta-2*q
            e={n:(c*ex-1)*v for n,v in G.get((h,q),{}).items()}
            for i in range(J+1):
                j=h-1-i
                if j<0 or j>J:continue
                for u in range(q+1):
                    v=q-u
                    t=advection(P[i,u],G[j,v],gamma-i*delta-2*u+1,gamma-j*delta-2*v)
                    for n,a in t.items():add_sine(e,n,a)
            E[h,q]=clean(e)
    return G,P,E

def run(name):
    src=BASE/'08_refits/inputs'/f'{name}_exact.json'
    raw=src.read_bytes();d=json.loads(raw);A=canonical(d);c=Q(d['cl'])
    old=json.loads((BASE/'source_audit/state131_exact.json').read_text())
    assert c==Q(old['exact_parameters']['cl'])
    original={tuple(k):Q(v) for k,v in zip(old['canonical_order'],old['canonical_coefficients'])}
    G,P,E=tail(A,c);G0,P0,E0=tail(original,c)
    assert G[0,0]==G0[0,0]
    assert not E[0,0] and not E[1,0]
    # Center Taylor polynomial through degree 8, followed by independent products.
    chi={}
    for (j,m,k),a in A.items():
        if 2*k<=8:chi=polyadd(chi,taylor_generator(j,m,k,c,8),a)
    strain=derivative(chi,2,2).get((0,0),Q(0))
    assert strain==1-c
    rho=polyadd(derivative(chi,2,1),derivative(chi,0,3))
    rho={k:-v for k,v in rho.items()}
    u1={k:-v for k,v in derivative(chi,1,2).items()};u2=derivative(chi,2,1)
    a0=derivative(rho,0,1).get((0,0),Q(0));assert a0>0
    F=polyadd({k:(c*sum(k)-1)*v for k,v in rho.items()},polymul(u1,derivative(rho,1,0),5))
    F=polyadd(F,polymul(u2,derivative(rho,0,1),5));F=clean(F)
    assert F.get((0,1),Q(0))==0
    sectors=[]
    for (h,q),e in E.items():
        exponent=1/c-h*(1-1/c)-2*q
        if exponent<=-Q(5,2):continue
        sectors.append({'h':h,'q':q,'exponent':str(exponent),'zero':not bool(e),'max_harmonic':max(e,default=0),'quarter_norm':norm(e).str(55),'coefficients':encpoly(e)})
    sectors.sort(key=lambda s:Q(s['exponent']),reverse=True)
    serialization='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(A.items()))+'\n'
    dest={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'source_sha256':hashlib.sha256(raw).hexdigest(),'canonical_sha256':hashlib.sha256(serialization.encode()).hexdigest(),'input_generator_count':len(d['generators']),'canonical_term_count':len(A),'cl':str(c),'center_strain':str(strain),'a0':str(a0),'a0_arb':aa(a0).str(55),'leading_density_unchanged':True,'E00_zero':True,'E10_zero':True,'center_residual_through_degree5':encpoly(F),'residual_sectors':sectors,'canonical_order':[list(k) for k in sorted(A)],'canonical_coefficients':[str(A[k]) for k in sorted(A)],'scope':'Exact sector identities, center jets, and individual angular L2 norms only. No whole-plane residual norm or transferred coefficient certificate.'}
    (HERE/f'{name}_audit.json').write_text(json.dumps(dest,indent=2)+'\n')
    print(name,'exact checks PASS; generators',len(d['generators']),'a0',aa(a0).str(18),'source hash',dest['source_sha256'],flush=True)
    for s in sectors:print('sector',s['h'],s['q'],'zero',s['zero'],'norm',s['quarter_norm'],flush=True)
    print('cubic',[ (k,aa(v).str(18)) for k,v in F.items() if sum(k)==3],flush=True)

if __name__=='__main__':
    for n in sys.argv[1:] or ['n12_m4','n12_m5']:run(n)
