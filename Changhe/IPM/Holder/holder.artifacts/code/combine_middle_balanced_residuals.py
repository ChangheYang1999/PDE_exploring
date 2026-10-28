"""Exact residual replacement in previously accepted C and D bounds."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json,hashlib,re
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
RAD=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement'
ctx.prec=320
ALPHAS=['3/10','1/2','3/4','9/10']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def pair(d):
    lo,hi=Q(d['lower']),Q(d['upper']);assert lo<=hi;return lo,hi
def ends(text):
    if not text.startswith('['):return Q(text),Q(text)
    m=re.fullmatch(r'\[\s*([^ ]+)\s*\+/-\s*([^ ]+)\s*\]',text);assert m,text
    c,r=map(Q,m.groups());assert r>=0;return c-r,c+r
def rec(x):return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(40,more=True))
def ceil10(q):
    k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'
def main():
    hashes={};replay=[];ref=None
    def bind(p):hashes[str(p.relative_to(ROOT))]=sha(p)
    oldlo={a:[Q(0)]*17 for a in ALPHAS};oldhi={a:[Q(0)]*17 for a in ALPHAS};newhi={a:[Q(0)]*17 for a in ALPHAS}
    for k in range(512):
        p=BASE/'verification/mass_replay'/f'row_{k:03d}.json';d=load(p);bind(p)
        assert d['row']==k and d['angles']==512 and d['radial_rows']==512 and d['phase_intervals']==16
        assert d['integer_unit']==2**44 and d['precision_bits']==160 and d['alphas']==ALPHAS
        if ref is None:ref=d['source_hashes']
        else:assert d['source_hashes']==ref
        for key,n in [('radial_left',k),('radial_right',k+1)]:
            l,u=pair(d[key]);exact=arb.pi()*n/1024
            assert l<=Q(str(exact.lower().fmpq()))<=Q(str(exact.upper().fmpq()))<=u
        assert len(d['phases'])==17
        for j,v in enumerate(d['phases']):
            assert v['phase']==j and len(v['masses'])==512
            assert all(type(x) is int for x in v['masses'])
            assert sum(v['masses'])==v['signed_integer_sum'] and sum(map(abs,v['masses']))==v['absolute_integer_sum']
            for a in ALPHAS:
                l,u=pair(v['old'][a]);new=Q(v['new'][a]['upper']);assert 0<=new<=u
                oldlo[a][j]+=l;oldhi[a][j]+=u;newhi[a][j]+=new
        replay.append(d)
    for name,h in ref.items():assert sha(ROOT/name)==h;bind(ROOT/name)
    midpath=ROOT/'data/middle_circle_certificate_n512.json';mid=load(midpath);bind(midpath)
    for name,h in mid['source_hashes'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    for name,h in mid['input_hashes'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    assert mid['angles_per_half']==512 and mid['radial_cells']==512 and mid['phase_intervals']==16
    rows={r['alpha']:r for r in mid['rows']};assert set(rows)==set(ALPHAS)
    dpath=ROOT/'data/middle_composite_upper_n512.json';ddata=load(dpath);bind(dpath)
    for name,h in ddata['input_sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    drows={r['alpha']:r for r in ddata['rows']}
    ac=RAD/'verification/accepted.json';approval=load(ac);bind(ac)
    assert approval['verdict']=='CONFIRMED' and approval['ledger']=='V161'
    for name,h in approval['sha256'].items():assert sha(ROOT/name)==h;bind(ROOT/name)
    cpath=RAD/'verification/independent_audit.json';cc=load(cpath);bind(cpath);crows={r['alpha']:r for r in cc['rows']}
    oldcpath=RAD.parent/'existing_certificates/verification/independent_audit.json';oc=load(oldcpath);bind(oldcpath)
    ocrows={r['alpha']:r for r in oc['rows']}
    factor=1/(arb.pi()/64).cos();results=[]
    for a in ALPHAS:
        residual=[];dphase=[];cphase=[];checks=[]
        for j in range(17):
            sl,su=ends(rows[a]['residual_intervals'][j])
            assert max(sl,oldlo[a][j])<=min(su,oldhi[a][j]),(a,j,'old residual replay mismatch')
            gain=sl-newhi[a][j]
            # If rounding obscures a tiny gain, retain the old bound for that phase.
            gain=max(Q(0),gain);residual.append(str(gain))
            dphase.append(ends(drows[a]['regular_plus_far_grid'][j])[1]-gain)
            cphase.append(Q(crows[a]['phase_upper'][j])-gain)
            checks.append(dict(phase=j,old_intervals_overlap=True,old_source_lower=str(sl),old_replay_lower=str(oldlo[a][j]),
                old_replay_upper=str(oldhi[a][j]),new_residual_upper=str(newhi[a][j]),accepted_gain=str(gain)))
        wd=max(range(17),key=lambda j:dphase[j]);wc=max(range(17),key=lambda j:cphase[j])
        D=arb(str(ends(drows[a]['near_D'])[1]))+factor*arb(str(dphase[wd]))
        C=arb(str(ocrows[a]['small_upper']))+factor*arb(str(cphase[wc]))
        sd=ceil10(Q(str(D.upper().fmpq())));sc=ceil10(Q(str(C.upper().fmpq())))
        assert Q(sd)<=Q(drows[a]['safe_upper_D']) and Q(sc)<=Q(crows[a]['safe_upper_C'])
        results.append(dict(alpha=a,safe_upper_C=sc,safe_upper_D=sd,upper_C=rec(C),upper_D=rec(D),
            old_upper_C=crows[a]['safe_upper_C'],old_upper_D=drows[a]['safe_upper_D'],worst_C_phase=wc,worst_D_phase=wd,
            C_phase_upper=list(map(str,cphase)),D_phase_upper=list(map(str,dphase)),residual_checks=checks))
        print(a,'C',sc,'D',sd,'phases',wc,wd,flush=True)
    bind(Path(__file__))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='NUMERICAL CHECKS PASS; separate analytic and final acceptance required',rows=results,sha256=hashes)
    (BASE/'verification/independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
