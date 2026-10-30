from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time,re
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
def H(p):return sha256(p.read_bytes()).hexdigest()
def A(q):
    q=Q(q)
    return arb(q.numerator)/arb(q.denominator)
def val(x):return x.str(85)
def logarithmic_onset(S,sig,tau):
    return (arb.pi().log()+A(S).log()-A(2*sig).log()-2*A(tau).log())/(2*A(sig)*arb(10).log())
start=time.monotonic();ctx.prec=384
n4=BASE/'source/n4_sectors.json';a2=BASE/'source/a2_sector6.json';target=BASE/'source/T2_review.log'
z=json.loads(n4.read_text());old=json.loads(a2.read_text());c=Q(z['cl']);delta=1-1/c
v6={int(n):Q(v) for n,v in z['branches']['6']['forcing_sin'].items()}
assert v6=={int(n):Q(v) for n,v in old['leading_sine_coefficients'].items()}
tols={'T1 model D(b)':Q(12726,10**13),'FW-T-TB-rebal-v1':Q(18332,10**12),'FW-T-TB-graded-v1 (i)':Q(35378,10**12),'FW-T-TB-graded-v1 (ii)':Q(31820,10**12),'FW-T-TB-sharp-v1':Q(21259,10**11)}
rows={};objects={}
for j in (6,7,8):
    b=z['branches'][str(j)];sig=(j+1)*delta-3;assert sig==-2-Q(b['residual_exponent']) and sig>0
    v={int(n):Q(x) for n,x in b['forcing_sin'].items()};assert all(n>0 and n%2 for n in v)
    S=sum((x*x/(n+sig)**2 for n,x in v.items()),Q(0));P=sum((x*x for x in v.values()),Q(0));Z=sum((x*x/(n*(n+sig)) for n,x in v.items()),Q(0))
    amp=(arb.pi()*A(P)).sqrt();eff=(arb.pi()*A(S)).sqrt();tr=(arb.pi()*A(Z)).sqrt()
    onsets={name:logarithmic_onset(S,sig,tau) for name,tau in tols.items()}
    objects[j]={'sigma':A(sig),'A':amp,'A_eff':eff,'onsets':onsets}
    rows[str(j)]={'sigma':val(A(sig)),'max_mode':max(v),'modes':len(v),'A':val(amp),'A_eff':val(eff),'A_truncated':val(tr),'ratio':val(eff/amp),'log10_onset':{name:val(x) for name,x in onsets.items()},'largest_shares':[[n,val(A(x*x/P))] for n,x in sorted(v.items(),key=lambda it:it[1]*it[1],reverse=True)[:5]]}
comparisons=[];j=None
for line in target.read_text().splitlines():
    m=re.match(r'    branches ([678]): sigma = (\[.*?\]), A = (\[.*?\]), N = (\d+), A_eff = (\[.*?\]),',line)
    if m:
        j=int(m[1]);assert int(m[4])==rows[str(j)]['max_mode']
        for key,index in [('sigma',2),('A',3),('A_eff',5)]:
            ok=objects[j][key].overlaps(arb(m[index]));assert ok
            comparisons.append({'branch':j,'key':key,'peer_interval':m[index],'overlap':ok})
    elif j and line.startswith('      '):
        m=re.search(r'exact \(2\): (\[.*?\])',line)
        if m:
            name=line.strip().split(' tau =')[0].strip();assert name in tols
            ok=objects[j]['onsets'][name].overlaps(arb(m[1]));assert ok
            comparisons.append({'branch':j,'key':name,'peer_interval':m[1],'overlap':ok})
assert len(comparisons)==24
out={'utc':datetime.now(timezone.utc).isoformat(),'code_sha256':H(Path(__file__)),'proof_sha256':H(BASE/'PROOF.md'),'input_sha256':{p.name:H(p) for p in (n4,a2,target)},'precision_bits':ctx.prec,'branch6_exact_agreement':True,'all24_interval_comparisons_overlap':True,'rows':rows,'comparisons':comparisons,'elapsed_seconds':time.monotonic()-start}
(BASE/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'all24_interval_comparisons_overlap':True,'elapsed_seconds':out['elapsed_seconds'],'onsets':{j:r['log10_onset'] for j,r in rows.items()}},indent=2))
