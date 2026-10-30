"""Independently check the original and sharper T4 weak-probe bounds."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];ctx.prec=512;start=time.monotonic()
src=ROOT/'research/weak_probe/verification/d2_1024.json'
peer=ROOT/'research/pure_l2_probe/peer_review/T4_d2_512.json'
row=next(v for v in json.loads(src.read_text())['probes'] if v['p']==2)
target=json.loads(peer.read_text());I=abs(arb(row['pairing']));A,B,C=[arb(row[k]) for k in ['A','B','C']]
assert I.overlaps(arb(target['I']))
rows=[]
for b,exact_r in [(5,'27/10000'),(3,'29/10000')]:
 D=A+b*B+C;m=arb(int(exact_r.split('/')[0]))/int(exact_r.split('/')[1])
 root=2*I/(D+(D*D+4*I).sqrt());gap=I-D*m-m*m;assert gap>0
 pr=next(v for v in target['rows'] if v['B_coefficient']==b)
 rpeer=arb(27)/10000;gp=I-D*rpeer-rpeer*rpeer
 checks={'D':D.overlaps(arb(pr['D'])),'root':root.overlaps(arb(pr['necessary_L2_radius'])),'gap':gp.overlaps(arb(pr['gap']))}
 assert all(checks.values())
 rows.append({'B_coefficient':b,'D':D.str(80),'necessary_L2_radius':root.str(80),'excluded_closed_radius_exact':exact_r,
              'strict_gap_at_radius':gap.str(80),'T4_comparisons':checks})
 print(b,'root',root.str(30),'excluded',exact_r,'gap',gap.str(30),flush=True)
def sha(p):return sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':sha(src),'peer_sha256':sha(peer),
 'code_sha256':sha(Path(__file__)),'review_sha256':sha(ROOT/'research/pure_l2_probe/REVIEW_T4.md'),
 'precision_bits':ctx.prec,'rows':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'research/pure_l2_probe/verification/T4_comparison_512.json').write_text(json.dumps(out,indent=2)+'\n')
