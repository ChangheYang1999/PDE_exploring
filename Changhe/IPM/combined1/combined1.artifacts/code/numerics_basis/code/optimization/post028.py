#!/usr/bin/env python3
"""After snap028.sh: read 028's diag2 JSON and the snapshot MANIFEST; patch NUMERICS_FINAL (7b entry, table row, 0b), write the v15 change lines, print a NOTES entry draft."""
import json, os, re, sys, glob, datetime, hashlib
root='RUN_ROOT/numerics_N1N2'; opt=root+'/numerics/optimization'; T='legqs25_nin24_m9to15_gpu_m16'
d=json.load(open(f'{opt}/candD2/{T}_diag2.json')); bl=d['BL2']
snaps=sorted(glob.glob('candidates/C1-N1-028*'))
snap=snaps[-1] if snaps else None; sid=os.path.basename(snap) if snap else 'C1-N1-028 (snapshot pending)'
stamp='?'
if snap:
    m=json.load(open(f'{snap}/MANIFEST.json')); stamp=m.get('created_utc', m.get('time', m.get('created', '?')))
sha=hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json','rb').read()).hexdigest()
mid32=(f"G0 {d['G0']:.4f} (MID 16 report 0.2437; 027 0.2762, 026 0.2788, 022 0.2816, 016 0.3089, 007 0.3767), G1 {d['G1']:.3f} (MID 16 3.253; 027 3.426), P2 {d['P2']:.1f} (MID 16 197.3; 027 199.7), "
       f"rF {d['rF']:.3f} (MID 16 6.551; 027 6.820), H {d['H']:.4f} (027 0.6101), sup|F| {d['supF']:.4f} (MID 16 0.1290; 027 0.1240), theta_inner {bl['theta_inner_sup']:.4f}, kappa_inner {bl['kappa_inner']:.4f} "
       f"((B-L2) margin {0.810319 - bl['theta_inner_sup'] - bl['kappa_inner']:+.4f}; 027 +0.0689)")
rel=max(abs(d['G0']/0.2436548-1), abs(d['G1']/3.252719-1), abs(d['P2']/197.3494-1), abs(d['rF']/6.550651-1))
h18=(f"H18 check part 2: the MID 32 norms differ from the MID 16 optimizer values by at most {100*rel:.1f} percent in G0, G1, P2 and rF (027 pair: at most 1 percent in G0); against the listed MID 32 endpoints of this lane, 028's G0 {d['G0']:.4f} is "
     f"{'below' if d['G0']<0.2762 else 'not below'} 027's 0.2762, its G1 {d['G1']:.3f} {'below' if d['G1']<3.426 else 'not below'} 027's 3.426 and its P2 {d['P2']:.1f} {'below' if d['P2']<199.7 else 'not below'} 027's 199.7 (the earlier 'lowest P2 of the campaign' wording was withdrawn: 013 reported P2 191.5 at MID 16); sampled sup|F| at MID 32 is {d['supF']:.4f} against 027's 0.1240 (FLOAT mesh maxima).")
p=f'{root}/NUMERICS_FINAL.md'; s=open(p).read()
a="MID 32 norms (diag2) and snapshot: PENDING (diag2 running since about 14:46Z; then snap028.sh)."
b=f"MID 32 norms (diag2, FLOAT): {mid32}. {h18} Snapshot {sid} ({stamp}; exact JSON sha256 {sha[:8]}...)."
assert s.count(a)==1; s=s.replace(a,b)
a2="| MID 16: 0.2437 | 3.253 | 197.3 | 6.551 | - | 0.1290 | - |"
b2=f"| {d['G0']:.4f} (MID 16 0.2437) | {d['G1']:.3f} | {d['P2']:.1f} | {d['rF']:.3f} | {d['H']:.4f} | {d['supF']:.4f} | {bl['kappa_inner']:.4f} |"
assert s.count(a2)==1; s=s.replace(a2,b2)
s=s.replace("run done 14:05Z, tests running)", f"run done 14:05Z; snapshot {stamp})")
s=s.replace("MID 32 norms PENDING (diag2 about 15:00Z); result in numerics_v14 |", "MID 32 norms in 7b; result in numerics_v14/v15 |")
s=s.replace("snapshots C1-N1-001 to C1-N1-027 (028 PENDING: snapshot after its diag2)", f"snapshots C1-N1-001 to C1-N1-028 ({sid} {stamp})")
open(p,'w').write(s)
c=f'{root}/numerics/v15_changes.md'; t=open(c).read()
t=t.replace('SNAP028LINE', f"{sid} ({stamp}; exact JSON sha256 {sha}; 2666 generators; held-out file heldout/HELDOUT_028.md sha256 caf3517a... bound in the MANIFEST description). MID 32 norms (diag2, FLOAT): {mid32}.")
t=t.replace('MID32LINE', h18); open(c,'w').write(t)
print(f"NOTES DRAFT:\n{sid} ({stamp}; exact JSON sha256 {sha}). FLOAT (MID 32): {mid32}. {h18}")
print('NUMERICS_FINAL sha256', hashlib.sha256(open(p,'rb').read()).hexdigest()[:16])
