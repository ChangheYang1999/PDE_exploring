"""Prepare a Q9 specialization of the previously audited prefix protocol."""
from pathlib import Path
from datetime import datetime,timezone
root=Path('research/280_period_nine_prefixes')
for sub in ['sources','verification']:(root/sub).mkdir(parents=True,exist_ok=True)
text=Path('research/261_period_seven_eight_prefixes/PROOF.md').read_text()
text=text.split('## Completed applications')[0]
text=text.replace('Status: PROVED applications V539. All twenty finite prefixes, independent polar replays and exact scalar box checks passed. The original protocol was written before computation.', 'Status: conditional application protocol. The ten new Q9 prefix applications require completed Cartesian, polar and exact-box replays. The proof is written before computation.')
text=text.replace('Certified longer prefixes at periods seven and eight','Certified longer prefixes at period nine').replace('Fix Q in {7,8}', 'Fix Q=9').replace('certified in253 or256','certified in267').replace('proved in132 and258','proved in132 and270').replace('Dependencies:01,130,132,169,172,175,253,256,258.', 'Dependencies:01,130,132,169,172,175,267,270,277,278.').replace('the displayed L and kappa','the displayed L=243/104 and kappa')
text+='''
## Period-nine input specialization

The exact compatibility polynomial has degree18 and ten real simple roots, as established in267. The low-order reference coefficients are the independently derived Cartesian polynomials through18. The all-index lower response bounds may be the old bounds from267, or rational numbers strictly below the global infima from278. In the latter case the receipt must name the278 certificate, prove the rounded lower bound is smaller than its directed infimum, and require278 to be admitted before using the new radius. Each root retains a separate bound and no claim is made between these isolated profiles except the already proved local genericity theorem.

A separate polar recurrence uses two full provisional continuations for every tuned harmonic, so it does not depend on the compact-response formula used by the Cartesian producer. It verifies overlap of the density and stream norms at every order and verifies the rational bounds used by every majorant box. This is a new execution of the previously audited261 protocol at Q=9; it does not introduce a different convergence mechanism.
'''
(root/'PROOF.md').write_text(text)
for old,new in [('period_high_prefix.py','period_nine_prefix.py'),('period_high_prefix_replay.py','period_nine_prefix_replay.py'),('period_polar_prefix_replay.py','period_nine_polar_replay.py')]:
 src=Path('code',old).read_text().replace('research/261_period_seven_eight_prefixes','research/280_period_nine_prefixes')
 src=src.replace("folder=Path('research', '253_period_seven_tuning' if Q==7 else '256_period_eight_tuning')","folder=Path('research/267_period_nine_tuning')")
 src=src.replace('a.Q in [7,8]','a.Q==9').replace('longer Q7/Q8 prefixes','longer Q9 prefixes')
 src=src.replace("'period_high_prefix.py'","'period_nine_prefix.py'").replace("'period_high_prefix_replay.py'","'period_nine_prefix_replay.py'").replace("'period_polar_prefix_replay.py'","'period_nine_polar_replay.py'")
 if old=='period_high_prefix.py':
  src=src.replace("s=F(review['s'])", "s=F(review['s'])\n ip=Path('research/278_period_nine_response_infima/verification/checks.json.gz');ir=ip.read_bytes();infima=json.loads(gzip.decompress(ir));assert infima['all_checks_pass']\n ib=arb(infima['rows'][index-1]['infimum']);scale=F(1)\n while endpoints(ib)[0]*scale<1000:scale*=10\n while endpoints(ib)[0]*scale>=10000:scale/=10\n s=F((endpoints(ib)[0]*scale).__floor__())/scale;assert s>0 and ball(mpq(str(s)))<ib")
  src=src.replace('[(op,ob),(rp,rr)]','[(op,ob),(rp,rr),(ip,ir)]')
 Path('code',new).write_text(src)
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
with Path('research/INDEX.md').open('a') as f:f.write(f'\n- 280: [Longer period-nine prefixes](280_period_nine_prefixes/PROOF.md). Proof protocol written{now}; admission requires Cartesian/polar replay, exact boxes and278.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: topic280 longer period-nine prefix protocol\n\nI have specialized the accepted261/175 protocol to Q9 with L=243/104 and the same N-dependent kappa. The response bounds are rational round-downs of the278 global infima. I will compare1536-bit Cartesian prefixes with2048-bit polar two-continuation replays and then reassemble every rational majorant box. This is solely a sharper sufficient-radius computation; the existing ten convergent branches and73-profile count stay fixed. Please review the Q9 specialization together with278 when available.\n\n'+p.read_text())
print(now)
