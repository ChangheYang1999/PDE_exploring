"""Audit signed S1 compression using independent gradient pairings."""
from pathlib import Path
from hashlib import sha256
from math import factorial
from functools import lru_cache
from datetime import datetime,timezone
import json,sys,time,importlib.util
from flint import fmpq as Q,fmpq_mat,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/signed_compression_audit'
helper=ROOT/'research/parity_angular_audit/code/check.py'
spec=importlib.util.spec_from_file_location('n4_angular_helper',helper)
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

def H(p):return sha256(p.read_bytes()).hexdigest()
def ldl(mat):
    size=len(mat);L=[[Q(i==j) for j in range(size)] for i in range(size)];D=[]
    for i in range(size):
        p=mat[i][i]-sum((L[i][k]**2*D[k] for k in range(i)),Q(0));assert p>0,('not positive',i)
        D.append(p)
        for j in range(i+1,size):L[j][i]=(mat[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),Q(0)))/p
    return D

def direct_ball_ldl(mat):
    size=len(mat);L=[[arb(i==j) for j in range(size)] for i in range(size)];D=[]
    A=[[lib.ar(x) for x in row] for row in mat]
    for i in range(size):
        p=A[i][i]-sum((L[i][k]**2*D[k] for k in range(i)),arb(0))
        assert p>0,('direct ball LDL not positive',i,p.str(25))
        D.append(p)
        for j in range(i+1,size):
            L[j][i]=(A[j][i]-sum((L[j][k]*L[i][k]*D[k] for k in range(i)),arb(0)))/p
    return D

