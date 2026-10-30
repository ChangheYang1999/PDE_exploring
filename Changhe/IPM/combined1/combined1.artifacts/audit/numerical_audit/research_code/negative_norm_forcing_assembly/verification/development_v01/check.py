"""Independent monotone norm comparisons with verified rational endpoints."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time
from fractions import Fraction
from flint import arb, fmpq as Q, ctx

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/negative_norm_forcing_assembly'

def H(p):
    return sha256(Path(p).read_bytes()).hexdigest()

def R(q):
    if isinstance(q, str):
        f = Fraction(q)
        return Q(f.numerator, f.denominator)
    return Q(q)

def A(q):
    q = R(q)
    return arb(q.numerator)/arb(q.denominator)

def interval(row, low='norm_lower_ball', high='norm_upper_ball'):
    return arb(row[low]).union(arb(row[high]))

def bounds(value, digits=7):
    scale = 10**digits
    center = int(float(value)*scale)
    for padding in [2, 4, 16, 256, 65536, 16777216]:
        lo, hi = Q(center-padding, scale), Q(center+padding, scale)
        if value > A(lo) and value < A(hi):
            return {'ball': value.str(90), 'strict_lower_exact': str(lo),
                    'strict_upper_exact': str(hi), 'strict_bounds_verified': True}
    raise ArithmeticError('No outward rational endpoints at the requested scale')

def derive(comp, s, w1, w2, cw):
    s, cw = Q(s), Q(cw)
    assert 0 < s < 1 and 1-Q(48,25)*s > 0
    E = (comp['P2']**2+w1*comp['G1']**2+w2*comp['G0']**2).sqrt()
    lower = (1-A(Q(48,25)*s))*E
    upper = E**A(1-s)*(2*comp['Q3']**2+A(cw)*E**2)**A(s/2)+A(Q(48,25)*s)*E
    return E, lower, upper

import gzip
start=time.monotonic();ctx.prec=512
sources=json.loads((BASE/'source/MANIFEST.json').read_text())
for rel,row in sources['files'].items():assert H(BASE/'source'/rel)==row['sha256']
prior=ROOT/'research/registered_norm_assembly/source'
oldman=json.loads((prior/'MANIFEST.json').read_text())
for key in ['N4_G0.json','N4_derivatives.json','N4_Q3.json','N4_candidate_audit.json']:assert H(prior/key)==oldman['files'][key]['sha256']
read=lambda p:json.loads(Path(p).read_text())
g0=read(prior/'N4_G0.json');der=read(prior/'N4_derivatives.json');q3=read(prior/'N4_Q3.json');ident=read(prior/'N4_candidate_audit.json')
accepted=ROOT/'research/negative_norm007_peer/verification/result.json';acc=read(accepted)
assert H(accepted)=='a59be362d5ca29e7e60c7293211a611ddf932620e41d9269d879b231b126dde3'
assert acc['source_and_fix_bindings_confirmed'] and acc['peer_totals_reproduced_at512bits'] and acc['own_full_norm_strictly_inside_peer']
hfile=ROOT/'research/negative_norm007_peer/source/N3_007_hminus1.json.gz'
hbytes=gzip.decompress(hfile.read_bytes());assert sha256(hbytes).hexdigest()==acc['peer_original_result_sha256']
hrec=json.loads(hbytes);peer=read(BASE/'source/N3_registered.json')
assert peer['source_sha256']==ident['generator_sha256']==acc['source_sha256']
assert g0['source_sha256']==ident['canonical_sha256']==acc['canonical_file_sha256']
assert peer['canonical_sha256']==acc['canonical_serialization_sha256']
assert hrec['H_lower']==peer['components']['H']['LB'] and hrec['H_upper']==peer['components']['H']['UB']
assert g0['status']=='FINITE' and der['complete'] and q3['complete']
comp={'G0':interval(g0),'G1':interval(der['norms']['G1']),'P2':interval(der['norms']['P2']),'Q3':interval(q3),'H':arb(hrec['H_lower']).union(arb(hrec['H_upper']))}
checks={k:comp[k].overlaps(interval(peer['components'][k],'LB','UB')) for k in comp}
assert all(checks.values())
elo=(arb(der['norms']['P2']['norm_lower_ball'])**2+2**14*arb(der['norms']['G1']['norm_lower_ball'])**2+2**18*arb(g0['norm_lower_ball'])**2+A(Q(2**18*20,21))*arb(hrec['H_lower'])**2).sqrt()
ehi=(arb(der['norms']['P2']['norm_upper_ball'])**2+2**14*arb(der['norms']['G1']['norm_upper_ball'])**2+2**18*arb(g0['norm_upper_ball'])**2+A(Q(2**18*20,21))*arb(hrec['H_upper'])**2).sqrt()
assert elo>0 and ehi>elo
pe=peer['derived']['E_2 (NORM-A2-E2)']
checks['E_lower_strictly_inside_printed_peer']=elo>A(pe['LB']);checks['E_upper_strictly_inside_printed_peer']=ehi<A(pe['UB'])
instances=[('FW-A2-Db','1/262144','1/1572864'),('FW-A2-Da','1/268435456','1/2684354560'),('FW-T-TB-rebal-v1','1/65536','91553/10000000000'),('FW-T-TB-sharp-v1','1/8192','5289/50000000')]
rows=[]
for name,ss,tt in instances:
 s0=Q(ss);th=Q(tt);assert 0<s0<Q(1,34)
 low=(1-A(34*s0))*elo
 high=ehi**A(1-s0)*(2*arb(q3['norm_upper_ball'])**2+16410*ehi**2)**A(s0/2)+A(34*s0)*ehi
 recs=[v for k,v in peer['thresholds'].items() if k.startswith(name+' (')];assert len(recs)==1;pr=recs[0]
 nesting={'lower':bool(low>A(pr['LB'])),'upper':bool(high<A(pr['UB']))};assert all(nesting.values()),(name,nesting)
 ratio=low/A(th);assert ratio>1
 rows.append({'framework':name,'s_exact':str(s0),'threshold_exact':str(th),'lower_comparison':bounds(low,6),'upper_comparison':bounds(high,6),'strict_necessary_norm_lower':bounds(low,6)['strict_lower_exact'],'strict_norm_upper':bounds(high,6)['strict_upper_exact'],'ratio_lower':bounds(ratio,1),'peer_printed_strict_containment':nesting,'peer_threshold_display_is_approximate':pr['threshold'],'sufficient_smallness_fails':True})
assert all(checks.values()),checks
sq={'P2':comp['P2']**2,'G1':2**14*comp['G1']**2,'G0':2**18*comp['G0']**2,'H':A(Q(2**18*20,21))*comp['H']**2};esq=sum(sq.values(),arb(0));shares={k:v/esq for k,v in sq.items()}
inputs={str(p.relative_to(ROOT)):H(p) for p in [Path(__file__),BASE/'PROOF.md',BASE/'source/MANIFEST.json',prior/'MANIFEST.json',accepted,hfile]+[prior/k for k in ['N4_G0.json','N4_derivatives.json','N4_Q3.json','N4_candidate_audit.json']]}
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':g0['candidate'],'source_sha256':acc['source_sha256'],'bits':ctx.prec,'checks':checks,'H_input_lower_ball':hrec['H_lower'],'H_input_upper_ball':hrec['H_upper'],'E_lower':bounds(elo,6),'E_upper':bounds(ehi,6),'energy_share_balls':{k:v.str(70) for k,v in shares.items()},'instances':rows,'inputs':inputs,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED numerical assembly from independently confirmed whole-plane components and A2 comparison theorem; all four sufficient thresholds fail; no correction-distance or existence inference'}
dest=BASE/'verification/result.json'
with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('E',elo.str(30),ehi.str(30),'seconds',out['elapsed_seconds'])
for row in rows:print(row['framework'],row['strict_necessary_norm_lower'],row['strict_norm_upper'],'ratiofloor',row['ratio_lower']['strict_lower_exact'])
print('SHA256',H(dest))
