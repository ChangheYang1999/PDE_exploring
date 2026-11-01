"""Refresh live handoff indexes without changing historical admissions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
p=Path('FINAL_CLAIM_MAP.md');s=p.read_text();s=re.sub(r'Updated [^.]+\.',f'Updated {now}.',s,count=1)
s=s.replace('PROVED. Irrational delta/2 with finite Brjuno sum;', 'PROVED. Irrational 0<delta<1 with delta/2 having finite Brjuno sum;')
s=s.replace('[303](research/303_period_nine_ten_floating_extensions/PROOF.md) |','[303](research/303_period_nine_ten_floating_extensions/PROOF.md), [305](research/305_final_conditional_fit_scope/PROOF.md) |')
a=s.index('## Pending final checks');b=s.index('The canonical rational logarithmic convergence question',a)
s=s[:a]+'''## Final checks and remaining integration

- Topic290 is complete throughV610. All norm overlaps match; the single printed tuning discrepancy remains explicit.
- Topic266 is complete through conditional order440, V622/V623. Its norm, last-order Poisson, full-vector fit and monitor checks retain the order329 midpoint condition and their stated nonlinear-replay limits.
- V618 confirms the scoped frozen-summary review against68 complete proof rereads. V613 andV617 close the earlier wording repairs. Later insertions have separate receipts.
- Topic305, V621/V626: all seven printed regression windows reproduce. Rounding reverses the final-window ranking; unrounded and printed-data fits must be named separately. Peer wording integration is being checked.
- Topic300, V624: the universal10^-0.70 decay-rate clause is refuted by the half-exponent run. Repair is pending.
- Topic303: Q10roots1..11 are admitted as finite floating statistics; the remaining Q10 and Q9 extensions are being checked, including all printed differences.

'''+s[b:];p.write_text(s)
refs=[]
for name in dict.fromkeys(re.findall(r'\]\(([^)]+)\)',s)):
 q=Path(name.split('#')[0]);assert q.is_file(),q
 refs.append(dict(path=str(q),sha256=sha256(q.read_bytes()).hexdigest()))
Path('artifacts/final_claim_map_sources.json').write_text(json.dumps(dict(at=now,scope='Proof-file inventory only; not a fresh proof or full artifact audit.',map_sha256=sha256(p.read_bytes()).hexdigest(),sources=refs),indent=2)+'\n')
p=Path('VERIFY_SUMMARY.md');s=p.read_text();s=re.sub(r'Updated [^\n]+',f'Updated {now}, through V626. The campaign is active. Superseded claims and their corrections remain in the chronological [verification ledger](VERIFY_REPORT.md). The [claim map](FINAL_CLAIM_MAP.md) and [research index](research/INDEX.md) give the reading order and exact standalone statements.',s,count=1)
a=s.index('Q10 extension roots');b=s.index('\n\n',a)
s=s[:a]+'''Q10 extension roots1..11 are admitted in V612, V614, V619, V620 and V625. All printed norm overlaps agree. Three root1 tuning components differ by10^-12. The largest admitted same-window A change is6.39309% at root1 on the lower100 window; its apparent-radius change is28.13134%. Remaining Q10 and Q9 extensions are pending and will be admitted separately.'''+s[b:]
a=s.index('## Remaining work and evidence')
s=s[:a]+'''## Remaining work and evidence

The conditional delta2/3 audit through440 is complete. Pending work consists of the remaining Q9/Q10 floating extensions, final prose integration and evidence/publication checks. The admission-reference audit at22:55:42Z checked85 receipts and438 references:435 current matches, two historical proof snapshots and one lossless compressed original, with no unexplained mismatch. It will be refreshed for later receipts. This is a provenance check, not a fresh mathematical proof. [PUBLICATION_INDEX.md](PUBLICATION_INDEX.md) identifies operational exclusions and four sanitized transcript projections.

V621/V626 compare the final class-zero fits: all31 printed multiplier bins and49 fit-statistic bins pass;42 distinct regressions were replayed at two precisions. On420..438, printed power RMS4.27390e-5 is below exponential4.35272e-5, whereas unrounded exponential RMS1.10211e-5 is below power3.21563e-5. Rounding reverses the ranking. These data sets and the all-order vector fits in V622 must remain distinct. No infinite growth law follows. The numerics lane accepted the printed-data correction; final integration remains under review.

V624 refutes a separate universal decay-rate sentence in the numerical summary. For the canonical half-exponent run, every density log10 increment on271..300 lies between-0.421 and-0.417, with mean-0.41870918846. The claimed common rate-0.70 does not apply to this included run. This is a finite counterexample, not a convergence verdict.
''';p.write_text(s)
p=Path('research/301_final_claim_audit/PROOF.md');s=p.read_text();s=s.replace('Status: protocol prepared; final frozen reports not yet admitted.','Status: scoped frozen-summary review admitted in V618; subsequent finite insertions require their own checks.');p.write_text(s)
p=Path('FINAL_AUDIT_PLAN.md');s=p.read_text();s=re.sub(r'Updated [^.]+\.',f'Updated {now}.',s,count=1);s=s.replace('V621 refutes one new final numerical ranking statement; repair remains pending in peer text.','V621/V626 establish the printed-versus-unrounded ranking reversal. Numerics accepts V621; verify final lead integration. V624 flags the remaining universal decay-rate clause.');s=s.replace('Q10roots1..9 admitted.','Q10roots1..11 admitted.');p.write_text(s)
p=Path('RUN_STATUS.md');s=p.read_text();s=re.sub(r'Updated [^.]+\.',f'Updated {now}.',s,count=1);s=s.replace('Ledger throughV623; nextV624.','Ledger throughV626; nextV627.');s=s.replace('Prompt reread fully22:01Z this shift.','Prompt reread fully23:07:36Z this shift.');s=s.replace('V612,V614,V619,V620 admit Q10roots1..9.','V612,V614,V619,V620,V625 admit Q10roots1..11.');s=s.replace('No infinite theorem changed.','V626 replays all7windows and shows unrounded-data ranking reverses the printed final-window ranking. V624 adds a pending correction: the half-exponent late mean is-0.418709, contradicting the universal-0.70 clause. No infinite theorem changed.');s=s.replace('FINAL_CLAIM_MAP.md and its source hashes refreshed now. VERIFY_SUMMARY.md consolidated22:56:40 through619.','FINAL_CLAIM_MAP.md and its source hashes refreshed23:10Z. VERIFY_SUMMARY.md consolidated through626.');s=s.replace('Latestinventory22:55:42 allocated2983096320bytes,unique2957853453,logical2964766331,sharedfree127.6GB.','Latestinventory23:05:42 allocated2979540992bytes,unique2953944186,logical2960857064,sharedfree124.7GB.');p.write_text(s)
with Path('WORKLOG.md').open('a') as f:f.write(f'\n{now}: Refreshed live summary, claim map ({len(refs)} links), source hashes and handoff throughV626. Historical snapshots remain unchanged.\n')
print(now,len(refs))
