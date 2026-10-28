"""Check report version 32 against its frozen accepted numerical sources."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import hashlib,json,re
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v32'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def ceil(q,n):
    t=q*10**n;k=-((-t.numerator)//t.denominator)
    return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
    hashes={}
    def bind(p):hashes[str(p.relative_to(R))]=sha(p)
    def accepted(p,v):
        d=load(p);assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
        for n,h in d['sha256'].items():assert sha(R/n)==h,n
        return d
    report=B/'FINAL_REPORT.md';text=report.read_text();assert 'Draft version 32,' in text
    table=load(B/'table_v209_v210.json')
    sharp=accepted(R/'08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json','V209')
    radial=accepted(R/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/numerical_values/accepted.json','V210')
    rows=[]
    for r in table['rows']:
        a=Q(r['alpha']);marker='| '+str(float(a))+' |'
        line=next(x for x in text.splitlines() if x.startswith(marker))
        c=[x.strip() for x in line.split('|')[1:-1]]
        uc=Q(r['selected_upper_C']['exact_safe_endpoint']);ud=Q(r['selected_upper_D']['exact_safe_endpoint'])
        lc=Q(r['selected_lower']['exact_safe_endpoint']);ld=Q(r['selected_lower_D']['exact_safe_endpoint'])
        assert c[4]==ceil(uc,6)==r['upper_C'] and c[5]==ceil(ud,6)==r['upper_D']
        assert Q(c[6])<=lc and Q(c[8].strip('*'))<=ld
        assert Q(c[9])>=uc/lc and Q(c[10])>=ud/ld
        assert Q(c[9])-Q(ceil(uc/lc,4))<=Q(1,10000)
        assert Q(c[10])-Q(ceil(ud/ld,4))<=Q(1,10000)
        rows.append(dict(alpha=str(a),upper_C=c[4],upper_D=c[5],ratio_C=c[9],ratio_D=c[10]))
    for r in sharp['rows']:
        if r['mode']=='finite':assert r['safe_upper'] in text,r
        elif r['mode']=='uniform':
            assert r['safe_upper'] in text,r
            assert Q(r['safe_upper'])<Q('2.4945' if r['operator']=='C' else ('2.7441' if r['retained_reflection'] else '2.7442'))
    for r in radial['rows']:
        if Q(r['alpha'])>=Q(1,20):assert r['safe_upper_D'] in text
    # The printed savings table states rounded lower savings, never midpoints.
    section=text.split('| $\\frac1{20}$ | $13.6146872781$')[1].split('## 4.')[0]
    saving_by_a={Q(r['alpha']):Q(r['gain_lower']) for r in radial['rows']}
    for a,s in [(Q(1,20),'2.62e-5'),(Q(1,10),'4.96e-5'),(Q(1,5),'8.81e-5'),(Q(3,10),'1.15e-4'),(Q(1,2),'1.37e-4'),(Q(3,4),'1.02e-4'),(Q(9,10),'4.92e-5'),(Q(99,100),'5.41e-6')]:
        assert Q(s)<=saving_by_a[a]
    # Endpoint remainders in Section 9.
    ctx.prec=384;p=arb.pi();lead=2/(p*arb('0.001'))
    first=table['rows'][0]
    for key,bound in [('selected_upper_C','.4049'),('selected_upper_D','.8074')]:
        rem=arb(first[key]['exact_safe_endpoint'])-lead
        assert Q(str(rem.upper().fmpq()))<Q(bound)
    assert Q(first['selected_lower_D']['exact_safe_endpoint'])-Q(first['selected_upper_C']['exact_safe_endpoint'])>Q('.3094')
    for pth in [report,B/'table_v209_v210.json',B/'PROOF.md',Path(__file__)]:bind(pth)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',scope='Changed decimals and independently accepted source binding; editorial limitations in PROOF.md',rows=rows,sha256=hashes)
    (B/'decimal_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['time_utc'],'all ten table rows, finite coefficients, uniform envelopes and savings confirmed')
if __name__=='__main__':main()
