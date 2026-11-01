"""Prepare the Q10 application before computing its prefix certificates."""
from pathlib import Path
from datetime import datetime,timezone
root=Path('research/286_period_ten_prefixes')
for sub in ['sources','verification']:(root/sub).mkdir(parents=True,exist_ok=True)
text=Path('research/280_period_nine_prefixes/PROOF.md').read_text().split('## Period-nine input specialization')[0]
text=text.replace('period nine','period ten').replace('Fix Q=9','Fix Q=10').replace('one of the ten real roots','one of the fourteen real roots').replace('certified in267','certified in281')
text=text.replace('Status: conditional application protocol, independently reviewed by the lead on2026-10-31 at20:26:02Z. The ten new Q9 prefix applications are pending their completed Cartesian, polar and exact-box replays. The proof was written before computation.', 'Status: conditional application protocol written before computation. The fourteen Q10 applications require completed Cartesian, polar and exact-box replays, together with admissions281,282,283 and285.')
text=text.replace('Let f_n,g_n be the unique tuned pure density and stream coefficients from those results.', 'Let f_n,g_n be the formal tuned pure density and stream coefficients defined by the recurrence and the nonzero responses of282. This construction is formal until the majorant below proves convergence.')
text=text.replace('proved in132 and270','proved in132 and283').replace('L=243/104','L=75/29').replace('Dependencies:01,130,132,169,172,175,267,270,277,278.','Dependencies:01,130,132,169,172,175,281,282,283,285.')
text+='''
## Period-ten input specialization

The compatibility polynomial in281 has degree20. Its fourteen real simple roots and the exact Cartesian prefix through20 must be admitted before the application is called proved. The generic response identity in282 and its degree and factor certificates supply nonvanishing at every root. The positive rational lower bound s for each root comes from285, whose entire root interval is certified; the bound is not inferred from finite samples. At N=20 the displayed kappa equals1092/25; subsequent N use the displayed formula exactly.

Each finite calculation is independently repeated by a polar recurrence with two full provisional continuations for every tuned free harmonic. Its density and stream norms must overlap the Cartesian intervals and lie below every rational majorant input. Every rational supersolution is then replayed from its input data. An admission records the actual completed N and dyadic q separately for each root. The physical radius is2^(q/2)|epsilon|^5. No empirical growth fit replaces any of these checks.
'''
(root/'PROOF.md').write_text(text)
for old,new in [('period_nine_prefix.py','period_ten_prefix.py'),('period_nine_prefix_replay.py','period_ten_prefix_replay.py'),('period_nine_polar_replay.py','period_ten_polar_replay.py')]:
 src=Path('code',old).read_text().replace('research/280_period_nine_prefixes','research/286_period_ten_prefixes').replace('research/267_period_nine_tuning','research/281_period_ten_finite_algebra')
 src=src.replace('longer Q9 prefixes','longer Q10 prefixes').replace('a.Q==9 and 1<=a.root<=10','a.Q==10 and 1<=a.root<=14')
 for a,b in [('period_nine_prefix.py','period_ten_prefix.py'),('period_nine_prefix_replay.py','period_ten_prefix_replay.py'),('period_nine_polar_replay.py','period_ten_polar_replay.py')]:src=src.replace(a,b)
 if old=='period_nine_prefix.py':
  start=src.index(" rp=folder/f'verification/root{index}_review.json'")
  end=src.index('\n b,I=refine_root',start)
  src=src[:start]+"\n ip=Path('research/285_period_ten_response_bounds/verification/checks.json.gz');ir=ip.read_bytes();bounds=json.loads(gzip.decompress(ir));assert bounds['all_checks_pass']\n boundrow=bounds['rows'][index-1];assert boundrow['root_index']==index and boundrow['root_interval']==obs['real_roots'][index-1]['interval'];s=F(boundrow['s']);assert s>0"+src[end:]
  src=src.replace('[(op,ob),(rp,rr),(ip,ir)]','[(op,ob),(ip,ir)]')
 Path('code',new).write_text(src)
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
with Path('research/INDEX.md').open('a') as f:f.write('\n286. [Period-ten prefix majorants](286_period_ten_prefixes/PROOF.md): formal tuned branches become convergent only after independently replayed positive supersolutions.\n')
p=Path('NOTES_FOR_TEAM.md');p.write_text(f'## {now} VERIFIER -> LEAD: Q10 prefix-majorant protocol286 prepared for review\n\nThe proof specializes175/280 to Q10, L=75/29 and kappa20=1092/25. It assumes only formal tuned coefficients before applying the majorant, so it does not assume convergence. Four candidate prefixes20/40/60/80 and physical radius2^(q/2)|epsilon|^5; all-index bounds must come from285, independently replayed. No Q10 prefix computation has started. Please review this specialization alongside285.\n\n'+p.read_text())
print(now)
