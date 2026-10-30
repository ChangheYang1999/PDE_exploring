"""Recompute complementary parity blocks from rho-gradient pairings."""
from pathlib import Path
from hashlib import sha256
from math import factorial, comb
from functools import lru_cache
from datetime import datetime, timezone
import json, sys, time
from flint import fmpq as Q, fmpq_mat, arb, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/parity_angular_audit'
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial, pshift, ar

def digest(p): return sha256(p.read_bytes()).hexdigest()
def clean(p): return {k:v for k,v in p.items() if v}
def add(*polys):
    out={}
    for poly in polys:
        for key,val in poly.items(): out[key]=out.get(key,Q(0))+val
    return clean(out)
def scale(poly,v): return clean({k:x*v for k,x in poly.items()})
def product(a,b):
    out={}
    for (i,j,p),v in a.items():
        for (u,w,q),z in b.items():
            key=(i+u,j+w,p+q);out[key]=out.get(key,Q(0))+v*z
    return clean(out)
def derivative(poly,axis):
    out={}
    for (i,j,p),v in poly.items():
        degree=(i,j)[axis]
        if degree:
            key=(i-1,j,p) if axis==0 else (i,j-1,p)
            out[key]=out.get(key,Q(0))+degree*v
        key=(i+1,j,p+1) if axis==0 else (i,j+1,p+1)
        out[key]=out.get(key,Q(0))-2*p*v
    return clean(out)
