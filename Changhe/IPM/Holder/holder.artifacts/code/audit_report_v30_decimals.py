"""Check decimal claims against already accepted exact endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,ctx
import hashlib,json,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'05_team_audit/report_v30'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ep(x,up=False):return Q(str((x.upper() if up else x.lower()).fmpq()))
def ceil(q,n):
    t=q*10**n;k=-((-t.numerator)//t.denominator)
    return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
    report=OUT/'FINAL_REPORT.md';text=report.read_text();assert sha(report)=='136650521776f99a49c91434e611eb2fd35fa32ed1b5d8fec13ea7ebc08335db'
    tp=OUT/'table_v198.json';table=load(tp)
    source=ROOT/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density/symmetric_concavity/fourth_moment/numerical_values/accepted.json';d=load(source)
    assert d['verdict']=='CONFIRMED' and d['ledger']=='V198'
    for name,digest in d['sha256'].items():assert sha(ROOT/name)==digest,name
    leadp=ROOT/'05_team_audit/strict_gain_lead49/source/eta_apply.json';lead={Q(r['alpha']):r for r in load(leadp)['rows']}
    accepted={Q(r['alpha']):r for r in d['rows']};rows=[]
    for row in table['rows']:
        a=Q(row['alpha']);item=accepted[a];assert lead[a]['new_upper_D']==item['safe_upper_D']
        ur=Q(item['safe_upper_D']);low=Q(row['selected_lower_D']['exact_safe_endpoint'])
        marker='| '+str(float(a))+' |';line=next(x for x in text.splitlines() if x.startswith(marker));cells=[s.strip() for s in line.split('|')[1:-1]]
        assert cells[5]==ceil(ur,6)==row['upper_D'];assert Q(cells[10])>=ur/low
        assert Q(cells[10])-Q(ceil(ur/low,4))<=Q(1,10000)
        assert cells[4]==row['upper_C'] and cells[8].strip('*')==row['lower_D']
        assert item['safe_upper_D'] in text
        rows.append(dict(alpha=str(a),upper_D=cells[5],ratio_D=cells[10],least_ratio_ceiling=ceil(ur/low,4),lead_endpoint_agrees=True))
    ctx.prec=384;remainder=arb('42.2175842339')-3*arb(3).sqrt()/(arb('0.04')*arb.pi());assert ep(remainder,True)<Q('.8680')
    record=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',scope='Numerical changes only; prose limitations are in PROOF.md',rows=rows,endpoint_remainder=remainder.str(45),sha256={str(p.relative_to(ROOT)):sha(p) for p in [report,tp,source,leadp,OUT/'PROOF.md',Path(__file__)]})
    (OUT/'decimal_checks.json').write_text(json.dumps(record,indent=2)+'\n');print('All ten endpoints and ratios, lead comparison, remainder ceiling confirmed.')
if __name__=='__main__':main()
