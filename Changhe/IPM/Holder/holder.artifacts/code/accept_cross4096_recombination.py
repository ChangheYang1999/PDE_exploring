"""Exact endpoint substitution and independent two-precision cross recombination."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import argparse, hashlib, json, re
R=Path(__file__).resolve().parents[1]
B=R/'05_team_audit/cross4096'; O=B/'recombination'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def up(x): return Q(str(x.upper().fmpq()))
def low(x): return Q(str(x.lower().fmpq()))
def ends(s):
    if not s.startswith('['): return Q(s),Q(s)
    m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',s); assert m,s
    c,r=map(Q,m.groups()); assert r>=0; return c-r,c+r

def ceil10(x):
    k=-((-x*10**10).__floor__()); return f'{k//10**10}.{k%10**10:010d}'

def phase_calc(a,U,prec):
    ctx.prec=prec; A=arb(a); p=arb.pi(); d=p/32; c=d.cos(); s=d.sin(); cl=low(c)
    if prec==384:
        near=arb(2)**(1-A)*((A+2)/2).gamma()/(2*p.sqrt()*((A+3)/2).gamma())/A+arb(1)/2
    else:
        near=arb(2)**(-A)*((A+2)/2).gamma()/(p.sqrt()*((A+3)/2).gamma()*A)+arb(1)/2
    H=[]
    for u,v in zip(U,U[1:]):
        if v<=u*cl: h=u
        elif u<=v*cl: h=v
        else:
            uu,vv=arb(str(u)),arb(str(v))
            amp=(uu*uu+vv*vv-2*uu*vv*c).sqrt()/s if prec==384 else (uu*uu+((vv-uu*c)/s)**2).sqrt()
            h=min(up(amp),up(arb(str(max(u,v)))/(d/2).cos()))
        H.append(h)
    return up(near),H,up(near+arb(str(max(U)))/(d/2).cos())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);args=ap.parse_args(); hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(R); hashes[str(p.relative_to(R))]=sha(p)
    def accepted(p,v):
        z=load(p); assert z['verdict']=='CONFIRMED' and z['ledger']==v;bind(p)
        for name,h in z['sha256'].items(): assert sha(R/name)==h,name;bind(R/name)
        return z
    accepted(R/'08_improved_upper_bounds/phase_interpolation/verification/accepted.json','V177')
    v168=accepted(R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/accepted.json','V168')
    v179=accepted(R/'05_team_audit/d36_recombination/verification/accepted.json','V179')
    diag=load(B/'verification/independent_diagnostic.json')
    for name,h in diag['sha256'].items():assert sha(R/name)==h,name;bind(R/name)
    new=load(B/'source/cross_disk_certificate_4096.json');old=load(R/'data/cross_disk_certificate.json')
    assert new['source_hashes']==old['source_hashes']
    assert new['cells_per_axis']==4096 and new['precision_bits']==160 and new['phase_intervals']==16
    for name,h in new['source_hashes'].items():assert sha(B/'source'/name)==sha(R/name)==h;bind(B/'source'/name)
    assert [r['alpha'] for r in new['rows']]==['1/5','3/10','1/2','3/4','9/10','99/100']
    X0={r['alpha']:list(map(lambda s:ends(s)[1],r['cross_phase_intervals'])) for r in old['rows']}
    X1={r['alpha']:list(map(lambda s:ends(s)[1],r['cross_phase_intervals'])) for r in new['rows']}
    for r in diag['rows']:
        assert r['all_34_comparisons_inside'] and r['all_new_uppers_below_old']
        assert list(map(Q,r['upper_endpoints']))==X1[r['alpha']]
        for j,s in enumerate(next(z for z in new['rows'] if z['alpha']==r['alpha'])['cross_phase_intervals']):
            l,h=ends(s)
            assert all(l<Q(str(r[k][j]))<h for k in ['cartesian_gauss_256','cartesian_gauss_512'])
    midpath=R/'data/middle_circle_certificate_n512.json';farpath=R/'data/far_circle_certificate_fine.json'
    W={r['alpha']:[ends(s)[1] for s in r['middle_phase_intervals']] for r in load(midpath)['rows']}
    E={r['alpha']:[ends(s)[1] for s in r['far_phase_intervals']] for r in load(farpath)['rows']}
    auditpath=R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/independent_audit.json'
    va={r['alpha']:r for r in load(auditpath)['rows']}; vb={r['alpha']:r for r in v179['rows']}
    basepath=R/'05_team_audit/table37_lead/verification/independent_audit.json'
    gainpath=R/'08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification/independent_audit.json'
    bases={r['alpha']:r for r in load(basepath)['rows']}; gains={r['alpha']:r for r in load(gainpath)['rows']}
    submissions={}
    for f in ['d36x.json','v168x.json']:
        for r in load(O/'source'/f)['rows']:
            assert r['alpha'] not in submissions;submissions[r['alpha']]=r
    rows=[]
    for a,X in X1.items():
        assert len(X)==len(X0[a])==17 and all(x<y for x,y in zip(X,X0[a]))
        X=[min(x,y) for x,y in zip(X,X0[a])]
        if a in ['1/5','99/100']:
            r=vb[a];r0=bases[a];rg=gains[a]
            gs=list(map(Q,rg['accepted_gains']))
            assert gs==[max(Q(0),Q(x)-Q(y)) for x,y in zip(rg['old_source_lower'],rg['new_residual_upper'])]
            ws=[Q(z['upper'])-g for z,g in zip(r0['middle'],gs)]
            es=[min(Q(z['upper']),e) for z,e in zip(r0['far'],E[a])]
            U0=[w+x+e for w,x,e in zip(ws,X0[a],es)]
            assert U0==list(map(Q,r['phase_upper']))
            U=[w+x+e for w,x,e in zip(ws,X,es)]
            assert U==[u-x+y for u,x,y in zip(U0,X0[a],X)]
            previous=r['safe_upper_D']
        else:
            r=va[a];gs=[Q(z['accepted_gain']) for z in r['residual_checks']]
            assert len(gs)==17 and all(g>=0 for g in gs)
            U0=[w+x+e-g for w,x,e,g in zip(W[a],X0[a],E[a],gs)]
            DP=list(map(Q,r['D_phase_upper']));assert all(u<=d for u,d in zip(U0,DP))
            U=[w+x+e-g for w,x,e,g in zip(W[a],X,E[a],gs)]
            assert all(u<=d-x+y for u,d,x,y in zip(U,DP,X0[a],X))
            previous=next(z['safe_upper'] for z in load(R/'08_improved_upper_bounds/phase_interpolation/verification/accepted.json')['rows'] if z['alpha']==a and z['operator']=='D')
        assert len(U)==17 and all(u>=0 for u in U)
        sub=submissions[a]
        target=sub.get('phase_values',sub.get('phase_upper'));assert len(target)==17
        assert all(u<=Q(v) for u,v in zip(U,target))
        S,H,sec=phase_calc(a,U,384);S2,H2,sec2=phase_calc(a,U,768)
        assert S2<=S and all(x<=y for x,y in zip(H2,H)) and sec2<=sec
        total=S+max(H); safe=ceil10(total)
        assert S2+max(H2)<=total<=Q(safe)<total+Q(1,10**10)
        producer_interpolated = sub.get('pending_interpolated_D_upper', sub.get('interpolated_D_upper'))
        assert producer_interpolated is not None
        assert Q(safe)<=Q(producer_interpolated)<Q(previous)
        assert ceil10(sec)==sub['safe_upper_D']
        rows.append(dict(alpha=a,safe_upper_D=safe,previous_upper_D=previous,secant_upper_D=ceil10(sec),uniform_part=str(S),phase_upper=list(map(str,U)),interval_upper=list(map(str,H)),worst_node=max(range(17),key=lambda j:U[j]),worst_interval=max(range(16),key=lambda j:H[j]),producer_interpolated_upper_D=producer_interpolated))
    for p in [B/'verification/independent_diagnostic.json',O/'PROOF.md',midpath,farpath,auditpath,basepath,gainpath,Path(__file__)]:bind(p)
    for p in (O/'source').iterdir():
        if p.is_file():bind(p)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',precision_bits=[384,768],rows=rows,sha256=hashes,method='Audited unchanged interval source and completed producer sum; independent all-node Cartesian diagnostics; exact endpoint recombination with independent 384/768-bit interpolation',scope='No full independent4096-cell interval rerun; no strict-projection saving used')
    (O/'verification/accepted.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['time_utc'],args.ledger,'CONFIRMED')
    for r in rows:print(r['alpha'],r['safe_upper_D'])
if __name__=='__main__':main()