def radial_fn(n):
    return {Q(2*n-2*k+1,2):Q((-1)**(n+k)*factorial(n)*factorial(2*n-2*k),2**n*factorial(k)*factorial(n-k)*factorial(n-2*k)) for k in range(n//2+1)}
def harmonic(n,m,kind):
    radial=radial_fn(n)
    for _ in range(m):radial={p+1:-p*v for p,v in radial.items()}
    out={}
    parity=0 if kind=='cos' else 1
    for k in range(parity,m+1,2):
        weight=2**m*comb(m,k)*(-1)**((k-parity)//2)
        for p,v in radial.items():out[m-k,k,p]=weight*v
    return out
@lru_cache(None)
def angular_monomial(i,j):
    if i%2 or j%2:return Q(0)
    a,b=i//2,j//2
    return Q(2*factorial(i)*factorial(j),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
@lru_cache(None)
def angular(kind,n,i,j):
    if n>i+j:return Q(0)
    parity=0 if kind=='b' else 1
    return sum(((-1)**((k-parity)//2)*comb(n,k)*angular_monomial(i+n-k,j+k) for k in range(parity,n+1,2)),Q(0))
def main():
    start=time.monotonic();ctx.prec=1024
    N,M=map(int,sys.argv[1:3]);name='C1-N1-008-d2w-j7-x3bal'
    target=BASE/f'verification/candidate008_n{N}_m{M}.json'
    assert not target.exists(),target
    peerfile=BASE/f'source/T4_008_n{N}_m{M}.json'
    peer=json.loads(peerfile.read_text());assert (peer['N'],peer['M'])==(N,M)
    canonical=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
    energy=ROOT/f'research/background_sobolev/verification/{name}.json'
    maps={f'parity_hs_budget/data/{name}_canonical.json':canonical,
          f'parity_hs_budget/data/{name}_HS.json':ROOT/f'research/candidate_audits/peer_review/T4_008/background_norm_reproduction/verification/{name}_reproduction.json',
          'weak_probe_audit/code/reproduce.py':ROOT/'research/parity_budget_audit/source/T4_fields.py',
          'parity_hs_angular/code/check.py':BASE/'source/T4_check.py',
          'parity_hs_angular/PROOF.md':BASE/'source/T4_PROOF.md',
          f'parity_hs_budget/verification/{name}_d12.json':ROOT/'research/parity_budget_audit/source/T4_008_d12.json'}
    for p,h in peer['inputs'].items():assert digest(maps[p])==h,(p,digest(maps[p]),h)
    model=Radial(canonical)
    gradients={kind:{} for kind in ('a','b')}
    for kind,field in (('a',model.rx),('b',model.ry)):
        for (j,n),P in field.items():
            assert n%2==0
            gradients[kind].setdefault(n,[]).append((j,pshift(P,2)))
    @lru_cache(None)
    def radial_moment(kind,n,d,p):
        out=Q(0)
        for j,P in gradients[kind].get(n,[]):
            q=p+(j+1)*model.delta/2-d-1;assert q>0
            bv=Q(1)/q
            for k in range(1,d+1):bv*=Q(k)/(q+k)
            for l,v in enumerate(P):
                out+=v*bv
                bv*=Q(d+l+1)/(q+d+l+1)
        return out
    @lru_cache(None)
    def moment(kind,i,j,p):
        assert (i+j)%2==0
        d=(i+j)//2
        return sum((angular(kind,n,i,j)*radial_moment(kind,n,d,p)/2 for n in gradients[kind] if n<=i+j and angular(kind,n,i,j)),Q(0))
    def integral(kind,poly):return sum((v*moment(kind,*key) for key,v in poly.items()),Q(0))
    blocks={p:[] for p in ('++','-+','--')}
    for m in range(M+1):
        for kind in (['cos','sin'] if m>0 and m%2==0 else ['cos']):
            parity='--' if kind=='sin' else '-+' if m%2 else '++'
            for n in range(N):
                f=harmonic(n,m,kind);nxt=harmonic(n+1,m,kind)
                fxx=derivative(derivative(f,0),0)
                h=scale(add(fxx,derivative(derivative(f,1),1)),-1)
                blocks[parity].append({'label':[kind,m,n],'h':h,'u1':scale(derivative(derivative(f,0),1),-1),'u2':fxx,'v1':scale(derivative(nxt,0),-1),'v2':scale(derivative(nxt,1),-1)})
    reports={};total=Q(0);entries=0
    for parity,tests in blocks.items():
        d=len(tests)
        if not d:continue
        old=peer['blocks'][parity];assert old['labels']==[t['label'] for t in tests]
        G=[[Q(0) for _ in tests] for _ in tests];B=[[Q(0) for _ in tests] for _ in tests]
        for i,ti in enumerate(tests):
            for j in range(i+1):
                tj=tests[j]
                ki,mi,ni=ti['label'];kj,mj,nj=tj['label']
                g=Q(0) if (ki,mi)!=(kj,mj) else Q((2 if mi==0 else 1)*(-1)**(ni+nj)*factorial(2*mi+ni+nj+3),2**(2*mi+ni+nj+4))
                A=scale(add(product(ti['h'],tj['u1']),product(tj['h'],ti['u1']),scale(product(ti['v1'],tj['v2']),-1),scale(product(ti['v2'],tj['v1']),-1)),Q(1,2))
                D=add(scale(add(product(ti['h'],tj['u2']),product(tj['h'],ti['u2'])),Q(1,2)),product(ti['v1'],tj['v1']))
                b=integral('a',A)+integral('b',D)
                assert g==Q(old['G_over_pi'][i][j])==Q(old['G_over_pi'][j][i]),('G',parity,i,j)
                assert b==Q(old['B_over_pi'][i][j])==Q(old['B_over_pi'][j][i]),('B',parity,i,j)
                G[i][j]=G[j][i]=g;B[i][j]=B[j][i]=b;entries+=2
            print('checked',parity,i+1,'/',d,'seconds',time.monotonic()-start,flush=True)
        L=[[Q(i==j) for j in range(d)] for i in range(d)];pivots=[]
        for i in range(d):
            p=G[i][i]-sum((L[i][k]**2*pivots[k] for k in range(i)),Q(0));assert p>0 and p==Q(old['positive_LDL_pivots'][i]);pivots.append(p)
            for j in range(i+1,d):L[j][i]=(G[j][i]-sum((L[j][k]*L[i][k]*pivots[k] for k in range(i)),Q(0)))/p
        inverse_product=fmpq_mat(G).solve(fmpq_mat(B))
        T=sum((inverse_product[i,j]*inverse_product[j,i] for i in range(d) for j in range(d)),Q(0))
        assert T>=0 and T==Q(old['captured_exact']);total+=T
        assert ar(T).overlaps(arb(old['captured']))
        reports[parity]={'dimension':d,'labels':[t['label'] for t in tests],'all_G_B_entries_equal':True,'all_LDL_pivots_positive_and_equal':True,'exact_trace_equal':True,'trace':ar(T).str(85)}
        print('block',parity,'trace',ar(T).str(25),'seconds',time.monotonic()-start,flush=True)
    norms=json.loads(energy.read_text())['norms'];Ex=Q(norms['D_rho_x']['unweighted_rational_sum']);Ey=Q(norms['D_rho_y']['unweighted_rational_sum'])
    kappa2=((arb(2).log()-Q(1,2))*ar(Ex)+(3*arb(2).log()-2)*ar(Ey))/32
    assert total==Q(peer['total_captured_exact']) and kappa2>ar(total)
    bound=(kappa2-ar(total)).sqrt();budget=ar(model.c-1)-bound
    values={'total_captured':ar(total),'full_kappa':kappa2.sqrt(),'remaining_S1_HS_upper':bound,'theta_budget_for_beta2':budget}
    assert all(v.overlaps(arb(peer[k])) for k,v in values.items())
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'N':N,'M':M,'precision_bits':ctx.prec,'blocks':reports,'lower_triangle_entries_checked':entries,**{k:v.str(85) for k,v in values.items()},'all_peer_scalar_balls_overlap':True,'code_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),'inputs':{str(p.relative_to(ROOT)):digest(p) for p in [canonical,energy,peerfile,*maps.values(),ROOT/'research/radial_fourier/code/radial.py']},'elapsed_seconds':time.monotonic()-start,'status':'Finite arithmetic and complementary parity compression CONFIRMED. Low-generator, theta, high inverse and nonlinear closure remain separate.'}
    target.write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',N,M,bound.str(30),budget.str(30),out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