def main():
    start=time.monotonic();ctx.prec=2048;N,M=map(int,sys.argv[1:3]);name='C1-N1-008-d2w-j7-x3bal'
    peerfile=BASE/f'source/T4_008_n{N}_m{M}_ball.json';peer=json.loads(peerfile.read_text())
    dest=BASE/f'verification/candidate008_n{N}_m{M}.json';assert not dest.exists()
    assert peer['candidate']==name and (peer['N'],peer['M'])==(N,M)
    canonical=ROOT/f'research/candidate_audits/data/{name}/canonical.json'
    energy=ROOT/f'research/background_sobolev/verification/{name}.json'
    complement=ROOT/'research/parity_angular_audit/source/T4_008_n8_m6.json'
    reviewed=ROOT/'research/parity_angular_audit/verification/candidate008_n8_m6.json'
    cdata=json.loads(complement.read_text());cvalid=json.loads(reviewed.read_text())
    assert cvalid['inputs'][str(complement.relative_to(ROOT))]==H(complement)
    maps={f'parity_hs_budget/data/{name}_canonical.json':canonical,
          f'parity_hs_budget/data/{name}_HS.json':ROOT/f'research/candidate_audits/peer_review/T4_008/background_norm_reproduction/verification/{name}_reproduction.json',
          'weak_probe_audit/code/reproduce.py':ROOT/'research/parity_budget_audit/source/T4_fields.py',
          'signed_compression_budget/code/check_ball_ldl.py':BASE/'source/T4_check_ball_ldl.py',
          'signed_compression_budget/PROOF.md':BASE/'source/T4_PROOF.md',
          'signed_compression_budget/BALL_LDL.md':BASE/'source/T4_BALL_LDL.md',
          f'signed_compression_budget/verification/{name}_n{N}_m{M}_matrices.json':BASE/f'source/T4_008_n{N}_m{M}_matrices.json',
          f'parity_hs_angular/verification/{name}_n8_m6.json':complement}
    for p,digest in peer['inputs'].items():assert H(maps[p])==digest,(p,H(maps[p]),digest)
    checkpoint=json.loads((BASE/f'source/T4_008_n{N}_m{M}_matrices.json').read_text())
    assert checkpoint['blocks']==peer['blocks']
    assert checkpoint['canonical_sha256']==H(canonical)
    assert checkpoint['target_HS_exact']==peer['target_HS_exact']
    model=lib.Radial(canonical);gradients={k:{} for k in ('a','b')}
    for kind,field in [('a',model.rx),('b',model.ry)]:
        for (j,n),P in field.items():gradients[kind].setdefault(n,[]).append((j,lib.pshift(P,2)))
    @lru_cache(None)
    def radial(kind,n,d,p):
        total=Q(0)
        for j,P in gradients[kind].get(n,[]):
            q=p+(j+1)*model.delta/2-d-1;assert q>0
            beta=Q(1)/q
            for k in range(1,d+1):beta*=Q(k)/(q+k)
            for l,v in enumerate(P):total+=v*beta;beta*=Q(d+l+1)/(q+d+l+1)
        return total
    @lru_cache(None)
    def moment(kind,i,j,p):
        assert (i+j)%2==0
        return sum((lib.angular(kind,n,i,j)*radial(kind,n,(i+j)//2,p)/2 for n in gradients[kind] if n<=i+j and lib.angular(kind,n,i,j)),Q(0))
    def integral(kind,poly):return sum((v*moment(kind,*key) for key,v in poly.items()),Q(0))
    tests=[];labels=[]
    for m in range(1,M+1,2):
        for n in range(N):
            f=lib.harmonic(n,m,'sin');nextf=lib.harmonic(n+1,m,'sin')
            xx=lib.derivative(lib.derivative(f,0),0)
            tests.append({'h':lib.scale(lib.add(xx,lib.derivative(lib.derivative(f,1),1)),-1),'u1':lib.scale(lib.derivative(lib.derivative(f,0),1),-1),'u2':xx,'v1':lib.scale(lib.derivative(nextf,0),-1),'v2':lib.scale(lib.derivative(nextf,1),-1)})
            labels.append(['sin',m,n])
    old=peer['blocks']['+-'];assert old['labels']==labels;size=len(tests)
    G=[[Q(0) for _ in tests] for _ in tests];B=[[Q(0) for _ in tests] for _ in tests]
    for i,a in enumerate(tests):
        for j in range(i+1):
            b=tests[j];_,m,n=labels[i];_,mm,nn=labels[j]
            g=Q(0) if m!=mm else Q((-1)**(n+nn)*factorial(2*m+n+nn+3),2**(2*m+n+nn+4))
            A=lib.scale(lib.add(lib.product(a['h'],b['u1']),lib.product(b['h'],a['u1']),lib.scale(lib.product(a['v1'],b['v2']),-1),lib.scale(lib.product(a['v2'],b['v1']),-1)),Q(1,2))
            D=lib.add(lib.scale(lib.add(lib.product(a['h'],b['u2']),lib.product(b['h'],a['u2'])),Q(1,2)),lib.product(a['v1'],b['v1']))
            value=integral('a',A)+integral('b',D)
            assert g==Q(old['G_over_pi'][i][j])==Q(old['G_over_pi'][j][i])
            assert value==Q(old['B_over_pi'][i][j])==Q(old['B_over_pi'][j][i]),('B',i,j)
            G[i][j]=G[j][i]=g;B[i][j]=B[j][i]=value
        print('matched row',i+1,'/',size,'seconds',time.monotonic()-start,flush=True)
    pivots=ldl(G);assert pivots==list(map(Q,old['positive_LDL_pivots']))
    matrix=fmpq_mat(G).inv()*fmpq_mat(B)
    total=sum((matrix[i,j]*matrix[j,i] for i in range(size) for j in range(size)),Q(0))
    assert total==Q(old['captured_exact'])==Q(peer['target_HS_exact']) and total>=0
    q=Q(peer['certified_q']);assert q>=0
    positive=direct_ball_ldl([[q*G[i][j]-B[i][j] for j in range(size)] for i in range(size)])
    assert all(arb(x)>0 for x in peer['qI_minus_C_positive_ball_LDL_pivots'])
    subtract=total-q*q;assert subtract==Q(peer['target_subtracted_energy_exact'])
    norms=json.loads(energy.read_text())['norms'];Ex=Q(norms['D_rho_x']['unweighted_rational_sum']);Ey=Q(norms['D_rho_y']['unweighted_rational_sum'])
    kappa2=((arb(2).log()-Q(1,2))*lib.ar(Ex)+(3*arb(2).log()-2)*lib.ar(Ey))/32
    other=Q(cdata['total_captured_exact']);remaining=kappa2-lib.ar(other)-lib.ar(subtract);assert remaining>0
    bound=remaining.sqrt();budget=lib.ar(model.c-1)-bound
    values={'target_HS':lib.ar(total),'target_subtracted_energy':lib.ar(subtract),'complement_captured':lib.ar(other),'full_kappa':kappa2.sqrt(),'S1_signed_quadratic_upper':bound,'theta_budget_for_beta2':budget}
    assert all(v.overlaps(arb(peer[k])) for k,v in values.items())
    output={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'N':N,'M':M,'dimension':size,'precision_bits':ctx.prec,'all_G_B_entries_equal':True,'positive_Gram_LDL_pivots_equal':True,'direct_qG_minus_B_LDL_pivots':[v.str(85) for v in positive],'all_direct_LDL_pivots_positive':True,'exact_trace_equal':True,'certified_q':str(q),'all_scalar_balls_overlap':True,**{k:v.str(85) for k,v in values.items()},'inputs':{str(p.relative_to(ROOT)):H(p) for p in [peerfile,canonical,energy,complement,reviewed,*maps.values(),helper,BASE/'PROOF.md',BASE/'MATRIX_PROOF.md',Path(__file__)]},'elapsed_seconds':time.monotonic()-start,'status':'Signed finite matrix bound CONFIRMED; theta, generator and high-space hypotheses remain separate'}
    dest.write_text(json.dumps(output,indent=2)+'\n');print('DONE',bound.str(30),budget.str(30),output['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
