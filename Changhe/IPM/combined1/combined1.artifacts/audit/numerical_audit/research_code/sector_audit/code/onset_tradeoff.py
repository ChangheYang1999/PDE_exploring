from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1]
def H(p):return sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
start=time.monotonic();ctx.prec=512
source=BASE/'peer_data/N1_E_4_16.json';d=json.loads(source.read_text())
verified=BASE/'verification/stationary_extension_16_summary.json';v=json.loads(verified.read_text())
assert v['input_hashes']['peer_data/N1_E_4_16.json']==H(source)
assert all(r['exact_energy_match'] and r['exponent_match'] for r in v['norm_checks'])
rows=[];cost={}
for n in range(6,17):
 r=d[str(n)];e=Q(r['exponent_exact']);E=(arb.pi()*ar(Q(r['E_n_full_squared_over_pi_exact']))).sqrt();assert e<-1
 costs={str(T):E*arb(T)**ar(e+1)/ar(-2*e-2).sqrt() for T in [10,100,1000]}
 onset=(E/(arb('1e-8')*ar(-2*e-2).sqrt()))**ar(1/(-e-1))
 rows.append({'order':n,'exponent':str(e),'full_circle_norm':E.str(70),'isolated_L2_costs':{k:x.str(70) for k,x in costs.items()},'isolated_onset_for_1e_8':onset.str(70)})
 cost[n]=costs['10']
assert cost[10]<cost[9]
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'source_sha256':H(source),'verified_prefix_sha256':H(verified),'claim_sha256':H(BASE/'peer_data/numerics_v03.md'),'proof_sha256':H(BASE/'PROOF_ONSET_TRADEOFF.md'),'code_sha256':H(Path(__file__)),'rows':rows,'T10_order10_over_order9':(cost[10]/cost[9]).str(70),'T10_strict_decrease_9_to_10':True,'elapsed_seconds':time.monotonic()-start,'scope':'Isolated-sector costs. No complete-residual bound or infinite-series convergence claim.'}
p=BASE/'verification/onset_tradeoff.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('T10 cost9',cost[9].str(30),'cost10',cost[10].str(30),'ratio',(cost[10]/cost[9]).str(30),flush=True)
