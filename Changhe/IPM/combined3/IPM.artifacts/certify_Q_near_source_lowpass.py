#!/usr/bin/env python3
"""Apply the actual radial envelopes to the genuine Q near low-block price."""
import argparse,json
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--envelopes',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    data=json.loads(args.envelopes.read_text())
    assert data['status']=='CERTIFIED_RADIAL_NEAR_SOURCE_ENVELOPES'
    ctx.prec=384
    for name,digest in data['configuration']['bindings'].items():
        assert sha256((HERE/name).read_bytes()).hexdigest()==digest
    mu=arb(1);e=arb(1).exp()
    A2=2/e.sqrt();A3=3*arb(3).sqrt()/e
    B0=arb(1);B1=1/e.sqrt();B2=2/e
    def Cl(l):
        s=(arb(l)+(arb(l*l+4)).sqrt())/2
        return s.sqrt()*(1+s)**(arb(l)/2)*(-s/2).exp()
    D2=2*Cl(0)+Cl(2);D3=3*Cl(1)+Cl(3)
    rows=[]
    for row in data['rows']:
        a0=arb(row['a0']);a1=arb(row['a1'])
        L2=(A2+2*D2)*a0+2*A2*a1
        L3=(A3+2*D3)*a0+2*A3*a1
        rest2=(4*B1+8*B0)*a0
        rest3=(arb(8).sqrt()*A2+24*B1+4*B2+40*B0)*a0
        Cb=(L2+rest2)**arb('.9')*(L3+rest3)**arb('.1')
        Cr=(arb(5).sqrt()/2*L2+rest2)**arb('.9')*(
             arb(5).sqrt()/2*L3+rest3)**arb('.1')
        coefficient=arb(3).sqrt()*Cb+Cr
        prices={}
        for delta in ['.1','.2','.25','.5']:
            prices[delta]=(coefficient*coefficient/(4*arb(delta))).str(80)
        rows.append({'cut_R':row['cut_R'],'a0':row['a0'],'a1':row['a1'],
                     'C_b':Cb.str(80),'C_R1':Cr.str(80),
                     'mixed_coefficient':coefficient.str(80),
                     'weak_price_by_p2_charge':prices})
    files=[Path(__file__),HERE/'Q_NEAR_SOURCE_LOWPASS_PRICE.md',
           args.envelopes]
    out={'status':'CERTIFIED_ACTUAL_Q_NEAR_SOURCE_LOW_BLOCK_PRICE',
         'mu':'1','rows':rows,
         'bindings':{str(p):sha256(p.read_bytes()).hexdigest() for p in files},
         'finished_utc':datetime.now(timezone.utc).isoformat(),
         'scope':'Only near source low/low form. Near high/cross, transport, '
                 'fractional source, and complete energy remain separate.'}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
